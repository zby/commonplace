---
description: "When a system preferentially transfers decisions whose premises, criteria, and checks are available, the remaining human decisions become harder to warrant per decision; this predicts a residue composition, not structural computational openness"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions

Call a decision **warrantable for computational supply** when the deciding path
has the premises it needs, a sufficiently settled objective, criterion, or
authority, and evidence capable of rejecting a plausible but harmful candidate.
These conditions are relative to a declared task distribution, boundary,
objective, horizon, and available oracles.

The claim is conditional. When a system preferentially transfers warrantable
decisions out of its human cut, the decisions left with people become enriched
for unrepresented premises, unsettled criteria, weak checks, and delayed
consequences. Per decision, the residue is harder to warrant than the set that
moved.

This is a selection effect, not a claim that the remaining work is essentially
human. It also does not establish that real systems usually transfer decisions
in this order. That prevalence question needs before-and-after evidence from
actual automation paths.

## Why the residue changes composition

A formatter can take formatting decisions because its inputs are represented,
its rule is settled, and idempotence or comparison with a specification supplies
a cheap check. It stops before design or maintenance decisions because those
are not merely more examples of formatting. Their premises, criteria, and
consequences have a different warrant structure.

Repeat this pattern across mechanisms. Each mechanism takes the slice that its
representations, decision rules, and oracles can support. What remains is not a
random sample of the original work. It is selected by the reasons transfer
failed.

This differs from the elastic-backlog effect in which freed attention moves to
new frontier work. The selection effect operates even with the incoming
workload held fixed. The human cut may shrink while the average ambiguity,
stakes, or evaluation cost of its remaining decisions rises.

## The residue is a work list

| Why the decision stayed human | What must grow before warranted transfer |
|---|---|
| A required premise is unavailable to the deciding process | Representation, retrieval, or acquisition of the premise |
| The objective, commitment, criterion, or authority does not settle what may be accepted | Methodological settlement, an explicit commitment, or a represented grant of authority |
| No sufficiently independent check can defeat the candidate | Verification, decorrelated criticism, delayed exposure, or accepted error-cost tolerance |
| The decision arises after the automatic path ends | Continuity, persistent state, and later reactivation |
| Transfer is possible but costs more than human judgment | No structural capacity; the available transfer is currently uneconomic |

The table should be applied to individual decisions, not to job titles. A
residual design decision can contain formalizable and checkable substeps, and a
nominally automated task can still export its decisive premise or acceptance to
a person.

## Coherent modification is the hardest delayed-evidence case

At an open-ended program-modification crux, no complete local rule or cheap
oracle determines which change preserves the program's purpose and organization.
A human theory-holder does not solve that problem by possessing a perfect
specification. The person uses a partial program theory to guide search,
interpret failure, backtrack, and revise as later evidence arrives.

A computational composite can carry the same decision only by sustaining that
longitudinal process. The theory may make a provisional proposal better
warranted without settling it immediately. Warrant accumulates through exposure,
recovery, and read-back across later demands, [because holding a program theory
means sustaining coherent search under delayed feedback](./holding-a-program-theory-means-sustaining-coherent-search-under-delayed-feedback.md).

This is where the bearer question and the residue question meet. They still ask
different things. The bearer question asks whether the composite can preserve
coherent search and recovery. The transfer question asks whether enough of that
process and its corrective evidence lie inside the declared boundary to move
the decision with warrant.

## Consequences for closure and evaluation

Structural computational closure asks where required decisions and transitions
occur. A path can be computationally closed while using a captured evaluator,
a viability-only gate, or a bad objective. Those failures make the path weak,
dangerous, or inadequately warranted; they do not make a decision cross the
human boundary.

The selection effect therefore does **not** imply that an evaluator decides
computational closure. It implies that an adequate evaluator is often the
binding condition for **warranted, non-degenerate closure** and for transferring
the hardest residual decisions without merely hiding them.

