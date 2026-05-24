# Business Economics Analysis - Validation Checklist

Binary pass/fail criteria for validating output quality.

**For automated QC/Audit:** Each check is classified as either:
- **FIXABLE** — Can be fixed without source data (format, structure, placeholders)
- **FLAG-ONLY** — Requires source verification to fix (content accuracy)

---

## Executive Summary

| Check | Classification |
|-------|----------------|
| Quick Reference table uses exact 6 questions | FIXABLE |
| Question column has correct text | FIXABLE |
| Answers reference correct sections | FLAG-ONLY |
| At least 2 quirks in "The Big Quirks" | FLAG-ONLY |
| At least 3 metrics in "What to Focus On" | FLAG-ONLY |
| At least 2 metrics in "What to Ignore" | FLAG-ONLY |

- [ ] Quick Reference table uses **exactly the 6 question rows** from the template (do NOT substitute with an "attribute" table):
  - Row 1: "What type of business?" → Primary classification from Section 1
  - Row 2: "What's the key metric?" → #1 Primary KPI from Section 4
  - Row 3: "What's misleading in GAAP?" → Top quirk from Section 3
  - Row 4: "What multiple to use?" → Preferred multiple from Section 8
  - Row 5: "Who are true peers?" → Top 2-3 peers from Section 7
  - Row 6: "Biggest analytical mistake?" → #1 mistake from Section 6
- [ ] **FORMAT CHECK (FIXABLE):** The Question column must contain the exact text above, not different attribute labels
  - **COMMON MISTAKE:** Do NOT paraphrase questions. "What's the biggest accounting quirk?" ≠ "What's misleading in GAAP?"
  - **SELF-CHECK:** Before finalizing, verify each question matches EXACTLY (copy-paste if needed)
- [ ] At least 2 quirks listed in "The Big Quirks" section **(FLAG-ONLY if missing content)**
- [ ] At least 3 metrics listed in "What to Focus On" **(FLAG-ONLY if missing content)**
- [ ] At least 2 metrics listed in "What to Ignore" **(FLAG-ONLY if missing content)**

---

## Section 1: Business Model Classification

| Check | Classification |
|-------|----------------|
| Primary category assigned | FLAG-ONLY |
| "How This Business Makes Money" is company-specific | FLAG-ONLY |
| Explanation identifies actual cash source | FLAG-ONLY |

- [ ] Primary category assigned from standard classification table **(FLAG-ONLY)**
- [ ] "How This Business Makes Money" explanation is company-specific (not generic industry description) **(FLAG-ONLY)**
- [ ] Explanation identifies the actual cash source (not just "sells products/services") **(FLAG-ONLY)**

---

## Section 2: Economic Engine

| Check | Classification |
|-------|----------------|
| All 6 driver rows filled | FIXABLE (structure) / FLAG-ONLY (content) |
| Core Unit of Value is specific | FLAG-ONLY |
| Capital Intensity includes reasoning | FLAG-ONLY |
| Economic Engine Summary present | FIXABLE (header) / FLAG-ONLY (content) |

- [ ] All 6 driver rows in table are filled (Primary Cash Source, Core Unit of Value, Growth Drivers, Margin Drivers, Capital Intensity, Reinvestment Requirements) **(FLAG-ONLY if content missing)**
- [ ] Core Unit of Value is specific (e.g., "clearing transaction" not "revenue") **(FLAG-ONLY)**
- [ ] Capital Intensity answer includes reasoning, not just "high" or "low" **(FLAG-ONLY)**
- [ ] Economic Engine Summary paragraph present and explains the economics in plain language **(FLAG-ONLY)**

---

## Section 3: Key Accounting Quirks

| Check | Classification |
|-------|----------------|
| At least 2 quirks documented | FLAG-ONLY |
| Each quirk has What/Distortion/Adjustment | FIXABLE (structure) / FLAG-ONLY (content) |
| Quirks are company-specific | FLAG-ONLY |
| At least 1 references specific GAAP | FLAG-ONLY |

