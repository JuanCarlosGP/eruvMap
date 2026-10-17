import pickle,sys
from helpers2 import *
from load2 import load2
R=lambda m: m/111000
def L(k,folder=None,exclude=('Directions',)):
    it=[(t,p,n,g) for t,p,n,g in load2(f'kml/{k}.kml') if t!='pt']
    if folder: it=[x for x in it if folder in x[1][-1]]
    it=[x for x in it if not any(e in x[1][-1] or e in x[2] for e in exclude)]
    return it
def lines(k,folder=None,exclude=('Directions',)): return [g for t,p,n,g in L(k,folder,exclude) if t=='line']
def poly(k,name): 
    r=[g for t,p,n,g in L(k) if t=='poly' and name in n]; assert len(r)==1,(k,name,len(r)); return r[0]
jobs={}
def line_job(key,k,r,folder=None,exclude=('Directions',)):
    ls=lines(k,folder,exclude); jobs[key]=('line',ls,close(ls,R(r)))
def poly_job(key,k,name):
    g=poly(k,name).buffer(0); jobs[key]=('poly',[g],g)
line_job('atl','atl1',50,'Toco')
poly_job('bham','birmingham','Overton')
line_job('chs','charleston',50,'BSBI Downtown')
poly_job('eng','englewood','Eruv Coverage')
poly_job('glen','glendale','Glendale Eruv'); poly_job('bay','glendale','Bayside'); poly_job('meq','glendale','Mequon'); poly_job('mke','glendale','Milwaukee East')
poly_job('av','miami','Aventura Eruv'); poly_job('avs','miami','Aventura South'); poly_job('hal','miami','Hallandale'); poly_job('hl','miami','Highland Lakes')
poly_job('nash','nashville','Nashville Eruv'); poly_job('op','overlandpark','Overland Park')
poly_job('port','portland','Main Eruv Boundary')
line_job('prov','providence',50)
poly_job('rva','richmondva','Eruv Boundaries')
line_job('sea','seattle',50)
line_job('sko','skokie',50)
line_job('wh','westhartford',50)
if __name__=='__main__':
    for k,(t,ls,g) in jobs.items():
        polys=list(g.geoms) if hasattr(g,'geoms') else [g]
        print(k,t,g.geom_type,len(polys),[round(p.area*1e4,2) for p in polys])
        if t=='poly': add(k,g,ls)
        else:
            polys=sorted(polys,key=lambda p:-p.area); add(k,polys[0] if len(polys)==1 else g,ls)
    pickle.dump(res,open('res4a.pkl','wb'))
    for k,v in res.items():
        print(k,v['nv'],round(v['iou'],3))
        preview(k,k,v['geom'],v['orig'],f'batch4-{k}.png')
