---
source: https://arxiv.org/html/2605.23904v2
description: "SkillOpt paper treating agent skill documents as trainable external state with bounded text edits, validation gates, rejected-edit buffers, and slow/meta updates"
captured: 2026-05-28
capture: web-fetch
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# SkillOpt: Executive Strategy for Self-Evolving Agent Skills

Author: Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Xue Yang, Chong Luo
Source: https://arxiv.org/html/2605.23904v2
Date: 25 May 2026

arXiv:2605.23904v2 [cs.AI]

Snapshot note: The arXiv HTML rendering omits or mangles some mathematical notation and numeric table deltas. This snapshot preserves the recoverable prose, section structure, qualitative findings, and visible table values. Check the PDF before relying on precise formulas or missing table values.

## Abstract

The paper argues that agent skills should be trained as external state for frozen agents, rather than hand-written, generated once, or loosely self-revised. SkillOpt is presented as a controllable text-space optimizer for agent skills: a separate optimizer model converts scored rollouts into bounded add/delete/replace edits on a single skill document, and edits are accepted only when they improve a held-out validation score. The method adds a textual learning-rate budget, rejected-edit buffer, and epoch-wise slow/meta update. The deployed result is a compact skill document that adds no optimizer calls or model-weight updates at inference time.

Across six benchmarks, seven target models, and three execution harnesses (direct chat, Codex, Claude Code), the authors report that SkillOpt is best or tied-best across all evaluated model/benchmark/harness cells, outperforming no-skill, human-skill, one-shot LLM skill, Trace2Skill, TextGrad, GEPA, and EvoSkill baselines. Transfer experiments report positive transfer across model scales, across Codex and Claude Code harnesses, and to a nearby math benchmark.

## 1 Introduction

The paper frames agent adaptation as increasingly procedural rather than purely parametric. In tool-using and file-using agents, a skill document can package procedures, tool policies, output constraints, and failure modes. If the recurring adaptation object is the agent's procedure, the authors argue that the skill document itself should be treated as a trainable object.

SkillOpt repeatedly samples trajectory batches, analyzes successes and failures, proposes structured add/delete/replace edits, ranks candidate edits under a textual learning-rate budget, applies bounded updates, and evaluates each candidate skill on a held-out selection split. Rejected edits become negative feedback; an epoch-wise slow/meta update preserves longer-horizon regularities. Only the best accepted skill is exported as `best_skill.md`.

The paper stresses that the deep-learning analogy is operational: rollout and reflection batch sizes control evidence noise; textual learning rate controls how far the skill can move; held-out validation gates accepted updates; and the slow/meta update acts like a momentum-like consolidation mechanism.

## 2 Related Work

The paper positions SkillOpt between prompt auto-tuning, agent-configuration search, and skill construction/evolution systems. It cites GEPA, ABSTRAL, EvoTest, SkillsBench, Trace2Skill, SkillX, AutoSkill, AutoRefine, EvoSkills, SkillRL, and related work on trajectory-driven reflection and prompt optimization.

The authors distinguish SkillOpt by optimizing one persistent, portable domain skill with training-style controls, rather than optimizing full prompts, whole agent configurations, growing skill libraries, or model weights.

## 3 Method

### 3.1 Problem Setup

A skill is a natural-language policy inserted into the agent context before execution. In direct-chat benchmarks it is prepended to system or developer instructions; in tool-use harnesses it becomes persistent procedural memory. The target model and execution harness are frozen. SkillOpt uses train, selection, and test splits: train supplies rollout experience, selection gates candidate skill updates, and test is held out for final reporting.

The optimizer state includes the current skill, best validation-gated skill, cached skill hashes, a rejected-step buffer, and optional slow/meta-update state.

### 3.2 Forward Pass: Rollout Evidence

At each optimization step, the target model runs a rollout batch with the current skill. The harness records task metadata, messages, tool calls, observations, command outputs, final answers, verifier feedback, and benchmark-specific context such as spreadsheet previews or document references. Smaller batches update quickly but noisily; larger batches expose recurring patterns before the skill changes.

