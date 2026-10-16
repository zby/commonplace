---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Origin, branded Wenlan in the frozen checkout, as a local knowledge system at commit 61b462ea6adf019b3e27d3f58ac5a0fe055f76b1."
run-id: AAS-2026-10-15-origin-805d03bc599f-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "61b462ea6adf019b3e27d3f58ac5a0fe055f76b1"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/7xuanlu/origin
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-16-origin/related-systems/7xuanlu--origin
  revision: 61b462ea6adf019b3e27d3f58ac5a0fe055f76b1
  sha256: null
---

# Origin boundary

## Boundary and evidence

This run examines Origin's shipped knowledge-production, maintenance, review and reuse loop. The frozen checkout calls the product Wenlan. That branding does not change the supplied repository identity. The intended use is to explain how documents, conversations, direct notes and agent captures become retained memories and pages that humans and AI clients can subsequently use. It is not an analysis of an enclosing Claude Code, Codex or ChatGPT runtime.

The target class is **memory/knowledge/context-engineering system**. Its model-dependent work includes knowledge organization and page synthesis; it also supports storage and retrieval without a configured generative model. This is an in-scope system, not merely a generic database or isolated MCP adapter. SRC-1, `README.md` and `crates/wenlan-core/README.md` distinguish these modes:

> Local memory mode does storage and retrieval without a local model or API key. Extraction, richer distill cycles, and page synthesis require an on-device model or configured provider.
> --- `crates/wenlan-core/README.md`

The boundary kind is **whole-system**: the core library, owning daemon, desktop application, frontend, CLI, MCP transports, shipped client instructions and optional remote-access relay all belong to the target. The desktop and command-line callers are not excluded hosts simply because they use HTTP. Initial inspection traced these responsibilities in SRC-1:

- Entry and ownership: `Cargo.toml` declares the core, types, server, MCP, CLI and app workspace members. `crates/wenlan-server/src/main.rs` prepares retained state, registers workers, starts the scheduler and serves HTTP. `app/src/lib.rs` contains desktop startup and daemon-sidecar selection.
- Admission and persistence: `crates/wenlan-mcp/src/tools.rs` maps capture to `/api/memory/store`; `crates/wenlan-server/src/memory_routes.rs` implements admission, durable-store status and write signalling. `crates/wenlan-core/src/db.rs` opens the local libSQL file and exposes document upserts. CLI dispatch and recall were traced through `crates/wenlan-cli/src/main.rs` and `crates/wenlan-cli/src/commands/recall.rs`.
- Maintenance and reload: `crates/wenlan-server/src/scheduler.rs` owns automatic work and calls the Markdown edit watcher. `crates/wenlan-core/src/sources/page_watcher.rs` scans retained page projections and reflects external edits back into database state. `app/src/sources/sync.rs` delegates source synchronization to the daemon. `crates/wenlan-core/src/prompts/mod.rs` supplies the intelligence prompt registry, including compiled defaults and override-file loading.
- Synthesis and review: `crates/wenlan-core/src/synthesis/distill.rs` exposes page refresh through the canonical page-write path. The inspected refresh contract covers citation verification and review proposals for human-owned pages; this boundary does not establish that every writer obeys that contract. `plugin/skills/curate/SKILL.md` specifies explicit user decisions for pending revisions, captures and refinements.
- Later consumption: `plugin/skills/recall/SKILL.md` instructs a client agent to query retained memory and assess returned hits. `crates/wenlan-mcp/src/tools.rs` forwards recall to `/api/memory/search` and returns memories and supplemental pages. The handler in `crates/wenlan-server/src/memory_routes.rs` resolves read scope and invokes database retrieval. `src/lib/tauri.ts` and `app/src/api.rs` expose desktop access to retained data and review operations.
- Remote access and evaluation: `relay/src/worker.ts` wires OAuth queries and device reverse connections; `relay/README.md` describes their deployment and reachability constraints. `crates/wenlan-core/src/eval/runner.rs` constructs per-case databases and seeds fixtures. `docs/eval/README.md` distinguishes retrieval snapshots from end-to-end answer-quality reporting.

Two short passages retain the evidence for responsibilities that a library-only boundary would miss:

> // Automatic enrichment is intentionally not spawned from the request path.
> // The ambient scheduler owns admission, ordering, retries, and the one-call
> // budget for every automatic inference stage.
> --- `crates/wenlan-server/src/memory_routes.rs`

> match wenlan_core::sources::page_watcher::sync_filesystem_edits(&db, &knowledge_path)
> --- `crates/wenlan-server/src/scheduler.rs`

These establish source-level ownership and a reload call, not measured scheduling behavior or demonstrated successful reuse. Client-side instructions are part of the mechanism, not evidence that an external model followed them:

