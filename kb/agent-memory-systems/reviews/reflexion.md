---
description: "Reflexion review: benchmark agents turn failed trajectories and test feedback into task-local verbal lessons for later attempts"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# Reflexion

Reflexion, from `noahshinn/reflexion`, is a research codebase for "Language Agents with Verbal Reinforcement Learning." At the reviewed commit, it implements HotPotQA reasoning agents, AlfWorld/WebShop decision-making agents, and programming agents that turn failed attempts, environment histories, and test feedback into short self-reflections injected into later attempts on the same benchmark instance.

**Repository:** https://github.com/noahshinn/reflexion

**Reviewed commit:** [218cf0ef1df84b05ce379dd4a8e47f17766733a0](https://github.com/noahshinn/reflexion/commit/218cf0ef1df84b05ce379dd4a8e47f17766733a0)

**Source directory:** related-systems/reflexion

## Core Ideas

**Memory is verbal repair advice, not retrieved world knowledge.** HotPotQA agents keep `self.reflections` and `self.reflections_str`; when a previous attempt is incorrect, halted, or exhausted, `reflect()` asks a reflection model to diagnose the failed scratchpad and formats the result into the next agent prompt ([hotpotqa agents](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/agents.py), [hotpotqa prompts](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/prompts.py)). The stored artifact is a prose plan for avoiding a repeated failure.

**AlfWorld and WebShop persist task-local memories across trials.** Their `main.py` files initialize each environment config with `memory: []`, optionally resume a prior `env_results_trial_<n>.json`, run a trial, call `update_memory()` when `--use_memory` is set, and write the updated configs back to JSON ([AlfWorld main](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/main.py), [WebShop main](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/webshop_runs/main.py)). Failed environment logs become reflection strings appended to the same environment's memory list ([AlfWorld reflections](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/generate_reflections.py), [WebShop reflections](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/webshop_runs/generate_reflections.py)).

**Programming Reflexion uses tests as the retry oracle.** `run_reflexion()` generates internal tests, runs an implementation, collects test feedback, asks for a self-reflection when the implementation fails, and passes the previous implementation, feedback, and reflection into the next `strategy="reflexion"` generation call ([programming loop](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/programming_runs/reflexion.py), [generator utilities](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/programming_runs/generators/generator_utils.py)). The JSONL result record stores reflections, implementations, test feedback, solution, and solved status.

**Context efficiency comes from same-instance scope and small windows.** HotPotQA uses accumulated reflections for one question; AlfWorld and WebShop pass at most the latest three memory entries into environment history and reflection generation; programming Reflexion carries the latest implementation, feedback, and reflection within the current benchmark item ([AlfWorld trial](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/alfworld_trial.py), [WebShop trial](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/webshop_runs/webshop_trial.py)). There is no global vector store, semantic retrieval layer, or cross-task memory index.

**The benchmark harness, not the acting agent, decides read-back.** Reflections are inserted through prompt formatting: HotPotQA fills `{reflections}`, AlfWorld/WebShop prepend "Your memory for the task below", and programming generation includes `[reflection on previous impl]` or `hint:` before the improved implementation request ([HotPotQA prompts](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/prompts.py), [AlfWorld environment history](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/env_history.py), [WebShop environment history](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/webshop_runs/env_history.py), [generator utilities](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/programming_runs/generators/generator_utils.py)).

## Artifact analysis

- **Storage substrate:** `in-memory` `files` — HotPotQA reflections live in agent object fields during repeated runs; AlfWorld/WebShop persist environment memory in JSON configs and logs; programming runs write JSONL records with reflections, code, feedback, and result status.
- **Representational form:** `prose` `symbolic` — operative memories are prose reflections; JSON configs, JSONL records, benchmark statuses, tests, prompt templates, and implementation strings are symbolic or mixed prompt/program records.
- **Lineage:** `authored` `trace-extracted` — prompt templates, harness code, task configs, and benchmark scripts are authored; retained reflections are derived from failed scratchpads, action-observation histories, generated implementations, and test feedback.
- **Behavioral authority:** `knowledge` `instruction` `validation` `routing` `learning` — logs and result records are audit knowledge; injected reflections advise or instruct the next attempt; exact-match checks, environment success, rewards, exhaustion, and tests validate failure; benchmark instance identity routes memory; reflection generation is the learning step.

**HotPotQA reflection fields.** Reflections live in `CoTAgent` and `ReactReflectAgent` fields and are formatted into the next prompt only after an earlier run failed. The raw scratchpad remains evidence; the distilled prose reflection becomes prompt advice for the same question.

**AlfWorld and WebShop environment configs.** `env_results_trial_<n>.json` is the durable memory surface for these tasks. Each environment config carries `memory`, success state, and, in AlfWorld, skip state. Failed logs are split by environment, converted into a "New plan", appended to that environment's memory, and later included in `EnvironmentHistory` for the same config slot.

**Programming result records.** The programming loop keeps reflections and feedback in process for the current item and writes them into JSONL after the item completes. During the loop, the reflection has instruction authority over the next code generation; after logging, the same record is mostly audit knowledge unless another run or evaluator consumes it.

**Prompt templates and benchmark scripts.** The templates and runners are system-definition artifacts: they define when a failure counts, what history is shown to the reflection model, how many memories are shown, and where the reflection appears in the next model call.

Promotion path: failed trace or failed implementation -> LLM-generated prose reflection -> same-instance prompt context for another attempt -> optional JSON/JSONL/log record. Reflexion does not promote lessons into reusable cross-task notes, tools, validators, embeddings, or model weights at this commit.

## Comparison with Our System

| Dimension | Reflexion | Commonplace |
|---|---|---|
| Primary purpose | Improve repeated benchmark attempts through verbal self-reflection | Maintain a git-native methodology KB for agents and maintainers |
| Canonical substrate | Runtime fields, environment JSON, trial logs, programming JSONL | Typed Markdown artifacts, snapshots, validators, indexes, review runs |
| Memory unit | Short failure-derived plan or hint | Source-grounded note, review, instruction, ADR, or generated index |
| Learning trigger | Incorrect answer, halted trajectory, failed environment, failed tests | Authored capture, ingest, review, validation, connection, deliberate promotion |
| Read-back | Harness-injected same-instance reflection | Mostly deliberate pull through search/indexes/links/skills, with instructions and validators as stronger control |
| Trust model | Benchmark oracle and repeated attempt | Source grounding, type contracts, validation, semantic review, git history |

Reflexion is narrower than Commonplace but sharper about behavioral timing. It does not ask a future agent to search for a lesson; the harness inserts a task-local reflection just before another attempt on the same instance. Commonplace usually preserves richer provenance and review state, but its ordinary knowledge artifacts often rely on agents to retrieve them deliberately.

The authority tradeoff is scope. Reflexion can automatically create and re-use a reflection because the retry target and oracle are tight: same question, same environment slot, same programming item, exact answer/success/test feedback. Commonplace's methodology notes usually operate under weaker evidence and broader reuse, so an analogous automatic write should enter a workshop or review queue before becoming durable instruction.

### Borrowable Ideas

**Generate lessons immediately after bounded failure.** Ready for workshops. Validation failures, failed tests, and repeated review warnings can produce candidate lessons while the trace is fresh, but those candidates should stay below library authority until reviewed.

**Keep raw trace and distilled lesson separate.** Ready now as review vocabulary. Reflexion's logs and scratchpads remain evidence; reflections are the behavior-shaping distilled artifacts.

**Use same-instance identity before semantic retrieval.** Ready for narrow retry loops. When a task has a stable issue id, file path, benchmark item, or review run id, use that identifier before considering broad relevance search.

**Cap retry memory aggressively.** Ready now. The last-three cap is crude, but it prevents repeated-attempt context from becoming a growing transcript dump.

**Treat strong tests as local promotion oracles only.** Ready with constraints. Unit tests and deterministic validation can nominate stronger lessons than vague self-reflection, but their authority should remain scoped to the failure class they actually tested.

## Write side

**Write agency:** `automatic` `manual` — Reflections are generated automatically from failed attempts and test feedback when the benchmark strategy or `--use_memory` path enables them; operators manually select run parameters, reflection strategy, resume directories, and benchmark scripts.

**Curation operations:** `promote` — A failed trace or failed implementation gains stronger future-action authority when the benchmark harness turns it into a retained prose reflection for a later attempt on the same instance.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `trajectories` — HotPotQA scratchpads, AlfWorld/WebShop action-observation logs, programming implementations, test feedback, and benchmark success/failure states provide the raw signal.

**Learning scope:** `per-task` — Each reflection is scoped to the same question, environment config slot, or programming item rather than to a project or cross-task library.

**Learning timing:** `staged` — Reflexion attempts, evaluates, reflects on failure, inserts the reflection, and retries.

**Distilled form:** `prose` — The durable behavior-shaping unit is a verbal plan, diagnosis, hint, or self-reflection.

Extraction is LLM-mediated and oracle-gated. HotPotQA reflects only after an incorrect, halted, or failed run. AlfWorld/WebShop update memory only for unsolved environments. Programming Reflexion asks for self-reflection after internal tests fail and then evaluates improved code against tests. The code does not attach exact source spans or formal proof of reflection truth; it relies on tight retry scope and benchmark feedback.

Survey placement: Reflexion is the canonical trace-to-prose-advice example. It strengthens the survey distinction between raw traces as evidence and distilled lessons as behavior-shaping memory. It is not trace-to-vector, trace-to-graph, trace-to-tool, or trace-to-weights at this commit.

## Read-back

**Read-back:** `push` — The harness inserts retained reflections into later prompts for the same benchmark instance; the acting agent does not choose to search or call a memory tool.

**Read-back signal:** `identifier` — Reflection selection keys on the same question, environment config index, trial slot, programming item, or current implementation chain.

**Faithfulness tested:** `yes` — The repository includes baseline/reflection strategy switches, shipped run logs, and benchmark success/test loops that compare behavior with and without memory at aggregate run level; per-reflection causal attribution is not verified.

**Direction edge cases.** HotPotQA can use the last attempt trace, a generated reflection, or both, but all are inserted by the agent class before the next run. AlfWorld/WebShop expose `--use_memory`; when enabled, the runner decides whether memory reaches the environment history. Programming Reflexion similarly passes self-reflection through generator arguments rather than through an agent-initiated lookup.

**Targeting and signal.** Targeting is same-instance rather than semantic. The selected reflection is associated with the same question, same environment config slot, or same programming item. AlfWorld/WebShop also apply a latest-three window before prompt assembly.

**Injection point.** Read-back is pre-invocation: reflections are assembled into the prompt before the next reasoning/action loop or code generation call. Reflection generation after a failed run is write-side learning, not a second read.

**Selection, scope, and complexity.** Scope is intentionally narrow and context volume is low: accumulated HotPotQA reflections, latest three environment memories, or one current programming reflection plus code/test feedback. Complexity remains manageable because memories are short prose plans, not retrieval bundles. The code does not measure prompt dilution or whether the model actually follows each reflection.

**Authority at consumption.** Reflections are advisory prose placed in structurally privileged prompt positions: the templates tell the model to use them to improve strategy, remember prior plans, or write an improved implementation. They are not hard gates, but they have stronger authority than a note sitting in a store because the harness guarantees prompt presence.

**Other consumers.** Humans and evaluators can inspect trial logs, environment JSON, HotPotQA examples, and programming JSONL. Those are audit/reporting consumers, not separate agent read-back paths.

## Curiosity Pass

**The strongest mechanism is the narrowest one.** Same-instance retry makes relevance nearly trivial. That is much easier than open-ended agent memory, where the current task rarely carries an exact prior-attempt identity.

**The implementation is benchmark-local rather than library-shaped.** HotPotQA, AlfWorld, WebShop, and programming tasks each implement their own reflection loop. There is no shared memory API, provenance model, lifecycle policy, or retrieval layer.

**Reflection authority is higher than reflection governance.** A generated plan can be wrong, stale, or overfit, yet the next prompt tells the model to use it. Reflexion controls that risk mostly through short scope and repeated evaluation.

**The memory cap is a context-design decision.** Latest-three environment memories are enough for retry guidance; if more history is needed, the system probably needs consolidation or a different artifact, not unbounded prompt growth.

## What to Watch

- Whether future Reflexion-style systems retain source pointers from each reflection to exact trace segments, actions, observations, or failing tests.
- Whether reflections gain update, merge, or retirement policies rather than append-only bounded lists.
- Whether same-instance reflections become cross-task lesson libraries; that would change the relevance and governance problem.
- Whether per-reflection ablations appear, showing which inserted lesson changed a later action rather than only aggregate success.
- Whether recurring prose lessons are promoted into symbolic tests, policies, or tools with stronger authority and clearer validation.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Reflexion turns failed trajectories and test feedback into task-local verbal advice for later attempts.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: failed attempts are distilled into reusable but scoped memory artifacts.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: Reflexion's reflections matter because the harness inserts them before retry, not because they are merely logged.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: raw traces, prose reflections, JSON records, prompt templates, and tests carry different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: logs and result records provide evidence and audit context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompt templates, benchmark oracles, and injection code shape future behavior.
