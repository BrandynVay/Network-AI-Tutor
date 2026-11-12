import math
from lib import *
B = "SEC 5 · LEC 1 · COMMUNICATIONS: ANTENNAS"
T = lambda x: B.replace("COMMUNICATIONS: ANTENNAS", x)
DEFS = '<defs><marker id="ar" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#111"/></marker><marker id="ar2" markerWidth="6" markerHeight="6" refX="1" refY="3" orient="auto"><path d="M6,0 L0,3 L6,6 z" fill="#111"/></marker></defs>'

def wave(x0, x1, y, amp, fn, sw=1.6, dash=""):
    pts = []
    x = x0
    while x <= x1 + 0.01:
        t = (x - x0) / (x1 - x0)
        pts.append("%.1f,%.1f" % (x, y - amp * fn(t)))
        x += 0.5
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return '<polyline points="%s" fill="none" stroke="#111" stroke-width="%s"%s/>' % (" ".join(pts), sw, d)

two_pi = 2 * math.pi
main = wave(20, 308, 70, 26, lambda t: math.sin(two_pi * (t * 288) / 96), 2.2)
sig = wave(70, 320, 312, 9, lambda t: math.sin(two_pi * t), 1.8)
car = wave(70, 320, 338, 8, lambda t: math.sin(two_pi * 16 * t), 1.2)
am = wave(70, 320, 366, 12, lambda t: (1 + 0.6 * math.sin(two_pi * t)) / 1.6 * math.sin(two_pi * 16 * t), 1.2)
fm = wave(70, 320, 396, 8, lambda t: math.sin(two_pi * 16 * t - 8 * math.cos(two_pi * t)), 1.2)

svgA = f'''<svg width="100%" height="428" viewBox="0 0 330 412" style="display:block" font-family="Verdana, sans-serif">{DEFS}
<text x="8" y="13" font-size="10" font-weight="bold" fill="#111">1 · A WAVE: wavelength and frequency</text>
<line x1="14" y1="70" x2="318" y2="70" stroke="#999" stroke-width="0.8"/>
{main}
<line x1="46" y1="32" x2="138" y2="32" stroke="#111" stroke-width="1.2" marker-end="url(#ar)" marker-start="url(#ar2)"/>
<line x1="44" y1="28" x2="44" y2="42" stroke="#777" stroke-width="0.8"/><line x1="140" y1="28" x2="140" y2="42" stroke="#777" stroke-width="0.8"/>
<text x="92" y="27" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">λ = wavelength</text>
<text x="322" y="27" text-anchor="end" font-size="8.5" fill="#111">crest to crest, in metres</text>
<text x="8" y="114" font-size="8.5" fill="#111">f = frequency = waves passing per second (hertz, Hz)</text>
<text x="165" y="131" text-anchor="middle" font-size="10" font-weight="bold" fill="#111">c = λ × f  ·  c = 300,000 km/s, always</text>
<text x="165" y="144" text-anchor="middle" font-size="8.5" fill="#111">so: higher frequency → shorter wavelength</text>
<line x1="8" y1="152" x2="322" y2="152" stroke="#bbb" stroke-width="1"/>
<text x="8" y="167" font-size="10" font-weight="bold" fill="#111">2 · ANTENNA = metal rod, half a wave long</text>
<line x1="72" y1="187" x2="258" y2="187" stroke="#111" stroke-width="1" marker-end="url(#ar)" marker-start="url(#ar2)"/>
<text x="165" y="183" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">λ ÷ 2</text>
<line x1="70" y1="198" x2="158" y2="198" stroke="#111" stroke-width="3.2"/><line x1="172" y1="198" x2="260" y2="198" stroke="#111" stroke-width="3.2"/>
<line x1="158" y1="198" x2="158" y2="214" stroke="#111" stroke-width="1.4"/><line x1="172" y1="198" x2="172" y2="214" stroke="#111" stroke-width="1.4"/>
<rect x="143" y="214" width="44" height="15" rx="3" fill="#ddd" stroke="#111" stroke-width="1.4"/><text x="165" y="225" text-anchor="middle" font-size="8" font-weight="bold" fill="#111">radio</text>
<text x="8" y="246" font-size="8.5" fill="#111">the wave pushes electrons to and fro in the rod → a voltage</text>
<text x="8" y="258" font-size="8.5" fill="#111">FM radio 100 MHz: λ = 3 m → rod 1.5 m</text>
<text x="8" y="270" font-size="8.5" font-weight="bold" fill="#111">voice 100 Hz: λ = 3,000 km → rod 1,500 km. Impossible.</text>
<line x1="8" y1="279" x2="322" y2="279" stroke="#bbb" stroke-width="1"/>
<text x="8" y="294" font-size="10" font-weight="bold" fill="#111">3 · MODULATION: the voice rides a fast carrier</text>
<g font-size="8.5" font-weight="bold" fill="#111"><text x="8" y="315">signal</text><text x="8" y="341">carrier</text><text x="8" y="369">AM</text><text x="8" y="399">FM</text></g>
{sig}{car}{am}{fm}
</svg>'''

