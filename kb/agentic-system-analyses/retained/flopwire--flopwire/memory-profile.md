---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Flopwire memory profile: retained conversation evidence, derived navigation, coordination
  and restrictive state'
run-id: AAS-2026-10-20-flopwire-184bd013bba1-01
source-identity: https://github.com/flopwire/flopwire
reviewed-boundary: 057a4b87603cc878e81d9eb49298ddc4eb9eeb23
memory-comparison:
  version: 2
  scope: Extracted conversation/tool evidence; local/server indexes, digests and commit projections; archived
    and recovered history, captured readable and opaque checkpoint alternatives, masks/tombstones and
    historical sharing provenance; retained bus messages, delivery state and adapter-stored copies; backup/restore
    and later retrieval, maintenance and delivery consumers. Excludes static shipped instructions/binaries,
    evaluation model weights, ordinary unretained current-call state and independent external harness
    internals. Captured checkpoint provenance and its unresolved originating consumer remain included
    as limits.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Local extracted text, FTS/access state, digest, commit projection, Cowork history and local
          bus bodies/leases
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records: &id001
          - memory.md#mem-obj-message-text
          - memory.md#mem-obj-index-metadata
          - memory.md#mem-obj-digest
          - memory.md#mem-obj-commit-evidence
          - memory.md#mem-obj-cowork-history
          - memory.md#mem-obj-bus-messages
          - memory.md#mem-obj-delivery-metadata
          note: SQLite retains text, derived projections and symbolic access/delivery state; FTS shards
            do not imply vectors.
        records: *id001
        note: Local retained parts have identified SQLite storage, independently of their encoding.
      - scope: Shared parsed history, digest, commit evidence, bus content and archive manifests
        assessment: known
        findings:
        - value: rdbms
          basis: wired
          records: &id002
          - memory.md#mem-obj-archive
          - memory.md#mem-obj-digest
          - memory.md#mem-obj-commit-evidence
          - memory.md#mem-obj-bus-messages
          note: Server Postgres retains parsed/shared state, projections, messages and archive metadata.
        records: *id002
        note: Postgres is distinct from local SQLite and archive object payloads.
      - scope: Shared source-byte archive chunks
        assessment: known
        findings:
        - value: service-object
          basis: wired
          records: &id003
          - memory.md#mem-obj-archive
          - memory.md#mem-rte-restore-state
          note: Compressed content-addressed chunks persist in object storage.
        records: *id003
        note: Payload opacity leaves its recorded archive substrate identifiable.
      - scope: Captured native source/checkpoint files, local masking sidecar/key and independent backup/export
          files
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id004
          - memory.md#mem-obj-compacted
          - memory.md#mem-obj-tombstone
          - memory.md#mem-rte-restore-state
          - memory.md#mem-rte-import-recovery
          - runtime.md#rt-rte-history-retrieval
          note: Native source bytes, JSONL masks/key and backup dump/manifest/object files are retained
            as files.
        records: *id004
        note: File copies have different availability and deletion horizons from parsed databases.
      - scope: Opencode host-stored delivered message parts
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-adapter-delivery
        note: Host APIs store parts for later model calls, but the external host storage implementation
          is not frozen; no substrate can be assigned to that retained copy.
      records:
      - memory.md#mem-obj-message-text
      - memory.md#mem-obj-index-metadata
      - memory.md#mem-obj-digest
      - memory.md#mem-obj-commit-evidence
      - memory.md#mem-obj-cowork-history
      - memory.md#mem-obj-bus-messages
      - memory.md#mem-obj-delivery-metadata
      - memory.md#mem-obj-archive
      - memory.md#mem-rte-restore-state
      - memory.md#mem-obj-compacted
      - memory.md#mem-obj-tombstone
      - memory.md#mem-rte-import-recovery
      - runtime.md#rt-rte-history-retrieval
      - runtime.md#rt-rte-adapter-delivery
      note: Inventory includes local/server memory, archive, masks, imports/backups and adapter-retained
        copies. The host copy prevents complete storage classification; external model weights and static
        shipped instructions are excluded.
    representational_form:
      assessment: partial
      units:
      - scope: Extracted prose, digest Intent/Last snippets, readable captured summary and bus body at
          model/history consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id005
          - memory.md#mem-obj-message-text
          - memory.md#mem-obj-digest
          - memory.md#mem-obj-compacted
          - memory.md#mem-obj-bus-messages
          - memory.md#mem-rte-thread-history
          note: Later readers interpret conversation claims, clipped snippets and message requests as
            prose.
        records: *id005
        note: Textual tool evidence is returned for interpretation rather than replayed as executable
          commands.
      - scope: Index selectors, digest activity/State, commit observations, archive manifests, refs, delivery
          state, tombstones and Cowork restrictions at code consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id006
          - memory.md#mem-obj-index-metadata
          - memory.md#mem-obj-digest
          - memory.md#mem-obj-commit-evidence
          - memory.md#mem-obj-archive
          - memory.md#mem-obj-bus-messages
          - memory.md#mem-obj-delivery-metadata
          - memory.md#mem-obj-tombstone
          - memory.md#mem-obj-cowork-history
          note: Localized identities, counters, hashes, offsets and flags receive fixed code interpretation.
        records: *id006
        note: Structured tool call/result strings and typed checkpoint envelopes are symbolic encodings;
          prose within them remains separately classified.
      - scope: Encrypted checkpoint payloads, including captured archive alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-compacted
        - memory.md#mem-obj-archive
        note: Readable extraction does not reveal the opaque payload representation or host consumption
          semantics. Encryption and compression establish neither symbolic nor parametric consumed content.
      records:
      - memory.md#mem-obj-message-text
      - memory.md#mem-obj-digest
      - memory.md#mem-obj-compacted
      - memory.md#mem-obj-bus-messages
      - memory.md#mem-rte-thread-history
      - memory.md#mem-obj-index-metadata
      - memory.md#mem-obj-commit-evidence
      - memory.md#mem-obj-archive
      - memory.md#mem-obj-delivery-metadata
      - memory.md#mem-obj-tombstone
      - memory.md#mem-obj-cowork-history
      note: Readable prose and operative code metadata are classified separately. Opaque checkpoint content
        prevents complete form coverage; no parametric memory finding is warranted by an external evaluation
        model.
    lineage:
      assessment: partial
      units:
      - scope: Parser-extracted transcript text, trace-derived digest/commit projections and transcript-derived
          receipt/provenance metadata
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id007
          - memory.md#mem-obj-message-text
          - memory.md#mem-rte-derive-navigation
          - memory.md#mem-obj-delivery-metadata
          - memory.md#mem-obj-cowork-history
          note: Native work-session turns and tool outcomes feed automatic extraction, folding, projection
            and receipt/provenance updates.
        records: *id007
        note: This identifies inspected derivation, not authenticity or complete initial provenance of
          every underlying utterance.
      - scope: Acquired native/archive content, recovered CASS history, captured host summaries and restored
          state
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id008
          - memory.md#mem-obj-archive
          - memory.md#mem-rte-import-recovery
          - memory.md#mem-rte-capture-compaction
          - memory.md#mem-rte-restore-state
          note: Existing external history/checkpoints or saved state enter through upload, capture, recovery
            or restore rather than being newly authored by Flopwire.
        records: *id008
        note: Imported lineage concerns the acquired copy; subsequent extraction and fold paths remain
          distinct.
      - scope: Sender-created bus body at explicit send
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id009
          - memory.md#mem-obj-bus-messages
          - workflow.md#wf-rte-request-reply
          note: A sender supplies message/request/answer content that software admits and retains.
        records: *id009
        note: Sender authorship is supported without identifying the sender as human or computational.
      - scope: Original host compaction/checkpoint derivation and opaque replacement content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-compacted
        - memory.md#mem-rte-capture-compaction
        note: Original summary production, admission, reasons and encrypted derivation are uninspected;
          known Flopwire extraction does not resolve them.
      - scope: Initial content provenance within recovered snapshots and arbitrary native material
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-import-recovery
        - memory.md#mem-obj-message-text
        note: Parser capture and caller selection do not establish the complete upstream derivation of
          all acquired content; converter fidelity remains unresolved.
      records:
      - memory.md#mem-obj-message-text
      - memory.md#mem-rte-derive-navigation
      - memory.md#mem-obj-delivery-metadata
      - memory.md#mem-obj-cowork-history
      - memory.md#mem-obj-archive
      - memory.md#mem-rte-import-recovery
      - memory.md#mem-rte-capture-compaction
      - memory.md#mem-rte-restore-state
      - memory.md#mem-obj-bus-messages
      - workflow.md#wf-rte-request-reply
      - memory.md#mem-obj-compacted
      note: Known local derivations coexist with unresolved upstream lineage; backup serialization alone
        adds no unsupported other-compiled finding.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Returned history, digest snippets, commit references and retained thread bodies at requesting
          models
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id010
          - runtime.md#rt-rte-history-retrieval
          - memory.md#mem-rte-derive-navigation
          - memory.md#mem-rte-thread-history
          note: Tool results supply evidence and navigation for later interpretation, including historical
            messages without new action authorization.
        records: *id010
        note: Delivery supports context/evidence authority, not truth endorsement or demonstrated compliance.
      - scope: Retained own-user request bodies at direct recipient context
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id011
          - memory.md#mem-obj-bus-messages
          - runtime.md#rt-bap-message-guidance
          - workflow.md#wf-rte-request-reply
          note: Direct delivery presents requests as tasks within existing permissions; recipient interpretation
            is guided by static policy.
        records: *id011
        note: The accumulated message body carries directions; static standing instructions are excluded
          from memory inventory. Other-person messages have advisory/confirmation limits.
      - scope: Retained message text and lexical access features at ranking code
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id012
          - memory.md#mem-obj-index-metadata
          - runtime.md#rt-rte-history-retrieval
          note: Stored text and token/trigram features influence relative search priority under fixed
            lexical ranking.
        records: *id012
        note: Ranking influence does not require learned weights or stored ranking policy.
      - scope: Retained cursors, digest State, commit references, delivery/receipt state and provenance
          at later selectors/workers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id013
          - memory.md#mem-obj-index-metadata
          - memory.md#mem-obj-digest
          - memory.md#mem-obj-commit-evidence
          - memory.md#mem-obj-delivery-metadata
          - memory.md#mem-bap-history-restriction
          note: State selects resume windows, subsequent folds, evidence addresses, recipients, redelivery
            and restrictive sharing paths.
        records: *id013
        note: These are actual code consumers rather than unconsumed metadata.
      - scope: Durable masks, historical sharing restrictions, deletion tombstones and retained eligibility
          state at admission/read/write gates
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records: &id014
          - memory.md#mem-obj-tombstone
          - memory.md#mem-bap-history-restriction
          - memory.md#mem-rte-withdraw-history
          note: Masks and restrictions veto exposure, sharing or reingestion and constrain later writes.
        - value: validation
          basis: wired
          records: *id014
          note: Retained masks/provenance/tombstones supply admissibility criteria for subsequent writes
            or sharing qualification.
        records: *id014
        note: Validation criteria and enforced consequences are separate forces at the fixed code consumer;
          remote completeness remains unverified.
      - scope: Retained trace rows/sightings at digest/projection and receipt/provenance update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id015
          - memory.md#mem-rte-derive-navigation
          - memory.md#mem-obj-delivery-metadata
          - memory.md#mem-bap-history-restriction
          note: Recorded experience feeds automatic updates to durable navigation or behavior-selecting
            state that later consumers use.
        records: *id015
        note: Learning authority at the update consumer is separate from downstream knowledge, routing
          and enforcement. It establishes no capacity improvement.
      - scope: Opaque host checkpoint at its original host consumer
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-compacted
        - memory.md#mem-rte-capture-compaction
        note: Host reuse and consumed payload are unresolved; readable summaries cannot establish the
          opaque alternative authority.
      records:
      - runtime.md#rt-rte-history-retrieval
      - memory.md#mem-rte-derive-navigation
      - memory.md#mem-rte-thread-history
      - memory.md#mem-obj-bus-messages
      - runtime.md#rt-bap-message-guidance
      - workflow.md#wf-rte-request-reply
      - memory.md#mem-obj-index-metadata
      - memory.md#mem-obj-digest
      - memory.md#mem-obj-commit-evidence
      - memory.md#mem-obj-delivery-metadata
      - memory.md#mem-bap-history-restriction
      - memory.md#mem-obj-tombstone
      - memory.md#mem-rte-withdraw-history
      - memory.md#mem-obj-compacted
      - memory.md#mem-rte-capture-compaction
      note: Consumer-specific forces coexist. The external checkpoint consumer prevents a complete inventory;
        static shipped guidance is not classified as accumulated memory.
    write_agency:
      assessment: partial
      units:
      - scope: Transcript extraction, navigation projection, subsequent compaction capture, delivery-state
          updates and automatic policy/redaction maintenance
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id016
          - runtime.md#rt-rte-transcript-index
          - memory.md#mem-rte-derive-navigation
          - memory.md#mem-rte-capture-compaction
          - memory.md#mem-obj-delivery-metadata
          - memory.md#mem-rte-withdraw-history
          - memory.md#mem-rte-redact-content
          note: Parser, selector, fold and worker code admit retained changes without per-content operator
            approval.
        records: *id016
        note: Workflow initiation and human authorship of some prompts do not make these admissions manual.
      - scope: Bus send admission and import/restore validation
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id017
          - memory.md#mem-obj-bus-messages
          - memory.md#mem-rte-import-recovery
          - memory.md#mem-rte-restore-state
          note: Software cleaning, eligibility, manifest/hash and structural checks accept or reject supplied
            content/state.
        records: *id017
        note: This classifies software admission independently of the unresolved principal supplying the
          candidate.
      - scope: Content-specific request/control for redaction, deletion, recovery selections, restore
          replacements and bus authoring
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-redact-content
        - memory.md#mem-rte-withdraw-history
        - memory.md#mem-rte-import-recovery
        - memory.md#mem-rte-restore-state
        - memory.md#mem-obj-bus-messages
        note: Explicit caller choices are established, but generic credentials do not prove an explicit
          human content decision; manual cannot be inferred.
      - scope: Original external host summary/checkpoint admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-capture-compaction
        - memory.md#mem-obj-compacted
        note: External producer and summary admission control are uninspected; known subsequent extraction
          does not classify original agency.
      records:
      - runtime.md#rt-rte-transcript-index
      - memory.md#mem-rte-derive-navigation
      - memory.md#mem-rte-capture-compaction
      - memory.md#mem-obj-delivery-metadata
      - memory.md#mem-rte-withdraw-history
      - memory.md#mem-rte-redact-content
      - memory.md#mem-obj-bus-messages
      - memory.md#mem-rte-import-recovery
      - memory.md#mem-rte-restore-state
      - memory.md#mem-obj-compacted
      note: Automatic admission witnesses do not resolve original host admission or human control of explicit
        content requests. No unsupported manual value is asserted.
    curation_operations:
      assessment: partial
      units:
      - scope: Digest fold over retained session turns and activity
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id018
          - memory.md#mem-rte-derive-navigation
          - epistemic.md#epi-rte-digest-fold
          - memory.md#mem-obj-digest
          note: Selected first/last snippets and bounded activity sets reduce existing retained trace
            content for later navigation.
        - value: evolve
          basis: wired
          records: *id018
          note: Subsequent folds revise stored digest fields/bookkeeping as new or reparsed rows arrive.
        records: *id018
        note: Consolidation is deterministic selection/compression, not model inference or a claim of
          semantic verification.
      - scope: Local/server content masks and dependent-view refresh
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id019
          - memory.md#mem-rte-redact-content
          - epistemic.md#epi-rte-index-redact
          note: Explicit masking revises retained rows, titles, digests and projections; maintenance reapplies
            masks.
        records: *id019
        note: Masking changes retained content without a truth-falsity judgment.
      - scope: Reversible server hiding and superseded source generations
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records: &id020
          - memory.md#mem-rte-withdraw-history
          - runtime.md#rt-rte-transcript-index
          note: Hidden/superseded history loses current retrieval eligibility while historical state can
            remain.
        records: *id020
        note: Reversible invalidation is distinguished from permanent purge.
      - scope: Expired retained bus content and policy/deletion purge
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id021
          - memory.md#mem-rte-thread-history
          - memory.md#mem-rte-withdraw-history
          - runtime.md#rt-rte-hook-delivery
          note: Expiry and purge forget retained material after their route-specific retention horizons.
        records: *id021
        note: Different local/server horizons do not imply universal erasure or expiry of independent
          backups.
      - scope: Original host compaction transformation and opaque replacement alternative
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-compacted
        - memory.md#mem-rte-capture-compaction
        note: The originating transformation is not inspected; receiving a summary does not establish
          its curation algorithm.
      - scope: Unaudited maintenance/converter and evaluator-update alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-import-recovery
        - memory.md#mem-rte-withdraw-history
        - runtime.md#rt-rte-workflow-trial
        note: Converter/policy variants and evaluator revision consumers are not completely assessed.
          No complete operation enumeration or absence of synthesis, promotion or deduplication is warranted.
      records:
      - memory.md#mem-rte-derive-navigation
      - epistemic.md#epi-rte-digest-fold
      - memory.md#mem-obj-digest
      - memory.md#mem-rte-redact-content
      - epistemic.md#epi-rte-index-redact
      - memory.md#mem-rte-withdraw-history
      - runtime.md#rt-rte-transcript-index
      - memory.md#mem-rte-thread-history
      - runtime.md#rt-rte-hook-delivery
      - memory.md#mem-obj-compacted
      - memory.md#mem-rte-capture-compaction
      - memory.md#mem-rte-import-recovery
      - runtime.md#rt-rte-workflow-trial
      note: Only implemented transformations over retained content receive values. Acquisition, index
        rebuilding and primary-key/window collision suppression alone do not establish curation operations.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested history search/read/raw/change, sessions/outline, inbox and retained server-thread
          reads
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id022
          - runtime.md#rt-rte-history-retrieval
          - memory.md#mem-rte-thread-history
          - memory.md#mem-rte-derive-navigation
          - workflow.md#wf-rte-request-reply
          note: The user/model requests retained evidence; fixed selection and return fulfill that request.
        records: *id022
        note: Delivering the requested page is not an additional push operation.
      - scope: Eligible hooks, opencode insertion and cloud delivery of retained pending envelopes
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id023
          - runtime.md#rt-rte-hook-delivery
          - runtime.md#rt-rte-adapter-delivery
          note: Automatic event/lease/recipient selectors supply retained messages without a recipient
            history request.
        records: *id023
        note: An upstream sender selects the destination; later automatic delivery remains push.
      - scope: Automatic later fold/resume/masking/sharing and delivery workers consuming retained state
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id024
          - memory.md#mem-rte-derive-navigation
          - memory.md#mem-obj-index-metadata
          - memory.md#mem-obj-tombstone
          - memory.md#mem-bap-history-restriction
          - memory.md#mem-obj-delivery-metadata
          note: Indexer/worker triggers automatically supply prior digest State, cursors, masks and restrictions
            to their code consumers.
        records: *id024
        note: Includes internal later consumers, not only model-facing delivery.
      - scope: Original host read-back of opaque checkpoints
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-compacted
        - memory.md#mem-rte-capture-compaction
        note: Requested Flopwire extraction reads do not establish the original host reuse route.
      records:
      - runtime.md#rt-rte-history-retrieval
      - memory.md#mem-rte-thread-history
      - memory.md#mem-rte-derive-navigation
      - workflow.md#wf-rte-request-reply
      - runtime.md#rt-rte-hook-delivery
      - runtime.md#rt-rte-adapter-delivery
      - memory.md#mem-obj-index-metadata
      - memory.md#mem-obj-tombstone
      - memory.md#mem-bap-history-restriction
      - memory.md#mem-obj-delivery-metadata
      - memory.md#mem-obj-compacted
      - memory.md#mem-rte-capture-compaction
      note: Both requested evidence and unsolicited context/state supply are wired; unresolved original
        host reuse prevents complete direction coverage.
    read_back_signal:
      assessment: partial
      units:
      - scope: Pending-message push at eligible hook/adapter/cloud event
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id025
          - runtime.md#rt-rte-hook-delivery
          - runtime.md#rt-rte-adapter-delivery
          - memory.md#mem-obj-delivery-metadata
          note: Recipient session/root identity matches select the retained envelopes supplied to that
            recipient.
        - value: coarse
          basis: wired
          records: *id025
          note: Pending/leased availability, eligible events, busy-state and message/byte budgets gate
            the available delivery batch.
        records: *id025
        note: Trigger is a hook/host event or cloud delivery opportunity; identity targeting and coarse
          eligibility/budget tests remain distinct. Body semantics do not select the delivery.
      - scope: Triggered source folds, resumptions, mask replay and restrictive provenance refresh
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id026
          - memory.md#mem-rte-derive-navigation
          - memory.md#mem-obj-index-metadata
          - memory.md#mem-obj-tombstone
          - memory.md#mem-bap-history-restriction
          note: Source/session/generation/message identities select the retained State, cursor, masks
            or historical restriction used by the automatic consumer.
        - value: coarse
          basis: wired
          records: *id026
          note: Active/superseded, readiness and available-state conditions gate automatic processing.
        records: *id026
        note: These identity matches select operative retained parts, beyond merely naming a requested
          file.
      - scope: Original host checkpoint selection
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-compacted
        - memory.md#mem-rte-capture-compaction
        note: Host trigger, selector inputs and selected opaque payload are uninspected; cannot declare
          the branch inapplicable based on known pull retrieval.
      records:
      - runtime.md#rt-rte-hook-delivery
      - runtime.md#rt-rte-adapter-delivery
      - memory.md#mem-obj-delivery-metadata
      - memory.md#mem-rte-derive-navigation
      - memory.md#mem-obj-index-metadata
      - memory.md#mem-obj-tombstone
      - memory.md#mem-bap-history-restriction
      - memory.md#mem-obj-compacted
      - memory.md#mem-rte-capture-compaction
      note: Lexical ranking belongs to requested pull search here and does not establish an inferred-lexical
        push signal. Known push selectors coexist with unresolved host selection.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatic digest and commit projection writes from retained session/tool traces to later
          navigation/evidence consumers
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id027
          - memory.md#mem-rte-derive-navigation
          - epistemic.md#epi-rte-digest-fold
          - epistemic.md#epi-rte-commit-check
          - epistemic.md#epi-rte-commit-store
          note: Retained trace-fed reduced artifacts are automatically written and later consumed as context/navigation;
            wired qualification does not require observed improvement.
        records: *id027
        note: Durable summaries and evidence projections qualify beyond raw log retention.
      - scope: Transcript-derived receipt and historical-provenance writes to later delivery/sharing decisions
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id028
          - memory.md#mem-obj-delivery-metadata
          - memory.md#mem-obj-cowork-history
          - memory.md#mem-bap-history-restriction
          note: Automatic trace-fed state persists and shapes redelivery or sharing restrictions at later
            code consumers.
        records: *id028
        note: Symbolic behavior-shaping artifacts qualify without changing parameters.
      - scope: Externally produced readable/opaque host checkpoints
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-compacted
        - memory.md#mem-rte-capture-compaction
        note: Known automatic Flopwire extraction preserves acquired material, but original summary production/admission
          and opaque host consumption are unresolved; no complete original trace-fed chain is established.
      - scope: Alternative evaluator/report-fed revision routes
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-workflow-trial
        note: The supplied trial does not establish an automatic product-update consumer; unassessed alternatives
          support neither a global negative nor an additional positive.
      records:
      - memory.md#mem-rte-derive-navigation
      - epistemic.md#epi-rte-digest-fold
      - epistemic.md#epi-rte-commit-check
      - epistemic.md#epi-rte-commit-store
      - memory.md#mem-obj-delivery-metadata
      - memory.md#mem-obj-cowork-history
      - memory.md#mem-bap-history-restriction
      - memory.md#mem-obj-compacted
      - memory.md#mem-rte-capture-compaction
      - runtime.md#rt-rte-workflow-trial
      note: Supported local yes findings give a supported system yes with partial coverage. No absence
        record warrants local or system no. This axis concerns automatic trace-fed durable updates, independently
        of improved capacity.
    trace_source:
      assessment: partial
      units:
      - scope: Digest/navigation updates from user and assistant turns
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id029
          - memory.md#mem-rte-derive-navigation
          - epistemic.md#epi-rte-digest-fold
          note: Recorded conversational turns supply selected prompt/reply text and navigation context.
        records: *id029
        note: Original content is work-session dialogue, independent of its parser serialization.
      - scope: Commit evidence and activity updates from captured commands/results
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id030
          - memory.md#mem-rte-derive-navigation
          - epistemic.md#epi-rte-commit-check
          - epistemic.md#epi-rte-commit-store
          note: Recorded tool requests, shell execution outcomes and supporting results supply retained
            provenance updates.
        records: *id030
        note: Command/result linkage establishes tool origin; it does not establish multi-step state/action/outcome
          trajectories.
      - scope: Read-receipt and historical restriction updates from captured sightings/provenance
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id031
          - memory.md#mem-obj-delivery-metadata
          - memory.md#mem-obj-cowork-history
          - runtime.md#rt-rte-hook-delivery
          note: Recognized transcript hook-context rows supply recorded sightings for later receipt state.
        - value: event-streams
          basis: wired
          records: *id031
          note: Discrete capture/index evidence and delivery/confirmation events feed durable receipt
            and historical-restriction state.
        records: *id031
        note: Session-derived wrapper sightings are distinguished from actual runtime delivery/capture
          events; wrapping turns does not itself add an event-stream source.
      - scope: Original host summary/checkpoint mixed or opaque input
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-compacted
        - memory.md#mem-rte-capture-compaction
        note: External turns are described, but exact inputs, opaque derivation and original qualifying
          update route are not established.
      - scope: Alternative evaluation-fed revision inputs
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-workflow-trial
        note: No qualifying update consumer or complete evaluator-input inventory is established by the
          inspected trial.
      records:
      - memory.md#mem-rte-derive-navigation
      - epistemic.md#epi-rte-digest-fold
      - epistemic.md#epi-rte-commit-check
      - epistemic.md#epi-rte-commit-store
      - memory.md#mem-obj-delivery-metadata
      - memory.md#mem-obj-cowork-history
      - runtime.md#rt-rte-hook-delivery
      - memory.md#mem-obj-compacted
      - memory.md#mem-rte-capture-compaction
      - runtime.md#rt-rte-workflow-trial
      note: Source values apply to the qualifying writes above, not every imported file or raw log. No
        trajectories value follows merely from ordered session records.
