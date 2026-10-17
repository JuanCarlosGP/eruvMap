import sys
sys.path.insert(0,'.')
exec(open('helpers2.py').read())
from load2 import load2
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import unary_union
def L(k,folder=None,excl=None,names=None):
    out=[]
    for t,p,n,g in load2(f'kml/{k}.kml'):
        if t!='line': continue
        if folder and (len(p)<2 or p[1] not in folder): continue
        if excl and any(e in ' '.join(p)+' '+n for e in excl): continue
        if names and not any(x in n for x in names): continue
        out.append(g)
    return out
def P(k,pred=lambda n,p:True):
    return [g for t,p,n,g in load2(f'kml/{k}.kml') if t=='poly' and pred(n,p)]
def comps(g,minarea=1e-7):
    ps=list(g.geoms) if hasattr(g,'geoms') else [g]
    return sorted([p for p in ps if p.area>minarea],key=lambda p:-p.area)
