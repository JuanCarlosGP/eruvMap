import numpy as np,cv2,pickle
from PIL import Image
from scipy import ndimage as ndi
from shapely.geometry import Polygon
from gm import *
img=np.array(Image.open('img/irv.png').convert('RGB')); a=img.astype(int); R,G,B=a[:,:,0],a[:,:,1],a[:,:,2]
white=((R>=250)&(G>=250)&(B>=250)).astype(np.uint8)*255
L=osm_lines('irv-osm.json',['primary','secondary','tertiary','residential','trunk','motorway'])
aff=init((278,384),(33.657344775,-117.82777917499999),3.98)
aff=coarse(aff,L,white,rng=30,step=2,sg=3); aff=coarse(aff,L,white,rng=4,step=1,sg=2)

mag=((R>200)&(G<90)&(B>200)).astype(np.uint8)
d=cv2.dilate(mag,np.ones((5,5),np.uint8)); fl=cv2.erode(ndi.binary_fill_holes(d>0).astype(np.uint8),np.ones((5,5),np.uint8))
fl=cv2.morphologyEx(fl,cv2.MORPH_OPEN,np.ones((9,9),np.uint8))
cs,_=cv2.findContours(fl,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE); c=max(cs,key=cv2.contourArea); print(cv2.contourArea(c),img.shape)
o=img.copy(); r=render(aff,L,img.shape[:2],1); o[r>0]=(0,160,0); cv2.drawContours(o,[c],-1,(255,0,255),1); Image.fromarray(o).save('img/irv_ov2.png')
p=Polygon([tuple(v) for v in pix2lonlat(aff,c[:,0,:])]).buffer(0); print(p.area*1e4)
pickle.dump(p,open('irv-poly.pkl','wb'))
