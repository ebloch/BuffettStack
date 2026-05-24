# Phase 1: Scuttlebutt Synthesis Prompt

Use this prompt for the synthesis pass of the scuttlebutt workflow.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are conducting a Philip Fisher-style scuttlebutt analysis for [COMPANY] ([TICKER]).

This answers the question: **What do the people who interact with this company actually think? What's the word on the street?**

This skill goes beyond management presentations and investor materials to understand how customers, employees, partners, and competitors actually perceive the company. It's the qualitative "ground truth" that can validate or contradict official narratives.

**Source Documents:**
- 10K Synthesis Memos: [10K_MEMO_PATHS]

**Output Paths:**
- Analysis: [ANALYSIS_OUTPUT_PATH]
- Memo: [MEMO_OUTPUT_PATH]

**Timestamp:** [TIMESTAMP]

---

## Your Task

Complete the full scuttlebutt analysis workflow:

### Step 1: Read 10K Source Material

Read ALL 10K synthesis memos provided. Use to understand:
- Business model and customer segments
- Management's stated competitive advantages
- Key risk factors
- Revenue sources and geographic mix

This context informs which stakeholder groups to prioritize and what claims to validate. More years = better context for historical patterns and trend validation.

### Step 2: Read Templates

Read required templates:
- Analysis template: `.codex/skills/scuttlebutt/references/output-template-analysis.md`
- Memo template: `.codex/skills/scuttlebutt/references/output-template-memo.md`
- Validation checklist: `.codex/skills/scuttlebutt/references/validation-checklist.md`

### Step 3: Systematically Search Each Stakeholder Category

Search all 6 stakeholder categories using web search. For each category, follow the detailed instructions below.

---

## Analysis Framework (6 Stakeholder Categories)

### 1. Customer Voice

**Goal:** Understand what customers actually experience, not what the company claims.

**Sources to Search:**

| Source Type | Examples | Search Queries |
|-------------|----------|----------------|
| Product Reviews | G2, Capterra, TrustPilot, App Store, Google Play | "[Company] reviews", "[Product] reviews G2" |
| Consumer Reviews | Amazon, BBB, Consumer Affairs | "[Company] BBB complaints", "[Product] Amazon reviews" |
| Discussion Forums | Reddit, Hacker News, industry-specific forums | "site:reddit.com [Company]", "[Company] hacker news" |
| Social Media | Twitter/X, LinkedIn | "[Company] customer complaints", "[Company] customer experience" |
| Industry-specific sources | J.D. Power, CFTC complaints, FIA, trade associations | "[Company] [industry] reviews", "[Company] customer satisfaction" |

**B2B Company Note:** For B2B infrastructure companies (exchanges, enterprise software, industrial suppliers), traditional consumer review platforms (G2, Capterra, App Store) may not apply. In these cases:
1. Search for industry-specific review sources (e.g., Gartner Peer Insights for enterprise tech, J.D. Power for financial services)
2. Look for institutional customer feedback in trade publications, regulatory filings, or industry forums
3. Note "N/A - B2B model" for inapplicable consumer platforms rather than forcing a search
4. Weight professional/institutional sources more heavily than scattered retail complaints

**What to Extract:**

- **Overall Rating Trends:** Are scores improving, stable, or declining?
- **Common Praise:** What do customers consistently love?
- **Common Complaints:** What recurring issues appear?
- **Switching Intent:** Do customers mention switching to competitors? Why?
- **Customer Support Quality:** How do customers rate support interactions?
- **Value Perception:** Do customers feel they get good value?

**Red Flags to Watch:**
- Sudden rating drops
- Recurring complaints about core product quality
- "Used to love them, but now..."
- Complaints about pricing without corresponding value
- Long-standing bugs or issues that never get fixed

### 2. Employee Voice

**Goal:** Understand company culture, management quality, and operational health from inside.

**Sources to Search:**

| Source Type | Search Queries |
|-------------|----------------|
| Glassdoor | "[Company] Glassdoor reviews", "[Company] Glassdoor CEO approval" |
| Blind | "site:teamblind.com [Company]", "[Company] Blind reviews ratings" |
| LinkedIn | "[Company] LinkedIn employee count", "[Company] hiring" |
| Indeed | "[Company] Indeed reviews" |
| Comparably | "[Company] Comparably ratings" |

**What to Extract:**

| Metric | What to Find |
|--------|--------------|
| Overall Glassdoor Rating | X.X out of 5, trend over time |
| CEO Approval | X% (exact figure from Glassdoor, not estimated) |
| Recommend to Friend | X% |
| Business Outlook | Positive/Neutral/Negative % |
| Culture Scores | Work-life balance, compensation, management, etc. |

