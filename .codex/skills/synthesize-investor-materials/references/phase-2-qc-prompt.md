# Phase 2: Quality Control Prompt

Use this reference for the QC pass for synthesize-investor-materials.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing quality control on an investor materials synthesis memo.

**Context:**
- Company: [COMPANY]
- Event Name: [EVENT_NAME]
- Memo Path: [MEMO_PATH]
- Event Type: [EVENT_TYPE]

**Source PDFs (for re-reading):**
[PDF_PATHS]

---

## CRITICAL: Skill Distinction

**You are running `$quality-control`, NOT `$audit-output`.** These are different skills:

| Skill | What It Does |
|-------|-------------|
| `$quality-control` | Re-reads source docs (PDFs) to find CONTENT gaps, then edits documents in-place |
| `$audit-output` | Checks compliance against templates (no source reading), then edits documents in-place |

**DO NOT** confuse these. This phase uses `$quality-control` which:
- Re-reads the original source PDFs
- Finds missing content that exists in sources
- Surgically edits the output document(s) to fill gaps — does NOT save a separate report file

---

## Your Task

Run the quality-control skill on the synthesis memo to identify and fix content gaps.

**Step 1: Invoke the quality-control skill**
```
$quality-control synthesize-investor-materials "[COMPANY]" "[EVENT_NAME]"
```

**Step 2: Provide source document paths**

The QC skill will need to re-read source documents. Pass the PDF paths:
```
[PDF_PATHS]
```

PDFs should be read directly from the workspace (they were downloaded to `/tmp` during Phase 1).

**Step 3: Monitor the QC process**

The skill will:
1. Re-read the source PDFs from the workspace
2. Compare extracted content vs. what's in the memo
3. Identify gaps (missing content, thin analysis, unsupported claims)
4. Surgically edit the memo to fill gaps

---

## Quality Focus Areas

Pay special attention to:

### Content Completeness

- All required sections present and populated
- Event-type checklist items captured (per event-type checklist)
- Key financial data accurate
- Management quotes with slide references

### Source Alignment

- Facts in memo match what's in the source PDFs
- No fabricated or hallucinated data
- Verbatim quotes are actually verbatim

### Promise & Claim Extraction

- Minimum 3 promises with verbatim quotes and slide references
- Claims include verifiability ratings
- No paraphrased "upgrades" of management language

### Analytical Quality

- Key Takeaways provide genuine insights (not just restated facts)
- Red Flags section addresses real concerns
- Investment Implications are actionable

---

## Gap Classification

Gaps should be classified as:
- **CRITICAL:** Missing core content that undermines the analysis
- **HIGH:** Important content gap that reduces usefulness
- **MINOR:** Nice-to-have content that would enhance completeness

Focus on CRITICAL and HIGH gaps. MINOR gaps can be noted but don't require fixes.

---

## Re-Reading Source Documents

The PDFs were downloaded to `/tmp` during Phase 1. Read them from the workspace:

```
Read: /tmp/[company]-[event]-[desc].pdf
```

Compare key claims, promises, and guidance between source PDFs and memo.

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
- Focus on what's MISSING, not reformatting what exists
- If the QC skill identifies issues it cannot fix (need source verification), note them in the return value
- Maximum 3 iteration loops within the QC skill
```
