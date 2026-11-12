from lib import *
B="SEC 4 · LEC 3 · ELECTRIC PROPULSION + ION THRUSTERS"
T=lambda x:B.replace("ELECTRIC PROPULSION + ION THRUSTERS",x)
def atom(x,y): return f'<circle cx="{x}" cy="{y}" r="4.2" fill="#fff" stroke="#111" stroke-width="1.3"/>'
def ion(x,y): return f'<circle cx="{x}" cy="{y}" r="4.6" fill="#fff" stroke="#111" stroke-width="1.3"/><text x="{x}" y="{y+2.6}" text-anchor="middle" font-size="7.5" font-weight="bold" fill="#111">+</text>'
def el(x,y): return f'<circle cx="{x}" cy="{y}" r="1.7" fill="#111"/>'
svg=f'''<svg width="100%" height="428" viewBox="0 0 330 412" style="display:block" font-family="Verdana, sans-serif">
<defs><marker id="ar" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#111"/></marker>
<pattern id="hat" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" stroke="#111" stroke-width="1"/></pattern></defs>
<text x="8" y="13" font-size="10" font-weight="bold" fill="#111">1 · INSIDE AN ION THRUSTER</text>
<text x="228" y="30" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#111">+ grid | − grid</text>
<line x1="221" y1="34" x2="221" y2="52" stroke="#777" stroke-width="0.8"/><line x1="233" y1="34" x2="233" y2="52" stroke="#777" stroke-width="0.8"/>
<rect x="95" y="40" width="34" height="10" fill="url(#hat)" stroke="#111" stroke-width="1.2"/><rect x="160" y="40" width="34" height="10" fill="url(#hat)" stroke="#111" stroke-width="1.2"/>
<rect x="95" y="136" width="34" height="10" fill="url(#hat)" stroke="#111" stroke-width="1.2"/><rect x="160" y="136" width="34" height="10" fill="url(#hat)" stroke="#111" stroke-width="1.2"/>
<path d="M221,54 H72 V132 H221" fill="none" stroke="#111" stroke-width="2.2"/>
<line x1="221" y1="54" x2="221" y2="132" stroke="#111" stroke-width="2.2" stroke-dasharray="5 4"/>
<line x1="233" y1="54" x2="233" y2="132" stroke="#111" stroke-width="2.2" stroke-dasharray="5 4"/>
<rect x="58" y="84" width="24" height="18" fill="#ddd" stroke="#111" stroke-width="1.6"/>
<line x1="14" y1="66" x2="68" y2="66" stroke="#111" stroke-width="1.4" marker-end="url(#ar)"/>
<text x="8" y="60" font-size="8.5" font-weight="bold" fill="#111">gas in</text>
<text x="8" y="118" font-size="8.5" font-weight="bold" fill="#111">electron</text><text x="8" y="129" font-size="8.5" font-weight="bold" fill="#111">gun</text>
{el(92,93)}{el(104,88)}{el(117,99)}{el(150,70)}{el(170,112)}{el(196,84)}
{atom(100,70)}{atom(128,116)}{atom(145,92)}
{ion(170,74)}{ion(190,104)}{ion(205,68)}{ion(152,118)}
{ion(250,66)}{ion(250,93)}{ion(250,120)}
<line x1="258" y1="66" x2="318" y2="66" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/><line x1="258" y1="93" x2="320" y2="93" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/><line x1="258" y1="120" x2="318" y2="120" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
<rect x="262" y="24" width="30" height="13" fill="#ddd" stroke="#111" stroke-width="1.5"/>
{el(284,45)}{el(292,52)}{el(302,58)}
<text x="322" y="18" text-anchor="end" font-size="8.5" font-weight="bold" fill="#111">neutralizer</text>
<text x="322" y="146" text-anchor="end" font-size="8.5" font-weight="bold" fill="#111">ions out at ~40 km/s</text>
<text x="8" y="163" font-size="8" fill="#111">○ neutral atom   ⊕ positive ion   • electron</text>
<text x="8" y="175" font-size="8" fill="#111">hatched = magnet · dashed = grid with holes</text>
<line x1="8" y1="184" x2="322" y2="184" stroke="#bbb" stroke-width="1"/>
<text x="8" y="199" font-size="10" font-weight="bold" fill="#111">2 · THE FOUR STEPS</text>
<g font-size="8.5" fill="#111">
<rect x="8" y="206" width="152" height="38" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="15" y="221" font-weight="bold">1 FEED</text><text x="15" y="234">xenon gas, a few mg per second</text>
<rect x="170" y="206" width="152" height="38" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="177" y="221" font-weight="bold">2 IONIZE</text><text x="177" y="234">electrons knock electrons off</text>
<rect x="8" y="250" width="152" height="38" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="15" y="265" font-weight="bold">3 ACCELERATE</text><text x="15" y="278">grids pull the ions out fast</text>
<rect x="170" y="250" width="152" height="38" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="177" y="265" font-weight="bold">4 NEUTRALIZE</text><text x="177" y="278">add electrons back to the beam</text>
</g>
<line x1="8" y1="296" x2="322" y2="296" stroke="#bbb" stroke-width="1"/>
<text x="8" y="311" font-size="10" font-weight="bold" fill="#111">3 · TORTOISE AND HARE</text>
<line x1="40" y1="400" x2="40" y2="320" stroke="#111" stroke-width="1.3" marker-end="url(#ar)"/>
<line x1="40" y1="400" x2="318" y2="400" stroke="#111" stroke-width="1.3" marker-end="url(#ar)"/>
<text x="8" y="330" font-size="8" fill="#111">speed</text><text x="300" y="411" font-size="8" fill="#111">time</text>
<path d="M40,400 L56,356 L300,356" fill="none" stroke="#111" stroke-width="2.4"/>
<path d="M40,400 L296,327" fill="none" stroke="#111" stroke-width="2.4" stroke-dasharray="7 4"/>
<text x="64" y="350" font-size="8.5" font-weight="bold" fill="#111">chemical: minutes, then coast</text>
<text x="322" y="378" text-anchor="end" font-size="8.5" font-weight="bold" fill="#111">electric (dashed): gentle push</text>
<text x="322" y="390" text-anchor="end" font-size="8.5" font-weight="bold" fill="#111">for months, ends up faster</text>
</svg>'''
p1=spread(B,'The tortoise <span>engine</span>','S4 / L3 — Electric propulsion',svg,
 "○ atom · ⊕ ion · • electron · hatched = magnet · dashed line = grid · dashed curve = electric",
 ["1. Electric = very fast exhaust, very little propellant, very small push.",
  "2. Thrust is capped by electric power; it wins by pushing for months.",
  "3. Ion thruster: ionize the gas, grids fling the ions out, neutralizer adds electrons."],
 ['What do electric and chemical engines have in common?','Why does electric use so little propellant?','Why is the thrust so low?',
  'How does a tiny push reach a high speed?','What is it used for? What can\'t it do?','Ion thruster: the four steps?',
  'What do the two grids do?','Why the neutralizer?','Two example missions?','<span class="hl b">? what exactly is plasma</span>'],
 ['<span class="hl y">electric propulsion</span>: stored propellant → high-speed jet (same idea as chemical)',
  '<span class="hl y">Isp</span> very high (<span class="hl k">3,000+ s</span>) → exhaust very fast → <span class="hl g">very little propellant</span>',
  'thrust <span class="hl o">low</span>: limited electric power → tiny mass flow',
  'low thrust × very long time = <span class="hl g">very high final speed</span>',
  'mature tech · most new satellites carry it',
  'uses: orbit changes (<span class="hl y">primary propulsion</span>) · orbit maintenance · <span class="hl o">NOT launch or landing</span> (no big thrust)',
  '<span class="hl y">ion thruster</span> = accelerates ions with electricity',
  '<span class="hl y">ionize</span>: electron gun fires electrons at neutral atoms → knocks an electron off → positive <span class="hl y">ion</span> · <span class="hl y">plasma</span> = ionized gas · magnets help',
  'accelerate: voltage between <span class="hl y">+ grid</span> and <span class="hl y">− grid</span> shoots ions out at <span class="hl k">~40 km/s</span>',
  '<span class="hl y">neutralizer</span>: fires electrons into the beam → ship stays uncharged',
  'Deep Space 1 (NASA, <span class="hl k">1998</span>) · BepiColombo (ESA + JAXA, <span class="hl k">2018</span>, to Mercury)'])

