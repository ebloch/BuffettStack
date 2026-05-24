# Phase 3: Compliance Audit Prompt

Use this reference for the audit pass for synthesize-investor-materials.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing a compliance audit on an investor materials synthesis memo.

**Context:**
- Company: [COMPANY]
- Event Name: [EVENT_NAME]
- Memo Path: [MEMO_PATH]
- Event Type: [EVENT_TYPE]

---

## Your Task

Run the audit-output skill to check the memo against skill requirements and fix compliance violations.

**Step 1: Invoke the audit-output skill**
```
$audit-output synthesize-investor-materials "[COMPANY]" "[EVENT_NAME]"
```

**Step 2: Monitor the audit process**

The skill will:
1. Load skill requirements:
   - `SKILL.md`
   - `output-template.md`
   - `validation-checklist.md`
   - `event-type-checklists/[EVENT_TYPE].md`
2. Check the memo against each requirement
3. Classify violations as FIXABLE or FLAG-ONLY
4. Apply surgical edits for FIXABLE violations

---

## Audit Focus Areas

### What Can Be Fixed (FIXABLE)

- Missing YAML fields → Add field with `null` + explanation
- Format violations → Fix table structure, section headers
- Missing required sections → Add skeleton/placeholder
- Missing slide references → Add "(Slide XX - verify)" placeholder
- Number format violations → Convert to correct format (M suffix, etc.)
- Missing "minimum 3 promises" statement → Add explanation if <3

### What Gets Flagged Only (FLAG-ONLY)

- Incorrect data/calculations → Needs source verification
- Missing content requiring extraction → Content must come from PDFs
- Claims needing source validation → Must verify against original
- Incomplete analysis → Requires source reading to expand
- Non-verbatim "quotes" → Must verify against source

---

## Compliance Checks

Key compliance items for synthesize-investor-materials:

### YAML Frontmatter

- [ ] All required metadata fields present (company, ticker, event_type, event_date, event_name, synthesis_date)
- [ ] Files analyzed count matches Source Materials table
- [ ] Key metrics populated (if presented) or `null`
- [ ] Capital allocation populated (if discussed) or `null`
- [ ] Quality ratings set: new_information, specificity, event_significance

### Body Sections

- [ ] Key Takeaways: 5-7 bullets with **bold lead-ins**
- [ ] Source Materials: Table listing all files with type, slides, focus
- [ ] Strategic Messaging: Core thesis prose + New vs. Known table + Priorities table
- [ ] Guidance & Targets: Table with Metric, Target, Timeline, Specificity, Source
- [ ] Promises to Track: Minimum 3 entries (or explanation if fewer)
- [ ] Claims to Verify: Table with verifiability ratings
- [ ] Business Updates by Segment: Prose bullets per segment (or omitted if no segment detail)
- [ ] Red Flags & Concerns: 2-4 prose bullets + Unanswered Questions (3-5)
- [ ] Investment Implications: Current Holders + Prospective Investors paragraphs
- [ ] Source: Event metadata with file list

### Source References

- [ ] All verbatim quotes include slide references `(Slide XX)`
- [ ] All guidance/targets include source references
- [ ] All promises include slide references
- [ ] All competitive claims include slide references

### Number Formats

- [ ] Tables use M suffix, no $ (e.g., `4272M`)
- [ ] Prose uses full currency (e.g., `$4.3 billion`)
- [ ] Percentages use one decimal (e.g., `21.4%`)
- [ ] Growth targets use sign prefix (e.g., `+15%`)

### Event-Type Specific

Based on `[EVENT_TYPE]`, verify checklist items from:
```
.codex/skills/synthesize-investor-materials/references/event-type-checklists/[EVENT_TYPE].md
```

---

## Return Value

When complete, return a JSON object:
```json
{
  "violations_found": [number],
  "fixes_applied": [number],
  "flagged_for_review": [number],
  "status": "success" | "partial" | "failed",
  "flagged_issues": ["list of FLAG-ONLY issues"]
}
```

---

## Important Notes

- This audit does NOT read source documents — it only checks compliance
- FLAG-ONLY issues should be passed to user for manual review
- All FIXABLE violations should be addressed before completing
- The memo should pass all compliance checks after this phase
- Make scoped file edits — don't rewrite the entire memo
```
