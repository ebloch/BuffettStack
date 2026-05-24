# Validation Checklist: analyze-moat-strength

Use this checklist to verify output completeness before finalizing.

---

## CRITICAL VALIDATION (Check First)

These items MUST pass before the analysis is complete. If any fail, fix before outputting.

- [ ] **All 10 moat items scored** — A1-A7 and B1-B3 each have a score from -2 to +2
- [ ] **Every +2 score has "Why Not Higher?" = N/A** — if any concern exists in segments >~15% of revenue, max is +1
- [ ] **Materiality map present** — segment revenue breakdown table in Part 2, used to weight +2 gate decisions
- [ ] **Composite math is correct** — sum of 10 scores / 10 = stated composite
- [ ] **Rating matches composite** — >= 1.25 = WIDE, 0.50-1.24 = NARROW, < 0.50 = NONE
- [ ] **Each scored item has quantified evidence** — not vague descriptors

---

## Part 1: Executive Summary & Scorecard

- [ ] Moat Rating stated (WIDE / NARROW / NONE — not hedged)
- [ ] Trajectory stated (WIDENING / STABLE / NARROWING)
- [ ] Confidence stated (HIGH / MEDIUM / LOW)
- [ ] Composite score stated as X.XX / 2.00
- [ ] Summary present (4-6 sentences, not multi-paragraph)
- [ ] Category A scorecard table: all 7 items (A1-A7) with Score, Why Not Higher?, Evidence Summary
- [ ] Category B scorecard table: all 3 items (B1-B3) with Score, Why Not Higher?, Evidence Summary
- [ ] Composite calculation shown: [sum] / 10 = [X.XX] → [RATING]

---

## Part 2: Detailed Evidence

### For Each of the 10 Items (A1-A7, B1-B3)

- [ ] Score stated at top of section
- [ ] 2-4 bullet point justification (not paragraphs; don't repeat evidence table data)
- [ ] Evidence table with quantified metrics (specific numbers, not vague)
- [ ] Source citations in evidence table

### Item-Specific Checks

#### A1: Pricing Power
- [ ] Price increase history with dates and amounts
- [ ] Customer retention/volume impact post-increase
- [ ] Price premium vs competitors quantified

#### A2: Switching Costs
- [ ] Switching cost quantified ($$, time, effort)
- [ ] Customer retention rate cited
- [ ] Average customer tenure or contract length

#### A3: Network Effects
- [ ] Network effect type identified (direct, indirect, data, platform)
- [ ] Multi-homing risk assessed
- [ ] Network growth/density metric provided

#### A4: Cost / Scale Advantages
- [ ] Margin comparison vs peers (specific numbers)
- [ ] Source of advantage identified (structural vs scale)
- [ ] Minimum efficient scale assessed

#### A5: Branding
- [ ] Brand premium quantified (% over generic/private label)
- [ ] Brand recall or awareness metric cited
- [ ] Customer willingness-to-pay premium evidenced
- [ ] Distinct from A6 — brand is durable consumer perception, not IP/licenses

#### A6: Cornered Resource
- [ ] Specific exclusive resources identified (patents, licenses, data, geology, contracts)
- [ ] Patent runway / regulatory barrier quantified where applicable
- [ ] Resource scarcity and exclusivity assessed
- [ ] Not just "good engineers" — must be truly exclusive access

#### A7: Process Power
- [ ] Specific embedded processes/culture identified
- [ ] Operational metrics vs peers cited (cost per unit, quality, speed)
- [ ] Process tenure assessed (years sustained)
- [ ] Key test addressed: could you hire away the CEO and replicate it?

#### B1: The $10B Test
- [ ] "What Can't Be Copied" table present
- [ ] Time-to-replicate assessed for each advantage
- [ ] Honest about what CAN be copied

#### B2: Disruption Risk
- [ ] All 3 Christensen vectors assessed (Low-End, New-Market, Technology)
- [ ] Each vector has a threat level (Low / Medium / High)
- [ ] Overshooting assessment present
- [ ] Specific disruptors named (not just "technology risk")

#### B3: Structural vs Executional
- [ ] Each moat source categorized as Structural or Executional
- [ ] Management dependency assessed (Low / Medium / High)
- [ ] "Would this survive a mediocre CEO?" answered

---

## Part 3: Trajectory Assessment

- [ ] Direction stated (WIDENING / STABLE / NARROWING)
- [ ] Trajectory composite stated
- [ ] All 3 trajectory items scored (T1-T3) with -2 to +2 scores
- [ ] Trajectory math correct: sum of 3 scores / 3 = stated composite
- [ ] Direction matches composite: >= 0.75 = WIDENING, -0.74 to 0.74 = STABLE, <= -0.75 = NARROWING
- [ ] Trajectory narrative present (4-6 sentences)

### Trajectory Item-Specific Checks

#### T1: Competitive Position Trend
- [ ] Market share data cited (5-year if available)
- [ ] Competitive entry/exit patterns noted

#### T2: Reinvestment Quality
- [ ] R&D or capex vs peers
- [ ] Moat-widening investment vs financial engineering assessed

#### T3: Secular Alignment
- [ ] 2-3 secular trends identified
- [ ] Directional impact on moat stated for each

---

## Part 4: Reference Sections

### Who Lost and Why
- [ ] At least 2 former industry leaders analyzed
- [ ] Table has: Company, Peak Position, What Happened, Moat That Failed, Lesson
- [ ] Pattern analysis present
- [ ] Implications for subject company stated

### Disruption Watch List
- [ ] At least 3 specific disruptors listed
- [ ] Each has: Stage (Nascent/Emerging/Accelerating), Threat Vector, Threat Level, Warning Signal
- [ ] Supports the B2 Disruption Risk score

---

## Part 5: Conclusion

- [ ] Final rating matches Part 1 (WIDE/NARROW/NONE)
- [ ] Final trajectory matches Part 3 (WIDENING/STABLE/NARROWING)
- [ ] At least 3 key threats with warning signals and timelines
- [ ] Rationale present (4-6 sentences)

---

## Sources

- [ ] Sources section present
- [ ] Lists all source documents used
- [ ] Lists web sources used

---

## Common Failure Modes

| Issue | Check |
|-------|-------|
| +2 with concerns | "Why Not Higher?" must be N/A for +2; only concerns in segments >~15% of revenue gate a +2 |
| Vague evidence | "Strong brand" fails; "20% pricing premium over 10 years" passes |
| Wrong composite | Recalculate: sum all 10 scores, divide by 10 |
| Wrong rating | Check thresholds: >= 1.25 WIDE, 0.50-1.24 NARROW, < 0.50 NONE |
| Wrong trajectory | Check thresholds: >= 0.75 WIDENING, -0.74 to 0.74 STABLE, <= -0.75 NARROWING |
| Missing disruption vectors | All 3 Christensen vectors must be assessed in B2 |
| Structural/executional missing | Each moat source from A1-A7 must appear in B3 table |
| Trajectory anchored on moat | Trajectory should assess direction, not re-rate strength |
