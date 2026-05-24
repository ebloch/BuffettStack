# Phase 3: Compliance Audit Prompt

Use this reference for the audit pass for scenario-analysis.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing a compliance audit on a 10-Year Scenario Analysis.

**Context:**
- Company: [COMPANY]
- Analysis Path: [MEMO_PATH]

---

## Your Task

Run the audit-output skill to check the analysis against skill requirements and fix compliance violations.

**Step 1: Invoke the audit-output skill**
```
$audit-output scenario-analysis "[COMPANY]"
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

## Audit Focus Areas for Scenario Analysis

### What Can Be Fixed (FIXABLE)

These violations can be fixed autonomously because they don't require analytical judgment:

| Violation | Fix Applied |
|-----------|-------------|
| Missing Scenario Overview table | Add skeleton table with 5 rows + Total |
| Missing Probability Rationale section | Add "### Probability Rationale" header + placeholder bullets |
| Missing Key Drivers subsections | Add "### Uncertainties", "### Tailwinds", "### Headwinds" headers |
| Missing Scenario Monitoring section | Add skeleton table + "### Probability Update Triggers" header |
| Missing Sources section | Add "## Sources" header + placeholder list |
| Missing Total row in overview table | Add "\| **Total** \| **100%** \| \|" row |
| Missing scenario component headers | Add "### Key Assumptions", "### Moat Status", "### Trigger Signals" headers |
| Table formatting issues | Fix markdown table alignment |
| Missing Executive Summary section | Add "## Executive Summary" header + placeholder |
| Missing Quarterly Review Checklist table | Add skeleton monitoring table |

### What Gets Flagged Only (FLAG-ONLY)

These violations are documented but NOT fixed because they require analytical judgment:

| Violation | Why Flagged |
|-----------|-------------|
| Probabilities don't sum to 100% | Changing probabilities requires analytical judgment about evidence |
| Probability outside 5-50% range | Redistribution requires research-based reasoning |
| Fewer or more than 5 scenarios | Adding/removing scenarios requires full analytical work |
| Narrative too short (<2 paragraphs) or generic | Expanding narratives requires source document synthesis |
| Assumptions vague or unverifiable | Making assumptions specific requires research context |
| Moat Status uses invalid value | Selecting correct value requires moat analysis context |
| Financial projections in narratives | Removing projections while preserving meaning requires judgment |
| Trigger signals vague or not observable within 1-2 years | Making signals specific requires research context |
| Scenarios not grounded in research | Grounding scenarios requires re-reading source documents |
| Missing scenario entirely | Writing a new scenario requires full analytical work |
| Probability rationale lacks evidence | Adding evidence requires source document knowledge |

---

## Compliance Checks

### Section A: Critical Validation

- [ ] Exactly 5 scenarios present — **FLAG-ONLY** if wrong count
- [ ] Probabilities sum to exactly 100% — **FLAG-ONLY** if sum is off
- [ ] Each probability ≥5% and ≤50% — **FLAG-ONLY** if out of range
- [ ] Each scenario has all 4 components (Narrative, Assumptions, Moat Status, Triggers) — **FIXABLE** if headers missing: add headers + placeholder
- [ ] Moat Status uses valid values (Widened/Stable/Eroding/Impaired/Gone) — **FLAG-ONLY** if invalid value
- [ ] Scenario Overview table present with Total = 100% — **FIXABLE** if table missing: add skeleton
- [ ] No financial projections in narratives — **FLAG-ONLY** if projections found

### Section B: Scenario Completeness

- [ ] Each scenario has probability in 5-50% range — **FLAG-ONLY** if out of range
- [ ] Each scenario has 2-3 paragraph narrative — **FLAG-ONLY** if too short/long
- [ ] Each scenario has 3-5 key assumptions — **FLAG-ONLY** if too few/many
- [ ] Each scenario has moat status from valid enum — **FLAG-ONLY** if invalid
- [ ] Each scenario has trigger signals — **FIXABLE** if header missing: add header + placeholder

### Section C: Probability Validation

- [ ] Sum = 100% (add all 5 probabilities) — **FLAG-ONLY**
- [ ] Probability Rationale section present — **FIXABLE** if missing: add header + placeholder bullets
- [ ] Each scenario has justification in rationale — **FLAG-ONLY** if missing substance
- [ ] Evidence-based rationale (not gut feel) — **FLAG-ONLY** if vague

### Section D: Narrative Quality

- [ ] 2-3 paragraphs per scenario — **FLAG-ONLY** if too short
- [ ] Written as "history from the future" — **FLAG-ONLY** if wrong voice
- [ ] Specific, not generic — **FLAG-ONLY** if generic language detected
- [ ] No financial projections — **FLAG-ONLY** if EPS/revenue targets found
- [ ] Covers full arc (years 1-3, inflection, endpoint) — **FLAG-ONLY** if incomplete

### Section E: Assumptions Quality

- [ ] 3-5 assumptions per scenario — **FLAG-ONLY** if too few/many
- [ ] Specific and verifiable — **FLAG-ONLY** if vague
- [ ] Trace back to research — **FLAG-ONLY** if unsupported
- [ ] Internally consistent — **FLAG-ONLY** if contradictory

### Section F: Trigger Signals Quality

- [ ] Observable within 1-2 years — **FLAG-ONLY** if longer timeframe
- [ ] Specific metrics or events — **FLAG-ONLY** if vague
- [ ] Actionable for investor — **FLAG-ONLY** if not actionable
- [ ] Different across scenarios — **FLAG-ONLY** if duplicated

### Section G: Supporting Sections

- [ ] Key Uncertainties section present (3+ items) — **FIXABLE** if header missing: add header
- [ ] Tailwinds section present (3+ items) — **FIXABLE** if header missing: add header
- [ ] Headwinds section present (3+ items) — **FIXABLE** if header missing: add header
- [ ] Scenario Overview table with all 5 rows — **FIXABLE** if missing: add skeleton
- [ ] Scenario Monitoring section present — **FIXABLE** if missing: add skeleton
- [ ] Quarterly Review Checklist table present — **FIXABLE** if missing: add skeleton table
- [ ] Probability Update Triggers present — **FIXABLE** if missing: add header + placeholder

### Section H: Sources

- [ ] Sources section present — **FIXABLE** if missing: add "## Sources" header
- [ ] All 5 required prerequisite types referenced — **FLAG-ONLY** if types missing
- [ ] Files actually exist as referenced — **FLAG-ONLY** if broken references
- [ ] Specific insights traced to sources — **FLAG-ONLY** if generic sourcing

---

## FIXABLE vs FLAG-ONLY Decision Matrix

| Check | If Missing/Wrong | Classification | Fix Action |
|-------|------------------|----------------|------------|
| Scenario Overview table | Missing entirely | FIXABLE | Add skeleton table with 5 rows + Total |
| Probability Rationale section | Missing header | FIXABLE | Add header + placeholder bullets |
| Key Drivers subsections | Missing headers | FIXABLE | Add Uncertainties/Tailwinds/Headwinds headers |
| Scenario Monitoring section | Missing entirely | FIXABLE | Add skeleton table + update triggers header |
| Sources section | Missing header | FIXABLE | Add "## Sources" + placeholder |
| Total row in overview table | Missing | FIXABLE | Add Total = 100% row |
| Scenario component headers | Missing | FIXABLE | Add Key Assumptions/Moat Status/Trigger Signals headers |
| Table formatting | Broken markdown | FIXABLE | Fix alignment |
| Executive Summary | Missing | FIXABLE | Add header + placeholder |
| Quarterly Review Checklist | Missing table | FIXABLE | Add skeleton table |
| Probability Update Triggers | Missing | FIXABLE | Add header + placeholder |
| Probabilities wrong sum | ≠ 100% | FLAG-ONLY | Note for review |
| Probability out of range | <5% or >50% | FLAG-ONLY | Note for review |
| Wrong scenario count | ≠ 5 | FLAG-ONLY | Note for review |
| Thin narrative | <2 paragraphs | FLAG-ONLY | Note for review |
| Generic language | Not specific | FLAG-ONLY | Note for review |
| Vague assumptions | Not verifiable | FLAG-ONLY | Note for review |
| Invalid moat status | Not in enum | FLAG-ONLY | Note for review |
| Financial projections | Numbers in narrative | FLAG-ONLY | Note for review |
| Vague trigger signals | Not observable | FLAG-ONLY | Note for review |
| Missing prerequisite type in sources | Type not referenced | FLAG-ONLY | Note for review |

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
