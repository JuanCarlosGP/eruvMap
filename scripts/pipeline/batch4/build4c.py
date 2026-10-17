import pickle
import helpers2
from helpers2 import *
helpers2.res.update(pickle.load(open('res4b.pkl','rb')))
res=helpers2.res
P=pickle.load(open('mtl.pkl','rb'))
main=[P['Greater Hampstead Eruv'],P['Cote-st-Luc Eruv'],P['CDN-NDG'],P['De Vimy']]
u=unary_union([g.buffer(0.00004) for g in main]); u=Polygon(u.exterior).buffer(-0.00004)
add('mtl',u,main)
out=P['Outremont Eruv - November 2023']; add('mtlo',out,[out])
pickle.dump(res,open('res4b.pkl','wb'))
for k in ['mtl','mtlo']:
    v=res[k]; print(k,v['nv'],round(v['iou'],3),flush=True); preview(k,k,v['geom'],[],f'batch4-{k}.png')
