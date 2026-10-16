---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Atomic's shipped knowledge system, clients, agentic consumers and maintenance drivers at commit 983bea6baf449d060514c94b3b15b5f85f77ba9b."
run-id: AAS-2026-10-12-atomic-f98683232831-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "983bea6baf449d060514c94b3b15b5f85f77ba9b"
analysis-cutoff: "2026-10-12"
evidence-tier: code-grounded
source:
  identity: https://github.com/kenforthewin/atomic
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/atomic-f98683232831/related-systems/kenforthewin--atomic
  revision: "983bea6baf449d060514c94b3b15b5f85f77ba9b"
  sha256: null
---

# Atomic boundary

## Boundary and evidence

This run analyses Atomic as a shipped personal knowledge system, not merely its Rust library or MCP endpoint. The intended use is to explain how retained notes and generated content enter storage, receive model-dependent enrichment, are maintained and admitted, and are later consumed by search, chat, wiki synthesis and reports. The target class is `memory/knowledge/context-engineering system`; its bounded chat and research agents are included mechanisms, not evidence that Atomic owns an external MCP client's enclosing runtime.

The boundary is `whole-system`: the frozen repository includes core logic, the standalone server's background drivers, the cloud composition's dispatcher, desktop and mobile shells, browser capture, frontend state consumers, plugins, import/reset utilities and evaluators. Shipped callers are included even when they communicate through HTTP or directly write SQLite. There is no excluded in-repository host supplying the material maintenance loop. This is an initial boundary trace, not a claim that every included implementation detail has already been audited.

The immutable evidence is SRC-1 at commit `983bea6baf449d060514c94b3b15b5f85f77ba9b`, with applicability cutoff **2026-10-12**. HEAD matches the acquisition object and the checkout reports no modifications. No other repository, website, downloaded dataset or release binary is frozen. Overall evidence is **code-grounded**: inspected implementation supplies operation paths, while target documentation supplies declared intent. No target code, tests, examples, benchmark or provider calls were executed. Therefore this boundary does not establish observed reliability, deployed behavior, benchmark scores or causal improvements.

### Initial shipped-loop trace

1. **Produce and persist.** The public core `create_atom` writes through storage, enqueues embedding/tagging work and processes the queue. The MCP adapter calls that core path; the browser extension posts to `/api/atoms`; the iOS share extension posts to `/api/ingest/url`. Obsidian sync retains a file-to-atom mapping and updates or creates atoms. The shared command-line importer instead prepares a direct SQLite insert with pending enrichment statuses. These are included producers, not interchangeable execution paths. SRC-1: `crates/atomic-core/src/lib.rs`, `crates/atomic-server/src/mcp/server.rs`, `extension/background/service-worker.js`, `mobile/ios/App/ShareExtension/ShareViewController.swift`, `plugins/obsidian-plugin/src/sync-engine.ts`, `scripts/import/shared/index.js`.

> let atom_with_tags = self.storage.insert_atom_impl(&id, &request, &now).await?;
> --- `crates/atomic-core/src/lib.rs`

> INSERT INTO atoms (id, content, source_url, created_at, updated_at, embedding_status, tagging_status)
> VALUES (?, ?, ?, ?, ?, 'pending', 'pending')
> --- `scripts/import/shared/index.js`

2. **Maintain.** The standalone server supplies feed polling, registered draft-pipeline and graph-maintenance tasks, ledger garbage collection, wiki retry sweeps and scheduled report dispatch. The cloud driver is also material: its executor dispatches pipeline batches, system tasks, feed polls, wiki regeneration and reports into core routines. The desktop shell launches `atomic-server` as a sidecar. Thus neither the standalone scheduler nor the cloud dispatcher can be omitted by calling Atomic a library. SRC-1: `crates/atomic-server/src/main.rs`, `crates/atomic-cloud/src/main.rs`, `crates/atomic-cloud/src/dispatcher.rs`, `src-tauri/src/lib.rs`.

> registry.register(Arc::new(atomic_core::pipeline_task::DraftPipelineTask));
> registry.register(Arc::new(
>     atomic_core::graph_maintenance::GraphMaintenanceTask,
> ));
> --- `crates/atomic-server/src/main.rs`

