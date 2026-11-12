from lib import *
B="SEC 4 · LEC 2 · CHEMICAL ENGINES (ROCKETS)"
T=lambda x:B.replace("CHEMICAL ENGINES (ROCKETS)",x)
svg='''<svg width="100%" height="428" viewBox="0 0 330 412" style="display:block" font-family="Verdana, sans-serif">
<defs><marker id="ar" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#111"/></marker>
<pattern id="hat" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" stroke="#111" stroke-width="1"/></pattern></defs>
<text x="8" y="13" font-size="10" font-weight="bold" fill="#111">1 · LIQUID-PROPELLANT CHEMICAL ENGINE</text>
<text x="252" y="30" text-anchor="end" font-size="8.5" font-weight="bold" fill="#111">THROAT: narrowest, Mach 1</text>
<line x1="207" y1="34" x2="207" y2="84" stroke="#777" stroke-width="0.8"/>
<path d="M30,44 H150 V146 H30 Q8,95 30,44 z" fill="#fff" stroke="#111" stroke-width="1.4"/>
<ellipse cx="66" cy="68" rx="27" ry="15" fill="#fff" stroke="#111" stroke-width="1.8"/>
<text x="66" y="71" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#111">FUEL</text>
<ellipse cx="66" cy="122" rx="32" ry="15" fill="#fff" stroke="#111" stroke-width="1.8"/>
<text x="66" y="125" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#111">OXIDIZER</text>
<line x1="93" y1="68" x2="112" y2="68" stroke="#111" stroke-width="1.8"/>
<circle cx="120" cy="68" r="8" fill="#fff" stroke="#111" stroke-width="1.5"/><text x="120" y="71" text-anchor="middle" font-size="8" font-weight="bold" fill="#111">P</text>
<path d="M128,68 H160 V82" fill="none" stroke="#111" stroke-width="1.8" marker-end="url(#ar)"/>
<line x1="98" y1="122" x2="112" y2="122" stroke="#111" stroke-width="1.8" stroke-dasharray="4 3"/>
<circle cx="120" cy="122" r="8" fill="#fff" stroke="#111" stroke-width="1.5"/><text x="120" y="125" text-anchor="middle" font-size="8" font-weight="bold" fill="#111">P</text>
<path d="M128,122 H160 V108" fill="none" stroke="#111" stroke-width="1.8" stroke-dasharray="4 3" marker-end="url(#ar)"/>
<rect x="150" y="83" width="36" height="24" fill="url(#hat)" stroke="#111" stroke-width="1.8"/>
<path d="M186,83 L207,90 Q238,66 268,58" fill="none" stroke="#111" stroke-width="2.2"/>
<path d="M186,107 L207,100 Q238,124 268,132" fill="none" stroke="#111" stroke-width="2.2"/>
<text x="244" y="98" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#111">NOZZLE</text>
<g stroke="#111" stroke-width="1.2"><line x1="274" y1="66" x2="318" y2="58" marker-end="url(#ar)"/><line x1="274" y1="81" x2="320" y2="78" marker-end="url(#ar)"/><line x1="274" y1="95" x2="321" y2="95" marker-end="url(#ar)"/><line x1="274" y1="109" x2="320" y2="112" marker-end="url(#ar)"/><line x1="274" y1="124" x2="318" y2="132" marker-end="url(#ar)"/></g>
<text x="322" y="150" text-anchor="end" font-size="8.5" font-weight="bold" fill="#111">EXHAUST, speed vₑ</text>
<line x1="176" y1="107" x2="176" y2="160" stroke="#777" stroke-width="0.8"/>
<text x="150" y="171" font-size="8.5" font-weight="bold" fill="#111">COMBUSTION CHAMBER</text>
<text x="150" y="182" font-size="8" fill="#111">burns: ~3,300 K, 100+ bar</text>
<text x="8" y="171" font-size="8" fill="#111">P = pump</text>
<text x="8" y="182" font-size="8" fill="#111">solid line = fuel · dashed = oxidizer</text>
<line x1="8" y1="192" x2="322" y2="192" stroke="#bbb" stroke-width="1"/>
<text x="8" y="207" font-size="10" font-weight="bold" fill="#111">2 · THE NOZZLE TURNS PRESSURE INTO SPEED</text>
<g font-size="8.5" fill="#111">
<rect x="8" y="216" width="92" height="50" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="54" y="230" text-anchor="middle" font-weight="bold">CHAMBER</text><text x="54" y="243" text-anchor="middle">pressure HIGH</text><text x="54" y="256" text-anchor="middle">speed LOW</text>
<line x1="102" y1="241" x2="116" y2="241" stroke="#111" stroke-width="1.5" marker-end="url(#ar)"/>
<rect x="119" y="216" width="92" height="50" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="165" y="230" text-anchor="middle" font-weight="bold">THROAT</text><text x="165" y="243" text-anchor="middle">squeezed to the</text><text x="165" y="256" text-anchor="middle">speed of sound</text>
<line x1="213" y1="241" x2="227" y2="241" stroke="#111" stroke-width="1.5" marker-end="url(#ar)"/>
<rect x="230" y="216" width="92" height="50" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="276" y="230" text-anchor="middle" font-weight="bold">BELL EXIT</text><text x="276" y="243" text-anchor="middle">pressure LOW</text><text x="276" y="256" text-anchor="middle">speed 3–4 km/s</text>
</g>
<text x="165" y="282" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">hot + squeezed gas IN → fast gas OUT</text>
<line x1="8" y1="292" x2="322" y2="292" stroke="#bbb" stroke-width="1"/>
<text x="8" y="307" font-size="10" font-weight="bold" fill="#111">3 · THE TWO NUMBERS</text>
<g fill="#111">
<rect x="8" y="314" width="152" height="80" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="84" y="328" text-anchor="middle" font-size="9" font-weight="bold">SPECIFIC IMPULSE</text>
<text x="84" y="346" text-anchor="middle" font-size="12.5" font-weight="bold">Isp = vₑ ÷ g₀</text>
<text x="84" y="360" text-anchor="middle" font-size="8.5">seconds · the mileage</text>
<text x="84" y="372" text-anchor="middle" font-size="8.5">g₀ = 9.81 m/s²</text>
<text x="84" y="385" text-anchor="middle" font-size="8.5">3,414 m/s → 348 s</text>
<rect x="170" y="314" width="152" height="80" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="246" y="328" text-anchor="middle" font-size="9" font-weight="bold">THRUST</text>
<text x="246" y="346" text-anchor="middle" font-size="12.5" font-weight="bold">F = ṁ × vₑ</text>
<text x="246" y="360" text-anchor="middle" font-size="8.5">newtons · the push</text>
<text x="246" y="372" text-anchor="middle" font-size="8.5">ṁ = kg thrown per second</text>
<text x="246" y="385" text-anchor="middle" font-size="8.5">287 × 3,414 ≈ 981,000 N</text>
</g>
<text x="165" y="408" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">chemical: Isp LOW · ṁ HUGE → thrust HUGE</text>
</svg>'''
p1=spread(B,'Fire, a squeeze, <span>and a bell</span>','S4 / L2 — Chemical engines',svg,
 "solid pipe = fuel · dashed pipe = oxidizer · hatched box = where it burns · thin arrows = exhaust · Ⓟ = pump",
 ["1. Burn fuel + oxidizer, squeeze the gas through a throat, the bell makes it fast.",
  "2. Isp = vₑ ÷ g₀ is the mileage (s). F = ṁ × vₑ is the push (N).",
  "3. Chemical: low Isp, but tonnes thrown per second, so huge thrust."],
 ['What is a chemical rocket in one line?','Why carry an oxidizer?','Path of the propellant, tank to exhaust?',
  'What does the nozzle do? Where is the gas fastest?','Isp: formula, unit, what it measures?','Thrust: formula? Two ways to raise it?',
  '"Low Isp but high thrust." How can both be true?','Solid vs liquid?','<span class="hl b">? what do the two engines in the photos burn</span>'],
 ['<span class="hl y">chemical engine</span> = <span class="hl y">reaction engine</span>: stored propellant → high-speed jet (Newton 3)',
  '<span class="hl y">propellant</span> = <span class="hl y">fuel</span> + <span class="hl y">oxidizer</span> · no air in space → bring your own oxygen · e.g. liquid hydrogen + liquid oxygen',
  'tanks → <span class="hl y">pumps</span> → <span class="hl y">combustion chamber</span> (burns, <span class="hl k">~3,300 K</span>) → <span class="hl y">throat</span> → <span class="hl y">nozzle</span>',
  'nozzle: pressure + heat → <span class="hl g">speed</span> · bell shape lets the gas expand',
  '<span class="hl y">Isp</span> = vₑ ÷ g₀ · g₀ = <span class="hl k">9.81 m/s²</span> · unit: seconds · = efficiency · higher vₑ → less propellant for the same push',
  '<span class="hl y">thrust</span> F = ṁ × vₑ · ṁ = <span class="hl y">mass flow</span>, kg per second · unit: newtons',
  'chemical: Isp <span class="hl o">low</span> (250–450 s) but ṁ huge (tonnes/s) → <span class="hl g">thrust huge</span>',
  'best thrust for the engine\'s weight · the propellant is the heavy part (~90% of a rocket)',
  '<span class="hl y">solid rocket</span>: fuel + oxidizer premixed in one block · can\'t shut off · often boosters',
  'e.g. SpaceX 2nd stage (1 engine) · Saturn V (5 engines) · both kerosene + liquid oxygen'])

