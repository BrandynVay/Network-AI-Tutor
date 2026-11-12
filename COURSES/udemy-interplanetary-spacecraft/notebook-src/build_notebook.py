"""Build the single combined notebook PDF from every current course PDF.

Run from anywhere:  python3 build_notebook.py [version]
Needs: pypdf, node + playwright (for the generated pages), poppler (pdfinfo not required).
Order mirrors the paper notebook: front matter, lecture pages in course order with a
section divider before each section, then the back-of-notebook reference material.
"""
import html, json, os, subprocess, sys, tempfile
from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(HERE)
VER = sys.argv[1] if len(sys.argv) > 1 else "v1"
OUT = os.path.join(C, "Space-X-Notebook-COMPLETE-S1-S7-%s.pdf" % VER)
TMP = tempfile.mkdtemp(prefix="nb-")
esc = html.escape
F = lambda p: os.path.join(C, p)

SECTIONS = [
 dict(n=1, name="Mission design", color="#ff6b1a", prog="s1", scenes="1, 2",
      say="An orbit is falling and missing. Low is fast and sharp; one exact height hangs still over the equator.",
      num="LEO 400 km: 92 min, 7.7 km/s · GEO 35,786 km above the ground",
      dont='"36,000 km from the centre" (that figure is the altitude; from the centre it is 42,164 km)',
      lectures=[("Satellite types and orbits", "feedback/S1-satellite-types-and-orbits.pdf"),
                ("Types of interplanetary spacecraft", "feedback/S1-L3-types-of-interplanetary-spacecraft.pdf")]),
 dict(n=2, name="Space environment", color="#19b36b", prog="s2", scenes="4, 5",
      say="The air did five jobs for you: sunscreen, pressure, damper, fan, ground wire. Space does none.",
      num="atomic oxygen is the main gas from 200 to 600 km",
      dont='"atomic oxygen appears at 320–340 km" (it dominates from about 200 km)',
      lectures=[("Space vacuum", "feedback/S2-L4-space-vacuum.pdf"),
                ("Earth's atmosphere", "feedback/S2-L5-earth-atmosphere.pdf")]),
 dict(n=3, name="Orbital mechanics", color="#7b3fe4", prog="s3", scenes="3, 6, 7",
      say="Six numbers describe any orbit. The lazy half-ellipse is the cheapest way to go; a flyby steals speed from a planet.",
      num="Earth to Mars: 259 days, a window every 26 months",
      dont='"Lambert\'s problem takes the Δv and gives the time" (it takes two places and a time, and gives the orbit and its Δv)',
      lectures=[("Orbit definition and the six parameters", "feedback/S3-L1-orbital-mechanics-v3.pdf"),
                ("Earth orbits and constellations", "feedback/S3-L2-earth-orbits-v1.pdf"),
                ("Interplanetary transfers and flybys", "feedback/S3-L3-interplanetary-transfers-and-flybys-v2.pdf")]),
 dict(n=4, name="Space propulsion", color="#0e8f9c", prog="s4", scenes="8, 9, 10",
      say="Every engine throws mass backward. Chemical pushes hard and is thirsty; electric is gentle and efficient; nuclear never flew.",
      num="F = ṁ × vₑ · Isp: chemical 450 s, electric 3,000 s, nuclear 900 s",
      dont='"nuclear rockets are efficient because they run hotter" (they run cooler; the exhaust is lighter)',
      lectures=[("Propulsion: definitions and types", "feedback/S4-L1-space-propulsion-definitions-and-types-v2.pdf"),
                ("Chemical engines", "feedback/S4-L2-chemical-engines-v1.pdf"),
                ("Electric propulsion and ion thrusters", "feedback/S4-L3-electric-propulsion-ion-thrusters-v1.pdf"),
                ("Nuclear thermal rockets", "feedback/S4-L4-nuclear-thermal-rockets-v1.pdf")]),
 dict(n=5, name="Communications", color="#c0392b", prog="s5", scenes="11, 12, 13",
      say="Write the message on a radio wave, aim it with a dish, send it through the radio window, and land louder than the noise.",
      num="c = λ × f · Cassini: 20 W sent, 10⁻¹⁶ W received",
      dont='"a dish adds power" (it aims it) · "k is a relation for wavelength" (it is the Boltzmann constant)',
      lectures=[("Antennas", "feedback/S5-L1-communications-antennas-v1.pdf"),
                ("Atmosphere and frequency bands", "feedback/S5-L2-atmosphere-and-frequency-bands-v1.pdf"),
                ("Satellite and spacecraft links", "feedback/S5-L3-satellite-and-spacecraft-links-v1.pdf")]),
 dict(n=6, name="Attitude determination and control", color="#283593", prog="s6", scenes="14, 15, 16",
      say="Sense, compare, twist, forever. Gyros drift and stars fix them. Wheels swap spin; jets and magnets remove it.",
      num="star tracker 0.001° · Hubble holds 0.007 arcseconds",
      dont='"Explorer 1 failed" (it found the radiation belts) · "moment of inertia = mass in a direction" (distance from the axis)',
      lectures=[("Attitude: definitions and physics", "feedback/S6-L1-attitude-definitions-and-physics-v1.pdf"),
                ("Sensors", "feedback/S6-L2-attitude-sensors-v1.pdf"),
                ("Actuators", "feedback/S6-L3-attitude-actuators-v1.pdf")]),
 dict(n=7, name="Space power systems", color="#ef6c00", prog="s7", scenes="17, 18, 19",
      say="A sunlight sandwich near the Sun, a bucket for the dark, and a warm rock where the Sun doesn't reach.",
      num="1,361 W/m² at Earth · cells 30% · plutonium-238 halves in 87.7 years",
      dont='"three layers triple the efficiency" (20% becomes 30%) · "RTGs last 500 years" (decades)',
      lectures=[("Solar arrays", "feedback/S7-L1-solar-arrays-v1.pdf"),
                ("Batteries", "feedback/S7-L2-batteries-v1.pdf"),
                ("Radioisotope generators (RTG)", "feedback/S7-L3-radioisotope-generators-RTG-v1.pdf")]),
]
BACK = [
 ("Teach-it-back kit, Sections 1–3 (scenes, talks, quiz)", "review/Teach-It-Back-Kit-S1-S3-v3.pdf"),
 ("Concept cards in notebook layout, C1–C16", "Word-Bank-CONCEPT-CARDS-notebook-S1-S3-v1.pdf"),
 ("Word bank, concept level, Sections 1–3", "Word-Bank-CONCEPTS-S1-S3-v4.pdf"),
 ("Glossary, every word, Sections 1–3", "Glossary-COMPLETE-S1-S3-v2.pdf"),
 ("One-line word bank, Sections 1–3", "Word-Bank-COMPLETE-S1-S3-v1.pdf"),
 ("Copy-into-notes sheet (equations, map sentences), Sections 1–3", "Copy-Into-Notes-Engineer-S1-S3-v1.pdf"),
 ("Who's Who: every mission, engine and person named", "Whos-Who-names-and-missions-v7.pdf"),
 ("Map of the paper notebook", "Notebook-Map-v2.pdf"),
]
REVIEW = ("The whole course on one page + plan", "review/Whole-Course-Review-S1-S7-v1.pdf")

