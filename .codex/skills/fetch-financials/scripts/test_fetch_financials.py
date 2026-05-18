import json
from pathlib import Path

import pytest

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


def test_load_research_base_prefers_override(tmp_path: Path):
    assert ff.load_research_base(str(tmp_path)) == tmp_path


def test_load_research_base_prefers_environment_variable(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("RESEARCH_BASE_PATH", str(tmp_path))

    assert ff.load_research_base() == tmp_path


def test_load_research_base_reads_codex_settings(tmp_path: Path, monkeypatch):
    repo = tmp_path / "repo"
    research = tmp_path / "research-root"
    settings_dir = repo / ".codex"
    settings_dir.mkdir(parents=True)
    (settings_dir / "settings.local.json").write_text(json.dumps({"env": {"RESEARCH_BASE_PATH": str(research)}}))
    monkeypatch.delenv("RESEARCH_BASE_PATH", raising=False)
    monkeypatch.chdir(repo)

    assert ff.load_research_base() == research


def test_load_research_base_defaults_to_repo_research_dir(tmp_path: Path, monkeypatch):
    repo = tmp_path / "repo"
    (repo / ".git").mkdir(parents=True)
    monkeypatch.delenv("RESEARCH_BASE_PATH", raising=False)
    monkeypatch.chdir(repo)

    assert ff.load_research_base() == repo / "research"


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


def test_select_source_auto_prefers_fmp_when_token_exists(monkeypatch):
    monkeypatch.setenv("FMP_API_KEY", "token")

    assert ff.select_source("auto") == "fmp"


def test_select_source_auto_uses_free_without_token(monkeypatch):
    monkeypatch.delenv("FMP_API_KEY", raising=False)

    assert ff.select_source("auto") == "free"


def test_select_source_fmp_requires_token(monkeypatch):
    monkeypatch.delenv("FMP_API_KEY", raising=False)

    with pytest.raises(ff.FetchError):
        ff.select_source("fmp")


def sec_fact(tag: str, val: int | float, unit: str = "USD", **overrides):
    entry = {
        "fy": 2024,
        "fp": "FY",
        "form": "10-K",
        "filed": "2025-02-01",
        "accn": "0000000000-25-000001",
        "frame": "CY2024",
        "end": "2024-12-31",
        "val": val,
    }
    entry.update(overrides)
    return tag, {"units": {unit: [entry]}}


def test_transform_sec_facts_maps_annual_fields_and_sources():
    facts = {
        "facts": {
            "us-gaap": dict(
                [
                    sec_fact("RevenueFromContractWithCustomerExcludingAssessedTax", 6_000_000_000),
                    sec_fact("GrossProfit", 3_000_000_000),
                    sec_fact("OperatingIncomeLoss", 2_000_000_000),
                    sec_fact("NetIncomeLoss", 1_500_000_000),
                    sec_fact("EarningsPerShareDiluted", 10.25, "USD/shares"),
                    sec_fact("WeightedAverageNumberOfDilutedSharesOutstanding", 100_000_000, "shares"),
                ]
            )
        }
    }

    rows = ff.transform_sec_facts(facts, "income-statement", "annual", 10)

    assert list(rows) == ["2024"]
    row = rows["2024"]
    assert row["revenue"] == 6_000_000_000
    assert row["operating_expenses"] == 1_000_000_000
    assert row["gross_margin"] == pytest.approx(0.5)
    assert row["operating_margin"] == pytest.approx(1 / 3)
    assert row["eps_diluted"] == 10.25
    assert row["shares_diluted"] == 100_000_000
    assert row["_sources"]["revenue"]["tag"] == "RevenueFromContractWithCustomerExcludingAssessedTax"


def test_transform_sec_facts_maps_quarterly_and_derives_free_cash_flow():
    facts = {
        "facts": {
            "us-gaap": dict(
                [
                    sec_fact(
                        "NetCashProvidedByUsedInOperatingActivities",
                        700_000_000,
                        fp="Q3",
                        form="10-Q",
                        frame="CY2024Q3",
                        end="2024-09-30",
                    ),
                    sec_fact(
                        "PaymentsToAcquirePropertyPlantAndEquipment",
                        120_000_000,
                        fp="Q3",
                        form="10-Q",
                        frame="CY2024Q3",
                        end="2024-09-30",
                    ),
                ]
            )
        }
    }

    rows = ff.transform_sec_facts(facts, "cash-flow", "quarterly", 20)

    assert list(rows) == ["2024-Q3"]
    assert rows["2024-Q3"]["period"] == "Q3"
    assert rows["2024-Q3"]["operating_cash_flow"] == 700_000_000
    assert rows["2024-Q3"]["free_cash_flow"] == 580_000_000


def test_transform_sec_facts_converts_ytd_cash_flow_to_discrete_quarter():
    operating_cash_flow_entries = [
        {
            "fy": 2024,
            "fp": "Q1",
            "form": "10-Q",
            "filed": "2025-02-01",
            "accn": "0000000000-25-000001",
            "start": "2024-01-01",
            "end": "2024-03-31",
            "val": 100,
        },
        {
            "fy": 2024,
            "fp": "Q2",
            "form": "10-Q",
            "filed": "2025-02-01",
            "accn": "0000000000-25-000001",
            "start": "2024-01-01",
            "end": "2024-06-30",
            "val": 250,
        },
    ]
    capex_entries = [
        {**operating_cash_flow_entries[0], "val": 10},
        {**operating_cash_flow_entries[1], "val": 25},
    ]
    facts = {
        "facts": {
            "us-gaap": {
                "NetCashProvidedByUsedInOperatingActivities": {"units": {"USD": operating_cash_flow_entries}},
                "PaymentsToAcquirePropertyPlantAndEquipment": {"units": {"USD": capex_entries}},
            }
        }
    }

    rows = ff.transform_sec_facts(facts, "cash-flow", "quarterly", 20)

    assert rows["2024-Q2"]["operating_cash_flow"] == 150
    assert rows["2024-Q2"]["capex"] == 15
    assert rows["2024-Q2"]["free_cash_flow"] == 135
    assert rows["2024-Q2"]["_sources"]["operating_cash_flow"]["derived_from_ytd"] is True


def test_transform_sec_facts_prefers_discrete_quarter_over_ytd_entry():
    facts = {
        "facts": {
            "us-gaap": dict(
                [
                    sec_fact(
                        "RevenueFromContractWithCustomerExcludingAssessedTax",
                        300,
                        fp="Q2",
                        form="10-Q",
                        start="2024-01-01",
                        end="2024-06-30",
                    ),
                    sec_fact(
                        "RevenueFromContractWithCustomerExcludingAssessedTax",
                        125,
                        fp="Q2",
                        form="10-Q",
                        start="2024-04-01",
                        end="2024-06-30",
                    ),
                ]
            )
        }
    }

    rows = ff.transform_sec_facts(facts, "income-statement", "quarterly", 20)

    assert rows["2024-Q2"]["revenue"] == 125


def test_build_sec_statement_payload_preserves_canonical_shape():
    facts = {
        "facts": {
            "us-gaap": dict(
                [
                    sec_fact("Assets", 10_000_000_000),
                    sec_fact("CashAndCashEquivalentsAtCarryingValue", 1_000_000_000),
                    sec_fact("ShortTermBorrowings", 200_000_000),
                    sec_fact("LongTermDebtNoncurrent", 1_800_000_000),
                ]
            )
        }
    }

    payload = ff.build_sec_statement_payload(
        "CME",
        "CME Group Inc.",
        "USD",
        "balance-sheet",
        facts,
        "2026-05-17T00:00:00Z",
        "0001156375",
        include_quarterly=False,
        supplemental_metadata={"exchange": "NasdaqGS"},
    )

    assert payload["metadata"]["provider"] == "free"
    assert payload["metadata"]["sec_cik"] == "0001156375"
    assert payload["annual"]["2024"]["total_assets"] == 10_000_000_000
    assert payload["annual"]["2024"]["total_debt"] == 2_000_000_000
    assert payload["quarterly"] == {}
