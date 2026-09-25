---
type: types/note.md
description: "Ecdysis failure diagnosis, strict-score harness selection, checkpoint reuse, and the external adapter contracts that bound them."
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-ecdysis-01
source-identity: https://github.com/cuiyu-ai/Ecdysis
reviewed-revision: cf93866d545b0974dbb0bc83b39c31fbbdeeecb8
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-ecdysis-01/result.md
analysis-result-sha256: fc2ef3c6a009d4d93c1da5b9aa61d3bf112f95bf50a9c88736d4e336f8979533
---

# Ecdysis

Evidence basis: source code, repository documentation and prospective tests at commit `cf93866d545b0974dbb0bc83b39c31fbbdeeecb8`, inspected 2026-09-25; no target execution or author experiment was observed.

Ecdysis supplies a training controller that turns scored failures into proposed harness repairs, delegates their implementation, and retains a candidate only when its supplied score improves. Its shipped artifact is a **builder or improvement plane** with a **complete artifact, partial loop** boundary: the task model, collector, editor, scorer and executor are external callbacks. The package wires their coordination, including model-based diagnosis, but cannot establish the behavior of an arbitrary returned harness. See [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-ecdysis-01/result.md) — see-also: source excerpts, canonical records and both mandatory lenses.

## Execution and acceptance

Each training round collects trajectories for the current harness, scores them, extracts failures below a threshold and groups failures by termination and failed reward components. The review stage prioritizes groups spanning several tasks. Analyst, Critic and Engineer model calls iterate over those summaries; a Moderator produces a structured update specification. The editor receives that specification together with richer failure records and groups. The controller collects and scores candidate trajectories, replacing the current harness only if the candidate score is strictly greater. Rounds with no failures continue without editing. The final result retains the selected reference and numeric round records. [Training controller](https://github.com/cuiyu-ai/Ecdysis/blob/cf93866d545b0974dbb0bc83b39c31fbbdeeecb8/src/ecdysis/training.py) — evidenced-by.

The decisive guarantees are narrow. Strict comparison enforces numeric preference within a round. It does not verify equal task populations, stable scorers, valid reference answers or generalization. The editor receives the current object directly; an editor that mutates it can change the incumbent before rejection. Final inference wrappers avoid calling training, but neither deeply freeze the object nor sandbox the executor. Fixed evaluation and isolated editing are adapter contracts. Benchmark adapters also supply their own task loading, encoding and identity metadata.

## Diagnosis and retained context

The reviewer sees group counts and scalar outcomes for sampled failures, not message bodies, tool arguments or harness source code. A recurring signature therefore supplies a diagnosis heuristic rather than proof of a common defect. The Critic prompt explicitly challenges overfitting, false triggers and harmful changes; later Analyst turns are asked to address objections. These are wired opportunities for content-directed criticism. No actual diagnosis establishes that valid criticism occurred or that its meaning survived external editing. JSON parsing and field normalization establish neither truth nor semantic adequacy. [Review implementation](https://github.com/cuiyu-ai/Ecdysis/blob/cf93866d545b0974dbb0bc83b39c31fbbdeeecb8/src/ecdysis/fdcr/review.py) — evidenced-by.

Optional checkpoints retain dialogue, specifications, usage and review progress. An interrupted invocation resumes from the saved turn; later role prompts automatically receive the last twelve dialogue turns. A completed checkpoint returns its cached specification to the editor. This connects trajectory-derived guidance to later consumer calls, supporting the comparison profile's wired trace-learning route. Selection is automatic and coarse. The identity check covers rendered summary, pass count and model string; changed raw traces, role prompts, harness state or provider configuration can escape it if those covered inputs stay unchanged.

Standalone skill artifacts support JSON save/load, scope checks and first-ID-wins merging. No task-model consumer is established for those helpers. Their schema does not characterize the generic harness, whose storage, representation and authority remain undetermined. The complete repository inspection found prospective synthetic tests, not retained observed tests that establish behavior's dependence on recalled content.

## Learning and scope

The strongest supported contribution is the wired failure-to-diagnosis-to-candidate-selection-to-later-execution pathway, including optional reuse of generated guidance. Particular **conjectural learning** remains uninspected: no observed candidate-linked criticism and valid comparison establish improved future capacity attributable to that process. Narrow **reflection** is wired through checkpoint state representing the controller's own review progress: completed turns update it, and restoration changes subsequent calls. A revisable self-theory of the system's organization is uninspected. Demonstrated self-improvement is separately uninspected.

The README's reported accuracy, speed and generalization benefits remain attributed claims; this boundary includes no underlying trials. Concrete adapters, candidate-linked traces, controlled recall interventions and held-out evaluation would resolve the main uncertainties. Provider internals and exact model parameter identity are also outside the inspected boundary.

- [Conjectural learning](../../notes/definitions/conjectural-learning.md) — defined-in: criticism and attributable capacity improvement.
- [Reflective system](../../notes/definitions/reflective-system.md) — defined-in: causally connected self-representation.
