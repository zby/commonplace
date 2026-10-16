---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'MemPalace memory comparison profile: retained drawers, derived locators, continuity, temporal
  and coordination state with unresolved alternatives.'
run-id: AAS-2026-10-14-mempalace-ed71875aea5a-01
source-identity: https://github.com/milla-jovovich/mempalace
reviewed-boundary: 1392e1810c3ca67776bd7fe3e198788a96dbd6d1
memory-comparison:
  version: 2
  scope: 'Included: use-accumulated drawer text/access metadata/embeddings, closet locators, diary/checkpoint
    content and ingest state, editable identity, setup entity/origin state, temporal KG rows, tunnel/hallway
    navigation and proposal state, media references and original externally retained bytes, logstream
    tasks/events/artifacts, write audit state and backup/replication/recovery alternatives, plus unresolved
    provider request retention. Excluded: static shipped skills/prompts/configuration and pretrained model
    weights as computation, transient queues/search tags/audit reports, benchmark-only reporting without
    an established operational memory consumer, and the external host/model implementation. Shipped host
    adapters and their later-context routes remain included.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Drawer text, metadata, diary specializations, closets and their dense indexes in the inspected
          collection route
        assessment: known
        findings:
        - value: vector
          basis: wired
          records: &id001
          - memory.md#mem-obj-drawer-text
          - memory.md#mem-obj-drawer-metadata
          - memory.md#mem-obj-drawer-vectors
          - memory.md#mem-obj-closet-lines
          - memory.md#mem-obj-diary-entry
          - runtime.md#rt-rte-hermes-capture
          note: The drawer and locator collection persists indexed text, metadata and embeddings for later
            selection.
        records: *id001
        note: The Chroma collection route retains document/access parts in a vector store; dense vectors
          are not model weights.
      - scope: Temporal relationship rows and logstream task, patch and acknowledgment retention
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records: &id002
          - memory.md#mem-obj-kg-triples
          - runtime.md#rt-obj-task-request
          - runtime.md#rt-obj-patch-artifact
          - workflow.md#wf-rte-event-ack
          note: KG tables and logstream event/artifact rows persist relationships, task bodies, proposals
            and linked responses.
        records: *id002
        note: These independent retained objects have explicit SQLite storage.
      - scope: Identity, setup origin/entity files, original daily files and ingest state, tunnel sidecar,
          proposal plan and write audit log
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id003
          - memory.md#mem-obj-identity-text
          - runtime.md#rt-rte-init-detection
          - memory.md#mem-obj-diary-entry
          - memory.md#mem-obj-tunnels
          - epistemic.md#epi-rte-tunnel-maintenance
          - memory.md#mem-obj-write-log
          note: Filesystem objects persist these inputs, navigation parts and audit/proposal state.
        records: *id003
        note: The records identify editable text, JSON/sidecar/plan and JSONL retention rather than merely
          in-process values.
      - scope: Identity Layer0 instance cache and host wake-context cache retained across later prompt
          assemblies
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id004
          - memory.md#mem-obj-identity-text
          - memory.md#mem-rte-wake-context
          - runtime.md#rt-rte-palace-recall
          - runtime.md#rt-bap-agent-context
          note: Process/agent-local caches keep rendered identity and selected wake content available
            to later consumer invocations.
        records: *id004
        note: These are later-consumed cached copies of retained material, not durable filesystem replacements
          or transient worker queues.
      - scope: Hallway sidecar lifecycle, non-Chroma backend variants, native index persistence and backup/export/migration/replicated
          copies
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-tunnels
        - memory.md#mem-obj-drawer-vectors
        - memory.md#mem-obj-write-log
        - runtime.md#rt-rte-backend-registration
        - memory.md#mem-rte-memory-maintenance
        note: Adapter names and exposed repair/replication capabilities do not establish complete physical
          retention or replacement semantics; remote/native and recovery internals remain incompletely
          inspected.
      - scope: External provider request retention or other use-accumulated provider state
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-cmp-closet-provider
        - runtime.md#rt-cmp-openai-compat
        - runtime.md#rt-rte-init-detection
        note: The clients supply content to providers, but request retention is uninspected. Pretrained
          provider weights are excluded static computation, not classified as accumulated memory.
      records:
      - memory.md#mem-obj-drawer-text
      - memory.md#mem-obj-drawer-metadata
      - memory.md#mem-obj-drawer-vectors
      - memory.md#mem-obj-closet-lines
      - memory.md#mem-obj-diary-entry
      - runtime.md#rt-rte-hermes-capture
      - memory.md#mem-obj-kg-triples
      - runtime.md#rt-obj-task-request
      - runtime.md#rt-obj-patch-artifact
      - workflow.md#wf-rte-event-ack
      - memory.md#mem-obj-identity-text
      - runtime.md#rt-rte-init-detection
      - memory.md#mem-obj-tunnels
      - epistemic.md#epi-rte-tunnel-maintenance
      - memory.md#mem-obj-write-log
      - memory.md#mem-rte-wake-context
      - runtime.md#rt-rte-palace-recall
      - runtime.md#rt-bap-agent-context
      - runtime.md#rt-rte-backend-registration
      - memory.md#mem-rte-memory-maintenance
      - memory.md#mem-cmp-closet-provider
      - runtime.md#rt-cmp-openai-compat
      note: The inventory includes drawer/index collections, sidecar and identity files, temporal and
        coordination rows, proposal/WAL state, and unresolved backend, recovery and provider-retention
        alternatives. Known stores do not resolve those alternatives.
    representational_form:
      assessment: partial
      units:
      - scope: Drawer, diary, identity and closet word content at interpreting agent/human consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id005
          - memory.md#mem-obj-drawer-text
          - memory.md#mem-obj-diary-entry
          - memory.md#mem-obj-identity-text
          - memory.md#mem-obj-closet-lines
          - runtime.md#rt-bap-agent-context
          note: Words supply recall, continuity, identity guidance and topic/quote/summary locators through
            interpretation.
        records: *id005
        note: This unit classifies readable retained parts only, not accompanying access fields or media
          bytes.
      - scope: Task goal, definition of done, delivery body and acknowledgment prose
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id006
          - runtime.md#rt-obj-task-request
          - workflow.md#wf-rte-task-create
          - workflow.md#wf-rte-event-ack
          - runtime.md#rt-bap-task-handoff
          note: A later worker or coordination reader interprets retained task and response text.
        records: *id006
        note: Interpretive work directions and reported coordination outcomes differ from routing envelopes.
      - scope: Drawer access metadata, KG graph/temporal controls, tunnel endpoints/counters, WAL envelopes,
          task routing and patch diff
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id007
          - memory.md#mem-obj-drawer-metadata
          - memory.md#mem-obj-kg-triples
          - memory.md#mem-obj-tunnels
          - memory.md#mem-obj-write-log
          - runtime.md#rt-obj-task-request
          - runtime.md#rt-obj-patch-artifact
          note: Filters, reconstruction, validity, graph navigation, coordination linkage and potential
            patch consumers operate on symbolic structure.
        records: *id007
        note: Localized fields and diff units have fixed software consumers; this does not claim that
          patches are applied.
      - scope: KG entity labels and relation claim contents at interpreting fact readers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id008
          - memory.md#mem-obj-kg-triples
          - memory.md#mem-rte-temporal-facts
          note: Returned labels and relation claims require interpretation; their graph placement does
            not verify meaning.
        records: *id008
        note: World-relation interpretation is separate from the fixed temporal/database fields.
      - scope: Media descriptor title at an interpreting result reader
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id009
          - memory.md#mem-obj-media-asset
          - memory.md#mem-rte-media-index
          note: The title/descriptor supplies readable reference information.
        records: *id009
        note: The descriptor is not a caption/transcript of the opaque file.
      - scope: Media file-reference metadata at fixed index/result consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id010
          - memory.md#mem-obj-media-asset
          - memory.md#mem-rte-media-index
          note: Path, modality, dimensions, availability and provenance are structured reference fields.
        records: *id010
        note: Reference fields describe the asset without classifying its opaque payload.
      - scope: Stored drawer, closet and asset dense embeddings
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: &id011
          - memory.md#mem-obj-drawer-vectors
          - memory.md#mem-rte-media-index
          note: Dense representations influence candidate distance and selection.
        records: *id011
        note: Numerical data spreads representation across dimensions; inference-derived vectors are not
          trained weights.
      - scope: Original image/audio/video bytes reached only by a separate file-open consumer
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-media-asset
        - memory.md#mem-rte-media-index
        note: No automatic payload attachment or inspected downstream payload consumer establishes its
          operative representation; the descriptor cannot resolve it.
      - scope: Additional hallway, backend/native, recovery, provider-retained and incompletely inspected
          event/artifact parts
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-tunnels
        - memory.md#mem-obj-drawer-vectors
        - memory.md#mem-obj-write-log
        - runtime.md#rt-rte-backend-registration
        - runtime.md#rt-obj-patch-artifact
        note: Known object forms do not enumerate all opaque retained parts or their consumption semantics.
      records:
      - memory.md#mem-obj-drawer-text
      - memory.md#mem-obj-diary-entry
      - memory.md#mem-obj-identity-text
      - memory.md#mem-obj-closet-lines
      - runtime.md#rt-bap-agent-context
      - runtime.md#rt-obj-task-request
      - workflow.md#wf-rte-task-create
      - workflow.md#wf-rte-event-ack
      - runtime.md#rt-bap-task-handoff
      - memory.md#mem-obj-drawer-metadata
      - memory.md#mem-obj-kg-triples
      - memory.md#mem-obj-tunnels
      - memory.md#mem-obj-write-log
      - runtime.md#rt-obj-patch-artifact
      - memory.md#mem-rte-temporal-facts
      - memory.md#mem-obj-media-asset
      - memory.md#mem-rte-media-index
      - memory.md#mem-obj-drawer-vectors
      - runtime.md#rt-rte-backend-registration
      note: Readable content, fixed-rule access/control fields and dense numerical representations are
        split. Opaque media payloads and backend/recovery/provider alternatives remain unresolved; display
        descriptors never classify their full payload.
    lineage:
      assessment: partial
      units:
      - scope: Source-file, project/conversation corpus, daily-file and media-reference import paths
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id012
          - memory.md#mem-rte-source-filing
          - memory.md#mem-obj-diary-entry
          - memory.md#mem-rte-media-index
          - memory.md#mem-obj-drawer-text
          note: Existing files, exports, summaries and referenced media enter retained collections.
        records: *id012
        note: These paths acquire preexisting material; original authorship and parser fidelity remain
          separate questions.
      - scope: Host turn capture and deterministic silent checkpoint derivation
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id013
          - runtime.md#rt-rte-hermes-capture
          - runtime.md#rt-rte-hook-ingest
          - memory.md#mem-rte-diary-checkpoint
          note: Host session content supplies captured exchanges and selected user-message prefixes.
        records: *id013
        note: Recorded conversational activity is normalized or reduced into retained exchanges and continuity
          entries.
      - scope: General extraction and closet regeneration on retained session-derived drawers
        assessment: partial
        findings:
        - value: trace-extracted
          basis: wired
          records: &id014
          - memory.md#mem-rte-source-filing
          - memory.md#mem-rte-closet-regeneration
          - memory.md#mem-obj-closet-lines
          note: Session-derived content supplies selected segments or generated locators on the trace-fed
            branch.
        records: *id014
        note: The known derivation is selective extraction or source-grouped generation; source groups
          can also contain imported non-trace files.
      - scope: Generated metadata, vectors, entity classifications, heuristic locators and graph links/access
          fields
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id015
          - memory.md#mem-obj-drawer-metadata
          - memory.md#mem-obj-drawer-vectors
          - memory.md#mem-obj-closet-lines
          - runtime.md#rt-rte-init-detection
          - memory.md#mem-obj-tunnels
          - memory.md#mem-rte-tunnel-traversal
          note: Software or model inference constructs access metadata, embeddings, classifications, locators
            and navigation summaries.
        records: *id015
        note: Code/model derivation is known; original source and external embedding-weight provenance
          are not thereby settled.
      - scope: Formatted task envelope, acknowledgment linkage, WAL intent/outcome envelopes and proposal
          plan
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id016
          - workflow.md#wf-rte-task-create
          - workflow.md#wf-rte-event-ack
          - memory.md#mem-obj-write-log
          - epistemic.md#epi-rte-tunnel-maintenance
          note: Code formats supplied task/response fields and derives linked audit/proposal records.
        records: *id016
        note: The records establish software construction of these envelopes/plans, not original authorship
          of all embedded content.
      - scope: User-written identity text as shipped doctrine
        assessment: partial
        findings:
        - value: authored
          basis: claimed
          records: &id017
          - memory.md#mem-obj-identity-text
          note: Doctrine describes identity text as user-written.
        records: *id017
        note: Authorship is claimed by doctrine; the implemented file reader cannot establish the author
          of an installed file.
      - scope: Initial identity edits, explicit caller drawer/diary/KG/task/patch content and imported
          daily summaries
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-identity-text
        - runtime.md#rt-rte-mcp-dispatch
        - memory.md#mem-rte-diary-checkpoint
        - memory.md#mem-rte-temporal-facts
        - runtime.md#rt-obj-task-request
        - runtime.md#rt-obj-patch-artifact
        note: Generic caller identity and a stored source label cannot establish original authorship or
          derivation; these initial-content paths are included, not assumed authored.
      - scope: Original provenance of dense embeddings across providers/backends and additional recovery/import
          variants
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-drawer-vectors
        - runtime.md#rt-rte-backend-registration
        - memory.md#mem-obj-write-log
        - memory.md#mem-cmp-closet-provider
        note: Inference derivation is supported, but exact external artifacts, all retained provider state
          and native/recovery alternatives are not fully inspected.
      records:
      - memory.md#mem-rte-source-filing
      - memory.md#mem-obj-diary-entry
      - memory.md#mem-rte-media-index
      - memory.md#mem-obj-drawer-text
      - runtime.md#rt-rte-hermes-capture
      - runtime.md#rt-rte-hook-ingest
      - memory.md#mem-rte-diary-checkpoint
      - memory.md#mem-rte-closet-regeneration
      - memory.md#mem-obj-closet-lines
      - memory.md#mem-obj-drawer-metadata
      - memory.md#mem-obj-drawer-vectors
      - runtime.md#rt-rte-init-detection
      - memory.md#mem-obj-tunnels
      - memory.md#mem-rte-tunnel-traversal
      - workflow.md#wf-rte-task-create
      - workflow.md#wf-rte-event-ack
      - memory.md#mem-obj-write-log
      - epistemic.md#epi-rte-tunnel-maintenance
      - memory.md#mem-obj-identity-text
      - runtime.md#rt-rte-mcp-dispatch
      - memory.md#mem-rte-temporal-facts
      - runtime.md#rt-obj-task-request
      - runtime.md#rt-obj-patch-artifact
      - runtime.md#rt-rte-backend-registration
      - memory.md#mem-cmp-closet-provider
      note: The inventory preserves import, trace extraction and compiled access/index derivations beside
        claimed authorship and unresolved original content/provider provenance. One known derivation never
        resolves the initial material it consumes.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Drawer/diary text, KG assertions and media descriptors at later recall/fact/reference consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id018
          - memory.md#mem-obj-drawer-text
          - memory.md#mem-rte-diary-checkpoint
          - memory.md#mem-rte-temporal-facts
          - memory.md#mem-rte-media-index
          - runtime.md#rt-rte-palace-recall
          note: Selected testimony, continuity entries, relationship claims and asset references provide
            evidence/context to later readers.
        records: *id018
        note: The consumers receive selected content or references, not independently accepted truths
          or necessarily full payloads.
      - scope: Identity text at startup host guidance
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id019
          - memory.md#mem-obj-identity-text
          - runtime.md#rt-bap-agent-context
          note: Identity text is supplied as system-prompt guidance by the adapter.
        records: *id019
        note: The host-facing identity channel is implemented; actual host insertion and compliance remain
          unobserved.
      - scope: Retained task directions at the later worker named by the task protocol
        assessment: known
        findings:
        - value: instruction
          basis: afforded
          records: &id020
          - runtime.md#rt-obj-task-request
          - runtime.md#rt-bap-task-handoff
          - workflow.md#wf-rte-task-create
          note: The addressed worker is instructed to retrieve and follow goal/done/delivery text.
        records: *id020
        note: The stored body has a documented later instructional consumer; the pointer handoff does
          not establish completed body reload.
      - scope: Drawer and closet words, stored vectors and weighted/dated access metadata at retrieval/startup
          selection
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id021
          - memory.md#mem-obj-drawer-text
          - memory.md#mem-obj-closet-lines
          - memory.md#mem-obj-drawer-vectors
          - memory.md#mem-obj-drawer-metadata
          - runtime.md#rt-rte-palace-recall
          - memory.md#mem-rte-wake-context
          note: Content/embeddings affect semantic or lexical candidate priority; weights and timestamps
            order startup snippets.
        records: *id021
        note: Fixed software scoring still gives its retained inputs ranking authority; no learned scoring
          policy is required.
      - scope: Drawer source/chunk fields, entity registry, tunnel endpoints and task/event routing fields
          at fixed selectors
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id022
          - memory.md#mem-obj-drawer-metadata
          - runtime.md#rt-rte-init-detection
          - memory.md#mem-obj-tunnels
          - runtime.md#rt-obj-task-request
          - workflow.md#wf-rte-event-ack
          note: Software consumers select source groups, chunks, entity-linked scopes, graph endpoints
            and addressed events.
        records: *id022
        note: These retained fields choose filing scope, reconstructed input, navigation destinations
          and coordination recipients.
      - scope: Retained IDs/freshness metadata and drawer/vector content at duplicate/admission checks
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id023
          - memory.md#mem-obj-drawer-metadata
          - runtime.md#rt-rte-mcp-dispatch
          - epistemic.md#epi-rte-duplicate-check
          - epistemic.md#epi-rte-checkpoint-disposition
          note: Existing IDs, source freshness and indexed material are checked to determine write admissibility.
        - value: enforcement
          basis: wired
          records: *id023
          note: ID/freshness and positive duplicate results can veto retention on their implemented paths;
            dedup errors remain fail-open.
        records: *id023
        note: Retained state supplies structural/idempotency criteria or approximate similarity, not a
          truth oracle.
      - scope: KG validity intervals at explicit as_of/current-category consumers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id024
          - memory.md#mem-obj-kg-triples
          - memory.md#mem-rte-temporal-facts
          note: Temporal fields select current/historical/future buckets or an as_of input set.
        - value: enforcement
          basis: wired
          records: *id024
          note: Explicit as_of predicates exclude rows outside their actual validity intervals.
        records: *id024
        note: Interval fields affect eligibility or temporal grouping while history survives; reused successor
          visibility remains conditional.
      - scope: Session trace material at automatic checkpoint and trace-fed locator update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id025
          - memory.md#mem-rte-diary-checkpoint
          - memory.md#mem-rte-closet-regeneration
          - memory.md#mem-rte-source-filing
          note: Session content feeds durable continuity artifacts or locator updates used by later consumers.
        records: *id025
        note: This is the update-side force of retained experience, separate from output knowledge/ranking.
          No improvement is inferred.
      - scope: Tunnel strength/decay beyond displayed history, opaque media payload use, additional provider/backend/recovery
          and event/artifact consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-tunnel-traversal
        - memory.md#mem-obj-tunnels
        - memory.md#mem-rte-media-index
        - memory.md#mem-obj-drawer-vectors
        - memory.md#mem-obj-write-log
        - runtime.md#rt-obj-patch-artifact
        note: Records establish counters and references but not default-ranking influence, payload interpretation,
          full recovery effects or all coordination consumers. WAL diagnostics are afforded, not an automatic
          model-memory path.
      records:
      - memory.md#mem-obj-drawer-text
      - memory.md#mem-rte-diary-checkpoint
      - memory.md#mem-rte-temporal-facts
      - memory.md#mem-rte-media-index
      - runtime.md#rt-rte-palace-recall
      - memory.md#mem-obj-identity-text
      - runtime.md#rt-bap-agent-context
      - runtime.md#rt-obj-task-request
      - runtime.md#rt-bap-task-handoff
      - workflow.md#wf-rte-task-create
      - memory.md#mem-obj-closet-lines
      - memory.md#mem-obj-drawer-vectors
      - memory.md#mem-obj-drawer-metadata
      - memory.md#mem-rte-wake-context
      - runtime.md#rt-rte-init-detection
      - memory.md#mem-obj-tunnels
      - workflow.md#wf-rte-event-ack
      - runtime.md#rt-rte-mcp-dispatch
      - epistemic.md#epi-rte-duplicate-check
      - epistemic.md#epi-rte-checkpoint-disposition
      - memory.md#mem-obj-kg-triples
      - memory.md#mem-rte-closet-regeneration
      - memory.md#mem-rte-source-filing
      - memory.md#mem-rte-tunnel-traversal
      - memory.md#mem-obj-write-log
      - runtime.md#rt-obj-patch-artifact
      note: Each finding names retained part, consumer and effect. Context delivery is knowledge or guidance,
        not observed compliance. Index/update consumers differ from answering consumers. Uninspected graph,
        provider, recovery and coordination alternatives prevent complete coverage.
    write_agency:
      assessment: partial
      units:
      - scope: Hermes turns, hook transcript filing, corpus segment admission and media indexing
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id026
          - runtime.md#rt-rte-hermes-capture
          - runtime.md#rt-rte-hook-ingest
          - memory.md#mem-rte-source-filing
          - memory.md#mem-rte-media-index
          note: Software selects/adopts content after readiness, routing, format or modality checks without
            itemwise human approval.
        records: *id026
        note: A host trigger or operator starting import does not approve each retained item.
      - scope: Silent checkpoint, heuristic/LLM closet generation, automatic setup topics and tunnel traversal
          counters
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id027
          - memory.md#mem-rte-diary-checkpoint
          - memory.md#mem-rte-closet-regeneration
          - memory.md#mem-obj-closet-lines
          - runtime.md#rt-rte-init-detection
          - memory.md#mem-rte-tunnel-traversal
          note: Code/model admission creates continuity snippets, locators, passed-through topics and
            traversal summaries.
        records: *id027
        note: These exact branches admit derived material without a per-content human decision.
      - scope: Interactive people/project entity confirmation
        assessment: known
        findings:
        - value: manual
          basis: wired
          records: &id028
          - runtime.md#rt-rte-init-detection
          note: An explicit operator confirmation/edit supplies the adopted people/project entries.
        records: *id028
        note: This branch permits human editing/approval of the detected retained entity content.
      - scope: Noninteractive --yes setup admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id029
          - runtime.md#rt-rte-init-detection
          note: Detected entries are auto-accepted by the noninteractive branch.
        records: *id029
        note: Bypassing item review does not convert subsequent classifier output admission into human
          content approval.
      - scope: User-edited tunnel proposal followed by explicit application
        assessment: known
        findings:
        - value: manual
          basis: wired
          records: &id030
          - epistemic.md#epi-rte-tunnel-maintenance
          note: The operator can edit the retained plan and explicitly approve its application.
        records: *id030
        note: The proposal orchestration exposes retained rows for deletion/editing before operator adoption;
          underlying generation/prune algorithms remain outside this unit.
      - scope: Identity authoring, audit restructuring and exact normalized task approval under shipped
          operating doctrine
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records: &id031
          - memory.md#mem-obj-identity-text
          - memory.md#mem-rte-memory-maintenance
          - workflow.md#wf-rte-task-create
          note: Doctrine assigns identity writing, restructuring decisions and normalized task approval
            to the operator.
        records: *id031
        note: These policies require a human content decision but are not enforced by the file reader/write
          handlers/task constructor.
      - scope: Explicit drawer/diary/KG writes and replacements, task/patch/ack submissions, initial daily-file/identity
          content
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-mcp-dispatch
        - memory.md#mem-rte-memory-maintenance
        - memory.md#mem-rte-diary-checkpoint
        - memory.md#mem-rte-temporal-facts
        - workflow.md#wf-rte-task-create
        - runtime.md#rt-rte-patch-delivery
        - workflow.md#wf-rte-event-ack
        - memory.md#mem-obj-identity-text
        - memory.md#mem-obj-diary-entry
        note: Software structural checks are known, but generic client identity does not determine whether
          a human supplied/approved each retained content item. Automatic physical persistence alone cannot
          settle admission control.
      - scope: All legacy/prompted capture variants, graph prune/generation controls, backup/migration/replication
          and provider-retention alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-hook-ingest
        - memory.md#mem-rte-diary-checkpoint
        - epistemic.md#epi-rte-tunnel-maintenance
        - memory.md#mem-obj-write-log
        - runtime.md#rt-rte-backend-registration
        note: Known branches do not establish every alternate admission mechanism; prompted agent summaries
          remain requests, not demonstrated writes.
      records:
      - runtime.md#rt-rte-hermes-capture
      - runtime.md#rt-rte-hook-ingest
      - memory.md#mem-rte-source-filing
      - memory.md#mem-rte-media-index
      - memory.md#mem-rte-diary-checkpoint
      - memory.md#mem-rte-closet-regeneration
      - memory.md#mem-obj-closet-lines
      - runtime.md#rt-rte-init-detection
      - memory.md#mem-rte-tunnel-traversal
      - epistemic.md#epi-rte-tunnel-maintenance
      - memory.md#mem-obj-identity-text
      - memory.md#mem-rte-memory-maintenance
      - workflow.md#wf-rte-task-create
      - runtime.md#rt-rte-mcp-dispatch
      - memory.md#mem-rte-temporal-facts
      - runtime.md#rt-rte-patch-delivery
      - workflow.md#wf-rte-event-ack
      - memory.md#mem-obj-diary-entry
      - memory.md#mem-obj-write-log
      - runtime.md#rt-rte-backend-registration
      note: Admission is classified per mechanism, not physical I/O or authorship. Known automatic writes
        coexist with human-reviewed setup and claimed approval policies. Generic caller/initial-file control
        and alternate maintenance/capture mechanisms remain unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Selective general extraction, silent continuity checkpoints and heuristic/LLM closets over
          session/source content
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id032
          - memory.md#mem-rte-source-filing
          - memory.md#mem-rte-diary-checkpoint
          - memory.md#mem-obj-closet-lines
          - memory.md#mem-rte-closet-regeneration
          note: Retained derived content is reduced to selected segments, short user-message prefixes
            or topic/quote/summary lines.
        records: *id032
        note: Each branch selects or compresses existing content into retained segments, prefixes or locators;
          source fidelity and actual operation remain unobserved.
      - scope: Checkpoint near-duplicate suppression
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records: &id033
          - epistemic.md#epi-rte-duplicate-check
          - epistemic.md#epi-rte-checkpoint-disposition
          - memory.md#mem-rte-diary-checkpoint
          note: The check-consuming skip branch removes near-duplicate candidates from the retained save
            set.
        records: *id033
        note: This is approximate redundancy rejection, not semantic equivalence or a primary-key collision
          check.
      - scope: Explicit drawer replacement, source re-mining, diary-file rebuild and closet regeneration
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id034
          - memory.md#mem-rte-memory-maintenance
          - memory.md#mem-rte-source-filing
          - memory.md#mem-rte-diary-checkpoint
          - memory.md#mem-rte-closet-regeneration
          note: Replacement content, rebuilt source chunks or regenerated locators revise retained representations.
        records: *id034
        note: Existing entries or source-scoped derived sets are revised/replaced through inspected maintenance
          writes.
      - scope: Temporal assertion ending and old-value closure on supersession
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records: &id035
          - memory.md#mem-rte-temporal-facts
          - memory.md#mem-obj-kg-triples
          note: Ended validity withdraws an old assertion from eligible current/as_of use while historical
            rows survive.
        - value: evolve
          basis: wired
          records: *id035
          note: A newly inserted successor revises the represented relationship; the reuse branch instead
            returns an existing row.
        records: *id035
        note: History is retained while current reliance/eligibility changes; successor reuse need not
          align its starting instant.
      - scope: Tunnel effective-strength decay function versus an actual later downweighting consumer,
          and traversal strengthening versus promotion
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-tunnel-traversal
        - memory.md#mem-obj-tunnels
        note: A decay function and increased counters/strength are recorded, but scheduled forgetting,
          downstream downweighting and tier/salience promotion are not established. They cannot support
          decay/promote findings at an actual retained-memory consumer.
      - scope: Novel claims potentially generated by opaque providers or uninspected extraction/graph/recovery/maintenance
          branches
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-closet-regeneration
        - memory.md#mem-cmp-closet-provider
        - epistemic.md#epi-rte-tunnel-maintenance
        - memory.md#mem-obj-write-log
        - runtime.md#rt-rte-backend-registration
        - memory.md#mem-rte-memory-maintenance
        note: Generation and summary labels do not establish synthesis. The records do not settle semantic
          novelty or every implemented transformation; known consolidation does not classify opaque alternatives.
      records:
      - memory.md#mem-rte-source-filing
      - memory.md#mem-rte-diary-checkpoint
      - memory.md#mem-obj-closet-lines
      - memory.md#mem-rte-closet-regeneration
      - epistemic.md#epi-rte-duplicate-check
      - epistemic.md#epi-rte-checkpoint-disposition
      - memory.md#mem-rte-memory-maintenance
      - memory.md#mem-rte-temporal-facts
      - memory.md#mem-obj-kg-triples
      - memory.md#mem-rte-tunnel-traversal
      - memory.md#mem-obj-tunnels
      - memory.md#mem-cmp-closet-provider
      - epistemic.md#epi-rte-tunnel-maintenance
      - memory.md#mem-obj-write-log
      - runtime.md#rt-rte-backend-registration
      note: Transformation findings are bounded to implemented retained-content routes. Index rebuilds
        and ID collision checks are not deduplication; display truncation alone is not a retained consolidation.
        Graph decay/use, opaque provider transformations and full maintenance alternatives remain unresolved.
    read_back_direction:
      assessment: partial
      units:
      - scope: MCP/CLI search, host-requested Hermes prefetch and direct logical drawer GET
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id036
          - runtime.md#rt-rte-palace-recall
          - runtime.md#rt-rte-mcp-dispatch
          - memory.md#mem-obj-drawer-text
          note: Queries and direct reads return selected or complete retained drawer material on request.
        records: *id036
        note: The later consumer requests retained material; ranking/hydration and delivery fulfill that
          request.
      - scope: Requested diary continuity, entity/time KG query, tunnel follow, media query and coordination
          event/artifact reads
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id037
          - memory.md#mem-rte-diary-checkpoint
          - memory.md#mem-rte-temporal-facts
          - memory.md#mem-rte-tunnel-traversal
          - memory.md#mem-rte-media-index
          - runtime.md#rt-rte-task-launch
          - runtime.md#rt-rte-patch-delivery
          - workflow.md#wf-rte-event-ack
          note: Later calls retrieve continuity rows, assertions, graph links/previews, media references
            or addressed tasks/artifacts.
        records: *id037
        note: These are distinct request-driven later-consumer routes; documented worker reload is not
          proof of execution.
      - scope: DSH independently triggered session-start wake-up prompt providers and Hermes startup context
          cache
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id038
          - memory.md#mem-rte-wake-context
          - runtime.md#rt-rte-palace-recall
          - runtime.md#rt-bap-agent-context
          note: Session startup refresh/selection makes retained context available through host prompt
            providers.
        records: *id038
        note: Startup code selects and supplies retained identity/snippets without a consumer request
          for those specific stored contents; an explicit CLI wake request is separately pull.
      - scope: Explicit CLI wake-up
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id039
          - memory.md#mem-rte-wake-context
          - runtime.md#rt-rte-palace-recall
          note: An explicit wake request returns retained text selected for that call.
        records: *id039
        note: Requested wake content is not a second push because code delivers it.
      - scope: Exposed Layer2 filtered API without an established independent later consumer
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-palace-recall
        - memory.md#mem-rte-wake-context
        note: The filtered-read capability is known, but its unspecified caller does not establish an
          additional read-back route or direction.
      - scope: Other legacy wake/autosave host variants, diagnostic/recovery reloads, opaque provider
          retention and uninspected event/artifact recipient workflows
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-hook-ingest
        - memory.md#mem-obj-write-log
        - runtime.md#rt-rte-backend-registration
        - runtime.md#rt-obj-patch-artifact
        - memory.md#mem-rte-diary-checkpoint
        note: The accepted records do not establish all later consumer routes or their request boundaries.
          Known push/pull paths do not close this inventory.
      records:
      - runtime.md#rt-rte-palace-recall
      - runtime.md#rt-rte-mcp-dispatch
      - memory.md#mem-obj-drawer-text
      - memory.md#mem-rte-diary-checkpoint
      - memory.md#mem-rte-temporal-facts
      - memory.md#mem-rte-tunnel-traversal
      - memory.md#mem-rte-media-index
      - runtime.md#rt-rte-task-launch
      - runtime.md#rt-rte-patch-delivery
      - workflow.md#wf-rte-event-ack
      - memory.md#mem-rte-wake-context
      - runtime.md#rt-bap-agent-context
      - runtime.md#rt-rte-hook-ingest
      - memory.md#mem-obj-write-log
      - runtime.md#rt-rte-backend-registration
      - runtime.md#rt-obj-patch-artifact
      note: Requested recall and independent startup supply coexist. Each request/selection/delivery chain
        is classified once, not every return as push. Legacy host, recovery/provider and additional coordination
        consumers remain incompletely inspected.
    read_back_signal:
      assessment: partial
      units:
      - scope: Startup Layer0/Layer1 context selection supplied by DSH/Hermes
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id040
          - memory.md#mem-rte-wake-context
          - runtime.md#rt-rte-palace-recall
          - memory.md#mem-obj-identity-text
          - memory.md#mem-obj-drawer-metadata
          note: Availability, wing scope, recency/weight ordering and content budget select generic startup
            context, not query-inferred or identity-matched delivered parts.
        records: *id040
        note: Trigger is session startup/cache refresh; inputs are identity availability, optional wing,
          a recent candidate window, metadata weights/filing time and size budget; selected parts are
          full identity plus up to fifteen truncated drawer snippets.
      - scope: Inspected requested search, prefetch, diary, KG, tunnel, media and coordination reads
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-palace-recall
        - memory.md#mem-rte-diary-checkpoint
        - memory.md#mem-rte-temporal-facts
        - memory.md#mem-rte-tunnel-traversal
        - memory.md#mem-rte-media-index
        - runtime.md#rt-rte-task-launch
        - runtime.md#rt-rte-patch-delivery
        note: These units fulfill later consumer requests. Their embeddings, lexical matches, file IDs
          or correlation IDs do not establish push-selection signals.
      - scope: Additional legacy host wake/recall adapters and provider/recovery or other recipient supply
          alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-hook-ingest
        - memory.md#mem-obj-write-log
        - runtime.md#rt-rte-backend-registration
        - runtime.md#rt-obj-patch-artifact
        - memory.md#mem-rte-wake-context
        note: The records leave those routes incompletely inspected; their unsolicited selectors and delivered
          parts cannot be inferred from a known startup branch.
      records:
      - memory.md#mem-rte-wake-context
      - runtime.md#rt-rte-palace-recall
      - memory.md#mem-obj-identity-text
      - memory.md#mem-obj-drawer-metadata
      - memory.md#mem-rte-diary-checkpoint
      - memory.md#mem-rte-temporal-facts
      - memory.md#mem-rte-tunnel-traversal
      - memory.md#mem-rte-media-index
      - runtime.md#rt-rte-task-launch
      - runtime.md#rt-rte-patch-delivery
      - runtime.md#rt-rte-hook-ingest
      - memory.md#mem-obj-write-log
      - runtime.md#rt-rte-backend-registration
      - runtime.md#rt-obj-patch-artifact
      note: Only unsolicited startup selection is positively classified. Semantic and lexical queries
        are pull, not inferred push signals. Opaque/legacy startup alternatives remain unresolved and
        cannot be made inapplicable by inspected requested readers.
    trace_learning:
      assessment: partial
      units:
      - scope: Silent hook transcript-prefix checkpoint to retained diary to later continuity/search consumer
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id041
          - memory.md#mem-rte-diary-checkpoint
          - memory.md#mem-obj-diary-entry
          note: Trace-fed code selects user-message prefixes and retains them for later contextual continuity.
        records: *id041
        note: The automatic write produces a durable compact continuation artifact from session content;
          later diary/search consumption is recorded.
      - scope: General session extraction and heuristic/LLM locators on session-derived drawers to later
          recall/ranking
        assessment: partial
        findings:
        - value: 'yes'
          basis: wired
          records: &id042
          - memory.md#mem-rte-source-filing
          - memory.md#mem-obj-closet-lines
          - memory.md#mem-rte-closet-regeneration
          - runtime.md#rt-rte-palace-recall
          note: Automatic selection/generation retains derived session content or locators that shape
            later context/retrieval.
        records: *id042
        note: 'This unit includes the trace-fed branch, not every source group: imported project files
          can be non-traces. New knowledge, learned weights and benefit are not required.'
      - scope: Raw-ish Hermes exchange and transcript retention without derived continuation/update
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-hermes-capture
        - runtime.md#rt-rte-hook-ingest
        - memory.md#mem-rte-source-filing
        note: This isolated raw-retention part supplies future information access but no qualifying derived
          behavior-shaping update. General extraction and checkpoint/locator branches are classified separately.
      - scope: Traversal counters/strength with later audit/navigation display
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-tunnel-traversal
        - memory.md#mem-obj-tunnels
        note: Automatic event-fed persistence is known, but the records do not establish those counters
          changing downstream selection or durable behavioral guidance. Mere trace retention/display does
          not decide a qualifying learning route.
      - scope: Prompted or direct summaries, caller KG/content revisions, outcome drawers and initial
          daily summaries
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-diary-checkpoint
        - memory.md#mem-rte-temporal-facts
        - runtime.md#rt-rte-mcp-dispatch
        - workflow.md#wf-clm-review-closure
        - workflow.md#wf-rte-task-create
        note: Caller control, actual trace inputs and/or completion of the derived write are unresolved.
          A requested agent summary or prescribed outcome drawer cannot be upgraded to a wired qualifying
          write.
      - scope: Full hallway/tunnel graph maintenance, legacy host, recovery/native/backend and opaque
          provider update alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-tunnels
        - epistemic.md#epi-rte-tunnel-maintenance
        - runtime.md#rt-rte-hook-ingest
        - memory.md#mem-obj-write-log
        - runtime.md#rt-rte-backend-registration
        - memory.md#mem-cmp-closet-provider
        note: The accepted records do not enumerate every trace-fed write and later behavior-shaping consumer;
          static embedding weights are excluded, not a negative trace-learning witness.
      records:
      - memory.md#mem-rte-diary-checkpoint
      - memory.md#mem-obj-diary-entry
      - memory.md#mem-rte-source-filing
      - memory.md#mem-obj-closet-lines
      - memory.md#mem-rte-closet-regeneration
      - runtime.md#rt-rte-palace-recall
      - runtime.md#rt-rte-hermes-capture
      - runtime.md#rt-rte-hook-ingest
      - memory.md#mem-rte-tunnel-traversal
      - memory.md#mem-obj-tunnels
      - memory.md#mem-rte-temporal-facts
      - runtime.md#rt-rte-mcp-dispatch
      - workflow.md#wf-clm-review-closure
      - workflow.md#wf-rte-task-create
      - epistemic.md#epi-rte-tunnel-maintenance
      - memory.md#mem-obj-write-log
      - runtime.md#rt-rte-backend-registration
      - memory.md#mem-cmp-closet-provider
      note: Automatic durable continuity and trace-fed locator writes qualify without observed improvement.
        Raw transcript retention alone does not. Counters with only navigation/audit display and unresolved
        caller/provider/host/graph alternatives remain local uncertainties, not a system-wide no.
    trace_source:
      assessment: partial
      units:
      - scope: Silent hook checkpoint extraction of recorded session user messages
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id043
          - memory.md#mem-rte-diary-checkpoint
          note: Recorded user turns supply the deterministic retained continuation entry.
        records: *id043
        note: Original input is selected conversation messages, not the Stop callback that merely triggers
          processing.
      - scope: General conversation extraction and closet generation from known session-derived source
          groups
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records: &id044
          - memory.md#mem-rte-source-filing
          - memory.md#mem-rte-closet-regeneration
          - runtime.md#rt-rte-hermes-capture
          - memory.md#mem-obj-closet-lines
          note: Recorded conversational turns feed selected segments and derived locators used later.
        records: *id044
        note: Session provenance is supported for this branch. Source-group generation can also consume
          project/files or mixed material, so that separate provenance is retained as unresolved.
      - scope: Tool-output-containing and other mixed source groups used in general extraction or closet
          generation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-source-filing
        - memory.md#mem-rte-closet-regeneration
        - memory.md#mem-obj-closet-lines
        note: The filing inventory allows tool output and imported files, but does not establish precisely
          which qualifying update consumes which original tool/event/trajectory content. Session content
          does not resolve the whole mixed input.
      - scope: Raw capture-only part and static non-trace file-derived locator branch
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-hermes-capture
        - runtime.md#rt-rte-hook-ingest
        - memory.md#mem-rte-source-filing
        - memory.md#mem-rte-closet-regeneration
        note: Raw retention alone lacks a qualifying derived learning write; imported static project content
          is not a trace merely because transformed into an index. Trace-fed branches are separately included.
      - scope: Traversal-event, caller/prompted summary, outcome, graph/provider and legacy/recovery alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-tunnel-traversal
        - memory.md#mem-rte-diary-checkpoint
        - memory.md#mem-rte-temporal-facts
        - workflow.md#wf-clm-review-closure
        - epistemic.md#epi-rte-tunnel-maintenance
        - memory.md#mem-obj-write-log
        - runtime.md#rt-rte-backend-registration
        note: Trace-learning qualification or original input/control is unresolved on these included routes;
          no whole-axis inapplicability or event-stream/trajectory finding follows.
      records:
      - memory.md#mem-rte-diary-checkpoint
      - memory.md#mem-rte-source-filing
      - memory.md#mem-rte-closet-regeneration
      - runtime.md#rt-rte-hermes-capture
      - memory.md#mem-obj-closet-lines
      - runtime.md#rt-rte-hook-ingest
      - memory.md#mem-rte-tunnel-traversal
      - memory.md#mem-rte-temporal-facts
      - workflow.md#wf-clm-review-closure
      - epistemic.md#epi-rte-tunnel-maintenance
      - memory.md#mem-obj-write-log
      - runtime.md#rt-rte-backend-registration
      note: Source classification follows original content on each qualifying write. Session logs are
        established on known continuity/derived recall branches; mixed file/tool content and other unresolved
        trace-learning routes remain unresolved, not relabelled event streams by serialization.
