import math
from lib import *
B = "SEC 6 · LEC 1 · ATTITUDE: DEFINITIONS + PHYSICS"
T = lambda x: B.replace("ATTITUDE: DEFINITIONS + PHYSICS", x)
DEFS = '<defs><marker id="ar" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#111"/></marker></defs>'

def wave(x0, x1, y, fn, sw=1.3):
    pts = []
    x = x0
    while x <= x1 + 0.01:
        t = (x - x0) / (x1 - x0)
        pts.append("%.1f,%.1f" % (x, y - fn(t)))
        x += 0.5
    return '<polyline points="%s" fill="none" stroke="#111" stroke-width="%s"/>' % (" ".join(pts), sw)

def bx(x, y, t, w=78):
    return ('<rect x="%d" y="%d" width="%d" height="20" rx="4" fill="#fff" stroke="#111" stroke-width="1.6"/>'
            '<text x="%d" y="%d" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#111">%s</text>') % (x, y, w, x + w / 2, y + 13.5, t)

two_pi = 2 * math.pi
jit = wave(34, 316, 356, lambda t: 19 * math.sin(two_pi * 1.5 * t) + 5 * math.sin(two_pi * 42 * t))
svgA = f'''<svg width="100%" height="428" viewBox="0 0 330 412" style="display:block" font-family="Verdana, sans-serif">{DEFS}
<text x="8" y="13" font-size="10" font-weight="bold" fill="#111">1 · ATTITUDE = which way it points</text>
<rect x="152" y="58" width="26" height="22" fill="#ddd" stroke="#111" stroke-width="1.8"/>
<line x1="150" y1="69" x2="50" y2="69" stroke="#111" stroke-width="1.6" marker-end="url(#ar)"/>
<line x1="178" y1="62" x2="262" y2="34" stroke="#111" stroke-width="1.6" marker-end="url(#ar)"/>
<line x1="165" y1="80" x2="165" y2="124" stroke="#111" stroke-width="1.6" marker-end="url(#ar)"/>
<circle cx="165" cy="142" r="14" fill="#fff" stroke="#111" stroke-width="1.6"/><text x="165" y="145" text-anchor="middle" font-size="7" fill="#111">Earth</text>
<text x="8" y="58" font-size="9" font-weight="bold" fill="#111">ROLL axis</text><text x="8" y="84" font-size="8" fill="#111">the direction of travel</text>
<text x="322" y="26" text-anchor="end" font-size="9" font-weight="bold" fill="#111">PITCH axis</text><text x="322" y="54" text-anchor="end" font-size="8" fill="#111">across the orbit</text>
<text x="176" y="100" font-size="9" font-weight="bold" fill="#111">YAW axis</text><text x="176" y="112" font-size="8" fill="#111">the line to the planet</text>
<text x="8" y="168" font-size="8" fill="#111">like a plane: roll = tilt the wings · pitch = nose up or down</text>
<text x="8" y="179" font-size="8" fill="#111">yaw = nose left or right</text>
<line x1="8" y1="186" x2="322" y2="186" stroke="#bbb" stroke-width="1"/>
<text x="8" y="199" font-size="10" font-weight="bold" fill="#111">2 · THE CONTROL LOOP (ADCS)</text>
{bx(126, 204, "SPACECRAFT")}{bx(14, 238, "SENSORS")}{bx(238, 238, "ACTUATORS")}{bx(126, 272, "COMPUTER")}
<g stroke="#111" stroke-width="1.5"><line x1="126" y1="214" x2="57" y2="236" marker-end="url(#ar)"/><line x1="53" y1="258" x2="123" y2="281" marker-end="url(#ar)"/><line x1="204" y1="282" x2="273" y2="260" marker-end="url(#ar)"/><line x1="277" y1="238" x2="207" y2="215" marker-end="url(#ar)"/></g>
<g font-size="8" fill="#111"><text x="14" y="226">measure</text><text x="14" y="280">attitude error</text><text x="322" y="280" text-anchor="end">torque command</text><text x="322" y="226" text-anchor="end">torque</text>
<text x="165" y="244" text-anchor="middle">a closed loop:</text><text x="165" y="255" text-anchor="middle">it never stops</text></g>
<line x1="8" y1="300" x2="322" y2="300" stroke="#bbb" stroke-width="1"/>
<text x="8" y="313" font-size="10" font-weight="bold" fill="#111">3 · JITTER: it never sits perfectly still</text>
<line x1="30" y1="356" x2="320" y2="356" stroke="#777" stroke-width="0.8" stroke-dasharray="3 3"/>
<line x1="30" y1="386" x2="30" y2="324" stroke="#111" stroke-width="1.2" marker-end="url(#ar)"/>
{jit}
<text x="36" y="328" font-size="8" fill="#111">pointing angle</text>
<text x="8" y="398" font-size="8.5" fill="#111"><tspan font-weight="bold">slow swing</tspan> = the loop correcting itself</text>
<text x="8" y="410" font-size="8.5" fill="#111"><tspan font-weight="bold">fast fuzz</tspan> = jitter: vibration from wheels and pumps</text>
</svg>'''