---

# Flopwire memory profile

## Comparison rationale

The memory boundary follows retained parts and their consumers, rather than the whole runtime's configuration or external model service. The local-index container is split into prose, access metadata, digest, commit evidence and durable provenance. Archive payloads, masking sidecars, bus bodies and delivery state remain separate. Backups are retained copies with a conditional restore consumer, not automatic model input. See [MEM-OBJ-message-text](memory.md#mem-obj-message-text), [MEM-OBJ-index-metadata](memory.md#mem-obj-index-metadata), [MEM-OBJ-archive](memory.md#mem-obj-archive) and [MEM-RTE-restore-state](memory.md#mem-rte-restore-state).

Reconciliation supersedes the epistemic digest and commit-object declarations with [MEM-OBJ-digest](memory.md#mem-obj-digest) and [MEM-OBJ-commit-evidence](memory.md#mem-obj-commit-evidence). All classifications use those canonical objects. The narrower epistemic fold, check, retention and lookup routes remain distinct supporting mechanisms; they are not superseded. No finding upgrades a conditional commit observation into authenticated Git history.

Digest extraction consolidates existing retained turns; its clipped snippets need no new conjecture to qualify as trace-fed durable context. Commit projections preserve checked command/result relationships for later evidence recovery. Their update consumer gives traces learning authority; their downstream readers receive knowledge and navigation. Receipt/provenance updates instead shape code routing and restrictions. These wired paths establish automatic trace learning without evidence of improved future capacity. See [MEM-RTE-derive-navigation](memory.md#mem-rte-derive-navigation), [EPI-RTE-commit-check](epistemic.md#epi-rte-commit-check), [MEM-OBJ-delivery-metadata](memory.md#mem-obj-delivery-metadata) and [MEM-BAP-history-restriction](memory.md#mem-bap-history-restriction).

Explicit caller requests do not establish manual agency. Software admission is known, while human control of request content and original external checkpoint admission remains unresolved. Imported checkpoint text has known subsequent extraction; that cannot establish opaque payload form, original derivation or host reuse. The records contain no bounded absence permitting trace-learning no. See [MEM-RTE-redact-content](memory.md#mem-rte-redact-content), [MEM-RTE-import-recovery](memory.md#mem-rte-import-recovery) and [MEM-RTE-capture-compaction](memory.md#mem-rte-capture-compaction).

Search and addressed reads are pull, including their code-driven ranking and return. Pending-envelope delivery is push with recipient identity targeting and separate coarse event/budget gates. Internal consumers also automatically receive retained cursors, masks and fold/provenance state. Static instruction renewal is excluded from accumulated-memory read-back. See [RT-RTE-history-retrieval](runtime.md#rt-rte-history-retrieval), [RT-RTE-hook-delivery](runtime.md#rt-rte-hook-delivery) and [RT-RTE-adapter-delivery](runtime.md#rt-rte-adapter-delivery).

All findings rest on accepted implementation records. None asserts observed activation, reliable compliance or causal benefit. No source files were read for this profile; the supplied records and reconciliation supplied all warrants. Uninspected parser, converter, maintenance and evaluator variants prevent complete enumeration where named above.