CALL = [
 (1, "Why doesn't a satellite fall down?", "It is falling. It also moves sideways at 7.7 km/s, so the ground curves away as fast as it drops: 4.3 m every second. Gravity is the string; no engine is needed."),
 (1, "Why is geostationary exactly 35,786 km, and why over the equator?", "It is the one height where a lap takes one Earth rotation, 23 h 56 min. Only over the equator does it stay above one spot; tilted, it draws a figure-8."),
 (1, "Flyby, orbiter, lander: what changes?", "Each step needs more slowing down, so more fuel. A flyby needs no braking burn, an orbiter must brake into orbit, a lander must also get down."),
 (2, "The thermosphere is 1,000 °C. Why doesn't the ISS cook?", "Temperature is how fast the molecules move; heat is how much energy they deliver. The air is so thin that almost nothing hits you."),
 (2, "What is actually dangerous about a vacuum?", "The air did five jobs: blocked UV, held pressure, damped vibration, carried heat away, bled off static. In space you build all five yourself."),
 (2, "What is atomic oxygen?", "Single O atoms made when UV splits O₂: the main gas at 200–600 km. A satellite rams them at 7.5 km/s and they eat plastics such as Kapton."),
 (3, "What are the six orbital elements?", "The Classical (Keplerian) Orbital Elements: a size, e squash, i tilt, Ω swivel, ω where perigee points, ν where you are now. Five fix the orbit, one moves."),
 (3, "Why can't we leave for Mars any time?", "The cheap route is a Hohmann half-ellipse, 259 days. Mars must be about 44° ahead at launch so it arrives when you do. That lines up every 26 months."),
 (3, "Where does a gravity assist's speed come from?", "From the planet. In the planet's view you leave as fast as you came, only bent. In the Sun's view you picked up some of its orbital motion. It slows by an unmeasurable amount."),
 (4, "No air in space: what does a rocket push on?", "Its own exhaust. Newton's third law. Thrust = mass thrown per second × exhaust speed."),
 (4, "What is specific impulse?", "Exhaust speed ÷ 9.81, in seconds: the engine's mileage. Chemical about 450 s at best, ion about 3,000 s."),
 (4, "Why not ion engines for everything?", "Thrust is limited by electric power: 0.09 N from 2.3 kW. Perfect for years of cruising, useless for launch, landing or a capture burn."),
 (5, "How does 20 W reach Earth from Saturn?", "A 4 m dish squeezes it into a 0.6° beam, a gain of about 50,000, and a 70 m dish listens. The dish adds no power. It aims it."),
 (5, "Why radio and not something else?", "The air is a wall with two windows: visible light and radio (about 1 cm to 10 m). UV and X-rays are absorbed; long radio bounces off the ionosphere."),
 (5, "Why is deep-space data so slow?", "The signal spreads: twice as far, a quarter the power. What counts is signal ÷ noise at the receiver, and that sets bits per second. Voyager: 160."),
 (6, "How does it know where it is pointing?", "Gyros feel turning but drift. Sun sensor, star tracker, horizon sensor and magnetometer each see one outside reference. One direction gives only two angles, so they are combined."),
 (6, "How does it turn with nothing to push on?", "Spin a reaction wheel one way and the craft turns the other: angular momentum is conserved. Wheels fill up (saturate); thrusters or magnetic torquers empty them."),
 (6, "Why did Explorer 1 tumble?", "A pencil spun about its long axis, its smallest moment of inertia. Flexing antennas leaked energy, so it ended up spinning about its largest: end over end."),
 (7, "How does a solar cell work?", "Two layers, n and p, with a built-in field at the junction. A photon frees an electron, the field pushes it to one side, it returns through the wire. Triple-junction cells reach about 30%."),
 (7, "What is depth of discharge?", "How much of the battery you drain each cycle. Shallow drains last far longer but need a bigger battery. Low orbit means about 16 cycles a day."),
 (7, "How is Voyager still powered? Is that a reactor?", "RTGs: plutonium-238 decays and makes heat; thermocouples turn hot-against-cold into electricity, about 6%. Not a reactor: no chain reaction."),
]
SLIPS = [
 ("Nuclear rockets are efficient because they run hotter", "They run cooler. The exhaust is light hydrogen."),
 ("Project Orion was NASA's nuclear thermal rocket, 1986", "A 1958–65 study of riding nuclear bombs. Not thermal, not NASA's."),
 ("Electric propulsion is new, from the 1980s", "First flown in 1964."),
 ("A directional antenna gives you more power", "It aims the same power into a beam."),
 ("A triple-junction cell triples the efficiency", "About 20% becomes about 30%."),
 ("Explorer 1 was a failure", "It tumbled, and still discovered the radiation belts."),
 ("RTGs last 500 years", "The heat halves every 87.7 years."),
 ("A low orbit takes two hours", "About 92 minutes: 16 a day."),
]