svgB = f'''<svg width="100%" height="428" viewBox="0 0 330 412" style="display:block" font-family="Verdana, sans-serif">{DEFS}
<text x="8" y="13" font-size="10" font-weight="bold" fill="#111">1 · MOMENT OF INERTIA: three shapes</text>
<circle cx="56" cy="66" r="22" fill="#ddd" stroke="#111" stroke-width="1.6"/>
<g stroke="#111" stroke-width="1.3"><line x1="56" y1="66" x2="56" y2="34" marker-end="url(#ar)"/><line x1="56" y1="66" x2="90" y2="66" marker-end="url(#ar)"/><line x1="56" y1="66" x2="36" y2="90" marker-end="url(#ar)"/></g>
<rect x="158" y="34" width="14" height="64" fill="#ddd" stroke="#111" stroke-width="1.6"/>
<line x1="165" y1="24" x2="165" y2="108" stroke="#111" stroke-width="1" stroke-dasharray="4 3"/>
<line x1="128" y1="66" x2="204" y2="66" stroke="#111" stroke-width="3.2" marker-end="url(#ar)"/>
<ellipse cx="274" cy="70" rx="36" ry="9" fill="#ddd" stroke="#111" stroke-width="1.6"/>
<line x1="228" y1="70" x2="322" y2="70" stroke="#111" stroke-width="1" stroke-dasharray="4 3"/>
<line x1="274" y1="98" x2="274" y2="36" stroke="#111" stroke-width="3.2" marker-end="url(#ar)"/>
<g font-size="8.5" fill="#111" text-anchor="middle"><text x="56" y="120" font-weight="bold">SPHERE</text><text x="56" y="132">same about</text><text x="56" y="144">every axis</text>
<text x="165" y="120" font-weight="bold">ROD (pencil)</text><text x="165" y="132">biggest: across it</text><text x="165" y="144">smallest: along it</text>
<text x="274" y="120" font-weight="bold">DISK (coin)</text><text x="274" y="132">biggest: through</text><text x="274" y="144">the face</text></g>
<text x="165" y="159" text-anchor="middle" font-size="8.5" fill="#111">thick arrow = axis of MAXIMUM moment of inertia · dashed = minimum</text>
<line x1="8" y1="167" x2="322" y2="167" stroke="#bbb" stroke-width="1"/>
<text x="8" y="181" font-size="10" font-weight="bold" fill="#111">2 · THE RULE</text>
<rect x="14" y="188" width="302" height="46" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<g font-size="9" fill="#111" text-anchor="middle"><text x="165" y="202">no outside torque, and a little energy leaking away</text><text x="165" y="214">→ the body ends up spinning about its axis of</text><text x="165" y="227" font-weight="bold">MAXIMUM moment of inertia</text></g>
<text x="8" y="248" font-size="8.5" fill="#111">why: its spin can't change, but its energy drains away, and</text>
<text x="8" y="260" font-size="8.5" fill="#111">spinning about the biggest axis takes the least energy</text>
<line x1="8" y1="268" x2="322" y2="268" stroke="#bbb" stroke-width="1"/>
<text x="8" y="282" font-size="10" font-weight="bold" fill="#111">3 · EXPLORER 1 (1958) vs SPUTNIK 1 (1957)</text>
<rect x="26" y="300" width="92" height="10" rx="5" fill="#ddd" stroke="#111" stroke-width="1.6"/>
<g stroke="#111" stroke-width="0.9"><line x1="72" y1="300" x2="56" y2="290"/><line x1="72" y1="300" x2="88" y2="290"/><line x1="72" y1="310" x2="56" y2="320"/><line x1="72" y1="310" x2="88" y2="320"/></g>
<ellipse cx="128" cy="305" rx="4" ry="11" fill="none" stroke="#111" stroke-width="1.1" stroke-dasharray="3 2"/>
<text x="136" y="300" font-size="7.5" fill="#111">planned</text><text x="136" y="310" font-size="7.5" fill="#111">spin</text>
<path d="M22,326 Q72,350 122,326" fill="none" stroke="#111" stroke-width="1.6" marker-end="url(#ar)"/>
<text x="72" y="352" text-anchor="middle" font-size="8" font-weight="bold" fill="#111">ended up: end over end</text>
<circle cx="262" cy="308" r="16" fill="#ddd" stroke="#111" stroke-width="1.6"/>
<g stroke="#111" stroke-width="0.9"><line x1="250" y1="298" x2="206" y2="290"/><line x1="248" y1="304" x2="204" y2="304"/><line x1="250" y1="318" x2="206" y2="326"/><line x1="254" y1="322" x2="214" y2="340"/></g>
<text x="262" y="352" text-anchor="middle" font-size="8" font-weight="bold" fill="#111">any way up is fine</text>
<g font-size="8" fill="#111"><text x="8" y="368">a pencil, spun on its SMALLEST axis</text><text x="8" y="379">whip antennas flexed, energy leaked</text><text x="8" y="390">→ tumbled within hours</text><text x="8" y="401">still found the radiation belts</text>
<text x="322" y="368" text-anchor="end">a ball: no favorite axis</text><text x="322" y="379" text-anchor="end">antennas radiate all round</text><text x="322" y="390" text-anchor="end">so no pointing was needed</text></g>
</svg>'''

