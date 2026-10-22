---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Harness²'s shipped recursive harness-improvement framework and persistent experience loop at commit 1cfe254e8d25b15f37048c3730134686abe60335."
run-id: AAS-2026-10-22-harness2-d5a180ba559c-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: whole-system
reviewed-boundary: "1cfe254e8d25b15f37048c3730134686abe60335"
analysis-cutoff: "2026-10-22"
evidence-tier: code-grounded
source:
  identity: https://github.com/google-research/harness2
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/harness2-meta-audit-d5a180ba559c/related-systems/google-research--harness2
  revision: "1cfe254e8d25b15f37048c3730134686abe60335"
  sha256: null
---

# Harness² boundary

## Boundary and evidence

This run characterizes the shipped Harness² framework: a model-dependent improvement plane that edits execution harnesses, probes them through benchmark executors, composes refinements, selects outputs and retains adopted harnesses with lessons for later tasks. The intended use is to explain that framework's control and persistence mechanisms, not to reproduce its paper's performance claims. The target is in scope because its improvement stages issue model calls and consume execution evidence; it is not merely a static harness template. SRC-1: `README.md`, `harness2/cli/run_sweep.py`, `harness2/core/proposer.py`, `harness2/core/recursion.py`.

The boundary is **whole-system for the shipped improvement framework**, not for the internals of the external agent runtimes and benchmark platforms it invokes. It includes the command-line drivers, benchmark adapters, substrate integration, prompt contracts, validation of proposed trees and evidence, selection and reflection, experience-library persistence and reload, resume logic, judging and reporting, setup and bundled runner overlays. Callers inside this repository are included: the CLI and domain scheduler supply the persistent loop rather than constituting an excluded host application. SRC-1: `pyproject.toml`, `harness2/core/schedule.py`, `harness2/core/library.py`, `harness2/core/context.py`, `harness2/core/selection.py`, `harness2/install.py`.

The declared purpose is explicit:

> Harness² is a plug-and-play framework for **recursive agent harnessing** in an
> open world, where agents encounter tasks unseen during harness design. It
> connects two levels of recursion while keeping model weights fixed:
> --- `README.md`

The source trace establishes that persistence and later consumption belong to the shipped framework. The `harness2` entry point constructs a benchmark adapter and proposer, then calls `schedule.run_sweep` with a library root. `run_domain` constructs per-mode domain libraries, retains only preceding task entries and passes those libraries into `run_task`. `_run_one_mode` obtains `context_dir()`, supplies it to recursion, reflects after successful selection and adds the adopted tree when experience has the required fields. `context.build` copies that library into the improver's evidence tree. This is a source-level trace, not an observed execution. SRC-1: `harness2/cli/run_sweep.py`, `harness2/core/schedule.py`, `harness2/core/library.py`, `harness2/core/context.py`.

> """Every task in one domain, in `stream_order()` order, threading the library forward."""
> --- `harness2/core/schedule.py`

> """Store one adopted harness plus why it was adopted, and rebuild INDEX.md from disk.
>
>         The tree is checked for grader verdicts before anything is written.
>         """
> --- `harness2/core/library.py`

Reflection is part of this boundary, including its prompt instructions about evidence, abstention and transfer. Those instructions establish intended behavior, not proof that a model follows them. SRC-1: `harness2/core/selection.py`, `harness2/core/prompts.py`.

> "Adoption alone never establishes that an edit helped or will transfer. If the record "
> "shows no concrete, reusable execution contrast, write the single line NO_ENTRY in "
> "place of the <experience> block -- the edit rows are still worth writing.",
> --- `harness2/core/prompts.py`

### Repository coverage

The tracked root tree was enumerated at the reviewed commit. Every top-level tracked file or directory is classified below. “Included” fixes functional scope; it does not claim exhaustive line-by-line inspection. Detailed initial reads trace the improvement and retention loop; symbol searches and tree inventory identify supporting paths for subsequent inspection within SRC-1. Material not yet inspected is distinguished from unavailable evidence.

