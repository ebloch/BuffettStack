# Validation Checklist: analyze-investment-risks

Use this checklist to verify output completeness before finalizing the Risk Analysis.

---

## SECTION A: Critical Validation (Check First)

These items MUST pass before the analysis is complete. If any fail, fix before outputting.

- [ ] **All 7 risk categories present** — Each category has substantive analysis (not placeholder text)
- [ ] **Risk matrix severity math correct** — P × I = Severity, capped at 10 (even if P(3) × I(4) = 12)
- [ ] **Scoring rubric included** — Probability and Impact definitions with numeric values are present
- [ ] **At least 3 thesis killers identified** — Each specific and actionable (3-5 total)
- [ ] **Thesis killers have timeframes** — Each includes Immediate / 1-2 quarters / 1+ year
- [ ] **Top 5 risks have financial impact estimates** — Each includes revenue/earnings impact range
- [ ] **Risk correlations section present** — At least one correlated risk cluster identified
- [ ] **Monitoring dashboard has current values** — Not placeholders like "TBD" or "[X]"
- [ ] **Downside scenario probabilities valid** — Each 5-40%, sum <100%
- [ ] **Overall Risk Level uses standard format** — Exactly one of: LOW / MODERATE / HIGH / VERY HIGH (NOT "MODERATE-HIGH" or similar)

---

## SECTION B: Risk Category Completeness

All 7 categories must have substantive analysis (not placeholder text):

| # | Category | Present | Has Specific Risks | References Prior Research |
|---|----------|---------|-------------------|--------------------------|
| 1 | Business Model Risks | [ ] | [ ] | [ ] |
| 2 | Competitive Risks | [ ] | [ ] | [ ] |
| 3 | Financial Risks | [ ] | [ ] | [ ] |
| 4 | Operational Risks | [ ] | [ ] | [ ] |
| 5 | Regulatory and Political Risks | [ ] | [ ] | [ ] |
| 6 | Valuation Risks | [ ] | [ ] | [ ] |
| 7 | ESG and Reputational Risks | [ ] | [ ] | [ ] |

### Per-Category Requirements

- [ ] **At least one specific risk identified per category** — Not just headers
- [ ] **No placeholder text** — No "[Analysis here]" or "[TBD]"
- [ ] **Prior research referenced where applicable** — 10-K, Moat Analysis, Management Audit

---

## SECTION C: Risk Matrix Validation

### Per-Risk Requirements

For each risk in the matrix, verify:

- [ ] **Risk description is specific** — Not generic like "competition could increase"
- [ ] **Category matches one of the 7** — Correctly classified
- [ ] **Probability is valid** — Low(1) / Med(2) / High(3)
- [ ] **Impact is valid** — Low(1) / Med(2) / High(3) / Very High(4)
- [ ] **Severity math correct** — P × I = Severity
- [ ] **Severity capped at 10** — Even if P × I > 10
- [ ] **Mitigant is specific** — Not "management awareness" or similar

### Severity Interpretation Consistency

| Severity Score | Interpretation |
|----------------|----------------|
| 8-10 | Critical |
| 5-7 | Material |
| 3-4 | Moderate |
| 1-2 | Low |

- [ ] **Severity scores align with interpretations** in analysis

### Risk Matrix Examples

| Risk Description | Pass/Fail | Reason |
|------------------|-----------|--------|
| "Competition could increase" | FAIL | Generic, not specific |
| "Amazon entering segment via AWS partnership" | PASS | Specific, actionable |
| "Revenue concentration: top 3 clients = 45% of revenue" | PASS | Quantified, specific |
| "Might lose customers" | FAIL | Vague |

| Mitigant | Pass/Fail | Reason |
|----------|-----------|--------|
| "Management awareness" | FAIL | Too vague |
| "3-year contract lock-in with 90% retention" | PASS | Specific, quantified |
| "Diversified revenue base" | FAIL | Generic |
| "No single customer >8% of revenue; contracts have 12-month notice periods" | PASS | Specific |

---

## SECTION D: Top 5 Risks

- [ ] **Exactly 5 risks listed** — Ranked by severity
- [ ] **Ranking matches risk matrix severity scores** — Highest severity first
- [ ] **Each has description AND implications** — Not just name
- [ ] **Consistent with risk matrix** — Same risks, same severity order

### Validation Check

| Rank | Risk | Severity in Matrix | Correct Order |
|------|------|-------------------|---------------|
| 1 | ... | ... | [ ] |
| 2 | ... | ... | [ ] |
| 3 | ... | ... | [ ] |
| 4 | ... | ... | [ ] |
| 5 | ... | ... | [ ] |

