from lib import *
B = "SEC 6 · LEC 3 · ATTITUDE ACTUATORS"
T = lambda x: B.replace("ATTITUDE ACTUATORS", x)
svg = '''<svg width="100%" height="428" viewBox="0 0 330 412" style="display:block" font-family="Verdana, sans-serif">
<defs><marker id="ar" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#111"/></marker></defs>
<text x="8" y="13" font-size="10" font-weight="bold" fill="#111">1 · INSIDE: wheels swap spin with the craft</text>
<rect x="30" y="46" width="80" height="56" fill="#fff" stroke="#111" stroke-width="1.8"/>
<circle cx="70" cy="74" r="20" fill="#ddd" stroke="#111" stroke-width="1.6"/>
<path d="M58,67 A14,14 0 0 1 82,67" fill="none" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
<path d="M118,38 Q70,14 24,36" fill="none" stroke="#111" stroke-width="2.2" marker-end="url(#ar)"/>
<g transform="rotate(-25 245 69)"><ellipse cx="245" cy="69" rx="28" ry="9" fill="#ddd" stroke="#111" stroke-width="1.6"/><line x1="245" y1="69" x2="245" y2="32" stroke="#111" stroke-width="2.6" marker-end="url(#ar)"/></g>
<path d="M224,30 Q247,18 268,34" fill="none" stroke="#111" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#ar)"/>
<g font-size="8.5" fill="#111"><text x="8" y="116" font-weight="bold">REACTION WHEEL</text><text x="8" y="128">change the wheel's SPEED</text><text x="8" y="140">→ the craft turns the other way</text>
<text x="322" y="116" text-anchor="end" font-weight="bold">CONTROL MOMENT GYRO</text><text x="322" y="128" text-anchor="end">speed stays the same</text><text x="322" y="140" text-anchor="end">TILT its axis → a big twist</text></g>
<line x1="8" y1="148" x2="322" y2="148" stroke="#bbb" stroke-width="1"/>
<text x="8" y="162" font-size="10" font-weight="bold" fill="#111">2 · OUTSIDE: push on something else</text>
<line x1="14" y1="212" x2="126" y2="166" stroke="#111" stroke-width="1" stroke-dasharray="4 3"/>
<rect x="34" y="182" width="72" height="12" fill="#fff" stroke="#111" stroke-width="1.6"/>
<g stroke="#111" stroke-width="1"><line x1="42" y1="182" x2="46" y2="194"/><line x1="52" y1="182" x2="56" y2="194"/><line x1="62" y1="182" x2="66" y2="194"/><line x1="72" y1="182" x2="76" y2="194"/><line x1="82" y1="182" x2="86" y2="194"/><line x1="92" y1="182" x2="96" y2="194"/></g>
<path d="M112,186 Q120,176 114,168" fill="none" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
<rect x="222" y="176" width="48" height="30" fill="#fff" stroke="#111" stroke-width="1.8"/>
<line x1="272" y1="180" x2="304" y2="180" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
<line x1="220" y1="202" x2="188" y2="202" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
<path d="M255,198 A10,10 0 1 0 237,198" fill="none" stroke="#111" stroke-width="1.5" marker-end="url(#ar)"/>
<g font-size="8.5" fill="#111"><text x="8" y="228" font-weight="bold">MAGNETIC TORQUER</text><text x="8" y="240">a coil = an electromagnet</text><text x="8" y="252">Earth's field twists it, like a compass</text><text x="8" y="264">weak · no fuel · low orbit only</text>
<text x="322" y="228" text-anchor="end" font-weight="bold">THRUSTERS</text><text x="322" y="240" text-anchor="end">small jets, off-centre, in pairs</text><text x="322" y="252" text-anchor="end">strong · but they use propellant</text></g>
<line x1="8" y1="272" x2="322" y2="272" stroke="#bbb" stroke-width="1"/>
<text x="8" y="286" font-size="10" font-weight="bold" fill="#111">3 · WHEELS FILL UP (saturation)</text>
<line x1="30" y1="368" x2="30" y2="294" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
<line x1="30" y1="368" x2="320" y2="368" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
<line x1="30" y1="312" x2="312" y2="312" stroke="#111" stroke-width="1" stroke-dasharray="4 3"/>
<polyline points="30,364 140,312 146,360 256,312 262,360 310,338" fill="none" stroke="#111" stroke-width="2.2"/>
<text x="36" y="302" font-size="8" fill="#111">wheel speed</text><text x="318" y="307" text-anchor="end" font-size="8" fill="#111">maximum speed</text>
<text x="8" y="381" font-size="8" fill="#111">ramp = soaking up a steady outside nudge · drop = dumping it</text>
<text x="165" y="396" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">wheels and CMGs only SWAP spin with the craft</text>
<text x="165" y="408" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">thrusters and magnetic torquers REMOVE it</text>
</svg>'''
p1 = spread(B, 'Spin a wheel, <span>turn the ship</span>', 'S6 / L3 — Attitude actuators', svg,
 "thin arrow = wheel or exhaust · thick arrow = the craft's turn · dashed arrow = tilting · dashed line = magnetic field or limit",
 ["1. Spin a wheel one way and the spacecraft turns the other way.",
  "2. Wheels and CMGs only swap spin, so they fill up (saturate).",
  "3. Thrusters and magnetic torquers push on the outside and empty them."],
 ['The five actuators?', 'Why does spinning a wheel turn the spacecraft?', 'Momentum wheel vs reaction wheel?', 'What is saturation? What fixes it?',
  'Why 3 or 4 wheels?', 'CMG: what changes? Why use one?', 'Magnetic torquer: how? Good and bad?', 'Thrusters: how do they make a twist?',
  'What is slew rate?', '<span class="hl b">? which ones can empty a wheel</span>'],
 ['<span class="hl y">actuators</span> twist the spacecraft: momentum wheels · reaction wheels · magnetic torquers · control moment gyros · thrusters',
  '<span class="hl y">conservation of angular momentum</span>: spin a wheel one way → the craft turns the other (helicopter + tail rotor)',
  '<span class="hl y">momentum wheel</span>: always spinning, <span class="hl k">5,000+ rpm</span> · change its speed to turn the craft · fast, so the wheel can be light',
  '<span class="hl y">saturation</span>: a wheel at top speed can do no more → thrusters or other help',
  'DC motor → <span class="hl y">flywheel</span> → spacecraft rotation · too fast → the wheel can break',
  '<span class="hl y">reaction wheel</span>: same idea, starts at rest · change the <span class="hl g">SPEED</span> · 3–4 wheels for 3 axes',
  '<span class="hl y">CMG</span>: wheel at constant speed · change the <span class="hl g">DIRECTION</span> of its axis → large torque · high <span class="hl y">slew rate</span> · the ISS uses them',
  '<span class="hl y">magnetic torquer</span>: coil (solenoid) makes a magnet that the field of the Earth twists · weak · no moving parts, reliable, cheap',
  '<span class="hl y">thrusters</span>: small cold-gas or hot-gas jets placed off-centre · torque = force × arm · <span class="hl o">use propellant</span>'])

