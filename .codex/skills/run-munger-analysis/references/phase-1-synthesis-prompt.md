# Phase 1: Munger Analysis Synthesis Prompt

Use this reference for the synthesis pass for run-munger-analysis.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are creating a Munger Analysis for [COMPANY].

**Timestamp:** [TIMESTAMP]
**Output Directory:** [OUTPUT_DIR]

**Source Documents:**
- Business Overview: [BUSINESS_OVERVIEW_PATH]
- Financial Statements: [FINANCIAL_STATEMENTS_PATH]
- Management Audit: [MANAGEMENT_AUDIT_PATH]
- Scuttlebutt: [SCUTTLEBUTT_PATH] (or "N/A" if none)
- Competitive Landscape: [COMPETITIVE_LANDSCAPE_PATH] (or "N/A" if none)
- Moat Strength: [MOAT_STRENGTH_PATH] (or "N/A" if none)
- Risk Assessment: [RISK_ASSESSMENT_PATH] (or "N/A" if none)

---

## Your Task

Complete the full Munger Analysis using a 4-stage sequential process. Each stage reads specific documents, builds on the prior stage's Working Analysis, and passes cross-reference flags forward.

**CRITICAL:** Maintain strict stage isolation — each stage reads ONLY its designated documents plus the prior Working Analysis. Do NOT read ahead.

### Stage 1: Business Foundation

Read the stage instructions:
```
.codex/skills/run-munger-analysis/references/stage-1-business-foundation.md
```

Read these documents:
1. **Business Overview** — [BUSINESS_OVERVIEW_PATH]
2. **Financial Statements** — [FINANCIAL_STATEMENTS_PATH]

Assess:
- **Circle of Competence (Full):** Business understanding, key drivers, failure modes
- **Financial Strength (Full):** Balance sheet, returns, FCF
- **Predictability (Partial):** Financial stability factors only

Read the working analysis template:
```
.codex/skills/run-munger-analysis/references/working-analysis-template.md
```

Output Working Analysis v1 in a code block following the v1 template. Include 2-4 cross-reference flags for Stage 2.

---

### Stage 2: Management & Execution

Read the stage instructions:
```
.codex/skills/run-munger-analysis/references/stage-2-management.md
```

Read these documents:
1. **Management Credibility Audit** — [MANAGEMENT_AUDIT_PATH]
2. **Working Analysis v1** — From the code block you wrote above

**CRITICAL:** Before assessing management, address EACH flag from Working Analysis v1's "Cross-Reference Flags for Stage 2" section. Mark each as ✓ Validated or ✗ Challenged with evidence.

Assess:
- **Quality of Management (Full):** Say/do, alignment, capital allocation
- **Predictability (Refinement):** Add execution track record
- **Long-Term Orientation (Partial):** Management time horizon

Output Working Analysis v2 in a code block following the v2 template. Include 2-4 cross-reference flags for Stage 3.

---

### Stage 3: Competitive Position

Read the stage instructions:
```
.codex/skills/run-munger-analysis/references/stage-3-competitive-position.md
```

Read ALL that exist:
1. **Scuttlebutt** — [SCUTTLEBUTT_PATH]
2. **Competitive Landscape** — [COMPETITIVE_LANDSCAPE_PATH]
3. **Moat Strength** — [MOAT_STRENGTH_PATH]
4. **Risk Assessment** — [RISK_ASSESSMENT_PATH]
5. **Working Analysis v2** — From the code block above

**CRITICAL:** Before assessing moat, address EACH flag from Working Analysis v2's "Cross-Reference Flags for Stage 3" section. Mark each as ✓ Validated or ✗ Challenged with evidence.

Assess:
- **Moat & Competitive Advantage (Full):** Type, durability, direction
- **Predictability (Final):** Add disruption/competitive risks
- **Long-Term Orientation (Final):** Tailwinds/headwinds
- **Lollapalooza Effects (Full):** Combining forces, virtuous cycles

Output Working Analysis v3 in a code block following the v3 template. Include complete scoring summary, tensions registry, and holistic adjustment recommendation.

---

### Stage 4: Final Synthesis

Read the stage instructions:
```
.codex/skills/run-munger-analysis/references/stage-4-final-synthesis.md
```

Read **Working Analysis v3 only** — no new source documents.

Process:
1. **Score Reconciliation:** Gut check each category score
2. **Tension Resolution:** Address each item in tensions registry
3. **Holistic Adjustment:** Apply 0 / -1 / -2 with rationale
4. **Final Score & Verdict:** Calculate and calibrate
5. **Final Gut Check:** Does verdict match intuition?

Read the output template:
```
.codex/skills/run-munger-analysis/references/output-template.md
```

Write the final Munger Analysis memo using the output template.

---

### Step 5: Validate Before Writing

Read the validation checklist:
```
.codex/skills/run-munger-analysis/references/validation-checklist.md
```

Run through ALL validation checks before finalizing. Pay special attention to:
- Every +2 score has "Why Not Higher?" = "N/A"
- Every flag from Stage N is marked ✓ Validated or ✗ Challenged in Stage N+1
- Unresolved tensions reflected in Holistic Adjustment
- Stage isolation maintained (each stage read only its designated documents)
- EXCEPTIONAL verdict requires at least score +9 with clean +2 gate enforcement

### Step 6: Write Output

Save the final memo to:
```
[OUTPUT_DIR]/Munger Analysis - Memo - [COMPANY] - [TIMESTAMP].md
```

---

## File Exclusions

When reading prerequisite files, **exclude meta-documents** matching these patterns:
- `QC Report - *` (quality control reports)
- `Gap Analysis - *` (gap analysis documents)
- `Improvement Suggestions - *` (improvement suggestion memos)
- `Audit Report - *` (audit output reports)

---

## Tool Usage

- **Read:** Use for reading source documents, stage prompts, templates, and checklists
- **Write:** Use for saving the final output memo
- **File search pattern:** Use for finding additional research files if paths change

---

## Return Value

When complete, return a JSON object:
```json
{
  "output_file_path": "[path to written memo]",
  "sources_used": ["list of all source file paths read"],
  "status": "success" | "partial" | "failed",
  "notes": "[any issues encountered]"
}
```

The `sources_used` list is CRITICAL — Phase 2 QC will use these paths to re-read source documents.
```
