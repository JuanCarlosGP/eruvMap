import numpy as np,cv2,json,math
from PIL import Image
from reg import *
m=cv2.imread('balt_mask3.png',0)
ys,xs=np.where(m>0); x0,y0=xs.min(),ys.min(); mm=m[y0:ys.max()+1,x0:xs.max()+1]
lat0,lon0=39.35,-76.68
L,kx,ky=load_osm('balt-osm-mw.json',lat0,lon0)
best=search(mm,L,[x/100 for x in range(618,646,2)],[-1,-.5,0,.5,1],extent_m=20000); print(best)
nccs,sc,rot,loc,W=best
json.dump(dict(sc=sc,rot=rot,loc=list(map(int,loc)),W=W,x0=int(x0),y0=int(y0),lat0=lat0,lon0=lon0),open('balt-reg.json','w'))
# overlay all OSM roads
La,_,_=load_osm('balt-osm.json',lat0,lon0)
can=render(La,sc,math.radians(rot),W,W,W//2,W//2)
img=np.array(Image.open('balt.jpg').convert('RGB'))
H,Wi=img.shape[:2]
cx=loc[0]-x0; cy=loc[1]-y0   # canvas coords of image (0,0)
crop=can[cy:cy+H,cx:cx+Wi]
ov=img.copy(); ov[crop>0]=(255,0,0)
Image.fromarray(ov).save('balt_ov.png')
Image.fromarray(ov[40:600,60:860]).save('balt_ov1.png')
