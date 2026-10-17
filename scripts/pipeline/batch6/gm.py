import numpy as np,cv2,math
from PIL import Image
from refine import *
def init(anchor_px,anchor_ll,mpp):
    # no rotation; y down. anchor_ll=(lat,lon)
    la,lo=anchor_ll; dlat=mpp/110574; dlon=mpp/(111320*math.cos(math.radians(la)))
    M=[[dlon,0],[0,-dlat]]; M=np.array(M); t=np.array([lo,la])-M@np.array(anchor_px,float)
    return Aff(M,t)
def coarse(aff,L,mask,rng=60,step=4,sg=4):
    mb=cv2.GaussianBlur(mask.astype(np.float32),(0,0),sg); mb=(mb-mb.mean())/(mb.std()+1e-9)
    best=(-9,0,0)
    for dx in range(-rng,rng+1,step):
        for dy in range(-rng,rng+1,step):
            a=Aff(aff.M,aff.t+aff.M@np.array([dx,dy]))
            r=cv2.GaussianBlur(render(a,L,mask.shape).astype(np.float32),(0,0),sg); r=(r-r.mean())/(r.std()+1e-9)
            s=float((r*mb).mean())
            if s>best[0]: best=(s,dx,dy)
    s,dx,dy=best; print('coarse',best); return Aff(aff.M,aff.t+aff.M@np.array([dx,dy]))