p2 = f'''<div class="page">{top(T("TEACH"),'Turning with <span>nothing to push on</span>','Simple story first, then the official names, then how it actually works with numbers you can check.')}
<div class="eli"><b style="font-size:14px">🧒 Like you're 5</b><br>
Sit on a swivel chair with your feet up and swing your arms hard to the left. The chair turns to the right. You pushed on nothing; you and your arms just traded spin. That is a <b>reaction wheel</b>: a motor spins a heavy wheel one way and the whole spacecraft slowly turns the other way. Stop the wheel and the spacecraft stops, pointing somewhere new. No fuel at all.<br>
The catch: sunlight and thin air keep nudging the spacecraft the same way, day after day. To hold still, the wheel must keep spinning faster to soak that up, until it hits top speed. It is full: <b>saturated</b>. To empty it you must push on something <i>outside</i>: a puff from a small jet (<b>thruster</b>), or an electromagnet that leans on the Earth's magnetic field like a compass needle (<b>magnetic torquer</b>). For very big spacecraft there is a stronger trick. Hold a spinning bicycle wheel by its axle and try to tilt it: it twists hard in your hands. A <b>control moment gyro</b> is that wheel, tilted on purpose. Four of them steer the Space Station.</div>
<div class="two">
<div class="card" style="padding:9px 13px"><h3>🏷 The official names (name first, then what it means)</h3>
<ul class="names" style="font-size:10.7px">
<li><b>Actuator</b>: any device that applies a torque. <b>Momentum-exchange devices</b>: the ones that work by trading spin (wheels and CMGs).</li>
<li><b>Reaction wheel</b> (RW; the slide's "reactor wheel" is a typo): a wheel that normally sits near zero speed and is spun either way.</li>
<li><b>Momentum wheel</b> (bias momentum wheel): a wheel kept spinning fast all the time. Its spin also stiffens the spacecraft against tipping: <b>gyroscopic stiffness</b>. <b>Flywheel</b>: the heavy rotor itself.</li>
<li><b>Angular momentum</b> (h or L): moment of inertia × spin rate, in newton-metre-seconds. <b>Conservation of angular momentum</b>.</li>
<li><b>Saturation</b>: a wheel at its top speed. <b>Momentum dumping</b> (desaturation, momentum unloading): emptying it with an outside torque.</li>
<li><b>Control moment gyroscope, CMG</b>: a wheel at constant speed on a motor-driven <b>gimbal</b>. Output torque = angular momentum × <b>gimbal rate</b>.</li>
<li><b>Slew</b>: a deliberate turn to a new target. <b>Slew rate</b>: how fast it can be done, in degrees per second.</li>
<li><b>Magnetorquer</b> (magnetic torquer, torque rod, torque coil): a coil that makes a <b>magnetic dipole moment</b>; the planet's field twists it.</li>
<li><b>Reaction control system, RCS</b>: the set of small attitude thrusters. <b>Cold-gas thruster</b> (just releases stored gas) and <b>monopropellant thruster</b> (hot gas). A <b>couple</b>: two equal thrusters on opposite sides, giving a pure twist. <b>Moment arm</b>: distance from the centre of mass.</li>
<li><b>Internal torque</b> (wheels, CMGs) versus <b>external torque</b> (thrusters, magnetorquers, and the disturbances).</li>
</ul></div>
<div class="card" style="padding:9px 13px"><h3>🛠 How it actually works</h3>
<table class="mech" style="font-size:10px"><tr><th style="width:68px">Step</th><th>The mechanism, with numbers</th></tr>
<tr><td><b>1 · The swap</b></td><td>Wheel spin + craft spin = constant. Wheel inertia 0.01, craft 100 kg·m²: a ratio of 10,000. Spin the wheel up to 1,000 rpm and the craft turns at 0.1 rpm (0.6° per second) the other way. Brake the wheel and the craft stops.</td></tr>
<tr><td><b>2 · Three axes</b></td><td>One wheel per axis, plus a fourth mounted at a slant as a spare. The Kepler telescope lost two of its four in 2013 and could no longer hold its target.</td></tr>
<tr><td><b>3 · Filling up</b></td><td>A steady outside twist of 0.00001 N·m for a day (86,400 s) adds 0.86 N·m·s. A wheel that holds 4 N·m·s is full in under <b>5 days</b>.</td></tr>
<tr><td><b>4 · Dumping</b></td><td>Switch on a magnetorquer or fire a thruster to twist the craft one way while the wheel slows down to cancel it. The extra spin leaves the spacecraft for good.</td></tr>
<tr><td><b>5 · CMG</b></td><td>The Space Station's: a 98 kg wheel at 6,600 rpm stores 4,760 N·m·s. Tilt its axis at 3.1° per second (0.054 rad/s) and out comes 4,760 × 0.054 ≈ <b>258 N·m</b>. A reaction wheel gives about 0.1 N·m.</td></tr>
<tr><td><b>6 · Magnetorquer</b></td><td>Torque = coil strength × field: 10 A·m² × 0.00003 tesla = <b>0.0003 N·m</b>. Tiny but free. It cannot twist about the field line itself, and it needs a strong field: low orbit only.</td></tr>
<tr><td><b>7 · Thrusters</b></td><td>Torque = force × arm. Two 1 N jets, each 1 m from the centre, firing opposite ways: <b>2 N·m</b> and no sideways push. Every puff is propellant you never get back.</td></tr>
<tr><td><b>8 · Why wheels burst</b></td><td>The rim of a 20 cm wheel at 6,000 rpm moves at 63 m/s. At 65,000 rpm it would be 680 m/s, and the stress (density × speed²) about 3.6 GPa: more than steel can take.</td></tr></table></div>
</div></div>'''

