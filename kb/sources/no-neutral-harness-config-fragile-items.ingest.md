---
description: "A multiple-choice harness grid traces ranking changes to unstable items, supporting diagnostic prompt variation while limiting scoring attribution and robust-only comparisons."
type: types/ingest-report.md
source: https://arxiv.org/abs/2608.21382
captured: "2026-09-24"
ingested: "2026-09-25"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: ee87a7a5c8d0e09bf4c46eaf16d74ff1501c8c14fb311cc8d2dd7ddd808d13be
domains: [llm-evaluation, prompt-sensitivity, benchmark-design]
---

# Ingest: There Is No Neutral Harness

## Classification

Scientific paper reporting a matched evaluation and an item-level analysis of configuration sensitivity. V. S. Raghu Parupudi lists a University of California, San Diego affiliation. The [arXiv paper](https://arxiv.org/abs/2608.21382) supplies methods, tables, limitations, and a reproducibility appendix; the retained source does not establish peer-review status. Its empirical claims are author-reported here, without independent execution of the released code or records.

## Summary

The paper evaluates twelve instruction-tuned open-weight models on the same 3,679 four-option questions from ARC, HellaSwag, MMLU, and TruthfulQA. Its grid crosses four generation templates with six option orders and adds two likelihood cloze configurations, holding weights, items, and zero-shot greedy generation fixed. It records correctness for each model, item, and configuration, then identifies items whose correctness changes. These items account for 95.7% of the mean nonzero adjacent-model gap under the reference configuration. Four models attain first place somewhere in the grid, although two win only by one or three items. Item discrimination under the reference configuration correlates with configuration fragility at 0.28. The useful contribution is tracing aggregate ranking sensitivity to individual items. The grid is not a complete factorial experiment: the generation-versus-likelihood comparison jointly changes presentation, the answer interface, and scoring. Results therefore establish sensitivity to these harness configurations, without isolating a scoring algorithm's effect or establishing that the small, outcome-selected stable subsets measure capability better.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper supplies empirical evidence for the diagnostic use of [systematic prompt variation](../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md). Its ordering and format variants expose brittle responses and show which items support a ranking; they do not aggregate independent evidence or vary an explanation's premises. The item-level decomposition makes that existing distinction more operational.

It also provides a comparison case for [the limits of an experimental contrast](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md). Exact item-level measurement cannot isolate the components changed together by switching from generated labels to likelihood-scored continuations. Even the letter-versus-digit templates vary answer instructions as well as labels. The reported dominance of the scoring axis is consequently a result for the implemented bundle of differences.

The [pairwise-comparison test plan](../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md) offers a narrower transfer destination: evaluate winner stability across interface variants alongside discrimination and agreement with adjudicated quality. This is a design analogy. The paper evaluates multiple-choice answering, not pairwise judging or Commonplace's review process.

## Extractable Value

1. **Resolve sensitivity to the items supporting a decision.** [quick-win] The correctness grid separates consistently correct, consistently wrong, and configuration-sensitive items, then decomposes each reference ranking gap. That is a concrete diagnostic extension to the systematic-variation note. Its 95.7% result averages ten nonzero adjacent-pair gaps equally; pooling their contributions gives 99.7%. These describe the observed reference gaps, not the proportion of capability caused by the harness.
2. **Report attainable score ranges and winner margins separately from item-wise envelopes.** [quick-win] For the model named gemma4-31b, single-configuration accuracy ranges from 0.306 to 0.886. The wider robust-to-optimistic envelope counts items correct under every configuration versus at least one; its endpoints need not be achievable by any single configuration. Similarly, the four-member champion set needs margins: two models divide all 24 generation configurations, while the two likelihood winners lead by just one and three items. These distinctions prevent a sensitivity diagnostic from overstating uncertainty or decisiveness.
3. **Test compression against both configuration changes and size-matched random subsets.** [experiment] On this twelve-model pool, point-biserial item discrimination correlates with fragility at 0.2767, with a reported bootstrap interval of 0.25–0.30. The top 100 items have mean fragility 0.96 versus 0.85 overall. Across seeded tie-breaks, they yield 5.67 distinct champions on average, compared with 5.08 for random 100-item subsets and four for the full set. Most of the increase comes from reducing the sample; the additional association with discrimination is smaller. This supports checking a cheap evaluation subset across interfaces before treating its ranking fidelity under one configuration as sufficient.

## Limitations (our opinion)

The tested task remains four-option answering with known gold labels, greedy generation capped at eight tokens, regex extraction, and mean continuation log-probability for likelihood scoring. Unparseable generations count as wrong. The study does not separate answer knowledge from output compliance or extraction effects, compare stochastic decoding, or evaluate agentic tasks. Its axis-robust accuracies of 0.598 for ordering, 0.396 for format, and 0.314 for scoring are absolute accuracies under the selected contrasts, not fractions of already credited answers. As the experimental-contrast note explains, these bundle comparisons cannot establish that scoring alone causes the difference or that an alternative extraction interface would retain it.

The strongest ranking claim needs a selection qualification. Jointly robust sets contain only 72–336 items and are selected using the models' observed responses across the grid. Five adjacent pairs have identical correctness on those sets, four differ on one item, and two have opposing differences that cancel. For nine pairs, bootstrap inclusion of zero is partly structural because disagreements are absent in at least one direction. This supports near-agreement on the selected items; it does not establish equivalent capability, nor validate the proposed rule of comparing models only on robust items. A simpler account remains that the selection removes many items on which models differ usefully, together with items sensitive to presentation.

The finite grid and benchmark construction constrain reuse. TruthfulQA's constructed items put the gold answer first in the reference order. Removing that benchmark preserves the main sensitivity findings but changes the champion count from four to three and the minimum rank correlation from −0.09 to +0.03. The appendix also says all five non-identity permutations move that answer, while its displayed permutation table includes rows that retain original option zero in the first slot. This inconsistency remains unresolved in the paper-only analysis. The choice to include likelihood scoring as an equally appropriate interface for instruction models is itself a methodological judgment.

The compression result evaluates one discrimination statistic estimated from twelve models, not every benchmark-compression method. At the top-100 cutoff, only 36 items are uniquely selected; 64 slots are filled from 102 tied items. Seeded tie-breaks expose that uncertainty, but do not establish downstream selection quality or a universal defect in compressed benchmarks. The evidence supports a stability check, not rejection of compression as a class.

## Recommended Next Action

Update [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) with this paper as a bounded example of item-level diagnostic variation, preserving the distinction between observed ranking sensitivity and the unvalidated prescription to compare models only on stable items.
