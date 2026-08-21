---
description: "SPADE is a code-grounded case of adaptive executable-environment generation inside a fixed training decomposition, with released mechanisms but unreleased outcome artifacts at the pinned commit."
source_snapshot: "spade-self-play-in-adaptive-synthetic-executable-environments.md"
ingested: "2026-08-21"
type: kb/sources/types/ingest-report.md
domains: [self-improving-systems, learning-theory, evaluation, agent-memory]
code_revisions:
  - https://github.com/spade-rl/spade/commit/65421ccb15a6d501ad6217bd969816146da15e11
---

# Ingest: SPADE: Self-Play in Adaptive Synthetic Executable Environments

Source: [spade-self-play-in-adaptive-synthetic-executable-environments.md](spade-self-play-in-adaptive-synthetic-executable-environments.md)
Captured: 2026-08-21
From: https://arxiv.org/abs/2608.19197v1

## Classification

Genre: scientific-paper -- an arXiv v1 preprint that defines a self-play RL method, reports two training settings and held-out evaluations, and includes algorithms, ablations, qualitative environment analyses, and an official implementation.
Domains: self-improving-systems, learning-theory, evaluation, agent-memory
Author: Bo Liu, Simon Yu, Yiding Jiang, Ao Qu, Andrew Zhao, Zichen Liu, Junsu Kim, Zijian Zhou, Seungone Kim, Tongzheng Ren, Mickel Liu, Hanfei Yu, Zhaorun Chen, Weiyan Shi, Paul Pu Liang, Luke Zettlemoyer, Yejin Choi, and Natasha Jaques, spanning nine universities. The multi-institution team and official executable release are strong authorship signals, but the paper was submitted two days before ingestion as a v1 preprint and its outcomes have not been independently reproduced in this KB.

## Summary

SPADE trains one language model in two roles: an Environment Designer writes complete Python environments and privileged hints, and a Reasoning Agent plays each environment with and without the hint. Both roles update the same weights. The deployed designer reward blends a difficulty target with the hint-conditioned return gap, while fresh corpus documents broaden what environments are about and a bounded memory of high-regret and too-easy or too-hard environments conditions later designs. On Qwen3 models up to 30B-A3B, the paper reports a 58.3 average on eight games-setting evaluations, 5.3 points above its strongest fixed-environment baseline, plus gains of 5.7 points on BFCL v4 multi-turn and 13.9 on ACEBench-Agent in the tool-use setting. For this KB, the main contribution is a worked separation among candidate generation, executable validity, learning value, and parametric retention—not evidence of an unconstrained or open-ended improvement loop.

## Code Grounding

