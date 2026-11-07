# Section 2 — Space Environment

3 lectures, ~11 min.

## Before you watch

**Draw this first:** Earth, with a thin shell around it labeled
*atmosphere* (drag, atomic oxygen), two donut-shaped bands around that
labeled *Van Allen radiation belts*, the Sun off to one side firing
*solar wind / solar flares*, and little dots everywhere labeled *debris
and micrometeoroids*. Then write on the spacecraft itself: *vacuum,
hot/cold swings, no gravity to sit on*. That drawing is the whole
section.

**Why this section exists:** space isn't "nothing." It's a list of ways
hardware dies. Every later subsystem is designed around this list.

**Plain-English terms you'll hear:**
- **Vacuum** — no air. Two consequences: materials *outgas* (trapped
  gases bleed out and can fog lenses), and there's **no convection** —
  heat can only leave by *radiation* (glowing it away) or *conduction*
  through solid parts. No fan can cool a satellite.
- **Thermal extremes** — sunlit side can be +120 °C, shaded side −150 °C
  on the same object at the same time. Hence gold/silver blankets (MLI),
  radiators, heaters, and spinning or slewing to even things out.
- **Radiation** — three sources: *trapped particles* in the **Van Allen
  belts** (worst for MEO and anything crossing them), *solar particle
  events* (flares/CMEs), and *galactic cosmic rays* (rare, very
  energetic, from outside the solar system). Two effects: **total
  ionizing dose** (TID: slow cumulative damage, electronics drift and
  solar cells lose output) and **single-event effects** (SEU: one
  particle flips a bit or latches up a chip). Fix: rad-hard parts,
  shielding, error-correcting memory, watchdogs.
- **Atomic oxygen (AO)** — in LEO (~200–700 km) the thin air is mostly
  single oxygen atoms, which chemically eat polymers like Kapton. Fix:
  protective coatings.
- **Atmospheric drag** — in LEO there's still enough air to slow you
  down. ISS re-boosts regularly; uncontrolled LEO sats eventually
  re-enter. Higher = less drag; the solar cycle puffs the atmosphere up
  and makes it worse.
- **Microgravity** — not "no gravity" (at ISS altitude it's ~90% of
  surface gravity); it's *free fall*. Consequences: fluids don't settle
  (propellant tank design), nothing sits still, no convection.
- **Debris and micrometeoroids** — hypervelocity impacts (~10 km/s). A
  paint fleck cracks a window. Fix: Whipple shields (a sacrificial outer
  wall that vaporizes the impactor), tracking and avoidance for bigger
  objects. The runaway-collision scenario is the **Kessler syndrome**.
- **Plasma and spacecraft charging** — the spacecraft collects charge
  from the surrounding plasma; differential charging between surfaces
  causes arcing. Fix: conductive coatings, grounding everything.

**Quick inverse-square reminder** (you'll need it in Section 7 too):
sunlight intensity at Earth is ~1,361 W/m². At Mars (1.52 AU) it's
1,361 / 1.52² ≈ 590 W/m². At Jupiter (5.2 AU) it's ~50 W/m².

## Your notes (brain-dump, video closed)

> _write here_

## Transcript

<details><summary>Transcript</summary>

_paste here_

</details>

## Recall quiz

1. Why can't a satellite use a fan to cool its electronics? What does it
   use instead?
2. What's the difference between total ionizing dose and a single-event
   upset? Give one mitigation for each.
3. Which orbit regime is worst for trapped radiation, and why?
4. Name two things in LEO that are *not* problems in GEO.
5. "Astronauts float because there's no gravity on the ISS." What's
   wrong with that sentence?
6. What is a Whipple shield and why does a thin outer sheet help more
   than you'd expect?

<details><summary>Answers</summary>

1. No air, so no convection. Heat leaves only by radiation (radiator
   panels facing cold space) and conduction (heat pipes, straps to the
   radiator).
2. TID is slow cumulative damage from accumulated dose (parts degrade,
   solar cells lose output) — mitigate with shielding and rad-hard
   parts, and design margins for end-of-life output. SEU is a single
   particle flipping a bit or triggering latch-up — mitigate with
   error-correcting memory, redundant voting logic, watchdog resets,
   latch-up current limiters.
3. MEO (roughly 2,000–20,000 km, e.g. GPS altitude) sits in the Van
   Allen belts, so it accumulates dose fastest. GEO is above the worst
   of it; LEO is mostly below it (except the South Atlantic Anomaly).
4. Atmospheric drag and atomic oxygen (both need residual atmosphere).
   Also frequent eclipses (~15/day in LEO vs. a few weeks a year of
   short eclipses in GEO).
5. Gravity at ISS altitude is ~90% of surface gravity. They float
   because the station and everyone in it are in free fall together —
   continuously falling around Earth. "Microgravity" means free fall,
   not absence of gravity.
6. A sacrificial outer wall spaced away from the hull. A hypervelocity
   impactor hitting it shatters/vaporizes into a spray that spreads out
   before reaching the real wall, so the energy is distributed over a
   wide area instead of punching a hole.

</details>
