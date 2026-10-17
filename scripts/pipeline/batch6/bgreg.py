import json,numpy as np,cv2,math,pickle
im=cv2.imread('../raw5/img/bg_big.png'); h,w=im.shape[:2]; print(w,h)
hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
# yellow/orange roads: hue 15-35, sat>60
m=((hsv[...,0]>=15)&(hsv[...,0]<=32)&(hsv[...,1]>70)&(hsv[...,2]>200)).astype(np.uint8)*255
m[int(h*0.92):]=0; m[:int(h*0.02)]=0
cv2.imwrite('bg_yel.png',m)
d=json.load(open('../raw5/bg-osm.json'))
lat0=42.16; KX=111320*math.cos(math.radians(lat0)); KY=110574
ways=[np.array([(q['lon']*KX,-q['lat']*KY) for q in e['geometry']]) for e in d['elements'] if e.get('type')=='way' and 'geometry' in e and e['tags'].get('highway') in ('primary','secondary','trunk')]
f=0.5
a=cv2.resize(m,None,fx=f,fy=f,interpolation=cv2.INTER_AREA).astype(np.float32); a=cv2.GaussianBlur(a,(0,0),2); a=(a-a.mean())/a.std()
ox=-88.02*KX; oy=-42.23*KY
res=[]
for mpp in np.arange(2.0,9.0,0.25):
    sc=mpp/f; cw=int(0.14*KX/sc); ch=int(0.14*KY/sc)
    if cw<a.shape[1] or ch<a.shape[0]: continue
    img=np.zeros((ch,cw),np.uint8)
    for l in ways:
        q=(l-[ox,oy])/sc; cv2.polylines(img,[np.round(q).astype(np.int32).reshape(-1,1,2)],False,255,2)
    b=cv2.GaussianBlur(img.astype(np.float32),(0,0),2); b=(b-b.mean())/b.std()
    cc=cv2.matchTemplate(b,a,cv2.TM_CCOEFF_NORMED); _,mx,_,loc=cv2.minMaxLoc(cc); res.append((mx,mpp,loc))
res.sort(reverse=True); print(res[:6])
