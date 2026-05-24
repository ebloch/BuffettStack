# Phase 3: Compliance Audit Prompt

Use this reference for the audit pass for analyze-competitive-landscape.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing a compliance audit on a Competitive Landscape Analysis.

**Context:**
- Company: [COMPANY]
- Analysis Path: [MEMO_PATH]

---

## Your Task

Run the audit-output skill to check the analysis against skill requirements and fix compliance violations.

**Step 1: Invoke the audit-output skill**
```
$audit-output analyze-competitive-landscape "[COMPANY]"
```

**Step 2: Monitor the audit process**

The skill will:
1. Load skill requirements:
   - `SKILL.md`
   - `output-template.md`
   - `validation-checklist.md`
2. Check the analysis against each requirement
3. Classify violations as FIXABLE or FLAG-ONLY
4. Apply surgical edits for FIXABLE violations

---

## Audit Focus Areas for Competitive Landscape

### What Can Be Fixed (FIXABLE)

These violations can be fixed autonomously because they don't require source verification:

| Violation | Fix Applied |
|-----------|-------------|
| Missing source hyperlinks section | Add "## Sources" with placeholder `[Source needed](URL)` |
| Missing "[est.]" suffix on unsourced market share | Add "[est.]" marker after percentage |
| Tildes in numerical values | Remove "~", add "[est.]" if unsourced |
| Missing trend impact ratings | Add "[TBD]" placeholder after trend description |
| Missing life cycle duration | Add "[duration needed]" placeholder |
| Missing "Vertical Integration Dynamics" section header | Add section header with placeholder text |
| Missing "Competitive Response Dynamics" section header | Add section header with placeholder text |
| CAGR missing year range | Add "[FY20XX-FY20XX needed]" placeholder |
| Broken table formatting | Fix markdown table alignment |
| Missing skeleton tables for multi-segment | Add Overlap Matrix and Segment Variations table shells |
| Missing Five Forces summary table | Add skeleton table with 5 rows |
| Missing Emerging Threats summary table | Add skeleton table |
| Format violations (section headers, table structure) | Fix structural formatting |

### What Gets Flagged Only (FLAG-ONLY)

These violations are documented but NOT fixed because they require source data or analytical judgment:

| Violation | Why Flagged |
|-----------|-------------|
| Incorrect market share percentages | Needs source data to verify correct value |
| Wrong CAGR calculations | Needs revenue figures to recalculate |
| Market share arithmetic errors | Sum doesn't match claimed aggregate — needs data |
| Missing major competitor | Requires industry knowledge to identify |
| Thin analysis sections | Requires source reading and research to expand |
| Incorrect Porter's Force ratings | Needs analytical judgment and evidence |
| Conflicting CAGRs for same company | Needs source resolution to determine correct value |
| Mixed corporate/systemwide metrics in comparison table | Needs research to standardize basis |
| Wrong industry life cycle assessment | Needs industry knowledge to correct |
| Missing competitor financial depth | Needs financial data research |
| Industry CAGR presented as range without resolution | Needs source investigation to select figure |

---

## Compliance Checks

### Section 1: Industry Overview

- [ ] TAM provided with dollar figure and source — **FIXABLE** if missing: add "[TAM needed]"
- [ ] Historical growth is SINGLE numerical CAGR with source — **FLAG-ONLY** if range or qualitative
- [ ] Projected growth is SINGLE numerical CAGR with source — **FLAG-ONLY** if range or qualitative
- [ ] Industry life cycle stage identified — **FIXABLE** if missing: add "[Phase needed]"
- [ ] Life cycle includes approximate duration in phase — **FIXABLE** if missing: add "[duration needed]"
- [ ] At least 3 key industry trends identified — **FLAG-ONLY** if fewer than 3
- [ ] Each trend has impact rating (HIGH/MEDIUM/LOW) — **FIXABLE** if missing: add "[TBD]"
- [ ] Industry structure describes consolidation level — **FLAG-ONLY** if thin

### Section 2: Value Chain Economics

- [ ] Value chain map table present — **FIXABLE** if missing: add skeleton table
- [ ] Value migration analysis present — **FLAG-ONLY** if missing or thin
- [ ] "Vertical Integration Dynamics" subsection present — **FIXABLE** if missing: add header + placeholder
- [ ] Implications for subject company stated — **FLAG-ONLY** if missing

### Section 2B: Segment Analysis (Conditional)

- [ ] Segment detection decision documented — **FLAG-ONLY** if not addressed
- [ ] If multi-segment: Segment Overview table present — **FIXABLE** if missing: add skeleton
- [ ] If multi-segment: Per-segment analyses present — **FLAG-ONLY** if missing
- [ ] If multi-segment: Competitor Overlap Matrix present — **FIXABLE** if missing: add skeleton
- [ ] If multi-segment: Segment TAMs differ from consolidated — **FLAG-ONLY** if identical
- [ ] If multi-segment: Segment competitors differ — **FLAG-ONLY** if identical

