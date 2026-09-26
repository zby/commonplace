---
description: "When writing is delegated to an agent, a recorded commit-challenge-respond loop can prove that one flawed claim was fixed, but not that the method is reliable or matches solo writing; explains which composition-exposed errors LLM reviewers can and cannot catch."
type: types/note.md
traits: [title-as-claim, synthesis, has-external-sources]
tags: [foundations]
---

# A recorded composition loop can establish a local correction without validating the method

People who write to think report that writing a claim out by hand exposes weak ideas. When an agent drafts the prose instead, that exposure can be lost. This note asks whether a writing workflow split between people and agents can keep it, and what evidence would show that it has.

The answer is narrower than "yes" or "no." Suppose the workflow keeps a record of three things: the claim as committed before acceptance, a challenge that points to a specific fault in it, and the response to that challenge. If a separate judge then confirms that the fault was real and that the response resolved it, the record proves one local result: this artifact was corrected. The response may fix the claim, narrow it, or reject it. The record does not prove that the method works reliably across cases, that it matches solo writing, or that any one step caused the improvement. Those claims need different evidence.

## What hand composition does

"Writing is thinking" is usually stated as a slogan. Here it names a set of operations that a writer performs while composing a substantive claim:

- **Commit.** The writer must choose exact words, so a vague idea becomes one definite claim with definite premises.
- **Expose a failing step.** Writing out the route from premises to claim makes a weak step visible. The writer reaches a "because" and cannot finish the sentence. [The composition stall](./llm-generation-relaxes-goals-where-human-writing-stalls.md) describes this: the failure shows up at the point where it occurs.
- **Test against cases.** A definite claim can be checked against counterexamples. A counterexample to one premise calls for revising that premise; a counterexample to the conclusion calls for replacing or rejecting it.
- **Revise or discard.** The writer changes the claim, narrows it, or drops it.

This note calls the combined effect of these operations the **writing-is-thinking filter**: weak claims tend to be caught before they are published. [Putting ideas into words](../sources/putting-ideas-into-words.ingest.md), [thinking through conjecture and counterexample](../sources/how-to-think-in-writing.ingest.md), and [learning by iterated writing](../sources/learning-by-writing.ingest.md) describe these operations from the practice of individual writers. They are practitioner accounts, not controlled comparisons. They show what the operations are; they do not show how often the filter works, or that any other arrangement reproduces it.

**Naive prose delegation** skips the filter. Someone gives an agent a seed idea, reads the generated prose once, and approves it. No step in that workflow forces a commitment, exposes a failing step, or records a challenge. [LLM generation can hide a relaxed goal](./llm-generation-relaxes-goals-where-human-writing-stalls.md): a model can drop a constraint it cannot meet and still produce fluent prose, with nothing on the surface marking where the constraint went missing. The writing is out of scope when its substance is already settled elsewhere: rendering fixed content, transcription, and stylistic editing lose nothing, because there is no search for a claim to lose.

## A record contract that keeps the operations visible

One candidate way to keep the filter's operations in a split workflow is to record each of them as a separate handoff. This contract is a design choice for unsettled substantive claims. It is neither canonical nor validated.

- **Commit-and-expose** records the claim before acceptance, together with its constraints, premises, and the route from premises to claim.
- **Challenge-and-locate** records objections tied to specific premises, counterexamples, and missing support, each with a proposed location of the fault. It does not record a global grade.
- **Respond-and-decide** records a status for every challenge. "Investigate" is an interim status. A final status does one of four things: rejects the challenge with cited support, revises or narrows the claim, rejects the claim, or keeps the uncertainty explicit at acceptance.

The hand-composition operations motivate these three handoffs. They do not show that the handoffs keep the operations' effects.

Keeping the input, the challenge, and the response makes each handoff inspectable afterwards. Two roles stay distinct: the **checker**, who looks for faults, and the **acceptor**, who has authority to admit the artifact into the KB. Either role may be filled by a person, an agent, or a fixed policy, provided the choice has its own justification. [Human analogies suggest functions, not component boundaries](./human-analogies-suggest-functions-not-component-boundaries.md), so the fact that a solo writer performs both roles does not mean one actor must. To test a given allocation, the record must also say who or what filled each role and under what conditions. Naive delegation keeps no such record, so its output cannot be audited this way.

## Which composition errors LLM reviewers can and cannot catch

If an agent fills the checker role, the question is whether it catches the errors that hand composition would have exposed. The KB holds no measurement of LLM critics on this task. It does hold findings about adjacent tasks that bear on it. Together they suggest that the answer depends on whether the error is visible in the text the reviewer receives.

