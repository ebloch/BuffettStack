# Pre-Output Validation Checklist

**MANDATORY:** Complete all validation passes before writing the final memo.

---

## A. Industry Checklist Verification

- [ ] Identified company's industry (insurance, bank, SaaS, REIT, manufacturing, platform, ota, media-entertainment, exchange, aircraft-leasing)
- [ ] Read appropriate industry checklist from `industry-checklists/[industry].md`
- [ ] For EACH checklist item, confirmed:
  - Captured the metric in YAML frontmatter or body, **OR**
  - Used correct language for missing data (see A.1 below)
- [ ] If any mandatory item missing, went back and extracted it

### A.1 MD&A Extraction Quality Check (CRITICAL)

- [ ] **Checked MD&A extraction status:** Is the `mda` section full content or just a page reference stub?
- [ ] If MD&A extraction incomplete:
  - [ ] Added "**MD&A Extraction Note**" prominently in output noting the limitation
  - [ ] For metrics typically in MD&A (segment revenue, NIM, capital ratios), used "Not extracted — see MD&A pages X-Y" (NOT "Not disclosed")
  - [ ] Added a question to "Questions for Further Research" about key missing MD&A data

### A.2 "Not Disclosed" vs "Not Extracted" Language Check

- [ ] **Never used "Not disclosed" for metrics that definitely exist in 10-K** — e.g., major bank CET1 ratios, segment revenue for multi-segment companies
- [ ] For data that exists but wasn't captured: "Not extracted — see [section] pages X-Y"
- [ ] For data genuinely not in 10-K: "Not disclosed in 10-K"
- [ ] For data type not typically in 10-Ks: "Verify via [external source]" (e.g., credit ratings)

---

## B. YAML Frontmatter Complete

- [ ] All basic metadata fields populated (company, ticker, fiscal_year, industry, etc.)
- [ ] Form type captured (10-K, 20-F, or 40-F)
- [ ] Accounting standard noted (GAAP or IFRS) — **40-F filers use IFRS**
- [ ] Key metrics section complete (revenue, op income, net income, FCF, employees)
- [ ] Industry-specific metrics added (see industry checklist)
- [ ] Segments captured (top 3-5)
- [ ] Affiliates section populated (or "none" if no equity method investments)
- [ ] Capital section complete (buyback auth, deployed, dividends, total debt)
- [ ] Shares section complete (basic, diluted, options/RSUs, dilution %)
- [ ] **Share count validation:** Diluted shares MUST be >= basic shares. If not, investigate whether "diluted" figure is actually weighted average (different concept). Flag any inconsistency.
- [ ] Quality flags set (disclosure, accounting)
- [ ] Risk tags populated for filtering

---

## C. Affiliate Completeness Check

- [ ] Cross-referenced affiliates list against Notes to Financial Statements
- [ ] Checked "Investments" or "Equity Method Investments" notes specifically
- [ ] Confirmed ALL equity method investments captured in YAML
- [ ] For each affiliate, verified ownership % and income contribution

---

## D. Capital Allocation Completeness

- [ ] Buyback authorization remaining ($ amount or "not disclosed")
- [ ] Buybacks deployed this FY ($ amount)
- [ ] Dividends paid this FY ($ amount)
- [ ] Total debt captured in YAML
- [ ] Capital allocation commentary includes stated priorities vs. actual deployment
- [ ] For insurers/banks: dividend capacity from subs mentioned in commentary
- [ ] For insurers/banks: regulatory capital ratio mentioned in commentary

---

## E. Promises & Claims Tables

- [ ] At least 2 promises in "Promises to Track" table
- [ ] All promises have exact quotes with page references (p.XX)
- [ ] All promises have verification timeline (Q/FY)
- [ ] Claims to Verify table populated with external validation methods
- [ ] All claims have page references

---

## F. Risk Factors Section

