import numpy as np,cv2,json,math,pickle
from PIL import Image
from shapely.geometry import Polygon
a=np.array(Image.open('balt.jpg').convert('RGB')).astype(int)
R,G,B=a[:,:,0],a[:,:,1],a[:,:,2]
yel=(R>220)&(G>220)&(B<205)&(B>140)
org=(R>225)&(G>150)&(G<205)&(B<140)
sal=(R>230)&(G>170)&(G<215)&(B>150)&(B<200)&(R-B>35)
red=(R>200)&(G<90)&(B<90)
m=(yel|org|sal|red).astype(np.uint8)
m[:, 1255:]=0; m[:58]=0; m[1015:]=0; m[:, :100]=0
m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(25,25)))
cnts,_=cv2.findContours(m,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
c=max(cnts,key=cv2.contourArea)
filled=np.zeros_like(m); cv2.drawContours(filled,[c],-1,1,-1)
filled=cv2.morphologyEx(filled,cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11)))
cnts,_=cv2.findContours(filled,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE); c=max(cnts,key=cv2.contourArea)
print(cv2.contourArea(c),len(c))
np.save('balt-filled.npy',filled)
img=np.array(Image.open('balt.jpg').convert('RGB')); ov=img.copy(); cv2.drawContours(ov,[c],-1,(0,0,255),3); Image.fromarray(ov).resize((1000,int(1000*ov.shape[0]/ov.shape[1]))).save('balt_poly_ov.png')
r=json.load(open('balt-reg.json')); sc,rot,loc,W,x0,y0=r['sc'],math.radians(r['rot']),r['loc'],r['W'],r['x0'],r['y0']
lat0,lon0=r['lat0'],r['lon0']; kx=111320*math.cos(math.radians(lat0)); ky=110574
pts=[]
cs,sn=math.cos(rot),math.sin(rot)
for (ix,iy) in c[:,0,:]:
    cxp=ix-x0+loc[0]; cyp=iy-y0+loc[1]
    X=(cxp-W//2)*sc; Y=(W//2-cyp)*sc   # rotated frame (render: x'=(x c - y s)/sc ; y'=(x s + y c)/sc)
    x=X*cs+Y*sn; y=-X*sn+Y*cs
    pts.append((lon0+x/kx,lat0+y/ky))
p=Polygon(pts).buffer(0); print(p.geom_type,p.area*1e4,[round(v,4) for v in p.bounds])
pickle.dump(p,open('balt-poly.pkl','wb'))
