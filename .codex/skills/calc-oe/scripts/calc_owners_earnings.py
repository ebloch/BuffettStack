#!/usr/bin/env python3
"""Calculate historical owner's earnings from financial statement JSON."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


BUSINESS_TYPES = {
    "general-operating": {
        "formula": "Net Income + D&A - Maint Capex - SBC",
        "default_maint_capex_rate": 0.5,
    },
    "insurance": {
        "formula": "Net Income - SBC",
        "default_maint_capex_rate": 0.0,
    },
    "reit": {
        "formula": "Operating Cash Flow - Maint Capex - SBC (FFO/AFFO proxy unless manually adjusted)",
        "default_maint_capex_rate": 0.5,
    },
    "bank-lender": {
        "formula": "Net Income - SBC (provision normalization requires manual source-backed adjustment)",
        "default_maint_capex_rate": 0.0,
    },
    "asset-heavy-industrial": {
        "formula": "EBITDA - Maint Capex - SBC - Income Tax Expense",
        "default_maint_capex_rate": 0.6,
    },
    "aircraft-lessor": {
        "formula": "Net Income + D&A - Maint Capex - SBC",
        "default_maint_capex_rate": 0.5,
    },
    "exchange-asset-light": {
        "formula": "Net Income + D&A - Capex - SBC",
        "default_maint_capex_rate": 1.0,
    },
}

META_EXCLUSIONS = (
    "QC Report - ",
    "Gap Analysis - ",
    "Improvement Suggestions - ",
    "Audit Report - ",
    "Owner's Earnings - ",
)


class CalcError(RuntimeError):
    """Raised when owner earnings cannot be calculated."""


@dataclass
class YearCalculation:
    year: str
    revenue: float | None
    operating_income: float | None
    net_income: float | None
    ebitda: float | None
    depreciation_amortization: float | None
    eps_diluted: float | None
    shares_diluted: float | None
    operating_cash_flow: float | None
    capex: float | None
    free_cash_flow: float | None
    stock_based_compensation: float | None
    income_tax: float | None
    starting_metric_name: str
    starting_metric: float | None
    maint_capex: float
    one_time_adjustments: float
    owners_earnings: float | None
    oe_per_share: float | None
    oe_growth_yoy: float | None
    oe_margin: float | None
    sbc_pct_of_oe: float | None
    data_gaps: list[str]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Calculate historical owner's earnings.")
    parser.add_argument("--company", required=True, help="Company folder/name to calculate")
    parser.add_argument("--ticker", help="Ticker override")
    parser.add_argument("--business-type", required=True, choices=sorted(BUSINESS_TYPES))
    parser.add_argument("--maint-capex-rate", type=float, help="Maintenance capex as decimal share of total capex")
    parser.add_argument("--research-base", help="Override RESEARCH_BASE_PATH")
    parser.add_argument("--timestamp", help="Filename timestamp override, YYYY-MM-DD-HHMM")
    args = parser.parse_args(argv)
    if args.maint_capex_rate is not None and not 0 <= args.maint_capex_rate <= 1:
        parser.error("--maint-capex-rate must be a decimal between 0 and 1")
    return args


def find_repo_root() -> Path:
    start = Path(__file__).resolve()
    for parent in [start, *start.parents, Path.cwd(), *Path.cwd().parents]:
        if (parent / ".claude" / "settings.local.json").exists():
            return parent
    raise CalcError("Could not find .claude/settings.local.json")


def load_research_base(override: str | None = None) -> Path:
    if override:
        return Path(override).expanduser()
    settings_path = find_repo_root() / ".claude" / "settings.local.json"
    settings = json.loads(settings_path.read_text())
    base = settings.get("env", {}).get("RESEARCH_BASE_PATH")
    if not base:
        raise CalcError("RESEARCH_BASE_PATH missing from .claude/settings.local.json")
    return Path(base).expanduser()


def normalize_name(value: str) -> str:
    value = value.lower()
    value = re.sub(r"\b(incorporated|inc|corp|corporation|company|co|ltd|limited|plc|sa|ag|nv)\b\.?", "", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def resolve_company_dir(research_base: Path, company: str, ticker: str | None = None) -> Path:
    if not research_base.exists():
        raise CalcError(f"Research base does not exist: {research_base}")

    target_norm = normalize_name(company)
    ticker_norm = ticker.lower() if ticker else company.lower()
    candidates = [path for path in research_base.iterdir() if path.is_dir()]
    for path in candidates:
        if path.name == company:
            return path
    for path in candidates:
        path_norm = normalize_name(path.name)
        if path_norm == target_norm:
            return path
    for path in candidates:
        path_norm = normalize_name(path.name)
        if target_norm and (target_norm.startswith(path_norm) or path_norm.startswith(target_norm)):
            return path
        if path.name.lower() == ticker_norm:
            return path
    raise CalcError(f"Could not resolve company folder under {research_base}: {company}")


def read_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    frontmatter = text[3:end]
    data: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("\"'")
    return data


def extract_year_from_memo(path: Path) -> str | None:
    text = path.read_text(errors="ignore")
    frontmatter = read_frontmatter(text)
    fiscal_year = frontmatter.get("fiscal_year") or frontmatter.get("year")
    if fiscal_year:
        match = re.search(r"\d{4}", fiscal_year)
        if match:
            return match.group(0)
    match = re.search(r"FY\s*(\d{4})", path.name, re.IGNORECASE)
    return match.group(1) if match else None


def extract_ticker_from_memo(path: Path) -> str | None:
    frontmatter = read_frontmatter(path.read_text(errors="ignore"))
    ticker = frontmatter.get("ticker")
    return ticker.upper() if ticker else None


def find_annual_memos(company_dir: Path) -> dict[str, Path]:
    filings_dir = company_dir / "1.1-Annual-Filings"
    if not filings_dir.exists():
        return {}
    memos: dict[str, Path] = {}
    for path in sorted(filings_dir.glob("*Synthesis - Memo*.md")):
        if any(token in path.name for token in META_EXCLUSIONS):
            continue
        year = extract_year_from_memo(path)
        if year:
            memos[year] = path
    return dict(sorted(memos.items()))


def find_latest_business_economics(company_dir: Path) -> Path | None:
    biz_dir = company_dir / "2.1-Business-Economics"
    if not biz_dir.exists():
        return None
    files = [path for path in biz_dir.glob("Business Economics Analysis - *.md") if not any(token in path.name for token in META_EXCLUSIONS)]
    return sorted(files)[-1] if files else None


def find_statement_json(company_dir: Path, suffix: str, ticker: str | None = None) -> Path:
    financial_dir = company_dir / "1.3-Financial-Statements"
    if not financial_dir.exists():
        raise CalcError(f"Missing financial statements directory: {financial_dir}")
    patterns = [f"{ticker.upper()}-{suffix}.json"] if ticker else []
    patterns.append(f"*-{suffix}.json")
    for pattern in patterns:
        matches = sorted(financial_dir.glob(pattern))
        if matches:
            return matches[-1]
    raise CalcError(f"Missing *-{suffix}.json in {financial_dir}")


def load_statement(path: Path) -> dict[str, dict[str, Any]]:
    payload = json.loads(path.read_text())
    if isinstance(payload, dict) and "annual" in payload:
        annual = payload.get("annual") or {}
        return {str(year): row for year, row in annual.items() if isinstance(row, dict)}
    if isinstance(payload, list):
        rows: dict[str, dict[str, Any]] = {}
        for row in payload:
            if not isinstance(row, dict):
                continue
            year = str(row.get("fiscalYear") or row.get("calendarYear") or str(row.get("date", ""))[:4])
            if year and year != "None":
                rows[year] = row
        return rows
    raise CalcError(f"Unsupported statement JSON shape: {path}")


def get_value(row: dict[str, Any] | None, *keys: str) -> float | None:
    if not row:
        return None
    for key in keys:
        value = row.get(key)
        if value is None:
            continue
        try:
            return float(value)
        except (TypeError, ValueError):
            continue
    return None


def calc_cagr(first: float | None, last: float | None, periods: int) -> float | None:
    if first is None or last is None or first <= 0 or last <= 0 or periods <= 0:
        return None
    return (last / first) ** (1 / periods) - 1


def pct(current: float | None, base: float | None) -> float | None:
    if current is None or base in (None, 0):
        return None
    return current / base


def calculate_year(
    year: str,
    business_type: str,
    maint_capex_rate: float,
    income_row: dict[str, Any] | None,
    cash_row: dict[str, Any] | None,
) -> YearCalculation:
    revenue = get_value(income_row, "revenue")
    operating_income = get_value(income_row, "operating_income", "operatingIncome")
    net_income = get_value(income_row, "net_income", "netIncome")
    ebitda = get_value(income_row, "ebitda")
    income_tax = get_value(income_row, "income_tax", "incomeTaxExpense")
    depreciation = get_value(
        cash_row,
        "depreciation_amortization",
        "depreciationAndAmortization",
        "depreciation_and_amortization",
    )
    if depreciation is None:
        depreciation = get_value(income_row, "depreciation_amortization", "depreciationAndAmortization")
    eps_diluted = get_value(income_row, "eps_diluted", "epsdiluted")
    shares_diluted = get_value(
        income_row,
        "shares_diluted",
        "weightedAverageShsOutDil",
        "weighted_average_shs_out_dil",
    )
    operating_cash_flow = get_value(cash_row, "operating_cash_flow", "operatingCashFlow")
    capex = get_value(cash_row, "capex", "capitalExpenditure", "capital_expenditure")
    free_cash_flow = get_value(cash_row, "free_cash_flow", "freeCashFlow")
    sbc = get_value(cash_row, "stock_based_compensation", "stockBasedCompensation")

    data_gaps: list[str] = []
    if net_income is None:
        data_gaps.append("net income missing")
    if shares_diluted in (None, 0):
        data_gaps.append("diluted shares missing")
    if sbc is None:
        data_gaps.append("SBC missing; treated as 0 until source-reviewed")
        sbc_value = 0.0
    else:
        sbc_value = sbc

    capex_value = abs(capex) if capex is not None else 0.0
    maint_capex = capex_value * maint_capex_rate
    one_time_adjustments = 0.0
    starting_metric_name = "Net Income"
    starting_metric = net_income
    owners_earnings: float | None

    if business_type in ("general-operating", "aircraft-lessor", "exchange-asset-light"):
        d_and_a = depreciation or 0.0
        if depreciation is None:
            data_gaps.append("D&A missing; treated as 0")
        owners_earnings = None if net_income is None else net_income + d_and_a - maint_capex - sbc_value + one_time_adjustments
    elif business_type == "insurance":
        owners_earnings = None if net_income is None else net_income - sbc_value + one_time_adjustments
    elif business_type == "bank-lender":
        data_gaps.append("provision normalization not applied by script")
        owners_earnings = None if net_income is None else net_income - sbc_value + one_time_adjustments
    elif business_type == "reit":
        starting_metric_name = "Operating Cash Flow proxy"
        starting_metric = operating_cash_flow
        data_gaps.append("FFO/AFFO not available in generic statement JSON; OCF proxy requires review")
        owners_earnings = None if operating_cash_flow is None else operating_cash_flow - maint_capex - sbc_value + one_time_adjustments
    elif business_type == "asset-heavy-industrial":
        starting_metric_name = "EBITDA"
        starting_metric = ebitda
        tax_value = income_tax or 0.0
        if ebitda is None:
            data_gaps.append("EBITDA missing")
        if income_tax is None:
            data_gaps.append("income tax missing; treated as 0")
        owners_earnings = None if ebitda is None else ebitda - maint_capex - sbc_value - tax_value + one_time_adjustments
    else:
        raise CalcError(f"Unsupported business type: {business_type}")

    oe_per_share = None
    if owners_earnings is not None and shares_diluted not in (None, 0):
        oe_per_share = owners_earnings / shares_diluted

    return YearCalculation(
        year=year,
        revenue=revenue,
        operating_income=operating_income,
        net_income=net_income,
        ebitda=ebitda,
        depreciation_amortization=depreciation,
        eps_diluted=eps_diluted,
        shares_diluted=shares_diluted,
        operating_cash_flow=operating_cash_flow,
        capex=capex,
        free_cash_flow=free_cash_flow,
        stock_based_compensation=sbc,
        income_tax=income_tax,
        starting_metric_name=starting_metric_name,
        starting_metric=starting_metric,
        maint_capex=maint_capex,
        one_time_adjustments=one_time_adjustments,
        owners_earnings=owners_earnings,
        oe_per_share=oe_per_share,
        oe_growth_yoy=None,
        oe_margin=pct(owners_earnings, revenue),
        sbc_pct_of_oe=pct(sbc_value, owners_earnings),
        data_gaps=data_gaps,
    )


def calculate_all(
    years: list[str],
    business_type: str,
    maint_capex_rate: float,
    income: dict[str, dict[str, Any]],
    cash: dict[str, dict[str, Any]],
) -> list[YearCalculation]:
    calculations = [
        calculate_year(year, business_type, maint_capex_rate, income.get(year), cash.get(year))
        for year in years
    ]
    previous_oe: float | None = None
    for calc in calculations:
        calc.oe_growth_yoy = pct(
            None if calc.owners_earnings is None or previous_oe is None else calc.owners_earnings - previous_oe,
            previous_oe,
        )
        if calc.owners_earnings is not None:
            previous_oe = calc.owners_earnings
    return calculations


def fmt_money_m(value: float | None) -> str:
    if value is None:
        return ""
    amount = value / 1_000_000
    if amount < 0:
        return f"({abs(amount):,.0f})"
    return f"{amount:,.0f}"


def fmt_dollar(value: float | None) -> str:
    if value is None:
        return ""
    return f"${value:,.2f}"


def fmt_pct(value: float | None) -> str:
    if value is None:
        return ""
    return f"{value * 100:.1f}%"


def fmt_shares_m(value: float | None) -> str:
    if value is None:
        return ""
    return f"{value / 1_000_000:,.1f}"


def row(label: str, values: list[str], source: str | None = None) -> str:
    cells = [label, *values]
    if source is not None:
        cells.append(source)
    return "| " + " | ".join(cells) + " |"


def build_table(headers: list[str], rows: list[str]) -> list[str]:
    return [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" if i == 0 else "---:" for i in range(len(headers))) + " |",
        *rows,
    ]


def average(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def build_markdown(
    company: str,
    ticker: str,
    business_type: str,
    maint_capex_rate: float,
    calculations: list[YearCalculation],
    income_path: Path,
    cash_path: Path,
    memo_paths: dict[str, Path],
    business_economics_path: Path | None,
    output_date: str,
) -> str:
    years = [calc.year for calc in calculations]
    fy_headers = [f"FY{year}" for year in years]
    formula = BUSINESS_TYPES[business_type]["formula"]
    oe_values = [calc.owners_earnings for calc in calculations]
    cagr = calc_cagr(oe_values[0] if oe_values else None, oe_values[-1] if oe_values else None, max(len(oe_values) - 1, 0))
    avg_margin = average([calc.oe_margin for calc in calculations if calc.oe_margin is not None])
    latest = calculations[-1] if calculations else None

    lines = [
        f"# {company} - Owner's Earnings",
        "",
        f"**Date:** {output_date}",
        f"**Ticker:** {ticker}",
        f"**Business Type:** {business_type}",
        f"**OE Formula:** {formula}",
        f"**Fiscal Years:** FY{years[0]}-FY{years[-1]}" if years else "**Fiscal Years:**",
        "",
        "---",
        "",
        "## Summary",
        "",
    ]
    summary_rows = [
        row("Total OE ($M)", [fmt_money_m(calc.owners_earnings) for calc in calculations]),
        row("OE per Share", [fmt_dollar(calc.oe_per_share) for calc in calculations]),
        row("OE Growth YoY", [fmt_pct(calc.oe_growth_yoy) for calc in calculations]),
        row("OE Margin (OE/Rev)", [fmt_pct(calc.oe_margin) for calc in calculations]),
        row("SBC ($M)", [fmt_money_m(calc.stock_based_compensation) for calc in calculations]),
        row("SBC % of OE", [fmt_pct(calc.sbc_pct_of_oe) for calc in calculations]),
    ]
    lines.extend(build_table(["Metric", *fy_headers], summary_rows))
    lines.extend(
        [
            "",
            f"**OE CAGR:** {fmt_pct(cagr)}",
            f"**Average OE Margin:** {fmt_pct(avg_margin)}",
            "",
            "---",
            "",
            "## OE Calculation Detail",
            "",
        ]
    )

    detail_rows = [
        row(calculations[0].starting_metric_name if calculations else "Starting metric", [fmt_money_m(calc.starting_metric) for calc in calculations], "Income Statement / Cash Flow"),
        row("+ D&A", [fmt_money_m(calc.depreciation_amortization) for calc in calculations], "Cash Flow / Income Statement"),
        row("- Maint Capex", [fmt_money_m(calc.maint_capex) for calc in calculations], f"EST: {maint_capex_rate * 100:.0f}% of total capex"),
        row("- SBC", [fmt_money_m(calc.stock_based_compensation) for calc in calculations], "Cash Flow JSON unless source-overridden"),
        row("+/- One-time adjustments", [fmt_money_m(calc.one_time_adjustments) for calc in calculations], "None applied by script"),
        row("= Owner's Earnings", [fmt_money_m(calc.owners_earnings) for calc in calculations], ""),
        row("Diluted Shares (M)", [fmt_shares_m(calc.shares_diluted) for calc in calculations], "Income Statement"),
        row("OE per Share", [fmt_dollar(calc.oe_per_share) for calc in calculations], ""),
    ]
    lines.extend(build_table(["Component", *fy_headers, "Source"], detail_rows))
    lines.extend(["", "---", "", "## Input Data", "", "### Income Statement Extract", ""])

    income_rows = [
        row("Revenue", [fmt_money_m(calc.revenue) for calc in calculations]),
        row("Operating Income", [fmt_money_m(calc.operating_income) for calc in calculations]),
        row("Net Income", [fmt_money_m(calc.net_income) for calc in calculations]),
        row("EBITDA", [fmt_money_m(calc.ebitda) for calc in calculations]),
        row("D&A", [fmt_money_m(calc.depreciation_amortization) for calc in calculations]),
        row("EPS (Diluted)", [fmt_dollar(calc.eps_diluted) for calc in calculations]),
        row("Diluted Shares (M)", [fmt_shares_m(calc.shares_diluted) for calc in calculations]),
    ]
    lines.extend(build_table(["Line Item", *fy_headers], income_rows))
    lines.extend(["", "### Cash Flow Extract", ""])
    cash_rows = [
        row("Operating Cash Flow", [fmt_money_m(calc.operating_cash_flow) for calc in calculations]),
        row("Capital Expenditure", [fmt_money_m(calc.capex) for calc in calculations]),
        row("Free Cash Flow", [fmt_money_m(calc.free_cash_flow) for calc in calculations]),
        row("Stock-Based Compensation", [fmt_money_m(calc.stock_based_compensation) for calc in calculations]),
    ]
    lines.extend(build_table(["Line Item", *fy_headers], cash_rows))
    lines.extend(
        [
            "",
            "---",
            "",
            "## One-Time Adjustments",
            "",
            "No material one-time items were identified by the deterministic script. Add source-backed adjustments after reviewing annual-filing memos.",
            "",
            "| Year | Item | Amount ($M) | Action | Rationale |",
            "|---|---|---:|---|---|",
            "",
            "---",
            "",
            "## Key Assumptions & Notes",
            "",
            "### Business Type Rationale",
            "",
            f"Classified as `{business_type}`. Confirm this against Business Economics and annual-filing memos before relying on the output.",
            "",
            "### OE Formula Rationale",
            "",
            f"Applied formula: {formula}.",
            "",
            "### Maintenance Capex",
            "",
            f"Maintenance capex estimated at {maint_capex_rate * 100:.0f}% of total capital expenditure. Update this if company disclosures support a better split.",
            "",
            "### SBC Source",
            "",
            "SBC is sourced from cash flow statement JSON. Years with blank or zero SBC require source review against the 10-K memo.",
            "",
            "### Data Gaps",
            "",
        ]
    )
    gaps = [f"- FY{calc.year}: {gap}" for calc in calculations for gap in calc.data_gaps]
    lines.extend(gaps or ["No deterministic data gaps identified."])
    lines.extend(["", "---", "", "## Cross-Check", "", "### vs. Business Economics Section 8", ""])
    if business_economics_path:
        lines.extend(
            [
                f"Business Economics file available for manual cross-check: `{business_economics_path}`",
                "",
                "| Metric | This Calculation | Biz Econ Section 8 | Difference | Explanation |",
                "|---|---:|---:|---:|---|",
                f"| Owner's Earnings ($M) | {fmt_money_m(latest.owners_earnings) if latest else ''} |  |  | Pending manual cross-check |",
                f"| OE per Share | {fmt_dollar(latest.oe_per_share) if latest else ''} |  |  | Pending manual cross-check |",
            ]
        )
    else:
        lines.append("No Business Economics analysis available for cross-check.")
    lines.extend(["", "### vs. Free Cash Flow", ""])
    if latest:
        fcf_difference = None
        if latest.owners_earnings is not None and latest.free_cash_flow is not None:
            fcf_difference = latest.owners_earnings - latest.free_cash_flow
        fcf_rows = [
            row("Owner's Earnings", [fmt_money_m(latest.owners_earnings)]),
            row("Reported FCF", [fmt_money_m(latest.free_cash_flow)]),
            row("Difference", [fmt_money_m(fcf_difference)]),
            row("Explanation", ["Review working capital, growth capex, and formula-specific adjustments."]),
        ]
        lines.extend(build_table(["Metric", f"FY{latest.year}"], fcf_rows))
    lines.extend(["", "---", "", "## Sources", ""])
    lines.append(f"- Income Statement: `{income_path}`")
    lines.append(f"- Cash Flow Statement: `{cash_path}`")
    lines.append("- Annual Filing Memos:")
    for year, path in memo_paths.items():
        lines.append(f"  - FY{year}: `{path}`")
    if business_economics_path:
        lines.append(f"- Business Economics: `{business_economics_path}`")
    return "\n".join(lines) + "\n"


def infer_ticker(cli_ticker: str | None, income_path: Path, memo_paths: dict[str, Path]) -> str:
    if cli_ticker:
        return cli_ticker.upper()
    try:
        payload = json.loads(income_path.read_text())
        ticker = payload.get("metadata", {}).get("ticker")
        if ticker:
            return str(ticker).upper()
    except Exception:
        pass
    if memo_paths:
        ticker = extract_ticker_from_memo(list(memo_paths.values())[-1])
        if ticker:
            return ticker
    match = re.match(r"([A-Za-z0-9.\-]+)-income-statement\.json", income_path.name)
    if match:
        return match.group(1).upper()
    return "UNKNOWN"


def execute(args: argparse.Namespace) -> dict[str, Any]:
    research_base = load_research_base(args.research_base)
    company_dir = resolve_company_dir(research_base, args.company, args.ticker)
    memo_paths = find_annual_memos(company_dir)
    if not memo_paths:
        raise CalcError(f"No annual-filing synthesis memos found under {company_dir / '1.1-Annual-Filings'}")

    income_path = find_statement_json(company_dir, "income-statement", args.ticker)
    cash_path = find_statement_json(company_dir, "cash-flow", args.ticker)
    income = load_statement(income_path)
    cash = load_statement(cash_path)
    ticker = infer_ticker(args.ticker, income_path, memo_paths)
    years = sorted(memo_paths)
    available_years = [year for year in years if year in income or year in cash]
    if not available_years:
        raise CalcError("Financial JSON does not overlap annual-filing memo years")

    maint_capex_rate = (
        args.maint_capex_rate
        if args.maint_capex_rate is not None
        else BUSINESS_TYPES[args.business_type]["default_maint_capex_rate"]
    )
    calculations = calculate_all(available_years, args.business_type, maint_capex_rate, income, cash)
    timestamp = args.timestamp or datetime.now().strftime("%Y-%m-%d-%H%M")
    output_date = timestamp[:10]
    business_economics_path = find_latest_business_economics(company_dir)
    financial_dir = company_dir / "1.3-Financial-Statements"
    output_path = financial_dir / f"Owner's Earnings - {company_dir.name} - {timestamp}.md"
    output_path.write_text(
        build_markdown(
            company=company_dir.name,
            ticker=ticker,
            business_type=args.business_type,
            maint_capex_rate=maint_capex_rate,
            calculations=calculations,
            income_path=income_path,
            cash_path=cash_path,
            memo_paths={year: memo_paths[year] for year in available_years},
            business_economics_path=business_economics_path,
            output_date=output_date,
        )
    )
    missing_years = [year for year in years if year not in available_years]
    return {
        "company": company_dir.name,
        "ticker": ticker,
        "business_type": args.business_type,
        "maint_capex_rate": maint_capex_rate,
        "years_calculated": available_years,
        "missing_years": missing_years,
        "output_path": str(output_path),
        "income_statement_path": str(income_path),
        "cash_flow_path": str(cash_path),
    }


def main(argv: list[str] | None = None) -> int:
    try:
        result = execute(parse_args(argv or sys.argv[1:]))
    except CalcError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
