# BATCH2 eruv perimeters (2026-10-17)

Output: `batch2-eruvs.geojson` (5 Polygon features), previews `batch2-<slug>.png` (red = traced shape, blue = source linework, OSM tiles © OpenStreetMap contributors). Same method as [`BATCH1-NOTES.md`](BATCH1-NOTES.md): approximate derived traces, `status: unknown`, source cited, `boundary_map_url` pointing to the official map. Nobody contacted; no aggregators (eruvfinder, ShulMap) used.

## Traced
| id | source (official) | verts | how | confidence |
|---|---|---|---|---|
| detroit-eruv-perimeter (replaces us-mi-detroit-oak-park-southfield) | detroiteruv.org/eruv, map data `eruv-boundary.geojson` ("current boundary", operational eruv only; Google My Maps export, generated 2026-10-09) | 74 | source ring already closed, simplified | High |
| toronto-north-eruv-perimeter (replaces toronto-eruv) | torontoeruv.org/boundaries: the page's Leaflet map draws the "North eruv - the 401 up to the 407" polygon (coordinates read from the site's own map code) | 146 | source ring; it had one self-touching vertex, repaired (area unchanged) | High (checked vs. site text: 401/407/404/400, CN/CP tracks) |
| toronto-south-eruv-perimeter | same map, "South eruv - the CP tracks up to the 401" | 108 | source ring | High |
| richmond-hill-eruv-perimeter | same map, "Richmond Hill - a separate eruv, no crossover from the north eruv" | 51 | source ring | Medium-high (operator not named on the Toronto page; included because the official map draws it) |
| lower-washington-heights-eruv-perimeter | eruv.nyc, `wh-eruv-map-2026-08-07.png` (map updated 2025-12-19) | 48 | raster georeferenced by hand: 7 street intersections (Amsterdam/St Nicholas Aves x W 160-175th St) matched to OSM, affine fit, residual 3-10 m; shaded in-eruv area segmented by colour and vectorised | Medium (about 10-30 m; sidewalk/park-wall conventions not resolved) |

Notes: Toronto's North and South sections are drawn as separate polygons by the community (the 401 may only be crossed at Bathurst, Wilson, Bayview) and kept as two features because the validator/UI accept only Polygon/LineString. Lower Washington Heights is connected to the Mount Sinai Eruv (Broadway W178-179 St) and YU Eruv (Amsterdam Ave W178-180 St); neither map is traced, and it is separate from `manhattan-eruv` (whose map stops at about 145th St). The Detroit planned expansion into Berkley is not shown by the community and therefore not traced.

## Not traced (point kept / nothing added) and why
- **Miami: Aventura, Aventura South, Hallandale, Highland Lakes, North Miami Beach, Skylake, Sunny Isles.** The only vector map is the Google My Map linked from miamibeacheruv.org/eruv-map, which that page labels *"Unaffiliated Eruv Google Map URL (unaffiliated with Miami Beach Eruv Council - not checked or endorsed)"*; KML says "As of 9/27/2021". The Council's own official map (PDF 2025-09-12) covers Miami Beach only (an aerial image, south of 73rd St). The zone communities' own pages (chabadfl.org Aventura, lubavitchaventurasouth.org, chabadchayil.org) give text boundaries / a colour map image but were blocked (HTTP 403) for automated fetch, so no official map could be read. No reliable official map, so the existing points (`us-fl-aventura`, `us-fl-aventura-south`) stay and the other five have no feature. Aventura South's text boundary (191st & Dixie / 29th Ave / 180th & US-1 / 183rd Terr & Dixie) could be traced by hand if wanted.
- **Baltimore (Eruv of Baltimore, eruvstat.us).** The current official map (PDF "Eruv_Map26-1.3", 2026-08-05, with sidewalk-level detail) is behind a Cloudflare challenge (HTTP 403); not bypassed. The two OSM partial segments remain.
- **Chicago (West Rogers Park, Lincolnwood-Peterson Park, Skokie).** The only official maps are scanned images in `crcweb.org/eruv maps.pdf` (2010 paper scan): West Rogers Park is a schematic without scale, the others are low-resolution scans of street maps; the communities' own sites (skokieeruv.com, chicagoeruv.tripod.com) did not load. Too stale and imprecise to trace without inventing limits, so points remain.
- **Manhattan north of the PDF map**: only Lower Washington Heights has an official map; nothing for Inwood/Marble Hill/Hamilton Heights/Harlem north of 145th (covered by the Manhattan Eruv map note or not mapped).

## Caveat on batch 1 (Miami Beach)
`miami-beach-eruv-perimeter` was traced from the same unaffiliated 2021 Google map. The Miami Beach Eruv Council page marks the old map as "INACTIVE (prior to Aug 2025)" and publishes a new official PDF (2025-09-12). Treat that polygon as outdated until retraced from the PDF.

License: all rights reserved by sources; approximate derivative pending community permission. Display only, not for halachic reliance.
