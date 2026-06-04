---
description: "Reflexion review: benchmark agents that turn failed trajectories and test feedback into verbal self-reflections pushed into later attempts"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# Reflexion

Reflexion, from `noahshinn/reflexion`, is a research codebase for "Language Agents with Verbal Reinforcement Learning." The repository implements benchmark runners for HotPotQA reasoning, AlfWorld and WebShop decision-making, and programming tasks. Its memory mechanism is not a general knowledge base: failed attempts produce short natural-language reflections, and those reflections are fed into later attempts on the same question, environment, or programming item.

**Repository:** https://github.com/noahshinn/reflexion

**Reviewed commit:** [218cf0ef1df84b05ce379dd4a8e47f17766733a0](https://github.com/noahshinn/reflexion/commit/218cf0ef1df84b05ce379dd4a8e47f17766733a0)

**Last checked:** 2026-06-02

## Core Ideas

**Memory is verbal policy advice derived from failure, not retrieved world knowledge.** The central artifact is a reflection such as a concise plan, hint, or diagnosis. In HotPotQA, `ReactReflectAgent.run()` calls `reflect()` only after a previous run halted or finished incorrectly, then formats accumulated reflections into the next prompt ([hotpotqa_runs/agents.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/agents.py), [hotpotqa_runs/prompts.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/prompts.py)).

> The following reflection(s) give a plan to avoid failing to answer the question in the same way you did previously.
> --- [hotpotqa_runs/prompts.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/prompts.py)

**AlfWorld and WebShop persist per-environment reflection memory across trials.** Their `main.py` files initialize `env_configs` with `memory: []`, optionally load prior configs on resume, run a trial, call `update_memory()` after the trial when `--use_memory` is set, then write `env_results_trial_<n>.json` ([alfworld_runs/main.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/main.py), [webshop_runs/main.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/webshop_runs/main.py)). This is the clearest durable memory path in the repository: a failed trajectory log becomes a reflection string in a JSON config, and later trials inject that memory into the task prompt.

**The memory window is deliberately small.** AlfWorld and WebShop include only the last three memories when more than three exist, and their reflection generators likewise pass only the last three prior memories into the next reflection prompt ([alfworld_runs/alfworld_trial.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/alfworld_trial.py), [alfworld_runs/generate_reflections.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/generate_reflections.py), [webshop_runs/webshop_trial.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/webshop_runs/webshop_trial.py), [webshop_runs/generate_reflections.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/webshop_runs/generate_reflections.py)). Context efficiency comes from this task-local cap and from compressing whole trajectories into short prose plans; there is no vector retrieval, semantic deduplication, source ranking, or global memory index.

**Programming Reflexion uses tests as the oracle.** `run_reflexion()` generates internal tests, runs an implementation, asks the generator for a self-reflection from the failed implementation and feedback, then generates the next implementation with the previous code, feedback, and reflection ([programming_runs/reflexion.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/programming_runs/reflexion.py), [programming_runs/generators/generator_utils.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/programming_runs/generators/generator_utils.py)). The log record stores `reflections`, `implementations`, `test_feedback`, `solution`, and `is_solved`, making the trial history inspectable after the run.

**Read-back is pushed by the benchmark harness.** The acting agent does not decide to search a memory store. The runner conditionally includes reflections in the prompt before the next attempt: HotPotQA formats them into `{reflections}`, AlfWorld and WebShop prepend "Your memory for the task below", and programming prompts include `[reflection on previous impl]` before asking for an improved implementation ([hotpotqa_runs/agents.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/agents.py), [alfworld_runs/env_history.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/env_history.py), [webshop_runs/env_history.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/webshop_runs/env_history.py), [programming_runs/generators/generator_utils.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/programming_runs/generators/generator_utils.py)).

**Read-back:** `push` — For the acting agent. Task-local reflections are automatically placed in later prompts by task runners; the agent has no implemented retrieval tool or deliberate memory query path

## Artifact analysis

- **Storage substrate:** `in-memory` — Python object fields `self.reflections` and `self.reflections_str` inside `CoTAgent` and `ReactReflectAgent`
- **Representational form:** `prose` — Prose reflection strings plus formatted prompt text
- **Lineage:** `authored` `trace-extracted` — authored prompt templates/generators shape the loop, while failed traces, logs, and test feedback are distilled into reflections
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `learning` — logs provide audit knowledge; injected reflections and templates instruct; harness placement routes memory; benchmark oracles validate failure; reflection generation is the learning step

**In-process HotPotQA reflections.** Storage substrate: Python object fields `self.reflections` and `self.reflections_str` inside `CoTAgent` and `ReactReflectAgent`. Representational form: prose reflection strings plus formatted prompt text. Lineage: trace-derived from the prior scratchpad when the previous attempt was incorrect, halted, or finished wrong; `LAST_ATTEMPT` can also reuse the whole truncated previous trace as context. Behavioral authority: system-definition-adjacent prompt advice for the next run on the same question, because the reflection header explicitly instructs the model to use the plans to avoid the previous failure. This path is not durable beyond the agent object unless notebooks or logs preserve it.

**AlfWorld and WebShop environment configs.** Storage substrate: run directories containing `env_results_trial_<n>.json` plus `world.log` and `trial_<n>.log`. Representational form: symbolic JSON with `memory`, `is_success`, `skip` in AlfWorld, and per-environment names; the operative memory entries are prose plans. Lineage: failed trial logs are split by environment, parsed into reflection prompts, and appended to `env_configs[i]["memory"]`; resume loads a prior JSON config as the next trial's state. Behavioral authority: high-priority prompt context for later attempts on the same environment when `--use_memory` is set. The reflection entries are knowledge artifacts as evidence of past mistakes, but they become system-definition artifacts when injected under "Your memory for the task below."

**Environment histories and trial logs.** Storage substrate: plain text log files written during AlfWorld and WebShop trials. Representational form: prose/symbolic action-observation transcripts with status summaries. Lineage: raw traces from environment steps, LLM actions, observations, rewards, and failures. Behavioral authority: knowledge artifact authority for audit and for the reflection generator; raw logs do not directly guide the next agent until `update_memory()` distills them into a reflection.

**Programming result JSONL.** Storage substrate: JSONL records written to the configured log path. Representational form: symbolic benchmark records with prose reflections, code strings, test feedback, and pass/fail fields. Lineage: generated from attempted code, internal test results, self-reflection calls, and final evaluation. Behavioral authority: within the running loop, the latest reflection and feedback are prompt instructions for the next implementation; after logging, the JSONL is mostly audit data unless a later resume or analysis consumes it.

**Prompt templates and generators.** Storage substrate: Python source files and few-shot text files. Representational form: mixed prose prompt instructions and symbolic formatting code. Lineage: authored benchmark harness artifacts. Behavioral authority: system-definition artifacts because they decide when reflection is created, how much history is included, which failure oracle is trusted, and where the reflection appears in the next model call.

The promotion path is narrow and benchmark-local: raw trace or test feedback -> generated prose reflection -> next-attempt prompt context -> optional persisted JSON/JSONL/log evidence. Reflexion does not promote reflections into reusable cross-project notes, tools, validators, or model weights in this repository.

## Comparison with Our System

| Dimension | Reflexion | Commonplace |
|---|---|---|
| Primary purpose | Improve repeated benchmark attempts through verbal self-reflection | Maintain a git-native methodology KB for future agents and maintainers |
| Canonical substrate | Runtime fields, run logs, environment JSON, programming JSONL | Typed Markdown artifacts, source snapshots, validators, indexes |
| Memory unit | Short failure-derived plan or hint | Source-grounded note, review, instruction, type contract, or generated index |
| Learning trigger | Failed attempt, failed test, halted trajectory, optional `--use_memory` | Authored capture, source ingest, review, validation, and deliberate promotion |
| Read-back | Harness-pushed reflection in later prompts | Mostly pull through search/indexes/skills, with validation and instructions as stronger control |
| Governance | Task success/failure and tests as local oracles | Type specs, citations, deterministic validation, semantic review, git history |

Reflexion is the cleanest small example of trace-derived prose learning: a failed run is not simply stored, it is distilled into advice meant to change the next run. Commonplace has a broader artifact system and stronger review discipline, but Reflexion is sharper about the timing of behavior change. The reflection is inserted before the repeated action, not left in a log for retrospective search.

The tradeoff is scope and trust. Reflexion's reflections are task-local, short-lived, and often generated from a strong benchmark oracle: exact match, environment success, reward, or unit tests. That makes the automatic promotion tolerable. Commonplace cannot copy that authority directly because KB memories often come from weaker signals: partial success, user preference, design judgment, or ambiguous source synthesis.

Reflexion also shows why "memory" and "learning" do not require a database. The learned object is a prose plan. Its effect comes from placement in the next prompt and from the harness deciding when to create and inject it.

### Borrowable Ideas

**Use failure-conditioned reflection as a candidate generator.** Ready now for low-authority workshop state. Commonplace could generate candidate observations after failed validation, failed tests, or repeated review warnings, but the candidates should enter an inbox rather than immediately becoming durable instructions.

**Keep raw trace and distilled lesson separate.** Ready now as review vocabulary. Reflexion's logs and environment histories remain raw evidence, while reflections are the distilled behavior-shaping artifacts. Commonplace should preserve the same split for any session-trace workflow.

**Cap repeated-attempt memory aggressively.** Ready now. The last-three memory cap in AlfWorld/WebShop is crude but useful: if a lesson needs more than a few attempts to matter, it probably needs promotion, retirement, or rewriting rather than endless prompt accumulation.

**Treat tests and success signals as promotion oracles only within their scope.** Ready with constraints. Programming Reflexion's test feedback is a stronger oracle than broad self-reflection over a chat log. Commonplace should let deterministic validation failures generate stronger candidate lessons than weak semantic hunches.

**Push lessons before repeated mistakes.** Worth borrowing carefully. Reflexion's main advantage is pre-action placement. Commonplace should borrow the timing, but not unconditional authority: pushed memories need scope, provenance, expiry, and evidence that they improve behavior.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
**Trace source:** `session-logs` `tool-traces` `trajectories` — scratchpads, action-observation trial logs, implementations, test feedback, and failed benchmark trajectories supply the raw signal

**Learning scope:** `per-task` — reflections are scoped to the same question, environment, or programming item rather than a project or cross-task library

**Learning timing:** `staged` — each cycle attempts, evaluates, reflects on failure, injects the reflection, and retries

**Distilled form:** `prose` — failed traces and feedback are compressed into verbal plans, hints, and diagnoses

**Trace source.** Reflexion qualifies as trace-derived learning. The qualifying traces are HotPotQA scratchpads, AlfWorld/WebShop action-observation trial logs, programming implementations plus unit-test feedback, and benchmark success/failure status. The trace boundary is a failed or incomplete attempt, not a continuous session miner.

**Extraction.** Extraction is LLM-mediated but oracle-gated. HotPotQA asks the reflection model to diagnose a failed reasoning trace. AlfWorld and WebShop generate a "New plan" from an unsuccessful environment history and prior memory. Programming tasks ask for a few-sentence explanation of why the implementation is wrong according to tests, then use that reflection as a hint for the next implementation ([alfworld_runs/generate_reflections.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/generate_reflections.py), [webshop_runs/generate_reflections.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/webshop_runs/generate_reflections.py), [programming_runs/generators/generator_utils.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/programming_runs/generators/generator_utils.py)).

**Scope and timing.** Scope is per-question, per-environment, or per-programming item. Timing is staged in cycles: attempt, evaluate, reflect if failed, inject reflection, retry. AlfWorld and WebShop can persist across trials and resume runs; HotPotQA and programming mostly operate inside a benchmark item, though programming writes the trace/reflection bundle to JSONL.

**Survey placement.** Reflexion belongs in the trace-to-prose-advice branch of the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md). It strengthens the survey's raw/distilled split: raw trajectories are evidence, while the behavior-shaping artifact is the verbal reflection pushed into the next prompt. It is not a trace-to-vector, trace-to-graph, trace-to-skill, or trace-to-weights system at this commit.

