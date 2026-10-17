import json,subprocess
base=json.loads(subprocess.check_output(['git','show','HEAD:data/eruvs.geojson'],cwd='../eruvmap-repo'))
b=json.load(open('./batch4-eruvs.geojson'))
rep={f['properties'].get('replaces_id') for f in b['features']}-{None}
ids={f['properties']['id'] for f in base['features']}
assert rep<=ids,rep-ids
new=[f for f in base['features'] if f['properties']['id'] not in rep]
for f in b['features']:
    f['properties'].pop('replaces_id',None); assert f['properties']['id'] not in ids; new.append(f)
base['features']=new
json.dump(base,open('../eruvmap-repo/data/eruvs.geojson','w'),ensure_ascii=False,indent=4)
print(len(new),len(rep))
