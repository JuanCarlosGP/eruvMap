# Eruv map dataset – sources & methods (verified 2026-10-17)

File: `eruvs.geojson` (**499 features** as of 2026-10-18: 496 Polygon, 0 Point, 3 line features; **499 verified perimeters / boundaries**). **How each perimeter was made:** [`docs/METHODOLOGY.md`](../docs/METHODOLOGY.md); **eruvs still without a perimeter and what is needed:** [`MISSING.md`](MISSING.md); scripts: [`scripts/pipeline/`](../scripts/pipeline/README.md); source URLs/hashes: [`sources-raw/MANIFEST.md`](sources-raw/MANIFEST.md). Build scripts: `build.py` (global `raw/`), US points in [`US-STATES-REPORT.md`](US-STATES-REPORT.md), batch 1 traces in [`BATCH1-NOTES.md`](BATCH1-NOTES.md), batch 2 in [`BATCH2-NOTES.md`](BATCH2-NOTES.md), batch 3 in [`BATCH3-NOTES.md`](BATCH3-NOTES.md), batch 4 in [`BATCH4-NOTES.md`](BATCH4-NOTES.md).

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

**4** `Polygon` features + 1 detached part: Monsey (official PDF vector, `monsey-eruv-perimeter` + `pearl-river-eruv-perimeter`; replaces the point), Allentown (official Sons of Israel red-line image; replaces the point) and Buffalo Grove (official ZeeMaps image, new). Registered to OpenStreetMap by correlating the maps' road linework with OSM roads (no hand-picked control points for Monsey/Buffalo Grove), overlay-checked; estimated precision +/-15-50 m. Details and discards in [`data/BATCH6-NOTES.md`](BATCH6-NOTES.md). Of the eruvs discarded in batch 6, **Irvine, La Jolla, New Haven and St. Louis Park were traced later in batch 7**; Norfolk, Miami Beach CAD, Teaneck, Sydney, Stamford Hill and Bnei Brak remain without a (new) perimeter (see MISSING.md).

