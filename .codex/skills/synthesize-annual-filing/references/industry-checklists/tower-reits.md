# Tower REITs — Mandatory Checklist

**Applies to:** American Tower (AMT), Crown Castle (CCI), SBA Communications (SBAC), Uniti Group (UNIT), and similar tower/infrastructure REITs.

**CRITICAL:** Every item must be addressed (found and included, OR explicitly noted as "not disclosed").

---

## Business Model Overview

Tower REITs lease space on communications infrastructure (towers, small cells, fiber, rooftops) to wireless carriers. Key economic features:
- **High customer concentration:** 3-5 carriers typically = 70-90% of revenue
- **Long-term contracts:** 5-10 year initial terms with multiple renewal options
- **Built-in escalators:** ~3% annual in U.S., CPI-linked internationally
- **Operating leverage:** Minimal incremental cost to add tenants to existing sites
- **Low churn:** Typically 1-3% except during carrier consolidation (e.g., Sprint/T-Mobile)

---

## YAML Frontmatter (Required Fields)

- [ ] `metrics.ffo_m` — Nareit FFO (see note below if not disclosed)
- [ ] `metrics.affo_m` — Adjusted FFO (see note below if not disclosed)
- [ ] `metrics.churn_pct` — Tenant churn as % of billings (can derive from retention rate)
- [ ] `metrics.site_count` — Total towers/sites owned
- [ ] `metrics.adjusted_ebitda_m` — For leverage calculation

**Note on FFO/AFFO:** Some tower REITs (notably CCI) do not disclose FFO/AFFO in their 10-K, using Adjusted EBITDA as their primary non-GAAP metric instead. If FFO/AFFO is not disclosed:
- Set YAML value to `null` with comment: "Not disclosed — uses Adjusted EBITDA"
- Note in Questions for Further Research: "FFO/AFFO: Not disclosed in 10-K — check quarterly supplemental materials or calculate from components"
- Ensure Adjusted EBITDA is captured as the primary metric

**Note on Churn Rate:** If churn is disclosed as a retention rate (e.g., "98-99% retention"), calculate: `churn_pct = 100% - retention_pct`. If disclosed as a dollar amount, calculate: `churn_pct = churn_$ / prior_year_site_rental_revenue`. If neither calculable, note the disclosed range (e.g., "1-2% historical range").

---

## Key Metrics

### Primary Metrics (REQUIRED)
- [ ] FFO and AFFO (NOT GAAP net income as primary metric)
- [ ] Churn rate (% of tenant billings)
- [ ] Site/tower count by geography
- [ ] Net Debt / Adjusted EBITDA (primary leverage metric)
- [ ] Dividend payout ratio (as % of AFFO)

### Organic Growth Components (REQUIRED)
- [ ] Organic tenant billings growth breakdown:
  - Colocations and amendments (new tenants on existing sites)
  - Contractual escalations
  - Churn impact (negative)
- [ ] Contractual escalator terms (% for U.S., CPI-linked for international if applicable)

### Forward Visibility (REQUIRED)
- [ ] Non-cancellable lease revenue backlog ($B) — contracted future revenue

---

## Tenant/Customer Economics

- [ ] **Top tenant concentration by segment** — % of revenue from top 3 customers per geographic segment (e.g., "AT&T, T-Mobile, Verizon = 86% of U.S. & Canada")
- [ ] **Named major tenants** — Identify the specific carriers/customers
- [ ] **Master Lease Agreement (MLA) terms** — If disclosed, note any special arrangements affecting churn or pricing
- [ ] **Average initial lease term** — Typically 5-10 years; note if disclosed
- [ ] **Renewal options** — Multiple renewal periods at tenant option

---

## Geographic Mix

- [ ] **Revenue by geography** — Domestic vs. international split (% of total)
- [ ] **Site count by geography** — Number of towers/sites per region
- [ ] **Pass-through revenue** — For international operations: ground rent recovery, power recovery from tenants
- [ ] **Currency exposure** — Note material FX impacts by region

---

## Traditional REIT Metrics — Tower Equivalents

**IMPORTANT:** Traditional property REIT metrics don't apply directly to towers. Use these tower equivalents:

| Traditional REIT | Tower Equivalent | Notes |
|-----------------|------------------|-------|
| Occupancy rate | **N/A** | Towers have "capacity" not occupancy. Note qualitatively if disclosed ("majority of towers have capacity for additional tenants") |
| Same-store NOI | **Organic tenant billings growth** | Colocations + escalators - churn. This is the tower industry's equivalent of same-store performance |
| Rent spreads | **Contractual escalators** | Escalators are contractual (~3% U.S., CPI internationally), not market-driven at renewal |
| Lease expiration schedule | **Non-cancellable backlog** | Forward contracted revenue ($B). Tower leases don't have traditional expiration schedules |
| Cap rates | **N/A** | Tower acquisitions don't typically disclose cap rates |
| NOI | **Segment gross margin** | Revenue less property operating expenses (excludes D&A, SG&A) |

**In the memo:** Include the following mapping table explicitly in Business Summary or as a separate section:

```markdown
**Traditional REIT Metrics — Tower Equivalents:**

| Traditional REIT | This Company | Notes |
|-----------------|--------------|-------|
| Occupancy rate | N/A | [Qualitative note on capacity if disclosed] |
| Same-store NOI | [Organic growth %] | Colocations + escalators - churn |
| Rent spreads | [Escalator %] | [e.g., "~3% contractual" or "Not disclosed"] |
| Lease expiration schedule | $[X]B backlog | [X] year weighted avg remaining |
| Cap rates | N/A | Not disclosed |
```

This table is **REQUIRED** for tower REITs to ensure readers understand why traditional metrics are absent.

---

## Watch Items (Flag If Moving in Concerning Direction)

- [ ] **Churn rate increasing** — Especially if >2%; flag carrier consolidation impacts
- [ ] **Escalator rates declining** — Watch for contract renegotiations
- [ ] **Tenant concentration increasing** — Carrier consolidation creates binary risk
- [ ] **Net leverage exceeding 6x** — Net Debt / EBITDA above 6x is elevated for tower REITs
- [ ] **AFFO payout ratio exceeding 90%** — Limited capacity for debt paydown or growth
- [ ] **International currency headwinds** — Material FX impacts quarter-over-quarter
- [ ] **Technology disruption mentions** — Small cells, DAS, LEO satellites as tower substitutes

---

## Data Centers Sub-Segment (if applicable)

If the tower REIT has data center operations (e.g., AMT/CoreSite):

- [ ] Data center revenue and YoY growth rate
- [ ] NRSF (net rentable square feet) or equivalent capacity metric
- [ ] Interconnection revenue (if disclosed separately)
- [ ] Data center segment gross margin
- [ ] Geographic distribution of data center facilities

---

## Debt & Capital Structure

- [ ] **Debt maturity schedule** — Summary of upcoming maturities
- [ ] **Fixed vs. floating rate mix** — Important given leverage levels
- [ ] **Credit ratings** — If disclosed in 10-K (often investment grade)
- [ ] **Covenant compliance** — Note any covenant discussions if disclosed

---

## Key Questions to Answer

The memo should address or flag for further research:

1. What is the churn outlook? (Is current elevated churn temporary or structural?)
2. What is the international growth profile? (Are emerging markets replicating U.S. network densification?)
3. What is the data center strategy? (If applicable — growth platform or non-core?)
4. What is the capacity for incremental colocation revenue? (Operating leverage potential)
5. How does leverage compare to financial policy targets?
