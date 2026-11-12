from lib import *
B = "SEC 5 · LEC 2 · ATMOSPHERE + FREQUENCY BANDS"
T = lambda x: B.replace("ATMOSPHERE + FREQUENCY BANDS", x)
bands = [("L", "1"), ("S", "2"), ("C", "4"), ("X", "8"), ("Ku", "12"), ("K", "18"), ("Ka", "27")]
uses = [("GPS", ""), ("Wi-Fi 2.4", "spacecraft"), ("Wi-Fi 5", ""), ("deep", "space"), ("sat TV", "Starlink"), ("", ""), ("deep", "space")]
bx = ""
for i, (b, lo) in enumerate(bands):
    x = 10 + i * 44
    bx += '<rect x="%d" y="318" width="44" height="24" fill="#fff" stroke="#111" stroke-width="1.5"/>' % x
    bx += '<text x="%d" y="334" text-anchor="middle" font-size="10" font-weight="bold" fill="#111">%s</text>' % (x + 22, b)
    bx += '<text x="%d" y="352" text-anchor="middle" font-size="7.5" fill="#111">%s</text>' % (x, lo)
    u1, u2 = uses[i]
    if u1: bx += '<text x="%d" y="365" text-anchor="middle" font-size="7.5" fill="#111">%s</text>' % (x + 22, u1)
    if u2: bx += '<text x="%d" y="375" text-anchor="middle" font-size="7.5" fill="#111">%s</text>' % (x + 22, u2)
