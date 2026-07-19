---
description: "Maps the ADR-026 tag-readme trace onto the search/evaluation/retention loop, showing which half of each step runs in code and which stays human"
type: kb/types/note.md
traits: [has-implementation]
---

# The tag-readme trace read as a self-improving loop

The [observed trace](./tag-readme-trace-observed-causal-connection.md) discharges causal connection. Read against [self-improving system](../notes/definitions/self-improving-system.md), the same change also discharges that definition, which asks for two things the reflective obligations do not: a change to the system's own organization, and a response to evidence about an objective it could have failed. Commonplace improves in the [proposal-selection](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) shape — draft a candidate, review it with a real chance of rejection, merge selectively — so that loop is the grid to lay over the trace. This note does the full mapping; the [classification](./commonplace-as-a-reflective-system.md) draws the human, joint, and computational allocation profile from it.

| Requirement | In the trace | Runs in |
|---|---|---|
| **Change to the system itself** | The edit landed on `kb/types/tag-readme.md`, a self-representing artifact rather than ordinary content. | — |
| **Search** | Splits: a maintainer noticed the `index` type was doing two jobs and that the `learning-theory` head had outgrown its completeness claim. Formulating that into ADR 026's specific candidate ran through an agent retrieving [stale indexes are worse than no indexes](../notes/stale-indexes-are-worse-than-no-indexes.md) as self-representation and drafting the split around it. | Human, then computational; the candidate path is joint overall |
| **Improvement objective** | The bar the change could have missed: a marked head must not mislead a thorough reader, per [stale indexes are worse than no indexes](../notes/stale-indexes-are-worse-than-no-indexes.md). ADR 026 makes it testable — `complete` is a mark the validator can falsify. | Human frames it; code checks it |
| **Evaluation** | Tests and the validator mechanically check that the marks are consistent; the judgment that the split was the right *shape* was the maintainer's. | Split |
| **Operative retention** | The three consumers — enforcement, routing, advice — keep acting on the change after merge. | Code (after human merge) |

## What the mapping settles, and what it does not

Naming the objective is the step the reflective reading never had to take, and it is what makes the loop improvement-*directed* rather than merely change-directed. A change loop with no objective can only report that something moved; this one can report that a specific bar — do not mislead a thorough reader — is being held, and can fail against it.

The honesty check lives here too: the validator passing means the marks are consistent, not that the type split actually made the KB better. Evaluating the *objective* is mechanical; evaluating whether the objective was worth adopting is not, and that judgment stays the maintainer's. The pass is a result; the improvement is still a claim.

## The allocation the mapping exposes

Search and evaluation are joint: the maintainer chooses the target and judges the design's shape, while the agent formulates the candidate and the validator checks the codified objective. Retention becomes computational after human adoption. The whole pathway is reflective because the accepted change is mediated through operative self-representation, but that does not determine actor allocation. Human gates remain where no adequate automatic check reaches, [since warranted autonomy is bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md).

---

Relevant Notes:

- [Commonplace as a reflective self-improving system](./commonplace-as-a-reflective-system.md) — part-of: the classification and allocation profile this reading supports
- [The tag-readme change as an observed causal-connection trace](./tag-readme-trace-observed-causal-connection.md) — part-of: the trace this reading interprets
- [Where change candidates come from in Commonplace](./where-change-candidates-come-from-in-commonplace.md) — part-of: surveys the wider set of candidate-forming mechanisms the agent's role in Search is one instance of
- [Admitting a human into the boundary moves reflective discrimination to computational allocation](../notes/admitting-a-human-into-the-boundary-moves-reflective-discrimination-to-computational-allocation.md) — grounds: why actor allocation is reported separately from the pathway's reflectivity
- [Self-improving system](../notes/definitions/self-improving-system.md) — rationale: the definition this trace is read against
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — rationale: the search/evaluation/retention grid used here
- [warranted autonomy is bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) — rationale: why the human gates sit where the oracle runs out
- [stale indexes are worse than no indexes](../notes/stale-indexes-are-worse-than-no-indexes.md) — rationale: the improvement objective the loop aims at
