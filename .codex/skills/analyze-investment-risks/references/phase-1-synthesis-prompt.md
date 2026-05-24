# Phase 1: Risk Analysis Synthesis Prompt

Use this reference for the synthesis pass for analyze-investment-risks.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are creating a comprehensive Risk Analysis for [COMPANY] ([TICKER]).

This answers the questions: **What could go wrong? What are the thesis killers? What should I monitor?**

This is systematic risk identification and assessment — stress-testing the investment thesis by synthesizing company-disclosed risks, competitive vulnerabilities, and management quality concerns.

**Source Documents:**
- 10K Synthesis Memos: [10K_MEMO_PATHS]
- Moat Analysis (Scuttlebutt / Competitive Landscape / Moat Strength): [MOAT_ANALYSIS_PATHS]
- Management Credibility Audit: [MANAGEMENT_AUDIT_PATH]

**Output Directory:** [OUTPUT_DIR]
**Timestamp:** [TIMESTAMP]

---

## Your Task

Complete the full risk analysis workflow:

### Step 1: Read All Source Documents (REQUIRED FIRST)

**Before conducting any web research**, read all existing company research as foundational context.

#### 10K Synthesis Memos
Read ALL 10K synthesis memos provided. These contain:
- Risk factors identified by the company itself
- Business model vulnerabilities management has disclosed
- Financial concerns and accounting notes
- Industry-specific risks
- Customer concentration and dependency data

#### Moat Analysis
Read ALL moat analysis memos provided (scuttlebutt, competitive landscape, moat strength). These contain:
- Competitive landscape and threats
- Moat strength and vulnerabilities
- Scuttlebutt findings (customer/employee/competitor sentiment)
- Disruption risk assessment
- Industry dynamics and competitive positioning

#### Management Audit
Read management credibility audit memos. These contain:
- Promise vs. delivery track record
- Capital allocation history and quality
- Management transparency and candor
- Red flags and integrity concerns

**This existing research is your foundation.** The 10K memos surface risks the company discloses; the Moat Analysis surfaces competitive risks; the Management Audit surfaces execution and integrity risks.

### Step 2: Read Templates

Read required templates:
- Output template: `.codex/skills/analyze-investment-risks/references/output-template.md`
- Validation checklist: `.codex/skills/analyze-investment-risks/references/validation-checklist.md`

### Step 3: Web Research

After reading existing research, conduct targeted web searches to:
- Verify current status of disclosed risks
- Identify new/emerging risks not in older 10Ks
- Research competitor actions and industry developments
- Check for regulatory changes or pending litigation
- Search for recent analyst concerns or downgrades

### Step 4: Generate Analysis

Create the full analysis following the output template structure:

#### Executive Summary

1-2 paragraph summary of key risks.

**Overall Risk Level:** Exactly one of LOW / MODERATE / HIGH / VERY HIGH (no hybrids like "MODERATE-HIGH").

#### Risk Assessment by Category (All 7 Required)

##### 1. Business Model Risks
- What could fundamentally break the business model?
- Technology disruption threats
- Customer behavior changes
- Disintermediation risk
- Product obsolescence
- Dependency on key products/services

##### 2. Competitive Risks
- New entrant threats
- Existing competitor actions
- Price competition / margin compression
- Loss of market share
- Industry overcapacity
- Substitute products

##### 3. Financial Risks
- Balance sheet concerns (leverage, liquidity)
- Debt maturities and refinancing risk
- Pension or off-balance sheet liabilities
- Working capital issues
- Currency exposure
- Interest rate sensitivity
- Earnings quality concerns
- Cash flow sustainability

##### 4. Operational Risks
- Key person risk
- Execution risk on strategic initiatives
- Supply chain vulnerabilities
- Customer concentration
- Supplier concentration
- Labor/talent availability
- Technology/systems risk
- Cybersecurity

##### 5. Regulatory and Political Risks
- Current regulatory threats
- Potential policy changes
- Antitrust concerns
- Environmental/ESG regulations
- Tax changes
- Geopolitical exposure
- Sanctions risk

##### 6. Valuation Risks
- What growth/margins are priced in?
- Sensitivity to multiple compression
- Historical valuation context
- Downside scenarios
- Catalyst dependency

##### 7. ESG and Reputational Risks
- Environmental liabilities
- Social/labor issues
- Governance concerns
- Reputational vulnerabilities
- Litigation exposure

#### Risk Matrix with Scoring Rubric

Include the Scoring Rubric table so readers can verify calculations:

**Probability:**
| Rating | Value | Definition |
|--------|-------|------------|
| Low | 1 | <20% chance of occurring in next 3 years |
| Medium | 2 | 20-50% chance of occurring in next 3 years |
| High | 3 | >50% chance of occurring in next 3 years |

**Impact:**
| Rating | Value | Definition |
|--------|-------|------------|
| Low | 1 | <5% impact on revenue/earnings or minor operational disruption |
| Medium | 2 | 5-15% impact on revenue/earnings or moderate disruption |
| High | 3 | 15-30% impact on revenue/earnings or significant disruption |
| Very High | 4 | >30% impact on revenue/earnings or existential threat |

