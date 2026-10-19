---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "AI-Context-OS public desktop, CLI and MCP memory system at frozen commit 9ed263080cadf98702bebb42d5260b45bd526f6c."
run-id: AAS-2026-10-18-ai-context-os-82777c0c3926-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "9ed263080cadf98702bebb42d5260b45bd526f6c"
analysis-cutoff: "2026-10-18"
evidence-tier: code-grounded
source:
  identity: https://github.com/alexdcd/AI-Context-OS
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-ai-context-os-retry-1/related-systems/alexdcd--AI-Context-OS
  revision: "9ed263080cadf98702bebb42d5260b45bd526f6c"
  sha256: null
---

# AI-Context-OS boundary

## Boundary and evidence

This analysis covers the shipped public AI-Context-OS system, branded MEMM: a local workspace memory and context layer intended for AI agents and human operators. It is in scope because it persists knowledge and serves selected context to model-consuming clients, and also ships its own provider-backed chat and ingestion paths. The target class is **memory/knowledge/context-engineering system**, not an enclosing general-purpose agent runtime. The boundary kind is **whole-system**: the desktop application, CLI, MCP transports, generated agent instructions, workspace lifecycle, admission paths, governance and evaluators belong to the target, rather than only the Rust retrieval API. Sources are read-only; no target, example, test or provider was executed. [SRC-1: `README.md`, `src-tauri/src/lib.rs`, `src-tauri/src/cli.rs`, `src-tauri/src/core/mcp.rs`, `src/components/chat/ChatPanel.tsx`, `src-tauri/src/commands/inbox.rs`]

The immutable boundary is commit `9ed263080cadf98702bebb42d5260b45bd526f6c` of `https://github.com/alexdcd/AI-Context-OS`. HEAD matched that pin and the checkout had no reported modifications. The applicability cutoff is **2026-10-18**, the supplied run date, not a claim that the snapshot represents private development on that date. Overall evidence is **code-grounded**; documentation supplies attributed intent and proposals, not proof of implementation or observed effectiveness.

The source explicitly limits its public coverage:

> This repository is temporarily limited to an earlier public snapshot.
> --- `README.md`

> Active development is continuing in private and a newer public version will be published again once it is ready.
> --- `README.md`

Private development and subsequent public revisions are outside the frozen source. This gap prevents conclusions about the current private product, later fixes or newer releases. It does not prevent analysis of the public snapshot. [SRC-1: `README.md`]

### Functional coverage and entry-point trace

The desktop bootstrap registers configuration, memory and raw-file operations, inbox capture and proposal admission, scoring/chat, governance, journal/tasks, vault switching, backup and observability commands. It starts an MCP HTTP service sharing workspace state. The CLI independently initializes, scans, scores, regenerates adapters and exposes stdio MCP; the desktop binary also has an embedded stdio-MCP mode. These are shipped drivers, not excluded callers. Binary declarations and command bodies establish these entry points. [SRC-1: `src-tauri/Cargo.toml`, `src-tauri/src/lib.rs`, `src-tauri/src/cli.rs`]

Persistence and later consumption were traced across the boundary, not inferred from a library declaration:

- **Production and editing:** the desktop memory-save command writes canonical content, updates its index and conditionally regenerates router artifacts. MCP `save_memory` writes Markdown and regenerates routers. Inbox proposal application writes promoted or source memories and refreshes retrieval state. Raw files, journal and tasks are additional shipped state surfaces, included for subsequent analysis rather than treated as external applications. [SRC-1: `src-tauri/src/commands/memory.rs`, `src-tauri/src/core/mcp.rs`, `src-tauri/src/commands/inbox.rs`, `src-tauri/src/lib.rs`]
- **Admission and reloading:** recursive indexing parses frontmatter, applies usage metadata and checks folder contracts. Root inbox content remains outside canonical retrieval until promotion; folder-contract violations are logged rather than universally rejected. Desktop workspace synchronization refreshes the index and binds a watcher. Watcher events reach a frontend hook that regenerates routing and reloads memories, files and graph after external edits or deletion. [SRC-1: `src-tauri/src/core/index.rs`, `src-tauri/src/commands/config.rs`, `src-tauri/src/core/watcher.rs`, `src/hooks/useFileWatcher.ts`]
- **Serving and consumption:** the engine scans retained files for each context query, builds a rules prelude, scores memories and selects detail levels. MCP returns assembled context and records access. The shipped chat panel calls `buildChatContext` and sends its result with conversation history to `chatCompletion`; the backend can reassemble vault context when none was supplied, then calls a configured provider. External agent clients are not the only consumers. [SRC-1: `src-tauri/src/core/engine.rs`, `src-tauri/src/core/mcp.rs`, `src/components/chat/ChatPanel.tsx`, `src-tauri/src/commands/inbox.rs`]
- **Prompts and maintenance:** router generation emits reading and writing instructions, while compatibility renderers wrap that output for Claude, Cursor and Windsurf. Inbox inference has a conservative JSON-proposal prompt. Governance/observability and optimization commands are in scope; an `apply_optimization` command changing a database status is not, by itself, proof of autonomous canonical edits. The autonomous-maintenance document is explicitly a feature proposal. [SRC-1: `src-tauri/src/core/router.rs`, `src-tauri/src/core/compat.rs`, `src-tauri/src/commands/inbox.rs`, `src-tauri/src/commands/observability.rs`, `docs/Memm wiki/sistema-autonomo-de-mantenimiento-ia.md`]
- **Bridge and evaluation surfaces:** Connectors builds summary copy/handoff output and can persist `.ai/scratch/handoff.md`; Simulation invokes the scoring endpoint. The ignored real-vault diagnostic and inline Rust tests are inspectable evaluator source, not observed test results. `sim_test.js` exercises graph-layout mechanics, not memory quality. [SRC-1: `src/views/ConnectorsView.tsx`, `src/views/SimulationView.tsx`, `src-tauri/tests/diagnose_vault_query.rs`, `src-tauri/src/core/engine.rs`, `sim_test.js`]

