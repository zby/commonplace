---
type: agentic-systems/types/agentic-system-reconciliation-report.md
description: Reconciliation of instinctual-memory records at 6acb13dc35765bf5ccfc87e445dd09c480f1c28a
run-id: AAS-2026-10-02-instinctual-memory-02
reviewed-boundary: 6acb13dc35765bf5ccfc87e445dd09c480f1c28a
---

# instinctual-memory reconciliation

## Reconciliation

The members share SRC-1 and SRC-2 at the frozen commit. Implementation findings remain wired; no supplied run or experiment establishes operation, host activation, improved capacity, extraction fidelity or causal retrieval benefit. Epistemic architectural status `implemented` and runtime conclusion status `wired` describe compatible evidence layers. Neither upgrades operation to observed.

### Record identity and ownership

The memory member declares no new records. Its annotations attach memory fields to the runtime inventory without duplicating identity. EPI-OBJ-1 is a transient proposal before admission, distinct from published OBJ-1 and source OBJ-2. EPI-OBJ-2 is a transient tidy finding, distinct from its assessed fact and subsequently retained suppression. EPI-OBJ-3 is an evaluation rubric/report, distinct from searched content. EPI-OBJ-4 and EPI-RTE-1 concern timing, distinct from RTE-11's content rubric. No duplicate supersession is warranted.

OBJ-1 remains the composite Git snapshot. Its materially different parts are assessed separately: statements supply knowledge/instruction and ranking inputs; provenance supplies source attribution; controls supply validation and enforced vetoes; checkpoint position supplies routing; dispositions and receipts record operational outcomes. The memory annotation and epistemic inventory already distinguish those parts and consumers. The proposed split is resolved by retaining the composite identity with these separate part assessments, rather than creating undeclared replacement records. In particular, disposition `accepted` is not a statement-truth endorsement or inserted-fact count: the RTE-3 ledger's placement and accounting passages show that a proposal can be dropped before its event is marked accepted. SRC-1: `src/consolidate.rs`.

OBJ-3 likewise retains its composite integration identity, with accumulated exports and delivered retained preferences distinguished from static setup configuration and shipped skill text. RTE-8 has separate setup and writeback parts. Only accumulated content and its later-consumer routes enter the memory comparison scope; installation files and model machinery do not.

Runtime owns the canonical progression and admission fields of RTE-2, RTE-3, RTE-4, RTE-6, RTE-7, RTE-8 and RTE-10. The memory annotations preserve their trigger, producer, admission/rejection, recovery, proposal guidance and persistence while adding memory-specific selection and transformation fields. No new memory route requires a second admission trace. RTE-3's rules generation, model generation, occurrence/shape checking, placement, retention and file-lineage retirement retain their separate ledger functions and evaluator scopes. RTE-4's diagnosis and application remain separately assessed below. Shared ownership does not merge checking with disposition, retention with lifecycle integration, or advisory findings with applied withdrawal.

### Amendments and integration dispositions

Amendment: RTE-4's description of duplicate/session-only diagnosis as wholly deterministic, and its theory account's reference to deterministic session-only patterns, are replaced by deterministic overlap-based duplicate diagnosis plus optional CMP-1-configured model session-only judgment through `chat_json` and `JUDGE_PROMPT`. Code proposes duplicate findings; the configured model proposes session-only IDs; code maps those IDs to live facts; operator `--apply` and `--keep` determine withdrawal; validator/CAS can reject publication. Without model configuration the session-only branch is skipped. This corrects the runtime account and the memory annotation's blanket deterministic wording. It changes neither supported dedup/invalidate values nor evidence of cleanup utility. Evidence: SRC-1 `src/tidy.rs`; the epistemic ledger's retained model-judgment passage and EPI-OBJ-2. Affected findings: RTE-4 diagnosis roles and theory guidance; RTE-3 remains the separate extraction route.

Amendment: CMP-1's extractor-only consumer description is extended to its same `LlmConfig` configuration used for RTE-4's session-only judge under a different prompt. Its unpinned configuration, mutable endpoint and uninspected provider parameters remain unchanged. Evidence: SRC-1 `src/tidy.rs`, `src/consolidate.rs`; RTE-4 model-judgment passage in the epistemic ledger. Affected findings: RTE-4 evaluator identity and CMP-1 use scope, without claiming that both invocations resolve identical immutable weights.

Amendment: RTE-8's writeback selection of “current active” facts is replaced by project/entity selection, exclusion of Superseded/Retracted/Expired enum statuses, visibility allowance and default omission of file-only sources. It does not call temporal eligibility or consult controls and can include Disputed or temporally expired facts whose enum status remains Active. Setup admission and recovery are unchanged. Evidence: SRC-1 `src/cli.rs`, `src/fact.rs`; retained writeback passage in the memory annotation on RTE-8. Affected findings: OBJ-3 exported content eligibility, RTE-8 selection and the epistemic rendering ledger. Existing exports also lack automatic retraction after later withdrawal.

Amendment: RTE-2 and RTE-3's unqualified “no TTL” statements are narrowed to ordinary inspected producers leaving expiry unset and the absence of a general automatic expiry assignment. RTE-1's curated lexical search applies `expires_at` and `valid_to` through `Fact::is_eligible` when populated; public Fact/change surfaces permit such fields. Evidence: SRC-1 `src/fact.rs`, `src/change.rs`, `src/lib.rs`; memory annotation on RTE-1 retains the temporal gate, and the epistemic RTE-3 placement passage retains unset temporal fields. Affected findings: OBJ-1 temporal metadata, RTE-1 consumer eligibility and conditional decay. No universal decay or universal read-path enforcement follows.

