# Eruv map dataset – sources & methods (verified 2026-10-17)

File: `eruvs.geojson` (96 features after US points batch). Build scripts: `build.py` (global `raw/`), US batch documented in [`US-STATES-REPORT.md`](US-STATES-REPORT.md).

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

## United States representative points (2026-10-17)

**80** new `geometry_kind: point` features from community verification (`us-eruvs.geojson` merge). Not re-added (already in dataset): `manhattan-eruv`, `brooklyn-eruv`, `los-angeles-eruv`, `miami-beach-eruv`.

- **Rights & method:** Official-page facts only; no boundary geometry copied. Coordinates via Nominatim/OSM (ODbL), `geometry_precision: approximate`. Optional properties: `state`, `official_boundary_map`, `boundary_map_url`, `stated_terms`, `hotline_or_contact`, `status_as_of`, `evidence`, `coordinate_source`, `extra_note`.
- **Full report:** [`data/US-STATES-REPORT.md`](US-STATES-REPORT.md) (per-state tables, evidence tiers, exclusions).

## Methods (global dataset)
1. Overpass API (mirror https://maps.mail.ru/osm/tools/overpass/api/interpreter, data timestamp 2026-10-17; overpass-api.de was unreachable from the box). Queried `eruv=*`, `boundary=eruv`, `boundary=religious`+`name=Eruv`, `utility=telecom;eruv`, and name/description regexes. Cross-checked tag counts with taginfo (key `eruv`: 5 objects worldwide). **OSM holds very little eruv data**, so the worldwide perimeter set is tiny.
2. Official pages checked (via web search/fetch on 2026-10-17): eruv.co.uk (KLBD, NW London + Chigwell), eruv.nyc, brooklyneruv.com, torontoeruv.org, cosv.org.au/eruv, jhbbethdin.co.za/eruvin, laeruv.com, miamibeacheruv.org, machsike-hadass.be/eruv.
3. Points: only for eruvim confirmed on an official page; coordinates are OSM place/admin label points (via Nominatim, ODbL), flagged `geometry_precision: approximate`, with `coordinate_source`. They are NOT boundaries.
4. Geometry: 6-decimal coordinates where noted in build logs.
5. No coordinates or boundaries were invented without a documented method. Wikidata was queried only as a pointer (see gaps).

## Counts (after US points)
By country (approx.): United States **86** (2 NYC approximate polygons, 2 partial lines, 82 representative points including prior LA/Miami), Israel 3, United Kingdom 3, Canada 1, Australia 1, South Africa 1, Belgium 1. Perimeter geometry: 9; points: **87**.

## Caveats
- `status`: "active" only where an official page showed up/in-use or maintained status (e.g. NW London, Miami Beach). NYC polygons are `unknown` until verified against weekly community status. Eruv status changes weekly; link users to `source_url`/`contact_url`.
- Jerusalem Sha'arei Chesed areas A/B/C: OSM-only; no official page found.
- Baltimore (2 segments) and NW London fragments (11 tiny segments) are partial OSM pieces, not full perimeters.
- Chigwell polygon: from OSM relation (its source tag points to a community narrative-boundary doc); confirmed existing by KLBD page.
- NYC: see `NYC-NOTES.md` for exclusions, north limit (~145th St on Manhattan PDF), and licence.

## Known gaps
Queens/Five Towns/Lakewood, full Jerusalem city eruv, Tel Aviv/Bnei Brak, Paris, Montreal, Sydney, Buenos Aires, Johannesburg sub-eruvim, Manchester (MBD), Gateshead, etc. Recommended next step: obtain boundary files directly from community organisations (permission) or have volunteers map them into OSM (`boundary=eruv`).
