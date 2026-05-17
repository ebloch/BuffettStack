# Annual Filing Synthesis Output Template (Hybrid)

This hybrid format combines:
- **YAML frontmatter** — Structured metadata for filtering/search
- **Prose-driven body** — Narrative sections for comprehension and token efficiency
- **Tracking tables** — Promises to Track, Claims to Verify from new format

Target: ~300-350 lines, ~2,700-3,100 tokens per memo.

---

## Source Reference Guidelines

Include page references `(p.XX)` for:
- Direct quotes from management
- Specific numerical claims not from financial tables
- Risk factors highlighted
- All entries in "Promises to Track" and "Claims to Verify"

---

## Number Format Rules

| Context | Format | Example |
|---------|--------|---------|
| Tables (all) | M suffix, no $ | `4272M` |
| Prose | Full currency | `$4.3 billion` |
| Percentages | One decimal | `21.4%` |
| Per-share | $ + two decimals | `$53.11` |
| YoY changes | Sign prefix | `+21.4%` |

---

## YAML Frontmatter

```yaml
---
type: 10k-synthesis
company: [Company Name]
ticker: [TICKER]
fiscal_year: [YYYY]
fiscal_year_end: [YYYY-MM-DD]
filing_date: [YYYY-MM-DD]
synthesis_date: [YYYY-MM-DD]
form_type: [10-K|20-F|40-F|URD|UK-ANNUAL-REPORT|INTEGRATED-REPORT]  # Type of annual filing
regulator: [SEC|AMF|FCA|FSA|null]  # SEC for US filings, AMF for French URDs, FCA for UK filings, FSA for Japanese filings
accounting_standard: [GAAP|IFRS]  # GAAP for US 10-K/20-F (most), IFRS for European filings and 40-F
reporting_currency: [USD|EUR|GBP|JPY|null]  # Reporting currency; null for USD-denominated filings
industry: [industry-slug]  # insurance, saas, exchange, reit, bank, manufacturing, platform, ota, media-entertainment, aircraft-leasing, luxury-goods

# Key metrics (M = millions, numbers only)
metrics:
  revenue_m: [number]
  operating_income_m: [number]
  net_income_m: [number]
  fcf_m: [number]
  employees: [number]
  # Add 2-4 industry-specific metrics (REQUIRED):
  # Insurance: combined_ratio, gpw_m, npw_m, book_value_per_share
  # Bank: nim_pct, cet1_ratio, npl_ratio
  # SaaS: arr_m (null if not disclosed), net_retention_pct (null if not disclosed), gross_retention_pct (derive from attrition if needed), gross_margin_pct, rpo_m, crpo_m, rule_of_40
  # Traditional REIT: ffo_m, affo_m, occupancy_pct
  # Tower REIT (AMT, CCI, SBAC): ffo_m, affo_m, churn_pct, site_count, adjusted_ebitda_m
  # Exchange: adv_contracts_m, average_rpc, electronic_volume_pct
  # OTA: gross_bookings_m, take_rate_pct
  # Aircraft Leasing: fleet_owned_count, fleet_avg_age_years, utilization_rate_pct, adjusted_debt_to_equity, book_value_per_share
  # Media/Entertainment: streaming_subs_total_m, streaming_arpu_domestic, streaming_dtc_operating_income_m, content_assets_m, content_amortization_m, content_impairments_m, parks_attendance_change_pct, parks_per_cap_change_pct

# Ratings (for insurers, banks, debt issuers, aircraft lessors — omit if N/A)
ratings:
  am_best: [rating or null]
  sp: [rating or null]
  moodys: [rating or null]
  fitch: [rating or null]  # Include if rated (common for aircraft lessors)
  outlook: stable|positive|negative|null

# Segments (top 3-5)
segments:
  - name: [Segment 1]
    revenue_m: [number]
    pct_total: [number]
  - name: [Segment 2]
    revenue_m: [number]
    pct_total: [number]

# Strategic investments (simplified — detail in body if material)
# NOTE: ownership_pct MUST be a numeric value (e.g., 28.4) if disclosed in the 10-K
# Search "equity method" or "investment" notes for ownership percentages
# If ownership % not disclosed, use null and note in body: "Ownership %: Not disclosed"
affiliates:
  - name: [Affiliate name]
    ownership_pct: [number or null if not disclosed]
    income_contribution_m: [number or "Part of $XM equity method income"]

# Capital allocation & flexibility
capital:
  buyback_auth_remaining_m: [number or null]  # Dollar value remaining, NOT share count. Search Item 5 or proxy for authorization. If truly not disclosed, use null AND add "Buyback auth: Not disclosed in 10-K" to Capital Allocation commentary
  buyback_deployed_fy_m: [number or null]  # Dollar value deployed THIS fiscal year
  dividends_paid_m: [number or null]  # Total dividends (common + preferred) paid THIS fiscal year
  total_debt_m: [number]  # For holding companies: corporate recourse debt only
  total_consolidated_debt_m: [number or null]  # For holding companies: include non-recourse
  capital_priorities: [list of 1-3 stated priorities]

# Share count & dilution
shares:
  basic_m: [number]
  diluted_m: [number]
  options_rsus_m: [number]
  dilution_pct: [number]

# Quality flags
quality:
  disclosure: good|adequate|poor
  accounting: clean|concerns|red-flags

# Risk tags (for filtering)
risk_tags:
  - [risk-tag-slug]
  - [risk-tag-slug]
---
```

