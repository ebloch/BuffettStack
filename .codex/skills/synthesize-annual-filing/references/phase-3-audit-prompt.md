# Phase 3: Compliance Audit Prompt

Use this prompt to invoke `$audit-output` from `$synthesize-annual-filing`.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing a compliance audit on an annual filing synthesis memo.

**Context:**
- Company: [COMPANY] ([TICKER])
- Fiscal Year: [YEAR]
- Memo Path: [MEMO_PATH]
- Industry: [INDUSTRY]
- Parsing Mode: [PARSING_MODE] (sec = EDGAR, pdf = PDF file)
- PDF Source: [PDF_SOURCE] (only when PARSING_MODE=pdf)

## Your Task

Invoke `$audit-output` to check the memo against skill requirements and fix compliance violations.

**Process**
1. Call `$audit-output synthesize-annual-filing "[COMPANY]" FY[YEAR]`.
2. The helper will load skill requirements (`SKILL.md`, `references/output-template.md`, `references/validation-checklist.md`, and the relevant industry checklist).
3. Check the memo against each requirement.
4. Classify violations as FIXABLE or FLAG-ONLY.
5. Apply surgical edits for FIXABLE violations.

## Audit Focus Areas

### What Can Be Fixed (FIXABLE)
- Missing "Not disclosed in 10-K" statements → Add statement
- Missing YAML fields → Add field with `null` + explanation
- Format violations → Fix table structure, section headers
- Missing required sections → Add skeleton/placeholder
- Tag/cross-reference inconsistencies → Add missing tags
- Missing page references → Add "p.XX - verify" placeholder

### What Gets Flagged Only (FLAG-ONLY)
- Incorrect data/calculations → Needs source verification
- Missing content requiring extraction → Content must come from filing
- Claims needing source validation → Must verify against original
- Incomplete analysis → Requires source reading to expand

## Compliance Checks

Key compliance items for synthesize-annual-filing:

### YAML Frontmatter
- [ ] All required metadata fields present
- [ ] Key metrics populated (or `null` with explanation)
- [ ] Industry-specific metrics per checklist
- [ ] Segments with revenue and % total
- [ ] Capital allocation fields
- [ ] Share count fields
- [ ] Quality flags set

### Body Sections
- [ ] Key Takeaways: 5-7 bullets with bold lead-ins
- [ ] Business Summary: Segment table present
- [ ] Management Commentary: Direct quote with page reference
- [ ] Guidance & Promises: At least 2 trackable promises
- [ ] Financial Snapshot: P&L and Balance Sheet tables
- [ ] Risk Factors: 3-5 bullets with probability/impact ratings
- [ ] Accounting Quality: 7-item checklist table
- [ ] Questions for Further Research: 3-5 with "why it matters"
- [ ] Topic Index: All tags listed with section locations
- [ ] Source: Filing metadata and page references

### Calculated Metrics
- [ ] ROIC: Explicit calculation shown in footnote
- [ ] Net Debt / EBITDA: Calculation shown in notes
- [ ] Interest Coverage: Explicit formula (not approximations like ">10x")

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

## Important Notes

- This audit does NOT read source documents — it only checks compliance
- FLAG-ONLY issues should be passed to user for manual review
- All FIXABLE violations should be addressed before completing
- The memo should pass all compliance checks after this phase
```
