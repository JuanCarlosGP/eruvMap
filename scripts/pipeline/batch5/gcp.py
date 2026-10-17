import json,subprocess,numpy as np
from ov import overpass
def inter(pairs,bbox,tag):
    """pairs: list of (nameA,nameB). returns dict (A,B)->(lat,lon) or None"""
    names=sorted({n for p in pairs for n in p})
    rx='|'.join(names)
    q=f'[out:json][timeout:90];way["highway"]["name"~"({rx})"]({bbox});out geom;'
    open(f'q_{tag}.q','w').write(q); assert overpass(f'q_{tag}.q',f'gcp_{tag}.json')
    d=json.load(open(f'gcp_{tag}.json'))
    ways={}
    for e in d['elements']:
        
        for n in names:
            if n in e['tags']['name']: ways.setdefault(n,[]).append([(p['lat'],p['lon']) for p in e['geometry']])
    out={}
    for A,B in pairs:
        sa={pt for w in ways.get(A,[]) for pt in w}; sb={pt for w in ways.get(B,[]) for pt in w}
        c=sa&sb
        if not c:
            # nearest vertices
            best=min(((a[0]-b[0])**2+(a[1]-b[1])**2,a,b) for a in sa for b in sb) if sa and sb else None
            out[(A,B)]=(( (best[1][0]+best[2][0])/2,(best[1][1]+best[2][1])/2) if best and best[0]<2e-8 else None)
        else:
            out[(A,B)]=(np.mean([p[0] for p in c]),np.mean([p[1] for p in c]))
    return out
def fit(px,ll,lat0=None):
    """affine px(x,y)->lon,lat (small area) ; returns function and residuals in m"""
    px=np.array(px,float); ll=np.array(ll,float)  # ll as (lat,lon)
    A=np.c_[px,np.ones(len(px))]
    cx,_,_,_=np.linalg.lstsq(A,ll[:,1],rcond=None); cy,_,_,_=np.linalg.lstsq(A,ll[:,0],rcond=None)
    pred=np.c_[A@cy,A@cx]; la=ll[:,0].mean()
    res=np.hypot((pred[:,0]-ll[:,0])*110574,(pred[:,1]-ll[:,1])*111320*np.cos(np.radians(la)))
    f=lambda x,y:(float(np.dot([x,y,1],cx)),float(np.dot([x,y,1],cy)))  # lon,lat
    return f,res
def inter_local(fn,pairs):
    d=json.load(open(fn)); ways={}
    for e in d['elements']:
        nm=e.get('tags',{}).get('name','')
        for A,B in pairs:
            for n in (A,B):
                if n in nm: ways.setdefault(n,[]).append([(p['lat'],p['lon']) for p in e['geometry']])
    out={}
    for A,B in pairs:
        sa={pt for w in ways.get(A,[]) for pt in w}; sb={pt for w in ways.get(B,[]) for pt in w}
        c=sa&sb
        if c: out[(A,B)]=(float(np.mean([p[0] for p in c])),float(np.mean([p[1] for p in c])))
        elif sa and sb:
            d2,a,b=min(((a[0]-b[0])**2+(a[1]-b[1])**2,a,b) for a in sa for b in sb)
            out[(A,B)]=((a[0]+b[0])/2,(a[1]+b[1])/2) if d2<4e-8 else None
        else: out[(A,B)]=None
    return out
