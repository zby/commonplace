---
type: types/note.md
description: jaz-evals wires benchmark feedback and adaptation, with bounded memory guarantees, bundled interventions
  and disclosed reproduction limits.
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-26-jaz-evals-01
source-identity: https://github.com/jaz-lang/jaz-evals
reviewed-revision: 83dc51ebbd02c9299890b6db93ddc773f07b74b9
analysis-result: kb/agentic-systems/reports/retained-archive/AAS-2026-09-26-jaz-evals-01/result.md
analysis-result-sha256: 335469e47ab7a2a92c21755fca3d6b1160146dc53e730978502c42dd054332e3
---

# jaz-evals

Evidence basis: source code, shipped prompts/configurations and reported result tables at commit `83dc51ebbd02c9299890b6db93ddc773f07b74b9`, inspected on 2026-09-26. No live reproduction or raw-run audit.

jaz-evals is the paper's experiment package: it pairs agent methods with StuLife or AppWorld, controls task delivery, records outcomes and produces comparison tables. It also implements ACE adaptation and supplies the prompts for JAZ's long-horizon delegation and solver improvement. The runtime and benchmark dependencies remain outside this analysis; the inspected code establishes how the package connects them.

## How the experiments work

The runner constructs a fresh environment, method adapter and state namespace for each attempt. A method error is recorded and completed work is still graded. Task-level grader errors and aggregate measurement failures have different handling, so an error label alone does not say whether the agent, task grader or whole measurement failed.

The JAZ adapter distinguishes shared tools from root-only queue controls. Root-only tools do not propagate automatically, but the root can deliberately pass them onward. Finish validation applies across the tree for StuLife continuation and at the root for AppWorld's bounded solver calls. Those are sequencing controls, not a security boundary.

The oracle differs by benchmark. AppWorld's completion call returns assertion feedback to the optimizer, including failure details. StuLife records correctness for evaluation while returning only sequencing feedback to the agent. The latter tests long-horizon recall without exposing a per-task correctness signal for adaptation (RTE-3 and RTE-4).

## Memory and improvement routes

JAZ's long-horizon configuration warns near the context limit and tells the model to delegate with history, state, a summary and next steps. The warning is wired; faithful handoff depends on model behavior. CodeAct and smolagents variants ask the model to keep their own output histories. Wrapped displays can be bounded while the underlying retained object continues growing.

For AppWorld, JAZ's root prompt asks for explicit failure hypotheses, minimal prompt/tool changes and validation on later task batches. The root controls whether to comply and which revisions to retain. This affords criticism-driven improvement; the prose is not an enforced acceptance gate.

ACE provides a more explicit update route: task trajectory and feedback → reflector → curator additions → optional deduplication → playbook supplied to the next fresh solver. Invalid structural operations or adaptation failures preserve the previous playbook. The playbook is explicitly advisory. Its shape checks and embedding-based merges do not establish that a retained lesson is true. The shipped configuration adapts for 42 tasks, then keeps using the frozen playbook; its reflector/curator calls also sit outside the solver session's BudgetPool.

Letta's adapter sends tasks into searchable conversation and intercepts compaction for accounting, but the external service owns much of the memory lifecycle. The analysis retains that uncertainty. Diagnostic logs alone are not an agent memory route, while ACE's consumed trajectories are.

## What the comparisons establish

The shipped tables report higher means for JAZ, including 74.2% AppWorld task completion versus 71.1% for CodeAct plus subagents, and 69.9% StuLife far-recall pass versus Letta's 61.8%. These remain reported outcomes in this analysis. The AppWorld table explicitly says six repetitions do not statistically separate JAZ from CodeAct plus subagents.

Two implementation details limit finer attribution. The CodeAct hook jointly removes programmatic history and string-valued input/scope bindings; the comparison does not isolate one feature. ACE stops adaptation after 42 tasks while JAZ is prompted to continue, so their difference includes adaptation schedule. These are method comparisons, not a causal test of one criticism or memory mechanism.

The package also discloses that original runs used development commits, mostly with uncommitted changes. The pinned installable JAZ release is the closest available version rather than the exact original code. Reproduction machinery and historical byte-exact reproducibility are therefore separate claims.

## Scope

The code wires a substantive path from task evidence to retained future solver guidance. Actual uptake, formulated criticism and improved future capacity require candidate-linked traces and controlled evidence. The analysis separately records all four [theory-builder conditions](../../notes/definitions/theory-builder.md), persistence, [reflection](../../notes/definitions/reflective-system.md) and [self-improvement](../../notes/definitions/self-improving-system.md); it does not infer them from a higher score or a stored playbook. External runtime, oracle and task-data correctness remain uninspected.

---

- [Exact analysis result](../reports/retained-archive/AAS-2026-09-26-jaz-evals-01/result.md) — see-also: complete routes, source quotations, comparison fields and evidential limits
- [Pinned evaluation source](https://github.com/jaz-lang/jaz-evals/tree/83dc51ebbd02c9299890b6db93ddc773f07b74b9) — evidenced-by: frozen implementation and reported results
