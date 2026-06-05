---
description: "AgentFly/Memento review: planner-executor agent with JSONL case-bank memory, trace-judged case writes, and parametric or SimCSE case read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
tags: [trace-derived]
---

# AgentFly

AgentFly, branded as Memento in the inspected repository, is an Agent-on-the-Fly planner-executor agent for benchmark question answering. Its memory system is a case-based reasoning layer: previous tasks, plans, rewards, labels, and retrieved-case outcomes are stored as JSONL rows, then read back as positive and negative planning examples through either non-parametric SimCSE retrieval or a trained pairwise case retriever.

**Repository:** https://github.com/Agent-on-the-Fly/AgentFly

**Reviewed commit:** [42fbbcac63dd58ed6856c0761357345a58e4f032](https://github.com/Agent-on-the-Fly/AgentFly/commit/42fbbcac63dd58ed6856c0761357345a58e4f032)

**Last checked:** 2026-06-04

## Core Ideas

**The agent is a hierarchical planner-executor with MCP tools.** The baseline client asks a meta-planner to produce JSON task plans, sends each task to an executor with MCP tool schemas, records intermediate task results in shared history, and loops back to the planner for final answer or replanning ([client/agent.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/agent.py)). The memory variants keep that architecture and add case read-back before planning ([client/no_parametric_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/no_parametric_cbr.py), [client/parametric_memory_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/parametric_memory_cbr.py)).

**Memory is a compact case bank, not full trajectory replay.** The durable memory rows contain question/case text, plan JSON, and a reward or positive/negative case label; the larger result records contain meta traces, executor traces, tool history, judgements, and rationales, but the read-back prompt uses compact examples rather than replaying those full traces ([memory/memory.jsonl](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/memory.jsonl), [memory/dummy_memo.jsonl](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/dummy_memo.jsonl), [client/no_parametric_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/no_parametric_cbr.py), [client/parametric_memory_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/parametric_memory_cbr.py)). This is the main context-efficiency move: preserve the plan-shaped lesson, not the whole interaction.

**Read-back is bounded by top-k and label filtering.** Non-parametric retrieval embeds case keys and the current task with a SimCSE model, selects top-k by cosine similarity, then formats positive reward rows and negative reward rows under separate caps ([memory/np_memory.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/np_memory.py), [client/no_parametric_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/no_parametric_cbr.py)). Parametric retrieval scores each case-plus-plan prompt against the current query with a trained classifier, sorts by score, and injects at most `MEMORY_TOP_K` cases ([memory/parametric_memory.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/parametric_memory.py), [client/parametric_memory_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/parametric_memory_cbr.py)). The complexity is still example-heavy: every selected case can carry a full plan.

**The parametric path learns a retriever, not an executor model.** `train_memory_retriever.py` trains a SimCSE-backed classifier over `(retrieved case prompt, current query) -> truth_label`, saving `best.pt` and `last.pt` checkpoints when invoked ([memory/train_memory_retriever.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/train_memory_retriever.py)). The LLM weights are unchanged; the learned artifact is a read-back ranking model that decides which cases become in-context examples.

**Trace-derived learning is benchmark-loop mediated.** The main automatic write paths run inside benchmark scripts: they judge answers with an LLM, append result JSONL rows, append compact memory entries, append retrieved-case training rows in the parametric variant, and reload the memory pool for later tasks ([client/no_parametric_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/no_parametric_cbr.py), [client/parametric_memory_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/parametric_memory_cbr.py)). The implementation supports continual accumulation in those evaluation loops, but the inspected source does not implement autonomous compression, deduplication, contradiction handling, or personal preference memory; those are README TODOs ([README.md](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/README.md)).

## Artifact analysis

- **Storage substrate:** `files` `model-weights` — Case banks, training rows, dummy memory, benchmark result rows, and source data are JSONL files; the parametric retriever can persist PyTorch checkpoints under the configured output directory, although no checkpoint file is present in the inspected checkout.
- **Representational form:** `prose` `symbolic` `parametric` — Questions, cases, rationales, and plans are prose; JSON fields, rewards, case labels, truth labels, traces, and prompt templates are symbolic; the optional case retriever checkpoint is distributed-parametric state.
- **Lineage:** `authored` `imported` `trace-extracted` — Prompt templates and client code are authored; benchmark data and seed case rows are imported or preloaded; result rows, compact case entries, retrieved-case training rows, and retriever checkpoints derive from task trajectories and judgement outcomes.
- **Behavioral authority:** `knowledge` `instruction` `validation` `ranking` `learning` — Case examples are knowledge artifacts when they evidence prior tasks; the formatted "positive" and "negative" blocks instruct the planner to imitate or avoid patterns; LLM judge outputs validate benchmark answers; SimCSE similarity and the trained classifier rank read-back; training rows and checkpoints provide learning authority for future retrieval.

**Case-bank rows.** `memory.jsonl` rows use `case`, `plan`, and `case_label`; `dummy_memo.jsonl` rows use `question`, `plan`, and `reward`. Both formats are consumed by wrapper-specific loaders and formatted into examples. Their operative split is the plan prose/JSON used as planner advice and the label/reward used as a selection and warning signal.

**Training-data rows.** `training_data.jsonl` rows connect a current query, a retrieved case, its case label, the retrieved plan, and a truth label indicating whether the full run was judged correct. These are not read directly into the planner; they are learning artifacts for the retriever training script.

**Retriever model.** `MemoryRetrieverClassifier` concatenates two encoded text representations and classifies whether a case should be useful for a query. Its effective relevance quality is not verified from source code alone; the code shows the architecture and save/load path, not deployment performance.

**Benchmark result rows.** The benchmark loops write result records with plan JSON, meta trace, executor trace, tool history, prediction, ground truth, judgement, rationale, and reward. These are retained trace evidence for humans and for memory acquisition, but the read-back path does not load the full traces into future planner prompts.

The promotion path is case-bank to retrieval training to checkpoint-mediated ranking. A compact case can first act as prompt-visible advice, then later contribute to the learned read-back policy; it does not become a validator, tool, symbolic procedure, or durable Commonplace-style reviewed instruction.

## Comparison with Our System

AgentFly and Commonplace both treat retained artifacts as behavior-shaping context rather than as hidden model updates. The important difference is artifact granularity. Commonplace keeps typed, reviewed, source-linked notes and instructions in git; AgentFly keeps compact benchmark cases and labels in JSONL, with optional promotion into a trained ranker.

AgentFly is stronger as a quick online-learning loop for benchmark agents. It can run a task, judge the result, append a case, and use the updated case pool for the next task in the same batch. Commonplace is stronger as a governed knowledge base: its artifacts carry frontmatter, type contracts, validation, replacement history, citations, and explicit review state.

The clearest tradeoff is authority. AgentFly's read-back cases are powerful because they are injected before planning, but they are also brittle: positive and negative examples can steer the planner without provenance beyond the case row and judge label. Commonplace would not promote a trace-derived pattern into system-definition authority without source preservation and review.

### Borrowable Ideas

**Positive and negative examples as a compact read-back format.** Commonplace could use paired "imitate / avoid" examples in operational instructions or review-gate prompts when repeated failures have clear shape. Ready for narrow workflows; not ready as a general replacement for notes.

**Keep full traces separate from compact lessons.** AgentFly stores rich result traces but serves compact cases. Commonplace can apply the same split to review runs: preserve full outputs as evidence, then serve only a small distilled lesson or warning.

**Train retrieval from judged usefulness, not just semantic similarity.** The parametric retriever is a useful design direction: retrieval should learn which prior artifacts helped, not only which look textually similar. This needs a concrete Commonplace use case with enough judged retrieval events before implementation.

**Reload memory after writes in batch runs.** The benchmark loop immediately reloads the memory pool after appending a case. Commonplace could mirror that for long review sweeps where a newly accepted finding should affect later items in the same run, but only with explicit scope boundaries.

**Do not borrow ungated example authority wholesale.** Injected cases tell the planner to follow positives and avoid negatives. In Commonplace, that authority should pass through review status, source links, and expiry or supersession policy.

## Write side

**Write agency:** `automatic` — The benchmark clients automatically append result rows, compact memory entries, and parametric training rows after judged task runs; the training script can then write retriever checkpoints from accumulated training data.

**Curation operations:** `promote` — Reward/case labels, retrieved-case truth labels, and the trained retriever change which existing cases receive read-back salience. The code does not implement automatic deduplication, consolidation, in-place evolution, contradiction invalidation, age decay, or cleanup over stored cases.

### Trace-derived learning

**Trace source:** `trajectories` `tool-traces` — The result records retain plan output, meta-planner cycles, executor steps, tool calls, answer judgement, rationale, and reward; the compact memory writes mostly consume the query, plan, and judged success/failure rather than the full trace body.

**Extraction.** The non-parametric loop turns each judged task into a compact `(question, plan, reward)` row and reloads the memory pool. The parametric loop turns each judged task into a compact `(case, plan, case_label)` row and, when cases were retrieved, appends `(query, retrieved case, retrieved plan, truth_label)` rows for offline retriever training. The oracle is an LLM judge over the predicted answer and ground truth.

**Learning scope:** `cross-task` — Rows from one benchmark task can influence retrieval and planning for later tasks in the same configured memory pool.

**Learning timing:** `staged` — Case rows are appended online during benchmark execution, but parametric learning is a separate offline training step that writes checkpoints.

**Distilled form:** `prose` `symbolic` `parametric` — The first distilled artifacts are prose/symbolic case rows and labels; the optional second-stage artifact is a trained neural retriever checkpoint.

On the survey axes, AgentFly is trace-derived learning with a compact case-bank output and an optional weight-learning read-back policy. It strengthens the distinction between learning LLM task behavior and fine-tuning the LLM itself: the learned weights, when present, belong to a retrieval selector, not to the planner or executor model.

## Read-back

**Read-back:** `push` — The host client retrieves cases from memory and appends the formatted case prompt to `shared_history` before the meta-planner call; from the planner's perspective, the memory arrives without a separate tool request.

**Read-back signal:** `inferred / embedding` — Non-parametric read-back uses SimCSE embeddings and cosine similarity over case keys; parametric read-back uses a learned classifier over encoded query and case-plus-plan text. Both infer relevance from content rather than matching an explicit case identifier.

**Faithfulness tested:** `no` — The code records retrieved cases, benchmark judgements, and rewards, but it does not run with/without read-back ablations or post-answer audits proving that a particular injected case changed the planner's behavior.

Read-back assembles before the planner invocation. In the non-parametric variant, the selected examples are split by reward into positive and negative blocks with configurable caps; in the parametric variant, selected examples are split by `case_label`. The injected prompt explicitly tells the planner to focus on positive examples and avoid negative patterns. That makes the cases more forceful than passive evidence, but effective uptake, precision, and context dilution are not verified from code.

The selection policy is bounded by `MEMORY_TOP_K`, `MEMORY_MAX_POS_EXAMPLES`, and `MEMORY_MAX_NEG_EXAMPLES`; the broader conversation is separately trimmed by token count. There is no progressive disclosure inside a case: if a case is selected, its question and plan text are included.

Other consumers include the offline trainer, which consumes training rows to update retriever weights, and human evaluators, who can inspect result JSONL rows and benchmark figures. Those consumers are separate from the planner read-back classification.

## Curiosity Pass

The repository name and README branding diverge: the requested source is AgentFly, while the README, package name, and clone instructions call the system Memento. The review uses AgentFly as the local review title and names the internal branding in prose.

The README's "continual learning" claim is partly code-grounded and partly operational. The code does implement automatic case accumulation and retriever training data capture; retraining still requires a separate training invocation, and there is no scheduler or closed-loop checkpoint refresh in the inspected files.

The case bank is narrower than "experience replay" can suggest. Full meta/executor/tool traces are recorded in result files, but future planner prompts receive compact question-plan examples, not replayed tool trajectories or environment states.

The parametric retriever is the most distinctive mechanism, but it adds an opaque ranking layer around otherwise inspectable JSONL cases. That may improve relevance, yet it weakens the local-first audit story unless training data, checkpoint provenance, and evaluation results remain easy to inspect.

The current memory implementation is benchmark-shaped. User personal memory, memory compression, and multi-modal memory are listed as future work, so they should not be counted as implemented retained-artifact mechanisms at this commit.

## What to Watch

- Whether the repository wires automatic retraining or checkpoint refresh into the benchmark loop; that would move AgentFly from staged learning toward a tighter online selector-learning loop.
- Whether memory compression is implemented over stored cases; that would add a real consolidation operation rather than only compact acquisition from traces.
- Whether duplicate, contradictory, or stale cases are detected; without that, the case bank can accumulate misleading negative and positive examples.
- Whether result traces become read-back material or training inputs beyond compact plans; that would change both context complexity and trace-derived classification.
- Whether user personal memory is added as a separate store; that would shift the system from benchmark case reasoning toward a broader agent memory substrate.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes AgentFly's JSONL case bank from the host-client injection path that actually puts cases into planner context.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - frames the top-k case-selection and compact-plan strategy as the central memory design tradeoff.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - supports separating case rows, training rows, result traces, prompt templates, and learned retriever weights.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - frames judged task runs becoming compact cases and selector-training rows.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies the prompts, labels, retrieval policy, and trained selector when they steer future planning.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies prior task cases and result traces as evidence or advice before stronger authority is assigned.