svgB = f'''<svg width="100%" height="428" viewBox="0 0 330 412" style="display:block" font-family="Verdana, sans-serif">{DEFS}
<text x="8" y="13" font-size="10" font-weight="bold" fill="#111">1 · THREE WAYS TO SPREAD THE SIGNAL</text>
<circle cx="56" cy="74" r="34" fill="none" stroke="#111" stroke-width="1.4" stroke-dasharray="5 4"/><circle cx="56" cy="74" r="3" fill="#111"/>
<line x1="165" y1="44" x2="165" y2="104" stroke="#111" stroke-width="3.2"/>
<ellipse cx="141" cy="74" rx="22" ry="15" fill="none" stroke="#111" stroke-width="1.4" stroke-dasharray="5 4"/><ellipse cx="189" cy="74" rx="22" ry="15" fill="none" stroke="#111" stroke-width="1.4" stroke-dasharray="5 4"/>
<path d="M236,50 Q222,74 236,98" fill="none" stroke="#111" stroke-width="3"/>
<path d="M238,74 Q282,56 320,74 Q282,92 238,74 z" fill="none" stroke="#111" stroke-width="1.4" stroke-dasharray="5 4"/><path d="M238,74 Q250,46 262,52 Q256,66 238,74 z" fill="none" stroke="#111" stroke-width="1" stroke-dasharray="3 3"/><path d="M238,74 Q250,102 262,96 Q256,82 238,74 z" fill="none" stroke="#111" stroke-width="1" stroke-dasharray="3 3"/>
<g font-size="8.5" fill="#111"><text x="56" y="124" text-anchor="middle" font-weight="bold">ISOTROPIC</text><text x="56" y="136" text-anchor="middle">every direction</text><text x="56" y="148" text-anchor="middle">ideal only · gain 1</text>
<text x="165" y="124" text-anchor="middle" font-weight="bold">OMNI (dipole)</text><text x="165" y="136" text-anchor="middle">all around the rod</text><text x="165" y="148" text-anchor="middle">none off the ends</text>
<text x="274" y="124" text-anchor="middle" font-weight="bold">DIRECTIONAL (dish)</text><text x="274" y="136" text-anchor="middle">main lobe + side lobes</text><text x="274" y="148" text-anchor="middle">gain 1,000s</text></g>
<line x1="8" y1="158" x2="322" y2="158" stroke="#bbb" stroke-width="1"/>
<text x="8" y="173" font-size="10" font-weight="bold" fill="#111">2 · GAIN = same power, squeezed into a beam</text>
<circle cx="60" cy="222" r="7" fill="#fff" stroke="#111" stroke-width="1.8"/>
<g stroke="#111" stroke-width="1"><line x1="60" y1="210" x2="60" y2="194"/><line x1="60" y1="234" x2="60" y2="250"/><line x1="48" y1="222" x2="32" y2="222"/><line x1="72" y1="222" x2="88" y2="222"/><line x1="51" y1="213" x2="40" y2="202"/><line x1="69" y1="213" x2="80" y2="202"/><line x1="51" y1="231" x2="40" y2="242"/><line x1="69" y1="231" x2="80" y2="242"/></g>
<text x="60" y="266" text-anchor="middle" font-size="8.5" fill="#111">bare bulb: dim everywhere</text>
<path d="M188,198 Q170,222 188,246" fill="none" stroke="#111" stroke-width="3"/><circle cx="192" cy="222" r="5" fill="#fff" stroke="#111" stroke-width="1.6"/>
<g stroke="#111" stroke-width="1.1"><line x1="200" y1="208" x2="312" y2="204" marker-end="url(#ar)"/><line x1="200" y1="222" x2="314" y2="222" marker-end="url(#ar)"/><line x1="200" y1="236" x2="312" y2="240" marker-end="url(#ar)"/></g>
<text x="322" y="198" text-anchor="end" font-size="8.5" font-weight="bold" fill="#111">beamwidth</text>
<text x="250" y="266" text-anchor="middle" font-size="8.5" fill="#111">same bulb + reflector: bright far away</text>
<text x="165" y="282" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">An antenna adds no power. It aims it.</text>
<line x1="8" y1="292" x2="322" y2="292" stroke="#bbb" stroke-width="1"/>
<text x="8" y="307" font-size="10" font-weight="bold" fill="#111">3 · HIGH GAIN vs LOW GAIN</text>
<g font-size="8.5" fill="#111">
<rect x="8" y="314" width="152" height="92" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="84" y="328" text-anchor="middle" font-weight="bold">HIGH-GAIN (dish)</text>
<text x="15" y="343">narrow beam</text><text x="15" y="356">strong signal, fast data</text><text x="15" y="369">must point at Earth</text><text x="15" y="382">Cassini: 4 m dish</text><text x="15" y="395">Apollo rover: TV dish</text>
<rect x="170" y="314" width="152" height="92" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="246" y="328" text-anchor="middle" font-weight="bold">LOW-GAIN (rod)</text>
<text x="177" y="343">wide beam</text><text x="177" y="356">weak signal, slow data</text><text x="177" y="369">works in any attitude</text><text x="177" y="382">CubeSat: crossed dipoles</text><text x="177" y="395">Apollo rover: voice, driving</text>
</g></svg>'''

