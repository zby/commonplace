---
description: "SkillGLoW consolidates execution-derived skills by shared procedure; its selected training gains and narrower held-out tests inform abstraction scope, not universal library superiority."
source: https://arxiv.org/abs/2609.02217
captured: "2026-09-24"
ingested: "2026-09-25"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: e4676895076968cb80c94a64c5849a43ba0f5cf29d5a244a7ab0203473d0e2f9
type: ingest-report
domains: [procedural-memory, skill-consolidation, deploy-time-learning, transfer]
learning_claims: true
---

# Ingest: SkillGLoW: Procedural-Family Skill Consolidation

## Classification

Scientific preprint by Ao Yan, Zhang Xin, Jiawei Du, and Joey Tianyi Zhou, affiliated with the National University of Singapore and the Institute of Advanced Intelligence and Computing. The captured v1 paper reports a method, benchmark comparisons, deployment records, held-out evaluations, and pipeline prompts. These are author-reported experiments; this ingest does not independently reproduce them.

## Summary

SkillGLoW groups task-local skills by their proposed solving procedure, compresses each group into a reusable textual prior, and regenerates instance-specific guidance from the current task's own execution feedback. A frozen model performs solving and consolidation. Retrieval supplies a base prior plus at most one family prior, and a gate selects whole-library revisions using execution scores on the training stream. Across four benchmarks and three models, peak admitted libraries improve hard success by an average 17.2 percentage points over no skill; adding local regeneration gives 18.0 points. These are selected training-stream results for the combined clustering, compression, retrieval, and admission scheme. Separate tests with unchanged libraries raise mean success from 73.9% to 83.9% on 60 unseen ALFWorld tasks and from 40.0% to 45.6% on 30 unseen SWE instances for one model. The paper contributes a concrete way to separate reusable procedure from instance bindings, with narrower evidence for within-benchmark transfer than for its claim that procedural families are the right unit of skill storage.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a methodological comparison for [transfer over a shared mechanism](../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md). Its terminal-task analysis distinguishes similar subject matter from similar operations: within one binary-related family, the prior helped two byte-processing tasks while three other tasks remained unsolved. This is a useful local illustration, not a controlled isolation of mechanism identity. The held-out gains retain benchmark structure, and ALFWorld retains task categories; they do not establish transfer across arbitrary domain changes.

It also sharpens the distinction needed by [abstraction boundaries](../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md). Compression retains applicability conditions, procedure, and failure modes while removing instance bindings. The paper's household example replaces a remembered furniture-location ranking with instructions to read the current observation. A generated condition proposes where a lesson applies; neither stating it nor obtaining a high clustering purity establishes that scope. Outcome testing supplies additional, distribution-bound evidence.

Compared with [SkillOpt](skillopt-executive-strategy-self-evolving-agent-skills.ingest.md), SkillGLoW maintains a recalled family library instead of one optimized document. Its adapted SkillOpt comparator uses a neutral starting skill, the same solver and optimizer model, and common task adapters. The reported ranking concerns that configuration and selected training peaks, not SkillOpt's original evaluation or a comparison isolating granularity alone.

## Learning Claims (our opinion)

The retained object is procedural text that changes a frozen agent's context. The learner receives task instructions, trajectories, verifier scores, and differences between repeated executions. It can regenerate local guidance, regroup skill cards, compress families, append guards derived from failures, or carry forward earlier priors. Local guidance becomes evidence for later consolidation rather than entering the long-term library verbatim. The held-out results provide evidence of improved future-task capacity within the evaluated benchmarks; the training peaks alone would establish only improvement on revisited tasks.