p2=f'''<div class="page">{top(T("TEACH"),'A fire with <span>only one way out</span>','Simple story first, then the official names, then how it actually works with numbers you can check.')}
<div class="eli"><b style="font-size:14px">🧒 Like you're 5</b><br>
Blow up a balloon and let it go. Air squirts out the neck one way and the balloon shoots off the other way. A rocket engine is a balloon that keeps refilling itself by lighting a fire inside. A fire needs two things: something to burn (<b>fuel</b>) and oxygen. There is no air in space, so the rocket carries its own oxygen in a second tank (<b>oxidizer</b>).<br>
The fire makes gas that is very hot and very squeezed, and it has only one way out: a small hole called the <b>throat</b>, then a bell called the <b>nozzle</b>. The bell is where the magic happens. It lets the squeezed gas spread out, and as it spreads it speeds up, to about four times the speed of a rifle bullet. Two numbers describe any engine: how hard it pushes (<b>thrust</b>) and how far it gets on each kilo of propellant (<b>specific impulse</b>). A chemical rocket is a drag racer: enormous push, terrible mileage.</div>
<div class="two">
<div class="card" style="padding:9px 13px"><h3>🏷 The official names (name first, then what it means)</h3>
<ul class="names">
<li><b>Chemical rocket engine</b> (chemical propulsion): makes thrust by burning propellant and expelling the gas.</li>
<li><b>Bipropellant</b> (biprop): an engine with two propellants, a <b>fuel</b> and an <b>oxidizer</b>. The slide's diagram is one. A <b>monopropellant</b> engine uses a single liquid that breaks down on a catalyst (hydrazine).</li>
<li><b>Cryogenic propellants</b>: liquids kept very cold. <b>LH₂</b> (liquid hydrogen, −253 °C) and <b>LOX</b> (liquid oxygen, −183 °C). <b>RP-1</b> is refined kerosene, stored at room temperature.</li>
<li><b>Turbopump</b> (the slide's "pressure pump"): a turbine-driven pump that forces propellant into the chamber. Small engines skip it and push with tank pressure: <b>pressure-fed</b>.</li>
<li><b>Combustion chamber</b> (thrust chamber): where the propellants mix and burn.</li>
<li><b>de Laval nozzle</b> (converging–diverging nozzle, bell nozzle): narrows to a <b>throat</b>, then widens. Turns pressure and heat into exhaust speed.</li>
<li><b>Exhaust velocity (vₑ)</b> (the instructor's "velocity of ejection"): how fast the gas leaves.</li>
<li><b>Mass flow rate (ṁ)</b>, said "m-dot" (his "flux of propellant"): kilograms leaving per second.</li>
<li><b>Specific impulse (Isp)</b> = vₑ ÷ g₀, in seconds. <b>g₀</b> is <b>standard gravity</b>, 9.80665 m/s².</li>
<li><b>Solid rocket motor</b> (SRM): fuel and oxidizer cast together as one solid block, the <b>grain</b>.</li>
<li><b>Thrust-to-weight ratio</b>: an engine's thrust divided by its own weight.</li>
</ul></div>
<div class="card" style="padding:9px 13px"><h3>🛠 How it actually works</h3>
<table class="mech"><tr><th style="width:70px">Step</th><th>The mechanism, with numbers</th></tr>
<tr><td><b>1 · Two tanks</b></td><td>Burning is fuel joining with oxygen. Hydrogen + oxygen gives steam and 13 million joules per kg of mix. A jet plane takes its oxygen from the air; a rocket must carry it, and the oxidizer is most of the load (about 6 kg of oxygen per kg of hydrogen).</td></tr>
<tr><td><b>2 · Feed</b></td><td>The chamber is at 100+ times air pressure, so propellant has to be forced in. Each Saturn V F-1 engine had a 41 MW turbopump moving <b>2.6 tonnes every second</b>.</td></tr>
<tr><td><b>3 · Burn</b></td><td>In the chamber: about 3,300 K (hotter than steel's melting point of 1,700 K) and 100–300 bar. The gas is hot and squeezed but slow.</td></tr>
<tr><td><b>4 · Throat</b></td><td>The narrowing speeds the gas up until, at the narrowest point, it hits exactly the speed of sound (Mach 1).</td></tr>
<tr><td><b>5 · Bell</b></td><td>Past Mach 1 the rule flips: a <i>widening</i> pipe speeds the gas up. Pressure and temperature fall, speed climbs. SpaceX's Merlin Vacuum exits at <b>3.4 km/s</b>.</td></tr>
<tr><td><b>6 · Thrust</b></td><td>F = ṁ × vₑ = 287 kg/s × 3,414 m/s ≈ <b>981,000 N</b>, enough to hold up 100 tonnes.</td></tr>
<tr><td><b>7 · Isp</b></td><td>Isp = 3,414 ÷ 9.81 = <b>348 s</b>. In words: 1 kg of propellant can give 9.81 N of push (1 kg of weight) for 348 seconds.</td></tr>
<tr><td><b>8 · The ceiling</b></td><td>The energy in a kilo of propellant is fixed by chemistry. Even at 100% conversion, 13 MJ/kg gives vₑ = √(2 × 13,000,000) ≈ 5.2 km/s. Real best: 4.5 km/s, Isp about 460 s. No chemical engine will ever reach 1,000 s.</td></tr>
<tr><td><b>9 · Not melting</b></td><td>The cold fuel is piped through channels in the chamber and nozzle walls before it burns: <b>regenerative cooling</b>.</td></tr></table></div>
</div></div>'''

