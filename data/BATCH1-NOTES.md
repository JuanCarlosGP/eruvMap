# BATCH1 eruv perimeters (2026-10-17)

Output: `batch1-eruvs.geojson` (10 Polygon features), previews `batch1-<slug>.png` (red = traced shape, blue = source linework, OSM tiles © OpenStreetMap contributors). Raw KMLs + scripts: `raw1/` (build1.py, mk.py). Not pushed to GitHub; nobody contacted.

## Method
1. Located official pages embedding each map (HTML fetched, `mid=` confirmed) -> source_url / boundary_map_url.
2. Read geometry via `google.com/maps/d/kml?mid=..&forcekml=1` (Philadelphia: official map-data.geojson) only to georeference.
3. Open route lines joined into rings by morphological closing (buffer r, fill holes, un-buffer), keeping outer envelope only (labels, points, internal cut-offs, cemeteries/ponds exclusions dropped). Existing closed polygons/rings used directly.
4. Douglas-Peucker simplification, max vertices per ring <=150 (actual 59-143), 5 decimals.
5. Visual check on OSM basemap. `replaces_id` set to the existing point ids. New perimeter ids are `*-perimeter`.
`trace_iou`: IoU of simplified vs. pre-simplification shape (0.97-1.0). It does NOT measure closing error.

## Per eruv (source page -> confidence)
| id | page (maps embedded) | verts | closing | confidence |
|---|---|---|---|---|
| la-community-eruv-perimeter (replaces los-angeles-eruv) | laeruv.com/boundaries/ (mid zYmw...) | 92 | none, source polygon | High |
| miami-beach-eruv-perimeter (replaces miami-beach-eruv) | miamibeacheruv.org/eruv-map | 143 | none, source polygon (Miami Beach/Bal Harbour only) | High (IoU .97, narrow spurs/causeway simplified) |
| five-towns-eruv-perimeter (replaces us-ny-five-towns) | fivetownseruv.org (both mids embedded on the home page; the two KMLs are near-identical, 1uh_ used) | 134 | ~35 m | Medium-high; looks right vs. OSM, internal cutoffs and sub-areas dropped |
| greater-boston-eruv-perimeter (replaces us-ma-greater-boston) | bostoneruv.org/bound.htm (mid 1tvzN...) | 136 | ~350 m, east side | Medium-low: east edge (Kenmore/Brookline) is interpolated; BU extension missing |
| malden-eruv-perimeter | bostoneruv.org/bound.htm (mid 1AS_c...) | 75 | ~60 m | Medium-high |
| waltham-brandeis-eruv-perimeter | bostoneruv.org/bound.htm (mid 17eM6...) | 62 | none | High |
| north-shore-swampscott-eruv-perimeter | bostoneruv.org/bound.htm (mid 1axrH...) | 59 | ~50 m | Medium-high (Phase 1 only) |
| cleveland-eruv-perimeter (replaces us-oh-cleveland-heights) | clevelanderuv.com/eruv-map/ | 59 | none, source ring | High |
| silver-spring-eruv-perimeter (replaces us-md-silver-spring) | wp.yise.org/eruv/ (SSEA map, mid 1WvS7...) | 142 | ~50 m | Medium-high; map may be older than the 2003 boundary PDF |
| center-city-philadelphia-eruv-perimeter (replaces us-pa-center-city-philadelphia) | centercityeruv.com (map-data.geojson) | 118 | ~75 m | Medium-high |

## Caveats
- Boston's four maps are four separate eruvim (main Newton/Brookline, Malden, Waltham/Brandeis, Swampscott), so output is four features. Malden, Waltham, Swampscott have no existing app point (nothing to replace). Main Boston: Brookline/Allston/BU north of the Pike is shown on the site only as GIF/JPG, so coverage is incomplete.
- Silver Spring: yise.org hosts the Silver Spring Eruv Association map (SSEA is independent of the shul); source attributed accordingly.
- Miami map also contains Aventura, Aventura South, Hallandale, Highland Lakes, North Miami Beach, Skylake, Sunny Isles polygons; not traced (not requested), easy to add.
- License: all rights reserved by sources; shown as approximate derivative pending community permission. Status all `unknown`. Use for display only, not halachic reliance.
