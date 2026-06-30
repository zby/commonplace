---
description: Outcome and process verification are two verify-rung oracles — an outcome check licenses replaying an instance, not distilling a rule, since only a process check inspects the generalizing mechanism
type: kb/types/note.md
traits: [title-as-claim]
status: seedling
tags: [learning-theory, agent-memory]
---

# An outcome check licenses replay; a rule needs the process verified

The verify rung of [trace-derived memory](./trace-derived-memory-earns-authority-per-operation-not-at-capture.md) needs "an oracle that can discriminate a correct diagnosis from a plausible-but-wrong one" — but leaves open *what* the oracle checks. There are two choices, and they are different oracles. An **outcome check** asks whether the final answer came out right. A **process check** asks whether the intermediate steps held — whether the answer was reached for a reason that survives inspection. They pass different things, and the difference decides which rung an artifact can climb to.

## Outcome checks admit the right answer for the wrong reason

An outcome oracle has a characteristic false positive: the right answer reached by a wrong or coincidental route — a lucky guess, a spurious shortcut, two errors that cancel. The check fires "correct," but the route that produced the answer is unexamined. A process check spends its discrimination on exactly that route, so it catches failures an outcome pass waves through. This is why integrating step-level process rewards with outcome rewards [outperforms outcome-only training](../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md): the process signal rejects trajectories that an outcome signal, seeing only the final state, would reinforce.

## What each oracle licenses

The two checks license different *uses* of the verified episode, and the uses correspond to the two rungs above verify:

- A success that passed only an outcome check is safe to **replay verbatim in the same context**. The claim is just "this produced the right result here," and replay re-runs *here* — claim and use match. This is the success preserved as a [concrete, replayable demonstration](./abstract-an-experience-only-when-you-can-state-the-boundary.md) rather than a rule.
- **Distilling a rule** transfers the mechanism to new contexts: a rule asserts "do X because Y." An outcome check never inspected Y, so it cannot tell a real mechanism from a coincidence — and the coincidence is precisely the part that fails to transfer. Only a process check verifies the *why*, and the why is what [carries past the original case](./first-principles-reasoning-selects-for-explanatory-reach-over.md).

So the verify and distill rungs do not merely "have different oracles" in the abstract; the distill rung specifically requires a *process* oracle. An outcome oracle, however hard, can climb fail→verify for replay but cannot license verify→distill. Generalizing a rule off an outcome check is over-generalization at its root — it stamps rule authority on a correlation whose mechanism was never checked.

## This is a what-you-check axis, orthogonal to oracle hardness

The [oracle-strength spectrum](./oracle-strength-spectrum.md) grades oracles by how cheaply and reliably they check, hard to soft. Process-versus-outcome is a different axis: *what* the check inspects. A hard outcome oracle (a passing end-to-end test) and a hard process oracle (a checker over the steps) can both be cheap and deterministic yet license different things. Hardening along the strength axis does not convert an outcome check into a process check — you have to inspect the steps, which costs more and is often itself a soft oracle: a process reward model's accuracy across modalities is typically assumed, not measured. Process verification buys the right *kind* of discrimination, not necessarily a strong amount of it.

## Scope

Process verification makes a lesson's basis articulable; it does not by itself produce a [statable boundary](./abstract-an-experience-only-when-you-can-state-the-boundary.md) — verifying the mechanism is necessary for a trustworthy rule, not sufficient, and you still have to say where the rule stops. Where the task is an exact spec — the outcome *is* the thing wanted, with no hidden mechanism to generalize — the gap narrows: right-answer-wrong-reason still blocks generalization but not replay. The claim bites wherever a rule will be applied outside the context that produced it, which is the whole point of distilling one.

---

Relevant Notes:

- [trace-derived memory earns authority per operation, not at capture](./trace-derived-memory-earns-authority-per-operation-not-at-capture.md) — extends: names which oracle the distill rung requires — a process check, not an outcome check — sharpening that note's "the operations have different oracles"
- [abstract an experience into a lesson only when you can state where the lesson stops](./abstract-an-experience-only-when-you-can-state-the-boundary.md) — mechanism: process verification is the verify-side operation that makes a boundary statable; this note supplies the oracle that note's distil step assumes
- [first-principles reasoning selects for explanatory reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: the mechanism (the why) is what has reach, so checking the process is what earns a lesson its transfer
- [oracle-strength spectrum](./oracle-strength-spectrum.md) — contrasts: strength (how cheaply you check) is orthogonal to what-you-check (outcome vs process); a hard oracle can still be the wrong kind for distillation
- [diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) — grounds: inspectable intermediate steps are the evidence a process check consumes; without them only an outcome check is available
- [trace-derived learning techniques in related systems](../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) — evidence: OpenClaw-RL's process + outcome reward integration outperforms outcome-only on general agentic tasks
