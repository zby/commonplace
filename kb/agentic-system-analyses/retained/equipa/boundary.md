---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "EQUIPA's shipped orchestration, retained context and improvement paths at Git revision fa8f41a6948584ee53e804edbb08b7449d05cd14."
run-id: AAS-2026-10-15-equipa-32016e8dd9ae-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: fa8f41a6948584ee53e804edbb08b7449d05cd14
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/sbknana/equipa
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-equipa/related-systems/sbknana--equipa
  revision: fa8f41a6948584ee53e804edbb08b7449d05cd14
  sha256: null
---

# EQUIPA boundary

## Boundary and evidence

This run examines EQUIPA as a shipped agent orchestration system, including its retained context and its separate improvement programs. The intended use is to explain its design and operating responsibilities, not to establish production effectiveness. The source is the acquired checkout at the full commit above. HEAD matches that commit and the checkout reports no working-tree changes. The analysis cutoff is 2026-10-15; later revisions, live deployments and linked external pages supply no evidence.

The target class is **enclosing runtime**: EQUIPA selects and dispatches agents, controls task iteration, admits results through review and merge paths, and records outcomes for later consumption. Claude Code supplies an inner agent execution engine; its internals are not EQUIPA's own implementation. EQUIPA also ships an Ollama tool-calling loop. This is not merely an MCP adapter or a lesson-retrieval API. The boundary is **whole-system**, including package entry points, root-level drivers, interactive session skills, prompts, standing orders, maintenance, evaluation and improvement tooling. These same-repository consumers are not treated as external hosts. Evidence: SRC-1, `equipa/cli.py`, `equipa/agent_runner.py`, `ollama_agent.py`, `forgesmith.py`, `.claude/skills/forge-end/SKILL.md`.

The entry-point trace starts at `forge_orchestrator.py` and `equipa/__main__.py`, which import the package CLI. Its mode registry includes single and parallel tasks, goals, automatic dispatch, initiatives, configuration and MCP serving. The MCP dispatch handler launches `python -m equipa.cli`; the arena driver launches the root orchestrator. Goal planning/evaluation surrounds task execution in `equipa/manager.py`; initiative waves reuse parallel task dispatch in `equipa/initiative_runner.py`. These are included shipped drivers, not excluded enclosing applications. Evidence: SRC-1, `forge_orchestrator.py`, `equipa/__main__.py`, `equipa/cli.py`, `equipa/mcp_server.py`, `equipa/manager.py`, `equipa/initiative_runner.py`, `tools/forge_arena.py`.

> cmd = [sys.executable, "-m", "equipa.cli", "--task", str(task_id), "--role", role, "--yes"]
> --- `equipa/mcp_server.py`

The inspected operating path covers production, admission and later consumption of state. Task dispatch creates worktrees and routes execution toward security review and gated merge. The dev-test loop restores session/checkpoint context and constructs developer and tester calls. Post-task telemetry records status and runs, invokes scoring and reflection, and updates the values of injected episodes. Episode recording sanitizes agent-authored reflection before SQLite insertion; prompt construction retrieves lessons and episodes and tracks which were shown. Project-context loading also reads session notes, questions and decisions. Interactive session-end instructions write those same categories. Evidence: SRC-1, `equipa/dispatch.py`, `equipa/loops.py`, `equipa/cli.py`, `equipa/lessons.py`, `equipa/prompts.py`, `equipa/sessions.py`, `equipa/tasks.py`, `.claude/skills/forge-end/SKILL.md`.

> update_task_status(task["id"], outcome, output=output, merged_sha=merged_sha)
> record_agent_run(task, result, outcome, role=role, model=model,
>                  max_turns=max_turns, cycle_number=cycle_number)
> --- `equipa/cli.py`

> static_prefix = common_text + "\n\n---\n\n" + role_text + standing_orders
> --- `equipa/prompts.py:508-508`

The improvement plane is inside the boundary. `forgesmith.py` collects/analyzes runs, evaluates previous changes, extracts lessons, calls SIMBA, scores runs, applies changes, and conditionally invokes OPRO and GEPA; it also calls the LITM audit. Prompt construction imports GEPA's A/B prompt selector. Benchmarking and sweep programs are included as consumers of task execution and its recorded results. Their presence and source logic do not establish that a scheduled job ran or that a proposed prompt improved results. Evidence: SRC-1, `forgesmith.py`, `equipa/prompts.py`, `forgesmith_gepa.py`, `forgesmith_litm.py`, `scripts/forgesmith_simba.py`, `scripts/autoresearch_loop.py`, `scripts/equipa_harness_sweep.py`, `tools/forge_arena.py`.

> findings, runs, blocked = run_analysis(cfg)
> --- `forgesmith.py:3209-3209`

### Tracked top-level coverage

Every top-level tracked entry is classified below. Included means eligible within this system boundary, not that every file has been read or its behavior verified. Initial inspection traced the paths described above and the named source ranges; tree/function/search inspection established the remaining layout. Detailed internals not yet inspected remain available at the same frozen commit. No material shipped path was inaccessible. All rows refer to SRC-1.

