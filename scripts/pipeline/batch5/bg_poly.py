import numpy as np,cv2,pickle
from PIL import Image
from shapely.geometry import Polygon
from refine import *
px=[(301,164),(342,436),(363,576),(423,436)]
ll=[(42.17015866,-87.96322004),(42.15329875,-87.961794),(42.138913125,-87.95919295),(42.154206075,-87.955043825)]
aff=from_gcp(px,ll)
img0=np.array(Image.open('img/bg.png').convert('RGB')); a=img0.astype(int); R,G,B=a[:,:,0],a[:,:,1],a[:,:,2]
blue=((B>200)&(R<150)&(G<120)).astype(np.uint8); print(blue.sum())
# road mask: bright/white thin lines and orange: pixels differing from bg: use light (min>=252) or yellow/orange main roads
road=(((R>=252)&(G>=252)&(B>=250))|((R>230)&(G>200)&(B<150)&(R-B>90))).astype(np.uint8)*255
road[blue>0]=0; road[760:]=0
L=osm_lines('bg-osm.json')
aff2,sc=refine(aff,L,road,sig=2)
r=render(aff2,L,road.shape); ov=img0.copy(); ov[r>0]=(0,160,0); Image.fromarray(ov).resize((1000,1295)).save('img/bg_ov.png')
m=cv2.dilate(blue,np.ones((5,5),np.uint8)); m[775:]=0; m[:3]=m[:3]
inv=(1-m).astype(np.uint8); n,lab,st,_=cv2.connectedComponentsWithStats(inv,connectivity=4)
out=lab==lab[10,10]; filled=cv2.erode((~out).astype(np.uint8),np.ones((5,5),np.uint8))
cs,_=cv2.findContours(filled,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE); c=max(cs,key=cv2.contourArea); print(cv2.contourArea(c))
cv2.drawContours(ov,[c],-1,(255,0,0),2); Image.fromarray(ov).resize((1000,1295)).save('img/bg_ov.png')
p=Polygon([tuple(v) for v in pix2lonlat(aff2,c[:,0,:])]).buffer(0); print(p.area*1e4,p.bounds)
pickle.dump(p,open('bg-poly.pkl','wb'))
