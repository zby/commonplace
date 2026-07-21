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

A terminology note: the concept descends from Ashby's **adaptation** — his ultrastable system, examined below, is the conceptual ancestor even though it classifies outside the subtype — but it is named for what the loop aims at rather than by his word for it. Everyday adaptation is transient compensation, an eye adjusting to the dark, and retains nothing; retention is one of the three requirements. Where this note says *adaptation* or *adaptive*, it means Ashby's phenomenon. The architecture described here is named **proposal-selection** throughout.

A [reflective system](./definitions/reflective-system.md) supplies one possible causal path into this loop. Through **intercession** — an operation that changes the system through its causally connected self-representation — it can modify a represented aspect of itself. Making that path available does not itself provide search, evaluation, or retention.

## Search determines what enters consideration

Search brings an unrealized change under consideration. It may include:

- detecting a problem, opportunity, or adaptation signal;
- selecting the aspect and operation to change;
- generating one or more candidates;
- allocating effort and deciding when to stop or escalate.

At minimum, search must produce a candidate from a space in which other possible changes remain unrealized. It need not compare several candidates at once or operate autonomously. A maintainer may choose the problem, a model may draft a candidate, and a script may enumerate alternatives within one declared socio-technical loop. Assigning those functions establishes the loop's boundary; it does not make the loop reflective.

Search range and evaluation strength are independent limits:

> Evaluation cannot select a candidate that search never reaches.

A strong verifier can improve judgments within a narrow generator's range, but it cannot expand that range. [Automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) gives one concrete search space—extract, split, synthesize, relink, regroup, reformulate, retire—whose judgment-heavy parts remain substantially human-driven.

## Evaluation determines which changes may remain operative

Evaluation applies criteria to a proposed or already actualized change. Its result must be able to affect selection, rollback, or continued retention. Evaluation is non-vacuous only if some possible result permits rejection: an unconditional trigger is not an evaluator merely because it precedes a transition, and a conditional trigger whose only effect is to launch the next variation is not one either. The verdict must control an operation distinct from producing the next candidate — select, discard, block, roll back — so that rejecting a change and merely changing again are different events in the mechanism.

**Oracle** is shorthand for the component or procedure that supplies the evidence or judgment. It may be a proof system, test, validator, empirical measurement, rubric, model evaluator, human review, or some combination. The [oracle-strength spectrum](./oracle-strength-spectrum.md) grades these mechanisms, while [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) explains why constructing an adequate oracle is often harder than generating candidates.

Any judgment remains scoped to what the check establishes. An oracle may accept a candidate under specified criteria without establishing that the change is globally beneficial. Search and evaluation may be performed by the same person or process, but they fail in different ways and improve by different means. They are analytically separable rather than independent: automating one changes the load on the other.

## Operative retention makes the change consequential

Acceptance alone does not make a change consequential. Operative retention combines persistence with an authority path through which the retained result can affect later behavior. In [behavioral authority](./definitions/behavioral-authority.md) terms, the change needs a **consumer**, a **channel**, and a **force**.

- A reviewed note that no future reader or prompt-assembly step loads has no consumer.
- An approved patch that is never merged has no channel.
- A generated validator that no command invokes has no force.

In each case, search ran and evaluation passed, but the proposal-selection loop remained open: the artifact exists without becoming behaviorally consequential.

Artifact labels do not decide whether retention is operative. A knowledge artifact consumed as evidence or advice can affect later behavior, while a nominal system-definition artifact with no consumer cannot. The test is the [behavioral-authority](./definitions/behavioral-authority.md) path: consumer, channel, and force relative to the objective and declared horizon.

For self-improvement, the accepted change must reach the system's own [behavior-determining organization](./definitions/behavior-determining-organization.md). Promotion into instruction, enforcement, or configuration is one way to strengthen that path, and may itself run as another proposal-selection instance — [the two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) develops that promotion architecture, with recurrence as the trigger, pre-promotion verification as the gate, and methodology growth plus a coverage-test update as retention — but it is not universally required for reflective or operative change.

## Repetition does not establish cumulativity

A proposal-selection loop can repeat on a timer or fresh request without using anything retained by an earlier iteration. Whether later improvement consumes or preserves earlier improvement-relevant information is **cumulativity**, whose criterion and counterexamples belong to the [pathway profile](./a-self-improving-system-needs-a-profile-not-a-ladder.md). Retained rationale can provide that dependence when later search or evaluation actually consumes it; [design rationale management in Commonplace](../reference/design-rationale-management.md) documents that path.

