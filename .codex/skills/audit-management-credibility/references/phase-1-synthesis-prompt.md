# Phase 1: Management Credibility Audit Synthesis Prompt

Use this reference for the synthesis pass for audit-management-credibility.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are conducting a comprehensive historical audit of management credibility for [COMPANY] ([TICKER]).

**Output Paths:**
- Analysis: [ANALYSIS_PATH]
- Memo: [MEMO_PATH]
- Output Directory: [OUTPUT_DIR]
- Timestamp: [TIMESTAMP]

---

## Your Task

Complete the full management credibility audit workflow. This is a deep-dive analysis reviewing up to 5 years of earnings transcripts and press releases to systematically assess whether management does what they say they will do.

### Step 1: Read Templates

Read required templates:
- Analysis template: `.codex/skills/audit-management-credibility/references/output-template-analysis.md`
- Memo template: `.codex/skills/audit-management-credibility/references/output-template-memo.md`
- Validation checklist: `.codex/skills/audit-management-credibility/references/validation-checklist.md`

### Step 2: Fetch & Validate Data

**CRITICAL: Use the provided script for ALL FMP API calls. Do NOT use raw curl commands. If `FMP_API_KEY` is unavailable, skip the script and use free sources: company IR pages, earnings-call transcript pages found through web search, SEC filings/proxies, and existing local earnings files.**

**Fetch all transcripts (5 years):**
```bash
.codex/skills/audit-management-credibility/scripts/fmp-fetch.sh transcripts [TICKER] <START_YEAR> <END_YEAR> /tmp
```

Choose a 5-year window ending with the most recent full year. Example for an audit in 2026:
```bash
.codex/skills/audit-management-credibility/scripts/fmp-fetch.sh transcripts [TICKER] 2021 2025 /tmp
```

**Fetch press releases:**
```bash
.codex/skills/audit-management-credibility/scripts/fmp-fetch.sh press-releases [TICKER] 500
```

**After Fetching:** Read the saved transcript files from `/tmp/{ticker}_q{quarter}_{year}.json`

**Quarter counting:** Count the actual number of transcripts retrieved, not the theoretical maximum. If auditing FY2021-FY2025 but only through Q2 of FY2025, that's 18 quarters (4x4 + 2), not 20.

**CRITICAL: Verify quarter count mathematically.** Before writing the header, perform explicit calculation:
- Example: "Q1 2021 to Q1 2025" = 4 (2021) + 4 (2022) + 4 (2023) + 4 (2024) + 1 (2025) = **17 quarters**
- Do NOT estimate or round. Count each quarter in the range.
- The header "X quarters reviewed" MUST match both:
  1. The mathematical calculation above
  2. The actual rows in the Appendix: Source Documents table

**CRITICAL: Header/Appendix consistency.** The quarter count in the document header ("X quarters reviewed") MUST match:
1. The number of transcripts listed in the Appendix: Source Documents table
2. The "X of Y quarters" figure in the Data Sources table

**Press releases to focus on:**
- Earnings announcements
- Guidance updates
- M&A announcements
- Strategic initiative announcements
- Leadership changes

**Note:** Press releases endpoint may require a higher subscription tier. If unavailable, note this in data gaps and proceed with transcripts only.

#### Data Source Tracking

Track what data was successfully retrieved. This table MUST appear in the final output as the **"Data Sources" section** at the very beginning of the Analysis document:

| Source | Count | Date Range | Coverage |
|--------|-------|------------|----------|
| Earnings Transcripts (FMP) | X | YYYY-QX to YYYY-QX | X of Y quarters |
| Earnings Transcripts (web search) | X | YYYY-QX to YYYY-QX | Fallback for missing |
| Press Releases (FMP) | X | YYYY-MM to YYYY-MM | Guidance, M&A, strategic |
| Web Research | N/A | Various | Insider ownership, compensation, proxy |

**Data Gaps:** [Note any missing quarters or "None — full coverage for audit period"]

**If FMP data is unavailable or incomplete:**
- Note which quarters are missing
- Use web search as fallback: search for "[Company] Q[X] [YEAR] earnings call transcript"
- Check company investor-relations sites, SEC filings, and reputable transcript mirrors before giving up on a quarter
- Mark any web search/IR/SEC-sourced transcripts in the final output
- Document gaps clearly in output: `DATA GAPS: Transcripts unavailable for Q1-Q2 2021.`

