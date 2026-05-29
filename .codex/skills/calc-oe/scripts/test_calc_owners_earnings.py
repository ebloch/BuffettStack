import json
from pathlib import Path

import pytest

import calc_owners_earnings as oe


def test_general_operating_formula_deducts_sbc_and_maintenance_capex():
    calc = oe.calculate_year(
        "2024",
        "general-operating",
        0.5,
        {
            "revenue": 1_000_000_000,
            "net_income": 200_000_000,
            "shares_diluted": 100_000_000,
        },
        {
            "depreciation_amortization": 50_000_000,
            "capex": -40_000_000,
            "stock_based_compensation": 10_000_000,
        },
    )

    assert calc.maint_capex == pytest.approx(20_000_000)
    assert calc.owners_earnings == pytest.approx(220_000_000)
    assert calc.oe_per_share == pytest.approx(2.20)
    assert calc.oe_margin == pytest.approx(0.22)


def test_insurance_formula_excludes_d_and_a_and_capex_but_deducts_sbc():
    calc = oe.calculate_year(
        "2024",
        "insurance",
        0.0,
        {"netIncome": 500_000_000, "weightedAverageShsOutDil": 50_000_000},
        {
            "depreciationAndAmortization": 99_000_000,
            "capitalExpenditure": -20_000_000,
            "stockBasedCompensation": 5_000_000,
        },
    )

    assert calc.owners_earnings == pytest.approx(495_000_000)
    assert calc.oe_per_share == pytest.approx(9.90)


def test_exchange_asset_light_uses_full_capex_as_maintenance():
    calc = oe.calculate_year(
        "2024",
        "exchange-asset-light",
        1.0,
        {"net_income": 300_000_000, "shares_diluted": 100_000_000},
        {
            "depreciation_amortization": 30_000_000,
            "capex": -15_000_000,
            "stock_based_compensation": 5_000_000,
        },
    )

    assert calc.owners_earnings == pytest.approx(310_000_000)


def test_calculate_all_adds_yoy_growth():
    calculations = oe.calculate_all(
        ["2023", "2024"],
        "insurance",
        0,
        {
            "2023": {"net_income": 100_000_000, "shares_diluted": 10_000_000},
            "2024": {"net_income": 125_000_000, "shares_diluted": 10_000_000},
        },
        {
            "2023": {"stock_based_compensation": 0},
            "2024": {"stock_based_compensation": 0},
        },
    )

    assert calculations[0].oe_growth_yoy is None
    assert calculations[1].oe_growth_yoy == pytest.approx(0.25)


def test_extract_year_from_frontmatter_and_filename(tmp_path: Path):
    memo = tmp_path / "FY2023 - Example - 10-K Synthesis - Memo.md"
    memo.write_text("---\nfiscal_year: 2024\nticker: EX\n---\nbody")
    fallback = tmp_path / "FY2022 - Example - 10-K Synthesis - Memo.md"
    fallback.write_text("body")

    assert oe.extract_year_from_memo(memo) == "2024"
    assert oe.extract_year_from_memo(fallback) == "2022"
    assert oe.extract_ticker_from_memo(memo) == "EX"


def test_load_statement_supports_codex_schema_and_raw_fmp_array(tmp_path: Path):
    codex_file = tmp_path / "EX-income-statement.json"
    codex_file.write_text(json.dumps({"annual": {"2024": {"net_income": 1}}}))
    raw_file = tmp_path / "raw.json"
    raw_file.write_text(json.dumps([{"fiscalYear": "2023", "netIncome": 2}]))

    assert oe.load_statement(codex_file)["2024"]["net_income"] == 1
    assert oe.load_statement(raw_file)["2023"]["netIncome"] == 2


def test_parse_args_rejects_maintenance_capex_rate_over_one():
    with pytest.raises(SystemExit):
        oe.parse_args(["--company", "Example Co", "--business-type", "general-operating", "--maint-capex-rate", "50"])


def test_load_research_base_prefers_override(tmp_path: Path):
    assert oe.load_research_base(str(tmp_path)) == tmp_path


