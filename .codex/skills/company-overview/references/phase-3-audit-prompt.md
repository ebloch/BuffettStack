# Phase 3: Compliance Audit Prompt

Use this reference for the audit pass for company-overview.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing a compliance audit on a Business Overview memo.

**Context:**
- Company: [COMPANY]
- Memo Path: [MEMO_PATH]

## Your Task

Run the audit-output skill to check the memo against skill requirements and fix compliance violations.

**Step 1: Invoke the audit-output skill**
```
$audit-output company-overview "[COMPANY]"
```

**Step 2: Monitor the audit process**
The skill will:
1. Load skill requirements (SKILL.md, output-template.md, validation-checklist.md)
2. Check the memo against each requirement
3. Classify violations as FIXABLE or FLAG-ONLY
4. Apply surgical edits for FIXABLE violations

## Audit Focus Areas

### What Can Be Fixed (FIXABLE)
- Missing "Not disclosed" or "Unable to assess" statements → Add statement
- Missing YAML fields → Add field with `null` + explanation
- Format violations → Fix table structure, section headers
- Missing required sections → Add skeleton/placeholder
- Incorrect trajectory labels → Fix based on data
- Missing trend arrows in Risk Evolution Matrix → Add ↑/→/↓

### What Gets Flagged Only (FLAG-ONLY)
- Incorrect CAGR calculations → Needs manual verification
- Missing content requiring source extraction → Content must come from Foundation memos
- Claims needing source validation → Must verify against original
- Incomplete analysis → Requires source reading to expand

## Compliance Checks

Key compliance items for company-overview:

### YAML Frontmatter
- [ ] `type: company-overview` present
- [ ] `company` field populated
- [ ] `ticker` field populated
- [ ] `period_start` and `period_end` fields present
- [ ] `years_analyzed` field present
- [ ] `source_count` section with annual_filings, investor_presentations, financial_statements

### Body Sections
- [ ] Key Takeaways: 5-8 bullets with bold lead-ins
- [ ] The Business: 2-3 paragraphs + segment table
- [ ] Financial Evolution: Table with start/end values, CAGR, trajectory
- [ ] Segment Mix Shift: Table with start/end percentages, Δ, significance
- [ ] Management Credibility Scorecard: Promise table with scores + rating
- [ ] Risk Evolution Matrix: 4+ risk categories with trend arrows
- [ ] Key Events Timeline: Minimum 3 events with impact
- [ ] Questions for Monitoring: 3-5 with "why it matters"
- [ ] Year Card Summary: One card per fiscal year
- [ ] Source Files: All sources listed, organized by type

### Content Quality
- [ ] Key Takeaways are cross-year synthesis (not point-in-time facts)
- [ ] Business description explains economic engine
- [ ] CAGR calculations use correct formula
- [ ] Risk matrix shows evolution (not just current state)
- [ ] Questions are specific to this company

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