p1 = spread(B, 'Point, check, <span>nudge</span>', 'S6 / L1 (1/2) — Attitude + the loop', svgA,
 "box = spacecraft · three arrows = the three axes · four boxes = the loop · wavy line = pointing angle · dotted = target",
 ["1. Attitude = which way it points. Roll, pitch, yaw are the three ways to turn.",
  "2. ADCS is a loop: measure, compare, command, twist, repeat.",
  "3. Pointing always shakes a little (jitter). Keep it inside the requirement."],
 ['What is attitude? How is it different from orbit?', 'Roll, pitch, yaw: which axis is each?', 'Attitude determination vs attitude control?',
  'What does ADCS stand for?', 'The four boxes of the loop?', 'What travels along each arrow?', 'Why is it a "closed" loop?',
  'What is attitude jitter?', 'Can jitter be zero?', '<span class="hl b">? measured against what</span>'],
 ['<span class="hl y">attitude</span> = orientation of the spacecraft: which way it points (orbit = where it is)',
  '<span class="hl y">roll</span>: turning about the direction of travel · <span class="hl y">pitch</span>: about the axis across the orbit · <span class="hl y">yaw</span>: about the line to the central body',
  '<span class="hl y">attitude determination</span> = measuring the orientation',
  '<span class="hl y">attitude control</span> = returning the spacecraft to the desired attitude',
  '<span class="hl y">ADCS</span> = attitude determination and control system',
  '<span class="hl y">closed feedback loop</span>: sensors → attitude error → on-board computer → torque commands → actuators → torque → spacecraft → sensors…',
  'attitude error = where it points − where it should point',
  '<span class="hl y">torque</span> = a twist: the turning version of a force',
  '<span class="hl y">attitude jitter</span>: small shaking of the pointing angle that never fully goes away',
  'jitter must stay <span class="hl o">inside the mission\'s requirement</span>'])
