# Phase 1: Competitive Landscape Synthesis Prompt

Use this reference for the synthesis pass for analyze-competitive-landscape.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are creating a Competitive Landscape Analysis for [COMPANY] ([TICKER]).

**Source Documents:**
- 10K Synthesis Memos: [10K_MEMO_PATHS]
- Scuttlebutt Analysis: [SCUTTLEBUTT_PATH]

**Output Directory:** [OUTPUT_DIR]
**Timestamp:** [TIMESTAMP]

---

## Your Task

Complete the full competitive landscape analysis workflow:

### Step 1: Read ALL Source Documents (REQUIRED FIRST)

**Read ALL 10K synthesis memos listed above.** Unlike other skills that use only the most recent memo, competitive landscape analysis benefits from ALL years because:
- Competitor mentions evolve over time
- Market share shifts become visible across years
- Risk factor language changes signal competitive dynamics
- Management positioning statements reveal strategic shifts

From the 10K memos, extract:
- Competitors mentioned, risk factors flagged, market segments discussed
- Management's stated positioning and competitive claims
- Historical changes in competitive language across years

**Read the scuttlebutt analysis.** Extract:
- Customer perspective on competitive alternatives
- Employee views on company vs. competitors
- Partner/supplier insights on market dynamics
- Stakeholder voices to integrate into competitive analysis

**CRITICAL:** These source documents inform WHERE to dig and WHAT to dig for. Verify claims independently via web research.

### Step 2: Segment Detection

Multi-segment companies require segment-level competitive analysis using focused passes.

**Trigger:** If 2+ segments each contribute ≥15% of total revenue, run separate segment passes.

**Detection Process:**
1. Read the most recent 10K synthesis memo
2. Parse YAML frontmatter `segments:` field
3. Calculate each segment's % of total revenue
4. If 2+ segments ≥15%, flag as multi-segment and proceed with Section 2B

**Examples:**
- JPMorgan Chase: CCB (40%), CIB (51%), AWM (10%) → Run 2 segment passes (CCB, CIB meet threshold)
- Apple: Products (78%), Services (22%) → Run 2 segment passes
- Costco: Warehouse (99%), Other (1%) → No separate segment passes needed (single segment dominates)

**If NOT multi-segment:** Skip Section 2B entirely and proceed directly to Section 3.

### Step 3: Read Templates

Read required templates:
- Output template: `.codex/skills/analyze-competitive-landscape/references/output-template.md`
- Validation checklist: `.codex/skills/analyze-competitive-landscape/references/validation-checklist.md`

### Step 4: Generate Analysis

Create the full analysis following the output template structure.

#### Section 1: Industry Overview

**Market Definition:**
- What industry/market does this company operate in?
- How do you define the relevant market boundaries?
- Are there distinct sub-segments?

**Market Size and Growth:**
- Total addressable market (TAM) size
- Historical growth rate (10 years if available) — **Must be a SINGLE numerical CAGR**, not qualitative or a range. If sources provide conflicting CAGRs, you MUST: (1) state the range found, (2) explain WHY sources differ (market definition, data methodology, time period), and (3) SELECT A SINGLE PREFERRED FIGURE with justification (e.g., "Using 4.5% CAGR from IBISWorld as preferred source due to consistent QSR market definition"). **NEVER output a range like "4-5% CAGR" as the final answer.**
- Projected growth rate (5-10 years) — **Must be a SINGLE numerical CAGR**, not qualitative or a range. Follow the same process: (1) if sources conflict, state the range, (2) explain discrepancy, (3) select single preferred figure with justification. **NEVER output a range like "3-6% CAGR" as the final answer.**
- What's driving growth or decline?

**Industry Structure:**
- Consolidated (few large players) or fragmented (many small players)?
- How has consolidation trended over 10-20 years?
- Are there distinct tiers of competitors?

