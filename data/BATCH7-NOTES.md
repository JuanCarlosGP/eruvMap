# Batch 7 notes (branch `cursor/batch7-polygons`)

Rules: only official, citable maps; approximate perimeters (`status: unknown`, `geometry_precision: approximate`); no invented geometry; nobody contacted; no captcha/Cloudflare bypass.

## Traced (5 points -> perimeters, 1 commit each)
| Eruv | Source | Method | Est. precision |
|---|---|---|---|
| St. Louis Park (MN) | official community map | hand-picked street intersections vs OSM, affine fit | ~+/-30 m |
| Irvine (CA) | official community map | hand-picked intersections + road correlation | ~+/-40 m |
| La Jolla (CA) | official map | 3 hand control points vs OSM | ~+/-50 m |
| St. Louis (MO) | community's own published boundary array (`eruv-boundary.js` on its public map page) | coordinates used as published | as published |
| East Denver (CO) | official EDOS KML (`Eruv2024.kml`) | KML used as published | as published |
| New Haven (CT) | official nheruv.org PDF (Oct 2007) | boundary rings rebuilt from the PDF's vector paths; raster georeferenced to OSM by road correlation (rot 20.5 deg, 4.45 m/px, corr 0.65) with overlay check | ~+/-30-40 m |

(Total features remain 125: all replace points.) New Haven caveats: map is from 2007; hatched exclusions (Edgewood Park, Yale Farm, both cemeteries) are raster hatching and are not subtracted.

## Attempted and discarded
- **Norfolk (Ghent)**: only source is a Wayback scan; automatic correlation and RANSAC failed, hand-identified intersections not reliable enough.
- **Mercer Island**: official map shows a dotted boundary network (no single unambiguous closed contour); island-outline registration worked but closure is ambiguous.
- **Miami Beach**: CAD 2025 PDF is multi-colour partial polylines with ambiguous closure; georeference not rigorous. The existing 2021 polygon stays (outdated) -- see MISSING.md.
- **Princeton University**: vector PDF recovered via Wayback but road correlation vs OSM was weak (best 0.24, edge of scan range) -> not trusted, no polygon.
- **Great Neck** (sgcaptcha 202) and **Cherry Hill** (eruvstat.us 403): not bypassed.
- Other searches (Teaneck, Sydney, Stamford Hill, Chicago, Austin, Las Vegas, Boca Raton, Hollywood FL, Ann Arbor, Columbus, Lower Merion, San Antonio, Bnei Brak): no accessible official static map/vector/KML found within this batch's time; Sydney's app was not inspected beyond public pages.
