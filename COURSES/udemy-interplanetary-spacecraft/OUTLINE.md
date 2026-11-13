# Interplanetary Spacecraft and Satellite Engineering (Udemy)

**Status: ACTIVE course (started 2026-11-07).** Replaces the Network+
track for now — see root `CLAUDE.md` § Current focus.

- **Course:** "Aerospace Engineering: A Complete Guide to Design and
  Technology of Interplanetary Rocket Space Missions and Satellites"
  (Udemy Business, via the student's employer account). ~3.5 hours of
  video total, 7 sections visible so far.
- **What it is:** a survey course. Short lectures, a little math (orbit
  periods, time of flight, rocket equation, link budgets). The risk is
  not volume — it's watching it like TV and keeping nothing.
- **How we work it:** one file per section in `sections/`. Each has a
  *Before you watch* primer (draw-first prompts, key terms explained in
  plain English), a *Your notes* block the student fills in from memory
  after watching, a place to paste the Udemy transcript, and a short
  recall quiz written by Claude. Method details: `NOTES_METHOD.md`.
- **Claude's job per section:** after the student pastes their brain-dump
  (and optionally the transcript), check it for errors, draw the diagram
  the lecture should have drawn (inline SVG, same standard as the
  Network+ reference chapters), grade the quiz, and add any missed idea
  to the primer so the file becomes the section's standing reference.

## Syllabus (mirrors the Udemy course panel)

| # | Section | Lectures | Length | File | Done |
|---|---------|----------|--------|------|------|
| 1 | Presentation, intro to space engineering, mission design & objectives, Quiz 1 (time of flight) | 3 + quiz | 13 min | `sections/01-mission-design-and-time-of-flight.md` | [x] 2026-11-07 |
| 2 | Space Environment | 3 | 11 min | `sections/02-space-environment.md` | [ ] |
| 3 | Orbital Mechanics | 3 | 34 min | `sections/03-orbital-mechanics.md` | [ ] |
| 4 | Space Propulsion Systems | 5 | 27 min | `sections/04-space-propulsion.md` | [x] 2026-11-12, 4 lectures (the panel's 5th item is unconfirmed, probably a quiz) |
| 5 | Communications from Space to Earth | 3 | 44 min | `sections/05-communications.md` | [x] 2026-11-12, 3 lectures |
| 6 | Attitude Determination and Control | 4 | 36 min | `sections/06-attitude-determination-and-control.md` | [x] 2026-11-12, 3 lectures (the panel's 4th item is unconfirmed, probably a quiz) |
| 7 | Space Power Systems | 3 + Quiz 5 (designing a photovoltaic array) | 33 min | `sections/07-space-power-systems.md` | [x] 2026-11-12, 3 lectures (Quiz 5 not yet taken) |
| 8+ | *(not visible in the course panel yet — add when known)* | | | | |

Visible sections sum to ~3.3 hours, so there is at most one short
section beyond 7. Add it to this table when the student scrolls to it.

## Pace

No fixed schedule. A section a sitting is realistic (longest is 44 min
of video plus maybe 20 min of notes and quiz). Finishing in two weeks at
the student's ~1 hour/day budget is comfortable; a month is fine. Tick
the Done column and date it when a section's quiz is graded.

## Session log

| Date | Section | What happened |
|------|---------|---------------|
| 2026-11-07 | — | Course adopted; Network+ paused. Scaffold written. |
| 2026-11-07 | 1 | Lec 3 slide "Types of interplanetary spacecraft" (flyby → orbiter → atmospheric → lander → rover → penetrator, + observatory, comms). PDF: `feedback/S1-L3-types-of-interplanetary-spacecraft.pdf` (the "commitment ladder" diagram, examples, Q-bank cards). |
| 2026-11-11 | 1-3 | Mechanism pass: "how it actually works" rows with worked numbers added to all 7 scenes in the app (+11 MC, +11 cards, +15 terms → 72 / 63 / 193). Header toggle 🧒/🛠 added; Terms tab mode-aware; "How this app helps you" card on Today. Complete word bank (161 lines) + complete glossary v2 (10 pp) issued; notebook map v2 (30 back pages). |
| 2026-11-10 | 1-3 | Student flagged missing official terminology (saw "Classical Keplerian Elements" on Google). Added a **Terms** tab to the app: 115 official terms with also-called names and plain meanings, searchable, filter by scene. New standing rule: name it, then explain it. |
| 2026-11-10 | 1-3 | Teach-back split into per-section talks (S1 3¼ min, S2 3 min, S3 4¼ min) + full 7 min, in the app Teach tab and in `review/Teach-It-Back-Kit-S1-S3-v3.pdf` (section talks pp 12-13; engineer-level mechanism pages 4-10 added 2026-11-11). Student will use the PDF on a call. |
| 2026-11-10 | 2 | Added atmospheric composition to the app at student request ("need to know everything"): Go-deeper table on the air scene (gas mix by height: N₂/O₂/Ar/CO₂ → atomic O → He → H; ozone; ionosphere; anomalous O), +8 MC, +8 cards. |
| 2026-11-10 | 1-3 | Built the **Space X Study** app (interactive quiz, flashcards with spaced review, ELI5 scenes, timed teach-back): https://claude.ai/artifact/CnDfEEJHGhs76GMZNu7BSM · source in `app/`. Content = the Teach-It-Back Kit, interactive. |
| 2026-11-09 | 1-3 | REVIEW PAUSE at student's request. Built `review/Teach-It-Back-Kit-S1-S3-v1.pdf` (7 pp): the one-paragraph through-line, 7 scenes re-taught at 5th-grade level with "SAY" lines and napkin drawings, minute-by-minute 7-minute teach-back script, 24-question quiz (F/W/A types) + answers keyed to scenes, rehearsal plan (3 runs, record run 3), cue card. Next: student does quiz cold, rehearses, sends recording/transcript for grading. |
| 2026-11-09 | 3 | Lec 3 "Interplanetary transfers + flybys" (Lambert, Hohmann, gravity assist, Rosetta): transcript + 5 slides. PDF: `feedback/S3-L3-interplanetary-transfers-and-flybys-v1.pdf`. Instructor loose: Lambert inputs/outputs reversed; "most efficient" (almost always); flyby-can-brake and the 26-month phase angle not covered. Who's Who updated to v2 (67P, Hohmann/Lambert, Galileo ambiguity, GLONASS/BeiDou). Section 3 complete → conversation test due. Student missed the "why not over New York" check (gave the LEO 90-min answer); corrected. |
| 2026-11-09 | 3 | Lec 2 "Earth Orbits + constellations": transcript + 2 slides. PDF: `feedback/S3-L2-earth-orbits-v1.pdf`. Mostly repeats S1 satellite page; new = periods, why 35,786, coverage-vs-detail trade-off, constellations. Student proposed skipping; agreed to a 4-line add-on to the S1 page instead of a new spread. Instructor loose: "36,000 km from center" (that is altitude; center ≈ 42,164). Section 2 confirmed 3/3 complete in Udemy. |
| 2026-11-09 | 3 | Lec 1 "Orbital Mechanics: definition + 6 parameters": transcript + 4 slides. PDF: `feedback/S3-L1-orbital-mechanics-definition-and-parameters.pdf` (hula-hoop analogy for a/e/i/Ω/ω/ν; instructor wrong on reference plane/direction for Earth orbits (said ecliptic / toward Sun; correct: equator / vernal equinox ♈); 8 caption errors). Section 2 third lecture not yet confirmed. Student decided: one spread per video, not per section. |
| 2026-11-08 | 2 | Lec 5 "Earth Atmosphere": transcript + 3 slides. PDF: `feedback/S2-L5-earth-atmosphere.pdf` (layer stack + temperature zigzag drawing; 8 caption errors tabled; instructor loose on "AO appears at 320-340 km" (dominant from ~200 km per his own chart) and on atomic N; drag not covered by the lecture, flagged). Section 2 = 2/3 lectures done. |
| 2026-11-07 | 2 | Lec 4 "Space Vacuum Conditions": transcript + all 6 slides received. PDF: `feedback/S2-L4-space-vacuum.pdf` (5 "free services" diagram, fact checks: 0.3 µm not mm, corrosion vs UV bond-breaking, "no dissipation" overstated; vocabulary page added at student request). Section 1 complete (4/4). |
| 2026-11-07 | 1 | Student sent a photo of their first Cornell page (satellite types, LEO/MEO/GEO altitudes — all correct). Feedback PDF: `feedback/S1-satellite-types-and-orbits.pdf` (geosync vs geostationary, why 35,786 km, harder cues, group the 8 types by job, draw the left page). |

- **2026-11-11 (later)** — Student: "add these to the app too and I need
  the word bank to explain these words better… understand the meaning and
  concept around the word completely." App v8: new **Numbers** tab
  (equations with a worked value each, constants, mission numbers), the
  15 "but how?" Q/A cards added to the explain-out-loud quiz (WHY now 28),
  a per-scene "when they ask but how?" mechanism line on every Learn
  card, and 32 core terms given a concept layer (why it exists · example
  with numbers · don't confuse with · connects to) in the Terms tab.
  `Word-Bank-CONCEPTS-S1-S3-v4.pdf` (9 pp; v3 withdrawn for a wrong torque number) is the same 32 entries on
  paper, with a note on what to copy into the notebook (name/also/meaning
  only; concept + numbers go in the lecture-page margin).

- **2026-11-11 (later still)** — Student wants the concept word bank
  handwritten. Issued `Word-Bank-CONCEPT-CARDS-notebook-S1-S3-v1.pdf`
  (10 pp): 8 full-size spreads = notebook pages C1–C16, two cards a
  page, plus a map page. Told the student plainly that the whole-course
  word bank (~45 pp) no longer fits one ~95-page notebook; plan is cards
  at 44-from-the-end now, second notebook before Section 7. Notebook's
  real page count still unconfirmed. App v9: three number corrections.

- **2026-11-12** — **Section 4 started** (student's decision; the S1 talk
  run and the S3 conversation test are still ungraded). Lec 1 "Space
  propulsion: definitions + types" and Lec 2 "Chemical engines
  (rockets)": transcripts + all slides (3 + 4). PDFs:
  `feedback/S4-L1-space-propulsion-definitions-and-types-v1.pdf` (6 pp)
  and `feedback/S4-L2-chemical-engines-v1.pdf` (7 pp), now with a "copy
  into notes" page (routes A-E) and concept-card pages C17-C19 in
  notebook layout. Instructor wrong/loose: electric propulsion "from
  the 1980s, kind of new" (first flown 1964, operational 1971); nuclear
  "being developed by NASA right now" (NERVA ended 1972, DRACO
  cancelled 2025 as far as known, nothing has flown); "lightest and
  highest thrust" (best thrust-to-weight, heaviest system); nozzle
  "maximizes pressure" (it spends pressure for speed); "commonly liquid
  hydrogen" while both photographed engines burn kerosene. App v10:
  scene 8 "Throw it backward" (16 MC, 6 explain, 16 cards, 36 terms,
  10 concept entries, 3 formulas). Who's Who v3 (page 3 = S4 names).
  Remaining S4 lectures (electric, nuclear, ...) to come from the
  student; the Section 4 talk, word-bank sheet and glossary PDF get
  rebuilt once the section is complete.

- **2026-11-12 (later)** — S4 Lec 3 "Electric propulsion + ion
  thrusters": transcript + 4 of 7 slides (2, 4, 5, 7; slides 3 and 6
  reconstructed from the transcript). PDF:
  `feedback/S4-L3-electric-propulsion-ion-thrusters-v1.pdf` (7 pp):
  ion-thruster cutaway + four steps + tortoise/hare speed-time sketch;
  mechanism with Deep Space 1 numbers (1,100 V -> 40 km/s, 0.092 N from
  2.3 kW, 16 m/s per day, 4.3 km/s from 74 kg Xe); concept cards
  C20-C21 (EP, ion thruster, plasma, neutralizer). Instructor loose:
  "breaking electronic bonds" (it is ionization of single atoms);
  plasma = "the positive particles" (ions AND electrons); neutralizer
  explained as letting gas disperse (real reason: charge balance);
  BepiColombo's ion engines are for the cruise to Mercury, not
  maneuvers around it (arrival was planned for Nov 2026; not
  verified); low thrust blamed on mass flow rather than power; Hall
  thruster never mentioned. 14 caption errors tabled. App v11: scene 9
  "The tortoise engine" (12 MC, 4 explain, 12 cards, 21 terms, 5
  concept entries, 2 formulas). Two S4 lectures remain.

- **2026-11-12 (evening)** — S4 Lec 4 "Nuclear propulsion: nuclear
  thermal rockets": transcript + 5 slides. PDF:
  `feedback/S4-L4-nuclear-thermal-rockets-v1.pdf` (7 pp), concept cards
  C22-C23 (NTR, molecular mass, payload, enrichment). **Most errors of
  any lecture so far:** (1) "high Isp because working temperatures are
  higher" (the core is cooler than a flame; Isp doubles because the
  exhaust is H2, v_e goes as sqrt(T/M)); (2) Project Orion called a
  1986 NASA nuclear thermal project (it was a 1958-65 nuclear PULSE
  study, not NASA's); (3) "attractive for interstellar flight" (75,000
  years to the nearest star); plus "sketched in the 1960s" (about 20
  reactors were run), "lift-off mass is half" (in-orbit stage),
  "high-velocity liquid" (it is gas), lecture dated 2018. Instructor
  says this closes the section. **Section 4 complete on Claude's side:**
  app v12 has scene 10 "The kettle with no fire" (12 MC, 4 explain, 12
  cards, 17 terms, 4 concept entries) and a Section 4 timed talk
  (`PROGRAMS.s4`, 4 min). Lecture 1 PDF reissued as v2 (it said nuclear
  hydrogen is heated to "about the same" temperature as a flame;
  corrected to cooler-but-lighter). Who's Who v4. Due from the student:
  Section 4 map page from memory, one Section 4 talk run; still
  outstanding: Section 1 talk run and Section 3 conversation test.

- **2026-11-12 (night)** — **Section 5 started.** Lec 1
  "Communications: antennas": transcript + slides 2-7 of 8 (slide 8,
  the Cassini / Apollo 17 examples, reconstructed from the transcript).
  PDF: `feedback/S5-L1-communications-antennas-v1.pdf` (9 pp). **Two
  spreads** for this lecture (it holds two separate ideas and would not
  fit one): (1) waves, c = lambda x f, half-wave antenna, modulation;
  (2) isotropic / omni / directional, gain, HGA vs LGA. Concept cards
  C24-C26. Instructor loose: "wavelength of my voice" (voice is sound;
  his 3,000 km is a radio wave at 100 Hz); modulation justified only by
  antenna size (also channel sharing and data rate); AM/FM presented as
  if spacecraft use them (they use phase modulation); "higher frequency
  = smaller antenna" holds for rods, not dishes; gain described as
  "more information"; Apollo 17 HGA/LGA explanation muddled. Worst
  captions so far (14 tabled). App v13: scene 11 "The radio flashlight"
  (16 MC, 5 explain, 16 cards, 33 terms, 6 concept entries, 4
  formulas). Who's Who v5 (page 4 = Section 5 names). Tied explicitly to
  the student's networking background (Wi-Fi 2.4 GHz = 12.5 cm, dBi).

- **2026-11-12 (late night)** — S5 Lec 2 "Atmospheric absorption +
  typical telecom frequencies": transcript + all 3 content slides. PDF:
  `feedback/S5-L2-atmosphere-and-frequency-bands-v1.pdf` (7 pp), one
  spread (wall with two windows; why, by photon energy; band-letter
  strip), concept cards C27-C28 (atmospheric window, photon energy,
  frequency bands, uplink/downlink). Instructor loose: absorption
  explained as "high energy interacts basically always" (it is about
  the photon energy matching something the molecule can do, which is
  why weaker infrared is absorbed and visible passes); long-wave radio
  "blocked" without saying it is reflected by the ionosphere; no reason
  given for separate uplink/downlink frequencies or for moving to
  higher bands; slide table lumps Ku/K/Ka. He was right about eyes and
  the visible window. Linked back to Section 1 (why "look out"
  telescopes are in orbit) and Section 2 (ozone, ionosphere, eV). App
  v14: scene 12 "Two windows in the wall" (14 MC, 4 explain, 12 cards,
  23 terms, 4 concept entries, 2 formulas). Who's Who v6. One Section 5
  lecture left (satellite links).

- **2026-11-12 (last of the day)** — S5 Lec 3 "Satellite and
  spacecraft links": transcript + slides 2, 3, 5, 6 of 6. PDF:
  `feedback/S5-L3-satellite-and-spacecraft-links-v1.pdf` (9 pp): chain
  diagram + power zigzag + link equation; a full worked link budget
  (Cassini to a 70 m dish: +13 dBW, +47 dB, -294 dB, +74 dB = -160 dBW;
  N0 at 20 K; S/N0 about 56 dB-Hz, about 100 kbit/s) with a decibel
  primer tied to Wi-Fi dBm; concept cards C29-C31. Instructor wrong or
  loose: called 1/k "a relation for wavelength" (k is the Boltzmann
  constant, N0 = kT); LNA "avoids mistaking signal for noise" (no
  amplifier can; it adds little noise of its own and is first in the
  chain); free-space loss not explained as spreading; "encoder" given
  as voice-to-electrical (that is a microphone; encoding = compression
  + error correction); up-conversion blurred with modulation; gain
  mixed with power; diagram is a relay (comsat) link. **Section 5
  complete:** app v15 has scene 13 "Shouting across a stadium" (14 MC,
  5 explain, 14 cards, 26 terms, 6 concept entries, 3 formulas) and a
  Section 5 timed talk (`PROGRAMS.s5`, 4 min). Who's Who v7. Owed by
  the student now: Section 5 map page + talk, Section 4 map page +
  talk, Section 1 talk, Section 3 conversation test. Nothing has been
  explained back since Section 3; flagged to the student.

- **2026-11-12 (after midnight push)** — **DEADLINE disclosed by the
  student: they must understand the rest of the course by the night of
  2026-11-13.** They are sending lectures while listening and said "we
  will review all this later" about the outstanding talk runs. What the
  deadline event is (call, test, presentation) is not yet known; asked.
  **Lean mode from here until the deadline:** lecture PDFs are spread(s)
  + TEACH + FACT CHECK (with a short say-it-out-loud box) + VOCABULARY
  only; the copy-into-notes page and concept-card pages are paused, as
  is Who's Who. App scenes are still added per lecture.
  S6 Lec 1 "Attitude: definitions and physics" (16:51): transcript + 5
  slides. PDF `feedback/S6-L1-attitude-definitions-and-physics-v1.pdf`
  (5 pp, two spreads: attitude + loop + jitter; spin stability).
  Instructor wrong/loose: moment of inertia described as "amount of
  mass in a direction" (it is distance from the axis; his conclusions
  are right); Explorer 1 called a failure (it tumbled but worked four
  months and found the radiation belts); "Russians understood it, US
  marketing style" (nobody knew the rule; Explorer's tumble taught it);
  sphere "moves randomly"; major-axis rule stated without the energy
  loss it depends on; sensors said to compute the error; jitter "cannot
  be corrected"; slide says inertial frame but draws the orbital frame.
  App v16: scene 14 "Point, check, nudge" (14 MC, 4 explain, 12 cards,
  23 terms, 4 concept entries, 3 formulas).

- **2026-11-12 (deadline push)** — S6 Lec 2 "Sensors": transcript + all
  7 content slides. Lean PDF `feedback/S6-L2-attitude-sensors-v1.pdf`
  (4 pp): what each sensor looks at, gyro-drift sawtooth, accuracy
  ladder; six-sensor comparison table. Added what the lecture never
  says: one direction fixes only two angles, and gyros drift, which is
  why sensors are combined. Instructor loose: gyroscope "determines
  position and orientation" (rotation rate only); the Cubli called a
  gyroscope (it is a reaction-wheel balancing cube = actuators); star
  trackers justified by a dim Sun (they are chosen for accuracy and are
  standard in Earth orbit); Earth "100-1000 K" (about 255 K); GPS
  attitude explained by positions (it uses arrival-time differences).
  App v17: scene 15 "Inner ear, eyes and a compass" (12 MC, 4 explain,
  10 cards, 16 terms, 3 concept entries, 2 formulas).

- **2026-11-12 (deadline push)** — S6 Lec 3 "Actuators": transcript +
  all 7 content slides; the instructor says it closes the section. Lean
  PDF `feedback/S6-L3-attitude-actuators-v1.pdf` (4 pp): reaction wheel
  vs CMG, magnetic torquer vs thrusters, saturation sawtooth;
  five-actuator comparison table. Added the idea the lecture never
  states: internal actuators (wheels, CMGs) only swap angular momentum,
  external ones (thrusters, magnetorquers) change the total, hence
  saturation and momentum dumping. Instructor loose: saturation blamed
  on "instabilities" (steady disturbance torques); momentum vs reaction
  wheel blurred; "65,000 rpm" (flight wheels run a few thousand); CMG
  called a full set of wheels (one wheel on a gimbal); slew rate called
  responsiveness; magnetorquer called a sensor and "like a CMG"; cold
  gas "usually CO2" (nitrogen); slide typos "Reactor wheels", "3 axis
  determination". **Section 6 complete on Claude's side:** app v18 has
  scene 16 "Spin a wheel, turn the ship" (14 MC, 4 explain, 12 cards,
  15 terms, 4 concept entries, 4 formulas) and a Section 6 timed talk
  (`PROGRAMS.s6`, 4¼ min). Next: Section 7, space power systems.

- **2026-11-12 (deadline push)** — **Section 7 started.** The course
  panel (seen in a screenshot) lists: 19 Solar Array Technology
  (14 min), 20 Batteries (10 min), 21 Radioisotope Thermal Generators
  (9 min), Quiz 5 "Designing a Photovoltaic Array". S7 Lec 1 "Solar
  arrays": transcript + all 6 content slides. Lean PDF
  `feedback/S7-L1-solar-arrays-v1.pdf` (4 pp): flux bars by planet,
  p-n junction with circuit, triple-junction stack, power formula; a
  sizing table and three-step recipe aimed at Quiz 5 (1 kW needs 3.1 m2
  at Earth, 7.1 at Mars, 83 at Jupiter with 30% cells and 0.8 losses).
  Instructor loose: triple junction "multiplies efficiency by three"
  (about 20% to 30%); photon gives the electron "inertia" (the junction
  field drives it); electron/hole directions tangled; LEO "two hours,
  12 cycles a day" (90-100 min, 15-16); slide equates thermal cycling
  with low efficiency; clean-room photo credited to Rosetta (looks like
  Juno). App v19: scene 17 "The sunlight sandwich" (14 MC, 4 explain,
  12 cards, 18 terms, 3 concept entries, 3 formulas). App patches now
  go through `app/applib.py` (dedupes terms automatically).

- **2026-11-12 (deadline push)** — S7 Lec 2 "Batteries": transcript +
  slides 2, 4, 5 of 5 (slide 3, the definitions and DoD formula,
  reconstructed from the transcript). Lean PDF
  `feedback/S7-L2-batteries-v1.pdf` (4 pp): primary vs secondary,
  charge zigzag with DoD, life-vs-DoD curve with the slide's values,
  sizing formula; a five-step sizing recipe and a low-orbit vs GEO
  table. Instructor loose: battery called "auxiliary, low power" (it is
  the only source in eclipse); "penumbra time" for eclipse; "two-hour
  cycle, 12 a day" again (about 92 min, 16 a day; he says 1.5 h earlier
  in the same lecture); secondary "low energy density" (lower, not
  low); no account of how a cell works, which chemistries fly, or that
  the array must also recharge the battery. App v20: scene 18 "The
  bucket for the dark" (12 MC, 4 explain, 10 cards, 15 terms, 3 concept
  entries, 3 formulas). One lecture left: RTGs.

