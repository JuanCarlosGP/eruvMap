import json,pickle,sys
sys.path.insert(0,'./raw1')
from shapely.geometry import mapping
res=pickle.load(open('./raw1/res.pkl','rb'))
LIC='All rights reserved by source; approximate traced derivative, shown with attribution pending community permission'
NOTE="Traced approximately from the official map; always check the community's official map and status before relying on it"
B='https://www.bostoneruv.org/bound.htm'; GB='Greater Boston Eruv Corporation (bostoneruv.org)'
S=[
('la','la-community-eruv-perimeter','Los Angeles Community Eruv','Los Angeles','CA','los-angeles-eruv','Los Angeles Community Eruv (laeruv.com)','https://laeruv.com/boundaries/','https://laeruv.com/boundaries/',''),
('miami','miami-beach-eruv-perimeter','Miami Beach / Bal Harbour Eruv','Miami Beach','FL','miami-beach-eruv','Miami Beach Eruv (miamibeacheruv.org)','https://www.miamibeacheruv.org/eruv-map','https://www.miamibeacheruv.org/eruv-map','Only the "Miami Beach/Bal Harbour Eruv" polygon of the 8-polygon South Florida map is traced; Aventura, Hallandale, Highland Lakes, North Miami Beach, Skylake and Sunny Isles are not included.'),
('5t','five-towns-eruv-perimeter','Five Towns Eruv','Woodmere / Cedarhurst / Lawrence / Hewlett','NY','us-ny-five-towns','Five Towns Eruv (fivetownseruv.org)','https://www.fivetownseruv.org/','https://www.fivetownseruv.org/','Outer envelope of ~35 route segments joined by morphological closing (~35 m); internal cut-offs, emergency cutoffs and excluded interior areas ignored.'),
('bos','greater-boston-eruv-perimeter','Greater Boston Eruv (Brookline / Newton / Brighton)','Brookline / Newton / Brighton','MA','us-ma-greater-boston',GB,B,B,'Traced from one of four embedded Google maps (Newton/South Brookline/Nonantum/Pike); gaps on the east side near Kenmore/Brookline were closed (~350 m closing) and the BU extension (only a JPG on bu_bound.htm) is NOT included. Cemeteries/ponds/golf courses ignored. Lower confidence on east edge.'),
('malden','malden-eruv-perimeter','Malden Eruv','Malden','MA',None,GB,B,B,'Two route lines joined by closing (~60 m).'),
('waltham','waltham-brandeis-eruv-perimeter','Brandeis / Waltham Eruv','Waltham','MA',None,GB,B,B,'Source line was already a closed ring.'),
('northshore','north-shore-swampscott-eruv-perimeter','North Shore (Swampscott) Eruv','Swampscott','MA',None,GB,B,B,'Map shows Phase 1 only; five segments joined by closing (~50 m).'),
('cle','cleveland-eruv-perimeter','Cleveland Eruv (East Side suburbs)','Cleveland Heights / University Heights / Beachwood / South Euclid','OH','us-oh-cleveland-heights','Cleveland Eruv Society (clevelanderuv.com)','https://clevelanderuv.com/eruv-map/','https://clevelanderuv.com/eruv-map/','Source ring already closed; small exclusion lines ignored.'),
('ss','silver-spring-eruv-perimeter','Silver Spring Eruv (Kemp Mill / Hillandale / White Oak / Wheaton)','Silver Spring','MD','us-md-silver-spring','Silver Spring Eruv Association (via Young Israel Shomrai Emunah, yise.org)','https://wp.yise.org/eruv/','https://wp.yise.org/eruv/','~25 segments joined by closing (~50 m).'),
('cc','center-city-philadelphia-eruv-perimeter','Center City Eruv (Philadelphia)','Philadelphia','PA','us-pa-center-city-philadelphia','Center City Eruv (centercityeruv.com)','https://www.centercityeruv.com/','https://www.centercityeruv.com/','Official GeoJSON of ~30 border segments joined by closing (~75 m); interior street segments ignored.'),
]
feats=[]
for k,i,n,c,st,rep,src,su,bu,ex in S:
    p=dict(id=i,name_en=n,city=c,country='US',state=st,geometry_kind='perimeter',status='unknown',source=src,source_url=su,boundary_map_url=bu,license=LIC,verified_at='2026-10-17',geometry_precision='approximate',note=NOTE+(' ('+ex+')' if ex else ''))
    if rep: p['replaces_id']=rep
    feats.append({'type':'Feature','properties':p,'geometry':mapping(res[k]['geom'])})
    print(i,res[k]['geom'].geom_type,res[k]['nv'],round(res[k]['iou'],3))
json.dump({'type':'FeatureCollection','features':feats},open('./batch1-eruvs.geojson','w'),separators=(',',':'))
