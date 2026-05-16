---
description: "Lech Mazur's public benchmark announcement compressing the headline position-bias result, the GPT-5.4 callout, and the operational motivation from everyday comparison prompts"
source_snapshot: "kb/sources/does-an-llm-keep-the-same-judgment-when-you-swap-the-answer-order.md"
ingested: "2026-04-23"
type: kb/sources/types/ingest-report.md
source_type: tool-announcement
domains: [evaluation, judge-reliability, position-bias, llm-as-judge]
---

# Ingest: Thread by @LechMazur

Source: kb/sources/does-an-llm-keep-the-same-judgment-when-you-swap-the-answer-order.md
Captured: 2026-04-23T16:14:07.941709+00:00
From: https://x.com/LechMazur/status/2046661738339430489

## Classification

Type: tool-announcement -- this is a public launch thread for a new benchmark/repo rather than the benchmark artifact itself; it highlights headline findings, links to the repository, and frames why the failure mode matters.
Domains: evaluation, judge-reliability, position-bias, llm-as-judge
Author: Lech Mazur is already represented in this KB through the deeper [position-bias benchmark ingest](./position-bias.ingest.md); the signal here is not institutional authority but that he is the benchmark author summarizing and motivating his own measurement artifact.

## Summary

Mazur announces a new position-bias benchmark for LLM judges: show the same pair of lightly edited stories twice with the display order swapped, then measure how often the model's underlying preference flips. The thread compresses the main findings into a few public-facing numbers: the average judge picks the first-shown answer 63% of the time, the median decisive-case flip rate is high enough to make order sensitivity a dominant failure mode, and GPT-5.4 (high) is singled out as especially position-sensitive. Relative to the repo snapshot already in the KB, the thread's distinct contribution is not methodology depth but a compact launch surface, the author's operational motivation ("this kept happening in regular-use comparison prompts"), and reply links pointing toward human order-effect literature.

## Connections Found

Connect found two kinds of fit. First, this thread is a strong **source-to-source compare-with** for [position-bias.ingest.md](./position-bias.ingest.md): the repo ingest remains the authoritative evidence substrate, while this thread is the compact public summary and motivation surface for the same benchmark family. Second, it offers lighter-weight `evidence` for the existing note cluster around pairwise judging and prompt-variation diagnostics: [Brainstorming: how to test whether pairwise comparison can harden soft oracles](../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md) already lists position bias as a failure mode to measure; [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) treats order-swapping as a textbook diagnostic perturbation; and [Operational signals that a component is a relaxing candidate](../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) predicts exactly this kind of brittleness under reordering. Connect also flagged [Agent Skills for Context Engineering](../agent-memory-systems/reviews/agent-skills-for-context-engineering.md) as an evidentially strong but outbound-label-misaligned match: the review recommends order-swapping pairwise comparisons, and this thread is a concise public example of why.

## Extractable Value

1. **Production-relevance signal for judge bias** -- The most transferable new point is the author's motivation: this was not only a lab curiosity but a failure mode encountered in ordinary comparison prompts. That helps argue that order contamination matters in everyday soft-oracle workflows, not just curated eval harnesses. [quick-win]
2. **Compact citation surface for the headline result** -- The thread is a low-cost way to cite the public-facing headline numbers and the GPT-5.4 callout when you do not need the full repo evidence tree. Low reach, but operationally convenient. [just-a-reference]
3. **Bridge from LLM position bias to older human order-effect literature** -- The replies surface external references on human response-order effects, which makes the benchmark easier to frame as an instance of a broader judgment problem rather than an LLM-only oddity. This is a hypothesis bridge, not a settled comparison, but it is new relative to the repo ingest. [experiment]
4. **Human-vs-LLM baseline question becomes explicit** -- The reply claiming humans look less order-biased than the LLM judges sharpens a concrete follow-up question: how much of the benchmark result is generic judgment-order sensitivity and how much is model-specific contamination? The thread does not answer it, but it names the right comparison. [deep-dive]
5. **Announcement threads and repo snapshots should be treated as separate source surfaces** -- The repo ingest carries method and data; the launch thread carries motivation, narrative compression, and a public-summary entry point. Keeping both surfaces distinct is useful when the same external artifact has both an evidential substrate and a more navigable explanatory wrapper. [quick-win]

## Limitations (our opinion)

This thread should not be trusted as the main evidence source for the benchmark. It is derivative of the repository snapshot already ingested in [position-bias.ingest.md](./position-bias.ingest.md), and it omits the methods, scope caveats, raw outputs, and dataset structure that make the repo artifact usable as evidence. The strongest numeric claims are stated without methodological context here, so any serious downstream note should cite the repo ingest rather than this thread where possible. The human-order-effect bridge is also thin in this source: the replies point to papers and assert that humans look less biased, but the thread does not show a controlled human-vs-LLM comparison. A simpler account for most of the thread is "public summary of an already-captured benchmark," and that simpler account mostly wins. The distinctive value is packaging and motivation, not new explanatory reach.

## Recommended Next Action

Update [position-bias.ingest.md](./position-bias.ingest.md): add a short paragraph noting that the benchmark was motivated by failures in ordinary comparison prompts and that Mazur's launch thread also points toward human order-effect literature, because the repo ingest already carries the main evidence and this thread's main value is incremental context rather than a new note-worthy claim.
