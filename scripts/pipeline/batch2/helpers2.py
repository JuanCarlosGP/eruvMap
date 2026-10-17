import math, os, json, io, requests, time
from load import *
from shapely.geometry import Polygon, MultiPolygon, mapping, shape
from shapely.ops import unary_union
from PIL import Image
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
OUT='./'
M=lambda m: load(m)
def close(lines,r):
    u=unary_union(lines).buffer(r)
    polys=[Polygon(p.exterior) for p in (u.geoms if hasattr(u,'geoms') else [u])]
    return unary_union(polys).buffer(-r)
def simp(g,maxv=150):
    tol=0.00005
    while True:
        s=g.simplify(tol,preserve_topology=True)
        if not s.is_valid: s=s.buffer(0)
        ps=list(s.geoms) if hasattr(s,'geoms') else [s]
        ps=[Polygon(p.exterior) for p in ps if p.area>g.area*0.002]  # drop holes & slivers
        if all(len(p.exterior.coords)-1<=maxv for p in ps): break
        tol*=1.25
    s=unary_union(ps)
    return s,tol
def rnd(g):
    def r(c): return [round(x,5) for x in c]
    ps=list(g.geoms) if hasattr(g,'geoms') else [g]
    out=[Polygon([tuple(r(c)) for c in p.exterior.coords]) for p in ps]
    return out[0] if len(out)==1 else MultiPolygon(out)
def tile(z,lon,lat):
    n=2**z; return (lon+180)/360*n,(1-math.log(math.tan(math.radians(lat))+1/math.cos(math.radians(lat)))/math.pi)/2*n
def untile(z,x,y):
    n=2**z; return x/n*360-180, math.degrees(math.atan(math.sinh(math.pi*(1-2*y/n))))
def preview(slug,title,final,orig,fn):
    minx,miny,maxx,maxy=unary_union([final]+orig).bounds
    padx,pady=(maxx-minx)*.08,(maxy-miny)*.08
    minx-=padx;maxx+=padx;miny-=pady;maxy+=pady
    z=17
    while z>8:
        x0,y1=tile(z,minx,miny);x1,y0=tile(z,maxx,maxy)
        if (int(x1)-int(x0)+1)*(int(y1)-int(y0)+1)<=30: break
        z-=1
    X0,X1,Y0,Y1=int(x0),int(x1),int(y0),int(y1)
    img=Image.new('RGB',((X1-X0+1)*256,(Y1-Y0+1)*256))
    os.makedirs('tiles',exist_ok=True)
    for x in range(X0,X1+1):
        for y in range(Y0,Y1+1):
            p=f'tiles/{z}_{x}_{y}.png'
            if not os.path.exists(p):
                r=requests.get(f'https://tile.openstreetmap.org/{z}/{x}/{y}.png',headers={'User-Agent':'eruvmap-preview/1.0 (derived-data QA)'},timeout=20)
                open(p,'wb').write(r.content); time.sleep(.2)
            img.paste(Image.open(p).convert('RGB'),((x-X0)*256,(y-Y0)*256))
    W,H=img.size
    ext=(*untile(z,X0,Y1+1),*untile(z,X1+1,Y0))  # lon0,lat_bottom,lon1,lat_top
    fig,ax=plt.subplots(figsize=(10,10*H/W))
    ax.imshow(img,extent=(ext[0],ext[2],ext[1],ext[3]))
    # mercator tiles vs lon/lat axes: fix aspect
    ax.set_aspect(1/math.cos(math.radians((miny+maxy)/2)))
    for g in orig:
        gs=g.geoms if hasattr(g,'geoms') else [g]
        for h in gs:
            x,y=(h.exterior.xy if h.geom_type=='Polygon' else h.xy); ax.plot(x,y,color='#1565c0',lw=.8,alpha=.8)
    for p in (final.geoms if hasattr(final,'geoms') else [final]):
        x,y=p.exterior.xy; ax.plot(x,y,'r-',lw=2); ax.fill(x,y,color='red',alpha=.12)
    ax.set_xlim(minx,maxx);ax.set_ylim(miny,maxy)
    ax.set_title(title+'\nred = simplified traced shape; blue = source linework (georeferencing only)\n© OpenStreetMap contributors',fontsize=9)
    fig.savefig(OUT+fn,dpi=90,bbox_inches='tight'); plt.close(fig)
def iou(a,b): return a.intersection(b).area/a.union(b).area
res={}
def add(key,final_raw,orig_lines,origpoly=None):
    s,tol=simp(final_raw); s=rnd(s)
    ref=origpoly if origpoly is not None else final_raw
    res[key]=dict(geom=s,orig=orig_lines,iou=iou(s,ref),nv=[len(p.exterior.coords)-1 for p in (s.geoms if hasattr(s,'geoms') else [s])],tol=tol)