### 3.3 Backward Pass: Minibatch Reflection

The optimizer model turns trajectories into skill edits. It separates failures from successes, partitions them into reflection minibatches, and asks for structured add/delete/replace proposals. Failure minibatches propose corrective rules for common failures; success minibatches preserve behaviors that work. Local proposals are merged hierarchically, first within failure and success groups, then with failure corrections prioritized.

### 3.4 Bounded Text Updates

SkillOpt's learning-rate analogue is an edit budget: the maximum number of skill edits applied at one step. The optimizer ranks merged edits by expected utility and clips them to the allowed budget. The paper argues that bounded updates prevent useful rules from being erased, incompatible instructions from being introduced, or local failures from causing overfit rewrites.

SkillOpt supports constant, linear, cosine, and autonomous schedules. It can operate in patch mode with append, insert, replace, and delete operations, or in rewrite mode where selected suggestions condition a full skill rewrite.

### 3.5 Validation Gate and Rejected-Edit Buffer

Every candidate skill is evaluated on the selection split with the same frozen target model and harness. A candidate is accepted only if it strictly improves the current selection score; otherwise it is rejected. Rejected updates are recorded with observed failure patterns and score drops, then fed into later reflection calls in the same epoch so the optimizer can avoid repeating failed edits.

The paper emphasizes strict gating: ties are rejected, and the deployed skill should not silently drift. Edit application is logged in `edit_apply_report.json` so the source of each change can be recovered.

### 3.6 Epoch-Wise Slow/Meta Update

Fast updates learn from current rollout batches. At the end of an epoch, SkillOpt compares the same sampled training tasks under the previous epoch's skill and the current skill, grouping them into improvements, regressions, persistent failures, and stable successes. The optimizer writes longitudinal guidance into a protected slow-update field, and this candidate is also passed through validation.

The optimizer-side meta skill summarizes which edit patterns helped, which were rejected, and which failures persisted across epochs. This guidance is used only during training; it is not shipped with the target model. The deployed skill remains compact while the optimizer benefits from richer training history.

### 3.7 Harness-Agnostic Deployment

SkillOpt uses a lightweight adapter interface. An adapter constructs train/evaluation batches, injects the current skill into the agent context, runs the native harness, and returns scored trajectories. The same optimizer is used for direct QA, spreadsheet execution, document reasoning, multimodal QA, embodied environments, and Codex-style or Claude Code-style execution loops.

## 4 Experiments

The experiments evaluate SkillOpt across SearchQA, SpreadsheetBench, OfficeQA, DocVQA, LiveMathematicianBench, and ALFWorld. Target models include GPT-family and Qwen-family models. Harnesses include direct chat, Codex, and Claude Code. Baselines include no skill, human skill, one-shot LLM skill, Trace2Skill, TextGrad, GEPA, and EvoSkill.

### 4.1 Main Results

The main result table reports held-out test scores. SkillOpt is described as best or tied-best on every evaluated cell, with positive gains over no-skill baselines throughout. On GPT-5.5 direct chat, visible rows include SearchQA from 77.7 to 87.3, SpreadsheetBench from 41.8 to 80.7, OfficeQA from 33.1 to 72.1, DocVQA from 78.8 to 91.2, LiveMathematicianBench from 37.6 to 66.9, and ALFWorld from 83.6 to 95.5.

The paper reports that gains are especially large on procedural benchmarks such as SpreadsheetBench, OfficeQA, and LiveMathematicianBench, where strict procedures and answer formats expose the limits of zero-shot frontier models. Smaller target models also benefit, which the authors interpret as compact skills supplying procedural knowledge that the target model does not already hold in weights.

### 4.2 Ablations

Hyperparameter and component ablations vary training set size, reflection minibatch size, rollout batch size, edit budget, scheduler, slow-update samples, rejected buffer, and slow/meta update.

The qualitative findings are:

