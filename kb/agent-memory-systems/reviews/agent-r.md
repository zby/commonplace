---
description: Self-training agent that mines MCTS action-observation trees into path-paired revision conversations, then hands the resulting JSONL off to an external fine-tuner rather than keeping a persistent memory artifact
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-12"
---

# Agent-R

Agent-R is a research codebase for training language-model agents to reflect on failure during environment interaction. The concrete loop in the repo is: run a task-specific Monte Carlo Tree Search over action trajectories in an AgentGym environment, collect high-value and low-value leaf paths under environment reward, ask a verifier model where the bad path first goes wrong, splice the corrected continuation from a sibling good path onto that wrong step with a synthetic revision thought, and rewrite the resulting conversations into `{system, input, output}` JSONL training samples. Built by ByteDance Seed as the open-source implementation of the Agent-R paper.

**Repository:** https://github.com/ByteDance-Seed/Agent-R

## Core Ideas

**The durable learning target is model weights; inspectable artifacts are intermediate.** The repo produces two kinds of files: MCTS search-tree JSON dumps under `mcts_result/{task}/{model}/` and per-task JSONL training data under the `--output_dir` passed to `path_collection.py`. The README then hands that JSONL off to Xtuner (`xtuner train llama3_8b_instruct_full_alpaca_e3_copy.py --deepspeed deepspeed_zero2`). Trees and conversations exist only to feed training; nothing in this checkout persists a reusable reflection, rule, or playbook.

**Trajectory collection is MCTS over environment rollouts, not sampling from chat logs.** `mcts_collection.py` instantiates `ExtendedMCTS` from one of `mcts_utils/{webshop,sciworld,textcraft}/mcts_*.py`. Each task subclass overrides `_generate` to reset the environment to the task index, replay `node.recent_actions` to the current node, issue one more action via `FuncCallOffline.llm_func(...)`, and create a child node carrying `action`, `obs`, `env_score`, and a `disaster` flag when `new_env_score < 0`. `expand()` samples `N_GEN` children, deduplicates by LLM response, and back-propagates terminal rewards up the tree; `best_child()` selects by PUCT (`mcts_raw.py`).

**Reflection is path surgery over a search tree, not freeform self-critique.** `path_collection.py::find_leaf_paths` enumerates root-to-leaf paths; `sort_leaf_paths_by_value` ranks them by `node.value / node.visits`; `pair_leaf_paths` forms ordered pairs whose average-value gap exceeds `BETA`. For each pair, `revise_worst_path(calling, worst_path, best_path, task_description)` walks the bad path, asks the verifier about each step, and stops at the first `bad` judgement. `conversation_generation(bad_node_path, good_node_path)` then emits the bad prefix with `loss: False`, a randomly sampled `revision_thoughts` line plus `Action: wait` with `loss: True`, and the good continuation from the shared parent onwards.

**The verifier is local, step-sensitive, and prompt-coupled to the corruption vocabulary.** In `llm_server.py`, `prompt_template` asks the verifier to classify the current action-observation pair as `good`, `bad`, or `uncertain` given task description and running action-observation history. In `revise_worst_path`, `good` and `uncertain` advance the revise path; `bad` (or `disaster`) terminates and becomes the splice point. There is no voting, no ensemble, no calibration — the verifier is a single prompted call whose output string must contain a keyword after `Judgement:`.

**Dataset rewriting discards search structure aggressively.** `rewrite(dataset, output_path)` in `llm_server.py` converts each `revise_log` into a flattened Xtuner-style schema: the first three messages become `{system, input, output}`, then remaining pairs become `{input, output}` records inside a `conversation` list. Tree topology, sibling paths, verifier feedback, path values, and `BETA`/`ALPHA` gate thresholds all disappear at this boundary. The surgery is upstream of training; the trainer sees only rewritten conversations.

**The repo is much stronger on data construction than on the training harness.** Everything under `mcts_collection.py`, `path_collection.py`, and the three `mcts_utils/{task}/mcts_*.py` modules is present and runnable. The training step is delegated: Xtuner is an external project, the referenced config `llama3_8b_instruct_full_alpaca_e3_copy.py` is not in this checkout, and `xtuner_config/` does not exist. `eval.py` and `perform_test_revise(...)` in `llm_server.py` evaluate a separately trained model via an `agentenv` server. So "iterative self-training" is real as a data-generation pipeline; the training loop itself is out of repo.

## Comparison with Our System

Agent-R and Commonplace sit on opposite ends of the substrate-class axis. Agent-R treats inspectable traces as temporary supervision material and compiles the learned result into model weights. Commonplace keeps the learned result in inspectable artifacts — notes, links, instructions — and accepts a slower human-plus-agent loop as the cost.

| Dimension | Agent-R | Commonplace |
|---|---|---|
| Trace source | Task-indexed MCTS trees with action, observation, env_score, disaster flags | Editing sessions, notes, links, workshop artifacts |
| Learned substrate | Xtuner-ingested JSONL conversations, then model weights | Inspectable text artifacts only |
| Promotion target | Model weights via external fine-tuning | Human-curated notes, indexes, and instructions |
| Update style | Pair paths by value gap, splice corrections, rewrite, fine-tune | Manual curation, targeted file edits, review bundles |
| Oracle strength | Strong environment reward plus step-sensitive verifier | Human judgment with local validation gates |
| Scope | Three benchmark task families with executable AgentGym servers | Cross-domain methodology KB |

Agent-R is ahead of Commonplace on closed-loop supervision: once an AgentGym environment and a task list exist, the repo can turn its own failures into correction examples without human labeling. Commonplace is ahead on inspectability and incremental refinement — after Agent-R's fine-tuning step, the learned behavior is no longer an editable artifact and cannot be argued with or linked to other knowledge.