p2=f'''<div class="page">{top(T("TEACH"),'Static electricity, <span>pointed backward</span>','Simple story first, then the official names, then how it actually works with numbers you can check.')}
<div class="eli"><b style="font-size:14px">🧒 Like you're 5</b><br>
Rub a balloon on your hair and it pulls your hair toward it without touching. That pull is electricity grabbing things that are <b>charged</b>. An ion engine is that trick, aimed out the back. Step one: take a gas and knock one tiny piece (an electron) off each atom. The atom is now charged, and it is called an <b>ion</b>. Step two: put two metal screens full of holes at the back, one charged plus and one charged minus. They yank the ions through the holes and fling them out at 40 km a second, forty times faster than a rifle bullet. Step three: squirt the knocked-off electrons out as well, or the ship would end up charged and pull its own exhaust straight back.<br>
The push is about the weight of two sheets of paper. But it never stops. A chemical rocket is the hare: one huge sprint, then it is out of breath. The ion engine is the <b>tortoise</b>: a tiny push, every second, for years, and it ends up going faster on a fifth of the propellant.</div>
<div class="two">
<div class="card" style="padding:9px 13px"><h3>🏷 The official names (name first, then what it means)</h3>
<ul class="names">
<li><b>Electric propulsion, EP</b> (<b>solar electric propulsion, SEP</b>, when solar panels supply the power): electricity, not fire, accelerates the propellant.</li>
<li><b>Gridded ion thruster</b> (electrostatic ion thruster, ion engine): the type in this lecture. Its cousin the <b>Hall-effect thruster</b> is the most common electric engine today and was not covered.</li>
<li><b>Ionization</b> (here: electron-impact ionization): knocking an electron off a neutral atom. It costs the <b>ionization energy</b>, 12.1 eV for xenon.</li>
<li><b>Ion</b>: an atom with a net charge. Lose an electron and it is a positive ion.</li>
<li><b>Plasma</b>: gas hot or energetic enough that it is a mix of ions and free electrons. Overall it is still neutral. Often called the fourth state of matter.</li>
<li><b>Discharge chamber</b> (ionization chamber): the can where the gas is ionized.</li>
<li><b>Discharge cathode</b> (hollow cathode; the slide's "electron gun") and <b>anode</b>: the negative source of electrons and the positive wall that attracts them.</li>
<li><b>Potential difference</b> (voltage): the electrical "height" between two points. Charges fall through it and speed up.</li>
<li><b>Ion optics</b>: the pair of grids. <b>Screen grid</b> (the slide's "positive grid") and <b>accelerator grid</b> ("negative grid").</li>
<li><b>Neutralizer</b> (neutralizer cathode; the slide's "neutralizing electron gun"): emits electrons into the ion beam.</li>
<li><b>Electron backstreaming</b>: outside electrons rushing back into the engine. The negative grid blocks it.</li>
<li><b>Recombination</b>: an ion and an electron rejoining into a neutral atom.</li>
<li><b>Primary propulsion</b> / <b>station-keeping</b> / <b>attitude control</b>: the main Δv job / holding an orbit / pointing.</li>
</ul></div>
<div class="card" style="padding:9px 13px"><h3>🛠 How it actually works</h3>
<table class="mech"><tr><th style="width:70px">Step</th><th>The mechanism, with numbers (Deep Space 1's engine)</th></tr>
<tr><td><b>1 · Feed</b></td><td>Xenon gas trickles into the chamber: about <b>3 milligrams per second</b>. Xenon because it is heavy, easy to ionize and does not react with anything.</td></tr>
<tr><td><b>2 · Ionize</b></td><td>The cathode emits electrons; about 30 volts speeds them up. One that hits a xenon atom hard enough (12.1 eV) knocks an electron off: now it is a positive ion. Magnets make the electrons spiral, so they travel far farther before reaching the wall and get many more chances to hit an atom.</td></tr>
<tr><td><b>3 · Accelerate</b></td><td>Screen grid at <b>+1,100 V</b>, accelerator grid at −180 V, half a millimetre apart. An ion that drifts into a hole falls through that voltage: energy = charge × voltage = ½mv². For xenon, v = √(2qV ÷ m) ≈ <b>40 km/s</b>.</td></tr>
<tr><td><b>4 · Where the push lands</b></td><td>The grids pull the ions backward-out; the ions pull the grids forward with the same force. Newton's third law again. The thrust is felt on the grids.</td></tr>
<tr><td><b>5 · Neutralize</b></td><td>The beam carries off 1.76 amps of positive charge. Unbalanced, the ship would charge negative in microseconds and drag its own ions back: no thrust. The neutralizer emits the same 1.76 A of electrons.</td></tr>
<tr><td><b>6 · Thrust</b></td><td>F = ṁ × vₑ ≈ 3 mg/s × 30 km/s = <b>0.092 N</b>, 9 grams of push. (Effective exhaust is 30, not 40 km/s, because some gas leaves un-ionized.) Isp ≈ <b>3,100 s</b>.</td></tr>
<tr><td><b>7 · Power is the limit</b></td><td>That 0.092 N took 2,300 W, a whole solar array. Thrust ≈ 2 × efficiency × power ÷ vₑ. For fixed power, faster exhaust means <i>less</i> thrust. About 40 mN per kW.</td></tr>
<tr><td><b>8 · Add it up</b></td><td>0.092 N on 486 kg adds 16 m/s every day. Deep Space 1 thrust for 678 days in total: Δv <b>4.3 km/s</b> from 74 kg of xenon. A chemical engine would need about 360 kg.</td></tr></table></div>
</div></div>'''

