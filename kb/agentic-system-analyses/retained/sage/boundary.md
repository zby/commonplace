---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "SAGE's shipped memory service, admission machinery, maintenance, prompts and consumers at commit e2e0242a421afbd356ed135d7d754a35b0ad5f14."
run-id: AAS-2026-10-15-sage-d3843de6d2dd-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: e2e0242a421afbd356ed135d7d754a35b0ad5f14
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/l33tdawg/sage
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/sage-d3843de6d2dd/related-systems/l33tdawg--sage
  revision: e2e0242a421afbd356ed135d7d754a35b0ad5f14
  sha256: null
---

# SAGE boundary

## Boundary and evidence

This run covers SAGE as a shipped memory/knowledge/context-engineering system, not merely its MCP API. Its intended use is to let authorized agents retain experience and retrieve it in later work. The boundary is whole-system: server entry points, signed admission and consensus, persistent and serving state, retrieval, maintenance, operator controls, shipped agent instructions, hooks, connectors, SDK consumers and evaluators are included. The frozen evidence is SRC-1 at `e2e0242a421afbd356ed135d7d754a35b0ad5f14`, with applicability cutoff 2026-10-15. HEAD matches that revision and the checkout reports no tracked modifications. Evidence is code-grounded, supplemented by source-native doctrine; nothing was executed to establish operational performance.

The scope is model-dependent even though its deterministic storage and consensus machinery does not itself constitute an enclosing conversational runtime. SAGE serves model clients, ships instructions controlling when they recall and write, and optionally calls semantic judges during admission. The enclosing Claude Code, Codex, Cursor and other model-client implementations are not shipped here and are not attributed to SAGE. SRC-1, `README.md`, `sage-memory/SKILL.md`, `internal/mcp/tools.go`, `internal/voter/gate.go`.

> SAGE gives AI agents a persistent memory of project decisions, failed approaches
> and useful lessons. Connect your tools to the same local node so authorized
> agents can record experience and recall relevant context in later sessions.
> --- `README.md`

> // Gate is the optional memory gate: a semantic check, asked of one or more
> // operator-configured judges, of whether a proposed memory is lasting
> // knowledge or a remark about the session it came from — and, for a memory
> // submitted with evidence, whether that evidence supports it.
> --- `internal/voter/gate.go`

### Shipped loop and boundary rationale

Initial tracing establishes that the repository contains both the memory service and material producers and consumers. `cmd/sage-gui/main.go` dispatches serving, MCP, hook, compaction, import/export, recovery and upgrade commands. `cmd/sage-gui/node.go` opens SQLite and Badger, constructs the REST server, wires the auto-voter and supervises canonical cleanup; `cmd/amid/main.go` supplies a separate server path with PostgreSQL. These are included drivers, not external hosts. SRC-1, `cmd/sage-gui/main.go`, `cmd/sage-gui/node.go`, `cmd/amid/main.go`.

The MCP turn path recalls committed content, conditionally submits an observation and checks the pipeline inbox. Signed REST admission and ABCI memory-submit/vote/commit handlers lead to canonical and serving state. The auto-voter polls pending memories, with optional background semantic judgment. Cleanup rechecks state and authority before signing a memory challenge. This is sufficient to select the system boundary; detailed guarantees of those paths remain matters for later analysis, not conclusions conferred by the boundary. SRC-1, `internal/mcp/tools.go`, `api/rest/memory_handler.go`, `internal/abci/app.go`, `internal/voter/voter.go`, `web/cleanup.go`.

> // Phase 1: Recall — get consensus-committed memories relevant to this topic.
> // Uses semantic vector search (Ollama) or FTS5 text search (hash mode).
> --- `internal/mcp/tools.go`

> // Phase 2: Store — save this turn's observation as an episodic memory.
> // Goes through consensus: submit → CheckTx → FinalizeBlock → Commit → auto-validator → committed.
> --- `internal/mcp/tools.go`

