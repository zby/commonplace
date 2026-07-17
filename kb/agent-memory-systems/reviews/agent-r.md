---
description: "Agent-R review: MCTS trace collection, revision-trajectory synthesis, checkpoint-level read-back, and no runtime retrieval store"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
tags: [trace-learning]
---

# Agent-R

Agent-R, from ByteDance Seed's `ByteDance-Seed/Agent-R` repository, is an iterative self-training framework for language-model agents in WebShop, SciWorld, and TextCraft-style environments. At the reviewed commit, it collects MCTS rollout trees, converts high- and low-value paths into revision training conversations, relies on external Xtuner training to turn those conversations into model weights, and evaluates by loading a checkpoint through vLLM. It is an agent-memory system only in the trace-derived, parametric-memory sense: past trajectories are retained in files and then distilled into model weights, not retrieved at runtime as a memory database.

**Repository:** https://github.com/ByteDance-Seed/Agent-R

**Reviewed commit:** [82fcc1ca7873b460949ed49022146dd988c32e31](https://github.com/ByteDance-Seed/Agent-R/commit/82fcc1ca7873b460949ed49022146dd988c32e31)

**Source directory:** `related-systems/Agent-R`

## Core Ideas

**MCTS is the trace collection engine.** `mcts_collection.py` initializes an AgentGym environment, runs `ExtendedMCTS.search()`, and saves per-task JSON trees under `mcts_result/{Task}/{model_name}/search_results_{idx}.json` ([mcts_collection.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_collection.py)). The task-specific MCTS nodes retain model responses, actions, observations, recent action history, environment score, terminal/disaster flags, visits, value, and children ([mcts_utils/webshop/mcts_ws.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/webshop/mcts_ws.py), [mcts_utils/sciworld/mcts_sci.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/sciworld/mcts_sci.py)).

**Revision data is synthesized from path contrasts, not stored as episodic memory.** `path_collection.py` loads a saved tree, sorts leaf paths by average value, pairs high- and low-value paths whose gap exceeds `BETA`, optionally asks the actor model to judge where the bad path first goes wrong, then splices bad-prefix and good-continuation material into `revise_log` JSONL training entries ([path_collection.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/path_collection.py)). The durable artifact before training is a dataset of conversations with loss flags, not a searchable memory object.

**The learned memory is distributed-parametric.** The README's training step sends the generated revision data into Xtuner training, and the inference wrapper loads `MODEL_DIR` with vLLM's `LLM(model=os.environ["MODEL_DIR"], dtype="half")` ([README.md](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/README.md), [mcts_utils/llm_server.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/llm_server.py)). The repository does not ship a trained checkpoint or the Xtuner config it references, so the review can verify the data-generation and checkpoint-loading surfaces, but not the actual fine-tuned weights.

**Runtime context efficiency is truncation plus parametric compression.** During MCTS generation and evaluation, prompts are assembled from the current conversation and trimmed by deleting older message pairs when tokenized length exceeds `MAX_TOKEN_LENGTH` ([mcts_utils/webshop/mcts_ws.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/webshop/mcts_ws.py), [mcts_utils/llm_server.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/llm_server.py)). There is no top-k retrieval, index, progressive disclosure ladder, or runtime trace lookup. The main context-efficiency move is offline compression of many trajectories into checkpoint behavior.

**Trust comes from environment reward and model-guided critique, not provenance governance.** MCTS backpropagates environment reward through tree nodes; path selection uses `ALPHA` and `BETA`; revision mode asks an LLM verifier for `good`, `bad`, or `uncertain` judgments over action-observation history ([path_collection.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/path_collection.py), [mcts_utils/mcts_raw.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/mcts_raw.py)). The code preserves generated traces and feedback fields, but it does not attach stable provenance to learned weights, implement invalidation, or review individual distilled lessons.

## Artifact analysis

- **Storage substrate:** `model-weights` — Authored code and intermediate MCTS/revision/evaluation artifacts live in repository and local files, but the final behavior-shaping retained artifact is an externally trained checkpoint loaded from `MODEL_DIR`.
- **Representational form:** `prose` `symbolic` `parametric` — Trajectories contain prose model responses and observations plus symbolic roles, actions, rewards, loss flags, node values, and tree structure; after training, the retained correction behavior is parametric model state.
- **Lineage:** `authored` `trace-extracted` — Scripts, prompt templates, and task wiring are authored; MCTS trees, revision conversations, evaluation logs, and fine-tuned weights are derived from agent-environment trajectories.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Trace files are evidence for training and audit; prompts and environment adapters instruct and route interaction; environment rewards and verifier judgments validate trajectories; MCTS values rank candidate paths; the generated conversations drive checkpoint learning.

**MCTS result trees.** Storage substrate: JSON files under `mcts_result/{Task}/{model_name}`. Representational form: symbolic tree records with prose model responses and observations. Lineage: trace-extracted from actor-model rollouts against AgentGym environments. Behavioral authority: learning input and ranking surface, because node values, visits, rewards, and terminal flags decide which paths can become training examples.

**Revision training data.** Storage substrate: JSONL files produced by `path_collection.py`, defaulting to `mcts_training_data/{task}_{data_type}.jsonl`. Representational form: conversation records containing role/content fields, `loss` flags, high/low logs, task descriptions, and optional verifier feedback. Lineage: trace-extracted and synthesized from paired MCTS paths. Behavioral authority: learning authority over the future checkpoint; the data does not directly advise a runtime agent unless a host reads it separately.

**Fine-tuned checkpoint.** Storage substrate: model weights outside the reviewed repository, loaded from `MODEL_DIR` for MCTS, revision judging, and evaluation. Representational form: parametric. Lineage: intended to be trained from revision trajectories through the README's Xtuner workflow, but the concrete training config and resulting checkpoint are not present in the checkout. Behavioral authority: push-like instruction/knowledge authority at inference, because the checkpoint changes every generated action without adding textual memory to the prompt.

**Task and environment adapters.** Storage substrate: repository Python modules plus AgentGym service objects. Representational form: symbolic code and prose prompt/history construction. Lineage: authored. Behavioral authority: routing and validation authority: task selection imports the WebShop, SciWorld, or TextCraft MCTS implementation; environment rewards and valid-action filters determine terminal state, disaster flags, and acceptable actions ([mcts_collection.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_collection.py), [mcts_utils/sciworld/eval_utils_sw.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/sciworld/eval_utils_sw.py)).

**Evaluation result files.** Storage substrate: JSON files under `test_result/{Task}/{model_name}` or `test_result/{Task}/{model_name}_{MODEL_TYPE}` depending on the script path. Representational form: symbolic records with full conversation state. Lineage: trace-extracted from checkpoint rollouts. Behavioral authority: validation evidence for comparing checkpoints, but the code does not feed these results back into online memory during the same evaluation run ([eval.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/eval.py), [mcts_utils/llm_server.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/llm_server.py)).

**Promotion path.** Agent-R promotes task experience through a staged chain: environment rollout -> MCTS tree -> high/low path pairing -> verifier-guided revision conversation -> external fine-tuning -> checkpoint-loaded evaluation. The promotion crosses from files and symbolic/prose traces into parametric authority. It does not promote individual memories into citations, rules, validators, or a governed review state.

## Comparison with Our System

Agent-R and Commonplace both treat past work as material that should change future agent behavior, but they put the retained authority in different places. Agent-R turns trajectories into model weights. Commonplace turns sources, analyses, and procedures into typed Markdown artifacts, generated indexes, validation rules, and review workflows. Agent-R has higher behavioral compression: a checkpoint can apply learned corrections without extra prompt tokens. Commonplace has higher auditability: retained claims remain inspectable, linkable, replaceable, and validated in git.

The strongest divergence is read-back. Commonplace mostly depends on explicit retrieval through `rg`, indexes, links, and skills. Agent-R has no runtime retrieval layer at all; once trained, the learned trace-derived behavior is always present because the checkpoint is loaded. That avoids memory-selection misses but makes provenance, targeted recall, and invalidation much harder.

Agent-R's trace pipeline is also more automated than Commonplace's normal authoring loop. It can synthesize many correction examples from environment rollouts without human writing. The cost is that the learned artifact cannot be inspected as a set of durable lessons. Commonplace would need an intermediate artifact layer if it borrowed the trace-learning loop: traces should first become reviewable examples, rules, or candidate notes before gaining stronger authority.

### Borrowable Ideas

**Path-contrast training examples.** A Commonplace analogue would compare failed and successful agent trajectories that share a common prefix, then generate reviewable correction examples. Ready as a workshop/report pattern, not as automatic library mutation.

**First-error localization before synthesis.** Agent-R's verifier asks where a bad path first becomes bad, then splices from the adjacent good path. Commonplace could use the same idea in review QA: localize the first unsupported claim or wrong decision before rewriting a whole artifact. Ready for constrained review workflows.

**Keep raw traces separate from distilled authority.** Agent-R has a clear raw-tree to revision-data to checkpoint chain. Commonplace should preserve that separation for any trace-derived workflow: logs are evidence, synthesized examples are candidates, accepted notes or instructions are the durable authority. Ready as a convention.

**Do not borrow checkpoint-only memory for KB methodology.** Parametric compression is useful for agent policy learning, but it is a poor fit for Commonplace's goal of inspectable methodology. It needs measurable task loops and an audit surface before it should influence repository instructions.

## Write side

**Write agency:** `manual` `automatic` — A user manually configures and runs collection, revision, training, and evaluation scripts, but the distinctive store changes are automatic: MCTS writes rollout trees, path processing synthesizes revision conversations, Xtuner training is expected to update model weights, and evaluation writes rollout results.

**Curation operations:** `synthesize` `promote` — Agent-R generates new revision-training conversations from paired high- and low-value paths, then the staged training workflow promotes those examples into checkpoint-level behavioral authority. It filters and ranks paths with rewards and thresholds, but it does not implement durable memory deduplication, consolidation, invalidation, decay, or in-place evolution of a textual memory store.

### Trace-learning

**Trace source:** `trajectories` `session-logs` — The raw signal is agent-environment trajectories: model responses, actions, observations, environment rewards, recent-action histories, terminal/disaster flags, and full conversation states saved in MCTS or evaluation outputs.

**Learning scope:** `per-project` `cross-task` — The scripts are task-family scoped (`webshop`, `sciworld`, `textcraft`) and write task-specific traces, while the README frames the trained agent model as reusable across these task settings.

**Learning timing:** `offline` `staged` — MCTS data collection, path-to-training-data conversion, external Xtuner training, and evaluation are separate offline stages. The evaluated agent does not update a memory store online while solving a test task.

**Distilled form:** `parametric` — The durable learned behavior after the full workflow is a fine-tuned checkpoint; intermediate distilled examples are prose/symbolic JSONL conversations.

**Extraction.** `mcts_collection.py` collects candidate behavior through tree search. `path_collection.py` ranks leaf paths by average value, pairs better and worse paths when their value gap exceeds `BETA`, optionally asks the actor model to label actions as good, bad, or uncertain, and emits a conversation where bad behavior is followed by a reflection/wait step and then a good continuation ([path_collection.py](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/path_collection.py)). The oracle is a mix of environment reward, path value thresholds, and LLM verifier judgment.

**Distillation trigger and policy.** The trigger is operator-run staged processing: collect MCTS files first, run `path_collection.py` over an input directory, then train with Xtuner as described in the README. The curation policy is value-thresholded and pairwise: high paths must exceed `ALPHA`, high/low pairs must differ by more than `BETA`, and the optional revision mechanism truncates at the first judged bad action.

**Survey placement.** Agent-R belongs in the trace-derived self-training family, with a stronger parametric endpoint than systems that retain playbooks or notes. It strengthens the survey split between raw trace retention and distilled behavior-shaping artifacts: the raw MCTS trees are not the operative memory at evaluation time; the checkpoint is.

## Read-back

**Read-back:** `push` — The retained learned behavior re-enters action by loading the fine-tuned checkpoint from `MODEL_DIR`; every model call uses that parametric state. The repository contains no runtime memory lookup API, vector store, episodic retrieval, or prompt injector.

**Read-back signal:** `coarse` — Checkpoint read-back is always-on for every generation made by that loaded model. It is not targeted by task instance identifiers, lexical matching, embeddings, or an LLM relevance judgment at runtime.

**Faithfulness tested:** `no` — The code writes evaluation results and labels output directories with `MODEL_TYPE`, but it does not implement a with/without-memory ablation, perturbation test, or post-action audit proving that a particular trace-derived correction caused a behavior change.

**Direction edge case.** This is push only in the parametric-memory sense: no remembered text is inserted into the prompt. The system's memory read-back is checkpoint selection before invocation, not contextual activation through retrieved artifacts.

**Selection, scope, and complexity.** Selection happens before the agent loop when the operator chooses `MODEL_DIR` and `MODEL_TYPE`; inside the loop, the code only trims conversation history to fit `MAX_TOKEN_LENGTH`. Runtime context volume is bounded by truncation, while learned trace knowledge carries no token budget because it lives in weights. That improves prompt efficiency but makes the scope and contents of the retained behavior opaque.

**Authority at consumption.** Checkpoint read-back has strong behavioral authority: it changes the policy that produces every `Thought` and `Action`. It is not an enforced gate, and the environment can still reject or penalize actions, but the learned correction behavior is more than advisory context.

**Other consumers.** Humans can inspect MCTS JSON, revision JSONL, and evaluation result files. Those files are evidence and training inputs; the evaluated agent does not consult them unless a separate run retrains or loads a different checkpoint.

## Curiosity Pass

**The repository is mostly the data pipeline, not the trained memory.** The code makes the trace and revision stages inspectable, but the operative parametric artifact is outside the checkout. That is normal for training research code, but it limits code-grounded review of the learned behavior.

**"Reflect on the fly" is implemented as trained behavior, not online memory maintenance.** The runtime agent can generate reflective actions because the model was trained on revision conversations, but evaluation does not append a new lesson, retrieve past failures, or update a memory store during a task.

**The strongest memory is the least inspectable artifact.** MCTS trees and revision JSONL are readable; the checkpoint is what actually changes future action. This is the central tradeoff: excellent context compression, weak lineage at the point of consumption.

**Path pairing is a compact synthesis mechanism.** Instead of summarizing a whole failed episode, Agent-R constructs a local correction by contrasting nearby tree paths. Even if the checkpoint endpoint is not borrowable for Commonplace, the path-contrast idea is useful for review and repair workflows.

## What to Watch

- Whether the repository adds the referenced Xtuner config or trained checkpoints. That would make the parametric artifact and training recipe directly inspectable.
- Whether evaluation gains explicit Agent-R vs raw ablation wiring beyond directory labels. That would strengthen the read-back faithfulness claim.
- Whether revision examples gain stable provenance links back to tree node ids or source file paths. That would make trace-derived lessons easier to audit and invalidate.
- Whether a runtime memory component is added. Any retrieval store, prompt injector, or online adaptation loop would materially change the read-back verdict.
- Whether path processing adds deduplication, contradiction handling, or curriculum management across generated examples. That would move the write side beyond synthesis into richer curation.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Agent-R has trace-derived retention, but no runtime retrieval or textual memory activation.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - applies: Agent-R turns trajectories into future behavior through self-training.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Agent-R requires separating raw trace files, synthesized training data, authored scripts, and parametric checkpoints.
- [Lineage](../../notes/definitions/lineage.md) - frames: the useful audit question is how a checkpoint traces back to MCTS trees and revision examples.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - frames: checkpoint loading gives retained traces strong policy-level authority without textual context.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: MCTS and evaluation logs are evidence artifacts until training turns them into policy.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompts, thresholds, environment adapters, and checkpoint weights configure future behavior.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: Agent-R shifts context pressure from runtime prompt selection into offline parametric compression.
