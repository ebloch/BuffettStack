# Phase 1: Annual Filing Synthesis Prompt

Use this prompt for the synthesis pass of `$synthesize-annual-filing`.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are synthesizing the FY [YEAR] [FORM_TYPE] for [COMPANY] ([TICKER]).

**Filing Details:**
- Form Type: [FORM_TYPE] (10-K = US company, 20-F = foreign private issuer, 40-F = Canadian company, URD = French, UK-ANNUAL-REPORT = UK, INTEGRATED-REPORT = Japanese/international)
- Accounting Standard: [ACCOUNTING_STANDARD] (GAAP or IFRS)
- Parsing Mode: [PARSING_MODE] (sec = EDGAR, pdf = PDF file)
- PDF Source: [PDF_SOURCE] (only when PARSING_MODE=pdf)

**IMPORTANT:** You have access ONLY to this year's filing. Do not reference or compare to other years except where the filing itself provides prior year comparisons.

## Script Usage (MANDATORY)

**DO NOT** write ad-hoc Python. Use ONLY the bundled scripts:
- `python3 scripts/parse_annual_filing.py TICKER [--year YYYY]`
- `python3 scripts/parse_pdf_filing.py [URL or path]`

**Forbidden:** `python3 -c "..."`, heredoc (`<< EOF`), temp scripts. If parsing fails, report in Questions — do not work around with custom code.

## Your Task

1. Parse the annual filing:
   - If PARSING_MODE=sec: `python3 scripts/parse_annual_filing.py [TICKER] --year [YEAR]`
   - If PARSING_MODE=pdf: `python3 scripts/parse_pdf_filing.py [PDF_SOURCE] --json`
2. Read the output template from: `references/output-template.md`
3. Identify the company's industry and read the appropriate checklist from: `references/industry-checklists/[INDUSTRY].md`
4. Read the validation checklist from: `references/validation-checklist.md`
5. Synthesize the annual filing following the template structure (hybrid format)
6. Complete the validation checklist before finalizing
7. Write the memo to: [OUTPUT_PATH]

## Output Format Requirements

### YAML Frontmatter (REQUIRED)
Every memo MUST start with valid YAML frontmatter containing:
- Basic metadata: company, ticker, fiscal_year, filing_date, synthesis_date, industry, form_type, accounting_standard
- Key metrics: revenue_m, operating_income_m, net_income_m, fcf_m, employees + industry-specific
- **Ratings** (for insurers/banks): am_best, sp, moodys, outlook
- Segments: name, revenue_m, pct_total (top 3-5)
- **Affiliates** (simplified): name, ownership_pct, income_contribution_m
- Capital: buyback_auth_remaining_m, buyback_deployed_fy_m, dividends_paid_m, total_debt_m, capital_priorities
- Shares: basic_m, diluted_m, options_rsus_m, dilution_pct
- Quality flags: disclosure (good/adequate/poor), accounting (clean/concerns/red-flags)
- Risk tags: list of risk-tag-slugs for filtering

### Number Formats
- Tables: M suffix, no $ (e.g., `4272M`)
- Prose: Full currency (e.g., `$4.3 billion`)
- Percentages: One decimal (e.g., `21.4%`)
- Per-share: $ + two decimals (e.g., `$53.11`)
- YoY changes: Sign prefix (e.g., `+21.4%`)

### Body Section Style
The body uses a **prose-driven style** for comprehension:
- **Key Takeaways:** 5-7 narrative bullets with **bold lead-ins** — insight + data, not just metrics
- **Business Summary:** 2-3 paragraphs of flowing prose + one segment table (Revenue, % Total, YoY, Op Margin if disclosed)
- **What Changed:** Simple bullet list, no tags
- **Management Commentary:** Direct quote + key points list
- **Guidance & Promises:** Guidance table + Promises to Track table + Claims to Verify table
- **Financial Snapshot:** Two consolidated tables (P&L/Returns + Balance Sheet)
- **Capital Allocation:** Sources/uses table + 2-4 sentence commentary
- **Risk Factors:** 3-5 prose bullets with editorial interpretation — flag [NEW] risks
- **Accounting Quality:** Checklist table + summary sentence
- **Questions for Further Research:** Numbered list with "why it matters" context
- **Topic Index:** Tag cross-reference table
- **Source:** Filing metadata + page references

### Fact vs. Analysis Integration
In Risk Factors, combine disclosed facts with analyst interpretation in prose form:
- State what the 10-K says (with page reference)
- Add your assessment of probability, severity, and whether it's boilerplate or real

### NEW Risk Flagging
Mark risks with `[NEW]` if they are:
- Entirely new risk factors not present in prior year's 10-K
- Materially expanded (significant new language or detail added)
- Elevated in prominence (moved higher in the risk factors list)

## Synthesis Guidelines

- **Token Efficiency:** Target ~2,800-3,100 tokens. Prose is more efficient than multi-table formats.
- **Investor Focus:** Write for someone evaluating this as a potential holding
- **Filter Boilerplate:** Identify what's actually material in Risk Factors
- **Specific Over Generic:** "Revenue grew 15% driven by cloud expansion" > "Revenue grew"
- **Year-over-Year Context:** Use YoY comparisons FROM the 10-K itself
- **Intellectual Honesty:** If the 10-K is vague on something important, note that
- **Bold Lead-ins:** Key Takeaways bullets start with **bold phrase** followed by colon