- [ ] 3-5 prose bullets covering material risks
- [ ] Each risk includes: description, status, page reference (p.XX), *Probability: X. Impact: X.* in italics, analyst interpretation
- [ ] Each risk has inline topic tag `[RISK-SLUG]` at end of bullet
- [ ] [NEW] flag added to any new or materially expanded risk factors
- [ ] **For single-year synthesis:** Statement at section start: "Unable to assess [NEW] vs. prior year — single-year analysis"
- [ ] Thesis-critical risks (regulatory/structural) explicitly addressed

### Industry-Specific Risk Searches

**Insurance / Mortgage Insurance:**
- [ ] GSE reform / privatization — search: "GSE", "Fannie", "Freddie", "conservatorship"
- [ ] Basel III / Basel III Endgame — search: "Basel", "capital relief"
- [ ] PMIERs changes — search: "PMIERs", "eligible mortgage insurer"

**All P&C Insurers:**
- [ ] Social inflation / litigation trends — search: "social inflation", "tort", "nuclear verdicts"
- [ ] Climate risk disclosure — search: "climate", "ESG", "wildfire"
- [ ] Cyber risk — search: "cyber", "ransomware", "cyber insurance"

**Banks:**
- [ ] Basel III Endgame
- [ ] CECL changes
- [ ] Stress test results

**Exchanges/Platforms:**
- [ ] New competition — search: "FMX", "new exchange", "competing"
- [ ] Transaction tax proposals

**Retailers/Warehouse Clubs:**
- [ ] Tariff exposure — search: "tariff", "trade policy", "import" — **MUST include in Risk Factors section if mentioned in 10-K**
- [ ] E-commerce competition — search: "Amazon", "online", "delivery"
- [ ] Labor costs/unionization — search: "wage", "labor", "union" — **MUST include in Risk Factors section if material**
- [ ] Shrinkage/theft — search: "shrinkage", "theft", "inventory loss" — **MUST include in Risk Factors section OR note "Shrinkage: Below industry average per management" in Risk Factors or Accounting Quality if only mentioned as competitive advantage**
- [ ] Supply chain disruption — search: "supply chain", "disruption", "logistics" — **MUST include in Risk Factors section if explicitly listed as risk factor in 10-K**

**Note:** Industry-specific risks that appear in the 10-K's Risk Factors section MUST have a corresponding bullet in the output's Risk Factors section. If the risk is only mentioned as a competitive advantage (not a risk), note that context.

---

## G. Body Section Quality

### Key Takeaways
- [ ] 5-7 bullets with **bold lead-ins**
- [ ] Each bullet is insight + data, not just restating metrics
- [ ] Most important insights first

### Business Summary
- [ ] 2-3 paragraphs of flowing prose
- [ ] Segment table included with columns: Revenue, % Total, YoY, Op Margin (if disclosed)
- [ ] **Segment operating margin check:** Search MD&A "Operations Review" for each segment's operating income/margin — include in table if available
- [ ] Geographic mix and concentration noted
- [ ] Strategic investments mentioned if material

### What Changed
- [ ] Simple bullet list of material changes
- [ ] Regulatory/competitive changes included
- [ ] Acquisitions/divestitures noted

### Management Commentary
- [ ] Direct quote with page reference
- [ ] Key points list (3-5 items)
- [ ] Tone/sentiment observation if notable

