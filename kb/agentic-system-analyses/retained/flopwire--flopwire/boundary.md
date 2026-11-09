---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Flopwire shared transcript history and messaging at frozen commit 057a4b87603cc878e81d9eb49298ddc4eb9eeb23"
run-id: AAS-2026-10-20-flopwire-184bd013bba1-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "057a4b87603cc878e81d9eb49298ddc4eb9eeb23"
analysis-cutoff: "2026-10-20"
evidence-tier: code-grounded
source:
  identity: https://github.com/flopwire/flopwire
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/flopwire-184bd013bba1/related-systems/flopwire--flopwire
  revision: "057a4b87603cc878e81d9eb49298ddc4eb9eeb23"
  sha256: null
---

# Flopwire boundary

## Boundary and evidence

Flopwire is in scope as a memory/knowledge/context-engineering system: it retains agent conversation history, serves that history back through retrieval tools, and supplies messages and handling instructions to agent contexts. Its intended use is recovery of prior work and coordination across sessions, harnesses, devices and people. The boundary is the whole shipped Flopwire system, including its device daemon, optional team server, CLI, MCP server, harness plugins, standing instructions, retrieval guidance, administrative console and evaluation drivers. It is not limited to a storage or search API. SRC-1: `README.md`, `cmd/flopwire/main.go`, `cmd/flopwire/mcp.go`, `plugins/codex/flopwire/skills/messaging/SKILL.md`, `plugins/opencode/flopwire.js`.

The classification rests on both retained content and a shipped consumption procedure. The Codex and Claude Code skills explicitly direct models to recover earlier evidence:

> Use `flopwire_search` for topic or decision history, `flopwire_grep` for exact text, `flopwire_sessions` for session discovery, and the commit workflow below for change provenance. Use `flopwire_read` on relevant evidence; an outline is optional session navigation and omits intervening assistant answers. Check presence only when the task needs contact or live status.
> --- `plugins/codex/flopwire/skills/messaging/SKILL.md`

The local store retains extracted conversation content independently of the continued existence of the original transcript. Its declared storage contract is:

> // The index is derived data. It is rebuildable from the harness files, holds
> // the owner's own data unredacted, and keeps the extracted text of every row
> // (zstd-compressed) so search survives a harness deleting its transcript.
> --- `internal/localindex/store.go`

Initial source tracing followed the shipped `main` command dispatch into `agent`, `serve`, retrieval, `mcp`, `hook`, `setup`, `probe` and `bench`. On the production side, the device agent discovers harness sources, applies collection and upload policy, extracts transcript messages into a local sink, and notifies synchronization. The server constructor wires chunk ingestion, the parse queue, commit-evidence projection, retrieval and the message bus, together with deletion, credential and chunk maintenance workers. On the consumption side, CLI and MCP retrieval choose a local read-only index or the enrolled server; MCP calls dispatch into the shared retrieval renderer or bus handlers. These are shipped responsibilities within this boundary. SRC-1: `cmd/flopwire/main.go`, `cmd/flopwire/agent.go`, `internal/agent/agent.go`, `internal/agent/index.go`, `internal/agent/store.go`, `internal/agent/policy.go`, `internal/ingest/queue.go`, `cmd/flopwire/retrieve.go`, `cmd/flopwire/mcp.go`.

The inspected executable extraction path creates the local sink and passes it to transcript extraction:

> sink := &cwdSink{Sink: a.store.NewSink(ctx, st.ID, gen), reads: readSightings{agent: t.src.Agent}}
> sink.BatchSize = a.cfg.BatchRows
> --- `internal/agent/index.go`

> result, err := transcript.Extract(ctx, t.parser, transcript.Input{Source: &src, R: rec, Size: id.Size}, cur, sink)
> --- `internal/agent/index.go`

The reuse loop also includes shipped model-facing instructions and delivery adapters. Codex and Claude Code hook configurations invoke Flopwire on session and tool events. The device bus tracks instruction delivery and renewal after context changes. The opencode plugin supplies tools and inserts guidance into the model prompt. This makes consumption part of the shipped artifact even though the enclosing model loop belongs to an external harness. SRC-1: `plugins/codex/flopwire/hooks/hooks.json`, `plugins/claude-code/flopwire/hooks/hooks.json`, `internal/devicebus/instruct.go`, `internal/busrender/busrender.go`, `plugins/opencode/flopwire.js`.

> //   - Puts Flopwire's standing instruction and tool guidance into every
> //     model call's system prompt (experimental.chat.system.transform).
> --- `plugins/opencode/flopwire.js`

Evaluation drivers are included. `flopwire probe` starts external harness sessions to check delivery; the workflow qualification script drives real model turns; acceptance scripts exercise indexing, freshness, parser parity and retrieval. Their existence is implementation evidence about evaluation design, not an observed result of this analysis. In particular, model calls made by evaluators do not establish that routine indexing or retrieval requires model inference. SRC-1: `cmd/flopwire/probe.go`, `scripts/qualify-agent-workflow.py`, `scripts/nightly-codex.py`, `scripts/acceptance.sh`, `testdata/oracle/README.md`, `.github/workflows/validation-nightly.yml`.

