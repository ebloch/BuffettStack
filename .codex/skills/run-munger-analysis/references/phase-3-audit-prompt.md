# Phase 3: Compliance Audit Prompt

Use this reference for the audit pass for run-munger-analysis.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing a compliance audit on a Munger Analysis.

**Context:**
- Company: [COMPANY]
- Analysis Path: [MEMO_PATH]

---

## Your Task

Run the audit-output skill to check the analysis against skill requirements and fix compliance violations.

**Step 1: Invoke the audit-output skill**
```
$audit-output run-munger-analysis "[COMPANY]"
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

## Audit Focus Areas for Munger Analysis

### What Can Be Fixed (FIXABLE)

These violations can be fixed autonomously because they don't require source verification:

| Violation | Fix Applied |
|-----------|-------------|
| Missing category section (of 7) | Add section skeleton from output-template.md |
| "Why Not Higher?" missing for a scored category | Add placeholder: "[Why Not Higher? needed]" |
| Circle of Competence not using INSIDE/PARTIAL/OUTSIDE | Fix to correct format |
| Score not on -2 to +2 scale | Fix format to match scale |
| Holistic Adjustment missing rationale | Add placeholder: "[rationale needed]" |
| Final Score arithmetic wrong | Recalculate: sum of 6 scores + Holistic Adjustment |
| Verdict doesn't match score range | Fix verdict to match score per scale |
| Summary table scores don't match section scores | Fix table to match sections |
| "Would Munger Buy This?" not answered | Add placeholder section |
| One-Sentence Thesis missing | Add placeholder: "[thesis needed]" |
| Key Strengths missing (need 3) | Add placeholder bullets |
| Key Concerns missing (need 3) | Add placeholder bullets |
| Sources section missing or incomplete | Add missing source file references |
| Score Reconciliation table missing | Add template from output-template.md |
| Lollapalooza score negative | Fix to 0 (minimum for this category) |

### What Gets Flagged Only (FLAG-ONLY)

These violations are documented but NOT fixed because they require analytical judgment:

| Violation | Why Flagged |
|-----------|-------------|
| Content quality thin in a section | Requires re-reading source docs to expand |
| "Why Not Higher?" answer not substantive | Requires analytical judgment to improve |
| Score seems inflated (e.g., +2 with concerns) | Requires scoring judgment |
| Circle of Competence assessment seems wrong | Requires business understanding |
| Holistic Adjustment rationale thin | Requires cross-cutting analysis |
| Verdict doesn't match gut check narrative | Requires reconciliation judgment |
| Moat direction assessment unsupported | Requires competitive evidence |
| Mental models generic, not company-specific | Requires deeper analysis |
| Tensions Registry incomplete | Requires cross-stage analysis |

---

## Compliance Checks

### Summary Table

- [ ] All 7 categories present with scores and assessments
- [ ] "Why Not Higher?" column filled for every row
- [ ] Holistic Adjustment row present with rationale
- [ ] Category Subtotal calculated correctly (sum of 6 scored categories)
- [ ] Final Score = Subtotal + Holistic Adjustment
- [ ] Verdict matches score range:
  - +9 to +12 = EXCEPTIONAL
  - +5 to +8 = STRONG
  - +1 to +4 = ACCEPTABLE
  - -4 to 0 = WEAK
  - -12 to -5 = AVOID
- [ ] One-Sentence Thesis present and specific to this company
- [ ] Key Strengths has exactly 3 bullets
- [ ] Key Concerns has exactly 3 bullets

### Section 1: Circle of Competence

- [ ] Assessment uses INSIDE / PARTIAL / OUTSIDE (not a numeric score)
- [ ] Business explanation is 2-3 sentences
- [ ] 3 key economic drivers identified
- [ ] 3 failure modes listed (Inversion)
- [ ] One-Paragraph Explanation present
- [ ] Key Insight block present

### Section 2: Moat & Competitive Advantage

- [ ] Score uses -2 to +2 scale
- [ ] Assessment uses: WIDE & WIDENING / WIDE & STABLE / NARROW / ERODING / NONE
- [ ] Moat type table with at least 2 types rated
- [ ] Direction stated with evidence
- [ ] Key Barriers listed (minimum 2)
- [ ] Returns on Capital table with ROIC and ROE
- [ ] Key Insight block present

### Section 3: Quality of Management

- [ ] Score uses -2 to +2 scale
- [ ] Assessment uses: EXCEPTIONAL / GOOD / ADEQUATE / CONCERNING / POOR
- [ ] Incentive Alignment table present
- [ ] Capital Allocation Track Record table (M&A, Buybacks, Reinvestment)
- [ ] Candor & Transparency section present
- [ ] Credibility Score table (if management audit available)
- [ ] Say/Do Quadrant placement stated
- [ ] Key Insight block present

### Section 4: Predictability & Simplicity

- [ ] Score uses -2 to +2 scale
- [ ] Assessment uses: HIGH / MODERATE-HIGH / MODERATE / LOW / VERY LOW
- [ ] Stability Factors listed (minimum 3)
- [ ] Volatility Factors listed (minimum 2)
- [ ] "What Could Go Wrong?" has 5 specific risks
- [ ] Key Insight block present

### Section 5: Financial Strength

- [ ] Score uses -2 to +2 scale
- [ ] Assessment uses: FORTRESS / STRONG / ADEQUATE / WEAK / DISTRESSED
- [ ] Balance Sheet table with specific $ amounts
- [ ] Leverage table with Debt/EBITDA, Interest Coverage
- [ ] Returns on Capital table with Current, 5Y Ago, Direction
- [ ] Free Cash Flow table with FCF Margin, FCF Conversion
- [ ] Key Insight block present

### Section 6: Long-Term Orientation

- [ ] Score uses -2 to +2 scale
- [ ] Assessment uses: STRONG COMPOUNDER / MODERATE / LIMITED / UNLIKELY / VALUE TRAP
- [ ] 10-20 Year Ownership Comfort section present
- [ ] Secular Tailwinds listed (minimum 3)
- [ ] Secular Headwinds listed (minimum 3)
- [ ] Compounding Potential table present
- [ ] 10-Year Scenarios table present
- [ ] Key Insight block present

### Section 7: Lollapalooza Effects

- [ ] Score uses +2 / +1 / 0 only (never negative)
- [ ] Assessment uses: PRESENT / PARTIAL / NONE
- [ ] Combining Forces section present
- [ ] Virtuous Cycle mapped OR "No clear virtuous cycle identified"
- [ ] 5 mental models listed with application explanations
- [ ] Key Insight block present

### Final Verdict

- [ ] Score Reconciliation table completed (gut check, what would change mind, comparable companies)
- [ ] "Would Munger Buy This?" answered with Yes/No/Maybe + 2-3 sentence rationale
- [ ] "At what price?" addresses valuation sensitivity

### Sources

- [ ] Sources section present
- [ ] Lists all research files used (Business Overview, Financial Statements, Management Audit, etc.)

---

## FIXABLE vs FLAG-ONLY Decision Matrix

| Check | If Missing/Wrong | Classification | Fix Action |
|-------|------------------|----------------|------------|
| Category section missing | Missing entirely | FIXABLE | Add skeleton from output-template |
| "Why Not Higher?" blank | Empty field | FIXABLE | Add "[Why Not Higher? needed]" |
| CoC format wrong | Not INSIDE/PARTIAL/OUTSIDE | FIXABLE | Fix format |
| Score format wrong | Not -2 to +2 | FIXABLE | Fix format |
| Holistic Adjustment no rationale | Missing text | FIXABLE | Add "[rationale needed]" |
| Final Score arithmetic | Wrong sum | FIXABLE | Recalculate correctly |
| Verdict vs. score mismatch | Wrong verdict for range | FIXABLE | Fix verdict to match |
| Summary table mismatch | Table ≠ sections | FIXABLE | Fix table to match sections |
| Missing Munger verdict | No "Would Munger Buy?" | FIXABLE | Add placeholder section |
| Missing thesis | No one-sentence thesis | FIXABLE | Add "[thesis needed]" |
| Missing strengths/concerns | <3 bullets | FIXABLE | Add placeholder bullets |
| Missing sources | No sources section | FIXABLE | Add from source paths |
| Lollapalooza negative score | Score < 0 | FIXABLE | Set to 0 |
| Content quality thin | Weak analysis | FLAG-ONLY | Note for review |
| Score seems inflated | +2 with concerns | FLAG-ONLY | Note for review |
| Assessment mismatch | Assessment contradicts score | FLAG-ONLY | Note for review |
| Mental models generic | Not company-specific | FLAG-ONLY | Note for review |
| Tensions incomplete | Missing cross-stage tensions | FLAG-ONLY | Note for review |

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

- This audit does NOT read source documents — it only checks compliance against templates
- FLAG-ONLY issues should be passed to user for manual review
- All FIXABLE violations should be addressed before completing
- The analysis should pass all format/structure checks after this phase
- Make scoped file edits — don't rewrite the entire analysis
```
