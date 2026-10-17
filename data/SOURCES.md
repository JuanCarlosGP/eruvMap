# Eruv map dataset – sources & methods (verified 2026-10-17)

File: `eruvs.geojson` (125 features after batch 6 perimeters). Build scripts: `build.py` (global `raw/`), US points in [`US-STATES-REPORT.md`](US-STATES-REPORT.md), batch 1 traces in [`BATCH1-NOTES.md`](BATCH1-NOTES.md), batch 2 in [`BATCH2-NOTES.md`](BATCH2-NOTES.md), batch 3 in [`BATCH3-NOTES.md`](BATCH3-NOTES.md), batch 4 in [`BATCH4-NOTES.md`](BATCH4-NOTES.md).

## Attribution (required)
Contains data © OpenStreetMap contributors, available under the Open Database License (ODbL 1.0): https://www.openstreetmap.org/copyright . Features derived from OSM carry `license: "ODbL OpenStreetMap contributors"`. Any app using this must show that attribution and share-alike derived database terms apply to the OSM-derived geometries. Point features use official-site facts (existence/status) plus OSM-derived coordinates.

## NYC approximate perimeters (2026-10-17)

Two polygon features — `manhattan-eruv`, `brooklyn-eruv` — are **approximate traces** derived from official community maps, not copies of those maps:

| id | Source | URL |
|----|--------|-----|
| `manhattan-eruv` | Manhattan Eruv Inc. (PDF map) | https://eruv.nyc/eruv-map.pdf |
| `brooklyn-eruv` | Brooklyn Eruv (My Map / boundaries page) | https://www.brooklyneruv.com/eruv-boundaries/ |

- **Rights:** All rights reserved by the original publishers. These geometries are simplified derivatives for orientation only, shown with attribution pending explicit community permission.
- **Method & confidence:** See [`data/NYC-NOTES.md`](NYC-NOTES.md) (raster colour segmentation + georeferencing for Manhattan; KML ring simplification for Brooklyn).
- **Properties:** `geometry_precision: approximate`, `status: unknown`, `geometry_kind: perimeter`. The former Manhattan **point** (eruv.nyc centre) was removed to avoid duplicating the borough.

## Batch 1 approximate perimeters (2026-10-17)

**10** `Polygon` features from `batch1-eruvs.geojson` (LA Community, Miami Beach/Bal Harbour, Five Towns, Greater Boston + Malden + Waltham/Brandeis + North Shore/Swampscott, Cleveland, Silver Spring, Center City Philadelphia). Each replaced an existing **representative point** where noted in [`BATCH1-NOTES.md`](BATCH1-NOTES.md) (`los-angeles-eruv`, `miami-beach-eruv`, `us-ny-five-towns`, `us-ma-greater-boston`, `us-oh-cleveland-heights`, `us-md-silver-spring`, `us-pa-center-city-philadelphia` removed from the dataset).

- **Rights:** All rights reserved by the original publishers. Approximate traced derivatives for orientation only, shown with attribution pending explicit community permission.
- **Method:** Official My Maps KML / GeoJSON georeferenced, morphological closing where routes were open rings, Douglas–Peucker simplification (see `BATCH1-NOTES.md`).
- **Properties:** `geometry_precision: approximate`, `status: unknown`, `note`, `source_url`, `boundary_map_url`, `license` as in source file.

## Batch 2 approximate perimeters (2026-10-17)

**5** `Polygon` features from `batch2-eruvs.geojson`: Detroit (detroiteruv.org `eruv-boundary.geojson`), Toronto North / South and Richmond Hill (torontoeruv.org interactive map), Lower Washington Heights (eruv.nyc PNG map, georeferenced by hand). Replaced points: `us-mi-detroit-oak-park-southfield`, `toronto-eruv` (removed). Not traced: Miami zones (only an unaffiliated 2021 map), Baltimore (official PDF blocked), Chicago (2010 scans); see [`BATCH2-NOTES.md`](BATCH2-NOTES.md).

