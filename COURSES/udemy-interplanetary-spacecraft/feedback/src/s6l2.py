from lib import *
B = "SEC 6 · LEC 2 · ATTITUDE SENSORS"
T = lambda x: B.replace("ATTITUDE SENSORS", x)
rows3 = [("magnetometer", "about 1°", "low orbits only"), ("Sun sensor", "about 0.1°", "blind in Earth's shadow"),
         ("horizon sensor", "about 0.1°", "only tells you 'down'"), ("star tracker", "about 0.001°", "blinded by the Sun; costly"),
         ("gyroscope", "feels turning", "fast, but drifts")]
lad = ""
for i, (a, b, c) in enumerate(rows3):
    y = 330 + i * 13
    lad += '<text x="8" y="%d" font-weight="bold">%s</text><text x="118" y="%d">%s</text><text x="190" y="%d">%s</text>' % (y, a, y, b, y, c)
svg = f'''<svg width="100%" height="428" viewBox="0 0 330 412" style="display:block" font-family="Verdana, sans-serif">
<defs><marker id="ar" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#111"/></marker></defs>
<text x="8" y="13" font-size="10" font-weight="bold" fill="#111">1 · WHAT EACH SENSOR LOOKS AT</text>
<path d="M118,135 Q150,90 200,60" fill="none" stroke="#111" stroke-width="1" stroke-dasharray="4 3"/>
<path d="M130,141 Q162,96 212,66" fill="none" stroke="#111" stroke-width="1" stroke-dasharray="4 3"/>
<text x="165" y="28" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#111">GYROSCOPE (inside)</text>
<text x="165" y="39" text-anchor="middle" font-size="8" fill="#111">am I turning? how fast?</text>
<line x1="165" y1="43" x2="165" y2="76" stroke="#777" stroke-width="0.8"/>
<rect x="150" y="78" width="30" height="24" fill="#ddd" stroke="#111" stroke-width="1.8"/>
<circle cx="165" cy="90" r="6" fill="#fff" stroke="#111" stroke-width="1.2"/>
<circle cx="38" cy="90" r="9" fill="#fff" stroke="#111" stroke-width="1.6"/>
<g stroke="#111" stroke-width="1"><line x1="38" y1="76" x2="38" y2="70"/><line x1="38" y1="104" x2="38" y2="110"/><line x1="24" y1="90" x2="18" y2="90"/><line x1="28" y1="80" x2="24" y2="76"/><line x1="28" y1="100" x2="24" y2="104"/><line x1="48" y1="80" x2="52" y2="76"/><line x1="48" y1="100" x2="52" y2="104"/></g>
<line x1="148" y1="90" x2="56" y2="90" stroke="#111" stroke-width="1.4" marker-end="url(#ar)"/>
<g fill="#111"><circle cx="284" cy="76" r="2"/><circle cx="302" cy="88" r="2"/><circle cx="290" cy="102" r="2"/><circle cx="314" cy="72" r="2"/><circle cx="310" cy="104" r="2"/></g>
<line x1="182" y1="90" x2="272" y2="90" stroke="#111" stroke-width="1.4" marker-end="url(#ar)"/>
<text x="8" y="124" font-size="8.5" font-weight="bold" fill="#111">SUN SENSOR</text><text x="8" y="135" font-size="8" fill="#111">where is the Sun?</text>
<text x="322" y="124" text-anchor="end" font-size="8.5" font-weight="bold" fill="#111">STAR TRACKER</text><text x="322" y="135" text-anchor="end" font-size="8" fill="#111">which stars are those?</text>
<path d="M70,190 Q165,140 260,190" fill="none" stroke="#111" stroke-width="2"/>
<text x="165" y="186" text-anchor="middle" font-size="8" fill="#111">EARTH (warm)</text>
<line x1="165" y1="104" x2="165" y2="160" stroke="#111" stroke-width="1.4" marker-end="url(#ar)"/>
<text x="176" y="149" font-size="8.5" font-weight="bold" fill="#111">HORIZON SENSOR</text><text x="176" y="160" font-size="8" fill="#111">where is the warm edge?</text>
<text x="8" y="154" font-size="8.5" font-weight="bold" fill="#111">MAGNETOMETER</text><text x="8" y="165" font-size="8" fill="#111">which way is the field?</text>
<text x="222" y="56" font-size="7.5" fill="#111">magnetic field (dashed)</text>
<line x1="8" y1="197" x2="322" y2="197" stroke="#bbb" stroke-width="1"/>
<text x="8" y="211" font-size="10" font-weight="bold" fill="#111">2 · THE GYRO DRIFTS, THE STARS RESET IT</text>
<line x1="30" y1="286" x2="30" y2="220" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
<line x1="30" y1="286" x2="320" y2="286" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
<polyline points="30,284 100,246 100,282 170,244 170,282 240,244 240,282 310,244" fill="none" stroke="#111" stroke-width="2.2"/>
<text x="36" y="226" font-size="8" fill="#111">error in the gyro's answer</text>
<text x="322" y="298" text-anchor="end" font-size="8" fill="#111">time →</text>
<text x="8" y="298" font-size="8" fill="#111">ramp = gyro drifting · drop = star tracker corrects it</text>
<line x1="8" y1="304" x2="322" y2="304" stroke="#bbb" stroke-width="1"/>
<text x="8" y="316" font-size="10" font-weight="bold" fill="#111">3 · HOW SHARP, AND THE CATCH</text>
<g font-size="8.5" fill="#111">{lad}</g>
<text x="165" y="397" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">one direction pins down only 2 of the 3 angles</text>
<text x="165" y="409" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">→ always combine at least two sensors</text>
</svg>'''
p1 = spread(B, 'Inner ear, eyes <span>and a compass</span>', 'S6 / L2 — Attitude sensors', svg,
 "box = spacecraft · arrows = what a sensor looks at · dashed = magnetic field · zigzag = gyro error over time",
 ["1. A gyro feels turning. The rest look at something outside.",
  "2. One direction fixes only two angles, so sensors are combined.",
  "3. Gyro: fast but drifts. Star tracker: exact but slow. Use both."],
 ['The five kinds of attitude sensor?', 'Which three are optical?', 'Gyroscope: how does it work?', 'Sun sensor: how? good and bad?',
  'Star tracker: how? good and bad?', 'Horizon scanner: what does it see? Why infrared?', 'Magnetometer: what does it compare? Where does it work?',
  'Three other options?', 'Why is one sensor never enough?', '<span class="hl b">? why does a gyro need a star tracker</span>'],
 ['sensors: <span class="hl y">gyroscopes</span> · optical (<span class="hl y">Sun sensor</span>, <span class="hl y">star tracker</span>, <span class="hl y">horizon scanner</span>) · <span class="hl y">magnetometers</span>',
  'gyroscope: a spinning <span class="hl y">rotor</span> keeps its direction · the frame and <span class="hl y">gimbals</span> turn with the spacecraft → measure the turn',
  'Sun sensor: solar cells detect sunlight from a certain direction → angles to the Sun · <span class="hl g">light, cheap</span>',
  'star tracker: camera matches the star field to a sky map → orientation · <span class="hl g">very accurate</span> · <span class="hl o">complex, expensive</span> · good far from the Sun',
  'horizon scanner: <span class="hl y">infrared</span> · warm Earth vs cold space (<span class="hl k">2.7 K</span>) → finds the horizon → 2 axes',
  'magnetometer: direction + strength of the magnetic field, compared with a 3D model of Earth\'s field · <span class="hl o">low Earth orbit</span> only: the field fades with altitude',
  'others: fibre-optic gyros · accelerometers + gyros · several GPS antennas',
  'one direction = only 2 angles → <span class="hl o">combine sensors</span>',
  'gyro drifts → the star tracker resets it'])

