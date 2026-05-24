# Working Analysis Templates

This file contains the intermediate output formats for each stage of the Munger Analysis v2 staged processing. Each Working Analysis carries forward findings to the next stage while staying compact (~2.5-4K tokens).

---

## Working Analysis v1 (Stage 1 Output)

```markdown
# Working Analysis v1: [Company] - Business Foundation

**Stage 1 Completed:** [Date/Time]
**Source Documents:** [List files read]

---

## Circle of Competence Assessment

**Assessment:** INSIDE / PARTIAL / OUTSIDE

### Business Understanding
[2-3 sentences — can you explain how it makes money in simple terms?]

### Key Economic Drivers
1. [Driver 1 — most important]
2. [Driver 2]
3. [Driver 3]

### Failure Modes (Inversion)
1. [What would cause this business to fail?]
2. [Second failure mode]
3. [Third failure mode]

### Why Not Higher?
[If PARTIAL, what's unclear? If INSIDE, write "N/A — business model is straightforward"]

---

## Financial Strength Assessment

**Score:** +2 / +1 / 0 / -1 / -2
**Assessment:** FORTRESS / STRONG / ADEQUATE / WEAK / DISTRESSED

### Balance Sheet Summary
| Metric | Value | Assessment |
|--------|-------|------------|
| Cash & Equivalents | $X B | |
| Net Debt (Cash) | $X B | |
| Debt/EBITDA | X.X | |
| Interest Coverage | X.X | |

### Returns on Capital
| Metric | Current | 5Y Avg | 10Y Avg | Direction |
|--------|---------|--------|---------|-----------|
| ROIC | X% | X% | X% | ↑/→/↓ |
| ROE | X% | X% | X% | ↑/→/↓ |

### Free Cash Flow
| Metric | Current | 5Y Avg | Direction |
|--------|---------|--------|-----------|
| FCF Margin | X% | X% | ↑/→/↓ |
| FCF Conversion | X% | X% | ↑/→/↓ |

### Key Strengths
- [Financial strength 1]
- [Financial strength 2]

### Key Concerns
- [Financial concern 1]
- [Financial concern 2]

### Why Not Higher?
[What prevents +2? Or "N/A — no material financial concerns"]

---

## Predictability Assessment (Partial - Financial Factors Only)

**Preliminary Assessment:** HIGH / MODERATE / LOW

### Financial Stability Factors
- [Factor 1 — e.g., "Recurring revenue"]
- [Factor 2 — e.g., "Low cyclicality"]
- [Factor 3]

### Financial Volatility Factors
- [Factor 1 — e.g., "Commodity exposure"]
- [Factor 2 — e.g., "Interest rate sensitivity"]

**Note:** This is a partial assessment based on financial data only. Stage 2 will add execution track record, Stage 3 will add competitive/disruption risks.

---

## Cross-Reference Flags for Stage 2

The following items require validation or further investigation in Stage 2 (Management):

- [ ] **Financial claims to verify:** [e.g., "10Y ROIC consistency — does management track record support sustainable returns?"]
- [ ] **Capital allocation history:** [e.g., "Strong FCF generation — how has management deployed it?"]
- [ ] **Execution consistency:** [e.g., "Stable margins — is this management skill or favorable conditions?"]

---

## Carried Forward Summary

### Completed Assessments
| Category | Score/Assessment | Key Finding |
|----------|------------------|-------------|
| Circle of Competence | INSIDE / PARTIAL / OUTSIDE | [One line] |
| Financial Strength | +X | [One line] |
| Predictability | Partial: [Level] | [Financial factors only] |

### Key Evidence to Preserve
1. [Most important financial metric/finding]
2. [Second most important]
3. [Third most important]

### Tensions or Concerns
- [Any inconsistencies noticed]
- [Any red flags to track]
```

---

## Working Analysis v2 (Stage 2 Output)

