---
description: "Defines the writing-is-thinking filter as three operations a human-agent critique loop can split across roles, explains which composition errors LLM reviewers catch or miss and why, and separates one corrected claim from evidence that the method works."
type: kb/types/note.md
traits: [title-as-claim, synthesis, has-external-sources]
tags: [foundations]
---

# A human-agent critique loop can relocate the error exposure of solo composition

When a person writes out an argument by hand, the writing itself exposes some of their errors. They try to state the claim in exact words and find that it says less than they meant. They write "because" and find that the reason does not support the conclusion. They list what the design must achieve and find that two of the goals conflict. Writers call this "writing is thinking". This note calls it the **filter**: errors that survive in a vague idea get caught when the idea has to take a definite written form.

The filter is lost when an LLM drafts the text and a person only approves it. The claim of this note is that the filter is not tied to one person holding the pen. It consists of operations, and those operations can be split across roles: one party commits to a claim, another challenges it, and a third decides what happens to it. A loop that records each step can show that a specific error was exposed and corrected. That is the weakest version of the claim, and it is the only version the available evidence supports. It is an existence claim: one recorded, independently confirmed correction witnesses it. The note does not claim that such a loop catches as many errors as solo writing, that it is reliable across cases, or that any one step caused an improvement. Each of those claims needs evidence of a different kind, described below.

## The filter as three operations

Three accounts of writing as a way of thinking describe the same sequence: [putting ideas into words](../sources/putting-ideas-into-words.ingest.md), [thinking through conjecture and counterexample](../sources/how-to-think-in-writing.ingest.md), and [learning by iterated writing](../sources/learning-by-writing.ingest.md). All three are reports of practice, not controlled comparisons. Read together, they describe three operations:

1. **Commit-and-expose.** State the claim in exact words, with its constraints, premises, and the reasoning route from premises to conclusion. Until this happens, a weak point has nothing definite to attach to.
2. **Challenge-and-locate.** Find a specific weakness: a premise that does not hold, a counterexample, missing support, or goals that cannot all be met. The output is a located objection ("this 'because' does not support that step"), not an overall grade.
3. **Respond-and-decide.** Do something about each objection: reject it with reasons, revise or narrow the claim, drop the claim, or accept it with the uncertainty stated.

A solo writer performs all three in one head, often without noticing the boundaries. The stall at a failing "because" is the moment operation 2 fires. These accounts motivate the three-operation breakdown. They do not show that splitting the operations across roles preserves what they achieve for a solo writer. The breakdown is one workable taxonomy, not a validated or canonical one.

## Why an LLM draft removes the filter

A human writer who reaches a constraint they cannot satisfy may stall at that point. An LLM does not stall. It can return fluent text in which one constraint was silently dropped, and nothing on the surface shows where, as argued in [LLM generation can hide a relaxed goal where human writing exposes a stall](./llm-generation-relaxes-goals-where-human-writing-stalls.md). The text's fluency is no evidence that the goal was met, because [generation confidence does not by itself certify soundness](./generation-confidence-does-not-by-itself-certify-soundness.md). So when an LLM drafts, operation 2 no longer happens as a side effect of writing. If it happens at all, some other step must perform it.

## Which errors LLM reviewers catch and miss

The obvious replacement is an LLM reviewer. Whether that works depends on the kind of error. The following is a mechanism-based account, not a measured error rate. Each mechanism predicts a class of error that a reviewer will tend to miss, and each is testable.

**What a reviewer can catch.** A reviewer can check whatever is on the page against whatever else is in its context. That covers contradictions between two sentences of the text, a cited claim that a supplied source does not support, a known counterexample to a stated generalization, and a missing step when the reviewer is told to list each inference and test it. A reviewer that did not write the text also lacks the author's reasoning trace, so it does not share errors that came from that trace. For these error classes, an LLM reviewer can plausibly perform operation 2.

**What a reviewer tends to miss, and why.**

- **Faulty routes to acceptable conclusions.** The composing writer is checking the route: does *this* reason support *this* step? A reviewer asked whether an argument works may instead derive the conclusion by its own route and check that the answers agree. In math grading, models that did this overlooked invalid steps once the final answer matched; see [reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md). Route faults are the core of what composition exposes, so they are the class most at risk.
- **Constraints that are absent from the text.** A dropped constraint leaves no trace in the draft. A solo writer knows what they were trying to achieve and notices when it is missing. A reviewer sees only the finished text, so it has nothing to compare against. It can notice an omission only if the constraints were written down before the draft existed. This is why operation 1 has to be recorded, not left implicit.
- **Errors the field shares.** Reviewers drawn from one training distribution share its consensus. Using a second model or a fresh context removes errors from the author's reasoning, but not errors the whole field makes; on those, several reviewers converge on the same mistake. The same prior makes reviewers push against claims that contest the consensus, whether or not the claim is wrong. See [decorrelated reviewers still share the field's prior](./reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md).
- **Overall grades.** Asked for a verdict such as "is this sound?", a reviewer can be right most of the time and still fail to tell which particular arguments are unsound. Checking only helps when the checker accepts sound arguments more often than unsound ones, and when repeated checks do not fail together, as [error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) explains. An overall grade hides whether either condition holds. A located objection can be checked directly.

