---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "deja-vu's shipped cross-agent history, retained-note and context-delivery system at commit 4c08fb26ad8a8b8e656a120f06ca4175a7078148."
run-id: AAS-2026-10-14-deja-vu-22137d4d39a5-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "4c08fb26ad8a8b8e656a120f06ca4175a7078148"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/vshulcz/deja-vu
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/deja-vu-22137d4d39a5/related-systems/vshulcz--deja-vu
  revision: "4c08fb26ad8a8b8e656a120f06ca4175a7078148"
  sha256: null
---

# deja-vu boundary

## Boundary and evidence

This run analyses deja-vu as the shipped system that turns coding-agent history and explicit decisions into retrievable history and context for later agent sessions. Its intended use is cross-session recall, recovery after compaction, finding prior fixes and decisions, and maintaining standing rules across supported hosts. The target class is **memory/knowledge/context-engineering system**, not an enclosing agent runtime. The boundary kind is **whole-system**: the binary, its internal state machinery, shipped consumers and installers, prompts and maintenance instructions, and evaluators belong to the target. External hosts' own generation and action loops do not.

The classification is grounded in a shipped producer-to-consumer trace, rather than only a product description:

- The dispatcher exposes `remember`, `promote`, `rules`, `forget`, `sync`, `recall`, `ctx`, `mcp`, and the context, prompt, tool and compaction hooks (SRC-1, `cmd/deja/main.go`). `remember` writes a note through `sources.AppendNoteTagged`, then updates the search index; `promote` appends sourced lifecycle-marked notes and requests indexing (SRC-1, `cmd/deja/remember.go`, `cmd/deja/promote.go`).
- The notes source both persists JSONL and reloads it as sessions. The source registry defines discovery, full parsing and incremental parsing; the index admits these sessions into retained search state and refreshes that state (SRC-1, `internal/sources/notes.go`, `internal/sources/registry.go`, `internal/index/ingest.go`). The persistence and reload are real implementation paths:

> return json.NewEncoder(f).Encode(note{TS: now.UTC().Format(time.RFC3339Nano), Project: project, Text: text, Tags: NormalizeTags(tags)})
> --- `internal/sources/notes.go`

> func ParseNotesFile(path string) ([]model.Session, error) {
> 	return ParseNotesFileFromOffset(path, 0)
> }
> --- `internal/sources/notes.go`

- The MCP `remember` branch uses the same writer, journals the write, and attempts nonblocking indexing. Recall uses the index and serves bounded answers. The startup digest loads recent project sessions and promoted conventions under the automatic-activation policy, then renders them for injection (SRC-1, `cmd/deja/mcp.go`, `cmd/deja/hook_context.go`).
- A shipped consumer is inside the repository: the pi extension calls the binary's context and prompt hooks and returns their output as a model-facing message. It also adds history beside tool results, captures compaction state, and closes the live session stamp. These are target responsibilities, not excluded merely because they run in another host (SRC-1, `extensions/pi/index.ts`). The context-delivery return is explicit:

> return { message: { customType: "deja-recall", content: digest, display: false } };
> --- `extensions/pi/index.ts`

- Compaction capture extracts structured state and stores it through `index.PutCompaction`; recovery retrieves it, checks repository freshness, renders a bounded packet, and records delivery only after writing the output (SRC-1, `cmd/deja/hook_compaction.go`). Shipped agent instructions ask the consuming model to search before editing and to store settled decisions; maintenance instructions require user selection before copying candidate standing rules across hosts (SRC-1, `skills/deja-search/SKILL.md`, `GEMINI.md`, `cmd/deja/rules.go`).

The system therefore qualifies even when its lexical retrieval performs no generation call: its shipped context-delivery and instruction paths serve model-dependent agent work. Optional embedding requests are also present; they do not make deja-vu the host's inference controller (SRC-1, `internal/embed/client.go`).

### Functional inclusions and exclusions

Included are transcript/store discovery and parsing; explicit and promoted notes; derived indexes and sidecars; redaction, exclusion and activation policy; lexical and optional semantic retrieval; CLI, MCP and interactive readers; automatic context delivery and its session ledgers; compaction recovery; rules maintenance; forgetting, sync, export, handoff and restoration; generated and packaged host integrations; and source-native tests and evaluation drivers. The shipped wrappers and extension consumers remain included. Their hosts' scheduling, model inference, execution of suggested actions and original transcript production remain external.

The initially traced loop covers writing, reload/index admission, refresh, retrieval, model-context delivery and compaction recapture. It does not establish identical behavior in every supported host. The frozen repository makes the remaining implementations available to later jobs; an uninspected file is not an access gap. The source register's initial scope is not a path allowlist.