p1 = spread(B, 'Ripples you can <span>write on</span>', 'S5 / L1 (1/2) — Waves + modulation', svgA,
 "λ arrow = one wavelength · thick bar = antenna rod · row 1 = your voice · row 2 = carrier · AM = height changes · FM = spacing changes",
 ["1. Radio is an electromagnetic wave. c = λ × f, and c never changes.",
  "2. Antenna ≈ half a wavelength, so high frequency = small antenna.",
  "3. Modulation: a slow signal rides a fast carrier (AM height, FM frequency)."],
 ['What carries the information through space?', 'The two fields: what are they, how are they arranged?', 'Wavelength? Frequency? Units?',
  'The formula that links them?', 'How does an antenna receive? Transmit?', 'What sets the size of an antenna?',
  'Why can\'t you transmit a voice directly?', 'What is modulation? What is a carrier?', 'AM vs FM?', '<span class="hl b">? is my voice a radio wave</span>'],
 ['<span class="hl y">electromagnetic (EM) wave</span> carries the signal · crosses empty space',
  '<span class="hl y">electric field</span> ⊥ <span class="hl y">magnetic field</span> · <span class="hl y">sinusoidal</span> (smooth, repeating)',
  '<span class="hl y">wavelength λ</span> = crest to crest (m) · <span class="hl y">frequency f</span> = waves per second (<span class="hl y">Hz</span>)',
  '<span class="hl k">c = λ × f</span> · c = <span class="hl k">3×10⁸ m/s</span>, constant → f up, λ down',
  'receive: the wave\'s electric field → <span class="hl y">voltage</span> in the antenna at the same f → receiver reads it',
  'transmit: the reverse · the same antenna does both',
  'antenna size ≈ <span class="hl k">λ ÷ 2</span> (<span class="hl y">dipole</span>) → higher f = <span class="hl g">smaller antenna</span>',
  'voice ~100 Hz → λ = 3,000 km → antenna <span class="hl o">1,500 km</span> ✗',
  '<span class="hl y">modulation</span>: put the slow <span class="hl y">information signal</span> on a fast <span class="hl y">carrier signal</span>',
  '<span class="hl y">AM</span>: carrier\'s height follows the signal · <span class="hl y">FM</span>: carrier\'s frequency follows it'])
p1b = spread(B, 'A flashlight <span>for radio</span>', 'S5 / L1 (2/2) — Directivity + gain', svgB,
 "dashed outline = where the signal goes · big petal = main lobe, small = side lobes · thick line = antenna",
 ["1. Isotropic = everywhere · omni = all around a rod · directional = one beam.",
  "2. Gain concentrates power into a beam. It never creates power.",
  "3. High gain = fast data but must be aimed. Low gain = slow but always works."],
 ['Isotropic antenna?', 'Omnidirectional?', 'Directional? What is beamwidth?', 'What is gain, really?', 'Does an antenna add power?',
  'What does high gain cost you?', 'Why does a CubeSat use dipoles?', 'Why must Cassini\'s dish point at Earth?', 'High-gain vs low-gain: when each?',
  '<span class="hl b">? how can 20 watts reach Earth from Saturn</span>'],
 ['<span class="hl y">directivity</span> = how much an antenna favors one direction',
  '<span class="hl y">isotropic</span>: equal in ALL directions (a sphere) · ideal only · the reference',
  '<span class="hl y">omnidirectional</span>: equal all around in one plane · e.g. a <span class="hl y">dipole</span>',
  '<span class="hl y">directional</span>: one <span class="hl y">main lobe</span> + small <span class="hl y">side lobes</span> · <span class="hl y">beamwidth</span> = angle where power is still above half (<span class="hl k">3 dB</span>) · dish, rooftop TV antenna',
  '<span class="hl y">gain</span> = increase in signal strength due to directivity (vs isotropic) · more directional = more gain',
  'an antenna adds <span class="hl o">no power</span>: it concentrates it',
  'high gain → better signal, more data · but must point exactly → attitude control',
  'CubeSat: two crossed dipoles → works whichever way it faces · weak signal',
  'Cassini: <span class="hl k">4 m</span> <span class="hl y">high-gain antenna</span>, must point at Earth',
  'Apollo 17 rover: <span class="hl y">low-gain</span> (wide, while driving) + high-gain dish (aimed, for TV)'])

