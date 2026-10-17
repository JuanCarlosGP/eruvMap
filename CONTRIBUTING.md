# Contribuir a eruvMap

Gracias por ayudar a ampliar el mapa mundial de eruvs. **Ningún dato se publica sin revisión humana.**

## Flujo de revisión

1. **Propuesta** — Usas la herramienta «Proponer eruv» en el mapa (o abres un issue manualmente con la plantilla *Proponer un eruv*). Se crea un issue en GitHub con etiqueta `propuesta`.
2. **Revisión** — Un mantenedor comprueba la fuente oficial, la geometría, la licencia (p. ej. ODbL si procede de OpenStreetMap) y, si aplica, la coherencia de la foto de verificación (distancia al trazo).
3. **Integración** — Si se acepta, se añade el feature a `data/eruvs.geojson`, se ejecuta `npm run validate:geojson` y se fusiona un PR.
4. **Publicación** — Tras merge en `main`, GitHub Pages vuelve a desplegar el sitio.

Los issues rechazados se cierran con una breve explicación. Puedes corregir y volver a enviar.

## Herramienta en el mapa (sin servidor)

- Dibuja un **polígono**, **línea** (segmento parcial) o **punto aproximado**.
- Completa nombre (EN/HE), ciudad, país y **URL de fuente oficial** obligatoria.
- Opcional: foto de prueba — solo se lee la **ubicación** (EXIF o GPS del navegador); **la imagen no se sube** a eruvMap.
- **Enviar** abre un issue prefilled en GitHub; si el GeoJSON es muy largo, se copia al portapapeles.
- **Descargar GeoJSON** guarda la propuesta en tu equipo con nota de licencia/atribución.

## Requisitos de datos

- No inventes perímetros: cita `source_url` verificable (comunidad, OSM, etc.).
- Geometría en WGS84; coordenadas con sentido (polígonos cerrados).
- Si usas OSM: respeta [ODbL](https://www.openstreetmap.org/copyright) y mantén la atribución.
- `status` solo `active` si la fuente lo confirma; en caso contrario `unknown`.

## Desarrollo local

```bash
npm install
cp .env.example .env   # VITE_MAPBOX_TOKEN
npm run dev
```

Antes de un PR que toque datos:

```bash
npm run validate:geojson
npm run typecheck
npm run build
```

## Código de conducta

Sé respetuoso. No publiques datos personales sin consentimiento.
