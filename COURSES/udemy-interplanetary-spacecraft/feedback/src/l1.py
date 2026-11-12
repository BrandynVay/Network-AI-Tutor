from lib import *
B="SEC 4 · LEC 1 · PROPULSION: WHAT + TYPES"
svg='''<svg width="100%" height="428" viewBox="0 0 330 412" style="display:block" font-family="Verdana, sans-serif">
<defs><marker id="ar" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#111"/></marker></defs>
<text x="8" y="13" font-size="10" font-weight="bold" fill="#111">1 · THRUST = throw mass backward</text>
<rect x="150" y="42" width="92" height="38" rx="6" fill="#fff" stroke="#111" stroke-width="2.2"/>
<text x="196" y="65" text-anchor="middle" font-size="10" font-weight="bold" fill="#111">SHIP</text>
<path d="M150,52 L130,43 L130,79 L150,70 z" fill="#ddd" stroke="#111" stroke-width="1.8"/>
<line x1="124" y1="61" x2="30" y2="61" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
<line x1="124" y1="50" x2="60" y2="42" stroke="#111" stroke-width="0.9" stroke-dasharray="3 3"/>
<line x1="124" y1="72" x2="60" y2="80" stroke="#111" stroke-width="0.9" stroke-dasharray="3 3"/>
<line x1="248" y1="61" x2="316" y2="61" stroke="#111" stroke-width="4" marker-end="url(#ar)"/>
<text x="10" y="98" font-size="9" font-weight="bold" fill="#111">ACTION</text>
<text x="10" y="110" font-size="8.5" fill="#111">gas thrown backward</text>
<text x="322" y="98" text-anchor="end" font-size="9" font-weight="bold" fill="#111">REACTION</text>
<text x="322" y="110" text-anchor="end" font-size="8.5" fill="#111">ship pushed forward</text>
<text x="165" y="129" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">It pushes on its OWN exhaust. No air needed.</text>
<text x="165" y="143" text-anchor="middle" font-size="9" fill="#111">thrust F = ṁ × vₑ  (kg thrown per second × exhaust speed)</text>
<line x1="8" y1="153" x2="322" y2="153" stroke="#bbb" stroke-width="1"/>
<text x="8" y="168" font-size="10" font-weight="bold" fill="#111">2 · TWO WAYS TO GET A Δv</text>
<circle cx="78" cy="218" r="15" fill="#ddd" stroke="#111" stroke-width="1.8"/>
<text x="78" y="221" text-anchor="middle" font-size="7" fill="#111">planet</text>
<path d="M14,246 Q78,170 150,200" fill="none" stroke="#111" stroke-width="1.8" stroke-dasharray="6 4" marker-end="url(#ar)"/>
<text x="10" y="266" font-size="9" font-weight="bold" fill="#111">SLINGSHOT (gravity)</text>
<text x="10" y="278" font-size="8.5" fill="#111">free, but the planet must be there</text>
<line x1="170" y1="178" x2="170" y2="280" stroke="#bbb" stroke-width="1"/>
<rect x="228" y="204" width="50" height="24" rx="5" fill="#fff" stroke="#111" stroke-width="2"/>
<path d="M228,210 L216,205 L216,227 L228,222 z" fill="#ddd" stroke="#111" stroke-width="1.5"/>
<line x1="212" y1="216" x2="184" y2="216" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
<line x1="282" y1="216" x2="316" y2="216" stroke="#111" stroke-width="3.5" marker-end="url(#ar)"/>
<text x="180" y="266" font-size="9" font-weight="bold" fill="#111">THRUST (engine)</text>
<text x="180" y="278" font-size="8.5" fill="#111">any time, costs propellant</text>
<line x1="8" y1="288" x2="322" y2="288" stroke="#bbb" stroke-width="1"/>
<text x="8" y="303" font-size="10" font-weight="bold" fill="#111">3 · THREE ENGINE FAMILIES</text>
<g font-size="8" fill="#111">
<rect x="8" y="310" width="100" height="100" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="58" y="324" text-anchor="middle" font-size="9" font-weight="bold">CHEMICAL</text>
<text x="13" y="339">push</text><rect x="40" y="332" width="62" height="8" fill="#888" stroke="#111" stroke-width="0.8"/>
<text x="13" y="354">mpg</text><rect x="40" y="347" width="10" height="8" fill="#888" stroke="#111" stroke-width="0.8"/>
<text x="13" y="373">burns fuel + oxidizer</text><text x="13" y="385">Isp 250–450 s</text><text x="13" y="397">launch, capture</text>
<rect x="115" y="310" width="100" height="100" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="165" y="324" text-anchor="middle" font-size="9" font-weight="bold">ELECTRIC</text>
<text x="120" y="339">push</text><rect x="147" y="332" width="3" height="8" fill="#888" stroke="#111" stroke-width="0.8"/>
<text x="120" y="354">mpg</text><rect x="147" y="347" width="62" height="8" fill="#888" stroke="#111" stroke-width="0.8"/>
<text x="120" y="373">electricity throws ions</text><text x="120" y="385">Isp ~3,000 s</text><text x="120" y="397">long cruise</text>
<rect x="222" y="310" width="100" height="100" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="272" y="324" text-anchor="middle" font-size="9" font-weight="bold">NUCLEAR</text>
<text x="227" y="339">push</text><rect x="254" y="332" width="40" height="8" fill="#888" stroke="#111" stroke-width="0.8"/>
<text x="227" y="354">mpg</text><rect x="254" y="347" width="22" height="8" fill="#888" stroke="#111" stroke-width="0.8"/>
<text x="227" y="373">reactor heats H₂</text><text x="227" y="385">Isp ~900 s</text><text x="227" y="397">never flown</text>
</g></svg>'''
p1=spread(B,'Throw something backward, <span>go forward</span>','S4 / L1 — Propulsion: what + types',svg,
 "thin arrow = exhaust · thick arrow = ship's motion · dashed = flight path · gray bar = how much · mpg = Isp",
 ["1. Orbit change = Δv: from a planet's gravity (slingshot) or from thrust.",
  "2. Thrust = Newton's 3rd law: throw mass back, ship goes forward. No air.",
  "3. Chemical strong + thirsty · electric weak + efficient · nuclear between."],
 ['Why does a spacecraft need propulsion at all?','Two ways to get a Δv?','How is thrust made? Which law?',
  '"There\'s nothing to push against in space." What\'s wrong with that?','The three engine families?',
  'Which one pushes hardest? Which gets the best mileage?','What decides which engine a mission uses?',
  '<span class="hl b">? is electric propulsion really "new"</span>'],
 ['<span class="hl y">space propulsion</span> = making thrust to change velocity → change orbit (a <span class="hl y">Δv</span>)',
  'Δv two ways: <span class="hl y">slingshot</span> (planet\'s gravity, free, planet must be in place) · <span class="hl y">thrust</span> (engine, any time, costs propellant)',
  '<span class="hl y">thrust</span> = <span class="hl y">Newton\'s 3rd law</span>: throw mass back → ship goes forward · pushes on its <span class="hl g">OWN exhaust</span>, not on air',
  '<span class="hl y">propellant</span> = the stuff you throw out the back',
  '<span class="hl y">chemical</span> (rockets): burn fuel + oxidizer · <span class="hl g">big thrust</span> · low Isp <span class="hl k">250–450 s</span>',
  '<span class="hl y">electric</span> / low-thrust: electricity throws ions very fast · tiny thrust (grams) · <span class="hl g">high Isp</span> <span class="hl k">~3,000 s</span> · runs for years',
  '<span class="hl y">nuclear</span>: reactor heats hydrogen · Isp <span class="hl k">~900 s</span> · political · ground-tested, <span class="hl o">never flown</span>',
  '<span class="hl y">requirements</span>: the mission picks the engine · launch / landing / capture → chemical · long slow cruise → electric',
  'the trade: <span class="hl o">thrust vs efficiency</span>, you can\'t max both'])

