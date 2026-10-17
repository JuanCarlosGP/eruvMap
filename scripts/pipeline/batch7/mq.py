import subprocess,json,time
q='[out:json][timeout:60];(way["place"="island"](47.5,-122.3,47.65,-122.1);rel["place"="island"](47.5,-122.3,47.65,-122.1);way["natural"="water"](47.55,-122.26,47.60,-122.2););out geom;'
open('/tmp/qm.q','w').write(q)
for t in range(5):
    subprocess.run(['curl','-s','-m','90','-A','eruvmap-derived-data/1.0 (QA)','--data-urlencode','data@/tmp/qm.q','https://maps.mail.ru/osm/tools/overpass/api/interpreter','-o','mer-island.json'])
    try:
        d=json.load(open('mer-island.json')); print([(e['type'],e['id'],e['tags'].get('name'),len(e.get('geometry',e.get('members',[])))) for e in d['elements']]); break
    except Exception as ex: print('retry'); time.sleep(5)
