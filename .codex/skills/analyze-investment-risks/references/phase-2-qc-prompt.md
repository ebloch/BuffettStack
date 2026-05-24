# Phase 2: Quality Control Prompt

Use this reference for the QC pass for analyze-investment-risks.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing quality control on a Risk Analysis.

**Context:**
- Company: [COMPANY]
- Analysis Path: [MEMO_PATH]

**Source Documents (for re-reading):**
- 10K Synthesis Memos: [10K_MEMO_PATHS]
- Moat Analysis (Scuttlebutt / Competitive Landscape / Moat Strength): [MOAT_ANALYSIS_PATHS]
- Management Credibility Audit: [MANAGEMENT_AUDIT_PATH]

---

## CRITICAL: Skill Distinction

**You are running `$quality-control`, NOT `$audit-output`.** These are different skills:

| Skill | What It Does |
|-------|-------------|
| `$quality-control` | Re-reads source docs to find CONTENT gaps, then edits documents in-place |
| `$audit-output` | Checks compliance against templates (no source reading), then edits documents in-place |

**DO NOT** confuse these. This phase uses `$quality-control` which:
- Re-reads the original research documents
- Finds missing content that exists in sources but was omitted from the analysis
- Surgically edits the output document(s) to fill gaps — does NOT save a separate report file

---

## Your Task

Run the quality-control skill on the Risk Analysis to identify and fix content gaps.

**Step 1: Invoke the quality-control skill**
```
$quality-control analyze-investment-risks "[COMPANY]"
```

**Step 2: Provide source document paths**

The QC skill needs to re-read source documents. The prerequisite research files are:
```
10K Synthesis Memos: [10K_MEMO_PATHS]
Moat Analysis: [MOAT_ANALYSIS_PATHS]
Management Credibility Audit: [MANAGEMENT_AUDIT_PATH]
```

Read each available source document from the workspace to extract facts for comparison.

**Step 3: Monitor the QC process**

The skill will:
1. Re-read source documents from the workspace
2. Compare source content vs. what's in the risk analysis
3. Identify gaps (missing risk factors, thin analysis, unsourced claims)
4. Surgically edit the analysis to fill gaps

---

## Quality Focus Areas for Risk Analysis

Pay special attention to these risk-specific issues:

### Risk Factor Coverage

| Check | What to Verify |
|-------|----------------|
| 10K risk factors reflected | All material risk factors from 10K memos appear in appropriate risk categories |
| Competitive risks from moat analysis | Moat vulnerabilities and competitive threats reflected in Category 2 (Competitive) and Category 1 (Business Model) |
| Management concerns reflected | Management audit findings reflected in Category 4 (Operational — execution risk, key person) |
| No major omissions | Compare company-disclosed risks in 10K vs. risks in the analysis |

### Severity Math

| Check | What to Verify |
|-------|----------------|
| P × I = Severity | Every risk in the matrix has correct multiplication |
| Severity capped at 10 | No severity score exceeds 10, even if P(3) × I(4) = 12 |
| Probability values valid | Low=1, Medium=2, High=3 only |
| Impact values valid | Low=1, Medium=2, High=3, Very High=4 only |

### Mitigant Quality

| Check | What to Verify |
|-------|----------------|
| Specific mitigants | Each mitigant identifies a concrete defense (not "management awareness") |
| Source-backed | Mitigants reference actual company capabilities from 10K or moat analysis |
| Honest residual risk | Risks without real mitigants state "None identified — residual risk" |

### Top 5 Ranking

| Check | What to Verify |
|-------|----------------|
| Matches severity scores | Top 5 order matches severity scores from risk matrix |
| Financial impact present | Each of the 5 has a quantified revenue/earnings impact estimate |
| Impact is specific | Not "significant impact" but "5-10% revenue decline" or "$500M at risk" |

### Thesis Killer Specificity

| Check | What to Verify |
|-------|----------------|
| Observable triggers | Each thesis killer is an observable event (not "things get worse") |
| Actionable | Investor knows when to sell |
| Timeframes present | Each has Immediate / 1-2 quarters / 1+ year |
| 3-5 count | Not fewer than 3, not more than 5 |

