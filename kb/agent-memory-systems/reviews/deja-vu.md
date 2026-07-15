---
description: "deja-vu review: local lexical memory over Claude, Codex, and opencode traces with redacted file index, MCP recall, sync/share, and SessionStart auto-recall"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
last-checked: "2026-07-15"
---

# deja-vu

deja-vu, by Vladislav Shulcz, is a Go CLI and stdio MCP server that turns existing Claude Code, Codex CLI, and opencode session histories into local agent memory. At the reviewed commit it parses local harness stores, writes a redacted lexical index under `~/.cache/deja/index.db`, serves search/context/share/stats/sync commands, exposes MCP `recall` and `recall_context` tools, and can install a Claude `SessionStart` hook that injects recent project memories from an already-warm index.

**Repository:** https://github.com/vshulcz/deja-vu

**Reviewed commit:** [c76ece2629683a4a10b861b498c8dab99610e8e2](https://github.com/vshulcz/deja-vu/commit/c76ece2629683a4a10b861b498c8dab99610e8e2)

**Last checked:** 2026-07-15

## Core Ideas

**The memory source is retrospective agent traces, not a new capture API.** The README frames the tool as indexing histories that Claude Code, Codex, and opencode already write, and the parsers implement that literally: Claude and Codex JSONL files become `Session`/`Message` records, while opencode text parts are read from its local SQLite database through the `sqlite3` CLI ([README.md](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/README.md), [internal/sources/claude.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/internal/sources/claude.go), [internal/sources/codex.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/internal/sources/codex.go), [internal/sources/opencode.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/internal/sources/opencode.go), [internal/model/model.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/internal/model/model.go)).

**The durable store is a redacted lexical cache.** The architecture document describes `records.bin`, token bucket files, `manifest.gob`, and `sessions.gob`; the indexer builds those files from parsed sessions, redacts before every record write, and updates incrementally when source files append or change ([docs/ARCHITECTURE.md](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/docs/ARCHITECTURE.md), [internal/index/index.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/internal/index/index.go), [internal/redact/redact.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/internal/redact/redact.go)). Tests assert that common secret forms do not enter `records.bin` and that redaction counts remain visible in the manifest ([internal/index/index_test.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/internal/index/index_test.go)).

**Context efficiency is lexical, bounded, and deliberately shallow.** Search tokenizes the query, intersects postings, expands to substring postings when exact token matches fail, pre-ranks by count and recency, then reads only candidate records; regex search falls back to scanning ([internal/index/index.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/internal/index/index.go), [internal/search/search.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/internal/search/search.go)). Volume controls are explicit: normal output caps hits and snippets, `deja ctx` caps a best-session digest at about 8KB, MCP `recall` caps text near 4KB, and auto-recall caps startup context at 2KB. Complexity is low because there are no embeddings, graph walks, or generated summaries; precision and recall are only as good as lexical overlap and project metadata.

**Read-back has both pull and optional push surfaces.** CLI search, `deja ctx`, `show`, `last`, and the MCP tools are explicit lookup interfaces; `install --auto` additionally writes Claude MCP config and a `SessionStart` hook that runs `deja hook-context` ([cmd/deja/main.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/cmd/deja/main.go), [cmd/deja/mcp.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/cmd/deja/mcp.go), [cmd/deja/install.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/cmd/deja/install.go), [cmd/deja/hook_context.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/cmd/deja/hook_context.go)). The hook is intentionally non-blocking: it reads only an existing manifest, selects up to three recent sessions matching the current project, and returns no output on missing index or errors.

**Sharing and sync preserve the same redacted-trace model.** `deja share` formats a bounded markdown digest and re-applies redaction, while sync export/import writes append-only JSONL batches, tracks export watermarks and import dedupe keys, preserves imported records across rebuilds, and avoids echoing imported records back out ([cmd/deja/share.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/cmd/deja/share.go), [cmd/deja/sync.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/cmd/deja/sync.go), [cmd/deja/sync_ssh.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/cmd/deja/sync_ssh.go), [internal/index/sync.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/internal/index/sync.go), [internal/index/sync_persist_test.go](https://github.com/vshulcz/deja-vu/blob/c76ece2629683a4a10b861b498c8dab99610e8e2/internal/index/sync_persist_test.go)). The README's privacy claim is accurate for indexing and search; explicit `sync ssh` is a network path through system `ssh`/`scp`, not a hidden service.

## Artifact analysis

- **Storage substrate:** `files` — deja-vu's own retained store is a directory of binary records, bucket files, GOB manifests/session metadata, and optional JSONL sync batches. Claude and Codex source traces are files, and opencode's SQLite database is an external source substrate rather than deja-vu's index store.
- **Representational form:** `prose` `symbolic` — Session text, snippets, context digests, share digests, and auto-recall bullets are prose; records, postings, manifests, session metadata, redaction counters, sync watermarks, MCP schemas, installer edits, and hook JSON are symbolic. There is no parametric retrieval state.
- **Lineage:** `authored` `imported` `trace-extracted` — MCP/hook configuration entries are authored by installer commands; sync batches and imported records can be brought from another machine; the core index records, buckets, metadata, stats, and auto-recall digests are derived from agent session traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `ranking` `learning` — Retrieved snippets and digests advise as knowledge artifacts; installed config tells host tools how to expose or call deja-vu; token buckets, project names, filters, and MCP schemas route access; count/recency scoring ranks recall; the trace-derived index is the learned memory surface that changes future read-back. I did not find enforcement gates or semantic validation of recalled claims.

**Harness source traces.** Storage substrate: Claude/Codex JSONL files and the opencode SQLite database. Representational form: prose message text with symbolic session id, harness, project/path, role, and timestamps. Lineage: imported from external agent harness stores that pre-exist deja-vu. Behavioral authority: evidence for search, stats, redaction counts, context digests, sync exports, and auto-recall; the original logs remain outside deja-vu's control.

**Local index cache.** Storage substrate: files under `index.DefaultDir()` (`~/.cache/deja/index.db` unless overridden). Representational form: redacted prose record text plus symbolic offsets, session ordinals, bucket postings, file state, watermarks, imported-record dedupe keys, and source redaction counters. Lineage: trace-extracted from local harness stores and imported sync records, with changed source files invalidating or appending index sections. Behavioral authority: knowledge, routing, ranking, and learning; it determines which prior sessions can be recalled and in what order.

**MCP and hook configuration.** Storage substrate: host config files such as `~/.claude.json`, `~/.codex/config.toml`, opencode JSON/JSONC config, and Claude `settings.json` hooks. Representational form: symbolic configuration pointing at the `deja mcp` server or `deja hook-context` command. Lineage: authored by `deja install`, with `.bak` backups for changed files. Behavioral authority: instruction and routing; these artifacts make host agents expose pull tools or receive startup context.

**Sync batches and imported records.** Storage substrate: JSONL batch files plus imported records retained inside the index with virtual source path `deja-sync-import`. Representational form: prose text with symbolic harness/session/project/role/time metadata. Lineage: imported from another machine's deja-vu export, redacted again on import. Behavioral authority: knowledge and routing; imported sessions become searchable as `imported:<project>` while dedupe and watermarks prevent repeat import and echo export.

**Promotion path.** deja-vu promotes raw harness traces into redacted index records, token buckets, session metadata, search hits, context digests, MCP tool results, and optional Claude startup context. It does not promote traces into durable rules, skills, validators, or enforced policies.

## Comparison with Our System

| Dimension | deja-vu | Commonplace |
|---|---|---|
| Primary purpose | Fast local recall over prior coding-agent sessions | Reviewable methodology KB for agents and maintainers |
| Main substrate | File-backed lexical cache derived from external logs | Typed Markdown collections, schemas, source snapshots, validation reports |
| Canonical retained unit | Redacted session message record plus session metadata/postings | Typed artifact with frontmatter, links, citations, and validation rules |
| Write path | Automatic trace import/index/update/sync when commands run | Deliberate writing, review, validation, and source-grounded promotion |
| Read path | CLI/MCP pull plus optional Claude SessionStart project recall | Mostly pull through `rg`, indexes, links, skills, and review workflows |
| Governance | Redaction, file locks, manifest freshness, dedupe/watermarks, tests | Collection/type contracts, schema validation, git history, semantic review |

deja-vu is much stronger than Commonplace as a low-friction operational recall layer: it does not ask agents or users to write notes, and it turns already-paid-for session history into a useful local memory index. Commonplace is stronger where retained claims need reviewable meaning: its promoted artifacts have types, links, citations, validation, and human-readable source control instead of binary postings over transcripts.

The sharpest divergence is authority. deja-vu makes prior traces easy to find and, with the Claude hook, easy to push into context, but it keeps those traces as recalled evidence. Commonplace promotes only selected, reviewed content into durable knowledge or system-definition artifacts. deja-vu optimizes reuse speed; Commonplace optimizes claim discipline.

### Borrowable Ideas

**Redact before indexing and again before export.** Ready now. Commonplace source snapshots and review artifacts could borrow the double-pass pattern for any trace or transcript ingestion that might contain credentials.

**Keep auto-recall read-only and non-blocking.** Ready with a concrete hook. The `hook-context` design is a useful shape for optional startup context: read a warm index, cap output, return nothing on failure, and never delay the host agent.

**Separate disposable access structures from retained evidence.** Ready now. deja-vu treats records and buckets as rebuildable cache over original logs, while preserving sync-imported records that otherwise have no local source. Commonplace should keep that distinction clear if it adds high-volume trace indexes.

**Use project identifiers for cheap targeted push.** Needs a Commonplace use case. Project-scoped startup recall is weaker than semantic relevance, but it is cheap and explainable when the current path is a reliable symbol.

**Do not confuse fast recall with curated memory.** Ready as a constraint. deja-vu's trace-derived memory is useful precisely because it stays at the evidence/retrieval layer rather than auto-promoting repeated snippets into rules.

## Write side

**Write agency:** `automatic` — User commands trigger the workflows, but the memory store changes by automatic parsing, redaction, indexing, manifest update, sync import, and export-watermark maintenance over existing session traces. I did not find a deja-vu interface for manually authoring or editing memory entries.

**Curation operations:** `none` — The automatic path acquires/imports traces, tokenizes them, redacts them, ranks them at read time, and deduplicates sync imports by record key. It does not consolidate, evolve, synthesize, invalidate, decay, or promote already-stored memory content.

### Trace-derived learning

**Trace source:** `session-logs` — Claude Code, Codex CLI, and opencode conversation histories are the raw trace sources. The code extracts text-bearing messages/parts, not a rich typed model of tool events.

**Learning scope:** `per-project` `cross-task` — The index spans multiple harnesses and projects for cross-task search, while project metadata scopes filters and Claude startup recall.

**Learning timing:** `staged` — Indexing happens when commands such as search, warmup, stats, sync export, or MCP recall ensure the cache; the Claude hook intentionally reads only an already-warm index.

**Distilled form:** `prose` `symbolic` — Raw conversations become redacted prose records and context digests plus symbolic postings, metadata, watermarks, redaction counters, and host config entries.

**Extraction.** The extraction oracle is mechanical: source parsers select text messages, redaction rewrites secret values, index code tokenizes text into bucket postings, and search ranks matches by count and recency. There is no LLM judge deciding whether a trace became a lesson, no abstraction pass over multiple sessions, and no quality check that a recalled conclusion is still true.

**Scope and timing.** The learning unit is a session message record. Freshness is tied to source file size/mtime, index version, scope, and opencode updated timestamps; append-only changes can add records without a full rebuild, while removed or non-append changes rewrite affected state. Sync imports are retained inside the index and replayed across rebuilds because their source batch may no longer be present locally.

**Survey placement.** deja-vu sits in the trace-to-search and trace-to-startup-context family. It strengthens the survey claim that trace-derived learning need not synthesize rules to be useful: exact prior sessions, redacted and cheaply ranked, can be enough to alter future work. It weakens any broad claim that "agent memory" must involve embeddings, summaries, or model calls.

## Read-back

**Read-back:** `both` — Search, `ctx`, `show`, `last`, share, stats, and MCP recall are pull surfaces; an installed Claude `SessionStart` hook can push recent project sessions into the agent's context without a fresh agent lookup.

**Read-back signal:** `identifier` — The push path derives current project names from `CLAUDE_PROJECT_DIR` or `cwd`, then selects recent sessions whose stored project metadata matches those identifiers. It does not infer relevance from the current prompt content.

**Faithfulness tested:** `no` — Tests cover MCP output, installer idempotence, hook JSON shape, digest caps, redaction, and sync persistence, but I did not find a with/without ablation or post-action audit showing that agents reliably use pushed or pulled memories.

**Direction edge cases.** MCP recall and `deja ctx` remain pull even when a host agent calls them through a tool: the agent or user requested a query. The Claude hook is push from the agent's perspective because the host invokes it on session start and injects `additionalContext` before the user asks a memory question.

**Targeting and signal.** Pull retrieval is inferred lexical matching over query tokens or regex. Push retrieval is identifier-targeted by project name and recency: `hookDigest()` asks the index for up to three recent sessions for each candidate project name, deduplicates by harness/session id, sorts by update time, and formats a 2KB digest.

**Injection point.** CLI and MCP reads serve memory before whichever prompt or tool result consumes them. The Claude auto-recall hook returns a `SessionStart` response containing `additionalContext`; no later post-action read-back exists. Index updates, redaction, and sync import/export are write-side maintenance for future reads.

**Selection, scope, and complexity.** Normal search caps displayed hits and snippets; `recall` defaults to five hits within about 4KB; `recall_context` and `ctx` return an 8KB best-session digest; `hook-context` caps at three sessions and 2KB. Selection is shallow but predictable: lexical match, project filter, harness filter, since/role filters, count, and recency.

**Authority at consumption.** Recalled sessions are advisory evidence. MCP schemas route tool calls, and installed host config makes recall available or startup context automatic, but deja-vu does not enforce behavior or validate that old conclusions should be followed.

**Other consumers.** Humans can use the same memory through CLI search, show, last, ctx, share, stats, sources, sync, and direct inspection of the original harness logs. The binary index is less inspectable than source logs, but the source logs remain the authority for full context.

## Curiosity Pass

The `index.db` name is slightly misleading: deja-vu's own index is not SQLite, but a directory of binary files and GOB metadata. SQLite appears only as an opencode source store read through the local `sqlite3` command.

The auto-recall hook is intentionally weaker than the README phrase "relevant memory lands in context" can sound. It does not search the current prompt; it injects recent sessions from the current project if, and only if, a warm index already exists.

"No models" is both the adoption advantage and the quality ceiling. The system cannot hallucinate a summary, but it also cannot bridge vocabulary gaps except by substring matching and whatever words the old session happened to contain.

The privacy story is local by default, but sync is deliberately an escape hatch. `sync export` writes redacted batches to a directory, and `sync ssh` moves them over system SSH/SCP; operators still own the transport and destination trust boundary.

## What to Watch

- Whether planned project exclusion lands; without it, broad indexing can create privacy and noise problems in sensitive repositories.
- Whether aider or Gemini parser support is added; parser breadth is the main way deja-vu grows memory coverage without changing its architecture.
- Whether auto-recall expands beyond Claude `SessionStart`; Codex or opencode startup push would change deployed read-back even if the index stays the same.
- Whether the system adds summarization, clustering, or rule extraction; that would move it from trace-to-recall toward trace-to-policy and require stronger review/validation.
- Whether sync gains encryption or access-control affordances; redaction reduces risk but does not make shared trace batches harmless.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes deja-vu's stored index from pull recall and the optional Claude startup push.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - contrasts with deja-vu's trace-derived recall, which does not promote traces into durable instructions.
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places deja-vu in trace-to-search and trace-to-startup-context rather than trace-to-policy.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies recalled snippets, context digests, shares, and imported sessions as advisory evidence.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies installed MCP and hook configuration as behavior-shaping routing/instruction surfaces.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains why auto-recall's targeted push depends on project-name identifiers being available and reliable.
