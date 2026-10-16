---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "auto-harness's shipped agent-improvement plane at Git revision 52360dbbeb8cea8886d90778e634a145c51da735."
run-id: AAS-2026-10-15-auto-harness-92303e444cb2-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: whole-system
reviewed-boundary: "52360dbbeb8cea8886d90778e634a145c51da735"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/neosigmaai/auto-harness
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-auto-harness/related-systems/neosigmaai--auto-harness
  revision: 52360dbbeb8cea8886d90778e634a145c51da735
  sha256: null
---

# auto-harness boundary

## Boundary and evidence

The target is the shipped auto-harness agent-improvement plane: instructions for an external coding agent, benchmark adapters, candidate agent templates, persistent experiment state, regression gating and iteration recording. Its intended use is to improve an agent against benchmark rewards through repeated edits and evaluations. This is in scope because its operation depends on model-driven candidate agents and a model-driven coding agent, rather than being a standalone deterministic benchmark utility. The primary class is **builder or improvement plane**, not an enclosing coding-agent runtime (SRC-1, `program_templates/base.md`, `benchmark.py`, `agent/templates/terminal_bench.py`).

The shipped loop's contract states:

> You are an autonomous coding agent optimizing `agent/agent.py` to perform better on a benchmark. You run a tight loop:
> --- `program_templates/base.md`

Its outer execution is delegated to a user-supplied coding agent. The repository supplies the program and commands, not that agent's own scheduler, model transport or context management. The README's launch procedure is explicit:

> Point your coding agent at the repo and prompt:
> --- `README.md:162-162`

The **whole-system** boundary covers the repository's shipped improvement system, including its local candidate-agent implementations and BIRD service/runtime wrapper. It does not mean the external coding agent or benchmark frameworks are implemented here. The local drivers are included, even where they hand work to external frameworks: `benchmark.py` imports the tau candidate, passes the Terminal candidate's import path to Harbor, and starts the harness-owned BIRD system-agent service alongside external services (SRC-1, `benchmark.py`).

Entry-point tracing establishes the state loop at source level. `prepare.py` validates dependencies, initializes the workspace, selects agent/program templates and records a baseline. `benchmark.py` executes configured tasks, extracts rewards, writes the latest result mapping and, on the Terminal/BIRD train paths, copies traces. `gating.py` reloads the suite, prior training results and score history; it evaluates the candidate and promotes newly passing training tasks. `record.py` appends an iteration row with the current commit and caller-supplied scores. The program instructs the coding agent to analyze failures, edit, gate, commit, record and append learnings. These are all included responsibilities, not excluded callers (SRC-1, `prepare.py`, `benchmark.py`, `gating.py`, `record.py`, `program_templates/base.md`). For example, the gate's implementation connects retained training results to later admission:

> train_results = load_train_results()
> --- `gating.py`

> newly_fixed = sorted(tid for tid, r in recheck.items() if r is not None and r >= 0.5)
> --- `gating.py`

> suite["tasks"] = sorted(suite_set | set(newly_fixed))
> --- `gating.py`

This establishes shipped behavior and intended operator sequencing, not an observed successful optimization run. In particular, the recorder accepts score arguments; the boundary does not imply an independently authenticated gate-to-record transaction (SRC-1, `record.py`).

### Repository coverage

Every top-level tracked item is classified below. All rows refer to SRC-1; code paths describe implementation evidence, while prose and templates also supply doctrine/design evidence. Included means part of the functional boundary, not that every sentence has been exhaustively analyzed. The entry-point and state-consumer paths above were inspected; no material shipped loop component was left unavailable. Documentation inspection was targeted to the purpose, component map, launch instructions and benchmark-specific programs.

| Top-level item | Classification and material paths inspected | Role and exclusion consequence |
|---|---|---|
| `.env.example` | Included; `.env.example` | Model and sandbox credential interface; no actual credentials or provider behavior established. |
| `.gitignore` | Included; `.gitignore` | Distinguishes ignored workspace, configuration and externally provisioned data/ADK paths from tracked source. |
| `Dockerfile` | Included; `Dockerfile` | Python/uv dependency environment and interactive container entry point. |
| `LICENSE` | Excluded deliberately; identified in tracked tree, contents not inspected | Licensing is outside operational analysis; no licensing or reuse-permission conclusion. |
| `PROGRAM.md` | Included; `PROGRAM.md` | Tracked placeholder, composed from program templates by preparation; not itself a completed experiment program at this pin. |
| `README.md` | Included; `README.md` purpose/component map and running-loop/template sections | Declared purpose and external coding-agent launch; narrative performance claims are not treated as measured evidence. |
| `agent/` | Included; `agent/agent.py`, `agent/templates/tau_bench.py`, `agent/templates/terminal_bench.py`, `agent/templates/bird_interact.py`, `agent/helpers/bird_interact/setup.py`, `agent/helpers/bird_interact/bird_service.py`, `agent/helpers/bird_interact/bird_adk_runtime.py`; package initializers identified in tree | Placeholder candidate; three benchmark-specific candidate implementations; provisioning; HTTP session entry points; ADK runner/session/event wrapper. Candidate consumers traced through `benchmark.py` and the wrapper's import of `agent.agent`. |
| `benchmark.py` | Included; `benchmark.py` | Shared scoring API, tau registration and execution, Harbor subprocess/results/traces, BIRD service lifecycle and orchestrator handoff, task selection, trace copying and CLI result persistence. |
| `docker-compose.yml` | Included; `docker-compose.yml` | Credentials, model/data environment and source/workspace volume mounts. |
| `experiment_config.yaml.template` | Included; `experiment_config.yaml.template` | Configuration examples for all three integrations; not an actual experiment configuration. |
| `gating.py` | Included; `gating.py` | File guard, suite reload/update, best-score reload, regression/test checks, promotion and configured runner construction. |
| `prepare.py` | Included; `prepare.py` | Dependency/data checks, state initialization, candidate/program generation, split generation and baseline recording. |
| `program_templates/` | Included; `program_templates/base.md`, `program_templates/tau_bench.md`, `program_templates/terminal_bench.md`, `program_templates/bird_interact.md` | Outer coding-agent procedure, learning-log maintenance, stop/revert rules, trace-use restrictions and benchmark-specific edit guidance. |
| `pyproject.toml` | Included; `pyproject.toml` | Packaging/dependencies, including the declared tau2 Git dependency revision. |
| `record.py` | Included; `record.py` | Post-commit file guard and append-only iteration history consumed by future gating. |

