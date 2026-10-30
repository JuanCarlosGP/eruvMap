# Eruv perimeter verification status

**Status as of 2026-10-30 (audit against PR #12 rules, keep-polygons policy):**

The dataset contains **499 features**:
- **495 Polygons** (`geometry_kind: "perimeter"`)
- **3 Lines** (`LineString` / `MultiLineString`)
- **1 representative point(s)** (`Point`)

Of the perimeter/line features:
- **182 boundary_verified: true** — geometry from an official eruv source (community KML/GeoJSON/PDF/My Maps/published coordinates, or OSM `boundary=eruv`), with the source cited
- **316 boundary_verified: false** — approximate **placeholder** perimeters kept so users can correct them in the suggest/edit tool by moving vertices; **not** from an official eruv map. Each has `boundary_basis` describing the placeholder origin.

Montevideo (`uru-montevideo-eruv`) remains a representative point: Resolución 2351/18 only authorizes the Rambla segment; inland sides are unpublished. Point at Yavne, Luis B. Cavia 2800, Pocitos.

## Why placeholders exist

After PR #12 (commit `2d6c425` / `7aaf6c6`, **125 features**: 89 polygons, 33 points, 3 lines) later commits on main converted many representative points into polygons taken from **OSM municipal/administrative relations, residential areas, and road-network outlines**, and “rescaled” some oversized municipal polygons to neighborhood OSM shapes. A municipal or neighborhood boundary is **not** an eruv perimeter.

Per product decision (2026-10-30), those geometries are **kept as polygons** (easier to correct by dragging vertices) but flagged:
- `boundary_verified: false`
- `boundary_basis`: `municipal_osm` | `admin_osm` | `neighborhood_osm` | `residential_osm` | `unverified`
- note explaining they are placeholder perimeters; corrections welcome

They must not be treated as halachic or surveyed eruv boundaries. Replace them only when an official community map can be traced (see [`docs/METHODOLOGY.md`](../docs/METHODOLOGY.md)).

## Unverified placeholder perimeters by basis


### Municipal / settlement OSM outlines used as placeholder perimeters (`boundary_basis: municipal_osm`, 232)

| id | name |
|---|---|
| `acre-eruv-perimeter` | Acre Eruv |
| `afula-eruv-perimeter` | Afula Eruv |
| `amsterdam-singelgracht-eruv-perimeter` | Amsterdam Singelgracht Canal Ring Eruv |
| `arad-eruv-perimeter` | Arad Eruv |
| `ariel-eruv-perimeter` | Ariel Eruv |
| `ashdod-eruv-perimeter` | Ashdod Eruv |
| `ashkelon-eruv-perimeter` | Ashkelon Eruv |
| `avnei-hefetz-eruv-perimeter` | Avnei Hefetz Eruv |
| `azor-eruv-perimeter` | Azor Eruv |
| `balfouria-eruv-perimeter` | Balfouria Eruv |
| `batyam-eruv-perimeter` | Bat Yam Eruv |
| `beersheba-eruv-perimeter` | Beersheba Eruv |
| `beitar-illit-eruv-perimeter` | Beitar Illit Eruv |
| `beitshean-eruv-perimeter` | Beit She'an Eruv |
| `beitshemesh-eruv-perimeter` | Beit Shemesh Eruv |
| `binghamton-vestal-perimeter` | Binghamton - Vestal Community Eruv Perimeter |
| `binyaminagivatada-eruv-perimeter` | Binyamina-Giv'at Ada Eruv |
| `bneiayish-eruv-perimeter` | Bnei Ayish Eruv |
| `bneibrak-eruv-perimeter` | Bnei Brak Eruv |
| `boca-raton-community-perimeter` | Boca Raton Community Eruv Perimeter |
| `ca-london-ontario-community-perimeter` | London Ontario Community Eruv Perimeter |
| `chicago-hyde-park-perimeter` | Hyde Park - University of Chicago Eruv Perimeter |
| `dimona-eruv-perimeter` | Dimona Eruv |
| `eilat-eruv-perimeter` | Eilat Eruv |
| `einharod-eruv-perimeter` | Ein Harod Eruv |
| `elad-eruv-perimeter` | El'ad Eruv |
| `fra-metz-perimeter` | Metz Eruv Perimeter |
| `fra-strasbourg-perimeter` | Strasbourg Eruv Perimeter |
| `ganeitikva-eruv-perimeter` | Ganei Tikva Eruv |
| `ganyavne-eruv-perimeter` | Gan Yavne Eruv |
| `gedera-eruv-perimeter` | Gedera Eruv |
| `givatayim-eruv-perimeter` | Giv'atayim Eruv |
| `givatshmuel-eruv-perimeter` | Giv'at Shmuel Eruv |
| `hadar-haifa-eruv-perimeter` | Hadar (Haifa) Eruv |
| `hadera-eruv-perimeter` | Hadera Eruv |
| `haifa-eruv-perimeter` | Haifa Eruv |
| `hatzorhaglilit-eruv-perimeter` | Hatzor HaGlilit Eruv |
| `herzliya-eruv-perimeter` | Herzliya Eruv |
| `hodhasharon-eruv-perimeter` | Hod HaSharon Eruv |
| `holon-eruv-perimeter` | Holon Eruv |
| `hoshaya-eruv-perimeter` | Hoshaya Eruv |
| `il-ahuzatbarakeruv-perimeter` | il-ahuzatbarakeruv Eruv Perimeter |
| `il-aminadaveruv-perimeter` | il-aminadaveruv Eruv Perimeter |
| `il-aviezereruv-perimeter` | il-aviezereruv Eruv Perimeter |
| `il-beit-hilkia-perimeter` | il-beit-hilkia-eruv Eruv Perimeter |
| `il-beitezraeruv-perimeter` | il-beitezraeruv Eruv Perimeter |
| `il-beitmeireruv-perimeter` | il-beitmeireruv Eruv Perimeter |
| `il-beitnekofaeruv-perimeter` | il-beitnekofaeruv Eruv Perimeter |
| `il-beitshikmaeruv-perimeter` | il-beitshikmaeruv Eruv Perimeter |
| `il-beituzieleruv-perimeter` | il-beituzieleruv Eruv Perimeter |
| `il-bekoa-perimeter` | il-bekoa-eruv Eruv Perimeter |
| `il-bnei-reem-perimeter` | il-bnei-reem-eruv Eruv Perimeter |
| `il-eitaneruv-perimeter` | il-eitaneruv Eruv Perimeter |
| `il-eshtaoleruv-perimeter` | il-eshtaoleruv Eruv Perimeter |
| `il-evensapireruv-perimeter` | il-evensapireruv Eruv Perimeter |
| `il-ganeihadareruv-perimeter` | il-ganeihadareruv Eruv Perimeter |
| `il-givatyearimeruv-perimeter` | il-givatyearimeruv Eruv Perimeter |
| `il-gizoeruv-perimeter` | il-gizoeruv Eruv Perimeter |
| `il-hafetzhaimeruv-perimeter` | il-hafetzhaimeruv Eruv Perimeter |
| `il-kfar-chabad-perimeter` | il-kfar-chabad-eruv Eruv Perimeter |
| `il-kiryat-yearim-perimeter` | Kiryat Yearim Eruv Perimeter |
| `il-kiryattivoneruv-perimeter` | Kiryat Tivon Eruv Perimeter |
| `il-mahseya-perimeter` | il-mahseya-eruv Eruv Perimeter |
| `il-mataeruv-perimeter` | il-mataeruv Eruv Perimeter |
| `il-matzliaheruv-perimeter` | il-matzliaheruv Eruv Perimeter |
| `il-mazkeret-batya-perimeter` | Mazkeret Batya Eruv Perimeter |
| `il-mevobeitareruv-perimeter` | il-mevobeitareruv Eruv Perimeter |
| `il-migdal-perimeter` | Migdal Eruv Perimeter |
| `il-mitzperamoneruv-perimeter` | Mitzpe Ramon Eruv Perimeter |
| `il-naaneruv-perimeter` | il-naaneruv Eruv Perimeter |
| `il-nahameruv-perimeter` | il-nahameruv Eruv Perimeter |
| `il-nehushaeruv-perimeter` | il-nehushaeruv Eruv Perimeter |
| `il-nesharimeruv-perimeter` | il-nesharimeruv Eruv Perimeter |
| `il-nessziona-perimeter` | Ness Ziona Eruv Perimeter |
| `il-nesszionaeruv-perimeter` | il-nesszionaeruv Eruv Perimeter |
| `il-netzerhazanieruv-perimeter` | il-netzerhazanieruv Eruv Perimeter |
| `il-nevemichaeleruv-perimeter` | il-nevemichaeleruv Eruv Perimeter |
| `il-noameruv-perimeter` | il-noameruv Eruv Perimeter |
| `il-talmeiyehieleruv-perimeter` | il-talmeiyehieleruv Eruv Perimeter |
| `il-taozeruv-perimeter` | il-taozeruv Eruv Perimeter |
| `il-tarumeruv-perimeter` | il-tarumeruv Eruv Perimeter |
| `il-tirosheruv-perimeter` | il-tirosheruv Eruv Perimeter |
| `il-tzafriaeruv-perimeter` | il-tzafriaeruv Eruv Perimeter |
| `il-tzelafon-perimeter` | il-tzelafon-eruv Eruv Perimeter |
| `il-yashresheruv-perimeter` | il-yashresheruv Eruv Perimeter |
| `il-zanoah-perimeter` | il-zanoah-eruv Eruv Perimeter |
| `il-zeitaneruv-perimeter` | il-zeitaneruv Eruv Perimeter |
| `il-zekharya-perimeter` | il-zekharya-eruv Eruv Perimeter |
| `ithaca-cornell-perimeter` | Ithaca - Cornell University Eruv Perimeter |
| `jerusalem-eruv-perimeter` | Jerusalem Eruv |
| `kadimazoran-eruv-perimeter` | Kadima-Zoran Eruv |
| `karmiel-eruv-perimeter` | Karmiel Eruv |
| `katzrin-eruv-perimeter` | Katzrin Eruv |
| `kfarmaas-eruv-perimeter` | Kfar Ma'as Eruv |
| `kfarsaba-eruv-perimeter` | Kfar Saba Eruv |
| `kfarshmaryahu-eruv-perimeter` | Kfar Shmaryahu Eruv |
| `kfartavor-eruv-perimeter` | Kfar Tavor Eruv |
| `kfaryona-eruv-perimeter` | Kfar Yona Eruv |
| `kiryatata-eruv-perimeter` | Kiryat Ata Eruv |
| `kiryatbialik-eruv-perimeter` | Kiryat Bialik Eruv |
| `kiryatekron-eruv-perimeter` | Kiryat Ekron Eruv |
| `kiryatgat-eruv-perimeter` | Kiryat Gat Eruv |
| `kiryatmalakhi-eruv-perimeter` | Kiryat Malakhi Eruv |
| `kiryatmotzkin-eruv-perimeter` | Kiryat Motzkin Eruv |
| `kiryatono-eruv-perimeter` | Kiryat Ono Eruv |
| `kiryatshmona-eruv-perimeter` | Kiryat Shmona Eruv |
| `kiryatyam-eruv-perimeter` | Kiryat Yam Eruv |
| `lehavim-eruv-perimeter` | Lehavim Eruv |
| `lod-eruv-perimeter` | Lod Eruv |
| `long-beach-ny-eruv-perimeter` | Long Beach Barrier Island Eruv |
| `maalottarshiha-eruv-perimeter` | Ma'alot-Tarshiha Eruv |
| `meitar-eruv-perimeter` | Meitar Eruv |
| `meron-eruv-perimeter` | Meron Eruv |
| `metula-eruv-perimeter` | Metula Eruv |
| `mevaseretzion-eruv-perimeter` | Mevaseret Zion Eruv |
| `migdalhaemek-eruv-perimeter` | Migdal HaEmek Eruv |
| `modiin-eruv-perimeter` | Modi'in Eruv |
| `nahariya-eruv-perimeter` | Nahariya Eruv |
| `netanya-eruv-perimeter` | Netanya Eruv |
| `netivot-eruv-perimeter` | Netivot Eruv |
| `new-rochelle-eruv-perimeter` | New Rochelle Eruv |
| `nofhagalil-eruv-perimeter` | Nof HaGalil Eruv |
| `north-seattle-perimeter` | North Seattle Community Eruv Perimeter |
| `ofakim-eruv-perimeter` | Ofakim Eruv |
| `omer-eruv-perimeter` | Omer Eruv |
| `oryehuda-eruv-perimeter` | Or Yehuda Eruv |
| `pardeshannakarkur-eruv-perimeter` | Pardes Hanna-Karkur Eruv |
| `park-city-perimeter` | Park City Community Eruv Perimeter |
| `petahtikva-eruv-perimeter` | Petah Tikva Eruv |
| `pol-krakow-perimeter` | Kraków Eruv Perimeter |
| `raanana-eruv-perimeter` | Ra'anana Eruv |
| `ramatgan-eruv-perimeter` | Ramat Gan Eruv |
| `ramathasharon-eruv-perimeter` | Ramat HaSharon Eruv |
| `ramatyishai-eruv-perimeter` | Ramat Yishai Eruv |
| `ramla-eruv-perimeter` | Ramla Eruv |
| `rehovot-eruv-perimeter` | Rehovot Eruv |
| `rekhasim-eruv-perimeter` | Rekhasim Eruv |
| `rishonlezion-eruv-perimeter` | Rishon LeZion Eruv |
| `roshhaayin-eruv-perimeter` | Rosh HaAyin Eruv |
| `roshpinna-eruv-perimeter` | Rosh Pinna Eruv |
| `safed-eruv-perimeter` | Safed Eruv |
| `sandy-springs-perimeter` | Sandy Springs Community Eruv Perimeter |
| `savyon-eruv-perimeter` | Savyon Eruv |
| `scarsdale-eruv-perimeter` | Scarsdale Community Eruv |
| `sderot-eruv-perimeter` | Sderot Eruv |
| `shlomi-eruv-perimeter` | Shlomi Eruv |
| `shoham-eruv-perimeter` | Shoham Eruv |
| `swi-zurich-perimeter` | Zurich Eruv Perimeter |
| `tiberias-eruv-perimeter` | Tiberias Eruv |
| `tzur-hadassah-eruv-perimeter` | Tzur Hadassah Eruv |
| `uk-gateshead-perimeter` | Gateshead Eruv Perimeter |
| `uk-hale-perimeter` | Hale Eruv Perimeter |
| `uk-stamford-hill-perimeter` | Stamford Hill Eruv Perimeter |
| `us-ca-long-beach-perimeter` | Long Beach Eruv Perimeter |
| `us-ct-fairfield-perimeter` | Fairfield (Bridgeport/Fairfield) Eruv Perimeter |
| `us-ct-norwich-perimeter` | Norwich Eruv Perimeter |
| `us-ct-waterbury-perimeter` | Waterbury Eruv Perimeter |
| `us-fl-cooper-city-perimeter` | Cooper City Eruv Perimeter |
| `us-fl-coral-springs-perimeter` | Coral Springs Eruv Perimeter |
| `us-fl-deerfield-beach-perimeter` | Deerfield Beach Eruv Perimeter |
| `us-fl-delray-beach-perimeter` | Delray Beach Eruv Perimeter |
| `us-fl-hollywood-perimeter` | Hollywood Community Eruv Perimeter |
| `us-fl-ormond-beach-perimeter` | Ormond Beach Eruv Perimeter |
| `us-nj-aberdeen-township-perimeter` | Aberdeen Township Eruv Perimeter |
| `us-nj-bradley-beach-perimeter` | Bradley Beach Eruv Perimeter |
| `us-nj-clark-perimeter` | Clark Eruv Perimeter |
| `us-nj-cranford-perimeter` | Cranford Eruv Perimeter |
| `us-nj-east-brunswick-perimeter` | East Brunswick Eruv Perimeter |
| `us-nj-elizabeth-perimeter` | Elizabeth Eruv Perimeter |
| `us-nj-fort-lee-perimeter` | Fort Lee Eruv Perimeter |
| `us-nj-jersey-city-perimeter` | Jersey City Eruv Perimeter |
| `us-nj-linden-perimeter` | Linden Eruv Perimeter |
| `us-nj-manalapan-township-perimeter` | Manalapan Township Eruv Perimeter |
| `us-nj-maplewood-perimeter` | Maplewood Eruv Perimeter |
| `us-nj-marlboro-township-perimeter` | Marlboro Township Eruv Perimeter |
| `us-nj-morristown-perimeter` | Morristown Eruv Perimeter |
| `us-nj-parsippany-perimeter` | Parsippany Eruv Perimeter |
| `us-nj-princeton-university-perimeter` | Princeton University Eruv Perimeter |
| `us-nj-rahway-perimeter` | Rahway Eruv Perimeter |
| `us-nj-roselle-perimeter` | Roselle Eruv Perimeter |
| `us-nj-rutherford-perimeter` | Rutherford Eruv Perimeter |
| `us-nj-springfield-union-county-perimeter` | Springfield (Union County) Eruv Perimeter |
| `us-nj-west-orange-perimeter` | West Orange Eruv Perimeter |
| `us-ny-poughkeepsie-perimeter` | Poughkeepsie Eruv Perimeter |
| `us-ny-roslyn-perimeter` | Roslyn Eruv Perimeter |
| `us-ny-south-blooming-grove-perimeter` | South Blooming Grove Eruv Perimeter |
| `us-ny-valley-stream-perimeter` | Valley Stream Eruv Perimeter |
| `us-ny-westhampton-beach-perimeter` | Westhampton Beach Eruv Perimeter |
| `us-ny-yonkers-perimeter` | Yonkers Eruv Perimeter |
| `us-pa-bensalem-perimeter` | Bensalem Eruv Perimeter |
| `us-pa-lancaster-perimeter` | Lancaster Eruv Perimeter |
| `us-pa-scranton-perimeter` | Scranton Eruv Perimeter |
| `us-pa-wilkes-barre-perimeter` | Wilkes-Barre Eruv Perimeter |
| `wb-ahiya-perimeter` | wb-ahiya-eruv Eruv Perimeter |
| `wb-beit-el-perimeter` | Beit El Eruv Perimeter |
| `wb-einav-perimeter` | wb-einav-eruv Eruv Perimeter |
| `wb-elon-moreh-perimeter` | wb-elon-moreh-eruv Eruv Perimeter |
| `wb-esh-kodesh-perimeter` | wb-esh-kodesh-eruv Eruv Perimeter |
| `wb-geva-binyamin-perimeter` | wb-geva-binyamin-eruv Eruv Perimeter |
| `wb-givat-harel-perimeter` | wb-givat-harel-eruv Eruv Perimeter |
| `wb-halamish-perimeter` | wb-halamish-eruv Eruv Perimeter |
| `wb-har-brakha-perimeter` | wb-har-brakha-eruv Eruv Perimeter |
| `wb-hinanit-perimeter` | wb-hinanit-eruv Eruv Perimeter |
| `wb-itamar-perimeter` | wb-itamar-eruv Eruv Perimeter |
| `wb-kfar-tapuach-perimeter` | wb-kfar-tapuach-eruv Eruv Perimeter |
| `wb-kokhav-hashahar-perimeter` | wb-kokhav-hashahar-eruv Eruv Perimeter |
| `wb-kokhav-yaakov-perimeter` | wb-kokhav-yaakov-eruv Eruv Perimeter |
| `wb-leshem-perimeter` | wb-leshem-eruv Eruv Perimeter |
| `wb-maale-adumim-perimeter` | Maale Adumim Eruv Perimeter |
| `wb-maoz-tzvi-perimeter` | wb-maoz-tzvi-eruv Eruv Perimeter |
| `wb-mevo-dotan-perimeter` | wb-mevo-dotan-eruv Eruv Perimeter |
| `wb-mevo-horon-perimeter` | wb-mevo-horon-eruv Eruv Perimeter |
| `wb-mitzpe-yeriho-perimeter` | wb-mitzpe-yeriho-eruv Eruv Perimeter |
| `wb-modiin-illit-perimeter` | wb-modiin-illit-eruv Eruv Perimeter |
| `wb-peduel-perimeter` | wb-peduel-eruv Eruv Perimeter |
| `wb-rehelim-perimeter` | wb-rehelim-eruv Eruv Perimeter |
| `wb-revava-perimeter` | wb-revava-eruv Eruv Perimeter |
| `wb-rotem-perimeter` | wb-rotem-eruv Eruv Perimeter |
| `wb-salit-perimeter` | wb-salit-eruv Eruv Perimeter |
| `wb-shaked-perimeter` | wb-shaked-eruv Eruv Perimeter |
| `wb-shvut-rachel-perimeter` | wb-shvut-rachel-eruv Eruv Perimeter |
| `wb-tal-menashe-perimeter` | wb-tal-menashe-eruv Eruv Perimeter |
| `wb-talmon-perimeter` | wb-talmon-eruv Eruv Perimeter |
| `wb-tel-zion-perimeter` | wb-tel-zion-eruv Eruv Perimeter |
| `wb-tzofim-perimeter` | wb-tzofim-eruv Eruv Perimeter |
| `wb-yitzhar-perimeter` | wb-yitzhar-eruv Eruv Perimeter |
| `white-plains-eruv-perimeter` | White Plains Eruv |
| `yavne-eruv-perimeter` | Yavne Eruv |
| `yavneel-eruv-perimeter` | Yavne'el Eruv |
| `yehudmonosson-eruv-perimeter` | Yehud-Monosson Eruv |
| `yokneamillit-eruv-perimeter` | Yokneam Illit Eruv |
| `zikhronyaakov-eruv-perimeter` | Zikhron Ya'akov Eruv |

### OSM administrative boundary relations (`boundary_basis: admin_osm`, 48)

| id | name |
|---|---|
| `aus-perth-eruv` | Perth Eruv |
| `aus-sydney-eruv-eastern-suburbs` | Sydney Eruv (Eastern Suburbs) Eruv |
| `blr-drahichyn-eruv` | Drahichyn Eruv |
| `ca-kitchener-eruv` | Kitchener Eruv |
| `chi-santiago-eruv` | Santiago Eruv |
| `fra-paris-eruv` | Paris (Metropolitan Area / Saint-Mandé) Eruv |
| `fra-reims-eruv` | Reims Eruv |
| `hk-hong-kong-eruv` | Hong Kong Eruv |
| `ltu-vilnius-eruv` | Vilnius Eruv |
| `por-belmonte-eruv` | Belmonte Eruv |
| `svk-bratislava-eruv` | Bratislava Eruv |
| `ukr-odesa-eruv` | Odesa Eruv |
| `ukr-umaneruv` | Uman Eruv |
| `uru-punta-del-este-eruv` | Punta del Este Eruv |
| `us-az-chandler` | Chandler Eruv |
| `us-az-guadalupe` | Guadalupe Eruv |
| `us-az-tempe` | Tempe Eruv |
| `us-ga-alpharetta` | Alpharetta Eruv |
| `us-ga-dunwoody` | Dunwoody Eruv |
| `us-ga-savannah` | Savannah Eruv |
| `us-il-glenview` | Glenview Eruv |
| `us-il-lakeview` | Lakeview Eruv |
| `us-il-northbrook` | Northbrook Eruv |
| `us-in-south-bend` | South Bend Eruv |
| `us-ma-cambridge-somerville` | North Charles Community Eruv (Cambridge/Somerville) Eruv |
| `us-ma-longmeadow` | Longmeadow Eruv |
| `us-ma-springfield` | Springfield Eruv |
| `us-ma-west-newton` | West Newton Eruv |
| `us-md-annapolis` | Annapolis Eruv |
| `us-mi-ann-arbor` | Ann Arbor Eruv |
| `us-mi-west-bloomfield-township` | West Bloomfield Township Eruv |
| `us-mn-highland-park-saint-paul` | Highland Park, Saint Paul Eruv |
| `us-mo-chesterfield` | Chesterfield Eruv |
| `us-nc-durham` | Durham Eruv |
| `us-nc-sparta` | Sparta Eruv |
| `us-ny-east-northport` | East Northport Eruv |
| `us-ny-great-neck` | Great Neck Eiruv Eruv |
| `us-ny-merrick` | Merrick Eruv |
| `us-ny-oceanside` | Oceanside Eruv |
| `us-ny-plainview` | Plainview Eruv |
| `us-ny-stony-brook` | Stony Brook Eruv |
| `us-ny-wingdale` | Wingdale Eruv |
| `us-oh-columbus` | Columbus Eruv (Berwick/Bexley/Eastmoor) Eruv |
| `us-pa-harrisburg` | Harrisburg Eruv |
| `us-ri-newport` | Newport Eruv |
| `us-sc-columbia` | Columbia SC Eruv |
| `us-ut-salt-lake-city` | Salt Lake City Eruv |
| `us-vt-burlington` | Burlington Eruv |

### OSM neighborhood / road-network / rescaled neighborhood outlines (`boundary_basis: neighborhood_osm`, 17)

| id | name |
|---|---|
| `atlanta-intown-virginia-highland-eruv` | Intown Atlanta (Virginia-Highland / Morningside) Eruv |
| `ca-halifax-eruv` | Halifax Eruv |
| `ca-hamilton-community-eruv` | Hamilton Community Eruv |
| `la-north-valley-eruv` | North San Fernando Valley Eruv |
| `tampa-bay-perimeter` | Tampa Palms - Temple Terrace Eruv Perimeter |
| `us-az-tucson` | Tucson Eruv |
| `us-ca-san-diego-university-city` | University City Eruv (San Diego) Eruv |
| `us-ca-san-jose-perimeter` | San Jose Eruv Perimeter |
| `us-co-aurora` | Aurora Eruv |
| `us-fl-coconut-grove` | Coconut Grove Eruv |
| `us-pa-northeast-philadelphia` | Northeast Philadelphia (Rhawnhurst/Castor Gardens) Eruv |
| `us-sc-west-ashley` | West Ashley Eruv |
| `us-tn-green-hills` | Green Hills Eruv |
| `us-tx-san-antonio` | San Antonio Eruv |
| `us-va-norfolk-ghent` | Norfolk (Ghent) Eruv |
| `us-wi-milwaukee-east-side` | Milwaukee East Side Eruv |
| `za-edenvale-eruv` | Edenvale Eruv |

### OSM residential landuse or settlement road perimeters (`boundary_basis: residential_osm`, 8)

| id | name |
|---|---|
| `il-hemederuv` | il-hemederuv Eruv |
| `wb-bnei-adam-eruv` | wb-bnei-adam-eruv Eruv |
| `wb-eli-eruv` | wb-eli-eruv Eruv |
| `wb-evyatar-eruv` | wb-evyatar-eruv Eruv |
| `wb-harasha-eruv` | wb-harasha-eruv Eruv |
| `wb-kedem-arava-eruv` | wb-kedem-arava-eruv Eruv |
| `wb-neve-erez-eruv` | wb-neve-erez-eruv Eruv |
| `wb-shilo-eruv` | wb-shilo-eruv Eruv |

### No verifiable official eruv-map geometry cited (`boundary_basis: unverified`, 11)

| id | name |
|---|---|
| `canvey-island-eruv-perimeter` | Canvey Island Eruv |
| `gib-gibraltar-perimeter` | Gibraltar Eruv Perimeter |
| `il-kerem-yavneh-eruv` | il-kerem-yavneh-eruv Eruv |
| `ita-veniceeruv-perimeter` | Venice Eruv Perimeter |
| `melilla-eruv-perimeter` | Melilla Community Eruv |
| `mercer-island-eruv-perimeter` | Mercer Island Eruv |
| `rus-moscoweruv` | Moscow Eruv |
| `shepherd-park-woodside-eruv-perimeter` | Shepherd Park - Woodside Community Eruv |
| `teaneck-north-eruv-perimeter` | Teaneck-Bergenfield North Eruv |
| `teaneck-south-eruv-perimeter` | Teaneck-Bergenfield South Eruv |
| `us-tx-fondren-southwest` | Fondren Southwest Eruv |

## Next steps

1. Prefer correcting an unverified polygon in the map tool over drawing from scratch.
2. Promote `boundary_verified` to `true` only when geometry is re-traced from an official community eruv map (and drop `boundary_basis`).
3. Do **not** treat OSM `admin_level`, place, landuse, or road-network polygons as finished eruv geometry.
4. Encourage local inspectors to tag `boundary=eruv` in OpenStreetMap when they publish a real perimeter.
