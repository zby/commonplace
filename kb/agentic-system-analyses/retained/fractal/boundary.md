---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Fractal's shipped CLI, session lifecycle and PredictRLM integration at commit 6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385."
run-id: AAS-2026-10-14-fractal-ee03010af4c2-01
result-disposition: complete
target-class: runtime client
boundary-kind: whole-system
reviewed-boundary: "6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/trampoline-ai/fractal
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/fractal-ee03010af4c2/related-systems/trampoline-ai--fractal
  revision: 6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385
  sha256: null
---

# Fractal boundary

## Boundary and evidence

This run analyses Fractal as a terminal coding agent and headless delegation interface, including its own durable session state and the paths that consume that state on subsequent turns. It is in scope because shipped executable code constructs and calls a model-dependent PredictRLM computation, rather than merely returning static tool data (SRC-1, `src/fractal/agent/service.py`).

The target class is **runtime client**: Fractal owns request admission, terminal presentation, provider selection, session persistence and resumption, and configuration of the delegated computation. PredictRLM supplies the inner model/code execution loop. The name `FractalRuntime` does not establish ownership of that inner loop. The boundary is **whole-system** for the Fractal artifact, not a claim to cover the implementation of its separately distributed dependencies. Both interactive and headless drivers are included, as are bundled calling recipes; none is excluded as an external host merely because it invokes an API (SRC-1, `pyproject.toml`, `src/fractal/cli.py`, `src/fractal/runtime.py`, `src/fractal/agent/service.py`, `.agents/skills/fractal/RECIPES.md`).

The shipped command resolves to this entry point:

> [project.scripts]
> fractal = "fractal.cli:main"
> --- `pyproject.toml`

The implementation constructs the delegated runtime and awaits its call:

> predictor = PredictRLM(signature, **predictor_kwargs)
> --- `src/fractal/agent/service.py`

> await predictor.acall(
>     workspace=workspace,
>     included_paths=included_workspaces or None,
>     user_message=user_message,
>     session_history=session_history or [],
> ),
> --- `src/fractal/agent/service.py`

The traced state loop is admission through `cli.py` or `tui/app.py`, pending-turn persistence in `runtime.py`, prompt/history preparation in `session.py` and `agent/signature.py`, execution delegation in `agent/service.py`, and result/error persistence followed by later loading and rendering. Both the interactive `/resume` path and headless `--resume` path reach `FractalRuntime.resume`. Full history is bounded by the session implementation; structured summary and retained traces are distinct inputs to later computation (SRC-1, `src/fractal/cli.py`, `src/fractal/tui/app.py`, `src/fractal/runtime.py`, `src/fractal/session.py`, `src/fractal/agent/signature.py`).

> def session_history_payload(self) -> list[SessionHistoryTurn]:
>     # Full traces can be large. The structured summary is the durable
>     # compressed trajectory, so history is bounded to exact-recall data.
>     self._enforce_history_limit()
>     return list(self.state.history)
> --- `src/fractal/session.py`

Workspace mutation, additional mounts, root `AGENTS.md` loading, filesystem skill instructions, runtime event accounting, and sandbox lifecycle configuration are included. The corresponding behavior inside PredictRLM, its document skills, DSPy/model adapters, Docker SBX, model services and arbitrary user projects is external. Their source and execution are not supplied here. This prevents conclusions about internal recursive scheduling, actual sandbox isolation, model quality, or end-to-end reliability beyond Fractal's visible configuration and call sites (SRC-1, `src/fractal/agent/service.py`, `src/fractal/agent/signature.py`, `src/fractal/agent/skills.py`, `src/fractal/runtime_lms.py`, `pyproject.toml`). User project instructions and state are runtime inputs, not frozen evidence in this run.

The frozen source is the acquired Git checkout at **6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385**. HEAD was checked against that pin; the checkout was read only. Applicability is cut off at **2026-10-14**, the supplied run date, and does not extend to later releases or moving websites. The overall tier is **code-grounded**. Documentation supplies declared intent, while test source supplies inspectable checks, not observed executions. No target command, test, example or provider was executed. There is no observed-run or causal-experiment evidence.

### Tracked top-level coverage

Every top-level tracked entry is classified below. All paths refer to SRC-1. “Indexed” means paths or definitions were inspected, not that every file body was read; it is not an access gap. Included paths remain within the frozen source for later inspection. No material shipped state-loop path was inaccessible.

