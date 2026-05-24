# Phase 1: Fisher Analysis Prompt

Use this reference for the analysis pass for run-fisher-analysis.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are conducting a Philip Fisher 15-Point Analysis for [COMPANY] ([TICKER]).

**Output Path:** [OUTPUT_PATH]

---

## Philosophy

You are applying Philip Fisher's framework from "Common Stocks and Uncommon Profits" (1958). Fisher believed that qualitative factors — management quality, competitive position, growth potential — matter more than quantitative metrics alone. His approach emphasizes:
- Finding companies that can grow for "years to come"
- Management that is both competent AND honest
- Businesses with genuine competitive advantages
- Long-term thinking over short-term metrics

---

## Step 1: Read All Existing Research

Read all available prerequisite research files to build a comprehensive foundation:

### Required Research (all must exist)
- `**/[COMPANY]/1.1-Annual-Filings/*.md` — 10K synthesis memos
- `**/[COMPANY]/1.3-Financial-Statements/*.md` — Financial statements
- `**/[COMPANY]/2.4-Management-Audit/*.md` — Management credibility audits
- `**/[COMPANY]/2.2-Scuttlebutt/*.md`, `**/[COMPANY]/2.3-Competitive-Landscape/*.md`, `**/[COMPANY]/2.6-Moat-Strength/*.md` — Competitive landscape, moat strength, scuttlebutt
- `**/[COMPANY]/2.5-Risk-Assessment/*.md` — Risk analysis, bear case

### Optional Research (read if exists)
- `**/[COMPANY]/1.2-Investor-Presentations/*.md` — Investor day memos
- `**/[COMPANY]/1.4-Earnings/*.md` — Quarterly earnings reviews

**Leverage prior research:** When scoring each Fisher point, cite specific findings from existing memos rather than re-researching from scratch. Reference the source file.

---

## Rating System

For each of the 15 points, assign a score from -2 to +2:

| Score | Meaning | Criteria |
|-------|---------|----------|
| **+2** | Clear strength / competitive advantage | Unmistakable evidence of excellence; top-tier vs. peers |
| **+1** | Above average / solid | Better than most competitors; positive but not exceptional |
| **0** | Average / neutral / no edge | Neither advantage nor disadvantage; industry-typical |
| **-1** | Below average / concern | Weaker than peers; pattern suggests problems |
| **-2** | Significant weakness / red flag | Clear negative evidence; potential disqualifier |

**Total score range:** -30 to +30

| Total Score | Interpretation |
|-------------|----------------|
| +20 to +30 | Exceptional quality; rare |
| +10 to +19 | High quality; strong candidate |
| 0 to +9 | Average to above-average; needs other factors |
| -10 to -1 | Below average; significant concerns |
| -30 to -11 | Poor quality; likely avoid |

**Important:** Every score MUST include specific evidence. No assertions without facts. A score of 0 is not a cop-out — it means genuinely average with evidence to support that assessment.

---

## The 15 Points — Detailed Analysis

### Point 1: Market Potential

**Question:** Does the company have products or services with sufficient market potential to make possible a sizable increase in sales for at least several years?

**What to investigate:**
- Total addressable market (TAM) size and growth rate
- Company's current market share and penetration
- New markets or geographies the company can enter
- Product/service expansion opportunities
- Secular trends supporting demand growth
- Risk of market saturation

**Scoring guidance:**
- **+2:** TAM growing >10% annually, company gaining share, multiple expansion vectors
- **+1:** TAM growing steadily, company maintaining or slightly gaining share
- **0:** Mature but stable market, company holding position
- **-1:** Flat or declining TAM, limited expansion opportunities
- **-2:** Shrinking market, company in structural decline

---

### Point 2: Management Determination to Develop New Products

**Question:** Does the management have a determination to continue to develop products or processes that will still further increase total sales potentials when the growth potentials of currently attractive product lines have largely been exploited?

**What to investigate:**
- R&D spending trends (absolute and as % of revenue)
- Pipeline of new products/services in development
- Track record of successful new product launches
- Management commentary on innovation priorities
- Ability to evolve when existing products mature

