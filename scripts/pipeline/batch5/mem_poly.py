import numpy as np,cv2,pickle
from PIL import Image
from shapely.geometry import Polygon
from refine import *
px=[(476,805),(484,535),(468,1172),(1045,777),(437,2028),(437,1549),(946,2177),(969,1483)]
ll=[(35.1304597,-89.8873817),(35.1355494,-89.8871655),(35.1239176,-89.8876411),(35.13107755,-89.87352295),(35.1091618,-89.8883678),(35.1171974,-89.8879171),(35.1057195,-89.8772207),(35.1183162,-89.8766889)]
aff=from_gcp(px,ll)
a=np.array(Image.open('img/mem.png').convert('RGB')).astype(int)
R,G,B=a[:,:,0],a[:,:,1],a[:,:,2]
white=((R>=250)&(G>=250)&(B>=250)).astype(np.uint8)*255
white[:1300,:]=white[:1300,:]
L=osm_lines('mem-osm.json')
aff2,sc=refine(aff,L,white,sig=2)
lav=((abs(R-219)<4)&(abs(G-220)<4)&(abs(B-229)<4)).astype(np.uint8)
m=cv2.morphologyEx(lav,cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(45,45)))
cs,_=cv2.findContours(m,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE); c=max(cs,key=cv2.contourArea)
img=np.array(Image.open('img/mem.png').convert('RGB')); cv2.drawContours(img,[c],-1,(255,0,0),5)
r=render(aff2,L,white.shape); img[r>0]=(0,160,0); Image.fromarray(img).resize((600,1088)).save('img/mem_ov2.png')
p=Polygon([tuple(v) for v in pix2lonlat(aff2,c[:,0,:])]).buffer(0); print(p.area*1e4,p.bounds)
pickle.dump(p,open('mem-poly.pkl','wb'))
