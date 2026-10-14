---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Cognee memory: graph knowledge, session guidance, trace promotion, ranking state and proposal-first skill replacement, with partial interface coverage."
run-id: AAS-2026-10-14-cognee-d8839fe03c5b-01
source-identity: https://github.com/topoteretes/cognee
reviewed-boundary: f154b32a9e544dac73e7ddf2010327cf9988edcd
---

# Cognee memory report

## Boundary and evidence

Cognee retains several different things: corpus knowledge, conversation records, execution traces, derived guidance, retrieval weights, summaries and procedural skills. These have different consumers and withdrawal rules. This report traces the memory routes selected in [RT-RTE-permanent-memory](runtime.md#rt-rte-permanent-memory), [RT-RTE-recall-dispatch](runtime.md#rt-rte-recall-dispatch), [RT-RTE-session-improve](runtime.md#rt-rte-session-improve), [RT-RTE-decorated-agent](runtime.md#rt-rte-decorated-agent), [RT-RTE-agentic-tools](runtime.md#rt-rte-agentic-tools) and [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision). It adds maintenance, progressive disclosure, typed writes and withdrawal tracing. It does not expand the boundary's **complete artifact, partial loop** claim into whole-system coverage.

All direct reads below are implementation or doctrine/design evidence from SRC-1 at the frozen commit. The Source register remains in [boundary](boundary.md#source-register). Checkout HEAD was rechecked and equals the supplied revision. No target code, tests, examples, provider or storage service was executed. Successful persistence, activated guidance, learning benefit and causal improvement remain unobserved.

### Coverage inventory

Rows marked supplied rely on runtime findings rather than a fresh full trace. Direct rows describe newly read source; a path inventory or bounded search is not exhaustive behavior inspection.

| Entry point / operation | Source path and evidence basis | Records / remaining facts and prevented conclusion |
| --- | --- | --- |
| Permanent remember / add / cognify; raw documents, graph facts and indexes | Supplied runtime assembly; direct storage entry read: `cognee/tasks/storage/add_data_points.py` | [RT-RTE-permanent-memory](runtime.md#rt-rte-permanent-memory), [MEM-OBJ-graph-content](#mem-obj-graph-content), [MEM-OBJ-graph-structure](#mem-obj-graph-structure), [MEM-OBJ-vector-index](#mem-obj-vector-index). Raw-file loaders, all extractors, indexing bodies and backend transactions not fully traced: no uniform provenance, atomicity or extraction-fidelity claim. |
| Typed QA, trace, feedback and SkillRun writes | Direct `cognee/api/v1/remember/remember.py` typed dispatch; `cognee/modules/tools/skill_runs.py`; `cognee/api/v1/session/session.py` | [MEM-RTE-typed-admission](#mem-rte-typed-admission). Caller-supplied origins may be mixed/opaque; a typed trace is not authenticated execution. |
| Session cache, feedback/context rows and TTL | Direct `cognee/infrastructure/databases/cache/models.py`, `cognee/infrastructure/databases/cache/get_cache_engine.py`; selected FS deletion methods and TTL search | [MEM-OBJ-session-qa](#mem-obj-session-qa), [MEM-OBJ-session-agent-trace](#mem-obj-session-agent-trace), [MEM-OBJ-session-feedback](#mem-obj-session-feedback), [MEM-OBJ-session-context](#mem-obj-session-context). Redis, SQL and Tapes bodies not audited: no backend parity or universal erasure guarantee. |
| Session answer construction, feedback extraction, ranking and history reload | Direct `cognee/infrastructure/session/session_turn.py`, `cognee/infrastructure/session/session_context_builder.py`, `cognee/modules/retrieval/utils/completion.py` | [MEM-RTE-session-guidance](#mem-rte-session-guidance). Session embeddings' selector internals and concurrent-turn alternative not fully traced; no total history-token bound or sequential/concurrent parity claim. |
| Nine improve stages, QA/trace persistence and extraction | Direct `cognee/modules/improve/registry.py`, `cognee/modules/improve/stages.py`, `cognee/tasks/memify/extract_user_sessions.py`, `cognee/tasks/memify/extract_agent_trace_feedbacks.py`, `cognee/tasks/memify/cognify_session.py`, `cognee/tasks/memify/cognify_agent_trace_feedback.py`, `cognee/infrastructure/session/agent_context_extraction.py` | [MEM-RTE-trace-promotion](#mem-rte-trace-promotion). Supplied orchestration [RT-RTE-session-improve](runtime.md#rt-rte-session-improve); pipeline result aggregation and watermark backend atomicity not fully traced. A completed stage need not prove every window persisted. |
| Session distillation and writer rejection | Direct `cognee/modules/session_distillation/distill.py`, `cognee/infrastructure/llm/prompts/session_distillation_writer_system.txt` | [MEM-RTE-session-distillation](#mem-rte-session-distillation), [MEM-OBJ-session-learning](#mem-obj-session-learning). Novelty-search failures return no matches; no independent truth oracle or guaranteed groundedness. |
| Global feedback weights and personal preference weights/text | Direct `cognee/tasks/memify/apply_feedback_weights.py`, `cognee/modules/user_preferences/update.py`, `cognee/modules/graph/cognee_graph/CogneeGraph.py`, `cognee/modules/retrieval/graph_completion_retriever.py`, `cognee/modules/retrieval/hybrid/ranking.py` | [MEM-RTE-ranking-maintenance](#mem-rte-ranking-maintenance), [MEM-OBJ-feedback-weight](#mem-obj-feedback-weight), [MEM-OBJ-preference-state](#mem-obj-preference-state), [MEM-OBJ-preference-text](#mem-obj-preference-text). Preference storage/lookup adapters not fully traced: no universal re-rating, cross-dataset or deletion parity claim. |
| Truth subspace numerical maintenance | Direct `cognee/modules/truth_subspace/build.py`, `cognee/modules/retrieval/hybrid/ranking.py`; hybrid truth call-site search | [MEM-OBJ-truth-state](#mem-obj-truth-state), [MEM-RTE-truth-maintenance](#mem-rte-truth-maintenance). Centroid update mathematics and all hybrid caller options not fully inspected; truth label establishes no factual verification. |
| Global context summaries and read-back prelude | Direct `cognee/tasks/memify/global_context_index/summarize.py`, `cognee/tasks/memify/global_context_index/persist.py`, `cognee/modules/retrieval/utils/global_context.py`, `cognee/modules/retrieval/graph_completion_retriever.py` | [MEM-OBJ-global-context-summary](#mem-obj-global-context-summary), [MEM-RTE-summary-readback](#mem-rte-summary-readback). Build/update bucketing and stale-summary rebuild on item deletion not fully traced. |
| Skills ingestion, discovery, load and replacement | Direct `cognee/modules/tools/ingest_skills.py`, `cognee/modules/engine/models/Skill.py`, `cognee/modules/retrieval/skills_retriever.py`, `cognee/modules/tools/builtin/load_skill.py`, selected agentic loop and run recorder, complete `cognee/modules/memify/skill_improvement.py` | [MEM-OBJ-skill-procedure](#mem-obj-skill-procedure), [MEM-OBJ-skill-metadata](#mem-obj-skill-metadata), [MEM-OBJ-skill-run](#mem-obj-skill-run); annotations on supplied skill records. Parser and all graph-backed Tool producers not fully traced: provenance metadata is not publisher validation. |
| Decorator hook and gateway injection | Supplied runtime plus direct `cognee/modules/agent_memory/runtime.py` | Annotation on [RT-RTE-decorated-agent](runtime.md#rt-rte-decorated-agent). Only structured-output gateway injection established, not arbitrary host-provider calls. |
| Recall alternative lanes: session, trace, active context, graph, tool, code, skills; readiness and fallback | Supplied `cognee/api/v1/recall/recall.py` account, remember typed/code/skills branch search; direct skills/graph completion read | [RT-RTE-recall-dispatch](runtime.md#rt-rte-recall-dispatch). Code, temporal, lexical, BM25, custom/community retrievers, external metadata and all lane ACLs remain unresolved; no single selector or authority claim for every recall result. |
| CLI and MCP dispatch | Direct selected command registry `cognee/cli/_cognee.py` and HTTP dispatcher `cognee/cli/api_dispatch.py`; bounded `cognee-mcp/src/server.py` registration/call-site search; supplied MCP client findings | [RT-RTE-recall-dispatch](runtime.md#rt-rte-recall-dispatch), [MEM-RTE-typed-admission](#mem-rte-typed-admission), [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal). Sessions/feedback/eval CLI commands exist beyond remember/recall; not all option forwarding or HTTP handlers traced. MCP local/API mode differs; no transport parity. |
| Forget, session invalidation and feedback removal | Direct `cognee/api/v1/forget/forget.py`, `cognee/modules/session_lifecycle/invalidate_sessions.py`, `cognee/api/v1/session/session.py`, FS deletion methods | [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal). Lower graph deletion implementations, update/migration, prune, preference/skill-specific withdrawal and material already copied outside Cognee not completely traced. |
| Shipped evaluation | Direct `cognee/eval_framework/evaluation/direct_llm_eval_adapter.py`; framework file inventory | [MEM-CLM-evaluation-boundary](#mem-clm-evaluation-boundary). Golden-answer scoring is implemented; no inspected link installs those scores into production SkillRuns or gates distillation. Other evaluators/retained run artifacts remain uninspected; no measured benefit. |
| Other included shipped consumers and maintainers | Boundary inventory: frontend, HTTP integrations, connectors, distributed workers, starter-kit, notebooks; supplied Company Brain later recall driver | Available but not substantively traced here. Prevents whole-system lifecycle closure, deployed host-use and UI authorization claims. |

External provider/model weights, database internals, separately distributed plugins and enclosing hosts stay excluded as in boundary. Their adapter calls remain included. There was no access gap for inspected files. These are bounded inspection limits, not evidenced absences.

## Core ideas

1. **Retention is layered, not one permanent memory store.** Session QA and sanitized traces can remain in an expiring cache. Improve can separately cognify their text, extract active guidance, distill standalone lessons, and update ranking state. Each result has a different gate and later reader. Session storage success does not imply graph publication; graph publication does not prove model use. See [MEM-RTE-trace-promotion](#mem-rte-trace-promotion) and [MEM-RTE-session-distillation](#mem-rte-session-distillation).
2. **Derived guidance has multiple selectors and authority levels.** Content prose influences a model; IDs, counters, flags and weights influence code. The session ranker budget-selects whole entries; graph retrieval selects triplets; skills discovery returns metadata and full procedures are requested separately. No one context-budget guarantee covers these routes. See [MEM-RTE-session-guidance](#mem-rte-session-guidance), [MEM-OBJ-feedback-weight](#mem-obj-feedback-weight) and the skill annotations.
3. **Admission checks do not authenticate source truth.** Dataset grants and local-path roots regulate access. Confidence thresholds, exact deduplication and writer rejection regulate software admission. Caller or model authorship remains separate. Models are asked to reject unsupported lessons, but those requests and the name “truth subspace” do not establish factual verification. See [MEM-RTE-session-distillation](#mem-rte-session-distillation) and [MEM-RTE-truth-maintenance](#mem-rte-truth-maintenance).
4. **Withdrawal follows only recorded dependencies.** Item deletion can propagate from graph IDs through QA, feedback, derived session guidance and later QA. Trace entries without graph IDs and append-only alternatives break that chain. Stored preferences, summaries and skill revisions have their own lifecycles; deleting evidence is not automatically undoing every derived update. See [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal).

## Shared records

### Components

none declared in this member

Model/embedding components already have identities and fixity limits in [RT-CMP-llm-gateway](runtime.md#rt-cmp-llm-gateway) and [RT-CMP-embedding-config](runtime.md#rt-cmp-embedding-config). This report adds retained numerical objects, not another provider component or any observed weight training.

### Operative objects

#### MEM-OBJ-graph-content
Label: Retained graph content text

Source-native identity: text-bearing DataPoints, including DocumentChunk, Entity descriptions and summaries. Representational form: natural-language content when rendered into completion input. Storage substrate: configured graph storage, with indexed copies/payloads in vector storage. Lineage: ingestion/chunking/extraction/summarization under [RT-RTE-permanent-memory](runtime.md#rt-rte-permanent-memory); later session promotion can contribute more content. This is the retained content produced by that route, not another declaration of its progression. SRC-1, `cognee/tasks/storage/add_data_points.py`, `cognee/modules/retrieval/graph_completion_retriever.py`.

> Add a batch of data points to the graph database by extracting nodes and edges,
> deduplicating them, and indexing them for retrieval.
> --- `cognee/tasks/storage/add_data_points.py`

Actual consumers are retrievers, summarizers and extraction/update models. Graph completion resolves selected edges to readable text before generating an answer. Delivery grants informational influence, not enforced truth or mandatory action. Fidelity to raw source and actual semantic extraction quality are unobserved. Raw files and relational data records remain separately retained on memory-only forget; they are not interchangeable with this derived content.

#### MEM-OBJ-graph-structure
Label: Graph identity and provenance structure

Source-native identity: DataPoint node/edge IDs, relationships, NodeSet membership and optional source references/run IDs. Representational form: symbolic units consumed by storage, scoping, deletion and graph traversal. Storage substrate: graph plus conditional relational provenance ledger; not model weights. SRC-1, `cognee/tasks/storage/add_data_points.py`. Distinct from [MEM-OBJ-graph-content](#mem-obj-graph-content): same store does not make content and access/lineage metadata the same operative part. Closest supplied route is [RT-RTE-permanent-memory](runtime.md#rt-rte-permanent-memory).

> data_id = data_item_id(data_item)
> stores_provenance = False
> if user and dataset and data_id is not None:
> --- `cognee/tasks/storage/add_data_points.py`

Provenance depends on a concrete context. Code can use graph-folded provenance or a relational ledger; hybrid writes can attach references in a second pass. This establishes different retention/recovery arrangements, not universal cross-store atomicity. IDs govern retrieval/deletion dependencies; source prose has different authority.

#### MEM-OBJ-vector-index
Label: Retained retrieval vector index

Source-native identity: DataPoint field collections, for example `Skill_search_text` and `GlobalContextSummary_text`, and dense indexed representations. Representational form: distributed numerical representation for similarity, distinct from symbolic collection names/payload IDs and readable text payloads. Storage substrate: configured vector engine. Lineage: selected Embeddable/index fields of retained DataPoints processed by the embedding component; exact indexing internals and immutable embedding provenance per entry remain uninspected. SRC-1, `cognee/modules/engine/models/Skill.py`, `cognee/modules/retrieval/skills_retriever.py`. This is a retained output/input surface of [RT-CMP-embedding-config](runtime.md#rt-cmp-embedding-config), not its inference component.

> "index_fields": ["search_text"],
> "identity_fields": ["name", "source_dir"],
> --- `cognee/modules/engine/models/Skill.py`

Skills retrieval searches vectors, then filters payloads and omits procedure text. A numerical hit is selection evidence, not source trust, correctness or complete procedural delivery.

#### MEM-OBJ-session-qa
Label: SessionQAEntry conversation record

Source-native identity: `SessionQAEntry`, including question/answer/context and symbolic QA/time/dependency/bookkeeping fields. Representational form: natural-language conversation fields consumed by completion; symbolic IDs and memify metadata separately govern selection, update and invalidation. Storage substrate: configured session cache (factory offers SQL, FS, Redis and Tapes), with configured session TTL. Lineage: generated exchanges or typed caller entries; summaries may replace stored context, but not question/answer. SRC-1, `cognee/infrastructure/databases/cache/models.py`, `cognee/infrastructure/databases/cache/get_cache_engine.py`, `cognee/modules/retrieval/utils/completion.py`. Retained object of [RT-RTE-session-improve](runtime.md#rt-rte-session-improve) and [RT-RTE-recall-dispatch](runtime.md#rt-rte-recall-dispatch), not either route.

> used_session_context_ids: list[str] | None = None
> --- `cognee/infrastructure/databases/cache/models.py`

Later history formatting deliberately omits context in the inspected answer paths. QA question/answer text also feeds graph promotion. `used_graph_element_ids` and `used_session_context_ids` are recorded dependencies, not proof every influential input was captured. Factory selection proves available substrates, not equivalent durability/TTL semantics on all adapters.

#### MEM-OBJ-session-agent-trace
Label: SessionAgentTraceEntry retained trace

Source-native identity: `SessionAgentTraceEntry`: function/status, memory query/context, parameters, returned value, error and per-step feedback. Representational form: symbolic fields plus natural-language/display serialization; arbitrary returned objects become sanitized representations rather than executable host objects. Storage substrate: session cache. Lineage: decorated host outcome or caller-supplied typed trace. SRC-1, `cognee/infrastructure/databases/cache/models.py`, `cognee/modules/agent_memory/runtime.py`. Distinct retained result of [RT-RTE-decorated-agent](runtime.md#rt-rte-decorated-agent); not a SkillRun or opaque full execution checkpoint.

> def sanitize_method_return_value(cls, v: Any) -> Any:
>     return sanitize_value(v)
> --- `cognee/infrastructure/databases/cache/models.py`

Later consumers include recent trace-feedback injection, pending-window extraction and graph promotion. A summary string is not the entire trace payload. Original host return values may have external/mixed provenance; typed traces are software-admitted records, not authenticated observed-run evidence. Sanitization/truncation loses information, and no resumable program-stack checkpoint is established by these fields.

#### MEM-OBJ-session-feedback
Label: SessionFeedbackEntry turn evidence

Source-native identity: `SessionFeedbackEntry`, storing raw follow-up text, referenced QA/rating, influencing context IDs and candidate-context dumps. Representational form: natural-language feedback and candidates with symbolic provenance/reference fields. Storage substrate: session-context cache list. Lineage: model turn analysis applied by code, distinct from direct QA `feedback_score` editing. SRC-1, `cognee/infrastructure/session/session_turn.py`. Closest supplied account is [RT-RTE-session-improve](runtime.md#rt-rte-session-improve); this evidence part is not the orchestration route.

> referenced_qa_ids=[previous_qa_id] if previous_qa_id else [],
> referenced_qa_rating=previous_answer_rating,
> influencing_context_ids=list(served_ids or []),
> --- `cognee/infrastructure/session/session_turn.py`

Consumers are preference update, feedback extraction and session invalidation; active-context ranking excludes non-context kinds. This is raw feedback plus model interpretation, not an independently verified correctness judgment. Candidate dumps retain some derivation evidence; they do not preserve inaccessible model reasoning.

#### MEM-OBJ-session-context
Label: SessionContextEntry active guidance

Source-native identity: `SessionContextEntry`, with QA or agent profile, section/content, confidence, priority, helpful/harmful counts, source feedback/trace IDs and timestamps. Representational form: natural-language guidance plus symbolic selection/provenance state. Storage substrate: session-context cache, not necessarily permanent graph. Lineage: accepted QA-turn candidates, live error lessons or batch trace extraction. SRC-1, `cognee/infrastructure/session/session_context_builder.py`, `cognee/infrastructure/session/agent_context_extraction.py`. This retained result is distinct from the workflow container [RT-RTE-session-improve](runtime.md#rt-rte-session-improve).

> No LLM, no fuzzy matching, no auto-delete. Each
> candidate is wrapped so one failure never raises; the whole call is fail-open and returns
> ``[]`` on outer failure.
> --- `cognee/infrastructure/session/session_context_builder.py`

Admission requires valid profile/section, nonempty bounded content and confidence at least 0.75; duplicates match normalized content within profile/section and receive source links. Batch agent lessons deliberately use an empty source ID, unlike live error lessons. Ranking/delivery and distillation consume these entries. Read-time counter updates change selection authority without editing guidance meaning. A whole entry is inspectable/editable through storage APIs, but complete derivation/rationale and deployed UI editing controls remain unestablished.

#### MEM-OBJ-session-learning
Label: Session learning document

Source-native identity: rendered `Session learning` documents tagged `session_learnings` and a session-specific truth node set. Representational form: natural-language standalone statement with optional `why_learned` sentence, plus symbolic document/session/set identity. Storage substrate: add's retained data and cognified graph/vector representations. Lineage: gated context and QA timeline → curator proposal → writer acceptance → deterministic rendering. SRC-1, `cognee/modules/session_distillation/distill.py`. Distinct product of the supplied maintenance container [RT-RTE-session-improve](runtime.md#rt-rte-session-improve).

> body = f"{statement} ({why}.)" if why else statement
> return f"# Session learning (session {session_id})\n\n{body}\n"
> --- `cognee/modules/session_distillation/distill.py`

Unlike raw QA/trace text, this is requested semantic curation. Reasons persist as prose within the document; model-proposed member IDs, decision reasons and glossary arrays are not all rendered into it. The whole statement/reason text can reach graph retrieval and truth embedding; a separate later criticism/rationale-review consumer is not established. Date-free rendering is intended to let identical retries deduplicate; that does not prove all differently worded lessons deduplicate.

#### MEM-OBJ-feedback-weight
Label: Graph feedback_weight ranking state

Source-native identity: per-node/per-edge `feedback_weight` and QA applied-ID/score/source/attempt metadata. Representational form: symbolic localized numerical ranking parameters, not distributed model weights or revised source propositions. Storage substrate: graph attributes plus cache bookkeeping. Lineage: explicit or inferred 1–5 answer rating and recorded used-element IDs; bounded streaming update. SRC-1, `cognee/tasks/memify/apply_feedback_weights.py`, `cognee/modules/graph/cognee_graph/CogneeGraph.py`. Material state part of the broad maintenance route [RT-RTE-session-improve](runtime.md#rt-rte-session-improve), distinct from its lock/admission policy.

> updated = float(previous_weight) + alpha * (normalized_rating - float(previous_weight))
> final_score = max(0.0, min(1.0, float(updated)))
> --- `cognee/tasks/memify/apply_feedback_weights.py`

Actual downstream authority is code ranking: positive feedback influence blends valid distances with this state; zero influence leaves distances unchanged. Raw feedback is retained separately. Bookkeeping can stop attempts even with missing/failed IDs; re-rating resets selected accounting rather than restoring pre-rating weights. Later consumers do not need to read feedback prose to apply the numerical effect.

#### MEM-OBJ-preference-state
Label: User prefers-edge ranking state

Source-native identity: user preference subgraph's `prefers` edges with weight/updated-at-turn and node turn counter. Representational form: symbolic localized numerical state consumed by decay and ranking code. Storage substrate: dataset graph, with per-QA applied/counted metadata in cache. Lineage: explicit QA rating takes precedence over inferred feedback-row rating; only used node IDs become targets. SRC-1, `cognee/modules/user_preferences/update.py`, `cognee/modules/retrieval/hybrid/ranking.py`. Distinct from global [MEM-OBJ-feedback-weight](#mem-obj-feedback-weight); closest supplied container is [RT-RTE-session-improve](runtime.md#rt-rte-session-improve).

> if rating is None or rating == 3:
>     continue
> --- `cognee/modules/user_preferences/update.py`

Neutral rating is skipped; turn counting includes unrated turns. Decay is computed on read, and near-neutral edges are pruned or subject to a storage fallback. Triplet scoring and hybrid chunk scoring can consume personal weights with separate influence settings. These weights do not assert user preferences in language; their content lineage and authority differ from preference text.

#### MEM-OBJ-preference-text
Label: Durable preference text

Source-native identity: preference node `text` and `text_watermark`. Representational form: natural-language preference lines plus symbolic watermark. Storage substrate: user/dataset graph node. Lineage: gated preferences-section context entries newer than the watermark, added newest first and whole-line capped; no semantic rewrite or content dedup in this refresh. SRC-1, `cognee/modules/user_preferences/update.py`. This is the text track beside [MEM-OBJ-preference-state](#mem-obj-preference-state), not another identity for it; both arise within [RT-RTE-session-improve](runtime.md#rt-rte-session-improve).

> combined = _truncate_to_whole_lines(combined, MAX_PREFERENCE_TEXT_CHARS)
> --- `cognee/modules/user_preferences/update.py`

Completion consumers receive preference guidance, even via a preferences-only block when auto-feedback is off; sessionless graph completion supplies preference text as its guidance layer. The text watermark and truncation can discard older statements. Known source entries do not establish human approval of each admitted line or uniform withdrawal on feedback removal.

#### MEM-OBJ-truth-state
Label: Truth centroid and alignment state

Source-native identity: retained centroid slots with learning IDs/epoch, and DocumentChunk `truth_alignment` numerical coordinates with `truth_epoch`. Representational form: distributed numerical embedding-derived geometry; epoch/signature/IDs are separate symbolic validity metadata. Storage substrate: vector-engine centroids and graph per-chunk state. Lineage: accepted session-learning text embeddings → centroid construction → chunk embedding projection. SRC-1, `cognee/modules/truth_subspace/build.py`, `cognee/modules/retrieval/hybrid/ranking.py`. New numerical product inside the maintenance container [RT-RTE-session-improve](runtime.md#rt-rte-session-improve), not [RT-CMP-embedding-config](runtime.md#rt-cmp-embedding-config)'s weights.

> scored[node_id] = {
>     "truth_alignment": coords,
>     "truth_epoch": current_epoch,
> }
> --- `cognee/modules/truth_subspace/build.py`

Actual consumer is conditional hybrid reranking. Matching epochs permit a bounded score multiplier; the label does not establish truth correspondence. The object changes through builds, but no provider-weight update is established. A mutable embedding endpoint may produce a changed basis; per-build immutable model provenance is uninspected.

#### MEM-OBJ-global-context-summary
Label: GlobalContextSummary hierarchy text

Source-native identity: `GlobalContextSummary`, including root/bucket text, level and dataset identity; `summarized_in` edges link children and parents. Representational form: natural-language compressed content plus symbolic hierarchy/provenance; indexed numerical representation is a separate selection part. Storage substrate: graph DataPoints and vector `GlobalContextSummary_text` collection. Lineage: child summary texts → model bucket/root summarization → persistence. SRC-1, `cognee/tasks/memify/global_context_index/summarize.py`, `cognee/tasks/memify/global_context_index/persist.py`. Product of optional indexing in [RT-RTE-session-improve](runtime.md#rt-rte-session-improve), not raw ingestion content.

> return await summarize_with_prompt(children, "global_context_bucket_summary.txt")
> --- `cognee/tasks/memify/global_context_index/summarize.py`

Later graph completion can receive root text plus query-selected bucket summaries. Model compression is requested, not demonstrated faithful; structural source references are dataset-level, not a complete single-document semantic dependency map. Persistence helpers can delete graph/index nodes; automatic rebuild across every upstream change remains uninspected.

#### MEM-OBJ-skill-procedure
Label: Skill procedure body

Source-native identity: `Skill.procedure`, with body copies in skill/search text. Representational form: natural-language operational instructions; symbolic skill ID/name identify the unit but do not execute its prose. Storage substrate: graph Skill with searchable field copies/index. Lineage: explicit SKILL.md ingestion or applied proposal. SRC-1, `cognee/modules/engine/models/Skill.py`, `cognee/modules/tools/ingest_skills.py`, `cognee/modules/tools/builtin/load_skill.py`. Distinct from proposal [RT-OBJ-skill-proposal](runtime.md#rt-obj-skill-proposal): this is deployed retained procedure, not candidate payload.

> body = skill.procedure or "(this skill has no procedure body)"
> if len(body) > MAX_SKILL_BODY_CHARS:
>     body = body[:MAX_SKILL_BODY_CHARS] + "\n... [truncated]"
> --- `cognee/modules/tools/builtin/load_skill.py`

Consumer is the agentic model after load_skill, through truncated tool-result text. Body admission is software ingestion or caller-requested replacement; original publisher and applying caller need not be human. Reasons for a revision reside in the proposal rather than the load result. Whole-procedure addressability is established; separately revisable assumptions and reliable compliance are not.

#### MEM-OBJ-skill-metadata
Label: Skill discovery and scope metadata

Source-native identity: `Skill` name/description, declared tools, dataset_scope/is_active and publisher/source metadata. Representational form: description interpreted by a model; symbolic scope/active/tool fields interpreted by code; publisher labels are informational. Storage substrate: graph and projected vector payload. Lineage: parser/ingester or graph writes; ingestion stamps dataset scope and stable scoped identity. SRC-1, `cognee/modules/tools/ingest_skills.py`, `cognee/modules/retrieval/skills_retriever.py`. Distinct from [MEM-OBJ-skill-procedure](#mem-obj-skill-procedure); both inform [RT-RTE-agentic-tools](runtime.md#rt-rte-agentic-tools).

> if not payload.get("is_active", True):
>     continue
> scope = [str(entry) for entry in (payload.get("dataset_scope") or [])]
> if self.dataset_id not in scope:
>     continue
> --- `cognee/modules/retrieval/skills_retriever.py`

Discovery over-fetches at least 20 or four times top_k, then filters/deduplicates/trims. It returns metadata, not body. Description guides model choice; scope and declared tool union affect code-level availability. Maintaining labels is not trusted publisher authentication, and scope filtering does not sandbox a permitted handler.

#### MEM-OBJ-skill-run
Label: SkillRun retained execution summary

Source-native identity: `SkillRun` with selected/candidate skills, task/result summary, tool trace, score/error and timing. Representational form: natural-language task/results and symbolic event/score/identity fields. Storage substrate: graph DataPoint and related records through add_data_points. Lineage: shipped agentic recorder after opened skills or typed caller SkillRunEntry; latter's actual execution and score origin can be opaque. SRC-1, `cognee/modules/retrieval/agentic_retriever.py`, `cognee/modules/tools/skill_runs.py`. Distinct retained input to [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision), not [RT-OBJ-skill-proposal](runtime.md#rt-obj-skill-proposal).

> result_summary=(result[:500] if isinstance(result, str) else ""),
> --- `cognee/modules/retrieval/agentic_retriever.py`

Recorder retains at most 1,000 output characters per tool call and a 500-character result summary. It records opened skills only; exceptional runs get zero score, otherwise a neutral unscored default. Drafting consumes run IDs/scores/errors/result summaries, not the full tool trace. This is retained operation evidence for a revision mechanism, not a guaranteed evaluation oracle or full replay checkpoint.

### Routes

#### MEM-RTE-typed-admission
Label: Typed memory admission

Endpoints/progression: typed remember input → QA/Trace/Feedback dispatch to SessionManager or SkillRun graph writer → result; caller may request skill revision. Owner: software dispatch and dataset/session resolution; caller supplies content. Context/state effects: cache rows or dataset-scoped SkillRun graph state. SRC-1, `cognee/api/v1/remember/remember.py`, `cognee/modules/tools/skill_runs.py`. Distinct admission alternative to [RT-RTE-permanent-memory](runtime.md#rt-rte-permanent-memory), overlapping session objects but not duplicating the generic bridge [RT-RTE-session-improve](runtime.md#rt-rte-session-improve).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: RememberResult with entry type/ID; session-backed entries report session_stored or errored, SkillRun returns completed after graph write.
- Later read-back: Session answer/history, trace extraction and feedback maintenance read their corresponding rows; skill revision reads qualifying SkillRuns.
- Delegated visibility: Store receives structured caller fields; typed traces need not be freshly executed host events.
- Selection predicate: Entry class; explicit session required except SkillRun; user and dataset resolution govern destination.
- Invalidation or expiry: Session TTL and session deletion; graph-backed SkillRun withdrawal is a separate graph lifecycle and not fully traced.
- Activation or effect: Storage dispatch and optional proposal creation wired; actual persistence/use unobserved.
- Evidence limits: Typed entries do not establish provenance authenticity, human authorship or every HTTP transport's equivalent admission.

Admission is software schema/access control, not per-item human approval. Caller can choose not to write or apply; caller role remains unresolved. Open record ingestion has no reference-answer oracle. QA/trace/feedback branches return immediately after their write rather than executing the ordinary automatic bridge in this function. Session attribution lookup fails open; attribution is not itself a universal dataset-write authorization gate for all session rows.

> if not session_id:
>     raise ValueError(
>         f"session_id is required for typed memory entries (got {type(entry).__name__})"
>     )
> --- `cognee/api/v1/remember/remember.py`

#### MEM-RTE-session-guidance
Label: Session guidance update and delivery

Endpoints/progression: next user turn plus preceding QA/served guidance → model analysis → feedback record/candidate admission/counter updates → history and active-guidance selection → completion → stored QA with served IDs. Owner: session-turn code, analysis model proposing interpretations and deterministic applier/ranker. This is a transformation/read-back part of the supplied session/recall behavior, not another whole recall dispatcher. SRC-1, `cognee/infrastructure/session/session_turn.py`, `cognee/infrastructure/session/session_context_builder.py`, `cognee/modules/retrieval/utils/completion.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Turn preparation/effective query or feedback acknowledgment; answer generation returns answer and selected context IDs.
- Later read-back: Subsequent answers reload selected prior question/answer history, current profile guidance and durable preference lines.
- Delegated visibility: Analysis receives current message, previous question/answer and served guidance content; completion receives history, rendered query/context, then guidance in user input.
- Selection predicate: Caching/auto-feedback gates; hybrid recent turns plus session vector hits; guidance ranks profile/section, confidence, query overlap, helpfulness, priority and recency, then fits whole content into 400-character per-section / 1,200-character total defaults.
- Invalidation or expiry: Context entries remain until cache expiry/deletion; counters/ranking can reduce delivery without removing content; invocation prompt is not a durable pointer to the store.
- Activation or effect: Prompt assembly and stored candidate/counter updates wired; obedience, factual correctness and changed behavior unobserved.
- Evidence limits: Budgets count content, not headings/time labels or all conversation tokens; concurrent answer alternative and session vector implementation not fully inspected.

Admission: model proposes candidates/rates context; code can reject shape, length, section, low confidence or duplicates. Human follow-up is possible but caller identity does not establish it. Ratings are judgments, not a golden-answer oracle. This is open conversational maintenance. Stored feedback candidates/source links retain selected evidence, not full reasoning; later ranker reads counters/content, not a formulated criticism record.

> user_prompt = "\n\n".join(filter(None, (session.history, rendered, session.guidance)))
> --- `cognee/modules/retrieval/utils/completion.py`

Working-context control is selection/omission, not isolation of a separate agent. Removed history is reachable via session selection; omitted guidance remains cached. Preference lines share the guidance content budget rather than creating a second session block. Old-to-new ordering is accompanied by a natural-language request to prefer later conflicting items, not an enforced conflict resolver. Optional context summarization runs beside answer generation and stores a summary; the inspected later history route omits context, so this summary is not established as a rolling compaction checkpoint used by the next answer.

#### MEM-RTE-trace-promotion
Label: Trace and QA promotion

Part of: [RT-RTE-session-improve](runtime.md#rt-rte-session-improve)

Endpoints/progression: session QA/trace cache → pending windows → text formatting → add/cognify into `user_sessions_from_cache` / `agent_trace_feedbacks`; separately traces → live error candidates or bounded model extraction → active agent-profile guidance. Owner: extraction/persist tasks and stage code. Relation is to a containing route; these transformations do not own its lock/start policy. SRC-1, `cognee/tasks/memify/extract_user_sessions.py`, `cognee/tasks/memify/extract_agent_trace_feedbacks.py`, `cognee/tasks/memify/cognify_session.py`, `cognee/tasks/memify/cognify_agent_trace_feedback.py`, `cognee/infrastructure/session/agent_context_extraction.py`, `cognee/modules/improve/stages.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Persist-task completion or propagated error; context extractor returns touched entry IDs, stage aggregates counts/results.
- Later read-back: Cognified text enters graph retrieval; active agent entries can be retrieved with the agent profile or distilled into graph lessons.
- Delegated visibility: QA graph promotion formats question/answer, not every QA metadata/context field; trace promotion uses summary or raw return text; batch extraction receives sanitized compact output/error lines plus up to 40 existing lessons.
- Selection predicate: Session/user scope and persist watermarks; capped trace persistence drains oldest pending steps; live status=error with message; batch pending interval 10 with overlap 3 and maximum 40 latest steps, improve flush threshold 1, at most five proposed lessons admitted per batch.
- Invalidation or expiry: Persist counts advance after checked cognify success; empty trace text can advance without ingestion; extraction count advances after completed attempt; raw cache TTL/deletion is separate from already cognified text.
- Activation or effect: Raw-to-derived writes and future retrieval paths wired; new semantic lessons and improved future actions unobserved.
- Evidence limits: Partial batch/save failures and result aggregation complicate progress claims; graph persistence is not full trace replay or authenticated experience.

Admission is software/model controlled: no per-window human approval. Default improve persists all pending traces in summary mode, but fallback summaries append sanitized returned content; explicit raw mode persists return values. Live error lessons are deterministic redacted error restatements with confidence 0.85, not inferred causal diagnoses. Batch extraction requests richer guidance under a prompt and deterministic candidate gate. These trace-fed results can shape later guidance, but raw logging alone would not establish that update path.

> return f"{fallback} Output: {return_text}"
> --- `cognee/tasks/memify/extract_agent_trace_feedbacks.py`

The bounded batch extractor selects the newest pending-plus-overlap window then stamps total trace count. A backlog exceeding 40 can therefore leave older pending steps outside that extraction window while advancing coverage; this differs from oldest-first bounded graph persistence. Batch lessons have no individual source-trace ID. The applier can swallow per-candidate store failures, so “completed extraction attempt” is weaker than every candidate stored.

Non-budget cognify error results can be logged and continued rather than raised by QA/trace persist tasks; failed windows retain their watermark. Extraction likewise can skip individual sessions. Thus the fatal QA stage policy handles propagated errors, not proof that every unsuccessful per-window build aborts the stage. No expected-answer oracle is used in these promotion transforms. Recovery retries retained windows; it is not atomic rollback of all previously published output.

#### MEM-RTE-session-distillation
Label: Session lesson distillation

Part of: [RT-RTE-session-improve](runtime.md#rt-rte-session-improve)

Endpoints/progression: authorized session/dataset → confidence/helpfulness-gated context → new-entry check → bounded chronological QA/context batches → curator → per-lesson novelty/glossary retrieval → writer accept/reject → standalone document → add/cognify → distilled-ID watermark. Owner: code selection and rendering; curator/writer models propose/decide content. Public distill_session can also run independently of improve. SRC-1, `cognee/modules/session_distillation/distill.py`, `cognee/infrastructure/llm/prompts/session_distillation_writer_system.txt`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: DistillationResult status/documents, or error after surviving documents may already be published.
- Later read-back: Graph recall can select published statement/reason text; truth build embeds tagged learning chunks; next distillation searches similar prior lessons.
- Delegated visibility: Curator sees truncated QA question/answer/feedback and candidate statements; writer sees proposed statement, resolved member contents, similar lessons and entity glossary, not full original trace payloads.
- Selection predicate: Context kind/profile rows, nonnegative clamped net helpfulness and minimum gate confidence; a new undistilled ID triggers work but curator uses all gated entries plus QA history; novelty search scopes lesson chunks by node set.
- Invalidation or expiry: Completed rejection/empty proposal runs advance gated-entry IDs; failed curator/writer calls leave watermark untouched; graph/raw lesson deletion and original-context changes have separate lifecycle limits.
- Activation or effect: Model judgment to document publication is wired; future graph delivery possible, factual warrant and behavioral benefit unobserved.
- Evidence limits: Search failure yields empty prior/glossary results; writer compliance unobserved; no per-member completeness check or independent truth oracle established.

Admission is two computational judgments plus code checks for accept and nonblank statement. Caller chooses to start but no per-lesson human review is required in this path. Writer guidance requests rejection of already-known, nondurable or unsupported lessons and exact glossary naming; model judgment supplies no independent oracle. This is open maintenance, not bounded comparative experimentation. Retry dedup relies on identical date-free rendered content; survivors persist before a later failure is raised. Rejection reasons are not all retained as durable documents, while accepted `why_learned` prose is.

> - accept=false, reason="unsupported": the MEMBER ENTRIES do not actually support the statement.
> --- `cognee/infrastructure/llm/prompts/session_distillation_writer_system.txt`

#### MEM-RTE-ranking-maintenance
Label: Feedback and preference maintenance

Part of: [RT-RTE-session-improve](runtime.md#rt-rte-session-improve)

Endpoints/progression: scored/inferred session feedback and used IDs → global graph feedback weight updates/bookkeeping; separate rated turns/context preferences → user preference subgraph/text/watermarks → later ranking and prompt guidance. Owner: deterministic software update, with upstream model-inferred ratings or explicit caller scores. Two parts share stage orchestration but not update/re-rating/invalidation semantics. SRC-1, `cognee/tasks/memify/apply_feedback_weights.py`, `cognee/modules/user_preferences/update.py`, `cognee/modules/graph/cognee_graph/CogneeGraph.py`, `cognee/modules/retrieval/hybrid/ranking.py`, `cognee/modules/retrieval/graph_completion_retriever.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Applied/skipped feedback counts or preference status/turn/edge/text counts, with nonfatal per-item failures and bookkeeping retries.
- Later read-back: Triplet ranking consumes global feedback/personal weights; hybrid consumes personal weights; answer input consumes preference text.
- Delegated visibility: Update code reads IDs/ratings/metadata and preference content; later ranking needs numerical state, not full feedback reasons.
- Selection predicate: Valid rating and pending used-element IDs for feedback; implicit feedback reduces alpha; personalization flag gates its own path; preferences use node IDs, nonneutral ratings and newer usable preferences-section context.
- Invalidation or expiry: Feedback applied-ID tracking/attempt cap limits retries and changed score/source resets selected tracking; preferences count each turn and apply each rating once, decay/prune on advancing turn counter, and cap old text.
- Activation or effect: Retained state changes ranking rules when influence is positive and preference prose reaches completion; exercised changes and better answers unobserved.
- Evidence limits: Store/bookkeeping operations are not one established cross-store transaction; feedback deletion is not an inverse update; personal re-rating behavior differs from global feedback reset.

Admission is software arithmetic/gates; explicit caller feedback need not be human and inferred ratings are computational. Invalid inputs or disabled personalization prevent writes; no benchmark oracle/adoption trial gates them. Recovery marks failed preference writes unapplied and keeps feedback applied IDs where possible; global attempt exhaustion can give up on missing/failed IDs. Removing feedback does not implement a general rewind to previous numerical state in the inspected clear/update functions.

> done = qa_success or attempts >= FEEDBACK_WEIGHTS_MAX_ATTEMPTS
> --- `cognee/tasks/memify/apply_feedback_weights.py`

#### MEM-RTE-truth-maintenance
Label: Truth alignment maintenance

Part of: [RT-RTE-session-improve](runtime.md#rt-rte-session-improve)

Endpoints/progression: opt-in, writable dataset/capable graph → accepted-learning text → embedding/centroid build or extension → all dataset DocumentChunk projections → per-chunk state writes → final centroid commit → conditional hybrid ranking. Owner: software geometry, external embedding inference and adapter writes; no additional generative truth judge. SRC-1, `cognee/modules/truth_subspace/build.py`, `cognee/modules/retrieval/hybrid/ranking.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Counts/signature/live epoch with completed/skipped/errored status.
- Later read-back: Query projection and matching-epoch chunk alignments can multiply hybrid ranking scores.
- Delegated visibility: Embedding component receives learning/chunk text; scorer reads numeric coordinates/epoch and query geometry, not full lesson reasons as criticism.
- Selection predicate: Opt-in and backend capability; session-scoped builds extend prior centroids, unscoped builds rebuild; only DocumentChunk text projected; use_truth_weight and query coordinates gate ranking.
- Invalidation or expiry: Chunk state is written before centroid epoch commit; mismatched epochs are ignored; failed batches skip nodes. Epoch-only matching has a known abandoned-basis countercase.
- Activation or effect: Numerical update and conditional reranking wired; no factual verification, activation or improved quality observed.
- Evidence limits: Epoch equality is not exact basis identity; full centroid mathematics and adapter atomicity uninspected.

Admission is deterministic update from already accepted lessons, not human approval or an independent expected-answer oracle. Source comments' strong “never wrong reranking” explanation is qualified by the same file's countercase: failed epoch-N+1 build, different next basis also at N+1, and skipped chunks can leave abandoned coordinates passing the guard. No universal consistency claim follows. Recovery keeps previous live epoch on failed final commit but does not roll back every chunk write.

> if truth_state.get("truth_epoch") == current_truth_epoch:
>     final_score *= truth_factor(truth_state.get("truth_alignment", []), q_coords)
> --- `cognee/modules/retrieval/hybrid/ranking.py`

#### MEM-RTE-summary-readback
Label: Global summary construction and readback

Part of: [RT-RTE-session-improve](runtime.md#rt-rte-session-improve)

Endpoints/progression: optional index stage → model bucket/root summaries and hierarchy persistence → later single-query graph-completion opt-in → root + query-relevant non-root summaries → textual prelude plus graph context → completion. Owner: stage/index software and summarizing model; caller opts into read-time prelude. This part spans production and later consumption, not the whole recall dispatcher [RT-RTE-recall-dispatch](runtime.md#rt-rte-recall-dispatch). SRC-1, `cognee/modules/improve/stages.py`, `cognee/tasks/memify/global_context_index/summarize.py`, `cognee/tasks/memify/global_context_index/persist.py`, `cognee/modules/retrieval/utils/global_context.py`, `cognee/modules/retrieval/graph_completion_retriever.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Generated/persisted summaries on write; textual root/area prelude on read or empty text when unavailable.
- Later read-back: Retained root/bucket content enters a future graph completion's context if include_global_context_index is true.
- Delegated visibility: Summary model receives child texts; answer model receives compressed root/relevant-area text, not every child body or complete rationale.
- Selection predicate: Write opt-in/LLM gate; stage graph buckets max size four; read root detection plus vector similarity for top_k non-root summaries (default three); batch graph-context branch does not build this prelude.
- Invalidation or expiry: Helpers delete graph/vector summary IDs and retain dataset-level provenance; complete automatic rebuild after upstream deletions is uninspected.
- Activation or effect: Model compression and later context prepending wired; faithful compression and influenced answers unobserved.
- Evidence limits: No total prelude character/token limit established by the inspected loader; index build/update scheduling and all retriever variants not traced.

Admission is software/model publication, not per-summary human review; no expected-answer oracle. Compression retains derived content and structural linkage, not an independently persisted critique. This is retained cross-invocation context selection, not removal of current agent turns followed by a resumable checkpoint.

> return f"{prelude}\n\n{graph_context}"
> --- `cognee/modules/retrieval/graph_completion_retriever.py`

#### MEM-RTE-memory-withdrawal
Label: Memory withdrawal and dependency cleanup

Endpoints/progression: forget target/authorization → dataset lock → graph/vector deletion → best-effort attributed session deletion or used-ID invalidation fixpoint → evidence cleanup/status reset → result; direct session feedback/context deletion provides narrower alternatives. Owner: delete/invalidation code, caller target selection and storage adapters. Distinct lifecycle route from the supplied ingestion/recall routes, especially [RT-RTE-permanent-memory](runtime.md#rt-rte-permanent-memory) and [RT-RTE-recall-dispatch](runtime.md#rt-rte-recall-dispatch). SRC-1, `cognee/api/v1/forget/forget.py`, `cognee/modules/session_lifecycle/invalidate_sessions.py`, `cognee/api/v1/session/session.py`, `cognee/infrastructure/databases/cache/fscache/FsCacheAdapter.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Deletion summary or error; nonfatal session cleanup failure can coexist with success.
- Later read-back: Successfully removed graph/vector/QA/context material cannot be selected from those stores; preserved raw records can be re-cognified on memory-only forget; unremoved traces/derived copies can remain reachable.
- Delegated visibility: Invalidation receives deleted node/edge IDs and recorded QA/feedback/context dependency fields, not semantic inspection of all retained prose.
- Selection predicate: Caller item/dataset/everything/memory_only; delete permission precedes context provisioning; data invalidation unions attributed and unattributed sessions, then follows used graph IDs → QA → feedback → source-linked context → later served-context QA to a fixpoint.
- Invalidation or expiry: Dataset deletion drops attributed sessions; item deletion removes matched contaminated rows and lowers surviving QA persist count when necessary; FS session deletion clears QA/trace/context keys; feedback deletion clears score/text only.
- Activation or effect: Cleanup paths wired; universal deletion, privacy erasure and suppression of already copied knowledge not established.
- Evidence limits: Trace text has no graph dependency IDs; Tapes append-only alternative does not see deletes; partial or missing provenance and nonfatal cleanup prevent universal withdrawal claims.

Admission of withdrawal is caller-selected software authorization, not necessarily human veto. Memory-only mode keeps data/raw files and resets status for rebuilding; this is recovery affordance, not rollback of all semantic derivatives. Source documents the deliberate gaps:

> Known limits (documented, deliberate): agent-trace entries carry context text
> without element ids and are not matched; the tapes cache backend is
> append-only and never sees deletes; sessions predating dataset attribution are
> only found through the ``{default_session_id}_{dataset_id}`` naming.
> --- `cognee/modules/session_lifecycle/invalidate_sessions.py`

The intra-session chain is source-supported, but no inspected item-level route reverses previously applied feedback weights, all preference text, lesson truth centroids or every global summary/procedure derived from removed evidence. Those are unresolved lifecycle questions, not evidence that no other shipped task could maintain them. Everything forget calls cache prune without a user argument; backend tenant extent requires adapter inspection before claiming it removes only that user's cache.

### Claims

#### MEM-CLM-evaluation-boundary
Label: Evaluation is not production admission

Claimed operation: the inspected direct LLM evaluator compares an answer against caller-supplied golden answer, returning score/explanation and attaching correctness metrics. SRC-1, `cognee/eval_framework/evaluation/direct_llm_eval_adapter.py`. This is a distinct evaluator surface, not a duplicate of [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision)'s score-based selector.

> args = {"question": question, "answer": answer, "golden_answer": golden_answer}
> --- `cognee/eval_framework/evaluation/direct_llm_eval_adapter.py`

A golden answer provides an expected-answer input to this evaluator; its provider/content provenance and actual runs are uninspected. No inspected connection writes this metric into production SkillRuns, validates proposed procedures through a held-out test, or controls session distillation admission. That is a linkage limitation, not a system-wide absence claim. QA follow-up ratings and neutral unscored SkillRun defaults must not be relabelled benchmark measurements.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-session-guidance
Label: Session guidance to answer generation

Consumer: structured-output completion model on subsequent session answers. Channel: user input assembled from history, rendered question/context and guidance last. Force: natural-language interpreted information/instructions; counters/scopes/budgets are enforced by code, conflict preference is requested in text. Horizon: later turns while cached guidance survives; durable preference text can span sessions. SRC-1, `cognee/modules/retrieval/utils/completion.py`, `cognee/infrastructure/session/session_context_builder.py`. Distinct from [RT-BAP-memory-injection](runtime.md#rt-bap-memory-injection)'s decorator prepending and [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance)'s tool-result channel. Supporting verbatim assembly is in [MEM-RTE-session-guidance](#mem-rte-session-guidance). Delivery is wired, actual influence unobserved.

#### MEM-BAP-ranking-state
Label: Retained ranking state to selection

Consumer: triplet and hybrid ranking code, then answer models/callers receiving selected results. Channel: feedback/personal scalar adjustment and conditional truth geometry multiplier. Force: code-determined ordering within candidate sets, not an instruction enforcing answer truth. Horizon: subsequent retrievals until state changes/deletes or configuration disables influence. SRC-1, `cognee/modules/graph/cognee_graph/CogneeGraph.py`, `cognee/modules/retrieval/hybrid/ranking.py`. Distinct from [RT-BAP-memory-injection](runtime.md#rt-bap-memory-injection) and [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance): retained experience can have update/selection authority without a model reading its reasons. Supporting arithmetic/guards appear under [MEM-OBJ-feedback-weight](#mem-obj-feedback-weight) and [MEM-RTE-truth-maintenance](#mem-rte-truth-maintenance). Selection wiring is established; changed output/benefit is unobserved.

## Annotations

#### On [RT-RTE-decorated-agent](runtime.md#rt-rte-decorated-agent)

Read-back selects recent cached trace **feedback strings**, not full trace payloads, and graph search uses GRAPH_SUMMARY_COMPLETION with configured top_k. Query can come from configured method parameter, fixed query, or first eligible string parameter. In only_context mode it selects bare context_result from verbose search output. SRC-1, `cognee/modules/agent_memory/runtime.py`.

> return truncate_text("\n\n".join(memory_parts), MAX_MEMORY_CONTEXT_LENGTH)
> --- `cognee/modules/agent_memory/runtime.py`

Recent-session text precedes graph text in the combined 4,000-character envelope, so truncation can preferentially exclude graph memory. Memory is automatically supplied at the decorated call trigger, not independently unsolicited ingestion. The ContextVar frame is discarded/reset on exit; returned host values and persistent traces escape it. No separate provider sandbox or hidden-agent context is established. Periodic trace graph persistence uses count divisibility and configured oldest-pending cap; it is not proof all prior traces became durable knowledge.

#### On [RT-OBJ-skill-proposal](runtime.md#rt-obj-skill-proposal)

Retained old/proposed procedures and rationale are natural-language; target IDs, runs_used, scope/status/confidence are symbolic admission/review fields in graph DataPoint storage. Proposal construction stores selected runs and model-name metadata; a model string is not a weight pin. Review get_proposal can expose rationale to a caller, but deployed load_skill returns only Skill name/body, not proposal reasoning. SRC-1, `cognee/modules/memify/skill_improvement.py`.

> rationale=draft.rationale,
> status="proposed",
> --- `cognee/modules/memify/skill_improvement.py`

This retains a reason-bearing revision proposal, not demonstrated content-directed criticism. The old procedure is a recovery reference; application does not compare current procedure to the stored old base. No separately wired rationale-guided next revision consumer was found in the inspected draft input.

#### On [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision)

Memory lineage: current Skill plus selected failing/low-scoring runs → complete replacement draft → retained proposal → caller-requested apply → Skill procedure/skill_text/search_text overwrite → future skill resolution/loading. SRC-1, `cognee/modules/memify/skill_improvement.py`. Draft input uses run result summaries rather than unabridged tool trace; proposals retain runs_used and rationale, but subsequent drafting uses current procedure and failure summaries rather than prior proposal criticism.

> skill.search_text = skill.skill_text
> skill.belongs_to_set = [_skills_node_set()]
> proposal.status = "applied"
> --- `cognee/modules/memify/skill_improvement.py`

Authorship is computational drafting, admission is caller-selected apply; caller may be human or software. The route supports trace-fed guidance replacement, not demonstrated capacity improvement. Neither score threshold nor apply is a correctness test. The downstream procedure may be truncated in load_skill/agentic delivery, so stored replacement is not guaranteed wholly received. Whole-procedure revisability is established; fine-grained assumptions, performed criticism and causal action changes remain unestablished as already qualified by runtime.

#### On [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance)

Direct handler inspection closes the runtime's full-load transformation gap, but refutes interpreting “full body” literally for all inputs. The handler slices procedure at 12,000 characters, prefixes a Skill heading and marks it opened; the agentic loop further caps tool output at 8,000 characters before append and keeps 1,000 in stored tool trace. SRC-1, `cognee/modules/tools/builtin/load_skill.py`, `cognee/modules/retrieval/agentic_retriever.py`.

> tool_output=tool_result[:1000],
> --- `cognee/modules/retrieval/agentic_retriever.py`

Selector is a foreground model's load_skill request by name within the already active set, not semantic dereferencing of an arbitrary retained pointer. Catalog name/description stays visible before the body. Truncated body sections remain in graph but no offset/page reload is established in this inspected handler. Natural-language procedure affects interpretation; ACL/tool-scope code retains separate authority. Frame reset removes active/opened selection metadata, not persistent procedure content. No whole-loop token cap follows from per-tool output and iteration caps.

## Write side

The primary graph write is caller ingestion through add/cognify, described in [RT-RTE-permanent-memory](runtime.md#rt-rte-permanent-memory). Software/model transformation controls admission after a caller requests it; the request is not a human endorsement of every extracted fact. Initial raw authorship and model extraction quality remain local unknowns. Content, symbolic graph/provenance and numerical indexes remain separate operative parts.

Session writes have alternative admission routes: generated exchanges, decorator traces, direct session APIs and typed remember records in [MEM-RTE-typed-admission](#mem-rte-typed-admission). Typed SkillRun entries are graph-backed even without session_id. Explicit skills ingestion requires content_type=skills, trusted local source roots and an explicit dataset; software stamps scope and IDs (SRC-1, `cognee/modules/tools/ingest_skills.py`). File/publisher provenance labels do not prove who authored or approved instructions.

Automatic transformations include QA-turn analysis/candidate admission and ratings ([MEM-RTE-session-guidance](#mem-rte-session-guidance)), live/batch trace extraction and QA/trace cognification ([MEM-RTE-trace-promotion](#mem-rte-trace-promotion)), two-model lesson curation/admission ([MEM-RTE-session-distillation](#mem-rte-session-distillation)), arithmetic feedback/preferences ([MEM-RTE-ranking-maintenance](#mem-rte-ranking-maintenance)), embedding-derived truth coordinates ([MEM-RTE-truth-maintenance](#mem-rte-truth-maintenance)) and summary compression ([MEM-RTE-summary-readback](#mem-rte-summary-readback)). All have later consumer paths; none supplies observed beneficial learning merely by being called improve.

QA traces become formatted question/answer graph content; trace records become summary/return-text graph content or agent-profile guidance, then potentially standalone distillates. SkillRuns become selected revision evidence. These transformations are not weight training. Derived lesson reasons survive as why_learned prose; skill proposal reasons survive in a separate proposal/review channel; active batch lessons do not keep individual source-trace links. Consequently later retrieval of useful text need not preserve all reasons used to admit it.

Authoring/editing surfaces differ from admission: caller can supply extraction prompts or typed fields; store APIs create/update/delete context entries; explicit feedback API edits QA scores; applied skill proposals replace procedure text. The inspected applier does not automatically rewrite old guidance on conflict. Ranking can change reliance while leaving text untouched. Skill application can be withheld, but no held-out evaluation or automatic rollback accompanies replacement. Withdrawal and reconstruction are traced in [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal); cleanup success must be assessed per store/dependency chain, not inferred from deletion's status label.

## Read-back

Request and delivery are separate stages. Recall requests select source lanes, search type and scope; automatic fallthrough can stop after session success ([RT-RTE-recall-dispatch](runtime.md#rt-rte-recall-dispatch)). Within graph completion, retained triplets are converted into readable text and supplied to a model; with no usable LLM, runtime establishes a chunk-oriented alternative. These are different consumers, not a universal generated-answer route.

Session answer preparation reloads a recent-plus-vector-hit question/answer history and ranked current guidance, and can inject graph preference lines under a shared guidance budget ([MEM-RTE-session-guidance](#mem-rte-session-guidance)). Agentic history instead uses its own get_session call and guidance builder; the inspected builder call defaults to QA profile, so agent-profile trace lessons are not automatically in this particular agentic guidance block (SRC-1, `cognee/modules/retrieval/agentic_retriever.py`, `cognee/infrastructure/session/session_context_builder.py`). Their other consumer is distillation/explicit profile selection. Do not infer agent-loop injection from storage under an agent label.

The decorator is a configured push at host invocation: code chooses recent trace-feedback and query-selected graph memory, then the structured-output gateway prepends it. A host using an unrelated provider remains outside this delivery path. Session guide delivery and skill delivery are different authority channels ([MEM-BAP-session-guidance](#mem-bap-session-guidance), [RT-BAP-memory-injection](runtime.md#rt-bap-memory-injection), [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance)).

Skill discovery returns filtered metadata; the foreground model requests procedure text via load_skill. Per-tool truncation and count bounds control pieces of working context, not a total model window. Current tool results accumulate by value; active/opened ContextVars are reset after the invocation and SkillRun summaries survive. No inspected route reloads a omitted suffix by offset. The frame lens fits selection-state reset, but not isolation of model-visible history: the ordinary loop has one accumulated input and a final return.

Feedback/personal/truth state can shape code selection without appearing as prose to the model ([MEM-BAP-ranking-state](#mem-bap-ranking-state)). Optional global summaries reintroduce compressed external retained content into graph completion, not host-turn compaction ([MEM-RTE-summary-readback](#mem-rte-summary-readback)). Pure get_session/get_proposal/storage APIs alone are storage/review capabilities; this report attributes operational read-back only where shipped answer, maintenance or documented review consumers are identified.

## Integration issues

1. **Qualify fatal QA persistence.** [RT-RTE-session-improve](runtime.md#rt-rte-session-improve)'s fatal-stage policy is implemented at orchestration, but [MEM-RTE-trace-promotion](#mem-rte-trace-promotion) establishes that non-budget per-window cognify error results can be continued without raising, and session extraction can skip failed sessions. Source: SRC-1, `cognee/tasks/memify/cognify_session.py`, `cognee/tasks/memify/extract_user_sessions.py`. Reconciliation should preserve policy while avoiding “successful/completed stage means all QA admitted.” End-to-end result aggregation remains uninspected.
2. **Typed admission is not the generic automatic bridge.** Typed session writes return from their branches; SkillRun is graph-backed and optionally produces a skill proposal. [MEM-RTE-typed-admission](#mem-rte-typed-admission) complements [RT-RTE-session-improve](runtime.md#rt-rte-session-improve) and [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision). Source: SRC-1, `cognee/api/v1/remember/remember.py`. Interface parity and automatic continuation claims must name their branch.
3. **Close progressive disclosure transformation uncertainty.** Annotation on [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) establishes handler/body truncation followed by loop truncation. [MEM-OBJ-skill-procedure](#mem-obj-skill-procedure) is deployed procedure; [RT-OBJ-skill-proposal](runtime.md#rt-obj-skill-proposal) is candidate/review state, not a duplicate. Source: SRC-1, `cognee/modules/tools/builtin/load_skill.py`, `cognee/modules/retrieval/agentic_retriever.py`. Full stored replacement need not reach the model wholly.
4. **Agent-profile delivery remains route-specific.** Batch/live trace extraction stores agent-profile guidance; inspected agentic guidance builder uses default QA profile. [MEM-OBJ-session-context](#mem-obj-session-context), [MEM-RTE-trace-promotion](#mem-rte-trace-promotion) and [RT-RTE-agentic-tools](runtime.md#rt-rte-agentic-tools) must not be collapsed into direct agent-lessons injection. Source: SRC-1, `cognee/infrastructure/session/agent_context_extraction.py`, `cognee/modules/retrieval/agentic_retriever.py`. Distillation/explicit profile reader provides other routes, but all public context-lane behavior is not traced.
5. **Different bounded windows have different coverage.** Trace graph persistence drains oldest pending steps; bounded batch lesson extraction reads latest at most 40 and stamps total count. [MEM-RTE-trace-promotion](#mem-rte-trace-promotion) records the backlog countercase. Source: SRC-1, `cognee/tasks/memify/extract_agent_trace_feedbacks.py`, `cognee/infrastructure/session/agent_context_extraction.py`. No uniform all-traces semantic extraction guarantee follows.
6. **Truth epoch is weaker than basis identity.** [MEM-RTE-truth-maintenance](#mem-rte-truth-maintenance) preserves both implemented commit ordering and abandoned-basis countercase in SRC-1, `cognee/modules/truth_subspace/build.py`. Reconciliation must not equate truth geometry with factual criticism or a complete consistency invariant.
7. **Withdrawal does not close all derivatives.** [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal) establishes intra-session dependency cleanup but leaves trace-ID gaps, append-only cache, already published distillates/summary updates, preference retraction and numerical reversal unresolved. Source: SRC-1, `cognee/modules/session_lifecycle/invalidate_sessions.py`, `cognee/api/v1/forget/forget.py`. These are lifecycle limits, not system-wide absences. Everything-forget cache prune's tenant extent also requires backend tracing.
8. **Evaluator linkage is unestablished.** [MEM-CLM-evaluation-boundary](#mem-clm-evaluation-boundary) establishes golden-answer scoring but not its connection to [MEM-OBJ-skill-run](#mem-obj-skill-run) or proposal admission. Source: SRC-1, `cognee/eval_framework/evaluation/direct_llm_eval_adapter.py`, `cognee/modules/retrieval/agentic_retriever.py`. Do not treat unscored defaults as measured task success.
9. **No new declaration knowingly duplicates a supplied referent.** Route parts explicitly mark the maintenance container; objects identify its retained products/inputs. New authority paths distinguish session-guide input and code ranking from decorator/skill channels. Closest supplied records are cited locally. Remaining possible overlap depends on unresolved all-lane and interface tracing, not a conflicting second declaration.

## Limitations and checks

The source identity/revision and supplied run fields were rechecked. Analysis is source-grounded capacity inspection at one commit, not observed operation. No targets or providers were executed. Missing evidence prevents claims of activated context, factual reliability, capacity improvement, successful autonomous theory building or causal self-improvement. The supplied skill theory account remains independently qualified; this report does not promote it from proposal/storage wiring to performed criticism or benefit.

Inventory explicitly retains opaque/uninspected alternatives: cache adapters, raw loaders, extraction/index internals, concurrent session flow, full recall lanes, skill parser/Tool producers, lower deletion/provenance operations, migrations/update/prune, UI/connectors/workers and other evaluators. Available evidence was not mistaken for access failure or absence. Source scans of missing guessed directories were not used as negative evidence. No static shipped prompt was counted as accumulated read-back merely because a later call loads it.

Validation: deterministic validate-output passed after the completed report was checked. Its form, identity, record references and quotation checks do not establish semantic correctness, integration acceptance or successful target execution.
