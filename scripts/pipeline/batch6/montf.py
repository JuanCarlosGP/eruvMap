import numpy as np,math
lat0=41.12; S=0.25
KX=111320*math.cos(math.radians(lat0)); KY=110574
OX=-74.25*KX; OY=-41.30*KY
def inv(ll,mpp,loc):
    sc=mpp/S
    mx=ll[:,0]*KX; my=-ll[:,1]*KY
    return np.c_[((mx-OX)/sc-loc[0])/S,((my-OY)/sc-loc[1])/S]
def fwd(xy,mpp,loc):
    sc=mpp/S; xy=np.asarray(xy,float)
    mx=(xy[:,0]*S+loc[0])*sc+OX; my=(xy[:,1]*S+loc[1])*sc+OY
    return np.c_[mx/KX,-my/KY]
