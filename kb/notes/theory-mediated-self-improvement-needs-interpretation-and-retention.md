---
description: "Reflective self-improvement inherits the theory-mediated sample-efficiency conjecture only where one substrate both interprets a theory about the system's own operation and retains it addressably"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Theory-mediated self-improvement needs both interpretation and retention from one substrate

[Theory-mediated learning may improve sample efficiency under structured shifts](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) is indifferent to what its theories are about. A learner retaining a theory of how a market moves or what makes a build fail gets whatever the conjecture offers. Reflective self-improvement is the case where the retained theory is about the system's own operation and participates in the [causally connected self-representation](./definitions/reflective-system.md) through which the system changes its own behavior.

That case does not inherit the conjecture automatically. It inherits it under three conditions, and the third is where most substrates fail:

1. **Membership.** The theory participates in the self-representation. Explicit domain knowledge can transfer beautifully without making any improvement pathway reflective — transfer is not reflection.
2. **Interpretation.** Something inside the boundary can say what the theory claims, derive its consequences, and judge whether its reach is genuine — [reach-assessment](./definitions/reach-assessment.md) applied to a theory about the system itself. [Reflection buys addressability](./reflection-buys-addressability.md), and addressability is a handle, not a judgment.
3. **Retention with separable parts.** The theory persists as an object whose content, assumptions, and applicability conditions are separately accessible, so that a failure can rescope it rather than only delete it.

Interpretation and retention are the pair that has to come from somewhere. A system satisfying membership and retention but not interpretation revises confidently in the wrong direction; one satisfying membership and interpretation but not retention re-derives its theory every episode and cannot accumulate.

## Self-directed theories arrive unformalized

Interpretation and retention could in principle be sourced separately and composed. In practice, what a system can say about its own operation resists the move that would make composition easy.

A formal pathway gets both cheaply inside a supplied language, because [formalization buys a mechanical acceptance test](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — and pays for it with a language, variables, primitives, and acceptance criteria fixed in advance.

Theories about a system's own operation are mostly not yet in such a language. "This retrieval step surfaces the wrong artifact when the query names a type rather than a topic" is a claim about the system, with real consequences and a real scope, and no formal apparatus receives it. So the mechanical acceptance test is unavailable exactly where the reflective case needs one, and condition 2 has to be discharged over prose.

## Only a semantic interpreter over retained text supplies both

This is why the substrate matters rather than the architecture diagram. [Purely parametric retention exposes no scope](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md), and the documented partial routes out of that fail differently but fail alike here: neither yields a self-directed theory that persists with its applicability conditions attached. Formal retention supplies both conditions inside a language the reflective case rarely has.

An LLM operating over retained text supplies both, and does so by division of labor: the weights are the semantic interpreter, competent over prose theories including prose about the system's own behavior; the retained artifact is the persistent, separately revisable object. Neither half is sufficient. A capable model with no retained artifact re-derives its theory each session — [and a theory nothing surfaces at the moment of need contributes nothing](./retrieval-failure-is-reflection-failure.md). A retained artifact with no interpreter is a table of rules that reasons about nothing.

So the conjecture reaches reflective self-improvement on LLM-plus-artifact substrates specifically, not on reflective systems in general. That is a claim about what is currently available, not about what is possible: any substrate that supplied semantic competence over its own unformalized self-descriptions and retained them addressably would qualify equally.

## The retention half is what scale might absorb

The bitter lesson is not an objection to theory-mediated learning, [since what scale selects against is unearned reach rather than structure](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md). But it does bear on the division of labor above. If a sufficiently scaled model runs the same theory search implicitly in activations, with reach-assessment and revision happening inside a forward pass, then the retained artifact is scaffolding that compensates for a context window rather than a load-bearing part of the pathway. On that reading, condition 3 is a temporary engineering fact and the externalized theory disappears.

Nothing here rebuts that. What it predicts is where to look: the artifact earns its place only where persistence across sessions, selective rescoping of a *named* theory, and inspection by a process other than the one that formed it are doing work that a longer context would not do.

## Open Questions

- Whether satisfying the three conditions without a human is enough. Structurally it is already done: [Exo](../agentic-systems/exo.md) edits its own prompts, tools, and executor, rebuilds, and restarts, with the source it edits being the organization that determines its behavior — so the conditions do not need the [Gödel machine](./goedel-machines-are-a-proof-governed-case-of-self-modification.md), still unimplemented, or [Commonplace](../reference/commonplace-as-a-reflective-system.md), which runs but is human-inclusive. What a running instance does not settle is condition 2 at strength: Exo's acceptance oracles are build success, tests, and observed behavior after restart, which reject a change that breaks and admit one that merely reasons worse. Whether anything in such a loop is assessing reach, rather than proposing changes that fail to crash, is the open part.
- Whether the closure question was ever the interesting one. It framed the human as the thing to remove, when what the human was supplying is the evaluator — [methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md), and a loop can close computationally while its acceptance gate gets weaker.
- Whether a deliberately minimal toy pathway, built to be reflective and computationally closed from the start and sized to test the conjecture rather than to be useful, stays autonomous end to end — or whether the human reappears at a different point, designing its objective or judging its results.
- Whether self-directed theories are harder to reach-assess than domain theories, since the system evaluating the theory is the system the theory describes, and a flattering self-theory has no external oracle to contradict it.
- Whether condition 3's separable parts can be had at all in prose, or whether prose theories are addressable only as indivisible documents — replaceable but not rescopable — which would collapse the advantage over wholesale replacement.

---

Relevant Notes:

- [Theory-mediated learning may improve sample efficiency under structured shifts](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — grounds: the general conjecture this note specializes, including its test design and cost ledger
- [Reflective system](./definitions/reflective-system.md) — defined-in: the causally connected self-representation condition 1 requires
- [Self-improving system](./definitions/self-improving-system.md) — defined-in: the reflective/non-reflective distinction the specialization runs along
- [Reach-assessment](./definitions/reach-assessment.md) — defined-in: the capability condition 2 names, applied to a theory about the system itself
- [Reflection buys addressability](./reflection-buys-addressability.md) — grounds: the affordance that supplies condition 3's handle without supplying condition 2's judgment
- [Reflection makes retained lessons second-order: a lesson can reject or rescope a prior commitment](./reflection-makes-retained-lessons-second-order.md) — mechanism: the explicit operations on a represented prior theory that selective rescoping needs
- [Retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md) — mechanism: why retention without surfacing contributes nothing
- [Representational form](./definitions/representational-form.md) — defined-in: the axis along which the substrate's two halves divide
- [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](./formal-systems-assess-explanatory-reach-through-causal-and-proof.md) — grounds: what a supplied formal language buys and costs
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — evidence: the formal instance that satisfies the conditions inside an axiomatized language, unimplemented
- [Methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md) — grounds: why reflective membership does not establish the closure a test would need
- [Commonplace as a reflective self-improving system](../reference/commonplace-as-a-reflective-system.md) — evidence: the closest running instance, with human, joint, and computational functions explicitly located
- [Exo](../agentic-systems/exo.md) — evidence: a running system satisfying the three conditions without a human, whose acceptance oracles reach liveness but not reach
