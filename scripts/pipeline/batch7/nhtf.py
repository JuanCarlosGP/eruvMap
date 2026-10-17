import pickle,math,numpy as np
(sc_,rot,mpp,loc,(cw,ch)),ox,oy,lat0,f=pickle.load(open('nh-reg.pkl','rb'))
KX=111320*math.cos(math.radians(lat0)); KY=110574
c,s=math.cos(math.radians(rot)),math.sin(math.radians(rot)); R=np.array([[c,-s],[s,c]]); sc=mpp/f
cen=np.array([cw/2,ch/2])
def png2ll(P):
    P=np.asarray(P,float); q=P*f+loc
    u=(q-2*cen)@R.T+cen; XY=u*sc+[ox,oy]
    return np.c_[XY[:,0]/KX,-XY[:,1]/KY]
def ll2png(ll):
    ll=np.asarray(ll); XY=np.c_[ll[:,0]*KX,-ll[:,1]*KY]; u=(XY-[ox,oy])/sc
    q=(u-cen)@R+2*cen; return (q-loc)/f
