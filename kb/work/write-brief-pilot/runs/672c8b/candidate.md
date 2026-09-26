---
description: "Separates evidence that a recorded challenge corrected one artifact from evidence that a distributed writing method is reliable, causal, or equivalent to solo composition; explains why LLM critics can miss the gaps hand composition exposes."
type: types/note.md
traits: [title-as-claim, synthesis, has-external-sources]
tags: [foundations]
---

# A recorded composition loop can establish a local correction without validating the method

Writers often report that composing a text by hand tests the thinking behind it. When a writer tries to put a claim into exact words, a weak premise or a missing step tends to show up as a sentence that will not come out right. Call this the writing-is-thinking filter. When a language model drafts the text instead, that filter may be lost. One proposed replacement is a distributed loop: a **generator** drafts, a **critic** challenges the draft, and an **acceptor** decides whether the result is admitted.

This note asks what such a loop can show when its steps are recorded. The claim is conditional. Suppose a recorded challenge identifies a load-bearing fault, meaning a fault on which the claim depends. Suppose further that independent adjudication confirms both the fault and that the final response resolves it. Under those conditions, the record establishes a local **artifact outcome**: this artifact was corrected. The response may correct the claim, narrow it, or reject it altogether. The record does not establish that the loop is reliable across cases, that it matches solo composition, or that any one stage caused the improvement. Each of those claims needs different evidence, set out below.

Here, **independent adjudication** is a separate role that applies a stated criterion to the recorded fault and response. A different actor alone does not make the adjudication independent.

## A candidate record contract

For unsettled substantive claims, one candidate record contract separates three operations:

- **Commit-and-expose** records the claim before acceptance, with its constraints, premises, and inferential route.
- **Challenge-and-locate** records objections tied to premises, counterexamples, missing support, and a proposed location for each fault. It does not record a global grade.
- **Respond-and-decide** records a status for every reported challenge. **Investigate** is an interim status. A final disposition does one of four things: rejects the challenge with cited support, revises or narrows the claim, rejects the claim, or accepts the claim with its uncertainty stated explicitly.

Three essays on writing practice motivate these operations: [Putting ideas into words](../sources/putting-ideas-into-words.ingest.md), [thinking through conjecture and counterexample](../sources/how-to-think-in-writing.ingest.md), and [learning by iterated writing](../sources/learning-by-writing.ingest.md). They report practice; they are not controlled comparisons. Across them, writing exposes a commitment, locates a weakness in it or in its support, and revises or discards it. That sequence motivates the contract's three recorded handoffs. It does not show that splitting the sequence across roles preserves the effects the essays describe. The contract is one candidate; it is neither canonical nor validated.

Keeping the input, the challenge report, and the disposition makes each handoff inspectable. The critic and the acceptor remain distinct roles. Either may be filled by a human, an agent, or a policy, but each allocation needs its own warrant, and testing an allocation requires recording who or what filled each role and under what conditions.

The contrast case is **naive prose delegation**: someone supplies a seed, the model generates prose, and the prose is accepted after a global read or an approval. No record of the separate operations is kept, so the resulting artifact cannot support the audit this note describes.

## Why LLM critics can miss what composition exposes

The loop only helps if the critic finds the faults that hand composition would have exposed. There are specific reasons to expect current LLM critics to miss some of them, and specific conditions under which they may catch them. The mechanisms below are drawn from other notes in this KB. They predict where a critic will fail; they do not measure how often it does.

**The fault leaves no mark in finished prose.** In hand composition, failure tends to report its own location: the writer stops at the "because" they cannot justify. [An LLM can instead ship fluent prose after silently dropping a goal it could not satisfy](./llm-generation-relaxes-goals-where-human-writing-stalls.md) (a conjectured mechanism in that note). The dropped constraint is then absent from the text. A critic reading only the text has nothing to point at, and finding the gap means re-deriving the problem constraint by constraint. A constraint that was never written down can only be checked if the critic can reconstruct it independently.

**A critic can check the destination instead of the route.** [Producing a sound route is not the same as evaluating the route presented](./reasoning-production-is-not-reasoning-evaluation.md). A model asked whether an argument works may reconstruct its own path to the same conclusion and then endorse the text. In a benchmark reported there, models evaluating math solutions often overlooked or rationalized invalid steps once the final answer matched. A composing writer cannot take this shortcut, because they must produce each step themselves. So the error class hand composition catches best, a true conclusion reached by an invalid route, is the class a destination-checking critic is most likely to pass.

**Fluency is not evidence of soundness, for the generator or the critic.** [Generation confidence does not by itself certify soundness](./generation-confidence-does-not-by-itself-certify-soundness.md). A critic's verdict is another generated judgment with the same limitation. Smooth prose gives the critic no signal that a step is weak.

