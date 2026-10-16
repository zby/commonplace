---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'SAGE memory comparison: governed content, retrieval representations, admission feedback,
  hook context, operator preferences and local Messages at the frozen boundary.'
run-id: AAS-2026-10-15-sage-d3843de6d2dd-01
source-identity: https://github.com/l33tdawg/sage
reviewed-boundary: e2e0242a421afbd356ed135d7d754a35b0ad5f14
memory-comparison:
  version: 2
  scope: 'Included: accumulated governed memory text/envelopes and indexes; relationships; local evidence,
    verdict and operator-review state; capture units/progress; validator feedback; imported and federated
    copies; boot preferences and cleanup continuation; benchmark retained text/results; exact-local Messages
    and unresolved task-board, pipeline/history, recovery and removal alternatives. Excluded: shipped
    static instructions as memory objects, external model weights, host-owned conversation/compaction
    policy, transient current-call scores and binary installation state unrelated to this memory boundary.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Canonical memory envelopes, scoped content and validator feedback state
        assessment: known
        findings:
        - value: kv
          basis: wired
          records: &id001
          - memory.md#mem-obj-memory-record
          - memory.md#mem-obj-validator-stats
          note: Badger retains canonical state and numerical validator statistics.
        records: *id001
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Personal-node content, gate evidence/verdict/review, links and exact-local Messages
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records: &id002
          - memory.md#mem-obj-memory-record
          - memory.md#mem-obj-gate-material
          - memory.md#mem-obj-review-decision
          - memory.md#mem-obj-memory-relationships
          - workflow.md#wf-rte-local-exchange
          note: SQLite retains these separately consumed parts; relationship structure is not proof of
            a separate graph storage engine.
        records: *id002
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Daemon memory serving records
        assessment: partial
        findings:
        - value: rdbms
          basis: wired
          records: &id003
          - memory.md#mem-obj-memory-record
          - runtime.md#rt-rte-memory-admission
          note: The shipped daemon uses PostgreSQL; full parity with SQLite paths remains uninspected.
        records: *id003
        note: The daemon substrate is established, but versioned serving/projection alternatives are not
          exhaustively covered.
      - scope: Retained dense-vector retrieval index
        assessment: known
        findings:
        - value: vector
          basis: wired
          records: &id004
          - memory.md#mem-obj-memory-indexes
          - memory.md#mem-rte-reembed-index
          note: SQL-retained embeddings form the operative vector-search representation.
        - value: sqlite
          basis: wired
          records: *id004
          note: The inspected retained index and search implementation reside in SQLite.
        records: *id004
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Per-thread capture progress sidecars
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id005
          - memory.md#mem-obj-capture-progress
          note: Local per-thread progress files survive capture attempts and drive retries.
        records: *id005
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Benchmark retained result output
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id006
          - memory.md#mem-rte-evaluation-readback
          - epistemic.md#epi-rte-benchmark-check
          note: Per-question results are aggregated and written as JSON for later reporting.
        records: *id006
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Boot preferences and cleanup continuation state
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-boot-instructions
        - runtime.md#rt-rte-maintenance-cleanup
        note: Persistence is established, but these records name a preference store and durable run state
          without resolving a controlled physical substrate for each.
      - scope: Included task-board, pipeline/history and federation removal/recovery alternatives beyond
          the inspected exact-local Messages path
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-record
        - memory.md#mem-obj-memory-relationships
        - memory.md#mem-rte-sync-copy
        - workflow.md#wf-rte-local-exchange
        note: Memory coverage and integration issues leave these operative families incompletely traced.
          Exact-local Messages resolves only its own branch; complete storage substrate classification
          is prevented.
      records:
      - memory.md#mem-obj-memory-record
      - memory.md#mem-obj-validator-stats
      - memory.md#mem-obj-gate-material
      - memory.md#mem-obj-review-decision
      - memory.md#mem-obj-memory-relationships
      - workflow.md#wf-rte-local-exchange
      - runtime.md#rt-rte-memory-admission
      - memory.md#mem-obj-memory-indexes
      - memory.md#mem-rte-reembed-index
      - memory.md#mem-obj-capture-progress
      - memory.md#mem-rte-evaluation-readback
      - epistemic.md#epi-rte-benchmark-check
      - runtime.md#rt-obj-boot-instructions
      - runtime.md#rt-rte-maintenance-cleanup
      - memory.md#mem-rte-sync-copy
      note: Known retained substrates coexist with unresolved preference/run storage and included recovery/coordination
        alternatives. External inference weights and current-call transient scores are excluded, not classified
        as accumulated memory.
    representational_form:
      assessment: partial
      units:
      - scope: Readable memory, imported material, captured conversational text, message payload/results,
          boot text and gate reasons/evidence
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id007
          - memory.md#mem-obj-memory-record
          - memory.md#mem-obj-capture-unit
          - memory.md#mem-obj-gate-material
          - runtime.md#rt-obj-boot-instructions
          - workflow.md#wf-rte-local-exchange
          note: Models or humans interpret retained prose; encoded capture headers and message identities
            are separate parts.
        records: *id007
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Memory metadata, relationships, gate decisions, capture bookkeeping, cleanup intent and
          message ownership/replay state
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id008
          - memory.md#mem-obj-memory-record
          - memory.md#mem-obj-memory-relationships
          - memory.md#mem-obj-review-decision
          - memory.md#mem-obj-capture-progress
          - runtime.md#rt-rte-maintenance-cleanup
          - workflow.md#wf-rte-local-exchange
          note: Localized identifiers, enums, counters and fixed rules govern code consumers.
        records: *id008
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Retained numerical validator feedback
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id009
          - memory.md#mem-obj-validator-stats
          - memory.md#mem-rte-verdict-feedback
          note: Counters and EWMA accumulators are fixed-rule numerical state, not distributed model parameters.
        records: *id009
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Dense retrieval embeddings
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: &id010
          - memory.md#mem-obj-memory-indexes
          note: Dense numerical representations support semantic retrieval; readable memory content is
            not itself an embedding.
        records: *id010
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Included task-board, pipeline/history and federation removal/recovery alternatives beyond
          the inspected exact-local Messages path
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-record
        - memory.md#mem-obj-memory-relationships
        - memory.md#mem-rte-sync-copy
        - workflow.md#wf-rte-local-exchange
        note: Memory coverage and integration issues leave these operative families incompletely traced.
          Exact-local Messages resolves only its own branch; complete representational form classification
          is prevented.
      records:
      - memory.md#mem-obj-memory-record
      - memory.md#mem-obj-capture-unit
      - memory.md#mem-obj-gate-material
      - runtime.md#rt-obj-boot-instructions
      - workflow.md#wf-rte-local-exchange
      - memory.md#mem-obj-memory-relationships
      - memory.md#mem-obj-review-decision
      - memory.md#mem-obj-capture-progress
      - runtime.md#rt-rte-maintenance-cleanup
      - memory.md#mem-obj-validator-stats
      - memory.md#mem-rte-verdict-feedback
      - memory.md#mem-obj-memory-indexes
      - memory.md#mem-rte-sync-copy
      note: Mixed text, code-interpreted state and dense representations are split by consumption. Untraced
        families prevent a complete inventory; external weights are not retained memory writes.
    lineage:
      assessment: partial
      units:
      - scope: Explicit caller prose, relationships and operator guidance/review
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id011
          - memory.md#mem-obj-memory-record
          - memory.md#mem-obj-memory-relationships
          - memory.md#mem-obj-review-decision
          - runtime.md#rt-rte-boot-guidance
          note: Callers supply assertions/relationships; operators supply boot text and semantic decisions.
            Authored does not mean human-authored for generic callers.
        records: *id011
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: File imports, federated copied content and benchmark-seeded session material
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id012
          - memory.md#mem-rte-import-material
          - memory.md#mem-rte-sync-copy
          - memory.md#mem-rte-evaluation-readback
          note: External content is parsed, seeded or copied into local memory; import does not establish
            source truth.
        records: *id012
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Selected conversational capture and generated outcome lessons
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id013
          - memory.md#mem-obj-capture-unit
          - runtime.md#rt-rte-bridge-distillation
          note: Capture selects transcript text; the bridge automatically generates observations from
            challenge/outcome data.
        records: *id013
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Embeddings, capture progress, fixed session event text, verdicts and validator statistics
          derived by software/model
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id014
          - memory.md#mem-obj-memory-indexes
          - memory.md#mem-obj-capture-progress
          - memory.md#mem-rte-session-lifecycle
          - epistemic.md#epi-obj-semantic-verdict
          - memory.md#mem-rte-verdict-feedback
          note: These retained representations/decisions are computed from content, attempts, events or
            votes rather than copied as supplied prose.
        records: *id014
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Existing deployed content and legacy initial embeddings
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-record
        - memory.md#mem-obj-memory-indexes
        note: No deployed content initialization is supplied; empty legacy embedding stamps leave initial
          provenance unresolved. Known later re-embedding does not repair that historical gap.
      - scope: Included task-board, pipeline/history and federation removal/recovery alternatives beyond
          the inspected exact-local Messages path
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-record
        - memory.md#mem-obj-memory-relationships
        - memory.md#mem-rte-sync-copy
        - workflow.md#wf-rte-local-exchange
        note: Memory coverage and integration issues leave these operative families incompletely traced.
          Exact-local Messages resolves only its own branch; complete lineage classification is prevented.
      records:
      - memory.md#mem-obj-memory-record
      - memory.md#mem-obj-memory-relationships
      - memory.md#mem-obj-review-decision
      - runtime.md#rt-rte-boot-guidance
      - memory.md#mem-rte-import-material
      - memory.md#mem-rte-sync-copy
      - memory.md#mem-rte-evaluation-readback
      - memory.md#mem-obj-capture-unit
      - runtime.md#rt-rte-bridge-distillation
      - memory.md#mem-obj-memory-indexes
      - memory.md#mem-obj-capture-progress
      - memory.md#mem-rte-session-lifecycle
      - epistemic.md#epi-obj-semantic-verdict
      - memory.md#mem-rte-verdict-feedback
      - workflow.md#wf-rte-local-exchange
      note: Supported derivation paths do not resolve unknown initial content, legacy vector provenance
        or untraced imported/recovery alternatives.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Recalled/captured prose and Messages results at foreground or benchmark answer models
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id015
          - runtime.md#rt-bap-retained-context
          - memory.md#mem-rte-evaluation-readback
          - workflow.md#wf-rte-local-exchange
          note: Retained content supplies context or untrusted data, not a grant of privileged user/system
            authority.
        records: *id015
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Operator boot text at the external inception consumer
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id016
          - runtime.md#rt-obj-boot-instructions
          - runtime.md#rt-rte-boot-guidance
          - runtime.md#rt-bap-client-guidance
          note: Saved directions are appended to later operating guidance; compliance is unobserved.
        records: *id016
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Retained content, vectors, confidence and validator statistics at retrieval/quorum scoring
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id017
          - memory.md#mem-obj-memory-indexes
          - runtime.md#rt-rte-targeted-recall
          - memory.md#mem-rte-verdict-feedback
          note: Retained vectors/text/confidence influence retrieval priority; accumulated validator factors
            influence relative vote weights.
        records: *id017
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Review enum and cached semantic verdict at Gate.Apply
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id018
          - memory.md#mem-obj-review-decision
          - epistemic.md#epi-obj-semantic-verdict
          - epistemic.md#epi-rte-semantic-disposition
          note: Stored decisions determine semantic admissibility subject to fresh baseline/scope checks.
        - value: enforcement
          basis: wired
          records: *id018
          note: Reject or hold prevents this node from supplying an accept vote; these are not direct
            all-validator controls.
        records: *id018
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Lifecycle/access metadata, sync suppression and message session/revision state at service
          checks
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id019
          - memory.md#mem-rte-lifecycle-change
          - memory.md#mem-rte-sync-copy
          - workflow.md#wf-rte-local-exchange
          note: State and identity criteria test candidate actions or deliveries.
        - value: enforcement
          basis: wired
          records: *id019
          note: Suppression, lifecycle and ownership fences reject or exclude inadmissible actions/reads.
        records: *id019
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Capture cursor, cleanup pending intent and sync recovery ledger at later workers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id020
          - memory.md#mem-obj-capture-progress
          - runtime.md#rt-rte-maintenance-cleanup
          - memory.md#mem-rte-sync-copy
          note: Retained state selects next capture windows, challenge targets or recovery operations.
        records: *id020
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Recorded vote outcomes at the statistics update consumer
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id021
          - memory.md#mem-rte-verdict-feedback
          note: Experience feedback updates durable factors that shape future quorum decisions; improved
            truth checking is not established.
        records: *id021
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Prior retained lessons at bridge proposal generation
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id022
          - runtime.md#rt-rte-bridge-distillation
          note: Prior excerpts provide context to the summary model.
        - value: learning
          basis: wired
          records: *id022
          note: The model receives prior experience while producing another durable advice proposal; no
            in-place revision or useful improvement is shown.
        records: *id022
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Task-board/triple and benchmark metric consumers beyond inspected routes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-relationships
        - memory.md#mem-obj-memory-record
        - memory.md#mem-rte-evaluation-readback
        note: Triple insertion alone supplies no traced consumer. Full task-board and production feedback
          from benchmark metrics are unresolved; unconsumed metadata is not assigned authority.
      - scope: Included task-board, pipeline/history and federation removal/recovery alternatives beyond
          the inspected exact-local Messages path
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-record
        - memory.md#mem-obj-memory-relationships
        - memory.md#mem-rte-sync-copy
        - workflow.md#wf-rte-local-exchange
        note: Memory coverage and integration issues leave these operative families incompletely traced.
          Exact-local Messages resolves only its own branch; complete behavioral authority classification
          is prevented.
      records:
      - runtime.md#rt-bap-retained-context
      - memory.md#mem-rte-evaluation-readback
      - workflow.md#wf-rte-local-exchange
      - runtime.md#rt-obj-boot-instructions
      - runtime.md#rt-rte-boot-guidance
      - runtime.md#rt-bap-client-guidance
      - memory.md#mem-obj-memory-indexes
      - runtime.md#rt-rte-targeted-recall
      - memory.md#mem-rte-verdict-feedback
      - memory.md#mem-obj-review-decision
      - epistemic.md#epi-obj-semantic-verdict
      - epistemic.md#epi-rte-semantic-disposition
      - memory.md#mem-rte-lifecycle-change
      - memory.md#mem-rte-sync-copy
      - memory.md#mem-obj-capture-progress
      - runtime.md#rt-rte-maintenance-cleanup
      - runtime.md#rt-rte-bridge-distillation
      - memory.md#mem-obj-memory-relationships
      - memory.md#mem-obj-memory-record
      note: Authority follows each consumed part and effect. Textual requests and service fences are not
        interchangeable; unresolved consumers prevent whole-system completeness.
    write_agency:
      assessment: partial
      units:
      - scope: Ordinary proposals, bridge outputs, capture units, session events, vector regeneration,
          verdict caches and statistics admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id023
          - runtime.md#rt-rte-memory-admission
          - runtime.md#rt-rte-bridge-distillation
          - runtime.md#rt-rte-hook-context
          - memory.md#mem-rte-session-lifecycle
          - memory.md#mem-rte-reembed-index
          - epistemic.md#epi-rte-lasting-check
          - memory.md#mem-rte-verdict-feedback
          note: Software/model admission requires no per-content human approval. Process consent or operator-started
            migration does not make every output manual.
        records: *id023
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Operator boot preference replacement and semantic review
        assessment: known
        findings:
        - value: manual
          basis: wired
          records: &id024
          - runtime.md#rt-rte-boot-guidance
          - memory.md#mem-obj-review-decision
          note: The operator supplies/replaces exact instruction text or explicitly approves/rejects the
            held content.
        records: *id024
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Import conversion, federated copying and local Messages protocol admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id025
          - memory.md#mem-rte-import-material
          - memory.md#mem-rte-sync-copy
          - workflow.md#wf-rte-local-exchange
          note: Software admits parsed records/copies/protocol state without a mandatory per-item human
            content decision; agreement/file selection is process-level input.
        records: *id025
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Caller-authored correction, reflection, co-commit and relationship content control
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-correction-cycle
        - memory.md#mem-rte-reflection-storage
        - runtime.md#rt-rte-co-commit
        - memory.md#mem-obj-memory-relationships
        note: Generic client identity/signatures do not distinguish explicit human content selection from
          agent authorship. Computational veto/admission is known, but manual control of these caller
          alternatives is not.
      - scope: Initial existing content and automatic provider-ready vector repair alternative
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-record
        - memory.md#mem-rte-reembed-index
        note: Deployed initialization is unavailable. The manual re-embedding lane records an automatic
          repair alternative without independently tracing its complete control path.
      - scope: Included task-board, pipeline/history and federation removal/recovery alternatives beyond
          the inspected exact-local Messages path
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-record
        - memory.md#mem-obj-memory-relationships
        - memory.md#mem-rte-sync-copy
        - workflow.md#wf-rte-local-exchange
        note: Memory coverage and integration issues leave these operative families incompletely traced.
          Exact-local Messages resolves only its own branch; complete write agency classification is prevented.
      records:
      - runtime.md#rt-rte-memory-admission
      - runtime.md#rt-rte-bridge-distillation
      - runtime.md#rt-rte-hook-context
      - memory.md#mem-rte-session-lifecycle
      - memory.md#mem-rte-reembed-index
      - epistemic.md#epi-rte-lasting-check
      - memory.md#mem-rte-verdict-feedback
      - runtime.md#rt-rte-boot-guidance
      - memory.md#mem-obj-review-decision
      - memory.md#mem-rte-import-material
      - memory.md#mem-rte-sync-copy
      - workflow.md#wf-rte-local-exchange
      - memory.md#mem-rte-correction-cycle
      - memory.md#mem-rte-reflection-storage
      - runtime.md#rt-rte-co-commit
      - memory.md#mem-obj-memory-relationships
      - memory.md#mem-obj-memory-record
      note: Automatic and explicit manual mechanisms coexist. Human workflow initiation, generic signatures
        and physical I/O do not resolve per-content control on every branch.
    curation_operations:
      assessment: partial
      units:
      - scope: Confidence aging at later retrieval
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id026
          - memory.md#mem-obj-memory-indexes
          note: Time/domain decay downweights eligible memories; open tasks have an explicit exemption.
        records: *id026
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Correction and lifecycle/cleanup withdrawal
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id027
          - memory.md#mem-rte-correction-cycle
          - memory.md#mem-rte-lifecycle-change
          - runtime.md#rt-rte-maintenance-cleanup
          note: Correction proposes changed content with parent lineage before retiring the original.
        - value: invalidate
          basis: wired
          records: *id027
          note: Canonical challenge/deprecation changes current reliance while history can remain; a challenge
            need not immediately exclude disputed content.
        records: *id027
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Selected transcript capture
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id028
          - memory.md#mem-obj-capture-unit
          - runtime.md#rt-rte-hook-context
          note: Automatic selection retains a reduced conversational-text representation, excluding tool
            bodies and metadata; it creates no new recommendation.
        records: *id028
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Reflection fact typing and salience assignment
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-reflection-storage
        note: The formatter prefixes caller DO text, assigns type/confidence and proposes a new record.
          This does not establish raising the tier or salience of already retained memory; no controlled
          curation value is established by initial proposal packaging.
      - scope: Bridge model transformation
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-bridge-distillation
        note: The model call and durable proposal path are wired, but the requested distillation and
          novelty do not establish consolidation or synthesis. Without full input/output pairs, the
          semantic transformation remains indeterminate; no controlled curation value is established.
      - scope: Dedup checks, re-embedding and graph insertion
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-baseline-check
        - memory.md#mem-rte-reembed-index
        - memory.md#mem-obj-memory-relationships
        note: Collision rejection, index regeneration and relationship insertion alone establish no controlled
          curation operation over retained claims; no merge/removal of near-duplicate retained entries
          is established.
      - scope: Included task-board, pipeline/history and federation removal/recovery alternatives beyond
          the inspected exact-local Messages path
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-record
        - memory.md#mem-obj-memory-relationships
        - memory.md#mem-rte-sync-copy
        - workflow.md#wf-rte-local-exchange
        note: Memory coverage and integration issues leave these operative families incompletely traced.
          Exact-local Messages resolves only its own branch; complete curation operations classification
          is prevented.
      records:
      - memory.md#mem-obj-memory-indexes
      - memory.md#mem-rte-correction-cycle
      - memory.md#mem-rte-lifecycle-change
      - runtime.md#rt-rte-maintenance-cleanup
      - memory.md#mem-obj-capture-unit
      - runtime.md#rt-rte-hook-context
      - memory.md#mem-rte-reflection-storage
      - runtime.md#rt-rte-bridge-distillation
      - epistemic.md#epi-rte-baseline-check
      - memory.md#mem-rte-reembed-index
      - memory.md#mem-obj-memory-relationships
      - memory.md#mem-obj-memory-record
      - memory.md#mem-rte-sync-copy
      - workflow.md#wf-rte-local-exchange
      note: Retained-content selection, correction, aging and withdrawal have separate warrants.
        Initial reflection packaging establishes no promotion of retained memory. Opaque bridge model
        semantics and untraced maintenance prevent a complete operation inventory.
    read_back_direction:
      assessment: partial
      units:
      - scope: Foreground topic/ID/list/link recall and explicit Messages inspection/result paging
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id031
          - runtime.md#rt-rte-targeted-recall
          - memory.md#mem-obj-memory-relationships
          - workflow.md#wf-rte-local-exchange
          note: The consumer explicitly requests retained content or replies; returning that request is
            not another push.
        records: *id031
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: SessionStart recent prefetch and resumed-thread reconstruction
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id032
          - runtime.md#rt-rte-hook-context
          - memory.md#mem-obj-capture-unit
          note: Host callbacks automatically select and supply retained context without a foreground memory
            request.
        records: *id032
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Bridge prior-knowledge chain
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id033
          - runtime.md#rt-rte-bridge-distillation
          note: The bridge explicitly queries stored knowledge.
        - value: push
          basis: wired
          records: *id033
          note: Its automatic prompt assembly supplies selected prior excerpts to the summary model, which
            did not request them.
        records: *id033
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Later gate, feedback and continuation workers
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id034
          - memory.md#mem-obj-review-decision
          - epistemic.md#epi-rte-semantic-disposition
          - memory.md#mem-rte-verdict-feedback
          - memory.md#mem-obj-capture-progress
          - runtime.md#rt-rte-maintenance-cleanup
          note: Code consumers explicitly load persisted decisions, factors or cursor/intent state for
            their later invocation.
        records: *id034
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Later inception guidance
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id035
          - runtime.md#rt-rte-boot-guidance
          note: Inception explicitly loads preferences.
        - value: push
          basis: wired
          records: *id035
          note: Code appends nonempty saved guidance to the returned operating instructions without a
            separate request for that custom text.
        records: *id035
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Benchmark seed-to-answer route
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id036
          - memory.md#mem-rte-evaluation-readback
          note: Harness retrieval requests seeded material.
        - value: push
          basis: wired
          records: *id036
          note: The harness automatically assembles selected retained context into the answer-model prompt.
        records: *id036
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Included task-board, pipeline/history and federation removal/recovery alternatives beyond
          the inspected exact-local Messages path
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-record
        - memory.md#mem-obj-memory-relationships
        - memory.md#mem-rte-sync-copy
        - workflow.md#wf-rte-local-exchange
        note: Memory coverage and integration issues leave these operative families incompletely traced.
          Exact-local Messages resolves only its own branch; complete read-back direction classification
          is prevented.
      records:
      - runtime.md#rt-rte-targeted-recall
      - memory.md#mem-obj-memory-relationships
      - workflow.md#wf-rte-local-exchange
      - runtime.md#rt-rte-hook-context
      - memory.md#mem-obj-capture-unit
      - runtime.md#rt-rte-bridge-distillation
      - memory.md#mem-obj-review-decision
      - epistemic.md#epi-rte-semantic-disposition
      - memory.md#mem-rte-verdict-feedback
      - memory.md#mem-obj-capture-progress
      - runtime.md#rt-rte-maintenance-cleanup
      - runtime.md#rt-rte-boot-guidance
      - memory.md#mem-rte-evaluation-readback
      - memory.md#mem-obj-memory-record
      - memory.md#mem-rte-sync-copy
      note: Requested returns and automatic downstream prompt supply are distinguished inside chains.
        Exact-local Messages adds a pull witness, not complete coordination coverage.
    read_back_signal:
      assessment: partial
      units:
      - scope: SessionStart recency prefetch
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id037
          - runtime.md#rt-rte-hook-context
          note: Trigger is SessionStart; selector uses explicit/home domain and newest committed availability,
            capped at ten 200-byte excerpts.
        records: *id037
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Resumed-thread capture push
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id038
          - runtime.md#rt-rte-hook-context
          - memory.md#mem-obj-capture-unit
          note: On resume, durable session identity and exact thread tag/domain match select delivered
            captured units; sequence/part reconstruction follows the match.
        records: *id038
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Bridge automatic prior-excerpt supply
        assessment: partial
        findings:
        - value: coarse
          basis: wired
          records: &id039
          - runtime.md#rt-rte-bridge-distillation
          - runtime.md#rt-rte-targeted-recall
          note: Bridge query/domain selects up to five committed prior items and bounds each excerpt.
        records: *id039
        note: Domain and item bounds are established. The accepted bridge record does not resolve every
          search mode behind query_knowledge; inferred embedding/lexical selection cannot be upgraded
          from another recall witness.
      - scope: Inception custom boot guidance
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id040
          - runtime.md#rt-rte-boot-guidance
          note: Later initialized inception includes available nonempty custom text; this is availability-conditioned
            supply, not targeted identifier matching to delivered knowledge parts.
        records: *id040
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Benchmark answer-prompt supply
        assessment: partial
        findings:
        - value: coarse
          basis: wired
          records: &id041
          - memory.md#mem-rte-evaluation-readback
          note: Dataset/run domain and top-K bound retained context assembled for the answer model.
        records: *id041
        note: The chain has embedding and optional query expansion, but records do not fully isolate every
          alternative selector in downstream prompt supply; question/reference IDs alone do not establish
          identifier-targeted push.
      - scope: Explicit requested foreground/relationship/Message reads
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-targeted-recall
        - memory.md#mem-obj-memory-relationships
        - workflow.md#wf-rte-local-exchange
        note: These specifically named delivery operations fulfill consumer requests. Their embedding/lexical/identifier
          selectors are pull selectors, not positive push signals.
      - scope: Included task-board, pipeline/history and federation removal/recovery alternatives beyond
          the inspected exact-local Messages path
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-record
        - memory.md#mem-obj-memory-relationships
        - memory.md#mem-rte-sync-copy
        - workflow.md#wf-rte-local-exchange
        note: Memory coverage and integration issues leave these operative families incompletely traced.
          Exact-local Messages resolves only its own branch; complete push selection signal classification
          is prevented.
      records:
      - runtime.md#rt-rte-hook-context
      - memory.md#mem-obj-capture-unit
      - runtime.md#rt-rte-bridge-distillation
      - runtime.md#rt-rte-targeted-recall
      - runtime.md#rt-rte-boot-guidance
      - memory.md#mem-rte-evaluation-readback
      - memory.md#mem-obj-memory-relationships
      - workflow.md#wf-rte-local-exchange
      - memory.md#mem-obj-memory-record
      - memory.md#mem-rte-sync-copy
      note: Positive unsolicited selectors coexist with unresolved automatic prompt-selection alternatives;
        known pull routes cannot make the whole axis inapplicable.
    trace_learning:
      assessment: partial
      units:
      - scope: Consensus vote feedback to durable quorum factors
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id042
          - memory.md#mem-rte-verdict-feedback
          - memory.md#mem-obj-validator-stats
          note: Recorded votes and terminal outcomes automatically update retained statistics consumed
            by later quorum weighting; no improved correctness is implied.
        records: *id042
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Bridge outcome-to-advice-to-later-context chain
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id043
          - runtime.md#rt-rte-bridge-distillation
          - runtime.md#rt-bap-retained-context
          note: Outcome/challenge experience feeds automatic durable observation proposals; admitted outputs
            reach later query and summary consumers without per-output human review.
        records: *id043
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Capture selection/encoding and reconstructed trace context
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-capture-unit
        - runtime.md#rt-rte-hook-context
        note: Records establish selected conversational text re-encoding/reconstruction, not a derived
          recommendation or generated continuation summary. Raw retention alone establishes no yes; no
          canonical bounded-absence record is declared to warrant a controlled no.
      - scope: Caller reflection and SessionEnd event recording
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-reflection-storage
        - memory.md#mem-rte-session-lifecycle
        note: Reflection receives already-authored text without a traced original activity-to-generation
          chain. SessionEnd retains fixed event text without a derived behavior-shaping update. These
          records do not establish a qualifying trace-fed learning value for the broader alternatives.
      - scope: Task/history, benchmark production feedback and recovery alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-record
        - memory.md#mem-rte-evaluation-readback
        - workflow.md#wf-rte-local-exchange
        note: Messages retains raw requests/results, not an established learning update. Other included
          history/task and production-feedback consumers remain untraced; no system-wide negative follows.
      records:
      - memory.md#mem-rte-verdict-feedback
      - memory.md#mem-obj-validator-stats
      - runtime.md#rt-rte-bridge-distillation
      - runtime.md#rt-bap-retained-context
      - memory.md#mem-obj-capture-unit
      - runtime.md#rt-rte-hook-context
      - memory.md#mem-rte-reflection-storage
      - memory.md#mem-rte-session-lifecycle
      - memory.md#mem-obj-memory-record
      - memory.md#mem-rte-evaluation-readback
      - workflow.md#wf-rte-local-exchange
      note: Two qualifying automatic update chains are wired. Capture records establish raw retention
        but declare no bounded absence warrant for a local no; unresolved routes prevent a complete system-wide
        assessment.
    trace_source:
      assessment: partial
      units:
      - scope: Qualifying consensus verdict-statistics update
        assessment: known
        findings:
        - value: event-streams
          basis: wired
          records: &id044
          - memory.md#mem-rte-verdict-feedback
          note: Original inputs are recorded accept/reject vote events and the terminal verdict transition,
            not conversational logs or trained weights.
        records: *id044
        note: The cited records resolve this narrowly named part; operation and benefit were not observed.
      - scope: Qualifying bridge advice generation
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-bridge-distillation
        note: Bounded challenge/outcome fields establish experience input, but original recording format
          and origin are not supplied. No session-log, tool-trace, event-stream or linked-trajectory value
          can be inferred from raw_text or outcome labels alone.
      - scope: Capture-only encoding branch
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-capture-unit
        - runtime.md#rt-rte-hook-context
        note: Original content is conversational session text, but records do not establish a qualifying
          learning update or canonical bounded absence. Session-log source is not asserted independently
          of qualifying learning, nor is this uncertainty made inapplicable.
      - scope: Unresolved reflection, task/history and production-feedback writes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-reflection-storage
        - memory.md#mem-obj-memory-record
        - memory.md#mem-rte-evaluation-readback
        - workflow.md#wf-rte-local-exchange
        note: Qualifying writes and their original sources are not completely established, so source cannot
          be made inapplicable for the whole family.
      records:
      - memory.md#mem-rte-verdict-feedback
      - runtime.md#rt-rte-bridge-distillation
      - memory.md#mem-obj-capture-unit
      - runtime.md#rt-rte-hook-context
      - memory.md#mem-rte-reflection-storage
      - memory.md#mem-obj-memory-record
      - memory.md#mem-rte-evaluation-readback
      - workflow.md#wf-rte-local-exchange
      note: Consensus supplies an event-stream witness; bridge source origin and included alternatives
        remain unresolved. Source classifications apply only to qualifying learning writes, not all imports
        or stored traces.
