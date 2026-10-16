---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Pond's shipped session archive, retrieval, restoration and host integrations at commit 0c440e130faf44052d0d896a585e572090079f1f."
run-id: AAS-2026-10-14-pond-7a589a889ca1-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "0c440e130faf44052d0d896a585e572090079f1f"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/tenequm/pond
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/pond-7a589a889ca1/related-systems/tenequm--pond
  revision: "0c440e130faf44052d0d896a585e572090079f1f"
  sha256: null
---

# Pond boundary

## Boundary and evidence

This run analyses Pond as a durable archive and recall system for agent sessions, not as an enclosing agent runtime. Its intended use is to preserve prior sessions, retrieve their content for later model context, and restore sessions into supported clients. The target class is **memory/knowledge/context-engineering system**; this includes archival recall rather than assuming a distilled-fact memory mechanism. The boundary kind is **whole-system**: the shipped Rust application and library, adapters, prompts, maintenance paths, host plugins, restoration consumers, deployment examples and evaluation material belong to the target. The host integrations are not excluded merely because they call Pond's APIs.

The frozen evidence is SRC-1, repository `https://github.com/tenequm/pond` at commit `0c440e130faf44052d0d896a585e572090079f1f`. The checkout HEAD equals this acquisition pin and the checkout status was clean. The applicability cutoff is **2026-10-14**, the supplied run date, not a claim that all reported measurements were made that day. The overall evidence tier is **code-grounded**. Source inspection supports implementation descriptions; the source's specification and tool instructions supply declared contracts. No target program, test, model provider or deployment was executed in this run.

### Qualification and functional loop

The source describes the archival purpose directly:

> pond ingests sessions from agentic clients - Claude Code, Codex, and others on the roadmap - into one canonical form, stores them in Lance, and serves search (full-text, with optional semantic search; one arm per query, Section 8.7) over them at message granularity.
> --- `docs/spec.md`

This is in scope because its retained state is served to model-driven clients through recall tools and shipped consumption instructions. The bundled skill makes that consumption policy explicit (SRC-1, `packages/pond/SKILL.md`):

> has it: recall first, then answer. Before you say "I don't know" or re-derive
> something that sounds prior, search pond.
> --- `packages/pond/SKILL.md`

The initially traced loop comprises:

- **Produce and admit:** external harnesses produce native logs; Pond's shipped adapter registry parses them into canonical events. `AdapterFactory` owns discovery/configuration and serialization; `Adapter` streams events and offers freshness planning. The CLI's sync pipeline drives these adapters, and `ingest_adapter` validates/batches their output. HTTP ingest is a second admission surface. Evidence: SRC-1, `packages/pond/src/adapter/mod.rs`, `packages/pond/src/main.rs`, `packages/pond/src/handlers.rs`, `packages/pond/src/transport.rs`.
- **Persist and maintain:** the session store filters existing message/part keys, optionally embeds new message rows, appends messages and parts and inserts absent sessions through the storage substrate. Sync has a shared pipeline for CLI and in-server use, including index maintenance and OpenClaw deletion detection. Scheduled sync, explicit optimize, copy and archive restore remain included state-maintenance paths. Evidence: SRC-1, `packages/pond/src/sessions.rs`, `packages/pond/src/substrate.rs`, `packages/pond/src/main.rs`, `packages/pond/src/schedule.rs`.
- **Reload and consume:** search handlers select full-text or optional vector retrieval from the store; get/session/message and SQL surfaces expose retained content. MCP tool descriptions route model callers to search and subsequent transcript reads. The Pi, OpenClaw and Hermes packages register recall tools and supervise or connect to a Pond server. Their managed server arguments include periodic sync, so the integrations participate in capture as well as recall. Evidence: SRC-1, `packages/pond/src/handlers.rs`, `packages/pond/src/transport.rs`, `packages/pi-pond/index.ts`, `packages/pi-pond/src/service.ts`, `packages/openclaw-pond/index.ts`, `packages/openclaw-pond/src/service.ts`, `packages/hermes-pond/__init__.py`, `packages/hermes-pond/service.py`.
- **Restore and continue:** the CLI reloads retained lineage and serializes it through a target adapter. Pi's shipped command bridges this write-producing CLI operation to the host's session switch; it is a material later consumer, not an external application excluded from the target. Evidence: SRC-1, `packages/pond/src/main.rs`, `packages/pi-pond/src/resume.ts`, `packages/pi-pond/index.ts`.

