from lib import *
B = "SEC 5 · LEC 3 · SATELLITE + SPACECRAFT LINKS"
T = lambda x: B.replace("SATELLITE + SPACECRAFT LINKS", x)

def box(x, y, t, w=84):
    return ('<rect x="%d" y="%d" width="%d" height="15" rx="3" fill="#fff" stroke="#111" stroke-width="1.4"/>'
            '<text x="%d" y="%d" text-anchor="middle" font-size="7.5" font-weight="bold" fill="#111">%s</text>') % (x, y, w, x + w / 2, y + 10.5, t)

left = box(8, 92, "HIGH-POWER AMP") + box(8, 111, "UP-CONVERTER") + box(8, 130, "MODULATOR") + box(8, 149, "ENCODER")
right = box(238, 92, "LOW-NOISE AMP") + box(238, 111, "DOWN-CONVERTER") + box(238, 130, "DEMODULATOR") + box(238, 149, "DECODER")
svg = f'''<svg width="100%" height="428" viewBox="0 0 330 412" style="display:block" font-family="Verdana, sans-serif">
<defs><marker id="ar" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#111"/></marker></defs>
<text x="8" y="13" font-size="10" font-weight="bold" fill="#111">1 · THE LINK IS A CHAIN</text>
<rect x="115" y="22" width="100" height="32" rx="5" fill="#ddd" stroke="#111" stroke-width="1.8"/>
<text x="165" y="35" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">SATELLITE</text>
<text x="165" y="47" text-anchor="middle" font-size="8" fill="#111">repeater: boost + resend</text>
{left}{right}
<path d="M34,86 Q50,68 66,86" fill="none" stroke="#111" stroke-width="2.4"/><line x1="50" y1="78" x2="50" y2="92" stroke="#111" stroke-width="1.4"/>
<path d="M264,86 Q280,68 296,86" fill="none" stroke="#111" stroke-width="2.4"/><line x1="280" y1="78" x2="280" y2="92" stroke="#111" stroke-width="1.4"/>
<line x1="60" y1="70" x2="113" y2="52" stroke="#111" stroke-width="1.6" marker-end="url(#ar)"/>
<line x1="217" y1="52" x2="270" y2="70" stroke="#111" stroke-width="1.6" stroke-dasharray="5 3" marker-end="url(#ar)"/>
<text x="8" y="60" font-size="8.5" font-weight="bold" fill="#111">UPLINK</text>
<text x="322" y="60" text-anchor="end" font-size="8.5" font-weight="bold" fill="#111">DOWNLINK</text>
<line x1="98" y1="164" x2="98" y2="94" stroke="#111" stroke-width="1.3" marker-end="url(#ar)"/>
<line x1="232" y1="94" x2="232" y2="164" stroke="#111" stroke-width="1.3" marker-end="url(#ar)"/>
<g font-size="8" fill="#111" text-anchor="middle"><text x="165" y="112">each box on the right</text><text x="165" y="123">undoes its partner</text><text x="165" y="134">on the left</text></g>
<text x="8" y="177" font-size="8" fill="#111">information in ↑</text>
<text x="322" y="177" text-anchor="end" font-size="8" fill="#111">↓ information out</text>
<line x1="8" y1="186" x2="322" y2="186" stroke="#bbb" stroke-width="1"/>
<text x="8" y="200" font-size="10" font-weight="bold" fill="#111">2 · POWER ALONG THE LINK</text>
<line x1="30" y1="292" x2="30" y2="208" stroke="#111" stroke-width="1.3" marker-end="url(#ar)"/>
<line x1="30" y1="292" x2="320" y2="292" stroke="#111" stroke-width="1.3" marker-end="url(#ar)"/>
<line x1="30" y1="248" x2="312" y2="248" stroke="#777" stroke-width="0.8" stroke-dasharray="3 3"/>
<polyline points="30,248 70,216 140,280 175,228 255,286 300,248" fill="none" stroke="#111" stroke-width="2.4"/>
<g font-size="8.5" font-weight="bold" fill="#111"><text x="74" y="214">HPA</text><text x="108" y="240">space loss</text><text x="180" y="224">repeater</text><text x="176" y="286">space loss</text><text x="304" y="270">LNA</text></g>
<text x="36" y="211" font-size="8" fill="#111">power</text>
<text x="322" y="304" text-anchor="end" font-size="8" fill="#111">along the link →</text>
<line x1="8" y1="310" x2="322" y2="310" stroke="#bbb" stroke-width="1"/>
<text x="8" y="324" font-size="10" font-weight="bold" fill="#111">3 · THE LINK EQUATION</text>
<rect x="24" y="331" width="282" height="24" rx="6" fill="#fff" stroke="#111" stroke-width="1.6"/>
<text x="165" y="347" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#111">S ÷ N₀ = P × Gₜ × (Gᵣ ÷ T)  ÷  (k × Lₛ × Lₐ)</text>
<g font-size="8.5" fill="#111">
<text x="8" y="370"><tspan font-weight="bold">helps:</tspan> power P · transmit gain Gₜ · receive gain Gᵣ</text>
<text x="8" y="383"><tspan font-weight="bold">hurts:</tspan> space loss Lₛ · air loss Lₐ · noise k × T</text>
<text x="8" y="396">S ÷ N₀ = signal compared with noise</text>
</g>
<text x="165" y="409" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">bigger S ÷ N₀ = more bits per second</text>
</svg>'''
p1 = spread(B, 'A chain, a loss, <span>and a ratio</span>', 'S5 / L3 — Satellite links', svg,
 "solid arrow = uplink · dashed arrow = downlink · curved line = dish · zigzag = signal power · dotted line = starting level",
 ["1. A link is a chain: every receive box undoes one transmit box.",
  "2. Space loss is spreading, not soaking up: twice as far = a quarter the power.",
  "3. What counts is signal ÷ noise: more power, bigger dishes, colder receiver."],
 ['What do encoders and decoders do?', 'Up-converter: what, and why after modulation?', 'HPA: where, and what for?', 'What two losses hit the signal in flight?',
  'What does a satellite repeater do?', 'LNA: where, and why "low noise"?', 'The whole chain, in order?', 'S ÷ N₀: what is it? High or low is good?',
  'Link equation: what helps, what hurts?', 'Why does the power graph zigzag?', '<span class="hl b">? what is k really</span>'],
 ['<span class="hl y">encoder / decoder</span>: convert information from one format or code to another (compress it, protect it) and back',
  '<span class="hl y">modulator / demodulator</span>: put the signal on a carrier / take it off',
  '<span class="hl y">up-converter</span>: raises the frequency (MHz or a few GHz → up to <span class="hl k">30 GHz</span>) · <span class="hl y">down-converter</span> reverses it',
  '<span class="hl y">HPA</span> (high-power amplifier): boosts the signal just before the antenna',
  'in flight: <span class="hl o">free-space loss</span> Lₛ (distance) + <span class="hl o">atmospheric loss</span> Lₐ',
  '<span class="hl y">satellite repeater</span>: boosts the signal on board and sends it back down',
  '<span class="hl y">LNA</span> (low-noise amplifier): boosts the weak received signal while adding as little noise as possible',
  'chain: encode → modulate → up-convert → HPA → antenna ⇒ LNA → down-convert → demodulate → decode',
  '<span class="hl y">S ÷ N₀</span> = signal over noise · high = <span class="hl g">lots of information</span>',
  'S ÷ N₀ = P × Gₜ × (Gᵣ ÷ T) ÷ (k × Lₛ × Lₐ)',
  'P power · Gₜ Gᵣ antenna gains · T noise temperature · k <span class="hl y">Boltzmann constant</span>'])

