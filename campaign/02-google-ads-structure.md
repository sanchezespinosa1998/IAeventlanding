# Google Ads — Campaign Structure (Search · Spain · EN)

> Lanza la campaña en modo **paused** para el ejercicio. No se gastará un céntimo hasta que la actives.

## Campaign-level settings
| Setting | Value | Why |
|---------|-------|-----|
| Name | `EventAI - Search - ES - EN` | Naming convention: `Brand - Type - Geo - Lang` |
| Campaign type | Search | Bottom-of-funnel intent |
| Networks | Google Search only (uncheck Search Partners + Display) | Avoid low-quality impressions on Day 1 |
| Locations | Spain — *People in or regularly in your targeted locations* | Avoids tourists/translators searching outside Spain |
| Languages | English + Spanish | English-speaking buying committee but session language can vary |
| Daily budget | €27 (= €825/mo) | 55% of monthly working budget |
| Bid strategy | **Maximize Conversions** (no tCPA yet — needs ≥30 conv to optimize) | Switch to tCPA €100 after 30 conversions |
| Ad rotation | Optimize for conversions | Default — let Google's ML pick winners |
| Ad schedule | All days, 24h initially → review after 2 weeks | Need data to know peak hours |
| Audience signals | Observation: In-market — *Business Services > Marketing Software* | Observe but don't restrict |
| Conversion goal | `generate_lead` only (set as Primary) | Don't optimize toward soft events |

## Ad group structure (3 ad groups)

### AG1 — Event ROI Analytics (high-intent, bottom funnel)
**Theme:** People searching for how to measure/prove event ROI.
**Final URL:** https://sanchezespinosa1998.github.io/IAeventlanding/?utm_source=google&utm_medium=cpc&utm_campaign=eventai_search_es&utm_content=ag_event_roi&utm_term={keyword}

### AG2 — B2B Event Marketing (category, mid-funnel)
**Theme:** Generic "event marketing software / B2B event tools" queries.
**Final URL:** ...&utm_content=ag_b2b_event_marketing&utm_term={keyword}

### AG3 — Competitor Alternatives (high-intent, comparison)
**Theme:** "vendelux alternative / feathr alternative / cvent alternative" — buyers in eval mode.
**Final URL:** ...&utm_content=ag_competitors&utm_term={keyword}
**Important:** Never use competitor trademarks in ad text (Google will disapprove). Bid on as keywords ✅, write in copy ❌.

## Extensions (asset-level)

### Sitelinks (4)
| Text (≤25 ch) | Description line 1 (≤35) | Description line 2 (≤35) | Final URL anchor |
|----------|-------------------|-------------------|-------|
| AI ICP Filtering | Find ideal customers at events | Powered by AI lead scoring | `/#features` |
| Compare to Alternatives | See feature-by-feature breakdown | EventAI vs. legacy tools | `/#comparison` |
| Request Demo | See EventAI live in 20 minutes | Free, no commitment | `/#form` |
| Predictive ROI | Forecast event ROI in advance | Stop guessing event impact | `/#features` |

### Callout extensions (6)
- AI-Powered Lead Scoring
- Predictive ROI Modeling
- Enterprise-Grade Analytics
- CRM & MAP Integration
- Built for B2B Event Teams
- Free Demo - No Commitment

### Structured snippets (1)
- **Header:** Features
- **Values:** ICP Filtering, ROI Analytics, ABM Insights, Predictive Modeling, CRM Integration

### Lead form extension (optional but recommended)
- CTA: "Request demo"
- Headline: "See EventAI in 20 minutes"
- Description: "AI event analytics that prove ROI for B2B marketing teams"
- Privacy policy URL: https://sanchezespinosa1998.github.io/IAeventlanding/ (placeholder — replace with real privacy URL before publishing)

## Bidding & quality
- Initial Max CPC ceiling not needed (Maximize Conversions auto-bids).
- Expected first-week CPC range: €1.20 – €3.80 depending on ad group.
- Quality Score levers we've already pulled:
  - Landing speed (single-page, no heavy JS)
  - Message match (headlines mention "Event ROI" / "B2B Event Marketing" — same terms as KWs)
  - Mobile responsive
  - Working form