### Financial Snapshot
- [ ] P&L & Returns table complete — MUST include all standard rows: Revenue, Gross Profit, Gross Margin, Operating Income, Net Income, **EPS (Diluted)**, Operating Margin, ROIC, Cash from Operations, FCF, FCF Conversion
- [ ] **EPS (Diluted)** included in P&L table with proper format ($X.XX per share). For ADR/ADS companies, include per-ADS figure and note the ADS ratio
- [ ] **ROIC** calculated and included in P&L & Returns table (NOPAT / Invested Capital). **For capital-light businesses (asset managers, platforms):** May note "ROIC: Not calculated — capital-light fee business" if ROIC isn't meaningful. **For banks:** Use ROTCE instead — note "ROIC: Not applicable for banks — use ROTCE"
- [ ] **ROIC formula shown:** Footnote includes explicit formula: "ROIC = NOPAT $XM (Op Inc $XM × (1 - X% tax rate)) / Avg Invested Capital $XM = X%"
- [ ] **ROIC consistency check:** Table value MATCHES footnote calculation — only ONE ROIC figure presented
- [ ] Balance Sheet table complete
- [ ] **Net Debt / EBITDA** calculated and included in Balance Sheet table. Notes column MUST show: "Net Debt $XM / EBITDA $XM". **For holding companies:** Calculate at corporate level (recourse debt only) and note: "Excludes $XXB non-recourse debt at subsidiaries"
- [ ] **Interest Coverage** calculated explicitly — NOT approximations like ">10x". Notes column MUST show: "EBIT $XM / Int Exp $XM"
- [ ] Debt structure described in 1-2 sentences

### Capital Allocation
- [ ] Sources of cash listed
- [ ] Uses of cash table complete
- [ ] Commentary includes priorities vs. deployment analysis

### Accounting Quality
- [ ] All 7 checklist items rated (✓/⚠/✗)
- [ ] Summary sentence included
- [ ] **Numerical accuracy check:** ALL numerical comparisons in the summary or body text must be verified against Financial Snapshot tables. Example: If stating "Inventory increased 15% (from $250M to $287M)", verify: (1) direction matches (287 > 250 = increase), (2) percentage is correct (287-250)/250 = 14.8% ≈ 15%. Flag any mismatches before finalizing.

### Questions for Further Research
- [ ] 3-5 numbered questions
- [ ] Each includes "why it matters" context

### Topic Index & Source
- [ ] All tags used in document listed
- [ ] **Inline tags verification:** Every tag in Topic Index appears as `[TAG-SLUG]` somewhere in body text (Key Takeaways, Risk Factors, or Guidance)
- [ ] Page references for major 10-K sections

---

## H. Operating Metrics (Industry-Specific)

### Insurers (REQUIRED)
- [ ] GPW and NPW by segment (not just NPE) — in YAML or Business Summary. If GPW not disclosed, explicitly state "GPW: Not disclosed separately"
- [ ] Segment table uses NPW as Revenue column (not NPE) when available
- [ ] Combined ratio components table in Financial Snapshot — loss ratio, expense ratio, cat impact, PYD impact, CAY ex-cat
- [ ] Prior Year Development table by segment in Financial Snapshot — or state "Segment-level PYD: Not disclosed"
- [ ] Investment portfolio metrics (per industry checklist) — duration, credit quality, unrealized G/L. Qualitative descriptions OK if quantitative not available
- [ ] Reserve development aggregate ($ and points)

### Mortgage Insurers (REQUIRED)
- [ ] NIW, IIF, RIF volumes
- [ ] Persistency rate
- [ ] Delinquency rate
- [ ] PMIERs sufficiency

### SaaS / Subscription (REQUIRED)
- [ ] **ARR/MRR** — in YAML as `arr_m` or `mrr_m`. If not disclosed, set to `null` AND state "ARR: Not disclosed" in Business Summary
- [ ] **Net Retention (NRR/NDR)** — in YAML as `net_retention_pct`. If not disclosed, set to `null` AND state "Net retention: Not disclosed" in Business Summary
- [ ] **Gross Retention** — in YAML as `gross_retention_pct`. If attrition rate disclosed, calculate: 100 - attrition. Note derivation in memo
- [ ] **Gross vs. Net Retention Distinguished** — Do NOT conflate attrition rate with net retention. Attrition → gross retention only
- [ ] **RPO and cRPO** — in YAML with YoY growth rates stated in body
- [ ] **RPO vs. Revenue Growth Comparison** — Explicit statement in Key Takeaways or Risk Factors (e.g., "RPO growth +11% vs. revenue +9%")
- [ ] **Gross Margin** — in YAML as `gross_margin_pct`. Subscription gross margin preferred; total acceptable
- [ ] **Rule of 40** — in YAML as `rule_of_40`. Show explicit calculation: revenue_growth_pct + fcf_margin_pct
- [ ] **CAC Payback** — If not disclosed, state "CAC payback: Not disclosed in 10-K"
- [ ] **Customer Concentration** — "No customer >10%" or specific concentration noted
- [ ] **Watch Items Assessed** — RPO deceleration, margin compression, attrition trends explicitly evaluated