- [ ] At least 2 quirks documented **(FLAG-ONLY if content missing)**
- [ ] Each quirk has all 3 required elements: What (description), Distortion (impact), Adjustment (how to handle) **(FIXABLE for structure, FLAG-ONLY for content)**
- [ ] Quirks are company-specific, not generic industry quirks copy-pasted **(FLAG-ONLY)**
- [ ] At least 1 quirk references specific GAAP treatment or line item **(FLAG-ONLY)**

---

## Section 4: Metrics That Matter

| Check | Classification |
|-------|----------------|
| At least 5 metrics in table | FLAG-ONLY |
| "Why It Matters" present | FLAG-ONLY |
| "Where to Find It" present | FLAG-ONLY |
| Benchmark has good threshold | FLAG-ONLY |
| Benchmark has concern threshold | FIXABLE (add placeholder) |
| Benchmark is quantified | FIXABLE (add placeholder) |
| Primary KPIs ranked 1-2-3 | FLAG-ONLY |

- [ ] At least 5 metrics in the table **(FLAG-ONLY)**
- [ ] Each metric has "Why It Matters" explanation (not just "important for this industry") **(FLAG-ONLY)**
- [ ] Each metric has "Where to Find It" source (e.g., "10-K Item 7", "Earnings release") **(FLAG-ONLY)**
- [ ] **CRITICAL: Each metric has a QUANTIFIED benchmark** — must be a number, range, or threshold (e.g., "<90% excellent", "15-20% historical range", ">12% is strong") **(FIXABLE: add "[quantify]" placeholder)**
- [ ] **CRITICAL: Each benchmark must include a "concerning" or "alert" threshold** — not just what's "good" **(FIXABLE: add "; [concern threshold needed]")**
  - REQUIRED format: [Good threshold] + [Concern threshold]
  - Example: ">80% excellent; 50-80% acceptable; <50% concerning"
  - NOT just: ">15 is good" (missing what triggers concern)
- [ ] **Benchmark format check (FIXABLE):** Each benchmark must be an evaluation threshold, NOT a comparative statement
  - GOOD: ">8% is strong, 5-8% adequate, <5% concerning"
  - BAD: "should track or exceed revenue growth"
- [ ] Benchmarks are NOT qualitative (FIXABLE: add "[quantify]") — reject: "higher is better", "growth = good"
- [ ] Primary KPIs ranked 1-2-3 with reasoning for order **(FLAG-ONLY)**

---

## Section 5: Metrics to Ignore or Adjust

| Check | Classification |
|-------|----------------|
| At least 2 misleading metrics | FLAG-ONLY |
| Each has problem + alternative | FLAG-ONLY |
| GAAP Net Income Issues section | FIXABLE (header) / FLAG-ONLY (content) |
| GAAP Cash Flow Issues section | FIXABLE (header) / FLAG-ONLY (content) |
| Standard Ratio Assessment table | FIXABLE (structure) / FLAG-ONLY (content) |

- [ ] At least 2 metrics identified as misleading **(FLAG-ONLY)**
- [ ] Each metric has specific problem explanation **(FLAG-ONLY)**
- [ ] Each metric has alternative approach **(FLAG-ONLY)**
- [ ] **GAAP Net Income Issues** section present with company-specific explanation **(FIXABLE for header, FLAG-ONLY for content)**
- [ ] **GAAP Cash Flow Issues** section present with company-specific explanation **(FIXABLE for header, FLAG-ONLY for content)**
- [ ] Standard Ratio Assessment table covers P/E, EV/EBITDA, P/B, FCF Yield **(FIXABLE for structure, FLAG-ONLY for content)**
- [ ] Each ratio has usability rating with explanation **(FLAG-ONLY)**

---

## Section 6: Common Analytical Mistakes

| Check | Classification |
|-------|----------------|
| At least 2 mistakes documented | FLAG-ONLY |
| Each has "Why It's Wrong" | FLAG-ONLY |
| Each has "Correct Approach" | FLAG-ONLY |
| At least 1 Red/Green Flag documented | FIXABLE (section header) / FLAG-ONLY (content) |

