---
description: "auto-harness review: benchmark-driven coding-agent loop that mines train traces, evolves agent.py, promotes evals, and gates changes"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
last-checked: "2026-06-04"
---

# auto-harness

`neosigmaai/auto-harness` is a benchmark optimization harness for autonomous coding agents. It gives the agent a generated `PROGRAM.md`, a benchmark-specific starting `agent/agent.py`, train traces, a persistent learnings log, an automatically promoted regression suite, and a gate that rejects non-improving or out-of-scope edits. The reviewed commit is `de6b3ed51517909ff7a92466908e9ea161964865`.

**Repository:** https://github.com/neosigmaai/auto-harness

**Reviewed commit:** [de6b3ed51517909ff7a92466908e9ea161964865](https://github.com/neosigmaai/auto-harness/commit/de6b3ed51517909ff7a92466908e9ea161964865)

**Last checked:** 2026-06-04

## Core Ideas

**The harness externalizes the agent-improvement loop as a program file.** `prepare.py` composes `PROGRAM.md` from `program_templates/base.md` plus a benchmark-specific supplement, then copies the selected starting agent template into `agent/agent.py` ([prepare.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/prepare.py), [program_templates/base.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/program_templates/base.md)). The human prompt is deliberately small: point a coding agent at the repo and tell it to read `PROGRAM.md`.

**The retained behavior target is source code, not a memory database.** The coding agent owns `agent/agent.py`; benchmark runners import `HarnessAgent` from that file, so every accepted code or prompt change becomes the next agent version ([README.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/README.md), [benchmark.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/benchmark.py)). The memory system is therefore a learning harness around an editable agent artifact, not a standalone retrieval service.

**Train traces are exposed, test traces are structurally withheld.** Terminal-Bench train runs copy `trace.json` and `result.json` into `workspace/traces/latest/` and preserve first-run copies under `workspace/traces/baseline/`; non-train or baseline runs set `HARNESS_SAVE_TRACE=0` to prevent test-trace leakage ([benchmark.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/benchmark.py), [agent/templates/terminal_bench.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/agent/templates/terminal_bench.py)). BIRD-Interact similarly writes train dialogue history, tool trajectories, ADK events, and results to `workspace/traces/latest/` ([benchmark.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/benchmark.py)).

**The gate turns benchmark evidence into hard update control.** `gating.py` first rejects tracked edits outside `agent/agent.py` and generated `PROGRAM.md`, then requires the regression suite to pass, then requires full test `val_score` to meet or beat the best score in `workspace/results.tsv`; only after both gates pass does it promote newly fixed train failures into `workspace/suite.json` ([gating.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/gating.py)). `record.py` repeats the file guard against the last commit before appending an iteration row, closing an obvious bypass ([record.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/record.py)).

**Context efficiency is workspace-scoped trace selection plus accumulated summaries.** The coding agent is instructed to read failing train traces and `workspace/train_results.json`, not every benchmark artifact or test output; Terminal-Bench guidance explicitly says to read only `workspace/traces/latest/`, not raw job directories that may contain test data ([program_templates/base.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/program_templates/base.md), [program_templates/terminal_bench.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/program_templates/terminal_bench.md)). The complexity control is procedural and directory-based rather than search-based: raw traces remain available, while `workspace/learnings.md`, `workspace/suite.json`, and accepted `agent.py` commits are the compressed surfaces meant to steer later iterations.

**Adoption is CLI-and-git native.** The repo avoids a hosted service: users configure `experiment_config.yaml`, run `prepare.py`, then let a normal coding agent use Python scripts, git commits, workspace files, and benchmark CLIs ([README.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/README.md), [experiment_config.yaml.template](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/experiment_config.yaml.template)). That makes state inspectable and revertible, but also means the coding agent's compliance with the program file is supplied by the host agent, not enforced by a wrapper around every model call.

## Artifact analysis

- **Storage substrate:** `files` — The standing retained state is a repository and gitignored workspace file tree: program templates, `PROGRAM.md`, `agent/agent.py`, `workspace/learnings.md`, `workspace/suite.json`, `workspace/results.tsv`, `workspace/train_results.json`, and copied train traces.
- **Representational form:** `prose` `symbolic` — `PROGRAM.md`, benchmark supplements, learnings, prompts, and traces are prose-heavy; Python runners, JSON/TSV workspace files, task ids, git commits, thresholds, and file guards are symbolic.
- **Lineage:** `authored` `trace-extracted` — Program templates, infrastructure, and starting agent templates are authored; traces, train/test results, suite promotions, learnings entries, and accepted agent changes derive from benchmark runs and coding-agent iterations.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `validation` `learning` — Traces and learnings advise the coding agent; `PROGRAM.md` instructs the loop; file guards and benchmark gates enforce allowed edits and score constraints; the suite and test split validate changes; the overall loop learns improved agent behavior from failures.

**Program and benchmark supplements.** Storage substrate is Markdown files in `program_templates/` plus generated `PROGRAM.md`. Representational form is prose with symbolic command names, file roles, loop steps, and forbidden-action lists. Lineage is authored infrastructure copied by `prepare.py`. Behavioral authority is instruction: it tells the coding agent which files it owns, which traces it may read, how to gate, when to record, and when to stop.

**Evolving agent file.** Storage substrate is `agent/agent.py`, copied from `agent/templates/{benchmark}.py` and then modified by the coding agent. Representational form is symbolic Python code plus embedded prompt prose. Lineage starts as authored template code and becomes trace-derived through iterative edits made after failure analysis. Behavioral authority is instruction and execution authority: benchmark runners import this file as the agent under evaluation.

**Raw train traces and results.** Storage substrate is `workspace/traces/latest/`, `workspace/traces/baseline/`, and `workspace/train_results.json`. Representational form is symbolic JSON containing prose conversations, tool calls, rewards, and benchmark metadata. Lineage is trace-extracted from train benchmark runs; test traces are not copied into the readable workspace path. Behavioral authority is knowledge and learning evidence for later failure analysis, not a direct runtime prompt for the benchmark agent.

**Learnings log.** Storage substrate is `workspace/learnings.md`. Representational form is prose structured by iteration headings and fields such as what changed, pattern confirmed, what worked, and needs from human. Lineage is trace-derived distillation by the coding agent after each pass or failure. Behavioral authority is knowledge and soft instruction for subsequent iterations; the file can shape hypotheses but does not itself gate a change.

**Regression suite and score history.** Storage substrate is `workspace/suite.json` and `workspace/results.tsv`. Representational form is symbolic task ids, thresholds, last results, scores, commits, and timestamps. Lineage is trace-extracted from benchmark outcomes and accepted iterations. Behavioral authority is validation and enforcement: `gating.py` reruns suite tasks, compares test score against prior best, and promotes newly fixed failures into the suite.

**Gate and record scripts.** Storage substrate is repository Python files. Representational form is symbolic code. Lineage is authored infrastructure. Behavioral authority is enforcement and validation: `gating.py` returns failure on out-of-scope edits or score regression, while `record.py` refuses to append results if the committed diff touched forbidden tracked files.

Promotion path: raw train traces and benchmark results are read by the coding agent, distilled into `workspace/learnings.md` and edits to `agent/agent.py`, accepted only if the gate passes, then partially codified into `workspace/suite.json` when newly fixed failures become regression obligations. The path crosses from knowledge evidence to executable agent behavior and validation state, but it does not attach per-change source spans from traces to the resulting code.

## Comparison with Our System

| Dimension | auto-harness | Commonplace |
|---|---|---|
| Primary purpose | Improve a benchmark agent through autonomous code edits | Maintain a typed methodology KB for agents and maintainers |
| Main retained artifact | `agent/agent.py`, `workspace/learnings.md`, train traces, suite, results history | Typed Markdown notes, reviews, instructions, source snapshots, indexes, and validators |
| Write path | Coding agent mines train failures, edits code, logs learnings, and passes gates | Human/agent authors write artifacts under collection/type contracts and review gates |
| Read-back | Program and accumulated workspace files are read by the coding agent between iterations | Search, indexes, links, skills, loaded instructions, and review reports |
| Governance | File guard, regression suite, test-score gate, commit history, anti-test-trace copying | Frontmatter schemas, link checks, source citations, review bundles, generated indexes |

The closest Commonplace analogue is not a note-writing workflow but a self-improving skill or command loop. Auto Harness has a stronger closed-loop enforcement path: benchmark outcomes can automatically block a code change and promote new regression obligations. Commonplace's review and validation loops are more source-grounded and auditable, but most improvement remains agent- or maintainer-mediated rather than benchmark-driven.

The main tradeoff is evaluability versus transferability. Auto Harness works because a benchmark supplies scalar rewards, train/test splits, and traces. Commonplace artifacts often lack that clean oracle; validation can catch structure and link health, but semantic quality is harder to reduce to a score without narrowing the task.

Auto Harness also exposes a useful anti-cheating pattern. It does not merely tell the agent to avoid test data; the Terminal-Bench runner disables trace saving outside the train split, and the program narrows the readable trace path. Commonplace has analogous source and review boundaries, but fewer mechanisms that remove tempting evidence from the agent's filesystem.

### Borrowable Ideas

**Gate promotion from repeated failures into durable regression obligations.** Ready for command and review workflows. Commonplace could promote fixed validator or review-bundle failures into a small regression set for the responsible command, instead of relying only on broad test suites.

**Keep train evidence and held-out evidence structurally separate.** Ready now for review workflows that use examples. A Commonplace benchmark or review gate should expose only allowed traces to the drafting agent and keep held-out cases outside the normal navigation path.

**Use a learnings log as a low-authority bridge before codification.** Ready for workshops. `workspace/learnings.md` is a useful intermediate surface: cheaper than a note, but persistent enough for repeated agent iterations. Commonplace's workshop layer could use this pattern before promoting stable findings into instructions or notes.

**Pair file ownership instructions with an executable file guard.** Ready for agent-run scripts. Auto Harness makes "only edit these files" a gate condition rather than a reminder. Commonplace already has validation; narrower workflow-specific file guards would reduce accidental artifact churn.

**Do not borrow scalar-score gating where the oracle is weak.** Needs a concrete benchmark. Auto Harness' strongest mechanism depends on reliable rewards. Applying the same loop to open-ended KB writing without a defensible oracle would reward proxy gaming.

## Write side

**Write agency:** `automatic` `manual` — Infrastructure automatically initializes workspace files, copies templates, records results, copies train traces, checks gates, and promotes suite tasks; the coding agent automatically edits `agent/agent.py` and appends `workspace/learnings.md`; humans still configure the experiment and may inspect or steer the loop.

**Curation operations:** `consolidate` `evolve` `synthesize` `promote` — The loop consolidates failure evidence into learnings, evolves `agent/agent.py` in place across iterations, synthesizes new prompt/tool/code hypotheses from traces, and promotes newly fixed failures into the regression suite. It does not implement durable contradiction invalidation, duplicate merging, or age-based decay.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `trajectories` — Terminal-Bench saves full conversation messages and bash tool calls for train runs; BIRD-Interact saves dialogue history, tool trajectories, ADK events, final responses, and result metadata; benchmark outputs record task rewards and timeouts.

**Learning scope:** `per-project` `cross-task` — The retained changes are scoped to the configured benchmark experiment but are reused across many tasks in the train/test split.

**Learning timing:** `online` `staged` — The loop learns after each benchmark/gate cycle: run, inspect failures, edit, gate, record, update learnings, repeat.

**Distilled form:** `prose` `symbolic` — Distillation produces prose learnings and symbolic Python agent changes, suite JSON, result TSV rows, and commits.

**Trace source.** The qualifying raw traces are not generic application logs; they are task execution records produced by the evaluated agent. Terminal-Bench copies only train `trace.json` and `result.json` into `workspace/traces/`, and BIRD-Interact creates trace payloads from dialogue, tool trajectory, ADK events, and final response.

**Extraction.** Extraction is partly procedural and partly delegated to the coding agent. Deterministic scripts compute per-task rewards, copy allowed traces, save train results, and promote newly fixed failures. The coding agent is the abstraction oracle for diagnosing failure modes, choosing a code/prompt change, and writing `workspace/learnings.md`; benchmark gates decide whether that distilled change survives.

**Scope and timing.** The learning loop is project-local: one configured benchmark, one `agent/agent.py`, one workspace, and one score history. Timing is staged by explicit CLI calls rather than a background daemon. The system can iterate overnight, but each durable update happens at a visible boundary: benchmark output, gate result, commit, record row, and learnings entry.

**Survey placement.** Auto Harness is a trace-to-code-and-eval-suite system. It strengthens the survey claim that trace-derived learning becomes safer when raw traces are separated from higher-authority distilled artifacts and when promotion has an external oracle. It also shows a higher-authority branch than prose playbooks: accepted learnings can become executable code and regression requirements.

## Read-back

**Read-back:** `both` — The coding agent deliberately pulls traces, results, and learnings while following `PROGRAM.md`, while generated `PROGRAM.md` and benchmark supplements are pushed as ambient loop instructions when the human starts the agent with "read PROGRAM.md"; the benchmark agent itself receives retained changes because `benchmark.py` imports the current `agent/agent.py`.

**Read-back signal:** `coarse` `identifier` — `PROGRAM.md` is coarse always-load loop context; benchmark-specific supplements, task ids, split names, and trace paths provide identifier-scoped selection for which files and tasks to inspect.

**Faithfulness tested:** `yes` — The harness does not test whether the coding agent read a specific `learnings.md` paragraph, but it does test the behavioral consequence of retained agent changes through regression-suite and full-test gates before recording an iteration.

**Direction edge cases.** From the coding agent's perspective, trace inspection is pull: `PROGRAM.md` tells it to read failing train traces, and it chooses files under `workspace/traces/latest/`. The generated program itself is push-like because the human prompt and repo layout make it ambient instruction for the optimization loop. For the evaluated benchmark agent, accepted edits to `agent/agent.py` are pushed by import: the runner loads the current code before each task.

**Targeting and signal.** Most read-back is coarse at the loop level: read the program, inspect workspace state, run the configured benchmark. Instance-level selection is by identifiers already present in the system: task ids, train/test split names, benchmark names, trace directory names, and suite task lists. There is no embedding, lexical search, or LLM relevance router in the harness itself.

**Injection point.** Read-back happens before the next coding-agent action or benchmark-agent invocation. The coding agent reads program/workspace files before editing; benchmark runners import `agent/agent.py` before task execution; gate scripts load suite/results before deciding whether the current change survives. Post-run trace copying, suite promotion, and result recording are write-side maintenance.

**Selection, scope, and complexity.** Selection is file- and task-level. The harness narrows the agent's inspection surface to train traces and workspace files, but it does not budget trace tokens or summarize automatically before the coding agent reads them. Complexity can still grow with trace volume and `learnings.md`; the current control is path discipline plus iterative summaries, not retrieval scoring.

**Authority at consumption.** `PROGRAM.md` has instruction authority over the coding agent. Train traces and learnings have advisory knowledge authority. `agent/agent.py` has executable authority for benchmark runs. `workspace/suite.json` and `workspace/results.tsv` have validation authority inside `gating.py`.

**Faithfulness.** The harness tests retained agent behavior indirectly: a code or prompt change must pass suite and full-test gates, and `record.py` records the accepted commit. It does not ablate individual learnings entries, trace reads, or prompt clauses, so faithfulness of those smaller memory units is not separately measured.

**Other consumers.** Human operators inspect `workspace/results.tsv`, `workspace/learnings.md`, diffs against templates, gate output, and benchmark summaries. The same retained state is therefore both agent memory and experiment audit trail.

## Curiosity Pass

**The "self-maintained eval suite" is automatic but narrow.** `gating.py` promotes newly fixed previously-failing train tasks after a successful gate; the coding agent does not author rich eval cases or assertions. The suite is a task-id list plus threshold, not a semantic test specification.

**The loop relies on the host coding agent honoring `PROGRAM.md`.** File guards catch tracked infrastructure edits, but they cannot force the agent to append a high-quality learning, inspect the right trace deeply, or make exactly one hypothesis per iteration.

**Test protection is strongest for Terminal-Bench traces.** The code explicitly disables trace saving for non-train Terminal-Bench runs and copies only train traces into the recommended workspace path. The same broad principle appears for BIRD-Interact copied traces, but tau-bench trace availability is mostly described in program guidance rather than a visible copied-trace implementation at this commit.

**The gate rewards monotonic test score, which can be brittle.** Requiring the current test score to meet or exceed best-so-far is simple and useful, but stochastic benchmarks or model variance could reject beneficial changes unless users control seeds and concurrency carefully.

**The memory store is intentionally disposable.** `workspace/` is gitignored, while accepted `agent.py` commits and `results.tsv` rows carry the durable experiment history. That split is practical for overnight optimization, but weak if a later auditor needs exact trace-to-code lineage.

## What to Watch

- Whether future versions attach accepted `agent.py` changes to the specific failing trace ids and learnings entries that motivated them; that would make trace-derived code evolution auditable.
- Whether the harness adds automatic summarization or clustering of trace failures before the coding agent reads them; that would change context efficiency from path scoping to real consolidation.
- Whether suite promotion gains richer metadata such as failure class, source iteration, or expected behavior; that would move `suite.json` from a task list toward a reviewable validation artifact.
- Whether stochastic score handling appears, such as repeated gate runs, confidence intervals, or seed rotation; that would make the monotonic score gate less brittle.
- Whether the file guard expands to untracked or gitignored workspace policy for workflows where workspace artifacts themselves become high-authority retained state.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Auto Harness derives learnings, code changes, and regression obligations from benchmark traces and outcomes.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: workspace files affect later action only when the coding agent or gate reads them.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Auto Harness bundles traces, code, instructions, suite state, and gates with different forms and authorities.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: repeated task failures become future agent behavior through iterative edits and suite promotion.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: traces, results, and learnings advise later diagnosis and editing.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `PROGRAM.md`, `agent/agent.py`, `gating.py`, and `workspace/suite.json` carry instruction, execution, and validation force.
