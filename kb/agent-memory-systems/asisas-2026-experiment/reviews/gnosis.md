---
description: "Gnosis review: repo-local why-memory CLI with JSONL entries, disposable SQLite FTS search, doctrine-guided agent capture, and pull-only read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
---

# Gnosis

Gnosis is Stavros Korokithakis's small Go CLI for repo-local coding-agent memory. It asks maintainers to add two AGENTS lines so future agents search prior "why" entries before work, write durable decisions during work, and review the session afterward; the implementation stores those entries in `.gnosis/entries.jsonl` and builds a disposable SQLite FTS5 search cache.

**Repository:** https://github.com/skorokithakis/gnosis

**Reviewed commit:** [cd1f9921605c6fd43fda2128030b9b43ac72422f](https://github.com/skorokithakis/gnosis/commit/cd1f9921605c6fd43fda2128030b9b43ac72422f)

**Last checked:** 2026-06-04

## Core Ideas

**The durable memory is committed JSONL, not a service.** Each entry carries a six-character ID, normalized topics, free-form text, related entry IDs, and created/updated timestamps; writes create `.gnosis` on demand and append to `.gnosis/entries.jsonl` ([internal/storage/storage.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/storage/storage.go), [.gnosis/entries.jsonl](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/.gnosis/entries.jsonl)). The README explicitly presents this as memory that lives in the repo and ships with the code ([README.md](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/README.md)).

**SQLite FTS5 is a rebuildable access structure.** The index lives outside `.gnosis` in a per-repo cache path, uses FTS5 with BM25 ranking and snippets, and is rebuilt when the JSONL mtime changes or when `gn reindex` is invoked ([internal/index/index.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/index/index.go), [internal/commands/search.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/search.go), [internal/commands/reindex.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/reindex.go)). That keeps the retained memory auditable while allowing faster retrieval.

**The behavior change is instruction-mediated.** Gnosis does not integrate through hooks, MCP, background jobs, or an agent runtime. Adoption is adding instructions that tell agents to run `gn help plan` at the start and `gn help review` at the end; those embedded doctrine files tell agents to search before implementing, surface conflicts, write decisions as they arise, and prefer human-provided or empirical context over analysis a future agent can rederive from code ([README.md](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/README.md), [internal/doctrine/plan.txt](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/doctrine/plan.txt), [internal/doctrine/review.txt](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/doctrine/review.txt)).

**Context efficiency is lexical narrowing plus doctrine, not compaction.** The system does not summarize, embed, rerank semantically, or budget prompt tokens. It relies on agents choosing relevant search keywords, FTS5 matching over text and topics, result limits, snippets, topic/ID lookup, and the doctrine's "do not record reproducible analysis" filter to keep future context small and useful ([internal/commands/search.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/search.go), [internal/commands/show.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/show.go), [docs/PRODUCT_STRATEGY.md](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/docs/PRODUCT_STRATEGY.md)).

**Operational safety is stronger than semantic governance.** Appends and rewrites use locks, ID generation is serialized, rewrites go through temp files and atomic rename, topics are normalized on write/read, and removals warn about dangling related references instead of silently editing survivors ([internal/storage/storage.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/storage/storage.go), [internal/commands/write.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/write.go), [internal/commands/edit.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/edit.go), [internal/commands/rm.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/rm.go)). The content quality model remains doctrinal: entries have no kind, confidence, source span, review state, stale marker, or validator.

## Artifact analysis

- **Storage substrate:** `files` — The retained behavior-shaping store is `.gnosis/entries.jsonl`; SQLite FTS5 is an external cache rebuilt from that file rather than the canonical memory substrate.
- **Representational form:** `prose` `symbolic` — Entry bodies and doctrine text are prose; IDs, topics, related IDs, timestamps, command schemas, normalized topic rules, and the FTS index are symbolic access and routing structures.
- **Lineage:** `authored` — Entries are explicitly written or edited by agents/humans through `gn write` and `gn edit`; Gnosis does not preserve raw transcripts or automatically mine session logs.
- **Behavioral authority:** `knowledge` `instruction` `ranking` — Entries advise later agents as knowledge artifacts; AGENTS/doctrine text instructs agents to search, write, review, and tidy; FTS5/BM25 and topic sorting rank what explicit lookups return.

**Entries.** A Gnosis entry is a compact knowledge artifact: topic-labeled text with optional related IDs and timestamps. Its future authority depends on a later agent reading it and deciding whether it conflicts with the current task; the code does not attach confidence, source evidence, or review status ([internal/storage/storage.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/storage/storage.go), [internal/doctrine/plan.txt](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/doctrine/plan.txt)).

**Doctrine and AGENTS instructions.** The help text is an embedded system-definition artifact: it instructs agents when to search, when to write, what not to write, and how to remove or relate superseded entries ([internal/doctrine/plan.txt](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/doctrine/plan.txt), [internal/doctrine/review.txt](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/doctrine/review.txt)). The host repo's AGENTS file is the adoption hook, but Gnosis itself only ships the doctrine and CLI.

**Search projection.** The FTS5 table is a derived ranking artifact over entry text and topics. It changes which entries are cheap to find, but not what memory exists; deletion or corruption of the index is recoverable through `EnsureFresh` or `gn reindex` ([internal/index/index.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/index/index.go), [internal/commands/reindex.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/reindex.go)).

**Promotion path.** Gnosis has no internal promotion ladder from entry to test, validator, ADR, instruction, or enforced gate. Promotion can happen only outside the system when a human or agent turns an entry into ordinary repo work.

## Comparison with Our System

| Dimension | Gnosis | Commonplace |
|---|---|---|
| Primary purpose | Capture project-local "why" memory for coding agents | Maintain typed methodology knowledge for agent-operated KBs |
| Canonical substrate | Repo-local JSONL entries | Repo-local Markdown collections with type specs |
| Retrieval | Explicit CLI pull through FTS5, latest, topic, and ID lookup | `rg`, indexes, links, generated reports, and skills |
| Write path | Agent/human CLI writes and edits | Authored notes/reviews/instructions plus validation/review workflows |
| Governance | Doctrine, topic normalization, locks, and manual edit/remove | Collection contracts, schemas, validators, semantic review, git history |

Gnosis is a deliberately narrow memory layer. It is stronger than Commonplace on low-friction adoption: one binary and two AGENTS lines can get agents searching and writing in an ordinary repo. Commonplace is stronger on artifact contracts and trust: its notes, reviews, type specs, and validation reports carry more declared authority and review surface.

The systems also differ in what they consider valuable memory. Gnosis tries to avoid entries that future agents can rederive from code and docs; Commonplace often wants reusable theory distilled from agent analysis once the mechanism is understood. That makes Gnosis a good product pattern for decision capture, but too restrictive as a methodology KB.

### Borrowable Ideas

**Two-line adoption hook.** Commonplace skills and installed commands should keep a tiny AGENTS-facing invocation path for the common workflow boundary. Ready now.

**Committed source plus disposable search cache.** Gnosis cleanly separates durable memory from search acceleration. Commonplace can borrow that shape for heavier lexical/vector caches without making generated state authoritative. Ready when a cache is needed.

**Topic/ID lexical partition.** Gnosis requires topics to be longer than six-character IDs, which lets `show` dispatch short targets as ID prefixes and longer targets as topics without a fallback ambiguity ([internal/commands/show.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/show.go), [internal/commands/write.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/write.go)). Useful if Commonplace ever adds short stable IDs.

**Noise control as doctrine first.** The "record what the human knows" filter is cheap, memorable, and product-shaping. Commonplace can borrow the clarity while keeping its broader remit for transferable claims.

## Write side

**Write agency:** `manual` — Entries change only through explicit `gn write`, `gn edit`, and `gn rm` operations by an agent or human; index freshness/rebuilds are access-structure upkeep, not content curation.

Because write agency is manual-only, Gnosis has no automatic curation-operation lead line under the current contract. The code supports create/update/delete and search-index rebuilds, but I found no automatic `consolidate`, `dedup`, `evolve`, `synthesize`, `invalidate`, `decay`, or `promote` operation over stored memory.

## Read-back

**Read-back:** `pull` — Retained entries reach future agents only when the agent or user explicitly runs `gn search`, `gn show`, `gn latest`, or `gn topics`; Gnosis ships doctrine telling agents to perform that pull, but it does not push retained memory through hooks, startup context, MCP responses, or an always-loaded memory block.

Pull retrieval is keyword/topic/ID based. `search` sanitizes a user query, runs FTS5 over entry text and topics, and returns ranked snippets; `show` dispatches short targets to ID-prefix resolution and longer targets to normalized topic lookup; `latest` sorts by created time ([internal/commands/search.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/search.go), [internal/commands/show.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/show.go), [internal/commands/latest.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/latest.go)). Precision, recall, and whether agents actually obey conflicting entries are not verified from code.

The AGENTS/doctrine path is important but does not change the read-back verdict. Static instructions that tell an agent to search are baseline context; the retained memory itself still enters only after an explicit lookup.

## Curiosity Pass

**The strongest design move is refusing automation.** Gnosis does not try to mine transcripts, infer importance, or summarize sessions. It makes the acting agent decide what the human knows that would otherwise be lost, which keeps the implementation tiny but moves quality risk into instruction-following.

**The source of truth is reviewable but coarse.** JSONL in git is easy to inspect and diff, but the entry body is an undifferentiated prose assertion. There is no entry type, stale state, source pointer, or claim-level provenance.

**The repo's own entries are part of the product evidence.** The checked-in `.gnosis/entries.jsonl` records decisions such as rejecting MCP for now and choosing FTS5 over Bleve, showing the intended use case directly in the reviewed repository ([.gnosis/entries.jsonl](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/.gnosis/entries.jsonl)).

**Search quality is intentionally lexical.** FTS5 stemming, prefix indexes, snippets, and BM25 are enough for small repo-local why-memory. The absence of semantic retrieval is a feature until users need fuzzy recall across larger stores.

## What to Watch

- Whether Gnosis keeps betting on shell access or adds MCP/server surfaces for agents that cannot run a CLI.
- Whether shared `.gnosis` directories develop merge-conflict, import/export, or stale-entry workflows as teams collaborate through git.
- Whether entry metadata grows kind, confidence, source, supersession, or review fields without losing the capture-first product stance.
- Whether doctrine-only noise control is enough once multiple agents and users write into the same repo memory.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Gnosis stores memory locally but relies on explicit agent pull for read-back.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: Gnosis separates file-backed prose entries from symbolic CLI/index/doctrine machinery.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: Gnosis entries advise future agents as evidence and context.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: AGENTS/doctrine instructions shape when agents search, write, review, and tidy memory.
- [Retained artifact](../../../notes/definitions/retained-artifact.md) - grounds: only explicit entries and doctrine persist; raw session context is not retained by Gnosis.
