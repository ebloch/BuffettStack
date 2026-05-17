# Luxury Goods Industry Checklist

Use this checklist for luxury goods companies including Hermès, LVMH, Kering, Richemont, Burberry, Prada, and similar premium/luxury brands.

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

  # Luxury-specific metrics (REQUIRED)
  organic_growth_pct: [number]  # Constant currency, like-for-like growth (exclude FX, M&A)
  operating_margin_pct: [number]  # Operating income / Revenue
  gross_margin_pct: [number]  # Gross profit / Revenue (proxy for pricing power)

  # Geographic revenue breakdown (% of total)
  revenue_europe_pct: [number]
  revenue_americas_pct: [number]
  revenue_asia_pacific_pct: [number]  # Excluding Japan (standard for luxury)
  revenue_japan_pct: [number]  # Japan reported separately (important for luxury)
  revenue_other_pct: [number or null]

  # Store/distribution metrics
  store_count: [number]  # Directly operated stores (DOS)
  store_count_change: [number]  # Net openings YoY

  # Optional but valuable
  capex_pct_revenue: [number or null]  # CapEx intensity (luxury often 4-8%)
  inventory_days: [number or null]  # Days inventory outstanding
```

---

## Product Category Breakdown

Luxury conglomerates typically report by product category. Capture in segment table:

### Hermès Categories
- Leather goods & saddlery (core — watch closely)
- Ready-to-wear & accessories
- Silk & textiles
- Perfumes & beauty
- Watches
- Other Hermès métiers

### LVMH Categories
- Fashion & Leather Goods (Louis Vuitton, Dior, etc.)
- Selective Retailing (Sephora, DFS)
- Perfumes & Cosmetics
- Watches & Jewelry
- Wines & Spirits

### Kering Categories
- Gucci (dominant — watch margin closely)
- Saint Laurent
- Bottega Veneta
- Other Houses (Balenciaga, Alexander McQueen, etc.)
- Kering Eyewear

Note in Key Takeaways which category drove growth and any notable margin changes.

---

## Geographic Analysis

Luxury is highly sensitive to regional dynamics:

### Asia-Pacific (ex-Japan)
- China is typically 30-35% of global luxury demand
- Track "Greater China" or "Mainland China" specifically
- Note any store count changes in China
- Watch for government policy impacts (crackdown on gifting, etc.)

### Japan
- Reported separately due to different consumer dynamics
- Yen weakness can boost tourism spending
- Note if "Japan" growth is driven by locals vs. tourists

### Europe
- Tourist spending vs. local demand
- Note any VAT refund or tourism commentary

### Americas
- Aspirational vs. absolute luxury positioning
- Note any "normalization" commentary post-COVID

**Key metric:** Organic growth by region (constant currency, comparable scope)

---

## Distribution Channel Mix

Track directly operated stores (DOS) vs. wholesale:

| Channel | Implications |
|---------|--------------|
| **Directly operated stores** | Higher margin, better brand control, customer data |
| **Wholesale** | Broader reach, lower CapEx, less control |
| **E-commerce** | Growing channel, margin can vary |

Note in Business Summary:
- DOS % of revenue (trend matters)
- E-commerce % of revenue (if disclosed)
- Any "selective distribution" strategy commentary

**Hermès specificity:** Hermès limits production and rarely wholesales — note if DOS is >90%.

---

## Pricing Power Indicators

Luxury business model depends on pricing power. Look for:

### Direct Indicators
- Price increase announcements (typically annual)
- ASP (average selling price) growth vs. volume growth
- "Price-mix" contribution to organic growth

### Indirect Indicators
- Gross margin stability or expansion
- "Desirability" or "brand equity" commentary
- Waiting lists (especially Hermès bags)
- Resale market premium over retail

Note in Key Takeaways if pricing power is strong/weakening.

---

## Production & Supply Chain

Luxury brands often emphasize craftsmanship:

### Manufacturing Strategy
- In-house vs. outsourced production
- Country of origin (France, Italy, Switzerland, etc.)
- Vertical integration (tanneries, ateliers, etc.)

### Capacity Constraints
- New production facilities (CapEx)
- Leather goods capacity (Hermès constraint)
- Artisan hiring and training programs

### Raw Material Costs
- Leather, precious metals, gemstones
- Any hedging commentary
- Currency impact on sourcing costs

---

## Industry-Specific Risks

Search for and flag in Risk Factors:

| Risk | Search Terms | Impact |
|------|--------------|--------|
| **China slowdown** | "China", "Greater China", "Asia Pacific" | 30-35% of demand |
| **Currency volatility** | "foreign exchange", "FX", "currency", "hedging" | Revenue translation, tourism |
| **Counterfeiting** | "counterfeit", "intellectual property", "trademark" | Brand dilution |
| **Fashion risk** | "desirability", "trend", "creative director" | Revenue volatility |
| **Supply chain** | "leather", "artisan", "capacity", "sourcing" | Production constraints |
| **Tourism** | "tourist", "travel retail", "duty-free" | Especially Japan, Europe |
| **Digital disruption** | "e-commerce", "digital", "social media" | Channel shift |
| **Sustainability/ESG** | "environment", "sustainable", "animal welfare" | Reputation, regulation |
| **Key person risk** | "designer", "creative director", "succession" | Creative continuity |

---

## ESG/Sustainability Section

European filings (especially URDs) include extensive ESG disclosure:

### Environmental
- Carbon emissions (Scope 1, 2, 3)
- Sustainable materials (% of sourcing)
- Water usage, waste reduction
- Animal welfare policies

### Social
- Artisan employment and training
- Supply chain labor practices
- Diversity metrics

### Governance
- Family ownership structure (common in luxury)
- Executive compensation
- Board independence

Note major ESG commitments in Sustainability section or Key Takeaways if material.

---

## Valuation Considerations

Luxury trades at premium multiples due to:

- High ROIC and asset-light (relative to inventory)
- Pricing power and margin resilience
- Long-term brand value (100+ year brands)
- Scarcity/exclusivity strategy

### Key Multiples
- P/E: Luxury often trades 25-40x
- EV/EBITDA: Typically 15-25x
- Note forward organic growth rate when assessing valuation

### Brand Value
- Impossible to replicate established brands
- Note if brand rankings (Interbrand, etc.) are cited
- Heritage and history matter

---

## Questions to Consider

Add to Questions for Further Research if not answered:

1. **China exposure:** What % of revenue is from Chinese consumers (including tourists)?
2. **E-commerce strategy:** What is digital % of sales and is it margin-accretive?
3. **Capacity constraints:** Is production capacity limiting growth (especially leather goods)?
4. **Brand health:** Are there waiting lists? What is resale market premium?
5. **Creative leadership:** Who is creative director and how long have they been in role?
6. **Pricing strategy:** What were recent price increases and reception?

---

## Watch Items

Flag in Key Takeaways or Risk Factors if concerning:

- [ ] Organic growth decelerating (especially in core categories)
- [ ] Asia-Pacific/China growth slowing significantly
- [ ] Gross margin declining (pricing power concern)
- [ ] Inventory growing faster than revenue (potential markdown risk)
- [ ] Wholesale % increasing (brand control erosion)
- [ ] Creative director change (transition risk)
- [ ] Promotional activity increasing (brand erosion risk)
- [ ] Store closures exceeding openings

---

## Accounting Considerations

### Currency Translation
- Revenue in local currencies, consolidated in EUR (for European groups)
- Note constant currency vs. reported growth
- Hedging policies and FX impact on margin

### Inventory
- Luxury rarely marks down — watch for obsolescence reserves
- Raw material inventory (leather, precious metals)
- Work in progress for long production cycles

### Brand Impairment
- Goodwill/brand intangibles from acquisitions
- Any impairment charges signal brand health issues

### Revenue Recognition
- Wholesale vs. retail timing
- Gift card/loyalty program deferrals
- Consignment arrangements

---

## European Filing Specifics (URD)

URDs include additional sections not in US 10-Ks:

### Non-Financial Statement (DPEF in France)
- Detailed ESG metrics
- Carbon footprint
- Workforce statistics
- Supply chain responsibility

### Governance Report
- Detailed board composition
- Executive compensation (say-on-pay)
- Shareholder structure
- Family control mechanisms (holding companies, voting rights)

### Statutory Auditor Reports
- Note any qualified opinions
- Emphasis of matter paragraphs
- Key audit matters (similar to CAMs in US)

Note material findings in Accounting Quality section.
