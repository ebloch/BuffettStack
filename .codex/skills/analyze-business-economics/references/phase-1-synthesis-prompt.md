# Phase 1: Business Economics Synthesis Prompt

Use this reference for the synthesis pass for analyze-business-economics.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are creating a Business Economics Analysis for [COMPANY] ([TICKER]).

**Source Documents:**
- Business Overview: [BUSINESS_OVERVIEW_PATH]
- 10K Memo: [10K_MEMO_PATH]

**Output Directory:** [OUTPUT_DIR]
**Timestamp:** [TIMESTAMP]

---

## Your Task

Complete the full business economics analysis workflow:

### Step 1: Read Business Overview (REQUIRED FIRST)

Read the Business Overview memo first. This provides multi-year context and identifies the company's industry classification.

**Extract from Business Overview:**
- Primary business description (used for industry detection)
- Key business segments
- Historical context and trajectory

### Step 2: Identify Industry & Load Checklist

Based on the business description in the Business Overview, identify if the company matches any available industry checklist:

**Available Industry Checklists:**
| Industry | Trigger Keywords | Checklist Path |
|----------|------------------|----------------|
| Insurance | "insurer", "insurance company", "P&C", "property and casualty", "underwriter" | `industry-checklists/insurance.md` |

**If industry match found:**
1. Read the industry checklist: `.codex/skills/analyze-business-economics/references/industry-checklists/[industry].md`
2. The checklist specifies REQUIRED metrics, quirks, and valuation methods for this industry
3. These requirements SUPPLEMENT (not replace) the generic output template

**If no industry match:** Proceed with generic template only.

### Step 3: Read 10K Source Material

Read the 10K synthesis memo provided (most recent year). Pay special attention to:
- Business description and revenue model
- Critical Accounting Policies section
- Management's discussion of metrics they use
- Unusual line items or disclosures
- Industry-specific terminology
- Segment reporting structure
- Cash flow statement anomalies

**CRITICAL:** Track key facts, metrics, and accounting policies you extract — these become the basis for your analysis.

**Note:** Only the most recent 10K memo is provided because accounting policies rarely change year-to-year. The Business Overview already provides multi-year context.

### Step 4: Read Templates

Read required templates:
- Output template: `.codex/skills/analyze-business-economics/references/output-template.md`
- Validation checklist: `.codex/skills/analyze-business-economics/references/validation-checklist.md`
- Industry checklist (if loaded in Step 2): `.codex/skills/analyze-business-economics/references/industry-checklists/[industry].md`

### Step 5: Web Research

Conduct targeted searches to supplement 10K understanding:
- "[COMPANY] accounting policies"
- "[COMPANY] non-GAAP metrics"
- "[COMPANY] investor FAQ financials"
- "[Industry] financial analysis guide"
- "How to analyze [industry] companies"
- "[COMPANY] owner's earnings calculation"

### Step 6: Generate Analysis

Create the full analysis following the output template structure:

#### Section 1: Business Model Classification

- Assign primary category from standard classification table
- Identify secondary characteristics if hybrid
- Write "How This Business Makes Money" — must be company-specific, not generic

#### Section 2: Economic Engine

Fill ALL 6 driver rows in table:
- Primary Cash Source
- Core Unit of Value (specific, not "revenue")
- Growth Drivers
- Margin Drivers
- Capital Intensity (with reasoning)
- Reinvestment Requirements

Write Economic Engine Summary paragraph.

For asset-light businesses: Include ROIC calculation guidance.
If seasonal: Include working capital timing description.

#### Section 3: Key Accounting Quirks (MINIMUM 2)

For each quirk, document:
- **What:** Description of the accounting treatment
- **Distortion:** What line items are affected and how
- **Adjustment:** How to handle it
- **Example:** Specific reference from 10K if available

**CRITICAL:** Each quirk must reference specific GAAP treatment or line items from the company's filings.

**INDUSTRY CHECKLIST INTEGRATION:**
If an industry checklist was loaded in Step 2, ALL quirks listed under "Required Quirks" MUST be documented. Customize the generic descriptions with company-specific examples from the 10K memos.

#### Section 4: Metrics That Matter (MINIMUM 5)

For each metric:
- Why It Matters — company-specific explanation
- Where to Find It — specific source (10K section, earnings release, etc.)
- Benchmark — MUST include BOTH:
  - Good threshold (e.g., ">85% strong")
  - Concern threshold (e.g., "<78% signals pricing erosion")

**BENCHMARK FORMAT REQUIRED:**
- ">8% strong, 5-8% adequate, <5% concerning"
- "80-85% for quality pharma; <78% signals pricing erosion"
- NOT: "higher is better" or "15+ for large cap"

**INDUSTRY CHECKLIST INTEGRATION:**
If an industry checklist was loaded in Step 2, ALL metrics marked "REQUIRED" in that checklist MUST be included in Section 4. Use the checklist's benchmarks as a starting point, then refine based on company-specific context.

Rank Primary KPIs 1-2-3 with reasoning.

#### Section 5: Metrics to Ignore or Adjust (MINIMUM 2)

For each:
- The metric
- Why it's misleading for THIS company
- What to do instead

Complete:
- GAAP Net Income Issues — company-specific explanation
- GAAP Cash Flow Issues — company-specific explanation
- Standard Ratio Assessment table (P/E, EV/EBITDA, P/B, FCF Yield)

