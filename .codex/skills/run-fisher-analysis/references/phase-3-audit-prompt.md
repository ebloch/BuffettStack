# Phase 3: Compliance Audit Prompt

Use this reference for the audit pass for run-fisher-analysis.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing a compliance audit on a Fisher 15-Point Analysis.

**Context:**
- Company: [COMPANY] ([TICKER])
- Analysis Path: [ANALYSIS_PATH]

---

## Your Task

Run the audit-output skill to check the analysis against skill requirements and fix compliance violations.

**Step 1: Invoke the audit-output skill**
```
$audit-output run-fisher-analysis "[COMPANY]"
```

**Step 2: Monitor the audit process**
The skill will:
1. Load skill requirements (SKILL.md, output-template.md, validation-checklist.md)
2. Check the analysis against each requirement
3. Classify violations as FIXABLE or FLAG-ONLY
4. Apply surgical edits for FIXABLE violations

---

## Audit Focus Areas

### What Can Be Fixed (FIXABLE)

- Missing scorecard rows → Add missing points
- Invalid score values (not -2 to +2) → Flag for correction
- Missing verdict section → Add skeleton/placeholder
- Format violations → Fix table structure, section headers
- Missing Sources section → Add skeleton
- Total score not shown → Calculate and add
- Missing disqualifier warning → Add Fisher's quote if P14/P15 = -2

### What Gets Flagged Only (FLAG-ONLY)

- Incorrect evidence/data → Needs source verification
- Score contradicts evidence → Requires human judgment
- Missing content requiring research → Content must come from source files
- Total score math wrong → Needs manual recalculation verification
- Unsupported scores → Must verify against research files

---

## Compliance Checks

Key compliance items from `validation-checklist.md`:

### Section A: Critical Validation

- [ ] **All 15 points scored** — Summary Scorecard table has all 15 rows with valid scores
- [ ] **No score without evidence** — Every score in Detailed Analysis cites specific facts
- [ ] **Points 14 & 15 disqualifier check** — Both reviewed for -2; if either is -2, explicit warning in verdict
- [ ] **Total score math correct** — Sum of 15 individual scores equals stated Total Score
- [ ] **Verdict matches score range** — Per interpretation table

### Section B: Scorecard Completeness

- [ ] Summary Scorecard table present at top
- [ ] All 15 rows populated
- [ ] Scores are valid values (-2, -1, 0, +1, or +2 only)
- [ ] Total Score shown in "X / 30" format

### Section C: Detailed Analysis Quality

For each point (1-15):
- [ ] Score present
- [ ] Analysis present
- [ ] Evidence cited
- [ ] Prior research referenced

### Section D: Evidence Standards

- [ ] Numbers over adjectives (quantified evidence)
- [ ] Specific dates/timeframes
- [ ] Comparisons to peers
- [ ] Source citations

### Section E: Disqualifier Check

- [ ] Point 14 (Transparency) reviewed for -2 status
- [ ] Point 15 (Integrity) reviewed for -2 status
- [ ] If either = -2: Explicit warning in Verdict section
- [ ] If either = -2: Fisher's quote referenced
- [ ] If either = -2: Verdict adjusted (MARGINAL or FAIL)

### Section F: Summary Sections

- [ ] Strengths section lists all +1 and +2 points
- [ ] Concerns section lists all -1 and -2 points
- [ ] Critical Factors (2-3 most important) identified
- [ ] Verdict stated: PASS, MARGINAL, or FAIL
- [ ] 2-3 paragraph synthesis present
- [ ] "Would Philip Fisher invest?" answered

### Section G: Sources

- [ ] Internal research files listed with filenames
- [ ] External sources listed if used

---

## Score Interpretation Table

| Total Score | Interpretation | Expected Verdict |
|-------------|----------------|------------------|
| +20 to +30 | Exceptional quality; rare | PASS |
| +10 to +19 | High quality; strong candidate | PASS |
| 0 to +9 | Average to above-average | MARGINAL |
| -10 to -1 | Below average; significant concerns | MARGINAL or FAIL |
| -30 to -11 | Poor quality; likely avoid | FAIL |

**Disqualifier Override:** A -2 on Point 14 or Point 15 can convert PASS to MARGINAL or FAIL regardless of total score.

---

## Common Audit Issues

| Issue | Type | Fix |
|-------|------|-----|
| Missing point in scorecard | FIXABLE | Add row with placeholder |
| Score out of range (e.g., "+3") | FIXABLE | Flag as violation, add note |
| No Total Score | FIXABLE | Calculate and add |
| Verdict missing | FIXABLE | Add skeleton Verdict section |
| Verdict contradicts score | FLAG-ONLY | Note for human review |
| Total math incorrect | FLAG-ONLY | Note discrepancy for verification |
| Evidence is vague | FLAG-ONLY | Note which points need stronger evidence |
| Disqualifier not flagged | FIXABLE | Add warning to Verdict if P14/P15 = -2 |
| Missing Sources section | FIXABLE | Add skeleton Sources section |
| R&D marked N/A without alternative | FLAG-ONLY | Note Point 3 needs equivalent evaluation |

---

## Disqualifier Handling

**If Point 14 or Point 15 = -2:**

The audit MUST verify:
1. Explicit warning appears in Verdict section (not buried in analysis)
2. Fisher's quote is referenced: "If there is a serious question of the lack of a strong management sense of trusteeship for stockholders, the investor should never seriously consider participating in such an enterprise."
3. Verdict is MARGINAL or FAIL (not PASS)

If any of these are missing, this is a FIXABLE violation — add the required elements.

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
- The analysis should pass all compliance checks after this phase
- Pay special attention to disqualifier handling (Points 14 & 15)
```
