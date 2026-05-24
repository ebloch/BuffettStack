---
name: analyze-investment-risks
description: Analyze investment risks for a company, including risk categories, severity matrix, thesis killers, monitoring dashboard, and downside scenarios. Use when explicitly invoked as $analyze-investment-risks with a company name or ticker.
---

# Analyze Investment Risks

Use this skill to produce a comprehensive risk assessment that answers what could go wrong, what would kill the thesis, and which indicators should be monitored.

## Inputs

Accept invocation text after `$analyze-investment-risks`:

```text
COMPANY_OR_TICKER
```

If no company or ticker is provided, ask for it. Resolve ambiguous tickers or company folders before writing output.

## Resources

This skill is self-contained. Use these bundled files:

- `references/phase-1-synthesis-prompt.md` for the synthesis pass.
- `references/phase-2-qc-prompt.md` for the quality-control pass.
- `references/phase-3-audit-prompt.md` for the compliance-audit pass.
- `references/output-template.md` for risk analysis structure.
- `references/validation-checklist.md` for completion checks.

Run synthesis locally, then invoke `$quality-control` and `$audit-output` as explicit helper skills for the review passes.

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

After the draft exists, run `$quality-control analyze-investment-risks "COMPANY"` first. The QC helper must edit the output in place and set `formal_qc_run: true`, `qc_status`, `qc_completed_at`, and `qc_result`.

Only after formal QC is complete or partial, run `$audit-output analyze-investment-risks "COMPANY"`. The audit helper must edit the output in place and set `formal_audit_run: true`, `audit_status`, `audit_completed_at`, and `audit_result`.

Do not report the workflow as complete unless `formal_qc_run: true` and `formal_audit_run: true` are present in the final output. If either helper pass cannot run, report the workflow as incomplete and state exactly which pass is missing.

## Workflow

1. Resolve the research context.
   - Resolve the research root from `RESEARCH_BASE_PATH`, `.codex/settings.local.json`, or the repo-local `research/` default.
   - Use that research root for prerequisite reads and output writes.
   - Search under the research root for the company folder.
   - Generate a timestamp with `date "+%Y-%m-%d-%H%M"`.

2. Check prerequisites.
   - Require annual-filing synthesis research: `$RESEARCH_BASE_PATH/[Company]/1.1-Annual-Filings/*.md`.
   - Require moat analysis: `$RESEARCH_BASE_PATH/[Company]/2.6-Moat-Strength/*.md`.
   - Require management audit: `$RESEARCH_BASE_PATH/[Company]/2.4-Management-Audit/*.md`.
   - Exclude files containing `QC`, `Audit`, `Gap`, or `Improve`.
   - Stop if required research is missing and list the exact skill to run first: `$synthesize-annual-filing`, `$analyze-moat-strength`, or `$audit-management-credibility`.

3. Pre-compute the output path.

```text
$RESEARCH_BASE_PATH/[Company]/2.5-Risk-Assessment/Risk Assessment - Analysis - [Company] - [TIMESTAMP].md
```

4. Run the synthesis pass.
   - Read `references/phase-1-synthesis-prompt.md`, `references/output-template.md`, and `references/validation-checklist.md`.
   - Fill placeholders with company, ticker if known, timestamp, output path, and prerequisite source paths.
   - Cover all required risk categories, thesis killers, scenario implications, and monitoring indicators.
   - Write the analysis to the pre-computed output path.

5. Run quality control.
   - Invoke `$quality-control analyze-investment-risks "COMPANY"` after the output exists.
   - Use `references/phase-2-qc-prompt.md` as the bridge prompt if invoking the helper manually.

6. Run the compliance audit.
   - Invoke `$audit-output analyze-investment-risks "COMPANY"` after QC.
   - The helper must load this skill's `SKILL.md`, `references/output-template.md`, and `references/validation-checklist.md`.
   - Use `references/phase-3-audit-prompt.md` as the bridge prompt if invoking the helper manually.

7. Report results.
   - Include output path, source paths, severity-score status, QC status, audit status, and remaining flags.

## Guardrails

- Include the scoring rubric from the output template so severity calculations are auditable.
- Do not soften thesis killers; separate probability from severity.
- Distinguish company-specific risks from generic market noise.
- Do not modify skill definitions or settings files while running this skill.
