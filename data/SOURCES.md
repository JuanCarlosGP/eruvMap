# Eruv map dataset – sources & methods (verified 2026-10-17)

File: `eruvs.geojson` (15 features, ~20 KB). Build script: `build.py` (reads `raw/`).

## Attribution (required)
Contains data © OpenStreetMap contributors, available under the Open Database License (ODbL 1.0): https://www.openstreetmap.org/copyright . Features derived from OSM carry `license: "ODbL OpenStreetMap contributors"`. Any app using this must show that attribution and share-alike derived database terms apply to the OSM-derived geometries. Point features use official-site facts (existence/status) plus OSM-derived coordinates.

## Methods
1. Overpass API (mirror https://maps.mail.ru/osm/tools/overpass/api/interpreter, data timestamp 2026-10-17; overpass-api.de was unreachable from the box). Queried `eruv=*`, `boundary=eruv`, `boundary=religious`+`name=Eruv`, `utility=telecom;eruv`, and name/description regexes. Cross-checked tag counts with taginfo (key `eruv`: 5 objects worldwide). **OSM holds very little eruv data**, so the worldwide perimeter set is tiny.
2. Official pages checked (via web search/fetch on 2026-10-17): eruv.co.uk (KLBD, NW London + Chigwell), eruv.nyc, torontoeruv.org, cosv.org.au/eruv, jhbbethdin.co.za/eruvin, laeruv.com, miamibeacheruv.org, machsike-hadass.be/eruv.
3. Points: only for eruvim confirmed on an official page; coordinates are OSM place/admin label points (via Nominatim, ODbL), flagged `geometry_precision: approximate`, with `coordinate_source`. They are NOT boundaries and several (Toronto, LA, Manhattan, Miami Beach, Antwerp) are city centres.
4. Geometry: 6-decimal coordinates, no simplification needed (small).
5. No coordinates or boundaries were invented. Wikidata was queried only as a pointer (see gaps).

## Counts
By country: Israel 3 (polygons), United States 5 (3 points, 2 partial lines), United Kingdom 3 (1 polygon, 1 multiline fragments, 1 point), Canada 1, Australia 1, South Africa 1, Belgium 1. Perimeter geometry: 7 features (3 Jerusalem polygons + Chigwell polygon exact; 3 are partial line fragments, see `note`); points: 8.

## Caveats
- `status`: "active" only for NW London, Manhattan, Miami Beach (official pages showed up/in-use or a maintained status; Manhattan "Up" had no dated check; Miami site status line was "temporarily unavailable"), Toronto set to unknown because its page said "Pending" on 2026-10-16. Everything else "unknown". Eruv status changes weekly; link users to `source_url`/`contact_url`.
- Jerusalem Sha'arei Chesed areas A/B/C: OSM-only; no official page found.
- Baltimore (2 segments) and NW London fragments (11 tiny segments) are partial OSM pieces, not full perimeters.
- Chigwell polygon: from OSM relation (its source tag points to a community narrative-boundary doc); confirmed existing by KLBD page. chigshul.org.uk/eruv returned 404.
- Official boundary maps (Google/ArcGIS/app embeds) were not scraped; license/terms unknown, so not copied.

## Known gaps
Brooklyn/Queens/Five Towns/Lakewood, Jerusalem (city), Tel Aviv/Bnei Brak, Paris, Montreal, Sydney, Buenos Aires, Johannesburg sub-eruvim, Manchester (MBD), Gateshead, Hamburg (Wikidata Q443985 "Altonaer Eruv", historical; excluded – no primary source), Basel/Zurich, Amsterdam, etc. Wikidata search found only one eruv-instance item. Eruv.org directory entries (e.g. Johannesburg, Antwerp) were seen but only used as pointers. Recommended next step: obtain boundary files directly from community organisations (permission) or have volunteers map them into OSM (boundary=eruv).