### Step 3: Extract and Categorize Promises

Systematically review each transcript and relevant press releases. Extract forward-looking commitments.

**Work through transcripts chronologically** (oldest to newest) so you can track promises as they're made and then score them when outcomes become clear.

**Promise Categories:**

| Category | Examples |
|----------|----------|
| **Financial Targets** | Revenue growth, margin expansion, EPS guidance |
| **Capital Allocation** | Buyback amounts, dividend policy, M&A intentions, capex plans |
| **Operational Goals** | Product launches, capacity expansion, headcount |
| **Cost/Efficiency Programs** | Restructuring savings, margin improvement initiatives, cost takeout targets |
| **Strategic Initiatives** | Market entry, partnerships, pivots, long-term vision |

*Note: Timeline commitments are tracked as an attribute of each promise (via the "Timeframe" column) rather than a separate category.*

**Cost/Efficiency Programs (High-Value Tracking):**

These deserve special attention because they are:
- Highly specific (usually dollar amounts)
- Time-bound (usually 2-3 year programs)
- Frequently overpromised
- Often used to justify restructuring charges

For each program announced, track:

| Program Name | Announced | Savings Target | Timeline | Restructuring Cost | Actual Savings | Score |
|--------------|-----------|----------------|----------|-------------------|----------------|-------|
| "Project X" | Q2 2022 | $500M annual | "By 2024" | $300M charge | $XXM | +2 to -2 |

**CRITICAL: Quantify all figures.** The table must contain actual dollar amounts, not qualitative assessments:
- Good: "Actual Savings: $520M" / "Restructuring Cost: $280M"
- Bad: "Actual Savings: Exceeded" / "Restructuring Cost: Included above"

If exact figures are not disclosed, provide best estimate with source: "~$500M (derived from segment OI improvement Q1-Q4 FY2024)"

**What to watch:**
- Do savings targets get revised down over time?
- Are restructuring costs higher than initially estimated?
- Does the program quietly disappear from earnings calls?
- Are "new" efficiency programs announced before old ones are completed?
- Is the savings number gross or net of restructuring costs?

**Business Model Variations:**

Not all companies run formal cost/efficiency programs. Asset managers, exchanges, and holding companies often focus on growth, deployment, and returns rather than cost takeouts.

**If no formal cost programs exist:**
- State explicitly: "No formal cost/efficiency programs announced during audit period. Business model focuses on [growth/deployment/returns] rather than cost optimization."
- Do NOT leave this category empty or use "N/A (organic)"
- Instead, assess: Are there any operational efficiency claims? Fee compression commitments? Margin improvement targets?
- If truly none: Include a brief section explaining why (e.g., "Brookfield operates as an asset manager with fee-based revenue; cost efficiency programs would apply at portfolio company level, not parent entity")

**Distinguishing Formal Programs from Informal Initiatives:**

Not everything management discusses qualifies as a "cost/efficiency program." Use this test:

| Characteristic | Formal Program (include in table) | Informal Initiative (exclude from table) |
|----------------|-----------------------------------|------------------------------------------|
| Has a name | "Project X", "Emerging Stronger" | General "productivity improvements" |
| Has dollar target | "$500M in savings by 2024" | "Ongoing efficiency" |
| Has timeline | "By end of Year 2" | "Continuously improving" |
| Has restructuring charge | $300M charge announced | No charge |
| Reported to investors | Tracked quarter-by-quarter | Mentioned in passing |

**For informal initiatives:** Do NOT create table rows with "N/A" values. Instead, include a note after the table:

```
*Additional efficiency initiatives (not formally tracked): [List with brief description]*
```

**CRITICAL:** If a company announces restructuring charges WITHOUT specific savings targets (common for organizational changes), document the charge but note: "Savings target: Not disclosed. Restructuring charge: $XXM."

**For each promise, record:**
- Date made (quarter/year)
- Source (transcript or press release)
- **Exact quote (REQUIRED - verbatim, in quotation marks)**
- Category
- Specificity rating:
  - **Specific:** Contains a number, date, or measurable target (e.g., "25 net new warehouses," "$400M in synergies by 2025")
  - **Directional:** Indicates direction without a number (e.g., "we expect growth to continue," "margins should improve")
  - **Vague:** Lacks both number and clear direction (e.g., "we're focused on operational excellence") — exclude from scoring
