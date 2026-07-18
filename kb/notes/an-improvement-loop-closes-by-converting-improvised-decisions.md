---
description: "Names the graded closedness of an improvement loop and claims autonomy advances by converting improvised decisions into addressable, settled, oracle-warranted machinery"
type: kb/types/note.md
traits: [title-as-claim, synthesis]
tags: [foundations, self-improving-systems]
---

# An improvement loop closes by converting improvised decisions into governed machinery

A [proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md), and an instance of the loop *closes* — binary — when a candidate is generated, judged, and made operative. This note names a second, graded sense worth keeping distinct: **how closed the loop is**. A loop is more closed the fewer of the decisions one improvement cycle raises must be supplied through improvised external intervention.

The grading is about improvisation, not headcount. Take one recurring decision: may this tag head claim it links every note carrying the tag? Supplied by improvisation, a maintainer re-derives the answer each time — sweep the tag, eyeball the list, decide. Supplied by machinery, a schema names the mark, a validator recomputes membership on every run, and the failure message routes to the fix; where a person is still involved, they answer a well-posed question ("add this missing member?") rather than an open-ended one. So a cycle whose every step waits on someone deciding from scratch what to check and whether it passed is barely closed even when it completes, while a cycle that runs from candidate to enforced retention with a person supplying only a merge is nearly closed even though a human sits in it.

The claim is that a loop closes by **conversion**, one decision at a time, and that each conversion has the same anatomy. The cluster's [three independent gradings](./three-independent-gradings-place-a-self-improving-system.md) name its faces, and the Commonplace change that produced the enforced completeness mark (ADR 026) shows all three at once:

- the decision's inputs become **addressable** — retained where the deciding process can read them, [since reflection buys addressability](./reflection-buys-addressability.md). The mark's rationale — an unenforced completeness claim is a trap — was a retained, retrievable claim the drafting agent could read, not a hunch re-derived per session.
- the decision itself becomes **settled** — the methodology supplies criteria or determines the result instead of merely naming a decider, [since a methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md). ADR 026 settled the artifact's form, its check, and its authority path in one stroke, leaving nothing about the mark to improvise later.
- the check that warrants acting on the result unattended becomes an oracle whose domain covers the case, [since warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md). The completeness verdict can be trusted unattended because membership is exactly what the validator's query computes — the check establishes the whole decision, not a proxy for it.

Read statically, the gradings place a system. Read dynamically, they are the mechanism by which autonomy advances: autonomy is not a further ingredient layered onto the taxonomy but what accrues as improvisation is converted out of the cycle.

## The displacement ladder

