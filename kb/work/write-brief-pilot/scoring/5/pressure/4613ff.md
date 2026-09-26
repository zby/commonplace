---
description: "Separates evidence that a recorded challenge corrected one artifact from evidence that a distributed writing method is reliable, causal, or equivalent to solo composition; explains which composition faults LLM reviewers can and cannot see."
type: types/note.md
traits: [title-as-claim, synthesis, has-external-sources]
tags: [foundations, llm-reliability]
---

# A recorded composition loop can establish a local correction without validating the method

Writers often report that composing a text by hand is also how they find out what they think. Choosing exact words forces a vague idea into a definite claim. The writer then hits the places where it fails: a "because" they cannot complete, two requirements that cannot both hold, a premise they had assumed without noticing. Call this effect the **composition filter**. When an LLM drafts the text instead, the filter can disappear, because the model can produce fluent prose past a gap that would have stopped a human writer.

A **distributed writing workflow** tries to put the filter back by splitting composition across separate steps and actors. For example, an author states a claim, one model drafts, a second model attacks the draft, and a human decides what to accept. This note asks what the records of such a workflow can prove.

The answer is narrow but real. Suppose the record preserves a challenge that identifies a load-bearing fault. If independent adjudication confirms both the fault and that the final text resolves it, the record establishes a **local correction**: this artifact was improved in this respect. The response may correct the claim, narrow it, or reject it altogether. The record does not establish that the method is reliable across cases, that it matches solo composition, or that any one step caused the improvement. Those claims require different evidence.

## What the loop records

For unsettled substantive claims, one candidate record contract separates three operations:

- **Commit-and-expose** records, before acceptance, the claim, its constraints, its premises, and the inferential route from premises to claim.
- **Challenge-and-locate** records objections tied to specific premises, counterexamples, missing support, and a proposed location for each fault, rather than a global grade.
- **Respond-and-decide** records a status for every reported challenge. **Investigate** is an interim status. A final disposition rejects the challenge with cited support, revises or narrows the claim, rejects the claim, or keeps the uncertainty explicit at acceptance.

Three practitioner accounts motivate this split: [putting ideas into words](../sources/putting-ideas-into-words.ingest.md), [thinking through conjecture and counterexample](../sources/how-to-think-in-writing.ingest.md), and [learning by iterated writing](../sources/learning-by-writing.ingest.md). They report practice rather than controlled comparisons. Across them, writing exposes a commitment, locates a weakness in it or its support, and revises or discards it. That sequence motivates the contract's three recorded handoffs. It does not show that the handoffs keep the epistemic effect the practices have when one person does all three. The split is neither canonical nor validated.

Preserving the input, the challenge report, and the disposition makes each handoff inspectable. Checking and accepting remain distinct roles. A human, an agent, or a fixed policy may fill either role when that allocation has its own justification, because [human analogies suggest functions, not component boundaries](./human-analogies-suggest-functions-not-component-boundaries.md). Testing an allocation also requires recording who or what filled each role and under what conditions.

The contrasting case is **naive prose delegation**: someone supplies a seed idea, a model writes the text, and the person accepts it after reading it through or approving it as a whole. No step-level record remains, so the artifact cannot support the audit described here. Rendering, transcription, and stylistic editing are outside this note's scope when the substantive claims and checks are fixed elsewhere.

## Which composition faults an LLM reviewer can see

The loop depends on the challenge step finding the faults that the composition filter would have exposed. Whether an LLM reviewer can do that depends less on the reviewer's general capability than on where the fault is located. A reviewer reads the text it is given. It can only find a fault that the text, or the record beside it, makes visible. The mechanisms below come from linked notes; none of them gives a measured rate for current reviewers on prose.

**Faults stated in the text are within reach.** An explicit inference that does not follow, a premise the text asserts without support, and two sentences that contradict each other are all on the page. A reviewer with a fresh context, asked to list each load-bearing inferential step and mark its support, can check them. A self-grade cannot do this job, because a model's confidence in its own output [does not by itself certify soundness](./generation-confidence-does-not-by-itself-certify-soundness.md). The [composition friction gate](../instructions/composition-friction-gate.md) uses this shape: it enumerates inferential steps and returns no overall verdict.

**A reviewer can judge the conclusion instead of the route.** In the case reported in [reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md), reasoning models graded a submitted math solution by solving the problem themselves. When the final answers matched, they overlooked invalid steps in the submitted reasoning. Prose review invites the same substitution: if the reviewer finds the conclusion plausible, it can rebuild its own argument for it and pass the text's weak "because". This is the fault the composition filter catches most directly, since a writer who stalls at a weak "because" is evaluating the route, not the destination. A reviewer escapes the substitution only when the prompt forces it to trace the stated premises to the stated conclusion. Even then, whether it discriminates valid from invalid routes has to be tested.