p1b = spread(B, 'Pencils tumble, <span>coins spin</span>', 'S6 / L1 (2/2) — Spin stability', svgB,
 "thick arrow = biggest moment of inertia · dashed = smallest · dashed loop = planned spin · curved arrow = what happened",
 ["1. Moment of inertia = how far the mass sits from the axis.",
  "2. Left alone, a real body ends up spinning about its biggest-inertia axis.",
  "3. Explorer 1 was a pencil spun the wrong way. Sputnik 1 was a ball."],
 ['What does torque-free mean?', 'What is moment of inertia?', 'Biggest axis for a sphere? A rod? A disk?', 'The stable-spin rule?',
  'How was Explorer 1 meant to spin?', 'What happened instead, and why?', 'Why didn\'t Sputnik 1 care?', 'So what shape should a spinning satellite be?',
  '<span class="hl b">? why only the maximum axis</span>'],
 ['<span class="hl y">torque-free</span> = no outside twist acting on the body',
  '<span class="hl y">moment of inertia</span> = how hard a body is to spin about an axis · big when the mass is <span class="hl g">far from that axis</span>',
  'sphere: the same about every axis · no favorite',
  'cylinder (rod): <span class="hl k">maximum</span> about any axis across it · minimum about its own long axis',
  'disk: maximum about the axis through its face',
  'rule: with no outside torque, a body spins stably only about its axis of <span class="hl y">maximum moment of inertia</span>',
  '<span class="hl y">Explorer 1</span> (USA, 1958): pencil shape, meant to spin about its long axis → <span class="hl o">tumbled</span>',
  '<span class="hl y">Sputnik 1</span> (USSR, 1957): sphere → no preferred axis, nothing to go wrong',
  'lesson: spinning satellites are built like <span class="hl g">drums</span>, not pencils'])