### Repository coverage

Every top-level tracked entry is classified below. Included means part of the functional or supporting source boundary, not a claim that every file has already been read. Initial inspection established the material production, maintenance, admission and consumption paths above. Listed but unread files remain available for later source inspection at the same commit; they are neither unavailable evidence nor access gaps. Each row refers to SRC-1; code paths are implementation evidence, and documentation or prompt instructions state contracts or intended use.

| Top-level tracked entry | Classification | Material paths, role and initial inspection | Exclusion or inspection limit |
|---|---|---|---|
| `.agents` | Included | `.agents/plugins/marketplace.json`: Codex plugin distribution; tracked tree inspected. | Manifest contents not yet inspected; no installation-success claim. |
| `.claude-plugin` | Included | `.claude-plugin/marketplace.json`: Claude plugin distribution; tracked tree inspected. | Manifest contents not yet inspected. |
| `.github` | Included | `.github/workflows/validation-nightly.yml` inspected; CI, E2E, performance and release workflow paths enumerated. | Workflow source establishes planned checks, not their successful execution. |
| `.dockerignore`, `.gitignore` | Included | Build and source packaging controls; tracked entries enumerated. | Contents not yet inspected; no packaging-completeness conclusion. |
| `.env.example` | Included | Deployment configuration template, alongside inspected `compose.yaml`. | Template contents not yet inspected. |
| `.goreleaser.yaml`, `.release-please-manifest.json`, `release-please-config.json` | Included | Binary release and version metadata; tracked entries enumerated. | Release configuration contents not yet inspected; no released-binary equivalence claim. |
| `AGENTS.md`, `CLAUDE.md` | Included | Repository development instructions; entries enumerated, not adopted as analysis instructions. | Contents not yet inspected; no development-process compliance claim. |
| `CHANGELOG.md` | Included | Source-native release history. | Not yet inspected; no historical outcome claim. |
| `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md` | Excluded | Community and contribution administration. | No conclusions about contributor governance or practice. |
| `LICENSE`, `NOTICE` | Excluded | Legal notices. | No licensing or legal-compliance assessment. |
| `README.md` | Included | Product scope, agent discovery and deployment overview inspected through documentation index. | Descriptions remain attributed intent unless traced in code. |
| `SECURITY.md` | Included | Security contract linked from inspected README; available, not yet inspected. | No complete threat-model or security-audit conclusion. |
| `Dockerfile`, `Dockerfile.release`, `Makefile` | Included | Build and server packaging entry points, enumerated. | Contents not yet inspected; no reproducible-build claim. |
| `compose.yaml`, `compose.dev.yaml` | Included | Team deployment; `compose.yaml` inspected for Postgres, object storage and Flopwire wiring. | Development overlay not yet inspected; no running-deployment result. |
| `deploy` | Included | `deploy/launchd/com.flopwire.agent.plist`, `deploy/nginx.conf.example`: daemon startup and reverse proxy deployment. | Paths enumerated; configuration contents not yet inspected. |
| `docs` | Included | `docs/architecture.md`, opening operations in `docs/runbook.md` inspected; harness, path-rule, recovery, diagnostics, search and probe documents enumerated. | Remaining operational instructions and performance captures not yet inspected; no measured performance claim. |
| `go.mod`, `go.sum` | Included | Dependency identities and build contract; enumerated. | Dependency implementation and supply-chain behavior not assessed. |
| `cmd` | Included | `cmd/flopwire/main.go`, `agent.go`, `retrieve.go`, `mcp.go`, `mcp_runtime.go`, `probe.go` inspected in bounded ranges; setup, hooks, backup, import, admission, bus and benchmark entry paths enumerated. | Boundary tracing is not an exhaustive handler audit. |
| `internal` | Included | Inspected `agent/{agent,index,store,policy,reads}.go`, `localindex/store.go`, `retrieval/local/local.go`, `devicesync/syncer.go`, `ingest/queue.go`, `api/api.go`, `devicebus/instruct.go`, `busrender/busrender.go`, `backup/backup.go`. Tree also covers transcript parsers, ingest/admission, redaction, path policy, provenance, server store, bus, client, recovery, cloud adapters and embedded web assets. | Includes all material packages; uninspected implementations remain to be traced for mechanism-specific conclusions. No target code or tests executed. |
| `landing` | Included | `landing/install.sh` inspected for installation/update entry; `landing/assets/brand-mark.svg` is imported by inspected console source. Other assets, preview pages and site worker enumerated. | Promotional text and previews cannot establish runtime behavior; remaining site code not yet inspected. |
| `migrations` | Included | `migrations/001_schema.sql` through `019_text_statistics.sql` and `embed.go` enumerated: durable storage, admission/policy, redaction and bus evolution. | SQL contents not yet inspected; no full schema or upgrade-correctness conclusion. |
| `notes` | Included | Source-native designs, experiments, evaluation reports and maintenance rationale enumerated. | Contents not yet inspected; no reported-operation or experimental outcome adopted from them. |
| `plugins` | Included | Codex and Claude Code messaging skills and hook manifests inspected; `plugins/opencode/flopwire.js` inspected for tool, prompt and delivery integration; hook shims and embedding paths enumerated. | Host-side implementation is external; no successful installation or actual delivery inferred from adapters alone. |
| `scripts` | Included | `scripts/{acceptance.sh,qualify-agent-workflow.py,nightly-codex.py}` inspected in bounded ranges; oracle, E2E, performance, release and web-build checks enumerated. | Scripts are evaluation and maintenance procedures, not fresh run evidence. |
| `testdata` | Included | `testdata/oracle/README.md` inspected; oracle expected outputs, SQL seed, redaction, sanitized transcript and acceptance fixture paths enumerated. | Synthetic fixtures do not establish deployment performance or real user outcomes. |
| `third_party` | Excluded | Enumerated license and notice directories for attributed upstream work. | No independent characterization or legal audit of upstream systems. Bundled Flopwire implementation remains included under its actual code paths. |
| `tools` | Included | `tools/{avdump,ci-shard,fad-dump}` enumerated: parser/oracle inspection and CI support; oracle README identifies the FAD adapter's role. | Tool implementations not yet inspected; no oracle execution or independent upstream analysis. |
| `web` | Included | `web/src/App.tsx` inspected for health, people, policy, archive, audit and messaging routes; API, messaging, tests and build files enumerated. | Remaining client handlers not yet inspected; no browser execution result. |

