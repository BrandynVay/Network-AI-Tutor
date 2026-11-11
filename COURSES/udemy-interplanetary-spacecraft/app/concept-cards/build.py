import sys,html
sys.path.insert(0,'.'); from entries import E; from count import lines
esc=html.escape
SC={1:"Falling & missing",2:"Three shelves",3:"The hula hoop",4:"Five free services",5:"The air bites back",6:"The fuel bill",7:"The free lunch"}
head=open('../pdf/glossary.html').read().split('</head>')[0]
css='''<style>
.nbwrap{display:flex;gap:14px;justify-content:center}
.nb{width:4.95in;height:7.38in;border:3px solid #111;border-radius:10px;background:#fff;position:relative;padding:0 12px 0 12px;overflow:hidden}
.nbh{height:.5in;display:flex;justify-content:space-between;align-items:flex-end;padding-bottom:5px;font-size:11px;font-weight:900;letter-spacing:.5px;color:#333;border-bottom:2px solid #111}
.nbh span.pg{border:2px solid #111;border-radius:6px;padding:1px 8px;font-size:13px}
.ln{height:.3in;border-bottom:1px solid #c9d1de;display:flex;align-items:flex-end;padding-bottom:3px;font-size:15px;white-space:nowrap;color:#222}
  .ln .s{flex:none;width:50px;font-weight:900;font-size:13.5px;color:#000}
.ln.n{font-weight:900;font-size:14.5px;color:#000}
.ln.n .nmbox{border:2px solid #111;border-radius:5px;padding:0 5px;margin-left:-3px;background:#eee}
.ln.n2{font-weight:700}
.ln .num{flex:none;width:16px;font-size:8px;color:#9aa3b2;margin-left:-10px}
.ln.gap{background:repeating-linear-gradient(90deg,#999 0 6px,transparent 6px 12px) center/100% 1.5px no-repeat}
.cap{font-size:10.5px;color:#444;text-align:center;margin-top:5px}
.key{border:3px solid #111;border-radius:12px;padding:10px 14px;background:#fff;font-size:12.5px;line-height:1.5}
.key h3{margin:0 0 4px;font-size:15px}
.kt{border-collapse:collapse;width:100%;font-size:12px}
.kt td,.kt th{border:1.5px solid #111;padding:3px 7px;text-align:left;vertical-align:top}
.kt th{background:#111;color:#fff}
.strip{display:flex;border:3px solid #111;border-radius:10px;overflow:hidden;font-size:10.5px;font-weight:700;text-align:center}
.strip div{padding:8px 4px;border-right:2px solid #111;background:#fff}
.strip div:last-child{border-right:0}
.strip .hl2{background:#ddd}
.ix{columns:4;font-size:10px;line-height:1.45}
</style>'''
def page_html(n):
    a,b=lines(E[2*n]),lines(E[2*n+1]); spare=22-len(a)-len(b)
    rows=[]; i=0
    def emit(ls,sc):
        nonlocal i
        first=True
        for k,t in ls:
            i+=1
            if k=="N":
                nm=t; rest=""
                rows.append(f'<div class="ln n"><span class="num">{i}</span><span class="nmbox">{esc(t)}</span><span style="margin-left:auto;font-size:10px;font-weight:700;color:#555">scene {sc}</span></div>')
            elif k=="N2":
                rows.append(f'<div class="ln n2"><span class="num">{i}</span><span class="s"></span>{esc(t)}</div>')
            else:
                rows.append(f'<div class="ln"><span class="num">{i}</span><span class="s">{esc(k)}</span>{esc(t)}</div>')
    emit(a,E[2*n][0])
    if spare>=1:
        i+=1; rows.append(f'<div class="ln gap"><span class="num">{i}</span></div>')
    emit(b,E[2*n+1][0])
    while i<22:
        i+=1; rows.append(f'<div class="ln"><span class="num">{i}</span></div>')
    scs=sorted({E[2*n][0],E[2*n+1][0]})
    return f'<div class="nb"><div class="nbh"><span>WORD BANK · CONCEPT CARDS · {" + ".join("scene %d"%s for s in scs)}</span><span class="pg">C{n+1}</span></div>{"".join(rows)}</div>',len(a)+len(b)
