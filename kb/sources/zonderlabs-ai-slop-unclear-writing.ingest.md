---
description: "Zonder Labs names three clarity faults in work-context AI prose (hidden characters/actions, vague wording, empty statements) and says style tells are not the problem; rates uncaptured"
source: https://zonderlabs.com/slop
captured: "2026-11-11"
capture: trafilatura
capture_scope: partial-source
genre: practitioner-report
snapshot_sha256: 520ed773344d97ba9566f86fee71ce6c5c19d85d62999719ff6fd1823eeda2d3
ingested: "2026-11-11"
type: types/ingest-report.md
domains: [ai-writing, clarity-faults, williams-style, claude-code-replies]
tags: [prose-readability]
---

# Ingest: Why is AI Slop so Frustrating to Read?

## Classification

A research-lab blog post dated 2026-11-09 that reports the authors' own annotation work. It argues from worked examples and reports measurements, but it publishes no method, annotator count, agreement statistic or sample description in the captured prose. It is therefore a practitioner report, not a scientific paper.
Author: Zonder Labs, a group that publishes research updates on AI writing. The writer speaks in the first person and works with Claude Code on GPU inference code. The post builds on Joseph Williams's *Style: The Basics of Clarity and Grace* and cites IdeaLens as its AI detector. No individual author or affiliation is named in the capture.

## Summary

Zonder Labs argues that work-context AI "slop" is costly because it is unclear, not because it carries stylistic tells. Its examples are a Slack message or a PR description that a reader must decode to move work forward. The post names three recurring faults. The first is hidden characters and actions: Williams's principle that the clearest sentence makes the story's character the grammatical subject and its action the verb, which AI writing violates without purpose through nominalizations. The second is vague wording: ambiguous references, stacked nouns, and especially odd word combinations such as "user-session entry boundary". The post calls vague wording the most common fault in Claude Code. The third is empty statements and misplaced emphasis: sentences whose words are clear but whose point is hard to find. The authors claim strong agreement among human annotators on what is clear, and use that agreement as a gold standard for annotating AI and human samples (Claude Code replies against Stack Overflow, and articles). They report much higher fault rates for AI, and say that "delve" and em dashes do not make writing sloppy, comparing their measure with an AI detector. They conjecture that writing lags coding because it is harder to reward and less economically attractive. The capture keeps only the prose and footnotes. The fault rates, the per-fault breakdown, the detector comparison and the annotated Claude Code example are absent, so every quantitative claim is asserted, not inspected.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a reader-side companion to [Why is AI-generated language so hard to understand? (ingest)](./why-is-ai-generated-language-so-hard-to-understand.ingest.md), with which it **compares-with** on the axis of how AI-prose difficulty is measured. Clark et al. count producer-side constructions (stacked noun compounds, inanimate subjects with animate verbs, rare n-grams) and borrow reader cost from psycholinguistics. Zonder names overlapping patterns as hidden characters and vague wording, and judges them by human clarity annotation. That ingest's limitations note that the paper never measures reader comprehension. Zonder claims such a measurement, but its rates are not in the capture. The two sources also offer competing causal stories that should stay separate: a length penalty in RL fine-tuning versus the absence of straightforward rewards for clarity. Both may hold.

