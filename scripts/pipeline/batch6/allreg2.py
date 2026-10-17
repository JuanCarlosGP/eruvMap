import json,numpy as np,cv2,math,pickle
im=cv2.imread('al_live.jpg'); hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
# orange highways
m=((hsv[...,0]>=8)&(hsv[...,0]<=20)&(hsv[...,1]>120)&(hsv[...,2]>200)).astype(np.uint8)*255
m[:280]=0;m[950:]=0
cv2.imwrite('al_orange.png',m)
d=json.load(open('all-big.json'))
lat0=40.60; KX=111320*math.cos(math.radians(lat0)); KY=110574
ways=[(e['tags']['highway'],np.array([(q['lon']*KX,-q['lat']*KY) for q in e['geometry']])) for e in d['elements'] if e['type']=='way' and 'geometry' in e and e['tags'].get('highway') in ('motorway','trunk','motorway_link','trunk_link','primary')]
print(len(ways))
f=1.0
a=cv2.resize(m,None,fx=f,fy=f,interpolation=cv2.INTER_AREA).astype(np.float32); a=cv2.GaussianBlur(a,(0,0),3); a=(a-a.mean())/a.std()
ox=-75.60*KX; oy=-40.66*KY
res=[]
for mpp in np.arange(4.7,5.12,0.02):
    sc=mpp/f; cw=int(0.20*KX/sc); ch=int(0.12*KY/sc)
    img=np.zeros((ch,cw),np.uint8)
    for t,l in ways:
        q=(l-[ox,oy])/sc; cv2.polylines(img,[np.round(q).astype(np.int32).reshape(-1,1,2)],False,255,3 if t!='primary' else 1)
    b=cv2.GaussianBlur(img.astype(np.float32),(0,0),3); b=(b-b.mean())/b.std()
    if b.shape[0]<a.shape[0] or b.shape[1]<a.shape[1]: continue
    cc=cv2.matchTemplate(b,a,cv2.TM_CCOEFF_NORMED); _,mx,_,loc=cv2.minMaxLoc(cc); res.append((mx,mpp,loc))
res.sort(reverse=True); print(res[:6]); print(sorted(res,key=lambda r:r[1])[::5])
