---
description: "Defines the writing-is-thinking filter as commit, challenge, and respond operations; argues a human-agent loop can split them across roles, explains which composition-exposed errors LLM reviewers miss, and bounds what one trace proves."
type: types/note.md
traits: [title-as-claim, synthesis, has-external-sources]
tags: [foundations]
---

# A human-agent critique loop can relocate the error-exposure operations of solo composition

Writing an argument out by hand can expose errors that thinking about it did not. A goal that seemed coherent splits into incompatible parts once it has to be stated exactly. A "because" turns out to have no reason behind it. This note calls that effect the **writing-is-thinking filter** and defines it by the operations that produce it, not by who performs them.

The claim is that these operations can be split across roles in a loop where a human and an LLM agent draft, challenge, and decide, with each handoff recorded. It is an existential claim: one case in which the recorded loop demonstrably corrected an artifact witnesses it. It does not claim that such a loop is reliable, or that it exposes errors as well as a person writing alone. Those are comparative claims, and no comparative evidence is supplied here.

## The filter, defined by its operations

Three essays describe how writing exposes weak thinking: [putting ideas into words](../sources/putting-ideas-into-words.ingest.md), [thinking through conjecture and counterexample](../sources/how-to-think-in-writing.ingest.md), and [learning by iterated writing](../sources/learning-by-writing.ingest.md). They report practice rather than controlled comparisons. Across them, writing does three things: it fixes a commitment in words, it locates a weakness in that commitment or its support, and it revises or discards the commitment. This note turns that sequence into three recordable operations:

- **Commit-and-expose** records the claim before it is accepted, together with its constraints, its premises, and the inferential route from premises to claim.
- **Challenge-and-locate** records objections tied to specific premises, counterexamples, missing support, and a proposed location of the fault. It does not record a global grade.
- **Respond-and-decide** records a status for every challenge. *Investigate* is an interim status. A final disposition does one of four things: it rejects the challenge with cited support, revises or narrows the claim, rejects the claim, or accepts the claim with its uncertainty stated explicitly.

The operations target three kinds of error that composition by hand tends to expose:

1. **Incompatible goals.** The claim wants several properties at once, and stating it exactly shows that no single version has them all.
2. **Unsupported steps.** A stated reason does not carry the conclusion it is offered for. In solo writing this can appear as a stall at the weak connective, as [LLM generation can hide a relaxed goal where human writing exposes a stall](./llm-generation-relaxes-goals-where-human-writing-stalls.md) describes.
3. **Omitted distinctions.** A writer composing a sentence must decide on qualifications and cases that a reader of a finished sentence never sees raised.

The derivation from the essays motivates the three operations. It does not show that the operations, once split across roles, keep the effects the essays report. The taxonomy is one candidate, neither canonical nor validated.

## How a loop relocates the operations

In solo composition one person performs all three operations, often without separating them. A loop gives them to roles. A **reviewer** performs challenge-and-locate. An **acceptor** performs respond-and-decide and has the authority to admit the artifact. Either role may be filled by a human, an agent, or a policy, but each allocation needs its own warrant, since [human analogies suggest functions, not component boundaries](./human-analogies-suggest-functions-not-component-boundaries.md). Testing an allocation also requires recording who or what filled each role and under what conditions.

Keeping the claim as committed, the challenge report, and the disposition makes every handoff inspectable. Contrast **naive prose delegation**: a person supplies a seed idea, an LLM writes the prose, and the person accepts it after a global read or approval. That workflow keeps no record of any operation, so it cannot support the checks below. Rendering, transcription, and stylistic editing are outside this claim when the substantive commitments and checks are fixed elsewhere.

## Why LLM reviewers catch some of these errors and miss others

Relocation works only if the reviewer actually finds the errors that composition would have exposed. Reading a text is a different task from writing it, and the difference explains where an LLM reviewer is likely to fail.

**The text carries no marker at the fault.** A writer who reaches an unsupported step may stall there, and the stall points to the fault. A generator produces fluent prose whether or not it met every constraint, and [generation confidence does not by itself certify soundness](./generation-confidence-does-not-by-itself-certify-soundness.md). The reviewer therefore receives a text whose weak steps read as smoothly as its strong ones. Writing a "because" requires producing the reason; reading one does not.

**A reviewer can judge the conclusion instead of the route.** Asked whether an argument works, a model may build its own route to the same conclusion and then accept the text's route because the conclusions agree. [Reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md) reports this pattern in math grading. It predicts misses on the second kind of error: a true conclusion reached through an invalid step passes.

