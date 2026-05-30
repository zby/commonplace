---
description: "Benchmark trace-to-memory system that extracts reasoning items from WebArena and SWE-Bench trajectories, retrieves by task-query embeddings, and reinjects selected items into prompts"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# ReasoningBank

ReasoningBank is the Google Research code release for *ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory*. It implements a benchmark trace-to-memory loop for WebArena and SWE-Bench: run an agent, evaluate whether the trajectory succeeded, extract structured reasoning memories from successful or failed trajectories, append them to a JSONL memory bank, retrieve a small number of prior memories by embedding similarity over task queries, and inject the selected memory text into future agent prompts. The system is best read as an experience-memory benchmark harness, not as a general long-term memory product.

**Repository:** https://github.com/google-research/reasoning-bank

**Reviewed revision:** [ea65efd240f833b17b5cdd22df77d546527c82dd](https://github.com/google-research/reasoning-bank/commit/ea65efd240f833b17b5cdd22df77d546527c82dd)

## Core Ideas

**The main loop is run, evaluate, extract.** WebArena's `pipeline_memory.py` enumerates benchmark config files, runs `run.py` with an optional `--memory_path`, evaluates the finished result directory with `autoeval.evaluate_trajectory`, then calls `induce_memory.py` to append extracted items to `memories_{memory_mode}/{website}.jsonl` ([`WebArena/pipeline_memory.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/WebArena/pipeline_memory.py)). SWE-Bench folds the same stages into the mini-swe-agent batch runner: before each instance it retrieves memory, after the run it saves the trajectory and prediction, judges success with an LLM, then appends generated memory to `./memory/{model}.jsonl` ([`third_party/src/minisweagent/run/extra/swebench.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/third_party/src/minisweagent/run/extra/swebench.py)). The lifecycle is benchmark-sequential: memory from prior tasks can affect later tasks, but updates occur between completed runs.

**Memory items are structured prose records, not workflows or weights.** The ReasoningBank prompts ask the model to produce up to three Markdown memory items, each with `Title`, `Description`, and `Content`, from either a successful or failed trajectory ([`WebArena/prompts/memory_instruction.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/WebArena/prompts/memory_instruction.py), [`third_party/src/minisweagent/memory/instruction.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/third_party/src/minisweagent/memory/instruction.py)). WebArena writes a JSONL record containing `task_id`, `query`, `think_list`, `action_list`, `status`, `memory_items`, and `template_id`; SWE-Bench writes `task_id`, `query`, `memory_items`, and `status` ([`WebArena/induce_memory.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/WebArena/induce_memory.py), [`third_party/src/minisweagent/run/extra/swebench.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/third_party/src/minisweagent/run/extra/swebench.py)). The durable operative part is prose advice; embeddings are only a retrieval index over task queries.

**Success and failure have separate extraction prompts.** For successful runs, the extractor asks why the trajectory succeeded and summarizes reusable strategies. For failed runs, it asks why the attempt failed and what preventative lessons should transfer ([`WebArena/prompts/memory_instruction.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/WebArena/prompts/memory_instruction.py)). WebArena can use ground-truth reward or an autoeval file as the correctness signal, and when autoeval is used it appends evaluator thoughts to the extraction input ([`WebArena/induce_memory.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/WebArena/induce_memory.py), [`WebArena/autoeval/evaluate_trajectory.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/WebArena/autoeval/evaluate_trajectory.py)). The WebArena autoeval prompt is deliberately strict about completeness, grounding, and exact target because false successes become future memory ([`WebArena/prompts/autoeval_prompts.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/WebArena/prompts/autoeval_prompts.py)).

**Retrieval matches current task queries against cached prior task queries.** Both WebArena and SWE-Bench load the JSONL memory bank, call `select_memory(n=1, ...)`, and then concatenate the selected record's `memory_items` into prompt text ([`WebArena/run.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/WebArena/run.py), [`third_party/src/minisweagent/run/extra/swebench.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/third_party/src/minisweagent/run/extra/swebench.py)). The retrieval code loads `{website}_embeddings.jsonl` or `{model}_embeddings.jsonl`, embeds the current query, appends that query embedding to the cache, then ranks cached prior query embeddings with cosine similarity; it does not embed the memory-item content itself ([`WebArena/memory_management.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/WebArena/memory_management.py), [`third_party/src/minisweagent/memory/memory_management.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/third_party/src/minisweagent/memory/memory_management.py)). The cache is therefore both an index and a side-effect log of retrieval attempts.

**Prompt injection gives selected memory advisory system-definition force.** In WebArena, `run.py` writes selected memory items into a transient `{website}.txt` file, and the legacy agent appends that file to its system message with an instruction to explicitly decide whether to use each item ([`WebArena/run.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/WebArena/run.py), [`WebArena/agents/legacy/agent.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/WebArena/agents/legacy/agent.py)). SWE-Bench does the same in `DefaultAgent.run`: selected memory is appended to the system message before the issue prompt ([`third_party/src/minisweagent/agents/default.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/third_party/src/minisweagent/agents/default.py)). The phrasing says memories are optional, but placement in the system channel makes them behavior-shaping instructions rather than passive notes.

**The WebArena path includes three memory modes.** `reasoningbank` extracts success/failure memory items with the ReasoningBank prompts. `awm` extracts AWM-style workflows only on successful trajectories. `synapse` stores the successful trajectory itself as the memory item ([`WebArena/induce_memory.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/WebArena/induce_memory.py)). These modes are useful comparison baselines because they change the retained representational form while leaving the runner and retrieval surface mostly the same. At this commit, the non-ReasoningBank modes are less robustly wired for failed trajectories because the write path still expects `generated_memory_item`.

**Scaling mode is a self-contrast extraction sketch with implementation rough edges.** `pipeline_scaling.py` launches several WebArena trials for the same task on different ports, then calls `induce_scaling.py`, whose prompt asks the model to compare multiple trajectories and extract up to five memory items by self-contrast reasoning ([`WebArena/pipeline_scaling.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/WebArena/pipeline_scaling.py), [`WebArena/induce_scaling.py`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/WebArena/induce_scaling.py)). The intended idea is important: memory is another test-time scaling axis, where multiple attempts create contrastive evidence for better memories. The inspected implementation appears experimental: `pipeline_scaling.py` passes only the final `results_{i}` directory into induction after the launch loop, and `induce_scaling.py` repeats that same result directory for `num_samples` rather than loading all trial directories.

**Runtime surfaces are benchmark scripts, not a memory service.** The user-facing tools are shell scripts and Python runners: WebArena's `run.sh`, `pipeline_memory.py`, `pipeline_scaling.py`, `run.py`, and mini-swe-agent's `mini-extra swebench` path ([`README.md`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/README.md), [`SWE-Bench/run.sh`](https://github.com/google-research/reasoning-bank/blob/ea65efd240f833b17b5cdd22df77d546527c82dd/SWE-Bench/run.sh)). The storage substrate is ordinary benchmark directories plus JSONL files, text prompt files, and embedding-cache JSONL files. There is no CRUD API, reviewer UI, schema validator, memory editor, or promotion gate beyond append-on-run.

## Comparison with Our System

| Dimension | ReasoningBank | Commonplace |
|---|---|---|
| Primary source signal | Completed WebArena and SWE-Bench trajectories with success/failure labels | Human and agent-authored notes, source snapshots, reviews, validation output, workshop artifacts |
| Raw trace surface | Result directories, step pickle files, trajectory JSON, evaluator JSON, predictions | Git-tracked markdown, logs, generated reports, source snapshots |
| Distilled artifact | JSONL records containing Markdown memory items | Typed markdown notes, reviews, instructions, ADRs, indexes, skills |
| Storage substrate | Filesystem JSONL and transient prompt `.txt` files; embedding cache JSONL | Git repository with typed files, schemas, generated indexes, review artifacts |
| Representational form | Prose memory items; query embeddings for retrieval | Prose plus symbolic frontmatter, links, type schemas, scripts, validation rules |
| Retrieval | Top-1 similarity over current task query versus cached prior task queries | Lexical search, directory indexes, authored links, skill/instruction loading |
| Behavioral authority | System-channel advisory instruction for the acting benchmark agent | Split advice, instruction, validation, routing, review, and generated-index authority by artifact type |
| Lifecycle | Append-only memory bank; retrieval cache grows by side effect | Status transitions, review, supersession, generated index refresh, git history |
| Evaluation | Benchmark reward, WebArena autoeval, SWE LLM success judge, downstream benchmark scores | Deterministic validation plus semantic review and human judgment |

ReasoningBank is stronger than commonplace on the trace-to-advice loop. It has a concrete mechanism that turns each completed benchmark run into a future prompt-time memory item, including lessons from failure. Commonplace has richer artifact contracts and governance, but it does not yet have an automated loop that mines ordinary agent work traces into candidate instructions or notes after every task.

Commonplace is stronger on retained-artifact discipline. ReasoningBank separates raw trajectories, evaluated results, extracted memory items, retrieval indexes, and prompt-injection files in the filesystem, but the memory records do not carry source run IDs beyond `task_id`, extraction prompt version, evaluator version, confidence, author/reviewer state, supersession links, or invalidation rules. In commonplace terms, the raw trajectories are knowledge artifacts when used as evidence, while selected memory items become system-definition artifacts when injected into the agent's system prompt. ReasoningBank does not encode that authority distinction inside the artifacts themselves.

The main design divergence is activation. ReasoningBank activates memory automatically before every benchmark task with a fixed top-1 retrieval policy. Commonplace usually relies on agent navigation, authored links, and explicit skill/instruction loading. ReasoningBank's activation is cheap and timely, but brittle: if the embedding cache is incomplete, stale, or polluted by current-query side effects, relevant memory will not load; if an irrelevant item wins top-1, it still lands in the system channel.

## Borrowable Ideas

**Mine failures as first-class source traces.** Ready to borrow as a workflow shape. ReasoningBank's separate failed-trajectory prompt captures preventative lessons, not just success recipes. Commonplace could use failed validation runs or abandoned workshop attempts as evidence for candidate instructions, but promotion should remain reviewed.

**Keep raw traces, evaluation, memory records, and prompt views separate.** Ready to borrow. The WebArena path distinguishes result directories, autoeval outputs, JSONL memory banks, embedding caches, and transient prompt files. Commonplace already has analogous surfaces; ReasoningBank is a useful benchmark-grounded reminder that the source trace and the behavior-shaping artifact should not be the same object.

**Use evaluator rationale as extraction context.** Ready to borrow cautiously. WebArena appends autoeval thoughts when extracting memory, so the extractor sees not only what happened but why the judge classified it that way. For commonplace this maps to feeding review findings or validation diagnostics into candidate-note or candidate-instruction drafting.

**Treat query-to-query retrieval as a baseline, not the destination.** Needs a use case before adoption. ReasoningBank shows that even a simple cache of prior task-query embeddings can support benchmark memory activation. For commonplace, embedding search over titles, descriptions, and selected operative sections would likely be more appropriate than matching only prior task statements.

**Borrow self-contrast extraction only after the data plumbing is solid.** The idea of comparing multiple attempts before extracting memory is strong: contrast can reveal what actually mattered. The current scaling scripts are too experimental to copy directly, so the borrowable idea is the prompt/evidence pattern, not the implementation.

**Do not borrow append-only lifecycle for durable methodology.** ReasoningBank's append-only JSONL works for benchmark iteration. A durable KB needs edit, merge, retire, confidence, lineage, and authority controls before extracted memories become instructions.

## Trace-derived learning placement

**Trace source.** ReasoningBank qualifies as trace-derived learning. The raw signals are benchmark task trajectories: WebArena step pickle files, action/thinking traces, observations, screenshots, `summary_info.json`, and autoeval JSON; and SWE-Bench mini-swe-agent message trajectories and patch submissions. Trigger boundaries are one completed benchmark task for sequential memory and multiple intended attempts for scaling mode.

**Extraction.** WebArena extracts `think`/`action` pairs, classifies the run as success or failure by ground-truth reward or autoeval, optionally includes autoeval thoughts, and calls a model with success- or failure-specific system instructions. SWE-Bench joins non-system messages from the saved trajectory, asks an LLM judge whether the task was completed, then uses the same success/failure extraction pattern. Scaling mode intends to compare several trajectories for one task and extract self-contrast memory items.

**Storage substrate.** Raw traces live in benchmark output directories and trajectory files. Evaluated results live in `summary_info.json`, `{model}_autoeval.json`, `preds.json`, and trajectory JSON. Extracted memories live in append-only JSONL files: `memories_{mode}/{website}.jsonl` for WebArena and `./memory/{model}.jsonl` for SWE-Bench. Retrieval state lives in embedding-cache JSONL files. Runtime prompt surfaces are transient `.txt` files for WebArena and in-memory selected strings for SWE-Bench.

**Representational form.** Raw traces are mixed evidence: observations, screenshots, natural-language reasoning, actions, outputs, and scores. Distilled ReasoningBank memory items are prose records with a light Markdown schema. AWM mode stores workflow-like symbolic/prose action snippets; Synapse mode stores raw trajectory text. Query embeddings are distributed-parametric retrieval aids, but they do not replace the prose memory bank and are not learned model weights.

**Lineage.** The derivation chain is procedural rather than artifact-local: task run -> evaluator result or LLM judge -> extraction prompt -> appended JSONL record -> embedding-cache retrieval -> prompt injection. A memory record carries a task id and query, and WebArena carries the original think/action lists, but it does not record the exact source directory, extraction prompt version, model response metadata, evaluator prompt version, cache revision, reviewer, or supersession state. Regeneration is possible by rerunning scripts over saved traces; invalidation is manual.

**Behavioral authority.** Raw trajectories and evaluator outputs are knowledge artifacts because they serve as evidence for extraction and audit. Extracted memory records are knowledge artifacts at rest in JSONL. Once selected and appended to the system prompt, they become advisory system-definition artifacts: the acting agent is instructed to consider them before each step, but there is no enforcement beyond prompt pressure. Embedding caches have ranking influence because they decide which memory receives that authority.

**Scope and timing.** Scope is benchmark-local: website-specific WebArena memory and model-specific SWE-Bench memory. Timing is staged between completed tasks in the normal pipeline, not online within a trajectory. Scaling mode tries to add within-task multi-sample evidence before extraction, but still writes memory after the task attempts complete.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), ReasoningBank is a trajectory-run, readable-artifact learner with bidirectional success/failure extraction. It strengthens the survey's structured-record subtype: the retained artifact is a title/description/content memory item rather than a single reflection string or a full workflow file. It also sharpens the lifecycle-axis contrast because its memory bank is append-only while its retrieval cache is a side-effect index, so activation can evolve without any explicit review of the memory records.

## Curiosity Pass

**The retrieval index is not a memory embedding index.** The code retrieves memories by matching the current task query to prior task queries. This is simpler than embedding each memory item, but it means a useful memory from a dissimilar task statement may be invisible, while a superficially similar query can inject irrelevant advice.

**The cache mutates during lookup.** `screening` appends the current query embedding before returning ranked prior ids, while ranking against the embeddings loaded before the append. This makes the cache an operational trace of retrieval calls, not just a built index. It also means memory-bank records and embedding-cache records can drift unless runs are strictly sequential and never pruned.

**System-channel injection is stronger than the prose suggests.** The prompt says the agent can use memories "when you feel it's relevant," but it appears in the system message and asks the agent to explicitly discuss each item. That is a real behavior-shaping channel even when individual memories are advisory.

**Autoeval is load-bearing.** WebArena's strict evaluator prompt is not just measurement; its status and rationale feed the memory extractor. If the evaluator is wrong, the error is amplified into future system-definition content. The code recognizes this risk in the prompt, but there is no downstream quarantine or reviewer gate.

**The scaling claim is clearer than the scaling code.** Memory-aware test-time scaling is a plausible design direction, and the self-contrast prompt is useful. The inspected orchestration does not yet look like a reliable multi-trajectory evidence pipeline, so the review should treat scaling as an experimental path rather than the same maturity level as sequential ReasoningBank.

**Lifecycle is the central missing subsystem.** There is no merge, deduplication, retirement, source invalidation, confidence update, or negative interaction tracking. The system can accumulate memories and measure benchmark outcomes, but it cannot explain which memory item helped, which one became stale, or which one should stop receiving prompt authority.

## What to Watch

- Whether future versions embed and retrieve over memory-item content, not only task queries.
- Whether memory records gain lineage fields for source run, evaluator, extraction prompt, model, timestamp, confidence, and supersession.
- Whether the scaling path is repaired to actually aggregate multiple distinct trajectories and compare success/failure contrast.
- Whether WebArena and SWE-Bench converge on one shared memory schema and extraction library rather than parallel implementations.
- Whether the system adds memory editing operations, deduplication, or reviewer gates before prompt-time injection.
- Whether benchmark improvements can be attributed to specific memory items rather than to the presence of the retrieval/injection loop as a whole.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - source-inspected instance: ReasoningBank extracts structured memory records from successful and failed benchmark trajectories
- [Designing agent memory systems](../../notes/designing-agent-memory-systems.md) - exemplifies: memory matters because a retained item changes future action, not because it is stored in a particular substrate
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - supports: completed task traces can become reusable advice when extraction and authority are explicit
- [Activate behavior-changing memory](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies: selected memory is useful because it loads before action selection
- [Make authority explicit](../../notes/agent-memory-requirements/make-authority-explicit.md) - contrasts: ReasoningBank gives prompt-time authority to JSONL records without encoding authority or review state in the records
- [Preserve evidence without loading history](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - contrasts: ReasoningBank keeps traces and memory records separate, but weakens provenance inside the retained memory
- [Agent Workflow Memory](./agent-workflow-memory.md) - compares-with: both mine WebArena trajectories, but AWM writes website-scoped workflow files while ReasoningBank appends structured reasoning memory items
- [ExpeL](./expel.md) - contrasts: both learn from success and failure, but ExpeL has explicit memory edit operations while ReasoningBank is append-only
