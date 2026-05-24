---
name: run-fisher-analysis
description: Score a company against Philip Fisher's 15-point checklist using existing research, financial data, management analysis, moat work, and risk assessment. Use when explicitly invoked as $run-fisher-analysis with a company name or ticker.
---

# Run Fisher Analysis

Use this skill to produce an evidence-backed Philip Fisher 15-point checklist score and verdict for a company.

## Inputs

Accept invocation text after `$run-fisher-analysis`:

```text
COMPANY_OR_TICKER
```

If no company or ticker is provided, ask for it. Resolve ambiguous tickers or company folders before writing output.

## Resources

This skill is self-contained. Use these bundled files:

- `references/phase-1-analysis-prompt.md` for the 15-point analysis pass.
- `references/phase-2-qc-prompt.md` for the quality-control pass.
- `references/phase-3-audit-prompt.md` for the compliance-audit pass.
- `references/output-template.md` for analysis structure.
- `references/validation-checklist.md` for completion checks.

Run analysis locally, then invoke `$quality-control` and `$audit-output` as explicit helper skills for the review passes.

## Formal Review Gate

The review passes are mandatory and sequential. A manual review by the synthesis pass is not a substitute for running the helper skills.

When the draft output is first written, add or update these YAML frontmatter fields:

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

After the draft exists, run `$quality-control run-fisher-analysis "COMPANY"` first. The QC helper must edit the output in place and set `formal_qc_run: true`, `qc_status`, `qc_completed_at`, and `qc_result`.

Only after formal QC is complete or partial, run `$audit-output run-fisher-analysis "COMPANY"`. The audit helper must edit the output in place and set `formal_audit_run: true`, `audit_status`, `audit_completed_at`, and `audit_result`.

Do not report the workflow as complete unless `formal_qc_run: true` and `formal_audit_run: true` are present in the final output. If either helper pass cannot run, report the workflow as incomplete and state exactly which pass is missing.

## Workflow

1. Resolve the research context.
   - Resolve the research root from `RESEARCH_BASE_PATH`, `.codex/settings.local.json`, or the repo-local `research/` default.
   - Use that research root for prerequisite reads and output writes.
   - Search under the research root for the company folder.
   - Generate a timestamp with `date "+%Y-%m-%d-%H%M"`.

2. Check prerequisites.
   - Require annual-filing synthesis research in `1.1-Annual-Filings/`.
   - Require financial data in `1.3-Financial-Statements/`.
   - Require management credibility research in `2.4-Management-Audit/`.
   - Require at least one moat source from `2.2-Scuttlebutt/`, `2.3-Competitive-Landscape/`, or `2.6-Moat-Strength/`.
   - Require risk assessment research in `2.5-Risk-Assessment/`.
   - Exclude files containing `QC`, `Audit`, `Gap`, or `Improve`.
   - Stop if required research is missing and list only the missing prerequisite skills.

3. Pre-compute the output path.

```text
$RESEARCH_BASE_PATH/[Company]/3.1-Fisher-Checklist/Fisher 15-Point Checklist - Analysis - [Company] - [TIMESTAMP].md
```

4. Run the analysis pass.
   - Read `references/phase-1-analysis-prompt.md`, `references/output-template.md`, and `references/validation-checklist.md`.
   - Fill placeholders with company, ticker if known, output path, and source paths.
   - Score all 15 Fisher points with evidence and compute the total score and verdict.
   - Write the analysis to the pre-computed output path.

5. Run quality control.
   - Invoke `$quality-control run-fisher-analysis "COMPANY"` after the output exists.
   - Use `references/phase-2-qc-prompt.md` as the bridge prompt if invoking the helper manually.

6. Run the compliance audit.
   - Invoke `$audit-output run-fisher-analysis "COMPANY"` after QC.
   - The helper must load this skill's `SKILL.md`, `references/output-template.md`, and `references/validation-checklist.md`.
   - Use `references/phase-3-audit-prompt.md` as the bridge prompt if invoking the helper manually.

7. Report results.
   - Include output path, total score, verdict, QC status, audit status, and remaining flags.

## Guardrails

- Score every point from evidence; do not give benefit of doubt where research is thin.
- Keep scoring consistent with the rubric in the output template.
- Mark unknown items explicitly rather than filling gaps with memory.
- Do not modify skill definitions or settings files while running this skill.
