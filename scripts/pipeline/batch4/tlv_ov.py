import numpy as np,cv2,json,math
from PIL import Image
from reg import *
r=json.load(open('tlv-reg.json')); sc,rot,loc,W,x0,y0=r['sc'],r['rot'],r['loc'],r['W'],r['x0'],r['y0']
L,_,_=load_osm('tlv-osm.json',r['lat0'],r['lon0'])
can=render(L,sc,math.radians(rot),W,W,W//2,W//2)
img=np.array(Image.open('w3/tlv_kav.jpg').convert('RGB')); H,Wi=img.shape[:2]
cx=loc[0]-x0; cy=loc[1]-y0
crop=can[cy:cy+H,cx:cx+Wi]; crop=cv2.dilate(crop,np.ones((3,3),np.uint8))
ov=img.copy(); ov[crop>0]=(255,0,0)
Image.fromarray(ov).resize((905,1280)).save('tlv_ov.png')
