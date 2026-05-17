# Alternative Asset Manager Checklist

For holding companies, asset managers, private equity managers, and diversified financials (e.g., Brookfield, Blackstone, KKR, Apollo, Carlyle, Ares).

---

## Industry Overview

Alternative asset managers earn money through:
1. **Management fees** — recurring fees on AUM/FBC
2. **Performance/incentive fees** — carried interest when funds exceed hurdles
3. **Investment income** — returns on co-investments and balance sheet capital

Key distinction: Unlike operating companies, GAAP/IFRS net income is often misleading due to fair value accounting, deconsolidation gains, and non-cash items. **Distributable Earnings (DE)** or **Fee-Related Earnings (FRE)** are typically the primary performance metrics.

---

## YAML Metrics (REQUIRED)

Add these to the `metrics:` section in YAML frontmatter:

| Metric | YAML Key | Where to Find |
|--------|----------|---------------|
| AUM | `aum_b` | MD&A, investor presentation |
| Fee-bearing capital | `fee_bearing_capital_m` | MD&A |
| Fee revenue | `fee_revenue_m` | Segment financials |
| Fee-related earnings | `fee_related_earnings_m` | Non-GAAP reconciliation |
| Distributable earnings | `distributable_earnings_m` | Non-GAAP reconciliation |
| DE before realizations | `distributable_earnings_before_realizations_m` | Non-GAAP reconciliation |
| Realized carried interest | `realized_carried_interest_m` | Segment or non-GAAP |
| Unrealized carried interest | `unrealized_carried_interest_m` | Balance sheet / notes |
| Uncalled commitments | `uncalled_commitments_m` | Liquidity discussion |
| Deployable capital | `deployable_capital_m` | Liquidity discussion |

**CRITICAL: Dry Powder / Uncalled Commitments Mapping**
- "Dry powder" and "uncalled commitments" are synonymous — both refer to committed but undeployed capital
- If the 10-K discloses "dry powder" or "deployable capital," populate BOTH `uncalled_commitments_m` AND `deployable_capital_m` with that value
- Do NOT leave `uncalled_commitments_m: null` if dry powder is disclosed in the body

**For holding company structures (BN, BRK):**
- `net_income_attributable_to_shareholders_m` — attributable to parent, not total
- Segment metrics may use different performance measures (DE, FFO, DOE, NOI)

---

## Business Summary Requirements

