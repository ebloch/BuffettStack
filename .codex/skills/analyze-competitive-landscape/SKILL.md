---
name: analyze-competitive-landscape
description: Analyze a company external competitive environment including industry structure, market share, Porter's Five Forces, value chain economics, profit pools, and emerging threats. Use when explicitly invoked as $analyze-competitive-landscape with a company name or ticker.
---

# Analyze Competitive Landscape

Use this skill to produce an external battlefield view: who competes with the company, where economics accrue, how power is distributed, and which threats could reshape returns.

## Inputs

Accept invocation text after `$analyze-competitive-landscape`:

```text
COMPANY_OR_TICKER
```

If no company or ticker is provided, ask for it. Resolve ambiguous tickers or company folders before writing output.

## Resources

This skill is self-contained. Use these bundled files:

- `references/phase-1-synthesis-prompt.md` for the synthesis pass.
- `references/phase-2-qc-prompt.md` for the quality-control pass.
- `references/phase-3-audit-prompt.md` for the compliance-audit pass.
- `references/output-template.md` for analysis structure.
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

After the draft exists, run `$quality-control analyze-competitive-landscape "COMPANY"` first. The QC helper must edit the output in place and set `formal_qc_run: true`, `qc_status`, `qc_completed_at`, and `qc_result`.

Only after formal QC is complete or partial, run `$audit-output analyze-competitive-landscape "COMPANY"`. The audit helper must edit the output in place and set `formal_audit_run: true`, `audit_status`, `audit_completed_at`, and `audit_result`.

Do not report the workflow as complete unless `formal_qc_run: true` and `formal_audit_run: true` are present in the final output. If either helper pass cannot run, report the workflow as incomplete and state exactly which pass is missing.

## Workflow

1. Resolve the research context.
   - Resolve the research root from `RESEARCH_BASE_PATH`, `.codex/settings.local.json`, or the repo-local `research/` default.
   - Use that research root for prerequisite reads and output writes.
   - Search under the research root for the company folder.
   - Generate a timestamp with `date "+%Y-%m-%d-%H%M"`.

2. Check prerequisites.
   - Require at least one annual-filing synthesis memo: `$RESEARCH_BASE_PATH/[Company]/1.1-Annual-Filings/*Synthesis - Memo*.md`.
   - Require scuttlebutt research: `$RESEARCH_BASE_PATH/[Company]/2.2-Scuttlebutt/*.md`.
   - Exclude files containing `QC`, `Audit`, `Gap`, or `Improve`.
   - Stop if prerequisites are missing and tell the user to run `$synthesize-annual-filing` or `$scuttlebutt` first.

3. Pre-compute the output path.

```text
$RESEARCH_BASE_PATH/[Company]/2.3-Competitive-Landscape/Competitive Landscape - Analysis - [Company] - [TIMESTAMP].md
```

4. Run the synthesis pass.
   - Read `references/phase-1-synthesis-prompt.md`, `references/output-template.md`, and `references/validation-checklist.md`.
   - Fill placeholders with company, ticker if known, timestamp, output path, annual-filing memo paths, and scuttlebutt paths.
   - Use current public web research where needed for competitors, market share, industry data, and emerging threats.
   - Write the analysis to the pre-computed output path.

5. Run quality control.
   - Invoke `$quality-control analyze-competitive-landscape "COMPANY"` after the output exists.
   - Use `references/phase-2-qc-prompt.md` as the bridge prompt if invoking the helper manually.

6. Run the compliance audit.
   - Invoke `$audit-output analyze-competitive-landscape "COMPANY"` after QC.
   - The helper must load this skill's `SKILL.md`, `references/output-template.md`, and `references/validation-checklist.md`.
   - Use `references/phase-3-audit-prompt.md` as the bridge prompt if invoking the helper manually.

7. Report results.
   - Include output path, source paths, QC status, audit status, and remaining flags.

## Guardrails

- This is external competitive analysis; use `$analyze-moat-strength` for internal durability scoring.
- Do not rely on memory for current market shares, competitors, or regulatory changes; search and cite current sources when needed.
- Distinguish direct competitors, substitutes, suppliers, customers, regulators, and ecosystem partners.
- Do not modify skill definitions or settings files while running this skill.