p2 = f'''<div class="page">{top(T("TEACH"),'How do you know which way <span>you\'re facing?</span>','Simple story first, then the official names, then how it actually works with numbers you can check.')}
<div class="eli"><b style="font-size:14px">🧒 Like you're 5</b><br>
Sit on a spinning office chair with your eyes shut. Your <b>inner ear</b> feels the turning, so for a few seconds you know roughly which way you face. Keep going and you lose track. That is a <b>gyroscope</b>: it feels turning instantly, but small mistakes pile up. Now open your eyes. Find the <b>Sun</b>: one bright thing, easy, but it only tells you one direction, and it vanishes in the Earth's shadow. Recognize the <b>constellations</b>: now you know exactly how you are turned, though it takes a careful look. Find the <b>horizon</b>: that tells you which way is down. Check a <b>compass</b>: rough, but it works in the dark.<br>
A spacecraft has all of these. And here is the catch that explains why: pointing at one thing is never enough. Point your arm straight at the Sun. You can still roll your wrist without your arm leaving the Sun. One direction pins down two of your three turns; you need a <b>second, different</b> direction for the third.</div>
<div class="two">
<div class="card" style="padding:9px 13px"><h3>🏷 The official names (name first, then what it means)</h3>
<ul class="names" style="font-size:10.7px">
<li><b>Gyroscope</b> (gyro; rate gyro): measures how fast the spacecraft is rotating. A set of three, usually with accelerometers, is an <b>inertial measurement unit, IMU</b>.</li>
<li><b>Rotor</b>, <b>spin axis</b>, <b>gimbal</b>, <b>frame</b>: the spinning wheel, the line it spins about, the pivoting rings that let it stay put, and the housing.</li>
<li><b>Gyro drift</b> (bias): the slow build-up of error in a gyro's answer.</li>
<li><b>Fibre-optic gyroscope, FOG</b> and <b>ring laser gyro</b> (the lecture's "optic gyroscopes"): no spinning parts; they time light going both ways round a loop.</li>
<li><b>Sun sensor</b>: measures the direction to the Sun. <b>Coarse</b> ones are bare solar cells; <b>fine</b> (digital) ones use a slit or pinhole over a detector.</li>
<li><b>Star tracker</b> (star sensor, star camera): photographs stars and matches them to a <b>star catalogue</b>.</li>
<li><b>Horizon sensor</b> (horizon scanner, Earth sensor): finds the edge of the Earth's warm disc in infrared.</li>
<li><b>Magnetometer</b>: measures the direction and strength of the local magnetic field. The map it is compared with is a <b>geomagnetic field model</b> (IGRF).</li>
<li><b>GPS attitude determination</b>: several GPS antennas on one spacecraft, comparing signal arrival.</li>
<li><b>Absolute sensor</b> (sees an outside reference) versus <b>relative sensor</b> (feels change only: the gyro).</li>
<li><b>Sensor fusion</b>: blending several sensors into one best answer, usually with a <b>Kalman filter</b>.</li>
</ul></div>
<div class="card" style="padding:9px 13px"><h3>🛠 How it actually works</h3>
<table class="mech" style="font-size:10.1px"><tr><th style="width:70px">Step</th><th>The mechanism, with numbers</th></tr>
<tr><td><b>1 · Two arrows</b></td><td>One measured direction fixes two angles and leaves you free to spin about that direction. Two different directions (Sun + magnetic field, or two stars) fix all three.</td></tr>
<tr><td><b>2 · Gyroscope</b></td><td>A spinning rotor keeps its axis fixed in space (angular momentum, last lecture), so the turning of the frame around it can be read off. It reports turn <i>rate</i>, 100 times a second. Add the rates up to get the angle, and the errors add up too: a drift of 0.01° per hour is 0.24° after a day.</td></tr>
<tr><td><b>3 · Sun sensor</b></td><td>A solar cell's current falls as the Sun moves off straight-on (as the cosine of the angle). Put four cells under one pinhole and compare their currents: two angles to the Sun. From about 1° for bare cells to 0.01° for fine ones. Tens of grams.</td></tr>
<tr><td><b>4 · Star tracker</b></td><td>A small camera photographs 10 to 50 stars, measures the angles between them and finds the same pattern in a catalogue of a few thousand stars. One picture gives all three angles to about <b>3 arcseconds</b> (0.001°), several times a second.</td></tr>
<tr><td><b>5 · Horizon sensor</b></td><td>Earth radiates like a body at 255 K, peaking near 11 µm (2,898 ÷ T). Space is 2.7 K. At 15 µm the planet is a sharp, even, warm disc day and night. From 400 km it is 140° wide. Find its centre and you know "down": roll and pitch, not yaw.</td></tr>
<tr><td><b>6 · Magnetometer</b></td><td>A three-axis compass. In low orbit the field is 25–65 microtesla. Measure its direction, look up what the field model says it should be at your position, and compare: about 1°. The field falls with distance cubed, so at GEO it is about 0.1 microtesla and little use.</td></tr>
<tr><td><b>7 · Fusion</b></td><td>The gyros carry the answer from moment to moment; every star-tracker picture pulls it back to the truth. That sawtooth is on your drawing.</td></tr></table></div>
</div></div>'''