---

# SAGE memory profile

## Comparison rationale

This profile classifies accepted records, not new source facts. No frozen-source reads were needed or made. Every axis remains partial because the reports explicitly retain unresolved material alternatives; a strong local witness does not complete their inventory. No operation or causal benefit is claimed from source wiring.

Reconciliation supersedes the epistemic content, reflection, correction-replacement and lifecycle-disposition declarations with [MEM-OBJ-memory-record](memory.md#mem-obj-memory-record), [MEM-RTE-reflection-storage](memory.md#mem-rte-reflection-storage), [MEM-RTE-correction-cycle](memory.md#mem-rte-correction-cycle) and [MEM-RTE-lifecycle-change](memory.md#mem-rte-lifecycle-change). Those canonical records carry the affected content, lineage, revision and reliance findings. Reflection's initial fact typing and confidence assignment do not establish promotion of an already retained entry; that unit therefore retains no controlled curation finding. Gate evidence, model verdict and human review remain distinct valid parts; [MEM-OBJ-review-decision](memory.md#mem-obj-review-decision) supplies manual admission and conditional validation/enforcement, not learning or model-facing instructions.

SQL relationship tables are not a separate graph substrate merely because the tool calls them a knowledge graph. Dense retained vectors are a vector access substrate and parametric form; symbolic feedback accumulators are not model weights. The daemon PostgreSQL path does not establish full consumer parity. [MEM-OBJ-memory-relationships](memory.md#mem-obj-memory-relationships), [MEM-OBJ-memory-indexes](memory.md#mem-obj-memory-indexes), [MEM-OBJ-validator-stats](memory.md#mem-obj-validator-stats).

Trace learning and useful learning differ. [MEM-RTE-verdict-feedback](memory.md#mem-rte-verdict-feedback) closes automatic experience-to-statistic-to-decision wiring. [RT-RTE-bridge-distillation](runtime.md#rt-rte-bridge-distillation) closes outcome-fed durable advice and later context routes while leaving original trace-source categories and actual summary semantics unresolved. Its requests for distillation and novel insights establish neither consolidation nor synthesis as a curation operation, even with a claimed basis. The bridge curation unit therefore remains not-determinable with no positive findings; this does not withdraw its separately established trace-fed write and later-context route. Capture retains selected trace text, not an automatically generated recommendation or continuation summary; the missing bounded-absence declaration prevents a controlled local no without erasing the qualifying positive routes. [MEM-OBJ-capture-unit](memory.md#mem-obj-capture-unit).

Read-back distinguishes an explicit retrieval request from automatic downstream model-input assembly. Topic embedding and lexical recall are not automatically push signals. The hook's exact thread match is identifier-based push, whereas domain/recency prefetch is coarse. Bridge and benchmark prompt assembly have bounded positive selection evidence but do not inherit complete selectors from unrelated recall paths. [RT-RTE-targeted-recall](runtime.md#rt-rte-targeted-recall), [RT-RTE-hook-context](runtime.md#rt-rte-hook-context), [MEM-RTE-evaluation-readback](memory.md#mem-rte-evaluation-readback).

[WF-RTE-local-exchange](workflow.md#wf-rte-local-exchange) resolves SQLite retention, prose/symbolic form, automatic protocol admission, enforced session ownership and requested later delivery for one coordination branch. It does not complete the task-board, legacy provider, pipeline-journal or federation inventory left open by [MEM-OBJ-memory-record](memory.md#mem-obj-memory-record) and [MEM-RTE-sync-copy](memory.md#mem-rte-sync-copy). These limits prevent complete-value statistics, not existence findings.