- Timeframe for delivery
- Outcome (when evaluating)

**CRITICAL: Direct Quotes Are Required**

Every promise tracked MUST include the exact verbatim quote from the transcript. This is non-negotiable. Examples:

Good: "We expect to achieve $200 million in run-rate synergies by the end of 2021" - Terry Duffy, Q2 2020

Bad: Management said they would achieve synergies by 2021

Direct quotes:
- Provide evidence the reader can verify
- Capture the specificity (or vagueness) of the commitment
- Allow readers to judge tone and confidence level
- Create accountability for the audit itself

### Step 4: Score Every Promise (Including Misses)

For each promise where sufficient time has passed, determine the outcome.

**CRITICAL: Document ALL Misses Explicitly**

Even if overall credibility is high, you MUST document every missed or partially missed promise in a **dedicated "Missed & Partial Promises" section** in the output. This section is REQUIRED even if credibility is high. This is essential for audit credibility:

1. **Create a "Missed & Partial Promises" section** — List every promise scored 0, -1, or -2
2. **Include the original quote** — What exactly did they promise?
3. **Document how management addressed it** — Did they acknowledge it? Make excuses? Ignore it?
4. **Assess the pattern** — Was this a one-time miss or recurring?

**REQUIRED TABLE:** The Missed & Partial Promises section MUST include this table format:

| Date | Original Promise (Verbatim Quote) | What Happened | Management Response | Score |
|------|-----------------------------------|---------------|---------------------|-------|
| QX 20XX | "[Exact quote]" | [Actual outcome] | [How addressed / Not addressed] | 0/-1/-2 |

**REQUIRED ANALYSIS:** After the table, include:
- Total promises missed or partial: X of Y scored promises (X%)
- Pattern in misses: [Are they concentrated in one area? One time period?]
- How management handles failure: [Transparent / Excuses / Ignored]

**If no misses exist:** State explicitly: "No promises scored below +1 during audit period. Verify scoring rigor was applied."

**Why this matters:** An audit that only highlights successes is promotional, not analytical. Investors need to see how management handles failure — this often reveals more about character than successes do.

**Scoring Scale:**

| Score | Definition | Characteristics |
|-------|------------|-----------------|
| **+2** | Exceeded | Beat stated target by meaningful margin |
| **+1** | Delivered | Achieved what was promised |
| **0** | Partial | Mostly delivered with valid explanation for shortfall |
| **-1** | Missed | Failed to deliver, made excuses or blamed external factors |
| **-2** | Abandoned | Never mentioned again, quietly dropped |

**Scoring Guidelines:**
- Be fair but rigorous
- External factors can justify a 0 but not a +1
- Pattern of "one-time" issues that recur = -1 or -2
- Vague promises that can't be verified = exclude from scoring
- Give credit for transparency about misses (may upgrade -1 to 0)

### Step 5: Analyze Patterns

Look for patterns across the full audit period.

**REQUIRED: Quantitative Scorecard (Three Tables)**

You MUST produce all three of these tables in the Quantitative Scorecard section:

**Table 1: Promise Delivery Summary (by category)**

| Category | Promises Made | Scored | Hit Rate | Avg Score |
|----------|---------------|--------|----------|-----------|
| Financial Targets | X | X | X% | X.X |
| Capital Allocation | X | X | X% | X.X |
| Operational Goals | X | X | X% | X.X |
| Cost/Efficiency Programs | X | X | X% | X.X |
| Strategic Initiatives | X | X | X% | X.X |
| **Total** | **X** | **X** | **X%** | **X.X** |

*Note: Timeline commitments are tracked as an attribute of each promise via the "Timeframe" column, not as a separate category.*

**Table 2: Trend Over Time (by year)**

| Year | Promises Scored | Hit Rate | Avg Score | Notable Events |
|------|-----------------|----------|-----------|----------------|
| 20XX | X | X% | X.X | [CEO change, M&A, etc.] |
| 20XX | X | X% | X.X | |
| ... | | | | |

