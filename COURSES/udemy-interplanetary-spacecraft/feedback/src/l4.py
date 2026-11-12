from lib import *
B = "SEC 4 · LEC 4 · NUCLEAR THERMAL ROCKETS"
T = lambda x: B.replace("NUCLEAR THERMAL ROCKETS", x)
svg = '''<svg width="100%" height="428" viewBox="0 0 330 412" style="display:block" font-family="Verdana, sans-serif">
<defs><marker id="ar" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#111"/></marker>
<pattern id="hat" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" stroke="#111" stroke-width="1"/></pattern></defs>
<text x="8" y="13" font-size="10" font-weight="bold" fill="#111">1 · NUCLEAR THERMAL ROCKET</text>
<text x="160" y="44" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#111">REACTOR CORE</text>
<ellipse cx="50" cy="90" rx="40" ry="28" fill="#fff" stroke="#111" stroke-width="1.8"/>
<text x="50" y="87" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#111">LIQUID</text>
<text x="50" y="98" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#111">HYDROGEN</text>
<line x1="90" y1="90" x2="100" y2="90" stroke="#111" stroke-width="1.8"/>
<circle cx="108" cy="90" r="8" fill="#fff" stroke="#111" stroke-width="1.5"/><text x="108" y="93" text-anchor="middle" font-size="8" font-weight="bold" fill="#111">P</text>
<line x1="116" y1="90" x2="126" y2="90" stroke="#111" stroke-width="1.8" marker-end="url(#ar)"/>
<rect x="128" y="52" width="64" height="76" fill="url(#hat)" stroke="#111" stroke-width="2"/>
<path d="M192,60 L212,84 Q244,62 276,54" fill="none" stroke="#111" stroke-width="2.2"/>
<path d="M192,120 L212,96 Q244,118 276,126" fill="none" stroke="#111" stroke-width="2.2"/>
<text x="250" y="93" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#111">NOZZLE</text>
<g stroke="#111" stroke-width="1.2"><line x1="282" y1="62" x2="320" y2="56" marker-end="url(#ar)"/><line x1="282" y1="76" x2="322" y2="74" marker-end="url(#ar)"/><line x1="282" y1="90" x2="323" y2="90" marker-end="url(#ar)"/><line x1="282" y1="104" x2="322" y2="106" marker-end="url(#ar)"/><line x1="282" y1="118" x2="320" y2="124" marker-end="url(#ar)"/></g>
<text x="10" y="134" font-size="8" fill="#111">20 K (−253 °C)</text>
<text x="128" y="142" font-size="8" fill="#111">hot uranium, no flame</text>
<text x="128" y="153" font-size="8" fill="#111">heats the gas to ~2,700 K</text>
<text x="322" y="142" text-anchor="end" font-size="8.5" font-weight="bold" fill="#111">hydrogen gas out</text>
<text x="322" y="153" text-anchor="end" font-size="8.5" font-weight="bold" fill="#111">~9 km/s</text>
<line x1="8" y1="164" x2="322" y2="164" stroke="#bbb" stroke-width="1"/>
<text x="8" y="179" font-size="10" font-weight="bold" fill="#111">2 · WHY THE MILEAGE DOUBLES</text>
<g font-size="8.5" fill="#111">
<rect x="8" y="186" width="152" height="74" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="84" y="200" text-anchor="middle" font-weight="bold">CHEMICAL exhaust</text>
<circle cx="34" cy="230" r="14" fill="#ddd" stroke="#111" stroke-width="1.5"/><text x="34" y="234" text-anchor="middle" font-size="10" font-weight="bold">18</text>
<text x="56" y="219">steam: heavy</text><text x="56" y="232">3,500 K</text><text x="56" y="245">4.4 km/s · 450 s</text>
<rect x="170" y="186" width="152" height="74" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="246" y="200" text-anchor="middle" font-weight="bold">NUCLEAR exhaust</text>
<circle cx="194" cy="230" r="7" fill="#ddd" stroke="#111" stroke-width="1.5"/><text x="194" y="233" text-anchor="middle" font-size="7.5" font-weight="bold">2</text>
<text x="212" y="219">hydrogen: light</text><text x="212" y="232">2,700 K (cooler!)</text><text x="212" y="245">8.8 km/s · 900 s</text>
</g>
<text x="165" y="276" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">light molecules fly faster: vₑ ∝ √(T ÷ M)</text>
<line x1="8" y1="286" x2="322" y2="286" stroke="#bbb" stroke-width="1"/>
<text x="8" y="301" font-size="10" font-weight="bold" fill="#111">3 · THE THREE FAMILIES</text>
<line x1="46" y1="398" x2="46" y2="312" stroke="#111" stroke-width="1.3" marker-end="url(#ar)"/>
<line x1="46" y1="398" x2="320" y2="398" stroke="#111" stroke-width="1.3" marker-end="url(#ar)"/>
<text x="8" y="322" font-size="8" fill="#111">push</text><text x="248" y="410" font-size="8" fill="#111">mileage (Isp)</text>
<circle cx="76" cy="326" r="6" fill="#111"/><text x="88" y="329" font-size="8.5" font-weight="bold" fill="#111">CHEMICAL 450 s</text>
<circle cx="112" cy="346" r="6" fill="#fff" stroke="#111" stroke-width="2"/><text x="124" y="349" font-size="8.5" font-weight="bold" fill="#111">NUCLEAR ~900 s (never flown)</text>
<circle cx="292" cy="388" r="6" fill="#111"/><text x="282" y="385" text-anchor="end" font-size="8.5" font-weight="bold" fill="#111">ELECTRIC 3,000+ s</text>
</svg>'''
p1 = spread(B, 'A kettle <span>with no fire</span>', 'S4 / L4 — Nuclear thermal rockets', svg,
 "hatched box = reactor core · Ⓟ = pump · number in circle = how heavy the exhaust molecule is · ● flown · ○ never flown",
 ["1. A reactor, not a fire, heats hydrogen; the nozzle does the rest.",
  "2. Light exhaust is fast exhaust: Isp ~900 s, twice chemical, with real thrust.",
  "3. Ground-tested in the 1960s, never flown: cost, politics, radiation."],
 ['What heats the propellant in a nuclear thermal rocket?', 'Path of the hydrogen, tank to exhaust?', 'Isp compared with chemical? Why?',
  'What sets the temperature limit?', 'Why is it attractive for Mars?', 'What is payload?', 'Low-enriched uranium: what and why?',
  'Why has it never flown?', 'The two examples: what are they really?', '<span class="hl b">? is it hotter than a chemical rocket</span>'],
 ['<span class="hl y">nuclear thermal rocket</span> (NTR): a <span class="hl y">reactor</span> heats the propellant; nothing burns',
  'liquid hydrogen → pump → reactor (heated, <span class="hl k">~2,700 K</span>) → nozzle (expands, pressure ↓, speed ↑) → thrust',
  'Isp ≈ <span class="hl k">2×</span> chemical (~900 s vs 450 s) · and still high thrust',
  'why: exhaust is light hydrogen, not heavy steam (<span class="hl o">not</span> because it is hotter)',
  'limit = what the reactor <span class="hl y">materials</span> can stand',
  '2× Isp → about half the mass for the same trip, or 2–3× the <span class="hl y">payload</span>',
  '<span class="hl y">payload</span> = the useful cargo: instruments, cameras, crew',
  'Mars: faster trip → <span class="hl g">less radiation exposure</span> for the crew',
  '<span class="hl y">low-enriched uranium</span> (LEU): safer to build and test, fewer security rules, cheaper',
  'ground-tested <span class="hl k">1960s</span> · politics + cost → <span class="hl o">never flown</span>',
  'theory: fuel mixed into the fluid (liquid / gas core) → hotter → higher Isp',
  'examples: bimodal NTR (drawing only) · Project Orion (really nuclear <span class="hl o">pulse</span>: bombs)'])

