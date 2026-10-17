import json,pickle,sys
from shapely.geometry import mapping
sys.path.insert(0,'./raw2')
res=pickle.load(open('./raw2/res2.pkl','rb'))
LIC='All rights reserved by source; approximate traced derivative, shown with attribution pending community permission'
NOTE="Traced approximately from the official map; always check the community's official map and status before relying on it"
TE='https://www.torontoeruv.org/boundaries/'
S=[
('det','detroit-eruv-perimeter','Detroit Eruv (Oak Park / Southfield / Huntington Woods)','Oak Park / Southfield','US','MI','us-mi-detroit-oak-park-southfield','The Detroit Eruv (detroiteruv.org)','https://www.detroiteruv.org/eruv','https://www.detroiteruv.org/eruv','Ring published by the community as the "current boundary" of the operational eruv (folder "original main eruv"); planned expansion into Berkley is not included.'),
('tn','toronto-north-eruv-perimeter','Toronto Eruv - North section (401 to 407)','Toronto / Vaughan / Thornhill','CA',None,'toronto-eruv','Toronto Eruv (torontoeruv.org)',TE,TE,'Official map draws two sections ("North eruv - the 401 up to the 407" and "South eruv - the CP tracks up to the 401"), kept as two features; the site lists where the 401 may be crossed (Bathurst, Wilson, Bayview only). Richmond Hill is a separate eruv.'),
('ts','toronto-south-eruv-perimeter','Toronto Eruv - South section (CP tracks to 401)','Toronto','CA',None,None,'Toronto Eruv (torontoeruv.org)',TE,TE,'Second section of the official two-section map; see the North section note.'),
('trh','richmond-hill-eruv-perimeter','Richmond Hill Eruv','Richmond Hill','CA',None,None,'Toronto Eruv (torontoeruv.org) - map shows it as a separate eruv with no crossover from the Toronto north eruv',TE,TE,'Shown on the Toronto Eruv official map as "a separate eruv"; operated separately from the Toronto Eruv, whose page does not name its own operator.'),
('wh','lower-washington-heights-eruv-perimeter','Lower Washington Heights Eruv (W 160th - W 178th St)','New York (Washington Heights)','US','NY',None,'Manhattan Eruv Inc. (eruv.nyc)','https://eruv.nyc/','https://eruv.nyc/wh-eruv-map-2026-08-07.png','Official raster map (updated 2025-12-19) georeferenced by hand to OSM street intersections (residual <=10 m) and traced from the shaded area. Connected to the Mount Sinai Eruv (Broadway W178-179 St) and the YU Eruv (Amsterdam Ave W178-180 St), whose maps are not traced. Separate from the Manhattan Eruv polygon (manhattan-eruv).'),
]
feats=[]
for k,i,n,c,co,st,rep,src,su,bu,ex in S:
    p=dict(id=i,name_en=n,city=c,country=co)
    if st: p['state']=st
    p.update(geometry_kind='perimeter',status='unknown',source=src,source_url=su,boundary_map_url=bu,license=LIC,verified_at='2026-10-17',geometry_precision='approximate',note=NOTE+' ('+ex+')')
    if rep: p['replaces_id']=rep
    g=res[k]['geom']; assert g.geom_type=='Polygon' and g.is_valid
    feats.append({'type':'Feature','properties':p,'geometry':mapping(g)})
json.dump({'type':'FeatureCollection','features':feats},open('./batch2-eruvs.geojson','w'),separators=(',',':'))
print(len(feats))
