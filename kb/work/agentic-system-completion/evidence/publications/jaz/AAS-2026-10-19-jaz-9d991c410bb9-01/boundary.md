---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "JAZ's shipped Python agent runtime and console at commit 0803d4971be785e95b80054b02259664d70fa3da."
run-id: AAS-2026-10-19-jaz-9d991c410bb9-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "0803d4971be785e95b80054b02259664d70fa3da"
analysis-cutoff: "2026-10-19"
evidence-tier: code-grounded
source:
  identity: https://github.com/jaz-lang/JAZ
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-23-jaz/related-systems/jaz-lang--JAZ
  revision: "0803d4971be785e95b80054b02259664d70fa3da"
  sha256: null
---

# JAZ boundary

## Boundary and evidence

This run analyses how JAZ turns keyword inputs and Python tools into model-driven REPL execution, controls recursive invocations, returns results, and records or reuses execution state. JAZ qualifies as an agent system and is classified as an **enclosing runtime**: its own agent loop queries the model, parses the response, executes committed code, feeds observations back, and decides whether to continue or finish. It is not classified as merely a runtime client because an application can call `invoke`. SRC-1, `src/jaz/invoke.py`, `src/jaz/_agent.py`, and `src/jaz/repl/python_repl.py` establish these responsibilities.

The source's declared loop is:

> Agents execute in a REPL loop where the LLM generates code, observes results, and iterates until the task is complete.
> --- `README.md`

The inspected implementation connects model queries to execution through `do_one_repl_iteration`, including this committed-code call:

> exec_result = self.repl_template.exec(
>     state, span.committed_code, str(iteration), exec_timeout_override
> )
> --- `src/jaz/_agent.py`

The **whole-system** boundary is the package shipped in this repository, including its console driver, prompts, configuration and credentials, hook governance, recording/replay, and support utilities. It is not a claim to cover the authors' unshipped development or evaluation environment. Both installed `jaz` and `python -m jaz` lead to `jaz.console.main`; the console loads settings, builds its namespace, activates selected hooks, and dispatches interactive, command, file or piped input. The console is included, not treated as an external host. SRC-1, `pyproject.toml`, `src/jaz/__main__.py`, `src/jaz/console.py`.

> [project.scripts]
> jaz = "jaz.console:main"
> --- `pyproject.toml`

State-producing and consuming paths are included together. Public invocation builds an `Agent` and recursive invoke tool; the loop owns per-invocation REPL history and message observations. The console records completed or failed prompt turns and supplies prior live input/result objects to later invocations. Its model-setting writer and startup loader are also inside the boundary. Trajectory recording, trace loading and replay, workflow-package materialization, and return validation are included rather than dismissed as auxiliary callers. SRC-1, `src/jaz/invoke.py`, `src/jaz/_agent.py`, `src/jaz/console.py`, `src/jaz/hooks/builtin/atif_trace.py`, `src/jaz/hooks/builtin/replay.py`, `src/jaz/hooks/builtin/workflow_replay.py`, `src/jaz/hooks/builtin/return_hooks.py`.

> if history.turns:
>     extra["conversation_history"] = history
> try:
>     result = jaz.invoke(*hooks, task=task, **extra)
> --- `src/jaz/console.py`

### Tracked top-level coverage

The frozen Git tree contains the following five top-level entries. “Included” fixes functional scope; it does not mean every implementation line has already been inspected. Initial reads and bounded searches establish the entry points and material state loop. Files not yet individually read remain available to later jobs under SRC-1, not access gaps.

| Tracked entry | Treatment and material paths | Role and coverage limits |
|---|---|---|
| `README.md` | Included; read in full. | Source-native usage, configuration, recursive invocation, console, hook and backend contracts; doctrine/design, not proof of execution quality. |
| `pyproject.toml` | Included; read in full. | Distribution, dependencies, package data and installed console entry point. Pytest configuration does not itself supply tests or evaluation results. |
| `src/` | Included in full. Entry-point trace: `src/jaz/__main__.py` → `src/jaz/console.py` → `src/jaz/invoke.py` → `src/jaz/_agent.py`; core execution reaches `src/jaz/repl/python_repl.py` and the LLM backend layer, including `src/jaz/llm/_litellm.py`. | Produces and consumes invocation inputs, model messages, REPL state and returned values. Initial inspection covered selected loop, query/exec and driver ranges; not every async branch or alternative backend. Those remain in scope and inspectable. |
| `src/` (state and policy detail) | Same included directory, expanded for material coverage: `src/jaz/templates/`, `src/jaz/protocol/`, `src/jaz/repl/`, `src/jaz/hooks/`, `src/jaz/user_settings.py`, `src/jaz/credentials.py`, `src/jaz/paths.py`, `src/jaz/utils/`, and remaining package modules. | Prompt construction and permissions; hook admission/control; in-session history; settings/credentials persistence and reload; trajectory recording, replay and workflow materialization; tracing and artifact converters. Initial reads covered the system prompt and selected recorder/replay/validator implementations; symbol searches covered persistence loaders/writers. Other templates, permission internals, hook variants and converter internals are included but not yet individually inspected. |
| `CHANGELOG.md` | Included as attributed release history; initial read covered the 0.2.0a4 entry. | Provides declared changes and pointers, not observed runs or evidence that historical defects are absent. Older entries remain inspectable, not an access gap. |
| `LICENSE` | Deliberately excluded from operational analysis. | Legal terms, not a runtime path. This analysis makes no licensing or redistribution conclusion. |

