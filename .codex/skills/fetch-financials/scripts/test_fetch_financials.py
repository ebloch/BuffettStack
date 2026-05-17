import json
from pathlib import Path

import fetch_financials as ff


def test_transform_income_statement_annual_maps_fields():
    records = [
        {
            "date": "2024-12-31",
            "fiscalYear": "2024",
            "revenue": 6_000_000_000,
            "grossProfitRatio": 0.82,
            "epsdiluted": 10.25,
        }
    ]

    transformed = ff.transform_records(records, "income-statement", "annual")

    assert list(transformed) == ["2024"]
    assert transformed["2024"]["date"] == "2024-12-31"
    assert transformed["2024"]["fiscal_year"] == "2024"
    assert transformed["2024"]["revenue"] == 6_000_000_000
    assert transformed["2024"]["gross_margin"] == 0.82
    assert transformed["2024"]["eps_diluted"] == 10.25


def test_transform_quarterly_uses_fiscal_year_and_period_key():
    records = [
        {
            "date": "2024-09-30",
            "fiscalYear": "2024",
            "period": "Q3",
            "freeCashFlow": 500_000_000,
        }
    ]

    transformed = ff.transform_records(records, "cash-flow", "quarterly")

    assert list(transformed) == ["2024-Q3"]
    assert transformed["2024-Q3"]["period"] == "Q3"
    assert transformed["2024-Q3"]["free_cash_flow"] == 500_000_000


def test_merge_payload_preserves_old_periods_and_overwrites_fresh_periods():
    existing = {
        "metadata": {"ticker": "CME", "last_updated": "old"},
        "annual": {
            "2023": {"revenue": 3},
            "2022": {"revenue": 2},
        },
        "quarterly": {
            "2023-Q4": {"revenue": 1},
        },
    }
    fresh = {
        "metadata": {"ticker": "CME", "last_updated": "new"},
        "annual": {
            "2024": {"revenue": 4},
            "2023": {"revenue": 33},
        },
        "quarterly": {},
    }

    merged = ff.merge_payload(existing, fresh, force=False)

    assert merged["metadata"]["last_updated"] == "new"
    assert list(merged["annual"]) == ["2024", "2023", "2022"]
    assert merged["annual"]["2023"]["revenue"] == 33
    assert merged["annual"]["2022"]["revenue"] == 2
    assert merged["quarterly"]["2023-Q4"]["revenue"] == 1


def test_force_merge_returns_only_fresh_payload():
    existing = {"metadata": {}, "annual": {"2022": {"revenue": 2}}, "quarterly": {}}
    fresh = {"metadata": {}, "annual": {"2024": {"revenue": 4}}, "quarterly": {}}

    merged = ff.merge_payload(existing, fresh, force=True)

    assert merged["annual"] == {"2024": {"revenue": 4}}


def test_resolve_company_dir_reuses_existing_simpler_company_folder(tmp_path: Path):
    existing = tmp_path / "CME Group"
    existing.mkdir()

    resolved = ff.resolve_company_dir(tmp_path, "CME Group Inc.", "CME")

    assert resolved == existing


def test_build_markdown_contains_source_links_and_formatted_values():
    last_updated = "2026-05-03T12:00:00Z"
    income = ff.build_statement_payload(
        "CME",
        "CME Group Inc.",
        "USD",
        "income-statement",
        [
            {"date": "2024-12-31", "fiscalYear": "2024", "revenue": 6_000_000_000, "operatingIncomeRatio": 0.65},
            {"date": "2023-12-31", "fiscalYear": "2023", "revenue": 5_000_000_000, "operatingIncomeRatio": 0.60},
        ],
        None,
        last_updated,
    )
    balance = ff.build_statement_payload(
        "CME",
        "CME Group Inc.",
        "USD",
        "balance-sheet",
        [
            {"date": "2024-12-31", "fiscalYear": "2024", "totalDebt": 3_000_000_000, "totalStockholdersEquity": 30_000_000_000},
            {"date": "2023-12-31", "fiscalYear": "2023", "totalDebt": 2_000_000_000, "totalStockholdersEquity": 20_000_000_000},
        ],
        None,
        last_updated,
    )
    cash = ff.build_statement_payload(
        "CME",
        "CME Group Inc.",
        "USD",
        "cash-flow",
        [
            {"date": "2024-12-31", "fiscalYear": "2024", "freeCashFlow": 3_000_000_000},
            {"date": "2023-12-31", "fiscalYear": "2023", "freeCashFlow": 2_500_000_000},
        ],
        None,
        last_updated,
    )

    markdown = ff.build_markdown(
        "CME Group Inc.",
        "CME",
        {"income-statement": income, "balance-sheet": balance, "cash-flow": cash},
    )

    assert "# CME Group Inc. - Financial Statements" in markdown
    assert "[[CME-income-statement.json]]" in markdown
    assert "| 2024 | $6.0B" in markdown
    assert "## Key Metrics" in markdown


def test_written_json_is_pretty_and_round_trips(tmp_path: Path):
    output = tmp_path / "statement.json"
    payload = {"metadata": {"ticker": "CME"}, "annual": {"2024": {"revenue": 1}}, "quarterly": {}}

    ff.write_json(output, payload)

    assert json.loads(output.read_text()) == payload
    assert output.read_text().endswith("\n")