### Dashboard Current Values

| Check | What to Verify |
|-------|----------------|
| No placeholders | No "TBD", "[X]", "[Current Value]", "N/A" |
| Actual numbers | Specific values like "45%", "1.2x", "$3.4B" |
| Warning levels specific | Specific thresholds like "<1.5x", ">25%" (not "declining" or "worsening") |
| At least 5 metrics | Dashboard has 5+ rows |

### Downside Probability Constraints

| Check | What to Verify |
|-------|----------------|
| Range valid | Each probability between 5% and 40% |
| Sum constraint | All scenario probabilities sum to less than 100% |
| Methodology stated | Probability derivation method described at top of section |
| Justifications present | Each probability has a brief justification |

### Source Alignment

| Check | What to Verify |
|-------|----------------|
| Competitive risks reflect moat analysis | Threats from moat/competitive analysis appear in risk categories |
| Management risks reflect audit | Management credibility concerns appear in operational or governance risks |
| 10K risks captured | Company-disclosed risk factors from 10K are covered |
| No contradictions | Risk assessment doesn't contradict findings from source documents |

### Risk Correlations

| Check | What to Verify |
|-------|----------------|
| Section present | Risk Correlations section exists |
| At least one cluster | At least one correlated risk cluster identified |
| Cascade scenario described | How one risk triggers another |
| Combined severity estimated | Impact if risks materialize together |

### Overall Risk Level Format

| Check | What to Verify |
|-------|----------------|
| Standard format | Exactly one of: LOW / MODERATE / HIGH / VERY HIGH |
| No hybrids | Not "MODERATE-HIGH" or "Moderate to High" |
| Consistent with body | Level reflects the risks described in the analysis |

---

## Gap Classification

Gaps should be classified as:

| Classification | Definition | Examples |
|---------------|------------|----------|
| **CRITICAL** | Missing risk categories, severity math wrong, thesis killers vague/missing timeframes, Top 5 missing financial impact | Core structural failures |
| **HIGH** | Dashboard placeholders, moat vulnerabilities not reflected, management concerns missing from risks, risk correlations absent | Important content gaps |
| **MINOR** | Additional risks, formatting, extra context, minor evidence gaps | Nice-to-have improvements |

Focus on CRITICAL and HIGH gaps. MINOR gaps can be noted but don't require fixes.

---

## Re-Reading Source Documents

From the source documents, extract and compare:

### From 10K Synthesis Memos
- Company-disclosed risk factors — are ALL material ones reflected in the risk categories?
- Business model vulnerabilities — captured in Category 1 (Business Model)?
- Financial concerns and accounting notes — captured in Category 3 (Financial)?
- Customer concentration data — captured in Category 4 (Operational)?
- Regulatory disclosures — captured in Category 5 (Regulatory)?
- Industry-specific risks — distributed across appropriate categories?

### From Moat Analysis (Scuttlebutt / Competitive / Moat Strength)
- Competitive threats — reflected in Category 2 (Competitive)?
- Moat vulnerabilities — reflected in thesis killers and risk matrix?
- Disruption risk assessment — captured in Category 1 (Business Model)?
- Customer sentiment concerns — reflected in appropriate risk categories?
- Industry dynamics and competitive positioning — consistent with competitive risk assessment?

### From Management Credibility Audit
- Promise vs. delivery gaps — reflected in Category 4 (Operational — execution risk)?
- Capital allocation concerns — reflected in Category 3 (Financial) or Category 4 (Operational)?
- Management transparency issues — reflected in Category 7 (ESG/Reputational — governance)?
- Key person risk — captured in Category 4 (Operational)?
- Red flags — captured in thesis killers where appropriate?

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
- Re-read source documents to find evidence gaps — this is what distinguishes QC from audit
- If the QC skill identifies issues it cannot fix (need deeper analysis), note them in the return value
- Maximum 3 iteration loops within the QC skill
```