| Top-level entry | Classification and material paths or role | Initial inspection and limits |
|---|---|---|
| `equipa/` | Included: `__main__.py`, `cli.py`, `dispatch.py`, `loops.py`, `agent_runner.py`, `agent_launcher.py`, `manager.py`, `initiative_runner.py` form the execution/control paths; `prompts.py`, `lessons.py`, `sessions.py`, `tasks.py`, `checkpoints.py`, `reflexion.py`, `embeddings.py`, `graph.py`, `db.py` produce and consume retained state; `mcp_server.py`, `hooks/`, isolation, merge, routing, security and configuration modules support admission and dispatch. | Entry-point bodies, dispatch/provider selection, loop entry, isolated task execution, prompt assembly, episode insertion, session save/reload, project-context reads and telemetry inspected; remaining modules mapped by tree/search, not comprehensively audited. |
| `forge_orchestrator.py` | Included: legacy CLI entry and re-exports. | Complete file inspected; delegates to package CLI. |
| `ollama_agent.py` | Included: local-model agent/tool loop. | Entry and tool/function map inspected; provider is reached from package dispatch. |
| `forgesmith.py` | Included: maintenance, scoring, lesson extraction, prompt/config changes and rollback orchestration. | Function map and `run_full` inspected. |
| `forgesmith_gepa.py` | Included: prompt evolution, validation, storage, A/B selection and rollback. | Function map plus caller and prompt-selector consumer inspected; optimizer internals not yet read in detail. |
| `forgesmith_litm.py` | Included: positional-weight audit and configuration updates. | Function map and ForgeSmith caller inspected. |
| `lesson_sanitizer.py` | Included: admission/sanitization helpers for retained content. | Function map and consumers in episode recording and session-end instructions inspected; detailed rejection rules remain for later analysis. |
| `rubric_quality_scorer.py` | Included: output-quality scoring and score persistence. | Function map and `loops.py` scoring caller inspected. |
| `db_migrate.py` | Included: schema upgrades, versioning and backups. | Migration/entry-point function map inspected. |
| `equipa_setup.py` | Included: bootstrap, database/config generation, AI-tool integration and ForgeSmith scheduling. | Main sequence and function map inspected. |
| `schema.sql` | Included: tasks, decisions, session notes, runs, lessons, episodes, improvement history, graph, flows, configuration versions and sessions. | Table declarations searched; schema details not yet exhaustively read. |
| `schema_personal.sql` | Included: optional personal/project-adjacent tables shipped with setup. | Table inventory inspected; not evidence of deployed personal data or actual use. |
| `prompts/` | Included: `_common.md`, role prompts, paralysis retry templates and `languages/` guidance. | Common rules excerpt and assembly/loading consumers inspected; other prompt bodies remain available, not yet fully inspected. |
| `standing_orders/` | Included: role-specific operating authority, approval and escalation instructions. | Developer file and assembly consumer inspected; other roles not yet individually read. |
| `skills/` | Included: developer, tester, debugger, code-reviewer and security plugin instructions, reference files and bundled helpers. | Tracked inventory and integrity-scanning consumer searched; individual skill bodies not yet inspected. These are shipped prompt material, not external operational evidence. |
| `.claude/` | Included: `skills/forge-start`, `forge-end`, `forge-context`, `forge-search`, `forge-update`, `forge-orchestrate`, `housekeeping`. | `forge-end/SKILL.md` inspected for writes and sanitization instructions; other session/maintenance procedures inventoried, not yet read. |
| `hooks/` | Included: `post_agent_lint.py`, `preflight_build.py`, `pretooluse_bash_gate.py`. | Inventory and runner's hook-related function map inspected; bodies not yet inspected. |
| `scripts/` | Included: `autoresearch_loop.py`, `autoresearch_prompts.py`, `forgesmith_simba.py`, `equipa_harness_sweep.py`, `nightly_review.py`, performance/impact/backfill tools, migrations, deployment, synchronization and verification/probe programs. | Function maps for improvement/review drivers, sweep search and full inventory inspected. Probe outputs have not been executed or observed. Deployment/sync programs remain shipped integration logic, not evidence about remote hosts. |
| `tools/` | Included: `forge_arena.py`, `forge_dashboard.py`, `benchmark_migrations.py`, `prepare_training_data.py`, `ingest_training_results.py`. | Function maps and arena dispatch body inspected; training exports/imports and dashboards are included downstream state consumers, with detailed internals not yet read. |
| `tests/` | Included: runtime, isolation, merge/review, prompt, memory, session, improvement and integration tests; fixtures and timing/probe helpers. | Full tracked inventory and cross-attempt-memory test excerpt inspected. Tests are source contracts, not passing-run evidence. |
| `examples/` | Included: `roles/README.md` and custom role examples. | Inventory only; illustrates extension surface, not executed behavior. |
| `docs/` | Included: architecture, API, coordinator/orchestrator, deployment, isolation, concurrency, training, tool-result storage, initiatives and user guidance. | Inventory only in this initial pass; no claim relies on uninspected document prose. |
| `README.md` | Included: target's declared purpose, entry points, architecture and limitations. | Complete file inspected as doctrine/design and attributed reported operation, not independently verified results. |
| `CHANGELOG.md`, `CONTRIBUTING.md` | Included: target-authored history and contributor guidance. | Inventory only; no historical or operational claim derived from their unread bodies. |
| `dispatch_config.example.json`, `forge_config.example.json`, `forgesmith_config.example.json`, `goals.example.json` | Included: shipped configuration/goal templates. | Inventory and configuration-loading consumer located; example settings not assumed to be deployment settings. |
| `mcp_config.example.json`, `hooks.json.example`, `.env.example` | Included: tool, lifecycle and environment integration templates. | Inventory only; real endpoints, credentials and local configuration are absent from this evidence set. |
| `skill_manifest.json` | Included: pinned prompt/skill integrity metadata. | Manifest generation/verification consumer searched; no full independent hash audit performed. |
| `pytest.ini`, `requirements-dev.txt` | Included: evaluator configuration/dependencies. | Inventory only; no tests run or dependencies installed. |
| `.github/` | Included: `workflows/tests.yml`, `docs-drift-check.yml`, `plugin-boundary-check.yml`. | Inventory only; workflow definitions are not CI execution results. |
| `.githooks/` | Included: `pre-commit`. | Inventory only; installation or enforcement not established. |
| `.deploy-allowlist` | Included: deployment packaging policy. | Inventory only; deployed installation contents not established. |
| `.gitattributes`, `.gitignore` | Included: checkout and untracked-file policy. | Inventory only; not evidence of ignored runtime state. |
| `LICENSE` | Excluded from functional analysis: licensing text. | Inventory only; prevents any conclusion about legal suitability, not about the operating loop. |

