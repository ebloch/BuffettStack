---
name: fetch-financials
description: Fetch and store income statement, balance sheet, and cash flow statement data from FMP into the investment research folder. Use when explicitly invoked as $fetch-financials with a ticker, optionally with --quarterly or --force.
---

# Fetch Financials

Use this skill to fetch financial statements from FMP and store them as canonical JSON plus a human-readable Markdown summary under the research root.

## Inputs

Accept invocation text after `$fetch-financials`:

```text
TICKER [--quarterly] [--force]
```

Examples:

- `CME`
- `AAPL --quarterly`
- `CME --force`

If the ticker is missing or ambiguous, ask for it before fetching.

## Resources

This skill is self-contained. Use these bundled files instead of `.claude` paths:

- `scripts/fmp-financials.sh` wraps FMP statement/profile endpoints.
- `scripts/fetch_financials.py` orchestrates fetch, transform, merge, and Markdown output.
- `scripts/test_fetch_financials.py` tests deterministic transform behavior.

Do not call FMP with `curl` directly. The Python script calls the bundled shell wrapper, which requires `FMP_API_KEY`.

## Workflow

1. Parse the invocation text.
   - Extract ticker.
   - Detect `--quarterly` to fetch 20 quarterly periods in addition to 10 annual periods.
   - Detect `--force` to overwrite existing annual/quarterly cache data instead of merging.

2. Prepare the environment.
   - Read the research root from `.claude/settings.local.json` at `env.RESEARCH_BASE_PATH`.
   - Run from this skill directory so bundled paths resolve:

```bash
cd .codex/skills/fetch-financials
```

3. Run the bundled orchestrator:

```bash
python3 scripts/fetch_financials.py TICKER
python3 scripts/fetch_financials.py TICKER --quarterly
python3 scripts/fetch_financials.py TICKER --force
```

4. Confirm outputs.
   - The script writes to:

```text
$RESEARCH_BASE_PATH/[Company]/1.3-Financial-Statements/
  TICKER-income-statement.json
  TICKER-balance-sheet.json
  TICKER-cash-flow.json
  Financial Statements - [Company].md
```

5. Report status.
   - Include company name, ticker, annual year coverage, quarterly coverage if fetched, and all files created or updated.
   - Report any script error clearly. If `FMP_API_KEY` is missing, ask the user to set it rather than trying another API path.

## Behavior

- Existing JSON files are merged by default: newly fetched years/quarters overwrite matching periods, while older cached periods are preserved.
- `--force` rebuilds the JSON files only from the fresh fetch.
- Folder selection uses the FMP company name, but reuses an existing matching company folder under `RESEARCH_BASE_PATH` when possible.
- The Markdown file is a view over the JSON files. Treat JSON as canonical data.

## Guardrails

- Use `RESEARCH_BASE_PATH`, not the repo working directory, for research outputs.
- Do not modify `.claude/**`, `CLAUDE.md`, or existing Claude skill files.
- Do not invent missing fields. Leave unavailable values as `null` in JSON and blank cells in Markdown.
- Do not use direct `curl` calls with `FMP_API_KEY`.