External dependencies include compatible host event APIs and readable host stores; the `sqlite3` command for database-backed parsers; system Git for repository-state and attribution work; SSH/SCP and a remote deja binary for cross-machine sync; and an embedding endpoint when semantic functionality is used (SRC-1, `docs/ARCHITECTURE.md`, `cmd/deja/install_pi.go`, `cmd/deja/sync.go`, `internal/embed/client.go`). The Go module declares Go 1.25 and no module dependencies, while the npm launcher resolves a platform binary package (SRC-1, `go.mod`, `npm/bin/deja`). None of those services, host implementations or installed binary distributions is separately frozen here. This prevents claims about their actual availability, host compatibility or production execution in this run. The repository can support what deja attempts, handles or declares, not what an excluded host or service actually does.

### Top-level coverage

The tracked tree was enumerated at the reviewed commit. Every top-level tracked file or directory is classified below. “Included” means within the functional/evidence boundary, not exhaustively read. Initial inspection names concrete paths where done; explicitly uninspected material remains available. All repository-path references in this table are SRC-1.

| Top-level tracked entries | Disposition and material paths/role | Inspection or exclusion limit |
|---|---|---|
| `cmd/` | Included: `cmd/deja/main.go`, `remember.go`, `promote.go`, `mcp.go`, `hook_context.go`, `hook_compaction.go`, `rules.go`, `sync.go`, `install_pi.go`; other install/hook implementations, resume/writeback, handoff, forgetting, CLI/TUI readers, doctor, stats and bench paths | Named entry points and loop slices inspected; other implementations and tests not yet inspected. Includes generated host consumers, not just public command APIs. |
| `internal/` | Included: `internal/sources/registry.go`, `notes.go` and host parsers; `internal/index/ingest.go`, retrieval, storage, sync, compaction and derived sidecars; `internal/search/`, `digest/`, `policy/`, `redact/`, `usage/`, `embed/`; model, normalization, terminal and atomic-file support, benchmark and test packages | Registry, notes, refresh and embedding-client slices inspected; architecture locates the remaining responsibilities. Most parser variants, supporting packages and tests not yet inspected. |
| `extensions/` | Included: `extensions/pi/index.ts` and `lib.mjs`; opencode, dsh, openclaw, hermes, kimi, grok and zed entry points, manifests, skills and tests | README and complete pi entry point inspected; other host variants not yet inspected. They shell out to or integrate with the same binary and retained state. |
| `skills/` | Included: `skills/deja-search/SKILL.md`, model-use and standing-rule maintenance instructions | Complete instruction inspected as target doctrine, not instructions to this worker. |
| `GEMINI.md` | Included: always-loaded extension guidance | Complete file inspected as target doctrine. |
| `claude-plugin/` | Included: plugin manifests, `hooks/deja.sh`, `hooks/hooks.json`, `mcp/deja-mcp.sh`, `commands/deja.md`, `skills/deja-history/SKILL.md` | Portable manifest and failure-hook mapping inspected; wrapper scripts and other prompts not yet inspected. |
| `codex-plugin/`, `codebuddy-plugin/`, `devin-plugin/` | Included: each plugin's manifest, MCP/hook launcher, hook configuration where shipped, and `skills/deja-history/SKILL.md` | Tree inspected; contents not yet inspected. Includes shipped caller and prompt variants. |
| `docs/` | Included: `docs/ARCHITECTURE.md`, `INTEGRATING.md`, `SECURITY-MODEL.md`, `compaction.md`, `json-output.md`, host registry, operating guides and benchmark artifacts | Architecture inspected completely. Other operational documents and retained benchmark data not yet inspected. Deliberately exclude cross-system comparison pages from this run's characterization evidence; this prevents comparative claims, not tracing the target's loop. |
| `scripts/` | Included: `scripts/longmemeval/main.go`, locomo, benchmark drivers, agent-smoke/e2e, mockmodel, corpus generation, release and registry tooling | LongMemEval setup and production-query/evaluation path inspected. Other drivers not yet inspected. Cross-system `scripts/day0compare/` deliberately excluded from characterization evidence; no comparative performance conclusion follows. No script executed. |
| `tools/` | Included: `tools/bench492/` corpus generator, benchmark runner and instructions; Unicode table generators | Tree inspected only. Evaluator results and generator correctness are not established by their presence. |
| `fixtures/` | Included: `fixtures/registry/` host-format examples and `fixtures/synthetic/` transcript/compaction fixtures | Tree inspected only. Synthetic fixtures are not observed production sessions. |
| `npm/` | Included: `npm/bin/deja`, package metadata and installation guidance | Complete binary launcher inspected; metadata and README not yet inspected. |
| `packaging/` | Included: MCP bundle, Scoop and Winget descriptors and packaging guidance | Tree inspected only; shipped-artifact correspondence and installation success not established. |
| `gemini-extension.json`, `kimi.plugin.json`, `plugin.json`, `mcp.json`, `server.json`, `package.json`, `glama.json` | Included: root distribution, host discovery and MCP manifests | Paths enumerated; integration roles documented by `extensions/README.md`; contents not yet inspected. |
| `.agents/`, `.claude-plugin/` | Included: `.agents/plugins/marketplace.json`, `.claude-plugin/marketplace.json` distribution discovery | Tree inspected only; external registry acceptance not established. |
| `.claude/` | Included: `.claude/commands/harness.md`, repository maintenance procedure | Tree inspected only; maintenance instructions not yet assessed. |
| `go.mod` | Included: module and toolchain contract | Complete file inspected. |
| `changelog_embed.go`, `dsh_embed.go` | Included: embedded changelog and host-integration resources | Tree inspected only; embedding implementation not yet assessed. |
| `README.md`, `ROADMAP.md`, `CHANGELOG.md`, `SECURITY.md`, `CONTRIBUTING.md`, `llms-install.md` | Included: target intent, development, security and installation doctrine | Not yet inspected; no additional claims taken from these documents. |
| `install.sh`, `Dockerfile`, `Makefile`, `.goreleaser.yaml` | Included: build, binary installation and release/container paths | Not yet inspected; no claim that a release was built or installed successfully. |
| `.github/` | Excluded from functional-loop assessment: workflow, issue-template, ownership and release-automation metadata | Deliberate exclusion prevents CI, release-pipeline and supply-chain assurance conclusions. Does not exclude shipped benchmark code or runtime consumers. |
| `.dockerignore`, `.gitattributes`, `.gitignore`, `.golangci.yml`, `.plugin-scanner.toml` | Excluded from functional-loop assessment: repository/build/lint/scanner settings | Deliberate exclusion prevents configuration-completeness or scanner-effectiveness conclusions. |
| `assets/` | Excluded: product art, logos and demonstration media | Deliberate exclusion prevents treating demonstrations as observed execution evidence. |
| `LICENSE` | Excluded: license text | Deliberate exclusion prevents legal/licensing assessment. |

