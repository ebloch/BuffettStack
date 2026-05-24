---
name: scenario-analysis
description: Create qualitative 10-year forward scenarios with probability assignments from existing company research, without financial projections or return calculations. Use when explicitly invoked as $scenario-analysis with a company name or ticker.
---

# Scenario Analysis

Use this skill to synthesize prior research into plausible 10-year future paths. This is qualitative scenario work with probability assignments, not a valuation model.

## Inputs

Accept invocation text after `$scenario-analysis`:

```text
COMPANY_OR_TICKER
```

If no company or ticker is provided, ask for it. Resolve ambiguous tickers or company folders before writing output.

## Resources

This skill is self-contained. Use these bundled files:

- `references/phase-1-synthesis-prompt.md` for the synthesis pass.
- `references/phase-2-qc-prompt.md` for the quality-control pass.
- `references/phase-3-audit-prompt.md` for the compliance-audit pass.
- `references/output-template.md` for scenario memo structure.
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

After the draft exists, run `$quality-control scenario-analysis "COMPANY"` first. The QC helper must edit the output in place and set `formal_qc_run: true`, `qc_status`, `qc_completed_at`, and `qc_result`.

Only after formal QC is complete or partial, run `$audit-output scenario-analysis "COMPANY"`. The audit helper must edit the output in place and set `formal_audit_run: true`, `audit_status`, `audit_completed_at`, and `audit_result`.

Do not report the workflow as complete unless `formal_qc_run: true` and `formal_audit_run: true` are present in the final output. If either helper pass cannot run, report the workflow as incomplete and state exactly which pass is missing.

## Workflow

1. Resolve the research context.
   - Resolve the research root from `RESEARCH_BASE_PATH`, `.codex/settings.local.json`, or the repo-local `research/` default.
   - Use that research root for prerequisite reads and output writes.
   - Search under the research root for the company folder.
   - Generate a timestamp with `date "+%Y-%m-%d-%H%M"`.

2. Check prerequisites.
   - Require business overview: `$RESEARCH_BASE_PATH/[Company]/*Overview*.md`.
   - Require management audit: `$RESEARCH_BASE_PATH/[Company]/2.4-Management-Audit/*.md`.
   - Require financial data: `$RESEARCH_BASE_PATH/[Company]/1.3-Financial-Statements/*.md`.
   - Require moat strength analysis: `$RESEARCH_BASE_PATH/[Company]/2.6-Moat-Strength/*.md`.
   - Require risk assessment: `$RESEARCH_BASE_PATH/[Company]/2.5-Risk-Assessment/*.md`.
   - Treat investor presentation memos in `1.2-Investor-Presentations/` as optional strategy context.
   - Exclude files containing `QC`, `Audit`, `Gap`, or `Improve`.
   - Stop if required research is missing and list only the missing prerequisite skills.

3. Pre-compute the output path.

```text
$RESEARCH_BASE_PATH/[Company]/3.3-Scenarios/10-Year Scenario Analysis - [Company] - [TIMESTAMP].md
```

4. Run the synthesis pass.
   - Read `references/phase-1-synthesis-prompt.md`, `references/output-template.md`, and `references/validation-checklist.md`.
   - Fill placeholders with company, ticker if known, output path, prerequisite source paths, and optional investor presentation paths.
   - Write detailed base, bull, bear, and other required scenario narratives with probabilities that sum to 100%.
   - Do not include financial projections, CAGRs, return calculations, or price targets.

5. Run quality control.
   - Invoke `$quality-control scenario-analysis "COMPANY"` after the output exists.
   - Use `references/phase-2-qc-prompt.md` as the bridge prompt if invoking the helper manually.

6. Run the compliance audit.
   - Invoke `$audit-output scenario-analysis "COMPANY"` after QC.
   - The helper must load this skill's `SKILL.md`, `references/output-template.md`, and `references/validation-checklist.md`.
   - Use `references/phase-3-audit-prompt.md` as the bridge prompt if invoking the helper manually.

7. Report results.
   - Include output path, scenario probabilities, QC status, audit status, and remaining flags.

## Guardrails

- Probability percentages are the only required numbers; this skill should not become valuation work.
- Scenarios must diverge on business drivers, not just sentiment.
- Make thesis killers visible in bear cases and execution upside visible in bull cases.
- Do not modify skill definitions or settings files while running this skill.