p3=f'''<div class="page">{top(T("FACT CHECK"),'Where it is used, <span>and what he got loose</span>','The uses, the caption errors (many this time) and where the instructor was loose or wrong.')}
<div class="two">
<div>
<div class="card" style="padding:8px 13px"><h3>🛰 What electric propulsion does and doesn't do</h3>
<table class="mech" style="font-size:10.4px"><tr><th>Job</th><th>Electric?</th><th>Why</th></tr>
<tr><td><b>Launch from the ground</b></td><td>Never</td><td>Thrust is 10,000+ times less than the craft's weight, and the engine only works in vacuum.</td></tr>
<tr><td><b>Landing, capture burns</b></td><td>No</td><td>They need km/s within minutes.</td></tr>
<tr><td><b>Raising orbit to GEO</b></td><td>Yes</td><td>Takes about 6 months instead of days, but saves tonnes of propellant.</td></tr>
<tr><td><b>Station-keeping</b></td><td>Yes, since the 1990s</td><td>Small, steady corrections: exactly what it is good at.</td></tr>
<tr><td><b>Deep-space cruise</b></td><td>Yes</td><td>Months of thrust add up to many km/s: Deep Space 1, Dawn, BepiColombo, Psyche.</td></tr>
<tr><td><b>Fine pointing</b></td><td>Starting to</td><td>Tiny electric thrusters already do this on a few science missions.</td></tr></table></div>
<div class="card" style="margin-top:10px;padding:8px 13px"><h3>🔎 Caption errors</h3>
<table class="t" style="font-size:10px"><tr><th>Captions said</th><th>Instructor meant</th></tr>
<tr><td>"stort much propellant… propeller"</td><td><b>stored mass propellant</b>… propellant</td></tr>
<tr><td>"specific Kimballs" / "G-0 GZA"</td><td>specific <b>impulse</b> / <b>g₀</b></td></tr>
<tr><td>"X and velocity", "section velocity"</td><td><b>ejection</b> velocity</td></tr>
<tr><td>"lexing propulsion"</td><td><b>electric</b> propulsion</td></tr>
<tr><td>"healthy object"</td><td>type of <b>objective</b></td></tr>
<tr><td>"looking for parts and systems"</td><td><b>launch or landing</b> systems</td></tr>
<tr><td>"I am now using a new tool Gus"</td><td><b>ionizing a neutral gas</b></td></tr>
<tr><td>"election", "electron gamma ray"</td><td><b>electron</b>, electron <b>gun</b></td></tr>
<tr><td>"a cathode and that out"</td><td>a cathode and <b>an anode</b></td></tr>
<tr><td>"the Greeks", "negative grade"</td><td>the <b>grids</b>, negative <b>grid</b></td></tr>
<tr><td>"the plastic"</td><td>the <b>plasma</b></td></tr>
<tr><td>"in the camps the organization efficiency"</td><td><b>enhance the ionization</b> efficiency</td></tr>
<tr><td>"audience", "electrons annoyance"</td><td><b>ions</b>, electrons <b>and ions</b></td></tr>
<tr><td>"a sound yak's a collaboration… All of them be"</td><td><b>ESA and JAXA</b> collaboration… <b>BepiColombo</b></td></tr></table></div></div>
<div><div class="card" style="padding:8px 13px"><h3>▲ Where the instructor was loose</h3>
<ul class="r" style="font-size:10.7px">
<li><b>"Electrons collide with atoms breaking their electronic bonds."</b> No bonds are involved; xenon is single atoms. The collision knocks an electron <i>off the atom</i>. That is ionization.</li>
<li><b>"Plasma is… all of these particles which are positive."</b> Plasma is the ions <i>and</i> the free electrons together, neutral overall. Only the ions get pulled out by the grids.</li>
<li><b>"The neutralizer… so the gas will freely disperse."</b> The real reason is charge. Fire out only positive ions and the ship goes negative and pulls them back. This is the spacecraft charging from Section 2, self-inflicted.</li>
<li><b>"It cannot be used for launch… because of very low mass ejection."</b> Closer: its thrust is thousands of times smaller than the craft's weight, and it needs vacuum to run.</li>
<li><b>"By 2020 half of all satellites will have electric propulsion."</b> An old forecast that came true and more. Every Starlink has an electric thruster, and they are most of what gets launched.</li>
<li><b>BepiColombo "to perform orbital maneuvers around Mercury."</b> Its ion engines are for the trip <i>to</i> Mercury, braking against the Sun's pull for years. That module is dropped before arrival; chemical thrusters do the capture. Arrival was planned for November 2026, which is right now. I can't confirm whether it has happened.</li>
<li><b>"Electron gun" and "positive / negative grid"</b> are the diagram's labels. The engineering names are discharge cathode, screen grid and accelerator grid.</li>
<li><b>Not said: why low thrust.</b> He says the mass flow is low. The cause is power: every milligram needs about 500 joules to reach 30 km/s, and the panels only supply so many joules per second.</li>
<li><b>Not said: the Hall thruster</b>, the most common electric engine flying.</li></ul></div>
<div class="card" style="margin-top:10px;padding:8px 13px"><h3>📒 Question bank cards</h3>
<ul class="r" style="font-size:10.8px">
<li>Four steps of an ion thruster, in order.</li>
<li>What limits an electric engine's thrust: propellant, or power?</li>
<li>What happens if the neutralizer fails?</li>
<li>Where on the engine does the push actually land?</li>
<li>Name three jobs electric propulsion does and two it can't.</li></ul></div></div>
</div></div>'''