p2 = f'''<div class="page">{top(T("TEACH"),'Shouting across <span>a stadium</span>','Simple story first, then the official names, then how it actually works with numbers you can check.')}
<div class="eli"><b style="font-size:14px">🧒 Like you're 5</b><br>
You want to tell a friend a secret across a huge, noisy stadium. First you pack the message small and add a few spare words so a missed word can be guessed (<b>encode</b>). You put it on a whistle note that carries (<b>modulate</b>), move that note up to the pitch you were told to use (<b>up-convert</b>), and blow as hard as you can (<b>high-power amplifier</b>) through a megaphone (the <b>antenna</b>).<br>
On the way, your shout does not get eaten. It <b>spreads out</b>. Twice as far away, it covers four times the area, so each ear gets a quarter of it. A helper halfway hears you faintly and shouts it on again (the <b>repeater</b>). Your friend cups a big ear (a dish) and uses a hearing aid that adds almost no hiss of its own (the <b>low-noise amplifier</b>), then undoes every step in reverse. Whether the secret arrives depends on one thing only: how loud your shout is <b>compared with the crowd noise</b> at your friend's ear. That comparison is the whole link equation.</div>
<div class="two">
<div class="card" style="padding:9px 13px"><h3>🏷 The official names (name first, then what it means)</h3>
<ul class="names" style="font-size:10.6px">
<li><b>Communications link</b>: one complete radio path, transmitter to receiver. <b>Uplink</b>, <b>downlink</b>. The <b>space segment</b> is the satellite; the <b>ground segment</b> is the Earth stations.</li>
<li><b>Source coding</b> (compression) and <b>channel coding</b> (forward error correction, FEC): the two jobs the lecture's "encoder" does. One removes waste; the other adds protective spare bits. <b>Codec</b> = coder + decoder.</li>
<li><b>Modem</b>: modulator + demodulator.</li>
<li><b>Up-converter / down-converter</b> (frequency converter, mixer): shifts a modulated signal to a different frequency without changing what it carries. The low starting frequency is the <b>intermediate frequency, IF</b>; the on-air one is the <b>radio frequency, RF</b>.</li>
<li><b>High-power amplifier, HPA</b> (power amplifier): the last stage before the transmit antenna.</li>
<li><b>Free-space path loss, Lₛ</b> (spreading loss; the slide's "free space loss"). <b>Atmospheric loss, Lₐ</b> (atmospheric attenuation).</li>
<li><b>Transponder</b> (the lecture's "satellite repeater"): receives, shifts frequency, amplifies, retransmits. A satellite that only does this is a <b>bent-pipe</b> relay.</li>
<li><b>Low-noise amplifier, LNA</b>: the first stage after the receive antenna.</li>
<li><b>Thermal noise</b>; <b>noise power density, N₀</b> = k × T. <b>Boltzmann constant, k</b>. <b>System noise temperature, T</b>.</li>
<li><b>EIRP</b>, effective isotropic radiated power: P × Gₜ. <b>G/T</b> ("G over T"): receive gain ÷ noise temperature, a station's figure of merit.</li>
<li><b>Signal-to-noise ratio</b>; here <b>S/N₀</b>. <b>Link budget</b>: the gains-and-losses ledger. <b>Decibel, dB</b>. <b>Link margin</b>.</li>
</ul></div>
<div class="card" style="padding:9px 13px"><h3>🛠 How it actually works</h3>
<table class="mech" style="font-size:10.1px"><tr><th style="width:68px">Step</th><th>The mechanism, with numbers</th></tr>
<tr><td><b>1 · Encode</b></td><td>Squeeze out the waste (compression), then add structured spare bits so the far end can repair errors. Good codes let you send about 5 times more data over the same link.</td></tr>
<tr><td><b>2 · Modulate, then move</b></td><td>Write the bits onto a carrier at an easy fixed frequency, say 70 MHz. Then mix it with a 7,100 MHz tone: out comes the same signal at <b>7,170 MHz</b>, in the X-band uplink slot. Two steps, because precise modulators are easy to build low and one design then serves any band.</td></tr>
<tr><td><b>3 · Amplify out</b></td><td>The signal is strong and clean here, so noise is no worry. Only watts matter: 20 W on Cassini, 20,000 W on a Deep Space Network dish.</td></tr>
<tr><td><b>4 · Space loss</b></td><td>Nothing absorbs the wave. It spreads over a sphere of area 4πd². <b>Twice the distance, a quarter of the power.</b> In the standard form Lₛ = (4πd ÷ λ)². To a GEO satellite: 10²⁰. Saturn to Earth: 2.5 × 10²⁹.</td></tr>
<tr><td><b>5 · Repeat</b></td><td>A relay satellite hears perhaps 10⁻¹⁰ W, moves it to the downlink frequency so it cannot jam its own receiver, amplifies it about 10¹¹ times and sends it down.</td></tr>
<tr><td><b>6 · Amplify in</b></td><td>Everything warm hisses with radio noise: N₀ = k × T watts in every hertz, with k = 1.38 × 10⁻²³. Whatever noise the <i>first</i> amplifier adds is amplified by all the stages after it, so that one stage must be the quietest thing in the station. NASA chills its to about 15 K. Then down-convert, demodulate, decode.</td></tr>
<tr><td><b>7 · The ratio</b></td><td>An amplifier cannot tell signal from noise; it lifts both. So the ratio fixed at the first amplifier is all you ever get. Data rate ≈ S/N₀ ÷ (a factor of about 2 to 4 that the code needs).</td></tr></table></div>
</div></div>'''

