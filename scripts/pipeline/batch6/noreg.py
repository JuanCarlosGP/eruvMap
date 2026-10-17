import json,numpy as np,cv2,math,pickle
im=cv2.imread('nor_img-000.jpg',0); print(im.shape)
bw=(im<110).astype(np.uint8)*255
# remove thick perimeter lines
thick=cv2.morphologyEx(bw,cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7)))
thin=cv2.subtract(bw,cv2.dilate(thick,np.ones((5,5),np.uint8)))
# also exclude title and legend regions
thin[:200]=0; thin[930:]=0
cv2.imwrite('nor_thin.png',thin)
d=json.load(open('nor-osm.json'))
lat0=36.86; KX=111320*math.cos(math.radians(lat0)); KY=110574
ways=[np.array([(q['lon']*KX,-q['lat']*KY) for q in e['geometry']]) for e in d['elements'] if e['type']=='way' and 'geometry' in e and e['tags'].get('highway') in ('residential','tertiary','secondary','primary','unclassified','trunk')]
# scan px per meter mpp; downscale scan by f
f=0.5
a=cv2.resize(thin,None,fx=f,fy=f,interpolation=cv2.INTER_AREA)
a=cv2.GaussianBlur(a.astype(np.float32),(0,0),2.5); a=(a-a.mean())/a.std()
h,w=a.shape
ox=-76.33*KX; oy=-36.90*KY
best=[]
for rot in np.arange(-8,8.1,2):
  for mpp in np.arange(2.0,4.01,0.25):   # meters per ORIGINAL scan px
    sc=mpp/f  # meters per resized px
    cw=int(0.08*KX/sc); ch=int(0.07*KY/sc)
    img=np.zeros((ch,cw),np.uint8)
    c,s=math.cos(math.radians(rot)),math.sin(math.radians(rot))
    cx,cy=cw/2,ch/2
    for l in ways:
        q=(l-[ox,oy])/sc; q=(q-[cx,cy])@np.array([[c,-s],[s,c]])+[cx,cy]
        cv2.polylines(img,[np.round(q).astype(np.int32).reshape(-1,1,2)],False,255,1)
    b=cv2.GaussianBlur(img.astype(np.float32),(0,0),2.5); b=(b-b.mean())/b.std()
    cc=cv2.matchTemplate(b,a,cv2.TM_CCORR); _,mx,_,loc=cv2.minMaxLoc(cc)
    best.append((mx/a.size,rot,mpp,loc)); 
best.sort(reverse=True)
for x in best[:8]: print(x)
pickle.dump(best,open('nor-best.pkl','wb'))
