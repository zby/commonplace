---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Hindsight memory: extracted facts, observation consolidation, living knowledge pages, curation and bounded later delivery, with partial shipped-consumer coverage."
run-id: AAS-2026-10-14-hindsight-34c2ca821edf-01
source-identity: "https://github.com/vectorize-io/hindsight"
reviewed-boundary: "610c135b6f2d0d8b972da94146ae635943f36271"
---

# Hindsight memory report

## Boundary and evidence

The subject is Hindsight's retained-content loop at the frozen Git boundary in [boundary](boundary.md#boundary-and-evidence). Scope follows the supplied retention, reflection and Claude Code routes, but also includes discovered service-side consolidation, knowledge-page creation/refresh, curation, registered MCP tools, CLI dispatch and a filesystem mirror. It remains a **complete artifact, partial loop** account, not an exhaustive characterization of all integrations or deployments.

All direct evidence below is SRC-1 at the reviewed commit. Direct reads add implementation evidence from the engine's retain, memories-store, consolidation, recall-budget, reflect-tool, mental-model and directive methods; CLI registration and mirror synchronization; MCP registration and invalidation wrappers; and the system-evaluation judge, page test and report writer. Comments and prompt wording are doctrine/design, even when attached to executable methods. No target code, tests, examples, providers or services were executed. Supplied runtime findings are distinguished from these direct reads. Source access was available; uninspected paths are not access failures.

