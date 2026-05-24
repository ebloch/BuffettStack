# Phase 2: Quality Control Prompt

Use this reference for the QC pass for run-fisher-analysis.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing quality control on a Fisher 15-Point Analysis.

**Context:**
- Company: [COMPANY] ([TICKER])
- Analysis Path: [ANALYSIS_PATH]

---

## CRITICAL: Skill Distinction

**You are running `$quality-control`, NOT `$audit-output`.** These are different skills:

| Skill | What It Does |
|-------|-------------|
| `$quality-control` | Re-reads source docs to find CONTENT gaps, then edits documents in-place |
| `$audit-output` | Checks compliance against templates (no source reading), then edits documents in-place |

**DO NOT** confuse these. This phase uses `$quality-control` which:
- Re-reads the prerequisite research files
- Finds missing content that exists in sources
- Surgically edits the output document(s) to fill gaps — does NOT save a separate report file

---

## QC Sources for Fisher Analysis

**Important:** Unlike 10-K synthesis (which re-reads the raw filing), Fisher QC re-reads the **prerequisite research files**. Fisher analysis synthesizes from prior research, not raw filings.

### Source Files to Re-Read

| Folder | Pattern | What to Look For |
|--------|---------|------------------|
| 10K Synthesis | `**/[COMPANY]/1.1-Annual-Filings/*.md` | Business understanding, risk factors, management commentary |
| Financial Statements | `**/[COMPANY]/1.3-Financial-Statements/*.md` | Margins, dilution, share counts, capital allocation |
| Management Audit | `**/[COMPANY]/2.4-Management-Audit/*.md` | Integrity evidence, transparency track record, say/do analysis |
| Scuttlebutt | `**/[COMPANY]/2.2-Scuttlebutt/*.md` | Customer sentiment, employee satisfaction, supplier relationships |
| Competitive Landscape | `**/[COMPANY]/2.3-Competitive-Landscape/*.md` | Market share, competitive position, industry dynamics |
| Moat Strength | `**/[COMPANY]/2.6-Moat-Strength/*.md` | Sustainable advantages, pricing power evidence |
| Risk Assessment | `**/[COMPANY]/2.5-Risk-Assessment/*.md` | Thesis killers, bear case, risk severity |

---

## Your Task

Run the quality-control skill on the Fisher analysis to identify and fix content gaps.

**Step 1: Invoke the quality-control skill**
```
$quality-control run-fisher-analysis "[COMPANY]"
```

**Step 2: Monitor the QC process**
The skill will:
1. Re-read the prerequisite research files (listed above)
2. Compare evidence in research vs. what's cited in Fisher analysis
3. Identify gaps (missing evidence, thin scores, unsupported claims)
4. Surgically edit the analysis to fill gaps

---

## Quality Focus Areas

Pay special attention to:

### Evidence Completeness

For each of the 15 points:
- Does the score have specific, quantified evidence?
- Is the evidence sourced from prerequisite research files?
- Are metrics cited correctly (matching the source files)?

### Source Alignment

- Do facts in the Fisher analysis match what's in the research files?
- Are direct quotes attributed to their source file?
- No fabricated or unsupported claims?

### Coverage of Key Points

| Point | Key Evidence to Verify |
|-------|----------------------|
| 1 (Market Potential) | TAM data, market share, growth rates |
| 5 (Profit Margins) | Specific margin percentages vs. industry |
| 7 (Labor Relations) | Glassdoor rating, turnover data |
| 10 (Cost Controls) | Forecast accuracy, restatement history |
| 13 (Equity Dilution) | Share count trend, SBC as % revenue |
| 14 (Transparency) | Evidence from management audit |
| 15 (Integrity) | Evidence from management audit, any red flags |

### Disqualifier Points (14 & 15)

**Extra scrutiny for Points 14 and 15:**
- Is the management audit file fully leveraged for these scores?
- Does the transparency score reflect actual behavior during bad quarters?
- Does the integrity score account for all known issues?
- If either point is scored -2, is the evidence compelling?

---

## Gap Classification

Gaps should be classified as:
- **CRITICAL:** Missing evidence for a score, or score contradicts available research
- **HIGH:** Important supporting evidence exists but wasn't cited
- **MINOR:** Nice-to-have context that would enhance completeness

Focus on CRITICAL and HIGH gaps. MINOR gaps can be noted but don't require fixes.

---

## Common Fisher QC Issues

| Issue | How to Detect | Fix |
|-------|--------------|-----|
| Score without evidence | Point analysis lacks specific data | Pull evidence from research files |
| Generic assertions | "Management is strong" without specifics | Add tenure, track record, metrics |
| Missing industry context | No peer comparison for margins/metrics | Add industry benchmarks from research |
| Ignoring disqualifiers | -2 on P14/P15 not flagged in verdict | Add explicit warning per Fisher's quote |
| Zero without justification | "0 - average" with no proof | Add evidence showing genuinely average |
| Unused research | Management audit not cited for P14/P15 | Cross-reference and cite |

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

- You have fresh context — no anchoring on the original analysis
- Focus on what's MISSING from the research, not reformatting what exists
- If a gap requires external data (not in existing research files), note it but don't fabricate
- Maximum 3 iteration loops within the QC skill
```