**Errors a reviewer has a reason to catch.** Some errors are visible once the commitment is written down. Examples: a step that does not follow from the premises stated next to it, two stated claims that contradict each other, or a counterexample to a stated premise. For these, the reviewer's task is local: compare a written step with written premises. A reviewer that starts from a fresh context also does not share the drafting agent's reasoning trace. So it does not inherit errors that came from that trace, as [decorrelated reviewers still share the field's prior](./reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) explains. This is an argument about where a critic could have signal, not evidence that current critics have it.

**Errors a reviewer has reasons to miss.** Four mechanisms work against the reviewer.

1. **The reviewer can check the conclusion instead of the route.** [Reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md). In a benchmark where six models graded math solutions, their written evaluations often showed the model solving the problem itself and then endorsing invalid submitted steps once the final answer matched. That is a math-grading result, and the authors' reading of it is suggestive rather than causal. But it matches the error hand composition is best at exposing: a conclusion that may well be true, reached through a step the writer cannot justify. A reviewer that agrees with the conclusion may pass the step.
2. **The dropped constraint is not in the text.** When generation silently drops a constraint, the constraint existed in the author's intent, not in the prose. A reviewer that sees only the prose has nothing to compare it against. A hand writer who stalls knows the constraint because they are trying to satisfy it.
3. **Reviewer and generator share a prior.** The drafting model tends to relax a goal toward the most plausible weaker version. A reviewer trained on similar data may find that same version plausible. [Error correction needs above-chance, decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md), and that note reports that content biases in reasoning are shared across model families and persist through scaling and instruction tuning. Using a different model therefore does not by itself make the reviewer's errors independent of the generator's.
4. **The reviewer's confidence does not flag its own misses.** [Generation confidence does not by itself certify soundness](./generation-confidence-does-not-by-itself-certify-soundness.md), and [the augmentation-automation boundary is discrimination, not accuracy](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) reports that across model releases calibration improved while per-instance discrimination did not. A reviewer whose overall verdicts are usually right may still be unable to tell which of its verdicts are wrong.

This split explains why commit-and-expose carries weight in the contract. Writing the claim, constraints, premises, and route down before review moves errors from the second group into the first: a constraint that is written down can be checked, and a route that is written down can be checked step by step. It also explains why challenge-and-locate asks for premise-linked objections rather than a grade, since a grade lets the reviewer answer from conclusion agreement. Neither move shows that current critics succeed. An error that never reaches the written commitment stays invisible to a critic that reads only the record.

## What each claim needs as evidence

The evidence must match the level of the claim.

- **A local correction** needs independent adjudication of both the reported fault and the final response. The adjudicator must confirm that the resulting claim resolves the fault, not merely that the text changed. **Independent adjudication** here means a separate role that applies a stated criterion to the recorded fault and response. Using a different actor does not by itself make it independent.
- **A reliable critic** needs to be shown to separate supported from unsupported arguments, where support has been decided independently. Test sets should include true conclusions reached through invalid routes, because that is the case the first mechanism above predicts a critic will miss. When several checks are counted as independent evidence, the correlation of their errors must also be measured.
- **A comparison with solo writing** needs a specified baseline, role allocation, and measurement rule. Attributing a result to one step of the loop needs evidence at the level of that step.

The evidence available here gives commit-and-expose no test of completeness: nothing shows that the record captured every commitment the claim depends on. It also supplies no calibrated prose critics and no comparison between the loop and solo writing.

Neither the actor's identity nor an approval substitutes for these tests. Reviewing finished prose can invite **passive assent**, as a [practitioner account of substantive AI writing](../sources/why-almost-never-use-ai-to-write-anything-substantive.ingest.md) argues: fluent generated wording **anchors** the reviewer, who then approves sentences instead of re-deriving the claims and constraints behind them. A human approval establishes the authority to admit an artifact. It does not establish that the route was checked or that a reported fault was corrected. Which actor fills a role may still affect performance, so that choice must be evaluated rather than used as a stand-in for evaluation.

## Separate outcomes

The loop can have three different outcomes, and each needs its own evidence.

- An **artifact outcome** is a claim that was corrected or justifiably rejected.
- A **human-understanding outcome** is a change in what the person knows. It needs an independent probe of whether the person can restate, update, or apply the claim, its route, or its uncertainty. Assent, or a restatement copied from the text, does not count.
- A **later-system outcome** is a change in what the system does later. It needs the artifact to be retrieved when relevant and to change a later use or decision. Being stored is not enough.

**Acceptance** records admission authority and proves none of these outcomes. The available evidence supports the record design and the conditional local artifact result. It does not support a general validation of the method.

## Scope

- The claim covers substantive writing where composing the text is part of finding the claim. It does not cover rendering, transcription, or editing of settled content.
- The three-handoff contract is one candidate design, not the only way to keep the filter's operations. The claim about evidence levels does not depend on this particular contract.
- The analysis of LLM reviewers rests on findings from adjacent tasks: math grading, reasoning tasks with content effects, and model confidence. It predicts where prose critics should succeed and fail, but it has not been tested on prose critique of KB notes.

## Open Questions

- Can blinded prose critics distinguish invalid routes from valid arguments well enough to be useful, with errors that are sufficiently uncorrelated with each other and with the generator's?
- What task-specific criterion could show that commit-and-expose captured every commitment the claim depends on?
- Does recording the commitments before showing the acceptor any generated prose reduce anchoring?
- Under which allocation of roles, if any, does a measured outcome reach a solo-writing baseline?

---

Relevant Notes:

- [Human analogies suggest functions, not component boundaries](./human-analogies-suggest-functions-not-component-boundaries.md) — grounds: actor allocation must be justified independently
- [Inspectable artifacts, not supervision, defeat the black-box problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — grounds: inspectability enables evaluation without establishing it
- [Error correction works with above-chance, decorrelated oracles](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — grounds: discrimination and correlation conditions for checks, and shared content bias across model families
- [Vibe noting](./vibe-noting.md) — grounds: persistence, activation, and verification are separate properties
- [LLM generation can hide a relaxed goal where human writing exposes a stall](./llm-generation-relaxes-goals-where-human-writing-stalls.md) — mechanism: why a fluent draft can omit a constraint without marking where, so the reviewer cannot see it in the text
- [Reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md) — grounds: reviewers can substitute conclusion agreement for route checking, the error class hand composition exposes
- [Generation confidence does not by itself certify soundness](./generation-confidence-does-not-by-itself-certify-soundness.md) — grounds: fluency and confidence do not mark which steps are unsound
- [The augmentation-automation boundary is discrimination not accuracy](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — grounds: per-instance discrimination, not aggregate accuracy, decides whether a reviewer can flag its own misses
- [Decorrelated reviewers still share the field's prior](./reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) — extends: fresh-context review removes errors from the author's trace but not errors from a shared prior