Include a **Trend statement**: "[Improving / Stable / Declining] — [1-2 sentence explanation]"

**Table 3: Guidance Accuracy (by metric type)**

| Metric Type | Times Guided | Beat | Met | Missed | Accuracy |
|-------------|--------------|------|-----|--------|----------|
| Expense | X | X | X | X | X% |
| Revenue | X | X | X | X | X% |
| Margin | X | X | X | X | X% |
| EPS | X | X | X | X | X% |
| Other | X | X | X | X | X% |

**Guidance philosophy note:** If the company explicitly does not provide guidance for certain metrics (e.g., EPS, revenue), include a row stating "Not Provided — [reason]" rather than omitting the row. This documents the company's guidance approach and shows the analysis was thorough.

Include a **Guidance style statement**: "[Conservative sandbagging / Tight and accurate / Optimistic / Variable]"

**Qualitative Analysis:**

*Positive Patterns (list with specific evidence):*
- Consistent sandbagging (guide low, beat)
- Quick acknowledgment of misses
- Proactive updates when plans change
- Long-term commitments honored

*Negative Patterns:*
- Chronic overpromising
- "One-time" charges that recur
- Moving goalposts (changing definitions of success)
- Strategic initiatives that disappear
- Blaming external factors repeatedly
- Avoiding topics that went wrong
- Guidance always "conservative" but missed

**Kitchen Sink Quarters (Critical Pattern):**

Look for quarters where management dumps multiple negative items at once:
- Large write-downs or impairments
- Restructuring charges
- Guidance reductions
- Leadership changes
- Strategy pivots

**Why this matters:** Kitchen sink quarters are often followed by easy comps and "beat and raise" quarters. This is a manipulation tactic — reset expectations low, then look like heroes.

**How to identify:**
1. Find quarters with unusually large charges or multiple negative announcements
2. Check if guidance was cut significantly that quarter
3. Track subsequent quarters — did they suddenly start beating?
4. Note if CEO/CFO was new (clearing the decks is common for new leadership)

**Scoring implication:** If you see a kitchen sink followed by consistent beats, discount the "credibility" of those beats. They were manufactured.

### Step 6: Say/Do Matrix

Plot management on the credibility matrix:

```
                      DELIVERS
                          |
           UNDERPROMISE   |   CREDIBLE
           OVERDELIVER    |   CONSISTENT
           (Sandbagging)  |   (Trustworthy)
                          |
VAGUE ────────────────────┼──────────────────── SPECIFIC
                          |
           EMPTY          |   OVERPROMISE
           SUITS          |   UNDERDELIVER
           (Avoid)        |   (Promotional)
                          |
                     FAILS TO DELIVER
```

**Quadrant Definitions:**

| Quadrant | Characteristics | Investment Implication |
|----------|-----------------|------------------------|
| **Credible Consistent** (Upper Right) | Specific promises, reliable delivery | High trust, can rely on guidance |
| **Underpromise Overdeliver** (Upper Left) | Conservative but delivers more | Positive surprises likely, guidance is floor |
| **Overpromise Underdeliver** (Lower Right) | Specific but unreliable | Discount all guidance, promotional management |
| **Empty Suits** (Lower Left) | Vague and unreliable | Avoid entirely, no accountability |

### Step 7: Deep Dives on Key Issues

**REQUIRED SECTION:** The "Deep Dive: Key Issues" section MUST appear in the output.

For any significant misses or concerns (scored -1 or -2, or patterns of concern), conduct deeper analysis using this structure:

**For each issue:**
- **What exactly was promised?** (Exact quotes with date)
- **What was the context?** (Market conditions, company situation at time)
- **What actually happened?** (Outcomes with dates)
- **How did management explain it?** (Excuses vs. accountability)
- **What was the pattern?** (First time or recurring?)
- **What are the implications?** (Can we trust future statements?)

**If no significant issues exist:** Include the section header with: "No issues warranting deep dive. Management scored >=0 on all promises with no concerning patterns identified."

**Do NOT omit this section.** Even "clean" audits need to explicitly state no issues were found.

### Step 8: Capital Allocation Track Record

Specific focus on how management has allocated capital. This is often the highest-stakes test of credibility.

#### M&A Synergy Tracking (Critical)

