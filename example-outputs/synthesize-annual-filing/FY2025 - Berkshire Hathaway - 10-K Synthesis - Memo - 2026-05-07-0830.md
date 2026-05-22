---
type: 10k-synthesis
company: Berkshire Hathaway Inc.
ticker: BRK
fiscal_year: 2025
fiscal_year_end: 2025-12-31
filing_date: 2026-03-02
synthesis_date: 2026-05-07
form_type: 10-K
regulator: SEC
accounting_standard: GAAP
reporting_currency: USD
industry: diversified-conglomerates

# Key metrics (M = millions)
metrics:
  revenue_m: 371444
  operating_income_m: 92049         # Earnings before income taxes and equity method earnings
  net_income_m: 66968               # Attributable to Berkshire shareholders
  fcf_m: 25042                      # OCF $45,969M - CapEx $20,927M
  employees: 387800
  # Conglomerate-specific metrics
  operating_earnings_excl_investment_m: 44486   # Sum of segment after-tax operating earnings (UW + II + BNSF + BHE + MSR + Other)
  insurance_underwriting_after_tax_m: 7258
  insurance_investment_income_after_tax_m: 12513
  bnsf_after_tax_m: 5476
  bhe_after_tax_m: 3979
  manufacturing_service_retailing_after_tax_m: 13647
  other_after_tax_m: 1613
  investment_gains_after_tax_m: 30737
  ottli_kraft_oxy_after_tax_m: -8255
  segment_count: 5                  # Insurance, BNSF, BHE, MSR, Other (Pilot/financing)
  equity_method_income_m: 900       # After-tax other-earnings line, excluding OTTI
  shareholders_equity_m: 717419
  book_value_per_share: 332.65       # $717.4B / 2,157,335 thousand B-equivalents = $332.65/B
  roe_pct: 9.8                       # $66,968M / avg ($717,419M + $649,368M)/2
  net_debt_to_equity: 0.20           # Net debt $145.0B / equity $717.4B at consolidated level
  # Insurance-specific (per insurance.md checklist)
  combined_ratio_total: null         # Not disclosed at consolidated level — see segment ratios
  geico_combined_ratio: 84.7
  bh_primary_combined_ratio: 95.8
  bhrg_pc_combined_ratio: 84.5
  npw_total_m: 89376                  # GEICO 45,193 + BH Primary 18,713 + BHRG P/C 20,168 + BHRG L/H 5,302
  npe_total_m: 88902                  # Per income statement insurance premiums earned
  float_m: 176000
  investable_assets_m: 528963          # Per insurance investments table
  cash_treasury_bills_m: 369000        # Insurance + other consolidated, per MD&A
  equity_securities_m: 297778
  fixed_maturity_securities_m: 17816
  loss_reserves_total_m: 151761        # PC $120.7B + Retroactive $31.0B
  prior_year_development_total_m: 1867 # Favorable: GEICO $957M + BHRG P/C $1,100M - BH Primary $190M adverse
  catastrophe_losses_after_tax_m: 850
  underwriting_profit_pretax_m: 9460
  statutory_surplus_us_m: 333000
  # Diversified-conglomerates required metrics (per industry checklist)
  core_operating_cf_m: 45969           # Cash from operations per CF statement (Berkshire does not separately disclose "core" operating CF excluding working capital swings)
  resource_revenue_pct: null            # Not disclosed at consolidated level — BHE Energy + Pilot fuel ~7-12% of revenue but no explicit "resource" segment classification in 10-K
  dividend_payout_ratio_pct: 0          # Berkshire pays no dividend
  total_shareholder_return_pct: 0       # No buybacks ($0) + no dividends ($0) in 2025; TSR via retained earnings only
  # Insurance-specific (additional, per insurance.md checklist)
  pct_below_investment_grade: null      # Not disclosed in 10-K — fixed maturity book is dominated by short-dated U.S. Treasuries (high IG); foreign govt 95% AA+ per p.K-39
  aoci_unrealized_gains_losses_m: null  # Not separately disclosed at consolidated level — equity securities mark-to-market flows through net income (FASB ASU 2016-01), not OCI

ratings:
  am_best: "A++ (Superior)"
  sp: "AA+"
  moodys: "Not disclosed in 10-K"
  fitch: null
  outlook: stable

# Segments (top 5 by net earnings)
segments:
  - name: Insurance (Underwriting + Investment Income)
    revenue_m: 88902             # Insurance premiums earned
    pct_total: 23.9
  - name: BNSF (Railroad)
    revenue_m: 23330
    pct_total: 6.3
  - name: Berkshire Hathaway Energy
    revenue_m: 26393             # Energy + real estate ops
    pct_total: 7.1
  - name: Manufacturing, Service & Retailing
    revenue_m: 214330
    pct_total: 57.7
  - name: Other (incl. Pilot, finance)
    revenue_m: 18489
    pct_total: 5.0

# Equity portfolio: 10-K body does NOT identify individual top holdings by issuer name.
# Aggregate carrying value: $297.8B fair value (insurance + other equity securities).
# Aggregate dividend income: $5,086M pre-tax across the entire equity portfolio.
# Equity-method investments named in 10-K: Kraft Heinz and Occidental Petroleum ($20.0B combined carrying value).
# Wholly-owned (consolidated): Pilot Travel Centers (since Jan 2023).
# Top fair-value holdings (Apple, BAC, AmEx, Coca-Cola, Chevron) are NOT disclosed in 10-K body — historically per 13F filings.
affiliates:
  - name: Occidental Petroleum (OXY) — equity method
    ownership_pct: null            # Not disclosed in 10-K body (historically ~28% per public filings)
    income_contribution_m: -4500   # After-tax OTTI in 2025; ongoing equity method earnings also declined per MD&A
  - name: Kraft Heinz (KHC) — equity method
    ownership_pct: null            # Not disclosed in 10-K body (historically ~27.5% per public filings)
    income_contribution_m: -3760   # After-tax OTTI in 2025
  - name: Pilot Travel Centers — wholly owned (consolidated since Jan 2023)
    ownership_pct: 100
    income_contribution_m: 190     # Pilot pre-tax 2025 (declined 69% from $614M in 2024)

