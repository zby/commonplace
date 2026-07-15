---
description: "A proposal-selection improvement loop — candidates generated, evaluated with possible non-adoption, selectively retained — requires search, evaluation that can reject, and operative retention"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [foundations, computational-model, self-improving-systems]
---

# A proposal-selection improvement loop requires search, evaluation, and operative retention

A **proposal-selection improvement loop** is the architecture of improvement in which candidate changes are generated, evaluated with a possibility of non-adoption, and selectively made operative. It is a named subtype, not the whole of the phenomenon: a [self-improving system](./definitions/self-improving-system.md) needs its changes to be responsive to evidence bearing on an improvement objective, and evidence may instead determine an update directly — gradient-, reward-, error-, or viability-driven — with no candidate ever standing to be rejected. What follows is the anatomy of the subtype, and it applies with full force exactly there.

A proposal-selection loop requires three functions: **search** brings a candidate change into consideration, **evaluation** supplies grounds for accepting or rejecting it, and **operative retention** preserves an accepted change with behavioral authority. Remove any one and the loop does not close — a change nobody proposed, nobody could reject, or nobody will ever act on.

The loop is therefore narrower than self-modification. A blind, accidental, or unconditional rewrite may change later behavior without applying any criterion; a transient rewrite may fail to preserve the result. Both can count as self-modification, but neither closes a proposal-selection loop. Conversely, the three functions can close the loop in a system that is not reflective at all.

A terminology note: the concept descends from Ashby's **adaptation** — his ultrastable system is the precedent developed below — but it is named for what the loop aims at rather than by his word for it. Everyday adaptation is transient compensation, an eye adjusting to the dark, and retains nothing; retention is one of the three requirements. Where this note says *adaptation* or *adaptive*, it means Ashby's phenomenon; the loop is the proposal-selection improvement loop, and *improvement loop* below abbreviates it.

A [reflective system](./definitions/reflective-system.md) supplies one possible causal path into this loop. Through **intercession** — an operation that changes the system through its causally connected self-representation — it can modify a represented aspect of itself. Making that path available does not itself provide search, evaluation, or retention.

## Search determines what enters consideration

Search brings an unrealized change under consideration. It may include:

- detecting a problem, opportunity, or adaptation signal;
- selecting the aspect and operation to change;
- generating one or more candidates;
- allocating effort and deciding when to stop or escalate.

At minimum, search must produce a candidate from a space in which other possible changes remain unrealized. It need not compare several candidates at once or operate autonomously. A maintainer may choose the problem, a model may draft a candidate, and a script may enumerate alternatives within one declared socio-technical loop. Assigning those functions establishes the loop's boundary; it does not make the loop reflective.

Search reach and evaluation strength are independent limits:

> Evaluation cannot select a candidate that search never reaches.

A strong verifier can improve judgments within a narrow generator's reach, but it cannot expand that reach. [Automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) gives one concrete search space—extract, split, synthesize, relink, regroup, reformulate, retire—whose judgment-heavy parts remain substantially human-driven.

## Evaluation determines which changes may remain operative

Evaluation applies criteria to a proposed or already actualized change. Its result must be able to affect selection, rollback, or continued retention. Evaluation is non-vacuous only if some possible result permits rejection: an unconditional trigger is not an evaluator merely because it precedes a transition.

**Oracle** is shorthand for the component or procedure that supplies the evidence or judgment. It may be a proof system, test, validator, empirical measurement, rubric, model evaluator, human review, or some combination. The [oracle-strength spectrum](./oracle-strength-spectrum.md) grades these mechanisms, while [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) explains why constructing an adequate oracle is often harder than generating candidates.

Any judgment remains scoped to what the check establishes. An oracle may accept a candidate under specified criteria without establishing that the change is globally beneficial. Search and evaluation may be performed by the same person or process, but they fail in different ways and improve by different means. They are analytically separable rather than independent: automating one changes the load on the other.

## Operative retention makes the change consequential

Acceptance alone does not make a change consequential. Operative retention combines persistence with an authority path through which the retained result can affect later behavior. In [behavioral authority](./definitions/behavioral-authority.md) terms, the change needs a **consumer**, a **channel**, and a **force**.

- A reviewed note that no future reader or prompt-assembly step loads has no consumer.
- An approved patch that is never merged has no channel.
- A generated validator that no command invokes has no force.

In each case, search ran and evaluation passed, but the improvement loop remained open: the artifact exists without becoming behaviorally consequential.

## Feedback is what makes later iterations responsive

The loop can repeat without feedback — on a timer, on a fresh request, on an unrelated proposal. What it cannot do without feedback is respond to what the last iteration did: the consequences of retained changes have to reach later search or evaluation, through tests, usage traces, incidents, human observation, or revised criteria. Feedback is a condition on learning from the loop, not on running it.

Retained design rationale is one such channel. Recorded constraints and rejected alternatives can narrow later search, while prior evidence can explain why an evaluator once accepted a choice. The record neither establishes that the same oracle remains adequate after the environment, criteria, or risk posture changes nor affects the loop unless a later consumer reads it. [Design rationale management in Commonplace](../reference/design-rationale-management.md) documents this useful but non-mechanical retention path.

## Boundary cases clarify the claim

