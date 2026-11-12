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
| 4 | Space Propulsion Systems | 5 | 27 min | `sections/04-space-propulsion.md` | [ ] 3 of 5 lectures (2026-11-12) |
| 5 | Communications from Space to Earth | 3 | 44 min | `sections/05-communications.md` | [ ] |
| 6 | Attitude Determination and Control | 4 | 36 min | `sections/06-attitude-determination-and-control.md` | [ ] |
| 7 | Space Power Systems | 4 | 33 min | `sections/07-space-power-systems.md` | [ ] |
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
