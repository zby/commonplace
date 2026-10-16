---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Sparks knowledge-base runtime and shipped agent contract at commit 49abddc848ea55f78518bfbbbe04c3d37a5f2705."
run-id: AAS-2026-10-15-sparks-563865f8b26f-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "49abddc848ea55f78518bfbbbe04c3d37a5f2705"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/YogiRK/sparks
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/sparks-563865f8b26f/related-systems/YogiRK--sparks
  revision: 49abddc848ea55f78518bfbbbe04c3d37a5f2705
  sha256: null
---

# Sparks boundary

## Boundary and evidence

This run covers Sparks as the shipped knowledge-base system, including its executable maintenance tools and the instructions supplied to agents that write and later read the vault. The intended use is an agent-maintained personal knowledge base: humans capture sources, an external model-driven agent writes derived wiki content, and Sparks maintains mechanical state. It qualifies as a memory/knowledge/context-engineering system, not an enclosing model runtime. Its executable tool layer is deterministic; its shipped protocol serves semantic work performed by an external agent (SRC-1, `README.md`, `internal/contract/contract.md`, `internal/core/ingest.go`).

> **Knowledge base runtime for AI agents.** A single Go binary that maintains the mechanical integrity of a personal-scale knowledge base, so any agent — Claude Code, Codex CLI, Gemini CLI, or whatever ships next — can operate it through one CLI or one MCP server.
> --- `README.md`

The boundary kind is **whole-system**, relative to the Sparks product in this repository, not the enclosing agent harness. It includes initialization, the embedded contract and generated harness instruction files, inbox preparation and finalization, manifest persistence and reloading, wiki metadata and link processing, collection/index regeneration, tasks, health checks, structured retrieval, weekly-brief gathering, and the local viewer. The shipped CLI callers and MCP handlers are included, not treated as external applications. Agent-side instructions to deduplicate, revise, persist pages and logs, retrieve pages, and synthesize answers are also included as doctrine, not as proof that a model obeyed them (SRC-1, `cmd/sparks/main.go`, `internal/contract/contract.go`, `internal/core/agent.go`, `internal/mcp/serve.go`, `internal/contract/contract.md`).

> 1. `sparks query` for structured lookup (by title, tag, type, link graph).
> 2. Read the matching wiki pages.
> 3. Synthesize the answer with `[[wikilink]]` citations.
> --- `internal/contract/contract.md`

Initial tracing follows `cmd/sparks/main.go` to the ingest command and core prepare/finalize functions; finalization archives and clears the inbox, scans persisted files and optionally invokes Git. Scanning updates file/frontmatter records and rebuilds link edges. MCP handlers reopen the vault and manifest; query consumes manifest page/link state, brief combines retained files and manifest signals, and the viewer reads page files and manifest metadata. This establishes the shipped persistence-to-later-consumption paths without executing them (SRC-1, `cmd/sparks/ingest.go`, `internal/core/ingest.go`, `internal/core/ingest_finalize.go`, `internal/core/scan.go`, `internal/mcp/serve.go`, `internal/manifest/queries.go`, `internal/core/brief.go`, `internal/view/server.go`).

> 	// Rescan so the manifest reflects the archived files + cleared inbox.
> 	if _, err := Scan(v, db); err != nil {
> 		return result, fmt.Errorf("post-finalize scan: %w", err)
> 	}
> --- `internal/core/ingest_finalize.go`

The frozen evidence is the acquired Git repository at **49abddc848ea55f78518bfbbbe04c3d37a5f2705**. The applicability cutoff is **2026-10-15**, the supplied run date; it is not a claim about the commit's date. Overall evidence is **code-grounded**. Source text, embedded instructions, documentation and test definitions are available. No target code, tests, examples, model calls or services were run. Authored test assertions are implementation evidence about intended checks, not observed passing results. Documentation describing personal-vault production use is reported operation only (SRC-1, `cmd/sparks/e2e_test.go`, `README.md`).

### Repository coverage

The table accounts for every top-level tracked entry. All paths refer to SRC-1. “Included” fixes functional scope; it does not assert exhaustive line-by-line review. Material entry points, persistence/consumption paths and shipped instructions were inspected as described above. Supporting helpers and additional test cases remain available for deeper inspection; they are not access gaps.

