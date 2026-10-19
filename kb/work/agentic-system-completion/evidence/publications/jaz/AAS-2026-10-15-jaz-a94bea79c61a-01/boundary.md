---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "JAZ's shipped Python agent runtime and console at commit 0803d4971be785e95b80054b02259664d70fa3da."
run-id: AAS-2026-10-15-jaz-a94bea79c61a-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: 0803d4971be785e95b80054b02259664d70fa3da
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/jaz-lang/JAZ
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/jaz-a94bea79c61a/related-systems/jaz-lang--JAZ
  revision: 0803d4971be785e95b80054b02259664d70fa3da
  sha256: null
---

# JAZ boundary

## Boundary and evidence

The target is the JAZ package distributed by this repository, including its shipped console, experimental components and retained-execution tooling. The intended use is to explain how this package runs model-directed Python agents, carries state through iterations and recursive calls, controls execution through hooks, and records or reuses execution content. This is not an analysis of an arbitrary application built with JAZ.

JAZ qualifies as an **enclosing runtime**, with a **whole-system** boundary: it owns the model-query/REPL iteration loop and terminal result handling, even when a Python application starts it through a library call. A callable API is not the complete target in isolation. The installed console and module entry point are shipped consumers and remain included. SRC-1, `pyproject.toml`, `src/jaz/__main__.py`, `src/jaz/invoke.py`, `src/jaz/_agent.py` and `src/jaz/console.py` establish these entry points and responsibilities.

The package declares its loop directly:

> An agent runs as a conversation with a Python REPL: the LLM writes code, sees what it
> evaluated to, and iterates until it finishes with a native ``return`` (or ``raise``)::
> --- `src/jaz/__init__.py`

The implementation builds an `Agent` for an invocation, initializes run-local REPL state and opening messages, repeatedly calls `do_one_repl_iteration`, appends observations for `Continue`, and completes on `Return` or `Raise`. The sync and async paths are both within scope. SRC-1, `src/jaz/invoke.py` and `src/jaz/_agent.py` supply implementation evidence; this is not merely a README classification.

> repl_iter_result = self.do_one_repl_iteration(
>     i,
>     depth,
>     can_recurse,
>     messages,
>     state,
>     invoke_id,
>     repl_history=repl_history,
> )
> --- `src/jaz/_agent.py`

The functional boundary includes input resolution and descriptions, scoped values and recursive invocation, configuration, protocol and prompt rendering, Python execution and permission controls, model adapters and accounting, hooks and their state/effects, console history and settings, trace production and replay, workflow materialization, rollout collection and trace/log utilities. Provider infrastructure and caller-defined tool implementations are external dependencies, not capabilities implemented by JAZ. The shipped SWE tool implementation is included rather than treated as an external caller.

The console is material to the state loop. Its chat wrapper passes earlier session turns into subsequent invocations and records both results and exceptions; its namespace creates fresh main/helper histories. It also persists model defaults and reloads them at console startup. These are JAZ responsibilities, not duties assigned to an excluded application. SRC-1, `src/jaz/console.py`:

> if history.turns:
>     extra["conversation_history"] = history
> --- `src/jaz/console.py`

The evidence boundary is Git revision **0803d4971be785e95b80054b02259664d70fa3da**, applicable through **2026-10-15**. The acquired checkout's HEAD matches that pin and its status was clean when inspected. The source object above is unchanged from acquisition. Evidence is **code-grounded**: source text establishes implemented paths, while package documentation and inline contracts establish declared intent. No target code, examples or tests were executed. No observed-run or causal-experiment evidence is registered.

### Shipped-path coverage

The tracked root contains exactly `CHANGELOG.md`, `LICENSE`, `README.md`, `pyproject.toml` and `src/`. The table accounts for each; subdivisions of `src/` distinguish material responsibilities. “Included” defines the analytical boundary, not a claim that every line has already been audited. Initially inspected source ranges are recorded below; available but uninspected implementation details are not access gaps and remain available to subsequent jobs under SRC-1.