```markdown
# Working Analysis v2: [Company] - Management & Execution

**Stage 2 Completed:** [Date/Time]
**Source Documents:** [List files read, including Working Analysis v1]

---

## Cross-Reference Validation (from Stage 1)

### Stage 1 Flags Resolution

| Flag from Stage 1 | Status | Evidence/Finding |
|-------------------|--------|------------------|
| [Financial claims to verify] | ✓ Validated / ✗ Challenged | [What the management audit revealed] |
| [Capital allocation history] | ✓ Validated / ✗ Challenged | [M&A, buyback, dividend track record] |
| [Execution consistency] | ✓ Validated / ✗ Challenged | [Management role in results] |

### Tensions Identified
- [Any contradictions between Stage 1 financials and management track record]

---

## Quality of Management Assessment

**Score:** +2 / +1 / 0 / -1 / -2
**Assessment:** EXCEPTIONAL / GOOD / ADEQUATE / CONCERNING / POOR

### Incentive Alignment
| Factor | Data | Assessment |
|--------|------|------------|
| CEO Ownership | $X / X% | Good / Adequate / Weak |
| Insider Ownership | X% | Good / Adequate / Weak |
| Compensation Structure | [Mix] | Good / Adequate / Weak |

### Capital Allocation Track Record
| Category | Rating | Evidence |
|----------|--------|----------|
| M&A Discipline | Good / Mixed / Poor | [Brief] |
| Buyback Timing | Good / Mixed / Poor | [Brief] |
| Reinvestment Returns | Good / Mixed / Poor | [Brief] |
| Dividend Policy | Good / Mixed / Poor | [Brief] |

### Credibility Score (from Audit)
| Category | Delivery Rate |
|----------|---------------|
| Financial Targets | X% |
| Operational Guidance | X% |
| Capital Allocation | X% |
| **Overall** | **X%** |

**Say/Do Quadrant:** [Quadrant name]

### Candor & Transparency
[2-3 sentences with specific examples]

### Key Strengths
- [Management strength 1]
- [Management strength 2]

### Key Concerns
- [Management concern 1]
- [Management concern 2]

### Why Not Higher?
[What prevents +2? Or "N/A — no material management concerns"]

---

## Predictability Assessment (Refined - Add Execution)

**Updated Assessment:** HIGH / MODERATE-HIGH / MODERATE / LOW

### Stability Factors (cumulative)
- [From Stage 1: Financial factors]
- [New: Execution track record factors]

### Volatility Factors (cumulative)
- [From Stage 1: Financial factors]
- [New: Execution risk factors]

### Management Impact on Predictability
[1-2 sentences on how management affects predictability — e.g., "Conservative guidance leads to predictable beats" or "History of overpromising creates guidance uncertainty"]

---

## Long-Term Orientation (Partial - Management Horizon)

**Preliminary Assessment:** LONG-TERM / MEDIUM-TERM / SHORT-TERM

### Evidence of Time Horizon
- [Evidence of long-term thinking]
- [Evidence of short-term pressures]

**Note:** This is a partial assessment. Stage 3 will add secular trends and competitive dynamics.

---

## Cross-Reference Flags for Stage 3

The following items require validation or further investigation in Stage 3 (Competitive Position):

- [ ] **Moat claims to verify:** [e.g., "Management claims pricing power — do customer/competitor perspectives confirm?"]
- [ ] **Competitive threats:** [e.g., "Management downplays competitor X — is this accurate?"]
- [ ] **Execution in competitive context:** [e.g., "Strong capital allocation — but is moat widening or just milking?"]

---

## Carried Forward Summary

### Completed Assessments
| Category | Score/Assessment | Key Finding |
|----------|------------------|-------------|
| Circle of Competence | [From v1] | [One line] |
| Financial Strength | [From v1] | [One line] |
| Quality of Management | +X | [One line] |
| Predictability | Partial: [Level] | [Financial + Execution] |
| Long-Term Orientation | Partial: [Horizon] | [Management perspective only] |

### Key Evidence to Preserve
1. [Most important management finding]
2. [Key credibility data point]
3. [Capital allocation verdict]
4. [From v1: Key financial finding]
5. [From v1: Second financial finding]

### Tensions or Concerns (Cumulative)
- [From Stage 1, still unresolved]
- [New tensions from Stage 2]
```

---

## Working Analysis v3 (Stage 3 Output)

