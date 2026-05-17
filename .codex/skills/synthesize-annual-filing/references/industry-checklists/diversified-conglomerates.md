# Diversified Conglomerates Industry Checklist

Use this checklist for diversified trading/investment conglomerates including Japanese sogo shosha (Mitsui, Mitsubishi Corp, ITOCHU, Sumitomo Corp, Marubeni) and similar multi-sector conglomerates.

---

## Industry-Specific YAML Metrics

Add these to the `metrics` section:

```yaml
metrics:
  # Standard metrics (always required)
  revenue_m: [number]
  operating_income_m: [number]
  net_income_m: [number]
  fcf_m: [number]  # Core operating cash flow preferred
  employees: [number]

  # Conglomerate-specific metrics (REQUIRED)
  core_operating_cf_m: [number]  # Core operating cash flow (excludes working capital swings from commodity trades)
  equity_method_income_m: [number]  # Income from equity method investments (often >30% of earnings)
  segment_count: [number]  # Number of reportable business segments
  net_debt_to_equity: [number]  # Net D/E ratio — primary leverage metric for sogo shosha
  roe_pct: [number]  # Return on equity — primary return metric
  resource_revenue_pct: [number or null]  # Revenue from resource/commodity segments as % of total

  # Optional but valuable
  dividend_payout_ratio_pct: [number or null]
  total_shareholder_return_pct: [number or null]  # Buybacks + dividends as % of net income
  book_value_per_share: [number or null]
```

**Note:** Revenue for sogo shosha may be in JPY (hundreds of billions). Note currency prominently in YAML and throughout memo.

---

## Segment Analysis

Sogo shosha typically have 6-10+ business segments. ALL segments must be captured.

### Segment Table Format

| Segment | Revenue | % Total | Op Income | Op Margin | YoY |
|---------|---------|---------|-----------|-----------|-----|
| [Segment 1] | [X]M | [X]% | [X]M | [X]% | [+X%] |
| [Segment 2] | [X]M | [X]% | [X]M | [X]% | [+X%] |
| ... | ... | ... | ... | ... | ... |

### Segment Classification

Identify each segment as:
- **Core/Stable:** Non-resource segments with recurring earnings (machinery, chemicals, food, urban development)
- **Resource/Volatile:** Commodity-exposed segments (metals, energy, mineral resources)
- **Growth:** Segments receiving investment priority (digital, next-gen energy, healthcare)

Note in Key Takeaways: ratio of core/stable vs. resource/volatile earnings.

### Common Sogo Shosha Segments

**Mitsubishi Corp:** Natural Gas, Industrial Materials, Petroleum & Chemicals, Mineral Resources, Industrial Infrastructure, Automotive & Mobility, Food Industry, Consumer Industry, Power Solution, Urban Development

**Mitsui:** Mineral & Metal Resources, Energy, Machinery & Infrastructure, Chemicals, Iron & Steel Products, Lifestyle, Innovation & Corporate Development

**ITOCHU:** Textile, Machinery, Metals & Minerals, Energy & Chemicals, Food, General Products & Realty, ICT & Financial Business, The 8th Company

**Sumitomo Corp:** Metal Products, Transportation & Construction Systems, Infrastructure, Media & Digital, Living Related & Real Estate, Mineral Resources/Energy/Chemical & Electronics

**Marubeni:** Food, Agri Business, Forest Products, Chemicals, Metals & Mineral Resources, Energy, Power, Infrastructure, Finance/Leasing/Real Estate, Aerospace & Ship, Construction/Industrial Machinery/Mobility, Next Generation Business Development, CDIO

---

## Equity Method Investments

Equity method investments are often the largest contributor to net income for sogo shosha. This section is CRITICAL.

### What to Capture

| Associate | Ownership % | Income Contribution | Sector | Cash Dividend Received |
|-----------|-------------|--------------------:|--------|----------------------:|
| [Name] | [X]% | [X]M | [sector] | [X]M or N/D |
| [Name] | [X]% | [X]M | [sector] | [X]M or N/D |

### Key Analysis Points

- **Cash vs. accrual gap:** Equity method income is accrual-based. Actual cash dividends received from associates may differ significantly. Note the gap if disclosed.
- **Concentration risk:** Flag any single associate contributing >15% of group net income.
- **Impairment risk:** Note any associates with recent impairment charges or declining performance.
- **Strategic vs. financial:** Distinguish associates held for strategic integration vs. pure financial return.

---

## Resource/Commodity Exposure

### Key Commodities to Track

| Commodity | Segment | Price Sensitivity | Hedging |
|-----------|---------|-------------------|---------|
| Iron ore | Mineral Resources | [$/ton impact] | [Yes/No/Partial] |
| Coking coal | Mineral Resources | [$/ton impact] | [Yes/No/Partial] |
| Copper | Mineral Resources | [$/lb impact] | [Yes/No/Partial] |
| LNG/Natural gas | Energy | [$/MMBtu impact] | [Yes/No/Partial] |
| Crude oil | Energy | [$/bbl impact] | [Yes/No/Partial] |

### Analysis Points