The Pi continuation handoff is executable code, not just an advertised use (SRC-1, `packages/pi-pond/index.ts`):

> await ctx.switchSession(outcome.sessionFile, {
>     withSession: async (fresh) => {
>       fresh.ui.notify(note, "info");
>     },
>   });
> --- `packages/pi-pond/index.ts`

Shipped prompt material includes both the bundled skill and plugin tool definitions. In particular, the Pi tools attach `promptSnippet` and `promptGuidelines`; its entry-point comment's “no prompt hooks” must not be read as absence of instructions supplied to the model (SRC-1, `packages/pi-pond/src/tools.ts`). These instructions and the tool descriptions are included even though the model's decision to invoke them remains a host/model responsibility.

### Repository coverage

The table classifies every top-level tracked file or directory found at the pin. **Included** means inside the analysis boundary, not that every blob has already been read. “Not yet inspected” is an inspection status, not an access gap. The initial inspection traced material entry points and consumers; later analysts may inspect further files at this same commit under SRC-1.

| Top-level tracked path | Classification and material paths/role | Initial inspection status; exclusion consequence |
|---|---|---|
| `packages/` | Included: `pond/src/main.rs` CLI/server/sync/copy/optimize/resume; `pond/src/adapter/` codecs; `sessions.rs`, `substrate.rs`, `rowmap.rs`, `syncstate.rs` persistence/freshness; `handlers.rs`, `transport.rs`, `render.rs`, `sql.rs`, `wire.rs` admission/retrieval; `embed.rs` optional model; `init.rs`, `schedule.rs`, `bin/pondw.rs` setup/maintenance; `pond/SKILL.md` consumption policy. Also `pi-pond/`, `openclaw-pond/`, `hermes-pond/` registration, managed capture, tool instructions, scoping and Pi resume; all package tests, fixtures and benches as evaluation evidence. | Inspected manifest, library surface, adapter seam, sync/server/resume implementation ranges, ingest/store/retrieval ranges, three plugin entry points, service/tool searches, Pi resume bridge and bundled skill; Windows launcher read. Individual codecs, remaining persistence internals, plugin scoping internals, tests/fixture contents and benches are not yet inspected. None unavailable; no material shipped loop path deliberately excluded. |
| `docs/` | Included: `spec.md` contracts; `site/src/pages/get-started/`, `guides/`, `reference/` setup/maintenance/consumption instructions; `adapters/` source-format documentation; `benchmarks/`, `researches/` evaluators, scripts and results; `plans/`, `check-later/`, `other/`, `references/` design/research context. Site assets/build files are supporting publication material. | Specification overview/scope and headings inspected; recall-context-cost report read. Other documents/scripts/results not yet inspected. Plans are not evidence of shipped implementation; reports are attributed measurements unless their run evidence is inspected. |
| `ops/` | Included: `examples/pi-fleet/worker.sh` and `docker-compose.yml` shipped producer/shared-volume/sync/read-side driver; `e2e/` CLI evaluator; `search-benchmarks/` retrieval evaluator; `scripts/`, `homebrew/`, `nix/`, `toolchain-id.json` release/profiling/support machinery. | Fleet worker read, compose capture/read-side ranges read; e2e README read; remaining scripts and results not yet inspected. Fleet driver stays included despite supplying external harness state. |
| `skills/` | Included: `pond-add-adapter/SKILL.md` adapter-building and conformance procedure. | Tree identified; body not yet inspected. This is a development instruction, distinct from the shipped recall skill in `packages/pond/`. |
| `README.md` | Included: purpose, installation, sync/recall/restore deployment and declared design. | Read completely; declarations are not automatically verified implementation or independent comparison evidence. |
| `server.json` | Included: MCP distribution/entry-point metadata. | Tree identified; body not yet inspected. |
| `AGENTS.md`, `CONTRIBUTING.md` | Included: source-native development/maintenance rules. | Tree identified; bodies not yet inspected; treated as target doctrine, not instructions to this analysis worker. |
| `CHANGELOG.md` | Included: source-native release account. | Tree identified; body not yet inspected; history does not establish current behavior. |
| `.cargo/`, `.github/`, `.moon/` | Included supporting build, test, release and repository-maintenance machinery: Cargo config; GitHub workflows/actions/hooks/security; Moon tasks/toolchains/workspace. | Tree inventory only; contents not yet inspected. No CI-success claim follows from presence. |
| `.envrc`, `.gitignore`, `.prototools`, `moon.yml`, `rust-toolchain.toml` | Included supporting environment, task and toolchain configuration. | Tree inventory only; bodies not yet inspected. |
| `Cargo.toml`, `Cargo.lock`, `flake.nix`, `flake.lock`, `kasetto.yaml`, `kasetto.lock` | Included workspace/build/dependency/package support. | Tree inventory only; package-level `packages/pond/Cargo.toml` inspected for binaries and dependencies. Root bodies not yet inspected. |
| `LICENSE` | Excluded from functional analysis: legal licensing text. | Deliberate exclusion prevents a licensing/compliance conclusion, not a storage/recall-loop conclusion. |

