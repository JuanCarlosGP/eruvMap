import pickle,numpy as np,cv2,io,contextlib
from gm import *
r=pickle.load(open('../raw4/mon-vec.pkl','rb'))
S=0.1
H,W=int(3456*S),int(2592*S)
m=np.zeros((H,W),np.uint8)
for st,w,d,p in r:
    if (st.startswith('rgb(20.4') and w>=3 and not d) or (st.startswith('rgb(43.8') or st.startswith('rgb(80.3') or st.startswith('rgb(54.3')):
        if len(p)>1 and abs(p).max()<1e5 and p[:,0].min()>40 and p[:,0].max()<2550 and p[:,1].min()>40:
            cv2.polylines(m,[np.round(p*S).astype(np.int32).reshape(-1,1,2)],False,255,1)
L=osm_lines('../raw4/mon-osm.json',['motorway','trunk','primary'])
out=[]
for mp in [9,10,11,12,13,14,15,17]:
    aff=init((1278*S,2365*S),(41.1145,-74.149),mp/S)
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf): a2=coarse(aff,L,m,rng=70,step=2,sg=1.2)
    print(mp,buf.getvalue().strip(),flush=True)
