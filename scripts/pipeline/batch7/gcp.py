import json,collections,numpy as np
def load(f):
    d=json.load(open(f)); nodes=collections.defaultdict(set); pos={}
    for e in d['elements']:
        if e['type']=='way' and 'geometry' in e:
            n=e['tags'].get('name') or e['tags'].get('ref')
            for nid,g in zip(e['nodes'],e['geometry']):
                pos[nid]=(g['lon'],g['lat'])
                if n: nodes[nid].add(n)
    return nodes,pos
def inter(nodes,pos,a,b):
    r=[pos[n] for n,s in nodes.items() if any(a in x for x in s) and any(b in x for x in s)]
    return r
def fit(px,ll,kind='aff'):
    px=np.array(px,float); ll=np.array(ll,float); lat0=ll[:,1].mean()
    KX=111320*np.cos(np.radians(lat0)); KY=110574
    m=np.c_[ll[:,0]*KX,ll[:,1]*KY]
    if kind=='sim':
        A=[];B=[]
        for (x,y),(X,Y) in zip(px,m): A+= [[x,-y,1,0],[y,x,0,1]]; B+=[X,Y]
        s=np.linalg.lstsq(np.array(A),np.array(B),rcond=None)[0]
        M=np.array([[s[0],-s[1],s[2]],[s[1],s[0],s[3]]])
    else:
        A=np.c_[px,np.ones(len(px))]; sol=np.linalg.lstsq(A,m,rcond=None)[0]; M=sol.T
    def f(p):
        p=np.asarray(p,float); q=np.c_[p,np.ones(len(p))]@M.T; return np.c_[q[:,0]/KX,q[:,1]/KY]
    res=np.hypot(*(np.c_[(f(px)-ll)[:,0]*KX,(f(px)-ll)[:,1]*KY]).T)
    return f,res
