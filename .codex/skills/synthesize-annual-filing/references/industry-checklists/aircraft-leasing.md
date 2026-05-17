# Aircraft Leasing Industry Checklist

Use this checklist when synthesizing 10-K/20-F filings for aircraft leasing companies (e.g., AerCap, Air Lease Corp, Avolon, BOC Aviation).

---

## Why This Industry Is Different

Aircraft leasing is a capital-intensive, asset-backed business where:
- **Operating cash flow ≠ FCF:** Asset sales/purchases are core operations, not investing activities
- **Debt-to-equity is the primary leverage metric:** Matching assets and liabilities matters more than EBITDA-based ratios
- **Book value is critical:** Trading vs. book value indicates market's view of asset quality
- **Gain-on-sale validates book values:** Consistent gains suggest conservative depreciation assumptions
- **Fleet age and composition drive value:** New-technology, fuel-efficient aircraft command premium rates

---

## Industry-Specific Metrics (REQUIRED in YAML)

```yaml
metrics:
  # Standard metrics
  revenue_m: [lease revenue]
  operating_income_m: [income before taxes + interest — or use pre-tax income]
  net_income_m: [number]
  fcf_m: [operating cash flow — note: "FCF not meaningful for leasing"]
  employees: [number or null]

  # Aircraft Leasing-Specific (REQUIRED)
  fleet_owned_count: [number]  # Owned aircraft
  fleet_managed_count: [number]  # Managed for third parties
  fleet_avg_age_years: [number]  # Weighted average age
  utilization_rate_pct: [number]  # % of fleet on lease
  adjusted_debt_to_equity: [number]  # Primary leverage metric
  book_value_per_share: [number]  # Critical for valuation
  average_cost_of_debt_pct: [number]  # Interest expense / avg debt

  # Optional but Valuable
  gain_on_sale_margin_pct: [number]  # Validates book values
  orderbook_aircraft: [number]  # Forward commitments
  lease_yield_per_aircraft_m: [number]  # Basic rents / fleet count
```

---

## Fleet Composition (Business Summary Section)

Must capture:
- [ ] Total owned aircraft (by operating lease, finance lease, held for sale)
- [ ] Managed aircraft (serviced for third parties)
- [ ] Engines owned/managed (if material)
- [ ] Helicopters (if applicable)
- [ ] Aircraft type breakdown (by NBV % or count):
  - Narrowbody vs. widebody
  - Passenger vs. freighter
  - New technology (neo, MAX) vs. previous generation
- [ ] Weighted average fleet age (if disclosed)
- [ ] Orderbook (aircraft on order, delivery schedule)

**Table format:**
| Aircraft Type | Count | % of NBV | Age (avg) |
|--------------|-------|----------|-----------|
| A320neo Family | X | X% | X yrs |
| Boeing 787 | X | X% | X yrs |
| ...

---

## Geographic Distribution (Business Summary Section)

Must capture:
- [ ] Full regional breakdown (Asia-Pacific, Europe, Americas, Middle East/Africa)
- [ ] Country-level concentration (any country >10% of assets or revenue)
- [ ] Note geopolitical exposure (China, Russia exposure, etc.)

---

## Customer Concentration (Business Summary Section)

Must capture:
- [ ] Top 5 lessees by % of lease revenue
- [ ] Any lessee >10% of total revenue
- [ ] Country concentration of lessees

---

## Financial Snapshot — Leasing-Specific

### P&L Breakdown
| Metric | FY[Year] | FY[Year-1] | Change |
|--------|----------|------------|--------|
| Basic Lease Rents | [X]M | [X]M | |
| Maintenance Rents | [X]M | [X]M | |
| Total Lease Revenue | [X]M | [X]M | |
| Net Gain on Sales | [X]M | [X]M | |
| Other Income | [X]M | [X]M | |
| Total Revenue | [X]M | [X]M | |

### Key Ratios
- [ ] Gain-on-sale margin (proceeds vs. NBV) — validates book values
- [ ] Operating margin (income from ops / total revenue)
- [ ] Interest coverage (operating income / interest expense)

### Balance Sheet
- [ ] Flight equipment (net book value)
- [ ] Pre-delivery payments (for orderbook)
- [ ] Total debt (by type: unsecured notes, secured, credit facilities)
- [ ] Adjusted debt-to-equity ratio
- [ ] Undrawn credit facilities (liquidity buffer)

### Debt Structure
- [ ] Fixed vs. floating rate breakdown
- [ ] Average cost of debt
- [ ] Maturity schedule (next 5 years)
- [ ] Any subordinated debt (often gets equity credit from rating agencies)

---

## Capital Allocation — Leasing-Specific

Aircraft lessors recycle capital constantly. Capture:
- [ ] Aircraft purchases (new technology vs. used)
- [ ] Aircraft sales (average age of sold aircraft — validates fleet renewal strategy)
- [ ] Pre-delivery payments (forward commitment)
- [ ] Share buybacks (often aggressive when trading below book value)
- [ ] Dividends
- [ ] Debt paydown

**Key question:** Is management buying back stock below book value while selling aircraft above book value? If so, this is value-accretive capital allocation.

---

## Accounting Quality — Leasing-Specific

In addition to standard checks:
- [ ] **Depreciation assumptions:** Useful life, residual values — compare to peers
- [ ] **Impairment testing:** How many aircraft tested, what % passed?
- [ ] **Gain-on-sale consistency:** Multi-year trend validates book values
- [ ] **Lease classification:** Operating vs. finance lease mix
- [ ] **Maintenance reserves:** Timing of recognition

---

## Risk Factors — Leasing-Specific

Search for and flag:
- [ ] **Geopolitical risk:** Country concentration (China, Russia precedent)
- [ ] **Manufacturer concentration:** Boeing, Airbus dependency
- [ ] **Engine issues:** GTF, LEAP, other fleet groundings
- [ ] **Interest rate exposure:** Fixed vs. floating debt mismatch
- [ ] **Lessee credit risk:** Airline bankruptcies, restructurings
- [ ] **Residual value risk:** Aircraft values if technology shifts
- [ ] **Tariff/trade policy:** Aviation exemptions, cross-border leasing
- [ ] **Insurance coverage:** Adequate for asset base?

---

## Ratings Section

Aircraft lessors are typically rated by multiple agencies. Include in YAML:
```yaml
ratings:
  sp: [rating]
  moodys: [rating]
  fitch: [rating]  # Fitch often covers lessors
  outlook: stable|positive|negative
```

---

## Strategic Investments

Many lessors have JVs for engines or regional markets. Capture:
- [ ] Engine leasing JVs (e.g., Shannon Engine Support)
- [ ] Regional JVs (e.g., China-focused entities)
- [ ] Equity method income contribution

---

## Key Questions for Further Research

Typical unanswered questions for aircraft lessors:
1. What is the competitive positioning vs. peers (Air Lease, Avolon, BOC Aviation)?
2. What are lease rate trends by aircraft type?
3. How are manufacturer delivery delays affecting the orderbook?
4. What is the plan for end-of-life aircraft (part-out, conversion, sale)?
5. How does management think about optimal leverage?

---

## Validation Checklist Items

Before writing final memo, verify:
- [ ] Fleet count reconciles (owned + managed = total in narrative)
- [ ] Geographic breakdown sums to 100%
- [ ] Debt-to-equity matches company's stated "adjusted" metric
- [ ] Gain-on-sale margin calculated (not just stated)
- [ ] Book value per share calculated (equity / shares outstanding)
- [ ] Utilization rate calculated (on-lease / total owned)