p2 = f'''<div class="page">{top(T("TEACH"),'A 20-watt whisper <span>from Saturn</span>','Simple story first, then the official names, then how it actually works with numbers you can check.')}
<div class="eli"><b style="font-size:14px">🧒 Like you're 5</b><br>
Drop a stone in a pond and ripples spread out. A radio wave is a ripple too, but in electricity and magnetism, and it needs no water and no air, so it crosses empty space at the speed of light. An <b>antenna</b> is a metal stick. When the ripple washes over it, it pushes the electricity inside the stick back and forth, like a cork bobbing, and the radio reads the bobbing. To send, do the reverse: shake the electricity in the stick and ripples fly off.<br>
The stick works best when it is half as long as one ripple. Voice ripples are slow and would be 3,000 km long, so the stick would be longer than Texas. So we cheat. We take a fast, short ripple, the <b>carrier</b>, and make it carry the voice by changing its height (<b>AM</b>) or squeezing its spacing (<b>FM</b>) in step with the voice. Last trick: a bare bulb lights a room dimly, but the same bulb in a flashlight throws a bright spot far away. A dish antenna is a flashlight for radio. That is <b>gain</b>. The Cassini probe talked to Earth from Saturn with 20 watts, a fridge bulb, because its 4-metre dish squeezed everything into one thin beam aimed exactly at us.</div>
<div class="two">
<div class="card" style="padding:9px 13px"><h3>🏷 The official names (name first, then what it means)</h3>
<ul class="names" style="font-size:10.7px">
<li><b>Electromagnetic wave</b> (EM wave, electromagnetic radiation): a travelling ripple of electric and magnetic field. Radio, microwaves, light, UV and X-rays are all the same thing at different frequencies: the <b>electromagnetic spectrum</b>.</li>
<li><b>Wavelength, λ</b> ("lambda"): distance from one crest to the next. <b>Frequency, f</b>: waves per second, in <b>hertz</b> (Hz; kHz, MHz, GHz = thousand, million, billion). <b>Period</b>: seconds per wave, 1 ÷ f.</li>
<li><b>Speed of light, c</b>: 299,792 km/s. <b>c = λ × f</b>.</li>
<li><b>Antenna</b>: a conductor that turns an electrical signal into a radio wave and back. <b>Transmitter</b> (TX), <b>receiver</b> (RX).</li>
<li><b>Half-wave dipole</b>: two rods end to end, λ ÷ 2 in total. The basic antenna. A <b>monopole</b> is half of one (λ ÷ 4), like a car aerial.</li>
<li><b>Modulation</b>: changing a carrier wave so that it carries information. <b>Carrier signal</b>: the fast wave. <b>Information signal</b> (baseband, message): the slow one.</li>
<li><b>Amplitude modulation, AM</b> / <b>frequency modulation, FM</b>. Spacecraft actually use <b>phase modulation</b> (phase-shift keying, PSK) to send digital bits.</li>
<li><b>Radiation pattern</b>: the shape of where an antenna sends its power. <b>Isotropic radiator</b>, <b>omnidirectional antenna</b>, <b>directional antenna</b>.</li>
<li><b>Directivity</b> and <b>antenna gain</b>: how many times stronger the signal is in the best direction than from an isotropic antenna. Written in <b>dBi</b>: 10 dBi = 10×, 20 = 100×, 30 = 1,000×.</li>
<li><b>Main lobe</b> and <b>side lobes</b>: the big beam and the small leaks beside it. <b>Half-power beamwidth</b> (3 dB beamwidth): the angle across the main lobe between the points where power has fallen to half. <b>Aperture</b>: the antenna's collecting area.</li>
<li><b>High-gain antenna, HGA</b> / <b>low-gain antenna, LGA</b>. <b>Parabolic reflector</b> (dish).</li>
</ul></div>
<div class="card" style="padding:9px 13px"><h3>🛠 How it actually works</h3>
<table class="mech" style="font-size:10.2px"><tr><th style="width:68px">Step</th><th>The mechanism, with numbers</th></tr>
<tr><td><b>1 · The wave</b></td><td>A changing electric field makes a changing magnetic field, which makes a changing electric field… The pair keeps itself going, at right angles to each other and to the direction of travel, at 299,792 km/s. No medium needed.</td></tr>
<tr><td><b>2 · c = λ × f</b></td><td>FM radio 100 MHz: 300,000,000 ÷ 100,000,000 = <b>3 m</b>. Wi-Fi 2.4 GHz: <b>12.5 cm</b>. Deep-space link 8.4 GHz: <b>3.6 cm</b>.</td></tr>
<tr><td><b>3 · Receive</b></td><td>Metal is full of loose electrons. The wave's electric field shoves them one way, then the other, so a tiny alternating voltage appears along the rod at the wave's frequency: millionths of a volt. A rod half a wave long fits the wave exactly and rings loudest, like a guitar string.</td></tr>
<tr><td><b>4 · Transmit</b></td><td>The reverse. Drive an alternating voltage into the rod; electrons shaken back and forth give off a wave at that frequency.</td></tr>
<tr><td><b>5 · Size</b></td><td>Rod = λ ÷ 2. 100 MHz → 1.5 m. 2.4 GHz → 6 cm. 100 Hz → 1,500 km. That is why nothing is transmitted at voice frequency.</td></tr>
<tr><td><b>6 · Modulate</b></td><td>AM radio: a 1 MHz carrier whose height follows the voice. FM radio: a 100 MHz carrier whose frequency swings ±75 kHz with it. Digital links flip the carrier's phase to mean 1 or 0.</td></tr>
<tr><td><b>7 · Gain</b></td><td>A dish D wide squeezes the beam: gain ≈ ½ × (π × D ÷ λ)². Cassini: 4 m at 3.6 cm → about <b>50,000×</b> (47 dBi). Beamwidth ≈ 70 × λ ÷ D ≈ <b>0.6°</b>.</td></tr>
<tr><td><b>8 · What it buys</b></td><td>Cassini's transmitter: <b>20 W</b>. Through the dish, toward Earth it looked like 1,000,000 W. After 1.4 billion km, a 70 m dish on Earth caught about 0.0000000000000001 W (10⁻¹⁶). Still readable.</td></tr></table></div>
</div></div>'''