**CEO Approval Sourcing (CRITICAL):**
1. **First search:** "[Company] Glassdoor CEO approval" — Look for the company-wide CEO approval percentage prominently displayed on the Glassdoor company page (typically 60-90% for well-run companies)
2. **Verify you have company-wide data:** CEO approval should be based on ALL employee reviews, not filtered by job title or seniority level. If you only find approval for specific roles (e.g., "Senior Directors"), keep searching for the main company figure.
3. **Cross-reference with Comparably:** Search "[Company] Comparably CEO score" for additional validation. Comparably often shows CEO approval and culture scores.
4. **If Glassdoor doesn't display company-wide CEO approval:** Glassdoor has reduced visibility of some metrics. If company-wide CEO approval is not available after thorough searching:
   - Use Comparably CEO score as the primary metric (e.g., "CEO Score: 70/100 via Comparably")
   - Note "Glassdoor CEO approval: Not publicly displayed" in the limitations section
   - Do NOT estimate or fabricate a Glassdoor percentage
5. **If no CEO approval data found anywhere:** Note "CEO approval: Data not available" — never present role-filtered data as if it were company-wide.

**Comparably Data (if available):**
Comparably provides culture scores and CEO ratings that often differ from Glassdoor. Search for:
- Overall culture score (X/100)
- CEO score (X/100)
- Diversity score
- Gender score
If found, include in Employee Voice section alongside Glassdoor data. If not found, note "Comparably: Not available."

*Note: Comparably typically does not publish historical trend data publicly. If trend is unavailable, note "Trend: Not available" rather than estimating.*

**Indeed Data (if available):**
Indeed provides employee reviews with structured metrics. Search for:
- Overall rating (X.X/5)
- Work wellbeing score (out of 100)
- Dimension scores: Work-Life Balance, Pay & Benefits, Job Security, Management, Culture
- Number of reviews
If found, include in Employee Voice alongside Glassdoor data. If not found, note "Indeed: Not available."

*Note: Indeed is particularly useful for companies with fewer Glassdoor reviews, as it often has broader coverage.*

**Blind Data (if available):**
Blind provides anonymous employee feedback that often differs from Glassdoor. If the company has a Blind presence, capture:
- Overall rating (X.X/5)
- Dimension scores (work-life balance, compensation, culture, career growth)
- Notable themes from discussions (often more candid than Glassdoor)
- If Blind data is not found, note "Blind: Not available" in the Employee Voice section

*Note: Blind typically does not publish historical scores. Focus on current ratings and themes; note sample size if available.*

**Qualitative Themes:**
- What do employees praise about working there?
- What are the most common complaints?
- How do employees describe management and leadership?
- Are there concerns about company direction?
- Engineering/product team sentiment (for tech companies)

**Red Flags to Watch:**
- CEO approval below 60%
- "Business outlook" declining
- Recurring complaints about layoffs, cost-cutting, or instability
- Executive turnover mentions
- "Great company, but..." patterns
- Culture complaints that touch core values

### 3. Partner/Supplier Voice

**Goal:** Understand how business partners and suppliers perceive the company.

**Sources to Search:**

| Source Type | Search Queries |
|-------------|----------------|
| Partner Programs | "[Company] partner program reviews", "[Company] reseller experience" |
| Supplier News | "[Company] supplier relations", "[Company] payment terms" |
| Developer Community | "[Company] API reviews", "[Company] developer experience" (for tech) |
| Channel Partners | "[Company] distributor", "[Company] partner satisfaction" |

**What to Extract:**

- **Partner Program Quality:** How do partners rate the program?
- **Payment Practices:** Any news about payment disputes or extended terms?
- **Supplier Concentration:** Are suppliers dependent on this company?
- **Developer Sentiment:** (For tech) How do developers feel about working with the platform/API?
- **Channel Satisfaction:** Are distributors/resellers happy?

**Red Flags to Watch:**
- Payment disputes with suppliers
- Partners complaining about margin squeeze
- Developer community exodus
- Major partner defections

### 4. Competitor Voice

**Goal:** Understand how competitors position against and perceive the company.

**Sources to Search:**

| Source Type | Search Queries |
|-------------|----------------|
| Win/Loss Analysis | "[Company] vs [Competitor]", "[Competitor] vs [Company] comparison" |
| Competitor Positioning | "[Competitor] why choose us over [Company]" |
| Industry Analyst Reports | "[Company] Gartner", "[Company] Forrester", "[Company] IDC" |
| Comparison Sites | "[Company] alternatives", "[Company] vs competitors" |

**What to Extract:**

