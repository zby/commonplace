---
description: "pond review: Lance-backed cross-harness agent-session archive with canonical codecs, scheduled ingestion, BM25/vector recall, read-only MCP/SQL, and pull-only read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-08-03"
---

# pond

pond, by tenequm, is a Rust archive and retrieval layer for AI-agent sessions. It parses histories from multiple coding-agent harnesses into a canonical Session/Message/Part model, stores them in Lance on local or object storage, derives full-text and vector retrieval structures, and serves bounded transcript recall through CLI, HTTP, MCP, and read-only SQL. Its durable target is the trace corpus itself, not a curated fact or lesson store.

**Repository:** https://github.com/tenequm/pond

**Reviewed commit:** [9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808](https://github.com/tenequm/pond/commit/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808)

**Last checked:** 2026-08-03

## Core Ideas

**The canonical session archive is the product.** Pond models a session as messages and typed parts, including conversational text, reasoning, files, tool calls/results, approval events, provider options, project/source metadata, and parent-session links. Adapters preserve source-specific records in the options bag while core types require provenance and prevent several synthesized fallback values, so future agents can inspect what actually happened rather than only a preselected summary ([docs/spec.md](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/docs/spec.md), [packages/pond/src/wire.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/wire.rs), [packages/pond/src/adapter/mod.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/adapter/mod.rs)).

**Cross-harness interchange is implemented as typed codecs.** The adapter registry covers Claude Code, Claude Desktop, Claude.ai export, Codex CLI, OpenCode, OpenClaw, NanoClaw, Hermes, and pi-coding-agent. Each factory discovers/opens one source format and can serialize canonical sessions toward a target format; source extractors and ingest validation enforce identity, ordering, parentage, provenance, and additive writes ([packages/pond/src/adapter/mod.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/adapter/mod.rs), [packages/pond/src/adapter/codex_cli.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/adapter/codex_cli.rs), [packages/pond/src/handlers.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/handlers.rs)). Native and foreign serializers exist, but the inspected CLI does not yet expose restoration into a harness; the production restore helper is explicitly described as future wiring ([packages/pond/src/adapter/mod.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/adapter/mod.rs)).

**Context efficiency comes from selective, progressively deeper reads.** Ingest computes one `search_text` per message from conversational parts and excludes system/tool carrier rows, reasoning, tool bodies, and harness-injected scaffolding from ordinary search. A query chooses either BM25 full-text or vector retrieval, pushes project/session/source/date filters before ranking, excludes subagents by default, groups hits by session, returns roughly 600-character match windows, and exposes whole-session or one-message expansion as separate calls. Search also reports the in-scope message count so an empty result is not silently read as proof that no relevant history exists ([docs/spec.md](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/docs/spec.md), [packages/pond/src/handlers.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/handlers.rs), [packages/pond/src/transport.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/transport.rs)).

**Trace ingestion is staged and can run unattended.** Explicit, scheduled, or in-server sync discovers enabled adapters, skips sources whose watermarks are already represented, streams canonical events through validation, embeds new searchable messages inline, appends them to three Lance datasets, and folds deferred index tails. `pond optimize` handles old or model-stale embedding backlogs through the same embedding seam. This is a durable trace-to-parametric-ranking loop, but it does not infer reusable lessons from the sessions ([packages/pond/src/main.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/main.rs), [packages/pond/src/embed.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/embed.rs), [packages/pond/src/substrate.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/substrate.rs)).

**Trust is preservation- and provenance-oriented, not semantic-review-oriented.** Pond distinguishes conversational from injected parts, records source and ingest-host provenance, makes the canonical store authoritative after ingest, keeps MCP strictly read-only, and validates writes at typed and storage chokepoints. The repository tests codec and storage behavior and carries search benchmarks, but whether a retrieved old session is correct for the present task, and whether an agent follows it faithfully, are not verified by these mechanisms ([docs/spec.md](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/docs/spec.md), [packages/pond/src/wire.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/wire.rs), [packages/pond/src/transport.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/transport.rs)). Adoption is local-first and inspectable at the command/schema level, though Lance datasets are less directly editable than Markdown and the first semantic-search use may download a roughly 500 MB model.

## Artifact analysis

- **Storage substrate:** `files` `service-object` `vector` — The three Lance datasets and their manifests/indexes persist either in a local directory or in an operator-owned S3/GCS/Azure-compatible object store; `messages.vector` and its optional IVF_SQ index provide vector-store behavior over the same dataset ([packages/pond/src/substrate.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/substrate.rs), [packages/pond/src/sessions.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/sessions.rs)).
- **Representational form:** `natural-language` `symbolic` `parametric` — Conversational text and transcript views are natural-language; canonical rows, typed parts, provenance, adapter metadata, schemas, filters, indexes, config, and tool contracts are symbolic; per-message embedding vectors are retained parametric representations used for similarity ranking.
- **Lineage:** `authored` `trace-extracted` `other-compiled` — Configuration, the bundled skill, schemas, and retrieval policy are authored; canonical sessions, `search_text`, and message embeddings are extracted from agent traces; FTS/vector/scalar indexes and row maps are compiled from already-retained dataset columns. A source session growing invalidates the sync watermark, an embedding-model id change invalidates its vectors, and a dataset tail advances the index-fold state ([packages/pond/src/adapter/mod.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/adapter/mod.rs), [packages/pond/src/embed.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/embed.rs), [packages/pond/src/substrate.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/substrate.rs)).
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` — Stored sessions and returned transcript windows are knowledge artifacts for agents and humans; the installed skill instructs agents when and how to recall; tool schemas, adapter/source/project filters, and session/message identifiers route reads; canonical types, ingest checks, storage chokepoints, and read-only SQL/MCP gates validate operations; BM25, cosine, recency, scalar prefilters, and grouping rank recall. Pond does not promote trace content into an enforced rule or reviewed instruction.

**Canonical session corpus.** Sessions, messages, and parts are durable trace-extracted knowledge artifacts. Natural-language conversational content sits inside a symbolic envelope carrying role, timestamps, source agent, project, parentage, typed parts, options, and provenance. The canonical dataset is the retained source of truth; source records needed for faithful reconstruction are carried inside its options rather than kept in a second raw store ([docs/spec.md](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/docs/spec.md), [packages/pond/src/wire.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/wire.rs)).

**Search text, embeddings, and indexes.** `search_text` is a lossy retrieval projection over the value-complete archive: it keeps conversational text and file metadata while excluding other preserved parts. One locally loaded E5/XLM-RoBERTa pass produces one FP16 vector per message, truncated to 512 model tokens with no chunking; BM25 and vector indexes then compile those columns into access structures. These artifacts have ranking authority, not truth authority, and retrieval precision is not verified from source inspection alone ([packages/pond/src/embed.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/embed.rs), [packages/pond/src/sessions.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/sessions.rs)).

**Skill, tool schemas, and configuration.** The bundled `SKILL.md`, MCP instructions/resources, adapter configuration, storage URL/credential rules, and search settings are authored system-definition artifacts. They tell an agent when to use `pond_search`, when to expand a session/message, and when SQL is the correct escape hatch; the MCP surface itself exposes no write tool ([packages/pond/SKILL.md](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/SKILL.md), [packages/pond/src/transport.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/transport.rs), [packages/pond/src/config.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/config.rs)).

**Promotion path.** Pond promotes raw harness histories into a canonical trace archive, a conversational search projection, parametric message vectors, and compiled indexes. This strengthens form and retrieval authority, but not semantic authority: there is no implemented step from a recalled episode to a reviewed fact, procedural rule, validator, or enforced gate.

## Comparison with Our System

Pond and Commonplace both favor operator-owned durable state, explicit provenance, typed boundaries, and agent-facing retrieval commands. Pond is stronger at retaining high-volume execution evidence across heterogeneous harnesses and at serving bounded recall from a corpus too large to load directly. Commonplace is stronger at turning selected evidence into readable, linkable, reviewed artifacts whose type and behavioral authority are explicit.

The systems therefore answer different questions. Pond answers “what happened in prior sessions?” by preserving and ranking traces. Commonplace answers “what should future agents believe or do?” through authored notes, source-grounded reviews, instructions, schemas, and validation. Pond's canonical archive is columnar and operationally robust but not pleasant to hand-edit; Commonplace's Markdown is transparent and version-controlled but is intentionally not a raw event warehouse.

Their trust models also diverge. Pond's no-synthesis and provenance rules protect fidelity to the source trace, while Commonplace's review and citation rules protect the meaning of promoted claims. Combining the two would require an explicit promotion boundary: a Pond result can be evidence for a Commonplace artifact, but relevance rank or recurrence cannot itself grant the artifact authority.

### Borrowable Ideas

**Report retrieval scope even when no result matches.** Ready now for agent-facing search. Pond's `searchable_in_scope` count distinguishes an empty corpus/filter slice from weak relevance, reducing false claims of absence.

**Make heterogeneous import omissions unrepresentable.** Ready for any future Commonplace importer. Pond's sealed extractor values, per-part provenance, and mandatory attribution are a useful shape when several source formats map into one retained model.

**Use a trace archive beneath, not inside, the knowledge library.** Needs a concrete operational use case. Commonplace could use an external Pond-like corpus as evidence for investigations while promoting only selected, cited findings into `kb/`; raw session rows should not become ordinary library notes.

**Expose progressive transcript expansion as separate tools.** Ready where review output references large traces. Search snippets, session pages, and one-message tool-body expansion give agents explicit control over both volume and semantic complexity.

**Do not treat embeddings as review state.** Ready as a constraint. Pond's vectors are rebuildable ranking aids; Commonplace should keep any similar index non-load-bearing and never let similarity substitute for source grounding or semantic review.

## Write side

**Write agency:** `automatic` — Enabled adapters, scheduled sync, `serve --with-sync`, HTTP ingest, inline embedding, backlog optimization, copying, and index maintenance mechanically acquire or derive retained state. Operators configure and trigger these paths, but the corpus has no manual semantic-curation interface comparable to editing a note.

**Curation operations:** `none` — Automatic writes acquire canonical trace rows, produce embeddings, and maintain access structures. The inspected code does not consolidate sessions into summaries, deduplicate semantically similar memories, evolve stored content from later evidence, synthesize new claims, invalidate contradictions while retaining history, decay by age/capacity, or promote recurrent content.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `event-streams` `trajectories` — Adapters consume harness session files/databases and exports containing user/assistant turns, system carriers, reasoning, files, tool calls/results, approvals, subagent links, timestamps, and provider metadata.

**Learning scope:** `cross-task` — One store can accumulate sessions across projects, machines, source harnesses, and time; project, session, source-agent, and date fields scope later retrieval rather than separate the learning store.

**Learning timing:** `offline` `staged` — Normal adapters read histories after they have been written by their harness, either on explicit/scheduled sync or a periodic in-server cycle. Live ingestion while a session is running is explicitly deferred in the reviewed specification ([docs/spec.md](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/docs/spec.md)).

**Distilled form:** `natural-language` `symbolic` `parametric` — The trace becomes retained conversational text, a symbolic canonical/session schema and `search_text` projection, and parametric message embeddings used for future ranking.

**Extraction.** The oracle is mechanical, not an LLM judge: source-specific adapters parse known record shapes, sealed extractors preserve absence instead of inventing values, ingest validation rejects or attributes malformed events, core code decides which conversational parts become `search_text`, and the configured embedding model maps that text to one vector. Pond learns how to retrieve the trace, not what lesson the trace contains.

**Scope and timing.** Sync can run every few minutes and embed new searchable messages in the same append commit, but the source boundary is still a previously persisted harness history. Embedding-model changes cause a staged re-embedding pass; dataset growth causes later index folds, while unfurled tails remain searchable by flat scan.

**Survey fit.** Pond belongs beside deja-vu in the survey's weak-promotion, trace-to-recall branch, but adds a value-complete cross-harness canonical archive, parametric semantic ranking, typed provenance, and object-store scale. It strengthens the survey claim that trace-derived memory can remain a knowledge/ranking artifact and still affect future work without being distilled into lessons, rules, or harness mutations.

## Read-back

**Read-back:** `pull` — Retained sessions reach an agent only after the agent, user, or host explicitly invokes `pond_search`, `pond_get_session`, `pond_get_message`, or `pond_sql`. The bundled skill and MCP tool descriptions encourage those calls but are static routing instructions, not pushed retained memory.

Pull selection is deliberately bounded: a caller chooses vector or BM25, filters by project/session/source/date, raises a capped session limit when needed, then expands only the relevant session or message. Search suppresses injected/tool/reasoning bodies from the first retrieval surface, pages long sessions, and byte-bounds plugin responses. Actual context dilution, retrieval precision, and whether the returned history changes the receiving agent's behavior are not verified from code.

Other consumers include humans using CLI search/get/SQL/status, OpenClaw and Hermes agents through read-only projected tools, HTTP clients, and operators copying or inspecting archives. None of these surfaces automatically injects recalled session content into every model invocation ([packages/openclaw-pond/src/tools.ts](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/openclaw-pond/src/tools.ts), [packages/hermes-pond/tools.py](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/hermes-pond/tools.py)).

## Curiosity Pass

**Pond is deliberately an archive beneath memory, yet it still qualifies as trace-learning here.** It does not extract lessons, but it does transform agent traces into durable parametric embeddings and ranking structures that change which past behavior is retrieved. The `trace-learning` label therefore describes its learned access path, not semantic knowledge distillation.

**“Lossless archive” and “selective search” are compatible because they are separate paths.** Canonical storage preserves tool bodies, reasoning, injected scaffolding, and provider details; ordinary search intentionally omits much of that material and exposes it through later message/SQL expansion. This is a useful separation of preservation from context budgeting.

**The specification overstates implemented erasure.** It specifies `pond erase` as the operator-only append-only exception, but the reviewed sync path only detects some OpenClaw deletions and reports that erasure is pending:

> openclaw: {} explicitly deleted session(s) detected (erase pending; pond erase is not yet implemented): {}
> --- [packages/pond/src/main.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/main.rs)

This leaves the documented byte-purge and resurrection-denylist privacy contract unimplemented at the reviewed revision ([docs/spec.md](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/docs/spec.md)).

**Cross-client continuation is also ahead of its production surface.** Adapter serializers and fidelity tests support the codec claim, but the core source says the production restore CLI “will route through” the helper, and the current `pond copy` restore path restores a Pond archive into a Pond store rather than materializing a session into another agent client ([packages/pond/src/adapter/mod.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/adapter/mod.rs), [packages/pond/src/main.rs](https://github.com/tenequm/pond/blob/9ab0165c1e68f3e3d35eb22ca6e17ed8a07ec808/packages/pond/src/main.rs)).

**One-vector-per-message is a simple but consequential boundary.** It makes embedding cost and lineage clear, while 512-token truncation means semantic rank may ignore the tail of a long message even though the complete content remains retrievable from canonical storage.

## What to Watch

- Whether `pond erase` lands with byte purge plus a resurrection denylist; until then, Pond's preservation guarantee is stronger than its deletion/privacy guarantee.
- Whether adapter serializers gain a production command for restoring a canonical session into a different harness; that determines whether interchange is a usable workflow or mainly a tested internal seam.
- Whether deferred live-write is implemented; it would move trace learning from offline/staged history ingestion toward online capture and change the durability boundary for in-flight events.
- Whether the planned FM-index for `parts.variant_data` lands; indexed tool-body substring search would reduce the need for scoped SQL scans and make tool traces a first-class retrieval surface.
- Whether the deferred versioned-document consumer is activated; that would make Pond a knowledge/memory store as well as an archive and force new authority, curation, and read-back decisions.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Pond retains a large session corpus, but memory read-back remains explicit pull through search/get/SQL.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: canonical traces, search projections, embeddings, indexes, skills, and config carry different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: archived sessions and retrieved transcript windows serve as evidence, reference, and context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: adapter contracts, tool schemas, the bundled skill, validation, and ranking policy shape how traces are written and consumed.
- [Use trace extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) - qualifies: Pond derives durable retrieval state from traces but stops before lesson or rule extraction.
- [Rule-based context selection needs a pre-existing signal](../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) - relates: project, session, source-agent, date, role, provenance, and message ids provide explicit retrieval signals alongside inferred lexical/vector relevance.
