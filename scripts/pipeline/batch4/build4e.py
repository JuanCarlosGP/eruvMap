import pickle
import helpers2
from helpers2 import *
res=helpers2.res; res.clear()
p=pickle.load(open('balt-poly.pkl','rb'))
add('balt',p,[])
v=res['balt']; print(v['nv'],round(v['iou'],3)); preview('balt','balt',v['geom'],[],'batch4-balt.png')
old=pickle.load(open('res4c.pkl','rb')); old.update(res); pickle.dump(old,open('res4c.pkl','wb'))
