---
description: Iterative self-training agent that mines MCTS search trees into revision conversations and weight-update datasets, using strong environment rewards rather than persistent artifact memory
type: note
tags: [related-systems]
status: current
last-checked: 2026-03-20
---

# Agent-R

Agent-R is a research codebase for training language-model agents to revise mistakes during environment interaction. In the inspected repo, the concrete loop is: run Monte Carlo Tree Search over action trajectories, collect good and bad paths under environment reward, optionally ask a verifier model where the failed path first goes wrong, splice corrected continuations into revision conversations, then rewrite those conversations into a training dataset for later fine-tuning. Built by the ByteDance Seed team as the open-source implementation of the Agent-R paper.

**Repository:** https://github.com/ByteDance-Seed/Agent-R

## Core Ideas

**The primary learned target is model weights, not a memory artifact.** The repo's durable outputs are search trees and JSONL conversation datasets, but the README's training phase hands those datasets to Xtuner for fine-tuning. The inspectable artifacts are intermediate supervision products, not the final learning substrate.

**Trajectory collection is MCTS over environment interaction.** `mcts_collection.py` drives task-specific `ExtendedMCTS` implementations for WebShop, SciWorld, and TextCraft. Each node executes a candidate action in the environment, records observation and reward, and backpropagates `env_score` through the tree. Failed branches can terminate early as `disaster` states when reward drops below zero.

**Reflection is constructed by path surgery, not freeform summarization.** `path_collection.py` does not merely ask for a reflection string. It pairs high-value and low-value leaf paths, finds the first wrong step in the bad path through `revise_worst_path(...)`, inserts a synthetic revision thought, and then splices the remainder of a better path onto the corrected branch. The core artifact is a repaired conversation trace.

**The verifier is local and step-sensitive.** In revision mode, Agent-R prompts a verifier over the running action-observation history plus the next action and observation. The goal is to judge whether the step is good, uncertain, or wrong early enough to revise mid-trajectory rather than waiting for end-of-rollout failure.

**Dataset construction is explicit and lossy in a useful way.** `conversation_generation(...)` and `rewrite(...)` convert searched paths into training conversations with `loss` markers and simplified `{system,input,output}` style turns. The tree structure, branch statistics, and alternate paths are mostly discarded once the training sample is written. Agent-R intentionally compresses rich search traces into standard fine-tuning examples.

**The repo implements collection and rewriting more concretely than training.** Search, path pairing, revision, and JSON/JSONL rewriting are all present in code. The actual fine-tuning stage is delegated to external Xtuner commands, and the README references a training config that is not included in this checkout. So the weight-learning story is real, but the inspected implementation is stronger on data generation than on the training harness itself.

## Comparison with Our System

Agent-R is almost the opposite of Commonplace on substrate choice. It uses inspectable traces only as temporary supervision material, then pushes the learning into model weights. We keep the learned result in inspectable artifacts and accept the slower human+agent loop that comes with that choice.

| Dimension | Agent-R | Commonplace |
|---|---|---|
| Trace source | MCTS-searched task trajectories with action, observation, and reward | Human+agent editing traces, notes, links, workshop artifacts |
| Learned substrate | Fine-tuning dataset first, then model weights | Notes, links, instructions, workshop artifacts |
| Promotion target | Weight updates via external training | Inspectable text artifacts only |
| Update style | Search, pair good/bad paths, splice corrected conversations, train | Manual curation and targeted file edits |
| Oracle strength | Strong environment reward and path-value comparisons | Mostly human judgment and local validation |
| Scope | Benchmark task families with executable environments | Cross-domain KB |

Agent-R is stronger than our current system on automatic supervision generation toward a closed learning loop. Once the environments and rewards are in place, the repo can turn its own failures into training data and hand that data off to a weight-update stage.

Commonplace is stronger on inspectability and incremental refinement. Agent-R's datasets are readable, but the learned policy after training no longer participates in the same editable knowledge substrate as the traces that produced it.

Relative to [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md), Agent-R is a clean weight-learning case with a more explicit correction-conversation construction phase than [OpenClaw-RL](../../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md). The interesting middle layer is the dataset surgery between trace collection and training.

## Borrowable Ideas

**Construct corrected conversations from paired good and bad paths.** Needs a use case first. Agent-R's splice operation is more informative than a simple success/failure label because it shows what the corrected continuation looks like from the failure point onward.

**Use step-local verification instead of only end-of-run judgment.** Ready now as a design pattern where the oracle is strong enough. The verifier in `revise_worst_path(...)` tries to locate the first actionable mistake, which is exactly where repair guidance is most useful.

**Keep search traces and training samples as separate layers.** Ready now as a pattern. Agent-R makes an explicit distinction between rich exploratory logs and the compressed supervision format used downstream. That separation could help workshop pipelines that need both auditability and compact downstream artifacts.

**Exploit value gaps, not just binary success.** Needs a use case first. Pairing leaf paths only when their average values differ by more than `BETA` is a concrete reminder that not all failures are equally informative.

## Curiosity Pass

The most interesting part of Agent-R is not that it does self-training. Many systems can say that. The interesting part is the intermediate representation it invents on the way to self-training: a repaired conversation built from adjacent good and bad branches in a search tree.

That makes Agent-R more relevant to our survey than a generic fine-tuning pipeline. It shows a concrete way to turn trajectories into better supervision than "successful rollout yes/no." The repo is effectively learning how to write better correction examples from search structure.

The ceiling is the usual split-substrate problem. Once the correction capability is trained into weights, the system gets better behavior but loses the editable knowledge surface. The code can construct revision traces elegantly, but the final learner still becomes opaque.

## What to Watch

- Whether later versions keep the path-surgery dataset construction or collapse to simpler preference pairs or outcome labels
- Whether the missing training-harness details get filled in with a first-class in-repo fine-tuning pipeline
- Whether step-local verifier judgments transfer outside benchmarks with clear action-observation traces
- Whether similar correction-trace construction appears in systems that keep the promoted result as artifacts instead of weights

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: Agent-R is a clean trajectory-to-weights case with an unusually explicit dataset-construction layer between trace collection and training
- [memory management policy is learnable but oracle-dependent](../memory-management-policy-is-learnable-but-oracle-dependent.md) — sharpens: Agent-R also works because it has a strong environment oracle and executable task family, not because weight learning removes the evaluation problem
- [OpenClaw-RL: Train Any Agent Simply by Talking](../../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md) — compares: both learn from interaction into weights, but Agent-R shows a richer intermediate supervision-construction step through search-tree pairing and revision traces
- [ExpeL](./expel.md) — contrasts: ExpeL keeps its learned result in inspectable rules and retrieved traces, while Agent-R uses inspectable traces only as supervision on the way to weight updates
- [Reflexion](./reflexion.md) — sharpens: Agent-R also cares about correction after failure, but it turns failure into training data rather than a prompt-visible verbal memory