# ---------------------------------------------------------------- helpers
def npages(path):
    return len(PdfReader(F(path)).pages)

def programs():
    js = r'''const fs=require("fs");const h=fs.readFileSync(process.argv[2],"utf8");
const m=h.match(/<script>([\s\S]*)<\/script>/)[1];
const head=m.slice(0,m.indexOf("// ---------------------------------------------------------------- STATE"));
console.log(JSON.stringify(new Function(head+"; return PROGRAMS")()));'''
    p = os.path.join(TMP, "prog.js"); open(p, "w").write(js)
    return json.loads(subprocess.check_output(["node", p, F("app/space-x-study.html")]))

def to_pdf(html_path, pdf_path):
    subprocess.check_call(["node", os.path.join(HERE, "mk.js"), html_path, pdf_path])

HEAD = open(F("feedback/src/s3-om3.html")).read().split("</head>")[0] + '''<style>
.mech{border-collapse:collapse;width:100%}
.mech th,.mech td{border:1.5px solid #111;padding:4px 7px;text-align:left;vertical-align:top}
.mech th{background:#0b1437;color:#fff}
.toc{font-size:11.6px;line-height:1.5;columns:2;column-gap:28px}
.toc div{display:flex;justify-content:space-between;gap:10px;break-inside:avoid}
.toc .sec{font-weight:900;margin-top:5px;border-bottom:2px solid #111}
.toc .sub2{padding-left:14px}
.big{font-size:54px;font-weight:900;line-height:1.02;margin:0}
</style>'''
def top(badge, h1, sub):
    return '<div class="top"><div class="badge">%s</div><h1>%s</h1></div><div class="sub">%s</div>' % (badge, h1, sub)

