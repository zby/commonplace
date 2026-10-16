---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Signet memory comparison: retained evidence, semantic heads/graph, summaries, retrieval
  feedback and benchmark checkpoint alternatives.'
run-id: AAS-2026-10-14-signetai-64f703d83203-01
source-identity: https://github.com/signet-ai/signetai
reviewed-boundary: 12dba1ce753babda735f2ba7b6f150c6c0b7f95e
memory-comparison:
  version: 2
  scope: Accumulated captured/caller/imported evidence and access structures; semantic graph and curated
    head/projection; maintenance history/runbook; host compaction/recovery and hierarchy/thread-head alternatives;
    edited identity/authored working memory; retrieval vectors and feedback state; retained benchmark
    phase/results and unresolved optimization, provider/native-source, coordination and backup/recovery
    routes. Excludes unchanged shipped instructions, current-invocation prompts/staging buffers, external
    model weights/host internals, and secrets merely stored as opaque nonsemantic payloads.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Remembered rows and semantic aggregate notes
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-memories
          - epistemic.md#epi-obj-aggregate-answer
          note: Content and eligibility metadata inhabit SQLite memories.
        records:
        - memory.md#mem-obj-memories
        - epistemic.md#epi-obj-aggregate-answer
        note: SQLite backing is established for these retained rows.
      - scope: Canonical session transcripts and completed session content
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-session-transcripts
          note: Canonical turns are retained in JSONL files.
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-session-transcripts
          note: Completed session content is retained in SQLite.
        records:
        - memory.md#mem-obj-session-transcripts
        note: Files and database content are separate retained parts.
      - scope: Curated head, revisions, entries and filesystem projection
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-memory-head
          note: Head state, revisions and provenance are database-backed.
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-memory-head
          note: MEMORY.md is a filesystem projection, potentially stale or unpublished.
        records:
        - memory.md#mem-obj-memory-head
        note: Database retention and file publication have different failure boundaries.
      - scope: Entity/aspect/attribute state and projections
        assessment: known
        findings:
        - value: graph
          basis: wired
          records:
          - memory.md#mem-obj-entity-attributes
          note: Entities, attributes and relationships form retained graph state.
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-entity-attributes
          note: Graph and linked projection rows are retained in SQLite.
        records:
        - memory.md#mem-obj-entity-attributes
        note: Graph is the operative access structure; SQLite is its backing substrate.
      - scope: Dense retrieval representations
        assessment: partial
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-cmp-embedding-provider
          note: Generated embeddings can be stored in SQLite.
        - value: vector
          basis: wired
          records:
          - memory.md#mem-cmp-embedding-provider
          note: Dense representations are retained in vector indexes.
        records:
        - memory.md#mem-cmp-embedding-provider
        - memory.md#mem-rte-aggregate-recall
        note: Stored vectors are known; every alternative provider/index implementation is not.
      - scope: Maintenance history and feedback events/weights
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-dreaming-history
          - memory.md#mem-obj-path-feedback
          note: History nodes and feedback selection state are SQLite material.
        records:
        - memory.md#mem-obj-dreaming-history
        - memory.md#mem-obj-path-feedback
        note: Both named persistent stores are database-backed.
      - scope: Edited identity and authored working-memory files
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-identity-files
          note: The inspected reader consumes filesystem Markdown.
        records:
        - memory.md#mem-obj-identity-files
        note: Only accumulated edits and authored working memory are included, not unchanged installation
          prompts.
      - scope: Host compaction summary rows and alternative artifacts/checkpoints
        assessment: partial
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-session-summaries
          - memory.md#mem-obj-memories
          note: Host compaction text is inserted as a session-summary memory row.
        records:
        - memory.md#mem-obj-session-summaries
        - memory.md#mem-obj-memories
        note: Summary insertion into the memory store establishes SQLite for the row; artifact, snapshot
          and hierarchy backing remain incompletely recorded.
      - scope: Imported artifacts and benchmark checkpoints
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-artifacts
        - memory.md#mem-obj-run-checkpoint
        note: Logical retention is established, but complete physical storage/serialization for these
          parts is not recorded.
      - scope: Other provider/native-source retained state, hierarchy/thread heads, backup and coordination
          state
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-artifacts
        - memory.md#mem-obj-session-summaries
        - memory.md#mem-obj-identity-files
        - memory.md#mem-obj-run-checkpoint
        note: Included alternatives are mapped but storage and recovery details remain unread. Secret
          storage alone is excluded from semantic memory; accumulated coordination state remains unresolved.
      records:
      - memory.md#mem-obj-memories
      - epistemic.md#epi-obj-aggregate-answer
      - memory.md#mem-obj-session-transcripts
      - memory.md#mem-obj-memory-head
      - memory.md#mem-obj-entity-attributes
      - memory.md#mem-cmp-embedding-provider
      - memory.md#mem-rte-aggregate-recall
      - memory.md#mem-obj-dreaming-history
      - memory.md#mem-obj-path-feedback
      - memory.md#mem-obj-identity-files
      - memory.md#mem-obj-session-summaries
      - memory.md#mem-obj-memory-artifacts
      - memory.md#mem-obj-run-checkpoint
      note: Named SQLite, graph, vector and file witnesses do not enumerate all retained provider, artifact,
        checkpoint and coordination substrates. Transient prompts and staging buffers are excluded.
    representational_form:
      assessment: partial
      units:
      - scope: Retained evidence, transcripts, head bodies, graph claim text and aggregate notes at model/human
          consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-memories
          - memory.md#mem-obj-session-transcripts
          - memory.md#mem-obj-memory-head
          - memory.md#mem-obj-entity-attributes
          - epistemic.md#epi-obj-aggregate-answer
          note: Consumers interpret content as evidence or context.
        records:
        - memory.md#mem-obj-memories
        - memory.md#mem-obj-session-transcripts
        - memory.md#mem-obj-memory-head
        - memory.md#mem-obj-entity-attributes
        - epistemic.md#epi-obj-aggregate-answer
        note: These text parts are distinct from their control envelopes.
      - scope: Scope, lineage, membership, mutation and graph relationship control parts
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-memories
          - memory.md#mem-obj-session-transcripts
          - memory.md#mem-obj-memory-head
          - memory.md#mem-obj-entity-attributes
          note: IDs, flags, relationships and revision membership have fixed code consumers.
        records:
        - memory.md#mem-obj-memories
        - memory.md#mem-obj-session-transcripts
        - memory.md#mem-obj-memory-head
        - memory.md#mem-obj-entity-attributes
        note: Localized identifiers and fixed eligibility rules establish symbolic consumption.
      - scope: Dense embeddings and their profile metadata
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-cmp-embedding-provider
          note: Retrieval vectors are distributed dense representations.
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-cmp-embedding-provider
          note: Profile IDs, dimensions and links are localized metadata.
        records:
        - memory.md#mem-cmp-embedding-provider
        note: Dense numerical form is not synonymous with numerical feedback weights.
      - scope: History lines and runbook/pass text at later maintenance prompts
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-dreaming-history
          note: Leaf/merged lines carry descriptions of prior work.
        records:
        - memory.md#mem-obj-dreaming-history
        note: Rendered history is interpreted by the maintenance model.
      - scope: History indexing/accounting and path-feedback selection state
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-dreaming-history
          - memory.md#mem-obj-path-feedback
          note: Scopes, node links, ratings and aspect weights have fixed code consumers.
        records:
        - memory.md#mem-obj-dreaming-history
        - memory.md#mem-obj-path-feedback
        note: Numeric aspect weights are symbolic under fixed localized update rules.
      - scope: Imported readable projections versus canonical JSON and access metadata
        assessment: partial
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-memory-artifacts
          note: Readable projection text supplies evidence.
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-memory-artifacts
          note: Canonical JSON and lineage/access metadata remain separate.
        records:
        - memory.md#mem-obj-memory-artifacts
        note: Inspected JSON/CSV forms do not resolve other provider payloads.
      - scope: Compaction/recovery summaries, edited identity and benchmark checkpoint text/control
        assessment: partial
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-session-summaries
          - memory.md#mem-obj-identity-files
          - memory.md#mem-obj-run-checkpoint
          note: Summary, guidance, answers and explanations require interpretation.
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-session-summaries
          - memory.md#mem-obj-identity-files
          - memory.md#mem-obj-run-checkpoint
          - epistemic.md#epi-obj-judge-result
          note: Session/hierarchy/configuration/phase status is fixed-rule state.
        records:
        - memory.md#mem-obj-session-summaries
        - memory.md#mem-obj-identity-files
        - memory.md#mem-obj-run-checkpoint
        - epistemic.md#epi-obj-judge-result
        note: Text and structural control parts are both recorded; opaque hierarchy and snapshot details
          prevent complete classification.
      - scope: Opaque provider payloads and accumulated coordination/backup alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-artifacts
        - memory.md#mem-obj-identity-files
        note: An inspected display does not resolve an opaque consumed payload.
      records:
      - memory.md#mem-obj-memories
      - memory.md#mem-obj-session-transcripts
      - memory.md#mem-obj-memory-head
      - memory.md#mem-obj-entity-attributes
      - epistemic.md#epi-obj-aggregate-answer
      - memory.md#mem-cmp-embedding-provider
      - memory.md#mem-obj-dreaming-history
      - memory.md#mem-obj-path-feedback
      - memory.md#mem-obj-memory-artifacts
      - memory.md#mem-obj-session-summaries
      - memory.md#mem-obj-identity-files
      - memory.md#mem-obj-run-checkpoint
      - epistemic.md#epi-obj-judge-result
      note: Text, symbolic controls and dense vectors coexist. Uninspected payloads and alternative consumers
        prevent a complete form inventory; provider model weights are not accumulated Signet memory.
    lineage:
      assessment: partial
      units:
      - scope: Captured canonical session evidence
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-session-transcripts
          - memory.md#mem-rte-transcript-capture
          note: Host activity supplies retained session turns.
        records:
        - memory.md#mem-obj-session-transcripts
        - memory.md#mem-rte-transcript-capture
        note: Processing strips injected context and canonicalizes turns rather than retaining every original
          byte.
      - scope: Caller-supplied memories and imported document parts
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - runtime.md#rt-rte-direct-remember
          - memory.md#mem-obj-memory-artifacts
          note: External caller text/documents enter retained evidence.
        records:
        - runtime.md#rt-rte-direct-remember
        - memory.md#mem-obj-memories
        - memory.md#mem-obj-memory-artifacts
        note: Acquisition is known, but caller authorship and every provider derivation are unresolved.
      - scope: Derived head and graph claims from retained session evidence
        assessment: partial
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-rte-dreaming-pass
          - memory.md#mem-rte-transcript-capture
          - memory.md#mem-obj-memory-head
          note: Captured session evidence can feed semantic/head writes.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-memory-head
          - memory.md#mem-obj-entity-attributes
          - runtime.md#rt-rte-dreaming-pass
          note: Models and daemon operations compile retained evidence into curated entries and graph
            projections.
        records:
        - runtime.md#rt-rte-dreaming-pass
        - memory.md#mem-obj-memory-head
        - memory.md#mem-obj-entity-attributes
        - memory.md#mem-rte-transcript-capture
        note: Trace-fed derivation is included alongside imported and other evidence; initial graph lineage
          and every operation remain unresolved.
      - scope: Maintenance history leaf and parent summaries
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-dreaming-history
          - memory.md#mem-rte-history-compaction
          note: Selected pass/tool activity feeds leaf lines.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-rte-history-compaction
          note: Adjacent retained child lines feed merged parents.
        records:
        - memory.md#mem-obj-dreaming-history
        - memory.md#mem-rte-history-compaction
        note: Leaf extraction and parent compression are separately supported.
      - scope: Aggregate semantic notes and embeddings
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-rte-aggregate-recall
          - memory.md#mem-cmp-embedding-provider
          note: Synthesis and embedding transforms create derived retained parts.
        records:
        - memory.md#mem-rte-aggregate-recall
        - memory.md#mem-cmp-embedding-provider
        note: Compilation is wired; original evidence/provider provenance is not completely resolved.
      - scope: Host summaries/checkpoints, authored identity alternatives and feedback state
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-session-summaries
          note: The daemon receives a host-produced summary.
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-identity-files
          note: Authored MEMORY.md is a retained alternative to generated projection; author identity/control
            is unresolved.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-path-feedback
          note: Fixed formulas derive weights from ratings and recorded retrieval paths.
        records:
        - memory.md#mem-obj-session-summaries
        - memory.md#mem-obj-identity-files
        - memory.md#mem-obj-path-feedback
        note: Host-provided summary import and feedback derivation are known, but initial authorship/approval
          and complete original inputs are not.
      - scope: Benchmark result checkpoint payload
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - epistemic.md#epi-rte-benchmark-checkpoint
          note: Evaluator results become checkpoint phase data.
        records:
        - memory.md#mem-obj-run-checkpoint
        - epistemic.md#epi-rte-benchmark-checkpoint
        note: Scores and explanations derive from evaluation; reference creation and all phase origins
          are unresolved.
      - scope: Other provider sources, hierarchy/thread heads, identity propagation, backup and coordination
          origins
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-artifacts
        - memory.md#mem-obj-session-summaries
        - memory.md#mem-obj-identity-files
        note: These included origins were not traced.
      records:
      - memory.md#mem-obj-session-transcripts
      - memory.md#mem-rte-transcript-capture
      - runtime.md#rt-rte-direct-remember
      - memory.md#mem-obj-memories
      - memory.md#mem-obj-memory-artifacts
      - runtime.md#rt-rte-dreaming-pass
      - memory.md#mem-obj-memory-head
      - memory.md#mem-obj-entity-attributes
      - memory.md#mem-obj-dreaming-history
      - memory.md#mem-rte-history-compaction
      - memory.md#mem-rte-aggregate-recall
      - memory.md#mem-cmp-embedding-provider
      - memory.md#mem-obj-session-summaries
      - memory.md#mem-obj-identity-files
      - memory.md#mem-obj-path-feedback
      - memory.md#mem-obj-run-checkpoint
      - epistemic.md#epi-rte-benchmark-checkpoint
      note: Known derivation paths do not resolve initial content or embedding provenance. Authored does
        not imply manual admission; imported session summaries do not establish complete trace origin.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retained content at foreground lookup/startup and maintenance evidence consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-rte-explicit-recall
          - runtime.md#rt-bap-host-context
          - memory.md#mem-obj-memory-head
          - memory.md#mem-obj-entity-attributes
          note: Selected facts and head bodies reach model-input/tool channels.
        records:
        - memory.md#mem-obj-memories
        - memory.md#mem-rte-explicit-recall
        - runtime.md#rt-bap-host-context
        - memory.md#mem-obj-memory-head
        - memory.md#mem-obj-entity-attributes
        note: Delivered text supplies reference/context, not host action permission.
      - scope: Accumulated identity edits at foreground guidance consumer
        assessment: partial
        findings:
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-obj-identity-files
          note: Identity/preferences supply host guidance.
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-identity-files
          note: Background and authored working memory supply context.
        records:
        - memory.md#mem-obj-identity-files
        note: Only edited/maintained material is scoped; static shipped templates are excluded.
      - scope: Evidence text and access structures at retrieval selectors
        assessment: partial
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-rte-explicit-recall
          - memory.md#mem-cmp-embedding-provider
          - memory.md#mem-bap-feedback-selection
          note: Retained content/features and aspect weights affect relative retrieval priority.
        records:
        - memory.md#mem-rte-explicit-recall
        - memory.md#mem-cmp-embedding-provider
        - memory.md#mem-obj-entity-attributes
        - memory.md#mem-obj-path-feedback
        - memory.md#mem-bap-feedback-selection
        note: Text, vectors, graph features and localized weights influence selection; complete alternate
          ranking policies remain unresolved.
      - scope: Eligibility/provenance/scope state at head and current-memory admission/read consumers
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - epistemic.md#epi-rte-head-support
          - memory.md#mem-obj-memory-head
          note: Retained source/currentness/provenance state determines admissible support and carried
            entries.
        - value: enforcement
          basis: wired
          records:
          - epistemic.md#epi-rte-head-support
          - memory.md#mem-rte-state-withdrawal
          - epistemic.md#epi-rte-memory-supersession
          note: Deleted/stale/superseded or invalid supports are vetoed at inspected consumers.
        records:
        - memory.md#mem-obj-memory-head
        - epistemic.md#epi-rte-head-support
        - memory.md#mem-rte-state-withdrawal
        - epistemic.md#epi-rte-memory-supersession
        note: Checks have bounded correspondence and eligibility force; successful NOOP is not fresh support
          validation.
      - scope: Trace-derived evidence/history and feedback at durable update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-rte-transcript-capture
          - runtime.md#rt-rte-dreaming-pass
          - memory.md#mem-rte-history-compaction
          - memory.md#mem-rte-path-feedback
          note: Session/pass experience and retrieval feedback feed durable semantic, summary and selector
            updates.
        records:
        - memory.md#mem-rte-transcript-capture
        - runtime.md#rt-rte-dreaming-pass
        - memory.md#mem-rte-history-compaction
        - memory.md#mem-rte-path-feedback
        note: Learning authority names the update input, separately from downstream knowledge/ranking
          and without demonstrated improvement.
      - scope: History and recovery material at subsequent model invocations
        assessment: partial
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-rte-history-compaction
          - memory.md#mem-obj-session-summaries
          note: Later maintenance/foreground invocations receive historical context.
        records:
        - memory.md#mem-obj-dreaming-history
        - memory.md#mem-rte-history-compaction
        - memory.md#mem-obj-session-summaries
        note: Selected summaries supply context; no blanket standing-instruction classification follows.
      - scope: Retained checkpoint phase status at benchmark resume consumer
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - epistemic.md#epi-rte-benchmark-checkpoint
          note: Phase status selects which questions are evaluated on resume.
        records:
        - epistemic.md#epi-rte-benchmark-checkpoint
        - memory.md#mem-obj-run-checkpoint
        note: Completed evaluations are skipped; judge explanations are not established product-memory
          validation criteria.
      - scope: Untraced provider, hierarchy, identity-propagation, backup and coordination consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-artifacts
        - memory.md#mem-obj-session-summaries
        - memory.md#mem-obj-identity-files
        note: Force cannot be inferred from storage or opaque payload labels.
      records:
      - memory.md#mem-obj-memories
      - memory.md#mem-rte-explicit-recall
      - runtime.md#rt-bap-host-context
      - memory.md#mem-obj-memory-head
      - memory.md#mem-obj-entity-attributes
      - memory.md#mem-obj-identity-files
      - memory.md#mem-cmp-embedding-provider
      - memory.md#mem-obj-path-feedback
      - memory.md#mem-bap-feedback-selection
      - epistemic.md#epi-rte-head-support
      - memory.md#mem-rte-state-withdrawal
      - epistemic.md#epi-rte-memory-supersession
      - memory.md#mem-rte-transcript-capture
      - runtime.md#rt-rte-dreaming-pass
      - memory.md#mem-rte-history-compaction
      - memory.md#mem-rte-path-feedback
      - memory.md#mem-obj-dreaming-history
      - memory.md#mem-obj-session-summaries
      - epistemic.md#epi-rte-benchmark-checkpoint
      - memory.md#mem-obj-run-checkpoint
      - memory.md#mem-obj-memory-artifacts
      note: 'Authority is consumer-relative: knowledge/instruction, ranking, learning inputs, enforcing
        validation and checkpoint routing have separate witnesses. Untraced consumers prevent a whole-boundary
        union from being complete.'
    write_agency:
      assessment: partial
      units:
      - scope: Terminal capture, history compression, Dreaming proposals/head finalization and aggregate-note
          admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-transcript-capture
          - memory.md#mem-rte-history-compaction
          - runtime.md#rt-rte-dreaming-pass
          - workflow.md#wf-rte-head-finalization
          - memory.md#mem-rte-aggregate-recall
          note: Code/model gates admit these writes even when a human starts a pass or request.
        records:
        - memory.md#mem-rte-transcript-capture
        - memory.md#mem-rte-history-compaction
        - runtime.md#rt-rte-dreaming-pass
        - workflow.md#wf-rte-head-finalization
        - memory.md#mem-rte-aggregate-recall
        note: Software/model admission does not await human per-content approval.
      - scope: Document importer and host-summary persistence
        assessment: partial
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-memory-artifacts
          - memory.md#mem-obj-session-summaries
          note: Daemon admission retains supplied documents/host summaries without a recorded per-content
            human gate.
        records:
        - memory.md#mem-obj-memory-artifacts
        - memory.md#mem-obj-session-summaries
        note: Inspected daemon persistence is automatic; upstream host summary production and all importer
          alternatives remain unresolved.
      - scope: Direct remember, modify/withdrawal and caller-rating submission
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-direct-remember
        - memory.md#mem-obj-memories
        - memory.md#mem-rte-state-withdrawal
        - memory.md#mem-rte-path-feedback
        note: Generic HTTP caller origin does not resolve human supply/approval; downstream feedback propagation
          has its own mechanism.
      - scope: Feedback weight/statistic propagation
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-path-feedback
          note: Fixed code updates persistent selector state from admitted feedback.
        records:
        - memory.md#mem-rte-path-feedback
        note: This is distinct from unresolved upstream rating authorship.
      - scope: Benchmark checkpoint phase update
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - epistemic.md#epi-rte-benchmark-checkpoint
          note: Evaluation results automatically update checkpoint phases.
        records:
        - epistemic.md#epi-rte-benchmark-checkpoint
        note: Orchestrator, not a per-result human decision, writes completion/failure state.
      - scope: Identity initialization/editing, source synchronization, backup replacement, other adapters
          and hierarchy writes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-identity-files
        - memory.md#mem-obj-memory-artifacts
        - memory.md#mem-obj-session-summaries
        note: Initial content approval and alternative admission controls remain uninspected; no manual
          finding is warranted from authored filenames alone.
      records:
      - memory.md#mem-rte-transcript-capture
      - memory.md#mem-rte-history-compaction
      - runtime.md#rt-rte-dreaming-pass
      - workflow.md#wf-rte-head-finalization
      - memory.md#mem-rte-aggregate-recall
      - memory.md#mem-obj-memory-artifacts
      - memory.md#mem-obj-session-summaries
      - runtime.md#rt-rte-direct-remember
      - memory.md#mem-obj-memories
      - memory.md#mem-rte-state-withdrawal
      - memory.md#mem-rte-path-feedback
      - epistemic.md#epi-rte-benchmark-checkpoint
      - memory.md#mem-obj-identity-files
      note: Automatic admission has concrete witnesses. Arbitrary caller control, identity editing and
        recovery alternatives remain unresolved; no explicit human per-content decision is recorded strongly
        enough to add manual.
    curation_operations:
      assessment: partial
      units:
      - scope: Maintenance-history leaf extraction and pairwise parent compression
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-history-compaction
          note: Implemented extraction/merging compresses retained work descriptions.
        records:
        - memory.md#mem-rte-history-compaction
        - memory.md#mem-obj-dreaming-history
        note: Retained selected pass records and child lines become reduced summaries while children remain
          reachable.
      - scope: Aggregate-note duplicate handling and duplicate refresh
        assessment: partial
        findings:
        - value: dedup
          basis: wired
          records:
          - memory.md#mem-rte-aggregate-recall
          note: Eligible aggregates are normalized and deduplicated.
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-aggregate-recall
          note: Duplicate refresh can revise existing aggregate memory.
        records:
        - memory.md#mem-rte-aggregate-recall
        note: Normalization/deduplication and refreshing an existing note are wired; semantic novelty
          of synthesis is not established.
      - scope: Mutable memory and complete-head revision paths
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-state-withdrawal
          - memory.md#mem-obj-memory-head
          - epistemic.md#epi-rte-head-publication
          note: Modify/replacement and changed head membership revise retained state.
        records:
        - memory.md#mem-rte-state-withdrawal
        - memory.md#mem-obj-memory-head
        - epistemic.md#epi-rte-head-publication
        note: Supported revision paths coexist with immutable episodic rows and NOOP branches.
      - scope: Tombstone, supersession, linked staleness and head freshness withdrawal
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-rte-state-withdrawal
          - epistemic.md#epi-rte-memory-supersession
          note: Deleted/superseded/stale status withholds future current-memory reliance.
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-state-withdrawal
          note: Forget removes a row from ordinary current reliance; this is forgetting, not a demonstrated
            time-based downweighting policy.
        records:
        - memory.md#mem-rte-state-withdrawal
        - epistemic.md#epi-rte-memory-supersession
        note: History can remain while current reliance is withdrawn; erasure from prior host context
          is not guaranteed.
      - scope: Requested head condensation
        assessment: partial
        findings:
        - value: consolidate
          basis: claimed
          records:
          - workflow.md#wf-rte-head-finalization
          note: The head tool requests reduction of existing retained entries to fit the budget.
        records:
        - workflow.md#wf-rte-head-finalization
        note: The tool instructs the model to condense/drop entries; no execution proves compliance.
      - scope: Semantic transformation of Dreaming claims and aggregate notes
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-dreaming-pass
        - epistemic.md#epi-rte-aggregate-synthesis
        note: Recorded requests do not establish whether realized content preserves existing claims, derives
          or adds a claim. No synthesize finding follows solely from the route name.
      - scope: Other ontology operations, source synchronization, hierarchy summaries, recovery and optimization
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-entity-attributes
        - memory.md#mem-obj-memory-artifacts
        - memory.md#mem-obj-session-summaries
        - memory.md#mem-obj-run-checkpoint
        note: Mapped alternatives lack operation-level transformation coverage; promote and other operations
          cannot be ruled out.
      records:
      - memory.md#mem-rte-history-compaction
      - memory.md#mem-obj-dreaming-history
      - memory.md#mem-rte-aggregate-recall
      - memory.md#mem-rte-state-withdrawal
      - memory.md#mem-obj-memory-head
      - epistemic.md#epi-rte-head-publication
      - epistemic.md#epi-rte-memory-supersession
      - workflow.md#wf-rte-head-finalization
      - runtime.md#rt-rte-dreaming-pass
      - epistemic.md#epi-rte-aggregate-synthesis
      - memory.md#mem-obj-entity-attributes
      - memory.md#mem-obj-memory-artifacts
      - memory.md#mem-obj-session-summaries
      - memory.md#mem-obj-run-checkpoint
      note: Implemented consolidation, deduplication, revision and withdrawal coexist with requested condensation
        and unresolved semantic novelty. No route name establishes synthesis or promotion.
    read_back_direction:
      assessment: partial
      units:
      - scope: Explicit Pi/MCP/CLI recall and maintenance zoom/evidence requests
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-explicit-recall
          - memory.md#mem-rte-history-compaction
          note: Explicit lookup and zoom fulfill consumer requests.
        records:
        - memory.md#mem-rte-explicit-recall
        - memory.md#mem-rte-history-compaction
        - memory.md#mem-rte-transcript-capture
        note: The consumer requests retained material; returning it is not a second unsolicited push.
      - scope: Pi startup automatic background selection and hidden context delivery
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-pi-lifecycle
          - runtime.md#rt-bap-host-context
          note: Signet automatically supplies selected retained startup context.
        records:
        - runtime.md#rt-rte-pi-lifecycle
        - runtime.md#rt-bap-host-context
        - memory.md#mem-obj-memory-head
        - memory.md#mem-obj-session-summaries
        note: A lifecycle request triggers automatic selection of accumulated context, not an item-specific
          memory request.
      - scope: Scoped history injection into later maintenance prompts
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-history-compaction
          - runtime.md#rt-obj-pass-prompt
          note: Folded history is supplied when a fresh maintenance prompt is built.
        records:
        - memory.md#mem-rte-history-compaction
        - memory.md#mem-obj-dreaming-history
        - runtime.md#rt-obj-pass-prompt
        note: Initial history is automatic; zoom is separately requested.
      - scope: Saved aggregate notes at later ordinary recall
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-aggregate-recall
          - memory.md#mem-rte-explicit-recall
          note: Saved aggregates participate in later requested current-memory recall.
        records:
        - memory.md#mem-rte-aggregate-recall
        - memory.md#mem-rte-explicit-recall
        note: Immediate unsaved synthesis is not accumulated-memory read-back.
      - scope: Benchmark checkpoint phase reload on resume
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - epistemic.md#epi-rte-benchmark-checkpoint
          note: getPhaseStatus fulfills the resume consumer’s checkpoint read.
        records:
        - epistemic.md#epi-rte-benchmark-checkpoint
        note: The resumed orchestrator reads retained phase status rather than receiving independent background
          injection.
      - scope: Other hosts, provider/native-source consumers, hierarchy/thread heads and backup/coordination
          consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-artifacts
        - memory.md#mem-obj-session-summaries
        - memory.md#mem-obj-identity-files
        - memory.md#mem-obj-run-checkpoint
        note: These included read-back routes remain untraced; object storage alone supplies no direction.
      records:
      - memory.md#mem-rte-explicit-recall
      - memory.md#mem-rte-history-compaction
      - memory.md#mem-rte-transcript-capture
      - runtime.md#rt-rte-pi-lifecycle
      - runtime.md#rt-bap-host-context
      - memory.md#mem-obj-memory-head
      - memory.md#mem-obj-session-summaries
      - memory.md#mem-obj-dreaming-history
      - runtime.md#rt-obj-pass-prompt
      - memory.md#mem-rte-aggregate-recall
      - epistemic.md#epi-rte-benchmark-checkpoint
      - memory.md#mem-obj-memory-artifacts
      - memory.md#mem-obj-identity-files
      - memory.md#mem-obj-run-checkpoint
      note: Both requested read-back and unsolicited selection exist. Pi/history witnesses do not resolve
        every shipped adapter or provider route.
    read_back_signal:
      assessment: partial
      units:
      - scope: Startup ranked memories and graph constraints
        assessment: partial
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-pi-lifecycle
          note: Session start triggers availability/scope and budget filtering of retained candidates.
        records:
        - runtime.md#rt-rte-pi-lifecycle
        - memory.md#mem-rte-explicit-recall
        - memory.md#mem-obj-entity-attributes
        note: Agent/project policy, scoring, focal entities and budgets are recorded, but all ranking/predictor
          internals are not. No lexical/embedding startup finding is inferred from explicit-recall capability
          alone.
      - scope: Current working-memory/identity sections selected at startup
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-identity-files
          - memory.md#mem-obj-memory-head
          - workflow.md#wf-rte-head-finalization
          note: Startup supplies eligible edited sections/current head under configured budgets.
        records:
        - memory.md#mem-obj-identity-files
        - memory.md#mem-obj-memory-head
        - workflow.md#wf-rte-head-finalization
        note: Configured inclusion, freshness and budget supply whole retained sections; a path alone
          does not establish targeted identity matching.
      - scope: Maintenance history stream selection and folding
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-obj-dreaming-history
          - memory.md#mem-rte-history-compaction
          note: Actual matching stream-scope IDs select retained history for the pass.
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-history-compaction
          note: Available parent nodes and byte-target folding bound the selected scoped view.
        records:
        - memory.md#mem-obj-dreaming-history
        - memory.md#mem-rte-history-compaction
        note: Trigger is new pass construction; allowed stream scopes select history nodes, then level/byte-target
          folding limits the delivered lines.
      - scope: Checkpoint recovery, continuity, inherited context and predicted startup context
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-summaries
        - runtime.md#rt-rte-pi-lifecycle
        note: Startup includes these alternatives, but complete selectors/input lineage are not recorded.
          Session labels alone do not establish an identifier-selection finding.
      - scope: Explicit recall/zoom and benchmark checkpoint reload
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-explicit-recall
        - memory.md#mem-rte-history-compaction
        - epistemic.md#epi-rte-benchmark-checkpoint
        note: These named operations are pull; push-signal classification does not apply to their requested
          return. Maintenance initial injection remains a separate applicable unit.
      - scope: Other adapter/source/hierarchy automatic deliveries
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-artifacts
        - memory.md#mem-obj-session-summaries
        - memory.md#mem-obj-identity-files
        note: Untraced alternatives cannot be declared pull-only or signal-inapplicable.
      records:
      - runtime.md#rt-rte-pi-lifecycle
      - memory.md#mem-rte-explicit-recall
      - memory.md#mem-obj-entity-attributes
      - memory.md#mem-obj-identity-files
      - memory.md#mem-obj-memory-head
      - workflow.md#wf-rte-head-finalization
      - memory.md#mem-obj-dreaming-history
      - memory.md#mem-rte-history-compaction
      - memory.md#mem-obj-session-summaries
      - epistemic.md#epi-rte-benchmark-checkpoint
      - memory.md#mem-obj-memory-artifacts
      note: Recorded push selection supports coarse gating and scope-identifier history matching. Explicit
        recall query selectors do not classify startup push. Missing startup predictor and alternative-selector
        facts prevent complete signal classification.
    trace_learning:
      assessment: partial
      units:
      - scope: Captured session evidence to semantic/head maintenance to later context
        assessment: partial
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-transcript-capture
          - runtime.md#rt-rte-dreaming-pass
          - memory.md#mem-obj-memory-head
          - runtime.md#rt-bap-host-context
          note: Session traces can produce durable behavior-shaping semantic/head content automatically.
        records:
        - memory.md#mem-rte-transcript-capture
        - runtime.md#rt-rte-dreaming-pass
        - memory.md#mem-obj-memory-head
        - runtime.md#rt-bap-host-context
        note: Automatic evidence-fed semantic/head writes have later context consumers; actual improvement
          and every alternate evidence source remain unresolved.
      - scope: Pass/tool activity to history leaf/parent lines to later maintenance prompt
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-history-compaction
          - memory.md#mem-obj-dreaming-history
          note: Automatic trace-fed summaries persist and reach later maintenance invocations.
        records:
        - memory.md#mem-rte-history-compaction
        - memory.md#mem-obj-dreaming-history
        note: This generated continuation-context chain qualifies without proving new knowledge or improved
          decisions.
      - scope: Session retrieval records plus ratings to aspect weights to later traversal
        assessment: partial
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-path-feedback
          - memory.md#mem-bap-feedback-selection
          note: Recorded retrieval experience and ratings alter durable ordering state consumed later.
        records:
        - memory.md#mem-rte-path-feedback
        - memory.md#mem-obj-path-feedback
        - memory.md#mem-bap-feedback-selection
        note: Automatic propagation is known even though upstream rating agency/origin and other statistics
          consumers remain unresolved.
      - scope: Host compaction summary and recovery/hierarchical alternatives
        assessment: partial
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-session-summaries
          - runtime.md#rt-rte-pi-lifecycle
          note: Host-generated compaction context is automatically retained and can shape later invocations;
            opaque original content does not erase this route.
        records:
        - memory.md#mem-obj-session-summaries
        - runtime.md#rt-rte-pi-lifecycle
        note: Host compaction produces a retained continuation summary and automatic daemon ingestion
          makes it available to later memory/head consumers. Original turn types, surviving tail and hierarchy
          alternatives remain unresolved.
      - scope: Aggregate recall from mixed evidence, caller memory, imported sources and benchmark/optimization
          alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-aggregate-recall
        - memory.md#mem-obj-memory-artifacts
        - memory.md#mem-obj-run-checkpoint
        - runtime.md#rt-rte-direct-remember
        note: Automatic aggregate admission is known, but a qualifying original trace input is not fixed
          for all saved notes. Benchmark retention alone does not establish a behavior-shaping update;
          optimization alternatives remain unread.
      - scope: Other hierarchy, identity-maintenance, source-provider and coordination update routes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-session-summaries
        - memory.md#mem-obj-identity-files
        - memory.md#mem-obj-memory-artifacts
        note: Neither qualifying writes nor bounded absence were established for these included alternatives.
      records:
      - memory.md#mem-rte-transcript-capture
      - runtime.md#rt-rte-dreaming-pass
      - memory.md#mem-obj-memory-head
      - runtime.md#rt-bap-host-context
      - memory.md#mem-rte-history-compaction
      - memory.md#mem-obj-dreaming-history
      - memory.md#mem-rte-path-feedback
      - memory.md#mem-obj-path-feedback
      - memory.md#mem-bap-feedback-selection
      - memory.md#mem-obj-session-summaries
      - runtime.md#rt-rte-pi-lifecycle
      - memory.md#mem-rte-aggregate-recall
      - memory.md#mem-obj-memory-artifacts
      - memory.md#mem-obj-run-checkpoint
      - runtime.md#rt-rte-direct-remember
      - memory.md#mem-obj-identity-files
      note: Four wired trace-fed update/continuation chains establish yes locally, including host compaction
        summaries. No bounded absence record warrants no for unresolved routes, and no observed benefit
        or learned provider parameters is claimed.
    trace_source:
      assessment: partial
      units:
      - scope: Canonical session input to semantic/head trace-fed maintenance
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-obj-session-transcripts
          - memory.md#mem-rte-transcript-capture
          note: Recorded host session turns supply the qualifying session-fed maintenance route.
        records:
        - memory.md#mem-obj-session-transcripts
        - memory.md#mem-rte-transcript-capture
        - runtime.md#rt-rte-dreaming-pass
        - memory.md#mem-obj-memory-head
        note: Conversational turns are known; all host turn types and mixed imported/other inputs are
          not enumerated.
      - scope: Maintenance pass/tool records feeding history summaries
        assessment: partial
        findings:
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-obj-dreaming-history
          - memory.md#mem-rte-history-compaction
          note: Retained pass/tool activity supplies history leaf extraction.
        records:
        - memory.md#mem-obj-dreaming-history
        - memory.md#mem-rte-history-compaction
        note: Selected operation/tool results and completion/error views are recorded, not a full model
          reasoning trajectory.
      - scope: Retrieval/path activity and opaque upstream ratings feeding weights
        assessment: partial
        findings:
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-rte-path-feedback
          - memory.md#mem-obj-path-feedback
          note: Recorded retrieval membership/path experience feeds the automatic selector-state update.
        records:
        - memory.md#mem-obj-path-feedback
        - memory.md#mem-rte-path-feedback
        note: Session-recorded retrieval IDs and paths are recorded tool-use experience; rating origin
          remains unresolved and is not silently treated as a session log or environmental event.
      - scope: Host summary/recovery and aggregate mixed-evidence original inputs
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-summaries
        - memory.md#mem-rte-aggregate-recall
        note: Host summary labels and selected evidence arrays do not identify every original qualifying
          input. Event-streams or trajectories cannot be inferred from serialization or sequence alone.
      - scope: Provider/native-source, hierarchy, identity/coordination and optimization alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-artifacts
        - memory.md#mem-obj-session-summaries
        - memory.md#mem-obj-identity-files
        - memory.md#mem-obj-run-checkpoint
        note: Original inputs of possible qualifying writes remain uninspected; unresolved learning cannot
          make trace source inapplicable.
      records:
      - memory.md#mem-obj-session-transcripts
      - memory.md#mem-rte-transcript-capture
      - runtime.md#rt-rte-dreaming-pass
      - memory.md#mem-obj-memory-head
      - memory.md#mem-obj-dreaming-history
      - memory.md#mem-rte-history-compaction
      - memory.md#mem-obj-path-feedback
      - memory.md#mem-rte-path-feedback
      - memory.md#mem-obj-session-summaries
      - memory.md#mem-rte-aggregate-recall
      - memory.md#mem-obj-memory-artifacts
      - memory.md#mem-obj-identity-files
      - memory.md#mem-obj-run-checkpoint
      note: Session logs and tool traces have local qualifying-write witnesses. Mixed/opaque inputs remain
        unresolved; no event-stream or multi-step trajectory positive follows merely from callback dispatch
        or pass chronology.
