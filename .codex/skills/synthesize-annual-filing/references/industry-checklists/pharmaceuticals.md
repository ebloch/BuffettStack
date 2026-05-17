# Pharmaceuticals / Biotech Checklist

For pharmaceutical and biotechnology companies (Eli Lilly, Pfizer, Merck, AbbVie, Johnson & Johnson Pharma, Bristol-Myers Squibb, Amgen, Gilead, Regeneron, Biogen, etc.)

---

## Industry-Specific YAML Metrics

Add to `metrics:` section:

```yaml
metrics:
  # Standard (required)
  revenue_m: [number]
  operating_income_m: [number]
  net_income_m: [number]
  fcf_m: [number]
  employees: [number]

  # Pharma-specific (required)
  gross_margin_pct: [number]  # Typically 70-85% for branded pharma
  rd_expense_m: [number]  # R&D expense absolute
  rd_pct_revenue: [number]  # R&D as % of revenue (typically 15-25%)

  # Pipeline metrics (if disclosed)
  pipeline_phase3_count: [number or null]  # Compounds in Phase 3
  pipeline_submitted_count: [number or null]  # Compounds under regulatory review
```

---

## Business Model Elements

### Product Mix (REQUIRED)
- [ ] **Top products by revenue** — List products >5% of revenue with YoY growth
- [ ] **Therapeutic area breakdown** — Revenue by therapeutic area (oncology, immunology, cardiometabolic, neuroscience, etc.)
- [ ] **Product concentration** — Explicitly state concentration (e.g., "Top 3 products = X% of revenue")

### Geographic Mix (REQUIRED)
- [ ] **U.S. vs. International split** — At minimum, U.S. % and international %
- [ ] **Major market breakdown** — If disclosed: Europe, Japan, China, Rest of World
- [ ] **International growth rate** — Compare U.S. vs. OUS growth rates

### Pipeline Summary (REQUIRED)
- [ ] **Key late-stage compounds** — List Phase 3 and submitted compounds with indications
- [ ] **Next major launches** — Expected approvals within 12-24 months
- [ ] **Breakthrough/Priority designations** — Any FDA Breakthrough Therapy or Priority Review

---

## Patent / Exclusivity Timeline (CRITICAL)

Patent expiration is the single most important risk for branded pharma.

- [ ] **Patent cliff exposure** — State % of revenue facing LOE within 5 years
- [ ] **Key product patents** — For top 5 products: compound patent expiry (U.S., EU, Japan)
- [ ] **Biologics exclusivity** — For biologics: data exclusivity periods (12 years U.S., 10 years EU)
- [ ] **Pending patent challenges** — Any ANDA/BPCIA challenges disclosed

### YAML Addition for Patents

If key products have disclosed patent timelines, add to Key Takeaways or Risk Factors:
- "Tirzepatide (Mounjaro/Zepbound) compound patent extends to 2036 (U.S.), 2037 (EU)"
- "Trulicity LOE in 2027 (U.S.) — represents X% of current revenue"

---

## Pricing & Reimbursement (REQUIRED)

- [ ] **Realized price trends** — Volume vs. price components of growth
- [ ] **IRA exposure** — Any products subject to Medicare drug price negotiation
- [ ] **Gross-to-net adjustments** — Rebate liability growth vs. revenue growth
- [ ] **340B exposure** — If disclosed, impact of 340B Drug Pricing Program
- [ ] **Payer concentration** — Wholesaler concentration (McKesson, Cencora, Cardinal)

---

## Industry-Specific Risks (REQUIRED in Risk Factors)

Must search for and include if material:

- [ ] **Product concentration** — If any product >20% of revenue, highlight as key risk
- [ ] **Patent expiration / LOE** — Near-term (within 5 years) loss of exclusivity
- [ ] **Pricing pressure** — Government price controls, IRA drug negotiations, international reference pricing
- [ ] **Clinical development risk** — Phase 3 failures, regulatory delays
- [ ] **Competition** — Biosimilar/generic entry, competing mechanisms, compounding pharmacy risk
- [ ] **Manufacturing / supply chain** — Capacity constraints, single-source materials, China exposure
- [ ] **Regulatory** — FDA complete response letters, post-market safety requirements, label changes

---

## Accounting Quirks

### Revenue Recognition
- [ ] **Gross-to-net adjustments** — Rebates, chargebacks, returns, copay assistance
- [ ] **Rebate liability** — Compare rebate liability growth to revenue growth (should be proportional)

### R&D Accounting
- [ ] **Acquired IPR&D** — Large one-time charges for in-process R&D from acquisitions
- [ ] **Milestone payments** — Upfront vs. milestone breakdown if material

### Intangibles
- [ ] **Goodwill concentration** — Total goodwill and impairment risk
- [ ] **Intangible amortization** — Acquired product rights amortization

---

## Key Ratios to Calculate

| Ratio | Formula | Benchmark |
|-------|---------|-----------|
| Gross Margin | Gross Profit / Revenue | 70-85% typical for branded pharma |
| R&D Intensity | R&D Expense / Revenue | 15-25% for research-driven pharma |
| SG&A Ratio | SG&A / Revenue | 20-30% typical |
| FCF Conversion | FCF / Net Income | >80% healthy |

---

## Watch Items

Red flags specific to pharma:

- [ ] **Rebate liability growing faster than revenue** — May indicate pricing pressure
- [ ] **R&D intensity declining** — May indicate pipeline concerns
- [ ] **Multiple large acquisitions** — May indicate organic growth challenges
- [ ] **A/R growth >> Revenue growth** — Investigate channel dynamics
- [ ] **Recurring "one-time" IPR&D charges** — May indicate M&A-dependent growth model

---

## Questions to Consider

1. What % of revenue faces patent expiration in the next 5 years?
2. How does pipeline depth compare to LOE exposure?
3. What is the competitive landscape for key growth products?
4. How is pricing power evolving (realized price trends)?
5. What manufacturing capacity is being built and why?
