# Banks / Financial Services — Mandatory Checklist

**CRITICAL:** Every item must be addressed (found and included, OR explicitly noted as "not disclosed").

## YAML Frontmatter (Required Fields)

- [ ] `metrics.nim_pct` (net interest margin)
- [ ] `metrics.cet1_ratio`
- [ ] `metrics.npl_ratio`
- [ ] `ratings.sp`, `ratings.moodys`
- [ ] `capital.regulatory_ratio` (CET1, Tier 1, Total Capital)

## Investment Portfolio Section (REQUIRED)

- [ ] Securities portfolio size and composition
- [ ] Unrealized gains/losses (AOCI impact)
- [ ] Duration and rate sensitivity

## Capital & Liquidity Section (REQUIRED)

- [ ] CET1, Tier 1, Total Capital ratios
- [ ] LCR (Liquidity Coverage Ratio) if disclosed
- [ ] Dividend capacity
- [ ] Share repurchase authorization

## Risk Register — Liability Uncertainty (REQUIRED)

- [ ] Allowance for credit losses adequacy
- [ ] CECL reserve coverage ratios
- [ ] Stress test results if disclosed

## Credit Quality Metrics

- [ ] NPL ratio and trend
- [ ] NCO (net charge-off) rate
- [ ] Allowance coverage ratio
- [ ] Criticized/classified assets

## Return Metrics (REQUIRED)

- [ ] **ROTCE (Return on Tangible Common Equity)** — primary return metric for banks, NOT ROIC
  - If disclosed in MD&A, extract directly
  - If not disclosed, calculate: `(Net Income - Preferred Dividends) / Average Tangible Common Equity`
  - TCE = Total Stockholders' Equity - Goodwill - Intangibles - Preferred Stock

## Thesis-Critical Regulatory Risks (ACTIVELY SEARCH FOR)

- [ ] **Basel III Endgame** — search "Basel", "capital requirements", "risk-weighted assets"
- [ ] **CECL changes** — search "CECL", "allowance methodology", "credit losses"
- [ ] **Stress test results** — search "CCAR", "DFAST", "stress test"
- [ ] **Resolution planning / TLAC** — search "TLAC", "resolution", "living will", "total loss-absorbing capacity"
  - G-SIBs must maintain minimum TLAC
  - Look for resolution planning discussions and any regulatory actions