bx += '<text x="318" y="352" text-anchor="middle" font-size="7.5" fill="#111">40</text>'
svg = f'''<svg width="100%" height="428" viewBox="0 0 330 412" style="display:block" font-family="Verdana, sans-serif">
<defs><marker id="ar" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#111"/></marker>
<pattern id="hat" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" stroke="#111" stroke-width="1"/></pattern></defs>
<text x="8" y="13" font-size="10" font-weight="bold" fill="#111">1 · THE AIR IS A WALL WITH TWO WINDOWS</text>
<g font-size="8" font-weight="bold" fill="#111" text-anchor="middle"><text x="52" y="40">GAMMA · X-RAY · UV</text><text x="154" y="40">INFRARED</text><text x="297" y="40">LONG RADIO</text></g>
<rect x="10" y="46" width="85" height="48" fill="url(#hat)" stroke="#111" stroke-width="1.6"/>
<rect x="118" y="46" width="72" height="48" fill="url(#hat)" stroke="#111" stroke-width="1.6"/>
<rect x="275" y="46" width="45" height="48" fill="url(#hat)" stroke="#111" stroke-width="1.6"/>
<line x1="95" y1="46" x2="118" y2="46" stroke="#111" stroke-width="0.8" stroke-dasharray="2 2"/><line x1="95" y1="94" x2="118" y2="94" stroke="#111" stroke-width="0.8" stroke-dasharray="2 2"/>
<line x1="190" y1="46" x2="275" y2="46" stroke="#111" stroke-width="0.8" stroke-dasharray="2 2"/><line x1="190" y1="94" x2="275" y2="94" stroke="#111" stroke-width="0.8" stroke-dasharray="2 2"/>
<line x1="106" y1="30" x2="106" y2="106" stroke="#111" stroke-width="1.6" marker-end="url(#ar)"/>
<line x1="218" y1="30" x2="218" y2="106" stroke="#111" stroke-width="1.6" marker-end="url(#ar)"/><line x1="246" y1="30" x2="246" y2="106" stroke="#111" stroke-width="1.6" marker-end="url(#ar)"/>
<g font-size="7.5" fill="#111" text-anchor="middle"><text x="52" y="106">absorbed up high</text><text x="154" y="106">absorbed</text><text x="297" y="106">bounced back</text></g>
<g font-size="8.5" fill="#111" text-anchor="middle"><text x="106" y="121" font-weight="bold">VISIBLE</text><text x="106" y="132">eyes</text>
<text x="232" y="121" font-weight="bold">RADIO WINDOW</text><text x="232" y="132">1 cm – 10 m · all space links</text></g>
<text x="8" y="149" font-size="8" fill="#111">← short wavelength · high frequency · high energy</text>
<text x="322" y="160" text-anchor="end" font-size="8" fill="#111">long wavelength · low frequency · low energy →</text>
<line x1="8" y1="168" x2="322" y2="168" stroke="#bbb" stroke-width="1"/>
<text x="8" y="183" font-size="10" font-weight="bold" fill="#111">2 · WHY: energy per packet = h × f</text>
<g font-size="8.5" fill="#111">
<text x="8" y="199"><tspan font-weight="bold">gamma, X, UV</tspan>  hit hard: rip electrons off air atoms → absorbed</text>
<text x="8" y="213"><tspan font-weight="bold">visible</tspan>  too weak to break air, too strong to shake it → passes</text>
<text x="8" y="227"><tspan font-weight="bold">infrared</tspan>  just right to shake water + CO₂ molecules → absorbed</text>
<text x="8" y="241"><tspan font-weight="bold">radio</tspan>  far too gentle to do anything → passes</text>
<text x="8" y="255"><tspan font-weight="bold">long radio</tspan>  the ionosphere's electrons bounce it back</text>
</g>
<text x="165" y="273" text-anchor="middle" font-size="9" font-weight="bold" fill="#111">higher frequency = more energy in each packet (photon)</text>
<line x1="8" y1="282" x2="322" y2="282" stroke="#bbb" stroke-width="1"/>
<text x="8" y="297" font-size="10" font-weight="bold" fill="#111">3 · BAND LETTERS (edges in GHz)</text>
<text x="322" y="310" text-anchor="end" font-size="7.5" fill="#111">frequency rises →</text>
{bx}
<text x="165" y="392" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#111">UPLINK = Earth → space · DOWNLINK = space → Earth</text>
<text x="165" y="405" text-anchor="middle" font-size="8.5" fill="#111">different frequencies, so they don't drown each other</text>
</svg>'''
p1 = spread(B, 'A wall with <span>two windows</span>', 'S5 / L2 — Atmosphere + bands', svg,
 "hatched block = the air blocks it · gap + arrow = it gets through · boxes = band letters, numbers = GHz at each edge",
 ["1. The air is a wall with two windows: visible light and radio.",
  "2. Higher frequency = more energy per photon. Radio is too gentle to absorb.",
  "3. Spacecraft talk in the radio window: S, X, Ka. Uplink and downlink differ."],
 ['What is atmospheric opacity?', 'Which waves does the air block?', 'Which two get through?', 'Why are gamma, X and UV stopped?',
  'Why can our eyes use visible light?', 'What stops infrared? Long radio?', 'Where do spacecraft links sit?', 'The frequency-band names, low to high?',
  'Satellite letter bands in order?', 'Uplink vs downlink?', '<span class="hl b">? why are space telescopes in space</span>'],
 ['<span class="hl y">atmospheric opacity</span> = how much the air blocks at each wavelength (0% clear, 100% blocked)',
  'short wavelength = high frequency = <span class="hl y">high energy</span>',
  '<span class="hl y">gamma, X-ray, UV</span>: <span class="hl o">blocked</span> by the upper atmosphere · protects us',
  '<span class="hl y">visible light</span>: gets through (a gap) · why eyes use it',
  '<span class="hl y">infrared</span>: mostly absorbed by gases (water, CO₂) → observe from space',
  '<span class="hl y">radio waves</span> <span class="hl k">~1 cm – 10 m</span>: <span class="hl g">get through</span> → telecommunications',
  'long-wavelength radio: blocked (bounced by the ionosphere)',
  'bands: VLF · LF · MF · HF · VHF · UHF · <span class="hl y">SHF</span> · EHF (each 10× the last)',
  'satellites: SHF <span class="hl k">3–30 GHz</span> · letter bands <span class="hl y">L S C X Ku K Ka</span> (1–40 GHz)',
  'deep space: S ~2.1 / 2.3 · <span class="hl y">X</span> 7.2 / 8.4 · Ka 34 / 32 GHz (up / down)',
  '<span class="hl y">uplink</span> = Earth → space · <span class="hl y">downlink</span> = space → Earth'])