- **2026-11-12 (end of the push)** — S7 Lec 3 "Radioisotope Thermal
  Generators (RTG)": transcript + all 4 content slides. Lean PDF
  `feedback/S7-L3-radioisotope-generators-RTG-v1.pdf` (4 pp): decay,
  finned cross-section + thermocouple, fading curve, which power where;
  a table of all Section 7 power sources; Galileo's slide numbers
  checked against the half-life (290 W x 0.895 = 260 W, ageing takes it
  to 250). Instructor loose: name ("thermal" for thermoelectric); "500
  years" spoken vs 100 on his slide (useful life is decades); "1.50 m"
  vs 114 cm on the slide; "temperature ejected from the nucleus"; "only
  for space" (Soviet Sr-90 lighthouses, pacemakers); ESA "developing
  strontium" (americium-241 as far as known); efficiency never given.
  **ALL SEVEN SECTIONS NOW HAVE LECTURE PDFs (23 lectures).** App v21:
  scene 19 "The rock that stays warm" (12 MC, 4 explain, 10 cards, 12
  terms, 3 concept entries, 3 formulas), `PROGRAMS.s7` (3.5 min) and
  `PROGRAMS.all` = whole-course 7-minute talk (the old "full" talk is
  relabelled "S1-S3 talk"). New: `review/Whole-Course-Review-S1-S7-v1.pdf`
  (2 pp: all seven sections on one page with say-this / number /
  don't-repeat; a five-block three-hour plan for 2026-11-13 and the
  Quiz 5 recipe). The deadline event is still unknown (asked four
  times). Nothing explained back since Section 3 (16 lectures).

