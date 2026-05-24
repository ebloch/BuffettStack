# Phase 1A: Moat Strength Scoring Prompt

Use this reference for the moat strength pass for analyze-moat-strength.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are scoring 10 moat items for [COMPANY] ([TICKER]) using a -2 to +2 checklist.

This answers the question: **Can this company defend its position? Prove it with scored, quantified evidence.**

**Source Documents:**
- 10K Synthesis Memos: [10K_MEMO_PATHS]
- Scuttlebutt Analysis: [SCUTTLEBUTT_PATH]
- Competitive Landscape Analysis: [COMPETITIVE_LANDSCAPE_PATH]

**Output Directory:** [OUTPUT_DIR]
**Timestamp:** [TIMESTAMP]

---

## Scoring System: -2 to +2

| Score | Meaning | +2 Requirement |
|-------|---------|----------------|
| +2 | Exceptional — unmistakable, proven advantage | **No material concerns in segments >~15% of revenue.** "Why Not Higher?" must be N/A |
| +1 | Real advantage with identified limitations | Strong, but has identifiable limitations |
| 0 | Neutral — no meaningful advantage or disadvantage | Neither helps nor hurts |
| -1 | Weakness or emerging concern | Notable weakness requiring monitoring |
| -2 | Significant weakness — red flag / potential thesis killer | Active drag on competitive position |

**+2 Gate:** If ANY material concern exists for an item, the maximum score is +1. Only award +2 when "Why Not Higher?" is genuinely N/A. **Materiality matters:** a concern must affect segments representing >~15% of revenue/profit to gate a +2. Weaknesses in immaterial segments should be noted but do not cap the score.

---

## Your Task

### Step 1: Read All Source Documents (REQUIRED FIRST)

**Before conducting any web research**, read all existing company research as foundational context.

#### 10K Synthesis Memos
Read ALL 10K synthesis memos provided. Extract:
- Management's stated competitive advantages and moat claims
- Risk factors that reveal moat vulnerabilities
- Market position, share, and customer data
- R&D spending and strategic priorities
- Customer concentration and retention metrics

#### Scuttlebutt Analysis
Read the scuttlebutt analysis. Extract:
- Customer perspective on why they choose this company
- What would make customers switch (critical for switching cost assessment)
- Employee views on competitive position
- Real-world validation or contradiction of moat claims

#### Competitive Landscape Analysis
Read the competitive landscape analysis. Extract:
- Competitor positions and relative strengths
- Who Lost and Why (for reference section)
- Industry disruption signals
- Market share dynamics

**This existing research is your foundation.** Your job is to score each item based on evidence, not rewrite the research.

### Step 1B: Build Materiality Map

Before scoring, identify the company's revenue/profit breakdown by segment. This map determines what counts as a "material concern" for the +2 gate.

Produce a table like:

| Segment | Revenue | % of Total | Material (>~15%)? |
|---------|---------|------------|-------------------|
| [segment] | [$X] | [X%] | Yes/No |

**How to use:** When evaluating evidence for/against a score, weight it by the segment it applies to. A weakness in a segment representing <15% of revenue should be noted but does not cap a score at +1. Only concerns affecting material segments (>~15%) trigger the +2 gate.

Include this materiality map in the output file as a reference table near the top of Part 2 (before the first scored item).

### Step 2: Read Templates

Read required templates:
- Output template: `.codex/skills/analyze-moat-strength/references/output-template.md`
- Validation checklist: `.codex/skills/analyze-moat-strength/references/validation-checklist.md`

### Step 3: Web Research

After reading existing research, conduct targeted web searches to fill evidence gaps:

**Pricing Power (A1):**
- "[COMPANY] price increases", "[COMPANY] pricing history", "[COMPANY] pricing power"

**Switching Costs (A2):**
- "[COMPANY] customer retention rate", "[COMPANY] implementation cost", "[COMPANY] switching cost"

**Network Effects (A3):**
- "[COMPANY] network effects", "[COMPANY] user growth", "[COMPANY] platform ecosystem"

**Cost/Scale (A4):**
- "[COMPANY] operating margin vs peers", "[COMPANY] cost advantage", "[COMPANY] economies of scale"

