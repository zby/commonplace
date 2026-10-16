---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Binder's local-first knowledge graph, shipped access surfaces and agent workflows at commit e4066d750ac5c6918706f44b12daa261b261106e."
run-id: AAS-2026-10-15-binder-a35c41531d40-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: e4066d750ac5c6918706f44b12daa261b261106e
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/mpazik/binder
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-binder/related-systems/mpazik--binder
  revision: e4066d750ac5c6918706f44b12daa261b261106e
  sha256: null
---

# Binder boundary

## Boundary and evidence

Binder is in scope as a **memory/knowledge/context-engineering system**, not as an enclosing autonomous agent runtime. Its intended use is persistent, typed, shared state for people, scripts and agents. The target is the shipped repository, including its knowledge graph engine, CLI runtime, document synchronization, MCP and HTTP access, editor integrations, library entry points, and shipped agent skills and examples. This is a **whole-system** boundary: callers and prompts shipped in this repository remain inside the target even when they use a library or launch an external agent executable. SRC-1, `README.md`, `packages/cli/src/index.ts`, `packages/cli/src/workspace.ts`, `examples/journal/git-import-logs.ts`.

The README explicitly includes agent memory among the uses:

> **Agent context and memory** so your AI tools have somewhere typed and persistent to share state among themselves and people. Structured, fully transparent and easy to maintain.
> --- `README.md`

Initial tracing establishes the state loop, rather than treating the repository package alone as the system:

- **Produce and admit state:** CLI update, MCP transact, HTTP transactions, document synchronization and editor saves feed the knowledge graph. The transaction processor prepares configuration changes before record changes against the resulting schema. SRC-1, `packages/cli/src/commands/update.ts`, `packages/cli/src/mcp/tools/transact.ts`, `packages/cli/src/http/server.ts`, `packages/cli/src/plugins/docs/commands.ts`, `packages/cli/src/lsp/handlers/save-handler.ts`, `packages/repo/src/transaction-processor.ts`.
- **Persist and maintain state:** workspace opening connects a SQLite database to the knowledge graph; the CLI runtime installs journal, undo and document-rendering plugins. Graph updates use the transaction preparation/application path; post-commit subscribers maintain derived files and logs. These responsibilities are included, not delegated to an excluded caller. SRC-1, `packages/repo/src/local/open.ts`, `packages/repo/src/knowledge-graph.ts`, `packages/cli/src/runtime.ts`, `packages/cli/src/plugins/journal/index.ts`, `packages/cli/src/plugins/undo/register.ts`, `packages/cli/src/plugins/docs/index.ts`.
- **Reload and consume state:** read/search and relation expansion expose retained entities through fresh workspace opens. The bundled workspace library uses the full CLI runtime. The shipped journal driver creates missing periodic records through the CLI; journal prompts subsequently read retained entries and write summaries or plans. Task workflows read stored task state to select their next guide. SRC-1, `packages/cli/src/commands/read.ts`, `packages/repo/src/knowledge-graph.ts`, `packages/cli/src/workspace.ts`, `examples/journal/journal.ts`, `examples/journal/skills/day-start/SKILL.md`, `examples/journal/skills/day-summary/SKILL.md`, `examples/workflow/skills/implement-task/SKILL.md`.

The executable write entry is explicit:

