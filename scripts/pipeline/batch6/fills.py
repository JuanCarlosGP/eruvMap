import re,pickle,numpy as np,sys
sys.path.insert(0,'../raw4')
from lxml import etree
ns='{http://www.w3.org/2000/svg}'
exec(open('../raw4/svgx.py').read().split('res=[]')[0])
from shapely.geometry import Polygon
from shapely.ops import unary_union
out=[]
def walk2(el,M):
    for c in el:
        tag=c.tag.replace(ns,'')
        if tag=='defs': continue
        if tag=='g': walk2(c,M@mat(c.get('transform')))
        elif tag=='path':
            f=c.get('fill')
            if not f or f=='none': continue
            Mm=M@mat(c.get('transform'))
            rings=[np.array(p) for p in poly(c.get('d'),Mm) if len(p)>3]
            if not rings: continue
            a=np.vstack(rings)
            out.append((f,c.get('fill-rule'),c.get('fill-opacity'),rings))
root=etree.parse('../raw4/mon.svg',etree.XMLParser(huge_tree=True)).getroot()
walk2(root,np.eye(3))
print(len(out))
pickle.dump(out,open('mon-fills.pkl','wb'))
