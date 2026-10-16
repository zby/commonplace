---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Ecdysis's shipped harness-improvement plane and inference interfaces at commit cf93866d545b0974dbb0bc83b39c31fbbdeeecb8."
run-id: AAS-2026-10-13-ecdysis-bb4c64dbdf60-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: whole-system
reviewed-boundary: cf93866d545b0974dbb0bc83b39c31fbbdeeecb8
analysis-cutoff: "2026-10-13"
evidence-tier: code-grounded
source:
  kind: git
  identity: https://github.com/cuiyu-ai/Ecdysis
  revision: cf93866d545b0974dbb0bc83b39c31fbbdeeecb8
  path: /home/zby/llm/commonplace/.commonplace/worktrees/ecdysis-bb4c64dbdf60/related-systems/cuiyu-ai--Ecdysis
  sha256: null
---

# Ecdysis boundary

## Boundary and evidence

This run analyses Ecdysis as a **builder or improvement plane**: a method-level system that collects scored task trajectories, groups failures, calls models for collaborative refinement, delegates candidate editing, and admits a candidate harness by score comparison. Its intended use is harness training followed by inference with the retained harness. It is in scope because its refinement operation issues model calls; it is not classified as the enclosing task-agent runtime (SRC-1, `src/ecdysis/training.py`, `src/ecdysis/fdcr/review.py`, `src/ecdysis/llm_client.py`).

> """Run failure aggregation, FDCR, editing, and strict validation."""
> --- `src/ecdysis/training.py`

> reply = client.chat(messages, temperature=0.3)
> --- `src/ecdysis/fdcr/review.py`

> accepted = candidate_score > baseline_score
> --- `src/ecdysis/training.py`

The boundary is **whole-system for the shipped Ecdysis artifact**, not the paper's complete experimental environment. It includes both CLI entry points, public Python APIs, the shipped synthetic driver, training and inference orchestration, failure grouping and score helpers, FDCR role prompts and checkpoint maintenance, model-client behavior, reusable-skill serialization/loading/merging, and synthetic evaluators. No material tracked path remains uninspected. The example and tests are included as shipped consumers, not excluded as external applications (SRC-1, `pyproject.toml`, `examples/quickstart.py`, `src/ecdysis/__init__.py`, `src/ecdysis/artifacts.py`, `tests/test_training.py`).

State production, maintenance, admission and consumption are covered by the trainer and its collector/editor/scorer interfaces, FDCR checkpoint write/reload paths, artifact save/load/merge APIs and their test consumers, and retained-harness inference through the result object, batch runner and benchmark driver. The artifact utilities are included without assuming that the trainer automatically persists or injects learned skills: the shipped trainer consumes the review specification through the supplied editor, while artifact persistence is a separate API (SRC-1, `src/ecdysis/training.py`, `src/ecdysis/fdcr/review.py`, `src/ecdysis/artifacts.py`, `src/ecdysis/inference.py`, `src/ecdysis/benchmark.py`, `tests/test_artifacts.py`, `tests/test_evolution_checkpoint.py`).

External responsibilities remain external. Real task execution, task-model/environment behavior, candidate implementation and custom scoring are supplied through adapters. The repository includes a synthetic implementation of these responsibilities, which is inspected, but not a production task runtime or editor. The source-native contract states:

> - `collector(harness)` executes the fixed task model and environment, returning
>   scored trajectory records.
> - `editor(harness, specification, failures, groups)` creates an isolated candidate
>   without mutating the retained harness.
> - `scorer(results)` computes the fixed aggregate training score. The default is
>   the arithmetic mean of available trajectory rewards.
> --- `README.md`

The real benchmark installations, adapter modules and harness factories are not frozen here. Their absence prevents conclusions about production harness execution, real editor isolation, external benchmark correctness or reproduction of paper-level gains. The generic benchmark integration remains included (SRC-1, `README.md`, `src/ecdysis/benchmark.py`).

> The adapter module, benchmark installation, and harness are user-provided. No
> dataset, secret, or local configuration is read from this repository. Record the
> external benchmark commit and the command used for each reported experiment.
> --- `README.md`

External dependencies include Python 3.12–3.13, the OpenAI SDK, an OpenAI-compatible model service and credentials for real FDCR calls, plus the user-supplied adapters above. Packaging declares Hatchling for builds and pytest/ruff as development dependencies. These dependencies' implementations and live services are not included; their reliability, deployed model behavior and real costs cannot be established by this source inspection (SRC-1, `pyproject.toml`, `src/ecdysis/llm_client.py`). The linked paper is not a registered source and is not inspected; this prevents independent assessment of its methodology and numerical results. The README's results are reported claims, not observed runs (SRC-1, `README.md`).

Evidence is frozen at **cf93866d545b0974dbb0bc83b39c31fbbdeeecb8**, with applicability cutoff **2026-10-13**. The checkout HEAD matches this revision and has no tracked changes. The overall tier is **code-grounded**. All tracked files were read as source text; no target code, test, example or provider call was executed. Tests and expected example output supply implementation/design evidence, not evidence that a run succeeded. There are no unavailable tracked files or deliberate tracked-path exclusions; missing external implementations and execution evidence are the conclusion limits described above.

