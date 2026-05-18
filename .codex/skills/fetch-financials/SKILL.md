---
name: fetch-financials
description: Fetch and store income statement, balance sheet, and cash flow statement data into the investment research folder. Use when explicitly invoked as $fetch-financials with a ticker, optionally with --quarterly, --force, or --source.
---

# Fetch Financials

Use this skill to fetch financial statements and store them as canonical JSON plus a human-readable Markdown summary under the research root.

Default source behavior is `--source auto`: use FMP when `FMP_API_KEY` is available; otherwise use free SEC EDGAR Company Facts with Yahoo Finance quote/profile data only as supplemental metadata.

## Inputs

Accept invocation text after `$fetch-financials`:

```text
TICKER [--quarterly] [--force] [--source auto|fmp|free]
```

Examples:

- `CME`
- `AAPL --quarterly`
- `CME --force`
- `AAPL --source free`
- `AAPL --source fmp`

If the ticker is missing or ambiguous, ask for it before fetching.

## Resources

This skill is self-contained. Use these bundled files:

- `scripts/fmp-financials.sh` wraps FMP statement/profile endpoints.
- `scripts/fetch_financials.py` orchestrates source selection, fetch, transform, merge, and Markdown output.
- `scripts/test_fetch_financials.py` tests deterministic transform behavior.

Do not call FMP with `curl` directly. The Python script calls the bundled shell wrapper when the selected source is FMP.

## Workflow

1. Parse the invocation text.
   - Extract ticker.
   - Detect `--quarterly` to fetch 20 quarterly periods in addition to 10 annual periods.
   - Detect `--force` to overwrite existing annual/quarterly cache data instead of merging.
   - Detect `--source`:
     - `auto` (default): FMP if `FMP_API_KEY` exists, otherwise free SEC/Yahoo data.
     - `fmp`: require `FMP_API_KEY` and use FMP.
     - `free`: use SEC EDGAR Company Facts for statements and Yahoo Finance only for supplemental profile/market metadata.

2. Prepare the environment.
   - Resolve the research root from `--research-base`, `RESEARCH_BASE_PATH`, `.codex/settings.local.json`, or the repo-local `research/` default.
   - Run from this skill directory so bundled paths resolve:

```bash
cd .codex/skills/fetch-financials
```

3. Run the bundled orchestrator:

```bash
python3 scripts/fetch_financials.py TICKER
python3 scripts/fetch_financials.py TICKER --quarterly
python3 scripts/fetch_financials.py TICKER --force
python3 scripts/fetch_financials.py TICKER --source free
python3 scripts/fetch_financials.py TICKER --source fmp
```

4. Confirm outputs.
   - The script writes to:

```text
$RESEARCH_ROOT/[Company]/1.3-Financial-Statements/
  TICKER-income-statement.json
  TICKER-balance-sheet.json
  TICKER-cash-flow.json
  Financial Statements - [Company].md
```

5. Report status.
   - Include company name, ticker, annual year coverage, quarterly coverage if fetched, and all files created or updated.
   - Report any script error clearly. If `--source fmp` is requested and `FMP_API_KEY` is missing, ask the user to set it or rerun with `--source free`.

## Behavior

- Existing JSON files are merged by default: newly fetched years/quarters overwrite matching periods, while older cached periods are preserved.
- `--force` rebuilds the JSON files only from the fresh fetch.
- Folder selection uses the selected provider's company name, but reuses an existing matching company folder under the resolved research root when possible.
- The Markdown file is a view over the JSON files. Treat JSON as canonical data.
- Free-source annual and quarterly statement rows include SEC provenance in `_sources` where available: taxonomy, tag, unit, form, filed date, accession, frame, and period end.
- Yahoo Finance is supplemental only in free mode; do not treat Yahoo statement tables as authoritative source data.

## Guardrails

- Use the resolved research root, not the skill directory, for research outputs.
- Do not modify skill definitions or settings files while running this skill.
- Do not invent missing fields. Leave unavailable values as `null` in JSON and blank cells in Markdown.
- Do not use direct `curl` calls with `FMP_API_KEY`.
