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
| 4 | Space Propulsion Systems | 5 | 27 min | `sections/04-space-propulsion.md` | [ ] |
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
| 2026-11-09 | 3 | Lec 2 "Earth Orbits + constellations": transcript + 2 slides. PDF: `feedback/S3-L2-earth-orbits-v1.pdf`. Mostly repeats S1 satellite page; new = periods, why 35,786, coverage-vs-detail trade-off, constellations. Student proposed skipping; agreed to a 4-line add-on to the S1 page instead of a new spread. Instructor loose: "36,000 km from center" (that is altitude; center ≈ 42,164). Section 2 confirmed 3/3 complete in Udemy. |
| 2026-11-09 | 3 | Lec 1 "Orbital Mechanics: definition + 6 parameters": transcript + 4 slides. PDF: `feedback/S3-L1-orbital-mechanics-definition-and-parameters.pdf` (hula-hoop analogy for a/e/i/Ω/ω/ν; instructor wrong on reference plane/direction for Earth orbits (said ecliptic / toward Sun; correct: equator / vernal equinox ♈); 8 caption errors). Section 2 third lecture not yet confirmed. Student decided: one spread per video, not per section. |
| 2026-11-08 | 2 | Lec 5 "Earth Atmosphere": transcript + 3 slides. PDF: `feedback/S2-L5-earth-atmosphere.pdf` (layer stack + temperature zigzag drawing; 8 caption errors tabled; instructor loose on "AO appears at 320-340 km" (dominant from ~200 km per his own chart) and on atomic N; drag not covered by the lecture, flagged). Section 2 = 2/3 lectures done. |
| 2026-11-07 | 2 | Lec 4 "Space Vacuum Conditions": transcript + all 6 slides received. PDF: `feedback/S2-L4-space-vacuum.pdf` (5 "free services" diagram, fact checks: 0.3 µm not mm, corrosion vs UV bond-breaking, "no dissipation" overstated; vocabulary page added at student request). Section 1 complete (4/4). |
| 2026-11-07 | 1 | Student sent a photo of their first Cornell page (satellite types, LEO/MEO/GEO altitudes — all correct). Feedback PDF: `feedback/S1-satellite-types-and-orbits.pdf` (geosync vs geostationary, why 35,786 km, harder cues, group the 8 types by job, draw the left page). |