p3 = f'''<div class="page">{top(T("COMPARE + FACT CHECK"),'Five actuators, <span>one table</span>','The comparison to know, then where the instructor was loose, the caption errors, and the say-it-out-loud script.')}
<div class="card" style="padding:7px 13px;margin-bottom:8px"><h3>📋 The actuators side by side</h3>
<table class="mech" style="font-size:10.3px"><tr><th>Actuator</th><th>How it twists</th><th>Kind</th><th>Typical torque</th><th>Uses up</th><th>The catch</th></tr>
<tr><td><b>Reaction wheel</b></td><td>changes its speed, either way</td><td>inside: swaps</td><td>0.01–0.5 N·m</td><td>electricity</td><td>saturates; bearings wear out</td></tr>
<tr><td><b>Momentum wheel</b></td><td>spins fast always; small speed changes</td><td>inside: swaps</td><td>0.01–0.5 N·m</td><td>electricity</td><td>controls one axis; saturates</td></tr>
<tr><td><b>Control moment gyro</b></td><td>tilts a constant-speed wheel</td><td>inside: swaps</td><td>100s of N·m</td><td>electricity</td><td>heavy, complex; saturates too</td></tr>
<tr><td><b>Magnetic torquer</b></td><td>electromagnet in the planet's field</td><td>outside: removes</td><td>about 0.0003 N·m</td><td>electricity</td><td>low orbit only; nothing about the field line</td></tr>
<tr><td><b>Thrusters</b></td><td>small jets off-centre, in pairs</td><td>outside: removes</td><td>0.1 to 100s of N·m</td><td>propellant</td><td>runs out; coarse; exhaust can coat optics</td></tr></table></div>
<div class="two">
<div><div class="card" style="padding:7px 13px"><h3>▲ Where the instructor was loose</h3>
<ul class="r" style="font-size:10.3px">
<li><b>Not said: the inside / outside split.</b> Wheels and CMGs only trade spin with the spacecraft; the total never changes. Only thrusters and magnetic torquers can change the total. That is why every wheel system also carries one of those. It is the most important idea in this lecture.</li>
<li><b>Saturation "occurs commonly due to instabilities".</b> It comes from steady outside nudges: sunlight pressure, thin air, the pull of gravity on a long body. They push the same way for days, and the wheel has to keep absorbing them.</li>
<li><b>Momentum wheel versus reaction wheel.</b> He blurs them. A momentum wheel keeps a large spin all the time. A reaction wheel rests near zero and goes either way.</li>
<li><b>"Speeds from 3,500 to 65,000 rpm."</b> Flight wheels run at a few thousand rpm. As far as I know, 65,000 belongs to experimental energy-storage flywheels.</li>
<li><b>"CMGs are a complete set of momentum wheels in all directions."</b> One CMG is one wheel on a gimbal. Several are needed; the Station has four.</li>
<li><b>"High slew rate… very time-responsive, not much lag."</b> Slew rate is how fast the spacecraft can turn. CMGs give big torque, so heavy craft turn quickly.</li>
<li><b>Magnetic torquers "align the sensor" and "work similarly to CMGs".</b> They are actuators, and nothing like a CMG: they push on the Earth's field, which is outside the spacecraft.</li>
<li><b>Cold gas "usually carbon dioxide".</b> Usually nitrogen. Hot-gas ones burn or decompose hydrazine.</li>
<li><b>Slide typos:</b> "Reactor wheels" = reaction wheels. "3 axis determination" = 3-axis <i>control</i>.</li>
<li><b>He was right</b> about the helicopter: the tail rotor exists to cancel the body's reaction to the main rotor.</li></ul></div></div>
<div><div class="card" style="padding:7px 13px"><h3>🔎 Caption errors</h3>
<table class="t" style="font-size:9.8px"><tr><th>Captions said</th><th>Instructor meant</th></tr>
<tr><td>"attrited determination"</td><td><b>attitude</b> determination</td></tr>
<tr><td>"momentum Boyle's", "moments of will"</td><td><b>momentum wheels</b></td></tr>
<tr><td>"magnetic talks / talkers", "restoring talk"</td><td>magnetic <b>torquers</b>, restoring <b>torque</b></td></tr>
<tr><td>"thrust us"</td><td><b>thrusters</b></td></tr>
<tr><td>"helicopters need to tail"</td><td>need <b>a tail rotor</b></td></tr>
<tr><td>"the amount of the wind can blow"</td><td>the <b>mass of the wheel can be low</b></td></tr>
<tr><td>"separation limit"</td><td><b>saturation</b> limit</td></tr>
<tr><td>"Maybrick"</td><td><b>may break</b></td></tr>
<tr><td>"reactor Wilt's"</td><td><b>reaction wheels</b></td></tr>
<tr><td>"Control Moment Hiros", "momand Jews"</td><td><b>control moment gyros</b></td></tr>
<tr><td>"solar noise"</td><td><b>solenoids</b> (coils)</td></tr>
<tr><td>"calls of hot thrusters"</td><td><b>cold or hot gas</b> thrusters</td></tr>
<tr><td>"froggeries ontology axis"</td><td>probably the <b>horizontal</b> axis (angle θ on the slide)</td></tr></table></div>
<div class="card" style="margin-top:8px;padding:7px 13px"><h3>🗣 Say it out loud</h3>
<div style="font-size:10.8px;line-height:1.45"><b>Friend:</b> "How does a spacecraft turn with nothing to push against?"<br>
<b>You:</b> Mostly by spinning a wheel inside. Spin the wheel one way and the spacecraft turns the other, like swinging your arms on a swivel chair. No fuel. The catch is that outside nudges make the wheels spin faster and faster until they are full. Then it has to push on something outside to empty them: a little jet, or an electromagnet leaning on the Earth's magnetic field. Big things like the Space Station use a spinning wheel they tilt, which twists much harder.</div></div></div>
</div></div>'''

