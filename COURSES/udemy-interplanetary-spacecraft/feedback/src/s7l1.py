from lib import *
B = "SEC 7 · LEC 1 · SOLAR ARRAYS"
T = lambda x: B.replace("SOLAR ARRAYS", x)
planets = [("Mercury", "0.39 AU", "9,100", 60), ("Venus", "0.72 AU", "2,600", 17), ("Earth", "1 AU", "1,361", 9), ("Mars", "1.52 AU", "590", 4), ("Jupiter", "5.2 AU", "50", 0.6)]
bars = ""
for i, (n, d, f, h) in enumerate(planets):
    x = 14 + i * 62
    bars += '<rect x="%d" y="%.1f" width="34" height="%.1f" fill="#bbb" stroke="#111" stroke-width="1.2"/>' % (x + 10, 90 - h, h)
    bars += '<text x="%d" y="102" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#111">%s</text>' % (x + 27, n)
    bars += '<text x="%d" y="113" text-anchor="middle" font-size="8.5" fill="#111">%s W/m²</text>' % (x + 27, f)
    bars += '<text x="%d" y="124" text-anchor="middle" font-size="7.5" fill="#111">%s</text>' % (x + 27, d)
svg = f'''<svg width="100%" height="428" viewBox="0 0 330 412" style="display:block" font-family="Verdana, sans-serif">
<defs><marker id="ar" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#111"/></marker></defs>
<text x="8" y="13" font-size="10" font-weight="bold" fill="#111">1 · SUNLIGHT FADES WITH DISTANCE (solar flux)</text>
<line x1="14" y1="90" x2="320" y2="90" stroke="#111" stroke-width="1"/>
{bars}
<text x="165" y="139" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">flux = 1,361 ÷ distance² · twice as far = a quarter</text>
<line x1="8" y1="146" x2="322" y2="146" stroke="#bbb" stroke-width="1"/>
<text x="8" y="159" font-size="10" font-weight="bold" fill="#111">2 · INSIDE A SOLAR CELL</text>
<rect x="46" y="176" width="150" height="22" fill="#fff" stroke="#111" stroke-width="1.6"/>
<rect x="46" y="198" width="150" height="22" fill="#ddd" stroke="#111" stroke-width="1.6"/>
<text x="34" y="191" text-anchor="middle" font-size="10" font-weight="bold" fill="#111">n</text><text x="34" y="213" text-anchor="middle" font-size="10" font-weight="bold" fill="#111">p</text>
<line x1="70" y1="164" x2="100" y2="195" stroke="#111" stroke-width="1.3" stroke-dasharray="3 3" marker-end="url(#ar)"/>
<text x="76" y="170" font-size="8" fill="#111">photon</text>
<circle cx="108" cy="194" r="2.6" fill="#111"/><line x1="110" y1="192" x2="122" y2="182" stroke="#111" stroke-width="1.1" marker-end="url(#ar)"/>
<circle cx="108" cy="203" r="3" fill="#fff" stroke="#111" stroke-width="1.1"/><line x1="110" y1="205" x2="122" y2="214" stroke="#111" stroke-width="1.1" marker-end="url(#ar)"/>
<path d="M196,186 H250 V192" fill="none" stroke="#111" stroke-width="1.6" marker-end="url(#ar)"/>
<rect x="236" y="193" width="28" height="14" rx="3" fill="#fff" stroke="#111" stroke-width="1.4"/><text x="250" y="203" text-anchor="middle" font-size="7.5" font-weight="bold" fill="#111">load</text>
<path d="M250,207 V211 H200" fill="none" stroke="#111" stroke-width="1.6" marker-end="url(#ar)"/>
<text x="272" y="190" font-size="8" fill="#111">electrons</text><text x="272" y="200" font-size="8" fill="#111">go round</text><text x="272" y="210" font-size="8" fill="#111">= current</text>
<text x="8" y="234" font-size="8.5" fill="#111">• electron · ○ hole · the junction pushes electrons up, holes down</text>
<text x="8" y="246" font-size="8.5" fill="#111">one cell: 0.6 volts (silicon) · 2.7 volts (triple-junction)</text>
<line x1="8" y1="253" x2="322" y2="253" stroke="#bbb" stroke-width="1"/>
<text x="8" y="266" font-size="10" font-weight="bold" fill="#111">3 · THREE LAYERS CATCH MORE COLOURS</text>
<rect x="30" y="286" width="118" height="15" fill="#fff" stroke="#111" stroke-width="1.5"/><rect x="30" y="301" width="118" height="15" fill="#eee" stroke="#111" stroke-width="1.5"/><rect x="30" y="316" width="118" height="15" fill="#ccc" stroke="#111" stroke-width="1.5"/>
<g stroke="#111" stroke-width="1.4"><line x1="52" y1="272" x2="52" y2="292" marker-end="url(#ar)"/><line x1="89" y1="272" x2="89" y2="307" marker-end="url(#ar)"/><line x1="126" y1="272" x2="126" y2="322" marker-end="url(#ar)"/></g>
<g font-size="8.5" fill="#111"><text x="156" y="297"><tspan font-weight="bold">top cell:</tspan> short waves (blue)</text><text x="156" y="312"><tspan font-weight="bold">middle cell:</tspan> medium (red)</text><text x="156" y="327"><tspan font-weight="bold">bottom cell:</tspan> long (infrared)</text></g>
<text x="165" y="345" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">one layer ≈ 20% · three layers ≈ 30% · the rest is heat</text>
<line x1="8" y1="352" x2="322" y2="352" stroke="#bbb" stroke-width="1"/>
<text x="8" y="365" font-size="10" font-weight="bold" fill="#111">4 · HOW MUCH POWER</text>
<rect x="24" y="371" width="282" height="19" rx="5" fill="#fff" stroke="#111" stroke-width="1.5"/>
<text x="165" y="384" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#111">power = flux × area × efficiency</text>
<text x="165" y="400" text-anchor="middle" font-size="8.5" fill="#111">1 m² at Earth: 1,361 × 0.30 ≈ 400 W · hot cells give less</text>
</svg>'''
p1 = spread(B, 'A sandwich that <span>turns light into current</span>', 'S7 / L1 — Solar arrays', svg,
 "bar = how much sunlight · dashed arrow = photon · • electron · ○ hole · arrows down = light reaching each layer",
 ["1. Sunlight fades with distance squared: 1,361 W/m² at Earth, 50 at Jupiter.",
  "2. A photon frees an electron; the junction pushes it round the wire.",
  "3. Three stacked layers catch about 30%. Hot cells make less."],
 ['What is solar flux? Units?', 'How does it change with distance?', 'Deployable vs body-mounted arrays?', 'What are n-type and p-type?',
  'How does a photon become current?', 'Why stack three cells? Which catches what?', 'Typical efficiency?', 'What does heat do to a cell?',
  'How much power from an array?', '<span class="hl b">? where does the other 70% go</span>'],
 ['<span class="hl y">solar array</span>: turns sunlight into electricity',
  '<span class="hl y">solar flux</span> = solar radiation per unit of surface (<span class="hl k">W/m²</span>) · more flux = more power · farther from the Sun = <span class="hl o">less flux</span>',
  'Mercury: huge · Mars: needs big arrays · Jupiter: very big, efficient arrays · beyond: not enough',
  '<span class="hl y">deployable arrays</span>: folded for launch, opened in space → lots of area (Juno, Rosetta)',
  '<span class="hl y">body-mounted arrays</span>: cells on the body → less area (CubeSat, Philae)',
  '<span class="hl y">photovoltaics</span>: photon energy → electrical energy · two semiconductor layers: <span class="hl y">n-type</span> (spare electrons) + <span class="hl y">p-type</span> (<span class="hl y">holes</span>)',
  'photon knocks an electron free → it travels round the circuit = current',
  'each material uses certain wavelengths → stack three: <span class="hl y">triple-junction</span> gallium arsenide cell ≈ <span class="hl k">30%</span>',
  'top: short waves · middle: medium · bottom: long',
  'power = volts × amps · <span class="hl o">hotter cell = less power</span> · coldest (best) just out of eclipse'])

