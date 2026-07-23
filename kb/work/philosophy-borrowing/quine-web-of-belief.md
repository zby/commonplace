# Quine: Web Of Belief

## Candidate borrowing

Quine's web-of-belief picture treats beliefs as mutually supporting rather than individually isolated. Central beliefs are harder to revise because many other commitments depend on them; peripheral beliefs can be changed with less disruption.

For commonplace, the useful analogue is not a theory of truth. It is a maintenance heuristic: revisions to central, high-reach notes have wider downstream impact than revisions to local, low-reach notes.

## Why it fits

The KB already has the ingredients:

- claim titles expose commitments
- link semantics encode support, contradiction, and extension
- reach marks how far an explanation transfers
- backlinks and staleness detection are active maintenance concerns

The web-of-belief frame could unify those into a revision workflow: when a note changes, do not only ask "which files link to it?" Ask how central the changed claim is to the KB's reasoning.

## Possible operational form

For high-reach or high-centrality notes, revision should trigger a downstream review packet:

1. Identify inbound strong links: notes that use the changed note as `grounds`, `extends`, or inline premise.
2. Classify the change: local wording, boundary condition, mechanism change, or conclusion reversal.
3. Review only the downstream claims whose dependency type makes the change relevant.
4. If downstream review is too broad, create a workshop rather than silently accepting the revision.

## Existing connections

- [Brainstorming: how reach informs KB design](../../notes/brainstorming-how-explanatory-reach-informs-kb-design.md) — already states that high-reach revisions can silently break downstream reasoning
- [Inbound and outbound links serve asymmetric reader needs](../../notes/inbound-and-outbound-links-serve-asymmetric-reader-needs.md) — backlinks would surface who depends on a note
- [Link-graph plus timestamps enables make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — pairwise staleness detection catches some dependency changes but may miss high-reach conceptual drift
- [Linking theory](../../notes/linking-theory.md) — typed links reduce decision cost and expose dependency types

## Failure mode

The risk is over-philosophizing a maintenance problem already covered by reach and backlinks. Quine is worth borrowing only if it changes the workflow: centrality-sensitive revision handling, dependency-aware review packets, or a clearer distinction between peripheral edits and theory revisions.

## What would make this worth promoting?

Promote this if a high-reach note revision invalidates downstream reasoning in a way simple timestamp checks or local validation would miss. That would show the web-of-belief framing has operational value.
