# Insurance — Business Economics Checklist

This checklist supplements the generic output template with insurance-specific requirements. All items below are **mandatory** for insurance company analyses.

---

## Required Metrics (Section 4)

### Underwriting Metrics (ALL REQUIRED)

| Metric | Benchmark | Why It Matters |
|--------|-----------|----------------|
| Combined Ratio | <95% excellent; 95-100% acceptable; >100% unprofitable underwriting | Measures underwriting profitability before investment income |
| Loss Ratio | 55-65% typical P&C; compare to peers by line of business | Indicates claims severity and pricing adequacy |
| Expense Ratio | 25-35% typical; trend direction matters more than level | Operating efficiency; watch for expense creep |
| CAY Loss Ratio ex-Cat | Core underwriting quality; should be stable YoY | Strips out volatility to show true underwriting skill |
| CAY Combined Ratio ex-Cat | <92% excellent; 92-96% good; >96% concerning | Most comparable metric across companies and time |
| Catastrophe Load | 3-6 pts typical; >8 pts elevated exposure | Risk concentration indicator |

### Investment Metrics (ALL REQUIRED)

| Metric | Benchmark | Why It Matters |
|--------|-----------|----------------|
| Investment Yield | Calculate: NII / Avg Invested Assets; >3.5% strong; <2.5% low duration bet | Float economics depend on investment returns |
| Float Leverage | Float / Shareholders Equity; 1.5-2.5x typical | Higher = more earnings power from float; also more risk |
| Portfolio Duration | 3-5 yrs typical; <3 yrs defensive; >5 yrs rate-sensitive | Interest rate sensitivity indicator |
| Credit Quality | >90% investment grade; <5% below-IG preferred | Portfolio risk indicator |

### Capital & Returns (ALL REQUIRED)

| Metric | Benchmark | Why It Matters |
|--------|-----------|----------------|
| ROE vs. Cost of Equity | ROE > COE = creating value; spread >3pts strong; <0 destroying value | The key value creation metric for financials |
| Book Value Per Share Growth | >10% CAGR strong; 5-10% adequate; <5% weak | Long-term compounding metric; Buffett's preferred |
| Tangible Book Value / Share | Track growth rate vs. BVPS | Some insurers carry intangibles from acquisitions |
| Operating ROE | 12-15% good; >15% excellent; <10% inadequate | Excludes AOCI volatility for cleaner picture |

### Reserve Quality (ALL REQUIRED)

| Metric | Benchmark | Why It Matters |
|--------|-----------|----------------|
| Reserve Development (PYD) | Consistent favorable 1-3 pts = conservative reserving; adverse = red flag | Reveals reserving philosophy and potential earnings manipulation |
| Reserve Releases / Net Income | <30% sustainable; >50% concerning over-reliance | Earnings quality indicator |
| Reserves / NPE Ratio | Compare to peers; rising = potential under-reserving in past | Relative reserve adequacy |

---

## Required Quirks (Section 3)

The following accounting quirks MUST be documented for insurance companies:

### 1. Reserve Estimation Uncertainty

- **What:** Loss reserves are management estimates; actual claims may differ materially
- **Distortion:** Prior Year Development (PYD) flows through current period income, masking true underwriting results
- **Adjustment:** Always analyze Current Accident Year results separately from calendar year; track PYD trends over 5+ years

### 2. Float Economics

- **What:** Insurance liabilities (unpaid claims, unearned premiums) represent "float" — money held temporarily that generates investment income
- **Distortion:** GAAP shows investment income separately, obscuring that underwriting funds this float
- **Adjustment:** Calculate float cost = combined ratio - 100%; if negative, float has negative cost (better than free)

### 3. AOCI Volatility (Unrealized Gains/Losses)

- **What:** Available-for-sale securities marked to market through OCI, creating book value swings
- **Distortion:** GAAP book value moves with interest rates even if securities will be held to maturity
- **Adjustment:** Track "adjusted book value" excluding AOCI; use operating ROE excluding AOCI impact

### 4. Reinsurance Accounting

