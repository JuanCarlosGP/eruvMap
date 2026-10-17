import numpy as np,cv2,json,math,pickle
from PIL import Image
from shapely.geometry import Polygon
a=np.array(Image.open('w3/tlv_kav.jpg').convert('RGB')).astype(int)
R,G,B=a[:,:,0],a[:,:,1],a[:,:,2]
bl=((R<90)&(G>60)&(G<170)&(B>200)).astype(np.uint8)
bl[1500:1800,1400:]=0   # legend sample
bl[2300:,1500:]=0; bl[1700:1760,1500:]=0
bl[1650:1760, 1500:]=0
m=cv2.dilate(bl,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(41,41)))
H,W=m.shape
inv=(1-m).astype(np.uint8); n,lab,st,_=cv2.connectedComponentsWithStats(inv,connectivity=4)
outside=lab==lab[5,5]
filled=(~outside).astype(np.uint8)
# remove legend box and text: keep big comps
n,lab,st,_=cv2.connectedComponentsWithStats(filled)
keep=np.zeros_like(filled)
for i in range(1,n):
    if st[i,4]>200000: keep[lab==i]=1
print([st[i,4] for i in range(1,n)])
filled=cv2.erode(keep,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(41,41)))  # undo dilation
cs,_=cv2.findContours(filled,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
img=np.array(Image.open('w3/tlv_kav.jpg').convert('RGB')); ov=img.copy()
cv2.drawContours(ov,cs,-1,(255,0,0),4)
Image.fromarray(ov).resize((905,1280)).save('tlv_poly_ov2.png')
r=json.load(open('tlv-reg.json')); sc,rot,loc,Wc,x0,y0=r['sc'],math.radians(r['rot']),r['loc'],r['W'],r['x0'],r['y0']
lat0,lon0=r['lat0'],r['lon0']; kx=111320*math.cos(math.radians(lat0)); ky=110574
polys=[]
for c in cs:
    if cv2.contourArea(c)<50000: continue
    pts=[]
    for ix,iy in c[:,0,:]:
        X=(ix-x0+loc[0]-Wc//2)*sc; Y=(Wc//2-(iy-y0+loc[1]))*sc
        pts.append((lon0+X/kx,lat0+Y/ky))
    polys.append(Polygon(pts).buffer(0)); print(polys[-1].area*1e4)
pickle.dump(polys,open('tlv-poly.pkl','wb'))