**Branding (A5):**
- "[COMPANY] brand premium", "[COMPANY] brand value", "[COMPANY] brand loyalty", "[COMPANY] brand vs private label"

**Cornered Resource (A6):**
- "[COMPANY] patents", "[COMPANY] regulatory license", "[COMPANY] proprietary data", "[COMPANY] exclusive contracts"

**Process Power (A7):**
- "[COMPANY] operating system", "[COMPANY] production system", "[COMPANY] operational excellence", "[COMPANY] culture advantage"

**$10B Test (B1):**
- "[COMPANY] competitive entry barriers", "new entrants [industry]"

**Disruption Risk (B2):**
- "[COMPANY] disruption risk", "[industry] disruption", "[COMPANY] competitors emerging"

**Structural vs Executional (B3):**
- "[COMPANY] management dependency", "[COMPANY] CEO impact", "[COMPANY] organizational advantages"

### Step 4: Score All 10 Items

For each item, produce:
1. **Score** (-2 to +2)
2. **"Why Not Higher?"** — if score < +2, state the limitation; if +2, must be "N/A"
3. **2-4 bullet points** explaining the score rationale. Do NOT repeat data from the evidence table — bullets explain *why* the evidence matters, the table provides the *what*.
4. **Evidence table** with quantified metrics, periods, and sources

#### Category A: Moat Sources

**A1: Pricing Power** — Can they raise prices without losing customers?
- Look for: price increase history, customer retention post-increase, price premium vs competitors
- Buffett's #1 moat test: "The single most important decision in evaluating a business is pricing power"

**A2: Switching Costs** — How painful is it for customers to leave?
- Look for: implementation cost of alternatives, customer retention rates, average tenure, integration depth
- Quantify the cost: dollars, months, risk of switching

**A3: Network Effects** — Does each user make the product more valuable?
- Look for: user growth curves, network density, multi-homing rates
- Identify type: direct (users attract users), indirect (two-sided), data (more data = better product), platform
- Score 0 if no meaningful network effect exists — don't force it

**A4: Cost / Scale Advantages** — Structurally lower cost than competitors?
- Look for: margin vs peer average, fixed cost leverage, purchasing power, minimum efficient scale
- Distinguish structural (geology, location, proprietary process) from scale-based

**A5: Branding** — Does the brand command higher prices/volumes via historically-earned consumer trust?
- Brand premium must be quantified: "25% price premium vs private label" not "strong brand"
- Look for: brand recall, customer willingness to pay more, brand equity valuation
- Distinct from A6 — brand is durable consumer perception, not IP/licenses/regulatory assets
- Score +2 if: consistently commands 20%+ premium with no erosion
- Score 0 if: functional/commodity brand
- Score -2 if: brand damaged or declining

**A6: Cornered Resource** — Preferential access to a valuable resource others cannot obtain?
- Must be specific: "14 patents expiring 2030-2035" not "strong IP portfolio"
- Examples: patents with runway, FDA-approved facilities, regulatory licenses, geological rights, proprietary data, exclusive contracts
- NOT just "good engineers" — must be truly exclusive access
- Score +2 if: truly exclusive and critical to competitive position
- Score 0 if: resources available to competitors
- Score -2 if: cornered resource expiring or eroding

**A7: Process Power** — Deeply embedded organizational processes/culture enabling superior results, built through sustained evolution?
- Look for: operational metrics vs peers (cost per unit, quality, speed), process tenure, failed competitor replication
- Examples: Toyota Production System, Danaher Business System, Costco's culture
- Key test: could you hire away the CEO and replicate it? If yes → executional, not Process Power
- Score +2 if: quantifiable process advantage sustained 10+ years, competitors tried and failed to copy
- Score 0 if: industry-standard processes
- Score -2 if: processes are competitive disadvantage

#### Category B: Moat Durability

**B1: The $10B Test** — Could a well-funded competitor replicate this?
- Be brutally honest: most businesses CAN be replicated given enough capital and time
- What specifically can't be copied? Network effects with critical mass? Decades of customer relationships? Regulatory moat?
- Produce the "What Can't Be Copied" table