**A model critic can share the generator's errors.** [Error correction needs checks whose errors are not correlated](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md). That note reports reasoning errors driven by content that are shared across different model families. A fresh-context critic removes errors that came from the author's own reasoning trace. But [decorrelated reviewers still share the field's prior](./reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md). Where the generator dropped a constraint in favor of the most plausible or conventional reading, a critic trained on similar data is likely to find that reading plausible too.

These mechanisms also say when a critic can catch such faults. A critic catches a fault more readily when the commitment it violates is recorded, because the check becomes a comparison between a stated constraint and the text rather than an unaided reconstruction. This is the job of commit-and-expose. A critic also catches more when it must name premises and inferential steps and locate faults instead of returning a global grade, which is the job of challenge-and-locate. Finally, a critic that runs in a fresh context without the author's trace does not inherit the author's reasoning errors. These conditions make detection possible; none makes it reliable. Whether a given critic discriminates faulty routes from sound ones is an empirical question, and the evidence cited here does not answer it for prose critics.

The same limits apply to a human in the acceptor role. A [practitioner account of substantive AI writing](../sources/why-almost-never-use-ai-to-write-anything-substantive.ingest.md) argues that reviewing finished prose invites passive assent: the generated wording anchors the expert, who may then miss distinctions they would have made while composing. This is a serious objection to any loop that shows generated prose before the human has committed to a position. The recorded contract does not answer the objection; it only makes it testable, by allowing commitments to be recorded before the prose is shown.

## What each claim requires as evidence

Evidence must match the level of the claim:

- **A local correction** requires independent adjudication of both the reported fault and the final response. The adjudicator must confirm that the resulting claim resolves the fault, not merely that the claim changed.
- **Critic reliability** requires evidence that the critic discriminates between supported and unsupported arguments, as judged by adjudication. Tests should include true conclusions reached through invalid routes, for the reason given in the previous section.
- **Combined checks** counted as independent evidence require a measurement of how correlated their errors are.
- **Whole-loop comparison** with solo composition requires a specified comparator, a role allocation, and a measurement rule.
- **Stage attribution**, crediting the result to one operation, requires evidence at the level of that stage.

The evidence available to this note gives commit-and-expose no criterion for completeness. It also provides neither calibrated prose critics nor a comparison between the loop and solo composition.

Neither the identity of the actor, human or agent, nor an approval substitutes for these tests. Human approval grants authority to admit an artifact. It does not show that the route was checked or that a reported fault was corrected. The choice of actor may affect performance, so it must be evaluated rather than used as a proxy for it.

## Four outcomes to keep separate

- An **artifact outcome** is a corrected claim, or a claim justifiably rejected.
- A **human-understanding outcome** needs an independent probe of whether the human can restate, update, or apply the claim, route, or uncertainty involved. Assent, or a restatement copied from the text, is not enough.
- A **later-system outcome** requires that a later system retrieve the artifact when relevant and change a use or decision because of it. Persistence alone is not enough.
- **Acceptance** records admission authority. It proves none of the other three outcomes.

The evidence available supports the record design and the conditional local artifact outcome. It does not support general validation of the method.

## Scope

- The note concerns composition where the substantive commitments are still being formed. Rendering, transcription, and stylistic editing are outside scope when the substantive commitments and checks are fixed elsewhere.
- Human writing practices serve here as motivating comparators. They are not evidence that a distributed loop preserves their effects.
- The account of why LLM critics miss faults relies on mechanisms argued in the linked notes, one of them explicitly conjectural. It predicts which errors to test for; it gives no detection rates.

## Open Questions

- Can blinded prose critics distinguish invalid routes from valid arguments with useful discrimination and sufficiently uncorrelated errors?
- What task-specific criterion can show that commit-and-expose captured every load-bearing commitment?
- Does recording commitments before showing generated prose reduce anchoring in the acceptor?
- Which measured outcome, if any, reaches a solo-composition baseline under a distributed allocation?

---

Relevant Notes:

- [Human analogies suggest functions, not component boundaries](./human-analogies-suggest-functions-not-component-boundaries.md) — grounds: actor allocation must be justified independently
- [Inspectable artifacts, not supervision, defeat the black-box problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — grounds: inspectability enables evaluation without establishing it
- [Error correction works with above-chance, decorrelated oracles](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — grounds: discrimination and correlation conditions for checks
- [Reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md) — grounds: why critics must be tested on true conclusions reached by invalid routes
- [LLM generation can hide a relaxed goal where human writing exposes a stall](./llm-generation-relaxes-goals-where-human-writing-stalls.md) — mechanism: why a fault that stalls a human writer can leave no mark for a critic of finished prose
- [Generation confidence does not by itself certify soundness](./generation-confidence-does-not-by-itself-certify-soundness.md) — grounds: fluent prose and a critic's verdict both lack a built-in soundness signal
- [Decorrelated reviewers still share the field's prior](./reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) — grounds: fresh-context critics remove the author's errors but not errors from a shared prior
- [Vibe noting](./vibe-noting.md) — grounds: persistence, activation, and verification are separate properties