p2 = f'''<div class="page">{top(T("TEACH"),'Light in, <span>electricity out</span>','Simple story first, then the official names, then how it actually works with numbers you can check.')}
<div class="eli"><b style="font-size:14px">🧒 Like you're 5</b><br>
Sunlight is a rain of tiny packets of energy (the photons from Section 5). A solar cell is a sandwich made of two slightly different slices of crystal. Where the slices touch there is a built-in one-way slope. A packet of light knocks an electron loose, like a ball knocked off a shelf. The slope rolls it to one side, and the only way back is the long way round, through a wire, and through your equipment on the way. That flow is electricity. Nothing moves, nothing burns.<br>
Two catches. First, each crystal only uses packets of the right size: too small and they pass straight through, too big and the extra is wasted as heat. So the best cells stack <b>three</b> crystals, each tuned to a different colour, and catch about 30% of the light. Second, sunlight spreads out exactly like the radio signal did: twice as far from the Sun, a quarter as much. At Jupiter it is 27 times weaker than here, so the Juno probe needs three panels, each as long as a bus, to make what a hair dryer uses.</div>
<div class="two">
<div class="card" style="padding:9px 13px"><h3>🏷 The official names (name first, then what it means)</h3>
<ul class="names" style="font-size:10.6px">
<li><b>Solar array</b> (solar panel, photovoltaic array): many <b>solar cells</b> (photovoltaic cells, PV cells) wired together.</li>
<li><b>Solar flux</b> (solar irradiance): sunlight power per square metre. At Earth's distance it is the <b>solar constant</b>, 1,361 W/m². <b>Astronomical unit, AU</b>: the Earth–Sun distance, 150 million km. <b>Inverse-square law</b>.</li>
<li><b>Deployable array</b> (solar wings) and <b>body-mounted array</b>. A <b>solar array drive</b> turns the wings to face the Sun. <b>Hold-down and release mechanism</b>: what lets the folded wings go, often a small pyrotechnic cutter.</li>
<li><b>Photovoltaic effect</b>: light producing a voltage in a material.</li>
<li><b>Semiconductor</b>: a material such as silicon that conducts a little. <b>Doping</b>: adding a trace of another element. <b>n-type</b>: extra electrons. <b>p-type</b>: missing electrons, called <b>holes</b>.</li>
<li><b>p–n junction</b>: where the two meet. Its <b>built-in electric field</b> (in the <b>depletion region</b>) is the one-way slope.</li>
<li><b>Band gap</b>: the energy a photon needs to free an electron in that material.</li>
<li><b>Multi-junction cell</b> (<b>triple-junction</b>, 3J): several junctions stacked. Usual stack: gallium indium phosphide / <b>gallium arsenide</b> / germanium.</li>
<li><b>Efficiency</b>: electrical power out ÷ sunlight power in.</li>
<li><b>I–V curve</b>: current against voltage for a cell. <b>Maximum power point</b>: the spot on it where volts × amps is largest.</li>
<li><b>Thermal cycling</b>: repeated heating and cooling, once per orbit. <b>Beginning of life / end of life</b> power: arrays fade with age.</li>
</ul></div>
<div class="card" style="padding:9px 13px"><h3>🛠 How it actually works</h3>
<table class="mech" style="font-size:9.9px"><tr><th style="width:66px">Step</th><th>The mechanism, with numbers</th></tr>
<tr><td><b>1 · Flux</b></td><td>Flux = 1,361 ÷ (distance in AU)². Mercury (0.39): 9,100. Venus (0.72): 2,600. Mars (1.52): 590. Jupiter (5.2): <b>50</b>. Saturn (9.5): 15 W/m².</td></tr>
<tr><td><b>2 · Two slices</b></td><td>Silicon with a trace of phosphorus has spare electrons (n). With a trace of boron it has gaps where electrons are missing (p). Join them: electrons near the boundary drop into gaps, leaving a thin zone with a permanent electric field.</td></tr>
<tr><td><b>3 · Photon in</b></td><td>A photon with at least the band-gap energy frees an electron and leaves a hole. Silicon's gap is 1.1 eV, so any light shorter than 1,240 ÷ 1.1 ≈ 1,100 nm works (the eV rule from Section 5).</td></tr>
<tr><td><b>4 · Sorted</b></td><td>The built-in field sweeps the electron to the n side and the hole to the p side. That piles up charge: about <b>0.6 V</b> for silicon. Connect a wire and electrons flow from n, through the load, to p.</td></tr>
<tr><td><b>5 · The losses</b></td><td>Photons below the gap pass through unused. Photons above it lose their extra as heat. One material can never beat about 33%; real silicon reaches about 20%.</td></tr>
<tr><td><b>6 · Three layers</b></td><td>Top, gap 1.9 eV: takes light up to 650 nm. Middle, 1.4 eV: up to 890 nm. Bottom, 0.67 eV: up to 1,850 nm. Each uses its colours well and lets the rest through: about <b>30%</b>, 2.7 V per cell.</td></tr>
<tr><td><b>7 · Power</b></td><td>P = flux × area × efficiency × cos(tilt). 1 m² at Earth: 1,361 × 0.30 ≈ <b>410 W</b>. Tilt the panel 60° away from the Sun and you get half.</td></tr>
<tr><td><b>8 · Heat</b></td><td>On the slide's graph the current stays near 3.5 A while the top voltage falls from 0.63 V at 25 °C to 0.55 V at 60 °C. Power is volts × amps, so a hot cell gives less: about 0.2–0.4% per degree. A panel is at its best cold, just out of Earth's shadow.</td></tr>
<tr><td><b>9 · Age</b></td><td>Radiation knocks atoms out of place: roughly 1–3% of power lost per year. Arrays are sized for the last day of the mission.</td></tr></table></div>
</div></div>'''