It **compares-with** [Hacker News — I'm becoming AI-blind (ingest)](./hacker-news-im-becoming-ai-blind.ingest.md) on the axis of provenance or style signals versus reader-cost faults. The thread found that style detection and substantive review are different tasks. Zonder makes the same separation explicitly ("delve" and em dashes are not what make writing sloppy) and claims a measured comparison with an AI detector.

It **compares-with** [Reverse compression is when LLM output expands without adding information](../theory/reverse-compression-is-when-llm-output-expands-without-adding.md) on the axis of selection versus encoding. Zonder's third fault, empty statements and misplaced emphasis, is a sentence-level case of low extractable payload. Its first two faults are encoding failures in text that need not be expanded at all. The source therefore adds a second, independent example of encoding as a separate cause of reader cost.

It **is-evidence-for** [Measurable, widespread model failures are candidates for upstream fixes](../theory/measurable-widespread-model-failures-and-upstream-fixes.md), as a practitioner case that bears on the note's mechanism. The source explains why writing lags coding with two of the note's conditions: writing is harder to optimize with straightforward rewards (measurability), and it seems less economically appealing (incentive). It then publishes a clarity taxonomy with a claimed human-agreement gold standard, which is the kind of measurability the note says publication can supply. This is conjecture plus an uninspected measurement, so it does not test the note's persistence prediction.

## Extractable Value

1. **Three-fault taxonomy as a reader-side vocabulary for AI-prose clarity** -- hidden characters/actions, vague wording, and empty statements/misplaced emphasis give the KB named faults for agent-drafted prose at sentence level. Two of them align with constructions the Clark ingest measured, and the third aligns with reverse compression. The taxonomy is not new to writing pedagogy, because it repackages Williams, but it is new as a framing for AI work output in this KB. The taxonomy is context-bound to the post's examples until its annotation method is published. [quick-win]
2. **Second independent source for the selection-versus-encoding distinction** -- with the Clark ingest (producer-side construction counts) and reverse compression (selection), this source supplies a human-judged encoding leg. A theory note stating that unclear encoding is a reader cost separate from length would now rest on two kinds of evidence. Zonder's rates are claimed, not captured, so that leg is weaker than it looks. [deep-dive]
3. **Clarity-fault measurement as a case of the measurability condition** -- the post diagnoses its own failure class with the upstream-fix conditions and then publishes an evaluation scheme. That makes it a datable case for the persistence experiment proposed in the measurable-failures note: whether Claude Code's vague-wording rate falls in later releases. [experiment]
4. **Style tells and clarity faults are separate measures** -- the post adds a claimed quantitative comparison to the HN thread's qualitative finding that detecting AI provenance is not the same as finding what burdens a reader. For KB review, this supports reviewing agent prose for reader-cost faults, not for AI signatures. [just-a-reference]
5. **Williams's character/action principle has no KB theory or reference home** -- review lenses and the established-style simplification procedure depend on it, but no durable artifact outside instructions states it or its evidence. This source is a second external pointer to it, not grounding for it. [just-a-reference]

## Limitations (our opinion)

The capture boundary is the main limit. Charts, rates, the per-fault breakdown, the detector comparison and the annotated example were not captured. This ingest therefore cannot establish that AI samples show higher fault rates, that vague wording is the most frequent fault, or that clarity measures diverge from detector scores. It can establish only that the authors claim these things. The claim of "strong agreement among humans" has no statistic, annotator description or protocol in the captured prose. Agreement on a fault taxonomy written by the same group that annotated the samples is weak evidence that the taxonomy measures reader cost rather than the annotators' shared style training.

As a practitioner report, the sample is not visible: we cannot see how the Claude Code replies and Stack Overflow answers were chosen, whether genre and task were matched, or which model version produced the AI text. A Claude Code reply written mid-task to the person running it differs in audience and purpose from a Stack Overflow answer written for strangers, so a simpler account of some of the gap is a difference in register, not in model capability. The illustrative examples are partly constructed; the author says the "beverage retailer" sentence was invented on purpose. The causal story for why writing lags (hard to reward, less economically appealing) is offered without argument or evidence and competes with Clark et al.'s length-penalty account. The post does not compare its faults with readers' actual comprehension or task speed, beyond one remark that a sentence "takes more than 10 seconds to process". Clarity is therefore measured by annotator judgment, not by reader outcome.

## Recommended Next Action

Write a theory note stating that unclear encoding (hidden characters/actions, vague word combinations, stacked nouns) is a cause of AI-prose reader cost separate from length or selection. Ground it in the Clark ingest as producer-side evidence and this ingest as a claimed reader-side judgment marked "claimed, not inspected", contrast it with [reverse compression](../theory/reverse-compression-is-when-llm-output-expands-without-adding.md), and scope it as untested on KB prose.
