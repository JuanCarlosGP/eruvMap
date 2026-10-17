import sys
from load import *
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
def ov(items,out,pts=False):
    fig,ax=plt.subplots(figsize=(12,12))
    for k,n,g in items:
        if k=='line': x,y=g.xy; ax.plot(x,y,lw=1)
        elif k=='poly': x,y=g.exterior.xy; ax.plot(x,y,lw=1)
        elif pts and k=='pt': ax.plot(g.x,g.y,'k.',ms=2)
    ax.set_aspect(1/0.8); fig.savefig(out,dpi=70)
if __name__=='__main__':
    ov(load('1uh_hbGmyful743HBD5E7HNj7fc4'),'ov5t.png')
    ov(load('1tvzN1lm0vi9vmObe9_SVpnxCOmc'),'ovbos.png')
    ov(load('1WvS7elEjWZFUEvMUpoCtDuMWZqo'),'ovss.png')
    ov(loadcc(),'ovcc.png')