> update: (input: TransactionInput) =>
>       prepareApplyAndNotify(async (tx) => {
> --- `packages/repo/src/knowledge-graph.ts`

The later-use path is also present in shipped prompts, not merely a proposed external use:

> After completing a guide, re-read the task and check the table again. If another condition applies, load that guide next. If no conditions match, go to implement.
> --- `examples/workflow/skills/implement-task/SKILL.md`

The journal summary procedure separates discussion and confirmation from persistence:

> Use `binder update` to update the target day's entry (key from context):
> --- `examples/journal/skills/day-summary/SKILL.md`

These prompt instructions are doctrine/design evidence, not evidence that a model obeyed them. The journal Git-import script is included as a shipped model-consuming caller: it reads prior/current journal logs, invokes an external `claude` or `opencode` command, parses proposed entries and prints a changeset. Printing is not persistence; no automatic application of that changeset is inferred. The generic `callLlm` helper also belongs inside the source boundary, but initial search found its definition rather than an integrated core command consumer. Its presence alone does not turn the database into an agent runtime. SRC-1, `examples/journal/git-import-logs.ts`, `packages/cli/src/lib/llm.ts`.

### Frozen revision and applicability

The sole frozen source is SRC-1 at **e4066d750ac5c6918706f44b12daa261b261106e**. The read-only checkout's HEAD matched the acquired revision. The applicability cutoff is **2026-10-15**, the supplied run date; it is not a claim that upstream was unchanged on that date. No other revision, live website, package release, linked video or external repository supplies evidence. The overall tier is **code-grounded**, with implementation and doctrine/design distinguished below. No target code, tests, examples or model calls were executed.

### Coverage of the shipped repository

The tracked top-level tree was enumerated before classification. “Included” fixes functional scope; it does not claim every file has already received a detailed audit. Initial inspection below names the material paths traced. Remaining detailed inspection is distinguished from unavailable evidence and deliberate exclusions.

| Top-level tracked path | Status and role | Initial inspection / limits and conclusion prevented |
|---|---|---|
| `.binder/` | Included: the project's own curated workspace configuration. | Read `.binder/README.md` and `.binder/config.yaml`; inventoried `fields.yaml`, `types.yaml`, `navigation.yaml`. Detailed schema contents not yet inspected. The README says changing internal scratchpad material is maintained separately; its absence prevents conclusions about the maintainer's full live workspace. |
| `.github/` | Excluded: branding and screenshot assets. | Tree inspected; no executable workflow files in this revision. Images are not used as proof of operation; this prevents screenshot-based UX or run claims. |
| `.gitignore` | Excluded: repository ignore configuration. | Inventoried, not content-inspected; no inference about ignored runtime state or deployment packaging. |
| `.idea/` | Excluded: contributor IDE configuration. | Inventoried separately from the included IntelliJ integration. No conclusion about individual developer environment behavior. |
| `.ignore` | Excluded: search ignore configuration. | Inventoried, not content-inspected; no claim about contributor search behavior. |
| `.prettierignore` | Excluded: formatter configuration. | Inventoried, not content-inspected; formatting coverage is not assessed. |
| `.vscode/` | Excluded: contributor editor settings. | Inventoried separately from the included VS Code integration. No claim about contributor-specific editor configuration. |
| `AGENTS.md` | Included: shipped project/developer doctrine. | Read fully; package responsibilities and testing declarations are intent, not test results. |
| `LICENSE` | Excluded: legal terms. | Inventoried; no licensing analysis. |
| `README.md` | Included: intended use, entry surfaces, setup and roadmap. | Read fully; remote images/video and linked sites not fetched. Roadmap and advertised capabilities are not automatically treated as implementation. |
| `bun.lock` | Included: dependency pinning context. | Inventoried, not content-inspected. No dependency implementation or reproducible-build conclusion. |
| `docs/` | Included: source-native concepts, maintenance/developer instructions and HTTP/workspace-script guides. | Read `docs/concepts/repository.md`; inventoried concepts, contributing instructions, `docs/guides/http-server.md`, `docs/features/cli/workspace-scripts.md`. Other documents remain available for detailed inspection, not access gaps. Claims such as conflict-free sync in the concept document need separate implementation support. |
| `eslint.config.js` | Included: development checking configuration. | Inventoried, not content-inspected; lint enforcement is not established. |
| `examples/` | Included: shipped agent callers and retained-state workflows. | Read journal README, `journal.ts`, `git-import-logs.ts`, day-start and day-summary prompts, and workflow implement-task prompt; inspected journal schema opening and searched all workflow/journal skills for read/write consumers. `add-log.ts`, remaining journal skills, workflow capture/refinement and guide details remain available for later inspection. Include their persistence, reload and maintenance duties; do not reduce scope to the engine API. |
| `integrations/` | Included: editor clients that start the LSP. | Read `integrations/vscode/src/extension.ts` and `integrations/intellij-plugin/src/main/kotlin/com/binder/intellij/lsp/BinderLspServerDescriptor.kt`. They launch Binder LSP. Other settings/build files inventoried; no claim about actual installation or editor execution. |
| `package.json` | Included: monorepo build, entry and test commands. | Read fully. Declared commands were not run. |
| `packages/` | Included: executable state loop and evaluators. | `cli/src/index.ts` dispatch; `cli/src/runtime.ts` plugin wiring; `cli/src/workspace.ts` full-runtime library caller; `repo/src/local/open.ts` database reopen; `repo/src/knowledge-graph.ts` mutation, query and subscription paths; `repo/src/transaction-processor.ts` admission; CLI read/update, MCP request/tool handlers, HTTP routes, LSP save handling and docs sync/render paths inspected. Journal/undo registration and model helper inspected. `cli/src/document/`, `cli/src/lib/snapshot.ts`, `repo/src/changeset-*`, `repo/src/transaction-*`, `repo/src/entity-store.ts`, schema/model/filter/relationship paths and `utils/src/` are included supporting implementation; deeper algorithms remain to be inspected. |
| `skills/` | Included: shipped operation, import, modeling and app-building instructions. | Read `skills/binder-cli/SKILL.md`; title/section and usage searches across binder-import, binder-modeling, binder-app and references. Detailed remaining skill instructions are not yet inspected. These are prompt contracts, not runtime-enforced policies. |
| `tools/` | Included: development checker implementation. | Inventoried `tools/eslint-rules/require-ctx-for-services.js`; not yet content-inspected. No claim about its effectiveness. |
| `tsconfig.json` | Included: build/typechecking context. | Inventoried, not content-inspected; successful typechecking is not established. |

Evaluators are inside `packages/`, not excluded as incidental tests. Initial inspection read the round-trip portion of `packages/cli/tests/doc-sync.test.ts` and all of `packages/cli/tests/workspace-script.test.ts`; searched test declarations in MCP, HTTP, LSP and knowledge-graph suites. These cover authored checks for reading after writes, file synchronization, editor saves and transaction behavior. Other unit/integration test bodies remain available for analysis. None supplies an observed passing run here. SRC-1, `packages/cli/tests/doc-sync.test.ts`, `packages/cli/tests/workspace-script.test.ts`, `packages/cli/tests/mcp.test.ts`, `packages/cli/tests/http.test.ts`, `packages/cli/tests/lsp.test.ts`, `packages/repo/src/knowledge-graph.test.ts`.

### External dependencies and access limits

Node/Bun, SQLite adapters, Drizzle, Zod, MCP/LSP libraries, Hono, pi-ai/model services, editor hosts and externally installed agent executables are dependencies, not independently inspected systems. Workspace-defined plugins, hook commands, scripts and custom HTTP modules are supported extension boundaries; shipped loaders and their integration are included, but unshipped user extensions are not. Consequently this run cannot establish arbitrary extension behavior, provider correctness, host-agent scheduling, prompt loading in a particular harness, or end-to-end model compliance. SRC-1, `packages/cli/package.json`, `packages/repo/src/local/open.ts`, `packages/repo/src/local/plugin-loader.ts`, `packages/cli/src/http/server.ts`, `examples/journal/git-import-logs.ts`.

No required shipped material was inaccessible during boundary declaration. Available-but-uninspected details above are not access gaps and do not narrow the selected system. Missing live workspace contents and missing execution evidence do limit operational and efficacy conclusions. The source checkout supports source analysis, not claims of measured retrieval quality, autonomous improvement, successful deployment or causal effects.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/mpazik/binder` | e4066d750ac5c6918706f44b12daa261b261106e | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-binder/related-systems/mpazik--binder`. Implementation: CLI dispatch/runtime/workspace, repo opening/knowledge graph/transaction processing, read/update, MCP search/transact, HTTP routes, editor launchers, save/sync/render paths, journal/undo registration, Git-import caller and LLM helper; authored tests as source. Doctrine/design: README, AGENTS, repository concept, curated workspace README/config, CLI skill, journal README/schema opening/day-start/day-summary and task implementation prompt. Coverage table distinguishes full reads, bounded excerpts, searches and inventoried material. Listed paths are initial inspection, not an allowlist. | Implementation: [dispatch](https://github.com/mpazik/binder/blob/e4066d750ac5c6918706f44b12daa261b261106e/packages/cli/src/index.ts), [workspace open](https://github.com/mpazik/binder/blob/e4066d750ac5c6918706f44b12daa261b261106e/packages/repo/src/local/open.ts), [graph](https://github.com/mpazik/binder/blob/e4066d750ac5c6918706f44b12daa261b261106e/packages/repo/src/knowledge-graph.ts), [runtime wiring](https://github.com/mpazik/binder/blob/e4066d750ac5c6918706f44b12daa261b261106e/packages/cli/src/runtime.ts), [journal caller](https://github.com/mpazik/binder/blob/e4066d750ac5c6918706f44b12daa261b261106e/examples/journal/git-import-logs.ts). Doctrine/design: [README](https://github.com/mpazik/binder/blob/e4066d750ac5c6918706f44b12daa261b261106e/README.md), [later-use prompt](https://github.com/mpazik/binder/blob/e4066d750ac5c6918706f44b12daa261b261106e/examples/workflow/skills/implement-task/SKILL.md), [journal summary](https://github.com/mpazik/binder/blob/e4066d750ac5c6918706f44b12daa261b261106e/examples/journal/skills/day-summary/SKILL.md). | No inaccessible tracked source established. Untracked live workspace and external dependencies are not captured; no observed execution or causal experiment. Implementation supports source-path claims; prompt text supports intended procedure only. Neither establishes deployed behavior or efficacy. |
