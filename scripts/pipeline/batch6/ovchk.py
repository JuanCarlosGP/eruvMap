import numpy as np,cv2,json,subprocess
from montf import *
subprocess.run(['pdftoppm','-r','72','-scale-to-x','1296','-png','../raw4/monsey.pdf','mp'])
img=cv2.imread('mp-1.png'); k=1296/2592
d=json.load(open('../raw4/mon-osm.json'))
for e in d['elements']:
    if e['type']=='way' and 'geometry' in e and e['tags'].get('highway') in ('motorway','trunk','primary','secondary'):
        p=inv(np.array([(q['lon'],q['lat']) for q in e['geometry']]),5.84,(293,319))*k
        cv2.polylines(img,[np.round(p).astype(np.int32).reshape(-1,1,2)],False,(0,0,255),2)
cv2.imwrite('mon_ov.png',img[800:1700,0:1296])
