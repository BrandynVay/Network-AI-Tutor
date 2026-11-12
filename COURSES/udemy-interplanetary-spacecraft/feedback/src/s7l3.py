import math
from lib import *
B = "SEC 7 · LEC 3 · RADIOISOTOPE GENERATORS (RTG)"
T = lambda x: B.replace("RADIOISOTOPE GENERATORS (RTG)", x)
fins = "".join('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#111" stroke-width="2.2"/>' % (
    72 + 40 * math.cos(a), 180 + 40 * math.sin(a), 72 + 54 * math.cos(a), 180 + 54 * math.sin(a)) for a in [i * math.pi / 4 for i in range(8)])
spokes = "".join('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#111" stroke-width="0.9" stroke-dasharray="3 2"/>' % (
    72 + 14 * math.cos(a), 180 + 14 * math.sin(a), 72 + 38 * math.cos(a), 180 + 38 * math.sin(a)) for a in [math.pi / 8 + i * math.pi / 4 for i in range(8)])
curve = " ".join("%.1f,%.1f" % (40 + 2.6 * t, 330 - 44 * 0.5 ** (t / 87.7)) for t in range(0, 101, 5))
svg = f'''<svg width="100%" height="428" viewBox="0 0 330 412" style="display:block" font-family="Verdana, sans-serif">
<defs><marker id="ar" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#111"/></marker>
<pattern id="hat" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" stroke="#111" stroke-width="1"/></pattern></defs>
<text x="8" y="13" font-size="10" font-weight="bold" fill="#111">1 · A LUMP THAT HEATS ITSELF (decay)</text>
<circle cx="42" cy="56" r="22" fill="#ddd" stroke="#111" stroke-width="1.6"/><text x="42" y="54" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#111">Pu-238</text><text x="42" y="65" text-anchor="middle" font-size="7" fill="#111">plutonium</text>
<line x1="68" y1="56" x2="100" y2="56" stroke="#111" stroke-width="1.6" marker-end="url(#ar)"/>
<circle cx="124" cy="56" r="20" fill="#fff" stroke="#111" stroke-width="1.6"/><text x="124" y="54" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#111">U-234</text><text x="124" y="65" text-anchor="middle" font-size="7" fill="#111">uranium</text>
<line x1="58" y1="74" x2="76" y2="88" stroke="#111" stroke-width="1.1" marker-end="url(#ar)"/><circle cx="83" cy="93" r="5" fill="#fff" stroke="#111" stroke-width="1.4"/>
<text x="92" y="97" font-size="8" fill="#111">α particle</text>
<g font-size="8.5" fill="#111"><text x="158" y="40">α particle = 2 protons + 2 neutrons</text><text x="158" y="53">it stops inside the fuel → <tspan font-weight="bold">HEAT</tspan></text><text x="158" y="66">1 gram gives 0.57 W of heat</text><text x="158" y="79">half the atoms gone in 87.7 years</text><text x="158" y="92">nothing to switch on or off</text></g>
<line x1="8" y1="104" x2="322" y2="104" stroke="#bbb" stroke-width="1"/>
<text x="8" y="117" font-size="10" font-weight="bold" fill="#111">2 · HEAT → ELECTRICITY (Seebeck effect)</text>
<circle cx="72" cy="180" r="40" fill="#fff" stroke="#111" stroke-width="1.8"/>{fins}{spokes}
<circle cx="72" cy="180" r="13" fill="#999" stroke="#111" stroke-width="1.6"/>
<text x="72" y="246" text-anchor="middle" font-size="8" fill="#111">hot fuel in the middle</text><text x="72" y="257" text-anchor="middle" font-size="8" fill="#111">cold shell with fins</text>
<rect x="160" y="146" width="22" height="48" fill="url(#hat)" stroke="#111" stroke-width="1.5"/><text x="171" y="141" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#111">HOT</text>
<line x1="182" y1="152" x2="268" y2="152" stroke="#111" stroke-width="3.2"/><line x1="182" y1="188" x2="268" y2="188" stroke="#111" stroke-width="3.2" stroke-dasharray="6 3"/>
<text x="225" y="146" text-anchor="middle" font-size="8" fill="#111">material A</text><text x="225" y="202" text-anchor="middle" font-size="8" fill="#111">material B</text>
<text x="246" y="173" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#111">COLD</text>
<path d="M268,152 H300 V162" fill="none" stroke="#111" stroke-width="1.4"/><rect x="286" y="162" width="28" height="16" rx="3" fill="#fff" stroke="#111" stroke-width="1.4"/><text x="300" y="173" text-anchor="middle" font-size="7.5" font-weight="bold" fill="#111">load</text><path d="M300,178 V188 H268" fill="none" stroke="#111" stroke-width="1.4"/>
<g font-size="8.5" fill="#111"><text x="160" y="220">hot end + cold end → a voltage</text><text x="160" y="232">only about 6% becomes electricity</text><text x="160" y="244">the rest leaves through the fins</text><text x="160" y="256">no moving parts</text></g>
<line x1="8" y1="263" x2="322" y2="263" stroke="#bbb" stroke-width="1"/>
<text x="8" y="276" font-size="10" font-weight="bold" fill="#111">3 · IT FADES SLOWLY</text>
<line x1="40" y1="330" x2="40" y2="281" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/><line x1="40" y1="330" x2="312" y2="330" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
<polyline points="{curve}" fill="none" stroke="#111" stroke-width="2.2"/>
<line x1="40" y1="308" x2="268" y2="308" stroke="#111" stroke-width="0.8" stroke-dasharray="3 3"/><line x1="268" y1="308" x2="268" y2="330" stroke="#111" stroke-width="0.8" stroke-dasharray="3 3"/>
<g font-size="8" fill="#111"><text x="36" y="290" text-anchor="end">100%</text><text x="36" y="311" text-anchor="end">50%</text><text x="40" y="341" text-anchor="middle">0</text><text x="268" y="341" text-anchor="middle">88 years</text>
<text x="318" y="276" text-anchor="end">Galileo: 290 W → 250 W in 14 years</text><text x="48" y="323">Voyager: 470 W in 1977, about 220 W now</text></g>
<line x1="8" y1="346" x2="322" y2="346" stroke="#bbb" stroke-width="1"/>
<text x="8" y="358" font-size="10" font-weight="bold" fill="#111">4 · WHICH POWER WHERE</text>
<g font-size="8.5" fill="#111"><text x="8" y="370"><tspan font-weight="bold">SOLAR ARRAY</tspan>  near the Sun, out to Jupiter</text><text x="8" y="381"><tspan font-weight="bold">BATTERY</tspan>  through the shadow</text><text x="8" y="392"><tspan font-weight="bold">RTG</tspan>  far from the Sun, or dark for weeks (Pluto, Mars night)</text></g>
<text x="165" y="406" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">an RTG is not a reactor and not an engine</text>
</svg>'''
p1 = spread(B, 'The rock that <span>stays warm</span>', 'S7 / L3 — RTGs', svg,
 "big circle = atom · small circle = α particle · grey = hot · solid bar = material A · dashed bar = material B · curve = power left",
 ["1. Plutonium-238 decays by itself and the decay makes heat.",
  "2. Hot inside, cold outside: thermocouples turn about 6% into electricity.",
  "3. Works anywhere, for decades. Used where sunlight is too weak."],
 ['What does RTG stand for?', 'What do Voyager 1 and New Horizons have in common?', 'Where does the heat come from?', 'What does Pu-238 decay into?',
  'How does heat become electricity?', 'What are the fins for?', 'How long does it last?', 'Why is it controversial?',
  'Is it a nuclear reactor?', 'Galileo\'s RTG: the numbers?', '<span class="hl b">? why plutonium-238 and not another</span>'],
 ['<span class="hl y">RTG</span> = radioisotope thermal (thermoelectric) generator',
  'Voyager 1 + New Horizons: no solar panels → very far from the Sun → RTGs',
  'heat from the <span class="hl y">natural decay</span> of <span class="hl y">plutonium-238</span> → uranium-234 + an <span class="hl y">alpha particle</span> (2 protons + 2 neutrons)',
  '<span class="hl y">Seebeck effect</span>: two different materials, one end hot, one end cold → a voltage',
  'hot centre, cold outside · <span class="hl y">fins</span> keep the outside cold',
  'power does <span class="hl g">not depend on the Sun</span>',
  'lasts decades (slide: up to 100 years) · fades as the plutonium decays',
  'expensive · plutonium is <span class="hl o">controversial</span> · NASA uses it, ESA rarely',
  '<span class="hl o">NOT a nuclear reactor</span>: natural decay, no fission chain',
  'Galileo\'s: <span class="hl k">290 W</span> new → <span class="hl k">250 W</span> at end · 55 kg · 7.5 kg Pu-238 · 114 cm long'])