**Scoring guidance:**
- **+2:** Consistent R&D investment, track record of successful launches, clear pipeline visibility
- **+1:** Adequate R&D, some successful new products, management focused on innovation
- **0:** R&D exists but hit-or-miss track record; industry-typical investment
- **-1:** Minimal R&D, milking existing products, few new launches
- **-2:** R&D being cut, no pipeline, company riding legacy products to decline

---

### Point 3: R&D Effectiveness

**Question:** How effective are the company's research and development efforts in relation to its size?

**What to investigate:**
- R&D spending efficiency (revenue growth per R&D dollar)
- Success rate of R&D projects
- Time from R&D to commercial product
- Comparison to competitors' R&D spending and outcomes
- Quality of research organization and talent

**Scoring guidance:**
- **+2:** R&D dollars translate to market-leading products; competitive advantage from innovation
- **+1:** Solid R&D producing competitive products; keeping pace with industry
- **0:** Adequate R&D with typical industry results
- **-1:** R&D underperforming peers; slow to market; products not differentiated
- **-2:** R&D clearly failing; falling behind competitors technologically

**Note:** For companies where R&D isn't applicable (e.g., pure distribution, financial services), evaluate their equivalent innovation capability — new service development, process improvement, etc.

---

### Point 4: Sales Organization

**Question:** Does the company have an above-average sales organization?

**What to investigate:**
- Sales force effectiveness and productivity
- Customer acquisition costs and trends
- Win rates in competitive situations
- Sales team tenure and turnover
- Quality of sales leadership
- Channel partner relationships (if applicable)

**Scoring guidance:**
- **+2:** Industry-leading sales productivity, strong win rates, low turnover, excellent reputation
- **+1:** Solid sales organization, competitive effectiveness
- **0:** Average sales capability; wins some, loses some
- **-1:** Below-average productivity, high turnover, losing to competitors
- **-2:** Dysfunctional sales organization, major customer losses, talent exodus

---

### Point 5: Profit Margins

**Question:** Does the company have a worthwhile profit margin?

**What to investigate:**
- Gross margin vs. industry average
- Operating margin vs. competitors
- Net margin trends over time
- Margin consistency through economic cycles
- Understanding what drives margins (pricing power, scale, efficiency)

**Scoring guidance:**
- **+2:** Margins significantly above industry, stable or improving, demonstrates pricing power
- **+1:** Above-average margins, reasonably stable
- **0:** Industry-average margins, stable
- **-1:** Below-industry margins, declining trend
- **-2:** Chronically low margins, no path to improvement, structural disadvantage

---

### Point 6: Margin Improvement Actions

**Question:** What is the company doing to maintain or improve profit margins?

**What to investigate:**
- Specific initiatives to improve efficiency
- Pricing strategy and pricing power
- Cost reduction programs and their effectiveness
- Automation or technology investments
- Supply chain optimization
- Mix shift toward higher-margin products/services

**Scoring guidance:**
- **+2:** Clear, effective margin initiatives; track record of delivery; structural advantages being built
- **+1:** Reasonable margin focus, some effective initiatives
- **0:** Typical cost management; margins stable but no clear improvement plan
- **-1:** No clear margin strategy, margins drifting down
- **-2:** Margins deteriorating with no credible plan to address

---

### Point 7: Labor Relations

**Question:** Does the company have outstanding labor and personnel relations?

**What to investigate:**
- Employee satisfaction (Glassdoor, Blind, surveys)
- Turnover rates vs. industry
- Union relationships (if applicable)
- History of labor disputes or strikes
- Compensation competitiveness
- Workplace culture reputation

**Scoring guidance:**
- **+2:** Top-tier employer reputation, low turnover, highly engaged workforce, no labor issues
- **+1:** Good employer, reasonable satisfaction, manageable turnover
- **0:** Average employer; typical industry turnover and satisfaction
- **-1:** Below-average satisfaction, high turnover, difficulty attracting talent
- **-2:** Major labor problems, toxic culture, strikes, mass departures

