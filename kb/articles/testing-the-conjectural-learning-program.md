---
description: "Rewrite plan for the testing supplement: intent, end state, constraints, inputs, and open choices for a compact pre-registration that a lab could run, with the three adopted hypotheses quoted as adopted"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/conjectural-learning.md
  - kb/notes/definitions/theory-builder.md
  - kb/notes/definitions/externally-tested-theory-builder.md
  - kb/notes/definitions/reflective-theory-builder.md
  - kb/notes/definitions/autonomous-theory-builder.md
  - kb/notes/definitions/actionable-methodology.md
  - kb/notes/definitions/operative-change.md
  - kb/notes/commonplace-studies-conjectural-learning-through-retained-theories.md
  - kb/notes/a-complete-theory-path-does-not-establish-improved-capacity.md
  - kb/notes/a-claim-without-external-assessment-carries-three-obligations.md
  - kb/notes/retained-theory-intervention-isolates-one-explicit-surface.md
  - kb/notes/retained-theories-may-improve-sample-efficiency.md
  - kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md
  - kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/notes/evidence/commonplace-as-a-reflective-system.md
---

# Testing the conjectural-learning program

> **Rewrite plan, not the article.** The previous draft of this supplement is
> superseded and stays in git history at commit `2da543f0`. This page holds
> the plan for its replacement, in the compact form of
> [Conjectural Learning with Today's LLMs](./conjectural-learning-with-fixed-models.md).
> Comments on the plan are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

## Purpose

The lead article ends on a research question and says we think the answer
is yes. This supplement exists to make that answer refutable by someone who
is not us. A researcher who has read the lead should finish this article
knowing exactly what is claimed, what observation would refute each claim,
what has to come from outside the system for the result to count, and what
the first experiment is, specified closely enough that a lab could run it on
its own harness and report a result we would have to accept.

## End state

A draft of about 1,200 to 1,600 words at this path, in the form of a
pre-registration, that a technical reader with no KB context can restate as
four things:

1. **The system under test and its boundary.** The whole deployed system,
   with people who perform internal roles counted inside the boundary and
   recorded; model weights fixed at declared versions; hosted models
   allowed. Persistence is continuity of responsibility, not survival of
   any component.
2. **The three hypotheses, each with its refuter.** Sufficiency,
   comparative, and reflection, quoted as adopted on 2026-09-17. The
   refuter stands next to each. The comparative hypothesis names the
   control that matters: a baseline that searches the raw records without
   the learned methodology. The two-part learning test from the lead,
   operative and better, is shown to be what the sufficiency and
   comparative hypotheses operationalize.
3. **What must come from outside.** An external falsifier, an external
   objective, and an outcome level independent of the builder's own
   evaluators. Without these, a claim carries three obligations the builder
   must discharge itself, and the article says what they are.
4. **The first experiment.** One bounded component experiment specified to
   the point of execution: the intervention on a retained theory, the
   matched conditions, the budget accounting, the outcome measure, and the
   three questions it answers, causal contribution, advantage, and sample
   efficiency. The choices a run must still fix, model version, task
   sample, and budget, are listed as such, not hidden.

The article states plainly that no run has been performed. It carries the
draft banner, links each claim to the note that develops it, links external
texts as themselves, lists its source notes, and passes
`commonplace-validate`. The articles README entry is rewritten to match.

## Constraints

- **Refutable first.** Open with what would show the bet wrong, not with
  definitions. Terms are defined in one sentence where first needed, with
  the definition note linked.
- **The hypotheses are quoted as adopted.** Their wording is a program
  commitment. Quote it; do not paraphrase, tighten, or narrow it. Commentary
  goes around the quotation.
- **Honest about people.** Any episode or trial cited names who decided
  what. Human contributions are recorded, not credited to computation.
- **Component results do not substitute for whole-program results.** The
  article says so once, where the first experiment is introduced, and does
  not hedge it again.
- **Ordinary words.** "Precise description of the work" or "methodology",
  never "ontology". Reach, warrant, and oracle are defined if used.
- **Length.** Under 1,600 words. The admissible-path formalism, the
  reconstruction comparisons, and the boundary-case table do not fit; what
  is worth keeping from them goes to a note first, the rest stays in git
  history.

## Inputs

- The superseded draft at `2da543f0`, also copied to
  `/tmp/testing-the-conjectural-learning-program.md` on 2026-09-22: its
  hypotheses section is reused verbatim; its evidence-interface section,
  component-experiment design, and limits are material, not structure.
- The lead article's "What would count as learning?" section, for the
  two-part test this supplement operationalizes.
- The externally-tested-builder definition and the three-obligations note
  for claim 3; the intervention-isolates-one-surface note and the
  sample-efficiency note for claim 4; the complete-theory-path note for why
  operative use alone does not establish improvement.
- The evidence notes for what has and has not been observed in Commonplace.
- The Schmidhuber workshop's first-experiment sketch under `kb/work/`, for
  the matched-budget design, read as workshop material and not linked.

## Choices left to the writer

- Which of the three component questions the first experiment is specified
  around, or whether one design serves all three.
- Whether the Gödel-machine contrast survives as one paragraph or is
  dropped with a link to its note.
- Section titles and order after the opening.

## Verification and stop

Validate with `commonplace-validate`. Then read the draft cold and check
that a reader could run the first experiment from the text plus the listed
open choices. If the experiment cannot be specified that closely without
inventing a budget or sample size, say which choices remain and stop there;
do not fill them. If a claim needs support no note supplies, write the note
first.
