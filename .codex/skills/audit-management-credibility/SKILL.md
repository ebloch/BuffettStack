---
name: audit-management-credibility
description: Audit management credibility by comparing promises, guidance, capital allocation claims, and execution outcomes across filings, transcripts, and investor materials. Use when explicitly invoked as $audit-management-credibility with a company name or ticker.
---

# Audit Management Credibility

Use this skill to produce a detailed promise-versus-delivery analysis and concise memo on management credibility, candor, and capital allocation quality.

## Inputs

Accept invocation text after `$audit-management-credibility`:

```text
COMPANY_OR_TICKER
```

If no company or ticker is provided, ask for it. Resolve ambiguous tickers or company folders before writing output.

## Resources

This skill is self-contained. Use these bundled files:

- `scripts/fmp-fetch.sh` for FMP transcript and press-release fetches when `FMP_API_KEY` is available.
- `references/phase-1-synthesis-prompt.md` for the synthesis pass.
- `references/phase-2-qc-prompt.md` for the quality-control pass.
- `references/phase-3-audit-prompt.md` for the compliance-audit pass.
- `references/output-template-analysis.md` for detailed analysis structure.
- `references/output-template-memo.md` for concise memo structure.
- `references/validation-checklist.md` for completion checks.

Run synthesis locally, then invoke `$quality-control` and `$audit-output` as explicit helper skills for the review passes.

## Formal Review Gate

The review passes are mandatory and sequential. A manual review by the synthesis pass is not a substitute for running the helper skills.

When the draft outputs are first written, add or update these YAML frontmatter fields in each output:

```yaml
formal_qc_run: false
formal_audit_run: false
qc_status: pending
audit_status: blocked_until_qc_complete
qc_completed_at: null
audit_completed_at: null
qc_result: null
audit_result: null
```

After the draft outputs exist, run `$quality-control audit-management-credibility "COMPANY"` first. The QC helper must edit the outputs in place and set `formal_qc_run: true`, `qc_status`, `qc_completed_at`, and `qc_result`.

Only after formal QC is complete or partial, run `$audit-output audit-management-credibility "COMPANY"`. The audit helper must edit the outputs in place and set `formal_audit_run: true`, `audit_status`, `audit_completed_at`, and `audit_result`.

Do not report the workflow as complete unless `formal_qc_run: true` and `formal_audit_run: true` are present in the final outputs. If either helper pass cannot run, report the workflow as incomplete and state exactly which pass is missing.

## Workflow

1. Resolve the research context.
   - Resolve the research root from `RESEARCH_BASE_PATH`, `.codex/settings.local.json`, or the repo-local `research/` default.
   - Use that research root for prerequisite reads and output writes.
   - Search under the research root for the company folder.
   - Generate a timestamp with `date "+%Y-%m-%d-%H%M"`.

2. Gather source context.
   - Prefer annual-filing synthesis memos in `1.1-Annual-Filings/`.
   - Include investor presentation memos in `1.2-Investor-Presentations/` when present.
   - Include earnings or transcript material in `1.4-Earnings/` when present.
   - Use `scripts/fmp-fetch.sh` for FMP transcript and press-release fetches when local source coverage is insufficient and `FMP_API_KEY` is available; do not call FMP APIs directly.
   - If `FMP_API_KEY` is not available, use free sources instead: company IR sites, SEC filings, earnings-call transcript pages found through web search, press-release feeds, and existing local `1.4-Earnings/` files. Mark the source as web search/IR/SEC in the output.
   - Exclude files containing `QC`, `Audit`, `Gap`, or `Improve` unless they are the target of review.

3. Pre-compute output paths.

```text
$RESEARCH_BASE_PATH/[Company]/2.4-Management-Audit/Management Credibility - Analysis - [Company] - [TIMESTAMP].md
$RESEARCH_BASE_PATH/[Company]/2.4-Management-Audit/Management Credibility - Memo - [Company] - [TIMESTAMP].md
```

4. Run the synthesis pass.
   - Read `references/phase-1-synthesis-prompt.md`, both output templates, and `references/validation-checklist.md`.
   - Fill placeholders with company, ticker if known, timestamp, output paths, and source paths.
   - Score every verifiable promise on the required scale, document misses explicitly, and reconcile scorecard math.
   - Write both outputs to the pre-computed paths.

5. Run quality control.
   - Invoke `$quality-control audit-management-credibility "COMPANY"` after both outputs exist.
   - Use `references/phase-2-qc-prompt.md` as the bridge prompt if invoking the helper manually.

6. Run the compliance audit.
   - Invoke `$audit-output audit-management-credibility "COMPANY"` after QC.
   - The helper must load this skill's `SKILL.md`, both output templates, and `references/validation-checklist.md`.
   - Use `references/phase-3-audit-prompt.md` as the bridge prompt if invoking the helper manually.

7. Report results.
   - Include analysis path, memo path, scorecard status, QC status, audit status, and remaining flags.

## Guardrails

- Run bundled scripts from `.codex/skills/audit-management-credibility` so `scripts/fmp-fetch.sh` resolves correctly.
- Do not infer a promise unless management made a specific claim, target, guidance item, or capital allocation commitment.
- Separate controllable execution from macro-driven outcomes.
- Keep score math transparent and consistent between the analysis and memo.
- Do not modify skill definitions or settings files while running this skill.