p2 = f'''<div class="page">{top(T("TEACH"),'Hard hitters get stopped. <span>Radio slips through.</span>','Simple story first, then the official names, then how it actually works with numbers you can check.')}
<div class="eli"><b style="font-size:14px">🧒 Like you're 5</b><br>
The air around the Earth is a wall with two windows in it. One window lets in ordinary light, the kind your eyes use. The other lets in radio. Everything else gets stopped. The dangerous rays (ultraviolet, X-rays, gamma rays) are soaked up high in the sky, which is what keeps us alive. Heat rays (infrared) are soaked up by the water and carbon dioxide in the air. And very long radio waves bounce off an electric layer near the top, like a ball off a ceiling.<br>
Why? Light of every kind arrives in tiny packets, and the faster it wiggles, the harder each packet hits. Hard-hitting packets smash into air atoms and are used up. Gentle radio packets slip between them untouched. So if you want to talk to a spacecraft from the ground you <b>must</b> use the radio window. And if you want to see X-rays or infrared from the stars, you have to lift the telescope above the wall. That is why Hubble and Webb are in space.</div>
<div class="two">
<div class="card" style="padding:9px 13px"><h3>🏷 The official names (name first, then what it means)</h3>
<ul class="names" style="font-size:10.8px">
<li><b>Atmospheric opacity</b> (its opposite is <b>transmittance</b>): the share of radiation the air stops, as a function of wavelength.</li>
<li><b>Atmospheric window</b>: a wavelength range the air lets through. The <b>optical window</b> (visible light) and the <b>radio window</b> (about 1 cm to 10 m, or 30 GHz down to 30 MHz).</li>
<li><b>Photon</b>: one packet of electromagnetic energy. <b>Photon energy</b> E = h × f, where h is the <b>Planck constant</b>.</li>
<li><b>Absorption</b>: a photon giving its energy to an atom or molecule and vanishing. <b>Ionization</b> when it knocks an electron off; <b>molecular vibration</b> when it sets a molecule shaking.</li>
<li><b>Ionospheric reflection</b>: long radio waves being turned back by the ionosphere's free electrons. The cut-off is the <b>critical frequency</b>, around 10 MHz.</li>
<li><b>Radio-frequency bands</b> (ITU bands): <b>VLF, LF, MF, HF, VHF, UHF, SHF, EHF</b>. Each covers ten times the frequency of the one before. <b>Microwaves</b> are roughly 1–100 GHz.</li>
<li><b>Letter bands</b> (IEEE radar bands): <b>L, S, C, X, Ku, K, Ka</b>. Wartime radar code letters, deliberately meaningless. Ku and Ka mean "K-under" and "K-above".</li>
<li><b>Uplink</b>: Earth to spacecraft. <b>Downlink</b>: spacecraft to Earth.</li>
<li><b>Deep space</b>, in radio rules: farther than 2 million km from Earth. Its bands are protected because the signals are so faint.</li>
<li><b>ITU</b>, the International Telecommunication Union: the UN body that decides who may use which frequency. <b>Frequency allocation</b>.</li>
<li><b>Rain fade</b>: rain and water vapour weakening signals above about 10 GHz.</li>
</ul></div>
<div class="card" style="padding:9px 13px"><h3>🛠 How it actually works</h3>
<table class="mech" style="font-size:10.2px"><tr><th style="width:70px">Step</th><th>The mechanism, with numbers</th></tr>
<tr><td><b>1 · Photon energy</b></td><td>E = h × f. Handy form: energy in eV = 1,240 ÷ wavelength in nanometres. UV at 250 nm: <b>5 eV</b>. Green light, 550 nm: 2.3 eV. Infrared, 10,000 nm: 0.12 eV. X-band radio, 3.6 cm: <b>0.000035 eV</b>.</td></tr>
<tr><td><b>2 · Gamma, X, UV</b></td><td>Splitting an oxygen molecule takes about 5 eV; tearing an electron off nitrogen takes 15. These photons have that, so they are used up 50–100 km overhead. That is what makes the ozone layer and the ionosphere (Section 2).</td></tr>
<tr><td><b>3 · Visible</b></td><td>1.8 to 3.1 eV: not enough to break air molecules, far too much to match their vibrations. Nothing in clean air can take it, so it passes.</td></tr>
<tr><td><b>4 · Infrared</b></td><td>About 0.1 eV is exactly what sets water and CO₂ molecules bending and stretching. Absorbed. This is the greenhouse effect, and why infrared telescopes fly.</td></tr>
<tr><td><b>5 · Radio window</b></td><td>Millionths of an eV: too little to excite anything. Transparent from about 30 MHz to 30 GHz. Every spacecraft link lives here. Edges: water vapour absorbs near 22 GHz, oxygen near 60 GHz, and rain hurts above 10 GHz.</td></tr>
<tr><td><b>6 · Long radio</b></td><td>Below a critical frequency ≈ 9 × √(electrons per m³) hertz, the ionosphere's electrons move fast enough to send the wave back. With 10¹² electrons per m³ that is <b>9 MHz</b>. So shortwave radio skips round the world, and can't reach a spacecraft.</td></tr>
<tr><td><b>7 · Up ≠ down</b></td><td>Deep-space X-band: uplink 7.2 GHz, downlink 8.4 GHz. If both were the same, the craft's 20 W transmitter would deafen its own receiver, which is listening for a signal a billion billion times weaker.</td></tr>
<tr><td><b>8 · Why go higher</b></td><td>Same dish, Ka (32 GHz) instead of X (8.4): the wavelength is 3.8 times shorter, so the gain is 3.8² ≈ <b>14 times</b> higher. Price: rain fade and a beam 3.8 times narrower to point.</td></tr></table></div>
</div></div>'''

