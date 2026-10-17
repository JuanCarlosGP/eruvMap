import pickle,sys
exec(open('geo3.py').read())
res=pickle.load(open(sys.argv[1],'rb'))
T=dict(l.split('|') for l in open(sys.argv[2]).read().strip().split('\n'))
for k,t in T.items():
    if k not in res: continue
    fn=f'batch3-{t.split("~")[0]}.png'
    preview(k,t.split('~')[1],res[k]['geom'],res[k]['orig'],fn); print(fn,flush=True)
