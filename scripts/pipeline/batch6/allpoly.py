import numpy as np,cv2,pickle
from shapely.geometry import Polygon
from alltf import *
im=cv2.imread('al_live.jpg')
b,g,r=[im[...,i].astype(int) for i in range(3)]
m=((r>150)&(g<115)&(b<115)&(r-g>80)).astype(np.uint8)*255
m[:250]=0; m[980:]=0
print(m.sum()/255)
m2=cv2.dilate(m,np.ones((13,13),np.uint8))
ff=m2.copy(); h,w=ff.shape; mask=np.zeros((h+2,w+2),np.uint8)
cv2.floodFill(ff,mask,(5,300),128)
inside=((ff!=128)).astype(np.uint8)*255
reg=inside
reg=cv2.erode(reg,np.ones((9,9),np.uint8))  # restore to line centre
cv2.imwrite('al_reg.png',reg)
cs,_=cv2.findContours(reg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
c=max(cs,key=cv2.contourArea)[:,0,:].astype(float)
P=Polygon(c).buffer(0).simplify(2.0)
print(P.geom_type,len(P.exterior.coords),P.area)
ll=fwd(np.array(P.exterior.coords))
G=Polygon(ll); print(G.is_valid,G.bounds)
pickle.dump(G,open('al-poly.pkl','wb'))
ov=im.copy(); cv2.polylines(ov,[np.round(np.array(P.exterior.coords)).astype(np.int32).reshape(-1,1,2)],True,(255,0,0),2); cv2.imwrite('al_trace.png',ov[250:980,60:1650])