p3 = f'''<div class="page">{top(T("BANDS + FACT CHECK"),'Same wave, <span>different sizes</span>','The frequency bands (including ones you already use), the caption errors, and where the instructor was loose.')}
<div class="card" style="padding:8px 13px;margin-bottom:9px"><h3>📻 Check c = λ × f on things you know</h3>
<table class="mech" style="font-size:10.4px"><tr><th>Band</th><th>Frequency</th><th>Wavelength λ</th><th>Half-wave rod</th><th>Who uses it</th></tr>
<tr><td><b>AM radio</b></td><td>1 MHz</td><td>300 m</td><td>150 m</td><td>AM stations. Their towers are a quarter-wave, about 75 m.</td></tr>
<tr><td><b>FM radio</b></td><td>100 MHz</td><td>3 m</td><td>1.5 m</td><td>FM stations. A car aerial is a quarter-wave, 75 cm.</td></tr>
<tr><td><b>UHF</b></td><td>437 MHz</td><td>69 cm</td><td>34 cm</td><td>CubeSats: the tape-measure antennas in the lecture's picture.</td></tr>
<tr><td><b>L-band</b></td><td>1.575 GHz</td><td>19 cm</td><td>9.5 cm</td><td>GPS.</td></tr>
<tr><td><b>S-band</b></td><td>2.4 GHz</td><td>12.5 cm</td><td>6 cm</td><td>Wi-Fi and Bluetooth. Spacecraft command links sit nearby at 2.1–2.3 GHz.</td></tr>
<tr><td><b>X-band</b></td><td>8.4 GHz</td><td>3.6 cm</td><td>1.8 cm</td><td>Deep-space downlinks: Voyager, Cassini, the Mars orbiters.</td></tr>
<tr><td><b>Ka-band</b></td><td>32 GHz</td><td>9 mm</td><td>5 mm</td><td>The newest high-rate deep-space links.</td></tr>
<tr><td><b>Visible light</b></td><td>600,000 GHz</td><td>0.0005 mm</td><td>—</td><td>Your eyes. Ultraviolet from Section 2 is just past it.</td></tr></table>
<div style="font-size:10.4px;margin-top:3px">You already own the proof: the stubby antennas on a Wi-Fi router are about 3 cm, a quarter of 12.5 cm.</div></div>
<div class="two">
<div class="card" style="padding:8px 13px"><h3>🔎 Caption errors (the worst transcript so far)</h3>
<table class="t" style="font-size:9.8px"><tr><th>Captions said</th><th>Instructor meant</th></tr>
<tr><td>"electric in a negative way", "it two magnetic waves"</td><td><b>electromagnetic wave(s)</b></td></tr>
<tr><td>"this to Bush tends to be seen as soil"</td><td>the <b>distribution</b> tends to be <b>sinusoidal</b></td></tr>
<tr><td>"Nalanda" · "units of Kurds"</td><td><b>lambda</b> (λ) · units of <b>hertz</b></td></tr>
<tr><td>"describing a scene disorder"</td><td>describing a <b>sinusoid</b></td></tr>
<tr><td>"a hundred foot" · "ten to the light"</td><td>a hundred <b>hertz</b> · ten to the <b>eight</b></td></tr>
<tr><td>"deep hole antenna"</td><td><b>dipole</b> antenna</td></tr>
<tr><td>"I am an F Am" · "amplitude in moderation"</td><td><b>AM and FM</b> · amplitude <b>modulation</b></td></tr>
<tr><td>"the main canvasing"</td><td>the main <b>carrier signal</b></td></tr>
<tr><td>"indoor activity" · "beam with"</td><td><b>antenna directivity</b> · <b>beamwidth</b></td></tr>
<tr><td>"ID or isotropic" · "higher gangs"</td><td><b>ideal</b> isotropic · higher <b>gains</b></td></tr>
<tr><td>"Phi game in tennis" · "parabolic tunnels"</td><td><b>high-gain antennas</b> · parabolic <b>antennas</b></td></tr>
<tr><td>"cube set"</td><td><b>CubeSat</b></td></tr></table></div>
<div class="card" style="padding:8px 13px"><h3>▲ Where the instructor was loose</h3>
<ul class="r" style="font-size:10.5px">
<li><b>"The wavelength of my voice."</b> Your voice is a sound wave: air pressure, 343 m/s, and it cannot cross a vacuum at all. A microphone turns it into a voltage wiggling at the same frequency. His 3,000 km is what a <i>radio</i> wave at 100 Hz would measure. His arithmetic is right.</li>
<li><b>Modulation "so antennas can be small."</b> True, and only one reason of three. It also lets thousands of users share the air, each on its own carrier frequency (that is what tuning to a station is), and a faster carrier can carry more data per second.</li>
<li><b>AM and FM are not what spacecraft use.</b> Both are analog. Space links and Wi-Fi send bits by shifting the carrier's phase.</li>
<li><b>"The higher the frequency, the smaller the antenna"</b> is for rods. A dish is different: it must be many wavelengths wide, and for the same dish a higher frequency gives a tighter beam and more gain.</li>
<li><b>"With a directional antenna we can get more information."</b> Precisely: gain compares the signal in the best direction with an isotropic antenna fed the same power. The antenna creates nothing. It moves power from where you don't need it to where you do.</li>
<li><b>Apollo 17.</b> His explanation tangles. The Moon rover carried two antennas: a low-gain one with a wide beam for voice while driving, and an umbrella-shaped high-gain dish the astronauts aimed at Earth by hand for television when parked.</li>
<li><b>Not said: polarization.</b> The receiving rod has to line up with the wave's electric field. It is the real reason the CubeSat has two dipoles at right angles.</li>
<li><b>Not said: an isotropic antenna cannot be built.</b> It is a yardstick only.</li></ul></div>
</div></div>'''

