---
description: "ReasoningBank review: trace-derived benchmark memories selected by embeddings and injected into WebArena and mini-SWE-agent prompts"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# ReasoningBank

ReasoningBank, from Google Research's `google-research/reasoning-bank` repository, is a research codebase for making WebArena and SWE-Bench agents reuse lessons extracted from prior successful and failed trajectories. At the reviewed commit, the implemented memory system is not a general memory server; it is two benchmark-integrated loops that write JSONL memory banks, append embedding-cache rows, select one similar prior task, and inject that selected memory text into the next agent run.

**Repository:** https://github.com/google-research/reasoning-bank

**Reviewed commit:** [ed80611788292ea739f1effd31f16c53823b8a0d](https://github.com/google-research/reasoning-bank/commit/ed80611788292ea739f1effd31f16c53823b8a0d)

**Source directory:** `related-systems/reasoning-bank`

## Core Ideas

**Memory is induced from benchmark trajectories.** WebArena's `pipeline_memory.py` runs a task, evaluates the result, then invokes `induce_memory.py` to append a memory record to a website/mode-scoped JSONL file ([pipeline](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/pipeline_memory.py), [induction](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/induce_memory.py)). The SWE-Bench path follows the same shape inside the patched mini-SWE-agent batch runner: select prior memory, run the instance, save the trajectory, judge success/failure, and append generated memory items ([SWE-Bench runner](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/third_party/src/minisweagent/run/extra/swebench.py)).

**Successful and failed runs are both learning inputs.** WebArena extracts think/action pairs from `step_*.pkl.gz`, attaches the task query and correctness signal, and uses separate success/failure prompts to produce up to three Markdown memory items ([WebArena induction](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/induce_memory.py), [WebArena memory prompts](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/prompts/memory_instruction.py)). The mini-SWE-agent path saves message trajectories, asks an LLM judge whether the task succeeded, then uses coding-specific success/failure prompts ([SWE-Bench runner](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/third_party/src/minisweagent/run/extra/swebench.py), [SWE memory prompts](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/third_party/src/minisweagent/memory/instruction.py)).

**Retrieval is top-1 embedding selection over prior task queries.** Both memory managers load cached query embeddings, embed the current task with Gemini or Qwen support, score an instruction-aware current query against cached vectors, and map the highest scoring cached task id back to a JSONL memory record ([WebArena memory management](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/memory_management.py), [SWE memory management](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/third_party/src/minisweagent/memory/memory_management.py)). The default call requests `n=1`; the inspected code does not add confidence thresholds, diversity, deduplication, source freshness, or a memory-level token budget.

**Read-back is prompt injection performed by the harness.** WebArena writes the selected memory items to a text file before constructing the BrowserGym experiment, and the legacy agent appends that file to the system message when it is non-empty ([WebArena run](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/run.py), [legacy agent](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/agents/legacy/agent.py)). The mini-SWE-agent runner passes `selected_memory` into `DefaultAgent.run`, which appends it to the system template before the first user task message ([SWE runner](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/third_party/src/minisweagent/run/extra/swebench.py), [default agent](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/third_party/src/minisweagent/agents/default.py)).

**Context efficiency is a cheap precedent budget.** ReasoningBank avoids loading the whole bank by selecting one prior task's memory items. That controls volume at the task-record level, but complexity is still weakly governed: a selected record can contain multiple Markdown items, the embedding cache grows by appending each current query, and read-back is outside a provenance-aware assembly policy.

**Memory-aware scaling is another induction loop, not a different store.** `pipeline_scaling.py` runs parallel WebArena trials with the same selected-memory text file, then `induce_scaling.py` compares the resulting trajectories and appends synthesized memory items to `memories_scaling/{website}.jsonl` ([scaling pipeline](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/pipeline_scaling.py), [scaling induction](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/induce_scaling.py)). It treats repeated rollouts as better evidence for induction, while preserving the same JSONL memory-bank pattern.

## Artifact analysis

- **Storage substrate:** `files` — WebArena stores memory banks and embedding caches as local JSONL files plus selected-memory text files; mini-SWE-agent stores `./memory/{model}.jsonl` and `./memory/{model}_embeddings.jsonl`; trajectories and evaluation artifacts live in benchmark output directories.
- **Representational form:** `prose` `symbolic` `parametric` — memory items are Markdown/prose lessons, JSONL records and prompts carry symbolic structure, and embedding vectors are distributed-parametric ranking state.
- **Lineage:** `authored` `trace-extracted` — prompts and harness code are authored; memory banks, embedding caches, selected-memory files, and outcome labels are derived from benchmark task configs, trajectories, evaluator outputs, saved messages, and LLM judgments.
- **Behavioral authority:** `knowledge` `instruction` `validation` `ranking` `learning` — stored memories and raw trajectories are evidence; injected memory text becomes system-message advice; benchmark evaluators and LLM judges label traces; embeddings rank read-back; induction prompts create learned memory.

**Reasoning memory JSONL records.** The central retained artifact is a JSONL record containing task id, query/problem statement, success/failure status, and generated memory items. WebArena records can also preserve think/action lists and template ids. The record is trace-extracted from benchmark execution, but at rest it is a knowledge artifact until selected and injected into a later prompt.

**Embedding cache JSONL.** The cache stores task ids, query text, and embedding vectors. It is a derived access structure over prior task statements, not over the memory prose itself. It has ranking authority because similarity order decides which memory record can be read back, and it is also a side-effect log because every retrieval appends the current task embedding.

**Extraction prompts and judges.** Success/failure prompts define what a retained lesson should look like, while WebArena autoeval/ground-truth reward and mini-SWE-agent's LLM judge decide which prompt branch runs. These are system-definition artifacts for learning and validation; they decide which trace gets summarized as success advice or failure-prevention advice.

**Selected-memory handoff.** WebArena materializes selected memory in a transient text file; mini-SWE-agent keeps it as a string argument. The handoff is prose derived from the JSONL bank by embedding retrieval. Its authority changes at consumption time, because the receiving agent sees it in the system message with an instruction to explicitly discuss whether to use each memory item.

Promotion path: raw benchmark trace -> success/failure label -> LLM-generated memory items -> JSONL memory bank -> embedding-selected memory text -> system-message advice. The system crosses from trace evidence into prompt-level behavioral context, but it does not promote memories into reviewed rules, executable tools, validators, or typed artifacts.

## Comparison with Our System

| Dimension | ReasoningBank | Commonplace |
|---|---|---|
| Primary purpose | Improve benchmark agents through trajectory-derived reasoning memory | Maintain a typed methodology KB for future agents and maintainers |
| Main retained unit | JSONL memory item with prose lessons and task metadata | Git-tracked Markdown artifacts with frontmatter, type specs, links, and validation |
| Learning source | WebArena and SWE-Bench trajectories plus success/failure signals | Source-grounded writing, review, validation, and workshop-to-library promotion |
| Read-back | Embedding-selected top-1 prior task injected into the agent prompt | Mostly deliberate pull through search, indexes, links, skills, and review gates |
| Governance | Prompt constraints, benchmark evaluator, LLM judge, embedding ranker | Collection contracts, schemas, deterministic validation, semantic review, git history |

ReasoningBank is closer to Commonplace's workshop layer than to its library layer. It captures runs, distills compact lessons, and immediately makes them eligible to shape later runs. Commonplace uses a slower path: a run may produce a report or note candidate, but durable methodology gains authority through type contracts, validation, review, and explicit links.

The useful divergence is authority speed. ReasoningBank lets one benchmark result influence the next task after automatic induction. That is attractive for adaptation, but the selected memory text does not carry source trajectory ids, model versions, evaluator confidence, reviewer state, expiry, or prompt version into the receiving context.

ReasoningBank also makes the activation boundary concrete. Stored JSONL memory is inert until the harness selects it; after injection it becomes system-message advice. That gives Commonplace a useful benchmark case for separating storage, ranking, and effective authority at consumption time.

### Borrowable Ideas

**Treat failed runs as extraction sources.** Commonplace could summarize failed validation, review, or migration runs into compact preventive lessons before deciding whether any lesson deserves promotion to an instruction. Ready as a workshop/report convention; not ready for automatic high-authority promotion.

**Bind induction to an outcome oracle.** ReasoningBank waits for reward, autoeval, or an LLM judge before generating memory. Commonplace could require explicit outcome labels before producing candidate lessons from automation runs. Ready as a governance rule when the oracle is auditable.

**Use one retrieved precedent as the baseline context budget.** A top-1 prior task is a cheap default worth testing for review or fix workflows before designing richer retrieval. Needs source and freshness metadata before becoming default behavior.

**Keep raw traces and distilled lessons separate.** ReasoningBank keeps result directories and induced memory records distinct. Commonplace should preserve the same split: raw logs remain evidence, while distilled notes or rules gain behavior-shaping authority only after review.

**Ask the model to discuss memory use.** The prompt tells agents to explicitly decide whether to use each injected memory item. Ready as an instruction pattern for injected context, but it still needs audit checks before being treated as evidence of actual use.

## Write side

**Write agency:** `automatic` `manual` — The benchmark pipelines automatically append memory and embedding-cache records after task runs; operators manually configure memory mode, memory paths, model, judge, website/task slices, and scaling parameters.

**Curation operations:** `promote` — A benchmark trace gains stronger future-action authority when evaluator or judge output routes it through a memory-induction prompt and the generated lesson is appended to the retained memory bank.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `trajectories` — WebArena consumes step pickle files, thoughts, actions, task configs, result directories, and autoeval/ground-truth signals; mini-SWE-agent consumes saved message trajectories, command outputs, model predictions, and an LLM success/failure judgment.

**Learning scope:** `per-task` `cross-task` — Memory is induced after individual benchmark tasks or same-task scaling trials, then reused across later tasks within a website/mode-scoped WebArena bank or model-scoped SWE-Bench bank.

**Learning timing:** `online` `staged` — The ordinary pipeline updates memory after each benchmark instance; the scaling path stages multiple trials before one induction pass.

**Distilled form:** `prose` `symbolic` `parametric` — Distilled lessons are prose/Markdown inside JSONL records, symbolic task/status metadata surrounds them, and embedding vectors support later selection.

Extraction is LLM-mediated and outcome-gated. WebArena chooses the success or failure prompt from reward/autoeval results and can append autoeval thoughts to the trajectory before induction. mini-SWE-agent judges the saved non-system messages with the same model family, then calls success or failure memory prompts.

Survey placement: ReasoningBank belongs in the trace-to-prose-reasoning-memory family. It strengthens the raw/distilled split: trajectories and evaluator outputs are raw evidence, while the JSONL memory item is the retained artifact that later gains prompt authority through embedding-selected injection. It also strengthens the failed-run variant because failure trajectories can produce avoidance strategies, not only successful workflow reuse.

## Read-back

**Read-back:** `both` — The harness performs a pull-style embedding lookup over the retained bank, but the receiving WebArena or mini-SWE-agent agent gets the selected memory pushed into its system context before acting.

**Read-back signal:** `inferred / embedding` — Selection is instance-conditioned by embedding similarity between the current query/problem statement and cached prior task embeddings.

**Faithfulness tested:** `no` — The repository provides the structural wiring and benchmark modes, but I did not find an audit or with/without perturbation proving that the selected memory changed behavior in the intended direction.

**Direction edge cases.** From the harness perspective, `select_memory()` is a retrieval call; from the acting agent's perspective, the memory arrives unsolicited in the system prompt. There is no agent-facing command that lets the WebArena or mini-SWE-agent policy deliberately search the memory bank during the action loop.

**Targeting and signal.** Targeting is instance-level: each configured task run embeds the current WebArena intent or SWE-Bench problem statement, ranks cached prior task embeddings, and selects one matching task id. The signal is inferred embedding similarity rather than an authored task tag or identifier.

**Injection point.** Read-back occurs before model invocation. WebArena writes the selected memory text before the experiment run, then `GenericAgent.get_action()` appends it to the system message on each action call. mini-SWE-agent appends selected memory while constructing the initial system message, before adding the user task message.

**Selection, scope, and complexity.** Selection is top-1 after embedding ranking and task-id mapping. Scope is website/memory-mode for WebArena and model name for SWE-Bench. Volume is bounded to one prior task record, but a record can contain several memory items and there is no code-level token budget, provenance filter, quality score, or stale-memory policy for the selected text.

**Authority at consumption.** The injected memory is advisory prose, but system-message placement and the explicit "discuss whether to use" instruction make it soft system-definition context for the next action loop. The stored JSONL item remains a knowledge artifact until this read-back path gives it behavioral force.

**Other consumers.** Researchers and operators can inspect JSONL memory banks, embedding caches, selected-memory text files, result directories, autoeval logs, SWE-Bench trajectory JSON, and prediction files. Those are evidence/debugging surfaces; the agent-facing authority comes from prompt injection.

## Curiosity Pass

**The root package is a placeholder.** `main.py` prints a greeting; the memory system lives in `WebArena/` and the patched mini-SWE-agent tree ([main](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/main.py), [WebArena run](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/run.py), [SWE-Bench runner](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/third_party/src/minisweagent/run/extra/swebench.py)).

**The README path for prompts is stale.** The README names `WebArena/prompt/`, while this checkout has `WebArena/prompts/` and imports `prompts.memory_instruction` ([README](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/README.md), [induction import](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/induce_memory.py)). The executable scripts are the source of truth.

**The embedding cache is not just an index of accepted memory.** Retrieval appends the current task embedding before scoring against previous cache contents. That makes the cache a growing attempted-task trace, and cached ids can exist before or without a matching retained memory item.

**`use_memory` is not the ReasoningBank path in WebArena.** `run.py` sets BrowserGym's scratchpad-style `use_memory=False` while passing `memory_path`; the legacy agent then appends that file directly to the system message. ReasoningBank's read-back path is selected-memory prompt injection, not BrowserGym's internal memory flag.

**Scaling status labels deserve care.** `induce_memory.py` treats reward `1` as success, while `induce_scaling.py` labels reward `0` as success in the inspected branch. That may reflect different reward semantics, but any borrowed scaling loop should make outcome-label meaning explicit before induction.

## What to Watch

- Whether memory records gain source trajectory ids, model versions, evaluator details, prompt versions, timestamps, and expiry policy; that would make induced memories auditable enough for stronger reuse.
- Whether retrieval moves beyond top-1 task similarity to confidence thresholds, deduplication, diversity, recency, or token budgets; that would change it from cheap precedent injection to governed context assembly.
- Whether selected-memory faithfulness is tested through ablations, perturbations, or post-action audits; that would make the pushed read-back mechanism more trustworthy as a reusable pattern.
- Whether the WebArena and SWE-Bench memory code is factored into a shared library surface; that would clarify which mechanisms are ReasoningBank proper versus benchmark-specific harness edits.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../../trace-derived-learning-techniques-in-related-systems.md) - places: ReasoningBank distills successful and failed benchmark trajectories into prose reasoning memory.
- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: ReasoningBank separates stored JSONL memory from embedding-selected prompt injection.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: JSONL memories, embedding caches, prompts, judges, trajectories, and handoff files carry different forms and authorities.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: raw trajectories, evaluator outputs, stored memory items, and caches are evidence until activated.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: prompts, judges, embedding rankers, and injected memory text configure learning or action.
- [Use trace-derived extraction](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: ReasoningBank extracts reusable lessons from traces after outcome labeling.
