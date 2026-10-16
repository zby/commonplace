---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "ByteRover CLI's repository-defined memory system at commit 1052ac1a5dd0fde4da8693d4712064f7876c269c, with external callers and dependency implementations outside the frozen evidence."
run-id: AAS-2026-10-15-byterover-cli-71610aaf716b-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: "1052ac1a5dd0fde4da8693d4712064f7876c269c"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/campfirein/byterover-cli
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-byterover-cli/related-systems/campfirein--byterover-cli
  revision: "1052ac1a5dd0fde4da8693d4712064f7876c269c"
  sha256: null
---

# ByteRover CLI boundary

## Boundary and evidence

This run examines how ByteRover CLI retains project knowledge and supplies it to coding agents, including how knowledge is authored, admitted, maintained and retrieved. The target is the repository-defined memory/knowledge/context-engineering system, not merely its agent library or an MCP endpoint. Its advertised purpose is persistent structured memory (SRC-1, `README.md`), and its shipped workflow explicitly directs later use of retained content (SRC-1, `src/server/templates/sections/workflow.md`):

> - **Start from memory.** First retrieve relevant context with `brv query`, then read only the code that's still necessary.
> - **Keep a local context tree.** The context tree is your local memory store—update it with `brv curate` when you learn something valuable.
> --- `src/server/templates/sections/workflow.md`

The boundary includes all first-party tracked implementation, prompts, connector instructions, clients, maintenance paths and tests at the frozen commit. Same-repository CLI, TUI and WebUI callers are included, not treated as external hosts. The installed `brv` entry maps to `bin/run.js`, which dispatches through oclif; `package.json` declares the command directory, hooks and resource-copy build steps. Initial tracing follows CLI curate into session persistence and daemon dispatch, daemon validation/write and side effects, and query into retrieval and rendering (SRC-1, `package.json`, `bin/run.js`, `src/oclif/lib/curate-session.ts`, `src/server/infra/daemon/agent-process.ts`, `src/oclif/lib/query-retrieval.ts`, `src/server/infra/executor/query-executor.ts`).

Do not infer that every public memory operation invokes ByteRover's own LLM from the presence of an internal agent runtime. The inspected CLI curate path returns an authoring prompt to its caller and resumes with caller-authored HTML; the query path dispatches deterministic retrieval. The latter describes its division of responsibility explicitly (SRC-1, `src/oclif/lib/query-retrieval.ts`):

> * mode removes those tiers: the calling agent owns synthesis,
> * byterover just retrieves + renders. No LLM lives inside byterover
> * on this path.
> --- `src/oclif/lib/query-retrieval.ts`

The curate continuation dispatches a `curate-tool-mode` task; the daemon validates the topic, backs up existing content for review, writes it, updates runtime signals and logs, and schedules index regeneration. These are shipped state responsibilities within the target, rather than responsibilities attributed to an excluded caller (SRC-1, `src/oclif/lib/curate-session.ts`, `src/server/infra/daemon/agent-process.ts`). The MCP surface also supplies authoring instructions and uses the same task family (SRC-1, `src/server/infra/mcp/tools/brv-curate-tool.ts`). Maintenance instructions split structural candidate enumeration from the caller's semantic judgment and subsequent writes (SRC-1, `src/server/templates/skill/dream.md`).

The boundary kind is **complete artifact, partial loop**. The frozen evidence covers the main repository artifact, including its first-party clients, but not the implementation of the calling coding agents that generate, select and later act on knowledge. Nor does it include the transport-client dependency or shared UI implementation. The shared UI is a Git submodule reference, not tracked source content available in this checkout: `packages/byterover-packages` points to commit `2dec813d8dcb473d46ff575d043391ddb423efd2`, and its directory has no captured files. `src/webui/App.tsx` imports that package, and the Vite configuration resolves it from either the submodule or an installed package. These are actual dependency boundaries, not evidence that an available first-party file was inaccessible (SRC-1, `.gitmodules`, `package.json`, `src/webui/App.tsx`, `src/webui/vite.config.ts`). The submodule reference does not register a second frozen repository.

### Functional coverage and inspection status

“Included, pending detailed inspection” means available evidence for later jobs, not an access gap or a claim that its behavior has already been established.

