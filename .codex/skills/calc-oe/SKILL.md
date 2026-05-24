---
name: calc-oe
description: Calculate historical owner's earnings for all fiscal years with annual-filing synthesis memos, using financial statement JSON from $fetch-financials and a business-type-appropriate formula. Use when explicitly invoked as $calc-oe with a company name or ticker.
---

# Calculate Owner's Earnings

Use this skill to produce a clean, auditable owner's earnings memo from existing annual-filing synthesis memos and financial statement JSON.

## Inputs

Accept invocation text after `$calc-oe`:

```text
COMPANY_OR_TICKER
```

Examples:

- `CME`
- `CME Group`
- `Chubb`

If no company or ticker is provided, ask for it.

## Resources

This skill is self-contained. Use these bundled files:

- `scripts/calc_owners_earnings.py` reads financial JSON, computes OE tables, and writes the memo.
- `scripts/test_calc_owners_earnings.py` tests deterministic calculation behavior.
- `references/output-template.md` defines the target memo structure.
- `references/phase-2-qc-prompt.md` defines the QC review focus.

For missing financial JSON, invoke `$fetch-financials TICKER` in auto mode rather than calling a data provider directly. Auto mode uses FMP when `FMP_API_KEY` is available and otherwise falls back to free SEC/Yahoo data.

## Formal Review Gate

The QC pass is mandatory after the deterministic memo is written. A manual review by the calculation pass is not a substitute for running `$quality-control`.

When the draft memo is first written, add or update these YAML frontmatter fields:

```yaml
formal_qc_run: false
qc_status: pending
qc_completed_at: null
qc_result: null
```

After the draft exists, run `$quality-control calc-oe "COMPANY"`. The QC helper must edit the memo in place and set `formal_qc_run: true`, `qc_status`, `qc_completed_at`, and `qc_result`.

Do not report the workflow as complete unless `formal_qc_run: true` is present in the final memo. If QC cannot run, report the workflow as incomplete and state that formal QC is missing.

## Workflow

1. Resolve the research context.
   - Resolve the research root from `--research-base`, `RESEARCH_BASE_PATH`, `.codex/settings.local.json`, or the repo-local `research/` default.
   - Search under that research root, not the repo working directory.

2. Check prerequisites.
   - Find annual-filing synthesis memos:

```text
$RESEARCH_ROOT/[Company]/1.1-Annual-Filings/*Synthesis - Memo*.md
```

   - Stop if no synthesis memos exist and tell the user to run `$synthesize-annual-filing`.
   - Find financial JSONs in `1.3-Financial-Statements/`:
     - `*-income-statement.json`
     - `*-cash-flow.json`
   - If either JSON is missing, resolve ticker from the user input or the newest filing memo YAML, then invoke `$fetch-financials TICKER` and re-check.

3. Determine business type.
   - Prefer explicit classification in `2.1-Business-Economics/Business Economics Analysis - *.md` when present.
   - Otherwise infer from annual-filing memos.
   - Supported script values:
     - `general-operating`
     - `insurance`
     - `reit`
     - `bank-lender`
     - `asset-heavy-industrial`
     - `aircraft-lessor`
     - `exchange-asset-light`
   - If the company does not fit one of these, stop and explain what formula support should be added.

4. Pick conservative assumptions.
   - SBC is always deducted.
   - Maintenance capex defaults:
     - `exchange-asset-light`: 100% of total capex
     - `insurance` and `bank-lender`: 0% unless source documents support a capex adjustment
     - all others: 50% of total capex unless source documents support a better assumption
   - If one-time adjustments are supportable from 10-K memos, apply them manually after the script output and document year, amount, and rationale. Do not exclude recurring items.

5. Run the deterministic calculation from this skill directory:

```bash
cd .codex/skills/calc-oe
python3 scripts/calc_owners_earnings.py --company "COMPANY" --business-type general-operating
python3 scripts/calc_owners_earnings.py --company "COMPANY" --ticker TICKER --business-type exchange-asset-light --maint-capex-rate 1.0
```

   - Use `--research-base PATH` only for tests or unusual local setups.
   - Use `--timestamp YYYY-MM-DD-HHMM` only when deterministic filenames are needed.

6. Review and edit the output.
   - Read the generated memo.
   - Add or correct any source-backed company-specific adjusted metrics, SBC overrides, one-time adjustments, or maintenance capex disclosures.
   - Preserve the script's arithmetic unless you can trace a correction to source documents.

7. Run quality control.
   - Invoke `$quality-control calc-oe "COMPANY"` after the memo exists.
   - Use `references/phase-2-qc-prompt.md` as the review rubric if the helper skill is not automatically loaded.

8. Report results.
   - Include output path, business type, years calculated, QC status, and remaining flags.

## Guardrails

- This is a calculation, not a thesis. Keep the output numerical, sourced, and conservative.
- Do not modify skill definitions or settings files.
- Do not use direct provider API calls. Use `$fetch-financials` for missing statement data.
- Do not calculate OE for an unsupported business type with a generic fallback.
- Do not treat stock-based compensation as free. Deduct it every year unless source documents prove it is genuinely zero.
- Do not double-count SBC by deducting SBC and also applying a separate dilution penalty.
