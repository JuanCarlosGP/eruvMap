import json,numpy as np,cv2,math,sys,pickle
img,osmf,mode,lo_,hi_=sys.argv[1],sys.argv[2],sys.argv[3],float(sys.argv[4]),float(sys.argv[5])
im=cv2.imread(img); h,w=im.shape[:2]
hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
if mode=='yellow':
    m=((hsv[...,0]>=12)&(hsv[...,0]<=32)&(hsv[...,1]>50)&(hsv[...,2]>200)&(hsv[...,1]<200)).astype(np.uint8)*255
    hw=('motorway','trunk','primary','secondary','motorway_link','trunk_link')
else:
    g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY); m=(g>=250).astype(np.uint8)*255   # white roads
    hw=('motorway','trunk','primary','secondary','tertiary','residential','unclassified','motorway_link','trunk_link')
cv2.imwrite('gen_mask.png',m)
d=json.load(open(osmf))
la=[q['lat'] for e in d['elements'] if 'geometry' in e for q in e['geometry']]
lat0=np.mean(la); KX=111320*math.cos(math.radians(lat0)); KY=110574
ways=[np.array([(q['lon']*KX,-q['lat']*KY) for q in e['geometry']]) for e in d['elements'] if e.get('type')=='way' and 'geometry' in e and e['tags'].get('highway') in hw]
allp=np.vstack(ways); ox,oy=allp[:,0].min()-500,allp[:,1].min()-500; W=allp[:,0].max()-ox+500; H=allp[:,1].max()-oy+500
f=0.5
a=cv2.resize(m,None,fx=f,fy=f,interpolation=cv2.INTER_AREA).astype(np.float32); a=cv2.GaussianBlur(a,(0,0),2); a=(a-a.mean())/(a.std()+1e-9)
res=[]
for mpp in np.arange(lo_,hi_,(hi_-lo_)/40):
    sc=mpp/f; cw=int(W/sc); ch=int(H/sc)
    if cw<a.shape[1] or ch<a.shape[0]: continue
    canvas=np.zeros((ch,cw),np.uint8)
    for l in ways: cv2.polylines(canvas,[np.round((l-[ox,oy])/sc).astype(np.int32).reshape(-1,1,2)],False,255,2)
    b=cv2.GaussianBlur(canvas.astype(np.float32),(0,0),2); b=(b-b.mean())/(b.std()+1e-9)
    cc=cv2.matchTemplate(b,a,cv2.TM_CCOEFF_NORMED); _,mx,_,loc=cv2.minMaxLoc(cc); res.append((round(mx,3),round(mpp,3),loc))
res.sort(reverse=True); print(res[:6]); print(sorted(res,key=lambda r:r[1])[::4])
pickle.dump((res[0],ox,oy,lat0),open('gen_best.pkl','wb'))