From outside, conversion looks like the displacement of human mediation down a ladder: a person performs a check; then a person follows a written gate; then an agent applies the gate; then a validator enforces it; then failures route into a standing repair procedure; then the system proposes revisions to the gate itself. Each rung keeps the check and moves its performance. [Commonplace's tag-readme pathway](../reference/commonplace-as-a-reflective-system.md) has climbed the middle rungs — a check once performed by eye is now enforced by a validator, consumed by an agent, and routed to a documented fix on failure — while the top rung stays unoccupied. The ladder also fixes what evidence for the thesis looks like: not one episode, but a sequence of traces in which the same class of decision is supplied by progressively less improvisation.

## Why single episodes look like ordinary development

Viewed locally, every episode decomposes innocently: a person had the idea, an agent drafted the change, a person approved it, code enforced it afterward. Nothing in the episode looks like self-improvement, and a critic who samples episodes will correctly find a human at every consequential step. The loop is visible only in the recurrent structure: previously retained methodology shapes the diagnosis and the proposal; the accepted proposal changes the methodology or its machinery; the revised artifacts govern later agents; validators keep the change enforced and surface regressions; and evidence from that operation initiates the next revision. The claim's unit of analysis is this temporally extended structure, not any step of it — which is why the claim can be true while every individual episode remains describable as ordinary supervised work.

## Partial closure is the predicted state, not a way station

Because conversion is per-decision — codify one objective, harden one oracle, settle one meta-decision — a system should be expected to occupy a mixed state for most of its life: some pathways closed end to end, others still terminating in human judgment wherever no adequate oracle or settled criterion reaches. Commonplace is evidence of exactly this architecture. The all-or-nothing question — *is it self-improving, or is it just people using tools?* — therefore misses the design-relevant quantity: where the intervention frontier currently sits, and which conversions would move it. As it moves, the human role shifts outward — toward supplying objectives, resolving the judgments no oracle covers, and extending what can be converted next.

## What closing may buy

Payoff hypotheses, not definitional consequences: lower marginal human mediation per completed improvement; faster cycles, because no step waits on an improvised decision; retention that detects its own regressions; selective correction — a wrong mark is deleted in place, not trained away; and recursive leverage, since converted machinery is itself [organization](./definitions/behavior-determining-organization.md) the loop can be turned on. Reduced new target data is one member of this list, not its headline — [reflection may improve sample efficiency under structured shifts](./reflection-may-improve-sample-efficiency-under-structured-shifts.md) sharpens it into a falsifiable prediction. What closing does not promise is fewer human hours, [since a closing improvement loop relocates human effort to the frontier instead of reducing it](./a-closing-loop-relocates-human-effort-to-the-frontier.md).

## Vocabulary and scope

- Three senses now live near "closed" in this cluster and must not be conflated: a loop instance **closes** (binary — the three functions complete and the change becomes operative); a methodology is **closed under its own recommendations** (an axis of the placement scheme, and one face of conversion here); and a loop is **more or less closed** (this note's graded property over whole cycles).
- The property survives either boundary convention: grade each decision as machine-mediated, externally supplied, or jointly performed, and nothing depends on whether "reflective" is defined to admit established human roles, [a move Commonplace's definition separately declines](./admitting-a-human-into-the-boundary-trades-reflectivity-for-autonomy.md).
- The graded property is defined here, but measuring it inherits the open commensurability problem: [measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md). The thesis gives that measurement problem its purpose — showing the intervention frontier moving outward — without solving it.

## Open Questions

- Whether conversion is net-monotone: automating a decision class lets the system attempt harder changes, which raise new improvised decisions — can the frontier recede on net, and how would that be detected?
- Whether some decisions — objective-setting above all — resist conversion in principle, or only until their inputs are represented and their oracles built.
- Whether a governed-but-human-decided step (a well-posed question routed to a person) should count as partially converted, or whether closedness should count only fully machine-mediated decisions.

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: the loop whose cycles the graded property quantifies over, and the binary sense of "closes" this note extends
- [Three independent gradings place a self-improving system](./three-independent-gradings-place-a-self-improving-system.md) — extends: the placement scheme this note reads dynamically, as the faces of conversion
- [Reflection buys addressability](./reflection-buys-addressability.md) — grounds: the representation face — a decision's inputs retained where the deciding process can read them
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — grounds: the governance face — settled criteria rather than a named decider
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: the warrant face — why the frontier sits exactly where adequate oracles run out
- [Reflection may improve sample efficiency under structured shifts](./reflection-may-improve-sample-efficiency-under-structured-shifts.md) — extends: one payoff hypothesis of a closing loop, sharpened into a test design
- [A closing improvement loop relocates human effort to the frontier instead of reducing it](./a-closing-loop-relocates-human-effort-to-the-frontier.md) — extends: the human-side consequence, and the measures that replace total hours
- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — contrasts: the commensurability problem any measurement of closedness inherits
- [Admitting a human into the boundary trades reflectivity for autonomy](./admitting-a-human-into-the-boundary-trades-reflectivity-for-autonomy.md) — contrasts: the boundary-convention dispute the graded property is robust to
- [Self-improving system](./definitions/self-improving-system.md) — defined-in: the base category and its pathway-relative autonomy grading
- [Commonplace as a partially autonomous, reflective self-improving system](../reference/commonplace-as-a-reflective-system.md) — evidence: one pathway observed part-way up the displacement ladder
- [The tag-readme trace read as a self-improving loop](../reference/tag-readme-trace-as-self-improving-loop.md) — evidence: the specific trace behind the running example, showing which half of each loop function runs in code and which stays human
- [Oracle-strength spectrum](./oracle-strength-spectrum.md) — mechanism: the operational content of "harden one oracle" — the gradient a check climbs as it becomes cheaply verifiable
- [LLM-executed methodologies are metacircular interpreters, not compilers](./llm-executed-methodologies-are-metacircular-interpreters.md) — mechanism: the same displacement read as interpretation-to-codification — prose rules re-interpreted each session until stable paths cross into validators and commands
- [Codification](./definitions/codification.md) — defined-in: the prose-to-symbolic crossing at the machine-mediated extreme of conversion
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — contrasts: the same frontier stated statically — automation stalls where verification is expensive; here the frontier moves as conversions harden oracles
