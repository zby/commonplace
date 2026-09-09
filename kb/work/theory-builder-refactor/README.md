# Workshop: refactor the research program around the theory builder

## Goal

Reorder the KB's research program so that the automated theory builder is the
postulate and the automated software house is a derived requirement. Today the
[automated software house conjecture](../../articles/automated-software-houses-with-fixed-llms.md)
is the head of the program, and theory refinement appears as the mechanism by
which the house learns ([training article](../../articles/the-software-house-as-the-unit-of-training.md)).
The reordered program starts from a persistent, automated system that develops
and revises theories it did not anticipate, and asks whether sufficient
open-endedness forces that system to contain something that meets the
[software house](../../notes/definitions/software-house.md) definition.

The reorder is not a new claim. The derived step already exists as
[an open-domain theory builder becomes a software house when new domains
require production-machinery changes](../../notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md).
What changes is which end is load-bearing, and the novelty claim that follows:
automatic theory refinement is old (EITHER, FORTE); acquiring the
theory-family-specific refinement machinery is the proposed advance.

## Who posed it

The operator, on 2026-09-09, from a summary of a ChatGPT discussion. The
summary proposed a four-level ladder: classical theory refinement, universal
theory refinement, automatic universal theory refinement, and a fourth rung
for refinement embedded in a closed action-and-consequence loop. The agent's
assessment in the same session found the ladder mixed two axes (role
allocation and loop closure), found *universal* unstable as a term, and found
that natural-language form alone does not make a theory refinable. The
workshop uses the KB's term, theory refinement, throughout; the summary's own
names are not carried in. The operator then commissioned this workshop: start from this
README, then write a proposal for the theory builder the program needs, under
whatever adjective fits, copying the good parts of the software-house
definition.

## Working artifacts

- [Theory-builder proposal](./theory-builder-proposal.md) — the draft
  definition of the open-ended automated theory builder, the role table that
  replaces the ladder, the derived software-house claim, the discriminating
  test, and the choices left to the operator.

## What closes the workshop

1. A definition of the theory builder is accepted into
   `kb/notes/definitions/`, or the operator declines it with a recorded
   reason.
2. The derived claim (open-endedness forces a software house) has one home in
   `kb/notes/`, reconciled with the existing open-domain note rather than
   duplicated beside it.
3. Every artifact in the inventory below has a disposition: reframe, keep, or
   decline. Reframes are executed in their own commits, not in this workshop.
4. The discriminating test named in the proposal has run once, or its
   deferral is recorded with the reason.

## Inventory of artifacts the reorder touches

The proposal names how each would change. Dispositions are recorded here as
they are decided.

| Artifact | Current head | Disposition |
|---|---|---|
| `kb/articles/automated-software-houses-with-fixed-llms.md` | software house first | open |
| `kb/articles/bootstrapping-the-first-automated-software-house.md` | software house first | open |
| `kb/articles/the-software-house-as-the-unit-of-training.md` | house is the trained unit; theory refinement is the mechanism | open |
| `kb/articles/nearest-existing-constructions-to-a-witness-house.md` | witness-house lens | open |
| `kb/notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md` | already the derived step | open (candidate home for closing condition 2) |
| `kb/notes/definitions/theory-refinement.md` | genus definition; departures listed as form, then subject | reframed 2026-09-09: machinery is the first departure, form its consequence, subject independent |
| `kb/notes/definitions/software-house.md` | complete persistent producer | keep; the proposal copies its structure |
| `kb/notes/definitions/codification.md` | the natural-language to symbolic crossing | keep unchanged; codification back is this crossing per family, not a new term |
| `kb/notes/universal-software-factory-needs-a-declared-universality-axis.md` | four universality axes | keep; supplies the rule that *universal* needs a declared axis |
| `kb/notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md` | house needs procedures per theory | open; states the machinery gap from the house side |
| `kb/notes/open-ended-theory-learning-and-factory-learning-close-the-same.md` | carries a factory-to-house TODO | open |
| `kb/notes/broad-software-demands-create-pressure-for-agentic-factory-development.md` | carries a factory-to-house TODO | open |

## Evaluation boundary

Evidence is the local KB at commit `c4ef2e2e` plus the two classical
theory-refinement ingests (EITHER, FORTE). No new external search was run for
the framing. The discriminating test in the proposal uses this repository's
own git history as its corpus; a result there bears on Commonplace as one
witness, not on the derived claim in general.

## Coordination

- [commonplace-nearest-constructions](../commonplace-nearest-constructions/README.md)
  already treats Commonplace as three objects, the first of which is "the
  human-inclusive theory builder operating today". The definition proposed
  here should become the shared term for that object; do not fork a second
  sense.
- [explanatory-theories-deployment-time-learning](../explanatory-theories-deployment-time-learning/README.md)
  owns the experiments on theory use inside an improvement loop. This
  workshop does not redesign them; it only names where they sit on the
  loop-closure axis.
- [operator-led-article-clarification](../operator-led-article-clarification/README.md)
  edits the three articles for readability. Reframing their heads is a content
  change and must not be mixed into clarification commits.
- The work index lists a `reachability-working-paper-publication` workshop
  whose directory no longer exists. Not this workshop's problem; noted so a
  later triage does not look for it here.

Write scope while open: this directory only. Library edits happen in separate
commits once a disposition is recorded above.
