---
description: "Reflexion review: benchmark trace-to-reflection loops that reinject failed-attempt plans into retries"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-05-16"
---

# Reflexion

Reflexion is Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao's NeurIPS 2023 research implementation of "Language Agents with Verbal Reinforcement Learning." The repository is not a general-purpose memory service; it is a set of benchmark loops where failed task trajectories are turned into natural-language reflections and injected into later attempts on the same task.

**Repository:** https://github.com/noahshinn/reflexion

**Reviewed commit:** [218cf0ef1df84b05ce379dd4a8e47f17766733a0](https://github.com/noahshinn/reflexion/commit/218cf0ef1df84b05ce379dd4a8e47f17766733a0)

**Last checked:** 2026-05-16

## Core Ideas

**The memory object is a rolling list of reflection strings.** In ALFWorld and WebShop, each environment config starts with `memory: []`; after a trial, `update_memory(...)` reads the trial log, generates a reflection only for unsolved environments, and appends it to that environment's memory list ([alfworld_runs/main.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/main.py), [alfworld_runs/generate_reflections.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/generate_reflections.py), [webshop_runs/main.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/webshop_runs/main.py)). Runtime prompt construction keeps only the last three reflections when memory grows past three entries ([alfworld_runs/alfworld_trial.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/alfworld_trial.py), [webshop_runs/webshop_trial.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/webshop_runs/webshop_trial.py)). That rolling window is the lifecycle policy.

**Failure is the reflection trigger.** ALFWorld and WebShop call the reflection generator after each trial only when `is_success` is false; solved environments are skipped in future trials and do not accumulate new reflections ([alfworld_runs/generate_reflections.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/generate_reflections.py), [webshop_runs/generate_reflections.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/webshop_runs/generate_reflections.py)). In HotPotQA, `ReactReflectAgent.run(...)` and `CoTAgent.run(...)` reflect when a previous attempt finished, halted, or answered incorrectly, subject to the selected `ReflexionStrategy` ([hotpotqa_runs/agents.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/agents.py)). In programming runs, unit-test failure triggers self-reflection, and the next implementation prompt receives the previous code, test feedback, and reflection ([programming_runs/reflexion.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/programming_runs/reflexion.py), [programming_runs/generators/generator_utils.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/programming_runs/generators/generator_utils.py)).

**Reflection prompts ask for a corrective plan, not a summary.** The ALFWorld and WebShop reflection prompts explicitly tell the model not to summarize the environment, but to diagnose the failed path and produce a concise new plan for the same task ([alfworld_runs/generate_reflections.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/generate_reflections.py), [webshop_runs/generate_reflections.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/webshop_runs/generate_reflections.py)). HotPotQA's prompts frame reflections as plans to avoid the same failure in answering the question ([hotpotqa_runs/prompts.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/prompts.py)). Programming prompts ask for a few sentences explaining why the implementation is wrong, then pass that explanation as a hint for the next implementation ([programming_runs/generators/py_generate.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/programming_runs/generators/py_generate.py)).

**Prompt reinjection is the behavior-changing surface.** In ALFWorld and WebShop, `EnvironmentHistory` inserts memory under "Your memory for the task below" before the task text ([alfworld_runs/env_history.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/env_history.py), [webshop_runs/env_history.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/webshop_runs/env_history.py)). HotPotQA formats either previous attempts, reflections, or both through `ReflexionStrategy.NONE`, `LAST_ATTEMPT`, `REFLEXION`, and `LAST_ATTEMPT_AND_REFLEXION` ([hotpotqa_runs/agents.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/agents.py)). Programming reinjects reflection inside the next code-generation prompt together with the failing implementation and test feedback ([programming_runs/generators/generator_utils.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/programming_runs/generators/generator_utils.py)).

**Persistence is benchmark-local files and serialized run outputs.** ALFWorld and WebShop write `trial_<n>.log`, `world.log`, and `env_results_trial_<n>.json`, with reflection strings embedded in each environment's JSON config ([alfworld_runs/main.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/alfworld_runs/main.py), [webshop_runs/main.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/webshop_runs/main.py)). Programming runs append JSONL records containing `reflections`, `implementations`, `test_feedback`, `solution`, and `is_solved` ([programming_runs/reflexion.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/programming_runs/reflexion.py), [programming_runs/utils.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/programming_runs/utils.py)). HotPotQA includes joblib and text result artifacts under the experiment root, but the core runtime object is still the agent's in-memory `reflections` list and formatted prompt string ([hotpotqa_runs/util.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/util.py), [hotpotqa_runs/agents.py](https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/agents.py)).

## Comparison with Our System

| Dimension | Reflexion | Commonplace |
|---|---|---|
| Primary purpose | Improve repeated benchmark attempts on the same task | Maintain an agent-operated methodology KB |
| Raw substrate | Failed trajectories, trial logs, scratchpads, unit-test feedback | Git-tracked notes, sources, instructions, reviews, indexes |
| Distilled artifact | Natural-language reflection strings | Typed notes, ADRs, instructions, schemas, commands, review artifacts |
| Activation | Prompt reinjection on the next retry | Navigation, links, indexes, skills, validation, review gates |
| Lineage | Run files contain source traces; reflection strings do not cite exact source spans | Source links, reviewed revisions, archives, validation, authored links |
| Behavioral authority | Reflection strings instruct or strongly guide same-task retries | Knowledge artifacts advise; system-definition artifacts instruct, validate, route, or enforce |
| Lifecycle | Append reflections, use last three, stop once solved | Status fields, replacement archives, validation, curated indexes, review lifecycle |

Reflexion is much narrower than commonplace. It does not try to build a reusable knowledge library, a retrieval layer, a type system, or a promotion pipeline. It takes one failed attempt, asks for a verbal corrective policy, and puts that policy back into the next attempt's prompt.

That narrowness is the design strength. Reflexion's artifact contract is easy to understand: raw trace first, reflection second, retry with reflection third. The system therefore has an unusually crisp distinction between source trace and behavior-shaping artifact. The weakness is that the reflection object itself has almost no durable metadata. It carries no explicit source citation, confidence, expiry condition, cross-task scope, review status, or invalidation rule beyond being attached to a benchmark environment or result row.

The behavioral-authority split is important. Failed trajectories, logs, previous attempts, and test feedback are knowledge artifacts when used as evidence for reflection. The generated reflection becomes a system-definition artifact when inserted under prompt text that tells the agent to use it to improve the next attempt. The artifact is still prose, but its authority comes from the retry prompt channel.

## Borrowable Ideas

**Use failure as a clean promotion trigger.** Ready now for narrow workflows. Reflexion does not mine every trace; it asks for reflection when an oracle says the attempt failed. Commonplace could use the same trigger discipline for review warnings, validation failures, or repeated operator mistakes, while keeping human or validation gates for durable promotion.

**Separate raw trace capture from corrective prose.** Ready now as a workshop-layer pattern. Trial logs should remain evidence; candidate reflections should be separate artifacts whose authority depends on where they are injected.

**Keep reflection windows small at activation time.** Useful but scope-bound. Reflexion's last-three rule is crude, but it recognizes that prompt memory must be bounded. Commonplace should prefer authored selection and typed relevance over a fixed rolling window, but bounded activation is the right instinct.

**Borrow the same-task retry loop, not the whole memory model.** Reflexion is ideal for short-horizon repair: answer again, navigate again, implement again. It is not enough for long-lived methodology claims, where retained artifacts need provenance, status, and composable links.

**Treat prompt headers as authority controls.** Ready now. Reflexion's reflections matter because the prompt says to use them. Commonplace should continue to distinguish notes that advise from instructions, validators, and skills that bind or enforce behavior.

## Trace-derived learning placement

**Trace source.** Reflexion qualifies as trace-derived learning. Its source traces are failed task trajectories: ALFWorld and WebShop action/observation logs, HotPotQA scratchpads and previous attempts, and programming implementations with unit-test feedback. Trigger boundaries are per environment trial, per QA retry, or per programming iteration.

**Extraction.** Extraction is LLM-generated self-reflection. The oracle is benchmark success/failure, exact-match answer correctness, halted/truncated reasoning, reward completion, or unit-test failure depending on the loop. The model receives the failed trace and produces a concise plan or diagnosis intended for the next attempt.

**Storage substrate.** Raw traces persist in local logs, result text files, joblib artifacts, and JSONL run records. Reflection strings persist in ALFWorld/WebShop `env_results_trial_<n>.json`, in HotPotQA agent state or serialized experiment artifacts, and in programming JSONL result rows. There is no database, vector store, graph, prompt registry, or model-artifact store.

**Representational form.** Raw traces are mixed prose and symbolic event records: thoughts, actions, observations, tests, feedback, booleans, rewards, and status fields. Reflections are prose. Programming loops also carry symbolic code and test results, but the behavior-shaping retained artifact is the natural-language reflection string; no learned weights or embeddings are produced.

**Lineage.** Lineage is run-local rather than artifact-local. A JSON or JSONL record can show the task, feedback, implementation history, and reflections for that run, but a reflection string does not itself carry a source pointer, derivation metadata, confidence, or regeneration rule. ALFWorld and WebShop preserve stronger per-environment continuity because the memory list stays with the environment config across trials.

**Behavioral authority.** Failed logs, scratchpads, previous attempts, and test feedback are knowledge artifacts when consumed as evidence for reflection generation. Reflection strings become system-definition artifacts when prompt headers instruct the acting agent to use them as plans, hints, or memory for the next attempt. The strategy enum in HotPotQA is a runtime system-definition surface because it configures whether no memory, last attempt, reflection, or both are injected.

**Scope.** Scope is task-local and benchmark-local. ALFWorld and WebShop memories are tied to a specific environment task; HotPotQA reflections attach to the same question; programming reflections guide the next implementation of the same problem. The code does not implement cross-task consolidation into reusable rules.

**Timing.** Reflexion is online within an evaluation episode or staged trial loop: attempt, fail, reflect, retry. It is not an offline corpus-mining system, though the repository also includes saved logs from paper runs.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Reflexion sits in the trace-to-prose-reflection branch with prompt reinjection and task-local scope. It strengthens the survey's distinction between raw trace artifacts and distilled behavior-shaping artifacts, and it weakens any assumption that trace-derived learning requires long-term retrieval infrastructure.

## Curiosity Pass

The name "verbal reinforcement learning" can sound more durable than the implementation is. The code does not update a policy, train a model, or maintain a general memory index. It writes or holds short prose reflections and gives them prompt authority on retries.

The strongest design move is the clean source/artifact split: failed trace in, reflection out, reflection back into the prompt. The weakest part is lifecycle. Reflections accumulate until success or until the rolling prompt window excludes older ones; they are not reviewed, merged, retired by evidence, or promoted into higher-authority rules.

The HotPotQA strategy enum is useful because it makes the ablation surface explicit. `LAST_ATTEMPT` tests trace replay, `REFLEXION` tests distilled prose, and `LAST_ATTEMPT_AND_REFLEXION` tests both. That is a clearer authority experiment than systems where every retained object is simply called memory.

## What to Watch

- Whether descendants add per-reflection provenance without losing Reflexion's simple retry loop.
- Whether task-local reflections can be consolidated into cross-task rules without becoming brittle benchmark lore.
- Whether explicit strategy controls remain visible in newer implementations or disappear into prompt templates.
- Whether reflection strings help because they diagnose failure, because they change sampling, or because they simply add more task-specific context.
- Whether programming variants keep reflections separate from unit-test feedback and code history when logs are resumed or post-processed.

## Bottom Line

Reflexion is a precise trace-to-reflection system: failed trajectories produce short natural-language corrective plans, and those plans are reinjected into same-task retries. Its lesson for commonplace is not a storage architecture, but an authority pattern: keep raw traces as evidence, make distilled reflections separate, and be explicit about the prompt channel that turns advice into instruction.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Reflexion anchors task-local trace-to-prose reflection with prompt reinjection.
- [ExpeL](./expel.md) - compares-with: ExpeL builds on Reflexion-style trajectories but adds cross-task rule extraction and rule maintenance.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: Reflexion's failed traces and logs advise as source evidence.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: Reflexion's prompt-injected reflections carry retry guidance authority.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - clarifies: Reflexion's memory effect comes from the consumer channel, not from the storage label.
