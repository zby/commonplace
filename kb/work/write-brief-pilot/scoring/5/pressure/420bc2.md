---
description: "Separates evidence that a recorded challenge corrected one artifact from evidence that a distributed writing method is reliable, and explains when LLM reviewers do or do not catch the gaps hand composition exposes."
type: types/note.md
traits: [title-as-claim, synthesis, has-external-sources]
tags: [foundations]
---

# A recorded composition loop can establish a local correction without validating the method

Writing a text by hand tests the ideas in it. To put a claim into exact words, the writer must decide what the claim is, what supports it, and how the support leads to it. A gap in that reasoning often shows up as a sentence the writer cannot finish. This note calls that effect the writing-is-thinking filter. When an LLM drafts the text, the writer no longer composes the sentences, so the filter may no longer operate.

A distributed writing workflow tries to rebuild the filter from separate steps. Someone states the claim, someone else challenges it, and someone decides what to do about each challenge. Each step can be performed by a human, an agent, or a policy. If those steps leave a record, the record can show something specific. Suppose a recorded challenge found a fault that the claim depends on. Suppose also that a separate judge confirmed the fault and confirmed that the final version fixes it. Then the record establishes a local correction: this artifact was improved in this respect. The final version may correct the claim, narrow it, or drop it.

The record does not establish that the workflow is reliable across cases, that it matches composing by hand, or that any one step caused the improvement. Those claims need different evidence. The rest of this note explains what the filter exposes, how a record can split it into steps, why current LLM reviewers catch some of the exposed errors and miss others, and what each level of evidence requires.

## What composing by hand exposes

Three practitioner accounts describe the filter. [Putting ideas into words](../sources/putting-ideas-into-words.md) describes exact wording exposing that an idea is incomplete. [Thinking through conjecture and counterexample](../sources/how-to-think-in-writing.md) describes stating a definite claim, listing its premises, and searching for counterexamples. [Learning by iterated writing](../sources/learning-by-writing.md) describes writing down a current view, attacking it, and revising it repeatedly. These are reports of practice, not controlled comparisons.

Across them, composing exposes a commitment, locates a weakness in the commitment or its support, and then revises or discards it. The errors this sequence tends to expose fall into a few kinds:

- **An unsupported step.** The writer reaches "because" or "therefore" and finds no reason to write next.
- **A dropped constraint.** The goal asks for several things at once, and writing out a concrete version shows they cannot all hold. A human writer may stall at that point. An LLM can instead produce fluent text that silently satisfies a weaker goal, as [LLM generation can hide a relaxed goal where human writing exposes a stall](./llm-generation-relaxes-goals-where-human-writing-stalls.md) argues.
- **A missing distinction.** An expert who composes the text would have added a qualification or a sensitivity that generated text leaves out.

## A record that splits the filter into three steps

For claims that are still unsettled, one candidate record design separates the filter into three recorded steps:

- **Commit-and-expose** records the claim before it is accepted, together with its constraints, its premises, and the inferential route from premises to claim.
- **Challenge-and-locate** records objections tied to specific premises, counterexamples, and missing support. Each objection names where the fault is. It does not give the draft an overall grade.
- **Respond-and-decide** gives every reported challenge a status. **Investigate** is an interim status. A final status does one of four things: rejects the challenge with cited support, revises or narrows the claim, rejects the claim, or keeps the uncertainty explicit at acceptance.

The practitioner sequence above motivates these three steps. It does not show that the steps keep the epistemic effect the practices have when one person composes. The three-step split is one possible design; it is neither canonical nor validated.

Keeping the input, each challenge, and each decision makes the steps inspectable. The role that challenges (the checker) and the role that admits the artifact (the acceptor) stay separate. Either role may be filled by a human, an agent, or a policy, but each allocation needs its own justification. To test an allocation, the record must also say who or what filled each role and under what conditions.

The contrast case is **naive prose delegation**: someone supplies a seed idea, an LLM writes the prose, and the person accepts it after reading it through or approving it. That workflow keeps no step-level record, so its record cannot support the checks this note describes.

## Why LLM reviewers catch some of these errors and miss others

An LLM reviewer could, in principle, stand in for the challenge the writer's own composing would have supplied. Whether it does depends on whether the error is visible in what the reviewer reads, and on whether the reviewer checks the reasoning or only the conclusion. The mechanisms below come from other notes in this KB. Several are hypotheses, and this note supplies no measured rate at which reviewers catch any kind of error.

**Why a reviewer can miss them.**

