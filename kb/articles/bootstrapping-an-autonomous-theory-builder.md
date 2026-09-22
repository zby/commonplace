---
description: "Rewrite plan for the bootstrap supplement: intent, end state, constraints, inputs, and open choices for a compact article claiming that starting from a working human-agent system is what makes the automation bet tractable"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/commonplace-studies-conjectural-learning-through-retained-theories.md
  - kb/notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/system-use-selects-theory-fit-without-a-fixed-oracle.md
  - kb/notes/definitions/theory-builder.md
  - kb/notes/definitions/autonomous-theory-builder.md
  - kb/notes/definitions/reflective-theory-builder.md
  - kb/notes/definitions/externally-tested-theory-builder.md
  - kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md
  - kb/notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md
  - kb/notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md
  - kb/notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md
  - kb/notes/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md
  - kb/notes/evidence/commonplace-revision-used-theory-guided-computational-search.md
  - kb/notes/evidence/commonplace-as-a-reflective-system.md
---

# Bootstrapping an Autonomous Theory Builder

> **Rewrite plan, not the article.** The previous draft of this supplement is
> superseded and stays in git history at commit `14c634dd`. This page holds
> the plan for its replacement, in the compact form of
> [Conjectural Learning with Today's LLMs](./conjectural-learning-with-fixed-models.md).
> Comments on the plan are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

## Purpose

The lead article bets that a fully automated conjectural learner can be built
with today's fixed-weight LLMs. This supplement exists to say how we get
there from Commonplace as it is, and to make one claim the lead only points
at: **starting from a system that already works, with people supplying the
functions not yet automated, is what makes the bet tractable.** A researcher
who has read the lead should finish this article knowing why we start where
we start, what a step toward automation is, how we tell that a step was
taken, and when we would stop.

## End state

A draft of about 1,200 to 1,600 words at this path, bet first, that a
technical reader with no KB context can restate as four claims:

1. **The seed.** An LLM-interpreted methodology is a delta over pretrained
   competence; it directs what it need not encode. Earlier realizations of
   recursive self-improvement had to encode that competence executably, and
   the ones that ran stayed in bounded domains. This difference is shared
   with every LLM-era attempt and does not by itself distinguish us.
2. **The start.** A machinery improvement pays through the later episodes
   that reuse it, and the bootstrap is the running system itself. A working
   system supplies the episode stream from the first day and is the initial
   selection environment where no fixed oracle exists. Sustaining human
   supply of the unautomated functions requires a system people want to
   use; Commonplace is one, because its operators build and use the
   knowledge base for their own work. This is what distinguishes the
   arrangement from a benchmark plus a search loop.
3. **The program.** Internal roles move to computation one bounded class at
   a time. Each transfer is tested twice: does computation now make the
   decision, and does the system learn to revise the machinery that makes
   it. The second test is reflection: the builder holds a theory of its own
   machinery, connected in both directions. Readiness conditions say when a
   class may move; stop or redirect conditions say what would end the
   program.
4. **The price.** Earlier realizations certified each change by proof or by
   reward rate. Here the interpreter's judgments are hidden, the working
   system works partly because of its people, and every human contribution
   is recorded rather than credited to computation. Transfer leaves people
   the decisions hardest to warrant, so the residue must be named, not
   hidden.

The draft carries the draft banner, links each claim to the note that
develops it, links external texts as themselves, lists its source notes, and
passes `commonplace-validate`. The articles README entry is rewritten to
match.

## Constraints

- **Bet first.** State the claim in the first hundred words. No case, no
  definition walk-through before it. Concrete detail enters only where it
  makes a mechanism easier to see, and says what it establishes.
- **Divergence claims stay divergent.** Claims 2 and 3 are the program's
  bets. State each with its refutation condition; do not narrow them to
  their sources in review.
- **Ordinary words.** "Precise description of the work" or "methodology",
  never "ontology". "Popper's account of science" and "a research
  community", never "how science works". Define *theory builder*,
  *autonomous*, and *reflective* where first needed, in one sentence each,
  linking the definition notes.
- **Human contributions are recorded, not credited.** Any episode cited as
  evidence names who decided what.
- **The second bet, code as well as prose, is in by default and brief.**
  Operator direction of 2026-09-21: it is one of the program's bets, stated
  comparatively, that the loop is easier when the builder also writes code
  that operates its knowledge; not that prose alone would fail. One
  paragraph in the machinery part of claim 3, resting on the
  missing-procedures note. The operator may strike it before drafting.
- **Length.** Under 1,600 words. What does not fit goes back to a note, not
  into a longer article.

## Inputs

- The superseded draft at `14c634dd`: its two-kinds-of-transfer distinction,
  readiness conditions, stop conditions, and the Markdown-checks trial are
  reusable material, not a structure to preserve.
- The research companion's section on the research program and development
  path, which already states claims 1, 2, and 4 in note form.
- The machinery-investment, bootstrap-compatibility, and system-use notes
  for claim 2; the three builder definitions and the warrant note for
  claim 3; the residue and warranted-transfer notes for claim 4.
- The two evidence notes for any episode the article cites.
- The lead article, for the promises this supplement must keep: starting
  from Commonplace, transferring roles one class at a time, and covering
  reflection.

## Choices left to the writer

- Whether to keep the Markdown-checks trial as the one concrete example, or
  to use an episode from the evidence notes instead.
- How much of the readiness and stop conditions to carry as lists versus
  prose.
- Section titles and order after the opening bet.

## Verification and stop

Validate with `commonplace-validate`. Then check the end-state test by
reading the draft cold: can the four claims be restated from it? If a claim
needs support no note supplies, stop and write the note first; the article
is distilled from the notes. If the second bet cannot be stated in one
paragraph without overclaiming, leave it out and say so in the commit.