### Frozen revision and time limit

The sole frozen source is `https://github.com/vshulcz/deja-vu` at full commit `4c08fb26ad8a8b8e656a120f06ca4175a7078148`. The checkout's HEAD matched the acquisition pin and its short status was empty when inspected. The acquired Git source object is reproduced unchanged in frontmatter. The analysis cutoff is the supplied run date, **2026-10-14**; applicability is to this commit, not later repository or host changes.

The overall evidence tier is **code-grounded**. Executable source supports implementation claims; shipped prompts and architecture supply doctrine/design. Source comments reporting earlier measurements are attributed reported operation, not observations performed by this run. No target tests, examples, agents, model providers or services were executed. No independent execution trace or causal experiment is frozen. Consequently this boundary supports source-native mechanism analysis, not validated effectiveness, latency, retention durability under real failures, universal host delivery or user compliance.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/vshulcz/deja-vu` | 4c08fb26ad8a8b8e656a120f06ca4175a7078148 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/deja-vu-22137d4d39a5/related-systems/vshulcz--deja-vu`. Tracked tree enumerated. Implementation: slices of `cmd/deja/main.go`, `remember.go`, `promote.go`, `mcp.go`, `hook_context.go`, `hook_compaction.go`, `rules.go`, `sync.go`, `install_pi.go`; `internal/sources/notes.go`, `registry.go`, `internal/index/ingest.go`; complete `internal/embed/client.go`, `extensions/pi/index.ts`, `npm/bin/deja`, `go.mod`; LongMemEval driver setup and `runQuestion` path. Doctrine/design: complete `docs/ARCHITECTURE.md`, `extensions/README.md`, `skills/deja-search/SKILL.md`, `GEMINI.md`; Claude portable manifest and failure-hook configuration. Reported operation: source comments and architecture's attributed historical observations only. | Implementation: [dispatcher](https://github.com/vshulcz/deja-vu/blob/4c08fb26ad8a8b8e656a120f06ca4175a7078148/cmd/deja/main.go), [notes](https://github.com/vshulcz/deja-vu/blob/4c08fb26ad8a8b8e656a120f06ca4175a7078148/internal/sources/notes.go), [index admission/refresh](https://github.com/vshulcz/deja-vu/blob/4c08fb26ad8a8b8e656a120f06ca4175a7078148/internal/index/ingest.go), [consumer](https://github.com/vshulcz/deja-vu/blob/4c08fb26ad8a8b8e656a120f06ca4175a7078148/extensions/pi/index.ts), [recovery](https://github.com/vshulcz/deja-vu/blob/4c08fb26ad8a8b8e656a120f06ca4175a7078148/cmd/deja/hook_compaction.go), [evaluator](https://github.com/vshulcz/deja-vu/blob/4c08fb26ad8a8b8e656a120f06ca4175a7078148/scripts/longmemeval/main.go). Doctrine/design and reported operation: [architecture](https://github.com/vshulcz/deja-vu/blob/4c08fb26ad8a8b8e656a120f06ca4175a7078148/docs/ARCHITECTURE.md), [agent/maintenance instructions](https://github.com/vshulcz/deja-vu/blob/4c08fb26ad8a8b8e656a120f06ca4175a7078148/skills/deja-search/SKILL.md). | No access gap in the frozen checkout. Host runtimes, user stores, deployed binaries, external endpoints and independently inspectable runs are not frozen; no real-host effectiveness or causal claim. Available but uninspected variants are identified above, not represented as unavailable. Reported measurements support attribution only. |
