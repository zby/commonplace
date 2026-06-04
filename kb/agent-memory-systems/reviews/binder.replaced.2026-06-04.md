---
description: "Binder review: local-first typed knowledge graph with Markdown views, transactions, CLI/MCP/LSP access, and agent-facing skills"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: outdated
tags: []
last-checked: "2026-06-01"
---

# Binder

> Replaced 2026-06-04. See [Binder](./binder.md) for the current review.

Binder, from Marek Pazik's `mpazik/binder` repository, is a local-first knowledge graph for tools, scripts, editors, and agents. It stores typed entities and schema configuration in a SQLite-backed repository, renders selected records as Markdown or YAML files, records every accepted change as a transaction, and exposes the same graph through a CLI, MCP server, LSP/editor integrations, HTTP API, library API, hooks, and installable agent skills.

**Repository:** https://github.com/mpazik/binder

**Reviewed commit:** [da86cb6166e207099a205076107cf626da16ba56](https://github.com/mpazik/binder/commit/da86cb6166e207099a205076107cf626da16ba56)

**Last checked:** 2026-06-01

## Core Ideas

**The primary memory is a typed graph, not a folder of notes.** Binder defines records as field-value entities classified by type, with fields and types themselves stored as configuration entities. The README frames Markdown as a view over the graph, while the repo package implements `fetchEntity`, `search`, `update`, `apply`, `rollback`, schema loading, relation-aware search, and transaction listing over SQLite tables for records, configs, and transactions ([README.md](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/README.md), [packages/repo/src/knowledge-graph.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/knowledge-graph.ts), [packages/repo/src/schema.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/schema.ts)).

**Schema is data with operational authority.** Field and type definitions are not only documentation. They are loaded from the config namespace into a record schema, merged with core schema, and used to validate mandatory fields, option constraints, relation targets, and value data types before transactions are accepted ([packages/repo/src/knowledge-graph.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/knowledge-graph.ts), [packages/repo/src/changeset-processor.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/changeset-processor.ts), [.binder/types.yaml](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/.binder/types.yaml), [.binder/fields.yaml](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/.binder/fields.yaml)).

**Markdown files are synchronized projections with edit-back semantics.** Navigation config maps queries or `where` clauses to paths and views. The renderer materializes records and config entities into files, while extraction parses Markdown/YAML back into fieldsets and projections. This gives humans and agents an inspectable file surface without making the file tree the only source of truth ([packages/cli/src/document/navigation.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/document/navigation.ts), [packages/cli/src/document/repository.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/document/repository.ts), [packages/cli/src/document/extraction.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/document/extraction.ts), [.binder/navigation.yaml](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/.binder/navigation.yaml)).

**Transactions are the governance layer.** Updates become immutable transaction records with hashes, previous hashes, author, optional tags/message/source/channel metadata, record/config changesets, and timestamps. The CLI keeps a JSONL transaction journal beside the SQLite state, verifies database/log divergence, supports undo/redo, and rerenders files after accepted changes ([packages/repo/src/transaction-applier.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/transaction-applier.ts), [packages/cli/src/lib/journal.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/lib/journal.ts), [packages/cli/src/lib/orchestrator.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/lib/orchestrator.ts), [packages/cli/src/commands/transaction.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/commands/transaction.ts)).

**Agents get structured read/write tools rather than a prompt-only memory.** Binder exposes an MCP server with `schema`, `search`, and `transact` tools; the CLI supports read/search/create/update/delete/transaction workflows; and the repository ships agent skill files for CLI use, schema modeling, import, and app-building ([packages/cli/src/mcp/tools/index.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/mcp/tools/index.ts), [packages/cli/src/mcp/tools/search.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/mcp/tools/search.ts), [packages/cli/src/mcp/tools/transact.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/mcp/tools/transact.ts), [skills/binder-cli/SKILL.md](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/skills/binder-cli/SKILL.md)).

## Artifact analysis

- **Storage substrate:** `sqlite` — `.binder/data/binder.db`, opened through `@binder/repo/local` with SQLite/Drizzle migrations and WAL-oriented pragmas ([packages/repo/src/local/constants.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/local/constants.ts), [packages/repo/src/db.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/db.ts))
- **Representational form:** `symbolic` — Symbolic tables containing JSON field blobs for records, configs, and transactions
- **Lineage:** `authored` `imported` — authored records, schema config, navigation, skills, and transactions can enter through files, CLI/MCP writes, init blueprints, transaction imports, and rendered-file sync; the review does not identify trace-extracted learning artifacts
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` — projected files, search results, and logs act as knowledge; skills and tools instruct use; schema, transactions, validation, navigation, and editors enforce, route, and validate state changes

**Workspace graph state.** Storage substrate: `.binder/data/binder.db`, opened through `@binder/repo/local` with SQLite/Drizzle migrations and WAL-oriented pragmas ([packages/repo/src/local/constants.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/local/constants.ts), [packages/repo/src/db.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/repo/src/db.ts)). Representational form: symbolic tables containing JSON field blobs for records, configs, and transactions. Lineage: authored or tool-applied transaction inputs become normalized transactions, applied changesets, and current record/config state. Behavioral authority: system-definition artifact for future reads and writes, because the graph is the authoritative substrate for schema, records, relations, and versioned rollback.

**Schema configuration entities.** Storage substrate: config namespace rows in SQLite, plus YAML file projections such as `.binder/types.yaml`, `.binder/fields.yaml`, and `.binder/navigation.yaml` in this repository's own Binder workspace. Representational form: symbolic YAML/JSON fieldsets. Lineage: authored through files, transaction imports, CLI/MCP writes, or init blueprints, then loaded into the runtime schema. Behavioral authority: system-definition artifact with validation, routing, and rendering force. The schema decides what a valid record can be, which relations are allowed, and where entities appear on disk.

**Markdown/YAML document views.** Storage substrate: workspace files under the configured docs path, with navigation-controlled paths and generated config files under `.binder/`. Representational form: mixed prose and symbolic slots/frontmatter/YAML lists. Lineage: derived views from the graph during render, and possible edit sources during sync or LSP workflows. Behavioral authority: knowledge artifacts when read as context by humans or agents; soft system-definition artifacts when edited back into transactions because parsed fields can change the authoritative graph. The promotion path is explicit: prose/file edits must survive extraction, validation, and transaction application before they become graph state.

**Transaction log and undo log.** Storage substrate: SQLite `transactions` table, `.binder/data/transactions.jsonl`, and `.binder/data/undo.jsonl` ([packages/cli/src/config.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/config.ts), [packages/cli/src/lib/journal.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/lib/journal.ts)). Representational form: symbolic JSON and JSONL transaction objects. Lineage: generated from accepted transaction inputs and rollback/redo operations. Behavioral authority: audit and enforcement artifact for repair, undo/redo, replay, and divergence checks. It is not trace-derived learning by itself because the log is not mined into new rules, prompts, validators, rankers, or tools in the inspected implementation.

**MCP and CLI tools.** Storage substrate: TypeScript command/tool definitions in `packages/cli/src/commands/` and `packages/cli/src/mcp/tools/`. Representational form: symbolic code plus natural-language tool descriptions. Lineage: authored interface code over the same knowledge graph APIs. Behavioral authority: system-definition artifacts for agents and scripts because they constrain reads and writes to typed schemas and transaction inputs. As read-back, these are pull tools: an agent or user asks for schema/search/read/write explicitly.

**LSP/editor integration and validation.** Storage substrate: TypeScript language-server code, VS Code extension code, and IntelliJ plugin packaging. Representational form: symbolic code and diagnostics/completion rules. Lineage: authored integration over workspace discovery, document parsing, schema context, validation, and file rerender notifications ([packages/cli/src/lsp/workspace-manager.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/lsp/workspace-manager.ts), [packages/cli/src/lsp/document-context.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/lsp/document-context.ts), [packages/cli/src/validation/engine.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/validation/engine.ts), [integrations/vscode/README.md](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/integrations/vscode/README.md)). Behavioral authority: advisory and validation authority for human/editor workflows, not an agent memory push path.

**Agent skill files.** Storage substrate: `skills/binder-*` Markdown files. Representational form: prose instructions with YAML frontmatter names and descriptions. Lineage: authored operational guidance for using Binder's CLI, modeling, import, and app-building surfaces. Behavioral authority: system-definition artifacts only when a host skill system installs and loads them; inside Binder itself they are reference material. I did not find router tests or a Binder-owned relevance gate comparable to an activation benchmark.

**LLM and import examples.** Storage substrate: `.binder/logs/llm.jsonl` for LLM call accounting, plus the journal example scripts. Representational form: symbolic JSONL logs and TypeScript scripts with prompt text. Lineage: LLM calls append usage/error logs; `git-import-logs.ts` can derive journal entries from git commits using an external LLM ([packages/cli/src/lib/llm.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/lib/llm.ts), [packages/cli/src/lib/llm-log.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/packages/cli/src/lib/llm-log.ts), [examples/journal/git-import-logs.ts](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/examples/journal/git-import-logs.ts)). Behavioral authority: knowledge artifact or generated record input depending on use. These do not qualify as trace-derived agent learning in the current review because git commits and LLM-call accounting are not agent execution traces being distilled into durable behavior-shaping policy.

### Borrowable Ideas

**Use a transaction ledger as the spine for reversible KB work.** Commonplace has git history and review artifacts, but Binder's transaction objects are domain-level and can carry author/source/channel metadata. Worth borrowing for generated KB operations that need replay, undo, and semantic audit before they become commits. Ready for a workshop prototype, not core migration.

**Separate graph authority from document affordance.** Binder's file views are convenient for humans and agents, while the typed graph remains the authority. Commonplace could borrow this as a future layer for structured indexes or task/workshop state where Markdown is a view, not the only database. Needs a strong use case because Commonplace currently benefits from Git-native simplicity.

**Make navigation rules executable.** Binder's navigation config turns type/status fields into file placement, including archive movement. Commonplace already has collection contracts and generated indexes; a Binder-like symbolic placement layer could help for workshop artifacts with lifecycle transitions. Ready as a comparison lens; implementation should wait.

**Expose the same substrate through CLI, MCP, LSP, and HTTP.** Binder's most practical design move is not any single interface, but the shared graph API underneath them. Commonplace should keep this as a pressure test for future commands: if a workflow matters, can it be consumed by shell, agent, editor, and browser without duplicating semantics?

**Do not borrow the weak trace story.** Binder's transaction and LLM logs are useful audit records, but they are not distilled behavior change. Commonplace should preserve the distinction between logging activity and learning from traces.

## Comparison with Our System

| Dimension | Binder | Commonplace |
|---|---|---|
| Primary purpose | Local-first typed graph for small tools, agents, editors, scripts, and apps | Methodology KB and framework for agent-operated knowledge bases |
| Main retained unit | Entity/config/transaction in SQLite, projected as Markdown/YAML | Typed Markdown artifact in Git, governed by collection/type contracts |
| Schema authority | Runtime validation and rendering authority from config entities | Frontmatter/type specs, validation scripts, review gates, and collection contracts |
| Read/write surface | CLI, MCP, library API, HTTP, LSP/editor, file sync | Files, CLI validators/indexers/review commands, skills, git |
| Audit model | Domain transaction chain plus JSONL journal and undo/redo | Git diffs/commits plus validation/review artifacts |
| Agent memory posture | Structured pull database for agents to query and mutate | Curated knowledge and instructions that agents navigate, validate, and revise |

The strongest alignment is that both systems treat stored knowledge as an operative artifact rather than passive documentation. Binder formalizes that as a graph: schema, navigation, records, transactions, and views are data that the runtime executes. Commonplace formalizes it as a repository: collection contracts, type specs, notes, instructions, indexes, and validation scripts are files that agents can read and tools can check.

The main divergence is the source of authority. Binder's authority sits in a live local database and transaction processor, with Markdown as an editable projection. Commonplace's authority sits in Git-tracked Markdown plus typed conventions; the system relies on validation and review rather than a runtime graph enforcing every state transition.

Binder is more operational for small apps and agent-accessible state. It gives agents a schema tool, search tool, and transaction tool over a typed store. Commonplace is stronger as a durable methodology library: citations, review sections, cross-note links, and prose argument structure matter more than low-latency CRUD.

**Read-back:** `pull` — For agent memory in the reviewed implementation. Agents can deliberately call MCP/CLI/search/read tools or use installed skill guidance, but I did not find a Binder-owned relevance-gated push mechanism that injects memories before action

## Write-side placement

**Write agency:** `automatic` `manual` — the review describes system-driven generation, extraction, consolidation, or update of retained artifacts rather than only manual authoring.

**Curation operations:** `dedup` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

## Curiosity Pass

**The agent-memory claim is strongest for shared structured state.** Binder is compelling when agents, scripts, and people need to coordinate around typed records, queues, tasks, decisions, or registries. It is less like episodic recall and more like a local operational database with transparent views.

**The Markdown sync boundary is the hard part.** The design promises bidirectional sync, but that means path interpolation, frontmatter extraction, view slots, relation projections, orphan cleanup, and divergence handling all become semantic machinery. The repo has substantial code and tests around these surfaces, which suggests the feature is central rather than incidental.

**Transactions are audit, not learning.** Binder records who changed what and can undo/replay changes. That is valuable lineage, but it does not by itself extract lessons or change future behavior except through the resulting graph state.

**The skills are adjacent to the product, not the product's routing engine.** The checked-in `skills/` directory gives agents good operating instructions, but the inspected Binder runtime does not own the host skill router. Treating those files as evidence for engineered push activation would overstate the implementation.

**The repository uses Binder on itself.** The `.binder/` directory contains real schema/navigation config for tasks, milestones, problems, decisions, use cases, features, concepts, and notes. That makes Binder an unusually concrete self-example of the product's intended operating mode ([.binder/README.md](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/.binder/README.md), [.binder/types.yaml](https://github.com/mpazik/binder/blob/da86cb6166e207099a205076107cf626da16ba56/.binder/types.yaml)).

## What to Watch

- Whether full-text or semantic search lands in the roadmap; that would change Binder from structured pull memory to a broader retrieval substrate, but still would not imply activation without a trigger policy.
- Whether transaction log compaction preserves enough lineage for undo, provenance, and review; compaction can easily weaken the audit value that makes Binder attractive for agents.
- Whether the MCP surface adds resources or richer read tools beyond `schema`, `search`, and `transact`; that would affect how much context an agent can inspect before deciding to mutate state.
- Whether the skills gain activation fixtures, router benchmarks, or host integration metadata; that would make a future `push-activation` tag more defensible.
- Whether LLM-assisted scripts move from examples into core workflows that mine transactions, documents, or tool traces into schema changes, rules, or validators; that would be the line where trace-derived placement might become relevant.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Binder stores and exposes structured memory, but agent use is still mostly deliberate pull.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: Binder schema, navigation, transactions, validators, and tool definitions can instruct, route, validate, or enforce future behavior.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: projected Markdown, transaction history, search results, and LLM logs are evidence or context until a consumer grants stronger authority.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - sharpens: the same Binder field can be advisory when read, validating when schema-enforced, and routing when used in navigation.
- [Lineage](../../notes/definitions/lineage.md) - applies: Binder's transaction chain and rendered-file derivation model make provenance and invalidation visible.
- [Storage substrate](../../notes/definitions/storage-substrate.md) - applies: Binder shows why the distinction between SQLite graph, JSONL journal, and Markdown projection matters operationally.
