import sys; sys.path.insert(0,'.')
from reg import *
import json,pickle
from skimage import measure
from shapely.geometry import Polygon
mx,sc,rot,loc,W=json.load(open('pce-reg.json'))
reg=np.load('pce-reg200.npy')
c=max(measure.find_contours(np.pad(reg,1).astype(float),.5),key=len)-1
lat0,lon0=40.855,-74.15
kx=111320*math.cos(math.radians(lat0)); ky=110574
c_,s_=math.cos(math.radians(rot)),math.sin(math.radians(rot))
def tr(row,col):
    u=(col/2-518)/2; v=(row/2-28)/2
    px=loc[0]+u; py=loc[1]+v
    xm=(px-W/2)*sc; ym=(W/2-py)*sc
    X=xm*c_+ym*s_; Y=-xm*s_+ym*c_
    return (lon0+X/kx, lat0+Y/ky)
p=Polygon([tr(r,cc) for r,cc in c]).buffer(0)
print(p.geom_type,p.area*1e4)
pickle.dump(p,open('pce-poly.pkl','wb'))
# registration residual: median distance of mask pixels to nearest osm road px
import scipy.ndimage as ndi
m=np.load('pce-mask.npy')
can=render(load_osm('pce-osm.json',lat0,lon0)[0],sc,math.radians(rot),W,W,W//2,W//2)
crop=can[loc[1]:loc[1]+m.shape[0],loc[0]:loc[0]+m.shape[1]]
dt=ndi.distance_transform_edt(crop==0)
d=dt[m>127]*sc
print('median m',np.median(d),'p75',np.percentile(d,75),'p90',np.percentile(d,90))
