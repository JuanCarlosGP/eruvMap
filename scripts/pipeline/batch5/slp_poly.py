import numpy as np,cv2,pickle
from PIL import Image
from scipy import ndimage as ndi
from shapely.geometry import Polygon
from gm import *
from gcp import fit
k=564/1024
px=[(808,612),(808,415),(460,213),(460,612),(262,318),(868,333)][:5]
px=[(x*k,y*k) for x,y in px]
ll=[(44.9483894,-93.3289211),(44.9516843,-93.32877525),(44.9558071,-93.337801),(44.9484733,-93.337809),(44.9538959,-93.3428946)]
f,res=fit(px,ll); print('res',res.round(0))
aff=from_gcp(px,ll)
img=np.array(Image.open('img/slp.jpg').convert('RGB')); a=img.astype(int); R,G,B=a[:,:,0],a[:,:,1],a[:,:,2]
white=((R>=248)&(G>=248)&(B>=248)).astype(np.uint8)*255
L=osm_lines('slp-osm.json',['primary','secondary','tertiary','residential','trunk','motorway'])
aff=coarse(aff,L,white,rng=8,step=1,sg=2)
H=[(183,15),(385,22),(395,62),(435,88),(445,62),(470,95),(505,122),(545,125),(575,100),(740,92),(742,160),(750,180),(775,235),(805,285),(850,298),(850,288),(905,288),(915,310),(935,335),(933,610),(912,612),(910,708),(860,710),(755,712),(752,740),(665,740),(655,718),(630,712),(628,688),(607,688),(607,648),(525,650),(525,672),(410,750),(225,802),(125,798),(85,765),(100,700),(98,640),(100,585),(85,470),(75,380),(78,300),(95,225),(135,170),(138,145),(140,120)]
c=(np.array(H)*k).reshape(-1,1,2)
o=img.copy(); r=render(aff,L,img.shape[:2],1); o[r>0]=(0,160,0); cv2.polylines(o,[np.round(c).astype(np.int32)],True,(255,0,255),1); o=cv2.resize(o,None,fx=2,fy=2); Image.fromarray(o).save('img/slp_ov2.png')
p=Polygon([tuple(v) for v in pix2lonlat(aff,c[:,0,:])]).buffer(0); print(p.area*1e4)
pickle.dump(p,open('slp-poly.pkl','wb'))
