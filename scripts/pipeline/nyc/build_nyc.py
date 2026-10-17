import numpy as np, json, re, sys
from shapely.geometry import Polygon, MultiPolygon, LineString, shape, mapping
from shapely.ops import unary_union, transform
from skimage import measure
from scipy import ndimage as ndi
import matplotlib;matplotlib.use('Agg');import matplotlib.pyplot as plt
import urllib.request
D='raw/nyc/'
lat0=40.78;kx=111320*np.cos(np.radians(lat0));ky=110574
p=np.load(D+'par2.npy')
def pix2ll(P):
    a,b,c,d,tx,ty=p;M=np.array([[a,b],[c,d]]);Q=P@M.T+[tx,ty]
    return np.c_[Q[:,0]/kx-73.97,Q[:,1]/ky+lat0]
inm=np.load(D+'in.npy');land=np.load(D+'land.npy')
inm=ndi.binary_fill_holes(inm)
lab,n=ndi.label(inm);sz=ndi.sum(inm,lab,range(1,n+1));inm=lab==(1+np.argmax(sz))
cs=measure.find_contours(np.pad(inm,1).astype(float),0.5)
c=max(cs,key=len)-1
ll=pix2ll(np.c_[c[:,1],-c[:,0]])
man=Polygon(ll).buffer(0)
def simp(poly,maxv=150):
    tol=0.00005
    while True:
        s=poly.simplify(tol,preserve_topology=True)
        if len(s.exterior.coords)-1<=maxv: return s,tol
        tol*=1.15
man_s,tol=simp(man)
def rnd(poly):
    return Polygon([(round(x,5),round(y,5)) for x,y in poly.exterior.coords])
man_s=rnd(man_s)
assert man_s.is_valid,'man invalid'
print('manhattan verts',len(man_s.exterior.coords)-1,'tol deg',tol,'valid',man_s.is_valid,'area km2',Polygon(np.c_[(np.array(man_s.exterior.coords)[:,0]+73.97)*kx,(np.array(man_s.exterior.coords)[:,1]-lat0)*ky]).area/1e6, 'full area',Polygon(np.c_[(ll[:,0]+73.97)*kx,(ll[:,1]-lat0)*ky]).area/1e6)
# Brooklyn
t=open('b.kml').read()
pts=[]
for m in re.finditer(r'<Placemark>(.*?)</Placemark>',t,re.S):
    b=m.group(1);n=re.search(r'<name>(.*?)</name>',b).group(1)
    if not n.startswith('Line'):continue
    cc=re.search(r'<coordinates>(.*?)</coordinates>',b,re.S).group(1).split()
    seg=[tuple(map(float,x.split(',')[:2])) for x in cc]
    pts+=seg if not pts else seg
bk=Polygon(pts).buffer(0)
print('bk raw',len(pts),bk.geom_type,bk.is_valid)
bk_s,tolb=simp(bk if bk.geom_type=='Polygon' else max(bk.geoms,key=lambda g:g.area),150)
bk_s=rnd(bk_s);assert bk_s.is_valid
print('brooklyn verts',len(bk_s.exterior.coords)-1,tolb)
def mdev(a,b):
    return a.exterior.hausdorff_distance(b.exterior)*110000
print('hausdorff m: man',mdev(man,man_s),'bk',mdev(bk,bk_s))
common=dict(country='US',geometry_kind='perimeter',status='unknown',
 license='All rights reserved by source; approximate traced derivative, shown with attribution pending community permission',
 verified_at='2026-10-17',geometry_precision='approximate',
 note="Traced approximately from the official map; always check the community's official map and status before relying on it")
feats=[
 dict(type='Feature',properties=dict(id='manhattan-eruv',name_en='Manhattan Eruv',city='New York (Manhattan)',source='Manhattan Eruv Inc. (eruv.nyc)',source_url='https://eruv.nyc/eruv-map.pdf',**common),geometry=mapping(man_s)),
 dict(type='Feature',properties=dict(id='brooklyn-eruv',name_en='Brooklyn Eruv',city='New York (Brooklyn)',source='Brooklyn Eruv (brooklyneruv.com)',source_url='https://www.brooklyneruv.com/eruv-boundaries/',**common),geometry=mapping(bk_s))]
json.dump(dict(type='FeatureCollection',features=feats),open('nyc-eruvs.geojson','w'),indent=1,ensure_ascii=False)
# previews
g=json.load(open(D+'nom.json'))[0]['geojson']['coordinates']
isl=np.array(max(g,key=lambda q:len(q[0]))[0])
fig,ax=plt.subplots(1,2,figsize=(12,12),gridspec_kw={'width_ratios':[1,1.0]})
ax[0].plot(*isl.T,'k-',lw=.8,label='OSM Manhattan Island outline (Nominatim, ODbL)')
x,y=man_s.exterior.xy;ax[0].fill(x,y,fc='#f08070',alpha=.5,ec='r',lw=1,label='Traced eruv (%d vertices)'%(len(x)-1))
ax[0].set_aspect(1/np.cos(np.radians(40.78)));ax[0].legend(loc='lower right',fontsize=7);ax[0].set_title('Manhattan Eruv - approximate trace of eruv.nyc map (3/2023)')
im=plt.imread(D+'m-1.png');ax[1].imshow(im);ax[1].axis('off');ax[1].set_title('Source map (eruv.nyc/eruv-map.pdf)')
plt.tight_layout();plt.savefig('manhattan-preview.png',dpi=80);plt.close()
fig,ax=plt.subplots(figsize=(10,8))
x,y=bk.exterior.xy;ax.plot(x,y,'b-',lw=.6,label='KML geometry (georeference only, full detail)')
x,y=bk_s.exterior.xy;ax.fill(x,y,fc='#80b0f0',alpha=.5,ec='r',lw=1.2,label='Traced eruv (%d vertices)'%(len(x)-1))
try:
    req=urllib.request.Request('https://nominatim.openstreetmap.org/search?q=Brooklyn,New+York&format=jsonv2&polygon_geojson=1&limit=1&featuretype=settlement',headers={'User-Agent':'eruvmap-research/1.0'})
    r=json.load(urllib.request.urlopen(req))
    for x_ in r:
        gg=x_['geojson'];
        for pl in (gg['coordinates'] if gg['type']=='MultiPolygon' else [gg['coordinates']]):
            a=np.array(pl[0]);ax.plot(a[:,0],a[:,1],'k-',lw=.5)
    ax.plot([],[],'k-',lw=.5,label='OSM Brooklyn admin outline (ODbL)')
except Exception as e:print('nominatim',e)
ax.set_aspect(1/np.cos(np.radians(40.65)));ax.legend(fontsize=7);ax.set_title('Brooklyn Eruv - approximate trace (brooklyneruv.com map)')
plt.tight_layout();plt.savefig('brooklyn-preview.png',dpi=80)