# ---------------------------------------------------------------- layout (page numbers are 1-based)
PROG = programs()
plan = []   # (kind, title, source, pages, level, stamp)
plan.append(("gen:contents", "Contents", None, 1, 0, "Front"))
plan.append(("pdf", REVIEW[0], REVIEW[1], npages(REVIEW[1]), 0, "Front"))
plan.append(("gen:call", "Call sheet: what he will ask, what you say", None, 2, 0, "Front"))
for s in SECTIONS:
    st = "S%d · %s" % (s["n"], s["name"])
    plan.append(("gen:div%d" % s["n"], "Section %d · %s" % (s["n"], s["name"]), None, 1, 0, st))
    for t, f in s["lectures"]:
        plan.append(("pdf", t, f, npages(f), 1, st))
plan.append(("gen:back", "Back of the notebook", None, 1, 0, "Back"))
for t, f in BACK:
    plan.append(("pdf", t, f, npages(f), 1, "Back"))
start = {}; p = 1; rows = []
for i, (k, t, f, n, lvl, st) in enumerate(plan):
    start[i] = p; rows.append((i, k, t, f, n, lvl, st, p)); p += n
TOTAL = p - 1
def page_of(src):
    return next(r[7] for r in rows if r[3] == src)

# ---------------------------------------------------------------- generated pages
toc = ""
for i, k, t, f, n, lvl, st, pg in rows:
    cls = "sub2" if lvl else "sec"
    toc += '<div class="%s"><span>%s</span><span>%d</span></div>' % (cls, esc(t), pg)
contents = f'''<div class="page">{top("SPACE X · NOTEBOOK · " + VER, "The whole course, <span>in one notebook</span>", f"Everything from the course in one file, in the order of your paper notebook. {TOTAL} pages. The page number is in the top right corner of every page.")}
<div class="two"><div class="card" style="flex:1.7;padding:10px 16px"><h3>Contents</h3><div class="toc">{toc}</div></div>
<div style="flex:1"><div class="card" style="padding:10px 14px"><h3>How it is laid out</h3><ul class="r" style="font-size:11.6px;line-height:1.5">
<li><b>Front:</b> the whole course on one page, the plan, and the call sheet.</li>
<li><b>Middle:</b> the seven sections in course order. Each starts with a divider page: what to say, the cue card for that section's talk, and the page of every lecture.</li>
<li><b>Each lecture:</b> page 1 is the spread you copy (drawing left, cues and notes right). Then the teaching page ("Like you're 5", official names, how it works), then what the instructor got wrong, then every word.</li>
<li><b>Back:</b> the Sections 1–3 teach-back kit, concept cards, word banks, glossary and Who's Who.</li></ul></div>
<div class="callout" style="margin-top:10px;font-size:12px">Before the call, read only this: pages 2 to 5, then the seven divider pages. That is 12 pages.</div>
<div class="card" style="margin-top:10px;padding:10px 14px"><h3>What changed along the way</h3><div style="font-size:11px;line-height:1.5">Sections 4–5 lectures also have copy-into-notes and concept-card pages (C17–C31). Sections 6–7 were made during the deadline push and stop at the vocabulary page. Older versions of any page were left out.</div></div></div></div></div>'''

def qa_table(secs, fs):
    out = '<table class="mech" style="font-size:%spx;line-height:1.36"><tr><th style="width:34px">Sec</th><th style="width:31%%">He asks</th><th>You say</th></tr>' % fs
    for n, q, a in CALL:
        if n in secs:
            out += "<tr><td><b>%d</b></td><td><b>%s</b></td><td>%s</td></tr>" % (n, esc(q), esc(a))
    return out + "</table>"
