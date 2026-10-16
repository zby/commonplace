---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: Semiont memory comparison of retained knowledge, derived access stores and outcome/progress
  controls at the frozen partial-loop boundary.
run-id: AAS-2026-10-15-semiont-d516c7013d8f-01
source-identity: https://github.com/The-AI-Alliance/semiont
reviewed-boundary: a920067ac4ea63a57b1855b7d263485fbd22bab4
memory-comparison:
  version: 2
  scope: 'Included: accumulated resource files, resource/annotation event history and current views, annotation
    prose/anchors/tags/bindings and registered vocabulary, graph projection, numerical vectors and readable
    payload, anchored extraction text/declines, remembered indexing outcomes, Weaver and job recovery
    state, their admission/maintenance and later browse/search/gather/generation routes, and afforded
    aggregate composition/read-back. Unresolved included alternatives: direct-input human control and
    initial provenance, arbitrary uploaded formats, full Browser/desktop lifecycle, offline restoration,
    remaining backend/host paths. Excluded: static shipped prompts/configuration as memory, request-local
    gathered prose/scores and compiler repair state unless retained for a later consumer, external assistant
    conversation memory, provider-internal retention/training and external weights/corpora. No universal
    corpus or deployment coverage is asserted.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Resource content, JSONL record history, materialized views, extracted-text cache and Weaver
          sequence marks
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-content
          - runtime.md#rt-rte-resource-admission
          - memory.md#mem-rte-content-revision
          - memory.md#mem-obj-event-log
          - memory.md#mem-rte-record-replay
          - memory.md#mem-obj-anchored-text
          - memory.md#mem-rte-vector-maintenance
          - memory.md#mem-obj-weaver-checkpoint
          - memory.md#mem-rte-graph-maintenance
          note: Resource files and sharded event/cache files are operative stores; service-state view
            and checkpoint files are distinct retained parts.
        records:
        - memory.md#mem-obj-content
        - runtime.md#rt-rte-resource-admission
        - memory.md#mem-rte-content-revision
        - memory.md#mem-obj-event-log
        - memory.md#mem-rte-record-replay
        - memory.md#mem-obj-anchored-text
        - memory.md#mem-rte-vector-maintenance
        - memory.md#mem-obj-weaver-checkpoint
        - memory.md#mem-rte-graph-maintenance
        note: Inspected filesystem-backed objects are covered. Staging is not a Git commit, so repo is
          not inferred from a working-tree location.
      - scope: Retained graph projection
        assessment: known
        findings:
        - value: graph
          basis: wired
          records:
          - memory.md#mem-obj-graph
          - memory.md#mem-rte-graph-maintenance
          note: Resource/annotation nodes and relationships are stored through the configured graph interface.
        records:
        - memory.md#mem-obj-graph
        - memory.md#mem-rte-graph-maintenance
        note: Logical graph substrate is established; live backend correctness is not.
      - scope: Embeddings, readable point payload and remembered extraction declines
        assessment: known
        findings:
        - value: vector
          basis: wired
          records:
          - memory.md#mem-obj-vector-points
          - memory.md#mem-obj-vector-payload
          - memory.md#mem-rte-vector-maintenance
          - memory.md#mem-obj-declined
          - memory.md#mem-bap-projection-control
          note: VectorStore retains points/payloads and separate non-search decline bookkeeping; bookkeeping
            is not itself a semantic vector.
        records:
        - memory.md#mem-obj-vector-points
        - memory.md#mem-obj-vector-payload
        - memory.md#mem-rte-vector-maintenance
        - memory.md#mem-obj-declined
        - memory.md#mem-bap-projection-control
        note: Classifies the operative store, not the encoding of each field.
      - scope: Retained job inputs and retry/checkpoint records
        assessment: known
        findings:
        - value: service-object
          basis: wired
          records:
          - runtime.md#rt-obj-job-params
          - runtime.md#rt-rte-mark-detection
          note: Dispatcher retains job records through JetStream; no relational or KV implementation is
            inferred beyond the named service-backed records.
        records:
        - runtime.md#rt-obj-job-params
        - runtime.md#rt-rte-mark-detection
        note: Queue retention is finite but spans later worker attempts.
      - scope: Other backend implementations and Browser/desktop retained-state alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-graph
        - memory.md#mem-rte-graph-maintenance
        - memory.md#mem-obj-vector-points
        - memory.md#mem-obj-vector-payload
        - memory.md#mem-rte-vector-maintenance
        - runtime.md#rt-obj-job-params
        - runtime.md#rt-rte-mark-detection
        note: These records bound their backend/recovery coverage; the reports do not establish all alternative
          host-state substrates.
      records:
      - memory.md#mem-obj-content
      - runtime.md#rt-rte-resource-admission
      - memory.md#mem-rte-content-revision
      - memory.md#mem-obj-event-log
      - memory.md#mem-rte-record-replay
      - memory.md#mem-obj-anchored-text
      - memory.md#mem-rte-vector-maintenance
      - memory.md#mem-obj-weaver-checkpoint
      - memory.md#mem-rte-graph-maintenance
      - memory.md#mem-obj-graph
      - memory.md#mem-obj-vector-points
      - memory.md#mem-obj-vector-payload
      - memory.md#mem-obj-declined
      - memory.md#mem-bap-projection-control
      - runtime.md#rt-obj-job-params
      - runtime.md#rt-rte-mark-detection
      note: 'Positive store classes cover the named inspected objects, not every shipped host or backend.
        No trained weights are included: externally served inference parameters are excluded from this
        accumulated-knowledge boundary.'
    representational_form:
      assessment: partial
      units:
      - scope: Readable resource text, extracted text, vector passages and annotation comment/assessment
          bodies at human/model consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-content
          - runtime.md#rt-rte-resource-admission
          - memory.md#mem-rte-content-revision
          - memory.md#mem-obj-anchored-text
          - memory.md#mem-rte-vector-maintenance
          - memory.md#mem-obj-vector-payload
          - memory.md#mem-obj-annotation-text
          note: Readable claims and judgments supply context or advice; PDF encoding is not an additional
            form.
        records:
        - memory.md#mem-obj-content
        - runtime.md#rt-rte-resource-admission
        - memory.md#mem-rte-content-revision
        - memory.md#mem-obj-anchored-text
        - memory.md#mem-rte-vector-maintenance
        - memory.md#mem-obj-vector-payload
        - memory.md#mem-obj-annotation-text
        note: Textual operative parts are separated from metadata and numerical vectors.
      - scope: Event envelopes, views, selectors/tags/bindings, graph structure, cache geometry/stamps/declines
          and recovery controls at fixed-rule consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-event-log
          - memory.md#mem-rte-record-replay
          - memory.md#mem-obj-graph
          - memory.md#mem-rte-graph-maintenance
          - memory.md#mem-obj-anchored-text
          - memory.md#mem-rte-vector-maintenance
          - memory.md#mem-obj-declined
          - memory.md#mem-bap-projection-control
          - memory.md#mem-obj-weaver-checkpoint
          - runtime.md#rt-obj-job-params
          - runtime.md#rt-rte-mark-detection
          - memory.md#mem-obj-annotation-links
          note: IDs, event types, sequence numbers, geometry, checksums, cursors and graph edges have
            localized fixed-rule interpretation.
        records:
        - memory.md#mem-obj-event-log
        - memory.md#mem-rte-record-replay
        - memory.md#mem-obj-graph
        - memory.md#mem-rte-graph-maintenance
        - memory.md#mem-obj-anchored-text
        - memory.md#mem-rte-vector-maintenance
        - memory.md#mem-obj-declined
        - memory.md#mem-bap-projection-control
        - memory.md#mem-obj-weaver-checkpoint
        - runtime.md#rt-obj-job-params
        - runtime.md#rt-rte-mark-detection
        - memory.md#mem-obj-annotation-links
        note: Annotation prose and extracted wording remain in the natural-language unit, not conflated
          with their envelopes.
      - scope: Retained dense resource-chunk and annotation-quote embeddings at similarity comparison
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-vector-points
          note: Distributed numerical vectors are the parametric form here, distinct from external provider
            weights and readable payload.
        records:
        - memory.md#mem-obj-vector-points
        note: Form is established even though dimensions do not provide human-readable reasons.
      - scope: Arbitrary uploaded program/JSON/binary parts at format-specific consumers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-content
        - runtime.md#rt-rte-resource-admission
        - memory.md#mem-rte-content-revision
        note: The content record permits symbolic program/JSON content but does not establish every actual
          downstream consumption path.
      records:
      - memory.md#mem-obj-content
      - runtime.md#rt-rte-resource-admission
      - memory.md#mem-rte-content-revision
      - memory.md#mem-obj-anchored-text
      - memory.md#mem-rte-vector-maintenance
      - memory.md#mem-obj-vector-payload
      - memory.md#mem-obj-annotation-text
      - memory.md#mem-obj-event-log
      - memory.md#mem-rte-record-replay
      - memory.md#mem-obj-graph
      - memory.md#mem-rte-graph-maintenance
      - memory.md#mem-obj-declined
      - memory.md#mem-bap-projection-control
      - memory.md#mem-obj-weaver-checkpoint
      - runtime.md#rt-obj-job-params
      - runtime.md#rt-rte-mark-detection
      - memory.md#mem-obj-annotation-links
      - memory.md#mem-obj-vector-points
      note: Mixed objects are split by their actual consumer. Arbitrary content and untraced consumer
        alternatives prevent a complete inventory of forms across all uploaded material.
    lineage:
      assessment: partial
      units:
      - scope: Direct caller uploads and local CLI files entering retained resources
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-content
          - runtime.md#rt-rte-resource-admission
          - memory.md#mem-rte-content-revision
          note: Caller bytes and local files enter the KB through upload; human versus computational origin
            is not resolved by principal identity.
        records:
        - memory.md#mem-obj-content
        - runtime.md#rt-rte-resource-admission
        - memory.md#mem-rte-content-revision
        note: The acquisition path is known; initial authorship and provenance before acquisition are
          not certified.
      - scope: Worker-generated resources and model-produced annotation bodies
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - runtime.md#rt-rte-yield-generation
          - runtime.md#rt-rte-mark-detection
          - epistemic.md#epi-rte-assessment-proposal
          note: Models compose documents and annotation judgments that software can retain without per-item
            approval.
        records:
        - runtime.md#rt-rte-yield-generation
        - runtime.md#rt-rte-mark-detection
        - epistemic.md#epi-rte-assessment-proposal
        note: Authored output does not imply factual novelty, accepted knowledge, or preserved full reasoning.
      - scope: Replayed views/graph, clones, extraction text and embedding/index derivations
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-event-log
          - memory.md#mem-rte-record-replay
          - memory.md#mem-obj-graph
          - memory.md#mem-rte-graph-maintenance
          - memory.md#mem-obj-content
          - runtime.md#rt-rte-resource-admission
          - memory.md#mem-rte-content-revision
          - memory.md#mem-obj-anchored-text
          - memory.md#mem-rte-vector-maintenance
          - memory.md#mem-obj-vector-points
          - memory.md#mem-obj-vector-payload
          note: Fixed replay, copying, extraction and embedding derive retained parts from source content
            or accepted records.
        records:
        - memory.md#mem-obj-event-log
        - memory.md#mem-rte-record-replay
        - memory.md#mem-obj-graph
        - memory.md#mem-rte-graph-maintenance
        - memory.md#mem-obj-content
        - runtime.md#rt-rte-resource-admission
        - memory.md#mem-rte-content-revision
        - memory.md#mem-obj-anchored-text
        - memory.md#mem-rte-vector-maintenance
        - memory.md#mem-obj-vector-points
        - memory.md#mem-obj-vector-payload
        note: Known transformations do not authenticate source wording or immutable remote embedding weights.
      - scope: Remembered extraction failure and recovery progress derived from runtime outcomes
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-declined
          - memory.md#mem-rte-vector-maintenance
          - memory.md#mem-bap-projection-control
          - memory.md#mem-obj-weaver-checkpoint
          - memory.md#mem-rte-graph-maintenance
          - runtime.md#rt-obj-job-params
          - runtime.md#rt-rte-mark-detection
          note: Extraction outcomes and applied/completed progress are reduced into decline or resume
            controls for later invocations.
        records:
        - memory.md#mem-obj-declined
        - memory.md#mem-rte-vector-maintenance
        - memory.md#mem-bap-projection-control
        - memory.md#mem-obj-weaver-checkpoint
        - memory.md#mem-rte-graph-maintenance
        - runtime.md#rt-obj-job-params
        - runtime.md#rt-rte-mark-detection
        note: Derived controls are distinct from retaining raw lifecycle event envelopes.
      - scope: Documented aggregate composition
        assessment: known
        findings:
        - value: authored
          basis: afforded
          records:
          - memory.md#mem-rte-aggregate-writing
          note: The shipped procedure asks an assistant/operator to compose a source-linked report.
        records:
        - memory.md#mem-rte-aggregate-writing
        note: A documented composition path, not an observed aggregate run.
      - scope: Initial provenance of arbitrary direct content and alternate restoration/admission paths
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-content
        - runtime.md#rt-rte-resource-admission
        - memory.md#mem-rte-content-revision
        - memory.md#mem-rte-annotation-edit
        note: Generic caller identity and uninspected alternatives do not determine all original derivation
          paths.
      records:
      - memory.md#mem-obj-content
      - runtime.md#rt-rte-resource-admission
      - memory.md#mem-rte-content-revision
      - runtime.md#rt-rte-yield-generation
      - runtime.md#rt-rte-mark-detection
      - epistemic.md#epi-rte-assessment-proposal
      - memory.md#mem-obj-event-log
      - memory.md#mem-rte-record-replay
      - memory.md#mem-obj-graph
      - memory.md#mem-rte-graph-maintenance
      - memory.md#mem-obj-anchored-text
      - memory.md#mem-rte-vector-maintenance
      - memory.md#mem-obj-vector-points
      - memory.md#mem-obj-vector-payload
      - memory.md#mem-obj-declined
      - memory.md#mem-bap-projection-control
      - memory.md#mem-obj-weaver-checkpoint
      - runtime.md#rt-obj-job-params
      - memory.md#mem-rte-aggregate-writing
      - memory.md#mem-rte-annotation-edit
      note: Known acquisition and derivation paths coexist with unresolved initial provenance. Wrapping
        imported content in an event does not make that content trace-extracted.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Resource/extracted/passage/assessment prose read by clients and generation
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - runtime.md#rt-rte-annotation-gather
          - memory.md#mem-rte-resource-gather
          - runtime.md#rt-bap-generation-prompt
          - memory.md#mem-obj-anchored-text
          - memory.md#mem-rte-vector-maintenance
          - memory.md#mem-obj-annotation-text
          - memory.md#mem-obj-vector-payload
          note: Later clients and Worker prompts receive selected prose as reference, evidence or advisory
            criticism, not an enforced truth verdict.
        records:
        - runtime.md#rt-rte-annotation-gather
        - memory.md#mem-rte-resource-gather
        - runtime.md#rt-bap-generation-prompt
        - memory.md#mem-obj-anchored-text
        - memory.md#mem-rte-vector-maintenance
        - memory.md#mem-obj-annotation-text
        - memory.md#mem-obj-vector-payload
        note: Selection and delivery are wired; obedience, factual correctness and benefit are unobserved.
      - scope: Retained graph descriptors, text, vectors, types and assessment prose at candidate selection
          and ordering
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-rte-resource-search
          - memory.md#mem-rte-reference-search
          - memory.md#mem-rte-mcp-browse
          - memory.md#mem-obj-vector-points
          - memory.md#mem-obj-vector-payload
          - memory.md#mem-rte-vector-maintenance
          note: Lexical/vector/structural comparisons and optional Matcher rescoring use retained features
            to choose and order results.
        records:
        - memory.md#mem-rte-resource-search
        - memory.md#mem-rte-reference-search
        - memory.md#mem-rte-mcp-browse
        - memory.md#mem-obj-vector-points
        - memory.md#mem-obj-vector-payload
        - memory.md#mem-rte-vector-maintenance
        note: Fixed scoring still gives its retained inputs ranking authority; request-local scores are
          not learned policy.
      - scope: Sequence marks, job cursors/completed units, extraction stamps and declines at maintenance/retry
          consumers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-weaver-checkpoint
          - memory.md#mem-rte-graph-maintenance
          - runtime.md#rt-obj-job-params
          - runtime.md#rt-rte-mark-detection
          - memory.md#mem-obj-declined
          - memory.md#mem-rte-vector-maintenance
          - memory.md#mem-bap-projection-control
          note: Retained progress and outcome state choose replay windows, resumed units, re-extraction
            or skip branches.
        records:
        - memory.md#mem-obj-weaver-checkpoint
        - memory.md#mem-rte-graph-maintenance
        - runtime.md#rt-obj-job-params
        - runtime.md#rt-rte-mark-detection
        - memory.md#mem-obj-declined
        - memory.md#mem-rte-vector-maintenance
        - memory.md#mem-bap-projection-control
        note: These are accumulated operational controls, not static service configuration.
      - scope: Recorded assignment holder/job identity and registered vocabulary at admission
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - runtime.md#rt-rte-resource-admission
          - memory.md#mem-rte-annotation-edit
          - runtime.md#rt-rte-mark-detection
          note: Recorded assignments and registered types/schemas supply admissibility criteria.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-rte-resource-admission
          - memory.md#mem-rte-annotation-edit
          - runtime.md#rt-rte-mark-detection
          note: The matching-holder/required-job and vocabulary checks can refuse writes, rather than
            merely advise.
        records:
        - runtime.md#rt-rte-resource-admission
        - memory.md#mem-rte-annotation-edit
        - runtime.md#rt-rte-mark-detection
        note: Force is bounded to these checks. Generic direct non-worker admission and offline restoration
          are not thereby covered.
      - scope: Extraction outcome at the automatic decline-state updater
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-obj-declined
          - memory.md#mem-rte-vector-maintenance
          - memory.md#mem-bap-projection-control
          note: The outcome of reading/extracting bytes feeds a durable decline artifact that changes
            later startup work.
        records:
        - memory.md#mem-obj-declined
        - memory.md#mem-rte-vector-maintenance
        - memory.md#mem-bap-projection-control
        note: Learning authority at the update consumer is separate from routing authority of the resulting
          decline; no capacity improvement is demonstrated.
      - scope: Authority at untraced host, restoration and provider consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-content
        - runtime.md#rt-rte-resource-admission
        - memory.md#mem-rte-content-revision
        - memory.md#mem-obj-graph
        - memory.md#mem-rte-graph-maintenance
        - memory.md#mem-obj-vector-points
        - memory.md#mem-obj-vector-payload
        - memory.md#mem-rte-vector-maintenance
        note: Existing records do not exhaust every later consumer. Assessment prose does not by itself
          establish a standing instruction or a factual veto.
      records:
      - runtime.md#rt-rte-annotation-gather
      - memory.md#mem-rte-resource-gather
      - runtime.md#rt-bap-generation-prompt
      - memory.md#mem-obj-anchored-text
      - memory.md#mem-rte-vector-maintenance
      - memory.md#mem-obj-annotation-text
      - memory.md#mem-obj-vector-payload
      - memory.md#mem-rte-resource-search
      - memory.md#mem-rte-reference-search
      - memory.md#mem-rte-mcp-browse
      - memory.md#mem-obj-vector-points
      - memory.md#mem-obj-weaver-checkpoint
      - memory.md#mem-rte-graph-maintenance
      - runtime.md#rt-obj-job-params
      - runtime.md#rt-rte-mark-detection
      - memory.md#mem-obj-declined
      - memory.md#mem-bap-projection-control
      - runtime.md#rt-rte-resource-admission
      - memory.md#mem-rte-annotation-edit
      - memory.md#mem-obj-content
      - memory.md#mem-rte-content-revision
      - memory.md#mem-obj-graph
      note: Knowledge, ranking, routing, validation, enforcement and local learning forces coexist at
        different consumers. No standing instruction authority is inferred from the shipped prompt or
        an assessing label.
    write_agency:
      assessment: partial
      units:
      - scope: Worker document/annotation commits and software projection/extraction/checkpoint writes
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-yield-generation
          - runtime.md#rt-rte-mark-detection
          - memory.md#mem-obj-event-log
          - memory.md#mem-rte-record-replay
          - memory.md#mem-obj-graph
          - memory.md#mem-rte-graph-maintenance
          - memory.md#mem-obj-vector-points
          - memory.md#mem-obj-vector-payload
          - memory.md#mem-rte-vector-maintenance
          - memory.md#mem-obj-anchored-text
          - memory.md#mem-obj-weaver-checkpoint
          note: Software admits generated outputs and derived state without an explicit human decision
            on each retained item.
        records:
        - runtime.md#rt-rte-yield-generation
        - runtime.md#rt-rte-mark-detection
        - memory.md#mem-obj-event-log
        - memory.md#mem-rte-record-replay
        - memory.md#mem-obj-graph
        - memory.md#mem-rte-graph-maintenance
        - memory.md#mem-obj-vector-points
        - memory.md#mem-obj-vector-payload
        - memory.md#mem-rte-vector-maintenance
        - memory.md#mem-obj-anchored-text
        - memory.md#mem-obj-weaver-checkpoint
        note: Starting generation, detection or maintenance does not turn its subsequent admissions into
          manual writes.
      - scope: Direct upload, clone/update, body/binding/type edits and aggregate content admission control
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-content
        - runtime.md#rt-rte-resource-admission
        - memory.md#mem-rte-content-revision
        - memory.md#mem-rte-annotation-edit
        - epistemic.md#epi-rte-knowledge-withdrawal
        - memory.md#mem-rte-aggregate-writing
        note: Caller identity and assistant/operator wording do not establish an explicit human supplying,
          editing or approving each retained item. Automatic command execution alone cannot resolve the
          per-content decision.
      - scope: Offline restoration and full Browser/desktop write lifecycle
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-content
        - runtime.md#rt-rte-resource-admission
        - memory.md#mem-rte-content-revision
        - memory.md#mem-rte-annotation-edit
        - epistemic.md#epi-rte-knowledge-withdrawal
        note: Accepted reports leave these alternatives uninspected; ordinary live command gates cannot
          be generalized to them.
      records:
      - runtime.md#rt-rte-yield-generation
      - runtime.md#rt-rte-mark-detection
      - memory.md#mem-obj-event-log
      - memory.md#mem-rte-record-replay
      - memory.md#mem-obj-graph
      - memory.md#mem-rte-graph-maintenance
      - memory.md#mem-obj-vector-points
      - memory.md#mem-obj-vector-payload
      - memory.md#mem-rte-vector-maintenance
      - memory.md#mem-obj-anchored-text
      - memory.md#mem-obj-weaver-checkpoint
      - memory.md#mem-obj-content
      - runtime.md#rt-rte-resource-admission
      - memory.md#mem-rte-content-revision
      - memory.md#mem-rte-annotation-edit
      - epistemic.md#epi-rte-knowledge-withdrawal
      - memory.md#mem-rte-aggregate-writing
      note: Automatic admission is established locally. Manual agency is not asserted merely because a
        UI or a generic caller exists; unresolved direct decisions remain included.
    curation_operations:
      assessment: partial
      units:
      - scope: Existing resource content and annotation bodies revised through update/body operations
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-content
          - runtime.md#rt-rte-resource-admission
          - memory.md#mem-rte-content-revision
          - memory.md#mem-rte-annotation-edit
          - epistemic.md#epi-rte-knowledge-withdrawal
          note: Updating current bytes/checksum or replacing/removing/adding bodies changes existing retained
            entries.
        records:
        - memory.md#mem-obj-content
        - runtime.md#rt-rte-resource-admission
        - memory.md#mem-rte-content-revision
        - memory.md#mem-rte-annotation-edit
        - epistemic.md#epi-rte-knowledge-withdrawal
        note: Supported revisions do not promise immutable old bytes or distributed rollback.
      - scope: Current annotation/resource reliance withdrawn while event history remains
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-rte-annotation-edit
          - epistemic.md#epi-rte-knowledge-withdrawal
          - memory.md#mem-obj-event-log
          - memory.md#mem-rte-record-replay
          note: Deletion/archive removes current annotation or searchable resource representations while
            historical events remain.
        records:
        - memory.md#mem-rte-annotation-edit
        - epistemic.md#epi-rte-knowledge-withdrawal
        - memory.md#mem-obj-event-log
        - memory.md#mem-rte-record-replay
        note: Withdrawal is not erasure and does not automatically retract previously generated descendants.
      - scope: Retained terminal job/recovery state subject to retention pruning
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - runtime.md#rt-rte-yield-generation
          - runtime.md#rt-rte-mark-detection
          note: Configured terminal-record pruning forgets accumulated queue state after its retention
            horizon.
        records:
        - runtime.md#rt-rte-yield-generation
        - runtime.md#rt-rte-mark-detection
        note: This is forgetting of queue memory, not decay of resource claims or learned retrieval weights.
      - scope: Semantic transformation in generated resources, requested summaries and aggregate reports
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-yield-generation
        - epistemic.md#epi-rte-summary-generation
        - memory.md#mem-rte-aggregate-writing
        note: Generation/summary requests and composition names do not establish whether retained outputs
          consolidate existing claims or synthesize new ones. Actual semantic relations are unresolved;
          gather-only summaries are not a durable curation store.
      - scope: Other host curation and untraced alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-annotation-edit
        - epistemic.md#epi-rte-knowledge-withdrawal
        - memory.md#mem-obj-vector-points
        - memory.md#mem-obj-vector-payload
        - memory.md#mem-rte-vector-maintenance
        note: Index rebuild and primary-key collision checks establish neither deduplication nor consolidation.
          Remaining host transformations are not exhaustively inspected.
      records:
      - memory.md#mem-obj-content
      - runtime.md#rt-rte-resource-admission
      - memory.md#mem-rte-content-revision
      - memory.md#mem-rte-annotation-edit
      - epistemic.md#epi-rte-knowledge-withdrawal
      - memory.md#mem-obj-event-log
      - memory.md#mem-rte-record-replay
      - runtime.md#rt-rte-yield-generation
      - runtime.md#rt-rte-mark-detection
      - epistemic.md#epi-rte-summary-generation
      - memory.md#mem-rte-aggregate-writing
      - memory.md#mem-obj-vector-points
      - memory.md#mem-obj-vector-payload
      - memory.md#mem-rte-vector-maintenance
      note: Evolve, invalidate and queue forgetting are supported. No consolidate, synthesize, dedup or
        promote value is inferred from route names, embedding, or replay alone.
    read_back_direction:
      assessment: partial
      units:
      - scope: Explicit browse/search/gather and requested generation-context delivery
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-annotation-gather
          - memory.md#mem-rte-resource-gather
          - runtime.md#rt-bap-generation-prompt
          - memory.md#mem-rte-resource-search
          - memory.md#mem-rte-reference-search
          - memory.md#mem-rte-mcp-browse
          note: Clients request retained knowledge; gather and Worker field selection fulfill that requested
            chain rather than add unsolicited injection.
        records:
        - runtime.md#rt-rte-annotation-gather
        - memory.md#mem-rte-resource-gather
        - runtime.md#rt-bap-generation-prompt
        - memory.md#mem-rte-resource-search
        - memory.md#mem-rte-reference-search
        - memory.md#mem-rte-mcp-browse
        note: Includes resource and annotation focuses and narrower MCP display. Worker clipping is not
          a second push solely because code delivers the prompt.
      - scope: Automatic maintenance selection and delivery of event-targeted retained content
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-graph
          - memory.md#mem-rte-graph-maintenance
          - memory.md#mem-obj-vector-points
          - memory.md#mem-obj-vector-payload
          - memory.md#mem-rte-vector-maintenance
          note: Received resource/annotation events and startup reconcile select retained parts to fold,
            extract or index without a knowledge consumer asking to retrieve them.
        records:
        - memory.md#mem-obj-graph
        - memory.md#mem-rte-graph-maintenance
        - memory.md#mem-obj-vector-points
        - memory.md#mem-obj-vector-payload
        - memory.md#mem-rte-vector-maintenance
        note: Push is local maintenance supply, not independently triggered unsolicited foreground-model
          context.
      - scope: Explicit history/cache reads within maintenance and recovery
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-obj-event-log
          - memory.md#mem-rte-record-replay
          - memory.md#mem-obj-graph
          - memory.md#mem-rte-graph-maintenance
          - memory.md#mem-obj-anchored-text
          - memory.md#mem-rte-vector-maintenance
          - runtime.md#rt-obj-job-params
          - runtime.md#rt-rte-mark-detection
          note: History, cached extraction and retry state are requested by replay/recovery callers. Those
            requests coexist with the automatic upstream maintenance selector.
        records:
        - memory.md#mem-obj-event-log
        - memory.md#mem-rte-record-replay
        - memory.md#mem-obj-graph
        - memory.md#mem-rte-graph-maintenance
        - memory.md#mem-obj-anchored-text
        - memory.md#mem-rte-vector-maintenance
        - runtime.md#rt-obj-job-params
        - runtime.md#rt-rte-mark-detection
        note: Request and automatic selection are distinct operations within the chain.
      - scope: Documented aggregate browse/read role
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-rte-aggregate-writing
          note: The procedure names later report reading and browse-by-type rather than unsolicited delivery.
        records:
        - memory.md#mem-rte-aggregate-writing
        note: No deployed external host behavior is inferred.
      - scope: Full Browser/desktop host refresh and other retained-content consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-annotation-gather
        - memory.md#mem-rte-resource-gather
        - runtime.md#rt-bap-generation-prompt
        - memory.md#mem-rte-resource-search
        - memory.md#mem-rte-reference-search
        - memory.md#mem-rte-mcp-browse
        - runtime.md#rt-obj-job-params
        - runtime.md#rt-rte-mark-detection
        note: Records establish selected callers, not every host reload or unsolicited delivery policy.
      records:
      - runtime.md#rt-rte-annotation-gather
      - memory.md#mem-rte-resource-gather
      - runtime.md#rt-bap-generation-prompt
      - memory.md#mem-rte-resource-search
      - memory.md#mem-rte-reference-search
      - memory.md#mem-rte-mcp-browse
      - memory.md#mem-obj-graph
      - memory.md#mem-rte-graph-maintenance
      - memory.md#mem-obj-vector-points
      - memory.md#mem-obj-vector-payload
      - memory.md#mem-rte-vector-maintenance
      - memory.md#mem-obj-event-log
      - memory.md#mem-rte-record-replay
      - memory.md#mem-obj-anchored-text
      - runtime.md#rt-obj-job-params
      - runtime.md#rt-rte-mark-detection
      - memory.md#mem-rte-aggregate-writing
      note: Both requested knowledge return and automatic maintenance supply exist. A pull witness does
        not resolve other included consumers or imply pull-only operation.
    read_back_signal:
      assessment: partial
      units:
      - scope: Event-triggered maintenance selection of the corresponding retained resource/annotation
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-obj-graph
          - memory.md#mem-rte-graph-maintenance
          - memory.md#mem-obj-vector-points
          - memory.md#mem-obj-vector-payload
          - memory.md#mem-rte-vector-maintenance
          note: 'Trigger: recorded resource/annotation event. Selector input: event target IDs. Selected
            part: matching retained resource bytes, current annotation or graph target delivered to fold/index
            processing.'
        records:
        - memory.md#mem-obj-graph
        - memory.md#mem-rte-graph-maintenance
        - memory.md#mem-obj-vector-points
        - memory.md#mem-obj-vector-payload
        - memory.md#mem-rte-vector-maintenance
        note: Actual target identity selects the operative part; no universal token budget is asserted.
      - scope: Startup maintenance inventory and progress/compatibility filtering
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-graph
          - memory.md#mem-rte-graph-maintenance
          - memory.md#mem-obj-vector-points
          - memory.md#mem-obj-vector-payload
          - memory.md#mem-rte-vector-maintenance
          - memory.md#mem-obj-declined
          - memory.md#mem-bap-projection-control
          - memory.md#mem-obj-weaver-checkpoint
          note: 'Trigger: service startup/reconcile. Selector inputs: catalog availability, sequence marks
            and checksum/type/stamp compatibility. Selected parts: outstanding histories/resources or
            changed/eligible extraction inputs, with unchanged declines skipped.'
        records:
        - memory.md#mem-obj-graph
        - memory.md#mem-rte-graph-maintenance
        - memory.md#mem-obj-vector-points
        - memory.md#mem-obj-vector-payload
        - memory.md#mem-rte-vector-maintenance
        - memory.md#mem-obj-declined
        - memory.md#mem-bap-projection-control
        - memory.md#mem-obj-weaver-checkpoint
        note: Availability/progress filtering is distinct from targeted event identity selection and from
          semantic query scoring.
      - scope: Signals for untraced host push alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-annotation-gather
        - memory.md#mem-rte-resource-gather
        - runtime.md#rt-bap-generation-prompt
        - memory.md#mem-rte-resource-search
        - memory.md#mem-rte-reference-search
        - memory.md#mem-rte-mcp-browse
        note: Known requested IDs, lexical searches and embedding queries are pull selectors, not evidence
          of inferred-lexical or inferred-embedding push. Other host supply is unresolved.
      records:
      - memory.md#mem-obj-graph
      - memory.md#mem-rte-graph-maintenance
      - memory.md#mem-obj-vector-points
      - memory.md#mem-obj-vector-payload
      - memory.md#mem-rte-vector-maintenance
      - memory.md#mem-obj-declined
      - memory.md#mem-bap-projection-control
      - memory.md#mem-obj-weaver-checkpoint
      - runtime.md#rt-rte-annotation-gather
      - memory.md#mem-rte-resource-gather
      - runtime.md#rt-bap-generation-prompt
      - memory.md#mem-rte-resource-search
      - memory.md#mem-rte-reference-search
      - memory.md#mem-rte-mcp-browse
      note: Signals classify only automatic maintenance push. Requested search/gather does not become
        push because it uses IDs, embeddings or model judgment; host alternatives prevent a complete signal
        inventory.
    trace_learning:
      assessment: partial
      units:
      - scope: Extraction failure outcome to remembered decline to later startup reconcile
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-declined
          - memory.md#mem-rte-vector-maintenance
          - memory.md#mem-bap-projection-control
          note: A bytes-read/no-usable-text outcome automatically writes durable checksum/type/reason
            state; later startup suppresses repeating that extraction for unchanged input.
        records:
        - memory.md#mem-obj-declined
        - memory.md#mem-rte-vector-maintenance
        - memory.md#mem-bap-projection-control
        note: The wired outcome-fed behavioral artifact qualifies without new factual knowledge or measured
          improvement.
      - scope: Applied/completed activity to persisted sequence marks or unit/cursor state to later restart/attempt
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-weaver-checkpoint
          - memory.md#mem-rte-graph-maintenance
          - runtime.md#rt-obj-job-params
          - runtime.md#rt-rte-mark-detection
          note: Automatic progress writes shape a later replay window or resumed processing rather than
            merely storing an unused raw log.
        records:
        - memory.md#mem-obj-weaver-checkpoint
        - memory.md#mem-rte-graph-maintenance
        - runtime.md#rt-obj-job-params
        - runtime.md#rt-rte-mark-detection
        note: Recovery behavior is the bounded later effect; no generalized learned strategy or exactly-once
          guarantee is asserted.
      - scope: Generated content, graph/vector knowledge transformations and aggregate alternatives as
          trace-fed learning
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-yield-generation
        - runtime.md#rt-rte-mark-detection
        - memory.md#mem-obj-graph
        - memory.md#mem-rte-graph-maintenance
        - memory.md#mem-obj-vector-points
        - memory.md#mem-obj-vector-payload
        - memory.md#mem-rte-vector-maintenance
        - memory.md#mem-rte-aggregate-writing
        note: Knowledge retention alone does not establish original trace input on every route. Document
          bytes and source annotations are not automatically sessions/tool traces; aggregate execution
          and other host updates are unresolved.
      records:
      - memory.md#mem-obj-declined
      - memory.md#mem-rte-vector-maintenance
      - memory.md#mem-bap-projection-control
      - memory.md#mem-obj-weaver-checkpoint
      - memory.md#mem-rte-graph-maintenance
      - runtime.md#rt-obj-job-params
      - runtime.md#rt-rte-mark-detection
      - runtime.md#rt-rte-yield-generation
      - memory.md#mem-obj-graph
      - memory.md#mem-obj-vector-points
      - memory.md#mem-obj-vector-payload
      - memory.md#mem-rte-aggregate-writing
      note: Local qualifying yes findings coexist with unresolved other writes. No system-wide no is inferred
        from fixed model parameters, lack of execution evidence, or lack of demonstrated improvement.
    trace_source:
      assessment: partial
      units:
      - scope: Original runtime extraction outcome used to create remembered decline
        assessment: known
        findings:
        - value: event-streams
          basis: wired
          records:
          - memory.md#mem-obj-declined
          - memory.md#mem-rte-vector-maintenance
          - memory.md#mem-bap-projection-control
          note: The qualifying input is the discrete runtime outcome of extraction (bytes read, no text,
            reason), not the source document treated as a conversation or a tool transcript.
        records:
        - memory.md#mem-obj-declined
        - memory.md#mem-rte-vector-maintenance
        - memory.md#mem-bap-projection-control
        note: Event-stream classification is bounded to the retained extraction outcome that drives the
          decline update.
      - scope: Runtime completion/application progress used for later resume controls
        assessment: known
        findings:
        - value: event-streams
          basis: wired
          records:
          - memory.md#mem-obj-weaver-checkpoint
          - memory.md#mem-rte-graph-maintenance
          - runtime.md#rt-obj-job-params
          - runtime.md#rt-rte-mark-detection
          note: Applied event sequence and completed-unit/cursor progress encode runtime activity used
            to advance durable resume state.
        records:
        - memory.md#mem-obj-weaver-checkpoint
        - memory.md#mem-rte-graph-maintenance
        - runtime.md#rt-obj-job-params
        - runtime.md#rt-rte-mark-detection
        note: No conversational turns, recorded tool request/result transcript, or linked state-action-outcome
          trajectory is established on these progress routes.
      - scope: Original inputs of unresolved trace-fed alternatives
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-yield-generation
        - runtime.md#rt-rte-mark-detection
        - memory.md#mem-obj-graph
        - memory.md#mem-rte-graph-maintenance
        - memory.md#mem-obj-vector-points
        - memory.md#mem-obj-vector-payload
        - memory.md#mem-rte-vector-maintenance
        - memory.md#mem-rte-aggregate-writing
        note: Qualifying trace learning and original trace content are not fully determined for the other
          included alternatives; wrapping imported document content as an event does not add an event-stream
          source.
      records:
      - memory.md#mem-obj-declined
      - memory.md#mem-rte-vector-maintenance
      - memory.md#mem-bap-projection-control
      - memory.md#mem-obj-weaver-checkpoint
      - memory.md#mem-rte-graph-maintenance
      - runtime.md#rt-obj-job-params
      - runtime.md#rt-rte-mark-detection
      - runtime.md#rt-rte-yield-generation
      - memory.md#mem-obj-graph
      - memory.md#mem-obj-vector-points
      - memory.md#mem-obj-vector-payload
      - memory.md#mem-rte-aggregate-writing
      note: Event-stream findings attach to specific outcome/progress-fed writes. Other inputs remain
        unresolved; no session-logs, tool-traces or trajectories value follows from adapter labels or
        general agent activity.