3. **Admit generated state.** Reports resolve source scope, call their agent, reject empty prose and write a finding with provenance and citations through a transactional storage helper. Wiki routes expose proposal creation, retrieval, acceptance and dismissal. Agentic wiki retrieval explicitly filters to captured atoms rather than report findings. These paths establish that generated-content admission belongs inside the boundary; the detailed correctness of each gate remains for later analysis. SRC-1: `crates/atomic-core/src/reports/runner.rs`, `crates/atomic-server/src/routes/wiki.rs`, `crates/atomic-core/src/wiki/agentic.rs`.

> let kinds = crate::models::KindFilter::only(crate::models::AtomKind::Captured);
> --- `crates/atomic-core/src/wiki/agentic.rs`

4. **Reload and consume.** Chat saves the user message, reloads the conversation and its scope, builds model context and runs a bounded tool loop. Its completion path saves the assistant turn, tool calls and citations. The shipped frontend can also turn an answer into a new atom through the ordinary create path. MCP supplies retained wiki and report readers as well as atom readers and writers. These consumers are part of Atomic; downstream MCP clients are not. SRC-1: `crates/atomic-core/src/agent.rs`, `crates/atomic-core/src/agent_runtime/run.rs`, `src/components/chat/saveAnswerAsAtom.ts`, `src/stores/chat.ts`, `src/lib/transport/command-map.ts`, `crates/atomic-server/src/mcp/server.rs`.

> let mut api_messages = vec![Message::system(system_prompt)];
> api_messages.extend(messages);
> --- `crates/atomic-core/src/agent.rs`

> export async function saveAnswerAsAtom(input: AnswerAtomContentInput): Promise<AtomWithTags> {
>   const content = buildAnswerAtomContent(input);
>   const tagId = await findOrCreateChatAnswersTag();
>   return useAtomsStore.getState().createAtom(content, undefined, [tagId]);
> }
> --- `src/components/chat/saveAnswerAsAtom.ts`

5. **Evaluate.** The benchmark crate and fixtures are included consumers. The inspected LongMemEval path imports sessions as atoms, waits for enrichment, searches in hybrid mode and maps retrieved atoms back to session IDs. Its documentation distinguishes retrieval scoring from future answer-generation and judge scoring. Evaluator source is not an observed evaluation result. SRC-1: `bench/README.md`, `crates/atomic-bench/src/suites/memory_longitudinal.rs`, `crates/atomic-bench/src/suites/pipeline_smoke.rs`.

### Top-level tracked coverage

Every top-level tracked entry is classified below. Grouped entries receive the same classification individually. “Included” fixes scope; the inspection column distinguishes an initial trace from detail not yet inspected. An available but unread file is not an access gap. Directory rows name material paths rather than treating the directory name as sufficient coverage. All rows refer to SRC-1.