## Boundary cases clarify the claim

Cybernetician W. Ross Ashby's ultrastable system marks the subtype's edge from just outside it, and its exclusion follows from the evaluation criterion above, not from a missing component. The electromechanical Homeostat has exactly one evidence-responsive transition: when essential variables leave viable bounds, the parameters jump to new random values ([Ashby 1960, chapters 7–8](../sources/ashby-design-for-a-brain-ultrastability.md)). That single jump both discards the incumbent configuration and produces its successor — rejection is not an operation distinct from generation — and a configuration that restores viability persists through equilibrium, with nothing whose function is to accept it. The functions collapse into one trigger, so under the definitions here the machine is a non-reflective, **direct viability-driven** [self-improving system](./definitions/self-improving-system.md), not an instance of this subtype.

What the Homeostat does admit is a functional variation–selection–retention reading: configurations vary, viability determines whether variation continues, and the survivor persists through non-displacement. That reading is an analyst's reconstruction, not architecture, and its value is to mark the floor of each function — search as a draw from a random-number table bearing no relation to the problem, evaluation as a one-bit viability boundary that ranks nothing, retention as equilibrium, a configuration surviving because nothing is left to displace it. Read this way, the Homeostat is the cheapest demonstration of what a stronger generator and a real oracle actually buy. Reflection is still not a premise of the decomposition. An evolutionary strategy supplies the genuine non-reflective instance: it runs an explicit generate-and-select loop over parameters nothing inside it can read.

The Homeostat's contrast with a gated system is architectural, not a difference of gate strength: a gradient learner has no evaluator either — [online gradient descent](../sources/zinkevich-online-convex-programming.md) adopts every step the revealed cost dictates, with no accept/reject anywhere (Zinkevich 2003) — and Zinkevich's Greedy Projection/GIGA result supplies the technical counterexample to treating an acceptance gate as universal. The Homeostat stands with it, on the excluded side of the boundary just drawn. [Gödel machines](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) sit inside the subtype at its formal extreme, a proof-mediated gate rather than none at all; that architecture is developed in their own note.

Reflection is a separate axis from this exclusion: the Homeostat is also non-reflective, and [what that costs is addressability, not category membership](./reflection-buys-addressability.md) — evidence-responsive operative change to the system's own organization, with or without a self-representation and with or without a gate, is what makes a [self-improving system](./definitions/self-improving-system.md).

## What the decomposition claims

The three functions are analytically separable, not architecturally separate. One process may perform several of them — a maintainer who notices a problem, drafts the fix, and merges it performs all three — and evaluation may run before a candidate becomes operative or after. Co-location has a floor, though: the functions must remain causally distinguishable even when one process performs them — rejection, in particular, must be an event distinct from the arrival of the next candidate. Where they collapse into a single evidence-triggered transition, as in the Homeostat, the loop is not weakly present; it is absent, and the pathway is direct. The decomposition specifies what the loop must accomplish, not a sequence, a component diagram, or a division of labour. Its use is diagnostic: when a loop stalls, ask which of the three is missing rather than which component failed.

The status claimed here matches how the neighboring self-adaptive-systems field treats its own loop models: MAPE-K and its relatives are presented as reference models for *engineering* adaptation, not as the definition of it ([Weyns, Software Engineering of Self-Adaptive Systems](../sources/weyns-software-engineering-self-adaptive-systems-tour.md)), and a systematic review of that literature finds no settled formal definition from which any single loop architecture would follow ([Petrovska, Erjiage, and Kugele 2025](../sources/defining-self-adaptive-systems-systematic-literature-review.md)). The proposal-selection decomposition is offered in the same spirit — a conceptual model of one architecture, with the [category membership question](./definitions/self-improving-system.md) settled elsewhere.

## Open Questions

- Whether search range can be measured or bounded for a socio-technical loop in the way oracle strength can be graded.
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
- [Reflection buys addressability](./reflection-buys-addressability.md) — extends: what routing the loop through a self-representation adds to bare retention
- [Ashby, Design for a Brain — ultrastability](../sources/ashby-design-for-a-brain-ultrastability.md) — evidence: the contrast case just outside the subtype — its one evidence-responsive transition collapses rejection into generation, while its functional reconstruction marks the floor of each function
- [Behavioral authority](./definitions/behavioral-authority.md) — grounds: the consumer/channel/force vocabulary the two force families specialize
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — mechanism: the developed architecture of retention-strengthening promotion — recurrence as trigger, verification as reject-capable gate, coverage-test update as retention
