# Eruvpedia

Mapa interactivo mundial de **eruvs** (perímetros del eruv judío) para la comunidad judía y el público en general. Permite localizar dónde hay eruvs documentados, filtrar por estado y contribuir nuevos datos de forma abierta.

## Datos y metodología

- [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md): cómo se obtuvo cada perímetro (pipeline por tipo de fuente, validación, ética, limitaciones).
- [`data/SOURCES.md`](data/SOURCES.md): fuentes y atribución por lote; [`data/MISSING.md`](data/MISSING.md): eruvs sin perímetro y qué documento haría falta.
- [`scripts/pipeline/`](scripts/pipeline/README.md): scripts usados; [`data/sources-raw/MANIFEST.md`](data/sources-raw/MANIFEST.md): URLs de origen y hashes (no se redistribuyen los originales).

## Instalación

Requisitos: **Node.js 20+** y npm.

```bash
git clone https://github.com/JuanCarlosGP/eruvMap.git
cd eruvMap
npm install
cp .env.example .env
# Edita .env y añade tu token público de Mapbox
npm run dev
```

La aplicación estará disponible en `http://localhost:5173` (puerto por defecto de Vite).

## Variables de entorno

| Variable | Descripción |
|----------|-------------|
| `VITE_MAPBOX_TOKEN` | Token **público** de [Mapbox](https://account.mapbox.com/access-tokens/). Necesario para el mapa y la búsqueda por geocoding. |
| `VITE_BASE_PATH` | Ruta base de Vite (por defecto `/`). El workflow de GitHub Pages la fija en `/eruvMap/`. |

No subas el archivo `.env` al repositorio. Usa `.env.example` como referencia.

## Sitio publicado

La app está en **https://eruvpedia.com**. Cloudflare sirve el Worker `eruv` en ese dominio y en `www.eruvpedia.com`.

## Despliegue en GitHub Pages

El workflow de GitHub Pages sigue publicando una copia en:

**https://juancarlosgp.github.io/eruvMap/**

### Configuración del repositorio

1. En **Settings → Pages**, el origen debe ser **GitHub Actions** (no la rama `gh-pages`).
2. En **Settings → Secrets and variables → Actions → Variables**, crea la variable de repositorio:
   - `VITE_MAPBOX_TOKEN` — token **público** de Mapbox (el mismo que usarías en `.env` local).

El workflow [`.github/workflows/pages.yml`](.github/workflows/pages.yml) compila en cada push a `main` (y también con **Run workflow** manual), sube el artefacto y despliega con `deploy-pages`.

### Base path (`/eruvMap/`)

El repositorio se llama `eruvMap`, así que GitHub Pages sirve el sitio bajo el subpath `/eruvMap/`. Vite usa `base: '/eruvMap/'` (configurable con `VITE_BASE_PATH`). Los assets de `public/` (p. ej. `favicon.svg`) y el GeoJSON empaquetado desde `data/eruvs.geojson` respetan esa base en el build.

Para probar el mismo layout en local:

```bash
VITE_BASE_PATH=/eruvMap/ npm run build
npm run preview
# Abre http://localhost:4173/eruvMap/
```

El build genera además `404.html` (copia de `index.html`) para que GitHub Pages devuelva la SPA en rutas no encontradas.

### Restringir el token de Mapbox por URL

Como el token es público en el cliente, conviene limitarlo en [Mapbox → Access tokens](https://account.mapbox.com/access-tokens/):

1. Edita el token usado en producción.
2. En **URL restrictions**, añade por ejemplo:
   - `https://eruvpedia.com/*`
   - `https://www.eruvpedia.com/*`
   - `https://juancarlosgp.github.io/*`
3. Guarda y usa ese token en la variable `VITE_MAPBOX_TOKEN` del repositorio.

Puedes añadir también `http://localhost:*` para desarrollo local con el mismo token, si Mapbox lo permite en tu cuenta.

## Scripts

| Comando | Uso |
|---------|-----|
| `npm run dev` | Servidor de desarrollo |
| `npm run build` | Compilación de producción |
| `npm run preview` | Vista previa del build |
| `npm run lint` | Linter (oxlint) |
| `npm run typecheck` | Comprobación de tipos TypeScript |
| `npm run validate:geojson` | Valida `data/eruvs.geojson` |

## Estructura del proyecto

```
├── data/
│   ├── eruvs.geojson      # Datos de eruvs (GeoJSON)
│   └── SOURCES.md         # Fuentes, métodos y atribución OSM
├── scripts/
│   └── validate-geojson.mjs
├── src/
│   ├── components/        # Mapa, barra de herramientas, panel de detalle
│   ├── i18n/              # Traducciones HE / EN
│   ├── lib/               # Utilidades de geometría y mapa
│   ├── theme/             # Tema claro / oscuro
│   └── types/             # Tipos del esquema de datos
├── .github/
│   ├── workflows/ci.yml
│   ├── workflows/pages.yml
│   └── ISSUE_TEMPLATE/nuevo_eruv.yml
└── .env.example
```

## Esquema de datos (`data/eruvs.geojson`)

Cada feature incluye `properties.id` (único) y:

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `name_en` | string | Nombre en inglés |
| `name_he` | string (opc.) | Nombre en hebreo |
| `city` | string | Ciudad o zona |
| `country` | string | País |
| `geometry_kind` | `"perimeter"` \| `"point"` | Perímetro o punto representativo |
| `status` | `"active"` \| `"unknown"` | Estado conocido |
| `source` | string | Descripción de la fuente |
| `source_url` | string | URL de la fuente |
| `license` | string | Licencia (p. ej. ODbL OSM) |
| `verified_at` | string | Fecha de verificación (ISO) |
| `contact_url` | string (opc.) | Enlace comunitario |
| `geometry_precision` | `"exact"` \| `"approximate"` | Exactitud de la geometría |
| `note` | string (opc.) | Notas (p. ej. segmentos parciales) |
| `state` | string (opc., US) | Código de estado EE. UU. (p. ej. `NY`) |
| `official_boundary_map` | string (opc.) | Descripción del mapa oficial de límites |
| `boundary_map_url` | string (opc.) | URL del mapa oficial de límites |
| `stated_terms` | string (opc.) | Términos citados en la fuente |
| `hotline_or_contact` | string (opc.) | Teléfono o contacto de estado |
| `status_as_of` | string (opc.) | Fecha de estado indicada por la comunidad |
| `evidence` | string (opc.) | Nota de verificación / método |
| `coordinate_source` | string (opc.) | Origen de las coordenadas (p. ej. Nominatim) |
| `extra_note` | string (opc.) | Aclaración adicional |

Geometría: `Polygon` / `LineString` / `MultiLineString` para `perimeter`; `Point` para `point` (siempre `approximate`). Los perímetros con `note` que indique *partial* se dibujan como línea, sin relleno de polígono.

Validación: `npm run validate:geojson`.

## Atribución y fuentes

Los perímetros y muchas coordenadas proceden de **OpenStreetMap** (ODbL 1.0). La aplicación muestra la atribución en el pie de página y en el control de atribución del mapa (Mapbox).

- Detalle del dataset, métodos y limitaciones: [`data/SOURCES.md`](data/SOURCES.md).
- Texto requerido: *Contains data © OpenStreetMap contributors, ODbL 1.0* — [openstreetmap.org/copyright](https://www.openstreetmap.org/copyright).

## Contribuir

**Nada se publica sin revisión.** Flujo completo en [`CONTRIBUTING.md`](CONTRIBUTING.md).

1. En el sitio, pulsa **«Proponer eruv»** (hebreo/inglés): dibuja polígono, línea o punto en el mapa, rellena el formulario y opcionalmente adjunta una foto de verificación (solo se usa la ubicación en el navegador; la imagen no se sube al servidor).
2. **Enviar** abre un [issue con plantilla](https://github.com/JuanCarlosGP/eruvMap/issues/new?template=nuevo_eruv.yml) (etiqueta `propuesta`) con GeoJSON y metadatos; arrastra la foto al issue en GitHub.
3. **Descargar GeoJSON** guarda la propuesta localmente con nota de atribución.
4. Un mantenedor revisa la fuente y, si procede, integra el feature en `data/eruvs.geojson` (`npm run validate:geojson`) y despliega vía GitHub Pages.

## Hoja de ruta

- [ ] Ampliar cobertura con datos verificados por comunidad
- [ ] Historial de cambios por eruv (fechas y fuentes)
- [ ] Exportar perímetro (GeoJSON / KML)
- [ ] Modo sin conexión básico (PWA)
- [ ] API o feed RSS para integraciones comunitarias
- [ ] Revisión colaborativa de geometrías (diff en PR)

## Licencia

Por definir. Los datos de terceros deben respetar sus licencias y permisos.

## Aviso

**Eruvpedia** es una herramienta informativa. Antes de confiar en un eruv para halajá, consulta siempre con tu rabino o la autoridad local de tu comunidad.
