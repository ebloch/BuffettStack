# Validation Checklist: company-overview

Use this checklist to verify output completeness before finalizing the Company Overview.

---

## SECTION A: Critical Validation (Must Pass)

These items MUST pass before the overview is complete. If any fail, fix before outputting.

- [ ] **At least 1 Foundation material read** — Annual filing memo, investor presentation memo, or financial data file
- [ ] **Excluded files filtered out** — No QC, Gap, or Improve files read as source material
- [ ] **YAML frontmatter complete** — type, company, ticker, period_start, period_end, years_analyzed, source_count
- [ ] **Key Takeaways present** — 5-8 bullets with cross-year synthesis, not point-in-time repetition
- [ ] **The Business section present** — 2-3 paragraphs explaining business model clearly
- [ ] **Financial Evolution table present** — With start/end values, CAGRs, and trajectory
- [ ] **Source Files section present** — Lists all materials read, organized by type

---

## SECTION B: Key Takeaways Quality

- [ ] **5-8 bullets present** — Not fewer than 5, not more than 8
- [ ] **Cross-year synthesis** — Each bullet identifies a pattern or trend across years, not single-year facts
- [ ] **Specific data included** — Each bullet includes supporting numbers (CAGRs, changes, mix shifts)
- [ ] **"So what?" answered** — Each bullet explains why the insight matters for investment analysis
- [ ] **Bold lead-ins** — Each bullet starts with a bolded phrase
- [ ] **Most important first** — Bullets ordered by significance, not chronology

### Key Takeaways Examples

| Takeaway | Pass/Fail | Reason |
|----------|-----------|--------|
| "Revenue grew in 2023." | ❌ FAIL | Point-in-time fact, no pattern, no "so what?" |
| "**Consistent double-digit growth:** Revenue CAGR of 12.4% over 5 years demonstrates durable demand..." | ✅ PASS | Pattern, specific data, explains significance |
| "Things got better over time." | ❌ FAIL | Vague, no data |
| "**Margin expansion despite inflation:** Operating margin improved from 18% to 24% as pricing power offset cost increases..." | ✅ PASS | Trend, specific numbers, explains mechanism |

---

## SECTION C: The Business Section Quality

- [ ] **Standalone readability** — Someone new to the company could understand the business
- [ ] **Business model explained** — What products/services, who are customers, how revenue is generated
- [ ] **Economic engine identified** — What drives value creation, why this business works
- [ ] **Segments table present** — With description and % of revenue for each segment
- [ ] **Geographic mix noted** — Breakdown provided or "Not disclosed" stated
- [ ] **Customer concentration noted** — Data provided or "No single customer >10%" stated

### Business Section Examples

| Description | Pass/Fail | Reason |
|-------------|-----------|--------|
| "Company XYZ operates in the technology sector." | ❌ FAIL | Too vague, doesn't explain what they do |
| "CME Group operates the world's largest derivatives exchange, generating revenue primarily from transaction fees..." | ✅ PASS | Clear, specific, explains business model |

---

## SECTION D: Financial Evolution Table

### Required Metrics

- [ ] **Revenue** — Start value, end value, CAGR, trajectory
- [ ] **Operating Income** — Start value, end value, CAGR, trajectory
- [ ] **Net Income** — Start value, end value, CAGR, trajectory
- [ ] **FCF** — Start value, end value, CAGR, trajectory
- [ ] **Employees** — Start value, end value, CAGR, trajectory (if available)
- [ ] **Operating Margin** — Start value, end value, change in pts
- [ ] **ROIC** — Start value, end value, change in pts (if applicable to business)

### CAGR Math Verification

```
CAGR Formula: ((End Value / Start Value) ^ (1 / Years)) - 1

Example verification:
Start: $1,000M | End: $1,500M | Years: 5
CAGR = ((1500 / 1000) ^ (1/5)) - 1 = (1.5 ^ 0.2) - 1 = 1.0845 - 1 = 8.45%
```

- [ ] **CAGR math correct** — Manually verify at least one CAGR calculation
- [ ] **Trajectory accurate** — Matches the data (e.g., "Accelerating" means growth rate increased)

### Trajectory Definitions

