# US eruv verification report (2026-10-17, Europe/Madrid)

Scope: user-supplied leads treated as unverified. Public sources only; nobody was contacted; no aggregator data was copied (eruvfinder.com / eruvmaps.com / ShulMap / eruv.org were used only to discover leads, and are not cited as sources). No boundary was traced, downloaded or stored.

## Counts

- **80 confirmed eruv records** in `us-eruvs.geojson` across **32 states** (all Points, geometry_precision approximate).
- Status: 6 "active" (official page states up + a date; Fairfax, Cincinnati, West Valley LA, Cherry Hill East, Pittsburgh, Center City Philadelphia [stale: Aug 28]); 74 "unknown".
- Evidence: 49 records had their official page fetched by me today; 31 are confirmed from the official page text as returned by the search index only (the site blocked or errored on my fetch: HTTP 403/406/500/Cloudflare). Each record carries an `evidence` field. Treat those as lower assurance.
- Not confirmed / excluded: Palo Alto, UC San Diego, Aurora, Cambridge/Somerville, Burlington VT, Newport RI (non-functional), Park City UT (down), Salt Lake City. Already in app / not re-added: Manhattan, Brooklyn, Los Angeles Community Eruv, Miami Beach, Baltimore.
- Not on the user list but added because an official page confirmed them: Valley Eruv Society and Rosana Miller (West Valley) in LA, Aventura South, Hollywood FL, Great Neck, Highland Park/New Brunswick, Princeton University, Cherry Hill East/West, Northeast Philadelphia, Nashville West, Milwaukee East/West/Glendale, Dallas group, Houston group.

## Caveats

- Coordinates are Nominatim/OSM city or neighbourhood centroids (named by the official source). They are representative locations, not boundaries, and several eruvim span multiple towns; multiple eruvim in one city share one point.
- Where several eruvim are grouped (Dallas, Houston) a single marker stands for the group.
- Terms: no community states an open licence. Footers seen are "(c)" or "All rights reserved" (noted per row). Maps are Google My Maps / PDFs / custom viewers; I only list them. Portland says its public map is generalized and not for Shabbos use; Plano, Darchei Noam (MN), Overland Park, Cincinnati, Austin say maps are approximate; most pages say to confirm status before Shabbat.
- Status/hotline values come from the cited official page (hotline numbers for snapshot-only pages come from the search snapshot and should be rechecked). Status changes weekly; `status` is only "active" when the page itself gave a date.
- OSM: per earlier check (taginfo 2026-10-16) there are no US `boundary=eruv` objects; Overpass mirror was not re-queried. Nominatim was used only for geocoding.
- Not pushed to GitHub. Build script: `build_us.py`; raw fetched HTML in `raw/us/` (scratch, HTML pages only).

## Per-state tables

### Alabama

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Overton Eiruv (Birmingham) (Mountain Brook / Birmingham) | CONFIRMED | Knesseth Israel Congregation: https://www.kicong.org/eiruv | map on page (per snapshot) (https://www.kicong.org/eiruv) | not checked (page not directly fetchable) | unknown; (205) 969-5913 shul office | search snapshot only |

### Arizona

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Valley Eruv Project (Scottsdale Eruv) (Scottsdale / Phoenix / Paradise Valley) | CONFIRMED Note: Phoenix: only the part of Phoenix inside the VEP boundary is confirmed. | Valley Eruv Project / Ahavas Torah: https://www.ahavastorah.org/community/eruv/ | Google My Maps embed; detailed map at arizonaeruv.org (https://arizonaeruv.org/) | Ahavas Torah footer: "Copyright 2026 Ahavas Torah. All rights reserved." | unknown; weekly status posted at arizonaeruv.org | fetched |