### External dependencies and limits

External agent runtimes and providers supply session records and execute later model/tool loops. Their implementations are outside this repository boundary. Their APIs are visible through shipped plugins and adapters, but this prevents attributing host context selection, provider behavior, upstream compaction or actual restored-session continuation to Pond alone. Pond's own plugin registration, prompts, capture supervision and session-switch handoff remain included. Evidence: SRC-1, `packages/pi-pond/index.ts`, `packages/openclaw-pond/index.ts`, `packages/hermes-pond/__init__.py`, `docs/spec.md`.

Lance/object-store services supply storage, indexing and concurrency primitives; Candle/model artifacts supply optional embeddings; axum, rmcp, Tokio and host SDKs supply transport/runtime interfaces. The package manifest and source specification establish these dependencies, but their external repositories, cloud services and remotely downloaded model weights are not additional frozen sources. Their absence prevents independently verifying their internals, operational reliability or deployed IAM/encryption. Evidence: SRC-1, `packages/pond/Cargo.toml`, `docs/spec.md`.

No required repository evidence was unavailable. Uninspected files listed above are available for later inspection. There is no newly observed execution trace or causal experiment. The benchmark report initially read supplies **reported operation** on one author's corpus/machine with five selected queries and byte-based token estimates; it cannot establish universal recall quality, current-pin latency, or causal downstream task improvement. Tests and captures in the repository are included evidence candidates, not assumed passing tests or authenticated production outcomes (SRC-1, `docs/benchmarks/recall-context-cost.md`, `ops/e2e/README.md`).

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/tenequm/pond` | 0c440e130faf44052d0d896a585e572090079f1f | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/pond-7a589a889ca1/related-systems/tenequm--pond`. Implementation: tracked tree; `packages/pond/Cargo.toml`, `src/lib.rs`, `src/main.rs` server/sync/resume ranges, `src/adapter/mod.rs` seam, `src/handlers.rs` ingest/search, `src/sessions.rs` write batch, `src/transport.rs` MCP search; searches in substrate/schedule/init; three plugin entry points and service/tool paths, Pi resume bridge, Windows launcher; `ops/examples/pi-fleet/worker.sh` and compose capture/read-side. Doctrine/design: complete `README.md`, `packages/pond/SKILL.md`, `docs/spec.md` overview/scope, plugin instruction text and `ops/e2e/README.md`. Reported operation: `docs/benchmarks/recall-context-cost.md`. Paths under `src/` in this cell are relative to `packages/pond/`. | Implementation: [CLI/server/sync/resume](https://github.com/tenequm/pond/blob/0c440e130faf44052d0d896a585e572090079f1f/packages/pond/src/main.rs), [store](https://github.com/tenequm/pond/blob/0c440e130faf44052d0d896a585e572090079f1f/packages/pond/src/sessions.rs), [Pi consumer](https://github.com/tenequm/pond/blob/0c440e130faf44052d0d896a585e572090079f1f/packages/pi-pond/index.ts), [MCP tools](https://github.com/tenequm/pond/blob/0c440e130faf44052d0d896a585e572090079f1f/packages/pond/src/transport.rs). Doctrine/design: [specification](https://github.com/tenequm/pond/blob/0c440e130faf44052d0d896a585e572090079f1f/docs/spec.md), [recall skill](https://github.com/tenequm/pond/blob/0c440e130faf44052d0d896a585e572090079f1f/packages/pond/SKILL.md). Reported operation: [context-cost report](https://github.com/tenequm/pond/blob/0c440e130faf44052d0d896a585e572090079f1f/docs/benchmarks/recall-context-cost.md). | No repository access gap. Implementation inspection is not execution verification; doctrine is not demonstrated behavior; reported measurements retain their corpus/machine/date and method limits. External hosts/services/model artifacts are not frozen here, preventing host-loop, cloud-security and provider-internals conclusions. Initial paths are not an allowlist: all files at this repository commit remain within the registered source. |
