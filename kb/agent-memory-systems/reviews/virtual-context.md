---
description: "Virtual Context review: proxy-owned context virtualization with trace-derived compaction, facts, tag summaries, paging tools, and engineered prompt injection"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-02"
tags: [trace-derived, push-activation]
---

# Virtual Context

Virtual Context, from the `virtual-context/virtual-context` repository, is a Python context-virtualization layer for long-running LLM conversations. It runs as an HTTP proxy, Python engine, CLI, TUI, and MCP server that stores conversation traces, compacts older turns into topic summaries and facts, retrieves relevant retained context, and injects a bounded `<virtual-context>` block into future provider requests.

**Repository:** https://github.com/virtual-context/virtual-context

**Reviewed commit:** [4acad1285455e61ad88db312dc909f1bbeeb2917](https://github.com/virtual-context/virtual-context/commit/4acad1285455e61ad88db312dc909f1bbeeb2917)

**Last checked:** 2026-06-02

## Core Ideas

**The proxy owns the active context window.** The README frames Virtual Context as sitting between the client and upstream provider: the client can send a large conversation history, while VC compresses, indexes, pages, and sends a smaller curated payload to the model ([README.md](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/README.md)). The architecture docs describe the implemented request pipeline: format detection, history ingestion, `on_message_inbound`, context injection, upstream forwarding, then background `on_turn_complete` tagging and compaction ([docs/architecture.md](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/docs/architecture.md)).

**Inbound read-back and post-turn distillation are separate paths.** `VirtualContextEngine.on_message_inbound` delegates to retrieval and assembly before the upstream model call, while `on_turn_complete` tags the completed turn and compacts when thresholds fire ([virtual_context/engine.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/engine.py)). That split matters: read-back can affect the next answer, but compaction and fact extraction affect later turns.

**Context efficiency is explicit, not incidental.** Retrieval tags the inbound message, expands with related tags, scores stored summaries using tag/idf, BM25/FTS-style text, and embedding signals, skips active recent tags when appropriate, and applies result limits and budget fractions ([virtual_context/core/retriever.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/core/retriever.py), [virtual_context/core/retrieval_scoring.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/core/retrieval_scoring.py)). The assembler then allocates a bounded pool across tag sections and facts, trims conversation history to budget, and can serve topics at summary, segment, or full-text depth through a working set ([virtual_context/core/assembler.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/core/assembler.py), [virtual_context/types.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/types.py)).

**Compaction turns traces into layered memory artifacts.** The compaction pipeline loads uncompacted canonical turns outside the protected window, segments them, asks an LLM compactor for summaries and facts, stores segment records, marks canonical turns compacted, builds tag rollups, and stores tag-summary embeddings for later scoring ([virtual_context/core/compaction_pipeline.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/core/compaction_pipeline.py), [virtual_context/core/compactor.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/core/compactor.py)). The prompts emphasize preserving decisions, entities, dates, exact numbers, code refs, and facts from raw conversation text.

**Raw tool and media evidence remains restorable.** Tool output and chain snapshots are stored and linked to turns and segments; the proxy runtime can restore compacted tool output or chain content back into the mutable request body via `vc_restore_tool` ([virtual_context/storage/sqlite.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/storage/sqlite.py), [virtual_context/proxy/handlers.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/proxy/handlers.py)). Media compression similarly stores compressed image metadata and files while replacing or stubbing payload blocks when allowed by the protected-window policy ([virtual_context/proxy/media.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/proxy/media.py)).

**Adoption surfaces are broad.** The package entry point exposes `virtual-context`; the README and docs show proxy, daemon, SDK, MCP, CLI, dashboard, and OpenClaw integration paths ([pyproject.toml](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/pyproject.toml), [README.md](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/README.md)). The MCP server exposes recall, compaction, topic expansion, quote search, fact query, summary search, and status resources over the same engine ([virtual_context/mcp/server.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/mcp/server.py)).

## Artifact analysis

**Canonical turns.** Storage substrate: SQLite or PostgreSQL rows, with filesystem and graph-adjacent stores also present behind the store protocols. Representational form: symbolic records carrying raw user/assistant content, raw provider blocks, normalized hashes, tags, fact signals, code refs, session dates, source batches, and compaction markers. Lineage: trace-derived from live proxy payloads, SDK calls, MCP compaction inputs, and import adapters; canonical rows are source material for later compaction. Behavioral authority: knowledge artifacts as evidence and replay material, plus system-definition authority for lifecycle state because compaction and recovery read their turn ids, hashes, and `compacted_at` status.

**Segments and tag summaries.** Storage substrate: store tables/files for segments, segment tags, tag summaries, tag-summary embeddings, and FTS indexes. Representational form: mixed prose summaries plus symbolic metadata and distributed-parametric embeddings. Lineage: LLM-derived from canonical turns through the segmenter and compactor, with source turn numbers, segment refs, canonical-turn ids, and cover-through metadata. Behavioral authority: advisory knowledge artifacts when injected into prompts; ranking and routing artifacts when their tags, embeddings, and summaries drive future retrieval. The promotion path is raw turn trace to segment summary to tag rollup to prompt-injected memory.

**Facts and fact links.** Storage substrate: `facts`, `fact_tags`, and optional fact-link graph storage. Representational form: symbolic fact records with prose `what` fields, plus relation types such as supersession, contradiction, same-as, and related-to. Lineage: extracted from raw conversation text during compaction, curated and supersession-checked by configured LLM/embedding paths, then stored with segment and conversation provenance ([virtual_context/ingest/supersession.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/ingest/supersession.py)). Behavioral authority: knowledge artifacts when displayed or queried; prompt-time advisory artifacts when selected facts are placed in the `<facts>` block; weak system-definition authority where supersession hides older facts from default queries.

**Retrieval and assembly configuration.** Storage substrate: YAML config, dataclass config objects, model catalog data, and runtime engine state. Representational form: symbolic parameters for context window, budgets, protected turns, tag/fact caps, paging, embedding model, store backend, and provider formats. Lineage: authored operator configuration and presets. Behavioral authority: system-definition artifact: it determines what can enter the model request, what is protected from compaction, how much memory is injected, and when paging tools are available.

**Tool, media, request, and telemetry records.** Storage substrate: store tables for tool outputs, tool calls, turn/segment tool-output links, chain snapshots, media outputs, request captures, request context, and telemetry ledgers. Representational form: symbolic JSON/SQL rows plus binary media files and raw text payloads. Lineage: trace-derived from provider requests, tool results, media blocks, and proxy events. Behavioral authority: mostly evidence and audit knowledge artifacts, but `vc_restore_tool` can give raw evidence direct prompt authority by restoring compacted content into the request body.

**Proxy, MCP, CLI, TUI, and user commands.** Storage substrate: Python code, package metadata, docs, and command handlers. Representational form: symbolic code with natural-language tool descriptions and command names. Lineage: authored integration surface over the engine. Behavioral authority: system-definition artifacts for consumers: they decide how agents and users can recall, compact, expand, restore, attach, label, forget, or inspect memory.

## Comparison with Our System

| Dimension | Virtual Context | Commonplace |
|---|---|---|
| Primary purpose | Runtime context virtualization for long conversations | Agent-operated methodology KB and framework |
| Main retained unit | Conversation turn, segment summary, tag summary, fact, tool/media artifact | Typed Markdown artifact in Git |
| Storage substrate | Service-owned stores: SQLite/Postgres/graph/filesystem, plus media files | Filesystem and Git, with generated indexes and validation outputs |
| Read-back | Both: automatic prompt injection plus explicit tools/commands | Mostly pull through search, indexes, links, skills, and explicit instruction loading |
| Lineage model | Trace-derived, operational, and store-level | Authored/source-grounded artifacts with frontmatter, links, validation, review, and Git history |
| Context strategy | Replace raw history with retrieved summaries, facts, tools, and protected recent turns | Select and load durable knowledge artifacts into agent context by navigation and workflow |

Virtual Context is closer to an operating layer for a live conversation than to a library of curated knowledge. Its strongest design move is owning the provider request path: it can remove stale bulk, inject selected memory, provide tools for deeper paging, and keep raw evidence recoverable. Commonplace deliberately does not own the runtime LLM request; it instead makes retained artifacts reviewable, navigable, and validatable before agents consume them.

The tradeoff is governance. Virtual Context has rich operational lineage and regression coverage, but the central learned artifacts are LLM-derived summaries and facts whose semantic faithfulness is mostly assumed from prompts, tests, and runtime behavior. Commonplace is slower and less automatic, but its artifacts can carry citations, explicit type contracts, review comments, and human-readable argument structure.

Read-back: both - automatic relevance-scored proxy injection pushes selected summaries/facts into the model request, while MCP tools, VC commands, SDK calls, and paging tools provide deliberate pull paths.

### Borrowable Ideas

**Treat context as a budgeted working set.** Ready as a design lens. Commonplace already has indexes and skills, but Virtual Context's summary/segment/full depth model gives a useful vocabulary for progressive disclosure: a note can be visible as a title, abstract, excerpt, full artifact, or source bundle, each with different cost and authority.

**Keep raw trace evidence restorable beside compressed memory.** Ready for workshop tooling. A Commonplace trace-derived workflow should keep raw transcripts, command logs, or review bundles reachable after generating a compact note, instead of letting the summary become the only inspectable object.

**Use source-aware fact supersession cautiously.** Needs a concrete use case. Commonplace could borrow the idea of active/superseded fact rows for workshop state or claims under revision, but durable library notes need citation and review semantics stronger than automatic contradiction checks.

**Separate automatic activation from manual recall.** Ready now as taxonomy. Virtual Context demonstrates that "memory exists" and "memory reaches the next action" are different mechanisms. Commonplace should continue labeling pull navigation, always-load instruction, search retrieval, and relevance-gated push separately.

**Do not borrow opaque summary authority.** Virtual Context must compress at runtime; Commonplace usually has time to cite, review, and validate. Trace-derived Commonplace artifacts should land as candidates with provenance, not as high-authority instructions just because a summarizer produced them.

## Trace-derived learning placement

**Trace source.** Virtual Context qualifies as trace-derived learning. Raw signals include live user/assistant turns, provider payload history, tool calls and tool results, media blocks, imported conversation exports, MCP-supplied message lists, request captures, benchmark conversations, and conversation identity/alias events.

**Extraction.** Extraction is staged. Inbound tagging extracts a query-time signal for immediate retrieval. Post-turn tagging enriches canonical turns with semantic tags, fact signals, code refs, and session metadata. Compaction then turns selected canonical turns into segment summaries, facts, tag summaries, embeddings, supersession relationships, and restorable tool/media references. The extraction oracle is a mixture of deterministic budget/lifecycle logic, embedding and lexical retrieval, LLM tagging/summary/fact prompts, and optional supersession/fact-link checks.

**Scope and timing.** Scope is per conversation, with cross-session and cross-platform continuity through conversation ids, aliases, labels, VCATTACH, and shared stores. Timing is online: inbound retrieval happens before the model call; turn tagging and compaction happen after the response or in background/recovery paths; imports and manual compaction are staged batch paths.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Virtual Context belongs in the deploy-time trace-to-symbolic-and-prose memory family with engineered read-back. It strengthens the survey distinction between raw trace retention and distilled behavior-shaping artifacts: canonical turns, tool outputs, and media are evidence; segment summaries, tag summaries, facts, embeddings, and injected prompt blocks are the behavior-changing layer.

## Read-back placement

**Direction.** Both. From the answering model's perspective, proxy injection is push: selected `<virtual-context>` sections and `<facts>` arrive in the system/instructions field without the model first asking for them. Tool/MCP/CLI paths are pull when an agent or user deliberately asks for recall, quote search, topic expansion, fact query, or restoration.

**Trigger and relevance signal.** The automatic path triggers on an inbound provider request or SDK `on_message_inbound` call. Relevance is engineered from inbound tags, related tags, active-tag skipping, IDF/tag overlap, text search, embedding similarity, alias ride-alongs, fact prefetch, and budget-aware assembly. Precision and recall are not verifiable from static code alone.

**Timing relative to action.** Push read-back occurs before the upstream model call, so it can change the next answer. Tagging, compaction, tag-summary rebuilding, fact extraction, and supersession occur after completed turns or in manual/batch paths, so they can only affect later requests.

**Selection, scope, and complexity.** Selection is constrained by strategy result limits, context-injection budgets, tag and fact caps, protected recent turns, active-tag suppression, working-set depth, and hard prompt budget trimming. Complexity is higher than simple RAG because injected context can include core files, a context hint, tag summaries, segment/full expansions, facts, and restorable tool hints.

**Authority at consumption.** Injected memory is advisory prompt context rather than a hard validator. Tool restoration is stronger for evidence because it can splice raw compacted content back into the mutable request body. Configuration and paging tool definitions have system-definition authority over what the model can request or receive.

**Faithfulness.** The repository has extensive tests for mechanics, storage, retrieval, compaction, and proxy formats, but I did not find a read-back faithfulness test that proves injected memory changes behavior through a WITH/WITHOUT ablation. Treat effective authority as unverified from code.

**Other consumers.** The dashboard, TUI, CLI, MCP resources, telemetry, and tests also consume retained memory. Those surfaces matter operationally but do not change the push/pull classification for the answering model.

## Curiosity Pass

**The OS metaphor is unusually literal.** Virtual Context really does combine protected recent working memory, compressed pages, explicit restore tools, and a managed prompt ceiling. The analogy is more than product language; it appears in storage, retrieval, assembly, and paging code.

**The system is strongest where it controls the transport.** Proxy mode lets VC inject context, stub payloads, restore raw evidence, capture requests, and run background compaction. The MCP server is useful, but without owning the provider request path it is mostly a pull interface.

**Summaries and facts carry a lot of authority for LLM-derived objects.** The code preserves lineage fields and raw restorability, but injected summaries and facts can still shape answers before a human reviews them. That is the central governance risk.

**Tool-output memory is more interesting than ordinary chat memory.** Coding-agent sessions often lose context to tool result bloat. VC's stubs, chain snapshots, segment links, and restore tool make raw tool evidence addressable without keeping all of it in the live prompt.

**The implementation is broader than a simple local package.** The repo includes multi-format proxying, multi-instance support, optional Postgres/graph backends, Redis/session-state concepts, OpenClaw plugin material, dashboard/TUI surfaces, benchmark support, and a large regression test suite. That breadth is impressive, but it also makes the trust boundary harder to audit from one file.

## What to Watch

- Whether trace-derived summaries and facts gain source-span citations or quote anchors back to canonical turns; that would make injected memory more auditable and closer to Commonplace's source-grounded review standards.
- Whether retrieval quality gains explicit prompt-faithfulness or WITH/WITHOUT behavior tests; that would upgrade `push-activation` from structural evidence to measured activation.
- Whether VCATTACH and cross-platform shared memory introduce user-facing provenance controls, because shared conversation stores make stale or misattributed memory more consequential.
- Whether fact supersession becomes more transparent in the dashboard and CLI; hidden invalidation is useful operationally but risky when users need to understand why a fact disappeared.
- Whether paging tools become the dominant path for autonomous models; that would shift the design from proxy-managed push toward a hybrid where the model actively manages its own memory working set.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Virtual Context derives summaries, facts, embeddings, and restorable evidence links from conversation and tool traces, then injects selected memory into later requests.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: live traces can produce retained artifacts that change future agent behavior.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Virtual Context implements both storage and an activation path.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - exemplifies: the system is built around token budgets, compaction, retrieval, and paging depth.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: proxy code, config, tool definitions, and retrieval policies can instruct, route, or constrain behavior.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: canonical turns, raw tool outputs, media, summaries, facts, and request captures are evidence or context until consumed with stronger authority.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - applies: the same retained fact can be evidence in a dashboard, advisory context in a prompt, or suppressed by supersession logic.
- [Lineage](../../notes/definitions/lineage.md) - applies: source turn ids, segment refs, canonical-turn ids, hashes, and compaction markers decide invalidation and auditability.
