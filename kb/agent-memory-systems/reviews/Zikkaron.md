---
description: "Zikkaron review: Claude Code MCP memory with SQLite/FTS/vector storage, predictive write gating, trace-learning consolidation, hooks, and push/pull recall"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-05"
tags: [trace-learning]
---

# Zikkaron

Zikkaron, by amanhij, is a local persistent memory engine for Claude Code. At the reviewed commit it runs as a Python MCP server backed by one SQLite database, exposes memory tools and resources, auto-installs Claude hooks, and uses neuroscience-inspired modules for write gating, retrieval ranking, reconsolidation, consolidation, decay, compression, project seeding, and compaction recovery.

**Repository:** https://github.com/amanhij/Zikkaron

**Reviewed commit:** [dda34a5d903d04ecb5517af214d437873c833302](https://github.com/amanhij/Zikkaron/commit/dda34a5d903d04ecb5517af214d437873c833302)

**Last checked:** 2026-06-05

## Core Ideas

**The memory substrate is one local SQLite database, not Markdown or a hosted service.** The README advertises "One SQLite file," and `StorageEngine` creates the canonical tables for episodes, memories, entities, relationships, vectors, profiles, derived beliefs, archives, checkpoints, action logs, and consolidation history, with WAL, FTS5, and `sqlite-vec` enabled ([README.md](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/README.md), [zikkaron/storage.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/storage.py)). This gives Zikkaron strong local adoption affordances for Claude Code users, but less textual auditability than file-first KB systems.

**Writes are filtered and enriched before they become durable memory.** The MCP `remember` tool first runs `PredictiveCodingGate.should_store`, then embeds the accepted content, computes surprise/importance/valence/heat, lets `MemoryCurator` create, merge, or link similar memories, captures the item in the sensory buffer, assigns domain processes, optionally auto-protects decision-pattern memories, may create micro-checkpoints, and returns related context for reinjection ([zikkaron/server.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/server.py), [zikkaron/curation.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/curation.py)). That is a real curation layer, though many decisions are heuristic rather than externally reviewed.

**Read-back is multi-signal retrieval plus host hooks.** Pull retrieval goes through MCP tools such as `recall`, `get_project_context`, `recall_hierarchical`, `navigate_memory`, `restore`, and project story/gap tools. `HippoRetriever.recall` routes query types, fuses vector, FTS, PPR, spreading activation, fractal, Hopfield, HDC, SR, temporal, profile, and derived-belief signals, then applies rerankers, rules, diversity, and cognitive-load management where configured ([zikkaron/server.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/server.py), [zikkaron/retrieval.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/retrieval.py)). Push read-back is implemented through Claude hooks that print session context, auto-recall, and restoration Markdown into Claude's context ([zikkaron/hooks/session-start-context.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/hooks/session-start-context.py), [zikkaron/hooks/prompt-recall.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/hooks/prompt-recall.py)).

**Context efficiency is engineered by ranking, heat, and chunk limits rather than by source-preserving progressive disclosure.** Retrieval is capped by `max_results`, candidate-pool settings, heat thresholds, reranker limits, MMR diversity, metacognitive `manage_context`, and hook-side character/result limits ([zikkaron/config.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/config.py), [zikkaron/hooks/prompt-recall.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/hooks/prompt-recall.py), [zikkaron/restoration.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/restoration.py)). The system controls volume, but complexity and provenance are mostly controlled by ranking and truncation, not by citation-bearing summaries.

**Trace-extracted maintenance is extensive.** Claude hook scripts write tool actions to `action_log`; consolidation groups unprocessed actions into session-activity memories, extracts entities from episodes, merges duplicates, decays heat, runs memify pruning/strengthening/reweighting/derived memories, promotes episodic patterns through CLS, compresses cold memories, and can run sleep-time dream replay and community detection ([zikkaron/hooks/post-tool-capture.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/hooks/post-tool-capture.py), [zikkaron/consolidation.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/consolidation.py), [zikkaron/curation.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/curation.py), [zikkaron/sleep_compute.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/sleep_compute.py)). The system also rewrites memory on recall through reconsolidation when mismatch thresholds fire ([zikkaron/reconsolidation.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/reconsolidation.py)).

## Artifact analysis

- **Storage substrate:** `sqlite` `files` — Canonical runtime memory persists in SQLite tables and vector/FTS virtual tables; source code, hook scripts, installed Claude settings, and synced CLAUDE.md instructions live as files.
- **Representational form:** `prose` `symbolic` `parametric` — Memory content, checkpoints, narratives, and hook-injected context are prose; tables, tags, heat, staleness flags, rules, triggers, relationships, clusters, action logs, checkpoints, and tool schemas are symbolic; embeddings, Hopfield patterns, HDC vectors, cross-encoders, NLI/GTE rerankers, and sentence-transformer models are parametric access structures.
- **Lineage:** `authored` `imported` `trace-extracted` — Users and agents author memories/rules/checkpoints; `seed_project` imports project structure, config, docs, CI, and entry points; episodes, action logs, access counts, reconsolidated memories, derived beliefs/profiles, clusters, links, dream insights, and compression outputs are extracted from interactions and stored traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Stored memories advise Claude as knowledge; synced CLAUDE.md text and hook outputs instruct the host agent; triggers, rules, project directories, entities, graph links, and cognitive-map navigation route memory; staleness checks and coverage/gap tools validate; retrieval scores and heat rank; consolidation, reconsolidation, curation, profile extraction, derived beliefs, and action-log processing learn or reshape future memory.

**Memory rows and auxiliary tables.** A memory row carries prose content plus embedding, tags, directory context, heat, staleness, importance, confidence, access counters, compression level, protection, slot index, provenance, and enrichment fields ([zikkaron/storage.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/storage.py)). The operative split is important: prose is the agent-facing recollection, while symbolic fields decide filtering, ranking, protection, compression, curation, and validity.

**Hooks and instruction artifacts.** Startup calls `sync_instructions()` and `install_hooks(cwd)` best-effort; the installed hooks add PreCompact, SessionStart, PostToolUse, and UserPromptSubmit commands to `.claude/settings.json` ([zikkaron/server.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/server.py)). These files have system-definition authority for Claude Code because their stdout becomes context or their commands mutate the memory database.

**Action logs and episodes.** Raw trace artifacts are `episodes` and `action_log` rows. They are knowledge artifacts while raw, then become stronger behavior-shaping artifacts when consolidation extracts entities, relationships, derived memories, clusters, and summarized action memories from them ([zikkaron/consolidation.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/consolidation.py)).

**Retrieval packages.** MCP responses and hook stdout are assembled, transient read-back artifacts. They are not the canonical store, but they carry direct advisory or instructional authority at the next model invocation.

**Promotion path.** Zikkaron has several promotion routes: project files become seed memories; tool traces become action summaries; repeated entities become graph relationships and clusters; high-weight co-occurrences or dream replay can create derived memories; retrieval mismatch can update or archive a memory; user anchors and decision detection can promote facts to protected status. The promotion path is powerful, but provenance is mostly row-level metadata rather than source-span evidence.

## Comparison with Our System

Zikkaron and Commonplace both treat memory as behavior-shaping infrastructure rather than passive storage, but they optimize different trust surfaces. Zikkaron is runtime-first: it captures traces, ranks hot memories, and pushes context into Claude Code with minimal user ceremony. Commonplace is artifact-first: it keeps Markdown notes, type specs, collection contracts, validation, review bundles, and source-grounded citations where later agents can audit the reasoning.

The strongest alignment is the separation between canonical state and served context. Zikkaron stores a rich database and assembles small retrieval packages at session start, prompt submit, explicit recall, or post-compaction restore. Commonplace similarly keeps a larger library and asks agents to load only the relevant contracts, notes, and reviews. Zikkaron's hook surface is a concrete implementation of push read-back that Commonplace mostly avoids or leaves to operator discipline.

The strongest divergence is lineage and governance. Zikkaron can automatically merge, derive, decay, compress, and reconsolidate memories. Commonplace usually requires authored artifacts, validation, and review before a claim gains durable authority. Zikkaron moves faster and captures more traces; Commonplace keeps stronger audit semantics and safer replacement history.

The README's benchmark claims are reported, not independently reproduced here. The code contains benchmark scripts, but this review did not rerun LoCoMo, LongMemEval, or BEAM; the implementation claims should therefore be treated as source-grounded architecture plus reported evaluation, not verified performance ([README.md](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/README.md), [benchmarks](https://github.com/amanhij/Zikkaron/tree/dda34a5d903d04ecb5517af214d437873c833302/benchmarks)).

### Borrowable Ideas

**Hook-mediated session start and prompt recall.** Commonplace could add optional host hooks that inject a small, clearly labeled context package for the current repo or task. Ready as an experiment for workspaces with stable hook semantics; not ready as default behavior without faithfulness and override controls.

**Action log as a low-latency trace buffer.** Zikkaron separates cheap hook capture from slower consolidation. Commonplace could use the same pattern for review runs or long editing sessions: append trace rows first, then promote reviewed reports later. Ready for workshop-layer telemetry.

**Protected anchors for compaction survival.** An explicit anchor path with max heat/protection is useful for constraints that must survive context compaction. Commonplace could model this as a temporary workshop artifact or run-local retained artifact, not as an unreviewed library note. Ready for session/workshop state.

**Write gate plus related-context reinjection.** Zikkaron's `remember` both decides whether a fact is surprising enough to store and returns nearby memory. Commonplace could borrow the pattern for note creation assistants: show likely duplicates and related claims before writing. Needs a concrete authoring workflow.

**Trace-extracted maintenance suggestions before automatic mutation.** Zikkaron already mutates automatically in several places, but its stats and action-log processing suggest a safer Commonplace variant: produce reviewable maintenance records for stale, duplicate, hot, or repeatedly retrieved artifacts before touching library notes. Ready where deterministic evidence is available.

## Write side

**Write agency:** `manual` `automatic` — Users and agents manually store memories, rules, triggers, checkpoints, anchors, and seed requests through MCP/CLI tools; automatic paths include hook action capture, startup hook/instruction installation, write gating, curation merge/link/create, heat updates, access counters, reconsolidation on recall, consolidation, decay, duplicate deletion, compression, action-log summarization, graph extraction, sleep-time connections, and profile/belief extraction.

**Curation operations:** `dedup` `evolve` `synthesize` `invalidate` `decay` `promote` — Similar memories can merge or be deleted as duplicates; reconsolidation updates or archives memories on retrieval mismatch; memify derives new co-occurrence claims; staleness and reconsolidation can mark stale/archive old state; thermodynamic decay cools memories and entities; heat boosts, useful ratings, decision auto-protection, anchors, and CLS promotion raise salience or tier.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — Raw inputs include explicit remembered session content, sensory-buffer episodes, PostToolUse action rows, recall/access events, compaction checkpoints, project seeding scans, and hook-triggered session/prompt events.

**Extraction.** The extraction oracles are mostly deterministic or model-backed subsystem heuristics: write-gate surprisal, embedding similarity, FTS/vector retrieval, regex/entity extraction, typed relationship extraction, graph co-occurrence, heat/access counters, cross-encoder/NLI rerankers, staleness hashes, and settings thresholds. Consolidation turns traces into entities, relationships, summarized action memories, clusters, semantic-store promotions, compressed memories, derived co-occurrence memories, and dream-insight memories. Reconsolidation uses mismatch between stored memory and retrieval context to update or archive memories.

**Learning scope:** `per-project` `cross-task` — Directory context scopes many reads and writes, but the default database is global under `~/.zikkaron/memory.db`, and global/anchored/protected memories can cross sessions and tasks.

**Learning timing:** `online` `staged` — `remember`, recall heat boosts, reconsolidation, hooks, and prompt recall happen online; consolidation, sleep compute, action-log processing, compression, and seeding are staged cycles or explicit commands.

**Distilled form:** `prose` `symbolic` `parametric` — Stored recollections, action summaries, checkpoints, narratives, and dream insights are prose; tables, rules, graph edges, clusters, triggers, profiles, derived beliefs, and memory flags are symbolic; embeddings, HDC vectors, Hopfield retrieval, and rerankers are parametric access machinery.

**Survey placement.** Zikkaron is a strong trace-learning runtime-memory system: raw interaction traces become durable memories, metadata, rankings, graph links, protected anchors, and hook-injected context. It strengthens the survey split between raw trace capture and distilled behavior-shaping artifacts, and it shows the governance risk when automatic mutation outruns reviewable provenance.

## Read-back

**Read-back:** `both` — Claude or a user can pull memory through MCP tools and resources, while installed SessionStart/UserPromptSubmit/PreCompact/PostCompact hooks can push stored or restored memory into Claude's context without the receiving model making a separate memory call.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / embedding` `inferred / judgment` — SessionStart context is coarse hot/anchored/recent loading; project-directory and tag/rule/triggers are identifiers; prompt-recall and full recall use FTS/BM25-style lexical matching; vector, HDC, SR, Hopfield, and cross-encoder paths use embedding/model similarity; metacognition, NLI reranking, profile/belief inference, and coverage/gap tools add judgment-like selection when configured.

**Faithfulness tested:** `no` — The code records access, ratings, retrieval confidence, benchmark scripts, and reported aggregate evaluations, but the inspected implementation does not perform per-invocation with/without-memory ablations or post-action audits showing that a particular pushed memory changed Claude's behavior.

**Direction edge case.** MCP `recall` is pull from the agent or user that calls it. Claude hooks are push for the receiving Claude Code session because their stdout is injected into context at session start, prompt submit, or compaction restore. The installed hook behavior depends on Claude Code honoring those settings; the source shows the hook files and installer, not actual host execution.

**Selection, scope, and complexity.** Explicit recall defaults to five results and a minimum heat of 0.1; prompt auto-recall injects at most five memories and roughly 3,000 characters; session-start context loads up to six hot project memories, four anchors, and recent actions; restoration uses a configured max restore-memory count and sections for checkpoint, anchored, recent, hot, predicted, and gap context ([zikkaron/server.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/server.py), [zikkaron/hooks/prompt-recall.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/hooks/prompt-recall.py), [zikkaron/hooks/session-start-context.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/hooks/session-start-context.py), [zikkaron/restoration.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/restoration.py)). Effective precision, recall, and context dilution are not proven by code.

**Injection point.** Read-back is pre-invocation: hooks print context before Claude processes a session/prompt/restore event, and MCP tools return context before the caller uses it. PostToolUse capture and consolidation are write-side maintenance for future calls, not read-back.

**Authority at consumption.** Most read-back is advisory context. Synced CLAUDE.md instructions and hook-injected headings carry stronger instruction-like pressure, and rules can filter/rerank memories before delivery, but there is no hard gate that forces the model to obey recalled content.

## Curiosity Pass

**The neuroscience vocabulary maps onto real modules, but not always to auditable semantics.** There are implemented Hopfield, HDC, SR, engram, thermodynamic, reconsolidation, and sleep-compute components, but a later maintainer still has to inspect ordinary code paths, thresholds, and database mutations to know what authority they have.

**Reconsolidation is unusually aggressive for a persistent memory system.** Retrieval can update or archive memory based on mismatch, which may be useful for evolving projects but can erase the distinction between remembered evidence and current interpretation unless archive review is added.

**Startup side effects are broad.** Running the server attempts to sync global `~/.claude/CLAUDE.md` and install project hooks automatically. That helps adoption, but it gives a package startup path authority over host-agent instructions and local project settings.

**Benchmarks emphasize retrieval quality, but governance remains the hard part.** High reported LoCoMo/LongMemEval/BEAM scores, if reproducible, make Zikkaron a strong retrieval implementation. They do not answer whether automatically derived, merged, compressed, or reconsolidated memories remain faithful enough for high-authority use.

**The database is both strength and risk.** SQLite makes local operation and rich indexing easy, but unlike Markdown notes it hides many behavior-shaping changes from ordinary diff/review workflows unless operators inspect tables or export state.

## What to Watch

- Whether Zikkaron adds source-span provenance or audit trails for derived, compressed, reconsolidated, and dream-generated memories; that would make automatic mutation safer and closer to Commonplace's reviewable lineage.
- Whether the hook installation path becomes opt-in or more narrowly scoped; automatic CLAUDE.md and `.claude/settings.json` edits are powerful system-definition writes.
- Whether benchmark scripts are kept reproducible against the exact released code and model settings; the README's evaluation claims are central but were not rerun here.
- Whether reconsolidation and memify-generated memories gain review or rollback workflows; without them, automatic evolution can become silent belief drift.
- Whether prompt auto-recall gains per-memory faithfulness audits or at least logged fired-memory/outcome pairs; that would move push read-back from structural injection to tested behavioral influence.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes Zikkaron's SQLite memory store from its MCP and hook paths that actually serve memory into Claude's context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - supports separating database rows, hook files, synced instructions, embeddings, action logs, and generated summaries by substrate, form, lineage, and authority.
- [Use trace extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) - frames Zikkaron's action-log, episode, consolidation, and reconsolidation loops as trace-learning.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - describes the authority carried by hook settings, synced CLAUDE.md instructions, rules, validators, and retrieval policy.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - describes the advisory role of ordinary stored memories, project context, checkpoints, and raw traces.
- [Lineage](../../notes/definitions/lineage.md) - highlights the provenance risk around automatic compression, derivation, reconsolidation, and dream replay.