- **Rights:** All rights reserved by the original publishers. Approximate traced derivatives for orientation only, shown with attribution pending explicit community permission.
- **Properties:** `geometry_precision: approximate`, `status: unknown`, `source_url`, `boundary_map_url`, `license`, `note`.

## Batch 3 approximate perimeters (2026-10-17)

**24** `Polygon` features from `batch3-eruvs.geojson`, from Google My Maps embedded on each community's official page (KML export) and joined/simplified as in batch 1: Berkeley, Fairfax, Eugene, Pittsburgh, Valley (Scottsdale/Phoenix), Buffalo/Amherst, Milwaukee West Side, Houston (Meyerland), Highland Park/Edison, New Brunswick, Plano, Richardson, North Dallas, Far North Dallas, South of Forest, Antwerp, Victory Park, Glenhazel, Orchards (Johannesburg), NW London complex, Edgware/Stanmore, Pinner, Borehamwood, Bushey. 13 points removed (replaced): `us-ca-berkeley-eastbayshore`, `us-va-fairfax`, `us-or-eugene`, `us-pa-pittsburgh-squirrel-hill`, `us-az-valley-eruv-project`, `us-ny-buffalo-amherst`, `us-wi-milwaukee-west-side`, `us-tx-houston`, `us-nj-highland-park-new-brunswick`, `us-tx-plano`, `us-tx-dallas`, `antwerp-eruv`, `nw-london-eruv`. `miami-beach-eruv-perimeter` (batch 1) now flagged OUTDATED/LOW RELIABILITY (traced from an unaffiliated 2021 map). Details, exclusions and next steps in [`BATCH3-NOTES.md`](BATCH3-NOTES.md).

- **Rights:** All rights reserved by the original publishers. Approximate traced derivatives for orientation only, shown with attribution pending explicit community permission.

## United States representative points (2026-10-17)

**80** `geometry_kind: point` features from community verification (`us-eruvs.geojson` merge). Not re-added at merge time: `manhattan-eruv`, `brooklyn-eruv`, `los-angeles-eruv`, `miami-beach-eruv` (LA and Miami **points** later replaced by batch 1 polygons; see above).

- **Rights & method:** Official-page facts only; no boundary geometry copied. Coordinates via Nominatim/OSM (ODbL), `geometry_precision: approximate`. Optional properties: `state`, `official_boundary_map`, `boundary_map_url`, `stated_terms`, `hotline_or_contact`, `status_as_of`, `evidence`, `coordinate_source`, `extra_note`.
- **Full report:** [`data/US-STATES-REPORT.md`](US-STATES-REPORT.md) (per-state tables, evidence tiers, exclusions).

## Batch 4 approximate perimeters (2026-10-17)

**29** `Polygon` features (19 existing points replaced: Atlanta Toco Hills, Birmingham, Charleston, Englewood, Glendale WI, Aventura, Aventura South, Nashville, Overland Park, Portland, Providence, Richmond VA, Seattle, Skokie, West Hartford, Passaic-Clifton, Rochester, Bethesda, Melbourne; new: Bayside, Mequon, Hallandale, Highland Lakes, Manchester, Whitefield, Montreal, Outremont, Baltimore, Tel Aviv-Yafo). Sources: each community's own page / embedded map (some read through Wayback Machine copies of that page), see [`BATCH4-NOTES.md`](BATCH4-NOTES.md). Passaic-Clifton, Baltimore and Tel Aviv-Yafo were georeferenced to OpenStreetMap from the official PDF/JPG (estimated precision +/-15-150 m, stated per feature in the notes).

- **Rights:** All rights reserved by the original publishers; approximate traced derivatives for orientation only, attribution pending community permission.

## Batch 5 approximate perimeters (2026-10-17)

**5** `Polygon` features replacing existing points: Cincinnati (PDF Nov 2025), Memphis (PNG 2024), Omaha, Potomac, Indianapolis. All come from official raster maps with no coordinates, registered by hand/semi-automatically to OpenStreetMap (control points on street intersections, road-raster refinement, overlay check); estimated precision +/-15-40 m. Details, discards and remaining work in [`data/BATCH5-NOTES.md`](BATCH5-NOTES.md). Dataset now 123 features.