- Moderate bounded edit budgets are competitive across settings.
- Bounded updates outperform uncontrolled rewriting.
- Removing the rejected-edit buffer lowers scores on SearchQA, SpreadsheetBench, and LiveMath.
- Removing both meta skill and slow update produces the largest drop in the ablation suite, especially on SpreadsheetBench.
- Validation checkpoints tend to track held-out test performance, suggesting that selection gating reduces overfitting to training rollouts.

### 4.3 Analysis and Transfer

The paper evaluates transfer across model scale, execution harness, and nearby benchmarks. Visible transfer rows report positive transfer in every cross-model, cross-harness, and cross-benchmark cell shown.

For cross-harness transfer, a SpreadsheetBench skill trained inside Codex transfers to Claude Code with a large positive gain over Claude Code's no-skill baseline, and the reverse transfer also improves Codex. The authors argue that this suggests the learned skill is not only a harness-specific command recipe, but contains workbook-level procedures such as structure-first inspection, formula-aware verification, and static-value materialization.

The optimizer-strength analysis compares a strong frontier optimizer against a target-matched optimizer. The stronger optimizer produces larger gains in all tested cells, but target-matched optimization still recovers a substantial fraction of the gain. Because the optimizer runs offline, stronger optimizer use increases training cost but not deployment cost.

### 4.4 Learned Skills: Compactness, Cost, and Examples

The learned skills are reported as compact. Table 6 lists final skill lengths ranging from 379 tokens for LiveMathematicianBench to 1,995 tokens for SpreadsheetBench, with one to four accepted edits in the GPT-5.5 target/optimizer runs. The paper emphasizes that many proposed edits are rejected; only a few validation-passing edits survive into the deployed skill.

Training-token cost varies by benchmark. Procedural benchmarks with short rollouts are cheaper per test-point gain than longer or multimodal tasks such as SearchQA and DocVQA. The deployment distinction is that this training cost is paid once; after export, `best_skill.md` adds no optimizer calls, no weight updates, and only a compact context artifact.

### 4.5 Qualitative Skill Evolution

The paper gives qualitative examples for ALFWorld and SpreadsheetBench. The visible descriptions emphasize learned procedural rules rather than instance-specific answers: for example, environment exploration and inventory checks in ALFWorld, or workbook structure inspection, formula awareness, verification, and value materialization in SpreadsheetBench.

## 5 Conclusion

The paper concludes that agent skill documents can be optimized as external natural-language state for frozen agents. It presents SkillOpt as a reproducible, validation-gated text-space training loop that improves a compact skill artifact while keeping the target model and harness fixed. The authors position this as a lightweight alternative to model-weight adaptation for domains where scored trajectories and held-out validation are available.

## Appendix B Limitations

The authors identify several limitations:

- SkillOpt relies on scored trajectories and a held-out selection split, so it is most directly applicable when tasks have automatic verifiers, exact-match metrics, executable checks, or reliable feedback signals.
- Open-ended domains with subjective, multidimensional, or costly success criteria may require stronger human or model-based evaluation.
- Training requires rollout computation and optimizer-model calls. This cost is amortized when a skill is reused, but may be unattractive for one-off tasks.
- SkillOpt optimizes one portable skill rather than a large skill library or model weights, so a single skill may be insufficient for highly heterogeneous domains.
- Optimized skills can encode training-distribution heuristics, so held-out evaluation remains necessary before transfer to substantially different models, harnesses, or task settings.

## Appendix C Signals

The appendix provides executable prompt contracts for the optimizer model. These include failure-analysis prompts, success-analysis prompts, merge prompts, final ranking prompts, slow-update prompts, and optimizer-memory prompts. The prompts require structured JSON outputs so edits can be parsed, filtered, applied, and validated without manual intervention.

The failure-analysis prompt asks the optimizer to identify common failure patterns across multiple failed trajectories and propose concise generalizable edits. The success-analysis prompt asks for common successful behaviors worth encoding. Slow-update and meta-skill prompts distinguish training-model-facing longitudinal guidance from optimizer-side memory.