Shipped prompts are part of this loop. The skill prescribes inception, per-turn memory and reflection; the MCP implementation also returns mode-dependent instructions and reads custom boot instructions. Those surfaces must be compared rather than treating the skill as an exhaustive runtime contract. Session-start hooks print caller-scoped retained memories into host context. Opt-in pre-compaction capture submits transcript chunks and saves capture progress; resumed-session recall reads committed chunks and reconstructs thread context. Therefore retention and later use are not confined to explicit MCP calls, and the skill's privacy statements cannot be generalized across all configurations. SRC-1, `sage-memory/SKILL.md`, `internal/mcp/tools.go`, `cmd/sage-gui/hook.go`, `cmd/sage-gui/hook_precompact.go`, `cmd/sage-gui/nevercompact_recall.go`.

> // runHookSessionStart fetches recent committed memories and prints a context
> // block on stdout. Claude Code injects stdout from SessionStart hooks into the
> // agent's prompt.
> --- `cmd/sage-gui/hook.go`

> // Fetch custom boot instructions from preferences
> --- `internal/mcp/tools.go`

The browser extension implements its own recall/store turn path. The Level Up bridge returns recalled content to its caller and submits observations; the enclosing CTF agent is not supplied. SDK examples exercise stored-memory lifecycle operations. LoCoMo evaluation seeds conversations and retrieves evidence turns; the LongMemEval answer harness additionally supplies retrieved context to answer and judge models. All these shipped consumers and evaluation paths remain inside the analysis boundary, even where their external hosts, datasets or services do not. SRC-1, `extension/chrome/background.js`, `extension/chrome/sage-tools.js`, `integrations/levelup/sage_bridge.py`, `sdk/python/examples/full_lifecycle.py`, `bench/locomo/run.py`, `bench/longmemeval/run_with_llm.py`.

### Repository coverage

Every top-level tracked entry is classified below. “Included” specifies analytical scope, not exhaustive inspection or a correctness verdict. Initial trace means source text or targeted definitions/call sites were inspected; inventory-only paths are available but not yet inspected semantically. They are neither access gaps nor silent exclusions. Root administrative files are grouped explicitly. All entries belong to SRC-1; paths in the table are commit-relative anchors.

