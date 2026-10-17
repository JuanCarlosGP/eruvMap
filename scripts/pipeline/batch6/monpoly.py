import pickle,numpy as np
from shapely.geometry import Polygon
from shapely.ops import unary_union
out=pickle.load(open('mon-fills.pkl','rb'))
ids=[3,4,5,6,8,11,12,13,15,16,20,21,22,24,27,29]; pearl=[17]
def U(ids):
    ps=[]
    for i in ids:
        for r in out[i][3]:
            p=Polygon(r).buffer(0); ps.append(p)
    return unary_union([p.buffer(1.5) for p in ps]).buffer(-1.5)
main=U(ids); pr=U(pearl)
print(main.geom_type, main.area, [len(g.exterior.coords) for g in (main.geoms if main.geom_type=='MultiPolygon' else [main])], len(main.interiors) if main.geom_type=='Polygon' else '')
pickle.dump((main,pr),open('mon-poly-pdf.pkl','wb'))
