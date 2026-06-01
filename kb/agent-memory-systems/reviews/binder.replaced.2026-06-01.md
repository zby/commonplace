---
description: "Local-first SQLite knowledge graph whose markdown files are editable projections over typed entities, transactions, schemas, views, LSP, CLI, HTTP, and MCP"
type: ../types/agent-memory-system-review.md
status: outdated
last-checked: "2026-05-16"
tags: []
---

# Binder

> Replaced 2026-06-01. See [binder](./binder.md) for the current review.

Binder is mpazik's local-first database for agent-built tools: a TypeScript/Bun monorepo that stores typed entities in SQLite, projects them into editable markdown and YAML files, and exposes the same graph through CLI, LSP, HTTP, and MCP surfaces. It is directly relevant to agent memory because it treats "memory" as structured operational state that humans, scripts, editors, and agents can all read and mutate with transaction history.

**Repository:** https://github.com/mpazik/binder

**Reviewed commit:** [00257e64fe60f3461ccaed5739f51d2bc32eed64](https://github.com/mpazik/binder/commit/00257e64fe60f3461ccaed5739f51d2bc32eed64)

## Core Ideas

**SQLite is the source of truth; markdown is a synchronized view.** The README says Binder stores data as a graph of typed entities and explicitly frames markdown files as a view over that graph ([README.md](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/README.md)). The implementation backs that with SQLite tables for records, config entities, and transactions, opened through `@binder/repo/local` as the operational repository ([schema.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/repo/src/schema.ts), [open.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/repo/src/local/open.ts), [db.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/repo/src/db.ts)). The projected files are knowledge artifacts when read as context. The database schema, navigation rules, views, transaction processor, and validation rules are system-definition artifacts because they decide what exists, where it appears, how it validates, and how future writes are interpreted.

**The data model separates entities, reusable fields, types, and config namespaces.** Entities are flexible fieldsets with UIDs, mutable human keys, and internal sequential IDs; fields are reusable schema elements; types select and constrain fields without becoming rigid tables ([entity concept](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/docs/concepts/entity.md), [field concept](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/docs/concepts/field.md), [type concept](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/docs/concepts/type.md)). `openKnowledgeGraph` builds the record schema by reading `Field` and `Type` config entities, so schema is not only code or YAML; it becomes queryable repository state ([knowledge-graph.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/repo/src/knowledge-graph.ts)). That makes config entities strong system-definition artifacts with validation, rendering, query, and agent-write authority.

**Views and navigation are bidirectional projection machinery.** Navigation config maps queries to file paths; views interpolate field slots into markdown and extract edited content back into field values ([navigation concept](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/docs/concepts/navigation.md), [view concept](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/docs/concepts/view.md), [navigation.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/cli/src/document/navigation.ts), [view.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/cli/src/document/view.ts)). Snapshot metadata records rendered paths, entity UIDs, transaction versions, sizes, mtimes, and hashes; `docs render` writes projections while `docs sync` extracts modified files into transaction input ([snapshot.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/cli/src/lib/snapshot.ts), [change-extractor.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/cli/src/document/change-extractor.ts), [docs.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/cli/src/commands/docs.ts)). This gives agents file-native affordances without making files canonical.

**Transactions are immutable, hashed, attributed units of change.** A transaction groups config and record changesets, carries author/tags/message/source/channel metadata, hashes a canonical form, and points at the previous hash ([transaction concept](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/docs/concepts/transaction.md), [transaction.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/repo/src/model/transaction.ts), [transaction-processor.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/repo/src/transaction-processor.ts)). The transaction applier can invert and roll back transactions; the CLI keeps a JSONL transaction log, an undo log, redo support, log verification, and database/log repair paths ([transaction-applier.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/repo/src/transaction-applier.ts), [orchestrator.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/cli/src/lib/orchestrator.ts), [journal.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/cli/src/lib/journal.ts)). The docs describe a broader conflict-free sync ambition; the inspected code most clearly implements local history, undo/redo, repair, and replay.

**The agent API is typed and write-capable, but intentionally small.** MCP currently exposes `schema`, `search`, and `transact` tools; resources are defined as an empty registry but not mounted in the MCP method handler ([mcp index](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/cli/src/mcp/index.ts), [tools index](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/cli/src/mcp/tools/index.ts), [resources.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/cli/src/mcp/resources.ts)). The search tool is read-only; the transact tool can create/update records and config entities through transaction input ([search.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/cli/src/mcp/tools/search.ts), [transact.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/cli/src/mcp/tools/transact.ts)). That is a strong behavioral-authority split: schema and search advise the agent; transact has mutation authority over both knowledge artifacts and system-definition artifacts.

**Editor and HTTP surfaces make the graph a practical workspace, not just a library.** The LSP server provides diagnostics, completion, hover, definition, code actions, inlay hints, semantic tokens, and save-time sync ([lsp index](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/cli/src/lsp/index.ts), [diagnostics.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/cli/src/lsp/handlers/diagnostics.ts), [completion.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/cli/src/lsp/handlers/completion.ts)). The HTTP server serves schema, config, records, transactions, a built-in record browser, and optional user Hono routes from `.binder/web` ([server.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/cli/src/http/server.ts), [serverModule.ts](https://github.com/mpazik/binder/blob/00257e64fe60f3461ccaed5739f51d2bc32eed64/packages/cli/src/http/serverModule.ts)). Binder's memory story is therefore operational: the same retained graph can back editor workflows, scripts, agents, and small custom apps.

## Comparison with Our System

| Dimension | Binder | Commonplace |
|---|---|---|
| Primary substrate | SQLite repository with records, config, and transactions | Markdown files in git |
| File role | Editable projections/snapshots over database state | Canonical authored artifacts |
| Schema | Config entities plus TypeScript/Zod validation | Frontmatter, type specs, collection contracts, validation scripts |
| Main unit | Typed entity with reusable fields and relations | Typed note, reference doc, instruction, ADR, source, review, workshop artifact |
| History | Content-addressed transactions plus JSONL log, undo/redo, repair | Git history plus explicit review/archive workflows |
| Agent surface | MCP tools, CLI, HTTP API, LSP-backed files | Native file access, `rg`, skills, CLI validation/review commands |
| Activation | Agent must query/search/transact or read projected files | Agent navigates indexes, descriptions, links, and files progressively |
| Review/governance | Type validation, LSP diagnostics, transaction audit | Type validation, semantic review, link rules, curated indexes, human-readable diffs |

Binder is the clearest nearby alternative to commonplace's files-first premise. It preserves the human convenience of files while giving the application a typed operational core: queryable entities, relation includes, atomic mutation, transaction metadata, projections, and multiple serving surfaces. Commonplace would need substantial infrastructure to offer the same cross-client consistency.

The tradeoff is authority transparency. In commonplace, the note file is usually the retained artifact and the review target. In Binder, a markdown file is a projection whose behavior depends on schema/config state, navigation rules, view templates, snapshot metadata, transaction history, and extraction logic. That is good engineering for an app, but it means an agent cannot fully audit the memory system by reading the visible markdown tree alone.

Binder also exposes a sharper distinction between knowledge artifacts and system-definition artifacts than many database-backed KBs. A `Task`, `Decision`, `Note`, or `Concept` record is a knowledge artifact when consumed as context or evidence. A `Field`, `Type`, `Navigation`, `View`, LSP validator, MCP tool schema, or transaction processor is a system-definition artifact because it routes, validates, renders, constrains, or mutates later behavior.

**Read-back:** pull — the agent must query/search/transact or choose to read projected files.

## Borrowable Ideas

**Database-backed projected files.** Useful as a comparison pattern, not ready to adopt wholesale. Binder shows how to keep files ergonomic while making a database canonical. Commonplace should remain files-first for methodology notes, but a scoped database for high-volume derived state, snapshots, or review telemetry would be more defensible after seeing Binder's projection machinery.

**Config-as-data for schemas, views, and navigation.** Worth borrowing selectively. Binder's config namespace makes system-definition artifacts queryable and editable through the same transaction path as ordinary records. Commonplace could use this idea for future generated indexes or validation profiles, but only where the current file contracts become too static.

**Transaction metadata with source and channel.** Ready to borrow conceptually. Binder records author, tags, message, source, and channel inside hashed transactions. Commonplace already has git history, but agent-authored transformations could benefit from similarly explicit operation metadata in generated reports or review artifacts.

**Bidirectional projection with conflict checks.** Needs a concrete use case first. Binder's snapshot metadata, diverged-file detection, extraction, diffing, and transaction generation are the right machinery when humans edit derived files. Commonplace mostly edits canonical files directly, so this is useful only if generated views become editable.

**Small MCP surface with mutation behind a transaction contract.** Ready to borrow if commonplace gains MCP service mode. Binder's `schema`, `search`, and `transact` tools keep the agent API compact while making writes auditable through transactions. The important part is not MCP itself; it is placing mutation behind a typed, logged transaction boundary.

## Curiosity Pass

**The README's local-first sync language is broader than the inspected serving layer.** The transaction and changeset model has hashes, inverses, squashing, and rebase concepts; the CLI has repair paths between SQLite and the JSONL log. I did not find a complete remote sync service or multi-device merge protocol in the inspected tree, so the current review treats offline/local history as implemented and conflict-free distributed sync as an architectural direction.

**The markdown projection is powerful but can hide causality.** A user or agent editing a markdown file sees a normal document. The actual write path is extraction, normalization, reference resolution, diffing, transaction processing, save, re-render, and snapshot metadata refresh. That indirection is the cost of letting projected files feel native.

**This is not trace-derived learning.** Binder logs transactions and LLM calls, and it provides skills that instruct agents how to model/import/query Binder workspaces. I did not find an implemented loop that consumes agent/tool/session traces and distills them into durable lessons, rules, prompts, validators, rankers, tools, or model weights. Its learning-like behavior is schema evolution and human/agent data entry, not trace-derived artifact promotion.

**The most transferable mechanism is not the database; it is the authority boundary.** Binder makes every serious write become a transaction, and it lets schema/config changes travel through the same machinery as record changes. That is the part commonplace should study: when a retained artifact can change behavior, the mutation path should be typed, attributable, and reversible.

**Agent memory here is operational state, not reflective knowledge.** Binder is strong at storing tasks, decisions, registries, queues, and typed project context. It has weaker support for claim review, source confidence, semantic link labels, or theory-level distillation. That makes it closer to an agent-accessible work database than to a methodology library.

## What to Watch

- Whether the sync ambitions become a complete multi-device or remote collaboration protocol, or stay as local transaction history plus repair/replay.
- Whether MCP grows resource reads, richer includes, scoped edit guards, or transaction preview/dry-run before mutation.
- Whether projected files gain stronger provenance markers so an agent can see which schema/view/navigation entities shaped a document.
- Whether LLM logs become evidence for system improvement or remain operational audit logs.
- Whether Binder's own skills begin writing durable schema migrations, views, or validators from repeated workspace traces.
- Whether the HTTP app surface becomes the main adoption path, making Binder less a KB and more a local application framework over typed state.

---

Relevant Notes:

- [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) - contrasts: Binder is a strong database-first counterexample that keeps files as projections while making SQLite canonical
- [knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - frames: Binder stores and serves typed operational state, but activation still depends on an agent querying or reading the right surface
- [retained artifact](../../notes/definitions/retained-artifact.md) - clarifies: Binder records, config entities, views, navigation rules, transactions, snapshots, and tool schemas are retained artifacts with different consumers
- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: projected markdown and ordinary records advise users and agents when consumed as evidence or context
- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: fields, types, views, navigation, validators, transaction processors, and MCP tool schemas carry instruction, validation, routing, or mutation authority
- [Atomic](./atomic.md) - compares: both are database-backed personal/agent knowledge systems, but Atomic enriches markdown atoms into chunks/embeddings/wiki views while Binder projects typed graph entities into editable files
- [engraph](./engraph.md) - compares: both bridge markdown and agent access, but engraph keeps a vault-like graph closer to the file surface while Binder makes the database the canonical substrate