tot=sum(len(lines(e)) for e in E)
intro=f'''<div class="page"><div class="top"><span class="badge">SPACE X · COPY INTO NOTEBOOK</span><h1>Concept cards for the <span>word bank</span> · S1–S3 (v1)</h1></div>
<div class="sub">32 core terms · two cards per notebook page · <b>16 pages (8 spreads), numbered C1–C16</b> · {tot} handwritten lines. Every page that follows is one notebook spread at full size: copy it line for line.</div>
<div class="two">
<div class="key"><h3>The five symbols (write this key at the top of C1's facing page or on your abbreviation page)</h3>
<table class="kt"><tr><th style="width:60px">Write</th><th>Means</th><th>What that line does for you</th></tr>
<tr><td><b>[NAME]</b> = …</td><td>official name = also called</td><td>Box the name in pencil. Say it out loud before you write the rest.</td></tr>
<tr><td><b>=</b></td><td>meaning</td><td>The dictionary line. What the word points at.</td></tr>
<tr><td><b>WHY</b></td><td>why it exists</td><td>The problem it solves. This is the line that makes the word stick.</td></tr>
<tr><td><b>#</b></td><td>real numbers</td><td>One example you can check. No number = you can't test yourself.</td></tr>
<tr><td><b>≠</b></td><td>don't confuse with</td><td>The look-alike, and in brackets how to tell them apart.</td></tr>
<tr><td><b>→</b></td><td>connects to</td><td>Formulas and terms it plugs into. Your next sentence in a conversation.</td></tr></table>
<p style="margin:8px 0 0"><b>Pencil only.</b> Nothing here needs color. The tiny gray numbers 1–22 down the left edge are your ruled lines; don't copy them. The dashed line is one skipped line between the two cards.</p></div>
<div class="key"><h3>How to copy so it actually sticks</h3>
<ol style="margin:0;padding-left:18px">
<li><b>One spread per sitting</b> (4 cards, about 40 lines, 20–25 minutes). Eight sittings. Don't do all 16 pages in one go; by page 5 you would be copying shapes, not ideas.</li>
<li><b>Order:</b> C3–C7 first (scene 3, the orbital elements: your biggest gap and the heart of the 7-minute talk). Then C11–C15 (fuel bill + flybys). Then C1–C2, C8–C10, C16.</li>
<li><b>Per card:</b> read the whole card. Say the WHY line out loud. Then write the card. Writing first and reading later is the wrong way round.</li>
<li><b>Close the loop:</b> when a spread is done, cover everything except the four boxed names and say each WHY from memory. Miss one twice → it becomes a question-bank card.</li>
<li><b>Link the two banks:</b> in the one-line word bank, write "→ C5" (the card's page) at the end of that term's line. Index of all 32 is on the last page of this PDF.</li>
</ol></div></div>
<div class="callout" style="margin-top:10px">Where the 16 pages go, and what it costs the rest of the notebook, is on the last page. Short version: they start <b>44 pages from the end</b>, right in front of the talk cards. Nothing you have already written moves.</div>
</div>'''
sheets=[]
for s in range(8):
    L,nl=page_html(2*s); R,nr=page_html(2*s+1)
    sheets.append(f'<div class="page" style="padding:0.3in 0.4in"><div class="top" style="margin-bottom:4px"><span class="badge">SPREAD {s+1} OF 8</span><h1 style="font-size:17px">Left page <span>C{2*s+1}</span> · right page <span>C{2*s+2}</span></h1><span style="margin-left:auto;font-size:10.5px;color:#555">{nl} lines · {nr} lines of 22</span></div><div class="nbwrap">{L}{R}</div></div>')