---

### Point 8: Executive Relations

**Question:** Does the company have outstanding executive relations?

**What to investigate:**
- Executive team tenure and stability
- Internal promotion vs. external hiring for senior roles
- Executive compensation alignment with shareholders
- Relationships within the C-suite
- Management team depth and succession planning
- Executive departures and reasons

**Scoring guidance:**
- **+2:** Stable, long-tenured team; strong internal development; well-aligned compensation
- **+1:** Reasonably stable team, some depth, adequate alignment
- **0:** Typical executive tenure and turnover for industry
- **-1:** High executive turnover, compensation misalignment, talent gaps
- **-2:** Revolving door at C-suite, major executive conflicts, no succession planning

---

### Point 9: Management Depth

**Question:** Does the company have depth to its management?

**What to investigate:**
- Layers of capable management below CEO
- Internal talent development programs
- Succession readiness for key positions
- Ability to delegate and decentralize
- Track record when executives depart
- Quality of division/regional leadership

**Scoring guidance:**
- **+2:** Deep bench, strong succession plans, company thrives despite departures, excellent talent development
- **+1:** Adequate depth in most areas, reasonable succession plans
- **0:** Typical management structure; some key-person risk but not critical
- **-1:** Thin management layer, over-reliance on CEO, unclear succession
- **-2:** Critical key-person risk, no succession planning, single points of failure

---

### Point 10: Cost Analysis and Controls

**Question:** How good are the company's cost analysis and accounting controls?

**What to investigate:**
- Cost accounting sophistication
- Ability to identify and address cost problems quickly
- Budget discipline and accuracy
- Internal audit function quality
- Historical accuracy of financial forecasts
- Accounting conservatism vs. aggressiveness
- Any history of restatements or control issues

**Scoring guidance:**
- **+2:** Highly accurate forecasts, conservative accounting, no control issues, strong internal audit
- **+1:** Reasonable forecast accuracy, clean audit history, adequate controls
- **0:** Typical forecast accuracy; standard accounting practices
- **-1:** Poor forecast accuracy, aggressive accounting, weak controls
- **-2:** History of restatements, auditor concerns, control failures, SEC issues

---

### Point 11: Industry-Specific Competitive Clues

**Question:** Are there other aspects of the business, somewhat peculiar to the industry involved, which will give the investor important clues as to how outstanding the company may be in relation to its competition?

**What to investigate:**
- Industry-specific success metrics (varies by sector)
- Competitive advantages unique to this industry
- Key performance indicators that matter in this sector
- What separates winners from losers in this industry
- Regulatory or structural advantages

**Examples by industry:**
- **Retail:** Same-store sales, inventory turnover, sales per square foot
- **Insurance:** Combined ratio, reserve adequacy, underwriting discipline
- **Software:** Net revenue retention, CAC payback, rule of 40
- **Manufacturing:** Capacity utilization, defect rates, lead times
- **Financial services:** Net interest margin, efficiency ratio, credit quality

**Scoring guidance:**
- **+2:** Leading on industry-specific metrics, clear competitive advantages in industry context
- **+1:** Above-average on most industry metrics
- **0:** Average performer on industry-specific metrics
- **-1:** Lagging on key industry metrics
- **-2:** Significantly behind competitors on critical industry factors

---

### Point 12: Long-Range Outlook

**Question:** Does the company have a short-range or long-range outlook in regard to profits?

**What to investigate:**
- Investment horizon in decision-making
- Willingness to sacrifice short-term for long-term
- R&D and capex investment levels
- Management incentive time horizons
- History of short-term earnings management
- Strategic planning process and execution

**Scoring guidance:**
- **+2:** Consistently long-term focused, invests through cycles, resists quarterly pressures
- **+1:** Generally long-term oriented with occasional short-term pressures
- **0:** Balanced approach; neither clearly long-term nor short-term focused
- **-1:** Short-term focused, underinvesting in future, chasing quarterly numbers
- **-2:** Clearly sacrificing long-term for short-term, eating the seed corn

---

### Point 13: Equity Dilution Risk

