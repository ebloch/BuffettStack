---
name: audit-output
description: Check an investment research output against its skill requirements and surgically fix compliance violations. Use when explicitly invoked as $audit-output after a research skill produces a memo, especially after $quality-control.
---

# Audit Output

Use this skill to audit a research output against its governing skill requirements, templates, validation checklist, and industry checklist. Unlike `$quality-control`, this skill does not re-read source documents; it only checks requirement compliance.

## Inputs

Accept invocation text after `$audit-output`:

```text
skill-name company [FYyear]
```

Examples:

- `synthesize-annual-filing MELI FY2024`
- `analyze-moat-strength Costco`
- `scuttlebutt "CME Group"`

## Resources

- `references/compliance-check-prompt.md` defines the requirement audit rubric.

For migrated skills, load requirements from `.codex/skills/[skill-name]/`. For skills not yet migrated, use `.claude/skills/[skill-name]/` as read-only source material. Never modify `.claude/**`.

## Workflow

1. Parse inputs.
   - Extract target skill, company, and optional fiscal year.
   - Read `RESEARCH_BASE_PATH` from `.claude/settings.local.json` at `env.RESEARCH_BASE_PATH`.

2. Locate the output document.
   - Search under `$RESEARCH_BASE_PATH/[Company]/`.
   - If an FY token is provided, prefer files containing that fiscal year.
   - For `synthesize-annual-filing`, search `1.1-Annual-Filings/` for `*Synthesis - Memo*.md`.
   - Stop and report clearly if no unique output can be found.
   - After locating the output, read its YAML frontmatter to recover canonical metadata such as `company`, `ticker`, `fiscal_year`, `industry`, `form_type`, and `accounting_standard`.

3. Load requirements.
   - Prefer `.codex/skills/[skill-name]/SKILL.md`.
   - Read target references when present:
     - `references/output-template.md`
     - `references/validation-checklist.md`
     - `references/industry-checklists/[industry].md`
   - Determine `industry` from output YAML frontmatter when possible.
   - If the Codex skill does not exist yet, read corresponding `.claude/skills/[skill-name]` files as read-only migration source.

4. Check compliance.
   - Use `references/compliance-check-prompt.md`.
   - Classify each requirement as COMPLIANT, FIXABLE, or FLAG-ONLY.
   - FIXABLE means no source document is needed.
   - FLAG-ONLY means source verification or substantive analysis is required.

5. Apply fixable edits.
   - Add missing required sections or placeholders.
   - Add missing YAML fields with `null` and an explanation when source data is unavailable.
   - Fix malformed tables, section headers, tags, cross-references, and obvious format issues.
   - Preserve the author's analysis and avoid cosmetic rewrites.

6. Report status.
   - Include output path, requirements checked, fixes applied, and flag-only issues.
   - Recommend `$quality-control` for unresolved source-dependent issues.

## Guardrails

- Do not read source filings or external documents during audit.
- Do not invent values or calculations.
- Do not fix source-dependent violations with placeholders unless the requirement is purely structural.
- Do not modify `.claude/**`, `CLAUDE.md`, or existing Claude skill files.