**The reviewer may share the generator's errors.** Checks amplify reliability only when the checker discriminates correct from incorrect outputs and its errors are not correlated with the errors it checks, as [error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) shows. A fresh context removes errors that came from the author's own reasoning trace. It does not remove errors that come from a prior the generator and reviewer share, because [decorrelated reviewers still share the field's prior](./reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md). If the generator dropped a constraint because the weaker version is the typical one, a reviewer trained on similar material may find the weaker version typical too.

**An omission gives the reviewer nothing to check.** A reviewer can test the stated steps against each other. It has no reference point for a distinction the text never raised unless it reconstructs the problem independently. The same limit applies to a human acceptor who only reads. A [practitioner account of substantive AI writing](../sources/why-almost-never-use-ai-to-write-anything-substantive.ingest.md) argues that reviewing finished prose invites passive assent. Human approval can establish authority to admit an artifact, but not that its route was checked or that a reported fault was corrected.

The same analysis says where a reviewer can succeed. Incompatible goals and weak steps are present in the text, so a reviewer that must act on them can find them. The reviewer can be required to state the claim in one sentence, to list every inferential step and mark it unsupported when in doubt, and to report a fault location rather than a grade. Each requirement makes the reviewer produce something at a named point, which is closer to what composition forced than reading is. Where a hard external check exists — a type checker, a test, a verbatim source quote — it catches a dropped constraint whatever the reviewer's judgment. Varying the model, prompt, and framing of a claim can reduce correlated errors, but not errors that come from a prior all the reviewers share.

These are predictions, not results. If they hold, a reviewer given only "review this" misses unsupported steps more often than one that must list and mark every step, and omitted distinctions are the error type that text-only review catches least. Whether a given reviewer setup catches these errors is a measurable property of that setup: its discrimination on arguments with true conclusions and invalid routes, and the correlation of its errors with the generator's.

## What one recorded trace can establish

Evidence must match the level of the claim.

A **local correction** is the witness this note's claim needs. It requires a preserved challenge that identified a load-bearing fault, and **independent adjudication** of both the fault and the response: a separate role applies a stated criterion and confirms that the fault was real and that the final claim resolves it, not merely that the claim changed. A different actor alone does not make the adjudication independent. The response may correct the claim, narrow it, or reject it altogether.

A local correction does not establish anything about the method in general:

- **Reviewer reliability** requires measured discrimination between adjudicated supported and unsupported arguments. The test set should include true conclusions reached through invalid routes. When nominally separate checks are combined as independent evidence, their error correlation must also be measured.
- **Loop-versus-solo comparison** requires a specified comparator, role allocation, and measurement rule.
- **Stage attribution** — the claim that one operation caused an improvement — requires stage-level evidence.

A trace can also support three different outcomes, which need different evidence. An **artifact outcome** is a corrected or justifiably rejected claim. A **human-understanding outcome** needs an independent probe of whether the human can restate, update, or apply the implicated claim, route, or uncertainty; assent or copied restatement is not enough. A **later-system outcome** requires that the artifact was retrieved when relevant and changed a later use or decision; persistence alone is not enough. **Acceptance** records authority to admit the artifact and proves none of these outcomes.

## Scope

- The supported claim is existential and local: a recorded loop can, in a given case, correct an artifact under independent adjudication. It claims no edge over solo composition.
- The supplied evidence gives commit-and-expose no completeness criterion, and supplies neither calibrated LLM reviewers nor a loop-versus-solo comparison.
- The reviewer analysis rests on mechanisms reported in the linked notes; its predictions about miss rates are untested.
- The claim applies where writing is doing the thinking. Where the substantive commitments are settled elsewhere, there is no filter to relocate.

## Open Questions

- Can blinded LLM reviewers distinguish invalid routes from valid arguments with useful discrimination and sufficiently uncorrelated errors?
- What task-specific criterion can show that commit-and-expose captured every load-bearing commitment?
- Does recording commitments before showing generated prose reduce anchoring in the acceptor?
- Can any review setup recover omitted distinctions without independently reconstructing the problem?
- Which measured outcome, if any, reaches a solo-composition baseline under a distributed allocation?

---

Relevant Notes:

- [Human analogies suggest functions, not component boundaries](./human-analogies-suggest-functions-not-component-boundaries.md) — grounds: actor allocation must be justified independently
- [Inspectable artifacts, not supervision, defeat the black-box problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — grounds: inspectability enables evaluation without establishing it
- [Error correction works with above-chance, decorrelated oracles](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — grounds: discrimination and correlation conditions for checks
- [LLM generation can hide a relaxed goal where human writing exposes a stall](./llm-generation-relaxes-goals-where-human-writing-stalls.md) — grounds: the stall at the fault that a reviewer of fluent prose does not inherit
- [Generation confidence does not by itself certify soundness](./generation-confidence-does-not-by-itself-certify-soundness.md) — grounds: fluent output carries no marker at an unsound step
- [Reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md) — grounds: reviewers can substitute conclusion agreement for route checking
- [Decorrelated reviewers still share the field's prior](./reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) — grounds: a fresh reviewer context leaves prior-driven errors correlated
- [Vibe noting](./vibe-noting.md) — grounds: persistence, activation, and verification are separate properties
- [Reconstruct a note's composition friction](../instructions/composition-friction-gate.md) — see-also: a report-only reviewer procedure that lists inferential steps and locates weak support instead of grading
