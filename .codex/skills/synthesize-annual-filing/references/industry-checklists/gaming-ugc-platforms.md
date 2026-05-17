# Gaming / UGC Platforms — Mandatory Checklist

**CRITICAL:** Every item must be addressed (found and included, OR explicitly noted as "not disclosed").

**Applies to:** Gaming platforms, UGC (user-generated content) platforms, virtual worlds, creator economies (Roblox, Unity, AppLovin, Epic Games, potentially Discord/Twitch)

---

## Why This Industry Is Different

Gaming/UGC platforms have fundamentally different economics than transaction-based platforms (exchanges, OTAs):

1. **Engagement-first model:** Value creation measured by time spent, not transactions completed
2. **Deferred revenue:** Virtual currency purchases create liability; revenue recognizes over estimated user lifetime
3. **Two-sided creator marketplace:** Platform health depends on both users AND content creators
4. **Heavy SBC:** High stock-based compensation often obscures true profitability

---

## YAML Frontmatter Metrics (Required)

```yaml
metrics:
  # Standard (always required)
  revenue_m: [number]
  operating_income_m: [number]
  net_income_m: [number]
  fcf_m: [number]
  employees: [number]

  # Engagement (REQUIRED)
  bookings_m: [number]                # Cash received (=/= revenue)
  dau_m: [number]                     # Daily Active Users (millions)
  mau_m: [number or null]             # Monthly Active Users (if disclosed)
  hours_engaged_b: [number or null]   # Total engagement hours (billions)
  hours_per_dau: [number or null]     # Daily hours per user

  # Monetization (REQUIRED)
  abpdau: [number or null]            # Avg Bookings Per DAU (clarify: annual $ or daily cents)
  arpdau: [number or null]            # Avg Revenue Per DAU (if disclosed)
  payer_conversion_pct: [number or null]  # Daily unique payers / DAU

  # Deferred Revenue (REQUIRED)
  deferred_revenue_m: [number]        # Unearned revenue balance
  deferred_revenue_change_m: [number] # YoY change
  bookings_to_revenue_pct: [number]   # Revenue / Bookings (recognition rate)

  # Creator Economics (REQUIRED for two-sided platforms)
  developer_exchange_fees_m: [number or null]  # Payouts to creators
  creator_payout_pct: [number or null]         # Dev exchange / Bookings
  qualified_creators: [number or null]         # Creators earning income
  active_experiences_m: [number or null]       # Content items on platform

  # Cost Structure
  sbc_m: [number]                     # Stock-based compensation
  sbc_pct_of_revenue: [number]        # SBC / Revenue (flag if >15%)
  adjusted_ebitda_m: [number or null] # Primary profitability metric
```

---

## Key Metrics Extraction

### A. Engagement Metrics (REQUIRED)

- [ ] **DAU (Daily Active Users)** — Core engagement metric with YoY change
- [ ] **MAU (Monthly Active Users)** — If disclosed; calculate DAU/MAU ratio for stickiness
- [ ] **Hours Engaged** — Total platform engagement hours with YoY change
- [ ] **Hours per DAU** — Engagement intensity (hours engaged / DAU / 365). **Include YoY change.** Flag declining trend.
- [ ] **Geographic DAU mix** — North America, Europe, APAC, ROW breakdown
- [ ] **Age demographics** — If disclosed (critical for child safety risk assessment)

**Search terms:** "daily active users", "DAU", "hours engaged", "engagement", "monthly active users", "MAU"

---

### B. Monetization Metrics (REQUIRED)

- [ ] **Bookings** — Cash received from users (NOT revenue) with YoY change
- [ ] **ABPDAU** — Average Bookings Per DAU. Clarify units (annual $ or daily cents).
- [ ] **ARPDAU** — Average Revenue Per DAU (if disclosed separately from ABPDAU)
- [ ] **Payer conversion rate** — Daily unique payers / DAU as percentage