The official repository was reviewed at commit [65421ccb15a6d501ad6217bd969816146da15e11](https://github.com/spade-rl/spade/commit/65421ccb15a6d501ad6217bd969816146da15e11).

**Implemented mechanisms.** The shared rollout adapter collects Environment Designer and Reasoning Agent trajectories into one training batch and delays designer credit until paired plays are available ([`spade/slime/spade_rollout.py`](https://github.com/spade-rl/spade/blob/65421ccb15a6d501ad6217bd969816146da15e11/spade/slime/spade_rollout.py)). The orchestrator generates hints with the same training model, plays hint and no-hint arms, computes their return gap, validates generated games, and carries delayed designer rewards ([`spade/core/orchestrator.py`](https://github.com/spade-rl/spade/blob/65421ccb15a6d501ad6217bd969816146da15e11/spade/core/orchestrator.py)). Corpus injection and the 200-entry example buffer are separate modules ([`spade/core/corpus_orchestrator.py`](https://github.com/spade-rl/spade/blob/65421ccb15a6d501ad6217bd969816146da15e11/spade/core/corpus_orchestrator.py), [`spade/core/env_memory.py`](https://github.com/spade-rl/spade/blob/65421ccb15a6d501ad6217bd969816146da15e11/spade/core/env_memory.py)). Structural/runtime checks and the model-based solvability screen are also present ([`spade/core/env_validator.py`](https://github.com/spade-rl/spade/blob/65421ccb15a6d501ad6217bd969816146da15e11/spade/core/env_validator.py), [`spade/core/envs/synthetic_game_env.py`](https://github.com/spade-rl/spade/blob/65421ccb15a6d501ad6217bd969816146da15e11/spade/core/envs/synthetic_game_env.py)). These files confirm the claimed mechanism, not its training outcome.

**Artifact-supported experiment setup.** The released games and tool-use launchers expose the paper-like shared-model, corpus, memory, and reward settings ([`cmd/games/train_spade_30b.sh`](https://github.com/spade-rl/spade/blob/65421ccb15a6d501ad6217bd969816146da15e11/cmd/games/train_spade_30b.sh), [`cmd/tool_use/_train_spade_blend.sh`](https://github.com/spade-rl/spade/blob/65421ccb15a6d501ad6217bd969816146da15e11/cmd/tool_use/_train_spade_blend.sh)). The ablation wrappers distinguish strong command matches from a frozen-designer/no-memory control explicitly marked “Reconstructed” ([`cmd/ablations/README.md`](https://github.com/spade-rl/spade/blob/65421ccb15a6d501ad6217bd969816146da15e11/cmd/ablations/README.md)). An offline evaluation driver and suite configurations are present, but require external datasets, benchmark repositories, model endpoints, and a model-specific BFCL handle ([`eval_offline/README.md`](https://github.com/spade-rl/spade/blob/65421ccb15a6d501ad6217bd969816146da15e11/eval_offline/README.md)).

**Paper-only outcomes and execution status.** The reported training curves, benchmark scores, diversity measurements, scaling behavior, and qualitative trajectory shift remain paper-only. Appendix C.3 says evaluation outputs and every figure script ship with the code, but no result artifact or figure/plot script was tracked at the reviewed commit. Five cheap existing test modules were executed without installing dependencies or downloading data: `50 passed in 0.32s` for environment reward assignment, learning potential, game utilities, delayed environment rewards, and optional imports. No training, model inference, benchmark evaluation, dataset or weight download, or submodule initialization was performed. Passing these unit tests is not a reproduction of any paper result.

## Connections Found

SPADE is a strong second-domain case for [choosing what to learn requires both validity and learning-value gates](../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md). Candidate environments must first survive parse, instantiate, reset, runtime-probe, and—in tool use—semantic feasibility checks. Only then do the difficulty anchor and hint-conditioned return gap supply learning value. Corpus grounding controls search breadth upstream, so generation, validity, and value remain distinguishable rather than becoming one opaque “quality” score.

Interpretation [rests on the effective update space](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). SPADE exposes environment-design mappings and shared model weights to learning, but fixes the Gym-style interface, corpus composition and sampler, six-skill partition, tool schemas, reward blend, validator, memory schema and capacity, GRPO algorithm, role prompts, evaluation suite, and checkpoint-selection procedure. Its ablations must likewise be read through [the contrast they actually run](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): removing corpus or memory tests those coordinates, while the frozen-designer controls also remove memory or swap the model and therefore do not isolate designer gradient updates.

Relative to [Co-Harness](co-harness-co-evolving-harness-and-model-weights.ingest.md), SPADE uses generated executable code to shape weight updates but does not retain a separately versioned, regression-gated harness. Relative to [Voyager](../agent-memory-systems/reviews/voyager.md), its memory has the narrower authority of conditioning curriculum design: it retains high-regret seeds and negative difficulty examples, not a reusable library of promoted action skills.

## Extractable Value

1. **Candidate breadth, validity, and learning value are separate control surfaces.** Corpus documents seed the proposal distribution; functional and semantic checks reject malformed or impossible environments; hint-regret plus the difficulty anchor ranks feasible environments by expected training value. This three-part audit generalizes beyond self-play to any loop that synthesizes its own training material. [quick-win]
2. **Learning the task generator broadens the update space without eliminating a fixed decomposition.** SPADE makes executable environment production responsive to learner performance, yet the representation, skill taxonomy, signals, optimizer, validator, memory policy, and evaluation boundary remain authored. It is a concrete case for auditing what changed rather than labeling the whole pipeline “self-improving.” [deep-dive]
3. **A current-policy counterfactual can be a sharper curriculum signal than historical progress.** The hint/no-hint return gap asks whether extra privileged information changes the present policy's result on the same environment. The paper's matched reward ablation reports 58.3 for the regret blend versus 55.9 for a slow-EMA learning-potential signal, but that outcome remains unreproduced and specific to the tested reward definitions. [experiment]
4. **Corpus and curriculum memory serve different roles.** The corpus supplies topical breadth; memory supplies difficulty-relative continuity by surfacing high-regret seeds and mastered or impossible negatives. Single-removal ablations report 53.5 without corpus and 53.2 without memory versus 58.3 for the full configuration, while the no-corpus run's diversity collapses. Those contrasts support retaining the distinction, not treating either component as a generic memory benefit. [experiment]
5. **Executable environments unify interaction and verification at a useful interface boundary.** A reset/step program can represent both reasoning games and simulated tool use, making state transitions, reward logic, and success criteria inspectable. The interface is a practical reference for generated-curriculum systems even where the paper's performance claims do not transfer. [just-a-reference]
6. **A runnable mechanism release can still leave the main empirical chain unauditable.** Training and evaluation entry points are present, but the claimed result JSONs and plotting scripts are absent at the pinned commit. Code-grounded ingestion should therefore classify outcomes separately from mechanism and configuration evidence. [quick-win]

## Limitations (our opinion)

Static inspection and 50 passing unit tests establish only narrow implementation facts. They do not verify the expensive training runs, checkpoints, benchmark scores, generated-environment distribution, or scaling result. The missing result and figure artifacts are especially consequential because the paper says they are included; without them, this ingest cannot trace reported table cells to raw outputs or reconstruct figures without rerunning the study. The two uninitialized submodules and external benchmark/data requirements also mean the reviewed checkout is not an as-is reproduction package.

The experimental uncertainty is underspecified. The headline games comparisons appear to report one training trajectory per configuration rather than variation across independent training runs, while Table 3 explicitly selects each ablation's best checkpoint on the same eight-benchmark suite it reports. That selection can make the displayed ablation levels optimistic. The designer-adaptation controls also change multiple variables at once; the paper acknowledges that they establish only that the full bundle wins, not that designer gradient updates alone caused the difference. The reward ablation is cleaner, but it identifies only the regret blend against the particular standalone EMA signal tested.

The “open-ended self-improvement” framing exceeds the evidence. The source itself concedes that environment complexity is bounded by model scale and context, GRPO remains human-authored, no optimal-curriculum result is proved, and evaluation stays on fixed tasks. Under [the fixed-decomposition lens](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), gains within this pipeline do not validate its excluded representations, operations, partitions, or objectives.

Finally, environment validity is not the same as execution safety. The inspected loader executes generated Python with `exec`, while timeouts, smoke tests, and a model-based solvability screen check functionality and can fail open; they do not by themselves establish containment. Running this approach outside an independently sandboxed training host would therefore require a separate security argument.

## Recommended Next Action

Update [Choosing what to learn requires both validity and learning-value gates](../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) with SPADE as an executable-environment case, explicitly separating corpus-driven search breadth from functional/semantic validity gates and hint-regret-based learning value.