- [ ] At least 2 mistakes documented in table **(FLAG-ONLY)**
- [ ] Each mistake has "Why It's Wrong" explanation **(FLAG-ONLY)**
- [ ] Each mistake has "Correct Approach" guidance **(FLAG-ONLY)**
- [ ] At least 1 "Red Flag That Isn't" or "Green Flag That Isn't" documented **(FIXABLE for section header, FLAG-ONLY for content)**

---

## Section 7: Peer Selection

| Check | Classification |
|-------|----------------|
| At least 2 true comparables | FLAG-ONLY |
| Each has "Why Comparable" | FLAG-ONLY |
| Each has "Key Differences" | FLAG-ONLY |
| At least 1 false comparable | FLAG-ONLY |
| "Best Comparables for Valuation" list | FLAG-ONLY |

- [ ] At least 2 true comparable peers listed **(FLAG-ONLY)**
- [ ] Each peer has "Why Comparable" explanation **(FLAG-ONLY)**
- [ ] Each peer has "Key Differences" noted **(FLAG-ONLY)**
- [ ] At least 1 false comparable identified with explanation **(FLAG-ONLY)**
- [ ] "Best Comparables for Valuation" list provided **(FLAG-ONLY)**

---

## Section 8: Valuation Implications

| Check | Classification |
|-------|----------------|
| At least 2 preferred methods with rationale | FLAG-ONLY |
| Multiples table has at least 4 multiples | FIXABLE (structure) / FLAG-ONLY (content) |
| Each multiple has usability rating | FLAG-ONLY |
| Benchmark Range for High/Medium multiples | FIXABLE (add placeholder) |
| DCF Considerations table | FIXABLE (structure) / FLAG-ONLY (content) |
| Owner's Earnings with dollar amounts | FLAG-ONLY |
| All amounts sourced or marked [EST] | FIXABLE (add "[source needed]") |
| Same fiscal year across all figures | FLAG-ONLY |
| Quirk-to-Calculation mapping table | FIXABLE (skeleton) / FLAG-ONLY (content) |
| All quirks mapped | FLAG-ONLY |
| Terminal Value considerations | FIXABLE (header) / FLAG-ONLY (content) |

- [ ] At least 2 preferred valuation methods listed with rationale **(FLAG-ONLY)**
- [ ] Multiples Assessment table has at least 4 multiples rated **(FIXABLE for structure, FLAG-ONLY for content)**
- [ ] Each multiple has usability rating (High/Medium/Low/Avoid) with explanation **(FLAG-ONLY)**
- [ ] **CRITICAL: Benchmark Range column is filled for every multiple rated High or Medium** (use "N/A" only for Avoid/Low ratings) **(FIXABLE: add "[verify range]")**
  - **REQUIRED FORMAT:** `"<Ax cheap, A-Bx typical, >Cx expensive"`
  - **FAIL** if benchmark only shows "typical" range without cheap/expensive thresholds
- [ ] DCF Considerations table has at least 1 issue documented **(FIXABLE for structure, FLAG-ONLY for content)**
- [ ] Owner's Earnings calculation shows company-specific adjustments (not just generic formula) **(FLAG-ONLY)**
- [ ] **CRITICAL: Owner's Earnings shows explicit adjustment line items with dollar amounts** **(FLAG-ONLY)**
- [ ] **CRITICAL: All Owner's Earnings dollar amounts are sourced or labeled as estimates:** **(FIXABLE: add "[source needed]")**
  - Figures from 10-K/financial statements → cite source
  - Analyst estimates → marked with `[EST: methodology]`
