import pickle,numpy as np,cv2,io,contextlib
from gm import *
r=pickle.load(open('../raw4/mon-vec.pkl','rb'))
def isteal(s): return s.startswith('rgb(20.4') 
S=0.2
H,W=int(3456*S),int(2592*S)
m=np.zeros((H,W),np.uint8)
n=0
for st,w,d,p in r:
    if (isteal(st) and w>=3 and not d) or (st.startswith('rgb(43.8') or st.startswith('rgb(80.3') or st.startswith('rgb(54.3')):
        if len(p)>1 and abs(p).max()<1e5 and p[:,0].min()>40 and p[:,0].max()<2550:
            cv2.polylines(m,[np.round(p*S).astype(np.int32).reshape(-1,1,2)],False,255,2); n+=1
print(n); cv2.imwrite('mon_hw.png',m)
L=osm_lines('../raw4/mon-osm.json',['motorway','trunk','primary','secondary'])
for mp in [25,30,35,40,45,50]:
    aff=init((W/2,H/2),(41.11,-74.06),mp)
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf): aff=coarse(aff,L,m,rng=80,step=4,sg=2)
    print(mp,buf.getvalue().strip(),flush=True)
