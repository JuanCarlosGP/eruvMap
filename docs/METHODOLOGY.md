# Methodology: how each eruv perimeter was obtained

## Resumen (español)
Cada perímetro de `data/eruvs.geojson` es un **trazado aproximado** derivado de un mapa **oficial** publicado por la propia comunidad (nunca de agregadores). Según la fuente: (1) KML de Google My Maps incrustado en la web oficial; (2) GeoJSON/JS o KML publicado por la comunidad; (3) PDF vectorial del que se extraen los trazos; (4) imagen/PDF sin coordenadas, georreferenciada contra OpenStreetMap con puntos de control en intersecciones y/o correlación de carreteras, con transformación afín/similar y comprobación por superposición. Los anillos abiertos se cierran morfológicamente, se simplifican (Douglas–Peucker) y se validan con `npm run validate:geojson`. Todos llevan `status: unknown` y `geometry_precision: approximate`. No se contacta a nadie, no se salta captcha ni robots.txt y no se inventa geometría. Lo que falta está en [`data/MISSING.md`](../data/MISSING.md). Scripts en [`scripts/pipeline/`](../scripts/pipeline/README.md).

## 1. Principles / ethics
- **Official sources only**: the community's own page/map (or its published file). Aggregators (EruvFinder, eruvmaps, ShulMap, eruv.org...) were used at most to discover leads; **no aggregator geometry is used or stored** (see `data/US-STATES-REPORT.md`, `data/US-research.md`).
- Respect `robots.txt` and terms; no captcha/Cloudflare/403 bypass (Great Neck and Cherry Hill were left alone); no logins, no credentials.
- Nobody was contacted. Rights remain with publishers: features carry `license: "All rights reserved ... approximate traced derivative"` and the source URLs.
- Nothing invented: if the contour cannot be established unambiguously, the eruv stays a point and is listed in [`data/MISSING.md`](../data/MISSING.md).

## 2. Pipelines by source type
### A. Google My Maps KML
1. Find the official page that embeds the map and read the `mid=` of the iframe (if the page is dead, read an archived copy through the Wayback Machine `web.archive.org/web/<ts>if_/<url>`).
2. Fetch `https://www.google.com/maps/d/kml?mid=<MID>&forcekml=1` with plain HTTP.
3. Parse Placemarks (`scripts/pipeline/batch1/load.py`): LineString routes, Polygons, Points (labels/cut-offs dropped).
4. Ring construction (see §3).

### B. Embedded GeoJSON / JS / KML published by the community
Interactive map pages sometimes ship the boundary as a static file or JS array (Detroit `eruv-boundary.geojson`, Philadelphia `map-data.geojson`, St. Louis `eruv-boundary.js`, East Denver `Eruv2024.kml`). The coordinates are read from the public page resources exactly as published (no authentication, no API probing) and only simplified/rounded.

### C. Vector PDF -> polygons
`pdftocairo -svg` converts the PDF; `svgx.py` (stroked paths with transforms) or `fills.py` (filled areas) extracts the vector paths. The boundary is selected by stroke colour/width, snapped (buffer-boundary polygonize) and kept as faces (Monsey, New Haven, Baltimore, Tel Aviv). Vector coordinates are PDF points, then georeferenced as in D.

### D. Raster / PDF without coordinates -> georeferencing against OSM
1. Render the map; build a mask of its road linework (colour thresholds).
2. **Road correlation**: rasterise OSM roads (Overpass, tiled, small bboxes) and run template matching (`cv2.matchTemplate`, `TM_CCOEFF_NORMED`) over a scale (and rotation) grid; a clear peak (typical 0.4-0.65, well above the next one) is accepted, then refined by Powell/grid search (`refine*.py`). Weak peaks (e.g. Princeton 0.24) are rejected.
3. **Control points**: when correlation fails or the map has labelled streets, intersections identifiable on both map and OSM are hand-picked (`gcp.py` finds the OSM node for a street pair) and an affine (or similarity) transform is least-squares fitted; residuals are reported in metres.
4. Local equirectangular projection (KX=111320·cos(lat0), KY=110574 m/deg) for metric work.
5. **Verification overlay**: the registered linework/boundary is drawn on OSM tiles/roads and inspected (`ov*.py`, previews `batchN-*.png`); the result is accepted only if roads coincide.
6. Boundary extraction: colour segmentation of the boundary line, morphological closing, flood-fill from outside to obtain the interior (`trace7.py`), or vector selection (C).

## 3. Ring closing, simplification
Open route lines are joined by morphological closing: `union(lines).buffer(r)` → fill holes (keep exterior) → `buffer(-r)`; r is chosen as small as possible (gaps of 35-350 m are noted per eruv). Slivers and internal holes (cemeteries/parks exclusions) are dropped unless stated. Shapes are simplified with Douglas–Peucker (shapely `simplify`, tolerance ≈0.00005° increased until ≤150 vertices per ring) and rounded to 5-6 decimals. `trace_iou` (simplified vs unsimplified) is only a simplification check, not a closing-error measure.

## 4. Validation and fields
- `npm run validate:geojson` (`scripts/validate-geojson.mjs`): schema, unique ids, valid geometries; CI also runs lint, typecheck and build.
- `geometry_precision`: `approximate` (derived traces, typically ±15-50 m, more for hand control points) or `exact` (published coordinates used as-is / OSM relations).
- `status`: `unknown` for traced perimeters (weekly eruv status must be checked at `source_url`); `active` only where an official page showed it.
- `geometry_kind`: `perimeter` or `point` (points are place labels, not boundaries). `replaces`/`replaces_id` marks a point superseded by a perimeter.
- `note` documents the method, gaps closed and caveats per feature; `source_url`/`boundary_map_url` cite the official origin; `verified_at` is the date of retrieval.

## 5. Limitations
- Maps may be outdated (e.g. New Haven 2007; Miami Beach 2021 polygon vs 2025 CAD not reconciled) and exclusions drawn as raster hatching are not subtracted.
- Georeferencing error depends on the base map; sketch maps and dotted boundaries are ambiguous (Mercer Island, Norfolk).
- Interactive maps behind captchas or blocks, and eruvs with no public map, remain points ([`data/MISSING.md`](../data/MISSING.md)).
- Not a halachic authority: always check the community's own map and status.
- Reproducibility limits: see [`scripts/pipeline/README.md`](../scripts/pipeline/README.md).