slips = "".join("<tr><td>%s</td><td>%s</td></tr>" % (esc(a), esc(b)) for a, b in SLIPS)
call1 = f'''<div class="page">{top("SPACE X · CALL SHEET · 1 OF 2", "What he will ask, <span>and what you say</span>", "Your friend knows the course, so expect why and how questions. These are the three most likely per section, with an answer short enough to say in one breath.")}
<div class="two"><div style="flex:1"><div class="card" style="padding:9px 14px"><h3>How to answer anything</h3><ol style="margin:0;padding-left:18px;font-size:11.8px;line-height:1.5">
<li><b>Picture first.</b> Start with the one-line picture: "it's falling and missing", "it's a flashlight for radio".</li>
<li><b>Then the official name.</b> "That's the Seebeck effect." It shows you know the real term.</li>
<li><b>Then one number.</b> 7.7 km/s. 35,786 km. 30%. One is enough.</li>
<li><b>If you blank,</b> say what you do know and reason out loud, or sketch it. Reasoning counts for more than recall.</li>
<li><b>"I don't know that one"</b> is a fine answer. Guessing with confidence is not.</li></ol></div>
<div class="card" style="margin-top:9px;padding:9px 14px;border-color:var(--orange)"><h3>He learned from the same instructor</h3>
<div style="font-size:11px;line-height:1.45;margin-bottom:5px">So he may say these, because the course did. Don't argue. Say "the course says that, but I checked", and give the reason.</div>
<table class="mech" style="font-size:10.4px;line-height:1.3"><tr><th>The course says</th><th>What is true</th></tr>{slips}</table></div></div>
<div style="flex:1.45"><div class="card" style="padding:9px 14px"><h3>Sections 1 to 3</h3>{qa_table((1,2,3), "10.8")}</div></div></div></div>'''
call2 = f'''<div class="page">{top("SPACE X · CALL SHEET · 2 OF 2", "Sections 4 to 7: <span>the ones you have only copied</span>", "You rehearsed Sections 1–3 out loud. These four you have not. Say each answer aloud once before the call, with this page covered.")}
<div class="two"><div class="card" style="padding:9px 14px"><h3>Propulsion and communications</h3>{qa_table((4,5), "11")}</div>
<div class="card" style="padding:9px 14px"><h3>Attitude control and power</h3>{qa_table((6,7), "11")}</div></div>
<div class="callout" style="margin-top:10px;font-size:12px">One idea ties three sections together: <b>twice as far = a quarter as much.</b> Gravity (Section 1), a radio signal (Section 5) and sunlight (Section 7) all thin out the same way, because each spreads over a sphere.</div></div>'''

def divider(s):
    P = PROG[s["prog"]]
    lec = "".join('<tr><td>%d</td><td><b>%s</b></td><td>%d</td><td>%d pages</td></tr>' % (j + 1, esc(t), page_of(f), npages(f)) for j, (t, f) in enumerate(s["lectures"]))
    cue = "".join("<li>%s</li>" % esc(c) for c in P["cue"])
    return f'''<div class="page" style="border-top:22px solid {s["color"]}">{top("SPACE X · SECTION %d OF 7" % s["n"], "Section %d · <span>%s</span>" % (s["n"], esc(s["name"])), "Start here. The sentence, the talk card, and the page of every lecture in this section.")}
<div class="two"><div style="flex:1.15">
<div class="card" style="padding:12px 16px;border-color:{s["color"]}"><h3>Say this</h3><div style="font-size:17px;line-height:1.4;font-weight:700">{esc(s["say"])}</div></div>
<div class="card" style="margin-top:10px;padding:10px 16px"><h3>The lectures</h3><table class="mech" style="font-size:12.5px"><tr><th style="width:26px">#</th><th>Lecture</th><th style="width:60px">Page</th><th style="width:70px">Length</th></tr>{lec}</table>
<div style="font-size:11.5px;margin-top:6px">In each one: page 1 is the spread to copy, the next page teaches it, the one after is what the instructor got wrong.</div></div>
<div class="two" style="margin-top:10px"><div class="mini" style="font-size:11.5px;line-height:1.45"><b>Number to know</b><br>{esc(s["num"])}</div><div class="mini" style="font-size:11.5px;line-height:1.45"><b>Don't repeat</b><br>{esc(s["dont"])}</div></div></div>
<div style="flex:1"><div class="card" style="padding:12px 16px"><h3>Talk card · {esc(P["mins"])}</h3>
<div style="font-size:12px;line-height:1.45;margin-bottom:6px"><b>He opens with:</b> {esc(P["opener"])}</div>
<ul class="r" style="font-size:12px;line-height:1.5">{cue}</ul>
<div style="font-size:12px;line-height:1.45;margin-top:6px"><b>Land on:</b> {esc(P["land"])}</div></div>
<div class="callout" style="margin-top:10px;font-size:12px">In the app: scenes {s["scenes"]} in Learn, and the "{esc(P["short"])}" talk in Teach.</div></div></div></div>'''

