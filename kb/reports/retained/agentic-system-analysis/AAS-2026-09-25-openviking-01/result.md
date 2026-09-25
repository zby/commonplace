---
type: kb/types/agentic-system-analysis-result.md
description: 'OpenViking session and user-memory subsystem: queued commit, cumulative
  continuation, extracted memory and scoped later-consumer routes'
run-id: AAS-2026-09-25-openviking-01
system: OpenViking
run-date: '2026-09-25'
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: subsystem-only
reviewed-boundary: 4edc30b068934893bc94a4e1b8e87bab2100bce5
analysis-cutoff: '2026-09-25'
evidence-tier: code-grounded
memory-comparison:
  axes:
    behavioral_authority:
      assessment: known
      basis: wired
      note: Text is advisory context at inspected model/API boundaries. Index scores
        rank; checkpoint and served-URI metadata route selected context. Soul/identity
        wording does not prove binding instruction adoption by an excluded host.
      records:
      - OBJ-3
      - OBJ-4
      - OBJ-5
      - OBJ-7
      - RTE-5
      - RTE-6
      - RTE-4
      values:
      - knowledge
      - ranking
      - routing
    curation_operations:
      assessment: known
      basis: wired
      note: WM compression consolidates and updates; model-guided identity merge deduplicates;
        patches evolve entries; removal with retained diff history withdraws reliance;
        configurable recency/frequency changes salience and cooldown suppresses recent
        returns. No synthesis-of-new-claims requirement is established. Configured
        custom semantic policies remain deployment-specific.
      records:
      - RTE-2
      - RTE-3
      - OBJ-4
      - OBJ-7
      - RTE-6
      values:
      - consolidate
      - dedup
      - evolve
      - invalidate
      - decay
      - promote
    distilled_form:
      assessment: known
      basis: wired
      note: Derived WM/checkpoint bodies and preference prose are natural language;
        schema-governed identity/metadata fields and anchor/source-ID bindings are
        symbolic parts of the persisted derived artifacts. No weight update is included.
      records:
      - OBJ-2
      - OBJ-3
      - OBJ-5
      values:
      - natural-language
      - symbolic
    faithfulness_tested:
      assessment: uninspected
      basis: null
      note: No retained execution evidence testing dependence on recalled content
        was inspected. Source tests and documentation claims cannot establish yes,
        and static-only analysis cannot establish a system-wide no.
      records:
      - BAP-1
      - RTE-4
      values: []
    learning_scope:
      assessment: not-determinable
      basis: null
      note: User preferences explicitly span conversations; checkpoints continue one
        active User Turn. A session can contain several tasks and a turn need not
        equal a task. These facts do not determine the complete per-task/cross-task/per-project
        union.
      records:
      - RTE-2
      - RTE-3
      - OBJ-5
      values: []
    learning_timing:
      assessment: known
      basis: wired
      note: Use-time commit schedules asynchronous summary/extraction, persists outputs,
        and makes them available to ongoing continuation and later requests. Online
        here describes that service loop, not synchronous token-by-token updating;
        excluded training is not evidence for offline timing.
      records:
      - RTE-2
      - RTE-3
      - RTE-5
      values:
      - online
    lineage:
      assessment: known
      basis: afforded
      note: Caller-supplied messages/payloads are imported; caller-authored memory
        writes are afforded; summaries/user memory are trace-extracted; previews,
        metadata and index representations are compiled. Authored defaults alone are
        not the evidence for manual memory authorship.
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-3
      - OBJ-4
      - RTE-9
      values:
      - authored
      - imported
      - other-compiled
      - trace-extracted
    read_back_direction:
      assessment: known
      basis: afforded
      note: External agent retrieval and extractor-issued read requests are pull.
        Server-provided WM/checkpoints, initial extraction prefetch and merge prefetch
        are automatic push to named internal models. API return itself is not counted
        again as push.
      records:
      - RTE-4
      - RTE-5
      - RTE-6
      - RTE-7
      - RTE-8
      values:
      - pull
      - push
    read_back_signal:
      assessment: known
      basis: wired
      note: Automatic WM selects latest terminal session archive (coarse); checkpoint
        anchor and required-file matching supply identifier selection; extraction/merge
        prefetch uses semantic search with optional reranking judgment. User-requested
        find signals are not classified as push signals.
      records:
      - RTE-5
      - RTE-6
      - RTE-7
      - RTE-8
      values:
      - coarse
      - identifier
      - inferred-embedding
      - inferred-judgment
    representational_form:
      assessment: not-determinable
      basis: null
      note: Natural-language summaries and symbolic records/index metadata are established;
        arbitrary tool payloads and image content are opaque and cannot be classified
        from their text previews or URL containers.
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-3
      - OBJ-4
      - OBJ-5
      - OBJ-6
      values: []
    storage_substrate:
      assessment: uninspected
      basis: null
      note: VikingFS files and vector indexes are established. The physical AGFS/backend
        alternatives and general snapshot backend were not fully inspected; files/vector
        alone would not be a complete substrate set.
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-3
      - OBJ-4
      - OBJ-5
      - OBJ-6
      - OBJ-7
      values: []
    trace_learning:
      assessment: known
      basis: wired
      note: Automatic retained WM, checkpoint and user-memory writes feed later context/planning/extraction
        consumers. This definition does not require training weights or demonstrated
        improvement.
      records:
      - RTE-2
      - RTE-3
      - RTE-5
      values:
      - 'yes'
    trace_source:
      assessment: known
      basis: wired
      note: WM/checkpoints consume role-labelled messages and hydrated tool outputs.
        User-memory extraction omits ToolPart by default and may replace images with
        descriptions. Raw retention and recall bookkeeping are not additional learning
        routes.
      records:
      - RTE-2
      - RTE-3
      - OBJ-5
      - OBJ-6
      values:
      - session-logs
      - tool-traces
    write_agency:
      assessment: known
      basis: afforded
      note: Automatic commit transformations and caller-controlled content edits;
        a human-triggered commit remains automatic extraction. Manual external authoring
        is afforded through the write API.
      records:
      - RTE-1
      - RTE-2
      - RTE-3
      - RTE-9
      values:
      - automatic
      - manual
  scope: Session message capture, archive/commit, cumulative Working Memory and partial-Turn
    checkpoints; user-stage memory extraction/merge/write and later continuation,
    extraction prefetch, direct find, context-aware search and bounded user-memory
    recall. Excludes agent-evolution/training, session skills, resource/wiki compilation,
    plugin/bot loops and arbitrary host stores.
---

