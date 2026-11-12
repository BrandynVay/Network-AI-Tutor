from lib import *
B = "SEC 7 · LEC 2 · BATTERIES"
T = lambda x: B.replace("BATTERIES", x)
svg = '''<svg width="100%" height="428" viewBox="0 0 330 412" style="display:block" font-family="Verdana, sans-serif">
<defs><marker id="ar" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#111"/></marker></defs>
<text x="8" y="13" font-size="10" font-weight="bold" fill="#111">1 · TWO KINDS OF BATTERY</text>
<g font-size="8.5" fill="#111">
<rect x="8" y="20" width="152" height="68" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="84" y="34" text-anchor="middle" font-weight="bold">PRIMARY</text>
<text x="15" y="48">one shot · NO recharge</text><text x="15" y="60">most energy per kilo</text><text x="15" y="72">one-time jobs: pyro, stage</text><text x="15" y="83">separation, opening arrays</text>
<rect x="170" y="20" width="152" height="68" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="246" y="34" text-anchor="middle" font-weight="bold">SECONDARY</text>
<text x="177" y="48">rechargeable from the array</text><text x="177" y="60">less energy per kilo</text><text x="177" y="72">runs everything while the</text><text x="177" y="83">craft is in shadow</text></g>
<line x1="8" y1="95" x2="322" y2="95" stroke="#bbb" stroke-width="1"/>
<text x="8" y="108" font-size="10" font-weight="bold" fill="#111">2 · ONE CYCLE EVERY ORBIT</text>
<line x1="40" y1="180" x2="40" y2="114" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
<line x1="40" y1="180" x2="296" y2="180" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
<line x1="40" y1="126" x2="296" y2="126" stroke="#111" stroke-width="0.8" stroke-dasharray="3 3"/>
<line x1="40" y1="152" x2="296" y2="152" stroke="#111" stroke-width="0.8" stroke-dasharray="3 3"/>
<polyline points="40,152 116,126 165,152 241,126 290,152" fill="none" stroke="#111" stroke-width="2.4"/>
<g font-size="8" fill="#111"><text x="36" y="129" text-anchor="end">100%</text><text x="36" y="155" text-anchor="end">70%</text><text x="36" y="183" text-anchor="end">0%</text>
<text x="78" y="191" text-anchor="middle">sunlight: charge</text><text x="140" y="191" text-anchor="middle">shadow</text><text x="203" y="191" text-anchor="middle">sunlight</text><text x="265" y="191" text-anchor="middle">shadow</text></g>
<line x1="304" y1="128" x2="304" y2="150" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
<text x="310" y="137" font-size="8" font-weight="bold" fill="#111">DoD</text><text x="310" y="148" font-size="8" font-weight="bold" fill="#111">30%</text>
<text x="165" y="205" text-anchor="middle" font-size="8.5" fill="#111">depth of discharge (DoD) = how much you drain each time</text>
<line x1="8" y1="211" x2="322" y2="211" stroke="#bbb" stroke-width="1"/>
<text x="8" y="224" font-size="10" font-weight="bold" fill="#111">3 · DRAIN IT LESS, IT LASTS LONGER</text>
<line x1="40" y1="300" x2="40" y2="230" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
<line x1="40" y1="300" x2="320" y2="300" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
<path d="M52,232 C56,262 66,274 76,276 S120,288 166,292 S260,295 310,296" fill="none" stroke="#111" stroke-width="2.2"/>
<g fill="#111"><circle cx="52.6" cy="236" r="2.6"/><circle cx="76" cy="276" r="2.6"/><circle cx="166" cy="292" r="2.6"/><circle cx="310" cy="296" r="2.6"/></g>
<g font-size="8" fill="#111"><text x="60" y="240">80% → 700 cycles</text><text x="84" y="271">30% → 2,000</text><text x="134" y="285">10% → 7,000</text><text x="318" y="289" text-anchor="end">5% → 15,000</text>
<text x="8" y="262">DoD</text><text x="318" y="311" text-anchor="end">number of cycles →</text></g>
<text x="165" y="324" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">shallow cycles = long life, but a bigger, heavier battery</text>
<line x1="8" y1="331" x2="322" y2="331" stroke="#bbb" stroke-width="1"/>
<text x="8" y="344" font-size="10" font-weight="bold" fill="#111">4 · HOW BIG A BATTERY</text>
<rect x="24" y="350" width="282" height="19" rx="5" fill="#fff" stroke="#111" stroke-width="1.5"/>
<text x="165" y="363" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#111">battery energy = load × shadow time ÷ DoD</text>
<g font-size="8.5" fill="#111" text-anchor="middle"><text x="165" y="382">1,000 W × 0.6 h ÷ 0.30 = 2,000 Wh (about 13 kg)</text><text x="165" y="394">watt-hours = ampere-hours × volts</text><text x="165" y="406">2,000 Wh ÷ 28 V = 71 Ah</text></g>
</svg>'''
p1 = spread(B, 'The bucket <span>for the dark</span>', 'S7 / L2 — Batteries', svg,
 "zigzag = battery charge over two orbits · dotted lines = full and lowest level · dots = points on the life curve",
 ["1. Primary = one shot, most energy per kilo. Secondary = rechargeable.",
  "2. Depth of discharge = how much you drain each orbit.",
  "3. Shallow drains last far longer but need a heavier battery."],
 ['Primary vs secondary battery?', 'What are primary batteries used for?', 'When does a spacecraft run on its battery?', 'Capacity vs stored energy: units?',
  'What is depth of discharge?', 'Three questions for designing a battery?', 'How does DoD affect battery life?', 'What does a small DoD cost?',
  'How many cycles a day in low orbit?', '<span class="hl b">? why does deep draining wear it out</span>'],
 ['two kinds: <span class="hl y">primary</span> and <span class="hl y">secondary</span> batteries',
  'primary: one shot, <span class="hl o">no recharge</span> · high <span class="hl y">energy density</span> · missiles, rockets · one-time jobs: <span class="hl y">pyro</span>, stage separation, deploying arrays',
  'secondary: <span class="hl g">rechargeable</span> from the solar array · lower energy density · runs the systems in the shadow',
  '<span class="hl y">capacity</span> in ampere-hours (<span class="hl k">Ah</span>) · stored energy in watt-hours (<span class="hl k">Wh</span>) = Ah × volts',
  '<span class="hl y">depth of discharge</span> (DoD) = % of capacity used · 80% left → DoD 20%',
  'one charge + one discharge per orbit',
  'design: 1) time in shadow · 2) rate of discharge (the load) · 3) rate of charge → capacity + power',
  'must survive a <span class="hl o">very high number of cycles</span>',
  'small DoD → <span class="hl g">long life</span> · but a bigger, heavier battery → trade mass against life'])

