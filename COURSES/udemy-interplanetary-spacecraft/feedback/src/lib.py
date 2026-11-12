import html,textwrap
esc=html.escape
HEAD=open('../pdf/s3-om3.html').read().split('</head>')[0]+'''<style>
.gl2{columns:2;column-gap:22px;font-size:10.6px;line-height:1.38}
.gl2 div{break-inside:avoid;margin-bottom:4px}
.gl2 i{color:#555}
.mech{border-collapse:collapse;width:100%;font-size:10.4px}
.mech th,.mech td{border:1.5px solid #111;padding:3px 6px;text-align:left;vertical-align:top}
.mech th{background:#0b1437;color:#fff}
.eli{background:#fff8d6;border:3px solid #111;border-radius:14px;padding:9px 15px;margin-bottom:10px;font-size:12.2px;line-height:1.48}
.names{font-size:11px;line-height:1.45;margin:0;padding-left:16px}
.nb{width:4.3in;height:6.4in;border:3px solid #111;border-radius:10px;background:#fff;position:relative;padding:0 10px;overflow:hidden;flex:none}
.nbh{height:.42in;display:flex;justify-content:space-between;align-items:flex-end;padding-bottom:4px;font-size:9.5px;font-weight:900;letter-spacing:.5px;color:#333;border-bottom:2px solid #111}
.nbh span.pg{border:2px solid #111;border-radius:6px;padding:1px 7px;font-size:12px}
.ln{height:.262in;border-bottom:1px solid #c9d1de;display:flex;align-items:flex-end;padding-bottom:2px;font-size:12.6px;white-space:nowrap;color:#222}
.ln .s{flex:none;width:42px;font-weight:900;font-size:11.5px;color:#000}
.ln.n{font-weight:900;font-size:12.4px;color:#000}
.ln.n .nmbox{border:2px solid #111;border-radius:5px;padding:0 5px;margin-left:-3px;background:#eee}
.ln.n2{font-weight:700}
.ln .num{flex:none;width:14px;font-size:7.5px;color:#9aa3b2;margin-left:-8px}
.ln.gap{background:repeating-linear-gradient(90deg,#999 0 6px,transparent 6px 12px) center/100% 1.5px no-repeat}
.route{font-size:11px;line-height:1.45}
.route h3{margin:0 0 3px;font-size:13px}
.route .copy{font-family:"DejaVu Sans Mono",monospace;font-size:10.2px;background:#f4f4f4;border:1.5px dashed #777;border-radius:6px;padding:5px 8px;margin:3px 0 8px;white-space:pre-wrap;line-height:1.5}
</style>'''
W=37
def lines(e):
    name,also,m,why,num,nt,con=e
    head=name+("  = "+also if also!="—" else "")
    out=[("N" if i==0 else "N2",l) for i,l in enumerate(textwrap.wrap(head,W+4))]
    for k,t in (("=",m),("WHY",why),("#",num),("≠",nt),("→",con)):
        for i,l in enumerate(textwrap.wrap(t,W)): out.append((k if i==0 else "",l))
    return out
def cardpage(a,b,label,scene):
    A=lines(a); B=lines(b) if b else []
    assert len(A)+len(B)<=22,(label,len(A),len(B))
    rows=[]; i=0
    def emit(ls):
        nonlocal i
        for k,t in ls:
            i+=1
            if k=="N": rows.append(f'<div class="ln n"><span class="num">{i}</span><span class="nmbox">{esc(t)}</span></div>')
            elif k=="N2": rows.append(f'<div class="ln n2"><span class="num">{i}</span><span class="s"></span>{esc(t)}</div>')
            else: rows.append(f'<div class="ln"><span class="num">{i}</span><span class="s">{esc(k)}</span>{esc(t)}</div>')
    emit(A)
    if B and len(A)+len(B)<22:
        i+=1; rows.append(f'<div class="ln gap"><span class="num">{i}</span></div>')
    emit(B)
    while i<22:
        i+=1; rows.append(f'<div class="ln"><span class="num">{i}</span></div>')
    return f'<div class="nb"><div class="nbh"><span>WORD BANK · CONCEPT CARDS · {scene}</span><span class="pg">{label}</span></div>{"".join(rows)}</div>', len(A), len(B)
def top(badge,h1,sub): return f'<div class="top"><div class="badge">{badge}</div><h1>{h1}</h1></div><div class="sub">{sub}</div>'
def spread(badge,h1,hdr,svg,key,takes,cues,notes):
    return f'''<div class="page">{top(badge,h1,"Left = your left notebook page. Right = your right page. Copy the drawing in pencil first, then the cues and notes. The summary box stays empty until the video and this PDF are closed.")}
<div style="display:flex; gap:18px; justify-content:center">
  <div class="bg o"><span class="tag">🖍 LEFT PAGE · DRAW</span>
    <div class="hdr"><span>{hdr}</span><span>date · pg __</span></div>
    {svg}<div class="bz" style="margin-top:4px; font-size:10.5px"><b>✏️ PENCIL KEY</b> · {key}</div>
    <div class="bz"><b>⭐ 3 TAKEAWAYS</b> <span class="lb">3 lines</span><br><span class="ink">{"<br>".join(takes)}</span></div>
    <div class="bz" style="border-color:var(--green); background:#f2fff7"><b>🧠 SUMMARY · video + PDF closed</b> <span class="lb">3 lines</span><br>
      <span class="pencil" style="font-size:12px">1. ______________________________________<br>2. ______________________________________<br>3. ______________________________________</span></div>
  </div>
  <div class="bg b"><span class="tag">❓ RIGHT PAGE · CORNELL</span>
    <div class="hdr"><span>CUES (questions)</span><span>NOTES (keywords)</span></div>
    <div style="display:flex; height:6.5in">
      <div style="width:37%; border-right:3px solid var(--blue); padding-right:8px" class="ink">{"".join(f'<p class="q">{c}</p>' for c in cues)}</div>
      <div style="flex:1; padding-left:10px" class="ink">{"".join(f'<div style="margin-bottom:5px">{n}</div>' for n in notes)}</div>
    </div>
  </div>
</div></div>'''
def write(name,pages):
    open(name,'w').write(HEAD+'</head><body>'+"".join(pages)+'</body></html>')
