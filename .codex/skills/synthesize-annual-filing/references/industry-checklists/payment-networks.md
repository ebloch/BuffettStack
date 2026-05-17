# Payment Networks — Mandatory Checklist

**Applies to:** Visa, Mastercard, American Express, Discover, PayPal, and similar payment network/processor companies

**CRITICAL:** Every item must be addressed (found and included, OR explicitly noted as "not disclosed").

---

## Industry Classification

Payment networks operate as toll-booth businesses on global commerce. They differ from banks (no credit risk) and platforms (not matching buyers/sellers). Key characteristics:

- **Revenue model:** Fees per transaction, cross-border fees, value-added services
- **Network effects:** More cardholders → more merchants → more cardholders
- **Gross margin:** Near 100% — costs are below the operating line (personnel, technology, incentives)
- **Capital intensity:** Minimal — no loan book, no inventory, no physical assets

---

## Key Metrics

### Volume Metrics (REQUIRED)
- [ ] **Payments volume (or equivalent)** — Total dollar value of transactions processed. In YAML as `payments_volume_b`. Include YoY growth rate.
- [ ] **Processed transactions** — Number of transactions. In YAML as `processed_transactions_b`. Include YoY growth rate.
- [ ] **Payment credentials / cards** — Network reach indicator. In YAML as `payment_credentials_b`.
- [ ] **Merchant acceptance locations** — Network breadth. Note in Business Summary.

### Revenue Components (REQUIRED)
- [ ] **Revenue by type breakdown** — Typically: Service Revenue (volume-based), Data Processing (transaction-based), International/Cross-Border (FX + cross-border), Other/VAS. Include as segment table even if single operating segment.
- [ ] **Client incentives** — Payments to issuers/acquirers. MUST show both gross and net revenue. Flag if incentive growth exceeds volume growth (competitive pressure signal).
- [ ] **Value-Added Services (VAS) revenue** — Growing non-transaction revenue. Note growth rate and % of total net revenue. If company reports multiple VAS definitions, reconcile and note the difference.

### Yield/Take Rate Metrics (REQUIRED)
- [ ] **Revenue vs. volume growth differential** — MUST explicitly state in Key Takeaways: "Net revenue grew X% vs. payments volume Y%, reflecting Z bps yield [expansion/compression]"
- [ ] **Incentive intensity** — Client incentives as % of gross revenue or vs. volume growth. Flag if incentives growing faster than volume.
- [ ] **Cross-border volume growth** — Highest-yield revenue stream. Include growth rate and whether it's driving or lagging total growth.

### Network Health Indicators
- [ ] **Credit vs. debit vs. commercial mix** — Volume breakdown by card type. Note any mix shift.
- [ ] **U.S. vs. international split** — Revenue and/or volume. Note which region is growing faster.
- [ ] **Digital adoption metrics** — Tap-to-pay penetration, mobile wallet adoption, e-commerce penetration if disclosed.
- [ ] **Token metrics** — Number of tokens provisioned, Visa Direct or equivalent P2P/push payment transactions.

---

## Watch Items (Flag If Concerning)

Include a **Watch Items** section in Financial Snapshot with assessment:

- [ ] **Yield/take rate trend:** Expanding / Stable / Compressing — revenue growth vs. volume growth
- [ ] **Client incentive intensity:** Stable / Concerning — incentive growth vs. volume growth
- [ ] **Cross-border recovery:** Healthy / Slowing — cross-border volume and revenue growth
- [ ] **Debit share:** Stable / Under pressure — regulatory and competitive dynamics
- [ ] **VAS penetration:** Expanding / Stable — diversification away from core network fees

---

## Gross Margin Treatment

**Important:** Payment networks typically show ~100% "gross margin" because their costs (personnel, technology, marketing, client incentives) are classified below the gross profit line.

**In the Financial Snapshot P&L table:**
- Either omit Gross Profit / Gross Margin rows entirely, OR
- Note: "Gross Margin: N/A — network model; costs (personnel, technology, incentives) are operating expenses"
- Do NOT show "Gross Profit = Net Revenue" as this implies no COGS when the reality is different accounting treatment

---

## Competitive Landscape

### Direct Network Competitors
- [ ] **Market share data** — If disclosed, reference source (e.g., Nilson Report). Note Visa vs. Mastercard vs. UnionPay positioning.
- [ ] **Competitor comparison table** — If 10-K includes comparison data, extract it.

### Alternative Payment Threats
- [ ] **Real-time payment (RTP) networks** — PIX (Brazil), UPI (India), FedNow (U.S.), SEPA Instant (Europe). Note penetration and company's response.
- [ ] **Stablecoin/crypto competition** — If discussed, note company's positioning (enabler vs. competitor).
- [ ] **Closed-loop systems** — Apple Pay, PayPal, Buy Now Pay Later. Note if gaining share.

---

## Regulatory Risks (ACTIVELY SEARCH FOR)

Payment networks face unique regulatory scrutiny. Search for and flag:

- [ ] **Interchange regulation** — Durbin Amendment (U.S.), IFR (Europe), new proposals. Note impact on debit specifically.
- [ ] **Debit routing rules** — Routing choice expansion to card-not-present transactions.
- [ ] **Antitrust/competition investigations** — DOJ, FTC, EC investigations into network practices.
- [ ] **Data localization** — China, India, Indonesia requirements limiting network access.
- [ ] **Transaction taxes** — FTT proposals that could reduce transaction volumes.

---

## Litigation (REQUIRED IF MATERIAL)

Payment networks often have significant litigation exposure:

- [ ] **Interchange MDL** — For Visa/Mastercard, this is material. Note accrual amount, change YoY, and estimated interchange at issue.
- [ ] **Other class actions** — Merchant suits, consumer suits.
- [ ] **Settlement structures** — For Visa, note the Class A vs. Class B structure and its implications.

---

## Capital Allocation

### Capital Return (REQUIRED)
- [ ] **Share repurchases** — Amount deployed, authorization remaining.
- [ ] **Dividends** — Amount paid, dividend per share, YoY change.
- [ ] **Capital return as % of OCF** — Payment networks typically return 80-100% of OCF.

### Balance Sheet
- [ ] **Net debt position** — Payment networks are often net cash or low leverage.
- [ ] **Share class structure** — For Visa specifically, note Class A vs. Class B shares and preferred stock mechanics.

---

## Questions to Ask

If not answered in the 10-K, add to Questions for Further Research:

1. What is the net take rate trend by product (credit, debit, commercial) and geography?
2. What is the win/loss rate for issuer portfolio renewals (client incentive context)?
3. How does VAS margin compare to core network margin?
4. What is the realistic threat timeline from RTP networks in developed markets?
