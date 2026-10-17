import numpy as np,cv2,pickle
from scipy import ndimage as ndi
from PIL import Image
from shapely.geometry import Polygon
from refine import *
px=[(285,288),(285,645),(470,288),(470,645),(690,288)]
ll=[(41.248626775,-96.1195607),(41.23408695,-96.119510625),(41.2486252,-96.1097912),(41.23408695,-96.1097912),(41.2486597,-96.0974778)]
aff=from_gcp(px,ll)
a=np.array(Image.open('img/oma1.jpg').convert('RGB')).astype(int)
R,G,B=a[:,:,0],a[:,:,1],a[:,:,2]
white=((R>=248)&(G>=248)&(B>=248)).astype(np.uint8)*255
white[:, :190]=0
L=osm_lines('oma-osm.json',['primary','secondary','tertiary','residential','trunk','unclassified'])
aff2,sc=refine(aff,L,white,sig=2); print(sc)
c=np.array([(275,48),(378,48),(384,107),(633,110),(631,195),(636,200),(632,278),(666,282),(668,318),(641,322),(640,358),(633,362),(631,630),(645,655),(275,655)])
img=np.array(Image.open('img/oma1.jpg').convert('RGB')); cv2.polylines(img,[c.reshape(-1,1,2)],True,(255,0,255),1)
r=render(aff2,L,white.shape); img[r>0]=(0,160,0); Image.fromarray(img).save('img/oma_ov3.png')
p=Polygon([tuple(v) for v in pix2lonlat(aff2,c)]).buffer(0); print(p.area*1e4,p.bounds)
pickle.dump(p,open('oma-poly.pkl','wb'))