Human approval has a related weakness. Reading fluent finished prose may invite passive assent: the reviewer endorses sentences instead of working out the distinctions they would have had to make while writing, as a [practitioner account of substantive AI writing](../sources/why-almost-never-use-ai-to-write-anything-substantive.ingest.md) argues.

None of this shows that LLM reviewers cannot perform operation 2. It shows which conditions a loop has to supply for them to have a chance: commitments recorded before the draft, so that omissions become visible; objections aimed at specific steps, not overall grades; checkers whose errors are not correlated with the author's or with each other; and a separate judge for each outcome. Whether a particular reviewer meets these conditions is something to measure, not something to assume from its model or its role.

## What the loop records

A loop that relocates the filter keeps a record of each operation:

- **Commit-and-expose** records the claim before acceptance, with its constraints, premises, and reasoning route.
- **Challenge-and-locate** records each objection, the premise it targets, and where the fault is proposed to lie.
- **Respond-and-decide** records a status for every objection. "Investigate" is an interim status. A final disposition rejects the objection with cited support, revises or narrows the claim, drops the claim, or keeps the claim with its uncertainty stated.

The record makes each handoff inspectable. The roles of checker and acceptor stay distinct, and a human, an agent, or a fixed policy may fill either one when that choice has its own justification; [human analogies suggest functions, not component boundaries](./human-analogies-suggest-functions-not-component-boundaries.md). To test a particular assignment of roles, the record must also say who or what filled each role and under what conditions.

The contrast case is **naive delegation**: someone supplies a seed idea, an LLM writes the text, and the person accepts it after reading it through. No operation leaves a trace, so the record cannot support any of the checks below.

## What a record can and cannot show

Different claims need different evidence.

- **One corrected claim.** Suppose a recorded objection identifies a fault that the argument depends on. The record shows a local correction when an independent judge confirms two things: that the fault was real, and that the final claim resolves it, not merely that the claim changed. Here an **independent judge** is a separate role that applies a stated criterion to the recorded objection and response. Being a different person or model is not enough to make it independent.
- **A reliable reviewer.** A reviewer is reliable only if it separates sound from unsound arguments on cases where the answer has been independently settled. The test cases should include true conclusions reached by invalid routes, because that is the error a reviewer is most likely to miss. When several checks are counted as independent evidence, their error correlation must also be measured.
- **A loop as good as solo writing.** Comparing the loop with solo writing needs a stated comparator, a stated assignment of roles, and a measurement rule. Crediting the result to one step needs evidence about that step.

No such evidence exists for the loop described here. There is no criterion for when operation 1 has captured every commitment that matters, no calibrated test of prose reviewers, and no comparison of the loop with solo writing. The evidence supports the record design and the single-case correction result, not the method in general.

Neither the identity of an actor nor an approval substitutes for these tests. Human approval can give an artifact the authority to be admitted, but it cannot show that the route was checked or that a reported fault was corrected. Which actor fills a role may affect results, so that choice has to be evaluated, not used as a proxy for quality.

The tests also keep apart outcomes that are easy to run together:

- An **artifact outcome** is a claim that was corrected, or justifiably dropped.
- A **human-understanding outcome** needs a separate probe of whether the person can restate, update, or apply the claim, its route, or its uncertainty. Assent or copied restatement does not count.
- A **later-system outcome** needs the claim to be retrieved when relevant and to change a later use or decision. Being stored is not enough; see [vibe noting](./vibe-noting.md).
- **Acceptance** records that the artifact was admitted. It shows none of the three outcomes above.

## Scope

- The claim covers substantive claims that are still unsettled, where writing is doing the work of finding out what is true. Rendering, transcription, and copy editing are outside scope when the claims and checks are fixed elsewhere.
- The account of what LLM reviewers miss rests on mechanisms and on one domain-specific result (math grading). How often each miss occurs for prose arguments has not been measured.
- The note claims no advantage for the loop over solo writing, and no disadvantage. Either claim needs a comparison that has not been run.

## Open Questions

- Can blinded prose reviewers tell invalid routes from valid ones well enough to be useful, with errors that are not strongly correlated?
- Which of the missed error classes above is most common in practice for prose arguments?
- What task-specific criterion can show that commit-and-expose captured every commitment the argument depends on?
- Does recording the commitments before the acceptor sees generated prose reduce anchoring?
- Which measured outcome, if any, reaches a solo-writing baseline when the roles are split?

---

Relevant Notes:

- [Human analogies suggest functions, not component boundaries](./human-analogies-suggest-functions-not-component-boundaries.md) — grounds: actor allocation must be justified independently
- [Inspectable artifacts, not supervision, defeat the black-box problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — grounds: inspectability enables evaluation without establishing it
- [Error correction works with above-chance, decorrelated oracles](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — grounds: discrimination and correlation conditions for checks
- [Vibe noting](./vibe-noting.md) — grounds: persistence, activation, and verification are separate properties
- [LLM generation can hide a relaxed goal where human writing exposes a stall](./llm-generation-relaxes-goals-where-human-writing-stalls.md) — grounds: why an LLM draft removes the stall that performs challenge-and-locate for a solo writer
- [Reasoning production is not reasoning evaluation](./reasoning-production-is-not-reasoning-evaluation.md) — mechanism: why reviewers miss faulty routes to acceptable conclusions
- [Decorrelated reviewers still share the field's prior](./reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) — mechanism: why decorrelating reviewers leaves field-wide errors uncaught
