---
description: "Sparks review: Go runtime for Karpathy-style LLM wikis with raw/wiki files, SQLite manifest, embedded agent contracts, CLI/MCP plumbing, and pull-only read-back"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-03"
---

# Sparks

Sparks, from `yogirk/sparks`, is a Go runtime for a personal-scale "LLM wiki": humans capture raw material, an agent maintains a derived Markdown wiki, and Sparks owns the deterministic plumbing around that workflow. At the reviewed commit, it is not a semantic memory engine, vector store, or autonomous learner. It is a single binary that initializes a fixed vault shape, tracks files and wikilinks in SQLite, parses inbox captures, exposes structured CLI/MCP operations, regenerates hardcoded collections, validates deterministic health checks, and emits an embedded agent contract for Claude Code, Codex, Gemini, or generic harnesses.

**Repository:** https://github.com/yogirk/sparks

**Reviewed commit:** [49abddc848ea55f78518bfbbbe04c3d37a5f2705](https://github.com/yogirk/sparks/commit/49abddc848ea55f78518bfbbbe04c3d37a5f2705)

**Last checked:** 2026-06-03

## Core Ideas

**The memory model is raw capture plus derived wiki.** Sparks initializes a vault with `inbox.md`, append-oriented `raw/`, mutable agent-maintained `wiki/`, fixed wiki subdirectories, `sparks.toml`, and `sparks.db` ([internal/vault/init.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/vault/init.go), [internal/vault/vault.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/vault/vault.go)). The repo documentation states the same three-layer model: raw files are source of truth, wiki pages are derived views, and the manifest tracks state for incremental operations ([README.md](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/README.md), [sparks-contracts.md](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/sparks-contracts.md)).

**It codifies mechanical KB work into a binary.** The central design move is to remove deterministic bookkeeping from agent prose: file hashing, frontmatter parsing, wikilink graph rebuilds, inbox splitting, collection regeneration, stale/thin/orphan checks, and optional git commits live in Go packages rather than in a harness-specific instruction file ([internal/core/scan.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/scan.go), [internal/lint/lint.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/lint/lint.go), [internal/core/ingest_finalize.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/ingest_finalize.go)). The agent is still responsible for semantic work: deciding pages, writing synthesis, resolving contradictions, and choosing task sections.

**The embedded runtime contract is the agent-facing system definition.** `internal/contract/contract.md` is embedded into the binary; `sparks describe` prints it, and `sparks init --agent` writes the same content to `CLAUDE.md`, `AGENTS.md`, or `GEMINI.md` depending on the target harness ([internal/contract/contract.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/contract/contract.go), [cmd/sparks/describe.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/cmd/sparks/describe.go), [internal/core/agent.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/agent.go), [cmd/sparks/init.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/cmd/sparks/init.go)). This is a strong adoption affordance: the protocol is identical across agent harnesses, while the filename adapts to each harness.

**Context efficiency comes from replacing prose procedure with structured operations.** The agent does not need to reread a long operational manual and rederive regexes each run. It calls `sparks ingest --prepare` for bounded JSON entries and deterministic hints, `sparks query` for structured manifest lookup, `sparks affected` for collection impact, `sparks brief` for a recent-activity snapshot, and `sparks lint` for mechanical health checks ([internal/core/ingest.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/ingest.go), [cmd/sparks/query.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/cmd/sparks/query.go), [internal/core/affected.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/affected.go), [internal/core/brief.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/brief.go)). The context volume is bounded by command outputs and the contract's 10-15 entry ingest recommendation; context complexity is reduced by moving deterministic state inspection into code. There is no semantic search budget, embedding top-k, or automatic relevance injection.

**The adapters are intentionally thin and tested that way.** CLI commands parse flags and format output; MCP handlers open the vault and call the same `internal/core` functions. A guard test rejects forbidden imports and oversized command functions in `cmd/sparks`, so SQLite, git, YAML/TOML parsing, and filesystem business logic stay behind internal packages ([internal/mcp/serve.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/mcp/serve.go), [cmd/sparks/arch_test.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/cmd/sparks/arch_test.go)). This matters for memory architecture because the CLI and MCP surfaces are different read/write channels over the same state machine, not competing implementations.

**Collections are deterministic projections, not agent-authored memory.** Sparks hardcodes seven regenerated collections - Quotes, Bookmarks, Books, ReadingList, Media, Ideas, and Projects - with Tasks as the live editable exception. Source globs are configurable only for selected raw-backed collections; extractor behavior and output filenames are code-owned ([internal/collections/collections.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/collections/collections.go), [internal/core/tasks.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/tasks.go)). This gives agents stable derived indexes without asking them to preserve every collection convention manually.

## Artifact analysis

- **Storage substrate:** `files` - The primary knowledge substrate is the vault filesystem: `inbox.md`, `raw/`, `wiki/`, generated collection pages, instruction files, `sparks.toml`, and git-tracked Markdown. A local SQLite `sparks.db` manifest is the secondary operational substrate for hashes, frontmatter, wikilinks, and ingest rows.
- **Representational form:** `mixed` - Prose Markdown carries raw captures, wiki pages, logs, and agent instructions; symbolic TOML, SQLite rows, YAML frontmatter, wikilink edges, command schemas, and Go code carry the deterministic contract.

**Raw captures and inbox entries.** Storage substrate: files under `inbox.md` and `raw/`, with archived inbox entries grouped by capture date. Representational form: mostly prose Markdown with deterministic date separators and hint patterns. Lineage: authored by the human, parsed by `inbox.Split()`, then archived by finalize; raw material is source state, not a generated view ([internal/inbox/inbox.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/inbox/inbox.go), [internal/core/ingest_finalize.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/ingest_finalize.go)). Behavioral authority: knowledge artifacts and evidence for the agent-maintained wiki; agents are instructed not to mutate raw files except through the capture/ingest protocol.

**Wiki pages.** Storage substrate: Markdown files under `wiki/entities/`, `wiki/concepts/`, `wiki/summaries/`, `wiki/synthesis/`, and `wiki/collections/`. Representational form: mixed prose plus YAML frontmatter and wikilinks. Lineage: derived by the agent from raw captures and existing wiki state; `sources:` fields, `created:`, `updated:`, aliases, and revision sections preserve part of the derivation contract. Behavioral authority: knowledge artifacts when read as context or evidence; weak system-definition artifacts when page frontmatter, aliases, maturity, and wikilinks determine query, lint, stale-page, or graph behavior.

**SQLite manifest.** Storage substrate: `sparks.db`, opened with WAL mode and migrations ([internal/manifest/manifest.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/manifest/manifest.go), [internal/manifest/migrations/0001_init.sql](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/manifest/migrations/0001_init.sql)). Representational form: symbolic rows for files, frontmatter, wikilinks, ingest history, and schema version. Lineage: derived from filesystem scans, frontmatter parsing, wikilink extraction, and ingest lifecycle calls. Behavioral authority: system-definition state for structured query, stale detection, affected-collection routing, incremental scans, brief generation, and lint checks. If the manifest is stale, the system's read-back and health reports can be stale until `scan` refreshes it.

**Embedded contract and generated agent files.** Storage substrate: `internal/contract/contract.md` inside the binary, plus generated `CLAUDE.md`, `AGENTS.md`, or `GEMINI.md` in a vault. Representational form: prose instructions with embedded symbolic schemas and command protocols. Lineage: authored package contract copied into harness-specific filenames; the code comments make the embedded contract the source of truth and the repo-root contracts document a synced copy. Behavioral authority: prompt-level system-definition artifact for the host agent, telling it what to do during ingest, query, brief, tasks, and health checks.

**CLI and MCP operations.** Storage substrate: Go modules in `cmd/sparks/`, `internal/core/`, and `internal/mcp/`. Representational form: symbolic command/tool definitions, typed structs, JSON fields, and text renderers. Lineage: authored code, with architecture tests enforcing adapter boundaries. Behavioral authority: system-definition interface for agents and humans; it controls which operations are available, what output enters context, and which writes are mediated by the runtime.

**Generated indexes and collections.** Storage substrate: Markdown files under `wiki/index.md` and `wiki/collections/`. Representational form: mostly prose/Markdown lists generated from symbolic manifest state or raw globs. Lineage: derived views regenerated by `sparks index` and `sparks collections regen`; Tasks is explicitly excluded from regeneration and remains live editable. Behavioral authority: routing/navigation artifacts for later agents and readers. They should be trusted as generated projections of the last scanned state, not as independent sources.

**Lint, affected, status, and brief reports.** Storage substrate: transient command/MCP output, optionally captured elsewhere by the agent. Representational form: symbolic JSON or concise text summaries. Lineage: derived from the manifest and current filesystem. Behavioral authority: advisory and gating-adjacent system-definition outputs. They do not enforce by themselves, but they tell agents what needs repair, what collections need regeneration, and what recent state is worth synthesizing.

**Web viewer.** Storage substrate: embedded templates/CSS and runtime HTTP rendering over vault files. Representational form: rendered HTML from Markdown plus resolved wikilinks. Lineage: derived from wiki Markdown and the same graph resolver used elsewhere ([internal/view/render.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/view/render.go), [internal/graph/resolve.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/graph/resolve.go)). Behavioral authority: human read surface, not agent memory read-back. It helps inspect what agents built but does not decide future actions.

**Promotion path.** Sparks has a clear source-derived promotion path - human capture -> raw archive -> agent-authored wiki page -> generated index/collection -> brief/query/lint outputs - but not an automated trace-to-rule promotion path. The strongest authority jump is the embedded contract and Go runtime: mechanical wiki rules become executable tools rather than recurring prose obligations.

## Comparison with Our System

| Dimension | Sparks | Commonplace |
|---|---|---|
| Primary purpose | Runtime for a personal agent-maintained LLM wiki | Methodology KB and framework for typed agent-operated knowledge bases |
| Main substrate | Vault files plus SQLite manifest | Git-tracked Markdown collections plus validation/review/index commands |
| Artifact contract | Fixed v1 Karpathy-shaped page schema and embedded agent contract | Collection-local contracts, type specs, schemas, skills, and review gates |
| Agent role | Semantic maintainer of wiki pages; runtime owns plumbing | Author/reviewer/operator of typed KB artifacts under collection contracts |
| Context strategy | CLI/MCP commands return bounded structured state; no semantic search | `rg`, indexes, links, type contracts, skills, validation, review reports |
| Governance | Deterministic lint/fmt/frontmatter/link checks, hardcoded ownership rules, git commits on finalize | Deterministic validation, semantic review gates, archive/replacement workflow, curated methodology |

Sparks is close to Commonplace in philosophy: both prefer inspectable files, deterministic plumbing, git-friendly state, and explicit agent contracts over opaque memory services. The difference is scope. Sparks productizes one fixed personal-wiki shape and hardcodes the mechanical layer. Commonplace is a meta-KB system: it lets each collection define its own register, type contracts, validation shape, review process, and navigation surface.

That fixed shape is Sparks's strength. An agent can enter a Sparks vault, ask the binary for the contract, and operate a small set of commands without learning a large methodology. Commonplace is more expressive and more governable, but it asks the agent to load more local conventions before acting. Sparks shows what Commonplace looks like when a large chunk of its operational contract is compiled into a runtime.

The tradeoff is extensibility and authority precision. Sparks v1 hardcodes page types, maturity values, frontmatter fields, collection extractors, and ownership rules. That is excellent for adoption and deterministic correctness, but it means domains that need different artifact families must either fit the Karpathy wiki shape or wait for a future declarative schema layer. Commonplace pays more upfront complexity to keep the type surface open.

**Read-back:** `pull` - Retained memory reaches the agent through explicit CLI/MCP calls such as `query`, `brief`, `status`, `affected`, `lint`, and direct file reads; Sparks does not implement unsolicited relevance-gated memory injection into a future agent action.

### Borrowable Ideas

**Embed the operational contract in the runtime.** Commonplace already ships skills and commands, but Sparks's `describe` command is a clean pattern: the binary can teach agents the exact protocol it implements. Ready now for command documentation surfaces where implementation and agent instruction should not drift.

**Make one small fixed path excellent before generalizing.** Sparks's fixed v1 schema is a useful counterweight to over-general collection design. Commonplace should keep extensibility, but consuming-project templates could start with one opinionated vault shape rather than exposing every type-system knob up front. Ready for onboarding templates.

**Use architecture tests to protect adapter boundaries.** The thin-adapter guard is directly borrowable: Commonplace commands that wrap core library behavior can enforce "no business logic in the command adapter" with tests. Ready where the boundary is already clear.

**Treat deterministic reports as agent context surfaces.** `brief`, `affected`, `status`, and `lint` are not just human commands; they are structured context feeds for agents. Commonplace already has similar reports, but Sparks's product framing makes the role obvious. Ready for command-output UX review.

**Keep generated views clearly subordinate to source state.** Sparks distinguishes raw source, agent-derived wiki, manifest, generated collections, and live Tasks. Commonplace can borrow that explicit ownership table for generated indexes and workshop/library promotion. Ready as documentation and validation messaging.

**Do not borrow the fixed schema wholesale.** Commonplace's whole point is methodology for many artifact types. A fixed entity/concept/summary/synthesis shape is useful as an install profile, not as the framework's core type model.

## Curiosity Pass

**Sparks is an agent memory system without autonomous memory learning.** The memory improvement loop exists, but the semantic step is outside the runtime: the host agent reads prepared entries and writes wiki pages. Sparks preserves and governs the pathway; it does not decide what knowledge should be learned.

**The SQLite manifest is operationally central but not the source of truth.** The docs emphasize files and git, yet many read paths depend on a fresh manifest. That is a reasonable split, but it means agents need to understand when to run `scan` before trusting query, lint, affected, or brief output.

**The contract is both documentation and prompt material.** Writing the same embedded contract into `CLAUDE.md`, `AGENTS.md`, and `GEMINI.md` makes it a portable instruction artifact. It also creates a synchronization problem that Sparks handles by making the binary source authoritative and treating root docs as readable copies.

**The system draws a sharp LLM/code boundary.** Ingest hints use deterministic regex-like classifiers for URLs, tasks, books, to-read markers, and quotes. Semantic categorization is explicitly agent work. This is a clean practical example of codifying only the parts with hard oracles.

**The viewer is intentionally read-only.** That keeps the edit authority with humans, agents, and deterministic commands rather than adding another mutation surface. For a personal wiki, that is a useful trust-preserving constraint.

## What to Watch

- Whether v2 makes page schemas declarative. That would test whether Sparks can keep its runtime-contract simplicity while supporting project-specific KB types.
- Whether semantic or full-text search lands. That would change read-back from structured pull over known symbols toward content-inferred retrieval, and would raise precision/context-dilution questions.
- Whether the MCP surface gains collection regeneration or richer write helpers. That would make MCP a fuller agent operation channel rather than a mirror of the current core subset.
- Whether `sparks describe` and generated agent files gain version/freshness checks. That would make contract drift auditable when a vault was initialized with an older binary.
- Whether raw-to-wiki derivation gains citation verification or review state. That would move Sparks closer to Commonplace's governed artifact lifecycle.

## Bottom Line

Sparks is a strong example of codifying the mechanical half of an agent-operated knowledge base. It does not try to learn from traces or infer relevance automatically; it gives agents a stable runtime for the parts that should be deterministic, then leaves language understanding to the model. For Commonplace, the borrowable lesson is the runtime-owned contract and thin structured tool layer. The caution is that hardcoding a single wiki shape buys reliability by giving up type-system generality.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Sparks stores and queries retained memory but does not push relevant memory into the agent automatically.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Sparks separates files, manifest rows, generated views, embedded contracts, and command outputs by substrate, form, lineage, and authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: the embedded contract, Go command surface, manifest schema, lint checks, and collection generators configure future agent behavior.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: Sparks is mainly a routing/loading/scoping runtime for a bounded agent-maintained wiki.
- [Codification](../../notes/definitions/codification.md) - frames: Sparks moves mechanical KB rules from prose instructions into executable Go code.
- [Methodology enforcement is constraining](../../notes/methodology-enforcement-is-constraining.md) - compares: Sparks pushes repeated mechanical procedures down the instruction-to-script gradient.