| Top-level entry | Classification and role | Initial inspection and remaining detail | Exclusion limit |
| --- | --- | --- | --- |
| `crates` | Included: core state, models, storage, agentic consumption, service drivers and evaluation | Traced `atomic-core/src/lib.rs`, `agent.rs`, `agent_runtime/run.rs`, `extraction.rs`, `wiki/agentic.rs`, `reports/runner.rs`; `atomic-server/src/main.rs`, `routes/chat.rs`, `routes/wiki.rs`, `mcp/server.rs`; `atomic-cloud/src/main.rs`, `dispatcher.rs`; `atomic-bench/src/suites/memory_longitudinal.rs`, `pipeline_smoke.rs`; searched manager, executor and wiki runners. Included for further inspection: SQLite/Postgres adapters and migrations, ingestion, search, graph maintenance, compaction, task ledger, report/wiki prompts and citation gates, cloud tenant admission/quotas/backpressure, account/backup/deletion paths, MCP bridge, test-support and crate test suites. | None; all shipped runtime variants remain in scope. |
| `src` | Included: user production, state reload, generated-output consumption and admission UI | Inspected `components/chat/saveAnswerAsAtom.ts`; searched `stores/chat.ts` and `lib/transport/command-map.ts` connecting commands to atom/search/wiki/chat/ingestion APIs. Included detail not yet inspected: atom/wiki/report stores and readers, `WikiProposalDiff.tsx`, report editors, settings, import/cache/transport code, embedded frontend tests. | None. |
| `src-tauri` | Included: desktop server lifecycle and local import integration | Traced `src/lib.rs` sidecar launch; `src/main.rs`, `src/apple_notes.rs`, capabilities and configuration are included but not yet inspected in detail. | None; desktop driver is not an external host. |
| `extension` | Included: browser capture, offline queue and API writes | Inspected `background/service-worker.js` API write and searched queue/sync driver; content extraction, configuration and popup/options surfaces remain included, not yet inspected in detail. | None. |
| `mobile` | Included: mobile shells and share capture | Inspected `ios/App/ShareExtension/ShareViewController.swift` ingestion request. iOS main/shared-config/plugin code and Android shell/configuration are included; other native details not yet inspected. | None; no claim of equivalence to an untracked App Store client. |
| `plugins` | Included: shipped external-platform capture, persistence mapping and consumers | Inspected `obsidian-plugin/src/sync-engine.ts` file sync; searched `discord/src/core/atomic-client.ts` atom CRUD/search. Included further detail: Discord pipeline/dedup/settle/confirmation, Obsidian sync-state, chat/wiki/search views and WebSocket/client code, plugin tests. | None; host-platform APIs are external dependencies, but plugin responsibilities are Atomic's. |
| `scripts` | Included: imports, reset/repair, stress tooling and build drivers | Read `README.md`, inspected `import/shared/index.js`; searched `import/obsidian.js`, `reset-chunks.js`, `reset-tags.js` writes/deletions. Included further detail: RSS/Wikipedia import, database reset/drop, stress scripts, benchmark download and editor/MCP harnesses, development/release/build scripts. | None; direct database maintenance is not excluded as mere tooling. |
| `bench` | Included: evaluator contract and tracked fixtures | Read `README.md`; inventoried `datasets/atomic-mini/` and `datasets/longmemeval-mini.json`. Fixture contents not yet inspected; no tracked run output was identified by the tree inventory. | None; untracked/downloaded datasets are not evidence. |
| `docs` | Included: source-native manuals, design and maintenance instructions | README references inspected; tree identifies `manual/concepts/`, `manual/guides/`, `manual/self-hosting/`, `reference/embedding-tagging-pipeline.md`, `plans/` and target-authored `research/`. These documents are available but not yet individually inspected; plans and audits require attribution, not adoption as implementation fact. Images/video are presentation assets. | None; no document-derived performance conclusion is established here. |
| `README.md` | Included: declared target, features and shipped architecture | Read completely. Architecture declaration checked against initial core/server/cloud/client traces. | None. |
| `AGENTS.md`, `CLAUDE.md`, `CHANGELOG.md` | Included: target development instructions and historical claims | Inventoried, not yet inspected; they are evidence data, not instructions binding this worker. | None; history does not substitute for current code. |
| `Cargo.toml`, `package.json` | Included: workspace and shipped command entry points | Read completely; workspace includes cloud, benchmark and test-support crates; npm exposes import and reset commands. | None. |
| `Cargo.lock`, `package-lock.json` | Included: pinned dependency metadata | Inventoried, not yet inspected. | None; dependency behavior still requires independent evidence. |
| `capacitor.config.ts`, `index.html`, `tsconfig.json`, `tsconfig.node.json`, `vite.config.ts`, `vitest.config.ts` | Included: mobile/frontend build, startup and test configuration | Inventoried; npm scripts establish build targets, but configuration details remain uninspected. | None. |
| `.cargo`, `.github` | Included: build and CI/release composition | Inventoried `.cargo/config.toml` and `.github/workflows/` cloud-image, Docker, release, plugin-release and test workflows; details not yet inspected. | None; source tests/workflows do not prove successful runs. |
| `deploy`, `docker` | Included: deployment, backup and serving composition | Inventoried `deploy/docker-compose.yml`, `cloud-init.yml`, `scripts/`, `README.md`, `MONITORING.md`, proxy/telemetry configuration; `docker/litestream.yml`, nginx variants and supervisord. Available deployment details not yet inspected. | None; live service topology remains unobserved. |
| `Dockerfile`, `cloud.dockerfile`, `server.dockerfile`, `web.dockerfile`, `docker-compose.build.yml`, `docker-compose.dev.yml`, `docker-compose.test.yml`, `docker-compose.yml`, `fly.toml.example` | Included: packaged execution variants | Inventoried; server/desktop/cloud entry paths traced in code, packaging details not yet inspected. | None; no assertion about deployed image contents. |
| `public` | Included: frontend runtime assets and callback/configuration surfaces | Inventoried `manifest.webmanifest`, `openrouter-callback.html`, icons, fonts and `vite.svg`; callback behavior not yet inspected. | None; static assets supply no memory-quality evidence. |
| `.dockerignore`, `.gitignore`, `.nvmrc` | Included: packaging exclusions and tool-version metadata | Inventoried, not yet inspected. | None. |
| `LICENSE` | Excluded: legal text, not a state-loop mechanism | Deliberate analytical exclusion, not unavailable evidence. | Prevents an independent licensing/compliance assessment. |

