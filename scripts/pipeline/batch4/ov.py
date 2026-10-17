import subprocess,json,sys
def overpass(q,out):
    for e in ['https://maps.mail.ru/osm/tools/overpass/api/interpreter']:
        for t in range(3):
            r=subprocess.run(['curl','-s','-m','60','-A','eruvmap-derived-data/1.0 (QA)','--data-urlencode','data@'+q,e,'-o',out,'-w','%{http_code}'],capture_output=True,text=True)
            try:
                json.load(open(out)); return True
            except Exception: pass
    return False