p2 = f'''<div class="page">{top(T("TEACH"),'Not hotter. <span>Lighter.</span>','Simple story first, then the official names, then how it actually works with numbers you can check.')}
<div class="eli"><b style="font-size:14px">🧒 Like you're 5</b><br>
A normal rocket heats its gas by burning it. A nuclear rocket is a kettle with no fire. Inside is a block of special metal, uranium, that gets scorching hot all by itself when its atoms split. The engine squirts the lightest gas there is, hydrogen, through holes in that hot block. The gas comes out blazing and shoots through the same bell nozzle as before.<br>
Why is that better? Throw a ping-pong ball and a bowling ball with the same arm: the ping-pong ball leaves much faster. The fire in a chemical rocket makes steam, which is the bowling ball. A reactor doesn't need to burn anything, so it can throw plain hydrogen, the ping-pong ball. Same kind of heat, twice the exhaust speed, twice the mileage, and it still pushes hard. The catch: the hot block is radioactive, the engine is heavy, and nobody has ever flown one. They ran on test stands in the Nevada desert in the 1960s.</div>
<div class="two">
<div class="card" style="padding:9px 13px"><h3>🏷 The official names (name first, then what it means)</h3>
<ul class="names">
<li><b>Nuclear thermal propulsion, NTP</b> (<b>nuclear thermal rocket, NTR</b>; solid-core nuclear rocket): a fission reactor heats a propellant that leaves through a nozzle.</li>
<li><b>Nuclear fission</b>: a heavy atom (uranium-235) splitting in two and releasing heat. A <b>reactor</b> keeps that going at a controlled rate. A <b>fuel element</b> is one of the rods that holds the uranium; together they are the <b>reactor core</b>.</li>
<li><b>Working fluid</b> (here the same thing as the propellant): the hydrogen that gets heated and thrown. Three different words now: <b>nuclear fuel</b> is the uranium, <b>propellant</b> is the hydrogen, and nothing is "fuel" in the burning sense.</li>
<li><b>Molecular mass, M</b> (molar mass): how heavy one molecule of the exhaust is. Hydrogen 2, steam 18.</li>
<li><b>Enrichment</b>: the share of uranium that is the splittable kind, U-235. <b>Low-enriched uranium, LEU</b>: under 20%. <b>Highly enriched, HEU</b>: 20% and up; weapons grade is about 90%.</li>
<li><b>Payload</b>: the part of the spacecraft that is the reason for the trip. <b>Payload fraction</b>: its share of the total mass.</li>
<li><b>Bimodal nuclear thermal rocket</b>: one reactor, two jobs. Thrust during burns, electricity the rest of the time.</li>
<li><b>Liquid-core / gas-core nuclear rocket</b>: the slide's "mixing nuclear fuel and the working fluid". Paper designs only.</li>
<li><b>Nuclear pulse propulsion</b> (Project Orion): riding a string of small nuclear explosions. Not a thermal rocket.</li>
<li><b>Radiation exposure</b> (dose): how much damaging radiation a crew absorbs. A <b>shadow shield</b> sits between reactor and crew.</li>
</ul></div>
<div class="card" style="padding:9px 13px"><h3>🛠 How it actually works</h3>
<table class="mech"><tr><th style="width:74px">Step</th><th>The mechanism, with numbers (the 1960s NERVA engine)</th></tr>
<tr><td><b>1 · The heat source</b></td><td>Splitting 1 kg of uranium-235 releases about 80 million MJ. Burning 1 kg of hydrogen and oxygen releases 13. Six million times more, so energy is never the limit.</td></tr>
<tr><td><b>2 · Flow path</b></td><td>Liquid hydrogen at 20 K → turbopump → channels in the nozzle wall (cooling it) → down through hundreds of holes in the hot core → out as gas at about <b>2,700 K</b> → throat → bell.</td></tr>
<tr><td><b>3 · Why it is faster</b></td><td>Exhaust speed goes as √(T ÷ M). Chemical: 3,500 K ÷ 13.6 (steam with spare hydrogen). Nuclear: 2,700 K ÷ 2. Ratio of the square roots ≈ 2.3. The reactor is <i>cooler</i> and still wins, because its exhaust is seven times lighter.</td></tr>
<tr><td><b>4 · The two numbers</b></td><td>vₑ ≈ 8.3 km/s, so Isp = 8,300 ÷ 9.81 ≈ <b>850 s</b> (NERVA measured 841 s). Thrust <b>246,000 N</b>, about 25 tonnes of push.</td></tr>
<tr><td><b>5 · Check it</b></td><td>ṁ = F ÷ vₑ = 246,000 ÷ 8,300 ≈ 30 kg of hydrogen per second. Jet power = ½ṁvₑ² ≈ 1,000 MW. The reactor was rated 1,100 MW. It adds up.</td></tr>
<tr><td><b>6 · What it buys</b></td><td>Leaving Earth orbit for Mars needs about 4 km/s. Rocket equation: at 450 s the ship is 60% propellant; at 900 s it is 36%. Spend the saving on payload, or on speed for a shorter trip.</td></tr>
<tr><td><b>7 · The limits</b></td><td>The core must stay solid, so about 2,700–2,900 K at most. Hot hydrogen eats the fuel rods. Liquid hydrogen is 14 times less dense than water: huge tanks. Reactor and shield weigh tonnes: thrust is only 3–4 times the engine's weight, against 70–180 for chemical.</td></tr>
<tr><td><b>8 · History</b></td><td>US Project Rover and NERVA, 1955–1973: about 20 reactors run in Nevada. In 1969 one engine was started 28 times. Cancelled when the Mars plans were. Never flown.</td></tr></table></div>
</div></div>'''

