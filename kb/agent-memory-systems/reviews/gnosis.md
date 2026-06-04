---
description: "Gnosis review: tiny Go CLI for repo-local agent-written why memory, JSONL source of truth, FTS5 cache, and doctrine-mediated agent workflow"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-06-01"
---

# Gnosis

Gnosis is Stavros Korokithakis's small Go CLI for project-local agent memory. It stores the "why" behind a codebase - decisions, rejected alternatives, constraints, and intent - in a repository directory that coding agents can search before work and update while work is happening. Its memory model is deliberately low-ceremony: agent behavior is changed by two `AGENTS.md` instructions, an embedded doctrine prompt, and a shell command surface rather than by a daemon, MCP server, hosted service, or model-side memory layer.

**Repository:** https://github.com/skorokithakis/gnosis

**Reviewed commit:** [cd1f9921605c6fd43fda2128030b9b43ac72422f](https://github.com/skorokithakis/gnosis/commit/cd1f9921605c6fd43fda2128030b9b43ac72422f)

**Last checked:** 2026-06-01

## Core Ideas

**Repo-local JSONL is the canonical memory substrate.** `storage.NewStore` finds the repo root, points the store at `.gnosis/entries.jsonl`, and creates `.gnosis` only on first write. Each entry has a six-letter ID, normalized topics, free text, related entry IDs, and created/updated timestamps; appends and rewrites serialize complete JSON lines rather than maintaining a hidden database as the source of truth ([internal/storage/storage.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/storage/storage.go), [.gnosis/entries.jsonl](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/.gnosis/entries.jsonl)).

**SQLite FTS5 is a disposable retrieval projection.** Search opens a per-repo cache under `XDG_CACHE_HOME` or `~/.cache`, keyed by a hash of the repo root, then rebuilds the FTS5 index when the JSONL mtime changes. The index stores entry IDs, text, topics, snippets, BM25 ranking, stemming, unicode tokenization, and short prefix structures, but `gn reindex` can rebuild it from JSONL at any time ([internal/index/index.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/index/index.go), [internal/paths/paths.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/paths/paths.go), [internal/commands/reindex.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/reindex.go)).

**The behavior-changing layer is doctrine.** The README tells adopters to add two lines to `AGENTS.md`: run `gn help plan` at task start and `gn help review` after finishing. The embedded plan doctrine tells agents to search before implementation, surface conflicts, record decisions during work, and prefer human or empirical knowledge over analysis reproducible from the code. The review doctrine repeats the same filter at session end ([README.md](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/README.md), [internal/doctrine/plan.txt](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/doctrine/plan.txt), [internal/doctrine/review.txt](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/doctrine/review.txt), [docs/PRODUCT_STRATEGY.md](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/docs/PRODUCT_STRATEGY.md)).

**Context efficiency comes from a tiny pull path, not from budgeting.** `gn help plan` instructs the agent to choose keywords from its plan and search with explicit `OR` terms; `gn search` defaults to 20 one-line snippet results; `gn show` expands an ID or topic to full entries; `gn latest` and `gn topics` provide cheap orientation surfaces ([internal/doctrine/plan.txt](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/doctrine/plan.txt), [internal/commands/search.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/search.go), [internal/commands/show.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/show.go), [internal/commands/latest.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/latest.go), [internal/commands/topics.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/topics.go)). There is no token budget, semantic chunking, embeddings, summarizer, or automatic context injection; efficiency depends on the agent making a good query and expanding only relevant hits.

**The command surface is intentionally narrow and shell-native.** `cmd/gn/main.go` dispatches to help, write, search, latest, show, topics, edit, remove, and reindex. `write` accepts comma-separated topics and optional related IDs; `show` dispatches by ID-prefix length versus topic length; `edit` supports `$EDITOR`, positional replacement, and piped stdin; `rm` warns about dangling related references without silently mutating survivors ([cmd/gn/main.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/cmd/gn/main.go), [internal/commands/write.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/write.go), [internal/commands/resolve.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/resolve.go), [internal/commands/edit.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/edit.go), [internal/commands/rm.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/rm.go)).

**Operational integrity is stronger than semantic governance.** Writes use `O_APPEND`; ID generation and rewrites take exclusive file locks; full rewrites go through temp-file rename; topics normalize on write and read; the index rebuild reads entries and captures mtime under the same shared lock ([internal/storage/storage.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/storage/storage.go), [internal/index/index.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/index/index.go)). The semantic side is mostly doctrine: there are no entry kinds, source fields, confidence, freshness markers, validation gates, stale/superseded states, or review status beyond manual edit, remove, and related IDs.

## Artifact analysis

- **Storage substrate:** `files` — Ordinary files under `.gnosis/`, intended to ship with code and be visible to git
- **Representational form:** `prose` `symbolic` — prose body text and doctrine, plus symbolic metadata for ID, topics, related IDs, timestamps, indexes, and command routing
- **Lineage:** `authored` `trace-extracted` — entries are authored by an agent or human through CLI commands, and doctrine can make the agent distill live-session observations into durable entries
- **Behavioral authority:** `knowledge` `instruction` `routing` `ranking` — entries provide advisory knowledge; doctrine and host instructions route agents into the CLI; FTS5 decides ranked retrieval order

**Entries.** The central retained artifacts are `.gnosis/entries.jsonl` entries in the project repo. Their storage substrate is ordinary files under `.gnosis/`, intended to ship with code and be visible to git. Their representational form combines prose body text with symbolic metadata for ID, topics, related IDs, and timestamps. Their lineage is authored live by an agent or human through `gn write` or rewritten through `gn edit`; when produced by the planning/review doctrine, they are distilled from the agent's current work session rather than regenerated from source files or retained raw logs. Their behavioral authority is mostly knowledge-artifact authority: future agents consume entries as evidence, reference, context, or advice. They become stronger only when an agent accepts a retrieved decision as constraining the next plan.

**Doctrine.** `internal/doctrine/*.txt`, exposed through `gn help`, is a prose system-definition artifact. Its storage substrate is embedded text in the Go binary, sourced from repo files at build time. Its representational form is prose instruction. Its lineage is authored product doctrine, with `docs/PRODUCT_STRATEGY.md` documenting the signal-to-noise decision behind "record what the human knows." Its behavioral authority is instruction and routing: when `AGENTS.md` tells an agent to run `gn help plan` or `gn help review`, the doctrine tells the agent when to search, what counts as worth recording, and when to avoid writing noise.

**Index and cache.** The SQLite FTS5 database and lock file live outside the repo in a per-repo cache directory. Their storage substrate is a local cache, not the canonical memory. Their representational form is symbolic index state derived from entry text and topics. Their lineage is the current JSONL file and recorded mtime; deleting or rebuilding the cache should not lose knowledge. Their behavioral authority is ranking and retrieval: the index decides which entries are surfaced for a query, but the returned snippets remain advisory context rather than enforced policy.

**Agent integration.** The adoption instructions in a host repo's `AGENTS.md` are prose system-definition artifacts in that host repo, not generated by gnosis. Their authority depends on the agent runtime loading `AGENTS.md`. They route the agent into the CLI at task boundaries, but gnosis itself does not install hooks, intercept actions, or inject memories.

There is no implemented promotion path from entry evidence to a stronger artifact such as a typed rule, validator, or enforced gate. Promotion is manual: a maintainer or agent can turn a retrieved decision into code, documentation, comments, or a new instruction outside gnosis.

## Comparison with Our System

| Dimension | Gnosis | Commonplace |
|---|---|---|
| Primary purpose | Capture repo-local "why" memory for coding agents | Build and govern a typed agent-operated methodology KB |
| Canonical substrate | `.gnosis/entries.jsonl` in the project repo | Git-tracked markdown collections under `kb/` |
| Retrieval | FTS5 search, latest, topics, show by ID/topic | `rg`, descriptions, indexes, authored links, skills, review reports |
| Context activation | Agent follows doctrine and runs CLI searches | Agent follows repo instructions, collection contracts, skills, and review workflows |
| Artifact authority | Lightweight advisory entries plus doctrine | Typed artifacts, schemas, validators, review gates, indexes, instructions |
| Lifecycle | Manual edit/remove and related IDs | Status fields, replacement archives, validation, review findings, curated/generative indexes |

Gnosis is much narrower than Commonplace, and that narrowness is the design. It does not try to model a knowledge base methodology, define artifact families, preserve source snapshots, validate links, or curate a library. It asks one operational question: how can a repo make coding agents remember non-obvious decisions without expecting humans to maintain a wiki?

The strongest alignment is the filesystem-first premise. Both systems treat durable memory as inspectable project state and treat indexes as derived aids rather than the source of truth. Gnosis is the smaller version of that idea: one JSONL file, one CLI, one cache, and one doctrine surface.

The biggest divergence is authority and reviewability. Commonplace gives durable artifacts explicit contracts: a review, note, type spec, instruction, or ADR promises a known shape and can be validated or reviewed. Gnosis entries have low friction but weak semantics. A carefully recorded rejected alternative and a vague stale note have the same schema; trust comes from future agent judgment and manual cleanup.

The second divergence is the writer filter. Commonplace often wants agents to distill transferable mechanisms from source material. Gnosis explicitly discourages recording what a future competent agent could rederive from code and docs. That is a good fit for repo-local institutional memory, but it would be too restrictive for a methodology KB whose job is to accumulate abstractions.

**Read-back:** `pull` — Agents deliberately run `gn search`, `gn latest`, `gn topics`, or `gn show`; host `AGENTS.md` can make that pull habitual, but gnosis does not implement relevance-gated push activation

### Borrowable Ideas

**Two-line adoption hook.** Ready now as a packaging pattern. Gnosis gets behavior change by asking users to add a tiny instruction to `AGENTS.md` rather than integrating with every agent runtime. Commonplace skills and init flows should keep their entrypoint similarly small.

**Committed source plus disposable retrieval cache.** Ready for future retrieval work. Gnosis keeps the canonical memory in git and moves locks/indexes into a per-repo cache. Commonplace should preserve that source/projection split for any future FTS, embedding, or ranking cache.

**Doctrine as the signal-to-noise control.** Needs a use case before copying wholesale. Gnosis's "record what the human knows, not what you can infer" rule is too narrow for Commonplace notes, but useful for any future lightweight project-memory mode.

**Lexical partition between IDs and topics.** Ready as a small design trick. Requiring normalized topics to exceed the six-character ID length lets `show` dispatch without an ambiguous fallback. If Commonplace adds short IDs, avoid overlapping identifier spaces.

**No MCP until the target agents need it.** Ready as a product discipline. Gnosis's shell-first surface is enough for coding agents with terminal access. Commonplace should add protocol surfaces only when they carry different authority or reach, not just because the protocol exists.

## Trace-derived learning placement

- **Trace source:** `session-logs` — the source trace is the live agent session context rather than stored chat logs, shell history, commits, or hidden tool traces
- **Learning scope:** `per-task` `per-project` `cross-task` — capture happens during one task, storage is project-local, and entries are meant to inform later tasks in the same repo
- **Learning timing:** `online` `staged` — agents write during work and again during end-of-session review; there is no offline corpus pass
- **Distilled form:** `prose` `symbolic` — distilled JSONL entries carry prose observations plus symbolic topics, IDs, related IDs, and timestamps

Gnosis qualifies as trace-derived in the manual/live-extraction sense, not the automated transcript-mining sense. The code does not ingest stored chat logs, shell history, commits, or hidden tool traces. Instead, the embedded doctrine makes the acting agent use the current work session as the trace and explicitly write distilled entries while context is still available.

**Trace source.** The source trace is the live agent session: the user's task context, plan, decisions made during implementation, rejected alternatives, empirical findings, and end-of-session observations. `plan.txt` tells the agent to record decisions immediately when context might be lost, and `review.txt` tells the agent to scan the finished session for durable intangibles ([internal/doctrine/plan.txt](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/doctrine/plan.txt), [internal/doctrine/review.txt](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/doctrine/review.txt)).

**Extraction.** The extraction oracle is the acting agent following prose doctrine. It decides whether a session observation is non-reproducible enough to retain, then writes a distilled prose entry through `gn write <topics> <text> [--related id,id]`. Gnosis does not supply an LLM judge, confidence score, automatic summarizer, or separate curation pass ([internal/commands/write.go](https://github.com/skorokithakis/gnosis/blob/cd1f9921605c6fd43fda2128030b9b43ac72422f/internal/commands/write.go)).

**Four fields.** The raw trace is ephemeral working context, not a retained gnosis artifact. The durable extracted artifact is the JSONL entry described in Artifact analysis: file substrate, prose/symbolic form, session-authored lineage, and knowledge-artifact authority at future read time. The doctrine and host `AGENTS.md` instructions are the system-definition artifacts that cause the extraction loop to run.

**Scope and timing.** The loop is per-repository and cross-session in storage, but per-task in capture. Extraction happens online during work and again at a staged end-of-session review. There is no offline corpus pass over accumulated transcripts.

**Survey placement.** Gnosis sits at the manual/live-extraction end of the trace-derived axis. It strengthens the survey claim that the extraction oracle matters more than the storage substrate: a plain JSONL store becomes an agent-memory system because doctrine tells the agent which parts of the session are worth distilling.

## Curiosity Pass

**The memory system is mostly an instruction system.** The durable entries matter, but the distinctive mechanism is the doctrine that tells agents when not to write. Without that filter, `.gnosis/entries.jsonl` would be just a lightweight notes file.

**The end-of-session review is trace-derived but not automatic.** `gn help review` asks the agent to scan the session and decide whether anything should be recorded, but the checked code does not read transcripts, tool traces, shell history, commits, or logs. The durable artifact is authored through judgment, not extracted by a background trace-processing pipeline.

**The cache boundary is clean.** Moving the lock and `index.db` out of `.gnosis` avoids committing runtime coordination and derived state. That is a small but important difference from tools that let caches blur into canonical memory.

**Related IDs are intentionally weak structure.** They preserve manual adjacency but do not define link types, supersession, contradiction, rationale, or evidence. This keeps capture cheap and makes later interpretation more expensive.

**The repository dogfoods its own memory.** The checked-in `.gnosis/entries.jsonl` includes release, distribution, architecture, and search-index decisions, so the repo is a useful example of the artifact shape. The examples also show the tradeoff: entries are readable, but they are not typed by decision kind or lifecycle state.

## What to Watch

- Whether entry lifecycle gains stale, superseded, confidence, source, or kind fields without undermining the capture-first workflow.
- Whether the doctrine remains enough to control noise as more agents write entries across different coding environments.
- Whether a future MCP or editor integration preserves the same source/projection split instead of making a hidden service object canonical.
- Whether search gains fielded ranking, topic filters, or recency weighting, and whether those ranking rules remain auditable to agents.
- Whether project-local entries grow into cross-repo or organization-level memory, which would require stronger lineage, scoping, and authority rules.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: Gnosis stores repo memory, but behavior changes only when the agent follows doctrine and pulls relevant entries.
- [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) - exemplifies: Gnosis changes repo instructions, shell workflow, source control, and search habits rather than only adding a backend.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: entries, doctrine, host instructions, and search indexes need separate substrate/form/lineage/authority classification.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: Gnosis entries are mainly retained evidence, reference, context, and advice.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: doctrine and host `AGENTS.md` instructions route and instruct future agents.