p3 = f'''<div class="page">{top(T("THE LINK BUDGET"),'Cassini to Earth, <span>line by line</span>','The link equation with real numbers. Multiply the middle column, or add the right-hand column: decibels turn the whole thing into addition.')}
<div class="two">
<div class="card" style="padding:8px 13px"><h3>🧾 The ledger: Saturn to a 70 m dish, 8.4 GHz</h3>
<table class="mech" style="font-size:10.6px"><tr><th>Item</th><th>As a number</th><th>In decibels</th></tr>
<tr><td><b>P</b> · transmitter power</td><td>20 W</td><td>+13 dBW</td></tr>
<tr><td><b>Gₜ</b> · Cassini's 4 m dish</td><td>× 50,000</td><td>+47 dB</td></tr>
<tr><td><i>EIRP = P × Gₜ</i></td><td><i>1,000,000 W</i></td><td><i>+60 dBW</i></td></tr>
<tr><td><b>Lₛ</b> · space loss, 1.4 billion km</td><td>÷ 2.5 × 10²⁹</td><td>−294 dB</td></tr>
<tr><td><b>Lₐ</b> · air, clear sky</td><td>÷ 1.05</td><td>−0.2 dB</td></tr>
<tr><td><b>Gᵣ</b> · 70 m dish on Earth</td><td>× 25,000,000</td><td>+74 dB</td></tr>
<tr><td><b>S</b> · signal received</td><td><b>10⁻¹⁶ W</b></td><td><b>−160 dBW</b></td></tr>
<tr><td><b>N₀</b> = k × T, with T = 20 K</td><td>2.8 × 10⁻²² W per Hz</td><td>−216 dBW/Hz</td></tr>
<tr><td><b>S ÷ N₀</b></td><td><b>about 400,000</b></td><td><b>56 dB-Hz</b></td></tr></table>
<div style="font-size:10.6px;margin-top:5px;line-height:1.45"><b>Reading the answer.</b> The signal is as strong as the noise in a 400,000 Hz slice. Divide by about 4 for the code's needs and a safety margin: roughly <b>100,000 bits per second</b>. Cassini's real top rate was 166,000.<br>
<b>Why rates collapse with distance.</b> Voyager 1 is 17 times farther than Saturn, so its space loss is 17² ≈ 300 times worse. It sends 160 bits per second. New Horizons needed 15 months to return its Pluto data.</div></div>
<div><div class="card" style="padding:8px 13px"><h3>📐 Decibels in one minute</h3>
<div style="font-size:10.8px;line-height:1.5">A decibel counts multiplications. <b>+3 dB = ×2 · +10 dB = ×10 · +20 dB = ×100 · −30 dB = ÷1,000.</b> Multiplying numbers means adding their decibels, which is why the right-hand column simply adds up: 13 + 47 − 294 − 0.2 + 74 = −160.<br>
<b>dBW</b> means "compared with 1 watt". <b>dBm</b> means "compared with 1 milliwatt". You have seen this already: a Wi-Fi router sends about +20 dBm (0.1 W), your laptop reports the signal as about −60 dBm, and its noise floor is near −95 dBm. That is a link budget. Cassini's is the same sum with bigger numbers.</div></div>
<div class="card" style="margin-top:9px;padding:8px 13px"><h3>🎚 The only knobs there are</h3>
<ul class="r" style="font-size:10.7px">
<li><b>More power</b> (P): costs solar panels and heat.</li>
<li><b>Bigger or higher-frequency dish</b> (Gₜ): costs mass and pointing accuracy.</li>
<li><b>Bigger ground dish, or several combined</b> (Gᵣ): 70 m is about the limit.</li>
<li><b>Colder receiver</b> (T): halve the noise temperature, double the data.</li>
<li><b>Better codes</b>: free decibels from mathematics.</li>
<li><b>Distance</b> (Lₛ): the one you cannot touch, and by far the largest term.</li></ul>
<div style="font-size:10.4px;margin-top:3px">A decibel gained anywhere is worth the same as a decibel gained anywhere else.</div></div></div>
</div></div>'''

