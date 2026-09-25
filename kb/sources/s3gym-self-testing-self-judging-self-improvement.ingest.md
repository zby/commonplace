---
description: "S3Gym separates action self-scoring from later verified performance; history-versus-summary results expose uneven adaptation without isolating judgment or abstraction as its cause."
source: https://arxiv.org/abs/2608.31100
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: d30f83c892f364328be78e7ee2be2c593a19bdaa90edf17d1e272a5be771a9aa
ingested: "2026-09-25"
type: kb/sources/types/ingest-report.md
domains: [agent-memory, learning-theory, agent-evaluation]
learning_claims: true
---

# Ingest: S3Gym: Can LLMs Turn Self-Testing and Self-Judging into Self-Improvement?

## Classification

An empirical benchmark paper presenting seven executable text games, two context-level experience treatments, an auxiliary training experiment, and analyses of self-scoring and subsequent performance. The captured version is arXiv v1, dated August 31, 2026, with September 1 on the manuscript. Jiajun Shi and collaborators list ByteDance Seed, M-A-P, and TokenWave.AI affiliations. This is the benchmark authors' own evaluation; the capture does not establish independent replication or peer review.

## Summary

[S3Gym](https://arxiv.org/abs/2608.31100) tests whether agents improve after exploring permissive versions of seven games and then facing stricter, held-out configurations. The agent predicts an immediate reward alongside each proposed action; executable verifier rewards and final scores remain hidden during exploration, although observable state changes provide indirect feedback. The main comparison evaluates seven models using raw previous-episode history or summaries of that history, while preserving current state and raw current-episode history in both conditions. Summaries help some model–game pairs and hurt others; the treatment also adds a compression call and repeats the game prompt, so it does not isolate abstraction quality. Local self-score accuracy is nearly uncorrelated with subsequent improvement in the aggregate analysis. A separate Qwen3-8B training experiment improves some games and degrades another. The paper contributes a useful separation of judgment quality from later behavior, with evidence confined to fixed games, interfaces, feedback rules, and experience-processing procedures.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source supplies a concrete measurement example for [evaluating memory by its effects](../notes/agent-memory-requirements/evaluate-memory-by-effects.md): self-score agreement and later strict-mode performance are separate outcomes. Across the tested history and summary treatments, agreement with verifier rewards does not reliably predict the next checkpoint's gain. This supports keeping intermediate quality and downstream benefit separate, without establishing that improving the judge would have no causal effect.

The mixed summary results are a bounded comparison with [diagnostic richness](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md). Only cross-episode experience is compressed; current state and current-episode history remain available. Consequently, the authors' explanation that failed summaries lose needed state detail is a hypothesis about use of prior experience, not a demonstration that the agent lacked its present state. The additional call and duplicated game prompt also make this an example of why [an experiment identifies only its actual contrast](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): the comparison varies a memory-and-prompt treatment, not rawness, causal explanation, or judgment accuracy independently.

## Learning Claims (our opinion)

The source defines improvement through later environment scores. Its main mechanism retains self-scored exploration trajectories either directly or as natural-language strategy tips. These tips are supplied to future action calls. The auxiliary mechanism converts selected or corrected experience into supervised training examples. Self-judging here is specifically a prediction of the proposed action's immediate reward before execution, not necessarily a retrospective explanation of failure. The benchmark separately observes the true reward and uses it to assess those predictions.

Summary tips can state candidate theories of how to act: the examples include planning backward toward arithmetic cancellation and conditioning strategy on an opponent. This partly maps to a [theory builder](../notes/definitions/theory-builder.md). In the summary arm, the tips are the retained theories (condition 1), and they are carried into stricter, held-out configurations (condition 4). Selected tips and matching actions suggest use, but the outcome comparison leaves open whether their content caused the gains (condition 2, unestablished). Criticism (condition 3) is unestablished and decides the verdict: self-scoring predicts an action's immediate reward, which is not criticism of what a tip says, and the paper shows no process that tests a retained tip. The raw-history arm retains only trajectories, which are input and outcome records; alone they do not meet the retention condition, whatever a model reconstructs from them during inference. The auxiliary training does not exclude membership, but gradient updates supply no criticism. Learning is uneven across model–game pairs, and it is not attributed to criticism of the tips.

The effective update space includes action choices informed by visible transitions, carried history, generated tips, and, in the auxiliary experiment, changed weights. Game objectives, legal actions, observation formats, reward definitions, and the consolidation scaffold remain supplied. The learner does not redesign those interfaces or construct the external verifier. As [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) distinguishes, improved performance within that space does not validate the fixed choices against alternatives. S3Gym's contribution to Commonplace is therefore a way to separate internal judgment from external outcome evidence, not evidence that its three-part decomposition exhausts learning or that a summary is a sufficient retained theory.

## Extractable Value

1. **Evaluate interpretation and subsequent benefit separately.** The paper measures 116,117 transitions across 98 model–pathway–game runs. Aggregate blockwise correlations with the next strict-mode score change are −0.010 for positive-event agreement and −0.018 for negative normalized scoring error. These are descriptive associations under the fixed benchmark, useful as an example for effects-based memory evaluation; they do not test replacing the judge with a more accurate one. [quick-win]
2. **Record the actual experience interface before transferring a summary result.** Appendix A preserves raw current-episode history in both arms and compresses only previous episodes. Summary Memory also adds a call and repeats the system prompt. Its mixed outcomes support testing the complete treatment in context, while leaving alternative summaries and the causal contribution of retained detail unresolved. This bounds reuse of the source alongside the diagnostic-richness note. [quick-win]
3. **Keep degradation visible in improvement metrics.** The paper's positive area above baseline, AUC+, clips all below-baseline deviations to zero. Its normalized version additionally depends on the initial score or a first-positive fallback. Neither measures net benefit. The auxiliary training result makes the issue concrete: Plants-vs-Zombies falls from 23 initially to 6 at every updated checkpoint. A future evaluation should retain signed changes and full trajectories alongside any positive-area metric. [experiment]

## Limitations (our opinion)

The main experiment uses 30 exploration episodes, evaluation every three episodes, and three strict-mode episodes per checkpoint. Disjoint exploration and evaluation seeds, with evaluation trajectories excluded from memory, reduce direct leakage. They do not supply independent repeated-run uncertainty. Sparse rewards make occasional successes influential; selecting the maximum checkpoint and clipping negative deviations can make noisy excursions look like progress. Explicit concurrency failures are excluded, and AUC connects adjacent remaining valid checkpoints. Raw AUC values cannot be compared across games with different score scales.

The judgment analysis is observational. No verifier-score replacement or no-self-score control isolates the effect of self-judging. Positive-event agreement can also be high because many transitions have zero reward: Plants-vs-Zombies reports 0.881 agreement alongside 0.882 normalized error. Neither agreement nor the near-zero aggregate coupling identifies why an agent improves or fails.

The summary examples are illustrative selections. They do not isolate loss of information, quality of abstraction, extra inference, prompt duplication, or semantic uptake. Both arms retain current state and current-episode history, so generic advice followed by a bad move could also reflect weak execution or attention rather than unavailable state information. The paper does not compare summary policies or match total inference cost. These limits follow the [experimental-contrast boundary](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md).

The training study uses a different model and 20 checkpoints, with optimizer, filtering, and correction details insufficient to establish a matched training-versus-context comparison. The cause of its persistent regression remains unresolved. No implementation was inspected or executed for this ingest; the mechanism descriptions and results remain paper evidence. The fixed games do not establish open-ended deployment adaptation, discovery of new objectives, or construction of reliable feedback. The task called Chess predicts hidden piece-movement rules and positions; it is not ordinary chess play.

## Recommended Next Action

Update [Evaluate Memory By Effects, Not By Existence](../notes/agent-memory-requirements/evaluate-memory-by-effects.md) with S3Gym as a bounded example of measuring self-judgment accuracy separately from subsequent verified performance, retaining the qualification that their association does not test the causal benefit of improving the judge.
