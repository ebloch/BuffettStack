# SaaS / Subscription Businesses — Mandatory Checklist

**CRITICAL:** Every item below must be addressed:
- If data is in the 10-K → include it
- If data is NOT in the 10-K → explicitly state "Not disclosed" in YAML or body
- If data is derivable (e.g., gross retention from attrition) → calculate and note the derivation

---

## YAML Frontmatter (Required Fields)

```yaml
metrics:
  # Core SaaS metrics (ALL required - use "not_disclosed" or null if unavailable)
  arr_m: [number or null]              # Annual Recurring Revenue
  mrr_m: [number or null]              # Monthly Recurring Revenue (alternative to ARR)
  net_retention_pct: [number or null]  # Net Dollar Retention / Net Revenue Retention
  gross_retention_pct: [number or null] # Gross Retention (logo/customer retention)
  rpo_m: [number]                      # Remaining Performance Obligations (total)
  crpo_m: [number]                     # Current RPO (next 12 months)
  gross_margin_pct: [number]           # Subscription gross margin preferred; total acceptable
  rule_of_40: [number]                 # Calculated: revenue_growth_pct + fcf_margin_pct
```

**Metric Availability by Company (Common Patterns):**
| Company | ARR | NRR | Gross Retention | RPO | Notes |
|---------|-----|-----|-----------------|-----|-------|
| Salesforce | No | No | Implied (~attrition) | Yes | cRPO is key forward metric |
| ServiceNow | Yes | Yes | Yes | Yes | Full disclosure |
| Adobe | Yes | Yes | No | Yes | Strong NRR disclosure |
| Workday | No | Yes | Yes | Yes | |
| Snowflake | No | Yes | No | Yes | Strong NRR (>100%) focus |

---

## Key Metric Definitions

**Understand the difference between gross and net retention:**

| Metric | Definition | What It Measures | Typical Range |
|--------|------------|------------------|---------------|
| **Gross Retention** | (Prior Year Revenue - Churned Revenue) / Prior Year Revenue | Customer/logo retention | 85-95% |
| **Net Retention** (NRR/NDR) | (Prior Year Revenue - Churn + Expansion) / Prior Year Revenue | Revenue retention including upsell | 100-130% |
| **Attrition Rate** | Revenue lost from churned customers / Total revenue | Opposite of gross retention | 5-15% |

**Key Relationship:**
- Gross Retention ≈ 100% - Attrition Rate
- If 10-K discloses "~8% attrition," gross retention is ~92%
- Net Retention = Gross Retention + Expansion Rate

**Do NOT conflate attrition rate with net retention.** They measure different things.

---

## Key Metrics Extraction

### Required (Must Appear in YAML or Body)

- [ ] **ARR/MRR** — Annual or monthly recurring revenue
  - If not disclosed: `arr_m: null` in YAML + "ARR: Not disclosed" in Business Summary
  - Some companies (Salesforce) don't report ARR; use RPO as proxy

- [ ] **Net Dollar Retention (NDR/NRR)** — Revenue retention including expansion
  - If not disclosed: `net_retention_pct: null` in YAML + "Net retention: Not disclosed" in Business Summary
  - Do NOT derive from attrition — attrition measures gross retention, not net

- [ ] **Gross Retention** — Customer/logo retention rate
  - If disclosed as "attrition rate," calculate: `gross_retention_pct = 100 - attrition_rate`
  - Note derivation in memo: "~92% gross retention (implied from 8% attrition)"

- [ ] **RPO (Total)** — Remaining performance obligations
  - Include YoY growth rate
  - For most SaaS, this is the primary forward revenue indicator

- [ ] **cRPO (Current)** — RPO expected to be recognized in next 12 months
  - Include YoY growth rate
  - Compare cRPO growth to revenue growth (see Watch Items)

- [ ] **Gross Margin** — Subscription gross margin preferred; total acceptable
  - Calculate from income statement if not explicitly stated
  - Subscription gross margin is more meaningful than total (excludes services)

- [ ] **Rule of 40** — Combined growth + profitability score
  - **Formula:** Revenue Growth % + FCF Margin %
  - **FCF Margin:** Free Cash Flow / Revenue
  - **Example:** 9% revenue growth + 33% FCF margin = 42 (passing)
  - Rule of 40 >40 = healthy SaaS economics
  - Include explicit calculation in Financial Snapshot or Key Takeaways

### Optional (Include If Disclosed)

- [ ] **CAC Payback Period** — Months to recover customer acquisition cost
  - Rarely disclosed in 10-K; more common in investor presentations
  - If not disclosed: "CAC payback: Not disclosed in 10-K"

- [ ] **LTV/CAC Ratio** — Lifetime value / customer acquisition cost
  - Rarely disclosed in 10-K

- [ ] **Customer Count** — Total number of customers
  - Some SaaS (Snowflake, Datadog) disclose; most don't
  - Enterprise SaaS typically doesn't disclose total count

- [ ] **Large Customer Concentration** — % of revenue from top customers
  - Required disclosure: >10% customer concentration
  - "No customer >10%" is common and should be noted

---

## Watch Items (REQUIRED Evaluation)

**For each Watch Item, explicitly assess in Risk Factors or Key Takeaways:**

| Watch Item | How to Assess | Red Flag Threshold |
|------------|---------------|-------------------|
| **Net retention declining** | Compare to prior year if disclosed | <100% or declining trend |
| **RPO growth < Revenue growth** | Compare YoY growth rates | cRPO growth < revenue growth |
| **Gross margin compression** | Compare to prior year | Declining for 2+ years |
| **Attrition increasing** | Compare to prior year | Rising trend |
| **Large customer concentration increasing** | Compare to prior year | Any increase in top-customer % |

**Output Requirement:**
In **Key Takeaways** or **Risk Factors**, include an explicit assessment:
- "RPO growth (+11%) exceeds revenue growth (+9%), suggesting improving forward visibility"
- "RPO growth (+9%) trails cRPO growth (+11%), worth monitoring for deceleration"
- "No customer >10% of revenue; concentration risk remains low"

---

## Common 10-K Data Patterns

### What You'll Usually Find:
- Revenue breakdown by product/cloud
- RPO and cRPO with growth rates
- Attrition rate (often as "approximately X%")
- Gross margin (calculable from financials)
- Geographic revenue mix
- "No customer >10%" concentration statement

### What You Often Won't Find:
- ARR (many enterprise SaaS don't disclose)
- Net dollar retention (increasingly disclosed but not universal)
- Customer count (enterprise SaaS typically doesn't)
- CAC payback / LTV/CAC (rarely in 10-K)
- Cohort data

### Handling Missing Data:
When a key SaaS metric is not in the 10-K, you MUST:
1. Set YAML field to `null` or omit
2. Explicitly note "Not disclosed" in the relevant body section
3. Suggest alternative proxies if available (e.g., "Use cRPO growth as proxy for contract health")

---

## Validation Checklist

Before finalizing the memo, verify:

- [ ] All YAML SaaS metrics populated (with `null` for undisclosed)
- [ ] Gross vs. net retention correctly distinguished (NOT conflated)
- [ ] Rule of 40 calculated with explicit formula shown
- [ ] RPO growth vs. revenue growth comparison stated
- [ ] Watch Items explicitly assessed in body
- [ ] "Not disclosed" stated for any missing required metrics
- [ ] Attrition rate converted to gross retention (if attrition disclosed)
- [ ] Subscription gross margin captured (or total if subscription not broken out)
