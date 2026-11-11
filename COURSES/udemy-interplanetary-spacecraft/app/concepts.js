// Build Word-Bank CONCEPT sheet from the app's TERMS + ENRICH data.
const fs=require('fs'); const js=fs.readFileSync('app/check.js','utf8');
const head=js.slice(0, js.indexOf("// ---------------------------------------------------------------- STATE"));
const {TERMS,ENRICH,SCENES}=new Function(head+"; return {TERMS,ENRICH,SCENES}")();
const esc=s=>String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;");
const styleHead=fs.readFileSync('pdf/glossary.html','utf8').split('</head>')[0];
const sceneName=id=>{const s=SCENES.find(x=>x.id===id); return `Scene ${s.n} · ${s.name}`;};
const order=["fall","shelf","hoop","vac","air","fuel","flyby"];
const items=TERMS.filter(t=>ENRICH[t[0]]).sort((a,b)=>order.indexOf(a[3])-order.indexOf(b[3]));
const card=t=>{const e=ENRICH[t[0]]; const s=SCENES.find(x=>x.id===t[3]); return `<div class="ent" style="border-color:${s.color}">
<div class="nm"><b>${esc(t[0])}</b><span class="sc" style="background:${s.color}">${s.n}</span></div>
${t[1]&&t[1]!=="—"?`<div class="al">Also called: ${esc(t[1])}</div>`:""}
<div class="row"><span class="lb">Meaning</span><span>${esc(t[2])}</span></div>
<div class="row"><span class="lb">Concept</span><span>${esc(e.c)}</span></div>
<div class="row"><span class="lb">Numbers</span><span>${esc(e.e)}</span></div>
<div class="row"><span class="lb">Not this</span><span>${esc(e.x)}</span></div>
<div class="row"><span class="lb">Connects</span><span>${esc(e.l)}</span></div></div>`;};
// 4 entries per page, 2x2
let pages=[]; for(let i=0;i<items.length;i+=4) pages.push(items.slice(i,i+4));
const intro=`<div class="page"><div class="top"><span class="badge">SPACE X · WORD BANK</span><h1>Word bank, <span>concept level</span> — S1–S3 (v4)</h1></div>
<div class="sub">32 core terms. Each one answers five questions, in this order, every time.</div>
<div class="card" style="font-size:13px;line-height:1.5"><h3>How to read an entry (and how to write it in your notebook)</h3>
<ul class="r" style="font-size:13px">
<li><b>Name</b> in bold first, then <b>Also called</b>. Say the official name out loud before anything else; that's the rule.</li>
<li><b>Meaning</b> = the one-line definition you'd put in a dictionary. This is what you've been copying so far. It is not enough on its own.</li>
<li><b>Concept</b> = <i>why the thing exists</i>: what problem it solves, what would go wrong without it. This is the part that makes the word stick, because now it has a job.</li>
<li><b>Numbers</b> = one real example with a real value. A term with no number attached is a term you can't check yourself.</li>
<li><b>Not this</b> = the thing people mix it up with, and the one-line test that separates them.</li>
<li><b>Connects</b> = which formulas or other terms it plugs into. This is how you walk from one idea to the next in a conversation instead of stalling.</li>
</ul>
<div class="callout">In the notebook: the back word-bank pages only have room for Name · Also called · Meaning (one line). Put <b>Concept</b> and <b>Numbers</b> in the margin of the lecture page the term came from, or say them out loud when you review. Don't copy all five lines for all 32 terms; the app has them.</div>
<div class="two" style="margin-top:12px"><div class="mini"><b>Order of the entries:</b> by scene, in the order the app shows them (1 Falling &amp; missing → 7 The free lunch). The number badge is the scene.</div><div class="mini"><b>Test yourself:</b> cover everything but the name. Say the concept line. If you can't say <i>why it exists</i>, you don't own the word yet, even if you can define it.</div></div>
</div></div>`;
const body=pages.map((pg,n)=>`<div class="page"><div class="top"><span class="badge">WORD BANK · ${n+1}/${pages.length}</span><h1>Concept-level <span>word bank</span></h1></div><div class="g2">${pg.map(card).join("")}</div></div>`).join("");
const extra=`<style>
.g2{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:10px;height:7.25in}
.ent{border:3px solid #111;border-radius:12px;padding:8px 11px;font-size:10.6px;line-height:1.35;background:var(--paper);overflow:hidden}
.nm{display:flex;justify-content:space-between;align-items:center;font-size:14px;margin-bottom:1px}
.sc{color:#fff;font-weight:900;border-radius:999px;padding:1px 8px;font-size:10px}
.al{color:#555;font-size:10px;margin-bottom:4px}
.row{display:flex;gap:7px;margin:3px 0}
.lb{flex:none;width:58px;font-weight:900;font-size:9.5px;letter-spacing:.5px;text-transform:uppercase;color:#333;padding-top:1px}
</style>`;
fs.writeFileSync('pdf/wordbank-concepts.html', styleHead+extra+'</head><body>'+intro+body+'</body></html>');
console.log(items.length,'entries',pages.length,'pages');