---

# Signet memory profile

## Comparison rationale

This profile classifies accepted records only. Every axis is partial because the memory account retains material included alternatives whose objects, admissions, selectors or consumers remain unresolved. Strong local wiring does not resolve those alternatives. No source files were read for this profile; no records or new evidence were added.

Reconciliation asserts no supersessions. Containers and parts remain canonical at their own scopes. The head object, support check and workflow finalization remain distinct: [MEM-OBJ-memory-head](memory.md#mem-obj-memory-head), [EPI-RTE-head-support](epistemic.md#epi-rte-head-support), and [WF-RTE-head-finalization](workflow.md#wf-rte-head-finalization). The corrected head account retains unchanged-current-body and already-empty-head NOOP branches before submitted support validation. Enforcing validation applies at its actual checks, not to every successful finalization. Database revision, file publication and conditional startup supply are separate outcomes.

Graph and SQLite findings describe access organization and physical backing of the same retained graph parts. Dense embeddings are parametric representations, not proof of provider-weight learning. Localized feedback weights are symbolic because their consumers use fixed update and ordering rules. Transient in-memory prompts and staged submissions are not independently accumulated objects. See [MEM-OBJ-entity-attributes](memory.md#mem-obj-entity-attributes), [MEM-CMP-embedding-provider](memory.md#mem-cmp-embedding-provider), and [MEM-OBJ-path-feedback](memory.md#mem-obj-path-feedback).

Admission is not authorship. Software/model gates establish automatic writes for named transformations; an arbitrary caller or an authored filename does not establish a human per-content decision. Initial identity approval, rating authorship and other import/recovery controls remain unresolved. See [RT-RTE-direct-remember](runtime.md#rt-rte-direct-remember), [MEM-OBJ-identity-files](memory.md#mem-obj-identity-files), and [MEM-RTE-path-feedback](memory.md#mem-rte-path-feedback).

History leaf extraction and parent compression support consolidation without requiring semantic fidelity or hard byte ceilings. Aggregate duplicate handling and refresh support deduplication and evolution. Forgetting and tombstone/staleness transitions support forgetting and invalidation at current-reliance consumers, not privacy erasure. The route called synthesis does not establish a new claim absent from its inputs: the accepted epistemic account leaves that relation indeterminate. Requested head condensation is kept at claimed basis, separate from wired history reduction. See [MEM-RTE-history-compaction](memory.md#mem-rte-history-compaction), [MEM-RTE-state-withdrawal](memory.md#mem-rte-state-withdrawal), [EPI-RTE-aggregate-synthesis](epistemic.md#epi-rte-aggregate-synthesis), and [WF-RTE-head-finalization](workflow.md#wf-rte-head-finalization).

Explicit recall and zoom are pull. Automatically supplied startup background and initial maintenance history are push, even when a lifecycle request precedes them. Scope matching actually selects history streams; filenames on requested reads do not establish identifier push. Recall's lexical/vector capabilities do not by themselves prove the startup selector's signal. Inherited, recovery and predicted-context selectors and other host adapters remain unresolved. See [MEM-RTE-explicit-recall](memory.md#mem-rte-explicit-recall), [RT-RTE-pi-lifecycle](runtime.md#rt-rte-pi-lifecycle), and [MEM-RTE-history-compaction](memory.md#mem-rte-history-compaction).

Trace learning is established by automatic session-fed semantic/head writes, pass/tool-fed history summaries and retrieval-feedback-fed selector weights with later consumers. Their update inputs have learning authority; outputs independently have knowledge or ranking authority. Host compaction supplies another automatically retained continuation-summary route, without resolving its complete original inputs. This does not establish exercised improvement. Host summary origins and aggregate mixed-evidence origins remain locally unresolved. Tool activity is not automatically a multi-step trajectory, and conversational material wrapped in capture events remains session logs. See [MEM-RTE-transcript-capture](memory.md#mem-rte-transcript-capture), [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass), [MEM-RTE-history-compaction](memory.md#mem-rte-history-compaction), [MEM-RTE-path-feedback](memory.md#mem-rte-path-feedback), and [MEM-OBJ-session-summaries](memory.md#mem-obj-session-summaries).

Benchmark checkpoint status routes subsequent evaluation, but retained scores are not established product-memory acceptance or optimization inputs. Unknown serialization and unread optimization consumers prevent stronger substrate, lineage and trace conclusions. See [MEM-OBJ-run-checkpoint](memory.md#mem-obj-run-checkpoint) and [EPI-RTE-benchmark-checkpoint](epistemic.md#epi-rte-benchmark-checkpoint). No bounded absence records support a system-wide negative on any axis.
