# Insurance Companies — Mandatory Checklist

**CRITICAL:** Every item must be addressed (found and included, OR explicitly noted as "not disclosed").

---

## Risk Factors (REQUIRED)

*Actively search for these emerging risk themes — they are often underweighted in standard analysis.*

- [ ] **Social Inflation / Litigation Risk** — search: "social inflation", "litigation", "tort", "jury verdicts", "litigation funding", "nuclear verdicts"
- [ ] **Climate Change Risk** — search: "climate", "ESG", "thermal coal", "decarbonization", "wildfire", "flood risk"
- [ ] **Cyber Risk** — search: "cyber", "ransomware", "data breach", "privacy", "cyber insurance" (both operational exposure AND underwriting exposure)

---

## Operating Metrics (REQUIRED)

- [ ] Employee count
- [ ] **Gross Premiums Written (GPW) by segment** — if not disclosed, explicitly state "GPW: Not disclosed separately (only NPW reported)" in Business Summary. Do NOT duplicate NPW values as GPW.
- [ ] **Net Premiums Written (NPW) by segment** — REQUIRED for segment table in Business Summary. Use NPW (not NPE) for segment revenue column when available.
- [ ] **Policy acquisition cost ratio by segment** — ACTIVELY capture from MD&A segment results tables
  - For each segment, capture: policy acquisition cost ratio (%)
  - Also note: administrative expense ratio (%) if disclosed separately
  - Flag YoY trend direction (improving = lower ratio, deteriorating = higher ratio)
  - Search terms: "policy acquisition cost ratio", "acquisition cost", "expense ratio" in segment tables
- [ ] **Combined ratio components** — REQUIRED in Financial Snapshot insurance tables:
  - Loss & loss expense ratio
  - Policy acquisition cost ratio
  - Administrative expense ratio
  - Total combined ratio
  - Catastrophe loss impact (points)
  - Prior period development impact (points)
  - Current accident year combined ratio ex-cat

---

## YAML Frontmatter (Required Fields)

- [ ] `metrics.combined_ratio`
- [ ] `metrics.investable_assets_m`
- [ ] `metrics.book_value_per_share`
- [ ] `ratings.am_best`, `ratings.sp`, `ratings.moodys`
- [ ] `capital.dividend_capacity_m` (what operating subs can pay to holdco)
- [ ] `capital.regulatory_ratio` (RBC or equivalent)
- [ ] `affiliates` (equity method investments — Coface, Somers, etc.)

## Investment Portfolio Section (REQUIRED)

Include in Capital Allocation commentary or separate paragraph:

- [ ] Total investable assets ($ amount)
- [ ] Portfolio duration — search: "duration", "interest rate sensitivity", "average life". If only qualitative (e.g., "short duration"), state that.
- [ ] Average credit quality (S&P/Moody's) — search: "credit quality", "investment grade", "average rating". If only qualitative, state that.
- [ ] Unrealized gains/losses on fixed income — search OCI section of income statement or balance sheet AOCI
- [ ] AOCI / accumulated unrealized gains (losses) — especially for HTM vs AFS breakdown
- [ ] Investment yield (pre-tax) — if not explicitly stated, note "Investment yield: Not disclosed"
- [ ] % below investment grade — REQUIRED, search: "below investment grade", "high yield", "non-investment grade"
- [ ] Asset allocation summary — e.g., "65% fixed income, 20% equities, 15% alternatives"

**If data is qualitative only:** State what is known (e.g., "Duration: 'relatively short' per MD&A") rather than omitting.

## Capital & Liquidity Section (REQUIRED)

- [ ] RBC ratio or equivalent regulatory capital
- [ ] Dividend capacity from operating subs to holdco
- [ ] Share repurchase authorization remaining
- [ ] Debt/leverage ratios

## Risk Register — Liability Uncertainty (REQUIRED)

- [ ] **Loss reserves by segment (absolute $ amounts)** — CRITICAL: search Note 8, "Unpaid Losses", "Loss Reserves", or segment footnotes in Notes to Financial Statements
  - Required for: each operating segment (Insurance, Reinsurance, MI, etc.)
  - Include: gross reserves, ceded reserves, net reserves
  - Note YoY change in reserves (organic growth vs. reserve strengthening)
  - If segment-level reserves not explicitly disclosed, state "Segment reserves: Not disclosed at segment level" — do NOT estimate without clear sourcing
- [ ] Reserve variability disclosure (Monte Carlo / simulation range) — note "Not disclosed" if absent
- [ ] Key sensitivities (loss development, severity assumptions) — search "sensitivity" in Critical Accounting Estimates
- [ ] Prior year reserve development by segment (both $ amount AND percentage points impact)

## Prior Year Development (CRITICAL — Separates Earnings Quality)

- [ ] Net favorable/adverse development by segment ($ and points)
- [ ] Current accident year loss ratio vs. calendar year loss ratio
- [ ] Current accident year combined ratio vs. calendar year combined ratio
- [ ] Trend in reserve releases (increasing reliance = red flag)

## Underwriting Metrics

- [ ] Combined ratio and components (loss ratio, expense ratio)
- [ ] Current accident year loss ratio ex-cat
- [ ] Catastrophe losses (points and $)
- [ ] Prior year development (favorable/adverse, $M)
- [ ] Float/invested assets economics

---

## Catastrophe Losses (REQUIRED for P&C)

*If any catastrophe activity, capture breakdown — not just total.*

- [ ] Total cat losses ($M and points)
- [ ] Cat losses by segment (Insurance, Reinsurance, etc.)
- [ ] Named events with individual loss amounts (e.g., Hurricane Ian, Ukraine, wildfire)
- [ ] Prior year cat development (favorable/adverse)
- [ ] Management commentary on cat load expectations going forward

---

## Mortgage Insurance Segment (If Applicable)

### Volume & Portfolio Metrics
- [ ] New Insurance Written (NIW) — $ amount and YoY change
- [ ] Insurance in Force (IIF) — $ amount
- [ ] Risk in Force (RIF) — $ amount
- [ ] Persistency rate — % and YoY change
- [ ] Delinquency rate — % and YoY change (WATCH ITEM)
- [ ] Risk-to-capital ratio — and YoY change (WATCH ITEM)
- [ ] **PMIERs sufficiency ratio (REQUIRED for MI companies)** — search "PMIERs", "available assets", "minimum required assets", "sufficiency" in MD&A or notes. This is the binding GSE regulatory constraint. State as percentage (e.g., "165% of required assets") or "Not disclosed"

### Credit Quality Detail (REQUIRED — Include Tables in Memo)

**FICO Distribution Table:** MUST include in memo for mortgage insurers
| FICO Band | NIW ($M) | % of NIW | IIF ($M) | % of IIF |
|-----------|----------|----------|----------|----------|
| >=740 | | | | |
| 700-739 | | | | |
| 680-699 | | | | |
| <680 | | | | |

**LTV Distribution Table:** MUST include in memo for mortgage insurers
| LTV Band | NIW ($M) | % of NIW | RIF ($M) | % of RIF |
|----------|----------|----------|----------|----------|
| 95.01%+ | | | | |
| 90.01-95% | | | | |
| 85.01-90% | | | | |
| <=85% | | | | |

*These tables are CRITICAL for credit risk assessment. Search MD&A mortgage segment results.*

- [ ] FICO score distribution by band — populate table above
- [ ] LTV distribution by band — populate table above
- [ ] Weighted average FICO score and YoY change
- [ ] Weighted average LTV and YoY change
- [ ] Default-to-claim rate (historical or estimate)
- [ ] Claim severity estimate (% of unpaid principal)
- [ ] Loss reserves by accident year or policy year (absolute $ amounts)
- [ ] Reserve development by vintage year

## Watch Items (Flag If Moving in Concerning Direction)

- [ ] Persistency declining (signals portfolio runoff accelerating)
- [ ] Delinquency rising (early warning for claims)
- [ ] Risk-to-capital ratio rising (regulatory leverage increasing)
- [ ] Reserve releases as % of earnings (over-reliance on favorable development)
- [ ] Expense ratio trend (operating leverage or dis-leverage)

## Thesis-Critical Regulatory Risks (ACTIVELY SEARCH FOR)

- [ ] **GSE reform / privatization announcements** — search "GSE", "Fannie", "Freddie", "conservatorship", "Treasury", "FHFA"
- [ ] **Basel III Endgame** — search "Basel", "capital relief", "risk-weighted assets" — could eliminate MI capital benefits
- [ ] **PMIERs changes** — search "PMIERs", "eligible mortgage insurer", "financial requirements"
- [ ] **FHA/VA policy changes** — premium cuts, eligibility expansion