p3 = f'''<div class="page">{top(T("FACT CHECK"),'Three real errors <span>in this lecture</span>','This lecture has more wrong statements than any so far. The first three change what you would say to a friend.')}
<div class="two">
<div>
<div class="card" style="padding:8px 13px;border-color:var(--orange)"><h3>⛔ Wrong, and worth getting right</h3>
<ul class="r" style="font-size:10.9px">
<li><b>"Very high specific impulse since the working temperatures are higher."</b> A nuclear core runs <i>cooler</i> than a chemical flame (2,700 K against 3,500 K), because the fuel rods must not melt. The Isp doubles because the exhaust is light hydrogen and not heavy steam. He half-remembers the rule ("the square root of the temperature"). The full rule is √(temperature ÷ molecular mass).</li>
<li><b>"NASA's ORION nuclear project… developed in 1986… nuclear thermal rockets."</b> Three errors. Project Orion ran <b>1958–1965</b>, led by a company (General Atomics) for the US military. It is <b>not a thermal rocket</b>: the ship drops small nuclear bombs behind itself and rides the blasts on a giant plate with shock absorbers. That is exactly what his own slide diagram labels: pusher, shock absorbers, propellant magazines. The 1963 treaty banning nuclear explosions in space killed it. And it has nothing to do with today's Orion crew capsule.</li>
<li><b>"It is also attractive for interstellar flight."</b> No. A nuclear thermal rocket gives perhaps 10–20 km/s. The nearest star is 40 trillion km away: at Voyager's 17 km/s that is <b>75,000 years</b>. It is an engine for reaching Mars, not other stars.</li></ul></div>
<div class="card" style="margin-top:10px;padding:8px 13px"><h3>🔎 Caption errors</h3>
<table class="t" style="font-size:10px"><tr><th>Captions said</th><th>Instructor meant</th></tr>
<tr><td>"nuclear them a rocket / rock edge"</td><td>nuclear <b>thermal rocket(s)</b></td></tr>
<tr><td>"on the QM state of the art… react to development"</td><td>the <b>current</b> state of the art… <b>reactor</b> development</td></tr>
<tr><td>"specific import" · "lift of mass" · "tripped"</td><td>specific <b>impulse</b> · <b>lift-off</b> mass · <b>tripled</b></td></tr>
<tr><td>"radiation explosion"</td><td>radiation <b>exposure</b> (slide: "exposition")</td></tr>
<tr><td>"hitting some kind of liquid"</td><td><b>heating</b> some kind of liquid</td></tr>
<tr><td>"knotholes"</td><td><b>nozzles</b></td></tr>
<tr><td>"Nysa… by mode on nuclear rocket"</td><td><b>NASA</b>… <b>bimodal</b> nuclear rocket</td></tr>
<tr><td>"NASA's Arrian nuclear project"</td><td>the <b>Orion</b> nuclear project</td></tr>
<tr><td>"nuclear production / proportion"</td><td>nuclear <b>propulsion</b></td></tr></table></div></div>
<div><div class="card" style="padding:8px 13px"><h3>▲ Where else he was loose</h3>
<ul class="r" style="font-size:10.7px">
<li><b>"First proposed and sketched in the 1960s… some prototypes."</b> Proposed in the 1940s. By the 1960s the US had built and run about 20 reactors at full power. It was far more than sketched.</li>
<li><b>"Right now it's 2018."</b> The lecture is eight years old. Since then NASA and DARPA started a flight demo (DRACO, 2023) and cancelled it in 2025, as far as I know.</li>
<li><b>"The required lift-off mass is half."</b> Nobody plans to lift off from the ground on one: too heavy for its thrust, and radioactive. It is a stage you start in orbit. The honest version: the mass you must put <i>into Earth orbit</i> for a Mars trip roughly halves.</li>
<li><b>"The liquid at high temperature… high velocity liquid."</b> It goes in as liquid at 20 K and is a gas long before it reaches 2,700 K. Liquids don't expand through nozzles.</li>
<li><b>"We all know what happens if we cannot withstand some nuclear reaction."</b> A reactor cannot explode like a bomb. The real failure is fuel rods cracking or melting.</li>
<li><b>"A dispute among the scientific community."</b> The physics isn't disputed; it was demonstrated. The obstacles are cost, testing (the exhaust is radioactive) and public acceptance.</li>
<li><b>"Low-enriched uranium… promoted in the European Union."</b> The switch to low-enriched fuel was NASA's own choice in the late 2010s. I don't know of a European programme he could mean.</li>
<li><b>"Mixing nuclear fuel and the working fluid."</b> These are liquid-core and gas-core designs: let the fuel melt or vaporize so temperature is no longer capped. Isp of 1,500 to 5,000 s on paper. None has been built.</li></ul></div>
<div class="card" style="margin-top:10px;padding:8px 13px"><h3>📒 Question bank cards</h3>
<ul class="r" style="font-size:10.8px">
<li>A nuclear rocket runs cooler than a chemical one. Why is its Isp double?</li>
<li>Trace the hydrogen from tank to exhaust.</li>
<li>Nuclear fuel, propellant, working fluid: which is which here?</li>
<li>Why would a crew to Mars want one? Give two reasons.</li>
<li>Project Orion: what was it really, and why did it end?</li></ul></div></div>
</div></div>'''