# Capital allocation & flexibility
capital:
  buyback_auth_remaining_m: null      # No fixed authorization — unlimited but constrained by $30B cash floor and "below intrinsic value" test
  buyback_deployed_fy_m: 0            # NO repurchases in 2025 — material signal
  dividends_paid_m: 0                 # Berkshire pays no dividends
  total_debt_m: 22700                 # Berkshire parent recourse only (excludes BHE/BNSF/BHFC non-recourse)
  total_consolidated_debt_m: 129081   # All borrowings: $45,763M Insurance & Other + $83,318M Railroad/Utilities/Energy
  capital_priorities:
    - "Acquire whole businesses (OxyChem $9.5B closed Jan 2, 2026)"
    - "Marketable equity securities at attractive prices"
    - "Repurchase BRK below intrinsic value (none in 2025)"
    - "Maintain $30B+ minimum cash floor — non-negotiable"
  # Insurance-specific capital fields (per insurance.md checklist)
  dividend_capacity_m: null            # Specific 2026 dividend capacity from insurance subs to holdco not disclosed in 10-K. Statutory surplus of $333B (p.K-2) dwarfs minimum capital requirements; subsidiary-to-holdco upstreaming is not a practical constraint per MD&A.
  regulatory_ratio: null               # Berkshire reports U.S. statutory surplus ($333B) rather than a single RBC ratio. Individual insurance subsidiaries hold A++ (A.M. Best) and AA+ (S&P) financial-strength ratings; consolidated RBC equivalent: Not disclosed in 10-K.

# Share count & dilution
shares:
  basic_m: 1.4382                    # Class A equivalent shares — millions
  diluted_m: 1.4382                  # No options/RSUs at parent — same as basic
  options_rsus_m: 0
  dilution_pct: 0.0

# Quality flags
quality:
  disclosure: good
  accounting: clean

# Risk tags
risk_tags:
  - succession-risk
  - equity-portfolio-concentration
  - catastrophe-loss
  - social-inflation
  - climate-wildfire
  - regulatory-utility
  - capital-allocation-discipline
  - cyber-risk
  - tariffs-trade
  - cash-deployment-drag
---

# Berkshire Hathaway — FY2025 10-K Synthesis

---

## Key Takeaways

- **Buffett-to-Abel succession is now a fact, not a future event:** The Board appointed Greg Abel CEO effective January 1, 2026, with major capital allocation decisions explicitly his responsibility (p.K-24). The 2025 filing is the last under Buffett's signature; how Abel deploys the $369B cash pile becomes the central thesis question. `[SUCCESSION]`

- **Operating earnings held the line at ~$44.5B even as headline profits collapsed 25%:** The $22B drop in net income (from $89.0B to $67.0B) is almost entirely mark-to-market noise — investment gains fell $10.8B and Berkshire took $8.3B in non-cash impairments on Kraft Heinz ($3.76B) and Occidental ($4.5B). Underlying segment earnings (excluding investment G/L and OTTI) actually *rose* roughly 1% on the back of strong BNSF and manufacturing performance. `[EARNINGS-QUALITY]`

- **Capital allocation indiscipline was the dog that didn't bark — zero buybacks for the full year:** Despite holding $369 billion in cash and Treasury Bills, Berkshire repurchased no shares in 2025 (vs. $2.9B in 2024 and $9.2B in 2023). This is Buffett signaling intrinsic value < market price. With BRK trading near record highs and $369B earning ~4% in T-Bills, the cash drag is real — but the OxyChem deal ($9.5B closed Jan 2, 2026) shows Abel is willing to write large checks. `[CAPITAL-ALLOCATION]`

- **Insurance underwriting profit fell 17% on softer GEICO and BHRG results:** Pre-tax underwriting earnings dropped from $11.4B to $9.5B. GEICO's expense ratio jumped 270bps to 12.4% on increased advertising/acquisition spend, BHRG P/C ceded $1.7B of property volume on competitive pricing, and BH Primary turned slightly adverse on prior-year reserves ($190M unfavorable vs. $52M favorable). Float still grew to $176B (from $171B). `[INSURANCE-UW]`

- **BNSF was the bright spot — earnings up 8.8% on operating leverage:** BNSF posted $5.5B net earnings on flat revenue ($23.4B) by driving the operating ratio down 250bps to 65.5%. Drivers were lapping the 2024 SMART-TD labor charge ($290M), lower fuel cost, and productivity gains. Volumes were modestly up (+0.3%) — earnings growth is operating leverage, not demand. `[BNSF-OPERATIONS]`

- **The $8.3B Kraft Heinz/Occidental impairment is a quiet admission of capital allocation mistakes:** Berkshire wrote down its equity-method investments in both companies due to "other-than-temporary" declines. Combined equity method earnings dropped $619M ex-impairments. KHC has been a 10+ year underperformer and OXY's commodity exposure has compressed since the 2022 inflation thesis. These are not paper marks — they reflect lasting earnings power deterioration. `[INVESTMENT-MISTAKES]`

- **BHE quietly simplified its capital structure — Berkshire now owns 100%:** All remaining noncontrolling interests in BHE common stock were acquired in 2024 and the preferred stock (held by other Berkshire subs) was redeemed in 2025. BHE is now wholly owned, eliminating minority interest noise. Earnings benefited from lower wildfire accruals at PacifiCorp ($100M vs. $346M). `[BHE-SIMPLIFICATION]`

