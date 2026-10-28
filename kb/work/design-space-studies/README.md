# Design-space studies

## Commission

Opened on 2026-10-28 at the operator's request. Explore whether a consequential
Commonplace design decision should pass through an explicit **design-space
study** before a proposal or ADR. Such a study is a revisable map of the frame,
the constraints and their provenance, decision axes, compatibility rules,
candidate regions, decision-critical unknowns and the posture of each open
choice. The goal is to find out whether such a study changes decisions, and if
so, what the smallest procedure is that does so.

The prompt was a long ChatGPT exploration supplied by the operator. It is kept
as [background](./background/initial-llm-exploration-2026-10-28.md). It is
**not on the reading path**: treat it as a source of candidate ideas, not as a
specification. Its citations were generated with it and have not been checked.

**Closes when** one of two things happens. Either an instruction for running a
design-space study exists in `kb/instructions/`, with at least one study whose
map exposed something the existing route would have missed (a demoted
constraint, a hidden alternative, a missing axis, or an unknown that changed
the decision). Or the method is rejected with a recorded reason, such as
pilots where the map changed nothing that inverting the request and the
productive-deferral test did not already catch. Theory gained along the way
goes to `kb/theory/`. Then delete this directory and its entry in
`kb/work/README.md`.

## Coupling with other workshops

- [decision-lifecycle-evidence](../decision-lifecycle-evidence/README.md) owns
  the question of what must survive behind an adopted architecture so later
  work can reconsider alternatives. A design-space map is one candidate answer
  to that question. Do not decide durable storage for maps here. Hand findings
  about retention to that workshop.
- [conjecture-store](../conjecture-store/README.md) is developing cheap
  refutable records for theory. A map's axes and compatibility rules are
  conjectures of that kind. Borrow from it without adopting its record type.
- [windows-install](../windows-install/README.md) holds the evidence for the
  candidate retrospective pilot. Read its records; do not edit them.

## Library this builds on

- [First-principles analysis maps a design space before selecting within it](../../theory/first-principles-analysis-maps-design-space-before-selection.md) — rests-on: the map, its falsifiability, rival maps
- [Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](../../theory/productive-deferral-requires-option-evidence-and-convergence.md) — rests-on: the posture of an open choice
- [A framework rule with a boundary-preserving rival is not inherited](../../theory/a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md) — rests-on: demoting a supposed constraint
- [Solve low-degree-of-freedom subproblems first](../../theory/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) — draws-on: commitment ordering
- [Invert solution-shaped requests](../../instructions/invert-solution-shaped-requests.md) — draws-on: the existing framing procedure a study would extend or replace
- [Design rationale management](../../reference/design-rationale-management.md) and [ADR 070](../../reference/adr/070-notes-bind-choices-reference-records-selections-and-state.md) — rests-on: where beliefs, selections and state live today

## Sources ingested for this workshop

- [Lane 1990, design spaces and rules](../../sources/lane-1990-design-spaces-and-rules.ingest.md): dimensions plus weighted rules, tested against held-out systems
- [Ritchey, General Morphological Analysis](../../sources/ritchey-general-morphological-analysis.ingest.md): pairwise cross-consistency with typed exclusions
- [ATAM](../../sources/kazman-2000-atam-architecture-evaluation.ingest.md): scenario evaluation, sensitivity and tradeoff points, assumption-bound judgments
- Already in the KB: [set-based rework](../../sources/kennedy-sobek-kennedy-set-based-rework.ingest.md), [real options](../../sources/pindyck-irreversibility-uncertainty-investment.ingest.md), [Build Systems à la Carte](../../sources/build-systems-a-la-carte.ingest.md), [Parnas 1972](../../sources/parnas-1972-criteria-decomposing-systems-modules.ingest.md)

Not yet ingested:

- **NASA SE Handbook §6.8** (trade studies, value of information): blocked because Smart App Control refuses the `trafilatura` launcher.
- **ArchHypo** (IEEE TSE 2025, open access): IEEE blocks scripted download, so it needs a manually downloaded PDF.

## Files

- [operationalizing.md](./operationalizing.md) — initial agent thoughts on how to test and operationalize the idea; a proposal awaiting the operator's direction, not an adopted plan
- [background/](./background/) — the original exploration; background only

## Conventions

Commits carry `Workshop: kb/work/design-space-studies`.
