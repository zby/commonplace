---
description: "Agent-R review: MCTS trajectory collection and self-training pipeline that distills failed and successful agent rollouts into revision training data"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-01"
---

# Agent-R

Agent-R, from ByteDance Seed's `ByteDance-Seed/Agent-R` repository, is a research pipeline for training language-model agents to revise mistakes. The implementation does not provide a persistent runtime memory store. Instead, it collects task rollouts with Monte Carlo Tree Search, converts paired good and bad paths into supervised revision conversations, and expects those examples to be used for model fine-tuning. The behavior-shaping retained artifact is ultimately a trained model, with JSON and JSONL trajectory artifacts as the inspectable intermediate memory.

**Repository:** https://github.com/ByteDance-Seed/Agent-R

**Reviewed commit:** [82fcc1ca7873b460949ed49022146dd988c32e31](https://github.com/ByteDance-Seed/Agent-R/commit/82fcc1ca7873b460949ed49022146dd988c32e31)

**Last checked:** 2026-06-01

## Core Ideas

**The retained learning signal starts as search trees, not notes.** `mcts_collection.py` selects a task environment from `TASK`, runs an `ExtendedMCTS` search for each training item, and saves each root under `mcts_result/{Task}/{model_name}/search_results_{idx}.json` ([mcts_collection.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_collection.py)). The saved nodes include conversation state, LLM response, action, observation, recent actions, environment score, visit/value statistics, terminal state, and children ([mcts_utils/webshop/mcts_ws.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/webshop/mcts_ws.py), [mcts_utils/mcts_raw.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/mcts_raw.py)).

**MCTS expands action trajectories against external task environments.** The WebShop, SciWorld, and TextCraft wrappers all reset an AgentGym environment, replay recent actions, sample candidate LLM actions, step the environment, mark negative rewards as disasters, deduplicate sampled responses, and backpropagate terminal rewards ([mcts_utils/webshop/mcts_ws.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/webshop/mcts_ws.py), [mcts_utils/sciworld/mcts_sci.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/sciworld/mcts_sci.py), [mcts_utils/textcraft/mcts_tc.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/textcraft/mcts_tc.py)). This is trace construction for later training, not runtime recall.

**Training data is made by contrasting high-value and low-value paths.** `path_collection.py` loads a saved MCTS root, finds terminal leaf paths, sorts them by average node value, pairs paths whose value gap exceeds `BETA`, and keeps only high paths above `ALPHA` ([path_collection.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/path_collection.py)). It then emits JSONL entries containing `revise_log`, `high_log`, `low_log`, task description, and optional verifier feedback. This turns a tree of exploratory action traces into a smaller supervised-learning artifact.

**Revision is represented inside the conversation target.** For bad-to-good examples, `conversation_generation` preserves the shared prefix, marks bad assistant turns with `loss: False`, inserts a synthetic reflection thought plus `Action: wait` with `loss: True`, and then appends the corrected good-path assistant turns as trainable outputs ([path_collection.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/path_collection.py)). The lesson is not a prose rule or retrieval document; it is encoded as target behavior in the training sequence.

**A verifier model can choose the first bad step.** With `--revise 1`, `revise_worst_path` asks an LLM verifier to judge each action in the bad path as good, bad, or uncertain, using accumulated action-observation context and the task description ([path_collection.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/path_collection.py), [mcts_utils/llm_server.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/llm_server.py)). The first judged-bad action becomes the splice point into the adjacent good path. That verifier output is a trace-derived curation signal, but the code does not attach durable prompt/model provenance to each accepted correction.

**Evaluation is a plain rollout of the current model.** `eval.py` initializes the same environment family and calls `perform_test`, which repeatedly sends the current conversation to the model, parses the next `Action:`, steps the environment, truncates old messages when the prompt exceeds `MAX_TOKEN_LENGTH`, and saves final result JSON under `test_result/` ([eval.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/eval.py), [mcts_utils/llm_server.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/llm_server.py)). There is no retrieval index, memory query API, MCP server, or hook that injects stored trajectories at runtime.

## Artifact analysis

- **Storage substrate:** `model-weights` — JSON files written under `mcts_result/{Task}/{model_name}/` through `ExtendedMCTS.save`, using `mmengine.dump` on the root node
- **Representational form:** `prose` `symbolic` `parametric` — conversation text and revision thoughts, symbolic tree/training/evaluation fields, and distributed-parametric fine-tuned weights
- **Lineage:** `authored` `imported` `trace-extracted` — authored verifier prompts and splice policy, imported task/base-model inputs, and trace-extracted MCTS trees, revision JSONL, and intended fine-tuned model behavior
- **Behavioral authority:** `knowledge` `instruction` `validation` `ranking` `learning` — saved trees and evaluations are audit knowledge; prompts/splice policy instruct extraction; rewards, thresholds, and verifier judgments validate and rank candidates; JSONL and weights carry learning authority

**MCTS result trees.** Storage substrate: JSON files written under `mcts_result/{Task}/{model_name}/` through `ExtendedMCTS.save`, using `mmengine.dump` on the root node. Representational form: mixed symbolic and prose traces: tree topology, visits, values, rewards, actions, observations, full conversation messages, terminal flags, and disaster flags. Lineage: derived from sampled model actions, environment observations/rewards, task data, MCTS parameters from environment variables, and task-specific action cleanup. Behavioral authority: knowledge artifacts while inspected as search evidence; system-definition artifacts on the offline learning path because `path_collection.py` loads them to select which trajectories become trainable examples.

**Revision-training JSONL entries.** Storage substrate: append-only JSONL files at the configured `--output_dir`, defaulting to `mcts_training_data/{task}_{data_type}.jsonl`. Representational form: mixed conversation prose plus symbolic fields such as `loss`, `revise`, `task_num`, `high_log`, `low_log`, and `revise_feedback`. Lineage: derived from paired MCTS leaf paths, `ALPHA`/`BETA` thresholds, optional verifier judgments, and the splice logic in `conversation_generation`. Behavioral authority: system-definition artifacts for fine-tuning because they decide which tokens are supervised and which mistakes are masked out.

**Verifier prompt, revision thoughts, and splice policy.** Storage substrate: Python constants and functions in `path_collection.py` and `mcts_utils/llm_server.py`. Representational form: prose prompt instructions, fixed revision-thought strings, and symbolic control flow. Lineage: authored framework code, not learned from traces. Behavioral authority: system-definition artifacts because they interpret bad-path traces, choose a correction boundary, and shape the exact training target. Effective verifier quality is not established by the code.

**Fine-tuned agent model.** Storage substrate: external model checkpoint directory supplied through `MODEL_DIR` and trained through the README's Xtuner workflow, not through a complete training script in this checkout ([README.md](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/README.md), [mcts_utils/llm_server.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/llm_server.py)). Representational form: distributed-parametric weights. Lineage: intended to be derived from the revision JSONL plus the base model and external training configuration. Behavioral authority: system-definition artifact with always-on generation influence during later evaluation; the checkpoint is the promoted form of the trace-derived lessons.

**Evaluation outputs.** Storage substrate: JSON files under `test_result/{Task}/{model_name}_{model_type}/` and `revise_result/{Task}/{model_name}_{model_type}/`. Representational form: symbolic metrics and replayable message traces. Lineage: derived from a model checkpoint, environment server, task ids, and rollout policy. Behavioral authority: knowledge artifacts for audit and comparison; they do not feed back into the training loop in this code.

The promotion path is unusually explicit: environment trace -> saved MCTS tree -> paired revision JSONL -> external fine-tuned model. It crosses from prose/symbolic traces into distributed-parametric behavior. The weak point is governance rather than mechanics: accepted correction examples do not carry durable source-node ids, verifier prompt/model versions, or review state through to the final training corpus.

## Comparison with Our System

| Dimension | Agent-R | Commonplace |
|---|---|---|
| Primary purpose | Train agents to revise task mistakes through self-training | Maintain a typed methodology KB for future agents and maintainers |
| Raw evidence | MCTS rollouts, environment observations, rewards, and verifier judgments | Source snapshots, notes, reviews, work artifacts, validation and review reports |
| Canonical retained unit | Training examples and ultimately model weights | Git-tracked markdown artifacts with frontmatter, type specs, links, and status |
| Learning loop | Offline trace selection and fine-tuning | Source-grounded writing, review, validation, and workshop-to-library promotion |
| Read-back | Always-on model parameters after training; no runtime retrieval | Pull through search/indexes/links, plus explicit instructions and generated context where configured |
| Governance | Numeric thresholds, reward scores, verifier prompt, and external evaluation | Collection contracts, schemas, deterministic validation, semantic review, git history |

Agent-R is close to Commonplace only at the broad "retained artifacts change later agent behavior" level. It does not keep inspectable advice, notes, playbooks, link graphs, or contextual snippets. Its central bet is that reflection behavior should be distilled into model weights from curated rollouts, while Commonplace keeps behavior-shaping knowledge in readable artifacts unless a symbolic gate or generated index is justified.

The strongest contrast is reviewability. Commonplace can inspect the exact rule, note, link, or validation schema that changed future behavior. Agent-R can inspect the intermediate traces and training examples, but after fine-tuning the operative lesson is distributed across parameters. That is powerful when the desired behavior is low-level action correction, but it makes source-level invalidation and semantic review much harder.

The context-cost tradeoff also differs. Agent-R pays the cost offline in rollout generation, path pairing, verifier calls, and training. At runtime it does not load past trajectories, so it avoids prompt bloat. Commonplace pays a smaller ongoing retrieval/navigation cost and keeps the loaded material explainable.

**Read-back:** `push` — Coarse always-on parameterization after fine-tuning; the code does not implement pull retrieval or instance-targeted push activation over stored trajectories
**Read-back signal:** `coarse` — after fine-tuning the retained lesson is always-on model parameterization, not an identifier or inferred retrieval signal over stored trajectories
**Faithfulness tested:** `no` — the review records evaluation rollouts, but no code-grounded with/without read-back ablation over the learned parameter influence

### Borrowable Ideas

**Promote repeated failures into supervised correction candidates.** A Commonplace analogue would collect repeated validation or review failures into a workshop artifact containing bad attempt, splice point, corrected answer, and evidence. Ready as a report format; not ready for automatic instruction promotion.

**Keep the raw search tree before extracting the lesson.** Agent-R preserves enough tree structure to audit alternatives before generating the smaller training corpus. Commonplace could borrow this for review or planning runs by retaining compact decision trees before promoting a final note or rule. Needs a concrete high-cost workflow where alternatives matter.

**Represent correction boundaries explicitly.** The verifier's first-bad-step judgment is a useful primitive. In Commonplace, a failed agent run could mark the first invalid assumption or first unsupported source use before proposing a fix. Ready for review tooling if paired with source citations and human/semantic gate review.

**Separate trace construction from behavior promotion.** Agent-R's MCTS collection, path conversion, and model training are distinct stages. Commonplace should preserve the same separation for trace-derived methodology: collect evidence first, distill candidates second, promote only after review. Ready as a design constraint.

**Use loss masks as authority markers.** The `loss: False` and `loss: True` flags distinguish context to condition on from tokens to train. A prose-artifact analogue would mark evidence, proposed rule text, and non-authoritative commentary distinctly. Needs a use case in generated training or evaluation corpora.

## Write-side placement

**Write agency:** `automatic` — MCTS collection, path pairing, verifier-assisted splice selection, JSONL generation, and external fine-tuning stages convert rollout traces into retained training artifacts and intended model behavior.

**Curation operations:** `consolidate` `synthesize` `promote` — saved trees are reduced to paired revision examples, those examples synthesize correction behavior, and external fine-tuning promotes the trace-derived lesson into model weights.

### Trace-derived learning

**Trace source:** `trajectories` — MCTS rollouts over task environments preserve conversation state, actions, observations, rewards, terminal flags, and tree statistics
**Learning scope:** `cross-task` — the review describes benchmark/task-family training data and a promoted model behavior, not project-local memory
**Learning timing:** `offline` `staged` — generation, path extraction, external fine-tuning, and evaluation are separate offline stages
**Distilled form:** `prose` `symbolic` `parametric` — revision conversations and thoughts, JSONL fields/loss masks, and final fine-tuned weights

**Trace source.** Agent-R qualifies as trace-derived learning. The raw traces are task rollouts produced by MCTS over WebShop, SciWorld, and TextCraft environments: conversation state, sampled model responses, parsed actions, observations, environment rewards, terminal flags, and tree statistics. Optional verifier calls add action-level judgments over bad paths.

**Extraction.** Extraction is staged. MCTS first builds an exploratory tree and saves it. `path_collection.py` then finds leaf paths, scores them by average value, pairs high and low paths with a configured value gap, optionally asks a verifier to find the first bad action, and writes revision conversations. The final intended extraction step is external fine-tuning, where those JSONL examples become changed model behavior.

**Scope and timing.** Scope is benchmark/task-family oriented rather than project memory. The loop is offline and staged: generate trajectories, derive training data, fine-tune, then evaluate the resulting model. Evaluation rollouts are saved, but I did not find code that automatically mines evaluation failures back into the next training-data cycle.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Agent-R belongs in the trace-to-weights family. It strengthens the survey distinction between inspectable trace-derived artifacts and behavior-shaping artifacts: the MCTS trees and JSONL examples are inspectable, while the promoted capability is distributed-parametric and harder to audit directly.

## Curiosity Pass

**The system title says reflection, but the implemented memory is training data.** Runtime agents are not given a reflective notebook or retrieved memories. They are expected to internalize the correction behavior through fine-tuning.

**The repository has the data-generation path, not a complete shipped training harness.** The README describes Xtuner training and a config path, but the inspected top-level checkout does not include a full training configuration directory. That makes the retained-artifact chain partly code-grounded and partly operationally external.

**Verifier feedback is saved but not deeply governed.** `revise_feedback` records the LLM judgment response, yet there is no durable schema for verifier identity, prompt version, accepted/rejected status, or later audit.

**Prompt truncation protects runtime context size by deleting old messages.** Both MCTS generation and evaluation trim conversation history when it exceeds `MAX_TOKEN_LENGTH`. That keeps action prompts bounded, but it can also remove earlier evidence from long tasks.

**The MCTS implementation is task-wrapper duplicated.** WebShop, SciWorld, and TextCraft share nearly identical `ExtendedMCTS` code with small action/observation differences. That makes the mechanism easy to inspect but raises the chance of task-specific drift.

## What to Watch

- Whether the repository adds the actual fine-tuning configs and scripts referenced by the README; that would make the trace-to-weights promotion path fully inspectable.
- Whether training examples gain stronger lineage fields, such as source tree file, high/low path node ids, verifier model, prompt version, and threshold values; that would make correction candidates easier to audit.
- Whether evaluation failures are automatically routed back into a new MCTS/path-collection cycle; that would turn the current staged pipeline into a more complete iterative self-training loop.
- Whether the task-specific MCTS wrappers are unified behind one tested abstraction; that would reduce hidden differences between task families.
- Whether any runtime retrieval or reflection interface appears; that would change Agent-R from parameterized self-training into a hybrid memory/read-back system.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - compares: Agent-R distills MCTS rollouts into training examples and ultimately model weights.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: Agent-R requires separating MCTS trees, JSONL training data, verifier prompts, model weights, and evaluation logs by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: saved trees, verifier feedback, and evaluation logs are mostly evidence until consumed by extraction or audit.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: training examples, splice policy, verifier prompt, and fine-tuned weights configure or directly shape later behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Agent-R turns execution traces into reusable correction behavior rather than storing raw trajectories for runtime lookup.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Agent-R stores many trajectories, but later behavior changes only after extraction and model training.