p2=f'''<div class="page">{top(B.replace("PROPULSION: WHAT + TYPES","TEACH"),'A rocket pushes on <span>its own exhaust</span>','Simple story first, then the official names, then how it actually works with numbers you can check.')}
<div class="eli"><b style="font-size:14px">🧒 Like you're 5</b><br>
Sit on a skateboard holding a bowling ball. Throw the ball <b>backward</b> as hard as you can. You roll <b>forward</b>. You didn't push on the ground or the air. You pushed on the ball, and the ball pushed back on you. That is every rocket ever built: the ball is the gas it throws out the back. Throw it faster, or throw more of it each second, and you get a bigger push. That push is called <b>thrust</b>.<br>
There are three kinds of thrower. <b>Chemical</b> is a fire hose: a huge amount of stuff, pretty fast, empty in minutes. <b>Electric</b> is a pea-shooter that fires each pea ten times faster than the hose: the push is tiny, about the weight of a few sheets of paper, but one small bag of peas lasts for years. <b>Nuclear</b> is a kettle heated by a reactor instead of a fire: it throws its steam about twice as fast as the fire hose can.</div>
<div class="two">
<div class="card" style="padding:9px 13px"><h3>🏷 The official names (name first, then what it means)</h3>
<ul class="names">
<li><b>Space propulsion</b> (spacecraft propulsion, in-space propulsion): any system that changes a spacecraft's velocity.</li>
<li><b>Thrust (F)</b>: the force an engine makes, in newtons (N). 1 N is about the weight of an apple.</li>
<li><b>Newton's third law of motion</b> (action–reaction, the reaction principle): forces come in equal and opposite pairs. The deeper rule behind it is <b>conservation of momentum</b>.</li>
<li><b>Propellant</b> (reaction mass, working fluid): the stuff thrown out. A <b>reaction engine</b> is any engine that works by throwing it.</li>
<li><b>Chemical propulsion</b> (chemical rocket; the instructor's "chemical internal heat engine"): the energy comes from burning the propellant itself.</li>
<li><b>Electric propulsion, EP</b> (low-thrust propulsion): electricity accelerates the propellant. Main kinds: the <b>ion thruster</b> (gridded ion engine) and the <b>Hall-effect thruster</b>.</li>
<li><b>Nuclear thermal propulsion, NTP</b> (nuclear thermal rocket): a fission reactor heats hydrogen. Its cousin <b>nuclear electric propulsion, NEP</b> uses a reactor to power electric thrusters.</li>
<li><b>Gravity assist</b> (slingshot, flyby, swing-by): the no-propellant way to change velocity. Repeat from Section 3.</li>
<li><b>Requirements</b>: what the mission needs the engine to do. Choosing against them is a <b>trade study</b>.</li>
</ul></div>
<div class="card" style="padding:9px 13px"><h3>🛠 How it actually works</h3>
<table class="mech"><tr><th style="width:74px">Step</th><th>The mechanism, with numbers</th></tr>
<tr><td><b>1 · Momentum is kept</b></td><td>Momentum = mass × velocity, and the total can't change. A 1,000 kg ship at rest throws 1 kg backward at 3,000 m/s. 1 × 3,000 = 999 × v, so the ship moves forward at <b>3 m/s</b>. Air appears nowhere in that sum.</td></tr>
<tr><td><b>2 · Thrust</b></td><td>Thrust is how fast you throw momentum away: <b>F = ṁ × vₑ</b>. Throw 0.1 kg every second at 3,000 m/s and F = <b>300 N</b>.</td></tr>
<tr><td><b>3 · Δv</b></td><td>a = F ÷ m = 300 ÷ 1,000 = 0.3 m/s². Burn 10 s: Δv = 3 m/s, using 1 kg. Same answer as step 1. Thrust and time build the Δv your orbit change needs.</td></tr>
<tr><td><b>4 · Why electric is weak</b></td><td>Same 300 N from 0.01 kg/s at 30,000 m/s uses ten times less propellant. But the jet's power is ½ṁvₑ²: 0.45 MW for the first, <b>4.5 MW</b> for the second. A chemical engine gets that from the fire. An electric one needs solar panels, and the whole ISS makes about 0.1–0.2 MW. So real electric thrusters run at a few kW and push with a fraction of a newton.</td></tr>
<tr><td><b>5 · Real electric</b></td><td>NASA's NEXT ion thruster (the slide photo): 6.9 kW in, <b>0.236 N</b> out (the weight of 5 sheets of paper), exhaust at 41 km/s, Isp 4,190 s. The Dawn probe took 4 days to go 0–100 km/h, then thrust for 5.9 years: total Δv <b>11.5 km/s</b> from 425 kg of xenon.</td></tr>
<tr><td><b>6 · Why nuclear wins on speed</b></td><td>Exhaust speed goes as √(temperature ÷ molecule mass). Burning hydrogen and oxygen makes steam, mass 18. A reactor heats plain hydrogen, mass 2, to about 2,700 K. That is cooler than the flame (3,500 K), but far lighter molecules fly faster: Isp ≈ <b>900 s</b> against 450 s.</td></tr>
<tr><td><b>7 · What mileage buys</b></td><td>For a 5 km/s Δv the rocket equation says: Isp 320 s needs <b>80%</b> of the ship to be propellant; Isp 3,000 s needs <b>16%</b>.</td></tr></table></div>
</div></div>'''

