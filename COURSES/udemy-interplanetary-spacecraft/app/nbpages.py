"""Notebook page images for the app's Notebook tab.

Usage (from this folder):
  mkdir -p png nb && pdftoppm -r 180 -png ../Space-X-Notebook-COMPLETE-S1-S7-v1.pdf png/p && python3 nbpages.py nb
then `python3 mkdist.py` to rebuild dist/. If the notebook page count or section starts change,
update NB.total and NB.toc in space-x-study.html to match the PDF bookmarks.
"""
import glob,os,sys
from multiprocessing import Pool
from PIL import Image
OUT=sys.argv[1]
def conv(f):
    n=int(os.path.basename(f)[2:-4])
    im=Image.open(f).convert('RGB')
    small=im.resize((330,255))
    ncol=len(small.getcolors(maxcolors=100000))
    o=os.path.join(OUT,'p%03d.webp'%n)
    if ncol>9000:   # photo-like page: keep true colour
        im.save(o,'WEBP',quality=72,method=6); kind='lossy'
    else:
        im.quantize(64,method=Image.Quantize.MEDIANCUT,dither=Image.Dither.NONE).convert('RGB').save(o,'WEBP',lossless=True,method=6); kind='pal'
    return n,kind,ncol,os.path.getsize(o)
if __name__=='__main__':
    fs=sorted(glob.glob('png/p-*.png'))
    with Pool(4) as p: res=sorted(p.map(conv,fs))
    tot=sum(r[3] for r in res)
    print(len(res),'pages',tot/1e6,'MB','max',max(r[3] for r in res))
    print('lossy pages:',[(r[0],r[2],r[3]) for r in res if r[1]=='lossy'])
    print('colour counts top:',sorted([(r[2],r[0]) for r in res])[-12:])
