import numpy as np,cv2,json,pickle
from PIL import Image
from shapely.geometry import Polygon
from tilereg import *
r=json.load(open('cin-reg.json')); mx,s,loc=r['best']; X0,Y0=r['X0'],r['Y0']
a=np.array(Image.open('img/cin200-1.png').convert('RGB')).astype(int)
R,G,B=a[:,:,0],a[:,:,1],a[:,:,2]
blue=((B>200)&(R<80)&(G<80)).astype(np.uint8)
blue[:200,:760]=0; blue[1180:1420,80:540]=0  # legends
m=cv2.dilate(blue,np.ones((7,7),np.uint8))
H,W=m.shape; inv=(1-m).astype(np.uint8); n,lab,st,_=cv2.connectedComponentsWithStats(inv,connectivity=4)
out=lab==lab[3,3]; filled=(~out).astype(np.uint8)
filled=cv2.erode(filled,np.ones((7,7),np.uint8))
cs,_=cv2.findContours(filled,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE); c=max(cs,key=cv2.contourArea)
print(cv2.contourArea(c))
pts=[px2ll((x,y),s,loc,16,X0,Y0) for x,y in c[:,0,:]]
p=Polygon(pts).buffer(0); print(p.area*1e4,p.bounds)
pickle.dump(p,open('cin-poly.pkl','wb'))
# subtract pink construction exclusion
pink=((R>235)&(G>120)&(G<175)&(B>140)&(B<190)).astype(np.uint8)
pink[:, 1300:]=0; pink[:150]=0; pink[1180:]=0
pink=cv2.morphologyEx(pink,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
n,lab,st,_=cv2.connectedComponentsWithStats(pink)
k=1+np.argmax(st[1:,4]); print('pink px',st[k]); pk=(lab==k).astype(np.uint8)
pk=cv2.morphologyEx(pk,cv2.MORPH_CLOSE,np.ones((25,25),np.uint8))
cs,_=cv2.findContours(pk,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE); c2=max(cs,key=cv2.contourArea)
pp=Polygon([px2ll((x,y),s,loc,16,X0,Y0) for x,y in c2[:,0,:]]).buffer(0)
q=p.difference(pp); 
if q.geom_type!='Polygon': q=max(q.geoms,key=lambda g:g.area)
q=Polygon(q.exterior); print(p.area*1e4,pp.area*1e4,q.area*1e4)
pickle.dump(q,open('cin-poly.pkl','wb'))
