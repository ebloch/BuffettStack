# Phase 3: Compliance Audit Prompt

Use this prompt for the compliance-audit pass of the scuttlebutt workflow.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing a compliance audit on an Scuttlebutt analysis.

**Context:**
- Company: [COMPANY]
- Analysis Path: [ANALYSIS_PATH]
- Memo Path: [MEMO_PATH]

**Timestamp:** [TIMESTAMP]

---

## Your Task

Run the audit-output skill to check both the Analysis and Memo against skill requirements and fix compliance violations.

**Step 1: Invoke the audit-output skill**
```
$audit-output scuttlebutt "[COMPANY]"
```

**Step 2: Monitor the audit process**

The skill will:
1. Load skill requirements:
   - `SKILL.md`
   - `output-template-analysis.md`
   - `output-template-memo.md`
   - `validation-checklist.md`
2. Check BOTH documents against each requirement
3. Classify violations as FIXABLE or FLAG-ONLY
4. Apply surgical edits for FIXABLE violations

---

## Audit Focus Areas for Scuttlebutt

**IMPORTANT:** Scuttlebutt produces TWO output documents (Analysis + Memo). Both must be audited.

### What Can Be Fixed (FIXABLE)

These violations can be fixed autonomously because they don't require source verification:

| Violation | Fix Applied |
|-----------|-------------|
| Missing section skeletons in Analysis | Add template section with placeholder content |
| Missing "Switching Intent Signals" subsection | Add subsection header with placeholder |
| Missing "Customer Support Quality" subsection | Add subsection header with placeholder |
| Missing "N/A - B2B model" notes for inapplicable platforms | Add notation where appropriate |
| Score inconsistency across 3 locations | Recalculate weighted average and update all 3 locations |
| Missing severity ratings on red flags | Add "[severity needed]" placeholder |
| Missing warning thresholds on monitoring metrics | Add "[threshold needed]" placeholder |
| Missing "Data not available" notes for unfound metrics | Add notation |
| Memo Quick Reference missing a required metric row | Add row with placeholder value |
| Memo Moat Implications table missing Validation column values | Add "Neutral" placeholder |
| Missing "What Stakeholders Love" or "Complain About" minimum rows | Add placeholder rows to reach 4 minimum |
| Format violations | Fix table structure, section headers |
| Missing confidence justification in Partner/Supplier section | Add "[justification needed]" |

### What Gets Flagged Only (FLAG-ONLY)

These violations are documented but NOT fixed because they require judgment or re-research:

| Violation | Why Flagged |
|-----------|-------------|
| Score seems wrong for evidence presented | Needs judgment to recalibrate |
| Thin stakeholder section (few sources, sparse evidence) | Needs web re-search to expand |
| Quotes may be fabricated or misattributed | Needs source verification |
| CEO approval appears role-filtered, not company-wide | Needs Glassdoor/Comparably re-search |
| Customer Review Avg uses ACSI instead of review platform avg | Needs recalculation from correct sources |
| Monitoring thresholds use vague language ("declining") | Needs industry research for specific numbers |
| Memo Key Takeaways don't match Analysis findings | Needs content judgment to align |
| Short interest reported as "Low (est.)" without source | Needs actual data lookup |

---

## Compliance Checks

### Analysis Document

#### Executive Summary
- [ ] 3-4 paragraphs present
- [ ] Scuttlebutt Health Score stated (X.X / 5.0)
- [ ] Assessment stated (Strong / Mixed / Concerning / Poor)
- [ ] Score matches Scorecard table

#### Scorecard Table
- [ ] All 6 stakeholders listed with correct weights (30/25/15/10/10/10)
- [ ] Each row has: Score, Weighted Score, Key Signal
- [ ] Overall row present with weighted sum
- [ ] **CRITICAL:** Overall score matches Executive Summary and Memo header

#### Section 1: Customer Voice
- [ ] Overview with Score, Trend, Sample Size
- [ ] Quantitative Metrics table (at least 2 source rows)
- [ ] "What Customers Love" table (at least 2 themes with quotes)
- [ ] "What Customers Complain About" table (at least 2 themes with quotes and severity)
- [ ] "Switching Intent Signals" subsection present
- [ ] "Customer Support Quality" subsection present
- [ ] Customer Voice Summary paragraph(s)

#### Section 2: Employee Voice
- [ ] Overview with Score, Trend, Primary Source
- [ ] Glassdoor Metrics table (Overall Rating, CEO Approval, Recommend, Outlook)
- [ ] Culture Dimension Scores table
- [ ] "What Employees Praise" table
- [ ] "What Employees Complain About" table
- [ ] Leadership Sentiment subsection
- [ ] Hiring and Retention Signals subsection
- [ ] Employee Voice Summary paragraph(s)
- [ ] CEO approval is company-wide (not role-filtered)
- [ ] Comparably data captured or "Not available" noted
- [ ] Blind data captured or "Not available" noted
- [ ] Indeed data captured or "Not available" noted

#### Section 3: Partner/Supplier Voice
- [ ] Overview with Score, Confidence level, Confidence Justification
- [ ] Partner Program Sentiment table
- [ ] Supplier Relationship Signals table
- [ ] Developer Community section (if tech) or omitted (if not applicable)
- [ ] Summary paragraph(s)

