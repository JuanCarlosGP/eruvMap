import math,os,time,requests,numpy as np,cv2
from PIL import Image
def tile(z,lon,lat):
    n=2**z; return (lon+180)/360*n,(1-math.log(math.tan(math.radians(lat))+1/math.cos(math.radians(lat)))/math.pi)/2*n
def untile(z,x,y):
    n=2**z; return x/n*360-180, math.degrees(math.atan(math.sinh(math.pi*(1-2*y/n))))
def mosaic(z,lat,lon,rad):
    cx,cy=tile(z,lon,lat); X0,X1,Y0,Y1=int(cx)-rad,int(cx)+rad,int(cy)-rad,int(cy)+rad
    img=Image.new('RGB',((X1-X0+1)*256,(Y1-Y0+1)*256)); os.makedirs('tiles',exist_ok=True)
    for x in range(X0,X1+1):
        for y in range(Y0,Y1+1):
            p=f'tiles/{z}_{x}_{y}.png'
            if not os.path.exists(p):
                r=requests.get(f'https://tile.openstreetmap.org/{z}/{x}/{y}.png',headers={'User-Agent':'eruvmap-preview/1.0 (derived-data QA)'},timeout=20)
                open(p,'wb').write(r.content); time.sleep(.15)
            img.paste(Image.open(p).convert('RGB'),((x-X0)*256,(y-Y0)*256))
    return np.array(img),X0,Y0
def match(gray,mask,z,lat,lon,rad,scales):
    M,X0,Y0=mosaic(z,lat,lon,rad); Mg=cv2.cvtColor(M,cv2.COLOR_RGB2GRAY)
    best=None
    for s in scales:
        g=cv2.resize(gray,None,fx=s,fy=s,interpolation=cv2.INTER_AREA); m=cv2.resize(mask,None,fx=s,fy=s,interpolation=cv2.INTER_NEAREST)
        if g.shape[0]>=Mg.shape[0] or g.shape[1]>=Mg.shape[1]: continue
        r=cv2.matchTemplate(Mg,g,cv2.TM_CCOEFF_NORMED,mask=m)
        r[~np.isfinite(r)]=0
        _,mx,_,loc=cv2.minMaxLoc(r)
        if best is None or mx>best[0]: best=(mx,s,loc)
    return best,(M,X0,Y0)
def px2ll(pt,s,loc,z,X0,Y0):
    # pt: (col,row) in original image
    tx=X0+(loc[0]+pt[0]*s)/256; ty=Y0+(loc[1]+pt[1]*s)/256
    return untile(z,tx,ty)
