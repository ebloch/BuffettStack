---
name: run-munger-analysis
description: Evaluate a company through Charlie Munger's mental models checklist, covering business quality, management, competitive position, risk, and long-term compounding potential. Use when explicitly invoked as $run-munger-analysis with a company name or ticker.
---

# Run Munger Analysis

Use this skill to synthesize prior research into a staged Charlie Munger-style assessment of business quality, management, moat durability, risks, and long-term compounding potential.

## Inputs

Accept invocation text after `$run-munger-analysis`:

```text
COMPANY_OR_TICKER
```

If no company or ticker is provided, ask for it. Resolve ambiguous tickers or company folders before writing output.

## Resources

This skill is self-contained. Use these bundled files:

- `references/phase-1-synthesis-prompt.md` for the overall synthesis workflow.
- `references/stage-1-business-foundation.md` for business foundation analysis.
- `references/stage-2-management.md` for management analysis.
- `references/stage-3-competitive-position.md` for moat and competitive position analysis.
- `references/stage-4-final-synthesis.md` for final scoring and verdict synthesis.
- `references/working-analysis-template.md` for staged working notes.
- `references/phase-2-qc-prompt.md` for the quality-control pass.
- `references/phase-3-audit-prompt.md` for the compliance-audit pass.
- `references/output-template.md` for final memo structure.
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

After the draft exists, run `$quality-control run-munger-analysis "COMPANY"` first. The QC helper must edit the output in place and set `formal_qc_run: true`, `qc_status`, `qc_completed_at`, and `qc_result`.

Only after formal QC is complete or partial, run `$audit-output run-munger-analysis "COMPANY"`. The audit helper must edit the output in place and set `formal_audit_run: true`, `audit_status`, `audit_completed_at`, and `audit_result`.

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
   - Require at least one moat source from `2.2-Scuttlebutt/`, `2.3-Competitive-Landscape/`, or `2.6-Moat-Strength/`.
   - Require risk assessment: `$RESEARCH_BASE_PATH/[Company]/2.5-Risk-Assessment/*.md`.
   - Exclude files containing `QC`, `Audit`, `Gap`, or `Improve`.
   - Stop if required research is missing and list only the missing prerequisite skills.

3. Pre-compute the output path.

```text
$RESEARCH_BASE_PATH/[Company]/3.2-Munger-Analysis/Munger Analysis - Memo - [Company] - [TIMESTAMP].md
```

4. Run the staged synthesis.
   - Read `references/phase-1-synthesis-prompt.md`, stage prompts 1 through 4, `references/working-analysis-template.md`, `references/output-template.md`, and `references/validation-checklist.md`.
   - Fill placeholders with company, ticker if known, output path, and prerequisite source paths.
   - Work through business foundation, management, competitive position, and final synthesis in sequence.
   - Enforce the scoring rubric and `Why Not Higher?` discipline before writing the final memo.

5. Run quality control.
   - Invoke `$quality-control run-munger-analysis "COMPANY"` after the output exists.
   - Use `references/phase-2-qc-prompt.md` as the bridge prompt if invoking the helper manually.

6. Run the compliance audit.
   - Invoke `$audit-output run-munger-analysis "COMPANY"` after QC.
   - The helper must load this skill's `SKILL.md`, `references/output-template.md`, and `references/validation-checklist.md`.
   - Use `references/phase-3-audit-prompt.md` as the bridge prompt if invoking the helper manually.

7. Report results.
   - Include output path, total score, verdict, QC status, audit status, and remaining flags.

## Guardrails

- Do not let narrative admiration outrun evidence; every score needs limitations and evidence.
- Complexity, incentives, and downside avoidance are first-class parts of the verdict.
- Keep the circle of competence assessment separate from the numeric score.
- Do not modify skill definitions or settings files while running this skill.