---

# MemPalace memory profile

## Comparison rationale

### Inventory and evidence strength

The profile classifies accepted records, not source execution. Drawer text, access metadata, embeddings and locator lines are distinct operative parts: [MEM-OBJ-drawer-text](memory.md#mem-obj-drawer-text), [MEM-OBJ-drawer-metadata](memory.md#mem-obj-drawer-metadata), [MEM-OBJ-drawer-vectors](memory.md#mem-obj-drawer-vectors) and [MEM-OBJ-closet-lines](memory.md#mem-obj-closet-lines). Diary rows specialize drawer storage; SQLite temporal and coordination objects are independent stores. The filesystem tunnel sidecar is not classified as a graph substrate merely because its encoding expresses links. Media descriptors classify references, not opaque file contents. See [MEM-OBJ-diary-entry](memory.md#mem-obj-diary-entry), [MEM-OBJ-kg-triples](memory.md#mem-obj-kg-triples), [RT-OBJ-task-request](runtime.md#rt-obj-task-request), [MEM-OBJ-tunnels](memory.md#mem-obj-tunnels) and [MEM-OBJ-media-asset](memory.md#mem-obj-media-asset).

Every axis is partial because its inventory retains unresolved included alternatives. Backend names do not establish native/remote retention semantics. Initial file and generic caller control are unresolved. Provider request retention, complete graph policy, every host wrapper, full recovery/replacement and all event/artifact consumers are incompletely established. These limits are carried by [MEM-OBJ-drawer-vectors](memory.md#mem-obj-drawer-vectors), [RT-RTE-backend-registration](runtime.md#rt-rte-backend-registration), [MEM-OBJ-write-log](memory.md#mem-obj-write-log), [MEM-RTE-memory-maintenance](memory.md#mem-rte-memory-maintenance), [MEM-CMP-closet-provider](memory.md#mem-cmp-closet-provider), [RT-OBJ-patch-artifact](runtime.md#rt-obj-patch-artifact) and the route-specific citations in the units. Static embedding/provider weights are computation, not evidence of accumulated model-weight memory. No observation or causal support is asserted.

### Admission, content and effects

An operator starting import or regeneration does not approve each generated item. Software capture and silent checkpoint writes are automatic. Interactive setup confirmation is manual; its --yes alternative is automatic. Generic foreground tool callers and initial daily summaries do not establish human control. Identity writing, restructuring approval and task approval are separately claimed policies rather than universally enforced admission gates. See [RT-RTE-hermes-capture](runtime.md#rt-rte-hermes-capture), [MEM-RTE-closet-regeneration](memory.md#mem-rte-closet-regeneration), [RT-RTE-init-detection](runtime.md#rt-rte-init-detection), [MEM-RTE-diary-checkpoint](memory.md#mem-rte-diary-checkpoint) and [WF-RTE-task-create](workflow.md#wf-rte-task-create).

Knowledge means a retained part supplies context or reference at its consumer, not that its propositions were accepted as true. Identity supplies guidance; worker task instructions have a documented reload consumer, not an observed reload. Ranking is established by stored words, vectors and weighted metadata consumed by fixed scoring code. Duplicate checks separately give retained content validation and enforcing admission effects; ordinary primary-key idempotency alone is not curation deduplication. See [RT-BAP-agent-context](runtime.md#rt-bap-agent-context), [RT-BAP-task-handoff](runtime.md#rt-bap-task-handoff), [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall), [EPI-RTE-duplicate-check](epistemic.md#epi-rte-duplicate-check) and [EPI-RTE-checkpoint-disposition](epistemic.md#epi-rte-checkpoint-disposition).

Consolidation records reduced retained representations, not merely transient wake rendering. Checkpoint prefixes and generated locator lines reduce existing source material; extraction fidelity defects do not establish synthesis. Explicit replacement evolves entries. Temporal ending invalidates current eligibility while preserving history. The corrected successor-reuse branch does not guarantee visibility at the requested boundary, so neither enforcement nor evolution implies unconditional replacement coverage. See [MEM-RTE-source-filing](memory.md#mem-rte-source-filing), [MEM-RTE-diary-checkpoint](memory.md#mem-rte-diary-checkpoint), [MEM-RTE-closet-regeneration](memory.md#mem-rte-closet-regeneration) and [MEM-RTE-temporal-facts](memory.md#mem-rte-temporal-facts).

### Later delivery and trace-fed updates

Query-driven retrieval and host-requested prefetch are pull. Independent startup context supply is push; its selector uses availability, wing, recency/weight and budget. Query embeddings and lexical hydration are therefore not push-signal findings. A task/correlation identifier on a requested reload is not identifier-based push. See [RT-RTE-palace-recall](runtime.md#rt-rte-palace-recall), [MEM-RTE-wake-context](memory.md#mem-rte-wake-context) and [RT-RTE-task-launch](runtime.md#rt-rte-task-launch).

Automatic checkpoint prefixes qualify as trace learning because recorded conversational turns produce a durable continuation artifact for later contextual use. Session-fed extracted segments and locators likewise have later recall/ranking consumers. This classification requires neither learned weights nor improved capacity. Their inputs have learning authority at the update consumer, while the outputs supply knowledge or ranking downstream. Raw transcript retention alone does not establish that update. Traversal counters have recorded audit/navigation display but no established downstream ranking effect; the profile retains that uncertainty instead of assigning a local or system-wide no. See [MEM-RTE-diary-checkpoint](memory.md#mem-rte-diary-checkpoint), [MEM-RTE-source-filing](memory.md#mem-rte-source-filing), [MEM-RTE-closet-regeneration](memory.md#mem-rte-closet-regeneration), [RT-RTE-hermes-capture](runtime.md#rt-rte-hermes-capture) and [MEM-RTE-tunnel-traversal](memory.md#mem-rte-tunnel-traversal).

The Stop event triggers checkpoint work but does not become the checkpoint's original trace source: selected user messages are session logs. Mixed source groups retain their uncertainty; imported project text is not an event stream. No qualifying tool-trace, event-stream or trajectory value is established solely by a callback, source label or stored event envelope. See [MEM-RTE-diary-checkpoint](memory.md#mem-rte-diary-checkpoint) and [MEM-RTE-source-filing](memory.md#mem-rte-source-filing).

### Canonical resolution and source-read log

Reconciliation resolves the duplicated epistemic drawer object to [MEM-OBJ-drawer-text](memory.md#mem-obj-drawer-text), the duplicated epistemic triple object to [MEM-OBJ-kg-triples](memory.md#mem-obj-kg-triples), and the duplicated epistemic temporal route to [MEM-RTE-temporal-facts](memory.md#mem-rte-temporal-facts). The profile uses those canonical destinations. The temporal amendment changes identity resolution, not evidence strength, and keeps the corrected successor-reuse limitation. Startup, duplicate disposition and drawer revision remain valid parts/overlaps, not replacement identities; their local findings are not upgraded by a stronger container witness.

Source reads: none. The supplied accepted records and their annotations establish the classifications and limitations; no new evidence, record declarations or reopened verification were needed.
