# Case packet

Neutral case identifier: case-fd065e5a4769ae

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# Measuring autonomy well enough to see it improve is an open problem

A shovel does none of the digging's judgment — every stroke is a human motor decision, the tool only transmits force. A hand-operated excavator still has a human deciding every bucket position; it amplifies force but not judgment. A computer-guided excavator that grades to a digital terrain model now has the machine choosing depth-at-this-point instead of the operator's hand choosing it. Somewhere in that progression "the machine now does part of the work" becomes true, but there is no principled place to draw the line and say "40% machine." Decision content is continuous; any percentage cutoff is arbitrary. The same problem applies to any claim that a system is "60% autonomous."

[Actor allocation already avoids this trap for a single system] by refusing the scalar: it reports who performs each named function of the improvement pathway — search, evaluation, retention, where the pathway is proposal-selection — against the same declared boundary [membership] is read against. That profile locates one system at one time but does not answer two comparative questions:

- **Is this system becoming more autonomous over time?** Tracking a profile across releases seems tractable if the function list stays fixed — count how many named functions moved from human to mechanical or agent performance. But the function list itself is not fixed. Commonplace's own history is evidence: `commonplace-freshness-status` is confirmed new (ADR 052, days old at the time of writing) and was not a separable noticing function before it — one instance of [candidate-forming and noticing channels getting added as the system grows]. Comparing a profile against its own earlier self runs into the same commensurability problem as comparing two different systems, just deferred.
- **Is one system more autonomous than another?** A bare comparison needs both systems' profiles indexed by the same functions. Two architectural proposal-selection loops that both decompose into search, evaluation, and retention can be compared directly, in principle — the Gödel machine and Commonplace's own proposal-selection pathways are this kind of case. The Homeostat sits at a coarser floor: it can be reconstructed as variation, viability pressure, and retention, but not as the same architectural subtype because generation and rejection are not separated by an evaluator. But two systems need not decompose their work the same way at all: one KB tool might channel candidate formulation through typed collections with per-collection contracts, as Commonplace does; another might get an analogous quality effect through a single style guide and strict human review, with no separable "collection contract" step to count at all. Counting named functions and comparing the counts would be comparing units that do not correspond.

Neither difficulty is solved by adding precision. Two profiles — one system at different times, or different systems — need a *commensurable* decomposition before their per-function readings can be compared. Without one, “is this getting more autonomous?” is not yet well-posed.

