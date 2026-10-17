import json,numpy as np,cv2,math,pickle
r=pickle.load(open('prin-vec.pkl','rb'))
S=0.25; H,W=int(2592*S),int(1728*S)
m=np.zeros((H,W),np.uint8)
for st,w,d,p in r:
    if st.startswith('rgb(61.3') or st.startswith('rgb(80.0'):
        if len(p)>1 and abs(p).max()<1e5: cv2.polylines(m,[np.round(p*S).astype(np.int32).reshape(-1,1,2)],False,255,1)
m[int(2592*S*0.915):]=0
cv2.imwrite('prin_roads.png',m)
d=json.load(open('prin-osm.json'))
lat0=40.35; KX=111320*math.cos(math.radians(lat0)); KY=110574
ways=[np.array([(q['lon']*KX,-q['lat']*KY) for q in e['geometry']]) for e in d['elements'] if e.get('type')=='way' and 'geometry' in e and e['tags'].get('highway') in ('primary','secondary','tertiary','unclassified','residential','trunk','motorway','primary_link','secondary_link')]
allp=np.vstack(ways); ox,oy=allp[:,0].min()-500,allp[:,1].min()-500; Wm=allp[:,0].max()-ox+500; Hm=allp[:,1].max()-oy+500
a=cv2.GaussianBlur(m.astype(np.float32),(0,0),1.5); a=(a-a.mean())/a.std()
res=[]
for rot in range(-20,21,5):
  for mpp in np.arange(1.5,5.0,0.25):   # m per pt
    sc=mpp/S; cw=int(Wm/sc); ch=int(Hm/sc)
    if cw<W or ch<H: continue
    c,s=math.cos(math.radians(rot)),math.sin(math.radians(rot)); cen=np.array([cw/2,ch/2])
    canvas=np.zeros((ch*2,cw*2),np.uint8)
    for l in ways:
        q=(l-[ox,oy])/sc; q=(q-cen)@np.array([[c,-s],[s,c]])+2*cen
        cv2.polylines(canvas,[np.round(q).astype(np.int32).reshape(-1,1,2)],False,255,1)
    b=cv2.GaussianBlur(canvas.astype(np.float32),(0,0),1.5); b=(b-b.mean())/b.std()
    cc=cv2.matchTemplate(b,a,cv2.TM_CCOEFF_NORMED); _,mx,_,loc=cv2.minMaxLoc(cc); res.append((round(mx,3),rot,float(mpp),loc,(cw,ch)))
res.sort(reverse=True); print(res[:6])
pickle.dump((res[0],ox,oy,lat0,S),open('prin-reg.pkl','wb'))
