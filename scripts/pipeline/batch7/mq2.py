import subprocess,json,time
qs={'mer-island.json':'[out:json][timeout:60];(way["place"="island"]["name"="Mercer Island"];rel["place"="island"]["name"="Mercer Island"];);out geom;',
'mer-roads.json':'[out:json][timeout:90];way["highway"~"^(motorway|trunk|primary|secondary|tertiary|residential)$"](47.53,-122.26,47.60,-122.20);out geom qt;'}
E=['https://maps.mail.ru/osm/tools/overpass/api/interpreter','https://overpass-api.de/api/interpreter','https://overpass.kumi.systems/api/interpreter','https://overpass.private.coffee/api/interpreter']
for out,q in qs.items():
    open('/tmp/qm2.q','w').write(q); ok=False
    for t in range(6):
        for e in E:
            subprocess.run(['curl','-s','-m','100','-A','eruvmap-derived-data/1.0 (QA)','--data-urlencode','data@/tmp/qm2.q',e,'-o',out])
            try: json.load(open(out)); ok=True; print(out,e,flush=True); break
            except Exception: pass
        if ok: break
        time.sleep(10)
    print(out,ok,flush=True)
