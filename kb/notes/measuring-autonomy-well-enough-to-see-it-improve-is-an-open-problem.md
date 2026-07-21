---
description: "Autonomy is reported per function rather than scored as a percentage, but that profile does not yet support comparison across systems or time"
type: kb/types/note.md
tags: [foundations, self-improving-systems]
---

# Measuring autonomy well enough to see it improve is an open problem

A shovel does none of the digging's judgment — every stroke is a human motor decision, the tool only transmits force. A hand-operated excavator still has a human deciding every bucket position; it amplifies force but not judgment. A computer-guided excavator that grades to a digital terrain model now has the machine choosing depth-at-this-point instead of the operator's hand choosing it. Somewhere in that progression "the machine now does part of the work" becomes true, but there is no principled place to draw the line and say "40% machine." Decision content is continuous; any percentage cutoff is arbitrary. The same problem applies to any claim that a system is "60% autonomous."

[The pathway profile's actor allocation already avoids this trap for a single system](./a-self-improving-system-needs-a-profile-not-a-ladder.md) by refusing the scalar: it reports who performs each named function of the improvement pathway — search, evaluation, retention, where the pathway is proposal-selection — against the same declared boundary [membership](./definitions/self-improving-system.md) is read against. That profile locates one system at one time but does not answer two comparative questions:

- **Is this system becoming more autonomous over time?** Tracking a profile across releases seems tractable if the function list stays fixed — count how many named functions moved from human to mechanical or agent performance. But the function list itself is not fixed. Commonplace's own history is evidence: `commonplace-freshness-status` is confirmed new (ADR 052, days old at the time of writing) and was not a separable noticing function before it — one instance of [candidate-forming and noticing channels getting added as the system grows](../reference/where-change-candidates-come-from-in-commonplace.md). Comparing a profile against its own earlier self runs into the same commensurability problem as comparing two different systems, just deferred.
- **Is one system more autonomous than another?** A bare comparison needs both systems' profiles indexed by the same functions. Two architectural proposal-selection loops that both decompose into search, evaluation, and retention can be compared directly, in principle — the Gödel machine and Commonplace's own proposal-selection pathways are this kind of case. The Homeostat sits at a coarser floor: it can be reconstructed as variation, viability pressure, and retention, but not as the same architectural subtype because generation and rejection are not separated by an evaluator. But two systems need not decompose their work the same way at all: one KB tool might channel candidate formulation through typed collections with per-collection contracts, as Commonplace does; another might get an analogous quality effect through a single style guide and strict human review, with no separable "collection contract" step to count at all. Counting named functions and comparing the counts would be comparing units that do not correspond.

Neither difficulty is solved by adding precision. Two profiles — one system at different times, or different systems — need a *commensurable* decomposition before their per-function readings can be compared. Without one, “is this getting more autonomous?” is not yet well-posed.

A count would also erase a real difference in stakes even where decompositions do match. Search and evaluation fail asymmetrically: a bad candidate that search produces unattended still meets evaluation and is rejected at the cost of wasted effort, while a bad acceptance that evaluation makes unattended becomes operative and nothing downstream catches it, [since only the last filter's errors survive](./false-positive-generation-is-filtered-before-retention.md). Handing search to an agent is therefore comparatively cheap even without a strong local check; handing evaluation over is exactly where [warrant, bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md), is the question that matters. A bare count of "how many functions run unattended" would treat these as interchangeable when they are not.

## Open Questions

- Whether a coarse, largely system-independent function list — search, evaluation, retention, from [the proposal-selection loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — can serve as a common ontology that most systems' finer decompositions refine, making cross-system and across-time comparison possible at that coarser grain even when finer function lists diverge.
- Whether a rough, admittedly imprecise proxy — counting non-human-performed functions, weighted by both scope and the search/evaluation stakes asymmetry above — is worth adopting despite lacking a principled basis, the way composite proxy scores are tolerated elsewhere for KB curation ([notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md)).

---

Relevant Notes:

- [A self-improving system needs a profile, not a ladder](./a-self-improving-system-needs-a-profile-not-a-ladder.md) — grounds: actor allocation, the per-function, non-scalar autonomy profile this note takes as its starting point and finds insufficient for comparison
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: the function list that happens to be shared across the systems the grounding note already compares
- [Self-improving system](./definitions/self-improving-system.md) — grounds: the declared-boundary relativity the allocation profile inherits from membership
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — contrasts: that note bounds how much evaluation autonomy can be trusted; this note is about whether autonomy can be measured or compared at all
- [False-positive generation is filtered; false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — grounds: the search/evaluation stakes asymmetry a bare function count would erase
- [Where change candidates come from in Commonplace](../reference/where-change-candidates-come-from-in-commonplace.md) — evidence: `commonplace-freshness-status`, a search-function mechanism confirmed added recently, showing the function list itself changes over time
