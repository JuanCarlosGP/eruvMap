import json,numpy as np,cv2,math,pickle
im=cv2.imread('p_nh-1.png'); hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
m=((hsv[...,0]>=18)&(hsv[...,0]<=34)&(hsv[...,1]>90)&(hsv[...,2]>200)).astype(np.uint8)*255
cv2.imwrite('nh_yel_mask.png',m)
d=json.load(open('../raw5/nh-osm.json'))
la=[q['lat'] for e in d['elements'] if 'geometry' in e for q in e['geometry']]; lat0=np.mean(la)
KX=111320*math.cos(math.radians(lat0)); KY=110574
ways=[np.array([(q['lon']*KX,-q['lat']*KY) for q in e['geometry']]) for e in d['elements'] if e.get('type')=='way' and 'geometry' in e and e['tags'].get('highway') in ('primary','secondary','trunk','motorway','motorway_link','trunk_link')]
allp=np.vstack(ways); ox,oy=allp[:,0].min()-3000,allp[:,1].min()-3000; W=allp[:,0].max()-ox+3000; H=allp[:,1].max()-oy+3000
f=0.25
a=cv2.resize(m,None,fx=f,fy=f,interpolation=cv2.INTER_AREA).astype(np.float32); a=cv2.GaussianBlur(a,(0,0),1.5); a=(a-a.mean())/(a.std()+1e-9)
res=[]
for rot in np.arange(19,23.1,0.5):
  for mpp in np.arange(4.35,4.66,0.05):
    sc=mpp/f; cw=int(W/sc*1.0); ch=int(H/sc)
    c,s=math.cos(math.radians(rot)),math.sin(math.radians(rot))
    cx,cy=cw/2,ch/2
    canvas=np.zeros((ch*2,cw*2),np.uint8)
    for l in ways:
        q=(l-[ox,oy])/sc; q=(q-[cx,cy])@np.array([[c,-s],[s,c]])+[cx*2,cy*2]
        cv2.polylines(canvas,[np.round(q).astype(np.int32).reshape(-1,1,2)],False,255,2)
    b=cv2.GaussianBlur(canvas.astype(np.float32),(0,0),1.5); b=(b-b.mean())/(b.std()+1e-9)
    if b.shape[0]<a.shape[0] or b.shape[1]<a.shape[1]: continue
    cc=cv2.matchTemplate(b,a,cv2.TM_CCOEFF_NORMED); _,mx,_,loc=cv2.minMaxLoc(cc); res.append((round(mx,4),float(rot),float(mpp),loc,(cw,ch)))
res.sort(reverse=True); print(res[:8])

pickle.dump((res[0],ox,oy,lat0,f),open('nh-reg.pkl','wb'))