**A dropped constraint leaves nothing in the text to flag.** When a human writer cannot satisfy all the requirements at once, the writing stalls at the conflict. An LLM can instead [silently relax the goal](./llm-generation-relaxes-goals-where-human-writing-stalls.md) and write a fluent answer to a weaker problem. The missing requirement is then absent from the text rather than wrong in it. A reviewer who sees only the draft has no way to tell that it answers a weaker question than the author meant, because the author's intended purpose cannot be reconstructed from the draft alone. The same holds for distinctions a domain expert would have made while writing but that the generated draft omits. This is the main reason for **commit-and-expose**: a record of the claim and constraints made before drafting gives the reviewer something to compare the draft against. A reviewer can then find a missing constraint as a mismatch between the record and the text.

**Reviewers share the generator's prior.** A second model, or a fresh context, removes errors that came from the drafter's own chain of reasoning. It does not remove errors that come from what models learned in common. [Decorrelated reviewers still share the field's prior](./reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md): where the familiar reading of a claim is wrong, the drafter and the reviewers tend to be wrong together. [Error correction needs checks whose errors are decorrelated](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md). That note reports content effects on reasoning that were shared across architecturally different models and survived scaling and instruction tuning, so switching models is not enough by itself. Two reviewers that agree therefore count as less evidence than two independent checks. Their agreement is weakest on the original claims, which are the ones a writer most needs checked.

So an LLM reviewer can partly reconstruct the composition filter for faults that are written down, and only when the prompt forces route inspection. It cannot reconstruct the filter for faults that consist of something missing, unless the record supplies what should have been there. On claims where the familiar reading is wrong, several LLM reviewers add less than their number suggests.

## Evidence must match the claim's level

A local correction requires independent adjudication of both the reported fault and the final response. The adjudicator must confirm that the revised claim resolves the fault, not merely that it changed. Here, **independent adjudication** is a separate role that applies a stated criterion to the preserved fault and response. A different actor does not by that fact alone make the adjudication independent.

Claims above the local level need more:

- **Critic reliability** requires showing that critics discriminate between adjudicated supported and unsupported arguments. Test sets should include true conclusions reached through invalid routes, since that is where conclusion-for-route substitution hides.
- **Combined checks** counted as independent evidence require measuring how their errors correlate.
- **Whole-loop comparison** requires a specified comparator, role allocation, and measurement rule.
- **Attribution to one step** requires step-level evidence.

The sources cited here give **commit-and-expose** no test for whether it captured every load-bearing commitment. They also provide no calibrated prose critics and no comparison of the loop against solo composition.

## Actor identity and approval are not tests

Neither the identity of an actor nor an approval substitutes for those tests. Reviewing finished prose may invite passive assent: a [practitioner account of substantive AI writing](../sources/why-almost-never-use-ai-to-write-anything-substantive.ingest.md) argues that fluent generated wording anchors an expert reader and omits distinctions the expert would have made while composing. Human approval can establish authority to admit an artifact. It cannot establish that the artifact's route was checked or that a reported fault was corrected. The choice of actor may affect performance, so it must be evaluated rather than used as a stand-in for evaluation.

## Separate outcomes need separate evidence

- An **artifact outcome** is a claim that was corrected or justifiably rejected.
- A **human-understanding outcome** needs an independent probe of whether the human can restate, update, or apply the claim, route, or uncertainty involved. Assent or a copied restatement is not enough.
- A **later-system outcome** requires that the artifact is retrieved when relevant and changes a later use or decision. Persistence alone is not enough, as [vibe noting](./vibe-noting.md) separates persistence, activation, and verification.
- **Acceptance** records authority to admit the artifact and proves none of these outcomes.

The sources cited here support the record design and the conditional local artifact result. They do not support general validation of the method.

## Open Questions

- Can blinded prose critics distinguish invalid routes from valid arguments with useful discrimination and sufficiently uncorrelated errors?
- Does giving a reviewer the commit-and-expose record let it find dropped constraints that it misses when it sees only the draft?
- What task-specific criterion can show that `commit-and-expose` captured every load-bearing commitment?
- Does recording commitments before showing generated prose reduce anchoring in the acceptor?
- Which measured outcome, if any, reaches a solo-composition baseline under a distributed allocation?

---

Relevant Notes:

- [Human analogies suggest functions, not component boundaries](./human-analogies-suggest-functions-not-component-boundaries.md) — grounds: actor allocation must be justified independently
- [Inspectable artifacts, not supervision, defeat the black-box problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — grounds: inspectability enables evaluation without establishing it
- [Error correction works with above-chance, decorrelated oracles](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — grounds: discrimination and correlation conditions for checks
- [Vibe noting](./vibe-noting.md) — grounds: persistence, activation, and verification are separate properties
- [Reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md) — mechanism: a reviewer can substitute conclusion agreement for route inspection
- [LLM generation can hide a relaxed goal where human writing exposes a stall](./llm-generation-relaxes-goals-where-human-writing-stalls.md) — mechanism: why a dropped constraint leaves nothing in the draft for a reviewer to flag
- [Decorrelated reviewers still share the field's prior](./reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) — mechanism: why several LLM reviewers are not several independent checks
