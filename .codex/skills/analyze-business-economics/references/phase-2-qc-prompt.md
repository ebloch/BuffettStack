# Phase 2: Quality Control Prompt

Use this reference for the QC pass for analyze-business-economics.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing quality control on a Business Economics Analysis.

**Context:**
- Company: [COMPANY]
- Analysis Path: [MEMO_PATH]
- Industry: [INDUSTRY] (or "none" if no industry checklist was used)

**Source Document (for re-reading):**
[SOURCE_MEMO_PATH]

**Industry Checklist (if applicable):**
[INDUSTRY_CHECKLIST_PATH] (or "N/A" if no industry checklist)

---

## CRITICAL: Skill Distinction

**You are running `$quality-control`, NOT `$audit-output`.** These are different skills:

| Skill | What It Does |
|-------|-------------|
| `$quality-control` | Re-reads source docs (10K memos) to find CONTENT gaps, then edits documents in-place |
| `$audit-output` | Checks compliance against templates (no source reading), then edits documents in-place |

**DO NOT** confuse these. This phase uses `$quality-control` which:
- Re-reads the original 10K synthesis memos
- Finds missing content that exists in sources
- Surgically edits the output document(s) to fill gaps — does NOT save a separate report file

---

## Your Task

Run the quality-control skill on the business economics analysis to identify and fix content gaps.

**Step 1: Invoke the quality-control skill**
```
$quality-control analyze-business-economics "[COMPANY]"
```

**Step 2: Provide source document path**

The QC skill will need to re-read the source document. The 10K synthesis memo is at:
```
[SOURCE_MEMO_PATH]
```

Read this memo from the workspace to extract facts for comparison.

**Step 3: Monitor the QC process**

The skill will:
1. Re-read the 10K synthesis memo from the workspace
2. Compare extracted content vs. what's in the analysis
3. Identify gaps (missing quirks, unsourced figures, thin analysis)
4. Surgically edit the analysis to fill gaps

---

## Quality Focus Areas for Business Economics

Pay special attention to these business-economics-specific issues:

### Owner's Earnings Accuracy

| Check | What to Verify |
|-------|----------------|
| Dollar amounts sourced | Every $ in Owner's Earnings traces to 10K memo OR marked [EST] |
| Fiscal year consistency | All figures from same FY (not mixing FY2024 + FY2025) |
| Quirk mapping complete | Every Section 3 quirk appears in Section 8 mapping table |
| Calculation consistency | Figures match what's stated in quirk descriptions |

### Quirk Quality

| Check | What to Verify |
|-------|----------------|
| GAAP specificity | Each quirk references specific GAAP treatment or line item |
| Example sourced | Each quirk has specific example from 10K |
| Adjustment actionable | Each quirk has clear "how to adjust" guidance |
| Completeness | All major accounting quirks from 10K captured |

### Benchmark Quality

| Check | What to Verify |
|-------|----------------|
| Two-sided thresholds | Each benchmark has good AND concern thresholds |
| Quantified | No qualitative benchmarks ("higher is better") |
| Sourced or estimated | Industry benchmarks marked if estimated |
| Company-specific | Benchmarks relevant to this specific company |

### Source Alignment

| Check | What to Verify |
|-------|----------------|
| Business model accurate | Primary classification matches 10K description |
| Cash sources identified | Primary cash source matches 10K revenue breakdown |
| Segment coverage | All major segments from 10K addressed |
| No fabrication | No claims not supported by 10K memos |

### Industry-Specific Completeness (If Checklist Loaded)

If an industry checklist was used (industry is not "none"), read the checklist and verify:

| Check | What to Verify |
|-------|----------------|
| Required metrics present | All metrics marked "REQUIRED" in checklist appear in Section 4 |
| Required quirks documented | All quirks listed under "Required Quirks" appear in Section 3 |
| Valuation method appropriate | Primary valuation method follows checklist guidance (e.g., P/B for insurance) |
| Benchmarks match industry | Metric benchmarks align with checklist ranges |
| Red/Green flags considered | Industry-specific warning signs addressed |

**For Insurance Companies:**
- Combined Ratio, Loss Ratio, Expense Ratio all present?
- Investment Yield calculated (NII / Avg Invested Assets)?
- ROE vs. Cost of Equity spread analyzed?
- Reserve development (PYD) trends documented?
- P/B used as primary valuation method (not P/E)?

---

## Gap Classification

Gaps should be classified as:

| Classification | Definition | Examples |
|---------------|------------|----------|
| **CRITICAL** | Undermines the analysis | Owner's Earnings wrong, major quirk missing, wrong business model |
| **HIGH** | Reduces usefulness | Missing source citation, benchmark missing concern threshold |
| **MINOR** | Nice-to-have enhancement | Additional supporting data, formatting improvements |

Focus on CRITICAL and HIGH gaps. MINOR gaps can be noted but don't require fixes.

---

## Re-Reading Source Document

The 10K synthesis memo contains the extracted accounting policies and business descriptions.

From the source memo, extract:
- Accounting policies and GAAP treatments mentioned
- Dollar figures (revenue, expenses, cash flows)
- Business segment descriptions
- Management's discussed metrics
- Unusual items or one-time charges

Compare these extractions against the analysis to identify:
- Missing quirks that should be documented
- Figures that don't match source
- Segments or aspects not covered

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
- If the QC skill identifies issues it cannot fix (need source verification), note them in the return value
- Maximum 3 iteration loops within the QC skill
```
