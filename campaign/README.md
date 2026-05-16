# EventAI · Campaign Deliverables
**Ironhack Project 2 — Outbound Paid Media**

Landing: https://sanchezespinosa1998.github.io/IAeventlanding/

---

## Contents

| File | What it is |
|------|-----------|
| `01-strategy.md` | Plan estratégico, objetivos SMART, ICP, budget, KPIs |
| `02-google-ads-structure.md` | Estructura completa de la Search campaign + copies + extensiones |
| `03-ga4-measurement-plan.md` | Plan GA4: conversiones, audiencias, link a Ads, Enhanced Conversions |
| `04-step-by-step-setup.md` | Guía clic-a-clic para configurar todo (≈45-60 min) |
| `05-presentation-outline.md` | Esquema de las 20 slides para la entrega |
| `csv/01-campaign.csv` | Campaign settings (importar a Google Ads Editor) |
| `csv/02-adgroups.csv` | 3 ad groups |
| `csv/03-keywords.csv` | 35 keywords con UTMs en el Final URL |
| `csv/04-ads.csv` | 3 RSAs (45 headlines + 12 descriptions en total) |
| `csv/05-sitelinks.csv` | 4 sitelinks |
| `csv/06-callouts.csv` | 6 callouts |
| `csv/07-negatives.csv` | 20 keywords negativas |

---

## Orden recomendado para ejecutar

1. **Lee** `01-strategy.md` (5 min) — contexto general.
2. **Sigue** `04-step-by-step-setup.md` paso a paso (45-60 min) — configura Ads + GA4.
3. **Cuando crees la conversión en Google Ads** (Step 4-5 de la guía):
   - Si elegiste **Opción A (importar GA4)** → no necesitas tocar `index.html`. ✅
   - Si elegiste **Opción B (conversión nativa)** → Google te da `AW-XXXXXXXXX` y `CONVERSION_LABEL`. **Pásamelos por chat** y reemplazo en `index.html` (líneas 29, 32, 37 y 849).
4. **Reemplaza también el GA4 Measurement ID** (`G-XXXXXXXXXX`) en `index.html` con el de tu propiedad GA4 (Admin → Data Streams → Web → Measurement ID).
5. **Después del setup** → usa `05-presentation-outline.md` para montar tus 20 slides.

---

## Lo que necesitas darme para terminar

Cuando hayas hecho los Steps 1-5 de `04-step-by-step-setup.md`, mándame por chat:

- **GA4 Measurement ID**: `G-...` (de Admin → Data Streams)
- **Google Ads Conversion ID**: `AW-...` (de Tools → Conversions → tu conversion → tag setup)
- **Google Ads Conversion Label** (solo si elegiste Opción B): un string tipo `AbC-D_efG-h12_34-567`

Con esos 3 valores reemplazo los placeholders en `index.html` en 10 segundos y queda 100% trackeado.

---

## Importante (modo "no se gasta")

La campaña queda en **Paused** tras el import. Cero gasto.

Si tu profe quiere ver tráfico real, pasa Status a **Enabled** un par de días y luego pausa de nuevo. Con €27/día tendrás impresiones en pocas horas.

---

## Lo que NO está cubierto (intencionalmente)

- LinkedIn Ads campaign build: el ejercicio pide *strategy*, no setup. Está en la slide 12 del outline.
- Display creatives: el outline lista los formatos pero las imágenes las generas con Canva / Figma / la herramienta que te pida el curso.
- Make scenarios: outline en slide 14. Si quieres que te genere los JSON exports concretos, dímelo.