### Manufacturing / Industrials (REQUIRED)
- [ ] **Backlog** — in YAML as `backlog_m`. Include backlog by segment in Business Summary if disclosed. **If not disclosed:** set to `null` in YAML AND add to Questions: "Backlog: Not disclosed — what is the order pipeline?"
- [ ] **Book-to-bill ratio** — in YAML as `book_to_bill`. Calculate if not stated: New Orders ÷ Revenue. **If not calculable:** set to `null` in YAML AND add to Questions: "Book-to-bill: Not calculable — order data not disclosed"
- [ ] **Working capital days (ALL THREE required):**
  - `inventory_days` — (Average Inventory ÷ COGS) × 365
  - `receivables_days` — (Average Receivables ÷ Revenue) × 365
  - `payables_days` — (Average Payables ÷ COGS) × 365
  - If any cannot be calculated, set to `null` and note in Questions why
- [ ] **Working capital assessment** — Flag unusual divergences (e.g., receivables growing faster than revenue). Include in Accounting Quality or Key Takeaways
- [ ] **Capacity utilization** — in YAML as `capacity_utilization_pct` if disclosed. **If not disclosed:** set to `null` in YAML AND add to Questions: "Capacity utilization: Not disclosed — unclear how much production headroom exists"
- [ ] **CapEx description** — Total in Capital Allocation. Note maintenance vs. growth split if disclosed. **If not disclosed:** add to Questions: "CapEx split: What portion is maintenance vs. growth?"
- [ ] **Input cost exposure** — Key exposures (raw materials, labor, energy, tariffs) in Risk Factors
- [ ] **Supply chain status** — Current state of supply chain challenges in What Changed or Risk Factors

**Manufacturing null metric enforcement:** For EACH manufacturing metric that is `null` in YAML, there MUST be a corresponding question in "Questions for Further Research" explaining why it matters. The skill must NOT have null manufacturing metrics without corresponding questions.

**For Defense/Aerospace specifically:**
- [ ] **Program concentration** — Largest program % of revenue in Key Takeaways (e.g., "F-35 at 27% of sales")
- [ ] **Government dependency** — U.S. Government % of sales in Business Summary
- [ ] **Fixed-price contract losses** — Quantify reach-forward losses in Key Takeaways and Risk Factors if material
- [ ] **Budget/policy risk** — NDAA status, Executive Orders affecting capital return in Risk Factors

### Exchanges/Platforms (REQUIRED)
- [ ] ADV / Volume by product class
- [ ] Rate per Contract with YoY trend
- [ ] Member vs. non-member volume %

### OTAs/Marketplaces (REQUIRED)
- [ ] Gross Bookings (GTV)
- [ ] Take Rate with YoY trend
- [ ] **Revenue vs. GMV growth differential stated** — MUST include explicit sentence in Key Takeaways or Financial Snapshot: "Revenue grew X% vs. GMV Y%, [indicating/reflecting] Z bps take rate [expansion/compression]"
- [ ] Watch Items section populated (or "No concerning trends identified")
- [ ] Gross Margin / Gross Profit in P&L table (important for merchant model economics)
- [ ] ROIC in P&L table (capital efficiency for asset-light business)

