---
name: analyze-business-economics
description: Analyze a company business model, unit economics, accounting quirks, and key operating metrics from existing business overview and annual filing research. Use when explicitly invoked as $analyze-business-economics with a company name or ticker.
---

# Analyze Business Economics

Use this skill to produce a source-grounded business economics memo that identifies how the company makes money, what drives returns, which accounting conventions matter, and which metrics deserve ongoing monitoring.

## Inputs

Accept invocation text after `$analyze-business-economics`:

```text
COMPANY_OR_TICKER
```

If no company or ticker is provided, ask for it. Resolve ambiguous tickers or company folders before writing output.

## Resources

This skill is self-contained. Use these bundled files:

- `references/phase-1-synthesis-prompt.md` for the synthesis pass.
- `references/phase-2-qc-prompt.md` for the quality-control pass.
- `references/phase-3-audit-prompt.md` for the compliance-audit pass.
- `references/output-template.md` for memo structure.
- `references/validation-checklist.md` for completion checks.
- `references/industry-checklists/` for industry-specific metrics and accounting quirks.

Run synthesis locally, then invoke `$quality-control` and `$audit-output` as explicit helper skills for the review passes. If those helpers are not automatically loaded, read their `.codex/skills/.../SKILL.md` files directly and follow them.

## Formal Review Gate

The review passes are mandatory and sequential. A manual review by the synthesis pass is not a substitute for running the helper skills.

When the draft memo is first written, add or update these YAML frontmatter fields:

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

After the draft exists, run `$quality-control analyze-business-economics "COMPANY"` first. The QC helper must edit the memo in place and set `formal_qc_run: true`, `qc_status`, `qc_completed_at`, and `qc_result`.

Only after formal QC is complete or partial, run `$audit-output analyze-business-economics "COMPANY"`. The audit helper must edit the memo in place and set `formal_audit_run: true`, `audit_status`, `audit_completed_at`, and `audit_result`.

Do not report the workflow as complete unless `formal_qc_run: true` and `formal_audit_run: true` are present in the final memo. If either helper pass cannot run, report the workflow as incomplete and state exactly which pass is missing.

## Workflow

1. Resolve the research context.
   - Resolve the research root from `RESEARCH_BASE_PATH`, `.codex/settings.local.json`, or the repo-local `research/` default.
   - Use that research root for all prerequisite reads and output writes.
   - Search under the research root for the company folder before creating new paths.
   - Generate a timestamp with `date "+%Y-%m-%d-%H%M"`.

2. Check prerequisites.
   - Require the company business overview: `$RESEARCH_BASE_PATH/[Company]/[Company] - Business Overview*.md`.
   - Require the most recent annual-filing synthesis memo: `$RESEARCH_BASE_PATH/[Company]/1.1-Annual-Filings/*Synthesis - Memo*.md`.
   - Exclude files containing `QC`, `Audit`, `Gap`, or `Improve`.
   - Stop if either prerequisite is missing and tell the user to run `$company-overview` or `$synthesize-annual-filing` first.

3. Pre-compute the output path.

```text
$RESEARCH_BASE_PATH/[Company]/2.1-Business-Economics/Business Economics Analysis - [Company] - [TIMESTAMP].md
```

4. Run the synthesis pass.
   - Read `references/phase-1-synthesis-prompt.md`, `references/output-template.md`, `references/validation-checklist.md`, and the relevant industry checklist when available.
   - Fill placeholders with company, ticker if known, timestamp, output path, business overview path, and annual-filing memo path.
   - Write the memo to the pre-computed output path.

5. Run quality control.
   - Invoke `$quality-control analyze-business-economics "COMPANY"` after the memo exists.
   - Use `references/phase-2-qc-prompt.md` as the bridge prompt if invoking the helper manually.

6. Run the compliance audit.
   - Invoke `$audit-output analyze-business-economics "COMPANY"` after QC.
   - The helper must load this skill's `SKILL.md`, `references/output-template.md`, `references/validation-checklist.md`, and any relevant industry checklist.
   - Use `references/phase-3-audit-prompt.md` as the bridge prompt if invoking the helper manually.

7. Report results.
   - Include output path, source paths, selected industry checklist, QC status, audit status, and remaining flags.

## Guardrails

- Treat this as business-model analysis, not valuation or investment recommendation.
- Prefer source documents over memory; do not invent operating metrics or accounting details.
- Preserve source dates and citation context where available.
- Do not modify skill definitions or settings files while running this skill.
- If a review phase fails after the memo exists, continue when possible and report partial completion.