### Frozen evidence and external limits

The source is exactly the acquired Git object above, unchanged. The checkout HEAD was verified as `057a4b87603cc878e81d9eb49298ddc4eb9eeb23`. The analysis cutoff is 2026-10-20 and all conclusions apply only to that revision. No live website, later release, other repository, external execution trace or fresh experiment is registered. The overall tier is code-grounded because shipped entry points, extraction, backend selection, server wiring and context adapters were inspected as source text.

External dependencies include the enclosing Claude Code, Codex, Devin and opencode harnesses and their model services, OS transcript/process/hook facilities, SQLite, and optional Postgres plus S3-compatible object storage. The supplied repository includes Flopwire's adapters, drivers and deployment wiring; it does not include the complete implementations or live configurations of those external services. Their model scheduling, permissions, context retention and compliance with retrieved guidance cannot be attributed to Flopwire. The dependency boundary prevents conclusions about end-to-end behavior across uninspected harness versions or deployments. SRC-1: `compose.yaml`, `internal/agent/agent.go`, `plugins/opencode/flopwire.js`, `cmd/flopwire/probe.go`.

No material shipped Flopwire path was inaccessible. No target executable, test, example, model provider or service was run. That absence prevents claims of observed delivery, retrieval quality, performance, reliability or causal improvement. Available but unread source is recorded above as an inspection limit, not an access failure. Source-native evaluation reports can be inspected later under SRC-1 with their conditions preserved; their existence alone is not evidence of a successful run.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/flopwire/flopwire` | 057a4b87603cc878e81d9eb49298ddc4eb9eeb23 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/flopwire-184bd013bba1/related-systems/flopwire--flopwire`. Implementation: tracked root/tree inventory, command dispatch, server wiring, local extraction/persistence, retrieval backend selection, MCP dispatch, device instruction delivery, plugin integration, backup and evaluation-driver source ranges named above. Doctrine/design: README, architecture, runbook opening, messaging skills, standing instruction, oracle contract and evaluator comments. | Implementation: [command and server entry](https://github.com/flopwire/flopwire/blob/057a4b87603cc878e81d9eb49298ddc4eb9eeb23/cmd/flopwire/main.go), [extraction](https://github.com/flopwire/flopwire/blob/057a4b87603cc878e81d9eb49298ddc4eb9eeb23/internal/agent/index.go), [retrieval](https://github.com/flopwire/flopwire/blob/057a4b87603cc878e81d9eb49298ddc4eb9eeb23/cmd/flopwire/retrieve.go), [opencode integration](https://github.com/flopwire/flopwire/blob/057a4b87603cc878e81d9eb49298ddc4eb9eeb23/plugins/opencode/flopwire.js). Doctrine/design: [architecture](https://github.com/flopwire/flopwire/blob/057a4b87603cc878e81d9eb49298ddc4eb9eeb23/docs/architecture.md), [retrieval skill](https://github.com/flopwire/flopwire/blob/057a4b87603cc878e81d9eb49298ddc4eb9eeb23/plugins/codex/flopwire/skills/messaging/SKILL.md), [standing instruction](https://github.com/flopwire/flopwire/blob/057a4b87603cc878e81d9eb49298ddc4eb9eeb23/internal/busrender/busrender.go). | No repository access gap. External harnesses and services are not frozen here, preventing claims about their internal operation. No target execution or independent runtime observations; evaluation code supports procedure descriptions only. Unread available files and deliberate exclusions are distinguished in the coverage table. |
