---
description: "Agent-R review: MCTS trajectory self-training system that turns failed and successful task rollouts into revision data and model weights"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-04"
---

# Agent-R

> Replaced 2026-06-04. See [Agent-R](./agent-r.md) for the current review.

Agent-R, from ByteDance Seed, is an offline self-training framework for language-model agents in WebShop, SciWorld, and TextCraft environments. It is not a runtime memory database or retrieval layer. Its memory-relevant mechanism is a trace-derived learning loop: MCTS samples agent-environment trajectories, path processing pairs high- and low-value rollouts, an LLM/verifier-style critique locates the first bad step, and the resulting revision conversations are used to fine-tune a future agent model.

**Repository:** https://github.com/ByteDance-Seed/Agent-R

**Reviewed commit:** [82fcc1ca7873b460949ed49022146dd988c32e31](https://github.com/ByteDance-Seed/Agent-R/commit/82fcc1ca7873b460949ed49022146dd988c32e31)

**Last checked:** 2026-06-04

## Core Ideas

**The retained lesson is a trained policy, not a retrievable memory record.** The README frames Agent-R as iterative self-training where MCTS constructs samples that recover correct trajectories from erroneous ones, then those samples train the model to reflect and revise on the fly ([README.md](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/README.md)). The durable behavior-shaping endpoint is the fine-tuned model checkpoint described by the Xtuner training step, not a queryable store of past cases.

**MCTS turns task interaction into a ranked trajectory tree.** `mcts_collection.py` initializes an AgentGym environment, builds a FastChat conversation, runs an environment-specific `ExtendedMCTS`, and writes each search tree to `mcts_result/{Task}/{model_name}/search_results_{idx}.json` ([mcts_collection.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_collection.py)). The WebShop/TextCraft/SciWorld MCTS classes store action, observation, reward-derived score, terminal/disaster status, recent actions, model response, PUCT value, and children in the node JSON ([mcts_utils/webshop/mcts_ws.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/webshop/mcts_ws.py), [mcts_utils/sciworld/mcts_sci.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/sciworld/mcts_sci.py), [mcts_utils/textcraft/mcts_tc.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/textcraft/mcts_tc.py)).

**Revision data is built by contrasting sibling paths.** `path_collection.py` loads saved MCTS roots, enumerates leaf paths, sorts them by average value, pairs paths whose value gap exceeds `BETA`, requires the high path to clear `ALPHA`, and writes JSONL entries carrying `revise_log`, `high_log`, `low_log`, task description, revision flag, and verifier feedback ([path_collection.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/path_collection.py)). This is not memory recall; it is dataset construction from trajectories.

**The critique oracle is model-mediated and local to the bad path.** `revise_worst_path()` builds an action-observation log, asks the model to classify the current action as good, bad, or uncertain, keeps walking while the judgment is good or uncertain, and stops at the first bad/disaster step before splicing into the better path ([path_collection.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/path_collection.py), [mcts_utils/llm_server.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/llm_server.py)). The oracle is useful but opaque: the retained JSONL keeps the free-form `revision_feedback`, not a separately validated proof that the identified first error is correct.

**Context efficiency is handled by truncating active trajectories, not by retrieval.** MCTS generation and evaluation repeatedly delete older conversation message pairs until the serialized prompt fits `MAX_TOKEN_LENGTH - 60`; the revision verifier truncates its action-observation prompt by chopping the string while it is too long ([mcts_utils/webshop/mcts_ws.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/webshop/mcts_ws.py), [mcts_utils/llm_server.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/llm_server.py), [path_collection.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/path_collection.py)). There is a hard budget and shallow recent-history retention, but no progressive disclosure, index, retrieval, or source-preserving compaction of the generated training corpus.

**Evaluation reads the learned policy as ordinary model behavior.** `eval.py` loads an environment, builds the initial conversation, calls `perform_test()`, and saves final test traces under `test_result/{Task}/{model_name}_{MODEL_TYPE}/...`; the script records `MODEL_TYPE` in the output path but does not implement a governed with/without memory ablation by itself ([eval.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/eval.py), [mcts_utils/llm_server.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/llm_server.py)).

## Artifact analysis

- **Storage substrate:** `files` `repo` `model-weights` — Authored scripts and seed task ids live in the repository; generated MCTS trees, training JSONL, and test traces are local files; the final behavior-changing artifact is the trained checkpoint loaded from `MODEL_DIR`.
- **Representational form:** `prose` `symbolic` `parametric` — Conversations, thoughts, observations, task descriptions, and verifier feedback are prose; JSON nodes, rewards, path values, thresholds, actions, ids, and environment state are symbolic; the trained Agent-R policy is distributed-parametric model state.
- **Lineage:** `authored` `imported` `trace-extracted` — Prompts, scripts, task lists, and action-validity helpers are authored; AgentGym environments and task datasets are imported; MCTS trees, revision conversations, verifier judgments, and trained behavior are extracted from agent-environment trajectories.
- **Behavioral authority:** `knowledge` `instruction` `validation` `ranking` `learning` — Raw and processed traces are knowledge/evidence artifacts; prompt templates and revision thoughts instruct the model; SciWorld action repair and verifier judgments validate candidate actions; MCTS values and path thresholds rank/select traces; the JSONL corpus and checkpoint carry learning authority over future behavior.

**MCTS search trees.** Storage substrate: local JSON files under `mcts_result/{Task}/{model_name}/`. Representational form: prose model responses and observations wrapped in symbolic tree structure: visits, values, PUCT scores, actions, terminal flags, disaster flags, depth, and children. Lineage: trace-extracted from sampled model actions and environment observations/rewards. Behavioral authority: knowledge and ranking artifacts during dataset construction; high-value and low-value leaves become candidates for later revision examples, but the tree itself is not served to the runtime agent.

**Revision JSONL records.** Storage substrate: local JSONL files written by `path_collection.py`. Representational form: prose conversations and verifier feedback inside symbolic fields such as `revise_log`, `high_log`, `low_log`, `task_num`, and `revise`. Lineage: derived from paired MCTS paths, value thresholds, and optional model-guided first-error critique. Behavioral authority: learning artifact for supervised fine-tuning; it changes future behavior only after a training pipeline consumes it.

**Prompt templates and revision thoughts.** Storage substrate: repository source in `mcts_utils/llm_server.py`. Representational form: prose instructions with symbolic output contract `Judgement: <Good or Bad or Uncertain>`. Lineage: authored system-definition artifacts. Behavioral authority: instruction and validation authority over which bad-path prefix is retained before splicing.

**Task/environment data and action repair.** Storage substrate: small repository JSON files plus AgentGym environment servers outside this repo. Representational form: symbolic ids and task filters, plus prose observations and action strings. Lineage: imported from WebShop, SciWorld, TextCraft, and AgentGym. Behavioral authority: validation/routing authority in the data collection loop; SciWorld's `findValidActionNew()` maps invalid model actions to valid environment actions before stepping.

**Trained Agent-R checkpoint.** Storage substrate: model weights loaded through `MODEL_DIR`; the reviewed repo describes the Xtuner training invocation but does not include the referenced `xtuner_config/` directory in the checkout. Representational form: distributed-parametric. Lineage: trace-extracted from MCTS/revision examples after external fine-tuning. Behavioral authority: learning and instruction-like policy authority at inference time; the learned reflection behavior is not inspectable as a discrete memory artifact.

Promotion path: Agent-R has a clear trajectory-to-weights promotion path: raw rollouts -> ranked MCTS trees -> paired failure/success examples -> revision JSONL -> fine-tuned checkpoint. It does not promote traces into readable skills, rules, validators, or a retrievable case library.

## Comparison with Our System

| Dimension | Agent-R | Commonplace |
|---|---|---|
| Primary purpose | Improve task-agent policy through offline trajectory self-training | Maintain a typed, inspectable methodology KB for future agents and maintainers |
| Canonical retained unit | MCTS tree JSON, revision JSONL, trained model checkpoint | Typed Markdown artifacts, source snapshots, indexes, schemas, review reports |
| Write path | Automatic trajectory sampling, value ranking, model-guided critique, JSONL generation, external fine-tuning | Human/agent authored notes and reviews with validation and semantic gates |
| Read-back | Coarse parametric activation through the trained model weights | Mostly explicit pull through search/indexes/links, plus instructions where loaded |
| Governance | Environment reward, value thresholds, verifier prompt, evaluation traces | Type specs, collection contracts, deterministic validation, review bundles, git diffs |

Agent-R is much closer to ML continual-learning research than to Commonplace's file-native knowledge system. It accepts opacity in exchange for a closed learning loop: if the training signal and task environments are good enough, the trained model's behavior improves without needing a human to edit durable rules. Commonplace takes the opposite trade: learned claims, procedures, and reviews stay inspectable, diffable, and linkable, but the learning loop is not automatically closed.

The strongest comparison point is oracle quality. Agent-R can use environment reward and path contrast to decide which trajectories are better, then train on those contrasts. Commonplace rarely has such a compact objective for KB edits: a better note, link, or instruction may pay off only in future tasks that are not known when the artifact is written.

**Read-back:** `push` — The trace-derived artifact reaches future action through model weights loaded for every inference call; the acting model does not retrieve individual past trajectories or ask for a memory lookup.

**Read-back signal:** `coarse` — Activation is checkpoint-level and always-on for that model, not selected by task id, path id, embedding relevance, keyword match, or verifier judgment at inference time.

**Faithfulness tested:** `no` — The repo includes data collection and evaluation scripts, but I did not find a code-level with/without test that isolates whether a particular retained revision artifact changes a later action.

### Borrowable Ideas

**Use paired failure/success trajectories when the oracle is strong.** Ready for benchmarked agent workflows, not for ordinary KB writing. If Commonplace has a task suite with objective pass/fail outcomes, contrasting failed and successful runs could produce candidate instructions or tests.

**Keep first-error localization separate from repair.** Ready as a review-gate pattern. Agent-R's first bad step search suggests a useful QA habit: identify the earliest invalid assumption before rewriting the whole artifact.

**Treat trajectory values as candidate ranking, not acceptance.** Ready now. MCTS scores and `ALPHA`/`BETA` thresholds are useful triage signals, but Commonplace should still require source spans, review state, and validation before promoting a trace-derived lesson into a note or instruction.

**Do not borrow weight promotion as the default KB learning path.** Needs a narrow, high-signal use case. Fine-tuning can close the loop, but it loses the inspectable lineage and composable artifact structure that make Commonplace useful.

**Borrow staged distillation, not the exact substrate.** Ready as a conceptual pattern. The raw -> ranked -> critiqued -> distilled pipeline is more important for Commonplace than whether the final artifact is JSONL or weights.

## Write-side placement

**Write agency:** `automatic` `manual` — Authored scripts and prompts define the workflow, while MCTS collection, path pairing, verifier critique, JSONL writing, evaluation trace writing, and external fine-tuning automatically change retained artifacts from trajectories.

**Curation operations:** `dedup` `synthesize` `promote` — MCTS expansion drops duplicate sampled responses within a node; path processing synthesizes new revision conversations by splicing low- and high-value paths; value thresholds and pairwise gaps promote selected trajectories into the training corpus.

### Trace-derived learning

**Trace source:** `trajectories` `tool-traces` — The raw signal is agent actions, environment observations, rewards, terminal flags, and conversation state from WebShop, SciWorld, and TextCraft rollouts.

**Learning scope:** `cross-task` — The generated corpus is built from many task instances and is intended to train a model that generalizes its reflection behavior across later tasks in the supported environments.

**Learning timing:** `offline` `staged` — Search, path processing, revision-data generation, fine-tuning, and evaluation are separate batch stages rather than an online memory update during deployment.

**Distilled form:** `prose` `symbolic` `parametric` — The intermediate artifacts are prose/symbolic traces and JSONL records; the final learned behavior is distributed-parametric model state.

**Trace source.** Agent-R qualifies as trace-derived because durable training artifacts are generated from model-environment trajectories. Each MCTS node records the acting model's response, selected action, observation, environment score, terminal state, and recent-action history. For SciWorld, action repair also consumes valid-action lists and recent actions before stepping the environment.

**Extraction.** The extraction loop has three filters. MCTS ranks sampled paths by environment reward propagated through the tree. Path collection pairs high- and low-value leaf paths only when their value gap exceeds `BETA` and the high path exceeds `ALPHA`. Optional revision asks the model to judge each bad-path step and stops at the first bad action before joining the better path.

**Scope and timing.** Scope is environment/task-family level, not project memory. Timing is staged: first collect search trees, then generate revision JSONL, then fine-tune with an external Xtuner workflow, then evaluate the trained model.

**Survey placement.** In the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Agent-R belongs in the trajectory-to-weights branch. It strengthens the survey split between readable artifact learning and distributed-parametric learning: the intermediate traces are inspectable JSON, but the behavior-changing memory is the checkpoint.

## Curiosity Pass

**This is memory by policy adaptation, not by storage and retrieval.** Agent-R remembers through changed weights. That is a valid retained behavior-shaping artifact, but it bypasses most memory-system concerns around lookup, provenance, deletion, and contextual activation.

**The training config boundary is outside the inspected code.** The README describes Xtuner training, but the checkout does not include the referenced `xtuner_config/` directory. The review can ground data construction and evaluation in code; exact training hyperparameters and reproducibility are less grounded here.

**The verifier and actor can be the same capability surface.** `path_collection.py` initializes `FuncCallOffline` with `MODEL_NAME` for revision critique. The code supports on-policy revision, but it also means first-error labels inherit the model's current blind spots.

**Prompt truncation is crude but aligned with the benchmark loop.** Deleting older message pairs keeps rollout prompts under budget, but it can erase causally relevant earlier observations. Agent-R relies on training over many trajectories rather than on precise retrieval of old state.

**The generated corpus carries more lineage than the final model.** MCTS JSON and JSONL records expose actions, observations, rewards, and feedback. Once promoted into weights, that lineage becomes behavioral evidence only through probes and evaluation.

## What to Watch

- Whether the repository adds the missing training configuration and checkpoint metadata; that would make the model-weight artifact's lineage auditable rather than README-level.
- Whether revision examples record source path ids, sibling-path ids, and exact first-error positions as stable fields; that would improve traceability from a trained behavior back to source trajectories.
- Whether evaluation scripts add explicit Raw vs Agent-R paired ablations over the same task ids; that would test effective read-back of the learned revision behavior.
- Whether a future version emits readable rules or skills alongside the fine-tuned checkpoint; that would create a bridge from trajectory learning into inspectable Commonplace-style artifacts.
- Whether the critique oracle is diversified beyond the current model; that would reduce the risk that the learner trains on its own uncorrected failure modes.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Agent-R turns task trajectories into revision data and then distributed-parametric behavior.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - contrasts: Agent-R uses traces for weight learning rather than readable memory artifacts.
- [Continual learning's open problem is behaviour, not knowledge](../../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md) - classifies: Agent-R changes behavior through distributed-parametric state, not through knowledge accumulation.
- [Memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) - compares: both Agent-R and AgeMem depend on strong task/environment oracles to justify opaque policy learning.
- [Treat continual learning as substrate coevolution](../../notes/treat-continual-learning-as-substrate-coevolution.md) - frames: Agent-R optimizes the parametric substrate while leaving prose/symbolic artifacts as intermediate data.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Agent-R has coarse parametric activation, not retrieval-based read-back of stored cases.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Agent-R requires separating files, trace JSON, prompts, rankings, and model weights by substrate, form, lineage, and authority.
