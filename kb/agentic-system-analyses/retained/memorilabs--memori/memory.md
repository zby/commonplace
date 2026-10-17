---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Memori memory production, selective context delivery, withdrawal and service-dependent restoration across SDKs and agent integrations."
run-id: AAS-2026-10-17-memori-fd4a0418c09b-01
source-identity: https://github.com/MemoriLabs/Memori
reviewed-boundary: 574b1ea3e876f100ef82c37817d603eb7e258e59
---

# Memori memory report

## Boundary and evidence

The memory boundary follows the supplied runtime: Python interception and explicit operations, TypeScript hooks and synthetic capture, native augmentation/retrieval, shipped host integrations, hosted MCP guidance and benchmark consumers. It includes conversation rows, derived facts, vectors, summaries, graph triples, process attributes, agent trace payloads and requested resume representations. It excludes implementations of provider inference, external hosts, databases and hosted Memori services, not their shipped client contracts. The boundary remains a complete artifact with a partial service-dependent loop; local storage does not imply local derivation. Source identity and revision follow [boundary](boundary.md#source-register).

All direct reads below are SRC-1 implementation evidence unless marked doctrine/design. The checkout HEAD was rechecked against the frozen revision. No target code, notebook, provider or service was executed. Supplied runtime findings are used explicitly where source inspection was not repeated. Available but uninspected adapters and frameworks remain included uncertainties, not access gaps or evidence of uniform behavior.

| Operation or part | Source paths and inspection basis | Coverage, or missing fact and conclusion prevented |
|---|---|---|
| Python registered invocation, streams and example | Supplied runtime; `memori/llm/invoke/invoke.py`, `memori/llm/invoke/iterator.py`, `examples/sqlite/main.py` | [RT-RTE-python-invocation](runtime.md#rt-rte-python-invocation), [RT-RTE-stream-exhaustion](runtime.md#rt-rte-stream-exhaustion); generic streaming cannot be assigned non-streaming augmentation semantics. Framework-specific stream completeness remains uninspected. |
| Local and cloud SDK recall; explicit recall and deletion | Direct: `memori/__init__.py`, `memori/memory/recall.py`, `memori/llm/pipelines/recall_injection.py`, `memori/llm/pipelines/conversation_injection.py` | [MEM-RTE-fact-selection](#mem-rte-fact-selection), [MEM-RTE-entity-withdrawal](#mem-rte-entity-withdrawal); manual recall is data return, not proof of a later consumer. |
| Python derivation and queued writes | Direct: `memori/memory/augmentation/augmentations/memori/_augmentation.py`, `memori/memory/augmentation/_db_writer.py`; supplied manager/registry findings | [RT-RTE-augmentation-admission](runtime.md#rt-rte-augmentation-admission), [RT-RTE-augmentation-extension](runtime.md#rt-rte-augmentation-extension), annotations below. Hosted extraction/admission criteria unavailable. |
| Native derivation, fallback and retrieval | Direct: `core/src/augmentation/pipeline.rs`, `core/src/retrieval/pipeline.rs`, `core/src/search/api.rs`; supplied worker/embedding findings | [MEM-OBJ-entity-fact](#mem-obj-entity-fact), [MEM-RTE-fact-selection](#mem-rte-fact-selection); native mock and raw-content fallback qualify the service-derived-only reading. Binding execution and adapter support for fallback operations are uninspected. |
| SQLite content, lineage and access metadata | Direct relevant classes: `memori/storage/drivers/sqlite/_driver.py`; migration mention constraints located by search | Objects below. Other SQL/Mongo drivers and TypeScript storage bridges are available but not independently audited; no all-driver deduplication, cascade or transaction claim. |
| TypeScript before/after and explicit agent APIs | Direct recall engine: `memori-ts/src/engines/recall.ts`; supplied persistence/augmentation and integration-base findings | [RT-RTE-typescript-hooks](runtime.md#rt-rte-typescript-hooks) plus annotation; explicit recall/summary/compaction APIs are requested delivery, not unsolicited push. |
| Hermes, Claude Code, OpenClaw capture and read-back | Supplied runtime routes; direct CLI dispatch search, Hermes tool-schema search, OpenClaw feedback and compaction implementations | [RT-RTE-hermes-provider](runtime.md#rt-rte-hermes-provider), [RT-RTE-claude-skill](runtime.md#rt-rte-claude-skill), [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks), [MEM-OBJ-agent-memory](#mem-obj-agent-memory), [MEM-RTE-feedback-submission](#mem-rte-feedback-submission). Host compliance and hosted result construction unavailable. |
| MCP explicit durable admission | Supplied runtime's source-grounded doctrine: `docs/memori-cloud/mcp/skills/memori-mcp/SKILL.md` | [RT-RTE-mcp-guidance](runtime.md#rt-rte-mcp-guidance); distinct policy from ambient Claude capture, no server enforcement inferred. |
| Evaluation indexes, answers and judgments | Direct: `benchmarks/README.md`, selected decoded code cells of `benchmarks/01_load_indexes.ipynb`, `benchmarks/02_run_benchmark.ipynb` | [MEM-OBJ-benchmark-artifacts](#mem-obj-benchmark-artifacts), [MEM-RTE-benchmark-reload](#mem-rte-benchmark-reload). External downloaded memories/dataset/model were not acquired; no verified benchmark result or production-feedback connection. |

## Core ideas

1. **Two retained layers have different lineage.** Conversation rows retain formatted messages, not the complete original execution trace. Derived facts and summaries come from a service response or explicit native alternatives. Mention links can reconnect facts to conversation summaries, but this is not an extraction-reason record. See [MEM-OBJ-conversation-message](#mem-obj-conversation-message), [MEM-OBJ-entity-fact](#mem-obj-entity-fact) and [MEM-OBJ-conversation-summary](#mem-obj-conversation-summary).
2. **Retrieval budgets act before model context.** Local recall first bounds candidate embeddings, then ranks facts, then applies a relevance threshold for injection. Associated summaries expand the delivered text beyond the fact count. History replay is separately selected by conversation/session and is not governed by that fact threshold. A top-k setting is therefore not a token budget for the complete request. See [MEM-RTE-fact-selection](#mem-rte-fact-selection) and the runtime-route annotations.
3. **Authority changes at delivery.** Stored text is passive until a later request receives it. SDK code places facts and summaries in system/instruction channels with relevance guidance. Agent integrations return tool data under prompts asking for contextual evidence or resume-state use. Neither placement establishes model obedience, truth, safe instruction precedence or learning benefit. See [RT-BAP-recalled-context](runtime.md#rt-bap-recalled-context), [RT-BAP-host-memory-guidance](runtime.md#rt-bap-host-memory-guidance).
4. **Maintenance is not uniform retraction.** SQLite duplicate admission updates access metadata rather than replacing fact content. Summary updates replace a conversation field. Entity deletion removes facts and graph entries but deliberately preserves conversations; later replay can still carry old material. Feedback submission is not an implemented fact-correction or deletion route. See [MEM-OBJ-fact-access](#mem-obj-fact-access), [MEM-RTE-entity-withdrawal](#mem-rte-entity-withdrawal), [MEM-RTE-feedback-submission](#mem-rte-feedback-submission).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-conversation-message
Label: Persisted conversation messages

Source-native identity: `memori_conversation_message`, read through `ConversationMessages.read`. Representational form: natural-language content in symbolic role/type/identity envelopes. Storage substrate: configured database; SQLite is directly inspected. Lineage: provider-adapted request/response through the writer, or explicit captured turn, not necessarily untouched source messages. Consumer: later session/conversation replay injects role/content values into model requests. No separate retained tool-call linkage is established by the SQLite read shape. This differs from transient [RT-OBJ-recall-context](runtime.md#rt-obj-recall-context) and is retained state used by [RT-RTE-python-invocation](runtime.md#rt-rte-python-invocation), not a duplicate invocation route. Evidence: SRC-1, `memori/storage/drivers/sqlite/_driver.py`, `memori/llm/pipelines/conversation_injection.py`; supplied runtime persistence account.

> SELECT role,
>                        content
>                   FROM memori_conversation_message
>                  WHERE conversation_id = ?
>                  ORDER BY id
> --- `memori/storage/drivers/sqlite/_driver.py`

The OpenAI-compatible sanitizer drops tool rows and blank assistant rows and normalizes `model` to `assistant`. Responses-style replay additionally drops system rows. This is lossy restoration, not faithful tool-trace replay (SRC-1, `memori/llm/pipelines/conversation_injection.py`).

> if role == "tool":
>             continue
>         if role == "assistant" and not (content or "").strip():
>             continue
> --- `memori/llm/pipelines/conversation_injection.py`

#### MEM-OBJ-entity-fact
Label: Derived entity fact content

Source-native identity: `memori_entity_fact.content`. Representational form: natural-language text, including text flattened from semantic triples. Storage substrate: database rows, distinct from their numerical embeddings and access metadata. Lineage: Python service facts or triple-derived text; Rust accepts string facts, object `content`, or flattened triple fields. Its `use_mock_response` branch can instead use supplied/default mock memory; if a parsed response produces no operations and input `content` exists, it emits `upsert_fact` with that content. This is a write-batch capability, not proof each adapter supports the operation. Thus not every emitted memory operation represents accepted service-derived knowledge. Evidence: SRC-1, `core/src/augmentation/pipeline.rs`, `memori/memory/augmentation/augmentations/memori/_augmentation.py`, `memori/storage/drivers/sqlite/_driver.py`.

Closest supplied records: this is durable input behind [RT-OBJ-recall-context](runtime.md#rt-obj-recall-context), not that transient display object. Production overlaps [RT-RTE-augmentation-admission](runtime.md#rt-rte-augmentation-admission), annotated below. Later consumer: recall selectors and then provider context; stored content does not itself command a model. SQLite exact duplicate identity uses `generate_uniq([fact])`; conflict increments count/time instead of replacing content or embedding. Truth, conflict reconciliation and semantic consolidation remain service-policy gaps, not consequences of deduplication.

> if ops.is_empty() {
>         if let Some(content) = input.content.clone() {
>             ops.push(WriteOp {
>                 op_type: "upsert_fact".to_string(),
> --- `core/src/augmentation/pipeline.rs`

#### MEM-OBJ-content-embedding
Label: Stored fact embeddings

Source-native identity: `content_embedding` / `fact_embeddings`. Representational form: dense numerical, distributed-parametric representation of fact text; not updated model weights. Storage substrate: database embedding field, with runtime retrieval accepting numerical buffers or a base64 fallback. Producer: selected embedding model; native attachment aligns vectors with embeddable fact positions and checks nonzero signal. Python can schedule fact writes without embeddings after embedding failure. Initial model choice and version provenance are not stored by these inspected write payloads as an immutable vector-generating artifact identity. Consumer: similarity search, not a natural-language model interpreting the vector as instructions. Distinct from [RT-CMP-sentence-transformers-embedder](runtime.md#rt-cmp-sentence-transformers-embedder) and [RT-CMP-tei-embeddings](runtime.md#rt-cmp-tei-embeddings), which compute vectors. Evidence: SRC-1, `core/src/augmentation/pipeline.rs`, `core/src/retrieval/pipeline.rs`, `memori/memory/augmentation/augmentations/memori/_augmentation.py`.

> logger.warning(
>                 "Embeddings failed; writing AA facts without embeddings. %s",
> --- `memori/memory/augmentation/augmentations/memori/_augmentation.py`

Writing text without a vector establishes storage, not that every dense recall path can retrieve it. Native retrieval rejects incompatible dimensions; zero/empty/missing-vector behavior varies by path and adapter and was not exhaustively checked.

#### MEM-OBJ-fact-access
Label: Fact access metadata and mention links

Source-native identity: SQLite fact `uniq`, `num_times`, `date_last_time`, and `memori_entity_fact_mention`. Representational form: symbolic hashes, identifiers, counters, timestamps and joins. Storage substrate: database columns and relation rows. Lineage: fact admission and fact-to-conversation attachment, not a model-authored explanation. Later consumers: `get_embeddings` orders the bounded candidate pool by recency, count and ID; `get_facts_by_ids` joins mention links to current nonempty conversation summaries. These metadata can change what text reaches a later model without themselves being delivered as instructions. Distinct from [RT-OBJ-recall-context](runtime.md#rt-obj-recall-context), which contains selected display text rather than this access structure. Evidence: SRC-1, `memori/storage/drivers/sqlite/_driver.py`.

> ORDER BY date_last_time DESC,
>                           num_times DESC,
>                           id DESC
>                  LIMIT ?
> --- `memori/storage/drivers/sqlite/_driver.py`

> ON CONFLICT(entity_id, uniq) DO UPDATE SET
>                     num_times = num_times + 1,
>                     date_last_time = datetime('now')
> --- `memori/storage/drivers/sqlite/_driver.py`

Repeated content can therefore refresh candidate eligibility without revising its meaning. Mention links provide source-conversation association, not reasons for trusting the extracted assertion.

#### MEM-OBJ-conversation-summary
Label: Mutable conversation summary

Source-native identity: `memori_conversation.summary`. Representational form: natural language; stored as a field in a symbolic row. Storage substrate: configured database, directly checked in SQLite. Producer: augmentation response mapped to `conversation.update`; SQLite overwrites the field without a version-history operation in this method. Consumers: Python's next augmentation reads it and selects the latest user/assistant pair when one exists; fact recall joins mention-linked summaries and formats them into later model context. Summary text is thus both input to further derivation and indirect model-facing memory. No separate retained extraction rationale is present in the inspected summary write/read payload. This durable object is distinct from summary text copied into [RT-OBJ-recall-context](runtime.md#rt-obj-recall-context). Evidence: SRC-1, `memori/storage/drivers/sqlite/_driver.py`, `memori/memory/augmentation/augmentations/memori/_augmentation.py`, `memori/llm/pipelines/recall_injection.py`.

> UPDATE memori_conversation
>                SET summary = ?
>              WHERE id = ?
> --- `memori/storage/drivers/sqlite/_driver.py`

> return [messages[user_idx], messages[assistant_idx]]
> --- `memori/memory/augmentation/augmentations/memori/_augmentation.py`

The Rust payload instead sets `summary: None`; the Python recursive-summary lineage cannot be generalized to the native augmentation route (SRC-1, `core/src/augmentation/pipeline.rs`). A summary may contain reasons in ordinary prose, but these clients establish no required reason field or later reason-directed critic.

#### MEM-OBJ-knowledge-graph
Label: Semantic triples and graph rows

Source-native identity: `semantic_triples`, `memori_knowledge_graph`, subject/predicate/object rows. Representational form: symbolic graph relations whose names/content carry natural language. Storage substrate: database graph tables. Lineage: service response normalization, with subject/type, predicate and object/type used in SQLite insertion and duplicate handling. Consumer established here: graph writer and entity deletion. A separate later graph-query-to-model route is uninspected; the inspected fact recall reads facts and embeddings, not graph traversal. Text synthesized from triples has the separate fact route. This is a distinct output part of [RT-RTE-augmentation-admission](runtime.md#rt-rte-augmentation-admission), not another name for all memory. Evidence: SRC-1, `memori/storage/drivers/sqlite/_driver.py`, `memori/memory/augmentation/augmentations/memori/_augmentation.py`, `core/src/augmentation/pipeline.rs`.

> ctx.add_write(
>                 "knowledge_graph.create",
>                 entity_id,
>                 memories.entity.semantic_triples,
>             )
> --- `memori/memory/augmentation/augmentations/memori/_augmentation.py`

Local initialization/admission is software-driven under application configuration, not inspected per-content human approval. Hosted triple proposal policy is unavailable. A graph label alone establishes no knowledge warrant or behavioral authority.

#### MEM-OBJ-process-attribute
Label: Derived process attributes

Source-native identity: `process.attributes` / `memori_process_attribute`. Representational form: natural-language attribute content plus symbolic process identity and duplicate counters. Storage substrate: configured database. Lineage: augmentation response, admitted when a process ID resolves and attributes are present; SQLite upserts repetition metadata. Consumer established here: storage writer; later model-facing retrieval of process attributes is uninspected in the inspected SDK recall routes. Their presence cannot be counted as delivered skills or operative self-improvement. Distinct from the provider/model components and from [RT-OBJ-recall-context](runtime.md#rt-obj-recall-context). Evidence: SRC-1, `memori/memory/augmentation/augmentations/memori/_augmentation.py`, `memori/storage/drivers/sqlite/_driver.py`.

> ctx.add_write(
>                 "process_attribute.create", process_id, memories.process.attributes
>             )
> --- `memori/memory/augmentation/augmentations/memori/_augmentation.py`

#### MEM-OBJ-agent-memory
Label: Hosted agent memory and resume representations

Source-native identity: agent recall, recall summary and compaction responses. Representational form: client-visible symbolic JSON with natural-language values; private retained representation is uninspected. Storage substrate: hosted service, not the tool-result message itself. Lineage: submitted user/assistant turns and optional traces/summaries under [RT-RTE-hermes-provider](runtime.md#rt-rte-hermes-provider), [RT-RTE-claude-skill](runtime.md#rt-rte-claude-skill), [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks) and the documented [RT-RTE-mcp-guidance](runtime.md#rt-rte-mcp-guidance). Native versus cloud payload coverage differs as the runtime notes. Raw trace submission is not proof the service preserves each tool result or a derivation rationale.

Actual consumer affordance/wiring: a requesting host agent receives JSON/text tool results. Compaction guidance describes environment, standing orders, active tasks, timeline, workspace changes, continuation and recent messages; these are advertised output fields, not inspected actual service responses. There is no source-grounded private-store ontology or claim that each field is independently persisted. Closest supplied record [RT-BAP-host-memory-guidance](runtime.md#rt-bap-host-memory-guidance) describes authority, not this opaque retained/output boundary. Evidence: SRC-1, `integrations/openclaw/src/tools/memori-compaction.ts`, `memori-ts/src/engines/recall.ts`; supplied host routes.

> const result = await client.agentCompaction(finalParams);
> --- `integrations/openclaw/src/tools/memori-compaction.ts`

> content: [{ type: 'text' as const, text: JSON.stringify(result) }],
> --- `integrations/openclaw/src/tools/memori-compaction.ts`

Compaction requests a new resume representation after context loss; it is not evidence this client removes old host context or directly restores a checkpoint. Tool default `numMessages` guidance is 5, with about 20 suggested only on user request; schema and pass-through do not enforce that as a hard budget. Server-side truncation and fidelity are unavailable.

#### MEM-OBJ-benchmark-artifacts
Label: Benchmark memory indexes and evaluation reports

Source-native identity: `indexes_gemma/<conv_id>/faiss.index`, `metadata.json`, and `results_gemma/eval_<timestamp>.json`. Representational form: numerical dense index; natural-language memory/context/summary metadata with symbolic session/timestamp links; natural-language generated answers and judgments plus symbolic labels/metrics. These parts have different consumers: FAISS selects IDs, metadata renders context, answer model consumes prose, judge compares answer with gold, JSON reports retain results for readers. Storage substrate: local files written by notebooks. Initial memories come from an external preaugmented JSON URL, not an inspected run of this repository's production extractor. Metadata copies each memory plus session, summary and timestamp. No immutable embedding artifact digest is set in the inspected notebook model construction; no training step is inspected. Actual downloaded weights and remote answer-model resolution remain uninspected. This is distinct from production provider inference in [RT-CMP-provider-model](runtime.md#rt-cmp-provider-model) and production fact storage. Evidence: SRC-1, `benchmarks/01_load_indexes.ipynb`, `benchmarks/02_run_benchmark.ipynb`, `benchmarks/README.md`.

> - **Input:** `advanced_augmented_memories.json` (downloaded automatically if missing).
> - **Output:** `indexes_gemma/<conv_id>/` directories, each containing `faiss.index` and `metadata.json`.
> - Re-run this notebook whenever the memory data or embedding model changes.
> --- `benchmarks/README.md`

### Routes

#### MEM-RTE-fact-selection
Label: Bounded local fact selection

Part of: [RT-RTE-python-invocation](runtime.md#rt-rte-python-invocation)

This route record isolates the Python invocation's retrieval subroute; it is not a duplicate whole invocation. Endpoints/progression: extracted user query and resolved entity → query embedding → bounded database embeddings → cosine candidate pool → content/summary fetch → dense/lexical rank → top facts → threshold → formatted provider context. Owner: deterministic SDK/native selection rules, with parametric query embedding. Retained inputs are [MEM-OBJ-entity-fact](#mem-obj-entity-fact), [MEM-OBJ-content-embedding](#mem-obj-content-embedding), [MEM-OBJ-fact-access](#mem-obj-fact-access), [MEM-OBJ-conversation-summary](#mem-obj-conversation-summary). Delivery follows [RT-BAP-recalled-context](runtime.md#rt-bap-recalled-context). The record's scope is the invocation-local read path; manual recall returns data without establishing an arbitrary caller's later consumption.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ranked facts to the injection pipeline, then modified provider kwargs; original request when gates yield no content.
- Later read-back: selected fact and associated summary text reaches the next registered inference request, by value.
- Delegated visibility: selector sees entity-scoped embeddings and fetched candidate content; provider sees formatted selected text, not the complete store or vector pool.
- Selection predicate: entity/storage/query gates; Python defaults to 1000 embedding rows, 5 facts and threshold 0.1; native candidate limit scales fact limit by 10 with floor 50, bounded by loaded rows before ranking.
- Invalidation or expiry: candidate recency/count ordering and later writes change eligibility; entity withdrawal removes facts from later database selection but cannot revoke text already delivered.
- Activation or effect: context construction and provider delivery are wired; changed answer quality or obedience is unobserved.
- Evidence limits: no token ceiling for combined fact, summary and replay text is established here; all-driver ordering and embedding compatibility are uninspected; hosted selection is opaque.

Evidence: SRC-1, `core/src/retrieval/pipeline.rs`, `core/src/search/api.rs`, `memori/search/_core.py`, `memori/_config.py`, `memori/storage/drivers/sqlite/_driver.py`, `memori/llm/pipelines/recall_injection.py`. Python fallback likewise forms a dense candidate pool and reranks by weighted lexical and cosine scores. This is relevance selection, not semantic validation or a human admission decision.

> rank_score: (w_cos * cos_score) + (w_lex * lex_score),
> --- `core/src/search/api.rs`

> # Keep summaries scoped to the same relevant fact subset we inject.
> --- `memori/llm/pipelines/recall_injection.py`

The hook automatically initiates this selection on a model call; it is not an independent unsolicited push outside that invocation. Summary deduplication prioritizes one summary per fact before additional unique summaries. Count limits on facts therefore do not limit summary length or history length.

#### MEM-RTE-entity-withdrawal
Label: Entity memory withdrawal preserving conversations

Endpoints/progression: application calls `delete_entity_memories` → BYODB/type/length checks → resolve entity → graph deletion → fact deletion. Owner: caller chooses entity; software performs deletion, with no separate human content-approval step established. State/effects: database graph and fact rows are removed, graph orphan nodes cleaned in SQLite; conversation rows and summary fields are not targeted by these calls. This is a distinct public maintenance route, not the expiry field of [RT-RTE-python-invocation](runtime.md#rt-rte-python-invocation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: None after deletion calls, or validation/runtime exception; missing storage/entity prerequisites can produce no action.
- Later read-back: subsequent fact retrieval no longer selects deleted rows; preserved conversation messages remain eligible for replay and existing conversation summaries remain eligible for subsequent augmentation input.
- Delegated visibility: database methods receive resolved entity ID; no model call or automatic host-context rewrite is performed by this route.
- Selection predicate: BYODB mode and explicit or configured external entity ID; deletion targets all facts/graph entries for the resolved entity.
- Invalidation or expiry: destructive deletion; no undo/history restoration is implemented by these methods; already injected contexts are unaffected.
- Activation or effect: local delete commands wired, not observed; no complete forgetting or service erasure guarantee.
- Evidence limits: database cascade enforcement is not tested; other driver cleanup semantics, concurrent pending augmentation, remote copies and re-derivation are not resolved by this route.

Admission/rejection: application supplies the destructive change; code permits it only in BYODB and validates supplied identity shape. Caller can decline invocation, but caller identity alone does not establish a human decision. Guidance is the public API's preserve-conversations contract. Operating mode: maintenance in open application use, no answer oracle or improvement curriculum. Recovery beyond thrown errors is uninspected; the two delete calls are not established as one all-or-nothing transaction. Evidence: SRC-1, `memori/__init__.py`, `memori/memory/recall.py`, `memori/storage/drivers/sqlite/_driver.py`.

> """Delete memory records for an entity while preserving conversations."""
> --- `memori/__init__.py`

> self.config.storage.driver.knowledge_graph.delete_by_entity(entity_id)
>         self.config.storage.driver.entity_fact.delete_by_entity(entity_id)
> --- `memori/memory/recall.py`

#### MEM-RTE-feedback-submission
Label: Agent integration feedback submission

Endpoints/progression: host tool or CLI feedback dispatch → client feedback request → hosted endpoint → success/error result. Owner: foreground agent supplies feedback text, possibly at user request; client transmits it. No local memory editor, fact ID target or rollback instruction is established by this path. It is a distinct operation discovered beside [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks), [RT-RTE-hermes-provider](runtime.md#rt-rte-hermes-provider) and [RT-RTE-claude-skill](runtime.md#rt-rte-claude-skill), not a duplicate capture or recall route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: success JSON or caught error in OpenClaw; CLI posts content and reports result.
- Later read-back: uninspected — hosted retention and any product/memory change consumer are unavailable.
- Delegated visibility: feedback content reaches the agent feedback service; OpenClaw also logs supplied content.
- Selection predicate: tool/CLI selected with required content; tool guidance requests immediate use for Memori feedback/bug/feature complaints.
- Invalidation or expiry: uninspected — client offers no inspected feedback withdrawal or memory-revision transaction.
- Activation or effect: request dispatch wired; no demonstrated correction of stored facts, extraction policy or later behavior.
- Evidence limits: feedback endpoint internals and maintainers' use are unavailable; a feedback label cannot establish an operative learning loop.

Evidence: SRC-1, `integrations/openclaw/src/tools/memori-feedback.ts`, `integrations/claude-code/index.ts`, `integrations/hermes/src/memori_hermes/tools.py`, `memori/__init__.py`. This is submission, not established admission of knowledge/product changes. Proposer is the tool caller; downstream deciding/vetoing principal and oracle are unknown. Routine user feedback is not a bounded optimization mode.

> await client.agentFeedback(params.content);
> --- `integrations/openclaw/src/tools/memori-feedback.ts`

#### MEM-RTE-benchmark-reload
Label: Benchmark index reload and answer evaluation

Endpoints/progression: external preaugmented JSON → notebook memory encoding and saved FAISS/metadata files → later benchmark notebook reload → hybrid search → formatted memories and unique session summaries → answer generation → gold-answer judge → timestamped result JSON. Owners: notebook code selects and formats; external models generate answers and judge labels. Context/state: per-conversation indexes and supplied questions. This route has no supplied counterpart after comparison with runtime's production routes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: notebook outputs and file writes; per-question answer records include selected context and formatted memory text.
- Later read-back: notebook 02 reloads index and metadata written by notebook 01 and delivers selected content to the answer model; report consumers beyond file output are uninspected.
- Delegated visibility: answer model receives formatted selected memories/summaries and question; judge receives question, gold answer and generated answer, not an automatically proven causal account of retrieval.
- Selection predicate: per-conversation index, query embedding and query text; default top-k 10, dense and BM25 pools each up to twice top-k, reciprocal rank fusion; summary text deduplicated across selected documents.
- Invalidation or expiry: README requests rebuild after data/model changes; notebook download helper keeps an existing input file. No automatic data/version invalidation or production-memory replacement established.
- Activation or effect: file reload, context formatting and model requests are implemented; benchmark operation and numerical benefit are not verified here.
- Evidence limits: downloaded memory provenance and dataset validity, actual model artifacts, notebook stored outputs and baseline comparability are not independently audited; no production admission consumer is established for saved judgments.

Oracle: dataset gold answer is the reference outcome; an LLM compares it with the generated answer and parser extracts CORRECT/WRONG, retaining raw judgment text and errors. Mode: bounded benchmark evaluation, unlike open SDK traffic. It does not propose/admit a successor memory or extractor in the inspected generation/judging/save cells; improved capacity does not follow from writing accuracy metrics. Evidence: SRC-1, `benchmarks/01_load_indexes.ipynb`, `benchmarks/02_run_benchmark.ipynb`; following documentation is doctrine corroborated by the inspected cells.

> | [`02_run_benchmark.ipynb`](02_run_benchmark.ipynb) | Loads the LoCoMo benchmark questions, retrieves relevant memories via hybrid search (FAISS + BM25), generates answers with an LLM, judges correctness, and reports accuracy metrics. |
> --- `benchmarks/README.md`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-augmentation-admission](runtime.md#rt-rte-augmentation-admission)

Memory lineage splits into fact text, numerical embeddings, symbolic graph structure, process attribute text and mutable summary text, declared separately above. Software admits mapped service response fields to queued writes without an inspected per-item human truth check. Human authorship of original conversation is not equivalent to approving extracted memory. Initial hosted store creation/admission remains unknown without obscuring known client transformations (SRC-1, `memori/memory/augmentation/augmentations/memori/_augmentation.py`, `core/src/augmentation/pipeline.rs`).

Python summary reuse feeds prior derived text plus selected latest messages into further derivation; Rust currently sends no prior summary. The native mock and raw-content fallback are additional admission alternatives. They qualify, rather than invalidate, the normal non-mock service dependency. Fact mention links preserve conversation association; retained extraction reasons and a later rationale-consuming route are not established. No claim of beneficial trace learning follows from this raw-to-derived-to-context chain.

Queued writes have weaker completion semantics than successful derivation. The Python writer groups tasks by connection factory, executes them, flushes/commits and attempts rollback on failure. SQLite driver methods inspected above also commit internally; therefore the outer batch rollback is not an established atomic transaction across all derived parts. Queue saturation may reject enqueue; failed batches are not shown here being requeued. These facts supplement the supplied runtime's best-effort background guarantee, not observed failure (SRC-1, `memori/memory/augmentation/_db_writer.py`, `memori/storage/drivers/sqlite/_driver.py`).

> except queue_module.Full:
>             return False
> --- `memori/memory/augmentation/_db_writer.py`

#### On [RT-RTE-python-invocation](runtime.md#rt-rte-python-invocation)

Fact-context retrieval is selected by query and entity; history replay separately reads the current cached/resolved conversation. In SQLite the history reader returns every matching role/content row in ID order, not a similarity-selected tail. Summary reuse does not itself replace those conversation rows or establish host-window compaction. Cloud history is opaque selected input from recall, while replay sanitization remains local. The provider receives text by value, not dereferenceable retained pointers. No sub-agent frame creation/isolation is implemented by these request-building functions (SRC-1, `memori/llm/pipelines/conversation_injection.py`, `memori/storage/drivers/sqlite/_driver.py`).

#### On [RT-RTE-typescript-hooks](runtime.md#rt-rte-typescript-hooks)

Local recall requests 100 dense candidates and 10 results, unlike Python defaults. Fact threshold affects rendered facts and summaries; history is separately sanitized and prepended. Local history sanitation drops tools and blank assistants; cloud additionally drops system rows. Thus rejection of all fact context does not necessarily reject conversation history. Local manual recall returns data only; hook wiring establishes the later provider consumer (SRC-1, `memori-ts/src/engines/recall.ts`).

> dense_limit: 100,
>       limit: 10,
> --- `memori-ts/src/engines/recall.ts`

#### On [RT-BAP-host-memory-guidance](runtime.md#rt-bap-host-memory-guidance)

The resume-state route requests behavioral use of standing orders and expected formats, not merely factual question answering. Its source trust rule asks for checking stale operational details and preserving newer user authority; enforcement is model interpretation, not a hard client-side priority control. Project/session/date/source/signal filters select requested namespaces/categories, but private service ranking and authorization remain unknown. The client serializes the response as text without a local field-level trust transformation (SRC-1, `integrations/openclaw/src/tools/memori-compaction.ts`, `memori-ts/src/engines/recall.ts`; supplied host guidance record).

## Write side

The ordinary completed-turn chain is capture → retained conversation → service-dependent derivation → typed write mapping → database → later selection. The generic streaming exhaustion route differs: supplied [RT-RTE-stream-exhaustion](runtime.md#rt-rte-stream-exhaustion) establishes conversation persistence without that generic iterator's augmentation dispatch. Early termination and background lifetime weaken universal capture promises; they are not proof all integrations lose memory.

Admission mechanisms must stay separate. Application configuration admits augmentation classes; automatic handlers admit mapped response fields; an intentional MCP agent judges whether a turn is durable enough to submit; Claude's skill instead requests ambient turn capture, with foreground-agent-authored payloads. None establishes per-item human approval of derived facts. Hosted derivation and rejection remain opaque. These distinctions are grounded in the supplied runtime routes, not generalized from one SDK.

Known curation includes latest-turn selection against an existing summary, triple-to-text conversion, vector attachment, duplicate-count refresh, summary-field replacement, summary deduplication for display and history sanitation. Each changes a different part; no single label such as augmentation establishes semantic correction. [MEM-OBJ-fact-access](#mem-obj-fact-access) explains why refreshing recency can change future recall even when fact content stays fixed.

Withdrawal is [MEM-RTE-entity-withdrawal](#mem-rte-entity-withdrawal), not complete erasure. Feedback is [MEM-RTE-feedback-submission](#mem-rte-feedback-submission), not demonstrated memory editing. Summary replacement and direct library deletion are the inspected material mutation surfaces; a general end-user editor, semantic conflict-resolution protocol, per-fact revision history, retention schedule and cloud erasure implementation remain unavailable or uninspected, not evidenced absences. Evaluator writes are isolated in [MEM-RTE-benchmark-reload](#mem-rte-benchmark-reload); their output is a report, not an inspected production-memory update.

## Read-back

There are three established consumer forms. SDK hooks automatically request selection at invocation time and deliver facts/summaries in provider context, plus separately replayed history. Host agents intentionally request recall/summary/compaction and receive tool text. Benchmark notebooks reload saved artifacts and deliver retrieved text to an answer model, then a separate gold-based judge. The library's manual recall API alone establishes no unspecified application's consumption route.

The automatic SDK route is invocation-triggered selection, not independent unsolicited supply. Selection inputs are query/entity for facts and conversation/session for history. Agent APIs add project/session/date/source/signal selectors; the Claude CLI refuses `--query`, whereas public Python agent recall accepts an optional query argument and the documented MCP route permits query-based use. Do not infer identical selector contracts from the shared recall name (SRC-1, `integrations/claude-code/index.ts`, `memori/__init__.py`; supplied [RT-RTE-mcp-guidance](runtime.md#rt-rte-mcp-guidance)).

Working-context control is selective restoration and sanitation. Old tool payloads can remain in external retained sources while being omitted from replay. Compaction requests a derived brief and recent tail after host context loss; this repository's client does not prove which original details survive hosted derivation, what the host removed or whether a resume field is faithful. There is no separately inspected isolated sub-agent frame here. The stack-frame analogy is therefore limited: these routes assemble context values rather than demonstrate a pushed/popped child context whose return alone escapes. Database IDs are selectors used by code, not model-dereferenceable heap references. Relevant load-bearing evidence is retained in the object records, route records and supplied authority paths.

## Integration issues

- **Qualification to service-derived-only admission:** [MEM-OBJ-entity-fact](#mem-obj-entity-fact) and the annotation on [RT-RTE-augmentation-admission](runtime.md#rt-rte-augmentation-admission) add the native mock branch and empty-operations/content fallback from SRC-1, `core/src/augmentation/pipeline.rs`. The normal non-mock path still calls the service. Reconciliation should not classify every possible emitted operation as service-approved extraction, nor treat fallback emission as proven adapter persistence.
- **No record duplicates identified:** durable object records differ from the runtime's transient [RT-OBJ-recall-context](runtime.md#rt-obj-recall-context); [MEM-RTE-fact-selection](#mem-rte-fact-selection) is explicitly part of [RT-RTE-python-invocation](runtime.md#rt-rte-python-invocation). Host memory overlaps authority and route descriptions but identifies their unresolved retained/output object, not a replacement route. Feedback, withdrawal and evaluator reload have distinct operations and consumers.
- **Graph/process consumer gap:** [MEM-OBJ-knowledge-graph](#mem-obj-knowledge-graph), [MEM-OBJ-process-attribute](#mem-obj-process-attribute) have inspected production/storage, but no established later model-facing consumer independent of triple-derived fact text. Their stored presence must not be promoted to operative knowledge/skill use.
- **Hosted admission and compaction gap:** [MEM-OBJ-agent-memory](#mem-obj-agent-memory), [RT-RTE-augmentation-admission](runtime.md#rt-rte-augmentation-admission), [RT-RTE-mcp-guidance](runtime.md#rt-rte-mcp-guidance) retain unknown service policy, reasons, revisions, retention and extraction fidelity. Source schemas and prompt field lists do not establish actual opaque payload contents or reliable current-user priority.
- **Partial forgetting and concurrency:** [MEM-RTE-entity-withdrawal](#mem-rte-entity-withdrawal) preserves replayable conversations. Pending augmentation, concurrent writers and future re-derivation are not canceled by the inspected deletion wrapper. This prevents system-wide forgetting/revocation claims.
- **Access and transaction limits:** [MEM-OBJ-fact-access](#mem-obj-fact-access) is SQLite-specific, and the augmentation annotation identifies internal commits versus outer rollback. Other adapters/bindings remain available but uninspected; no all-driver atomicity, tenant isolation or identical selection claim follows.
- **Evaluation is not deployed update evidence:** [MEM-RTE-benchmark-reload](#mem-rte-benchmark-reload) identifies a bounded answer/judge/report route with external initial memory provenance. No inspected connection installs judged results into production memory. Stored outputs were not audited, so no numerical performance conclusion is adopted.

## Limitations and checks

The source and method identity were rechecked against the supplied invocation, member type, record contract and frozen checkout HEAD. New coverage is itemized above; inherited runtime evidence is distinguished from direct reads. Target execution, tests, providers, network fetches and extra sources were not used. Source-code wiring establishes delivery capacity, not exercised recall, faithful derivation, improved future capacity, causally effective model behavior or reliable hosted operation. Facts without embeddings, private compaction construction, separate graph/process consumers, cross-adapter semantics and unanalyzed framework-specific wrappers remain explicit limits.

Deterministic validation: the invocation's `commonplace-run validate-output` check passed after writing this candidate. Its scope is structure, identity, relation and quotation checks, not semantic acceptance or target operation.