**CRITICAL — Bookings vs. Revenue Growth Differential (REQUIRED):**
Calculate and explicitly state: "Revenue grew X% vs. Bookings Y% = bookings-to-revenue ratio [expanding/compressing]."
- If Revenue > Bookings growth: Platform releasing deferred revenue (may mask slowdown)
- If Bookings > Revenue growth: Strong current demand, deferred revenue building
- Include in Key Takeaways with explicit percentages

**Search terms:** "bookings", "ABPDAU", "ARPDAU", "paying users", "payer", "monetization"

---

### C. Deferred Revenue Dynamics (REQUIRED)

- [ ] **Deferred revenue balance** — Current liability with YoY change
- [ ] **Bookings-to-revenue ratio** — Revenue / Bookings as percentage. Include 3-year trend if available.
- [ ] **Estimated paying user lifetime** — Management's assumption for revenue deferral period
- [ ] **Deferred revenue as % of trailing bookings** — Indicator of revenue recognition timing

**Key Insight:** Deferred revenue mechanics are central to understanding gaming platform financials.
- Longer estimated user lifetime = slower revenue recognition = higher deferred revenue balance
- Changes to lifetime estimates can materially impact revenue recognition

**Search terms:** "deferred revenue", "estimated paying user lifetime", "average lifetime", "revenue recognition"

---

### D. Creator Economics (REQUIRED for Two-Sided Platforms)

- [ ] **Developer Exchange Fees** — Cash paid to creators with YoY change
- [ ] **Creator payout ratio** — Dev exchange / Bookings as percentage. Include 3-year trend.
- [ ] **Qualified creators** — Number of creators earning income (threshold definition matters)
- [ ] **Active experiences/content** — Total content items on platform

**Creator Economics Growth Differential:**
Calculate and explicitly state: "Dev exchange grew X% vs. revenue Y%."
- If Dev exchange > Revenue growth: Platform investing in creator ecosystem
- If Dev exchange < Revenue growth: Platform taking larger share (margin expansion but supply risk)

**Search terms:** "developer exchange", "creator", "developer", "payout", "content creator"

---

### E. Platform Cost Structure (REQUIRED)

- [ ] **Infrastructure costs** — Hosting, bandwidth, compute costs
- [ ] **Payment processing fees** — Third-party payment costs
- [ ] **Content moderation / Trust & Safety** — Growing cost center; search for headcount or spend
- [ ] **App store fees** — Platform fees to Apple/Google. Note % of revenue from mobile.

**SBC Analysis (REQUIRED — Must Include All Three):**
1. **SBC $ amount** — Total stock-based compensation expense
2. **SBC as % of revenue** — Flag if >15% (dilution concern)
3. **SBC vs. Adjusted EBITDA** — If SBC > Adjusted EBITDA, company is truly unprofitable

Format in memo: "SBC: $XXM (XX% of revenue, X.Xx Adjusted EBITDA)"

**Search terms:** "stock-based compensation", "share-based", "infrastructure", "trust and safety", "App Store", "Google Play"

---

## Watch Items (REQUIRED Evaluation)

**For each Watch Item, explicitly assess in Risk Factors or Key Takeaways:**

| Category | Watch Item | Red Flag Threshold |
|----------|------------|-------------------|
| **Engagement** | DAU growth decelerating | 2+ consecutive periods |
| **Engagement** | Hours per DAU declining | YoY decline |
| **Monetization** | ABPDAU declining | YoY decline (pricing power concern) |
| **Monetization** | Revenue > Bookings growth | 2+ periods (deferred revenue release masking slowdown) |
| **Creator** | Creator payout ratio declining | Platform taking larger share |
| **Creator** | Qualified creator count flat/declining | Supply-side weakness |
| **Profitability** | SBC >20% of revenue | Significant dilution concern |
| **Profitability** | SBC > 2x Adjusted EBITDA | True losses hidden by non-GAAP |
| **Platform** | >80% mobile revenue, no alternative payments | App store dependency risk |