Against the [theory-builder definition](../notes/definitions/theory-builder.md), conditions 1 and 2 are met: skill cards are stated procedures, and retrieved priors change what the frozen agent does. Condition 3 is met through the failure-attribution route: the prompt asks which skill slot supplied missing or wrong guidance and requests a correction grounded in the attempted code, so criticism aims at what a procedure says. The whole-library score gate alone ranks variants and would be trial and error. Condition 4 (iteration) is met: corrections from failure attribution are kept in the library and shape the next round's guidance and consolidation. The evaluated arrangement is therefore inside the term. Each run builds one library for one benchmark's training stream, so the persistence grade reached is across rounds of one run. The held-out tests use the unchanged library, which is reuse of a frozen product and ends the builder; the paper does not show the library or its failure records taken up in later work on other problems. A deployment that kept revising the library across new task streams would reach a higher grade, but it is not tested. As a separate learning claim, the held-out results support improved capacity within two benchmarks. The paper does not isolate the repair route's contribution, and Appendix O reports repair differences of mixed sign across models. Separate applicability, procedure, and failure-mode content offers finer [addressability](../notes/definitions/theory-builder.md#addressability), but the benefit of that structure is likewise not independently tested.

The family partition is regenerated, so task membership is inside the update space. The architecture outside it fixes textual skills, supplied card views and fusion rules, family compression, top-one thresholded recall, and whole-library admission. As in [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), gains within this scheme do not vindicate all of those choices. The ablations vary some components, but none establishes the superiority of this entire decomposition over other ways to retain and route experience. The source adds a concrete candidate mechanism to Commonplace's account without requiring a change to the theory-builder definition.

## Extractable Value

- **Replace instance bindings with observations while preserving executable steps.** [quick-win] The household example shows what useful abstraction can retain: commands and turn-saving constraints survive while a memorized location ranking becomes a current-state lookup. This gives the abstraction-boundary note a concrete distinction between proposing a scoped rule and verifying its reuse.
- **Treat procedural families as a testable storage choice.** [experiment] The combined family-library system improves selected training scores and transfers within two benchmarks. Appendix O's closer flat-library comparison holds model, retriever, and injection channel fixed on a 15-task LMB validation set: a 22-entry family library matches the best 54-entry flat library at 46.7%. That single-trial result motivates testing compactness at comparable utility, not assuming a universal performance advantage.
- **Distinguish admission evidence from independent transfer evidence.** [quick-win] The gate evaluates deployment on the same stream used for learning, admits ties and soft-score declines within 0.02, and preserves better earlier libraries. This is a useful retention rule with a specific evidence boundary; it does not turn training success into a held-out guarantee.

## Limitations (our opinion)

The main table reports peak admitted libraries across rounds on training streams of 20–53 tasks, with one trial per task. The twelve positive differences and their paired significance describe those selected results. Repeated no-skill runs estimate baseline sampling variation, not uncertainty in the full process of learning, selection, and transfer. Held-out evidence consists of 60 ALFWorld tasks at one trial per model and 30 SWE instances averaged over three trials for MiniMax-M3. Cross-domain and cross-model transfer remain untested.

The organizational comparisons leave consequential differences entangled. Base-only receives one compression pass; SkillOpt iteratively optimizes one document. Local-only regenerates guidance for the current task and is not a retrieved historical pool. The AWM port pools retrieval results into one document injected identically into all tasks, whereas SkillGLoW retrieves per task. The small matched-retriever control is more focused but insufficient to settle family-library superiority. The reported 3.6× compression is a word-count ratio; last-round entry compression is about 3.23×. Neither establishes bounded growth under an indefinitely expanding set of procedures.

The gate comparison uses each round's already evaluated candidate against the retained incumbent, not an independently evolving ungated learner. Accepting a different candidate could change the next round's evidence and descendants. Two admitted candidates also fall below their anchors within the tolerance. Consequently the gate data show avoided immediate score losses, not guaranteed non-degradation or the long-run causal effect of gating.

Generated family names and applicability conditions are not independent evidence of shared procedure. Only ALFWorld provides external task-type labels, and even there those labels do not define every useful procedural partition. The source's task-level examples support inspection of scope, but do not identify whether clustering, text quality, routing, or extra optimization caused the gains. No implementation was inspected or executed for this ingest.

## Recommended Next Action

Review [Abstract an experience into a lesson only when you can state where the lesson stops](../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) against this source, focusing on whether the note sufficiently distinguishes a generated applicability condition from evidence that the condition bounds reliable reuse.
