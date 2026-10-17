import numpy as np,cv2
from PIL import Image
from tilereg import *
a=np.array(Image.open('img/bg.png').convert('RGB')); g=cv2.cvtColor(a,cv2.COLOR_RGB2GRAY)
t=g[20:740,0:618]
for z,sc in [(14,[x/100 for x in range(60,200,10)]),(15,[x/100 for x in range(40,110,5)])]:
    M,X0,Y0=mosaic(z,42.155,-87.96,4); Mg=cv2.cvtColor(M,cv2.COLOR_RGB2GRAY)
    for s in sc:
        tt=cv2.resize(t,None,fx=s,fy=s,interpolation=cv2.INTER_AREA)
        if tt.shape[0]>=Mg.shape[0] or tt.shape[1]>=Mg.shape[1]: continue
        r=cv2.matchTemplate(Mg,tt,cv2.TM_CCOEFF_NORMED); _,mx,_,loc=cv2.minMaxLoc(r); print(z,s,round(mx,3),loc,flush=True)