### Traditional REITs (REQUIRED for O, NNN, WPC, VICI, and similar net-lease/property REITs)
- [ ] **FFO and AFFO** — in YAML as `ffo_m` and `affo_m`. These are primary earnings metrics; GAAP net income is NOT the relevant measure
- [ ] **Occupancy rate** — in YAML as `occupancy_pct`
- [ ] **Same-store growth** — in YAML as `same_store_growth_pct`. Specify whether this is NOI or revenue growth in a footnote
- [ ] **Rent spreads** — In REIT-Specific Metrics table. Note "new vs. renewal" breakdown if disclosed, or overall recapture rate
- [ ] **Lease expiration schedule (REQUIRED TABLE)** — MUST include table in Financial Snapshot showing % of rent or ABR expiring by year for at least next 5 years. Format:
  | Year | Rent Expiring | % of Total |
  |------|---------------|------------|
  | 2025 | $XXM | X.X% |
  | 2026 | $XXM | X.X% |
  | ... | ... | ... |
- [ ] **WALT (weighted avg lease term)** — in YAML as `walt_years` and in REIT-Specific Metrics table
- [ ] **Cap rates (acquisitions)** — Disclosed yield on new investments in Key Takeaways or Capital Allocation
- [ ] **Debt maturity profile** — in Financial Snapshot Balance Sheet section
- [ ] **AFFO payout ratio** — Calculate: Dividends / AFFO. Include in REIT-Specific Metrics table
- [ ] **Tenant concentration** — Top tenants % of rent in Business Summary
- [ ] **Investment-grade tenant %** — If disclosed, include in Business Summary or REIT-Specific Metrics table
- [ ] **ROIC suppressed** — Do NOT include ROIC row in P&L table. Add footnote: "ROIC: Not calculated — REIT accounting makes this metric non-comparable"

### Tower REITs (REQUIRED for AMT, CCI, SBAC, UNIT)
- [ ] **FFO and AFFO** — in YAML as `ffo_m` and `affo_m`. If not disclosed (e.g., CCI uses Adjusted EBITDA instead), set to `null` with comment explaining alternative metric used. Note in Questions for Further Research.
- [ ] **Churn rate** — in YAML as `churn_pct`. If disclosed as retention rate, calculate: 100% - retention. If disclosed as $ amount, calculate: churn$ / site rental revenue. If only a range stated (e.g., "1-2%"), use midpoint or note the range.
- [ ] **Site/tower count** — in YAML as `site_count`. Include geographic breakdown in Business Summary
- [ ] **Adjusted EBITDA** — in YAML as `adjusted_ebitda_m`. Used for leverage calculation
- [ ] **Net Debt / Adjusted EBITDA** — in Balance Sheet table. Primary leverage metric for tower REITs
- [ ] **AFFO payout ratio** — Calculate: Dividends / AFFO. Note in Capital Allocation commentary
- [ ] **Organic growth components** — In Business Summary or What Changed: colocations, escalators, churn breakdown
- [ ] **Contractual escalators** — Note typical rates (e.g., "~3% U.S., CPI-linked international") in Business Summary
- [ ] **Non-cancellable lease backlog** — In Key Takeaways or Business Summary with $ amount
- [ ] **Tenant concentration** — In Business Summary: top 3 tenants % by segment
- [ ] **Traditional REIT metrics mapping table** — REQUIRED table showing: Occupancy → N/A, Same-store NOI → Organic growth %, Rent spreads → Escalator %, Lease expiration → Non-cancellable backlog $B, Cap rates → N/A. Include specific values for this company or "Not disclosed."
- [ ] **Watch items assessed** — Churn trend, leverage trend, escalator terms, technology disruption risks

### Aircraft Lessors (REQUIRED)
- [ ] Fleet count (owned, managed) in YAML and Business Summary
- [ ] Fleet composition by aircraft type (table or narrative)
- [ ] Utilization rate (% on lease) — calculate if not stated: on-lease / total owned
- [ ] Adjusted debt-to-equity ratio (primary leverage metric)
- [ ] Book value per share calculated
- [ ] Gain-on-sale margin (validates book values)
- [ ] Geographic distribution (full breakdown, flag China/emerging market concentration)
- [ ] Orderbook (aircraft on order, delivery schedule)
- [ ] Debt structure (fixed vs. floating, maturity schedule)
- [ ] [NEW] risks flagged for: geopolitical (China, Russia precedent), manufacturer issues, tariffs

