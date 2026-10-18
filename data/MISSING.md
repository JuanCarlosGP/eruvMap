# Eruvs without a perimeter (point only)

Reason codes: **NOMAP** no accessible official map found; **IMG** official map only as image/interactive without static data (needs georeferencing or the data); **BLOCK** site behind captcha/403 (not bypassed); **AMBIG** map exists but contour ambiguous; **OLD** outdated polygon.
No community has been contacted. "Where to ask" = the organisation that publishes the eruv, for Juan to decide.

Non-US places from the [Wikipedia list of places with eruvin](https://en.wikipedia.org/wiki/List_of_places_with_eruvin) were added on 2026-10-18 as representative points (Nominatim locality, no perimeter). Places already covered by a perimeter were not duplicated. Left off: Drahichyn, Vilnius, Kraków, Bratislava and Odesa (listed as not functional) and Hale (not yet completed). Migdal, Tzofim, Kerem B'Yavneh, Giv'at HaMoreh, Arzei Habira, Kiryat Ye'arim, Maoz Tzvi and Rehelim are now representative points. Migdal, Arzei Habira and Kiryat Ye'arim use the English Wikipedia locality coordinates; the other five use the OpenStreetMap place.

| id | Reason | Needed | Where to ask |
|---|---|---|---|
| us-ny-great-neck | BLOCK | Boundary map/KML of Great Neck Eiruv | Great Neck eruv organisation via its site (captcha-protected) |
| us-nj-teaneck-bergenfield | IMG | Teaneck/Bergenfield eruv map (PDF/KML) | Teaneck Eruv committee / local rabbinate |
| us-nj-cherry-hill-east / -west | BLOCK | Map/KML from eruvstat.us | Cherry Hill eruv committee |
| us-nj-princeton-university | AMBIG | PDF exists (Wayback) but georeferencing weak; need KML or labelled-intersection map | Princeton Chabad / Center for Jewish Life |
| us-pa-lower-merion | IMG | KML linked from yiml.org/eruv returned 404 | Main Line eruv organisation |
| us-pa-northeast-philadelphia | NOMAP | Rhawnhurst/Castor Gardens map | local shul/eruv committee |
| us-il-lincolnwood-peterson-park | IMG | Official boundary map (vector or KML). The cRc PDF page is a street atlas without a single closed line | Chicago Eruv / Lincolnwood eruv organisation |
| us-tx-san-antonio | NOMAP | Boundary description or map | Rodfei Sholom / Eruv of San Antonio |
| us-fl-boca-raton, us-fl-hollywood | IMG | Map as image/PDF with labelled streets, or KML | Boca Raton Synagogue / Young Israel Hollywood |
| us-mi-ann-arbor | IMG | a2eruv.org map data/KML | Ann Arbor eruv committee |
| us-oh-columbus | NOMAP | Boundary map (Berwick/Bexley/Eastmoor) | Columbus Torah Center / Agudas Achim |
| us-va-norfolk-ghent | AMBIG | Better-quality map than the Wayback scan | Norfolk Orthodox community (Ohef Sholom/Beth El area) |
| us-wa-mercer-island | AMBIG | Clean boundary line, or written street description | Mercer Island eruv organisation |
| us-fl-miami-beach (existing 2021 polygon) | OLD | 2025 CAD as KML/GIS, or one single-colour closed outline | Miami Beach Eruv / City of Miami Beach |
| johannesburg-eruv | NOMAP | Official map/sub-eruv boundaries | Johannesburg Beth Din |
| us-ca-la-west-valley-rosana-miller | AMBIG | Address-check polygon on oureruv.com closes with a ~3 km straight chord; need the real boundary | Rosana Miller Eruv |
| us-ct-fairfield | BLOCK | Page returned 403 | Congregation Ahavath Achim |
| us-ga-savannah | IMG | Embedded My Map KML returned 404; not confirmed as the eruv boundary | Congregation Bnai Brith Jacob |
| us-sc-columbia | AMBIG | Street list on the Chabad page, but Westbrook Rd does not meet Sandy Shore Rd in OSM (~600 m gap) plus a fence behind the Pep Boys | Chabad of South Carolina |
| us-in-south-bend, us-wi-milwaukee-east-side | NOMAP | Map image without coordinates (Milwaukee East Side site returned 404) | local Orthodox congregation running the eruv |
| Sydney, Stamford Hill, Bnei Brak, extra Jerusalem eruvim | NOMAP/IMG | Not (or only partly) in dataset; official map/KML | Sydney Beth Din / Stamford Hill Eruv committee / Bnei Brak municipality / Jerusalem Eruv authority |

General alternative: volunteers mapping `boundary=eruv` in OSM, then import with attribution.