# OpenViking session and user-memory subsystem

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-openviking-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/openviking.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-openviking-01/memory-report.md`

**Memory analysis report SHA-256:** 58f4885795bd7c327137bddb36eaf113d4ef58bc3f836d0704904d5b3774f779

## Boundary and evidence

Evidence basis: source implementation and shipped instructions at 4edc30b068934893bc94a4e1b8e87bab2100bce5, pinned on 2026-09-25. No system execution or causal experiment was performed. This is a subsystem-only analysis of a memory/knowledge/context-engineering system: session acquisition, commit/archive/continuation, user-memory extraction/update and direct/context-aware memory retrieval.

OpenViking is broader than this boundary. Optional agent-evolution/training and session skill-extraction branches are excluded, as are resource/wiki compilation, bot loops, agent plugins, benchmark experiments and arbitrary client hosts. These exclusions prevent whole-platform improvement, tool-permission, learned-skill and benchmark-effect judgments. They are not absent capabilities. The included extraction branch is `_extract_user_memories`, with non-agent-evolution memory types; the session continuation branch is included independently, including working summaries and raw/tool/context alternatives. External models, configured storage and the invoking agent are dependencies; their deployed identities, operational correctness and isolation are not established by this source-only pass.

Source allowlist: the named Git repository only. No linked paper, live documentation, previous review or prior comparison supplied analytical evidence. The access root is `/home/zby/llm/commonplace/related-systems/volcengine--OpenViking`; evidence was read at the full commit, not from its worktree.

## Source register

| Source ID | Kind | Identity/location | Revision | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/volcengine/OpenViking` | 4edc30b068934893bc94a4e1b8e87bab2100bce5 | implementation | session API/service, commit and context branches, compressor user-memory dispatch, model resolver and auth entry points; specialist memory paths registered below | `openviking/server/routers/sessions.py:661-714`; `openviking/service/session_service.py:189-222,369-453,534-618`; `openviking/session/session.py:1236-1390,1570-1680,1928-2145,2492-2605`; `openviking/session/compressor_v3.py:419-531,662-813`; `openviking/service/search_service.py:91-177`; `openviking/config/vlm.py:1-160`; `openviking/server/auth/__init__.py:88-145,174-202`; `openviking/server/auth/plugins/dev.py:20-65` | static source; deployment, excluded training/host branches and provider internals uninspected |
| SRC-2 | Git | `https://github.com/volcengine/OpenViking` | 4edc30b068934893bc94a4e1b8e87bab2100bce5 | doctrine/design | README's context database/session descriptions and scoped memory prompts | `README.md:41-130`; `openviking/prompts/templates/compression/ov_wm_v2.yaml`; `openviking/prompts/templates/memory/preferences.yaml`; `docs/en/api/16-memory.md`; `docs/en/concepts/08-session.md` | benchmark prose is a claim, not an observed experiment in this analysis |

## Shared records

### Components

CMP-1 — Session service, `Session`, ArchiveStore, QueueFS and task tracker coordinate persistence and background extraction. Symbolic Python and storage protocols; implementation conclusion status: wired. The HTTP client owns requests; code owns archive numbering, path locking and stage transitions. Evidence: SRC-1, `openviking/service/session_service.py:369-453`, `openviking/session/session.py:1236-1390,1570-1680`.

CMP-2 — Account-configured VLM supplies summary/extraction and query-planning calls. Distributed-parametric internals are external. Runtime model selection conclusion status: wired; exact parameter/version pinning: uninspected; parameter changes during the included operation: uninspected inside the provider. The resolver returns account-bound handles whose calls use current resources, rather than binding this source revision to model-weight bytes. Optional explicit agent training is excluded, not silently classified as absent. SRC-1, `openviking/config/vlm.py:24-47,88-158`; `openviking/session/compressor_v3.py:701-740`.

> class AccountBoundVLM:
>     """Long-lived Account proxy; every model call uses the current resource."""
> --- `openviking/config/vlm.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

CMP-3 — Embedding/retrieval machinery supplies indexed search. Distributed-parametric embedding and optional query-planner contributions are distinguished from symbolic filters and returned references. Embedding/retrieval backend. Implementation conclusion status: wired. Vector search and optional reranking choose candidates; configured hotness blends recency/frequency metadata. SRC-1 `openviking/storage/viking_fs/_semantic.py:240-310,410-527`; `openviking/retrieve/hierarchical_retriever.py:590-661`. No model-weights memory update is established by this component. Exact embedding/reranker model identity, fixed weights and provider parameter changes remain uninspected; no operation here establishes weight updates.

### Operative objects

OBJ-1 — Session messages, including TextPart, ContextPart, ImagePart and ToolPart. Implementation conclusion status: wired. Raw messages are caller-supplied, serialized JSONL; tool references and summaries do not exhaust the original payload. A ContextPart carries URI and abstract, not the full referenced resource. Image URLs may be converted to extraction-only descriptions. SRC-1 `openviking/message/part.py:1-78`; `openviking/session/session.py:1517-1546`. Arbitrary images/tool output prevent a complete form classification from the inspected wrappers.

OBJ-2 — Archived raw conversations plus generated summary sidecars. Implementation conclusion status: wired. Raw `messages.jsonl` is distinct from `.overview.md` WM and `.abstract.md`. WM is cumulative, natural-language, trace-extracted context. Source IDs, completion state and token metadata are symbolic control data. Summary generation writes sidecars with `generated_by` metadata; a counts-only fallback can replace semantic WM when the VLM is unavailable and no checkpoint is required. SRC-1 `openviking/session/session.py:1980-2104,2897-2964`. Rationale retention is requested, not guaranteed; later WM creation/update, continuation and intent analysis read the document.

OBJ-3 — User-stage memory Markdown records. Implementation conclusion status: wired. Account-defined schemas govern paths, fields and merge operators; predefined examples include preferences, profile, entities, events, identity and soul. Plain prose is accompanied by system metadata, versions and optional links. Initialization can copy authored defaults, extraction changes content, and public content edits are afforded. User-stage persona text is included because it is returned by this branch; it does not imply analysis of the excluded agent-evolution branch. SRC-1 `openviking/session/compressor_v3.py:692-780`; `openviking/session/memory/memory_updater.py:1087-1213`; `openviking/prompts/templates/memory/identity.yaml:1-55`; `openviking/prompts/templates/memory/soul.yaml:1-43`. At the inspected consumers it is contextual knowledge; prescriptive wording alone does not prove instruction authority in an excluded host.

>       Preference content in Markdown format describing "what the user prefers/is accustomed to".
>       Write one concise bullet per distinct, reusable preference; omit exact duplicates,
>       events, dates, and plans. Preserve the specific choice, list members, conditions,
>       exceptions, and user-stated reason or emotional meaning when they make the preference
>       answerable or distinguish it from nearby preferences.
> --- `openviking/prompts/templates/memory/preferences.yaml` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

OBJ-4 — Retrieval/index metadata. Implementation conclusion status: wired. Vector entries, abstracts, categories, tags, URI/level fields, active_count and updated_at govern ranking and selection. They are compiled access representations, not an independently verified account of source truth. SRC-1 `openviking/session/memory/memory_updater.py:1398-1542`; `openviking/retrieve/hierarchical_retriever.py:590-661`. Links/backlinks reside in files; that alone does not establish a graph database substrate.

>                 h_score = hotness_score(
>                     active_count=c.get("active_count", 0),
>                     updated_at=updated_at_val,
>                 )
>                 final_score = (1 - alpha) * semantic_score + alpha * h_score
>             else:
>                 final_score = semantic_score
> --- `openviking/retrieve/hierarchical_retriever.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

