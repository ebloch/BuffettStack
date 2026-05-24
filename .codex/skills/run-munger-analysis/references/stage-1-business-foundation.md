# Stage 1: Business Foundation

**Purpose:** Assess Circle of Competence and Financial Strength using Business Overview and Financial Statements.

**Input Documents (~8K tokens):**
- Business Overview memo (multi-year synthesis)
- Financial Statements markdown

**Output:** Working Analysis v1 (~2,500 tokens)

---

## Instructions

You are conducting Stage 1 of a 4-stage Munger Analysis. Your role is to establish the business and financial foundation that later stages will build upon.

### Documents to Read

1. **Business Overview** — `**/[Company]/1-Foundation/*Overview*.md`
   - Provides multi-year synthesis of all 10K memos
   - Focus on: Business model, segments, key metrics, financial evolution, management credibility scorecard, risk trajectory

2. **Financial Statements** — `**/[Company]/1-Foundation/1.3-Financial-Statements/*.md`
   - Focus on: Balance sheet strength, returns on capital, FCF trends

### What to Assess

#### 1. Circle of Competence (Full Assessment)

Ask yourself:
- Can I explain how this business makes money in 2-3 simple sentences?
- What are the 3 key drivers of long-term economics?
- What would cause this business to fail? (Inversion — list 3 failure modes)

**Assessment:** INSIDE / PARTIAL / OUTSIDE

**Critical:** If OUTSIDE, note this clearly. The final memo may recommend not proceeding.

#### 2. Financial Strength (Full Assessment)

Evaluate:
- **Balance Sheet:** Cash position, debt levels, Debt/EBITDA, interest coverage
- **Returns on Capital:** ROIC, ROE, ROCE — current vs. 5Y vs. 10Y trends
- **Free Cash Flow:** FCF margin, FCF conversion, consistency

**Score:** -2 to +2
**Assessment:** FORTRESS / STRONG / ADEQUATE / WEAK / DISTRESSED

**Remember the +2 Gate:** Only award +2 if there are NO material concerns. If "Why Not Higher?" has substantive content, score +1.

#### 3. Predictability (Partial — Financial Factors Only)

Identify:
- **Stability factors:** Recurring revenue, low cyclicality, stable margins
- **Volatility factors:** Commodity exposure, rate sensitivity, lumpy revenue

**Note:** This is partial. Stage 2 will add execution track record, Stage 3 will add competitive/disruption risks.

### Cross-Reference Flags

Identify 2-4 items that Stage 2 (Management) should validate or challenge:
- Financial claims that depend on management quality
- Capital allocation questions
- Execution consistency questions

### Output Format

Use the Working Analysis v1 template from `working-analysis-template.md`.

Write your output in a code block labeled `Working Analysis v1` so it can be referenced by later stages.

---

## Scoring Reference

### Financial Strength Scoring

| Score | Assessment | Criteria |
|-------|------------|----------|
| +2 | FORTRESS | Net cash or minimal debt, ROIC >15% sustained, FCF conversion >80%, no concerns |
| +1 | STRONG | Low leverage, ROIC >12%, consistent FCF, minor concerns |
| 0 | ADEQUATE | Moderate leverage, ROIC ~WACC, variable FCF |
| -1 | WEAK | High leverage, ROIC <WACC, FCF concerns |
| -2 | DISTRESSED | Excessive debt, negative returns, cash burn |

### Circle of Competence Assessment

| Assessment | Criteria |
|------------|----------|
| INSIDE | Business model is simple and understandable. Can explain it in 1 paragraph. Key drivers are clear. |
| PARTIAL | Understand the basics but some complexity remains. Industry dynamics or key metrics not fully grasped. |
| OUTSIDE | Business is too complex, opaque, or unfamiliar. Would require significant study to understand. |

---

## Key Principles

1. **Be specific with numbers:** Don't just say "strong ROIC" — say "ROIC of 18% vs. 15% 5Y ago"
2. **Show direction:** Use ↑/→/↓ to indicate trends
3. **Inversion is mandatory:** The failure modes are as important as the success factors
4. **Preserve evidence:** Later stages will rely on your findings — include key data points
5. **Flag uncertainties:** If something needs management or competitive validation, flag it explicitly
