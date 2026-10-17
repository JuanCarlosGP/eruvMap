import subprocess,json,sys,time,os
def get(s,w,n,e,out,hw='motorway|trunk|primary|secondary|tertiary|residential|unclassified'):
    q=f'[out:json][timeout:90];way["highway"~"^({hw})$"]({s},{w},{n},{e});out geom qt;'
    open('/tmp/q_'+out+'.q','w').write(q)
    for t in range(4):
        subprocess.run(['curl','-s','-m','100','-A','eruvmap-derived-data/1.0 (QA)','--data-urlencode','data@/tmp/q_'+out+'.q','https://maps.mail.ru/osm/tools/overpass/api/interpreter','-o',out])
        try: json.load(open(out)); return True
        except Exception: time.sleep(5)
    return False
if __name__=='__main__':
    import numpy as np
    s0,w0,n0,e0=map(float,sys.argv[1:5]); pre=sys.argv[5]; step=float(sys.argv[6])
    i=0
    for s in np.arange(s0,n0,step):
        for w in np.arange(w0,e0,step):
            f=f'{pre}-{i}.json'; i+=1
            if os.path.exists(f): continue
            print(f,get(s,w,s+step,w+step,f),flush=True)
