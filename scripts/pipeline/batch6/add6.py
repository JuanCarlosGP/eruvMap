import json,sys
from shapely.geometry import Polygon,mapping
REPO='../eruvmap-repo/data/eruvs.geojson'
LIC='All rights reserved by source; approximate traced derivative, shown with attribution pending community permission'
NOTE="Traced approximately from the official map; always check the community's official map and status before relying on it"
def clean(p,minhole=0.03):
    holes=[i for i in p.interiors if Polygon(i).area>0 and Polygon(i).area*4*3.14159/(i.length**2)>minhole]
    return Polygon(p.exterior,holes)
def add(id,name,city,country,state,source,source_url,map_url,extra,geoms,replaces=None):
    d=json.load(open(REPO))
    fs=d['features']
    if replaces: fs[:]=[f for f in fs if f['properties']['id']!=replaces]
    assert id not in [f['properties']['id'] for f in fs]
    for n,g in enumerate(geoms):
        g=clean(g); assert g.is_valid and g.geom_type=='Polygon'
        p=dict(id=id if n==0 else f'{id}-{n+1}',name_en=name if n==0 else f'{name} (part {n+1})',city=city,country=country,state=state,geometry_kind='perimeter',status='unknown',source=source,source_url=source_url,boundary_map_url=map_url,license=LIC,verified_at='2026-10-17',geometry_precision='approximate',note=NOTE+' ('+extra+')')
        fs.append({'type':'Feature','properties':p,'geometry':mapping(g)})
    json.dump(d,open(REPO,'w'),ensure_ascii=False,indent=4)
    print(len(fs))