Minimum passages supporting the consequential classification and loop boundary:

> AI Context OS is a desktop app (`React + TypeScript + Rust`) that turns a local folder into a universal, tool-agnostic memory layer for AI agents.
> --- `README.md`

> let all_entries = scan_memories(root);
> let total_memories = all_entries.len() as u32;
> let manifest = build_router_manifest(&all_entries, root, config);
> let rules_content = render_mcp_prelude(&manifest);
> --- `src-tauri/src/core/engine.rs`

> const response = await chatCompletion({
>         messages: history,
>         system_prompt: SYSTEM_PROMPT,
>         include_vault_context: shouldUseVaultContext,
>         context_prompt: contextPrompt || null,
>         context_memory_ids: contextIds,
>         model: providerConfig?.model ?? null,
>       });
> --- `src/components/chat/ChatPanel.tsx`

> // Inbox is a transient capture surface and does not participate
> // in canonical memory retrieval until explicit promotion.
> if dir == root && name.as_ref() == INBOX_DIR {
>     continue;
> }
> --- `src-tauri/src/core/index.rs`

### Top-level tracked coverage

“Included” establishes functional scope, not exhaustive inspection of every file. Initial inspection focused on the material entry points and loop above. Available files awaiting detailed inspection are not access gaps and remain eligible evidence at the same commit under SRC-1.

| Top-level tracked path | Classification and role | Initial inspection / exclusion consequence |
|---|---|---|
| `.claude/` | Excluded developer-harness configuration | `settings.json` inspected: developer command permissions; exclusion prevents assessing the project's own coding-agent safety policy, not its shipped memory loop. |
| `.gitattributes` | Excluded Git metadata | Tree inventoried, contents not inspected; no conclusions about checkout normalization. |
| `.github/` | Included packaging context | `workflows/release.yml` inspected: tag-triggered Tauri build/publish workflow; no release execution evidence. |
| `.gitignore` | Excluded developer Git filtering | Tree inventoried, contents not inspected; no claim about ignored local development artifacts. |
| `.npmrc` | Included build context | Inventoried, not yet content-inspected; no package-manager configuration conclusion. |
| `CONTRIBUTING.md` | Included author-declared development contract | Inventoried, not yet content-inspected; no contribution-process assessment established. |
| `LICENSE` | Excluded legal terms | Inventoried, not content-inspected; no licensing conclusions. |
| `README.es.md` | Included source-native doctrine | Inventoried; English README initially inspected instead; translation parity not established. |
| `README.md` | Included purpose, scope and public-snapshot notice | Fully inspected; product claims remain attributed unless traced in implementation. |
| `assets/` | Excluded branding images | `Memm_logo0.png`, `Memm_logo0_transpa.png` inventoried; no visual-design assessment. |
| `docs/` | Included doctrine, technical explanations and proposals | Initial inspection: documentation headings, chat-pipeline headings and opening maintenance-proposal sections. Material paths include `algorithms-and-scoring.md`, `chat-context-pipeline-architecture.md`, `Memm wiki/architecture-and-operating-model.md`, `Memm wiki/folder-contracts.md`, `Memm wiki/ARQUITECTURA-ACTUAL-ROUTER-CONTEXTO-Y-MEMORIAS.md` and `Memm wiki/sistema-autonomo-de-mantenimiento-ia.md`; other wiki papers and theme/landing guides remain available, not yet deeply inspected. Proposals are not counted as implemented features. |
| `index.html` | Included frontend entry context | Inventoried; no HTML-host security assessment established. |
| `package.json` | Included frontend build and dependency contract | Fully inspected; scripts establish Vite/Tauri build entry context. |
| `pnpm-lock.yaml` | Included dependency pin context | Inventoried; dependency internals and supply-chain integrity not assessed. |
| `sim_test.js` | Included narrow evaluator | Fully inspected; D3 graph-layout simulation only, not a retention or retrieval benchmark. |
| `src-tauri/` | Included backend, shipped drivers, retained-state operations and evaluators | Inspected Cargo manifest, desktop bootstrap, CLI, core MCP/index/router/compat/watcher, context-engine opening and inline-test locations, memory save, workspace runtime synchronization, proposal application, chat fallback and optimization commands; diagnostic test opening inspected. All `src/commands/` domains, `src/core/` algorithms, `state.rs`, `main.rs`, `tests/`, capabilities and Tauri configuration remain in scope. Icon assets supply packaging, not behavioral evidence. Detailed algorithm/security review remains for downstream analysis. |
| `src/` | Included shipped callers and consumers | Inspected chat send path, file-watcher hook, connector handoff; searched editor, Explorer, Governance, Journal, Task, Simulation and Observability consumers. Material paths include `App.tsx`, `main.tsx`, `lib/store.ts`, `lib/tauri.ts`, `lib/vaultStore.ts`, `components/editor/`, `components/onboarding/`, `views/` and `hooks/`. Settings, localization and themes are included UI context; initial source inspection does not establish every presentation detail. |
| `tsconfig.json` | Included build context | Inventoried, not content-inspected; no compiler-configuration assessment. |
| `vite.config.ts` | Included frontend build context | Inventoried, not content-inspected; no bundler-configuration assessment. |