For each acquisition during the audit period, track promises with timelines:

| Acquisition | Date | Price Paid | Synergy Promise | Timeline | Actual Result | Score |
|-------------|------|------------|-----------------|----------|---------------|-------|
| [Target] | YYYY | $XB | "$Xm cost synergies" | "By Year 3" | $Xm achieved / written down | +2 to -2 |

**What to track for each deal:**
- **Cost synergies** — Were specific dollar amounts promised? Achieved?
- **Revenue synergies** — Often promised, rarely delivered. Track separately.
- **Integration timeline** — "Fully integrated by end of Year 2" — did it happen?
- **Accretion promises** — "Accretive in Year 1" — was it?
- **Write-downs** — Any goodwill impairments later? This is a -2.
- **Strategic rationale** — Did the stated strategy play out?

**M&A credibility scoring:**
- +2: Exceeded synergy targets, deal clearly value-creating
- +1: Met synergy targets on timeline
- 0: Partial synergies with reasonable explanation
- -1: Missed targets, excuses made, deal quietly underperforms
- -2: Goodwill write-down, deal never mentioned again, obvious failure

#### Buyback Timing Analysis (Critical)

Buybacks reveal both capital allocation skill and potential self-dealing.

| Year | $ Spent on Buybacks | Avg Price Paid | Stock Price Range (Year) | Intrinsic Value Est. | Score |
|------|---------------------|----------------|--------------------------|---------------------|-------|
| 20XX | $XB | $XX | $XX - $XX | $XX | +1/-1 |

**What to assess:**
- **Bought low or high?** — Did they buy more when stock was cheap, less when expensive?
- **Intrinsic value discipline** — Did they only buy below fair value, or buy regardless?
- **Consistency vs. opportunism** — Steady program or panic buying to prop up stock?
- **Insider selling overlap** — Were executives selling while company was buying? (Major red flag)
- **Debt-funded buybacks** — Did they lever up to buy back stock at highs?

**Buyback credibility scoring:**
- +2: Consistently bought below intrinsic value, accelerated during sell-offs
- +1: Generally bought at reasonable prices, showed discipline
- 0: Mechanical program, no apparent value awareness
- -1: Bought heavily at peak prices, poor timing
- -2: Bought at highs while insiders sold, or debt-funded buybacks before stock decline

#### Other Capital Allocation

| Decision | Stated Rationale | Outcome | Score |
|----------|------------------|---------|-------|
| Dividend increase | "Confidence in cash flow" | Sustainable or cut later? | +1/-1 |
| Major capex project | "ROI of X% expected" | Actual returns vs. cost of capital | +1/-1 |
| Divestiture | "Non-core, proceeds to X" | Price achieved, use of proceeds | +1/-1 |

### Step 9: Insider Ownership & Compensation Analysis

Management alignment through ownership and compensation structure is a critical credibility signal.

**REQUIRED OUTPUT:** This section MUST produce:
1. Executive Ownership table (CEO, CFO, and other key executives)
2. Recent Insider Transactions table
3. Compensation Structure table with percentage breakdown
4. CEO total compensation figure
5. Compensation vs. performance comparison
6. Overall Alignment Score table

**Executive Transitions:** If the CEO, CFO, or other key executives changed during the audit period, note this explicitly in BOTH locations:

1. **In the Executive Ownership table header:** Add a note immediately after the table:
   ```
   *Note: [Executive] transition [announced/completed] [date] — [Name] succeeded by [Name] as [Title] effective [date].*
   ```

2. **In promise accountability context:** How does this affect promise tracking?
   - Promises made under prior executive
   - Pattern differences between leaders
   - Continuity or discontinuity in guidance style

#### 9a: Insider Ownership

Use current web research to find current insider ownership data. Search for:
- "[Company] insider ownership percentage CEO"
- "[Company] proxy statement executive ownership"
- "[Company] DEF 14A [current year]" (proxy statement)

**REQUIRED: Executive Ownership Table (minimum 3 executives):**

The table MUST include:
1. **CEO** (always required)
2. **CFO** (always required)
3. **At least one additional executive** from:
   - Segment/division presidents who speak on earnings calls
   - COO or other C-suite members who make forward-looking statements
   - Founder or controlling shareholders if different from CEO

