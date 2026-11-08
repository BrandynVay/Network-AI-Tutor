# How to take notes on this course (and actually keep it)

The research on study techniques is unusually clear: **retrieval
practice** (testing yourself) and **spacing** (coming back later) are
the high-value habits. Rereading, highlighting, and transcribing are
low-value — they feel productive because the material is right in front
of you, which is exactly why they don't build memory. Everything below
is built on that.

## During a lecture

1. **Draw before the instructor does.** Every section here is a
   picture: an orbit, a rocket losing mass, a radio link, a spinning
   body, a power chain. When a diagram is about to appear, pause and
   sketch your own guess first. Your bad drawing is the note. The
   instructor's slide is not.
2. **Rework every equation on paper.** When an equation appears, pause,
   cover the screen, and re-plug the numbers yourself. "Quiz 1: Time of
   flight" is a calculation. You pass it by having done one.
3. **Write sparse.** Keywords, questions, sketches. If you're writing
   full sentences, you're transcribing and not thinking.

## After a lecture (same day)

4. **Brain-dump from memory** into the section file's *Your notes*
   block with the video closed. Whatever you can't recall is the study
   list — that's the valuable output, not the notes themselves.
5. **Grab the transcript.** Udemy's player has a **Transcript** button
   (bottom-right of the video, by the speed/captions controls). Copy it
   and paste it into the section file's transcript block. This is the
   replacement for "an AI watching my screen" — it's the actual words,
   which is better than a screenshot of them.
6. **Hand it to Claude.** Claude checks your brain-dump against the
   transcript, draws the diagram properly, grades the quiz, and feeds
   anything you missed into the primer.

## Later

7. **Redo the quizzes cold** a few days after each section, then again
   after the course ends. Five minutes each. This is where it sticks.

## Tools

- **A plain text file you own** (these section files) beats Udemy's
  Notes tab, whose export is poor.
- **Claude in Chrome** (paid plan, Chrome only) can read the Udemy page
  on demand, transcript panel included, if copy-pasting gets old. Nothing
  passively monitors your screen, and you wouldn't want it to: a note
  you didn't write and never retrieve from is a PDF you own, not
  knowledge.

## Paper notebook layout (added 2026-11-07, for the new notebook)

Set the notebook up once, before lecture 1:

```
 inside cover      REVIEW TRACKER (one row per section, tick as you go)
                   Sec | watched | +1 day | +3 | +7 | +14 | +30
 page 1-2          INDEX: section / lecture -> page number
 page 3-4          EQUATIONS & KEY NUMBERS: every formula, boxed, with units and
                   one worked number. Grows all course. Nothing else goes here.
 last 10 pages     QUESTION BANK (work from the back): every quiz question
                   you got wrong or every "?" you wrote, one per line,
                   answer on the facing page. This is your flashcard deck.
```

Every lecture gets a **two-page spread**:

```
 LEFT PAGE: DRAW                       RIGHT PAGE: CORNELL
 +----------------------------+        +--------+---------------------+
 | Sec 3 / Lec 2   2026-11-08 |        | CUES   | NOTES               |
 |                            |        | (1/3)  | (2/3)               |
 |  your sketch, made BEFORE  |        |        |                     |
 |  the instructor shows the  |        | turn   | keywords, arrows,   |
 |  diagram. Big. Labeled.    |        | every  | boxed equations.    |
 |  Redraw it in a different  |        | note   | No full sentences.  |
 |  color after, correcting.  |        | into a | "?" in margin for   |
 |                            |        | QUESTION| anything you didn't |
 |                            |        | you can| follow -> goes to   |
 |  worked example of the     |        | later  | question bank.      |
 |  lecture's equation, by    |        | answer |                     |
 |  hand, with units          |        | from   |                     |
 |                            |        | memory |                     |
 +----------------------------+        +--------+---------------------+
                                       | SUMMARY (5 lines, written  |
                                       | with the video CLOSED)     |
                                       +----------------------------+
```

Rules for the spread:
- **Left page first.** Pause when a diagram is coming, draw your guess.
  Then draw the corrected version next to it. Keeping the wrong guess
  is the point: the correction is what you'll remember.
- **Cue column = questions, not labels.** "What sets GEO altitude?" not
  "GEO." A cue you can't answer later is a flashcard.
- **Summary last, from memory.** Close the video, five lines. If you
  can't, you don't have it yet, and that's the useful signal.