| Top-level entry | Classification and material paths / role | Initial inspection and limits |
| --- | --- | --- |
| `.claude` | Excluded: contributor harness configuration in `.claude/settings.json`. | Inventory only; no conclusion about the author's development-agent operation. |
| `.dockerignore`, `.gitattributes`, `.gitignore`, `.golangci.yml` | Excluded: packaging filters, repository and lint policy. | Inventory only; no packaging-completeness or lint-compliance conclusion. |
| `.github` | Included: CI, release, native-shell and fault-gate workflows under `.github/workflows/`. | Inventory only; no CI success inferred. |
| `.goreleaser.yaml` | Included: distribution configuration. | Inventory only; released binaries are not captured. |
| `CITATION.cff`, `CONTRIBUTING.md`, `LICENSE`, `THIRD_PARTY_NOTICES.md` | Excluded: attribution, contribution and licensing material. | Inventory only; no legal-compliance conclusion. |
| `README.md` | Included: intended use, deployment options and source-native claims. | Opening purpose and privacy qualifications inspected; release history not assessed. |
| `SECURITY.md`, `SECURITY_FAQ.md` | Included: security and disclosure contracts. | Inventory only; this boundary is not a security audit. |
| `Dockerfile`, `Makefile`, `docker-compose.sage-gui.yml` | Included: build and local deployment entry points. | Inventory only; no installation success inferred. |
| `api` | Included: `api/rest/server.go`, `api/rest/memory_handler.go`, middleware, federation, messaging, task and workflow handlers; OpenAPI and protobuf contracts. | Memory handler definitions, access/admission/retrieval entry points and post-commit projection handling inspected; other handlers remain available for tracing. |
| `bench` | Included: `bench/sage_bench.py`, `bench/locomo/run.py`, `bench/longmemeval/run.py`, `bench/longmemeval/run_with_llm.py`, judge qualification, reranker server and retained results. | LoCoMo seed/query/scoring code and LongMemEval answer/judge harness declaration inspected. Results, datasets and model accuracy not verified. |
| `buf.gen.yaml` | Included: generated API build configuration. | Inventory only. |
| `cmd` | Included: `cmd/sage-gui/main.go`, `node.go`, `mcp.go`, hooks, `nevercompact_recall.go`, configuration, recovery, snapshots and upgrades; `cmd/amid/main.go`, `cmd/sage-cli/main.go`, launcher, tray, update helper, embedding benchmark and fault fixture. | Main dispatch, server/store/MCP wiring, voter and cleanup call sites, hook capture and recall inspected. Auxiliary binaries are inventoried, not fully traced. |
| `deploy` | Included: compose deployments, init SQL, monitoring, backups, state-sync/fault and federation-acceptance harnesses. | Inventory only; actual clusters and service availability are outside frozen evidence. |
| `desktop` | Included: `desktop/sage-shell/src/main.rs`, `control.rs`, Tauri configuration and recovery UI. | Shell startup structures inspected; desktop operation not observed. |
| `docs` | Included: architecture, hooks, federation, lifecycle, write gate, cleanup, access control, compaction, deployment and upgrade contracts. | `docs/reference/concepts/memory-cleanup.md` inspected; other documents available for later claim checking. Brand images are non-mechanistic assets. |
| `e2e` | Included: browser scenarios for dashboard, identity, governance and federation. | Inventory only; tests not run. |
| `extension` | Included: `extension/chrome/background.js`, `sage-tools.js`, content/popup scripts and browser manifests. | Turn recall/store implementation, signed endpoints and prompt/tool definitions inspected; browser host behavior not observed. |
| `glama.json` | Included: MCP distribution metadata. | Inventory only. |
| `go.mod`, `go.sum` | Included: dependency boundary and pins. | Direct Go dependencies inspected; third-party service behavior not established by dependency declarations. |
| `installer` | Included: Linux, macOS and Windows installation and packaging scripts. | Inventory only; installer execution excluded. |
| `integrations` | Included: `integrations/levelup/sage_bridge.py` and `experiment_protocol.py`. | Bridge initialization, scoped committed recall and observation interface inspected; protocol inventoried. External Level Up agent code is not captured. |
| `internal` | Included: `internal/abci/app.go` and versioned lifecycle/state-sync paths; `internal/store/` canonical/serving persistence and projections; `internal/memory/` lifecycle/confidence; `internal/voter/`, `hunch/`, `contentvalidator/`; `internal/mcp/`; federation, governance, transaction signing, embedding/reranking, vault, transport, snapshots and sidecar management. | ABCI transition entry points, pending projection structures, MCP turn/inception/recall interfaces, voter loop/gate and federation manager/journal definitions inspected. Full protocol/security verification remains open; none of these shipped responsibilities is excluded. |
| `natter` | Included: optional connectivity service in `natter/main.go`, `host.go` and configuration. | `natter/README.md` inspected as design, not proof of its security claims; implementation inventoried. Hosted relay deployment is not captured. |
| `package-lock.json`, `package.json`, `playwright.config.js` | Included: JavaScript tooling and browser-test configuration. | Inventory only. |
| `papers` | Included: source-native research claims and experiment descriptions. | Inventory only; papers not read or results accepted. Their presence supplies no observed-run evidence. |
| `sage-memory` | Included: `sage-memory/SKILL.md`, shipped boot/write/recall/reflection and safety instructions. | Entire skill inspected as target doctrine, not instructions for this worker. |
| `scripts` | Included: static/UI/architecture contracts, native-shell quality gates, release checks, federation acceptance, organization setup and performance tooling. | Inventory only; no test or benchmark outcome inferred. |
| `sdk` | Included: Python synchronous/asynchronous clients, auth/models, examples and tests under `sdk/python/`. | `sdk/python/examples/full_lifecycle.py` submit/read/vote/corroborate/challenge/query path inspected; client implementations inventoried. |
| `server.json` | Included: MCP publication metadata. | Inventory only. |
| `test` | Included: integration, Byzantine and load/benchmark harnesses. | Inventory only; no execution evidence asserted. |
| `third_party` | Included: vendored `third_party/cometbft/` consensus, node, state and state-sync implementation and SAGE-specific tests. | Tree inventoried; consensus internals not yet inspected. Unlike uncaptured external dependencies, this code is available within SRC-1. |
| `web` | Included: dashboard handlers, memory import, boot/configuration, embedding repair, federation, operator authorization, cleanup and static clients in `web/static/`. | `web/cleanup.go` eligibility and durable signed challenge path inspected, plus runtime worker wiring in `cmd/sage-gui/node.go`; other UI and maintenance paths remain available. |

