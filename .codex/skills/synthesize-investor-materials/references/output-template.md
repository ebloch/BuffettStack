# Investor Materials Synthesis Output Template (Hybrid)

This hybrid format combines:
- **YAML frontmatter** — Essential metadata for filtering/search
- **Prose-driven body** — Narrative sections for comprehension
- **Tracking tables** — Promises to Track, Claims to Verify, New vs. Known

Target: ~250-300 lines, ~2,200-2,600 tokens per memo.

---

## Source Reference Guidelines

**MANDATORY:** Include slide/page references `(Slide XX)` or `(p.XX)` for:
- All verbatim quotes
- All guidance/targets
- All promises to track
- All competitive claims

---

## Number Format Rules

| Context | Format | Example |
|---------|--------|---------|
| Tables (all) | M suffix, no $ | `4272M` |
| Prose | Full currency | `$4.3 billion` |
| Percentages | One decimal | `21.4%` |
| Per-share | $ + two decimals | `$53.11` |
| Growth targets | Sign prefix | `+15%` |

---

## YAML Frontmatter

```yaml
---
type: investor-materials-synthesis
company: [Company Name]
ticker: [TICKER]
event_type: investor-day|capital-markets-day|quarterly-presentation|shareholder-letter|standing-overview
event_date: [YYYY-MM-DD]
event_name: "[Event name as presented]"
synthesis_date: [YYYY-MM-DD]
formal_qc_run: false
formal_audit_run: false
qc_status: pending
audit_status: blocked_until_qc_complete
qc_completed_at: null
audit_completed_at: null
qc_result: null
audit_result: null
files_analyzed: [count]

# Key metrics presented (if any)
metrics:
  revenue_m: [number or null]
  operating_income_m: [number or null]
  net_income_m: [number or null]
  # Add 2-3 key metrics emphasized in presentation

# Capital allocation (if discussed)
capital:
  buyback_auth_m: [number or null]
  dividend_policy: "[brief summary or null]"
  m_and_a_appetite: high|medium|low|none|null

# Quality assessment
quality:
  new_information: high|medium|low
  specificity: high|medium|low
  event_significance: high|medium|low
---
```

---

# [Company] — [Event Name] — Memo

**Date:** [Event Date]
**Materials:** [N] files ([brief list of types])

---

## Key Takeaways

Write 5-7 narrative bullets with **bold lead-ins**. Most important insights first.

- **[Lead-in phrase]:** [Narrative insight with specific data point and slide reference. Focus on what's new, what matters for the thesis, what changes your view.]

- **[Lead-in phrase]:** [Continue with material insights. Each bullet should answer "so what?" for an investor.]

- **[Lead-in phrase]:** [Include any surprises, concerns, or thesis-confirming data points.]

*Each bullet: one insight, 1-2 sentences. Reference slides for key claims.*

---

## Source Materials

| File | Type | Slides | Focus |
|------|------|--------|-------|
| [filename] | Strategy/Financial/Segment/Overview | [N] | [Brief description] |

---

## Strategic Messaging

**Management's Core Thesis:**

[2-3 paragraphs on what management wants investors to believe. What is the narrative? What are they emphasizing? What competitive advantages are they claiming? Write as flowing prose, not bullets.]

**New vs. Known:**

| New / Updated | Previously Known |
|---------------|------------------|
| [New insight 1 with slide ref] | [Known item 1] |
| [New insight 2] | [Known item 2] |
| [New insight 3] | [Known item 3] |

*Critical for assessing event value — is this genuinely new or just repetition?*

**Strategic Priorities (Ranked):**

| # | Priority | Evidence of Commitment |
|---|----------|------------------------|
| 1 | [Priority] | [Specific investment, resource allocation, or milestone] (Slide XX) |
| 2 | [Priority] | [Evidence] |
| 3 | [Priority] | [Evidence] |

---

## Guidance & Targets

| Metric | Target | Timeline | Specificity | Source |
|--------|--------|----------|-------------|--------|
| [Metric 1] | [Value/Range] | [By when] | High/Med/Low | Slide XX |
| [Metric 2] | [Value/Range] | [By when] | High/Med/Low | Slide XX |

*Specificity: High = explicit number, Med = range or directional, Low = qualitative only*

**Non-Operating Income (if material):**

[If presentation discloses significant non-operating income streams (equity method income, investment income, JV income), list them here with amounts. These are often material earnings drivers overlooked in operating analysis.]

**Capital Allocation:**

[2-3 sentences on capital allocation priorities as presented. Include: dividend policy, buyback authorization/deployment, M&A appetite, stated priorities in order.]

---

## Promises to Track

*Verbatim quotes with source references. These feed into management credibility audits.*

| Promise | Verbatim Quote | Source | Timeline | Category |
|---------|----------------|--------|----------|----------|
| [Short description] | "[Exact quote]" | Slide XX | [By when] | Financial/Operational/Strategic/Capital |
| [Short description] | "[Exact quote]" | Slide XX | [By when] | |
| [Short description] | "[Exact quote]" | Slide XX | [By when] | |

*Minimum 3 trackable promises. If fewer, state: "Limited specific commitments — event was primarily [informational/retrospective]."*

---

## Claims to Verify

*Competitive claims requiring external validation.*

| Claim | Verbatim Quote | Source | Verifiability | How to Verify |
|-------|----------------|--------|---------------|---------------|
| [Short description] | "[Exact quote]" | Slide XX | Strong/Moderate/Weak | [Data source] |
| [Short description] | "[Exact quote]" | Slide XX | | [Data source] |

*Verifiability: Strong = public data available, Moderate = requires research, Weak = no clear verification path*

---

## Business Updates by Segment

### [Segment 1]

- **Performance:** [Key metrics presented] (Slide XX)
- **Outlook:** [Forward commentary]
- **Key Initiatives:** [Specific projects or investments]

### [Segment 2]

- **Performance:** [Key metrics]
- **Outlook:** [Forward commentary]
- **Key Initiatives:** [Specific projects]

*Repeat for each segment discussed. Omit section if no segment-level detail.*

---

## Red Flags & Concerns

Write 2-4 prose bullets covering concerns. Include your interpretation — is this real or minor?

- **[Concern name]:** [What triggered this concern, evidence, severity assessment (high/medium/low). Include slide reference if applicable.]

- **[Concern name]:** [Continue with material concerns only.]

**Unanswered Questions:**

1. **[Question]?** — [Why it matters]
2. **[Question]?** — [Why it matters]
3. **[Question]?** — [Why it matters]

*What wasn't addressed that should have been?*

---

## Investment Implications

**For Current Holders:**

[1-2 paragraphs on what this event means for existing shareholders. Does this confirm or change the thesis? What should be monitored going forward?]

**For Prospective Investors:**

[1-2 paragraphs on what this event signals for potential entry. Key risks to understand, entry timing considerations.]

---

## Source

- **Event:** [Full event name]
- **Date:** [Event date]
- **Company:** [Company] ([TICKER])
- **Files:** [List each file name]
- **Synthesized:** [YYYY-MM-DD]
