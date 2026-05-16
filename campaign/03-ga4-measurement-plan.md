# GA4 Measurement Plan + Google Ads Conversions

> Tu landing ya envía estos eventos vía GTM + gtag. Aquí defino cuáles son conversiones (Key Events), cuáles audiencias crear, y cómo conectarlas con Google Ads.

## 1. Eventos ya implementados en `index.html`

| Evento (GA4 name) | Trigger | Capa | Marcar como Key Event |
|-------------------|---------|------|----------------------|
| `page_view` | Carga de página | gtag automático | No |
| `cta_click` | Click en "Request Demo" / "Learn More" del hero | gtag custom + dataLayer `hero_cta_click` | Sí (Micro) |
| `form_field_interaction` | Focus en input/select | dataLayer | No (engagement) |
| `scroll_depth` | 25 / 50 / 75 / 100% scroll | dataLayer | No (engagement) |
| `generate_lead` | Submit del form | gtag custom + dataLayer `form_submission` | **Sí (Macro — Primary)** |
| `consent_decision` | Click en banner cookies | dataLayer | No (operacional) |

## 2. Configurar Key Events en GA4

Ruta: **Admin → Events → mark as key event** (lo que antes se llamaba "Conversion").

1. Espera 24h tras publicar la landing para que GA4 detecte los eventos automáticamente, o crea cada evento manualmente:
   - Admin → Events → "Create event" → Name: `generate_lead` → Custom event with `event_name equals generate_lead`.
2. Activa el toggle "Mark as key event" para:
   - ✅ `generate_lead` (Macro)
   - ✅ `cta_click` (Micro — opcional, para optimizar)
3. Verifica en **Realtime → Conversions** que aparecen al rellenar el form en tu landing.

## 3. Configurar la conversión en Google Ads

Ruta: **Google Ads → Tools → Conversions → +New conversion action → Website**.

Hay dos formas, escoge una:

### Opción A (recomendada): Importar desde GA4
Requiere haber vinculado GA4 ↔ Ads primero (ver sección 5).
1. New conversion → "Import" → "Google Analytics 4 properties" → "Web".
2. Selecciona tu propiedad GA4 y marca `generate_lead`.
3. Set value: **Use the value from the GA4 event** (la landing manda `value: 50.0, currency: EUR`).
4. Count: **One** (un demo request por lead, no múltiples).
5. Click-through window: **30 días**. View-through: 1 día.
6. Attribution: **Data-driven**.

✅ Ventaja: una sola fuente de verdad, no necesitas reemplazar `CONVERSION_LABEL` en el HTML.

### Opción B: Crear conversión nativa en Ads (también funciona)
1. New conversion → Manual setup → Category: "Submit lead form".
2. Conversion name: `EventAI - Demo Request`.
3. Value: Use the same value for each conversion → €50.
4. Count: One.
5. Tras crear, Google te dará un **Conversion ID (`AW-XXXXXXXXX`)** y un **Conversion Label** (algo como `AbC-D_efG-h12_34-567`).
6. Pásamelos y reemplazo en `index.html` líneas 37, 38 y 849:
   - `AW-XXXXXXXXX` → tu ID real
   - `CONVERSION_LABEL` → tu label real

## 4. Audiencias a crear en GA4 (para remarketing en Display)

Ruta: **Admin → Audiences → +New audience**.

| Audience | Definition | Duración | Uso |
|----------|-----------|----------|-----|
| `All Visitors` | Include users where `Event count > 0` | 30 días | Pool de remarketing genérico |
| `Engaged - No Lead` | Include `scroll_depth ≥ 50%` AND Exclude `generate_lead` | 30 días | Retargeting principal |
| `Form Abandoners` | Include `form_field_interaction` AND Exclude `generate_lead` | 14 días | Audiencia caliente para Display |
| `Hero CTA Clickers` | Include `cta_click` AND Exclude `generate_lead` | 14 días | Audiencia muy caliente |
| `Converters` | Include `generate_lead` | 90 días | **Excluir** de campañas de adquisición |

Después de crear las audiences en GA4, tras 24-48h aparecerán en Google Ads → Audience manager → "Imported from GA4".

## 5. Vincular GA4 ↔ Google Ads (crítico — hazlo primero)

### Desde GA4
**Admin → Product links → Google Ads links → Link**
1. Choose Google Ads accounts → selecciona tu cuenta de Ads.
2. Configure settings: **Enable Personalized Advertising** ✅.
3. Enable auto-tagging ✅ (esto añade el parámetro `gclid` a las URLs y permite el match Ads ↔ GA4).
4. Submit.

### Desde Google Ads
**Tools → Linked accounts → Google Analytics (GA4) → Details → Link**
- Selecciona la propiedad GA4 y habilita "Import site metrics" (sesiones, bounce rate, etc. aparecerán en columnas de Ads).

### Verificación
- Crea un anuncio de prueba, dale click, abre la landing.
- Mira en GA4 → Realtime → primer "source/medium" debería ser `google / cpc` con un `gclid` largo.

## 6. Enhanced Conversions (ya implementado, solo activar)

Tu `index.html` ya envía `sha256_email_address` y `sha256_first_name` después de cada submit. Solo falta activarlo en Ads:

**Google Ads → Tools → Conversions → click en `generate_lead` → Enhanced conversions → Turn on**
- Method: **Google tag (gtag.js)**.
- URL: tu landing.
- Save.

Google empezará a usar los hashes en ~3-7 días y verás % de "Enhanced conversions" en la columna.

## 7. Validación end-to-end (haz esto antes de dar por buena la setup)

1. **Tag Assistant** (extensión Chrome): abre tu landing → debes ver GTM (`GTM-MHQVDJSJ`), GA4 (`G-...`) y Google Ads (`AW-...`) cargando.
2. **GA4 DebugView** (Admin → DebugView): abre la landing con `?gtm_debug=1`, navega y submite el form. Deberías ver `page_view`, `cta_click`, `generate_lead` en tiempo real con todos los parámetros.
3. **Google Ads diagnostics**: Tools → Conversions → tu conversion action → "Tag setup verified" debe estar verde.
4. **Cross-network test**: añade `?gclid=TEST123` a tu URL, hazte un submit → en GA4 Realtime verás `google / cpc`.

## 8. UTMs (auto-tagging cubre la mayoría, pero úsalos como fallback)

Para canales no-Ads (LinkedIn, manual posts) o si auto-tagging falla:

| Campo | Valor |
|-------|-------|
| utm_source | `google` / `linkedin` / `display` |
| utm_medium | `cpc` / `paid-social` / `display` |
| utm_campaign | `eventai_search_es` / `eventai_linkedin_q2` |
| utm_content | `ag_event_roi` / `lead_gen_form_v1` |
| utm_term | `{keyword}` (en Ads, se sustituye automático) |

Ya vienen aplicados en los Final URLs del CSV `03-keywords.csv`.