### California

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Eastbayshore Eruv (Berkeley/Albany) (Berkeley) | CONFIRMED | Eastbayshore Eruv Corporation: https://www.berkeleyeruv.org/boundaries/ | Google My Maps embed + printable PDF (map updated Feb 2024) (https://www.berkeleyeruv.org/boundaries/) | Footer "(c) 2026 Eastbayshore Eruv"; no reuse licence; site says check boundary with committee | unknown; info@berkeleyeruv.org if status not posted by 3 pm | fetched |
| San Francisco Sunset District Eruv (San Francisco) | CONFIRMED Note: Established Sivan 5769; upgraded Jan 2024 per synagogue post. | Congregation Adath Israel: https://www.adathisraelsf.org/index.php?Itemid=147&id=7&option=com_content&view=article | map link "via Google" + certification PDF (https://www.adathisraelsf.org/index.php?Itemid=147&id=7&option=com_content&view=article) | none seen | unknown; status link on the same page; (415) 564-5665 office | fetched |
| College Area Eruv (San Diego) (San Diego) | CONFIRMED Note: Home page snapshot showed "Up and Operational" as of May 7, 2026 (stale), so status left unknown. | College Area Eruv, Inc. via Beth Jacob Congregation: https://www.bjsd.org/sderuv | not verified | not checked (page not directly fetchable) | unknown; COLLEGEAREAERUV@GMAIL.COM; status on bjsd.org home | search snapshot only |
| La Jolla Eruv (San Diego) (La Jolla, San Diego) | CONFIRMED | Congregation Adat Yeshurun: https://www.adatyeshurun.org/eruv | boundary map + boundary-details document on page (https://www.adatyeshurun.org/eruv) | not checked (page not directly fetchable) | unknown | search snapshot only |
| Irvine Community Eruv (Irvine) | CONFIRMED Note: Home page snapshot showed "Eruv is UP" dated May 14, 2026 (stale) so status left unknown. | Beth Jacob Congregation of Irvine: https://www.bethjacobirvine.org/eruv.html | map image on page (https://www.bethjacobirvine.org/eruv.html) | not checked (page not directly fetchable) | unknown; weekly status emails (info@bethjacobirvine.org) | search snapshot only |
| Valley Eruv Society (Eastern San Fernando Valley) (North Hollywood / Valley Village / Van Nuys / Sherman Oaks) | CONFIRMED Note: Distinct from the Los Angeles Community Eruv (already in app). | Valley Eruv Society: https://valleyeruv.org/about/ | Boundaries page on site (format not inspected) (https://valleyeruv.org/) | none seen | unknown | fetched |
| Rosana Miller (West Valley) Eruv (Encino / Tarzana / Woodland Hills) | CONFIRMED | The Rosana Miller Eruv: https://oureruv.com/ | interactive map + address check on site (https://oureruv.com/) | Footer: "Copyright 2012 - 2025 The Rosana Miller Eruv. All Rights Reserved" | active - Oct 16, 2026 (page: "Eruv is Up", Shabbat Noach); info@oureruv.com | fetched |
| Palo Alto | NOT CONFIRMED: only eruv.org directory + 2007/2013 news; no current official community page found | - | - | - | - | - |
| San Diego - University City | NOT CONFIRMED: only a 2015 local-news item quoting Chabad of UC; chabaduc.org page not seen | - | - | - | - | - |
| Los Angeles (Community Eruv) | ALREADY IN APP (point); not re-added. Valley eruvim added as separate records | - | - | - | - | - |

### Colorado

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| East Denver Eruv (Denver) | CONFIRMED Note: Aurora not confirmed on a primary source. | East Denver Eruv Committee: http://denvereruv.org/denver-eruv-map | printable PNG map + interactive Google map (http://denvereruv.org/denver-eruv-map) | none seen | unknown; info@denvereruv.org; status page denvereruv.org/eruv-status | fetched |
| Aurora | NOT CONFIRMED: only a 2018 CPR news story; no primary Ohr Avner page found | - | - | - | - | - |

### Connecticut

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| West Hartford Eruv (West Hartford) | CONFIRMED | West Hartford Eruv Committee / Young Israel of West Hartford: https://www.youngisraelwh.org/the-west-hartford-eruv.html | official map on page (per snapshot) (https://www.youngisraelwh.org/the-west-hartford-eruv.html) | not checked (page not directly fetchable) | unknown; 860-232-6417; @WHartfordEruv | search snapshot only |
| New Haven Eruv (and Yale Eruv) (New Haven) | CONFIRMED | New Haven Eruv, Inc.: https://www.nheruv.net/eurv-info/ | boundary maps (nheruv.net/yale-new-haven-maps/) + PDF (https://www.nheruv.net/yale-new-haven-maps/) | not checked (site returned errors to my fetches) | unknown; 203-387-3897 (Friday afternoon) | search snapshot only |
| Fairfield (Bridgeport/Fairfield) Eruv (Fairfield) | CONFIRMED Note: Bridgeport side not separately confirmed on a primary page. | Congregation Ahavath Achim: https://www.ahavathachim.org/jewish-living/eruv | no map seen; page lists boundary changes/restrictions | not checked (page not directly fetchable) | unknown; 203-583-9142 (synagogue) | search snapshot only |
| Bridgeport | PARTIAL: Bridgeport/Fairfield eruv is documented via Ahavath Achim (Fairfield) only; Bridgeport synagogue page not seen | - | - | - | - | - |