p3=f'''<div class="page">{top(T("NUMBERS + FACT CHECK"),'Real engines, <span>real numbers</span>','Check F = ṁ × vₑ and Isp = vₑ ÷ g₀ against real engines, then the caption errors and where the instructor was loose or wrong.')}
<div class="card" style="padding:8px 13px;margin-bottom:10px"><h3>🚀 Engines you can check the formulas on</h3>
<table class="mech" style="font-size:10.6px"><tr><th>Engine</th><th>Where</th><th>Propellants</th><th>Thrust</th><th>Isp</th><th>vₑ = Isp × 9.81</th><th>ṁ = F ÷ vₑ</th></tr>
<tr><td><b>F-1</b></td><td>Saturn V stage 1, ×5 (right photo)</td><td>kerosene (RP-1) + LOX</td><td>6,770,000 N</td><td>263 s</td><td>2.6 km/s</td><td>2,600 kg/s each</td></tr>
<tr><td><b>Merlin Vacuum</b></td><td>Falcon 9 stage 2, ×1 (left photo)</td><td>kerosene (RP-1) + LOX</td><td>981,000 N</td><td>348 s</td><td>3.4 km/s</td><td>287 kg/s</td></tr>
<tr><td><b>RS-25</b></td><td>Space Shuttle, SLS</td><td>LH₂ + LOX</td><td>2,279,000 N</td><td>452 s</td><td>4.4 km/s</td><td>514 kg/s</td></tr>
<tr><td><b>Solid booster</b></td><td>Space Shuttle, ×2</td><td>solid grain</td><td>12,500,000 N</td><td>268 s</td><td>2.6 km/s</td><td>4,700 kg/s</td></tr>
<tr><td><b>Hydrazine thruster</b></td><td>most spacecraft</td><td>hydrazine</td><td>1–22 N</td><td>225 s</td><td>2.2 km/s</td><td>grams per second</td></tr></table>
<div style="font-size:10.5px;margin-top:4px">Hydrogen gets the best mileage; kerosene and solids the worst, yet they give the biggest push. All figures rounded; F-1 and booster thrust at liftoff, the rest in vacuum.</div></div>
<div class="two">
<div><div class="card" style="padding:8px 13px"><h3>🔎 Caption errors</h3>
<table class="t" style="font-size:10.2px"><tr><th>Captions said</th><th>Instructor meant</th></tr>
<tr><td>"chemical IntoNow heat engines"</td><td>chemical <b>internal</b> heat engines</td></tr>
<tr><td>"they have no specific impulse"</td><td><b>low</b> specific impulse</td></tr>
<tr><td>"velocity of a section / rejection"</td><td>velocity of <b>ejection</b> (exhaust velocity)</td></tr>
<tr><td>"divided by zero"</td><td>divided by <b>g-zero (g₀)</b></td></tr>
<tr><td>"nine point ninety nine point eighty eight to one"</td><td><b>9.81</b> m/s²</td></tr>
<tr><td>"specific forces / specific examples"</td><td>specific <b>impulse</b></td></tr>
<tr><td>"threat / frost / thirst"</td><td><b>thrust</b></td></tr>
<tr><td>"expecting a lot of mass"</td><td><b>expelling</b> a lot of mass</td></tr>
<tr><td>"thermal specific properties… higher food"</td><td><b>thermodynamic</b> properties… <b>fluid</b></td></tr>
<tr><td>"in this cost"</td><td>in this <b>course</b></td></tr></table></div>
<div class="card" style="margin-top:10px;padding:8px 13px"><h3>📒 Question bank cards</h3>
<ul class="r" style="font-size:11px">
<li>Trace a kilo of propellant from tank to exhaust: five stops.</li>
<li>Where in the engine is pressure highest? Where is speed highest?</li>
<li>Isp 300 s. What is the exhaust velocity? What does "300 seconds" mean?</li>
<li>An engine throws 500 kg/s at 4,400 m/s. Thrust?</li>
<li>Why can't a chemical engine reach Isp 1,000 s?</li>
<li>Chamber gas is hotter than steel melts. Why doesn't the engine melt?</li></ul></div></div>
<div class="card" style="padding:8px 13px"><h3>▲ Where the instructor was loose</h3>
<ul class="r" style="font-size:10.8px">
<li><b>"They are the lightest and have the highest thrust."</b> The engines have the best thrust for their own weight (a Merlin lifts about 180 times its weight). The rocket as a whole is the heaviest option, because about 90% of it is propellant.</li>
<li><b>"The nozzle shape maximizes the pressure we get out."</b> Backwards. The nozzle <i>spends</i> pressure to buy speed. Pressure is highest in the chamber and lowest at the exit.</li>
<li><b>"It's quite common that fuel is liquid hydrogen."</b> Common on upper stages. But both engines in his photos burn <b>kerosene</b> with liquid oxygen.</li>
<li><b>"In the United States you may use different units."</b> That is the whole reason Isp is in seconds: dividing by g₀ gives the same number in metric and imperial.</li>
<li><b>"Solid rockets, usually known as boosters."</b> Solid is a propellant type; booster is a job. Solids also serve as final kick stages (New Horizons left Earth on one), and boosters can be liquid.</li>
<li><b>"Pressure pump" on the slide</b> merges two feed systems: a turbopump, or no pump and pressurized tanks.</li>
<li><b>Not said: what spacecraft themselves carry.</b> Hydrogen and oxygen boil away in days. Probes use storable propellants that can sit in tanks for 20 years: hydrazine alone, or hydrazine-family fuel with nitrogen tetroxide (Isp about 320 s). They ignite on contact, with no spark: <b>hypergolic</b>.</li>
<li><b>Not said: why the bell is so big on the second stage.</b> In vacuum the gas can keep expanding, so a longer bell extracts more speed.</li></ul></div>
</div></div>'''