vocab = [("Telecommunications", "sending information over a distance. Here: by radio between spacecraft and ground.", ""),
("Signal / information", "a quantity that changes in a pattern that means something: a voice, a picture, data.", ""),
("Electromagnetic (EM) wave", "a travelling ripple of electric and magnetic field. Radio and light are both this.", "A ripple that needs no pond."),
("Electric field / magnetic field", "the region where a charge feels a push / where a magnet does. In a wave the two rise and fall together.", "Electric field is a repeat."),
("Perpendicular (⊥)", "at right angles, like the corner of a page.", ""),
("Sinusoidal / sinusoid / sine wave", "the smooth, endlessly repeating up-and-down shape.", ""),
("Variation / oscillating", "changing / swinging back and forth regularly.", ""),
("Voltage / difference in voltage", "electrical 'height' between two points. It makes current flow.", "Repeat, ion engines."),
("Induce", "to cause at a distance. The wave induces a voltage in the antenna.", ""),
("Speed of light (c)", "299,792 km/s, about 3×10⁸ m/s. The speed of every electromagnetic wave in vacuum.", ""),
("Wavelength (λ, 'lambda')", "distance from one crest to the next, in metres.", "Repeat, UV in Section 2."),
("Frequency (f)", "how many waves pass per second.", ""),
("Hertz (Hz) / kHz / MHz / GHz", "one per second / thousand / million / billion per second.", ""),
("Period", "how long one wave takes: 1 ÷ frequency.", ""),
("Constant", "a value that never changes. c is one.", "Repeat."),
("Inversely related", "when one goes up the other goes down.", ""),
("Antenna", "a metal conductor that turns electrical signals into radio waves and back.", "A stick that bobs on the ripples."),
("Transmitter / receiver", "the electronics that drive the antenna / that read what it picks up.", ""),
("Circuit", "a loop of electronic parts that current flows through.", ""),
("Dipole (half-wave dipole)", "two rods end to end, half a wavelength long in total.", ""),
("Dimension", "a size: length, width, diameter.", ""),
("Modulation", "changing a carrier wave in step with a signal so the carrier carries it.", "Writing on the ripples."),
("Carrier signal", "the fast, steady wave that does the travelling.", ""),
("Information signal (baseband)", "the slow signal you actually want to send.", ""),
("Amplitude", "the height of a wave.", ""),
("Amplitude modulation (AM)", "the carrier's height follows the signal.", ""),
("Frequency modulation (FM)", "the carrier's frequency follows the signal. Resists static better.", ""),
("Phase modulation / PSK", "shifting the carrier's timing to send bits. What spacecraft use.", ""),
("Directivity", "how strongly an antenna favors one direction.", ""),
("Radiation pattern", "the 3-D shape of where an antenna's power goes.", ""),
("Isotropic antenna", "an imaginary antenna that radiates equally in every direction.", "Bare bulb."),
("Homogeneous", "the same everywhere.", ""),
("Omnidirectional antenna", "equal all around in one plane: a donut shape.", ""),
("Directional antenna", "sends most of its power one way.", "Flashlight."),
("Beam / beamwidth", "the cone where the signal is strong / its angle in degrees.", ""),
("Main lobe / side lobes", "the big petal where most power goes / the small unwanted petals beside it.", ""),
("3 dB / decibel (dB)", "3 dB down means half the power. Decibels count in multiplications: 10 dB = ×10.", ""),
("Aperture / large aperture", "the opening or collecting area of an antenna. Bigger aperture, narrower beam.", ""),
("Gain / dBi", "how many times stronger than isotropic in the best direction / the unit it is quoted in.", ""),
("Parabolic antenna (dish)", "a curved reflector that focuses radio waves into a beam.", ""),
("High-gain antenna (HGA)", "a narrow-beam dish for fast data. Has to be aimed.", ""),
("Low-gain antenna (LGA)", "a wide-beam antenna for slow, always-available contact.", ""),
("Rooftop TV antenna (Yagi)", "the fishbone-shaped directional antenna on houses.", ""),
("Polarization", "the direction the wave's electric field swings in.", ""),
("CubeSat", "a tiny satellite built from 10 cm cubes.", "Who's Who."),
("Cassini", "NASA's Saturn orbiter, 2004–2017, with a 4 m dish.", "Repeat, Who's Who."),
("Apollo 17 / lunar rover", "the last crewed Moon landing, 1972 / the car the astronauts drove.", "Who's Who."),
("Positioning / rotation = attitude", "which way the spacecraft points.", "Section 6.")]
p4 = f'''<div class="page">{top(T("VOCABULARY"),'Every word used, <span>in plain English</span>',f'{len(vocab)} entries. "Repeat" = you have met it before.')}
<div class="gl2" style="font-size:10px;line-height:1.32">{"".join(f"<div><b>{esc(a)}</b> — {esc(b)}{(' <i>'+esc(c)+'</i>') if c else ''}</div>" for a,b,c in vocab)}</div></div>'''