**Industry Life Cycle:**
- Emerging / Growth / Mature / Declining?
- What phase of the cycle is this industry in?
- How long has it been in this phase? (Estimate in years: e.g., "Mature for ~15 years")
- **Duration estimate is REQUIRED** — Do not just state "Mature"; must include approximate years in current phase (e.g., "Mature (~20 years since early 2000s peak growth)")

**Key Industry Trends:**
- Technology changes
- Regulatory changes
- Customer behavior shifts
- Supply chain evolution
- Sustainability/ESG pressures
- Globalization/deglobalization effects

**For each trend, provide:**
- **Trend name:** Brief description
- **Impact on subject company:** HIGH / MEDIUM / LOW with 1-sentence explanation
- This standardized impact rating is REQUIRED for each trend identified

---

#### Section 2: Value Chain Economics

**Where does profit pool in this industry?**

Map the industry value chain and identify:
- Which stages capture the most profit margin?
- Where is value concentrating or migrating?
- Is the company positioned at a favorable point?

**Value Chain Map:**

| Stage | Key Players | Typical Margins | Trend |
|-------|-------------|-----------------|-------|
| Raw Materials/Inputs | ... | ...% | Stable/Growing/Shrinking |
| Manufacturing/Production | ... | ...% | ... |
| Distribution | ... | ...% | ... |
| Retail/End Customer | ... | ...% | ... |

**Value Migration Analysis:**
- Is value migrating up or down the chain?
- Are intermediaries being disintermediated?
- Is the company's position improving or deteriorating?
- What's driving value migration (technology, regulation, customer preferences)?

**Vertical Integration Dynamics:** (Required subsection — do not omit)
- Are competitors integrating forward (toward end customers) or backward (toward suppliers/manufacturing)?
- Is the subject company integrating? How does this affect competitive position?
- What are the risks of supplier or customer integration into the company's space?

---

#### Section 2B: Segment Focused Pass Orchestration (Multi-Segment Only)

**Skip this section if segment detection criteria not met.** Proceed directly to Section 3.

For each material segment (>=15% of revenue), run a focused segment-analysis pass with the following prompt template:

##### Segment Focused Pass Prompt Template

```
You are analyzing the competitive landscape for ONE business segment of [Company].

**Segment:** [Segment Name]
**Segment Revenue:** $[X]B ([Y]% of total company revenue)
**Segment Description:** [From 10K memo]

Your task: Research the competitive landscape for THIS SEGMENT ONLY. Do not analyze other segments of the company.

**Deliverables (structured output):**

## [Segment Name] Competitive Analysis

### Segment Market
| Metric | Value |
|--------|-------|
| Segment TAM | $...B (with source) |
| Historical Growth | X% CAGR (FY20XX-FY20XX, source) |
| Projected Growth | X% CAGR (source) |
| Industry Life Cycle | [Phase] |

### Segment-Specific Competitors

Identify 3-5 competitors who compete PRIMARILY in this segment (not just overall company competitors).

| Competitor | Why They Compete Here | Relative Strength |
|------------|----------------------|-------------------|
| [Competitor 1] | [Specific segment overlap] | Strong/Moderate/Weak |
| [Competitor 2] | ... | ... |
| [Competitor 3] | ... | ... |

### Segment Market Share
| Player | Share | Trend | Notes |
|--------|-------|-------|-------|
| [Company] | X% | ↑/↓/→ | ... |
| [Competitor 1] | X% | ... | ... |
| [Competitor 2] | X% | ... | ... |

### Segment Competitive Dynamics
- [Dynamic 1: What's unique about competition in THIS segment]
- [Dynamic 2: Key success factors in THIS segment]
- [Dynamic 3: How this segment differs from other company segments]

### Segment-Specific Threats
- [Threat 1: Emerging threat to THIS segment specifically]
- [Threat 2: ...]

**IMPORTANT:** Use current web research to research this specific segment market. Do NOT analyze other segments of the company. Output should be 400-600 words.
```

##### Focused Pass Execution

