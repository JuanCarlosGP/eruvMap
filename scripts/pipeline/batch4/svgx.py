import re,pickle,numpy as np
from lxml import etree
ns='{http://www.w3.org/2000/svg}'
def mat(t):
    m=np.eye(3)
    for f,a in re.findall(r'(\w+)\(([^)]*)\)',t or ''):
        v=[float(x) for x in re.split(r'[ ,]+',a.strip())]
        if f=='matrix': M=np.array([[v[0],v[2],v[4]],[v[1],v[3],v[5]],[0,0,1]])
        elif f=='translate': M=np.array([[1,0,v[0]],[0,1,v[1] if len(v)>1 else 0],[0,0,1]])
        elif f=='scale': M=np.array([[v[0],0,0],[0,v[-1],0],[0,0,1]])
        else: continue
        m=m@M
    return m
tok=re.compile(r'[MLCZmlcz]|-?\d+\.?\d*(?:e-?\d+)?')
def poly(d,M):
    t=tok.findall(d); i=0; out=[]; cur=[]; cmd=None
    def P(x,y): 
        p=M@np.array([x,y,1.0]); return (p[0],p[1])
    while i<len(t):
        if t[i] in 'MLCZmlcz': cmd=t[i]; i+=1
        if cmd=='M':
            if cur: out.append(cur)
            cur=[P(float(t[i]),float(t[i+1]))]; i+=2; cmd='L'
        elif cmd=='L': cur.append(P(float(t[i]),float(t[i+1]))); i+=2
        elif cmd=='C': cur.append(P(float(t[i+4]),float(t[i+5]))); i+=6
        elif cmd in 'Zz': 
            if cur: cur.append(cur[0])
            i+=0; cmd=None
            if i>=len(t): break
        else: i+=1
    if cur: out.append(cur)
    return out
res=[]
def walk(el,M,depth=0,skip=False):
    for c in el:
        tag=c.tag.replace(ns,'')
        if tag=='defs': continue
        if tag=='g':
            walk(c,M@mat(c.get('transform')))
        elif tag=='path':
            st=c.get('stroke'); 
            if not st or st=='none': continue
            Mm=M@mat(c.get('transform'))
            for p in poly(c.get('d'),Mm):
                if len(p)>1: res.append((st,float(c.get('stroke-width') or 1),c.get('stroke-dasharray'),np.array(p)))
root=etree.parse('mon.svg',etree.XMLParser(huge_tree=True)).getroot()
walk(root,np.eye(3))
print(len(res))
pickle.dump(res,open('mon-vec.pkl','wb'))
