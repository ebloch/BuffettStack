# SaaS/Cloud Software — Business Economics Checklist

**Trigger Keywords:** "software as a service", "SaaS", "cloud software", "subscription software", "recurring revenue", "enterprise software"

---

## Required Metrics (Section 4)

### Growth Metrics (ALL REQUIRED)

| Metric | Benchmark | Why It Matters |
|--------|-----------|----------------|
| ARR Growth | >25% strong growth; 15-25% healthy; <10% maturing | Core business momentum |
| Net Revenue Retention (NRR) | >120% excellent; 110-120% good; <100% churn issue | Expansion minus churn |
| Gross Revenue Retention | >90% strong; 85-90% acceptable; <85% concerning | Pure churn metric |
| Remaining Performance Obligations (RPO) | Growing faster than revenue = pipeline strength | Contracted future revenue |
| Customer Count Growth | Positive; declining concerning | Footprint expansion |

### Profitability Metrics (ALL REQUIRED)

| Metric | Benchmark | Why It Matters |
|--------|-----------|----------------|
| Gross Margin | >75% excellent; 70-75% good; <65% concerning | Scalability indicator |
| Rule of 40 (Growth + FCF Margin) | >40% strong; 30-40% adequate; <30% concerning | Growth vs. profitability balance |
| Operating Margin (Non-GAAP) | Positive and expanding | Path to profitability |
| Free Cash Flow Margin | >20% excellent; 10-20% healthy; negative concerning at scale | Cash generation |

### Unit Economics (ALL REQUIRED)

| Metric | Benchmark | Why It Matters |
|--------|-----------|----------------|
| LTV/CAC | >3x good; 2-3x acceptable; <2x concerning | Customer economics efficiency |
| CAC Payback Period | <18 months strong; 18-24 months acceptable; >24 months concerning | Sales efficiency |
| Magic Number | >0.75 efficient; 0.5-0.75 moderate; <0.5 inefficient | Sales and marketing efficiency |

---

## Required Quirks (Section 3)

### 1. Deferred Revenue Dynamics

- **What:** Subscription billings received in advance recognized ratably over service period
- **Distortion:** Revenue lags billings; strong bookings quarter shows deferred revenue build, not revenue pop
- **Adjustment:** Track billings growth and RPO alongside revenue; understand billing cadence (annual vs. monthly)

### 2. Stock-Based Compensation

- **What:** SBC often 15-25% of revenue for growth SaaS; creates significant GAAP vs. non-GAAP spread
- **Distortion:** Non-GAAP margins look much better; GAAP profitability often negative; dilution real
- **Adjustment:** ALWAYS deduct SBC from margins for valuation; track share count growth; SBC is real expense

### 3. Capitalized Software Development Costs

- **What:** Internal-use software costs capitalized and amortized; varies significantly by company
- **Distortion:** Some capitalize aggressively (improves GAAP margins); others expense all (worse GAAP margins)
- **Adjustment:** Compare R&D as % of revenue across peers; understand capitalization policy; FCF more reliable

### 4. Contract Assets and Liabilities (Multi-Year Deals)

- **What:** Large enterprise deals create contract assets (revenue ahead of billing) and liabilities (billing ahead of revenue)
- **Distortion:** Balance sheet swings with deal timing; revenue recognition may not match cash
- **Adjustment:** Track collections vs. revenue recognition; understand deal term lengths

---

## Valuation Guidance (Section 8)

### Primary Valuation Method

**EV/Revenue with growth and margin context** (for growth stage)

| Growth + Rule of 40 | Justified EV/Revenue | Rationale |
|---------------------|----------------------|-----------|
| >30% growth, Rule of 40 >50% | 12-20x | Premium for efficient growth |
| 20-30% growth, Rule of 40 >40% | 8-12x | Strong growth company |
| 10-20% growth, Rule of 40 >30% | 5-8x | Moderate growth |
| <10% growth | 3-6x | Mature SaaS |

**EV/FCF** (for profitable, mature stage)

| FCF Margin | Justified EV/FCF | Rationale |
|------------|------------------|-----------|
| >25% FCF margin | 25-35x | Premium for cash generation |
| 15-25% FCF margin | 18-25x | Solid profitability |
| 5-15% FCF margin | 12-18x | Emerging profitability |

### Secondary Methods

- **P/E (GAAP-adjusted):** Add back SBC, use 25-40x for growth
- **ARR Multiple:** Compare to enterprise value
- **Sum-of-Parts:** For platforms with multiple products

### Methods to AVOID

| Method | Why Inappropriate |
|--------|-------------------|
| GAAP P/E | SBC makes meaningless for growth |
| Non-GAAP P/E without SBC | Overstates earnings |
| P/B | Intangibles and SBC distort |
| Simple Revenue Multiple | Must adjust for growth and profitability |

### Owner's Earnings Adjustments

```
GAAP Net Income                               ($XXXM) (FYxxxx)
+ Stock-Based Compensation                    $XXXM [add back]
+ Depreciation & Amortization                 $XXXM [per 10-K]
- Maintenance CapEx                           ($XXXM) [EST: 60% of capex]
- Capitalized Software Development            ($XXXM) [real investment]
= Non-GAAP Owner's Earnings                  ~$XXXM

Alternative: Start with FCF
Free Cash Flow                                $XXXM (FYxxxx)
- Stock-Based Compensation (real cost)        ($XXXM)
= SBC-Adjusted FCF (True Owner's Earnings)   ~$XXXM

Note: For unprofitable SaaS, focus on path to FCF margin
```

---

## Peer Selection (Section 7)

### Match On

| Factor | Why It Matters |
|--------|----------------|
| Target market (SMB vs. mid-market vs. enterprise) | Different unit economics and growth rates |
| Growth rate cohort | Similar maturity |
| Gross margin profile | Scalability comparability |
| Product category (horizontal vs. vertical) | Different TAM and competition |
| Go-to-market model (sales-led vs. PLG) | Different cost structures |

### Flag as False Comparables

| Company Type | Why Not Comparable |
|--------------|-------------------|
| Legacy perpetual license software | Different model and metrics |
| Consumer subscription (Netflix) | Different unit economics |
| Infrastructure/IaaS (AWS) | Different gross margin and capex |
| Transactional software | Different revenue recognition |
| Hardware+software (Apple) | Hardware economics dominant |

---

## Red Flags to Document

| Red Flag | What It Signals |
|----------|-----------------|
| NRR declining below 100% | Churn exceeding expansion |
| Gross margin compression | Infrastructure or service cost issues |
| RPO growth below revenue growth | Bookings slowdown |
| CAC payback extending | Sales efficiency declining |
| SBC >25% of revenue growing | Excessive dilution |
| Rule of 40 declining | Growth/profitability balance deteriorating |

---

## Green Flags to Document

| Green Flag | What It Signals |
|------------|-----------------|
| NRR >130% sustained | Strong expansion economics |
| Gross margin >80% | Highly scalable model |
| FCF margin expanding toward 25%+ | Cash machine emerging |
| Enterprise deals expanding | Stickiness improving |
| Land-and-expand working | Efficient growth model |
