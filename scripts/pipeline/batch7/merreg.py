import json,numpy as np,cv2,math,pickle
from scipy.optimize import minimize
isl=cv2.imread('mer_land.png',0)
cs,_=cv2.findContours(isl,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE); c=max(cs,key=cv2.contourArea)
fill=np.zeros_like(isl); cv2.drawContours(fill,[c],-1,255,-1); H,W=fill.shape
d=json.load(open('mer-island.json'))
g=d['elements'][0]['geometry']; lat0=47.57
KX=111320*math.cos(math.radians(lat0)); KY=110574
O=np.array([(q['lon']*KX,-q['lat']*KY) for q in g]); cO=O.mean(axis=0)
M=cv2.moments(fill,True); cF=np.array([M['m10']/M['m00'],M['m01']/M['m00']])
def render(p):
    mpp,dx,dy,rot=p; c_,s_=math.cos(rot),math.sin(rot)
    q=((O-cO)/mpp)@np.array([[c_,s_],[-s_,c_]])+cF+[dx,dy]
    img=np.zeros((H,W),np.uint8); cv2.fillPoly(img,[np.round(q).astype(np.int32)],255); return img
def score(p):
    a=render(p)>0; b=fill>0; return -(a&b).sum()/((a|b).sum())
best=None
for mpp in np.arange(6,10,0.5):
    s=score([mpp,0,0,0]); 
    if best is None or s<best[0]: best=(s,mpp)
print(best)
r=minimize(score,[best[1],0,0,0],method='Powell',options=dict(xtol=1e-4,ftol=1e-7)); print(r.x,r.fun)
r2=minimize(score,r.x,method='Nelder-Mead',options=dict(xatol=1e-4,fatol=1e-8,maxiter=2000)); print(r2.x,r2.fun, math.degrees(r2.x[3]))
pickle.dump((r2.x,cO,cF,lat0),open('mer-par.pkl','wb'))
ov=cv2.imread('mer.jpeg'); cs2,_=cv2.findContours(render(r2.x),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE); cv2.drawContours(ov,cs2,-1,(0,0,255),2); cv2.imwrite('mer_reg.png',ov)