p3b = f'''<div class="page">{top(T("FACT CHECK"),'What the captions mangled, <span>and what he blurred</span>','The caption errors, then where the instructor was loose or wrong.')}
<div class="two">
<div class="card" style="padding:8px 13px"><h3>🔎 Caption errors</h3>
<table class="t" style="font-size:10px"><tr><th>Captions said</th><th>Instructor meant</th></tr>
<tr><td>"a few competence"</td><td>a few <b>components</b></td></tr>
<tr><td>"upconvert as… not that process to modulation"</td><td><b>up-converters</b>… an <b>added</b> process to modulation</td></tr>
<tr><td>"few geophones… 30 g of hurts"</td><td>few <b>gigahertz</b>… 30 <b>gigahertz</b></td></tr>
<tr><td>"de-code us" · "compress as"</td><td><b>decoders</b> · <b>compressors</b></td></tr>
<tr><td>"analogous signal"</td><td><b>analog</b> signal</td></tr>
<tr><td>"a much fake a twin ration", "a fake translation"</td><td><b>atmospheric attenuation</b></td></tr>
<tr><td>"low noise and profiles", "high power for fires"</td><td>low-noise <b>amplifiers</b>, high-power <b>amplifiers</b></td></tr>
<tr><td>"and blink" · "turns meets" · "gametes"</td><td>an <b>uplink</b> · <b>transmits</b> · <b>emits</b></td></tr>
<tr><td>"inverse Procida" · "Mody elaters"</td><td>inverse <b>process</b> · <b>modulators</b></td></tr>
<tr><td>"mathematically rented"</td><td>mathematically <b>oriented</b></td></tr>
<tr><td>"divided by zero and zero"</td><td>divided by <b>N-zero (N₀)</b></td></tr>
<tr><td>"the balsam and constant"</td><td>the <b>Boltzmann</b> constant</td></tr>
<tr><td>"PTZ t" · "gang transmitted"</td><td><b>P_T G_T</b> · <b>gain</b> transmitted</td></tr>
<tr><td>"less and y divided by L.A."</td><td><b>L_S</b> and 1 divided by <b>L_A</b></td></tr>
<tr><td>"space for the losses gave their names"</td><td><b>free-space</b> losses</td></tr></table></div>
<div class="card" style="padding:8px 13px"><h3>▲ Where the instructor was loose</h3>
<ul class="r" style="font-size:10.6px">
<li><b>"1/k… is just a relation for wavelength and other parameters."</b> Wrong. k is the <b>Boltzmann constant</b>, 1.38 × 10⁻²³ joules per kelvin. It turns the receiver's temperature into noise power: N₀ = k × T. It has nothing to do with wavelength.</li>
<li><b>The low-noise amplifier must "avoid mistaking the signal for noise".</b> No amplifier can tell them apart. It lifts both. The point is that it adds very little noise <i>of its own</i>, because anything the first stage adds is magnified by every stage after it.</li>
<li><b>"High-power amplifiers know the signal, so it's safe and they can amplify more."</b> The real reason is simpler: at the transmitter the signal is enormous compared with any noise, so only output power matters.</li>
<li><b>"Free-space losses."</b> Right that they grow with distance. Not said: nothing is lost to anything. The wave spreads, and the receiver catches a smaller share.</li>
<li><b>"Encoders… convert my voice into an electrical signal."</b> That is a microphone. Encoding means compressing the data and adding error-correcting bits. The second job is what makes deep-space links work at all.</li>
<li><b>"Up-conversion is similar to modulation."</b> Different jobs. Modulation writes the message on a carrier. Up-conversion moves the finished signal to another frequency and changes nothing in it.</li>
<li><b>"Gain is related to the high power and the directivity."</b> Antenna gain is directivity only. Power is its own term.</li>
<li><b>His diagram is a relay link:</b> ground to satellite to ground. That is a communications satellite, the "relay" type from Section 1. A science probe is one end of the link, not the middle.</li>
<li><b>Not said: what the ratio buys.</b> Bits per second. That is the reason anyone computes it.</li></ul></div>
</div></div>'''

