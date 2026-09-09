# Network-AI-Tutor

A personal, AI-driven study system for passing IT certifications —
built and run by Claude as a dedicated tutor, not a generic assistant.
It exists to prepare one student for a sequence of exams, one at a time:

**CompTIA Network+ → CompTIA Security+ → Cisco CCNA**

Everything here — the study plan, the reference material, the quizzes,
the companion app — is generated and maintained by Claude across
sessions, following the rules in [`CLAUDE.md`](./CLAUDE.md). This file
is the human-facing overview; `CLAUDE.md` is the operating manual Claude
actually follows.

## Why this exists

Passing a cert exam takes more than reading a book for 90 days. This
project exists to make sure specific things actually happen instead of
being good intentions:

- **Nothing requires leaving the project.** No "go Google this" — every
  explanation, quiz, and reference chapter is written to actually teach
  the material from scratch.
- **Progress is measured, not assumed.** A mastery gate blocks new
  material until quiz/flashcard accuracy clears 80% in that domain.
- **Old material doesn't quietly decay.** Spaced repetition is baked
  into the study schedule itself, not left to "review sometime."
- **Exam-day readiness gets practiced directly.** Full-length, timed
  practice exams are scheduled at fixed checkpoints, not assumed to
  follow automatically from knowing the material.
- **Hands-on practice uses real gear.** Labs are mapped to the
  student's actual physical networking equipment, not just diagrams.

The full rule set for how this is enforced session to session lives in
`CLAUDE.md` § Exam readiness.

## The companion app

**[Network+ Ops Console](https://claude.ai/code/artifact/55349816-2d86-4f3d-acd1-f7781164f2f9)**
— a phone-friendly web app that mirrors this project, so studying isn't
limited to sitting at a computer with Claude open.

| Tab | What it does |
|---|---|
| **Overview** | Exam countdown and a live per-domain confidence breakdown, weighted by the real exam blueprint. |
| **Diagnostic** | The 20-question diagnostic quiz, answered in-app and graded by Claude. |
| **Reference** | The full study guide, rendered from `CERTS/<track>/REFERENCE/`, readable from a phone. |
| **Flashcards** | Quick flip-card review, plus an active-recall "quiz mode" toggle (type an answer or pick from multiple choice) for one-handed use — waiting in line, between errands, wherever. |
| **90-Day Path** | A grid of where the student is in the schedule. |

At the very top, a **certification-track switcher** shows the whole
roadmap — Network+ (active) → Security+ → CCNA — with locked tracks
marked as such until it's their turn. A **dark-mode toggle** in the
header overrides the system theme and remembers the choice.

The app has its own live database, namespaced per track
(`tracks/<trackId>/...`) so Security+ and CCNA can plug in later without
touching Network+'s data. See `CLAUDE.md` § Companion app for the schema.

## Repository structure

```
CLAUDE.md                        Claude's operating rules — start here
                                  for how any of this actually works
README.md                        this file

CERTS/
  network-plus/                  the active track
    STUDENT_PROFILE.md           durable memory: interview, exam facts,
                                  diagnostic results, logistics, logs
    OUTLINE.md                   the full study plan (written once the
                                  diagnostic is graded)
    REFERENCE/                   standing study guide, one file per domain
    Day 01/ … Day 90/            one folder per session, generated
                                  just-in-time as each day happens

  security-plus/STATUS.md        not started — placeholder only
  ccna/STATUS.md                 not started — placeholder only
```

Two things worth knowing about this layout:

- **Day folders are chronological; `REFERENCE/` is topical.** Day
  folders are "what we covered on day 12." `REFERENCE/` is "everything
  known about VLANs," regardless of which day taught it. Use `REFERENCE/`
  to look something up; the day folders exist as a record of the actual
  session-by-session teaching.
- **Nothing is scaffolded speculatively.** Day folders past today, and
  the entirety of the Security+/CCNA tracks, don't hold real content
  until their turn actually comes. This project builds itself
  incrementally, not all at once up front.

## How the study plan works, briefly

1. **Interview** — background, time budget, learning style, lab access.
2. **Diagnostic quiz** — 20 questions across all 5 exam domains, to find
   real weak spots rather than guessing.
3. **Outline** — a full-length plan weighted toward those weak spots,
   with spaced-repetition review points, practice exam days, and a
   final no-new-material taper built in from the start.
4. **Daily sessions** — generated one at a time, adjusted as the student's
   actual performance reveals more than the original diagnostic could.
5. **Practice exams** at roughly the ⅓, ⅔, and ~90% marks of the plan —
   full-length, timed, blueprint-weighted — with a prompt to book the
   real exam once the ⅔ checkpoint is logged.

Full mechanics: `CLAUDE.md` §§ Exam readiness, How a daily session works.

## Current status

- [x] Project initialized, student interviewed, lab gear inventoried
- [x] Diagnostic quiz written and administered (20 questions, in-app)
- [x] Reference guide started — Networking Concepts fully written; four
      domains remaining
- [x] Companion app built: dashboard, diagnostic, reference, flashcards
      (flip + quiz mode), 90-day tracker, track switcher, dark mode
- [x] Exam-readiness methodology defined (mastery gate, spaced
      repetition, practice exams, taper, falling-behind policy)
- [x] Multi-certification structure in place for Security+ and CCNA
- [ ] **Diagnostic quiz answers** — waiting on the student
- [ ] `OUTLINE.md` and Day 01 — blocked on the diagnostic being graded

The live, authoritative checklist is `CLAUDE.md` § Project status —
this section is a snapshot for anyone skimming the repo on GitHub.

## For Claude, picking this back up

Read `CLAUDE.md` first, in full, before doing anything else. It is the
actual source of truth for how this project runs; this README describes
it for a human reader but is not itself a set of operating instructions.