- *The finished text does not mark where it failed.* When generation drops a constraint, the prose around the gap stays fluent. Nothing on the surface shows which constraint went unmet ([the relaxed-goal note](./llm-generation-relaxes-goals-where-human-writing-stalls.md)). A reviewer that reads only the final text must recompute each constraint to find the gap. It cannot do that for a constraint the text never states.
- *Fluency is not evidence of soundness.* A model's confidence in a continuation measures how likely it is, not whether it is true or valid, as [generation confidence does not by itself certify soundness](./generation-confidence-does-not-by-itself-certify-soundness.md) explains. A reviewer that treats smooth prose as a sign of a sound argument inherits the same gap.
- *Reviewers may check the conclusion instead of the route.* [Reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md): a model asked whether an argument works may rebuild its own argument for the same conclusion and then accept the text. In the math-grading benchmark that note reports, evaluators often passed over invalid steps once the final answer matched; the note treats this as suggestive rather than conclusive. This failure hits the unsupported-step error directly. A claim that is true but reached by an invalid step is exactly what such a reviewer passes.
- *Reviewers share the generator's blind spots.* Repeated checks help only when their errors are independent. LLM reasoning errors driven by the content of the premises recur across model families, so a second model does not by itself give an independent check ([error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md)). Reviewers trained on similar data also share the field's usual reading of a topic ([decorrelated reviewers still share the field's prior](./reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md)). A missing distinction that the field also tends to omit is therefore the kind an LLM reviewer is least likely to add back.

**Why a reviewer can catch them.**

- *The commitments are written down.* If commit-and-expose records the constraints and premises before generation, a reviewer can check the text against each one instead of against its own guess of what the text meant to do. A dropped constraint then becomes a visible mismatch instead of a gap in fluent prose.
- *The review asks for fault locations, not a grade.* A request to name which premise fails and where pushes the reviewer to inspect the route. A request for an overall verdict invites agreement with the conclusion. This is why challenge-and-locate records located objections rather than a grade.
- *The reviewer does not share the writer's context.* A fresh reviewer, given the recorded commitments but not the drafting session, does not inherit errors that came from the drafting session's own reasoning. Varying the framing of the check can also reduce shared content bias. Neither step removes errors that come from the field's shared prior.
- *Some content errors are visible on the page.* [Semantic review catches content errors that structural validation cannot](./semantic-review-catches-content-errors-that-structural-validation.md), such as internal contradictions, incomplete lists, and claims that drift from their cited evidence. These errors leave a trace in the text, so a reviewer can find them without the writer's intent.

The result is uneven. An LLM reviewer has the best chance with errors that leave a trace in the text or conflict with a recorded commitment. It has the least chance with a distinction that neither the text nor the record contains, especially one the field also tends to leave out. That last case is the same one a human editor is warned about: reading fluent generated prose may invite passive assent instead of recovering what the expert would have said while composing, as a [practitioner account of substantive AI writing](../sources/why-almost-never-use-ai-to-write-anything-substantive.md) argues. So the record design moves the check to a point where some of these errors become visible. Whether a given reviewer then catches them at a useful rate is an empirical question.

## What each level of evidence requires

Evidence must match the level of the claim.

- **A local correction** needs independent adjudication of both the reported fault and the final response. The adjudicator must confirm that the new claim resolves the fault, not merely that the claim changed. Here **independent adjudication** means a separate role that applies a stated criterion to the recorded fault and response. Using a different actor does not by itself make the adjudication independent.
- **Reviewer reliability** needs evidence that the reviewer separates adjudicated sound arguments from unsound ones. The test set should include true conclusions reached through invalid routes, because that is the case in which checking the conclusion and checking the route come apart. When several nominally separate checks are combined as independent evidence, the correlation of their errors must also be measured.
- **Whole-workflow performance** needs a named comparison baseline, a stated role allocation, and a measurement rule.
- **Attributing an improvement to one step** needs evidence at the level of that step.

The evidence behind this note gives commit-and-expose no test that it recorded every commitment the claim depends on. It also provides no calibrated prose reviewers and no comparison between the workflow and composing by hand.

Neither the identity of the actor nor approval replaces those tests. Human approval can establish the authority to admit an artifact. It cannot establish that the route was checked or that a reported fault was fixed. The choice of actor may affect performance, so it must be evaluated rather than used as a stand-in for evaluation.

These levels also keep different outcomes apart:

- An **artifact outcome** is a claim that was corrected or justifiably rejected.
- A **human-understanding outcome** needs a separate probe of whether the human can restate, update, or apply the claim, route, or uncertainty in question. Assent or a copied restatement does not count.
- A **later-system outcome** needs evidence that the artifact was retrieved when relevant and changed a later use or decision. Persisting in storage does not count.
- **Acceptance** records the authority to admit the artifact. It proves none of the three outcomes above.

The available evidence supports the record design and the conditional local correction. It does not support a general validation of the method.

## Scope

- The note concerns substantive claims that are still unsettled. Rendering, transcription, and stylistic editing are out of scope when the substantive commitments and their checks are fixed elsewhere.
- The account of what reviewers catch combines mechanisms argued in other notes. Some of those mechanisms are hypotheses, and none of them has been measured for prose review in this setting.

## Open Questions

- Can blinded prose reviewers separate invalid routes from valid arguments well enough to be useful, with errors that are sufficiently uncorrelated?
- What task-specific test can show that commit-and-expose captured every commitment the claim depends on?
- Does recording the commitments before showing generated prose reduce anchoring in the acceptor?
- Can any review step recover a missing distinction that neither the text nor the record contains, or does that error need the expert to compose?
- Which measured outcome, if any, reaches the level of composing by hand under a distributed allocation?

---

Relevant Notes:

- [Human analogies suggest functions, not component boundaries](./human-analogies-suggest-functions-not-component-boundaries.md) — grounds: actor allocation must be justified independently
- [Inspectable artifacts, not supervision, defeat the black-box problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — grounds: inspectability enables evaluation without establishing it
- [Error correction works with above-chance, decorrelated oracles](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — grounds: discrimination and correlation conditions for checks
- [LLM generation can hide a relaxed goal where human writing exposes a stall](./llm-generation-relaxes-goals-where-human-writing-stalls.md) — mechanism: why a dropped constraint leaves no mark in fluent text for a reviewer to find
- [Reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md) — grounds: why a reviewer can pass a true conclusion reached through an invalid route
- [Vibe noting](./vibe-noting.md) — grounds: persistence, activation, and verification are separate properties