idx=sorted([(e[1],i//2+1) for i,e in enumerate(E)])
ix="".join(f'<div>{esc(n)} <b>C{c}</b></div>' for n,c in idx)
last=f'''<div class="page"><div class="top"><span class="badge">NOTEBOOK MAP · v3</span><h1>Where the concept cards live, and <span>what it costs</span></h1></div>
<div class="sub">Count from the LAST page so the rule works whatever your notebook's real page count is. The page numbers in brackets assume ~95 pages; check your last page number once and adjust.</div>
<div class="strip">
<div style="flex:5">p1–5<br>index · equations · abbrev key</div>
<div style="flex:46">p6 → p51<br>LECTURE SPREADS + section maps<br><span style="font-weight:400">S1–S3 already used ≈ p6–24 · room left for Sections 4, 5, 6</span></div>
<div style="flex:16" class="hl2">16 pages [p52–67]<br>CONCEPT CARDS C1–C16<br><span style="font-weight:400">NEW · tab at 44 from end</span></div>
<div style="flex:2">2<br>talk cards</div>
<div style="flex:12">12 pages<br>ONE-LINE WORD BANK<br><span style="font-weight:400">unchanged</span></div>
<div style="flex:14">last 14<br>QUESTION BANK<br><span style="font-weight:400">unchanged</span></div>
</div>
<div class="two" style="margin-top:10px">
<div class="key"><h3>The page count, honestly</h3>
<table class="kt"><tr><th>Block</th><th>Pages</th><th>Why</th></tr>
<tr><td>Concept cards, S1–S3</td><td><b>16</b></td><td>32 terms × 9–11 lines = {tot} lines. Two cards fit a 22-line page; three don't.</td></tr>
<tr><td>Concept cards, S4–S7 (estimate)</td><td><b>~14</b></td><td>About 25–30 more core terms at the same rate (propulsion, comms, attitude, power).</td></tr>
<tr><td>One-line word bank, whole course</td><td>12 (have) · ~15 (need)</td><td>S1–S3 is 161 lines ≈ 7½ pages; four more sections won't fit in the 4½ left.</td></tr>
<tr><td><b>Word bank total by end of course</b></td><td><b>~45</b></td><td>The old map gave it 12.</td></tr></table>
<p style="margin:8px 0 0"><b>What that means:</b> one ~95-page notebook cannot hold 25 lectures, a 45-page word bank and a 14-page question bank. That is ~120 pages of content. The old 2-page buffer is gone and the lecture block now ends at p51, which is the end of <b>Section 6</b>.</p></div>
<div class="key"><h3>The plan</h3>
<ol style="margin:0;padding-left:18px">
<li><b>Now:</b> count 44 pages back from the last page, put a sticky tab there, label the next 16 pages C1–C16 in pencil (top outer corner). Copy the eight spreads into them.</li>
<li><b>Nothing else moves.</b> Talk cards, the 12 one-line pages and the question bank stay exactly where they are. Old tabs at 30 / 28 / 14 from the end stay.</li>
<li><b>Before Section 7:</b> get a second small notebook. It takes Section 7's lecture spreads, the S4–S7 concept cards (C17 onward) and the one-line overflow. Number its concept pages on from C17 so the "→ C__" pointers keep working.</li>
<li><b>If you would rather keep every lecture in this one book:</b> buy the second notebook now and put C1–C16 in it instead. Same cards, same numbering. Then this notebook's map stays exactly as v2.</li>
</ol>
<p style="margin:8px 0 0"><b>My recommendation is 1–3:</b> you are reviewing Sections 1–3 this week and need the cards next to those notes today.</p></div></div>
<div class="key" style="margin-top:8px;padding:7px 14px"><h3 style="font-size:13px">Index: which page each card is on (add "→ C#" to that term's line in the one-line word bank)</h3><div class="ix">{ix}</div></div>
</div>'''
open('concept-cards.html','w').write(head+css+'</head><body>'+intro+"".join(sheets)+last+'</body></html>')
print("ok",tot)