| Top-level entry | Boundary status and role | Initial inspection and limit |
| --- | --- | --- |
| `.agents/` | Included: headless caller guidance and development maintenance instructions. | Read `.agents/skills/fractal/SKILL.md` and the delegation/resume portion of `.agents/skills/fractal/RECIPES.md`; indexed `.agents/skills/fractal_add_provider/SKILL.md`. Recipes and skill are declared calling practice, not evidence that a host executed them. |
| `.github/` | Included: shipped test/release automation. | Indexed `.github/workflows/tests.yml` and `.github/workflows/release.yml`, including their test/build commands. No CI results inspected; successful CI cannot be inferred. |
| `.gitignore` | Included: repository hygiene. | Tree inventoried; body not yet inspected. No conclusion about ignored runtime state follows from this file. |
| `.python-version` | Included: development interpreter selection. | Tree inventoried; body not yet inspected. Interpreter compatibility is not experimentally established. |
| `AGENTS.md` | Included: project maintenance doctrine. | Indexed architecture, session, testing and caveat sections; not treated as executable authority for this analysis. |
| `CHANGELOG.md` | Included: attributed release history. | Inventoried, not yet inspected; no historical release claim used. |
| `CONTRIBUTING.md` | Included: developer setup, checks and provider-maintenance guidance. | Indexed setup, checks, credential and provider sections; no setup executed. |
| `LICENSE` | Included: distribution terms. | Inventoried, not yet inspected; no legal assessment made. |
| `README.md` | Included: product intent, setup, usage and claimed mechanism. | Read opening through architecture/requirements and start of the worked example. Capability and “no context rot” language is doctrine, not a measured result. |
| `assets/` | Excluded: branding images and SVG. | Inventoried logo assets. Exclusion prevents assessment of visual presentation, not the agent state loop. |
| `docs/` | Included: operator contracts. | Read `docs/headless.md`, `docs/session-management.md`, and opening provider/setup section of `docs/config.md`. Remaining configuration detail is available but not yet inspected. |
| `fractal-remotion/` | Excluded: release-video project, not a runtime caller. | Read `fractal-remotion/README.md`; inventoried `src/Composition.tsx`, `src/Root.tsx`, `src/index.ts`, package/config files and public assets. Exclusion prevents assessment of animation and promotional accuracy; it does not exclude an agent execution path. |
| `install.sh` | Included: installation and prerequisite checks. | Indexed installer steps, tool installation and SBX checks. Installer body not exhaustively traced; installation success not established. |
| `pyproject.toml` | Included: dependency, package, command and test-selection contracts. | Read completely, including `fractal.cli:main`, `predict-rlm[sbx]` dependency and integration-test marker. |
| `src/` | Included: all shipped Fractal implementation. | Traced `src/fractal/cli.py`, `runtime.py`, `agent/service.py`, `agent/signature.py`, `session.py`, and `tui/app.py` across admission, saving, resuming and consumption. Read portions of `agent/skills.py`, `runtime_lms.py`, and `context_meter.py`. Indexed supporting `config.py`, `config_commands.py`, `credentials.py`, `providers.py`, `onboarding.py`, `connectivity.py`, `events.py`, and `version_check.py`; these admission/configuration/accounting paths remain included, with detailed implementations not yet fully inspected. `agent/schema.py`, `errors.py`, and package initializers were inventoried rather than fully read. |
| `tests/` | Included: executable contracts and evaluators. | Indexed session, runtime, headless JSON and interrupt-recovery tests; read the pending/success runtime test and integration-test setup. Inventoried provider/config, CLI/TUI, event, context-meter, error, connectivity, credential, smoke and version-check suites and `tests/conftest.py`. No test result or performance measurement supplied. |
| `uv.lock` | Included: dependency resolution evidence. | Inventoried, not yet inspected. Exact resolved dependency versions and implementations are not established by reading only package constraints. |

Documentation can lag implementation. In particular, the bundled calling skill and recipe describe workspace-local session files, whereas `src/fractal/session.py` and `docs/session-management.md` establish workspace-keyed global state. Both remain included; documentation is not substituted for the persistence implementation (SRC-1, `.agents/skills/fractal/SKILL.md`, `.agents/skills/fractal/RECIPES.md`, `src/fractal/session.py`, `docs/session-management.md`).

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/trampoline-ai/fractal` | 6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/fractal-ee03010af4c2/related-systems/trampoline-ai--fractal`. Implementation: entry point, both CLI drivers, runtime state lifecycle, agent call/mount setup, signature construction, session persistence/loading/rendering, TUI submit/resume/listing, context-message estimator and representative test source. Supporting implementation definitions and automation indexed as described in the coverage table. Doctrine/design: README opening, headless/session docs, config opening, filesystem instruction opening, caller skill and multi-turn recipe, maintenance guidance and release-video description. | Implementation: [package/entry point](https://github.com/trampoline-ai/fractal/blob/6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385/pyproject.toml), [CLI](https://github.com/trampoline-ai/fractal/blob/6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385/src/fractal/cli.py), [runtime](https://github.com/trampoline-ai/fractal/blob/6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385/src/fractal/runtime.py), [agent](https://github.com/trampoline-ai/fractal/blob/6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385/src/fractal/agent/service.py), [session](https://github.com/trampoline-ai/fractal/blob/6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385/src/fractal/session.py), [TUI](https://github.com/trampoline-ai/fractal/blob/6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385/src/fractal/tui/app.py). Doctrine/design: [README](https://github.com/trampoline-ai/fractal/blob/6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385/README.md), [session contract](https://github.com/trampoline-ai/fractal/blob/6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385/docs/session-management.md), [caller recipes](https://github.com/trampoline-ai/fractal/blob/6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385/.agents/skills/fractal/RECIPES.md). Additional local anchors appear in the coverage table and prose. | No inaccessible Fractal checkout material identified. External dependency implementations, user workspaces and real services are outside this frozen source. No inspected execution trace or experiment: runtime reliability, model capability, isolation and causal benefits cannot be established. Available but unread files are initial-inspection limits, not access gaps. |
