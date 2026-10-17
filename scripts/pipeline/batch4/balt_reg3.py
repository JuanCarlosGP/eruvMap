import numpy as np,cv2,json
from PIL import Image
import reg
from reg import *
a=np.array(Image.open('balt.jpg').convert('RGB')).astype(int)
near=lambda c,t:(np.abs(a-np.array(c)).sum(2)<t)
db=near((40,50,150),110)&(a[:,:,2]>a[:,:,0]+30)&(a[:,:,2]<200)
db[:, 1255:]=0; db[:58]=0; db[1015:]=0; db[:, :100]=0
m=cv2.dilate((db*255).astype(np.uint8),np.ones((5,5),np.uint8))
n,lab,st,_=cv2.connectedComponentsWithStats(m)
for i in range(1,n):
    if st[i,4]<1500: m[lab==i]=0
cv2.imwrite('balt_mask3.png',m); print(m.mean()/255)
d=json.load(open('balt-osm.json'))
d['elements']=[e for e in d['elements'] if e.get('tags',{}).get('highway') in('motorway','motorway_link','trunk')]
json.dump(d,open('balt-osm-mw.json','w'))
lat0,lon0=39.35,-76.68
L,kx,ky=load_osm('balt-osm-mw.json',lat0,lon0); print(len(L))
ys,xs=np.where(m>0); x,y,w,h=xs.min(),ys.min(),xs.max()-xs.min(),ys.max()-ys.min(); print(x,y,w,h)
mm=m[y:y+h+1,x:x+w+1]
best=search(mm,L,[x/20 for x in range(110,150,2)],[0],extent_m=20000)
print(best)
json.dump([best[0],best[1],best[2],list(best[3]),best[4],[int(x),int(y)]],open('balt-reg3.json','w'))
