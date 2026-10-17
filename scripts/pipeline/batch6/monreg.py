import pickle,numpy as np,cv2,json,glob,math
r=pickle.load(open('../raw4/mon-vec.pkl','rb'))
S=0.25
H,W=int(3456*S),int(2592*S)
m=np.zeros((H,W),np.uint8)
for st,w,d,p in r:
    if st.startswith('rgb(100%, 100%, 100%)') or (st.startswith('rgb(20.4') and w>=3 and not d):
        if len(p)>1 and abs(p).max()<1e5 and p[:,0].min()>40 and p[:,0].max()<2550 and p[:,1].min()>40:
            if p[:,0].max()<760 and p[:,1].max()<1100 and w<2: continue  # info panel
            cv2.polylines(m,[np.round(p*S).astype(np.int32).reshape(-1,1,2)],False,255,1)
cv2.imwrite('mon_roads.png',m)