p3=f'''<div class="page">{top(B.replace("PROPULSION: WHAT + TYPES","COMPARE + FACT CHECK"),'Strong or efficient: <span>pick one</span>','The comparison to know cold, the caption errors, and where the instructor was loose or wrong.')}
<div class="card" style="padding:8px 13px;margin-bottom:10px"><h3>⚖️ The three families side by side</h3>
<table class="mech" style="font-size:10.6px"><tr><th>Family</th><th>Thrust</th><th>Isp</th><th>Burns for</th><th>Energy comes from</th><th>Used for</th><th>Flown?</th></tr>
<tr><td><b>Chemical</b></td><td>newtons up to millions of newtons</td><td>200–450 s</td><td>seconds to minutes</td><td>the propellant's own chemical bonds</td><td>launch, landing, capture burns, anything that must happen fast</td><td>Yes, on every mission</td></tr>
<tr><td><b>Electric</b></td><td>thousandths of a newton up to about 1 N</td><td>1,500–4,000+ s</td><td>months to years</td><td>solar panels (or a reactor)</td><td>station-keeping, orbit raising, deep-space cruise: Dawn, DART, BepiColombo, Psyche, Starlink</td><td>Yes, since 1964</td></tr>
<tr><td><b>Nuclear thermal</b></td><td>tens to hundreds of thousands of newtons</td><td>about 850–900 s</td><td>minutes to hours</td><td>a fission reactor heating hydrogen</td><td>proposed for fast crewed Mars trips</td><td>Ground tests only (NERVA, 1960s–1972)</td></tr></table></div>
<div class="two">
<div><div class="card" style="padding:8px 13px"><h3>🔎 Caption errors</h3>
<table class="t" style="font-size:10.3px"><tr><th>Captions said</th><th>Instructor meant</th></tr>
<tr><td>"tweeting definitions"</td><td><b>treating</b> definitions</td></tr>
<tr><td>"space robots"</td><td>space <b>propulsion</b></td></tr>
<tr><td>"space proportioned / reapportion / abortion"</td><td>space <b>propulsion</b> (every time)</td></tr>
<tr><td>"accelerating the spacecraft B or thrust"</td><td>accelerating the spacecraft <b>via thrust</b></td></tr>
<tr><td>"So how stressed up"</td><td>"So how is <b>thrust obtained</b>?"</td></tr>
<tr><td>"intersecting some kind of Propulsid propeller"</td><td><b>ejecting</b> some kind of <b>propellant</b></td></tr>
<tr><td>"with Sky interventions"</td><td><b>which kind of engines</b></td></tr>
<tr><td>"we want to feel"</td><td>we want to <b>fulfil</b></td></tr></table></div>
<div class="card" style="margin-top:10px;padding:8px 13px"><h3>📒 Question bank cards</h3>
<ul class="r" style="font-size:11px">
<li>A rocket in space has no air behind it. What does it push against?</li>
<li>Thrust formula, and the two ways to make thrust bigger?</li>
<li>Three engine families: rank them by thrust, then by Isp.</li>
<li>Why is electric thrust so small? (Think power.)</li>
<li>Why does a nuclear thermal rocket beat a chemical one on Isp?</li>
<li>You need to brake into Mars orbit in 30 minutes. Chemical or electric, and why?</li></ul></div></div>
<div class="card" style="padding:8px 13px"><h3>▲ Where the instructor was loose</h3>
<ul class="r" style="font-size:11px">
<li><b>"We need propulsion to increase velocity."</b> Half of it. You also need it to slow down (braking into orbit, landing) and to change direction. Δv is a change in velocity, any direction.</li>
<li><b>"Electric propulsion… I think it was already implemented in the 1980s… kind of new."</b> Wrong by two decades. Ion engines were first fired in space in <b>1964</b> (NASA's SERT-1; the Soviet Zond 2 used plasma thrusters the same year). Soviet weather satellites used Hall thrusters from 1971. Deep Space 1 (1998) was the first probe to cruise on an ion engine. Today most new communications satellites and every Starlink carry electric thrusters. It is mainstream.</li>
<li><b>"Nuclear… being developed especially by NASA right now."</b> The US built and ground-tested nuclear rockets (NERVA) until 1972. The recent NASA and DARPA flight demo, DRACO, was cancelled in 2025 as far as I know. No nuclear rocket has ever flown.</li>
<li><b>Not said: an RTG is not nuclear propulsion.</b> Voyager and New Horizons carry plutonium power packs (radioisotope thermoelectric generators). Those make electricity. They don't push anything.</li>
<li><b>Not said: the real sorting rule.</b> The three families differ in <i>where the energy comes from</i>: inside the propellant (chemical), from solar panels (electric), from a reactor (nuclear). That one idea explains the whole table above.</li>
<li><b>Not said: there are engines with no propellant at all.</b> A solar sail is pushed by sunlight. Rare, but it exists.</li>
<li><b>"Chemical internal heat engines"</b> is his own phrase. The term you will meet everywhere else is <b>chemical propulsion</b> or <b>chemical rocket</b>.</li></ul></div>
</div></div>'''

