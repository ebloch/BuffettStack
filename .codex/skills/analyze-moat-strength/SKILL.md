---
name: analyze-moat-strength
description: Score a company moat strength and trajectory with evidence-backed checklist scoring, devil's-advocate review, and compliance audit. Use when explicitly invoked as $analyze-moat-strength with a company name or ticker.
---

# Analyze Moat Strength

Use this skill to produce a scored assessment of competitive advantage durability, including evidence for each score, trajectory, and a devil's-advocate challenge.

## Inputs

Accept invocation text after `$analyze-moat-strength`:

```text
COMPANY_OR_TICKER
```

If no company or ticker is provided, ask for it. Resolve ambiguous tickers or company folders before writing output.

## Resources

This skill is self-contained. Use these bundled files:

- `references/phase-1a-moat-strength-prompt.md` for core moat scoring.
- `references/phase-1b-trajectory-prompt.md` for trajectory scoring.
- `references/phase-2-devils-advocate-prompt.md` for adversarial review.
- `references/phase-3-audit-prompt.md` for the compliance-audit pass.
- `references/output-template.md` for memo structure.
- `references/validation-checklist.md` for completion checks.

This skill uses its bundled devil's-advocate pass instead of `$quality-control`. Invoke `$audit-output` for the final compliance audit.

## Formal Review Gate

The devil's-advocate and audit passes are mandatory and sequential. A manual review by the synthesis pass is not a substitute for running the dedicated review phases.

When the draft output is first written, add or update these YAML frontmatter fields:

```yaml
formal_devils_advocate_run: false
formal_audit_run: false
devils_advocate_status: pending
audit_status: blocked_until_devils_advocate_complete
devils_advocate_completed_at: null
audit_completed_at: null
devils_advocate_result: null
audit_result: null
```

After the scoring and trajectory passes exist in the output, run the bundled devil's-advocate pass first. That pass must edit the output in place and set `formal_devils_advocate_run: true`, `devils_advocate_status`, `devils_advocate_completed_at`, and `devils_advocate_result`.

Only after the devil's-advocate pass is complete or partial, run `$audit-output analyze-moat-strength "COMPANY"`. The audit helper must edit the output in place and set `formal_audit_run: true`, `audit_status`, `audit_completed_at`, and `audit_result`.

Do not report the workflow as complete unless `formal_devils_advocate_run: true` and `formal_audit_run: true` are present in the final output. If either review pass cannot run, report the workflow as incomplete and state exactly which pass is missing.

## Workflow

1. Resolve the research context.
   - Resolve the research root from `RESEARCH_BASE_PATH`, `.codex/settings.local.json`, or the repo-local `research/` default.
   - Use that research root for prerequisite reads and output writes.
   - Search under the research root for the company folder.
   - Generate a timestamp with `date "+%Y-%m-%d-%H%M"`.

2. Check prerequisites.
   - Require annual-filing synthesis research: `$RESEARCH_BASE_PATH/[Company]/1.1-Annual-Filings/*.md`.
   - Require business economics research: `$RESEARCH_BASE_PATH/[Company]/2.1-Business-Economics/*.md`.
   - Require competitive landscape or scuttlebutt research: `$RESEARCH_BASE_PATH/[Company]/2.3-Competitive-Landscape/*.md` or `$RESEARCH_BASE_PATH/[Company]/2.2-Scuttlebutt/*.md`.
   - Exclude files containing `QC`, `Audit`, `Gap`, or `Improve`.
   - Stop if required research is missing and list the exact prerequisite skills to run first.

3. Pre-compute the output path.

```text
$RESEARCH_BASE_PATH/[Company]/2.6-Moat-Strength/Moat Strength - Analysis - [Company] - [TIMESTAMP].md
```

4. Run the moat scoring pass.
   - Read `references/phase-1a-moat-strength-prompt.md`, `references/output-template.md`, and `references/validation-checklist.md`.
   - Score each required item on the `-2` to `+2` scale.
   - Enforce the `+2` evidence gate from the source prompt.
   - Write the base analysis to the pre-computed output path.

5. Run the trajectory pass.
   - Read `references/phase-1b-trajectory-prompt.md`.
   - Score trajectory independently and insert it into the output's trajectory section.
   - If the trajectory pass fails, continue and flag the omission.

6. Run the devil's-advocate pass.
   - Read `references/phase-2-devils-advocate-prompt.md`.
   - Re-read raw source files, challenge optimistic scoring, and surgically edit unsupported claims or scores.
   - Preserve original scores only when evidence clears the rubric.

7. Run the compliance audit.
   - Invoke `$audit-output analyze-moat-strength "COMPANY"` after the devil's-advocate pass.
   - The helper must load this skill's `SKILL.md`, `references/output-template.md`, and `references/validation-checklist.md`.
   - Use `references/phase-3-audit-prompt.md` as the bridge prompt if invoking the helper manually.

8. Report results.
   - Include output path, source paths, final score, trajectory score, audit status, and remaining flags.

## Guardrails

- Scores must be evidence-backed; do not award `+2` for plausible but unproven advantages.
- Separate present moat strength from future trajectory.
- Treat the devil's-advocate pass as an adversarial evidence check, not a style edit.
- Do not modify skill definitions or settings files while running this skill.
