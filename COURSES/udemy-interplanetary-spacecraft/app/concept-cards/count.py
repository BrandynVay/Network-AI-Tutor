import textwrap,sys
sys.path.insert(0,'.'); from entries import E
W=37
def lines(e):
    sc,name,also,m,why,num,nt,con=e
    head=name+("  = "+also if also!="—" else "")
    out=[("N" if i==0 else "N2",l) for i,l in enumerate(textwrap.wrap(head,W+4))]
    for k,t in (("=",m),("WHY",why),("#",num),("≠",nt),("→",con)):
        for i,l in enumerate(textwrap.wrap(t,W)): out.append((k if i==0 else "",l))
    return out
if __name__=="__main__":
    tot=0
    for i in range(0,len(E),2):
        a,b=lines(E[i]),lines(E[i+1]); tot+=len(a)+len(b)
        flag="  <-- OVER" if len(a)+len(b)>22 else ""
        print(f"C{i//2+1:>2}: {E[i][1][:28]:28} {len(a):>2} + {E[i+1][1][:28]:28} {len(b):>2} = {len(a)+len(b)}{flag}")
    print("total",tot)