vocab=[("Space propulsion","any system that changes a spacecraft's velocity.","The spacecraft's legs."),
("Velocity","speed plus direction. Changing either one counts as a velocity change.","Repeat."),
("Delta-v (Δv)","the size of a velocity change; the currency every maneuver is priced in.","Repeat."),
("Orbit change / maneuver","a planned burn (or flyby) that moves you from one orbit to another.",""),
("Gravitational field","the region around a body where its gravity pulls on you.","Repeat."),
("Slingshot = gravity assist","swinging past a moving planet to change your speed and direction without propellant.","Repeat, scene 7."),
("Thrust (F)","the force an engine produces, in newtons.","The push."),
("Newton (N)","the unit of force. About the weight of one apple. 1 kN = 1,000 N, 1 MN = a million.",""),
("Accelerate / acceleration","to change velocity / how fast velocity changes (m/s²). a = F ÷ m.",""),
("Newton's third law","every force has an equal and opposite partner. Push the gas back, the gas pushes you forward.","Skateboard and bowling ball."),
("Action / reaction","the two halves of that pair: gas thrown back / ship pushed forward.",""),
("Momentum","mass × velocity. The total never changes unless something outside pushes.","The bookkeeping behind thrust."),
("Eject / expel","throw out. A rocket ejects propellant.",""),
("Propellant = reaction mass","the material thrown out to make thrust. Not the same word as fuel: fuel is only the part that burns.",""),
("Reaction engine","any engine that works by throwing mass backward: rockets, ion thrusters, jets.",""),
("Exhaust","the propellant after it has left the engine. Its speed is the exhaust velocity, vₑ.",""),
("Mass flow rate (ṁ, 'm-dot')","kilograms of propellant thrown out each second.",""),
("Chemical propulsion","engines whose energy comes from burning propellant. The instructor's 'chemical internal heat engines'.","Fire hose."),
("Heat engine","any machine that turns heat into motion. A rocket nozzle does exactly that.",""),
("Rocket","a reaction engine that carries everything it throws, including its own oxygen.",""),
("Liquid propellant","propellant stored as liquid in tanks, as opposed to a solid block.","Next lecture."),
("Electric propulsion (EP)","engines that use electricity to accelerate propellant. Very fast exhaust, very small thrust.","Pea-shooter."),
("Low-thrust propulsion","the family name for engines that push gently for a very long time. Mostly means electric.",""),
("Ion / ionize","an atom with an electron knocked off, so electricity can grab and fling it / to make ions.",""),
("Ion thruster (gridded ion engine)","ionizes xenon gas and fires the ions out through charged metal grids at 30–40 km/s.","The blue glow in the slide."),
("Hall-effect thruster","the other common electric engine; uses a magnetic field instead of grids. More thrust, a bit less Isp.",""),
("Xenon","a heavy, non-reactive gas. The usual propellant for ion engines because it is easy to ionize and store.",""),
("Nuclear propulsion","using a fission reactor as the energy source for an engine.",""),
("Nuclear thermal propulsion (NTP)","reactor heats hydrogen, hydrogen shoots out a nozzle. Isp about 900 s.","Reactor-heated kettle."),
("Nuclear electric propulsion (NEP)","reactor makes electricity, electricity runs ion or Hall thrusters.",""),
("Fission / reactor","splitting heavy atoms to release heat / the machine that does it under control.",""),
("RTG","radioisotope thermoelectric generator: a plutonium power pack that makes electricity. Not an engine.","Voyager, New Horizons."),
("Specific impulse (Isp)","engine efficiency in seconds: how much push you get per kilogram of propellant.","Miles per gallon. Full treatment next lecture."),
("Requirements","what the mission needs: how much Δv, how fast, how heavy, how much power.",""),
("Trade-off / trade study","giving up one good thing to get another / the formal comparison of options.","Thrust against mileage."),
("Controversial / political","here: people worry about launching a reactor, so nuclear engines need government approval.",""),
("NEXT","NASA's Evolutionary Xenon Thruster, the ion engine in the slide photo. A version flew on DART in 2021.","Add to Who's Who."),
("Dawn / Deep Space 1 / DART","NASA probes that flew on ion engines: asteroid belt (2007), technology test (1998), asteroid impact test (2021).","Add to Who's Who."),
("NERVA / DRACO","US nuclear rocket programs: NERVA ground-tested until 1972; DRACO, a planned flight demo, cancelled in 2025.","Add to Who's Who."),
("SERT-1 / Zond 2","the first electric thrusters fired in space, both in 1964 (US / Soviet).","Add to Who's Who.")]
p4=f'''<div class="page">{top(B.replace("PROPULSION: WHAT + TYPES","VOCABULARY"),'Every word used, <span>in plain English</span>',f'{len(vocab)} entries: the lecture\'s words plus every term I used on the other pages. "Repeat" = you have met it before. Names marked "Add to Who\'s Who" are missions or programs.')}
<div class="gl2">{"".join(f"<div><b>{esc(a)}</b> — {esc(b)}{(' <i>'+esc(c)+'</i>') if c else ''}</div>" for a,b,c in vocab)}</div></div>'''

