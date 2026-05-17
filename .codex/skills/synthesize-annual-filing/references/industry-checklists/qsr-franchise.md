# QSR / Franchise Restaurant Industry Checklist

Use this checklist for Quick Service Restaurant (QSR) companies that operate primarily through franchising (e.g., McDonald's, Yum Brands, Restaurant Brands International, Domino's, Wingstop).

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

  # QSR-specific metrics (REQUIRED)
  comparable_sales_growth_pct: [number]  # System-wide same-store sales growth
  store_count: [number]  # Total system restaurants at period end
  franchise_pct: [number]  # % of restaurants that are franchised
  systemwide_sales_m: [number]  # Total sales across all restaurants (company + franchise)

  # Franchise economics
  royalty_rate_pct: [number or null]  # If disclosed (typically 4-6%)
  initial_franchise_fee_k: [number or null]  # Per-unit initial fee if disclosed

  # Digital/Loyalty (increasingly important)
  loyalty_members_m: [number or null]  # Active loyalty members in millions
  digital_sales_pct: [number or null]  # Digital (app + delivery) as % of sales
  delivery_sales_pct: [number or null]  # Delivery as % of sales if disclosed separately

  # Unit economics (if disclosed)
  average_unit_volume_k: [number or null]  # AUV per restaurant in thousands

  # Margins
  franchised_margin_pct: [number]  # Franchise revenue margin (franchise revenue / operating income from franchised)
  company_owned_margin_pct: [number or null]  # Company-owned restaurant margin if disclosed
```

**Note on gross_margin_pct:** For franchise-heavy QSR companies, traditional "gross margin" is ambiguous. Use:
- `franchised_margin_pct` for franchise segment margins
- `company_owned_margin_pct` for company-operated segment margins
- If using `gross_margin_pct`, clarify in a footnote what it represents

---

## Retail Metrics That Are N/A for Franchise QSR

These metrics from the retail checklist typically **do not apply** to franchise-heavy QSR:

| Metric | Why N/A | What to Use Instead |
|--------|---------|---------------------|
| `inventory_turnover_x` | Minimal company inventory; franchisees hold inventory | Note "N/A - franchise model" in YAML |
| `membership_fee_revenue_m` | Not applicable (unless loyalty is fee-based) | `loyalty_members_m` for engagement metrics |
| `paid_members_m` | Not applicable | Use `loyalty_members_m` (free loyalty programs) |
| `ecommerce_pct` | Less relevant for QSR | Use `digital_sales_pct` or `delivery_sales_pct` |
| `shrinkage` | Franchisee responsibility | Note if disclosed as franchisee concern |

---

## Comparable Sales Decomposition

If disclosed, capture the components of comparable sales growth:

- **Traffic / guest count:** Change in number of transactions
- **Average check / ticket:** Change in average transaction value
- **Mix:** Menu mix shift (if disclosed)

**Important:** If only directional commentary is given (e.g., "positive average check growth offset by negative guest counts"), note this. Do not fabricate specific percentages.

Note in Key Takeaways or What Changed:
> "Comp sales +X% driven by [traffic/ticket] component; [other component] was [positive/flat/negative]"

Or if breakdown unavailable:
> "Comp sales +X% — traffic vs. ticket breakdown not quantified in filing"

---

## Franchise Economics

### Key Metrics to Extract

| Metric | Where to Find | YAML Field |
|--------|---------------|------------|
| Franchise revenue | Income statement | Part of `revenue_m` |
| Royalty rate | MD&A / Business | `royalty_rate_pct` |
| Initial franchise fee | Business section | `initial_franchise_fee_k` |
| Franchise margin | Segment data | `franchised_margin_pct` |
| Company-owned margin | Segment data | `company_owned_margin_pct` |

### Economic Model

Note in Business Summary:
- Revenue composition (franchise fees/royalties vs. company-owned sales)
- Margin differential between franchised and company-owned
- Real estate ownership model (if company owns land/buildings)
- Rent economics (if company collects rent from franchisees)

For heavily franchised models (>90%), emphasize:
- Royalty stream stability (% of systemwide sales)
- Real estate ownership as moat
- Capital-light nature of franchise model

---

## Unit Growth and Development

Track in What Changed and Key Takeaways:

- Gross openings
- Closures
- Net unit growth
- Development targets (e.g., "50,000 restaurants by 2027")
- Geographic expansion priorities

Note unit growth rate:
> "Net new units +X.X% YoY ([N] net additions)"

---

## Digital and Delivery

Increasingly critical for QSR:

| Metric | Search Terms | Notes |
|--------|--------------|-------|
| **Loyalty penetration** | "loyalty", "rewards", "members" | 90-day active users if disclosed |
| **Digital sales** | "digital", "app", "mobile" | % of sales through digital channels |
| **Delivery** | "delivery", "third-party", "aggregator" | % of sales via delivery |
| **Drive-thru** | "drive-thru", "drive thru" | % of restaurants with drive-thru |

---

## Industry-Specific Risks

Search for and flag in Risk Factors:

| Risk | Search Terms | Impact |
|------|--------------|--------|
| **Food safety** | "food safety", "E. coli", "salmonella", "outbreak", "recall" | Reputation/traffic |
| **Franchisee health** | "franchisee", "operator", "default", "termination" | Revenue stability |
| **Labor availability** | "labor", "staffing", "wage", "minimum wage" | Cost/service quality |
| **Commodity costs** | "commodity", "beef", "chicken", "food costs" | Franchisee margins → menu pricing |
| **Digital competition** | "delivery", "aggregator", "DoorDash", "Uber Eats" | Take rate pressure |
| **Consumer spending** | "consumer", "discretionary", "value" | Traffic trends |
| **International** | "geopolitical", "currency", "international" | For global QSR brands |

**Note:** For franchise models, labor and commodity risks primarily affect franchisees, which impacts their economics and ability to pay royalties. Note this distinction.

---

## Questions to Consider

Add to Questions for Further Research if not answered in 10-K:

1. **Franchisee unit economics:** What is the typical franchisee 4-wall margin?
2. **AUV trends:** Are average unit volumes growing with comp sales or is it traffic-driven?
3. **Remodel economics:** What is ROI on remodel/modernization programs?
4. **Digital attribution:** What % of loyalty members are incremental vs. shifted from non-digital?
5. **Delivery profitability:** What is the margin profile of delivery vs. in-store orders?

---

## Watch Items

Flag in Key Takeaways or Risk Factors if concerning:

- [ ] Negative traffic despite positive comps (pricing reaching limits)
- [ ] Comp sales decelerating vs. prior year
- [ ] Franchisee margins under pressure
- [ ] Unit growth slowing vs. targets
- [ ] Digital sales growth decelerating
- [ ] International segment underperforming
- [ ] Food safety incidents mentioned
- [ ] Franchise agreement renewals declining

---

## Accounting Considerations

### Revenue Recognition

- Franchise revenue recognized as royalties earned (% of sales)
- Initial franchise fees deferred and recognized over franchise term
- Rent revenue from franchisees (if company owns real estate)

### Segment Reporting

Typical segments for global QSR:
- U.S. (or home market)
- International Operated Markets (company-owned heavy)
- International Developmental Licensed Markets (franchise heavy)

Note if segments have different franchise %:
> "U.S. 95% franchised vs. IOM 89% franchised"

### Systemwide Sales vs. Revenue

**Critical distinction:**
- **Systemwide sales:** Total sales across all restaurants (company + franchise)
- **Company revenue:** Only what flows through company P&L (royalties + company-owned sales)

Always include systemwide_sales_m in YAML for QSR — it's the true scale metric.
