---
description: "WikiSkill improves skill evolution with a persistent diagnostic wiki; its ablations distinguish proposer memory from solver access while leaving wiki claims outside validation gating."
source: https://arxiv.org/abs/2608.27454
captured: "2026-09-17"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0
ingested: "2026-09-17"
type: kb/sources/types/ingest-report.md
domains: [agent-memory, learning-theory, skill-evolution]
learning_claims: true
---

# Ingest: WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution

## Classification

An experimental arXiv paper introducing a skill-evolution method, comparing benchmark performance, ablating wiki access, and testing cross-model skill transfer. Liyan Tang and colleagues list Google Research and Virginia Tech affiliations. The retained observation is the full paper, including algorithm, evaluation details, and agent prompts; this ingest does not independently reproduce its results.

## Summary

WikiSkill separates immutable execution traces, a persistent wiki of patterns and intervention history, and active procedural skills. A maintainer consolidates successful and failed traces; a proposer reads the wiki and selected traces to create or patch one skill; strict validation improvement determines whether that skill change survives. Wiki changes survive rejection. With full skill text injected into solver prompts and the broader harness fixed, the paper reports the highest five-benchmark average for each of five models against Trace2Skill, EvoSkill, and SkillOpt. In its Gemini ablation, adding both the wiki maintainer and proposer wiki access raises the four-benchmark average from 48.7% to 63.7%; this tests their combined contribution, not persistent storage alone. Cross-model experiments show that discovering useful skills and executing them are distinct capabilities, with both substantial gains and harmful transfer. The source is useful for designing diagnostic memory for an improvement loop, with weaker evidence for long-term knowledge quality or unrestricted deployment adaptation.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper supplies bounded evidence for [diagnostic richness constraining outer-loop learning](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md). Its proposer can combine pattern pages, recorded proposal diffs and outcomes, and raw-trace inspection. The 48.7% to 63.7% ablation result applies to the wiki-plus-maintainer treatment inside the fixed skill-update pipeline; it does not identify which retained information or maintenance operation caused the gain.

It also provides a concrete comparison for [trace-extracted memory earning authority per operation](../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md). Skill acceptance tests downstream performance, while wiki diagnoses and generalizations remain retained irrespective of that outcome. A useful skill does not thereby establish the truth of every pattern that motivated it. This separation matters directly to Commonplace: retention, use in a proposal, and justified confidence in a claim require different evidence.

## Learning Claims (our opinion)

Learning occurs through persistent natural-language artifacts, without updating model weights. The maintainer sees the existing wiki and up to eight sampled traces, including failures and successes. The proposer receives an index, intervention history, and task-outcome summaries, then can inspect pattern pages and raw traces. It creates or patches one skill at a time. The validation score selects active skills; the wiki retains both accepted and rejected interventions for later proposals.

This partially instantiates [theory refinement](../notes/definitions/theory-refinement.md): pattern pages expose editable diagnoses and proposed remedies, and procedural rules are revised against subsequent cases. The ALFWorld case study traces rejection of abstract guidance, acceptance of a concrete anti-loop rule, and a later edit for another loop variant. It illustrates empirical revision of explicit guidance. However, applying a diagnosis to propose a skill is not itself revision of that diagnosis. The paper does not demonstrate that wiki explanations systematically acquire and survive their own discriminating tests. The aggregate wiki ablation supports the usefulness of the diagnostic process, without establishing the causal accuracy of each retained explanation.

The effective update space includes broad procedural changes expressible in skill text and executable through each solver's existing tools. The layer boundaries, maintainer and proposer roles, tool interfaces, and strict acceptance rule remain outside that search. As in [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), improvements within this space do not establish that its partition is preferable to alternative partitions. The access ablation does vary one boundary: allowing the solver to read the wiki during training reduces the default four-benchmark average from 63.7% to 60.9%. The authors' explanation—that direct wiki use makes traces less informative for skill development—is a hypothesis, not an isolated causal finding.

The cross-model tests strengthen a different distinction: skill quality is relative to its consumer. Qwen-3.5-4B's OfficeQA skills reduce its own score from 30.2% to 28.5% but raise Qwen-3.6-27B from 42.1% to 52.9%. Conversely, its spreadsheet skills reduce Gemini from 50.5% to 18.1%. These full-injection experiments test execution after delivery, leaving skill discovery and loading in a deployed library untested.

## Extractable Value

1. **Evidence for retaining structured diagnostics alongside raw traces.** The wiki-plus-maintainer ablation supports a diagnostic bundle for skill proposers within a fixed harness. It adds a concrete comparison to the diagnostic-richness note, without establishing that a wiki is the uniquely effective representation. [quick-win]
2. **Keep intervention outcomes distinct from the authority of explanations.** Recording rejected diffs preserves useful search history even when procedural changes roll back. WikiSkill makes that separation concrete, but also exposes the need to avoid treating retained diagnoses as validated knowledge. [quick-win]
3. **Test the consumer separately from the skill author.** Cross-model results under direct skill injection reveal both useful procedures that their author executes poorly and harmful model-specific workarounds. A skill-evaluation experiment should vary the consuming model rather than infer portability from the author's score. [experiment]
4. **Treat solver access to improvement memory as a design variable.** The training-access ablation motivates testing whether access changes the traces available for later improvement. Its modest aggregate reduction does not justify a universal ban on solver access to a KB. [experiment]

## Limitations (our opinion)

The central ablation removes the maintainer together with proposer wiki access. Extra analysis and organized history are therefore alternative contributors to the gain; the experiment does not separate persistence, summarization, rejected-proposal memory, and additional reasoning. Main-method comparisons also differ in optimizer operation and batching. Appendix D counts optimizer calls, not matched end-to-end token cost or elapsed time.

Full skill injection removes retrieval and triggering failures by construction. The findings therefore concern procedural content after delivery, not navigation through a large skill collection. OfficeQA additionally supplies oracle reference pages in the initial prompt, limiting transfer to unaided document retrieval. The broader harness remains fixed, and the study does not test online adaptation within very long executions.

Validation splits contain only 10–40 cases and are repeatedly reused for selection. Three independent evolution runs and test-set bootstrap comparisons provide outcome evidence, but do not eliminate noisy acceptance or validation overfitting. Strict improvement rejects neutral changes that could enable later gains. Gemini's perfect initial ALFWorld validation score terminates evolution despite an 85.9% test baseline, illustrating the gate's limited view of remaining errors.

The wiki has no automated pruning and the reported iteration analysis ends at iteration 7. Continued accepted edits and one simplified case study do not establish increasing improvement productivity or reliable correction of stale diagnoses over long periods. No implementation was inspected or executed for this ingest; mechanism and performance claims remain paper-reported.

## Recommended Next Action

Update [Diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) with WikiSkill's 48.7% to 63.7% proposer-memory comparison, explicitly bounding it to the combined wiki-maintainer treatment within the fixed skill-evolution pipeline.
