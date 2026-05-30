---
description: "Incremental Python/Rust indexing engine whose flow definitions maintain derived vector, graph, table, and file targets from source artifacts"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-05-16"
---

# CocoIndex

CocoIndex is CocoIndex's Python-facing, Rust-backed framework for declaring data transformation apps that keep external indexes in sync with source state. It is relevant to agent memory as an indexing substrate: source files, database rows, meeting transcripts, session logs, and other artifacts can be transformed into derived vector, graph, table, file, or stream targets for later retrieval by agents and LLM applications. The framework does not make the exported index canonical knowledge; the authoritative behavior-shaping surface is the flow code plus connector contracts that decide how targets are maintained.

**Repository:** https://github.com/cocoindex-io/cocoindex

**Reviewed commit:** [40336d5c45e24738008ca8b254f2f6da483cb6e5](https://github.com/cocoindex-io/cocoindex/commit/40336d5c45e24738008ca8b254f2f6da483cb6e5)

## Core Ideas

**The flow definition is a system-definition artifact.** A CocoIndex app binds `AppConfig`, a Python main function, arguments, and an environment, then `update()` turns that function into a root component processor ([app wrapper](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/python/cocoindex/_internal/app.py), [Rust app](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/rust/core/src/engine/app.rs)). The docs frame this as state-driven programming: target state is declared as a function of source state, and the engine computes the change set ([core concepts](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/docs/src/content/docs/programming_guide/core_concepts.mdx), [target state guide](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/docs/src/content/docs/programming_guide/target_state.mdx)). That flow code has instruction, routing, validation, and update authority over the derived artifacts.

**Incrementality is persisted as operational tracking state, not hidden in target stores.** CocoIndex requires a database path and stores target-state and memoization state in LMDB ([internal storage docs](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/docs/src/content/docs/advanced_topics/internal_storage.mdx), [environment setup](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/rust/core/src/engine/environment.rs)). The schema distinguishes component memoization, function memoization, tracking info, child-existence entries, tombstones, target-state owner indexes, and id sequencer state ([state schema](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/rust/core/src/state/db_schema.rs), [state-store ops](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/rust/core/src/state_store/ops.rs)). This LMDB state is a system-definition artifact: it decides what can be skipped, updated, deleted, backfilled, or cleaned up on later runs.

**Function memoization combines input fingerprints, code fingerprints, and explicit dependency fingerprints.** The `@coco.fn` wrapper computes logic fingerprints from canonicalized AST or explicit version values, folds in declared `deps`, and can enable memoization at component or transform level ([function implementation](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/python/cocoindex/_internal/function.py)). File-like sources add memo-state validation using modification time plus content fingerprint, so a changed mtime can still reuse work if content is unchanged ([file resource](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/python/cocoindex/resources/file.py)). This is not semantic learning; it is symbolic invalidation and reuse.

**Connector contracts separate desired target declarations from imperative side effects.** Target handlers reconcile desired state, previous tracking records, and possible missingness into actions, tracking records, and optional child invalidation ([target-state contract](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/python/cocoindex/_internal/target_state.py), [Rust target contract](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/rust/core/src/engine/target_state.rs)). The pre-commit path compares declared states with tracked states, handles ownership preemption, invokes connector reconciliation, stores new tracking records, and prunes stale entries after commit ([execution reconciliation](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/rust/core/src/engine/execution.rs)). The connector contract is therefore the key system-definition surface for correctness.

**Exported targets are derived retrieval artifacts.** Postgres tables and vector indexes, Qdrant collections and points, graph targets, LanceDB tables, SQLite tables, local files, Kafka messages, and similar targets are maintained by connector-specific handlers rather than authored as canonical notes ([Postgres target](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/python/cocoindex/connectors/postgres/_target.py), [Qdrant target](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/python/cocoindex/connectors/qdrant/_target.py), [connectors package](https://github.com/cocoindex-io/cocoindex/tree/40336d5c45e24738008ca8b254f2f6da483cb6e5/python/cocoindex/connectors)). Query wrappers live in examples, such as pgvector and LanceDB code search, not as a uniform framework retrieval layer ([pgvector code example](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/examples/code_embedding/main.py), [LanceDB code example](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/examples/code_embedding_lancedb/main.py)).

**Inspection and operations expose engine state, not knowledge review.** The CLI can list apps, show stable paths from code or a database, run updates, run live updates, reset, and drop target state ([CLI](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/python/cocoindex/cli.py), [CLI docs](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/docs/src/content/docs/cli_commands.mdx)). The inspect API iterates stable paths and node types, which helps debug update topology but does not evaluate whether indexed knowledge is true, useful, or well connected ([inspect API](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/python/cocoindex/_internal/inspect_api.py)).

## Comparison with Our System

| Dimension | CocoIndex | Commonplace |
|---|---|---|
| Primary artifact | Python app plus connector declarations | Typed markdown notes, references, ADRs, instructions, reviews |
| Storage substrate | LMDB operational state plus external targets | Git-tracked files, generated indexes, validation reports |
| Derived artifacts | Vector/table/graph/file/message targets | Directory indexes, reports, review outputs |
| Authority surface | Flow code, context keys, connector handlers, LMDB tracking | Type specs, collection contracts, AGENTS.md, skills, validation/review commands |
| Retrieval surface | Target-store queries and example wrappers | `rg`, descriptions, authored links, curated indexes, connect reports |
| Lineage | Stable paths, target-state tracking records, memo fingerprints, source connector state | Source snapshots, frontmatter, links, git history, validation/review records |
| Evaluation | Convergence to declared target state and connector reconciliation | Fidelity, semantic review, link health, writing conventions, human-readable claims |

CocoIndex is strongest where commonplace intentionally stays weak: maintaining high-volume derived indexes from changing source artifacts. It treats a retrieval table or graph as a compiled view that should be regenerated or reconciled from source and code. That is closer to a build system or materialized view engine than to a library of reviewed claims.

Commonplace is stronger where the retained artifact itself needs reviewable meaning. A CocoIndex vector row can carry provenance fields if the flow author adds them, but the framework does not impose claim status, semantic links, review state, source confidence, retirement rationale, or navigation contracts. The exported index is a knowledge artifact when an agent queries it for evidence or context; the flow definition and connector contract are system-definition artifacts because they decide what gets exported, invalidated, deleted, and reprocessed.

The most important boundary is source-of-truth status. In CocoIndex, source artifacts and flow definitions are authoritative, LMDB tracking state is operational authority, and target stores are derived projections. In commonplace, the note or instruction is usually the canonical retained artifact, while generated indexes are secondary views.

## Borrowable Ideas

**Compiled retrieval targets with explicit source authority.** Commonplace could eventually use a CocoIndex-like pipeline to maintain vector or graph projections from notes and sources, while keeping markdown and snapshots canonical. Useful later; not needed until retrieval scale or latency makes current navigation insufficient.

**Connector-style reconciliation for generated views.** The `desired + previous tracking + may-be-missing -> action + tracking record` contract is a clean pattern for derived indexes. Commonplace generated indexes and reports currently rebuild simply; richer compiled views could borrow this when partial updates matter.

**Stable-path inspection for agent debugging.** `cocoindex show --tree` makes the update topology visible. A similar "what stable units does this KB operation own?" view could help debug review bundles, index generation, or workshop artifacts. Ready as a diagnostic idea, not an implementation priority.

**Memo-state hooks for expensive extraction.** File mtime plus content fingerprint is a practical invalidation pattern for sources where metadata changes more often than content. Commonplace snapshot and review workflows could reuse the idea when repeated parsing becomes expensive.

**Agent-facing skill bundled with the framework.** CocoIndex ships a `skills/cocoindex/` directory explaining the current API to coding agents, explicitly to reduce hallucinated old APIs ([agent-skill docs](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/docs/src/content/docs/getting_started/ai_coding_agents.mdx), [skill](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/skills/cocoindex/SKILL.md)). Commonplace already uses skills, but CocoIndex is a useful external example of treating agent instructions as part of the shipped developer surface.

## Curiosity Pass

**This is not trace-derived learning by default.** CocoIndex can index agent session traces, and the `entire_session_search` example embeds AI coding session transcripts, prompts, context summaries, and metadata into Postgres for semantic search ([session-search example](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/examples/entire_session_search/main.py)). That is a trace-derived retrieval projection for one example, not a framework-level loop that distills agent traces into durable lessons, rules, skills, validators, rankers, or model weights. I therefore did not classify CocoIndex itself as trace-derived learning.

**The docs say "fresh context," but the implementation is an index maintenance engine.** Freshness is real: live local filesystem sources use watchers, live components process updates through an operator, and `cocoindex update -L` keeps the app running after catch-up ([localfs live source](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/python/cocoindex/connectors/localfs/_source.py), [live component API](https://github.com/cocoindex-io/cocoindex/blob/40336d5c45e24738008ca8b254f2f6da483cb6e5/python/cocoindex/_internal/live_component.py)). But activation remains downstream: an agent must query or be given the maintained target.

**Connector correctness is the main risk.** The framework's promise depends on each connector faithfully representing external state with tracking records and reconciliation actions. Postgres, Qdrant, and similar connectors encode fingerprints and managed-by policies, but different backends have different atomicity and schema-change behavior.

**The internal state is behavior-shaping but not human-friendly.** LMDB tracking records are precise enough for incremental execution, not for ordinary source review. That is fine for an engine, but it means auditability for agents should live in flow code, target schemas, and explicit exported provenance fields rather than in the LMDB database.

## What to Watch

- Whether CocoIndex adds a first-class query service or MCP server over maintained targets, rather than leaving retrieval wrappers in examples and downstream apps.
- Whether source connectors beyond local filesystem gain live change feeds and strong content fingerprints, especially database and SaaS sources.
- Whether target connectors converge on consistent provenance fields so every exported vector, row, or graph edge can trace to a source artifact and flow version.
- Whether the agent-session search example grows into trace-derived artifact promotion, such as lessons, rules, validators, or prompt updates.
- Whether inspection tools expose target-state lineage and memo hits in a form an agent can use during debugging.

---

Relevant Notes:

- [knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - frames: CocoIndex maintains retrieval artifacts, but activation still depends on downstream query and prompt assembly
- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: flow definitions, connector contracts, context keys, and tracking state instruct or enforce later updates
- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: exported indexes advise agents when queried as evidence or context
- [lineage](../../notes/definitions/lineage.md) - clarifies: stable paths, memo fingerprints, tracking records, and source fields are lineage mechanisms for derived projections
- [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) - contrasts: CocoIndex appropriately uses a database for operational tracking while leaving source artifacts and flow code outside the engine state