**Output Requirement:** Include explicit assessment of at least 3 Watch Items in Key Takeaways or Risk Factors.

---

## Risk Factors to Search (ACTIVELY SEARCH FOR)

### Child Safety / Content Moderation

- [ ] **COPPA compliance** — Search: "COPPA", "children", "minors", "age verification", "child safety"
- [ ] **DSA / Online Safety Act** — Search: "DSA", "Digital Services Act", "Online Safety Act", "online harms"
- [ ] **Moderation capabilities** — Search: "moderation", "trust and safety", "content policy", "community standards"
- [ ] **Litigation / investigations** — Search: "FTC", "investigation", "lawsuit", "privacy"

*Child safety is existential risk for platforms with young user bases.*

### App Store Dependency

- [ ] **Apple App Store risk** — Search: "Apple", "App Store", "iOS", "30%", "in-app purchase", "App Tracking Transparency"
- [ ] **Google Play Store risk** — Search: "Google", "Play Store", "Android", "platform policy"
- [ ] **Alternative payment options** — Search: "direct billing", "web payments", "alternative payment"
- [ ] **Platform policy changes** — Search: "developer agreement", "platform terms"

*Quantify: What % of revenue flows through mobile app stores?*

### Competitive / Regulatory

- [ ] **Competition from established players** — Search: "Fortnite", "Minecraft", "Epic", "competition", "competitor"
- [ ] **Gambling / loot box regulation** — Search: "gambling", "loot box", "random item", "gacha"
- [ ] **China restrictions** — Search: "China", "restrictions", "blocked", "international"
- [ ] **AI disruption** — Search: "artificial intelligence", "AI", "generative", "machine learning"

---

## Conditional Sections

### Mobile Gaming / Ad Networks (AppLovin, Unity Ads, ironSource)

If advertising is a significant revenue stream:

- [ ] **Advertising revenue** — $ amount and % of total revenue
- [ ] **eCPM trends** — Effective cost per thousand impressions
- [ ] **ROAS metrics** — Return on ad spend for advertisers
- [ ] **Install base / DAU for ad-supported games**
- [ ] **Retention curves** — D1, D7, D30 if disclosed

### Game Engine / Developer Tools (Unity, Unreal)

If developer tools are core business:

- [ ] **Subscription seats / developers** — License count and growth
- [ ] **Consumption revenue** — Runtime fees, cloud services
- [ ] **Monthly active developers** — Platform adoption metric
- [ ] **Games shipped using engine** — Market share indicator

### Traditional Gaming Moving to Live Services (EA, Take-Two, Activision)

If transitioning from packaged goods to live services:

- [ ] **Live service bookings** — Full game + extra content
- [ ] **Live service as % of total bookings** — Mix shift indicator
- [ ] **MAU in live services** — Engagement in ongoing titles
- [ ] **New release pipeline** — Upcoming AAA titles

---

## Validation Checklist

Before finalizing the memo, verify:

- [ ] Engagement metrics captured (DAUs, hours engaged, or noted as "not disclosed")
- [ ] **Bookings vs. Revenue growth differential explicitly calculated and stated**
- [ ] Deferred revenue dynamics explained (balance, change, lifetime estimate if disclosed)
- [ ] Creator economics captured (dev exchange, payout ratio) or marked N/A for single-sided platforms
- [ ] **SBC analysis complete ($ amount, % of revenue, comparison to Adjusted EBITDA)**
- [ ] Platform dependency risks flagged (app store %, mobile concentration)
- [ ] Child safety risks assessed (if platform has young user demographic)
- [ ] **DSA/regulatory investigations flagged** — If DSA, OSA, or regulatory investigation mentioned, include in Risk Factors
- [ ] Watch Items explicitly evaluated (minimum 3 in Key Takeaways or Risk Factors)
- [ ] All YAML metrics populated (use `null` for undisclosed)
