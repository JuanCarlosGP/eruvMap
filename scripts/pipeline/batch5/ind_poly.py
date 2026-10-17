import numpy as np,cv2,pickle
from PIL import Image
from scipy import ndimage as ndi
from shapely.geometry import Polygon
from refine import *
from gcp import fit
k=935/627
px=[(583,44),(583,776),(375,42),(378,775),(165,360),(163,42),(60,783)]
px=[(x*k,y*k) for x,y in px]
ll=[(39.897635,-86.165046),(39.87259135,-86.1650158),(39.897608,-86.174505),(39.871985,-86.174521),(39.886174,-86.183922),(39.897518,-86.183977),(39.871851,-86.18872)]
f,res=fit(px,ll); print('res m',res.round(0))
aff=from_gcp(px,ll)
L=osm_lines('ind-osm.json',['primary','secondary','tertiary','residential','unclassified'])
img=np.array(Image.open('img/p_ind-1.png').convert('RGB'))
a=img.astype(int); R,G,B=a[:,:,0],a[:,:,1],a[:,:,2]
red=((R>180)&(G<70)&(B<70)).astype(np.uint8)
print(red.sum())
d=cv2.dilate(red,np.ones((9,9),np.uint8))
fl=cv2.erode(ndi.binary_fill_holes(d>0).astype(np.uint8),np.ones((9,9),np.uint8))
cs,_=cv2.findContours(fl,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE); c=max(cs,key=cv2.contourArea); print(cv2.contourArea(c),img.shape)
o=img.copy(); r=render(aff,L,img.shape[:2],1); o[r>0]=(255,255,0)
cv2.drawContours(o,[c],-1,(255,0,255),1); Image.fromarray(o).save('img/ind_ov.png')
p=Polygon([tuple(v) for v in pix2lonlat(aff,c[:,0,:])]).buffer(0); print(p.area*1e4,p.bounds)
pickle.dump(p,open('ind-poly.pkl','wb'))
