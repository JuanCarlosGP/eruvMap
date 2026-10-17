import numpy as np,cv2,io,contextlib
from PIL import Image
from gm import *
img=np.array(Image.open('img/all_a.jpg').convert('RGB')); a=img.astype(int); R,G,B=a[:,:,0],a[:,:,1],a[:,:,2]
m=((R>=250)&(G>=250)&(B>=250)).astype(np.uint8)*255
m[:280]=0; m[955:]=0; m[:, :70]=0; m[:,1580:]=0
s=3; ys=cv2.resize(m,None,fx=1/s,fy=1/s,interpolation=cv2.INTER_AREA)
L=osm_lines('all-osm.json',['primary','secondary','tertiary','trunk','motorway'])
for mp in [2.8,3.0,3.2,3.4,3.6,3.8,4.0,4.4]:
    aff=init((825/s,620/s),(40.6055,-75.499),mp*s)
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf): aff=coarse(aff,L,ys,rng=70,step=3,sg=1.5)
    print(mp,buf.getvalue().strip(),flush=True)
