---
type: types/note.md
description: "OpenRSI's released OpenMLE stack: executable program search, retained experience and training interfaces, with evaluation and autonomy boundaries"
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-26-openrsi-01
source-identity: https://github.com/FrontisAI/OpenRSI
reviewed-revision: "71ae803a035d5e3b78c19fa49ed9f67d0550cbaa"
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-26-openrsi-01/result.md
analysis-result-sha256: 1c38740d9385e44d06ec249887e01889d41af107039bb249accac74a51e6e35e
---

# OpenRSI: OpenMLE search, experience and training

**Evidence basis:** source code and repository documents at commit `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`, inspected on 2026-09-26. Performance tables are reported operation; this analysis did not run models or reproduce benchmarks.

OpenRSI's released contribution is **OpenMLE**, an executable machine-learning-engineering improvement stack. Gym builds task packages and evaluators; Evo searches over generated programs; ERL provides supervised and reinforcement-learning stages for the generator. The strongest supported result is a set of connected implementation routes plus reported model/harness gains. It is not evidence of one unattended, recursively accelerating improvement process: the stages are launched separately, and their external datasets, model weights and infrastructure remain deployment inputs. [Release overview](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/README.md).

## Runtime and retained experience

An Evo task run drafts Python, executes it, receives validity/metric feedback, repairs failures, and selects parents for Improve or Crossover. Synchronous generations and asynchronous workers share the journal, population, checkpoint and output machinery. The final product is selected program code plus evaluation records. The operator controls tasks, evaluator, model endpoint, budgets and launch configuration; computation selects and revises candidates inside the run.

Memory has several distinct consumers. Task-local journals retain code, plans, feedback and lineage. Derived experience cards supply selection features. Optional rich summaries retain a method overview and comparative experience, then automatically supply selected parent/ancestor/sibling or related-error context to later model calls. Training consumes stored examples or rewarded rollouts; checkpoint loaders restore prior parameters. This connects retained content to later consumers, but no inspected execution established whether recalled explanations caused a useful revision. See the exact result's RTE-3, RTE-10 and RTE-11 and its [shared controller source](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py).

The supervised path is wired for materialized messages and the vendored trainer. The evolutionary selector emits a selected-step manifest; the inspected release does not close its conversion into training messages. It also drops the supplied selection reasons while keeping selected indices. RL supplies rollout/reward/checkpoint interfaces to a separately installed training engine. Its reported short smoke does not independently establish checkpoint save/reload or rich-summary activation. These limits qualify the search-to-training loop rather than erase its implemented parts.

## What feedback authorizes

Default MLE-Bench score selection uses sandbox-derived feedback; trusting a model-reported validation score requires an explicit switch. The parent selector consumes that normalized node metric, so its avoidance of a separate raw-score field does not independently guarantee withheld-test separation.

The shipped distributed worker mounts the shared task tree read-only. That protects against writes, not reads: the source explicitly treats the private answer directory as an evaluation convention rather than an enforced secrecy boundary. This limits what the default deployment proves about evaluator isolation; it is not evidence of actual benchmark leakage. Gym additionally generates metric code. Compilation, finite-score checks and quality recommendations have narrower authority than independent confirmation that a metric expresses the intended scientific task. [Sandbox contract](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/OpenMLE-Gym/openmle-sandbox/README.md).

Debug and Improve explicitly request criticism of the preceding program and carry revised code into subsequent tests. This supports a wired, bounded [theory-builder](../../notes/definitions/theory-builder.md) route: localized proposed solutions, consumption, requested content-directed criticism and iteration. Actual criticism quality is unobserved; score ranking alone does not supply it. Retained search history can affect subsequent search, providing limited reflection, but criticism and revision of the search method itself are unestablished. Automated task-level operations do not establish whole-stack autonomy.

## Improvement claims and scope

The repository reports MLE-Bench Lite Medal Average rising from 39.39% to 60.61% when substituting Frontis-MA1-35B for its base model with Evo fixed. It separately reports 71.21% for Evo-Max, which changes the search system. These are model/harness comparisons, not isolated evidence that memory or formulated criticism caused the improvement. [Reported results and protocol](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/docs/results.md).

The review covers the released OpenMLE stack, excluding Horizon, external model/data payloads, external RL optimizer and NatureBench evaluator internals, and deployed services. Pinned external artifacts, candidate-linked criticism traces, and controlled memory/criticism interventions would strengthen the assessment. The complete memory profile, both lenses, quotations, branch qualifications and verification are in the [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-26-openrsi-01/result.md).
