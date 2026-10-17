import re, xml.etree.ElementTree as ET, json
from shapely.geometry import LineString, Polygon, Point
ns={'k':'http://www.opengis.net/kml/2.2'}
def coords(t):
    out=[]
    for c in t.split():
        p=c.split(',')
        out.append((float(p[0]),float(p[1])))
    return out
def load(mid):
    r=ET.parse(mid+'.kml').getroot()
    items=[]
    for pm in r.iter('{%s}Placemark'%ns['k']):
        n=pm.find('k:name',ns); n=n.text if n is not None else ''
        for ls in pm.iter('{%s}LineString'%ns['k']):
            items.append(('line',n,LineString(coords(ls.find('k:coordinates',ns).text))))
        for pg in pm.iter('{%s}Polygon'%ns['k']):
            o=pg.find('.//k:outerBoundaryIs//k:coordinates',ns)
            holes=[coords(h.text) for h in pg.findall('.//k:innerBoundaryIs//k:coordinates',ns)]
            items.append(('poly',n,Polygon(coords(o.text),holes)))
        for pt in pm.iter('{%s}Point'%ns['k']):
            items.append(('pt',n,Point(coords(pt.find('k:coordinates',ns).text)[0])))
    return items
def loadcc():
    from shapely.geometry import shape
    d=json.load(open('cc.geojson'))
    return [('line' if f['geometry']['type']=='LineString' else f['geometry']['type'],f['properties'].get('name',''),shape(f['geometry'])) for f in d['features']]
