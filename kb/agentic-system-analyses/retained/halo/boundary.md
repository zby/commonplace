---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Halo's shipped trace-analysis and harness-improvement plane at commit b7f8509745d67b499b4e80efe20ea37c03426a74, including desktop persistence, engine callers and improvement instructions."
run-id: AAS-2026-10-14-halo-c4ed89d7f99f-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: complete artifact, partial loop
reviewed-boundary: b7f8509745d67b499b4e80efe20ea37c03426a74
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/context-labs/halo
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/halo-c4ed89d7f99f/related-systems/context-labs--halo
  revision: b7f8509745d67b499b4e80efe20ea37c03426a74
  sha256: null
---

# Halo boundary

## Boundary and evidence

This analysis covers Halo as shipped in the frozen repository, not just its Python library API. Its intended use is to diagnose agent-harness behavior from execution traces and support iterative harness improvement. The primary target class is **builder or improvement plane**: an enclosing trace-exploration runtime is one component of that plane, alongside desktop trace ingestion, retained analysis conversations, report handoff, demos and operating instructions. The engine qualifies independently because it issues model calls and equips agents with trace, synthesis, context, sandbox and optional code/Git tools (SRC-1, `engine/main.py`, `engine/tools/subagent_tool_factory.py`). The package declares its narrower runtime role explicitly:

> description = "HALO engine: LLM agent runtime over OTel trace data, with bundled CLI."
> --- `pyproject.toml`

The repository's broader intended loop includes a separate coding agent and subsequent redeployment (SRC-1, `README.md`):

> 3. The engine decomposes the traces to understand common failure modes across harness executions and produces a report with its findings.
> 4. This report is fed into a coding agent like Cursor or Claude Code to generate and apply a set of changes to your harness.
> 5. The harness is then re-deployed, more traces are gathered, and the cycle repeats.
> --- `README.md`

The boundary kind is **complete artifact, partial loop**. All tracked repository content at this commit is eligible evidence, including shipped callers and evaluators. The implemented desktop path reaches report retention and coding-tool handoff. Execution of the receiving coding agent, changes to an arbitrary user's harness, deployment and subsequent production collection are outside this source boundary. This is not a subsystem-only analysis of `engine/`. Nor does possession of the repository establish a self-contained, automatically closed improvement loop. The external portion prevents conclusions about autonomous implementation, deployment, or causal production improvement by Halo itself. The shipped handoff explicitly requires user confirmation (SRC-1, `app/src/desktop/commands.ts`):

> * None of them auto-run; the user confirms inside the tool.
> --- `app/src/desktop/commands.ts`

### Included functional paths

- **Trace production and admission:** the SDK demo's agent driver and JSONL tracing processor; the vendored AppWorld harness, prompts and tracing integration; desktop OTLP, file, Langfuse and Phoenix import paths. The import queues' calls into the common telemetry store were located by source search. The common store's transactional span upsert and trace-summary refresh were inspected. Import-specific mapping behavior remains for later inspection, not an access gap (SRC-1, `demo/openai-agents-sdk-demo/main.py`, `demo/openai-agents-sdk-demo/tracing.py`, `demo/appworld/experiments/code/openai_agents/run.py`, `app/src/server/fileimport/importQueue.ts`, `app/src/server/langfuse/importQueue.ts`, `app/src/server/phoenix/importQueue.ts`, `app/src/server/telemetry/storage.ts`).
- **Analysis execution and context maintenance:** packaged CLI, sync/async engine entry points, per-file index resolution, root run construction, model-driven tools, runtime prompt templates, original-item lookup and compaction. These are source-visible responsibilities, not observed runtime outcomes (SRC-1, `halo_cli/main.py`, `engine/main.py`, `engine/tools/subagent_tool_factory.py`, `engine/agents/prompt_templates.py`, `engine/agents/agent_context.py`, `engine/agents/compactor.py`).
- **Persistence and subsequent consumption:** the desktop is a shipped consumer, not an excluded host. Its queue exports selected stored traces, invokes the Python bridge, retains answers and turns, and reconstructs message history for follow-ups. Follow-ups can reuse the original export. Report generation reads retained turns and writes a Markdown artifact; the UI supplies its path to an external coding tool (SRC-1, `app/src/server/halo/exporter.ts`, `app/src/server/halo/runQueue.ts`, `app/scripts/halo-local-runner.py`, `app/src/server/halo/storage.ts`, `app/src/server/halo/report.ts`, `app/src/mainview/halo/OpenInToolBar.tsx`). The history consumer is explicit:

