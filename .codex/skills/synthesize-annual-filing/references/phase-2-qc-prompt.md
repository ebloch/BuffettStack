# Phase 2: Quality Control Prompt

Use this prompt to invoke `$quality-control` from `$synthesize-annual-filing`.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing quality control on an annual filing synthesis memo.

**Context:**
- Company: [COMPANY] ([TICKER])
- Fiscal Year: [YEAR]
- Memo Path: [MEMO_PATH]
- Industry: [INDUSTRY]
- Parsing Mode: [PARSING_MODE] (sec = EDGAR, pdf = PDF file)
- PDF Source: [PDF_SOURCE] (only when PARSING_MODE=pdf)

---

## CRITICAL: Pass Distinction

**You are running the quality-control pass, NOT the audit pass.** These are different checks:

| Skill | What It Does |
|-------|-------------|
| Quality control | Re-reads source docs (annual filing) to find CONTENT gaps, then edits documents in-place |
| Audit | Checks compliance against templates (no source reading), then edits documents in-place |

**DO NOT** confuse these. This phase:
- Re-reads the original annual filing
- Finds missing content that exists in sources
- Surgically edits the output document(s) to fill gaps — does NOT save a separate report file

---

## Your Task

Invoke `$quality-control` on the synthesis memo to identify and fix content gaps.

**Process**
1. Call `$quality-control synthesize-annual-filing "[COMPANY]" FY[YEAR]`.
2. The helper will locate the memo and extract ticker/year/parser metadata from its YAML frontmatter and source section.
3. The helper will re-read the original filing:
   - SEC filing: `python3 scripts/parse_annual_filing.py [TICKER] --year [YEAR]`
   - PDF filing: `python3 scripts/parse_pdf_filing.py [PDF_SOURCE] --json`
4. Compare extracted content vs. what's in the memo.
5. Identify gaps (missing content, thin analysis, unsupported claims).
6. Surgically edit the memo to fill gaps.

## Quality Focus Areas

Pay special attention to:

### Content Completeness
- All required sections present and populated
- Industry-specific metrics captured (per industry checklist)
- Key financial data accurate
- Management quotes with page references

### Source Alignment
- Facts in memo match what's in the 10-K
- No fabricated or hallucinated data
- Appropriate "Not disclosed" vs "Not extracted" language

### Analytical Quality
- Risk Factors include editorial interpretation
- Key Takeaways provide genuine insights (not just restated metrics)
- Questions for Further Research are meaningful

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
- Maximum 3 iteration loops within the QC pass
```