| Top-level path | Classification and role | Initial inspection and limits |
|---|---|---|
| `README.md` | Included: declared purpose, usage, model-backed workflow, results and resume | Read completely; performance statements are reported claims, not observed results. |
| `pyproject.toml` | Included: package and seven installed CLI entry points | Read; traces refinement, judge, report, setup, check, demo and bridge destinations. |
| `harness2/` | Included: executable improvement framework | Detailed reads: `cli/run_sweep.py`; `core/schedule.py` domain and task-mode drivers; `core/recursion.py` parallel driver; `core/library.py` admission, persistence and index; `core/context.py` evidence construction; `core/selection.py` reflection; `core/prompts.py` experience contract; `core/judge.py` scoring; `substrate/opencode.py` and `substrate/codex.py` materialization and execution interfaces; `benchmarks/jobbench.py`, `benchmarks/lab.py`, `benchmarks/workbuddy.py` rollout launch and cache paths; `install.py` overlays. Symbol searches located proposer calls, selection, judge/report/setup/bridge drivers and adapter scoring. Sequential recursion, remaining prompt families, tree/spec/ledger/runmark internals, config/preflight, demo, rendering and full report/bridge bodies remain included but not yet deeply inspected. |
| `docs/` | Included: operation and evaluation doctrine | Read `EXPERIMENTS.md`; inventoried `SETUP.md` and `BENCHMARKS.md`, not yet read. These latter files are available, not access gaps. |
| `scripts/` | Included: benchmark driver shells, setup, partitioning and provenance utilities | Read `run_jobbench.sh`: check → refinement → judge → report; inventoried parallel LAB/WorkBuddy drivers and Python utilities, not yet fully read. |
| `third_party/` | Included: bundled runner overlays, baseline prompts/configurations, compatibility patches and provenance | Read `README.md`; inventoried `jb_runner/` baseline `AGENTS.md`, OpenCode prompt/memory/guardrail tree and Codex runner; `lab_runner/` OpenCode rendering/session/runner and Codex runner; `wb_runner/` agent implementations and harness configurations; `patches/` and `licenses/`. Symbol searches located LAB runner construction and WorkBuddy harness-agent hooks. Baseline prompt contents, runner bodies and patch details remain available for later inspection; they are not excluded host responsibilities. Setup's copy destinations were traced in `harness2/install.py`. |
| `dependencies/` | Included: dependency provenance and pin declarations, not downloaded upstream implementations | Read `PINNED.md`; inventoried `ASSETS.json` and `README.md`. This tracked directory registers inputs; external checkouts/data downloaded by setup are outside SRC-1. |
| `tests/` | Included: test contracts for recursion, resume, library prefixes, failed selection and proposer isolation | Inventoried and searched `test_workflow.py`; read its evidence/library-prefix test. Tests were not executed and supply implementation expectations, not observed runs. |
| `MANIFEST.in` | Included: distribution inventory | Read; packaging declarations alone do not prove installed-wheel contents or setup success. |
| `assets/` | Excluded: presentation images, animation and video | Tree inventory only. No independent interpretation of visual demonstrations or video behavior is supported. Mechanism scope uses source and text, not these media. |
| `CONTRIBUTING.md` | Excluded: contribution administration | Inventoried, not read; no conclusions about contributor process. |
| `LICENSE` | Excluded: licensing text | Inventoried, not read; no legal or license-compliance judgment. |

### Frozen evidence and external dependencies

The sole frozen source is SRC-1 at full Git commit `1cfe254e8d25b15f37048c3730134686abe60335`; the checkout's HEAD was checked against the acquired pin. The source mapping above preserves acquisition's identity, revision, path, kind and null digest. The analysis cutoff is 2026-10-22: this is an applicability cutoff for that snapshot, not evidence of the latest upstream behavior or model deployment on that date. The overall evidence tier is **code-grounded**, with source-native documentation and prompt contracts providing a distinct doctrine/design layer.

OpenCode, Codex, benchmark repositories/data, model endpoints and credentials, operating-system utilities and WorkBuddy's container platform are external dependencies. Substrates materialize harnesses but delegate execution to benchmark-supplied launchers; the adapters invoke runner commands and read their artifacts. The shipped adapters, overlays and patches are included; the complete downloaded upstream systems are not. Dependency pin declarations do not make those repositories additional frozen sources. This prevents attributing their complete tool loops, provider behavior or grading correctness to Harness². SRC-1: `harness2/substrate/opencode.py`, `harness2/substrate/codex.py`, `harness2/benchmarks/jobbench.py`, `harness2/benchmarks/lab.py`, `harness2/benchmarks/workbuddy.py`, `dependencies/PINNED.md`.

No target code, tests or examples were executed, and no runtime artifacts or controlled experiments were supplied. Therefore this boundary supports source-grounded control-flow and contract conclusions, not measured success, causal improvement, lesson validity, contamination resistance or paper-result reproduction. The paper and website linked by the README were not acquired and are not evidence. The experiment guide's account of a rollout retrieving a public rubric is reported operation only; no corresponding trace was inspected. SRC-1: `README.md`, `docs/EXPERIMENTS.md`.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/google-research/harness2` | 1cfe254e8d25b15f37048c3730134686abe60335 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/harness2-meta-audit-d5a180ba559c/related-systems/google-research--harness2`. Implementation: root tree, package entry points, CLI sweep, scheduler, recursion, library, context, reflection, judge, substrate materialization/delegation, three benchmark rollout adapters and setup overlays, as detailed in the coverage table. Doctrine/design: README, experiment guide, experience prompt and dependency/bundled-code notices. Reported operation: README performance statements and experiment-guide rubric-download anecdote. | Implementation: [entry points](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/pyproject.toml), [persistent-loop caller](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/schedule.py), [library](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/library.py), [reflection](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/selection.py). Doctrine/design: [experience prompt](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/prompts.py), [pins](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/dependencies/PINNED.md). Reported operation: [README](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/README.md), [experiments](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/docs/EXPERIMENTS.md). | No supplied observed-run or causal-experiment evidence; no acquired complete external executor/benchmark implementations, datasets or provider deployments. Prevents empirical efficacy, causal attribution, end-to-end runtime/grade correctness and historical-result reproduction claims. Available but not yet deeply inspected material is identified in the coverage table, not treated as unavailable. |
