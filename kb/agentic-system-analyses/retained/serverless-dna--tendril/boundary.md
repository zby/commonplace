---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Tendril's desktop agent, persistent capability registry and execution sandbox at commit e671a4143d28de68289efd81580002041bb4cb6a."
run-id: AAS-2026-10-15-tendril-f560fb299a37-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "e671a4143d28de68289efd81580002041bb4cb6a"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  kind: git
  identity: https://github.com/serverless-dna/tendril
  revision: e671a4143d28de68289efd81580002041bb4cb6a
  path: /home/zby/llm/commonplace/.commonplace/worktrees/tendril-f560fb299a37/related-systems/serverless-dna--tendril
  sha256: null
---

# Tendril boundary

## Boundary and evidence

This run covers Tendril as a shipped desktop agent system, not just its capability-registry API. Its intended use is to answer user requests by selecting existing tools or authoring and retaining new TypeScript capabilities for later execution. The target qualifies as an agent runtime: its Node sidecar constructs a model-backed Strands agent, streams user prompts through it and supplies callbacks that write and execute capabilities. The shipped Tauri host and React client are inside the boundary. They initialize the workspace, launch and restart the sidecar, submit prompts, expose retained capabilities and permit workspace-file editing (SRC-1, `tendril-agent/src/agent.ts`, `tendril-agent/src/index.ts`, `tendril-ui/src/App.tsx`, `tendril-ui/src-tauri/src/lib.rs`, `tendril-ui/src-tauri/src/workspace.rs`, `tendril-ui/src-tauri/src/files.rs`).

The classification is **enclosing runtime**, with a **whole-system** boundary. Delegating model/tool iteration to the external Strands SDK does not make Tendril only a registry subsystem. Tendril supplies the runnable agent, prompt, tool callbacks, protocol entry point and its own enclosing desktop application. The implementation explicitly constructs the agent and registers its three bootstrap tools (SRC-1, `tendril-agent/src/agent.ts`):

> tools: [
>       listCapabilities(registry),
>       registerCapability(registry),
>       executeCode(registry, workspacePath, config),
>     ],
> --- `tendril-agent/src/agent.ts`