p3 = f'''<div class="page">{top(T("BANDS + FACT CHECK"),'The names on <span>the dial</span>','Both naming systems from the slides with what lives in each band, then the caption errors and where the instructor was loose.')}
<div class="two" style="margin-bottom:9px">
<div class="card" style="padding:8px 13px"><h3>📻 The decade bands (each ×10)</h3>
<table class="mech" style="font-size:10.2px"><tr><th>Band</th><th>Frequency</th><th>Wavelength</th><th>What lives there</th></tr>
<tr><td><b>VLF</b> very low</td><td>3–30 kHz</td><td>100–10 km</td><td>submarine and maritime signals</td></tr>
<tr><td><b>LF</b> low</td><td>30–300 kHz</td><td>10–1 km</td><td>old navigation beacons (Loran-C)</td></tr>
<tr><td><b>MF</b> medium</td><td>0.3–3 MHz</td><td>1 km–100 m</td><td>AM radio</td></tr>
<tr><td><b>HF</b> high</td><td>3–30 MHz</td><td>100–10 m</td><td>shortwave: bounces off the ionosphere</td></tr>
<tr><td><b>VHF</b> very high</td><td>30–300 MHz</td><td>10–1 m</td><td>FM radio, TV, aircraft; small satellites</td></tr>
<tr><td><b>UHF</b> ultra high</td><td>0.3–3 GHz</td><td>1 m–10 cm</td><td>phones, GPS, Wi-Fi 2.4, CubeSats</td></tr>
<tr><td><b>SHF</b> super high</td><td>3–30 GHz</td><td>10–1 cm</td><td>satellites, deep space, Wi-Fi 5, radar</td></tr>
<tr><td><b>EHF</b> extremely high</td><td>30–300 GHz</td><td>1 cm–1 mm</td><td>radio astronomy, newest links, 5G mmWave</td></tr></table></div>
<div class="card" style="padding:8px 13px"><h3>🛰 The letter bands, and deep space's slices</h3>
<table class="mech" style="font-size:10.2px"><tr><th>Letter</th><th>GHz</th><th>You know it as</th><th>Deep-space uplink / downlink</th></tr>
<tr><td><b>L</b></td><td>1–2</td><td>GPS (1.575)</td><td>—</td></tr>
<tr><td><b>S</b></td><td>2–4</td><td>Wi-Fi 2.4, Bluetooth, microwave ovens</td><td>2.110–2.120 / 2.290–2.300</td></tr>
<tr><td><b>C</b></td><td>4–8</td><td>Wi-Fi 5 and 6 GHz, weather radar</td><td>—</td></tr>
<tr><td><b>X</b></td><td>8–12</td><td>the deep-space workhorse</td><td>7.145–7.190 / 8.400–8.450</td></tr>
<tr><td><b>Ku</b></td><td>12–18</td><td>satellite TV, Starlink to your dish</td><td>—</td></tr>
<tr><td><b>K</b></td><td>18–27</td><td>water vapour absorbs here (22 GHz)</td><td>—</td></tr>
<tr><td><b>Ka</b></td><td>27–40</td><td>Starlink gateways, newest probes</td><td>34.200–34.700 / 31.800–32.300</td></tr></table>
<div style="font-size:10.2px;margin-top:3px">The X-band uplink sits just under 8 GHz, in C-band by the letters. Nobody minds: the pair is still called X-band. Edges differ a little between sources; the slide draws K/Ka at 26.</div></div></div>
<div class="two">
<div class="card" style="padding:8px 13px"><h3>🔎 Caption errors</h3>
<table class="t" style="font-size:10px"><tr><th>Captions said</th><th>Instructor meant</th></tr>
<tr><td>"Katis graphic"</td><td><b>this</b> graphic</td></tr>
<tr><td>"an much Paik opacity", "atmospheric capacity"</td><td><b>atmospheric opacity</b></td></tr>
<tr><td>"a lead to a wavelength"</td><td>a <b>little</b> (short) wavelength</td></tr>
<tr><td>"very fine and energy"</td><td>very <b>high in</b> energy</td></tr>
<tr><td>"ultraviolet night"</td><td>ultraviolet <b>light</b></td></tr>
<tr><td>"merits in navigation"</td><td><b>maritime</b> navigation</td></tr>
<tr><td>"satellite micro telecommunications"</td><td>satellite <b>microwave</b> telecommunications</td></tr>
<tr><td>"3G Gerhard's… 30 Jihad's… ten to nine cuts"</td><td>3 <b>gigahertz</b>… 30 <b>gigahertz</b>… 10⁹ <b>hertz</b></td></tr>
<tr><td>"L as see x. Ok Kasan"</td><td><b>L, S, C, X, Ku, K, Ka</b></td></tr>
<tr><td>"nomenklatura"</td><td><b>nomenclature</b> (naming system)</td></tr></table></div>
<div class="card" style="padding:8px 13px"><h3>▲ Where the instructor was loose</h3>
<ul class="r" style="font-size:10.6px">
<li><b>"High-energy radiation interacts with any particle, basically always."</b> Not quite. A photon is absorbed when its energy matches something a molecule can do with it. Gamma, X and UV have enough to rip atoms apart. Infrared matches molecular vibrations. Visible and radio match nothing, so they pass. It is about matching, not just "more energy".</li>
<li><b>"Long-wavelength radio waves blocked."</b> By a different mechanism from the rest: the ionosphere <i>reflects</i> them. That is why shortwave radio reaches round the planet.</li>
<li><b>Not said: why uplink and downlink differ.</b> So the spacecraft can transmit and listen at once without deafening itself.</li>
<li><b>Not said: why anyone wants the higher bands.</b> The same dish gives more gain and there is more room for data. The cost is weather and tighter pointing.</li>
<li><b>Not said: who hands out frequencies.</b> The ITU, by international treaty.</li>
<li><b>The slide's table</b> lumps Ku, K and Ka together as "K, 12–40 GHz", and gives X-band's short end as 2.4 cm where 2.5 cm is correct.</li>
<li><b>He was right</b> that it is no accident we see in visible light: it is the window where the Sun is brightest and the air is clear.</li></ul></div>
</div></div>'''

