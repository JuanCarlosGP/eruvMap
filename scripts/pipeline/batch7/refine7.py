import numpy as np,cv2,json,math
from scipy.optimize import minimize
from gcp import *
def refine(img,osmf,px,ll,hw=('residential','tertiary','secondary','primary','unclassified','motorway','trunk','service','motorway_link','trunk_link'),white=250,sig=2.0,kind='sim',out=None):
    im=cv2.imread(img); g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    mask=(g>=white).astype(np.uint8)*255
    mb=cv2.GaussianBlur(mask.astype(np.float32),(0,0),sig); mb=(mb-mb.mean())/mb.std()
    f,res=fit(px,ll,kind); print('init resid',np.round(res,1))
    d=json.load(open(osmf))
    ways=[np.array([(q['lon'],q['lat']) for q in e['geometry']]) for e in d['elements'] if e.get('type')=='way' and 'geometry' in e and e['tags'].get('highway') in hw]
    # inverse map by affine fit ll->px
    A=np.c_[np.array(ll),np.ones(len(ll))]; sol=np.linalg.lstsq(A,np.array(px,float),rcond=None)[0]
    H,W=g.shape
    def render(p):
        dx,dy,ds,rot=p; c,s=math.cos(rot),math.sin(rot); R=(1+ds)*np.array([[c,-s],[s,c]])
        canvas=np.zeros((H,W),np.uint8)
        for l in ways:
            q=np.c_[l,np.ones(len(l))]@sol; q=(q-[W/2,H/2])@R.T+[W/2,H/2]+[dx,dy]
            if q[:,0].max()<0 or q[:,1].max()<0 or q[:,0].min()>W or q[:,1].min()>H: continue
            cv2.polylines(canvas,[np.round(q).astype(np.int32).reshape(-1,1,2)],False,255,1)
        return canvas,R
    def score(p):
        r=cv2.GaussianBlur(render(p)[0].astype(np.float32),(0,0),sig); r=(r-r.mean())/r.std(); return -float((r*mb).mean())
    best=np.zeros(4); bs=score(best)
    for dx in range(-14,15,2):
        for dy in range(-14,15,2):
            s=score(np.array([dx,dy,0,0.])); 
            if s<bs: bs,best=s,np.array([dx,dy,0,0.])
    print('grid',bs,best)
    r=minimize(score,best,method='Powell',options=dict(xtol=1e-3,ftol=1e-6,maxfev=500)); print(r.x,r.fun)
    p=r.x; canvas,R=render(p)
    ov=im.copy(); ov[canvas>0]=(0,0,255)
    if out: cv2.imwrite(out,ov)
    # final px->ll: px' = R(px-c)+c+d  is image px of osm; so osm px = ... invert: osm_px = R^-1 (px - d - c)+c
    Ri=np.linalg.inv(R); dx,dy=p[0],p[1]
    def px2ll(P):
        P=np.asarray(P,float); q=(P-[dx,dy]-[W/2,H/2])@Ri.T+[W/2,H/2]   # osm-affine px
        Ainv=np.linalg.inv(sol[:2].T)
        return (q-sol[2])@Ainv.T
    return px2ll,r.fun
