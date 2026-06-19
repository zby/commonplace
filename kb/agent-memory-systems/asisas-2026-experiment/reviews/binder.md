---
description: "Binder review: local-first typed SQLite graph with Markdown sync, transaction history, CLI/MCP access, LSP validation, and explicit agent reads"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
---

# Binder

Binder, from mpazik, is a local-first database and knowledge-graph workspace for tools built with agents. At the reviewed commit it stores typed entities and configuration in SQLite, projects them into Markdown/YAML files through navigation rules, records immutable transactions with undo/redo support, and exposes the same graph through a CLI, MCP server, LSP/editor integrations, HTTP API, scripts, and a TypeScript library.

**Repository:** https://github.com/mpazik/binder

**Reviewed commit:** [da86cb6166e207099a205076107cf626da16ba56](https://github.com/mpazik/binder/commit/da86cb6166e207099a205076107cf626da16ba56)

**Last checked:** 2026-06-04

## Core Ideas

**The retained unit is a typed entity graph, not a transcript or vector memory.** Binder represents records as entities with `uid`, optional human-facing `key`, `type`, tags, and arbitrary schema-defined fields; config entities define fields, types, navigation, and views ([packages/repo/src/model/entity.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/model/entity.ts), [packages/repo/src/model/schema.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/model/schema.ts)). Relation fields turn those entities into a graph, with UID-based record references and key-based config references ([docs/concepts/reference.md](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/docs/concepts/reference.md)).

**SQLite is the source of truth and files are a synchronized view.** The database has `records`, `configs`, and `transactions` tables, with user/config fields stored in JSON columns and indexed identity/type/key columns ([packages/repo/src/schema.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/schema.ts)). Workspace paths resolve the database under `.binder/data/binder.db` ([packages/repo/src/local/constants.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/local/constants.ts), [packages/repo/src/local/paths.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/local/paths.ts)). Navigation rules render entities to Markdown/YAML, clean up stale projections, and can reverse file edits back into graph changes ([packages/cli/src/document/repository.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/document/repository.ts), [packages/cli/src/document/navigation.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/document/navigation.ts), [packages/cli/src/document/change-extractor.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/document/change-extractor.ts)).

**Transactions give changes explicit lineage and rollback.** A transaction records record/config changesets, author, timestamp, tags, message/source/channel metadata, content hash, and previous hash; the processor resolves an input against the current schema and version before applying it ([packages/repo/src/model/transaction.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/model/transaction.ts), [packages/repo/src/transaction-processor.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/transaction-processor.ts)). Apply, rollback, undo, redo, squash, and journal repair are implemented as graph operations rather than informal file edits ([packages/repo/src/transaction-applier.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/transaction-applier.ts), [packages/cli/src/lib/orchestrator.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/lib/orchestrator.ts)).

**Agents get structured read/write APIs.** The MCP server exposes `schema`, `search`, and `transact`; `search` is read-only and returns structured content, while `transact` creates or updates records/config entities through the same transaction path as the CLI ([packages/cli/src/mcp/tools/index.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/mcp/tools/index.ts), [packages/cli/src/mcp/tools/search.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/mcp/tools/search.ts), [packages/cli/src/mcp/tools/transact.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/mcp/tools/transact.ts)). The CLI mirrors this with `search`, `create`, `update`, `read`, transaction import/log, and undo/redo commands ([packages/cli/src/commands/search.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/commands/search.ts), [packages/cli/src/commands/create.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/commands/create.ts), [packages/cli/src/commands/update.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/commands/update.ts)).

**Editor support turns schemas into adoption affordances.** The LSP resolves Binder workspaces, validates Markdown/YAML against navigation and schema, offers field-key and relation completions, and syncs saved files back to Binder transactions ([packages/cli/src/lsp/workspace-manager.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/lsp/workspace-manager.ts), [packages/cli/src/validation/engine.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/validation/engine.ts), [packages/cli/src/lsp/handlers/completion.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/lsp/handlers/completion.ts), [packages/cli/src/lsp/handlers/save-handler.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/lsp/handlers/save-handler.ts)). This makes Binder closer to an agent-editable structured notebook than to a hidden memory service.

**Context efficiency is explicit but pull-bound.** Binder keeps selection symbolic: filters, includes, ordering, pagination, path navigation, and relation traversal decide what an agent or script asks for ([packages/repo/src/model/query.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/model/query.ts), [packages/repo/src/filter-entities.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/filter-entities.ts), [packages/repo/src/relationship-resolver.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/relationship-resolver.ts)). At this commit, semantic search is described as roadmap work in the README rather than a source-visible retrieval layer ([README.md](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/README.md)).

## Artifact analysis

- **Storage substrate:** `sqlite` — The primary retained state persists in `.binder/data/binder.db` as SQLite tables for records, config entities, and transactions; Markdown/YAML files and JSONL journals are synchronized projections and audit surfaces, not the primary lead substrate.
- **Representational form:** `prose` `symbolic` — Richtext/plaintext fields and rendered Markdown carry prose, while schemas, field definitions, types, relation constraints, filters, navigation rules, views, transactions, and MCP/tool schemas are symbolic.
- **Lineage:** `authored` — Humans, agents, CLI commands, MCP calls, editor saves, HTTP calls, scripts, imports, and hooks author explicit entity/config/transaction changes; Binder records transaction lineage but does not implement durable trace-derived learning from agent transcripts.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` — Records and rendered files act as knowledge artifacts; types, fields, navigation, views, LSP validation, config, hooks, and MCP/tool schemas shape instruction, enforcement, routing, and validation paths.

**Record entities.** Storage substrate: SQLite `records` rows with identity columns and JSON field payloads. Representational form: mostly symbolic field/value records plus prose fields such as descriptions, details, and Markdown-rich text. Lineage: authored by CLI/MCP/HTTP/library calls or by reverse-synced file edits, then attributed through transactions. Behavioral authority: knowledge artifacts for agents, scripts, humans, and dashboards; relation fields and type fields can also route later retrieval.

**Config entities: fields, types, navigation, and views.** Storage substrate: SQLite `configs` rows, rendered to `.binder/fields`, `.binder/types`, `.binder/navigation`, and `.binder/views` projections. Representational form: symbolic schemas and route definitions with prose names/descriptions. Lineage: authored configuration, with config changes processed before records in a transaction so a new schema element can be used immediately ([packages/repo/src/transaction-processor.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/transaction-processor.ts)). Behavioral authority: system-definition artifacts, because they define valid fields, type constraints, relation ranges, file routing, and render/sync behavior.

**Transactions and journals.** Storage substrate: SQLite `transactions` rows plus transaction/undo JSONL logs under `.binder/data/`. Representational form: symbolic changesets, hashes, previous links, author/time/source/channel metadata, and optional prose message. Lineage: derived from each accepted change input after schema validation and canonicalization; rollback applies inverse transactions and deletes rolled-back transaction rows ([packages/repo/src/model/transaction.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/model/transaction.ts), [packages/repo/src/transaction-applier.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/transaction-applier.ts)). Behavioral authority: audit, validation, repair, undo/redo, and replay authority.

**Markdown/YAML projections.** Storage substrate: repository files outside `.binder/data`, generated by navigation and snapshot machinery. Representational form: prose Markdown, YAML records, frontmatter, and projected relation references. Lineage: derived views from SQLite graph state; file edits can become authored changes when the LSP/save-sync or docs-sync path extracts diffs back into transaction input ([packages/cli/src/document/change-extractor.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/document/change-extractor.ts), [packages/cli/src/lsp/handlers/save-handler.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/lsp/handlers/save-handler.ts)). Behavioral authority: knowledge and authoring surface; the database remains the source of truth.

**CLI, MCP, HTTP, and library APIs.** Storage substrate: repository code plus workspace configuration. Representational form: symbolic command/tool schemas, request parameters, filters, includes, and structured results. Lineage: authored integration surfaces. Behavioral authority: routing and enforcement, because they determine how agents and programs may read, write, validate, and scope changes.

**Hooks and plugins.** Storage substrate: workspace config and loaded plugin modules. Representational form: symbolic hook commands and plugin registration code. Lineage: authored operator configuration. Behavioral authority: post-transaction automation authority: `hooksToPlugin` registers handlers that receive each transaction as JSON on stdin, and plugins can register against the repo ([packages/repo/src/local/plugin-loader.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/local/plugin-loader.ts), [packages/repo/src/local/open.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/local/open.ts)).

Promotion path: Binder's strongest promotion path is structural rather than learned: loose authored records can be constrained by adding fields/types, projected into navigable files, validated by the LSP/docs lint path, and governed through transactions. It does not promote raw agent traces into durable rules or memories automatically.

## Comparison with Our System

| Dimension | Binder | Commonplace |
|---|---|---|
| Primary purpose | Local-first typed graph/database for agent-built tools | Git-native methodology KB for agent-operated knowledge bases |
| Main substrate | SQLite graph plus Markdown/YAML projections and JSONL journals | Markdown artifacts, type specs, validators, source snapshots, generated indexes |
| Canonical write | Transaction over records/configs | Git/file edit over typed KB artifacts |
| Read path | CLI/MCP/HTTP/library queries, editor files, LSP navigation | `rg`, indexes, links, skills, validation/report artifacts |
| Authority model | Schema/config/navigation/tools enforce structure around records | Collection contracts, type specs, instructions, review gates, validation |
| Learning model | Manual/explicit authoring and automation hooks | Manual/agent-authored notes plus review/validation workflows |

Binder and Commonplace share an important premise: agent memory should be inspectable and structured, not only embedded in a vector store. Binder makes this practical for small operational tools by giving agents a typed graph with a real transaction model and editor-friendly projections. Commonplace makes it practical for methodology work by keeping claims, sources, type contracts, and review status as ordinary repository artifacts.

Binder is stronger where the user needs an application data layer: task trackers, queues, catalogs, dashboards, and agent-shared state with undoable writes. Commonplace is stronger where the durable artifact is a claim, instruction, review, or theory note whose provenance and wording must be reviewed directly. Binder's SQLite source of truth is useful for transactional consistency; Commonplace's file-native source of truth is useful for diff review and semantic governance.

**Read-back:** `pull` — Binder exposes explicit reads through CLI search/read, MCP `schema` and `search`, HTTP endpoints, library calls, rendered files, editor navigation, and LSP completions; the reviewed code does not include a hook that automatically injects retained Binder records into an agent prompt before action.

### Borrowable Ideas

**Transaction metadata for agent writes.** Ready now as a design pattern. Binder's `author`, `source`, `channel`, message, tags, hash, and previous-link fields are a useful model for making agent-originated KB changes auditable beyond a raw Git diff.

**Schema-first agent tools.** Ready now. The MCP `schema` tool encourages agents to inspect valid types and fields before creating records. Commonplace skills already read collection/type specs; tooling could make that preflight more structured.

**Bidirectional projection with divergence detection.** Needs a concrete use case. Binder can render records to files and detect changed/diverged projections before sync. Commonplace could use similar snapshot metadata for generated indexes or workshop projections, but not for core notes unless the source-of-truth boundary is explicit.

**Navigation as data, not hardcoded folders.** Useful but not urgent. Binder stores navigation rules as config entities. Commonplace's collection routing is deliberately file-first, but generated or experimental workspaces could benefit from explicit route records.

**Do not borrow hidden database primacy for claim-heavy notes.** Binder's SQLite-first design fits operational records. For Commonplace reviews and methodology notes, retaining Markdown as the canonical artifact keeps review, citation, and semantic edits simpler.

## Write side

**Write agency:** `manual` `automatic` — Manual authoring comes through CLI/MCP/HTTP/library/editor/file-sync writes; automatic write-side operations include LSP save-sync extraction, docs sync, post-transaction rendering, undo/redo/rollback, journal repair, plugin hooks, and transaction squashing.

**Curation operations:** `invalidate` `consolidate` — Rollback/undo/redo and moved projections supersede prior state while preserving transaction history; transaction squashing consolidates consecutive transactions into one equivalent transaction for history compaction.

Binder does not qualify as trace-derived learning in the review sense. It can record an agent's authored records and transaction metadata, and hooks can run after every committed transaction, but the repository does not implement a durable raw-trace-to-distilled-memory loop over session logs, tool traces, event streams, or trajectories.

## Read-back

**Read-back:** `pull` — Agents, scripts, editors, and humans must ask Binder for stored memory through `search`, `read`, schema inspection, relation includes, rendered files, LSP navigation/completion, HTTP endpoints, or library calls; static skills and README setup guidance do not make retained workspace records arrive unsolicited.

Selection is symbolic and bounded by caller choices: filters, includes, relation traversal, ordering, pagination, namespace, navigation paths, and optional field selections. The `search` MCP tool is read-only, validates filters, applies pagination, and returns structured results; the CLI search path similarly parses a compact DSL or stdin JSON query. Text matching is exact substring-style filtering over plaintext/richtext fields, not source-visible semantic retrieval at this commit ([packages/repo/src/filter-entities.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/filter-entities.ts), [packages/cli/src/mcp/tools/search.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/mcp/tools/search.ts), [packages/cli/src/commands/search.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/commands/search.ts)).

Authority at consumption depends on the host. A retrieved record is advisory knowledge for an agent unless the consuming tool treats the schema, navigation, validation, or transaction API as a hard gate. Binder can enforce writes and validate documents, but it does not prove that a receiving model faithfully uses returned records. Faithfulness is therefore not applicable as a push-specific read-back test for this pull-only review.

## Curiosity Pass

**Binder is closer to a local app substrate than a memory assistant.** Its agent-memory value comes from giving agents a typed, auditable place to share state with humans and scripts, not from autonomous recall or learned preference extraction.

**The Markdown layer is deliberately not the only truth.** This is the reverse of many file-native KBs: files are readable/editable projections, while consistency, history, undo, and schema validation live in the database and transaction system.

**The transaction hash chain is a stronger idea than the current agent integrations require.** MCP tools could be used simply as CRUD, but the hash/previous lineage means Binder can support higher-trust workflows if agents include meaningful source/channel/message metadata.

**Hooks make automation possible without making learning automatic.** A hook can append audit logs, notify systems, or run custom processors after commits, but that is an extension point rather than an implemented trace-derived memory loop.

**The LSP is an important memory interface.** Autocomplete, diagnostics, and save-sync are not retrieval in the LLM sense, but they make structured memory maintainable by humans and coding agents in the same editor workspace.

## What to Watch

- Whether full-text and semantic search move from README roadmap into source-visible query/index code; that would change Binder's read-back signal from purely symbolic/lexical pull toward learned similarity retrieval.
- Whether MCP grows resource listings or prompt/context injection hooks beyond explicit tools; that would change the pull-only read-back verdict.
- Whether transaction log compaction lands and how it preserves auditability; compaction is useful but could weaken lineage if old source/channel/message detail is lost.
- Whether cross-device sync or encrypted backup changes the primary storage-substrate story from local SQLite to replicated/encrypted service objects.
- Whether Binder adds a first-class agent-session capture workflow; that would determine whether it becomes trace-derived or remains explicit authored state.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Binder stores durable agent-readable state but leaves recall to explicit CLI/MCP/HTTP/editor reads.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: Binder's records, config entities, projections, transactions, hooks, and tools have different authority despite sharing one database.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: Binder records and rendered files mostly serve as evidence, reference, and context.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: Binder schemas, navigation, views, validators, hooks, and tool definitions constrain future behavior.
- [Symbolic context engineering is bounded by symbol availability](../../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - relates: Binder's context efficiency depends on fields, identifiers, relation keys, filters, and navigation rules being present and maintained.
