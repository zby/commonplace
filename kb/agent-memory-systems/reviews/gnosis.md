---
description: "Gnosis review: repo-local why-memory CLI with JSONL entries, disposable SQLite FTS search, doctrine-guided capture, and pull-only read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-07-06"
---

# Gnosis

Gnosis, by Stavros Korokithakis, is a small Go CLI for repo-local coding-agent memory. It stores short "why" entries in `.gnosis/entries.jsonl`, builds a disposable SQLite FTS5 index for search, and relies on two AGENTS instructions plus embedded doctrine to make future agents search before work and record decisions during or after work.

**Repository:** https://github.com/skorokithakis/gnosis

**Reviewed commit:** [cd1f9921605c6fd43fda2128030b9b43ac72422f](https://github.com/skorokithakis/gnosis/commit/cd1f9921605c6fd43fda2128030b9b43ac72422f)

**Source directory:** `related-systems/skorokithakis--gnosis`

**Last checked:** 2026-07-06

## Core Ideas

**The memory unit is a repo-owned JSONL entry.** An entry has a six-character ID, normalized topics, free-form text, related entry IDs, and created/updated timestamps; `AppendNew` creates `.gnosis` on first write, generates a collision-free ID under a lock, and appends one JSON line to `entries.jsonl` ([internal/storage/storage.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/storage/storage.go), [internal/commands/write.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/write.go)). The README frames those entries as decisions, rejected alternatives, constraints, and intent that live in the repo and ship with the code ([README.md](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/README.md)).

**The SQLite database is a derived access structure, not the source of truth.** `internal/index` opens a per-repo cache directory, creates an FTS5 table with Porter stemming, Unicode tokenization, prefix indexes, BM25 ranking, and snippets, then rebuilds when the JSONL mtime changes or when `gn reindex` runs ([internal/index/index.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/index/index.go), [internal/commands/reindex.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/reindex.go), [internal/paths/paths.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/paths/paths.go)). Deleting or corrupting the cache loses ranking state, not the remembered entries.

**The integration surface is instruction plus shell, not a server.** The executable dispatches subcommands such as `write`, `search`, `latest`, `show`, `topics`, `edit`, `rm`, and `reindex`; there is no MCP server, hook daemon, background watcher, embedding service, or agent runtime in the inspected source ([cmd/gn/main.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/cmd/gn/main.go), [internal/doctrine/commands.txt](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/doctrine/commands.txt)). Adoption is adding AGENTS text that tells agents to run `gn help plan` at task start and `gn help review` after finishing ([README.md](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/README.md), [AGENTS.md](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/AGENTS.md)).

**Context efficiency is lexical narrowing plus a writing filter.** Gnosis does not summarize, compact, embed, semantically rerank, or impose prompt-token budgets. It keeps read-back small by making agents choose search terms, limiting search/latest results, showing snippets, dispatching short targets as ID prefixes and longer targets as topics, and instructing agents not to record analysis that the next agent can rederive from code ([internal/commands/search.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/search.go), [internal/commands/show.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/show.go), [internal/doctrine/plan.txt](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/doctrine/plan.txt), [docs/PRODUCT_STRATEGY.md](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/docs/PRODUCT_STRATEGY.md)).

**Trust comes from inspectability and explicitness, not semantic governance.** Writes and rewrites use file locks, atomic temp-file replacement, topic normalization, related-ID validation, and dangling-reference warnings on removal; the code does not attach source spans, confidence, entry kinds, stale states, review status, or validation beyond syntax/shape checks ([internal/storage/storage.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/storage/storage.go), [internal/commands/edit.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/edit.go), [internal/commands/rm.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/rm.go)). The checked-in `.gnosis/entries.jsonl` shows the intended artifact directly: concise decisions and rejected alternatives, including rejecting MCP for now and choosing SQLite FTS5 over Bleve ([.gnosis/entries.jsonl](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/.gnosis/entries.jsonl)).

## Artifact analysis

- **Storage substrate:** `files` `sqlite` — The canonical retained store is repo-local files: `.gnosis/entries.jsonl` plus AGENTS/doctrine text. SQLite persists in the per-repo cache as a rebuildable FTS5 ranking/search projection rather than canonical memory.
- **Representational form:** `prose` `symbolic` — Entry text and doctrine are prose; IDs, topics, related IDs, timestamps, command schemas, topic normalization, ID-prefix resolution, FTS queries, snippets, and BM25 ranking are symbolic structures.
- **Lineage:** `authored` — Entries are explicitly written, edited, or removed by a human or instructed agent through CLI commands; the inspected source does not mine transcripts, logs, tool traces, or embeddings into durable memory.
- **Behavioral authority:** `knowledge` `instruction` `ranking` — Entries advise later agents as knowledge artifacts; AGENTS/doctrine text tells agents when to search, write, review, and tidy; the FTS5 index ranks explicit lookup results.

**Entries.** A Gnosis entry is a compact knowledge artifact: topic-labeled prose with optional related IDs and timestamps. It can change a later action only when an agent reads it and treats the remembered decision, constraint, or rejected alternative as relevant. The source format is reviewable but coarse; there is no claim-level provenance, confidence, source pointer, stale marker, or entry type.

**Doctrine and AGENTS instructions.** The shipped doctrine is the system-definition surface. `gn help plan` tells agents to search before implementation, surface conflicting recorded decisions, write decisions immediately, and tidy contradictions; `gn help review` guides end-of-session capture and repeats the "human knowledge, not yours" filter ([internal/doctrine/plan.txt](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/doctrine/plan.txt), [internal/doctrine/review.txt](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/doctrine/review.txt)). The host repo's AGENTS file is the adoption hook, but Gnosis itself ships the doctrine and CLI rather than an automatic injection mechanism.

**Search projection.** The FTS5 table is a derived ranking artifact over entry text and topics. `Search` sanitizes the user's query, ensures the index is fresh, runs FTS5 `MATCH`, orders by `rank`, and prints IDs, dates, primary topics, and snippets ([internal/commands/search.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/search.go), [internal/index/index.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/index/index.go)). This changes what is easy to find, not what memory exists.

**Promotion path.** Gnosis has no internal promotion path from an entry into a stronger form or authority such as a code comment, ADR, validator, test, or enforced gate. The doctrine points agents toward comments when a decision has a clear code anchor and toward `gn rm` or related replacement entries when knowledge becomes stale, but any promotion into code or documentation happens outside Gnosis.

## Comparison with Our System

| Dimension | Gnosis | Commonplace |
|---|---|---|
| Primary purpose | Repo-local "why" memory for coding agents | Typed methodology knowledge for agent-operated KBs |
| Canonical substrate | JSONL entries plus doctrine in ordinary repo files | Markdown collections, type specs, source snapshots, and generated indexes |
| Retrieval | Explicit CLI pull through FTS5 search, latest, topic, and ID lookup | `rg`, curated indexes, links, skills, reports, and validators |
| Write path | Agent/human CLI writes and edits under doctrine | Authored notes, reviews, instructions, source ingests, validation, and review workflows |
| Governance | Syntax checks, topic normalization, locks, and doctrine | Collection contracts, frontmatter schemas, citations, validation, review gates, and git history |

Gnosis is much narrower than Commonplace. Its best design move is adoption: one binary and two AGENTS lines can get ordinary coding agents searching and writing in a repo they already operate. Commonplace is heavier because it asks artifacts to declare type, register, evidence, links, status, and sometimes review provenance.

The systems also disagree about what should be remembered. Gnosis tries to filter out anything a future agent can reconstruct from code and docs; Commonplace often wants transferable theory distilled from analysis once the mechanism is understood. That makes Gnosis a clean decision-capture product, but too restrictive as a methodology KB.

### Borrowable Ideas

**Two-line adoption hook.** Commonplace workflows should keep a minimal AGENTS-facing start/review path for common tasks. Ready now where the workflow boundary is stable.

**Committed source plus disposable search cache.** Gnosis cleanly separates durable memory from acceleration. Commonplace should keep any future lexical/vector cache subordinate to authored artifacts. Ready when a heavier cache is needed.

**Topic/ID partition.** Requiring normalized topics to be longer than six-character IDs lets `show` dispatch short targets as ID prefixes and longer targets as topics without fallback ambiguity ([internal/commands/show.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/show.go), [internal/commands/write.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/write.go)). Useful if Commonplace adds short stable IDs.

**Noise control as doctrine first.** "Record what the human knows" is a memorable product constraint. Commonplace can borrow the clarity while keeping its broader remit for transferable claims and methodology theory.

**Do not borrow doctrine-only governance for high-authority artifacts.** Gnosis can tolerate weak review state because entries are advisory. Commonplace should keep validators, citations, and semantic review before artifacts gain system-definition authority.

## Write side

**Write agency:** `manual` — The durable store changes only when a human or instructed agent explicitly runs `gn write`, `gn edit`, or `gn rm`; index freshness and `gn reindex` rebuild a derived search projection, not the content store.

Gnosis is manual-only under the current contract, so there is no `**Curation operations:**` lead line. The inspected implementation supports create, update, delete, topic normalization, related-ID validation, and index rebuilding, but I found no automatic `consolidate`, `dedup`, `evolve`, `synthesize`, `invalidate`, `decay`, or `promote` operation over already-stored memory. The README's "agents follow instructions every time" claim is an adoption bet about instruction-following agents, not an automatic curation mechanism implemented by Gnosis itself ([README.md](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/README.md), [docs/PRODUCT_STRATEGY.md](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/docs/PRODUCT_STRATEGY.md)).

## Read-back

**Read-back:** `pull` — Retained entries reach an agent only when the agent or user explicitly runs `gn search`, `gn show`, `gn latest`, or `gn topics`; Gnosis ships instructions to perform that lookup, but it does not push retained memory through hooks, session-start context, MCP responses, prompt assembly, or an always-loaded memory block.

Pull retrieval is lexical and symbolic. `search` uses FTS5 over entry text and topics with snippets and a default result limit; `show` treats targets of six characters or fewer as ID prefixes and longer targets as normalized topics; `latest` sorts by creation time; `topics` aggregates normalized topic counts ([internal/commands/search.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/search.go), [internal/commands/show.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/show.go), [internal/commands/latest.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/latest.go), [internal/commands/topics.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/topics.go)). Precision, recall, and whether agents faithfully obey conflicting entries are not verified from code.

The doctrine path matters but does not change the read-back verdict. Static AGENTS/doctrine text can tell an agent to search, but the retained memory itself is not in context until the agent performs the pull.

## Curiosity Pass

**The strongest design move is refusing automation.** Gnosis does not try to infer importance from transcripts, summarize sessions, or mine logs. It makes the acting agent decide what perishable knowledge should be recorded, which keeps the code small and the store inspectable while moving quality risk into instruction-following.

**The product calls agents "automatic," but the implementation is explicit.** Product strategy says agents participate automatically once AGENTS instructions exist; the code evidence shows explicit shell commands, not background capture or push read-back. That difference matters for comparison because Gnosis depends on agent obedience at task boundaries.

**The source of truth is easy to review but not typed.** JSONL in git is diffable and portable, but each body is an undifferentiated assertion. There is no built-in stale state, source link, confidence, owner, entry kind, or verification marker.

**Search quality is intentionally lexical.** FTS5 stemming, prefix indexes, snippets, and BM25 are enough for small repo-local why-memory. The absence of semantic retrieval is consistent with the product stance until stores become large enough that keyword choice is the bottleneck.

**The repository uses Gnosis on itself.** The checked-in entries are not just samples; they document product decisions such as rejecting MCP for now and choosing FTS5 over Bleve, so the reviewed system supplies evidence of its intended use pattern.

## What to Watch

- Whether Gnosis adds MCP or another non-shell interface for agents without CLI access; that would broaden integration without necessarily changing the pull-only read-back verdict.
- Whether shared `.gnosis` directories need merge-conflict, stale-entry, or replacement workflows as teams collaborate through git.
- Whether entries gain metadata such as kind, source, confidence, supersession, owner, or review status without losing the capture-first workflow.
- Whether doctrine-only noise control remains sufficient once multiple agents and users write into the same repo memory.
- Whether search remains lexical or grows semantic retrieval; that would change ranking machinery but not automatically create curation.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Gnosis stores memory locally but relies on explicit pull for read-back.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Gnosis separates file-backed entries, doctrine, and symbolic search/index structures.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: Gnosis entries advise future agents as evidence and context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: AGENTS/doctrine instructions shape when agents search, write, review, and tidy memory.
- [Retained artifact](../../notes/definitions/retained-artifact.md) - grounds: entries, doctrine, and derived indexes persist across sessions; raw session context does not.