p2 = f'''<div class="page">{top(T("TEACH"),'Power for where <span>the Sun doesn\'t reach</span>','Simple story first, then the official names, then how it actually works with numbers you can check.')}
<div class="eli"><b style="font-size:14px">🧒 Like you're 5</b><br>
Imagine a lump of metal that is hot to the touch and stays hot for a hundred years with nothing plugged in. Plutonium-238 is that lump. Its atoms are unstable: one by one, each spits out a tiny piece of itself, and every spit is a little kick of heat. A fresh pellet glows red by itself. Nobody starts it and nobody can stop it.<br>
Now the trick for getting electricity. Join two different materials, heat one end and keep the other end cold, and a small voltage appears between the cold ends. So you wrap hundreds of these little pairs around the hot lump and put cooling fins on the outside. That is the whole machine: no moving parts, nothing to wear out. It works in the dark, in a dust storm, at Pluto. The catches: only about 6% of the heat becomes electricity, the plutonium is rare and radioactive so launching it is a political fight, and the power slowly fades as the lump uses itself up. Voyager has been running on three of them since 1977.</div>
<div class="two">
<div class="card" style="padding:9px 13px"><h3>🏷 The official names (name first, then what it means)</h3>
<ul class="names" style="font-size:10.6px">
<li><b>Radioisotope thermoelectric generator, RTG</b> (the slide's "thermal generator"; nuclear battery): makes electricity from the heat of radioactive decay.</li>
<li><b>Radioisotope</b> (radioactive isotope): a version of an element whose atoms are unstable. <b>Radioactive decay</b>: an unstable nucleus changing by itself and releasing energy.</li>
<li><b>Alpha decay</b>: decay by throwing out an <b>alpha particle</b> (α; a helium nucleus: 2 protons + 2 neutrons).</li>
<li><b>Half-life</b>: the time for half the atoms to decay. Plutonium-238: 87.7 years.</li>
<li><b>Plutonium-238, Pu-238</b>: the usual fuel, used as a ceramic, plutonium dioxide. It decays to <b>uranium-234</b>.</li>
<li><b>Seebeck effect</b> (thermoelectric effect): a temperature difference across two joined materials produces a voltage.</li>
<li><b>Thermocouple</b> (in an RTG, a <b>unicouple</b>): one such pair. <b>Hot junction</b>, <b>cold junction</b>. Material: silicon-germanium.</li>
<li><b>General purpose heat source, GPHS</b>: the protective brick that holds the fuel pellets.</li>
<li><b>Radiator fins</b>: carry the waste heat away so the outside stays cold.</li>
<li><b>Thermal power</b> (heat, watts-thermal) versus <b>electrical power</b> (watts-electric). <b>BOL / EOL</b>: beginning of life / end of life.</li>
<li><b>Nuclear reactor</b>: a machine that runs a controlled <b>fission chain reaction</b>. An RTG is not one.</li>
<li><b>Radioisotope heater unit, RHU</b>: a small pellet used only to keep equipment warm.</li>
</ul></div>
<div class="card" style="padding:9px 13px"><h3>🛠 How it actually works</h3>
<table class="mech" style="font-size:9.9px"><tr><th style="width:66px">Step</th><th>The mechanism, with numbers (Galileo's RTG, from the slide)</th></tr>
<tr><td><b>1 · Decay</b></td><td>A plutonium-238 nucleus (94 protons, 144 neutrons) throws out an alpha particle and becomes uranium-234 (92 and 142). Count them: 94 − 2, 144 − 2.</td></tr>
<tr><td><b>2 · Heat</b></td><td>The alpha particle is stopped inside the fuel within a hair's width, and its energy turns into heat. One gram gives 0.57 W. Galileo's 7.5 kg: about <b>4,300 W</b> of heat. The fuel sits near 1,000 °C.</td></tr>
<tr><td><b>3 · Seebeck</b></td><td>Heat makes the charge carriers in a material drift from the hot end to the cold end. Two different materials drift by different amounts, so joining them at the hot end leaves a voltage between the cold ends. 572 pairs in series give about 30 V.</td></tr>
<tr><td><b>4 · Efficiency</b></td><td>Hot side about 1,000 °C, cold side about 300 °C. 290 W of electricity from 4,300 W of heat: <b>6.7%</b>. The other 4,000 W leaves through the fins (and helps keep the spacecraft warm).</td></tr>
<tr><td><b>5 · Fading</b></td><td>Power = starting power × 0.5^(years ÷ 87.7). That is 0.8% a year. Galileo flew 14 years: 0.5^(14 ÷ 87.7) = 0.895, so 290 W → 260 W from decay alone. The thermocouples age too, which gives the slide's <b>250 W</b>.</td></tr>
<tr><td><b>6 · Voyager</b></td><td>470 W at launch in 1977. About 220 W today, as far as I know, so instruments are being switched off one at a time.</td></tr>
<tr><td><b>7 · Why this isotope</b></td><td>Alpha particles are stopped by a sheet of paper, so almost no shielding is needed. And 88 years is long enough for a mission but short enough to be hot. Strontium-90 (29 years) needs heavy shielding. Americium-241 (432 years) gives a fifth of the heat per gram.</td></tr>
<tr><td><b>8 · Safety</b></td><td>The fuel is ceramic pellets clad in iridium inside graphite shells built to survive a launch accident and re-entry. Apollo 13's is lying intact on the floor of the Pacific. Plutonium-238 is not bomb material; that is plutonium-239.</td></tr></table></div>
</div></div>'''