**How to identify key executives:** Scan the earnings transcripts for executives other than CEO/CFO who:
- Present during prepared remarks
- Answer analyst questions
- Are quoted making commitments in the Promise-by-Promise tables

If an executive is mentioned prominently in transcripts but ownership data is unavailable in the proxy, include them with "Data not available in proxy — [reason]" rather than omitting them entirely.

**Minimum count:** If only CEO and CFO ownership data is available after searching the proxy, note: "Additional executive ownership data not separately disclosed in proxy statement."

**Table structure:**

| Executive | Title | Base Salary | Shares Owned | Value (approx) | % of Company | Multiple of Salary |
|-----------|-------|-------------|--------------|----------------|--------------|-------------------|
| [Name] | CEO | $X.XM | X,XXX,XXX | $XXM | X.X% | XXx |
| [Name] | CFO | $X.XM | X,XXX,XXX | $XXM | X.X% | XXx |
| [Name] | COO/Other | $X.XM | X,XXX,XXX | $XXM | X.X% | XXx |

**REQUIRED:** Base salary must be included for each executive to verify the "Multiple of Salary" calculation. Source from proxy statement.

**REQUIRED: Source citation with page number.** Cite the proxy statement with specific page reference:
- Format: `*Source: FY20XX Proxy Statement (DEF 14A), pages XX-XX*`
- Example: `*Source: FY2024 Proxy Statement (DEF 14A), pages 42-45*`
- **DO NOT cite aggregator sites (TipRanks, GuruFocus, etc.) as sources.** These are discovery tools only.
- **YOU MUST access the actual proxy document** and cite the specific page where ownership data appears.
- For Canadian companies (foreign private issuers), use the Management Information Circular or 40-F filing.

**How to find page numbers:**
1. Search SEC EDGAR: `web search query: "[Company] DEF 14A [year] site:sec.gov"`
2. The proxy table of contents typically lists: "Security Ownership of Certain Beneficial Owners and Management" (ownership data) and "Executive Compensation" (compensation data)
3. Common sections: Stock Ownership Table (pages 50-55 typical), Named Executive Officer Compensation (pages 35-50 typical)

**If page number is unavailable:**
- First, search for the proxy on SEC EDGAR using: `web search query: "[Company] DEF 14A [year] site:sec.gov"`
- If PDF is inaccessible, use format: `*Source: FY20XX Proxy Statement (DEF 14A) — page reference unavailable due to PDF access; verify via EDGAR*`
- **This is acceptable but noted as a data limitation** — the validation checklist will flag it

**Assessment statement required:** "[Strong alignment / Moderate / Minimal skin in the game]"

**Assessment criteria:**
- CEO ownership >1% of company = Strong alignment signal
- CEO ownership >$50M = "Skin in the game"
- Founders with large stakes = Generally positive
- All executives with minimal ownership = Concerning

#### 9b: Recent Insider Transactions

Search for insider buying/selling patterns:

```
web search query: "[Company] insider transactions 2024 2025"
web search query: "[Company] Form 4 filings CEO"
```

**Document:**

| Date | Executive | Transaction | Shares | Price | Value | Context |
|------|-----------|-------------|--------|-------|-------|---------|
| 2024-XX | CEO | Buy/Sell | XX,XXX | $XXX | $X.XM | [Planned 10b5-1 / Open market / Options exercise] |

**Red flags to watch:**
- Heavy selling during buyback programs (company buys while insiders sell)
- Cluster selling before bad news
- Executives never buying, only selling
- 10b5-1 plan modifications before stock moves

**Positive signals:**
- Open market purchases (especially during selloffs)
- Executives holding through vesting (not immediately selling)
- Buying after stock declines

#### 9c: Compensation Structure Analysis

Review proxy statement for compensation structure:

```
web search query: "[Company] executive compensation proxy [current year]"
web search query: "[Company] CEO pay structure bonus metrics"
web search query: "[Company] DEF 14A compensation discussion"
```

**REQUIRED: Compensation Structure Table:**

| Component | % of CEO Total Comp | Metrics/Vesting |
|-----------|---------------------|-----------------|
| Base Salary | X% | Fixed |
| Annual Bonus | X% | [Metrics: Revenue, EPS, etc.] |
| Long-term Incentive | X% | [Metrics: TSR, ROIC, etc.], [X-year vesting] |
| Stock Awards | X% | [Time-based / Performance-based], [X-year vesting] |