vocab=[("Electric propulsion (EP)","engines that use electricity to accelerate propellant.","Repeat, L1."),
("Solar electric propulsion (SEP)","electric propulsion powered by solar panels. Nearly all of it so far.",""),
("Stored mass propellant","the propellant carried on board. Here xenon gas.","Repeat."),
("Propulsive jet","the stream leaving the engine. Here a beam of ions.","Repeat."),
("Specific impulse (Isp)","exhaust speed ÷ g₀, in seconds. Electric: 1,500–4,000+ s.","Repeat."),
("Ejection velocity = exhaust velocity (vₑ)","how fast the propellant leaves. 30–40 km/s here.","Repeat."),
("g₀","9.81 m/s², a constant.","Repeat."),
("Thrust / low thrust","the push / here, a fraction of a newton.","Repeat."),
("Electric power (watts, kW)","energy per second supplied by the solar panels. 1 kW = 1,000 W.",""),
("Mature technology","proven, flown many times, no longer experimental.",""),
("Orbit change / primary propulsion","the engine that provides the mission's main Δv.",""),
("Orbital maintenance = station-keeping","small burns that hold an orbit against drift.","Repeat, scene 1."),
("Attitude control","controlling which way the spacecraft points.","Repeat. Section 6."),
("Launch / landing systems","getting off a planet / down onto one. Both need thrust bigger than weight.",""),
("Peak thrust","the most push an engine can give at one moment.",""),
("Ion thruster (gridded ion engine)","ionizes gas and accelerates the ions with charged grids.","Static electricity, pointed backward."),
("Atom / neutral atom","the smallest piece of an element / one with equal + and − charges, so no net charge.",""),
("Electron","the tiny negative particle around an atom. Easy to knock off.",""),
("Ion / positive ion","an atom with a net charge / one that lost an electron.",""),
("Ionize / ionization","to turn atoms into ions / the process.",""),
("Ionization energy","the energy it takes to knock one electron off. Xenon: 12.1 eV.","eV is a repeat from Section 2."),
("Charge (positive / negative)","the property electricity acts on. Opposites attract, likes repel.",""),
("Electric field","the region where a charge feels a push. Between the grids it is very strong.",""),
("Potential difference = voltage (V)","electrical 'height' between two points. A charge speeds up falling through it.","A hill for charges."),
("Cathode / anode","the negative electrode that gives off electrons / the positive one that collects them.",""),
("Electron gun","the slide's name for the cathode that sprays electrons into the chamber.",""),
("Electron beam","a stream of electrons.",""),
("Collide / collision","hit. Here an electron hitting an atom.",""),
("Plasma","ionized gas: ions and free electrons mixed, neutral overall. Lightning, neon signs, the Sun.","The fourth state of matter."),
("Discharge chamber","the can where the gas is ionized.",""),
("Magnet / magnetic field","makes electrons spiral so they hit more atoms.",""),
("Ionization efficiency","what fraction of the gas actually gets ionized.",""),
("Grid","a thin metal plate with thousands of holes.",""),
("Screen grid = positive grid","the inner grid, at high positive voltage.",""),
("Accelerator grid = negative grid","the outer grid, slightly negative. Pulls ions out and keeps outside electrons from getting in.",""),
("Repel","push away. Negative repels negative.",""),
("Neutralizer = neutralizing electron gun","a small cathode that sprays electrons into the ion beam so the ship stays uncharged.",""),
("Neutralize / charge balance","make the + and − equal again.",""),
("Recombination","an ion and an electron joining back into a neutral atom, out in the beam.",""),
("Disperse","spread out and drift away.",""),
("Xenon","the heavy, inert gas ion engines use.","Repeat, L1."),
("Ampere (A)","the unit of electric current: charge flowing per second.",""),
("Hall-effect thruster","the other main electric engine; not in this lecture.","Repeat, L1."),
("Deep Space 1","NASA's 1998 test probe, first to cruise on an ion engine.","Who's Who."),
("BepiColombo / ESA / JAXA","Mercury mission launched 2018 / European and Japanese space agencies.","Who's Who."),]
p4=f'''<div class="page">{top(T("VOCABULARY"),'Every word used, <span>in plain English</span>',f'{len(vocab)} entries. This lecture is full of electricity words, so they are all here. "Repeat" = you have met it before.')}
<div class="gl2" style="font-size:10.1px;line-height:1.33">{"".join(f"<div><b>{esc(a)}</b> — {esc(b)}{(' <i>'+esc(c)+'</i>') if c else ''}</div>" for a,b,c in vocab)}</div></div>'''

