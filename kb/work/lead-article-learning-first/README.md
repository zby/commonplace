# Lead article: learning first, then the automation bet

Posed by the operator on 2026-09-21, in a session that had just replaced the
lead article's exporter case with the docs-only case (commit `b36a185c`).

## Goal

Restructure the lead article,
[Conjectural Learning with Fixed Models](../../articles/conjectural-learning-with-fixed-models.md),
around this argument:

1. **The learning.** Conjectural learning is ordinary: everyday learning from
   mistakes, science as the large familiar case, the docs-only case as the
   worked example. Details and boundary cases come later or stay in the
   definition note.
2. **The bet.** We believe the whole loop can be run by computation. A
   sufficiently precise description of the work lets language models fill
   every internal role. This is why the definitions get so much care.
3. **Code as well as prose.** A second bet, stated briefly and not argued at
   length: the loop is easier when the theory builder also builds code that
   operates its knowledge, as science relies on mathematical notation and
   people rely on procedural memory. The claim is comparative. It does not
   say that prose alone would fail.
4. **The Bitter Lesson.** Full automation is what makes retained theories a
   learned product and not hand-built knowledge.

The operator's diagnosis of the current lead: it goes in wrong directions. It
reads as a defence of the definition, and the program's main bet first appears
as a bullet in the ninth section.

## What closes the workshop

The operator accepts a restructured lead article in `kb/articles/`, the notes
that must carry its new claims are updated first (the article is distilled
from the notes), and the sections removed from the lead have a recorded
destination (a supplement, a note, or deletion). Then delete this directory.

## Constraints a later session cannot reconstruct

- **These are divergence claims. Defend them; do not narrow them in review.**
  (a) The loop can be fully automated. (b) The loop is cheaper and more
  reliable when the builder also builds code. (c) The arrangement is
  compatible with the Bitter Lesson. State each as a bet with its refutation condition. The current
  lead's low content is partly the residue of hedging every claim.
- **One agreed weakening.** Automation is necessary for Bitter Lesson
  compatibility, not sufficient. Whether search and assessment over written
  theories scales, and whether weights do the same job more cheaply, stay
  empirical. The operator's first phrasing was "and thus Bitter Lesson
  compatible"; the draft argues the necessary-condition version and the
  operator has not yet ruled on it.
- **Outward wording.** Write "precise definitions" or "a precise description
  of the work", not "ontologies". The word invites the Cyc and expert-system
  reading, which is the case the Bitter Lesson is about. The article must draw
  that distinction itself.
- **The precise description is of the learning process, not of each domain.**
  A person supplying a vocabulary for each new area is a failure condition in
  [the bootstrap note](../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).
- **Science.** Write "Popper's account of science" and "a research
  community", not "how science works" or "science". The account is contested
  as description, and the definition needs a declared boundary.
- **Do not map the amoeba onto gradient descent or score-selected variants.**
  The article leaves private criticism inside an opaque model open.
- **Agent memory and automated-science systems** may be named only after
  checking what the KB's reviews and ingests support. The article must not
  classify them as learning or not learning in its sense.
- **The amoeba passage** (Popper 1968, p. 371, present in the snapshot) is not
  a retained quote. Ground it with `cp-skill-ground` before quoting it. The
  "die in their stead" sentence is already retained.
- **Lead length.** The lead gets a few sentences on automated science. A full
  comparison is a possible later supplement and is not part of this workshop.

## Deferred, outside this workshop

Five files still use the exporter example: the testing, bootstrap, and
software-house articles, and the sample-efficiency and missing-procedures
notes. The operator deferred that sweep.

## Files

- [front-half-draft.md](./front-half-draft.md) — draft of the new front half
  (parts 1–4), followed by notes on what the draft still needs and on which
  current sections it displaces.