### External dependencies and limits

Provider implementations for OpenRouter, Ollama and OpenAI-compatible services are inside the repository; provider services, model weights and their response behavior are outside it. SQLite/sqlite-vec, PostgreSQL, Rust/JavaScript/native framework dependencies and third-party editor/platform libraries are dependencies, not separately frozen sources. Browser, Obsidian, Discord, mobile OS and MCP-client runtimes are external hosts; the shipped Atomic integration code remains included. These exclusions prevent conclusions about host internals, provider quality, dependency guarantees or the end-to-end behavior of an external autonomous agent. The declared provider and platform roles are grounded in SRC-1 `README.md`, `Cargo.toml`, `package.json` and the integration paths named above.

No source access gap was encountered for the frozen checkout. No runtime credentials, live cloud tenant, production logs, external provider trace or benchmark execution result was supplied. That absence prevents operational and causal conclusions, not source-level analysis. Uninspected included files are future inspection work under SRC-1, not evidence that their mechanisms are absent. Later analysis may inspect any file at this commit without adding a source ID; another revision, repository or capture requires a new evidence-boundary decision.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/kenforthewin/atomic` | 983bea6baf449d060514c94b3b15b5f85f77ba9b | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/atomic-f98683232831/related-systems/kenforthewin--atomic`. Implementation: tracked-tree/workspace inventory; core atom insertion/queue, agent context/tool loop and persistence, wiki source filter, report finding write, standalone schedules and cloud dispatch, REST wiki admission/chat reload, MCP atom writes/readers, desktop sidecar, frontend command and saved-answer paths, browser/mobile ingestion, Obsidian sync and Discord API client, direct-import/reset write paths, benchmark pipeline/session retrieval. Doctrine/design: complete `README.md`, `bench/README.md`, `scripts/README.md`; tagging prompt in `crates/atomic-core/src/extraction.rs`. Initial inspection does not restrict later reads at this commit. | Implementation: `crates/atomic-core/src/lib.rs`, `crates/atomic-core/src/agent.rs`, `crates/atomic-core/src/agent_runtime/run.rs`, `crates/atomic-core/src/wiki/agentic.rs`, `crates/atomic-core/src/reports/runner.rs`, `crates/atomic-server/src/main.rs`, `crates/atomic-server/src/routes/wiki.rs`, `crates/atomic-server/src/routes/chat.rs`, `crates/atomic-server/src/mcp/server.rs`, `crates/atomic-cloud/src/main.rs`, `crates/atomic-cloud/src/dispatcher.rs`, `src-tauri/src/lib.rs`, `src/components/chat/saveAnswerAsAtom.ts`, `src/stores/chat.ts`, `src/lib/transport/command-map.ts`, `extension/background/service-worker.js`, `mobile/ios/App/ShareExtension/ShareViewController.swift`, `plugins/obsidian-plugin/src/sync-engine.ts`, `plugins/discord/src/core/atomic-client.ts`, `scripts/import/shared/index.js`, `scripts/import/obsidian.js`, `scripts/reset-chunks.js`, `scripts/reset-tags.js`, `crates/atomic-bench/src/suites/memory_longitudinal.rs`, `crates/atomic-bench/src/suites/pipeline_smoke.rs`. Doctrine/design: [README at reviewed commit](https://github.com/kenforthewin/atomic/blob/983bea6baf449d060514c94b3b15b5f85f77ba9b/README.md), [benchmark contract at reviewed commit](https://github.com/kenforthewin/atomic/blob/983bea6baf449d060514c94b3b15b5f85f77ba9b/bench/README.md), `scripts/README.md`, `crates/atomic-core/src/extraction.rs`. Workspace/commands: `Cargo.toml`, `package.json`. | No checkout access gap. Implementation supports source behavior, not successful execution. Doctrine/design supports declared purpose/contracts, not verification of operation. No observed-run or causal-experiment evidence is registered; live deployments, external service behavior and benchmark outcomes cannot be established. |
