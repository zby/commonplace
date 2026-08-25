---
description: One result-only check can warrant retaining an episode as evidence, but abstracting its explanation also needs evidence about a faithful producing process and an explicit scope boundary
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, agent-memory]
---

# A checked outcome licenses retaining an episode, not abstracting its explanation

[Trace-extracted memory](./trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) turns trace records into progressively more authoritative memory by testing a diagnosis or causal story against evidence before promoting it. This note extends that ladder to result-checked successful as well as failed episodes. The checker at the verify rung is an oracle. What the oracle checks determines what the episode can support.

Two targets matter. An **outcome check** asks whether the final result met its target. A **process check** asks whether the claimed route was valid and faithfully represented what produced the result. The two checks support different claims.

## One outcome underdetermines the producing process

A result-only checker can accept the right answer reached by a wrong or coincidental route: a lucky guess, a spurious shortcut, or two errors that cancel. All produce the same observed success. The final result does not distinguish among them.

This distinction is empirically testable. The [VAIR analysis](../sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.ingest.md) holds answer correctness fixed while inserting invalid reasoning, then measures whether evaluators notice the broken route. Answer correctness and reasoning validity can diverge because they are different targets.

## What a single checked outcome licenses

A result-only pass can warrant **retaining the episode as evidence or a demonstration**. It licenses only a case-level claim: “this produced the target result in the recorded episode.” It does not guarantee that executing the actions again will be safe or reproducible. Mutable state, non-idempotent actions, and [execution indeterminism](./execution-indeterminism-is-a-property-of-the-sampling-process.md) can make nominally similar reruns behave differently.

Abstracting the episode's explanation makes two stronger claims. A rule such as “do X because Y” asserts that Y was part of the process that produced the result and that Y remains relevant beyond the recorded case. An outcome check tests neither claim. Moving from the episode to the explanatory rule therefore requires evidence about a faithful producing process and a [statable boundary](./abstract-an-experience-only-when-you-can-state-the-boundary.md) for where the explanation transfers.

This is a ceiling on the evidence from one episode, not on every reusable rule. Repeated, varied, or exhaustive outcome tests can warrant an extensional rule over a declared domain without identifying its mechanism. That evidence supports “this mapping holds across the tested domain,” not an explanation abstracted from one success.

## Process evidence must be faithful

Checking a submitted sequence for locally valid steps does not show that those steps produced the answer. A system can use a shortcut and then emit a coherent post-hoc rationale. Controlled interventions in [language models' chain-of-thought](../sources/language-models-dont-always-say-what-they-think.ingest.md) show that reported reasoning can omit a feature that caused the answer.

Process evidence must therefore connect the inspected artifact to the route that actually produced the result. A faithful trace can provide that connection. So can an intervention that tests a candidate mechanism's causal role. By contrast, an evaluator that reconstructs a valid route to the same answer has performed [reasoning production, not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md). Evidence of a valid and faithful process is necessary for abstracting an episode's explanation, but it is not sufficient until the transfer boundary is also stated.

## Check target and checker strength are independent

The [oracle-strength spectrum](./oracle-strength-spectrum.md) grades how cheaply and reliably a checker discriminates. Outcome versus process identifies the proposition the checker tests. A deterministic end-to-end test can be a hard outcome checker without identifying the producing route. A process-directed checker can still be soft or inaccurate. Reliability does not change the target of the check.

## Scope

The claim concerns an explanation abstracted from one bounded episode. It does not cover extensional rules with complete outcome coverage, policies validated across a declared distribution, or exact specifications in which the final outcome is the entire target. Those can earn authority without inspection of an internal trace.

For explanatory rules learned from sparse cases, faithful process evidence remains necessary but not sufficient: the learner must also state where the mechanism stops. Retaining a checked episode stays below that abstraction threshold. It does not by itself authorize literal re-execution.

---

Relevant Notes:

- [trace-extracted memory earns authority per operation, not at capture](./trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) — extends: identifies the weaker episode-level authority an outcome check can supply and the stronger evidence needed for abstraction
- [abstract an experience into a lesson only when you can state where the lesson stops](./abstract-an-experience-only-when-you-can-state-the-boundary.md) — mechanism: process evidence supplies one prerequisite for abstraction; the boundary supplies another
- [first-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: a checked mechanism can carry explanatory reach beyond the case that produced it
- [diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) — grounds: inspectable intermediate evidence gives a process-directed checker something to test
- [an accepted edit verifies the change, not the rule](./an-accepted-edit-verifies-the-change-not-the-rule.md) — extends: applies the episode-versus-rule authority boundary to human-accepted edits
- [reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md) — extends: shows how an evaluator can confirm an answer by inventing a route instead of checking the submitted one
- [execution indeterminism is a property of the sampling process](./execution-indeterminism-is-a-property-of-the-sampling-process.md) — contrasts: retaining a successful episode does not guarantee that rerunning it reproduces the outcome
