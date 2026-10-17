import pickle,numpy as np,math,cv2,json
from shapely.geometry import Polygon,mapping
from montf import *
mpp,lx,ly,rot=pickle.load(open('mon-par.pkl','rb'))
main,pr=pickle.load(open('mon-poly-pdf.pkl','rb'))
S=0.25; H,W=864,648; cx,cy=W/2,H/2
c,s=math.cos(rot),math.sin(rot)
def tf(coords):
    xy=np.array(coords)*S
    xy=(xy-[cx,cy])@np.array([[c,s],[-s,c]])+[cx,cy]   # same as render's inv path (rotation applied in raster px of inv output)
    return xy
# render: q=inv(l)*S ; q'=(q-c)@R+c  => forward: q=(q'-c)@R^-1+c
Rinv=np.linalg.inv(np.array([[c,s],[-s,c]]))
def to_ll(coords):
    q2=np.array(coords)  # raster px after rotation
    q=(q2-[cx,cy])@Rinv+[cx,cy]
    pdf=q/S
    return fwd(pdf,mpp,(lx,ly))
def conv(g,tol):
    g=g.simplify(tol)
    polys=[g] if g.geom_type=='Polygon' else list(g.geoms)
    out=[]
    for p in polys:
        ext=to_ll(np.array(p.exterior.coords)*S)
        holes=[to_ll(np.array(i.coords)*S) for i in p.interiors if Polygon(i).area>5000]
        out.append(Polygon(ext,holes))
    return out
res={}
res['mon']=conv(main,2.5); res['pearl']=conv(pr,2.5)
for k,v in res.items(): print(k,[(len(p.exterior.coords),p.is_valid,round(p.area*1e6/ (1.0),1)) for p in v])
pickle.dump(res,open('mon-res.pkl','wb'))
