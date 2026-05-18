---
name: quality-control
description: Re-read source documents to identify content gaps and surgically edit investment research outputs. Use when explicitly invoked as $quality-control after a research skill has produced an output document, especially from $synthesize-annual-filing.
---

# Quality Control

Use this skill to improve an existing research output by re-reading its source documents and filling material gaps without regenerating the whole memo.

## Inputs

Accept invocation text after `$quality-control`:

```text
skill-name company [FYyear]
```

Examples:

- `synthesize-annual-filing "CME Group" FY2024`
- `analyze-moat-strength Costco`
- `scuttlebutt Salesforce`

The optional fiscal-year token targets year-specific outputs such as annual filing memos.

## Resources

- `references/source-review-prompt.md` guides source re-reading and gap classification.
- `references/enhancement-prompt.md` guides surgical edits for each approved gap.

Load requirements from `.codex/skills/[skill-name]/`. If the target skill is not present, stop and report that it has not been migrated.

## Workflow

1. Parse inputs.
   - Extract target skill, company, and optional fiscal year.
   - Resolve the research root from `RESEARCH_BASE_PATH`, `.codex/settings.local.json`, or the repo-local `research/` default.

2. Locate the output document.
   - Search under `$RESEARCH_ROOT/[Company]/`.
   - If an FY token is provided, prefer files containing that fiscal year.
   - For `synthesize-annual-filing`, search `1.1-Annual-Filings/` for `*Synthesis - Memo*.md`.
   - Otherwise use the target skill's output pattern from its `SKILL.md` or templates.
   - Stop and report clearly if no unique output can be found.
   - After locating the output, read its YAML frontmatter and source section to recover canonical metadata such as `company`, `ticker`, `fiscal_year`, `industry`, `form_type`, `accounting_standard`, parser mode, and PDF source URL/path.

3. Load target skill requirements.
   - Prefer `.codex/skills/[skill-name]/SKILL.md`.
   - Also read available target references such as `references/output-template.md`, `references/validation-checklist.md`, and `references/industry-checklists/[industry].md`.
   - If the target skill does not exist yet, stop and report that it has not been migrated.

4. Locate and re-read sources.
   - For `$synthesize-annual-filing`, re-parse the filing with the target skill's bundled parser:
     - Work from `.codex/skills/synthesize-annual-filing`.
     - Use the `ticker` and `fiscal_year` from the memo frontmatter, not just the user-provided company text.
     - SEC filing: `python3 scripts/parse_annual_filing.py TICKER --year YEAR`.
     - PDF filing: `python3 scripts/parse_pdf_filing.py PDF_SOURCE --json`.
     - If parser mode or PDF source is missing from the memo, infer it from the source metadata section; if still unclear, ask the user rather than guessing.
   - For research-synthesis skills, read prerequisite research memos under the relevant company folders.
   - For web/API source skills, re-fetch only when needed and when access is available.

5. Identify gaps.
   - Use `references/source-review-prompt.md`.
   - Classify gaps as CRITICAL, HIGH, or MINOR.
   - Preserve coverage wins and flag unsupported claims.

6. Apply surgical edits.
   - Address CRITICAL and HIGH gaps first.
   - Use `references/enhancement-prompt.md` as the edit rubric.
   - Apply narrow edits to the output document only.
   - Re-read the edited section after each edit.
   - Iterate up to 3 total review loops.

7. Report status.
   - Include output path, sources reviewed, gaps found, gaps fixed, and remaining issues.

## Guardrails

- Source documents are the authority. Do not fill gaps from memory.
- This skill edits research outputs, not skill definitions.
- Do not reformat compliant sections for style alone.
- If a fix requires source verification you cannot perform, leave it unresolved and report it.
- Do not modify skill definitions or settings files.