### Tracked top-level coverage

| Top-level tracked path | Classification | Material inspected paths and role | Exclusion or access limit and conclusion prevented |
|---|---|---|---|
| `.gitignore` | Included; inspected | `.gitignore`: declares local secrets, inputs, outputs and development caches outside tracked material (SRC-1). | No tracked exclusion. Ignored local data is not frozen evidence; no local-run conclusions. |
| `README.md` | Included; inspected | `README.md`: method, adapters, CLI usage, reported results and expected synthetic output (SRC-1). | Linked paper and separately installed benchmarks are outside the frozen source; no independent experimental verification. |
| `pyproject.toml` | Included; inspected | `pyproject.toml`: package, supported Python, dependencies, scripts `ecdysis` and `ecdysis-run`, test configuration (SRC-1). | Dependency and build-tool internals are outside the source; no installation or compatibility demonstration. |
| `examples/` | Included; inspected | `examples/quickstart.py`: synthetic review client, collector, editor, trainer and later batch inference consumer (SRC-1). | Inspected, not executed; no observed end-to-end success or real model behavior. |
| `src/` | Included; inspected | `src/ecdysis/__init__.py` and `src/ecdysis/__main__.py`: exports and result-analysis CLI; `src/ecdysis/evolution.py`: extraction, grouping, scoring and artifact construction; `src/ecdysis/training.py`: candidate admission and retained-harness consumption; `src/ecdysis/inference.py`: task execution interfaces and result persistence; `src/ecdysis/benchmark.py`: adapter loading, evaluation driver and output; `src/ecdysis/artifacts.py`: skill validation, save/load/deduplication/merge; `src/ecdysis/fdcr/__init__.py`, `src/ecdysis/fdcr/review.py` and `src/ecdysis/fdcr/roles.py`: review scheduling, shipped prompts, specification formatting and checkpoint maintenance/reuse; `src/ecdysis/llm_client.py`: provider-facing calls, parsing, retries and usage accounting; `src/ecdysis/README.md`: package responsibilities (SRC-1). | No material shipped path excluded or uninspected. Real adapters and services remain external; no claims about their operation or enforcement of their obligations. |
| `tests/` | Included; inspected | `tests/test_artifacts.py`: artifact persistence/merge consumers; `tests/test_benchmark.py`: synthetic evaluation adapter and output; `tests/test_cli.py`: result-analysis CLI; `tests/test_evolution.py`: extraction/grouping checks; `tests/test_evolution_checkpoint.py`: interrupted/completed checkpoint reload consumer; `tests/test_inference.py`: inference/output/error handling; `tests/test_training.py`: admission/rejection and later retained-harness execution (SRC-1). | Tests were read, not run. No pass-rate claim or production/causal evidence. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/cuiyu-ai/Ecdysis` | cf93866d545b0974dbb0bc83b39c31fbbdeeecb8 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/ecdysis-bb4c64dbdf60/related-systems/cuiyu-ai--Ecdysis`. Implementation: all Python files under `src/ecdysis/`, `examples/quickstart.py`, and all seven `tests/` files named in the coverage table. Doctrine/design: `.gitignore`, `pyproject.toml`, `README.md`, `src/ecdysis/README.md`, and role prompts in `src/ecdysis/fdcr/roles.py`. Reported operation: README paper-result claims and expected synthetic output. | Implementation: [training](https://github.com/cuiyu-ai/Ecdysis/blob/cf93866d545b0974dbb0bc83b39c31fbbdeeecb8/src/ecdysis/training.py), [FDCR](https://github.com/cuiyu-ai/Ecdysis/blob/cf93866d545b0974dbb0bc83b39c31fbbdeeecb8/src/ecdysis/fdcr/review.py), [artifacts](https://github.com/cuiyu-ai/Ecdysis/blob/cf93866d545b0974dbb0bc83b39c31fbbdeeecb8/src/ecdysis/artifacts.py), [benchmark](https://github.com/cuiyu-ai/Ecdysis/blob/cf93866d545b0974dbb0bc83b39c31fbbdeeecb8/src/ecdysis/benchmark.py). Doctrine/design: [roles](https://github.com/cuiyu-ai/Ecdysis/blob/cf93866d545b0974dbb0bc83b39c31fbbdeeecb8/src/ecdysis/fdcr/roles.py), [packaging](https://github.com/cuiyu-ai/Ecdysis/blob/cf93866d545b0974dbb0bc83b39c31fbbdeeecb8/pyproject.toml). Doctrine/design and reported operation: [README](https://github.com/cuiyu-ai/Ecdysis/blob/cf93866d545b0974dbb0bc83b39c31fbbdeeecb8/README.md). | No access gaps within tracked source. External task runtimes, editors, benchmark datasets/adapters, dependency internals, services and linked paper are not captured. No inspected execution trace or causal experiment; synthetic test source and README performance claims cannot establish actual success, generalization, costs or paper-result reproducibility. |
