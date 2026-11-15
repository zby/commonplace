---
description: Reference-answer adversarial post-training learns useful rewards on exact tasks, but abstract fooling rates do not establish scientific truth or KB review quality.
source: https://arxiv.org/abs/2610.38851
captured: "2026-11-15"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 4e361683a492928d6302b079304f06e59656e0ae6a07cfa2148572ae41c58cb1
ingested: "2026-11-15"
type: types/ingest-report.md
domains: [adversarial-post-training, reference-answer-supervision, learned-rewards]
learning_claims: true
---

# Ingest: Learning to Reason from Reference Samples Alone

## Classification

An empirical scientific paper proposing Reinforced Adversarial Learning (RAL), with five task settings, reward baselines, judge-size comparisons, and training configurations. Albert Bou and colleagues are affiliated with Edison Scientific Inc.; the authors report their own experiments and announce a code release. This ingest assesses the paper, not an independent replication or implementation audit.

## Summary

RAL co-trains a generator and a separately scalable LLM judge using reference final answers rather than reference reasoning traces. The judge learns reference-versus-generated classification from the task input and final answer; its reference-class probability rewards generator reinforcement learning, with malformed outputs receiving zero. Within this fixed answer-only judge interface, sufficiently large judges and extended training match or exceed direct verifiable-reward training on multiplication, Countdown-Code, and SMILES-to-formula, although supervised fine-tuning remains strongest on the chemistry task. An unconstrained abstract experiment recovers the reference corpus's biomedical domain without the topic collapse observed under a frozen Haiku judge, but that comparison also changes model, comparison format, and reward granularity. Title-conditioned NIH abstract generation raises mean held-out LLM fooling rate to about 35% and human fooling rate to 55%; those results establish resemblance to reference abstracts under the evaluation protocol, not factual validity or research utility. The proposed progression from superficial cues to deeper structure is consistent with the results, rather than directly isolated by them.

## Contribution assessment (our opinion)

Learning useful rewards where reference answers exist but reliable scoring rules do not is an important post-training problem. The strongest contribution appears to be the verifier-withheld experiments: independent exact evaluation tests whether a learned reference-membership signal improves correctness rather than merely its own score. Separate judge scaling and longer co-training make the recipe more informative than a single successful run. The paper positions its answer-only, independently scaled discriminator against earlier adversarial methods, but this ingest does not establish literature priority. Scientific-writing results broaden the demonstrated distribution-matching application; they do not yet establish scientific reasoning quality. Unequal training horizons and large judge requirements narrow claims of comparative efficiency without erasing the evidence that this supervision can work.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is a training-specific comparison for [models specialized for bounded judgments](../theory/language-models-for-bounded-judgments-form-an-emerging-category.md): its separately trained one-token classifier supplies an optimization reward, not a reusable calibrated decision service. Judge-size comparisons show capacity matters within the fixed input-plus-final-answer interface; they do not compare that interface with process-aware judging or establish calibrated probabilities for KB routing.

It also sharpens the checking distinction in [the verifiability gradient](../theory/verifiability-gradient.md). Exact checks withheld from training provide an independent test of correctness on the first three tasks. Abstract fooling rates check resemblance under discrimination, a different requirement from truth or usefulness. This makes RAL a useful boundary case for KB evaluation design, not direct evidence that adapting a KB reviewer improves its judgments.

## Learning Claims (our opinion)

The source's adaptation is parametric: the judge updates from reference-membership labels and current generated answers; the generator updates through group-relative policy optimization using judge probabilities. Both retain changes in weights. The NIH experiment additionally replays earlier generations and smooths the reward judge through weight averaging. Reasoning traces influence the generator's final answer and receive policy updates, but the judge never sees them. Better exact held-out performance supports improved capacity for future action on these task distributions, independently of whether the arrangement meets Commonplace's theory-builder conditions.

