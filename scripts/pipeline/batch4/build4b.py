import pickle,json
import helpers2
from helpers2 import *
from load2 import load2
res=helpers2.res
d=json.load(open('w3/mel.json'))
zs=[Polygon([(l['lon'],l['lat']) for l in z['points']]) for z in d]
mel=unary_union([z.buffer(0.00003) for z in zs]); mel=Polygon(mel.exterior if mel.geom_type=='Polygon' else max(mel.geoms,key=lambda g:g.area).exterior)
print('mel',mel.geom_type,mel.area*1e4)
add('mel',mel,zs)
man=pickle.load(open('w3/man.pkl','rb'))
add('man',man['mainBoundaryData'][0],man['mainBoundaryData']+man['oldBoundaryData'])
add('whf',man['whitefieldBoundaryData'][0],man['whitefieldBoundaryData'])
it=load2('kml/montreal.kml')
P={n:g.buffer(0) for t,p,n,g in it}
for n,g in P.items(): print(n,round(g.area*1e4,2),[round(x,3) for x in g.bounds])
main=[P['Greater Hampstead Eruv'],P['Cote-st-Luc Eruv'],P['CDN-NDG'],P['De Vimy']]
u=unary_union([g.buffer(0.00004) for g in main])
print(u.geom_type, [round(g.area*1e4,2) for g in (u.geoms if hasattr(u,'geoms') else [u])])
pickle.dump(P,open('mtl.pkl','wb'))
pce=pickle.load(open('pce-poly.pkl','rb')); print('pce',pce.geom_type,pce.area*1e4)
add('pce',pce,[])
pickle.dump(res,open('res4b.pkl','wb'))
for k,v in res.items():
    print(k,v['nv'],round(v['iou'],3),flush=True)
    preview(k,k,v['geom'],[],f'batch4-{k}.png')