---

## SECTION E: Thesis Killers

- [ ] **3-5 thesis killers identified** — Not <3, not >5
- [ ] **Each is specific and observable** — Not vague like "things get worse"
- [ ] **Each explains why it's fatal** — Not just what, but why it kills the thesis
- [ ] **Each is actionable** — Investor knows when to sell

### Thesis Killer Examples

| Thesis Killer | Pass/Fail | Reason |
|---------------|-----------|--------|
| "Things get worse" | FAIL | Vague, not observable |
| "Regulator revokes operating license" | PASS | Specific, observable, actionable |
| "Competition increases" | FAIL | Too vague |
| "Amazon announces competing product with pricing 40% below" | PASS | Specific trigger |
| "Something bad happens" | FAIL | Not specific |
| "CEO departure combined with loss of top 2 customers (>30% revenue)" | PASS | Specific, observable, quantified |

### Thesis Killer Timeframe Examples

| Format | Pass/Fail | Reason |
|--------|-----------|--------|
| "Attrition exceeds 12% — Timeframe: 1-2 quarters" | PASS | Timeframe explains how long to wait for confirmation |
| "Data breach causes enterprise loss — Timeframe: Immediate" | PASS | Single event trigger, sell immediately |
| "Market share drops below 15% — Timeframe: 1+ year" | PASS | Structural shift takes time to confirm |
| "Customer concentration increases" | FAIL | No timeframe specified |

### Overall Risk Level Examples

| Format | Pass/Fail | Reason |
|--------|-----------|--------|
| "MODERATE" | PASS | Standard format |
| "HIGH" | PASS | Standard format |
| "MODERATE-HIGH" | FAIL | Hybrid not allowed |
| "Moderate to High" | FAIL | Non-standard format |
| "VERY HIGH" | PASS | Standard format |
| "Medium" | FAIL | Wrong scale (use MODERATE) |

### Top 5 Risks Financial Impact Examples

| Format | Pass/Fail | Reason |
|--------|-----------|--------|
| "Microsoft bundling threatens 5-10% revenue loss" | PASS | Quantified range |
| "AI disruption could compress margins by 200-400bps" | PASS | Specific impact |
| "Customer concentration puts $1.2B ARR at risk" | PASS | Dollar amount |
| "Competition is increasing" | FAIL | No financial impact |
| "Significant revenue impact expected" | FAIL | Vague, not quantified |

---

## SECTION F: Monitoring Dashboard

### Per-Row Requirements

Each row must have:

| Field | Requirement |
|-------|-------------|
| Risk Area | Tied to an identified risk |
| Metric | Specific, measurable |
| Current | Actual number (not placeholder) |
| Warning Level | Specific threshold (not "declining") |
| Check Frequency | Quarterly / Monthly / Annual |
| Status | G / Y / R |

### Dashboard Validation

- [ ] **At least 5 metrics** in the dashboard
- [ ] **Current values are actual numbers** — Not "TBD", "[X]", "N/A"
- [ ] **Warning levels are specific thresholds** — Not "declining" or "worsening"
- [ ] **Status indicators present** — G/Y/R for each row

### Dashboard Examples

| Current Value | Pass/Fail | Reason |
|---------------|-----------|--------|
| "TBD" | FAIL | Placeholder |
| "[Current Value]" | FAIL | Placeholder |
| "45%" | PASS | Specific value |
| "1.2x" | PASS | Specific value |
| "~50%" | FAIL | Approximate |

| Warning Level | Pass/Fail | Reason |
|---------------|-----------|--------|
| "declining" | FAIL | Not specific threshold |
| "<1.5x" | PASS | Specific threshold |
| ">25%" | PASS | Specific threshold |
| "worsening" | FAIL | Not measurable |
| "if it gets worse" | FAIL | Vague |

---

## SECTION G: Downside Scenarios

### Structure Validation

Three scenarios required:
- [ ] **Mild Downside** present
- [ ] **Severe Downside** present
- [ ] **Catastrophic Downside** present

### Per-Scenario Requirements

For each scenario:

| Field | Present | Requirement |
|-------|---------|-------------|
| Assumptions | [ ] | Specific, not vague |
| Impact | [ ] | Includes: revenue %, margin %, EPS %, multiple, price target |
| Probability | [ ] | Percentage with justification |

### Probability Rules

