import numpy as np,cv2
from shapely.geometry import Polygon
def trace(img,maskfn,close=7,erode=7,simp=2.0,seed=(2,2)):
    im=cv2.imread(img); h,w=im.shape[:2]
    m=maskfn(im).astype(np.uint8)*255
    m2=cv2.dilate(m,np.ones((close,close),np.uint8)); ff=m2.copy(); mk=np.zeros((h+2,w+2),np.uint8); cv2.floodFill(ff,mk,seed,128)
    inside=(ff!=128).astype(np.uint8)*255
    inside=cv2.erode(inside,np.ones((erode,erode),np.uint8))
    cs,_=cv2.findContours(inside,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    c=max(cs,key=cv2.contourArea)[:,0,:].astype(float)
    P=Polygon(c).buffer(0).simplify(simp)
    print('traced',P.geom_type,len(P.exterior.coords),P.area,'img',w*h)
    return P