| Entry point or memory operation | Source paths and inspection basis | Coverage and prevented conclusion |
|---|---|---|
| Synchronous/queued retention; Claude Code trace admission | Supplied runtime: `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-integrations/claude-code/scripts/retain.py`, `hindsight-integrations/claude-code/scripts/recall.py`, `hindsight-integrations/claude-code/hooks/hooks.json` | [RT-RTE-retain-work](runtime.md#rt-rte-retain-work), [RT-RTE-claude-hooks](runtime.md#rt-rte-claude-hooks); annotations below. Concrete trace-to-facts-to-later-context chain; actual host consumption unobserved. |
| Extraction, ingress screening, replacement and alternative store ownership | Direct: `hindsight-api-slim/hindsight_api/engine/retain/fact_extraction.py`, `hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py`, `hindsight-api-slim/hindsight_api/engine/retain/fact_storage.py`, `hindsight-api-slim/hindsight_api/engine/memories/__init__.py` | [MEM-CLM-retain-admission](#mem-clm-retain-admission), content objects below. Verbatim/chunks modes, multimodal routing, append/delta and store sessions are located but not fully traced; no uniform extraction or atomicity claim. |
| Consolidation and deduplication | Direct: `hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py`, `hindsight-api-slim/hindsight_api/engine/memories/pg/consolidation.py` | [MEM-RTE-observation-consolidation](#mem-rte-observation-consolidation). Batch preparation/write and update history inspected; complete outer-job retries, scope-strategy traversal and dedup verdict handling uninspected. |
| Recall and provenance selection | Direct: `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/engine/fact_budget.py`, `hindsight-api-slim/hindsight_api/engine/source_facts.py` | [MEM-RTE-recall-selection](#mem-rte-recall-selection). Output selection/enrichment inspected; all retrieval arms, boost rules and reranker failover internals uninspected. |
| Reflect search, page reload and tool-result pruning | Direct: `hindsight-api-slim/hindsight_api/engine/reflect/tools.py`; supplied loop/context account | [MEM-RTE-page-delivery](#mem-rte-page-delivery), [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request), [RT-RTE-context-synthesis](runtime.md#rt-rte-context-synthesis). No claim that snippets entail whole-page contents or budget is a hard ceiling. |
| Mental models, knowledge pages, full/delta refresh and retraction | Direct bounded methods: `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, refresh outcome declarations in `hindsight-api-slim/hindsight_api/engine/mental_model_refresh.py` | [MEM-RTE-page-maintenance](#mem-rte-page-maintenance). Backing model/tree distinction, candidate refusals and grounding checks inspected. Full structured edit executor, cron scheduling, manual page deletion and UI controls uninspected; no complete page lifecycle guarantee. |
| Raw-memory edit/invalidate/restore; stale-observation cleanup | Direct: `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/engine/memories/pg/writes.py`, `hindsight-api-slim/hindsight_api/mcp_tools.py` | [MEM-RTE-memory-curation](#mem-rte-memory-curation). Authorization, archive move/restore, dependency sweep and post-commit refresh nudge inspected. Whole graph-maintenance and non-default store semantics uninspected. |
| Directive/configuration/mission admission and use | Direct directive create/update and prompt builders: `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/engine/reflect/prompts.py`; supplied configuration route | [MEM-RTE-directive-admission](#mem-rte-directive-admission), [RT-RTE-config-update](runtime.md#rt-rte-config-update). Mission/config overlay located, not separately traced through every writer; no universal instruction-compliance guarantee. |
| Shipped agent instructions | Supplied boundary's bounded `skills/hindsight-self-hosted/SKILL.md` read; direct reflection prompt/tool reads above | Static setup/retain/recall/reflect guidance is doctrine, not accumulated memory. Other skills/plugin instruction wiring remains uninspected; no complete agent-facing instruction inventory. |
| CLI and MCP alternate entry points | Direct: `hindsight-cli/src/main.rs`, searches of `hindsight-cli/src/commands/memory.rs`, `hindsight-api-slim/hindsight_api/api/mcp.py`, bounded invalidation wrapper in `hindsight-api-slim/hindsight_api/mcp_tools.py` | Dispatch reaches retain/recall/reflect and additional curation/page operations. Registry has environment allowlisting and extension registration. Most handlers/transport serializers uninspected; no parity or universally exposed-tool claim. |
| CLI filesystem read-back | Direct: `hindsight-cli/src/commands/fs/sync.rs` and CLI dispatch | [MEM-RTE-filesystem-mirror](#mem-rte-filesystem-mirror). Server-to-disk delivery wired; specific later agent file reads uninspected. |
| System evaluation and retained results | Direct: `hindsight-system-evals/evals/test_01_knowledge_page_convergence.py`, `hindsight-system-evals/hindsight_system_evals/judge.py`, `hindsight-system-evals/hindsight_system_evals/report.py`, `hindsight-system-evals/evals/conftest.py` | [MEM-RTE-page-evaluation](#mem-rte-page-evaluation). Source-defined criteria, model judge, failure record and JSON persistence; no supplied benchmark run or complete evaluator inventory. |
| Additional SDKs/integrations, embedded launchers, transfer/import, attachments, control-plane mutations and deployment modes | Available paths identified by boundary and engine search: `hindsight-integrations`, `hindsight-clients`, `hindsight-embed`, `hindsight-all`, `hindsight-control-plane`, `hindsight-api-slim/hindsight_api/engine/transfer`, `hindsight-api-slim/hindsight_api/engine/storage` | Included responsibilities remain uninspected beyond supplied or named reads. Missing caller-specific admission, retention horizon, transport and consumer facts prevent system-wide claims. Attachment blobs may have non-database storage; no text-only universality. |

External host orchestration, hosted Cloud internals and provider internals remain outside the boundary. Model parameters are opaque deployed state; repository fixity does not freeze them. The record inventory distinguishes readable content, symbolic access/lineage fields, dense retrieval outputs and working context rather than calling all of them one memory store.

## Core ideas

1. **Retain is normally a content transformation, not raw transcript replay.** Model-produced fact text and retrieval representations are distinct from optional stored document/chunk text. The extracted `why` can survive in fact prose; that is not assurance that the original reasoning episode survives. Ingress validators and conditional defense screening differ from extraction authorship. [MEM-OBJ-fact-text](#mem-obj-fact-text), [MEM-CLM-retain-admission](#mem-clm-retain-admission).
2. **Derived content has two later-use levels.** Consolidation revises observation text with source IDs. Living knowledge pages persist longer synthesized documents over a scoped query. Neither the label “ground truth” for raw facts nor “highest quality” for mental models establishes correctness: facts are extracted and pages can refresh automatically. [MEM-RTE-observation-consolidation](#mem-rte-observation-consolidation), [MEM-RTE-page-maintenance](#mem-rte-page-maintenance), [MEM-CLM-source-hierarchy](#mem-clm-source-hierarchy).
3. **Delivery is selective at several boundaries.** Recall ranks and budgets fact text separately from chunks and source facts. Reflect strips retrieval plumbing, bounds context fields, returns page snippets with on-demand whole-page reading, and separately controls its current working history. Consequently neither stored lineage nor an API response necessarily reaches a model whole. [MEM-RTE-recall-selection](#mem-rte-recall-selection), [MEM-RTE-page-delivery](#mem-rte-page-delivery), [RT-RTE-context-synthesis](runtime.md#rt-rte-context-synthesis).
4. **Withdrawal is a dependency operation, not merely deleting a fact.** Raw curation invalidates derived observations; retained page grounding can detect missing source IDs and solicit retraction edits. Automatic refresh nudges are best effort and omit manually refreshed pages. Old prose can therefore outlive the source until maintenance occurs. [MEM-RTE-memory-curation](#mem-rte-memory-curation), [MEM-RTE-page-maintenance](#mem-rte-page-maintenance).
5. **Instruction authority is separate from evidential authority.** Directives become imperative prompt text, while ordinary retrieved memory supplies evidence. Metadata can convey source provenance to reflection, but code does not turn that stamp into truth. The model interprets both; successful compliance or improved capacity was not observed. [MEM-BAP-reflect-content](#mem-bap-reflect-content), [MEM-BAP-directive-prompt](#mem-bap-directive-prompt).

## Shared records

### Components

#### MEM-CMP-consolidation-llm
Label: Configured consolidation model

Source-native identity: `_consolidation_llm_config`, including the `consolidation_dedup` operation configuration. Form: distributed-parametric model state in a provider or local server; symbolic configuration handles remain in the engine. Distinct operation from [RT-CMP-retain-llm](runtime.md#rt-cmp-retain-llm) and [RT-CMP-reflect-llm](runtime.md#rt-cmp-reflect-llm), although deployments may choose the same underlying model. SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py`.

> consolidation_model = consolidation_llm_model or config.consolidation_llm_model or memory_llm_model
> consolidation_base_url = consolidation_llm_base_url or config.consolidation_llm_base_url or memory_llm_base_url
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

Parameters changing during operation: visible calls are inference, provider-internal change uninspected. Exact version pinned: not established by configurable names. Mutable endpoint resolving to another model: possible with configured remote/base-URL providers; deployed resolution uninspected. Proposals affect observations only through the route's checks and writes, not by model-owned database authority.

#### MEM-CMP-refresh-llm
Label: Configured mental-model refresh model

Identity: `_mental_model_refresh_llm_override` or the dynamically resolved reflection configuration. Form/substrate: distributed-parametric provider/local-server weights; the Python handle is symbolic. Possible duplicate of [RT-CMP-reflect-llm](runtime.md#rt-cmp-reflect-llm) in the no-override deployment, but a distinct selectable operation role when overridden. SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`.

> refresh_provider = config.mental_model_refresh_llm_provider or reflect_provider
> refresh_api_key = config.mental_model_refresh_llm_api_key or reflect_api_key
> refresh_model = config.mental_model_refresh_llm_model or reflect_model
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

Parameters changing during operation: visible refresh inference is not training; provider internals uninspected. Exact version pinned: not established. Mutable endpoint resolving to another model: configurable provider/base URL permits it; actual deployed identity uninspected. The source does not warrant collapsing every refresh/compression/structured-output call into one immutable model identity.

#### MEM-CMP-cross-encoder
Label: Configured recall reranker

Identity: engine `_cross_encoder_reranker` wrapping a cross-encoder; directly inspected local alternative `LocalSTCrossEncoder`. Form/substrate: distributed-parametric local model state or remote provider state, distinct from generated scalar rank scores. This is not [RT-CMP-embeddings](runtime.md#rt-cmp-embeddings): it scores query/candidate pairs rather than storing fact embeddings. SRC-1, `hindsight-api-slim/hindsight_api/engine/cross_encoder.py`, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`.

> self.model_name = model_name or DEFAULT_RERANKER_LOCAL_MODEL
> self.force_cpu = force_cpu
> self.trust_remote_code = trust_remote_code
> --- `hindsight-api-slim/hindsight_api/engine/cross_encoder.py`

Parameters changing during operation: no training established by this scoring route; provider internals uninspected. Exact version pinned: no immutable model-artifact identity established. Mutable endpoint resolving to another model: remote variants are configurable and uninspected; the directly read local constructor does not itself require such an endpoint. RRF/interleave modes bypass cross-encoder ranking, so this component is not universal to recall.

#### MEM-CMP-evaluation-judge
Label: System-evaluation judge model

Identity: `judge_model()` and Google GenAI client. Form/substrate: distributed-parametric remote model; model name and JSON verdict are not weights. Distinct role from [RT-CMP-reflect-llm](runtime.md#rt-cmp-reflect-llm); configuration separation does not prove different serving weights. SRC-1, `hindsight-system-evals/hindsight_system_evals/judge.py`.

> return os.getenv("HINDSIGHT_EVAL_JUDGE_MODEL", "gemini-2.5-flash").removeprefix("google/")
> --- `hindsight-system-evals/hindsight_system_evals/judge.py`

Parameters changing during operation: provider internals uninspected; inspected calls are grading inference. Exact version pinned: not established by this name. Mutable endpoint resolving to another model: provider-side resolution uninspected and the selected model is environment-configurable. It evaluates against source-defined criteria, not independent execution truth.

### Operative objects

#### MEM-OBJ-document-text
Label: Stored original document and chunk text

Source-native parts: `documents.original_text` and chunk text. Natural-language content on database/default-store or configured store substrate; attachments are a separately unresolved non-text alternative. Lineage is submitted text after screening and configured retention. These are source material for expansion/reprocessing, not the derived fact assertions in [MEM-OBJ-fact-text](#mem-obj-fact-text). Distinct from [RT-OBJ-context-history](runtime.md#rt-obj-context-history): potentially cross-invocation source storage, not a reflection message list. SRC-1, `hindsight-api-slim/hindsight_api/engine/retain/fact_storage.py`, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`.

> if not config_dict.get("store_document_text", DEFAULT_STORE_DOCUMENT_TEXT):
>     effective_recall_include_chunks = False
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

Document storage without facts does not imply recall eligibility; raw source recovery is conditional on text storage and the later read route. Replacement invalidates outgoing facts and observations; complete append/chunk-delta preservation is not established here.

#### MEM-OBJ-fact-text
Label: Extracted raw-memory text

Identity: `Fact` text stored as `world`/`experience` memory text. Natural language in the default `memory_units` store or configured memory store. Extraction normally combines what/when/who/why; verbatim is an alternative mode. “Raw” means pre-consolidation, not untransformed transcript. Derived from submitted user/agent/document content; original speaker and factual truth are not authenticated by the fact-type label. Not the [RT-OBJ-context-history](runtime.md#rt-obj-context-history) object; [RT-RTE-retain-work](runtime.md#rt-rte-retain-work) produces this distinct durable result. SRC-1, `hindsight-api-slim/hindsight_api/engine/retain/fact_extraction.py`, `hindsight-api-slim/hindsight_api/engine/retain/fact_storage.py`.

> if who:
>     combined_parts.append(f"Involving: {who}")
>
> if why:
>     combined_parts.append(why)
>
> combined_text = " | ".join(combined_parts)
> --- `hindsight-api-slim/hindsight_api/engine/retain/fact_extraction.py:2272-2278`

Later recall/reflect/consolidation reads this text. Extraction reasons can survive as prose, but this neither preserves every source reason nor establishes criticism of a theory. Editing and invalidation follow [MEM-RTE-memory-curation](#mem-rte-memory-curation).

#### MEM-OBJ-fact-embedding
Label: Stored fact retrieval embedding

Identity: processed fact `embedding`; form: dense distributed-parametric representation, an inference output rather than model parameters. Substrate: default database vector or configured store's index. Lineage: embedding computation over processed fact input; precise augmentation and all alternatives remain uninspected. Later numerical search consumes it as relevance representation, not readable evidence. Distinct output from [RT-CMP-embeddings](runtime.md#rt-cmp-embeddings); no supplied object counterpart. SRC-1, `hindsight-api-slim/hindsight_api/engine/retain/types.py`, `hindsight-api-slim/hindsight_api/engine/retain/fact_storage.py`.

> def pack_embedding(values: Sequence[float]) -> PackedEmbedding:
>     """Pack an embedding vector for carrying through the retain pipeline."""
>     return array("f", values)
> --- `hindsight-api-slim/hindsight_api/engine/retain/types.py`

Curation restoration recomputes the embedding; opaque archived or external-store state is not assumed to preserve the same vector. See [MEM-OBJ-curation-archive](#mem-obj-curation-archive).

#### MEM-OBJ-memory-lineage
Label: Memory identity, access and provenance fields

Source-native identities include `source_memory_ids`, document/chunk IDs, tags, dates, `consolidated_at`, entity postings and links. Symbolic IDs/scopes/bookkeeping use fixed search/storage rules. Database/default-store or configured store substrate. Model-readable metadata is assessed separately in [MEM-OBJ-source-metadata](#mem-obj-source-metadata). This is a distinct retained part from [RT-OBJ-bank-config](runtime.md#rt-obj-bank-config): provenance/access over content, not operation overrides. SRC-1, `hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py`, `hindsight-api-slim/hindsight_api/engine/reflect/tools.py`.

> _UNREAD_RESULT_FIELDS = ("scores", "chunk_id", "document_id")
> --- `hindsight-api-slim/hindsight_api/engine/reflect/tools.py`

Retrieval consumers use access/identity fields; reflect tool presentation removes these three fields while preserving nonempty metadata and source fact IDs. Lineage can therefore remain in storage without every pointer reaching the model. `proof_count` counts contributing source IDs in the inspected dedup SQL; it is not independent verification of truth (SRC-1, `hindsight-api-slim/hindsight_api/engine/memories/pg/consolidation.py`).

#### MEM-OBJ-source-metadata
Label: Model-readable source metadata

Identity: memory `metadata`, including caller-supplied source stamps. Symbolic key/value serialization in the memory store, with natural-language authority when a model interprets a value such as guide versus conversation. This differs from access tags and numerical retrieval scores: the inspected tool formatter preserves nonempty metadata while removing storage plumbing. Original authorship and trust of a source stamp are unresolved; retaining it does not authenticate the source. Distinct from [RT-OBJ-bank-config](runtime.md#rt-obj-bank-config), whose mapping changes operation configuration. SRC-1, `hindsight-api-slim/hindsight_api/engine/reflect/tools.py`; the field-removal witness and selection account are in [MEM-OBJ-memory-lineage](#mem-obj-memory-lineage) and [MEM-RTE-page-delivery](#mem-rte-page-delivery).

#### MEM-OBJ-observation-text
Label: Consolidated observation text

Identity: observation-type memory text; natural language in the default memory store or configured store. Lineage: consolidation proposal over new fact text and recalled observation/source text, then checked create/update/delete. Source IDs and embeddings are distinct operative parts above. Closest supplied record is [RT-RTE-retain-work](runtime.md#rt-rte-retain-work), which schedules but does not describe this result; no supplied object counterpart. SRC-1, `hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py`; verbatim write witness in [MEM-RTE-observation-consolidation](#mem-rte-observation-consolidation).

Later recall, reflection and page refresh can consume the current observation. Optional history stores pre-update snapshots and new source IDs, not a guaranteed critique/rationale for the new text. The inspected update does not require human approval of each observation.

#### MEM-OBJ-mental-model
Label: Persistent mental-model document

Identity: `mental_models.content`, the page backing document. Natural-language prose in SQL even when a configured store owns its search index. Refresh specification, tree node and dense search representation are separately declared below. Authored creation and later automatic synthesis are separate lineage routes. Distinct from [RT-OBJ-context-history](runtime.md#rt-obj-context-history); this document survives requests. SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`; create/maintenance witnesses below.

Later reflect reads the document, not all its audit fields. Other manual update/clear/delete branches remain only partially inspected.

#### MEM-OBJ-refresh-specification
Label: Retained refresh query and controls

Identity: `source_query`, `trigger`, `max_tokens` and refresh watermarks attached to a mental model. Natural-language source query requests synthesis; symbolic scope, mode, scheduling and watermark fields determine what input window the code offers. SQL substrate. Lineage begins with caller settings and merged defaults, then maintenance updates watermarks/outcomes. Unlike the content document, these parts primarily govern the next maintenance invocation. Distinct from bank-wide [RT-OBJ-bank-config](runtime.md#rt-obj-bank-config); some defaults originate there, but the per-document specification has its own scope and update history. SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/engine/mental_model_refresh.py`; witnesses in [MEM-RTE-page-maintenance](#mem-rte-page-maintenance). No claim that a query is a formulated explanatory theory.

#### MEM-OBJ-page-embedding
Label: Mental-model search embedding

Identity: mental-model embedding generated from name/content; dense distributed-parametric inference output. Stored as SQL vector on the database search path or passed to the configured knowledge-page index. Different consumer/invalidation from the document prose: semantic search consumes the representation, then SQL hydrates selected page content. Distinct from [RT-CMP-embeddings](runtime.md#rt-cmp-embeddings), the producing model implementation, and from fact embeddings. SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/engine/reflect/tools.py`.

> embedding_vec = await self._mental_model_embedding_vector(name, content)
> embedding = str(embedding_vec) if embedding_vec else None
>
> if not mental_model_id:
>     mental_model_id = f"mm-{uuid.uuid4().hex}"
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

The page row can persist without SQL carrying the search vector when an alternate store owns indexing. Indexing after commit prevents publishing an uncommitted creation on the inspected path, but does not guarantee cross-store atomicity or repair success.

#### MEM-OBJ-knowledge-pages
Label: Knowledge tree nodes

Identity: `knowledge_pages` rows with folder/page kind, parent/name and `mental_model_id` reference. Symbolic hierarchy on SQL substrate. Lineage is caller creation/move/rename rather than independent synthesis of the referenced content. Consumers are tree APIs, administrative clients and mirror planning; semantic content delivery uses the backing model. This is not the working context in [RT-OBJ-context-history](runtime.md#rt-obj-context-history), and no supplied object counterpart exists. SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`; backing-model/node creation shares the inspected transaction in [MEM-RTE-page-maintenance](#mem-rte-page-maintenance). Full subtree deletion and every relocation branch remain uninspected.

#### MEM-OBJ-structured-content
Label: Structured mental-model edit baseline

Identity: `mental_models.structured_content`. Symbolic block structure with natural-language bodies, SQL JSON substrate. Its fixed edit operations identify parts of a document; the rendered Markdown is the separately consumed prose. Lineage: canonicalization at creation, model-produced document structure or split fallback at refresh, then delta operations. It is distinct from the document's search embedding and not [RT-OBJ-bank-config](runtime.md#rt-obj-bank-config). SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`.

> document = canonical_document(content)
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py:17027-17027`

The quoted creation method stores both render and structure. Refresh uses the baseline for localized operations; a later reader of content need not receive those edit addresses. Complete block-level rejection/rollback semantics remain uninspected; the page-maintenance route retains the inspected refusal guards.

#### MEM-OBJ-refresh-response
Label: Mental-model grounding, outcome and history

Identity: `reflect_response`, `mental_model_history` and operation outcome metadata. Symbolic IDs/outcomes plus natural-language supporting text, warnings, errors and optional traces, stored in SQL. Derived from refresh and preserved across invocations to different degrees: the current response can be overwritten; history and operation rows retain earlier outcomes subject to their retention policies. Distinct from [RT-OBJ-context-history](runtime.md#rt-obj-context-history): an audit/maintenance product, not the current message list. SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/engine/mental_model_refresh.py`.

> if (mental_model.get("trigger") or {}).get("keep_trace"):
>     reflect_response_payload["trace"] = run.to_trace().model_dump(mode="json")
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

The next delta refresh reads accumulated `based_on` to detect retracted source IDs. Only this run's supporting facts enter its delta proposal context; all historical evidence is not resent. Reasons are available to audit callers through outcomes/history, but no inspected ordinary reflect page-read sends full history or trace to the answering model.

#### MEM-OBJ-directive-content
Label: Retained directive text

Identity: `directives.content`; natural-language instructions in SQL, separately selected by symbolic active flag, priority and tags. Caller authorship may be human or software; inspected persistence does not resolve it. This content is not the configuration JSON in [RT-OBJ-bank-config](runtime.md#rt-obj-bank-config). SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/engine/reflect/prompts.py`; write/prompt passages below. Later authority is imperative model input, not code enforcement of the prose.

#### MEM-OBJ-curation-archive
Label: Invalidated raw-memory archive

Identity: `invalidated_memory_units`, including `invalidation_reason`, entity snapshots and causal-link descriptors. Natural-language text/reason and symbolic lineage descriptors in SQL; embedding/search-vector fields omitted. Derived by moving a live raw fact, not synthesizing a new claim. Distinct from [RT-OBJ-context-history](runtime.md#rt-obj-context-history) and from active recall content. SRC-1, `hindsight-api-slim/hindsight_api/engine/memories/pg/writes.py`.

> _ARCHIVE_OMITTED = ('"embedding"', '"search_vector"')
> --- `hindsight-api-slim/hindsight_api/engine/memories/pg/writes.py`

A restoration consumer reads archived state and recomputes retrieval representations; ordinary recall consumes live memory, not archive rows. Retained reasons support explanation of rejection to a caller, but a later reflection model is not shown those reasons by this archive mechanism. Permanent deletion and archive movement are not interchangeable.

### Routes

#### MEM-RTE-observation-consolidation
Label: Fact-fed observation consolidation

Endpoints: unconsolidated facts → scoped related-observation recall → unioned evidence/model proposal → prepared actions → batch store writes → later observations. Code owns scope, liveness/security checks, action ordering and persistence; [MEM-CMP-consolidation-llm](#mem-cmp-consolidation-llm) proposes prose and actions. This extends, rather than duplicates, [RT-RTE-retain-work](runtime.md#rt-rte-retain-work)'s scheduling account. SRC-1, `hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py`, `hindsight-api-slim/hindsight_api/engine/memories/pg/consolidation.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Per-memory action statistics, deletion count and batch failure indicator; not independent truth verification.
- Later read-back: Persisted observation text/source IDs reach subsequent recall, reflect and refresh; later consolidation can revise existing observations.
- Delegated visibility: Model sees batched facts and unioned recalled observations with selected source facts; action preparation checks sources and per-fact observation eligibility.
- Selection predicate: Pending facts grouped by scope; per-fact query recalls candidate observations; configured capacity and optional semantic dedup affect admission.
- Invalidation or expiry: Create/update/delete actions, stale-source sweep and optional bounded pre-update history. No universal observation TTL established.
- Activation or effect: Code writes checked proposals and consolidation markers; successful semantic integration and downstream reliance unobserved.
- Evidence limits: Full outer retry/failure marking and all configured store transactions uninspected; source-local batch guarantees are not whole-system exactly-once guarantees.

Open maintenance triggered by admitted facts or an explicit job. Software/model admission, not per-content human approval: model proposes, code can reject out-of-recall deletes, resolve/check sources and abort the batch. Failed related-observation recall raises rather than silently presenting no candidates. Guidance is consolidation configuration/prompt over source facts; stored result is revised prose, lineage and markers. No expected-answer oracle identified in this batch. Optional dedup model judgment is not such an oracle.

> prepared_deletes: list[str] = []
> for delete in llm_result.deletes:
>     # Security: the observation must be present in the unioned recall
>     if not any(str(obs.id) == delete.observation_id for obs in union_observations):
>         logger.debug(
>             f"Batch consolidation: rejected delete — observation {delete.observation_id} not in unioned recall"
>         )
>         continue
>     prepared_deletes.append(delete.observation_id)
> --- `hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py`

> await write_batch.commit()
> except BaseException:
>     await write_batch.abort()
>     raise
> --- `hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py`

The inspected SQL update rewrites text/retrieval representation and unions source IDs; optional observation history keeps a prior snapshot. Derivation/revision is established, but the record does not classify it as content-directed theory criticism or improved future capacity.

#### MEM-RTE-recall-selection
Label: Bounded recall selection

Endpoints: caller query/bank/filters → retrieval and chosen fusion/ranking → optional observation preference → top candidate window → chunk/fact/source enrichment → caller response. Code owns selection/delivery. This is a distinct engine recall route, also used inside [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request), not a second HTTP reflection record. SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/engine/fact_budget.py`, `hindsight-api-slim/hindsight_api/engine/source_facts.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Recall result with selected fact text and optional chunks, entities, source facts and diagnostics.
- Later read-back: Request-driven retrieval of retained facts/observations; concrete subsequent consumers include reflection callbacks and [RT-RTE-claude-hooks](runtime.md#rt-rte-claude-hooks). A bare API caller's eventual behavior remains unspecified.
- Delegated visibility: Caller receives a selected display projection, not every retained source or index; chunks and provenance have distinct budget/filter controls.
- Selection predicate: Query, bank, tag/group/date/type controls; fusion/reranking, optional preference for observations, candidate window and rank-ordered token selection.
- Invalidation or expiry: Live-store deletion/curation changes future candidates; in-flight response is not retroactively withdrawn.
- Activation or effect: Retained material is delivered to known downstream code routes; model reliance and external action changes unobserved.
- Evidence limits: All arm implementations, deployment grants and non-default full-recall stores uninspected; no universal relevance or response-size guarantee.

Fact selection skips individually oversized candidates rather than terminating at the first one. If positive budget admits none, it returns the first resolvable fact whole, over budget:

> if not selected and skipped and max_tokens > 0:
>     # Every candidate is individually over budget. Answering with nothing would be
>     # indistinguishable from "no such memory", so spend the floor on the top-ranked
>     # fact — the returned `total_tokens` shows the overshoot.
>     for fact_id in fact_ids_ordered:
>         text = text_by_id.get(fact_id)
>         if text is not None:
>             selected.append(fact_id)
>             total_tokens = count_tokens(text)
>             break
> --- `hindsight-api-slim/hindsight_api/engine/fact_budget.py`

Chunks are fetched from pre-fact-budget candidates, with separate budget and document visibility checks. Source facts are budgeted after fact selection, in observation rank order; per-observation caps replace the shared source budget. Source IDs can remain advertised when text is missing or omitted. This prevents treating provenance pointers as a complete readable justification received by the caller.

#### MEM-RTE-page-delivery
Label: Reflection page search and read

Endpoints: model/code-selected query → semantic page search → scoped freshness and top-hit/full-or-snippet display → model-requested IDs → page read → next reflection model call. Code owns search/read serialization; model chooses requested pages under the enclosing route. This is a distinct retained-content subroute of [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request). SRC-1, `hindsight-api-slim/hindsight_api/engine/reflect/tools.py`, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Search hits with current/stale indication and content or snippet; explicit reads return content and omitted-ID retry list.
- Later read-back: Authored or previously refreshed mental-model content reaches a later reflection invocation through its tool results.
- Delegated visibility: Search normally exposes one fitting best hit whole and other hits as short snippets; read exposes content, not full historical rationale/grounding.
- Selection predicate: Embedded query/top-k, tags/groups/exclusions and requested IDs; top-hit token ceiling, 280-character snippets and read token accounting.
- Invalidation or expiry: New/removed sources affect staleness; missing/out-of-scope pages read as omitted. Already delivered prose can remain in current context.
- Activation or effect: Next model invocation receives selected stored prose; that delivery is not proof of reliance or factual correctness.
- Evidence limits: Detailed staleness scope computation and every page search backend uninspected; freshness and relevance do not validate content.

> top_hit = not mental_models and count_prompt_tokens(content) <= top_result_max_tokens
> --- `hindsight-api-slim/hindsight_api/engine/reflect/tools.py`

The explicit read has a first-page floor: its `pages` condition means the first available page can exceed budget. It skips a later non-fitting page and reports it, rather than enforcing the docstring's stronger description of a hard bound/stop:

> if pages and spent + cost > max_tokens:
>     # The id, not the name: ``not_read`` is a retry list, and the model can
>     # only ask again with an id.
>     omitted.append(str(row["id"]))
>     continue
> --- `hindsight-api-slim/hindsight_api/engine/reflect/tools.py`

No cross-invocation compaction product is established by [RT-RTE-context-synthesis](runtime.md#rt-rte-context-synthesis). That separate working-context control blanks older tool bodies while keeping current-run backing history; these durable pages are brought in from an independent store, not dereferenced pointers into an evicted message frame.

#### MEM-RTE-page-maintenance
Label: Persistent knowledge-page maintenance

Endpoints: caller content/query/options → model plus optional knowledge tree node → scoped snapshot/reflect → full document or delta candidate/edit operations → refusals or persisted document/grounding → later refresh and page delivery. Code owns authorization, scope and candidate guards; [MEM-CMP-refresh-llm](#mem-cmp-refresh-llm) and associated model calls propose content/edits. Distinct from ordinary answer-only [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request): this wrapper persists the result. SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/engine/mental_model_refresh.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Created/refreshed page/model or explicit failure/no-change result; dry-run preview does not persist the document.
- Later read-back: Stored document reaches future reflection; next refresh reads baseline/query/trigger and accumulated grounding. Ordinary read tools omit full audit history.
- Delegated visibility: Refresh has scoped facts and optional sibling models; current delta evidence feeds structured edits, while historical grounding remains separately retained.
- Selection predicate: Stored query, tags/groups/type exclusions, configured full/delta mode and time window; retracted IDs are detected against live memories. Default knowledge-page trigger is observation-only, delta and auto-refresh.
- Invalidation or expiry: Full regeneration or applied delta can replace/remove prose. Missing grounding marks maintenance need; failed/deferred retraction keeps old IDs so later rounds can notice. Manually refreshed pages need their owner to request work.
- Activation or effect: Candidate passes code guards and persists as later-readable prose/structure; correct unsaying and improved answers unobserved.
- Evidence limits: Full delta/unsay executors, cron loop and all history bounds uninspected; scheduled refresh and retained grounding are not guarantees of timely withdrawal.

Open administrative creation plus recurring maintenance. Caller identity leaves human authorship/approval unresolved; automatic refresh has no per-edit human approval gate established. Optional validators and write/tag scope can veto creation; code refuses an empty candidate and failed delta-window replacement, preserving content and the watermark. Structured output may add another refusal at persistence. Local transaction and failure records provide recovery, not an independently scored improvement-selection policy. No answer oracle established for production refresh.

> """Create a page: a backing mental model plus the tree node that refs it.
>
> ``managed`` lets a client tag the page as system-owned vs. hand-authored.
> When ``trigger`` is omitted the page uses ``KNOWLEDGE_PAGE_DEFAULT_TRIGGER``
> (observation-only, delta, auto-refresh) so a knowledge page is a living
> document by default, with the hierarchical ``knowledge_page_default_trigger``
> config merged over it.
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

> if use_delta and not delta_applied and created_after is not None:
>     return _finish(
>         effective_mode=effective_mode,
>         mode_fallback_reason=mode_fallback_reason,
>         final_content=final_content,
>         final_structured=None,
>         delta_operations=delta_operations,
>         outcome="refresh_failed_delta_not_applied",
>     )
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

Retraction starts from stored `based_on`, not a global truth oracle. It checks source existence and defers when consolidation is pending, to avoid unsaying a replacement still being processed. A full refresh rebuilds grounding; delta merges historical grounding and prunes retracted IDs only when the retraction pass is handled. Failures retain outcomes/history and optionally traces. These are reasons and input/output records, not a demonstrated theory-criticism loop.

#### MEM-RTE-memory-curation
Label: Raw-memory editing and withdrawal

Endpoints: authorized caller edit/state/reason → current live/archive read → prepared representation/entity changes → transactional edit/archive/restore with dependency cleanup → maintenance scheduling → later recall/refresh. Code owns validation and mutation; caller proposes content/state. The MCP invalidation wrapper exposes retire/restore with optional reason. Distinct from [RT-RTE-config-update](runtime.md#rt-rte-config-update): content and dependency changes rather than operational overrides. SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/engine/memories/pg/writes.py`, `hindsight-api-slim/hindsight_api/mcp_tools.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Updated raw memory or missing result/error; explicit delete removes rather than archives it.
- Later read-back: Recall sees corrected/restored live text, not invalidated archive rows; consolidation rereads surviving/reset sources; refresh can detect retracted grounding.
- Delegated visibility: Caller supplies explicit fields and optional reason; store sees live/archive state. No inspected later answering-model route supplies the archive's rejection reason.
- Selection predicate: Bank/memory identity, write scope and requested edit/state; raw world/experience facts only, not direct observation edits.
- Invalidation or expiry: Archive movement removes live retrieval content and preserves restore state; stale observations/history are deleted and surviving source consolidation markers reset.
- Activation or effect: Live-store membership and content change subsequent selection; automatic page-refresh nudge is best effort and host reliance is unobserved.
- Evidence limits: Full curation phase-two implementation, alternate memory-store archive contracts and complete graph rebuild uninspected; restoring a fact is not restoring every prior derived observation/page byte.

Software admission checks UUID/state/text/type and configured validators plus write scope; human decision per item is unresolved because a client/model may call the same surface. Explicit reasons are retained in the archive, not inferred model criticism. Revert is a supported recovery path; permanent delete is not equivalent rollback. Embeddings and search representations are recomputed; source-derived causal descriptors are preserved rather than newly validated. No answer oracle identified in curation.

> ctx = BankWriteContext(
>     bank_id=bank_id, operation=BankWriteOperation.UPDATE_MEMORY_UNIT, request_context=request_context
> )
> await self._validate_operation(self._operation_validator.validate_bank_write(ctx))
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

> inserted = await conn.fetchval(
>     f"INSERT INTO {arch} ({arch_cols}, invalidation_reason, invalidated_at, entity_ids, causal_links) "
>     f"SELECT {arch_cols}, $2, now(), $3::uuid[], $5::jsonb FROM {mu} WHERE id = $1 AND bank_id = $4 "
>     f"RETURNING id",
> --- `hindsight-api-slim/hindsight_api/engine/memories/pg/writes.py`

The SQL stale-observation sweep removes observations citing any outgoing source, drops their history and resets surviving co-sources for reconsolidation. After a committed curation write, `_submit_refreshes_for_retracted_grounding` scans only auto-refreshing pages, avoids redundant pending-consolidation work and catches scheduling failures. A successful delete response therefore does not establish that every later page has stopped saying the deleted fact.

#### MEM-RTE-directive-admission
Label: Directive content admission

Endpoints: caller directive create/update → authentication/optional validator and writable scope → SQL text/selection metadata → later active/scoped directive loading → reflection prompt. Caller proposes, code authorizes/persists, model interprets. This differs from [RT-RTE-config-update](runtime.md#rt-rte-config-update)'s symbolic configuration admission and complements [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request)'s directive loading. SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/engine/reflect/prompts.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Created/updated directive row or missing/error result.
- Later read-back: Active selected directive text reaches subsequent reflection prompts/reminders.
- Delegated visibility: Caller authors content; model receives imperative rule prose. Selection metadata influences loading but does not enforce the content's meaning.
- Selection predicate: Active status, priority and tag scope; ordinary scoped loading versus caller-requested all-active loading as supplied by runtime.
- Invalidation or expiry: Update can change text or deactivate it; delete exists but complete handler trace and in-flight withdrawal are uninspected.
- Activation or effect: Persisted instruction enters a behavior-shaping model-input path; compliance and answer benefit unobserved.
- Evidence limits: Deployed writer identity, validator policy, full delete route and exhaustive response-level checking uninspected.

Open administration. Configured bank-write validator and scope can veto; no per-content human approval or semantic correctness oracle established. Guidance is caller-supplied rule text; persisted result is instruction plus selection metadata. Deactivation/replacement provides future-selection control, not an established historical rollback system.

> # An untagged directive steers everyone's reflect, so a restricted writer cannot make one.
> self._refuse_unwritable(tags, await self._write_tag_scope(bank_id, request_context), "a directive")
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

#### MEM-RTE-filesystem-mirror
Label: CLI filesystem knowledge mirror

Endpoints: `Commands::Fs` → synchronization configuration → API knowledge snapshot → planned directories/Markdown → local disk/state. Shipped code owns automatic selection of the configured bank's snapshot and filesystem effects. Distinct from [RT-RTE-claude-hooks](runtime.md#rt-rte-claude-hooks): pull-based mirror, not per-prompt recall injection. SRC-1, `hindsight-cli/src/main.rs`, `hindsight-cli/src/commands/fs/sync.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Synchronization counts/state or API/filesystem failure.
- Later read-back: Persisted API knowledge becomes local Markdown readable by external tools/agents; a specific later reader invocation is uninspected, so this establishes storage/delivery capability, not wired model consumption.
- Delegated visibility: Local files contain rendered snapshot pages and index, not necessarily all memory facts or refresh history.
- Selection predicate: Configured bank/API and knowledge-tree snapshot; drift comparison rewrites locally changed bytes even when the server page did not change.
- Invalidation or expiry: Successful fetch permits pruning removed pages; fetch failure records failure and returns before pruning. Writable mode does not establish server write-back.
- Activation or effect: Filesystem writes and local edit reversion are implemented; actual agent reading/reliance unobserved.
- Evidence limits: Daemon scheduling, full rendering/index format and external file readers uninspected.

> // Source of truth is the bytes on disk — so a local edit is detected
> // and overwritten even when the page is identical to last time.
> let on_disk = read_file_or_none(&abs_path);
> --- `hindsight-cli/src/commands/fs/sync.rs`

This is not a material-adoption editor: server→disk is one-way in the inspected code. Human or agent local edits are not admitted as page updates; the next pass restores API-derived content.

#### MEM-RTE-page-evaluation
Label: Knowledge-page evaluation and reporting

Endpoints: source-defined question/waves → page-building test helper → final document/size history → model criterion and trap verdicts → recorded result → assertions and optional JSON run report. Test code owns selection, judging requests, assertion and retention; [MEM-CMP-evaluation-judge](#mem-cmp-evaluation-judge) proposes verdict/reason. No supplied runtime evaluator counterpart. SRC-1, `hindsight-system-evals/evals/test_01_knowledge_page_convergence.py`, `hindsight-system-evals/hindsight_system_evals/judge.py`, `hindsight-system-evals/hindsight_system_evals/report.py`, `hindsight-system-evals/evals/conftest.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Test pass/fail and page/verdict result; optional suite JSON report is written at session end.
- Later read-back: Report module documents dashboard/publishing-script consumers of JSON. Their implementation is uninspected; no production memory-refresh consumer of these scores is established by the inspected path.
- Delegated visibility: Judge sees answer, criterion and optional context, not an independently verified whole execution trace; report receives outcome, reason, IDs and size history.
- Selection predicate: Source minimum-acceptance questions versus full mode; expected criteria and specific forbidden claims; a failed first judge verdict can be reasked and majority-smoothed.
- Invalidation or expiry: inapplicable — no inspected production-memory rollback follows this test verdict; suite-report lifecycle beyond configured output file is uninspected.
- Activation or effect: Verdicts cause assertions and retained reporting; deployed regression prevention, source edits and model improvement unobserved.
- Evidence limits: No evaluation was executed; helper page-building/settlement internals and dashboard consumers uninspected; other suites remain unresolved coverage.

Bounded test mode, not open ingestion. Expected-answer criteria and trap propositions are source-supplied reference criteria; the model applies them, not a truth oracle independent of those criteria. Software controls pass/fail; human test authorship is not per-production-page approval. Evidence guidance and judgments persist as report reasons, not automatically adopted directives or changed model parameters.

> if record:
>     RECORDED.append(
>         EvalRecord(
>             kind="knowledge_page",
>             question_id=question_id,
> --- `hindsight-system-evals/evals/test_01_knowledge_page_convergence.py`

> Path(output).write_text(report.to_json(), encoding="utf-8")
> --- `hindsight-system-evals/evals/conftest.py`

Results are appended before assertions, so failed tests can still retain a report. That wiring is not a supplied failed/successful run or causal experiment.

### Claims

#### MEM-CLM-retain-admission
Label: Retain admission has multiple controls

Claimed operation: optional operation validator may replace/reject ingress, then enabled defense extension/policy may allow, redact or block items before extraction. Extraction/model authorship and store I/O are not human approval. Closest supplied fact is [RT-RTE-retain-work](runtime.md#rt-rte-retain-work); this adds the distinct pre-extraction defense mechanism, not a duplicate retention route. SRC-1, `hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py`; implementation evidence:

> if memory_defense_extension is not None and _policy.enabled:
>     async with acquire_with_retry(pool) as _defense_conn:
>         for _idx, _content in enumerate(contents):
> --- `hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py`

> # All items blocked → raise so the HTTP layer can return 422.
> if len(_blocked_violations) == len(contents):
>     raise MemoryDefenseAllBlockedError(_blocked_violations)
> --- `hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py`

Partial blocking removes blocked items and realigns returned slots; redaction updates extraction content and source dictionary. Full-body screening has a separate caller contract for oversized submissions; complete coverage of all attachments/parsers and active deployment policy is uninspected. The conditional gate supports neither universal sanitization nor guaranteed semantic protection.

#### MEM-CLM-source-hierarchy
Label: Retrieval hierarchy is a prompt policy

Claimed operation: reflection presents mental models before observations and raw facts, with freshness/verification guidance. SRC-1, `hindsight-api-slim/hindsight_api/engine/reflect/tools.py`; doctrine/design:

> Implements hierarchical retrieval:
> 1. search_mental_models - User-curated stored reflect responses (highest quality)
> 2. search_observations - Consolidated knowledge with freshness
> 3. recall - Raw facts as ground truth
> --- `hindsight-api-slim/hindsight_api/engine/reflect/tools.py`

The operative countercases are model extraction in [MEM-OBJ-fact-text](#mem-obj-fact-text) and automatic living-page maintenance in [MEM-RTE-page-maintenance](#mem-rte-page-maintenance). “User-curated” cannot establish per-refresh human approval; “ground truth” cannot establish truth of model-derived assertions. Stored `is_stale` is maintenance information, not an answer oracle. Closest supplied route [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request) is consistent with this scoped interpretation; this claim does not replace it.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-reflect-content
Label: Retained content in reflection decisions

Consumer: Hindsight's configured reflection model, including page-maintenance calls. Channel: selected tool-result natural-language facts/observations/pages and preserved source metadata. Force: interpretive evidence and retrieval handles, not fixed-rule truth enforcement. Horizon: later requests/refresh rounds until content is withdrawn or replaced. Distinct from [RT-BAP-hook-context](runtime.md#rt-bap-hook-context), whose consumer is external Claude Code. SRC-1, `hindsight-api-slim/hindsight_api/engine/reflect/tools.py`; passages in [MEM-RTE-page-delivery](#mem-rte-page-delivery) and supplied loop [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request). Wiring establishes delivery, not activation or better future capacity.

#### MEM-BAP-directive-prompt
Label: Retained directives in reflection prompt

Consumer: configured reflection model. Channel: directive section and reminder assembled from stored content. Force: natural-language imperative policy; no semantic compliance invariant established. Horizon: subsequent selected calls while active. Distinct from [RT-BAP-config-consumer](runtime.md#rt-bap-config-consumer)'s symbolic setting selection. SRC-1, `hindsight-api-slim/hindsight_api/engine/reflect/prompts.py`:

> parts.append("Your response will be REJECTED if it violates any directive above.")
> parts.append("Do NOT include any commentary about how you handled directives - just follow them.")
> --- `hindsight-api-slim/hindsight_api/engine/reflect/prompts.py`

This is prompt text requesting compliance and asserting rejection, not evidence that a response-level checker implements rejection. The read boundary prevents inferring either a universal checker or its absence elsewhere.

## Annotations

#### On [RT-RTE-retain-work](runtime.md#rt-rte-retain-work)

Memory result: [MEM-OBJ-fact-text](#mem-obj-fact-text), [MEM-OBJ-fact-embedding](#mem-obj-fact-embedding) and lineage, with optional document/chunk text. Default SQL storage is only one alternative. SRC-1, `hindsight-api-slim/hindsight_api/engine/memories/__init__.py`:

> loaded = load_extension("MEMORIES", MemoriesExtension, context=context)
> if loaded is not None:
>     logger.info("[memories] store=%s (memory rows do not go to postgres)", loaded.name)
>     return loaded
> --- `hindsight-api-slim/hindsight_api/engine/memories/__init__.py`

Admission includes the conditional defense mechanism above. Subsequent transformations retain known content and lineage without resolving actual configured-store initialization, external commit or read-after-write semantics. Generic caller identity does not establish human editing/approval.

#### On [RT-RTE-claude-hooks](runtime.md#rt-rte-claude-hooks)

Automatic trace-fed update chain: selected user/assistant transcript and optional tool-call material → submitted document content → extracted facts/retrieval representation → optional observations/pages → later recall selection → hook formatting/score filter → external host `additionalContext`. The first write needs no per-item human approval in the supplied route. A trace label does not certify the original events; facts remain model-derived. Durable behavior-shaping material is the fact/derived store, not just local diagnostic state. The supplied record's stdout passage establishes delivery, not host reliance, improved capacity or exercised self-improvement.

#### On [RT-OBJ-context-history](runtime.md#rt-obj-context-history)

The supplied synthesis route retains raw tool evidence in current-request backing history when older visible tool bodies are blanked. Final map/reduce transforms slices into model prose; no inspected later invocation reloads this request history as durable memory. This is working-window trimming plus current-run recovery, not the same as stored page read-back. Isolation into compression calls keeps other slices out and returns only claim sections; it does not guarantee lossless semantic reconstruction. Source and passages remain those of [RT-RTE-context-synthesis](runtime.md#rt-rte-context-synthesis).

## Write side

Retention ingress is caller-authored or automatically trace-selected. Optional validator, enabled defense policy and extraction configuration have different roles: admission/replacement, screening, and model-derived authoring respectively. Physical persistence is downstream. The trace-fed write can influence later models through facts and derivatives, but no observed capacity improvement follows merely from this path. See [MEM-CLM-retain-admission](#mem-clm-retain-admission) and the retention/hook annotations.

Consolidation reads scoped existing observations and new facts before proposing create/update/delete. Code restricts actions and commits/aborts batch writes; source markers and derived content share the inspected batch scope. Observation history is a pre-update snapshot with contributing sources. It does not necessarily explain why the model selected the replacement. Future consolidation reads current observation/source material; a later answer model is not shown observation history by the inspected reflect tools. See [MEM-RTE-observation-consolidation](#mem-rte-observation-consolidation).

Mental-model creation can persist supplied Markdown without a preceding reflect. Knowledge-page creation adds a tree node and default automatic refresh options. Later refresh derives new content or localized edits and retains grounding/outcomes. Guards preserve old prose/watermarks on failed candidate admission; no-new-facts is separately represented. Stored supporting facts participate in retraction detection, while complete historical rationale is not replayed into every delta model call. See [MEM-RTE-page-maintenance](#mem-rte-page-maintenance), [MEM-OBJ-refresh-response](#mem-obj-refresh-response).

Raw curation admits explicit correction, invalidation, restoration and optional reason. Stale observations are swept and surviving source markers reset. Automatic page-refresh nudges follow committed curation and can fail independently; manual pages have a different maintenance principal. Rejection reasons survive in the archive but have no inspected model read-back path. Directives instead admit caller instruction text for future selected prompts. These are distinct authority surfaces, not one uniform learning gate. See [MEM-RTE-memory-curation](#mem-rte-memory-curation), [MEM-RTE-directive-admission](#mem-rte-directive-admission).

Evaluation retains verdicts/reasons and can fail an assertion, but the inspected route does not automatically revise production memories, methods or parameters. The filesystem mirror is also not a write-back/adoption mechanism. Unknown controls in additional integrations, imports/templates, attachments and alternate stores remain in the coverage table rather than being erased by the known transformations.

## Read-back

Request-directed recall uses query/bank/filters and independently budgets fact text, source text and chunks. Its known consumers are reflection callbacks and the supplied hook route; unspecified SDK/API callers establish capability only. The hook is host-event-triggered automatic delivery: prompt/context-derived query and configuration select memories, score filtering/formatting determines the actual extra context. The target supplies context, while the external host owns whether it loads or uses it. See [MEM-RTE-recall-selection](#mem-rte-recall-selection), [RT-RTE-claude-hooks](runtime.md#rt-rte-claude-hooks).

Reflection uses a combination of code-forced retrieval and model-requested selection. Mental models are not globally preloaded; semantic hits can be snippets and explicit reads reload whole pages. Tool formatting removes scores and storage pointers, keeps nonempty metadata and caps context fields. Fact/source/page budgets are therefore not equivalent to a hard ceiling on complete model context. Within-request compaction and terminal synthesis remain the separate working-context mechanism in runtime. See [MEM-RTE-page-delivery](#mem-rte-page-delivery), [RT-RTE-context-synthesis](runtime.md#rt-rte-context-synthesis).

Scheduled/explicit page maintenance reads retained query, baseline and grounding and delivers new prose to later answer requests. Directives are another later input channel, automatically selected after a reflect request and expressed as mandatory prompt rules, not demonstrated enforcement. File mirroring materializes retained pages to disk, but specific later model reads are unresolved. Evaluation JSON has documented report consumers, not an established feedback connection into live memory. See the respective routes and behavioral-authority records.

## Integration issues

- **No supported contradiction of a supplied runtime fact was found.** The retention description's database emphasis needs the configured memory-store qualification in its annotation; it must not become a universal SQL-substrate claim. Evidence: SRC-1, `hindsight-api-slim/hindsight_api/engine/memories/__init__.py`; [RT-RTE-retain-work](runtime.md#rt-rte-retain-work), [MEM-OBJ-fact-text](#mem-obj-fact-text). Actual selected store and commit/read guarantees remain unknown.
- **Possible component duplicate:** [MEM-CMP-refresh-llm](#mem-cmp-refresh-llm) may equal [RT-CMP-reflect-llm](runtime.md#rt-cmp-reflect-llm) when no override is configured. Source explicitly permits a separate operation configuration. Keep operation-role distinction without asserting distinct weights in every deployment.
- **Subroute overlap, not replacement:** [MEM-RTE-page-delivery](#mem-rte-page-delivery) describes retained-page selection inside [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request); [MEM-RTE-recall-selection](#mem-rte-recall-selection) also supplies hook and maintenance callers. [MEM-RTE-page-maintenance](#mem-rte-page-maintenance) wraps reflection with persistence. No other new record can replace a supplied referent after comparison.
- **Source descriptions overstate epistemic/admission force:** raw facts are extracted, and knowledge pages auto-refresh; [MEM-CLM-source-hierarchy](#mem-clm-source-hierarchy) bounds “ground truth” and “user-curated.” Prompt rejection wording is not a checker witness in [MEM-BAP-directive-prompt](#mem-bap-directive-prompt). Prevented conclusion: verified correctness or universal semantic enforcement.
- **Budget countercases:** [MEM-RTE-recall-selection](#mem-rte-recall-selection) and [MEM-RTE-page-delivery](#mem-rte-page-delivery) retain first-item floors; source-fact/chunk budgets are independent. These qualify any reconciliation inference from runtime's “tool token ceilings” to a hard whole-payload ceiling. Source evidence is the actual selector code, not only docstrings.
- **Withdrawal coverage gap:** [MEM-RTE-memory-curation](#mem-rte-memory-curation) changes live memory, while [MEM-RTE-page-maintenance](#mem-rte-page-maintenance) has best-effort scheduling, manual ownership and pending-work deferral. Full unsay semantics and every delete route were not inspected. Prevented conclusion: immediate universal removal of unsupported prose from all later contexts.
- **Missing shipped-route facts:** alternate integrations/SDKs, embedded persistence/reload, UI mutation, import/template admission, non-default stores, attachment consumption and other evaluators remain as named coverage gaps. [MEM-RTE-filesystem-mirror](#mem-rte-filesystem-mirror) has no inspected later agent reader; [MEM-RTE-page-evaluation](#mem-rte-page-evaluation) has no inspected production-update feedback. Prevented conclusion: whole-system consumer/admission inventory or deployed learning/self-improvement.
- **Method evidence limit:** all operations are source-wired or source-described, not observed runs. No member result here should be promoted to activation, successful withdrawal, benefit or causal improvement solely because validation succeeds.

## Limitations and checks

The source HEAD was rechecked as `610c135b6f2d0d8b972da94146ae635943f36271`, matching the supplied boundary. All new source reads stayed at that source identity; no external evidence or prior characterization was used. Inputs, member contracts and worker rules were read completely in the supplied batches, with bounded source inspection. The report preserves partial inspection rather than widening the boundary to whole-system.

Runtime identity was obtained from the Pi environment, not the requested profile. Validation: the supplied `commonplace-run validate-output` command passed with “Member content check passes; invocation residue not checked.” It checks member form, references and quotation occurrence; the result explicitly does not establish job acceptance or claim support. No target execution or observed performance check was performed.
