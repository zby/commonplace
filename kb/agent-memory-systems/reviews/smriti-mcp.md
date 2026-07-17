---
description: "Smriti-MCP review: MCP markdown memory server with file-backed notes, lexical recall, traces, salience, wikilinks, and agent-mediated consolidation"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-18"
tags: [trace-learning]
---

# Smriti-MCP

Smriti-MCP, by Deepak Bhardwaj, is a Python MCP server and CLI for durable agent memory in Markdown files with YAML frontmatter. At the reviewed commit it exposes tools for CRUD, search, recall bundles, raw trace recording, trace consolidation, supersession, frontmatter repair, wikilink repair, health review, and generated indexes; the store is local files rather than a database or hosted memory service.

**Repository:** https://github.com/deepak-bhardwaj-ps/smriti-mcp

**Reviewed commit:** [012d89fc922560505426ddc5992b8b90673671a1](https://github.com/deepak-bhardwaj-ps/smriti-mcp/commit/012d89fc922560505426ddc5992b8b90673671a1)

**Last checked:** 2026-06-18

## Core Ideas

**The memory store is an ordinary Markdown tree.** `MemoryStore` resolves a root, creates it if needed, and stores each memory as `<category>/<title>.md` by default, with YAML frontmatter carrying ids, tags, status, source agent, scope, salience, confidence, supersession, timestamps, and other recall metadata ([src/smriti_mcp/store.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/src/smriti_mcp/store.py), [README.md](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/README.md)). That keeps adoption simple: users can inspect, edit, back up, and version the memory files outside the MCP runtime.

**The MCP server exposes memory as explicit tools, not an always-on agent loop.** `create_server` registers tools for creating, reading, appending, updating, archiving, deleting, listing, searching, recalling context, marking access, recording traces, suggesting consolidation, consolidating, superseding, reviewing health, rebuilding, and loading indexes ([src/smriti_mcp/server.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/src/smriti_mcp/server.py), [tests/test_smriti_mcp_server.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/tests/test_smriti_mcp_server.py)). The package does not install host hooks or inject memory without a client invoking the tools.

**Context efficiency is lexical, scoped, and budgeted.** `search_memory` ranks title, aliases, tags, path, short description, body term frequency, exact phrase matches, backlinks, salience, access count, confidence, status, expiry, memory type, and source agent; it can omit full content and return snippets only. `recall_context` builds a compact Markdown bundle grouped by `memory_type`, follows wikilinks/backlinks optionally, excludes archived and superseded memories by default, and stops when an approximate word budget is reached ([src/smriti_mcp/store.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/src/smriti_mcp/store.py), [tests/test_smriti_store.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/tests/test_smriti_store.py)). It controls volume better than complexity: there is no embedding layer, semantic summarizer, or progressive file-reading ladder beyond snippets and recall summaries.

**Trace capture is first-class but distillation is deliberately agent-mediated.** `record_trace` appends NDJSON events under `.smriti/traces/<date>/<agent>.ndjson`; `remember` writes or appends a durable memory and records a `remembered` trace; `suggest_consolidation` groups raw traces and recommends review/create/update actions; `consolidate_memory` writes agent-supplied consolidated content and stores `trace:<id>` provenance in metadata ([src/smriti_mcp/store.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/src/smriti_mcp/store.py), [src/smriti_mcp/server.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/src/smriti_mcp/server.py)). Smriti keeps the trace pipeline visible, but it does not summarize traces itself.

**Relationship and maintenance features are symbolic and local.** Wikilinks are parsed into links/backlinks for ranking and recall expansion, `rebuild_memory` can fix frontmatter, add or normalize title/alias wikilinks, and rebuild `index.md` plus `index.yaml`, and `review_memory_health` reports duplicate titles, stale active notes, oversized notes, and unresolved links without mutating files ([src/smriti_mcp/store.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/src/smriti_mcp/store.py), [src/smriti_mcp/fix_frontmatter.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/src/smriti_mcp/fix_frontmatter.py)). Trust comes from inspectability and deterministic repair, not from review gates or proof obligations.

## Artifact analysis

- **Storage substrate:** `files` `in-memory` — Durable state is Markdown notes, `.smriti/traces/*.ndjson`, `index.md`, and `index.yaml` under the memory root; scan, search, recall, health, and wikilink candidate indexes are rebuilt in memory from those files when operations run.
- **Representational form:** `prose` `symbolic` — Memory bodies, recall bundles, snippets, and generated index lines are prose; YAML frontmatter, ids, categories, tags, status, scope, source metadata, trace NDJSON, wikilinks, links/backlinks, access counts, salience, health reports, MCP tool schemas, and machine index YAML are symbolic. The inspected code does not implement embeddings, model weights, or another parametric retained form.
- **Lineage:** `authored` `imported` `trace-extracted` — Users and agents author memories through MCP/CLI/API calls or direct file edits; existing Markdown files can be imported into the scan/rebuild/index path if frontmatter is present or repairable; raw trace events and agent-supplied consolidated memories with `trace:<id>` sources form a trace-extracted lineage.
- **Behavioral authority:** `knowledge` `routing` `validation` `ranking` `learning` — Notes and recall bundles advise agents as knowledge; categories, ids, scope, tags, aliases, wikilinks, and generated indexes route browsing and lookup; frontmatter repair, path traversal checks, metadata normalization, health review, and malformed-note skipping validate structure; lexical scores, backlinks, salience, access count, confidence, status, expiry, and exact matches rank recall; trace recording, consolidation provenance, access reinforcement, and remember-mode matching learn from interaction events enough to influence future recall.

**Memory Markdown files.** Each file combines a prose body with frontmatter metadata. The prose is the human/agent-facing recollection; the metadata is the routing, filtering, ranking, lifecycle, provenance, and governance surface consumed by list/search/recall/rebuild/health operations ([src/smriti_mcp/store.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/src/smriti_mcp/store.py), [src/smriti_mcp/frontmatter.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/src/smriti_mcp/frontmatter.py)).

**Trace logs.** Raw traces are append-only NDJSON files below `.smriti/traces`; they store event id, timestamp, type, agent, linked memory id, salience, scope, content, and metadata. As raw traces they are knowledge artifacts and provenance; they gain stronger future-action authority only when an agent consolidates them into Markdown memory or when `suggest_consolidation` recommends create/update actions ([src/smriti_mcp/store.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/src/smriti_mcp/store.py)).

**Derived access structures.** `index.md` is a human-readable browse surface and `index.yaml` is a machine index containing notes, aliases, links, backlinks, and terms. Both are derived from current Markdown files; they can be regenerated and should not be treated as the source of truth ([src/smriti_mcp/store.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/src/smriti_mcp/store.py)).

**MCP tool schemas and descriptions.** Pydantic models define the write, search, recall, trace, consolidation, and maintenance interface exposed to clients. These schemas are system-definition artifacts for client behavior because they tell agents which metadata exists and when to use each tool, but they do not enforce semantic quality of the remembered claims ([src/smriti_mcp/server.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/src/smriti_mcp/server.py)).

**Promotion path.** Smriti can promote plain Markdown into structured memory by adding required frontmatter, aliases, wikilinks, generated indexes, access metadata, salience, trace provenance, and supersession metadata. It cannot promote a memory into an enforced validator, host instruction, or automatically reviewed rule; stronger authority depends on the calling agent or user.

## Comparison with Our System

Smriti-MCP and Commonplace share a file-first bet: durable memory should be inspectable, editable, and versionable without a hosted service or opaque database. Both use Markdown plus YAML metadata, links, generated indexes, and command/tool surfaces that agents can call.

The divergence is in artifact contracts and governance. Smriti gives agents a general-purpose memory API with broad metadata fields and deterministic maintenance helpers. Commonplace gives agents collection contracts, type specs, validation, review gates, source-citation discipline, and curated navigation. Smriti is easier to drop into any MCP-compatible client; Commonplace gives each retained artifact a narrower role and higher review burden before it shapes future work.

The trace pipeline is also weaker but simpler than Commonplace's review workflows. Smriti records raw traces and supports agent-mediated consolidation, but the extraction oracle is outside the package. Commonplace's review and note workflows are heavier, but they make more of the judgment and validation process explicit in retained artifacts.

### Borrowable Ideas

**A small `recall_context` bundle format.** Ready as a tool-shaping idea. Commonplace could expose a deterministic "recall bundle" command that groups selected notes by type and respects a token budget, while preserving the existing `rg`/index/link workflow for deeper inspection.

**Access reinforcement as metadata, not hidden telemetry.** Needs a concrete use case. Smriti's `last_accessed_at`, `access_count`, and salience bump are transparent frontmatter changes; Commonplace could use a reviewable variant for workshop artifacts or temporary run state, but automatic salience changes in library notes would need governance.

**Trace suggestions before consolidation.** Ready for the workshop layer. Smriti's separation of raw trace logging, grouping suggestions, and agent-supplied consolidation is a safer pattern than autonomous summarization for Commonplace: collect candidates first, then require an authored note or review artifact.

**Health review as a read-only tool.** Ready now. The duplicate/stale/oversized/unresolved-link report is useful because it does not mutate the store; Commonplace already has validation, but similar cheap health summaries for workshops or review backlogs would fit.

**Do not borrow undifferentiated memory metadata into library notes.** Smriti's flexible fields are useful for general MCP memory, but Commonplace should keep collection-specific type contracts rather than adding broad optional memory fields everywhere.

## Write side

**Write agency:** `manual` `automatic` — Humans or agents explicitly create, append, update, archive, delete, consolidate, supersede, rebuild, and repair memories through tools or file edits; automatic behavior inside those calls includes deterministic remember-mode append selection, raw trace recording, recall-time access/salience updates, generated index rebuilds, frontmatter repair, and wikilink insertion/normalization.

**Curation operations:** `evolve` `promote` — `remember` can append a new observation to a strongly matching existing memory, `rebuild_memory` can add or normalize wikilinks and frontmatter, and `mark_accessed` changes access count, timestamp, and salience; explicit update, consolidation, and supersession tools can replace or supersede memories, but those are caller-directed writes rather than autonomous curation. Salience and access count promote recalled memories for later ranking.

### Trace-learning

**Trace source:** `event-streams` — The trace source is not an automatically captured shell or tool transcript; it is an MCP/API event stream that clients call through `record_trace`, `remember`, and `consolidate_memory`.

**Extraction.** Raw traces are grouped by normalized leading content terms, filtered by scope/agent/since, and paired with related memories through lexical search. The actual distilled memory body is supplied by the calling agent or user through `consolidate_memory`; Smriti records `trace:<id>` sources and a follow-up `consolidated` trace, but does not summarize, judge, or validate the trace content itself ([src/smriti_mcp/store.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/src/smriti_mcp/store.py), [src/smriti_mcp/server.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/src/smriti_mcp/server.py)).

**Learning scope:** `per-project` `cross-task` — Scope is an open metadata object, commonly project or repository scoped, and the default memory root can also accumulate memories across clients, sessions, and tasks.

**Learning timing:** `online` `staged` — `remember` and `record_trace` write online during agent use; `suggest_consolidation` and `consolidate_memory` are staged review-and-promotion steps.

**Distilled form:** `prose` `symbolic` — Consolidated outputs are Markdown prose plus symbolic metadata, trace sources, ids, tags, scope, status, salience, and links. There is no parametric learned state in the inspected code.

**Survey placement.** Smriti-MCP is a lightweight trace-derived memory system with manual/agent-mediated distillation: it strengthens the survey distinction between raw trace retention and distilled behavior-shaping memory, while showing a conservative design point where the package provides trace plumbing and provenance but leaves the summarizing oracle outside the memory server.

## Read-back

**Read-back:** `pull` — Stored memory reaches an agent only when the client, user, or agent calls `get_memory`, `search_memory`, `list_memories`, `recall_context`, `load_memory_index`, or related tools. The inspected package does not install hooks, run a daemon that watches prompts, or push memory into the model context on its own.

Selection is lexical and metadata-driven. Search and recall key on normalized content terms, exact phrase matches, title, aliases, tags, path/id, short description, backlinks, salience, access count, confidence, status, expiry, memory type, source agent, scope, and optional wikilink/backlink expansion. Recall returns compact summaries grouped by memory type under a token budget rather than full files by default ([src/smriti_mcp/store.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/src/smriti_mcp/store.py)).

At consumption, recalled content is advisory knowledge. The MCP server's own instructions tell clients Smriti is for durable memory, but ordinary memories are not distinguished as host instructions or hard gates, and the implementation does not test whether retrieved memories changed downstream agent behavior.

## Curiosity Pass

**The strongest design choice is restraint.** Smriti exposes traces and consolidation without pretending to solve summarization or truth maintenance. That makes the system less autonomous than many memory frameworks, but the resulting provenance boundary is easy to understand.

**`remember` is both convenient and narrow.** Auto mode only appends on a strong title match after search; weak lexical overlap creates a new note. That avoids some accidental merges, but it means semantic deduplication is intentionally absent ([src/smriti_mcp/store.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/src/smriti_mcp/store.py), [tests/test_smriti_store.py](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/tests/test_smriti_store.py)).

**Read-back mutates the store.** `recall_context` defaults `mark_accessed=True`, so a pull read can reinforce access count and salience. That is useful for ranking, but it couples inspection with future recall unless a caller disables it.

**Health review stops short of repair.** `review_memory_health` reports duplicates, stale notes, oversized notes, and unresolved links, while `rebuild_memory` handles frontmatter and wikilinks. The split is sensible: quality judgments are surfaced before the system makes semantic changes.

**The roadmap names embeddings, but the code remains lexical.** The README lists memory embeddings for semantic search as future work; at this commit retrieval is inspectable lexical/scoring code, not vector search ([README.md](https://github.com/deepak-bhardwaj-ps/smriti-mcp/blob/012d89fc922560505426ddc5992b8b90673671a1/README.md)).

## What to Watch

- Whether Smriti adds automatic host hooks or prompt-time recall; that would change read-back from pull-only to push or both and would require signal/faithfulness analysis.
- Whether embeddings are implemented from the roadmap; that would add a parametric access structure and a less directly inspectable ranking layer.
- Whether `suggest_consolidation` grows an internal summarizer or judge; that would strengthen trace-learning but would also require provenance and quality controls.
- Whether health review gains automatic deduplication, stale invalidation, or oversized-note consolidation; those would add stronger curation operations over already-stored memories.
- Whether the package adds typed memory classes with validation beyond flexible metadata; that would move it closer to Commonplace-style artifact contracts.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes Smriti's durable Markdown store from its explicit pull-only MCP read-back.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - supports separating notes, frontmatter, trace logs, indexes, MCP schemas, and recall bundles by substrate, form, lineage, and authority.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - frames Smriti's trace log plus reviewed consolidation path as a conservative trace-learning loop.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies ordinary memories, raw traces, snippets, indexes, and recall bundles as advisory retained knowledge.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - contrasts Smriti's MCP schemas, repair routines, and ranking policy with stronger instruction, validation, or enforcement artifacts.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - relates to Smriti's reliance on titles, aliases, tags, categories, scopes, wikilinks, and lexical terms as recall symbols.
