---
description: "Separates evidence that a recorded challenge corrected one artifact from evidence that a distributed writing method is reliable, causal, or equivalent to solo composition; explains which composition errors LLM reviewers can and cannot see."
type: types/note.md
traits: [title-as-claim, synthesis, has-external-sources]
tags: [foundations]
---

# A recorded composition loop can establish a local correction without validating the method

**Background.** Writing practitioners often say that writing is thinking. Putting an idea into sentences forces the writer to commit to one concrete version of it. At that point a weak "because" or two goals that cannot both hold often become visible, and the writer stalls. That stall does two jobs: it stops a bad claim before it is published, and it shows the writer where their understanding is thin. When an LLM drafts the prose instead, this check can disappear, because [LLM generation can hide a relaxed goal where human writing exposes a stall](./llm-generation-relaxes-goals-where-human-writing-stalls.md): fluent output looks the same whether or not every constraint was met. A distributed writing workflow tries to get the check back by splitting the work across roles. A generator drafts, a critic challenges, and an acceptor decides what is admitted to the knowledge base.

**Claim.** Such a workflow can establish a specific, local result under stated conditions. Suppose the workflow preserves a challenge that identifies a load-bearing fault, meaning a fault that changes whether the claim holds. Suppose also that independent adjudication confirms the fault and confirms that the final response resolves it. Then the preserved record establishes a local **artifact outcome**: this document was corrected. The response may correct the claim, narrow it, or reject it. The record does not establish that the method is reliable across cases, that it matches solo composition, or that any one stage caused the improvement. Each of those claims needs different evidence, set out below.

## A candidate record contract

For unsettled substantive claims, one candidate record contract separates three operations.

- **Commit-and-expose** records, before acceptance, the claim, its constraints, its premises, and the inferential route from premises to claim.
- **Challenge-and-locate** records objections tied to specific premises, counterexamples, missing support, and a proposed location for each fault. It does not record a global grade.
- **Respond-and-decide** records a status for every reported challenge. **Investigate** is an interim status. A final disposition does one of four things: rejects the challenge with cited support, revises or narrows the claim, rejects the claim, or keeps explicit uncertainty at acceptance.

Three practice essays motivate these operations: [putting ideas into words](../sources/putting-ideas-into-words.ingest.md), [thinking through conjecture and counterexample](../sources/how-to-think-in-writing.ingest.md), and [learning by iterated writing](../sources/learning-by-writing.ingest.md). They report practice; they are not controlled comparisons. Across them, writing exposes a commitment, locates a weakness in it or its support, and then revises or discards it. That sequence motivates the three recorded operations. It does not show that splitting the operations across roles preserves the effects the practices have for a single writer. The contract is neither canonical nor validated.

Preserving each operation's input, report, and disposition makes the handoffs between roles inspectable. The checker and the acceptor are distinct roles. A human, an agent, or a policy may fill either role, but each allocation needs its own justification. Testing an allocation also requires recording who or what filled each role and under what conditions.

The contrast case is **naive prose delegation**: a person supplies a seed idea and accepts the generated prose after only a global read or approval. No operation-level record remains, so there is nothing to audit at the level this note requires. Rendering, transcription, and stylistic editing are outside this note's scope when the substantive commitments and checks are fixed elsewhere.

## What LLM reviewers can and cannot see

The loop is only as good as its critic, and in practice the critic is often an LLM reviewer. The errors that hand composition exposes fall into kinds that current LLM reviewers are differently placed to catch. The reasons below come from mechanisms argued in linked notes. How often each case occurs has not been measured.

**Errors visible in the text.** Some faults leave a trace in the prose: two sentences that contradict each other, a cited premise that does not say what the text claims, a conclusion the stated premises plainly do not reach. A reviewer reading the text has the material it needs to find these. A reviewer can catch them if it inspects the route and does not just agree with the destination.

**True conclusions reached by invalid routes.** This is the most direct substitute for the writer's stalled "because", and reviewers are poorly placed to catch it. A reviewer asked whether an argument works may solve the problem itself, see that its answer matches, and pass over invalid steps in the submitted route. That is why [reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md). A reviewer that can produce the conclusion is not thereby checking the route. A review that asks for enumerated premises and joints, as challenge-and-locate does, targets this failure. Whether it removes the failure is untested.

