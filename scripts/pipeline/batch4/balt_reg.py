import numpy as np,cv2,json
from PIL import Image
from reg import *
a=np.array(Image.open('balt.jpg').convert('RGB')).astype(int)
def near(c,t): return (np.abs(a-np.array(c)).sum(2)<t)
lil=near((185,182,196),45)|near((51,62,98),60)
# restrict to map area
lil[:30,:]=0; lil[:, :55]=0; lil[:, 680*2:]=0
m=(lil*255).astype(np.uint8); m=cv2.dilate(m,np.ones((3,3),np.uint8))
print(m.mean()/255)
cv2.imwrite('balt_mask.png',m)
lat0,lon0=39.35,-76.68
L,kx,ky=load_osm('balt-osm.json',lat0,lon0)
print(len(L))
# map x extent ~ 1330px of 1562 (excl legend). crop to map area
mm=m[30:1060,55:1300]
mm_small=mm
best=search(mm,L,[3.6,3.9,4.2,4.5,4.8,5.1,5.4],[0],extent_m=14000)
print(best)
