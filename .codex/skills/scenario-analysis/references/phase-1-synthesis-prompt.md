# Phase 1: Scenario Analysis Synthesis Prompt

Use this reference for the synthesis pass for scenario-analysis.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are creating a 10-Year Scenario Analysis for [COMPANY] ([TICKER]).

**Source Documents (REQUIRED — read ALL before analyzing):**
- Business Overview: [BUSINESS_OVERVIEW_PATH]
- Management Audit: [MANAGEMENT_AUDIT_PATH]
- Financial Data: [FINANCIAL_DATA_PATHS]
- Moat Analysis: [MOAT_ANALYSIS_PATH]
- Risk Assessment: [RISK_ASSESSMENT_PATH]

**Source Documents (OPTIONAL — read if available):**
- Investor Presentations: [INVESTOR_PRESENTATIONS_PATHS]

**Output Directory:** [OUTPUT_DIR]
**Timestamp:** [TIMESTAMP]

---

## Your Task

Complete the full scenario analysis workflow:

### Step 1: Read ALL Source Documents (REQUIRED FIRST)

Read every source document listed above. This is a SYNTHESIS skill — you are synthesizing existing research into forward-looking scenarios, not conducting new research.

**From Business Overview, extract:**
- Multi-year business trajectory and evolution
- Financial performance trends
- Risk trajectory over time
- Strategic positioning and competitive context

**From Management Audit, extract:**
- Management credibility score and track record
- Capital allocation history
- Promise vs. delivery record
- Key strategic decisions and their outcomes

**From Financial Data, extract:**
- Revenue/earnings growth trends
- Margin trajectory
- Balance sheet health
- Cash flow generation patterns
- Return on capital trends

**From Moat Analysis, extract:**
- Moat type and durability assessment
- Competitive advantage sources
- Moat trajectory (widening, stable, narrowing)
- Key moat risks

**From Risk Assessment, extract:**
- Thesis killers (MUST appear in Scenario 5)
- Key risk factors by category
- Probability and severity assessments
- Mitigating factors

**From Investor Presentations (if available), extract:**
- Management's stated strategy and promises
- Forward guidance and targets
- Strategic initiatives in progress

**File Exclusions:** When reading prerequisite files, SKIP files matching:
- `QC Report - *`
- `Gap Analysis - *`
- `Improvement Suggestions - *`
- `Audit Report - *`

These are process artifacts, not source research.

**CRITICAL:** Every scenario, assumption, and trigger signal must trace back to specific findings from these source documents. This is synthesis, not speculation.

### Step 2: Read Templates

Read required templates:
- Output template: `.codex/skills/scenario-analysis/references/output-template.md`
- Validation checklist: `.codex/skills/scenario-analysis/references/validation-checklist.md`

### Step 3: Identify Key Drivers

Based on the research, identify what will determine outcomes over the next 10 years.

#### Key Uncertainties
What we don't know that will determine outcomes:
- Competitive dynamics (moat durability, new entrants, disruption)
- Growth trajectory (TAM expansion, market share, pricing power)
- Management execution (capital allocation, strategic decisions)
- External factors (regulation, macro, technology shifts)

#### Tailwinds
Forces working in the company's favor:
- Secular trends benefiting the business
- Competitive advantages strengthening
- Industry consolidation, pricing power gains
- Macro/demographic tailwinds

#### Headwinds
Forces working against the company:
- Competitive threats and disruption risks
- Margin pressure, commoditization
- Regulatory or political risks
- Cyclical or macro headwinds

### Step 4: Construct 5 Scenarios

Build scenarios from best to worst:

| # | Scenario | Description |
|---|----------|-------------|
| 1 | **Positive Surprise** | Something goes better than expected, upside case |
| 2 | **Thesis Validated** | Investment thesis plays out as expected, moat holds/strengthens |
| 3 | **Slow Compounding** | Adequate but not exceptional, some competitive pressure |
| 4 | **Stagnation** | Growth stalls, moat erosion begins, multiple compression |
| 5 | **Thesis Broken** | A thesis killer materializes, significant value destruction |

#### For Each Scenario, Write:

1. **Narrative (2-3 paragraphs):** Write a "history from the future" — tell the story of how this scenario unfolds over 10 years. Be specific and vivid. What happens in years 1-3? What inflection points occur? Where does the company end up?

2. **Key Assumptions:** List the 3-5 things that must be true for this scenario to play out. These should be specific and verifiable over time.

3. **Moat Status:** Where does the competitive position end up?
   - Widened — moat stronger than today
   - Stable — moat maintained
   - Eroding — moat weakening but still present
   - Impaired — significant moat damage
   - Gone — no meaningful competitive advantage remains

4. **Trigger Signals:** What are early indicators (within 1-2 years) that this scenario is playing out? These should be observable metrics or events.

**Important:** Keep scenarios qualitative. No financial projections or return calculations. The only numbers should be probability assignments.

### Step 5: Assign Probabilities

Assign probabilities to each scenario based on evidence from your research.

**Rules:**
- Must sum to exactly 100%
- No scenario below 5% (too speculative to be meaningful)
- No scenario above 50% (would dominate as obvious base case)
- Base probabilities on evidence, not optimism or pessimism
- Be intellectually honest — if you're uncertain, let the distribution reflect that

**Guidance:**
- If the company has a wide moat and strong track record, weight toward Scenarios 1-3
- If competitive threats are real, weight toward Scenarios 3-5
- Management credibility affects execution probability across all scenarios
- Recent momentum (positive or negative) can shift near-term probabilities

### Step 6: Complete Validation Checklist

Before writing the output, verify ALL items in the validation checklist (Sections A-H):

- [ ] Exactly 5 scenarios present
- [ ] Probabilities sum to exactly 100%
- [ ] Each probability ≥5% and ≤50%
- [ ] Each scenario has all 4 components (Narrative, Assumptions, Moat Status, Triggers)
- [ ] Moat Status uses valid values only (Widened/Stable/Eroding/Impaired/Gone)
- [ ] Scenario Overview table present with Total = 100%
- [ ] No financial projections in narratives
- [ ] Probability Rationale section present with evidence-based justifications
- [ ] Key Drivers section has Uncertainties, Tailwinds, and Headwinds (3+ items each)
- [ ] Scenario Monitoring section present with quarterly checklist and update triggers
- [ ] All 5 required prerequisites referenced in Sources section
- [ ] Narratives are specific (not generic "competition could increase" language)
- [ ] Assumptions are specific and verifiable
- [ ] Trigger signals are observable within 1-2 years

### Step 7: Write Output

Write the analysis to:
```
[OUTPUT_DIR]/10-Year Scenario Analysis - [COMPANY] - [TIMESTAMP].md
```

---

## Guidelines

**Narratives, Not Numbers:** The value of this skill is in thinking through *how* the future unfolds, not predicting specific financial outcomes. Write rich narratives.

**Specific, Not Generic:** "Competition could increase" is generic. "If Amazon launches a competing exchange with zero fees, leveraging AWS infrastructure..." is specific.

**Intellectually Honest:** If you're genuinely uncertain, let the probability distribution reflect that. A flat distribution (20% each) is honest if warranted.

**Grounded in Research:** Every assumption and scenario should trace back to evidence from the existing research. This is synthesis, not speculation.

**Useful for Monitoring:** Trigger signals should be observable within 1-2 years so the investor can update their view as the future unfolds.

---

## Tool Usage

- **Read:** Use for reading all prerequisite memos, template files, and checklists
- **Write:** Use for saving the output analysis
- **File search pattern:** Use for finding additional research files if needed

---

## Return Value

When complete, return a JSON object:
```json
{
  "output_file_path": "[path to written analysis]",
  "source_paths": {
    "business_overview": "/path/to/overview.md",
    "management_audit": "/path/to/audit.md",
    "financial_data": ["/path/to/fin1.json", "/path/to/fin2.json"],
    "moat_analysis": "/path/to/moat.md",
    "risk_assessment": "/path/to/risk.md",
    "investor_presentations": ["/path/to/pres1.md"]
  },
  "status": "success" | "partial" | "failed",
  "notes": "[any issues encountered]"
}
```

The `source_paths` object is CRITICAL — Phase 2 QC will use these to re-read the source documents.
```