1. **Run all segment passes independently:** Use Codex sub-agent orchestration when available; otherwise perform the segment passes sequentially.
2. Each segment pass uses web search to research its specific segment market
3. **Collect outputs from all segment passes** before proceeding
4. Proceed to Section 3 synthesis once all outputs are received

**Focused Pass Constraints:**
- Each segment pass should complete in 3-5 turns
- Output should be ~400-600 words per segment
- Segment passes must NOT analyze other segments

---

#### Section 3: Competitive Landscape

**For multi-segment companies:** This section synthesizes segment pass outputs from Section 2B.

**Segment Overview Table (Multi-Segment Only):**

Before the consolidated market share analysis, include a segment overview:

| Segment | Revenue | % Total | TAM | Growth | Primary Competitors |
|---------|---------|---------|-----|--------|---------------------|
| [Seg 1] | $...B | X% | $...B | X% | [Comp A], [Comp B] |
| [Seg 2] | $...B | X% | $...B | X% | [Comp C], [Comp D] |

**Per-Segment Competitive Analysis (Multi-Segment Only):**

Insert each segment pass output here, one section per segment.

**Competitor Overlap Matrix (Multi-Segment Only):**

| Competitor | [Seg 1] | [Seg 2] | [Seg 3] | Multi-Segment? |
|------------|---------|---------|---------|----------------|
| [Comp A] | Primary | — | — | No |
| [Comp B] | — | Primary | Secondary | Yes |

**Multi-Segment Rivals:** Competitors marked "Yes" compete across multiple segments and warrant deeper profiling.

---

**Market Share Analysis (10-Year View):**

| Company | Current Share | 5yr Ago | 10yr Ago | Trend | Key Strength |
|---------|---------------|---------|----------|-------|--------------|
| [Subject Company] | ...% | ...% | ...% | ↑/↓/→ | ... |
| Competitor 1 | ...% | ...% | ...% | ↑/↓/→ | ... |
| Competitor 2 | ...% | ...% | ...% | ↑/↓/→ | ... |
| Competitor 3 | ...% | ...% | ...% | ↑/↓/→ | ... |
| Others | ...% | ...% | ...% | — | Fragmented |

**Data Availability Note:** If 10-year historical data is unavailable, provide the longest time series available and note the limitation.

**Market Share Trajectory Analysis:**
- Who is gaining share? Why?
- Who is losing share? Why?
- Is the industry consolidating or fragmenting?
- What predicts future share shifts?

**Key Competitors Deep Dive:**

**For multi-segment companies:** Profile competitors who either (a) compete across multiple segments (marked "Yes" in Overlap Matrix), or (b) are the #1 competitor in a major segment.

For each major competitor (3-5), analyze:
- **Segment Focus:** Which segment(s) this competitor competes in (multi-segment companies only)
- Business model and strategy
- Geographic focus
- Customer segment focus
- Key strengths and weaknesses
- Recent strategic moves (M&A, new products, market entry)
- Financial comparison (revenue, margins, growth, ROIC) — **5-year revenue CAGR is required**, not just YoY growth. Calculate or source from financial databases/press releases; do not estimate with tildes (~)
- Management quality and track record (brief assessment: tenure, reputation, capital allocation history)

> **⚠️ STOP: Before writing competitor financials**
> You MUST calculate or source exact 5-year CAGRs. Tilde estimates (~21%, ~25%) are NOT acceptable and will fail validation. See "Calculating 5-Year Revenue CAGR" in Data Quality section. If data is unavailable, state "CAGR unavailable; [N]-year CAGR = X% (FY20XX-FY20XX)".

**Competitive Comparison Table:**

