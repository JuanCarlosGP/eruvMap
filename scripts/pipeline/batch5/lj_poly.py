import numpy as np,cv2,pickle
from PIL import Image
from scipy import ndimage as ndi
from shapely.geometry import Polygon
from gm import *
from gcp import fit
px=[(200,37),(293,205),(42,410),(268,38)]
ll=[(32.87014675,-117.2408458),(32.8622431,-117.2362876),(32.85022583333333,-117.25195129999999),(32.8719331,-117.23774750000001)]
f,res=fit(px,ll); print('res',res.round(0))
aff=from_gcp(px,ll)
img=np.array(Image.open('img/lj2.jpg').convert('RGB')); a=img.astype(int); R,G,B=a[:,:,0],a[:,:,1],a[:,:,2]
red=((R>190)&(G<70)&(B<70)); red[:,460:]=False; red[:,:15]=False
d=cv2.dilate(red.astype(np.uint8),np.ones((7,7),np.uint8)); fl=cv2.erode(ndi.binary_fill_holes(d>0).astype(np.uint8),np.ones((7,7),np.uint8))
cs,_=cv2.findContours(fl,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE); c=max(cs,key=cv2.contourArea); print(cv2.contourArea(c))
L=osm_lines('lj-osm.json',['motorway','trunk','primary','secondary','tertiary'])
o=img.copy(); r=render(aff,L,img.shape[:2],1); o[r>0]=(255,255,0); cv2.drawContours(o,[c],-1,(255,0,255),1); Image.fromarray(o).save('img/lj_ov1.png')
p=Polygon([tuple(v) for v in pix2lonlat(aff,c[:,0,:])]).buffer(0); print(p.area*1e4)
pickle.dump(p,open('lj-poly.pkl','wb'))
