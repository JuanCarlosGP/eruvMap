import numpy as np,cv2,pickle
from PIL import Image
from scipy import ndimage as ndi
from shapely.geometry import Polygon
from refine import *
from gcp import fit
px=[(125,579),(290,322),(335,639),(412,106),(515,321)]
ll=[(39.035484,-77.1944283),(39.0562996,-77.1794241),(39.0305285,-77.1727654),(39.07390,-77.16455),(39.05635,-77.15420)]
f,res=fit(px,ll); print('res m',res.round(0))
aff=from_gcp(px,ll)
L=osm_lines('pot-osm.json',['motorway','trunk','primary','secondary','tertiary'])
img=np.array(Image.open('img/pot.png').convert('RGB'))
a=img.astype(int); R,G,B=a[:,:,0],a[:,:,1],a[:,:,2]
blue=((B-np.maximum(R,G))>70).astype(np.uint8)
d=cv2.dilate(blue,np.ones((19,19),np.uint8))
fl=cv2.erode(ndi.binary_fill_holes(d>0).astype(np.uint8),np.ones((27,27),np.uint8))
print(blue.sum(),d.sum(),fl.sum())
cs,_=cv2.findContours(fl,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE); c=max(cs,key=cv2.contourArea); print(cv2.contourArea(c))
o=img.copy(); r=render(aff,L,img.shape[:2],2); o[r>0]=(255,0,0) if False else (255,255,0)
cv2.drawContours(o,[c],-1,(255,0,255),1); Image.fromarray(o).save('img/pot_ov.png')
p=Polygon([tuple(v) for v in pix2lonlat(aff,c[:,0,:])]).buffer(0); print(p.area*1e4,p.bounds)
pickle.dump(p,open('pot-poly.pkl','wb'))