| Metric | [Company] | Comp 1 | Comp 2 | Comp 3 |
|--------|-----------|--------|--------|--------|
| Revenue | $... | $... | $... | $... |
| Revenue Growth (5yr CAGR) | X% (FY20XX-FY20XX) | X% (FY20XX-FY20XX) | X% (FY20XX-FY20XX) | X% (FY20XX-FY20XX) |
| Gross Margin | ...% | ...% | ...% | ...% |
| Operating Margin | ...% | ...% | ...% | ...% |
| ROIC | ...% | ...% | ...% | ...% |
| Market Cap | $... | $... | $... | $... |
| P/E Ratio | ...x | ...x | ...x | ...x |

*Note: Revenue Growth MUST include year range and be calculated/sourced—not estimated. Format: "21% (FY2020-FY2025, from annual reports)"*

**Notes:**
- Use "N/A" with brief explanation when metrics are not applicable or unavailable
- If segment vs. standalone confusion exists, note this clearly
- For ROIC, specify methodology if using different capital bases

**Competitive Response Dynamics:** (Required subsection — do not omit)
- How do competitors typically respond to competitive moves?
- Is this a cooperative or hostile competitive environment?
- History of price wars or irrational behavior?
- Competitor financial health (can they sustain a fight?)

---

#### Section 4: Porter's Five Forces

Analyze each force and its impact on industry profitability:

**1. Threat of New Entrants**
- Barriers to entry (capital, technology, regulation, brand, scale, distribution)
- Recent new entrants and their success/failure
- How easy is it to start a competing business?
- What would a well-funded new entrant need to do?

**Rating:** Low / Moderate / High threat

**2. Bargaining Power of Suppliers**
- Supplier concentration
- Switching costs for inputs
- Importance of the company to suppliers
- Threat of forward integration
- Availability of substitutes for inputs

**Rating:** Low / Moderate / High power

**3. Bargaining Power of Buyers**
- Customer concentration
- Switching costs for customers
- Price sensitivity
- Importance of product to customers
- Threat of backward integration
- Information availability to buyers

**Rating:** Low / Moderate / High power

**4. Threat of Substitutes**
- What alternatives exist?
- Price-performance of substitutes
- Switching costs to substitutes
- Customer propensity to switch
- Emerging substitutes on the horizon

**Rating:** Low / Moderate / High threat

**5. Competitive Rivalry**
- Number and size of competitors
- Industry growth rate
- Product differentiation
- Exit barriers
- Price competition intensity
- Capacity utilization in industry

**Rating:** Low / Moderate / High rivalry

**Five Forces Summary:**

| Force | Rating | Impact on Profitability | Trend |
|-------|--------|------------------------|-------|
| New Entrants | ... | ... | Improving/Stable/Worsening |
| Supplier Power | ... | ... | ... |
| Buyer Power | ... | ... | ... |
| Substitutes | ... | ... | ... |
| Rivalry | ... | ... | ... |

**Overall Industry Attractiveness:** Highly Attractive / Attractive / Neutral / Unattractive / Highly Unattractive

**Segment Variations (Multi-Segment Only):**

For multi-segment companies, note where forces differ materially by segment:

| Force | Segment | Variation |
|-------|---------|-----------|
| [Force] | [Segment] | [How it differs from consolidated view] |

---

#### Section 5: Adjacent & Emerging Threats

**Tech Giant Risk:**
- Which tech giants (Amazon, Google, Apple, Microsoft, Meta) could enter this space?
- Have any shown interest? What signals exist?
- What advantages would they bring?
- How have incumbents fared when tech giants enter adjacent industries?

**Private Company Threats:**
- Well-funded private companies or startups in this space?
- Venture capital activity and funding trends
- Who are the "ones to watch"?
- What approaches are they taking?

**International Players:**
- Foreign competitors not yet in this market?
- Emerging market competitors with cost advantages?
- Cross-border competitive dynamics
- Trade/tariff implications

**Converging Industries:**
- Adjacent industries that could expand into this space?
- Industry boundaries blurring?
- Companies from other industries eyeing entry?

**Emerging Threats Summary:**

