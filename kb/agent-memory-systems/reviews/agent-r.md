---
description: "MCTS self-training pipeline that mines environment rollouts into verifier-spliced revision conversations, then documents external fine-tuning as the behavior-learning step"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# Agent-R

Agent-R is ByteDance Seed's research code for "Training Language Model Agents to Reflect via Iterative Self-Training." The repository does not implement a persistent runtime memory for deployed agents; it implements an offline data-construction pipeline that runs agents through AgentGym environments, saves Monte Carlo Tree Search rollouts, converts high/low path pairs into revision conversations, and documents Xtuner fine-tuning as the downstream step that can compile those conversations into model weights.

**Repository:** https://github.com/ByteDance-Seed/Agent-R

**Reviewed revision:** [82fcc1ca7873b460949ed49022146dd988c32e31](https://github.com/ByteDance-Seed/Agent-R/commit/82fcc1ca7873b460949ed49022146dd988c32e31)

## Core Ideas

**MCTS is the trace generator, not the learned memory.** [`mcts_collection.py`](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_collection.py) selects WebShop, SciWorld, or TextCraft adapters from `TASK`, starts an environment conversation, runs `ExtendedMCTS.search(...)`, and writes one `mcts_result/{Task}/{model_name}/search_results_{idx}.json` file per task. The task-specific MCTS classes in [`mcts_utils/webshop/mcts_ws.py`](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/webshop/mcts_ws.py), [`mcts_utils/sciworld/mcts_sci.py`](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/sciworld/mcts_sci.py), and [`mcts_utils/textcraft/mcts_tc.py`](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/textcraft/mcts_tc.py) store `state`, `recent_actions`, `action`, `obs`, `env_score`, `disaster`, visits, values, and children. Those search trees are raw trajectory evidence.

**The operative distillation step pairs better and worse leaves.** [`path_collection.py`](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/path_collection.py) loads an `ExtendedMCTS` root, finds terminal leaf paths, sorts them by average node value, and pairs paths whose terminal-value gap exceeds `BETA`. A high path must also pass the `ALPHA` lower bound. This means the durable training signal is not "all successful traces"; it is a selected contrast between a high-value path and a lower-value sibling path from one search tree.

**Revision conversations splice an error prefix to a better continuation.** `revise_worst_path(...)` walks the bad path step by step and asks a verifier model whether each current action is good, bad, or uncertain. `conversation_generation(...)` keeps the bad prefix until the first judged bad step, inserts a synthetic reflection thought plus `Action: wait`, then appends the unmatched part of the good path as supervised assistant turns. The output JSONL entry includes `revise_log`, `high_log`, `low_log`, `task_description`, `revise`, and `revise_feedback`; the JSONL writer is in [`mcts_utils/llm_server.py`](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/llm_server.py).

**The verifier is model-guided, not an environment oracle.** The verifier prompt in `llm_server.py` asks a model to judge a current action from preceding action-observation text and return `Judgement: <Good or Bad or Uncertain>`. Environment reward still ranks leaves and marks disaster nodes during MCTS, but the precise cut point for revision data is an LLM judgement over trace text.

**The repository writes data, not weights.** The README's training section instructs users to configure Xtuner and run `xtuner train ...`, but the checked-in repository has no `xtuner_config/` directory and no training script. The implemented retained artifacts stop at MCTS JSON and JSONL revision data. Weight learning is a documented downstream consumer, not code this repo can perform by itself.

**Evaluation is ordinary rollout, separate from data construction.** [`eval.py`](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/eval.py) runs `perform_test(...)` from `llm_server.py`, steps the selected environment until done or `max_steps`, and writes `test_result/{Task}/{model_name}_{MODEL_TYPE}/search_results_{idx}.json`. It evaluates a model against tasks; it does not retrieve the constructed conversations at runtime.

## Comparison with Our System

Agent-R is an offline trace-to-training-data system. Commonplace is a files-first knowledge base where agents and maintainers read, validate, link, and revise durable artifacts directly. The overlap is trace-derived learning; the difference is what becomes behavior-shaping.

| Dimension | Agent-R | Commonplace |
|---|---|---|
| Trace source | MCTS rollouts over AgentGym environments | Agent and human work over notes, reviews, indexes, and commands |
| Raw substrate | JSON search trees under `mcts_result/...` | Markdown, generated indexes, review reports, git history |
| Distilled artifact | JSONL revision conversations | Typed notes, instructions, ADRs, commands |
| Oracle mix | Environment reward for path value; LLM verifier for first-error judgement | Validation scripts, review gates, human judgement |
| Runtime activation | None in repo; fine-tuned weights are the intended downstream path | Agents load inspectable files and execute CLI commands |
| Lifecycle | Regenerate files from rollouts; no index, status, supersession, or retirement | Frontmatter status, links, indexes, review/validation procedures |
| Representational bet | Conversation-form supervision, optionally compiled into weights | Inspectable prose and symbolic tooling |

Using the artifact-analysis vocabulary, Agent-R separates [storage substrate](../../notes/definitions/storage-substrate.md) (where retained state persists), [representational form](../../notes/definitions/representational-form.md) (how the operative part is encoded), [lineage](../../notes/definitions/lineage.md) (source dependencies and derivation), and [behavioral authority](../../notes/definitions/behavioral-authority.md) (how the retained artifact can affect behavior) more sharply than many runtime memory systems. Raw search trees are file-backed mixed artifacts: symbolic tree structure plus prose conversation states. Revision JSONL is file-backed prose/mixed supervision. If passed to Xtuner, the behavioral authority moves into distributed-parametric weights, but that move is outside the implemented repo.

The design is stronger than commonplace where a task domain supplies cheap rollouts and scores. It can automatically produce many revision examples without asking a maintainer to write lessons. It is weaker where knowledge must remain inspectable, linkable, and governable. Once revision conversations become weights, the learned behavior is hard to inspect, retire, or cite back to the exact task pair that caused it unless the training pipeline preserves that lineage externally.

## Borrowable Ideas

**Keep raw search trees separate from distilled training material.** Ready as a framing. Agent-R's split between `mcts_result` trees and JSONL revision conversations is clean: raw evidence stays replayable, while the consumed artifact is a curated derivative.

**Use paired good/bad paths rather than isolated successes.** Needs a use case first. For commonplace, a review or workflow failure could be paired with the successful later path before writing an instruction. The value is contrast: the artifact says not just what worked, but where the previous path went wrong.

**Treat first-error localization as its own artifact.** Ready as a design idea, not a current need. `revise_feedback` is worth preserving because it records why a prefix was cut. A commonplace analogue would be a review finding that marks the earliest bad assumption in a failed agent run before promoting a fix.

**Do not blur data generation and weight learning.** Ready now as a caution. Agent-R's README narrates self-training, but the source tree's implemented boundary is data construction. Commonplace should keep the same discipline when reviewing systems: distinguish raw traces, distilled artifacts, and any separate learner that consumes them.

**Environment reward plus model verifier is a useful oracle stack.** Needs a domain with repeated scored tasks. The environment score ranks candidate paths, while the LLM verifier chooses the local correction point. That two-oracle split is more discriminating than asking an LLM to generate a lesson from a failed run with no hard signal.

## Trace-derived learning placement

**Trace source.** Agent-R consumes agent-environment rollouts from WebShop, SciWorld, and TextCraft. Trigger boundaries are per task index for MCTS collection and per saved search-tree file for path processing. The raw trace includes prompts, assistant actions, observations, environment scores, terminal flags, disaster flags, and child links in the MCTS tree.

**Extraction.** Extraction has three stages. First, MCTS expands action candidates and uses environment rewards to set node values. Second, `path_collection.py` selects high/low leaf-path pairs by `ALPHA` and `BETA`. Third, `revise_worst_path(...)` asks a verifier model to judge actions along the low path, then `conversation_generation(...)` rewrites the pair into one supervised revision conversation.

**Storage substrate.** Raw MCTS state persists as JSON files under `mcts_result/{Task}/{model_name}`. Distilled revision data persists as JSONL from `path_collection.py`'s `output_dir`, defaulting to `mcts_training_data`. `revise_feedback`, `high_log`, and `low_log` are stored beside `revise_log` in each JSONL entry. The README's Xtuner step would place later learned behavior in model-artifact storage, but that storage is not implemented in this repository.

**Representational form.** Raw search trees are mixed: symbolic tree structure, scalar visit/value fields, and prose conversation messages. Paired paths are symbolic selections over that tree. Verifier judgements are prose labels with explanation text. Revision JSONL is prose conversation supervision with `"loss": true/false` markers on assistant turns. Downstream fine-tuned weights, if produced, would be distributed-parametric.

**Lineage.** The lineage chain is environment task -> MCTS tree JSON -> high/low terminal path pair -> verifier-judged bad prefix -> spliced revision conversation -> optional external fine-tuning run. The repo preserves enough fields in each JSONL row to inspect the high path, low path, task description, and verifier feedback, but it does not add a stable source-tree file ID, commit hash, training run manifest, or invalidation rule to the JSONL output.

**Behavioral authority.** Raw trees and paired paths are [knowledge artifacts](../../notes/definitions/knowledge-artifact.md): they act as evidence for data construction. Verifier judgements have local evaluation authority inside the converter because they choose the cut point. Revision JSONL is a [system-definition artifact](../../notes/definitions/system-definition-artifact.md) when consumed by a trainer: it supplies learning input that can alter future model behavior. The final authority story, if Xtuner is run, is weight-level learning rather than prompt-time retrieval or file loading.

**Scope and timing.** Scope is benchmark/task-family specific, tied to AgentGym's WebShop, SciWorld, and TextCraft environments. Timing is offline or staged: collect trees, generate revision data, then train/evaluate a model. There is no online deployment memory loop.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Agent-R is a trajectory-run ingestion system whose distinctive output is paired-path revision supervision. It splits the survey's "symbolic artifact" branch: the repo itself produces inspectable JSON/JSONL artifacts, while the intended downstream effect is distributed-parametric behavior after external fine-tuning. It strengthens the survey claim that trace-derived learning often has multiple retained artifacts with different authority, and it should not be collapsed into a single "memory" label.

## Curiosity Pass

**The first-error story is stronger than the implementation boundary.** The README highlights timely revision from the first erroneous step. The code does implement verifier-guided first-error localization, but only as JSONL construction. The actual behavioral update depends on an external training setup absent from the repo.

**The "adjacent correct path" is operationally a paired high-value path, not a semantic sibling proof.** `pair_leaf_paths(...)` pairs any two leaf paths whose terminal average-value gap exceeds `BETA`. They share the same MCTS root, and may share a prefix, but the code does not explicitly require a same-parent divergence at the first error point. The verifier and splicing logic supply the local repair story after pair selection.

**The verifier can preserve uncertain actions.** `revise_worst_path(...)` treats both "good" and "uncertain" as keep-going labels. That makes sense for avoiding premature cuts, but it also means weak verifier confidence can leave questionable prefix steps in the supervised example until the first explicit "bad".

**The data writer preserves more audit material than the training format needs.** `revise_log` is the likely training payload, but each output row also retains `high_log`, `low_log`, and `revise_feedback`. That is a useful lineage affordance, even though there is no formal schema or manifest around it.

**The repository is small and research-script shaped.** Environment variables configure most behavior; imports select task-specific modules at import time from `TASK`; output directories are conventions rather than declared artifacts. That is acceptable for a paper release, but it limits direct borrowability as infrastructure.

## What to Watch

- Whether a future release includes the missing Xtuner config and records training-run lineage from JSONL rows into model artifacts.
- Whether pair selection is tightened to explicitly identify same-parent high/low branches at the first recoverable error.
- Whether verifier judgements are calibrated against environment replay, human labels, or a stronger evaluator.
- Whether generated revision data remains useful across model iterations, or whether each actor model requires fresh MCTS trees because its failure modes shift.
- Whether descendants keep the raw-tree / selected-pair / verifier-feedback / training-conversation split, which is the most reusable design element here.

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: Agent-R adds a paired-path revision-supervision case where inspectable JSONL is intended to become weight-level behavior through external fine-tuning
- [distillation](../../notes/definitions/distillation.md) — exemplifies: MCTS traces are compressed into goal-directed revision conversations for a learning consumer
- [representational form](../../notes/definitions/representational-form.md) — exemplifies: one pipeline moves from mixed trace trees to prose/symbolic supervision and potentially distributed-parametric weights
- [lineage](../../notes/definitions/lineage.md) — sharpens: Agent-R preserves high/low logs and verifier feedback but lacks a formal run manifest or invalidation rule
- [behavioral authority](../../notes/definitions/behavioral-authority.md) — exemplifies: the same trace family shifts from evidence to evaluation input to training input across the pipeline