p3 = f'''<div class="page">{top(T("COMPARE + FACT CHECK"),'Three ways to keep <span>the lights on</span>','Section 7 in one table, then where the instructor was loose, the caption errors, and the say-it-out-loud script.')}
<div class="card" style="padding:7px 13px;margin-bottom:8px"><h3>📋 The power sources side by side</h3>
<table class="mech" style="font-size:10.3px"><tr><th>Source</th><th>Energy comes from</th><th>Typical power</th><th>Lasts</th><th>Use it when</th><th>The catch</th></tr>
<tr><td><b>Solar array</b></td><td>sunlight</td><td>100s of W to 100,000+ W</td><td>15+ years, fading 1–3% a year</td><td>anywhere from Mercury to Jupiter</td><td>nothing in shadow; huge beyond Mars</td></tr>
<tr><td><b>Secondary battery</b></td><td>stored from the array</td><td>the whole spacecraft, for an hour</td><td>thousands of cycles</td><td>every eclipse</td><td>stores, does not make; heavy</td></tr>
<tr><td><b>Primary battery</b></td><td>its own chemicals, once</td><td>W to kW for hours</td><td>one use</td><td>pyro, short-lived probes</td><td>cannot be recharged</td></tr>
<tr><td><b>RTG</b></td><td>decay heat of plutonium-238</td><td>100–300 W each</td><td>decades, fading 0.8% a year</td><td>beyond Jupiter; long nights; dust</td><td>6% efficient; costly; scarce fuel; politics</td></tr></table>
<div style="font-size:10.3px;margin-top:3px">RTG users: Voyager 1 and 2, Galileo, Cassini, New Horizons, and the Mars rovers Curiosity and Perseverance (for the dust and the nights, not the distance).</div></div>
<div class="two">
<div><div class="card" style="padding:7px 13px"><h3>▲ Where the instructor was loose</h3>
<ul class="r" style="font-size:10.3px">
<li><b>The name.</b> His slides say radioisotope <i>thermal</i> generator. The proper name is radioisotope <b>thermoelectric</b> generator.</li>
<li><b>"They can last up to 500 years."</b> His own slide says 100. The honest answer: the heat halves every 87.7 years and the thermocouples age as well, so useful life is decades. Voyager is at 49 years and running short.</li>
<li><b>"One point fifty metres long."</b> His slide says 114 cm.</li>
<li><b>"Temperature is ejected from the nucleus."</b> A particle is ejected. It is stopped inside the fuel and its energy of motion becomes heat.</li>
<li><b>"Really only applicable for space."</b> The Soviet Union powered hundreds of remote lighthouses with strontium-90 units, and early heart pacemakers ran on plutonium-238.</li>
<li><b>"ESA is developing strontium."</b> As far as I know, the European programme is built on americium-241. Strontium-90 was the Soviet ground choice.</li>
<li><b>Only for "very far from the Sun".</b> Also for long darkness and dust: the Mars rovers, and the Apollo instruments that had to survive two-week lunar nights.</li>
<li><b>"New Horizons took a few poor photos of Pluto."</b> Probably the captions. It returned sharp close-ups of Pluto in 2015.</li>
<li><b>Not said: the efficiency (about 6%)</b>, and that an RTG cannot be turned off. It is hot on the launch pad and has to be cooled there.</li>
<li><b>He was right</b> that it is not a reactor: no chain reaction, no fission, nothing to control. And this is the "RTG is not an engine" point from Section 4.</li></ul></div></div>
<div><div class="card" style="padding:7px 13px"><h3>🔎 Caption errors</h3>
<table class="t" style="font-size:9.7px"><tr><th>Captions said</th><th>Instructor meant</th></tr>
<tr><td>"radio isotope with more generators"</td><td>radioisotope <b>thermal</b> generators</td></tr>
<tr><td>"apart from the intent"</td><td>apart from the <b>antenna</b></td></tr>
<tr><td>"far apart from soccer"</td><td>far from the <b>Sun</b></td></tr>
<tr><td>"the five to one"</td><td><b>Voyager 1</b></td></tr>
<tr><td>"plutonium to 3:8"</td><td>plutonium-<b>238</b></td></tr>
<tr><td>"the case time to uranium… not a particle"</td><td><b>decays into</b> uranium… <b>an alpha</b> particle</td></tr>
<tr><td>"to newsrooms and to printers"</td><td><b>two neutrons and two protons</b></td></tr>
<tr><td>"X thermic"</td><td><b>exothermic</b> (gives off heat)</td></tr>
<tr><td>"Seabeck", "seabag", "C-PAC effect"</td><td><b>Seebeck</b> effect</td></tr>
<tr><td>"occult material", "Hunter called Hellmann's"</td><td><b>a cold</b> material, <b>hot and cold elements</b></td></tr>
<tr><td>"a strong team"</td><td><b>strontium</b></td></tr>
<tr><td>"loan to date on RTG needs"</td><td><b>long debate</b> on RTGs</td></tr>
<tr><td>"regarding Cephalopoda"</td><td>regarding <b>RTGs</b></td></tr></table></div>
<div class="card" style="margin-top:8px;padding:7px 13px"><h3>🗣 Say it out loud</h3>
<div style="font-size:10.8px;line-height:1.45"><b>Friend:</b> "How does Voyager still have power after fifty years with no solar panels?"<br>
<b>You:</b> It carries lumps of plutonium-238, which is naturally hot because its atoms keep breaking down. Around the hot lump are hundreds of little pairs of two materials: hot on one end, cold on the other, and that difference makes a voltage. No moving parts, works in total darkness. It is not a reactor, just natural decay. It only turns about 6% of the heat into electricity and it loses a bit under 1% a year, which is why Voyager is now switching instruments off.</div></div></div>
</div></div>'''

