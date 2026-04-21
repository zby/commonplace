---
description: Minimal agent-optimization harness for improving one file against tau-bench with regression-suite and held-out-score gates, keeping learnings as workshop state rather than structured evaluators
type: kb/agent-memory-systems/types/agent-memory-system-review.md
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-04-04"
---

# auto-harness

auto-harness is a small Python harness from NeoSigma for iteratively improving a coding agent against a benchmark. The repo gives the agent a program file, a narrow mutation surface, and a gating loop: read failures, edit [`agent/agent.py`](https://github.com/neosigmaai/auto-harness/blob/f688ea40f63c3ccbf73438fd77bc4c6904561726/agent/agent.py), re-run a regression suite plus held-out benchmark, record the result, and repeat. Mechanically it is much thinner than the README's "self-improving system" framing: the implementation is a benchmark runner, a gate script, a workspace initializer, and a freeform learnings log. But the thinness is also the point. This is one of the cleanest reviewed examples of turning a coding agent into a benchmark-optimized outer loop without burying the mechanism under a large framework.

**Repository:** https://github.com/neosigmaai/auto-harness

## Core Ideas

**Program the improvement loop explicitly and narrow the mutation surface.** The center of gravity is not a controller service but [`PROGRAM.md`](https://github.com/neosigmaai/auto-harness/blob/f688ea40f63c3ccbf73438fd77bc4c6904561726/PROGRAM.md), which tells the agent to run `benchmark.py`, analyze failures, edit only [`agent/agent.py`](https://github.com/neosigmaai/auto-harness/blob/f688ea40f63c3ccbf73438fd77bc4c6904561726/agent/agent.py), gate the change, commit, and repeat. The harness does not try to make the agent generally self-modifying. It constrains self-improvement to one owned file and a fixed iteration rhythm. That is a strong architectural choice: it makes the mutable surface inspectable and keeps failures local.

**The verifier is a hard-oracle benchmark loop, not an LLM judge.** [`benchmark.py`](https://github.com/neosigmaai/auto-harness/blob/f688ea40f63c3ccbf73438fd77bc4c6904561726/benchmark.py) reduces behavior to `{task_id -> reward}` scores, and [`gating.py`](https://github.com/neosigmaai/auto-harness/blob/f688ea40f63c3ccbf73438fd77bc4c6904561726/gating.py) can enforce two real constraints before accepting a change: a pass-rate threshold on the current regression suite and a non-decreasing held-out `val_score` on the gate split. In the bootstrap case, though, `workspace/suite.json` starts empty and Step 1 is skipped, so early iterations are protected only by the held-out score gate. This means the system's learning pressure comes from repeatable task rewards, not from another model's opinion about quality. The loop is therefore only as strong as the benchmark, but where the benchmark is good, the enforcement is genuine.

**The "self-maintained eval suite" is really an auto-growing regression set.** The interesting part of the gate is Step 3: after a successful change, previously failing train tasks are re-run and newly passing ones are promoted into `workspace/suite.json`. This is a useful pattern because it converts observed failures into future checks with almost no extra machinery. But it is simpler than the README's framing suggests. The suite grows only from repaired train failures, so held-out-only regressions and unresolved train failures do not become Step 1 checks. The suite stores task IDs and a threshold, not generalized failure categories, richer assertions, or distilled behavioral rules.

**Memory lives in workshop files, not in transformed knowledge artifacts.** [`prepare.py`](https://github.com/neosigmaai/auto-harness/blob/f688ea40f63c3ccbf73438fd77bc4c6904561726/prepare.py) creates `workspace/suite.json`, `workspace/learnings.md`, `workspace/results.tsv`, and `workspace/train_results.json`. [`record.py`](https://github.com/neosigmaai/auto-harness/blob/f688ea40f63c3ccbf73438fd77bc4c6904561726/record.py) appends scores and commit hashes after passing runs. This gives the loop continuity, but the continuity is mostly operational. `learnings.md` is freeform text, `results.tsv` is a score log, and `suite.json` is a growing list of task IDs. The system accumulates history, but it does not yet distill that history into a richer symbolic artifact.

**The benchmark abstraction is real at the class boundary, weaker at the repo boundary.** [`benchmark.py`](https://github.com/neosigmaai/auto-harness/blob/f688ea40f63c3ccbf73438fd77bc4c6904561726/benchmark.py) exposes a `BenchmarkRunner` abstract base class and says the harness is benchmark-agnostic. That is true in the limited sense that the runner contract is small. But the shipped `__main__` paths and gate wiring still instantiate `TauBenchRunner` directly. So this is best read as a template for hard-oracle optimization loops, not as a fully pluggable benchmark framework.

## Comparison with Our System

| Dimension | auto-harness | Commonplace |
|---|---|---|
| Primary target | Improve one agent implementation against a scored benchmark | Improve a durable knowledge base used across many tasks |
| Mutation surface | One owned code file plus freeform workshop logs | Notes, links, instructions, scripts, and review artifacts |
| Verification | Hard-oracle-ish task rewards and held-out score gates | Deterministic validation plus judgment-heavy review; no global benchmark |
| Persistent memory | `workspace/` files: suite, learnings, results, last train run | Library notes plus emerging workshop layer with richer semantic links |
| Promotion mechanism | Passing formerly failing tasks become future regression checks | Manual and review-mediated promotion from raw text to structured knowledge |
| Main bottleneck | Benchmark coverage and suite quality | Oracle construction for judgment-heavy mutations |

auto-harness is stronger exactly where commonplace is weaker: it has a concrete, executable outer loop for iterative improvement under a measurable oracle. When the task family is stable and rewards are trustworthy, this repo shows how little machinery you need to get a real optimization cycle: score, gate, promote, record, repeat.

Commonplace is stronger where auto-harness becomes thin. We care about durable explanatory structure, articulated relationships, and knowledge that composes across tasks. auto-harness mostly does not try to represent knowledge at that level. Its "memory" is operational residue around an optimization process, not a curated substrate meant to support navigation, synthesis, or reuse outside the benchmark loop.

The deepest difference is that auto-harness is basically a **workshop subsystem**. Its artifacts are meant to drive one active experiment forward, not to accumulate into a library. That makes it a useful comparison for our workshop-layer notes more than for the library layer itself.

## Borrowable Ideas

**Treat the optimization loop itself as a first-class artifact.** [`PROGRAM.md`](https://github.com/neosigmaai/auto-harness/blob/f688ea40f63c3ccbf73438fd77bc4c6904561726/PROGRAM.md) is the actual control surface for the system. For commonplace, this reinforces that operational subsystems should often be "programmed" with explicit loop documents rather than buried in vague AGENTS instructions. This is ready to borrow now.

**Promote repaired failures directly into future checks.** The Step 3 suite-promotion pattern in [`gating.py`](https://github.com/neosigmaai/auto-harness/blob/f688ea40f63c3ccbf73438fd77bc4c6904561726/gating.py) is a compact spec-mining move: a failure that was just repaired becomes part of the regression boundary. Wherever commonplace gains hard-enough oracles for a workshop process, this is ready to borrow now.

**Keep workshop state explicit and local.** `workspace/` separates live experiment state from code under optimization. For commonplace, this supports the argument that temporal operational artifacts should live in a workshop layer instead of contaminating the library. This is ready to borrow now as an organizational principle.

**Narrow the mutable surface when running autonomous loops.** Letting the agent edit one owned file is a practical containment mechanism. For any future self-improving subsystem we build, constraining what can change per loop is a strong safety and interpretability pattern. This is ready to borrow now.

**Record outcome history as append-only operational telemetry.** `results.tsv` is simple, but it gives the loop a minimal lineage of scores and commits. Commonplace already does this in richer form for reviews; the broader pattern is worth reusing in other workshop subsystems. This is more a confirmation than a new idea.

## Curiosity Pass

**The repo's strongest idea is control by verifier shape, not "self-improvement" in the broad sense.** The property claimed is overnight autonomous improvement. Mechanistically, the real engine is simpler: benchmark tasks provide the oracle, the gate enforces non-regression, and the agent mutates one file. The system works to the degree that the benchmark is representative. So the central contribution is not a new learning architecture; it is a clean packaging of a hard-oracle outer loop.

**The eval suite is less agent-authored than the README implies.** The README says the coding agent "self-maintains" `suite.json`, but [`PROGRAM.md`](https://github.com/neosigmaai/auto-harness/blob/f688ea40f63c3ccbf73438fd77bc4c6904561726/PROGRAM.md) marks it read-only and [`gating.py`](https://github.com/neosigmaai/auto-harness/blob/f688ea40f63c3ccbf73438fd77bc4c6904561726/gating.py) promotes tasks automatically. That makes the suite closer to an auto-growing replay buffer than to a genuinely curated evaluator set. The simpler description is "the harness automatically turns repaired train failures into future regression tasks."

**The learnings log is advisory memory, not enforced memory.** [`PROGRAM.md`](https://github.com/neosigmaai/auto-harness/blob/f688ea40f63c3ccbf73438fd77bc4c6904561726/PROGRAM.md) tells the agent to append to `workspace/learnings.md` and to read it at session start, but none of the shipped scripts verify that this happened or inject the file into execution. The mechanism therefore depends on agent obedience. This is still useful, but it is much softer than the gate itself.

**Some of the "generality" is aspirational.** [`benchmark.py`](https://github.com/neosigmaai/auto-harness/blob/f688ea40f63c3ccbf73438fd77bc4c6904561726/benchmark.py) does define a small benchmark abstraction, but the live paths still instantiate `TauBenchRunner`; [`gating.py`](https://github.com/neosigmaai/auto-harness/blob/f688ea40f63c3ccbf73438fd77bc4c6904561726/gating.py) also ignores the `threshold` field in `experiment_config.yaml` and instead reads threshold only from `workspace/suite.json`, which is initialized to `0.8` in [`prepare.py`](https://github.com/neosigmaai/auto-harness/blob/f688ea40f63c3ccbf73438fd77bc4c6904561726/prepare.py). That makes the current repo feel more like a well-factored tau-bench template than a finished general harness.

**There is mild documentation drift already, which matters in a repo this small.** The README describes a two-step gate, while the code and [`PROGRAM.md`](https://github.com/neosigmaai/auto-harness/blob/f688ea40f63c3ccbf73438fd77bc4c6904561726/PROGRAM.md) clearly implement a three-step flow with suite promotion. In a lightweight harness, docs are part of the control plane. Small mismatches matter because there is so little other structure to absorb them.

## What to Watch

- Whether `learnings.md` stays freeform advice or evolves into structured failure taxonomies, reusable evaluator hints, or automated prompt deltas.
- Whether the regression suite gains pruning, weighting, clustering, or richer assertions instead of only monotonically accumulating task IDs.
- Whether the benchmark abstraction becomes a true plug-in surface rather than a tau-bench-shaped template with an abstract base class.
- Whether the threshold/config drift and README/code drift get cleaned up; in a thin harness, control-plane drift is architectural drift.
- Whether the loop keeps working outside strong-oracle benchmark domains, or whether its success is tightly coupled to tau-bench-like tasks with cheap scoring.

---

Relevant Notes:

- [The boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: auto-harness works because benchmark rewards make autonomous iteration cheaply verifiable
- [Evaluation automation is phase-gated by comprehension](../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) — exemplifies: the loop explicitly requires reading failures before changing the agent
- [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — exemplifies: `workspace/` is a concrete workshop layer around one active optimization process
- [Automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md) — contrasts: auto-harness automates because it has a benchmark oracle where KB mutations usually do not
- [spec mining as codification](../../notes/spec-mining-as-codification.md) — extends: promoting repaired failures into the regression suite is a narrow spec-mining move
- [Inspectable artifact, not supervision, defeats the blackbox problem](../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — foundation: the whole loop remains legible because the mutable surface, gate, and logs are ordinary files
- [Autocontext](./autocontext.md) — contrasts: both run iterative improvement loops, but auto-harness uses a far thinner control plane and a more uniformly benchmark-gated regime
- [HyperAgents](./hyperagents.md) — contrasts: both self-edit around benchmark feedback, but auto-harness narrows mutation to one file and one task family instead of evolving a larger code agent stack
