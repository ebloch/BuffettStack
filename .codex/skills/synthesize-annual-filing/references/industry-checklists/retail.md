# Retail / Warehouse Club Industry Checklist

Use this checklist for retailers, warehouse clubs (Costco, Sam's Club, BJ's), grocery chains, and general merchandise retailers.

---

## Industry-Specific YAML Metrics

Add these to the `metrics` section:

```yaml
metrics:
  # Standard metrics (always required)
  revenue_m: [number]
  operating_income_m: [number]
  net_income_m: [number]
  fcf_m: [number]
  employees: [number]

  # Retail-specific metrics (REQUIRED)
  comparable_sales_growth_pct: [number]  # Same-store sales growth
  store_count: [number]  # Total stores/warehouses at period end
  gross_margin_pct: [number]  # Gross profit / Revenue
  inventory_turnover_x: [number]  # COGS / Avg Inventory (calculate if not stated)
  ecommerce_pct: [number or null]  # E-commerce as % of total sales (null if not disclosed)

  # For membership-based retailers (Costco, Sam's Club, BJ's)
  membership_fee_revenue_m: [number or null]
  paid_members_m: [number or null]  # Paid membership households (millions)
  renewal_rate_pct: [number or null]  # Primary market renewal rate

  # Optional but valuable
  sales_per_sqft: [number or null]  # If disclosed
  private_label_pct: [number or null]  # Private label % of sales (e.g., Kirkland Signature)
```

---

## Comparable Sales Components

If disclosed, capture the components of comparable sales growth:

- **Traffic / frequency:** Change in number of transactions
- **Average ticket:** Change in average transaction value
- **Mix:** Any commentary on category mix shift

Note in Key Takeaways or What Changed:
> "Comp sales +X% driven by +Y% traffic and +Z% ticket growth"

---

## Margin Analysis

### Gross Margin Drivers

Watch for and note:
- **LIFO/FIFO inventory method** — LIFO creates conservative earnings in inflation
- **Shrinkage trends** — Theft/inventory loss impact on margin
- **Private label mix** — Higher margin private label growth
- **Fuel impact** — For clubs with gas stations, note margin ex-gasoline

### Operating Margin

Key expense categories to track:
- Labor costs (wages, benefits) as % of sales
- Occupancy costs
- E-commerce/delivery costs
- Technology investments

---

## Store Economics

### Unit Economics (if disclosed)

- New store payback period
- Mature store operating margin
- Cannibalization impact from new openings
- Average store size (sq ft)

### Store Count Reconciliation

Track in What Changed:
- Net new stores opened
- Stores closed
- Relocations
- By geography if material

---

## Working Capital Efficiency

Retailers often have favorable working capital dynamics:

- **Negative working capital:** Selling inventory before paying suppliers
- **Inventory days:** Days inventory outstanding
- **Payables days:** Days payables outstanding
- **Cash conversion cycle:** Inventory days + receivables days - payables days

Note if the retailer has a structural working capital advantage.

---

## Membership Model (Warehouse Clubs)

For Costco, Sam's Club, BJ's, etc.:

### Key Metrics

| Metric | Where to Find | YAML Field |
|--------|---------------|------------|
| Total paid members | Business section | `paid_members_m` |
| Renewal rate (primary market) | MD&A | `renewal_rate_pct` |
| Membership fee revenue | Income statement | `membership_fee_revenue_m` |
| Executive member penetration | MD&A/Business | Note in Business Summary |

### Economic Model

Note in Business Summary:
- Membership fees as % of operating profit (often ~100% for Costco)
- Low merchandise margin subsidized by membership fees
- Flywheel dynamics (low prices → traffic → membership → lower prices)

---

## Geographic Concentration Risk

Flag in Risk Factors if:
- Any single state > 20% of U.S. sales
- Any single country > 50% of total sales (outside home market)
- Significant emerging market exposure

---

## Industry-Specific Risks

Search for and flag in Risk Factors:

| Risk | Search Terms | Impact |
|------|--------------|--------|
| **E-commerce competition** | "Amazon", "online", "delivery", "omnichannel" | Traffic/share loss |
| **Labor costs** | "wage", "labor", "minimum wage", "union" | Margin pressure |
| **Tariffs/trade** | "tariff", "import", "trade policy", "duties" | Cost inflation |
| **Shrinkage/theft** | "shrinkage", "theft", "inventory loss", "organized retail crime" | Margin pressure |
| **Food safety** | "recall", "food safety", "contamination" | Reputation/liability |
| **Supply chain** | "supply chain", "logistics", "distribution" | Inventory availability |
| **Credit card fees** | "interchange", "credit card", "payment processing" | Margin pressure |

---

## Questions to Consider

Add to Questions for Further Research if not answered in 10-K:

1. **Unit economics:** What is the payback period on new stores?
2. **E-commerce profitability:** Is e-commerce/delivery margin-accretive or dilutive?
3. **Private label:** What is Kirkland/private label % of sales and trend?
4. **International expansion:** What are returns in newer international markets?
5. **Competitive positioning:** How does pricing compare to Amazon/Walmart?

---

## Watch Items

Flag in Key Takeaways or Risk Factors if concerning:

- [ ] Comp sales decelerating vs. prior year
- [ ] Traffic declining (even if ticket growing)
- [ ] Gross margin compressing
- [ ] E-commerce growth slowing
- [ ] Membership renewal rates declining
- [ ] Inventory growth > sales growth (potential obsolescence)
- [ ] New store growth slowing significantly

---

## Accounting Considerations

### Inventory Method

- **LIFO:** Creates hidden reserve in inflationary periods; more conservative
- **FIFO:** Better matches physical flow but higher taxes in inflation
- Note which method is used and any LIFO charge/benefit impact

### Lease Accounting

- Large operating lease portfolios (stores)
- Note ROU assets and lease liabilities
- Rent expense trends

### Revenue Recognition

- Gift card breakage
- Loyalty program deferrals
- Vendor allowances (rebates, co-op advertising)