### Payment Networks (REQUIRED for V, MA, AXP, DFS, PYPL)
- [ ] **Payments volume** — in YAML as `payments_volume_b`. Include YoY growth rate in Key Takeaways or Business Summary
- [ ] **Processed transactions** — in YAML as `processed_transactions_b`. Include YoY growth rate
- [ ] **Payment credentials/cards** — in YAML as `payment_credentials_b`. Network reach indicator
- [ ] **Revenue vs. volume growth differential (REQUIRED)** — MUST include explicit sentence in Key Takeaways: "Net revenue grew X% vs. payments volume Y%, reflecting [expanding/compressing] yield"
- [ ] **Client incentive intensity (REQUIRED)** — Track incentive growth vs. volume growth. Flag if incentives growing faster than volume as competitive pressure signal
- [ ] **Cross-border volume growth** — Highest-yield revenue. Include growth rate in Key Takeaways or Financial Snapshot
- [ ] **VAS revenue** — in YAML as `vas_revenue_m`. Include % of total revenue and growth rate. **RECONCILIATION CHECK:** If VAS appears with different values in MD&A vs. segment table, note the definitional difference
- [ ] **Watch Items section** — MUST include: Yield trend (expanding/stable/compressing), Incentive intensity (stable/concerning), Cross-border recovery, VAS penetration
- [ ] **Gross Margin treatment** — Either omit Gross Profit/Margin rows OR note "N/A — network model; costs are operating expenses." Do NOT show Gross Profit = Revenue
- [ ] **Regulatory risks** — Interchange regulation, debit routing rules, data localization in Risk Factors
- [ ] **Litigation** — For Visa/Mastercard, interchange MDL accrual is material and MUST be included

### Retailers/Warehouse Clubs (REQUIRED)
- [ ] **Comparable sales growth** — in YAML as `comparable_sales_growth_pct`. Include traffic vs. ticket breakdown if disclosed
- [ ] **Store count** — in YAML as `store_count` or `warehouse_count`. Include net new openings in What Changed
- [ ] **Gross margin** — in YAML as `gross_margin_pct`. Note any unusual items affecting margin (LIFO charges, etc.)
- [ ] **E-commerce % of sales** — in YAML as `ecommerce_pct` if disclosed. Note growth rate in Key Takeaways or What Changed
- [ ] **Inventory turnover** — calculate if not stated: COGS / Average Inventory. In YAML as `inventory_turnover_x`
- [ ] **Membership economics** (for clubs) — renewal rate, member count, fee revenue in YAML
- [ ] **Private label penetration** — % of sales from private label (e.g., Kirkland Signature) if disclosed
- [ ] **Geographic concentration** — flag if any region/state >20% of sales

### Media / Entertainment (REQUIRED)
- [ ] **Streaming subs by service** — Disney+, Hulu, ESPN+, Netflix, Max, etc. in YAML and Business Summary. If service subs not disclosed, state "Not disclosed"
- [ ] **ARPU by service** — at minimum domestic vs. international. In YAML as `streaming_arpu_[service]`
- [ ] **DTC profitability** — operating income/loss in YAML as `streaming_dtc_operating_income_m`
- [ ] **Advertising vs. subscription revenue split** — if ad-supported tiers exist. In Business Summary or Financial Snapshot

### Alternative Asset Managers (REQUIRED)
*For Brookfield, Blackstone, KKR, Apollo, Carlyle, Ares, and similar*

