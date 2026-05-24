# Validation Checklist: scenario-analysis

Use this checklist to verify output completeness before finalizing the Scenario Analysis.

---

## SECTION A: Critical Validation (Check First)

These items MUST pass before the analysis is complete. If any fail, fix before outputting.

- [ ] **Exactly 5 scenarios present** — Not 3, not 4, not 6. Must have all 5: Positive Surprise, Thesis Validated, Slow Compounding, Stagnation, Thesis Broken
- [ ] **Probabilities sum to exactly 100%** — Not 99%, not 101%. Exactly 100%
- [ ] **Each probability ≥5% and ≤50%** — No scenario below 5% (too speculative), none above 50% (would dominate)
- [ ] **Each scenario has all 4 components** — Narrative, Key Assumptions, Moat Status, Trigger Signals
- [ ] **Moat Status uses valid values** — Only: Widened / Stable / Eroding / Impaired / Gone
- [ ] **Scenario Overview table present** — With all 5 scenarios, probabilities, and Total = 100%
- [ ] **No financial projections in narratives** — Only qualitative analysis; probabilities are the only numbers

---

## SECTION B: Scenario Completeness

All 5 scenarios must be complete with all components:

| # | Scenario | Prob (5-50%) | Narrative (2-3¶) | Assumptions (3-5) | Moat Status | Triggers |
|---|----------|--------------|------------------|-------------------|-------------|----------|
| 1 | Positive Surprise | [ ] | [ ] | [ ] | [ ] | [ ] |
| 2 | Thesis Validated | [ ] | [ ] | [ ] | [ ] | [ ] |
| 3 | Slow Compounding | [ ] | [ ] | [ ] | [ ] | [ ] |
| 4 | Stagnation | [ ] | [ ] | [ ] | [ ] | [ ] |
| 5 | Thesis Broken | [ ] | [ ] | [ ] | [ ] | [ ] |

### Quick Math Check

```
Scenario 1: ___% + Scenario 2: ___% + Scenario 3: ___% + Scenario 4: ___% + Scenario 5: ___% = ____%

Must equal exactly 100%
```

---

## SECTION C: Probability Validation

### Math Check

- [ ] **Sum = 100%** — Add all 5 probabilities; must equal exactly 100%
- [ ] **No rounding drift** — If using decimals, verify they sum correctly

### Range Check

| Scenario | Probability | ≥5%? | ≤50%? | Valid |
|----------|-------------|------|-------|-------|
| 1. Positive Surprise | ...% | [ ] | [ ] | [ ] |
| 2. Thesis Validated | ...% | [ ] | [ ] | [ ] |
| 3. Slow Compounding | ...% | [ ] | [ ] | [ ] |
| 4. Stagnation | ...% | [ ] | [ ] | [ ] |
| 5. Thesis Broken | ...% | [ ] | [ ] | [ ] |

### Probability Rationale

- [ ] **Probability Rationale section present** — Dedicated section explaining assignments
- [ ] **Each scenario has justification** — 1-2 sentences explaining why this probability
- [ ] **Evidence-based, not gut feel** — Rationale references research findings
- [ ] **Distribution reflects uncertainty honestly** — If uncertain, distribution is flatter

### Probability Examples

| Format | Pass/Fail | Reason |
|--------|-----------|--------|
| "25%" with no explanation | ❌ FAIL | No justification |
| "25% — Historical management execution rate supports base case" | ✅ PASS | Justified with evidence |
| "3% — Very unlikely" | ❌ FAIL | Below 5% minimum |
| "60% — Most likely outcome" | ❌ FAIL | Exceeds 50% maximum |
| "20% — Moat analysis shows erosion risk; management audit shows inconsistent execution" | ✅ PASS | Evidence-based justification |

---

## SECTION D: Narrative Quality

For each scenario's narrative:

- [ ] **2-3 paragraphs present** — Not 1 sentence, not 5 paragraphs
- [ ] **Written as "history from the future"** — Tells the story of how it unfolds over 10 years
- [ ] **Specific, not generic** — Names specific events, competitors, dynamics
- [ ] **No financial projections** — No EPS, revenue targets, or return calculations
- [ ] **Covers full arc** — Years 1-3, inflection points, where company ends up

### Narrative Examples

| Narrative Excerpt | Pass/Fail | Reason |
|-------------------|-----------|--------|
| "Competition could increase and hurt the company." | ❌ FAIL | Generic, not specific |
| "By 2028, Amazon's entry with zero-fee trading forces margin compression. Management responds by..." | ✅ PASS | Specific competitor, timeline, mechanism |
| "The company will grow EPS at 15% annually to reach $50 per share." | ❌ FAIL | Financial projection (keep qualitative) |
| "Things get better over time." | ❌ FAIL | Vague, no story |
| "In the first two years, the regulatory approval in India unlocks a market 3x the current TAM. Management, whose credibility audit scored HIGH, executes the expansion playbook proven in Southeast Asia..." | ✅ PASS | Specific, references research, tells story |

---

## SECTION E: Assumptions Quality

For each scenario's Key Assumptions:

- [ ] **3-5 assumptions per scenario** — Not 1-2, not 6+
- [ ] **Specific and verifiable** — Can be checked over time
- [ ] **Trace back to research** — Grounded in 10-K, moat analysis, risk assessment, etc.
- [ ] **Internally consistent** — Assumptions don't contradict each other

### Assumption Examples

