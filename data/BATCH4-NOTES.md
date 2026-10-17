# BATCH4 eruv perimeters (2026-10-17)

Output: 29 `Polygon` features appended to `eruvs.geojson` (19 existing points replaced, 10 new areas). Same method and rules as batches 1-3 ([`BATCH1-NOTES.md`](BATCH1-NOTES.md), [`BATCH3-NOTES.md`](BATCH3-NOTES.md)): only maps published by (or embedded on the official page of) each community; approximate derived traces with `status: unknown`, cited `source_url` and `boundary_map_url`; nobody contacted; no aggregators (eruvfinder, ShulMap) used; Cloudflare/captcha blocks were **not** bypassed.

## What changed in the retrieval route
Pages that were unreachable in batch 3 were read through public **Wayback Machine** copies of the community's *own* page (CDX lookup, `id_` raw capture) to find the embedded Google My Maps id, then the map's public KML export (`/maps/d/kml?mid=..&forcekml=1`) was read as in batches 1-3. For the Baltimore JPG the archived image file was used. For Melbourne and Manchester the official pages themselves embed the boundary as JSON / JavaScript arrays (the COSV page embeds `eruv.herokuapp.com/map`, which reads a public JSON; the Manchester plans page contains `mainBoundaryData`/`whitefieldBoundaryData`).

## Traced from vector sources (KML / embedded polygon data)
| id (replaces) | official page | verts | method | confidence |
|---|---|---|---|---|
| toco-hills-eruv-perimeter (us-ga-atlanta-toco-hills) | bethjacobatlanta.org/eruv | 106 | route lines, closing ~50 m; Emory layer not traced | Medium-high |
| overton-eruv-perimeter (us-al-birmingham-overton) | kicong.org/eiruv | 23 | source polygon | High |
| charleston-downtown-eruv-perimeter (us-sc-charleston-downtown) | bsbisynagogue.org/eruv.html | 117 | route lines ~50 m, "Downtown" layer only | Medium-high |
| englewood-tenafly-eruv-perimeter (us-nj-englewood) | ahavathtorah.org/eruv | 97 | source polygon (2025 map) | High |
| glendale-wi / bayside-wi / mequon-eruv-perimeter (us-wi-glendale, -, -) | asktshul.org/eruv (Milwaukee Jewish community map) | 13 / 45 / 20 | source polygons; the Milwaukee East Side polygon is labelled PROPOSED and was **not** traced | High |
| aventura / aventura-south / hallandale / highland-lakes (us-fl-aventura, us-fl-aventura-south, -, -) | chabadchayil.org eruv page (embedded "Eruv Map of South Florida", legend colours blue/black/yellow/green) | 140 / 48 / 150 / 46 | source polygons | Medium (map titled 2021; page mentions later expansion of Highland Lakes) |
| nashville-sherith-israel-eruv-perimeter (us-tn-nashville) | sherithisrael.com/eruv | 39 | source polygon | High |
| overland-park-eruv-perimeter (us-ks-overland-park) | biav.org/community/local-eruv | 19 | source polygon | High |
| portland-main-eruv-perimeter (us-or-portland) | portlanderuv.com/boundaries | 72 | source polygon "Main Eruv Boundary" (small sub-eruvim omitted) | High |
| providence-eruv-perimeter (us-ri-providence) | proveruv.org | 99 | route lines ~50 m | Medium-high |
| richmond-va-eruv-perimeter (us-va-richmond) | kbirva.com/visitrva | 10 | source polygon | High |
| seward-park-eruv-perimeter (us-wa-seward-park) | bcmhseattle.org/eruv | 126 | route lines ~50 m (map June 2019) | Medium-high |
| skokie-eruv-perimeter (us-il-skokie) | skokieshul.org/eruv (Kehilat Chovevei Tzion) | 89 | route lines ~50 m | Medium-high |
| west-hartford-eruv-perimeter (us-ct-west-hartford) | youngisraelwh.org (KML 6/13/2018 on the page) | 85 | route lines ~50 m | Medium-high (2018) |
| rochester-eruv-perimeter (us-ny-rochester) | bethsholomrochester.org/general | 30 | route line ~50 m | Medium-high |
| bethesda-chevy-chase-eruv-perimeter (us-md-bethesda-chevy-chase) | bethelmc.org/membership/visit | 109 | 4 boundary lines ~60 m | Medium-high |
| melbourne-eruv-perimeter (melbourne-eruv) | cosv.org.au/eruv (embedded map JSON) | 141 | union of zones 1-3 incl. northern expansion | High (official data) |
| manchester-eruv-perimeter, whitefield-eruv-perimeter | manchestereruv.org.uk/plans.aspx | 135 / 91 | embedded boundary polygons; site says the map is simplified (real borders may be larger) | Medium-high |
| montreal-eruv-perimeter, outremont-eruv-perimeter | EruvStatus "Montreal Grand Eruv" page / montrealeruv.ca (Google My Map "Greater Hampstead Eruv") | 124 / 58 | union of Hampstead + Cote-St-Luc + CDN-NDG + De Vimy; Outremont separate; internal "out" holes ignored | High-medium |

