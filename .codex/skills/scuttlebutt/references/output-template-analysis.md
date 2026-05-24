# Scuttlebutt Analysis Output Template

Use this structure when writing the analysis document.

---

```markdown
---
formal_qc_run: false
formal_audit_run: false
qc_status: pending
audit_status: blocked_until_qc_complete
qc_completed_at: null
audit_completed_at: null
qc_result: null
audit_result: null
---

# [Company] - Scuttlebutt Analysis

**Date:** [Analysis Date]
**Ticker:** [TICKER]
**Industry:** [Industry Name]

---

## Executive Summary

[3-4 paragraphs covering:]
- Overall scuttlebutt health assessment
- Key strengths from stakeholder perspectives
- Key concerns or red flags identified
- Moat implications — does grassroots sentiment validate or challenge the investment thesis?

**Scuttlebutt Health Score:** X.X / 5.0
**Assessment:** [Strong / Mixed / Concerning / Poor]

---

## Scuttlebutt Health Scorecard

| Stakeholder | Weight | Score | Weighted | Key Signal |
|-------------|--------|-------|----------|------------|
| Customers | 30% | X.X | X.XX | [One-line summary] |
| Employees | 25% | X.X | X.XX | [One-line summary] |
| Partners | 15% | X.X | X.XX | [One-line summary] |
| Competitors | 10% | X.X | X.XX | [One-line summary] |
| Industry Experts | 10% | X.X | X.XX | [One-line summary] |
| Media/Social | 10% | X.X | X.XX | [One-line summary] |
| **Overall** | **100%** | | **X.XX** | |

**Score Interpretation:**
- 4.0+: Strong grassroots support
- 3.0-3.9: Mixed signals, investigate concerns
- 2.0-2.9: Concerning patterns
- <2.0: Red flags across stakeholders

---

## 1. Customer Voice

### Overview

**Score:** X.X / 5.0
**Trend:** Improving / Stable / Declining
**Sample Size:** ~X reviews/data points across Y sources

### Quantitative Metrics

| Source | Rating | Sample Size | Trend | Notes |
|--------|--------|-------------|-------|-------|
| G2 | X.X/5 | X reviews | ↑/→/↓ | [Notable observation] |
| Capterra | X.X/5 | X reviews | ↑/→/↓ | |
| TrustPilot | X.X/5 | X reviews | ↑/→/↓ | |
| App Store | X.X/5 | X reviews | ↑/→/↓ | |
| Google Play | X.X/5 | X reviews | ↑/→/↓ | |
| Amazon | X.X/5 | X reviews | ↑/→/↓ | |
| BBB | X/5 or Grade | X complaints | ↑/→/↓ | |

### What Customers Love

| Theme | Frequency | Representative Quote |
|-------|-----------|---------------------|
| [Theme 1] | Common/Frequent/Occasional | "[Actual quote from review]" |
| [Theme 2] | Common/Frequent/Occasional | "[Actual quote from review]" |
| [Theme 3] | Common/Frequent/Occasional | "[Actual quote from review]" |

### What Customers Complain About

| Theme | Frequency | Severity | Representative Quote |
|-------|-----------|----------|---------------------|
| [Complaint 1] | Common/Frequent/Occasional | High/Medium/Low | "[Actual quote]" |
| [Complaint 2] | Common/Frequent/Occasional | High/Medium/Low | "[Actual quote]" |
| [Complaint 3] | Common/Frequent/Occasional | High/Medium/Low | "[Actual quote]" |

### Switching Intent Signals

- **Mentions of switching to competitors:** [Frequency, which competitors mentioned]
- **Reasons cited for leaving:** [List main reasons]
- **Lock-in vs. loyalty:** [Are customers staying due to switching costs or genuine preference?]

### Customer Support Quality

- **Support ratings:** [If available]
- **Common support complaints:** [List]
- **Support praise:** [List]

### Customer Voice Summary

[2-3 paragraph synthesis of customer sentiment, noting the most important signals and any concerning patterns]

---

## 2. Employee Voice

### Overview

**Score:** X.X / 5.0
**Trend:** Improving / Stable / Declining
**Primary Source:** Glassdoor (X reviews)

### Glassdoor Metrics

| Metric | Current | 1 Year Ago | Trend |
|--------|---------|------------|-------|
| Overall Rating | X.X/5 | X.X/5 | ↑/→/↓ |
| CEO Approval | X% | X% | ↑/→/↓ |
| Recommend to Friend | X% | X% | ↑/→/↓ |
| Business Outlook | X% positive | X% positive | ↑/→/↓ |

### Culture Dimension Scores

| Dimension | Score | Industry Avg | Assessment |
|-----------|-------|--------------|------------|
| Work-Life Balance | X.X | X.X | Above/At/Below |
| Compensation & Benefits | X.X | X.X | Above/At/Below |
| Culture & Values | X.X | X.X | Above/At/Below |
| Career Opportunities | X.X | X.X | Above/At/Below |
| Senior Management | X.X | X.X | Above/At/Below |

### What Employees Praise

| Theme | Frequency | Representative Quote |
|-------|-----------|---------------------|
| [Theme 1] | Common/Frequent/Occasional | "[Actual quote from review]" |
| [Theme 2] | Common/Frequent/Occasional | "[Actual quote from review]" |
| [Theme 3] | Common/Frequent/Occasional | "[Actual quote from review]" |

### What Employees Complain About

| Theme | Frequency | Severity | Representative Quote |
|-------|-----------|----------|---------------------|
| [Complaint 1] | Common/Frequent/Occasional | High/Medium/Low | "[Actual quote]" |
| [Complaint 2] | Common/Frequent/Occasional | High/Medium/Low | "[Actual quote]" |
| [Complaint 3] | Common/Frequent/Occasional | High/Medium/Low | "[Actual quote]" |

### Leadership Sentiment

- **CEO perception:** [Summary of how employees view CEO]
- **Management quality:** [What employees say about management]
- **Executive turnover signals:** [Any mentions of leadership changes or concerns]

### Hiring and Retention Signals

- **LinkedIn employee count trend:** [Growing/Stable/Declining]
- **Hiring activity:** [Active/Moderate/Quiet]
- **Key departures:** [Any notable mentions]
- **Layoff mentions:** [Frequency and sentiment]

### Employee Voice Summary

[2-3 paragraph synthesis of employee sentiment, noting the most important signals and any concerning patterns]

---

## 3. Partner/Supplier Voice

### Overview

**Score:** X.X / 5.0
**Confidence:** High / Medium / Low
**Confidence Justification:** [1-sentence explanation of why this confidence level — e.g., "Medium: Based on partnership announcements and news reports; no direct partner survey data available" or "Low: Limited publicly available partner feedback for this company type"]

### Partner Program Sentiment

| Aspect | Assessment | Evidence |
|--------|------------|----------|
| Program quality | Strong/Adequate/Weak | [Source/evidence] |
| Partner profitability | High/Moderate/Low | [Source/evidence] |
| Support from company | Strong/Adequate/Weak | [Source/evidence] |
| Communication | Good/Mixed/Poor | [Source/evidence] |

### Supplier Relationship Signals

| Signal | Assessment | Evidence |
|--------|------------|----------|
| Payment practices | Good/Concerning/Unknown | [News, reports] |
| Supplier concentration | Diversified/Concentrated | [Analysis] |
| Bargaining dynamics | Balanced/Company-favored/Supplier-favored | [Evidence] |

### Developer Community Sentiment (if applicable)

| Aspect | Assessment | Evidence |
|--------|------------|----------|
| API quality | Strong/Adequate/Weak | [Developer reviews, forums] |
| Documentation | Good/Mixed/Poor | [Feedback sources] |
| Developer support | Responsive/Adequate/Poor | [Evidence] |
| Platform direction | Optimistic/Neutral/Concerned | [Community sentiment] |

### Partner/Supplier Voice Summary

[1-2 paragraph synthesis. Note if data was limited.]

---

## 4. Competitor Voice

### Overview

**Score:** X.X / 5.0
**Assessment:** [How competitors view and position against this company]

### Competitive Positioning Analysis

| Competitor | How They Position Against [Company] | What They Claim to Do Better |
|------------|-------------------------------------|------------------------------|
| [Competitor 1] | [Positioning strategy] | [Claimed advantages] |
| [Competitor 2] | [Positioning strategy] | [Claimed advantages] |
| [Competitor 3] | [Positioning strategy] | [Claimed advantages] |

### Win/Loss Intelligence

**Why Customers Choose [Company]:**
- [Reason 1] — Frequency: Common/Occasional
- [Reason 2] — Frequency: Common/Occasional

**Why Customers Choose Competitors:**
- [Reason 1] — Frequency: Common/Occasional
- [Reason 2] — Frequency: Common/Occasional

### Analyst Positioning

| Analyst Firm | Report/Quadrant | Position | Date |
|--------------|-----------------|----------|------|
| Gartner | [Magic Quadrant name] | [Leader/Challenger/etc.] | [Date] |
| Forrester | [Wave name] | [Position] | [Date] |
| IDC | [Report name] | [Position] | [Date] |

### Competitive Voice Summary

[1-2 paragraph synthesis of how competitors view the company and what this reveals about competitive dynamics]

---

## 5. Industry Expert Voice

### Overview

**Score:** X.X / 5.0
**Consensus:** Bullish / Neutral / Bearish

### Analyst Sentiment

| Perspective | Assessment | Source |
|-------------|------------|--------|
| Sell-side consensus | [Bullish/Neutral/Bearish] | [Rating distribution] |
| Buy-side mentions | [Sentiment if found] | [Sources] |
| Independent analysts | [Sentiment] | [Sources] |

### Trade Publication Coverage

| Publication | Recent Tone | Key Themes |
|-------------|-------------|------------|
| [Publication 1] | Positive/Neutral/Negative | [Main topics covered] |
| [Publication 2] | Positive/Neutral/Negative | [Main topics covered] |

### Expert Concerns

[List specific concerns raised by industry experts, with sources]

### Expert Praise

[List specific praise from industry experts, with sources]

### Industry Expert Summary

[1-2 paragraph synthesis of expert sentiment]

---

## 6. Social/Media Sentiment

### Overview

**Score:** X.X / 5.0
**Recent Trend:** Positive / Neutral / Negative

### News Sentiment

| Period | Tone | Key Stories |
|--------|------|-------------|
| Last 30 days | Positive/Neutral/Negative | [Major headlines] |
| Last 90 days | Positive/Neutral/Negative | [Trend summary] |

### Social Media Signals

| Platform | Sentiment | Notable Themes |
|----------|-----------|----------------|
| Twitter/X | Positive/Neutral/Negative | [Key themes] |
| LinkedIn | Positive/Neutral/Negative | [Key themes] |
| Reddit | Positive/Neutral/Negative | [Key themes, relevant subreddits] |

### Short Interest and Activist Signals

| Metric | Current | Trend | Implication |
|--------|---------|-------|-------------|
| Short Interest | X% of float | Rising/Stable/Falling | [Assessment] |
| Days to Cover | X days | | |
| Activist Activity | [None/Present] | | [Details if present] |

### Media/Social Summary

[1-2 paragraph synthesis]

---

## Pattern Analysis

### Cross-Stakeholder Themes

**Issues mentioned by multiple stakeholder groups:**

| Theme | Mentioned By | Significance |
|-------|--------------|--------------|
| [Theme 1] | Customers, Employees | [Assessment of importance] |
| [Theme 2] | Partners, Competitors | [Assessment of importance] |

### Positive Patterns

[Consistent strengths across stakeholder groups]

- **[Pattern 1]:** [Evidence from multiple stakeholders]
- **[Pattern 2]:** [Evidence from multiple stakeholders]

### Concerning Patterns

[Consistent weaknesses or warning signs across stakeholder groups]

- **[Pattern 1]:** [Evidence from multiple stakeholders]
- **[Pattern 2]:** [Evidence from multiple stakeholders]

### Sentiment Divergence

[Note any cases where stakeholder groups have divergent views — e.g., customers happy but employees unhappy]

---

## Red Flags Identified

| Red Flag | Severity | Stakeholder Source | Evidence | Moat Implication |
|----------|----------|-------------------|----------|------------------|
| [Flag 1] | High/Medium/Low | [Source] | [Specific evidence] | [What this means for moat] |
| [Flag 2] | High/Medium/Low | [Source] | [Specific evidence] | [What this means for moat] |
| [Flag 3] | High/Medium/Low | [Source] | [Specific evidence] | [What this means for moat] |

**Red Flag Summary:** [Clean / Minor Concerns / Moderate Concerns / Significant Concerns]

---

## Moat Implications

### Customer Signals → Moat Assessment

| Signal | Moat Implication |
|--------|------------------|
| [Customer finding 1] | [What it means for moat — validated/challenged/neutral] |
| [Customer finding 2] | [What it means for moat] |

### Employee Signals → Operational Health

| Signal | Moat Implication |
|--------|------------------|
| [Employee finding 1] | [What it means for competitive position] |
| [Employee finding 2] | [What it means for talent/culture moat] |

### Partner Signals → Ecosystem Strength

| Signal | Moat Implication |
|--------|------------------|
| [Partner finding 1] | [What it means for ecosystem moat] |

### Competitive Signals → Competitive Position

| Signal | Moat Implication |
|--------|------------------|
| [Competitive finding 1] | [What this reveals about defensibility] |

### Overall Moat Assessment

[2-3 paragraphs synthesizing what the scuttlebutt analysis reveals about the company's moat. Does grassroots sentiment validate or challenge the moat thesis?]

**Moat Validation Status:** Validated / Partially Validated / Challenged / Inconclusive

---

## Monitoring Dashboard

### Metrics to Track

| Metric | Current Value | Warning Threshold | Frequency |
|--------|---------------|-------------------|-----------|
| Glassdoor Rating | X.X | Below X.X | Quarterly |
| CEO Approval | X% | Below X% | Quarterly |
| [Review Site] Rating | X.X | Below X.X | Quarterly |
| Customer Churn Signals | [Current] | [Threshold] | Quarterly |
| Short Interest | X% | Above X% | Monthly |

### Early Warning Signals

- [ ] **Customer:** [Specific thing to watch for]
- [ ] **Employee:** [Specific thing to watch for]
- [ ] **Partner:** [Specific thing to watch for]
- [ ] **Competitive:** [Specific thing to watch for]

---

## Data Sources and Methodology

### Sources Consulted

| Category | Sources | Data Points |
|----------|---------|-------------|
| Customer | [List] | ~X |
| Employee | [List] | ~X |
| Partner | [List] | ~X |
| Competitor | [List] | ~X |
| Expert | [List] | ~X |
| Media | [List] | ~X |

### Limitations

[Note any data gaps, limited sources, or areas where confidence is lower]

### Search Queries Used

[List key search queries for reproducibility]

---

## Conclusion

### Scuttlebutt Health Assessment

**Overall Score:** X.X / 5.0
**Assessment:** [Strong / Mixed / Concerning / Poor]

**Summary:**
[2-3 paragraph conclusion synthesizing the key findings and their investment implications]

### Investment Implications

- **Trust company narrative on:** [Areas where scuttlebutt validates management claims]
- **Be skeptical about:** [Areas where scuttlebutt challenges or raises questions]
- **Key monitoring points:** [What to watch going forward]

### Connection to Other Analyses

- **Moat Strength:** This scuttlebutt analysis [validates/challenges/adds nuance to] the moat assessment
- **Competitive Landscape:** The grassroots view [confirms/contradicts/adds to] the competitive analysis
- **Investment Thesis:** [How does this affect the overall thesis?]

---

*Analysis Date: [YYYY-MM-DD-HHMM]*
```