c1=("ELECTRIC PROPULSION (EP)","—","electricity, not fire, accelerates the propellant","chemistry caps exhaust at ~4.5 km/s. Electricity has no cap, so EP uses a tenth of the propellant","Isp 3,000+ s · thrust under 1 N · runs for years","a weak = bad engine (more total Δv)","power limits thrust · ion + Hall thrusters")
c2=("ION THRUSTER","gridded ion engine","ionizes gas, then grids fling the ions out","a charged atom can be grabbed by voltage and thrown far faster than any flame can throw gas","+1,100 V → xenon ions at 40 km/s · 0.092 N from 2.3 kW","Hall thruster (magnetic, no grids)","ionize → accelerate → neutralize")
c3=("PLASMA","ionized gas","ions + free electrons, neutral overall","neutral gas ignores electricity. Knock electrons off and you can steer and accelerate it","xenon: 12.1 eV per atom to ionize","'only positive particles' (electrons are in it too)","ionization · ionosphere · spacecraft charging")
c4=("NEUTRALIZER","neutralizer cathode","sprays electrons into the ion beam","shoot out only + ions and the ship goes negative and pulls them back: thrust dies","Deep Space 1: 1.76 A of ions out, 1.76 A of electrons out","the electron gun inside (that one ionizes)","spacecraft charging · recombination")
cA,a1,a2=cardpage(c1,c2,"C20","scene 9"); cB,b1,b2=cardpage(c3,c4,"C21","scene 9")
p5=f'''<div class="page">{top(T("COPY INTO NOTES"),'Where each piece goes <span>in the notebook</span>','Routes A to D for this lecture. The concept cards (route E) are on the next page.')}
<div class="two route">
<div class="card" style="padding:9px 13px"><h3>A · Equations &amp; key numbers page (p3–4)</h3>
<div class="copy">v = √(2qV ÷ m)     ion speed from grid voltage
                   xenon, 1,100 V → 40 km/s
F ≈ 2·η·P ÷ vₑ     thrust from power (η = efficiency)
                   2,300 W → 0.092 N · ~40 mN per kW
ion engine         Isp ~3,100 s · ṁ ~3 mg/s · 16 m/s per day
Deep Space 1       678 days thrust · 74 kg Xe · Δv 4.3 km/s</div>
<h3>B · Section 4 map page (add to the sentence)</h3>
<div class="copy">electric: ionize xenon → grids (+1,100 V) fling ions at 40 km/s
→ neutralizer adds electrons; tiny push for years, power-limited</div>
<h3>D · Question bank ("but how?" cards)</h3>
<div class="copy">Q: How does an ion engine speed the gas up with no fire?
A: Knock an electron off each atom (ion). Charged grids pull the
   ions through 1,100 V: v = √(2qV/m) ≈ 40 km/s.
Q: Why does it need a neutralizer?
A: Positive ions leave, so the ship would charge negative and pull
   them back. Equal electrons out keeps it neutral.
Q: Why is the thrust so small?
A: Power. Fast exhaust costs ~500 J per milligram; panels give
   only a few thousand joules per second.
Q: How can 9 grams of push get anywhere?
A: It never stops: 16 m/s per day, 4.3 km/s after 678 days.</div></div>
<div class="card" style="padding:9px 13px"><h3>C · One-line word bank (new lines)</h3>
<div class="copy">p__ · electric propulsion (EP) = SEP · electricity throws it  → C20
p__ · primary propulsion · the engine doing the main Δv
p__ · ion thruster = gridded ion engine · ionize, then grids  → C20
p__ · atom / electron · smallest bit of an element / its − particle
p__ · ion · atom with a net charge (lost an electron = +)
p__ · ionization · knocking an electron off an atom
p__ · ionization energy · cost of that: xenon 12.1 eV
p__ · plasma = ionized gas · ions + electrons, neutral overall  → C21
p__ · charge · what electricity acts on; opposites attract
p__ · voltage = potential difference · a hill charges fall down
p__ · cathode / anode · gives off electrons / collects them
p__ · electron gun = discharge cathode · sprays electrons in
p__ · discharge chamber · the can where gas is ionized
p__ · screen grid (+) / accelerator grid (−) · pull the ions out
p__ · neutralizer · electrons into beam; ship stays neutral → C21
p__ · electron backstreaming · outside electrons rushing in
p__ · recombination · ion + electron → neutral atom again
p__ · Hall-effect thruster · other electric engine, magnetic
p__ · ampere (A) · current: charge per second</div></div>
</div></div>'''
p6=f'''<div class="page">{top(T("CONCEPT CARDS"),'Route E: <span>pages C20 and C21</span>','Two notebook pages, two cards each. Copy line for line; the faint numbers are your ruled lines.')}
<div style="display:flex;gap:16px;justify-content:center">{cA}{cB}</div>
<div style="text-align:center;font-size:10.5px;color:#444;margin-top:6px">C20: {a1} + {a2} lines of 22 · C21: {b1} + {b2} lines of 22</div></div>'''
p7=f'''<div class="page">{top(T("SAY IT OUT LOUD"),'Last page: <span>prove it by talking</span>','After the spread and the 3-line summary, with everything closed. Send me what you said and I will grade it like a friend would.')}
<div class="two"><div>
<div class="card"><h3>🗣 The friend's opening question</h3><div style="font-size:13px;line-height:1.5">"An engine that pushes as hard as two sheets of paper? How is that any use?"</div></div>
<div class="card" style="margin-top:12px"><h3>✅ Three sentences you should be able to say</h3><ul class="r" style="font-size:12px">
<li>Because it never stops. It adds a few metres per second every day for years, and ends up faster than a chemical rocket on a fifth of the propellant.</li>
<li>It works like static electricity: knock an electron off each gas atom so it is charged, then two charged grids fling those ions out the back at 40 kilometres a second.</li>
<li>The catch is power. Throwing gas that fast takes a lot of electricity and solar panels only give so much, so the push is tiny and you can't launch or land with it.</li></ul></div>
<div class="card" style="margin-top:12px"><h3>❓ Follow-ups a friend might ask</h3><ul class="r" style="font-size:12px">
<li>"What's an ion?" (an atom that lost an electron, so electricity can grab it)</li>
<li>"What's plasma?" (gas where the atoms have been split into ions and loose electrons)</li>
<li>"Why spit the electrons out too?" (otherwise the ship charges up and pulls its exhaust back)</li>
<li>"Has it actually flown?" (since 1964; Deep Space 1 in 1998, Dawn, BepiColombo, every Starlink)</li>
<li>"Why not just add more solar panels?" (you can, but panels are mass, and far from the Sun they fade)</li></ul></div></div>
<div><div class="card" style="min-height:3.2in"><h3>📝 Your explanation (paste or dictate)</h3><div style="border:2px dashed #999;border-radius:8px;height:2.5in;padding:8px;color:#999;font-size:11px">_ send it to me in chat; I'll put it here _</div></div>
<div class="card" style="margin-top:12px;min-height:2.2in;border-color:var(--green)"><h3 style="color:var(--green)">🎯 My read</h3><div style="border:2px dashed #999;border-radius:8px;height:1.5in;padding:8px;color:#999;font-size:11px">solid on: _<br>fuzzy on: _<br>fix: _<br>→ question-bank cards: _</div></div>
<div class="callout" style="margin-top:12px;font-size:11.5px">⚡ Two lectures left in Section 4. Send them the same way.</div></div></div></div>'''
write('s4-l3.html',[p1,p2,p3,p4,p5,p6,p7])
print('ok',a1,a2,b1,b2,len(vocab))
