---
description: "Auto-harness review: benchmark loop where train traces drive agent-file edits, learnings logs, regression-suite promotion, and score gates"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-01"
---

# auto-harness

> Replaced 2026-06-04. See [auto-harness](./auto-harness.md) for the current review.

auto-harness, from neosigmaai's `auto-harness` repository, is a benchmark-driven optimization harness for coding agents. It gives an external coding agent a benchmark, a mutable `agent/agent.py`, generated loop instructions, train-only failure traces, a persistent learnings log, and a gate that requires regression-suite and test-score checks before a change is recorded. The memory system is not a retrieval database; it is a work loop where traces and scores are distilled by the coding agent into source-code, instructions, logs, and regression tasks that shape later benchmark attempts.

**Repository:** https://github.com/neosigmaai/auto-harness

**Reviewed commit:** [de6b3ed51517909ff7a92466908e9ea161964865](https://github.com/neosigmaai/auto-harness/commit/de6b3ed51517909ff7a92466908e9ea161964865)

**Last checked:** 2026-06-01

## Core Ideas

**The retained agent is a source file under benchmark control.** `prepare.py` copies a benchmark-specific template into `agent/agent.py`, and the program tells the coding agent that this file is its edit target for optimization ([prepare.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/prepare.py), [program_templates/base.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/program_templates/base.md)). The benchmark runner then imports that file directly: tau-bench registers `HarnessAgent`, Terminal-Bench uses Harbor's `agent.agent:HarnessAgent` import path, and BIRD-Interact serves `agent.agent.build_agent()` through a FastAPI wrapper ([benchmark.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/benchmark.py), [agent/helpers/bird_interact/bird_adk_runtime.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/agent/helpers/bird_interact/bird_adk_runtime.py)).

**Train traces are the evidence layer, with test traces structurally withheld.** Terminal-Bench train runs copy `trace.json` and `result.json` into `workspace/traces/latest/` and preserve first-run traces under `workspace/traces/baseline/`; for non-train splits the runner sets `HARNESS_SAVE_TRACE=0` before calling Harbor ([benchmark.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/benchmark.py), [agent/templates/terminal_bench.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/agent/templates/terminal_bench.py)). BIRD-Interact similarly copies train dialogue history, tool trajectory, ADK events, final response, and result metadata into `workspace/traces/` ([benchmark.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/benchmark.py)). This is a deliberate anti-leakage boundary rather than a search layer.

**The coding agent is the distillation oracle.** The generated program instructs the agent to run the train benchmark, inspect failing train traces, diagnose root causes, edit `agent/agent.py`, gate the change, record the result, and append to `workspace/learnings.md` after every iteration ([program_templates/base.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/program_templates/base.md)). Benchmark-specific templates add local advice about which traces to read and what parts of the agent file are fair game ([program_templates/terminal_bench.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/program_templates/terminal_bench.md), [program_templates/bird_interact.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/program_templates/bird_interact.md), [program_templates/tau_bench.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/program_templates/tau_bench.md)). There is no separate extractor schema; the model doing the code work decides what trace signal becomes code or prose memory.

**Gating turns benchmark outcomes into enforced lifecycle policy.** `gating.py` first rejects tracked edits outside the allowlist, then reruns `workspace/suite.json`, then always runs the full test split and requires `val_score` to meet or exceed the best score already recorded, and finally promotes newly fixed train failures into the regression suite ([gating.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/gating.py)). `record.py` appends the accepted iteration, score, commit, eval counts, and timestamp to `workspace/results.tsv`, while also checking the file guard across the last commit ([record.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/record.py)). The latest commit explicitly counts missing verifier results as `0.0` in `val_score`, so timeouts become optimization failures rather than disappearing from the average ([benchmark.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/benchmark.py)).

**Benchmark adapters keep the outer loop reusable while preserving task-specific surfaces.** The repo ships runners for tau-bench, Terminal-Bench through Harbor, and BIRD-Interact through an external ADK service stack ([benchmark.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/benchmark.py), [agent/helpers/bird_interact/bird_service.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/agent/helpers/bird_interact/bird_service.py)). Each benchmark has both an agent template and a program supplement, so the retained agent file and the loop instructions are assembled for the chosen environment rather than treated as one universal prompt ([agent/templates](https://github.com/neosigmaai/auto-harness/tree/de6b3ed51517909ff7a92466908e9ea161964865/agent/templates), [program_templates](https://github.com/neosigmaai/auto-harness/tree/de6b3ed51517909ff7a92466908e9ea161964865/program_templates)).

**The agent's context is the evolved code, not a growing store.** Read-back is the imported `agent/agent.py`; traces are train-only, so the main volume risk is an unbounded `workspace/learnings.md` accumulating across iterations rather than retrieval bloat.

## Artifact analysis

- **Storage substrate:** `files` — Gitignored `workspace/traces/latest/`, `workspace/traces/baseline/`, benchmark job directories before pruning, and `workspace/train_results.json` ([benchmark.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/benchmark.py))
- **Representational form:** `prose` `symbolic` — prose prompts, learnings, traces, and instructions plus symbolic JSON/TSV, Python code, gates, split policy, and suite entries
- **Lineage:** `authored` `imported` `trace-extracted` — authored harness policy and templates, imported benchmark templates/splits, and trace-extracted edits, learnings, result summaries, and suite entries
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `learning` — traces and learnings advise diagnosis; `PROGRAM.md` instructs the optimizer; gates enforce/validate; templates and adapters route benchmark execution; accepted edits become learned agent behavior

**Raw traces and result files.** Storage substrate: gitignored `workspace/traces/latest/`, `workspace/traces/baseline/`, benchmark job directories before pruning, and `workspace/train_results.json` ([benchmark.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/benchmark.py)). Representational form: mixed JSON containing conversation traces, tool calls, command output, ADK events, rewards, and task metadata. Lineage: generated from train benchmark executions; Terminal-Bench baseline traces are preserved once, latest traces are overwritten each train run, and test traces are intentionally not saved. Behavioral authority: knowledge artifacts for the coding agent's diagnosis; they do not directly instruct the benchmarked agent until distilled into code, prompt text, or suite entries.

**`agent/agent.py`.** Storage substrate: repository source file copied from `agent/templates/` by `prepare.py` and then edited by the coding agent ([prepare.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/prepare.py), [agent/templates/terminal_bench.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/agent/templates/terminal_bench.py), [agent/templates/tau_bench.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/agent/templates/tau_bench.py), [agent/templates/bird_interact.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/agent/templates/bird_interact.py)). Representational form: mixed prose and symbolic code: prompts, tool schemas, constants, control flow, callbacks, and runtime wrappers. Lineage: initially template-derived, then trace- and benchmark-derived through the coding agent's edits and accepted git commits. Behavioral authority: system-definition artifact with direct instruction, tool, routing, and execution force over future benchmark attempts.

**Generated `PROGRAM.md` and program templates.** Storage substrate: repository templates under `program_templates/`, composed into `PROGRAM.md` by `prepare.py` ([prepare.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/prepare.py), [program_templates/base.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/program_templates/base.md)). Representational form: prose procedure with command tables, file ownership rules, benchmark-specific trace guidance, and stop conditions. Lineage: authored harness policy plus benchmark-specific supplements. Behavioral authority: system-definition artifact for the optimizing coding agent, because it defines what to read, what to edit, which commands to run, and how to respond to failed gates.

**`workspace/learnings.md`.** Storage substrate: gitignored workspace file initialized by `prepare.py` and appended by the coding agent according to the program ([prepare.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/prepare.py), [program_templates/base.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/program_templates/base.md)). Representational form: prose. Lineage: trace-derived and experiment-derived, but only as reliable as the coding agent's self-report. Behavioral authority: weak knowledge artifact by default, and a soft system-definition input when a later agent reads it as iteration guidance. The code initializes and requires appends; it does not enforce a structured read-back or validate claims inside the log.

**`workspace/suite.json` and `workspace/results.tsv`.** Storage substrate: gitignored workspace files managed by `prepare.py`, `gating.py`, and `record.py` ([prepare.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/prepare.py), [gating.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/gating.py), [record.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/record.py)). Representational form: symbolic JSON and TSV. Lineage: suite entries are promoted from previously failing train tasks that later pass; result rows are accepted-iteration summaries with commit and score metadata. Behavioral authority: `suite.json` is an enforcement artifact because gate failure blocks progress; `results.tsv` is an evaluation history used to set the best-score threshold for future gates.

**File guard and benchmark split policy.** Storage substrate: symbolic Python code and generated split files such as `tbench_data/task_split.json` or `bird_data/task_split.json` ([prepare.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/prepare.py), [gating.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/gating.py)). Representational form: symbolic policy. Lineage: authored harness design, with splits generated from baseline runs. Behavioral authority: system-definition artifact with governance force: it blocks infrastructure edits, hides test traces from the optimizer, and separates train diagnosis from test gating.

### Borrowable Ideas

**A work loop can be memory without a memory service.** Commonplace could reuse this pattern for bounded improvement campaigns: preserve evidence, give the agent an editable artifact, require a gate, and record accepted iterations. Ready for workshop workflows; not a replacement for library artifacts.

**Promote failures into a regression suite after demonstrated fixes.** Commonplace review gates could borrow the automatic "newly fixed cases become future guardrails" rule, but only where tasks have deterministic or reviewable pass criteria. Ready where validators exist; premature for open-ended prose quality.

**Keep test evidence out of the optimizer's context.** The train/test trace split is a clean context-engineering control. Commonplace can apply the same principle to evaluation sets for agent instructions: expose train failures for revision, withhold held-out traces for gate runs. Ready now for evaluation design.

**Treat generated instructions and mutable artifacts as separate authority surfaces.** auto-harness distinguishes `PROGRAM.md` as loop authority from `agent/agent.py` as benchmark-agent authority. Commonplace should keep making this split explicit when a workshop has both a worker procedure and a target artifact.

**Do not borrow unstructured learnings as durable methodology.** `workspace/learnings.md` is useful scratch memory, but it lacks typed lineage, status, source citations, and validation. Commonplace should require promotion into notes, instructions, tests, or ADRs before such lessons gain durable library authority.

## Comparison with Our System

| Dimension | auto-harness | Commonplace |
|---|---|---|
| Primary loop | Benchmark-run, trace inspection, agent-file edit, gate, commit, record | Source-grounded writing, linking, validation, semantic review, index maintenance |
| Raw evidence | Train traces, task rewards, result JSON, benchmark logs | Source snapshots, notes, reviews, reports, git diffs, command output |
| Distilled artifact | `agent/agent.py`, `workspace/learnings.md`, `workspace/suite.json`, commits | Typed markdown notes, instructions, ADRs, schemas, validators, indexes |
| Authority path | Edited agent code runs in the next benchmark; suite and score gates block bad changes | Instructions and type specs shape agents; validators and review gates check artifacts |
| Governance | File allowlist, train/test split, regression suite, full-test best-score gate | Collection contracts, frontmatter, link rules, schemas, deterministic validation, review bundles |
| Reviewability | Strong for code diffs and scores; weak for why a learning was accepted | Stronger typed lineage and prose review; weaker automatic performance feedback unless tasks are codified |

auto-harness is closest to a trace-derived, benchmark-coupled improvement workshop. Its durable behavior changes are made by editing the running agent implementation, not by retrieving memories into an otherwise fixed agent. That makes the read-back path simple and strong: the next benchmark imports the evolved code, while the next coding-agent session is expected to follow the generated program and may inspect the learnings log and traces.

Compared with Commonplace, the system has a sharper quantitative gate but a weaker semantic archive. It can tell whether the new `agent/agent.py` improved or preserved benchmark score; it cannot tell whether the explanation in `workspace/learnings.md` is true, whether a prompt rule overfits a train trace, or whether a promoted suite case represents a general capability. Commonplace has the opposite bias: stronger typed review and lineage, but less automatic evidence that a rule changes future behavior.

The most important artifact-authority split is between evidence, optimization policy, and executable agent state. Train traces and train results are knowledge artifacts. `PROGRAM.md`, benchmark templates, file guards, split policy, suite promotion, and score gates are system-definition artifacts for the optimizing loop. `agent/agent.py` is both the retained learned artifact and the executable system-definition artifact consumed by the benchmark.

**Read-back:** `both` — The benchmark gets a coarse memory push because every run imports the evolved `agent/agent.py`; the optimizing coding agent gets retained traces, `workspace/learnings.md`, and train results only by pulling the files that `PROGRAM.md` tells it to inspect. There is no instance-targeted signal, matcher, retrieval budget, before-action hook, or relevance-gated memory injection beyond deterministic benchmark execution and program-following

**Read-back signal:** `coarse` — the push path is deterministic import of the evolved `agent/agent.py` on every benchmark run, not an identifier match or inferred retrieval signal.

**Faithfulness tested:** `no` — score gates test the edited agent, but the review says there is no explicit ablation separating genuine behavior improvements from score noise.

## Write-side placement

**Write agency:** `automatic` `manual` — the harness automatically copies templates, records traces/results, enforces gates, promotes suite entries, and records accepted iterations, while the optimizing coding agent manually edits `agent/agent.py` and appends learnings from the trace evidence

**Curation operations:** `promote` `invalidate` — newly fixed failures are promoted into `workspace/suite.json` regression obligations, accepted scores/commits are recorded as the current best baseline, and gates reject or invalidate changes that touch disallowed files or regress the suite/test score

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` `trajectories` — train-split dialogue histories, tool trajectories, ADK events, trace files, and result summaries are the retained evidence layer.

**Learning scope:** `per-task` `cross-task` — task-level failures and fixes are promoted into suite obligations and agent edits that can affect later benchmark tasks.

**Learning timing:** `staged` — learning happens through train run, trace inspection, edit, gate, commit, record, and repeat cycles.

**Distilled form:** `prose` `symbolic` — traces are distilled into prose learnings plus symbolic Python code, JSON suite entries, gates, and result records.

**Trace source.** auto-harness qualifies as trace-derived learning. The qualifying traces are train-split conversation/tool traces and result files copied into `workspace/traces/` for Terminal-Bench and BIRD-Interact, plus train result summaries in `workspace/train_results.json` ([benchmark.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/benchmark.py)). tau-bench support exposes train benchmark results through the same runner and program loop, but the inspected implementation does not add a tau-specific trace-copying path comparable to Terminal-Bench or BIRD.

**Extraction.** Extraction is agentic rather than schema-bound. The coding agent reads failed train traces, stdout, and result files; it decides what failure mode matters; then it edits `agent/agent.py` and appends prose to `workspace/learnings.md` ([program_templates/base.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/program_templates/base.md)). Gating adds a second extraction path: newly passing train tasks that were previously failing are promoted into `workspace/suite.json` as future regression obligations ([gating.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/gating.py)).

**Scope and timing.** Scope is per experiment workspace and per benchmark configuration. Timing is staged in iterations: train run, trace inspection, edit, gate, commit, record, and repeat. The trace-derived artifact can affect the very next benchmark run through source-code import, while the learnings log affects only later optimizer behavior if the agent reads it.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), auto-harness belongs in the trace-to-code and trace-to-regression-suite family. It strengthens the survey claim that trace-derived learning does not have to look like RAG: a trace can be distilled into executable code, a gating suite, or an optimization procedure rather than a retrieved note. It also weakens any assumption that trace-derived systems have automatic extraction: here the coding agent is the extractor and reviewer, and the hard check is benchmark performance rather than semantic validation of the extracted lesson.

## Curiosity Pass

**The benchmarked agent and the optimizing agent are different consumers.** `agent/agent.py` shapes benchmark execution, while `PROGRAM.md`, traces, and learnings shape the coding agent that edits it. Reviews that collapse those into one "agent memory" surface will miss where authority actually enters.

**The self-maintained suite is partly automatic and partly earned.** The coding agent does not hand-pick every suite item. `gating.py` promotes newly passing previously failed train tasks after both gates pass, making the suite a derived enforcement artifact rather than only a human or model-authored checklist.

**The anti-cheating boundary is a memory-design feature.** Test traces are not merely ignored by instruction; Terminal-Bench sets `HARNESS_SAVE_TRACE=0` outside train runs, and program supplements warn the optimizer away from raw job directories ([benchmark.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/benchmark.py), [program_templates/terminal_bench.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/program_templates/terminal_bench.md)). That is a useful example of constraining what evidence can enter the learning loop.

**`workspace/learnings.md` is intentionally soft memory.** The README emphasizes that learnings close the loop, but the code does not parse, validate, or inject individual lessons ([README.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/README.md)). It is a human-readable knowledge artifact unless the next coding agent chooses to treat it as guidance.

**The latest timeout change matters for memory quality.** Counting missing verifier results as `0.0` prevents a learned agent from looking better by hanging on hard tasks. That is not a memory feature by itself, but it changes which edits survive and therefore which trace-derived behaviors persist.

## What to Watch

- Whether future versions add a structured extractor for traces and learnings, or keep the coding agent as the only distillation oracle.
- Whether `workspace/learnings.md` gains typed entries, source trace links, acceptance state, or promotion rules before it influences long-running campaigns.
- Whether tau-bench gets the same explicit trace-copying substrate and anti-leakage mechanics as Terminal-Bench and BIRD-Interact.
- Whether suite promotion evolves from "newly passing failed task" into a richer regression-selection policy that accounts for representativeness and overfitting risk.
- Whether the harness adds an explicit ablation step for prompt/code changes, separating genuine behavior improvements from score noise across repeated benchmark runs.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: auto-harness distills train traces into agent code, prose learnings, and regression-suite obligations.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: traces, result files, and learnings logs mostly serve as evidence or advice until promoted into stronger authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: `agent/agent.py`, `PROGRAM.md`, gates, suite policy, and split policy instruct, enforce, route, or evaluate behavior.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - sharpens: the same trace-derived observation changes force when it moves from a log entry into code or a blocking regression suite.
- [Lineage](../../notes/definitions/lineage.md) - cautions: trace-derived code changes and learnings need source and acceptance lineage if they are promoted beyond a workspace loop.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: storing `workspace/learnings.md` is weaker than importing evolved `agent/agent.py` or enforcing `workspace/suite.json`.