**B2: Disruption Risk** — Christensen disruption vectors
- Assess ALL 3 vectors: Low-End, New-Market, Technology
- Each gets a threat level: Low / Medium / High
- Overshooting assessment: is the company over-serving customers?
- Name specific disruptors for the Disruption Watch List (reference section)

**B3: Structural vs Executional** — Does the moat survive a mediocre CEO?
- Categorize each moat source from A1-A7 as Structural or Executional
- Structural: embedded in the business (network effects, regulatory moats, geological advantages)
- Executional: depends on continued excellent management (culture, operational excellence, capital allocation)
- Overall management dependency: Low / Medium / High

### Step 5: Compute Composite & Rating

1. Sum all 10 scores
2. Divide by 10 = composite
3. Map to rating:
   - >= 1.25 → **WIDE**
   - 0.50 to 1.24 → **NARROW**
   - < 0.50 → **NONE**

4. Assess confidence:
   - **HIGH**: All 10 items have quantified evidence; all source documents cross-referenced
   - **MEDIUM**: Most items quantified; 1-2 data gaps
   - **LOW**: Several items qualitative only; significant data gaps

### Step 6: Write Reference Sections

#### Who Lost and Why
- Minimum 2 former industry leaders from the competitive landscape analysis
- Table: Company, Peak Position, What Happened, Moat That Failed, Lesson
- Pattern Analysis: common thread that killed these moats
- Implications for [COMPANY]

#### Disruption Watch List
- Minimum 3 specific disruptors (from B2 research)
- Table: Disruptor, Stage (Nascent/Emerging/Accelerating), Threat Vector, Threat Level, Warning Signal

### Step 7: Run Validation Checklist

**MANDATORY:** Run through the validation checklist before writing. Key checks:

- [ ] All 10 items scored with -2 to +2
- [ ] Every +2 has "Why Not Higher?" = N/A
- [ ] Composite math correct (sum / 10)
- [ ] Rating matches composite thresholds
- [ ] Each item has quantified evidence table
- [ ] B2 has all 3 disruption vectors assessed
- [ ] B3 categorizes each A1-A7 moat source
- [ ] At least 2 former leaders in Who Lost and Why
- [ ] At least 3 disruptors in Watch List

### Step 8: Write Output

Write analysis to:
```
[OUTPUT_DIR]/Moat Strength - Analysis - [COMPANY] - [TIMESTAMP].md
```

Follow the output template structure exactly (Parts 1, 2, 4, 5). **Leave Part 3 (Trajectory) blank** — it will be filled by the trajectory pass.

Write a placeholder for Part 3:
```markdown
## Part 3: Trajectory Assessment

*[To be completed by trajectory pass]*
```

---

## Guidelines

**Be Concise:** Use bullet points, not paragraphs, for item justifications. The evidence table carries the data — bullets explain the reasoning. Summaries and narratives should be 4-6 sentences, not multi-paragraph essays.

**Quantify Everything:** "Strong brand" is not evidence. "20% pricing premium vs. generic alternatives sustained over 10 years" is evidence.

**Be Skeptical:** Assume the moat is weaker than management claims until proven otherwise.

**+2 Gate:** If any material concern exists, max score is +1. Reserve +2 for unmistakable advantages.

**Score 0 Generously:** Not every company has every moat source. Score 0 for items that don't apply — don't inflate scores to make the company look better.

**Negative Scores Matter:** A company with a -2 on disruption risk and +2 on pricing power tells a very different story than one with 0 on both.

**Connect to Existing Research:** Reference findings from scuttlebutt and competitive landscape. This moat strength analysis provides the scored assessment; the prerequisite research provides the raw evidence.

---

## Tool Usage

- **Read:** Use for reading source documents, template files, and checklists
- **Write:** Use for saving the output analysis
- **Web search:** Use for pricing data, competitor data, disruption signals, market share
- **File search pattern:** Use for finding additional research files if needed

---

## Return Value

When complete, return a JSON object:
```json
{
  "output_file_path": "[path to written analysis]",
  "sources_used": ["list of all source file paths read"],
  "status": "success" | "partial" | "failed",
  "notes": "[any issues encountered]"
}
```

The `sources_used` list is CRITICAL — Phase 2 Devil's Advocate will use these paths to re-read source documents.
```
