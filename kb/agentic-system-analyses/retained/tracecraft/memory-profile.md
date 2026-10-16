---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: Tracecraft memory comparison of bucket-backed coordination content, mirrored transcripts
  and their access state, with unresolved downstream consumers.
run-id: AAS-2026-10-14-tracecraft-9c4af961e8e2-01
source-identity: https://github.com/arrmlet/tracecraft
reviewed-boundary: 97c6b7447f8e696f0116357d9f86bb0ece25e5b1
memory-comparison:
  version: 2
  scope: Includes accumulated project-bucket values/history, mail/cursor, claim/status, handoff, artifacts,
    mirrored transcript parts/meta, registration, local mirror checkpoint and optional durable evaluator
    trial JSONL. Includes opaque caller/file/host-checkpoint alternatives and unresolved handoff/evaluator
    later consumption. Excludes static shipped instructions/package source, credentials/configuration,
    external host storage/model loops and provider internals, and ephemeral evaluator fixtures/current-trial
    reads.
  axes:
    storage_substrate:
      assessment: known
      units:
      - scope: Project-bucket values/history, mail/cursor, claim/status, handoff, artifacts, transcript
          parts/meta and registration
        assessment: known
        findings:
        - value: service-object
          basis: wired
          records: &id001
          - memory.md#mem-obj-memory-live
          - memory.md#mem-obj-memory-history
          - memory.md#mem-obj-message-content
          - memory.md#mem-obj-inbox-cursor
          - memory.md#mem-obj-handoff
          - memory.md#mem-obj-artifact-file
          - memory.md#mem-obj-session-parts
          - memory.md#mem-obj-session-meta
          - memory.md#mem-obj-agent-registration
          - runtime.md#rt-obj-step-state
          note: S3-compatible or HuggingFace bucket objects hold these retained parts. JSON and JSONL
            describe encodings, not additional database substrates.
        records: *id001
        note: All named operative parts are remote bucket objects on either supported backend.
      - scope: Local mirror cursor checkpoint
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-mirror-state
          note: Mirror saves its cross-invocation cursor under ~/.tracecraft/mirror-state.
        records:
        - memory.md#mem-obj-mirror-state
        note: The next mirror reads a local JSON file; host SQLite is an acquisition source, not Tracecraft
          retained storage.
      - scope: Optional durable contention evaluator trial JSONL
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-rte-evaluator-readback
          note: Requested local JSONL stores trial fields. Temporary evaluator bucket fixtures are excluded
            from durable inventory.
        records:
        - memory.md#mem-rte-evaluator-readback
        note: The supplied record establishes file emission, independently of the uninspected later report
          reader.
      records:
      - memory.md#mem-obj-memory-live
      - memory.md#mem-obj-memory-history
      - memory.md#mem-obj-message-content
      - memory.md#mem-obj-inbox-cursor
      - memory.md#mem-obj-handoff
      - memory.md#mem-obj-artifact-file
      - memory.md#mem-obj-session-parts
      - memory.md#mem-obj-session-meta
      - memory.md#mem-obj-agent-registration
      - runtime.md#rt-obj-step-state
      - memory.md#mem-obj-mirror-state
      - memory.md#mem-rte-evaluator-readback
      note: The recorded retained-object inventory covers project bucket objects, the local ingestion
        checkpoint and optional durable evaluator output. Opaque file content does not make its bucket
        substrate opaque; provider implementation is excluded.
    representational_form:
      assessment: partial
      units:
      - scope: Bucket envelopes, addresses, claim/status, cursors, metadata, registration and handoff
          path/state fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-memory-live
          - memory.md#mem-obj-memory-history
          - memory.md#mem-obj-message-content
          - memory.md#mem-obj-inbox-cursor
          - runtime.md#rt-obj-step-state
          - memory.md#mem-obj-handoff
          - memory.md#mem-obj-session-meta
          - memory.md#mem-obj-mirror-state
          - memory.md#mem-obj-agent-registration
          note: Keys, timestamps, state flags, cursor watermarks and path lists are symbolic.
        records:
        - memory.md#mem-obj-memory-live
        - memory.md#mem-obj-memory-history
        - memory.md#mem-obj-message-content
        - memory.md#mem-obj-inbox-cursor
        - runtime.md#rt-obj-step-state
        - memory.md#mem-obj-handoff
        - memory.md#mem-obj-session-meta
        - memory.md#mem-obj-mirror-state
        - memory.md#mem-obj-agent-registration
        note: These localized fields have fixed software parsing or display rules, separate from their
          textual payloads.
      - scope: Message text supplied to inbox readers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-message-content
          - runtime.md#rt-rte-mail-exchange
          note: Inbox displays communication text to a human or externally hosted agent; actual uptake
            is unobserved.
        records:
        - memory.md#mem-obj-message-content
        - runtime.md#rt-rte-mail-exchange
        note: The communication path delivers caller text for interpretation; envelope fields are classified
          separately.
      - scope: Optional handoff note and next-action prose
        assessment: partial
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-handoff
          - runtime.md#rt-rte-step-control
          note: Caller note and next-action text carry context or directions; no shipped content-reader
            is established.
        records:
        - memory.md#mem-obj-handoff
        - runtime.md#rt-rte-step-control
        note: The recorded prose is distinguishable from symbolic fields, but its later delivery/consumer
          is unresolved.
      - scope: Current/shared historical caller value payload
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-live
        - memory.md#mem-obj-memory-history
        note: 'findings empty: arbitrary strings may be natural language, symbolic serialization or other
          content. No concrete value or semantic consumer is supplied.'
      - scope: Downloaded artifact payload
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-artifact-file
        - runtime.md#rt-rte-artifact-share
        note: Arbitrary uploaded bytes and external parsing are unresolved; filename and step addressing
          classify only the access structure.
      - scope: Mirrored host transcript payload and decoded tail
        assessment: partial
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-session-parts
          note: Recorded host utterances include natural-language turns delivered by tail display.
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-session-parts
          note: Host event/tool/row metadata and Hermes serialized columns are symbolic; this does not
            classify every nested payload.
        records:
        - memory.md#mem-obj-session-parts
        - runtime.md#rt-rte-session-mirror
        note: Mixed textual and symbolic records are supported, but multimodal/opaque fields and already-derived
          checkpoints remain unresolved.
      - scope: Durable evaluator trial fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-rte-evaluator-readback
          note: Structured trial rows record evaluator measurements and comparison results.
        records:
        - memory.md#mem-rte-evaluator-readback
        note: Result/error/invariant/exclusion fields are fixed-code trial data; later report interpretation
          remains uninspected.
      records:
      - memory.md#mem-obj-memory-live
      - memory.md#mem-obj-memory-history
      - memory.md#mem-obj-message-content
      - memory.md#mem-obj-inbox-cursor
      - runtime.md#rt-obj-step-state
      - memory.md#mem-obj-handoff
      - memory.md#mem-obj-session-meta
      - memory.md#mem-obj-mirror-state
      - memory.md#mem-obj-agent-registration
      - runtime.md#rt-rte-mail-exchange
      - runtime.md#rt-rte-step-control
      - memory.md#mem-obj-artifact-file
      - runtime.md#rt-rte-artifact-share
      - memory.md#mem-obj-session-parts
      - runtime.md#rt-rte-session-mirror
      - memory.md#mem-rte-evaluator-readback
      note: Symbolic access/control parts and interpreted message/handoff text are classified separately.
        Caller values, uploaded files and opaque host fields prevent complete form coverage.
    lineage:
      assessment: partial
      units:
      - scope: Caller content entering current values, messages and artifact objects
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-memory-live
          - memory.md#mem-obj-message-content
          - memory.md#mem-obj-artifact-file
          - runtime.md#rt-rte-memory-write
          - runtime.md#rt-rte-mail-exchange
          - runtime.md#rt-rte-artifact-share
          note: Caller text or local file bytes enter the bucket through the CLI; imported does not mean
            source warrant is verified.
        records:
        - memory.md#mem-obj-memory-live
        - memory.md#mem-obj-message-content
        - memory.md#mem-obj-artifact-file
        - runtime.md#rt-rte-memory-write
        - runtime.md#rt-rte-mail-exchange
        - runtime.md#rt-rte-artifact-share
        note: Ingress is established; original human/model/tool authorship and earlier derivation are
          not.
      - scope: Memory history snapshot copy
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-memory-history
          - runtime.md#rt-rte-memory-write
          note: CLI wraps the submitted value with key and provenance and writes a separate version snapshot.
        records:
        - memory.md#mem-obj-memory-history
        - runtime.md#rt-rte-memory-write
        note: The snapshot is a code-produced version copy; initial provenance of its value is unresolved.
      - scope: Caller handoff text and symbolic completion fields
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-handoff
          - runtime.md#rt-rte-step-control
          note: Completion acquires caller notes, next action and selected outcome.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-handoff
          - runtime.md#rt-rte-step-control
          note: Fixed code assembles the schema, attribution, state and timestamp envelope.
        records:
        - memory.md#mem-obj-handoff
        - runtime.md#rt-rte-step-control
        note: Caller text/state enter through completion; optional Git acquisition is classified separately.
          Original prose authorship remains unresolved.
      - scope: Optional changed-files handoff field
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-handoff
          - epistemic.md#epi-rte-git-files
          note: Code parses Git name output into a symbolic list rather than extracting a lesson from
            a tool session.
        records:
        - memory.md#mem-obj-handoff
        - epistemic.md#epi-rte-git-files
        note: The field derives from the fixed Git diff path measurement; empty conflates failure and
          no diff.
      - scope: Mirrored host parts, including checkpoint/topic alternatives
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-session-parts
          - runtime.md#rt-rte-session-mirror
          note: Host file tails or database rows enter Tracecraft.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-session-parts
          - runtime.md#rt-rte-session-mirror
          - runtime.md#rt-rte-session-compact
          note: Hermes row serialization, optional regex replacement and later byte concatenation produce
            retained forms, not new lessons.
        records:
        - memory.md#mem-obj-session-parts
        - runtime.md#rt-rte-session-mirror
        - runtime.md#rt-rte-session-compact
        note: Tracecraft ingress/redaction/concatenation is established; original host production, pruning
          and checkpoint derivation are unresolved.
      - scope: Inbox cursor, session metadata and local mirror checkpoint
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-inbox-cursor
          - memory.md#mem-obj-session-meta
          - memory.md#mem-obj-mirror-state
          - runtime.md#rt-rte-mail-exchange
          - runtime.md#rt-rte-session-mirror
          note: Watermarks/seen keys, flush metadata and cursor checkpoints are code-assembled access
            structures.
        records:
        - memory.md#mem-obj-inbox-cursor
        - memory.md#mem-obj-session-meta
        - memory.md#mem-obj-mirror-state
        - runtime.md#rt-rte-mail-exchange
        - runtime.md#rt-rte-session-mirror
        note: Fixed code derives access state from listed keys, source descriptors, flush positions and
          prior state.
      - scope: Claim/status and agent registration
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - runtime.md#rt-obj-step-state
          - memory.md#mem-obj-agent-registration
          - runtime.md#rt-rte-step-control
          - runtime.md#rt-rte-init-config
          note: CLI constructs durable coordination and registration documents.
        records:
        - runtime.md#rt-obj-step-state
        - memory.md#mem-obj-agent-registration
        - runtime.md#rt-rte-step-control
        - runtime.md#rt-rte-init-config
        note: Caller-selected state/identity is wrapped by fixed code, not evidence of model authorship.
      - scope: Durable evaluator result rows
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-rte-evaluator-readback
          - epistemic.md#epi-rte-bucket-evaluation
          note: Evaluator records API outcomes and durable read-back measurements as trial fields.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-rte-evaluator-readback
          - epistemic.md#epi-rte-bucket-evaluation
          note: Fixed comparisons and serialization produce invariant/error/exclusion fields.
        records:
        - memory.md#mem-rte-evaluator-readback
        - epistemic.md#epi-rte-bucket-evaluation
        note: The sampled emitter and comparisons establish the derivation of optional trial fields, not
          observed trials.
      records:
      - memory.md#mem-obj-memory-live
      - memory.md#mem-obj-message-content
      - memory.md#mem-obj-artifact-file
      - runtime.md#rt-rte-memory-write
      - runtime.md#rt-rte-mail-exchange
      - runtime.md#rt-rte-artifact-share
      - memory.md#mem-obj-memory-history
      - memory.md#mem-obj-handoff
      - runtime.md#rt-rte-step-control
      - epistemic.md#epi-rte-git-files
      - memory.md#mem-obj-session-parts
      - runtime.md#rt-rte-session-mirror
      - runtime.md#rt-rte-session-compact
      - memory.md#mem-obj-inbox-cursor
      - memory.md#mem-obj-session-meta
      - memory.md#mem-obj-mirror-state
      - runtime.md#rt-obj-step-state
      - memory.md#mem-obj-agent-registration
      - runtime.md#rt-rte-init-config
      - memory.md#mem-rte-evaluator-readback
      - epistemic.md#epi-rte-bucket-evaluation
      note: Ingress, copying and code-derived metadata are classified without inventing original authorship
        or host checkpoint derivation. Imported content and compiled access structures coexist.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Returned shared values/history and inbox text at external human/agent readers
        assessment: partial
        findings:
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-obj-memory-live
          - memory.md#mem-obj-memory-history
          - memory.md#mem-obj-message-content
          - runtime.md#rt-rte-memory-write
          - runtime.md#rt-rte-mail-exchange
          - runtime.md#rt-bap-agent-prompt
          note: Requested CLI outputs can supply progress/context/reference to the instructed external
            agent.
        records:
        - memory.md#mem-obj-memory-live
        - memory.md#mem-obj-memory-history
        - memory.md#mem-obj-message-content
        - runtime.md#rt-rte-memory-write
        - runtime.md#rt-rte-mail-exchange
        - runtime.md#rt-bap-agent-prompt
        note: Shipped instructions afford later reference/context use, but unrestricted value/message
          content and actual uptake prevent complete downstream authority classification.
      - scope: Claim owner at completion admission
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - runtime.md#rt-obj-step-state
          - runtime.md#rt-rte-step-control
          note: Complete compares the retained claim owner against caller attribution.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-obj-step-state
          - runtime.md#rt-rte-step-control
          note: Mismatch refuses ordinary completion unless --force; this is cooperative CLI control,
            not authentication.
        records:
        - runtime.md#rt-obj-step-state
        - runtime.md#rt-rte-step-control
        note: The same retained owner criterion both checks admissibility and vetoes a mismatch, with
          the recorded force bypass.
      - scope: Claim/status at dependency waiter
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-obj-step-state
          - runtime.md#rt-bap-step-polling
          note: Status selects return, polling or blocked error.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-obj-step-state
          - runtime.md#rt-bap-step-polling
          note: Only complete permits successful wait; blocked prevents it and review-needed continues
            waiting.
        records:
        - runtime.md#rt-obj-step-state
        - runtime.md#rt-bap-step-polling
        - runtime.md#rt-rte-step-control
        note: Fixed state comparisons control return, wait or error, not task truth.
      - scope: Inbox cursor at new-mail selection and unread counting
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-inbox-cursor
          - runtime.md#rt-rte-mail-exchange
          note: Watermark and seen keys select new retained mail and computed unread counts.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-inbox-cursor
          - runtime.md#rt-rte-mail-exchange
          note: Seen-key/cursor rules suppress delivery of excluded items on the incremental route.
        records:
        - memory.md#mem-obj-inbox-cursor
        - runtime.md#rt-rte-mail-exchange
        note: Full inbox is the separate cursor-ignoring route.
      - scope: Local mirror cursor at subsequent ingestion
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-mirror-state
          - runtime.md#rt-rte-session-mirror
          note: The persisted cursor selects which later bytes/rows mirror consumes.
        records:
        - memory.md#mem-obj-mirror-state
        - runtime.md#rt-rte-session-mirror
        note: Recorded cursor alone determines the next source window; source identity is not revalidated.
      - scope: Session metadata and registration as inspection information at CLI views
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-session-meta
          - memory.md#mem-obj-agent-registration
          - runtime.md#rt-rte-session-mirror
          - runtime.md#rt-rte-init-config
          note: Metadata and registration furnish inspection/reference information to requested list/show/status
            views.
        records:
        - memory.md#mem-obj-session-meta
        - memory.md#mem-obj-agent-registration
        - runtime.md#rt-rte-session-mirror
        - runtime.md#rt-rte-init-config
        note: Display consumers supply descriptions, totals and age, not authenticated liveness. Session-list
          ordering and limit selection are classified separately below.
      - scope: Retained session metadata at session-list ordering and limit selection
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-session-meta
          - runtime.md#rt-rte-session-mirror
          note: Session list sorts retained metadata by recency or size before applying its default
            limit of 20; metadata therefore influences relative priority and which entries are returned.
        records:
        - memory.md#mem-obj-session-meta
        - runtime.md#rt-rte-session-mirror
        note: The recorded fixed-code sorting consumer establishes ranking independently of metadata
          display. This unit does not include registration display or claim observed agent uptake.
      - scope: Handoff notes, next action, recipient and optional Git paths
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-handoff
        - runtime.md#rt-rte-step-control
        - epistemic.md#epi-rte-git-files
        note: Content-reader wiring is unresolved. Stored directive/recipient text alone establishes neither
          instruction nor routing authority at a later consumer.
      - scope: Opaque artifact bytes at the downstream parser/agent
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-artifact-file
        - runtime.md#rt-rte-artifact-share
        note: Download is wired and an agent consumer is afforded, but file content and its operative
          effect are not established.
      - scope: Transcript tail at inspection reader
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-session-parts
          - runtime.md#rt-rte-session-mirror
          note: Decoded tail supplies retained activity records for inspection; no semantic endorsement
            is added.
        records:
        - memory.md#mem-obj-session-parts
        - runtime.md#rt-rte-session-mirror
        note: The established consumer is requested inspection, not host restoration or automatic guidance.
      - scope: Durable evaluator output at report/adoption consumer
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-evaluator-readback
        note: The later report reader was not inspected, preventing classification of force carried by
          durable trial rows. Immediate trial checks do not establish later authority.
      records:
      - memory.md#mem-obj-memory-live
      - memory.md#mem-obj-memory-history
      - memory.md#mem-obj-message-content
      - runtime.md#rt-rte-memory-write
      - runtime.md#rt-rte-mail-exchange
      - runtime.md#rt-bap-agent-prompt
      - runtime.md#rt-obj-step-state
      - runtime.md#rt-rte-step-control
      - runtime.md#rt-bap-step-polling
      - memory.md#mem-obj-inbox-cursor
      - memory.md#mem-obj-mirror-state
      - runtime.md#rt-rte-session-mirror
      - memory.md#mem-obj-session-meta
      - memory.md#mem-obj-agent-registration
      - runtime.md#rt-rte-init-config
      - memory.md#mem-obj-handoff
      - epistemic.md#epi-rte-git-files
      - memory.md#mem-obj-artifact-file
      - runtime.md#rt-rte-artifact-share
      - memory.md#mem-obj-session-parts
      - memory.md#mem-rte-evaluator-readback
      note: Fixed coordination effects, inspection displays and session-metadata ranking are wired;
        external-agent reference use is afforded. Opaque files,
        handoff delivery and later evaluator report consumption remain unresolved. Static shipped instructions
        are excluded.
    write_agency:
      assessment: partial
      units:
      - scope: Caller submission/replacement of values, messages, claim/completion/handoff, files and
          registration
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-memory-write
        - runtime.md#rt-rte-mail-exchange
        - runtime.md#rt-rte-step-control
        - runtime.md#rt-rte-artifact-share
        - runtime.md#rt-rte-init-config
        - memory.md#mem-obj-handoff
        note: Human versus model/software content decision is unresolved. Software physical I/O and command
          initiation alone do not establish automatic or manual admission of the submitted content.
      - scope: Per-flush transcript and access-state admission after mirror initiation
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-session-mirror
          - memory.md#mem-obj-session-parts
          - memory.md#mem-obj-session-meta
          - memory.md#mem-obj-mirror-state
          note: Caller initiation is upstream of automatic byte/row admission and derived state writes.
        records:
        - runtime.md#rt-rte-session-mirror
        - memory.md#mem-obj-session-parts
        - memory.md#mem-obj-session-meta
        - memory.md#mem-obj-mirror-state
        note: Mirror software selects deltas, optionally redacts and writes without per-item human approval.
      - scope: Inbox cursor advancement after requested display
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-inbox-cursor
          - runtime.md#rt-rte-mail-exchange
          note: Listed keys determine persisted watermark/seen state after display.
        records:
        - memory.md#mem-obj-inbox-cursor
        - runtime.md#rt-rte-mail-exchange
        note: The software derives and commits reader position, without a separate operator decision on
          retained cursor content.
      - scope: Optional Git-derived handoff path list
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - epistemic.md#epi-rte-git-files
          - memory.md#mem-obj-handoff
          note: Git output or empty fallback is inserted automatically.
        records:
        - epistemic.md#epi-rte-git-files
        - memory.md#mem-obj-handoff
        note: Enabling the flag does not approve each returned path; fixed code admits the measurement.
      - scope: Compact-produced merged payload and replacement manifest
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-session-compact
          - memory.md#mem-obj-session-meta
          note: Code admits merged bytes and compiled manifest, then deletes originals.
        records:
        - runtime.md#rt-rte-session-compact
        - memory.md#mem-obj-session-meta
        note: Requested maintenance triggers fixed concatenation and metadata replacement without per-result
          content approval.
      - scope: Optional durable evaluator trial rows
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-evaluator-readback
          note: Fixed evaluator logic emits trial data to requested JSONL.
        records:
        - memory.md#mem-rte-evaluator-readback
        note: Developer initiation selects conditions; software admits computed row fields.
      records:
      - runtime.md#rt-rte-memory-write
      - runtime.md#rt-rte-mail-exchange
      - runtime.md#rt-rte-step-control
      - runtime.md#rt-rte-artifact-share
      - runtime.md#rt-rte-init-config
      - memory.md#mem-obj-handoff
      - runtime.md#rt-rte-session-mirror
      - memory.md#mem-obj-session-parts
      - memory.md#mem-obj-session-meta
      - memory.md#mem-obj-mirror-state
      - memory.md#mem-obj-inbox-cursor
      - epistemic.md#epi-rte-git-files
      - runtime.md#rt-rte-session-compact
      - memory.md#mem-rte-evaluator-readback
      note: Automatic trace ingestion and software-derived access/result writes are established. Generic
        CLI caller identity cannot resolve per-content human control for caller submissions or replacements.
    curation_operations:
      assessment: partial
      units:
      - scope: Live-value, status/handoff and same-key artifact replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-rte-memory-write
          - runtime.md#rt-rte-step-control
          - runtime.md#rt-rte-artifact-share
          - memory.md#mem-obj-memory-live
          - memory.md#mem-obj-handoff
          - memory.md#mem-obj-artifact-file
          note: Later set/complete/upload revises the same live key, document or artifact.
        records:
        - runtime.md#rt-rte-memory-write
        - runtime.md#rt-rte-step-control
        - runtime.md#rt-rte-artifact-share
        - memory.md#mem-obj-memory-live
        - memory.md#mem-obj-handoff
        - memory.md#mem-obj-artifact-file
        note: These routes replace existing retained entries; underlying content authorship remains unresolved
          independently.
      - scope: Incremental access-state and manifest revision
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-inbox-cursor
          - memory.md#mem-obj-mirror-state
          - memory.md#mem-obj-session-meta
          - runtime.md#rt-rte-mail-exchange
          - runtime.md#rt-rte-session-mirror
          - runtime.md#rt-rte-session-compact
          note: Cursor advancement and cumulative/replacement manifest writes revise retained state.
        records:
        - memory.md#mem-obj-inbox-cursor
        - memory.md#mem-obj-mirror-state
        - memory.md#mem-obj-session-meta
        - runtime.md#rt-rte-mail-exchange
        - runtime.md#rt-rte-session-mirror
        - runtime.md#rt-rte-session-compact
        note: Software revises existing access structures, separate from payload meaning.
      - scope: Requested inbox deletion of displayed direct mail
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-obj-message-content
          - runtime.md#rt-rte-mail-exchange
          note: --delete forgets retained direct messages by removing their objects.
        records:
        - memory.md#mem-obj-message-content
        - runtime.md#rt-rte-mail-exchange
        note: Only direct displayed records are removed; broadcasts remain.
      - scope: Transcript compact payload and redaction/import alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-parts
        - runtime.md#rt-rte-session-compact
        - runtime.md#rt-rte-session-mirror
        - epistemic.md#epi-rte-regex-scrub
        note: Byte concatenation reduces object count but not content claims; ingress redaction is not
          established maintenance over prior retained content. These records do not establish a controlled
          semantic curation operation on payloads.
      - scope: History copies, initial registration and evaluator acquisition/emission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-history
        - memory.md#mem-obj-agent-registration
        - memory.md#mem-rte-evaluator-readback
        note: Copying/acquisition and emitting result rows alone establish no listed curation transformation
          over retained content.
      - scope: Direct API maintenance and already-derived host checkpoints
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-clm-history-immutability
        - memory.md#mem-obj-session-parts
        note: Generic put/delete capacity and opaque host checkpoint derivation do not identify a particular
          maintained-content transformation.
      records:
      - runtime.md#rt-rte-memory-write
      - runtime.md#rt-rte-step-control
      - runtime.md#rt-rte-artifact-share
      - memory.md#mem-obj-memory-live
      - memory.md#mem-obj-handoff
      - memory.md#mem-obj-artifact-file
      - memory.md#mem-obj-inbox-cursor
      - memory.md#mem-obj-mirror-state
      - memory.md#mem-obj-session-meta
      - runtime.md#rt-rte-mail-exchange
      - runtime.md#rt-rte-session-mirror
      - runtime.md#rt-rte-session-compact
      - memory.md#mem-obj-message-content
      - memory.md#mem-obj-session-parts
      - epistemic.md#epi-rte-regex-scrub
      - memory.md#mem-obj-memory-history
      - memory.md#mem-obj-agent-registration
      - memory.md#mem-rte-evaluator-readback
      - memory.md#mem-clm-history-immutability
      note: Recorded overwrites revise retained entries, and mailbox deletion forgets direct messages.
        Other transforms do not establish semantic consolidation, synthesis or deduplication; direct API
        and opaque host maintenance remain unresolved.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested get/history/inbox/status/wait/download/session-list/show/agents reads
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-memory-write
          - runtime.md#rt-rte-mail-exchange
          - runtime.md#rt-rte-step-control
          - runtime.md#rt-rte-artifact-share
          - runtime.md#rt-rte-session-mirror
          - memory.md#mem-obj-agent-registration
          - memory.md#mem-obj-session-meta
          note: Each delivered retained result fulfills an explicit consumer command.
        records:
        - runtime.md#rt-rte-memory-write
        - runtime.md#rt-rte-mail-exchange
        - runtime.md#rt-rte-step-control
        - runtime.md#rt-rte-artifact-share
        - runtime.md#rt-rte-session-mirror
        - memory.md#mem-obj-agent-registration
        - memory.md#mem-obj-session-meta
        note: Automatic filtering inside the request is not independent push.
      - scope: Mirror internal request for persisted cursor and prior metadata
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-obj-mirror-state
          - memory.md#mem-obj-session-meta
          - runtime.md#rt-rte-session-mirror
          note: Mirror loads the local checkpoint and remote metadata to determine the next flush.
        records:
        - memory.md#mem-obj-mirror-state
        - memory.md#mem-obj-session-meta
        - runtime.md#rt-rte-session-mirror
        note: Subsequent mirror explicitly loads access state as its requested input, rather than unsolicited
          context delivery.
      - scope: Handoff next-agent read-back
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-handoff
        - runtime.md#rt-rte-step-control
        note: A storage GET capability and producer promise do not establish a later consumer route or
          its direction.
      - scope: Durable evaluator trial JSONL later report read-back
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-evaluator-readback
        note: Emitter is established; downstream report-generation internals were not inspected. Same-trial
          fixture reads are not later consumption of durable output.
      records:
      - runtime.md#rt-rte-memory-write
      - runtime.md#rt-rte-mail-exchange
      - runtime.md#rt-rte-step-control
      - runtime.md#rt-rte-artifact-share
      - runtime.md#rt-rte-session-mirror
      - memory.md#mem-obj-agent-registration
      - memory.md#mem-obj-session-meta
      - memory.md#mem-obj-mirror-state
      - memory.md#mem-obj-handoff
      - memory.md#mem-rte-evaluator-readback
      note: Established content/inspection routes fulfill caller requests. Local mirror code also reloads
        persisted access state during subsequent flushes. Handoff delivery and durable evaluator report
        reads are unresolved; they cannot be excluded to claim a complete pull-only boundary.
    read_back_signal:
      assessment: not-determinable
      units:
      - scope: Established requested dynamic reads, including mirror access-state loads
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-memory-write
        - runtime.md#rt-rte-mail-exchange
        - runtime.md#rt-rte-step-control
        - runtime.md#rt-rte-artifact-share
        - runtime.md#rt-rte-session-mirror
        - memory.md#mem-obj-mirror-state
        - memory.md#mem-obj-session-meta
        - memory.md#mem-obj-agent-registration
        note: These are pull operations. Explicit identifiers, cursor filtering, sort and tail budgets
          on requests do not establish push signals.
      - scope: Handoff delivery selector
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-handoff
        - runtime.md#rt-rte-step-control
        note: next_agent is stored attribution, not an evidenced identity match selecting delivered content;
          trigger and consumer are missing.
      - scope: Durable evaluator-output delivery selector
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-evaluator-readback
        note: Later report consumer/selection is uninspected, so push signal cannot be classified.
      records:
      - runtime.md#rt-rte-memory-write
      - runtime.md#rt-rte-mail-exchange
      - runtime.md#rt-rte-step-control
      - runtime.md#rt-rte-artifact-share
      - runtime.md#rt-rte-session-mirror
      - memory.md#mem-obj-mirror-state
      - memory.md#mem-obj-session-meta
      - memory.md#mem-obj-agent-registration
      - memory.md#mem-obj-handoff
      - memory.md#mem-rte-evaluator-readback
      note: No positive push-selector value is established. Assessed requested routes are locally inapplicable,
        but unresolved handoff/evaluator routes prevent system-wide inapplicability.
    trace_learning:
      assessment: not-determinable
      units:
      - scope: Tracecraft mirror, scrub and compact to requested transcript inspection
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-parts
        - runtime.md#rt-rte-session-mirror
        - runtime.md#rt-rte-session-compact
        - epistemic.md#epi-rte-regex-scrub
        note: Automatic writes are wired, but these records describe trace preservation/layout rather
          than a derived continuation/behavior-shaping artifact with a later guidance consumer. Raw-log
          storage alone is insufficient.
      - scope: Caller coordination content and uploaded artifacts
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-live
        - memory.md#mem-obj-memory-history
        - memory.md#mem-obj-message-content
        - memory.md#mem-obj-handoff
        - memory.md#mem-obj-artifact-file
        - runtime.md#rt-rte-memory-write
        - runtime.md#rt-rte-mail-exchange
        - runtime.md#rt-rte-step-control
        - runtime.md#rt-rte-artifact-share
        note: Unknown caller decision/provenance and opaque file payload prevent determining whether any
          submitted part is a qualifying automatic trace-derived artifact.
      - scope: Already-derived external-host checkpoint input
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-parts
        - runtime.md#rt-rte-session-mirror
        note: Checkpoint filename establishes ingestion only; original automatic derivation and later
          host guidance consumption are unresolved.
      - scope: Access checkpoints, metadata, registration and claim/status
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-inbox-cursor
        - memory.md#mem-obj-mirror-state
        - memory.md#mem-obj-session-meta
        - memory.md#mem-obj-agent-registration
        - runtime.md#rt-obj-step-state
        note: Fixed bookkeeping/routing is established, but no record establishes the qualifying trace-to-behavior-shaping-artifact
          learning chain. This is not evidence of improved capacity.
      - scope: Durable evaluator results and later report/adoption
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-evaluator-readback
        - epistemic.md#epi-rte-bucket-evaluation
        note: Automatic trial recording is established; later report/adoption is uninspected and no recorded
          automatic policy update closes the chain.
      records:
      - memory.md#mem-obj-session-parts
      - runtime.md#rt-rte-session-mirror
      - runtime.md#rt-rte-session-compact
      - epistemic.md#epi-rte-regex-scrub
      - memory.md#mem-obj-memory-live
      - memory.md#mem-obj-memory-history
      - memory.md#mem-obj-message-content
      - memory.md#mem-obj-handoff
      - memory.md#mem-obj-artifact-file
      - runtime.md#rt-rte-memory-write
      - runtime.md#rt-rte-mail-exchange
      - runtime.md#rt-rte-step-control
      - runtime.md#rt-rte-artifact-share
      - memory.md#mem-obj-inbox-cursor
      - memory.md#mem-obj-mirror-state
      - memory.md#mem-obj-session-meta
      - memory.md#mem-obj-agent-registration
      - runtime.md#rt-obj-step-state
      - memory.md#mem-rte-evaluator-readback
      - epistemic.md#epi-rte-bucket-evaluation
      note: The accepted records establish raw/transformed trace retention and unresolved caller/host/evaluator
        routes, not a qualifying automatic trace-fed behavior-shaping update. They declare no bounded
        absence records, so a system-wide no is not authored.
    trace_source:
      assessment: not-determinable
      units:
      - scope: Mirror/compact and already-derived host checkpoint alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-parts
        - runtime.md#rt-rte-session-mirror
        - runtime.md#rt-rte-session-compact
        note: Host session/tool/opaque fields are possible inputs, but no qualifying Tracecraft learning
          route is established and checkpoint original derivation is unresolved.
      - scope: Caller values, mail, handoff and artifact alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-live
        - memory.md#mem-obj-memory-history
        - memory.md#mem-obj-message-content
        - memory.md#mem-obj-handoff
        - memory.md#mem-obj-artifact-file
        note: Original inputs to any qualifying caller-side trace-fed write are unknown; addressing and
          caller labels do not classify trace source.
      - scope: Access/control bookkeeping
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-inbox-cursor
        - memory.md#mem-obj-mirror-state
        - memory.md#mem-obj-session-meta
        - memory.md#mem-obj-agent-registration
        - runtime.md#rt-obj-step-state
        note: No qualifying trace-learning chain is established for these recorded fixed-code control
          structures.
      - scope: Durable evaluator-output adoption
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-evaluator-readback
        - epistemic.md#epi-rte-bucket-evaluation
        note: The later report/adoption route was not inspected; trial data cannot establish the source
          of an unestablished learning write.
      records:
      - memory.md#mem-obj-session-parts
      - runtime.md#rt-rte-session-mirror
      - runtime.md#rt-rte-session-compact
      - memory.md#mem-obj-memory-live
      - memory.md#mem-obj-memory-history
      - memory.md#mem-obj-message-content
      - memory.md#mem-obj-handoff
      - memory.md#mem-obj-artifact-file
      - memory.md#mem-obj-inbox-cursor
      - memory.md#mem-obj-mirror-state
      - memory.md#mem-obj-session-meta
      - memory.md#mem-obj-agent-registration
      - runtime.md#rt-obj-step-state
      - memory.md#mem-rte-evaluator-readback
      - epistemic.md#epi-rte-bucket-evaluation
      note: Sources are classified only for qualifying trace-learning writes. Recorded host sessions and
        trial activity alone cannot populate this axis without that chain; unresolved routes prevent inapplicability.
