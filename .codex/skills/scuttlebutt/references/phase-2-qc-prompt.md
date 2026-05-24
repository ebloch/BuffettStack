# Phase 2: Quality Control Prompt

Use this prompt for the quality-control pass of the scuttlebutt workflow.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing quality control on an Scuttlebutt analysis.

**Context:**
- Company: [COMPANY]
- Analysis Path: [ANALYSIS_PATH]
- Memo Path: [MEMO_PATH]

**Timestamp:** [TIMESTAMP]

---

## CRITICAL: Skill Distinction

**You are running `$quality-control`, NOT `$audit-output`.** These are different skills:

| Skill | What It Does |
|-------|-------------|
| `$quality-control` | Re-searches web sources to find CONTENT gaps, then edits documents in-place |
| `$audit-output` | Checks compliance against templates (no source reading), then edits documents in-place |

**DO NOT** confuse these. This phase uses `$quality-control` which:
- Re-searches the same web sources the synthesis pass used
- Finds missing content that exists in publicly available sources
- Surgically edits the output document(s) to fill gaps — does NOT save a separate report file

**UNIQUE TO SCUTTLEBUTT:** Unlike other skills where QC re-reads file-based sources (10K memos), scuttlebutt QC must re-search the web. You are independently verifying stakeholder coverage by searching review sites, forums, and news — not re-reading local files.

---

## Your Task

Run the quality-control skill on the scuttlebutt analysis to identify and fix content gaps.

**Step 1: Invoke the quality-control skill**
```
$quality-control scuttlebutt "[COMPANY]"
```

**Step 2: Provide source context**

The QC skill needs to evaluate TWO output documents:
- Analysis: `[ANALYSIS_PATH]`
- Memo: `[MEMO_PATH]`

Read both documents using the file-reading tools.

**Step 3: Re-search web sources**

For each stakeholder category in the analysis, independently search for the same data to verify coverage. The key sources to check:

| Stakeholder | Sources to Re-Search |
|-------------|---------------------|
| Customer Voice | Review sites (G2, Capterra, Trustpilot, App Store), forums (Reddit, HN), BBB |
| Employee Voice | Glassdoor, Blind, Indeed, Comparably |
| Partner/Supplier | Partner program reviews, supplier news, developer forums |
| Competitor Voice | "[Company] vs [Competitor]" comparisons, analyst quadrants |
| Industry Expert | Analyst ratings, trade publications |
| Social/Media | Recent news, short interest data, social sentiment |

**Step 4: Compare findings with analysis content**

For each stakeholder category, check:
- Were the key sources actually searched?
- Are metrics and ratings accurate?
- Were important findings missed?
- Are quotes plausible and properly attributed?

**Step 5: Surgically edit to fill gaps**

Use the file-editing tools to fix identified gaps directly in both the Analysis and Memo documents.

---

## Quality Focus Areas for Scuttlebutt

Pay special attention to these scuttlebutt-specific issues:

### Stakeholder Coverage

| Check | What to Verify |
|-------|----------------|
| All 6 categories present | Customer, Employee, Partner, Competitor, Expert, Media all have sections |
| Adequate search effort | Multiple sources consulted per category (not just 1 site) |
| B2B exceptions handled | If B2B, "N/A - B2B model" noted for inapplicable platforms |
| Data gaps disclosed | Missing data acknowledged, not silently omitted |

### Evidence Quality

| Check | What to Verify |
|-------|----------------|
| Quotes are real | Representative quotes traceable to actual review sources |
| Sample sizes noted | Number of reviews/data points stated for quantitative metrics |
| Recency indicated | Data freshness noted (year, or "as of [date]") |
| Sources attributed | Every metric has a named source platform |

### Score Accuracy

| Check | What to Verify |
|-------|----------------|
| Weighted math correct | (Score x Weight) summed correctly for each stakeholder |
| Consistent across 3 locations | Same score in: Analysis Executive Summary, Analysis Scorecard, Memo header |
| Scores justified | Each 1-5 score defensible from the evidence presented |
| No inflation/deflation | Honest calibration against scoring definitions |

### CEO Approval Sourcing

| Check | What to Verify |
|-------|----------------|
| Company-wide figure | CEO approval is for ALL employees, not role-filtered |
| Source identified | Glassdoor company-wide OR Comparably CEO score |
| No fabrication | If unavailable, noted as "Data not available" not estimated |
| Cross-referenced | Checked both Glassdoor and Comparably if possible |

### Missing Web Sources

| Check | What to Verify |
|-------|----------------|
| Glassdoor checked | Primary employee review source |
| Comparably checked | Secondary employee/culture source |
| Blind checked | Anonymous employee feedback |
| Indeed checked | Broader employee coverage |
| Industry-appropriate review sites | G2/Capterra for SaaS, J.D. Power for financial, etc. |
| Short interest data | Finviz, Yahoo Finance, or Nasdaq checked |

### Memo Consistency

| Check | What to Verify |
|-------|----------------|
| Memo reflects Analysis | Scores, ratings, and themes match between documents |
| Quick Reference complete | All required metric rows present |
| Key Takeaways accurate | Bullets align with Analysis findings |
| Moat Implications table | Validation column uses: Validated/Challenged/Neutral |

---

## Gap Classification

Gaps should be classified as:

| Classification | Definition | Examples |
|---------------|------------|----------|
| **CRITICAL** | Undermines the analysis | Score math wrong, stakeholder category missing, fabricated data |
| **HIGH** | Reduces usefulness | Missing source platform, CEO approval role-filtered, thin section |
| **MINOR** | Nice-to-have enhancement | Additional quotes, formatting improvements |

Focus on CRITICAL and HIGH gaps. MINOR gaps can be noted but don't require fixes.

---

## Return Value

When complete, return a JSON object:
```json
{
  "gaps_found": [number],
  "gaps_addressed": [number],
  "status": "success" | "partial" | "failed",
  "remaining_issues": ["list of unresolved issues if any"]
}
```

---

## Important Notes

- You have fresh context — no anchoring on the original synthesis
- Focus on what's MISSING or WRONG, not reformatting what exists
- Re-search the web independently; don't rely on the synthesis pass's searches
- If the QC skill identifies issues it cannot fix (need deeper research), note them in the return value
- Maximum 3 iteration loops within the QC skill
- Edit BOTH the Analysis and Memo if gaps affect both documents
```
