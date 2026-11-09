---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Eva-brain's desktop knowledge-maintenance system and shipped vault contract at commit 706fb91f4ee851cc355785f4e7c6eab37146938f."
run-id: AAS-2026-11-09-eva-brain-de4240cd9e79-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "706fb91f4ee851cc355785f4e7c6eab37146938f"
analysis-cutoff: "2026-11-09"
evidence-tier: code-grounded
source:
  identity: https://github.com/jp-lorenc1o/eva-brain
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/eva-brain-aee72a7a2324/related-systems/jp-lorenc1o--eva-brain
  revision: "706fb91f4ee851cc355785f4e7c6eab37146938f"
  sha256: null
---

# Eva-brain boundary

## Boundary and evidence

Eva-brain is an in-scope **memory/knowledge/context-engineering system**. Its intended use is a personal, local-first knowledge base maintained with an LLM, not a general autonomous-agent runtime. The whole-system boundary includes its desktop caller, Rust orchestration, runtime adapters, Markdown vault contract and starter files, MCP navigation service, structural linting, graph library, and shipped tests. The desktop is part of the target: it creates and imports brains, directs model-dependent maintenance, admits proposed changes, reloads the retained wiki, and lets users query or save derived answers. It is not an excluded host around a library API (SRC-1, `README.md`, `apps/desktop/src-tauri/src/main.rs`, `apps/desktop/src-tauri/src/ingest.rs`, `apps/desktop/src/main.ts`).

The source describes the durable intermediary explicitly:

> Eva is an open-source, local-first desktop app for building a personal
> knowledge base with an LLM. Instead of repeatedly retrieving from raw
> documents at question time, Eva helps an agent maintain a durable, linked
> Markdown brain between the sources and the user.
> --- `README.md`

The operating contract includes both production and later consumption of retained content:

> **Ingest:** read a source in `raw/`, search the existing wiki, create or update
> the necessary pages, preserve provenance, update the index, and let Eva append
> the operation log entry. Do not edit source files or infrastructure files.
> --- `schema/EVA.md`

> **Query:** search and read the wiki before answering. Cite the supporting page
> ids and source paths. Save an answer as an `analysis` page only when it will be
> useful later; otherwise leave the wiki unchanged.
> --- `schema/EVA.md`

Initial implementation inspection traced the material state loop. The Tauri entry point registers brain creation/import/settings, ingest enqueue/decision, query/save/decision, health, profile tools, and local-runtime setup. `bootstrap_vault` seeds the format marker and instructions. `ingest_enqueue` copies selected sources to `raw/`, commits them and queues jobs. `run_job` prepares a Git worktree, dispatches an agent and calls `gate_agent_changes`. That gate checks protected paths, commits changes and a log entry, compares lint issues, and either merges or holds for review. The implementation's branch condition is:

