---
description: "Pure-inference tabular experiments separate column readability from multi-column integration and provide a reusable benchmark-contamination probe"
source_snapshot: "why-large-language-models-fail-at-tabular-prediction.md"
ingested: "2026-08-04"
type: kb/sources/types/ingest-report.md
domains: [context-engineering, evaluation, in-context-learning, benchmark-design]
---

# Ingest: Why Large Language Models Fail at Tabular Prediction

Source: [why-large-language-models-fail-at-tabular-prediction.md](why-large-language-models-fail-at-tabular-prediction.md)
Captured: 2026-08-04
From: https://arxiv.org/abs/2608.02412

## Classification

Genre: scientific-paper -- an arXiv v1 preprint that uses controlled interventions, classical baselines, synthetic controls, and behavioral comparison to study single-pass in-context tabular classification.
Domains: context-engineering, evaluation, in-context-learning, benchmark-design
Author: Marta Garnelo of Fundamental Technologies and Wojciech M. Czarnecki of Voylab; the paper provides detailed protocols and configurations, but its main result relies on one frontier model and has not been independently reproduced in this KB.

## Summary

The paper studies Claude Opus 4.6 as a bare in-context classifier: one user message contains the full training and test tables, and one generation returns all labels, with no system prompt, tools, retrieval, multi-turn loop, or fine-tuning. Controlled experiments reject four proposed causes of failure within this regime: class overlap, inability to read linearized CSV columns, numeric precision, and the number of test labels requested per call. Accuracy instead falls as feature count rises under random projections and synthetic two-dimensional upscaling, while eight classical baselines remain flat or improve. In two dimensions, the model's predictions resemble local distance-based methods; in higher dimensions, none of 252 configured classical models reproduces them closely. A separate contamination probe finds prior recall of several standard datasets, and an explanation experiment finds that the model's stated rules often fail to match its prediction task.

## Connections Found

The paper is a new empirical anchor for [soft context degradation](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md): the model can retrieve a designated target column among 60 columns while classification degrades around much smaller feature counts, separating context readability from relational integration. Its intervention suite is also a worked case for [systematic variation as diagnosis](../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md), because each manipulation tests one proposed explanation under mostly fixed task semantics. Interpretation rests on [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): signals include the single prompt's examples and test rows, permitted output is a label vector, and the model's fixed hypothesis class supplies the mapping, while the interface, prompt, model, representation family, task selection, and evaluation protocol remain outside the effective update space.

The explanation study adds behavioral evidence for [the difference between legibility and faithfulness](../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md), but it is weaker than the causal intervention in [Turpin et al.](language-models-dont-always-say-what-they-think.ingest.md): it compares an executable stated rule with observed task behavior rather than identifying which factor caused a prediction. Relative to [Paulsen's effective-context-window study](paulsen-maximum-effective-context-window-mecw.ingest.md) and [ConvexBench](convexbench-can-llms-recognize-convex-functions.ingest.md), this source isolates a different load variable. The three sources together distinguish token volume, dependency depth, and multi-coordinate integration, without yet establishing that these are independent internal mechanisms.

## Extractable Value

1. **A contamination probe can force contextual learning and memorized recall to disagree** -- holding out every example of one class makes a learner using only the supplied training set score approximately zero against that class's original labels; above-zero recovery then signals prior dataset knowledge. This is a reusable evaluation design that is distinct from temporal splits and counterfactual task construction. [quick-win]

2. **Reading context and integrating context are different capacities** -- the target-column intervention remains near ceiling through 60 columns, yet classification falls toward majority guessing as the number of coordinates grows. This adds integration dimensionality as a candidate component of the soft context bound without pretending the paper identifies its internal mechanism. [quick-win]

3. **A falsification ladder is more informative than one aggregate benchmark score** -- the paper turns five informal explanations into predictions and targeted interventions, rejecting four rather than treating one failure score as evidence for all of them. The method transfers to agent evaluation whenever plausible failure mechanisms can be varied separately. [experiment]

4. **An information-preserving control strengthens a dimensionality claim** -- the synthetic experiment maps fixed two-dimensional data into 4, 8, 16, 32, and 64 correlated coordinates, so increased feature count does not add underlying information while LLM performance still falls. This is stronger evidence than the real-dataset projection sweep, although it remains bound to linear embeddings of toy tasks. [just-a-reference]

5. **Behavioral alignment and causal faithfulness require different assays** -- executing a model's stated rule and comparing its boundary with predictions can detect an explanation-behavior mismatch, while a causal faithfulness test must intervene on a candidate driver and check whether the explanation identifies it. Keeping these tests separate prevents “explanation quality” from collapsing distinct claims. [experiment]

6. **A failed surrogate search narrows but does not explain a mechanism** -- 252 configured classical learners reproduce the model's two-dimensional behavior much better than its higher-dimensional predictions, and tuned dimension-dependent noise adds little agreement. This rules out the tested simple surrogates; it does not reveal what computation the LLM performs. [deep-dive]

## Limitations (our opinion)

The title is broader than the evidence. The main experiments test Claude Opus 4.6 in one single-turn, default-sampling, no-tool, no-system-prompt configuration; Qwen is used only for the two-dimensional behavioral comparison. The results therefore bound bare-model in-context classification, not tool-using agents, feature-engineering harnesses, fine-tuned language models, tabular foundation models, or future LLM families.

The fixed decomposition also limits the causal reading. The model can condition only on the supplied prompt and pretrained state, can respond only through generated labels, and cannot choose a different representation, tool, memory policy, or decomposition. The interventions vary selected factors inside that setup. They do not validate the setup as the right way to use an LLM for tables. In particular, the target-column experiment shows that CSV columns remain readable; it does not compare CSV with other serializations or establish that representation is irrelevant to classification.

The main random-projection sweep changes the sampled projection as well as coordinate count, so it does not hold every usable distinction constant. The synthetic upscaling control is cleaner because all coordinates remain linear functions of a fixed two-dimensional manifold, but its regular toy tasks do not establish the same effect on heterogeneous real tables. The retained benchmark is also small: eleven toy-scale datasets after contamination and learnability filtering, with one prompt and metric family.

Finally, the paper is behavioral rather than mechanistic. Two-dimensional agreement with Gaussian processes and nearest neighbors does not show that the model implements either method, and failure to match 252 classical configurations does not identify the high-dimensional computation. The explanation comparison is qualitative and behavior-facing, not a causal test of internal reasoning. Even the cost evidence should be quoted cautiously: the limitations prose gives an aggregate that differs from Table 2's total.

## Recommended Next Action

Write a note titled **“Benchmark contamination probes should force contextual learning and memorized recall apart”** using the held-out-class intervention as the worked case, and contrast this behavioral probe with temporal provenance and counterfactual authored-world leakage controls.
