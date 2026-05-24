# Phase 3: Compliance Audit Prompt

Use this reference for the audit pass for audit-management-credibility.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing a compliance audit on a Management Credibility Audit.

**Context:**
- Company: [COMPANY]
- Analysis Path: [ANALYSIS_PATH]
- Memo Path: [MEMO_PATH]
- Timestamp: [TIMESTAMP]

---

## Your Task

Run the audit-output skill to check both the Analysis and Memo against skill requirements and fix compliance violations.

**Step 1: Invoke the audit-output skill**
```
$audit-output audit-management-credibility "[COMPANY]"
```

**Step 2: Monitor the audit process**

The skill will:
1. Load skill requirements:
   - `SKILL.md`
   - `output-template-analysis.md`
   - `output-template-memo.md`
   - `validation-checklist.md`
2. Check both documents against each requirement
3. Classify violations as FIXABLE or FLAG-ONLY
4. Apply surgical edits for FIXABLE violations

---

## Two-Document Audit

**CRITICAL: This skill produces TWO output documents.** Both must be audited:

### Analysis Document (15 Required Sections)

Check each section exists and meets requirements:

| # | Section | Key Compliance Checks |
|---|---------|----------------------|
| 1 | **Data Sources** | Table present with 4 columns (Source, Count, Date Range, Coverage) |
| 2 | **Executive Summary** | Rating stated (HIGH/MODERATE/LOW/CONCERNING), 3-5 paragraphs |
| 3 | **Quantitative Scorecard** | All 3 tables present (Promise Delivery, Trend Over Time, Guidance Accuracy) |
| 4 | **Say/Do Matrix Placement** | ASCII diagram, quadrant name, rationale, investment implication |
| 5 | **Key Management Quotes** | 5-10 verbatim quotes with speaker/title/quarter attribution |
| 6 | **Missed & Partial Promises** | Table of scores <=0, analysis paragraph (or explicit "none" statement) |
| 7 | **Promise-by-Promise Detail** | 5 category tables with verbatim quotes in each row |
| 8 | **Pattern Analysis** | Positive patterns, concerning patterns, kitchen sink analysis |
| 9 | **Capital Allocation** | M&A synergies table, buyback timing table, other decisions, overall rating |
| 10 | **Insider Ownership & Compensation** | Ownership table (3+ execs), transactions, comp structure, alignment score |
| 11 | **Non-GAAP Definition Drift** | Year 1 vs Year 5 comparison table, GAAP vs Non-GAAP gap table |
| 12 | **Red Flags Identified** | Table with severity ratings, summary statement |
| 13 | **Deep Dive: Key Issues** | Structured analysis OR explicit "No issues warranting deep dive" |
| 14 | **Conclusion** | Rating with criteria, guidance discount %, monitoring points (3-5 items) |
| 15 | **Appendix: Source Documents** | Transcript table with ALL quarters listed |

### Memo Document (7 Required Sections)

| # | Section | Key Compliance Checks |
|---|---------|----------------------|
| 1 | **Header** | Rating, Matrix Placement, Audit Period, Quarters Reviewed |
| 2 | **Key Takeaways** | 5-7 bullets with line breaks between |
| 3 | **What You Can Trust** | TABLE format (Guidance Type, Track Record, Confidence) |
| 4 | **What to Discount** | TABLE format (Guidance Type, Issue, Recommended Discount) |
| 5 | **Red Flags to Monitor** | CHECKLIST format (- [ ] items) |
| 6 | **Bottom Line** | 2-4 sentences |
| 7 | **Quick Reference** | TABLE with ALL 5 metrics (Hit Rate, Composite Score, Guidance Style, Capital Allocation, Insider Alignment) |

---

## Audit Focus Areas

### What Can Be Fixed (FIXABLE)

These violations can be fixed autonomously because they don't require source verification:

| Violation | Fix Applied |
|-----------|-------------|
| Missing section header (of 15 Analysis / 7 Memo) | Add section header with skeleton from output template |
| Missing Data Sources table | Add skeleton table with placeholder rows |
| Missing Quantitative Scorecard table (of 3 required) | Add skeleton table from output template |
| Missing Say/Do Matrix ASCII diagram | Add diagram from output template |
| Missing Missed & Partial Promises section | Add section header with "None identified" if no scores <=0 |
| Missing Promise-by-Promise category table | Add skeleton table for missing category |
| Missing Kitchen Sink Analysis section | Add "None identified" statement |
| Missing Capital Allocation rating | Add "[rating needed]" placeholder |
| Missing Executive Ownership proxy source citation | Add "*Source: [proxy citation needed]*" placeholder |
| Missing Base Salary column in ownership table | Add column with "[salary needed]" |
| Missing Non-GAAP Definition Drift table | Add skeleton comparison table |
| Missing Deep Dive: Key Issues section | Add section with "No issues warranting deep dive" if appropriate |
| Missing Appendix: Source Documents | Add skeleton appendix table |
| Missing Quick Reference table in Memo | Add skeleton with "[value needed]" placeholders |
| Memo "What You Can Trust" in prose format | Convert to TABLE format |
| Memo "What to Discount" in prose format | Convert to TABLE format |
| Memo "Red Flags to Monitor" not checklist format | Convert to "- [ ]" checklist format |
| Format violations (broken tables, missing headers) | Fix table structure, add headers |

