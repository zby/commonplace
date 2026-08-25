---
description: "Grunewald's critique exposes passive-assent risk and a gap between expert interpretation of a writing commission and generic LLM completion"
source: https://www.erichgrunewald.com/posts/why-i-think-you-should-almost-never-use-ai-to-write-anything-substantive/
captured: "2026-08-06"
capture: web-fetch
genre: conceptual-essay
snapshot_sha256: 15daf09817d95cbcedd639a30f4b05514b314851a0da86233ede134e1f39fa2e
ingested: "2026-08-06"
type: kb/sources/types/ingest-report.md
domains: [writing-as-thinking, llm-reliability, human-ai-collaboration, authorship]
---

# Ingest: Why You Should Almost Never Use AI to Write Anything Substantive

## Classification

An argumentative essay built from quotations, first-person experience, and one worked model-output critique rather than a controlled study.
Author: Erich Grunewald is a [Senior Researcher on the Institute for AI Policy and Strategy's compute policy team](https://www.iaps.ai/erich-grunewald), specializing in AI chip export controls and data-center security. That makes his line-by-line chip-smuggling audit unusually informed, but it does not give the essay's broader cognitive and ethical claims empirical authority.

## Summary

Grunewald argues that current AI models should almost never draft substantive prose, even from detailed notes and even when a human edits the result. His case has three parts: composition is part of forming and testing the thought rather than merely transcribing it; fluent AI prose contains dense, hard-to-notice vagueness and error that an expert must re-derive the subject matter to catch; and presenting such prose without disclosure violates an implicit reader-writer contract that the text represents the named author's considered thought. A detailed audit of an AI-generated paragraph on chip smuggling illustrates the second claim. He exempts logistics text, brainstorming, feedback, deliberately accepted line edits, and sometimes translation, and he limits the argument to current and near-term models.

## Quotes

No source quotes have been retained yet.

## Connections Found

The chip-smuggling example compares with [A bare writing prompt does not determine its intended contribution](../notes/a-bare-writing-prompt-does-not-determine-its-intended-contribution.md): a sparse request may cue an expert to contribute distinctive judgment and find what is worth saying while cueing a model only to instantiate the requested prose form. The source is also a stress test for [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md): Grunewald agrees that naive delegation loses the filter but argues that post-hoc editing may still fail because generated wording anchors an expert toward passive assent and omits sensitivities the expert would have expressed while composing. His chip-smuggling audit is a concrete instance of [LLM generation relaxing a goal while hiding the dropped constraint](../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md), and it illustrates the operational consequence of [Generation confidence not certifying soundness by itself](../notes/generation-confidence-does-not-by-itself-certify-soundness.md): the audit re-derives correctness instead of treating fluent generation as certification. Relative to [Borretti's earlier polemic](https://borretti.me/article/human-routers-of-machine-words), this essay independently restates the writing-as-thinking and reader-burden arguments, while adding a domain-expert error audit, clearer exceptions, and an explicit disclosure-and-trust claim.

## Extractable Value

1. **A writing commission implies more than an output form** -- A commissioned expert normally infers that the request calls for their particular knowledge and judgment, including finding an interesting contribution. The model's generic completion is therefore a meaningful default failure, but it does not by itself show that the model lacks relevant knowledge or that a workflow cannot elicit a richer objective. [quick-win]

2. **Human review can preserve the generator's blind spots through anchoring and passive assent** -- The existing adversarial-loop note makes human judgment load-bearing; Grunewald identifies a sharper failure condition: reading and endorsing already-fluent prose may not recover the tacit distinctions that productive generation would have forced the expert to make. The review must re-derive constraints, not merely approve sentences. [quick-win]

3. **The useful delegation boundary is whether prose is still doing epistemic search** -- The essay's exceptions separate settled rendering and coordination (copy edits, formulaic logistics, some translation) from composition that discovers the claim. This supports the scope line in the hidden-relaxation note more precisely than an artifact-level rule such as “never use AI for reports.” [quick-win]

4. **Verification cost comes from dense local defects, not only headline hallucinations** -- The chip-smuggling paragraph is broadly plausible yet contains many small substitutions: an irrelevant property, ungrounded ranges, missing dates and definitions, empty “matters” language, and generic applause. A useful evaluation would measure this defect density and the domain expertise needed to detect it, rather than score only whether the paragraph's central thesis is correct. [experiment]

5. **Disclosure changes the evidence a reader can infer from authorship** -- The reader-writer contract frames a byline as evidence that the named author performed enough cognitive work to stand behind the text. Labeling model-generated passages lets readers discount that evidence explicitly; leaving them unlabeled makes provenance and behavioral authority easy to overread. [deep-dive]

6. **Independent corroboration of the writing-is-thinking critique** -- Grunewald reaches much of Borretti's mechanism independently and with less rhetorical heat. This is useful as a second source for the critique, but it is corroborating argument, not independent empirical evidence. [just-a-reference]

## Limitations (our opinion)

This is editorial opinion, and the “almost never” conclusion outruns the evidence. The model-quality case rests on one author-selected output in the author's strongest domain, with no human-written baseline, disclosed prompt beyond one sentence, repeated samples, blinded judges, or comparison among drafting workflows. It demonstrates that a plausible paragraph can hide many defects; it does not estimate how often that happens or whether a specified review loop reduces it.

The sparse prompt nevertheless reveals a meaningful ordinary-use asymmetry, not merely an unfair setup. A commissioned expert normally infers that the request is for their particular knowledge and judgment and that they should find an interesting contribution. The model may instead treat the same words as a request for plausible topical prose. That supports a default failure of task construction, but it does not distinguish missing knowledge from failure to reconstruct the implicit objective or show what happens when a workflow supplies evidence, audience, contribution criteria, and angle search. Retrieval can add facts; it does not by itself decide what is worth saying.

The essay also treats drafting and reviewing as a nearly fixed cognitive asymmetry without testing the stronger workflow already proposed in the KB. [The adversarial-loop note](../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) does not claim that a human rubber stamp is enough; it requires adversarial recomputation and keeps the human as judge. Grunewald's passive-assent mechanism is a serious objection to that design, but not a refutation of it. His trust contract is similarly context-dependent: disclosure norms, collaborative authorship, accessibility needs, and a reader's reason for trusting a document can change what a byline implies. The essay's categorical treatment of non-native writers especially under-argues those tradeoffs.

## Recommended Next Action

Update [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) with an `evidenced-by` link to this snapshot and a named **anchoring/passive-assent failure condition**: human presence is insufficient unless review re-derives the draft's claims and constraints strongly enough to surface tacit expert distinctions that generation may have erased.