- [ ] **Primary metric identified** — Lead with Distributable Earnings (DE) or Fee-Related Earnings (FRE), not GAAP/IFRS net income
- [ ] **AUM and FBC** — in YAML as `aum_b` and `fee_bearing_capital_m`
- [ ] **FBC quality in Key Takeaways** — MUST include bullet stating FBC duration profile (% long-dated/perpetual). Example: "87% of FBC is long-dated or perpetual"
- [ ] **Fee revenue and FRE** — in YAML as `fee_revenue_m` and `fee_related_earnings_m`
- [ ] **Distributable earnings** — in YAML as `distributable_earnings_m` and `distributable_earnings_before_realizations_m`
- [ ] **Carried Interest table in Financial Snapshot** — MUST include: Realized Carried Interest, Unrealized Carry (or "Not disclosed"), Funds in Carry Position (if disclosed)
- [ ] **Uncalled commitments** — in YAML as `uncalled_commitments_m` (dry powder)
- [ ] **Fundraising & Deployment table in Financial Snapshot** — MUST include: Capital Raised, Uncalled Commitments, Capital Deployed, Fee Rate (Fee Revenue / FBC)
- [ ] **Segment table consistency** — If segments use different metrics (DE, FFO, DOE, NOI), either use separate tables OR include explicit footnote: "Metrics are not directly comparable"
- [ ] **YAML segments format** — Use `metric:` + `amount_m:` + `pct_contribution:` format (not standard `revenue_m:` + `pct_total:`)
- [ ] **Affiliate ownership** — For holding companies, list ownership percentages for major affiliates in YAML affiliates section and Business Summary
- [ ] **Recourse vs. non-recourse debt** — In Balance Sheet AND YAML, clearly separate corporate (recourse) debt from consolidated (non-recourse) debt. Use `total_debt_m` for recourse, `total_consolidated_debt_m` for total
- [ ] **GAAP/IFRS P&L included** — Even if secondary, include GAAP/IFRS P&L table with footnote explaining why DE is primary metric
- [ ] **Fee rate calculated** — Must calculate effective fee rate (Fee Revenue / FBC) in Fundraising & Deployment table

---

## I. Source Attribution Verification

- [ ] **Financial strength ratings** — only if explicitly quoted in filing
- [ ] **Market share claims** — verified with source page reference
- [ ] **Industry rankings** — verified with source page reference

If any item relies on external knowledge, flag with `[EXTERNAL SOURCE]` in memo.

---

## J. Form Type-Specific Checks

### For 40-F Filers (Canadian Companies)
- [ ] Accounting standard noted as IFRS in metadata and Source section
- [ ] IFRS-specific accounting noted where materially different from GAAP (e.g., lease accounting, revenue recognition)
- [ ] Canadian regulatory context noted if relevant (e.g., OSC vs. SEC)
- [ ] Content extracted from exhibits (Exhibit 99.1 = AIF, Exhibit 99.2 = MD&A + Financials)

### For 20-F Filers (Foreign Private Issuers)
- [ ] Accounting standard confirmed (GAAP or IFRS — check filing)
- [ ] Currency noted if not USD
- [ ] Foreign regulatory context noted if relevant

### For Integrated Reports (Japanese/International Companies)
- [ ] Accounting standard confirmed (IFRS or local GAAP — check filing)
- [ ] Reporting currency noted prominently (JPY amounts can be orders of magnitude larger than USD)
- [ ] Fiscal year end confirmed (Japanese companies: often March 31)
- [ ] Equity method investments captured thoroughly — often >30% of net income for sogo shosha
- [ ] Medium-term management plan (MTMP) extracted as guidance with targets vs. actuals
- [ ] Segment information mapped correctly — sogo shosha often have 6-10+ segments
- [ ] Revenue basis clarified (gross vs. net under IFRS 15)
- [ ] Cash vs. accrual gap noted for equity method income

---

## Validation Complete

All passes completed:
- [ ] A — Industry checklist verified
- [ ] B — YAML frontmatter complete
- [ ] C — Affiliates complete
- [ ] D — Capital allocation complete
- [ ] E — Promises & claims tables populated
- [ ] F — Risk factors section complete
- [ ] G — Body section quality verified
- [ ] H — Operating metrics captured (industry-specific)
- [ ] I — Source attribution verified
- [ ] J — Form type-specific checks (if 40-F, 20-F, or Integrated Report)

**Ready to write final memo.**
