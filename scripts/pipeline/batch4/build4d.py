import pickle
import helpers2
from helpers2 import *
from build4 import line_job,jobs
helpers2.res.update(pickle.load(open('res4b.pkl','rb')))  # not used
res=helpers2.res; res.clear()
line_job('roc','rochester',50,'Rochester Eruv')
line_job('bet','bethesda',60)
for k in ['roc','bet']:
    t,ls,g=jobs[k]; polys=list(g.geoms) if hasattr(g,'geoms') else [g]
    print(k,g.geom_type,[round(p.area*1e4,2) for p in polys])
    add(k,g,ls)
    v=res[k]; print(v['nv'],round(v['iou'],3),flush=True); preview(k,k,v['geom'],ls,f'batch4-{k}.png')
pickle.dump(res,open('res4c.pkl','wb'))