- What % of net income comes from resource segments?
- Is management actively diversifying away from commodity exposure?
- Note any sensitivity analysis disclosed (e.g., "$10/bbl change = ¥X billion impact")
- Reserve/resource life if disclosed

---

## Capital Allocation

### Shareholder Returns Framework

| Metric | FY[Year] | FY[Year-1] | Notes |
|--------|----------|------------|-------|
| Net Income | [X]M | [X]M | |
| Dividends Paid | [X]M | [X]M | |
| Buybacks | [X]M | [X]M | |
| Total Shareholder Return | [X]M | [X]M | |
| TSR as % of Net Income | [X]% | [X]% | |
| Dividend Payout Ratio | [X]% | [X]% | Target: [X]% |

### Investment Pipeline

- Total investment/divestiture plan under current MTMP
- Key investments made this year (sector, amount, strategic rationale)
- Divestiture proceeds and asset recycling
- Exit pipeline (non-core assets being divested)

---

## Medium-Term Management Plan (MTMP)

Japanese companies typically publish 3-year MTMPs. Capture in Guidance & Promises:

### MTMP Summary

| Target | MTMP Goal | Current FY Actual | On Track? |
|--------|-----------|-------------------|-----------|
| Net Income | [X]M | [X]M | Yes/Behind/Ahead |
| ROE | [X]% | [X]% | Yes/Behind/Ahead |
| Core Operating CF | [X]M | [X]M | Yes/Behind/Ahead |
| Shareholder Returns | [X]M over plan | [X]M cumulative | Yes/Behind/Ahead |

### Strategic Priorities

- Key growth areas / investment themes
- Portfolio transformation targets
- DX (digital transformation) initiatives
- Sustainability / carbon neutrality targets

Note the MTMP name and period (e.g., "Midterm Corporate Strategy 2024" covers FY2022-2024).

---

## Sogo Shosha-Specific Considerations

### Cross-Shareholdings

- Note any cross-shareholding reduction commitments
- Unrealized gains/losses on strategic holdings
- Impact on book value

### Yen Sensitivity

- Revenue and earnings sensitivity to JPY/USD movements
- Natural hedging from overseas operations
- Translation vs. transaction exposure

### Governance Reform

- Progress on board independence (target: >1/3 independent directors)
- Nomination/compensation committee composition
- CEO succession framework
- Abolition of takeover defense measures

### Reporting Currency

- **CRITICAL:** Note reporting currency (JPY) prominently
- Convert key metrics to USD at period-end rate for context if helpful
- FYE is typically March 31 for Japanese companies

---

## Industry-Specific Risks

Search for and flag in Risk Factors:

| Risk | Search Terms | Impact |
|------|--------------|--------|
| **Commodity price volatility** | "commodity", "price fluctuation", "resource" | Earnings swing |
| **Country risk** | "country risk", "geopolitical", "sanctions", "emerging market" | Asset impairment |
| **Currency risk** | "foreign exchange", "yen", "currency" | Translation, margins |
| **Credit risk** | "credit", "counterparty", "default" | Trading losses |
| **Climate/transition risk** | "climate", "carbon", "transition", "decarbonization" | Asset stranding |
| **Investment impairment** | "impairment", "write-down", "fair value" | One-time losses |
| **Concentration risk** | "concentration", "single project", "dependence" | Earnings volatility |

---

## Accounting Considerations

### IFRS vs. Japan GAAP

- Most sogo shosha report under IFRS (check)
- Key differences from US GAAP in consolidation, goodwill treatment
- Note accounting standard in metadata

### Equity Method Accounting

- Equity method income ≠ cash received
- Large gap between equity income and dividends can indicate earnings quality concern
- Note any impairment of equity method investments

### Fair Value Changes

- Commodity derivatives and trading positions
- Mark-to-market gains/losses on investments
- Distinguish "core" vs. "non-core" earnings

### Revenue Recognition

- Sogo shosha may report "gross" revenue (including trading pass-throughs)
- Some have shifted to "net" revenue under IFRS 15 — clarify which basis is used
- Gross profit or trading profit may be more meaningful than revenue

---

## Questions to Consider

Add to Questions for Further Research if not answered:

1. **Earnings quality:** What % of net income is cash-backed (dividends from associates vs. equity method accruals)?
2. **Resource concentration:** How sensitive is net income to iron ore / LNG price changes?
3. **MTMP execution:** Is current MTMP on track? What was outcome of prior MTMP?
4. **Portfolio transformation:** What is the trend in core/stable vs. resource earnings mix?
5. **Capital allocation:** Is management prioritizing TSR (buybacks + dividends) or growth investment?
6. **Governance progress:** Board independence ratio? Cross-shareholding reduction pace?

---

## Watch Items

Flag in Key Takeaways or Risk Factors if concerning:

- [ ] Resource segment earnings >50% of total (concentration risk)
- [ ] Equity method income growing but cash dividends not keeping pace
- [ ] Net D/E ratio rising above 1.0x
- [ ] ROE declining below management's target
- [ ] Large impairment charges on associates or resources
- [ ] MTMP targets being revised downward
- [ ] Cross-shareholding reduction stalling
- [ ] Single associate contributing >20% of group net income
