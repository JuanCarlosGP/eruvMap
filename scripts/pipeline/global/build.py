import json
D='2026-10-17'
OSM='ODbL OpenStreetMap contributors'
def r(c): return [round(c['lon'],6),round(c['lat'],6)]
def ring(g): return [r(p) for p in g]
F=[]
def add(geom,**p):
    p['verified_at']=D; F.append({"type":"Feature","properties":p,"geometry":geom})
osm=lambda t,i:f"https://www.openstreetmap.org/{t}/{i}"
# Jerusalem Sha'arei Chesed
for x in json.load(open('raw/q_nwrboundaryeruv.json'))['elements']:
    if x['type']=='way':
        a=x['tags']['name:en'].lower().split()[-1]
        c=ring(x['geometry']); assert c[0]==c[-1]
        add({"type":"Polygon","coordinates":[c]},id=f"jerusalem-shaarei-chesed-area-{a}",name_en=x['tags']['name:en'].replace('eruv','Eruv'),name_he=x['tags']['name'],city="Jerusalem",country="Israel",geometry_kind="perimeter",status="unknown",source=f"OpenStreetMap way {x['id']}",source_url=osm('way',x['id']),license=OSM,geometry_precision="exact",osm_id=f"way/{x['id']}",note="Geometry as mapped in OSM (boundary=eruv); no official community page confirmed; current operational status not verified.")
# Chigwell
w=json.load(open('raw/chigwell_way.json'))['elements'][0]['geometry']
c=ring(w); closed=c[0]==c[-1]
if not closed: c.append(c[0])
add({"type":"Polygon","coordinates":[c]},id="chigwell-hainault-eruv",name_en="Chigwell and Hainault Eruv",city="Chigwell",country="United Kingdom",geometry_kind="perimeter",status="unknown",source="OpenStreetMap relation 11776578; KLBD (London Eruvin) listing",source_url=osm('relation',11776578),license=OSM,geometry_precision="exact",osm_id="relation/11776578",contact_url="https://www.eruv.co.uk/eruvin/chigwell/",note="Geometry from OSM (its source tag cites the community's narrative boundary document). KLBD page confirms the eruv exists; weekly status must be checked there."+("" if closed else " OSM outer way was not closed; ring closed automatically."))
# Baltimore
for i,k in [(513968801,'a'),(515401544,'b')]:
    x=[e for e in json.load(open('raw/raw_geom.json'))['elements'] if e['id']==i][0]
    add({"type":"LineString","coordinates":ring(x['geometry'])},id=f"baltimore-md-osm-eruv-segment-{k}",name_en="Baltimore area eruv (partial segment, OSM)",city="Baltimore area",country="United States",geometry_kind="perimeter",status="unknown",source=f"OpenStreetMap way {i}",source_url=osm('way',i),license=OSM,geometry_precision="exact",osm_id=f"way/{i}",note=f"Partial segment only (eruv:type={x['tags'].get('eruv:type')}); not the full perimeter; no official source confirmed.")