| Threat | Source | Probability | Timeline | Severity |
|--------|--------|-------------|----------|----------|
| ... | Tech giants | Low/Med/High | 1-3yr/3-5yr/5+yr | Low/Med/High |
| ... | Private/VC | ... | ... | ... |
| ... | International | ... | ... | ... |
| ... | Adjacent | ... | ... | ... |

---

### Step 5: Pre-Output Validation

**Before finalizing the analysis, verify these critical items:**

#### Tilde & Approximation Check (CRITICAL)

**Run this check across the ENTIRE document before output:**

1. [ ] **Search for "~" character:** If ANY percentage uses "~" (e.g., "~7%", "~25%"), STOP and fix
2. [ ] **Search for "approximately":** If ANY growth rate uses "approximately", STOP and fix
3. [ ] **Search for ranges in single-value fields:** If a CAGR shows "4-6%" where a single value is required, STOP and select one figure

This applies to ALL numerical estimates, including:
- Industry historical and projected CAGRs
- Competitor 5-year revenue CAGRs
- Market share percentages
- Margin estimates

#### CAGR Reconciliation Check (CRITICAL)

**Before output, verify internal consistency:**

1. [ ] **Search for each company name** and verify all CAGRs mentioned for that company are consistent
2. [ ] **If the same CAGR appears in multiple places** (competitor profile table AND competitive comparison table), verify they match exactly
3. [ ] **If you calculate a CAGR in a footnote or note**, verify it matches the table cell it references
4. [ ] **Resolve any conflicts BEFORE outputting** — pick one figure and use it consistently throughout

#### Content Requirements Check

1. [ ] **5-Year CAGRs:** Every competitor revenue growth figure uses format "X% (FY20XX-FY20XX)" — NO tildes, NO approximations
2. [ ] **Historical Industry CAGR:** Market Size table includes explicit "Historical Growth (10yr) = X% CAGR" with source — SINGLE figure, not range
3. [ ] **Projected Industry CAGR:** Numerical CAGR with source, not qualitative language — SINGLE figure, not range
4. [ ] **Market Share Percentages:** If using estimates, use whole numbers without tildes (e.g., "70%" not "~70%"); note as "[est.]" if not sourced
5. [ ] **Vertical Integration:** Section explicitly present in Value Chain Economics
6. [ ] **Trend Impact Ratings:** Every industry trend has HIGH / MEDIUM / LOW rating
7. [ ] **Industry Life Cycle Duration:** Phase includes approximate years
8. [ ] **Competitive Response Dynamics:** Section explicitly present in Competitive Landscape

If any check fails, STOP and fix before outputting.

### Step 6: Write Output

Write analysis to:
```
[OUTPUT_DIR]/Competitive Landscape - Analysis - [COMPANY] - [TIMESTAMP].md
```

---

## Data Quality & Methodology Notes

**Handling Unavailable Data:**
- Use "N/A" with brief explanation when metrics don't apply to certain business models
- Note entity type clearly (e.g., "Eurex is a segment of Deutsche Borse, not standalone")
- When historical data is incomplete, state available time range and supplement with qualitative analysis

**Financial Comparison Requirements:**
- Revenue Growth must be 5-year CAGR, not just YoY — calculate from actual revenue figures or cite source; do not estimate with "~"
- ROIC methodology must be specified when comparing companies with different capital structures
- Gross Margin: If exchanges don't report separately, note "N/A (reported as part of operating margin)"
- When competitor is a segment of a larger company, note what metrics are available at segment level vs. unavailable

**Data Recency:**
- Use most recent available data from web research (press releases, earnings)
- Note when web-sourced data differs from 10-K prerequisite data

**COVID-Distorted Data Handling:**
- For industries severely impacted by COVID-19 (theme parks, travel, hospitality, live events, airlines):
  - If calculating a CAGR that spans 2020-2021, note the distortion explicitly
  - Provide BOTH the raw CAGR AND a normalized view (e.g., "Normalized: 3-4% CAGR using 2019 as base")
  - When selecting a single preferred figure, use the normalized CAGR as the primary figure if the COVID period materially distorts the data

