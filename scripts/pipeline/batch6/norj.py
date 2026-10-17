import json,numpy as np,cv2,math,pickle,collections
from scipy.spatial import cKDTree
from skimage.morphology import skeletonize
rng=np.random.default_rng(1)
thin=cv2.imread('nor_thin.png',0)>0
thin=cv2.morphologyEx(thin.astype(np.uint8),cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
sk=skeletonize(thin>0).astype(np.uint8)
nb=cv2.filter2D(sk,-1,np.ones((3,3),np.float32),borderType=cv2.BORDER_CONSTANT)-sk
J=(sk>0)&(nb>=3)
J=cv2.dilate(J.astype(np.uint8),np.ones((9,9),np.uint8))
n,lab,st,cen=cv2.connectedComponentsWithStats(J)
S=cen[1:]; print('scan junctions',len(S))
d=json.load(open('nor-osm.json'))
lat0=36.86; KX=111320*math.cos(math.radians(lat0)); KY=110574
cnt=collections.Counter(); pos={}
for e in d['elements']:
    if e['type']=='way' and 'geometry' in e and e['tags'].get('highway') in ('residential','tertiary','secondary','primary','unclassified'):
        for nid,g in zip(e['nodes'],e['geometry']): cnt[nid]+=1; pos[nid]=(g['lon']*KX,-g['lat']*KY)
O=np.array([pos[n] for n,c in cnt.items() if c>=2]); print('osm junctions',len(O))
# search: scan px -> meters : similarity s*R*x+t ; allow mirror no
tree=cKDTree(O)
best=(0,None)
Sn=len(S)
from itertools import product
for it in range(400000):
    i,j=rng.choice(Sn,2,replace=False); a,b=rng.choice(len(O),2,replace=False)
    v1=S[j]-S[i]; v2=O[b]-O[a]; d1=np.hypot(*v1)
    if d1<200: continue
    s=np.hypot(*v2)/d1
    if not(1.6<s<4.6): continue
    ang=math.atan2(v2[1],v2[0])-math.atan2(v1[1],v1[0])
    if abs(math.degrees((ang+math.pi)%(2*math.pi)-math.pi))>25: continue
    c,sn=math.cos(ang),math.sin(ang); R=s*np.array([[c,-sn],[sn,c]])
    t=O[a]-R@S[i]
    P=S@R.T+t
    dd,_=tree.query(P,distance_upper_bound=18)
    k=int((dd<18).sum())
    if k>best[0]: best=(k,(R,t,s,ang)); print(it,k,s,math.degrees(ang),flush=True)
pickle.dump(best,open('nor-ransac.pkl','wb'))
