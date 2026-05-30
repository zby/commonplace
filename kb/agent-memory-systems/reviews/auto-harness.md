---
description: "Minimal benchmark-driven coding-agent improvement loop with trace reading, mutable agent code, regression-suite promotion, result lineage, and learnings logs"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# auto-harness

auto-harness is NeoSigma's compact framework for running an autonomous coding agent against a benchmark, letting it inspect train failures, edit one harness agent file, gate the change, commit the winner, and repeat. The repo is intentionally small: `prepare.py` initializes the workspace and benchmark split, `benchmark.py` runs tau-bench, Terminal-Bench, or BIRD-Interact, `gating.py` enforces regression and held-out score gates, `record.py` appends iteration history, and `PROGRAM.md` tells the external coding agent how to operate.

**Repository:** https://github.com/neosigmaai/auto-harness

**Reviewed commit:** [de6b3ed51517909ff7a92466908e9ea161964865](https://github.com/neosigmaai/auto-harness/commit/de6b3ed51517909ff7a92466908e9ea161964865)

## Core Ideas

**The loop is encoded as agent instructions plus hard Python gates.** The README summarizes the loop as "run benchmark -> analyze -> improve agent/agent.py -> gate -> record -> update learnings -> repeat", and `PROGRAM.md` gives the coding agent the actual operating contract: run `benchmark.py`, inspect failing train traces, make one focused edit to `agent/agent.py`, run `gating.py`, commit after success, call `record.py`, and append to `workspace/learnings.md` ([README.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/README.md), [program_templates/base.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/program_templates/base.md)). The prose program is a system-definition artifact because the external agent consumes it as instruction; the Python gate is a stronger system-definition artifact because it enforces which edits can survive.

**The durable behavior surface is deliberately narrow.** `prepare.py` copies a benchmark-specific starting template into `agent/agent.py`, and the program tells the coding agent that it owns only `agent/agent.py` plus the ignored `workspace/learnings.md` log ([prepare.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/prepare.py), [agent/templates](https://github.com/neosigmaai/auto-harness/tree/de6b3ed51517909ff7a92466908e9ea161964865/agent/templates), [program_templates/base.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/program_templates/base.md)). The optimized agent file is not a memory record in the usual sense; it is executable or prompt-coded retained behavior. That makes it a system-definition artifact with direct instruction and execution authority over the next benchmark run.

**Benchmark outputs are split into train evidence and held-out gates.** `benchmark.py` records task rewards, saves `workspace/train_results.json`, and for Terminal-Bench and BIRD-Interact copies train traces into `workspace/traces/latest/` while preserving first-run traces under `workspace/traces/baseline/` ([benchmark.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/benchmark.py)). Terminal-Bench explicitly disables trace saving outside the train split with `HARNESS_SAVE_TRACE=0`, and the Terminal-Bench program tells the agent not to read raw job directories because they may contain test data ([benchmark.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/benchmark.py), [program_templates/terminal_bench.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/program_templates/terminal_bench.md)). The traces and train results are knowledge artifacts: they supply evidence and context for diagnosis, but they do not bind future behavior until distilled into code, prompt, suite, or instructions.

**The regression suite is mutable benchmark memory with validation force.** `workspace/suite.json` stores task IDs, a pass-rate threshold, and last results. `gating.py` reruns the suite, runs the full gate split, and only after both pass reruns previously failing train tasks and promotes newly passing ones into the suite ([gating.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/gating.py)). This is a compact form of trace-derived system memory: a previously failed task becomes a retained validator that future iterations must keep satisfying. It is symbolic rather than prose, and its behavioral authority is enforcement.

**Lineage is iteration-level, not fragment-level.** `record.py` appends `iteration`, `val_score`, short git commit, eval counts, and timestamp into `workspace/results.tsv`; the program requires the agent to commit `agent/agent.py` after a passing gate before recording the row ([record.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/record.py), [program_templates/base.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/program_templates/base.md)). This gives a clear chain from committed agent file to score row, but the changed prompt sentence or code branch inside `agent/agent.py` does not carry local provenance back to a specific trace or failure pattern.

**The file guard protects the small-loop premise.** `gating.py` rejects tracked changes outside `agent/agent.py` and generated `PROGRAM.md`, while `.gitignore` keeps `workspace/`, local experiment config, data, and benchmark clones out of tracked diffs ([gating.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/gating.py), [.gitignore](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/.gitignore)). This is an unusually clean authority boundary: the agent can learn by editing its own harness and work log, but cannot quietly mutate the benchmark machinery that judges it.

## Comparison with Our System

| Dimension | auto-harness | Commonplace |
|---|---|---|
| Primary retained state | `agent/agent.py`, `workspace/suite.json`, `workspace/learnings.md`, `workspace/results.tsv`, train traces | Typed markdown notes, reviews, instructions, sources, validation outputs, generated indexes |
| Source signal | Benchmark rewards, train traces, failed tasks, gate outcomes | Source snapshots, human and agent notes, review outputs, validation and workflow traces |
| Distilled artifacts | Mutated agent code/prompt, regression suite, learnings log, commits | Notes, instructions, skills, validation scripts, indexes, review decisions |
| Behavioral authority | Gate enforces suite and held-out score; agent file controls next run | Type contracts, instructions, validators, review gates, and authored links shape later agents |
| Lineage | Iteration rows plus git commits; trace directories for train evidence | Git history, frontmatter, source links, review records, generated-index provenance |
| Activation | The next benchmark run imports the evolved agent and gate suite | Agent navigation, skill loading, validation, and instruction loading activate retained artifacts |

auto-harness is narrower than commonplace and stronger inside that narrow domain. It does not try to build a general knowledge base, source library, or multi-type artifact system. It asks one empirical question: did this coding-agent harness change improve benchmark score without regressing protected tasks? That hard oracle lets it promote behavior with much less interpretive overhead than commonplace review workflows.

Commonplace has a richer artifact contract. auto-harness distinguishes practical surfaces through file ownership and commands, but it does not explicitly type knowledge artifacts, system-definition artifacts, lineage, review status, or promotion level. The distinction still exists in the implementation: traces and learnings advise, `PROGRAM.md` instructs, `gating.py` enforces, `suite.json` validates, `agent/agent.py` executes, and `results.tsv` audits.

The largest design contrast is library versus workshop. auto-harness is mostly a workshop: ignored runtime state, evolving code, temporary traces, and score rows around one benchmark. The only durable public methodology is the scaffold itself. Commonplace tries to accumulate reusable claims and procedures across tasks; auto-harness accumulates benchmark pressure into one mutable agent file.

**Read-back:** push — the next benchmark run imports the evolved agent and gate suite without an agent lookup.

## Borrowable Ideas

**Treat regression-suite promotion as memory promotion.** Ready to borrow where commonplace has executable checks. A fixed task that enters `suite.json` becomes durable memory with enforcement authority. For KB work, the analogue is promoting a discovered failure mode into a validator, review check, or small eval rather than only writing a lesson.

**Keep the optimized surface small.** Ready to borrow. auto-harness makes the learning target obvious: `agent/agent.py` changes, infrastructure does not. Commonplace trace-mining or skill-improvement loops should similarly define the exact files a worker may change before giving the worker autonomy.

**Separate train evidence from held-out judgment.** Ready to borrow for any benchmark-backed KB workflow. The system copies train traces for diagnosis while trying to keep test traces unavailable to the agent. Commonplace review bundles could use the same distinction: evidence for revision is not the same as evidence for final judgment.

**Record score lineage next to commit lineage.** Ready to borrow for code and validation loops. `results.tsv` is plain, cheap, and sufficient to connect each accepted iteration to a commit and score. Commonplace already has git history; adding compact outcome rows for repeated eval loops would make behavioral progress easier to audit.

**Do not borrow the narrow artifact model for general KB maintenance.** auto-harness works because one file can own most behavior and a benchmark can judge it. Commonplace's notes and instructions often shape future behavior indirectly, so a single score gate would hide too many quality dimensions.

## Trace-derived learning placement

**Trace source.** auto-harness qualifies as trace-derived learning. The source traces are train-split benchmark runs: Terminal-Bench conversation/tool traces and results copied from Harbor output, BIRD-Interact dialogue/tool/ADK event traces, tau-bench per-task simulation rewards, and the aggregate train/test reward tables produced by `benchmark.py` ([benchmark.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/benchmark.py)).

**Extraction.** Extraction is mostly performed by the external coding agent under `PROGRAM.md`: read failed train traces, identify failure patterns, update `workspace/learnings.md`, and edit `agent/agent.py` ([program_templates/base.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/program_templates/base.md)). The hard oracle is the gate: regression-suite pass rate and held-out `val_score` decide whether the proposed behavior survives ([gating.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/gating.py)). There is no separate LLM debugger or structured root-cause schema in the inspected implementation.

**Storage substrate.** Raw and copied traces live under ignored `workspace/traces/`; train results live in `workspace/train_results.json`; the regression suite lives in `workspace/suite.json`; learnings live in `workspace/learnings.md`; score lineage lives in `workspace/results.tsv`; durable behavior lives in tracked `agent/agent.py` and git commits. Benchmark templates and program templates live in tracked source files, but runtime workspace state is intentionally ignored ([.gitignore](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/.gitignore)).

**Representational form.** The raw trace layer is mixed: JSON messages, tool calls, dialogue histories, ADK events, result JSON, and scalar rewards. `workspace/learnings.md` is prose. `workspace/suite.json` and `workspace/results.tsv` are symbolic operational records. `agent/agent.py` is executable symbolic code with embedded prose prompts. No inspected path trains model weights, embeddings, adapters, rankers, or controllers.

**Lineage.** Lineage is good at the iteration level: accepted behavior is committed, `results.tsv` records the commit and score, `suite.json` records protected tasks, and train traces remain available for the latest and baseline runs. Lineage is weak at the fine-grained artifact level: a line in `agent/agent.py` or `learnings.md` does not carry a source trace ID, derivation rule, invalidation rule, or confidence status.

**Behavioral authority.** Raw traces, train results, and learnings are knowledge artifacts when consumed as evidence, context, or advice. `PROGRAM.md` and benchmark-specific program supplements are system-definition artifacts because they instruct the coding agent. `gating.py`, `suite.json`, and thresholds are system-definition artifacts because they validate and enforce. `agent/agent.py` is a system-definition artifact because the benchmark imports and executes it as the future agent.

**Scope and timing.** Scope is per-repo and per-configured benchmark. Timing is staged offline: run benchmark, inspect traces, edit retained behavior, gate, commit, record, repeat. The system is not online self-modification inside a single task, and it does not include a cross-project memory library.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), auto-harness belongs with outer-loop artifact-learning systems. It strengthens the survey claim that the most behaviorally important output of trace-derived learning is often not a memory note, but a system-definition artifact such as code, prompt, regression test, or gate. It also shows the minimal version of that pattern: no rich debugger, no vector memory, no taxonomy, just trace evidence, one mutable agent file, a promoted regression suite, and a held-out score gate.

## Curiosity Pass

**The self-maintained eval suite is partly automated, not fully agent-curated.** The README says the coding agent self-maintains the eval suite, but the inspected gate promotes newly fixed previously failing train tasks automatically after both gates pass ([README.md](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/README.md), [gating.py](https://github.com/neosigmaai/auto-harness/blob/de6b3ed51517909ff7a92466908e9ea161964865/gating.py)). The agent's role is to create behavior that fixes tasks; the suite update itself is deterministic gate logic.

**The learnings log is memory, but not an enforcement surface.** `workspace/learnings.md` can shape later iterations if the coding agent reads it, but the gate does not parse or validate it. It is a knowledge artifact unless manually transformed into prompt/code changes or a gate.

**The main learned artifact can become opaque quickly.** Repeated direct edits to `agent/agent.py` are powerful and easy to activate, but they can accumulate behavior without typed provenance. After enough iterations, the code may pass gates while becoming harder to explain than a set of separately reviewed lessons, tests, and patches.

**The held-out gate is unusually strong for a tiny system.** The full test split must meet or exceed the best recorded score, and Step 2 runs even when the regression suite fails. That creates useful signal, but it also means benchmark choice dominates the learning target.

**The public checkout demonstrates machinery more than accumulated runs.** The repo contains templates and loop code, not a checked-in corpus of completed workspaces, traces, suites, and result histories. The reviewable system is the scaffold for trace-derived learning, not a reusable library of distilled auto-harness experience.

## What to Watch

- Whether future versions add structured change manifests connecting each edit to failure patterns, predicted improvements, and risk tasks.
- Whether `workspace/learnings.md` becomes parseable or promotable into prompts, tests, or reusable skills rather than staying a free-form log.
- Whether suite promotion gains richer policies, such as task clustering, anti-overfitting limits, or retirement of brittle tasks.
- Whether the loop expands from one mutable file to multiple typed behavior surfaces without losing the current file-guard clarity.
- Whether recorded experiments are published, making score lineage and learned artifacts inspectable rather than only generated locally.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - source-inspected instance: auto-harness turns benchmark traces and task outcomes into edited agent code plus a promoted regression suite
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - supports: failure traces become signal for improving future agent behavior
- [Activate behavior-changing memory](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies: learned behavior activates by importing the next `agent/agent.py`, not by ad hoc retrieval
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - compares-with: auto-harness is mostly workshop state around a benchmark loop
- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: traces, train results, and learnings advise later iterations
- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `PROGRAM.md`, `gating.py`, `suite.json`, thresholds, and `agent/agent.py` instruct or enforce behavior
- [Agentic Harness Engineering](./agentic-harness-engineering.md) - compares-with: both improve coding-agent harness behavior from benchmark feedback, but AHE adds richer trace analysis, manifests, and component surfaces
- [Meta-Harness](./meta-harness.md) - compares-with: both optimize harness artifacts through benchmark pressure, with auto-harness representing a smaller hard-oracle loop