### Florida

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Boca Raton Community Eruv (Boca Raton) | CONFIRMED | Boca Raton Community Eruv / Boca Raton Synagogue: https://www.bocaeruv.org/ | not verified | none seen | unknown; Boca Raton Synagogue page: contact Rabbi Rabovsky 561-702-6714 | fetched |
| Aventura Eruv (Chabad Aventura) (Aventura) | CONFIRMED | Chabad Aventura: https://www.chabadfl.org/templates/articlecco_cdo/aid/1497904/jewish/Eruv.htm | not verified | not checked (page behind bot check) | unknown; 305-933-0770 | search snapshot only |
| Aventura South Eruv (Aventura) | CONFIRMED Note: Snapshot said "up" as of Mar 13, 2026 (stale). | Lubavitch Aventura South: https://www.lubavitchaventurasouth.org/templates/articlecco_cdo/aid/892394/jewish/ERUV-Aventura-South.htm | not verified; text boundaries (191st/Dixie to 180th/US-1) | not checked (page behind bot check) | unknown | search snapshot only |
| Hollywood Community Eruv (Hollywood / Fort Lauderdale) | CONFIRMED Note: Shul of Hollywood also publishes an eruv page. | Young Israel of Hollywood-Fort Lauderdale: https://yih.org/find-it-in-hollywood/local-eruv/ | viewable/printable map linked from page (https://yih.org/find-it-in-hollywood/local-eruv/) | none seen | unknown; contact the shul | fetched |
| Eruv of Jacksonville (Jacksonville) | CONFIRMED | Etz Chaim Synagogue: https://www.etzchaim.org/eruv-of-jacksonville.html | interactive map at jacksonvillejewish.com/eiruv + uMap (OSM-based) (https://www.jacksonvillejewish.com/eiruv) | not checked (page not directly fetchable) | unknown; (904) 262-3565 ext. 107 | search snapshot only |
| Miami Beach | ALREADY IN APP (point); not re-added | - | - | - | - | - |

### Georgia

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Toco Hills Eruv (Eruv of Atlanta) (Atlanta (Toco Hills)) | CONFIRMED Note: Old 2006 draft PDF at eruvofatlanta.org is outdated; not used. | Eruv of Atlanta, Inc. via Congregation Beth Jacob: https://www.bethjacobatlanta.org/eruv | official Google Maps link on page (per snapshot) (https://www.bethjacobatlanta.org/eruv) | not checked (page not directly fetchable) | unknown | search snapshot only |
| Savannah Eruv (Savannah) | CONFIRMED Note: Only evidence is the shul stating listed hotels are "within the Eruv"; no boundary/status page found. | Congregation Bnai Brith Jacob: https://www.bbjsynagogue.com/pages/visitors-information | page embeds a Google My Map (not verified to be the eruv boundary); hotels listed as inside the eruv (https://www.bbjsynagogue.com/pages/visitors-information) | none seen | unknown; 912-354-7721 (synagogue) | fetched |

### Illinois

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| West Rogers Park Eruv (Chicago) (Chicago) | CONFIRMED | Chicago Rabbinical Council (cRc): https://www.crcweb.org/guide_chicago.php | PDF maps (crcweb.org/eruv%20maps.pdf) (https://www.crcweb.org/eruv%20maps.pdf) | cRc footer: "Copyright. Chicago Rabbinical Council. All rights reserved." | unknown; (773) 743-7882 | fetched |
| Lincolnwood-Peterson Park Eruv (Lincolnwood / Chicago) | CONFIRMED | Chicago Rabbinical Council (cRc): https://www.crcweb.org/guide_chicago.php | PDF maps (crcweb.org/eruv%20maps.pdf) (https://www.crcweb.org/eruv%20maps.pdf) | cRc: All rights reserved | unknown; (847) 677-3788 | fetched |
| Skokie Eruv (Skokie) | CONFIRMED | Chicago Rabbinical Council (cRc): https://www.crcweb.org/guide_chicago.php | PDF maps (crcweb.org/eruv%20maps.pdf) (https://www.crcweb.org/eruv%20maps.pdf) | cRc: All rights reserved | unknown; (847) 679-3788 | fetched |