vocab = [("Radioisotope thermoelectric generator (RTG)", "a device that turns the heat of radioactive decay into electricity.", "A rock that stays warm, wrapped in heat-to-electricity strips."),
("Radioisotope", "a form of an element whose atoms are unstable and break down by themselves.", ""),
("Isotope", "one version of an element; versions differ in their number of neutrons.", ""),
("Radioactive decay / natural decay", "an unstable atom changing into another by itself, releasing energy.", ""),
("Spontaneous", "happening by itself, with no trigger.", ""),
("Nucleus", "the tiny heavy centre of an atom, made of protons and neutrons.", ""),
("Proton / neutron", "the positive / neutral particles in the nucleus.", ""),
("Plutonium-238 (Pu-238)", "the radioisotope used as RTG fuel. Half-life 87.7 years.", ""),
("Uranium-234 (U-234)", "what plutonium-238 turns into.", ""),
("Alpha particle (α)", "two protons and two neutrons thrown out together: a helium nucleus.", "Stopped by a sheet of paper."),
("Half-life", "the time it takes for half the atoms to decay.", ""),
("Exothermic", "giving off heat.", ""),
("Seebeck effect (thermoelectric effect)", "a voltage produced by a temperature difference across two joined materials.", ""),
("Thermocouple / junction", "a pair of different materials joined together / the place they join.", ""),
("Hot / cold side", "the end against the fuel / the end against the finned shell.", ""),
("Fins (radiator fins)", "thin plates that throw away waste heat so the outside stays cold.", "Repeat idea, Section 2."),
("Voltage", "electrical push.", "Repeat."),
("Watt (W)", "unit of power.", "Repeat."),
("BOL / EOL", "beginning of life / end of life: power when new and when the mission ends.", ""),
("Interplanetary / interstellar", "between planets / between stars.", "Repeat."),
("Controversial", "argued over.", "Repeat."),
("Strontium-90 / americium-241", "other radioisotopes that can fuel such generators.", ""),
("Nuclear reactor", "a machine that splits atoms in a controlled chain reaction.", "Repeat, Section 4."),
("Fission / fusion", "splitting heavy atoms / joining light ones. An RTG does neither.", ""),
("Chain reaction", "each split atom triggering more splits.", ""),
("Shielding", "material placed to stop radiation.", ""),
("Heat source (GPHS)", "the protective brick holding the plutonium pellets.", ""),
("Multi-foil insulation", "layers of thin foil that keep the heat going through the thermocouples.", "Like MLI, Section 2."),
("Voyager 1", "launched 1977; now beyond the Sun's bubble, in interstellar space.", "Repeat, Who's Who."),
("New Horizons", "the Pluto probe; one RTG.", "Repeat, Who's Who."),
("Galileo", "NASA's Jupiter orbiter of the 1990s; two RTGs.", "Repeat, Who's Who."),
("NASA / ESA", "the US and European space agencies.", "Repeat.")]
p4 = f'''<div class="page">{top(T("VOCABULARY"),'Every word used, <span>in plain English</span>',f'{len(vocab)} entries. "Repeat" = you have met it before.')}
<div class="gl2" style="font-size:10.6px;line-height:1.4">{"".join(f"<div><b>{esc(a)}</b> — {esc(b)}{(' <i>'+esc(c)+'</i>') if c else ''}</div>" for a,b,c in vocab)}</div></div>'''
write('s7-l3.html', [p1, p2, p3, p4])