| Top-level tracked path / material paths | Treatment | Role and initial inspection | Exclusion or inspection limit and conclusion prevented |
|---|---|---|---|
| `README.md` | Included | Package purpose, user-facing API, console, hook and backend contracts; read completely. | Documentation supports attributed intent, not successful operation. |
| `pyproject.toml` | Included | Distribution/version, dependencies, optional extras, package assets and installed `jaz = "jaz.console:main"` entry point; read completely. | Test configuration is not evidence that tests ship or pass. |
| `CHANGELOG.md` | Excluded | Release history; listed in tracked tree but not read. | No historical development or release-by-release behavior claims. |
| `LICENSE` | Excluded | Licensing text; listed but not read. | No licensing assessment. |
| `src/`: `jaz/__init__.py`, `jaz/__main__.py`, `jaz/agent.py`, `jaz/invoke.py`, `jaz/_agent.py`, `jaz/_invoke_tool.py` | Included | Public/export and module entry points; invocation construction, recursion binding, core sync loop, async query path. Export/module/shim files read completely; construction and loop inspected in bounded ranges. | Async parity, all hook interactions and recursion edge cases require further implementation tracing; no execution evidence. |
| `src/`: `jaz/console.py`, `jaz/user_settings.py`, `jaz/credentials.py`, `jaz/paths.py`, `jaz/instantiate.py` | Included | Shipped interactive/one-shot/file/stdin driver; session history admission/consumption; setup and settings persistence/reload; credential storage/loading. Inspected console history wrapper, namespace, settings writer/loader and `main`; searched persistence functions in settings and credentials. | Credential policy and helper confirmation details are not fully audited here. These files are available, not excluded or inaccessible. |
| `src/`: `jaz/protocol/`, `jaz/templates/`, `jaz/templates.py`, `jaz/template_loader.py`, `jaz/grammar.txt` | Included | Model-facing protocol, prompt construction and shipped templates. Read system template and protocol/history declaration; located parse and opener methods. | Other template bodies and exact rendering rules remain for mechanism analysis; no claim about model compliance. |
| `src/`: `jaz/repl/`, including `python_repl.py`, compiler, permissions, secure methods and execution guards | Included | State initialization, Python execution, native return/raise handling and safety-control implementations. Inspected imports/control seams and sync/async execution methods. | No sandbox security certification; supporting guard implementations have not all been inspected at boundary declaration. |
| `src/`: `jaz/hooks/`, especially `base.py`, `dispatcher.py`, `context.py`, `effects.py`, `events/`, `blackboard.py`, `builtin/` | Included | Hook-based admission, modification, termination, accounting and observation. Read initial hook contract; inspected trajectory writer, saved-response consumer and workflow materialization; searched recorder/rollout/directory handlers. Includes budget, iteration, recursion and return hooks, loggers and tracing integrations. | Individual policies and concurrency behavior require later tracing. No remote tracing service behavior is established. |
| `src/`: `jaz/llm/`, `jaz/_llm_client.py`, `jaz/llm_client.py`, `jaz/budget.py`, `jaz/tokens.py` | Included | Model calls, retries, pricing/accounting and provider adaptation. Inspected default LiteLLM sync/async call and normalization methods; other shipped adapters remain included. | Other providers' wire behavior and live cost accuracy are not established by this initial inspection. |
| `src/`: `jaz/_library/`, `jaz/library.py`, catalog/display modules and their shims, inputs/descriptions/config/scope/provenance/parent-output/string and warning helpers | Included | Tool/data exposure, input binding, configuration propagation, metadata and supporting implementation. Inspected invocation consumers and complete shipped SWE tool source; searched Library API. | No assertion that arbitrary supplied tools obey runtime restrictions. Supporting files remain available for detailed tracing. |
| `src/`: `jaz/utils/extract_git_diff.py`, `jaz/utils/log_to_markdown.py`, `jaz/utils/trace_to_directory.py` | Included | Shipped artifact post-processing. Located utility entry points and read ATIF-file ingestion and directory conversion. | These utilities do not provide a supplied evaluation result; detailed formatting and diff extraction were not audited. |

The retained-content paths are not excluded as mere logging. `TrajectoryRecorder` writes ATIF JSON, `TrajectoryReplay` loads saved responses and supplies them at query time, and `WorkflowReplay` emits standalone Python entry blocks. `trace_to_directory` is another shipped consumer of recorded ATIF files. SRC-1, `src/jaz/hooks/builtin/atif_trace.py`, `src/jaz/hooks/builtin/replay.py`, `src/jaz/hooks/builtin/workflow_replay.py`, `src/jaz/utils/trace_to_directory.py`.