**Calculating 5-Year Revenue CAGR (Required for Each Competitor):**

The skill REQUIRES calculated 5-year CAGRs, not estimates. Follow this process:

1. **Search for historical revenue:** Query "[Company] revenue 2020 2021 2022 2023 2024" or "[Company] annual report revenue history"
2. **Identify revenue figures for Year 0 and Year 5:** e.g., HubSpot FY2019 revenue = $674M, FY2024 revenue = $2.6B
3. **Calculate CAGR using formula:** CAGR = (Ending Value / Beginning Value)^(1/5) - 1
   - Example: ($2.6B / $0.674B)^(1/5) - 1 = 31% CAGR
4. **State the result with source:** "31% (FY2019-FY2024, from annual reports)"

**DO NOT:**
- Use tilde estimates (~25%, ~18%) — these violate the skill requirement
- Use single-year YoY growth as a proxy for 5-year CAGR
- Guess or interpolate when data is unavailable

**If precise 5-year data is unavailable:**
- State "5-year CAGR unavailable; [N]-year CAGR = X% (FY20XX-FY20XX)"
- Or state "CAGR not calculable; YoY growth for reference: FY2024 +X%, FY2023 +Y%"
- Never substitute a tilde estimate

**CAGR Calculation Verification (REQUIRED):**

Before including any CAGR in the output, verify it by:

1. **Show your work:** Include the actual calculation with starting and ending values
2. **Verify arithmetic:** CAGR = (End/Start)^(1/years) - 1 — re-check the math
3. **Cross-check with source:** Ensure the CAGR matches any source-provided CAGR
4. **Resolve conflicts:** If your calculation differs from a source, explain the discrepancy
5. **Never include self-contradicting figures:** If multiple CAGRs are mentioned for the same company, they must be for different periods with clear labels
6. **Corporate vs. Systemwide consistency:** For franchise companies, be explicit about whether revenue figures are corporate revenue or systemwide sales. The competitive comparison table must use CONSISTENT metrics across all companies

**Source Documentation:**
- All market share claims require sources
- Financial comparisons must cite source (annual report, earnings release, analyst estimate)
- Market share arithmetic must verify (e.g., if claiming "top 3 = 93%", sum the stated shares)

---

## Guidelines

**Define the Market Correctly:** A company can look dominant in a narrow market or weak in a broad market. Be thoughtful about market boundaries.

**Use Data:** Market share claims need sources. Financial comparisons need numbers. 10-year trends where possible.

**Be Objective About Competitors:** Understand competitor strengths, not just weaknesses.

**Think Like an Attacker:** What would a well-funded competitor do to take share?

**Don't Skip Emerging Threats:** The most dangerous competitors may not be on the radar yet.

**Connect to Moat Strength:** This external landscape analysis pairs with `$analyze-moat-strength` which analyzes the company's internal defenses.

---

## Tool Usage

- **Read:** Use for reading 10K memos, scuttlebutt analysis, template files, and checklists
- **Write:** Use for saving the output analysis
- **Web search:** Use for researching competitors, market share, industry data
- **File search pattern:** Use for finding additional research files if needed
- **Codex sub-agent coordination:** Use only if Codex sub-agent orchestration is available; otherwise perform the segment passes sequentially (multi-segment companies only)

---

## Return Value

When complete, return a JSON object:
```json
{
  "output_file_path": "[path to written analysis]",
  "source_memos": ["/path/to/10k-memo-1.md", "/path/to/10k-memo-2.md"],
  "scuttlebutt_path": "/path/to/scuttlebutt.md",
  "status": "success" | "partial" | "failed",
  "notes": "[any issues encountered]"
}
```

The `source_memos` and `scuttlebutt_path` fields are CRITICAL — Phase 2 QC will use these to re-read the source documents.
```
