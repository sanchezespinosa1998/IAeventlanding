# Presentation Outline — Ironhack Project 2 (15-20 slides)

> Sigue este esquema y cubres el 100% del rubric (Strategy 25% + Implementation 25% + Creative 20% + Analytics 15% + Quality 15%).

## Slide 1 — Title
- **EventAI · Outbound Paid Media Strategy**
- Subtítulo: "AI-driven event analytics for B2B marketing teams"
- Tu nombre · Ironhack Marketing · Date

## Slide 2 — Executive Summary (1 minuto)
- Producto: EventAI (B2B SaaS)
- Goal: 30 demos/mes a CPL < €120
- Budget: €1,500/mes · Mix: 55% Search · 30% LinkedIn · 10% Display · 5% reserva
- Diferenciador clave: AI ICP filtering + Predictive ROI modeling

## Slide 3 — Buyer Personas refinados
Tabla con 2 personas detalladas (de Project 1, ahora con paid-media angle):
| | Persona A | Persona B |
|---|----------|----------|
| Title | Event Marketing Manager | Director of Demand Gen |
| Pain | "Cannot prove event ROI" | "Manual event lead routing" |
| Channel where they live | Google Search + LinkedIn | LinkedIn + industry blogs |
| Trigger to convert | Free demo | ROI calculator / case study |

## Slide 4 — Campaign Objectives (SMART)
Lista de los 5 SMART objectives del `01-strategy.md` con tabla limpia.

## Slide 5 — Budget Allocation
Pie chart o donut: 55/30/10/5 (Search / LinkedIn / Display / Reserve).
- Justificación bajo del chart: por qué Search pesa más (bottom funnel B2B).

## Slide 6 — Media Mix Strategy (visual)
Diagrama de funnel:
- TOFU → LinkedIn awareness
- MOFU → Google Search (categoría)
- BOFU → Google Search (competitor + brand) + Display remarketing

## Slide 7 — Tracking Infrastructure
Diagrama de arquitectura:
```
Landing (gtag + GTM)
   ├─→ GA4 (events: page_view, cta_click, scroll, generate_lead)
   │     └─→ Audiences → Google Ads (via link)
   └─→ Google Ads (Enhanced Conversions w/ hashed PII)
        └─→ Conversion: generate_lead (€50, 30d window)
```

## Slide 8 — Google Search — Campaign Structure
Pirámide con 1 Campaign → 3 Ad groups:
- AG1 Event ROI Analytics (13 KWs)
- AG2 B2B Event Marketing (12 KWs)
- AG3 Competitor Alternatives (9 KWs)

## Slide 9 — Sample Ad (Creative)
Screenshot mock-up de una SERP con tu RSA + sitelinks + callouts.
Lleva visualmente la palabra "AI" en headline → mensaje match con keyword.

## Slide 10 — Keyword Strategy
Tabla con concordancias usadas (Phrase vs Exact), por qué no Broad (control inicial), y plan de expansión.

## Slide 11 — AI in the workflow (cumple criterio "AI Implementation" del rubric)
- ChatGPT generó variaciones de headlines/descriptions (15+4 por RSA).
- Maximize Conversions bidding = ML de Google.
- Data-Driven Attribution = ML.
- Enhanced Conversions = ML matching.
- (Opcional) Mencionar Performance Max como fase 2.

## Slide 12 — LinkedIn Ads Plan
- Campaign type: Sponsored Content + Lead Gen Forms (no need to land).
- Targeting: Job title (`Event Marketing Manager` OR `Director Demand Gen`) + Company size 200-5000 + Industry (SaaS, FinTech, Cybersecurity).
- Creative: 3 single-image ads + 1 video (15s).
- Budget: €450/mo, daily €15.
- KPI: CPL < €80 (LinkedIn más caro pero más cualificado).

## Slide 13 — Display Remarketing Plan
- Audience: `Engaged - No Lead` (GA4 audience) + `Form Abandoners`.
- Format: 6 responsive display creatives (300x250, 728x90, 160x600, 320x100, 1200x628, square).
- Frequency cap: 3 impressions/user/day, 15/week.
- Bidding: Viewable CPM, cap €4.
- KPI: View-through conversions + assist rate.

## Slide 14 — Automation con Make
Diagrama de workflow:
```
[Google Ads API] ─cada 4h→ [Make] ─→ [Google Sheet]
                                ├─→ Slack alert si CPL > €150
                                ├─→ Pause ad if QS < 4
                                └─→ Weekly digest email
```
Documenta 3-4 escenarios concretos para cumplir "Automation Setup" del rubric.

## Slide 15 — Analytics & Reporting
- GA4 Explorations:
  - Funnel: landing → cta_click → form_field_interaction → generate_lead
  - Path: source/medium → conversion
- Looker Studio dashboard mock (puedes generar con plantilla gratuita "GA4 + Google Ads" de Google).
- KPI dashboard: CPL, CVR, QS, ROAS, Pipeline €.

## Slide 16 — A/B Testing Framework
- Hipótesis 1: "Headlines with 'AI' outperform generic" → Test RSA H1.
- Hipótesis 2: "Lead form on landing vs Lead form extension" → Test 50/50.
- Hipótesis 3: "Value $50 vs $200 in conversion" → Test bidding impact.
- Statistical significance criterion: 95% confidence, ≥100 conv/variant.

## Slide 17 — Expected ROI Analysis
Tabla:
| Channel | Spend | Leads (est.) | CPL | Pipeline € (est.) | ROAS |
|---------|-------|--------------|-----|-------------------|------|
| Search | €825 | 8-10 | €90-100 | €25,000 | 30x |
| LinkedIn | €450 | 5-6 | €75-90 | €18,000 | 40x |
| Display | €150 | 1-2 | €100 | €4,000 | 27x |
| **Total** | **€1,425** | **14-18** | **€95** | **€47,000** | **33x** |

(Pipeline assume €2,500 avg deal × 30% MQL→SQL × 40% close rate. Adjust al sentido común para tu profesor.)

## Slide 18 — Risks & Mitigation
Tabla del `01-strategy.md` sección 7.

## Slide 19 — Implementation Timeline (Gantt)
```
Week 1: Setup (Ads + GA4 + Make)
Week 2: Launch Search · LinkedIn in beta
Week 3-4: Optimize, kill underperformers
Week 5: Launch Display remarketing (need pixel pool)
Week 6: A/B tests
Week 7-12: Scale winners, kill losers, expand keywords
```

## Slide 20 — Demo / Q&A
- Tag Assistant screenshot proving tracking funciona.
- GA4 Realtime screenshot del primer `generate_lead`.
- Link to live landing: https://sanchezespinosa1998.github.io/IAeventlanding/

---

## Appendix slides (no cuentan al límite, súbelos como anexo)
- A1: Full keyword list with match types (table from `03-keywords.csv`).
- A2: All 15 headlines × 3 RSAs (45 headlines + 12 descriptions total).
- A3: Make workflow JSON exports.
- A4: GA4 audience configurations screenshots.