**REQUIRED: CEO total compensation (most recent year):** $XX.XM

**REQUIRED: Compensation vs. Performance Comparison:**
- CEO pay growth over audit period: X%
- Stock price growth over same period: X%
- EPS growth over same period: X%

**REQUIRED: Alignment Assessment Statements:**
- Are incentives tied to long-term value creation? [Yes/Partially/No]
- Are metrics easy to manipulate (adjusted EPS) or harder (ROIC, FCF)? [Harder/Mixed/Easier]
- Is there meaningful equity ownership requirement? [Yes/No]

*Positive alignment signals:*
- Performance metrics tied to ROIC, FCF, or intrinsic value drivers
- Long vesting periods (3-5 years)
- Clawback provisions
- Stock ownership requirements
- Significant portion in equity vs. cash

*Concerning signals:*
- Bonuses tied primarily to revenue (easy to game)
- Adjusted EPS as primary metric (can be manipulated)
- Short vesting periods
- Large guaranteed bonuses
- Excessive perks
- Compensation growing faster than shareholder returns

**REQUIRED: Overall Alignment Score Table:**

| Factor | Assessment | Score |
|--------|------------|-------|
| Insider ownership level | [High/Moderate/Low] | +1/0/-1 |
| Recent transaction pattern | [Net buyer/Neutral/Net seller] | +1/0/-1 |
| Compensation structure | [Aligned/Mixed/Misaligned] | +1/0/-1 |
| Pay vs. performance | [Reasonable/Stretched/Excessive] | +1/0/-1 |
| **Overall Alignment** | | **+X** |

### Step 10: Red Flag Assessment

Compile all red flags identified during the audit:

**Financial Red Flags:**
- Earnings quality concerns (GAAP vs. adjusted divergence)
- Receivables or inventory growing faster than sales
- Frequent restructuring charges
- Acquisition write-downs
- Pension underfunding

**Non-GAAP Definition Drift (Critical):**

This is one of the most important credibility signals. Compare adjusted metrics definitions from Year 1 to Year 5:

| Metric | Year 1 Adjustments | Year 5 Adjustments | Drift? |
|--------|-------------------|-------------------|--------|
| Adjusted EPS | [List items excluded] | [List items excluded] | Y/N |
| Adjusted EBITDA | [List items excluded] | [List items excluded] | Y/N |
| Free Cash Flow | [Definition used] | [Definition used] | Y/N |

**Red flags for Non-GAAP drift:**
- Number of adjustment categories increasing over time
- "One-time" items that appear multiple years
- Stock-based comp excluded when it wasn't before
- Restructuring costs becoming permanent adjustments
- Gap between GAAP and non-GAAP *widening* as a % of earnings
- New "adjusted" metrics introduced when old ones look bad

**Communication Red Flags:**
- Changing adjusted metrics definitions (see Non-GAAP drift above)
- Opaque segment reporting
- Avoiding analyst questions
- CFO turnover
- Auditor changes

**Governance Red Flags:**
- Excessive executive compensation
- Related party transactions
- Board independence issues
- Shareholder unfriendly actions

### Step 11: Write Analysis

Follow the Analysis output template structure exactly. Verify ALL 15 required sections are present:

| # | Section | Required Elements |
|---|---------|-------------------|
| 1 | **Data Sources** | Table with source type, count, date range, coverage |
| 2 | **Executive Summary** | Rating, composite score, 3-5 paragraphs |
| 3 | **Quantitative Scorecard** | 3 tables: Promise Delivery Summary, Trend Over Time, Guidance Accuracy |
| 4 | **Say/Do Matrix Placement** | ASCII diagram, quadrant name, rationale, investment implication |
| 5 | **Key Management Quotes** | 5-10 verbatim quotes with attribution |
| 6 | **Missed & Partial Promises** | Table of ALL scores <=0, analysis paragraph |
| 7 | **Promise-by-Promise Detail** | 5 category tables: Financial, Capital Allocation, Operational, Cost/Efficiency, Strategic |
| 8 | **Pattern Analysis** | Positive patterns, concerning patterns, kitchen sink quarters |
| 9 | **Capital Allocation Track Record** | M&A synergies table, buyback timing table, other decisions |
| 10 | **Insider Ownership & Compensation** | Ownership table (CEO+CFO minimum), transactions, comp structure, alignment score |
| 11 | **Non-GAAP Definition Drift** | Year 1 vs Year 5 comparison table, gap trend |
| 12 | **Red Flags Identified** | Table with severity ratings, summary statement |
| 13 | **Deep Dive: Key Issues** | Detailed analysis OR "No issues warranting deep dive" |
| 14 | **Conclusion and Investment Implications** | Rating with criteria, guidance discount %, monitoring points |
| 15 | **Appendix: Source Documents** | Table listing ALL transcripts (quarter, date, source) |

