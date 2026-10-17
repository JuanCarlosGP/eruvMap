import subprocess,json,time,sys
def get(s,w,n,e,out,hw):
    q=f'[out:json][timeout:90];way["highway"~"^({hw})$"]({s},{w},{n},{e});out geom qt;'
    open('/tmp/qg_'+out+'.q','w').write(q)
    for t in range(6):
        for ep in ['https://overpass-api.de/api/interpreter','https://overpass.kumi.systems/api/interpreter','https://maps.mail.ru/osm/tools/overpass/api/interpreter']:
            subprocess.run(['curl','-s','-m','100','-A','eruvmap-derived-data/1.0 (QA)','--data-urlencode','data@/tmp/qg_'+out+'.q',ep,'-o',out])
            try: json.load(open(out)); return True
            except Exception: pass
        time.sleep(5)
    return False
if __name__=='__main__':
    s,w,n,e=map(float,sys.argv[1:5]); print(get(s,w,n,e,sys.argv[5],'motorway|trunk|primary|secondary|tertiary|unclassified|residential|service|motorway_link|trunk_link|primary_link|secondary_link'))
