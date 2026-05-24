# Phase 2: Quality Control Prompt

Use this reference for the QC pass for scenario-analysis.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing quality control on a 10-Year Scenario Analysis.

**Context:**
- Company: [COMPANY]
- Analysis Path: [MEMO_PATH]

**Source Documents (for re-reading):**
- Business Overview: [BUSINESS_OVERVIEW_PATH]
- Management Audit: [MANAGEMENT_AUDIT_PATH]
- Financial Data: [FINANCIAL_DATA_PATHS]
- Moat Analysis: [MOAT_ANALYSIS_PATH]
- Risk Assessment: [RISK_ASSESSMENT_PATH]
- Investor Presentations (optional): [INVESTOR_PRESENTATIONS_PATHS]

---

## CRITICAL: Skill Distinction

**You are running `$quality-control`, NOT `$audit-output`.** These are different skills:

| Skill | What It Does |
|-------|-------------|
| `$quality-control` | Re-reads source docs to find CONTENT gaps, then edits documents in-place |
| `$audit-output` | Checks compliance against templates (no source reading), then edits documents in-place |

**DO NOT** confuse these. This phase uses `$quality-control` which:
- Re-reads the original prerequisite research memos
- Finds missing content that exists in sources but didn't make it into the analysis
- Surgically edits the output document(s) to fill gaps — does NOT save a separate report file

---

## Your Task

Run the quality-control skill on the scenario analysis to identify and fix content gaps.

**Step 1: Invoke the quality-control skill**
```
$quality-control scenario-analysis "[COMPANY]"
```

**Step 2: Provide source document paths**

The QC skill will need to re-read the source documents. There are FIVE required source types plus one optional:

**Business Overview:**
```
[BUSINESS_OVERVIEW_PATH]
```

**Management Audit:**
```
[MANAGEMENT_AUDIT_PATH]
```

**Financial Data:**
```
[FINANCIAL_DATA_PATHS]
```

**Moat Analysis:**
```
[MOAT_ANALYSIS_PATH]
```

**Risk Assessment:**
```
[RISK_ASSESSMENT_PATH]
```

**Investor Presentations (optional):**
```
[INVESTOR_PRESENTATIONS_PATHS]
```

Read all source documents from the workspace to extract facts for comparison.

**Step 3: Monitor the QC process**

The skill will:
1. Re-read ALL prerequisite research memos from the workspace
2. Compare extracted content vs. what's in the scenario analysis
3. Identify gaps (missing research findings, ungrounded claims, weak scenarios)
4. Surgically edit the analysis to fill gaps

---

## Quality Focus Areas for Scenario Analysis

Pay special attention to these scenario-analysis-specific issues:

### Research Grounding

| Check | What to Verify |
|-------|----------------|
| Scenarios grounded in research | Each scenario traces to specific findings from prerequisite memos |
| Assumptions sourced | Key assumptions connect to evidence in source documents |
| No unsupported speculation | Claims in narratives have basis in research |
| Source insights utilized | Major findings from each prerequisite appear in relevant scenarios |

### Risk Coverage

| Check | What to Verify |
|-------|----------------|
| Thesis killers in Scenario 5 | All thesis killers from risk assessment appear in the Thesis Broken scenario |
| Key risks reflected | Major risks from 2.5-Risk-Assessment are represented across scenarios |
| Risk severity calibrated | Probability assignments reflect risk severity from source analysis |
| Downside scenarios specific | Stagnation and Thesis Broken scenarios reference actual identified risks |

### Management Calibration

| Check | What to Verify |
|-------|----------------|
| Credibility reflected | Management credibility score from audit influences execution scenarios |
| Track record integrated | Promise vs. delivery record informs scenario narratives |
| Execution probability calibrated | If management audit shows concerns, upside scenarios reflect lower execution probability |
| Capital allocation considered | Capital allocation history from audit informs financial trajectory in scenarios |

### Moat Alignment

| Check | What to Verify |
|-------|----------------|
| Moat status progression logical | Widened → Gone progression across scenarios aligns with moat strength findings |
| Moat type referenced | Specific moat sources from analysis appear in scenario narratives |
| Moat risks addressed | Moat vulnerabilities from analysis appear in downside scenarios |
| Durability assessment consistent | Moat durability rating from source informs probability distribution |

### Tailwind/Headwind Completeness

| Check | What to Verify |
|-------|----------------|
| Major forces captured | Key drivers section reflects major forces from all prerequisite research |
| No orphaned forces | Forces mentioned in prerequisites but absent from Key Drivers section |
| Balance of perspectives | Both positive and negative forces from research represented |
| Specificity matches sources | Drivers are as specific as the underlying research, not genericized |

### Source Completeness

| Check | What to Verify |
|-------|----------------|
| All 5 required types referenced | Business Overview, Management Audit, Financial Data, Moat Analysis, Risk Assessment in Sources |
| Specific files cited | Sources section lists actual file names, not generic descriptions |
| Balanced sourcing | Analysis draws from all prerequisites, not just 1-2 |
| Optional sources noted | If investor presentations were available and read, they appear in Sources |

---

## Gap Classification

Gaps should be classified as:

| Classification | Definition | Examples |
|---------------|------------|----------|
| **CRITICAL** | Undermines the analysis | Scenario ignores a thesis killer from risk assessment, moat status contradicts moat analysis, probabilities not grounded in evidence |
| **HIGH** | Reduces usefulness | Missing key risk from risk assessment, management execution assumed despite audit concerns, generic narratives not tied to research |
| **MINOR** | Nice-to-have enhancement | Additional detail from a source, supplementary trigger signals, formatting improvements |

Focus on CRITICAL and HIGH gaps. MINOR gaps can be noted but don't require fixes.

---

## Re-Reading Source Documents

### From Business Overview, extract:
- Multi-year business trajectory and key inflection points
- Financial evolution and growth patterns
- Risk trajectory over time
- Strategic positioning shifts

### From Management Audit, extract:
- Credibility score and assessment
- Key promises made vs. delivered
- Capital allocation track record
- Strategic decision quality

### From Financial Data, extract:
- Growth rate trends
- Margin trajectory
- Balance sheet health indicators
- Cash flow patterns

### From Moat Analysis, extract:
- Moat type and sources
- Durability assessment
- Key moat risks
- Competitive position trajectory

### From Risk Assessment, extract:
- Thesis killers (ALL must appear in Scenario 5)
- Risk factor categories and ratings
- Probability and severity assessments
- Mitigating factors

### From Investor Presentations (if available), extract:
- Management targets and guidance
- Strategic initiatives
- Market opportunity claims

Compare these extractions against the analysis to identify:
- Research findings not reflected in any scenario
- Thesis killers missing from Scenario 5
- Management credibility not calibrating execution scenarios
- Moat findings not informing moat status assignments
- Key risks absent from downside scenarios

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
- If the QC skill identifies issues it cannot fix (need analytical judgment), note them in the return value
- Maximum 3 iteration loops within the QC skill
```
