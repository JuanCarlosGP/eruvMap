import pickle,sys
import helpers2
from helpers2 import *
def go(key,pklfile,fn=None):
    p=pickle.load(open(pklfile,'rb')); add(key,p,[])
    v=helpers2.res[key]; print(key,v['nv'],round(v['iou'],3),flush=True)
    preview(key,key,v['geom'],[],f'batch5-{key}.png')
    try: old=pickle.load(open('res5.pkl','rb'))
    except Exception: old={}
    old[key]=v; pickle.dump(old,open('res5.pkl','wb'))
if __name__=='__main__': go(sys.argv[1],sys.argv[2])