Relative to [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md), Agent-R is a cleaner trajectory-to-weights case than [OpenClaw-RL](https://arxiv.org/html/2603.10165v1) because the intermediate data structure is much richer: not live next-state training samples with reward/directive signals, but a paired search tree with step-local bad-step localization and splice correction.

## Borrowable Ideas

**Pair high- and low-value traces and splice the correction at the first divergence.** Needs a use case first. Compared to a binary success/failure label or a freeform reflection, Agent-R's splice makes the correction itself visible in the artifact. The pattern transfers anywhere we have paired attempts at the same target, even without MCTS.

**Use step-local verifier judgements to locate the failure point.** Ready now as a design pattern where the oracle is strong enough. The `good/uncertain/bad` prompt is simple and localizable; the value is in forcing the verifier to commit to a step, not a whole rollout.

**Gate pairing on a meaningful value gap, not on strict success/failure.** Ready now as a pattern. The `BETA` threshold in `pair_leaf_paths` says "only contrast attempts whose outcomes differ enough that the diff is informative." That applies to any scoring system, including review or quality-gate data.

**Separate rich exploratory traces from the compressed downstream artifact.** Ready now as a pattern. Agent-R keeps full MCTS JSON dumps on disk and emits flattened JSONL for training. Workshop pipelines that need both auditability and compact downstream artifacts can use the same split.

**Sample revision-thought prefixes from a fixed pool.** Not borrowable as a direct technique, but instructive as a warning. The 20-phrase `revision_thoughts` list injects template-y self-criticism. It works as training-signal noise but would be immediately visible as a quality problem if it appeared in a text-artifact system; helpful boundary for what "reflection" can look like.

## Curiosity Pass

The interesting contribution is not "self-training language agents." Many systems claim that. The novel piece is the intermediate representation: a repaired conversation assembled from adjacent branches in a search tree with a synthesized revision thought glued in. That representation carries more information than a success/failure label and more structure than an open-ended reflection.

The ceiling, though, is exactly the substrate choice. The repaired conversations exist as JSONL only long enough to feed Xtuner. After training, the correction capability lives in weights; nothing in the resulting model can be inspected, linked, or contested the way a note can. The trace is informative, the intermediate artifact is readable, and the learned result is opaque — and that is by design.

The verifier call is also simpler than it sounds. A single-prompt classification with a keyword-matched judgement field has no calibration or aggregation. The path-surgery loop trusts the verifier completely to pick the splice point. Whether this is robust enough outside curated benchmarks is a separate question the repo does not answer.

And the training harness remaining out-of-repo is worth flagging. The "iterative self-training" narrative is doing some work here: the MCTS-to-JSONL pipeline is real, the fine-tuning step exists only as a README command plus a missing config file. Readers should treat the inspected repo as a data-generation codebase with a training story, not a training codebase.

## What to Watch

- Whether later versions keep the path-surgery construction or collapse to simpler preference-pair (DPO-style) or outcome-label datasets
- Whether the missing training harness gets included as first-class in-repo code or stays behind an Xtuner reference
- Whether step-local verifier judgements transfer to domains without clear action-observation boundaries
- Whether similar pair-splice correction appears in systems that keep the promoted artifact inspectable rather than compiling it into weights
- Whether the `revision_thoughts` pool gets replaced with learned or context-dependent transitions

**Trace-derived learning placement.** (1) Trace source: MCTS rollouts in three AgentGym environments (`webshop`, `sciworld`, `textcraft`); triggers are per-task-index search runs bounded by `MAX_DEPTH`, `ITERA`, and `N_GEN`, not per-turn or per-session. (2) Extraction: paired leaf paths, verifier-judged first-bad-step localization, and spliced revision conversations, then a flatten-and-rewrite pass to Xtuner conversation records; the oracle is the AgentGym `env_score` plus the verifier prompt. (3) Promotion target: model weights via external Xtuner fine-tuning; search trees and JSONL are intermediate. (4) Scope: per-benchmark task family (one task index at a time, generalizing within the benchmark), not cross-task or cross-domain. (5) Timing: staged in offline cycles — MCTS collection, then path pairing/revision, then rewriting, then fine-tuning; nothing runs online during deployment. On the survey's axes, Agent-R fits axis 1's **trajectory-run pattern** (repeated rollouts over a bounded task family) and axis 2's **weight learning** substrate. It strengthens the survey's claim that trajectory-to-weights systems can still carry a rich intermediate artifact layer, and it sharpens the subtype that pairs good and bad trajectories with explicit splice points rather than relying on binary outcome labels.

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: Agent-R is a trajectory-to-weights case with an unusually structured intermediate dataset-construction layer between trace collection and training
- [memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — sharpens: Agent-R works because AgentGym supplies both a reward oracle and an executable task family, not because weight learning removes the evaluation problem
- [OpenClaw-RL: Train Any Agent Simply by Talking](https://arxiv.org/html/2603.10165v1) — compares: both mine interaction into weights, but Agent-R shows a richer intermediate supervision-construction step via search-tree pairing and step-local revision splices rather than OpenClaw-RL's next-state training samples with reward/directive signals
- [ExpeL](./expel.md) — contrasts: ExpeL keeps its consolidation in a maintained natural-language rule list that persists across runs, while Agent-R uses inspectable traces only as supervision on the way to weight updates
- [Autocontext](./autocontext.md) — compares: both bridge trajectories to weights, but Autocontext keeps a persistent playbook/report layer alongside training export, while Agent-R treats the JSONL as transient supervision only