p2 = f'''<div class="page">{top(T("TEACH"),'A thermostat for <span>pointing</span>','Simple story first, then the official names, then how it actually works with numbers you can check.')}
<div class="eli"><b style="font-size:14px">🧒 Like you're 5</b><br>
A spacecraft has two different problems: where it <i>is</i> (its orbit) and which way it <i>faces</i> (its <b>attitude</b>). The dish has to face Earth and the panels have to face the Sun, and nothing in space holds it steady. So it works like the thermostat in your house. A thermostat feels the temperature, compares it with what you asked for and switches the heater. The spacecraft <b>looks</b> at the stars to see which way it is facing, <b>compares</b> that with where it should face, and <b>nudges</b> itself with a small twist. Then it looks again. Forever. That loop is the whole system.<br>
The second half is about spinning. Toss a coin spinning flat like a frisbee and it stays steady. Toss a pencil spinning around its length and it soon starts to wobble and ends up tumbling end over end. Things like to spin the "fat" way, with their weight as far from the spin line as possible. The first American satellite was a pencil spun around its length. Within hours it was tumbling. The first Soviet one was a ball, which has no fat way, so nothing could go wrong.</div>
<div class="two">
<div class="card" style="padding:9px 13px"><h3>🏷 The official names (name first, then what it means)</h3>
<ul class="names" style="font-size:10.6px">
<li><b>Attitude</b>: the orientation of a spacecraft relative to a reference frame. <b>ADCS</b>, attitude determination and control system (also <b>AOCS</b> when orbit control is included).</li>
<li><b>Roll, pitch, yaw</b>: rotations about the three body axes. Together they are a set of <b>Euler angles</b>.</li>
<li><b>Reference frame</b>: what you measure against. An <b>inertial frame</b> is fixed to the distant stars. The <b>orbital frame</b> (LVLH, local vertical / local horizontal) turns with the orbit: one axis to the planet, one along the track, one across. The slide's picture is the orbital frame. <b>Nadir</b>: straight down to the planet.</li>
<li><b>Attitude determination</b> (measuring) and <b>attitude control</b> (correcting). <b>Attitude error</b>: measured minus wanted.</li>
<li><b>Closed-loop control</b> (feedback control). The rule the computer uses is the <b>control law</b>.</li>
<li><b>Sensor</b> and <b>actuator</b>: the parts that measure and the parts that push. Details next lecture.</li>
<li><b>Torque</b> (moment): force × lever arm, in newton-metres. The turning version of force.</li>
<li><b>Pointing accuracy</b> (how close to the target) and <b>pointing stability</b> (how steady). <b>Jitter</b>: fast pointing vibration. <b>Arcsecond</b>: 1/3600 of a degree.</li>
<li><b>Moment of inertia, I</b>: the turning version of mass. <b>Principal axes</b>: the <b>major axis</b> (maximum I), <b>minor axis</b> (minimum), and the <b>intermediate axis</b>.</li>
<li><b>Angular momentum, L</b> = I × spin rate. Conserved when no torque acts.</li>
<li><b>Torque-free motion</b>. The <b>major-axis rule</b>. <b>Flat spin</b>: tumbling about the major axis. <b>Spin stabilization</b> versus <b>three-axis stabilization</b>.</li>
</ul></div>
<div class="card" style="padding:9px 13px"><h3>🛠 How it actually works</h3>
<table class="mech" style="font-size:10.1px"><tr><th style="width:70px">Step</th><th>The mechanism, with numbers</th></tr>
<tr><td><b>1 · Torque</b></td><td>Torque = force × lever arm. Angular speed-up = torque ÷ moment of inertia, the twin of a = F ÷ m.</td></tr>
<tr><td><b>2 · One turn of the loop</b></td><td>A spacecraft with I = 100 kg·m² is 1° off target. Its wheel can twist with 0.05 N·m. Speed-up = 0.05 ÷ 100 = 0.0005 rad/s². Twist one way for 6 s, the other way for 6 s: 1° corrected in about <b>12 seconds</b>. Measure again.</td></tr>
<tr><td><b>3 · Jitter</b></td><td>Wheels are never perfectly balanced, pumps hum, panels creak as they warm. The result is a fast tremble on top of the slow correction. Hubble holds <b>0.007 arcseconds</b>: the width of a hair seen from 3 km.</td></tr>
<tr><td><b>4 · Moment of inertia</b></td><td>I = sum of (mass × distance from the axis²). A 14 kg pencil 2 m long and 16 cm wide: about its long axis ½MR² = <b>0.044</b>; about an axis across its middle <b>4.9</b> kg·m². 110 times bigger, because the ends are a metre from that axis.</td></tr>
<tr><td><b>5 · What is kept</b></td><td>With no outside torque, angular momentum L = I × spin rate cannot change. The spin <i>energy</i> is L² ÷ (2 × I): for the same L, a bigger I means less energy.</td></tr>
<tr><td><b>6 · The leak</b></td><td>Real spacecraft are not rigid. Antennas flex, fuel sloshes, and each wobble turns a little spin energy into heat. L stays, energy falls, so the body slides toward the lowest-energy spin: about the <b>biggest</b> I.</td></tr>
<tr><td><b>7 · Explorer 1</b></td><td>Spun at 750 turns a minute about its long axis: 135 joules. Its four whip antennas flexed. After the slide: 750 ÷ 110 ≈ <b>7 turns a minute</b>, end over end, with about 1 joule. The other 99% went into bending wire.</td></tr>
<tr><td><b>8 · The fix</b></td><td>Make the spin axis the fat one: build spinning satellites as squat drums. Or don't spin at all and run the loop on three axes.</td></tr></table></div>
</div></div>'''

