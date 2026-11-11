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

## ELI5 box first (added 2026-11-09)

The student confirmed the goal is to be taught the concepts like they're
5, not just handed organized notes. **Page 2 of every lecture PDF opens
with a boxed "Like you're 5" paragraph**: plain words, a physical
picture (playground, hula hoop, sunscreen, doorknob zap), no Greek
letters, no numbers, before any technical content. If the box doesn't
make sense on its own, the rest of the page can't. The S3-L1 PDF has the
first one; earlier PDFs carry their analogies inside the teach section
rather than up front.

## The real goal (stated 2026-11-09): hold a conversation

The student's goal is not a grade: it's to understand everything and
**hold their own in a conversation** about these topics. That makes
*explaining out loud* the primary practice, not recall. Two standing
steps, in addition to everything above:

1. **60-second explain, every lecture.** After the 3-line summary, the
   student explains the lecture to Claude in their own words, no notes
   open, as if a friend asked "what did you learn?" Claude replies like
   a curious friend (follow-ups, "wait, why?"), then says honestly where
   it got fuzzy. Fuzzy → fix before moving on. Log each one in the
   OUTLINE session log with a one-line read (solid / fuzzy on X).
2. **Conversation test, every section.** When a section ends, Claude
   plays a space-curious person at a party and asks five questions
   (mix of easy and probing). Honest grade; shaky items go back into
   the review cycle and the question bank.

Each lecture PDF's page 2 ELI5 box doubles as the "say it out loud"
version of the material.

## Actual per-lecture order (confirmed by the student 2026-11-09)

1. Student watches the video (no notes during).
2. Student sends the Udemy transcript + slide screenshots.
3. Claude returns the PDF: spread · teach page (ELI5 box first) ·
   vocabulary · page 4 "Say it out loud".
4. Student writes the spread in the notebook **from the PDF**. Two
   safeguards Claude should keep repeating: cover the PDF's left page
   and draw first, then fix; and do the 3-line summary with the PDF
   closed.
5. Student sends a photo of the spread + the 60-second explanation.
   Claude replies as a curious friend, gives an honest read, and fills
   page 4's feedback box.

## PDF page 1 is now full size (changed 2026-11-09)

The small-notebook mock-up (two 3.6-inch pages plus a side card) was
too small to read. **Page 1 now shows the two notebook pages at half a
landscape sheet each** (about 5 × 7.3 in, 12 px text), nothing else on
the page. The line budget still applies to the content; the rendering
just got bigger. Watch for SVG text clipping at the bottom of the
drawing: give the viewBox room and check the rasterized page before
sending. Applies to every PDF from S3-L1 on.

## Drawings must be pencil-ready (added 2026-11-09)

The student draws in pencil only (highlighters are for the +1 review
pass, not for drawing). So **no meaning may be carried by color in a
page-1 drawing.** Encode everything with what a pencil can do:
thin vs thick line, solid vs dashed vs dotted, filled vs hollow dot,
shaded vs clear, and a text label on every line. Grayscale only.
A **"PENCIL KEY" box sits under the drawing** (HTML, not inside the SVG,
so it wraps) spelling out the code. Lay panels out vertically with
deliberate margins; check the rasterized page for overlapping labels
and for the summary box being pushed off the page before sending.
Re-issued S3-L1 (v3) and S3-L3 (v2) this way.

## Review kits (added 2026-11-09)

When the student pauses to review, the deliverable is a **Teach-It-Back
Kit** PDF in `review/`: (1) a one-paragraph through-line tying the
sections into one story, (2) each concept re-taught at 5th-grade level
with a bold "SAY:" line and a napkin-drawing prompt, (3) a timed
teach-back script skeleton (key line + drawing + hand-off per block),
(4) a quiz we own, mixing fact / explain-why / "a friend asks" items,
with answers keyed back to the scene to review, (5) a rehearsal plan
(with notes → cue card only → nothing + record) and a one-index-card
cue card. The student then sends the run-3 recording or transcript and
Claude grades it as the friend would hear it.

