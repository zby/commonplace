---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Citadel memory: revisioned source bytes, searchable projections, private session notes, volunteered traces and bounded context delivery."
run-id: AAS-2026-11-09-citadel-de4383eefa4e-01
source-identity: https://github.com/masumi-network/citadel
reviewed-boundary: "749a24014a6cef59499dbe13b6fb4c348f8044a4"
---

# Citadel memory report

## Boundary and evidence

Citadel retains engineering material for later people and agent invocations. This account includes source admission, lifecycle and legacy retention, personal notes, shared traces, promotion, enrichment, optimization notes, feedback, vault revisions, source synchronization and retrieval consumers. The enclosing coding agent's own transcript storage, compaction and decision loop are not Citadel mechanisms. Provider internals and actual private corpora were not captured; this prevents conclusions about complete graph contents, exercised memory use or improvement. The functional boundary and sole source declaration remain [boundary](boundary.md).

All direct source findings below use SRC-1 at the frozen commit. HEAD was independently checked as `749a24014a6cef59499dbe13b6fb4c348f8044a4`. Direct reads add implementation coverage at the paths below; inline prompts and tool instructions supply doctrine/design evidence. No target code, tests, providers or services were executed. Supplied runtime findings are identified separately rather than represented as fresh inspection.

| Entry or operation | Source path and inspection basis | Covering records or unresolved fact and prevented conclusion |
|---|---|---|
| CLI dispatch, local calls, MCP inventory | Direct function/dispatch inventory in `kb/cli.py`; direct MCP share/document and tool inventory in `kb/mcp_server.py`; supplied runtime for ordinary ingest/search/local handlers | [RT-RTE-local-access](runtime.md#rt-rte-local-access), [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission), [MEM-RTE-document-drilldown](#mem-rte-document-drilldown), [MEM-RTE-share-session](#mem-rte-share-session). Inventory also exposes verify, prepare-pr, learning-agent, backup and reconciliation operations; those are not all aliases of search. |
| SessionEnd and task injection hooks | Direct `kb/hooks/sync_session.py`, `kb/session_trace_distill.py`; supplied runtime for `kb/hooks/search_inject.py` | [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-task-search](runtime.md#rt-rte-task-search), [MEM-OBJ-node-note](#mem-obj-node-note). Git-push/root capture internals in `kb/capture.py` remain partially uninspected; no claim that their content selection matches transcript selection. |
| Source retention, current heads and lexical fallback | Direct schema, tombstone/read/search passages in `kb/lifecycle.py`; direct document assembly in `kb/service.py`; supplied runtime for admission and worker | [MEM-OBJ-source-revisions](#mem-obj-source-revisions), [MEM-OBJ-projection-receipts](#mem-obj-projection-receipts), [RT-RTE-source-projection](runtime.md#rt-rte-source-projection) |
| Vector, graph and legacy stores | Direct adapter/provider inventory and improve forwarding in `kb/cognee_client.py`; supplied runtime projection/retrieval | [MEM-OBJ-search-projections](#mem-obj-search-projections). Full graph extraction, global-context-index and Cognee improve semantics are opaque here; provider configuration is not a corpus dump. |
| Optional write-time enrichment | Direct `kb/learning.py` transformation and chunk calls; supplied runtime model identity | [MEM-RTE-source-enrichment](#mem-rte-source-enrichment). Exact model-output fidelity and preservation of the pre-enrichment whole input are not established. |
| Promotion and review | Supplied `kb/promotion.py` findings, not a new full engine audit | [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review). Queue/rejected-hash persistence is supported by that route; complete classifier rationale delivery to later search is not established. |
| Scheduled optimization | Direct `_apply` in `kb/self_improve.py`; supplied runtime for selection and scheduling | [MEM-OBJ-optimization-note](#mem-obj-optimization-note), [RT-RTE-index-curation](runtime.md#rt-rte-index-curation) |
| Feedback acquisition and processing | Direct `kb/service.py`, `kb/search_feedback.py` inventory, `kb/feedback_store.py` decision routine; scheduler call-site inventory in `scripts/run_railway.py` | [MEM-OBJ-feedback-events](#mem-obj-feedback-events), [MEM-RTE-feedback-processing](#mem-rte-feedback-processing). Mesh telemetry storage and all downstream operator uses remain incompletely inspected. |
| Vault sync, conflict, deletion and readback | Direct `kb/obsidian_sync.py`, `kb/server.py` push/document branches; supplied boundary for plugin consumer | [MEM-OBJ-obsidian-revisions](#mem-obj-obsidian-revisions), [MEM-RTE-vault-sync](#mem-rte-vault-sync). Plugin's local file-application semantics and browser execution are not independently verified. |
| GitHub/repository/Linear synchronization | Direct stable-key/write/tombstone call-site inventory in `kb/repo_content_sync.py`, `kb/linear_sync.py`; supplied boundary for GitHub sync and stage drivers | Lifecycle records cover known sinks. Full enumeration, upstream sensitivity policy, digest construction and sync checkpoint advancement remain uninspected; no assertion of complete source coverage or lossless mirroring. |
| Retrieval formatting and document expansion | Direct `kb/search_format.py` hit-budget and canonical-body functions, `kb/service.py` and `kb/server.py` document handlers | [MEM-RTE-document-drilldown](#mem-rte-document-drilldown); annotation on [RT-RTE-task-search](runtime.md#rt-rte-task-search). Source metadata and readable snippets are not the full retained payload. |
| Retrieval evaluation | Direct `kb/retrieval_eval.py` scoring function and function inventory; supplied boundary for launcher | [MEM-CLM-retrieval-evaluation](#mem-clm-retrieval-evaluation). No measured run or feedback-driven ranker installation established. |
| Static skills and host policy | Supplied boundary/router passage and runtime catalog refresh | [RT-RTE-skill-refresh](runtime.md#rt-rte-skill-refresh), [RT-CLM-explicit-approval](runtime.md#rt-clm-explicit-approval). Static bundled instructions are not accumulated memory. Satellite policy agreement and installed host versions remain uninspected. |
| Repair, backup and restore | Direct service repair/tombstone/garbage function and CLI/MCP entry inventories; supplied runtime worker recovery | [RT-RTE-source-projection](runtime.md#rt-rte-source-projection). Snapshot admission, restore cutover, legacy garbage predicates and all reconciliation guard branches remain partially uninspected; this prevents universal recovery or irreversible-erasure claims. |

Available but uninspected branches are not absences or access gaps. The table retains them within scope rather than silently shrinking the whole-system boundary.

## Core ideas

1. **Source retention and searchability are separate.** SQLite keeps content revisions and current-head pointers; projection jobs and receipts describe derivative readiness. Lexical retrieval can use current retained bytes before vector readiness. A receipt is not knowledge content or a quality judgment. See [MEM-OBJ-source-revisions](#mem-obj-source-revisions), [MEM-OBJ-projection-receipts](#mem-obj-projection-receipts), [RT-RTE-source-projection](runtime.md#rt-rte-source-projection).
2. **Trace memory is selective, not a transcript mirror.** Automatic personal notes extract prompt/outcome text, marked decisions and edited file names. Volunteered shared traces add capped commands and deterministic error/dead-end descriptions. Those are different artifacts and admission routes; neither establishes a model criticizing its method. See [MEM-OBJ-node-note](#mem-obj-node-note), [MEM-OBJ-session-trace](#mem-obj-session-trace).
3. **Context is bounded at delivery, with expansion on request.** The task hook returns very short descriptions. MCP/CLI can return longer bounded hit text; explicit document drilldown restores a canonical body, not merely another summary. These are external-memory request and host-triggered supply routes, not evidence of host conversation compaction. See [RT-RTE-task-search](runtime.md#rt-rte-task-search), [MEM-RTE-document-drilldown](#mem-rte-document-drilldown).
4. **Authorship, admission and authority differ.** Software can capture a model-authored session outcome without per-note approval. Models propose summaries or promotion judgments; code and sometimes reviewers admit results. Later agents receive untrusted context, not binding instruction merely because it is in Central. See [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review), [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery).
5. **Recorded feedback need not change ranking.** The durable processor classifies events into candidates or no-action and persists decisions. An explicit fallback feedback note can also enter searchable memory, independently of the candidate ledger. Neither proves capacity improvement. See [MEM-RTE-feedback-processing](#mem-rte-feedback-processing).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-source-revisions
Label: Lifecycle source revisions and heads

Source-native identity: `source_revisions` and `source_heads` in `LifecycleStore`. Storage substrate: SQLite BLOB bytes, metadata columns and relational pointers. Representational form: natural-language or source-code document bytes as submitted to this layer; symbolic identifiers, hashes, dataset/media-type fields and head relations are distinct access/control metadata. A BLOB does not imply a distributed-parametric representation. Lineage: source key, previous revision, locator, actor/run, capture metadata and content hash. Consumers: worker reload for projection, lexical search, and document drilldown; the head relation has fixed selection authority, while text has advisory authority at later agents. SRC-1: `kb/lifecycle.py`, `kb/service.py`.

Distinct from the acceptance receipt [RT-OBJ-ingest-result](runtime.md#rt-obj-ingest-result): that receipt refers to these durable objects but is not their content. This object is the retained input of [RT-RTE-source-projection](runtime.md#rt-rte-source-projection), not a duplicate route.

> retained_content BLOB NOT NULL,
> --- `kb/lifecycle.py`

> previous_revision_id TEXT REFERENCES source_revisions(source_revision_id),
> --- `kb/lifecycle.py`

Tombstoning adds an immutable head revision rather than erasing history. Lexical search joins current heads and filters `revision.tombstone = 0`. This warrants current-search exclusion, not physical forgetting or universal denial of historical-ID reads; [MEM-RTE-document-drilldown](#mem-rte-document-drilldown) has a different selection rule. Initialization is caller-supplied capture; human control over each content item is unresolved for generic API callers. Subsequent head replacement and automatic projection are code-controlled.

> """Write an immutable current-head tombstone without editing history."""
> --- `kb/lifecycle.py`

#### MEM-OBJ-projection-receipts
Label: Projection jobs and receipts

Source-native identity: `projection_jobs`, `projection_receipts`. Substrate: lifecycle SQLite tables. Form: symbolic job states, backend/model/dimensions, generation/config identity, affected IDs, error and searchability timestamps. Lineage: source revision → generation/version/config-bound job → backend receipt. Consumers: worker retry/resumption and service read eligibility; authority is fixed code gating, not a model's interpretation of content. These retain operational evidence, not a learned semantic rule. SRC-1: `kb/lifecycle.py`; [RT-RTE-source-projection](runtime.md#rt-rte-source-projection).

> UNIQUE(source_revision_id, generation_id, projection_version)
> --- `kb/lifecycle.py`

No counterpart after comparison with [RT-OBJ-ingest-result](runtime.md#rt-obj-ingest-result): the latter is the immediate public receipt; this record names durable processing state. A searchable backend receipt does not establish answer correctness or graph completeness.

#### MEM-OBJ-search-projections
Label: Vector and graph search projections

Source-native identity: gateway relational material, vector document chunks and graph extraction consumed by `Citadel.search`. Storage: configured Cognee backend stores; frozen adapter inventory includes Qdrant and pgvector branches, and Ladybug graph integration. Exact deployed configuration and full provider-owned objects remain uninspected. Form: chunk text is natural-language/source content; chunk/dataset/revision bindings and graph relations are symbolic; embedding vectors are distributed-parametric numerical representations, distinct from embedding model weights. Graph node descriptions may mix text with symbolic relations; their full derivation and curation cannot be inferred from gateway names. SRC-1: `kb/cognee_client.py`, `kb/lifecycle.py`; supplied [RT-RTE-source-projection](runtime.md#rt-rte-source-projection), [RT-RTE-task-search](runtime.md#rt-rte-task-search).

Lineage: retained bytes → provider projection → bound retrieval candidates, or legacy direct remember without lifecycle history. Later consumers: recall and graph/document views, then result shaping and host interpretation. Model mutability is separately documented by [RT-CMP-embedding-profile](runtime.md#rt-cmp-embedding-profile) and [RT-CMP-cognee-models](runtime.md#rt-cmp-cognee-models); no weight training follows from vector writes. No supplied operative-object counterpart; these are outputs, not the worker route itself.

The opaque alternative is material: gateway `improve` calls upstream Cognee, including the global-context-index flag. This establishes delegation, not the precise retained successor or its later activation.

> return await cognee.improve(
>     dataset=dataset,
>     session_ids=session_ids,
>     build_global_context_index=build_global_context_index,
> )
> --- `kb/cognee_client.py`

#### MEM-OBJ-node-note
Label: Dev session note

Source-native identity: Markdown headed `# Dev session note` produced by `distill_node_note`. Substrate: transient hook string, then admitted source storage in the personal node. Form: natural-language excerpts plus symbolic headings and file paths. Lineage: raw local transcript → deterministic extraction → UTF-8 byte cap → ingest; raw transcript is not sent by this hook. Authorship is mixed human first prompt and assistant text; file names come from tool-use entries. No new model summary is generated locally. SRC-1: `kb/session_trace_distill.py`, `kb/hooks/sync_session.py`.

This is the output object of [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), not a second capture-route declaration. Retains first task and last assistant outcome up to 280 characters each, up to eight marked decision excerpts and forty edited file names. A marker such as “root cause” selects text; it does not verify it or retain every reason. Empty extraction sends nothing. Later personal search and document consumers receive selected excerpts, not complete raw turns or tool results.

> recap_bits.append(f"Outcome: {_truncate(last_assistant_text, 280)}")
> --- `kb/session_trace_distill.py`

> for item in decisions[:8]:
>     lines.append(f"- {item}")
> --- `kb/session_trace_distill.py`

#### MEM-OBJ-session-trace
Label: Shared Session Trace

Source-native identity: `SessionTraceRecord` and `format_compact_context`; form: natural-language task/approach/dead-end descriptions mixed with symbolic author/time/repo/branch and file/command fields. Substrate: local Python record/Markdown then shared and personal source stores. Lineage: MCP accepts already-authored `data` or deterministically distills a local transcript; the supplied-data alternative leaves original provenance unresolved. Server forces author-seat from identity, not from text. SRC-1: `kb/session_trace_distill.py`, `kb/mcp_server.py`, `kb/server.py`.

Distinct from [MEM-OBJ-node-note](#mem-obj-node-note) and the output of [RT-RTE-session-capture](runtime.md#rt-rte-session-capture): sharing is volunteered and has separate dataset and trust treatment. The distiller caps task at 280, approach at 500, files at forty and redacted commands at twelve. Tool-error pairs feed deterministic dead-end generation; this is lossy trace transformation, not an inspectable model criticism loop. Consumers: later scoped search and document readers; host authority is reference-only under the supplied router contract, not attested team policy.

> commands=redact_commands(tuple(commands[:12])),
> --- `kb/session_trace_distill.py`

> dead_ends=_deterministic_dead_ends(tool_error_pairs),
> --- `kb/session_trace_distill.py`

#### MEM-OBJ-optimization-note
Label: Knowledge optimization note

Source-native identity: `Knowledge optimization note` written by `SelfImprovement._apply`. Substrate: admitted source note under `self-improve:<source-key>` and its projections. Form: natural-language summary/label and symbolic proposed tags, source key/locator/revision. Lineage: recent mesh document labels/tags → chat proposal → known-label parsing → additive re-ingest. The original document is not edited by this `_apply` routine. Subsequent revisions can replace the optimization note's own current head. SRC-1: `kb/self_improve.py`; supplied [RT-RTE-index-curation](runtime.md#rt-rte-index-curation).

Distinct from [RT-OBJ-optimize-prompt](runtime.md#rt-obj-optimize-prompt): that static prompt requests the transformation; this is retained output. Later Central search may return it as content. The persisted source pointer is lineage, not the reason the proposed tags are better. No objective-bearing critique, complete original rationale or later rationale reader is established by this format.

> f"Source revision: {proposal.get('source_revision_id') or 'not recorded'}\n"
> f"Summary: {summary}\n"
> f"Proposed tags: {', '.join(proposal.get('tags') or []) or 'none'}"
> --- `kb/self_improve.py`

#### MEM-OBJ-feedback-events
Label: Feedback events and processing decisions

Source-native identity: `FeedbackStore`, `FeedbackEvent`, `FeedbackDecision`; substrate: SQLite ledger. Form: symbolic redacted event IDs, scores, dataset/search/result/QA linkage and decision/reason strings. It is access/use metadata, not full conversation memory. Explicit event construction records text presence rather than free-form feedback in this ledger; a separate fallback note can retain feedback text. Lineage: search telemetry or explicit ratings → durable event → fixed-rule processing decision. SRC-1: `kb/feedback_store.py`, `kb/search_feedback.py`, `kb/service.py`.

No counterpart after comparison with [RT-RTE-index-curation](runtime.md#rt-rte-index-curation): activity counts are not this event processor or proof that event text reaches the optimization model. Consumers: bounded unprocessed-event selector and later decision listing; fixed rules assign repair/ranking candidates or no-action. Ranking-evaluation candidacy is not a modified ranker. Separate Cognee QA-cache feedback has opaque upstream consumer semantics.

> """Build a durable explicit event without storing free-form feedback text."""
> --- `kb/search_feedback.py`

#### MEM-OBJ-obsidian-revisions
Label: Obsidian source revisions and conflicts

Source-native identity: `ObsidianSyncStore` documents, revisions, changes and conflicts. Substrate: JSON file saved via temporary-file replacement, independent of lifecycle SQLite and search projections. Form: natural-language Markdown bodies; symbolic vault/path/revision/hash/cursor/deletion metadata; conflicts retain local and remote bodies. Lineage: plugin/API push → normalized path identity → revision or base-mismatch conflict. Consumers: manifest, pull, document history and conflict resolver; conflict choice has fixed source-replacement authority, body text only advisory downstream authority. SRC-1: `kb/obsidian_sync.py`, `kb/server.py`.

No supplied counterpart: this source store precedes [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)-like learning writes but is not the same acceptance object. In particular it can retain a revision before search admission rejects an oversized or scanned body. Generic authenticated push does not establish a human decision about every note.

> if resolution == "accept_local":
>     resolved_body = conflict["local_body"]
>     path = conflict["path"]
> --- `kb/obsidian_sync.py`

### Routes

#### MEM-RTE-source-enrichment
Label: Optional source enrichment before retention

Distinct from [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission): this is the optional generative transformation available to configured direct `LearningProcess.learn` callers, not part of the HTTP source-admission route. HTTP ingest passes no `allow_llm` override to `execute_learning_writes`; that helper defaults it to False, and `learn` disables enrichment on that branch. Direct learning calls instead default `allow_llm=True`, with full tier and enrichment configuration still required. Shared implementation does not establish route containment. Owner: `LearningProcess`; caller proposes input, configured model proposes chunk text/summary/tags, code chooses enrichment branch, and downstream ingest guards can reject chunks. Mode: capture/maintenance requests, not an answer-key comparison; answer oracle: none established. Input guidance is source text and enrichment instructions; persisted result is searchable chunk material, not a trained model. SRC-1: `kb/learning.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: aggregate LearningOutcome and per-chunk ingest results plus enrichment metadata.
- Later read-back: admitted derived chunk bodies and tags reach subsequent search/document invocations.
- Delegated visibility: enrichment model can receive admitted source input on enabled paths; light/shared or allow_llm=False paths bypass it.
- Selection predicate: content scan, allow_llm and tier, optional enrichment result; empty or failed enrichment falls back to plain material.
- Invalidation or expiry: stable chunk keys support revision replacement; obsolete keys are tombstoned only after all new chunks accept.
- Activation or effect: automatic transformation and persistence calls wired; model fidelity and later behavioral influence unobserved.
- Evidence limits: complete pre-transformation whole-input preservation, provider internals and actual enabled configuration uninspected.

> """Merge the one-line summary into the chunk body so it is searchable."""
> --- `kb/learning.py`

Rejection and recovery: whole-input scan precedes external enrichment, and each chunk passes service admission. Software controls subsequent transformation without per-chunk human approval. A successful call does not imply atomic replacement of every chunk; failures and partial acceptance must remain distinct. This is acquisition/curation, not evidence of improved future capacity.

#### MEM-RTE-share-session
Label: Volunteered trace to shared and personal memory

Distinct from [RT-RTE-session-capture](runtime.md#rt-rte-session-capture): registered MCP tool forwards to `/api/share-session`, which has its own capture-root, identity, size, scan and multi-target handling. Owner: MCP wrapper and HTTP server. Caller supplies text or transcript; deterministic code authors extracted form, server forces author-seat and admits writes. Explicit approval is tool policy, not a verified consent field. Mode: volunteered sharing; no answer oracle. SRC-1: `kb/mcp_server.py`, `kb/server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: target operations and acceptance result; persistent partial failure becomes HTTP 500 after a failed-target retry.
- Later read-back: accepted copies in session-traces and personal memory can enter later scoped search.
- Delegated visibility: server gets compact text, cwd, capture roots and error flag, not necessarily the raw transcript.
- Selection predicate: caller volunteering, local data/transcript choice; writer kb:ingest, server capture-root enforcement, byte and configured scan checks.
- Invalidation or expiry: downstream source revision rules; no separate trace TTL established.
- Activation or effect: dual-target admission and retries wired; reference-only trust is guidance to later consumers, not proof of compliance.
- Evidence limits: transcript provenance for supplied data, user approval, complete redaction and real successful dual writes unobserved.

> Writes to ``session-traces`` (reference-only) and your private Node.
> --- `kb/mcp_server.py`

> data = force_shared_trace_author_seat(body.data, actor.seat_slug)
> --- `kb/server.py`

Admission can reject secret content and unsuccessful writes. Retry is not rollback: a target already accepting can remain populated if another fails. The transformation retains selected failure descriptions, not every raw tool result or a demonstrated causal lesson.

#### MEM-RTE-document-drilldown
Label: Search pointer to source body

Distinct follow-up to [RT-RTE-task-search](runtime.md#rt-rte-task-search), not a redeclaration of retrieval. Owner: MCP/CLI request and server document handler. Trigger: caller chooses a document ID or exposed endpoint. Service prefers lifecycle retained body by revision ID when not chunk-scoped, otherwise gateway resolution; HTTP has separate GitHub-section and owned-Obsidian branches. SRC-1: `kb/mcp_server.py`, `kb/service.py`, `kb/server.py`, `kb/search_format.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: authorized source document, or 404/typed failure; MCP/CLI canonicalize duplicate body/content/text fields to body.
- Later read-back: yes — a later explicit invocation can recover retained content omitted from hit windows.
- Delegated visibility: caller receives body and public provenance; Obsidian document can include revision history; internal dataset node IDs are removed from gateway response.
- Selection predicate: requested ID, optional chunk scope, reader kb:read and dataset/vault visibility; not semantic reselection by a new query.
- Invalidation or expiry: lifecycle lookup by revision ID is not restricted here to current non-tombstoned heads; current-search exclusion therefore does not imply historical-ID erasure.
- Activation or effect: body delivery wired; host trust or behavioral reliance unobserved.
- Evidence limits: complete provider resolution semantics and deployed data not inspected; no universal current-only or physical-forgetting guarantee.

> source = self.lifecycle_store.get_source_revision(document_id)
> --- `kb/service.py:2293-2293`

> return retained_document(source, content)
> --- `kb/service.py:2293-2302`

The expansion body has no separate truncation in the inspected canonical-body routine; that routine removes redundant aliases, not semantic content. This is request-driven external-memory readback, not an unsolicited push or a pointer automatically dereferenced by the model window.

#### MEM-RTE-feedback-processing
Label: Feedback to ledger decisions and searchable fallback

Owner: service feedback handler, then scheduled fixed-rule `process_feedback_events`; explicit caller proposes rating/text, code records and categorizes it. No per-event human approval is encoded beyond the caller's submission. Mode: explicit ratings plus automatic telemetry and bounded processing batches. No expected-answer oracle in the processor; receipt gaps and +/-1 ratings are predicates, not answer truth. Distinct from [RT-RTE-index-curation](runtime.md#rt-rte-index-curation). SRC-1: `kb/service.py`, `kb/feedback_store.py`, `scripts/run_railway.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: recorded/improved flags and reason; processor returns a tuple of persisted decisions.
- Later read-back: processor reloads unprocessed events; optional durable fallback note enters later dataset search; session cache retains separate QA linkage when supported.
- Delegated visibility: durable event excludes free-form feedback text, while Cognee session feedback and fallback note may receive it.
- Selection predicate: unprocessed ledger batch limit; receipt-gap test first, explicit +/-1 second, otherwise no_action.
- Invalidation or expiry: recorded decisions remove events from unprocessed selection; TTL and ledger deletion not established.
- Activation or effect: classification and feedback-note admission wired; candidate labels do not themselves repair projection or modify ranking.
- Evidence limits: upstream Cognee feedback/improve semantics and later ranking-evaluation consumer unresolved; no measured improvement.

> return "no_action", "telemetry is recorded without autonomous mutation"
> --- `kb/feedback_store.py`

> """Process a bounded batch without LLM, promotion, or memory mutation."""
> --- `kb/feedback_store.py`

The docstring concerns the event processor, not all feedback paths. In `Citadel.feedback`, a failed session-cache match instead ingests a note containing QA, score and optional text. Guards can reject it, and `recorded` follows acceptance. `allow_llm=False` defaults suppress immediate improvement; opt-in internal automatic improvement has a separate evaluation gate. A recorded signal is not necessarily fed to the optimization prompt.

#### MEM-RTE-vault-sync
Label: Vault revision admission and searchable copy

Owner: owned-vault HTTP push and JSON source store, then learning pipeline. Caller/plugin supplies Markdown and base revision; code rejects duplicate normalized paths, detects stale-base conflicts and saves accepted source revisions. Search admission occurs afterward. Conflict resolver chooses remote, local, manual or save-both; generic actor identity does not resolve whether a person or software made that choice. Mode: synchronization/editing, not controlled experiment. Oracle: none established; matching a base revision is consistency checking, not semantic validation. SRC-1: `kb/obsidian_sync.py`, `kb/server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: accepted/skipped/conflict source results and separate ingest outcomes; source acceptance can precede search rejection.
- Later read-back: cursor pull and document history reload source material; admitted searchable copies enter later search.
- Delegated visibility: JSON source store retains bodies and conflicts; learning receives accepted current content; supplied boundary establishes plugin as a pull/push consumer, not verified local application.
- Selection predicate: vault ownership, normalized path and base revision; unchanged hashes skip; search path separately resolves target and checks size/content.
- Invalidation or expiry: deletion records empty-body deleted revision then requests lifecycle tombstone by stable Obsidian key; histories/conflicts are not physically erased by that operation.
- Activation or effect: source editing and search-copy updates wired; cross-store atomicity and deployed synchronization unobserved.
- Evidence limits: not every rejection unwinds prior JSON save; plugin/browser behavior, rollback across stores and actual human review uninspected.

> with tmp_path.open("w", encoding="utf-8") as handle:
>     json.dump(data, handle, indent=2, sort_keys=True)
> tmp_path.replace(self.path)
> --- `kb/obsidian_sync.py`

> result = get_obsidian_sync().push(
>     vault_id=body.vault_id,
>     actor=actor,
>     documents=push_documents,
>     dataset=push_dataset,
> )
> --- `kb/server.py`

The ordering matters: source revisions can survive a later oversized-note rejection or scanner failure. Thus the runtime's generic “rejected writes do not enter the store” must be read as the particular ingest store, not every memory substrate. Manual conflict bodies can be adopted as new revisions; that does not establish a semantic critique, improved knowledge or agent weight update.

### Claims

#### MEM-CLM-retrieval-evaluation
Label: Retrieval evaluation distinguishes answer text and source identity

Claimed operation and implementation: `score_question` separates answer-span rank, named-document recall and ordering checks. Supplied question `answer_spans` are the reference oracle; `expect_any` plus ground-truth matching supplies document identity expectations. This is bounded benchmark evaluation, not ordinary search's oracle or a universal admission gate. SRC-1: `kb/retrieval_eval.py`. No counterpart after comparison with [RT-RTE-index-curation](runtime.md#rt-rte-index-curation): evaluator presence does not wire its results into note admission or ranking revision.

> spans = [normalize(span) for span in question.get("answer_spans") or []]
> --- `kb/retrieval_eval.py`

> if any(span in body for body in bodies for span in spans):
>     answer_rank = entry["effective_rank"]
> --- `kb/retrieval_eval.py`

Bodies are normalized and headers split for the answer test. A second document quoting the answer can pass answer-text retrieval independently of named-document recall. Metrics therefore cannot alone attest provenance or correct later task behavior. No benchmark was run in this analysis; historical comments about executed probes are attributed source commentary, not supplied observed-run evidence.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-current-head
Label: Current head gates search eligibility

Consumer: lifecycle lexical selector and bound vector retrieval. Channel: symbolic source-head, tombstone and projection-identity fields. Force: code-enforced candidate eligibility within these paths. Horizon: later searches until head/config changes; not all historical document access. SRC-1: `kb/lifecycle.py`; supplied [RT-RTE-source-projection](runtime.md#rt-rte-source-projection), [RT-RTE-task-search](runtime.md#rt-rte-task-search). Distinct from [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery): this is the fixed selector's authority before delivery, not the host's interpretation afterward.

> JOIN source_revisions AS revision
>   ON revision.source_revision_id = head.source_revision_id
> --- `kb/lifecycle.py:1920-1948`

## Annotations

#### On [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Memory lineage and curation: [MEM-OBJ-node-note](#mem-obj-node-note) is a lossy derived artifact from raw user/assistant/tool-use trace material, with code choosing excerpts. The runtime correctly separates automatic admission from per-content approval. This is a trace-fed retained write with later personal-search consumer, not merely raw logging. Source reasons are retained only where the short selected assistant excerpt happens to contain them; future search does not reload the original transcript through this route. SRC-1: `kb/session_trace_distill.py`, `kb/hooks/sync_session.py`.

#### On [RT-RTE-task-search](runtime.md#rt-rte-task-search)

Working context: supplied runtime establishes hook top-three selection, 500-character descriptions and 6,000-character outer cap. Direct `prepare_search_payload_for_agent` inspection adds a distinct MCP/CLI delivery budget: default 2,000 hit-text characters, configurable through `CITADEL_MCP_MAX_HIT_TEXT_CHARS`; zero disables that trimming. Omitted full body remains in source storage, with an expansion hint only when drilldown is available. SRC-1: `kb/search_format.py`.

> if not raw:
>     return 2000
> --- `kb/search_format.py:2130-2138`

> "Truncated. Full document drilldown is unavailable for this result."
> --- `kb/search_format.py`

Read-back direction is layered: host prompt triggers the hook, code requests and selects retained hits, and stdout offers them to the host without the foreground agent making a search call. MCP/CLI instead respond to explicit calls. Neither proves an unsolicited service push independent of a task trigger. Retrieval targets query, scope and filters, not merely a file identifier. There is no separate subagent context here; full corpus is kept out and excerpts enter by value. The stack-frame analogy does not establish host turn eviction or reference liveness; IDs require an explicit read call to expand.

#### On [RT-RTE-index-curation](runtime.md#rt-rte-index-curation)

Retained output is [MEM-OBJ-optimization-note](#mem-obj-optimization-note), not a mutation of the original note's tags/body by `_apply`. Automatic source-note authorship comes from a model proposal using labels/tags, not full trace feedback. Reasons for the proposed semantic change are not a required persisted field. Separate upstream Cognee improve remains an opaque transformation in [MEM-OBJ-search-projections](#mem-obj-search-projections); this limit must not erase known additive note writes. SRC-1: `kb/self_improve.py`, `kb/cognee_client.py`.

#### On [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review)

Supplied findings establish copying private candidate material into later shared retrieval and hash-bound rejection preventing repeated admission of unchanged rejected content. This is admission curation, not proof that content became true or instruction-authoritative. Shared search consumer receives the accepted content and provenance, not an established complete rationale trail from the classification/review process. Storage details and complete rationale retention remain uninspected beyond the supplied route. SRC-1: `kb/promotion.py`; supporting passages are retained in the cited runtime record.

## Write side

| Mechanism | Authorship and physical write | Admission control, rejection and later material |
|---|---|---|
| User/API/local capture | Caller authors input; software writes retained source and projections | HTTP roles/targets and scans differ from direct local service access. Generic caller identity leaves human per-content control unresolved. See [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission), [RT-RTE-local-access](runtime.md#rt-rte-local-access). |
| Personal trace distillation | Code excerpts mixed human/assistant trace; no local model call | Automatic hook sends after one-time setup; server can reject. Retained note feeds later personal search, not host checkpoint restoration. [MEM-OBJ-node-note](#mem-obj-node-note). |
| Shared trace | Caller-authored compact text or deterministic trace conversion | Tool asks approval; endpoint enforces identity/root/size/scan and dual writes, not a consent attestation. Reasons can be truncated; partial writes are not atomically undone. [MEM-RTE-share-session](#mem-rte-share-session). |
| Optional enrichment | Model supplies text/summary/tags; code prepends summary and ingests chunks | Software/tier/config decide; scan before provider and service checks after transformation. Failed enrichment can fall back; obsolete chunk tombstones follow successful replacement. [MEM-RTE-source-enrichment](#mem-rte-source-enrichment). |
| Projection/maintenance | Worker reloads retained bytes; providers compute derivatives | Leases and backend read checks gate readiness. Opaque provider improve must not be conflated with explicit optimization-note writes. [RT-RTE-source-projection](runtime.md#rt-rte-source-projection), [MEM-OBJ-search-projections](#mem-obj-search-projections). |
| Promotion | Candidate content originates in seat memory; model judges and code copies | Known work can auto-admit, new projects require review; reject hash blocks repeat. No universal human approval. [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review). |
| Optimization notes | Model proposes from selected labels/tags; code re-ingests additive note | Known-label parser, dry-run application guard and ingest veto; not full-source editing or demonstrated objective-responsive improvement. [MEM-OBJ-optimization-note](#mem-obj-optimization-note). |
| Feedback | Caller rating, automatic telemetry and code decisions; fallback note can retain text | Fixed event categorization does not mutate ranker; admission of fallback note is a separate write. [MEM-RTE-feedback-processing](#mem-rte-feedback-processing). |
| Vault editing | Plugin/API supplies bodies; source store saves history/conflicts | Base-revision and ownership control source adoption, then distinct search checks. Human decision is explicit only when a human actually supplies/resolves content, not established for generic calls. [MEM-RTE-vault-sync](#mem-rte-vault-sync). |
| Connector writes and removal | Upstream artifacts enter source-keyed learning calls | Direct call-site inventory identifies repository-path and Linear issue keys plus tombstones. Full upstream filtering/checkpoint semantics remain unresolved; no complete mirror claim. SRC-1: `kb/repo_content_sync.py`, `kb/linear_sync.py`. |

Withdrawal has several meanings: rejected admission, replacing current heads, tombstoning searchable sources, rejecting promotion, and resolving source conflicts. These are not equivalent to erasing old bytes. Source heads and projection bindings can suppress obsolete retrieval while history remains. Neither a deletion label nor a quality-evaluation candidate establishes that every later consumer stops seeing historical material. Backup/restore and legacy garbage operations remain named uninspected limits in the coverage table, not omitted alternatives.

The known automatic trace-to-derived-to-consumer chain is transcript → short personal/shared artifact → accepted source/projection → later scoped search or document call → host. The retained result can shape future behavior without weight updates. This establishes a persistent experience pathway, not successful learning or exercised self-improvement. No transcript compaction checkpoint replacing the host window is established here; the alternative JSON vault history, lifecycle history and opaque provider context index remain distinct retained forms.

## Read-back

- **Task hook:** task-triggered automatic query selection and bounded stdout supply. The selector is code, not a memory-management model. Corpus and full documents remain outside the window; full text can sometimes be fetched later. Host compliance is not observed. [RT-RTE-task-search](runtime.md#rt-rte-task-search), [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery).
- **Explicit search:** MCP, HTTP and CLI return request-selected scoped hits. Dataset/session rules and lexical/vector alternatives matter; local service is a different authority envelope. No API alone establishes every possible external consumer. [RT-RTE-local-access](runtime.md#rt-rte-local-access), [MEM-OBJ-search-projections](#mem-obj-search-projections).
- **Document expansion:** requested IDs reload source bytes or provider documents and canonicalize body aliases; retained revision lookup differs from current-search selection. It is an actual registered call path, not merely hypothetical library storage. [MEM-RTE-document-drilldown](#mem-rte-document-drilldown).
- **Maintenance:** worker leases reload retained bytes; optimizer selects recent non-optimization document labels/tags; promotion reads seat candidates and rejection history. These consumers have transformation/admission authority before any host sees content. [RT-RTE-source-projection](runtime.md#rt-rte-source-projection), [RT-RTE-index-curation](runtime.md#rt-rte-index-curation), [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review).
- **Feedback:** scheduled processor consumes bounded unprocessed metadata, not an established model criticism corpus; fallback notes have independent semantic search visibility. [MEM-RTE-feedback-processing](#mem-rte-feedback-processing).
- **Vault:** cursor pull and history/document handlers consume saved revisions; conflict resolution can read retained local/remote bodies and write a successor. Supplied boundary identifies plugin/browser roles, but installed wiring and local application are unobserved. [MEM-RTE-vault-sync](#mem-rte-vault-sync).

Static skill content and its catalog hashes do not become accumulated memory merely because they are served on request. Conversely, mutable source revisions, optimization notes and derived trace summaries qualify as retained material when these later invocation routes reload them. None of these paths independently establishes that delivered content actually changed a host decision.

## Integration issues

1. **Scope correction to rejection language.** [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) says rejected writes do not enter the store. That is supported for rejected ingest, but cannot be generalized to all source retention: owned Obsidian push saves JSON revisions before size/scan/search admission. [MEM-OBJ-obsidian-revisions](#mem-obj-obsidian-revisions), [MEM-RTE-vault-sync](#mem-rte-vault-sync); SRC-1: `kb/server.py`, `kb/obsidian_sync.py`. Consequence: searchable admission and source retention must stay separate.
2. **Withdrawal boundary.** Current-head tombstones exclude ordinary search, not necessarily authorized historical-ID drilldown. [MEM-OBJ-source-revisions](#mem-obj-source-revisions), [MEM-RTE-document-drilldown](#mem-rte-document-drilldown), [MEM-BAP-current-head](#mem-bap-current-head); SRC-1: `kb/lifecycle.py`, `kb/service.py`. This qualifies, rather than contradicts, the runtime's current-revision vector account. Physical erasure and universal historical-read denial remain unestablished.
3. **Corrected route attribution; no duplicate declarations intended.** [MEM-RTE-source-enrichment](#mem-rte-source-enrichment) is a distinct direct-learning transformation, not part of [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission). Rechecking SRC-1 `kb/server.py` (`ingest`, `execute_learning_writes`) and `kb/learning.py` (`learn`) confirms HTTP supplies no override of the helper's `allow_llm=False`, while direct learning defaults to True. The erroneous formal containment and its dependent descriptions have been removed; enabled enrichment must not be attributed to HTTP admission. Other new objects are retained inputs/outputs/state rather than duplicate runtime routes. Trace sharing differs from automatic personal capture; document expansion differs from task search; event processing differs from label/tag optimization. Closest supplied records and identity distinctions are stated at each declaration. No known possible duplicate remains unresolved.
4. **Opaque provider successor.** [MEM-OBJ-search-projections](#mem-obj-search-projections) retains Cognee improve/global-context-index uncertainty. Supplied [RT-RTE-index-curation](runtime.md#rt-rte-index-curation) establishes a call, not exact upstream revised material or readback. This prevents a complete trace-learning or system-improvement conclusion for that alternative; it does not suppress the explicit optimization-note pathway.
5. **Reasons and downstream consumers.** [MEM-OBJ-optimization-note](#mem-obj-optimization-note) stores pointers/summary/tags, not mandatory reasons; promotion rationale retention/readback is uninspected; feedback decisions name candidates without an established installed ranking successor. [MEM-RTE-feedback-processing](#mem-rte-feedback-processing), [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review). Consequence: persistent records and curation must not be presented as iterative content-directed criticism or improved capacity.
6. **Remaining included paths.** Connector enumeration/checkpoint rules, root/git-push capture, backup/restore, complete reconciliation/garbage branches, satellite policies and plugin/browser application remain partially uninspected as itemized in the coverage table. Relevant known sinks and supplied records are retained, but these gaps prevent universal corpus, rollback, consent, erasure or policy-agreement conclusions. No evidence supports calling those mechanisms absent.

## Limitations and checks

Evidence supports implemented retention, transformation, selection and delivery, not observed use, reliable model judgment, benchmark performance or causal task benefit. The source revision and exact run/source identity were rechecked against supplied boundary and runtime. The job, member type, boundary/runtime types, collection, worker rules and complete records contract were read; no prior target analysis or other analyst output was consulted. Search errors for nonexistent guessed filenames were corrected by reading the actual imported module; they supply no absence finding.

The report deliberately does not claim exhaustive inspection of the whole-system repository. Named unresolved paths prevent stronger conclusions without changing the frozen boundary. Quotes retain minimum passages at SRC-1, including bounded line attributions where repeated code would otherwise be ambiguous. Deterministic validation: the final candidate passed the supplied role/artifact check (exit 0). This establishes form, relation resolution and quotation occurrence, not semantic acceptance.
