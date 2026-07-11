---
description: "Eidetic review: Claude Code Markdown memory with hook-pushed context, FTS/vector recall, trace capture, compounding, drift penalties, and vault export"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-18"
tags: [trace-derived]
---

# Eidetic

Eidetic, by LARIkoz, is a Claude Code long-term memory layer built from Markdown memory cards, Claude hooks, generated rules context, SQLite FTS indexes, optional vector embeddings, and an optional MCP server for non-hook hosts. At the reviewed commit it auto-injects bounded memory into Claude Code sessions, extracts session-end signals from transcripts, compounds related memories instead of always creating new cards, discounts agent-extracted memories, and flags stale or broken memory through drift diagnostics.

**Repository:** https://github.com/LARIkoz/eidetic

**Reviewed commit:** [7e152876dc87319cb2d864aefba540e986f335fe](https://github.com/LARIkoz/eidetic/commit/7e152876dc87319cb2d864aefba540e986f335fe)

**Source directory:** `related-systems/LARIkoz--eidetic`

## Core Ideas

**Markdown cards are the durable memory; indexes are rebuildable access structures.** Eidetic's schema defines one memory card as a Markdown file with YAML frontmatter plus body, and the indexer parses those files into `memory_chunks` rows and FTS5 triggers ([docs/MEMORY-SCHEMA.md](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/docs/MEMORY-SCHEMA.md), [bin/index_impl.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/bin/index_impl.py)). This is file-first memory in practice: SQLite is operational state, not the authored source of truth.

**Context efficiency is hook-pushed and budgeted.** On SessionStart, `smart-memory-inject.sh` reindexes, runs drift checks, optionally indexes code and vectors, then calls `assemble_context.py` to write `~/.claude/rules/memory-context.md`, which Claude Code auto-loads ([hooks/smart-memory-inject.sh](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/hooks/smart-memory-inject.sh), [bin/assemble_context.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/bin/assemble_context.py)). The assembler uses a fixed character budget, reserves ratios for feedback/project/recent context, clusters known rule families, and progressively shortens lower-ranked rules rather than dumping every card in full.

**Trust is encoded as ranking, not just prose.** Search and injection multiply retrieval relevance by evidence tier, source tier, freshness or drift penalty, and lifecycle status; constants put `agent-extracted` at half weight and `imported` lower still ([bin/constants.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/bin/constants.py), [bin/search_impl.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/bin/search_impl.py), [tests/test_ranking_weights.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/tests/test_ranking_weights.py)). That makes provenance and lifecycle metadata behavior-shaping, not only descriptive.

**Drift detection treats old memory as a live hazard.** `drift_check.py` detects broken wikilinks, age staleness, and confidence escalation from repeated agent-extracted updates, writes findings to a separate `drift_state.db`, auto-resolves disappeared findings, and feeds penalties back into search/context assembly ([bin/drift_check.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/bin/drift_check.py), [bin/assemble_context.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/bin/assemble_context.py)). It does not yet implement semantic contradiction detection; the source comments explicitly place automated contradiction detection in future work.

**Write paths converge on compounding.** Session-end signal capture and manual promotion both search before writing: matching memory cards get a `History` or `Update` section; otherwise Eidetic creates a new typed card ([hooks/session-signals.sh](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/hooks/session-signals.sh), [bin/compound.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/bin/compound.py), [bin/remember.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/bin/remember.py)). This is not just capture; it is an explicit anti-duplication maintenance path.

**Adoption affordances are strong for Claude Code, acceptable elsewhere.** Claude Code gets installer-managed SessionStart, Stop, PostToolUse, and rules-file integration; other agents can use an stdlib MCP server exposing search, detail, serendipity, health, reindex, lint, and vault export tools ([install.sh](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/install.sh), [mcp_server.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/mcp_server.py)). The core works without Python packages beyond stdlib/sqlite; vector and code search add optional dependencies.

## Artifact analysis

- **Storage substrate:** `files` `sqlite` `vector` — Canonical memory persists as Markdown files under Claude memory directories and generated rules files; SQLite stores FTS chunks, session counters, drift findings, lifecycle JSONL-adjacent state, and vector embeddings; the optional vector layer is a derived `vectors.db` over memory chunks.
- **Representational form:** `prose` `symbolic` `parametric` — Card bodies, descriptions, histories, updates, rules context, and signal text are prose; frontmatter fields, card kinds, lifecycle statuses, wikilinks, hook settings, MCP schemas, FTS tables, drift rows, detail ids, and op-log entries are symbolic; e5 embeddings and cross-encoder scores are parametric retrieval state.
- **Lineage:** `authored` `imported` `trace-extracted` — Humans and agents author cards directly or through `remember.py`; code index chunks are imported from project source files into the same search table; Stop-hook signal cards are trace-extracted from Claude transcript excerpts, and lifecycle event JSONL records are derived from tool-use hook payloads.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Cards and search results advise later work; injected feedback rules and generated `memory-context.md` instruct Claude Code; project slugs, card kinds, detail ids, hooks, MCP tools, and search filters route access; lint, doctor, schema expectations, protected-card guards, and drift checks validate or warn; evidence/source/freshness/status/vector/FTS scores rank retrieval; transcript-derived signals and promotions update the store for future sessions.

**Memory cards.** The central retained artifact is a Markdown card. Its prose body carries remembered knowledge or behavioral guidance, while frontmatter fields such as `type`, `card_kind`, `evidence`, `source`, `last_verified`, `status`, and supersession fields become search, ranking, drift, and export controls ([docs/MEMORY-SCHEMA.md](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/docs/MEMORY-SCHEMA.md), [bin/index_impl.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/bin/index_impl.py)).

**Generated memory context.** `memory-context.md` is a system-definition artifact produced from indexed memory. It is not canonical memory; it is a compiled prompt surface with drift diagnostics, behavioral rules, fresh handoff, project context, recent cross-project memory, and session awareness ([bin/assemble_context.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/bin/assemble_context.py), [hooks/smart-memory-inject.sh](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/hooks/smart-memory-inject.sh)).

**Derived indexes and drift state.** `index.db`, `vectors.db`, and `drift_state.db` are derived access and quality structures. Edits to Markdown cards invalidate rows by mtime/content hash; vector search suppresses mismatched model, dimension, or hash-scheme state rather than silently returning bad semantic hits ([bin/index_impl.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/bin/index_impl.py), [bin/embed.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/bin/embed.py), [bin/drift_check.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/bin/drift_check.py)).

**Hook and MCP surfaces.** Claude hooks are authored system-definition artifacts that decide when memory is pushed, captured, or logged. The MCP server wraps the same store as pull tools with structured payloads, `no_confident_results`, stable detail ids, and bounded limits ([install.sh](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/install.sh), [mcp_server.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/mcp_server.py), [tests/test_progressive_search.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/tests/test_progressive_search.py)).

**Vault export.** The Obsidian vault is a human-facing projection, not a read-back substrate for the agent. `export_vault.py` applies a quality gate, folders cards by type, rewrites them into a browseable vault, and may optionally run polish/synthesis, but the README states the vault is not read back by search/injection ([README.md](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/README.md), [bin/export_vault.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/bin/export_vault.py)).

Promotion path: authored or trace-extracted prose can become a typed Markdown card, then an indexed SQLite row, then ranked search result or compiled injected rule/context. Drift can down-rank or warn on that card, but it does not automatically promote a weak memory into a stronger validated artifact; human verification remains encoded through metadata.

## Comparison with Our System

Eidetic and Commonplace share the file-first premise: durable knowledge should be inspectable as Markdown, with generated indexes treated as subordinate. Both systems also use explicit type metadata, validation/health checks, lifecycle status, and generated access structures.

The divergence is where authority sits. Eidetic optimizes for runtime continuity in Claude Code: hooks assemble context, transcript signals write back automatically, and ranking metadata decides which memories are likely safe enough to use. Commonplace optimizes for reviewed knowledge artifacts: collection contracts, type specs, citations, semantic gates, and git history make durable claims slower to enter but easier to audit.

Eidetic is stronger as a personal operational memory surface. It has real push read-back, search-before-write compounding, code-aware recall, degraded-but-working core dependencies, and drift penalties tied directly into retrieval. Commonplace is stronger where memory needs source-grounded public rationale: it does not let an LLM transcript silently become methodology without review, and it keeps system-definition artifacts in the repository rather than generated user-local rules files.

The main tradeoff is safety versus immediacy. Eidetic's automatic trace loop can preserve useful decisions before they disappear, but its extraction oracle is an LLM call filtered by prefix and then trusted as `agent-extracted` memory. The 0.5x discount and drift checks help, but they are not equivalent to a retained review rationale.

### Borrowable Ideas

**Self-referential discount as a ranking primitive.** Commonplace could mark agent-drafted or trace-derived candidate notes with lower retrieval/ranking priority until reviewed. Ready for generated indexes or future search, not for authored Markdown semantics alone.

**Drift findings as retrieval penalties.** Broken links, stale verification dates, and confidence escalation are useful as machine-readable warnings that affect context assembly. Ready for validation/reporting; automatic down-ranking needs a serving layer.

**Compiled start-of-session brief with explicit budgets.** Eidetic's `memory-context.md` is a concrete pattern for bounded push context. Commonplace could generate task/review briefs from indexes and recent work, but should keep citations and artifact types visible.

**Search-before-write compounding.** `remember.py` and `compound.py` show a pragmatic anti-duplication write path. Commonplace already checks duplicates during note writing; a stronger candidate-update path would need review gates before mutating durable notes.

**Structured no-confident-results contract.** Programmatic consumers benefit from an explicit `no_confident_results` flag rather than treating weak candidates as memory. Ready for any future Commonplace search API.

**Do not borrow transcript extraction as direct library promotion.** The useful part is candidate capture; durable Commonplace artifacts should still require source grounding and review before becoming library knowledge.

## Write side

**Write agency:** `manual` `automatic` — Manual writes happen through direct Markdown authoring, `remember.py` promotion, MCP-triggered reindex/lint/export actions, and human edits; automatic writes include SessionStart index/context/drift/vector updates, Stop-hook transcript signal extraction and compounding, lifecycle event JSONL appends, op-log appends, code indexing, vector embedding maintenance, and vault export.

**Curation operations:** `consolidate` `dedup` `evolve` `promote` — Signal compounding appends new trace evidence into an existing card instead of creating a duplicate; promotion reuses same-slug cards and appends `## Update`; generated context consolidates ranked memory into a smaller rules/context surface; drift checks and indexing evolve derived state around existing cards; promotion changes a good answer from transient chat output into a typed memory card.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` — `session-signals.sh` reads the Claude Code transcript path from hook JSON, extracts recent user/assistant transcript lines, sends a bounded prompt to Claude or Codex, filters only `Decision:/Rule:/Worked:/Failed:/Knowledge:` lines, and pipes them to `compound.py`. `lifecycle_signals.py` separately records bounded metadata-only PostToolUse and PostToolUseFailure events for writes, edits, bash commands, and tool failures.

**Extraction.** The transcript extraction oracle is an LLM runner with a strict prompt and a prefix filter; code then normalizes only contract-shaped signal lines. Compounding uses FTS keywords to choose an existing memory card, refuses to mutate protected `feedback` or `user` cards, appends to `## History` when matched, or creates a dated `signals/<date>.md` card with `source: agent-extracted` when not matched ([hooks/session-signals.sh](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/hooks/session-signals.sh), [bin/compound.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/bin/compound.py)).

**Learning scope:** `per-project` `cross-task` — Project memory directories and cwd-derived project slugs route writes and read-back; the same indexed memory can affect later sessions and tasks in the project, with recent cross-project context also eligible for injection.

**Learning timing:** `online` `staged` — SessionStart read-back and indexing happen online at session start; Stop-hook extraction runs asynchronously at session end; vector/index rebuilds, lint, doctor, vault export, and manual promotion are staged operations.

**Distilled form:** `prose` `symbolic` `parametric` — Trace-derived signals become prose bullets/history entries plus symbolic frontmatter, names, statuses, project paths, op-log entries, and index rows; later vector embedding turns those chunks into parametric retrieval state.

Relative to the trace-derived survey, Eidetic is a trace-to-operational-memory system: transcripts produce low-trust knowledge artifacts that can later be pushed as context or pulled by search. It strengthens the survey's distinction between extraction and trust: the system learns from traces, but it deliberately discounts that lineage instead of pretending extracted memory is verified.

## Read-back

**Read-back:** `both` — Claude Code SessionStart pushes an assembled `memory-context.md` rules file into the agent's auto-loaded context, while `/memory-recall`, `search.sh`, `search_impl.py`, `memory_search`, `memory_search_detail`, and `memory_serendipity` are explicit pull interfaces.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / embedding` — The hook fires on a coarse session-start lifecycle event, then selects by project slug, memory type, card kind, lifecycle status, recency, and drift state; pull search uses FTS keyword matching, optional vector similarity, RRF merge, and cross-encoder salvage.

**Faithfulness tested:** `no` — The repository has regression tests for ranking weights, progressive search, lifecycle capture, promotion/op-log behavior, content hashes, and recall smoke cases, but I did not find with/without-memory ablations or post-action audits proving that injected memory changes model behavior faithfully ([bin/recall_smoke.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/bin/recall_smoke.py), [tests/test_progressive_search.py](https://github.com/LARIkoz/eidetic/blob/7e152876dc87319cb2d864aefba540e986f335fe/tests/test_progressive_search.py)).

The main injection point is pre-invocation: SessionStart writes `~/.claude/rules/memory-context.md` before the session begins. The Stop hook is write-side maintenance after the session, not read-back. MCP clients get capability but not deployed push unless their host separately calls the tools and injects results.

Selection and complexity are unusually explicit for a hook-based system. Feedback rules are treated as always-apply, project context is cwd-scoped, recent cross-project memory is capped, broad search defaults to compact output, detail ids fetch full content only after a candidate is selected, and vector-only results in the ambiguous e5 band are withheld from medium confidence without a second signal.

Authority at consumption is mixed. Injected `type=feedback` rules are instruction-like in Claude Code's rules channel; project/recent memories and drift diagnostics are advisory context; MCP search results are advisory unless the host agent upgrades them. Effective compliance is not verified from code.

Other consumers include humans using the Markdown files, the generated Obsidian vault, doctor/lint output, and op-log timeline. Those surfaces improve auditability, but only the memory cards and derived indexes drive agent recall.

## Curiosity Pass

Eidetic's strongest idea is not vector search; it is making memory trust part of the score. Evidence, source, drift, and status directly affect what reaches context, so provenance is operational.

The automatic learning loop is intentionally modest. It captures bounded transcript signals, but the durable artifact is still a low-trust Markdown card or history entry. That restraint is a design feature, not a weakness.

Lifecycle event capture looks like trace infrastructure but is not yet a visible recall path in the inspected code. It records privacy-preserving metadata and has cleanup tests, but I did not find code that distills those events into memory cards or uses them in read-back.

Drift detection is more concrete than most file-first systems, but it is not truth maintenance. Broken links, age, and confidence escalation are useful warning signals; contradiction detection and typed supersession edges are still future/planned.

The generated rules-file push is powerful and risky. It solves the "memory exists but is not activated" problem, but if the assembly policy is wrong, the agent gets stale or noisy instructions before it has a chance to ask.

## What to Watch

- Whether v6 implements typed supersession and contradiction detection; that would move Eidetic from ranking penalties toward real truth-maintenance authority.
- Whether lifecycle JSONL events become an input to synthesis, decay, or project-state updates; that would broaden trace-derived learning beyond transcript signal extraction.
- Whether importers become implemented code rather than schema/readiness paths; that would make `imported` lineage a real acquisition channel with provenance spans.
- Whether the hook-pushed context starts using semantic/vector selection rather than mostly project/type/recency/ranking assembly; that would increase inferred push and context-dilution risk.
- Whether faithfulness tests appear for injected rules/context; that would make Eidetic one of the few systems testing activation rather than only storage and retrieval mechanics.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes Eidetic's stored cards, hook-pushed rules context, and pull search tools.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies to cards, generated context, indexes, drift rows, hooks, and vault projections as different operative parts.
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places Eidetic's transcript-to-signal loop in the trace-derived landscape.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - frames session-end signal extraction as learning from agent traces.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains why project slugs, card kinds, statuses, and detail ids make selection targetable.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies ordinary memory cards, search results, and signal cards as advisory retained knowledge.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies hooks, generated rules context, MCP schemas, validators, and ranking policy as behavior-shaping control surfaces.
