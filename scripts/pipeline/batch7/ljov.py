from gcp import *
import cv2,json,sys
n,p=load('../raw5/lj-osm.json')
G=[((205,36),inter(n,p,'Torrey Pines','Village')[0]),((295,200),inter(n,p,'Gilman','Alicante')[0]),((42,412),inter(n,p,'Torrey Pines','Jolla Parkway')[0])]
px=[a for a,_ in G]; ll=[b for _,b in G]
extra=eval(sys.argv[1]) if len(sys.argv)>1 else []
px+=extra[0] if extra else []; ll+=extra[1] if extra else []
f,res=fit(px,ll,'aff'); print(res)
A=np.c_[np.array(ll),np.ones(len(ll))]; sol=np.linalg.lstsq(A,np.array(px,float),rcond=None)[0]
im=cv2.imread('lj2.jpg'); d=json.load(open('../raw5/lj-osm.json'))
for e in d['elements']:
    if e.get('type')=='way' and 'geometry' in e and e['tags'].get('highway') in ('motorway','trunk','primary','secondary','tertiary','motorway_link','residential'):
        q=np.c_[[(g['lon'],g['lat']) for g in e['geometry']],np.ones(len(e['geometry']))]@sol
        c=(0,255,255) if e['tags']['highway']!='residential' else (255,255,0)
        cv2.polylines(im,[np.round(q).astype(np.int32).reshape(-1,1,2)],False,c,1)
cv2.imwrite('lj_ov.png',cv2.resize(im[:,:480],None,fx=1.6,fy=1.6))
import pickle; pickle.dump((px,ll),open('lj-gcp.pkl','wb'))