| Trajectory | Definition |
|------------|------------|
| Accelerating | Growth rate increasing over the period |
| Steady | Consistent growth rate |
| Decelerating | Growth rate decreasing |
| Volatile | Inconsistent, no clear trend |
| Declining | Negative growth |

---

## SECTION E: Segment Mix Shift

- [ ] **All major segments included** — Segments representing >10% of revenue
- [ ] **Start and end percentages** — Mix at beginning and end of period
- [ ] **Change calculated** — Δ column shows percentage point change
- [ ] **Significance assessed** — Each segment flagged with significance level
- [ ] **Interpretation provided** — 1-2 sentences explaining what mix shift means

### Significance Flags

| Flag | Criteria |
|------|----------|
| Emerging driver | Grew from <10% to >20% |
| Stable core | Remained within ±5pts |
| Declining relevance | Shrank from >20% to <10% |
| New segment | Did not exist at start |

---

## SECTION F: Management Credibility Scorecard

- [ ] **At least 3 promises scored** — If trackable promises exist in source materials
- [ ] **Exact quote format** — Promise text in quotes with source attribution
- [ ] **Outcome assessed** — Each promise marked as Delivered/Partial/Missed/Abandoned
- [ ] **Score assigned** — +2 to -2 scale for each promise
- [ ] **Total score calculated** — Sum of individual scores
- [ ] **Rating assigned** — HIGH/MODERATE/LOW/CONCERNING based on thresholds

### Scoring Reference

| Score | Meaning |
|-------|---------|
| +2 | Exceeded promise |
| +1 | Delivered as stated |
| 0 | Partial with valid explanation |
| -1 | Missed with excuses |
| -2 | Abandoned/ignored |

### Rating Thresholds

| Total Score | Rating |
|-------------|--------|
| >+5 | HIGH |
| 0 to +5 | MODERATE |
| -5 to 0 | LOW |
| <-5 | CONCERNING |

- [ ] **Insufficient data handled** — If no trackable promises, explicitly states: "Unable to assess — no trackable promises in source materials."

---

## SECTION G: Risk Evolution Matrix

- [ ] **At least 4 risk categories** — From: Competitive, Regulatory, Financial, Operational, Technology, Market/Macro
- [ ] **Multi-year tracking** — Shows risk status across multiple years (not just current)
- [ ] **Trend arrows present** — ↑/→/↓ for each risk category
- [ ] **New risks flagged** — [NEW] label with first mention year
- [ ] **Retired risks flagged** — [RETIRED] label with last mention year
- [ ] **Commentary provided** — 1-2 sentences on overall risk trajectory

### Trend Arrow Meanings

| Arrow | Meaning |
|-------|---------|
| ↑ | Risk increasing |
| → | Risk stable |
| ↓ | Risk decreasing |

---

## SECTION H: Key Events Timeline

- [ ] **At least 3 events** — Significant events that shaped the business
- [ ] **Year column** — Fiscal year for each event
- [ ] **Event description** — Clear, specific description
- [ ] **Impact assessed** — Brief impact statement for each event
- [ ] **Covers variety** — Not all same type (e.g., not all acquisitions)

### Event Types to Include

- Acquisitions and divestitures
- Leadership changes (CEO, CFO)
- New product launches or exits
- Regulatory changes
- Strategic pivots
- Major market events affecting the company

---

## SECTION I: Questions for Monitoring

- [ ] **3-5 questions present** — Forward-looking questions based on observed patterns
- [ ] **Specific, not generic** — Each question is specific to this company
- [ ] **"Why it matters" included** — Each question has explicit investment relevance
- [ ] **Answerable over time** — Questions can be resolved as events unfold

### Question Quality Examples

| Question | Pass/Fail | Reason |
|----------|-----------|--------|
| "Will the company do well?" | ❌ FAIL | Too vague |
| "Can data services revenue maintain 15%+ growth as core clearing volumes mature?" | ✅ PASS | Specific, grounded in observed pattern |

---

## SECTION J: Year Card Summary

- [ ] **One card per fiscal year** — All years covered in the analysis
- [ ] **Theme present** — One phrase capturing the year
- [ ] **Key developments** — 2-3 most significant items
- [ ] **Performance metrics** — Revenue and Op Income with YoY change
- [ ] **Consistent format** — Same structure for each year