Cybernetician W. Ross Ashby's ultrastable system sits exactly on the subtype's boundary, and is not reflective. His electromechanical Homeostat varies parameters randomly when essential variables leave viable bounds, tests whether viability returns, and preserves a surviving configuration through non-displacement — readable as search, evaluation, and operative retention in their weakest viable forms, with no self-representation anywhere in the mechanism ([Ashby 1960, chapters 7–8](../sources/ashby-design-for-a-brain-ultrastability.md)).

It is a real instance, not a defective one, and it establishes that **reflection is not a premise of the decomposition** — the three functions are exhibited without appeal to a self-representation. It also marks the floor. Each function is present in its weakest viable form: search is a draw from a random-number table bearing no relation to the problem, evaluation is a one-bit viability test that ranks nothing, and retention is equilibrium — a configuration survives because nothing is left to displace it, not because anything endorsed it. Reading the Homeostat is therefore the cheapest way to see what a stronger generator and a real oracle actually buy.

The same machine also shows why the subtype boundary is a reading, not a component list. Nothing in the Homeostat separately represents a candidate, and nothing in it *is* an evaluator — the viability criterion is what the physical dynamics respond to. Described one way it is a minimal proposal-selection loop; described the other it is direct viability-driven adaptation, the non-loop way a [self-improving system](./definitions/self-improving-system.md) can be responsive to evidence. Both descriptions are faithful, because the improvement criterion a self-improving system needs is semantic, and the explicit evaluator is required only by the architecture this note describes. Systems above the floor come apart cleanly: a Gödel machine has an evaluator you can point to; a gradient learner has none — [online gradient descent](https://dl.acm.org/doi/10.5555/3041838.3041955) adopts every step the revealed cost dictates, and its no-regret guarantee holds without any gate (Zinkevich 2003).

What the Homeostat's floor does not buy is accumulation. What it retains is an opaque parameter setting rather than a representation, so nothing in the mechanism can read what it kept and the loop runs indefinitely without anything compounding. Routing the loop through a self-representation is what addresses that gap — it makes each retained change *addressable* by the next round, which is not the same as guaranteeing it is read. That is the subject of [reflection buys addressability, not compounding](./reflection-buys-addressability-not-compounding.md); evidence-responsive operative change to the system's own organization, with or without that routing and with or without the gate, is what makes a [self-improving system](./definitions/self-improving-system.md).

At the formal extreme, [Gödel machines](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) are proof-governed self-rewriting systems whose acceptance rule can govern changes to the rule-governed machinery itself. Their meta-level closure depends on proving a target theorem relative to axiomatized hardware, environment, and utility models ([Schmidhuber 2003](../sources/goedel-machines-schmidhuber.ingest.md)). A fallible evaluator may still estimate downstream consequences, but it does not inherit that guarantee.

## What the decomposition claims

The three functions are analytically separable, not architecturally separate. One process may perform several of them — a maintainer who notices a problem, drafts the fix, and merges it performs all three — and evaluation may run before a candidate becomes operative or after. The decomposition specifies what the loop must accomplish, not a sequence, a component diagram, or a division of labour. Its use is diagnostic: when a loop stalls, ask which of the three is missing rather than which component failed.

The status claimed here matches how the neighboring self-adaptive-systems field treats its own loop models: MAPE-K and its relatives are presented as reference models for *engineering* adaptation, not as the definition of it ([Weyns, Software Engineering of Self-Adaptive Systems](https://people.cs.kuleuven.be/~danny.weyns/papers/2017HSE.pdf)), and a systematic review of that literature finds no settled formal definition from which any single loop architecture would follow ([Petrovska, Erjiage, and Kugele 2025](https://arxiv.org/abs/2505.17798)). The proposal-selection decomposition is offered in the same spirit — a conceptual model of one architecture, with the [category membership question](./definitions/self-improving-system.md) settled elsewhere.

## Open Questions

- Whether search reach can be measured or bounded for a socio-technical loop in the way oracle strength can be graded.
- Whether a fallible evaluator can govern changes to its own acceptance criteria without either an external criterion or the axiomatization that buys formal closure.

---

Relevant Notes:

- [Reflective system](./definitions/reflective-system.md) — contrasts: reflection is structural and supplies one causal path into the loop; neither property implies the other
- [False-positive generation is filtered; false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — extends: the two functions fail asymmetrically because evaluation is the terminal filter
- [Actionable methodology](./definitions/actionable-methodology.md) — grounds: the operator, available operations, and setting that make a criterion usable in the loop
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — extends: asks whether a system's methodology governs changes to its own change process
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — exemplifies: realizes the three functions under a formal acceptance gate
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidence: traces the functions through an observed repository change loop
- [Schmidhuber, Gödel Machines](../sources/goedel-machines-schmidhuber.ingest.md) — evidence: supplies the proof-governed limit case
- [Self-improving system](./definitions/self-improving-system.md) — grounds: the base category this loop is a named subtype of — membership requires evidence-responsive operative change, not the gate architecture
- [Reflection buys addressability, not compounding](./reflection-buys-addressability-not-compounding.md) — extends: what routing the loop through a self-representation adds to bare retention
- [Ashby, Design for a Brain — ultrastability](../sources/ashby-design-for-a-brain-ultrastability.md) — evidence: the boundary case — the three functions at their weakest viable forms with no self-representation and no explicit evaluator, marking both the floor of each function and the edge of the subtype
