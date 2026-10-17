from gcp import *
import cv2,numpy as np,json
n,p=load('../raw5/slp-osm.json')
k=1/0.9078
G=[((262,213),('26th','Quentin')),((610,213),('26th','Joppa')),((458,213),('26th','Monterey')),((262,613),('Minnetonka','Quentin')),((610,613),('Minnetonka','Joppa')),((417,706),('31st','Natchez')),((262,415),('28th','Quentin')),((610,415),('28th','Joppa')),((556,291),('27th','Kipling')),((656,331),('Cedar Lake Av','Inglewood'))]
px=[];ll=[]
for (x,y),(a,b) in G:
    r=inter(n,p,a,b); px.append((x*k,y*k)); ll.append(r[0])
f,res=fit(px,ll); print(np.round(res,1))
import pickle; pickle.dump((px,ll),open('slp-gcp.pkl','wb'))
im=cv2.imread('slp_big.png')
d=json.load(open('../raw5/slp-osm.json'))
# inverse by sampling: fit reverse affine
fi,_=fit(ll,px)  # not meaningful scales; do manual inverse
A=np.c_[np.array(ll),np.ones(len(ll))]; sol=np.linalg.lstsq(A,np.array(px),rcond=None)[0]
for e in d['elements']:
    if e['type']=='way' and 'geometry' in e and e['tags'].get('highway') in ('residential','tertiary','secondary','primary'):
        q=np.c_[[(g['lon'],g['lat']) for g in e['geometry']],np.ones(len(e['geometry']))]@sol
        cv2.polylines(im,[np.round(q).astype(np.int32).reshape(-1,1,2)],False,(0,0,255),1)
cv2.imwrite('slp_ov.png',im)