### External dependencies and evidence limits

The overall tier is **code-grounded**. Only source text was inspected; no target, tests, examples, services or model calls were executed. Target-authored claims of production use and improvement in SRC-1, `README.md`, remain reported operation. There is no supplied run trace or causal experiment, so this boundary cannot establish reliability, security isolation in deployment, realized cost, retrieval quality or prompt-improvement effects.

External dependencies include Claude Code and model services, Ollama model/embedding services, Python/SQLite, Git, configured MCP servers, project repositories and their build/test systems, and optional optimizer dependencies. Their implementation and deployed state are excluded: this prevents attributing their internal scheduling, inference, sandboxing, persistence or test validity to EQUIPA. EQUIPA's own launch, configuration, guard and result-handling logic stays included. Evidence: SRC-1, `README.md`, `equipa/agent_runner.py`, `ollama_agent.py`, `equipa/loops.py`, `equipa_setup.py`.

Operator databases, credentials, ignored local configuration, project worktrees, checkpoint/session files and remote deployment hosts are not supplied frozen evidence. Their absence prevents claims about actual tasks, stored memories, enabled features, installed plugins, live scheduling and success rates. This does not exclude shipped producers, maintainers or consumers of that state. Available but uninspected source files above are not access gaps; later jobs may inspect them at this same registered commit.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/sbknana/equipa` | fa8f41a6948584ee53e804edbb08b7449d05cd14 | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-equipa/related-systems/sbknana--equipa`. Implementation: tracked tree, entry-point and consumer traces, loop/session/prompt/episode/telemetry paths, improvement driver and evaluator inventory as specified above. Doctrine/design: complete README, common prompt excerpt, developer standing orders, session-end instructions and selected test source. Reported operation: README's production and improvement claims only. | Implementation: [CLI](https://github.com/sbknana/equipa/blob/fa8f41a6948584ee53e804edbb08b7449d05cd14/equipa/cli.py), [dispatch](https://github.com/sbknana/equipa/blob/fa8f41a6948584ee53e804edbb08b7449d05cd14/equipa/dispatch.py), [prompts](https://github.com/sbknana/equipa/blob/fa8f41a6948584ee53e804edbb08b7449d05cd14/equipa/prompts.py), [lessons](https://github.com/sbknana/equipa/blob/fa8f41a6948584ee53e804edbb08b7449d05cd14/equipa/lessons.py), [sessions](https://github.com/sbknana/equipa/blob/fa8f41a6948584ee53e804edbb08b7449d05cd14/equipa/sessions.py), [ForgeSmith](https://github.com/sbknana/equipa/blob/fa8f41a6948584ee53e804edbb08b7449d05cd14/forgesmith.py). Doctrine/design and reported operation: [README](https://github.com/sbknana/equipa/blob/fa8f41a6948584ee53e804edbb08b7449d05cd14/README.md). Doctrine/design: [session-end skill](https://github.com/sbknana/equipa/blob/fa8f41a6948584ee53e804edbb08b7449d05cd14/.claude/skills/forge-end/SKILL.md), `prompts/_common.md`, `standing_orders/developer.md`, `tests/test_cross_attempt_memory.py`. | No inaccessible tracked source identified. External engines, live project/database/configuration state and independent execution records are not supplied; implementation supports source-level behavior only, doctrine supports stated instructions only, and reported operation cannot establish observed or causal results. |
