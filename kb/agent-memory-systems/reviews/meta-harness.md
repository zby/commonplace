---
description: "Meta-Harness review: offline evolutionary search over model harness code using proposer skills, candidates, traces, frontiers, and benchmark summaries"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-02"
---

# Meta-Harness

Meta-Harness, from Stanford IRIS Lab, is a framework for optimizing the code around a fixed base model: memory systems for text classification and agent scaffolds for Terminal-Bench 2. The public repository is a cleaned-up release with an onboarding prompt, two reference experiments, Claude Code proposer wrappers, proposer skills, candidate Python files, benchmark/evaluation scripts, and run-state artifacts such as pending candidates, frontiers, evolution summaries, logs, and job results.

**Repository:** https://github.com/stanford-iris-lab/meta-harness

**Reviewed commit:** [95175f70c758dd1145b395edfe8b67e6f9d80fbd](https://github.com/stanford-iris-lab/meta-harness/commit/95175f70c758dd1145b395edfe8b67e6f9d80fbd)

**Last checked:** 2026-06-02

## Core Ideas

**The searched object is executable harness code, not model weights or plain memory records.** The README defines a harness as "the code around a fixed base model that decides what to store, retrieve, and show while the model works," and the examples make that concrete: text classification candidates subclass `MemorySystem`, while Terminal-Bench 2 candidates are Python `AgentHarness` files loaded by Harbor ([README.md](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/README.md), [memory_system.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/memory_system.py), [terminal_bench_2 skill](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md)).

**Onboarding is an agent-facing spec elicitation step.** `ONBOARDING.md` is not a generic README; it tells an assistant to interview the user, fill required fields for task, harness, evaluation, baselines, offline experience, online experience, and budget, and only then write `domain_spec.md` ([ONBOARDING.md](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/ONBOARDING.md)). The release therefore treats domain adaptation itself as a constrained agent workflow before implementation begins.

**The text-classification loop searches memory-system implementations.** `meta_harness.py` runs baselines, calls Claude Code with the `meta-harness` skill, expects candidates in `pending_eval.json`, import-checks each candidate, benchmarks valid systems across configured datasets, updates `frontier_val.json`, and appends one JSONL row per candidate to `evolution_summary.jsonl` ([text_classification/meta_harness.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/meta_harness.py)). The candidate interface has `predict`, `learn_from_batch`, `get_state`, `set_state`, and `get_context_length`, so memory behavior and context footprint are explicit optimization surfaces ([memory_system.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/memory_system.py)).

**The Terminal-Bench 2 loop searches agent scaffolds.** Its loop calls Claude Code with a Terminal-Bench-specific skill, validates proposed `AgentHarness` imports, runs a smoke task, launches Harbor evaluations, parses per-trial job directories, updates the frontier, and records pass rates, token counts, cost, turns, and timing ([terminal_bench_2/meta_harness.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/meta_harness.py), [run_eval.sh](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/scripts/run_eval.sh)). The baseline KIRA scaffold exposes overridable tool-calling, command execution, prompt-template, image-read, and context-summarization methods ([baseline_kira.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/agents/baseline_kira.py)).

**Proposer skills are the durable search policy.** The two `.claude/skills` files instruct the proposer how to read previous state, avoid parameter-only changes, prototype or analyze trajectories, implement candidates, validate them, and write `pending_eval.json` ([text skill](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md), [Terminal-Bench skill](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md)). These are authored system-definition artifacts that shape candidate generation more directly than the benchmark scripts do.

**Context efficiency is measured and optimized, not just assumed.** In text classification, the benchmark records `memory_context_chars`, computes an accuracy-versus-context Pareto frontier, and baselines such as `FewShotMemory` cap formatted examples by character budget ([benchmark.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/benchmark.py), [fewshot_memory.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/agents/fewshot_memory.py)). In Terminal-Bench 2, the loop records input/output/cache tokens, cost, turns, and per-task metrics, while candidate scaffolds can change prompt templates, summarization, tools, and command-observation handling ([terminal_bench_2/meta_harness.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/meta_harness.py)).

**The release is explicit about its limits.** The README says this is a cleaned-up version of the paper code and "has not been tested beyond verifying that it runs," and the optimized Terminal-Bench 2 harness is in a separate artifact repository rather than this repo ([README.md](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/README.md)). A review should therefore treat the repository as a reference implementation and adaptation template, not a polished framework library.

## Artifact analysis

- **Storage substrate:** `files` — Repo files, with `ONBOARDING.md` shipped and `domain_spec.md` expected as a generated project-local file
- **Representational form:** `prose` — Prose instructions plus a structured Markdown template
- **Lineage:** `authored` `trace-extracted` — authored onboarding prompts, skills, baselines, and scripts combine with proposer/evaluation traces, summaries, frontiers, and generated candidate variants
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — logs and summaries inform later search; skills instruct proposers; import checks, smoke tests, and benchmarks enforce/validate candidates; harness code routes runtime behavior; frontiers rank; candidate generation learns from prior runs

**Onboarding and domain specs.** Storage substrate: repo files, with `ONBOARDING.md` shipped and `domain_spec.md` expected as a generated project-local file. Representational form: prose instructions plus a structured Markdown template. Lineage: authored onboarding prompt, then user/assistant elicitation fills a derived domain spec; unresolved fields are explicitly marked `unknown`. Behavioral authority: system-definition artifact for setup, because it constrains what a later implementation pass may assume and defines the task/harness/evaluation boundary.

**Proposer skills.** Storage substrate: `.claude/skills/.../SKILL.md` inside each reference example. Representational form: prose instructions with symbolic output contracts for `pending_eval.json`, candidate file paths, import paths, and validation commands. Lineage: authored prior for the proposer, sometimes consuming prior run summaries and trajectory logs. Behavioral authority: system-definition artifact loaded into Claude Code's system prompt by `claude_wrapper.run`; it instructs candidate generation, allowed workflow, anti-overfitting policy, and output shape.

**Candidate harness files.** Storage substrate: Python files under `reference_examples/text_classification/agents/` and `reference_examples/terminal_bench_2/agents/`; generated runs write additional candidates there. Representational form: symbolic executable code plus embedded prose prompts. Lineage: authored baselines or proposer-generated variants derived from prior summaries, logs, trajectories, and hypotheses; import checks, smoke tests, and benchmark results validate them. Behavioral authority: system-definition artifacts with direct runtime authority, because they decide prediction, learning, retrieval, prompt construction, tools, command execution, and context summarization.

**Run-state summaries and candidate manifests.** Storage substrate: per-run `logs/<run>/pending_eval.json`, `frontier_val.json`, `evolution_summary.jsonl`, reports directories, and text-classification `summary.json`/`frontier.json` outputs. Representational form: symbolic JSON/JSONL records with prose hypotheses, change descriptions, axes/components, scores, context length, timing, and rollout metrics. Lineage: `pending_eval.json` is proposed by Claude; frontiers and summaries are derived by harness scripts from benchmark outputs and previous frontier state. Behavioral authority: ranking/evaluation artifacts for the outer loop and knowledge artifacts for the next proposer; they shape later candidate search by telling the proposer what has been tried and what currently wins.

**Evaluation traces and logs.** Storage substrate: text-classification `logs/<dataset>/<memory>/<model>/log.jsonl`, `memory.json`, `val.json`, result JSONs, Claude session logs under `claude_sessions`, and Terminal-Bench `jobs/<run>/<task>__<trial>/result.json` directories. Representational form: mixed prose, symbolic events, tool/file-read summaries, prompts, predictions, targets, rewards, token/cost metrics, and raw streamed Claude events. Lineage: trace-derived from proposer sessions, memory-system training/evaluation, and Harbor rollouts. Behavioral authority: knowledge/audit artifacts during inspection and system-definition inputs when the proposer skill tells agents to read failures, successful trajectories, frontier state, and prior summaries before writing new candidates.

**Benchmark and validation scripts.** Storage substrate: Python and shell scripts such as `benchmark.py`, `inner_loop.py`, `meta_harness.py`, and `scripts/run_eval.sh`. Representational form: symbolic executable orchestration logic. Lineage: authored framework code, with run arguments/config deciding concrete splits, models, concurrency, and trial counts. Behavioral authority: evaluation and enforcement artifacts: they decide which candidates are valid, which results count, how frontiers are computed, and whether held-out test results are exposed.

Promotion path: Meta-Harness has a strong trace-to-code promotion path. Raw proposer/evaluation traces and per-candidate scores become summaries and frontiers; proposer skills turn those retained artifacts into hypotheses and executable candidate files; benchmark scripts then either reject, rank, or preserve the candidates. The promotion crosses from knowledge artifacts into system-definition artifacts, but it is mediated by offline evaluation rather than by human review or a git-native approval gate.

## Comparison with Our System

| Dimension | Meta-Harness | Commonplace |
|---|---|---|
| Primary purpose | Optimize task-specific model harness code around a fixed model | Maintain an agent-operated methodology KB |
| Canonical retained artifact | Candidate Python harness, proposer skill, frontier summary, run trace | Typed Markdown notes, instructions, reviews, source snapshots, indexes |
| Learning loop | Proposer generates code from prior traces; benchmark ranks candidates | Agents and maintainers write/revise artifacts under collection/type contracts |
| Read-back | Explicit proposer reads of summaries, frontiers, logs, and trajectories | Explicit agent pull through `rg`, indexes, links, skills, and loaded instructions |
| Governance | Import checks, smoke tests, benchmark splits, anti-overfitting rules | Git diffs, frontmatter schemas, validators, semantic gates, replacement archives |
| Context efficiency | Measured via context length, token/cost metrics, prompt/scaffold changes | Managed through progressive disclosure, indexes, summaries, and explicit scope |

Meta-Harness is closer to an automated adaptation workbench than to a standing memory store. It treats traces and summaries as raw material for changing the executable harness, then uses evaluation to decide which changes survive. Commonplace treats retained artifacts as reviewable knowledge and system definitions in a repo; promotion is slower but easier to inspect, cite, invalidate, and revert.

The strongest overlap is the separation between workshop and durable authority. Meta-Harness keeps volatile candidate generation in `logs/`, `jobs/`, and generated `agents/` files until evaluation gives them standing. Commonplace has a workshop layer for in-flight artifacts and a library layer for durable notes/instructions; the difference is that Commonplace's promotion boundary is semantic review and validation, while Meta-Harness's boundary is benchmark performance.

The biggest divergence is what "learning" produces. In Meta-Harness, successful learning can produce arbitrary Python code with direct behavioral authority. In Commonplace, trace-derived learning should usually first produce candidate notes, reports, or review comments; stronger authority, such as skills or validators, needs an explicit promotion step.

**Read-back:** `pull` — The durable state is read by the proposer or harness through explicit file paths, skills, logs, frontiers, and evaluation scripts; I did not find relevance-gated pre-action memory injection into the acting solver

### Borrowable Ideas

**Use a candidate manifest as the handoff between generation and evaluation.** Ready now for review/workshop loops. A Commonplace analogue would be a small JSON/YAML manifest listing proposed notes, checks, hypotheses, and expected effects before validation or semantic review runs.

**Record evolution summaries as first-class learning traces.** Ready for long-running review campaigns. `evolution_summary.jsonl` is compact enough for a future proposer to scan without replaying every run; Commonplace review sweeps could benefit from similarly compact per-attempt result rows.

**Treat context footprint as a benchmark metric.** Ready now. Meta-Harness's Pareto treatment of accuracy versus context length maps directly to Commonplace retrieval experiments: a candidate route or index should be judged on usefulness and context cost together.

**Keep proposer policy in an inspectable skill.** Ready now. The `.claude/skills` files make search policy explicit and portable. Commonplace already uses skills; the borrowable point is to make anti-overfitting, prototype, and output-contract rules local to each experiment.

**Borrow benchmark promotion, not arbitrary code authority.** Needs a concrete use case. Commonplace could let agents generate candidate validators or routing scripts, but only behind tests, review, and an explicit authority upgrade; Meta-Harness's direct candidate-code search would be too high-authority for the KB library layer.

**Use onboarding as a pre-implementation gate.** Ready now. `ONBOARDING.md` is a good pattern for forcing task unit, fixed components, evaluation split, baselines, traces, and budget before an agent starts building.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
**Trace source:** `session-logs` `tool-traces` `event-streams` `trajectories` — proposer sessions, Claude session logs, streamed events, tool/file-read traces, benchmark runs, memory-system trajectories, and Terminal-Bench job outputs feed later candidate generation

**Learning scope:** `per-project` `cross-task` — retained state is scoped by reference experiment and run name, while candidate generation reads benchmark/job trajectories across tasks within that experiment

**Learning timing:** `offline` `staged` — candidates are proposed, checked, benchmarked, summarized, and then consumed by a later iteration

**Distilled form:** `prose` `symbolic` — hypotheses and reports are prose-bearing records, while frontiers, summaries, manifests, metrics, and candidate harnesses are symbolic files/code

**Trace source.** Meta-Harness qualifies as trace-derived because later candidate generation consumes durable records from prior proposer sessions, benchmark runs, memory-system trajectories, and Terminal-Bench job outputs. The text-classification skill explicitly tells the proposer to read `evolution_summary.jsonl`, `frontier_val.json`, `config.yaml`, and recent `log.jsonl` traces. The Terminal-Bench skill tells a subagent to deep-read failed and successful trajectories under `jobs/` and `logs/` before proposing a candidate.

**Extraction.** The extraction oracle is mixed. Scripts deterministically parse benchmark outputs into frontier and summary JSON records; Claude Code, constrained by proposer skills, interprets those records and trajectories into hypotheses and candidate code. Import checks, smoke tests, validation runs, and benchmark scores decide which generated artifacts are evaluated, ranked, or ignored.

**Four fields.** Raw traces are logs, job results, predictions, rewards, tool-call records, token/cost metrics, and session events: mixed prose/symbolic knowledge artifacts with audit value. Distilled artifacts are `frontier_val.json`, `evolution_summary.jsonl`, reports, and eventually candidate Python files: summaries are ranking/evaluation artifacts, while candidate files become executable system-definition artifacts. Proposer skills and benchmark scripts are authored system-definition artifacts that control how raw traces are interpreted.

**Scope and timing.** Scope is per reference experiment and per run name. Text classification isolates outputs under `logs/<run>/`; Terminal-Bench isolates `logs/<run>/` and `jobs/<run>/`. Timing is staged and offline: propose candidates, validate/import-check, benchmark, update frontier/summary, then let the next iteration read those retained artifacts.

**Survey placement.** Meta-Harness belongs in the trace-to-executable-harness family. It strengthens the survey claim that trace-derived learning can cross from advisory summaries into system-definition artifacts: the durable output is not merely a memory fact or note but runnable code that changes future model behavior under evaluation.

## Curiosity Pass

**"Memory system" is example-specific, not the whole framework.** The text-classification example searches `MemorySystem` implementations, but Terminal-Bench 2 searches a broader agent scaffold. The general mechanism is harness search, with memory as one possible harness component.

**The strongest memory is the experiment state, not a vector store.** Meta-Harness does not need a retrieval database to be a memory system. Its retained state is files: skills, candidate code, run logs, summaries, frontiers, and job results.

**The proposer receives paths more than preloaded evidence.** The outer loop builds prompts naming where logs, frontiers, reports, and pending manifests live. The proposer then follows skill instructions to read them. That is disciplined pull, not automatic relevance matching.

**Benchmark governance can still overfit.** The skills warn against task-specific hints and dataset-specific code, and the onboarding prompt calls out leakage. Those are important but mostly instruction-level controls; the repo does not make leakage impossible.

**The public repo is intentionally thinner than the paper artifact.** The README caveat matters: this is a runnable cleaned-up reference, while the optimized Terminal-Bench 2 harness lives elsewhere. Claims about end-to-end performance should be tied to the paper/artifact, not inferred from this source tree alone.

## What to Watch

- Whether future releases include the optimized Terminal-Bench 2 artifact inline; that would make candidate-code lineage and final harness authority easier to inspect in one repository.
- Whether generated candidate files gain structured provenance headers pointing to the exact summary rows, job ids, and trajectories that motivated them.
- Whether the onboarding flow grows a validator for `domain_spec.md`; that would turn the prose pre-implementation gate into a checkable system-definition artifact.
- Whether future examples add automatic leakage checks beyond proposer instructions, especially for datasets or task suites with near-duplicate examples.
- Whether trace summaries become compact enough to serve as reusable cross-run priors without re-reading large job directories.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Meta-Harness converts proposer/evaluation traces into summaries and executable harness candidates.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: retained run state matters only when the proposer or harness explicitly reads it.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Meta-Harness requires separating skills, candidate code, traces, summaries, frontiers, and benchmark scripts by substrate, form, lineage, and authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: candidate Python files, proposer skills, benchmark scripts, and onboarding gates configure or constrain future behavior.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: logs, trajectories, job results, reports, and summaries provide evidence for later candidate generation.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: prior runs become structured signal for later behavior-changing artifacts.
