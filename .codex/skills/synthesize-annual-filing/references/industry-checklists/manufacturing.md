# Manufacturing / Industrials — Mandatory Checklist

**CRITICAL:** Every item must be addressed (found and included, OR explicitly noted as "not disclosed").

---

## YAML Metrics (Required)

Add these to the YAML frontmatter `metrics:` section:

```yaml
metrics:
  backlog_m: [number or null]     # Total backlog in millions (null if not disclosed)
  book_to_bill: [number or null]  # Book-to-bill ratio (null if not calculable)
  capacity_utilization_pct: [number or null]  # Capacity utilization (null if not disclosed)
  # Working capital days (ALL THREE required - calculate from balance sheet/income statement):
  inventory_days: [number]        # (Avg Inventory ÷ COGS) × 365
  receivables_days: [number]      # (Avg Receivables ÷ Revenue) × 365
  payables_days: [number]         # (Avg Payables ÷ COGS) × 365
```

**Important:** If any of `backlog_m`, `book_to_bill`, or `capacity_utilization_pct` are set to `null`, there MUST be a corresponding question in "Questions for Further Research" explaining why this metric matters and what it would tell the investor.

---

## Key Metrics

### Backlog and Book-to-Bill (REQUIRED)
- [ ] Total backlog in YAML as `backlog_m`
- [ ] Book-to-bill ratio in YAML as `book_to_bill`
  - If explicitly stated in 10-K, use that value
  - If NOT stated, calculate: New Orders ÷ Revenue (or note "Not calculable — order data not disclosed")
- [ ] Backlog by segment in Business Summary (if disclosed)
- [ ] Backlog conversion timing (% within 12/24 months) in Guidance section

### Capacity Utilization
- [ ] In YAML as `capacity_utilization_pct` if disclosed
- [ ] If NOT disclosed, add to Questions: "Capacity utilization: Not disclosed — unclear how much production headroom exists"
- [ ] If qualitative commentary exists (e.g., "expanding capacity"), note in What Changed

### Input Cost Exposure (REQUIRED in Risk Factors)
- [ ] **MUST include a Risk Factors bullet** addressing input cost exposure (raw materials, energy, labor, semiconductor components, rare earths)
- [ ] Tariff exposure quantified if mentioned in 10-K
- [ ] Supplier concentration if disclosed (single-source components)
- [ ] If input costs are NOT a material risk (rare for manufacturing), state explicitly: "Input costs: Not flagged as material risk in 10-K"

### Working Capital Days (ALL THREE REQUIRED)
- [ ] **Inventory Days** = (Average Inventory ÷ COGS) × 365
  - Include in YAML as `inventory_days`
  - Compare to prior year; flag if increasing >10% YoY
- [ ] **Receivables Days (DSO)** = (Average Receivables ÷ Revenue) × 365
  - Include in YAML as `receivables_days`
  - Flag unusual divergence from revenue growth (as in LMT: receivables +66% vs revenue +6%)
- [ ] **Payables Days (DPO)** = (Average Payables ÷ COGS) × 365
  - Include in YAML as `payables_days`
- [ ] If multi-year balance sheet data not available for averaging, use end-of-period values and note "Using period-end values — multi-year data not available for averaging"
- [ ] If COGS not separately disclosed (e.g., cost of revenue only), note the denominator used

**Cash Conversion Cycle** (optional but recommended): = Inventory Days + Receivables Days - Payables Days. A decreasing CCC indicates improving working capital efficiency.

### R&D Spend (REQUIRED for technology-intensive manufacturing)

*For semiconductors, aerospace, pharma-adjacent, or other R&D-intensive manufacturers:*

- [ ] Total R&D spending in Key Takeaways or Financial Snapshot
- [ ] R&D as % of revenue (calculate: R&D ÷ Revenue)
- [ ] YoY R&D growth rate noted
- [ ] R&D intensity comparison to peers if competitive position is questioned
- [ ] If R&D not separately disclosed: "R&D: Not separately disclosed — included in operating expenses"

**Note:** For traditional industrials (machinery, equipment), R&D may be less material. Use judgment.

### CapEx Split
- [ ] Total CapEx in Capital Allocation table
- [ ] Maintenance vs. growth split if disclosed (rare — most 10-Ks don't provide)
- [ ] If NOT disclosed, add to Questions: "CapEx split: What portion is maintenance vs. growth?"
- [ ] Qualitative description of CapEx focus (facilities, equipment, IT, capacity expansion)

### Debt Maturity Schedule (REQUIRED for capital-intensive manufacturers)

- [ ] Near-term maturities quantified in Financial Snapshot debt structure line
- [ ] Format: "$XM due 2025, $YM due 2026, $ZM due 2027"
- [ ] If maturity schedule not disclosed in MD&A, extract from debt footnotes
- [ ] If not extractable: "Detailed maturity schedule: Not disclosed in 10-K"
- [ ] Flag refinancing risk if large maturities coincide with weak coverage ratios

### Cyclicality Assessment
- [ ] Industry cycle position mentioned in Business Summary or Risk Factors
- [ ] Defense/Aerospace: Budget cycle dependency explicitly noted (NDAA, continuing resolutions)
- [ ] For cyclical industrials: Revenue volatility through recent cycles
- [ ] Government contract dependency % if applicable

---

## Watch Items (Flag If Moving in Concerning Direction)

Include these assessments in Key Takeaways or Risk Factors:

- [ ] **Backlog trend:** Declining or book-to-bill <1.0 → Flag as demand concern
- [ ] **Inventory days:** Increasing >10% YoY → Flag as demand softening or supply chain buildup
- [ ] **Receivables days:** Diverging from revenue growth → Flag collection issues or payment term changes
- [ ] **Capacity utilization:** Falling → Flag pricing pressure ahead
- [ ] **Input cost vs. pricing:** Rising costs without pricing power → Flag margin compression risk

---

## Defense/Aerospace Specific

For defense contractors (Lockheed Martin, Northrop, RTX, General Dynamics, L3Harris):

### Program Concentration
- [ ] Largest program as % of revenue in Key Takeaways (e.g., "F-35 at 27% of sales")
- [ ] Largest customer concentration (U.S. Government %)
- [ ] FMS vs. DCS breakdown for international sales

### Contract Mix Risk
- [ ] Fixed-price vs. cost-plus mix if disclosed
- [ ] Reach-forward losses (losses on long-term contracts) — quantify in Key Takeaways and Risk Factors
- [ ] "Estimate at completion" changes — these are judgment-laden and material

### Regulatory/Policy Risk
- [ ] Budget authorization status (NDAA amounts)
- [ ] Executive Orders affecting contractors
- [ ] Progress payment vs. performance-based payment changes
- [ ] Dividend/buyback restrictions tied to performance

### Supply Chain
- [ ] Rare earth/critical mineral exposure (China sourcing)
- [ ] Semiconductor shortage impact
- [ ] Classified supplier dependencies (if mentioned)