vocab = [("Link", "one radio connection from a transmitter to a receiver.", ""),
("Component", "one part of a system.", ""),
("Modulator / demodulator (modem)", "writes the signal onto a carrier / takes it off again.", "Repeat, L1."),
("Up-converter / down-converter", "moves a signal to a higher / lower frequency without changing what it carries.", "Changing lanes, not changing the cargo."),
("Encoder / decoder (codec)", "turns information into a compact, protected code / turns it back.", ""),
("Format / code", "an agreed way of writing information as symbols.", ""),
("Compressor / compression", "squeezing data into fewer bits by removing what is repeated or unneeded.", ""),
("Error-correcting code", "spare bits added in a pattern so the receiver can find and fix mistakes.", ""),
("Analog signal", "a smoothly varying signal, like a voice.", ""),
("Electric pulses / digital signal", "information as a string of 1s and 0s.", ""),
("Bit / bits per second", "one 1-or-0 / how many are sent each second: the data rate.", ""),
("Satellite repeater = transponder", "equipment on a satellite that receives a signal, boosts it and sends it on.", "The helper halfway across the stadium."),
("Attenuation", "weakening.", ""),
("Atmospheric attenuation = atmospheric loss (Lₐ)", "the weakening caused by the air and rain.", "Repeat, L2."),
("Free-space loss (Lₛ)", "the weakening caused by the wave spreading out over distance.", "Twice as far, a quarter as strong."),
("Amplifier / amplify", "a device that makes a signal stronger / to do so.", ""),
("High-power amplifier (HPA)", "the amplifier that feeds the transmitting antenna.", "Blowing hard."),
("Low-noise amplifier (LNA)", "the first amplifier after the receiving antenna, built to add almost no noise.", "A hearing aid with no hiss."),
("Noise", "random electrical hiss that is always present and hides weak signals.", ""),
("Thermal noise", "noise caused by heat: every warm object and circuit makes it.", ""),
("Signal (S)", "the power of the wanted signal at the receiver.", ""),
("N₀ (N-zero)", "noise power in each hertz of bandwidth. N₀ = k × T.", ""),
("Signal-to-noise ratio (S/N₀)", "how strong the signal is compared with the noise. Sets the data rate.", ""),
("Boltzmann constant (k)", "1.38 × 10⁻²³ joules per kelvin. Converts temperature into noise power.", ""),
("Kelvin (K)", "temperature counted from absolute zero. 20 K is −253 °C.", "Repeat."),
("System temperature (T)", "a single number for all the noise in a receiving station, as if it came from an object that warm.", ""),
("Transmitted power (P)", "watts fed to the transmitting antenna.", ""),
("Gain (Gₜ, Gᵣ)", "how much the transmit / receive antenna concentrates the signal.", "Repeat, L1."),
("EIRP", "power × transmit gain: how strong the transmitter looks from far away.", ""),
("G/T", "receive gain ÷ noise temperature: how good a listening station is.", ""),
("Link budget", "the list of every gain and loss between transmitter and receiver, added up.", "A bank statement for the signal."),
("Decibel (dB) / dBW / dBm", "a scale that counts multiplications / relative to 1 watt / to 1 milliwatt.", "Repeat, L1."),
("Margin", "the safety allowance left over after the sum.", ""),
("Transmitting / receiving Earth station", "the ground end that sends / listens.", ""),
("Space segment / ground segment", "the satellite part / the Earth part of a system.", ""),
("Uplink / downlink", "ground to satellite / satellite to ground.", "Repeat, L2."),
("Input / output information", "what goes into the chain / what comes out the far end.", ""),
("Distorted", "changed in shape on the way.", ""),
("Relay / bent pipe", "a satellite that only passes signals on.", "Repeat, Section 1."),
("Voyager 1 / New Horizons / Deep Space Network", "the farthest probe / the Pluto probe / NASA's 70 m dishes.", "Who's Who.")]
p4 = f'''<div class="page">{top(T("VOCABULARY"),'Every word used, <span>in plain English</span>',f'{len(vocab)} entries. "Repeat" = you have met it before.')}
<div class="gl2" style="font-size:10.2px;line-height:1.34">{"".join(f"<div><b>{esc(a)}</b> — {esc(b)}{(' <i>'+esc(c)+'</i>') if c else ''}</div>" for a,b,c in vocab)}</div></div>'''

