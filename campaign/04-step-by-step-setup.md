# Step-by-Step Setup Guide
> Orden recomendado. Tiempo total estimado: **45-60 minutos**.

## STEP 0 — Lo que necesitas a mano
- Acceso a tu cuenta de **Google Ads** (modo Expert, no Smart).
- Acceso a tu **propiedad GA4**.
- **Google Ads Editor** instalado (descarga gratis: https://ads.google.com/intl/en/home/tools/ads-editor/).
- Carpeta `D:\IRONHACK\Landing\campaign\csv\` (ya creada).

---

## STEP 1 — Vincular GA4 ↔ Google Ads (3 min)
Hazlo primero. Si lo haces después, las conversiones no se importarán bien.

1. GA4 → ⚙️ **Admin** → **Product links** → **Google Ads links** → `Link`.
2. Selecciona tu cuenta de Ads → `Next`.
3. Activa **"Enable Personalized Advertising"** y **"Enable auto-tagging"** → `Next` → `Submit`.
4. Verifica en Ads: **Tools → Linked accounts → Google Analytics (GA4)** debe mostrar "Linked".

---

## STEP 2 — Crear el Key Event en GA4 (5 min)
1. GA4 → **Admin** → **Events** → busca `generate_lead`. Si no aparece (porque nadie ha submiteado todavía), haz un test submit en tu landing y espera 1-2 min.
2. Toggle **"Mark as key event"** ON.
3. Opcional: hazlo también para `cta_click`.

---

## STEP 3 — Crear las audiencias GA4 (10 min)
Sigue la tabla del documento `03-ga4-measurement-plan.md`, sección 4.

Por cada audiencia:
1. GA4 → **Admin** → **Audiences** → `+ New audience` → `Create a custom audience`.
2. Pega el nombre y configura los `Include / Exclude` según la tabla.
3. Set membership duration → Save.

⏱️ Las audiencias tardan **24-48h** en poblarse y aparecer en Ads.

---

## STEP 4 — Crear la conversión en Google Ads (5 min)
Usaremos **Opción A: importar desde GA4**.

1. Google Ads → **Tools** → **Conversions** → `+ New conversion action`.
2. Source: **Import** → **Google Analytics 4 properties** → **Web** → `Continue`.
3. Marca ☑ `generate_lead` → `Import and continue`.
4. Click en la conversión recién creada → **Edit settings**:
   - Value: **Use the value from the event** (la landing manda €50).
   - Count: **One**.
   - Click-through window: **30 days**. View-through: **1 day**. Engaged-view: **3 seconds**.
   - Attribution: **Data-driven**.
   - Include in "Conversions": ✅ (es nuestra Primary).
5. Save.

---

## STEP 5 — Activar Enhanced Conversions (2 min)
1. En la misma conversion action → scroll a **Enhanced conversions**.
2. Toggle **ON** → Method: **Google tag (gtag.js)** → URL: `https://sanchezespinosa1998.github.io/IAeventlanding/`.
3. Agree to terms → Save.

(Tu landing ya envía `sha256_email_address` y `sha256_first_name`, así que no hay que tocar código.)

---

## STEP 6 — Importar la campaña con Google Ads Editor (10 min)

Esto es lo que te ahorra hora y media de clicks manuales.

1. Abre **Google Ads Editor** → conecta tu cuenta → `Get recent changes` (descarga el estado actual).
2. Menu **Account → Import → From file...** → selecciona `D:\IRONHACK\Landing\campaign\csv\01-campaign.csv`.
3. En el diálogo de import, revisa que detecte: 1 Campaign created → `Apply selected changes`.
4. Repite el import para cada CSV en orden:
   - `02-adgroups.csv` → 3 ad groups creados
   - `03-keywords.csv` → 35 keywords creadas
   - `04-ads.csv` → 3 RSAs creados
   - `05-sitelinks.csv` → 4 sitelinks (asocia al campaign-level)
   - `06-callouts.csv` → 6 callouts
   - `07-negatives.csv` → 20 keywords negativas
5. Revisa errores en la columna de la izquierda (validación local antes de subir).
6. **Post Changes** (botón arriba a la derecha) → confirma → Editor sube todo a Ads.

⚠️ Cuando Editor pregunte por **Conversion goal** asegúrate de seleccionar solo `generate_lead` (no "All conversions").

---

## STEP 7 — Verificación final (5 min)
1. Ads → **Campaigns** → tu campaña debe aparecer en **Paused** (correcto, no queremos gastar para el ejercicio).
2. Ads → **Recommendations** → revisa avisos. Ignora cualquiera que diga "expand to broad match" o "add Search Partners".
3. Ads → **Ads & assets** → **Ads**: los 3 RSAs deben tener **Ad strength = Good** mínimo. Si alguno está "Average", añade headlines más diversos.
4. **Tag Assistant** (extensión Chrome) en la landing → confirma GTM + GA4 + AW disparando.
5. **GA4 DebugView**: hace un test submit con `?gtm_debug=1` → ves `generate_lead` con todos los parámetros.

---

## STEP 8 — Listo para entregar
La campaña queda **Paused** (cero gasto). Pero todo está configurado y un instructor puede:
- Ver la estructura completa
- Inspeccionar copies, keywords, extensiones
- Validar tracking via Tag Assistant
- Activarla con un click si quiere ver tráfico real

**Si en algún momento quieres lanzarla:** Campaign → status toggle to **Enabled**. Empieza a gastar ~€27/día y verás impresiones en 1-3h.

---

## Troubleshooting rápido
| Síntoma | Probable causa | Fix |
|---------|----------------|-----|
| "No se importa la conversión desde GA4" | GA4 link no activo aún | Vuelve a Step 1, espera 24h |
| "Ad disapproved: trademark" | Mencionaste Vendelux/Feathr en headline | Ya está prevenido — copy AG3 no usa marcas |
| "Final URL doesn't match display URL" | Mismatch dominio en path | El path 1/2 es texto, no URL — está bien |
| Ad strength "Poor" | Pocos headlines únicos | Añade variaciones, usa más palabras de keywords |
| No impresiones tras 48h activa | Bid demasiado bajo o KW sin volumen | Sube Max CPC en ad group o usa Maximize Conv. |
