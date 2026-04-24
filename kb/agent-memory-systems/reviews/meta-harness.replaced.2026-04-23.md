---
description: "Stanford IRIS Lab harness-code optimizer with Claude-proposed memory/scaffold variants, benchmark-gated promotion, run logs, frontiers, and executable candidate artifacts"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-04-15"
---

# Meta-Harness

> Replaced 2026-04-23. See [Meta-Harness](./meta-harness.md) for the current review.

Meta-Harness is a Stanford IRIS Lab framework for optimizing model harnesses: the code around a fixed base model that decides what to store, retrieve, show, and scaffold while the model works. The repository is a cleaned-up release of the paper code, with an onboarding prompt for new domains and two reference experiments: text-classification memory-system search and Terminal-Bench 2 scaffold evolution, as described in its [README](https://github.com/stanford-iris-lab/meta-harness/blob/d283ab394ff6d59198dac4c098d4e6271cadfb71/README.md). It is not a general-purpose memory store; it is an outer-loop search harness where memory and context logic become executable candidate code.

**Repository:** https://github.com/stanford-iris-lab/meta-harness

**Reviewed commit:** https://github.com/stanford-iris-lab/meta-harness/commit/d283ab394ff6d59198dac4c098d4e6271cadfb71

## Core Ideas

**The search target is harness code, not the base model.** The top-level [README](https://github.com/stanford-iris-lab/meta-harness/blob/d283ab394ff6d59198dac4c098d4e6271cadfb71/README.md) defines the harness as the code around a fixed model that decides what information to store, retrieve, and present over time, and [ONBOARDING.md](https://github.com/stanford-iris-lab/meta-harness/blob/d283ab394ff6d59198dac4c098d4e6271cadfb71/ONBOARDING.md) turns that into a domain-specification exercise: define the evaluation unit, fixed model, candidate interface, budget, search set, held-out set, trace artifacts, and leakage risks before implementing anything. That boundary is the main architectural contribution. Meta-Harness optimizes the wrapper, not the model weights or a separate memory backend.

**The repo ships examples rather than one reusable package.** The [text-classification](https://github.com/stanford-iris-lab/meta-harness/tree/d283ab394ff6d59198dac4c098d4e6271cadfb71/reference_examples/text_classification) and [Terminal-Bench](https://github.com/stanford-iris-lab/meta-harness/tree/d283ab394ff6d59198dac4c098d4e6271cadfb71/reference_examples/terminal_bench_2) directories each contain their own `meta_harness.py`, `.claude/skills/.../SKILL.md`, `claude_wrapper.py`, logs, candidate directories, and benchmark wiring. The common pattern is clear, but it is copied into two concrete experiments instead of factored into a library API. The README is honest about this being a cleaned-up paper release rather than a hardened framework.

**A proposer agent writes executable candidates; the Python outer loop evaluates them.** In text classification, [meta_harness.py](https://github.com/stanford-iris-lab/meta-harness/blob/d283ab394ff6d59198dac4c098d4e6271cadfb71/reference_examples/text_classification/meta_harness.py) calls Claude Code through `claude_wrapper.run(...)`, passes a local `meta-harness` skill, expects `pending_eval.json`, import-checks proposed `agents/*.py` files, benchmarks them, updates `frontier_val.json`, and appends `evolution_summary.jsonl`. The [skill](https://github.com/stanford-iris-lab/meta-harness/blob/d283ab394ff6d59198dac4c098d4e6271cadfb71/reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md) instructs the proposer to read prior results and raw prediction logs, prototype mechanisms, implement exactly three memory systems, and leave benchmarking to the outer loop. That split keeps generation flexible while making acceptance mechanical.

**The memory-system example makes memory a typed interface.** [memory_system.py](https://github.com/stanford-iris-lab/meta-harness/blob/d283ab394ff6d59198dac4c098d4e6271cadfb71/reference_examples/text_classification/memory_system.py) defines the candidate contract: `predict`, `learn_from_batch`, `get_state`, and `set_state`, with `call_llm` tracking prompt length/hash/text. [inner_loop.py](https://github.com/stanford-iris-lab/meta-harness/blob/d283ab394ff6d59198dac4c098d4e6271cadfb71/reference_examples/text_classification/inner_loop.py) supports both online learning (`predict -> feedback -> learn_from_batch`) and offline training where ground truth is visible before validation. It writes JSONL step logs, memory checkpoints, `memory.json`, `val.json`, and `test.json`, while [benchmark.py](https://github.com/stanford-iris-lab/meta-harness/blob/d283ab394ff6d59198dac4c098d4e6271cadfb71/reference_examples/text_classification/benchmark.py) sweeps datasets, memory systems, models, and seeds and computes accuracy/context-length frontiers. This is a compact, code-level memory laboratory rather than a persistent knowledge base.

**The Terminal-Bench example evolves agent scaffolds instead of memory classes.** Its [meta_harness.py](https://github.com/stanford-iris-lab/meta-harness/blob/d283ab394ff6d59198dac4c098d4e6271cadfb71/reference_examples/terminal_bench_2/meta_harness.py) starts from Harbor/Terminus baselines, prompts Claude to create one `AgentHarness` subclass, import-checks and smoke-tests it on a cheap task, then runs Harbor over the Terminal-Bench 2 task set through [scripts/run_eval.sh](https://github.com/stanford-iris-lab/meta-harness/blob/d283ab394ff6d59198dac4c098d4e6271cadfb71/reference_examples/terminal_bench_2/scripts/run_eval.sh). It parses per-trial rewards, cost, tokens, turns, and API-call metrics from job directories, maintains a per-task and global frontier, and optionally runs a stronger final winner evaluation. The local [Terminal-Bench skill](https://github.com/stanford-iris-lab/meta-harness/blob/d283ab394ff6d59198dac4c098d4e6271cadfb71/reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md) makes the search space explicit: override tool schemas, LLM calls, command execution, context summarization, prompt templates, and the main loop, but keep the Harbor import contract stable.

**The trace format is intentionally rich.** The inspected code gives the proposer more than scalar scores: text-classification candidates can inspect `log.jsonl` prediction traces, saved memory states, prompt hashes, frontier summaries, and post-eval reports; Terminal-Bench candidates are instructed to deep-read failed and successful trajectories under `jobs/` and `logs/`, plus rollout metrics. The paper's central evidence about raw traces versus summaries is therefore visible as a design choice in the repo: useful outer-loop learning depends on diagnostic artifacts, not just leaderboard numbers.

## Comparison with Our System

| Dimension | Meta-Harness | Commonplace |
|---|---|---|
| Primary purpose | Improve a task-specific model harness through benchmark-gated code search | Build durable methodology knowledge for future agents and maintainers |
| Main substrate | Candidate Python files, run logs, result JSON, frontier summaries, Claude session logs | Markdown notes, indexes, instructions, ADRs, sources, and workshop artifacts |
| Memory model | Domain-specific harness logic; text example exposes `MemorySystem` state, TB2 exposes scaffold code | Typed knowledge artifacts with links, descriptions, and validation |
| Learning loop | Proposer writes code from traces; outer loop validates, benchmarks, and records | Human/agent curation, semantic review, deterministic validation, and manual synthesis |
| Oracle | Benchmark accuracy/pass rate, smoke tests, import checks, cost/token/turn metrics | Structural validation plus semantic review; no global task reward |
| Promotion target | Executable candidate harnesses and frontier records | Durable notes, instructions, indexes, and scripts |
| Lifecycle boundary | Run-local experiment workspace | Library plus emerging workshop layer |

Meta-Harness is stronger where commonplace is weakest: it closes a real optimization loop when a task has a measurable oracle. It defines a mutation surface, runs candidates, records outcomes, and lets the next proposer use the trace. That is the missing machinery behind many KB-learning ideas: not extraction, but repeated mutation under an evaluable target.

Commonplace is stronger where Meta-Harness stays intentionally thin. The repo does not try to maintain a durable theory of what it learns, represent semantic links among discovered patterns, or preserve explanations outside the run's logs and generated code. Its successful artifacts are executable harnesses, not explanatory knowledge. In our vocabulary, Meta-Harness is a workshop optimizer: it consumes value during an experiment and may produce artifacts worth distilling later, but it is not itself a library.

The useful contrast is not "benchmark loop versus knowledge base." It is boundary placement. Meta-Harness assumes the domain can supply a clean harness interface and a trustworthy evaluation split. Commonplace's harder problem is that many desirable mutations are judgment-heavy: better linking, better synthesis, better definitions, better indexes. Meta-Harness shows what the loop should look like once an oracle exists; it also clarifies how much work remains when the oracle is soft.

## Borrowable Ideas

**Onboarding as oracle construction.** [ONBOARDING.md](https://github.com/stanford-iris-lab/meta-harness/blob/d283ab394ff6d59198dac4c098d4e6271cadfb71/ONBOARDING.md) asks for evaluation unit, fixed components, search/held-out splits, budget, leakage risks, trace artifacts, and candidate interface before implementation. A future commonplace auto-improvement loop should have an equivalent domain-spec artifact before it mutates notes or instructions. Ready to borrow now as a workshop template.

**Separate candidate proposal from evaluation ownership.** The proposer writes code and metadata; `meta_harness.py` owns import checks, smoke tests, benchmark runs, frontier updates, and final test evaluation. For commonplace, review-bundle auto-fixes should follow the same separation: a generator can propose edits, but a runner should own validation, semantic QA, and acceptance. Ready to borrow now as a control-plane pattern.

**Make raw traces first-class proposer input.** The local skills tell Claude to read prediction traces, job outputs, state files, and reports, not only aggregate scores. For KB work, this argues against feeding a revision agent only review summaries. When possible, give it concrete failures, diffs, reviewer comments, and validation output. Ready to borrow now.

**Use cheap gates before expensive evaluations.** The Terminal-Bench loop import-checks candidates and runs a one-task smoke test before full evaluation. The KB analog is front-loading deterministic validation and small semantic checks before running an expensive corpus-level review bundle. Ready to borrow now.

**Record frontiers, not just winners.** The text example computes Pareto frontiers over accuracy and context length; the Terminal-Bench example keeps best agents per task as well as the global best. For commonplace, a review or retrieval experiment should preserve tradeoff frontiers, because "best" depends on which cost or quality dimension later matters. Needs a concrete experiment before implementation.

**Treat harness code as the learned artifact.** Meta-Harness makes a strong case that some memory lessons should not become prose memories. If a trace-derived pattern can be codified into retrieval, context assembly, or tool-use code, the durable artifact should be executable. Ready to borrow as a design principle, but not as an immediate implementation.

## Trace-derived learning placement

**Trace source.** Meta-Harness consumes repeated run trajectories, not one live chat transcript. In the text-classification example, traces include JSONL train/eval steps, predictions, correctness, prompt lengths/hashes, saved memory state, validation/test results, frontiers, evolution summaries, and Claude proposer sessions. In the Terminal-Bench example, traces include Harbor job directories, per-trial result JSON, verifier rewards, token/cost/turn metrics, frontier state, evolution summaries, and failed/successful trajectories read by the proposer skill.

**Extraction.** Extraction is delegated to Claude Code under experiment-specific skills. The text skill requires three candidate memory systems per iteration, each with a hypothesis, mechanism, prototype, implementation, and `pending_eval.json` entry. The Terminal-Bench skill requires a trajectory-analysis pass, one candidate scaffold, an importable `AgentHarness`, and metadata for evaluation. The oracle is external: import checks and smoke tests catch broken candidates; benchmark accuracy/pass rate decides whether the candidate improves the frontier.

**Promotion target.** The primary promotion target is executable symbolic artifacts: Python memory systems or agent harness subclasses under `agents/`. Secondary artifacts are `frontier_val.json`, `evolution_summary.jsonl`, result JSON, saved memory state, post-eval reports, and Claude session logs. The inspected repo does not promote into model weights. It also does not maintain a durable prose playbook except as run-local reports and proposer context.

**Scope.** Scope is per-domain and per-run. The onboarding prompt is general, but the implemented loops are specialized to text classification and Terminal-Bench 2. Within a domain, learning accumulates across iterations through candidate files and run artifacts. Cross-domain transfer is manual: a user must adapt the pattern and write a new domain spec.

**Timing.** Learning is staged and offline relative to deployment: propose candidates, validate, benchmark, update frontier, then repeat. The text memory systems may learn online or offline inside one benchmark run, but the meta-learning loop itself is an outer loop over completed evaluations.

**Survey placement.** On the [trace-derived learning survey axes](../trace-derived-learning-techniques-in-related-systems.md), Meta-Harness is a **trajectory-run pattern** with **symbolic executable-artifact promotion**. It sits near Autocontext, CORAL, and auto-harness, but its mutation target is broader than a playbook or one agent file: the harness itself is the learned artifact. It strengthens the survey's claim that trace richness is load-bearing. Scores alone are not enough; the implementation is built around giving the proposer raw logs, trajectories, state files, and reports because those artifacts carry the failure structure needed for useful code mutations.

## Curiosity Pass

**The "framework" is mostly a pattern encoded twice.** There is no central `meta_harness` package shared by both examples. Each reference experiment owns its own wrapper, skill, logs, candidate directory, and benchmark loop. That makes the repo easier to inspect but means the reusable unit is the architecture and onboarding prompt, not a library abstraction.

**The proposer priors are doing real work.** The evolution loops look simple partly because the local skills carry strong constraints: how many candidates to write, what traces to inspect, which files are mutable, how to avoid overfitting, and how to produce `pending_eval.json`. If those skills drift, the system drifts. In this repo, prompts are part of the implementation, not documentation around it.

**The examples use different proposer-control philosophies.** The text-classification skill says to do all work in the main session and not delegate; the Terminal-Bench skill explicitly asks for one analysis subagent and one implementation subagent. That is not a bug, but it shows that the "meta-harness" abstraction does not prescribe a single agent topology. The topology is another harness parameter.

**The held-out story is strongest in text classification.** The text loop has explicit val/test separation and saves `memory.json` from validation training before test evaluation, backed by the dataset sizing and split configuration in [config.yaml](https://github.com/stanford-iris-lab/meta-harness/blob/d283ab394ff6d59198dac4c098d4e6271cadfb71/reference_examples/text_classification/config.yaml). The Terminal-Bench example uses an official task set with optional stronger final evaluation, but it is still a scaffold search over a benchmark where repeated exposure to task-level outcomes can shape future candidates. The repo's own onboarding prompt correctly treats leakage as a first-class risk.

**The output is code, but the explanation is fragile.** `evolution_summary.jsonl` records hypotheses, axes, changes, and outcomes, but the durable explanation of why a harness improved is still whatever the proposer wrote and whatever a human later infers from logs. Meta-Harness optimizes harnesses more directly than it distills lessons. That is a reasonable tradeoff for benchmark work, but it means the learned knowledge is hard to reuse outside the target domain.

## What to Watch

- Does the repo factor a common library out of the two reference examples, or remain a paper artifact plus copyable pattern?
- Do proposer skills evolve stronger lifecycle management for candidates: pruning, rollback, duplicate detection, mechanism taxonomy, or anti-overfit checks grounded in prior failures?
- Does the optimized Terminal-Bench artifact repository expose enough history to inspect the full trajectory from baseline to final harness?
- Does Meta-Harness add support for softer oracles, pairwise judging, or human review, or stay focused on domains with benchmark-grade metrics?
- Do future examples promote lessons into prose, tests, or reusable skills, or does executable harness code remain the only durable learning target?

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: Meta-Harness is a trajectory-run system that promotes traces into executable harness code and strongly supports the trace-richness claim
- [The boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — exemplifies: Meta-Harness works where benchmark oracles make candidate evaluation cheap enough to automate
- [Evaluation automation is phase-gated by comprehension](../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) — parallels: the onboarding prompt forces domain comprehension and eval definition before optimization
- [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — exemplifies: Meta-Harness is a workshop optimizer whose run artifacts may later feed durable library knowledge
- [Automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md) — contrasts: Meta-Harness closes the loop only when a trustworthy task oracle exists
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) — grounds: harness-code evolution is deploy-time learning through durable artifacts rather than model retraining
- [auto-harness](./auto-harness.md) — sibling: both are benchmark-gated harness optimizers, but Meta-Harness gives the proposer richer traces and searches broader harness surfaces
- [CORAL](./CORAL.md) — sibling: both use benchmark-gated agent-code search, but CORAL emphasizes multi-agent shared workshop state while Meta-Harness emphasizes domain-specific harness optimization
- [Autocontext](./autocontext.md) — sibling: both are iterative outer loops with accumulated run artifacts, but Autocontext has a stronger playbook/session-report layer and optional weight distillation
