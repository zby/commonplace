---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Basic Memory's shipped knowledge engine and host packages at commit a72751c5d626380dedeed30f55f7a80ba3dc710d, with partial initial loop inspection."
run-id: AAS-2026-10-16-basic-memory-46fe4c6cfdc3-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: a72751c5d626380dedeed30f55f7a80ba3dc710d
analysis-cutoff: "2026-10-16"
evidence-tier: code-grounded
source:
  identity: https://github.com/basicmachines-co/basic-memory
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-basic-memory/related-systems/basicmachines-co--basic-memory
  revision: a72751c5d626380dedeed30f55f7a80ba3dc710d
  sha256: null
---

# Basic Memory boundary

## Boundary and evidence

Basic Memory qualifies as a memory/knowledge/context-engineering system serving model-driven callers. Its intended use is persistent knowledge shared between users and AI assistants, rather than ownership of an enclosing general-purpose agent runtime. This classification rests on its declared Markdown knowledge interface and inspected MCP and host-extension entry points, not the README's promotional claims of never forgetting (SRC-1, `README.md`, `src/basic_memory/mcp/server.py`, `integrations/pi/extensions/index.ts`).

> Your knowledge
> lives as Markdown files that both you and your AI can read, write, and
> search.
> --- `README.md`

The frozen artifact is the canonical repository at full commit `a72751c5d626380dedeed30f55f7a80ba3dc710d`. The acquired checkout's HEAD was checked against that pin without modifying it. The applicability cutoff is 2026-10-16, the supplied run date, not a claim about production deployment or the commit's authorship date. No additional repository, live documentation, external model service, or execution trace is registered.

### Functional boundary and entry-point trace

The functional target includes the Python knowledge engine, its CLI/API/MCP surfaces, retained-content handling, shipped model-facing instructions and skills, first-party host integrations and plugins, and repository evaluators. It is not narrowed to the MCP library API. Host-native callers that persist and reintroduce retained content belong to this artifact even though they run inside another product (SRC-1, `pyproject.toml`, `README.md`, `integrations/pi/package.json`, `integrations/pi/extensions/index.ts`).

The inspected entry-point trace is:

1. `basic-memory` and `bm` resolve to the same CLI application. Its main module registers the MCP, hook, tool, import, project and maintenance command modules (SRC-1, `pyproject.toml`, `src/basic_memory/cli/main.py`).
2. The `mcp` command imports tools, prompts and resources and invokes the FastMCP server. The server lifespan initializes the application, starts the watch coordinator and drains pending materializations and background tasks at shutdown. This establishes maintenance and persistence responsibilities inside the target; it does not yet establish every storage invariant (SRC-1, `src/basic_memory/cli/commands/mcp.py`, `src/basic_memory/mcp/server.py`).
3. The inspected `write_note` tool constructs an entity and delegates to the project-scoped `KnowledgeClient.write_note`. `build_context` delegates to `MemoryClient.build_context` and formats or serializes the returned graph for callers. The trace reaches these API-client boundaries, not a complete inspection of the receiving API, database transactions or materialization workers (SRC-1, `src/basic_memory/mcp/tools/write_note.py`, `src/basic_memory/mcp/tools/build_context.py`).
4. The Pi package declares its extension entry point. That extension captures session turns through CLI `tool write-note`, searches earlier `pi_session` notes for recall, and can use `hook session-start` and `hook pre-compact`. Its `before_agent_start` handler returns recalled content as a message. This is an inspected shipped consumer of retained content, not an imagined external caller (SRC-1, `integrations/pi/package.json`, `integrations/pi/extensions/index.ts`).

> [project.scripts]
> basic-memory = "basic_memory.cli.main:app"
> bm = "basic_memory.cli.main:app"
> --- `pyproject.toml`

> const content = cfg.useHookFlow
>         ? await runHook(cfg, ctx, "session-start", "startup", ctx.signal)
>         : hasProjectMapping()
>           ? await buildRecall(cfg, event.prompt, ctx.signal)
>           : SETUP_GUIDANCE;
>       if (!content) return;
>       return { message: { customType: ENTRY_TYPE, content, display: true } };
> --- `integrations/pi/extensions/index.ts`

Model-facing maintenance instructions are also part of the system, not merely development documentation. The inspected lifecycle skill instructs agents to archive notes and update their frontmatter. This supports an account of prescribed maintenance, not evidence that users or agents follow it (SRC-1, `skills/memory-lifecycle/SKILL.md`).

> Manage how entities move through status stages in Basic Memory. The core principle: **archive, never delete.** Completed work is valuable context — move it out of the active view, but keep it in the knowledge graph.
> --- `skills/memory-lifecycle/SKILL.md`

### Coverage status and prevented conclusions

The boundary kind is **complete artifact, partial loop**. The whole pinned repository is available as evidence, but this initial inspection does not demonstrate whole-system loop coverage. The following are inspection limits, not access failures or a prohibition on later analysts inspecting additional files at the same pin.