```markdown
# Working Analysis v3: [Company] - Competitive Position

**Stage 3 Completed:** [Date/Time]
**Source Documents:** [List files read, including Working Analysis v2]

---

## Cross-Reference Validation (from Stage 2)

### Stage 2 Flags Resolution

| Flag from Stage 2 | Status | Evidence/Finding |
|-------------------|--------|------------------|
| [Moat claims to verify] | ✓ Validated / ✗ Challenged | [What scuttlebutt/moat analysis revealed] |
| [Competitive threats] | ✓ Validated / ✗ Challenged | [External view of competition] |
| [Execution in competitive context] | ✓ Validated / ✗ Challenged | [Is moat widening/stable/shrinking?] |

### New Tensions Identified
- [Any contradictions between management claims and competitive reality]

---

## Moat & Competitive Advantage Assessment

**Score:** +2 / +1 / 0 / -1 / -2
**Assessment:** WIDE & WIDENING / WIDE & STABLE / NARROW / ERODING / NONE

### Moat Type Identification
| Moat Type | Strength | Key Evidence |
|-----------|----------|--------------|
| [Type 1] | Primary / Secondary / None | [One line with quantification if possible] |
| [Type 2] | Primary / Secondary / None | [One line] |
| [Type 3] | Primary / Secondary / None | [One line] |

### Moat Direction
**Direction:** Widening / Stable / Shrinking
[2-3 sentences with evidence from Scuttlebutt, Competitive Landscape, and/or Moat Strength analyses]

### Customer Perspective (from Scuttlebutt)
- **Why they choose:** [Key reasons]
- **What would make them switch:** [Switching triggers]
- **Sentiment:** Positive / Neutral / Negative

### Competitive Dynamics
- **Key competitors:** [List 2-3]
- **Market share trend:** Gaining / Stable / Losing
- **Competitive response risk:** Low / Medium / High

### Disruption Risk
[2-3 sentences on technological/business model disruption risk]

### Key Strengths
- [Moat strength 1]
- [Moat strength 2]

### Key Concerns
- [Moat concern 1]
- [Moat concern 2]

### Why Not Higher?
[What prevents +2? Or "N/A — no material moat concerns"]

---

## Predictability Assessment (Final)

**Final Score:** +2 / +1 / 0 / -1 / -2
**Assessment:** HIGH / MODERATE-HIGH / MODERATE / LOW / VERY LOW

### Stability Factors (Complete)
- [Financial factors from Stage 1]
- [Execution factors from Stage 2]
- [Competitive stability factors from Stage 3]

### Volatility Factors (Complete)
- [Financial factors from Stage 1]
- [Execution factors from Stage 2]
- [Competitive/disruption factors from Stage 3]

### Time Horizon Distinction
[1-2 sentences on short-term vs. long-term predictability]

### Inversion: What Could Go Wrong?
1. [Risk 1 — from Risk Assessment]
2. [Risk 2]
3. [Risk 3]
4. [Risk 4]
5. [Risk 5]

### Why Not Higher?
[What prevents +2 predictability?]

---

## Long-Term Orientation Assessment (Final)

**Final Score:** +2 / +1 / 0 / -1 / -2
**Assessment:** STRONG COMPOUNDER / MODERATE / LIMITED / UNLIKELY / VALUE TRAP

### Secular Tailwinds
- [Tailwind 1]
- [Tailwind 2]
- [Tailwind 3]

### Secular Headwinds
- [Headwind 1]
- [Headwind 2]
- [Headwind 3]

### Net Assessment
[2-3 sentences on tailwinds vs. headwinds balance]

### 10-20 Year Ownership Comfort
[2-3 sentences on what ownership experience would be like]

### Why Not Higher?
[What prevents +2?]

---

## Lollapalooza Effects Assessment

**Score:** +2 / +1 / 0
**Assessment:** PRESENT / PARTIAL / NONE

### Combining Forces
[2-3 sentences on whether multiple advantages reinforce each other]

### Virtuous Cycle (if present)
1. [Step 1] →
2. [Step 2] →
3. [Step 3] →
4. [Step 4] →
5. [Outcome / back to Step 1]

*If no virtuous cycle: "No clear virtuous cycle identified."*

### Reinforcing Feedback Loops
- [Loop 1]
- [Loop 2]
- [Loop 3]

### Mental Models That Apply
1. **[Model 1]:** [Brief application]
2. **[Model 2]:** [Brief application]
3. **[Model 3]:** [Brief application]
4. **[Model 4]:** [Brief application]
5. **[Model 5]:** [Brief application]

### Why Not Higher?
[What prevents +2 lollapalooza? Or "N/A — true lollapalooza present"]

---

## Final Synthesis Preparation

### Complete Scoring Summary

| Category | Score | Assessment | Why Not Higher? |
|----------|-------|------------|-----------------|
| Circle of Competence | INSIDE / PARTIAL / OUTSIDE | [From Stage 1] | [Brief] |
| Moat & Competitive Advantage | +X | [Assessment] | [Brief] |
| Quality of Management | +X | [From Stage 2] | [Brief] |
| Predictability & Simplicity | +X | [Final] | [Brief] |
| Financial Strength | +X | [From Stage 1] | [Brief] |
| Long-Term Compounding | +X | [Final] | [Brief] |
| Lollapalooza Effects | +X | [Assessment] | [Brief] |
| **Subtotal** | **X / 12** | | |

### Tensions Registry (All Stages)

| Tension | Source Stages | Resolution |
|---------|---------------|------------|
| [Tension 1] | Stage X vs. Stage Y | [Resolved / Unresolved — how?] |
| [Tension 2] | Stage X vs. Stage Y | [Resolved / Unresolved — how?] |

### Holistic Adjustment Considerations

Before Stage 4 finalizes, consider:
- [ ] Do category scores capture cross-cutting concerns?
- [ ] Does mechanical total match gut feel?
- [ ] Are there compounding risks across categories?
- [ ] Any "soft" concerns that didn't move individual scores but matter?

**Preliminary Holistic Adjustment Recommendation:** 0 / -1 / -2
**Rationale:** [Why this adjustment, or "None needed — scores capture full picture"]

### Key Evidence for Final Memo
1. [Most compelling positive finding]
2. [Second most compelling positive]
3. [Most material concern]
4. [Second most material concern]
5. [Unique insight from staged analysis]
```

---

## Usage Notes

### Token Budget
- **v1:** Target ~2,500 tokens (business + financial foundation)
- **v2:** Target ~3,000 tokens (adds management, cumulative)
- **v3:** Target ~4,000 tokens (comprehensive for final synthesis)

### Cross-Reference Discipline
- Every flag from Stage N must be explicitly addressed in Stage N+1
- Status must be "✓ Validated" or "✗ Challenged" — no "TBD" or blank
- Challenges should explain what the new evidence revealed

### "Why Not Higher?" Enforcement
- Every score requires this field
- If "Why Not Higher?" has substantive content, score is likely +1, not +2
- Only "N/A — no material concerns" allows +2

### Tensions Registry
- Contradictions between stages must be logged
- Final synthesis must resolve or acknowledge each tension
- Unresolved tensions may justify Holistic Adjustment