- **Box every equation twice** (if the lecture has one; many won't): once in the notes, once on the
  equation sheet with a worked number.

Retention schedule (this is the part most people skip, and it's the
whole game):
- **+1 day:** cover the notes column, answer the cues out loud. Tick.
- **+3, +7, +14, +30 days:** same, 5 minutes per section. Tick the
  tracker. Anything missed twice goes to the question bank.
- **End of each week:** on a blank page, redraw the whole course map so
  far from memory (mission -> environment -> orbit -> propulsion ->
  comms -> ADCS -> power), one line per box. Compare to the index.
- **Every few days, give Claude a photo of a spread** or type the cue
  questions in: Claude checks answers, catches wrong facts, and writes
  harder follow-ups for the question bank.

## Highlighter key (pencil + highlighters, "aesthetic but functional")

Printable version with a mock finished page: `SpaceX-Mission-Notebook.pdf`
in this folder (6 pages: cover, setup, filled example spread, blank
template, highlighter style page, review schedule).

- **Yellow** = term/definition to know · **Pink** = equation (boxed) ·
  **Blue** = question / "?" / ask Claude · **Green** = the "aha" line ·
  **Orange** = a mistake I made → copy to question bank.
- Write the whole lecture in pencil first. Light pencil = guess, dark
  pencil = corrected; don't erase the guess.
- **Highlight on the +1 day review, not while writing**, and only what
  you could not recall with the notes covered. The highlights then mark
  your gaps, which is what makes them functional instead of decorative.
- Keep: title banner per lecture, one tiny doodle icon per topic, a
  "3 takeaways" box. Skip: lettering practice, multiple fonts,
  re-copying neat versions, decorating during the video.

## Feedback format (added 2026-11-07)

The student wants every piece of feedback on their notes **as a PDF they
can look at**, not as chat text: a rebuilt version of their spread
(drawn left page + Cornell right page) plus a page of what was right /
what to sharpen / question-bank cards. Build it the same way as
`SpaceX-Mission-Notebook.pdf` (HTML → Playwright PDF, letter landscape)
and save it under `feedback/` named `S<section>-<topic>.pdf`.

## Small notebook (confirmed 2026-11-07)

The student's notebook is a small format (roughly A5, ~22 ruled lines
a page, exact count not yet confirmed). See
`SpaceX-Notebook-SMALL-addendum.pdf`. Same method, smaller budget:

- One lecture = one spread still. **Summary shrinks to 3 lines and
  moves to the bottom of the LEFT (draw) page**, under the 3 takeaways,
  so the right page is only cues + notes.
- Line budget per lecture: header 1 · drawing ~11 · takeaways 3 ·
  summary 3 · cues 4-6 · keyword notes 8-10. If it doesn't fit, start a
  second spread for the same lecture; never shrink the handwriting.
- Reserved pages: inside cover tracker · p1 index · p2 equations & key
  numbers · p3 abbreviation + highlighter key · last 6 pages question
  bank.
- Feedback PDFs from now on show the spread at the small page's
  proportions with this line budget; teaching detail, fact checks and
  Q-bank cards go on a separate screen-only page. One drawing per
  lecture on paper; extra diagrams live in the PDF.

## Vocabulary page (added 2026-11-07)

The student flagged that the instructor uses terms as if already known.
**Every lecture PDF gets a vocabulary page**: each term the lecture
uses, one plain-English line, one everyday analogy in italics, and a
note where the instructor used a word loosely (e.g. "corrosion" for UV
bond-breaking). It's read on screen, not copied. On the +1 day review
the student explains three of them aloud without looking.

**Strengthened 2026-11-07 at the student's request:** the vocabulary
page covers *every* term that appears anywhere in the PDF, including
words Claude itself introduces in the notes column or analogies
(Δv, prograde, capture burn, "commitment ladder", mission names).
Assume no prior vocabulary. The two earlier PDFs (S1 satellites, S1-L3
spacecraft types) were backfilled with vocabulary pages the same day.
**Nothing from a vocabulary page goes into the paper notebook** — the
student's pages are full and that's fine; the vocab is a screen-side
reference. **Paper version (decided 2026-11-07):** the student has no free
pages after Section 1, so the notebook gets a **word bank in the back**:
the 4 pages before the 6-page question bank. One line per word:
`word · page-it-appears-on · 3-5 word meaning`, grouped by section.
Only words that were actually new to the student (5-8 per lecture, not
the full PDF list). Reviewed by covering the meaning column on each
+1/+3/+7 pass; missed twice → question card; nailed 3× → tick and skip.
Layout: `Word-Bank-layout.pdf`.

Working pipeline now confirmed: the student pastes the Udemy transcript
plus slide screenshots → Claude returns one PDF: (1) the spread at the
small-page budget, (2) teach + fact-check + question-bank cards, (3)
vocabulary.

## Names & missions (added 2026-11-08)

The student doesn't know the proper names (Laika, Hubble, Voyager…)
that Claude uses as examples. `Whos-Who-names-and-missions.pdf` is the
running reference: every mission, spacecraft, place and agency named so
far, one line each, tagged by category. **Append to it whenever a new
name is used in a PDF**, and in each lecture PDF's vocabulary page
include every proper name used, not just technical terms. Never use a
name as an example without it being defined somewhere the student can
reach.