- **Pilot pre-tax earnings collapsed 69% — masked inside Service & Retailing:** Pilot Travel Centers pre-tax earnings fell from $614M (2024) to $190M (2025) on revenues down 10.0% to $42.2B (p.K-46/K-47). Pre-tax margin compressed to 0.5% from 1.3%. Acquired in early 2023 at a high purchase price, Pilot is now Berkshire's worst-performing significant operating business and is dragging down the otherwise stable Service & Retailing segment. Watch fuel margins and operating expense leverage in 2026. `[PILOT-EARNINGS-DRAG]`

---

## Business Summary

Berkshire Hathaway is a diversified holding company managed on an unusually decentralized basis, with Greg Abel (effective January 1, 2026) ultimately responsible for capital allocation across five primary economic engines: (1) a global insurance group (~42,600 employees) anchored by GEICO, BH Primary, and BHRG, generating $176B of float for investment; (2) BNSF Railway, one of two North American Class I western rail franchises, operating 32,500+ route miles in 28 U.S. states and three Canadian provinces (p.K-41); (3) Berkshire Hathaway Energy, a wholly-owned regulated utility/pipeline conglomerate serving ~5.4M retail electricity customers across PacifiCorp, MidAmerican Energy, NV Energy, plus ~20,900 miles of natural gas pipelines (~21.6 Bcf/d capacity), Northern Powergrid (~4.0M UK end-users), AltaLink (Alberta transmission), and ~6,400 net MW of independent power projects — total ~24,000 employees (p.K-7); (4) a portfolio of ~120+ manufacturing, service and retailing operations (manufacturing alone employs ~175,600) including Precision Castparts, Lubrizol, Marmon (~630 facilities), IMC, Clayton Homes, NetJets, McLane, Pilot, See's, and Forest River (~36% of U.S. RV market share); and (5) a $315.6 billion publicly-traded marketable securities portfolio plus $20.0B in equity-method holdings (chiefly Kraft Heinz and Occidental). Berkshire and subsidiaries employed approximately 387,800 worldwide at year-end 2025, ~80% in the U.S. and ~19% unionized (p.K-1).

The economic engine that distinguishes Berkshire from any peer is the float-plus-permanent-capital flywheel: insurance generates ~$176 billion of zero-cost (negative-cost, in fact, given consistent underwriting profits) policyholder funds, which are deployed alongside $717.4 billion of shareholder equity into operating businesses, equities, and Treasury Bills. Berkshire's combined U.S. statutory surplus of approximately $333 billion (p.K-2) is among the largest in the industry and supports A++ (A.M. Best) and AA+ (S&P) financial-strength ratings. The 2025 filing emphasizes that Berkshire will not repurchase shares if doing so reduces consolidated cash, cash equivalents, and Treasury Bills below $30 billion — a non-negotiable liquidity floor (p.K-55).

**Segments (FY2025):**

| Segment | Revenue | % Total | YoY | Pre-Tax Earnings | Margin |
|---------|---------|---------|-----|-----|--------|
| Insurance (Premiums Earned) | 88902M | 23.9% | +0.7% | 9460M (UW) + 15261M (II) | UW combined: ~89% |
| BNSF | 23330M | 6.3% | -0.1% | 7175M | Op ratio 65.5% |
| BHE | 26297M | 7.1% | -0.2% | 2342M | 8.9% pre-tax |
| Manufacturing | 78487M | 21.1% | +1.6% | 12571M | 16.0% |
| Service & Retailing (incl. Pilot) | 135843M | 36.6% | -2.0% | 4905M | 3.6% |
| **Total Revenues** | **371444M** | **100%** | **0.0%** | | |

*Note: Investment gains/losses ($39.1B pre-tax, $30.7B after-tax) and OTTI on equity-method investments ($-10.7B pre-tax) are excluded from segment revenue but flow through net earnings.*

**Geographic mix:** ~80% of Berkshire's 387,800 employees are in the U.S. (p.K-1). Specific geographic revenue split not disclosed at consolidated level. International operations span 23 countries for BHRG reinsurance, plus material UK (Northern Powergrid) and Canada (AltaLink) utility exposure.