### Indiana

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Indianapolis Eiruv (Indianapolis) | CONFIRMED | Congregation B'nai Torah: https://www.btorahindy.org/faqs/ | map linked from FAQ (PDF) (https://www.btorahindy.org/faqs/) | FAQ says map is as accurate as possible; confirm status | unknown; (317) 253-5253, Fridays after 1 pm | fetched |
| South Bend Eruv (South Bend) | CONFIRMED | South Bend Torah Life: https://www.sbtorahlife.com/our-community | no map seen | Footer: "(c) 2023 SB Torah Life. All rights reserved." | unknown; 574-703-1750 (South Bend Eruv Association) | fetched |

### Kansas

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Overland Park Eruv (Overland Park) | CONFIRMED | Vaad of Kansas City / Congregation Beth Israel Abraham and Voliner: https://www.biav.org/community/local-eruv/ | Google My Maps viewer + physical boundary description (https://www.biav.org/community/local-eruv/) | Footer (c) 2026 BIAV; page says map is a guide, not a halachic ruling | unknown; Vaad KC 913-235-6077 | fetched |

### Kentucky

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Louisville Eruv (Dutchmans Lane / Highlands) (Louisville) | CONFIRMED Note: Home page has an "Eruv" menu item; the eruv page URL was not fetched. | Congregation Anshei Sfard: https://ansheisfard.com/ | not verified | none seen | unknown; 502-451-3122; WhatsApp weekly status | fetched |

### Louisiana

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Metairie Community Eruv (Metairie) | CONFIRMED Note: New Orleans proper not separately confirmed. | Congregation Beth Israel: https://www.bethisraelnola.com/community-eruv-fund | not verified | not checked (page not directly fetchable) | unknown; 504-454-5080 | search snapshot only |

### Maryland

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Silver Spring Eruv (Silver Spring) | CONFIRMED | Silver Spring Eruv Association / YISE: https://wp.yise.org/eruv/ | Google My Maps embed (https://wp.yise.org/eruv/) | Footer "(c) 2026"; no licence | unknown | fetched |
| Bethesda-Chevy Chase Eruv (Bethesda) | CONFIRMED Note: Only a one-line reference to the eruv map on the shul visitor page. | Congregation Beth El of Montgomery County: https://www.bethelmc.org/membership/visit/ | Google My Maps viewer link on page (https://www.bethelmc.org/membership/visit/) | none seen | unknown | fetched |
| Potomac Community Eruv (Potomac) | CONFIRMED | Young Israel Ezras Israel of Potomac: https://www.yieip.org/potomaceruv | not verified | not checked (page not directly fetchable) | unknown; status posted Fridays (per snapshot) | search snapshot only |
| Baltimore | CONFIRMED but ALREADY IN APP as 2 partial OSM line segments (avoid duplicate); official site eruvstat.us/baltimore (old eruvofbaltimore.org redirects there), 2026 PDF map https://eruvstat.us/sites/default/files/inline-images/Eruv_Map26-1.3-Fry_01_0.pdf, search snapshot said UP Oct 16, 2026, hotline 410-358-3788; direct fetch got 403 | - | - | - | - | - |

### Massachusetts

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Greater Boston Eruv (Brookline / Newton / Brighton) | CONFIRMED | Greater Boston Eruv Corporation: https://www.bostoneruv.org/bound.htm | 4 Google My Maps embeds + street-by-street text (https://www.bostoneruv.org/bound.htm) | none seen | unknown; 781-446-9797 | fetched |
| Cambridge/Somerville (North Charles Community Eruv) | NOT CONFIRMED on a primary site: only eruvstat.us/camberville (status host, bot-blocked; status "NOT CHECKED" Oct 9, 2026) | - | - | - | - | - |

### Michigan

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Detroit Eruv (Oak Park/Southfield) (Oak Park / Southfield) | CONFIRMED | Detroit Eruv: https://www.detroiteruv.org/ | interactive web map on site (https://www.detroiteruv.org/) | none seen | unknown; (248) 968-3788 | fetched |
| Ann Arbor Eruv (Ann Arbor) | CONFIRMED | Ann Arbor Orthodox Minyan: https://www.annarborminyan.org/eruv | not verified | none seen | unknown; a2eruv@a2eruv.org (via eruv.org listing) | fetched |