- **2026-11-12 (after the last lecture)** — Student answered the open
  question: **the deadline is a call with a friend on the night of
  2026-11-13; the friend has already taken this course and will check
  what the student has learned and understood.** Student also asked for
  every PDF combined "like a notebook". Built
  `Space-X-Notebook-COMPLETE-S1-S7-v1.pdf` (169 pp, ~20 MB) with
  `notebook-src/build_notebook.py`: contents page, whole-course review
  (2 pp), a new 2-page **call sheet** (three likely questions per
  section with one-breath answers, how to answer anything, and eight
  instructor errors the friend may repeat because he learned from the
  same course), then the seven sections in course order, each behind a
  new divider page (say-this sentence, talk cue card pulled from the
  app's `PROGRAMS`, lecture page numbers, number to know, don't
  repeat), then the back matter (teach-back kit v3, concept cards,
  word banks, glossary, copy-into-notes, Who's Who v7, notebook map).
  Page numbers stamped top right on every page; PDF bookmarks per
  section and lecture. Only the latest version of each PDF is included;
  the three layout how-to PDFs are left out.
- **2026-11-13 — Notebook in the app, Duo layout, Homelab HQ link.** App
  Version 23 adds a Notebook tab: the 169-page combined notebook as page
  images (`app/dist/nb/`), with half-page, whole-page, split-at-hinge and
  two-page views, zoom, full screen, contents and section chips. "The
  DUO" turned out to be the student's foldable iPhone; sizes and layout
  rules came from the Homelab HQ session, which this session can now
  message. `app/dist/` is the ready-to-serve folder for hosting on the
  homelab (not deployed; the student decides, after the call). Progress
  tab gained Export/Import. Tested locally at the seven Duo sizes, on a
  laptop size, and offline from a localhost copy; not tested on the real
  device.