vocab = [("Actuator", "a device that pushes or twists the spacecraft.", "Repeat."),
("Torque", "a twist: force × lever arm. Captions write 'talk'.", "Repeat."),
("Angular momentum", "amount of spin: moment of inertia × spin rate.", "Repeat."),
("Conservation of angular momentum", "the total spin of a closed system never changes.", "Swing your arms on a swivel chair."),
("Momentum wheel", "a wheel kept spinning fast all the time; small speed changes turn the craft.", ""),
("Reaction wheel", "a wheel that rests near zero and is spun either way to turn the craft.", ""),
("Flywheel", "a heavy wheel built to store spin.", ""),
("rpm", "revolutions per minute.", ""),
("DC motor", "an electric motor run from steady (direct) current. It drives the wheel.", ""),
("Saturation / saturation limit", "the wheel has reached top speed and can absorb no more.", "A full bucket."),
("Momentum dumping", "emptying a wheel by pushing on something outside.", "Repeat."),
("Instability", "a tendency to drift or tip away.", ""),
("Centrifugal force", "the outward pull felt by anything going round. It tries to tear a fast wheel apart.", ""),
("Stress", "force inside a material per unit of area.", ""),
("Three-axis control", "controlling roll, pitch and yaw separately.", ""),
("Control moment gyro (CMG)", "a constant-speed wheel whose axis is tilted to make a large torque.", "A tilted bicycle wheel."),
("Gimbal", "the pivoting mount that tilts the wheel.", "Repeat."),
("Slew / slew rate", "a turn to a new target / how fast the craft can turn.", ""),
("Tracking", "keeping pointed at a moving target.", ""),
("Lag", "delay between command and response.", ""),
("International Space Station (ISS)", "the crewed station; it steers with four CMGs.", "Repeat."),
("Magnetic torquer (magnetorquer, torque rod)", "a coil that becomes a magnet when current flows; the planet's field twists it.", "A compass needle."),
("Solenoid", "a coil of wire.", ""),
("Magnetic dipole (moment)", "how strong a magnet the coil is.", ""),
("Restoring torque", "a twist that pulls something back into line.", ""),
("Electrical current", "the flow of electric charge, in amperes.", ""),
("Static (no moving parts)", "nothing in it moves, so nothing wears out.", ""),
("Reliable", "unlikely to fail.", ""),
("Thruster", "a small rocket engine used for pointing or small manoeuvres.", "Repeat, Section 4."),
("Cold-gas thruster", "a valve that lets stored gas (usually nitrogen) squirt out.", ""),
("Hot-gas thruster", "one that heats or burns its propellant, usually hydrazine.", ""),
("Moment arm", "the distance from the centre of mass to where a force acts.", ""),
("Couple", "two equal, opposite forces on opposite sides: a pure twist.", ""),
("Reaction control system (RCS)", "the full set of small attitude thrusters.", ""),
("Internal / external torque", "a twist from inside (wheels) / from pushing on something outside.", ""),
("Disturbance torque", "small unwanted outside twists that never stop.", "Repeat, Section 2."),
("Kepler", "NASA's planet-hunting telescope; it lost two of its four reaction wheels.", "Who's Who.")]
p4 = f'''<div class="page">{top(T("VOCABULARY"),'Every word used, <span>in plain English</span>',f'{len(vocab)} entries. "Repeat" = you have met it before.')}
<div class="gl2" style="font-size:10.4px;line-height:1.36">{"".join(f"<div><b>{esc(a)}</b> — {esc(b)}{(' <i>'+esc(c)+'</i>') if c else ''}</div>" for a,b,c in vocab)}</div></div>'''
write('s6-l3.html', [p1, p2, p3, p4])
print('ok', len(vocab))
