---
description: "A governed adaptation loop needs search to produce a candidate, evaluation that can reject it, and operative retention; reflection supplies only one causal path into that loop"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [foundations, computational-model, self-improving-systems]
---

# Governed adaptation requires search, evaluation, and operative retention

A governed adaptation loop requires three functions: **search** brings a candidate change into consideration, **evaluation** supplies grounds for accepting or rejecting it, and **operative retention** preserves an accepted change with behavioral authority. Remove any one and the loop does not close — a change nobody proposed, nobody could reject, or nobody will ever act on.

Governed adaptation is therefore narrower than self-modification. A blind, accidental, or unconditional rewrite may change later behavior without applying any criterion; a transient rewrite may fail to preserve the result. Both can count as self-modification, but neither completes a governed adaptation loop. Conversely, the three functions can organize adaptation in a system that is not reflective.

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

Any judgment remains scoped to what the check establishes. An oracle may accept a candidate under specified criteria without establishing that the change is globally beneficial. Search and evaluation may be performed by the same person or process, but they fail independently and improve by different means.

## Operative retention makes the change consequential

Acceptance alone does not make a change consequential. Operative retention combines persistence with an authority path through which the retained result can affect later behavior. In [behavioral authority](./definitions/behavioral-authority.md) terms, the change needs a **consumer**, a **channel**, and a **force**.

- A reviewed note that no future reader or prompt-assembly step loads has no consumer.
- An approved patch that is never merged has no channel.
- A generated validator that no command invokes has no force.

In each case, search ran and evaluation passed, but the adaptation loop remained open: the artifact exists without becoming behaviorally consequential.

## Feedback informs later iterations

For adaptation to repeat, consequences of retained changes must reach later search or evaluation through tests, usage traces, incidents, human observation, or revised criteria.

Retained design rationale is one such channel. Recorded constraints and rejected alternatives can narrow later search, while prior evidence can explain why an evaluator once accepted a choice. The record neither establishes that the same oracle remains adequate after the environment, criteria, or risk posture changes nor affects the loop unless a later consumer reads it. [Design rationale management in Commonplace](../reference/design-rationale-management.md) documents this useful but non-mechanical retention path.

## Boundary cases clarify the claim

Cybernetician W. Ross Ashby's ultrastable system is a governed adaptation loop that is not reflective. His electromechanical Homeostat varies parameters randomly when essential variables leave viable bounds, tests whether viability returns, and preserves a surviving configuration through non-displacement — search, evaluation, and operative retention, with no self-representation anywhere in the mechanism ([Ashby 1960, chapters 7–8](../sources/ashby-design-for-a-brain-ultrastability.md)).

It is a real instance, not a defective one; it is simply not the kind of system this KB is built to reason about. Its interest here is evidential: it shows that **reflection is not a premise of the decomposition**. The three functions are established without appeal to a self-representation, which is why the claim is stated for governed adaptation rather than restricted to reflective systems. The reflective case is the one everything downstream develops.

At the formal extreme, [Gödel machines](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) are proof-governed self-rewriting systems whose acceptance rule can govern changes to the rule-governed machinery itself. Their meta-level closure depends on proving a target theorem relative to axiomatized hardware, environment, and utility models ([Schmidhuber 2003](../sources/goedel-machines-schmidhuber.ingest.md)). A fallible evaluator may still estimate downstream consequences, but it does not inherit that guarantee.

## What the decomposition claims

The three functions are analytically separable, not architecturally separate. One process may perform several of them — a maintainer who notices a problem, drafts the fix, and merges it performs all three — and evaluation may run before a candidate becomes operative or after. The decomposition specifies what the loop must accomplish, not a sequence, a component diagram, or a division of labour. Its use is diagnostic: when a loop stalls, ask which of the three is missing rather than which component failed.

## Open Questions

- Whether search reach can be measured or bounded for a socio-technical loop in the way oracle strength can be graded.
- Whether a fallible evaluator can govern changes to its own acceptance criteria without either an external criterion or the axiomatization that buys formal closure.

---

Relevant Notes:

- [Reflective system](./definitions/reflective-system.md) — contrasts: reflection is structural and supplies one causal path into the loop; neither property implies the other
- [Search errors are filtered; evaluation errors are retained](./search-errors-are-filtered-evaluation-errors-are-retained.md) — extends: the two functions fail asymmetrically, because evaluation is the terminal filter and its errors are the permanent ones
- [Actionable methodology](./definitions/actionable-methodology.md) — grounds: the operator, available operations, and setting that make a criterion usable in the loop
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — extends: asks whether a system's methodology governs changes to its own change process
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — exemplifies: realizes the three functions under a formal acceptance gate
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidence: traces the functions through an observed repository change loop
- [Schmidhuber, Gödel Machines](../sources/goedel-machines-schmidhuber.ingest.md) — evidence: supplies the proof-governed limit case
- [Ashby, Design for a Brain — ultrastability](../sources/ashby-design-for-a-brain-ultrastability.md) — evidence: a governed adaptation loop with no self-representation, establishing that reflection is not a premise of the decomposition
