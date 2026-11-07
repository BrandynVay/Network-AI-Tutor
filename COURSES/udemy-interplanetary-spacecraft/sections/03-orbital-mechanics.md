# Section 3 — Orbital Mechanics

3 lectures, ~34 min. The math-heaviest section. Pause often.

## Before you watch

**Draw this first:** an ellipse with Earth at one *focus* (not the
center). Label the closest point **perigee** and the farthest
**apogee**. Draw the long axis and label half of it `a` (semi-major
axis). Now draw a second picture: a small circle, a big circle, and half
an ellipse connecting them — that's a **Hohmann transfer**. Mark the two
burns: one at the bottom to leave the small circle, one at the top to
circularize.

```
   Hohmann transfer (not to scale)

                 .  -  .   <- burn 2 at apogee: speed up to circular
            .               .
          .     - - - - -     .    outer circle r2
         .    .           .    .
         .   .   (Earth)   .   .   transfer ellipse, a = (r1+r2)/2
         .    .           .    .
          .     - - - - -     .    inner circle r1
            .               .
                 '  -  '   <- burn 1 at perigee: speed up to leave circle
```

**The intuition that makes all of it click:** an orbit is falling and
missing. Throw a ball sideways fast enough that the ground curves away
as fast as the ball falls, and it never lands. Faster = higher, up to
the point where it never comes back (escape).

**Kepler's three laws, in plain English:**
1. Orbits are ellipses with the central body at one focus.
2. The line to the body sweeps equal areas in equal times — so you move
   **fastest at perigee, slowest at apogee**.
3. T² ∝ a³ — bigger orbits take disproportionately longer. (This is
   the T = 2π√(a³/μ) you used in Section 1.)

**Three speeds to be able to write from memory** (μ_Earth = 398,600 km³/s²):
- Circular velocity: v = √(μ / r). LEO (r ≈ 6,771 km): ≈ 7.67 km/s.
- Escape velocity: v = √(2μ / r). At LEO: ≈ 10.85 km/s (√2 × circular).
- Anywhere on any orbit (**vis-viva**): v² = μ (2/r − 1/a). This one
  equation gives both of the above (circular: a = r; escape: a → ∞).

**Orbital elements — the six numbers that pin down an orbit:**
`a` size · `e` eccentricity (0 circle, 0–1 ellipse) · `i` inclination
(tilt vs. equator) · `Ω` RAAN (where the tilted plane crosses the
equator) · `ω` argument of perigee (where perigee sits within the plane)
· `ν` true anomaly (where the spacecraft is *right now*). Size, shape,
three angles for orientation, one for position.

**Orbit families you'll hear named:**
- **LEO** (~200–2,000 km): ISS, Starlink, imaging. 90-min periods.
- **MEO** (~2,000–35,000 km): GPS at 20,200 km, 12-h period.
- **GEO** (35,786 km, equatorial): 24-h period, hangs over one spot.
- **Sun-synchronous (SSO)**: a near-polar LEO whose plane precesses to
  keep the same local sun time — cameras get consistent lighting.
- **Molniya**: highly elliptical, 12-h, hangs over high latitudes.

**Going interplanetary:** the trick is **patched conics** — treat the
trajectory as Earth-centered until you leave Earth's *sphere of
influence*, then Sun-centered, then Mars-centered. A Hohmann to Mars
takes ~8.5 months, and the geometry only lines up every **~26 months**
(the launch window / synodic period). **C3** is the launch energy
(excess of v² over escape); a Mars mission needs C3 ≈ 10–15 km²/s².

## Your notes (brain-dump, video closed)

> _write here_

## Transcript

<details><summary>Transcript</summary>

_paste here_

</details>

## Recall quiz

1. Where in an elliptical orbit is the spacecraft moving fastest, and
   which Kepler law says so?
2. Compute circular velocity at 400 km altitude. (Earth radius 6,371 km,
   μ = 398,600 km³/s².)
3. Using vis-viva, what's the speed at perigee of an orbit with
   perigee radius 6,771 km and apogee radius 42,157 km?
4. Why does GEO have to be at 35,786 km and not somewhere else?
5. Why is a Hohmann transfer two burns, and in which direction is each?
6. Why can you only launch to Mars roughly every 26 months?

<details><summary>Answers</summary>

1. Perigee — Kepler's 2nd law (equal areas in equal times: close to the
   body the sweep line is short, so it must move fast to sweep the same
   area).
2. r = 6,771 km. v = √(398,600 / 6,771) = √58.87 ≈ **7.67 km/s**.
3. a = (6,771 + 42,157)/2 = 24,464 km. v² = 398,600 × (2/6,771 −
   1/24,464) = 398,600 × (2.9538×10⁻⁴ − 4.0876×10⁻⁵) = 398,600 ×
   2.5450×10⁻⁴ ≈ 101.4; v ≈ **10.07 km/s**. (That's the GTO perigee
   speed — about 2.4 km/s more than circular LEO, which is burn 1 of a
   LEO→GEO Hohmann.)
4. Kepler's 3rd law: period depends only on `a`. Exactly one radius
   gives a 23 h 56 min (sidereal day) period, so the satellite keeps
   pace with Earth's rotation. Add zero inclination and it hangs over
   one spot.
5. Burn 1 (prograde, along the direction of motion) at the inner orbit
   raises apogee out to the outer orbit's radius. Burn 2 (also prograde)
   at apogee raises perigee to match, making it circular. Both speed you
   up for an outward transfer; both would be retrograde coming inward.
6. Earth and Mars orbit the Sun at different rates; the relative
   geometry a Hohmann needs (Mars ~44° ahead of Earth at launch) recurs
   once per *synodic period*, ≈ 780 days ≈ 26 months.

</details>