**Question:** In the foreseeable future will the growth of the company require sufficient equity financing so that the larger number of shares then outstanding will largely cancel the existing stockholders' benefit from this anticipated growth?

**What to investigate:**
- Current balance sheet strength and cash position
- Capital intensity of growth plans
- Historical financing patterns (debt vs. equity)
- Stock-based compensation levels
- Share count trend over time
- Access to debt markets
- Free cash flow generation vs. capital needs

**Scoring guidance:**
- **+2:** Strong FCF, minimal dilution, can fund growth internally, buyback history
- **+1:** Adequate FCF, manageable SBC, unlikely to need equity
- **0:** Modest dilution from SBC; typical for industry
- **-1:** Regular equity raises, high SBC, significant dilution
- **-2:** Chronic dilution, capital-hungry business model, shareholders regularly diluted

---

### Point 14: Management Transparency

**Question:** Does the management talk freely to investors about its affairs when things are going well but "clam up" when troubles and disappointments occur?

**What to investigate:**
- Communication quality during good times AND bad times
- Willingness to discuss challenges and mistakes
- Consistency of disclosure practices
- Accessibility to investors and analysts
- Quality of conference call Q&A
- Treatment of bad news vs. good news

**Scoring guidance:**
- **+2:** Equally forthcoming in good and bad times, proactively discusses challenges, admits mistakes
- **+1:** Generally transparent, handles bad news reasonably well
- **0:** Typical corporate communication; somewhat guarded but not deceptive
- **-1:** Clearly more communicative when things go well, deflects on problems
- **-2:** Hides bad news, blames external factors, never admits mistakes

---

### Point 15: Management Integrity

**Question:** Does the company have a management of unquestionable integrity?

**What to investigate:**
- History of ethical issues or scandals
- Treatment of minority shareholders
- Related party transactions
- Compensation fairness and alignment
- Regulatory issues or legal problems
- Insider trading patterns
- Capital allocation decisions favoring insiders

**Scoring guidance:**
- **+2:** Spotless integrity record, shareholder-friendly actions, aligned incentives, industry respect
- **+1:** No integrity concerns, reasonable alignment
- **0:** No red flags but limited positive evidence; typical corporate governance
- **-1:** Some integrity concerns, related party issues, or questionable actions
- **-2:** Clear integrity red flags — avoid entirely

**Fisher's view:** "If there is a serious question of the lack of a strong management sense of trusteeship for stockholders, the investor should never seriously consider participating in such an enterprise."

---

## Output Template

Read the output template from:
```
.codex/skills/run-fisher-analysis/references/output-template.md
```

Follow its structure when producing the final analysis.

---

## Guidelines

**Evidence Required:** Every score must cite specific evidence. "Management seems good" is not acceptable; "CEO has been in role 15 years, grew revenue 4x, Glassdoor 4.2 rating" is.

**Industry Context:** Adjust expectations by industry. A 10% margin may be excellent in retail but poor in software. A score of 0 means average *for this industry*.

**Look for Disqualifiers:** Points 14 and 15 (transparency and integrity) are potential disqualifiers. A score of -2 on either should give serious pause regardless of total score.

**Negative Scores Matter More:** Fisher would reject a company with a +20 total if it had a -2 on integrity. A few critical weaknesses matter more than many modest strengths.

**Zero is Not a Cop-Out:** A score of 0 requires evidence that the company is genuinely average on that dimension. Don't use 0 to avoid making a judgment.

**Time Horizon:** This framework is for long-term investors. A company might have temporary issues but still score well if the fundamental quality is there.

---

## Write Output

Save the completed analysis to: [OUTPUT_PATH]

---

## Return Value

When complete, return a JSON object:
```json
{
  "output_file_path": "[path to written analysis]",
  "total_score": [number from -30 to +30],
  "verdict": "PASS" | "MARGINAL" | "FAIL",
  "disqualifier_flags": ["Point 14: -2" or "Point 15: -2" if applicable],
  "status": "success" | "partial" | "failed",
  "notes": "[any issues encountered]"
}
```
```