- [ ] **CRITICAL: Owner's Earnings uses consistent fiscal year across ALL line items** **(FLAG-ONLY)**
- [ ] **For EACH major quirk identified in Section 3**, there is a corresponding entry in the Quirk-to-Calculation Mapping table **(FIXABLE for skeleton table, FLAG-ONLY for complete mapping)**
- [ ] Quirk-to-Calculation Mapping table accounts for ALL quirks from Section 3 **(FLAG-ONLY)**
- [ ] If multiple Owner's Earnings approaches shown, reconciliation paragraph explains the difference **(FLAG-ONLY)**
- [ ] Terminal Value considerations noted **(FIXABLE for header, FLAG-ONLY for content)**

---

## Section 9: Seasonality & Working Capital (for applicable businesses)

| Check | Classification |
|-------|----------------|
| Seasonality section present if applicable | FLAG-ONLY |
| Quarterly patterns described | FLAG-ONLY |
| Period comparison impact noted | FLAG-ONLY |

- [ ] If business has material deferred revenue, float, or working capital timing effects, seasonality section present **(FLAG-ONLY)**
- [ ] Quarterly patterns described (e.g., "float highest Q1-Q2 as summer bookings collected") **(FLAG-ONLY)**
- [ ] Impact on period-over-period analysis noted **(FLAG-ONLY)**

---

## Content Quality Checks

| Check | Classification |
|-------|----------------|
| No generic industry descriptions | FLAG-ONLY |
| Specific numbers referenced | FLAG-ONLY |
| Company's own terminology used | FLAG-ONLY |
| All guidance is actionable | FLAG-ONLY |
| ROIC guidance for asset-light | FLAG-ONLY |
| Quantified risk impacts | FLAG-ONLY |

- [ ] No generic industry descriptions - all content is company-specific **(FLAG-ONLY)**
- [ ] Specific numbers, percentages, or line items referenced where applicable **(FLAG-ONLY)**
- [ ] Language references company's own terminology from filings **(FLAG-ONLY)**
- [ ] All guidance is actionable (tells analyst what to DO, not just what IS) **(FLAG-ONLY)**
- [ ] For asset-light businesses, ROIC calculation guidance explains what constitutes "invested capital" **(FLAG-ONLY)**
- [ ] Key risks include quantified impact estimate where data permits **(FLAG-ONLY)**

---

## Data Consistency Checks (CRITICAL)

| Check | Classification |
|-------|----------------|
| Calculation figures match stated figures | FLAG-ONLY |
| No uncertain data with caveats | FLAG-ONLY |
| Consistent approximations | FLAG-ONLY |
| Industry multiple benchmarks included | FIXABLE (placeholder) / FLAG-ONLY (values) |

- [ ] **Calculation consistency:** Figures used in calculations must match figures stated elsewhere **(FLAG-ONLY)**
- [ ] **No uncertain data:** Do NOT include data points with uncertainty qualifiers **(FLAG-ONLY)**
- [ ] **Consistent approximations:** If using approximate figures, use the same approximation throughout **(FLAG-ONLY)**
- [ ] **Industry multiple benchmarks:** If introducing an industry-specific multiple, include a benchmark range **(FIXABLE for placeholder, FLAG-ONLY for values)**

---

## Source Validation

| Check | Classification |
|-------|----------------|
| Sources section lists materials | FIXABLE (section) / FLAG-ONLY (content) |
| 10-K synthesis memo was read | FLAG-ONLY |
| At least 1 web search conducted | FLAG-ONLY |

- [ ] Sources section lists materials used **(FIXABLE for section header, FLAG-ONLY for content)**
- [ ] 10-K synthesis memo was read (per prerequisites) **(FLAG-ONLY)**
- [ ] At least 1 web search conducted for company-specific accounting guidance **(FLAG-ONLY)**

---

## Citation Requirements (CRITICAL)

| Check | Classification |
|-------|----------------|
| Numerical claims sourced | FIXABLE (add "[source needed]") |
| No unsourced peer/industry claims | FLAG-ONLY |
| Estimates labeled | FIXABLE (add "[EST]") |
| Generic benchmarks caveated | FIXABLE (add "[industry generalization]") |