#### Section 6: Common Analytical Mistakes (MINIMUM 2)

Document mistakes generalist analysts make:
- The mistake
- Why it's wrong for this business
- Correct approach

Include at least one:
- Red Flag That Isn't a Red Flag, OR
- Green Flag That Isn't a Green Flag

If quantifiable: Include risk impact calculations.

#### Section 7: Peer Selection (MINIMUM 2 true, 1 false)

True Comparables:
- Peer name
- Why comparable
- Key differences

False Comparables:
- Company name
- Why it seems similar
- Why it's not comparable

Rank "Best Comparables for Valuation" and "Best Comparables for Operating Metrics."

#### Section 8: Valuation Implications

**Preferred Valuation Methods:** List primary and secondary with rationale.

**INDUSTRY CHECKLIST INTEGRATION:**
If an industry checklist was loaded in Step 2, follow the "Valuation Guidance" section:
- Use the PRIMARY valuation method specified (e.g., P/B with ROE adjustment for insurance)
- AVOID methods listed as inappropriate for this industry
- Apply industry-specific DCF considerations

**Multiples Assessment Table:**
- Rate each multiple (High/Medium/Low/Avoid)
- Provide explanation
- **CRITICAL:** Include Benchmark Range for every High/Medium rated multiple
  - Format: "<20x cheap, 20-28x typical, >30x expensive"

**DCF Considerations Table:** At least 1 issue documented.

**Owner's Earnings Calculation:**

CRITICAL REQUIREMENTS:
1. **All figures from SAME fiscal year** — do not mix FY2024 and FY2025
2. **Every $ amount must be sourced:**
   - From 10K → cite "per 10-K FY[YEAR]"
   - Estimated → mark with "[EST: methodology]"
3. **Map EVERY Section 3 quirk** to either:
   - Dollar adjustment line item, OR
   - Interpretation note

Format:
```
Net Income                                    $X,XXXM (FY[Year]) [per 10-K synthesis]
+ Depreciation & Amortization                    $XXXM [per 10-K]
- Maintenance CapEx                              ($XXXM) [EST: X% of total, based on Y]
+/- [QUIRK 1]: [brief description]               $XXXM [source]
+/- [QUIRK 2]: [brief description]               ($XXXM) [source]
= Owner's Earnings                            ~$X,XXXM

Note: [Any interpretation quirks that affect how to read this figure]
```

**Quirk-to-Calculation Mapping Table (REQUIRED):**
| Section 3 Quirk | Treatment | Line Item or Note |
|-----------------|-----------|-------------------|
| [Quirk 1] | Dollar adjustment | [Line item name] |
| [Quirk 2] | Interpretation note | See calculation note |

Map ALL quirks from Section 3.

### Step 7: Complete Validation Checklist

**MANDATORY:** Complete ALL validation passes before writing final analysis:

- [ ] Quick Reference uses exact 6 questions
- [ ] At least 2 quirks with What/Distortion/Adjustment
- [ ] At least 5 metrics with quantified benchmarks (good + concern thresholds)
- [ ] At least 2 misleading metrics with alternatives
- [ ] At least 2 analytical mistakes documented
- [ ] At least 2 true peers + 1 false comparable
- [ ] Owner's Earnings shows dollar amounts with sources
- [ ] Quirk-to-Calculation mapping table complete
- [ ] Multiples with High/Medium rating have benchmark ranges
- [ ] **If industry checklist loaded:** All required industry metrics present
- [ ] **If industry checklist loaded:** All required industry quirks documented
- [ ] **If industry checklist loaded:** Valuation method follows industry guidance

### Step 8: Write Output

Write analysis to:
```
[OUTPUT_DIR]/Business Economics Analysis - [COMPANY] - [TIMESTAMP].md
```

---

## Output Format Requirements

### Quick Reference Table (CRITICAL)

The Question column MUST contain these EXACT 6 questions verbatim:
1. "What type of business?"
2. "What's the key metric?"
3. "What's misleading in GAAP?"
4. "What multiple to use?"
5. "Who are true peers?"
6. "Biggest analytical mistake?"

Do NOT paraphrase these questions. Copy exactly as written.

### Number Formats

- Owner's Earnings: Use $XXXM format with source citations
- Percentages: Include thresholds (">85%" not just "85%")
- Benchmark ranges: Both upper and lower bounds

### Sourcing Requirements

- All Owner's Earnings figures: Sourced or marked [EST]
- All quirk examples: Reference specific 10K disclosures
- All benchmarks: Quantified with both good and concern thresholds

---

## Tool Usage

- **Read:** Use for reading 10K memos, template files, and checklists
- **Write:** Use for saving the output analysis
- **Web search:** Use for supplementary research on accounting policies
- **File search pattern:** Use for finding additional research files if needed

---

## Return Value

When complete, return a JSON object:
```json
{
  "output_file_path": "[path to written analysis]",
  "source_memo": "/path/to/10k-memo.md",
  "business_overview_path": "[path to business overview memo]",
  "industry": "[industry slug or null if no checklist matched]",
  "status": "success" | "partial" | "failed",
  "notes": "[any issues encountered]"
}
```

The `source_memo` path is CRITICAL — Phase 2 QC will use this to re-read the source document.

The `industry` field should be:
- `"insurance"` if insurance checklist was loaded
- `null` if no industry checklist matched
```