p3 = f'''<div class="page">{top(T("SIZING + FACT CHECK"),'How big for <span>one kilowatt?</span>','A sizing table for your quiz on designing a solar array, then where the instructor was loose, the caption errors, and the say-it-out-loud script.')}
<div class="two" style="margin-bottom:8px">
<div class="card" style="padding:7px 13px"><h3>📐 Array area needed for 1,000 W</h3>
<table class="mech" style="font-size:10.4px"><tr><th>Where</th><th>Distance</th><th>Flux, W/m²</th><th>Area for 1,000 W</th></tr>
<tr><td><b>Mercury</b></td><td>0.39 AU</td><td>9,100</td><td>0.46 m²</td></tr>
<tr><td><b>Venus</b></td><td>0.72 AU</td><td>2,600</td><td>1.6 m²</td></tr>
<tr><td><b>Earth</b></td><td>1 AU</td><td>1,361</td><td>3.1 m²</td></tr>
<tr><td><b>Mars</b></td><td>1.52 AU</td><td>590</td><td>7.1 m²</td></tr>
<tr><td><b>Jupiter</b></td><td>5.2 AU</td><td>50</td><td>83 m²</td></tr>
<tr><td><b>Saturn</b></td><td>9.5 AU</td><td>15</td><td>280 m²</td></tr></table></div>
<div class="card" style="padding:7px 13px"><h3>🧮 The recipe (for the quiz)</h3>
<div style="font-size:11px;line-height:1.5"><b>1.</b> Flux = 1,361 ÷ (distance in AU)².<br>
<b>2.</b> Power per square metre = flux × efficiency × losses. Here: 30% cells, and 0.8 for wiring, gaps between cells and ageing.<br>
<b>3.</b> Area = power needed ÷ power per square metre.<br>
<b>Example, Mars:</b> 590 × 0.30 × 0.8 = 142 W per m². 1,000 ÷ 142 = <b>7.1 m²</b>.<br>
<b>Check on a real one:</b> Juno carries about 60 m² of cells. Near Earth they would give about 14,000 W. At Jupiter, 27 times less sunlight: about <b>500 W</b>.<br>
If the quiz gives different numbers for efficiency or losses, use theirs. The three steps stay the same.</div></div></div>
<div class="two">
<div><div class="card" style="padding:7px 13px"><h3>▲ Where the instructor was loose</h3>
<ul class="r" style="font-size:10.3px">
<li><b>"We multiply by three the efficiency."</b> No. One layer gets about 20%, three get about 30%. The layers share the same sunlight; each takes the colours it uses best. It is 1.5 times better, not 3.</li>
<li><b>The photon gives the electron "inertia to move through the circuit".</b> The photon only frees the electron. What pushes it one way is the electric field built into the junction. Without that field the electron would just fall back.</li>
<li><b>His account of which way electrons and holes go is tangled.</b> The clean version: freed electrons collect on the n side, holes on the p side, and electrons travel through the outside wire from n to p.</li>
<li><b>"Low Earth orbit… around two hours… 12 cycles a day."</b> Low orbits take 90 to 100 minutes (Section 1), so about 15 or 16 a day: nearly 6,000 hot-cold cycles a year.</li>
<li><b>Slide: "Thermal cycles: low efficiencies".</b> Two different things. Being <i>hot</i> lowers efficiency. <i>Cycling</i> between hot and cold cracks joints and ages the array.</li>
<li><b>"I think this image is from Rosetta."</b> It looks like the Juno array in a clean room, the same photo as in Section 2. I can't be certain.</li>
<li><b>"The maximum was around 40%."</b> Flight cells are 30–32%. Laboratory records with concentrated light are about 47%.</li>
<li><b>He was right</b> that no solar-powered craft has yet worked beyond Jupiter's distance, and that a cold panel fresh from the shadow gives the most power.</li>
<li><b>Not said: arrays make nothing in the shadow.</b> That is the reason for the next lecture, batteries.</li></ul></div></div>
<div><div class="card" style="padding:7px 13px"><h3>🔎 Caption errors</h3>
<table class="t" style="font-size:9.7px"><tr><th>Captions said</th><th>Instructor meant</th></tr>
<tr><td>"several of our race", "efficiency race"</td><td><b>solar arrays</b></td></tr>
<tr><td>"sort of flux"</td><td><b>solar flux</b></td></tr>
<tr><td>"3-D used" · "culpably"</td><td><b>reduced</b> · <b>probably</b></td></tr>
<tr><td>"the playable arrays"</td><td><b>deployable</b> arrays</td></tr>
<tr><td>"body mounts at the race"</td><td><b>body-mounted arrays</b></td></tr>
<tr><td>"keeps out"</td><td><b>CubeSat</b></td></tr>
<tr><td>"fil-A… the land of founders at"</td><td><b>Philae</b>, the lander of <b>Rosetta</b></td></tr>
<tr><td>"full of all types theory"</td><td><b>photovoltaics</b> theory</td></tr>
<tr><td>"solar foton", "fortune"</td><td>solar <b>photon</b></td></tr>
<tr><td>"pea type" · "election"</td><td><b>p-type</b> · <b>electron</b></td></tr>
<tr><td>"kind of whole… they name it all"</td><td>a <b>hole</b></td></tr>
<tr><td>"clean room terms"</td><td><b>equilibrium</b> terms</td></tr>
<tr><td>"unperson" · "Curran's times the Volt"</td><td><b>amperes</b> · <b>current × voltage</b></td></tr></table></div>
<div class="card" style="margin-top:8px;padding:7px 13px"><h3>🗣 Say it out loud</h3>
<div style="font-size:10.8px;line-height:1.45"><b>Friend:</b> "How do solar panels actually make electricity?"<br>
<b>You:</b> A solar cell is two slices of crystal with a built-in one-way slope where they meet. A packet of light knocks an electron loose, the slope pushes it to one side, and it has to go round through the wire to get back. That flow is the current. The best space cells stack three layers for three colours and turn about 30% of the light into power. And sunlight thins out with distance squared, so at Jupiter you need panels the size of buses.</div></div></div>
</div></div>'''