**Curation policy.** The curation oracle is benchmark-specific. Exact-answer checks, environment success, reward, exhaustion, and tests decide whether a reflection is needed; the LLM decides the content of the reflection. There is no independent review of reflection truthfulness, no source span carried into the memory entry, and no cross-task retirement policy beyond bounded windows and solved-task skipping.

## Read-back placement

**Direction.** Push-only for the acting agent. Reflection memory is selected and inserted by the runner before a future attempt. A human can inspect logs or JSONL, but the agent does not issue a memory search.

**Read-back signal:** `identifier` — the harness reuses the same question, environment config slot, programming item, or implementation chain when assembling the next prompt.

**Faithfulness tested:** `yes` — benchmark comparisons provide aggregate effect evidence for pushed reflections, though per-memory attribution remains unverified from code.

**Targeting and signal.** Targeting is `instance`: the pushed memory is selected for the same HotPotQA question, AlfWorld/WebShop environment config, programming item, or implementation chain, not by an always-load or generic action-type event. The signal is `identifier`: the harness already carries the question, environment index/config slot, dataset item, or current implementation state and reuses that identity when assembling the next prompt. AlfWorld/WebShop additionally cap memory to the latest three entries before prompt construction. Precision/recall of the generated reflection content is not verified from code.

**Injection point.** Read-back occurs before the next action loop or implementation generation, so it can change the next attempt. Reflection generation happens after the failed attempt, so it cannot repair the just-finished run.