- [ ] **All numerical claims must be sourced or marked as estimates** **(FIXABLE: add placeholder)**
- [ ] **No unsourced claims about peers or industry** **(FLAG-ONLY)**
- [ ] **Estimates must be labeled** **(FIXABLE: add "[EST]")**
- [ ] **Generic industry benchmarks must be sourced or caveated** **(FIXABLE: add "[industry generalization]")**

---

## Industry-Specific Validation (If Checklist Loaded)

**Only apply if an industry checklist was used during synthesis.**

### General Industry Compliance

| Check | Classification |
|-------|----------------|
| All required industry metrics present in Section 4 | FLAG-ONLY |
| All required industry quirks present in Section 3 | FLAG-ONLY |
| Valuation method follows industry guidance | FLAG-ONLY |
| Industry-specific benchmarks used | FLAG-ONLY |

### Insurance Industry Checklist

If industry = "insurance", verify these requirements from `industry-checklists/insurance.md`:

#### Section 3: Required Quirks

- [ ] Reserve Estimation Uncertainty quirk documented (PYD impact) **(FLAG-ONLY)**
- [ ] Float Economics quirk documented **(FLAG-ONLY)**
- [ ] AOCI Volatility quirk documented **(FLAG-ONLY)**
- [ ] Reinsurance Accounting quirk documented **(FLAG-ONLY)**

#### Section 4: Required Metrics

| Metric | Check | Classification |
|--------|-------|----------------|
| Combined Ratio | Present with <95%/95-100%/>100% benchmarks | FLAG-ONLY |
| Loss Ratio | Present separately from Combined Ratio | FLAG-ONLY |
| Expense Ratio | Present with trend direction noted | FLAG-ONLY |
| CAY Loss Ratio ex-Cat | Present for underwriting quality assessment | FLAG-ONLY |
| Investment Yield | Calculated as NII/Avg Invested Assets | FLAG-ONLY |
| ROE vs. Cost of Equity | Spread analysis with value creation threshold | FLAG-ONLY |
| Book Value Per Share Growth | CAGR with 10%/5-10%/<5% benchmarks | FLAG-ONLY |
| Reserve Development (PYD) | Favorable/adverse trend documented | FLAG-ONLY |

#### Section 8: Valuation Method

- [ ] Price-to-Book (P/B) is PRIMARY valuation method **(FLAG-ONLY)**
- [ ] P/B justified by ROE (>15% = 1.5-2x, 12-15% = 1.2-1.5x, etc.) **(FLAG-ONLY)**
- [ ] EV/EBITDA marked as "Avoid" or explained why inappropriate **(FLAG-ONLY)**
- [ ] Raw P/E marked as "Low" or "Avoid" due to earnings volatility **(FLAG-ONLY)**
- [ ] DCF considerations include cat normalization **(FLAG-ONLY)**
- [ ] Owner's Earnings normalized for PYD **(FLAG-ONLY)**

---

## Summary: FIXABLE vs FLAG-ONLY

### FIXABLE Violations (Audit can auto-fix)

| Violation Type | Fix Applied |
|----------------|-------------|
| Wrong Quick Reference questions | Replace with exact 6 questions |
| Missing concern threshold in benchmark | Add "; [concern threshold needed]" |
| Missing source citation in Owner's Earnings | Add "[source needed]" |
| Missing Quirk-to-Calculation table | Add skeleton table |
| Missing benchmark range for High/Medium multiple | Add "[verify range]" |
| Missing section headers | Add header with placeholder |
| Missing "[EST]" label | Add "[EST: verify methodology]" |
| Qualitative benchmark | Add "[quantify]" |

### FLAG-ONLY Violations (Requires QC/manual review)

| Violation Type | Why FLAG-ONLY |
|----------------|---------------|
| Incorrect dollar amounts | Needs 10K to verify |
| Wrong business model classification | Needs source verification |
| Incomplete quirk mapping | Requires understanding of all quirks |
| Thin analysis sections | Needs source reading to expand |
| Missing content (metrics, quirks, peers) | Content must come from research |
| Calculation consistency errors | Needs verification across document |