| Assumption | Pass/Fail | Reason |
|------------|-----------|--------|
| "Things go well" | ❌ FAIL | Vague, not verifiable |
| "Clearing revenue CAGR exceeds 8% as new products scale" | ✅ PASS | Specific, verifiable |
| "No major competitors emerge" | ❌ FAIL | Too vague |
| "Amazon does not enter the derivatives clearing space within 5 years" | ✅ PASS | Specific, verifiable |
| "Management continues strong capital allocation" | ❌ FAIL | Vague |
| "Buybacks continue at >$1B/year with ROIC maintained above 40%" | ✅ PASS | Specific, quantified, verifiable |

---

## SECTION F: Trigger Signals Quality

For each scenario's Trigger Signals:

- [ ] **Observable within 1-2 years** — Not 5-10 year indicators
- [ ] **Specific metrics or events** — Can be measured or observed
- [ ] **Actionable** — Investor can update view based on signal
- [ ] **Different across scenarios** — Each scenario has unique triggers

### Trigger Signal Examples

| Trigger Signal | Pass/Fail | Reason |
|----------------|-----------|--------|
| "Business improves" | ❌ FAIL | Vague, not observable |
| "Clearing volume growth >15% in next 4 quarters" | ✅ PASS | Specific, measurable, timely |
| "Competition increases" | ❌ FAIL | Not specific |
| "Announcement of major bank moving to alternative clearing venue" | ✅ PASS | Observable event |
| "Things start going wrong" | ❌ FAIL | Vague |
| "ROIC drops below 30% for 2 consecutive quarters" | ✅ PASS | Specific threshold, timeframe |

---

## SECTION G: Supporting Sections

### Key Drivers Section

- [ ] **Key Uncertainties present** — What we don't know that will determine outcomes
- [ ] **Tailwinds present** — Forces working in the company's favor
- [ ] **Headwinds present** — Forces working against the company
- [ ] **At least 3 items in each category** — Substantive, not placeholder

### Scenario Overview Table

- [ ] **All 5 scenarios listed** — With descriptive titles
- [ ] **Probability column** — With values for each
- [ ] **Moat Status column** — Using valid values only
- [ ] **Total row shows 100%** — Explicit sum verification

### Scenario Monitoring Section

- [ ] **Quarterly Review Checklist present** — What to check each quarter
- [ ] **At least 5 monitoring items** — Specific metrics/events
- [ ] **Probability Update Triggers present** — When to revise probabilities
- [ ] **At least 3 update triggers** — Specific events that warrant revision

---

## SECTION H: Sources

### Prior Research References

- [ ] **10K Synthesis cited** — `$synthesize-annual-filing` output referenced
- [ ] **Management Audit cited** — `$audit-management-credibility` output referenced
- [ ] **Financial Data cited** — `$fetch-financials` output referenced
- [ ] **Moat Analysis cited** — `$analyze-moat-strength` or `$analyze-competitive-landscape` or `$scuttlebutt`
- [ ] **Risk Assessment cited** — `$analyze-investment-risks` output referenced

### Source Validation

- [ ] **All 5 required prerequisites referenced** — Per SKILL.md requirements
- [ ] **Files actually exist** — Referenced files were read during analysis
- [ ] **Specific insights traced** — Scenarios connect to specific findings from research

---

## Common Failure Modes

| Issue | Check | How to Fix |
|-------|-------|-----------|
| Wrong scenario count | Count ≠ 5 | Must have exactly 5 scenarios in required order |
| Probabilities don't sum to 100% | Sum ≠ 100% | Adjust until exactly 100% |
| Probability <5% | P < 5% | Increase to at least 5% or combine with adjacent scenario |
| Probability >50% | P > 50% | Reduce to max 50%; redistribute to other scenarios |
| Missing narrative | <2 paragraphs | Write 2-3 paragraph "history from the future" |
| Missing assumptions | <3 assumptions | Add 3-5 specific, verifiable assumptions |
| Invalid moat status | Not in enum | Use only: Widened / Stable / Eroding / Impaired / Gone |
| Vague trigger signals | Not observable | Make specific and measurable within 1-2 years |
| Generic scenarios | "Competition increases" | Make specific: "Amazon launches X with Y pricing" |
| Missing probability rationale | No justification | Add 1-2 sentences per scenario citing evidence |
| Financial projections in narrative | Numbers beyond probability | Remove; keep qualitative only |
| Missing Key Drivers | No Uncertainties/Tailwinds/Headwinds | Add all three sections with 3+ items each |
| Missing monitoring section | No quarterly checklist | Add monitoring table and update triggers |
| Prerequisites not cited | Missing source references | Add Sources section listing all research used |

---

## Moat Status Quick Reference

| Value | Meaning |
|-------|---------|
| **Widened** | Moat stronger than today |
| **Stable** | Moat maintained |
| **Eroding** | Moat weakening but still present |
| **Impaired** | Significant moat damage |
| **Gone** | No meaningful competitive advantage remains |

---

## Validation Complete

After all sections:

- [ ] **All Section A-H items checked** (or N/A noted with reason)
- [ ] **Probability math verified** — Manually summed = exactly 100%, each 5-50%
- [ ] **All 5 scenarios complete** — Each has narrative, assumptions, moat status, triggers
- [ ] **Narratives are specific** — No generic "competition could increase" language
- [ ] **File saved** to correct path: `[Company]/3-Synthesis/3.3-Scenarios/10-Year Scenario Analysis - [Company] - [YYYY-MM-DD-HHMM].md`
- [ ] **Quality self-assessment:** STRONG / ADEQUATE / NEEDS IMPROVEMENT
