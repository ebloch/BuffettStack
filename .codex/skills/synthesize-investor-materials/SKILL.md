---
name: synthesize-investor-materials
description: Synthesize investor presentations, investor day decks, capital markets day materials, quarterly decks, and shareholder letters into investment research memos. Use when explicitly invoked as $synthesize-investor-materials with a company plus event, count, file, or URL.
---

# Synthesize Investor Materials

Use this skill to turn investor-facing materials into a source-grounded memo that captures management's strategy, claims, targets, capital allocation messaging, and open questions.

## Inputs

Accept invocation text after `$synthesize-investor-materials` in these forms:

```text
COMPANY_OR_TICKER
COMPANY_OR_TICKER last N
COMPANY_OR_TICKER EVENT_NAME_OR_PERIOD
--file /path/to/presentation.pdf
--url https://example.com/deck.pdf
```

Examples:

- `CME`
- `CME last 3`
- `CME Investor Day 2025`
- `CME Q4 2025`
- `--file /tmp/deck.pdf`
- `--url https://example.com/deck.pdf`

If the company, event, file, or URL target is ambiguous, ask for clarification before writing output.

## Resources

This skill is self-contained. Use these bundled files:

- `references/phase-1-synthesis-prompt.md` for the synthesis pass.
- `references/source-extraction-prompt.md` for source collection and material synthesis details.
- `references/phase-2-qc-prompt.md` for the quality-control pass.
- `references/phase-3-audit-prompt.md` for the compliance-audit pass.
- `references/output-template.md` for memo structure.
- `references/validation-checklist.md` for completion checks.
- `references/event-type-checklists/` for event-specific requirements.

Run synthesis locally, then invoke `$quality-control` and `$audit-output` as explicit helper skills for the review passes.

## Formal Review Gate

The review passes are mandatory and sequential. A manual review by the synthesis pass is not a substitute for running the helper skills.

When the draft memo is first written, add or update these YAML frontmatter fields:

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

After the draft exists, run `$quality-control synthesize-investor-materials "COMPANY"` first. The QC helper must edit the memo in place and set `formal_qc_run: true`, `qc_status`, `qc_completed_at`, and `qc_result`.

Only after formal QC is complete or partial, run `$audit-output synthesize-investor-materials "COMPANY"`. The audit helper must edit the memo in place and set `formal_audit_run: true`, `audit_status`, `audit_completed_at`, and `audit_result`.

Do not report the workflow as complete unless `formal_qc_run: true` and `formal_audit_run: true` are present in the final memo. If either helper pass cannot run, report the workflow as incomplete and state exactly which pass is missing.

## Workflow

1. Parse the invocation.
   - Extract company or ticker when present.
   - Determine mode: most recent, last N, specific event, direct file, or direct URL.
   - Resolve event name, count, local files, or URLs before writing output.

2. Resolve the research context.
   - Resolve the research root from `RESEARCH_BASE_PATH`, `.codex/settings.local.json`, or the repo-local `research/` default.
   - Use that research root for output writes.
   - Search under the research root for the company folder when a company is provided.
   - Generate a timestamp with `date "+%Y-%m-%d-%H%M"`.

3. Pre-compute the output directory.

```text
$RESEARCH_BASE_PATH/[Company]/1.2-Investor-Presentations/
```

The final filename should be:

```text
[Event Name] - Memo - [Company] - [TIMESTAMP].md
```

4. Find and read investor materials.
   - For direct file or URL input, use exactly those sources.
   - For company/event input, search the company IR site and public web for the requested material.
   - Download PDFs to a temporary path only as needed for parsing.
   - Identify event type: `investor-day`, `capital-markets-day`, `quarterly-presentation`, `shareholder-letter`, or `standing-overview`.

5. Run the synthesis pass.
   - Read `references/phase-1-synthesis-prompt.md`, `references/source-extraction-prompt.md`, `references/output-template.md`, `references/validation-checklist.md`, and the relevant event-type checklist.
   - Fill placeholders with company, ticker if known, mode, event specifier, source file paths or URLs, timestamp, event type, and output path.
   - Write the memo to the final output path.

6. Run quality control.
   - Invoke `$quality-control synthesize-investor-materials "COMPANY"` after the output exists.
   - The helper must re-read the source materials when available.
   - Use `references/phase-2-qc-prompt.md` as the bridge prompt if invoking the helper manually.

7. Run the compliance audit.
   - Invoke `$audit-output synthesize-investor-materials "COMPANY"` after QC.
   - The helper must load this skill's `SKILL.md`, `references/output-template.md`, `references/validation-checklist.md`, and the relevant event-type checklist.
   - Use `references/phase-3-audit-prompt.md` as the bridge prompt if invoking the helper manually.

8. Report results.
   - Include output path, event type, source file or URL list, QC status, audit status, and remaining flags.

## Guardrails

- Do not use direct vendor APIs unless a repo helper script explicitly supports the source.
- Preserve management claims, targets, and definitions accurately; avoid paraphrasing away important qualifiers.
- Distinguish management aspiration from delivered performance.
- Do not modify skill definitions or settings files while running this skill.
