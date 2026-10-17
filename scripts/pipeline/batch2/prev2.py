import pickle,sys
sys.path.insert(0,'.')
exec(open('helpers2.py').read())
res=pickle.load(open('res2.pkl','rb'))
T={'det':('batch2-detroit-eruv-perimeter.png','Detroit Eruv (detroiteruv.org official boundary)'),
'tn':('batch2-toronto-north-eruv-perimeter.png','Toronto Eruv - North (torontoeruv.org)'),
'ts':('batch2-toronto-south-eruv-perimeter.png','Toronto Eruv - South (torontoeruv.org)'),
'trh':('batch2-richmond-hill-eruv-perimeter.png','Richmond Hill Eruv (torontoeruv.org map)'),
'wh':('batch2-lower-washington-heights-eruv-perimeter.png','Lower Washington Heights Eruv (eruv.nyc raster, georeferenced)')}
for k,(fn,t) in T.items():
    preview(k,t,res[k]['geom'],res[k]['orig'],fn); print(fn)
