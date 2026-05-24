# Validation Checklist: analyze-competitive-landscape

Use this checklist to verify output completeness before finalizing.

---

## CRITICAL VALIDATION (Check First)

These items MUST pass before the analysis is complete. If any fail, fix before outputting.

### No Tilde or Approximation Checks

- [ ] **NO TILDE ESTIMATES ANYWHERE:** Search ENTIRE output for "~" character. If ANY numerical value uses tildes, FIX IMMEDIATELY. This includes:
  - Industry historical/projected CAGRs
  - Competitor 5-year revenue CAGRs
  - Market share percentages (use "70% [est.]" not "~70%")
  - Margin estimates
  - Dollar amounts (revenue, market cap, backlog, TAM)
  - ROIC and other financial ratios
  - Executive Summary prose (summaries often re-introduce approximations)
- [ ] **NO "APPROXIMATELY" FOR CAGRS:** Search for "approximately" in growth rate context. Replace with calculated figures.

### CAGR Format Checks

- [ ] **ALL CAGRs HAVE YEAR RANGES:** Every CAGR figure includes "(FY20XX-FY20XX)" format
- [ ] **HISTORICAL INDUSTRY CAGR IS A SINGLE FIGURE:** Not "4-5%" or "strong growth"—must be "4.5% CAGR" (single number). If sources conflicted, verify that (1) range was stated, (2) discrepancy was explained, AND (3) single preferred figure was selected
- [ ] **PROJECTED INDUSTRY CAGR IS A SINGLE FIGURE:** Not "5-7%"—must be "6% CAGR" or similar (single number with source). If sources conflicted, verify same three-step process was followed

### Internal Consistency Checks

- [ ] **CAGR RECONCILIATION:** For each company mentioned, search for ALL CAGR references. If the same company's CAGR appears in multiple places (competitor profile, comparison table, footnotes), they MUST match exactly.
- [ ] **NO SELF-CONTRADICTING CALCULATIONS:** If a footnote calculates a CAGR (e.g., "14.1%") and a table cell shows a different figure (e.g., "11.8%") for the same company and period, this is a FAIL. Resolve before output.
- [ ] **MARKET SHARE ARITHMETIC VERIFIED:** If stating "top N = X%", manually sum the individual shares to verify

### Source & Format Checks

- [ ] **SOURCES INCLUDE HYPERLINKS:** The Sources section must include at least 5 URLs in format `[Source Name](URL)`

---

## Section 2B: Segment Analysis (Conditional)

### Segment Detection
- [ ] **Checked 10K synthesis for segments:** Parsed YAML `segments:` field
- [ ] **Threshold evaluated:** Determined if 2+ segments each ≥15% of revenue
- [ ] **Decision documented:** Either completed separate segment passes OR noted "Single-segment — Section 2B not applicable"

### If Segment Passes Were Needed:
- [ ] **All material segments have segment passes:** One isolated segment pass per segment >=15%
- [ ] **Segment passes completed independently:** Parallel Codex sub-agent orchestration used when available, or each segment analyzed sequentially with isolated focus
- [ ] **Each segment pass output collected:** All segment analyses collected before proceeding

### Section 2B Content (If Included):
- [ ] **Segment Overview table present:** Shows all segments with revenue, % total, TAM, growth, primary competitors
- [ ] **Per-segment analysis complete:** Each segment has market metrics, competitors, market share, dynamics
- [ ] **Segment TAMs are DIFFERENT:** Not the same consolidated TAM repeated for each segment
- [ ] **Segment competitors are DIFFERENT:** Different segments have different competitive sets
- [ ] **Competitor Overlap Matrix present:** Shows which competitors span segments

### Cross-Reference Checks:
- [ ] **Competitor profiles reference segments:** Section 3 profiles note segment focus for multi-segment companies
- [ ] **Five Forces has segment variations:** If forces differ materially by segment, Section 4 includes Segment Variations table
- [ ] **Segment revenue matches 10K:** Figures consistent with source memo

---

## Section 1: Industry Overview

- [ ] TAM provided with dollar figure and source
- [ ] Historical growth rate is a **SINGLE numerical CAGR** with source (not "4-5%" ranges, not "~10%", not "growing")
- [ ] If historical growth is a range (e.g., "10-12% CAGR"), the range MUST be explained (conflicting sources, market definition differences) AND a preferred single figure selected
- [ ] **COVID-distorted CAGRs are noted:** For industries impacted by COVID (parks, travel, hospitality), if CAGR spans 2020-2021, note distortion and provide normalized alternative
- [ ] **Projected growth rate is a SINGLE numerical CAGR** with source (not "5-7%" ranges, not "continued growth expected")
- [ ] Industry structure describes consolidation level and trend
- [ ] Industry life cycle stage identified **WITH approximate duration in phase** (e.g., "Mature (~20 years)")
- [ ] At least 3 key industry trends identified with **standardized impact ratings (HIGH/MEDIUM/LOW)**

## Section 2: Value Chain Economics

- [ ] Value chain map table has columns: Stage, Key Players, Margins, Profit Pool/Trend
- [ ] Value migration analysis identifies direction and drivers
- [ ] **Vertical integration dynamics section present** — discusses forward/backward integration by competitors and subject company
- [ ] Implications for subject company explicitly stated