def test_load_research_base_prefers_environment_variable(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("RESEARCH_BASE_PATH", str(tmp_path))

    assert oe.load_research_base() == tmp_path


def test_load_research_base_reads_codex_settings(tmp_path: Path, monkeypatch):
    repo = tmp_path / "repo"
    research = tmp_path / "research-root"
    settings_dir = repo / ".codex"
    settings_dir.mkdir(parents=True)
    (settings_dir / "settings.local.json").write_text(json.dumps({"env": {"RESEARCH_BASE_PATH": str(research)}}))
    monkeypatch.delenv("RESEARCH_BASE_PATH", raising=False)
    monkeypatch.chdir(repo)

    assert oe.load_research_base() == research


def test_load_research_base_defaults_to_repo_research_dir(tmp_path: Path, monkeypatch):
    repo = tmp_path / "repo"
    (repo / ".git").mkdir(parents=True)
    monkeypatch.delenv("RESEARCH_BASE_PATH", raising=False)
    monkeypatch.chdir(repo)

    assert oe.load_research_base() == repo / "research"


def test_execute_writes_owner_earnings_memo(tmp_path: Path):
    company_dir = tmp_path / "Example Co"
    filings_dir = company_dir / "1.1-Annual-Filings"
    financial_dir = company_dir / "1.3-Financial-Statements"
    filings_dir.mkdir(parents=True)
    financial_dir.mkdir(parents=True)
    (filings_dir / "FY2023 - Example Co - 10-K Synthesis - Memo.md").write_text("---\nfiscal_year: 2023\nticker: EX\n---\n")
    (filings_dir / "FY2024 - Example Co - 10-K Synthesis - Memo.md").write_text("---\nfiscal_year: 2024\nticker: EX\n---\n")
    (financial_dir / "EX-income-statement.json").write_text(
        json.dumps(
            {
                "metadata": {"ticker": "EX"},
                "annual": {
                    "2023": {"revenue": 1_000_000_000, "net_income": 100_000_000, "shares_diluted": 10_000_000},
                    "2024": {"revenue": 1_100_000_000, "net_income": 120_000_000, "shares_diluted": 10_000_000},
                },
            }
        )
    )
    (financial_dir / "EX-cash-flow.json").write_text(
        json.dumps(
            {
                "annual": {
                    "2023": {
                        "depreciation_amortization": 10_000_000,
                        "capex": -20_000_000,
                        "stock_based_compensation": 5_000_000,
                        "free_cash_flow": 80_000_000,
                    },
                    "2024": {
                        "depreciation_amortization": 10_000_000,
                        "capex": -20_000_000,
                        "stock_based_compensation": 5_000_000,
                        "free_cash_flow": 90_000_000,
                    },
                }
            }
        )
    )

    result = oe.execute(
        oe.parse_args(
            [
                "--company",
                "Example Co",
                "--business-type",
                "general-operating",
                "--research-base",
                str(tmp_path),
                "--timestamp",
                "2026-05-03-1200",
            ]
        )
    )

    output = Path(result["output_path"])
    assert output.exists()
    text = output.read_text()
    assert "# Example Co - Owner's Earnings" in text
    assert "| Total OE ($M) | 95 | 115 |" in text
    assert result["years_calculated"] == ["2023", "2024"]


def test_insurance_markdown_omits_unused_d_and_a_and_maint_capex_rows(tmp_path: Path):
    output = oe.build_markdown(
        company="Insurer Co",
        ticker="INS",
        business_type="insurance",
        maint_capex_rate=0,
        calculations=[
            oe.calculate_year(
                "2024",
                "insurance",
                0,
                {"revenue": 1_000_000_000, "net_income": 100_000_000, "shares_diluted": 10_000_000},
                {
                    "depreciation_amortization": 20_000_000,
                    "capex": -10_000_000,
                    "stock_based_compensation": 1_000_000,
                    "free_cash_flow": 80_000_000,
                },
            )
        ],
        income_path=tmp_path / "INS-income-statement.json",
        cash_path=tmp_path / "INS-cash-flow.json",
        memo_paths={"2024": tmp_path / "FY2024 - Insurer Co - 10-K Synthesis - Memo.md"},
        business_economics_path=None,
        output_date="2026-05-29",
    )

    detail = output.split("## OE Calculation Detail", 1)[1].split("## Input Data", 1)[0]
    assert output.startswith("---\nformal_qc_run: false\n")
    assert "| + D&A |" not in detail
    assert "| - Maint Capex |" not in detail
    assert "| - SBC | 1 | Cash Flow JSON unless source-overridden |" in detail
