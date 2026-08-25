---
description: "Number-game evidence that Bayesian-like LLM hypothesis behavior is probe-dependent and fails structured domain extension"
source: https://arxiv.org/abs/2605.05851
captured: "2026-08-20"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: 7bf01e9c3ef61e38841fb0dd963526f02b6d956e7371e0b69f29bddaee7cc0f0
ingested: "2026-08-20"
type: kb/sources/types/ingest-report.md
domains: [llm-evaluation, inductive-reasoning, scientific-discovery, learning-theory]
---

# Ingest: Hypothesis generation and updating in large language models

## Classification

An arXiv v1 preprint reporting controlled number-game experiments across eight non-thinking pretrained LLMs, with matched thinking conditions for six, a configured Bayesian reference, and previously published human baselines.
Author: Huadong Xiong, School of Psychological and Brain Sciences at Georgia Tech. The paper states its models, prompts, hypothesis construction, fitting objective, and evaluation metrics in detail; it remains a sole-author preprint without independent replication in the captured record.

## Summary

Xiong studies how pretrained LLMs infer a numerical concept from up to four positive examples. The paper reads the resulting hypothesis state three ways: forced Yes/No predictions for each integer, confidence over a supplied candidate list, and free generation of ten hypotheses. Within the original `1..100` domain, a two-parameter Bayesian family often fits model behavior reasonably well: one parameter represents prior reliance and the other the strong-sampling size principle that favors smaller compatible hypotheses. That fit is not stable evidence of one posterior. Sampling-story prompts and thinking mode shift it; candidate evaluation selects hypotheses that cover the examples more often, while free generation favors narrower rule forms; and the three probes project to different fitted posteriors. When the query domain expands to `1..200` while examples stay in `1..100`, most models also fail to extend rule-consistent mass cleanly or preserve the original in-domain shape. The paper's useful conclusion is therefore diagnostic rather than Bayesian: plausible hypothesis-shaped behavior under one elicitation surface does not establish a stable hypothesis that survives another probe or domain.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a bounded empirical anchor for [first-principles reasoning selecting explanatory-reach over adaptive fit](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md): rule-like behavior and a good in-domain fit do not by themselves show that the represented structure reaches beyond the observations that elicited it. It also supplies a technical basis for [systematic prompt variation as diagnosis](../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md), because sampling stories and thinking alter the behavioral readout without identifying an internal Bayesian algorithm. Its supplied-candidate versus free-generation comparison bears on the distinct search and evaluation functions in [proposal-selection loops](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), while interpretation of every result rests on [the fixed-decomposition boundary](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).

Among captured sources, [FALSIFYBENCH](./falsifybench-inductive-reasoning-rule-discovery-games.ingest.md) is the sharpest comparison: it lets an agent choose disconfirming probes, whereas this experiment supplies fixed positive-only prefixes and measures the hypotheses they elicit. [The weakest-hypothesis paper](./optimal-choice-of-hypothesis-is-the-weakest-not-the-shortest.ingest.md) is a useful counterpoint to treating narrowness as generally beneficial, because its preference for the broadest valid hypothesis is itself conditional on a fixed language and uniform task prior.

## Extractable Value

1. **Cross-probe coherence is a stronger test than a plausible single readout** -- prediction, supplied-candidate evaluation, free generation, and domain extension disagree after projection into one predictive space. For agent evaluation, this yields a reusable criterion: do not infer a stable latent commitment until meaningfully different readouts preserve its consequences. This criterion is not yet captured by an existing note. [deep-dive]

2. **Rule-shaped output can be adaptive fit without explanatory-reach** -- models generate rule-like hypotheses over observed examples, yet fail to distinguish rule-consistent from non-rule targets cleanly in the unseen half of the enlarged domain. This gives the KB's explanatory-reach distinction a controlled behavioral instance rather than another verbal analogy. [quick-win]

3. **Supplying candidates changes what “evaluation ability” measures** -- candidate evaluation produces top hypotheses that more often contain all observations; free generation produces narrower, more rule-like candidates. A proposal-selection architecture must therefore assess the evaluator together with the candidate representation and search path, not treat judging strength as independent of what enters consideration. [quick-win]

4. **Sampling-story prompts can separate behavioral prior and likelihood effects** -- default, strong-, weak-, and explicit-candidate prompts shift the fitted prior/size-principle balance in interpretable directions, while thinking shifts it again without uniformly improving Bayesian fit. This is a reusable diagnostic design for testing which task assumptions a prompt elicits, provided the result is not reified as the model's internal algorithm. [experiment]

5. **Domain extension complements prompt variation** -- changing from `1..100` to `1..200` asks whether an inferred rule carries consequences beyond the observed region, rather than only whether equivalent wording changes the answer. The pair of tests separates elicitation brittleness from failed extension, even though neither alone identifies the internal representation. [experiment]

## Limitations (our opinion)

This is editorial judgment. The paper tests one deliberately small, one-dimensional concept-learning family, not debugging, diagnosis, KB synthesis, or scientific theory formation. Its “optimal Bayesian” comparison is optimal only inside the configured finite rule-and-interval model, prior, and sampling assumption. A good two-parameter fit to that reference is therefore descriptive compression of behavior, not evidence that an LLM implements Bayesian inference internally.

The effective update space is narrow. Behavior can condition on up to four positive integer examples, their order, the stated sampling story, an optional candidate list, and—under thinking runs—a concept-inference state. The available responses are forced Yes/No target scores, weights over supplied candidates, or ten generated hypotheses with confidences. The analysis can express mappings through a fixed rule registry, gridded intervals, two fitted parameters, and executable projections of matched labels. Fixed outside that space are the positive-only stimulus design, absence of agent-chosen experiments or negative evidence, rule/interval representation, prior mass, candidate-list construction, projection of free text, domain boundaries, model panel, and measurement interfaces. Free generation is nominally broader than the reference family, but unmatched labels are excluded from the projected curve, so projection agreement cannot validate the reference family as a complete account of model hypotheses.

Each contrast supports only what it varies. Strong- versus weak-sampling prompts establish cue-sensitive readout differences, not that models internally adopt either sampling assumption. Thinking comparisons show a behavioral shift, not a generally better inference process. The evaluation–generation contrast jointly changes whether candidates are supplied and whether the model must search, so it does not isolate a pure ability difference. Domain expansion directly tests transport across a changed query domain, but the authors' simpler alternative remains live: a model may form a different domain-conditioned posterior rather than fail to preserve one domain-independent state.

Finally, the main analysis uses one cached run and one seed per model; reported confidence intervals summarize variation across models or matched rows rather than repeated stochastic executions. The human comparison reuses published aggregate data, hypothesis generation is concentrated on the small TENENBAUM99 set, and no adjacent inductive task tests transfer beyond number concepts. This ingest did not inspect the associated experiment repository or execute its code, so all numerical and reproducibility claims remain paper-only.

## Recommended Next Action

Write a bounded evidence note titled **“A plausible readout under one probe does not establish a stable latent hypothesis”** under `kb/notes/evidence/`, using the paper's prediction/evaluation/generation and domain-extension contrasts while linking the claim to [systematic prompt variation](../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md), [explanatory-reach over adaptive fit](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md), and [experimental-contrast limits](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md).
