import json,numpy as np
from shapely.geometry import LineString,Point
from shapely.ops import unary_union
d=json.load(open('wh-osm.json'))
W={}
for e in d['elements']:
    W.setdefault(e['tags']['name'],[]).append(LineString([(p['lon'],p['lat']) for p in e['geometry']]))
W={k:unary_union(v) for k,v in W.items()}
def X(a,b,near):
    i=W[a].intersection(W[b]); ps=[]
    for g in (i.geoms if hasattr(i,'geoms') else [i]):
        if g.geom_type=='Point': ps.append(g)
        elif g.geom_type=='LineString' and not g.is_empty: ps.append(g.centroid)
    ps.sort(key=lambda p:p.distance(Point(near))); return (ps[0].x,ps[0].y)
A='Amsterdam Avenue';S='Saint Nicholas Avenue'
CP=[((870,380),X('West 175th Street',A,(-73.934,40.845))),
((868,718),X('West 170th Street',A,(-73.936,40.841))),
((860,1080),X('West 165th Street',A,(-73.938,40.838))),
((857,1217),X('West 163rd Street',A,(-73.939,40.8366))),
((853,1425),X('West 160th Street',A,(-73.9406,40.8347))),
((640,380),X('West 175th Street',S,(-73.9365,40.8454))),
((638,718),X('West 170th Street',S,(-73.939,40.842)))]
px=np.array([c[0] for c in CP],float); ll=np.array([c[1] for c in CP])
M=np.c_[px,np.ones(len(px))]
cx,_,_,_=np.linalg.lstsq(M,ll[:,0],rcond=None); cy,_,_,_=np.linalg.lstsq(M,ll[:,1],rcond=None)
def tr(x,y): return (cx[0]*x+cx[1]*y+cx[2], cy[0]*x+cy[1]*y+cy[2])
if __name__=='__main__':
    for (p,l) in CP:
        q=tr(*p); print(p,l,'res m',round(((q[0]-l[0])*84300)**2+((q[1]-l[1])*111200)**2,0)**.5)