OBJ-5 — partial-Turn checkpoint records in archive `.meta.json`. Implementation conclusion status: wired. Natural-language cumulative abstract plus symbolic anchor/source IDs and estimated token count; derivation is trace-extracted with server bindings. Budgets truncate to at most 1024 tokens, or up to 256/configured budget when active tokens exhaust the allowance. SRC-1 `openviking/session/checkpoints.py:345-400`. It is a distinct part of the parent's OBJ-2 container, not a reassignment of that ID.

> When Turn-budget retention keeps a still-active User Turn but archives the
> assistant/tool steps that overflow the budget, Phase 2 records a bounded
> cumulative *checkpoint* summary for that Turn. Context assembly later re-injects
> the checkpoint as a synthetic ``ContextPart`` right after the retained anchor,
> so the model keeps continuity without replaying the archived raw steps.
> --- `openviking/session/checkpoints.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

OBJ-6 — externalized tool-result bodies and deterministic previews. Implementation conclusion status: wired. File-backed content retains raw tool output, references, hashes and read bounds. Inline previews are compiled and lossy; read/hydration routes can request full text or a range. SRC-1 `openviking/session/tool_output_externalizer.py:1-22,123-169`; `openviking/message/part.py:45-78`. Generic tool payload semantics remain opaque.

OBJ-7 — session recall ledger `.recall_log.json`. Implementation conclusion status: wired. Raw symbolic served-URI/turn/detail metadata is capped/pruned and bypasses semantic processing. It changes which memory is eligible for future delivery; it is not a new extracted substantive claim. SRC-1 `openviking/retrieve/context_assembler/ledger.py:1-25,114-173`.

### Routes

RTE-1 — HTTP caller adds messages under a session request identity. The session dependency resolves account/user/role and deliberately omits the actor-peer view. `add_message_async` delegates to the authoritative batch append path. Producer is the external caller; acquired content may include user/model/tool material and is not assumed true. Implementation conclusion status: wired. Immediate return is stored message metadata; persistence, externalized tool payloads and later consumer details appear in the memory overlay. Authentication grants depend on the selected plugin; the repository also has localhost-only development ROOT mode and direct Python construction, so no deployment-wide isolation guarantee follows. Source: SRC-1, `openviking/server/auth/__init__.py:190-202`, `openviking/session/session.py:899-922`, `openviking/server/auth/plugins/dev.py:23-65`.

> """Build a Session context without accepting an actor peer view."""
> --- `openviking/server/auth/__init__.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

> return ResolvedIdentity(
>     role=Role.ROOT,
>     account_id=x_openviking_account or "default",
>     user_id=x_openviking_user or "default",
> )
> --- `openviking/server/auth/plugins/dev.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

RTE-2 — Explicit commit, or the configured best-effort automatic scheduler, triggers archive/continuation processing. Phase 1 locks the session path, rereads live messages and metadata, resolves retention/policy, persists an archive intent/raw conversation and queue item, then publishes retained root state and a ready marker. Phase 2 processes summary/memory work through persistent QueueFS. Implementation conclusion status: wired; durability/recovery guarantee strength: protocol contingent on storage/queue contracts, not observed crash resilience. The endpoint returns `accepted` and `task_id`, which do not mean extraction completed. Source: SRC-1, `openviking/session/session.py:1236-1390,1570-1647`.

> "status": "accepted",
> "task_id": task_id,
> "archive_uri": archive_uri,
> "archived": True,
> --- `openviking/session/session.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

Admission/recovery: code rejects inconsistent reset/retention arguments; the selected policy may disable working memory. Phase-1 failures mark the archive failed, restore the in-memory original message list and rethrow; Phase-2 progress records completed memory-step IDs for restart recovery and retries transient API errors. These mechanisms reduce repeated work but do not establish exactly-once side effects under every crash. A context-reset archive is a logical boundary, not deletion of raw history. Automatic scheduling deduplicates in-flight work and logs/skips scheduling errors; the next write/idle scan can retry. Source: SRC-1, `openviking/session/session.py:1281-1310,1598-1678,2009-2140`, `openviking/service/session_service.py:534-618`.

