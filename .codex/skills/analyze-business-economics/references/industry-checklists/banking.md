# Banking — Business Economics Checklist

**Trigger Keywords:** "bank", "banking", "commercial bank", "investment bank", "financial institution", "deposits", "net interest income"

---

## Required Metrics (Section 4)

### Profitability Metrics (ALL REQUIRED)

| Metric | Benchmark | Why It Matters |
|--------|-----------|----------------|
| Net Interest Margin (NIM) | >2.5% strong; 2.0-2.5% adequate; <2.0% concerning | Core spread business profitability |
| Return on Tangible Common Equity (ROTCE) | >15% excellent; 12-15% good; <10% concerning | True equity returns excluding goodwill |
| Efficiency Ratio | <55% excellent; 55-60% good; >65% concerning | Operating leverage and cost discipline |
| Pre-Provision Net Revenue (PPNR) | Growing and stable | Earnings before credit losses |

### Asset Quality Metrics (ALL REQUIRED)

| Metric | Benchmark | Why It Matters |
|--------|-----------|----------------|
| Net Charge-Off (NCO) Rate | <0.5% excellent; 0.5-1.0% normal; >1.5% concerning | Actual credit losses realized |
| Non-Performing Loan (NPL) Ratio | <1.0% healthy; 1.0-2.0% elevated; >2.0% concerning | Forward-looking credit quality |
| Allowance Coverage (ACL/NPL) | >150% strong; 100-150% adequate; <100% concerning | Reserve adequacy |
| Provision / NCO Ratio | >100% building reserves; <100% releasing | Reserve trajectory |

### Capital Metrics (ALL REQUIRED)

| Metric | Benchmark | Why It Matters |
|--------|-----------|----------------|
| CET1 Ratio | >12% strong; 10-12% adequate; <10% concerning | Regulatory capital adequacy |
| Tangible Book Value Per Share Growth | >8% CAGR strong; 5-8% adequate; <5% concerning | Long-term value creation |
| Loan-to-Deposit Ratio | 70-90% healthy; >100% liquidity concern | Funding stability |
| Dividend Payout Ratio | 30-50% sustainable; >60% may limit flexibility | Capital allocation |

---

## Required Quirks (Section 3)

### 1. Provision vs Net Charge-Offs

- **What:** Provision for credit losses is management estimate; NCOs are actual realized losses
- **Distortion:** Provisions can be manipulated to smooth earnings; NCOs lag economic reality
- **Adjustment:** Track provision/NCO ratio over time; compare to CECL reserve builds; focus on pre-provision earnings

### 2. AOCI Volatility (Available-for-Sale Securities)

- **What:** AFS securities marked to market through OCI; impacts book value but not income
- **Distortion:** Rising rates crush book value even if HTM intent; SVB demonstrated liquidity risk
- **Adjustment:** Track "adjusted TBV" excluding AOCI; understand HTM vs. AFS portfolio mix and duration

### 3. Non-Interest Income Composition

- **What:** Fee income, trading revenue, investment banking income all in one line
- **Distortion:** Trading gains are volatile; IB revenue cyclical; obscures stable fee income
- **Adjustment:** Break out wealth management, card fees, IB separately; track recurring vs. volatile

### 4. Derivative and Trading Book Accounting

- **What:** Trading assets marked to market daily; hedges may qualify for hedge accounting
- **Distortion:** Trading revenue swings with markets; hedge ineffectiveness creates volatility
- **Adjustment:** Normalize trading revenue to average; understand desk composition and risk limits

---

## Valuation Guidance (Section 8)

### Primary Valuation Method

**Price-to-Tangible Book Value (P/TBV) with ROTCE adjustment**

| ROTCE Range | Justified P/TBV | Rationale |
|-------------|-----------------|-----------|
| >16% sustainable | 2.0-2.5x | Premium for superior returns |
| 12-16% | 1.3-2.0x | Earning above cost of equity |
| 10-12% | 1.0-1.3x | Modest value creation |
| <10% | <1.0x | Discount for value destruction |

### Secondary Methods

- **P/E on Normalized Earnings:** Normalize for credit cycle; 8-12x for universal banks
- **Dividend Yield:** 3-4% yield reasonable for large banks
- **P/PPNR:** Pre-provision earnings multiple for credit-cycle normalization

### Methods to AVOID

| Method | Why Inappropriate |
|--------|-------------------|
| EV/EBITDA | Concept doesn't apply; interest is operating |
| P/B (book value) | Includes goodwill; TBV more relevant |
| Raw P/E | Earnings distorted by provision timing |
| FCF Yield | Cash flow statement not meaningful for banks |

### DCF Considerations

- **Excess capital deployment:** Model capital return trajectory
- **Credit cycle normalization:** Use through-cycle NCO rates
- **NIM sensitivity:** Model rate scenarios
- **Regulatory capital constraints:** Growth limited by capital generation

### Owner's Earnings Adjustments

```
Net Income                                    $XX,XXXM (FYxxxx)
+ Provision above normalized NCO             $X,XXXM [if over-reserving]
- Provision below normalized NCO             ($X,XXXM) [if under-reserving]
- AOCI gains included in income                 ($XXXM) [if material]
- Trading gains above average                   ($XXXM) [normalize trading]
= Normalized Owner's Earnings               ~$XX,XXXM

Note: For banks, "normalized ROE × tangible equity" is Owner's Earnings proxy
```

---

## Peer Selection (Section 7)

### Match On

| Factor | Why It Matters |
|--------|----------------|
| Business mix (consumer/commercial/IB/wealth) | Different risk and return profiles |
| Geographic footprint | Economic and regulatory exposure |
| Asset size and complexity | Regulatory treatment differs |
| Funding mix (deposits vs. wholesale) | Cost and stability |
| Credit quality profile | Risk tolerance and underwriting |

### Flag as False Comparables

| Company Type | Why Not Comparable |
|--------------|-------------------|
| Investment banks (pure) | Trading vs. lending economics |
| Regional vs. universal banks | Different business models |
| Credit card companies | Different asset type and returns |
| Insurance companies | Different liability structure |
| Fintech lenders | Different funding, regulatory, and cost structure |

---

## Red Flags to Document

| Red Flag | What It Signals |
|----------|-----------------|
| NCO rate rising for 3+ quarters | Credit quality deteriorating |
| NIM compression without offsetting fee growth | Earnings pressure |
| CET1 declining toward minimums | Capital stress |
| Efficiency ratio deteriorating | Cost control issues |
| NPL coverage declining | Reserve adequacy concerns |
| Deposit outflows or rising funding costs | Franchise weakness |

---

## Green Flags to Document

| Green Flag | What It Signals |
|------------|-----------------|
| ROTCE >15% through credit cycle | Superior franchise and underwriting |
| TBV per share CAGR >8% | Compounding value |
| Efficiency ratio improving | Operating leverage |
| NCO rate below peers consistently | Better credit underwriting |
| Consistent buybacks at <TBV | Capital discipline and value creation |