back_rows = "".join('<tr><td><b>%s</b></td><td>%d</td><td>%d pages</td></tr>' % (esc(t), page_of(f), npages(f)) for t, f in BACK)
back = f'''<div class="page" style="border-top:22px solid #0b1437">{top("SPACE X · BACK OF THE NOTEBOOK", "The back pages: <span>words, names and cards</span>", "Reference material. You look things up here; you don't read it through.")}
<div class="two"><div class="card" style="flex:1.5;padding:10px 16px"><table class="mech" style="font-size:12.5px"><tr><th>What</th><th style="width:60px">Page</th><th style="width:80px">Length</th></tr>{back_rows}</table></div>
<div style="flex:1"><div class="card" style="padding:10px 14px"><h3>Where to look</h3><ul class="r" style="font-size:12px;line-height:1.5">
<li><b>A word you don't know:</b> the lecture's own vocabulary page first, then the glossary here. For every word in the course, the app's Terms tab.</li>
<li><b>A name</b> (a probe, an engine, a person): Who's Who.</li>
<li><b>Sections 1–3 as a talk:</b> the teach-it-back kit.</li>
<li><b>What to write in the paper notebook:</b> the concept cards and the copy-into-notes sheet.</li></ul></div>
<div class="callout" style="margin-top:10px;font-size:12px">The word banks and glossary here cover Sections 1–3. For Sections 4–7 the words are on each lecture's vocabulary page.</div></div></div></div>'''

gen = [contents, call1, call2] + [divider(s) for s in SECTIONS] + [back]
hp = os.path.join(TMP, "gen.html"); open(hp, "w").write(HEAD + "</head><body>" + "".join(gen) + "</body></html>")
gp = os.path.join(TMP, "gen.pdf"); to_pdf(hp, gp)
G = PdfReader(gp); assert len(G.pages) == 3 + len(SECTIONS) + 1, len(G.pages)
gidx = {"gen:contents": [0], "gen:call": [1, 2], "gen:back": [3 + len(SECTIONS)]}
for j, s in enumerate(SECTIONS): gidx["gen:div%d" % s["n"]] = [3 + j]

# page-number overlay
ov = "".join('<div class="pg"><span>%s · <b>%d</b> / %d</span></div>' % (esc(r[6]), r[7] + j, TOTAL) for r in rows for j in range(r[4]))
op = os.path.join(TMP, "ov.html")
open(op, "w").write('<!doctype html><html><head><meta charset="utf-8"><style>@page{size:letter landscape;margin:0}body{margin:0;font-family:Verdana,"DejaVu Sans",sans-serif}'
                    '.pg{width:11in;height:8.5in;position:relative;page-break-after:always;overflow:hidden}.pg:last-child{page-break-after:auto}'
                    '.pg span{position:absolute;top:0.06in;right:0.14in;font-size:9.5px;color:#222;background:#fff;border:1px solid #888;border-radius:999px;padding:1px 9px}</style></head><body>' + ov + '</body></html>')
opdf = os.path.join(TMP, "ov.pdf"); to_pdf(op, opdf)
O = PdfReader(opdf); assert len(O.pages) == TOTAL, (len(O.pages), TOTAL)

# ---------------------------------------------------------------- merge
w = PdfWriter(); parent = None
for i, k, t, f, n, lvl, st, pg in rows:
    if k == "pdf":
        w.append(PdfReader(F(f)), import_outline=False)
    else:
        for gi in gidx[k]: w.add_page(G.pages[gi])
    item = w.add_outline_item(t, pg - 1, parent=parent if lvl else None)
    if not lvl: parent = item
assert len(w.pages) == TOTAL, (len(w.pages), TOTAL)
for i, page in enumerate(w.pages):
    page.merge_page(O.pages[i])
w.add_metadata({"/Title": "Space X Notebook: Interplanetary Spacecraft and Satellite Engineering (%s)" % VER})
w.compress_identical_objects()
with open(OUT, "wb") as fh: w.write(fh)
print("wrote", OUT, TOTAL, "pages", round(os.path.getsize(OUT) / 1e6, 1), "MB")
print("divider pages:", [page_of(s["lectures"][0][1]) - 1 for s in SECTIONS])
