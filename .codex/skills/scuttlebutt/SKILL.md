---
name: scuttlebutt
description: Gather Philip Fisher-style grassroots intelligence for a company from customers, employees, partners, competitors, experts, and media. Use when explicitly invoked as $scuttlebutt with a company name or ticker.
---

# Scuttlebutt

Use this skill to produce a source-grounded scuttlebutt analysis and concise memo that test management's narrative against what stakeholders actually say.

## Inputs

Accept invocation text after `$scuttlebutt`:

```text
COMPANY_OR_TICKER
```

Examples:

- `CME`
- `CME Group`
- `Costco`

If no company or ticker is provided, ask for it. If the company name and ticker are ambiguous, resolve them before writing output.

## Resources

This skill is self-contained. Use these bundled files:

- `references/phase-1-synthesis-prompt.md` for the research and synthesis pass.
- `references/phase-2-qc-prompt.md` for the quality-control pass.
- `references/phase-3-audit-prompt.md` for the compliance-audit pass.
- `references/output-template-analysis.md` for the detailed analysis structure.
- `references/output-template-memo.md` for the concise memo structure.
- `references/validation-checklist.md` for completion checks.

Run the synthesis locally, then invoke `$quality-control` and `$audit-output` as explicit helper skills for the review passes.
If the runtime does not automatically load those helper skills, read `.codex/skills/quality-control/SKILL.md` and `.codex/skills/audit-output/SKILL.md` directly and follow them.

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

After the draft outputs exist, run `$quality-control scuttlebutt "COMPANY"` first. The QC helper must edit the outputs in place and set `formal_qc_run: true`, `qc_status`, `qc_completed_at`, and `qc_result`.

Only after formal QC is complete or partial, run `$audit-output scuttlebutt "COMPANY"`. The audit helper must edit the outputs in place and set `formal_audit_run: true`, `audit_status`, `audit_completed_at`, and `audit_result`.

Do not report the workflow as complete unless `formal_qc_run: true` and `formal_audit_run: true` are present in the final outputs. If either helper pass cannot run, report the workflow as incomplete and state exactly which pass is missing.

## Workflow

1. Resolve the research context.
   - Resolve the research root from `RESEARCH_BASE_PATH`, `.codex/settings.local.json`, or the repo-local `research/` default.
   - Use that research root for prerequisite reads and output writes.
   - Search under the research root for the company folder before creating new paths.
   - Generate a timestamp with `date "+%Y-%m-%d-%H%M"`.

2. Check prerequisites.
   - Find annual-filing synthesis memos:

```text
$RESEARCH_BASE_PATH/[Company]/1.1-Annual-Filings/*.md
```

   - Exclude filenames containing `QC`, `Audit`, `Gap`, or `Improve`.
   - Stop if no annual-filing synthesis memo exists and tell the user to run `$synthesize-annual-filing` first.
   - Use every available annual-filing memo for business model, customer segment, risk, and claimed-moat context.

3. Pre-compute output paths.

```text
$RESEARCH_BASE_PATH/[Company]/2.2-Scuttlebutt/Scuttlebutt - Analysis - [Company] - [TIMESTAMP].md
$RESEARCH_BASE_PATH/[Company]/2.2-Scuttlebutt/Scuttlebutt - Memo - [Company] - [TIMESTAMP].md
```

4. Run the synthesis pass.
   - Read `references/phase-1-synthesis-prompt.md`, both output templates, and `references/validation-checklist.md`.
   - Fill placeholders with company, ticker, timestamp, output paths, and annual-filing memo paths.
   - Search current public web sources for all 6 stakeholder categories:
     - Customer Voice
     - Employee Voice
     - Partner/Supplier Voice
     - Competitor Voice
     - Industry Expert Voice
     - Social/Media Sentiment
   - Write both outputs to the pre-computed paths.

5. Run quality control.
   - Invoke `$quality-control scuttlebutt "COMPANY"` after both outputs exist.
   - The helper must re-search public web sources, compare findings to both outputs, and surgically edit content gaps.
   - Use `references/phase-2-qc-prompt.md` as the bridge prompt if invoking the helper from this workflow.

6. Run the compliance audit.
   - Invoke `$audit-output scuttlebutt "COMPANY"` after QC.
   - The helper must load this skill's `SKILL.md`, both output templates, and `references/validation-checklist.md`.
   - Use `references/phase-3-audit-prompt.md` as the bridge prompt if invoking the helper from this workflow.
   - Report any flag-only issues clearly in the final summary.

7. Report results.
   - Include analysis and memo paths.
   - Summarize synthesis, QC, and audit status.
   - List flagged issues needing manual review.

## Scoring

Score each stakeholder category from 1 to 5 and calculate the Scuttlebutt Health Score:

| Stakeholder | Weight |
| --- | ---: |
| Customers | 30% |
| Employees | 25% |
| Partners/Suppliers | 15% |
| Competitors | 10% |
| Industry Experts | 10% |
| Social/Media | 10% |

The weighted score must match across the analysis executive summary, analysis scorecard, and memo header.

## Guardrails

- Use current web research for scuttlebutt evidence; do not rely on memory for stakeholder sentiment.
- Prefer source diversity over one-platform conclusions.
- Note sample sizes, dates, and source limitations whenever available.
- For B2B infrastructure companies, mark inapplicable consumer-review platforms as `N/A - B2B model` and substitute industry-specific sources.
- Never fabricate review scores, CEO approval, quotes, short interest, or social sentiment. If unavailable, write `Data not available`.
- Do not present role-filtered CEO approval as company-wide approval.
- Do not modify skill definitions or settings files while running this skill.
- If a phase fails after outputs exist, continue to later review phases when possible and report partial completion.
