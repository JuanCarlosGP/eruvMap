import numpy as np,math
lat0=40.60; KX=111320*math.cos(math.radians(lat0)); KY=110574
OX=-75.60*KX; OY=-40.66*KY
P=dict(mpp=4.92,loc=(370,668))
def fwd(xy,P=P):
    xy=np.asarray(xy,float); sc=P['mpp']
    X=(xy[:,0]+P['loc'][0])*sc+OX; Y=(xy[:,1]+P['loc'][1])*sc+OY
    return np.c_[X/KX,-Y/KY]
def inv(ll,P=P):
    sc=P['mpp']; X=ll[:,0]*KX; Y=-ll[:,1]*KY
    return np.c_[(X-OX)/sc-P['loc'][0],(Y-OY)/sc-P['loc'][1]]