- **Competitor Claims:** What do competitors say they do better?
- **Win/Loss Signals:** What reasons do customers cite for choosing/leaving?
- **Analyst Positioning:** Where does the company sit in analyst quadrants?
- **Market Perception:** Is the company seen as leader, challenger, or laggard?

**Investment Insight:** When competitors consistently avoid competing on certain dimensions, that signals a real advantage. When competitors directly attack a claimed strength, that may signal vulnerability.

### 5. Industry Expert Voice

**Goal:** Understand how industry analysts and experts view the company.

**Sources to Search:**

| Source Type | Search Queries |
|-------------|----------------|
| Analyst Commentary | "[Company] analyst ratings", "[Company] industry analysis" |
| Trade Publications | "[Company] [industry] publication", "[Company] industry news" |
| Conference Presentations | "[Company] conference presentation", "[Company] industry keynote" |
| Expert Interviews | "[Company] CEO interview", "[Company] executive interview" |

**What to Extract:**

- **Analyst Sentiment:** Bullish, bearish, or neutral consensus?
- **Industry Position:** How do experts rank the company?
- **Trend Commentary:** What do experts say about the company's trajectory?
- **Specific Concerns:** Any expert-flagged risks or issues?

### 6. Social/Media Sentiment

**Goal:** Gauge broader public perception and identify sentiment shifts.

**Sources to Search:**

| Source Type | Search Queries |
|-------------|----------------|
| News Sentiment | "[Company] news", "[Company] recent news" |
| Social Media | "[Company] Twitter", "[Company] sentiment" |
| Short Interest | "[Company] short interest", "[Company] short sellers" |
| Activist Activity | "[Company] activist investor", "[Company] Elliott/Icahn/etc." |

**What to Extract:**

- **News Tone:** Generally positive, neutral, or negative recent coverage?
- **Social Sentiment:** How does the public perceive the brand?
- **Short Interest:** Is short interest elevated? Rising or falling?
- **Activist Signals:** Any activist involvement or campaigns?

**Short Interest Data Sourcing:**
Search "[Ticker] short interest" on Finviz, Yahoo Finance, MarketWatch, or Nasdaq. Look for:
- Short interest as % of float (the key metric — report as "X.X% of float")
- Days to cover (shares short / average daily volume)
- Trend vs. prior month (rising/stable/falling)
If data is unavailable, note "Short Interest: Data not found" rather than "Low (est.)"

**Investment Insight:** Elevated or rising short interest combined with negative grassroots signals may indicate sophisticated investors see problems not yet reflected in financials.

---

## Scuttlebutt Health Score

After gathering evidence from all stakeholders, synthesize into a health score.

**Scoring by Stakeholder:**

| Stakeholder | Weight | Score (1-5) | Weighted Score |
|-------------|--------|-------------|----------------|
| Customers | 30% | X.X | X.XX |
| Employees | 25% | X.X | X.XX |
| Partners | 15% | X.X | X.XX |
| Competitors | 10% | X.X | X.XX |
| Industry Experts | 10% | X.X | X.XX |
| Media/Social | 10% | X.X | X.XX |
| **Overall** | **100%** | | **X.XX** |

**Scoring Guidelines:**

| Score | Definition |
|-------|------------|
| **5** | Exceptional — Consistently positive sentiment, no concerning patterns |
| **4** | Strong — Mostly positive with minor concerns |
| **3** | Mixed — Balanced positive and negative signals |
| **2** | Concerning — More negative than positive, clear issues |
| **1** | Poor — Pervasive negative sentiment, serious problems |

**Health Score Interpretation:**

| Score Range | Interpretation |
|-------------|----------------|
| **4.0+** | Strong grassroots support — moat likely reinforced by stakeholder loyalty |
| **3.0-3.9** | Mixed signals — investigate specific concerns before investing |
| **2.0-2.9** | Concerning patterns — moat may be eroding, proceed with caution |
| **<2.0** | Red flags across stakeholders — serious concerns, avoid or exit |

---

## Moat Implications

After completing stakeholder analysis, connect findings to moat durability:

**Customer Signals -> Moat Validation:**
- High satisfaction + low switching intent = moat validated
- Complaints about core product = moat potentially eroding
- Price sensitivity increasing = pricing power at risk

**Employee Signals -> Operational Health:**
- Strong culture scores = talent advantage sustainable
- Executive turnover = potential strategic drift
- Cost-cutting complaints = margin pressure, possible quality decline

**Partner Signals -> Ecosystem Strength:**
- Happy partners = ecosystem moat reinforced
- Partner complaints = ecosystem may be extractive, not symbiotic

**Competitor Signals -> Competitive Position:**
- Competitors avoid direct competition = strong moat
- Competitors directly attacking = moat potentially vulnerable

---

## Step 4: Generate Analysis Document

