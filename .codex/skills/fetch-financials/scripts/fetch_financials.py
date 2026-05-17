#!/usr/bin/env python3
"""Fetch, normalize, merge, and summarize FMP financial statements."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


STATEMENTS = {
    "income-statement": {
        "file_suffix": "income-statement",
        "title": "Income Statement",
        "fmp_command": "income-statement",
        "fields": {
            "revenue": "revenue",
            "cost_of_revenue": "costOfRevenue",
            "gross_profit": "grossProfit",
            "gross_margin": "grossProfitRatio",
            "operating_expenses": "operatingExpenses",
            "operating_income": "operatingIncome",
            "operating_margin": "operatingIncomeRatio",
            "interest_expense": "interestExpense",
            "other_income": "totalOtherIncomeExpensesNet",
            "pretax_income": "incomeBeforeTax",
            "income_tax": "incomeTaxExpense",
            "net_income": "netIncome",
            "net_margin": "netIncomeRatio",
            "eps_basic": "eps",
            "eps_diluted": "epsdiluted",
            "shares_basic": "weightedAverageShsOut",
            "shares_diluted": "weightedAverageShsOutDil",
            "ebitda": "ebitda",
            "ebitda_margin": "ebitdaratio",
        },
    },
    "balance-sheet": {
        "file_suffix": "balance-sheet",
        "title": "Balance Sheet",
        "fmp_command": "balance-sheet",
        "fields": {
            "cash_and_equivalents": "cashAndCashEquivalents",
            "short_term_investments": "shortTermInvestments",
            "total_cash": "cashAndShortTermInvestments",
            "accounts_receivable": "netReceivables",
            "inventory": "inventory",
            "total_current_assets": "totalCurrentAssets",
            "pp_and_e": "propertyPlantEquipmentNet",
            "goodwill": "goodwill",
            "intangibles": "intangibleAssets",
            "total_assets": "totalAssets",
            "accounts_payable": "accountPayables",
            "short_term_debt": "shortTermDebt",
            "total_current_liabilities": "totalCurrentLiabilities",
            "long_term_debt": "longTermDebt",
            "total_debt": "totalDebt",
            "total_liabilities": "totalLiabilities",
            "retained_earnings": "retainedEarnings",
            "total_equity": "totalStockholdersEquity",
        },
    },
    "cash-flow": {
        "file_suffix": "cash-flow",
        "title": "Cash Flow",
        "fmp_command": "cash-flow",
        "fields": {
            "net_income": "netIncome",
            "depreciation_amortization": "depreciationAndAmortization",
            "stock_based_compensation": "stockBasedCompensation",
            "change_working_capital": "changeInWorkingCapital",
            "change_receivables": "accountsReceivables",
            "change_inventory": "inventory",
            "change_payables": "accountsPayables",
            "operating_cash_flow": "operatingCashFlow",
            "capex": "capitalExpenditure",
            "acquisitions": "acquisitionsNet",
            "asset_sales": "purchasesOfInvestments",
            "investing_cash_flow": "netCashUsedForInvestingActivites",
            "dividends_paid": "dividendsPaid",
            "share_repurchases": "commonStockRepurchased",
            "debt_repayment": "debtRepayment",
            "debt_issued": "debtRepayment",
            "financing_cash_flow": "netCashUsedProvidedByFinancingActivities",
            "free_cash_flow": "freeCashFlow",
            "net_change_in_cash": "netChangeInCash",
        },
    },
}

TABLES = {
    "income-statement": [
        ("Year", "year"),
        ("Revenue", "revenue"),
        ("Cost of Rev", "cost_of_revenue"),
        ("Gross Profit", "gross_profit"),
        ("Op Expenses", "operating_expenses"),
        ("Op Income", "operating_income"),
        ("Interest Exp", "interest_expense"),
        ("Pretax Income", "pretax_income"),
        ("Income Tax", "income_tax"),
        ("Net Income", "net_income"),
        ("EPS Diluted", "eps_diluted"),
        ("Shares Dil", "shares_diluted"),
        ("EBITDA", "ebitda"),
    ],
    "balance-sheet": [
        ("Year", "year"),
        ("Cash", "cash_and_equivalents"),
        ("ST Invest", "short_term_investments"),
        ("Total Cash", "total_cash"),
        ("Receivables", "accounts_receivable"),
        ("Inventory", "inventory"),
        ("Curr Assets", "total_current_assets"),
        ("PP&E", "pp_and_e"),
        ("Goodwill", "goodwill"),
        ("Total Assets", "total_assets"),
        ("Payables", "accounts_payable"),
        ("ST Debt", "short_term_debt"),
        ("LT Debt", "long_term_debt"),
        ("Total Debt", "total_debt"),
        ("Total Liab", "total_liabilities"),
        ("Total Equity", "total_equity"),
    ],
    "cash-flow": [
        ("Year", "year"),
        ("Net Income", "net_income"),
        ("D&A", "depreciation_amortization"),
        ("Stock Comp", "stock_based_compensation"),
        ("Delta WC", "change_working_capital"),
        ("Op CF", "operating_cash_flow"),
        ("CapEx", "capex"),
        ("Acquisitions", "acquisitions"),
        ("Invest CF", "investing_cash_flow"),
        ("Dividends", "dividends_paid"),
        ("Buybacks", "share_repurchases"),
        ("Debt Repay", "debt_repayment"),
        ("Fin CF", "financing_cash_flow"),
        ("FCF", "free_cash_flow"),
        ("Net Delta Cash", "net_change_in_cash"),
    ],
}


class FetchError(RuntimeError):
    """Raised when fetching or parsing FMP data fails."""


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch FMP financial statements.")
    parser.add_argument("ticker", help="Stock ticker, e.g. CME or AAPL")
    parser.add_argument("--quarterly", action="store_true", help="Also fetch 20 quarters")
    parser.add_argument("--force", action="store_true", help="Ignore existing cached JSON")
    parser.add_argument("--research-base", help="Override RESEARCH_BASE_PATH")
    return parser.parse_args(argv)


def find_repo_root() -> Path:
    candidates = [Path.cwd(), Path(__file__).resolve()]
    for candidate in candidates:
        for parent in [candidate, *candidate.parents]:
            if (parent / ".claude" / "settings.local.json").exists():
                return parent
    raise FetchError("Could not find .claude/settings.local.json")


def load_research_base(override: str | None = None) -> Path:
    if override:
        return Path(override).expanduser()

    settings_path = find_repo_root() / ".claude" / "settings.local.json"
    settings = json.loads(settings_path.read_text())
    base = settings.get("env", {}).get("RESEARCH_BASE_PATH")
    if not base:
        raise FetchError("RESEARCH_BASE_PATH missing from .claude/settings.local.json")
    return Path(base).expanduser()


def normalize_company_name(value: str) -> str:
    cleaned = value.lower()
    cleaned = re.sub(r"\b(incorporated|inc|corp|corporation|company|co|ltd|limited|plc|sa|ag|nv)\b\.?", "", cleaned)
    cleaned = re.sub(r"[^a-z0-9]+", " ", cleaned)
    return " ".join(cleaned.split())


def safe_folder_name(value: str) -> str:
    cleaned = re.sub(r"[/:\\]+", "-", value).strip()
    return cleaned or "Unknown Company"


def resolve_company_dir(research_base: Path, company_name: str, ticker: str) -> Path:
    target_norm = normalize_company_name(company_name)
    ticker_norm = ticker.lower()

    if not research_base.exists():
        return research_base / safe_folder_name(company_name)

    dirs = [path for path in research_base.iterdir() if path.is_dir()]
    for path in dirs:
        if path.name == company_name:
            return path

    for path in dirs:
        path_norm = normalize_company_name(path.name)
        if path_norm == target_norm:
            return path

    for path in dirs:
        path_norm = normalize_company_name(path.name)
        if target_norm and (target_norm.startswith(path_norm) or path_norm.startswith(target_norm)):
            return path
        if ticker_norm and ticker_norm == path.name.lower():
            return path

    return research_base / safe_folder_name(company_name)


def run_fmp(script_path: Path, *args: str) -> Any:
    result = subprocess.run(
        [str(script_path), *args],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise FetchError(result.stderr.strip() or f"FMP command failed: {' '.join(args)}")
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise FetchError(f"FMP returned invalid JSON for {' '.join(args)}") from exc


def parse_profile(profile_response: Any, ticker: str) -> dict[str, Any]:
    if isinstance(profile_response, list):
        profile = profile_response[0] if profile_response else {}
    elif isinstance(profile_response, dict):
        profile = profile_response
    else:
        profile = {}

    return {
        "ticker": ticker.upper(),
        "company_name": profile.get("companyName") or profile.get("company_name") or ticker.upper(),
        "currency": profile.get("currency") or profile.get("currencySymbol") or "USD",
    }


def period_key(record: dict[str, Any], period_type: str) -> str:
    fiscal_year = str(record.get("fiscalYear") or record.get("calendarYear") or "")
    if not fiscal_year:
        date = str(record.get("date") or "")
        fiscal_year = date[:4]
    if not fiscal_year:
        raise ValueError("Record missing fiscal year/date")

    if period_type == "annual":
        return fiscal_year

    period = str(record.get("period") or "").upper()
    if not period or period == "FY":
        period = "Q4"
    return f"{fiscal_year}-{period}"


def sort_period_keys(keys: list[str]) -> list[str]:
    def key_parts(key: str) -> tuple[int, int]:
        match = re.match(r"^(\d{4})(?:-Q([1-4]))?$", key)
        if not match:
            return (0, 0)
        year = int(match.group(1))
        quarter = int(match.group(2) or 0)
        return (year, quarter)

    return sorted(keys, key=key_parts, reverse=True)


def transform_records(
    records: Any,
    statement_name: str,
    period_type: str,
) -> dict[str, dict[str, Any]]:
    if not isinstance(records, list):
        raise FetchError(f"{statement_name} {period_type} response was not a JSON array")

    fields = STATEMENTS[statement_name]["fields"]
    output: dict[str, dict[str, Any]] = {}
    for record in records:
        if not isinstance(record, dict):
            continue
        try:
            key = period_key(record, period_type)
        except ValueError:
            continue
        row = {
            "date": record.get("date"),
            "fiscal_year": str(record.get("fiscalYear") or record.get("calendarYear") or key[:4]),
        }
        if period_type == "quarterly":
            row["period"] = record.get("period")
        for output_field, fmp_field in fields.items():
            row[output_field] = record.get(fmp_field)
        output[key] = row

    return {key: output[key] for key in sort_period_keys(list(output.keys()))}


def build_statement_payload(
    ticker: str,
    company_name: str,
    currency: str,
    statement_name: str,
    annual_records: Any,
    quarterly_records: Any | None,
    last_updated: str,
) -> dict[str, Any]:
    payload = {
        "metadata": {
            "ticker": ticker.upper(),
            "company_name": company_name,
            "last_updated": last_updated,
            "data_source": "FMP API",
            "currency": currency,
            "statement": statement_name,
        },
        "annual": transform_records(annual_records, statement_name, "annual"),
        "quarterly": {},
    }
    if quarterly_records is not None:
        payload["quarterly"] = transform_records(quarterly_records, statement_name, "quarterly")
    return payload


def merge_payload(existing: dict[str, Any] | None, fresh: dict[str, Any], force: bool) -> dict[str, Any]:
    if force or not existing:
        return fresh

    merged = {
        "metadata": {**existing.get("metadata", {}), **fresh.get("metadata", {})},
        "annual": dict(existing.get("annual", {})),
        "quarterly": dict(existing.get("quarterly", {})),
    }
    merged["annual"].update(fresh.get("annual", {}))
    merged["quarterly"].update(fresh.get("quarterly", {}))
    merged["annual"] = {key: merged["annual"][key] for key in sort_period_keys(list(merged["annual"].keys()))}
    merged["quarterly"] = {key: merged["quarterly"][key] for key in sort_period_keys(list(merged["quarterly"].keys()))}
    return merged


def read_existing(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text())


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n")


def format_money(value: Any) -> str:
    if value is None:
        return ""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return ""
    sign_open = "(" if number < 0 else ""
    sign_close = ")" if number < 0 else ""
    number = abs(number)
    if number >= 1_000_000_000_000:
        return f"{sign_open}${number / 1_000_000_000_000:.1f}T{sign_close}"
    if number >= 1_000_000_000:
        return f"{sign_open}${number / 1_000_000_000:.1f}B{sign_close}"
    if number >= 1_000_000:
        return f"{sign_open}${number / 1_000_000:.0f}m{sign_close}"
    return f"{sign_open}${number:,.0f}{sign_close}"


def format_number(value: Any) -> str:
    if value is None:
        return ""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return ""
    if abs(number) >= 1_000_000_000:
        return f"{number / 1_000_000_000:.1f}B"
    if abs(number) >= 1_000_000:
        return f"{number / 1_000_000:.0f}m"
    return f"{number:,.1f}"


def format_percent(value: Any) -> str:
    if value is None:
        return ""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return ""
    if abs(number) <= 1:
        number *= 100
    return f"{number:.1f}%"


def format_cell(field: str, value: Any) -> str:
    if field == "year":
        return str(value)
    if field.startswith("eps"):
        return "" if value is None else f"${float(value):.2f}"
    if "margin" in field or field.endswith("ratio"):
        return format_percent(value)
    if "shares" in field:
        return format_number(value)
    return format_money(value)


def markdown_table(statement_name: str, payload: dict[str, Any]) -> str:
    columns = TABLES[statement_name]
    lines = [
        "| " + " | ".join(header for header, _ in columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for year, row in payload.get("annual", {}).items():
        cells = []
        for _, field in columns:
            value = year if field == "year" else row.get(field)
            cells.append(format_cell(field, value))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def pct_change(current: float | None, prior: float | None) -> float | None:
    if current is None or prior in (None, 0):
        return None
    return (current - prior) / abs(prior)


def as_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def trend_label(values: list[float]) -> str:
    if len(values) < 2:
        return "flat"
    delta = values[0] - values[-1]
    if abs(delta) <= 0.01:
        return "flat"
    return "up" if delta > 0 else "down"


def average(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def build_key_metrics(
    income_payload: dict[str, Any],
    balance_payload: dict[str, Any],
    cash_payload: dict[str, Any],
) -> list[tuple[str, str, str, str]]:
    income_rows = list(income_payload.get("annual", {}).items())
    balance_rows = dict(balance_payload.get("annual", {}))
    cash_rows = dict(cash_payload.get("annual", {}))

    revenue_growth: list[float] = []
    operating_margins: list[float] = []
    net_margins: list[float] = []
    fcf_revenue: list[float] = []
    debt_equity: list[float] = []

    for index, (year, row) in enumerate(income_rows[:5]):
        revenue = as_float(row.get("revenue"))
        operating_margin = as_float(row.get("operating_margin"))
        net_margin = as_float(row.get("net_margin"))
        fcf = as_float(cash_rows.get(year, {}).get("free_cash_flow"))
        total_debt = as_float(balance_rows.get(year, {}).get("total_debt"))
        total_equity = as_float(balance_rows.get(year, {}).get("total_equity"))

        if index + 1 < len(income_rows):
            prior_revenue = as_float(income_rows[index + 1][1].get("revenue"))
            growth = pct_change(revenue, prior_revenue)
            if growth is not None:
                revenue_growth.append(growth)
        if operating_margin is not None:
            operating_margins.append(operating_margin)
        if net_margin is not None:
            net_margins.append(net_margin)
        if revenue not in (None, 0) and fcf is not None:
            fcf_revenue.append(fcf / revenue)
        if total_equity not in (None, 0) and total_debt is not None:
            debt_equity.append(total_debt / total_equity)

    rows = [
        ("Revenue Growth", revenue_growth, "percent"),
        ("Operating Margin", operating_margins, "percent"),
        ("Net Margin", net_margins, "percent"),
        ("FCF/Revenue", fcf_revenue, "percent"),
        ("Debt/Equity", debt_equity, "ratio"),
    ]

    formatted = []
    for label, values, kind in rows:
        latest = values[0] if values else None
        avg = average(values)
        latest_text = format_percent(latest) if kind == "percent" else (f"{latest:.1f}x" if latest is not None else "")
        avg_text = format_percent(avg) if kind == "percent" else (f"{avg:.1f}x" if avg is not None else "")
        formatted.append((label, latest_text, avg_text, trend_label(values)))
    return formatted


def build_markdown(company_name: str, ticker: str, payloads: dict[str, dict[str, Any]]) -> str:
    metadata = payloads["income-statement"]["metadata"]
    annual_years = list(payloads["income-statement"].get("annual", {}).keys())
    quarterly_periods = list(payloads["income-statement"].get("quarterly", {}).keys())

    lines = [
        f"# {company_name} - Financial Statements",
        "",
        f"**Ticker:** {ticker.upper()}",
        f"**Last Updated:** {metadata.get('last_updated', '')}",
        "**Data Source:** FMP API",
        f"**Currency:** {metadata.get('currency', '')}",
        "",
        "### Source Data (JSON)",
        "",
        f"- [[{ticker.upper()}-income-statement.json]]",
        f"- [[{ticker.upper()}-balance-sheet.json]]",
        f"- [[{ticker.upper()}-cash-flow.json]]",
        "",
        "---",
        "",
    ]

    if annual_years:
        lines.append(f"**Annual Coverage:** {annual_years[-1]}-{annual_years[0]}")
    if quarterly_periods:
        lines.append(f"**Quarterly Coverage:** {quarterly_periods[-1]}-{quarterly_periods[0]}")
    if annual_years or quarterly_periods:
        lines.extend(["", "---", ""])

    for statement_name in ("income-statement", "balance-sheet", "cash-flow"):
        lines.extend(
            [
                f"## {STATEMENTS[statement_name]['title']} (Annual)",
                "",
                markdown_table(statement_name, payloads[statement_name]),
                "",
                "---",
                "",
            ]
        )

    metrics = build_key_metrics(
        payloads["income-statement"],
        payloads["balance-sheet"],
        payloads["cash-flow"],
    )
    lines.extend(
        [
            "## Key Metrics",
            "",
            "| Metric | Latest | 5Y Avg | Trend |",
            "|---|---|---|---|",
        ]
    )
    for label, latest, avg, trend in metrics:
        lines.append(f"| {label} | {latest} | {avg} | {trend} |")
    lines.extend(["", "*Data from FMP API. JSON source files in this folder.*", ""])
    return "\n".join(lines)


def fetch_statement(script_path: Path, statement_name: str, ticker: str, period: str, limit: str) -> Any:
    command = STATEMENTS[statement_name]["fmp_command"]
    return run_fmp(script_path, command, ticker.upper(), period, limit)


def execute(args: argparse.Namespace) -> dict[str, Any]:
    ticker = args.ticker.upper()
    skill_dir = Path(__file__).resolve().parents[1]
    script_path = skill_dir / "scripts" / "fmp-financials.sh"
    research_base = load_research_base(args.research_base)

    profile = parse_profile(run_fmp(script_path, "profile", ticker), ticker)
    company_name = profile["company_name"]
    company_dir = resolve_company_dir(research_base, company_name, ticker)
    output_dir = company_dir / "1.3-Financial-Statements"
    output_dir.mkdir(parents=True, exist_ok=True)

    last_updated = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    payloads: dict[str, dict[str, Any]] = {}
    files: list[str] = []

    for statement_name, config in STATEMENTS.items():
        annual = fetch_statement(script_path, statement_name, ticker, "annual", "10")
        quarterly = fetch_statement(script_path, statement_name, ticker, "quarterly", "20") if args.quarterly else None
        fresh = build_statement_payload(
            ticker,
            company_name,
            profile["currency"],
            statement_name,
            annual,
            quarterly,
            last_updated,
        )
        output_path = output_dir / f"{ticker}-{config['file_suffix']}.json"
        payload = merge_payload(read_existing(output_path), fresh, args.force)
        write_json(output_path, payload)
        payloads[statement_name] = payload
        files.append(str(output_path))

    markdown = build_markdown(company_name, ticker, payloads)
    markdown_path = output_dir / f"Financial Statements - {company_name}.md"
    markdown_path.write_text(markdown)
    files.append(str(markdown_path))

    annual_years = list(payloads["income-statement"].get("annual", {}).keys())
    quarterly_periods = list(payloads["income-statement"].get("quarterly", {}).keys())
    return {
        "company_name": company_name,
        "ticker": ticker,
        "output_dir": str(output_dir),
        "annual_years": annual_years,
        "quarterly_periods": quarterly_periods,
        "files": files,
    }


def main(argv: list[str] | None = None) -> int:
    try:
        result = execute(parse_args(argv or sys.argv[1:]))
    except FetchError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