**Dropped constraints.** When generation silently drops a goal the author held, the dropped goal is usually absent from the text. The prose reads as a complete solution to a smaller problem. A reviewer that sees only the finished prose has nothing to check the missing constraint against. Next-token fluency is no signal here either, because [generation confidence does not by itself certify soundness](./generation-confidence-does-not-by-itself-certify-soundness.md). This is the strongest reason for commit-and-expose. Recording the claim and its constraints before the prose exists gives a later reviewer an explicit list to check the draft against. The contract has no completeness criterion for that list, so a constraint the author never wrote down can still vanish.

**Errors the reviewer shares.** A check helps only when it errs differently from the generator. [Error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md): voting or repeating checks averages out independent errors but not shared ones. A reviewer that runs in the generator's context, or on the same model with a similar prompt, tends to repeat the generator's errors. A fresh context removes errors from the author's own reasoning trace. It does not remove errors that come from what the field commonly believes, because [decorrelated reviewers still share the field's prior](./reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md). On an original claim, a reviewer's pushback may be pressure toward consensus rather than a found fault.

Together these cases explain why a reviewer's report counts as a challenge and not as a verdict. A challenge still needs adjudication. They also explain why the evidence tiers below ask for measured discrimination and error correlation rather than trusting the reviewer by type.

## Evidence must match the claim's level

Here, **independent adjudication** is a separate role that applies a stated criterion to the preserved fault and to the response. A different actor alone does not make a check independent.

- A **local correction** requires independent adjudication of both the reported fault and the final response. The adjudicator must confirm that the resulting claim resolves the fault, not merely that the claim changed.
- **Critic reliability** requires evidence that the critic discriminates between adjudicated supported and unsupported arguments. The test set should include true conclusions reached through invalid routes, for the reason given in the previous section.
- **Combined checks** can count as independent evidence only when their error correlation has been measured.
- **Whole-loop comparison** with solo composition requires a specified comparator, role allocation, and measurement rule.
- **Stage attribution**, crediting the result to one operation, requires stage-level evidence.

The available evidence gives commit-and-expose no completeness criterion. It provides no calibrated prose critics and no comparison of the loop against solo composition.

Neither actor identity nor approval substitutes for these tests. A human reviewing finished prose may simply assent to it, and reading the draft first may anchor them to it. A [practitioner account of substantive AI writing](../sources/why-almost-never-use-ai-to-write-anything-substantive.ingest.md) argues this as a reason to avoid AI drafting altogether. The objection bears directly on this loop: an acceptor shown generated prose is exposed to the same risk. Human approval can establish authority to admit an artifact. It cannot establish that the route was checked or that a reported fault was corrected. The choice of actor may affect performance, so it must be evaluated, not used as a proxy for performance.

## Separate outcomes

These evidence tiers keep four outcomes apart.

- An **artifact outcome** is a claim that was corrected or justifiably rejected.
- A **human-understanding outcome** needs an independent probe showing that the human can restate, update, or apply the implicated claim, route, or uncertainty. Assent or a copied restatement is not enough.
- A **later-system outcome** requires that the result is retrieved when relevant and changes a later use or decision. Persistence alone is not enough.
- **Acceptance** records admission authority. It proves none of the other three outcomes.

The available evidence supports the record design and the conditional local artifact outcome. It does not support general validation of the method.

## Scope

- The claim covers unsettled substantive claims, where composition is the search for a version of the claim that holds. It does not cover rendering a claim whose content is already fixed.
- The analysis of LLM reviewers rests on mechanisms argued in the linked notes, not on measurements of this loop.

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
- [Vibe noting](./vibe-noting.md) — grounds: persistence, activation, and verification are separate properties
- [LLM generation can hide a relaxed goal where human writing exposes a stall](./llm-generation-relaxes-goals-where-human-writing-stalls.md) — grounds: the composition stall and the silently dropped constraint that the loop tries to recover
