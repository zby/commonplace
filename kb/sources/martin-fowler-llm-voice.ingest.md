---
description: "Fowler separates aversion to perceived LLM prose from writing as thinking, bounding drafting prohibitions with accessibility and process-communication exceptions."
source: https://martinfowler.com/bliki/LLM-Voice.html
captured: "2026-10-30"
capture: trafilatura
capture_scope: full-source
genre: conceptual-essay
snapshot_sha256: 25fb8ea0a572738a986e31a30d7f01e1d5c83059ca5274ee0a5e714b5c522286
ingested: "2026-10-30"
type: types/ingest-report.md
domains: [llm-prose, writing-as-thinking, reader-reception, writing-accessibility]
learning_claims: true
---

# Ingest: LLM Voice

## Classification

A first-person essay offering writing advice and an argument about composition, not a controlled study of prose detection or learning. Author: Martin Fowler, an established software author describing his own reading reactions, writing practice, and editorial policy.

## Summary

Fowler reports losing interest in prose he perceives as LLM-written, while doubting both automated detection and his own ability to distinguish model output from changing human idiom. He recommends that authors write their own prose rather than edit generated drafts, and is wary even of suggested rephrasing. Separately, he argues that composing sentences exposes confusion and brings thoughts into coherence; delegating composition may therefore surrender thinking and the practice needed to become a better writer. These concerns are independent: indistinguishable model prose could still bypass the author's thinking. His advice is not absolute. He reports one professionally edited exception to detectable LLM voice, welcomes assistance that enables a colleague with Parkinson's disease to write, is ambivalent about translation, and permits delegation for process-oriented correspondence. Possible model-only documentation is a speculation, not an observed audience shift.

## Quotes

No source quotes have been retained yet.

## Connections Found

Fowler supplies a scope counterpoint to [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../theory/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md). That note proposes separating generated rendering from human and agent scrutiny. Fowler raises a different outcome requirement: even a scrutinized argument may repel human readers through its perceived voice. Recovering thought-testing would not by itself establish acceptable reception. Conversely, his dislike of the prose does not refute the loop's ability to expose errors. His accessibility exception also bounds any blanket prescription to eliminate generated prose: enabling an author to communicate can outweigh a reader's stylistic preference.

Commonplace is a working instance of the model-only documentation Fowler names as a speculation. The [landing page](../index.md) states the premise: LLM-written text can be useful even when no person reads it directly, because it can improve how an LLM answers your questions. The maintainer stated the same premise in the [Hacker News discussion of the essay](https://news.ycombinator.com/item?id=50301386), together with the gap-filling account that [LLM generation can hide a relaxed goal where human writing exposes a stall](../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md) develops. Fowler's reception concern therefore applies to this KB's human-facing surfaces, not to its premise.

## Learning Claims (our opinion)

Fowler's proposed mechanism is practice through composition: putting thoughts into words reveals confusion, and working through it develops understanding and writing skill. In [theory-builder](../theory/definitions/theory-builder.md) terms, written sentences provide localized content. Consumption is suggested by his report that composing brings his own thoughts into coherence, but no decision trace shows how a particular statement changes subsequent work. Content-directed criticism is plausible in his struggle with confusion, though the essay supplies no explicit refutation or comparison with rival explanations. Iteration is suggested by his habit of writing and then editing, without a worked sequence demonstrating that a stated criticism shapes the next version. A written artifact persists; the essay does not trace reuse of criticism across projects. Improved future writing capacity and its loss under delegation remain assertions, not measured outcomes. This is a partial conceptual mapping, not evidence that all four conditions are met. It supports investigating composition as a site of criticism, but does not establish that physical authorship is necessary or that an adversarial drafting workflow cannot preserve learning.

## Extractable Value

1. **Separate scrutiny from reception.** The existing adversarial-loop account addresses recovering thought-testing. Fowler adds a distinct acceptance risk for human-facing KB prose: a reader can disengage from perceived model voice regardless of actual provenance or argumentative quality. Treat the outcomes separately rather than using successful review as a proxy for reception. [quick-win]
2. **Bound voice-oriented rules by communication purpose and access.** Accessibility assistance and process correspondence are explicit exceptions; translation remains a tension rather than an endorsement. These cases make a universal ban on generated drafts a poor transfer from this essay to an agent-operated KB. [just-a-reference]

## Limitations (our opinion)

The essay establishes Fowler's stated preferences and policy, not their prevalence among readers. Its uncanny-valley framing names his reaction without isolating its cause. No blinded comparison separates wording, provenance expectations, topic, or substance. His acknowledged uncertainty about detection means perceived voice cannot establish actual authorship. The professional-editor example limits an absolute claim that editing cannot remove the voice, but gives no basis for estimating how often or at what cost editing succeeds. Writing as thinking is an introspective account with no comparison against assisted composition plus substantive review; it cannot rank those workflows or establish a causal loss of future skill. Accessibility benefits are reported through one colleague, not evaluated across users. These limits leave the essay useful as a warning and a boundary case, not tested KB methodology.

## Recommended Next Action

Review `kb/theory/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md` to distinguish recovery of argumentative scrutiny from human acceptance of the resulting prose, using Fowler's essay as an anecdotal scope qualification rather than a refutation.