## Quality Requirements (MANDATORY)

You MUST complete ALL sections. Do not skip sections.

- **MD&A Extraction Check:** Before synthesizing, check if the MD&A section contains full content or just a page reference stub. If incomplete:
  - Add "**MD&A Extraction Note:**" prominently near the top of the output
  - For metrics typically in MD&A, use "Not extracted — see MD&A pages X-Y" (NOT "Not disclosed")
  - Add a question about key missing MD&A data to "Questions for Further Research"
- **"Not Disclosed" vs "Not Extracted" Language:**
  - Use "Not disclosed in 10-K" ONLY for data that genuinely doesn't exist in the filing
  - Use "Not extracted — see pages X-Y" for data that exists but wasn't captured by parser
  - Use "Verify via [external source]" for data types not typically in 10-Ks (e.g., credit ratings)
  - **NEVER say "Not disclosed" for metrics that definitely exist** (e.g., CET1 for major banks, segment revenue)
- **YAML Frontmatter:** Valid YAML with all required fields populated
- **Two-pass MD&A:** Read MD&A twice — first for structure, second to fill gaps (if MD&A content is available)
- **Promises to Track:** Extract at least 2 specific, verifiable commitments with exact quotes. **MUST include page references (p.XX) for EVERY quote.**
- **Claims to Verify:** Identify forward-looking assertions that need external validation. **Include page references.**
- **Page Reference Requirement:** ALL direct quotes from management MUST include page references (p.XX).
- **Thesis-Critical Regulatory Search:** For your industry, actively search for regulatory risks that could fundamentally alter the business model (see industry checklist)
- **Risk Factors:** 3-5 prose bullets with editorial commentary. EVERY bullet MUST include: (1) page reference (p.XX), (2) *Probability: Low/Med/High. Impact: Low/Med/High.* in italics, (3) inline topic tag `[RISK-SLUG]`. Flag [NEW] risks explicitly, or state "Unable to assess [NEW] vs. prior year — single-year analysis" at section start.
- **Topic Index:** List all tags used with section locations. Tags MUST appear inline in body text (Key Takeaways, Risk Factors, Guidance) — not just in the index.
- **Industry-Specific Metrics:** Capture ALL relevant metrics per the industry checklist in YAML frontmatter
- **Calculated Metrics:** ROIC MUST use **average** invested capital (average of beginning and ending), not ending balances. Show calculation methodology in footnote below P&L table: "ROIC = NOPAT $XM / Avg Invested Capital $XM = X%"
- **Affiliate Completeness:** Cross-reference Notes to Financials to ensure ALL equity method investments captured
- **Capital Allocation:** Capture both authorization AND deployment — the gap between them is a signal

## Industry-Specific Requirements

See the industry checklist for detailed requirements. Key points:

**For Banks:**
- Use ROTCE instead of ROIC
- Include regulatory capital ratios (CET1, Tier 1, Total Capital)

**For Insurers:**
- Include combined ratio components table
- Include prior year development table
- Use NPW (not NPE) as Revenue in segment table

**For SaaS:**
- Distinguish gross retention from net retention (attrition → gross retention only)
- Calculate Rule of 40 explicitly

**For Integrated Reports (Japanese/International):**
- Revenue may be in JPY — note currency prominently in YAML and throughout memo
- FYE may be March 31 — confirm and note in metadata
- Equity method investments are often a major income source (>30% of net income for sogo shosha)
- "Medium-Term Management Plan" → extract as guidance section with targets vs. actuals
- "Value Creation Story" → maps to Business Summary
- Use `diversified-conglomerates` industry checklist for sogo shosha

**For REITs:**
- Lead with FFO/AFFO (not GAAP net income)
- Include lease expiration schedule table
- Suppress ROIC (not meaningful for REITs)

**For Alternative Asset Managers:**
- Lead with Distributable Earnings or FRE table
- Include Carried Interest table
- Include Fundraising & Deployment table with Fee Rate

## Ratings Source Verification (CRITICAL)

For financial strength ratings (A.M. Best, S&P, Moody's, Fitch):
- **ONLY include ratings that are EXPLICITLY STATED in the 10-K text**
- Do NOT use external knowledge or memory to fill in ratings
- If ratings are mentioned but specific values not stated, use: "Mentioned but not quantified"
- If ratings section not found in extracted content, use: "Not disclosed in filing"

## Tool Usage (CRITICAL)

- **Shell:** Use ONLY for running the bundled Python parser (`python3 scripts/parse_annual_filing.py ...`)
- **Read files:** Use for reading template files, checklists, and any other files.
- **Edit/write files:** Use for saving the output memo.
- **Do NOT use:** `sed` or `awk` for file manipulation. Use the Read and Write tools instead.

This is professional investment research. Thoroughness matters. Do not take shortcuts.

Do NOT read any other years' filings or memos. Your analysis must be independent.

## Return Value

When complete, return a JSON object:
```json
{
  "output_file_path": "[path to written memo]",
  "industry": "[detected industry slug]",
  "status": "success" | "partial" | "failed",
  "notes": "[any issues encountered]"
}
```
```