Coverage classifications above are grounded in the tracked tree and named paths of SRC-1. Functional findings use the commit-relative anchors in the preceding trace.

### External dependencies and evidence limits

The implementation depends on the local filesystem, Tauri and OS services, Rust/JavaScript packages, SQLite observability storage, MCP clients and optional inference providers. Their implementations are not separate frozen sources. The source manifest names `rmcp`, `rusqlite`, `reqwest`, Tauri plugins and frontend editor/state packages; source code distinguishes local model and API-provider handling. Their declarations establish integration dependencies, not successful interoperability or service availability. [SRC-1: `src-tauri/Cargo.toml`, `package.json`, `src-tauri/src/commands/inbox.rs`, `src-tauri/src/lib.rs`]

External agent reasoning, client-specific instruction loading, model inference quality and private user vaults are excluded. This prevents attributing end-to-end agent reliability, universal adapter compliance, provider quality or real-world retrieval accuracy to this snapshot. The included chat caller, CLI, connector bridge and generated prompts are not excluded with those hosts. No observed run or causal experiment was supplied; evaluator source and documentation cannot establish empirical quality, latency, maintenance autonomy or measured improvement. [SRC-1: `src-tauri/tests/diagnose_vault_query.rs`, `src-tauri/src/core/compat.rs`, `src-tauri/src/core/mcp.rs`, `src/components/chat/ChatPanel.tsx`]

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/alexdcd/AI-Context-OS` | 9ed263080cadf98702bebb42d5260b45bd526f6c | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-ai-context-os-retry-1/related-systems/alexdcd--AI-Context-OS`. Implementation: tracked tree; `package.json`, `src-tauri/Cargo.toml`, `src-tauri/src/lib.rs`, `src-tauri/src/cli.rs`, `src-tauri/src/core/index.rs`, `src-tauri/src/core/compat.rs`, `src-tauri/src/core/watcher.rs`, selected engine/router/MCP bodies, config/memory/inbox/observability command bodies, chat send path, connector handoff, watcher hook, consumer searches and evaluator source described above. Doctrine/design: full `README.md`, maintenance-proposal opening, documentation headings and generated router instructions. | Implementation: [bootstrap](https://github.com/alexdcd/AI-Context-OS/blob/9ed263080cadf98702bebb42d5260b45bd526f6c/src-tauri/src/lib.rs), [CLI](https://github.com/alexdcd/AI-Context-OS/blob/9ed263080cadf98702bebb42d5260b45bd526f6c/src-tauri/src/cli.rs), [MCP](https://github.com/alexdcd/AI-Context-OS/blob/9ed263080cadf98702bebb42d5260b45bd526f6c/src-tauri/src/core/mcp.rs), [chat caller](https://github.com/alexdcd/AI-Context-OS/blob/9ed263080cadf98702bebb42d5260b45bd526f6c/src/components/chat/ChatPanel.tsx). Doctrine/design: [README](https://github.com/alexdcd/AI-Context-OS/blob/9ed263080cadf98702bebb42d5260b45bd526f6c/README.md), [generated instructions](https://github.com/alexdcd/AI-Context-OS/blob/9ed263080cadf98702bebb42d5260b45bd526f6c/src-tauri/src/core/router.rs). | Public snapshot only; private continuation and later revisions unavailable, preventing current-private-product conclusions. No supplied runtime trace, provider execution, real user vault or experiment; prevents observed-quality or causal-effect claims. Available uninspected paths remain source evidence, not access gaps. |
