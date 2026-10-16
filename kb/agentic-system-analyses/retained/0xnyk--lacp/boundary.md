---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "LACP's shipped local agent operating layer, native agent loop and memory workflows at commit e31f134b689afd6a71d94b0420682d1f528d6fa1."
run-id: AAS-2026-10-14-lacp-91efd16f7a35-01
result-disposition: complete
target-class: agent operating layer
boundary-kind: whole-system
reviewed-boundary: e31f134b689afd6a71d94b0420682d1f528d6fa1
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/0xNyk/lacp
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/lacp-91efd16f7a35/related-systems/0xNyk--lacp
  revision: e31f134b689afd6a71d94b0420682d1f528d6fa1
  sha256: null
---

# LACP boundary

## Boundary and evidence

This run analyses LACP as shipped in the registered repository, not only its memory library or Claude plugin. The intended use is to establish how its agent execution controls, coordination, retained state, memory maintenance and later consumption fit together. The target is in scope because shipped paths both wrap model-dependent coding agents and implement a model/tool loop themselves (SRC-1, `bin/lacp`, `tui/repl.py`, `tui/providers.py`).

**Target class: agent operating layer.** Here this means a shipped local system that configures and coordinates agent operation, governs selected execution paths, and supplies context and retained state. It does not imply that every path is an external-runtime client. The class includes LACP's native REPL runtime alongside its host integrations, orchestration and improvement plane.

The documentation declares a narrower host relationship:

> LACP is a local execution wrapper and control plane. The coding-agent host still owns its
> model, tools, session, and interface. LACP owns the contract around a run: where it may
> execute, which risk tier applies, when approval is required, what evidence must be kept,
> and how a failed change is recovered.
> --- `README.md`

That is doctrine, not a sufficient description of every shipped entry point. The top-level dispatcher also launches a native REPL without an external coding-agent CLI (SRC-1):

