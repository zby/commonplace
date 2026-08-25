---
description: "The progress question for self-improving systems is not category membership but which decision-bearing functions humans still supply; the endpoint test is whether the boundary can be contracted to exclude them"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Computationally directed self-improvement is a fixed-boundary reallocation ending in contraction

Ask whether a system is self-improving and, under a boundary-relative membership definition, the answer arrives too early to be interesting: ordinary software maintained by humans already qualifies, because the codebase is the organization, the maintainers are inside the declared boundary, and their edits are evidence-responsive operative change — [one of the cases the definition classifies without a special clause](./the-self-improving-system-definition-classifies-its-boundary-cases.md). Growing machine capability does not change that verdict, because the verdict was never about machines.

The transition actually under study runs *inside* the category: from **human-directed** self-improvement, where people supply the decisions the improvement pathway needs, to **computationally directed** self-improvement, where the system's own machinery supplies them. What moves is the allocation of decision-bearing functions. Membership does not move, and treating the transition as a category crossing looks for the change in the one place it never occurs.

## The boundary has to be held fixed for the transition to exist

Two states of the same system are comparable only across a fixed frame. Let the boundary move during the comparison and the transition can be manufactured in either direction: draw it to exclude the maintainers and last year's system already looks computationally directed; draw it to include the model vendor's training pipeline and this year's looks less so. The same applies to the objective and the horizon, [since a self-improvement attribution is elliptical until its objective is named](./self-improvement-is-relative-to-a-declared-objective.md).

So the transition is a claim about one declared frame: hold boundary, horizon, and objective fixed, enumerate the improvement pathway's decision-bearing functions — [search, evaluation, and operative retention where the pathway is proposal-selection](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — and record for each whether a human, a computational process, or both supplies the decision. That is the per-function allocation profile, and [allocation is what carries the comparison](./methodological-and-computational-closure-track-different-changes.md).

## The endpoint is a boundary contraction

The profile locates a system but does not say when the transition is finished, and it deliberately refuses to be summed into a percentage, since functions differ in decomposition, authority, and stakes. The endpoint can be stated exactly anyway, without any aggregation.

Call a set of participants a **cut set** of the pathway when removing them stops the pathway from completing: the humans inside the boundary are a cut set exactly when some decision the pathway requires has no supplier but them.

> The transition is complete when the human participants are no longer a cut set — equivalently, when the boundary can be **contracted** to exclude them and the smaller system still satisfies the same self-improvement attribution, against the same objective, over the same horizon.

The endpoint is derived rather than stipulated. Nothing new is asserted about autonomy: the contracted system either satisfies the membership definition on its own terms or it does not. Boundary contraction is the point at which a redraw that would have been cheating — quietly excluding the maintainers to flatter the system — becomes simply true.

## Why a cut-set test rather than a count

**It has a definite pass condition.** Withhold the human decisions and see whether the pathway completes. That is an existence claim about one run, not an aggregation over functions that resist a common scale.

**It separates presence from participation.** A maintainer who observes every run but supplies no decision the pathway requires is not in the cut set, and their presence does not block the endpoint. A maintainer who intervenes once a quarter, indispensably, is in the cut set and does block it. Counting interventions gets both of these backwards; counting necessity gets both right.

**It grades without needing commensurable functions.** Index the test by horizon and pathway scope. Contraction that succeeds over a week and fails over a year is a real intermediate state, and the largest scope and horizon at which contraction succeeds orders two states of *the same* system — which is the ordering the profile could not supply. This inherits none of the cross-system comparison problem, because it never compares two different function lists. Comparing contraction results across systems remains as hard as before, [since measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md); the gain is intra-system.

The graded reading also reconciles this note with the observation that [increasing computational autonomy relocates human effort rather than reducing it](./increasing-computational-autonomy-relocates-human-effort.md). Contraction succeeding for one pathway at one horizon is fully consistent with flat human hours: attention moves to the pathways and horizons where contraction still fails. Those failures are a usable operationalization of the frontier that note points at.

## What contraction does not certify

**Not warrant.** A contracted pathway completes; whether its acceptances are any good is a separate question, [bounded by the domain over which its oracles are reliable](./warranted-autonomy-is-bounded-by-oracle-domain.md). Contraction can succeed on a pathway that reliably adopts bad changes.

