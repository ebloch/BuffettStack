---
name: company-overview
description: Create or refresh a company business overview from existing annual filing research, financial statements, and public context. Use when explicitly invoked as $company-overview with a company name or ticker.
---

# Company Overview

Use this skill to create the standing company overview memo that anchors later research: business description, segment economics, history, financial evolution, management, moat, risks, and key questions.

## Inputs

Accept invocation text after `$company-overview`:

```text
COMPANY_OR_TICKER
```

If no company or ticker is provided, ask for it. Resolve ambiguous tickers or company folders before writing output.

## Resources

This skill is self-contained. Use these bundled files:

- `references/phase-1-synthesis-prompt.md` for the synthesis pass.
- `references/phase-2-qc-prompt.md` for the quality-control pass.
- `references/phase-3-audit-prompt.md` for the compliance-audit pass.
- `references/output-template.md` for overview structure.
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

After the draft exists, run `$quality-control company-overview "COMPANY"` first. The QC helper must edit the output in place and set `formal_qc_run: true`, `qc_status`, `qc_completed_at`, and `qc_result`.

Only after formal QC is complete or partial, run `$audit-output company-overview "COMPANY"`. The audit helper must edit the output in place and set `formal_audit_run: true`, `audit_status`, `audit_completed_at`, and `audit_result`.

Do not report the workflow as complete unless `formal_qc_run: true` and `formal_audit_run: true` are present in the final output. If either helper pass cannot run, report the workflow as incomplete and state exactly which pass is missing.

## Workflow

1. Resolve the research context.
   - Resolve the research root from `RESEARCH_BASE_PATH`, `.codex/settings.local.json`, or the repo-local `research/` default.
   - Use that research root for prerequisite reads and output writes.
   - Search under the research root for the company folder.
   - Generate a timestamp with `date "+%Y-%m-%d-%H%M"`.

2. Gather source context.
   - Prefer annual-filing synthesis memos in `1.1-Annual-Filings/`.
   - Include financial statement summaries in `1.3-Financial-Statements/` when present.
   - Include investor presentation memos in `1.2-Investor-Presentations/` when present.
   - Search current public sources only to fill durable company context or resolve stale facts.
   - Exclude files containing `QC`, `Audit`, `Gap`, or `Improve`.

3. Pre-compute the output path.

```text
$RESEARCH_BASE_PATH/[Company]/[Company] - Business Overview.md
```

4. Run the synthesis pass.
   - Read `references/phase-1-synthesis-prompt.md`, `references/output-template.md`, and `references/validation-checklist.md`.
   - Fill placeholders with company, ticker if known, timestamp, output path, and source paths.
   - Write the overview to the pre-computed output path.

5. Run quality control.
   - Invoke `$quality-control company-overview "COMPANY"` after the output exists.
   - Use `references/phase-2-qc-prompt.md` as the bridge prompt if invoking the helper manually.

6. Run the compliance audit.
   - Invoke `$audit-output company-overview "COMPANY"` after QC.
   - The helper must load this skill's `SKILL.md`, `references/output-template.md`, and `references/validation-checklist.md`.
   - Use `references/phase-3-audit-prompt.md` as the bridge prompt if invoking the helper manually.

7. Report results.
   - Include output path, sources used, QC status, audit status, and remaining flags.

## Guardrails

- This overview is a durable reference document; keep it factual, source-grounded, and updateable.
- Do not overwrite a strong existing overview without preserving useful content and noting what changed.
- Do not invent financial history, segment details, or management claims.
- Do not modify skill definitions or settings files while running this skill.