p2 = f'''<div class="page">{top(T("TEACH"),'Saving sunlight <span>for the shadow</span>','Simple story first, then the official names, then how it actually works with numbers you can check.')}
<div class="eli"><b style="font-size:14px">🧒 Like you're 5</b><br>
Solar panels are like rain: wonderful while it lasts, but in low orbit the spacecraft flies into the Earth's shadow sixteen times a day. So it carries a bucket. In sunlight the panels run everything and fill the bucket. In the dark the bucket runs everything. That bucket is the <b>secondary battery</b>, the rechargeable kind, like the one in your phone. The other kind, the <b>primary battery</b>, is a firework: it holds more punch for its weight but works once. It is used for one-time jobs like firing the little charges that release the solar panels.<br>
The whole lecture is about one choice: how far down do you drain the bucket each time? That is the <b>depth of discharge</b>. Your phone battery lasts years longer if you keep it between 80% and 100% than if you run it flat every day. A spacecraft battery is the same, and it gets 6,000 cycles a year. Drain it gently and it lives. But to drain it gently you need a much bigger bucket, and every kilo costs. Life against weight: that is the trade.</div>
<div class="two">
<div class="card" style="padding:9px 13px"><h3>🏷 The official names (name first, then what it means)</h3>
<ul class="names" style="font-size:10.6px">
<li><b>Cell</b>: one electrochemical unit, a few volts. A <b>battery</b> is several cells wired together.</li>
<li><b>Primary battery</b> (non-rechargeable). Space types: lithium thionyl chloride, silver-zinc.</li>
<li><b>Secondary battery</b> (rechargeable; storage battery). Space types, oldest to newest: <b>nickel-cadmium</b> (NiCd), <b>nickel-hydrogen</b> (NiH₂), <b>lithium-ion</b> (Li-ion).</li>
<li><b>Energy density</b> (properly <b>specific energy</b>): watt-hours stored per kilogram.</li>
<li><b>Capacity</b>: charge a battery can deliver, in <b>ampere-hours</b> (Ah). <b>Stored energy</b>: in <b>watt-hours</b> (Wh) = Ah × volts.</li>
<li><b>Depth of discharge, DoD</b>: percentage of the capacity taken out. Its mirror is <b>state of charge, SoC</b> = 100% − DoD.</li>
<li><b>Charge rate / discharge rate</b> (C-rate): how fast. 1C empties or fills the battery in one hour.</li>
<li><b>Cycle</b>: one discharge plus one recharge. <b>Cycle life</b>: how many it survives.</li>
<li><b>Eclipse</b> (the lecture's "penumbra time"): the part of the orbit in the planet's shadow. <b>Umbra</b> is the full shadow; <b>penumbra</b> is only its fuzzy edge.</li>
<li><b>Anode, cathode, electrolyte</b>: the two electrodes and the ion-carrying material between them.</li>
<li><b>Pyrotechnic device</b> (pyro): a small explosive charge that cuts a bolt or opens a valve, once.</li>
<li><b>Bus voltage</b>: the spacecraft's supply voltage, commonly 28 V.</li>
</ul></div>
<div class="card" style="padding:9px 13px"><h3>🛠 How it actually works</h3>
<table class="mech" style="font-size:9.9px"><tr><th style="width:66px">Step</th><th>The mechanism, with numbers</th></tr>
<tr><td><b>1 · Inside a cell</b></td><td>Two electrodes hold lithium with different strength. The material between them lets charged lithium atoms (ions) through but not electrons. So when lithium moves across inside, its electrons must go the long way round through the wire: the same trick as the solar cell. About 3.6 V per lithium-ion cell; eight in a row make 28 V.</td></tr>
<tr><td><b>2 · One shot or many</b></td><td>In a primary cell the reaction cannot be run backwards, which allows more energetic chemistry: about 400–500 Wh per kg. Lithium-ion: 150–250. Older nickel-hydrogen: about 60.</td></tr>
<tr><td><b>3 · Units</b></td><td>Energy (Wh) = capacity (Ah) × volts. 71 Ah × 28 V ≈ 2,000 Wh.</td></tr>
<tr><td><b>4 · The shadow</b></td><td>At 400 km an orbit takes 92 minutes and up to 36 of them (0.6 h) are dark. About 16 orbits a day: 5,800 cycles a year, 29,000 in five years.</td></tr>
<tr><td><b>5 · Sizing</b></td><td>A 1,000 W spacecraft uses 1,000 × 0.6 = 600 Wh each shadow. Allow only a 30% drain: battery = 600 ÷ 0.30 = <b>2,000 Wh</b>, about 13 kg. Allow 80%: only 750 Wh and 5 kg, but it wears out several times sooner.</td></tr>
<tr><td><b>6 · Why depth hurts</b></td><td>The electrodes swell and shrink as lithium moves in and out. Deeper swings strain them more and feed side reactions that lock lithium away for good. The slide's curve: 80% → 700 cycles, 30% → 2,000, 10% → 7,000, 5% → 15,000. Today's lithium-ion space cells manage tens of thousands at 30%, with the same shape of curve.</td></tr>
<tr><td><b>7 · High orbits</b></td><td>A GEO satellite is in shadow only around the two equinoxes: about 90 eclipses a year, up to 72 minutes. That is 1,350 cycles in 15 years, so it can drain 70–80% each time.</td></tr>
<tr><td><b>8 · Refilling</b></td><td>The 600 Wh must go back in during 56 minutes of sunlight: 600 ÷ 0.93 h ÷ 0.9 (losses) ≈ 710 W. So the array for a 1,000 W spacecraft must make about <b>1,700 W</b>.</td></tr></table></div>
</div></div>'''