> return listHaloRunTurns(sqlite, run)
>     .filter(
>       (turn) =>
>         turn.turnIndex < upToTurnIndex &&
>         (turn.role === "user" || turn.content.trim().length > 0),
>     )
>     .map((turn) => ({ content: turn.content, role: turn.role }));
> --- `app/src/server/halo/storage.ts`

- **Improvement instructions and evaluation:** `skills/claude/SKILL.md` supplies the coding actor's baseline, diagnosis, verification, edit and remeasurement procedure. AppWorld task commands connect generated traces to the Halo CLI, and its evaluator loads task-output databases and invokes task-specific evaluation modules. Engine tests include live-provider checks; they were read as test definitions, not executed (SRC-1, `skills/claude/SKILL.md`, `demo/appworld/Taskfile.yml`, `demo/appworld/src/appworld/evaluator.py`, `tests/e2e/test_engine_e2e.py`). The skill contains older trace-only assumptions while the engine exposes optional repository tools at this pin. Both are included; the skill's claims are doctrine, not substitutes for implementation evidence (SRC-1, `skills/claude/SKILL.md`, `engine/tools/subagent_tool_factory.py`, `halo_cli/main.py`).

### Repository coverage

The following inventory accounts for every top-level tracked entry in SRC-1. “Included” means eligible within this functional boundary, not that every file has already been inspected. No top-level directory is excluded as an enclosing application. Material paths not yet inspected are identified separately from unavailable evidence.

| Top-level entry | Treatment and role | Initial inspection and limits |
| --- | --- | --- |
| `.githooks/` | Included: development checks | Tree inspected; hook bodies not yet inspected. No claim about their enforcement. |
| `.github/` | Included: engine/app release and test workflows | `workflows/` names inventoried; workflow bodies not yet inspected. No claim about successful CI or releases. |
| `.gitignore` | Included: repository configuration | Inventoried, not yet inspected. |
| `.infisical.json` | Included: environment configuration | Inventoried, not yet inspected; no credential or deployment claims. |
| `README.md` | Included: system intent, API guide and reported benchmark results | Read completely. Benchmark statements are reported operation, not a retained intervention comparison establishing causation. |
| `Taskfile.yml` | Included: root development commands | Inventoried, not yet inspected. |
| `app/` | Included: shipped desktop and server, trace admission, durable analysis state, follow-up consumption and report handoff | Inspected `scripts/halo-local-runner.py`, `src/server/halo/{engine,runQueue,storage,report,exporter}.ts`, `src/server/telemetry/storage.ts`, `src/mainview/halo/OpenInToolBar.tsx`, `src/desktop/commands.ts`; searched the file/Langfuse/Phoenix import queues and router. Remaining material includes `src/server/{app,start,db,telemetry,fileimport,langfuse,phoenix,live}/`, `src/bun/`, analysis and trace UI, and `tests/`. These remain available for later inspection. |
| `assets/` | Included: source-native diagrams, screenshots and benchmark presentation | Filenames inventoried; images not inspected. They supply no independently checked result here. |
| `demo/` | Included: callers, trace producers, prompts, configs and evaluation examples | SDK `main.py` read; `tracing.py` searched. AppWorld `HALO_PATCH.md`, `Taskfile.yml`, `experiments/code/openai_agents/run.py`, `experiments/code/hal/main.py` and `src/appworld/evaluator.py` inspected in relevant ranges. Remaining material includes SDK `agent.py`, `verify_traces.py`, sample traces, AppWorld `experiments/{code,configs,prompts}/`, environment/CLI/task code and bundled data. Bundle internals and task-specific evaluation modules were not inspected; no claim about their completeness or benchmark reproducibility. |
| `docs/` | Included: tracing integration contract | `integrations/openai-agents-sdk.md` inventoried, not yet inspected. |
| `engine/` | Included: trace indexing/store, model-driven analysis, context maintenance, delegation, tools, sandbox, code/Git inspection and telemetry | `main.py` read completely; relevant ranges of `agents/{prompt_templates,agent_context,compactor}.py` and `tools/subagent_tool_factory.py` inspected. Remaining `traces/`, `code/`, `git/`, `sandbox/`, `telemetry/`, tool implementations and runner/configuration code remain available; their detailed guarantees are not established by this boundary. |
| `halo-telemetry-run-legacy.jsonl` | Included: possible source-native run artifact | Inventoried, not inspected. No observed-run conclusions from it. |
| `halo_cli/` | Included: packaged executable consumer | `main.py` read completely; CLI registration traced from `pyproject.toml` to `stream_engine_async`. |
| `pyproject.toml` | Included: package identity, dependencies and entry point | Read completely; engine and CLI are wheel packages. |
| `pyrightconfig.json` | Included: development configuration | Inventoried, not yet inspected. |
| `scripts/` | Included: version checks and development hooks | `validate_pinned_versions.py`, `setup-git-hooks.sh`, `git-hooks/` inventoried, not yet inspected. |
| `skills/` | Included: coding actor's improvement procedure | `claude/SKILL.md` inspected through baseline capture, diagnosis, claim verification, edit and remeasurement instructions. Later tool inventory remains available. |
| `tests/` | Included: evaluators of engine behavior and fixtures | `e2e/test_engine_e2e.py` first live-model smoke test inspected; `unit/`, `integration/`, `probes/` and `fixtures/` inventoried. Definitions and fixtures are not proof of passing runs. |
| `uv.lock` | Included: frozen dependency resolution metadata | Inventoried, not yet inspected. External dependency implementations are not frozen by this file. |