**Severity = Probability × Impact (capped at 10)**

Then fill the risk matrix table:
| Risk | Category | Probability | Impact | Severity | Mitigant |
|------|----------|-------------|--------|----------|----------|
| [Specific risk] | [Category] | Low/Med/High | Low/Med/High/Very High | [P × I, cap 10] | [Specific mitigant] |

**Mitigant Quality:** Each risk must have a specific mitigant. "Management awareness" is insufficient. If no meaningful mitigant exists, state "None identified — residual risk."

#### Top 5 Risks (Ranked by Severity)

Rank by severity score from the matrix. Each must include a financial impact estimate:
1. **[Risk 1] (Severity: X):** [Description] — *Estimated Impact: [e.g., "5-10% revenue decline" or "$500M-$1B ARR at risk"]*
2. ... through 5

#### Risk Correlations

Identify risks that tend to materialize together:

| Risk Cluster | Risks Involved | Cascade Scenario | Combined Severity |
|--------------|----------------|------------------|-------------------|
| [Name] | Risk A + Risk B | [How one triggers the other] | [Combined severity] |

At least one correlated risk cluster with cascade scenario and combined severity estimate.

**Key Insight:** 1-2 sentences on how risk correlations affect overall portfolio risk.

#### Thesis Killers (3-5)

Specific events that would warrant immediate sale:
1. **[Thesis Killer 1]:** [Why it's fatal] — *Timeframe: [Immediate / 1-2 quarters / 1+ year]*
2. ... through 3-5

Each must be:
- Observable and actionable (not vague like "things get worse")
- Include a timeframe category

#### Monitoring Dashboard (5+ metrics)

| Risk Area | Metric | Current | Warning Level | Check Frequency | Status |
|-----------|--------|---------|---------------|-----------------|--------|
| ... | ... | [actual value] | [specific threshold] | Quarterly/Monthly/etc | G/Y/R |

- Current values must be actual numbers (no "TBD" or "[X]" placeholders)
- Warning levels must be specific thresholds (no "declining" or "worsening")
- At least 5 metrics

#### Downside Scenarios

**Probability Methodology:** State how probabilities are derived.

##### Mild Downside
- **Assumptions:** [Specific]
- **Impact:** [Revenue %, margin %, EPS %, multiple compression, price target]
- **Probability:** X% — *[justification]*

##### Severe Downside
- **Assumptions:** [Specific]
- **Impact:** [Revenue %, margin %, EPS %, multiple compression, price target]
- **Probability:** X% — *[justification]*

##### Catastrophic Downside
- **Assumptions:** [Specific]
- **Impact:** [Revenue %, margin %, EPS %, multiple compression, price target]
- **Probability:** X% — *[justification]*

Constraints: Each probability 5-40%, sum < 100%.

#### Sources

List all source documents used (prerequisite memos + web sources with dates).

### Step 5: Complete Validation Checklist

**MANDATORY:** Run through the validation checklist before writing. Pay special attention to:

- [ ] All 7 risk categories present with substantive analysis
- [ ] Risk matrix severity math correct (P × I = Severity, capped at 10)
- [ ] Scoring rubric included
- [ ] At least 3 thesis killers with timeframes
- [ ] Top 5 risks ranked by severity with financial impact estimates
- [ ] Risk correlations section with at least one cluster
- [ ] Monitoring dashboard has actual current values (no placeholders)
- [ ] Downside scenario probabilities: each 5-40%, sum <100%
- [ ] Overall Risk Level is exactly LOW/MODERATE/HIGH/VERY HIGH
- [ ] Mitigants are specific (not "management awareness")
- [ ] Warning levels are specific thresholds (not "declining")

### Step 6: Write Output

Write analysis to:
```
[OUTPUT_DIR]/Risk Analysis - [COMPANY] - [TIMESTAMP].md
```

---

## Guidelines

**Specific, Not Generic:** "Competition could increase" is generic. "Amazon's entry into X segment with Y capability" is specific.

**Quantify Financial Impact:** For Top 5 risks, estimate the revenue or earnings impact range. Use available data from 10K memos, moat analysis, and web research.

**Quantify Where Possible:** What is the actual probability? What is the dollar impact?

**Balance:** Being thorough about risks doesn't mean being pessimistic. It means being prepared.

**Actionable:** Thesis killers and monitoring points should be concrete enough to act on.

**Connect to Existing Research:** Reference findings from 10K memos, moat analysis, and management audit rather than duplicating their analysis. This risk analysis synthesizes threats identified across all prior research.

---

## Tool Usage

- **Read:** Use for reading source documents, template files, and checklists
- **Write:** Use for saving the output analysis
- **Web search:** Use for regulatory developments, litigation, competitor actions, industry risks
- **File search pattern:** Use for finding additional research files if needed

---

## Return Value

When complete, return a JSON object:
```json
{
  "output_file_path": "[path to written analysis]",
  "sources_used": ["list of all source file paths read"],
  "status": "success" | "partial" | "failed",
  "notes": "[any issues encountered]"
}
```

The `sources_used` list is CRITICAL — Phase 2 QC will use these paths to re-read source documents.
```