#### Section 4: Competitor Voice
- [ ] Overview with Score, Assessment
- [ ] Competitive Positioning Analysis table
- [ ] Win/Loss Intelligence section
- [ ] Analyst Positioning table (if applicable)
- [ ] Summary paragraph(s)

#### Section 5: Industry Expert Voice
- [ ] Overview with Score, Consensus
- [ ] Analyst Sentiment table
- [ ] Trade Publication Coverage table
- [ ] Expert Concerns and Praise sections
- [ ] Summary paragraph(s)

#### Section 6: Social/Media Sentiment
- [ ] Overview with Score, Recent Trend
- [ ] News Sentiment table
- [ ] Social Media Signals table
- [ ] Short Interest and Activist Signals table
- [ ] Summary paragraph(s)

#### Pattern Analysis
- [ ] Cross-Stakeholder Themes table
- [ ] Positive Patterns section
- [ ] Concerning Patterns section
- [ ] Sentiment Divergence section

#### Red Flags
- [ ] Red flags table present (even if "none identified")
- [ ] Each flag has: Severity (High/Medium/Low), Stakeholder Source, Evidence, Moat Implication
- [ ] Red Flag Summary status line

#### Moat Implications
- [ ] Customer -> Moat Assessment table
- [ ] Employee -> Operational Health table
- [ ] Partner -> Ecosystem Strength table
- [ ] Competitive -> Competitive Position table
- [ ] Overall Moat Assessment paragraph(s)
- [ ] Moat Validation Status (Validated / Partially Validated / Challenged / Inconclusive)

#### Monitoring Dashboard
- [ ] At least 5 metrics with Current Value, Warning Threshold, Frequency
- [ ] **CRITICAL:** All warning thresholds are specific numbers (not "declining" or "unknown")
- [ ] Early Warning Signals checklist by stakeholder

#### Data Sources
- [ ] Sources Consulted table by category
- [ ] Limitations section
- [ ] Search Queries Used section

#### Conclusion
- [ ] Overall Score and Assessment restated
- [ ] Investment Implications (Trust/Skeptical/Monitor lists)
- [ ] Connection to Other Analyses section

### Memo Document

#### Header
- [ ] Health Score matches Analysis Scorecard
- [ ] Assessment matches Analysis
- [ ] Date present

#### Key Takeaways
- [ ] 5-7 bullets with bold lead-ins
- [ ] Includes switching intent signal if customer data shows it
- [ ] Aligns with Analysis findings

#### Scorecard
- [ ] All 6 stakeholders with Score, Weight, Weighted, Key Signal
- [ ] Overall score matches Analysis

#### What Stakeholders Love
- [ ] Table with at least 4 rows
- [ ] Covers Customers, Employees, Partners at minimum
- [ ] Moat Signal summary below table

#### What Stakeholders Complain About
- [ ] Table with at least 4 rows with Severity column
- [ ] Covers Customers, Employees, Partners at minimum
- [ ] Moat Risk summary below table

#### Red Flags to Monitor
- [ ] Checklist format with warning thresholds
- [ ] Current Status line

#### Moat Implications
- [ ] Table with Aspect, Signal, Validation columns
- [ ] Validation uses: Validated / Challenged / Neutral (nothing else)
- [ ] Overall Moat Validation status

#### Bottom Line
- [ ] 2-4 sentences synthesizing investment implication

#### Quick Reference
- [ ] Health Score row
- [ ] Glassdoor Rating row
- [ ] CEO Approval row (or "Data not available")
- [ ] Customer Review Avg row (NOT ACSI — review platform average)
- [ ] Short Interest row
- [ ] Red Flag Status row

---

## FIXABLE vs FLAG-ONLY Decision Matrix

| Check | If Missing/Wrong | Classification | Fix Action |
|-------|------------------|----------------|------------|
| Section skeleton missing | Missing entirely | FIXABLE | Add template section |
| "N/A - B2B model" notation | Missing for B2B | FIXABLE | Add notation |
| Score math wrong | Arithmetic error | FIXABLE | Recalculate + update all 3 locations |
| Red flag severity | Missing rating | FIXABLE | Add "[severity needed]" |
| Warning threshold | Missing or vague | FIXABLE | Add "[threshold needed]" |
| "Data not available" note | Missing | FIXABLE | Add notation |
| Quick Reference row | Missing metric | FIXABLE | Add row with placeholder |
| Moat Validation column | Missing/wrong term | FIXABLE | Add "Neutral" placeholder |
| Confidence justification | Missing | FIXABLE | Add "[justification needed]" |
| Score vs evidence mismatch | Score seems off | FLAG-ONLY | Note for manual review |
| Thin stakeholder section | Sparse content | FLAG-ONLY | Note: needs re-search |
| Quotes seem fabricated | Unverifiable | FLAG-ONLY | Note: needs source check |
| CEO approval role-filtered | Wrong scope | FLAG-ONLY | Note: needs re-search |
| Short interest estimated | No real data | FLAG-ONLY | Note: needs data lookup |
| Key Takeaways misaligned | Doesn't match Analysis | FLAG-ONLY | Note for manual review |

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

- This audit does NOT read source documents or search the web — it only checks compliance
- FLAG-ONLY issues should be passed to user for manual review
- All FIXABLE violations should be addressed before completing
- Both Analysis and Memo should pass all format/structure checks after this phase
- Use surgical edits (file-editing tools) — don't rewrite entire documents
- When fixing score inconsistency, recalculate from individual stakeholder scores and update all 3 locations
```