> if deletions.is_empty() && new_issues.is_empty() {
> --- `apps/desktop/src-tauri/src/ingest.rs`

The desktop's `openVault` reads Markdown back into `buildVault`, `buildGraph` and `lintVault`. Query adapters receive the retained vault; the MCP server reloads it per call. Query and profile-tool UI actions can send returned content through `query_save`; `prepare_query_review` writes an analysis, index entry and log in a worktree, and `query_decide` merges or discards it. Health has its own model-dependent advisory path. These are included shipped consumers and maintainers, not external application responsibilities (SRC-1, `apps/desktop/src/main.ts`, `apps/desktop/src-tauri/src/ingest.rs`, `packages/eva-mcp/server.mjs`, `packages/eva-mcp/vault-io.mjs`, `packages/wiki-lib/src/vault.ts`, `packages/wiki-lib/src/lint.ts`). This trace establishes the boundary, not that every safety or semantic promise succeeds in operation.

### Repository coverage

Every top-level tracked file or directory is classified below. Included means within the analysis boundary, not that every line has already been inspected. No material state-loop path is deliberately excluded or unavailable.

| Top-level path | Classification and role | Initial inspection and limits |
| --- | --- | --- |
| `.github/` | Included: packaging and publication context. | Inspected `workflows/pages.yml` and `workflows/release.yml`; distinguishes static-site deployment from app bundling and bundled-tool verification. No release execution evidence. |
| `.gitignore` | Included: repository hygiene. | Inspected ignore rules; not a vault admission mechanism. |
| `AGENTS.md` | Included: source-native development constraints and reported runtime history. | Inspected macOS scope, runtime/model guidance and compatibility reports; treated as doctrine or attributed reports, not binding analyst instructions or independently observed tests. |
| `LICENSE` | Included: distribution context. | Inventoried, not inspected; no legal interpretation offered. |
| `README.md` | Included: intended product, setup, operations and dependency claims. | Inspected in full; promotional and operational claims remain attributed unless grounded in implementation. |
| `apps/` | Included: shipped desktop caller and state owner. | Inspected `desktop/src-tauri/src/main.rs`; traced material sections of `desktop/src-tauri/src/ingest.rs` covering bootstrap, agent adapters/prompts, dispatch, worktree/gate, persistence, query/health/tools and decisions; inspected `desktop/src/main.ts` brain opening and query/tool save consumers, and searched UI call sites. Inspected `desktop/package.json`, `desktop/scripts/bundle-tools.mjs`, `desktop/src-tauri/tauri.conf.json` and `desktop/test/tauri-config.test.mjs`. Rust inline tests were located. Remaining implementation, UI/i18n/style/assets, capabilities and build metadata remain available for deeper inspection; no complete UI/security audit or test-result claim is made here. |
| `docs/` | Included: format and operational doctrine. | Inspected `V1_VAULT_CONTRACT.md`; inventoried `EVA_BRAIN_STANDARD.md` as available canonical standard, not yet read. The boundary does not substitute the older overview for that standard. |
| `marketing/` | Excluded: static promotional site and media, not the brain state loop. | Inspected `README.md` and Pages workflow to establish separation from the workspace/app build. Other site files not inspected. Exclusion prevents assessment of website behavior or validation of demo and promotional effectiveness claims. |
| `package.json` | Included: workspace/build/test entry points. | Inspected in full; identifies shipped packages and test dispatch. |
| `package-lock.json` | Included: dependency pin context. | Inventoried, not inspected; no dependency-supply-chain assessment. |
| `packages/` | Included: navigation, structural evaluation and wiki representation. | Inspected `eva-mcp/server.mjs`, `vault-io.mjs`, `lint-cli.mjs`, `wiki-lib/src/vault.ts` and `src/lint.ts`; inspected initial `wiki-lib/test/wiki-lib.test.ts` parsing/fixture/graph assertions and inventoried the remaining tests and 16-page `test-vault/`. `wiki-lib/src/parse.ts`, `graph.ts`, exports and package metadata remain available for deeper inspection. Tests are executable specifications, not evidence of successful runs or semantic knowledge quality. |
| `schema/` | Included: shipped operating prompts and format marker. | Inspected `EVA.md`, `AGENTS.md`, `CLAUDE.md`, `eva.json` in full. Instructions cover ingest, query, lint, profile, provenance and local history. |
| `templates/` | Included: starter state consumed by vault bootstrap. | Inspected `vault/index.md` and `vault/log.md`; Rust bootstrap inspected as their shipped consumer. |

All coverage entries refer to SRC-1 at the frozen commit. Material files merely not yet inspected are not access gaps and remain available to later jobs within this same source identity.

### Dependencies, exclusions and evidence limits

Eva owns the vault format, prompts, subprocess invocation and admission orchestration; it delegates model reasoning and tool execution to external Codex CLI, Claude Code, or OpenCode, with Ollama for the local option. Git, Node.js, Tauri, MCP SDK and TypeScript/Rust dependencies support the shipped implementation (SRC-1, `README.md`, `apps/desktop/src-tauri/src/ingest.rs`, `packages/eva-mcp/server.mjs`, `apps/desktop/package.json`). External runtime internals, provider services, model weights, user-global configuration, user documents and actual installed apps are not frozen here. This prevents attributing runtime-internal scheduling, real-world containment, model quality, end-to-end privacy or production reliability to inspected Eva code alone. Runtime adapters and generated configuration remain included; their external callees do not become Eva implementation.

The applicability cutoff is 2026-11-09; the evidence is the repository at commit `706fb91f4ee851cc355785f4e7c6eab37146938f`, not later upstream changes or current live documentation. The overall tier is code-grounded because shipped entry points and their state-producing/admitting/consuming paths are inspectable. No target code, tests, examples or services were executed. No independent run trace or causal experiment was supplied. Source-native test and compatibility reports may support attributed reported operation, but cannot establish measured effectiveness, cross-platform operation or a successful run of this exact revision.

## Source register

| Source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/jp-lorenc1o/eva-brain` | 706fb91f4ee851cc355785f4e7c6eab37146938f | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/eva-brain-aee72a7a2324/related-systems/jp-lorenc1o--eva-brain`. Implementation: desktop registration, selected Rust orchestration/adapters/persistence sections, desktop reload/query/tool-save consumers, MCP server/loader/lint CLI, wiki vault/lint, build configuration, workflow and test source described above. Doctrine/design: README, AGENTS, schema, operational overview and templates. Reported operation: README and AGENTS platform/runtime compatibility and model-selection claims, attributed only. | Implementation: [desktop entry](https://github.com/jp-lorenc1o/eva-brain/blob/706fb91f4ee851cc355785f4e7c6eab37146938f/apps/desktop/src-tauri/src/main.rs), [orchestration](https://github.com/jp-lorenc1o/eva-brain/blob/706fb91f4ee851cc355785f4e7c6eab37146938f/apps/desktop/src-tauri/src/ingest.rs), [desktop consumer](https://github.com/jp-lorenc1o/eva-brain/blob/706fb91f4ee851cc355785f4e7c6eab37146938f/apps/desktop/src/main.ts), [MCP](https://github.com/jp-lorenc1o/eva-brain/blob/706fb91f4ee851cc355785f4e7c6eab37146938f/packages/eva-mcp/server.mjs), [lint](https://github.com/jp-lorenc1o/eva-brain/blob/706fb91f4ee851cc355785f4e7c6eab37146938f/packages/wiki-lib/src/lint.ts). Doctrine/design: [vault contract](https://github.com/jp-lorenc1o/eva-brain/blob/706fb91f4ee851cc355785f4e7c6eab37146938f/schema/EVA.md). Reported operation: [README](https://github.com/jp-lorenc1o/eva-brain/blob/706fb91f4ee851cc355785f4e7c6eab37146938f/README.md), [development guidance](https://github.com/jp-lorenc1o/eva-brain/blob/706fb91f4ee851cc355785f4e7c6eab37146938f/AGENTS.md). | Frozen checkout accessible; no material repository access gap identified. External runtimes/models and real user vaults are outside the source set. No observed-run or causal-experiment layer: cannot establish actual run success, semantic quality, runtime-internal guarantees or causal benefit from source and test definitions alone. |