vocab = [("Atmospheric absorption", "the air taking in radiation and stopping it.", ""),
("Atmospheric opacity", "how much of the incoming radiation the air blocks. 100% = nothing gets through.", "The wall."),
("Atmospheric window", "a range of wavelengths the air lets through.", "The window in the wall."),
("Wavelength / frequency", "crest-to-crest distance / waves per second. Short wavelength = high frequency.", "Repeat, L1."),
("Energy (of radiation) / photon", "light arrives in packets; each packet is a photon and carries energy = h × f.", ""),
("Planck constant (h)", "the tiny fixed number that turns frequency into energy.", ""),
("Electron-volt (eV)", "a unit of energy the size of one chemical bond.", "Repeat, Section 2."),
("Radiation", "energy travelling as waves or particles. Here: electromagnetic waves.", "Repeat."),
("Gamma rays / X-rays", "the highest-energy electromagnetic waves. Stopped high in the atmosphere.", ""),
("Ultraviolet (UV)", "just beyond violet light. Mostly stopped by oxygen and ozone.", "Repeat, Section 2."),
("Visible light", "the narrow band our eyes detect: 400–700 nanometres.", ""),
("Infrared (IR)", "just beyond red light; what warm things glow in. Mostly absorbed by water vapour and CO₂.", ""),
("Radio waves / microwaves", "the longest electromagnetic waves / the short end of radio, about 1 mm to 30 cm.", ""),
("Spectrum", "the whole range laid out in order.", "Repeat, L1."),
("Atom / molecule / electron configuration", "what air is made of, and how the electrons are arranged in it. That arrangement decides which energies can be absorbed.", ""),
("React / interact / collide", "here: a photon meeting an air particle and handing over its energy.", ""),
("Ionization", "knocking an electron off an atom.", "Repeat, ion engines."),
("Atmospheric gases", "here: mainly water vapour, carbon dioxide and ozone.", "Repeat."),
("Distortion", "the twinkling and blurring that moving air adds to starlight.", ""),
("Observable", "able to be seen or measured.", ""),
("Ionosphere", "the electrically charged upper atmosphere. Reflects long radio waves.", "Repeat, Section 2."),
("Reflect / critical frequency", "bounce back / the frequency below which the ionosphere reflects.", ""),
("VLF, LF, MF, HF, VHF, UHF, SHF, EHF", "very low, low, medium, high, very high, ultra high, super high, extremely high frequency.", ""),
("Kilohertz, megahertz, gigahertz", "thousand, million, billion waves per second.", "Repeat, L1."),
("Shortwave radio", "HF radio, 3–30 MHz, which skips off the ionosphere.", ""),
("Maritime / navigation aid", "to do with ships / a radio beacon for finding position.", ""),
("Radio astronomy", "studying the sky by its radio waves.", ""),
("Band", "a named slice of the spectrum.", ""),
("L, S, C, X, Ku, K, Ka bands", "the letter names for slices between 1 and 40 GHz.", ""),
("Nomenclature", "a naming system.", ""),
("Uplink / downlink", "Earth to spacecraft / spacecraft to Earth.", ""),
("Deep space / near-Earth", "in radio rules: farther / closer than 2 million km.", ""),
("Telecommunications link", "one radio connection between two ends.", "Next lecture."),
("ITU", "International Telecommunication Union: the body that allocates frequencies worldwide.", "Who's Who."),
("Frequency allocation", "the agreed assignment of a band to a use.", ""),
("Rain fade", "signal loss in rain, worse at higher frequencies.", ""),
("Greenhouse effect", "infrared from the ground being absorbed by water vapour and CO₂.", "Same physics as the infrared wall."),
("Hubble / Webb (JWST)", "space telescopes: Hubble for visible and UV, Webb for infrared.", "Repeat, Who's Who."),
("Loran-C", "a retired long-range radio navigation system that used low frequencies.", "Who's Who.")]
p4 = f'''<div class="page">{top(T("VOCABULARY"),'Every word used, <span>in plain English</span>',f'{len(vocab)} entries. "Repeat" = you have met it before.')}
<div class="gl2" style="font-size:10.3px;line-height:1.35">{"".join(f"<div><b>{esc(a)}</b> — {esc(b)}{(' <i>'+esc(c)+'</i>') if c else ''}</div>" for a,b,c in vocab)}</div></div>'''