p3 = f'''<div class="page">{top(T("FACT CHECK"),'Right conclusions, <span>shaky reasons</span>','Where the instructor was wrong or loose, the caption errors, and the question a friend would ask.')}
<div class="two">
<div><div class="card" style="padding:8px 13px;border-color:var(--orange)"><h3>⛔ Wrong, and worth getting right</h3>
<ul class="r" style="font-size:10.7px">
<li><b>"Moment of inertia is the amount of mass in one direction."</b> It is about how far the mass is from the spin axis. Along a pencil's length the mass hugs the axis, so that moment is small. Across the middle the ends are far away, so it is large. His conclusions for all three shapes are right; the reason he gives is not.</li>
<li><b>"Explorer 1 was completely unstable… difficult to recover data."</b> It did tumble, and nobody expected it. But it kept working for four months and made the first great discovery of the space age: the radiation belts around the Earth.</li>
<li><b>"The Russians understood this… the US goes for marketing style."</b> Nobody understood it yet. Explorer 1's tumble is how engineers <i>learned</i> the rule. Its pencil shape came from the rocket: the satellite was the top stage's casing with instruments in the nose.</li>
<li><b>"The sphere would move completely random."</b> A sphere keeps whatever spin it starts with. It has no preferred axis, so it is neither stable nor unstable. Sputnik 1 did not care because its four antennas radiated in every direction, like the omnidirectional antennas in Section 5.</li></ul></div>
<div class="card" style="margin-top:9px;padding:8px 13px"><h3>▲ Looser points</h3>
<ul class="r" style="font-size:10.6px">
<li><b>The rule needs a leak.</b> For a perfectly rigid body, spin about the smallest axis is stable too. Only the in-between axis is unstable. Try it: flip your phone over a bed about each of its three axes. One of them always wobbles.</li>
<li><b>"The sensors determine the difference."</b> Sensors only measure. The computer compares with the target.</li>
<li><b>Jitter "cannot really be corrected".</b> It can be reduced a great deal with balanced wheels and vibration isolators. It can't be made zero.</li>
<li><b>"An inertial reference frame."</b> The slide's axes (to the planet, along the velocity) turn with the orbit. That is the orbital frame. Both are used.</li></ul></div></div>
<div><div class="card" style="padding:8px 13px"><h3>🔎 Caption errors</h3>
<table class="t" style="font-size:10px"><tr><th>Captions said</th><th>Instructor meant</th></tr>
<tr><td>"A.D.C. s"</td><td><b>ADCS</b></td></tr>
<tr><td>"odorant itself"</td><td><b>orient</b> itself</td></tr>
<tr><td>"attitude areas", "area of altitude"</td><td>attitude <b>errors</b></td></tr>
<tr><td>"commands some talks", "actuating talks"</td><td>commands some <b>torques</b></td></tr>
<tr><td>"de-activate is able"</td><td><b>the actuator</b> is able</td></tr>
<tr><td>"the attitude cheater", "altitude data"</td><td>the attitude <b>jitter</b></td></tr>
<tr><td>"talk free rotational dynamics"</td><td><b>torque-free</b> rotational dynamics</td></tr>
<tr><td>"spin Stavely", "staple all spin"</td><td>spin <b>stably</b>, <b>stable</b> spin</td></tr>
<tr><td>"momentum of inertia", "moment to finish"</td><td><b>moment of inertia</b></td></tr>
<tr><td>"Selinda" · "the bass playing"</td><td><b>cylinder</b> · the <b>base plane</b></td></tr>
<tr><td>"this poor Nick", "this public"</td><td><b>Sputnik</b></td></tr>
<tr><td>"Ferric spacecraft"</td><td><b>spherical</b> spacecraft</td></tr>
<tr><td>"the exposure from 1958"</td><td>the <b>Explorer</b> from 1958</td></tr></table></div>
<div class="card" style="margin-top:9px;padding:8px 13px"><h3>🗣 Say it out loud</h3>
<div style="font-size:11.5px;line-height:1.5"><b>Friend:</b> "How does a spacecraft know which way it's facing, and how does it turn with nothing to push on?"<br>
<b>You:</b> It runs a loop, like a thermostat. Sensors look at the stars or the Sun to measure which way it points. The computer compares that with where it should point. Then it twists itself a little, usually by spinning a wheel inside, and checks again. It never stops, and the pointing always trembles a tiny bit.<br>
<b>Friend:</b> "Why not just spin it like a top?"<br>
<b>You:</b> You can, but only the fat way. Things end up spinning with their weight as far from the axis as possible. America's first satellite was a pencil spun lengthwise and it was tumbling within hours.</div></div></div>
</div></div>'''