---

# [Company] — FY[Year] [10-K|20-F|40-F] Synthesis

---

## Key Takeaways

Write 5-7 narrative bullets with **bold lead-ins**. Each bullet should provide insight + supporting data. Most important insights first. **Add inline topic tags** `[TAG-SLUG]` at the end of bullets for cross-referencing.

- **[Lead-in phrase]:** [Narrative insight with specific data points, not just restating metrics. Connect the numbers to what they mean for the business.] `[TAG-SLUG]`

- **[Lead-in phrase]:** [Another key insight. Focus on what changed, what matters, what's surprising or confirms/contradicts thesis.] `[TAG-SLUG]`

- **[Lead-in phrase]:** [Continue with material insights only. No filler bullets.] `[TAG-SLUG]`

*Each bullet: one key insight, 1-2 sentences. No redundancy with later sections. Focus on "so what?" not just "what." Include inline tags for Topic Index cross-referencing.*

**REQUIRED for OTAs/Platforms/Exchanges:** One bullet MUST explicitly state the Revenue vs. GMV (or Revenue vs. Volume) growth differential. Example: "**Take rate expansion signals pricing power:** Revenue grew +13.4% vs. gross bookings +12.4%, a 100bps take rate expansion driven by merchant model shift and payment facilitation revenue."

**REQUIRED for Alternative Asset Managers:** One bullet MUST explicitly state the FBC quality/duration profile. Example: "**High-quality fee base provides stability:** 87% of $539B fee-bearing capital is long-dated or perpetual, minimizing redemption risk compared to liquid alt peers."

---

## Business Summary

[2-3 paragraphs describing what the company does and how it makes money. Write as flowing prose — explain the business model, competitive position, and economic engine in narrative form. Weave in industry-specific context.]

**Segments:**

| Segment | Revenue | % Total | YoY | Op Margin |
|---------|---------|---------|-----|-----------|
| [Segment 1] | [X]M | [X]% | [+X%] | [X.X]% |
| [Segment 2] | [X]M | [X]% | [+X%] | [X.X]% |

*Segment operating margin is REQUIRED if disclosed in MD&A (typically in Operations Review by segment). Check each segment's discussion for operating income and calculate margin. If segment operating income/margin not disclosed, note "Segment margins not disclosed" below the table.*

*For insurers: Use NPW (Net Premiums Written) as Revenue. Add separate NPW by Segment table if NPW differs materially from NPE. If GPW not disclosed, note "GPW: Not disclosed separately."*

*For single-segment companies: If company reports as single segment, note "Single reportable segment" and describe asset/product breakdown if available (e.g., aircraft types, asset classes). Do NOT fabricate approximate segment values — use only disclosed figures.*

*For holding companies/asset managers with non-comparable segment metrics (DE, FFO, DOE, NOI):*
- **Option 1:** Use separate tables for each metric type
- **Option 2:** Single table with explicit footnote: "Metrics are not directly comparable — Asset Management uses DE, Operating Businesses use FFO, Real Estate uses NOI. Percentages show contribution to total earnings."

*For other industries: Omit margin column if not disclosed. Note: "Segment margins not disclosed."*

**Geographic mix:** [Region breakdown if disclosed, or "Not disclosed"]

**Concentration:** [Customer/supplier concentration, or "No single customer >10%"]

**Strategic investments:** [For material equity method investments — name, ownership %, income contribution. If none material, state "None material."]

---

## What Changed This Year

Simple bullet list of material changes. No tags, no formatting complexity.

- [Change 1 — be specific: what changed, by how much, why it matters]
- [Change 2]
- [Change 3]
- [Regulatory/competitive changes if material]
- [Acquisitions, divestitures, product launches/exits]
- [No material accounting changes] *or* [Material accounting changes: X]

---

## Management Commentary

> "[Direct quote from CEO/CFO letter or MD&A — choose the quote that best captures management's priorities]" (p.XX)

**Key points from management:**
- [Management priority or claim 1 — paraphrase or brief quote]
- [Priority 2]
- [Priority 3]
- [Tone/sentiment observation if notable]

*Focus on what management emphasizes, what they're defensive about, what promises they're making.*

---

## Guidance & Promises

**Guidance:**

| Metric | FY[Year+1] Target | Specificity |
|--------|-------------------|-------------|
| [Metric 1] | [Target] | High/Med/Low |
| [Metric 2] | [Target] | High/Med/Low |

*Specificity: High = explicit number, Med = range or directional, Low = qualitative only*

**Promises to Track:**

| Promise | Quote | Source | Verify By |
|---------|-------|--------|-----------|
| [Short description] | "[Exact quote]" | p.XX | [Q/FY] |
| [Short description] | "[Exact quote]" | p.XX | [Q/FY] |

*Minimum 2 trackable promises with page references. If none found, state: "No specific trackable promises — management commentary was qualitative."*

**Claims to Verify:**

| Claim | Quote | Source | How to Verify |
|-------|-------|--------|---------------|
| [Short description] | "[Exact quote]" | p.XX | [External data source] |
| [Short description] | "[Exact quote]" | p.XX | [External data source] |

*Forward-looking assertions needing external validation — market conditions, competitive position, trends management claims but can't control.*

---

## Financial Snapshot

**P&L & Returns:**

| Metric | FY[Year] | FY[Year-1] | Change |
|--------|----------|------------|--------|
| Revenue | [X]M | [X]M | [+X%] |
| Gross Profit | [X]M | [X]M | [+X%] |
| Gross Margin | [X]% | [X]% | [+Xbps] |
| Operating Income | [X]M | [X]M | [+X%] |
| Net Income | [X]M | [X]M | [+X%] |
| EPS (Diluted) | $[X.XX] | $[X.XX] | [+X%] |
| EPS (per ADS)* | $[X.XX] | $[X.XX] | [+X%] |
| Operating Margin | [X]% | [X]% | [+Xbps] |
| ROIC | [X]% | [X]% | [+Xbps] |
| Cash from Operations | [X]M | [X]M | [+X%] |
| FCF | [X]M | [X]M | [+X%] |
| FCF Conversion | [X]% | [X]% | FCF / Net Income |

*FCF Conversion: For loss-making companies with positive FCF, show FCF Margin (FCF/Revenue) instead. Note: "FCF Conversion: N/A (net loss); FCF Margin: X.X%"*

*EPS (per ADS) row: Include ONLY for 20-F filers with ADR programs (e.g., TSM, BABA). Note the ADS ratio in the table footnote (e.g., "1 ADS = 5 ordinary shares"). Omit row for standard 10-K filers.*

*Gross Margin is particularly important for OTAs/platforms with merchant models where payment facilitation costs affect margin. ROIC shows capital efficiency — critical for asset-light businesses.*

*For payment networks (Visa, Mastercard, etc.): Gross margin is typically N/A or near 100% because costs (personnel, technology, client incentives) are classified as operating expenses, not COGS. Either omit the Gross Profit/Margin rows OR note: "Gross Margin: N/A — network model; costs are operating expenses." Do NOT show Gross Profit = Revenue as this is confusing.*

*ROIC calculation (REQUIRED format): Show explicit formula with ALL components. CRITICAL: The calculation must reconcile — do NOT show inconsistent numbers.*

**Step-by-step process:**
1. Calculate NOPAT: Operating Income × (1 - Effective Tax Rate)
2. Calculate Invested Capital for each year: Total Equity + Total Debt - Cash
3. Calculate Average Invested Capital: (Beginning IC + Ending IC) / 2
4. Calculate ROIC: NOPAT / Average Invested Capital

**Footnote format:**
```
ROIC = NOPAT $X,XXXM (Op Inc $X,XXXM × (1 - XX.X% tax rate)) / Avg Invested Capital $XX,XXXM = XX.X%
Where: Avg IC = (Beginning IC $XX,XXXM + Ending IC $XX,XXXM) / 2
```

*The ROIC in the table MUST equal the footnote calculation. If they differ, recalculate.*

*For capital-light businesses (asset managers, platforms): If ROIC isn't meaningful, note: "ROIC: Not calculated — capital-light fee business; return measured via DE/FRE growth rate"*

*For capital-intensive leasing businesses (aircraft, equipment): Operating Cash Flow is typically the primary metric. FCF may not be meaningful if asset sales are included in investing activities. If FCF is misleading for the business model, note: "FCF: Not meaningful — asset sales/purchases are core operations" and include OCF with brief explanation.*

**Balance Sheet:**

| Metric | FY[Year] | FY[Year-1] | Notes |
|--------|----------|------------|-------|
| Cash & Equivalents | [X]M | [X]M | |
| Total Debt | [X]M | [X]M | |
| Net Debt | [X]M | [X]M | |
| Net Debt / EBITDA | [X.X]x | [X.X]x | Net Debt $XXXM / EBITDA $XXXM |
| Interest Coverage | [X.X]x | [X.X]x | EBIT $XXXM / Int Exp $XXXM |

*For aircraft/equipment lessors: Use Adjusted Debt-to-Equity as primary leverage metric (industry standard). Include Net Debt / EBITDA if calculable, but debt-to-equity is more relevant for matching assets and liabilities.*

*For holding companies with recourse vs. non-recourse debt: Calculate Net Debt / EBITDA at corporate level (recourse debt only). Note: "Net Debt / EBITDA (Corporate): X.Xx — excludes $XXB non-recourse debt at subsidiaries"*

*REQUIRED format for Net Debt / EBITDA: Show calculation in Notes column: "Net Debt $X,XXXM / EBITDA $X,XXXM". If EBITDA not stated, note: "EBITDA = Op Inc $XM + D&A $XM".*

*REQUIRED format for Interest Coverage: Show calculation in Notes column: "EBIT $X,XXXM / Interest Expense $XXXM". Never use approximations like ">10x".*

**Debt structure:** [1-2 sentences — MUST include: (1) total debt composition, (2) weighted avg maturity if disclosed, (3) **near-term maturities with amounts** (e.g., "$500M due 2025, $1.2B due 2026"). If maturity schedule not disclosed, note: "Detailed maturity schedule: Not disclosed in 10-K"]

*Working capital days (inventory, receivables, payables) are captured in YAML metrics section per industry checklist. When calculating, show formulas used:*
- *Inventory Days = (Avg Inventory ÷ COGS) × 365*
- *Receivables Days = (Avg Receivables ÷ Revenue) × 365*
- *Payables Days = (Avg Payables ÷ COGS) × 365*

**Alternative Asset Manager Tables (REQUIRED for BX, BN, KKR, APO, CG, ARES):**

*Carried Interest:*

| Metric | FY[Year] | FY[Year-1] | Notes |
|--------|----------|------------|-------|
| Realized Carried Interest | [X]M | [X]M | Cash received |
| Unrealized Carried Interest | [X]M | [X]M | Balance sheet accrual (if disclosed) |
| Funds in Carry Position | [X]% | [X]% | % of mature funds exceeding hurdle |

*If unrealized carry not disclosed, state "Unrealized carry: Not disclosed in 10-K." Hurdle rate typically 7-8% preferred return; note if disclosed.*

*Fundraising & Deployment:*

| Metric | FY[Year] | FY[Year-1] | Notes |
|--------|----------|------------|-------|
| Capital Raised | [X]B | [X]B | Annual fundraising |
| Uncalled Commitments | [X]B | [X]B | Dry powder |
| Capital Deployed | [X]B | [X]B | Investments made |
| Fee Rate (Implied) | [X.X]% | [X.X]% | Fee Revenue / FBC |

*Fee Rate calculation: Fee Revenue / Fee-Bearing Capital. This metric reveals fee compression trends — if FBC is growing faster than fee revenue, fees are compressing.*

**Insurance-Specific Tables (REQUIRED for P&C insurers):**

*Combined Ratio Components:*

| Component | FY[Year] | FY[Year-1] | Change |
|-----------|----------|------------|--------|
| Loss & Loss Expense Ratio | [X.X]% | [X.X]% | [+/-X.Xpts] |
| Policy Acquisition Cost Ratio | [X.X]% | [X.X]% | |
| Administrative Expense Ratio | [X.X]% | [X.X]% | |
| **P&C Combined Ratio** | **[X.X]%** | **[X.X]%** | |
| Catastrophe Losses (impact) | ([X.X])% | ([X.X])% | |
| Prior Period Development | [X.X]% | [X.X]% | Favorable = positive |
| **CAY Combined Ratio ex-Cat** | **[X.X]%** | **[X.X]%** | Core underwriting margin |

*Prior Year Reserve Development:*

| Segment | Favorable/(Adverse) | $ Amount | Points Impact |
|---------|---------------------|----------|---------------|
| [Segment 1] | Favorable/Adverse | [X]M | [+/-X.X]pts |
| [Segment 2] | Favorable/Adverse | [X]M | [+/-X.X]pts |
| **Total** | | [X]M | [+/-X.X]pts |

*If segment-level PYD not disclosed, state "Segment-level PYD: Not disclosed" and provide consolidated total.*

**Watch Items (REQUIRED for OTAs/Platforms/Exchanges):**

Review industry checklist watch items and flag any concerning trends:
- Take rate / RPC: [Expanding/Stable/Compressing] — [X]bps YoY
- GMV vs. Revenue growth: [Revenue outpacing/in-line/lagging] GMV
- Direct booking mix: [Improving/Stable/Degrading]
- [Any other watch item flagged]

*If no concerning trends, state: "Watch Items: No concerning trends identified — take rate expanding, direct mix stable."*

**Traditional REIT Tables (REQUIRED for O, NNN, WPC, VICI, and similar net-lease/property REITs):**

*REIT-Specific Metrics:*

| Metric | FY[Year] | FY[Year-1] | Notes |
|--------|----------|------------|-------|
| Same-Store Growth | [X.X]% | [X.X]% | Revenue or NOI (specify) |
| Occupancy | [X.X]% | [X.X]% | |
| Rent Recapture/Spreads | [X.X]% | [X.X]% | New vs. renewal if disclosed |
| WALT | [X.X] years | [X.X] years | Weighted avg lease term |
| AFFO Payout Ratio | [X.X]% | [X.X]% | Dividends / AFFO |
| Investment Grade Tenants | [X.X]% | [X.X]% | % of rent |

*Lease Expiration Schedule (REQUIRED):*

| Year | Rent Expiring ($M) | % of Total ABR | Cumulative % |
|------|-------------------|----------------|--------------|
| 2025 | [X]M | [X.X]% | [X.X]% |
| 2026 | [X]M | [X.X]% | [X.X]% |
| 2027 | [X]M | [X.X]% | [X.X]% |
| 2028 | [X]M | [X.X]% | [X.X]% |
| 2029 | [X]M | [X.X]% | [X.X]% |
| 2030+ | [X]M | [X.X]% | 100% |

*CRITICAL: This table is REQUIRED for all traditional REITs. Extract from 10-K lease expiration disclosure. Shows rollover risk profile.*

*ROIC Note:* For REITs, do NOT include ROIC in P&L table. GAAP depreciation distorts invested capital; FFO/AFFO are the relevant return metrics. Add footnote: "ROIC: Not calculated — REIT accounting makes this metric non-comparable."

---

## Capital Allocation

**Sources of cash:**
- Operating Cash Flow: $[X]M
- [Other sources if material]

**Uses of cash:**

| Use | FY[Year] | FY[Year-1] | Notes |
|-----|----------|------------|-------|
| CapEx | [X]M | [X]M | [Maintenance vs. growth if disclosed] |
| Acquisitions | [X]M | [X]M | |
| Dividends | [X]M | [X]M | |
| Buybacks | [X]M | [X]M | [Auth remaining: $XM — calculate if components available] |
| Debt Paydown | [X]M | [X]M | |

**Capital allocation commentary:**
[2-4 sentences on: stated priorities vs. actual deployment, any disconnect between words and actions, future capacity, regulatory constraints if applicable. For insurers/banks: include dividend capacity from subs and regulatory capital ratios.]

---

## Risk Factors

Write 3-5 prose bullets covering the most material risks. Include editorial commentary — not just what the 10-K says, but what it means and whether it's real. **Add inline topic tags** for cross-referencing.

- **[Risk name]:** [What it is, current status. (p.XX)] *Probability: [Low/Med/High]. Impact: [Low/Med/High].* [Analyst interpretation — is this boilerplate or real?] `[RISK-SLUG]`

- **[Risk name] [NEW]:** [Continue with material risks. Flag NEW or materially expanded risks. (p.XX)] *Probability: [Low/Med/High]. Impact: [Low/Med/High].* [Interpretation] `[RISK-SLUG]`

- **[Regulatory/thesis-critical risk]:** [Structural risks that could alter the business model — be specific about status, timeline, and implications. (p.XX)] *Probability: [Low/Med/High]. Impact: [Low/Med/High].* `[RISK-SLUG]`

*Focus on thesis-relevant risks. Skip boilerplate unless materially expanded. EVERY risk bullet MUST include: (1) page reference, (2) Probability/Impact ratings in italics, (3) inline topic tag.*

**[NEW] Risk Assessment:**
- For **multi-year synthesis**: Compare to prior year's risk factors and flag [NEW] risks.
- For **single-year synthesis**: State "Unable to assess [NEW] vs. prior year — single-year analysis" at section start, OR fetch prior year's Item 1A for comparison.

---

## Accounting Quality

| Check | Status | Notes |
|-------|--------|-------|
| Recurring "one-time" charges | ✓/⚠/✗ | [Brief note] |
| Revenue recognition changes | ✓/⚠/✗ | |
| Receivables vs. revenue growth | ✓/⚠/✗ | |
| Adjusted metric definition drift | ✓/⚠/✗ | |
| Goodwill impairment assumptions | ✓/⚠/✗ | |
| Related party transactions | ✓/⚠/✗ | |
| Auditor issues | ✓/⚠/✗ | [Auditor name] |

*✓ = clean, ⚠ = watch, ✗ = concern*

**Summary:** [1-2 sentences on overall earnings quality and accounting cleanliness]

---

## Questions for Further Research

Numbered list of 3-5 questions the 10-K doesn't answer. Each question MUST include explicit "why it matters" context.

1. **[Question]?**
   *Why it matters:* [Explicit statement connecting this to investment thesis or decision-making]

2. **[Question]?**
   *Why it matters:* [What changes if you learn the answer]

3. **[Question]?**
   *Why it matters:* [Investment relevance — valuation, risk, moat, etc.]

---

## Topic Index

| Tag | Sections |
|-----|----------|
| `[MEMBERSHIP]` | Key Takeaways, Business Summary |
| `[RISK-TARIFF]` | Key Takeaways, Risk Factors |
| `[MARGINS]` | Key Takeaways, Financial Snapshot |

*List ALL inline `[TAG-SLUG]` tags used in the document with their section locations. Tags MUST appear inline in the body text (Key Takeaways, Risk Factors, Guidance) — not just in this index.*

**Validation check:** Every tag in this index should be searchable in the document body above.

---

## Source

- **Filing:** [Company] [10-K|20-F|40-F|URD|UK Annual Report|Integrated Report] FY[Year]
- **Regulator:** [SEC|AMF|FCA|FSA]
- **Accounting Standard:** [GAAP|IFRS]
- **Filed:** [YYYY-MM-DD]
- **FYE:** [YYYY-MM-DD]
- **Auditor:** [Auditor name]
- **Retrieved via:** [edgartools|parse_pdf_filing.py]
- **Financial data via:** [FMP API] *(for European filings)*

**Page References:**
- Business: p.XX-XX
- Risk Factors: p.XX-XX
- MD&A: p.XX-XX
- Financials: p.XX-XX
- Governance: p.XX-XX *(European filings)*
- Sustainability: p.XX-XX *(European filings)*
