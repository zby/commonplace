---
description: "Sparks review: Go runtime for Karpathy-style LLM wikis with deterministic ingest, manifest, lint, collection, query, brief, and MCP plumbing"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-05"
---

# Sparks

Sparks, from `yogirk/sparks`, is a single-binary Go runtime for personal LLM wikis. It keeps the mechanical layer of a raw-capture plus agent-maintained wiki vault out of agent prose: initialization, inbox splitting, SQLite manifest maintenance, frontmatter and link parsing, deterministic lint, regenerated collections, task helpers, structured queries, weekly brief inputs, git commits, MCP tools, and a read-only local viewer. Semantic classification, page writing, synthesis, and contradiction handling remain the external agent's job.

**Repository:** https://github.com/yogirk/sparks

**Reviewed commit:** [49abddc848ea55f78518bfbbbe04c3d37a5f2705](https://github.com/yogirk/sparks/commit/49abddc848ea55f78518bfbbbe04c3d37a5f2705)

**Last checked:** 2026-06-05

## Core Ideas

**The binary owns the protocol, not the agent instruction file.** `sparks describe` returns an embedded runtime contract, and `sparks init --agent` writes the same contract to `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, or a generic file; only the bridge filename changes ([internal/contract/contract.md](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/contract/contract.md), [internal/core/agent.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/agent.go), [cmd/sparks/describe.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/cmd/sparks/describe.go)). The adoption affordance is strong: a new CLI or MCP-capable agent can use the same vault without a new long-form operating manual.

**The vault is a three-layer retained artifact.** The documented and implemented shape is append-only `raw/`, mutable agent-owned `wiki/`, and `sparks.db` as a SQLite manifest, all under a local filesystem and usually git ([README.md](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/README.md), [sparks-contracts.md](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/sparks-contracts.md), [internal/manifest/migrations/0001_init.sql](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/manifest/migrations/0001_init.sql)). Raw is source material, wiki is the agent-maintained derived view, and the manifest is the deterministic access and state-tracking layer.

**Ingest is two-phase because semantic work is outside the runtime.** `PrepareIngest` parses `inbox.md`, splits entries, opens an in-progress ingest row, and returns structured entries plus deterministic hints; the agent then creates or updates wiki pages; `FinalizeIngest` archives entries, clears the inbox, rescans, optionally commits, and completes the ingest row ([internal/core/ingest.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/ingest.go), [internal/core/ingest_finalize.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/ingest_finalize.go), [internal/inbox/inbox.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/inbox/inbox.go)). The write-side boundary is explicit: deterministic plumbing is automatic, semantic distillation is authored by the agent.

**Context efficiency comes from turning mechanical context into typed tool output.** Instead of making each agent reread prose rules and parse markdown separators, Sparks returns JSON for ingest, status, affected collections, query, lint, and brief operations; the MCP server exposes the same core operations as typed tools ([internal/mcp/serve.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/mcp/serve.go), [internal/core/types.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/types.go), [internal/core/brief.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/brief.go)). There is no semantic retrieval budget or vector ranking; efficiency is achieved by narrowing the agent's job to the structured state needed for the next semantic action.

**The graph and health checks are deterministic.** `Scan` hashes files, mirrors wiki frontmatter, rebuilds wikilink edges, marks disappeared files deleted, and stores all paths with forward slashes. `lint.Run` checks orphans, broken links, missing or invalid frontmatter, thin pages, stale pages, dead sources, and duplicate aliases without an LLM ([internal/core/scan.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/scan.go), [internal/lint/lint.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/lint/lint.go)).

**The implementation protects adapter thinness.** CLI commands and MCP handlers are adapters over `internal/core` and related packages; an architecture-guard test forbids command-layer imports for SQLite, YAML, TOML, MCP internals, and `os/exec`, and caps large command functions ([cmd/sparks/arch_test.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/cmd/sparks/arch_test.go), [internal/mcp/serve.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/mcp/serve.go)). That is not memory behavior by itself, but it matters for trust: the operational contract is testable code rather than scattered adapter logic.

## Artifact analysis

- **Storage substrate:** `files` `repo` `sqlite` — The retained store is a local vault of Markdown files plus `sparks.toml`, usually versioned by git; the behavior-shaping manifest lives in `sparks.db`, a SQLite database with files, frontmatter, wikilinks, ingests, and schema version tables.
- **Representational form:** `prose` `symbolic` — Raw captures, wiki pages, contracts, agent instruction files, index/log pages, and collections are prose; frontmatter, page type enums, paths, hashes, wikilink edges, ingest rows, lint issues, query filters, MCP tool schemas, and collection registries are symbolic. I found no vector, embedding, learned-ranker, or model-weight memory path in this commit.
- **Lineage:** `authored` `imported` — Humans author inbox/raw material and agents author wiki pages, logs, tasks, and descriptions; Sparks imports that material into manifest rows, parsed frontmatter, link edges, archived inbox files, collection pages, and status/query/brief reports. It does not automatically create durable semantic artifacts from agent traces, so `trace-extracted` is not assigned.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` — Raw and wiki pages advise as knowledge; the embedded contract and per-agent files instruct agents; ownership rules, page-type contracts, ingest locks, append-only raw discipline, git commit ownership, and regenerated collection rules constrain behavior; manifest queries, aliases, links, affected collections, and MCP tools route work; lint, fmt, scan, frontmatter parsing, and architecture tests validate mechanical integrity.

**Raw files and inbox entries.** Raw material persists as files, including archived inbox entries grouped by capture date during finalize. These are source material for future semantic wiki edits; Sparks treats raw markdown as opaque during scan, so raw content has knowledge authority but little direct routing authority beyond file paths and deterministic inbox hints ([internal/core/scan.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/scan.go), [internal/inbox/archive.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/inbox/archive.go)).

**Wiki pages and collection pages.** Wiki pages carry frontmatter and body prose under hardcoded page types. Most `wiki/collections/*` pages are regenerated deterministic views; `Tasks.md` is the live exception edited by agents and task helper commands ([sparks-contracts.md](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/sparks-contracts.md), [internal/collections/collections.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/collections/collections.go), [internal/core/tasks.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/tasks.go)). Their authority ranges from knowledge context to instruction-like workflow state when an agent reads tasks or collection membership.

**Manifest rows and graph edges.** The SQLite manifest is a derived symbolic artifact: content hashes, file mtimes, parsed frontmatter, wikilink resolution, ingest status, and changed-since-last-ingest state decide query results, lint results, affected collections, and stale/deleted signals ([internal/manifest/migrations/0001_init.sql](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/manifest/migrations/0001_init.sql), [internal/manifest/queries.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/manifest/queries.go), [internal/manifest/wikilinks.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/manifest/wikilinks.go)).

**Embedded contract and generated agent files.** The contract is both prose instruction and symbolic interface definition: it names page types, ownership boundaries, ingest steps, query limits, and forbidden actions. Because `WriteAgentFile` copies the embedded contract into harness-specific filenames, the generated files are bridges to the same authoritative runtime contract rather than separate policy sources ([internal/contract/contract.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/contract/contract.go), [internal/core/agent.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/agent.go)).

Promotion path: Sparks can promote human inbox/raw capture into archived raw files, manifest rows, deterministic hints, wiki pages authored by an external agent, collection pages, and index entries. The promotion from raw capture to semantic wiki knowledge is deliberately outside the binary; the promotion from wiki prose to validated/routable state happens when scan/lint/query convert frontmatter and links into manifest-backed operations.

## Comparison with Our System

| Dimension | Sparks | Commonplace |
|---|---|---|
| Primary purpose | Runtime plumbing for a personal LLM wiki operated by external agents | Methodology KB and framework for agent-operated knowledge bases |
| Canonical artifacts | Raw Markdown, agent-maintained wiki Markdown, SQLite manifest, embedded contract | Typed Markdown notes, reviews, instructions, sources, indexes, validators |
| Shape flexibility | Hardcoded v1 page types, frontmatter, collections, vault layout | Collection-local contracts and type specs with broader artifact families |
| Read-back | Explicit pull through CLI/MCP status, query, brief, lint, describe, viewer | Mostly explicit pull through `rg`, indexes, links, source snapshots, validation, review bundles |
| Write path | Two-phase ingest, deterministic archive/scan/regen/commit, agent-authored wiki edits | Agent/human-authored artifacts, deterministic validation, semantic review, generated indexes |
| Governance | Embedded contract, lint/fmt/scan, ingest locks, architecture guards, optional git commits | AGENTS instructions, collection contracts, schema validation, review gates, git diffs |

Sparks and Commonplace share the central claim that agent-readable prose plus deterministic tooling beats leaving operational bookkeeping inside a long prompt. Sparks is narrower and more productized: it picks one vault shape and turns mechanical maintenance into a small Go runtime. Commonplace is broader and more methodological: it supports multiple collections, type contracts, review workflows, and transferable notes, but it does not provide one compact personal-wiki runtime binary.

The main design tradeoff is fixed shape versus extensibility. Sparks gets a clean agent protocol because entity/concept/summary/synthesis/collection pages and collection extractors are hardcoded. Commonplace keeps richer local contracts but pays for that flexibility with more navigation and validation surface.

### Borrowable Ideas

**A tiny runtime contract command.** Ready now as a pattern. Commonplace could expose a concise `commonplace describe` or stronger command-level contract summary for agents, separate from the longer reference tree.

**Two-phase ingest with an explicit lock.** Ready for source-ingest workflows. Sparks' `prepare` / agent semantic work / `finalize` split keeps deterministic and semantic responsibilities clean; Commonplace source snapshots and review reruns could benefit from similarly visible lifecycle rows.

**Manifest-backed query for symbolic lookups.** Needs a concrete Commonplace use case first. Sparks shows the value of title, alias, type, maturity, tag, stale, orphan, and link-graph query as structured operations; Commonplace currently relies mostly on `rg` and generated indexes.

**Architecture guards for adapter thinness.** Ready now. The command-layer test is a cheap way to keep CLI and MCP adapters from absorbing business logic.

**Do not borrow the hardcoded taxonomy wholesale.** Sparks' hardcoded page and collection shape is its adoption advantage, but Commonplace's value depends on collection-local contracts and evolving type specs.

## Write side

**Write agency:** `manual` `automatic` — Humans write `inbox.md` and raw files; agents write wiki pages, live tasks, log entries, and index descriptions; Sparks automatically archives inbox entries, clears the inbox, scans and updates the manifest, regenerates non-task collections, rebuilds `wiki/index.md`, runs task helpers, marks tasks done, and optionally commits during finalize.

**Curation operations:** `invalidate` — The automatic write path changes derived state and access structures rather than semantically rewriting stored knowledge. The closest curation operation is invalidation: scan marks disappeared files as deleted without removing their manifest rows, lint flags stale pages when sources are newer than wiki updates, and ingest locks move from `in_progress` to completed or aborted. Collection regeneration and index rebuilds are deterministic derived-view upkeep, not semantic consolidation or synthesis.

Sparks does not qualify for trace-derived learning in this review. It can process traces that a human or agent drops into raw files, and `brief` can gather recent activity for an agent to synthesize, but the binary itself does not distill session logs, tool traces, trajectories, or event streams into durable semantic memories. The semantic output is authored by the external agent and then mechanically tracked.

## Read-back

**Read-back:** `pull` — Retained memory re-enters future work only when a human or agent explicitly asks Sparks for it through CLI/MCP commands such as `describe`, `status`, `query`, `brief`, `lint`, `affected`, `scan`, `index`, or the read-only viewer. I found no implemented hook that automatically injects vault memory into a receiving agent's prompt before an arbitrary task.

Sparks has strong pull surfaces. `sparks query` filters by symbolic page metadata and link graph state; `sparks brief` gathers log entries, new raw files, updated wiki pages, revisit signals, and open tasks; `sparks describe` returns the embedded contract; `sparks serve` exposes those operations as MCP tools ([internal/manifest/queries.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/manifest/queries.go), [internal/core/brief.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/core/brief.go), [internal/mcp/serve.go](https://github.com/yogirk/sparks/blob/49abddc848ea55f78518bfbbbe04c3d37a5f2705/internal/mcp/serve.go)). These are deliberate lookups, not unsolicited read-back.

Context scope is bounded by command choice rather than semantic ranking. Query results are structured page metadata; brief is capped to a recent window and a short task preview; ingest prepare returns only current inbox entries and deterministic hints. Actual semantic relevance, synthesis quality, and whether the agent obeys retrieved memory are not verified by code.

## Curiosity Pass

**Sparks is close to Commonplace in spirit but deliberately smaller.** It productizes one LLM-wiki shape instead of becoming a general KB methodology framework.

**The manifest is behavior-shaping even though users mostly see Markdown.** Hashes, mtimes, link resolution, ingest rows, and parsed frontmatter decide what the agent can cheaply ask and what the runtime flags as stale or invalid.

**The most important memory boundary is negative.** Sparks refuses semantic search and LLM synthesis inside the binary. That makes the runtime trustworthy as plumbing, but it means the quality of wiki knowledge depends on the external agent and its prompts.

**MCP does not make this push read-back.** The MCP server gives typed tools to agents, but the receiving agent must still call them. There is no code-grounded automatic memory injection path at this commit.

**`brief` is a useful liminal artifact.** It gathers recent activity and revisit signals in a structured way, then explicitly hands synthesis back to the agent. That is a clean split between context assembly and semantic interpretation.

## What to Watch

- Whether v2 makes page schemas or collection definitions declarative. That would move Sparks from a fixed runtime contract toward Commonplace-style type and collection contracts.
- Whether Sparks adds semantic search, embeddings, or full-text retrieval. That would change both representational form and read-back complexity.
- Whether MCP integrations gain host-side automatic calls before agent turns. That would move read-back from pull toward push or both, but the host wiring would need code-grounded evidence.
- Whether `brief` or ingest gains automatic synthesis. That would create a qualifying trace-derived or source-derived learning path rather than only deterministic gathering.
- Whether multi-user review, provenance spans, or semantic validation appear. Those would matter if Sparks' agent-authored wiki pages are expected to carry stronger authority than personal knowledge context.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Sparks stores and indexes memory, but read-back is pull-only at this commit.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Sparks' files, SQLite manifest, embedded contract, and generated collections differ by substrate, form, lineage, and authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: the embedded runtime contract, frontmatter schema, lint rules, ingest protocol, and MCP tool definitions constrain future agent behavior.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw captures, wiki pages, collection pages, and brief/query outputs mostly advise as evidence or context.
- [Workshop layer](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - relates: Sparks' two-phase ingest creates a bounded work interval before material is finalized into the wiki.