## Traced from raster / vector PDFs registered to OSM (item 1 and others)
| id | source | registration | estimated precision |
|---|---|---|---|
| passaic-clifton-eruv-perimeter (us-nj-passaic-clifton) | pceruv.com 2026 vector PDF (red outline, filled area) | OSM road network rendered at candidate scale/rotation and matched to the PDF's street linework by normalised cross-correlation, then overlay check (scale 0.5687 m/px at 100 dpi, rotation 7.5 deg, median residual ~8 m) | +/-15-30 m |
| baltimore-eruv-perimeter | eruvstat.us/baltimore, 2025 "newly revised" JPG (obtained from the Wayback copy of 2026-03-24; live site is behind Cloudflare). Area = yellow fill delimited by the red line incl. Greengate Extension | I-695 / I-83 highway lines of the JPG matched to OSM motorways (NCC 0.71, 6.26 m/px = the stated 2.5 in = 1 mile); overlay of Reisterstown Rd, Park Heights Ave, Old Court Rd, Smith Ave, Greenspring Ave checked | +/-30-50 m |
| tel-aviv-yafo-eruv-perimeter | Tel Aviv-Yafo Religious Council, "map of the eruv line" JPG (28.08.2017, 1:53,000) | coastline of the map matched to OSM coastline (NCC 0.36, 6.1 m/px as per the stated scale), checked with the Ayalon highway and the municipal outline; gaps of the dashed blue line bridged (closing ~120 m) | +/-100-150 m; map dated 2017 |

All new polygons keep `geometry_precision: approximate`, `status: unknown`, simplified to <=150 vertices, 5 decimals.

## Not traced and why
- **Monsey** (official PDF, `eiruvofmonsey.org`): registration against OSM did not reach a trustworthy fit (legend colours of highways confuse the mask; best NCC 0.175 at the edge of the scale range). Not traced rather than guessed; the point `us-ny-monsey` stays.
- **Teaneck-Bergenfield**: the official RCBC page embeds a Google My Map (`mid=183scbULzO_...`) that now returns 404 (deleted/private); no cached KML and no other official map (tberuv.org only has status icons, and blocks automated access). Point stays.
- **Atlanta Emory eruv layer**: open segments, not a closed boundary. **Milwaukee East Side**: labelled PROPOSED. **Denver**: map contains only crossing/route directions. **Savannah**: map 404. **Charlotte**: directions route. **Fairfield CT**: old map (batch 3).
- **Miami zones**: Aventura, Aventura South, Hallandale and Highland Lakes are traced because the official Chabad Chayil page embeds that map and its legend names them. **North Miami Beach, Sunny Isles and Skylake** appear in the same map but are not described on any official page found (Skylake is "coming soon"): not traced. Miami Beach: see BATCH3 (still outdated map, official 2025 CAD PDF not retraced).
- **Chicago** (West Rogers Park, Lincolnwood, Skokie scans on crcweb.org): low-resolution, schematic 2010 scans; kept as points (Skokie is now replaced from the KCT map above).
- **Stamford Hill**: no official map (the Union eruv committee distributes a printed map; none published online). **Sydney**: the official site serves its map from an interactive app (Firebase); no downloadable boundary. **Montreal** official site is behind Cloudflare; its map was read from the archived EruvStatus page. **Bnei Brak / extra Jerusalem**: municipal religious-council page timed out and the neighbourhood maps (hiruv.com, a private eruv organisation) were not retrievable from the box; Jerusalem Sha'arei Chesed areas stay as OSM-only.
- **Remaining US points checked one by one**: images/PDFs exist but were not registered in this batch (candidates for the next one): Cincinnati (PDF Nov 2025), Indianapolis (`Eiruv-Map.pdf`), Norfolk (`Map-of-Eruv.pdf`), Omaha, Richmond JPG, San Diego, La Jolla (PDF/JPG), Irvine PNG, Mercer Island JPEG, Potomac PNG, Memphis PNG, Charleston 2023 PDF, Allentown PDF, New Haven 2007 PDF, Buffalo Grove PNG, Lincolnwood PNG, Northeast Philadelphia PNG, St. Louis Park JPG, Jacksonville inspection JPG. Points with no static map found: Boca Raton, Hollywood FL, Ann Arbor, Las Vegas, Columbus, St. Louis, Great Neck, Cherry Hill East/West, Princeton, Lower Merion (map id private), Austin, San Antonio, South Bend, Louisville, Metairie, Columbia SC, LA Valley / West Valley, SF Sunset, Nashville West.

## Next batches (suggested)
1. Register the listed raster maps with the same NCC-on-roads method (needs per-map colour masks and visual checks).
2. Monsey with the SVG linework of the PDF; Miami Beach from the 2025 CAD PDF.
3. Bnei Brak / Jerusalem neighbourhood maps when reachable; Sydney if a boundary file is published.

License: all rights reserved by sources; approximate derivative pending community permission. Display only, not for halachic reliance.
