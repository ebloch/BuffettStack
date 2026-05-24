# Phase 1B: Trajectory Assessment Prompt

Use this reference for the trajectory pass for analyze-moat-strength.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are scoring the moat TRAJECTORY for [COMPANY] ([TICKER]) — an independent assessment of which direction the moat is moving.

**CRITICAL: You are assessing DIRECTION, not STRENGTH.** A company can have a WIDE moat that is NARROWING, or a NARROW moat that is WIDENING. Your job is to determine the trend, not re-rate the moat.

**You have NO knowledge of the moat strength scores.** This is by design — trajectory must be assessed independently to avoid anchoring.

**Source Documents:**
- 10K Synthesis Memos: [10K_MEMO_PATHS]
- Scuttlebutt Analysis: [SCUTTLEBUTT_PATH]
- Competitive Landscape Analysis: [COMPETITIVE_LANDSCAPE_PATH]

---

## Scoring System: -2 to +2

| Score | Meaning |
|-------|---------|
| +2 | Strong positive trend — clear evidence of moat widening |
| +1 | Modest positive trend with some uncertainty |
| 0 | Stable — no clear directional change |
| -1 | Modest negative trend — early warning signals |
| -2 | Strong negative trend — clear evidence of moat erosion |

---

## Your Task

### Step 1: Read All Source Documents

Read all provided source documents. Focus on TREND indicators:
- Multi-year market share changes
- R&D and investment trajectory
- Competitive dynamics shifting over time
- Management commentary about strategic direction
- Industry secular trends

### Step 2: Web Research

Conduct targeted searches for trend data:

**T1: Competitive Position Trend**
- "[COMPANY] market share 2020 2021 2022 2023 2024 2025"
- "[COMPANY] market share trend"
- "[industry] new entrants", "[industry] competitive dynamics"
- "[COMPANY] customer wins losses"

**T2: Reinvestment Quality**
- "[COMPANY] R&D spending trend"
- "[COMPANY] capital expenditure", "[COMPANY] capex vs peers"
- "[COMPANY] share buyback vs investment"
- "[COMPANY] acquisition strategy"

**T3: Secular Alignment**
- "[industry] secular trends", "[industry] future outlook"
- "[COMPANY] tailwinds headwinds"
- Macro trends affecting the industry (regulation, technology, demographics, ESG)

### Step 3: Score 3 Trajectory Items

#### T1: Competitive Position Trend
**Question:** Is market share gaining or losing? Are new entrants appearing or failing?

Evidence to find:
- Market share data over 5 years (even directional if exact numbers unavailable)
- New competitor entry/exit patterns
- Customer win/loss trends
- Pricing power trend (improving or deteriorating)

Score +2 if: gaining share consistently with competitors exiting
Score 0 if: stable position, normal competitive dynamics
Score -2 if: losing share to multiple competitors or new entrants gaining traction

#### T2: Reinvestment Quality
**Question:** Is the company investing to widen the moat, or harvesting/doing financial engineering?

Evidence to find:
- R&D as % of revenue vs peers and vs own history
- Capex directed toward moat-widening (new products, capacity, technology) vs maintenance
- Share buybacks vs organic investment ratio
- Acquisition strategy: moat-widening or revenue-chasing?

Score +2 if: consistently outinvesting peers in moat-widening activities
Score 0 if: investing at industry norms, maintaining position
Score -2 if: underinvesting, heavy buybacks at high valuations, harvesting

#### T3: Secular Alignment
**Question:** Do macro/secular trends reinforce or erode the moat?

Evidence to find:
- 2-3 major secular trends affecting the industry
- For each trend: does it help or hurt this company's competitive position?
- Regulatory direction (tightening = moat for incumbents? loosening = threat?)
- Technology shifts (AI, digital, etc.) — tailwind or headwind?

Score +2 if: multiple powerful secular trends reinforce the moat
Score 0 if: secular trends are mixed or neutral
Score -2 if: multiple secular trends actively erode the moat

### Step 4: Compute Trajectory Direction

1. Sum the 3 scores
2. Divide by 3 = trajectory composite
3. Map to direction:
   - >= +0.75 → **WIDENING**
   - -0.74 to +0.74 → **STABLE**
   - <= -0.75 → **NARROWING**

### Step 5: Write Trajectory Section

Produce the complete Part 3 content as markdown, following this structure:

```markdown
## Part 3: Trajectory Assessment

*Scored by independent pass with fresh context.*

**Direction:** [WIDENING / STABLE / NARROWING]
**Trajectory Composite:** [X.XX]

### Trajectory Scorecard

| # | Item | Score | Evidence Summary |
|---|------|-------|------------------|
| T1 | Competitive Position Trend | [score] | [one-line evidence] |
| T2 | Reinvestment Quality | [score] | [one-line evidence] |
| T3 | Secular Alignment | [score] | [one-line evidence] |

**Trajectory Composite:** [sum] / 3 = [X.XX] → [DIRECTION]

### Trajectory Narrative

[4-6 sentences. What's driving the trend? What could reverse it?]
```

---

## Guidelines

**Direction, Not Strength:** You're answering "which way is the moat moving?" not "how strong is it?" A WIDE moat can be NARROWING.

**Look for Inflection Points:** The most valuable insight is identifying when a trend is about to change direction.

**Be Independent:** You have no knowledge of the moat strength scores. Don't try to infer them or align with them.

**Quantify Trends:** "Market share growing" is weak. "Market share grew from 12% to 18% over 5 years" is evidence.

---

## Return Value

When complete, return a JSON object:
```json
{
  "trajectory_content": "[the full Part 3 markdown content]",
  "trajectory_direction": "WIDENING" | "STABLE" | "NARROWING",
  "trajectory_composite": [number],
  "status": "success" | "partial" | "failed"
}
```

The `trajectory_content` will be inserted into the output file by the orchestrator.
```