# ---------------- whole-course review (2 pages)
rows = [
 ("1 · Mission design", "An orbit is falling and missing. Low is fast and sharp; one exact height hangs still over the equator.", "LEO 400 km: 92 min, 7.7 km/s · GEO 35,786 km", "\"36,000 km from the centre\" (that is the altitude)"),
 ("2 · Space environment", "The air did five jobs for you: sunscreen, pressure, damper, fan, ground wire. Space does none.", "atomic oxygen rules 200–600 km", "\"atomic oxygen appears at 320 km\""),
 ("3 · Orbital mechanics", "Six numbers describe any orbit. The lazy half-ellipse is cheapest; a flyby steals speed from a planet.", "Mars: 259 days, window every 26 months", "\"Lambert takes the Δv and gives the time\" (reversed)"),
 ("4 · Propulsion", "Every engine throws mass backward. Chemical pushes hard and is thirsty; electric is gentle and efficient; nuclear never flew.", "F = ṁ × vₑ · Isp 450 s / 3,000 s / 900 s", "\"nuclear is efficient because it is hotter\" (lighter exhaust)"),
 ("5 · Communications", "Write the message on a radio wave, aim it with a dish, send it through the radio window, land louder than the noise.", "c = λ × f · Cassini: 20 W, 10⁻¹⁶ W received", "\"a dish adds power\" · \"k is about wavelength\""),
 ("6 · Attitude control", "Sense, compare, twist, forever. Gyros drift and stars fix them. Wheels swap spin; jets and magnets remove it.", "star tracker 0.001° · Hubble 0.007 arcsec", "\"Explorer 1 failed\" · \"inertia = mass in a direction\""),
 ("7 · Power", "A sunlight sandwich near the Sun, a bucket for the dark, a warm rock where the Sun doesn't reach.", "1,361 W/m² at Earth · cells 30% · Pu-238 87.7 years", "\"three layers = 3× efficiency\" · \"RTGs last 500 years\""),
]
tr = "".join(f"<tr><td><b>{esc(a)}</b></td><td>{esc(b)}</td><td>{esc(c)}</td><td>{esc(d)}</td></tr>" for a, b, c, d in rows)
r1 = f'''<div class="page">{top("SPACE X · WHOLE COURSE · v1","All seven sections <span>on one page</span>","One sentence to say, one number to know, and one thing the instructor said that you should not repeat. If you can say the middle column from memory, you can hold the conversation.")}
<div class="card" style="padding:9px 14px"><table class="mech" style="font-size:13px;line-height:1.38"><tr><th style="width:130px">Section</th><th>Say this</th><th style="width:210px">Number to know</th><th style="width:230px">Don't repeat</th></tr>{tr}</table></div>
<div class="callout" style="margin-top:9px;font-size:13px">The thread: a spacecraft has to do everything for itself. <b>Get there</b> (1, 3, 4) · <b>survive</b> (2) · <b>talk</b> (5) · <b>point</b> (6) · <b>stay powered</b> (7).</div>
<div class="two" style="margin-top:10px">
<div class="card" style="padding:8px 13px"><h3>The four formulas worth carrying</h3><div style="font-size:12.6px;line-height:1.55"><b>F = ṁ × vₑ</b> · thrust = mass thrown per second × exhaust speed<br><b>c = λ × f</b> · wavelength × frequency = speed of light<br><b>P = flux × area × efficiency</b> · solar array power<br><b>battery = load × shadow time ÷ depth of discharge</b></div></div>
<div class="card" style="padding:8px 13px"><h3>The one idea that repeats three times</h3><div style="font-size:12.6px;line-height:1.5"><b>Twice as far = a quarter as much.</b> It is why gravity weakens with height (Section 1), why a radio signal fades (Section 5) and why sunlight fades (Section 7). Anything that spreads out over a sphere does this.</div></div></div></div>'''
r2 = f'''<div class="page">{top("SPACE X · PLAN FOR TOMORROW","About three hours, <span>in five blocks</span>","Sections 1–3 you have rehearsed before. Sections 4–7 you have only copied. So the time goes to 4–7, and most of it to saying things out loud.")}
<div class="two">
<div class="card" style="padding:10px 14px"><h3>The blocks</h3>
<table class="mech" style="font-size:13.6px;line-height:1.45"><tr><th style="width:74px">Time</th><th>Do this</th></tr>
<tr><td><b>40 min</b></td><td><b>Read.</b> For each of the 12 lectures in Sections 4–7: the "Like you're 5" box and the "Where the instructor was loose" list. Nothing else. About 3 minutes each.</td></tr>
<tr><td><b>40 min</b></td><td><b>Quiz.</b> App → Quiz → new questions. Scenes 8 to 19. Every miss, read the explanation out loud.</td></tr>
<tr><td><b>45 min</b></td><td><b>Talk.</b> App → Teach. Section 4, 5, 6 and 7 talks, once each, timer running, cue card hidden after the first minute. Send me any one of them.</td></tr>
<tr><td><b>20 min</b></td><td><b>Whole course.</b> App → Teach → Whole course, twice. The second time, no cue card.</td></tr>
<tr><td><b>20 min</b></td><td><b>Quiz 5</b> in Udemy (designing a solar array), using the recipe on the right.</td></tr></table>
<div style="font-size:13.4px;margin-top:10px;line-height:1.55"><b>If you only have one hour:</b> the page before this one, then the whole-course talk twice, then the Section 4–7 "loose" lists.<br><b>If it is a test, not a talk:</b> swap the talk block for a second quiz block and the Numbers tab.</div></div>
<div><div class="card" style="padding:10px 14px"><h3>Recipe for Quiz 5: size a solar array</h3>
<div style="font-size:13.6px;line-height:1.6"><b>1.</b> Sunlight per m² = 1,361 ÷ (distance in AU)².<br><b>2.</b> Usable per m² = that × efficiency × any loss factor they give.<br><b>3.</b> Area = power needed ÷ usable per m².<br><b>4.</b> If there is a battery to refill, add its recharge power to "power needed" first.<br><b>Example:</b> 500 W at Mars, 30% cells, no other losses. 1,361 ÷ 1.52² = 590. 590 × 0.30 = 177 W per m². 500 ÷ 177 = <b>2.8 m²</b>.</div></div>
<div class="card" style="margin-top:10px;padding:10px 14px"><h3>What is still open</h3>
<div style="font-size:13.6px;line-height:1.6">You have not explained anything back to me since Section 3. That is 16 lectures of copying with no check. One talk sent tomorrow is worth more than re-reading everything.<br><br>Paused during the push, yours to ask for afterwards: concept-card pages for Sections 6–7, the copy-into-notes pages, and the Who's Who names for Sections 6–7.</div></div></div>
</div></div>'''
write('review.html', [r1, r2])
print('ok', len(vocab))