### What Gets Flagged Only (FLAG-ONLY)

These violations are documented but NOT fixed because they require source data or analytical judgment:

| Violation | Why Flagged |
|-----------|-------------|
| Incorrect promise scores | Needs transcript to verify correct score |
| Wrong verbatim quotes | Needs transcript to verify actual quote |
| Hit rate calculation error | Needs recounting of all scored promises |
| Composite score calculation error | Needs recalculation from all scores |
| Cross-document content mismatch (Analysis says X, Memo says Y) | Requires judgment on which is correct |
| Rating contradicts evidence | Requires analytical judgment |
| Missing promises from transcripts | Requires re-reading source transcripts (QC responsibility) |
| Insider ownership data incorrect | Needs proxy verification |
| Compensation breakdown doesn't sum to ~100% | Needs source verification |
| Capital allocation data incorrect | Needs source verification |
| Thin analysis sections | Requires source reading to expand |

---

## Cross-Document Consistency Checks

**CRITICAL:** These checks verify Analysis and Memo are consistent. Inconsistencies are FLAG-ONLY (require judgment on which is correct):

| Check | Analysis Location | Memo Location | Must Match |
|-------|-------------------|---------------|------------|
| Credibility Rating | Executive Summary, Conclusion | Header | Exact match (HIGH/MODERATE/LOW/CONCERNING) |
| Say/Do Matrix Placement | Section 4 | Header | Exact quadrant name |
| Promise Hit Rate | Quantitative Scorecard Total row | Quick Reference | Exact percentage |
| Composite Score | Quantitative Scorecard Total row | Quick Reference | Exact value |
| Guidance Style | Guidance Accuracy section | Quick Reference | Exact label |
| Capital Allocation Rating | Capital Allocation section | Quick Reference | Exact label |
| Insider Alignment | Overall Alignment Score section | Quick Reference | Exact label |
| Red Flag Status | Red Flags section | Red Flags to Monitor | Consistent severity |

---

## Compliance Checks Detail

### Data Sources (Section 1)

- [ ] Table present with 4 columns: Source, Count, Date Range, Coverage
- [ ] Quarter count mathematically correct
- [ ] Header/Appendix quarter count consistent
- [ ] Data gaps explicitly documented (or "None — full coverage")

### Quantitative Scorecard (Section 3)

- [ ] Table 1: Promise Delivery Summary — 5 categories + Total row
- [ ] Table 2: Trend Over Time — all audit years represented
- [ ] Table 3: Guidance Accuracy — metric types listed (or "Not Provided")
- [ ] Trend statement present (Improving/Stable/Declining)
- [ ] Guidance style statement present

### Promise-by-Promise Detail (Section 7)

- [ ] All 5 category tables present (Financial, Capital Allocation, Operational, Cost/Efficiency, Strategic)
- [ ] Each table has required columns: Date, Promise (verbatim), Source, Specificity, Timeframe, Outcome, Score
- [ ] Cost/Efficiency table: Only formal programs (no "N/A" rows for informal initiatives)
- [ ] Cost/Efficiency: Dollar amounts in Restructuring Cost and Actual Savings columns

### Insider Ownership (Section 10)

- [ ] Ownership table has 3+ executives (CEO, CFO, +1) or explicit explanation
- [ ] Table includes Base Salary column
- [ ] Proxy source cited with page numbers (or explicit note if unavailable)
- [ ] Source is NOT an aggregator site (TipRanks, GuruFocus)
- [ ] Compensation Structure table with % breakdown
- [ ] CEO total compensation stated
- [ ] Pay vs performance comparison (3 growth rates)
- [ ] Overall Alignment Score table with factor scores

### Appendix (Section 15)

- [ ] Earnings Transcripts table lists ALL quarters in audit period
- [ ] Table has columns: Quarter, Date, Source, Notes
- [ ] Quarter count matches header and Data Sources section

---

## FIXABLE vs FLAG-ONLY Decision Matrix

| Check | If Missing/Wrong | Classification | Fix Action |
|-------|------------------|----------------|------------|
| Section header missing | Missing entirely | FIXABLE | Add skeleton from output template |
| Table missing (structural) | Required table absent | FIXABLE | Add skeleton table |
| "None identified" statement | Section empty | FIXABLE | Add explicit statement |
| Format wrong (prose vs table) | Wrong output format | FIXABLE | Convert to correct format |
| Proxy source placeholder | Missing citation | FIXABLE | Add "[proxy citation needed]" |
| Promise score wrong | Incorrect value | FLAG-ONLY | Note for review |
| Quote not verbatim | Paraphrased | FLAG-ONLY | Note for transcript verification |
| Math error in scorecard | Wrong calculation | FLAG-ONLY | Note for recalculation |
| Cross-document mismatch | Values differ | FLAG-ONLY | Note both values, flag inconsistency |
| Rating contradicts evidence | Logic error | FLAG-ONLY | Note for analytical review |
| Content thin | Lacks depth | FLAG-ONLY | Note for source re-reading |

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
- Both Analysis AND Memo must be checked
- Cross-document consistency is a key audit focus for this dual-document skill
- FLAG-ONLY issues should be passed to user for manual review
- All FIXABLE violations should be addressed before completing
- Both documents should pass all format/structure checks after this phase
- Make scoped file edits — don't rewrite entire documents
```