| Top-level entry | Treatment and material paths | Role and limits |
|---|---|---|
| `.github/` | Included: `.github/workflows/ci.yml`; `.github/workflows/release.yml` available but not initially inspected | CI test/build and contract-sync definition inspected; release packaging details not assessed. No observed CI result. |
| `.gitignore` | Excluded: repository housekeeping | No conclusions about ignored-file packaging or operator Git hygiene. |
| `.goreleaser.yaml` | Excluded: release packaging | No conclusions about distributed binary provenance or platform release correctness. |
| `CHANGELOG.md` | Included: scoped release/feature search | Attributed historical claims, not independent execution evidence. |
| `GETTING_STARTED.md` | Included: full onboarding and daily-flow instructions | External harness setup, persistence and later query/brief consumption. |
| `LICENSE` | Excluded: licensing | No legal or license-compliance assessment. |
| `Makefile` | Included: build/test targets and contract-copy/sync checks | Development and embedded-instruction maintenance; targets not executed. |
| `README.md` | Included: full overview, architecture and usage | Intended use, dependencies, interfaces and reported operation. |
| `TODOS.md` | Included: scoped headings and mechanism search | Proposed work distinguished from shipped behavior; no roadmap delivery claim. |
| `cmd/` | Included: `cmd/sparks/main.go`, `ingest.go`, `collections.go`; scoped inspection of `init.go`, `describe.go`, `serve.go`, `view.go`, `query.go`, `brief.go`, `fmt.go`, `lint.go`, `index.go`; `arch_test.go` and `e2e_test.go` | Shipped CLI driver, generation and retrieval adapters; architecture checks located and ingest/tasks/brief test definitions inspected. Other command adapters remain available. Tests were not run. |
| `docs/` | Excluded: `docs/view.png` | Viewer illustration; no visual-fidelity conclusion. Viewer implementation remains included. |
| `go.mod` | Included: dependency declaration | Go/tooling and third-party library requirements, not dependency internals or security verification. |
| `go.sum` | Excluded: dependency checksum list | No dependency integrity or supply-chain audit. |
| `internal/` | Included: `core/{init,agent,ingest,ingest_finalize,scan,brief,index,tasks,affected}.go`; `contract/{contract.go,contract.md}`; `mcp/serve.go`; `manifest/{manifest,queries,ingests,frontmatter,wikilinks,migrations}.go` and SQL migration; `inbox/{inbox,classify,archive}.go`; `collections/collections.go` and extractors; `frontmatter/frontmatter.go`; `lint/lint.go`; `graph/{links,resolve}.go`; `git/git.go`; `vault/{init,vault}.go`; `view/{server,render,sidecar}.go`, templates/static assets; package tests | Full functional scope: construction, admission, persistence, maintenance and later consumption. Full reads cover central ingest/scan/brief, contract, MCP, collection dispatcher, lint and viewer server; supporting symbols/calls were searched. Helper details, templates and remaining tests are not all initially read, but no shipped material responsibility is excluded. |
| `sparks-contracts.md` | Included: repository-readable contract copy | Canonical embedded instructions were read at `internal/contract/contract.md`; `internal/contract/contract.go` and `Makefile` establish the copy/sync relationship. |
| `sparks-insight.md` | Included: scoped thesis/origin search | Declared design rationale and attributed dogfooding, not measured benefit. |
| `sparks-spec.md` | Included: scoped structure, ingest/query and integration search | Design intent; executable paths take precedence for implementation claims. |

External dependencies include the agent harness and model provider, user-supplied vault content and filesystem, optional system Git/configuration, the browser for viewing, and libraries declared in `go.mod`. Harness scheduling, model inference, context loading and semantic writing quality are outside this source boundary: no conclusions about their implementation, compliance or efficacy follow. The maintainer's actual vault and agent-session traces are not supplied; this prevents confirmation of end-to-end semantic retention, answer quality, token savings or reliability in production. Linked external articles and dependency repositories were not acquired and cannot supply evidence here (SRC-1, `GETTING_STARTED.md`, `internal/git/git.go`, `go.mod`).

No material shipped source was found inaccessible. Available but uninspected support files are an initial-inspection limit, not an unavailable-source claim. The only frozen source is the acquired repository; no live page, other revision or external execution artifact is incorporated.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/YogiRK/sparks` | 49abddc848ea55f78518bfbbbe04c3d37a5f2705 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/sparks-563865f8b26f/related-systems/YogiRK--sparks`. Implementation: tracked tree, CLI registrations and ingest/collection callers; core initialization, instruction writing, prepare/finalize, scan and brief; MCP tool handlers; manifest query; collection dispatcher; lint and viewer server; scoped helper/test searches and ingest/tasks/brief CLI test definitions. Doctrine/design: full `README.md`, `GETTING_STARTED.md`, `internal/contract/contract.md`, embedding/sync code; scoped `sparks-spec.md`, `sparks-insight.md`, `TODOS.md`, `CHANGELOG.md`. Reported operation: README personal-vault use and scoped origin/release claims. | Implementation: [entry point](https://github.com/YogiRK/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/cmd/sparks/main.go), [finalize](https://github.com/YogiRK/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/ingest_finalize.go), [MCP consumers](https://github.com/YogiRK/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/mcp/serve.go). Doctrine/design: [embedded contract](https://github.com/YogiRK/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/contract/contract.md). Reported operation: [README](https://github.com/YogiRK/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/README.md). | No checkout access gap. External harness/model implementation, personal vault, run traces and measured experiments are absent; prevents observed-run or causal claims and confirmation of semantic performance. Initial path list is not an allowlist; other files at this commit remain available. |