The retained-state loop is included end to end: model-facing listing and authoring; registry metadata and source-file writes; later disk reads for listing and execution; Deno subprocess execution; and results returned through the agent stream to the desktop UI. Registry creation/replacement is a shipped mechanism, not evidence that generated tools are effective. In particular, the registry writes both the index and TypeScript source, and execution reloads source by name (SRC-1, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/loop/sandbox.ts`, `tendril-ui/src/context/AgentContext.tsx`):

> await this.saveIndex(index);
>
>     await fs.writeFile(path.join(this.toolsPath, `${definition.name}.ts`), code);
> --- `tendril-agent/src/loop/registry.ts`

> code = await registry.load(name);
> --- `tendril-agent/src/loop/tools.ts`

The shipped system prompt is included as an operational instruction, not merely documentation. It tells the model to consult retained capabilities and create one when none matches (SRC-1, `tendril-agent/src/loop/prompt.ts`):

> 1. listCapabilities() — always list first. Read the results.
> 2. Match found? → execute(name, args)
> 3. No match? → registerCapability(definition, code) then execute(name, args)
> --- `tendril-agent/src/loop/prompt.ts`

These instructions establish intended behavior, not enforced compliance or measured improvement across sessions. The boundary also includes the shipped human inspection and maintenance surfaces: capability browsing, tool-source viewing and workspace-file read/write commands. These are not an excluded external host (SRC-1, `tendril-ui/src/hooks/useCapabilities.ts`, `tendril-ui/src-tauri/src/capabilities.rs`, `tendril-ui/src/components/CapabilityBrowser.tsx`, `tendril-ui/src/components/FileExplorer.tsx`, `tendril-ui/src-tauri/src/files.rs`).

### Frozen evidence and limits

The sole frozen source is SRC-1 at **e671a4143d28de68289efd81580002041bb4cb6a**, verified as the acquired checkout's HEAD. The applicability cutoff is **2026-10-15**, the opening's run date; later revisions and current live documentation are not evidence. The overall tier is **code-grounded**. Source text and test definitions support implementation analysis; no target, tests, examples or model services were executed.

External dependencies include the Strands SDK and its provider adapters, Bedrock/OpenAI/Anthropic services or an Ollama endpoint, Node.js, Deno, Tauri and its shell/dialog/Stronghold plugins, and the platform filesystem/process facilities. Tendril's integration code is included; dependency implementations, model weights, service internals and remote packages fetched by generated tools are not frozen here. This prevents conclusions about SDK-internal iteration guarantees, provider reliability, actual sandbox isolation under attack or the behavior of arbitrary downloaded code. Provider selection and Deno invocation are inspectable at SRC-1, `tendril-agent/src/agent.ts` and `tendril-agent/src/loop/sandbox.ts`; bundling is inspectable at `Makefile`.

No user workspace, accumulated capability corpus, production trace or controlled intervention is supplied. Therefore this run cannot establish real tool reuse rates, longitudinal improvement, user outcomes or causal benefits of retention. Test source is not a passing test result. The inspected integration test covers protocol initialization/session creation/shutdown and can skip when the built entry point is absent; it does not demonstrate model-driven capability improvement (SRC-1, `tendril-agent/tests/integration.test.ts`).

### Repository coverage

Every top-level tracked entry is classified below. Included means within the functional boundary, not that every file has already received a detailed behavioral audit. Initial inspection traced the material production, persistence and consumption paths named above; supporting modules and historical specifications remain available at the same pin for later analysis. No material shipped runtime path was unavailable. Inventory-only and search-only coverage are distinguished from full-file inspection.

| Top-level entry | Classification and material paths | Inspection and role; excluded conclusion |
|---|---|---|
| `tendril-agent/` | Included: `src/index.ts`, `src/agent.ts`, `src/config.ts`, `src/loop/{prompt,tools,registry,sandbox}.ts`, `src/transport/`, `src/types.ts`, `src/costs.ts`; `tests/`, package/build configuration | Full-file inspection of entry point, agent construction, config, all four loop modules and `src/transport/protocol.ts`; full integration-test read and test-case search across all seven test files. Covers state creation, reload, model/tool integration and execution. Stream/error/cost details and remaining test bodies are included but not yet fully inspected. Tests are evaluator source, not observed results. |
| `tendril-ui/` | Included: `src/App.tsx`, `src/context/AgentContext.tsx`, `src/hooks/`, `src/components/`, `src/stronghold.ts`; `src-tauri/src/{lib,main,acp,events,config,workspace,files,capabilities}.rs`, Tauri manifests/capabilities, build configuration and assets | Full-file inspection of App, agent context, both hooks, Rust command registration, process lifecycle, workspace initialization, file access and capability reading. Targeted search traced capability viewing and file-editor writes in components. Remaining UI, credential/config/event implementation details and packaging assets are included but not yet fully inspected. The host's management and maintenance responsibilities remain in scope. |
| `Makefile` | Included: agent build, SEA/sidecar bundling, Deno download, desktop launch/release and quality-gate targets | Full-file read; establishes shipped build and launch wiring, not build success. |
| `README.md` | Included: declared purpose, architecture and workspace usage | Full-file read; doctrine/design only where not corroborated by code. Examples and claims are not observed runs. |
| `CHANGELOG.md` | Included as release-history documentation | Inventory only; not yet inspected and not used to establish implemented behavior. |
| `docs/` | Included: `agent-capability-spec.md`, project brief and addendum, `agent-integrator-spec.pdf` | Markdown heading/selected-text search and file inventory only; detailed text and PDF not yet inspected. Available design/protocol context, not a substitute for current implementation. |
| `specs/` | Included as design/history: `001-tendril-tauri-app/`, `002-ci-workflows-templates/`, `003-code-review-remediation/`, `004-multi-provider-support/`, including contracts and plans | File inventory only; detailed claims remain uninspected. Target-owned remediation records may be read as attributed design evidence, not independent validation. |
| `.github/` | Included: `workflows/quality-gate.yml`, `workflows/release.yml`; issue and pull-request templates as supporting material | Workflow command search and inventory. Build/check/release wiring is in scope; no CI results are supplied, so no claim of passing CI or successful platform releases. |
| `.agents/` | Excluded from product runtime: developer `skills/speckit-*` and `decisions/` | Inventory only. Development workflow and decision history, not capability instructions supplied by `createAgent`; no assessment of repository-development agent effectiveness. |
| `.claude/` | Excluded from product runtime: developer `skills/speckit-*` | Inventory only. No conclusions about Claude development workflows or their effects on product quality. |
| `.specify/` | Excluded development plane: scripts, extensions/git, integrations, templates and `memory/constitution.md` | Inventory and constitution-heading search. This is specification/development scaffolding, not the retained tool registry; no assessment of its planning/maintenance effectiveness. |
| `CLAUDE.md` | Excluded developer guidance | Heading/command search only; not treated as the product's agent prompt. No conclusions about developer instruction compliance. |
| `.gitignore` | Excluded repository hygiene configuration | Inventory only; no conclusions about ignored local artifacts or secret-handling effectiveness. |

All path-based coverage and classifications in this table refer to SRC-1. Excluded development material can be inspected for relevance, but it is not silently attributed to the product runtime.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/serverless-dna/tendril` | e671a4143d28de68289efd81580002041bb4cb6a | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/tendril-f560fb299a37/related-systems/serverless-dna--tendril`. Implementation: full-file reads of agent entry/config/construction, loop modules, protocol, Rust lib/acp/workspace/files/capabilities, React App/context/hooks and integration test; targeted searches of remaining test cases, UI capability/file consumers and CI commands. Doctrine/design: README fully read; documentation and constitution headings searched. Repository coverage table records inventory-only and pending detail inspection separately. | Implementation: [agent construction](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/agent.ts), [registry](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/registry.ts), [host lifecycle](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/acp.rs), [desktop caller](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src/App.tsx). Doctrine/design: [shipped prompt](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/prompt.ts), [README](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/README.md). | No checkout access gap. External dependency implementations and service behavior are outside this frozen repository. No supplied execution traces, accumulated workspaces or experiments: prevents observed-operation, longitudinal-effectiveness and causal-benefit conclusions. Uninspected available files are not access gaps. |
