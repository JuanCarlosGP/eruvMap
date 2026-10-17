import numpy as np,cv2,json,math
from PIL import Image
from reg import *
a=np.array(Image.open('w3/tlv_kav.jpg').convert('RGB')).astype(int)
sea=(np.abs(a-np.array((190,232,255))).sum(2)<25).astype(np.uint8)
n,lab,st,_=cv2.connectedComponentsWithStats(sea)
l=lab[700,150]; sea=(lab==l).astype(np.uint8)
print(sea.sum())
sea=cv2.morphologyEx(sea,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
edge=cv2.morphologyEx(sea,cv2.MORPH_GRADIENT,np.ones((3,3),np.uint8))
H,W=edge.shape
edge[:8]=0; edge[:,:8]=0; edge[-8:]=0
e=(edge*255).astype(np.uint8)
hz=cv2.morphologyEx(e,cv2.MORPH_OPEN,np.ones((1,60),np.uint8)); vt=cv2.morphologyEx(e,cv2.MORPH_OPEN,np.ones((150,1),np.uint8))
e=e&~cv2.dilate(hz,np.ones((3,3),np.uint8))&~cv2.dilate(vt,np.ones((3,3),np.uint8))
edge=(e>0).astype(np.uint8)
n2,lab2,st2,_=cv2.connectedComponentsWithStats(edge.astype(np.uint8),connectivity=8)
k=1+np.argmax(st2[1:,4]); edge=(lab2==k).astype(np.uint8)
cv2.imwrite('tlv_edge.png',edge*255)
ys,xs=np.where(edge>0); x0,y0=xs.min(),ys.min(); mm=(edge[y0:ys.max()+1,x0:xs.max()+1]*255).astype(np.uint8)
print(mm.shape)
lat0,lon0=32.08,34.78
L,kx,ky=load_osm('tlv-osm.json',lat0,lon0)
L=[l for l in L if len(l)>1]
best=search(mm,L,[x/20 for x in range(110,140,2)],[0],extent_m=40000); print(best)
nccs,sc,rot,loc,Wc=best
json.dump(dict(sc=sc,rot=rot,loc=list(map(int,loc)),W=Wc,x0=int(x0),y0=int(y0),lat0=lat0,lon0=lon0),open('tlv-reg.json','w'))