vocab = [("Nuclear propulsion", "using a nuclear reactor (or explosions) as an engine's energy source.", "Repeat, L1."),
("Nuclear thermal rocket (NTR) = nuclear thermal propulsion (NTP)", "a reactor heats hydrogen, which leaves through a nozzle.", "Kettle with no fire."),
("Nuclear fission", "a heavy atom splitting in two and releasing a lot of heat.", ""),
("Uranium / U-235", "the heavy metal used as nuclear fuel / the kind of uranium atom that splits easily.", ""),
("Nuclear reactor", "a machine that keeps fission going at a steady, controlled rate.", ""),
("Reactor core / fuel element", "the hot heart of the reactor / one of the rods that holds the uranium.", ""),
("Nuclear fuel", "the uranium. It is not burned and not thrown out.", "Not the same as rocket fuel."),
("Working fluid", "the substance that is heated and expanded to do the work. Here hydrogen, which is also the propellant.", ""),
("Liquid hydrogen (LH₂)", "hydrogen chilled to 20 K. Very light, very bulky.", "Repeat, L2."),
("Efficiency / exceptional efficiency", "here: high specific impulse, a lot of Δv per kilo of propellant.", "Repeat."),
("Specific impulse (Isp)", "exhaust speed ÷ 9.81, in seconds. NTR: about 850–900 s.", "Repeat."),
("Working temperature", "how hot the gas gets inside the engine.", ""),
("Square root (√)", "the number that, multiplied by itself, gives the original. √4 = 2.", ""),
("Molecular mass (M)", "how heavy one molecule is, on a scale where hydrogen gas is 2 and water is 18.", "Ping-pong ball against bowling ball."),
("Proportional to (∝)", "'goes up and down together with'.", ""),
("Theoretical", "worked out on paper, not built.", ""),
("Liquid-core / gas-core rocket", "designs where the uranium itself is molten or gas and mixed with the propellant. Hotter, never built.", ""),
("Withstand", "survive without breaking or melting.", ""),
("Material properties", "what a material can take: melting point, strength, resistance to attack.", ""),
("Interplanetary / interstellar", "between planets / between stars. The second is thousands of times farther.", ""),
("State of the art", "the best that current technology can do.", ""),
("Prototype / model", "a first working version built for testing / a mock-up or a calculation.", ""),
("Lift-off mass", "the total mass of the rocket as it leaves the pad.", ""),
("Payload", "the cargo that is the reason for the mission: instruments, cameras, crew.", ""),
("Payload fraction", "the share of the total mass that is payload. Usually a few percent.", ""),
("Radiation exposure (dose)", "how much harmful radiation a person absorbs. In deep space it comes from the Sun and the galaxy.", ""),
("Enrichment", "raising the share of U-235 in uranium. Natural uranium has 0.7%.", ""),
("Low-enriched uranium (LEU)", "under 20% U-235. Cannot be made into a bomb easily, so fewer security rules.", ""),
("Highly enriched uranium (HEU)", "20% U-235 and up. The 1960s engines used about 93%.", ""),
("Security regulations", "the legal controls on who may handle bomb-grade material.", ""),
("Budget / schedule", "the money / the timeline.", ""),
("Turbine pump = turbopump", "the pump that forces hydrogen into the reactor.", "Repeat, L2."),
("Nozzle / expand / pressure", "the bell that turns pressure and heat into speed.", "Repeat, L2."),
("Fluid", "anything that flows: liquid or gas. The exhaust here is a gas.", "Repeat."),
("Bimodal", "two modes: the same reactor gives thrust and electricity.", ""),
("Artist's concept", "a painting of something that does not exist yet.", ""),
("Nuclear pulse propulsion", "propelling a ship with a series of nuclear explosions behind a pusher plate.", "Project Orion."),
("Pusher plate / shock absorber", "the thick plate that takes each blast / the springs that smooth the kick.", ""),
("Shadow shield", "a slab between the reactor and the crew that blocks its radiation.", ""),
("Project Rover / NERVA", "the US nuclear rocket programme, 1955–1973.", "Who's Who."),
("Project Orion (1958–1965)", "the US nuclear pulse study. Not the Orion crew capsule.", "Who's Who."),
("DRACO", "the cancelled NASA and DARPA flight demo of the 2020s.", "Who's Who.")]
p4 = f'''<div class="page">{top(T("VOCABULARY"),'Every word used, <span>in plain English</span>',f'{len(vocab)} entries. "Repeat" = you have met it before.')}
<div class="gl2" style="font-size:10.2px;line-height:1.34">{"".join(f"<div><b>{esc(a)}</b> — {esc(b)}{(' <i>'+esc(c)+'</i>') if c else ''}</div>" for a,b,c in vocab)}</div></div>'''

