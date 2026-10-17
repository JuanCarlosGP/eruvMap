import numpy as np,cv2,json,math,pickle
from scipy.optimize import minimize
from montf import *
S=0.25
m=cv2.imread('mon_roads.png',0); H,W=m.shape
mb=cv2.GaussianBlur(m.astype(np.float32),(0,0),1.5); mb=(mb-mb.mean())/mb.std()
d=json.load(open('mon-tert.json'))
ways=[np.array([(q['lon'],q['lat']) for q in e['geometry']]) for e in d['elements'] if e['type']=='way' and 'geometry' in e]
print(len(ways))
def render(p):
    mpp,lx,ly,rot=p
    img=np.zeros((H,W),np.uint8)
    c,s=math.cos(rot),math.sin(rot)
    for l in ways:
        q=inv(l,mpp,(lx,ly))*S   # raster px
        cx,cy=W/2,H/2
        q=(q-[cx,cy])@np.array([[c,s],[-s,c]])+[cx,cy]
        if q[:,0].max()<0 or q[:,1].max()<0 or q[:,0].min()>W or q[:,1].min()>H: continue
        cv2.polylines(img,[np.round(q).astype(np.int32).reshape(-1,1,2)],False,255,1)
    return img
def score(p):
    r=cv2.GaussianBlur(render(p).astype(np.float32),(0,0),1.5); r=(r-r.mean())/r.std()
    return -float((r*mb).mean())
p0=np.array([5.84,293,319,0.0])
print(score(p0))
best=p0;bs=score(p0)
for dx in range(-8,9,2):
    for dy in range(-8,9,2):
        p=p0+[0,dx,dy,0]; s=score(p)
        if s<bs: bs,best=s,p
print('grid',bs,best)
res=minimize(score,best,method='Powell',options=dict(xtol=1e-3,ftol=1e-5,maxfev=400),bounds=None)
print(res.x,res.fun)
pickle.dump(res.x,open('mon-par.pkl','wb'))
cv2.imwrite('mon_render.png',np.dstack([render(res.x),m,np.zeros_like(m)]))