---

# Semiont memory profile

## Comparison rationale

This revision-2 comparison classifies the accepted records, not a running deployment. Every axis remains partial: inspected paths establish positive findings, while included host, admission, content and backend alternatives remain unresolved. Wired means an inspected mechanism, not observed activation, factual accuracy or causal benefit.

The resource file, historical event envelope, annotation prose, symbolic anchors, graph structure, vector dimensions and readable search payload are different operative parts. A KB working-tree file is classified as files, not repo merely because Archivist stages it. Queue-backed retained jobs are service objects; no unrecorded storage engine is inferred. External inference weights are not accumulated KB memory. See [MEM-OBJ-content](memory.md#mem-obj-content), [MEM-RTE-record-replay](memory.md#mem-rte-record-replay), [RT-OBJ-job-params](runtime.md#rt-obj-job-params) and [MEM-OBJ-vector-points](memory.md#mem-obj-vector-points).

Lineage describes acquisition or derivation, not truth or human approval. Direct bytes are imported, model compositions are authored, and deterministic replay/extraction/embedding is other-compiled. Outcome/progress controls are trace-extracted at their own update paths. Generic caller identity cannot establish manual admission; the inspected Worker and follower writes are automatic. The uninspected restoration alternative cannot inherit live-command guarantees. See [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission), [MEM-RTE-content-revision](memory.md#mem-rte-content-revision), [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection) and [MEM-RTE-vector-maintenance](memory.md#mem-rte-vector-maintenance).

Knowledge supply, candidate ranking and maintenance routing are independent forces. Retained assignments/vocabulary can also validate and enforce admission. Assessment prose is advisory knowledge, not standing instruction or an automatic truth veto. Learning authority of an extraction outcome at its updater differs from routing authority of the resulting remembered decline at startup. These mappings do not assert learned model weights or improved capacity. See [MEM-OBJ-annotation-text](memory.md#mem-obj-annotation-text), [MEM-RTE-reference-search](memory.md#mem-rte-reference-search), [MEM-BAP-projection-control](memory.md#mem-bap-projection-control) and [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission).

The reconciliation supersedes the epistemic reference-search declaration with [MEM-RTE-reference-search](memory.md#mem-rte-reference-search). All ranking findings use that canonical route; supersession does not strengthen evidence. The retained disagreement over the workflow's unqualified citation/completion sentence is not used as evidence of successful citation storage. [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation) and [EPI-RTE-citation-retention](epistemic.md#epi-rte-citation-retention) establish refusal of this caller's nonempty generated-citation batches. Admitted resource bytes and successful source binding/linking remain separate retained outputs. No profile finding counts those refused citations as memory.

Requested retrieval remains pull even when the service uses embeddings or a model ranker and the Worker clips the response before prompting. Automatic event-targeted maintenance supplies selected retained parts independently of a knowledge-retrieval request; its identifier and coarse progress/compatibility selectors are classified separately. This is not evidence of unsolicited foreground-agent prompt injection. See [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather), [MEM-RTE-resource-gather](memory.md#mem-rte-resource-gather), [MEM-RTE-graph-maintenance](memory.md#mem-rte-graph-maintenance) and [MEM-RTE-vector-maintenance](memory.md#mem-rte-vector-maintenance).

Content/body revision supports evolve; withdrawal with retained event history supports invalidate; terminal queue pruning supports local decay. Replay and reindexing do not themselves establish semantic consolidation, deduplication or synthesis. Summary/generation requests leave actual meaning changes unresolved, and aggregate composition remains afforded. See [MEM-RTE-annotation-edit](memory.md#mem-rte-annotation-edit), [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection), [EPI-RTE-summary-generation](epistemic.md#epi-rte-summary-generation) and [MEM-RTE-aggregate-writing](memory.md#mem-rte-aggregate-writing).

The trace-learning positives are narrow: extraction outcomes become durable decline controls, and applied/completed activity becomes durable resume controls read at later startups or attempts. These are behavior-shaping artifacts even without new factual claims. Their source is runtime event/progress content, not sessions merely because an agent participates. Other generation and projection routes retain unresolved trace qualification; imported document content does not become an event-stream source simply by entering the event log. See [MEM-OBJ-declined](memory.md#mem-obj-declined), [MEM-RTE-vector-maintenance](memory.md#mem-rte-vector-maintenance), [MEM-OBJ-weaver-checkpoint](memory.md#mem-obj-weaver-checkpoint) and [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection).

Source-read log: none. This profile adds no source evidence or declarations and does not reopen report verification. Missing facts stay beside their scoped findings rather than being filled from unrecorded source facts.