Three common patterns create the appearance of warranted transfer:

- a captured evaluator lets the candidate supply the decisive standard;
- a viability-only gate treats build success or non-crash behavior as evidence
  of improvement; and
- boundary export leaves demand choice, missing premises, or final acceptance
  with a person outside the declared path.

The first two can occur inside a structurally closed system. The third is an
actual failure of the declared closure claim when the exported decision was
required by that declaration. Keeping these cases separate preserves the
[distinction between usefulness, autonomy, warrant, and
power](./usefulness-autonomy-warrant-and-power-are-separate-dimensions.md).

The remote-programmer benchmark is likewise a capability comparison under a
fixed client. It can show that the worker role moved while task choice, feedback,
and acceptance remain declared exports, [because holding the client fixed
exports the least-warrantable decisions](./holding-the-client-fixed-exports-the-least-warrantable-decisions.md).

## What would test the selection claim

A direct test should reconstruct successive transfers on one path while holding
the boundary, objective, horizon, and workload as stable as possible. Before
each transfer, classify candidate decisions by premise availability, criterion
settlement, checkability, delay, and cost. Then compare the decisions that moved
with those that remained.

Evidence for the mechanism would show that transferred decisions were more
warrantable under the preregistered classification and that the residual mix
shifted toward missing premises, unsettled criteria, or weak and delayed checks.
A cross-sectional finding that current systems often lack independent evaluation
is consistent with the predicted bottleneck, but it does not establish the
before-and-after selection effect.

A second test concerns displaced judgment. Compare reviewers who see only
escalated residual cases with reviewers who also see routine cases. If the first
group performs worse on the hard cases, that supports the concern that transfer
can weaken the information environment of the remaining human decisions.

## Scope

- The prediction requires preferential transfer of warrantable decisions. A
  system that automates whatever is cheap or attempts whatever a model will try
  can produce a different residue.
- Warrantability is system-relative and can regress when an oracle proves to be
  a weak proxy.
- The claim predicts enrichment, not purity. Warrantable decisions may remain
  human because transfer is uneconomic or intentionally withheld.
- Structural closure, capability, and warrant remain separate coordinates.
- The claim does not imply that residual decisions become impossible to move.
  It predicts what new representation, settlement, verification, or continuity
  machinery the next transfer must supply.

## Open Questions

- Do real automation histories show the predicted before-and-after enrichment?
- Which classification grain avoids counting a large architectural decision and
  a small formatting choice as comparable units?
- How should delayed evidence receive credit when several decisions and theory
  revisions intervene before the consequence appears?
- Does removing routine cases measurably degrade later human judgment on the
  escalated residue?

---

Relevant Notes:

- [Codifying predictable choices leaves agents with less predictable work](./codifying-predictable-choices-leaves-agents-with-less-predictable-work.md) — mechanism: supplies the analogous selection effect at the agent–code boundary
- [Computationally directed self-improvement is a fixed-boundary reallocation ending in contraction](./computationally-directed-self-improvement-is-a-reallocation.md) — grounds: defines the human cut and the transfer path
- [Holding a program theory means sustaining coherent search under delayed feedback](./holding-a-program-theory-means-sustaining-coherent-search-under-delayed-feedback.md) — extends: identifies the hardest delayed-evidence modification case
- [Each residue class needs a different mechanism, so a self-improving architecture must be mixed](./residue-classes-need-different-mechanisms-so-architecture-is-mixed.md) — extends: converts the residue reasons into distinct functional requirements
- [A benchmark that holds the client fixed exports the least-warrantable decisions by design](./holding-the-client-fixed-exports-the-least-warrantable-decisions.md) — extends: applies the residue analysis to a capability benchmark
- [Tool usefulness, computational autonomy, warrant, and system power are separate dimensions](./usefulness-autonomy-warrant-and-power-are-separate-dimensions.md) — grounds: prevents the evaluator bottleneck from redefining structural closure
