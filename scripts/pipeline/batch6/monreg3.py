import numpy as np,cv2,json,math
from scipy.signal import fftconvolve
m=cv2.imread('mon_roads.png',0); S=0.25
H,W=m.shape
d=json.load(open('../raw4/mon-osm.json'))
ways=[]
for e in d['elements']:
    if e['type']=='way' and 'geometry' in e and e['tags'].get('highway') in ('motorway','trunk','primary','secondary'):
        ways.append((e['tags']['highway'],np.array([(p['lon'],p['lat']) for p in e['geometry']])))
lat0=41.12
def merc(ll): 
    x=ll[:,0]*111320*math.cos(math.radians(lat0)); y=-ll[:,1]*110574; return np.c_[x,y]  # meters, y down
# PDF mask: only thick roads (teal highways) for major match
r=__import__('pickle').load(open('../raw4/mon-vec.pkl','rb'))
mm=np.zeros((H,W),np.uint8)
for st,w,dd,p in r:
    if (st.startswith('rgb(20.4') and w>=3 and not dd) or st.startswith('rgb(80.3') or st.startswith('rgb(54.3') :
        if len(p)>1 and abs(p).max()<1e5 and p[:,0].min()>40 and p[:,0].max()<2550 and p[:,1].min()>40:
            cv2.polylines(mm,[np.round(p*S).astype(np.int32).reshape(-1,1,2)],False,255,2)
cv2.imwrite('mon_major.png',mm)
a=cv2.GaussianBlur(mm.astype(np.float32),(0,0),2); a=(a-a.mean())/a.std()
best=[]
for mpp in np.arange(5.6,5.92,0.02):   # meters per PDF point
    sc=mpp/S  # meters per raster px
    # OSM raster in same px size, large canvas
    Ws,Hs=int(W*1.6),int(H*1.6)
    # canvas covers lon -74.2..-73.86 etc -> use bounds
    ox=-74.25*111320*math.cos(math.radians(lat0)); oy=-41.30*110574
    canvas_w=int((0.45*111320*math.cos(math.radians(lat0)))/sc); canvas_h=int((0.35*110574)/sc)
    img=np.zeros((canvas_h,canvas_w),np.uint8)
    for t,l in ways:
        p=(merc(l)-[ox,oy])/sc
        cv2.polylines(img,[np.round(p).astype(np.int32).reshape(-1,1,2)],False,255,2)
    b=cv2.GaussianBlur(img.astype(np.float32),(0,0),2); b=(b-b.mean())/b.std()
    cc=cv2.matchTemplate(b,a,cv2.TM_CCORR)
    _,mx,_,loc=cv2.minMaxLoc(cc)
    best.append((mx/(a.size),mpp,loc)); print(round(mpp,2),round(mx/a.size,4),loc,flush=True)