# NW London fragments
fr=[ring(x['geometry']) for x in json.load(open('raw/raw2.json'))['elements'] if x['tags'].get('name')=='Eruv' and x['tags'].get('boundary')=='religious']
ids=[x['id'] for x in json.load(open('raw/raw2.json'))['elements'] if x['tags'].get('name')=='Eruv' and x['tags'].get('boundary')=='religious']
add({"type":"MultiLineString","coordinates":fr},id="nw-london-osm-eruv-fragments",name_en="NW London eruv (partial OSM fragments)",city="London",country="United Kingdom",geometry_kind="perimeter",status="unknown",source="OpenStreetMap ways "+", ".join(map(str,ids)),source_url=osm('way',ids[0]),license=OSM,geometry_precision="exact",contact_url="https://www.eruv.co.uk/",note="11 tiny OSM segments (boundary=religious, name=Eruv, religion=jewish) in Camden/Primrose Hill area; NOT a full perimeter. Use the official KLBD map for boundaries.")
# Points
pts=[
("nw-london-eruv","NW London Eruv","London","United Kingdom","KLBD (Kehillos London Beth Din) – London Eruvin","https://www.eruv.co.uk/","Golders Green","OSM node 2369008993",51.5718577,-0.1954797,"Official KLBD site states the NW London Eruv is up and in use (checked 2026-10-17); interactive map and weekly status on site."),
("manhattan-eruv","Manhattan Eruv","New York","United States","Manhattan Eruv (eruv.nyc)","https://eruv.nyc/","Manhattan","OSM relation 8398124 (Nominatim label point)",40.7579554,-73.9855319,"Official site: eruv encloses most of Manhattan; interactive boundary map and weekly status."),
("toronto-eruv","Toronto Eruv","Toronto","Canada","Toronto Eruv (Va'ad Harabonim of Toronto)","https://www.torontoeruv.org/boundaries/","Toronto","OSM relation 324211 (Nominatim label point)",43.6534817,-79.3839347,"Official site gives perimeter description; eruv spans from Major Mackenzie to CP tracks near Dupont; point is city centre only, eruv does not cover entire city."),
("melbourne-eruv","Melbourne Eruv","Melbourne","Australia","Council of Orthodox Synagogues of Victoria (COSV)","https://cosv.org.au/eruv/","Caulfield","OSM way 397008500 (Caulfield station, via Nominatim)",-37.8773433,145.0422715,"Official COSV page describes Melbourne Eruv (Caulfield, St Kilda, Elwood, Brighton, Moorabbin, Carnegie, Bentleigh, northern expansion); map in official app."),
("johannesburg-eruv","Greater Johannesburg Eruv (incl. Glenhazel)","Johannesburg","South Africa","Johannesburg Beth Din – Eruvin","https://jhbbethdin.co.za/eruvin/","Glenhazel","OSM node 262706657",-26.14,28.1008333,"Official Beth Din page publishes maps for Greater Johannesburg, Victory Park, Glenhazel and Orchards eruvim."),
("los-angeles-eruv","Los Angeles Community Eruv","Los Angeles","United States","LA Community Eruv (laeruv.com)","https://laeruv.com/boundaries/","Los Angeles","OSM relation 207359 (Nominatim label point)",34.0536923,-118.2427676,"Official site describes boundaries (10 Fwy/Western – Santa Monica Blvd – Cahuenga – 101 – 405); ArcGIS map viewer on site. Point is city centre (downtown LA is outside the eruv)."),
("miami-beach-eruv","Miami Beach Eruv","Miami Beach","United States","Miami Beach Eruv Council","https://www.miamibeacheruv.org/eruv-map","Miami Beach","OSM relation 118856 (Nominatim label point)",25.7929198,-80.1353006,"Official council map (PDF updated 2025-09-12); council manages eruv south of 73rd St; Surfside/Bal Harbour/Bay Harbor separated 2025-09-12."),
("antwerp-eruv","Antwerp Eruv","Antwerp","Belgium","Machsike Hadass Antwerp","https://www.machsike-hadass.be/eruv","Antwerp","OSM relation 59518 (Nominatim label point)",51.2211097,4.3997081,"Official Machsike Hadass page describes the city eruv, weekly checks and exclusions (hospitals, Berchembrug, Scheldt stretch); eruv.org directory also lists it."),
]
for id_,n,city,co,src,url,loc,cs,lat,lon,note in pts:
    add({"type":"Point","coordinates":[round(lon,6),round(lat,6)]},id=id_,name_en=n,city=city,country=co,geometry_kind="point",status="active" if id_ in("nw-london-eruv","manhattan-eruv","toronto-eruv","miami-beach-eruv") else "unknown",source=src,source_url=url,license=f"Eruv existence: official source (facts). Coordinates: {OSM}",geometry_precision="approximate",contact_url=url,coordinate_source=cs,note=note+" Point is a representative location, not the boundary.")
# status honesty: 'active' only where official page said up/in use
json.dump({"type":"FeatureCollection","name":"eruvim","features":F,"attribution":"Contains data © OpenStreetMap contributors, ODbL 1.0 (https://www.openstreetmap.org/copyright). Verified 2026-10-17."},open('eruvs.geojson','w'),ensure_ascii=False,separators=(',',':'))
import collections
print(len(F),collections.Counter((f['properties']['country'],f['geometry']['type']) for f in F))
