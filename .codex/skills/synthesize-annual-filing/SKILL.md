---
name: synthesize-annual-filing
description: Synthesize a company's annual filing into an investment research memo. Use when explicitly invoked as $synthesize-annual-filing for a 10-K, 20-F, 40-F, Universal Registration Document, UK Annual Report, Integrated Report, or local/URL PDF annual filing.
---

# Annual Filing Synthesis

Use this skill to turn one fiscal year of a company's annual filing into a structured investment research memo with synthesis, quality control, and compliance audit passes.

## Inputs

Accept invocation text after `$synthesize-annual-filing` in one of these forms:

```text
TICKER YEAR
TICKER YEAR /path/to/annual-report.pdf
TICKER YEAR https://example.com/annual-report.pdf
```

Examples:

- `CME 2024`
- `AAPL 2023`
- `8058.T 2024 /path/to/mitsubishi_ir_2024.pdf`
- `RMS.PA 2024 https://example.com/hermes_urd.pdf`

If the ticker, year, or PDF source is ambiguous, ask for the missing detail before fetching or writing.

## Resources

This skill is self-contained. Use these bundled files:

- `scripts/parse_annual_filing.py` for SEC filings.
- `scripts/parse_pdf_filing.py` for local or URL PDF filings.
- `scripts/requirements-parsing.txt` for parser dependencies.
- `references/phase-1-synthesis-prompt.md` for the synthesis pass.
- `references/phase-2-qc-prompt.md` for the quality-control pass.
- `references/phase-3-audit-prompt.md` for the compliance-audit pass.
- `references/output-template.md` for memo structure.
- `references/validation-checklist.md` for completion checks.
- `references/industry-checklists/` for industry-specific requirements.

When running bundled scripts, first work from this skill directory (`.codex/skills/synthesize-annual-filing`) so relative paths like `scripts/parse_annual_filing.py` resolve correctly.

Run synthesis locally, then invoke `$quality-control` and `$audit-output` as explicit helper skills for the review passes.
If the runtime does not automatically load those helper skills, read `.codex/skills/quality-control/SKILL.md` and `.codex/skills/audit-output/SKILL.md` directly and follow them.

For separate structured financial statement JSON, use `$fetch-financials TICKER`. It now supports FMP side-by-side with a free SEC-first path: FMP is used when `FMP_API_KEY` exists, otherwise SEC EDGAR Company Facts is used with Yahoo Finance only as supplemental metadata.

## Workflow

1. Parse the invocation text.
   - Extract ticker, fiscal year, and optional PDF source.
   - Process exactly one fiscal year per run.
   - Treat URL or local PDF input as `pdf` mode; otherwise use `sec` mode.

2. Prepare the environment.
   - Resolve the research root from `RESEARCH_BASE_PATH`, `.codex/settings.local.json`, or the repo-local `research/` default.
   - Use that research root for all research reads and output writes.
   - Generate a timestamp with `date "+%Y-%m-%d-%H%M"`.
   - Pre-compute the output path:

```text
$RESEARCH_ROOT/[Company]/1.1-Annual-Filings/FY[Year] - [Company] - [FORM_TYPE] Synthesis - Memo - [TIMESTAMP].md
```

3. Parse the filing only with bundled scripts.
   - SEC mode: `python3 scripts/parse_annual_filing.py TICKER --year YEAR`
   - PDF mode: `python3 scripts/parse_pdf_filing.py PDF_SOURCE --json`
   - Do not create ad hoc Python scripts, use heredocs, or use `python3 -c` to work around parser failures.
   - If dependencies are missing, tell the user to install `scripts/requirements-parsing.txt` and stop unless they approve installation.

4. Run the synthesis pass.
   - Read `references/phase-1-synthesis-prompt.md`, `references/output-template.md`, and the relevant industry checklist.
   - Fill placeholders with company, ticker, year, form type, accounting standard, parsing mode, PDF source if any, and output path.
   - Write the memo to the pre-computed output path.

5. Run the quality-control pass.
   - Invoke `$quality-control` with `synthesize-annual-filing "[Company]" FY[Year]`.
   - The helper must re-read the source filing through this skill's bundled parser and surgically edit the memo for factual gaps, missing evidence, thin analysis, or template misses.
   - Use `references/phase-2-qc-prompt.md` as the bridge prompt if invoking the helper from this workflow.

6. Run the compliance-audit pass.
   - Invoke `$audit-output` with `synthesize-annual-filing "[Company]" FY[Year]`.
   - The helper must load this skill's `SKILL.md`, `references/output-template.md`, `references/validation-checklist.md`, and relevant industry checklist.
   - Use `references/phase-3-audit-prompt.md` as the bridge prompt if invoking the helper from this workflow.
   - Report any flag-only issues clearly in the final summary.

7. Report results.
   - Include the final memo path.
   - Summarize synthesis, QC, and audit status.
   - List flagged issues needing manual review.

## Guardrails

- Prefer existing research and source filings over memory.
- Preserve source quotes accurately and keep citations/page references when available.
- Do not invent missing filing data. Put unresolved questions in the memo's questions section or final flagged issues.
- Do not modify skill definitions or settings files while running this skill.
- If a phase fails after the memo exists, continue to later review phases when possible and report partial completion.