- [ ] **Probability methodology stated at top** — Historical, consensus, conditional, or judgment
- [ ] **Each scenario: 5% ≤ probability ≤ 40%** — None outside this range
- [ ] **Sum of all scenarios < 100%** — Base case (not shown) takes remainder

### Probability Calculation Check

| Scenario | Probability | In Range (5-40%) | Has Justification |
|----------|-------------|------------------|-------------------|
| Mild | ...% | [ ] | [ ] |
| Severe | ...% | [ ] | [ ] |
| Catastrophic | ...% | [ ] | [ ] |
| **Total** | ...% | **< 100%?** [ ] | |

### Probability Examples

| Format | Pass/Fail | Reason |
|--------|-----------|--------|
| "15%" | FAIL | No justification |
| "15% — historical recession frequency" | PASS | Justified |
| "3% — very unlikely" | FAIL | Below 5% minimum |
| "50% — quite possible" | FAIL | Exceeds 40% maximum |
| "25% — based on competitor loss rate in past disruptions" | PASS | Justified with reasoning |

---

## SECTION H: Sources

- [ ] **Prior research files cited** — 10K Synthesis, Moat Analysis, Management Audit, Competitive Landscape
- [ ] **Files actually exist** — Referenced files were read during analysis
- [ ] **External sources listed if used** — With dates for time-sensitive info

### Required Prerequisites

The following should be referenced (per SKILL.md prerequisites):

- [ ] 10K Synthesis (`$synthesize-annual-filing`)
- [ ] Moat Analysis (`$analyze-moat-strength` or `$analyze-competitive-landscape`)
- [ ] Management Credibility Audit (`$audit-management-credibility`)

---

## SECTION I: Risk Correlations

- [ ] **Risk Correlations section present** — At least one cluster identified
- [ ] **Cascade scenario described** — How one risk triggers another
- [ ] **Combined severity estimated** — Impact if risks materialize together

### Risk Correlation Examples

| Correlation | Pass/Fail | Reason |
|-------------|-----------|--------|
| "Data breach + reputation damage: breach triggers churn, amplifying revenue impact" | PASS | Specific cascade |
| "Executive departure + strategy uncertainty + key person clauses in contracts" | PASS | Multi-risk cluster |
| "Risks are correlated" | FAIL | No specifics |
| "Things could go wrong together" | FAIL | Vague |

---

## Common Failure Modes

| Issue | Check | How to Fix |
|-------|-------|-----------|
| Missing risk category | <7 categories with analysis | Add missing category analysis |
| Generic risks | "Competition could increase" | Change to "Amazon entering segment X via partnership" |
| Wrong severity math | P × I ≠ stated Severity | Recalculate and fix |
| Severity uncapped | Severity >10 | Cap at 10 (max) |
| Generic mitigant | "Management awareness" | Add specific: "3-year contracts with 90% retention" |
| Top 5 not ranked | Order doesn't match severity | Reorder by severity score |
| Top 5 missing impact | No financial impact estimate | Add: "5-10% revenue decline" or "$XM at risk" |
| Vague thesis killer | "Things get worse" | Make specific: "Regulator revokes license" |
| Missing thesis killer timeframe | No timeframe | Add: "Timeframe: 1-2 quarters" |
| Missing current values | Dashboard has "TBD" | Research and add actual values |
| Placeholder thresholds | Warning Level "declining" | Add specific: "<1.5x" |
| Probability out of bounds | <5% or >40% | Adjust to valid range with reasoning |
| Probability sum ≥100% | Scenarios sum to 100%+ | Reduce probabilities |
| Missing probability justification | "15%" alone | Add: "15% — historical recession frequency" |
| No severity cap | P(3) × I(4) = 12 | Cap at 10 |
| Hybrid risk level | "MODERATE-HIGH" | Choose one: MODERATE or HIGH |
| Missing scoring rubric | No P/I definitions | Include rubric table from template |
| No risk correlations | Section missing | Add Risk Correlations section with at least one cluster |

---

## Validation Complete

After all sections:

- [ ] **All Section A-H items checked** (or N/A noted with reason)
- [ ] **Severity math verified** — Manually checked P × I = Severity, capped at 10
- [ ] **Probability constraints verified** — Each 5-40%, sum <100%
- [ ] **Current values confirmed** — No placeholders in Monitoring Dashboard
- [ ] **File saved** to correct path: `[Company]/2-Analysis/2.5-Risk-Assessment/Risk Analysis - [Company] - [YYYY-MM-DD-HHMM].md`
- [ ] **Quality self-assessment:** STRONG / ADEQUATE / NEEDS IMPROVEMENT
