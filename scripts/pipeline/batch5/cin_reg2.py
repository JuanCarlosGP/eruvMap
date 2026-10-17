import numpy as np,cv2
from PIL import Image
import tilereg
from tilereg import *
a=np.array(Image.open('img/cin200-1.png').convert('RGB'))
g=cv2.cvtColor(a,cv2.COLOR_RGB2GRAY)
mask=np.ones_like(g,np.uint8)*255
mask[:200,:760]=0; mask[1180:1420,80:540]=0; mask[560:1260,1520:2160]=0; mask[:170]=0; mask[1600:]=0; mask[:,:90]=0; mask[:,1960:]=0
R,G,B=[a[:,:,i].astype(int) for i in range(3)]
blue=(B>200)&(R<80)&(G<80)
mask[cv2.dilate(blue.astype(np.uint8),np.ones((15,15),np.uint8))>0]=0
def edges(x):
    x=cv2.GaussianBlur(x,(0,0),1.5); gx=cv2.Sobel(x,cv2.CV_32F,1,0); gy=cv2.Sobel(x,cv2.CV_32F,0,1); return cv2.magnitude(gx,gy)
M,X0,Y0=mosaic(16,39.195,-84.43,9); Me=edges(cv2.cvtColor(M,cv2.COLOR_RGB2GRAY))
ge=edges(g); ge[mask==0]=0
best=None
for s in [x/100 for x in range(138,156,1)]:
    t=cv2.resize(ge,None,fx=s,fy=s,interpolation=cv2.INTER_AREA)
    t=t[int(170*s):int(1600*s),int(90*s):int(1960*s)]
    if t.shape[0]>=Me.shape[0] or t.shape[1]>=Me.shape[1]: continue
    r=cv2.matchTemplate(Me,t.astype(np.float32),cv2.TM_CCOEFF_NORMED); _,mx,_,loc=cv2.minMaxLoc(r)
    print(s,round(mx,3),loc,flush=True)
    if best is None or mx>best[0]: best=(mx,s,loc)
print(best)
import json; json.dump(dict(best=best,X0=X0,Y0=Y0),open('cin-reg.json','w'),default=float)
