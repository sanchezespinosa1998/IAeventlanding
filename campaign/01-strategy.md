# EventAI — Paid Media Strategy
**Ironhack Project 2 · Outbound Marketing**
Landing: https://sanchezespinosa1998.github.io/IAeventlanding/

---

## 1. Executive Summary
EventAI is a B2B SaaS that turns event data into ROI for enterprise event-marketing teams. This paid-media plan focuses **Phase 1 on Google Search** to capture high-intent demand (people actively searching for event-ROI / event-analytics tools), with secondary plans for Paid Social (LinkedIn) and Display retargeting documented for the assignment deliverable.

We prioritize Search because:
- B2B SaaS with a clear category → bottom-of-funnel demand exists on Google.
- Lead form is the conversion → Search delivers MQLs at a knowable CPL.
- Easiest channel to demonstrate full attribution (Ads ↔ GA4 ↔ Enhanced Conversions) for the assignment rubric.

## 2. SMART Objectives (90-day horizon)
| # | Objective | Metric | Target |
|---|-----------|--------|--------|
| O1 | Generate qualified demo requests | `generate_lead` conversions | 30 / month |
| O2 | Keep acquisition cost sustainable | Cost per Lead (CPL) | < €120 |
| O3 | Validate message-market fit | Landing CVR (visits → form submit) | ≥ 3.5% |
| O4 | Build a remarketing pool | GA4 audience size (30-day) | ≥ 2,000 users |
| O5 | Achieve quality keyword traffic | Avg. Quality Score on top 10 KWs | ≥ 7/10 |

## 3. ICP (refined from landing form roles)
**Primary:**
- Event Marketing Manager (decision driver)
- Director of Demand Generation (budget holder)

**Secondary:**
- Marketing Director / VP Marketing (final signoff)
- Director of Field Marketing / ABM Lead

**Firmographics:** B2B companies, 200–5,000 employees, run ≥ 4 corporate events/year, headquartered or operating in Spain with international scope (English-speaking buying committee). Industries: SaaS, FinTech, Cybersecurity, Consulting.

**Pain points (we will speak to in copy):**
1. Cannot prove event ROI to the CFO.
2. Manual lead-scoring after events; ICP fit unclear.
3. Tool-stack fragmentation (CRM + event app + marketing automation).
4. Competing tools (Vendelux, Feathr) lack predictive modeling.

## 4. Budget Allocation (illustrative — campaign will stay paused for the class exercise)
Monthly working budget: **€1,500**

| Channel | % | €/month | Rationale |
|---------|----|---------|-----------|
| Google Search (Brand + Non-brand + Competitors) | 55% | 825 | Highest-intent, MQL-driving |
| LinkedIn Ads (Sponsored Content + Lead Gen Forms) | 30% | 450 | Job-title precision for ICP |
| Display Remarketing (Google Display Network) | 10% | 150 | Re-engage non-converting traffic |
| Reserve / experiments | 5% | 75 | Reallocate based on weekly review |

**Daily Search budget at €825/mo:** ≈ €27/day → set as `daily_budget = 27` in Ads.

## 5. Channel Roles & KPIs
| Channel | Funnel Stage | Primary KPI | Secondary KPI |
|---------|-------------|-------------|---------------|
| Google Search | Bottom | CPL | Quality Score |
| LinkedIn Ads | Middle | CPL (Lead Gen Forms) | Cost per Engaged Account |
| Display Remarketing | Bottom retention | View-through conv. | Frequency cap ≤ 3/day |

## 6. Attribution Model
- **Google Ads:** Data-Driven Attribution (default since 2023).
- **GA4:** Data-Driven + reference comparison vs. Last-Click in Explorations.
- **Cross-channel:** UTMs on every paid link → GA4 `session_source` / `session_medium` dimensions.
- **Enhanced Conversions for Web** (already wired in `index.html`) → hashed email + first-name sent to Google Ads to recover ~5–15% of conversions lost to ITP/cookie blocking.

## 7. Risk & Mitigation
| Risk | Mitigation |
|------|-----------|
| Low search volume on niche KWs | Layer broader category KWs + competitor KWs |
| High CPCs on competitor terms | Cap bids; isolate in own ad group with tighter ad copy |
| Form low-quality leads | Require Work Email; pre-qualify with role dropdown (already in form) |
| Tracking gaps (cookie consent rejection) | Consent Mode v2 already implemented → modeled conversions in GA4 |