> Re-read the returned memories against the *original* query. Promote the
> ones that directly answer the question; demote ones that just share
> keywords.
> --- `plugin/skills/recall/SKILL.md`

### Repository coverage

The tracked tree was enumerated at the reviewed commit. Every top-level tracked item is classified below; grouped root-file rows name each item explicitly. Included means within the functional boundary, not exhaustively verified. Material paths named above received initial source inspection; uninspected files remain available for later jobs under SRC-1. There is no source-access gap requiring a partial-loop boundary.

| Top-level tracked item(s) | Classification and material paths or role | Inspection status and exclusion limit |
| --- | --- | --- |
| `crates/` | Included: `wenlan-core/src/db.rs`, `sources/`, `synthesis/`, `post_write/`, `refinery/`, `prompts/`, `retrieval/`, `eval/`; `wenlan-server/src/main.rs`, `scheduler.rs`, routes and workers; `wenlan-mcp/src/main.rs`, `tools.rs`, transports; `wenlan-cli/src/main.rs`, commands; `wenlan-types/src/` contracts. | Initial producer, storage, maintenance, reload, consumer and evaluator trace above. Remaining modules and tests are available, not all inspected; inclusion does not certify every path. |
| `app/` | Included: `src/lib.rs`, `api.rs`, `sources/`, daemon lifecycle, review/repair and remote-relay integration; `eval/` fixtures. | Startup, API and source-sync paths inspected or searched. Other native paths and fixtures remain available. |
| `src/` | Included: `main.tsx`, `App.tsx`, `lib/tauri.ts`, `components/memory/` editors, source readers and review surfaces. | Tauri invocation surface and page-detail references initially searched. Individual UI flows remain available, not behaviorally verified. |
| `plugin/` | Included: `skills/` capture, recall, brief, handoff, distill, curate, pages and lint procedures; `.mcp.json`, runners and hooks. | Recall and curate read; capture searched. Remaining shipped skills and wiring remain available. |
| `plugin-codex/` | Included: generated `skills/`, `overlay.json`, MCP runner and manifests. | README inspected: shared MCP backend and generation relationship to Claude skills. Generated variants remain available for parity checks. |
| `plugin-contract.json` | Included: cross-client plugin contract. | Enumerated, not yet inspected; no contract-conformance conclusion. |
| `relay/` | Included: `src/worker.ts`, OAuth, grants, reverse-device transport and proxy; deployment configuration and tests. | Worker wiring and README initially inspected. Detailed authorization and transport correctness remain to be established. |
| `docs/` | Included: knowledge/setup/technical/privacy contracts, Markdown projection documentation, `eval/` definitions and tracked result artifacts. | Initial eval workflow inspection; other documents remain available. Images and translated copies are not independent operational evidence. |
| `e2e/` | Included: memory, pages, sources, review, connection and runtime UI tests and mocks. | Tree inspected, individual tests not yet inspected. No test-pass claim. |
| `scripts/` | Included where they operate knowledge or evaluate it: smoke/first-run paths, lint maintenance probes, live distill/reconcile checks, evaluation seeding and analysis, plugin generation/validation. | Tree inspected; implementation remains available. Release/CI/visual-generation helpers deliberately excluded from functional conclusions; no build or distribution assurance. |
| `README.md`, `README.es-ES.md`, `README.zh-Hans.md`, `README.zh-Hant.md` | Included: declared product behavior and setup. | English product description inspected; translations not independently checked. |
| `Cargo.toml`, `Cargo.lock`, `package.json`, `pnpm-lock.yaml`, `index.html` | Included: workspace, dependencies and shipped frontend entry wiring. | Workspace manifest read; other wiring enumerated, not audited. No dependency-integrity conclusion. |
| `.agents/`, `.claude-plugin/` | Included: plugin marketplace discovery manifests. | Tree inspected, manifest contents not yet inspected; no discovery-success claim. |
| `chatgpt-app-submission.json` | Included: remote-client declared integration contract. | Enumerated, not inspected; no submission-readiness or approval conclusion. |
| `preview/`, `review/` | Excluded: browser previews, fixtures, mocks and review-shell substitutes. | Deliberate exclusion from real-runtime evidence; cannot establish production behavior from these substitutes. |
| `public/` | Excluded: fonts and licenses. | Tree inspection only; prevents typography or asset-license assessment, not knowledge-loop analysis. |
| `docker/`, `install.sh` | Excluded: container distribution and installer. | Tree inspection only; prevents conclusions about installation or deployed-image fidelity. |
| `.claude/`, `.githooks/`, `.github/`, `.config/`, `AGENTS.md`, `CLAUDE.md` | Excluded: repository-development agent configuration, hooks, CI and contributor instructions. | Distinct from included end-user plugin instructions; no development-process or CI-effectiveness assessment. |
| `.gitattributes`, `.gitignore`, `.release-please-manifest.json`, `release-please-config.json`, `version.txt` | Excluded: source-control and release metadata. | No release reproducibility, version-synchronization or publication conclusion. |
| `Cross.toml`, `clippy.toml`, `rust-toolchain.toml`, `tsconfig.json`, `tsconfig.tools.json` | Excluded: cross-build, lint and compiler configuration. | No platform-build or static-check assurance. |
| `playwright.config.ts`, `playwright.review.config.ts`, `vitest.config.ts` | Excluded: test harness configuration. | Tests remain available as source under included directories, but this run does not execute them or certify harness coverage. |
| `vite.config.ts`, `vite.dev-live.config.ts`, `vite.first-use-app.config.ts`, `vite.first-use-live.config.ts`, `vite.preview.config.ts`, `vite.review.config.ts` | Excluded: build and preview flavor configuration. | No production-bundle or preview-parity assurance. |
| `CHANGELOG.md`, `HISTORY.md`, `LICENSE` | Excluded: historical and legal context. | No historical evolution or license-compliance conclusion. |