**IMPORTANT:** If a section has no content (e.g., no red flags), still include the section with explicit "None identified" statement. Never omit a required section.

Write Analysis to: `[ANALYSIS_PATH]`

### Step 12: Write Memo

After completing the Analysis, read the memo template and synthesize key findings.

The Memo distills the Analysis into actionable takeaways for investment decision-making.

**CRITICAL: Required Memo Sections Checklist (ALL 7 must be present)**

| # | Section | Required Elements |
|---|---------|-------------------|
| 1 | **Header** | Rating, Matrix Placement, Audit Period, Quarters Reviewed |
| 2 | **Key Takeaways** | 5-7 bullets with line breaks between |
| 3 | **What You Can Trust** | TABLE format: Guidance Type, Track Record, Confidence |
| 4 | **What to Discount** | TABLE format: Guidance Type, Issue, Recommended Discount |
| 5 | **Red Flags to Monitor** | CHECKLIST format (- [ ] items) |
| 6 | **Bottom Line** | 2-4 sentences, final verdict |
| 7 | **Quick Reference** | TABLE with ALL 5 metrics below |

**REQUIRED: Quick Reference Table (all 5 metrics):**

| Metric | Value |
|--------|-------|
| Promise Hit Rate | [X]% |
| Composite Score | [+X.X] (-2 to +2 scale) |
| Guidance Style | [Conservative / Accurate / Optimistic] |
| Capital Allocation | [Excellent / Good / Mixed / Poor] |
| Insider Alignment | [Strong / Moderate / Weak] |

**CRITICAL: Maintain consistency between documents.** The Memo must accurately reflect the Analysis findings:
- If Analysis identifies something as a "red flag," Memo must not claim it's "completed" or "resolved" unless the Analysis says so
- Say/Do Matrix placement wording must be identical in both documents
- Ratings (HIGH/MODERATE/LOW) must match exactly
- Key metrics (hit rate, composite score) must be identical

Write Memo to: `[MEMO_PATH]`

### Step 13: Final Validation

Before returning, complete the validation checklist:

**Be Thorough:** This is meant to be comprehensive. Don't rush through transcripts.

**Use Exact Quotes:** When documenting promises, use management's actual words.

**Context Matters:** Consider market conditions and company circumstances when scoring.

**Fair but Rigorous:** Give credit where due, but don't make excuses for management.

**Actionable Output:** The audit should help the user decide whether to trust this management team.

**Data Transparency:** Always clearly document what data was available and what gaps exist. An audit with incomplete data can still be valuable if limitations are clearly stated.

---

## Tool Usage

- **Read:** Use for reading templates, transcript files, and checklist
- **Write:** Use for saving the Analysis and Memo outputs
- **Web search:** Use for insider ownership, compensation, proxy data, and missing transcripts
- **Bash:** Use for running fmp-fetch.sh and date commands
- **File search pattern:** Use for finding research files

---

## Return Value

When complete, return a JSON object:
```json
{
  "analysis_path": "[path to Analysis file]",
  "memo_path": "[path to Memo file]",
  "transcripts_fetched": [number of transcripts retrieved],
  "transcript_range": "YYYY-QX to YYYY-QX",
  "status": "success" | "partial" | "failed",
  "notes": "[any issues encountered]"
}
```

The `analysis_path` and `memo_path` are CRITICAL — Phase 2 QC will use these to review both documents.
The `transcript_range` is used by Phase 2 to re-fetch transcripts for verification.
```
