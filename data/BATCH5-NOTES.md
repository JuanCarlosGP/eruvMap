# Batch 5 notes (2026-10-17)

Same method as batches 1-4: approximate perimeter traced from the community's official map, `status: unknown`, `geometry_precision: approximate`, cited source and "official map" link. Nothing invented; nobody contacted; no aggregators.

## Traced (5, each replaces its point)
| Eruv | Source map | Registration | Precision |
|---|---|---|---|
| Cincinnati | cincinnatieruv.org PDF "Eruv Map November 2025" | edge-gradient template matching of the base map against an OSM tile mosaic | +/-30-40 m |
| Memphis | baronhirsch.org PNG "EruvMap2024withnotes" | 8 street-intersection GCPs + bounded road-raster refinement | +/-20-30 m |
| Omaha | orthodoxomaha.org boundary image | 5 GCPs + road refinement, overlay check | +/-15 m |
| Potomac | yieip.org/potomaceruv satellite PNG | 5 GCPs (affine), overlay check of MD 189 / I-270 / Bells Mill | +/-40 m |
| Indianapolis | btorahindy.org FAQ map PDF | 7 GCPs (residual 5-31 m), overlay check | +/-30 m |

GCPs are OSM street intersections (Overpass mirror maps.mail.ru). Each result was checked by drawing OSM roads over the source image.

## Not traced, and why
- **Norfolk**: map PDF returns 404 (also in Wayback). **Allentown**: PDF 406 / 404 in Wayback.
- **Richmond VA**: already traced from the KML in batch 4. **Charleston 2023**: PDF duplicates the 2022 KML already traced.
- **San Diego**: the image is a stock picture, not a map. **Jacksonville**: images are a group photo / not a boundary map.
- **Buffalo Grove**: ZeeMaps image; GCPs near-collinear and road matching diverged; no trustworthy fit, left as a point.
- **Lincolnwood**: tiny black-and-white scan, illegible. **Philadelphia NE**: grayscale map cropped by the frame; boundary not closed.
- **Mercer Island**: stylised cartography with side-of-street rules and ridge-line text, not a clean closed boundary. **La Jolla, Irvine, New Haven, St. Louis Park**: not registered in this batch (small/low-resolution or complex); remain points.
- **Austin**: image is a pre-construction sketch ("Start eruv construction on Phase 1...") on satellite; not an official final boundary.
- **Great Neck**: official image is behind a captcha (sgcaptcha); not bypassed, and no archived copy found.
- **No static map found** (no KML/mid in archived pages): Boca Raton, Hollywood FL, Ann Arbor, Las Vegas (Wix), Columbus, St. Louis, Cherry Hill (Wix, "updated map coming soon"), Princeton, Lower Merion (My Map private, 403), San Antonio.
- **Monsey SVG retry**: not attempted in this batch.

## Remaining
La Jolla, Irvine, New Haven, St. Louis Park, Mercer Island, Buffalo Grove (needs better GCPs), Monsey (SVG linework), Norfolk/Allentown if an alternative PDF appears.

License: all rights reserved by sources; approximate derivative pending community permission.