### Section 3: Competitive Landscape

- [ ] Market share table has 10-year view columns — **FIXABLE** if columns missing: add headers
- [ ] Market share percentages have no tildes — **FIXABLE**: remove "~", add "[est.]"
- [ ] Market share arithmetic verified — **FLAG-ONLY** if sum doesn't match
- [ ] At least 3 competitors profiled — **FLAG-ONLY** if fewer
- [ ] Each profile has geographic focus — **FLAG-ONLY** if missing
- [ ] Each profile has customer segment focus — **FLAG-ONLY** if missing
- [ ] Each profile has 5-year revenue CAGR — **FLAG-ONLY** if missing or tilde
- [ ] Each profile has management quality assessment — **FLAG-ONLY** if missing
- [ ] Competitive comparison table present — **FIXABLE** if missing: add skeleton
- [ ] Comparison table has no tildes — **FIXABLE**: remove "~", add "[est.]"
- [ ] Revenue Growth includes year range — **FIXABLE** if missing: add "[FY20XX-FY20XX needed]"
- [ ] Corporate/systemwide metrics consistent — **FLAG-ONLY** if mixed
- [ ] "Competitive Response Dynamics" subsection present — **FIXABLE** if missing: add header + placeholder

### Section 4: Porter's Five Forces

- [ ] All 5 forces analyzed — **FLAG-ONLY** if any missing
- [ ] Each force has explicit rating (Low/Moderate/High) — **FIXABLE** if missing: add "[Rating needed]"
- [ ] Five Forces summary table present — **FIXABLE** if missing: add skeleton table
- [ ] Overall industry attractiveness rating — **FIXABLE** if missing: add "[Rating needed]"
- [ ] If multi-segment: Segment Variations table present — **FIXABLE** if missing: add skeleton

### Section 5: Adjacent & Emerging Threats

- [ ] Tech giant risk assessed — **FLAG-ONLY** if missing entirely
- [ ] Private/VC threats assessed — **FLAG-ONLY** if missing entirely
- [ ] International threats assessed — **FLAG-ONLY** if missing entirely
- [ ] Converging industries assessed — **FLAG-ONLY** if missing entirely
- [ ] Emerging threats summary table present — **FIXABLE** if missing: add skeleton table

### Output Quality

- [ ] Executive summary present — **FIXABLE** if missing: add header + placeholder
- [ ] Executive summary has industry attractiveness rating — **FIXABLE** if missing: add "[Rating needed]"
- [ ] Executive summary avoids tildes and "approximately" — **FIXABLE**: remove "~"
- [ ] Watch list present — **FLAG-ONLY** if missing
- [ ] Sources section with at least 5 hyperlinks — **FIXABLE** if missing: add "## Sources" + placeholders
- [ ] All financial figures have year/source attribution — **FLAG-ONLY** if missing

---

## FIXABLE vs FLAG-ONLY Decision Matrix

| Check | If Missing/Wrong | Classification | Fix Action |
|-------|------------------|----------------|------------|
| Source hyperlinks section | Missing | FIXABLE | Add "## Sources" with placeholders |
| "[est.]" suffix | Missing on unsourced share | FIXABLE | Add "[est.]" after percentage |
| Tilde in value | "~70%" present | FIXABLE | Remove "~", add "[est.]" |
| Trend impact rating | Missing HIGH/MED/LOW | FIXABLE | Add "[TBD]" |
| Life cycle duration | "Mature" without years | FIXABLE | Add "[duration needed]" |
| Vertical Integration header | Section missing | FIXABLE | Add header + placeholder |
| Competitive Response header | Section missing | FIXABLE | Add header + placeholder |
| CAGR year range | Missing "(FY20XX-FY20XX)" | FIXABLE | Add "[FY20XX-FY20XX needed]" |
| Table formatting | Broken markdown | FIXABLE | Fix alignment |
| Multi-segment skeleton tables | Missing Overlap Matrix | FIXABLE | Add skeleton table |
| Five Forces summary table | Missing | FIXABLE | Add skeleton with 5 rows |
| Emerging threats table | Missing | FIXABLE | Add skeleton table |
| Market share percentage wrong | Incorrect value | FLAG-ONLY | Note for review |
| CAGR calculation wrong | Incorrect math | FLAG-ONLY | Note for review |
| Market share arithmetic | Sum ≠ aggregate | FLAG-ONLY | Note for review |
| Missing major competitor | Not profiled | FLAG-ONLY | Note for review |
| Thin analysis section | Insufficient depth | FLAG-ONLY | Note for review |
| Porter's Force rating wrong | Incorrect rating | FLAG-ONLY | Note for review |
| Conflicting CAGRs | Same company, different values | FLAG-ONLY | Note for review |
| Mixed metrics basis | Corporate vs systemwide | FLAG-ONLY | Note for review |

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
- The analysis should pass all format/structure checks after this phase
- Make scoped file edits — don't rewrite the entire analysis
```