> # Persist progress before waiting for sibling Phase 2
> # tasks. A process restart or a sibling failure can then
> # resume without applying this memory step twice.
> await self._merge_archive_meta(
> --- `openviking/session/session.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

> Phase 2 of a commit generates / updates a structured 7-section Working
> Memory document stored at ``archive_NNN/.overview.md``.
> 
> * First commit: call ``compression.ov_wm_v2`` with a plain completion unless
>   partial-Turn retention also needs checkpoint summaries. In that case the
>   same call uses ``create_working_memory`` and returns both products.
> * Subsequent commits: call ``compression.ov_wm_v2_update`` with the
>   ``update_working_memory`` tool to get a per-section decision plus any
>   requested checkpoint summaries, then run section-level merge against the
>   previous WM.
> --- `openviking/session/working_memory.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

>             lines.append(p.text)
>         elif isinstance(p, ToolPart) and p.tool_name:
>             status = p.tool_status or "completed"
>             output = redact_inline_images(p.tool_output or "")
>             lines.append(f"[tool:{p.tool_name} ({status})] {output}")
>         elif isinstance(p, ContextPart) and p.abstract:
>             lines.append(f"[context] {p.abstract}")
>     body = "\n".join(lines) if lines else "(no content)"
> --- `openviking/session/working_memory.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

>   ## Key Facts & Decisions
>   _Stable facts about the user's world: conclusions, relationships, preferences, constraints, technical choices with rationale, commitments, dates, quantities. One bullet per fact._
> --- `openviking/prompts/templates/compression/ov_wm_v2.yaml` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

Working-memory creation/update and partial-Turn checkpoints are both trace-fed retained products. Source-native seven-section WM consumes prior completed WM plus hydrated message/tool evidence. A counts-only fallback can replace semantic WM when the VLM is unavailable and no checkpoint requires content. Context reset stops older summaries; checkpoint validation rejects malformed output before persistence. The later consumers are RTE-5 and RTE-7. Task horizon remains not-determinable: an active turn is not necessarily an entire task. Input source union is session logs and tool traces; timing is online use-time asynchronous processing; distilled form combines natural-language summaries with symbolic bindings. Rationale/correction history is requested in prompts and delivered when included text is selected; neither complete preservation nor beneficial criticism is established. Formulation of a stored plan is afforded; its contextual use is wired; content-directed criticism and attributable capacity improvement remain uninspected.

Immediate return is archive/task acceptance; later delivery can occur only through successful terminal context selection. Delegated visibility is external-host-owned. RTE-5 selects by latest terminal archive, anchor identity and token budget; reset/terminal markers change eligibility. No actual activation is observed.

RTE-3 — Included user-memory extraction is invoked with messages, previous overview, account context, memory-type/peer policies and configured VLM. Its model-guided extraction loop proposes operations, can use registered memory tools, resolves operations and submits them to the streaming updater. Extractor loop defaults and final-answer instructions are policies, not a strict universal model-call cap: tool/refetch and resolution-repair branches extend iteration allowance. Implementation conclusion status: wired. The server/configuration governs allowed memory scope; the model proposes content and code admits operations under the implemented write rules. Source: SRC-1, `openviking/session/compressor_v3.py:662-813`, `openviking/session/memory/extract_loop.py:292-363`.

> operations, _tools_used = await orchestrator.run()
> if operations is None:
>     tracer.info("[v3_patch_merge] No memory operations generated")
>     return _V3ExtractionResult()
> --- `openviking/session/compressor_v3.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

> if iteration >= max_iterations:
>     max_iterations += 1
>     self._disable_tools_for_iteration = True
> --- `openviking/session/memory/extract_loop.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

Alternate branches are explicit: `extract_long_term_memories` also dispatches training-case, agent-experience/trajectory training and optional session-skill paths. This analysis does not infer their behavior from the user-memory route. `AGENT_EVOLUTION_MEMORY_TYPES` names cases, trajectories and experiences; excluding them is an analytical branch restriction, not a claim about default deployment. Source: SRC-1, `openviking/session/compressor_v3.py:419-531`, `openviking/session/memory/constants.py:4-9`.


Memory amendment for RTE-2: it archives raw input before summary generation. It uses the prior completed WM and new hydrated messages, creates or updates seven sections, and persists sidecars. Completion/failure markers and recorded completed extraction steps allow queued work to resume without deliberately applying completed steps twice. These are service recovery controls, not a semantic correctness test. Reset can append an empty completed boundary that stops older context and subsequent summaries. Failed terminal archives do not automatically replay their raw contents through the normal context route. SRC-1 `openviking/session/session.py:1644-1667,1680-1805,2106-2131,2601-2689`.

The checkpoint subobject OBJ-5 keeps the active User Turn anchor while summarizing its archived assistant/tool prefix. Server-owned IDs bind generated summaries to the right retained turns; output-count and empty-summary checks reject malformed checkpoint output before persistence. The later injection route preserves source message IDs and marks the synthetic message `checkpoint`. It supplies a concrete within-turn continuation horizon, but not a universal per-task horizon.

Memory amendment for RTE-3: it resolves the account's user-stage registry, self/peer scope and extraction VLM. The default user extraction conversation formatter omits tool calls/results; it does not inherit WM's full-tool evidence merely because both run in Phase 2. Although `latest_archive_overview` is accepted/stored by this provider, the inspected `_assemble_conversation` body does not append it. The accepted parameter therefore does not establish direct consumption of prior WM by RTE-3. SRC-1 `openviking/session/memory/session_extract_context_provider.py:297-355`. Image normalization constructs text descriptions before extraction and may omit image-only messages when no description can be produced.

The extraction prompt requires reading an existing memory before editing it and treats message roles as ownership evidence. The updater applies resolved types/peers, skips unresolved operations, reads latest disk content before field merges, and preserves a prior field when its merge operation fails. Updates increment version metadata and refresh vector representations; deletion removes the file and associated vector entry. Apply can report per-operation errors, so the model-facing phrase “single atomic plan” is not proof of all-or-nothing transactional semantic adoption. SRC-1 `openviking/session/memory/session_extract_context_provider.py:221-250`; `openviking/session/memory/memory_isolation_handler.py:195-206,349-427`; `openviking/session/memory/memory_updater.py:857-1025,1087-1213,1381-1395`.


The second-stage merge buffers proposals by scope/type, reads originals and candidates, and instructs the model to preserve every distinct fact before deletion/replacement. Required schema identity checks and exact patch mechanics do not validate the truth of user statements. The merge can fall back to unmerged operations when strict errors are disabled; provenance restoration after merging is explicitly best effort. SRC-1 `openviking/session/memory/streaming_memory_updater.py:751-902,1308-1351`. Records must not promote this mechanism into independently verified belief revision.

Reason retention is route-specific. WM's Key Facts & Decisions requests rationale and Errors & Corrections records correction history. Preference text keeps reasons where they distinguish a preference. Full-text reads by the maintenance model, future WM generation and context/intent supply can deliver those reasons. Short abstracts, compact result tiers, truncation, missing fields or model omission can remove them. No field requires every prescription to have a reason, and no later route guarantees it reads the relevant reason. Memory diff retains before/after/deleted content and skipped-operation reasons for audit; it is neither a mandatory explanatory rationale nor proof of executed rollback. SRC-1 `openviking/session/compressor_v3.py:314-417`; the RTE-3 identity-rule quotation and OBJ-3/RTE-2 rationale quotations.



> 
>             By default this provider extracts user/session memories, so tool
>             calls/results are omitted: they are execution evidence rather than
>             user utterances and can leak environment/database state into user
>             memories. Agent-scope providers enable tool evidence explicitly.
>             """
> --- `openviking/session/memory/session_extract_context_provider.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

> - Search similarity, a shared category, or an overlapping topic only identifies candidates for
>   review. It is never sufficient evidence that two memories have the same identity.
> - Merge memories only when they have the same identity under the active memory schema. For
>   real-world entities or events, require the same object or occurrence, or an explicit alias. For
>   preferences, both the owner and the behavioral choice dimension must match.
> --- `openviking/session/memory/merge_policy.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

>                         tracer.info(
>                             f"[memory_updater] Skipping field update after merge_op failure: uri={uri}, field={field.name}, error={e}"
>                         )
>                         if current_value is None:
>                             metadata.pop(field.name, None)
>                         else:
>                             metadata[field.name] = current_value
>                         continue
>                     metadata[field.name] = new_value
> --- `openviking/session/memory/memory_updater.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

>         for uri in result.deleted_uris:
>             deleted = delete_by_uri.get(uri)
>             deletes.append(
>                 {
>                     "uri": uri,
>                     "memory_type": (deleted.memory_type if deleted else None) or "unknown",
>                     "deleted_content": deleted.content if deleted else "",
>                 }
>             )
> --- `openviking/session/compressor_v3.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

The RTE-3 trace learning is wired: session-text/image-derived user-memory assertions persist and feed later extractor or retrieval consumers. ToolPart is omitted by this user formatter; tools still belong to the RTE-2 union. Guidance names identity preservation and user-stated reasons, not an independent answer oracle. Formulation of explanatory content is afforded by schemas; operative content use is wired; content-directed criticism, a criticism-caused revision and improvement attributable to it each remain uninspected. Edits/deletes and structural admission do not fill those missing links. Addressability is field/file-level under schemas; source rationale may be present but is not mandatory. Immediate return is operation/result metadata; persistence and later visibility depend on successful file/index writes. Selection/revision/invalidation follow schema/type/identity policies; human veto is optional configuration/editing, not an automatic per-write gate. Recovery may preserve failed fields or report skipped/failed operations, without proving all-or-nothing rollback.

RTE-4 — Caller requests `find` with query/target URI/filter/level/limit, or `search` with optional session context. Both return retrieval results to the caller. When intent is enabled and no image query is used, `search` obtains session context before calling VikingFS; direct `find` omits it. Implementation conclusion status: wired. The request's selection is not proof the returned memory changes the external agent's behavior. Source: SRC-1, `openviking/service/search_service.py:91-177`.

> if session is not None and self.is_intent_enabled() and not resolved_image_url:
>     session_info = await session.get_context_for_search(query)
> --- `openviking/service/search_service.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

Direct find/context-aware search. Implementation conclusion status: wired. API pull is afforded to external agents, while internal extractor prefetch is wired. Find performs QUICK semantic retrieval with scope/filter/level/limit; search can use retained session context in an account query planner and then execute planned queries. External return is an available result; an excluded host's subsequent adoption is uninspected. SRC-1 `openviking/service/search_service.py:91-176`; `openviking/storage/viking_fs/_semantic.py:240-310,410-527`. Immediate results are ranked references/content. Internal history/planner activation is wired only as supply; actual change to behavior is uninspected. Requested URI/filter/level/limit and contextual planning govern selection. Fast direct-find bypasses hotness; no universal decay claim covers all paths. Subsequent external consumer use is afforded. Delegation and semantic expiry are host/deployment-specific; updates and recall cooldown can alter eligibility.

RTE-5 — automatic continuation checkpoint assembly. Implementation conclusion status: wired. On session context assembly, the coordinator selects the latest terminal archive and raw newer pending messages; successful terminal checkpoints are matched against retained message IDs and inserted after their anchors as synthetic assistant ContextParts. The internal query planner receives this automatically assembled history; external continuation agents have a pull API affordance. Identifier push applies to checkpoint matching, coarse push to newest-archive selection. SRC-1 `openviking/session/session.py:2601-2689`; `openviking/session/checkpoints.py:402-478`.

>         result: List[Message] = []
>         for message in messages:
>             result.append(message)
>             candidate = candidates.get(message.id)
>             if not candidate:
>                 continue
>             abstract = candidate["abstract"]
>             if not abstract:
>                 continue
> --- `openviking/session/checkpoints.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

Route audit: immediate return is the selected content or write result; persistence is on the referenced objects, not a new implicit store. Later read-back/consumer and selectors are stated above; delegated visibility and actual activation remain uninspected. Scope and budget/cooldown/terminal-state rules delimit eligibility; no content-truth guarantee follows. Recovery is caller retry or the recorded upstream recovery path, not an asserted automatic semantic rollback.

RTE-6 — extraction and merge prefetch. Implementation conclusion status: wired. At extraction start, allowed self/peer schemas select fixed files and searchable directories. Search from compact conversation text delivers candidate results; eager mode automatically reads top N and disables further model tools. Without eager mode the extractor can request `read`. Merge prefetch reads required file URIs and, for new proposals, bounded semantic candidates. Recipients are the extraction and patch-merge models. SRC-1 `openviking/session/memory/session_extract_context_provider.py:363-402,481-624`; `openviking/session/memory/patch_merge_context_provider.py:174-224`. Required URI matching is identifier push; schema-wide fixed-file availability is coarse selection; semantic candidates use embedding and optional reranker judgment.

>         for file_uri in read_files:
>             call_id_seq = await self._append_structured_read_result(
>                 messages=pre_fetch_messages,
>                 call_id=call_id_seq,
>                 file_uri=file_uri,
>             )
> 
>         # eager_prefetch 模式：读取搜索结果 top-N
>         if self._eager_prefetch:
> --- `openviking/session/memory/session_extract_context_provider.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

Route audit: immediate return is the selected content or write result; persistence is on the referenced objects, not a new implicit store. Later read-back/consumer and selectors are stated above; delegated visibility and actual activation remain uninspected. Scope and budget/cooldown/terminal-state rules delimit eligibility; no content-truth guarantee follows. Recovery is caller retry or the recorded upstream recovery path, not an asserted automatic semantic rollback.

RTE-7 — automatic session-context supply to intent analysis. Implementation conclusion status: wired. Search with an eligible session triggers `get_context_for_search`, which returns newest terminal overview plus up to 20 assembled messages. The intent analyzer is constructed with five recent messages and receives compression_summary and current query. Images/disabled intent/no session instead use raw-query retrieval. Recipient is the internal account query planner; it did not request a particular memory. SRC-1 `openviking/service/search_service.py:122-137`; `openviking/session/session.py:2558-2574`; `openviking/storage/viking_fs/_semantic.py:410-484`.

>             with telemetry.measure("search.intent_analysis"):
>                 query_plan = await analyzer.analyze(
>                     compression_summary=session_summary or "",
>                     messages=current_messages or [],
>                     current_message=query,
>                     target_abstract=target_abstract,
>                 )
>             typed_queries = query_plan.queries
> --- `openviking/storage/viking_fs/_semantic.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

Route audit: immediate return is the selected content or write result; persistence is on the referenced objects, not a new implicit store. Later read-back/consumer and selectors are stated above; delegated visibility and actual activation remain uninspected. Scope and budget/cooldown/terminal-state rules delimit eligibility; no content-truth guarantee follows. Recovery is caller retry or the recorded upstream recovery path, not an asserted automatic semantic rollback.

RTE-8 — bounded user-memory context return. Implementation conclusion status: wired; external consumer status: afforded. The context assembly request expands queries optionally, excludes caller/cooled URIs, gathers candidates by quotas, prefetches bodies only for tiers that need them, budgets entries, renders memory blocks and optionally produces a request-time digest. Served entries update OBJ-7. No durable digest write was found in the inspected pipeline, so digest generation is not counted as trace learning. SRC-1 `openviking/retrieve/context_assembler/pipeline.py:54-208`; SRC-2 `docs/en/api/16-memory.md:30-40`. Plugin execution is excluded.

>     plan = plan_entries(
>         candidates,
>         contents,
>         max_tokens=params.max_tokens,
>         detail=pins,
>     )
> 
>     rendered = render_context(plan.entries) if params.render else ""
> --- `openviking/retrieve/context_assembler/pipeline.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

Route audit: immediate return is the selected content or write result; persistence is on the referenced objects, not a new implicit store. Later read-back/consumer and selectors are stated above; delegated visibility and actual activation remain uninspected. Scope and budget/cooldown/terminal-state rules delimit eligibility; no content-truth guarantee follows. Recovery is caller retry or the recorded upstream recovery path, not an asserted automatic semantic rollback. The request-time digest is not counted as retained trace learning. Recall ledger changes routing; failure degrades to no suppression. No independent answer oracle accepts the digest.

RTE-9 — caller-directed memory content editing. Conclusion status: afforded. The filesystem service write API supports content replacement and refresh; the coordinator dispatches memory files to memory-specific refresh. Memory extraction does not require a human adoption gate. A general snapshot restore facade also exists but this report does not claim it automatically reverses a session memory diff. SRC-1 `openviking/service/fs_service.py:1189-1217,1280-1325`; `openviking/storage/content_write.py:190-191,1334-1410`.


>     ) -> Dict[str, Any]:
>         """Write to an existing file and refresh semantics/vectors."""
>         viking_fs = self._ensure_initialized()
>         coordinator = ContentWriteCoordinator(viking_fs=viking_fs, vikingdb=self._vikingdb)
>         return await coordinator.write(
>             uri=uri,
>             content=content,
>             ctx=ctx,
> --- `openviking/service/fs_service.py` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

Route audit: immediate return is the selected content or write result; persistence is on the referenced objects, not a new implicit store. Later read-back/consumer and selectors are stated above; delegated visibility and actual activation remain uninspected. Scope and budget/cooldown/terminal-state rules delimit eligibility; no content-truth guarantee follows. Recovery is caller retry or the recorded upstream recovery path, not an asserted automatic semantic rollback. External caller proposes replacement; content API admits under its write/refresh rules and can reject write errors. Guidance, rationale, theory criticism and benefit are caller-owned and uninspected; arbitrary edits do not establish learning.

### Claims

CLM-1 — README presents OpenViking as a context database where session commit archives conversation and extracts inspectable/editable memories. Conclusion status: claimed; included RTE-2 and RTE-3 support implementation, not measured benefit. SRC-2, `README.md:41-63`.

> Committing a session archives the conversation and extracts memories as Markdown you can inspect, edit, and merge.
> --- `README.md` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

CLM-2 — README attributes accuracy/task-success improvements to memory-enabled integrations in benchmarks. Conclusion status: claimed. SRC-2, `README.md:110-123`. Benchmark source and candidate-linked executions were excluded, so this analysis neither verifies those comparisons nor attributes an individual component's effect.



### Evidenced absences

None claimed: uninspected capabilities are limitations rather than evidenced absences.

### Behavioral-authority paths

BAP-1 — Memory/context outputs reach requesting clients or internal model prompts. Channel, force and horizon differ by consumer; External agent-context block return is afforded, with advisory knowledge force and horizon the caller's request/continuation; no deployed activation demonstrated. SRC-2, `docs/en/api/16-memory.md`. Internal extractor/query-planner supply is wired through RTE-6 and RTE-7, carrying advisory context; index/URI metadata governs ranking/routing rather than truth.

> Search each memory type independently and assemble a bounded memory block that can be injected directly into Agent context.
> --- `docs/en/api/16-memory.md` @ `4edc30b068934893bc94a4e1b8e87bab2100bce5`

BAP-2 — Checkpoint/recall metadata is consumed by RTE-5 and RTE-8 selectors; routing force determines which retained parts are delivered, horizon current continuation/request and ledger cooldown. Conclusion status: wired. Its operational authority is selection, not epistemic endorsement.

## Runtime account

The ordinary included invocation is an authenticated HTTP client's session message append, followed by explicit or configured automatic commit. The caller chooses content and retention policy; service code resolves identity, locks authoritative session state and returns an archive/task handle after Phase 1. A background queue runs working-summary generation and permitted memory extraction. The extraction VLM may inspect current memory through registered tools before proposing operations; code applies accepted writes, and retrieval later returns selected content. The external agent owns the final task action and whether to use returned evidence.

Material controls are distinct: caller identity/account configuration; policy-governed allowed memory types/peer scope; symbolic persistence/queue transitions; model choices over proposed content; and downstream client use. Source-provided role/plugin hooks do not establish a deployed grant set. Development auth supplies ROOT only under localhost configuration; arbitrary direct Python callers and bot/plugin hosts lie outside the HTTP control claim. No general shell-tool isolation or user approval guarantee is inferred.

Static forcing cases: (1) commit accepted before extraction completes, so a task result must distinguish archive acceptance from derived-memory success; (2) disabled working-memory policy skips continuation generation; (3) transient Phase-2 error follows retry/progress recovery while permanent errors fail rather than manufacture memory; (4) direct `find` skips contextual intent planning, whereas `search` can supply accumulated session context. Optional training/skills are separate excluded branches, not covered by user-memory findings.

No dynamic check planned. Considered running commit/restart fixtures and retrieval integration tests; both require configured storage/model execution to establish operational effects. Static branch inspection is sufficient for stated wired controls and prevents confusing successful source acquisition with a system run. No dependencies, models or credentials were installed/used for behavioral probes.

Operating mode is service use by open client requests and configurable background commits. Proposals come from external message authors and the extraction VLM; configured policies and symbolic operation validation can reject writes. Humans can configure policy and edit stored material, but no human acceptance gate is assumed on automatic extraction. A model's judgment is not an expected-answer oracle. Within this selected route, reference truth for user preferences/events remains source assertion; no external expected-answer test was inspected. Optional agent-training evaluation uses outside this boundary remain uninspected.

## Lens scoping

### Memory/context scope

Full lens triggered by OBJ-1 session traces, OBJ-2 continuation/archives, OBJ-3 user memory and OBJ-4 retrieval metadata. Includes RTE-1, RTE-2, RTE-3 and RTE-4 with included alternatives; excludes optional agent-evolution/training, session-skill extraction, resource/wiki compilation and external host stores. Scope must distinguish raw retention, transformed continuation and cross-session user memory without counting unrelated platform branches.

### Epistemic scope

Full lens on acquisition, summary/extraction transformations, write admission and retrieval authority in the same selected subsystem. CLM-1 establishes memory operation claims; CLM-2 remains reported benchmark prose. Omitted empirical experiments prevent causal/learning-benefit and whole-system knowledge-production conclusions.

## Lens outputs

### Memory/context lens


The fourteen-axis profile uses exactly this subsystem boundary. Known sets distinguish source-native operations from classification: stored prose is knowledge at actual inspected consumption paths; URI/cooldown/checkpoint metadata provides routing, and index/access fields supply ranking. Persona prose is not promoted to binding instruction solely because its file is named `soul.md`. No enforcement/validation authority is assigned to memory from unrelated runtime access controls.

Lineage covers imported raw messages, authored caller edits, trace-extracted summaries/user memories and other-compiled metadata/previews/indexes. Automatic writes dominate extraction; manual refers only to caller-controlled editing. The weakest basis for mixed external affordances is afforded. Raw image and arbitrary tool bytes prevent a complete representational-form union; memory strings and symbolic containers do not determine their payload semantics. Logical files/vector storage are established, but a physical substrate union needs the backend/snapshot inspection that this report did not perform.

Curation maps WM reduction to consolidate; schema-identity merge to dedup; accepted patches to evolve; deletion with retained diff history to invalidate; recency loss and URI cooldown to decay; and configured frequency/recency boost to promote salience. No new-claim synthesis requirement is established by these mechanisms. These are wired capabilities whose semantic success is model-dependent. The ledger's own name “dedup” is not the evidence for the dedup classification. Custom deployments may change policy, so the known operation set describes the inspected shipped paths rather than every possible account template.

Trace learning includes both RTE-2 and RTE-3. Session logs and tool traces describe their union even though ToolPart is excluded from user-memory extraction. Use-time asynchronous commit supports online timing, with output visibility after completion; it is not proof of synchrony. Distilled products combine natural-language bodies and symbolic typed fields/checkpoint bindings. The prompt explicitly asks preferences to generalize across conversations, but arbitrary conversation/turn boundaries do not determine task scope, so learning_scope remains not-determinable. Faithfulness remains uninspected rather than an unsupported negative.


The specialist inventoried raw/tool payloads, cumulative WM, per-turn checkpoints, user-memory records and recall metadata. It identified automatic prefetch and internal planner supply separately from requested external returns. RTE-2 and RTE-3 support trace learning under the write-route definition; RTE-8's transient digest does not. This is not an observed capacity improvement or a claim that generic host memory is in scope.

### Epistemic lens

1. Source-and-claim boundary: SRC-1 and SRC-2, selected session/user-memory routes, CLM-1 and CLM-2. Training, benchmark interventions and external host actions remain excluded. The epistemic question is what the included transformations and admission checks warrant, not whether the platform discovers knowledge overall.

2. Object overlay: OBJ-1 contains acquired assertions and action/tool records; source identity can be retained without certifying truth. OBJ-2 includes raw archive preservation and model-written summaries, whose semantic faithfulness is not guaranteed by successful storage. OBJ-3 contains extracted preferences/entities/events and similar user-memory assertions, with source-specific lineage and scope. OBJ-4 supports access/selection; relevance ranking is not truth acceptance. Generic identity and form remain on the canonical records.

3. Authority-route ledger:

| Route | Function | Architectural status | Object / relation | Target, evaluator, timing and result | Epistemic authority | Operational and behavioral authority | Evidence and limit |
|---|---|---|---|---|---|---|---|
| RTE-1 | content transformation | implemented | OBJ-1; acquisition/import | caller's messages admitted under request/append protocol | imported source assertions only; no independent truth check | enters session state for later processing | SRC-1 session/auth paths; caller-authentication is not content warrant |
| RTE-2 | retention | implemented | raw part of OBJ-2; no content change | lock/archive/queue protocol, on commit; accepted task handle or error | persistence/identity, not truth | publishes raw archive and retained live state | SRC-1 session commit; accepted is not extraction complete |
| RTE-2 | content transformation | implemented | summary part of OBJ-2; indeterminate | VLM guided by summary schema, when working memory enabled | intended compression/continuity; semantic preservation unestablished | model-written continuation becomes available to later consumers | SRC-1 summary branch; output truth/faithfulness not tested here |
| RTE-3 | content transformation | implemented | OBJ-1/OBJ-2 to OBJ-3; indeterminate | extraction VLM under type/prompt guidance; proposed operations | preferences/events may preserve source facts or introduce inference; no blanket entailment | proposes memory edits | SRC-1 compressor and extraction loop; source-assertion errors can propagate |
| RTE-3 | operational admission/selection/consumption | implemented | OBJ-3 update operations; no new epistemic license | policy/target/schema/merge checks before write | structural/identity compatibility at check scope only | admits or skips writes according to code; no human gate presumed | see integrated RTE-3; mutation permission is distinct from truth acceptance |
| RTE-3 | retention | implemented | OBJ-3; no content change after accepted write | filesystem/updater persistence | storage itself grants no further warrant | later retrieval/continuation can consume retained material | see integrated RTE-3 and BAP-1 |
| RTE-4 | operational admission/selection/consumption | implemented | OBJ-2/OBJ-3/OBJ-4; no content change in selection | caller request, URI/filter/rank/context logic; returned matches | relevance/context availability, not evidence of truth | supplies context to internal planner or requesting client | SRC-1 search service and memory overlay; activation/benefit unobserved |

4. Per-object lifecycle disposition: OBJ-1 is acquisition; discovery lifecycle not applicable. Raw OBJ-2 archives preserve inputs; generated OBJ-2 summaries have indeterminate semantic relation (faithful reshaping versus added/dropped meaning), pending candidate-linked comparisons. OBJ-3 similarly combines extracted assertions and model inference; classify it as indeterminate rather than asserting all entries are ampliative discoveries. Its implemented checks/admission establish writable schema/targets, not empirical acceptance of a truth claim. OBJ-4 has no candidate truth-apt output in its access-metadata role; relevant update route RTE-3 and selection route RTE-4. No candidate-linked runtime artifact was inspected, so observed candidate state is no instance observed for produced summaries/memories. Empirical claim test/acceptance/post-acceptance integration architectural status is not determinable inside the selected boundary; retention and pre-acceptance use are not lifecycle integration.

The added route overlay is explicit: RTE-5 and RTE-7 are implemented operational supply of checkpoint/summary context (no new content change); RTE-6 is implemented model-input prefetch plus requested reads (no truth acceptance); RTE-8 is implemented selection/rendering and optional request-time digest (semantic preservation indeterminate), plus independent retention of OBJ-7 routing metadata; RTE-9 is afforded caller editing backed by implemented write/refresh. OBJ-5 is trace-derived checkpoint content with indeterminate preservation; OBJ-6 is retained raw payload and lossy preview, not accepted knowledge; OBJ-7 is symbolic routing history with no candidate truth-apt output. Their observed candidate state remains no instance observed. No stronger warrant or lifecycle integration follows from these added routes.

5. Claim comparison: CLM-1 has wired support for archiving, extraction and retrieval, with no observation of success in this run. CLM-2 is reported benchmark prose only; implementation of memory delivery does not reproduce the benchmark or isolate the effect of one transformation. No causal attribution is accepted from the README alone.

6. Bounded conclusion: this subsystem acquires, transforms, retains and supplies material for later reliance. Symbolic checks constrain operations and identities; model prompts ask for faithful extraction. They do not independently warrant recalled assertions. A memory can be operationally admitted without having passed a content-truth test. The analysis therefore separates a wired memory cycle from observed faithful recall, accepted scientific claims and improved future capacity.

## Reconciliation

Verified the report's complete status, run/source/boundary, input and method hashes, exact report digest and source quotations. Mappings: MEM-OBJ-1 → OBJ-5; MEM-OBJ-2 → OBJ-6; MEM-OBJ-3 → OBJ-7; MEM-RTE-1 → RTE-5; MEM-RTE-2 → RTE-6; MEM-RTE-3 → RTE-7; MEM-RTE-4 → RTE-8; MEM-RTE-5 → RTE-9. These add explicit subobjects/routes without reassigning seeded container IDs.

All seven integration issues are accepted: retain physical-substrate/payload-form/task-horizon/faithfulness uncertainty; distinguish WM tool evidence from the user formatter; do not infer prior-WM consumption from an accepted parameter; distinguish actual read tool availability from generic prompt references to search; prefer pinned implementation over older documentation; treat memory diffs as audit records, not proven rollback; and include bounded recall/context delivery without asserting a durable digest. Requested rationale/identity preservation remains distinct from successful preservation or truth verification. Coordinator mechanically normalized seven over-end citation endpoints against pinned blob line counts; quote bytes, findings, statuses and comparison profile are unchanged. The report hash binds those normalized bytes. No unresolved conflict remains. The specialist pass is not semantic clearance of the full result.

## Bounded synthesis

The included OpenViking subsystem turns session traces into retained continuation and user-memory material, then serves that material to later model/client consumers. Archive acceptance and memory extraction are separate stages, with explicit policy and recovery controls. This is stronger evidence than a storage-only API: selected later-consumer paths are wired. Their actual activation and benefit remain unobserved here.

The strongest supported improvement mechanism is automatic revision of retained context that later consumers can receive. Conjectural learning remains uninspected: no candidate-linked evidence shows criticism of an operative formulated theory improved future action capacity. Reflection also remains uninspected at this subsystem boundary: session traces often describe the excluded client agent, not a demonstrated self-representation of the memory subsystem with a two-way causal path. Self-improvement remains uninspected: automatic context updating is wired, but this source pass establishes neither improved capability nor a revision to the subsystem's own organization. These are independent properties, not a grade.

No platform-wide maturity or epistemic grade follows. Optional agent-evolution/training and skill generation require their own analysis. Candidate-linked downstream runs, replay/restart tests and controlled interventions on recalled content would change the current evidence boundary; a successful queue acknowledgment alone would not.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Evidence needed |
|---|---|---|---|---|
| Static source only | SRC-1, RTE-1, RTE-2, RTE-3, RTE-4 | selected session/user-memory subsystem | deployed reliability, activation, causal benefit | retained executed traces and controlled recall contrasts |
| Optional evolution/training/skills excluded | RTE-3 | user-memory branch only | whole-platform improvement or learned-skill characterization | separately scoped frozen branch analysis |
| Host and provider internals excluded | CMP-2, CMP-3, BAP-1 | service/API boundary | exact model weights, parameter updates, final action controls | deployment identity and provider/host evidence |
| Auth deployment uninspected | RTE-1 | request construction and dev plugin | actual grant set and isolation envelope | configured plugin/transport/storage verification |
| Included storage/payload/task-horizon alternatives unresolved | OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7 | session/user-memory boundary | complete physical substrate, representation or learning-scope sets | backend/payload and task-linked consumer evidence |

## Verification and blockers

### Semantic verification

Checked source pin, declared branch exclusions, HTTP identity vs deployed grants, Phase-1 acceptance vs Phase-2 completion, policy-disabled summaries, recovery/progress semantics and direct/context-aware retrieval alternatives. Verified all fourteen profile axes against scoped objects and route alternatives. Included RTE-2 WM and checkpoint transformations plus RTE-3 user extraction in trace-learning source/timing/form unions; task scope remains not-determinable. RTE-5 anchor and RTE-6 required-URI matching support identifier push, while latest archive/fixed-file supply is coarse; semantic prefetch and optional rerank supply embedding/judgment signals. Requested RTE-4/RTE-8 returns are pull, not duplicated as push. Retained ledger routing is distinct from transient digest generation. Curation claims remain route-specific; no incomplete physical/form set was asserted. Canonical additions preserve seed identities. Source quotations are retained once on supporting records.

### Deterministic validation

Target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-openviking-01/result.md`; `commonplace-validate --full` passed after specialist integration.

### Blockers

none
