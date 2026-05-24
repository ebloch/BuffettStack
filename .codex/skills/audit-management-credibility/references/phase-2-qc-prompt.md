# Phase 2: Quality Control Prompt

Use this reference for the QC pass for audit-management-credibility.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing quality control on a Management Credibility Audit.

**Context:**
- Company: [COMPANY] ([TICKER])
- Analysis Path: [ANALYSIS_PATH]
- Memo Path: [MEMO_PATH]
- Transcript Range: [TRANSCRIPT_RANGE]

---

## CRITICAL: Skill Distinction

**You are running `$quality-control`, NOT `$audit-output`.** These are different skills:

| Skill | What It Does |
|-------|-------------|
| `$quality-control` | Re-reads source docs (transcripts) to find CONTENT gaps, then edits documents in-place |
| `$audit-output` | Checks compliance against templates (no source reading), then edits documents in-place |

**DO NOT** confuse these. This phase uses `$quality-control` which:
- Re-reads the original earnings transcripts
- Finds missing content that exists in sources but was omitted from the analysis
- Surgically edits the output document(s) to fill gaps — does NOT save a separate report file

---

## Your Task

Run the quality-control skill on the Management Credibility Audit to identify and fix content gaps.

**Step 1: Invoke the quality-control skill**
```
$quality-control audit-management-credibility "[COMPANY]"
```

**Step 2: Re-read source transcripts**

The QC skill needs to re-read source documents. Re-fetch transcripts using:
```bash
.codex/skills/audit-management-credibility/scripts/fmp-fetch.sh transcripts [TICKER] <START_YEAR> <END_YEAR> /tmp
```

Use the transcript range from Phase 1: [TRANSCRIPT_RANGE]

Read the saved transcript files from `/tmp/{ticker}_q{quarter}_{year}.json` to extract facts for comparison.

**Step 3: Dual-Document QC**

**CRITICAL: This skill produces TWO output documents.** Both must be QC'd:

| Document | Path | What to Check |
|----------|------|---------------|
| **Analysis** | [ANALYSIS_PATH] | Promise extraction, scoring accuracy, data completeness |
| **Memo** | [MEMO_PATH] | Consistency with Analysis, metric accuracy |

**Check Analysis first, then Memo.** The Memo derives from the Analysis, so Analysis gaps propagate.

**Step 4: Monitor the QC process**

The skill will:
1. Re-read earnings transcripts from the workspace
2. Compare transcript content vs. what's in the Analysis
3. Identify gaps (missing promises, thin scoring, unsourced claims)
4. Surgically edit the Analysis AND Memo to fill gaps

---

## Quality Focus Areas for Management Credibility Audit

Pay special attention to these credibility-audit-specific issues:

### Promise Extraction Completeness

| Check | What to Verify |
|-------|----------------|
| All transcripts scanned | Every fetched transcript was reviewed for promises |
| Forward-looking statements captured | Key commitments from prepared remarks AND Q&A extracted |
| Category coverage | All 5 categories have entries (or explicit "none" explanation) |
| Chronological completeness | Promises from early AND recent transcripts are present |
| Promise count reasonable | 5+ years of transcripts should yield 15-40+ scoreable promises |

### Promise Quote Accuracy

| Check | What to Verify |
|-------|----------------|
| Verbatim quotes | Quoted text actually appears in transcript (spot-check 3-5 quotes) |
| Attribution correct | Speaker name and quarter match the transcript source |
| Context preserved | Quote not taken out of context (check surrounding sentences) |
| Specificity rating accurate | "Specific" promises actually contain numbers/dates/targets |

### Scoring Consistency

| Check | What to Verify |
|-------|----------------|
| Scale applied correctly | +2 to -2 scale used consistently across all categories |
| External factors fairly weighted | External disruptions scored 0, not +1 |
| Missed promises documented | ALL scores <=0 appear in Missed & Partial Promises section |
| Hit rate math correct | Hit rate = (scores >= +1) / total scored promises |
| Composite score math correct | Composite = average of all individual promise scores |

### Quantitative Scorecard Accuracy

| Check | What to Verify |
|-------|----------------|
| Table 1 totals correct | Category rows sum to Total row |
| Table 2 year coverage | Each year in audit period has a row |
| Table 3 guidance rows | All guided metrics represented (or "Not Provided" explanation) |
| Trend statement supported | Trend direction matches year-over-year data |
| Guidance style matches data | Style label consistent with beat/met/missed ratios |

### Capital Allocation Data

| Check | What to Verify |
|-------|----------------|
| M&A deals captured | All acquisitions during audit period tracked |
| Synergy promises quoted | Each deal has specific promise with source quote |
| Buyback data sourced | Annual buyback amounts and prices from 10-K or press releases |
| Other allocations complete | Dividends, capex, divestitures documented where relevant |
| Capital allocation rating supported | Rating matches evidence in tables |

### Insider Ownership & Compensation

| Check | What to Verify |
|-------|----------------|
| Executive count | Minimum 3 executives (CEO, CFO, +1) or explicit explanation |
| Proxy source cited | DEF 14A with page numbers (not aggregator sites) |
| Salary included | Base salary present for each executive |
| Compensation breakdown sums | % breakdown components sum close to 100% |
| Pay vs. performance comparison | All 3 growth rates present (pay, stock, EPS) |
| Alignment score math | Factor scores sum to overall alignment |

### Cross-Document Consistency

| Check | What to Verify |
|-------|----------------|
| Rating matches | Credibility Rating identical in Analysis and Memo |
| Matrix placement matches | Say/Do Matrix quadrant name identical in both |
| Hit rate matches | Promise Hit Rate identical in both |
| Composite score matches | Composite Score identical in both |
| Quick Reference accurate | All 5 Memo metrics match corresponding Analysis figures |
| Red flags consistent | If Analysis says "unresolved," Memo doesn't say "completed" |

---

## Gap Classification

Gaps should be classified as:

| Classification | Definition | Examples |
|---------------|------------|----------|
| **CRITICAL** | Undermines the audit | Missing promise categories, wrong scoring math, fabricated quotes, cross-document contradictions |
| **HIGH** | Reduces usefulness | Missing key promises from transcripts, thin capital allocation section, missing proxy source, incomplete scorecard tables |
| **MINOR** | Nice-to-have enhancement | Additional quotes, formatting improvements, extra context on individual promises |

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
- Re-read transcripts to find missed promises — this is what distinguishes QC from audit
- Both Analysis AND Memo must be checked for consistency
- If the QC skill identifies issues it cannot fix (need source verification), note them in the return value
- Maximum 3 iteration loops within the QC skill
```