vocab=[("Chemical engine / chemical rocket","an engine that makes thrust by burning propellant and throwing out the hot gas.","Balloon with a fire in it."),
("Internal heat engine","the instructor's phrase: a machine that burns fuel inside itself and turns the heat into motion.",""),
("Stored mass / propellant","everything the rocket carries to throw out. Fuel plus oxidizer.","Repeat."),
("Propulsive jet","the stream of fast gas leaving the nozzle.",""),
("Reaction engine","any engine that works by throwing mass backward (Newton's third law).","Repeat, L1."),
("Thrust (F)","the engine's push, in newtons. F = ṁ × vₑ.","Repeat, L1."),
("Overall thrust","just 'total thrust'. Nothing new.",""),
("Specific impulse (Isp)","exhaust velocity divided by g₀, in seconds. Push per kilo of propellant.","Miles per gallon."),
("Exhaust velocity (vₑ) = velocity of ejection","how fast the gas leaves the nozzle, relative to the rocket.",""),
("g₀ = standard gravity","9.80665 m/s², the pull of gravity at Earth's surface, used as a fixed constant.","A unit converter, nothing more."),
("Constant","a number that never changes. g₀ is one.",""),
("Efficiency","how much useful output you get per unit of input. For engines: Δv per kilo of propellant.",""),
("Mass flow rate (ṁ) = flux of propellant","kilograms of propellant leaving per second. Said 'm-dot'.","Repeat, L1."),
("Force / newton (N)","a push or pull / its unit. kN = thousand, MN = million.","Repeat, L1."),
("Fuel","the part of the propellant that burns: hydrogen, kerosene, hydrazine.",""),
("Oxidizer (oxidiser)","the part that supplies the oxygen: liquid oxygen, nitrogen tetroxide.","The air you brought with you."),
("Bipropellant / monopropellant","two propellants that burn together / one liquid that breaks down by itself on a catalyst.",""),
("Liquid hydrogen (LH₂)","hydrogen chilled to −253 °C. Best mileage, very bulky, boils away.",""),
("Liquid oxygen (LOX)","oxygen chilled to −183 °C. The usual oxidizer for launch rockets.",""),
("Cryogenic","stored extremely cold to stay liquid.",""),
("Kerosene / RP-1","refined jet-fuel-like liquid. Dense, room temperature, lower Isp than hydrogen.",""),
("Hypergolic / storable","propellants that ignite on contact, and keep for years in a tank.","What probes carry."),
("Hydrazine","the standard storable spacecraft propellant. Toxic. Isp about 225 s alone.",""),
("Pump / turbopump","forces propellant into the high-pressure chamber. Driven by a small turbine.",""),
("Pressure-fed","no pump: high-pressure gas in the tanks pushes the propellant out. Simple, for small engines.",""),
("Combustion / to burn","fuel joining with oxygen fast, releasing heat.",""),
("Combustion chamber","the strong can where the burning happens.",""),
("Reaction (chemical)","here: the burning itself. Not the same 'reaction' as in action–reaction.",""),
("Thermodynamic properties","the state of a gas: its temperature, pressure and density.",""),
("Fluid","anything that flows: a liquid or a gas.",""),
("Pressure / bar","how hard a gas pushes on its walls. 1 bar ≈ normal air pressure.","Repeat."),
("Throat","the narrowest point of the nozzle. Gas reaches the speed of sound there.",""),
("Nozzle","the shaped outlet that turns pressure and heat into speed.","The bell."),
("de Laval nozzle = converging–diverging nozzle = bell nozzle","narrows, then widens. Named after Gustaf de Laval, 1888.","Add to Who's Who."),
("Expand / expansion","gas spreading into more space. Its pressure and temperature drop.",""),
("Parabolic","the curved bell shape; a practical approximation of the ideal contour.",""),
("Speed of sound / Mach 1 / supersonic","how fast pressure waves travel in the gas / moving at that speed / faster than it.",""),
("Kinetic energy","energy of motion. The nozzle turns heat energy into it.","Repeat."),
("Regenerative cooling","running cold fuel through the engine walls to keep them from melting.",""),
("Solid rocket motor / grain","fuel and oxidizer cast as one rubbery block / that block. Lights once, can't be shut off.",""),
("Booster","a rocket strapped on to help at liftoff. A job, not a propellant type.",""),
("Stage / second stage / staging","a rocket section with its own engines and tanks, dropped when empty.","Repeat idea: rocket equation."),
("Thrust-to-weight ratio","thrust divided by weight. Above 1 means it can lift itself.",""),
("SpaceX / Falcon 9 / Merlin Vacuum","US rocket company / its workhorse rocket / that rocket's second-stage engine.","Add to Who's Who."),
("Saturn V / F-1","the Apollo Moon rocket (1967–1973) / its first-stage engine, the most powerful single-chamber liquid engine flown.","Add to Who's Who."),
("RS-25","the Space Shuttle main engine, hydrogen and oxygen.","Add to Who's Who.")]
p4=f'''<div class="page">{top(T("VOCABULARY"),'Every word used, <span>in plain English</span>',f'{len(vocab)} entries: the lecture\'s words plus every term I used on the other pages. "Repeat" = you have met it before.')}
<div class="gl2" style="font-size:10.1px;line-height:1.33">{"".join(f"<div><b>{esc(a)}</b> — {esc(b)}{(' <i>'+esc(c)+'</i>') if c else ''}</div>" for a,b,c in vocab)}</div></div>'''

