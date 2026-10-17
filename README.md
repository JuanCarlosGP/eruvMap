# eruvMap

Mapa interactivo mundial de **eruvs** (perímetros del eruv judío) para la comunidad judía y el público en general. Permite localizar dónde hay eruvs documentados, filtrar por estado y contribuir nuevos datos de forma abierta.

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
| `VITE_BASE_PATH` | Ruta base de Vite (por defecto `/eruvMap/`). Usa `/` en local si prefieres la raíz del dev server. |

No subas el archivo `.env` al repositorio. Usa `.env.example` como referencia.

## Despliegue en GitHub Pages

La app publicada está en:

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

Geometría: `Polygon` / `LineString` / `MultiLineString` para `perimeter`; `Point` para `point` (siempre `approximate`). Los perímetros con `note` que indique *partial* se dibujan como línea, sin relleno de polígono.

Validación: `npm run validate:geojson`.

## Atribución y fuentes

Los perímetros y muchas coordenadas proceden de **OpenStreetMap** (ODbL 1.0). La aplicación muestra la atribución en el pie de página y en el control de atribución del mapa (Mapbox).

- Detalle del dataset, métodos y limitaciones: [`data/SOURCES.md`](data/SOURCES.md).
- Texto requerido: *Contains data © OpenStreetMap contributors, ODbL 1.0* — [openstreetmap.org/copyright](https://www.openstreetmap.org/copyright).

## Contribuir

1. Abre un issue con la plantilla [**Proponer un eruv**](https://github.com/JuanCarlosGP/eruvMap/issues/new?template=nuevo_eruv.yml) e incluye geometría y fuente verificable.
2. Tras revisión, un mantenedor añadirá el feature a `data/eruvs.geojson`.
3. Ejecuta `npm run validate:geojson` antes de enviar cambios en los datos.

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

**eruvMap** es una herramienta informativa. Antes de confiar en un eruv para halajá, consulta siempre con tu rabino o la autoridad local de tu comunidad.