## Name it, then explain it (added 2026-11-10)

The student saw a Google answer naming the five fixed orbital parameters
as the "Classical Keplerian Elements" and realized the official names
had never been given alongside the analogies. Standing rule: **official
term in bold first, then also-called names, then the plain meaning and
the analogy.** The app's Terms tab (115 entries) is the living glossary;
every new lecture adds its official vocabulary there and in the lecture
PDF's vocabulary page. The depth target is "could read a real article or
NASA page and recognize every term," not just "can follow the course."

## Terms pass, not a rewrite (2026-11-11)

When the student feels their notes are "not the best" after learning
official terminology: **do not rewrite the notebook** (copying). Do a
terms pass per spread: (1) PDFs and app closed, guess the official name
for each cue in light pencil; (2) check against the Terms tab, correct
in dark pencil, keep the wrong guess; (3) add new words to the word
bank with page numbers. ~35 terms across the six S1-S3 spreads. Then
deepen with retrieval (quiz "due"), naming, and explaining (Teach tab
run 2, then send a run for grading). No new content until the Section 1
talk is clean.

## Final notebook map (2026-11-11)

The student asked for the whole notebook laid out once. `Notebook-Map-v1.pdf`
is the authority. Front: inside cover = tracker + highlighter key; p1-2
index; p3-4 equations & key numbers; p5 abbreviation key; p6 onward =
lecture spreads in course order with a from-memory **section map page**
after each section's last lecture. Back (counted from the last page):
question bank = last 14 pages (Q left / A facing right); word bank =
the 12 pages before that, by section and lecture, EVERY word the
lectures used (student's instruction 2026-11-11; "only new words" is
retired) — `Word-Bank-COMPLETE-S1-S3-v1.pdf` has the 161 S1-S3 lines; talk cards (cue cards per section
talk) = the 2 pages before that; 2-page buffer before the back section.
~95 pages total (`Notebook-Map-v2.pdf`). Every page numbered in pencil
first; sticky tabs at 30, 28 and 14 from the end. Shrink order if the notebook is short: question
bank → 10, word bank → 8, lectures take the rest.

## Complete glossary (2026-11-11)

Student's instruction: the word bank must hold **every** word the
lectures used, and every word needs a full definition they can reach.
Deliverables: `Word-Bank-COMPLETE-S1-S3-v1.pdf` (161 one-line entries
to copy into the back pages) and `Glossary-COMPLETE-S1-S3-v2.pdf`
(the same 161 terms with full definitions and analogies, same order,
8 pages, read on screen). The app's Terms tab was brought up to 178
entries so it matches. **For every new lecture from here on:** the
lecture PDF's vocabulary page feeds (1) new lines appended to the
word-bank sheet, (2) new entries in the glossary PDF, and (3) new
`TERMS` entries in the app, all three in the same pass.

## Three layers, always (2026-11-11)

The student's standard is now explicit: for every concept, (1) the
simple picture ("like I'm 5"), (2) the official name and what else it's
called, and (3) the mechanism with real, checkable numbers ("how does
it actually stay up?"). The app's Learn tab carries all three per scene
and a header toggle (🧒 Like I'm 5 / 🛠 Engineer) sets which comes
first; Terms shows the plain first sentence in 🧒 mode and the full
entry in 🛠 mode. Every lecture PDF from here on gets a "How it actually
works" block with worked numbers on page 2, and the same content goes
into the scene's `deep` rows in the app.

## Engineer level → notebook routing (2026-11-11)

Engineer-level content never goes on the full lecture spreads. It is
routed to reserved pages via a "copy into notes" sheet
(`Copy-Into-Notes-Engineer-S1-S3-v1.pdf`): (A) formulas + worked
numbers → equations & key numbers page; (B) one mechanism sentence per
scene → the section map pages; (C) new terms → word bank; (D) "but
how?" Q/A cards → question bank. Every future lecture PDF gets the same
four-way routing block.
