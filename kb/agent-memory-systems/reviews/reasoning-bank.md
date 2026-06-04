---
description: "ReasoningBank review: trace-derived reasoning memories for WebArena and SWE-Bench with embedding-selected prompt injection and scaling loops"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# ReasoningBank

ReasoningBank, from Google Research's `google-research/reasoning-bank` repository, is a research codebase for making WebArena and SWE-Bench agents reuse reasoning extracted from prior successful and failed trajectories. The implementation is not a general-purpose memory server; it is a pair of benchmark-integrated loops that write JSONL memory banks, maintain embedding caches, retrieve one related prior task by similarity, and inject the selected memory text into the next agent run.

**Repository:** https://github.com/google-research/reasoning-bank

**Reviewed commit:** [ed80611788292ea739f1effd31f16c53823b8a0d](https://github.com/google-research/reasoning-bank/commit/ed80611788292ea739f1effd31f16c53823b8a0d)

**Last checked:** 2026-06-02

## Core Ideas

**Reasoning memory is induced from benchmark trajectories, not authored as a separate KB.** WebArena's `pipeline_memory.py` runs a task, evaluates the trajectory, and then calls `induce_memory.py` to append memory items to a website-scoped JSONL file ([WebArena/pipeline_memory.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/pipeline_memory.py), [WebArena/induce_memory.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/induce_memory.py)). The SWE-Bench path performs the same pattern inside the patched mini-SWE-agent batch runner: load prior memory, run the instance, save the trajectory, judge success, and append new memory items ([third_party/src/minisweagent/run/extra/swebench.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/third_party/src/minisweagent/run/extra/swebench.py)).

**The memory item is a distilled reasoning lesson.** WebArena prompts separately handle successful and failed trajectories, asking for at most three Markdown memory items with a title, description, and concise content; the scaling path can compare multiple trajectories and extract up to five items ([WebArena/prompts/memory_instruction.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/prompts/memory_instruction.py), [WebArena/induce_scaling.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/induce_scaling.py)). SWE-Bench uses analogous coding-task prompts under `third_party/src/minisweagent/memory/instruction.py` and writes the generated memory list into `./memory/{model}.jsonl` ([third_party/src/minisweagent/memory/instruction.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/third_party/src/minisweagent/memory/instruction.py), [third_party/src/minisweagent/run/extra/swebench.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/third_party/src/minisweagent/run/extra/swebench.py)).

**Retrieval is embedding similarity over prior task queries.** Both WebArena and SWE-Bench load a JSONL embedding cache, embed the current query or problem statement with Gemini or Qwen, score the instruction-aware query against cached embeddings, and return the top memory-bank entry whose `task_id` matches the selected cached id ([WebArena/memory_management.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/memory_management.py), [third_party/src/minisweagent/memory/memory_management.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/third_party/src/minisweagent/memory/memory_management.py)). The default runtime selects `n=1`; there is no diversity policy, confidence threshold, memory-level token budget, or quality score on the selected memory.

**Read-back is engineered prompt injection.** WebArena's `run.py` materializes the selected memory items into a plain text file, then the legacy agent reads that file and appends the memory text to the system message with an instruction to discuss whether to use each memory item before acting ([WebArena/run.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/run.py), [WebArena/agents/legacy/agent.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/agents/legacy/agent.py)). The SWE-Bench agent receives the selected memory as an extra system-message suffix in `DefaultAgent.run` ([third_party/src/minisweagent/agents/default.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/third_party/src/minisweagent/agents/default.py)).

**Context efficiency is mostly top-1 selection, not governed context assembly.** The system avoids loading the whole bank by selecting one prior task's memory items, which is the main volume control. Complexity control is weaker: the selected task may contribute multiple Markdown memory items, the system prompt injection is outside WebArena's prompt-shrinking path, and the cache appends current query embeddings without pruning or deduplication ([WebArena/run.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/run.py), [WebArena/agents/legacy/dynamic_prompting.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/agents/legacy/dynamic_prompting.py), [WebArena/memory_management.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/memory_management.py)).

**Memory-aware scaling is a second loop, not a different store.** `pipeline_scaling.py` runs multiple WebArena trials against the same memory path, then `induce_scaling.py` compares trajectories for one task and writes a synthesized memory item to `memories_scaling/{website}.jsonl` ([WebArena/pipeline_scaling.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/pipeline_scaling.py), [WebArena/induce_scaling.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/induce_scaling.py)). It treats repeated rollouts as better evidence for memory induction, but the retained artifact remains the same JSONL memory format.

## Artifact analysis

- **Storage substrate:** `files` — WebArena writes website- and mode-scoped JSONL files such as `memories_reasoningbank/{website}.jsonl`, `memories_awm/{website}.jsonl`, `memories_synapse/{website}.jsonl`, and `memories_scaling/{website}.jsonl`; SWE-Bench writes `./memory/{model}.jsonl` under the mini-SWE-agent working tree
- **Representational form:** `prose` `symbolic` `parametric` — prose or Markdown memory items, symbolic JSON wrappers/metadata/prompts/judges, and distributed-parametric embedding vectors in the cache
- **Lineage:** `authored` `trace-extracted` — authored extraction prompts and benchmark harness code derive memory banks, embedding caches, and selected-memory handoffs from benchmark trajectories and evaluator/judge outcomes
- **Behavioral authority:** `knowledge` `instruction` `validation` `ranking` `learning` — stored memories and raw trajectories are evidence; prompt suffixes instruct the receiving agent; evaluators/judges label traces; embeddings rank read-back; extraction prompts create learned memory

**Reasoning memory JSONL records.** Storage substrate: WebArena writes website- and mode-scoped JSONL files such as `memories_reasoningbank/{website}.jsonl`, `memories_awm/{website}.jsonl`, `memories_synapse/{website}.jsonl`, and `memories_scaling/{website}.jsonl`; SWE-Bench writes `./memory/{model}.jsonl` under the mini-SWE-agent working tree. Representational form: mixed symbolic JSON wrapper plus prose or Markdown memory items; WebArena records also preserve query, task id, template id, status, and sometimes raw `think_list` and `action_list`. Lineage: trace-derived from benchmark result directories, step pickle files or trajectory JSON, task configs, auto-evaluation or LLM judge outcomes, and an LLM extraction prompt; the JSONL line is a distilled view, not the raw trace. Behavioral authority: knowledge artifact when inspected as evidence of prior experience; system-definition artifact when retrieved and injected into a later agent's system context as advice that can change the next action.

**Embedding cache JSONL.** Storage substrate: JSONL files such as `memories_reasoningbank/{website}_embeddings.jsonl` and `./memory/{model}_embeddings.jsonl`. Representational form: symbolic ids and text fields plus distributed-parametric embedding vectors. Lineage: generated online from task queries or problem statements by Gemini or Qwen embedding calls; each retrieval appends the current task embedding after loading the existing cache. Behavioral authority: ranking system-definition artifact because it decides which memory record is selected for read-back. The cache is not a canonical explanatory source; it is a derived selection index that can drift from the memory bank if ids are missing, duplicated, or stale.

**Extraction prompts and success/failure judges.** Storage substrate: Python prompt constants and evaluator scripts in `WebArena/prompts/`, `WebArena/autoeval/`, `WebArena/utils/`, and `third_party/src/minisweagent/memory/`. Representational form: prose instructions with symbolic output-format contracts. Lineage: authored framework code, with result labels derived from WebArena ground-truth or autoeval JSON and SWE-Bench's LLM status judge. Behavioral authority: system-definition artifacts for learning because they decide which trace lessons become retained memory and whether a trajectory is treated as success or failure. There is no separate review gate for whether a generated memory item is true or sufficiently general.

**Selected-memory handoff files and system-message suffixes.** Storage substrate: WebArena writes a transient `{website}.txt` memory file before the run; SWE-Bench keeps selected memory in a string passed to `agent.run`. Representational form: prose memory items concatenated with blank lines. Lineage: derived from the JSONL memory bank by embedding retrieval over the current query. Behavioral authority: system-definition context at consumption time, because the text is appended to the receiving agent's system message with an instruction to consider it before acting. Effective use by the model is not verified from code.

**Raw trajectories and evaluation artifacts.** Storage substrate: WebArena result directories with `step_*.pkl.gz`, logs, summary and autoeval JSON; SWE-Bench output directories with trajectory JSON, logs, and prediction files. Representational form: mixed messages, observations, actions, scores, judge thoughts, and model outputs. Lineage: generated by benchmark runs and environment/evaluator code. Behavioral authority: knowledge artifacts and learning inputs until `induce_memory.py`, `induce_scaling.py`, or the SWE-Bench runner distills them; they do not directly affect future actions except through the generated memory bank.

The promotion path is raw benchmark trace -> success/failure label -> LLM-distilled reasoning memory -> embedding-selected prompt advice. It crosses from trace evidence into prose system context, but it does not promote into a typed rule, validator, executable skill, or reviewed artifact.

## Comparison with Our System

| Dimension | ReasoningBank | Commonplace |
|---|---|---|
| Primary purpose | Improve benchmark agents through trajectory-derived reasoning memories | Maintain a typed methodology KB for future agents and maintainers |
| Main retained unit | JSONL memory item with prose lessons and task metadata | Git-tracked Markdown artifacts with frontmatter, type specs, links, and validation |
| Learning source | WebArena and SWE-Bench trajectories, success/failure signals, LLM extraction | Source-grounded writing, review, validation, and workshop-to-library promotion |
| Retrieval/read-back | Embedding-selected top-1 prior task, pushed into system context | Mostly pull through search/indexes/links, with explicit instructions and generated context where configured |
| Governance | Prompt constraints, benchmark evaluator, LLM judge, embedding ranker | Collection contracts, schemas, deterministic validation, semantic review, git history |
| Durability | Local JSONL and embedding files under run directories | Repository artifacts with explicit lifecycle and review state |

ReasoningBank is closer to Commonplace's workshop layer than to its library layer. It captures a run, distills the useful lesson, and immediately makes that lesson eligible to shape future runs. Commonplace uses a slower and more inspectable path: a run may produce a report or note candidate, but the durable artifact gains authority through type contracts, validation, review, and explicit links.

The useful divergence is authority speed. ReasoningBank is optimized for benchmark adaptation: after one task finishes, its memory can influence the next task. That is operationally attractive, but the induced memory has weak lineage once read back: the prompt text does not carry source trajectory ids, model version, evaluator confidence, reviewer state, or expiry policy into the agent context. Commonplace spends more overhead on provenance because its artifacts are meant to accumulate rather than optimize a benchmark sequence.

ReasoningBank also makes the read-back boundary unusually explicit. The selected memory is not just returned to a caller; the harness writes it into the agent's system context. That makes it a clear case where a knowledge-looking artifact becomes system-definition context at consumption time.

**Read-back:** `both` — Operators configure or omit the memory path, but from the receiving agent's perspective the implemented memory path is embedding-gated push: one selected prior memory is inserted into the system context before the next WebArena or SWE-Bench action loop

### Borrowable Ideas

**Treat failed runs as first-class extraction sources.** ReasoningBank has separate success and failure prompts and can derive preventive advice from failed trajectories. A Commonplace analogue would make failed validation, review, or migration runs eligible for compact lessons before deciding whether to promote them to instructions. Ready as a workshop/report convention; not ready for automatic instruction promotion.

**Preserve the raw-to-distilled split in run reports.** The code keeps raw trajectories and induced memory as different artifacts. Commonplace should keep the same separation when summarizing agent runs: raw logs remain evidence, while a distilled note or rule carries behavior-shaping authority only after review. Ready now as a review-writing discipline.

**Use top-1 retrieved precedent as a cheap baseline for agent context.** ReasoningBank's simplest context budget is "one similar prior task." Commonplace could test the same baseline for review bundles or fix workflows before designing richer retrieval. Ready for experiments; it needs explicit source and freshness metadata before becoming a default.

**Bind memory induction to an outcome oracle.** ReasoningBank waits for reward, autoeval, or an LLM judge before generating memory. Commonplace could require an explicit outcome label before producing candidate lessons from automation runs. Ready as a governance rule; the oracle must be auditable for high-authority artifacts.

**Make memory use discussable in the prompt.** The receiving agents are told to discuss whether to use each memory item before acting. Commonplace could borrow that as a faithfulness aid in workflows that inject retrieved notes: ask the agent to name which retrieved item it used and why. Ready as an instruction pattern, but still needs an audit check to verify actual use.

## Trace-derived learning placement

**Trace source:** `session-logs` `tool-traces` `trajectories` — WebArena and SWE-Bench consume logs/messages, action traces, and benchmark trajectories from prior runs

**Learning scope:** `per-task` `cross-task` — memory is induced after individual tasks or same-task scaling trials, then reused across later benchmark tasks within website/mode or model-scoped banks

**Learning timing:** `online` `staged` — the pipeline updates memory after each benchmark task, while the scaling path distills after a staged set of parallel trials

**Distilled form:** `prose` `symbolic` `parametric` — distilled lessons are prose/Markdown in JSONL records, with symbolic metadata and embedding vectors used for selection

**Trace source.** ReasoningBank qualifies as trace-derived learning in both benchmark paths. WebArena consumes result directories containing task configs, step pickle files, action/reasoning traces, summary rewards, and autoeval outputs. SWE-Bench consumes mini-SWE-agent trajectory JSON messages, model outputs, and an LLM success/failure judgment.

**Extraction.** WebArena extracts `think` and `action` sequences, prepends the task query, adds success/failure evidence, and calls a model with success, failure, AWM, Synapse, or parallel-scaling prompts. SWE-Bench joins non-system trajectory messages, asks an LLM judge whether the task succeeded, and then calls success or failure memory prompts. The extraction oracle is therefore split: benchmark/evaluator result first, LLM summarizer second.

**Scope and timing.** WebArena memory is scoped by website and memory mode, then updated after each task in `pipeline_memory.py`; the scaling path updates after a set of parallel trials for the same task. SWE-Bench memory is scoped by model name and updated inside each batch instance's `finally` block after trajectory saving. The loop is online across a benchmark sequence, not a background miner over an arbitrary agent-history corpus.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), ReasoningBank belongs in the trace-to-prose-reasoning-memory family. It strengthens the survey's raw/distilled split: trajectories and evaluation artifacts are raw evidence, while the JSONL memory item is the behavior-shaping retained artifact. It also adds a clear negative-example variant because failed trajectories can produce future avoidance strategies, not just successful workflow reuse.

## Read-back placement

**Direction.** ReasoningBank uses both pull and push over retained memory. The harness performs a pull-style embedding lookup over the memory bank, but the selected memory is pushed into the WebArena or SWE-Bench agent before the agent chooses actions.

**Read-back signal:** `inferred / embedding` — the pushed memory is selected by embedding similarity between the current query or problem statement and cached prior task embeddings.

**Read-back timing:** `pre-action` — selected memory is written or appended before the WebArena or SWE-Bench action loop starts.

**Faithfulness tested:** `no` — the review found benchmark comparisons but no code-grounded audit that the selected memory changed model behavior faithfully.

**Targeting and signal.** Targeting is `instance`: task start with a configured memory path or benchmark memory mode causes the harness to select a memory for this WebArena task or SWE-Bench instance. The signal is `inferred / embedding`: relevance is derived from embedding similarity between the current query or problem statement and cached prior task embeddings, with an instruction-aware query embedding used for scoring. The deployed code requests one memory entry. Precision, recall, and context dilution are runtime properties not verified by the code.

**Timing relative to action.** Read-back happens before the action loop: WebArena writes the selected memory file before constructing `ExpArgs`, and the legacy agent appends the file content to the system message on every `get_action` call; SWE-Bench appends selected memory before adding the first user task message.

**Selection, scope, and complexity.** Selection is top-1 after embedding ranking, then mapped back by task id. Scope is website/memory-mode for WebArena and model-name for SWE-Bench. Volume is bounded by one prior task record, but the memory record can contain several memory items and there is no token budget or schema-aware trimming for the selected memory text.

**Authority at consumption.** The injected memory is advisory prose, but because it is appended to the system message and paired with an instruction to explicitly discuss whether to use it, it has soft system-definition authority over the receiving agent's next actions. The memory item itself remains a knowledge artifact when stored in JSONL.

**Faithfulness.** I did not find a WITH/WITHOUT ablation or perturbation test that verifies a selected memory item changed behavior in the intended direction. The benchmark harness can compare memory modes and scaling conditions, but the inspected code does not audit whether the model actually used the injected memory faithfully.

**Other consumers.** Human researchers can inspect JSONL memory banks, embedding caches, result directories, autoeval logs, and SWE-Bench prediction files. Those consumer surfaces are evidence and debugging aids; the agent-facing authority comes from the prompt injection path.

## Curiosity Pass

**The root package is a placeholder; the real system lives in benchmark scripts.** `main.py` prints a greeting, while the implemented memory architecture is in `WebArena/` and the patched mini-SWE-agent tree ([main.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/main.py), [WebArena/run.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/run.py), [third_party/src/minisweagent/run/extra/swebench.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/third_party/src/minisweagent/run/extra/swebench.py)).

**The README describes `WebArena/prompt/`, but the checkout has `WebArena/prompts/`.** The code imports `prompts.memory_instruction`, and there is no `WebArena/prompt/` directory in this commit ([README.md](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/README.md), [WebArena/induce_memory.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/induce_memory.py)). That is minor for use, but it reinforces that the executable scripts are the source of truth.

**The embedding cache is also a trace artifact.** `screening` appends the current task's query embedding while retrieving. That means the cache is not only an index of accepted memories; it is also a log of attempted tasks, and some cached ids may not yet or ever have matching memory-bank entries.

**`use_memory` and `memory_path` are different mechanisms in WebArena.** `run.py` sets `use_memory=False` but still passes `memory_path`; the legacy agent then appends the selected memory file directly to the system message. The older dynamic-prompt `<memory>` field is not the ReasoningBank read-back path in this commit ([WebArena/run.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/run.py), [WebArena/agents/legacy/dynamic_prompting.py](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/agents/legacy/dynamic_prompting.py)).

**The scaling induction status check deserves audit.** `induce_memory.py` treats reward `1` as success, while `induce_scaling.py` labels reward `0` as success in the inspected branch. That may reflect different reward semantics, but it is surprising enough that any borrowed scaling loop should make outcome labels explicit before memory induction.

## What to Watch

- Whether memory records gain source trajectory ids, model versions, evaluator details, timestamps, and prompt versions; that would make induced memories auditable enough for higher-authority reuse.
- Whether retrieval moves beyond top-1 task similarity to confidence thresholds, deduplication, diversity, recency, or token budgets; that would change the design from cheap precedent injection to governed context assembly.
- Whether selected-memory faithfulness is tested through ablations or post-action audits; that would make the push-activation mechanism more trustworthy as a reusable pattern.
- Whether the WebArena and SWE-Bench memory code is factored into a shared library surface; that would clarify which parts are ReasoningBank proper versus benchmark-specific harness changes.
- Whether memory-aware scaling uses multiple rollouts to produce reviewed or scored memory candidates instead of immediately appending prompt-generated items; that would move the loop closer to Commonplace-style promotion.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - compares: ReasoningBank distills benchmark trajectories into prose reasoning memories and uses embedding-gated prompt injection for reuse.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: ReasoningBank requires separating raw trajectories, JSONL memories, embedding caches, extraction prompts, and selected-memory handoffs by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: raw trajectories, evaluator outputs, and stored memory items are evidence until a read-back path gives them behavior-shaping force.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: embedding caches, extraction prompts, evaluator labels, and selected-memory prompt injection configure learning or action.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: ReasoningBank's main contribution is extracting compact reusable lessons from successful and failed traces.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: ReasoningBank pairs storage with an explicit relevance-gated activation path, while unmatched JSONL memories remain inert.