Against the [theory-builder definition](../theory/definitions/theory-builder.md), the training loop has only a partial mapping. **Localized content:** answers and traces are explicit texts, but the retained adapting policies and reward function are weights, not stated theories. **Consumption:** the judge consumes answer content, and its score changes generator updates; that does not demonstrate consumption of retained stated theories. **Criticism:** reference-membership classification supplies error feedback, but not stated criticisms of identified claims that the loop can dispute or revise. **Iteration:** scores affect later generations through weight updates, so adaptive feedback clearly persists across rounds of a run; iteration of stated criticism is not established. The loop therefore demonstrates learning without establishing a theory builder. The scientists' qualitative observations about hypotheses and experiments in generated text do not establish a separate content-directed criticism loop inside training.

The paper is consistent with [learning within a fixed decomposition](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): increasing judge capacity improves the effective learned mapping behind an unchanged interface. The reference corpus, membership objective, answer parser, and exclusion of reasoning from judge inputs remain externally chosen. The experiments do not establish that these choices are preferable to alternatives. Learned weights can be retained for later inference, and replay preserves earlier generator strategies within the NIH run; cross-problem transfer or continued adaptation across deployments is not tested. The conjectured adversarial curriculum is plausible, but judge-score/error correlations and repeated classification recoveries do not alone identify which semantic distinctions were learned.

## Extractable Value

1. **Separate learned feedback from the property independently checked.** Verifier-withheld training followed by exact evaluation is a useful design pattern for testing whether an adaptive judge tracks a task objective. The abstract results illustrate why reference resemblance cannot substitute for a truth check. This supplies a concrete comparison for the verifiability-gradient note. [quick-win]
2. **Treat judge capacity as a variable, not a consequence of answer length.** A one-token judge may need substantially more capacity than its generator. Within the fixed answer-only interface, larger judges support stronger correctness gains; this is not evidence for a universal judge size or for that interface over other decompositions. [just-a-reference]
3. **Retain the frozen-judge collapse as a bounded failure example.** In the reported Haiku run, 125 of 128 final outputs converge on an out-of-domain oyster ecotoxicology theme despite increasing reward. This motivates checking domain coverage and semantic diversity separately from reward, but the confounded comparison cannot isolate co-training as the sole remedy. [just-a-reference]

## Limitations (our opinion)

The comparisons establish feasibility more clearly than efficiency or superiority over all simpler methods. RAL receives longer training to learn its reward, larger judges increase training cost, and reported best held-out checkpoints are not an untouched final test. Confidence intervals on evaluation examples do not establish robustness across independent training seeds. The chemistry table reports 81.6% for RAL with a 32B judge versus 67.9% for direct verifiable rewards, but 94.5% for SFT; matching RLVR is not the same as beating the strongest demonstrated baseline.

The frozen-Haiku comparison changes co-training, model identity, pointwise versus pairwise inputs, and continuous versus binary rewards together. It shows failure of that frozen configuration, not that frozen judges generally collapse. Replay and reward smoothing are added in the NIH experiment without isolated ablations, so their separate causal contributions remain open.

Reference answers are the sole task supervision for the RAL loop, not the absence of task engineering: format gates and task-specific prompts remain, and Countdown references were programmatically filtered for correctness during dataset construction. The Countdown judge receives a compact expression plus a test-modification flag rather than the full submitted files; conclusions about reward hacking inherit that representation and the reported absence of cheating-oriented pretraining.

NIH evaluation uses 128 held-out titles and discrimination by models and biomedical experts. The generator receives titles, not verified preliminary findings. It can therefore invent scientifically plausible evidence; fooling evaluators does not establish true premises, executable experiments, novelty, or benefit to scientists. Qualitative improvements in argument structure cover selected generations and do not independently measure those properties. No KB maintenance task is tested, and no code or training was executed for this ingest.

## Recommended Next Action

Review `kb/theory/verifiability-gradient.md` for a bounded RAL example contrasting verifier-withheld training with exact correctness evaluation and abstract resemblance evaluation.