vocab = [("Attitude", "which way a spacecraft is pointing. Not its height: that is altitude.", "Repeat."),
("Orientation", "the direction something faces.", ""),
("ADCS", "attitude determination and control system: the parts that measure pointing and correct it.", ""),
("Axis / axes", "an imaginary line something turns around. Three of them, at right angles.", ""),
("Roll / pitch / yaw", "turning about the direction of travel / about the across-orbit axis / about the line to the planet.", "Wings tilt / nose up-down / nose left-right."),
("Central body", "the planet being orbited.", "Repeat."),
("Velocity direction", "the way the spacecraft is travelling.", ""),
("Angle of attack", "aircraft term: how far the nose points above the airflow. A pitch angle.", ""),
("Reference frame / inertial frame", "the set of directions you measure against / one fixed to the distant stars.", ""),
("Attitude determination", "measuring the orientation.", ""),
("Attitude control", "turning the spacecraft back to the wanted orientation.", ""),
("Closed feedback loop", "a system that measures its own result and keeps correcting it.", "A thermostat."),
("Dynamics", "how something moves under the pushes and twists on it.", ""),
("Sensor", "a device that measures: a star camera, a Sun detector, a spin meter.", "Repeat; next lecture."),
("On-board computer", "the spacecraft's processor. Compares measured with wanted.", ""),
("Attitude error", "the difference between where it points and where it should.", ""),
("Command", "an instruction sent to a device.", ""),
("Actuator", "a device that pushes or twists: a wheel, a thruster, a magnetic coil.", "Next lecture."),
("Torque", "a twisting push: force × lever arm. Captions write 'talk'.", "A wrench on a bolt."),
("Jitter", "fast, small trembling of the pointing direction.", ""),
("Phenomenon / phenomena", "something that happens and can be observed.", ""),
("Imprecision", "not being exact.", ""),
("Requirement / constraint", "what the mission needs / a limit that must not be broken.", "Repeat."),
("Torque-free", "with no outside twist acting.", ""),
("Rotational dynamics", "the physics of spinning things.", ""),
("Spin", "to turn about an axis through yourself.", ""),
("Stable / unstable", "returns after a nudge / runs away after a nudge.", ""),
("Moment of inertia", "how hard a body is to spin about a given axis. Depends on how far its mass is from that axis.", "The turning version of mass."),
("Maximum moment of inertia axis", "the axis the mass is, on average, farthest from.", "The 'fat way' to spin."),
("Homogeneous", "the same all the way through.", "Repeat."),
("Rigid", "does not bend or flex.", ""),
("Sphere / cylinder / disk", "ball / tube or rod / flat round plate.", ""),
("Center of mass", "the balance point of a body.", ""),
("Mass distribution", "where the mass is placed inside a body.", ""),
("Plane", "a flat sheet.", "Repeat."),
("Angular momentum", "amount of spin: moment of inertia × spin rate. Kept unless a torque acts.", "A skater pulling in her arms."),
("Flat spin", "a tumble about the biggest-inertia axis.", ""),
("Explorer 1", "the first US satellite, 1958. A 2 m pencil that found the radiation belts.", "Who's Who."),
("Sputnik 1", "the first satellite of all, USSR, 1957. A 58 cm ball that beeped for three weeks.", "Who's Who."),
("Radiation belts (Van Allen belts)", "rings of trapped high-energy particles around the Earth.", "Who's Who.")]
p4 = f'''<div class="page">{top(T("VOCABULARY"),'Every word used, <span>in plain English</span>',f'{len(vocab)} entries. "Repeat" = you have met it before.')}
<div class="gl2" style="font-size:10.3px;line-height:1.35">{"".join(f"<div><b>{esc(a)}</b> — {esc(b)}{(' <i>'+esc(c)+'</i>') if c else ''}</div>" for a,b,c in vocab)}</div></div>'''
write('s6-l1.html', [p1, p1b, p2, p3, p4])
print('ok', len(vocab))