vocab = [("Space power system", "everything that makes, stores and hands out electricity on a spacecraft.", ""),
("Solar array / solar panel", "many solar cells wired together.", ""),
("Solar cell (photovoltaic cell)", "one unit that turns light into electricity.", ""),
("Solar flux", "sunlight power landing on each square metre, in W/m².", "How hard it is raining light."),
("Solar radiation", "the light and other electromagnetic waves from the Sun.", "Repeat."),
("Watt (W) / W/m²", "unit of power / power per square metre.", ""),
("Astronomical unit (AU)", "the Earth–Sun distance: 150 million km.", ""),
("Inverse-square law", "twice as far, a quarter as much.", "Repeat, Section 5."),
("Deployable array", "panels folded for launch and opened in space.", ""),
("Body-mounted array", "cells fixed to the spacecraft's own skin.", ""),
("Deploy", "to unfold or release.", ""),
("Interplanetary", "between planets.", "Repeat."),
("Photovoltaics", "making electricity directly from light.", ""),
("Photon", "one packet of light.", "Repeat, Section 5."),
("Electron", "the tiny negative particle that carries electric current.", "Repeat."),
("Semiconductor", "a material, such as silicon, that conducts electricity a little.", ""),
("n-type", "semiconductor with spare electrons (negative carriers).", ""),
("p-type", "semiconductor with missing electrons (positive 'holes').", ""),
("Hole", "a gap where an electron is missing. It behaves like a positive charge.", ""),
("Junction (p–n junction)", "the boundary between the n and p layers.", "The one-way slope."),
("Bond / escape the bond", "an electron held in place by its atom / being knocked free.", ""),
("Circuit", "the closed loop that current flows round.", "Repeat."),
("Electrical current", "the flow of electrons, in amperes.", "Repeat."),
("Voltage (volts)", "electrical push.", "Repeat."),
("Power = voltage × current", "watts = volts × amperes.", ""),
("Efficiency", "useful power out ÷ power in, as a percentage.", "Repeat."),
("Wavelength", "the size of a light wave; it sets the colour and the photon's energy.", "Repeat."),
("Multi-junction / triple-junction cell", "two or more / three cells stacked, each for a different colour.", ""),
("Gallium arsenide (GaAs)", "the semiconductor family used in the best space cells.", ""),
("Upper / intermediate / lower cell", "the three layers: short, medium and long wavelengths.", ""),
("Band gap", "the energy needed to free an electron in a given material.", ""),
("Temperature effect", "hot cells give lower voltage and so less power.", ""),
("Thermal cycle", "one round of heating in sunlight and cooling in shadow.", ""),
("Eclipse / shadow", "the part of the orbit where the planet blocks the Sun.", "Repeat."),
("Degradation", "slow loss of performance with age and radiation.", "Repeat, Section 2."),
("Juno / Rosetta / Philae", "solar-powered Jupiter orbiter / comet orbiter / its small lander.", "Repeat, Who's Who."),
("CubeSat", "a tiny satellite with cells on its faces.", "Repeat.")]
p4 = f'''<div class="page">{top(T("VOCABULARY"),'Every word used, <span>in plain English</span>',f'{len(vocab)} entries. "Repeat" = you have met it before.')}
<div class="gl2" style="font-size:10.4px;line-height:1.36">{"".join(f"<div><b>{esc(a)}</b> — {esc(b)}{(' <i>'+esc(c)+'</i>') if c else ''}</div>" for a,b,c in vocab)}</div></div>'''
write('s7-l1.html', [p1, p2, p3, p4])
print('ok', len(vocab))
