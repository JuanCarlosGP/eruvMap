# BATCH3 eruv perimeters (2026-10-17)

Output: `batch3-eruvs.geojson` (24 Polygon features), previews `batch3-<slug>.png` (red = traced shape, blue = source linework, OSM tiles © OpenStreetMap contributors). Same method and rules as [`BATCH1-NOTES.md`](BATCH1-NOTES.md) / [`BATCH2-NOTES.md`](BATCH2-NOTES.md): only maps published by (or embedded on the official page of) each community, approximate derived traces, `status: unknown`, source cited, `boundary_map_url` to the official map. Nobody contacted; no aggregators used. Vector data was read from the Google My Maps KML export (`/maps/d/kml?mid=..&forcekml=1`) of the map embedded on the official page; route lines were joined into rings by morphological closing (r = 35-70 m), outer envelope only, Douglas-Peucker simplification (<=150 vertices, 250 for the NW London complex), 5 decimals. 13 existing points were replaced (same method as batch 1: `replaces_id` in the batch file, dropped on integration).

## Traced
| id (replaces) | official page / map | verts | closing | confidence |
|---|---|---|---|---|
| berkeley-eruv-perimeter (us-ca-berkeley-eastbayshore) | berkeleyeruv.org/boundaries | 58 | none, source polygon | High |
| fairfax-eruv-perimeter (us-va-fairfax) | fairfaxeruv.org/map.php | 149 | none, source polygon (INOVA ext. omitted) | High |
| eugene-eruv-perimeter (us-or-eugene) | ahavastorah.info/kosher | 63 | none, source polygon ("Expansion" omitted) | High |
| pittsburgh-squirrel-hill-eruv-perimeter (us-pa-pittsburgh-squirrel-hill) | vaadpgh.org/eruv/status-map | 142 | ~50 m | Medium-high |
| valley-eruv-perimeter (us-az-valley-eruv-project) | ahavastorah.org/community/eruv | 138 | ~50 m | Medium-high (matches stated limits) |
| buffalo-amherst-eruv-perimeter (us-ny-buffalo-amherst) | yibuffalo.org/eruv (linked Google map) | 107 | ~50 m | Medium-high |
| milwaukee-west-side-eruv-perimeter (us-wi-milwaukee-west-side) | bethjehudah.org/the-west-side-eruv | 26 | none, one route line | Medium (site: approximate) |
| houston-meyerland-eruv-perimeter (us-tx-houston) | kollelhouston.org/eruv-maps | 41 | ~35 m; cutoff layers excluded | Medium-high; the Northfield-area eruv on the same page is not traced |
| highland-park-edison-eruv-perimeter (us-nj-highland-park-new-brunswick) | hperuv.org | 84 | ~50 m | High |
| new-brunswick-eruv-perimeter | hperuv.org | 78 | ~50 m | High |
| plano / richardson / north-dallas-eruv-perimeter (us-tx-plano, -, us-tx-dallas) | congregationlevyisrael.org/plano-eruv (map of the three DFW areas) | 51 / 109 / 90 | ~60 m | Medium (site: "not exact"; Richardson and North Dallas identified by position) |
| far-north-dallas-eruv-perimeter, south-of-forest-eruv-perimeter | dallasrabbinicalcouncil.org/rabbinic-services/eruvin (linked DOJLife map) | 106 / 24 | ~60 m / none | Medium (Far North Dallas has an internal dividing segment; envelope only) |
| antwerp-eruv-perimeter (antwerp-eruv) | machsike-hadass.be/eruv | 144 | none, closed ring | High |
| victory-park / glenhazel-eruv-perimeter | jhbbethdin.co.za/eruvin | 18 / 102 | none, source polygons | High |
| orchards-eruv-perimeter | jhbbethdin.co.za/eruvin | 73 | ~50 m | Medium-high |
| nw-london-eruv-perimeter (nw-london-eruv) | eruv.co.uk (KLBD map) | 238 | ~70 m, all layers + "Crossing Points" | Medium: connected complex, interior structure and sub-eruvim not shown |
| edgware-stanmore, pinner, borehamwood, bushey | eruv.co.uk (KLBD map) | 157 / 131 / 144 / 139 | ~70 m (edgware, pinner) / none | Medium (edgware, pinner) / High (polygons) |

## Not traced and why
- **Charlotte** (map is a Google "directions" route, not a drawn boundary), **Savannah** (map id returns 404), **Fairfield CT** (old map; page says "there has been a change in the Eruv boundaries"), **Johannesburg Greater eruv** (official map note "Work in progress!!", inner "don't cross" lines; point `johannesburg-eruv` stays), **Belmont/Stanmore "Area" polygon** and **Eugene "Expansion"** (unclear status), Chigwell (already an OSM polygon).
- **Passaic-Clifton** (official vector PDF `pceruv.com/s/2026-map.pdf`, clean red outline) and **Monsey** (official PDF `eiruvofmonsey.org`, coloured zones): readable, but the base map has no coordinates and needs automatic road-network registration against OSM; left for the next batch.
- **Blocked or without a map** (pages 403/empty for automated fetch or no map embedded): Teaneck-Bergenfield, Atlanta (Toco Hills), Denver, Cincinnati, Columbus, Boston-area others, Baltimore (Cloudflare), Boca Raton, Hollywood FL, Aventura/Hallandale/Highland Lakes (see BATCH2), Cleveland (done), St. Louis (static image only), Lower Merion, Portland, Seattle, Providence and most small-community points. Melbourne (COSV): map only in an app; Israel: no existing points and no official downloadable maps found; Montreal: no existing point and no official map located; Sydney: not in dataset.
- **Miami Beach retrace (requested): not done.** The official PDF (2025-09-12) is an aerial image with a CAD vector overlay (about 30k paths: eruv upgrades, poles, seawall lines, Surfside exclusion hatch) and no coordinates; a perimeter would have to be inferred from many interior and shoreline lines after registering the image to the coastline. Instead the existing `miami-beach-eruv-perimeter` now carries a clear OUTDATED/LOW RELIABILITY note and its source is correctly described as the unaffiliated 2021 map.

## Next batches (suggested)
1. Passaic-Clifton and Monsey vector PDFs (auto-register roads to OSM), then Teaneck-Bergenfield and Atlanta Toco Hills once fetchable.
2. Retrace Miami Beach from the 2025 PDF (needs aerial/coastline registration and decisions on water crossings).
3. Remaining US points with no vector map (Denver, Cincinnati, Columbus, St. Louis, Houston Northfield, Nashville West, etc.): check each for images/PDFs.
4. International: Melbourne (COSV app), Sydney, Montreal, Israel (official municipal/eruv bodies), Manchester, Stamford Hill (KLBD map if published).
5. Baltimore PDF (Cloudflare), Chicago, Aventura zones.

License: all rights reserved by sources; approximate derivative pending community permission. Display only, not for halachic reliance.