c1 = ("ATMOSPHERIC WINDOW", "optical + radio window", "wavelengths the air lets through", "the air blocks most of the spectrum. Ground links and ground telescopes must use the gaps", "visible 400–700 nm · radio ~1 cm – 10 m (30 GHz – 30 MHz)", "the ozone hole (a different thing)", "opacity · radio bands · space telescopes")
c2 = ("PHOTON ENERGY", "E = h × f", "energy of one packet of light", "it decides what a wave can do to matter: break it, shake it, or pass through", "UV 5 eV · visible 2 eV · infrared 0.1 eV · X-band 0.000035 eV", "total power (many weak photons)", "eV = 1,240 ÷ nm · ionization · UV damage")
c3 = ("FREQUENCY BANDS", "L S C X Ku K Ka", "named slices of the radio spectrum", "everyone shares one spectrum. Named, allocated slices keep users from jamming each other", "S 2–4 · X 8–12 · Ka 27–40 GHz · deep space X: 8.4 down", "channels (finer slices inside a band)", "ITU · SHF 3–30 GHz · Wi-Fi is S + C")
c4 = ("UPLINK / DOWNLINK", "—", "Earth → spacecraft / spacecraft → Earth", "the craft sends and listens at once. Separate frequencies stop its transmitter deafening its receiver", "X-band deep space: up 7.2 GHz, down 8.4 GHz", "upload / download speed", "transponder · bands · link budget")
cA, a1, a2 = cardpage(c1, c2, "C27", "scene 12"); cB, b1, b2 = cardpage(c3, c4, "C28", "scene 12")
p5 = f'''<div class="page">{top(T("COPY INTO NOTES"),'Where each piece goes <span>in the notebook</span>','Routes A to D for this lecture. The concept cards (route E) are on the next page.')}
<div class="two route">
<div class="card" style="padding:9px 13px"><h3>A · Equations &amp; key numbers page (p3–4)</h3>
<div class="copy">E = h × f          photon energy · eV = 1,240 ÷ λ in nm
                   UV 250 nm → 5 eV · radio 3.6 cm → 0.000035 eV
radio window       ~30 MHz – 30 GHz (10 m – 1 cm)
ionosphere cut-off f ≈ 9·√(electrons per m³) → ~9 MHz
bands (GHz)        L 1–2 · S 2–4 · C 4–8 · X 8–12 · Ku 12–18
                   K 18–27 · Ka 27–40
deep space X       uplink 7.2 · downlink 8.4 GHz</div>
<h3>B · Section 5 map page (second sentence)</h3>
<div class="copy">S5 · atmosphere: wall with 2 windows (visible, radio);
     hard photons absorbed, long radio bounced; space links
     use S / X / Ka; uplink ≠ downlink frequency</div>
<h3>D · Question bank ("but how?" cards)</h3>
<div class="copy">Q: Why does the air stop UV but not radio?
A: E = h × f. A UV photon (5 eV) can break air molecules, so it
   is absorbed. A radio photon is a million times too weak.
Q: Why does infrared get absorbed if it is weaker than light?
A: Its energy matches how water and CO₂ molecules vibrate.
Q: Why can't you talk to a spacecraft on shortwave?
A: Below ~10 MHz the ionosphere reflects the wave back down.
Q: Why are uplink and downlink on different frequencies?
A: So the craft's transmitter doesn't deafen its own receiver.</div></div>
<div class="card" style="padding:9px 13px"><h3>C · One-line word bank (new lines)</h3>
<div class="copy">p__ · atmospheric opacity · how much the air blocks, per λ
p__ · atmospheric window · λ range that gets through  → C27
p__ · optical / radio window · visible / ~1 cm – 10 m
p__ · photon · one packet of light
p__ · photon energy · E = h × f; more f, more energy  → C27
p__ · Planck constant (h) · turns frequency into energy
p__ · absorption · photon gives its energy to a molecule
p__ · gamma / X-ray / UV · high energy; stopped up high
p__ · infrared (IR) · heat rays; absorbed by H₂O + CO₂
p__ · microwave · short radio, ~1–100 GHz
p__ · ionospheric reflection · long radio bounced back
p__ · critical frequency · below it the ionosphere reflects
p__ · VLF … EHF · decade bands, each 10× the last
p__ · SHF · 3–30 GHz: where satellites talk
p__ · letter bands · L S C X Ku K Ka (1–40 GHz)  → C28
p__ · S / X / Ka-band · the deep-space trio
p__ · uplink / downlink · Earth → s/c / s/c → Earth  → C28
p__ · deep space (radio) · beyond 2 million km
p__ · ITU · body that allocates frequencies
p__ · rain fade · rain weakens signals above ~10 GHz</div></div>
</div></div>'''
p6 = f'''<div class="page">{top(T("CONCEPT CARDS"),'Route E: <span>pages C27 and C28</span>','Two notebook pages, two cards each. Copy line for line; the faint numbers are your ruled lines.')}
<div style="display:flex;gap:16px;justify-content:center">{cA}{cB}</div>
<div style="text-align:center;font-size:10.5px;color:#444;margin-top:6px">C27: {a1} + {a2} lines of 22 · C28: {b1} + {b2} lines of 22</div></div>'''
p7 = f'''<div class="page">{top(T("SAY IT OUT LOUD"),'Last page: <span>prove it by talking</span>','After the spread and the 3-line summary, with everything closed. Send me what you said and I will grade it like a friend would.')}
<div class="two"><div>
<div class="card"><h3>🗣 The friend's opening question</h3><div style="font-size:13px;line-height:1.5">"Why do they put telescopes in space? And why does everything in space use radio?"</div></div>
<div class="card" style="margin-top:12px"><h3>✅ Three sentences you should be able to say</h3><ul class="r" style="font-size:12px">
<li>Because the air is a wall with two windows. Ordinary light gets through one and radio gets through the other, and nearly everything else is stopped.</li>
<li>It comes down to how hard each packet of light hits. X-rays and ultraviolet hit hard enough to break air molecules, so they are absorbed high up, and infrared gets soaked up by water and CO₂. Radio is too gentle to do anything, so it sails through.</li>
<li>So telescopes for X-rays or infrared have to sit above the air, and anything you want to say to a spacecraft has to go through the radio window, in agreed bands like S, X and Ka.</li></ul></div>
<div class="card" style="margin-top:12px"><h3>❓ Follow-ups a friend might ask</h3><ul class="r" style="font-size:12px">
<li>"Why can we see, then?" (our eyes use exactly the window where the air is clear and the Sun is brightest)</li>
<li>"Does all radio get through?" (no: very long waves bounce off the ionosphere, and rain hurts the highest bands)</li>
<li>"What do the band letters mean?" (nothing: old radar code names; X is around 8 GHz)</li>
<li>"Is Wi-Fi one of those?" (yes: 2.4 GHz is S-band, 5 GHz is C-band)</li>
<li>"What's uplink and downlink?" (ground to spacecraft, spacecraft to ground, on different frequencies so they don't clash)</li></ul></div></div>
<div><div class="card" style="min-height:3.2in"><h3>📝 Your explanation (paste or dictate)</h3><div style="border:2px dashed #999;border-radius:8px;height:2.5in;padding:8px;color:#999;font-size:11px">_ send it to me in chat; I'll put it here _</div></div>
<div class="card" style="margin-top:12px;min-height:2.2in;border-color:var(--green)"><h3 style="color:var(--green)">🎯 My read</h3><div style="border:2px dashed #999;border-radius:8px;height:1.5in;padding:8px;color:#999;font-size:11px">solid on: _<br>fuzzy on: _<br>fix: _<br>→ question-bank cards: _</div></div>
<div class="callout" style="margin-top:12px;font-size:11.5px">⚡ One lecture left in Section 5: satellite links. Send it the same way.</div></div></div></div>'''
write('s5-l2.html', [p1, p2, p3, p4, p5, p6, p7])
print('ok', a1, a2, b1, b2, len(vocab))