| Surface | Initial coverage | Limit and conclusion prevented |
|---|---|---|
| CLI and packaging | Inspected `pyproject.toml`, `src/basic_memory/cli/main.py`, `src/basic_memory/cli/commands/mcp.py`. | Command registration and MCP startup traced; other command bodies not inspected, preventing claims of complete CLI behavior. |
| MCP and core knowledge path | Inspected `src/basic_memory/mcp/server.py`, `src/basic_memory/mcp/tools/write_note.py`, `src/basic_memory/mcp/tools/build_context.py`. | Write and context API-client boundaries inspected; receiving API, repository, index, cache, ingestion and worker implementations remain untraced, preventing end-to-end correctness or durability claims. |
| Shipped prompts and maintenance | Inspected server instructions in `src/basic_memory/mcp/server.py` and `skills/memory-lifecycle/SKILL.md`; distribution mappings in `pyproject.toml`. | Other skills, templates, prompts, manuals and schemas remain available but not inspected; no claim of complete admission or curation policy. |
| Pi caller | Inspected `integrations/pi/package.json` and `integrations/pi/extensions/index.ts`, including automatic recall/capture handlers and manual tools. | Helper implementations, Python hook bodies and host behavior remain untraced; no claim of complete capture fidelity, branch isolation or successful replay. |
| Other shipped host callers | README identifies `plugins/claude-code`, `integrations/hermes`, `integrations/openclaw`; packaging also ships Tau resources and the tree contains `plugins/codex`. | These are inside the functional target, but their implementations were not inspected. No attribution of Pi behavior to those packages and no complete cross-host loop claim. |
| Evaluators | Repository tree identifies `benchmarks/src/basic_memory_benchmarks`, `tests`, `test-int`, and package-local tests; pytest configuration inspected in `pyproject.toml`. | Evaluator implementations and results were not inspected. No benchmark quality, task-success, regression-pass or causal-effect conclusion. |
| Remaining repository material | Top-level tracked tree inspected for discovery; README read completely. | Build, CI, release, governance, development tooling and other documentation not comprehensively inspected. No repository-wide security, distribution or operational-completeness claim. |

All rows refer to SRC-1. An uninspected available path is not an access gap. Newly inspected paths at the registered commit may extend evidence coverage without adding a source identity.

### External dependencies and exclusions

Python dependencies, including FastMCP, FastAPI, SQLAlchemy, SQLite/vector tooling and optional backend/provider packages, are declared in `pyproject.toml` (SRC-1). Their separate implementations are outside this source set; this prevents assigning their internal guarantees to Basic Memory from declarations alone. Pi itself and its MCP adapter are external dependencies, while the Basic Memory Pi extension is included. The extension's imports and runtime registration establish that integration seam, not the host's scheduling or approval semantics (SRC-1, `integrations/pi/extensions/index.ts`).

The README describes a hosted cloud offering and external client/editor integrations. Live cloud infrastructure, authentication providers, other clients' implementation code, user knowledge bases, and actual production sessions are not captured. Consequently this run cannot verify hosted availability, team isolation, real-world recall quality, client compliance with instructions, or user outcomes (SRC-1, `README.md`). These exclusions do not remove cloud-routing code or first-party integration code present in the pinned artifact from the functional target.

The overall tier is **code-grounded**: implementation and declared design are both available, but no target code, tests or examples were executed. No observed-run or causal-experiment evidence is supplied.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/basicmachines-co/basic-memory` | a72751c5d626380dedeed30f55f7a80ba3dc710d | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-basic-memory/related-systems/basicmachines-co--basic-memory`. Implementation: `pyproject.toml`, `src/basic_memory/cli/main.py`, `src/basic_memory/cli/commands/mcp.py`, `src/basic_memory/mcp/server.py`, `src/basic_memory/mcp/tools/write_note.py`, `src/basic_memory/mcp/tools/build_context.py`, `integrations/pi/package.json`, `integrations/pi/extensions/index.ts`. Doctrine/design: `README.md`, server instructions in `src/basic_memory/mcp/server.py`, `skills/memory-lifecycle/SKILL.md`. Tracked tree inspected for discovery. | Implementation: [CLI registration](https://github.com/basicmachines-co/basic-memory/blob/a72751c5d626380dedeed30f55f7a80ba3dc710d/src/basic_memory/cli/main.py), [server lifecycle and instructions](https://github.com/basicmachines-co/basic-memory/blob/a72751c5d626380dedeed30f55f7a80ba3dc710d/src/basic_memory/mcp/server.py), [write tool](https://github.com/basicmachines-co/basic-memory/blob/a72751c5d626380dedeed30f55f7a80ba3dc710d/src/basic_memory/mcp/tools/write_note.py), [context tool](https://github.com/basicmachines-co/basic-memory/blob/a72751c5d626380dedeed30f55f7a80ba3dc710d/src/basic_memory/mcp/tools/build_context.py), [Pi consumer](https://github.com/basicmachines-co/basic-memory/blob/a72751c5d626380dedeed30f55f7a80ba3dc710d/integrations/pi/extensions/index.ts). Doctrine/design: [README](https://github.com/basicmachines-co/basic-memory/blob/a72751c5d626380dedeed30f55f7a80ba3dc710d/README.md), [lifecycle skill](https://github.com/basicmachines-co/basic-memory/blob/a72751c5d626380dedeed30f55f7a80ba3dc710d/skills/memory-lifecycle/SKILL.md). | No checkout access gap identified. Implementation limits: incomplete initial storage and host-path inspection prevents whole-system conclusions. Doctrine/design limits: prescriptions and product claims do not establish compliance or deployed behavior. No captured execution, production data or experiment; prevents observed reliability, effectiveness or causal claims. |