**Selection, scope, and complexity.** Selection is small and task-local. HotPotQA includes accumulated reflection strings or the last attempt depending on strategy; AlfWorld/WebShop include at most three memory entries; programming includes the previous implementation, feedback, and one current self-reflection for the next code generation. Complexity stays low because memories are prose plans rather than multi-document retrieval bundles; actual context dilution is not verified from code.

**Authority at consumption.** Reflections are advisory prose placed in prompt positions that instruct use: "Use them to improve your strategy", "Your memory for the task below", or `[reflection on previous impl]`. They are not hard gates, but they have stronger structural authority than ordinary reference notes because the harness places them directly in the next action prompt; effective authority is not verified from code.

**Faithfulness.** The code structurally verifies read-back by prompt assembly and repeated benchmark loops. The repository includes paper logs and benchmark scripts, but the source itself does not prove that each fired reflection was faithfully used by the model in a causal sense. The benchmark comparison is the effect evidence; per-memory attribution remains unverified from code.

**Other consumers.** Humans and evaluators consume world logs, trial logs, environment JSON, and programming JSONL to inspect failures, reflections, and accuracy. Those surfaces are audit/reporting consumers, not additional agent read-back paths.

## Curiosity Pass

**The strongest memory implementation is also the narrowest.** Reflexion works because the retry target is nearly identical: the same environment, question, or programming item. That makes relevance trivial compared with open-ended KB memory.