### Minnesota

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Minneapolis / St. Louis Park Eruv (St. Louis Park) | CONFIRMED | Congregation Darchei Noam: https://www.darcheinoammn.org/eruv-map | map on page; "Do not rely on this map alone" (https://www.darcheinoammn.org/eruv-map) | Footer (c) 2026 Darchei Noam; page says call hotline before Shabbat | unknown; 612-640-3788 | fetched |

### Missouri

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| St. Louis Community Eruv (University City / St. Louis) | CONFIRMED | St. Louis Community Eruv: https://stleruv.org/ | interactive + printable map (https://stleruv.org/) | none seen | unknown; (314) 863-1811 after 12:30 pm Fri (per snapshot of Bais Abraham page) | fetched |

### Nebraska

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Omaha Eruv (Omaha) | CONFIRMED | Beth Israel Synagogue: https://www.orthodoxomaha.org/erev.html | boundary maps on page (per snapshot) (https://www.orthodoxomaha.org/erev.html) | not checked (page not directly fetchable) | unknown; 402-556-6288 | search snapshot only |

### Nevada

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Las Vegas West Side Eruv (Las Vegas) | CONFIRMED | Community Kollel of Greater Las Vegas: https://www.lasvegaskollel.org/eruv | not verified | Footer (c) Community Kollel of Greater Las Vegas | unknown; weekly status on page | fetched |

### New Jersey

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Teaneck-Bergenfield Eruv (Teaneck) | CONFIRMED Note: Earlier KML check on the embedded map returned 404 (not publicly exportable). | RCBC Vaad / Teaneck-Bergenfield Area Eruv: https://rcbcvaad.org/teaneck-bergenfield-eruv/ | Google My Maps embed (rcbcvaad) + tberuv.org/Map.html (https://www.tberuv.org/Map.html) | none seen | unknown; (201) 530-0222 | fetched |
| Passaic-Clifton Eruv (Passaic / Clifton) | CONFIRMED | Passaic Clifton Eruv: https://www.pceruv.com/ | 2026 PDF map (https://www.pceruv.com/) | none seen | unknown; info@pceruv.com | fetched |
| Englewood Eruv (Englewood) | CONFIRMED | Congregation Ahavath Torah: https://www.ahavathtorah.org/eruv | boundary map on page (per snapshot) (https://www.ahavathtorah.org/eruv) | not checked (page not directly fetchable) | unknown; (201) 568-3116 Friday afternoon | search snapshot only |
| Cherry Hill East Eruv (Cherry Hill) | CONFIRMED Note: JCC extension was down on the status date. | Torah Links (Cherry Hill East Eruv): https://www.tlsnj.org/eruv | "Updated Map coming soon" | none seen | active - Oct 16-17, 2026 (page: UP; JCC extension DOWN); Rabbi Baruch Gore 818-687-4673 | fetched |
| Cherry Hill West Eruv (Cherry Hill) | CONFIRMED Note: Same city as East eruv; separate eruv. | Cherry Hill West Eruv / Torah Links: https://www.tlsnj.org/cherry-hill-west-eruv | map via eruvstat.us/cherryhillwest (per snapshot) (https://eruvstat.us/cherryhillwest) | none seen | unknown | fetched |
| Highland Park / New Brunswick Eruv (Highland Park) | CONFIRMED | Highland Park / New Brunswick Eruv: https://hperuv.org/ | Google My Maps embed (https://hperuv.org/) | none seen | unknown; status at hperuv.org/status | fetched |
| Princeton University Eruv (Princeton) | CONFIRMED Note: Government/university-type source. | Princeton University Facilities: https://facilities.princeton.edu/projects/the-princeton-university-eruv | not verified | not checked (page behind bot check) | unknown | search snapshot only |
| Lakewood (others) | NOT ADDED: no single boundary, contested reliance (per earlier research); Livingston/West Orange only seen in a search snippet, not verified | - | - | - | - | - |