p3 = f'''<div class="page">{top(T("SIZING + FACT CHECK"),'How big a bucket, <span>and for how long</span>','A sizing recipe with low orbit and high orbit side by side, then where the instructor was loose, the caption errors, and the say-it-out-loud script.')}
<div class="two" style="margin-bottom:8px">
<div class="card" style="padding:7px 13px"><h3>🧮 The recipe</h3>
<div style="font-size:11px;line-height:1.5"><b>1.</b> Shadow time in hours.<br>
<b>2.</b> Energy used = load (W) × shadow time (h).<br>
<b>3.</b> Battery energy = energy used ÷ depth of discharge.<br>
<b>4.</b> Capacity (Ah) = battery energy ÷ bus voltage.<br>
<b>5.</b> Mass = battery energy ÷ energy per kilo.<br>
<b>Worked:</b> 1,000 W × 0.6 h = 600 Wh. ÷ 0.30 = 2,000 Wh. ÷ 28 V = 71 Ah. ÷ 150 Wh/kg = <b>13 kg</b>.<br>
His formula is step 3 turned round: DoD (%) = energy taken out ÷ (capacity × voltage) × 100.</div></div>
<div class="card" style="padding:7px 13px"><h3>🛰 Low orbit against GEO</h3>
<table class="mech" style="font-size:10.4px"><tr><th></th><th>Low orbit, 400 km</th><th>GEO</th></tr>
<tr><td><b>One orbit</b></td><td>92 minutes</td><td>24 hours</td></tr>
<tr><td><b>Longest shadow</b></td><td>36 minutes</td><td>72 minutes</td></tr>
<tr><td><b>Cycles per year</b></td><td>about 5,800</td><td>about 90</td></tr>
<tr><td><b>Usual depth of discharge</b></td><td>20–40%</td><td>60–80%</td></tr>
<tr><td><b>What wears the battery</b></td><td>the number of cycles</td><td>mostly age</td></tr></table>
<div style="font-size:10.3px;margin-top:3px">GEO satellites only pass through the Earth's shadow for a few weeks around each equinox.</div></div></div>
<div class="two">
<div><div class="card" style="padding:7px 13px"><h3>▲ Where the instructor was loose</h3>
<ul class="r" style="font-size:10.4px">
<li><b>"Auxiliary power, low power."</b> In the shadow the battery is the <i>only</i> power on board. It has to carry the whole spacecraft.</li>
<li><b>"Penumbra time."</b> The word is eclipse. The penumbra is just the thin fuzzy edge of the shadow where the Sun is partly covered.</li>
<li><b>"Two-hour cycle… 12 cycles a day."</b> Again: low orbits take about 92 minutes, so about 16 cycles a day. Earlier in this same lecture he says 1.5 hours.</li>
<li><b>"Secondary batteries are low energy density."</b> Lower than primary ones, not low: 150–250 Wh per kg against 400–500.</li>
<li><b>The charge graph from 0% to 100%.</b> He says himself it is the limit case. No real design goes anywhere near 0%.</li>
<li><b>The life curve's numbers.</b> The shape is right for every battery. The values look like an older battery type; modern lithium-ion cells survive several times more cycles at the same depth, as far as I know.</li>
<li><b>Not said: how a battery works, or which types fly.</b> Both are on the teach page.</li>
<li><b>Not said: the array has to be bigger because of the battery.</b> It must run the spacecraft and refill the battery in the same sunlit stretch. That links this lecture to your solar array quiz.</li>
<li><b>He was right</b> about the phone: keeping it between 80% and 100% makes it last longer than running it flat.</li></ul></div></div>
<div><div class="card" style="padding:7px 13px"><h3>🔎 Caption errors</h3>
<table class="t" style="font-size:9.7px"><tr><th>Captions said</th><th>Instructor meant</th></tr>
<tr><td>"mistrials rockets"</td><td><b>missiles</b>, rockets</td></tr>
<tr><td>"look cool and just one one time"</td><td><b>occur</b> just one time</td></tr>
<tr><td>"the solar Appollo"</td><td>the solar <b>power</b></td></tr>
<tr><td>"measured in per hour"</td><td>measured in <b>ampere-hours</b></td></tr>
<tr><td>"Watchtower's", "vat's house"</td><td><b>watt-hours</b></td></tr>
<tr><td>"the Andy Awards… they empower hours"</td><td>the <b>ampere-hours</b></td></tr>
<tr><td>"depth of this charge", "deficit of this charge"</td><td><b>depth of discharge</b></td></tr>
<tr><td>"d o d", "diod D", "deodorize", "deity", "the O.D."</td><td><b>DoD</b></td></tr>
<tr><td>"multi-byte bytes are found"</td><td><b>multiplied by a hundred</b></td></tr>
<tr><td>"one charge and these talks Bob be it"</td><td>one charge and <b>discharge per orbit</b></td></tr>
<tr><td>"on the shuttle"</td><td>in the <b>shadow</b></td></tr>
<tr><td>"rate of chach" · "eyeball"</td><td>rate of <b>charge</b> · <b>are able</b></td></tr>
<tr><td>"lineal", "Linnea" · "Vardi"</td><td><b>linear</b> · <b>vary</b></td></tr></table></div>
<div class="card" style="margin-top:8px;padding:7px 13px"><h3>🗣 Say it out loud</h3>
<div style="font-size:10.8px;line-height:1.45"><b>Friend:</b> "What happens to a satellite's solar power when it goes behind the Earth?"<br>
<b>You:</b> It runs on a rechargeable battery. In sunlight the panels power everything and fill the battery; in the shadow the battery takes over, sixteen times a day in a low orbit. The design question is how far to drain it each time. Drain it only 30% and it lasts many times longer than if you run it flat, but then the battery has to be more than three times bigger than the energy you actually use. It is a trade between weight and lifetime.</div></div></div>
</div></div>'''