> self.output_path.write_text(json.dumps(data, indent=self.indent))
> --- `src/jaz/hooks/builtin/atif_trace.py`

> return [
>     SupplyLLMResponse(
>         content=r.content,
>         prompt_tokens=r.prompt_tokens,
>         completion_tokens=completion_tokens,
>         cost_usd=r.cost,
>     )
> ]
> --- `src/jaz/hooks/builtin/replay.py`

### External dependencies and evidence limits

The package uses Python and dependencies declared in `pyproject.toml`, including Jinja2, HTTPX, Tenacity, beartype, typing-extensions, pathspec and LiteLLM. Optional integrations include OpenTelemetry, Transformers and the GitHub Copilot SDK. Only JAZ's integration code is frozen; dependency source, provider services, user credentials, tool backends and model weights are not registered evidence. This prevents claims about their internal enforcement, uptime or model performance. SRC-1, `pyproject.toml` and `src/jaz/llm/_litellm.py`.

This repository describes itself as a generated distribution:

> This repository is generated: each release publishes a cleaned copy of the package, so
> changes are not made here. Contributor setup and code conventions live with the source.
> --- `README.md`

The tracked tree contains no tests, evaluation harness, benchmark datasets, run traces or contributor-source tree. References in documentation/comments to an eval harness, examples, experiments or other source-tree consumers do not make those artifacts available at this pin. This prevents independent assessment of benchmark outcomes, optimization/training effectiveness and behaviors of unshipped applications. It does not exclude the console or shipped replay tools. Available package files not yet read are inspection work, not unavailable evidence. No other repository or moving web documentation is admitted.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/jaz-lang/JAZ` | 0803d4971be785e95b80054b02259664d70fa3da | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/jaz-a94bea79c61a/related-systems/jaz-lang--JAZ`. Implementation: tracked-tree inventory; complete `pyproject.toml`, `src/jaz/__init__.py`, `src/jaz/__main__.py`, `src/jaz/agent.py`, `src/jaz/_library/swe.py`; bounded ranges of `src/jaz/invoke.py`, `src/jaz/_agent.py`, `src/jaz/console.py`, `src/jaz/repl/python_repl.py`, `src/jaz/protocol/code_only.py`, `src/jaz/llm/_litellm.py`, `src/jaz/hooks/builtin/atif_trace.py`, `src/jaz/hooks/builtin/replay.py`, `src/jaz/hooks/builtin/workflow_replay.py`, `src/jaz/utils/trace_to_directory.py`; scoped symbol/persistence searches in settings, credentials, library, utilities and built-in recorders. Doctrine/design: complete `README.md`, `src/jaz/templates/system_prompt.jinja2`, opening sections of `src/jaz/hooks/README.md` and inline contracts in inspected implementation. | Implementation: [entry point](https://github.com/jaz-lang/JAZ/blob/0803d4971be785e95b80054b02259664d70fa3da/pyproject.toml), [loop](https://github.com/jaz-lang/JAZ/blob/0803d4971be785e95b80054b02259664d70fa3da/src/jaz/_agent.py), [console](https://github.com/jaz-lang/JAZ/blob/0803d4971be785e95b80054b02259664d70fa3da/src/jaz/console.py), [replay](https://github.com/jaz-lang/JAZ/blob/0803d4971be785e95b80054b02259664d70fa3da/src/jaz/hooks/builtin/replay.py). Doctrine/design: [README](https://github.com/jaz-lang/JAZ/blob/0803d4971be785e95b80054b02259664d70fa3da/README.md), [system prompt](https://github.com/jaz-lang/JAZ/blob/0803d4971be785e95b80054b02259664d70fa3da/src/jaz/templates/system_prompt.jinja2). | Implementation available for the full registered repository, not just listed paths. Unshipped contributor source/evaluators and external dependency/service internals unavailable; prevents conclusions about those systems and independent reproduction of reported performance. No observed-run or causal-experiment artifact supplied. |
