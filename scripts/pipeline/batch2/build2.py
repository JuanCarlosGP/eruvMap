import json,pickle,sys
sys.path.insert(0,'.')
exec(open('helpers2.py').read())
from shapely.validation import make_valid
from shapely.geometry import Polygon,mapping
import numpy as np
# Detroit
d=json.load(open('detroit.geojson'))
c=d['features'][0]['geometry']['coordinates']
det=Polygon(c); assert det.is_valid
add('det',det,[det])
# Toronto
a=json.load(open('toronto-arrays.json'))
for k,key in [('z','tn'),('C','ts'),('S','trh')]:
    p=Polygon([(x[1],x[0]) for x in a[k]])
    q=p
    if not p.is_valid:
        v=make_valid(p); parts=[g for g in (v.geoms if hasattr(v,'geoms') else [v]) if g.geom_type=='Polygon']
        q=max(parts,key=lambda g:g.area); print(key,'invalid -> made valid; area ratio',q.area/p.area,'parts',len(parts))
    add(key,q,[p])
# Washington Heights
wh=pickle.load(open('wh-poly.pkl','rb'))
whs=wh.buffer(0)
add('wh',whs,[whs])
pickle.dump(res,open('res2.pkl','wb'))
for k,v in res.items(): print(k,v['nv'],round(v['iou'],4),v['geom'].geom_type,v['geom'].is_valid, round(v['geom'].area*1e4,3))