Amendment: RTE-5's generic “current curated fact eligibility” selection field is replaced by two predicates: SessionStart uses active-fact availability and `memory_read` of `pref_user`, whose entity response selects Active enum status; UserPromptSubmit uses facts-only lexical search and meaningful-term overlap. Startup preference reading does not apply search's temporal/controls gate. Individual fact reads and history are also separate from lexical eligibility. Evidence: SRC-1 `src/hook.rs`, `src/ops.rs`; the memory annotation on RTE-5 retains the identifier call, and the following generated passage retains the entity predicate. Affected findings: RTE-5 invalidation scope, RTE-1 requested-read scope, and RTE-2/RTE-4 epistemic descriptions of enforced withdrawal: enforcement is consumer-specific, rather than every read rejecting all withdrawn or expired content.

> let facts: Vec<Value> = found
>                     .facts
>                     .iter()
>                     .filter(|fact| fact.status == FactStatus::Active)
>                     .map(|fact| json!({"id": fact.id, "statement": fact.statement}))
>                     .collect();
> --- `src/ops.rs:270-275` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Amendment: RTE-10's “local transcript/file ingestion” trigger/input summary is extended to included calendar and timestamped voice adapters. These original event-stream contents become Note candidates on RTE-3; imported project files remain imported static content, and tool-role IDE events do not qualify as trace-learning inputs on the inspected extractors. Evidence: SRC-1 `src/ingest.rs`, `src/consolidate.rs`; memory annotations on OBJ-2 and RTE-3 retain calendar/voice and role-selection passages. Affected findings: OBJ-2 acquired content and RTE-3 trace-source coverage. Journal serialization alone does not create event-stream lineage.

The opaque model-content integration issue remains a scoped coverage limit, not a conflicting positive finding. Occurrence, lexical overlap, structural validity and publication do not establish semantic faithfulness. No member establishes content-directed revision of extraction/cleanup method texts or a retained criticism cycle. RTE-3 checkpoint iteration is operational iteration; RTE-11 and EPI-RTE-1 return reports without an implemented retained policy-update route.

### Memory comparison cross-check

The memory member's profile remains authoritative, including its scope, per-value bases and records, notes and uncertainties. The following checks do not create another profile or strengthen any value.

| Axis | Disposition against the whole set |
|---|---|
| storage_substrate | Known files/repo fit OBJ-1, OBJ-2, OBJ-3's accumulated export part and OBJ-4. Transient EPI-OBJ-1, EPI-OBJ-2, EPI-OBJ-3 and EPI-OBJ-4 do not add scoped stores. |
| representational_form | Known natural-language/symbolic fit statements, source text, tasks and access metadata. CMP-1, CMP-2 and CMP-3 are excluded machinery, not accumulated parametric memory. |
| lineage | Authored, imported, trace-extracted and other-compiled have distinct supported witnesses. Epistemic acquisition and rendering entries add no missing retained lineage. |
| behavioral_authority | Knowledge, instruction, learning, ranking, routing, validation and enforcement retain their named consumer scopes. Advisory host delivery remains separate from local vetoes; the amendments narrow enforcement by read path. |
| write_agency | Manual content authoring and automatic acquisition/transformation coexist. Operator initiation does not turn automatic extraction into manual writing. |
| curation_operations | Partial consolidate/dedup/evolve/invalidate/decay remains supported. The RTE-4 correction preserves duplicate dedup and applied withdrawal while exposing its separate model judge. Epistemic indeterminate transformation labels do not establish missing synthesis or invalidate deterministic consolidation witnesses. Conditional decay applies to lexical search. |
| read_back_direction | Known pull/push matches requested reads and automatic hook supply. RTE-8 export is requested; later external startup consumption remains afforded, not observed. |
| read_back_signal | Known coarse/identifier/inferred-lexical matches RTE-5's availability, pref_user match and prompt overlap. CMP-2/CMP-3 judgment belongs to requested pull, not another push signal. |
| trace_learning | Known yes, wired, follows OBJ-2 → RTE-3 → OBJ-1 → later RTE-1/RTE-5. Epistemic semantic uncertainty prevents warrant/benefit claims, not this automatic durable-write classification. |
| trace_source | Known session-logs/event-streams follows user turns and qualifying calendar/voice Note content. Tool-role traces remain excluded from inspected extraction; journal packaging adds no source value. |

Every epistemic record and retained-content transformation was checked: EPI-OBJ-1 participates in RTE-3's durable-write chain; EPI-OBJ-2's applied result is retained withdrawal state; EPI-OBJ-3 and EPI-OBJ-4 remain temporary reference/measurement artifacts; EPI-RTE-1 retains no later-consumed report. File-lineage retirement, authored replacement, forget/tidy withdrawal, erasure, hook/export reshaping and task mutation fit the memory member's existing scope and classifications. Model-family administration remains excluded machinery. No additional profile value is established by those records.

Agreement among members is shared-route corroboration, not independent convergence: both specialists received runtime findings, and some passages overlap. There are no duplicate declarations to supersede, no unresolved anchored conflict, and no finding requiring return to the memory analyst. Remaining uncertainty prevents semantic-completeness, host-activation, benefit and theory-builder conclusions within the named boundary.