Read the analysis template and follow its structure:

```
Read .codex/skills/scuttlebutt/references/output-template-analysis.md
```

The Analysis template includes all required sections with formatting guidance.

## Step 5: Generate Memo Document

After completing the Analysis, read the memo template and synthesize key findings:

```
Read .codex/skills/scuttlebutt/references/output-template-memo.md
```

The Memo distills the Analysis into actionable takeaways.

**Process:** Complete the full Analysis first, then synthesize the Memo from the Analysis.

---

## Step 6: Validation (REQUIRED)

**Do NOT finish until validation passes.**

After completing both outputs, read and run through the validation checklist:

```
.codex/skills/scuttlebutt/references/validation-checklist.md
```

The checklist has 7 passes:
- **Pass A:** Stakeholder completeness (all 6 categories)
- **Pass B:** Evidence quality (quotes, sources, sample sizes)
- **Pass C:** Scoring accuracy (weights, calculation)
- **Pass D:** Red flags & moat implications
- **Pass E:** Investment relevance (actionable conclusions)
- **Pass F:** Output structure (both documents)
- **Pass G:** Data integrity (no fabrication, limitations disclosed)

**If any pass fails:** Fix the issue before finishing. Common fixes:
- Missing stakeholder -> Search again or note "no data found"
- No quotes -> Add representative quotes with sources
- Score math wrong -> Recalculate weighted average
- Missing red flag severity -> Add High/Medium/Low rating

**Score consistency check:** The calculated weighted score MUST appear identically in: (a) Analysis Executive Summary, (b) Analysis Scorecard table, and (c) Memo header. Do not manually enter the score; copy the calculated value to all three locations.

---

## Additional Guidelines

**Be Comprehensive:** Search multiple sources for each stakeholder. Don't rely on a single review site.

**Capture Direct Quotes:** When possible, include actual quotes from reviews or discussions to provide evidence.

**Note Recency:** Pay attention to when reviews/comments were written. Recent sentiment matters more than old sentiment.

**Watch for Trends:** A company with 4.2 rating that was 4.5 last year is different from one that was 3.8 last year.

**Balance Positives and Negatives:** Don't just hunt for problems. Capture what stakeholders genuinely appreciate.

**Connect to Investment Thesis:** The goal is to validate or challenge the investment thesis, not just gather information.

**Cross-Reference:** When multiple stakeholder groups mention the same issue, it's likely real and significant.

**Be Skeptical of Extremes:** Very positive or very negative reviews may be planted. Look for detailed, balanced feedback.

**Distinguish Estimates from Hard Data:** When citing metrics that aren't publicly disclosed (e.g., churn rates, internal satisfaction scores), clearly label them as estimates with "(est.)" or "(inferred)" and note the source of the inference. Don't present estimates with the same confidence as confirmed data. Apply "(est.)" labels consistently throughout both documents — if a threshold or average is estimated, mark it every time it appears, not just once.

**Customer Review Avg for Quick Reference:** The Memo's Quick Reference requires a "Customer Review Avg" field. Calculate this by averaging ratings from customer review platforms (e.g., Trustpilot, App Store, Google Play). ACSI is NOT a customer review average — it's a separate survey metric. If review platforms show divergent ratings (e.g., 4.8 app store vs. 1.7 web reviews), present both with context rather than a misleading average. For B2B companies without consumer reviews, note "N/A - B2B model."

**Monitoring Thresholds Must Be Actionable:** Every metric in the Monitoring Dashboard must have a specific numeric warning threshold. If exact data isn't available, provide an estimated threshold based on industry norms or analyst commentary (e.g., "Below 3.5 (estimated based on industry avg)"). Never use vague thresholds like "declining" or "threshold unknown."

**Clarify What Different Metrics Measure:** Customer service scores measure support interactions; overall ratings measure product experience; NPS measures recommendation intent. Don't conflate different metric types when drawing conclusions. Note when different sources measure different things.

---

## Tool Usage

- **Read:** Use for reading 10K memos, template files, and checklists
- **Write:** Use for saving both output documents
- **Web search:** Use for all stakeholder category research
- **WebFetch:** Use for reading specific review sites, forums, articles
- **File search pattern:** Use for finding research files if needed

---

## Return Value

When complete, return a JSON object:
```json
{
  "analysis_path": "[path to written analysis]",
  "memo_path": "[path to written memo]",
  "source_memos": ["[path/to/10k-memo1.md]", "[path/to/10k-memo2.md]"],
  "status": "success" | "partial" | "failed",
  "notes": "[any issues encountered]"
}
```

Both paths are CRITICAL — Phase 2 QC and Phase 3 Audit will use these to evaluate the output.
```
