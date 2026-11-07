# Section 1 — Course intro, mission design & objectives, Quiz 1 (time of flight)

Lectures: 1. Presentation of the Course (3 min) · 2. Introduction to
Space Engineering and Course Structure (2 min) · 3. Define your Mission
Design and objectives (8 min) · Quiz 1: Time of flight quiz.

## Before you watch

**Draw this first:** a box labeled *Mission objective* at the top, an
arrow down to *Requirements* (what must it do, how precisely, for how
long, within what mass/power/cost), then arrows fanning out to the
subsystems that every spacecraft is made of. Guess the subsystems
before you read on.

```
          Mission objective  ("map Mars' surface at 1 m resolution")
                  |
             Requirements     (orbit, lifetime, pointing, data rate, mass, $)
                  |
   +-------+------+------+--------+-------+--------+---------+
 Payload Structure Thermal Power Propulsion ADCS  Comms  C&DH
```

The course's later sections are literally these boxes, one per section
(Environment → what you must survive; Orbits → where you are;
Propulsion → how you get there; Comms → talking to Earth; ADCS →
which way you point; Power → staying alive).

**Plain-English terms you'll hear:**
- **Payload** — the part that does the job (camera, radar, science
  instrument). Everything else is the "bus": the truck that carries it.
- **Mission design** — choosing the orbit, trajectory, lifetime, and
  budget *before* designing hardware. The objective drives the orbit;
  the orbit drives everything else.
- **Budgets** — not just money. Engineers keep a *mass budget*, *power
  budget*, *Δv (delta-v) budget*, and *link budget*. Each is a ledger of
  how much you have vs. how much you spend.
- **Time of flight (TOF)** — how long a transfer between two orbits
  takes. For the standard "Hohmann" transfer (half an ellipse touching
  both orbits), TOF is exactly **half the period of the transfer
  ellipse**.

**The one equation (work it yourself before the quiz):**

Orbital period  T = 2π · √(a³ / μ)
Hohmann TOF     = T / 2 = π · √(a³ / μ)

- `a` = semi-major axis of the transfer ellipse = (r₁ + r₂) / 2, where
  r₁ and r₂ are the two orbit radii **measured from Earth's center**
  (altitude + 6,371 km), not from the surface.
- `μ` (mu) = Earth's gravitational parameter = **398,600 km³/s²**.
  Keep km and seconds throughout.

Worked example — 300 km LEO to GEO (35,786 km altitude):

| Step | Value |
|---|---|
| r₁ = 6371 + 300 | 6,671 km |
| r₂ = 6371 + 35,786 | 42,157 km |
| a = (r₁ + r₂)/2 | 24,414 km |
| a³ / μ | ≈ 3.65 × 10⁷ s² |
| √ | ≈ 6,042 s |
| × π | ≈ 18,980 s ≈ **5.3 hours** |

That's the answer every reference gives for a LEO→GEO Hohmann: about
5¼ hours. If your number is off by a factor of ~1000, you mixed km and
m. If it's off by 2×, you used T instead of T/2.

## Your notes (brain-dump, video closed)

> _write here_

## Transcript (paste from Udemy's Transcript button)

<details><summary>Transcript</summary>

_paste here_

</details>

## Recall quiz (do it cold, then check)

1. What's the difference between the payload and the bus?
2. Name five subsystems every spacecraft has.
3. Why do engineers say "the orbit drives everything else"? Give two
   examples of a design choice the orbit forces.
4. A satellite moves from a 500 km circular orbit to a 20,000 km
   circular orbit via a Hohmann transfer. What is `a` for the transfer
   ellipse? (Earth radius 6,371 km.)
5. Using μ = 398,600 km³/s², what is the time of flight for question 4,
   in hours?

<details><summary>Answers</summary>

1. Payload does the mission's job (instrument, camera, antenna for a
   comms sat); the bus is everything that keeps the payload alive,
   pointed, powered, and talking to Earth.
2. Any five of: structure, thermal, power, propulsion, attitude
   determination & control (ADCS), communications, command & data
   handling (C&DH), payload.
3. Because the orbit sets the environment and the geometry. Examples:
   a LEO orbit means ~15 eclipses a day, so the battery is sized for
   eclipse power; a GEO or deep-space orbit means a long radio distance,
   so the antenna and transmitter must be bigger; a sun-synchronous
   orbit means consistent lighting for a camera; LEO means atmospheric
   drag and atomic oxygen, so you carry propellant to re-boost.
4. r₁ = 6,871 km, r₂ = 26,371 km, a = 16,621 km.
5. a³/μ = (16,621)³ / 398,600 ≈ 4.5916 × 10¹² / 398,600 ≈ 1.152 × 10⁷ s²;
   √ ≈ 3,394 s; × π ≈ 10,663 s ≈ **2.96 hours** (about 3 h).

</details>