**Concentration:** Equity portfolio is described as concentrated in "relatively small number of issuers" (p.K-25, Risk Factors) — the 10-K body does *not* identify individual top holdings by name; per 13F filings (outside this memo's source), Apple, BAC, AmEx, Coca-Cola, and Chevron have historically constituted the bulk of the marketable securities book. No single operating-business customer >10% disclosed at consolidated level. GEICO market share is ~11.6% (third-largest U.S. private auto insurer per A.M. Best 2024 data, p.K-3); the top-five private auto insurers held 63.6% combined market share.

**Strategic investments / equity-method holdings:** Kraft Heinz (~27.5% historical stake) and Occidental Petroleum (~28% historical stake) — both took other-than-temporary impairment charges in 2025 ($3.76B and $4.50B after-tax respectively, p.K-34, K-54). Equity method carrying value collapsed from $31.1B (2024) to $20.0B (2025).

---

## What Changed This Year

- **CEO succession finalized:** Board appointed Greg Abel as CEO effective January 1, 2026; Buffett remains Chairman. Ajit Jain (Vice Chair, Insurance) and Adam Johnson (President, Consumer Products/Service/Retailing) report to Abel (p.K-24).
- **OxyChem acquisition:** $9.5 billion deal signed October 1, 2025; closed January 2, 2026. Adds 21 U.S. manufacturing plants, ~4,000 employees, leading basic-chemicals position. Occidental retained legacy environmental liabilities (p.K-15, K-55).
- **Equity-method impairments:** $8.3B after-tax other-than-temporary impairment on Kraft Heinz ($3.76B) and Occidental ($4.5B) common stock holdings — first material equity-method writedowns in years (p.K-34, K-54).
- **No share buybacks:** Zero repurchases in 2025 vs. $2.9B in 2024 and $9.2B in 2023. Buybacks remain restricted to "below intrinsic value as conservatively determined" (p.K-55).
- **BHE structure simplified:** Berkshire acquired all remaining BHE noncontrolling interests in 2024 and redeemed all preferred stock in 2025 — BHE is now wholly owned by Berkshire.
- **OBBBA tax legislation enacted (July 4, 2025):** Accelerates phase-out of clean-energy production and investment tax credits for facilities starting construction after Dec 31, 2025. BHE expects no near-term material impact but future renewable economics may shift (p.K-43).
- **U.S. Paris Agreement withdrawal (Jan 2026) and EPA Endangerment Finding rescission (Feb 11, 2026):** Reduces regulatory pressure on BNSF/BHE GHG emissions; legal challenges expected to take years (p.K-9).
- **Bell Laboratories acquired (August 2025):** Adds rodent-control products to industrial portfolio.
- **Pilot earnings collapsed 69% pre-tax:** Pilot Travel Centers pre-tax earnings fell from $614M (2024) to $190M (2025) — a $424M decline on revenue down 10.0% to $42.2B. Pilot's pre-tax margin compressed to 0.5% from 1.3% (p.K-46/K-47). The decline reflects fuel-price-driven revenue compression and is the largest single profit headwind inside Service & Retailing.
- **PCC pre-tax earnings up 34.2% on aerospace recovery:** PCC revenues $10.8B in 2025 (+4.6%); aerospace product revenues +7.5% on growing demand. Earnings boosted by manufacturing efficiencies, business mix and insurance recoveries from a Q1 fasteners-facility fire (p.K-47). PCC is the dominant driver of the Industrial Products group's +13.1% pre-tax growth.
- **Foreign currency yen note issuance:** ¥451.6B (~$3.0B) of senior notes issued in 2025 at 1.35%–3.12% rates, maturities 2028–2055 (p.K-55).
- **FX swing on senior notes:** Berkshire/BHFC non-USD senior note remeasurement produced after-tax FX losses of $642M in 2025 vs. after-tax gains of $1.15B in 2024 — a $1.8B negative swing in the "Other" earnings line (p.K-54).
- **Goodwill impairments stepped up:** After-tax goodwill impairment losses grew to $1,555M in 2025 (vs. $399M in 2024) on certain building products, consumer products and retailing businesses (p.K-54).
- **Insurance reserve mix:** Total P&C unpaid losses grew to $151.8B at YE2025 (p.K-26).

---

## Management Commentary

> "Financial strength and redundant liquidity will always be of paramount importance at Berkshire. There were no share repurchases in 2025… We will not repurchase our stock if it reduces our consolidated cash, cash equivalents and U.S. Treasury Bills holdings to below $30 billion." (p.K-55)

> "We are currently unable to reliably predict the ultimate impact on our businesses, whether through changes in the availability of products, supply chain costs and efficiency, and customer demand for our products and services. It is reasonably possible there could be adverse consequences on our operating businesses, as well as on our investments in equity securities, which could significantly affect our future results." (p.K-34, on tariffs and trade)

**Key points from management:**
- Tariffs and trade policy uncertainty flagged prominently as macro risk to operating businesses *and* equity portfolio
- Underwriting earnings "exceptional compared to results over longer periods" but "may decline in the future from the ongoing impacts of competition within the industry and rising claim cost trends" (p.K-34) — explicit guide-down language
- Equity portfolio is "unusually concentrated in relatively few companies" — risk factor, not a defect; concentration is intentional
- Liquidity floor is non-negotiable: $30B minimum, currently sitting at $369B (12x the floor)
- Investment gains/losses described as "generally meaningless in understanding our reported periodic results" (p.K-53) — Buffett's standard framing carried into final letter
- Tone: defensive on capital deployment ("safety over yield"), confident on operating businesses, candid on impairments

---

## Guidance & Promises

**Guidance:**

| Metric | FY2026 Target | Specificity |
|--------|-----|-------------|
| BNSF + BHE CapEx | ~$15B | High |
| Berkshire interest expense | $4.9B (2026) declining to $4.3B (2030) | High |
| Other contractual obligations (next 5yr) | ~$25B, $10B in 2026 | Med |
| 2026 P&C claim payments (prior occurrences) | >$30B | Med |
| Insurance underwriting | "Earnings may decline" — no number | Low |
| Buybacks | None unless "below intrinsic value" | Low |

**Promises to Track:**

| Promise | Quote | Source | Verify By |
|---------|-------|--------|-----------|
| $30B cash floor | "We will not repurchase our stock if it reduces our consolidated cash, cash equivalents and U.S. Treasury Bills holdings to below $30 billion." | p.K-55 | Each Q |
| BNSF GHG reduction | "BNSF management has committed to a broad sustainability model… that is anticipated to result in a 30% reduction in BNSF Railway's GHG emissions by 2030 from its baseline year of 2018." | p.K-6 | FY2030 |
| BHE renewables investment continuity | "BHE plans to continue investing in renewable and other low-carbon generation and storage in the future and to cease coal operations at additional coal generation units in a reliable and cost-effective manner." | p.K-9 | Annual |
| OxyChem integration | "Berkshire acquired Occidental's chemicals business ('OxyChem') for approximately $9.5 billion." | p.K-55 | FY2026 first full-year results |
| Catastrophe loss tolerance ceiling | "avoid writing groups of policies from which pre-tax losses from a single catastrophe event might aggregate in excess of $15 billion." | p.K-26 | Each cat event |

**Claims to Verify:**

| Claim | Quote | Source | How to Verify |
|-------|-------|--------|---------------|
| Statutory surplus #1-tier | "Berkshire's insurance companies maintain capital strength at exceptionally high levels, which differentiates them from their competitors. The combined statutory surplus of Berkshire's U.S.-based insurers was approximately $333 billion at December 31, 2025." | p.K-2 | NAIC statutory filings, peer comparison |
| GEICO market position | "GEICO's market share being the third largest at approximately 11.6%." | p.K-3 | A.M. Best 2025 data when published |
| BHE renewable investment cumulative | "BHE has invested heavily in owned renewable generation and storage, with cumulative investments of $38.0 billion through December 31, 2025." | p.K-9 | BHE annual / FERC filings |
| Cost of float negative each year | "Our combined insurance operations generated pre-tax underwriting gains in each of the three years ending December 31, 2025 and the average cost of float was negative in each year." | p.K-39 | Calculate cost of float YoY |

---

## Financial Snapshot

**P&L & Returns:**

| Metric | FY2025 | FY2024 | Change |
|--------|--------|--------|--------|
| Total Revenue | 371444M | 371433M | +0.0% |
| Insurance Premiums Earned | 88902M | 88257M | +0.7% |
| Investment Gains (Losses) (pre-tax) | 39078M | 52799M | -26.0% |
| Pre-tax Earnings (ex-equity method) | 92049M | 108535M | -15.2% |
| Equity Method Earnings (Losses) | -9590M | 1841M | n/m |
| Net Earnings to BRK Shareholders | 66968M | 88995M | -24.7% |
| Operating Earnings (ex-Investment G/L, ex-OTTI) | 44486M | 44023M | +1.1% |
| EPS (Class A) | $46,563 | $61,900 | -24.8% |
| EPS (Class B equivalent) | $31.04 | $41.27 | -24.8% |
| Effective Tax Rate | 18.4% | 18.9% | -50bps |
| Cash from Operations | 45969M | 30592M | +50.3% |
| CapEx (PP&E + leased equipment) | 20927M | 18976M | +10.3% |
| FCF | 25042M | 11616M | +115.6% |
| FCF Conversion | 37.4% | 13.1% | FCF / Net Income |
| ROE (ending equity basis) | 9.8% | 14.7% | -490bps |

*ROIC — Not calculated as a single number. For a holding company of Berkshire's structure (insurance float + regulated utilities + railroad + manufacturing + $315B securities portfolio), traditional ROIC is non-comparable: NOPAT understates economic earnings (excludes unrealized gains and dividend income on equity portfolio held inside insurance subs), and invested capital is dominated by a $717B equity base much of which is mark-to-market securities. Buffett's preferred metric is per-share book value growth + dividend yield of underlying holdings. Per-share book value: $717,419M ÷ 1,438,223 Class A equivalents = $498,824/A share (vs. $451,652 prior year, +10.5%).*

*Operating Earnings calculation: Insurance UW $7,258M + Insurance II $12,513M + BNSF $5,476M + BHE $3,979M + MSR $13,647M + Other $1,613M = $44,486M after-tax. Excludes investment gains $30,737M and OTTI on equity method investments -$8,255M.*

**Balance Sheet:**

| Metric | FY2025 | FY2024 | Notes |
|--------|--------|--------|-------|
| Cash & Equivalents (incl. Treasury Bills) | 369000M | ~334000M | Insurance + Other; per MD&A p.K-55 |
| Investments in Equity Securities | 297778M | 271588M | Mark-to-market |
| Equity Method Investments | 19978M | 31134M | Post-impairment KHC + OXY |
| Fixed Maturity Securities | 17816M | 15364M | Mostly foreign govt + UST |
| Total Assets | 1222176M | 1153881M | +5.9% |
| Total Debt — Berkshire parent + BHFC | 41023M | 39521M | Recourse to Berkshire |
| Total Debt — BNSF | 24100M | 23535M | Non-recourse |
| Total Debt — BHE | 59300M | 56400M | Non-recourse |
| Total Consolidated Debt | 129081M | 124762M | All borrowings |
| Net Debt — Corporate (recourse) | -327977M | n/a | Recourse debt $41.0B - Cash/T-bills $369.0B; deeply negative |
| Net Debt / EBITDA — Corporate | n/m | n/m | Net Debt -$327,977M / EBITDA ~$112,000M (Op Inc $92,049M + D&A ~$20,000M) — non-meaningful (cash > debt). Excludes $83.4B non-recourse BNSF/BHE debt |
| Interest Coverage | 18.2x | 20.9x | EBIT $92,049M / Int Exp $5,069M |
| P&C Loss Reserves | 120713M | 115151M | +4.8% |
| Retroactive Reinsurance Reserves | 31048M | 32443M | Run-off |
| Float | 176000M | 171000M | +2.9% |
| Shareholders' Equity (BRK) | 717419M | 649368M | +10.5% |
| Treasury Stock | -78939M | -78939M | Unchanged — no buybacks |

**Debt structure:** Total consolidated debt of $129.1B splits into three buckets: (1) Berkshire parent + BHFC $41.0B (Berkshire's senior notes $22.7B at 1.35%–3.12% with maturities 2028–2055; BHFC $18.3B financing Clayton/Marmon railcars, fully guaranteed by Berkshire); (2) BNSF $24.1B (issued $1.85B 2056 debentures at 5.65% in 2025); (3) BHE $59.3B (issued $4.3B term debt at 6.2% in 2025; subsidiary debt non-recourse to Berkshire). Interest expense expected to range from $4.9B (2026) to $4.3B (2030). Berkshire does *not* guarantee BNSF or BHE debt (p.K-55). Maturity ladder is well distributed; no near-term refinancing wall.

**Insurance Combined Ratio Components:**

| Segment | 2025 Loss Ratio | 2025 Expense Ratio | 2025 Combined | 2024 Combined | Change |
|---------|----------------|--------------------|--------------:|---------------|--------|
| GEICO | 72.3% | 12.4% | 84.7% | 81.5% | +3.2pts |
| BH Primary | 66.9% | 28.9% | 95.8% | 95.4% | +0.4pts |
| BHRG Property/Casualty | 57.2% | 27.3% | 84.5% | 82.9% | +1.6pts |
| BHRG Life/Health | 74.5% (benefit) | 18.4% | 92.9% | 95.5% | -2.6pts |

**Prior Year Reserve Development (Favorable / [Adverse]):**

| Segment | 2025 ($M) | 2024 ($M) |
|---------|-----------|-----------|
| GEICO | +957 | +550 |
| BH Primary | (190) | +52 |
| BHRG Property/Casualty | +1,100 | +1,700 |
| BHRG Retroactive Reinsurance | (261) | (196) |
| **Aggregate (favorable)** | **+1,606** | **+2,106** |

*BH Primary turned modestly adverse on liability claims ("social inflation trends") for the first time in several years (p.K-37). Aggregate prior-year favorable development declined ~$500M, signaling tighter underwriting margin going forward.*

**Catastrophe Losses (after-tax):** ~$850M in 2025 vs. ~$1.2B in 2024 and ~$725M in 2023. 2025 events included Southern California wildfires (BHRG/BH Primary). 2024 included Hurricanes Helene and Milton ($360M GEICO impact alone).

**Investment Portfolio (Insurance subs):**

| Component | YE2025 | YE2024 |
|-----------|--------|--------|
| Cash + U.S. Treasury Bills | 212651M | 212591M |
| Equity Securities | 294144M | 263366M |
| Fixed Maturity Securities | 17466M | 15137M |
| Other (incl. loans to affiliates) | 4702M | 5980M |
| **Total** | **528963M** | **497074M** |

*Investment yield (pre-tax):* Pre-tax investment income $15.3B / average invested assets $513B ≈ 3.0%. Yield is intentionally suppressed — Berkshire holds ~40% of insurance investments in T-Bills earning short-term rates and ~55% in equities (yielding dividend income only).

*Duration / credit:* "Insist on safety over yield with respect to short-term investments" (p.K-39). U.S. T-bill book is by definition <1yr duration. Foreign government holdings: 95% rated AA or higher (p.K-39). No fixed-income duration target disclosed — Berkshire explicitly does not match asset-liability duration. **% below investment grade:** Not disclosed in 10-K — fixed maturity book is dominated by short-dated U.S. Treasuries (highest IG) plus foreign government holdings (95% AA or higher), so non-IG exposure is presumed minimal but not quantified. **AOCI / unrealized gains-losses on fixed maturity:** Not separately broken out in 10-K body — under FASB ASU 2016-01, BRK runs equity securities through net income (not OCI), so OCI/AOCI movements are dominated by FX translation and small fixed-maturity AFS marks rather than equity portfolio swings.

---

## Capital Allocation

**Sources of cash (FY2025):**
- Operating Cash Flow: $45,969M
- Sales of Equity Securities: $30,686M
- Net Treasury Bill rollover (redemptions $503,954M − purchases $586,129M): substantial gross rolls; net deployment ~$82B into T-bills

**Uses of cash:**

| Use | FY2025 | FY2024 | Notes |
|-----|--------|--------|-------|
| CapEx (PP&E + lease equipment) | 20927M | 18976M | $14.4B at BNSF + BHE |
| Acquisitions of Businesses | 1074M | 396M | Bell Laboratories + tuck-ins (excludes OxyChem closing Jan 2026) |
| Equity Securities Purchases | 16923M | 9237M | Net buyer of equities for first time since 2022 |
| Equity Securities Sales | -30686M | -143359M | Massive sales in 2024 (Apple); much lower in 2025 |
| Dividends Paid | 0 | 0 | Berkshire pays no dividend |
| Buybacks | 0 | 2918M | Zero in 2025 — material signal |
| Debt Issued | 9172M | 13186M | BNSF $1.85B, BHE $4.3B, Berkshire ¥451.6B |
| Debt Repaid | 7024M | 11947M | |

**Realized vs. unrealized split on investment gains:** Pre-tax investment gains of $39.1B in 2025 included $40.0B of *unrealized* gains on equity securities held at year-end and net realized losses of $18M on equities sold during the year (p.K-53). For comparison, 2024 unrealized gains were $49.3B and realized gains were $3.5B; 2023 unrealized $69.1B and realized $2.7B. Taxable investment gains (sale proceeds vs. original cost basis) were $23.7B in 2025 vs. $101.1B in 2024 — the 2024 spike reflected the massive Apple sales which are not repeated in 2025.

**Capital allocation commentary:**
The defining feature of Berkshire's 2025 is what *did not* happen: zero share repurchases, no dividends, and a swelling cash + Treasury Bill balance of $369 billion. Buffett is signaling — through inaction — that the stock trades above his conservative estimate of intrinsic value and that public-equity opportunities remain unattractive. The $30B liquidity floor is treated as inviolate and is now ~12x covered. Net deployment of capital into operating subs ($14.4B BNSF/BHE CapEx) and the OxyChem deal ($9.5B closed Jan 2, 2026) are the only meaningful capital exits. The 2025 pace of equity portfolio activity also marks a shift: $16.9B purchases vs. $30.7B sales (net seller, but vastly less than 2024's $143.4B in sales). With Buffett handing the controls to Abel on January 1, 2026, the question for 2026+ becomes whether Abel maintains the same discipline or moves cash off the sidelines via buybacks or larger acquisitions. Dividend capacity from insurance subs is regulated by NAIC/state authorities; Berkshire's $333B U.S. statutory surplus dwarfs minimum capital requirements, so subsidiary-to-holdco upstreaming is not a practical constraint. `[CAPITAL-ALLOCATION]` `[CASH-DEPLOYMENT-DRAG]`

---

## Risk Factors

*Unable to assess [NEW] vs. prior year — single-year analysis. Risks below are flagged as elevated where MD&A or filing language signals heightened concern in 2025.*

- **Key-person succession (elevated):** Greg Abel formally assumes CEO role January 1, 2026 with explicit responsibility for "major capital allocation and investment decisions" (p.K-24). Buffett's 60+ year track record is unrepeatable; Abel has run BHE since 2008 and Berkshire's non-insurance ops since 2018, but the market has not yet priced an Abel-led capital allocation regime. *Probability: High (event has happened). Impact: High.* The question is not whether succession occurs but whether discipline persists — first-year actions (buyback cadence, deal flow, equity sales) will be intensely watched. `[SUCCESSION-RISK]`

- **Equity portfolio concentration:** "We concentrate a high percentage of the equity security investments of our insurance subsidiaries in relatively small number of issuers. A significant decline in the fair values of our larger investments in equity securities may produce a material decline in our consolidated shareholders' equity and our consolidated earnings." (p.K-25). The 10-K also notes that "since a large percentage of our equity securities are held by our insurance subsidiaries, significant decreases in the fair values of these investments will produce significant declines in the statutory surplus of our insurance subsidiaries. Our large statutory surplus is a competitive advantage, and a long-term material decline could have an adverse effect on our claims-paying ability ratings and our ability to write new insurance business" (p.K-25). *Probability: Med. Impact: High.* This is structural, not boilerplate — the 10-K body does not break out individual top holdings, but per 13F filings the top-5 names historically constitute the majority of the $297.8B equity book. A 30% drawdown in top holdings could erase tens of billions of equity, pressuring statutory surplus, claims-paying ratings (currently AA+/A++), and underwriting capacity. `[EQUITY-PORTFOLIO-CONCENTRATION]`

- **Catastrophe loss tolerance and social inflation:** Berkshire explicitly underwrites to a $15B aggregate single-event ceiling ("avoid writing groups of policies from which pre-tax losses from a single catastrophe event might aggregate in excess of $15 billion," p.K-26). 2025 had $850M after-tax cat losses (Southern California wildfires). Separately, BH Primary's loss costs were "negatively impacted by unfavorable social inflation trends, including the impacts of jury awards and litigation costs" (p.K-37), and BH Primary turned $190M *adverse* on prior-year reserves vs. $52M favorable in 2024 — first directional shift in years. *Probability: High for both. Impact: Med-to-High (cat single-event), Med (social inflation chronic).* The reserve direction at BH Primary is a watch item — if 2026 confirms the trend, current accident year combined ratios may need to rise. `[CATASTROPHE-LOSS]` `[SOCIAL-INFLATION]`

- **BHE wildfire and utility regulatory risk:** PacifiCorp recorded $100M of pre-tax wildfire loss accruals in 2025 (down from $346M in 2024 and $1.7B in 2023). The 10-K explicitly notes that "regulated energy subsidiaries are exposed to losses arising from wildfires and related litigation and judicial outcomes" and "to the extent costs are not recoverable through approved rates, the operating results and financial condition of these businesses can be negatively impacted, perhaps materially" (p.K-27). *Probability: Med (annual recurrence). Impact: Med-to-High.* Utility commission disallowance of cost recovery is the structural risk — California, Oregon and Washington remain inversely exposed. `[CLIMATE-WILDFIRE]` `[REGULATORY-UTILITY]`

- **Tariffs, trade policy and macro uncertainty:** "Tensions from developing international trade policies and tariffs" flagged in MD&A as material to operating businesses and equity portfolio (p.K-34). Building products group earnings noted "negative impacts of international trade tensions" (p.K-49). PCC noted potential 2026 raw material cost pressure (p.K-47). *Probability: High (in flux). Impact: Med.* Berkshire's broad business mix provides natural diversification but PCC, Lubrizol, IMC, and Marmon all source globally; consumer-facing retailers (BHA, NFM) face demand sensitivity. `[TARIFFS-TRADE]`

- **Cybersecurity:** "Certain of our information systems have been subject to cyber threats… A significant disruption or cyber intrusion at one or more of our significant operations could adversely affect our results of operations, financial condition and/or liquidity" (p.K-24). *Probability: Med. Impact: Med-to-High.* Decentralized model creates >120 attack surfaces; no central CISO. Berkshire's underwriting of cyber risk in BHRG is also a separate insurance exposure not quantified in the 10-K. `[CYBER-RISK]`

---

## Accounting Quality

| Check | Status | Notes |
|-------|--------|-------|
| Recurring "one-time" charges | ⚠ | After-tax goodwill impairments $1,555M in 2025 (vs. $399M in 2024 and $0 in 2023) on certain building products, consumer products, retailing businesses (p.K-54); after-tax FX losses of $642M on non-USD senior notes vs. $1.15B gain in 2024; $8.3B equity-method OTTI on KHC + OXY |
| Revenue recognition changes | ✓ | None disclosed |
| Receivables vs. revenue growth | ✓ | Other receivables flat ($44.3B vs. $43.9B); no concerning divergence |
| Adjusted metric definition drift | ✓ | Buffett's emphasis on "operating earnings ex investment G/L" is consistent with prior years |
| Goodwill impairment assumptions | ⚠ | Goodwill declined to $83.1B from $83.9B; $1.6B impairment shows assumptions are being tested |
| Related party transactions | ✓ | Pilot borrows $3.7B from Berkshire insurance subs; Clayton borrows $29.5B from BHFC (consolidated) — disclosed |
| Auditor issues | ✓ | Deloitte & Touche LLP — no qualifications noted in extracted content |

**Summary:** Accounting is high-quality and conservative — Berkshire's willingness to take $8.3B of equity-method OTTI on KHC and OXY rather than deferring is a positive earnings-quality signal, and consistent goodwill testing produced $1.6B of writedowns at underperforming subs (building products, consumer products, retailing). The decentralized model creates audit complexity across 120+ businesses but no internal control issues are flagged. Buffett's insistence on reporting both GAAP and operating earnings — and explicitly characterizing investment gains/losses as "meaningless in any given period" — is industry best practice.

---

## Questions for Further Research

1. **What is Greg Abel's first-year capital allocation playbook — specifically buyback cadence and acquisition appetite?**
   *Why it matters:* The $369B cash pile generates ~$15B of pre-tax T-bill income but caps growth. If Abel is willing to repurchase shares at slightly higher P/B multiples than Buffett or pursue large public-to-private deals, the cash drag thesis improves materially. If discipline holds, BRK becomes a slow-compounding insurance-utility hybrid earning ~10% ROE.

2. **Is the BH Primary $190M adverse prior-year development a one-off or a trend reversal?**
   *Why it matters:* For two decades, Berkshire's commercial insurance segment has reliably released reserves. A turn to adverse development on social-inflation trends would suggest the entire industry's reserve estimates are under-stated, which could pressure 2026–2027 underwriting margins across the book. Track quarterly disclosures.

3. **What is the run-rate ongoing earnings power of the Kraft Heinz and Occidental equity-method stakes post-impairment?**
   *Why it matters:* The $11B equity method earnings line was restated lower by $619M ex-impairment. With KHC and OXY now carried at $20.0B (vs. $31.1B), the question is whether further impairments are likely or if these are now conservative. Each $1B of additional impairment is roughly $0.34/B-share book value.

4. **How does the OxyChem acquisition perform in its first year as a Berkshire sub?**
   *Why it matters:* $9.5B is the largest deal since Pilot/Alleghany. As Abel's first major capital allocation move (announced October 2025), execution sets the tone for his tenure. Margins, end-market mix, and integration friction are all unknown from public disclosure.

5. **What is the look-through earnings of the marketable equity portfolio, and how is it tracking vs. dividend income reported?**
   *Why it matters:* Berkshire's $5.1B of dividend income captures only ~25-30% of look-through earnings on its $315B portfolio. The economic earnings power of the portfolio is materially higher than reported and is a key driver of intrinsic value vs. reported book value.

6. **Will GEICO's 270bps expense ratio expansion (to 12.4%) reverse, and what is the lifetime value of new policies acquired through the marketing push?**
   *Why it matters:* Underwriting profit fell $989M at GEICO despite a 5.3% premium increase — attributed to advertising spend. If new policy LTV is healthy, this is a growth investment. If retention is poor, it's an expensive loss leader against Progressive.

7. **Is Pilot's 69% pre-tax earnings decline structural or cyclical, and does an impairment loom?**
   *Why it matters:* Pilot pre-tax fell from $614M to $190M on a 10% revenue decline — pre-tax margin compressed to 0.5%. With Berkshire having paid a high price for the acquisition completed in early 2023, sustained earnings deterioration could trigger goodwill impairment testing. Watch 2026 fuel margins, EV transition headwinds, and any management changes.

---

## Topic Index

| Tag | Sections |
|-----|----------|
| `[SUCCESSION]` / `[SUCCESSION-RISK]` | Key Takeaways, What Changed, Risk Factors |
| `[EARNINGS-QUALITY]` | Key Takeaways, Financial Snapshot |
| `[CAPITAL-ALLOCATION]` | Key Takeaways, Capital Allocation |
| `[CASH-DEPLOYMENT-DRAG]` | Key Takeaways, Capital Allocation |
| `[INSURANCE-UW]` | Key Takeaways, Financial Snapshot |
| `[BNSF-OPERATIONS]` | Key Takeaways |
| `[INVESTMENT-MISTAKES]` | Key Takeaways, What Changed |
| `[BHE-SIMPLIFICATION]` | Key Takeaways, What Changed |
| `[PILOT-EARNINGS-DRAG]` | Key Takeaways, What Changed |
| `[EQUITY-PORTFOLIO-CONCENTRATION]` | Risk Factors |
| `[CATASTROPHE-LOSS]` | Risk Factors, Financial Snapshot |
| `[SOCIAL-INFLATION]` | Risk Factors |
| `[CLIMATE-WILDFIRE]` | Risk Factors |
| `[REGULATORY-UTILITY]` | Risk Factors |
| `[TARIFFS-TRADE]` | Risk Factors |
| `[CYBER-RISK]` | Risk Factors |

**Validation check:** All tags above appear inline in document body sections.

---

## Source

- **Filing:** Berkshire Hathaway Inc. 10-K for FY2025
- **Regulator:** SEC
- **Accounting Standard:** GAAP
- **Filed:** 2026-03-02
- **FYE:** 2025-12-31
- **Auditor:** Deloitte & Touche LLP
- **CIK:** 1067983
- **Retrieved via:** edgartools (parse_annual_filing.py)

**Page References:**
- Business: K-1 to K-23
- Risk Factors: K-24 to K-28
- MD&A: K-34 to K-55
- Financials: K-56 onward (consolidated statements + notes)