**The repository's memory is mostly outside a reusable library abstraction.** Each benchmark runner implements its own reflection loop. That keeps the experiments simple, but it means there is no shared lifecycle, provenance model, or memory API to borrow wholesale.

**Reflection content is lower-governance than its prompt authority.** A generated plan can be wrong, overfit, or stale, yet the next prompt tells the agent to use it. The system relies on short scope and repeated evaluation rather than review metadata.

**Programming Reflexion is closer to repair-loop prompting than long-term memory.** The reflection becomes a hint for the next implementation in the same item, then the result is logged. It is trace-derived learning, but not a general retained memory system across tasks.

**The last-three cap is a quiet design decision.** It treats context as a scarce behavior-shaping surface. More memories are not assumed to be better.

## What to Watch

- Whether future Reflexion-style systems preserve source pointers from a reflection back to the exact trajectory segment or failing test that caused it; that would make trace-derived advice auditable.
- Whether reflections can update, merge, or retire earlier reflections rather than appending bounded lists; this would change the lifecycle story from retry memory to maintained memory.
- Whether cross-task reflection libraries emerge from this code path; that would make relevance and governance much harder than same-task retry.
- Whether per-reflection ablations appear, showing which pushed reflection actually changed a later action rather than only improving aggregate success.
- Whether a Reflexion implementation promotes recurring verbal lessons into tests, policies, or tool constraints; that would cross from prose advice into symbolic system-definition artifacts.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Reflexion turns failed trajectories and test feedback into task-local verbal advice for later attempts.
- [Use Trace-Derived Extraction As Meta-Learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: failed attempts are distilled after the fact into reusable but scoped memory artifacts.
- [Activate Behavior-Changing Memory Before The Mistake](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies: reflections are pushed before the repeated attempt, not left as retrospective logs.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Reflexion's retained lessons matter because the harness injects them at retry time.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Reflexion separates raw traces, prose reflections, prompt templates, and result logs by substrate, form, lineage, and authority.
