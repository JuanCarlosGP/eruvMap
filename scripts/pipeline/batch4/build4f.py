import pickle
import helpers2
from helpers2 import *
res=helpers2.res; res.clear()
p=pickle.load(open('tlv-poly.pkl','rb'))[0]
add('tlv',p,[])
v=res['tlv']; print(v['nv'],round(v['iou'],3)); preview('tlv','tlv',v['geom'],[],'batch4-tlv.png')
old=pickle.load(open('res4c.pkl','rb')); old.update(res); pickle.dump(old,open('res4c.pkl','wb'))
