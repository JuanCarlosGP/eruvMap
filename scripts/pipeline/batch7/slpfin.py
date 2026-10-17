import cv2,numpy as np,pickle,json
from shapely.geometry import Polygon,mapping
im=cv2.imread('slp_big.png'); k=1/0.9078
hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
orange=((hsv[...,0]>=5)&(hsv[...,0]<=15)&(hsv[...,1]>150)&(hsv[...,2]>150))
navy=((hsv[...,0]>=105)&(hsv[...,0]<=125)&(hsv[...,1]>150)&(hsv[...,2]<150))
yel=((hsv[...,0]>=22)&(hsv[...,0]<=32)&(hsv[...,1]>150)&(hsv[...,2]>200))
mask=(orange|navy|yel)
ys,xs=np.nonzero(mask); pts=np.c_[xs,ys]
from scipy.spatial import cKDTree
T=cKDTree(pts)
D=[(183,20),(265,15),(385,22),(400,58),(420,82),(440,62),(468,66),(480,95),(505,122),(545,125),(578,95),(740,93),(745,170),(790,260),(805,300),(812,305),(845,305),(870,290),(900,288),(912,300),(905,335),(935,337),(932,610),(910,640),(905,643),(858,655),(858,710),(752,710),(752,740),(665,738),(652,718),(632,715),(627,688),(605,670),(605,648),(525,648),(525,705),(410,750),(360,765),(220,800),(130,798),(85,765),(95,690),(100,585),(90,400),(75,300),(95,215),(140,170),(140,150)]
S=[]
for x,y in D:
    d,i=T.query([x*k,y*k]); S.append(pts[i] if d<14 else (x*k,y*k)); 
S=np.array(S,float)
ov=im.copy(); cv2.polylines(ov,[S.astype(np.int32).reshape(-1,1,2)],True,(0,200,0),2); cv2.imwrite('slp_trace.png',ov)
px,ll=pickle.load(open('slp-gcp.pkl','rb'))
A=np.c_[np.array(px),np.ones(len(px))]; sol=np.linalg.lstsq(A,np.array(ll),rcond=None)[0]
G=Polygon(np.c_[S,np.ones(len(S))]@sol); print(G.is_valid,G.area*1e4*0.7*1.0)
pickle.dump(G.buffer(0),open('slp-poly.pkl','wb'))
