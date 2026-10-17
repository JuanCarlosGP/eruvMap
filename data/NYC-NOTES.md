# NYC eruv perimeters (approximate traces)

Output: `nyc-eruvs.geojson` (2 Polygon features: `manhattan-eruv`, `brooklyn-eruv`), previews `manhattan-preview.png`, `brooklyn-preview.png`. Build script: `build_nyc.py` (intermediates in `raw/nyc/`). Generated 2026-10-17. Nothing was pushed; nobody was contacted.

## Sources
- Manhattan: Manhattan Eruv Inc., https://eruv.nyc/eruv-map.pdf (map by Nechama Rosenberg, "Updated 1/25/2023"; site lists it as updated March 10, 2023). Site text: https://eruv.nyc (Eruv Notes).
- Brooklyn: https://www.brooklyneruv.com/eruv-boundaries/ (page confirmed to embed Google My Map mid=1D3SexNo7tsEWLQlXeX8ktczF5k0BwfE; "Copy of Brooklyn Eruv Boundaries", layer "6.6.25"). Also listed at eruv.org directory.
- Reference only (not redistributed): OSM Manhattan Island outline via Nominatim (relation 3954665, ODbL) used to georeference and plot.
- No Hebrew names appear in either source, so `name_he` is omitted.

## Method
Manhattan: PDF rendered with pdftoppm at 150 dpi. Colours segmented: blue = water, yellow/green = "NOT in the Eruv" / "Park NOT in the Eruv", pink/purple = "In the Eruv"/"Park in the Eruv". Land mask (non-blue) was fit to the OSM Manhattan Island coastline with an affine ICP fit (map is rotated about 29.5 degrees so Manhattan is vertical). Fit residual of the coastline: median 14 m, 90th percentile 51 m, 98th percentile about 430 m (the straight cut at the map top accounts for most of the tail). That fit is the georeferencing (no manual landmark picking). In-eruv mask boundary was vectorised, small holes/specks removed (e.g. the black numbered marker), and simplified to 148 vertices (max deviation from the full-resolution trace about 22 m). Rounded to 5 decimals.
Brooklyn: the My Map KML (a closed chain of route lines, no polygon) was read only to georeference. Lines were joined into one ring, simplified to 140 vertices (max deviation about 77 m vs the KML ring), rounded to 5 decimals. No labels or per-segment detail kept.
Validation: previews overlay the polygon on the OSM outline (Manhattan, side by side with the source map) and on the KML ring plus OSM Brooklyn outline.

## Confidence
- Brooklyn: high for overall extent (about +/-80 m). Boundary follows the official map; the coastal/Jamaica Bay inlets are generalised.
- Manhattan: medium. Georeference good (tens of metres), but the trace comes from raster colour regions, so boundaries on streets (north/south side of street conventions, dotted lines) are only resolved to about 20-60 m, and colour segmentation can blur narrow slivers. Do not use for block-level decisions.

## Exclusions / caveats
- Manhattan, excluded areas visible in the map and reflected as notches or boundary offsets: Hudson River Greenway/Riverside Park strip (park NOT in the eruv) from about 95th St to 145th St and west-side park/shoreline strips; the yellow area east of Park Ave between about 111th and 145th St; a block east of 2nd Ave around 42nd St; west-side strip near 29th St–10th Ave and west of the Highline/piers south to 14th St (as labelled on the map). Also the shoreline piers. Eruv Notes on eruv.nyc: sidewalk included up to the park wall, park above 95th excluded, 95th St intersection complicated ("follow the wire").
- The map's north limit is about 145th St (traced polygon stops at about lat 40.828). Lower Washington Heights Eruv (separate, around W 160th-179th St, map dated 2025-12-19 at /wh-eruv-map-2026-08-07.png) is NOT included; Manhattan north of the PDF map is untraced. Site says it connects to Mount Sinai and YU eruvim.
- eruv.nyc currently notes: 9th and 10th Av between 20th and 22nd St are not in the eruv until further notice (construction). This temporary exclusion is not traced (too small and temporary).
- The PDF is dated 2023 and may not reflect the current wire; the website says the eruv status is updated weekly. `status` is 'unknown' on purpose.
- Brooklyn: the My Map has no explicit "not included" polygons; excluded areas (the traced ring has inlets in the southeast near Jamaica Bay) appear only as the boundary shape. Any internal exclusions, if any, cannot be traced from the KML ring alone. 
- Licence: all rights reserved by the sources; these are approximate derivatives, shown with attribution pending community permission.
