---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "OpenViking memory: archive/checkpoint reconstruction, trace-to-file admission, recall bookkeeping and shipped consumer selection at the frozen partial-loop boundary."
run-id: AAS-2026-10-14-openviking-7b5b57541af5-01
source-identity: "https://github.com/volcengine/OpenViking"
reviewed-boundary: "5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b"
---

# OpenViking memory report

## Boundary and evidence

This account covers OpenViking's retained context, transformations and selected later consumers at SRC-1, commit **5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b**. The source declarations are in [boundary](boundary.md#source-register). The boundary remains **complete artifact, partial loop**, not a whole-system lifecycle audit. Source inspection supplies implementation findings; supplied runtime records supply the explicitly identified retrieval and skill/config findings. No target code, tests, examples, models or services were executed. Delivery wiring does not establish activation or benefit.

The memory scope includes session archives, working-memory overviews, cumulative and legacy checkpoints, externalized tool results, ordinary user-memory files, case/trajectory/experience transformations, skills/resources, indexes, recall metadata, exposed editing/deletion and the selected OpenCode/VikingBot consumers. External providers' numerical state and third-party host scheduling remain excluded by the boundary; their behavior prevents claims about model quality, actual injection or learning. Available but uninspected included paths below are not absences or access gaps.

| Entry or operation | SRC-1 path / evidence origin | Coverage and prevented conclusion |
|---|---|---|
| List search, direct find, metadata lookup | Supplied runtime: `openviking/storage/viking_fs/_semantic.py`, `openviking/retrieve/hierarchical_retriever.py` | [RT-RTE-session-search](runtime.md#rt-rte-session-search), [RT-RTE-direct-find](runtime.md#rt-rte-direct-find). Scoped query construction is not deployed isolation or relevant recall. |
| Context-mode search and OpenCode automatic injection | Supplied runtime: `openviking/retrieve/context_assembler/pipeline.py`, `examples/opencode-plugin/lib/memory-recall.mjs` | [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly), [RT-RTE-plugin-recall](runtime.md#rt-rte-plugin-recall). Direct ledger inspection adds [MEM-OBJ-recall-ledger](#mem-obj-recall-ledger). |
| Durable session commit / phase-two work | Supplied runtime plus direct selected ranges: `openviking/session/session.py`, `openviking/session/compressor_v3.py` | [RT-RTE-session-commit](runtime.md#rt-rte-session-commit); [MEM-RTE-session-reconstruction](#mem-rte-session-reconstruction), [MEM-RTE-memory-application](#mem-rte-memory-application). Queue acceptance is not completed extraction. |
| Working-memory and checkpoint reconstruction | Direct: `openviking/session/session.py`, `openviking/session/checkpoints.py` | [MEM-OBJ-archive-overview](#mem-obj-archive-overview), [MEM-OBJ-checkpoint](#mem-obj-checkpoint). Missing overview and failed terminal archives limit continuity. |
| Oversized tool output / explicit reload | Direct: `openviking/session/tool_output_externalizer.py`, `openviking/session/tool_result_store.py` | [MEM-OBJ-tool-result](#mem-obj-tool-result), [MEM-RTE-tool-externalization](#mem-rte-tool-externalization). Payload hydration is wired; exact synopsis semantics, complete public-tool callers and expiration are uninspected. |
| Extraction, merge, rejection, indexing | Direct selected ranges: `openviking/session/memory/streaming_memory_updater.py`, `openviking/session/memory/memory_updater.py`, `openviking/session/memory/utils/memory_file_utils.py` | [MEM-OBJ-memory-file](#mem-obj-memory-file), [MEM-RTE-memory-application](#mem-rte-memory-application). Full merge-model protocol and every schema/output DSL are uninspected; no atomicity claim. |
| Cases, trajectories, experience proposals and persisted policies | Direct selected ranges: `openviking/session/compressor_v3.py`, `openviking/session/train/components/trajectory_analyzer.py`, `openviking/session/train/components/gradient_estimator.py`, `openviking/session/train/components/policy_updater.py`, `openviking/session/memory/experience_lineage.py` | [MEM-RTE-experience-maintenance](#mem-rte-experience-maintenance), separate objects below. Batch-run evaluator, remote rollout, trainer scheduling and snapshot restore are not fully traced; cannot claim uniform training, oracle use or improvement. |
| Manual extraction | Direct: `openviking/service/session_service.py` | Annotation on [RT-RTE-session-commit](runtime.md#rt-rte-session-commit). Uses live messages and `manual_extract`, not the ordinary archive trigger. Policy parity with queued commit is not established. |
| Skill upload and conditional trace-to-skill | Direct selected `openviking/utils/skill_processor.py`; supplied runtime optimizer/updater | Annotation on [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission). Package processing differs from a plain file edit; rollback and complete upload authorization are uninspected. |
| Resource ingestion and watch refresh | Router/entry searches: `openviking/server/routers/resources.py`, `openviking/server/mcp_endpoint.py`; supplied runtime `openviking/service/resource_service.py` | Job and parsing surfaces exist; parsers, privacy transformations, native storage, watcher refresh and alternate processing modes not traced end to end. Prevents uniform provenance/freshness or resource-to-memory admission claims. |
| File authoring/edit and forgetting | Searches: `openviking/server/mcp_endpoint.py`; direct `openviking/service/fs_service.py`, `openviking/storage/viking_fs/_ops.py` | [MEM-RTE-resource-withdrawal](#mem-rte-resource-withdrawal). Caller authorship is distinct from per-content human approval. Full write/index dispatch and management authorization remain uninspected. |
| Resource-linked memory cleanup | Direct: `openviking/service/resource_memory_link_service.py`, `openviking/service/fs_service.py` | [MEM-RTE-resource-withdrawal](#mem-rte-resource-withdrawal). Inspected ordering contradicts the cleanup function's name; low-level rm bypasses service cleanup. |
| Account extraction-template overrides / settings | Direct selected `openviking/session/memory/account_templates.py`; supplied [RT-RTE-config-patch](runtime.md#rt-rte-config-patch) | Managed edits admit top-level description, eligible content-template and selected field-description changes, not changed embedding-template values; override loading is distinct from update admission. Full admin principal controls and initial deployment template authorship unresolved. Prevents blanket human-curated guidance classification. |
| OpenCode trace capture state and compaction boundary | Direct selected `examples/opencode-plugin/lib/memory-session.mjs`; supplied plugin hook record | Local mapping/pending payload persistence inspected. Full event capture, offline queue/retry and imported package equivalence not audited; no lossless capture/recovery conclusion. |
| VikingBot memory and experience read-back | Direct selected `bot/vikingbot/agent/memory.py`, `bot/vikingbot/agent/context.py` | [MEM-RTE-bot-recall](#mem-rte-bot-recall). Bot has character-budgeted formatting and case-link selection, not just server context mode. Local MEMORY.md/HISTORY.md I/O exists; all writers/compaction and bot session commit paths are uninspected. |
| CLI / registered tools / library surfaces | Direct `openviking_cli/rust_cli.py`; searches of `crates/ov_cli/src/commands/session.rs`, `openviking/server/mcp_endpoint.py`, service methods | Python command forwards to Rust; MCP exposes search/read/write/edit/add_resource/add_skill/forget, and service exposes manual extract. Full Rust command dispatch, gateway, other plugins, web studio, SDKs and evaluators remain uninspected. Prevents claiming that the selected consumers exhaust shipped memory routes. |

## Core ideas

1. **One substrate does not imply one authority.** Text bodies can influence model interpretation. MEMORY_FIELDS, checkpoint anchor IDs and recall-ledger turn counters instead drive code-defined operations. Vectors select candidates without carrying the same readable reasons as a file. These parts have different consumers and failure modes: [MEM-OBJ-memory-file](#mem-obj-memory-file), [MEM-OBJ-checkpoint](#mem-obj-checkpoint), [MEM-OBJ-recall-ledger](#mem-obj-recall-ledger).
2. **Compaction has several retained products.** A completed archive overview substitutes for older history; partial-turn checkpoints are inserted after retained user anchors; oversized tool outputs leave a typed display stub with an explicit reload route. Pending raw archives, completed summaries and failed terminal archives are not interchangeable. See [MEM-RTE-session-reconstruction](#mem-rte-session-reconstruction) and [MEM-RTE-tool-externalization](#mem-rte-tool-externalization).
3. **Admission is computational and fallible, not synonymous with truth assessment.** Extraction/merge models propose changes. Resolution and updater rules can reject, skip or preserve fields and suppress unsafe deletes. Successful files can coexist with errors. These checks establish mutation controls, not corroboration of the stored claims: [MEM-RTE-memory-application](#mem-rte-memory-application).
4. **Recall is consumer-specific.** Server context assembly can return a digest or no visible content; the ledger cools only content-bearing served entries. VikingBot routes from a selected case to linked experiences and budgets full text independently. Retrieval presence therefore does not establish complete downstream evidence or instruction compliance: [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly), [MEM-RTE-bot-recall](#mem-rte-bot-recall).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memory-file
Label: Ordinary user MemoryFile

Source-native identity: persisted non-training user-memory MemoryFile, produced from resolved extraction operations. Distinct from raw session messages in [RT-OBJ-session-commit](runtime.md#rt-obj-session-commit); cases, trajectories and experiences below have additional producers/consumers. Storage: VikingFS/AGFS file. Form: natural-language Markdown body interpreted by later models; separate symbolic JSON metadata in a MEMORY_FIELDS HTML comment, including version, trace/extraction identifiers and links. Lineage: session messages → model operations → schema field merge/template rendering → stored file. Initial manual content provenance and complete per-type schemas are unresolved.

SRC-1, `openviking/session/memory/utils/memory_file_utils.py`, `openviking/session/memory/memory_updater.py`:

> """Serialize a MemoryFile as plain-text body plus MEMORY_FIELDS metadata."""
> --- `openviking/session/memory/utils/memory_file_utils.py`

> metadata["version"] = next_memory_version(old_content)
> --- `openviking/session/memory/memory_updater.py`

The updater reads current disk content, falls back to a prefetched snapshot on some in-place read failures, merges schema fields, preserves system metadata, and writes each URI separately. Trace identifiers record lineage, not the model's full justification. Later extraction can edit the file; search can select indexed previews; VikingBot reads bodies. Physical storage is not behavioral authority without those consumer paths.

#### MEM-OBJ-archive-overview
Label: Archive working-memory overview

Part of: [RT-OBJ-session-commit](runtime.md#rt-obj-session-commit)

This is the derived text part, not the raw archive or queue-control markers. Storage: archive `.overview.md`/`.abstract.md` in VikingFS, with overview-token and generation metadata. Form: natural-language summary plus symbolic metadata. Lineage: archived messages, hydrated tool outputs and prior overview → working-memory model create/update → stored overview. Session generation also has batching and fallback branches; their complete semantic fidelity is uninspected. SRC-1, `openviking/session/session.py`.

> uri=f"{archive_uri}/.overview.md",
> --- `openviking/session/session.py`

Later context collection loads the newest completed terminal overview; search planning can consume it, and later working-memory generation receives prior text. No inspected guarantee preserves all reasons or facts. A missing/unreadable overview does not cause replay of all older raw messages in the normal current-format path. See [MEM-RTE-session-reconstruction](#mem-rte-session-reconstruction).

#### MEM-OBJ-checkpoint
Label: Turn checkpoint

Part of: [RT-OBJ-session-commit](runtime.md#rt-obj-session-commit)

Distinct derived part of archive metadata: checkpoint abstract, source-message IDs, user-turn anchor, version and estimated tokens. Form: natural-language abstract plus symbolic mapping. Substrate: archive metadata, later synthesized Message/ContextPart in process. SRC-1, `openviking/session/checkpoints.py`.

> "checkpoint_version": CUMULATIVE_CHECKPOINT_VERSION,
> "turn_anchor_message_id": request.turn_anchor_message_id,
> --- `openviking/session/checkpoints.py`

Model summaries are bound to server-owned anchors and source IDs. Version 2 is cumulative; version 1 deltas trigger older-history compatibility merging. The builder rejects summary-count mismatch and empty summaries, truncates to a local checkpoint budget, and inserts a synthetic assistant checkpoint after its retained user anchor. This is software/model admission, not user authorship; `peer_id=None` is explicit. A later model receives summary text by value, not an automatically dereferenceable archive pointer. The source IDs support provenance, not complete retained reasoning.

#### MEM-OBJ-tool-result
Label: Externalized tool result and display stub

Distinct from the archive/queue container [RT-OBJ-session-commit](runtime.md#rt-obj-session-commit): raw tool output is stored separately under the session's `tool-results`; the message holds a synopsis/ref and integrity/location fields. SRC-1, `openviking/session/tool_result_store.py`, `openviking/session/tool_output_externalizer.py`.

> return f"{self._session_uri}/tool-results"
> --- `openviking/session/tool_result_store.py`

Form: original text can contain natural language, symbolic tool output or opaque encoded payload; display synopsis is readable text, not proof the entire payload is readable prose. Hash, IDs, source offset/limit and MIME type are symbolic metadata. Substrate: VikingFS ToolResultStore plus message fields. Lineage: captured ToolPart output → raw external store and synopsis → reduced session message. Later extraction can hydrate the original or source slice into a memory-only copy; explicit read/search APIs afford reload. Failed externalization may reject or leave a preview without a reference. Those paths have different recoverability; see [MEM-RTE-tool-externalization](#mem-rte-tool-externalization).

#### MEM-OBJ-case
Label: Case memory

Distinct from the raw commit object [RT-OBJ-session-commit](runtime.md#rt-obj-session-commit) and reusable skills in [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission). Cases are user-memory files used as training inputs and retrieval routing entries, not merely logs. Storage: VikingFS memory files and links. Form: readable case content plus symbolic type/name/input fields and links. Lineage: ordinary session extraction emits cases; an alternative first-message training-case protocol can bypass ordinary user extraction. SRC-1, `openviking/session/compressor_v3.py`.

> if fast_path_case is not None:
>     return await self._commit_training_case_fast_path(
> --- `openviking/session/compressor_v3.py`

Consumers: compressor training iterates extracted cases with the session rollout; VikingBot selects a case and follows linked experiences. Full fast-path validation and exact-case matching are uninspected; neither protocol metadata nor a case title proves a human provided a verified task specification.

#### MEM-OBJ-trajectory
Label: Trajectory memory

Distinct derived diagnostic memory beyond [RT-OBJ-session-commit](runtime.md#rt-obj-session-commit), and different from proposed skill patches in [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission). Storage: persisted trajectories MemoryFiles read back by TrajectoryRolloutAnalyzer. Form: natural-language trajectory content with symbolic name/outcome/source archive and retrieval tags. Lineage: rollout messages plus optional evaluation feedback → ExtractLoop operations → MemoryUpdater → reread Trajectory. SRC-1, `openviking/session/train/components/trajectory_analyzer.py`, `openviking/session/memory/experience_lineage.py`.

> evaluation = evaluation or _evaluation_from_trajectories(trajectories)
> --- `openviking/session/train/components/trajectory_analyzer.py`

The fallback evaluation records extraction success rather than proving task success. Later experience estimation receives each trajectory's content and URI. Consumed-experience lineage tags derive from completed read-tool traces filtered for ownership/status; they do not prove the agent followed the experience. Actual diagnostic blame/rationale and semantic accuracy are unobserved.

#### MEM-OBJ-experience
Label: Experience memory policy

Distinct from case routing, trajectory diagnostics and the skills route [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission). Source-native identity: ExperienceSet policies persisted as memory files by MemoryFilePolicyUpdater. Form: natural-language reusable content plus symbolic name/version/link fields. Substrate: VikingFS, process-local policy snapshots and optional snapshot commits. Lineage: trajectory → model-proposed experience operations → semantic gradients → optimizer plan → updater → retained files; case-to-output and experience-to-trajectory links can preserve provenance. SRC-1, `openviking/session/train/components/gradient_estimator.py`, `openviking/session/train/components/policy_updater.py`, `openviking/session/compressor_v3.py`.

> trajectory_summary=trajectory.content,
> trajectory_uri=trajectory.uri,
> --- `openviking/session/train/components/gradient_estimator.py:121-122`

Consumers: subsequent training uses the policy set, and VikingBot's reminder can load linked experience bodies. Full internal model rationale need not persist with the result. Relations identify source material; whether later foreground recall reads diagnostic reasons is separate and uninspected. Source-native “gradient”/“policy” terminology here denotes text operations, not weight training or a demonstrated explanatory theory.

#### MEM-OBJ-memory-index
Label: Memory index representation

Distinct from model component [RT-CMP-account-embedder](runtime.md#rt-cmp-account-embedder) and stored MemoryFile bodies. The index holds numerical embeddings plus symbolic URI/type/tags and readable abstract. Substrate: configured vector backend; queued embedding messages mediate updates. SRC-1, `openviking/session/memory/memory_updater.py`; retrieval consumer supplied by [RT-RTE-session-search](runtime.md#rt-rte-session-search).

> abstract = LinkRenderer.strip_all_links(mf.content or "")
> abstract = self._truncate_memory_abstract(abstract)
> embedding_text = abstract
> --- `openviking/session/memory/memory_updater.py`

Lineage: successful written/edited file → body reread → links stripped and abstract truncated → optional schema embedding-template text → queued embedding. Missing variables/render errors fall back to plain content; missing VikingDB skips vectorization. Numerical vectors select candidates; readable abstracts support rerank/display; neither is the whole retained body or rationale. Exact embedder provenance, backend consistency and completion timing remain bounded by runtime/provider limits. Consuming a schema embedding template does not establish an account editing capability: the managed update path rejects embedding-template changes relative to deployment defaults (SRC-1, `openviking/session/memory/account_templates.py`; Write side below).

#### MEM-OBJ-recall-ledger
Label: RecallLedger

Distinct from retained knowledge; closest route is [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly). Storage: session `.recall_log.json` via raw VikingFS file I/O. Form: symbolic URI → served turn/detail, with version and updated-turn fields. Lineage: context assembly's served entries → ledger record → later invocation's cooled URI set. Consumer: code excludes recently served content from gather. SRC-1, `openviking/retrieve/context_assembler/ledger.py`.

> if record.get("detail") == "uri":
> --- `openviking/retrieve/context_assembler/ledger.py`

Bare-URI entries do not cool; malformed/ahead-of-clock records are ignored. Record prunes to a four-times-dedup-turn horizon and at most 500 URIs. Load failures start empty; write failures do not fail recall. This is retained access metadata with selector authority, not a learned fact, semantic curation or proof that a host consumed every entry.

### Routes

#### MEM-RTE-memory-application
Label: Resolved memory application

Distinct continuation beyond the submission endpoint of [RT-RTE-session-commit](runtime.md#rt-rte-session-commit); also used by trajectory/policy updates, so not exclusively a part of that route. SRC-1, `openviking/session/memory/streaming_memory_updater.py`, `openviking/session/memory/memory_updater.py`. Owner: streaming updater batches/merges where selected; MemoryUpdater resolves application effects, schema merge operators and VikingFS writes/deletes. Context: RequestContext, registry, prior file, extraction context and operation lineage.

- Immediate return: submitter-scoped operations/apply result with written, edited, deleted, skipped and error outcomes; not a blanket successful transaction.
- Later read-back: persisted files and index previews reach later extraction, search and bot consumers; updater rereads existing bodies before subsequent patches.
- Delegated visibility: merge/extraction models see provider-selected context; updater receives resolved fields, not a guaranteed complete deliberation history; later readers can receive only abstract/digest.
- Selection predicate: append-only split versus grouped merge, resolved URIs, schema fields and merge operators, migration checks, upsert/delete conflicts and link validity.
- Invalidation or expiry: explicit edits/deletes and URI migration replace/remove material; successful writes trigger indexing and overview work, whose full completion consistency is uninspected.
- Activation or effect: persisted mutation and indexing submission are source-wired; changed foreground behavior remains unobserved.
- Evidence limits: selected apply/submit ranges, not all merge providers, isolation rules or JSON/Python output protocols; no concurrent/crash experiment or all-or-nothing guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: model proposals and code checks decide, with callers initiating/configuring the workflow. Per-item human approval is not established. Invalid operation errors/migrations can reject early; unresolved upserts suppress deletion; failed replacement or link migration prevents removal of a source. Field-level merge exceptions preserve the old field while processing continues. No inspected answer oracle establishes truth; mode is open trace-fed maintenance, not a controlled improvement experiment. Guidance persists in schema/templates and account settings; file results retain trace identifiers but not necessarily proposal reasons.

> if operations.has_errors():
>     for error in operations.errors:
>         result.add_error("unknown", ValueError(error))
>     return result
> --- `openviking/session/memory/memory_updater.py`

> "Skipped delete because batch contains unresolved upsert URIs"
> --- `openviking/session/memory/memory_updater.py`

A counterexample to universal model merging is append-only immediate application. A counterexample to atomic acceptance is per-upsert exception handling followed by further operations. Lock names and a successful return do not establish physical rollback.

#### MEM-RTE-session-reconstruction
Label: Session history reconstruction

Part of: [RT-RTE-session-commit](runtime.md#rt-rte-session-commit)

This route isolates the later session-context consumption branch of commit products, rather than redeclaring archive/enqueue. Owner: Session, ArchiveStore and CheckpointPlanner. SRC-1, `openviking/session/session.py`, `openviking/session/checkpoints.py`. Trigger: later session context or search-context request. State: raw archives/live messages, terminal markers, overview and checkpoints.

- Immediate return: budgeted message dictionaries and optional latest overview for session context; search context instead returns overview plus recent messages.
- Later read-back: completed derived overview/checkpoints and pending raw messages are selected for a later invocation; search planning consumes the selected search context.
- Delegated visibility: older raw history normally stays out; foreground receives copied summaries/messages, while explicit archive access remains a separate API capability.
- Selection predicate: newest-to-oldest first terminal marker; newer pending messages plus live messages, stable deduplication and terminal checkpoint anchors; session token budget prioritizes active messages before overview, while search selects a recent-message slice.
- Invalidation or expiry: failed terminal stops older replay without supplying overview; current-format completed archive is a boundary even if required overview is unreadable; reset-context archives alter the boundary. Legacy checkpoint reconstruction has a separate older-history path.
- Activation or effect: context assembly and search delivery are wired; faithful continuity and model behavior are unobserved.
- Evidence limits: no run validates token estimates, summary fidelity or recovery; full archive-store compatibility/retention planner internals are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> del query  # Current query no longer affects historical archive selection.
> --- `openviking/session/session.py`

> latest_archive and latest_archive["overview_tokens"] <= remaining_budget
> --- `openviking/session/session.py`

Summary/checkpoint production is model-authored under working-memory prompts and code-controlled admission. Checkpoint count/empty checks and local truncation can reject/degrade output. Neither retained anchor ownership nor initiating commit constitutes human approval. There is no inspected expected-answer oracle for semantic preservation. Mode: trace-fed context maintenance. Raw-to-derived-to-consumer chains are explicit; summaries may omit reasons. This resembles eviction plus reload, not a stack frame with automatic pointer dereferencing: returns are text by value and a URI requires a deliberate read.

#### MEM-RTE-tool-externalization
Label: Tool output externalization

Distinct from archive splitting in [RT-RTE-session-commit](runtime.md#rt-rte-session-commit): externalization also occurs when message groups are admitted. Owner: ToolOutputExternalizer/ToolResultStore. SRC-1, `openviking/session/tool_output_externalizer.py`, `openviking/session/tool_result_store.py`, `openviking/session/session.py`. Trigger: configured oversized/group-budget handling; code decides which captured ToolParts remain inline versus externally stored.

- Immediate return: message output becomes synopsis/ref/integrity metadata after raw-store write; failure mode can reject or emit a preview without a ref.
- Later read-back: phase-two extraction hydrates a sanitized memory-only copy from stored raw payload or source slice; explicit read/search/list APIs afford later targeted reload.
- Delegated visibility: ordinary message context retains synopsis rather than complete raw output; extraction can receive restored content, with inline image redaction.
- Selection predicate: configuration thresholds/group budget and ToolPart fields; hydration requires a ref and truncated/source-ref flag, with source offset/limit when applicable.
- Invalidation or expiry: uninspected — complete tool-result retention/expiration and deleting-session cleanup are not traced.
- Activation or effect: storage, substitution and phase-two hydration are wired; host interpretation of a stub or optional public reload is unobserved.
- Evidence limits: exact synopsis extraction and all public tool callers not traced; a preview-only failed write has no established full reload route.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> hydrated = [Message.from_dict(m.to_dict()) for m in messages]
> --- `openviking/session/tool_output_externalizer.py`

> if cfg.failure_mode == "reject":
>     raise FailedPreconditionError(
> --- `openviking/session/tool_output_externalizer.py`

Admission is code-controlled physical offload, not truth evaluation or a per-output human choice. Trace origin is captured tools, whose underlying provenance may be opaque or mixed. A read-back of an existing source is rewritten as a source reference rather than retained as a new independent result. Failed hydration logs and leaves the reduced output; therefore presence of a ref does not guarantee complete extraction inputs. The isolated copy protects the stored/session representation from hydration mutation; it is not a separate autonomous agent frame.

#### MEM-RTE-experience-maintenance
Label: Trace to experience maintenance

Distinct from ordinary user-memory submission [RT-RTE-session-commit](runtime.md#rt-rte-session-commit), overlapping the co-extracted skill branch [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) but retaining different artifacts/updater. Owner: compressor, trajectory analyzer, experience estimator, trainer/optimizer and MemoryFilePolicyUpdater. SRC-1, `openviking/session/compressor_v3.py`, `openviking/session/train/components/trajectory_analyzer.py`, `openviking/session/train/components/gradient_estimator.py`, `openviking/session/train/components/policy_updater.py`.

- Immediate return: analysis/gradient/training/apply outcomes, changed URIs and memory diffs; trajectory-only results can exist without experience gradients.
- Later read-back: trajectories are reread into estimation; retained experience policies enter later training; linked experiences can reach VikingBot reminders through cases.
- Delegated visibility: estimator gets trajectory summary/URI plus selected context; admitted files/links are distinct from internal optimizer messages and raw session transcript.
- Selection predicate: agent-evolution flag, allowed cases/trajectories/experiences types, available gradients, optimizer plan and updater checks; first-message training-case fast path is an alternate producer.
- Invalidation or expiry: executable upsert/delete plans can replace or withdraw experience files; errors preserve prior returned policy snapshot but do not demonstrate rollback of successful persisted effects.
- Activation or effect: trace-fed derived-file production and later selection wiring exist; improved task capacity and actual subsequent use of a particular changed file remain unobserved.
- Evidence limits: trainer scheduling, policy optimizer internals and evaluator contracts only partially covered here; no actual theory candidate, outcome trace or causal comparison supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if experiences_allowed:
>     exp_gradients = await ExperienceGradientEstimator(
> --- `openviking/session/compressor_v3.py`

> updated_policy_set=updated_policy_set if not errors else policy_set,
> --- `openviking/session/train/components/policy_updater.py`

Admission: models propose diagnostic/experience edits, optimizer maps proposals to plans, updater applies through MemoryUpdater. Software can reject erroneous operations; generic caller identity leaves human authorship/approval unresolved. An alternative DryRunPolicyUpdater simulates a snapshot without file writes, so policy-update terminology alone does not establish persistence. Evaluation may be supplied on rollout, delegated to an injected evaluator, or fall back to trajectory-extracted status; an expected-answer oracle and its provider/use are **uninspected**. Mode: open session-trace maintenance in this compressor path; batch-training mode is included but incompletely inspected.

Provenance links and source-archive fields retain input relationships; actual criticism/blame and its later reader are uninspected. Theory-builder conditions 1–4: each condition's conclusion status is uninspected because no actual formulated theory/criticism or criticism-shaped next round is supplied; source plumbing alone does not settle them. Addressability: text fields/files are editable; theory parts unresolved. Persistence: files and policy snapshots can cross sessions. Learning: uninspected — no evidence of improved future capacity or attribution. Reflection, reflective theory builder, autonomous theory builder and exercised self-improvement each remain uninspected; none is inferred absent from the lack of run evidence.

#### MEM-RTE-resource-withdrawal
Label: Resource and memory withdrawal

No supplied route covers this lifecycle; closest comparison is update/delete capability within [RT-RTE-session-commit](runtime.md#rt-rte-session-commit). Owner: FSService, VikingFS and optional ResourceMemoryLinkService. SRC-1, `openviking/service/fs_service.py`, `openviking/storage/viking_fs/_ops.py`, `openviking/service/resource_memory_link_service.py`; exposed MCP forgetting in `openviking/server/mcp_endpoint.py`.

- Immediate return: deletion estimate plus service freshness/cleanup outcomes, or exception; estimate is not a verified count of all retained derivatives.
- Later read-back: index removal affects retrieval; retained referencing memories can be model-updated through a deletion event and directly unlinked, with overview refresh for later readers.
- Delegated visibility: deletion bridge receives matched memory URIs/event; direct unlink edits references, not guaranteed every claim originally derived from a resource.
- Selection predicate: URI/type, recursive scope, write/manage checks and locks; service discovers referencing memories, runs optional bridge commit then rescans and cleans remaining matches.
- Invalidation or expiry: vector records are removed before underlying filesystem deletion; service then updates watches/parent freshness and linked memories. Low-level rm bypasses service-level memory cleanup.
- Activation or effect: explicit withdrawal and service cleanup are source-wired; universal removal from all downstream knowledge/host windows is not established.
- Evidence limits: no atomic failure/recovery experiment, exhaustive backlink completeness or already-injected content revocation; full reference discovery and derived-claim provenance remain uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> result = await viking_fs.rm(uri, recursive=recursive, ctx=ctx)
> --- `openviking/service/fs_service.py`

> cleanup_result = await self._resource_memory_link_service.before_resource_delete(
> --- `openviking/service/fs_service.py`

Despite the function name and error message, cleanup is called **after** physical resource deletion in this service path. Cleanup exceptions therefore cannot establish that the resource remains undeleted. The bridge catches commit failure, then attempts direct unlink and verifies residual references; direct raw writes here have different index-refresh handling from MemoryUpdater. Full semantic-index propagation after unlink is uninspected.

Caller chooses withdrawal; software checks scope/permission/lock and computes downstream cleanup; model may propose mutable-memory changes. Human confirmation is requested in the MCP forget description, not an inspected enforced approval step. No answer oracle evaluates truth of surviving memories. Mode: explicit administrative change plus event-fed maintenance. Recovery/rollback of removed resource and partially changed linked files is not established. The admitted result is removal/reference revision, not proof all derived knowledge was invalidated.

#### MEM-RTE-bot-recall
Label: VikingBot retained context delivery

Distinct shipped consumer from [RT-RTE-plugin-recall](runtime.md#rt-rte-plugin-recall); shares server read/search capabilities but performs its own selection and formatting. Owner: MemoryStore and ContextBuilder. SRC-1, `bot/vikingbot/agent/memory.py`, `bot/vikingbot/agent/context.py`. Trigger: building messages for a current user query; flags/session/config determine profile, user-memory and experience paths.

- Immediate return: model-input message list with system context, optional history, optional Experience Reminder, user-memory block and current message.
- Later read-back: query-selected stored user memories/profiles and case-linked experiences enter later bot invocations; local long-term-file read capability also exists but its complete current consumer loop is uninspected.
- Delegated visibility: user-memory formatting can retain full/summary/URI tiers; experience formatting uses full-content attempts without URI-only fallback. Cases route to experiences rather than being injected in that reminder.
- Selection predicate: query/identity/peer scopes, per-type quotas or alternate search, scores and character budgets; experience lookup may be explicit case lookup or top-one case search, linked experience dedup and excluded URIs.
- Invalidation or expiry: recalled-experience exclusions suppress repeated URIs; store edits/deletes affect later reads, but already-delivered text is not automatically revoked.
- Activation or effect: messages.append delivery is wired; actual model invocation compliance/use and improvement remain unobserved.
- Evidence limits: complete exact-case matching, profile/skill loading, bot write/compaction loop and deployment permissions not audited; returned recalled URI set need not equal bodies fitting the budget.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> top_case = cases[:1]
> linked_experiences = await self._linked_experiences_from_cases(
>     top_case,
>     client,
>     limit=0,
> )
> --- `bot/vikingbot/agent/memory.py`

> "content": f"[Experience Reminder]\n## Relevant Agent Experience\n{exp_content}",
> --- `bot/vikingbot/agent/context.py`

Formatting/delivery is not candidate admission. Code selects by relevance/linkage/budget; models interpret reminder content without hard compliance. Source-native local MEMORY.md/HISTORY.md are separate persistent text files with write/append methods; method presence alone does not establish which trace-fed author supplies them or how their contents reenter this bot's current model loop.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-ledger-selection
Label: Recall ledger to exclusion

Distinct from [RT-BAP-recall-context](runtime.md#rt-bap-recall-context): consumer is server context gather, not the host model. Channel: symbolic cooled-URI set derived from retained turn/detail metadata. Force: code-defined candidate exclusion, except URI-only/expired/malformed records; horizon: later session recall within configured dedup distance. SRC-1, `openviking/retrieve/context_assembler/ledger.py`, supported gather wiring [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly). Best-effort metadata persistence is not a knowledge correctness gate.

#### MEM-BAP-experience-reminder
Label: Experience content to bot input

Distinct shipped consumer from [RT-BAP-recall-context](runtime.md#rt-bap-recall-context). Consumer: bot's assembled messages and conditionally its model. Channel: user-role Experience Reminder containing selected retained natural-language experience bodies. Force: model-interpreted guidance, not executable permission or invariant compliance. Horizon: current invocation with later recall possible. Evidence: [MEM-RTE-bot-recall](#mem-rte-bot-recall), SRC-1, `bot/vikingbot/agent/context.py`. Wiring exists; activation and benefit are unobserved.

## Annotations

#### On [RT-OBJ-session-commit](runtime.md#rt-obj-session-commit)

Raw messages, derived summaries/checkpoints and queue/terminal metadata have different consumers. Raw archived messages are trace input to extraction; terminal markers determine eligibility and recovery, while derived text supplies later model context. Externalized tool output can be rehydrated only for extraction without replacing the session's stored stub. Direct evidence: SRC-1, `openviking/session/session.py`, `openviking/session/tool_output_externalizer.py`; operative parts [MEM-OBJ-archive-overview](#mem-obj-archive-overview), [MEM-OBJ-checkpoint](#mem-obj-checkpoint), [MEM-OBJ-tool-result](#mem-obj-tool-result).

#### On [RT-RTE-session-commit](runtime.md#rt-rte-session-commit)

Memory application is a continuation, not a guaranteed all-or-nothing admission. Caller initiation differs from computational per-item authorship/checks. Alternative service extraction uses `session.messages` and a `manual_extract` location rather than queued archive messages (SRC-1, `openviking/service/session_service.py`):

> archive_uri = f"{session.uri}/manual_extract"
> --- `openviking/service/session_service.py`

This affords/directly wires another acquisition route to the same compressor. Full equivalence of commit's policy scope, readiness checks and working-memory generation is not established for it. Its service annotation is not a second declaration of the commit referent.

#### On [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly)

RecallLedger persistence/expiry is now directly inspected rather than unresolved: session raw JSON, turn/detail-based selection, up to 500 recent URI records, pruning horizon and nonfatal failure. See [MEM-OBJ-recall-ledger](#mem-obj-recall-ledger), SRC-1, `openviking/retrieve/context_assembler/ledger.py`. This narrows only the ledger uncertainty, not every backend/host recall lifetime. Budget/rewrite selection can remove content while leaving stored sources reachable by deliberate reads. Digest preference and no_relevant omission remain as supplied.

#### On [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission)

The inspected package processor computes the skill abstract from header metadata, writes content/auxiliary files/source metadata and hands the package lock to queued semantic processing. SRC-1, `openviking/utils/skill_processor.py`:

> lease = None  # The semantic worker owns the handed-off lease.
> --- `openviking/utils/skill_processor.py`

Manual add_skill and trace-generated skills share package processing capacity but differ in authorship/admission. Search buckets and remote skill summaries do not establish that a new skill's full instructions were invoked. MCP documentation directs callers away from plain writes inside managed skill packages (SRC-1, `openviking/server/mcp_endpoint.py`); all actual enforcement points and rollback remain uninspected. The package's readable instructions and auxiliary opaque/code payloads must not be collapsed into a single prose-memory claim.

#### On [RT-RTE-plugin-recall](runtime.md#rt-rte-plugin-recall)

OpenCode's local session map persists pending captured payloads but stores completed-message metadata without parts; later startup deserializes version-2 state. This is capture/retry bookkeeping, distinct from server knowledge. SRC-1, `examples/opencode-plugin/lib/memory-session.mjs`:

> parts: message.captured ? [] : Array.from(message.parts.entries()),
> --- `examples/opencode-plugin/lib/memory-session.mjs`

Idle flush does not always commit; compaction and explicit boundaries can request commit. Full event/queue equivalence remains unresolved, and host compaction is externally scheduled. The retained mapping enables later session association; it is not itself model-visible instruction memory.

## Write side

**Acquisition and authorship.** Raw session traces are captured messages/tool outputs. User ownership is not equivalent to user authorship, verified source trust or human approval. Automatic summary/checkpoint/extraction and experience maintenance use code-selected model context; results can outlive their producing invocation. Explicit MCP file write/edit, resource upload and skill install accept caller content, whose human versus computational authorship is unresolved. Resource parsing, privacy and all alternate admission controls remain the named limits in the coverage inventory.

**Guidance control.** Static schemas/prompts are shipped method text, not accumulated read-back. The managed account-template update path permits top-level description, eligible content-template and selected existing-field description changes. It does **not** admit changed embedding-template values: `update_account_memory_template` completes supplied values from deployment defaults and rejects changes to locked fields. SRC-1, `openviking/session/memory/account_templates.py`:

> editable = {"description"}
> if memory_type in _EDITABLE_CONTENT_TEMPLATES:
>     editable.add("content_template")
> --- `openviking/session/memory/account_templates.py`

> elif type(value) is not type(target[key]) or value != target[key]:
>     # Unchanged locked values are accepted so GET effective -> PUT works.
>     raise ValueError(f"{location} is locked and must match the default template")
> --- `openviking/session/memory/account_templates.py`

The update function validates/completes, limits overrides to 1 MiB, stages under a lock, and resets unchanged-default forms by removing the override. The managed PUT delegates to that function and is decorated `require_auth_root_or_admin` (SRC-1, `openviking/server/routers/admin.py`); full principal enforcement and human versus computational authorship/approval remain unresolved. Initial deployment-template authorship is also unresolved.

Later registry resolution loads persisted account overrides, including well-formed older configurations. This loader can consume persisted embedding-template values, but loading is not permission to edit them through the managed update path. SRC-1, `openviking/session/memory/account_templates.py`:

> templates = await asyncio.gather(
>     *(read_account_memory_template(viking_fs, account_id, s.memory_type) for s in schemas)
> )
> --- `openviking/session/memory/account_templates.py`

This is a separate symbolic/template admission surface from inferred memory. The index consumer in [MEM-OBJ-memory-index](#mem-obj-memory-index) can use schema embedding guidance; no distinct account embedding-template editing path is established here. Model/resource settings remain the separate mechanism [RT-RTE-config-patch](runtime.md#rt-rte-config-patch), not an embedding-template edit or evidence of model weight mutation.

**Transformation and retention.** Raw archive → overview/checkpoint → later session/search context, raw tool result → stub → extraction-only hydration, and case/rollout → trajectory → experience → bot reminder are separate chains. Ordinary file application also creates index abstracts/template text, not necessarily embeddings of full file reasoning. Computational curation is wired, but truth corroboration and improved capacity remain unestablished. Trace/source IDs and links retain provenance; full extraction deliberations and justification for each adopted claim are not guaranteed retained or read by later consumers.

**Rejection and withdrawal.** Updater errors/skip codes, field preservation and replacement-delete guards are not universal atomic rollback. Resource withdrawal reaches indexes and some linked memory; service cleanup ordering and low-level bypass prevent a guarantee that no derivative survives deletion. Neither ledger cooling nor no_relevant rewrite deletes knowledge. Model context can omit a source while storage remains intact. See [MEM-RTE-memory-application](#mem-rte-memory-application), [MEM-RTE-resource-withdrawal](#mem-rte-resource-withdrawal).

## Read-back

- **Requested database context:** callers request list/context search or find; embedder/planner/reranker and code filters select retained parts; bodies or digest may be returned. Request direction remains caller-driven even when an enclosing plugin automatically issues it. Selection budgets and no_relevant omission are supplied in [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly).
- **Automatic OpenCode delivery:** a host chat hook requests recall then injects selected digest/rendered text as a synthetic part, under client guards. This is automatic model-context supply conditional on hook scheduling, not universal unsolicited recall. Session map and raw capture bookkeeping are distinct from the injected material.
- **Session reconstruction:** later context requests select terminal overview, pending/live raw messages and anchor checkpoints; active-message budget may prevent overview inclusion. Search-context history selection ignores query, unlike semantic store recall. Older retained raw archives stay addressable through explicit APIs but are not automatically replayed.
- **VikingBot delivery:** profile/user-memory formatting and case-linked Experience Reminder have independent flags, quotas and character budgets. Case selection is an intermediate routing operation; only selected experience bodies reach that reminder. Returning an experience URI in tracking metadata is not proof its full content fitted.
- **Updater consumption:** prior retained memory/policy text affects merge/extraction, then the derived output can affect later foreground recall. This trace-fed revision authority is distinct from demonstrated learning. Static shipped prompts and uncalled storage APIs are not themselves read-back routes.

## Integration issues

1. **Ledger uncertainty narrowed.** [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly) leaves durability/expiry internals uninspected. [MEM-OBJ-recall-ledger](#mem-obj-recall-ledger) now supplies direct implementation evidence for file persistence, expiry/pruning, URI-only exemption and failure fallback. This is an annotation/additional part, not a duplicate route or operational guarantee.
2. **Container parts, not duplicate archives.** [MEM-OBJ-archive-overview](#mem-obj-archive-overview) and [MEM-OBJ-checkpoint](#mem-obj-checkpoint) are parts of [RT-OBJ-session-commit](runtime.md#rt-obj-session-commit); [MEM-RTE-session-reconstruction](#mem-rte-session-reconstruction) is the later-consumer branch of [RT-RTE-session-commit](runtime.md#rt-rte-session-commit). Keep raw trace, derived text and code-control metadata separate without superseding the valid container.
3. **Adjacent updater route.** [MEM-RTE-memory-application](#mem-rte-memory-application) continues the runtime commit submission but also serves other producers; [MEM-RTE-experience-maintenance](#mem-rte-experience-maintenance) shares trace/model processing with [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) while writing different products. No identical referent was found. Full optimizer, schema isolation/output protocol and batch/evaluator contracts remain unresolved; prevents uniform admission or oracle/theory/improvement claims.
4. **Withdrawal ordering and bypass.** [MEM-RTE-resource-withdrawal](#mem-rte-resource-withdrawal) finds service cleanup after low-level removal, despite `before_resource_delete` naming. Direct lower-level rm skips that service cleanup. The supplied runtime does not assert the opposite; this resolves a previously untraced included maintenance mechanism, not a correction to a supplied positive. Exact reference discovery and unlink-index propagation remain unresolved; prevents universal revocation/freshness claims.
5. **Alternative admission/read-back paths remain bounded.** Manual extraction, first-message training-case fast path, templates, package installs, plain writes, watcher updates, snapshot restore, bot local files and other plugins/CLI/gateway/evaluators are included with the local uncertainties listed in coverage. No implicit equivalence with the ordinary commit/search path. Their remaining producer/control/consumer details prevent a whole-system guarantee.
6. **Account-template admission corrected.** The managed path admits description/eligible content-template and selected field-description edits, but locks embedding-template values against deployment defaults (SRC-1, `openviking/session/memory/account_templates.py`, `openviking/server/routers/admin.py`). Persisted-template consumption, including older configurations, does not establish update admission. This corrects the prior Write side claim and qualifies [MEM-OBJ-memory-index](#mem-obj-memory-index); it remains distinct from [RT-RTE-config-patch](runtime.md#rt-rte-config-patch). No alternate embedding-template editing path is established.
7. **Rationale and consumer visibility.** [MEM-OBJ-trajectory](#mem-obj-trajectory), [MEM-OBJ-experience](#mem-obj-experience), [MEM-OBJ-memory-index](#mem-obj-memory-index) preserve different text/metadata/lineage parts. Actual candidate reasoning, content-directed criticism and downstream use of those reasons are uninspected. Source-native policy/gradient labels cannot settle the epistemic analysis.

## Limitations and checks

HEAD was rechecked against the boundary pin; the frozen source checkout reported no changes. The invocation, supplied types, collection contract, worker rules and complete shared-record contract were read; the runtime input was read in supplied bounded ranges. New source inspection remains SRC-1 implementation, not new evidence identity. No prohibited prior analyses, peer run-state files or target execution were used.

Correction-round source reads rechecked managed PUT delegation, default completion, editable/locked fields, publication and registry loading in SRC-1, `openviking/server/routers/admin.py` and `openviking/session/memory/account_templates.py`. The remaining source findings are carried from the supplied previous report, not newly re-audited.

Coverage is selected source inspection, not an exhaustive audit. Producer triggers and provenance around server auto-commit and resource-addition-to-session processing remain incomplete; this report does not establish that resource-derived memory enters only through captured user conversations, equivalence of all producer policies, or a complete producer/admission comparison. Available native storage, full Rust CLI dispatch, gateway, alternative host plugins, evaluator/training implementations, resource parsing/privacy/watchers and bot write/compaction loops remain uninspected or partial as specified. This prevents claims of universal retention, atomic admission, lossless capture, uniform permissions, complete rationale, actual host compliance and efficacy. Partial knowledge is not an absence finding.

Deterministic validation: the invocation-specific validate-output check passed after authoring. It checks structure, identity, relations and quote occurrence; it does not establish analytical correctness, deployed operation or acceptance.
