# Phase 2: Quality Control Prompt

Use this reference for the QC pass for company-overview.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing quality control on a Business Overview memo.

**Context:**
- Company: [COMPANY]
- Memo Path: [MEMO_PATH]

---

## CRITICAL: Skill Distinction

**You are running `$quality-control`, NOT `$audit-output`.** These are different skills:

| Skill | What It Does |
|-------|-------------|
| `$quality-control` | Re-reads source docs (Foundation memos) to find CONTENT gaps, then edits documents in-place |
| `$audit-output` | Checks compliance against templates (no source reading), then edits documents in-place |

**DO NOT** confuse these. This phase uses `$quality-control` which:
- Re-reads the original Foundation materials (10-K memos, investor presentations, financial data)
- Finds missing content that exists in sources
- Surgically edits the output document(s) to fill gaps — does NOT save a separate report file

---

## Your Task

Run the quality-control skill on the Business Overview memo to identify and fix content gaps.

**Step 1: Invoke the quality-control skill**
```
$quality-control company-overview "[COMPANY]"
```

**Step 2: Monitor the QC process**
The skill will:
1. Re-read the Foundation materials (10-K memos, investor presentations, financial data)
2. Compare extracted content vs. what's in the memo
3. Identify gaps (missing content, thin analysis, unsupported claims)
4. Surgically edit the memo to fill gaps

## Quality Focus Areas

Pay special attention to:

### Content Completeness
- All required sections present and populated
- Key Takeaways are cross-year synthesis (not point-in-time facts)
- Financial Evolution table with correct CAGR calculations
- Management Credibility Scorecard with trackable promises
- Risk Evolution Matrix with trend arrows

### Source Alignment
- Facts in memo match what's in the Foundation memos
- No fabricated or hallucinated data
- All insights traceable to source materials

### Analytical Quality
- Key Takeaways provide genuine insights (not just restated metrics)
- Business description explains the economic engine
- Risk matrix shows evolution across years (not just current state)
- Questions for Monitoring are specific and investment-relevant

## Gap Classification

Gaps should be classified as:
- **CRITICAL:** Missing core content that undermines the analysis
- **HIGH:** Important content gap that reduces usefulness
- **MINOR:** Nice-to-have content that would enhance completeness

Focus on CRITICAL and HIGH gaps. MINOR gaps can be noted but don't require fixes.

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

## Important Notes

- You have fresh context — no anchoring on the original synthesis
- Focus on what's MISSING, not reformatting what exists
- If the QC skill identifies issues it cannot fix (need source verification), note them in the return value
- Maximum 3 iteration loops within the QC skill
```