---

## SECTION K: Source Files

- [ ] **All sources listed** — Every file read during the analysis
- [ ] **Organized by type** — Annual filing memos, investor presentations, financial statements
- [ ] **Filenames included** — Exact filenames for traceability
- [ ] **Total count stated** — "[N] files" summary

---

## SECTION L: Brevity & Density Check

These checks ensure the output is dense and scannable, not bloated with restated data.

- [ ] **Total output under 300 lines / 4,000 words** — Count lines and estimate word count
- [ ] **No extra sections beyond template** — No "Valuation Context," "Balance Sheet Snapshot," "Product Innovation Pipeline," etc.
- [ ] **Financial Narrative ≤ 4 sentences** — Summarizes the key story, does not walk through every metric
- [ ] **Commentary sections ≤ 2 sentences each** — Mix Shift, Credibility, Risk commentaries highlight the most important takeaway only
- [ ] **Key Takeaway bullets ≤ 60 words each** — Two-sentence maximum per bullet
- [ ] **The Business ≤ 200 words** — No sub-sections or extra tables beyond the Segments table
- [ ] **Questions use parenthetical format** — "Why it matters" is inline, not a separate indented line

### Before/After Examples

**Financial Narrative — BAD (restates table):**
> Revenue grew from $4.2B in FY2019 to $5.5B in FY2023, a CAGR of 7.0%. Operating income increased from $2.4B to $3.3B, a CAGR of 8.3%. Net income went from $2.1B to $3.0B. FCF expanded from $1.8B to $2.5B. Operating margin improved from 57.1% to 60.0%. ROIC increased from 8.2% to 9.8%.

**Financial Narrative — GOOD (explains why):**
> The margin story is the headline: operating margin expanded 290bps as clearing fee increases outpaced technology spending. Revenue growth accelerated in FY2022-23 driven by rate volatility boosting interest rate product volumes.

**Commentary — BAD (walks through rows):**
> The Market Data segment grew from 22% to 28%, while Clearing and Transaction Fees declined from 65% to 58%. Other revenue remained stable at 14%.

**Commentary — GOOD (key takeaway):**
> Market Data's rise to 28% of revenue signals a successful diversification away from pure transaction dependence — this is higher-margin, recurring revenue.

---

## Common Failure Modes

| Issue | Check | Fix |
|-------|-------|-----|
| Incorrect CAGR | Math error | Verify: ((End/Start)^(1/Years) - 1) × 100 |
| Point-in-time takeaways | Not synthesized | Rewrite to identify cross-year patterns |
| Generic business description | Could apply to any company | Add specific details about this company |
| Missing segments | Incomplete extraction | Re-read source memos for segment data |
| No credibility scores | Promises not extracted | Re-read for trackable promises with outcomes |
| Sparse timeline | <3 events | Review source memos for changes, acquisitions, leadership |
| Risk matrix without trends | No arrows | Add ↑/→/↓ based on evolution across years |
| QC/Gap files included | Wrong files read | Filter these out from source materials |
| Commentary restates table | Prose walks through every row | Rewrite to 1-2 sentences highlighting the key insight and explaining "why" |
| Extra sections added | Sections not in template | Remove — stick strictly to template sections |
| Output too long | >300 lines or >4,000 words | Cut prose that restates tabular data; tighten commentary to 1-2 sentences |

---

## Validation Complete

After all sections checked:

- [ ] **All Section A items pass** (critical validation)
- [ ] **CAGR math manually verified** — At least one calculation spot-checked
- [ ] **Key Takeaways are cross-year synthesis** — Not point-in-time facts
- [ ] **The Business section is readable by newcomer** — Clear, complete explanation
- [ ] **Risk matrix shows evolution** — Not just current state
- [ ] **Source files documented** — Full traceability
- [ ] **Brevity & density check passes** — Section L items all verified
- [ ] **File saved to correct path** — `[Company]/[Company] - Business Overview - Memo - [YYYY-MM-DD].md`
- [ ] **Quality self-assessment:** STRONG / ADEQUATE / NEEDS IMPROVEMENT