A count would also erase a real difference in stakes even where decompositions do match. Search and evaluation fail asymmetrically: a bad candidate that search produces unattended still meets evaluation and is rejected at the cost of wasted effort, while a bad acceptance that evaluation makes unattended becomes operative and nothing downstream catches it, [since only the last filter's errors survive]. Handing search to an agent is therefore comparatively cheap even without a strong local check; handing evaluation over is exactly where [warrant, bounded by oracle domain], is the question that matters. A bare count of "how many functions run unattended" would treat these as interchangeable when they are not.

## Open Questions

- Whether a coarse, largely system-independent function list — search, evaluation, retention, from [the proposal-selection loop] — can serve as a common ontology that most systems' finer decompositions refine, making cross-system and across-time comparison possible at that coarser grain even when finer function lists diverge.
- Whether a rough, admittedly imprecise proxy — counting non-human-performed functions, weighted by both scope and the search/evaluation stakes asymmetry above — is worth adopting despite lacking a principled basis, the way composite proxy scores are tolerated elsewhere for KB curation ([notes need quality scores to scale curation]).

---

Relevant Notes:

## Artifact B

# Self-improving system

A **self-improving system** makes operative changes to its own behavior-determining organization, where those changes are causally responsive to evidence bearing on an **improvement objective**.

*Its own* means the object of change is the system's [behavior-determining organization] — its parameters, policies, memory, rules, workflows, code — not an external work product. A compiler that optimizes programs is not self-improving; a compiler pipeline that rewrites its own optimizer is. This is Ashby's two-loop distinction: operating a system is one loop, modifying the system that operates is another. The attribution is assessed against a declared boundary: a model fine-tuned by an external training pipeline is being improved, while the composite of model plus pipeline self-improves — [the boundary cases make this dependence explicit].

*Operative* means the change affects subsequent operation over the relevant horizon, through a consumer, a channel, and a force — [operative change], which does not require permanence; a transient compensation, or a change nothing ever acts on, does not qualify.

*Makes* is read over a declared assessment horizon, like operativity: a system is self-improving over that horizon when evidence-responsive operative self-change occurs within it. The dispositional attribution — the system *has* a standing improvement pathway, currently exercised or not — is also available, but it is a different claim and must be marked as such; a pathway nothing has exercised over the relevant horizon supports only the dispositional reading. Tense, like boundary, is declared rather than fixed by the definition.

## Evidence-responsiveness does not require a gate

*Responsive to evidence* is defined in [evidence bearing on an improvement objective]. There must be a loss, reward, error, viability bound, test, judgment, or other criterion for the evidence to bear on; otherwise the change is merely caused, not improvement-directed.

The evidence may directly determine an update that is always adopted, or it may evaluate a candidate that can be rejected. A separately represented candidate, evaluator, or acceptance gate is therefore not required by membership. The [proposal-selection improvement loop] owns that named subtype and its search, evaluation, oracle, and retention vocabulary.

> An improvement criterion is required semantically; an explicit evaluator is not required architecturally.

## What membership leaves open

Membership establishes improvement-directed self-change, not a complete architecture or a successful outcome. Evidence-responsiveness can faithfully pursue a bad objective, and an evaluator can accept a harmful change: only outcome evidence establishes that improvement occurred.

Classify the remaining questions elsewhere:

- [Reflective system] owns whether the pathway changes itself through a causally connected self-representation; reflection is not required for membership.
- [The pathway profile] owns reflective structure, improvement dynamics, governance, and actor allocation; [the cumulativity criterion itself] is held separately.
- [Methodological and computational closure] owns the two closure readings, and [warranted autonomy] owns when unattended evaluation is trustworthy.

## Exclusions

- **Not self-modification alone.** Blind or accidental rewrites lack evidence-responsiveness.
- **Not regulation alone.** A thermostat changes its environment, not its own behavior-determining organization; a learning thermostat that revises its controller does.
- **Not work-product improvement.** Improving an answer or external code does not change the improving system's own organization.
- **Not reflection, a gate, or autonomy.** Each may describe a member, but none is a membership condition.
- **Not guaranteed success.** The term names an improvement-directed mechanism, not a favorable outcome.

## Misuse Cases

- Treating the proposal-selection improvement loop as the definition rather than a named subtype, which re-smuggles an architecture into semantics.
- Reporting an autonomy grade without declaring the boundary it was assessed against.
- Attributing self-improvement without naming the objective it is indexed to, or naming one the pathway's evidence is not diagnostic of — [the first leaves the attribution elliptical, the second makes it false].
- Reading a dormant improvement pathway as current self-improvement — the dispositional claim (*has* a pathway) and the horizon claim (evidence-responsive change is occurring over this horizon) are different attributions.
- Treating a helpful change to an external product as self-improvement of the tool that produced it.

## Provenance and departures

One departure is semantic rather than a retired restriction: the predicate is frame-indexed. The bearer of the property is a bounded system — a system under a declared boundary — not a substrate simpliciter, so an attribution is elliptical until the boundary is named. Established classification practice reads category membership frame-independently; the fine-tuning-pipeline case in [the boundary cases] is why that reading fails here — the same substrate is being improved under one boundary and self-improving under another.

Two earlier restrictions were retired because they excluded central cases. Requiring self-representation excluded parametric learners; the substantive benefit of reflection now belongs to [reflection buys addressability]. Requiring reject-capable evaluation excluded direct gradient- and viability-driven adaptation; proposal-selection now names that narrower architecture.

This architecture-neutral choice is consistent with uses of “self-improving” for gateless self-tuning algorithms ([Ailon et al. 2011]) and with self-adaptive-systems literature treating feedback-loop models as engineering reference models rather than definitions ([Weyns]; [Petrovska, Erjiage, and Kugele 2025]). It is Commonplace's explication, not a claimed field consensus.

---

Relevant Notes:

## Under-review context phrase

the declared-boundary relativity the allocation profile inherits from membership
