import numpy as np,cv2,json
from PIL import Image
from tilereg import *
a=np.array(Image.open('img/cin200-1.png').convert('RGB')); H,W=a.shape[:2]
g=cv2.cvtColor(a,cv2.COLOR_RGB2GRAY)
mask=np.ones_like(g,np.uint8)*255
mask[:200,:760]=0; mask[1180:1420,80:540]=0; mask[560:1260,1520:2160]=0; mask[:170]=0; mask[1600:]=0; mask[:,:90]=0; mask[:,1960:]=0
R,G,B=[a[:,:,i].astype(int) for i in range(3)]
blue=(B>200)&(R<80)&(G<80)
mask[cv2.dilate(blue.astype(np.uint8),np.ones((9,9),np.uint8))>0]=0
g=g.copy(); 
for z,sc in [(16,[x/100 for x in range(70,140,6)]),(15,[x/100 for x in range(40,75,4)])]:
    best,_=match(g,mask,z,39.19,-84.43,6,sc); print(z,best,flush=True)