- **Rights:** All rights reserved by the original publishers; approximate traced derivatives for orientation only, attribution pending community permission.

## Methods (global dataset)
1. Overpass API (mirror https://maps.mail.ru/osm/tools/overpass/api/interpreter, data timestamp 2026-10-17; overpass-api.de was unreachable from the box). Queried `eruv=*`, `boundary=eruv`, `boundary=religious`+`name=Eruv`, `utility=telecom;eruv`, and name/description regexes. Cross-checked tag counts with taginfo (key `eruv`: 5 objects worldwide). **OSM holds very little eruv data**, so the worldwide perimeter set is tiny.
2. Official pages checked (via web search/fetch on 2026-10-17): eruv.co.uk (KLBD, NW London + Chigwell), eruv.nyc, brooklyneruv.com, torontoeruv.org, cosv.org.au/eruv, jhbbethdin.co.za/eruvin, laeruv.com, miamibeacheruv.org, machsike-hadass.be/eruv.
3. Points: only for eruvim confirmed on an official page; coordinates are OSM place/admin label points (via Nominatim, ODbL), flagged `geometry_precision: approximate`, with `coordinate_source`. They are NOT boundaries.
4. Geometry: 6-decimal coordinates where noted in build logs.
5. No coordinates or boundaries were invented without a documented method. Wikidata was queried only as a pointer (see gaps).

## Batch 6 approximate perimeters (2026-10-17)

**4** `Polygon` features + 1 detached part: Monsey (official PDF vector, `monsey-eruv-perimeter` + `pearl-river-eruv-perimeter`; replaces the point), Allentown (official Sons of Israel red-line image; replaces the point) and Buffalo Grove (official ZeeMaps image, new). Registered to OpenStreetMap by correlating the maps' road linework with OSM roads (no hand-picked control points for Monsey/Buffalo Grove), overlay-checked; estimated precision +/-15-50 m. Details, discards (Norfolk, Miami Beach CAD, Irvine, St. Louis Park, La Jolla, New Haven, Teaneck, Sydney, Stamford Hill, Bnei Brak) and remaining work in [`data/BATCH6-NOTES.md`](BATCH6-NOTES.md). Dataset now 125 features.

## Batch 7
**6** new perimeters replacing points (St. Louis Park, Irvine, La Jolla, St. Louis, East Denver, New Haven); see [`data/BATCH7-NOTES.md`](BATCH7-NOTES.md) and [`data/MISSING.md`](MISSING.md). Dataset still 125 features.

## Counts (after batch 1)
By country (approx.): United States **87** (2 NYC approximate polygons, 10 batch-1 approximate polygons, 2 partial lines, 73 representative points), Israel 3, United Kingdom 3, Canada 1, Australia 1, South Africa 1, Belgium 1. Perimeter geometry: **19**; points: **80**.

## Caveats
- `status`: "active" only where an official page showed up/in-use or maintained status (e.g. NW London, Miami Beach). NYC polygons are `unknown` until verified against weekly community status. Eruv status changes weekly; link users to `source_url`/`contact_url`.
- Jerusalem Sha'arei Chesed areas A/B/C: OSM-only; no official page found.
- Baltimore (2 segments) and NW London fragments (11 tiny segments) are partial OSM pieces, not full perimeters.
- Chigwell polygon: from OSM relation (its source tag points to a community narrative-boundary doc); confirmed existing by KLBD page.
- NYC: see `NYC-NOTES.md` for exclusions, north limit (~145th St on Manhattan PDF), and licence.

## Known gaps
Queens/Five Towns/Lakewood, full Jerusalem city eruv, Tel Aviv/Bnei Brak, Paris, Montreal, Sydney, Buenos Aires, Johannesburg sub-eruvim, Manchester (MBD), Gateshead, etc. Recommended next step: obtain boundary files directly from community organisations (permission) or have volunteers map them into OSM (`boundary=eruv`).