c1=("EXHAUST VELOCITY (vₑ)","ejection speed","how fast the gas leaves the nozzle","it is the engine's quality in one number: faster exhaust = more push from every kilo","kerosene 3.4 km/s · hydrogen 4.4 · ion engine 41 · chemical max ~4.5","the ship's speed (vₑ is the GAS)","Isp = vₑ ÷ g₀ · F = ṁ × vₑ · rocket equation")
c2=("MASS FLOW RATE (ṁ)","m-dot","kg of propellant thrown out per second","thrust needs speed AND amount. ṁ is the amount; it is also how fast the tanks empty","Merlin Vacuum 287 kg/s · F-1 2,600 kg/s · ion engine mg/s","total propellant mass (ṁ is per second)","F = ṁ × vₑ · burn time = mass ÷ ṁ")
c3=("DE LAVAL NOZZLE","bell nozzle","narrows to a throat, then widens into a bell","chamber gas is hot and squeezed but slow. The nozzle trades pressure + heat for speed","Mach 1 at the throat → 3–4 km/s at the exit","a garden-hose nozzle (subsonic only)","throat · expansion · exhaust velocity")
c4=("BIPROPELLANT","fuel + oxidizer","engine that burns two propellants together","fire needs oxygen and space has none, so the rocket carries its own in a second tank","LH₂ + LOX 450 s · kerosene + LOX 350 s · hydrazine alone 225 s","monopropellant (one liquid, no burn)","combustion chamber · Isp · hypergolic")
cA,a1,a2=cardpage(c1,c2,"C18","scene 8"); cB,b1,b2=cardpage(c3,c4,"C19","scene 8")
p5=f'''<div class="page">{top(T("COPY INTO NOTES"),'Where each piece goes <span>in the notebook</span>','Routes A to D for this lecture. The concept cards (route E) are on the next page.')}
<div class="two route">
<div class="card" style="padding:9px 13px"><h3>A · Equations &amp; key numbers page (p3–4)</h3>
<div class="copy">Isp = vₑ ÷ g₀      g₀ = 9.81 m/s² · unit: seconds
                   3,414 m/s ÷ 9.81 = 348 s (Merlin Vacuum)
vₑ = Isp × g₀      452 s × 9.81 = 4.4 km/s (hydrogen engine)
F = ṁ × vₑ         287 kg/s × 3,414 m/s ≈ 981,000 N
chemical ceiling   vₑ ≈ 4.5 km/s · Isp ≈ 460 s
chamber            ~3,300 K · 100–300 bar · throat = Mach 1</div>
<h3>B · Section 4 map page (add to the sentence from L1)</h3>
<div class="copy">chemical: fuel + oxidizer burn → throat (Mach 1) → bell turns
pressure into speed; low Isp, huge ṁ → huge thrust</div>
<h3>D · Question bank ("but how?" cards)</h3>
<div class="copy">Q: How does a nozzle make gas go faster?
A: It spends pressure and heat to buy speed. Throat = Mach 1,
   then the widening bell speeds supersonic gas up further.
Q: What does "Isp = 348 s" physically mean?
A: 1 kg of propellant can give 9.81 N of thrust for 348 s.
   Same as vₑ = 348 × 9.81 = 3.4 km/s.
Q: Low Isp but high thrust. How?
A: F = ṁ × vₑ. vₑ is modest but ṁ is tonnes per second.
Q: Why doesn't the chamber melt at 3,300 K?
A: Regenerative cooling: cold fuel runs through the walls first.</div></div>
<div class="card" style="padding:9px 13px"><h3>C · One-line word bank (new lines)</h3>
<div class="copy">p__ · chemical rocket · burn propellant, throw the gas
p__ · fuel / oxidizer · what burns / the oxygen you bring
p__ · bipropellant / monopropellant · two liquids burn / one breaks down
p__ · LH₂ / LOX = liquid hydrogen / oxygen · cryogenic, best Isp
p__ · RP-1 = kerosene · dense, room temp, lower Isp
p__ · hypergolic / storable · ignite on contact, keep for years
p__ · hydrazine · spacecraft's standard propellant, ~225 s
p__ · turbopump / pressure-fed · pump forces it in / tank gas does
p__ · combustion chamber · where it burns, ~3,300 K
p__ · throat · narrowest point, Mach 1
p__ · nozzle = de Laval = bell · pressure + heat → speed
p__ · exhaust velocity (vₑ) · how fast the gas leaves
p__ · g₀ = standard gravity · 9.81 m/s², a constant
p__ · specific impulse (Isp) · vₑ ÷ g₀, seconds, mileage  → C13
p__ · regenerative cooling · fuel cools the walls first
p__ · solid rocket motor / grain · premixed block, can't shut off
p__ · booster · strap-on helper at liftoff (a job)
p__ · stage / staging · drop empty sections
p__ · thrust-to-weight ratio · thrust ÷ weight; > 1 lifts off</div>
<div style="font-size:10.5px;margin-top:4px"><b>Also:</b> on card C13 (specific impulse) add in the margin: <b>Isp = vₑ ÷ g₀ · 1 kg gives 9.81 N for Isp seconds</b>.</div></div>
</div></div>'''
p6=f'''<div class="page">{top(T("CONCEPT CARDS"),'Route E: <span>pages C18 and C19</span>','Two notebook pages, two cards each, same six-line shorthand as C1–C17. Copy line for line; the faint numbers are your ruled lines.')}
<div style="display:flex;gap:16px;justify-content:center">{cA}{cB}</div>
<div style="text-align:center;font-size:10.5px;color:#444;margin-top:6px">C18: {a1} + {a2} lines of 22 · C19: {b1} + {b2} lines of 22</div></div>'''
p7=f'''<div class="page">{top(T("SAY IT OUT LOUD"),'Last page: <span>prove it by talking</span>','After the spread and the 3-line summary, with everything closed. Send me what you said and I will grade it like a friend would.')}
<div class="two"><div>
<div class="card"><h3>🗣 The friend's opening question</h3><div style="font-size:13px;line-height:1.5">"So how does a rocket engine actually work? Isn't it just a big fire?"</div></div>
<div class="card" style="margin-top:12px"><h3>✅ Three sentences you should be able to say</h3><ul class="r" style="font-size:12px">
<li>It is a fire with only one way out. You pump fuel and oxygen into a chamber, they burn, and the hot squeezed gas has to leave through a narrow throat and a bell.</li>
<li>The bell is the clever part: it turns pressure into speed, so the gas leaves at three or four kilometres a second.</li>
<li>Two numbers describe it. Thrust is how much you throw per second times how fast, and specific impulse is the mileage. Chemical rockets push enormously hard and get poor mileage.</li></ul></div>
<div class="card" style="margin-top:12px"><h3>❓ Follow-ups a friend might ask</h3><ul class="r" style="font-size:12px">
<li>"Why two tanks?" (no air in space, so it brings its own oxygen)</li>
<li>"Why is the nozzle bell-shaped?" (the gas has to expand to speed up; past the speed of sound a widening pipe makes it faster)</li>
<li>"Why is specific impulse in seconds?" (exhaust speed divided by 9.81; it is how long a kilo can hold up a kilo)</li>
<li>"Why doesn't it melt?" (the cold fuel runs through the walls first)</li>
<li>"Can't we just build a better chemical engine?" (no: the energy per kilo is fixed by chemistry, ceiling about 460 s)</li></ul></div></div>
<div><div class="card" style="min-height:3.2in"><h3>📝 Your explanation (paste or dictate)</h3><div style="border:2px dashed #999;border-radius:8px;height:2.5in;padding:8px;color:#999;font-size:11px">_ send it to me in chat; I'll put it here _</div></div>
<div class="card" style="margin-top:12px;min-height:2.2in;border-color:var(--green)"><h3 style="color:var(--green)">🎯 My read</h3><div style="border:2px dashed #999;border-radius:8px;height:1.5in;padding:8px;color:#999;font-size:11px">solid on: _<br>fuzzy on: _<br>fix: _<br>→ question-bank cards: _</div></div>
<div class="callout" style="margin-top:12px;font-size:11.5px">⚡ Next: the rest of Section 4 (electric and nuclear engines). Send the transcript and slides when you have watched them.</div></div></div></div>'''
write('s4-l2.html',[p1,p2,p3,p4,p5,p6,p7])
print('ok',a1,a2,b1,b2,len(vocab))