### New York

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Monsey Eruv (Monsey) | CONFIRMED | The Eiruv of Monsey: https://eiruvofmonsey.org/ | PDF map + Google map + sections (https://eiruvofmonsey.org/pdf-map/) | Footer "(c) 2026 All Rights Reserved" | unknown; 845-584-5655; status page eiruvofmonsey.org/status/ | fetched |
| Five Towns Eruv (Woodmere / Cedarhurst / Lawrence) | CONFIRMED Note: Long Island. | Five Towns Eruv: https://fivetownseruv.org/ | 2 Google My Maps embeds (https://fivetownseruv.org/) | Footer "Copyright (c) 2015, Five Towns Eruv, all rights reserved." | unknown; 516-900-3831 | fetched |
| Great Neck Eiruv (Great Neck) | CONFIRMED Note: Long Island. | Eiruv Association of Great Neck: https://greatneckeiruv.org/ | not verified | not checked (page returned HTTP 202 to my fetch) | unknown | search snapshot only |
| Buffalo / Amherst Eruv (Amherst / Buffalo) | CONFIRMED Note: Federation article says eruv was reinstalled. | Young Israel of Greater Buffalo: https://www.yibuffalo.org/eruv | Google My Maps (edit link on page) (https://www.yibuffalo.org/eruv) | Footer (c) 2021 Young Israel of Greater Buffalo | unknown; 716-634-0212 | fetched |
| Rochester Eruv (Rochester) | CONFIRMED Note: Lower confidence: official shul page seen only via search snapshot; eruvstat.us status said NOT CHECKED (Oct 9, 2026). | Congregation Beth Sholom (eruv hosted on eruvstat.us): https://www.bethsholomrochester.org/general | map/status via eruvstat.us/rochester (https://eruvstat.us/rochester) | not checked (blocked) | unknown | search snapshot only |
| Manhattan, Brooklyn | ALREADY IN APP (polygons); not re-added | - | - | - | - | - |
| NYC other boroughs / Queens / Five Towns west | Not on list; not researched beyond Five Towns | - | - | - | - | - |

### North Carolina

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Charlotte Eruv (Charlotte) | CONFIRMED | Charlotte Torah Center: https://www.charlottetorahcenter.com/eruv | Google My Maps embed (https://www.charlottetorahcenter.com/eruv) | Footer (c) 2025 Charlotte Torah Center | unknown; status updated weekly on page | fetched |

### Ohio

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Cleveland Eruv (Cleveland Heights/University Heights) (Cleveland Heights) | CONFIRMED | Cleveland Eruv Society: https://clevelanderuv.com/eruv-map/ | Google My Maps embed (https://clevelanderuv.com/eruv-map/) | Footer (c) Cleveland Eruv Society 2021 | unknown; 216-586-9222 | fetched |
| Cincinnati Eruv (Cincinnati) | CONFIRMED | Cincinnati Eruv: https://www.cincinnatieruv.org/ | boundary PDF + approximate interactive map (https://www.cincinnatieruv.org/) | Footer "(c) 2026 Cincinnati Eruv. All rights reserved." | active - Oct 16, 2026 2:29 PM ("The Eruv is UP", Parshas Noach); (513) 351-3788 | fetched |
| Columbus Eruv (Berwick/Bexley/Eastmoor) (Columbus) | CONFIRMED | Columbus Eruv: https://eruv-columbus.com/eruv-map | map page (format not inspected) (https://eruv-columbus.com/eruv-map) | none seen | unknown; 614-489-8281 | fetched |

### Oregon

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Portland Eruv (Portland) | CONFIRMED Note: Site: detailed boundaries available only on request. | Portland Eruv: https://portlanderuv.com/boundaries/ | generalized Google My Map only; detailed boundaries NOT public (https://portlanderuv.com/boundaries/) | Footer (c) 2026; map "is not updated or maintained with actual boundaries. Do not rely on this map for Shabbos use." | unknown; status page portlanderuv.com/status | fetched |
| Eugene Eruv (Eugene) | CONFIRMED Note: Established 5779 (2019). | Congregation Ahavas Torah (Eugene): https://ahavastorah.info/kosher/kosher.htm | Google My Maps viewer + printable PDF (https://ahavastorah.info/kosher/kosher.htm) | none seen | unknown | fetched |

