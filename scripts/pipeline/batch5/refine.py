import json,math,numpy as np,cv2
from scipy.optimize import minimize
def osm_lines(fn,tags=None):
    d=json.load(open(fn)); L=[]
    for e in d['elements']:
        if e['type']=='way' and 'geometry' in e:
            if tags and e.get('tags',{}).get('highway') not in tags: continue
            L.append(np.array([(p['lon'],p['lat']) for p in e['geometry']]))
    return L
def affine_from(f,pts):
    pass
class Aff:
    # lon,lat <- x,y : [lon,lat]=M@[x,y]+t
    def __init__(s,M,t): s.M=np.array(M,float); s.t=np.array(t,float)
    def fwd(s,xy): return xy@s.M.T+s.t
    def inv(s,ll): return (ll-s.t)@np.linalg.inv(s.M).T
def from_gcp(px,ll):
    px=np.array(px,float); ll=np.array(ll,float)[:,::-1]  # lon,lat
    A=np.c_[px,np.ones(len(px))]; sol,_,_,_=np.linalg.lstsq(A,ll,rcond=None)
    return Aff(sol[:2].T,sol[2])
def render(aff,L,shape,thick=1):
    img=np.zeros(shape,np.uint8)
    for l in L:
        p=aff.inv(l); 
        if p[:,0].max()<-50 or p[:,0].min()>shape[1]+50 or p[:,1].max()<-50 or p[:,1].min()>shape[0]+50: continue
        cv2.polylines(img,[np.round(p).astype(np.int32).reshape(-1,1,2)],False,255,thick)
    return img
def refine(aff,L,mask,sig=3,iters=3):
    H,W=mask.shape; mb=cv2.GaussianBlur(mask.astype(np.float32),(0,0),sig); mb=(mb-mb.mean())/ (mb.std()+1e-9)
    cx,cy=W/2,H/2
    def mk(p):
        dx,dy,ds,rot=p
        # adjust affine: pixel transform x' = x applied before: compose similarity about centre in pixel space
        c,s=math.cos(rot),math.sin(rot); S=(1+ds)
        R=np.array([[c,-s],[s,c]])*S
        # new pixel->ll: ll = aff.fwd( R(x-c)+c+d )
        M=aff.M@R; t=aff.t+aff.M@(np.array([cx,cy])-R@np.array([cx,cy])+np.array([dx,dy]))
        return Aff(M,t)
    def obj(p):
        r=render(mk(p),L,mask.shape); rb=cv2.GaussianBlur(r.astype(np.float32),(0,0),sig); rb=(rb-rb.mean())/(rb.std()+1e-9)
        return -float((rb*mb).mean())
    p=np.zeros(4); best=None
    for sg in [sig*3,sig*2,sig]:
        mb=cv2.GaussianBlur(mask.astype(np.float32),(0,0),sg); mb=(mb-mb.mean())/(mb.std()+1e-9)
        def obj(p,sg=sg):
            r=render(mk(p),L,mask.shape); rb=cv2.GaussianBlur(r.astype(np.float32),(0,0),sg); rb=(rb-rb.mean())/(rb.std()+1e-9)
            return -float((rb*mb).mean())
        o=minimize(obj,p,method='Powell',options={'xtol':1e-3,'ftol':1e-5,'maxiter':3000},bounds=None)
        p=o.x; print('sigma',sg,'score',-o.fun,p.round(4),flush=True)
    return mk(p),-o.fun
def pix2lonlat(aff,pts): return aff.fwd(np.array(pts,float))