c1=("THRUST (F)","—","the force an engine makes, in newtons","orbits only change if a force acts. Thrust is that force: momentum thrown away each second","0.1 kg/s × 3,000 m/s = 300 N · ion engine 0.24 N · F-1 6.8 million N","Δv (thrust = the push, Δv = the result)","F = ṁ × vₑ · a = F ÷ m")
c2=("NEWTON'S THIRD LAW","action–reaction","every force has an equal, opposite partner","it is why a rocket works in vacuum: the ship pushes gas back, the gas pushes the ship forward","1,000 kg ship throws 1 kg at 3,000 m/s → ship gains 3 m/s","'pushing on the air' (no air needed)","momentum · thrust · reaction engine")
card,na,nb=cardpage(c1,c2,"C17","scene 8")
p5=f'''<div class="page">{top(B.replace("PROPULSION: WHAT + TYPES","COPY INTO NOTES"),'Where each piece goes <span>in the notebook</span>','The spread on page 1 is the lecture page. Everything deeper is routed to a reserved page, same five routes as before.')}
<div style="display:flex;gap:18px">
<div class="route" style="flex:1">
<div class="card" style="padding:9px 13px"><h3>A · Equations &amp; key numbers page (p3–4)</h3>
<div class="copy">F = ṁ × vₑ         thrust = kg per second × exhaust speed
                   0.1 kg/s × 3,000 m/s = 300 N
m₁v₁ = m₂v₂        momentum kept: 1 kg at 3,000 m/s back
                   → 1,000 kg ship gains 3 m/s
Isp: chemical 250–450 s · electric ~3,000 s · nuclear ~900 s</div>
<h3>B · Section 4 map page (one sentence, written after the last S4 lecture)</h3>
<div class="copy">propulsion: throw mass back → thrust F = ṁ × vₑ;
chemical = big ṁ, electric = big vₑ, nuclear = hot light gas</div>
<h3>C · One-line word bank (new lines)</h3>
<div class="copy">p__ · thrust (F) · engine's force, newtons
p__ · Newton's 3rd law = action–reaction · push gas back, go forward
p__ · propellant = reaction mass · the stuff thrown out
p__ · momentum · mass × velocity; total is kept
p__ · mass flow rate (ṁ) · kg thrown per second
p__ · chemical propulsion · burn it: big thrust, low Isp
p__ · electric propulsion (EP) · electricity flings ions: tiny thrust, high Isp
p__ · ion thruster / Hall thruster · the two main electric engines
p__ · xenon · heavy gas ion engines throw
p__ · nuclear thermal (NTP) · reactor heats H₂, Isp ~900 s, never flown
p__ · RTG · plutonium power pack; electricity, NOT thrust
p__ · trade study · comparing options against requirements</div>
<h3>D · Question bank ("but how?" cards)</h3>
<div class="copy">Q: What does a rocket push against in space?
A: Its own exhaust. Momentum is kept: gas goes back, ship goes forward.
Q: Why is electric thrust tiny if it is so efficient?
A: Jet power = ½ṁvₑ². Fast exhaust needs megawatts; panels give kilowatts.
Q: Why does nuclear thermal get ~900 s?
A: Cooler than a flame, but far lighter exhaust (H₂, mass 2,
   vs steam, mass 18) → about twice as fast.</div></div></div>
<div style="flex:none"><div class="route"><h3>E · Concept cards: next page, C17</h3><div style="font-size:10.5px;color:#444;width:4.3in;margin-bottom:6px">C1–C16 filled the 16 pages in this notebook. C17 onward goes in the second notebook, or wherever you decided the cards live. {na} + {nb} lines of 22.</div></div>{card}</div>
</div></div>'''