p3 = f'''<div class="page">{top(T("COMPARE + FACT CHECK"),'Six sensors, <span>one table</span>','The comparison to know, then where the instructor was loose, the caption errors, and the say-it-out-loud script.')}
<div class="card" style="padding:7px 13px;margin-bottom:8px"><h3>📋 The sensors side by side</h3>
<table class="mech" style="font-size:10.3px"><tr><th>Sensor</th><th>What it senses</th><th>Accuracy</th><th>Gives</th><th>Weakness</th></tr>
<tr><td><b>Gyroscope</b></td><td>its own rotation</td><td>drifts 0.001° to 10° per hour</td><td>turn rate, all 3 axes</td><td>relative only: needs resetting</td></tr>
<tr><td><b>Sun sensor</b></td><td>direction to the Sun</td><td>1° coarse, 0.01° fine</td><td>2 angles</td><td>nothing in eclipse</td></tr>
<tr><td><b>Star tracker</b></td><td>star patterns</td><td>about 0.001° (3 arcseconds)</td><td>all 3 angles</td><td>blinded by Sun, Earth, Moon; fails when tumbling; costly</td></tr>
<tr><td><b>Horizon sensor</b></td><td>edge of the warm planet in infrared</td><td>about 0.1°</td><td>roll + pitch</td><td>near a planet only; no yaw</td></tr>
<tr><td><b>Magnetometer</b></td><td>direction of the magnetic field</td><td>about 1°</td><td>2 angles</td><td>low orbit only; needs a field map; upset by the craft's own magnetism</td></tr>
<tr><td><b>GPS, several antennas</b></td><td>differences in signal arrival</td><td>about 0.3°</td><td>all 3 angles</td><td>only below the GPS satellites</td></tr></table></div>
<div class="two">
<div><div class="card" style="padding:7px 13px"><h3>▲ Where the instructor was loose</h3>
<ul class="r" style="font-size:10.4px">
<li><b>"A gyroscope determines the position and orientation."</b> It measures rotation only: how fast you are turning. It knows nothing about position, and it cannot tell you where you point unless something else told it the starting direction. Then it drifts.</li>
<li><b>"The Cubli, a cubic representation of a gyroscope."</b> The Cubli is a small cube from ETH Zurich that jumps up and balances on a corner by spinning wheels inside it. Those are <i>reaction wheels</i>: actuators, the subject of the next lecture. It is not a gyroscope.</li>
<li><b>Star trackers are for "interplanetary… the Sun's intensity is very low".</b> The Sun is still by far the brightest thing at Jupiter. Star trackers are chosen for accuracy, and because one picture gives all three angles. Nearly every modern satellite carries one, in Earth orbit too.</li>
<li><b>"Earth emits around 100–1,000 K."</b> About 255 K. Space is 2.7 K, as he says.</li>
<li><b>Horizon scanner "determines orientation on 2 axes".</b> Right, and it matters: it finds "down", so roll and pitch. It cannot see yaw.</li>
<li><b>Several GPS sensors each "receive an accurate position".</b> GPS positions are good to a few metres, and the antennas sit a metre apart, so positions alone cannot show the tilt. The method compares the exact moment the same radio wave reaches each antenna.</li>
<li><b>Magnetometers "not used for upper orbits".</b> Correct. The reason: the field falls with the cube of distance, so at GEO it is about 300 times weaker than in low orbit.</li>
<li><b>Not said at all: one sensor is never enough</b>, and gyros drift. Those two facts are why a spacecraft carries several kinds.</li></ul></div></div>
<div><div class="card" style="padding:7px 13px"><h3>🔎 Caption errors</h3>
<table class="t" style="font-size:9.8px"><tr><th>Captions said</th><th>Instructor meant</th></tr>
<tr><td>"basically telescopes", "a charge scope"</td><td><b>gyroscopes</b>, a gyroscope</td></tr>
<tr><td>"a story of some sensors"</td><td>such as <b>Sun sensors</b></td></tr>
<tr><td>"spin X is" · "Montane constant"</td><td><b>spin axis</b> · <b>maintained</b> constant</td></tr>
<tr><td>"Kimberlin… Joe's frame… Jones Cup"</td><td><b>gimbal and gyroscope frame</b></td></tr>
<tr><td>"the Cobley"</td><td>the <b>Cubli</b></td></tr>
<tr><td>"Startrek", "Star-Trek us", "stockbroker's"</td><td><b>star tracker(s)</b></td></tr>
<tr><td>"sunsets" · "Sun Center"</td><td><b>Sun sensors</b> · Sun sensor</td></tr>
<tr><td>"an iPhone 6 keeps out"</td><td>a <b>NanoAvionics CubeSat</b> (Sun sensor)</td></tr>
<tr><td>"Corelli's on the scanner"</td><td><b>horizon</b> scanner</td></tr>
<tr><td>"thermal pot"</td><td>thermal <b>part</b></td></tr>
<tr><td>"optic Jungers scopes"</td><td><b>optical gyroscopes</b></td></tr>
<tr><td>"CPS sensors… GPL"</td><td><b>GPS</b> sensors</td></tr>
<tr><td>"for Paul BNZ cannot be used"</td><td>for <b>upper orbits</b> (per the slide)</td></tr></table></div>
<div class="card" style="margin-top:8px;padding:7px 13px"><h3>🗣 Say it out loud</h3>
<div style="font-size:11px;line-height:1.45"><b>Friend:</b> "How does a spacecraft know which way it's pointing?"<br>
<b>You:</b> The same ways you would. It has gyroscopes, like an inner ear, that feel every turn but slowly lose track. And it has eyes: a sensor that finds the Sun, a camera that recognizes star patterns, one that finds the warm edge of the Earth, and a compass for the magnetic field. No single one is enough, because one direction only pins down two of your three turns. So it blends them: the gyros second by second, and the star camera to pull them back to the truth.</div></div></div>
</div></div>'''

