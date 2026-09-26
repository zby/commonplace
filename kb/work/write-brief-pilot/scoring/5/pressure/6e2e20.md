---
description: "Separates what a recorded challenge-and-response trace shows (one artifact corrected) from method validity, and explains which errors of hand composition LLM reviewers can and cannot see in finished prose."
type: types/note.md
traits: [title-as-claim, synthesis, has-external-sources]
tags: [foundations]
---

# A recorded composition loop can establish a local correction without validating the method

Writing a text by hand does more than put ideas into words. Several practitioner essays describe what composing does to a weak idea: [putting ideas into words](../sources/putting-ideas-into-words.ingest.md), [thinking through conjecture and counterexample](../sources/how-to-think-in-writing.ingest.md), and [learning by iterated writing](../sources/learning-by-writing.ingest.md). Across them, the same sequence recurs. The writer commits to an exact claim, finds where the claim or its support fails, and revises or discards it. This note calls that sequence the **writing-is-thinking filter**: commit to exact wording, locate a weakness, then revise, narrow, or discard. The essays report practice. They do not compare it with other methods under controlled conditions.

**Naive prose delegation** skips the filter. Someone gives a model a seed idea and accepts the generated prose after only a global read or approval. The model chose the wording, so nobody committed to it step by step, and no record shows where the claim might fail. One response is to rebuild the filter as a loop spread across people and agents: one party commits to a claim, a checker challenges it, and the author responds. This note asks what the record of such a loop can show.

The answer depends on the level of the claim. Suppose the record preserves a challenge that identifies a load-bearing fault, meaning a fault that would make the claim wrong or unsupported if it is real. Suppose also that a separate adjudicator confirms both the fault and that the final response resolves it. Then the trace establishes a **local artifact outcome**: this document's claim was corrected, narrowed, or rejected for a confirmed reason. The trace does not establish that the loop is reliable across cases, that it matches solo composition, or that any single stage caused the improvement. Each of those claims needs different evidence. Part of the reason is that the loop's checkers are fallible in specific ways, and the section on LLM reviewers below explains which composition errors they can see.

## A record contract with three operations

For unsettled substantive claims, one candidate record contract splits the filter into three recorded operations:

- **Commit-and-expose** records the claim before acceptance, with its constraints, premises, and inferential route.
- **Challenge-and-locate** records objections tied to specific premises, counterexamples, missing support, and a proposed location for the fault. It does not record a global grade.
- **Respond-and-decide** records a status for every reported challenge. **Investigate** is an interim status. A final disposition rejects the challenge with cited support, revises or narrows the claim, rejects the claim, or keeps the uncertainty explicit at acceptance.

The essays' commit, locate, revise sequence motivates these three handoffs. It does not show that the handoffs preserve what composing does for the writer. The taxonomy is neither canonical nor validated.

Keeping the input, the challenge report, and the disposition makes each handoff inspectable. The contract separates two roles. A **checker** tests the claim; an **acceptor** decides whether the artifact enters the knowledge base. A human, an agent, or a fixed policy may fill either role, but each allocation needs its own warrant, since [human analogies suggest functions, not component boundaries](./human-analogies-suggest-functions-not-component-boundaries.md). Testing an allocation also requires recording who or what filled each role and under what conditions. Naive prose delegation keeps no operation-level trace, so its record cannot support this audit. Rendering, transcription, and stylistic editing are outside scope when the substantive commitments and checks happen elsewhere.

## Why LLM reviewers catch some composition errors and miss others

Composition exposes an error at the place it occurs. A writer who cannot finish a sentence after "because" learns where their understanding ran out. [LLM generation can hide a relaxed goal where human writing exposes a stall](./llm-generation-relaxes-goals-where-human-writing-stalls.md) proposes that generation fails differently. When a model cannot satisfy every constraint of a request, it can still produce fluent prose that solves a weaker problem with one constraint dropped, and nothing on the surface marks the drop. That account is a mechanistic hypothesis motivated by a practitioner contrast, not a measured rate. If it holds, a reviewer of finished prose has to re-derive the constraints that the text no longer shows.

An LLM reviewer reads only what it is given. It can therefore look for faults whose evidence is in the text or in loaded sources. Examples are a claim contradicted elsewhere in the same text, a list that misses cases its own definition admits, a citation that does not say what the text attributes to it, or a step with no stated support. [Semantic review catches content errors that structural validation cannot](./semantic-review-catches-content-errors-that-structural-validation.md) describes these checks. No evidence supplied here measures how reliably current reviewers perform them on prose arguments.

Three mechanisms explain why errors that hand composition would expose can pass such a reviewer:

- **The violated constraint is absent from the input.** A constraint the author held but never wrote down is not in the text the reviewer reads. Prose that silently dropped it is still a coherent answer to the weaker problem, so a coherence check finds nothing. Commit-and-expose targets this gap: it records the claim, constraints, and route before the prose exists, so a checker can test the prose against them. It captures only what the committer states, however, and no completeness criterion exists for it.
- **The reviewer checks the destination instead of the route.** Asked whether an argument works, a model may build its own route to the same conclusion and accept the text because the conclusion looks right. [Reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md) reports this pattern in models' verbalized grading of math solutions; transfer to prose arguments is untested. The pattern matters here because the filter's main target is a plausible claim reached by a broken route. Challenge-and-locate asks for located objections instead of a global grade, which directs attention to the route. Whether that is enough is also untested.
- **The reviewer's errors coincide with the generator's.** A check is useful only if it flags faulty arguments more often than sound ones, and repeated checks add evidence only when their errors are not shared, as [error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) explains. That note cites content effects on reasoning that appear across several model families. A reviewer with a fresh context avoids errors that came from the author's own reasoning, but [decorrelated reviewers still share the field's prior](./reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md). Where a claim contests the consensus reading, several such reviewers act like one check, not several. A reviewer running on the same model as the generator may also share the generator's tendency to drop the same constraint.

So a reviewer can catch a composition error only under two conditions. The violated constraint must be present in what the reviewer reads, and the reviewer's errors must not coincide with the generator's. Recording commitments can improve the first condition. Neither the contract nor a change of reviewer guarantees the second; it has to be measured. A confident reviewer verdict does not settle either condition, because [generation confidence does not by itself certify soundness](./generation-confidence-does-not-by-itself-certify-soundness.md) and a verdict is another generated judgment. These limits are why a single trace supports the local claim, where an adjudicator examines one specific fault, and not a claim about how often the loop's checkers succeed.

## Evidence must match the claim's level

A local correction requires independent adjudication of both the reported fault and the final response. The adjudicator must confirm that the resulting claim resolves that fault, not merely that the text changed. Here, **independent adjudication** is a separate role that applies a stated criterion to the preserved fault and response. A different actor alone does not establish independence.

Claims above the local level need more:

- **Critic reliability** requires showing that critics separate adjudicated sound arguments from unsound ones. Test sets should include true conclusions reached through invalid routes, for the destination-agreement reason above.
- **Combined checks** count as independent evidence only after their error correlation is measured.
- **Whole-loop performance** requires a specified comparator, role allocation, and measurement rule.
- **Attribution to one stage** requires stage-level evidence.

The available evidence gives commit-and-expose no completeness criterion, and provides neither calibrated prose critics nor a comparison between the loop and solo composition.

## Human approval grants authority, not a check

Neither the actor's identity nor approval substitutes for those tests. A [practitioner account of substantive AI writing](../sources/why-almost-never-use-ai-to-write-anything-substantive.ingest.md) argues that reviewing finished prose can invite passive assent. A plausible mechanism is anchoring: the generated wording frames the reviewer's reading, so the reviewer may not recover distinctions they would have made while composing. Human approval can establish authority to admit an artifact. It cannot establish that the artifact's route was checked or that a reported fault was corrected. The choice of actor may affect performance, so it has to be evaluated rather than used as a proxy.

## Three outcomes to keep apart

- A corrected or justifiably rejected claim is an **artifact outcome**.
- A **human-understanding outcome** needs an independent probe of whether the human can restate, update, or apply the implicated claim, route, or uncertainty. Assent or a copied restatement is insufficient.
- A **later-system outcome** requires that the artifact is retrieved when relevant and changes a later use or decision. Persistence alone is not enough.

**Acceptance** records admission authority but proves none of these outcomes. The available evidence supports the record design and the conditional local artifact result. It does not support general validation of the method.

## Scope

- The writing essays are practitioner and conceptual evidence, not controlled demonstrations.
- The reviewer account combines KB notes whose evidence comes from math grading, reasoning benchmarks, and one review audit. None measures LLM review of prose arguments directly.
- The claim covers substantive claims still being worked out. It does not cover rendering settled content.

## Open Questions

- Can blinded prose critics distinguish invalid routes from valid arguments with useful discrimination and sufficiently uncorrelated errors?
- Does a reviewer flag a dropped constraint more often when a commit-and-expose record states that constraint than when it reads the prose alone?
- What task-specific criterion can show that commit-and-expose captured every load-bearing commitment?
- Does recording commitments before showing generated prose reduce anchoring in the acceptor?
- Which measured outcome, if any, reaches a solo-composition baseline under a distributed allocation?

---

Relevant Notes:

- [Human analogies suggest functions, not component boundaries](./human-analogies-suggest-functions-not-component-boundaries.md) — grounds: actor allocation must be justified independently
- [Inspectable artifacts, not supervision, defeat the black-box problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — grounds: inspectability enables evaluation without establishing it
- [Error correction works with above-chance, decorrelated oracles](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — grounds: discrimination and correlation conditions for checks
- [LLM generation can hide a relaxed goal where human writing exposes a stall](./llm-generation-relaxes-goals-where-human-writing-stalls.md) — mechanism: why a dropped constraint leaves no mark for a prose reviewer to find
- [Reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md) — grounds: the destination-agreement failure that critic tests must include
- [Decorrelated reviewers still share the field's prior](./reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) — grounds: why fresh-context reviewers are not independent on consensus-determined components
- [Vibe noting](./vibe-noting.md) — grounds: persistence, activation, and verification are separate properties