p6=f'''<div class="page">{top(B.replace("PROPULSION: WHAT + TYPES","SAY IT OUT LOUD"),'Last page: <span>prove it by talking</span>','After the spread and the 3-line summary, with everything closed. Send me what you said and I will grade it like a friend would.')}
<div class="two"><div>
<div class="card"><h3>🗣 The friend's opening question</h3><div style="font-size:13px;line-height:1.5">"There's no air in space. So what does a rocket even push against?"</div></div>
<div class="card" style="margin-top:12px"><h3>✅ Three sentences you should be able to say</h3><ul class="r" style="font-size:12px">
<li>It pushes against its own exhaust. That's Newton's third law: throw mass out the back and you get shoved forward, air or no air.</li>
<li>The push is called thrust, and it is how much stuff you throw each second times how fast you throw it.</li>
<li>There are three kinds of engine. Chemical rockets push hard but burn through propellant fast, electric engines push very gently but sip it for years, and nuclear sits in between and has never flown.</li></ul></div>
<div class="card" style="margin-top:12px"><h3>❓ Follow-ups a friend might ask</h3><ul class="r" style="font-size:12px">
<li>"If electric is so efficient, why not use it for everything?" (the push is a few sheets of paper; you can't launch or brake into orbit with that)</li>
<li>"Why is it so weak?" (fast exhaust takes huge power, and solar panels only give kilowatts)</li>
<li>"Is the nuclear stuff on Voyager an engine?" (no, an RTG makes electricity)</li>
<li>"Can you change orbit without an engine?" (yes, a gravity assist, but only when a planet is in the right place)</li>
<li>"How do you choose?" (the mission's requirements: how much Δv and how fast you need it)</li></ul></div></div>
<div><div class="card" style="min-height:3.2in"><h3>📝 Your explanation (paste or dictate)</h3><div style="border:2px dashed #999;border-radius:8px;height:2.5in;padding:8px;color:#999;font-size:11px">_ send it to me in chat; I'll put it here _</div></div>
<div class="card" style="margin-top:12px;min-height:2.2in;border-color:var(--green)"><h3 style="color:var(--green)">🎯 My read</h3><div style="border:2px dashed #999;border-radius:8px;height:1.5in;padding:8px;color:#999;font-size:11px">solid on: _<br>fuzzy on: _<br>fix: _<br>→ question-bank cards: _</div></div>
<div class="callout" style="margin-top:12px;font-size:11.5px">⚡ Next: Lecture 2, chemical engines. It turns "thrust" and "mileage" into two formulas.</div></div></div></div>'''
write('s4-l1.html',[p1,p2,p3,p4,p5,p6])
print('ok',na,nb,len(vocab))