### Frozen evidence and limits

The source is the acquired Git object unchanged: `https://github.com/7xuanlu/origin` at `61b462ea6adf019b3e27d3f58ac5a0fe055f76b1`. The checkout's HEAD matched that revision and its working tree was clean at inspection. The applicability cutoff is the supplied run date, **2026-10-15**. This is a revision boundary, not a claim about an installed release on that date. No other repository, later commit or moving website is evidence. Links in the target documentation are not separately acquired sources.

The overall tier is **code-grounded**. Source inspection supports implementation structure; target documentation and comments support attributed intent and contracts. No target program, test, example or model call was executed. Tracked evaluation material remains within the source boundary, but reported benchmark results are not a causal experiment or an independently observed run in this analysis. Untracked private benchmark caches are unavailable, preventing independent reconstruction of results that depend on them (SRC-1, `docs/eval/README.md`).

External dependencies include the host agent runtimes and human decisions, libSQL, embedding/model libraries and weights, optional local or remote model providers, OS filesystem/service facilities, and Cloudflare services for the optional relay (SRC-1, `Cargo.toml`, `README.md`, `relay/src/worker.ts`). Their implementations, credentials, live libraries, downloaded models, provider responses and deployed services are not frozen here. This prevents conclusions about actual user outcomes, live authorization, network privacy in deployment, model quality, performance and persistence across real process failures. The boundary includes Origin's integration code without attributing external hosts' scheduling or reasoning to Origin.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/7xuanlu/origin` | 61b462ea6adf019b3e27d3f58ac5a0fe055f76b1 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-16-origin/related-systems/7xuanlu--origin`. Implementation: tracked tree; workspace; daemon startup and scheduler; MCP capture/recall; store/search handlers; database open/upsert APIs; filesystem page watcher; app source-sync proxy; CLI dispatch/recall; frontend Tauri calls; prompt registry; refresh entry; relay worker wiring; evaluator setup. Doctrine/design: English README product sections, core README, recall/curate skills, Codex README, eval workflow, relay README. Searches also located capture instructions, page-detail references and post-ingest paths. | Implementation: [workspace](https://github.com/7xuanlu/origin/blob/61b462ea6adf019b3e27d3f58ac5a0fe055f76b1/Cargo.toml), [daemon](https://github.com/7xuanlu/origin/blob/61b462ea6adf019b3e27d3f58ac5a0fe055f76b1/crates/wenlan-server/src/main.rs), [MCP tools](https://github.com/7xuanlu/origin/blob/61b462ea6adf019b3e27d3f58ac5a0fe055f76b1/crates/wenlan-mcp/src/tools.rs), [scheduler](https://github.com/7xuanlu/origin/blob/61b462ea6adf019b3e27d3f58ac5a0fe055f76b1/crates/wenlan-server/src/scheduler.rs), [watcher](https://github.com/7xuanlu/origin/blob/61b462ea6adf019b3e27d3f58ac5a0fe055f76b1/crates/wenlan-core/src/sources/page_watcher.rs). Doctrine/design: [product](https://github.com/7xuanlu/origin/blob/61b462ea6adf019b3e27d3f58ac5a0fe055f76b1/README.md), [recall instructions](https://github.com/7xuanlu/origin/blob/61b462ea6adf019b3e27d3f58ac5a0fe055f76b1/plugin/skills/recall/SKILL.md), [evaluation limits](https://github.com/7xuanlu/origin/blob/61b462ea6adf019b3e27d3f58ac5a0fe055f76b1/docs/eval/README.md). Other initially inspected paths are named in the boundary trace above and resolve at this same commit. | No checkout access gap. Initial inspection is not exhaustive. No independently observed execution, private benchmark caches, user databases, provider responses or deployment state: cannot establish operational success, reproduce private-cache results or infer causal effectiveness. |
