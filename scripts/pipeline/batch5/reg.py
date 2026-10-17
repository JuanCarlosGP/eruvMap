import json,math,numpy as np,cv2
from PIL import Image
def load_osm(fn,lat0,lon0):
    d=json.load(open(fn)); kx=111320*math.cos(math.radians(lat0)); ky=110574
    L=[]
    for e in d['elements']:
        if e['type']=='way' and 'geometry' in e:
            L.append(np.array([((p['lon']-lon0)*kx,(p['lat']-lat0)*ky) for p in e['geometry']]))
    return L,kx,ky
def render(L,scale,rot,W,H,cx,cy):
    # metres -> px: rotate by rot, scale 1/scale; y flip; origin at canvas centre
    c,s=math.cos(rot),math.sin(rot)
    img=np.zeros((H,W),np.uint8)
    for a in L:
        x=(a[:,0]*c-a[:,1]*s)/scale; y=(a[:,0]*s+a[:,1]*c)/scale
        pts=np.c_[x+cx,cy-y].astype(np.int32)
        cv2.polylines(img,[pts.reshape(-1,1,2)],False,255,1)
    return img
def search(mask,L,scales,rots,extent_m=7000):
    best=None
    for sc in scales:
        n=int(extent_m/sc); W=H=n
        for r in rots:
            can=render(L,sc,math.radians(r),W,H,W//2,H//2)
            can=cv2.GaussianBlur(can,(0,0),2); m=cv2.GaussianBlur(mask,(0,0),2)
            if m.shape[0]>=can.shape[0] or m.shape[1]>=can.shape[1]: continue
            res=cv2.matchTemplate(can.astype(np.float32),m.astype(np.float32),cv2.TM_CCOEFF_NORMED)
            _,mx,_,loc=cv2.minMaxLoc(res)
            if best is None or mx>best[0]: best=(mx,sc,r,loc,W)
    return best
