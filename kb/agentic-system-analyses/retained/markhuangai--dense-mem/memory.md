---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Dense-Mem memory: evidence and semantic state, session checkpoints, derived organization, bounded read-back and withdrawal."
run-id: AAS-2026-10-15-dense-mem-1a314bed9a5c-01
source-identity: https://github.com/markhuangai/dense-mem
reviewed-boundary: bd736450454e237f1ab6d138f4ae9755916d73f6
---

# Dense-Mem memory report

## Boundary and evidence

Dense-Mem retains and governs memory for callers; it does not own their conversation loop. The frozen source is SRC-1 at `bd736450454e237f1ab6d138f4ae9755916d73f6`, with cutoff 2026-10-15 and the whole-system boundary supplied in [boundary](boundary.md#boundary-and-evidence). This account includes direct Remember, private session ingestion, semantic/lifecycle edits, automatic and manager organization, search repair, conflict resolution, trace/export, feedback, historical Dream display and shipped evaluation/host consumers. External host prompt assembly, provider internals and external infrastructure implementation remain outside it. These exclusions prevent end-to-end answer, provider-training and deployed durability conclusions.

The runtime findings are provisional supplied implementation findings. Additional direct reads below are implementation or target-authored contracts from the same SRC-1, not another source. No execution, provider calls, tests or evaluation runs were performed. Existing tracked tests are not treated as successful observations. No checkout access gap was encountered. Detailed available but uninspected paths are named below; they are not evidenced absences.

### Coverage inventory

| Entry or operation | Source paths in SRC-1; inspection basis | Covering records or local uncertainty and prevented conclusion |
| --- | --- | --- |
| CLI dispatch and registration | Direct: `cmd/server/main.go`, `internal/tools/registry/contract.go`, `internal/tools/registry/toolset.go`; supplied runtime: HTTP/MCP dispatch | Startup or explicit migration retirement, not an autonomous conversational loop. Eight production contract tools include session, correction, retraction, feedback and pack export, beyond Remember/recall. [RT-RTE-remember-intake](runtime.md#rt-rte-remember-intake); new routes below cover additional operations. Migration internals remain uninspected: no upgrade-safety claim. |
| Remember admission and replay | Direct: `internal/knowledge/postgres/remember_commit.go`; supplied runtime: service/preparer/processor | [RT-RTE-remember-intake](runtime.md#rt-rte-remember-intake), [MEM-OBJ-evidence-fragments](#mem-obj-evidence-fragments), [MEM-OBJ-relationship-records](#mem-obj-relationship-records). Detailed duplicate canonicalization and source-revision helper internals remain uninspected: no universal identity or revision-correctness claim. |
| Raw sessions, extraction/linking checkpoints and semantic commit | Direct: `internal/session/contract/types.go`, `internal/session/service/extraction.go`, `internal/knowledge/postgres/session_intake.go`, `session_checkpoint.go`, bounded `session_commit.go`; supplied runtime: provider and orchestration | [RT-RTE-session-intake](runtime.md#rt-rte-session-intake), [MEM-OBJ-session-events](#mem-obj-session-events), [MEM-OBJ-extraction-checkpoints](#mem-obj-extraction-checkpoints). Window construction and every extraction validator branch uninspected: no complete omission/grounding audit. |
| Recall, ranking and support eligibility | Direct: bounded `internal/recall/retrieval.go`, `internal/recall/postgres/recall_repository.go`; source search of `internal/recall/recall.go`; supplied runtime: recall/space branches | [RT-RTE-recall-context](runtime.md#rt-rte-recall-context). Hydration and present/historical eligibility are distinct; not every source/query helper audited. No complete historical consistency or ranking-quality guarantee. |
| Trace and graph views | Direct: `internal/trace/service.go`, bounded `internal/graph/graph.go`; supplied boundary: browser/Python consumer | [MEM-RTE-trace-export](#mem-rte-trace-export), [MEM-RTE-administrative-views](#mem-rte-administrative-views). Detailed trace SQL, graph SQL and final browser display transformations uninspected: no complete-field, full-content or UI authorization audit. |
| Memory-pack and skill export | Direct: `internal/memorypack/memory_pack.go`, registry catalog; supplied runtime: export prompt and registration | [MEM-RTE-trace-export](#mem-rte-trace-export), [RT-RTE-skill-export](runtime.md#rt-rte-skill-export). JSON export is not skill installation or an import route. External persistence/adoption unobserved. |
| Correction, retraction and supersession | Direct: `internal/lifecycle/service.go`, bounded `internal/knowledge/postgres/relationship_correction_repository.go`, `semantic_support_helpers.go`, `evidence_lifecycle_repository.go`, Remember commit | [MEM-RTE-lifecycle-changes](#mem-rte-lifecycle-changes). Detailed correction identity selection and reversal semantics remain uninspected. No generic undo guarantee. |
| Private erasure, credential retirement and retention | Direct: bounded `internal/privacy/service/service.go`, `internal/privacy/postgres/store.go`, `store_operations.go`; server startup | [MEM-RTE-private-erasure](#mem-rte-private-erasure). Manifest validation, retention selection and every transport authorization branch not fully read; external backups/provider copies excluded. No verified total-world erasure. |
| Ontology automatic/manager changes and later read-back | Direct: bounded `internal/ontology/postgres/organization.go`, `recall.go`, contract types/organization; supplied runtime: maintenance/service/management | [RT-RTE-ontology-maintenance](runtime.md#rt-rte-ontology-maintenance), [RT-RTE-manager-publication](runtime.md#rt-rte-manager-publication), [MEM-OBJ-ontology-records](#mem-obj-ontology-records), [MEM-OBJ-organization-receipt](#mem-obj-organization-receipt). Full publication/rollback transactions and dependency invalidation uninspected: no universal stale-publication prevention claim. |
| Community topic projection | Direct: `internal/community/service/topic_projection.go`; supplied runtime: recall/community consumers | [MEM-RTE-derived-projections](#mem-rte-derived-projections). Claim/append repository internals and all cohort/freshness rules uninspected; no exhaustive stale-community guarantee. |
| Search-vector repair | Direct: bounded `internal/search/reconciliation.go`; server worker startup | [MEM-RTE-derived-projections](#mem-rte-derived-projections), [MEM-OBJ-search-documents](#mem-obj-search-documents), [MEM-OBJ-search-vectors](#mem-obj-search-vectors). Repository completion fences not independently audited. |
| Conflict review and deletion-only derivation | Direct: bounded `internal/knowledge/postgres/conflict_derived_evidence_task_repository.go`, recall hydration; supplied runtime: review service | [RT-RTE-conflict-review](runtime.md#rt-rte-conflict-review), [MEM-OBJ-conflict-derivation](#mem-obj-conflict-derivation). Detailed resolution-plan execution and majority/fallback ordering remain uninspected; no complete conflict policy audit. |
| Optional feedback and diagnostics | Direct: bounded `internal/recall/feedback.go`, `internal/tools/registry/uat_feedback.go`, composition/startup; supplied runtime: diagnostics | [MEM-RTE-feedback-recording](#mem-rte-feedback-recording). Diagnostics purger internals and portal projection not fully inspected; no claim that every log becomes knowledge or that every diagnostic reason is later model-visible. |
| Historical Dream state | Direct: bounded `internal/dream/control.go`; registry catalog/startup | [MEM-RTE-administrative-views](#mem-rte-administrative-views). Historical payload provenance and all retained hypothesis fields uninspected; names do not establish current dream-generation or reflection. |
| Evaluation import/resume/scoring | Direct source search: `internal/evalharness/runner.go`; supplied runtime: runner and production build exclusion | [RT-RTE-evaluation-suite](runtime.md#rt-rte-evaluation-suite). Detailed import driver, saved-trace completeness and tracked baseline provenance not audited; ignored run artifacts unavailable. No achieved scores, causal benefit or score-driven installation established. |
| Shipped clients, portal, proxy and operational hooks | Supplied boundary/runtime: Python examples, client, proxy, browser endpoints, prompt registration and server workers | Returned context has concrete shipped request/display consumers, but host answer reliance is unobserved. CI/Git hook contents and other harness internals remain uninspected: no release-gate or automated memory-learning claim. Runtime workers above are the inspected automatic hooks, not host conversation hooks. |

## Core ideas

1. **Evidence, semantic state and derived organization have different authority.** Evidence text can reach a model or person as information. Relationship IDs, statuses, support decisions and temporal fields constrain software eligibility. Ontology assignments/groups change discovery and grouping; they are not new factual support. Recall guidance asks hosts to trace discovery before using it as support; it does not enforce host compliance ([RT-BAP-discovery-guidance](runtime.md#rt-bap-discovery-guidance)).
2. **Read-back includes recovery, not only semantic search.** Durable terminal Remember results replay. Private session intake retains raw events, prior-context snapshots, per-window extraction and linked outputs, then reloads them on retries. Later session extraction also receives a bounded selection of prior events. These are actual retained-to-later-invocation chains, unlike an unspecified storage API caller ([RT-RTE-remember-intake](runtime.md#rt-rte-remember-intake), [RT-RTE-session-intake](runtime.md#rt-rte-session-intake)).
3. **Withdrawal changes eligibility without necessarily deleting history.** Retraction appends lifecycle/support decisions, recomputes relationship status and retires search projections. A relationship with other effective support can remain eligible. Private erasure instead deletes a manifest of owned rows after sealing and generation change. These are different controls, not one generic forgetting operation ([MEM-RTE-lifecycle-changes](#mem-rte-lifecycle-changes), [MEM-RTE-private-erasure](#mem-rte-private-erasure)).
4. **Automatic curation is not automatically experience learning.** Session event text can contain caller-supplied interaction traces, but its origin is not authenticated as such. Extraction and ontology organization retain derived material that later intake/recall consumes. Feedback and evaluation retain operational traces for readers and scorers; the inspected paths do not establish automatic feedback-driven semantic revision, provider updates or improved future capacity. Conflict deletion-only evidence is audit input deliberately excluded from evidence recall, not learned factual support ([MEM-OBJ-conflict-derivation](#mem-obj-conflict-derivation)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-evidence-fragments
Label: Evidence content and occurrence lineage

Source-native identity: `evidence_fragments`, submitted/canonical occurrence references, source/revision and lifecycle records. PostgreSQL stores natural-language evidence content separately from symbolic hashes, IDs, ownership, space/generation, source keys/revisions, aliases, security and lifecycle events. These operative parts have different consumers: models/people interpret content; code uses metadata to select and admit it. No opaque embedding payload is being called text. This object spans intake and read routes, not a duplicate of the temporary [RT-OBJ-assessment-session](runtime.md#rt-obj-assessment-session). Closest supplied routes are [RT-RTE-remember-intake](runtime.md#rt-rte-remember-intake) and [RT-RTE-session-intake](runtime.md#rt-rte-session-intake); neither declares a persistent evidence object.

Direct Remember resolves evidence, advances optional source revisions, can write quarantine events, applies supersessions and remaps references before semantic effects. Session evidence is instead an exact source substring checked against staged event text and event/session metadata. Authority/source labels record attributed provenance, not independent factual validation. Read eligibility excludes quarantine, deletion-only conflict derivations and lifecycle-terminal evidence, with explicit historical conditions. Trace/export may expose provenance and historical material that ordinary recall omits. SRC-1, `internal/knowledge/postgres/remember_commit.go`, `internal/knowledge/postgres/session_commit.go`, `internal/recall/postgres/recall_repository.go`.

> if start < 0 || end <= start || end > len(runes) || item.Content != string(runes[start:end]) {
> return session.ErrInvalidInput
> }
> --- `internal/knowledge/postgres/session_commit.go`

> AND COALESCE(fragment.metadata->>'conflict_resolution_deletion_only', '') <> 'true'
> --- `internal/recall/postgres/recall_repository.go:700-710`

#### MEM-OBJ-relationship-records
Label: Relationships and effective support history

Source-native identity: `relationship_records`, `relationship_observations`, `relationship_evidence_supports`, support-decision and transition events. PostgreSQL stores symbolic entity/predicate/value references, polarity, versions, temporal intervals, status and support counts; attached quotes and text values retain natural-language content for interpretation. Support-decision metadata and IDs are access/lineage state, not an evidence summary. Proposed observations derive from submitted and authorized known evidence. Commit checks that submitted supports belong to the request or known snapshot and requires active applied relationships. The software effect is retained semantic eligibility; host truth acceptance is not established.

Different consumers read different parts: recall hydrates active/supported semantics, temporal queries can admit appropriately superseded history, trace exposes observations/support/lifecycle/transitions, and ontology/community consumers derive organization. A one-cardinality replacement can mark earlier active relationships superseded and record transitions rather than erase them. No counterpart object is declared in supplied runtime; closest [RT-RTE-remember-intake](runtime.md#rt-rte-remember-intake), [RT-RTE-conflict-review](runtime.md#rt-rte-conflict-review) and [RT-RTE-recall-context](runtime.md#rt-rte-recall-context) describe producers/consumers, not this store. SRC-1, `internal/knowledge/postgres/remember_commit.go`, `internal/knowledge/postgres/semantic_support_helpers.go`, `internal/recall/postgres/recall_repository.go`, `internal/trace/service.go`.

> Reason:         "one_cardinality_replaced",
> --- `internal/knowledge/postgres/semantic_support_helpers.go`

#### MEM-OBJ-search-documents
Label: Versioned searchable text projections

Source-native identity: `search_documents` text, document hash/version, source kind/ID/version, projection format/generation, search state and active embedding-contract references. PostgreSQL holds readable textual projections and symbolic access/freshness metadata. Text is derived from admitted evidence or semantic projections, not automatically the complete original trace. Reconciliation sends selected `DocumentText` to the embedding provider; recall obtains candidates through search and separately hydrates eligible evidence/relationships. A projection is not a factual admission oracle. Detailed formatting/truncation helpers are uninspected, preventing a full projection-fidelity claim. This persistent object is distinct from [RT-CMP-openai-embedding](runtime.md#rt-cmp-openai-embedding), which is the producer model, and spans [RT-RTE-remember-intake](runtime.md#rt-rte-remember-intake) and [RT-RTE-recall-context](runtime.md#rt-rte-recall-context). SRC-1, `internal/knowledge/postgres/remember_commit.go`, `internal/search/reconciliation.go`, `internal/recall/retrieval.go`.

> return nil, nil, errors.New("reconciliation document is missing text or hash")
> --- `internal/search/reconciliation.go`

#### MEM-OBJ-search-vectors
Label: Dense search vectors

Source-native identity: search-document `embedding` plus embedding-contract identity/dimensions. Numerical dense representations have distributed encoding; contract and dimension identifiers are symbolic metadata. PostgreSQL stores these vectors, separately from external model weights. Their lineage is text projection → embedding request → validated numerical vector → inline commit or reconciliation → later vector candidate search/fusion. They influence ranking, not semantic truth or host instruction authority. The exact transformation depends on the configurable provider described by [RT-CMP-openai-embedding](runtime.md#rt-cmp-openai-embedding); vectors are its retained outputs, not a second declaration of that model. External parameters/version and training remain uninspected. Retraction can null vectors while preserving event history. SRC-1, `internal/search/reconciliation.go`, `internal/knowledge/postgres/evidence_lifecycle_repository.go`, `internal/recall/retrieval.go`.

> embedding = NULL,
> embedding_updated_at = NULL,
> embedding_error = '',
> --- `internal/knowledge/postgres/evidence_lifecycle_repository.go`

#### MEM-OBJ-session-events
Label: Staged raw session events

Part of: [RT-RTE-session-intake](runtime.md#rt-rte-session-intake)

This is the route's retained raw-input part, not a competing intake route. Source-native identities: `session_events`, `session_submissions.intake` and `prior_context`. Natural-language event text and symbolic event/session/application/user IDs, hashes, results and scope are stored as PostgreSQL JSON. The caller supplies text; its actual origin can be mixed or opaque despite the `framework` field. Staging precedes extraction. Duplicate event IDs with different text conflict; unfinished events can require the original request. Previously completed same-session events are selected newest-first up to ten, then token-budgeted and reversed for extraction. The staged prior snapshot is reloaded on retry. Raw retained context thus reaches later model calls, independently of whether extraction creates semantic relationships. SRC-1, `internal/knowledge/postgres/session_intake.go`, `internal/session/service/extraction.go`.

> ORDER BY created_at DESC, event_index DESC LIMIT ?
> --- `internal/knowledge/postgres/session_intake.go`

#### MEM-OBJ-extraction-checkpoints
Label: Validated extraction and linking checkpoints

Part of: [RT-RTE-session-intake](runtime.md#rt-rte-session-intake)

Source-native identity: `session_extraction_checkpoints.body`; nonnegative `window_index` stores extraction, `-1` linking. PostgreSQL JSON retains model-derived entity/relationship proposals, citations and any security signals: symbolic references plus natural-language payloads, not hidden model state or full reasoning. Validated responses are saved and later decoded/revalidated instead of regenerated. A security-bearing extraction may already have been checkpointed before `ErrSecurity` is returned; checkpoint presence therefore does not establish accepted semantic memory. Commit requires complete extraction checkpoints and, when semantic preparation exists, a linking checkpoint. The derived-to-consumer chain is staged raw events → window extraction → checkpoints → linking request with proposed entities/relationships and only cited boundary segments → linked checkpoint → semantic preparation → evidence/relationships → later recall. SRC-1, `internal/session/service/extraction.go`, `internal/knowledge/postgres/session_checkpoint.go`, `internal/knowledge/postgres/session_commit.go`.

> if len(response.SecuritySignals) > 0 {
> return session.ExtractionResponse{}, session.ErrSecurity
> }
> --- `internal/session/service/extraction.go`

> if index == -1 {
> submission.Linked = body
> } else {
> submission.Extractions[index] = body
> }
> --- `internal/knowledge/postgres/session_intake.go`

#### MEM-OBJ-ontology-records
Label: Ontology definitions and operational organization

Source-native identity: ontology `Record` revisions/heads. PostgreSQL holds two operative kinds of content. Definitions have natural-language labels, descriptions and aliases used by organization model context and name/lexical lookup. Assignments, groups, overrides, source fingerprints and revision dependencies are symbolic controls consumed by software. A group is an equivalence/organization decision, not a new evidence fragment. Versions, source dependencies and `Current`/stale views localize validity; manager overrides constrain automatic decisions. Admission differs between automatic organization and manager publication, so a manager role is not a universal per-record approval requirement.

No counterpart persistent object is supplied; closest [RT-RTE-ontology-maintenance](runtime.md#rt-rte-ontology-maintenance) and [RT-RTE-manager-publication](runtime.md#rt-rte-manager-publication) are its distinct producers. Later automatic organization receives source-linked current records plus forced/exact/lexical vocabulary candidates; later recall uses name matching/current assignments and groups to discover/group evidence. Definition prose is interpreted by the organizer, while assignment IDs have fixed selection effects. Recall does not need the original organization's full repair conversation or reasons. SRC-1, `internal/ontology/contract/types.go`, `internal/ontology/postgres/organization.go`, `internal/ontology/postgres/recall.go`.

> if !view.Current {
> result.Degradation = "ontology_stale"
> continue
> }
> --- `internal/ontology/postgres/recall.go:196-207`

#### MEM-OBJ-organization-receipt
Label: Organization provenance and outcome receipt

Part of: [RT-RTE-ontology-maintenance](runtime.md#rt-rte-ontology-maintenance)

Source-native identity: `OrganizationReceipt`: hashes, provider-policy identity, source fingerprints, revision dependencies, outcomes, attempt token/failure accounting, ambiguous comparison reasons and optional publication result. It is a durable structured JSON provenance/outcome object, distinct from the model parameters and operational ontology records. Reasons are bounded natural language inside an otherwise symbolic result. The receipt is not necessarily full model deliberation: its contract has outcome/rejection reasons and ambiguous comparisons, not a raw transcript field. Repository `FindOrganization` affords retained-result reuse; supplied runtime establishes maintenance/receipt persistence. Direct recall reads operational record views, not this receipt as factual support. Detailed receipt persistence and all reuse predicates remain uninspected; no exhaustive rationale-retention claim. SRC-1, `internal/ontology/contract/organization.go`, `internal/ontology/postgres/recall.go`; [RT-RTE-ontology-maintenance](runtime.md#rt-rte-ontology-maintenance).

> AmbiguousComparisons []AmbiguousComparison `json:"ambiguous_comparisons,omitempty"`
> --- `internal/ontology/contract/organization.go`

#### MEM-OBJ-conflict-derivation
Label: Deletion-only conflict audit evidence

Part of: [RT-RTE-conflict-review](runtime.md#rt-rte-conflict-review)

Source-native identity: conflict-derived ingest/evidence fragment, `relationship_conflict_evidence_derivations` and task completion state. PostgreSQL stores a fixed natural-language deletion statement plus symbolic conflict, selected-position, target-fragment, origin-index and inferred-authority metadata. This is not a retained model explanation and cannot support a new relationship. The repository writes a deletion-only ingest without a vector document, records derivation identity and completion for recovery, and recall hydration explicitly excludes its metadata flag. Its authority is audit/recovery at the service, not host factual support. It narrows the supplied route's phrase “derived evidence tasks reach later knowledge consumers”: the resolution changes knowledge eligibility, but this derived payload is not itself recalled semantic evidence. SRC-1, `internal/knowledge/postgres/conflict_derived_evidence_task_repository.go`, `internal/recall/postgres/recall_repository.go`.

> content := "Overdue conflict review retracted prior evidence. This deletion-only derivation cannot establish a semantic relationship."
> --- `internal/knowledge/postgres/conflict_derived_evidence_task_repository.go`

> // commitDerivedEvidenceIngest writes deletion-only conflict evidence without
> // entering the retired placement ledger. The derivation is audit input, not a
> // semantic claim, and therefore does not require a vector document.
> --- `internal/knowledge/postgres/conflict_derived_evidence_task_repository.go`

### Routes

#### MEM-RTE-lifecycle-changes
Label: Caller correction and evidence withdrawal

Distinct from [RT-RTE-remember-intake](runtime.md#rt-rte-remember-intake): registry lifecycle bindings call the lifecycle service, not ordinary Remember semantic assessment. Endpoints: authenticated correction/retraction tool → lifecycle application → repository planning/embedding or lifecycle transaction → result and changed eligibility. Caller supplies patch, supports, reason, version/key and optional confirmation; code/repository decide and veto. Generic caller identity leaves human authorship/approval unresolved. Open administrative intake has no expected-answer oracle or demonstrated capacity-improvement objective. SRC-1, `internal/tools/registry/contract.go`, `internal/lifecycle/service.go`, `internal/knowledge/postgres/relationship_correction_repository.go`, `internal/knowledge/postgres/evidence_lifecycle_repository.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Correction receipt with completion, rejection/failure or awaiting-confirmation candidates/token; retraction result with affected, pending and retained-active counts.
- Later read-back: Correction submissions permit status/replay; support/lifecycle/transition events change recall eligibility and are traceable. Existing independent support can preserve a relationship after evidence withdrawal.
- Delegated visibility: Correction embedder receives planned documents, not arbitrary store access; retraction is a code mutation without a semantic model judgment in the inspected application.
- Selection predicate: Actor/team/owner, target IDs, expected version, patch/supports and idempotency; correction has explicit submit/confirm actions and bounded entity candidates. Retraction plans effective supports before revocation.
- Invalidation or expiry: Stale version/search contract, ownership/idempotency conflicts and terminal evidence can reject. Confirmation TTL is two hours in the repository; state-changing corrections cannot fall back to an asynchronous embedding queue.
- Activation or effect: Appended support revocations and relationship recomputation retire only ineligible relationship documents; target evidence documents become not_required and lose vectors. This is wired withdrawal, not observed host forgetting.
- Evidence limits: Full correction matching, confirmation selection and historical read rules not audited. No universal reversal or physical deletion guarantee; retraction history remains distinct from private erasure.

Guidance is the caller's reason/patch plus lifecycle/validation policy, not a learned replacement policy. Persisted events retain reason and IDs; trace can expose lifecycle/support decisions. Recovery uses idempotency and refresh/retry guidance; semantic undo is not established.

> // Corrections cannot fall back to the asynchronous embedding queue. This
> // compatibility entry point therefore fails a state-changing correction
> // unless its caller supplies the precomputed provider result.
> --- `internal/knowledge/postgres/relationship_correction_repository.go`

#### MEM-RTE-private-erasure
Label: Private-space sealing and manifest erasure

No supplied route declares this mechanism; it is distinct from [RT-RTE-manager-publication](runtime.md#rt-rte-manager-publication) and the lifecycle retraction route. Endpoints: owner/control/credential-retirement or retention request → private-memory repository → sealed/generation-advanced space and queued operation → leased worker → manifest deletion/audit scrubbing → completed operation. Service command validation requires irreversible acknowledgement; software policy, legal holds and repository fences can veto. Caller humanity remains unresolved; automatic retention is a separate policy trigger, not per-row human approval. No answer oracle or improvement experiment. SRC-1, `internal/privacy/service/service.go`, `internal/privacy/postgres/store.go`, `internal/privacy/postgres/store_operations.go`, `cmd/internal/serverapp/server.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Erasure/retirement operation, or validation/hold/conflict error; queued does not mean completed.
- Later read-back: Worker reloads operation/space/fence; later operations inspect completion/deleted counts. Intake and reads are bounded by active space generation; old-generation session checkpoints cannot authorize new writes.
- Delegated visibility: Worker gets manifest-scoped database state; no semantic model participates in the inspected deletion transaction.
- Selection predicate: Private space ownership/action, reason/key, retention policy or credential retirement, no conflicting operation/hold, worker lease/fence and matching target generation. Manifest includes session events/checkpoints/diagnostics and semantic/search state.
- Invalidation or expiry: Claim/fence loss, changed generation/state, hold or manifest/count failure rejects transactional completion. Failed sealed operations have an explicit recovery path; retirement can strengthen an existing erase.
- Activation or effect: Generation increments and space seals before deletion. Worker deletes owned rows, removes inbound cross-references, scrubs audit payloads, verifies zero remaining rows for each manifest table, then reactivates an erased space or retires a credential space. Metadata of the operation remains.
- Evidence limits: Full live-catalog manifest validation, transport authorization and retention selector not audited. Transaction implementation is not an observed erasure; external backups, exported artifacts and provider-retained copies are outside this guarantee.

Erasure is intended irreversible; it is not rollback of a model proposal. Retry/claim release and sealed-state recovery are operational recovery, not restoration of deleted content.

> SET generation = generation + 1,
> lifecycle_state = 'sealed',
> --- `internal/privacy/postgres/store.go`

> SET before_payload = NULL,
> after_payload = NULL,
> metadata = $1::jsonb
> --- `internal/privacy/postgres/store_operations.go`

#### MEM-RTE-trace-export
Label: Requested trace and bounded pack export

Distinct from [RT-RTE-recall-context](runtime.md#rt-rte-recall-context): caller supplies relationship handles instead of asking query-ranked recall. Trace service obtains retained provenance; pack export independently invokes the trace repository and assembles JSON. Closest [RT-RTE-skill-export](runtime.md#rt-rte-skill-export) is a different host drafting route, not JSON export. Owner: service code under actor scope. This read route does not admit a knowledge change. SRC-1, `internal/trace/service.go`, `internal/memorypack/memory_pack.go`, `internal/tools/registry/contract.go`; shipped Python tracing consumer supplied in boundary.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Structured trace or canonical pack JSON/hash/filename/omissions; pack artifact is returned, not automatically installed.
- Later read-back: Trace is requested access to accumulated observations, supports, decisions, lifecycle, verification, transitions, conflicts and lineage. Export external persistence/reimport is uninspected — no external consumer execution is supplied.
- Delegated visibility: Trace flags/bounds select content, verification/transitions and graph traversal; pack options omit support or entity names. Pack only collects evidence referenced by included supports.
- Selection predicate: Actor team and relationship ID; trace depth/edge/predicate/topic/relevance filters. Pack deduplicates selected IDs, requires active returned relationships and checks returned identity/team.
- Invalidation or expiry: Missing/inactive relationship rejects pack export; current repository scope applies. Pack bounds: 500 relationships, 100 trace events and 8000 fragment-content runes per trace call.
- Activation or effect: Returns selected memory/provenance to client for verification or export. Truncation/omission means returned payload is not necessarily the full original record. Actual verification, installation or influence on answers is unobserved.
- Evidence limits: Detailed trace repository redaction and historical selection not audited; exported SHA256 identifies bytes, not factual accuracy or complete provenance.

> if trace.Relationship.Status != string(domain.RelationshipStatusActive) {
> return nil, fmt.Errorf("%w: %s", ErrMemoryPackRelationshipNotActive, relationshipID)
> }
> --- `internal/memorypack/memory_pack.go`

#### MEM-RTE-feedback-recording
Label: Optional recall snapshots and feedback readers

No counterpart route in supplied runtime. Distinct from [RT-RTE-evaluation-suite](runtime.md#rt-rte-evaluation-suite): optional production recall feedback is event retention/observability, not qrel scoring or a semantic admission oracle. Endpoints: successful recall binding → optional snapshot recorder → PostgreSQL event repository; voluntary feedback submission → validated ordered writes/metrics; control portal readers → list/get; retention worker → prune. Caller supplies quality/use/comment judgments; software checks references/scope and can reject. Generic caller does not prove human review, truth or per-content approval. SRC-1, `internal/tools/registry/uat_feedback.go`, `internal/recall/feedback.go`, `cmd/internal/serverapp/application_composition.go`, `internal/http/control_portal_observability.go` (reader locations found by source search).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Recall remains successful with a degradation if snapshot persistence fails; feedback returns recorded count or bounded partial-failure guidance.
- Later read-back: Control readers list/get retained events and optional resolver enrichment; pruning removes old events. Inspected service/composition does not connect feedback to automatic semantic or model-parameter updates.
- Delegated visibility: Snapshot contains query, effective/input tool args, content-free result refs/ranks, contract/search/degradation state; comments add caller text. References are not original result content. Production composition omits the optional resolver dependency, so display-time current-content enrichment is not established there.
- Selection predicate: Feedback feature/config and recorder plus metrics gate snapshot creation; submission must match authorized team/space/generation/result refs. List filters or recall ID select read-back.
- Invalidation or expiry: Service defaults to 30-day retention with configured positive override; hourly prune loop. Failed batch stops at first failure, preserving earlier writes; invalid refs require correction, persistence failures request retry.
- Activation or effect: Operational event/feedback and metrics persist; later authorized reader can inspect them. No inspected automatic conversion into behavior-shaping memory is established.
- Evidence limits: Full repository schema, portal field projection and downstream operator action not audited. This bounded negative about inspected consumers is not a whole-repository absence claim or proof feedback never informs an external operator.

> // FeedbackResultRefs converts a Recall result into the stable, content-free
> // references stored with its feedback snapshot. References retain first-seen
> // ordering while duplicate ranks collapse to the earliest positive rank.
> --- `internal/recall/feedback.go`

> RecallFeedback:          buildRecallFeedbackApplication(recallFeedbackApplicationDependencies{Events: deps.RecallFeedbackEvents, Config: deps.AppConfig}),
> --- `cmd/internal/serverapp/application_composition.go`

#### MEM-RTE-derived-projections
Label: Automatic search and community projection maintenance

Distinct from [RT-RTE-ontology-maintenance](runtime.md#rt-rte-ontology-maintenance): these mechanisms consume retained source/projection work to repair vectors or materialize community membership, rather than ask the ontology organizer to classify sources. Shared class is automatic derived-state maintenance; the two operative branches and admission controls remain separate. Owner: server workers/repositories. SRC-1, `internal/search/reconciliation.go`, `internal/community/service/topic_projection.go`, `cmd/internal/serverapp/server.go`; later consumer wiring supplied by [RT-RTE-recall-context](runtime.md#rt-rte-recall-context).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Search run counts/status/errors; topic projection turn progress/error with bounded failure code.
- Later read-back: Updated search documents/vectors feed later candidate retrieval. Community memberships/source snapshots feed community discovery/recall. Claimed jobs and failures support subsequent worker recovery, not host instructions.
- Delegated visibility: Search provider gets selected deduplicated document texts; community projection is deterministic over claimed relationship inputs in the inspected service.
- Selection predicate: Search active contract/run reservation and at most 256 selected documents; provider model/dimensions/output shape/finiteness checks precede repository completion. Topic branch claims work, sorts relationship IDs and derives memberships/source-state hashes before append.
- Invalidation or expiry: Search contract/provider mismatch or failure rejects completion; topic source change/interruption records failure. Detailed repository drift/cohort fences are uninspected — service forwarding does not prove every stale write is rejected.
- Activation or effect: Persisted vectors/group membership can change later retrieval selection. Automatic admission is by code/repository, not per-item human review; no model-authored semantic claim is admitted by re-embedding alone.
- Evidence limits: No run or causal retrieval-quality comparison. Projection rebuild is not provider training, and current-source maintenance does not establish criticism or improved capacity.

Guidance is fixed projection/embedding policy; source state, derived projection and accounting persist, not a revised maintenance method. Retry/failure is operational recovery; rollback semantics depend on uninspected repository paths. No expected-answer oracle; this is recurring maintenance, not benchmark mode.

> _, members := topEntitiesAndMemberships(work.Inputs)
> batch := community.TopicProjectionBatch{Work: *work, Memberships: members}
> --- `internal/community/service/topic_projection.go`

#### MEM-RTE-administrative-views
Label: Graph and historical Dream read surfaces

No counterpart supplied route: these are exposed service/portal read surfaces, not another admission mechanism. Source-native endpoints are graph overview/local/node detail and Dream control list/get/runs/status; owner is caller plus service selector. The first projects current retained graph information; the second exposes historical hypotheses/runs. They are grouped as read-only administrative views, not as identical stores or shared provenance. SRC-1, `internal/graph/graph.go`, `internal/dream/control.go`, `cmd/internal/serverapp/transport_composition.go` (portal wiring supplied by boundary/runtime).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Graph snapshot/node or historical Dream records/status, including retired status, latest run and historical proposed count.
- Later read-back: Requested service/portal reads expose retained semantic state or historical hypotheses. No inspected automatic reinjection of historical Dream statements into assessment/recall is established.
- Delegated visibility: Graph uses normalized scope/query/types/anchor/depth/limit and readable title/body/status/source display fields, not vector values or full raw evidence. Dream display maps statement, rationale and payload summaries; raw payload schema/origin remains uninspected.
- Selection predicate: Team plus normalized graph query/node ID; historical list filters/status/cursor/sort or hypothesis ID select repository records.
- Invalidation or expiry: Missing graph node or historical record returns not-found; full repository eligibility and historical retention rules are uninspected — service methods alone do not show every filter.
- Activation or effect: Information reaches an administrative reader; no observed user decision or current Dream generation follows from display access.
- Evidence limits: Historical statement/rationale are natural language stored behind symbolic IDs; full payload may contain other opaque material. Initialization/write agency and current semantic reuse uninspected, preventing a learning/reflection inference from the label Dream.

> return &StatusResult{Retired: true, LatestRun: latest, HistoricalProposedCount: pending}, nil
> --- `internal/dream/control.go`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-organization-selection
Label: Retained organization into later context selection

Consumer: later organizer and recall service, with different force. Channel: persisted current definitions/assignments/groups selected through source dependencies and vocabulary/name matching. At the organizer, definition text is interpreted in a bounded model request under validation/manager constraints. At recall, symbolic current assignments and group identity have software selection/deduplication force. Horizon: later maintenance and recall invocations across requests, subject to source/revision freshness. This is distinct from [RT-BAP-discovery-guidance](runtime.md#rt-bap-discovery-guidance), which is advisory prose delivered after selection. Delivery of organized context does not guarantee host acceptance or beneficial grouping. Evidence: [MEM-OBJ-ontology-records](#mem-obj-ontology-records); SRC-1, `internal/ontology/postgres/organization.go`, `internal/ontology/postgres/recall.go`, `internal/recall/retrieval.go`.

## Annotations

#### On [RT-RTE-remember-intake](runtime.md#rt-rte-remember-intake)

Durable material is separated into [MEM-OBJ-evidence-fragments](#mem-obj-evidence-fragments), [MEM-OBJ-relationship-records](#mem-obj-relationship-records) and search text/vectors, plus assessment history and terminal attempt result. Provider working history is not the replay object. Accepted commit writes `PublicResult` in the terminal attempt; replay returns that stored result rather than reconstructing it from subsequently changed knowledge. Source-dependent support/embedding fences constrain admission, not truth. Caller supplies the evidence and proposals, assessor proposes interpretation, and code/repository admit; caller humanity remains unresolved. SRC-1, `internal/knowledge/postgres/remember_commit.go`; passage and replay basis supplied by [RT-CLM-commit-fences](runtime.md#rt-clm-commit-fences).

#### On [RT-RTE-session-intake](runtime.md#rt-rte-session-intake)

Raw and derived checkpoints are distinct retained parts ([MEM-OBJ-session-events](#mem-obj-session-events), [MEM-OBJ-extraction-checkpoints](#mem-obj-extraction-checkpoints)). Request lookup reloads original intake/prior context and checkpoints; cache hits are decoded and validated. Later new intake selects completed same-identity events newest-first, at most ten. Code then skips candidates exceeding 2048 prior-context tokens and reverses the kept list. Each extraction frame gets its own window plus that bounded prior, not every raw event or another frame's whole dialogue. Constants permit 20 events, eight windows, 8192 window tokens and 512-rune segments; actual constructor overlap rules remain uninspected. Linking receives proposals with window-prefixed references and only cited window boundary segments; guard limits are 3200 entities and 1600 relationships. Extracted evidence commit rechecks exact event spans. Reasons are therefore retained as source citations/provenance, not established full model deliberation. SRC-1, `internal/session/contract/types.go`, `internal/session/service/extraction.go`, `internal/knowledge/postgres/session_intake.go`, `internal/knowledge/postgres/session_commit.go`.

This is a conditional trace-fed update: when submitted event text is an interaction trace, extraction changes it into durable semantic knowledge and future intake/recall consumes it. The `framework` label alone does not authenticate trace origin; arbitrary caller text also fits. Neither case demonstrates capacity improvement.

#### On [RT-OBJ-assessment-session](runtime.md#rt-obj-assessment-session)

Working-context control is code-selected omission, not summarization. When repair input exceeds the configured budget, `boundRepairHistory` walks assistant turns from recent backward, substituting the fixed placeholder only when it reduces token count; if still oversized, the unchanged messages return to the later turn-budget check. Original request and validation feedback remain; the removed response is not reachable through a dereferenceable pointer. This bounds what the model sees without creating a durable summary. Diagnostics are a separate store; their mere persistence does not show model reload. SRC-1, `internal/provider/assessor/remember.go`; exact placeholder also appears in the supplied object's passage.

Session regeneration differs: original messages plus new validation correction omit prior invalid response text entirely ([RT-RTE-session-intake](runtime.md#rt-rte-session-intake)). Assessment, extraction/linking and organization resemble isolated call frames: selected inputs enter, parsed output escapes, full provider dialogue does not become the enclosing host conversation. The analogy stops at value delivery: no host-window reference semantics or host compaction/reload are supplied.

#### On [RT-RTE-recall-context](runtime.md#rt-rte-recall-context)

Read-back direction is caller-requested: code performs targeted selection within that request, not unsolicited push into host context. Inputs include query/vector, known evidence/relationship IDs, temporal filters, space branches and expansion IDs. `Retrieval` obtains the active contract, overfetches candidates, fuses branches, hydrates permitted IDs, applies organization/group filtering and returns a bounded list; relationship selection skips repeated semantic group keys. Constants give overfetch multiple six/floor sixty and reciprocal-rank-fusion constant sixty. Source search of normalization shows evidence default ten/max fifty and related-relationship default five/max twenty; community bounds are separate. These are result/candidate counts, not a demonstrated total host token budget. SRC-1, `internal/recall/retrieval.go`, `internal/recall/recall.go`.

Hydration can change the producer's apparent output: current/quarantined/lifecycle/source-revision rules filter support; historical valid/known-time queries can expose some superseded states. A failed vector does not necessarily remove lexical evidence. Returned evidence contains original fragment content while semantic projections/community paths are derived. Source guidance's verification requirement is advisory at the host. Private branch graph/community exclusions remain as supplied. Detailed fusion branches and every historical helper were not fully read: no complete ranking, temporal consistency or freshness guarantee. SRC-1, `internal/recall/postgres/recall_repository.go`; degradations and host guidance have passages in the supplied route.

#### On [RT-RTE-ontology-maintenance](runtime.md#rt-rte-ontology-maintenance)

Publication creates definitions, assignments/groups and dependencies, not provider parameter updates. [MEM-OBJ-ontology-records](#mem-obj-ontology-records) reaches later organizer and recall consumers; [MEM-OBJ-organization-receipt](#mem-obj-organization-receipt) retains bounded outcomes/reasons/accounting. Added direct read shows organization context selects source-linked records, forced definitions from current assignments/overrides, then forced/exact/lexical candidates under dependency bounds. Thus it is targeted model context, not arbitrary whole-store injection. Read-back uses current views and can flag stale ontology. Automatic admission remains software/model without per-item manager approval; initial vocabulary seeding and complete rejection/rollback semantics remain uninspected. SRC-1, `internal/ontology/postgres/organization.go`, `internal/ontology/postgres/recall.go`, `internal/ontology/contract/organization.go`.

#### On [RT-RTE-manager-publication](runtime.md#rt-rte-manager-publication)

Edits can replace definition text or symbolic assignments/groups/overrides. This is material editing/adoption under manager role plus repository validation, not proof of human authorship. Published record revisions affect later organization/recall; unpublished drafts are not established as recall authority. Publication reason/rollback identity are structured lineage fields in the contract; complete rollback eligibility is still uninspected. SRC-1, `internal/ontology/contract/types.go`; supplied route establishes draft/publish/discard and role/audit controls. The same store has automatic writers, so manager gating cannot be generalized to all organization.

#### On [RT-RTE-conflict-review](runtime.md#rt-rte-conflict-review)

[MEM-OBJ-conflict-derivation](#mem-obj-conflict-derivation) qualifies the route's derived-evidence statement. The fixed deletion-only fragment is audit/recovery input with inferred-authority metadata, no required vector and an explicit recall exclusion. Its retained selected-position/target lineage explains which withdrawal occurred; it is not the verifier's factual argument. Semantic resolutions affect later eligible relationships, but derivation presence alone cannot justify a new relationship. Full conflict assessment reasons and all resolution-plan consumers remain uninspected. SRC-1, `internal/knowledge/postgres/conflict_derived_evidence_task_repository.go`, `internal/recall/postgres/recall_repository.go`.

#### On [RT-RTE-evaluation-suite](runtime.md#rt-rte-evaluation-suite)

Retained local mapping/checkpoints are symbolic corpus-to-evidence identity and completion state; saved recall traces are operational result records. Runner source search confirms loaded traces/mapping can feed scoring without live recall; resume considers a source document complete when checkpoint membership has mapped evidence. Run artifacts include knowledge mapping, traces, scores and summary. These later consumers establish replay/measurement, not automatic admission of a revised retrieval policy. The qrel oracle is evaluation input, not provider judgment. Exact trace schema, import transformation and checkpoint completeness remain uninspected. SRC-1, `internal/evalharness/runner.go`; scoring/build exclusion passage in the supplied route. Ignored full datasets/run artifacts remain unavailable, preventing reproduced outcome claims.

#### On [RT-RTE-skill-export](runtime.md#rt-rte-skill-export)

This is an afforded memory-to-instruction transformation: requested recall → host distillation → proposed portable markdown → requested review. It differs from [MEM-RTE-trace-export](#mem-rte-trace-export), whose JSON pack has an inspected service implementation. The prompt alone does not establish persisted skill, installed instruction authority or an automatic trace-fed write. Its prohibition on automatic import and review requirement are guidance at the host, not a veto over all host tools. Evidence and quotation supplied in the route, SRC-1, `internal/promptcatalog/prompts/export_memory_as_agent_skill.md`.

## Write side

The write mechanisms are not one admission gate. Direct Remember has caller-authored input, model interpretation and fenced code commit; session intake has earlier raw staging, checkpoint saves and a later semantic transaction. Correction/retraction are explicit caller edits under lifecycle checks. Ontology has automatic proposals and separate manager publication. Search repair and community projection automatically admit derived access state under their own repository contracts. Private erasure has acknowledgement/policy/hold/fence controls; feedback has optional recording, scope/reference validation and pruning. The coverage table and records keep each mechanism's authorship, admission and physical storage separate.

Rejection leaves different retained results. Direct Remember terminal failure/replay is not accepted knowledge ([RT-RTE-remember-intake](runtime.md#rt-rte-remember-intake)); session failed/security-bearing extraction can leave staged raw/checkpoint/receipt state without semantic admission ([MEM-OBJ-extraction-checkpoints](#mem-obj-extraction-checkpoints)). Ontology keeps attempt/outcome receipts, while active operational records control recall. Conflict review can fall back after abstention, so rejection of a model answer is not necessarily no state change ([RT-RTE-conflict-review](runtime.md#rt-rte-conflict-review)). Retraction revokes effective support and changes search eligibility; private erasure physically deletes owned rows and scrubs audit content. Exported copies are not within that database withdrawal path.

No inspected transformation trains provider parameters. Durable source text, extracted semantics, definitions and symbolic selection metadata can nevertheless shape later decisions. Their reasons have unequal persistence: session citations retain exact source spans; lifecycle records retain reasons/targets; organization receipts retain bounded outcome and ambiguity reasons; direct assessment history exists separately from the terminal result; conflict derivation is a fixed audit statement. Later recall consumes eligible content/operational organization, not necessarily these reasons. A stored explanation without a traced reader is not claimed as later behavioral authority. No reliable factual truth, exercised learning or successful improvement follows from these writes alone.

## Read-back

Requested semantic recall, requested handle-based trace/export, requested administrative views and automatic background reads are distinct. Recall is a pull route even though code automatically ranks/expands within a request. No inspected automatic unsolicited insertion into a host conversation is established. Background organization/projectors select store state for their own next invocation; they do not establish host prompt assembly. Checkpoint/terminal-result replay is recovery read-back, not new evidence acquisition. Evaluation trace/mapping replay and control feedback readers are later consumers even without a semantic-memory update.

Working context is bounded at several stages: caller input/schema limits; server-prepared assessor candidates; token checks/assistant-history substitution; session windows/prior-event selection, regeneration and cited-segment linking; organization dependency/vocabulary/turn budgets; recall candidate/result limits; and trace/export truncation. Removed assistant turns are not summarized or reloadable through the placeholder. Omitted session events remain in durable raw storage and may be selected by a later intake under its own scope; the current frame does not get an unbounded reload capability. Host post-recall packing, compaction and response selection remain outside this source controller. See the annotations for the actual selectors, retained parts and channels rather than inferring them from API names.

## Integration issues

- **Qualification to supplied conflict retention:** [RT-RTE-conflict-review](runtime.md#rt-rte-conflict-review) says derived evidence tasks reach later knowledge consumers. [MEM-OBJ-conflict-derivation](#mem-obj-conflict-derivation) shows this payload is deletion-only audit input without required vector projection and is excluded from recall hydration. Preserve the semantic resolution's effect, but do not classify the fixed derived fragment as new factual support. Evidence: SRC-1, `internal/knowledge/postgres/conflict_derived_evidence_task_repository.go`, `internal/recall/postgres/recall_repository.go`.
- **Record identity:** no duplicate declarations are intended. Session raw/checkpoint objects, organization receipt and conflict derivation are explicit parts of supplied routes, not competing routes. Persistent evidence, relationship, search and ontology objects span supplied producer/consumer routes. New lifecycle/erasure/trace-feedback/projection/admin routes fill separate entry points, not replacements for Remember, recall, ontology organization or the evaluator. [MEM-BAP-organization-selection](#mem-bap-organization-selection) is software/model selection before delivery, not the advisory [RT-BAP-discovery-guidance](runtime.md#rt-bap-discovery-guidance). No possible-duplicate record remains after this comparison.
- **Grounding and duplicate lineage uncertainty:** complete window construction/validator, canonicalization and source-revision helpers are available but not fully inspected. The evidence-span witness supports exact retained session excerpts, not universal claim entailment or perfect duplicate/source identity. Concerns [MEM-OBJ-evidence-fragments](#mem-obj-evidence-fragments), [MEM-OBJ-extraction-checkpoints](#mem-obj-extraction-checkpoints), [RT-RTE-session-intake](runtime.md#rt-rte-session-intake).
- **Freshness/reversal uncertainty:** service-level ontology current checks, source-change failures and forwarded projection fences do not establish every repository publication/rollback/reconciliation race. Full transactional auditing remains outside performed reads. Concerns [MEM-OBJ-ontology-records](#mem-obj-ontology-records), [MEM-RTE-derived-projections](#mem-rte-derived-projections), [RT-RTE-manager-publication](runtime.md#rt-rte-manager-publication), [MEM-RTE-lifecycle-changes](#mem-rte-lifecycle-changes). Do not integrate a universal stale-free or undo guarantee.
- **Retained reasons versus consumers:** full diagnostic purger/display, conflict-resolution-plan reasons and historical payload provenance are uninspected. Existing reasons/provenance do not establish that later model calls read all rationale. Concerns [MEM-OBJ-organization-receipt](#mem-obj-organization-receipt), [MEM-OBJ-conflict-derivation](#mem-obj-conflict-derivation), [MEM-RTE-administrative-views](#mem-rte-administrative-views), [RT-OBJ-assessment-session](runtime.md#rt-obj-assessment-session).
- **Display/feedback uncertainty:** production feedback composition does not supply the optional resolver. Full browser transformations and direct SQL authorization remain uninspected; current-content resolution and complete display must not be inferred from the interface. Concerns [MEM-RTE-feedback-recording](#mem-rte-feedback-recording), [MEM-RTE-trace-export](#mem-rte-trace-export), [MEM-RTE-administrative-views](#mem-rte-administrative-views).
- **Erasure scope and evidence:** manifest/generation transaction is inspected, not executed; detailed retention/manifest validation and external copies are not established. Keep queued/completed, logical retraction and physical erasure separate. Concerns [MEM-RTE-private-erasure](#mem-rte-private-erasure), [MEM-RTE-lifecycle-changes](#mem-rte-lifecycle-changes).
- **Operation/benefit boundary:** host adoption, benchmark artifact provenance and all actual provider/runtime behavior remain unobserved. This prevents exercised learning or benefit claims, not the architectural read-back mechanisms established here. Concerns [RT-RTE-evaluation-suite](runtime.md#rt-rte-evaluation-suite), [RT-RTE-skill-export](runtime.md#rt-rte-skill-export), [RT-RTE-recall-context](runtime.md#rt-rte-recall-context).

## Limitations and checks

The source checkout HEAD matched the supplied full revision and `git status --short` was empty at opening inspection. All additional cited files belong to SRC-1; no other source or prior analysis was used. The supplied invocation, member types, collection, worker rules and record contract were read completely, including continuation reads. Only assigned outputs/identity were written. Method identity is the supplied invocation and local contracts; no independent method-commit identifier was supplied, and none is inferred.

This is a source-grounded mechanism account, not a complete database, security, release, migration or historical-consistency audit. The coverage inventory retains available-but-uninspected operative detail beside the conclusion it prevents. No runtime observation or intervention closes delivery-to-activation-to-benefit. No evidenced-absence record is declared from search misses. The required `commonplace-run validate-output` invocation passed: “Member content check passes; invocation residue not checked.” This establishes neither claim support nor job acceptance.