---

# Tracecraft memory profile

## Comparison rationale

The profile classifies accepted records, not additional source evidence. Bucket-backed content is `service-object`, while the local cursor and durable trial output are `files`. Host SQLite is an acquisition source. Shipped Markdown instructions and local credentials are outside accumulated memory, so their instruction authority and access controls do not become memory findings. The object inventory is supplied by [MEM-OBJ-session-parts](memory.md#mem-obj-session-parts), [MEM-OBJ-mirror-state](memory.md#mem-obj-mirror-state), [MEM-OBJ-agent-registration](memory.md#mem-obj-agent-registration) and [MEM-RTE-evaluator-readback](memory.md#mem-rte-evaluator-readback), together with the other cited object records.

Software storage I/O is not admission agency. Caller-submitted values, completion notes and uploaded files retain unresolved human control. In contrast, mirror deltas, cursor advancement, compiled compact output and evaluator row emission are automatic after initiation. See [RT-RTE-memory-write](runtime.md#rt-rte-memory-write), [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror), [MEM-OBJ-inbox-cursor](memory.md#mem-obj-inbox-cursor) and [MEM-RTE-evaluator-readback](memory.md#mem-rte-evaluator-readback).

Claim ownership supplies both an admissibility criterion and a veto at completion. Status supplies enforced dependency readiness and routes the waiter; neither checks work correctness. Message/value reference use is only afforded at the external agent. An uploaded file cannot be classified by its filename, and a stored handoff directive cannot be assigned operative instruction authority without its later consumer. See [RT-RTE-step-control](runtime.md#rt-rte-step-control), [RT-BAP-step-polling](runtime.md#rt-bap-step-polling), [MEM-OBJ-artifact-file](memory.md#mem-obj-artifact-file) and [MEM-OBJ-handoff](memory.md#mem-obj-handoff).

Retained session metadata has two distinct effects. List/show/status views display inspection information, supporting knowledge authority. Session list also sorts by recency or size and applies a default limit of 20, so retained metadata supplies ranking inputs even though fixed code implements the ordering. The ranking finding is wired, not evidence of actual agent uptake or a learned scoring policy. Registration display remains separate from this sorting effect. See [MEM-OBJ-session-meta](memory.md#mem-obj-session-meta), [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror) and [MEM-OBJ-agent-registration](memory.md#mem-obj-agent-registration).

Replacement revises retained entries. Deleting direct mail forgets those records. Cursor filtering suppresses delivery without deleting content; it is not retained-content deduplication. Transcript compact combines bytes and reduces object count, not the claims represented. Neither its name nor regex redaction establishes semantic consolidation or synthesis. See [RT-RTE-mail-exchange](runtime.md#rt-rte-mail-exchange), [RT-RTE-session-compact](runtime.md#rt-rte-session-compact) and [EPI-RTE-regex-scrub](epistemic.md#epi-rte-regex-scrub).

All established content deliveries are requested. A new-mail cursor, an exact file name, or a tail budget does not turn a requested result into push. Missing handoff-reader wiring and uninspected durable evaluator report reads prevent a complete pull-only classification and system-wide read-back-signal inapplicability. See [MEM-OBJ-handoff](memory.md#mem-obj-handoff), [RT-RTE-mail-exchange](runtime.md#rt-rte-mail-exchange) and [MEM-RTE-evaluator-readback](memory.md#mem-rte-evaluator-readback).

Raw/transformed session retention is not by itself trace learning. The records identify no derived continuation summary with a later guidance consumer; opaque already-derived host checkpoints do not supply their original derivation chain. Evaluator emission also lacks an inspected durable-output-to-policy consumer. No analyst declared an evidenced-absence record. Accordingly the trace axes retain uncertainty rather than manufacture a bounded `no` or declare trace source inapplicable. This does not suppress any accepted positive learning finding: none establishes the qualifying chain. See [MEM-OBJ-session-parts](memory.md#mem-obj-session-parts), [RT-RTE-session-mirror](runtime.md#rt-rte-session-mirror) and [MEM-RTE-evaluator-readback](memory.md#mem-rte-evaluator-readback).

Reconciliation supersedes the epistemic and workflow handoff objects with [MEM-OBJ-handoff](memory.md#mem-obj-handoff), the epistemic transcript object with [MEM-OBJ-session-parts](memory.md#mem-obj-session-parts), and the epistemic history-loss claim with [MEM-CLM-history-immutability](memory.md#mem-clm-history-immutability). The profile uses those canonical anchors; these identity amendments neither increase basis nor resolve consumer gaps. The two evaluator route records remain distinct.

Source-read log: none. Classification used the complete supplied members and contracts only; no frozen source ambiguity required a source read. Implementation findings are wired, external usage is afforded, and none is promoted to observed operation or causal benefit.
