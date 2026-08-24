---
description: "Co-Harness provides a provisional three-form learning case: validated harness repair alternates with fine-tuning on trajectories produced by the repaired harness"
source: https://arxiv.org/pdf/2607.22688
captured: "2026-07-28"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: 83c4f1716060cbdb060c50f8a0223e6e8c49f1bee4d2fe7d0b5ffdbd84bb0f45
ingested: "2026-07-28"
type: kb/sources/types/ingest-report.md
domains: [representational-form, harness-learning, post-training, trace-learning]
---

# Ingest: Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents

## Classification

An arXiv v1 preprint that defines an alternating optimization procedure, reports benchmark experiments and an autonomous case study, and includes algorithm, configuration, validation, and attribution details.
Author: Zhengyu Chen, Teng Xiao, Huaisheng Zhu, Yige Yuan, Luan Zhang, and Jingang Wang, affiliated with Meituan, the Allen Institute for AI, and independently; the paper is recent and its results have not been independently reproduced in this KB.

## Summary

Co-Harness treats an agent's model weights and runtime harness as coupled learning targets. In each round, an LLM critic classifies failed trajectories into prompt, tool, skill, middleware, memory, or model-side causes; proposes local harness diffs; and accepts only patches that improve the targeted failure set without regressing held-out behavior. The repaired harness then generates verified trajectories for supervised fine-tuning, and the updated model enters the next harness-repair round. Across Qwen3-8B and Qwen3-32B on three tool-integrated math benchmarks, the authors report an average rise from 58.5% after initial harness evolution to 78.9% after two full rounds, plus a 200-hour harness-only case study that recovered from crashes, reduced inference time, and selected an ensemble strategy.

## Claims

No claims have been grounded yet.

## Connections Found

This paper is the clearest current empirical anchor for [representational-form coevolution](../notes/treat-continual-learning-as-representational-form-coevolution.md): distributed-parametric weights and a harness containing natural-language prompts/skills plus symbolic tools, middleware, schemas, and registry diffs remain separately retained learning targets. It qualifies [the readable-artifact loop](../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), whose point-in-time inventory says distributed-parametric plus symbolic learning has no clean instantiation, and it exemplifies [diagnostic richness](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) through structured trace-grounded attribution before local repair. Relative to [SkillRL](skillrl-evolving-agents-recursive-skill-augmented-rl.ingest.md), Co-Harness broadens the localized target from natural-language skills to the whole mixed-form harness; relative to [Meta-Harness](meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md), it adds a weight-update loop instead of freezing the model.

## Extractable Value

1. **A three-form learning loop now has a concrete implementation** -- prompts and skills supply natural-language operative parts, tools and middleware supply symbolic ones, and SFT updates distributed-parametric weights; all remain live across rounds rather than treating one form only as a fixed reward channel. This directly updates the KB's point-in-time map of pairwise and three-way automation. [quick-win]
2. **The coupling is directional but recurrent** -- localized harness repair first changes the trajectory-generating environment, then SFT internalizes behavior from those trajectories, and the updated model exposes the next harness bottlenecks. This is stronger than one-way distillation because the external artifacts remain independently writable after behavior moves into weights. [deep-dive]
3. **Different forms retain different validation radii inside one loop** -- a harness diff has an explicit patch locus, held-in target, held-out regression set, versioned registry, and rollback path, while the weight update still requires broad behavioral probing. That is a worked case for the validation-radius distinction in the readable-artifact argument. [experiment]
4. **Cross-form credit assignment becomes an explicit abstaining classifier** -- HarnessCritic maps failures to five harness dimensions and reserves `agent error` for model-side failures excluded from patch generation. The taxonomy is a practical operator for deciding which representational form to update, although the paper's own limitations say counterfactual control-flow failures remain hard to attribute. [experiment]
5. **Compounding has stated failure conditions, not only a positive-loop slogan** -- the paper requires harness edits to improve trajectory quality, model updates to internalize the gain, and stronger models to unlock new useful harness changes; it also reports SFT plateau, harness over-patching, and attribution cascades as collapse modes. These conditions make the coevolution claim more falsifiable and transferable than the benchmark headline alone. [quick-win]
6. **The reported gains are a useful but narrow data point** -- two rounds average +20.4 percentage points over the harness-evolved/no-SFT baseline, with larger gains on the hardest benchmark-model combinations. This supports investigating mixed-form optimization, but not yet a general claim about long-lived heterogeneous agent systems. [just-a-reference]

## Limitations (our opinion)

The central causal claim is under-isolated. The reported comparison does not include a matched fixed-harness SFT arm, a harness-only arm carried through the same rounds, or an equal-compute control, so the gains cannot be assigned specifically to coevolution rather than additional fine-tuning, improved data, or harness search. The three benchmarks are 30-problem competition-math sets under one Python-interpreter harness and two Qwen3 scales; this is far narrower than the long-lived, heterogeneous systems in the KB's mixed-form conjecture. The paper also calls the SFT result reduced “Harness Debt,” but does not report a decisive harness-removal or harness-swap ablation, even though practitioner evidence warns that post-training can overfit models to harness interfaces. Finally, HarnessCritic's root-cause records and accepted diffs are generated by an LLM; human agreement is reported for the taxonomy, but the paper does not establish that the critic's causal explanations are faithful rather than merely useful proposal heuristics. The results should therefore motivate a controlled comparison, not be treated as confirmation that three-form coevolution compounds generally.

## Recommended Next Action

Revise [Treat continual learning as representational-form coevolution](../notes/treat-continual-learning-as-representational-form-coevolution.md) to add Co-Harness as the first concrete automated all-three-form case, replacing the now-stale pairwise inventory with a distinction between fixed-form training, one-way distillation, and recurrent coevolution while preserving the paper's missing-ablation caveat.
