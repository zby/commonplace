---
description: "Autonomy is graded per function, not scored as a percentage, but that profile doesn't yet let us compare two systems or track one system getting more autonomous over time"
type: kb/types/note.md
tags: [foundations, self-improving-systems]
---

# Measuring autonomy well enough to see it improve is an open problem

A shovel does none of the digging's judgment — every stroke is a human motor decision, the tool only transmits force. A hand-operated excavator still has a human deciding every bucket position; it amplifies force but not judgment. A computer-guided excavator that grades to a digital terrain model now has the machine choosing depth-at-this-point instead of the operator's hand choosing it. Somewhere in that progression "the machine now does part of the work" becomes true, but there is no principled place to draw the line and say "40% machine." Decision content is continuous; any percentage cutoff is arbitrary. The same problem applies to any claim that a system is "60% autonomous."

[Autonomy already avoids this trap for a single system](./definitions/self-improving-system.md) by refusing the scalar: it grades who performs each named function of the improvement pathway (search, evaluation, retention) against a declared boundary, rather than scoring the system as a whole. That sidesteps the false precision of a percentage — but it only tells you where one system sits, read once. It was not built to answer two questions this note is naming as open:

- **Is this system becoming more autonomous over time?** Tracking a profile across releases seems tractable if the function list stays fixed — count how many named functions moved from human to mechanical or agent performance. But the function list itself is not fixed. Commonplace's own history is evidence: `commonplace-freshness-status` is confirmed new (ADR 052, days old at the time of writing) and was not a separable noticing function before it — one instance of [candidate-forming and noticing channels getting added as the system grows](../reference/where-change-candidates-come-from-in-commonplace.md). Comparing a profile against its own earlier self runs into the same commensurability problem as comparing two different systems, just deferred.
- **Is one system more autonomous than another?** A bare comparison needs both systems' profiles indexed by the same functions. Two proposal-selection loops that both decompose into search, evaluation, and retention can be compared directly, in principle — the Homeostat, the Gödel machine, and Commonplace's own pathways are exactly this kind of case. But two systems need not decompose their work the same way at all: one KB tool might channel candidate formulation through typed collections with per-collection contracts, as Commonplace does; another might get an analogous quality effect through a single style guide and strict human review, with no separable "collection contract" step to count at all. Counting named functions and comparing the counts would be comparing units that do not correspond.

Neither difficulty is solved by grading harder. What is missing is a way to establish that two profiles — the same system at two times, or two different systems — are indexed by a *commensurable* decomposition before their per-function readings can be set against each other at all. Absent that, the honest answer to "is this getting more autonomous" or "which of these is more autonomous" is that the question is not yet well-posed, not that the answer is unknown.

A count would also erase a real difference in stakes even where decompositions do match. Search and evaluation fail asymmetrically: a bad candidate that search produces unattended still meets evaluation and is rejected at the cost of wasted effort, while a bad acceptance that evaluation makes unattended becomes operative and nothing downstream catches it, [since only the last filter's errors survive](./false-positive-generation-is-filtered-before-retention.md). Handing search to an agent is therefore comparatively cheap even without a strong local check; handing evaluation over is exactly where [warrant, bounded by oracle reach](./warranted-autonomy-is-bounded-by-oracle-reach.md), is the question that matters. A bare count of "how many functions run unattended" would treat these as interchangeable when they are not.

## Open Questions

- Whether a coarse, largely system-independent function list — search, evaluation, retention, from [the proposal-selection loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — can serve as a common ontology that most systems' finer decompositions refine, making cross-system and across-time comparison possible at that coarser grain even when finer function lists diverge.
- Whether a rough, admittedly imprecise proxy — counting non-human-performed functions, weighted by both scope and the search/evaluation stakes asymmetry above — is worth adopting despite lacking a principled basis, the way composite proxy scores are tolerated elsewhere for KB curation ([notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md)).

---

Relevant Notes:

- [Self-improving system](./definitions/self-improving-system.md) — grounds: the per-function, non-scalar autonomy grading this note takes as its starting point and finds insufficient for comparison
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: the function list that happens to be shared across the systems the grounding note already compares
- [Three independent gradings place a self-improving system](./three-independent-gradings-place-a-self-improving-system.md) — see-also: autonomy collapses into the reflective/non-reflective split rather than joining these as a fourth placement axis
- [Warranted autonomy is bounded by oracle reach](./warranted-autonomy-is-bounded-by-oracle-reach.md) — contrasts: that note bounds how much evaluation autonomy can be trusted; this note is about whether autonomy can be measured or compared at all
- [False-positive generation is filtered; false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — grounds: the search/evaluation stakes asymmetry a bare function count would erase
- [Where change candidates come from in Commonplace](../reference/where-change-candidates-come-from-in-commonplace.md) — evidence: `commonplace-freshness-status`, a search-function mechanism confirmed added recently, showing the function list itself changes over time