### Frozen evidence and external limits

The sole evidence source is `https://github.com/context-labs/halo` at full commit `b7f8509745d67b499b4e80efe20ea37c03426a74`. The acquired checkout's HEAD matches that pin and its working tree was clean when inspected. The analysis cutoff is **2026-10-14**, the supplied run date; it does not establish behavior of later releases, installed desktop engines or mutable hosted products. The overall evidence tier is **code-grounded**. Documentation and the skill provide declared intent; README benchmark claims provide attributed reported operation. No target code, examples, tests or providers were executed, and no observed-run or causal-experiment layer is claimed from the initial inspection.

External dependencies include the OpenAI-compatible model service and OpenAI Agents SDK, Deno/Pyodide sandbox components, Git/ripgrep, the desktop's Bun-based application stack, trace-provider services and receiving coding-agent applications (SRC-1, `pyproject.toml`, `engine/main.py`, `engine/agents/compactor.py`, `app/src/server/halo/engine.ts`, `app/scripts/halo-local-runner.py`, `app/src/desktop/commands.ts`). Their implementations and live service behavior are not captured. This prevents conclusions about provider reliability, sandbox security beyond the shipped implementation, remote import-service behavior, and coding-tool execution. Visible demo code is included as vendored content at the Halo commit, not registered as a separately inspected upstream repository. Linked hosted documentation, release downloads, arbitrary user harnesses and upstream repositories are not frozen sources; no evidence is imported from them.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/context-labs/halo` | b7f8509745d67b499b4e80efe20ea37c03426a74 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/halo-c4ed89d7f99f/related-systems/context-labs--halo`. Implementation: `pyproject.toml`, `halo_cli/main.py`, `engine/main.py`, relevant context/compaction and tool-factory ranges; desktop export, bridge, queue, history, report and handoff paths listed above; common ingestion transaction; demo driver, AppWorld tracing and evaluator ranges. Doctrine/design: complete root README, runtime prompt ranges, improvement-skill procedure and AppWorld patch documentation. Reported operation: root README benchmark account. Import queues, tracing processor and router were searched for callers; this does not establish all their behavior. | Implementation: [entry and lifecycle](https://github.com/context-labs/halo/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/engine/main.py), [desktop retained-state consumer](https://github.com/context-labs/halo/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/app/src/server/halo/runQueue.ts), [history reload](https://github.com/context-labs/halo/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/app/src/server/halo/storage.ts), [handoff](https://github.com/context-labs/halo/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/app/src/desktop/commands.ts). Doctrine/design: [runtime prompts](https://github.com/context-labs/halo/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/engine/agents/prompt_templates.py), [improvement procedure](https://github.com/context-labs/halo/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/skills/claude/SKILL.md). Reported operation: [README benchmarks](https://github.com/context-labs/halo/blob/b7f8509745d67b499b4e80efe20ea37c03426a74/README.md). | No checkout access gap established. Uninspected files remain available at this pin, not excluded or inaccessible. External coding executors, deployments, hosted services and dependency implementations are outside the frozen evidence; their behavior and loop closure cannot be attributed to Halo. Initial inspection supplies no observed execution or causal benchmark comparison. |