### Core Business Model
- [ ] Identify primary business pillars (e.g., Asset Management, Insurance/Wealth, Operating Businesses)
- [ ] Explain fee revenue sources (management fees, transaction fees, incentive fees)
- [ ] Describe carried interest mechanics (when it's earned, hurdle rates if disclosed)
- [ ] Note if company uses alternative performance metrics (DE, FRE) vs. GAAP/IFRS

### Fee-Bearing Capital Quality
- [ ] FBC breakdown by fund type (private funds, perpetual capital, liquid strategies)
- [ ] FBC duration profile (% long-dated or perpetual)
- [ ] Fee rate implied (Fee Revenue / FBC) if calculable

### Fee Rate Consistency (REQUIRED)
When calculating and presenting fee rate, use a SINGLE methodology throughout the memo:
- **Preferred method:** Management's stated "Annualized Base Management Fee Rate" if disclosed
- **Alternative:** Fee Revenue / Fee-Bearing Capital (or FEAUM)
- **Do NOT** present multiple conflicting fee rate figures without reconciliation
- If multiple rates shown, explain the difference (e.g., "Management's stated rate of 0.85% vs. implied 0.90% due to X")

### Operating Affiliates (for holding companies)
- [ ] List major affiliates with ownership percentages
- [ ] Note which are consolidated vs. equity method
- [ ] Include distributions from affiliates in Capital Allocation

---

## YAML Segment Format for Asset Managers

Asset managers require a different YAML segment format because segments use non-comparable metrics. Instead of the standard `revenue_m` / `pct_total` format, use:

```yaml
segments:
  - name: Asset Management
    metric: DE  # or FRE
    amount_m: 2645
    pct_contribution: 54  # % contribution to total earnings
  - name: Wealth Solutions
    metric: DOE
    amount_m: 1350
    pct_contribution: 28
  - name: Operating Businesses
    metric: FFO
    amount_m: 566
    pct_contribution: 12
    note: "Metrics not directly comparable across segments"
```

**Key differences from standard format:**
- `metric:` field specifies the performance measure used (DE, FRE, DOE, FFO, NOI)
- `amount_m:` instead of `revenue_m:` (since it may not be revenue)
- `pct_contribution:` instead of `pct_total:` (percentages may not sum to 100%)
- Optional `note:` field for important caveats

---

## Segment Table Guidance (Body)

**Challenge:** Asset managers often have segments with non-comparable metrics (DE for AM, FFO for operating businesses, NOI for real estate).

**Solution:** Use one of these approaches:

**Option 1 — Separate Tables:**
```markdown
**Asset Management & Wealth (DE-based):**
| Segment | DE | % of Total DE |
|---------|-----|---------------|

**Operating Businesses (FFO-based):**
| Segment | FFO | Distributions to Parent |
|---------|-----|------------------------|
```

**Option 2 — Single Table with Clear Labeling:**
```markdown
| Segment | Metric | Amount | % of Parent Earnings |
|---------|--------|--------|---------------------|
| Asset Management | DE | 2,645M | 54% |
| Wealth Solutions | DOE | 1,350M | 28% |
| Infrastructure | FFO | 566M | 12% |

*Note: Metrics are not directly comparable; percentages show contribution to DE before realizations*
```

**Never:** Mix DE/FFO/NOI in a single column without explicit footnote explaining non-comparability.

---

## Financial Snapshot Requirements

### Primary Metric Table (REQUIRED)
For companies using non-GAAP primary metrics:
- [ ] Lead with Distributable Earnings (or FRE) table
- [ ] Show DE before realizations (most stable measure)
- [ ] Show realized carried interest separately
- [ ] Show disposition gains separately (lumpy)
- [ ] Include YoY comparison

### GAAP/IFRS P&L Table (REQUIRED but secondary)
- [ ] Include for completeness
- [ ] Add footnote: "IFRS net income includes fair value adjustments, deconsolidations, and non-cash items. Distributable Earnings is management's primary performance measure."

### ROIC Guidance for Asset Managers
Asset managers are typically capital-light. ROIC calculation should:
- [ ] Focus on **fee-related earnings** vs. **invested capital in the asset management business**
- [ ] Exclude operating businesses that require separate capital analysis
- [ ] OR note "ROIC: Not calculated — capital-light fee business; return measured via DE growth"

**Alternative metric:** DE growth rate + FBC growth rate (shows scaling efficiency)

### Leverage Metrics Guidance

**Net Debt / EBITDA** is typically not meaningful for fee-based asset managers. Use alternative metrics:

**For pure-play asset managers (BX, KKR, APO, CG, ARES):**
- [ ] **Primary leverage metric:** Debt / FRE or Debt / Distributable Earnings
- [ ] Note corporate debt level and coverage in Balance Sheet section
- [ ] State "Net Debt / EBITDA: Not calculated — fee-based business; see Debt/FRE ratio" if traditional ratio omitted

**For holding companies with recourse vs. non-recourse debt (BN, BRK):**
- [ ] Calculate at **corporate level only** (recourse debt)
- [ ] Note consolidated debt separately (mostly non-recourse)
- [ ] Format: "Net Debt / EBITDA (Corporate): X.Xx — excludes $XXB non-recourse debt at subsidiaries"

### Interest Coverage Guidance

For asset managers, Interest Coverage can be calculated on either basis:
- **GAAP basis:** EBIT (Operating Income) / Interest Expense — acceptable, most comparable
- **Non-GAAP basis:** FRE / Interest Expense — shows coverage from recurring fees only

**Requirement:** State which basis is used in the Notes column. If using GAAP EBIT, show the explicit calculation. Example:
```
Interest Coverage | 14.6x | 6.9x | EBIT $6,459M / Int Exp $444M (GAAP basis)
```

---

## Carried Interest Section (REQUIRED)

Include in Financial Snapshot or separate section:

| Metric | FY[Year] | FY[Year-1] | Notes |
|--------|----------|------------|-------|
| Realized Carried Interest | | | Cash received |
| Unrealized Carried Interest | | | Balance sheet accrual (Net Accrued Performance Revenues) |
| Funds in Carry Position | | | % of mature funds exceeding hurdle |

**Key questions to answer:**
- What hurdle rate applies? (Usually 7-8% preferred return)
- What's the carry waterfall timing? (When does carry crystallize?)
- How much unrealized carry exists as future earnings potential?

**Note on "Funds in Carry Position":** This metric (% of funds exceeding hurdle) is often NOT disclosed in 10-Ks. If not available, mark as "Not disclosed" — this is acceptable and common for this industry.

---

## Fundraising & Deployment Metrics (REQUIRED)

| Metric | FY[Year] | FY[Year-1] | Notes |
|--------|----------|------------|-------|
| Capital Raised | | | Annual fundraising |
| Uncalled Commitments | | | Dry powder |
| Capital Deployed | | | Investments made |
| Deployment Pace | | | Uncalled / Avg Annual Deployment |

---

## Capital Allocation Requirements

For holding company structures:
- [ ] Distributions received from affiliates
- [ ] Corporate-level sources (fee earnings, investment income)
- [ ] Uses: buybacks, dividends, strategic M&A, debt paydown
- [ ] NCIB authorization and deployment pace
- [ ] Liquidity position (core liquidity, credit facilities)

---

## Risk Factors — Industry-Specific Searches

Search Risk Factors section for:
- [ ] **Fundraising risk** — "fundraising", "capital raising", "LP commitment"
- [ ] **Denominator effect** — "denominator", "liquidity", "institutional"
- [ ] **Interest rate sensitivity** — "interest rate", "refinancing", "floating rate"
- [ ] **Fee compression** — "fee pressure", "competition", "management fees"
- [ ] **Key person risk** — "key person", "founders", "executive departure"
- [ ] **Investment performance** — "performance", "returns", "benchmark"
- [ ] **Real estate exposure** — "office", "real estate", "property values" (if applicable)
- [ ] **Insurance/annuity risks** — "spread", "ALM", "surrender", "crediting rate" (if wealth segment)

---

## Accounting Quality — Special Considerations

| Check | Specific Concern |
|-------|------------------|
| Non-GAAP reliance | How transparent are DE/FRE definitions? Do they drift? |
| Fair value marks | What assets are marked to model vs. market? |
| Consolidation | What's consolidated vs. equity method? Could change? |
| Related party | Inter-company transactions between listed affiliates? |
| Carry recognition | When is carry recognized? Conservative or aggressive? |

---

## Questions for Further Research — Suggested Topics

1. **Carry economics:** What's the unrealized carry balance? When will it crystallize?
2. **Fundraising sustainability:** Can current pace continue or is this cyclical peak?
3. **Fee rate trends:** Is effective fee rate stable, expanding, or compressing?
4. **Insurance/wealth economics:** What's the spread income outlook? Surrender risk?
5. **Deployment velocity:** At current pace, how long until dry powder is deployed?
6. **Track record:** What are historical fund returns vs. benchmarks?

---

## Watch Items

Flag these trends if observed:
- [ ] FBC growth slowing while AUM growing (fee rate compression)
- [ ] Fundraising pace declining YoY
- [ ] Unrealized carry declining (performance concerns)
- [ ] Deployment pace accelerating without fundraising (dry powder depletion)
- [ ] Fee revenue / FRE margin compression
- [ ] Real estate office exposure concerns
