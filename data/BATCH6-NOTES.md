# Batch 6 notes (2026-10-17)

Same rules as batches 1-5: only official, citable community maps; approximate perimeters with `status: unknown`, `geometry_precision: approximate`, cited source and "official map" link; nothing invented; nobody contacted; no captcha/Cloudflare bypass; no aggregators (eruvfinder, ShulMap) used as sources. Georeferencing tool: OSM data via the Overpass mirror maps.mail.ru. New in this batch: **registration by template correlation of road linework** (no hand-picked control points) with overlay checks.

## Traced (4 features + 1 detached part; commit after each)
| Eruv | id | Source | Method | Precision |
|---|---|---|---|---|
| Monsey | `monsey-eruv-perimeter` (replaces `us-ny-monsey`) + `pearl-river-eruv-perimeter` | eiruvofmonsey.org/pdf-map, official PDF (vector, 2592x3456 pt) | Union of the 16 filled section polygons read from the PDF vector (no tracing by eye). Similarity transform fitted (scale search by correlation of the PDF's road vectors vs OSM major roads, then Powell optimisation against ~3,360 OSM tertiary+ roads): 5.84 m/pt, rotation -0.29 deg. Overlay: section edges follow the Thruway, Rt 59, Rt 45, Rt 306. Pearl River (section 5) is detached, so it is a separate feature (validator accepts only Polygon). Hole kept for the enclave near New City/Hillcrest; GoodSam Hospital Eruv not included. | +/-20-30 m |
| Allentown | `allentown-eruv-perimeter` (replaces `us-pa-allentown`) | sonsofisrael.net/allentown-eruv.html, red-line Google-Maps image (`images.shulcloud.com/14992/455648_orig.jpg`; the PDF of batch 5 was 406/404) | Registered by correlating the image's orange highways (US 22, PA 309, I-476) with OSM trunk/motorway (4.9 m/px, north-up, corr 0.61); vertices placed by hand along the red line (verified on overlay). | +/-30-50 m |
| Buffalo Grove | `buffalo-grove-eruv-perimeter` (new; no point existed) | Official ZeeMaps image ("Buffalo Grove Eruv", www.bgeruv.com, SAJE / National Eruv Initiative) | Basemap is OSM-style; yellow major roads correlated with OSM primary/secondary (7.25 m/px, corr 0.41 vs <=0.2 at all other scales); purple line segmented by colour and filled. Overlay of OSM roads coincides on Half Day, Aptakisic, Lake Cook, Dundee, Hintz. Fixes the batch 5 failure (near-collinear GCPs). | +/-15-25 m |

Previews (`/workspace/eruvmap-data/`): `batch6-mon.png`, `batch6-allentown.png`, `batch6-buffalo-grove.png`.

## Not traced, and why
- **Norfolk (Ghent)**: the 404 PDF of batch 5 was recovered from Wayback (capture 2016-08-24 of `216.104.180.25/wordpress/wp-content/uploads/2014/06/Map-of-Eruv.pdf`, linked from norfolktorahcommunity.com; Publisher file dated 2011): a clean black-and-white street map with a closed perimeter. But it is a hand-redrawn 1990s-style scan, with streets locally distorted and few readable street labels. Automatic registration (road-raster correlation, junction RANSAC) gave no consistent solution and I could not identify enough intersections without guessing, so no trace. Source file kept at `raw6/nor_img-000.jpg`. Needs 6+ carefully identified intersections.
- **Miami Beach (CAD 2025)**: the official PDF `ec5ef5_17da74fe...pdf` (AutoCAD LT 2023, 1728x2592 pt) is real vector with the street network, so rigorous georeferencing is feasible, but the eruv is drawn as several coloured polylines (seawall boundary, upgrades, poles on private fences, excluded hatched area, several detached islands) rather than a closed polygon. Not retraced in the time box; `miami-beach-eruv-perimeter` (2021 unaffiliated map, INACTIVE per the Council) is still outdated. Next step: extract the polylines by colour, georeference via the road network, and polygonise per the legend.
- **Irvine, St. Louis Park, La Jolla, New Haven**: images are screenshots of Google My Maps with either one linear feature (I-405 for Irvine; correlation is degenerate along the freeway) or no coloured major roads (St. Louis Park). Road-correlation did not converge to a single scale; still points. Needs hand-picked intersections (not done to avoid unreliable fits).
- **Teaneck-Bergenfield**: tberuv.org/Map.html is an interactive "locate an address" map; the only static images (`eruvSmall.gif`/`eruvLarge.gif`) are 180x74/400x164 thumbnails; rcbcvaad.org has no map file. Stays a point.
- **Sydney**: sydneyeruv.org.au/map is a JavaScript/Firebase app (data not exposed as a static file); older tripod map image (2010) is third-party hosted and stale. Stays a point.
- **Stamford Hill**: only news (JC) descriptions of the boundary; no official map found. **Bnei Brak**: no official eruv map found (municipal site only has bylaws). **Chicago**: nothing new beyond the 2010 CRC scans (see BATCH2-NOTES).
- Overpass mirror was unreliable (504 for large bboxes), which limited road data to tertiary+ for Monsey.

## Remaining
Norfolk (manual intersections), Miami Beach CAD (vector extraction), Irvine / St. Louis Park / La Jolla / New Haven (hand control points), Mercer Island, Teaneck, Sydney.

License: all rights reserved by sources; approximate derivative pending community permission. Display only, not for halachic reliance.
