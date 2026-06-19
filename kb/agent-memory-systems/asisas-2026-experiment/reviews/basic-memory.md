---
description: "Basic Memory review: local-first Markdown knowledge graph with SQLite/Postgres indexes, MCP pull tools, semantic search, schemas, and Claude hook read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
tags: [trace-derived]
---

# Basic Memory

Basic Memory, by Basic Machines, is a local-first knowledge graph and MCP server for AI assistants. At the reviewed commit it treats Markdown files as the durable user-owned memory surface, parses observations and relations into a database-backed graph/search layer, exposes MCP/CLI/API tools for reading and writing, and ships host integrations that can brief or checkpoint agent sessions.

**Repository:** https://github.com/basicmachines-co/basic-memory

**Reviewed commit:** [fc2ee07076eb397b09db7b2681e5213002df0d70](https://github.com/basicmachines-co/basic-memory/commit/fc2ee07076eb397b09db7b2681e5213002df0d70)

**Source directory:** `related-systems/basicmachines-co--basic-memory`

## Core Ideas

**Markdown is the user-facing source of truth; the database is the operational mirror.** The README frames the product as plain-text memory that humans and AIs both edit, and the code makes each Markdown file an `Entity` with frontmatter, observations, relations, file metadata, and a materialized `NoteContent` row ([README.md](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/README.md), [src/basic_memory/models/knowledge.py](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/src/basic_memory/models/knowledge.py), [src/basic_memory/markdown/entity_parser.py](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/src/basic_memory/markdown/entity_parser.py)). This gives strong adoption affordances: the store remains inspectable in an editor or Obsidian even when MCP is not running.

**The graph grammar is deliberately small.** A note has frontmatter, categorized observations, and wikilink-style relations; the parser extracts those into structured `Observation` and `Relation` rows while preserving the prose note body ([README.md](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/README.md), [src/basic_memory/markdown/plugins.py](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/src/basic_memory/markdown/plugins.py), [src/basic_memory/services/entity_service.py](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/src/basic_memory/services/entity_service.py)). The format is closer to an indexed personal knowledge base than to an opaque conversation-memory service.

**Context efficiency is tool-mediated and progressively bounded.** `search_notes` defaults to entity-level results, supports page sizes and structured filters, and chooses hybrid retrieval when semantic search is enabled; `build_context` follows graph edges with explicit `depth`, `page_size`, and `max_related` limits; `recent_activity` caps page size and defaults to entity-only results ([src/basic_memory/mcp/tools/search.py](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/src/basic_memory/mcp/tools/search.py), [src/basic_memory/mcp/tools/build_context.py](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/src/basic_memory/mcp/tools/build_context.py), [src/basic_memory/mcp/tools/recent_activity.py](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/src/basic_memory/mcp/tools/recent_activity.py)). Complexity is still host-dependent: the system gives bounded retrieval tools, but a client can keep calling them and overfill context.

**Search is hybrid but inspectable at the storage boundary.** Full-text rows, vector chunks, and embeddings are derived access structures over notes, observations, and relations. SQLite uses FTS5 plus sqlite-vec; Postgres support lives in a sibling repository implementation with vector tables and full-text search ([src/basic_memory/repository/search_repository_base.py](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/src/basic_memory/repository/search_repository_base.py), [src/basic_memory/repository/sqlite_search_repository.py](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/src/basic_memory/repository/sqlite_search_repository.py), [src/basic_memory/services/search_service.py](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/src/basic_memory/services/search_service.py)). Embeddings rank recall, but they do not replace the readable note store.

**Schemas add soft governance over notes.** Picoschema definitions map schema fields to observation categories, relation types, and frontmatter keys; validation is warning-oriented by default, and metadata search makes typed notes queryable by frontmatter fields ([src/basic_memory/schema/parser.py](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/src/basic_memory/schema/parser.py), [src/basic_memory/schema/validator.py](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/src/basic_memory/schema/validator.py), [docs/metadata-search.md](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/docs/metadata-search.md)). The authority is mostly advisory and diagnostic, not a hard write gate.

**Host packages turn the same graph into agent memory workflows.** The repository includes a Claude Code plugin, shared skills, and Hermes/OpenClaw integrations. The Claude plugin has SessionStart and PreCompact hooks: one pushes a bounded brief from Basic Memory into Claude Code, and the other writes an extractive session checkpoint back to the graph ([README.md](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/README.md), [plugins/claude-code/README.md](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/plugins/claude-code/README.md), [plugins/claude-code/hooks/session-start.sh](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/plugins/claude-code/hooks/session-start.sh), [plugins/claude-code/hooks/pre-compact.sh](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/plugins/claude-code/hooks/pre-compact.sh)).

## Artifact analysis

- **Storage substrate:** `files` — The primary retained memory surface is project-local Markdown files; SQLite or Postgres stores parsed entities, observations, relations, materialized note content, search rows, vector chunks, embeddings, project records, and cloud-routing/sync state as operational mirrors and access structures.
- **Representational form:** `prose` `symbolic` `parametric` — Note bodies, observations, plugin briefs, skills, and checkpoint summaries are prose; frontmatter, schemas, relations, permalinks, project routing, tool annotations, filters, validation results, and hook scripts are symbolic; semantic embeddings are parametric retrieval state.
- **Lineage:** `authored` `imported` `trace-extracted` — Humans and agents author Markdown through editors, MCP, CLI, and skills; importers ingest ChatGPT, Claude conversation/project exports, and memory JSON; sync/indexing derive graph/search state from files; Claude Code hooks can extract session checkpoints from JSONL transcripts.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Notes and observations serve as knowledge artifacts; MCP resources, skills, output styles, and plugin briefs instruct agents; projects, permalinks, schemas, relations, and tool annotations route work; schema validation and sync conflict checks warn or reject in bounded cases; FTS/vector/hybrid scores rank read-back; trace-derived session notes and reflection skills provide learning material for later sessions.

**Markdown entities.** The central artifact is a Markdown file whose operative parts split cleanly: frontmatter controls title/type/tags/permalink/metadata, observation bullets become categorized facts, relation bullets and wikilinks become graph edges, and the body remains readable prose. This bundled object has knowledge authority when read by an agent, routing/ranking authority when parsed into indexes, and validation authority when a schema is resolved against it.

**Database mirror and search indexes.** `Entity`, `Observation`, `Relation`, `NoteContent`, full-text rows, vector chunks, and vector embeddings are derived from the file/project state. Their lineage is compiled/indexed rather than canonical. The promotion path runs from authored/imported Markdown to parsed graph rows to ranked MCP results; deletion or edit of the file invalidates the derived rows during sync.

**MCP tool and prompt surface.** `write_note`, `edit_note`, `read_note`, `search_notes`, `build_context`, `recent_activity`, schema tools, and project tools form the agent-facing API. Tool annotations such as read-only, destructive, idempotent, and open-world hints are symbolic system-definition artifacts that help clients select tools without experimenting ([README.md](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/README.md), [src/basic_memory/mcp/tools/write_note.py](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/src/basic_memory/mcp/tools/write_note.py), [src/basic_memory/mcp/resources/ai_assistant_guide.md](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/src/basic_memory/mcp/resources/ai_assistant_guide.md)).

**Schemas and metadata filters.** Schema notes and parser/validator code let a note type acquire a checkable shape without making every note strictly enforced. Structured metadata search then gives those fields read-back power: a `type: decision` or `status: active` field can become a deterministic SessionStart query target.

**Claude Code plugin artifacts.** The plugin's hooks, output style, seed schemas, and skills are system-definition artifacts. SessionStart emits a bounded advisory brief; PreCompact writes a `type: session` checkpoint; the output style instructs the agent to search before recall, capture material decisions, and cite permalinks ([plugins/claude-code/hooks/session-start.sh](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/plugins/claude-code/hooks/session-start.sh), [plugins/claude-code/hooks/pre-compact.sh](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/plugins/claude-code/hooks/pre-compact.sh), [plugins/claude-code/output-styles/basic-memory.md](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/plugins/claude-code/output-styles/basic-memory.md)).

## Comparison with Our System

Basic Memory and Commonplace share the strongest premise: durable memory should be readable artifacts, not only hidden database state. Both systems use Markdown, frontmatter, links, validation-ish machinery, and generated/derived access surfaces. The difference is register and product shape. Basic Memory is a general user-facing memory graph with MCP tools and host integrations; Commonplace is a methodology KB with collection contracts, type specs, review gates, and stronger artifact lifecycle rules.

Basic Memory has the better general-purpose integration surface. It gives agents a compact tool suite, cloud/local routing, vector/hybrid search, schema inference/validation, and host-native hooks. Commonplace has the stronger curation contract: types are explicit, collection-level routing rules are authored, replacement history is maintained, and validation treats note quality and link health as repository governance.

The main tradeoff is authority. Basic Memory makes it easy for an agent to write a note, search it later, and bridge a session boundary. That lowers adoption cost, but it also means stale or weakly sourced notes can become future context. Commonplace is slower to write into, but more deliberate about source grounding, replacement, and review.

### Borrowable Ideas

**MCP behavior annotations as tool-selection context.** Commonplace commands exposed to agents could carry read-only/destructive/idempotent hints in a structured manifest. Ready for command documentation and future MCP wrappers.

**Structured metadata search as first-class read-back.** Basic Memory's filter-only search over frontmatter is a concrete pattern for making typed notes actionable without semantic search. Ready for Commonplace's generated indexes or any future search layer.

**Session checkpoint notes.** The Claude plugin's PreCompact checkpoint is a useful workshop-layer pattern: extract a resumable cursor before context compaction, then let the next session query it. Ready for workshop artifacts; durable promotion should require review.

**Host hook brief with hard bounds.** SessionStart caps shared projects and brief size, turning push read-back into a bounded product surface. Commonplace could use the same principle for review-run or task-start context assembly.

**Soft schema validation.** Basic Memory's schemas warn without blocking normal writing. Commonplace already validates harder in library collections; a softer mode could fit workshop drafts where learning the shape matters more than enforcement.

**Do not borrow database mirrors as canonical memory.** The value is in the file-first contract plus derived indexes. Commonplace should keep generated/vector/search state subordinate to authored artifacts.

## Write side

**Write agency:** `manual` `automatic` — Humans and agents write Markdown through editors, MCP tools, CLI commands, imports, and host skills; the system automatically syncs files, parses frontmatter/observations/relations, updates database rows, materializes note content, maintains search/vector indexes, watches files, writes hook checkpoints, and records watch/sync status.

**Curation operations:** `synthesize` — The core app mostly performs access-structure maintenance, not content curation. The qualifying curation path is in the agent packages: Claude Code PreCompact creates a new session checkpoint from transcript material, and the reflection/capture skills instruct agents to synthesize or rewrite memory notes from recent activity when invoked ([plugins/claude-code/hooks/pre-compact.sh](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/plugins/claude-code/hooks/pre-compact.sh), [skills/memory-capture/SKILL.md](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/skills/memory-capture/SKILL.md), [skills/memory-reflect/SKILL.md](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/skills/memory-reflect/SKILL.md)).

### Trace-derived learning

**Trace source:** `session-logs` — The implemented Claude Code PreCompact hook reads the host hook payload and the Claude transcript JSONL path, filters user/assistant turns, and writes a `type: session` note containing an extractive summary, recent user messages, observations, and session metadata.

**Extraction.** The current hook uses deterministic extraction, clipping, and frontmatter construction rather than an LLM judge. It requires a configured `primaryProject`, avoids shared-project writes, and exits silently on failure so compaction is not blocked. The shared skills describe richer agent-mediated capture/reflection loops, but those are instructions invoked by an agent rather than an always-on daemon.

**Learning scope:** `per-project` — Session checkpoints are routed to the configured Basic Memory project and capture folder; team projects are read for briefs but not auto-written.

**Learning timing:** `online` `staged` — The checkpoint fires during the agent lifecycle just before compaction; reflection is a staged skill workflow when run by cron, heartbeat, or explicit request.

**Distilled form:** `prose` `symbolic` — The durable output is a Markdown session note with prose summary/recent-thread text plus symbolic frontmatter, tags, observations, project, cwd, and session id fields.

Relative to the trace-derived survey, Basic Memory is strongest as trace-to-knowledge rather than trace-to-enforcement. It turns session traces into future advisory context and structured recall targets; it does not automatically derive validators, route tables, fine-tuned weights, or hard policy from the transcript.

## Read-back

**Read-back:** `both` — The MCP/CLI/API search, read, recent-activity, and graph-context tools are pull interfaces; host integrations such as the Claude Code SessionStart hook can push selected retained memory into the receiving agent's initial context.

**Read-back signal:** `coarse` `identifier` — SessionStart fires at a coarse lifecycle event, then selects active tasks, open decisions, recent sessions, and shared-project decisions through configured project refs and metadata filters such as type/status/timeframe. The ordinary `search_notes` tool can use lexical or embedding inference, but that remains pull unless a host hook or agent instruction injects the result.

**Faithfulness tested:** `no` — The repository has tests for tools, search behavior, schemas, sync, and integrations, but the inspected code does not implement with/without-memory ablations or post-answer audits proving that pushed or pulled memory changed the model's behavior faithfully.

The main injection point is pre-invocation. SessionStart prints a bounded brief to stdout before Claude Code begins the session; the output style adds standing instructions to search before recall and capture decisions; MCP prompts such as `continue_conversation` tell the agent to run tools before responding ([plugins/claude-code/hooks/session-start.sh](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/plugins/claude-code/hooks/session-start.sh), [plugins/claude-code/output-styles/basic-memory.md](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/plugins/claude-code/output-styles/basic-memory.md), [src/basic_memory/mcp/prompts/continue_conversation.py](https://github.com/basicmachines-co/basic-memory/blob/fc2ee07076eb397b09db7b2681e5213002df0d70/src/basic_memory/mcp/prompts/continue_conversation.py)).

Selection and complexity are partly governed. SessionStart caps shared projects and output size; `search_notes` uses page size, entity-type defaults, metadata filters, and configurable text/vector/hybrid modes; `build_context` bounds graph depth and related-result count. Effective precision, recall, and context dilution are not proven from code.

Authority at consumption is mostly advisory. Search results, graph context, and session briefs become context for the agent. Schemas can warn, tool annotations can guide selection, and output styles can instruct behavior, but Basic Memory does not generally make recalled notes a hard gate on the next action.

Other consumers matter. Humans can edit the same Markdown files, inspect sync/search effects through CLI/status commands, browse Basic Memory Cloud, and use Obsidian or other editors. That human-readable consumer surface is part of the trust model.

## Curiosity Pass

The README's local-first framing is accurate for the OSS core, but the reviewed repository also includes cloud routing, cloud API support, and hosted-product messaging. For architecture comparison, the important distinction is not local versus cloud; it is canonical Markdown plus database/search mirrors versus opaque service memory.

Basic Memory has two different "memory" stories in one repo: a general MCP knowledge graph and host-specific bridge packages. The trace-derived learning classification comes from the latter, especially Claude Code PreCompact, not from the core sync/index/search engine.

The semantic-search feature is retrieval infrastructure, not semantic curation. Embeddings help find notes by similarity, but they do not decide what should be remembered, merged, invalidated, or trusted.

The schema system is more important than it first looks. Because metadata filters can query schema-stamped types and statuses, schemas become read-back handles, not just validation documentation.

Session checkpoints are intentionally weakly governed. They preserve continuity, but they are extractive, not verified; without later review or reflection they can carry stale next steps forward.

## What to Watch

- Whether PreCompact changes from extractive checkpoints to summarized or validated checkpoints; that would strengthen trace-derived synthesis and may introduce a new oracle.
- Whether Basic Memory adds automatic consolidation, deduplication, decay, or contradiction handling over canonical notes; that would move write-side curation beyond synthesis.
- Whether schema validation becomes enforceable per project or per note type; that would change schemas from advisory validation to stronger system-definition authority.
- Whether host hooks start using semantic/vector search for pushed briefs rather than structured metadata filters; that would change the read-back signal from identifier-heavy to inferred/embedding.
- Whether cloud snapshots/backups become part of the OSS-reviewed implementation surface rather than hosted-service claims; that would broaden the storage-substrate analysis.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes Basic Memory's stored Markdown graph from MCP pull tools and host hook push.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - supports separating Markdown notes, database mirrors, search/vector indexes, schemas, and plugin hooks.
- [Use trace-derived extraction as meta-learning](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - frames session checkpoints and reflection/capture skills as trace-derived learning material.
- [Symbolic context engineering is bounded by symbol availability](../../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains why Basic Memory's typed frontmatter and project identifiers make pushed briefs more targetable.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies schemas, MCP tool annotations, output styles, and hooks as behavior-shaping control surfaces.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies ordinary notes, observations, relations, and session checkpoints as advisory remembered context.