### External dependencies and limits

The frozen evidence is solely the acquired Git repository at **52360dbbeb8cea8886d90778e634a145c51da735**, with applicability cutoff **2026-10-15**. The checkout's HEAD matched that revision and its working tree was clean when inspected. Overall evidence tier is **code-grounded**. No target programs, tests, examples or model calls were executed.

The external coding-agent runtime is deliberately excluded. The included program governs requested behavior, but this evidence cannot establish that an actual coding agent obeys its edit limits, learning updates, test-data restrictions or stopping rule (SRC-1, `program_templates/base.md`, `README.md`).

External tau2, Harbor, Google ADK, LiteLLM/model services, sandbox providers and BIRD-Interact-ADK are dependencies, not additional frozen sources. Included code supports conclusions about local imports, configuration, service starts and handoffs; their internal scheduling, tool execution, verifier correctness, isolation and provider reliability cannot be independently established here. The BIRD system-agent HTTP wrapper and ADK session adapter remain included; the external orchestrator, simulator, database service and callback/tool implementations do not become local responsibilities merely because the adapter invokes them (SRC-1, `benchmark.py`, `agent/helpers/bird_interact/bird_service.py`, `agent/helpers/bird_interact/bird_adk_runtime.py`, `agent/templates/bird_interact.py`, `pyproject.toml`).

Benchmark datasets, BIRD gold SQL, actual experiment configuration, generated workspace histories, learned agent revisions and runtime traces were not supplied as frozen evidence. Their absence prevents verification of task content, concrete scores, learning retention in operation, end-to-end success or causal improvement. Local provisioning and split-generation code is available and included; unavailable downstream data is not evidence that those local paths are missing (SRC-1, `prepare.py`, `agent/helpers/bird_interact/setup.py`, `.gitignore`). No README improvement claim or program-template technique estimate is promoted to observed-run or causal-experiment evidence.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/neosigmaai/auto-harness` | 52360dbbeb8cea8886d90778e634a145c51da735 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-auto-harness/related-systems/neosigmaai--auto-harness`. Implementation: `prepare.py`, `benchmark.py`, `gating.py`, `record.py`, all three `agent/templates/` candidates, `agent/agent.py`, BIRD setup/service/runtime helpers, packaging/container/configuration files listed above. Doctrine/design: `README.md` purpose/component map and launch/template sections, `PROGRAM.md`, all four `program_templates/` files. Initial inspection paths are not an allowlist. | Implementation: [preparation](https://github.com/neosigmaai/auto-harness/blob/52360dbbeb8cea8886d90778e634a145c51da735/prepare.py), [benchmark execution](https://github.com/neosigmaai/auto-harness/blob/52360dbbeb8cea8886d90778e634a145c51da735/benchmark.py), [gate](https://github.com/neosigmaai/auto-harness/blob/52360dbbeb8cea8886d90778e634a145c51da735/gating.py), [recorder](https://github.com/neosigmaai/auto-harness/blob/52360dbbeb8cea8886d90778e634a145c51da735/record.py), [BIRD runtime wrapper](https://github.com/neosigmaai/auto-harness/blob/52360dbbeb8cea8886d90778e634a145c51da735/agent/helpers/bird_interact/bird_adk_runtime.py). Doctrine/design: [outer program](https://github.com/neosigmaai/auto-harness/blob/52360dbbeb8cea8886d90778e634a145c51da735/program_templates/base.md), [launch documentation](https://github.com/neosigmaai/auto-harness/blob/52360dbbeb8cea8886d90778e634a145c51da735/README.md). | No checkout access gap for inspected shipped paths. External dependency internals, benchmark data/gold answers and concrete run artifacts are outside the supplied frozen source; no independent external-runtime, verifier-validity, achieved-performance or causal-improvement conclusion. Doctrine is a contract, not demonstrated compliance. LICENSE is deliberately outside operational scope, not unavailable evidence. |
