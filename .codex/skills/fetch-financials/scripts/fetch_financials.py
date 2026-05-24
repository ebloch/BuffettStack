#!/usr/bin/env python3
"""Fetch, normalize, merge, and summarize financial statements."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


DEFAULT_SEC_USER_AGENT = "buffettstack/0.1 research@example.com"
SEC_BASE_URL = "https://data.sec.gov"
SEC_FILES_URL = "https://www.sec.gov/files"
YAHOO_QUOTE_URL = "https://query1.finance.yahoo.com/v7/finance/quote"


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
    """Raised when fetching or parsing financial data fails."""


ANNUAL_FORMS = {"10-K", "10-K/A", "20-F", "20-F/A", "40-F", "40-F/A"}
QUARTERLY_FORMS = {"10-Q", "10-Q/A"}

SEC_FACT_ALIASES = {
    "income-statement": {
        "revenue": [
            ("us-gaap", "RevenueFromContractWithCustomerExcludingAssessedTax"),
            ("us-gaap", "Revenues"),
            ("us-gaap", "SalesRevenueNet"),
            ("ifrs-full", "Revenue"),
        ],
        "cost_of_revenue": [
            ("us-gaap", "CostOfRevenue"),
            ("us-gaap", "CostOfGoodsAndServicesSold"),
            ("ifrs-full", "CostOfSales"),
        ],
        "gross_profit": [("us-gaap", "GrossProfit"), ("ifrs-full", "GrossProfit")],
        "operating_expenses": [
            ("us-gaap", "OperatingExpenses"),
            ("us-gaap", "SellingGeneralAndAdministrativeExpense"),
            ("ifrs-full", "DistributionCosts"),
        ],
        "operating_income": [
            ("us-gaap", "OperatingIncomeLoss"),
            ("ifrs-full", "OperatingProfitLoss"),
        ],
        "interest_expense": [
            ("us-gaap", "InterestExpenseNonOperating"),
            ("us-gaap", "InterestExpense"),
            ("ifrs-full", "FinanceCosts"),
        ],
        "other_income": [
            ("us-gaap", "NonoperatingIncomeExpense"),
            ("us-gaap", "OtherNonoperatingIncomeExpense"),
        ],
        "pretax_income": [
            ("us-gaap", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest"),
            ("us-gaap", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"),
            ("us-gaap", "IncomeLossFromContinuingOperationsBeforeIncomeTaxes"),
            ("ifrs-full", "ProfitLossBeforeTax"),
        ],
        "income_tax": [
            ("us-gaap", "IncomeTaxExpenseBenefit"),
            ("ifrs-full", "IncomeTaxExpenseContinuingOperations"),
            ("ifrs-full", "IncomeTaxExpense"),
        ],
        "net_income": [("us-gaap", "NetIncomeLoss"), ("ifrs-full", "ProfitLoss")],
        "eps_basic": [("us-gaap", "EarningsPerShareBasic"), ("ifrs-full", "BasicEarningsLossPerShare")],
        "eps_diluted": [("us-gaap", "EarningsPerShareDiluted"), ("ifrs-full", "DilutedEarningsLossPerShare")],
        "shares_basic": [("us-gaap", "WeightedAverageNumberOfSharesOutstandingBasic")],
        "shares_diluted": [("us-gaap", "WeightedAverageNumberOfDilutedSharesOutstanding")],
    },
    "balance-sheet": {
        "cash_and_equivalents": [
            ("us-gaap", "CashAndCashEquivalentsAtCarryingValue"),
            ("ifrs-full", "CashAndCashEquivalents"),
        ],
        "short_term_investments": [("us-gaap", "ShortTermInvestments")],
        "accounts_receivable": [("us-gaap", "AccountsReceivableNetCurrent"), ("ifrs-full", "TradeAndOtherCurrentReceivables")],
        "inventory": [("us-gaap", "InventoryNet"), ("ifrs-full", "Inventories")],
        "total_current_assets": [("us-gaap", "AssetsCurrent"), ("ifrs-full", "CurrentAssets")],
        "pp_and_e": [
            ("us-gaap", "PropertyPlantAndEquipmentNet"),
            ("ifrs-full", "PropertyPlantAndEquipment"),
        ],
        "goodwill": [("us-gaap", "Goodwill"), ("ifrs-full", "Goodwill")],
        "intangibles": [
            ("us-gaap", "FiniteLivedIntangibleAssetsNet"),
            ("us-gaap", "IntangibleAssetsNetExcludingGoodwill"),
            ("ifrs-full", "IntangibleAssetsOtherThanGoodwill"),
        ],
        "total_assets": [("us-gaap", "Assets"), ("ifrs-full", "Assets")],
        "accounts_payable": [("us-gaap", "AccountsPayableCurrent"), ("ifrs-full", "TradeAndOtherCurrentPayables")],
        "short_term_debt": [
            ("us-gaap", "ShortTermBorrowings"),
            ("us-gaap", "ShortTermDebt"),
            ("us-gaap", "LongTermDebtCurrent"),
        ],
        "total_current_liabilities": [("us-gaap", "LiabilitiesCurrent"), ("ifrs-full", "CurrentLiabilities")],
        "long_term_debt": [("us-gaap", "LongTermDebtNoncurrent"), ("us-gaap", "LongTermDebt")],
        "total_liabilities": [("us-gaap", "Liabilities"), ("ifrs-full", "Liabilities")],
        "retained_earnings": [
            ("us-gaap", "RetainedEarningsAccumulatedDeficit"),
            ("ifrs-full", "RetainedEarnings"),
        ],
        "total_equity": [
            ("us-gaap", "StockholdersEquity"),
            ("us-gaap", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"),
            ("ifrs-full", "Equity"),
        ],
    },
    "cash-flow": {
        "net_income": [("us-gaap", "NetIncomeLoss"), ("ifrs-full", "ProfitLoss")],
        "depreciation_amortization": [
            ("us-gaap", "DepreciationDepletionAndAmortization"),
            ("us-gaap", "DepreciationAndAmortization"),
            ("ifrs-full", "DepreciationAmortisationAndImpairmentExpense"),
        ],
        "stock_based_compensation": [("us-gaap", "ShareBasedCompensation")],
        "change_working_capital": [
            ("us-gaap", "IncreaseDecreaseInOperatingAssetsAndLiabilitiesNet"),
            ("us-gaap", "IncreaseDecreaseInOperatingCapital"),
        ],
        "change_receivables": [("us-gaap", "IncreaseDecreaseInAccountsReceivable")],
        "change_inventory": [("us-gaap", "IncreaseDecreaseInInventories")],
        "change_payables": [("us-gaap", "IncreaseDecreaseInAccountsPayable")],
        "operating_cash_flow": [
            ("us-gaap", "NetCashProvidedByUsedInOperatingActivities"),
            ("ifrs-full", "CashFlowsFromUsedInOperatingActivities"),
        ],
        "capex": [
            ("us-gaap", "PaymentsToAcquirePropertyPlantAndEquipment"),
            ("ifrs-full", "PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"),
        ],
        "acquisitions": [("us-gaap", "PaymentsToAcquireBusinessesNetOfCashAcquired")],
        "asset_sales": [("us-gaap", "PaymentsToAcquireInvestments")],
        "investing_cash_flow": [
            ("us-gaap", "NetCashProvidedByUsedInInvestingActivities"),
            ("ifrs-full", "CashFlowsFromUsedInInvestingActivities"),
        ],
        "dividends_paid": [
            ("us-gaap", "PaymentsOfDividends"),
            ("us-gaap", "PaymentsOfDividendsCommonStock"),
            ("ifrs-full", "DividendsPaidClassifiedAsFinancingActivities"),
        ],
        "share_repurchases": [
            ("us-gaap", "PaymentsForRepurchaseOfCommonStock"),
            ("us-gaap", "PaymentsForRepurchaseOfEquity"),
        ],
        "debt_repayment": [("us-gaap", "RepaymentsOfDebt"), ("us-gaap", "RepaymentsOfLongTermDebt")],
        "debt_issued": [("us-gaap", "ProceedsFromIssuanceOfDebt"), ("ifrs-full", "ProceedsFromBorrowings")],
        "financing_cash_flow": [
            ("us-gaap", "NetCashProvidedByUsedInFinancingActivities"),
            ("ifrs-full", "CashFlowsFromUsedInFinancingActivities"),
        ],
        "net_change_in_cash": [
            ("us-gaap", "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect"),
            ("us-gaap", "CashAndCashEquivalentsPeriodIncreaseDecrease"),
            ("ifrs-full", "IncreaseDecreaseInCashAndCashEquivalents"),
        ],
    },
}


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch financial statements.")
    parser.add_argument("ticker", help="Stock ticker, e.g. CME or AAPL")
    parser.add_argument("--quarterly", action="store_true", help="Also fetch 20 quarters")
    parser.add_argument("--force", action="store_true", help="Ignore existing cached JSON")
    parser.add_argument("--research-base", help="Override research output directory")
    parser.add_argument(
        "--source",
        choices=["auto", "fmp", "free"],
        default="auto",
        help="Data source: auto uses FMP when FMP_API_KEY is set, otherwise free SEC/Yahoo data",
    )
    return parser.parse_args(argv)


def find_repo_root() -> Path:
    candidates = [Path.cwd(), Path(__file__).resolve()]
    for candidate in candidates:
        for parent in [candidate, *candidate.parents]:
            if (
                (parent / ".git").exists()
                or (parent / ".codex" / "skills").exists()
                or (parent / ".codex" / "settings.local.json").exists()
            ):
                return parent
    return Path.cwd()


def load_research_base(override: str | None = None) -> Path:
    if override:
        return Path(override).expanduser()

    env_base = os.environ.get("RESEARCH_BASE_PATH")
    if env_base:
        return Path(env_base).expanduser()

    repo_root = find_repo_root()
    settings_path = repo_root / ".codex" / "settings.local.json"
    if settings_path.exists():
        settings = json.loads(settings_path.read_text())
        base = settings.get("env", {}).get("RESEARCH_BASE_PATH")
        if base:
            return Path(base).expanduser()

    return repo_root / "research"


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


def fetch_json(url: str, headers: dict[str, str] | None = None, timeout: int = 30) -> Any:
    request = Request(url, headers=headers or {})
    try:
        with urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        raise FetchError(f"HTTP {exc.code} fetching {url}") from exc
    except URLError as exc:
        raise FetchError(f"Network error fetching {url}: {exc.reason}") from exc
    except json.JSONDecodeError as exc:
        raise FetchError(f"Invalid JSON fetching {url}") from exc


def sec_headers() -> dict[str, str]:
    return {
        "User-Agent": os.environ.get("SEC_USER_AGENT", DEFAULT_SEC_USER_AGENT),
        "Host": "data.sec.gov",
    }


def sec_files_headers() -> dict[str, str]:
    headers = sec_headers()
    headers["Host"] = "www.sec.gov"
    return headers


def yahoo_headers() -> dict[str, str]:
    return {"User-Agent": "Mozilla/5.0 buffettstack/0.1"}


def select_source(source: str) -> str:
    if source == "auto":
        return "fmp" if os.environ.get("FMP_API_KEY") else "free"
    if source == "fmp" and not os.environ.get("FMP_API_KEY"):
        raise FetchError("FMP_API_KEY is required when --source fmp is used")
    return source


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


def fetch_yahoo_profile(ticker: str) -> dict[str, Any]:
    query = urlencode({"symbols": ticker.upper()})
    try:
        payload = fetch_json(f"{YAHOO_QUOTE_URL}?{query}", headers=yahoo_headers(), timeout=15)
    except FetchError:
        return {}
    result = payload.get("quoteResponse", {}).get("result", [])
    if not result:
        return {}
    quote = result[0]
    return {
        "company_name": quote.get("longName") or quote.get("shortName"),
        "currency": quote.get("currency"),
        "exchange": quote.get("fullExchangeName") or quote.get("exchange"),
        "market_cap": quote.get("marketCap"),
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


def cik10(cik: str | int) -> str:
    return str(cik).strip().lstrip("0").zfill(10)


def resolve_cik(ticker: str) -> str:
    if re.fullmatch(r"\d{1,10}", ticker):
        return cik10(ticker)

    wanted = ticker.upper()
    payload = fetch_json(f"{SEC_FILES_URL}/company_tickers_exchange.json", headers=sec_files_headers())
    fields = payload.get("fields", [])
    for row in payload.get("data", []):
        record = dict(zip(fields, row))
        if str(record.get("ticker", "")).upper() == wanted:
            return cik10(record["cik"])

    fallback = fetch_json(f"{SEC_FILES_URL}/company_tickers.json", headers=sec_files_headers())
    if isinstance(fallback, dict):
        for row in fallback.values():
            if str(row.get("ticker", "")).upper() == wanted:
                return cik10(row["cik_str"])

    raise FetchError(f"Could not resolve SEC CIK for ticker: {ticker}")


def fetch_sec_company_data(ticker: str) -> tuple[str, dict[str, Any], dict[str, Any]]:
    cik = resolve_cik(ticker)
    submissions = fetch_json(f"{SEC_BASE_URL}/submissions/CIK{cik}.json", headers=sec_headers())
    facts = fetch_json(f"{SEC_BASE_URL}/api/xbrl/companyfacts/CIK{cik}.json", headers=sec_headers())
    return cik, submissions, facts


def infer_currency(facts: dict[str, Any], yahoo_profile: dict[str, Any] | None = None) -> str:
    counts: dict[str, int] = {}
    for taxonomy in facts.get("facts", {}).values():
        if not isinstance(taxonomy, dict):
            continue
        for concept in taxonomy.values():
            for unit in concept.get("units", {}):
                if "/" in unit or unit.lower() in {"shares", "pure"}:
                    continue
                counts[unit] = counts.get(unit, 0) + 1
    if counts:
        return max(counts, key=counts.get)
    if yahoo_profile and yahoo_profile.get("currency"):
        return str(yahoo_profile["currency"])
    return "USD"


def unit_score(unit: str, output_field: str) -> int:
    unit_lower = unit.lower()
    if output_field.startswith("shares"):
        return 0 if unit_lower == "shares" else 10
    if output_field.startswith("eps"):
        return 0 if "/shares" in unit_lower else 10
    if unit_lower in {"usd", "eur", "gbp", "jpy", "cad", "aud", "chf"}:
        return 0
    if "/" in unit_lower or unit_lower in {"shares", "pure"}:
        return 10
    return 2


def iter_sec_entries(facts: dict[str, Any], aliases: list[tuple[str, str]], output_field: str) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    fact_root = facts.get("facts", {})
    for taxonomy, tag in aliases:
        concept = fact_root.get(taxonomy, {}).get(tag)
        if not concept:
            continue
        units = concept.get("units", {})
        for unit in sorted(units, key=lambda value: unit_score(value, output_field)):
            for entry in units.get(unit, []):
                if "val" not in entry:
                    continue
                enriched = dict(entry)
                enriched["_taxonomy"] = taxonomy
                enriched["_tag"] = tag
                enriched["_unit"] = unit
                entries.append(enriched)
    return entries


def sec_period_key(entry: dict[str, Any], period_type: str) -> str | None:
    fiscal_year = entry.get("fy")
    if fiscal_year is None:
        fiscal_year = str(entry.get("end", ""))[:4]
    if not fiscal_year:
        return None
    fiscal_year = str(fiscal_year)
    fp = str(entry.get("fp") or "").upper()
    form = str(entry.get("form") or "").upper()

    if period_type == "annual":
        if form not in ANNUAL_FORMS or (fp and fp != "FY"):
            return None
        return fiscal_year

    if form not in QUARTERLY_FORMS or fp not in {"Q1", "Q2", "Q3", "Q4"}:
        return None
    return f"{fiscal_year}-{fp}"


def duration_days(entry: dict[str, Any]) -> int:
    try:
        start = datetime.fromisoformat(str(entry.get("start")))
        end = datetime.fromisoformat(str(entry.get("end")))
    except (TypeError, ValueError):
        return 999_999
    return (end - start).days


def sec_entry_sort_key(entry: dict[str, Any]) -> tuple[str, str, int, str]:
    return (
        str(entry.get("end") or ""),
        str(entry.get("filed") or ""),
        -duration_days(entry),
        str(entry.get("accn") or ""),
    )


def source_note(entry: dict[str, Any]) -> dict[str, Any]:
    return {
        "taxonomy": entry.get("_taxonomy"),
        "tag": entry.get("_tag"),
        "unit": entry.get("_unit"),
        "form": entry.get("form"),
        "filed": entry.get("filed"),
        "accession": entry.get("accn"),
        "frame": entry.get("frame"),
        "start": entry.get("start"),
        "end": entry.get("end"),
    }


def quarter_number(key: str) -> int | None:
    match = re.match(r"^\d{4}-Q([1-4])$", key)
    return int(match.group(1)) if match else None


def is_ytd_quarter(entry: dict[str, Any], key: str) -> bool:
    quarter = quarter_number(key)
    if quarter is None or quarter == 1:
        return False
    return duration_days(entry) > 120


def previous_quarter_key(key: str) -> str | None:
    match = re.match(r"^(\d{4})-Q([1-4])$", key)
    if not match:
        return None
    quarter = int(match.group(2))
    if quarter <= 1:
        return None
    return f"{match.group(1)}-Q{quarter - 1}"


def derive_quarterly_cash_flow_rows(
    rows: dict[str, dict[str, Any]],
    source_entries: dict[str, dict[str, dict[str, Any]]],
    source_notes: dict[str, dict[str, dict[str, Any]]],
) -> None:
    for key, fields in source_entries.items():
        previous_key = previous_quarter_key(key)
        if not previous_key:
            continue
        for field, entry in fields.items():
            if field not in SEC_FACT_ALIASES["cash-flow"] or not is_ytd_quarter(entry, key):
                continue
            previous_entry = source_entries.get(previous_key, {}).get(field)
            if not previous_entry:
                source_notes.setdefault(key, {}).setdefault(field, {})["ytd_unadjusted"] = True
                continue
            current_value = as_float(entry.get("val"))
            previous_value = as_float(previous_entry.get("val"))
            if current_value is None or previous_value is None:
                continue
            rows[key][field] = current_value - previous_value
            source_notes.setdefault(key, {}).setdefault(field, {}).update(
                {
                    "derived_from_ytd": True,
                    "prior_period": previous_key,
                    "prior_period_value": previous_value,
                }
            )


def transform_sec_facts(
    facts: dict[str, Any],
    statement_name: str,
    period_type: str,
    limit: int,
) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    sources: dict[str, dict[str, dict[str, Any]]] = {}
    source_entries: dict[str, dict[str, dict[str, Any]]] = {}
    for output_field, aliases in SEC_FACT_ALIASES[statement_name].items():
        best_by_period: dict[str, dict[str, Any]] = {}
        for entry in iter_sec_entries(facts, aliases, output_field):
            key = sec_period_key(entry, period_type)
            if not key:
                continue
            current = best_by_period.get(key)
            if current is None or sec_entry_sort_key(entry) >= sec_entry_sort_key(current):
                best_by_period[key] = entry

        for key, entry in best_by_period.items():
            row = rows.setdefault(key, {"date": entry.get("end"), "fiscal_year": key[:4]})
            if period_type == "quarterly":
                row["period"] = key[-2:]
            row[output_field] = entry.get("val")
            if entry.get("end") and (not row.get("date") or str(entry["end"]) > str(row["date"])):
                row["date"] = entry.get("end")
            sources.setdefault(key, {})[output_field] = source_note(entry)
            source_entries.setdefault(key, {})[output_field] = entry

    if statement_name == "cash-flow" and period_type == "quarterly":
        derive_quarterly_cash_flow_rows(rows, source_entries, sources)

    for key, row in rows.items():
        for output_field in SEC_FACT_ALIASES[statement_name]:
            row.setdefault(output_field, None)
        apply_derived_fields(statement_name, row)
        for output_field in STATEMENTS[statement_name]["fields"]:
            row.setdefault(output_field, None)
        if key in sources:
            row["_sources"] = sources[key]

    sorted_keys = sort_period_keys(list(rows.keys()))[:limit]
    return {key: rows[key] for key in sorted_keys}


def ratio(numerator: Any, denominator: Any) -> float | None:
    num = as_float(numerator)
    den = as_float(denominator)
    if num is None or den in (None, 0):
        return None
    return num / den


def apply_derived_fields(statement_name: str, row: dict[str, Any]) -> None:
    if statement_name == "income-statement":
        gross_profit = as_float(row.get("gross_profit"))
        operating_income = as_float(row.get("operating_income"))
        operating_expenses = as_float(row.get("operating_expenses"))
        if gross_profit is not None and operating_income is not None:
            derived_operating_expenses = gross_profit - operating_income
            if operating_expenses is None or abs(operating_expenses - derived_operating_expenses) > abs(derived_operating_expenses) * 0.05:
                row["operating_expenses"] = derived_operating_expenses
        row["gross_margin"] = row.get("gross_margin") or ratio(row.get("gross_profit"), row.get("revenue"))
        row["operating_margin"] = row.get("operating_margin") or ratio(row.get("operating_income"), row.get("revenue"))
        row["net_margin"] = row.get("net_margin") or ratio(row.get("net_income"), row.get("revenue"))
        row.setdefault("ebitda", None)
        row.setdefault("ebitda_margin", ratio(row.get("ebitda"), row.get("revenue")))
    elif statement_name == "balance-sheet":
        cash = as_float(row.get("cash_and_equivalents"))
        investments = as_float(row.get("short_term_investments"))
        if row.get("total_cash") is None and (cash is not None or investments is not None):
            row["total_cash"] = (cash or 0) + (investments or 0)
        short_debt = as_float(row.get("short_term_debt"))
        long_debt = as_float(row.get("long_term_debt"))
        if row.get("total_debt") is None and (short_debt is not None or long_debt is not None):
            row["total_debt"] = (short_debt or 0) + (long_debt or 0)
    elif statement_name == "cash-flow":
        operating_cash_flow = as_float(row.get("operating_cash_flow"))
        capex = as_float(row.get("capex"))
        if row.get("free_cash_flow") is None and operating_cash_flow is not None and capex is not None:
            row["free_cash_flow"] = operating_cash_flow - abs(capex)


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
    data_source: str = "FMP API",
    provider: str = "fmp",
    extra_metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    metadata = {
        "ticker": ticker.upper(),
        "company_name": company_name,
        "last_updated": last_updated,
        "data_source": data_source,
        "provider": provider,
        "currency": currency,
        "statement": statement_name,
    }
    if extra_metadata:
        metadata.update(extra_metadata)
    payload = {
        "metadata": metadata,
        "annual": transform_records(annual_records, statement_name, "annual"),
        "quarterly": {},
    }
    if quarterly_records is not None:
        payload["quarterly"] = transform_records(quarterly_records, statement_name, "quarterly")
    return payload


def build_sec_statement_payload(
    ticker: str,
    company_name: str,
    currency: str,
    statement_name: str,
    facts: dict[str, Any],
    last_updated: str,
    cik: str,
    include_quarterly: bool,
    supplemental_metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    metadata = {
        "ticker": ticker.upper(),
        "company_name": company_name,
        "last_updated": last_updated,
        "data_source": "SEC EDGAR Company Facts",
        "provider": "free",
        "currency": currency,
        "statement": statement_name,
        "sec_cik": cik,
        "source_priority": ["SEC EDGAR Company Facts", "Yahoo Finance quote metadata"],
    }
    if supplemental_metadata:
        metadata["supplemental"] = supplemental_metadata
    return {
        "metadata": metadata,
        "annual": transform_sec_facts(facts, statement_name, "annual", 10),
        "quarterly": transform_sec_facts(facts, statement_name, "quarterly", 20) if include_quarterly else {},
    }


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


def filename_company_name(company_name: str) -> str:
    return company_name.strip().rstrip(".") or company_name.strip()


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
    data_source = metadata.get("data_source", "")
    annual_years = list(payloads["income-statement"].get("annual", {}).keys())
    quarterly_periods = list(payloads["income-statement"].get("quarterly", {}).keys())

    lines = [
        f"# {company_name} - Financial Statements",
        "",
        f"**Ticker:** {ticker.upper()}",
        f"**Last Updated:** {metadata.get('last_updated', '')}",
        f"**Data Source:** {data_source}",
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
    lines.extend(["", f"*Data from {data_source}. JSON source files in this folder.*", ""])
    return "\n".join(lines)


def fetch_statement(script_path: Path, statement_name: str, ticker: str, period: str, limit: str) -> Any:
    command = STATEMENTS[statement_name]["fmp_command"]
    return run_fmp(script_path, command, ticker.upper(), period, limit)


def fetch_fmp_payloads(
    ticker: str,
    include_quarterly: bool,
    last_updated: str,
) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    skill_dir = Path(__file__).resolve().parents[1]
    script_path = skill_dir / "scripts" / "fmp-financials.sh"
    profile = parse_profile(run_fmp(script_path, "profile", ticker), ticker)
    payloads: dict[str, dict[str, Any]] = {}
    for statement_name in STATEMENTS:
        annual = fetch_statement(script_path, statement_name, ticker, "annual", "10")
        quarterly = fetch_statement(script_path, statement_name, ticker, "quarterly", "20") if include_quarterly else None
        payloads[statement_name] = build_statement_payload(
            ticker,
            profile["company_name"],
            profile["currency"],
            statement_name,
            annual,
            quarterly,
            last_updated,
        )
    return profile, payloads


def fetch_free_payloads(
    ticker: str,
    include_quarterly: bool,
    last_updated: str,
) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    cik, submissions, facts = fetch_sec_company_data(ticker)
    yahoo_profile = fetch_yahoo_profile(ticker)
    company_name = (
        submissions.get("name")
        or facts.get("entityName")
        or yahoo_profile.get("company_name")
        or ticker.upper()
    )
    currency = infer_currency(facts, yahoo_profile)
    profile = {
        "ticker": ticker.upper(),
        "company_name": company_name,
        "currency": currency,
        "cik": cik,
    }
    supplemental = {key: value for key, value in yahoo_profile.items() if value is not None}
    payloads = {
        statement_name: build_sec_statement_payload(
            ticker=ticker,
            company_name=company_name,
            currency=currency,
            statement_name=statement_name,
            facts=facts,
            last_updated=last_updated,
            cik=cik,
            include_quarterly=include_quarterly,
            supplemental_metadata=supplemental or None,
        )
        for statement_name in STATEMENTS
    }
    if not any(payloads["income-statement"].get("annual", {}).values()):
        raise FetchError(f"No SEC annual statement facts found for {ticker.upper()} / CIK {cik}")
    return profile, payloads


def fetch_payloads(
    ticker: str,
    source: str,
    include_quarterly: bool,
    last_updated: str,
) -> tuple[str, dict[str, Any], dict[str, dict[str, Any]]]:
    selected_source = select_source(source)
    if selected_source == "fmp":
        profile, payloads = fetch_fmp_payloads(ticker, include_quarterly, last_updated)
    else:
        profile, payloads = fetch_free_payloads(ticker, include_quarterly, last_updated)
    return selected_source, profile, payloads


def execute(args: argparse.Namespace) -> dict[str, Any]:
    ticker = args.ticker.upper()
    research_base = load_research_base(args.research_base)
    last_updated = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    selected_source, profile, fresh_payloads = fetch_payloads(ticker, args.source, args.quarterly, last_updated)
    company_name = profile["company_name"]
    company_dir = resolve_company_dir(research_base, company_name, ticker)
    output_dir = company_dir / "1.3-Financial-Statements"
    output_dir.mkdir(parents=True, exist_ok=True)

    payloads: dict[str, dict[str, Any]] = {}
    files: list[str] = []

    for statement_name, config in STATEMENTS.items():
        output_path = output_dir / f"{ticker}-{config['file_suffix']}.json"
        payload = merge_payload(read_existing(output_path), fresh_payloads[statement_name], args.force)
        write_json(output_path, payload)
        payloads[statement_name] = payload
        files.append(str(output_path))

    markdown = build_markdown(company_name, ticker, payloads)
    markdown_path = output_dir / f"Financial Statements - {filename_company_name(company_name)}.md"
    markdown_path.write_text(markdown)
    files.append(str(markdown_path))

    annual_years = list(payloads["income-statement"].get("annual", {}).keys())
    quarterly_periods = list(payloads["income-statement"].get("quarterly", {}).keys())
    return {
        "company_name": company_name,
        "ticker": ticker,
        "source": selected_source,
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