> if [[ $# -lt 1 ]]; then
>   # No args: launch LACP native REPL
>   exec python3 "${ROOT}/tui/repl.py"
> fi
> --- `bin/lacp`

The REPL requests provider output with conversation state and tool definitions, dispatches returned calls, and supplies their results to another turn. Its Anthropic provider calls the model API (SRC-1, `tui/repl.py`, `tui/providers.py`):

> async for event in self.provider.stream(
>     messages=self.messages,
>     system=self.system_prompt,
>     tools=tools if isinstance(self.provider, AnthropicProvider) else None,
> ):
> --- `tui/repl.py`

> with client.messages.stream(**kwargs) as stream:
> --- `tui/providers.py`

> if tool_name.startswith("mcp_") and self.mcp_manager:
>     result = self.mcp_manager.call_tool(tool_name, tool_input)
> else:
>     result = execute_tool(tool_name, tool_input)
> --- `tui/repl.py`

> # Add tool results to conversation
> self.messages.append({"role": "user", "content": tool_results})
> --- `tui/repl.py`

**Boundary kind: whole-system.** All shipped functional paths at this commit are included: native REPL and dashboards; external CLI adoption and streaming; policy routing and execution; orchestration, harnesses and evidence gates; installation and configuration; learning-event capture, retrieval, evaluation, promotion and rollback; session hooks, handoffs and self-memory; ingestion, vault curation, indexing and retrieval; and automated improvement/evaluation. A shipped caller is not excluded because it supplies state or calls a helper. Alternative distribution paths, including the plugin's separate hook scripts, remain included rather than assumed equivalent (SRC-1, `bin/lacp`, `plugin/hooks/hooks.json`, `Formula/lacp.rb`, `CLAUDE.md`).

The initial state-loop trace reaches writers, maintenance drivers, reloaders and consumers. The native REPL's memory tools write/read keyed JSON entries; its session module saves and reloads conversations, and the REPL restores loaded messages. The stop hook records SMS episodes and updates its self-model; the session-start hook obtains SMS context. Brain expansion invokes synchronization, consolidation, curation, archival, indexing and health checks. A separate memory-pipeline driver invokes extraction, index building, promotion suggestions and retrieval benchmarking. These paths establish functional coverage, not that every store is mutually integrated or every documented learning phase is automatically invoked (SRC-1, `tui/tools.py`, `tui/sessions.py`, `tui/repl.py`, `hooks/stop_quality_gate.py`, `hooks/session_start.py`, `bin/lacp-brain-expand`, `automation/scripts/run_memory_pipeline.sh`).

Minimum retained evidence for the host-memory producer/consumer pair:

> write_episode(episode)
> _debug(f"SMS: episode recorded (significance={significance:.2f}, files={len(files_modified)})")
> --- `hooks/stop_quality_gate.py`

> from self_memory_system import build_session_context
> sms_context = build_session_context()
> if sms_context:
>     injections.append((7, "sms", f"Agent memory (SMS):\n{sms_context}"))
> --- `hooks/session_start.py`

The improvement plane is also shipped, not an external operator responsibility: the idle agent constructs an experiment prompt, invokes Claude/Codex/Hermes, compares a new health score to its baseline and keeps or discards the change. Evaluation code and stored score artifacts belong to the boundary; stored scores alone do not establish causal improvement (SRC-1, `tui/idle_agent.py`, `autoresearch/evaluate.py`, `autoresearch/evaluate_memory.py`).

### Top-level coverage

Each tracked top-level entry is classified below. “Included” fixes functional scope; it does not assert full-file inspection of every descendant. The inspected scope in the source register and the table distinguish initial tracing from material still to inspect. No material shipped path was inaccessible during boundary declaration.

| Top-level entry | Classification and material paths/role | Initial inspection and conclusion limit |
|---|---|---|
| `.claude-plugin/` | Included: `marketplace.json`, root plugin discovery metadata | Tree inventoried; metadata contents not yet inspected. No marketplace-install claim. |
| `.github/` | Excluded: funding, issue/PR templates and disabled CI/release workflows | Tree inventoried; exclusion prevents claims about hosted CI or GitHub release automation. Local evaluators remain included. |
| `.gitignore` | Excluded: tracking rules | Tree inventoried; no assessment of completeness of ignored operator state. |
| `AGENTS.md` | Included: shipped repository-agent instructions | Read as source doctrine, not worker instructions. |
| `CHANGELOG.md` | Included: attributed release history | Inventoried, not yet inspected; no historical implementation conclusion. |
| `CLAUDE.md` | Included: host instructions, context modes, memory access/lifecycle descriptions and maintenance guidance | Read; declarations must be checked against executable consumers. |
| `CODE_OF_CONDUCT.md` | Excluded: community governance | No community-governance assessment. |
| `CONTRIBUTING.md` | Excluded: contributor process | No assessment of contributor compliance; shipped tests and runtime instructions remain included. |
| `Formula/` | Included: `lacp.rb`, installation of CLI commands | Read; distribution path is in scope, installation success not observed. |
| `Heartbeat.md` | Included: operational memory/status and update guidance | Read as reported operation and doctrine; claimed deployment coverage not independently verified. |
| `LICENSE` | Excluded: legal license text | No legal interpretation. |
| `Memory/` | Included: `README.md`, `glossary.md`, `people/README.md`, `projects/README.md`, `context/README.md` | Root scaffold instructions read; remaining scaffold text inventoried, not yet inspected. No actual operator-memory corpus supplied. |
| `README.md` | Included: intended use, entry points, system architecture and external dependencies | Read completely; code takes precedence for shipped behavior. |
| `SECURITY.md` | Excluded: vulnerability-disclosure document | No assessment of disclosure process; executable safety controls remain included. |
| `SUPPORT.md` | Excluded: support arrangements | No support-service assessment. |
| `TODO.md` | Included: proposed work, distinguishable from shipped behavior | Inventoried, not yet inspected; proposals cannot establish implementation. |
| `automation/` | Included: `scripts/` ingestion/session extraction, synchronization, RAG building/querying, consolidation, curation, pruning, promotion suggestions, benchmarks and scheduled maintenance | Driver `run_memory_pipeline.sh` and `DIRECTIVE.md` read; bounded searches traced `run_shared_memory.sh`, `run_weekly_maintenance.sh`, `extract_shared_memory.py`, `query_memory_rag.py`, `memory_consolidation.py`, `benchmark_memory_retrieval.py`. Helpers remain available for deeper analysis. |
| `autoresearch/` | Included: `evaluate.py`, `evaluate_memory.py`, `optimize.py`, `program.md`, stored evaluation/results files | Evaluator/optimizer function and dependency searches; program and stored results not yet inspected. No experiment performed or stored score accepted as causal evidence. |
| `bin/` | Included: dispatcher and all CLI commands, notably stream/adoption, route/sandbox, harness/workflow/swarm, brain/curation, learning lifecycle, health/canary/rollback, installation and release controls | Dispatcher dispatch routes searched and native entry read; `lacp-workflow-run` read completely; routing/adoption, brain expansion/stack, learning commands and sandbox dispatch initially traced. Other command bodies remain available, not access gaps. |
| `config/` | Included: policy/contract schemas, context-mode prompts, profiles/teams, MCP/credential configuration, memory and learning policy, Obsidian settings, cron and autoresearch program | Tree inventoried and callers traced; configuration contents need later claim-specific inspection. No default-policy equivalence inferred. |
| `docs/` | Included: framework/runbooks, memory-quality procedures, runtime isolation, learning gates/plans, research/design documents and illustrations | `framework-scope.md` read; learning-plan/gate references searched. Remaining docs are available but not yet inspected. Plans and source-authored audits are attributed evidence, not verified conclusions. |
| `hooks/` | Included: session start/orientation, stop/eval/guard hooks, extraction, SMS, contracts, telemetry and hook test | Session-start SMS consumption and stop-hook episode production read; function searches traced associated contracts/handoff/evaluation. Other hook paths remain in scope for later inspection. |
| `install.sh` | Included: bootstrap acquisition/install entry point | Bounded entry-point search; body not fully inspected. No installation or dependency-resolution guarantee. |
| `plugin/` | Included: plugin discovery, `hooks/hooks.json`, separate `hooks/scripts/` copies, context-mode prompts, quality-gate/session-hardening skills and command | Hook event mapping and session-hardening skill read. Separate script copies and remaining prompts not yet inspected; behavior parity is not established. |
| `scripts/` | Included: `lacp-lib.sh`, `runners/` host/remote/result adapters, brain helpers, `ci/` tests, demo driver, `tui/` dashboard implementation | Tree and host runner calls traced; learning lifecycle test references searched. Shared library, remaining runners/test bodies/dashboard require later claim-specific reads. No tests executed. |
| `tui/` | Included: `repl.py`, `providers.py`, `tools.py`, `sessions.py`, `mcp.py`, `idle_agent.py`, `autoresearch_metrics.py`, dashboard, panels, display and skins | Native model/tool loop, conversation restore, memory tool store and provider request read; sessions module read completely; idle experiment driver read. Other UI/MCP/evaluator details remain available. |
| `version` | Included: shipped version marker | Inventoried, not yet read; commit, not marketing version, identifies evidence. |

### Frozen revision, dependencies and limits

SRC-1 is frozen at `e31f134b689afd6a71d94b0420682d1f528d6fa1`; checkout HEAD was checked against the acquired revision. The applicability cutoff is **2026-10-14**, the supplied run date. Evidence is code-grounded through static source inspection. No target command, tests, examples, providers or services were executed. This boundary supports implementation and intent findings, not verified installation, performance, real task outcomes or causal effects.

External host implementations (Claude, Codex, Hermes and other supported CLIs), model services/SDKs and authentication systems, Obsidian and its CLI, external MCP servers/indexers such as QMD, GitNexus and smart-connections, terminal/session tools, and remote sandbox services are dependencies, not independently frozen sources. LACP's adapters, configuration and prompts for them are included; their internal behavior, availability, security and cross-version compatibility are not established. In particular, external-host tool/session ownership must not be attributed to LACP's wrapper; the native REPL's own responsibilities must not be attributed to an excluded host (SRC-1, `README.md`, `CLAUDE.md`, `tui/providers.py`, `bin/lacp-stream`, `bin/lacp-brain-stack`, `bin/lacp-sandbox-run`).

Private installed settings, vault contents, session histories, credentials, live indexes and deployed schedules were not supplied. Their absence prevents conclusions about actual retained knowledge, operational coverage, retrieval quality and scheduling reliability. It is not an access gap in the registered repository. Repository-authored status and evaluation artifacts may support attributed reported operation only within their own stated conditions.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/0xNyk/lacp` | e31f134b689afd6a71d94b0420682d1f528d6fa1 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/lacp-91efd16f7a35/related-systems/0xNyk--lacp`. Tracked tree inventoried. Implementation: initial dispatcher/native REPL/provider/tool/session trace; wrapper routing and sandbox dispatch; workflow state transitions; hook SMS producer/consumer; brain expansion and memory-pipeline drivers; bounded extraction/retrieval/consolidation/benchmark, learning lifecycle and evaluator searches; idle experiment driver; plugin hook mapping and Homebrew formula. Doctrine/design: complete `README.md`, `CLAUDE.md`, `AGENTS.md`, `docs/framework-scope.md`, `Memory/README.md`, `automation/scripts/DIRECTIVE.md`, `plugin/skills/session-hardening/SKILL.md`. Reported operation: `Heartbeat.md`; not independently verified. Initial paths are not an allowlist. | Implementation: [dispatcher](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/bin/lacp), [native loop](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/tui/repl.py), [memory pipeline](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/automation/scripts/run_memory_pipeline.sh), [session hook](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/hooks/session_start.py). Doctrine/design: [framework scope](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/docs/framework-scope.md), [host instructions](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/CLAUDE.md). Reported operation: [status](https://github.com/0xNyk/lacp/blob/e31f134b689afd6a71d94b0420682d1f528d6fa1/Heartbeat.md). Other local anchors above resolve at this same commit. | No repository access gap encountered. Static inspection supplies no observed run or causal experiment. External dependency internals and private deployment state are outside the frozen evidence; prevents claims of end-to-end reliability, real retrieval performance, deployment coverage or causal improvement. |
