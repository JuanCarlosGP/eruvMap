import numpy as np,cv2
from PIL import Image
from reg import *
a=np.array(Image.open('balt.jpg').convert('RGB')).astype(int)
near=lambda c,t:(np.abs(a-np.array(c)).sum(2)<t)
yel=((a[:,:,0]>225)&(a[:,:,1]>225)&(a[:,:,2]<200)&(a[:,:,2]>150)).astype(np.uint8)
yel[:, 1290:]=0; yel[:30]=0
k=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(15,15))
reg=cv2.morphologyEx(yel,cv2.MORPH_CLOSE,np.ones((41,41),np.uint8))
cnts,_=cv2.findContours(reg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE); c=max(cnts,key=cv2.contourArea)
hull=np.zeros_like(yel); cv2.drawContours(hull,[c],-1,1,-1)
lil=near((185,182,196),30)&(hull>0)
hull_er=cv2.erode(hull,np.ones((9,9),np.uint8))
lil&=hull_er>0
m=cv2.dilate((lil*255).astype(np.uint8),np.ones((3,3),np.uint8))
cv2.imwrite('balt_mask2.png',m); np.save('balt_hull.npy',hull)
x,y,w,h=cv2.boundingRect(c); print(x,y,w,h,m.mean()/255)
mm=m[y:y+h,x:x+w]
lat0,lon0=39.35,-76.68
L,kx,ky=load_osm('balt-osm.json',lat0,lon0)
best=search(mm,L,[x/10 for x in range(38,56,2)],[0],extent_m=16000)
print(best,(x,y,w,h))
import json; json.dump([best[0],best[1],best[2],list(best[3]),best[4],[x,y,w,h]],open('balt-reg.json','w'))
