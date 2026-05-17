---
description: "Stanford IRIS Lab framework for trace-derived harness optimization with onboarding specs, Claude-proposed candidate files, benchmark gates, and frontier artifacts"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-05-16"
---

# Meta-Harness

Meta-Harness is Stanford IRIS Lab's framework for optimizing task-specific model harnesses while keeping the base model fixed. The public repository packages an onboarding prompt for new domains plus two reference experiments: text-classification memory-system search and Terminal-Bench 2 scaffold evolution. Its memory-system relevance is direct: it learns from prior task runs, proposer-session logs, and benchmark outcomes by generating new candidate harness files, validating them, evaluating them, and retaining frontier summaries.

**Repository:** https://github.com/stanford-iris-lab/meta-harness

**Reviewed commit:** [95175f70c758dd1145b395edfe8b67e6f9d80fbd](https://github.com/stanford-iris-lab/meta-harness/commit/95175f70c758dd1145b395edfe8b67e6f9d80fbd)

## Core Ideas

**Onboarding turns a new domain into a harness-search spec before implementation.** `ONBOARDING.md` is an agent prompt, not runtime code. It asks the assistant to produce a `domain_spec.md` only after the task unit, fixed base model, mutable harness boundary, evaluation split, leakage risk, baselines, offline traces, online traces, and budget are known ([ONBOARDING.md](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/ONBOARDING.md)). This is a system-definition artifact with instruction authority over setup conversations. It does not enforce the spec mechanically, but it does force the important context-engineering questions up front: what can change, what judges it, and what retained experience is available.

**The reusable framework is mostly an example pattern, not a shared library.** The root README says the repo contains the framework and two reference experiments, but the implementation lives as two separate example directories with their own `meta_harness.py`, `claude_wrapper.py`, skill prompt, manifests, and evaluator scripts ([README.md](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/README.md), [reference_examples/text_classification](https://github.com/stanford-iris-lab/meta-harness/tree/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification), [reference_examples/terminal_bench_2](https://github.com/stanford-iris-lab/meta-harness/tree/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2)). There is no central Python package exporting a generic optimizer. The reusable part is the scaffold pattern: define a candidate interface, use Claude Code as proposer, write candidate files, import-check and smoke-test them, benchmark them, and update frontier/history files.

**Text classification searches over `MemorySystem` subclasses.** The text example defines an abstract `MemorySystem` with `predict`, `learn_from_batch`, `get_state`, and `set_state`, then has `inner_loop.py` run online or offline learning, save `memory.json`, write structured `log.jsonl`, and emit val/test result JSON ([memory_system.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/memory_system.py), [inner_loop.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/inner_loop.py)). `meta_harness.py` runs baselines, calls Claude Code with the `meta-harness` skill, validates proposed modules by importing them, evaluates them through `benchmark.py`, and appends `evolution_summary.jsonl` rows with hypothesis, axis, score delta, components, and timing ([meta_harness.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/meta_harness.py), [benchmark.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/benchmark.py)). The learned artifact is a Python memory-system file under `agents/`, not a free-floating note.

**The proposer-agent skills encode search discipline.** The text-classification proposer skill requires exactly three candidates per iteration, post-eval reports, trace reading, `/tmp` prototypes, candidate import checks, and a `pending_eval.json` handoff; it explicitly rejects mere parameter sweeps and dataset-specific hints ([text skill](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md)). The Terminal-Bench skill similarly requires one new `AgentHarness` file, analysis of failed and successful trajectories, general-purpose changes, import validation, and a `pending_eval.json` with hypothesis and expected efficiency ([Terminal-Bench skill](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md)). These are strong system-definition artifacts: they shape what the proposer may write and what metadata must accompany candidates.

**Terminal-Bench evolves executable scaffolds around Harbor.** The Terminal-Bench example starts from `baseline_kira.py`, a `Terminus2` subclass that changes the tool-calling interface, command execution, completion confirmation, output limits, image reading, and trajectory recording ([baseline_kira.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/agents/baseline_kira.py)). Its `meta_harness.py` runs Harbor jobs, parses per-trial `result.json` files, extracts pass rates, rollout cost/turn metrics, validates candidate imports, optionally runs a smoke task, benchmarks valid candidates, and updates `frontier_val.json` plus `evolution_summary.jsonl` ([Terminal-Bench meta_harness.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/meta_harness.py), [run_eval.sh](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/scripts/run_eval.sh)). The retained behavior surface is an `agents/<name>.py` file and optional prompt template, loaded later as `agents.<name>:AgentHarness`.

**The raw and derived run artifacts are deliberately different surfaces.** Raw traces and observations appear as training logs, trajectories, per-trial Harbor job directories, proposer-session logs, and result JSON. Derived artifacts include `pending_eval.json`, `frontier_val.json`, `frontier.json`, `evolution_summary.jsonl`, `summary.json`, post-eval reports, candidate Python files, saved memory states, and test results ([text benchmark.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/benchmark.py), [text claude_wrapper.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/text_classification/claude_wrapper.py), [Terminal-Bench meta_harness.py](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/reference_examples/terminal_bench_2/meta_harness.py)). The checked-out repo contains machinery for these artifacts, but no completed experiment corpus; the code-grounded review should treat Meta-Harness as a runnable optimizer scaffold, not as an included library of evolved harnesses.

## Comparison with Our System

| Dimension | Meta-Harness | Commonplace |
|---|---|---|
| Primary retained state | Candidate Python harness files, memory states, logs, frontiers, summaries, proposer-session records | Typed markdown notes, source snapshots, instructions, indexes, validation outputs, review records |
| Source signal | Offline examples, online prediction traces, Harbor trajectories, verifier rewards, proposer logs, benchmark scores | Source snapshots, agent/human notes, review bundles, validation output, work traces |
| Distilled artifacts | Candidate `agents/*.py`, prompt templates, `pending_eval.json`, `frontier_val.json`, `evolution_summary.jsonl`, reports | Notes, reviews, instructions, skills, commands, schemas, indexes |
| Behavioral authority | Candidate files execute; skills instruct proposer; import/smoke/benchmark gates validate; frontiers rank | Type contracts, instructions, validators, authored links, review gates, and generated indexes shape later agents |
| Lineage | Run-name directories, candidate metadata, score rows, proposer session logs, job/result paths | Git history, frontmatter, source links, generated-index provenance, review/gate records |
| Activation | Next evaluation imports the winning candidate class or memory system | Agents load instructions, notes, skills, and validators through navigation and workflow conventions |

Meta-Harness is narrower than commonplace but has a harder feedback loop. It only works where a domain can supply repeated tasks, a candidate harness interface, and a measurable search/held-out split. Within that boundary, it can make stronger promotion decisions than ordinary note review because candidate behavior is imported and evaluated.

Commonplace has the richer artifact contract. Meta-Harness distinguishes surfaces operationally: logs are evidence, skills are instructions, candidate files execute, frontier files rank, and validators gate. It does not type those surfaces as knowledge artifacts or system-definition artifacts, and it does not embed fine-grained provenance into a prompt paragraph, retrieval rule, or Python branch once that behavior enters a candidate file.

The key design contrast is "framework as pattern" versus "framework as knowledge base." Commonplace accumulates reusable methodology in a stable library. Meta-Harness accumulates pressure inside a run directory and promotes executable candidate files. It is most reusable when copied and adapted to a benchmarked domain, not when queried as a general memory store.

## Borrowable Ideas

**Use onboarding to define the oracle before the optimizer exists.** Ready to borrow. Commonplace trace-mining or skill-improvement loops should force the same fields before automation: mutable surface, fixed surface, evaluation unit, search set, held-out set, leakage risks, budget, and raw/derived artifact locations.

**Make the proposer write falsifiable candidate metadata.** Ready to borrow for any review or skill-generation loop. `pending_eval.json` is a compact bridge from agent proposal to benchmark gate: name, file/import path, hypothesis, expected mechanism, and candidate list. Commonplace could use the same handoff before running review bundles or small evals on generated instructions.

**Separate import/smoke gates from benchmark gates.** Ready to borrow. Meta-Harness checks that generated code imports and, in the Terminal-Bench path, runs a cheap smoke task before paying for the full run. Commonplace command or skill generation should keep that shape: syntax/import validation first, small behavioral smoke test second, expensive semantic or benchmark review last.

**Track frontier state as a derived view, not as source truth.** Ready to borrow. `frontier_val.json` is useful because it is cheap to read and drives proposer context, but the actual evidence remains in run logs, result JSON, candidate files, and summary rows. Commonplace generated indexes should keep the same humility: derived views accelerate navigation; they do not replace source artifacts.

**Do not borrow the lack of a shared core package as-is.** Meta-Harness is clear enough as research artifact code, but the two example loops duplicate orchestration ideas rather than exposing a reusable adapter interface. If commonplace needed this pattern, the reusable unit should probably be a small local command contract around candidate files, gates, and result manifests.

## Trace-derived learning placement

**Trace source.** Meta-Harness qualifies as trace-derived learning. The text-classification path consumes training/evaluation steps, per-example predictions, correctness, prompt hashes, memory checkpoints, and saved memory state from `inner_loop.py`. The Terminal-Bench path consumes Harbor trial directories, `result.json`, verifier rewards, rollout metrics, and KIRA trajectory steps. Both paths also preserve Claude proposer-session logs via `claude_wrapper.py`.

**Extraction.** Extraction is performed by a proposer agent under a skill prompt plus deterministic gates. The proposer reads summaries, frontier files, reports, and recent traces, then writes candidate files and `pending_eval.json`. The oracle is mixed: import checks reject syntactically or structurally invalid candidates; Terminal-Bench smoke tests reject runtime failures; validation and test benchmarks rank or promote candidates by score.

**Storage substrate.** Raw trace state lives mostly in ignored or generated run directories: text logs, `log.jsonl`, `memory.json`, Harbor `jobs/`, per-trial `result.json`, trajectory steps, Claude `claude_sessions/`, and result JSON. Derived reports and frontiers live as JSON, JSONL, markdown reports, and printed summaries under `logs/` or `results/`. Durable behavior-shaping state lives as Python candidate files under `agents/`, optional prompt templates, and saved memory states. The repo itself stores the scaffold and baselines; completed run state is generated locally rather than shipped in this checkout.

**Representational form.** The raw trace layer is mixed: natural-language messages, prompts, tool calls, JSONL events, scalar rewards, token/cost metrics, and serialized memory state. Reports and hypotheses are prose. Frontier, pending-eval, summary, and result files are symbolic JSON/JSONL. Candidate memory systems and agent scaffolds are executable symbolic Python, often with embedded prose prompts. There is no inspected path that trains weights, adapters, embeddings, rankers, or controllers as the retained learned form.

**Lineage.** Meta-Harness has run-level lineage: run names isolate logs; `evolution_summary.jsonl` records candidate hypotheses and score deltas; `frontier_val.json` records current winners; proposer sessions record tool/file activity; result directories preserve benchmark outputs. Fine-grained lineage is weaker: a line in a generated candidate file does not necessarily carry the exact source trace, report, or failed example that caused it, and frontier files are regenerated summaries rather than canonical evidence.

**Behavioral authority.** Raw traces, logs, reports, and summaries are knowledge artifacts when read as evidence or context. `ONBOARDING.md` and the `.claude/skills/` prompts are system-definition artifacts because they instruct setup and proposer behavior. `MemorySystem`, `AgentHarness`, `benchmark.py`, `meta_harness.py`, import checks, smoke checks, and Harbor invocations are system-definition artifacts because they define interfaces, execute candidates, validate candidates, or rank candidates. `frontier_val.json` has ranking influence rather than direct execution authority.

**Scope and timing.** Scope is per-domain and per-run: text-classification memory systems and Terminal-Bench scaffolds. Timing is staged offline: gather or evaluate runs, propose candidates from traces and frontier state, validate, benchmark, update derived state, repeat. It is not online self-modification during one task, though candidate memory systems may learn online within the inner loop.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), Meta-Harness belongs with outer-loop artifact-learning systems. It strengthens the survey claim that trace-derived learning often promotes into system-definition artifacts rather than memories: Python harnesses, prompt templates, gates, and ranking files. It also splits the "reusable framework" axis: the pattern is reusable, but the code is closer to two concrete example loops than a generic harness-optimization library.

## Curiosity Pass

**The repo is honest about being a cleaned-up release.** The README says the release has not been tested beyond verifying that it runs ([README.md](https://github.com/stanford-iris-lab/meta-harness/blob/95175f70c758dd1145b395edfe8b67e6f9d80fbd/README.md)). That matters: the reviewable claim is the scaffold design and example implementations, not production robustness.

**The paper artifact is split from this repo.** The optimized Terminal-Bench 2 harness lives in a separate artifact repository, according to the root README. This checkout can show how candidate scaffolds are proposed, evaluated, and recorded, but it does not include the paper's full evolved harness corpus.

**Candidate files are powerful but can become opaque.** Direct Python-file evolution is easy to activate and easy to benchmark. It is also easy for important lessons to disappear into untyped code branches unless the proposer writes strong reports and hypotheses.

**The text path and Terminal-Bench path use different proposer discipline.** Text classification forbids delegation and mandates three prototypes; Terminal-Bench explicitly asks for analysis and implementation subagents and one candidate. That divergence reinforces that Meta-Harness is a domain-adapted pattern, not one fixed optimizer protocol.

**The frontier is a useful but lossy memory.** It gives the proposer a compact current-best view, but it cannot explain why a mechanism worked. The richer behavioral memory is distributed across candidate files, reports, logs, and result directories.

## What to Watch

- Whether the two examples converge into a shared package with explicit domain adapters, candidate contracts, gate contracts, and run-artifact schemas.
- Whether future releases include completed run artifacts, not only the code for generating them.
- Whether candidate files gain embedded provenance tying mechanisms to trace evidence, reports, predictions, and invalidation criteria.
- Whether frontier state expands from score ranking into a richer design-memory surface that preserves why a candidate is on the frontier.
- Whether the onboarding prompt becomes executable validation for `domain_spec.md` rather than advisory setup guidance.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - source-inspected instance: Meta-Harness turns task traces and benchmark outcomes into candidate harness files and frontier state
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - supports: traces become signal for improving future harness behavior
- [Activate behavior-changing memory](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies: learned behavior activates when the next run imports the selected candidate file
- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: logs, traces, reports, summaries, and proposer-session records
- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: onboarding prompts, skills, candidate interfaces, candidate files, gates, and benchmark runners
- [auto-harness](./auto-harness.md) - compares-with: both use benchmark traces and gates to improve harness behavior, with Meta-Harness exposing broader candidate-file search and domain onboarding
- [Agentic Harness Engineering](./agentic-harness-engineering.md) - compares-with: both are outer-loop systems for optimizing agent harness code from traces and benchmark feedback