## Section 3: Competitive Landscape

- [ ] Market share table has 10-year view (Current, 5yr Ago, 10yr Ago columns)
- [ ] If 10-year data unavailable, data limitation is explicitly noted
- [ ] **Market share percentages use whole numbers** — "70%" not "~70%"; add "[est.]" suffix if not sourced (e.g., "70% [est.]")
- [ ] **Market share arithmetic verified** — if claiming "top 3 = X%", sum of stated individual shares must equal X%
- [ ] At least 3 key competitors profiled in depth
- [ ] Each competitor profile includes: business model, strategy, **explicit geographic focus (regions/countries)**, **explicit customer segment focus**, strengths/weaknesses, recent moves, financials, management quality assessment
- [ ] **Competitor financials include 5-year revenue CAGR** — calculated with shown work OR sourced with verification, never "~" or ranges
- [ ] **All CAGRs in output are internally consistent** — no self-contradicting figures for the same company/period
- [ ] **Corporate vs. Systemwide CONSISTENCY:** For franchise companies, competitive comparison table uses CONSISTENT metric basis across all companies (all corporate OR all systemwide—not mixed)
- [ ] Competitive comparison table includes all major competitors
- [ ] **Competitive comparison table has NO tildes:** Market cap, revenue, margins, ROIC, P/E must be whole numbers or "N/A" — never "~$800B" or "~40%"
- [ ] Competitive response dynamics section **explicitly labeled** and covers: how competitors respond, cooperative vs hostile, price war history, financial health

## Section 4: Porter's Five Forces

- [ ] All five forces analyzed with evidence
- [ ] Each force has explicit rating (Low / Moderate / High)
- [ ] Five Forces summary table present with Force, Rating, Impact, Trend
- [ ] Overall industry attractiveness rating provided with justification

## Section 5: Adjacent & Emerging Threats

- [ ] Tech giant risk assessed (at least Amazon, Google considered)
- [ ] Private company / VC-backed threats assessed
- [ ] International player threats assessed
- [ ] Converging industries assessed
- [ ] Emerging threats summary table present with Probability, Timeline, Severity

## Output Quality

- [ ] Executive summary includes industry attractiveness rating and competitive position assessment
- [ ] **Executive Summary prose avoids approximations:** Verify summary doesn't use "~", "approximately", or ranges where formal sections use precise figures
- [ ] Watch list includes specific metrics/dynamics to monitor
- [ ] Sources section cites at least 5 external sources with HYPERLINKS in format `[Source Name](URL)`
- [ ] All financial figures have year/source attribution
- [ ] Estimates clearly flagged (e.g., "[est.]" or explanation)

---

## Common Failure Modes

| Issue | Check |
|-------|-------|
| Qualitative projected growth | Must be "X% CAGR" not "continued growth" |
| Range-based CAGRs | Must pick single figure (e.g., "5% CAGR" not "4-6% CAGR"); explain source selection if ranges exist |
| Missing vertical integration | Required subsection in Value Chain |
| Estimated 5yr CAGR | Must calculate or source; no "~8%" or "~25%" |
| Self-contradicting CAGRs | If footnote shows different calc than table, resolve before publishing |
| Missing competitor financial depth | Each profile needs revenue, margins, ROIC, 5yr CAGR |
| Vague converging industries | Need specific companies/signals, not just categories |
| Market share math error | Sum stated individual shares to verify aggregate claims |
| Missing trend impact ratings | Each trend needs HIGH/MEDIUM/LOW impact on subject company |
| Missing life cycle duration | "Mature" alone is insufficient; add "(~X years)" |
| Missing source hyperlinks | Sources section must have URLs in `[Name](URL)` format |
| Mixed corporate/systemwide metrics | Comparison table must use consistent basis for all companies |
| Industry CAGR as range | Must select single preferred figure with source justification |
| Segment passes not isolated | Run each material segment as an isolated pass; parallelize with Codex sub-agent orchestration when available |
| Same competitors for all segments | Each segment needs its own distinct competitive set |
| Segment TAMs identical | Each segment operates in a different market with different TAM |
| Missing overlap matrix | Required for multi-segment companies to show multi-front rivals |
| Missing segment variations in Five Forces | If forces differ by segment, must include Segment Variations table |

---

## 5-Year CAGR Validation Examples

| Format | Pass/Fail | Reason |
|--------|-----------|--------|
| "25% (FY2019-FY2024, annual reports)" | ✅ PASS | Calculated with source and time range |
| "31% CAGR (calculated: $674M to $2.6B over 5 years)" | ✅ PASS | Shows calculation basis |
| "CAGR unavailable; 3-year CAGR = 22% (FY2021-FY2024)" | ✅ PASS | States limitation, provides alternative |
| "~25%" | ❌ FAIL | Tilde estimate, no source |
| "approximately 18%" | ❌ FAIL | Approximate without calculation |
| "high single digits" | ❌ FAIL | Qualitative, not numerical |
| "19-23% annually" | ❌ FAIL | Range of YoY growth, not 5-year CAGR |