**Not causal independence from humans.** The criteria, types, and gates the contracted system runs on are human decisions that were externalized into artifacts now sitting inside the contracted boundary. Contraction shows that no human decision is *required within the horizon*, not that none is *embodied*. Where the pathway cannot revise those artifacts, the human decision is deferred rather than removed — and that residue is a methodological-closure reading of what the retained method settles, not an allocation reading. This is the test's principal blind spot, and it is the reason the two closure readings are kept apart in the first place.

**Not substrate independence.** The model provider and the infrastructure sit outside the contracted boundary and stay there. Counting that dependency as human participation would put contraction out of reach of every model-mediated pathway and destroy the discrimination the test exists to provide.

**Not a ratchet.** Reallocation runs both ways: a function moved to a computational actor can move back when its oracle turns out to be a poor proxy, and the contraction result can regress without anything having broken.

## Reflection makes the cut set legible

Nothing in the argument uses reflectivity — the test applies to a gradient-driven pathway as readily as to an artifact-mediated one. What [routing change through a readable self-representation](./definitions/reflective-system.md) adds is inspection: when each decision is carried by a named artifact, the cut set can be read off the artifacts and the criteria they encode, rather than only discovered by running the excision experiment. That is [the addressability benefit](./reflection-buys-addressability.md) applied to the pathway's own allocation, and it makes the endpoint test cheap to run repeatedly instead of once.

## Scope

- The test reads necessity for pathway *completion*. A pathway that completes while producing worse changes still passes, which is why the warrant reading is held separately.
- Contraction is assessed per pathway. A system may be contractible for its validation pathway and not for its objective-setting pathway; a whole-system contraction claim without a named pathway hides the mixed architecture, exactly as a whole-system closure claim does.
- Withholding human decisions is not always a runnable experiment — an organization cannot easily stand its maintainers down for a year to see what happens. Where the experiment is infeasible, the test degrades to an argument from the recorded allocation, which is weaker evidence than an observed run.

## Open Questions

- Whether a partial contraction — excising some human participants but not all — is informative, or whether only the full excision has a clean interpretation.
- Whether the deferred-decision blind spot can be closed by requiring that the pathway's own governing artifacts be within its revision scope, or whether that requirement makes the endpoint unreachable in practice.
- Whether repository history can supply retrospective contraction results, by finding intervals in which no human decision entered a pathway and checking whether it completed.

---

Relevant Notes:

- [Methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md) — extends: supplies the per-function allocation profile and its no-human endpoint, which this note restates as a testable boundary contraction
- [The self-improving-system definition classifies its boundary cases without ad hoc exceptions](./the-self-improving-system-definition-classifies-its-boundary-cases.md) — grounds: shows human-inclusive maintained software is already a member, which is why the interesting transition is intra-category
- [Self-improving system](./definitions/self-improving-system.md) — defined-in: the boundary-relative membership the contracted system must independently satisfy
- [Self-improvement is relative to a declared objective](./self-improvement-is-relative-to-a-declared-objective.md) — grounds: the objective that must be held fixed alongside boundary and horizon for the comparison to mean anything
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: names the pathway functions the cut set is drawn over
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — contrasts: the separate reading that decides whether a contracted pathway's acceptances can be trusted
- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](./increasing-computational-autonomy-relocates-human-effort.md) — extends: the horizon-indexed contraction failures operationalize the frontier that note locates human attention at
- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — contrasts: the cross-system commensurability problem this test avoids only by staying intra-system
- [Reflection buys addressability](./reflection-buys-addressability.md) — mechanism: why a readable artifact layer lets the cut set be read rather than only run
- [Reflective system](./definitions/reflective-system.md) — defined-in: the causally connected self-representation that makes a pathway's allocation inspectable
- [Commonplace as a reflective system](./evidence/commonplace-as-a-reflective-system.md) — evidenced-by: a declared human-inclusive boundary whose maintainers are currently a cut set of its improvement pathway
- [Ingest: A Poetiq Perspective on Recursive Self-Improvement (snapshot required)](../sources/poetiq-perspective-on-recursive-self-improvement.ingest.md) — evidenced-by: scopes its reported zero-human-intervention result to harness construction after people choose the task, data, objective, evaluator, and outer process
- [Improvements can accumulate without compounding](./improvements-can-accumulate-without-compounding.md) — extends: explains how the human cut set limits the scale and duration of compounding without entering its definition
