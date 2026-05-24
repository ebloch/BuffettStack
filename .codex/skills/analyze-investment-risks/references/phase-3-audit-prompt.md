# Phase 3: Compliance Audit Prompt

Use this reference for the audit pass for analyze-investment-risks.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing a compliance audit on a Risk Analysis.

**Context:**
- Company: [COMPANY]
- Analysis Path: [MEMO_PATH]

---

## Your Task

Run the audit-output skill to check the analysis against skill requirements and fix compliance violations.

**Step 1: Invoke the audit-output skill**
```
$audit-output analyze-investment-risks "[COMPANY]"
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

## Audit Focus Areas for Risk Analysis

### What Can Be Fixed (FIXABLE)

These violations can be fixed autonomously because they don't require source verification:

| Violation | Fix Applied |
|-----------|-------------|
| Missing risk category (of 7 required) | Add category skeleton from output-template.md |
| Scoring rubric missing | Add rubric table from output template |
| Severity math wrong (P × I ≠ stated) | Recalculate correct value |
| Severity uncapped (>10) | Cap at 10 |
| Top 5 not ranked by severity | Reorder to match severity scores |
| Top 5 missing financial impact | Add "[impact estimate needed]" placeholder |
| <3 thesis killers | Add placeholder rows |
| Thesis killers missing timeframes | Add "[timeframe needed]" placeholder |
| Dashboard has placeholders ("TBD", "[X]") | Add "[current value needed]" placeholder |
| Warning levels vague ("declining") | Add "[specific threshold needed]" placeholder |
| Dashboard <5 metrics | Add placeholder rows |
| Missing downside scenario (Mild/Severe/Catastrophic) | Add skeleton from output template |
| Missing probability justification | Add "[justification needed]" placeholder |
| Risk correlations section missing | Add skeleton section with placeholder cluster |
| Mitigant is "management awareness" | Add "[specific mitigant needed]" placeholder |
| Sources section missing | Add from source document paths |
| Executive Summary missing | Add skeleton |

### What Gets Flagged Only (FLAG-ONLY)

These violations are documented but NOT fixed because they require analytical judgment:

| Violation | Why Flagged |
|-----------|-------------|
| Probability out of bounds (<5% or >40%) | Needs judgment to adjust — cannot pick value mechanically |
| Probability sum ≥100% | Needs rebalancing across scenarios — requires judgment |
| Overall Risk Level hybrid ("MODERATE-HIGH") | Needs judgment to pick one of LOW/MODERATE/HIGH/VERY HIGH |
| Top 5 financial impact seems wrong | Requires analytical judgment to correct estimate |
| Executive Summary doesn't match body | Requires reconciliation across sections |
| Content quality thin in a category | Requires re-reading source docs to expand (QC responsibility) |
| Risk assessment contradicts source findings | Requires source comparison and reconciliation |
| Thesis killer seems too vague but has timeframe | Requires judgment on specificity threshold |

---

## Compliance Checks

### Executive Summary

- [ ] Executive Summary present with 1-2 paragraphs
- [ ] Overall Risk Level stated (exactly LOW / MODERATE / HIGH / VERY HIGH)

### Risk Assessment by Category

- [ ] All 7 risk categories present (Business Model, Competitive, Financial, Operational, Regulatory/Political, Valuation, ESG/Reputational)
- [ ] Each category has substantive analysis (not placeholder text like "[Analysis here]")
- [ ] No empty categories

### Risk Matrix

- [ ] Scoring Rubric included (Probability and Impact definitions with numeric values)
- [ ] Risk Matrix table present
- [ ] Each risk has: Risk description, Category, Probability, Impact, Severity, Mitigant
- [ ] Probability values valid: Low(1), Medium(2), High(3) only
- [ ] Impact values valid: Low(1), Medium(2), High(3), Very High(4) only
- [ ] Severity math correct: P × I = Severity for every row
- [ ] Severity capped at 10 (even if P × I > 10)
- [ ] Mitigants are specific (not "management awareness" or "diversified revenue")

### Top 5 Risks

- [ ] Exactly 5 risks listed
- [ ] Ranked by severity (highest first)
- [ ] Ranking matches severity scores from risk matrix
- [ ] Each has description AND financial impact estimate
- [ ] Financial impact is quantified (not "significant impact")

### Risk Correlations

- [ ] Risk Correlations section present
- [ ] At least one correlated risk cluster in table
- [ ] Cascade scenario described for each cluster
- [ ] Combined severity estimated
- [ ] Key Insight sentence present

### Thesis Killers

- [ ] 3-5 thesis killers identified (not <3, not >5)
- [ ] Each is specific and observable (not "things get worse")
- [ ] Each explains why it's fatal
- [ ] Each has timeframe (Immediate / 1-2 quarters / 1+ year)

### Monitoring Dashboard

- [ ] At least 5 metrics in dashboard table
- [ ] Current values are actual numbers (no "TBD", "[X]", "N/A")
- [ ] Warning levels are specific thresholds (no "declining", "worsening")
- [ ] Status indicators present (G/Y/R for each row)
- [ ] Check Frequency present for each row

### Downside Scenarios

- [ ] All 3 scenarios present (Mild, Severe, Catastrophic)
- [ ] Each has Assumptions, Impact, and Probability
- [ ] Probability methodology stated at top of section
- [ ] Each probability has justification (not bare percentage)
- [ ] Each probability: 5% ≤ P ≤ 40%
- [ ] Sum of all probabilities < 100%

### Sources

- [ ] Sources section present
- [ ] Lists prerequisite research files used
- [ ] External sources listed with dates (if used)

---

## FIXABLE vs FLAG-ONLY Decision Matrix

| Check | If Missing/Wrong | Classification | Fix Action |
|-------|------------------|----------------|------------|
| Risk category missing (of 7) | Missing entirely | FIXABLE | Add skeleton from output template |
| Scoring rubric missing | No P/I definitions | FIXABLE | Add rubric table |
| Severity math wrong | P × I ≠ stated | FIXABLE | Recalculate |
| Severity >10 | Uncapped | FIXABLE | Cap at 10 |
| Top 5 wrong order | Doesn't match severity | FIXABLE | Reorder |
| Top 5 no impact | No financial estimate | FIXABLE | Add "[impact estimate needed]" |
| <3 thesis killers | Too few | FIXABLE | Add placeholder rows |
| No timeframes | Missing from thesis killers | FIXABLE | Add "[timeframe needed]" |
| Dashboard placeholders | "TBD" values | FIXABLE | Add "[current value needed]" |
| Warning levels vague | "declining" | FIXABLE | Add "[specific threshold needed]" |
| Dashboard <5 rows | Too few metrics | FIXABLE | Add placeholder rows |
| Missing scenario | <3 scenarios | FIXABLE | Add skeleton |
| No probability justification | Bare percentage | FIXABLE | Add "[justification needed]" |
| Risk correlations missing | No section | FIXABLE | Add skeleton section |
| Vague mitigant | "management awareness" | FIXABLE | Add "[specific mitigant needed]" |
| Sources missing | No section | FIXABLE | Add from source paths |
| Executive Summary missing | Not present | FIXABLE | Add skeleton |
| Probability out of bounds | <5% or >40% | FLAG-ONLY | Needs judgment to adjust |
| Probability sum ≥100% | Sum too high | FLAG-ONLY | Needs rebalancing |
| Risk Level hybrid | "MODERATE-HIGH" | FLAG-ONLY | Needs judgment to pick one |
| Impact estimate wrong | Seems incorrect | FLAG-ONLY | Needs analytical judgment |
| Summary ≠ body | Inconsistent | FLAG-ONLY | Needs reconciliation |
| Content thin | Weak analysis | FLAG-ONLY | QC responsibility |
| Contradicts sources | Inconsistent with research | FLAG-ONLY | Needs source comparison |

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