### Pennsylvania

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Center City Eruv (Philadelphia) (Philadelphia) | CONFIRMED Note: Status date is ~7 weeks old. | Center City Eruv: https://www.centercityeruv.com/ | interactive boundary map on site (https://www.centercityeruv.com/) | none seen | active - Aug 28, 2026 5:47 PM EDT (page: "currently up"; stale); status page on site | fetched |
| Lower Merion Eruv (Main Line) (Lower Merion) | CONFIRMED | Lower Merion Eruv / Young Israel of the Main Line: https://www.yiml.org/eruv | maps on lowermerioneruv.org (site not fetchable by me) (https://lowermerioneruv.org/wordpress/) | not checked | unknown | search snapshot only |
| Northeast Philadelphia (Rhawnhurst/Castor Gardens) Eruv (Philadelphia) | CONFIRMED | Northeast Eruv Corporation via Bnai Israel Ohev Zedek: https://www.biozshul.org/community/eruv/ | "Eruv Map" menu item on shul site (https://www.biozshul.org/community/eruv/) | none seen | unknown; (215) 333-3788 | fetched |
| Pittsburgh (Squirrel Hill/Oakland) Eruv (Pittsburgh) | CONFIRMED | Vaad Harabonim of Pittsburgh: https://www.vaadpgh.org/eruv/status-map | Google My Maps embed (https://www.vaadpgh.org/eruv/status-map) | none seen | active - Shabbos Noach 5787 (Oct 16-17, 2026): "KOSHER for Shabbos"; 412-421-1437 option 1 | fetched |
| Allentown Eruv (Allentown) | CONFIRMED | Congregation Sons of Israel: https://www.sonsofisrael.net/allentown-eruv.html | not verified | not checked (page not directly fetchable) | unknown | search snapshot only |

### Rhode Island

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Providence Eruv (Providence) | CONFIRMED Note: Newport eruv is documented as NOT functional; excluded. | Providence Eruv Corporation: https://proveruv.org/ | map and weekly status on site (per snapshot) (https://proveruv.org/) | not checked (site returned errors to my fetches) | unknown | search snapshot only |
| Newport | DOCUMENTED BUT NOT FUNCTIONAL: Congregation Jeshuat Israel page (fetched) says eruv "NOT currently functional" due to power-line maintenance; excluded | - | - | - | - | - |

### South Carolina

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Downtown Charleston Eruv (Charleston) | CONFIRMED Note: A second eruv (South Windermere, West Ashley) is listed only on eruv.org; not added. | Brith Sholom Beth Israel Synagogue: https://www.bsbisynagogue.org/eruv.html | eruv map on page (per snapshot) (https://www.bsbisynagogue.org/eruv.html) | not checked (page not directly fetchable) | unknown | search snapshot only |
| Columbia SC Eruv (Columbia) | CONFIRMED | Chabad of South Carolina: https://www.chabadofsc.com/templates/articlecco_cdo/aid/2289341/jewish/Eruv.htm | text boundary description only (per snapshot) | not checked (page behind bot check) | unknown | search snapshot only |
| Charleston - South Windermere (West Ashley) | Listed only on eruv.org; not added | - | - | - | - | - |

### Tennessee

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Eruv of Memphis (Memphis) | CONFIRMED | Baron Hirsch Congregation: https://www.baronhirsch.org/eruvofmemphis.html | not verified | not checked (page not directly fetchable) | unknown; (901) 683-7485 shul | search snapshot only |
| Nashville Eruv (Nashville) | CONFIRMED | Congregation Sherith Israel: https://www.sherithisrael.com/eruv | not verified | not checked (page not directly fetchable) | unknown; (615) 292-6614 | search snapshot only |
| Nashville Eruv - West (Bellevue) (Nashville (Bellevue)) | CONFIRMED | Chabad of Nashville: https://www.chabadnashville.com/templates/articlecco_cdo/aid/2852922/jewish/The-Map-for-the-Nashville-Eruv-West.htm | "Map for the Nashville Eruv - West" page (https://www.chabadnashville.com/templates/articlecco_cdo/aid/2852922/jewish/The-Map-for-the-Nashville-Eruv-West.htm) | not checked (page behind bot check) | unknown; (615) 646-5750 | search snapshot only |