The repeated `src/` row expands one tracked directory; it is not an additional source. No tracked test, benchmark, dataset or evaluator directory is present in this frozen tree. The README explains the publication boundary:

> This repository is generated: each release publishes a cleaned copy of the package, so
> changes are not made here. Contributor setup and code conventions live with the source.
> --- `README.md`

This limits conclusions about development-time optimization and evaluation. Shipped validators and replay hooks remain analysable, but absent evaluation tooling and results cannot establish benchmark performance, training gains, or the authors' complete improvement loop. SRC-1, `README.md`, `pyproject.toml`, `src/jaz/hooks/builtin/return_hooks.py`, `src/jaz/hooks/builtin/replay.py`.

### Frozen applicability and external dependencies

The reviewed boundary is exactly commit `0803d4971be785e95b80054b02259664d70fa3da`; the checkout's HEAD matched the acquired pin. The applicability cutoff is **2026-10-19**, the supplied run date. No later repository changes, live documentation, service responses or unregistered sources are evidence. This is a **code-grounded** analysis of the published implementation, supplemented by its own documentation. No target code, tests, examples or model calls were executed, and no observed-run or causal-experiment evidence was supplied.

External dependencies include the Python runtime, declared Python packages, provider services, optional telemetry services and user-supplied tools or data. JAZ's adapters and configuration for them are included; their implementations, actual service behavior and arbitrary consuming applications are excluded. Consequently the analysis cannot establish provider reliability, tool-side effects in a real application, sandbox resistance under attack, or end-to-end task success. The default LiteLLM adapter visibly delegates to `litellm.completion`/`litellm.acompletion`; that delegation is implementation evidence, not an observed provider call. SRC-1, `pyproject.toml`, `src/jaz/llm/_litellm.py`, `README.md`.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/jaz-lang/JAZ` | 0803d4971be785e95b80054b02259664d70fa3da | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-23-jaz/related-systems/jaz-lang--JAZ`. Tracked tree enumerated. Implementation: `pyproject.toml`, `src/jaz/__main__.py`; selected ranges and symbol searches in `src/jaz/invoke.py`, `src/jaz/_agent.py`, `src/jaz/console.py`, `src/jaz/repl/python_repl.py`, `src/jaz/llm/_litellm.py`, `src/jaz/hooks/builtin/atif_trace.py`, `src/jaz/hooks/builtin/replay.py`, `src/jaz/hooks/builtin/workflow_replay.py`, `src/jaz/hooks/builtin/return_hooks.py`; persistence searches in `src/jaz/user_settings.py` and `src/jaz/credentials.py`. Doctrine/design: full `README.md`, `src/jaz/templates/system_prompt.jinja2`, selected implementation docstrings and 0.2.0a4 `CHANGELOG.md`. Listed paths describe initial inspection, not an allowlist. | Implementation: [entry point](https://github.com/jaz-lang/JAZ/blob/0803d4971be785e95b80054b02259664d70fa3da/pyproject.toml), [console caller](https://github.com/jaz-lang/JAZ/blob/0803d4971be785e95b80054b02259664d70fa3da/src/jaz/console.py), [agent loop](https://github.com/jaz-lang/JAZ/blob/0803d4971be785e95b80054b02259664d70fa3da/src/jaz/_agent.py), [trace consumer](https://github.com/jaz-lang/JAZ/blob/0803d4971be785e95b80054b02259664d70fa3da/src/jaz/hooks/builtin/replay.py). Doctrine/design: [README](https://github.com/jaz-lang/JAZ/blob/0803d4971be785e95b80054b02259664d70fa3da/README.md), [system prompt](https://github.com/jaz-lang/JAZ/blob/0803d4971be785e95b80054b02259664d70fa3da/src/jaz/templates/system_prompt.jinja2). | No access gap within the registered checkout. Unshipped development/evaluation environment and external dependency implementations are outside the frozen source; no supplied runs or experiments establish operational success, safety or causal improvement. Deliberate license exclusion and material not yet individually inspected are distinguished above. |