- **What:** Ceded reinsurance reduces gross premiums and losses but creates recoverable asset
- **Distortion:** Reinsurance recoverables are an asset subject to counterparty credit risk; gross vs. net can differ materially
- **Adjustment:** Review reinsurer credit quality; monitor gross vs. net retention trends; watch for structural reinsurance that front-loads earnings

---

## Valuation Guidance (Section 8)

### Primary Valuation Method

**Price-to-Book (P/B) with ROE adjustment** — NOT Price-to-Earnings

| ROE Range | Justified P/B | Rationale |
|-----------|---------------|-----------|
| >15% sustainable | 1.5-2.0x | Premium for superior capital allocation |
| 12-15% | 1.2-1.5x | Earning cost of equity with modest premium |
| 10-12% | 1.0-1.2x | Near book value, modest value creation |
| <10% | <1.0x | Discount for value destruction |

### Secondary Methods

- **P/E on Operating Earnings:** Useful for comparison, but normalize for cat losses and reserve development
- **Dividend Yield:** Relevant for mature insurers with stable payout ratios

### Methods to AVOID

| Method | Why Inappropriate |
|--------|-------------------|
| EV/EBITDA | D&A not meaningful for insurers; no "enterprise" value concept applies well |
| Raw P/E | Earnings distorted by reserve releases, cat volatility, AOCI |
| FCF Yield | Cash flow statement captures premium cash flows, not economic earnings |
| Price/Sales (P/NPW) | Ignores profitability entirely |

### DCF Considerations

- **Normalize for catastrophes:** Use 10-year average cat load or expected cat budget, not single-year results
- **Normalize for reserve development:** Remove PYD from earnings; model assumes reserves are adequately stated
- **Growth constraints:** Premium growth constrained by capital; model capital needs explicitly
- **Terminal value:** Use P/B multiple approach rather than perpetuity growth on earnings

### Owner's Earnings Adjustments

```
Net Income                                    $X,XXXM (FYxxxx)
- Favorable PYD (reduce to normalize)        ($XXXM)
+ Adverse PYD (add back to normalize)           $XXXM
+/- Cat Normalization (actual vs. expected)  $XXXM
- AOCI Impact (if material one-time swing)   ($XXXM)
= Normalized Owner's Earnings                ~$X,XXXM

Note: For insurers, "owner's earnings" = normalized ROE × beginning book value
```

---

## Peer Selection (Section 7)

### Match On

| Factor | Why It Matters |
|--------|----------------|
| Line mix (P&C / specialty / life) | Completely different economics and risk profiles |
| Geographic focus (US / international / global) | Regulatory, cat exposure, competitive dynamics differ |
| Distribution model (broker / direct / captive) | Expense structures and pricing power vary |
| Float leverage | Higher leverage = higher earnings volatility |
| Reserving conservatism | Affects comparability of all metrics |

### Flag as False Comparables

| Company Type | Why Not Comparable |
|--------------|-------------------|
| Life insurers | Different liabilities, investment profile, regulation |
| Mortgage insurers | Highly levered to single risk factor (housing) |
| Reinsurers vs. primary | Different risk profile, cycle timing, capital needs |
| Captives / mutuals | Different ownership structure, capital constraints |
| Insurtech / startups | No underwriting track record, different growth/profit tradeoff |

---

## Red Flags to Document

| Red Flag | What It Signals |
|----------|-----------------|
| Reliance on favorable PYD >30% of earnings | Past under-earning; future releases unlikely |
| Rising combined ratio trend (3+ years) | Competitive pressure or underpricing |
| Cat losses consistently above guidance | Exposure management issues |
| Growing reinsurance recoverables | Counterparty risk building |
| Expense ratio rising despite premium growth | Operating de-leverage |
| Book value declining despite positive net income | AOCI or capital management issues |

---

## Green Flags to Document

| Green Flag | What It Signals |
|------------|-----------------|
| Consistent favorable PYD for 10+ years | Conservative reserving culture |
| CAY combined ratio <95% through cycle | True underwriting discipline |
| Float cost negative | Earning on free capital |
| BVPS growth >10% CAGR over 10 years | Compounding value |
| Returning excess capital consistently | Capital discipline, alignment |