### Texas

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Plano Eruv (Plano) | CONFIRMED | DATA of Plano / Congregation Lev Yisrael: https://www.congregationlevyisrael.org/plano-eruv | Google My Maps viewer (all three DFW eruv areas) (https://www.congregationlevyisrael.org/plano-eruv) | Footer (c) 2026 Congregation Lev Yisrael; "boundaries ... are not exact" | unknown; (917) 270-2990 Rabbi Zakon, updated Fridays | fetched |
| Dallas eruvin (Far North Dallas, North Dallas, Richardson, South of Forest) (Dallas) | CONFIRMED Note: DRC page lists the eruvin by name but gives no boundaries; this point is only a city-level marker for the group. | Dallas Rabbinical Council: https://www.dallasrabbinicalcouncil.org/rabbinic-services/eruvin/ | none on page | none seen | unknown; DRC (972) 835-6016 | fetched |
| Houston eruvin (Meyerland, UOS, Northfield area) (Houston) | CONFIRMED Note: TORCH also lists the Meyerland Minyan Eruv; no official weekly status page found. | Kollel of Houston (Eruv Maps page): https://kollelhouston.org/eruv-maps | Google My Maps embed + images (https://kollelhouston.org/eruv-maps) | none seen | unknown | fetched |
| Austin Eruv (Austin) | CONFIRMED Note: City of Austin documents (2012) exist at services.austintexas.gov/edims (ids 171814, 171517). | Austin Eruv Committee: https://austineruv.weebly.com/about.html | approximate boundaries in text | none seen | unknown; austineruv@gmail.com | fetched |
| San Antonio Eruv (San Antonio) | CONFIRMED | Eruv of San Antonio, Inc. via Rodfei Sholom: https://www.rodfeisholom.com/koshersa | not verified | not checked (page not directly fetchable) | unknown; (210) 493-3558 | search snapshot only |

### Utah

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Park City | EXCLUDED: Park City Jewish Community page (fetched) says the Canyons Village eruv "is not up"; no current eruv. Salt Lake City: none found | - | - | - | - | - |

### Vermont

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Burlington | NOT CONFIRMED: Chabad of Burlington page titled "Burlington Eruv" has only title+address (fetched), no description, boundary or status | - | - | - | - | - |

### Virginia

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Fairfax Eruv (Fairfax) | CONFIRMED | Fairfax Eruv Committee: https://www.fairfaxeruv.org/status.php | map page with boundary + hospital extension (https://www.fairfaxeruv.org/map.php) | none seen | active - Oct 16, 2026 ("The eruv is currently up"); weekly email/text alerts | fetched |
| Richmond Eruv (Richmond) | CONFIRMED | Keneseth Beth Israel: https://www.kbirva.com/visitrva | map on synagogue site (per snapshot) (https://www.kbirva.com/visitrva) | not checked (page not directly fetchable) | unknown; 804-288-7953 | search snapshot only |
| Norfolk (Ghent) Eruv (Norfolk) | CONFIRMED | Norfolk Torah Community / B'nai Israel: https://www.norfolktorahcommunity.com/jewish-norfolk-1 | PDF map linked from page (https://www.norfolktorahcommunity.com/jewish-norfolk-1) | none seen | unknown | fetched |

### Washington

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Seward Park Eruv (Seattle) (Seattle) | CONFIRMED | Bikur Cholim-Machzikay Hadath (BCMH): https://bcmhseattle.org/eruv/ | Google My Maps embed (https://bcmhseattle.org/eruv/) | none seen | unknown; 206-721-0970 (BCMH) | fetched |
| Mercer Island Eruv (Mercer Island) | CONFIRMED | Island Synagogue: https://www.islandsynagogue.org/eruv-map.html | ERUV Map page (https://www.islandsynagogue.org/eruv-map.html) | not checked (page not directly fetchable) | unknown | search snapshot only |

### Wisconsin

| Place / eruv | Result | Official source | Boundary map | Stated terms | Status / hotline | Evidence |
|---|---|---|---|---|---|---|
| Milwaukee East Side Eruv (Milwaukee) | CONFIRMED | East Side Eruv Committee: https://www.eastsideeruv.com/ | not verified | not checked (my fetch hit a hosting error) | unknown | search snapshot only |
| Milwaukee West Side Eruv (Milwaukee) | CONFIRMED Note: Same representative point as East Side; they are separate eruvin. | Congregation Beth Jehudah: https://bethjehudah.org/the-west-side-eruv/ | Google My Maps embed (https://bethjehudah.org/the-west-side-eruv/) | none seen | unknown; 414-444-3788 after 1 pm Friday | fetched |
| Glendale (Milwaukee) Eruv (Glendale) | CONFIRMED | Anshe Sfard Kehillat Torah: https://www.asktshul.org/eruv | not verified | not checked (page not directly fetchable) | unknown | search snapshot only |