c1 = ("NUCLEAR THERMAL ROCKET", "NTR · NTP", "a reactor heats hydrogen; a nozzle throws it", "fire caps exhaust at 4.5 km/s. A reactor needs no burning, so it can throw the lightest gas there is", "~2,700 K · 8.3 km/s · Isp ~850 s · 246,000 N (NERVA)", "RTG (electricity only) · nuclear pulse", "vₑ ∝ √(T ÷ M) · never flown")
c2 = ("MOLECULAR MASS (M)", "—", "how heavy one exhaust molecule is", "at the same heat, light molecules move faster, so light exhaust means high Isp", "hydrogen 2 · steam 18 · exhaust speed ∝ √(T ÷ M)", "the propellant's total mass", "why NTR doubles Isp while running cooler")
c3 = ("PAYLOAD", "—", "the cargo that is the reason for the trip", "everything else (engines, tanks, propellant) exists only to move it; better Isp frees mass for it", "Mars departure: 60% propellant at 450 s, 36% at 900 s", "the whole spacecraft", "rocket equation · payload fraction")
c4 = ("ENRICHMENT", "LEU · HEU", "share of uranium that is splittable U-235", "more U-235 = smaller reactor, but bomb-grade material means heavy security and cost", "natural 0.7% · LEU < 20% · 1960s engines 93%", "radioactivity level (different thing)", "fission · reactor core · budget + schedule")
cA, a1, a2 = cardpage(c1, c2, "C22", "scene 10"); cB, b1, b2 = cardpage(c3, c4, "C23", "scene 10")
p5 = f'''<div class="page">{top(T("COPY INTO NOTES"),'Where each piece goes <span>in the notebook</span>','Routes A to D for this lecture. Section 4 ends here, so route B is now the full sentence for the Section 4 map page.')}
<div class="two route">
<div class="card" style="padding:9px 13px"><h3>A · Equations &amp; key numbers page (p3–4)</h3>
<div class="copy">vₑ ∝ √(T ÷ M)      hot + LIGHT exhaust is fast
                   chemical 3,500 K ÷ 13.6 · nuclear 2,700 K ÷ 2
                   → about 2× the exhaust speed
nuclear thermal    Isp ~850–900 s · 246,000 N · 30 kg/s H₂
                   1,100 MW reactor (NERVA, 1960s)
Mars departure     4 km/s: 60% propellant at 450 s
                           36% propellant at 900 s</div>
<h3>B · Section 4 map page (write it now, from memory first)</h3>
<div class="copy">S4 · propulsion: throw mass back → F = ṁ × vₑ
S4 · chemical: burn → throat → bell; big ṁ, Isp 250–450 s
S4 · electric: ionize → grids → neutralize; mg/s, Isp 3,000+ s
S4 · nuclear: reactor heats H₂ (light = fast); Isp ~900 s,
     never flown
S4 · the trade: push vs mileage; energy from propellant /
     solar panels / reactor</div>
<h3>D · Question bank ("but how?" cards)</h3>
<div class="copy">Q: A nuclear core is cooler than a flame. Why is Isp double?
A: vₑ ∝ √(T ÷ M). Exhaust is H₂ (mass 2), not steam (18).
Q: How does the hydrogen get hot with nothing burning?
A: It flows through holes in a core heated by uranium fission.
Q: Why not launch from the ground with it?
A: Engine too heavy for its thrust (3–4× its weight) and
   radioactive. It is started in orbit.
Q: What was Project Orion?
A: Nuclear PULSE: bombs behind a pusher plate. 1958–1965.</div></div>
<div class="card" style="padding:9px 13px"><h3>C · One-line word bank (new lines)</h3>
<div class="copy">p__ · nuclear thermal rocket = NTR / NTP · reactor heats H₂  → C22
p__ · fission · heavy atom splits, releases heat
p__ · reactor / reactor core · controlled fission / its hot heart
p__ · fuel element · rod that holds the uranium
p__ · nuclear fuel vs propellant · uranium (stays) vs H₂ (thrown)
p__ · working fluid · what gets heated + expanded: H₂
p__ · molecular mass (M) · how heavy one molecule is  → C22
p__ · payload · the cargo the trip is for  → C23
p__ · payload fraction · payload ÷ total mass
p__ · lift-off mass · total mass leaving the pad
p__ · enrichment · share of U-235 in the uranium  → C23
p__ · LEU / HEU · under 20% / 20% and up (bomb-grade ~90%)
p__ · radiation exposure = dose · radiation a crew absorbs
p__ · shadow shield · slab between reactor and crew
p__ · bimodal NTR · one reactor: thrust + electricity
p__ · liquid-core / gas-core · molten or gas fuel; paper only
p__ · nuclear pulse propulsion · ride bomb blasts (Orion)
p__ · interstellar · between stars; NOT reachable this way</div>
<div style="font-size:10.5px;margin-top:4px"><b>Fix one earlier card:</b> in Lecture 1's question bank I wrote "Same heat, lighter exhaust" for nuclear. Change "Same heat" to "<b>Cooler than a flame, but</b>". Lecture 1's PDF is reissued as v2 with that corrected.</div></div>
</div></div>'''
p6 = f'''<div class="page">{top(T("CONCEPT CARDS"),'Route E: <span>pages C22 and C23</span>','Two notebook pages, two cards each. Copy line for line; the faint numbers are your ruled lines.')}
<div style="display:flex;gap:16px;justify-content:center">{cA}{cB}</div>
<div style="text-align:center;font-size:10.5px;color:#444;margin-top:6px">C22: {a1} + {a2} lines of 22 · C23: {b1} + {b2} lines of 22</div></div>'''
p7 = f'''<div class="page">{top(T("SAY IT OUT LOUD"),'Last page: <span>prove it by talking</span>','After the spread and the 3-line summary, with everything closed. Section 4 is complete after this, so the Section 4 talk is now in the app.')}
<div class="two"><div>
<div class="card"><h3>🗣 The friend's opening question</h3><div style="font-size:13px;line-height:1.5">"A nuclear rocket? So it's basically a bomb going off behind the ship?"</div></div>
<div class="card" style="margin-top:12px"><h3>✅ Three sentences you should be able to say</h3><ul class="r" style="font-size:12px">
<li>No, it's a kettle with no fire. A reactor gets hot, you blow hydrogen through it, and the hot gas goes out an ordinary rocket nozzle.</li>
<li>It gets about twice the mileage of the best chemical rocket, and the reason isn't that it is hotter. It is that the exhaust is plain hydrogen, the lightest gas, and light molecules fly faster.</li>
<li>It worked on test stands in the 1960s but has never flown, because it is heavy, radioactive, expensive to test and politically hard.</li></ul></div>
<div class="card" style="margin-top:12px"><h3>❓ Follow-ups a friend might ask</h3><ul class="r" style="font-size:12px">
<li>"Why would anyone want one?" (half the propellant for a Mars trip, or a faster trip and less radiation for the crew)</li>
<li>"Could it get us to another star?" (no: tens of thousands of years even at its best)</li>
<li>"Wasn't there one that did use bombs?" (Project Orion, 1958–1965, never built)</li>
<li>"Is that what powers Voyager?" (no, that is an RTG: electricity only)</li>
<li>"Which engine is best, then?" (none: chemical for push, electric for mileage, nuclear would sit in between)</li></ul></div></div>
<div><div class="card" style="min-height:3.2in"><h3>📝 Your explanation (paste or dictate)</h3><div style="border:2px dashed #999;border-radius:8px;height:2.5in;padding:8px;color:#999;font-size:11px">_ send it to me in chat; I'll put it here _</div></div>
<div class="card" style="margin-top:12px;min-height:2.2in;border-color:var(--green)"><h3 style="color:var(--green)">🎯 My read</h3><div style="border:2px dashed #999;border-radius:8px;height:1.5in;padding:8px;color:#999;font-size:11px">solid on: _<br>fuzzy on: _<br>fix: _<br>→ question-bank cards: _</div></div>
<div class="callout" style="margin-top:12px;font-size:11.5px">⚡ Section 4 done. Before Section 5: the Section 4 map page from memory, then one timed Section 4 talk from the app's Teach tab.</div></div></div></div>'''
write('s4-l4.html', [p1, p2, p3, p4, p5, p6, p7])
print('ok', a1, a2, b1, b2, len(vocab))