vocab = [("Battery", "a device that stores energy chemically and gives it back as electricity.", ""),
("Cell", "one unit of a battery, a few volts.", ""),
("Primary battery", "used once; cannot be recharged.", "A firework."),
("Secondary battery", "rechargeable.", "A bucket you refill."),
("One shot", "works a single time.", ""),
("Recharge", "push energy back in.", ""),
("Energy density", "energy stored per kilogram (or per litre).", ""),
("Missile / rocket", "vehicles whose flights last minutes, so one-shot batteries suit them.", ""),
("Pyrotechnic (pyro)", "a small explosive device that cuts or releases something.", ""),
("Stage separation", "dropping an empty rocket stage.", "Repeat, Section 4."),
("Deploy", "unfold or release.", "Repeat."),
("Auxiliary power", "back-up or secondary power.", ""),
("Penumbra / umbra", "the partly shaded edge of a shadow / the fully dark part.", ""),
("Eclipse", "the time the spacecraft spends in the planet's shadow.", "Repeat."),
("Capacity", "how much charge a battery holds, in ampere-hours.", "The size of the bucket."),
("Ampere-hour (Ah)", "one ampere flowing for one hour.", "Your phone lists it as mAh."),
("Stored energy", "the energy in the battery, in watt-hours.", ""),
("Watt-hour (Wh)", "one watt for one hour. Wh = Ah × volts.", ""),
("Voltage / average discharge voltage", "electrical push / its average value while the battery empties.", ""),
("Depth of discharge (DoD)", "the percentage of the capacity that has been used.", "How far down the bucket is."),
("State of charge", "the percentage left. 100% − DoD.", ""),
("Charge rate / discharge rate", "how fast energy goes in / comes out.", ""),
("Cycle", "one discharge followed by one recharge.", ""),
("Battery life / life expectancy", "how many cycles, or years, it lasts.", ""),
("Linear", "changing at a steady rate: a straight line on a graph.", ""),
("Empirical", "found by measurement, not derived from theory.", ""),
("Iterative", "repeated, improving the answer each round.", ""),
("Mass", "how much matter; what the launcher has to lift.", "Repeat."),
("Lithium-ion (Li-ion)", "today's standard rechargeable battery, in phones and spacecraft.", ""),
("Nickel-cadmium / nickel-hydrogen", "the older rechargeable types used on spacecraft.", ""),
("Electrode / electrolyte", "the two plates of a cell / the material between that carries ions.", ""),
("Ion", "an atom with an electric charge.", "Repeat, Section 4."),
("Bus voltage", "the spacecraft's main supply voltage, often 28 V.", ""),
("Equinox", "the two times a year when the Sun is over the equator; GEO eclipse seasons.", "")]
p4 = f'''<div class="page">{top(T("VOCABULARY"),'Every word used, <span>in plain English</span>',f'{len(vocab)} entries. "Repeat" = you have met it before.')}
<div class="gl2" style="font-size:10.5px;line-height:1.38">{"".join(f"<div><b>{esc(a)}</b> — {esc(b)}{(' <i>'+esc(c)+'</i>') if c else ''}</div>" for a,b,c in vocab)}</div></div>'''
write('s7-l2.html', [p1, p2, p3, p4])
print('ok', len(vocab))