### External dependencies and evidence limits

External model clients decide whether to follow SAGE's returned instructions and whether recalled content changes an answer. Their implementation and live sessions are absent, preventing conclusions about universal automatic capture, instruction compliance or end-to-end answer improvement. SAGE's shipped hooks, prompts and connector code remain included. SRC-1, `sage-memory/SKILL.md`, `internal/mcp/tools.go`, `cmd/sage-gui/hook.go`.

Embedding and optional judging depend on configured model providers and sidecars; benchmark answer/judge models and benchmark datasets are also external inputs. Database engines, operating systems, browser/Tauri hosts and actual federation peers or relays provide additional dependencies. Their deployed configurations, model weights and service responses are not frozen here. Consequently this run can characterize source paths and declared defaults but cannot establish availability, measured model quality, production latency, network fault tolerance or operational privacy for a particular deployment. Dependency declarations and local configuration paths are evidence about integration, not captured executions. SRC-1, `go.mod`, `cmd/sage-gui/node.go`, `internal/voter/gate.go`, `bench/longmemeval/run_with_llm.py`, `natter/README.md`.

No external repositories, live pages, released binaries, experiments or newly generated traces enter this evidence boundary. Available but initially uninspected files at the same commit can be examined later under SRC-1. A different revision or external evidence source requires a changed evidence boundary rather than an unregistered addition.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/l33tdawg/sage` | e2e0242a421afbd356ed135d7d754a35b0ad5f14 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/sage-d3843de6d2dd/related-systems/l33tdawg--sage`. Complete tracked tree inventoried. Implementation: command dispatch and server/store wiring; MCP turn/inception and recall interfaces; REST memory handler interfaces and projection handling; ABCI transition definitions; voter loop/gate; canonical cleanup; session prefetch, capture and thread recall; browser turn implementation; Level Up bridge; SDK lifecycle example; LoCoMo seed/query/scoring; LongMemEval harness declaration; federation definitions and desktop startup structures. Doctrine/design: README opening, complete shipped memory skill, cleanup reference, gate/capture comments and Natter README opening. Listed scopes are initial inspection, not an allowlist. | [Entry points](https://github.com/l33tdawg/sage/blob/e2e0242a421afbd356ed135d7d754a35b0ad5f14/cmd/sage-gui/main.go); [node wiring](https://github.com/l33tdawg/sage/blob/e2e0242a421afbd356ed135d7d754a35b0ad5f14/cmd/sage-gui/node.go); [MCP](https://github.com/l33tdawg/sage/blob/e2e0242a421afbd356ed135d7d754a35b0ad5f14/internal/mcp/tools.go); [voter](https://github.com/l33tdawg/sage/blob/e2e0242a421afbd356ed135d7d754a35b0ad5f14/internal/voter/voter.go); [cleanup](https://github.com/l33tdawg/sage/blob/e2e0242a421afbd356ed135d7d754a35b0ad5f14/web/cleanup.go); [capture](https://github.com/l33tdawg/sage/blob/e2e0242a421afbd356ed135d7d754a35b0ad5f14/cmd/sage-gui/hook_precompact.go); [thread recall](https://github.com/l33tdawg/sage/blob/e2e0242a421afbd356ed135d7d754a35b0ad5f14/cmd/sage-gui/nevercompact_recall.go); [agent doctrine](https://github.com/l33tdawg/sage/blob/e2e0242a421afbd356ed135d7d754a35b0ad5f14/sage-memory/SKILL.md); [evaluation](https://github.com/l33tdawg/sage/blob/e2e0242a421afbd356ed135d7d754a35b0ad5f14/bench/locomo/run.py). Other local anchors appear above. | No repository access gap established. External hosts, provider/model artifacts, datasets and deployed services are not captured. No observed run or causal experiment established by this boundary inspection; no execution, performance, efficacy or production-security guarantee follows. Inventory-only material is available, not inaccessible. |