c1 = ("ELECTROMAGNETIC WAVE", "EM wave", "travelling ripple of electric + magnetic field", "it needs no air or wire, so it is the only way to carry information across space", "c = 299,792 km/s · radio, light, UV all the same thing", "sound (air pressure, 343 m/s, no vacuum)", "c = λ × f · spectrum · antenna")
c2 = ("WAVELENGTH + FREQUENCY", "λ and f", "crest-to-crest distance / waves per second", "speed is fixed, so the two are tied: pick one and the other is set. λ sets antenna size", "100 MHz → 3 m · 2.4 GHz → 12.5 cm · 8.4 GHz → 3.6 cm", "amplitude (the wave's height)", "c = λ × f · dipole = λ ÷ 2")
c3 = ("HALF-WAVE DIPOLE", "dipole antenna", "two rods end to end, λ ÷ 2 long in total", "a rod that fits half a wave resonates, so it gives the biggest voltage for that frequency", "FM 100 MHz → 1.5 m · Wi-Fi → 6 cm · voice 100 Hz → 1,500 km", "a dish (a reflector, many λ wide)", "omnidirectional · monopole = λ ÷ 4")
c4 = ("MODULATION", "AM · FM · PSK", "changing a carrier wave so it carries a signal", "voice-speed waves need 1,500 km antennas. A fast carrier fits a small antenna and its own channel", "AM: 1 MHz carrier · FM: 100 MHz ± 75 kHz", "amplification (just makes it louder)", "carrier · AM = height · FM = spacing")
c5 = ("ANTENNA GAIN", "dBi", "strength in the best direction vs isotropic", "power spread over a whole sphere is wasted. Squeeze it into a beam and the far end hears more", "dipole 1.6× · Cassini dish ~50,000× (47 dBi)", "added power (it only aims)", "≈ ½(πD ÷ λ)² · beamwidth ≈ 70λ ÷ D")
c6 = ("HIGH-GAIN vs LOW-GAIN", "HGA · LGA", "narrow-beam dish / wide-beam rod", "you want both: speed when you can aim, and a link that still works when you can't", "Cassini HGA 4 m, 0.6° beam · 20 W looks like 1 MW", "transmitter power (same either way)", "attitude control · safe mode · CubeSat")
cA, a1, a2 = cardpage(c1, c2, "C24", "scene 11"); cB, b1, b2 = cardpage(c3, c4, "C25", "scene 11"); cC, d1, d2 = cardpage(c5, c6, "C26", "scene 11")
p5 = f'''<div class="page">{top(T("COPY INTO NOTES"),'Where each piece goes <span>in the notebook</span>','Routes A to D for this lecture. The concept cards (route E) are on the next two pages.')}
<div class="two route">
<div class="card" style="padding:9px 13px"><h3>A · Equations &amp; key numbers page (p3–4)</h3>
<div class="copy">c = λ × f          c = 3×10⁸ m/s (299,792 km/s)
                   100 MHz → 3 m · 2.4 GHz → 12.5 cm
dipole = λ ÷ 2     100 MHz → 1.5 m · 100 Hz → 1,500 km
gain ≈ ½(πD ÷ λ)²  4 m dish at 3.6 cm → ~50,000× (47 dBi)
beam ≈ 70·λ ÷ D    → 0.6°
Cassini            20 W → looks like 1 MW → 10⁻¹⁶ W at Earth</div>
<h3>B · Section 5 map page (first sentence; more after the next lectures)</h3>
<div class="copy">S5 · antennas: radio = EM wave, c = λ × f; rod = λ ÷ 2 so
     high f = small; modulation = signal on a fast carrier;
     gain = aim the power (dish), costs pointing</div>
<h3>D · Question bank ("but how?" cards)</h3>
<div class="copy">Q: How does a metal rod pick up a radio wave?
A: The wave's electric field pushes the rod's electrons to
   and fro → an alternating voltage at the wave's frequency.
Q: Why does the rod have to be about half a wavelength?
A: It resonates: it fits the wave, like a guitar string.
Q: How does a dish make a signal stronger with no extra power?
A: It takes the power going everywhere and aims it one way.
Q: How did 20 W reach Earth from Saturn?
A: A 4 m dish gave ~50,000× gain, and a 70 m dish listened.</div></div>
<div class="card" style="padding:9px 13px"><h3>C · One-line word bank (new lines)</h3>
<div class="copy">p__ · electromagnetic wave · ripple of E + B field  → C24
p__ · electromagnetic spectrum · radio … light … X-rays
p__ · wavelength (λ) · crest to crest, metres  → C24
p__ · frequency (f) / hertz · waves per second  → C24
p__ · period · seconds per wave = 1 ÷ f
p__ · speed of light (c) · 3×10⁸ m/s; c = λ × f
p__ · sinusoid · the smooth repeating wave shape
p__ · amplitude · height of the wave
p__ · antenna · metal that turns signal ↔ radio wave
p__ · transmitter / receiver · sends / listens
p__ · dipole · rod λ ÷ 2 long; the basic antenna  → C25
p__ · modulation · signal written onto a carrier  → C25
p__ · carrier / information signal · fast wave / slow message
p__ · AM / FM · height follows signal / frequency follows it
p__ · phase modulation (PSK) · bits by shifting timing
p__ · isotropic · equal every direction; ideal only
p__ · omnidirectional · equal all around one plane
p__ · directional / beamwidth · one beam / its angle at half power
p__ · main lobe / side lobes · the beam / small leaks beside it
p__ · decibel (dB) · 3 dB = half or double; 10 dB = ×10
p__ · gain (dBi) · × stronger than isotropic  → C26
p__ · HGA / LGA · narrow fast dish / wide slow rod  → C26
p__ · polarization · direction the E field swings</div></div>
</div></div>'''
p6 = f'''<div class="page">{top(T("CONCEPT CARDS"),'Route E: <span>pages C24 and C25</span>','Two notebook pages, two cards each. Copy line for line; the faint numbers are your ruled lines.')}
<div style="display:flex;gap:16px;justify-content:center">{cA}{cB}</div>
<div style="text-align:center;font-size:10.5px;color:#444;margin-top:6px">C24: {a1} + {a2} lines of 22 · C25: {b1} + {b2} lines of 22</div></div>'''
p7 = f'''<div class="page">{top(T("CONCEPT CARDS"),'Route E: <span>page C26</span>','The third card page for this lecture.')}
<div style="display:flex;gap:22px;justify-content:center;align-items:flex-start">{cC}
<div class="card" style="width:4.3in;padding:12px 16px;font-size:12px;line-height:1.5"><h3>Why this lecture got two spreads</h3>
It is the longest lecture so far and it holds two separate ideas: how a wave carries a signal (waves, antenna size, modulation), and how you aim it (directivity, gain). Your rule is one spread per video unless it doesn't fit, and never smaller writing. This one doesn't fit.<br><br>
<b>If you are short on pages</b>, copy spread 1 in full and add only the drawing from spread 2 under it. The gain idea is the one thing in spread 2 you can't skip.<br><br>
<b>You already know half of this.</b> This is the physical layer under everything in networking: 2.4 GHz and 5 GHz Wi-Fi, antenna gain in dBi, why a directional antenna reaches farther. Use that. When Network+ resumes, this page is a head start on the wireless objectives.<br><br>
C26: {d1} + {d2} lines of 22.</div></div></div>'''
p8 = f'''<div class="page">{top(T("SAY IT OUT LOUD"),'Last page: <span>prove it by talking</span>','After the spreads and the 3-line summaries, with everything closed. Send me what you said and I will grade it like a friend would.')}
<div class="two"><div>
<div class="card"><h3>🗣 The friend's opening question</h3><div style="font-size:13px;line-height:1.5">"How does a probe at Saturn talk to Earth? It can't have much power out there."</div></div>
<div class="card" style="margin-top:12px"><h3>✅ Three sentences you should be able to say</h3><ul class="r" style="font-size:12px">
<li>By radio, which is a ripple of electricity and magnetism that crosses empty space at the speed of light. An antenna is just a metal rod the ripple shakes.</li>
<li>You can't send a voice or data directly, because slow signals would need an antenna thousands of kilometres long. So you write the signal onto a fast carrier wave. That is modulation.</li>
<li>And it has very little power: Cassini had 20 watts. But a big dish squeezes it into a beam half a degree wide, which makes it tens of thousands of times stronger in our direction, as long as the dish points exactly at Earth.</li></ul></div>
<div class="card" style="margin-top:12px"><h3>❓ Follow-ups a friend might ask</h3><ul class="r" style="font-size:12px">
<li>"Why does frequency matter?" (frequency times wavelength is always the speed of light, and the antenna has to be about half a wavelength)</li>
<li>"AM and FM, what's the difference?" (AM changes the carrier's height, FM changes its spacing)</li>
<li>"Does a dish add power?" (no, it only aims what is there, like a flashlight reflector)</li>
<li>"What if the dish isn't pointing at Earth?" (you fall back to a low-gain antenna: wide beam, very slow)</li>
<li>"Is that the same as Wi-Fi?" (same physics: 2.4 GHz is a 12.5 cm wave, and router antennas are a quarter of that)</li></ul></div></div>
<div><div class="card" style="min-height:3.2in"><h3>📝 Your explanation (paste or dictate)</h3><div style="border:2px dashed #999;border-radius:8px;height:2.5in;padding:8px;color:#999;font-size:11px">_ send it to me in chat; I'll put it here _</div></div>
<div class="card" style="margin-top:12px;min-height:2.2in;border-color:var(--green)"><h3 style="color:var(--green)">🎯 My read</h3><div style="border:2px dashed #999;border-radius:8px;height:1.5in;padding:8px;color:#999;font-size:11px">solid on: _<br>fuzzy on: _<br>fix: _<br>→ question-bank cards: _</div></div>
<div class="callout" style="margin-top:12px;font-size:11.5px">⚡ Two more lectures in Section 5. Send them the same way.</div></div></div></div>'''
write('s5-l1.html', [p1, p1b, p2, p3, p4, p5, p6, p7, p8])
print('ok', a1, a2, b1, b2, d1, d2, len(vocab))
