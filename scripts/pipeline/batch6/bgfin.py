import json,numpy as np,cv2,math,pickle
from shapely.geometry import Polygon
im=cv2.imread('../raw5/img/bg_big.png'); h,w=im.shape[:2]
lat0=42.16; KX=111320*math.cos(math.radians(lat0)); KY=110574
OX=-88.02*KX; OY=-42.23*KY; mpp=7.25; loc=(134,456)
def fwd(xy): xy=np.asarray(xy,float); return np.c_[((xy[:,0]+loc[0])*mpp+OX)/KX,-((xy[:,1]+loc[1])*mpp+OY)/KY]
def inv(ll): ll=np.asarray(ll); return np.c_[(ll[:,0]*KX-OX)/mpp-loc[0],(-ll[:,1]*KY-OY)/mpp-loc[1]]
b,g,r=[im[...,i].astype(int) for i in range(3)]
m=((b>180)&(r<140)&(g<110)).astype(np.uint8)*255
m[int(h*0.9):]=0
cv2.imwrite('bg_purple.png',m); print(m.sum()/255)
m2=cv2.dilate(m,np.ones((5,5),np.uint8)); ff=m2.copy(); mk=np.zeros((h+2,w+2),np.uint8); cv2.floodFill(ff,mk,(2,h//2),128)
inside=(ff!=128).astype(np.uint8)*255
inside=cv2.erode(inside,np.ones((5,5),np.uint8))
cs,_=cv2.findContours(inside,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
c=max(cs,key=cv2.contourArea)[:,0,:].astype(float)
P=Polygon(c).buffer(0).simplify(2.5)
print(P.geom_type,len(P.exterior.coords),P.area, P.bounds)
G=Polygon(fwd(np.array(P.exterior.coords))); print(G.is_valid,G.bounds)
pickle.dump(G,open('bg-poly.pkl','wb'))
ov=im.copy()
d=json.load(open('../raw5/bg-osm.json'))
for e in d['elements']:
    if e.get('type')=='way' and 'geometry' in e and e['tags'].get('highway') in ('primary','secondary','tertiary'):
        p=inv(np.array([(q['lon'],q['lat']) for q in e['geometry']])); cv2.polylines(ov,[np.round(p).astype(np.int32).reshape(-1,1,2)],False,(0,0,255),1)
cv2.polylines(ov,[np.round(np.array(P.exterior.coords)).astype(np.int32).reshape(-1,1,2)],True,(0,160,0),2)
cv2.imwrite('bg_trace.png',ov)
