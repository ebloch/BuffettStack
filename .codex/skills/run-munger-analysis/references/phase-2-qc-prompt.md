# Phase 2: Quality Control Prompt

Use this reference for the QC pass for run-munger-analysis.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing quality control on a Munger Analysis.

**Context:**
- Company: [COMPANY]
- Analysis Path: [MEMO_PATH]

**Source Documents (for re-reading):**
- Business Overview: [BUSINESS_OVERVIEW_PATH]
- Financial Statements: [FINANCIAL_STATEMENTS_PATH]
- Management Audit: [MANAGEMENT_AUDIT_PATH]
- Scuttlebutt: [SCUTTLEBUTT_PATH] (or "N/A" if none)
- Competitive Landscape: [COMPETITIVE_LANDSCAPE_PATH] (or "N/A" if none)
- Moat Strength: [MOAT_STRENGTH_PATH] (or "N/A" if none)
- Risk Assessment: [RISK_ASSESSMENT_PATH] (or "N/A" if none)

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

Run the quality-control skill on the Munger Analysis to identify and fix content gaps.

**Step 1: Invoke the quality-control skill**
```
$quality-control run-munger-analysis "[COMPANY]"
```

**Step 2: Provide source document paths**

The QC skill needs to re-read source documents. The prerequisite research files are:
```
Business Overview: [BUSINESS_OVERVIEW_PATH]
Financial Statements: [FINANCIAL_STATEMENTS_PATH]
Management Audit: [MANAGEMENT_AUDIT_PATH]
Scuttlebutt: [SCUTTLEBUTT_PATH]
Competitive Landscape: [COMPETITIVE_LANDSCAPE_PATH]
Moat Strength: [MOAT_STRENGTH_PATH]
Risk Assessment: [RISK_ASSESSMENT_PATH]
```

Read each available source document from the workspace to extract facts for comparison.

**Step 3: Monitor the QC process**

The skill will:
1. Re-read source documents from the workspace
2. Compare source content vs. what's in the Munger memo
3. Identify gaps (missing evidence, thin analysis, unsourced claims)
4. Surgically edit the analysis to fill gaps

---

## Quality Focus Areas for Munger Analysis

Pay special attention to these Munger-specific issues:

### Cross-Reference Discipline

| Check | What to Verify |
|-------|----------------|
| Stage 1 → Stage 2 flags | Were ALL Stage 1 flags validated/challenged in Stage 2? |
| Stage 2 → Stage 3 flags | Were ALL Stage 2 flags validated/challenged in Stage 3? |
| No skipped flags | Every flag has ✓ Validated or ✗ Challenged — no "TBD" or blank |
| Challenge explanations | If ✗ Challenged, does new evidence explain why? |

### Scoring Rigor

| Check | What to Verify |
|-------|----------------|
| +2 gate enforcement | Every +2 score has "Why Not Higher?" = "N/A" — no exceptions |
| +2 with concerns | If "Why Not Higher?" has substantive content, score should be +1 max |
| No +2 for single-source moats | WIDE & WIDENING requires multiple reinforcing advantages |
| No +2 for management with gaps | Even 85% delivery rate has misses — verify acknowledged |

### Tensions Handling

| Check | What to Verify |
|-------|----------------|
| Tensions logged | All contradictions between stages appear in Tensions Registry |
| Resolution status | Each tension marked Resolved or Unresolved |
| Unresolved → Adjustment | Unresolved tensions reflected in Holistic Adjustment (-1 or -2) |
| Not ignored | No tensions simply dropped between stages |

### Evidence Sourcing

| Check | What to Verify |
|-------|----------------|
| Score evidence | Each category score backed by specific evidence from source documents |
| No vague assertions | Claims like "strong moat" or "good management" cite specific data |
| Financial metrics sourced | Return on capital, FCF, leverage figures trace to Financial Statements |
| Management claims checked | Credibility scores, say/do ratings trace to Management Audit |
| Moat claims sourced | Moat type/direction backed by Scuttlebutt, Competitive, or Moat research |

### Stage Isolation

| Check | What to Verify |
|-------|----------------|
| Stage 1 scope | Did NOT reference Management Audit or competitive documents |
| Stage 2 scope | Did NOT reference Scuttlebutt, Competitive, Moat, or Risk documents |
| Stage 3 scope | Read all available competitive documents + Working Analysis v2 |
| Stage 4 scope | Read ONLY Working Analysis v3 — no new source documents |

### Inversion Discipline

| Check | What to Verify |
|-------|----------------|
| Failure modes | "What would cause failure?" addressed in Circle of Competence |
| Predictability risks | "What could go wrong?" has 5 specific risks |
| Risk integration | Risk Assessment findings reflected in scoring |
| Downside honesty | Concerns are specific and substantive, not perfunctory |

---

## Gap Classification

Gaps should be classified as:

| Classification | Definition | Examples |
|---------------|------------|----------|
| **CRITICAL** | +2 score with unaddressed concern, missing cross-reference validation, unresolved tension not in Holistic Adjustment | Score inflation, skipped flags, dropped tensions |
| **HIGH** | Thin evidence for major score, management claims not checked against audit, moat claims without competitive evidence | Unsourced claims, single-evidence scores |
| **MINOR** | Additional supporting data, formatting, minor evidence gaps | Extra context, presentation issues |

Focus on CRITICAL and HIGH gaps. MINOR gaps can be noted but don't require fixes.

---

## Re-Reading Source Documents

From the source documents, extract and compare:

### From Business Overview
- Business model description — does Circle of Competence section accurately reflect it?
- Key economic drivers — are they correctly identified and ranked?
- Multi-year trajectory — is it reflected in Long-Term Orientation?

### From Financial Statements
- Return on capital metrics — do figures in Financial Strength match source?
- FCF trends — are they accurately captured?
- Balance sheet metrics — leverage, coverage ratios match?

### From Management Audit
- Credibility scores and delivery rates — do they match what's cited?
- Say/do quadrant placement — is it accurate?
- Capital allocation track record — management claims vs. audit findings?

### From Scuttlebutt / Competitive / Moat
- Customer perspective — is it reflected in moat assessment?
- Competitive dynamics — market share, competitor threats captured?
- Moat type and direction — supported by evidence from these sources?

### From Risk Assessment
- Key risks — are they in "What Could Go Wrong?" section?
- Thesis killers — reflected in scoring and Holistic Adjustment?
- Risk severity — does it match how risks are weighted in the analysis?

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
