import numpy as np,cv2,pickle,io,contextlib
from PIL import Image
from scipy import ndimage as ndi
from shapely.geometry import Polygon
from gm import *
img=np.array(Image.open('img/all_a.jpg').convert('RGB')); a=img.astype(int); R,G,B=a[:,:,0],a[:,:,1],a[:,:,2]
m=((R>=250)&(G>=250)&(B>=250)).astype(np.uint8)*255
m[:280]=0; m[955:]=0; m[:, :70]=0; m[:,1580:]=0
s=2; ys=cv2.resize(m,None,fx=1/s,fy=1/s,interpolation=cv2.INTER_AREA)
L=osm_lines('all-osm.json',['primary','secondary','tertiary','trunk','motorway','residential'])
best=None
for mp in [3.0,3.1,3.2,3.3,3.4]:
    aff=init((875/s,744/s),(40.5976063,-75.5278814),mp*s)
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf): a2=coarse(aff,L,ys,rng=24,step=2,sg=1.5)
    sc=float(buf.getvalue().split('(')[1].split(',')[0]); print(mp,buf.getvalue().strip(),flush=True)
    if best is None or sc>best[0]: best=(sc,mp,a2)
sc,mp,aff=best; print('best',mp)
