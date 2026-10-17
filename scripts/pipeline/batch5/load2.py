import xml.etree.ElementTree as ET
from shapely.geometry import LineString, Polygon, Point
K='{http://www.opengis.net/kml/2.2}'
def co(t): return [tuple(map(float,c.split(',')[:2])) for c in t.split()]
def load2(path):
    r=ET.parse(path).getroot(); out=[]
    def walk(el,path):
        for ch in el:
            tag=ch.tag.replace(K,'')
            if tag in('Folder','Document'):
                n=ch.find(K+'name'); walk(ch,path+[ (n.text or '').strip() if n is not None else ''])
            elif tag=='Placemark':
                n=ch.find(K+'name'); n=(n.text or '').strip() if n is not None else ''
                for ls in ch.iter(K+'LineString'): out.append(('line',path,n,LineString(co(ls.find(K+'coordinates').text))))
                for pg in ch.iter(K+'Polygon'):
                    o=pg.find('.//'+K+'outerBoundaryIs//'+K+'coordinates'); out.append(('poly',path,n,Polygon(co(o.text))))
                for pt in ch.iter(K+'Point'): out.append(('pt',path,n,Point(co(pt.find(K+'coordinates').text)[0])))
    walk(r,[]); return out