c1 = ("FREE-SPACE LOSS (Lₛ)", "spreading loss", "weakening from the wave spreading out", "nothing eats the signal. It covers a bigger sphere, so each dish catches a smaller share", "2× distance = ¼ power · GEO 10²⁰ · Saturn 2.5×10²⁹ (294 dB)", "absorption (that is Lₐ, the air)", "Lₛ = (4πd ÷ λ)² · inverse square · link budget")
c2 = ("SIGNAL-TO-NOISE RATIO", "S ÷ N₀", "signal power compared with noise", "a receiver can amplify forever, but it lifts noise too. Only the ratio decides what can be read", "Cassini: 10⁻¹⁶ W ÷ 2.8×10⁻²² W/Hz ≈ 400,000 (56 dB-Hz)", "signal strength alone", "N₀ = k × T · bits per second · coding")
c3 = ("LINK BUDGET", "—", "ledger of every gain and loss on a link", "it shows before launch whether the far end will hear you, and how fast you can talk", "13 + 47 − 294 + 74 = −160 dBW (Cassini)", "data budget (how much to send)", "decibels add · EIRP · G/T · margin")
c4 = ("LOW-NOISE AMPLIFIER", "LNA", "first amplifier after the receive antenna", "noise added by the first stage is magnified by all the rest, so it must be the quietest", "DSN: cooled to ~15 K · system noise ~20 K", "HPA (transmit side: watts matter)", "thermal noise · k × T · S ÷ N₀")
c5 = ("TRANSPONDER", "satellite repeater", "receives, shifts frequency, amplifies, resends", "after 36,000 km the signal is too weak to bounce. Boost it, and move it off the uplink frequency", "hears ~10⁻¹⁰ W · gain ~10¹¹ (110 dB)", "a science probe (an END of the link)", "relay satellite · uplink / downlink · bent pipe")
c6 = ("ERROR-CORRECTING CODE", "FEC", "spare bits that let the receiver fix errors", "weak signals arrive with mistakes. Patterned spare bits repair them, no resend needed", "good codes ≈ 5× more data on the same link", "compression (removes bits)", "encoder / decoder · S ÷ N₀ · data rate")
cA, a1, a2 = cardpage(c1, c2, "C29", "scene 13"); cB, b1, b2 = cardpage(c3, c4, "C30", "scene 13"); cC, d1, d2 = cardpage(c5, c6, "C31", "scene 13")
p5 = f'''<div class="page">{top(T("COPY INTO NOTES"),'Where each piece goes <span>in the notebook</span>','Routes A to D. Section 5 ends here, so route B is the full set of lines for the Section 5 map page.')}
<div class="two route">
<div class="card" style="padding:9px 13px"><h3>A · Equations &amp; key numbers page (p3–4)</h3>
<div class="copy">S/N₀ = P·Gₜ·(Gᵣ/T) ÷ (k·Lₛ·Lₐ)   the link equation
Lₛ = (4πd ÷ λ)²    space loss · 2× distance = ¼ power
N₀ = k × T         k = 1.38×10⁻²³ J/K · 20 K → 2.8×10⁻²² W/Hz
dB                 +3 = ×2 · +10 = ×10 · add, don't multiply
Cassini            13 + 47 − 294 + 74 = −160 dBW = 10⁻¹⁶ W
                   S/N₀ ≈ 56 dB-Hz → ~100,000 bits/s
Voyager 1          160 bits per second</div>
<h3>B · Section 5 map page (write it now, from memory first)</h3>
<div class="copy">S5 · antennas: radio = EM wave, c = λ × f; rod = λ ÷ 2;
     modulation = signal on a fast carrier; dish gain = aim
S5 · atmosphere: wall with 2 windows (visible, radio);
     links use S / X / Ka; uplink ≠ downlink
S5 · links: encode → modulate → up-convert → HPA ⇒ space
     loss (spreading) ⇒ LNA → down-convert → demod → decode
S5 · the point: signal ÷ noise sets bits per second</div>
<h3>D · Question bank ("but how?" cards)</h3>
<div class="copy">Q: Where does the signal's power go on the way?
A: Nowhere. It spreads over a sphere 4πd². 2× far = ¼ power.
Q: Why must the FIRST receive amplifier be low-noise?
A: Its added noise is amplified by every later stage.
Q: Why can't you just amplify a weak signal more?
A: Amplifiers lift signal and noise together. The ratio stays.
Q: What is k in the link equation?
A: Boltzmann constant: noise per hertz = k × temperature.</div></div>
<div class="card" style="padding:9px 13px"><h3>C · One-line word bank (new lines)</h3>
<div class="copy">p__ · link · one radio path, transmitter to receiver
p__ · encoder / decoder = codec · code the data / decode it
p__ · compression · fewer bits, same message
p__ · error-correcting code = FEC · spare bits fix errors → C31
p__ · up- / down-converter · shift frequency up / down
p__ · IF / RF · easy low frequency / the on-air one
p__ · HPA · high-power amp, before transmit antenna
p__ · LNA · low-noise amp, first after receive antenna → C30
p__ · free-space loss (Lₛ) · spreading; ∝ distance² → C29
p__ · atmospheric loss (Lₐ) · air + rain weakening
p__ · transponder = repeater · receive, shift, boost, resend → C31
p__ · bent pipe · satellite that only relays
p__ · thermal noise · hiss from anything warm
p__ · N₀ · noise per hertz = k × T
p__ · Boltzmann constant (k) · 1.38×10⁻²³ J/K
p__ · system noise temperature (T) · all noise as one temp
p__ · S/N₀ = signal-to-noise · sets data rate → C29
p__ · EIRP · power × transmit gain
p__ · G/T · receive gain ÷ noise temp
p__ · link budget · ledger of gains and losses → C30
p__ · dBW / dBm · dB vs 1 watt / vs 1 milliwatt
p__ · bit rate · bits per second</div></div>
</div></div>'''
p6 = f'''<div class="page">{top(T("CONCEPT CARDS"),'Route E: <span>pages C29 and C30</span>','Two notebook pages, two cards each. Copy line for line; the faint numbers are your ruled lines.')}
<div style="display:flex;gap:16px;justify-content:center">{cA}{cB}</div>
<div style="text-align:center;font-size:10.5px;color:#444;margin-top:6px">C29: {a1} + {a2} lines of 22 · C30: {b1} + {b2} lines of 22</div></div>'''
p7 = f'''<div class="page">{top(T("CONCEPT CARDS"),'Route E: <span>page C31</span>','The third card page for this lecture.')}
<div style="display:flex;gap:22px;justify-content:center;align-items:flex-start">{cC}
<div class="card" style="width:4.3in;padding:12px 16px;font-size:12px;line-height:1.5"><h3>Section 5 is complete</h3>
Three lectures, four spreads, eight card pages (C24–C31).<br><br>
<b>Before Section 6</b><br>
1. Write the Section 5 map page from memory, then check it against route B on the previous page.<br>
2. Do one timed Section 5 talk from the app's Teach tab. It is four minutes.<br><br>
<b>The thread through all three lectures</b><br>
Lecture 1: how a wave carries a message and how a dish aims it. Lecture 2: which waves can get through the air. Lecture 3: adding it all up to see whether the far end can hear you. Every number in today's ledger came from one of the first two lectures.<br><br>
<b>For Network+ later</b><br>
The decibel ledger on page 3 is the same arithmetic as a Wi-Fi link: transmit power in dBm, antenna gain in dBi, path loss, receiver sensitivity. You have now done it once with Saturn.<br><br>
C31: {d1} + {d2} lines of 22.</div></div></div>'''
p8 = f'''<div class="page">{top(T("SAY IT OUT LOUD"),'Last page: <span>prove it by talking</span>','After the spread and the 3-line summary, with everything closed. Send me what you said and I will grade it like a friend would.')}
<div class="two"><div>
<div class="card"><h3>🗣 The friend's opening question</h3><div style="font-size:13px;line-height:1.5">"Why does it take so long to get pictures back from far-away probes? Radio moves at the speed of light."</div></div>
<div class="card" style="margin-top:12px"><h3>✅ Three sentences you should be able to say</h3><ul class="r" style="font-size:12px">
<li>The radio is fast, but the signal arrives unbelievably faint. Nothing absorbs it; it just spreads out, so twice as far away you catch a quarter as much.</li>
<li>At the receiver it has to be picked out of the electrical hiss that everything warm makes. What matters is the signal compared with that noise, and that ratio sets how many bits per second you can send.</li>
<li>So engineers add up a budget: transmitter power, both dishes, the distance, the receiver's noise. From Saturn that gives about a hundred thousand bits a second. From Voyager it is 160.</li></ul></div>
<div class="card" style="margin-top:12px"><h3>❓ Follow-ups a friend might ask</h3><ul class="r" style="font-size:12px">
<li>"Can't they just amplify it more?" (an amplifier boosts the noise by the same amount; the ratio doesn't change)</li>
<li>"So how do you improve it?" (more power, bigger dishes, a colder receiver, cleverer codes)</li>
<li>"What's a low-noise amplifier?" (the first amplifier at the receiver, chilled so it adds almost no hiss of its own)</li>
<li>"What does a relay satellite do?" (hears the faint uplink, moves it to another frequency, boosts it and sends it back down)</li>
<li>"What are decibels for?" (they turn all those multiplications into one column you can add)</li></ul></div></div>
<div><div class="card" style="min-height:3.2in"><h3>📝 Your explanation (paste or dictate)</h3><div style="border:2px dashed #999;border-radius:8px;height:2.5in;padding:8px;color:#999;font-size:11px">_ send it to me in chat; I'll put it here _</div></div>
<div class="card" style="margin-top:12px;min-height:2.2in;border-color:var(--green)"><h3 style="color:var(--green)">🎯 My read</h3><div style="border:2px dashed #999;border-radius:8px;height:1.5in;padding:8px;color:#999;font-size:11px">solid on: _<br>fuzzy on: _<br>fix: _<br>→ question-bank cards: _</div></div>
<div class="callout" style="margin-top:12px;font-size:11.5px">⚡ Section 5 done. Next is Section 6: attitude determination and control.</div></div></div></div>'''
write('s5-l3.html', [p1, p2, p3, p3b, p4, p5, p6, p7, p8])
print('ok', a1, a2, b1, b2, d1, d2, len(vocab))