vocab = [("Sensor", "a device that measures something.", "Repeat."),
("Gyroscope (gyro)", "a sensor that feels rotation. Captions write 'telescope'.", "Your inner ear."),
("Rotor", "the spinning wheel inside a mechanical gyroscope.", ""),
("Spin axis", "the line the rotor spins about. It stays pointing the same way.", ""),
("Gimbal", "a pivoting ring that lets the rotor keep its direction while the frame turns.", ""),
("Gyroscope frame", "the housing, fixed to the spacecraft.", ""),
("Drift", "slow build-up of error.", ""),
("Rotation rate", "how fast something is turning, in degrees per second.", ""),
("Optical sensor", "a sensor that works by detecting light.", ""),
("Sun sensor", "measures the direction to the Sun.", "Find the brightest thing."),
("Solar cell", "a device that turns light into electric current.", "Section 7."),
("Body angles", "angles measured relative to the spacecraft's own body.", ""),
("Accuracy", "how close a measurement is to the truth.", ""),
("Star tracker", "a camera that recognizes star patterns to find the orientation.", "Reading the constellations."),
("Star field / star catalogue", "the stars in view / the stored map they are matched against.", ""),
("Interplanetary trajectory", "a path between planets.", "Repeat."),
("Horizon scanner (horizon sensor, Earth sensor)", "finds the edge of the planet's disc.", "Finding 'down'."),
("Horizon", "the line where the planet ends and space begins.", ""),
("Infrared", "heat radiation: light just beyond red, given off by anything warm.", "Repeat, Section 5."),
("Kelvin (K)", "temperature counted from absolute zero.", "Repeat."),
("Deep space (2.7 K)", "the background of space, almost absolute zero.", ""),
("Emit / radiate", "give off radiation.", "Repeat."),
("Magnetometer", "measures the direction and strength of a magnetic field.", "A three-axis compass."),
("Magnetic field", "the region where a compass needle feels a pull. Earth has one.", "Repeat."),
("Magnitude / direction", "size / which way.", "Repeat."),
("Field model", "a mathematical map of Earth's magnetic field at every point.", ""),
("Low Earth orbit (LEO)", "orbits below about 2,000 km.", "Repeat."),
("Fibre-optic gyroscope", "a gyro with no moving parts that times light going round a coil of glass fibre.", ""),
("Accelerometer", "a sensor that feels speeding up and slowing down in a straight line.", ""),
("IMU", "inertial measurement unit: gyros and accelerometers in one box.", ""),
("GPS sensor / antenna", "a receiver for the navigation satellites' signals.", "Repeat."),
("Absolute / relative sensor", "sees an outside reference / only feels change.", ""),
("Sensor fusion", "blending several sensors into one best answer.", ""),
("Eclipse", "being in the planet's shadow.", "Repeat."),
("Arcsecond", "1/3600 of a degree.", "Repeat."),
("The Cubli", "a balancing cube from ETH Zurich that uses reaction wheels. Not a gyroscope.", ""),
("NanoAvionics / Vectronic Aerospace", "companies that sell the Sun sensor and star tracker in the slide photos.", "")]
p4 = f'''<div class="page">{top(T("VOCABULARY"),'Every word used, <span>in plain English</span>',f'{len(vocab)} entries. "Repeat" = you have met it before.')}
<div class="gl2" style="font-size:10.4px;line-height:1.36">{"".join(f"<div><b>{esc(a)}</b> — {esc(b)}{(' <i>'+esc(c)+'</i>') if c else ''}</div>" for a,b,c in vocab)}</div></div>'''
write('s6-l2.html', [p1, p2, p3, p4])
print('ok', len(vocab))