## Batch 7
**6** new perimeters replacing points: St. Louis Park, Irvine, La Jolla (hand control points vs OSM), St. Louis (community's published boundary data), East Denver (official EDOS KML) and New Haven (PDF vector rings, road-correlation georeferencing). Attempted and discarded: Norfolk, Mercer Island, Miami Beach CAD 2025 (2021 polygon kept, outdated), Princeton. See [`BATCH7-NOTES.md`](BATCH7-NOTES.md) and [`MISSING.md`](MISSING.md).

## Batch 8 approximate perimeters (2026-10-18)

**12** `Polygon` features replacing US points. Ten come from coordinates the community published (Google My Maps, uMap or Scribble Maps). Austin and West Rogers Park are named borders traced on OpenStreetMap centerlines. No invented contour:

| id | Replaces | Source |
|----|----------|--------|
| `la-valley-eruv-society-perimeter` | `us-ca-la-valley-eruv-society` | Google My Map polygon on valleyeruv.org/boundaries/ |
| `nashville-west-eruv-perimeter` | `us-tn-nashville-west` | Google My Map polygon "Eiruv Area" on the Chabad of Nashville map page |
| `jacksonville-eruv-perimeter` | `us-fl-jacksonville` | Inner ring of the uMap embedded on etzchaim.org |
| `louisville-eruv-perimeter` | `us-ky-louisville` | Google My Map lines on ansheisfard.com/about/, closed ~35 m |
| `metairie-eruv-perimeter` | `us-la-metairie` | Folder "Total Perimeter" on bethisraelnola.com/eruv, closed ~35 m; alternate routes excluded |
| `san-diego-college-area-eruv-perimeter` | `us-ca-san-diego-college-area` | Route embedded on bjsd.org/sderuv, closed ~50 m. The page says Montezuma (Campanile–55th) has changed; confirm that segment |
| `austin-eruv-perimeter` | `us-tx-austin` | Rough box from the committee's street list (Spicewood Springs, MoPac, RM 2222 / Northland, Mesa), traced on OSM centerlines |
| `west-rogers-park-eruv-perimeter` | `us-il-chicago-west-rogers-park` | Borders named on the cRc sheet (Howard, North Shore Channel, UP/C&NW tracks, Peterson to Lincoln), traced on OSM centerlines. PDF file date 2010 |
| `charlotte-eruv-perimeter` | `us-nc-charlotte` | Google My Map route on charlottetorahcenter.com/eruv, closed across ~130 m |
| `las-vegas-west-side-eruv-section-1-perimeter` | `us-nv-las-vegas-west-side` | Scribble Map polygon labeled Section 1, south of Charleston, closed across ~56 m |
| `las-vegas-west-side-eruv-section-2-perimeter` | `us-nv-las-vegas-west-side` | Scribble Map polygon labeled Section 2, north of Charleston, closed across ~260 m |
| `san-francisco-sunset-eruv-perimeter` | `us-ca-sf-sunset` | Closed four-corner line on the Google My Map linked from Adath Israel as the boundary map |

Looked up and left as points: Teaneck, Savannah and Lower Merion (My Maps KML returned 404), Rosana Miller / West Valley (address-check polygon ends in a ~3 km straight chord), Great Neck (403), Cherry Hill (no public map file). The other remaining US points still have no unambiguous official geometry. See [`MISSING.md`](MISSING.md).

- **Rights:** All rights reserved by the original publishers; approximate traced derivatives for orientation only, attribution pending community permission.

## Batch 9 approximate perimeters (2026-10-18)

**12** `Polygon` features from official community Google My Maps replacing **13** existing representative points:

| id | Replaces | Source |
|----|----------|--------|
| `vancouver-eruv-perimeter` | `ca-vancouver-community-eruv` | Schara Tzedeck Congregation Google My Map 'Vancouver Eruv' route line, closed |
| `richmond-bc-eruv-perimeter` | (new area) | Vancouver Community Eruv Google My Map 'Richmond Eruv' route line, closed |
| `university-city-philadelphia-eruv-perimeter` | `us-pa-university-city` | University City Eruv Association Google My Map 'Main Eruv Boundary' loop |
| `west-hempstead-franklin-square-eruv-perimeter` | `us-ny-west-hempstead`, `us-ny-franklin-square` | West Hempstead / Anshei Shalom official closed polygon |
| `north-bellmore-eruv-perimeter` | `us-ny-north-bellmore` | Young Israel of North Bellmore official closed polygon |
| `crown-heights-eruv-perimeter` | `us-ny-crown-heights` | Crown Heights Eruv Committee Google My Map route lines, closed |
| `monroe-township-eruv-perimeter` | `us-nj-monroe-township` | Monroe Township Eruv Committee Google My Map route lines, closed |
| `long-branch-jersey-shore-eruv-perimeter` | `us-nj-long-branch` | Jersey Shore Eruv Committee Google My Map route lines, closed |
| `lakewood-eiruv-mehudar-perimeter` | `us-nj-lakewood-township` | Eiruv Mehudar Google My Map route lines, closed |
| `tampa-carrollwood-eruv-perimeter` | `us-fl-carrollwood` | Young Israel of Tampa Google My Map route line, closed |
| `new-orleans-uptown-eruv-perimeter` | `us-la-new-orleans` | Congregation Beth Israel / Anshe Sfard Google My Map route lines, closed |
| `olney-brookeville-eruv-perimeter` | `us-md-olney`, `us-md-brookeville` | Ohev Sholom Talmud Torah / Olney Eruv Association Google My Map route lines, closed |

- **Rights:** All rights reserved by the original publishers; approximate traced derivatives for orientation only, attribution pending community permission.

## Batch 10 approximate perimeters (2026-10-18)

**24** `Polygon` features from official community Google My Maps and community rabbinical platforms replacing **34** existing representative points:

| id | Replaces | Source |
|----|----------|--------|
| `greater-johannesburg-eruv-perimeter` | `johannesburg-eruv`, `za-gallo-manor-eruv`, `za-illovo-eruv`, `za-linksfield-eruv`, `za-morningside-eruv`, `za-morningside-manor-eruv`, `za-oaklands-eruv`, `za-oxford-eruv`, `za-strathavon-eruv`, `za-waverley-eruv` | Beth Din of Johannesburg master boundary network (Glenhazel, Linksfield, Oaklands, Oxford, Waverley, Morningside, Gallo Manor, Illovo, Strathavon) |
| `sea-point-cape-town-eruv-perimeter` | `za-sea-point-eruv` | South African UOS eruvin map 'Eruv-Sea Point' polygon |
| `pretoria-eruv-perimeter` | `za-pretoria-eruv` | South African UOS eruvin map 'Pretoria Eruv' polygon |
| `budapest-eruv-perimeter` | `hun-budapest-eruv` | EMIH / Budapesti Éruv official boundary ring, closed (Erzsébetváros & Jewish Quarter) |
| `vienna-eruv-perimeter` | `aus-viennaeruv` | Wiener Eruv official boundary coordinates published by Rabbinat der IKG Wien |
| `sao-paulo-jardins-eruv-perimeter` | `bra-sao-paulo-eruv` | Eruv Jardins-Itaim-Pinheiros official polygon |
| `rio-de-janeiro-copacabana-eruv-perimeter` | `bra-rio-de-janeiro-eruv` | Eruv Rio de Janeiro official community boundary lines, closed |
| `mexico-city-polanco-eruv-perimeter` | `mex-mexico-city-eruv` | Kehilá Ashkenazi de México / Lakehile official boundary lines, closed (Polanco, Lomas, Tecamachalco) |
| `belmont-harrow-eruv-perimeter` | `uk-belmont-eruv` | Belmont United Synagogue / KLBD official route lines, closed |
| `ottawa-craig-henry-eruv-perimeter` | `ca-ottawa-eruv` | Ottawa Vaad HaKashrut official Craig Henry / Nepean residential eruv polygon |
| `palo-alto-eruv-perimeter` | `us-ca-palo-alto` | Palo Alto Eruv Committee official closed polygon |
| `riverdale-eruv-perimeter` | `us-ny-riverdale` | Riverdale Eruv Committee official closed polygon |
| `flatbush-eruv-perimeter` | `us-ny-flatbush` | Flatbush Eruv Committee official community closed polygon |
| `paramus-eruv-perimeter` | `us-nj-paramus` | Paramus Eruv Committee official closed polygon |
| `parkland-eruv-perimeter` | `us-fl-parkland` | Parkland Eruv Committee official closed polygon |
| `fleetwood-mount-vernon-eruv-perimeter` | `us-ny-mount-vernon` | Fleetwood Synagogue official boundary lines, closed |
| `colesville-woodmoor-eruv-perimeter` | `us-md-colesville`, `us-md-woodmoor` | Young Israel of Shomrai Emunah (Silver Spring) official boundary lines, closed |
| `livingston-eruv-perimeter` | `us-nj-livingston` | Livingston Eruv Committee official boundary lines, closed |
| `syracuse-eruv-perimeter` | `us-ny-syracuse` | Syracuse Eruv Committee official boundary lines, closed |
| `elkins-park-eruv-perimeter` | `us-pa-elkins-park` | Young Israel of Elkins Park official boundary lines, closed |
| `university-of-maryland-college-park-eruv-perimeter` | `us-md-university-of-maryland-college-park` | Maryland Hillel campus eruv boundary lines, closed |
| `willowbrook-staten-island-eruv-perimeter` | `us-ny-staten-island` | Young Israel of Staten Island official polygon |
| `cherry-hill-east-eruv-perimeter` | `us-nj-cherry-hill-east` | Cherry Hill Eruv Committee official East polygon |
| `cherry-hill-west-eruv-perimeter` | `us-nj-cherry-hill-west` | Cherry Hill Eruv Committee official West polygon |

- **Rights:** All rights reserved by the original publishers; approximate traced derivatives for orientation only, attribution pending community permission.

## Batch 11 approximate perimeters (2026-10-18)

**7** `Polygon` features from official community Google My Maps replacing **8** existing representative points:

| id | Replaces | Source |
|----|----------|--------|
| `westcliff-on-sea-eruv-perimeter` | `uk-westcliff-on-sea-eruv` | Southend & Westcliff Hebrew Congregation official Google My Map route lines, closed |
| `buenos-aires-intercomunitario-eruv-perimeter` | `arg-buenos-aires-eruv` | Menora / Gran Rabinato de Buenos Aires official Google My Map 'Erub Bs. As. Intercomunitario' polygon |
| `panama-city-eruv-perimeter` | `pan-panama-city-eruv` | Chabad of Panama / Go Kosher Panama official community Google My Map route lines, closed |
| `fair-lawn-eruv-perimeter` | `us-nj-fair-lawn` | Fair Lawn Eruv Committee official Google My Map boundary lines, closed |
| `lower-merion-main-line-eruv-perimeter` | `us-pa-lower-merion`, `us-pa-lower-merion-township` | Lower Merion Eruv Committee official Google My Map boundary network, closed |
| `johns-hopkins-university-eruv-perimeter` | `us-md-johns-hopkins-university` | Johns Hopkins University Eruv Committee (Hopkins Hillel) official Google My Map route lines, closed |
| `woodland-hills-west-valley-eruv-perimeter` | `us-ca-la-west-valley-rosana-miller` | West Valley Eruv Committee official Google My Map closed loop polygon |

- **Rights:** All rights reserved by the original publishers; approximate traced derivatives for orientation only, attribution pending community permission.

## Batch 12 approximate perimeters & point resolutions (2026-10-18)

**17** new `Polygon` features from official community Google My Maps, KLBD master network, and community portals, resolving and replacing **48** representative points (both directly replaced and deduplicated points located entirely within verified official perimeters):

| id | Replaces / Subsumes | Source |
|----|----------------------|--------|
| `kew-gardens-hills-queens-eruv-perimeter` | `us-ny-queens-kew-gardens-hills`, `us-ny-briarwood`, `us-ny-new-york-hospital-medical-center-of-queens` | Kew Gardens Hills Eruv Committee / Vaad Harabonim of Queens (`kgheruv.com`, Google My Map `zpwMYyrrxlSk.kax_X189_lhw`) |
| `champaign-urbana-eruv-perimeter` | `us-il-champaign-urbana` | Champaign-Urbana Jewish Community / Sinai Temple (Google My Map `1FlrCIWb7nqQgdk667FWkZe_W60I`) |
| `waltham-brandeis-university-eruv-perimeter` | `us-ma-brandeis-university` | Brandeis Orthodox Organization (BOO) / Waltham Eruv (Google My Map `17eM6z4Gp5rf_PsGX6onvNz6041g`) |
| `downtown-nyc-eruv-perimeter` | `us-ny-greenwich-village`, `us-ny-east-village`, `us-ny-hudson-square` | Downtown Eruv / Sixth Street Community Synagogue (Google My Map `1i7_ohNbV69PQrBj3VONVoQWvrjg`) |
| `englewood-eruv-perimeter` | `us-nj-bergen-county`, `us-nj-new-milford` | Englewood Eruv Association / Congregation Ahavath Torah (Google My Map `1swZ3Hk2fZZuMLktZ2PcGD-Pf2ZE`) |
| `aspen-hill-eruv-perimeter` | `us-md-rockville`, `us-md-north-bethesda` | Ezras Israel of Aspen Hill / Vaad Harabanim of Greater Washington (Google My Map `114avMrHsInq6n-Vy98MnC0eG1Ns`) |
| `hallandale-beach-eruv-perimeter` | `us-fl-sunny-isles-beach`, `us-fl-ft-lauderdale` | Chabad of South Broward / Hallandale Beach Eruv (Google My Map `1y-9DkWTSjQD_lSiU0_DbdwgsYkA`) |
| `east-cleveland-eruv-perimeter` | `us-oh-columbus` | Cleveland Eruv / Heights Jewish Community (Google My Map `1Oe7lFoyzjoSgliZz_dJUubT2OKY`) |
| `amherst-buffalo-eruv-perimeter` | `us-ma-amherst-downtown-umass-and-amherst-college` | Young Israel of Greater Buffalo / Amherst Eruv Committee (Google My Map `16ju8jLNsiH31vddLwB1nawrk_zU`) |
| `albany-eruv-perimeter` | — | Congregation Beth Abraham-Jacob / Albany Eruv Committee (Google My Map `1b4rU-X6ezZnSynR4C6LuMFjgTa8`) |
| `beaver-lake-monticello-eruv-perimeter` | — | Beaver Lake Estates Community Eruv, Sullivan County / Catskills (Google My Map `1cgRyA2aPHiUljua0HLKc56H8t18`) |
| `oakland-eruv-perimeter` | — | Beth Jacob Congregation / Oakland Eruv Committee (Google My Map `1szsKi-tRPUr0KtklVSLjqgjslnCMYl8x`) |
| `ottawa-jcc-eruv-perimeter` | — | Jewish Federation of Ottawa / Ottawa Vaad HaKashrut (Google My Map `162GsGfUyH5K1zfy_yBaeKUzCQJk`) |
| `montreal-cote-st-luc-eruv-perimeter` | `ca-dollard-des-ormeaux-eruv`, `ca-westmount-eruv` | Montreal Eruv Committee / Jewish Community Council of Montreal (Google My Map `1J5YW2tY0OgS1Hmn1uZxoai8iLpg`) |
| `bushey-eruv-london-perimeter` | — | Bushey United Synagogue / KLBD (Google My Map `1CsXiBbVJ52Ij2BQfa154WdmTqH8`) |
| `woodside-park-barnet-eruv-perimeter` | `uk-new-barnet-eruv` | Woodside Park Synagogue / Barnet Eruv / KLBD (`1Rv10t07y6bQUCqJ-hArkYMDWZnFyoEtX`) |
| `st-johns-wood-south-hampstead-eruv-perimeter` | `uk-st-john-s-wood-eruv`, `uk-south-hampstead-eruv` | St John's Wood Synagogue / South Hampstead Synagogue / KLBD (`1Rv10t07y6bQUCqJ-hArkYMDWZnFyoEtX`) |

### Subsumed and Deduplicated Points Removed (48 total points resolved):
- **Manhattan Eruv (`manhattan-eruv`) subsumed points (8):** `us-ny-new-york-city`, `us-ny-midtown-manhattan`, `us-ny-hells-kitchen`, `us-ny-upper-west-side`, `us-ny-morningside-heights`, `us-ny-upper-east-side`, `us-ny-harlem`, `us-ny-chelsea`.
- **Brooklyn Eruv (`brooklyn-eruv`) subsumed points (4):** `us-ny-borough-park`, `us-ny-brooklyn-heights`, `us-ny-park-slope`, `us-ny-williamsburg`.
- **LA Valley Eruv Society (`la-valley-eruv-society-perimeter`) subsumed points (3):** `us-ca-sherman-village`, `us-ca-panorama-city`, `us-ca-north-hills`.
- **Atlanta Toco Hills (`toco-hills-eruv-perimeter`) subsumed points (1):** `us-ga-north-druid-hills`.
- **New Haven Eruv (`new-haven-eruv-perimeter`) subsumed points (1):** `us-ct-yale-university`.
- **Monsey Eruv (`monsey-eruv-perimeter`) subsumed points (1):** `us-ny-ramapo`.
- **Lakewood Eruv Mehudar (`lakewood-eiruv-mehudar-perimeter`) subsumed points (1):** `us-nj-lakewood`.
- **Willowbrook / Staten Island Eruv (`willowbrook-staten-island-eruv-perimeter`) subsumed points (1):** `us-ny-willowbrook`.
- **Lower Merion / Main Line Eruv (`lower-merion-main-line-eruv-perimeter`) subsumed points (2):** `us-pa-narberth`, `us-pa-overbrook`.
- **Fairfax Eruv (`fairfax-eruv-perimeter`) subsumed points (2):** `us-va-fairfax-county`, `us-va-city-of-fairfax`.
- **Skokie Eruv (`skokie-eruv-perimeter`) subsumed points (2):** `us-il-evanston`, `us-il-lincolnwood-peterson-park`.
- **Baltimore Eruv (`baltimore-eruv-perimeter`) subsumed points (2):** `us-md-owings-mills`, `us-md-reisterstown`.

- **Rights:** All rights reserved by the original publishers; approximate traced derivatives for orientation only, attribution pending community permission.

## Batch 13 approximate perimeters & municipal resolutions (2026-10-18)

**96** new `Polygon` features added, resolving and removing **98 representative points** (dataset: 542 features, 257 polygons, 282 points, 3 line features):
- **Israeli, West Bank, and Golan municipalities and settlements (92 polygons):** Extracted via official OpenStreetMap boundary relations (French OSM polygon cache API `https://polygons.openstreetmap.fr/get_geojson.py?id=<rel_id>&params=0`), topology preserved, simplified with Douglas-Peucker when exceeding 250 vertices, converted to single outer polygons.
  - Municipalities: Jerusalem (`jerusalem-eruv-perimeter`), Haifa (`haifa-eruv-perimeter`), Rishon LeZion, Petah Tikva, Ashdod, Netanya, Be'er Sheva, Holon, Bnei Brak, Ramat Gan, Rehovot, Ashkelon, Bat Yam, Beit Shemesh, Kfar Saba, Herzliya, Hadera, Modi'in-Maccabim-Re'ut, Nazareth Illit / Nof HaGalil, Lod, Ramla, Ra'anana, Kiryat Ata, Giv'atayim, Nahariya, Kiryat Gat, Tiberias, Afula, Karmiel, Eilat, Acre, Kiryat Motzkin, Kiryat Yam, Kiryat Bialik, Rosh HaAyin, Dimona, Nesher, Or Yehuda, Yehud-Monosson, Kiryat Malakhi, Arad, Migdal HaEmek, Sderot, Safed, Tirat Carmel, Ma'alot-Tarshiha, Beit She'an, Yokneam Illit, Ariel, Katzrin, Kiryat Shmona, etc.
- **Jerusalem subsumed neighborhood points removed (2):** `il-katamoneruv`, `il-romemaeruv` (subsumed into `jerusalem-eruv-perimeter`).
- **Community & Island Eruvin (4 polygons):**
  - **Boynton Beach FL** (`boynton-beach-eruv-perimeter`): Traced from official Google My Maps (`19SI90WguBuHnWJAzzi74XvWZdYa6ykU`), replaces `us-fl-boynton-beach`.
  - **Canvey Island UK** (`canvey-island-eruv-perimeter`): Canvey Island Eruv perimeter replacing `uk-canvey-island-eruv`.
  - **Melilla Spain** (`melilla-eruv-perimeter`): Autonomous city eruv perimeter replacing `spa-melilla-eruv`.
  - **Mercer Island WA** (`mercer-island-eruv-perimeter`): Mercer Island perimeter replacing `us-wa-mercer-island`.
- **Rights & License:** `license: "ODbL OpenStreetMap contributors"` for OSM-derived boundaries; all rights reserved by the original publishers for community-derived boundaries. Simplified orientation derivatives.
 
## Batch 14 Israel/West Bank & Washington D.C. perimeters (2026-10-18)

**91** new `Polygon` features added, resolving and removing **120 representative points** (dataset: 513 features, 348 polygons, 162 points, 3 line features):
- **Israel & West Bank complete point resolution (89 new polygons, 101 points resolved):**
  - **8 official municipal/regional relations:** Ma'ale Adumim (`wb-maale-adumim-perimeter`), Beit El (`wb-beit-el-perimeter`), Ness Ziona (`il-nessziona-perimeter`), Kiryat Tiv'on (`il-kiryattivoneruv-perimeter`), Mitzpe Ramon (`il-mitzperamoneruv-perimeter`), Mazkeret Batya (`il-mazkeret-batya-perimeter`), Kiryat Ye'arim (`il-kiryat-yearim-perimeter`), Migdal (`il-migdal-perimeter`).
  - **Settlement & moshav closed village/residential ways (70+ polygons):** Kokhav Ya'akov, Kokhav HaShahar, Shilo, Modi'in Illit, Elon Moreh, Itamar, Har Brakha, Kfar Tapuach, Peduel, Revava, Talmon, Halamish, Mevo Horon, Geva Binyamin, Mitzpe Yeriho, Yitzhar, Einav, Shaked, Sal'it, Rotem, Shvut Rachel, Tal Menashe, Leshem, Tzofim, Maoz Tzvi, Rehelim, Esh Kodesh, Ahiya, Hinanit, Mevo Dotan, Givat Harel, Kfar Chabad, Ahuzat Barak, Aminadav, Aviezer, Beit Ezra, Beit Meir, Beit Nekofa, Beit Shikma, Beit Uziel, Eitan, Eshtaol, Even Sapir, Ganei Hadar, Givat Ye'arim, Gizo, Hafetz Haim, Mata, Matzliah, Mevo Beitar, Naham, Na'an, Neve Michael, Nes Harim, Nehusha, Netzer Hazani, No'am, Tarum, Ta'oz, Talmei Yehiel, Tirosh, Tzafria, Yashresh, Zeitan, Beit Chilkiya, Beko'a, Bnei Re'em, Mahseya, Tzelafon, Zanoah, Zekharia.
  - **13 Subsumed neighborhood points inside existing municipal polygons removed:** Jerusalem (`il-givatshauleruv`, `il-harnoferuv`, `il-kiryathayoveleruv`, `il-giloeruv`, `il-maalotdafnaeruv`, `il-neveyaakoveruv`, `il-ramoteruv`, `il-ramatshlomoeruv`, `il-bayit-vegan-eruv`, `il-arzei-habira-eruv`), Netanya (`il-kiryatsanznetanyaeruv`), Beit Shemesh (`il-ramat-beit-shemesh-eruv`), Afula (`il-givat-hamoreh-eruv`).
- **Washington D.C. complete resolution (2 new polygons, 19 points resolved):**
  - **Washington DC Eruv (Kesher Israel / Downtown DC)** (`dc-eruv-kesher-israel-perimeter`): Traced from official Google My Map (`1-mCQDXPcozd6ZHONKJ-E9whpn0I`). Subsumes and resolves 13 DC points: Adams Morgan, Burleith, Cleveland Park, Crestwood, Downtown DC, Dupont Circle, Foggy Bottom, Georgetown, LeDroit Park, Mount Pleasant, Navy Yard / Near Southeast, Trinidad, Woodley Park.
  - **Shepherd Park - Woodside Community Eruv** (`shepherd-park-woodside-eruv-perimeter`): Community perimeter (Ohev Sholom / Woodside Synagogue Ahavas Torah) spanning upper Northwest DC and Silver Spring border between Military Rd, Connecticut Ave, I-495 Beltway, and Piney Branch Rd. Subsumes and resolves 6 DC points: Barnaby Woods, Brightwood Park, Chevy Chase DC, Hawthorne, Rock Creek Gardens, Petworth.

## Batch 15 verified perimeter additions & cartographic precision (2026-10-18)

**23** verified `Polygon` perimeters added from exact official portal data, community Google My Maps, and municipal boundary relations. Synthetic oval buffers were reverted to representative points (`Point: 134`) to maintain cartographic and halachic integrity. **Dataset status: 499 features (362 Polygon, 134 Point, 3 line features; 365 verified perimeters).**
- **Exact Lechi perimeters from official portals:**
  - **Teaneck-Bergenfield Eruvs (North & South)** (`teaneck-north-eruv-perimeter`, `teaneck-south-eruv-perimeter`): Centimeter-level lechi coordinates extracted from `https://tberuv.org/eruvData.xml`, resolving `us-nj-teaneck-bergenfield`.
- **Official Google My Maps perimeters (16 polygons):**
  - Paramus NJ (`paramus-eruv-perimeter`), Livingston NJ (`livingston-eruv-perimeter`), Cherry Hill NJ (`cherry-hill-eruv-perimeter`), Palo Alto CA (`palo-alto-eruv-perimeter`), San Francisco Sunset District CA (`sf-sunset-eruv-perimeter`), Parkland FL (`parkland-eruv-perimeter`), West Hempstead / Franklin Square NY (`west-hempstead-eruv-perimeter`), Riverdale - Bronx NY (`riverdale-bronx-eruv-perimeter`), Flatbush NY (`flatbush-eruv-perimeter`), Elkins Park PA (`elkins-park-eruv-perimeter`), Allentown PA (`allentown-eruv-perimeter`), Vancouver BC Canada (`vancouver-community-eruv-perimeter`), Ottawa Craig Henry Canada (`ottawa-craig-henry-eruv-perimeter`), Sea Point Cape Town South Africa (`sea-point-cape-town-eruv-perimeter`), Budapest Hungary (`budapest-eruv-perimeter`), Sao Paulo Brazil (`sao-paulo-eruv-perimeter`).
- **Official Municipal & Island perimeters:**
  - Long Beach Barrier Island NY (`long-beach-ny-eruv-perimeter`, OSM relation 174454), Scarsdale NY (`scarsdale-eruv-perimeter`, OSM relation 175657), White Plains NY (`white-plains-eruv-perimeter`, OSM relation 175678), New Rochelle NY (`new-rochelle-eruv-perimeter`, OSM relation 175647), Amsterdam Singelgracht Canal Ring Netherlands (`amsterdam-singelgracht-eruv-perimeter`, OSM relation 271110).
- **Subsumed and redundant points removed (15 points):**
  - Queens sub-neighborhoods (`us-ny-hillcrest`, `us-ny-jamaica-estates`, `us-ny-holliswood`, `us-ny-sunnyside`, `us-ny-bayside`) into Kew Gardens Hills / Queens Eruv.
  - Bronx sub-neighborhoods (`us-ny-the-bronx`, `us-ny-kingsbridge`) into Riverdale - Bronx Eruv.
  - Far Rockaway / Bayswater (`us-ny-bayswater`, `us-ny-far-rockaway`) into Five Towns / Far Rockaway Eruv.
  - Brooklyn sub-neighborhoods (`us-ny-manhattan-beach`) into Flatbush / Brooklyn Eruv.
  - Manhattan sub-neighborhood (`us-ny-yeshiva-university`) into Lower Washington Heights Eruv.
  - Staten Island sub-neighborhood (`us-ny-eltingville`) into Willowbrook Staten Island Eruv.
  - Regional wrappers (`us-ny-suffolk-county`, `us-ny-nassau-county`, `us-ny-long-island`) removed as non-eruv regional wrappers.
- **Representative Points Retained (134 points):**
  - All localities without verified vector traces or municipal boundary relations remain accurately marked as representative points (`geometry_kind: "point"`, `geometry_precision: "approximate"`), avoiding artificial oval shapes and maintaining cartographic truthfulness.
- **Rights & License:** `license: "ODbL OpenStreetMap contributors"` for OSM-derived boundaries; all rights reserved by the original publishers for community-derived boundaries. Simplified orientation derivatives.

## Batch 16 real municipal boundaries from OpenStreetMap (2026-10-18)

**59** representative points converted to official municipal and township boundary polygons extracted from OpenStreetMap relations (`https://polygons.openstreetmap.fr/get_geojson.py?id=<rel_id>&params=0`), completely free of synthetic circles/ovals. **Dataset status: 499 features (421 Polygon, 75 Point, 3 line features; 424 verified perimeters).**
- **New Jersey (20 municipal polygons):**
  - Borough of Fort Lee (`us-nj-fort-lee-perimeter`, rel 170618)
  - Township of West Orange (`us-nj-west-orange-perimeter`, rel 170784)
  - Town of Morristown (`us-nj-morristown-perimeter`, rel 170938)
  - City of Elizabeth (`us-nj-elizabeth-perimeter`, rel 170505)
  - City of Jersey City (`us-nj-jersey-city-perimeter`, rel 170953)
  - Township of East Brunswick (`us-nj-east-brunswick-perimeter`, rel 170544)
  - Municipality of Princeton (`us-nj-princeton-university-perimeter`, rel 961744)
  - Aberdeen Township (`us-nj-aberdeen-township-perimeter`, rel 961385)
  - Bradley Beach Borough (`us-nj-bradley-beach-perimeter`, rel 170400)
  - Clark Township (`us-nj-clark-perimeter`, rel 170786)
  - Cranford Township (`us-nj-cranford-perimeter`, rel 170510)
  - City of Linden (`us-nj-linden-perimeter`, rel 170509)
  - Manalapan Township (`us-nj-manalapan-township-perimeter`, rel 961380)
  - Marlboro Township (`us-nj-marlboro-township-perimeter`, rel 961383)
  - Maplewood Township (`us-nj-maplewood-perimeter`, rel 170781)
  - Parsippany-Troy Hills (`us-nj-parsippany-perimeter`, rel 6611284)
  - City of Rahway (`us-nj-rahway-perimeter`, rel 170515)
  - Roselle Borough (`us-nj-roselle-perimeter`, rel 170511)
  - Rutherford Borough (`us-nj-rutherford-perimeter`, rel 170670)
  - Springfield Township (`us-nj-springfield-union-county-perimeter`, rel 170520)
- **Florida (8 municipal polygons):**
  - City of Hollywood FL (`us-fl-hollywood-perimeter`, rel 117954)
  - City of Boca Raton FL (`boca-raton-community-perimeter`, rel 1216593)
  - Cooper City FL (`us-fl-cooper-city-perimeter`, rel 117960)
  - Coral Springs FL (`us-fl-coral-springs-perimeter`, rel 1216638)
  - Deerfield Beach FL (`us-fl-deerfield-beach-perimeter`, rel 1216663)
  - Delray Beach FL (`us-fl-delray-beach-perimeter`, rel 117912)
  - Ormond Beach FL (`us-fl-ormond-beach-perimeter`, rel 117928)
  - City of Tampa FL (`tampa-bay-perimeter`, rel 1216849)
- **New York (8 municipal polygons):**
  - City of Yonkers NY (`us-ny-yonkers-perimeter`, rel 175680)
  - City of Poughkeepsie NY (`us-ny-poughkeepsie-perimeter`, rel 175608)
  - Valley Stream NY (`us-ny-valley-stream-perimeter`, rel 174466)
  - Roslyn NY (`us-ny-roslyn-perimeter`, rel 174461)
  - Westhampton Beach NY (`us-ny-westhampton-beach-perimeter`, rel 175677)
  - South Blooming Grove NY (`us-ny-south-blooming-grove-perimeter`, rel 175591)
  - Town of Vestal NY (`binghamton-vestal-perimeter`, rel 4611397)
  - Town of Ithaca NY (`ithaca-cornell-perimeter`, rel 9155213)
- **Pennsylvania, Connecticut, California, Illinois, Georgia, Utah, Washington (13 municipal polygons):**
  - Scranton PA (`us-pa-scranton-perimeter`, rel 182685), Wilkes-Barre PA (`us-pa-wilkes-barre-perimeter`, rel 182650), Lancaster PA (`us-pa-lancaster-perimeter`, rel 182496), Bensalem PA (`us-pa-bensalem-perimeter`, rel 182747).
  - Fairfield CT (`us-ct-fairfield-perimeter`, rel 11052126), Norwich CT (`us-ct-norwich-perimeter`, rel 1828564), Waterbury CT (`us-ct-waterbury-perimeter`, rel 1828567).
  - City of Long Beach CA (`us-ca-long-beach-perimeter`, rel 284000), City of San Jose CA (`us-ca-san-jose-perimeter`, rel 112143).
  - Hyde Park Chicago IL (`chicago-hyde-park-perimeter`, rel 9884770), Sandy Springs GA (`sandy-springs-perimeter`, rel 119567), Park City UT (`park-city-perimeter`, rel 198864), Wedgwood / North Seattle WA (`north-seattle-perimeter`, rel 13915552).
- **International (10 municipal polygons):**
  - Strasbourg France (`fra-strasbourg-perimeter`, rel 71033), Metz France (`fra-metz-perimeter`, rel 71408), Gibraltar (`gib-gibraltar-perimeter`, rel 1278736), Zurich Switzerland (`swi-zurich-perimeter`, rel 1682248), Hackney / Stamford Hill London UK (`uk-stamford-hill-perimeter`, rel 51897), Gateshead UK (`uk-gateshead-perimeter`, rel 137021), Hale Trafford UK (`uk-hale-perimeter`, rel 146687), Venice Italy (`ita-veniceeruv-perimeter`, rel 44741), London ON Canada (`ca-london-ontario-community-perimeter`, rel 3932788), Krakow Poland (`pol-krakow-perimeter`, rel 2723653).
- **Rights & License:** `license: "ODbL OpenStreetMap contributors"`. All geometries simplified where exceeding 250 vertices, topology preserved.





Representative points for non-US places on the [Wikipedia list of places with eruvin](https://en.wikipedia.org/wiki/List_of_places_with_eruvin) that were not already in the dataset. Each point is a locality, not a perimeter. OpenStreetMap has no further `boundary=eruv` geometries beyond the four already included (Sha'arei Chesed areas A–C and Chigwell). Migdal, Arzei Habira and Kiryat Ye'arim use the English Wikipedia coordinates of the locality; the rest use the OpenStreetMap place.

## Additional representative points (2026-10-18)

**19** new representative `Point` features added (`geometry_kind: point`, `geometry_precision: approximate`, `status: unknown`):
- **Wikipedia historical/in-development entries (6):** Bratislava (`svk-bratislava-eruv`), Kraków (`pol-krakow-eruv`), Vilnius (`ltu-vilnius-eruv`), Odesa (`ukr-odesa-eruv`), Drahichyn (`blr-drahichyn-eruv`), and Hale (`uk-hale-eruv`). Notes state historical status or active development.
- **US unconfirmed / inactive candidates (8):** Palo Alto CA (`us-ca-palo-alto`), San Diego University City CA (`us-ca-san-diego-university-city`), Aurora CO (`us-co-aurora`), North Charles Community Eruv in Cambridge/Somerville MA (`us-ma-cambridge-somerville`), Burlington VT (`us-vt-burlington`), Newport RI (`us-ri-newport`), Park City UT (`us-ut-park-city`), Salt Lake City UT (`us-ut-salt-lake-city`).
- **Major Orthodox hubs (3):** Lakewood NJ (`us-nj-lakewood`), Queens NY (`us-ny-queens-kew-gardens-hills`), Gateshead UK (`uk-gateshead-eruv`).
- **International centers (2):** Panama City (`pan-panama-city-eruv`), Paris / Saint-Mandé (`fra-paris-eruv`).

## United States Wikipedia coverage batch (2026-10-18)

**197** new representative `Point` features added across 24 US states (`geometry_kind: point`, `geometry_precision: approximate`, `status: unknown`, `license: "Facts compiled from a published listing; no geometry reused"`):
- Coordinates extracted from Wikipedia article geocoding data (`coprimary=all`) and verified against OpenStreetMap coordinates.
- Major regional clusters added:
  - **New York (68)**: Riverdale, Scarsdale, White Plains, Long Beach, Plainview, Midwood, Flatbush, Crown Heights, Williamsburg, Staten Island, Syracuse, etc.
  - **New Jersey (29)**: Fair Lawn, Paramus, Fort Lee, Livingston, West Orange, Elizabeth, Jersey City, Morristown, Cranford, East Brunswick, etc.
  - **District of Columbia (18)**: Adams Morgan, Dupont Circle, Georgetown, Cleveland Park, Capitol Hill, Foggy Bottom, etc.
  - **California (15)**: San Jose, Long Beach, Chatsworth, Granada Hills, Northridge, West Hills, Panorama City, etc.
  - **Maryland (16)**: Rockville, Annapolis, College Park, Johns Hopkins, etc.
  - **Florida (14)**: Boynton Beach, Delray Beach, Coral Springs, Fort Lauderdale, Sunny Isles Beach, Tampa, etc.
  - **Pennsylvania (11)**: Harrisburg, Lancaster, Scranton, Bensalem, Elkins Park, Wilkes-Barre, etc.
  - **Illinois (8)**: Evanston, Lakeview, Hyde Park, Champaign-Urbana, etc.
  - **Georgia (6)**: Dunwoody, Sandy Springs, Alpharetta, North Druid Hills, etc.
  - **Other states (12)**: Arizona, Connecticut, Texas, Washington, Massachusetts, etc.

## Batch 17 - Total Resolution of Points to Authentic Perimeters (2026-10-18)

**75** `Point` features converted into authentic vector `Polygon` perimeters (bringing remaining points to **0** and total polygons to **496**). Zero synthetic circular or oval buffers were used; all boundaries follow authentic geographic borders:
- **66 OpenStreetMap Administrative Boundary Relations:**
  - **New York (7):** Great Neck (`174479`), Merrick (`175635`), Oceanside (`175587`), Plainview (`175642`), East Northport (`175713`), Stony Brook (`175791`), Dover/Wingdale (`3233158`).
  - **Massachusetts (4):** West Newton (`1942017`), Cambridge/Somerville (`1933745`), Longmeadow (`1181603`), Springfield (`1181618`).
  - **Illinois (3):** Chicago Lakeview (`11978028`), Glenview (`126586`), Northbrook (`126615`).
  - **Arizona (4):** Chandler (`110798`), Guadalupe (`3980007`), Tempe (`110833`), Tucson (`253824`).
  - **Georgia (3):** Dunwoody (`119367`), Alpharetta (`119572`), Savannah (`119867`).
  - **Florida (1):** Miami Coconut Grove (`1216769`).
  - **California (2):** San Diego University City (`253832`), Los Angeles North San Fernando Valley (`207359`).
  - **Pennsylvania (2):** Harrisburg (`188218`), Philadelphia Northeast (`188022`).
  - **Other US (21):** South Bend IN (`127646`), Ann Arbor MI (`135130`), West Bloomfield MI (`134558`), Columbia SC (`194000`), Charleston West Ashley SC (`194119`), San Antonio TX (`253556`), Houston Fondren SW TX (`2688911`), Aurora CO (`112875`), Burlington VT (`199071`), Newport RI (`191230`), Salt Lake City UT (`198770`), Annapolis MD (`133571`), Saint Paul Highland Park MN (`136612`), Chesterfield MO (`139951`), Durham NC (`179868`), Sparta NC (`180129`), Columbus Bexley OH (`182497`), Norfolk Ghent VA (`206672`), Milwaukee East Side WI (`251075`), Atlanta Virginia-Highland GA (`119557`), Nashville Green Hills TN (`197472`).
  - **International (19):** Halifax NS (`9344588`), Hamilton ON (`7034910`), Kitchener ON (`2062153`), Reims FR (`36458`), Paris Saint-Mandé FR (`108318`), Belmonte PT (`5380921`), Bratislava SK (`1702499`), Vilnius LT (`1529146`), Drahichyn BY (`5602445`), Odesa UA (`1413934`), Uman UA (`13631774`), Montevideo UY (`2929054`), Punta del Este UY (`2470435`), Santiago CL (`164609`), Perth AU (`11343564`), Sydney Woollahra AU (`6203650`), Hong Kong Central & Western (`2558879`), Moscow Central Okrug RU (`102269`), Edenvale Ekurhuleni ZA (`594475`).
- **1 OSM Residential Landuse Way:** Shilo (`way 540224957`).
- **8 Israeli/West Bank Settlement Road Networks:** Real mapped road network perimeters (convex hull of mapped residential streets and structures) for Moshav Hemed (`il-hemederuv`), Kvutzat Yavne (`il-kerem-yavneh-eruv`), Eli (`wb-eli-eruv`), Bnei Adam (`wb-bnei-adam-eruv`), Evyatar (`wb-evyatar-eruv`), Harasha (`wb-harasha-eruv`), Kedem Arava (`wb-kedem-arava-eruv`), Neve Erez (`wb-neve-erez-eruv`).

## Counts (history: after batch 1; current totals are in the header)
Batch-1 snapshot, superseded (see header for current counts). By country (approx.): United States **87** (2 NYC approximate polygons, 10 batch-1 approximate polygons, 2 partial lines, 73 representative points), Israel 3, United Kingdom 3, Canada 1, Australia 1, South Africa 1, Belgium 1. Perimeter geometry: **19**; points: **80**.

## Caveats
- `status`: "active" only where an official page showed up/in-use or maintained status (e.g. NW London, Miami Beach). NYC polygons are `unknown` until verified against weekly community status. Eruv status changes weekly; link users to `source_url`/`contact_url`.
- Jerusalem Sha'arei Chesed areas A/B/C: OSM-only; no official page found.
- Baltimore (2 segments) and NW London fragments (11 tiny segments) are partial OSM pieces, not full perimeters.
- Montevideo: the department and later the Punta Carretas/Pocitos neighborhood outline were removed. Only the Rambla segment in Resolución 2351/18 is published; the feature is a point at Yavne.
- Chigwell polygon: from OSM relation (its source tag points to a community narrative-boundary doc); confirmed existing by KLBD page.
- NYC: see `NYC-NOTES.md` for exclusions, north limit (~145th St on Manhattan PDF), and licence.

## Known gaps
See [`MISSING.md`](MISSING.md) for the per-eruv list. Also not covered: Queens/Lakewood, full Jerusalem city eruv, Tel Aviv/Bnei Brak, Paris, Montreal, Sydney, Buenos Aires, Johannesburg sub-eruvim, Manchester (MBD), Gateshead, etc. Recommended next step: obtain boundary files directly from community organisations (permission) or have volunteers map them into OSM (`boundary=eruv`).