| Surface | Boundary treatment and initial inspection | Limit or conclusion prevented |
|---|---|---|
| Entry and packaging | Included; inspected `package.json`, `bin/run.js` and tracked tree. Other `bin/` launchers and `src/index.ts` are available for detailed tracing. | No installed release or build was executed; source does not establish successful installation. |
| Public CLI and session state | Included; inspected `src/oclif/commands/query.ts`, the curate command's entry/flags, and kickoff, continuation and dispatch portions of `src/oclif/lib/curate-session.ts`; query dispatch in `src/oclif/lib/query-retrieval.ts`. Other commands, hooks and client helpers remain available. | Source supports the protocol division, not observed caller compliance or completion quality. |
| Agent and daemon | Included; inspected the curate-tool-mode branch in `src/server/infra/daemon/agent-process.ts` and query-tool-mode retrieval in `src/server/infra/executor/query-executor.ts`. `src/agent/`, daemon routing/pooling, executors and storage remain included for deeper inspection. | No target execution, provider calls or concurrency experiments were performed. |
| Retention and admission | Included; inspected writer contract and initial validation in `src/server/infra/render/writer/html-writer.ts`, plus daemon write/log/backup/sidecar/index wiring. Rendering, context-tree, storage, review, migration, version-control and cloud-client code remain included. | Detailed correctness and failure behavior require further source tracing; no cloud-server implementation is frozen. |
| Shipped instructions and maintenance | Included; inspected `src/server/templates/sections/workflow.md`, the first maintenance-workflow sections of `src/server/templates/skill/dream.md`, MCP curate description and `docs/curate-protocol.md` protocol sections. All `src/server/templates/`, `src/agent/resources/`, dream implementation and connector installers remain included. | Declared procedures do not establish that users or external agents follow them. Documentation can diverge from implementation and must be attributed separately. |
| First-party user interfaces | Included; inspected `src/webui/App.tsx` and build/dependency resolution in `src/webui/vite.config.ts`; enumerated TUI/WebUI context, task, review and transport paths. Detailed client behavior remains to be inspected. | Missing shared UI and transport dependency implementation prevents complete end-to-end UI/transport verification. |
| Evaluators and assertions | Included; inspected benchmark claims in `README.md` and `paper/README.md`; enumerated `test/` and searched curate-session test cases. `paper/main.tex`, fixtures and other test bodies remain available, not yet inspected. | No benchmark run artifacts or test execution were supplied. Reported scores are not observed results of this run or evidence of the current tool-mode path's effectiveness. |
| Ancillary repository material | `scripts/`, configuration, CI, developer-agent instructions, contribution documents, changelog, assets and license are included as repository context; initially tree-enumerated, not substantively inspected. | No behavioral finding is inferred from their presence. |
| External dependencies and hosts | Excluded implementations: npm/Git packages (including transport and shared UI), model services, ByteRover Cloud, hub registries, external coding-agent runtimes and external documentation pages. Their in-repository adapters, contracts and shipped instructions remain included. | Prevents conclusions about host model reasoning, external persistence/access controls, dependency internals or deployed behavior. No other repository, live page or revision may supply evidence without a boundary change. |

The source is frozen at `1052ac1a5dd0fde4da8693d4712064f7876c269c`, with applicability cutoff **2026-10-15**. The cutoff is this run's evidence boundary, not a claim about later releases. Overall evidence is **code-grounded**: implementation was inspected, while README, paper and instruction claims remain attributed doctrine/design or reported operation. No observed-run or causal-experiment evidence is registered.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/campfirein/byterover-cli` | 1052ac1a5dd0fde4da8693d4712064f7876c269c | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-byterover-cli/related-systems/campfirein--byterover-cli`. Implementation: tracked tree, `package.json`, `bin/run.js`, CLI query and curate entry, session kickoff/continuation/dispatch, query dispatch, daemon curate-tool-mode branch, query-tool-mode retrieval, writer validation entry, MCP curate description and WebUI dependency resolution. Doctrine/design: README, workflow template, dream skill workflow, curate protocol sections. Reported operation: benchmark assertions in README and paper README. This initial inspection list is not an allowlist; all files tracked by this repository at the revision remain available. | Implementation: [entry](https://github.com/campfirein/byterover-cli/blob/1052ac1a5dd0fde4da8693d4712064f7876c269c/bin/run.js), [session protocol](https://github.com/campfirein/byterover-cli/blob/1052ac1a5dd0fde4da8693d4712064f7876c269c/src/oclif/lib/curate-session.ts), [daemon writer path](https://github.com/campfirein/byterover-cli/blob/1052ac1a5dd0fde4da8693d4712064f7876c269c/src/server/infra/daemon/agent-process.ts), [retrieval](https://github.com/campfirein/byterover-cli/blob/1052ac1a5dd0fde4da8693d4712064f7876c269c/src/server/infra/executor/query-executor.ts). Doctrine/design: [shipped workflow](https://github.com/campfirein/byterover-cli/blob/1052ac1a5dd0fde4da8693d4712064f7876c269c/src/server/templates/sections/workflow.md). Reported operation: [paper README](https://github.com/campfirein/byterover-cli/blob/1052ac1a5dd0fde4da8693d4712064f7876c269c/paper/README.md). | Shared UI submodule contents, dependency internals, external hosts and services are not captured; prevents whole-loop/deployed-system verification. No run traces or benchmark result artifacts supplied; benchmark claims support attributed reporting only. Available but uninspected files are identified above and are not access gaps. |
