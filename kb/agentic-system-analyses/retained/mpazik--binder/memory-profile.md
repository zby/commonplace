---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Binder memory comparison: retained journal/task content, mutable graph configuration, file projections and recovery history."
run-id: AAS-2026-10-15-binder-a35c41531d40-01
source-identity: https://github.com/mpazik/binder
reviewed-boundary: e4066d750ac5c6918706f44b12daa261b261106e
memory-comparison:
  version: 2
  scope: >-
    Retained journal observations, summaries, scores, goals and plans; task findings,
    specifications, criteria, status and links; mutable schema/view/navigation
    configuration; transaction, redo and repair history; and selected disk projections
    with synchronization metadata. Includes their shipped capture, import, edit,
    maintenance, request/read and subscribed-delivery paths. Opaque journal data-sync
    injection and incompletely recorded workflow/app/browser alternatives remain
    unresolved where relevant. Excludes shipped static skills as accumulated memory,
    ephemeral importer proposals, fresh completion contexts and process-local caches
    as independent memory stores. External host/provider memory, weights and unshipped
    extension implementations are outside this boundary; shipped extension delivery
    and its limits remain included.
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Retained graph records, mutable config and transaction state"
          assessment: known
          findings:
            - value: sqlite
              basis: wired
              records: [runtime.md#rt-obj-knowledge-graph, memory.md#mem-obj-config-views]
              note: "The workspace database retains record/config tables and transaction history; graph is the data model, not an additional inferred substrate."
          records: [runtime.md#rt-obj-knowledge-graph, memory.md#mem-obj-config-views]
          note: "Covers the recorded database container and its journal/task/config parts; transient caches are not separate accumulated objects."
        - scope: "Rendered documents, snapshot metadata, transaction logs, backups and redo staging"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-snapshot-metadata, memory.md#mem-rte-history-maintenance]
              note: "Disk snapshots and JSONL/recovery files survive for later reading, synchronization or restoration."
            - value: sqlite
              basis: wired
              records: [memory.md#mem-obj-snapshot-metadata]
              note: "Snapshot synchronization metadata also resides in CLI database tables."
          records: [memory.md#mem-obj-snapshot-metadata, memory.md#mem-rte-history-maintenance]
          note: "Separates retained disk content from its database access metadata."
        - scope: "Journal extra data-sync payload before graph admission and unassessed app/browser retained alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-journal-curation, memory.md#mem-rte-selected-read]
          note: "The records name injected health/calendar/activity context and uninspected frontend details but do not establish their retained-object inventory or storage before delivery."
      records: [runtime.md#rt-obj-knowledge-graph, memory.md#mem-obj-snapshot-metadata, memory.md#mem-rte-history-maintenance, memory.md#mem-rte-journal-curation, memory.md#mem-rte-selected-read]
      note: "SQLite and files are wired; opaque injection and incompletely assessed consumer alternatives prevent complete inventory coverage. Provider storage and model weights are excluded, not classified as absent."
    representational_form:
      assessment: partial
      units:
        - scope: "Journal/task prose, goals, plans, specifications and displayed template text at people/model consumers"
          assessment: known
          findings:
            - value: natural-language
              basis: claimed
              records: [memory.md#mem-obj-journal-log, memory.md#mem-obj-journal-summary, memory.md#mem-obj-journal-plan, memory.md#mem-obj-task-findings, memory.md#mem-obj-task-specification, runtime.md#rt-bap-task-guidance]
              note: "Shipped journal/task procedures ask interpreting agents and people to use retained descriptions and contracts. This is not evidence of compliance."
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-snapshot-metadata, memory.md#mem-rte-document-projection]
              note: "Rendered documents carry selected text to filesystem/editor readers; rendering does not establish model use."
          records: [memory.md#mem-obj-journal-log, memory.md#mem-obj-journal-summary, memory.md#mem-obj-journal-plan, memory.md#mem-obj-task-findings, memory.md#mem-obj-task-specification, memory.md#mem-obj-snapshot-metadata]
          note: "Covers recorded prose parts and the separate interpreting versus rendering consumption paths."
        - scope: "Graph/config rules, keys, status/links, synchronization metadata and recovery transactions at fixed-rule consumers"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [runtime.md#rt-obj-knowledge-graph, memory.md#mem-obj-config-views, memory.md#mem-obj-snapshot-metadata, memory.md#mem-rte-history-maintenance]
              note: "Localized schema/query/path/hash/version units control admission, projection and recovery."
            - value: symbolic
              basis: claimed
              records: [memory.md#mem-obj-journal-summary, epistemic.md#epi-obj-task, runtime.md#rt-rte-task-guide]
              note: "Prompts assign score integers arithmetic/calibration roles and task status/field presence guide-selection roles."
          records: [runtime.md#rt-obj-knowledge-graph, memory.md#mem-obj-config-views, memory.md#mem-obj-snapshot-metadata, memory.md#mem-rte-history-maintenance, epistemic.md#epi-obj-task]
          note: "Typed containers and numeric scores are not distributed-parametric representations."
        - scope: "Opaque extra journal payload and unassessed consumer alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-journal-curation, memory.md#mem-rte-selected-read]
          note: "Named context categories and display projections cannot establish every consumed payload's encoding or interpretation."
      records: [runtime.md#rt-obj-knowledge-graph, memory.md#mem-rte-journal-curation, memory.md#mem-rte-selected-read, memory.md#mem-obj-config-views, memory.md#mem-obj-snapshot-metadata, epistemic.md#epi-obj-task]
      note: "Natural-language and symbolic findings retain their local evidence layers. External model computation is not a retained parametric memory finding within this scope."
    lineage:
      assessment: partial
      units:
        - scope: "Known journal capture, summary, planning and task capture/design derivation paths"
          assessment: partial
          findings:
            - value: authored
              basis: claimed
              records: [memory.md#mem-rte-journal-curation, memory.md#mem-rte-task-curation, memory.md#mem-obj-task-specification]
              note: "People supply or approve retained goals, plans, task descriptions and design contracts."
            - value: trace-extracted
              basis: claimed
              records: [memory.md#mem-obj-journal-log, memory.md#mem-obj-journal-summary, memory.md#mem-rte-journal-curation, epistemic.md#epi-rte-task-findings]
              note: "Conversation captures, activity distillation and investigation findings derive from recorded activity or execution feedback; approval does not erase this derivation."
            - value: imported
              basis: claimed
              records: [memory.md#mem-obj-journal-log, memory.md#mem-obj-journal-summary]
              note: "The journal permits externally sourced health information and information from articles; actual original-source provenance is not captured."
          records: [memory.md#mem-obj-journal-log, memory.md#mem-obj-journal-summary, memory.md#mem-obj-journal-plan, memory.md#mem-rte-task-curation, epistemic.md#epi-rte-task-findings]
          note: "Positive paths do not determine initial live-content authorship, every input's origin or opaque injected-data derivation."
        - scope: "Mutable schema/view configuration and fresh record/config import"
          assessment: partial
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-rte-history-maintenance, runtime.md#rt-rte-graph-update]
              note: "Parsed file/stdin transaction inputs admit records and config through graph update."
            - value: authored
              basis: claimed
              records: [memory.md#mem-obj-config-views, epistemic.md#epi-rte-import-mapping]
              note: "Modeling edits and approved mappings supply workspace configuration or mapped records."
          records: [memory.md#mem-obj-config-views, memory.md#mem-rte-history-maintenance, epistemic.md#epi-rte-import-mapping]
          note: "Live initialization and the original authorship of arbitrary imported content remain unknown."
        - scope: "Rendered snapshots, synchronization metadata and transaction recovery derivatives"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-snapshot-metadata, memory.md#mem-rte-document-projection, memory.md#mem-rte-history-maintenance]
              note: "Deterministic projection, metadata generation and recovery staging derive representations from graph/history inputs, not semantic model extraction."
          records: [memory.md#mem-obj-snapshot-metadata, memory.md#mem-rte-document-projection, memory.md#mem-rte-history-maintenance]
          note: "Known immediate derivation is not a claim that every original source or squash provenance field survives."
      records: [memory.md#mem-rte-journal-curation, memory.md#mem-rte-task-curation, memory.md#mem-obj-config-views, memory.md#mem-rte-document-projection, memory.md#mem-rte-history-maintenance]
      note: "Retains authored, imported, trace-extracted and compiled paths without resolving live initialization, injected inputs or omitted provenance."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Retained journal observations/summaries/scores and task diagnoses at briefing, review and implementation consumers"
          assessment: known
          findings:
            - value: knowledge
              basis: claimed
              records: [memory.md#mem-bap-journal-guidance, memory.md#mem-obj-task-findings, runtime.md#rt-bap-task-guidance]
              note: "Selected descriptions, diagnoses and scores supply evidence, context and calibration advice to the foreground agent/user."
            - value: learning
              basis: claimed
              records: [memory.md#mem-rte-journal-curation, epistemic.md#epi-rte-journal-review]
              note: "Retained activity and prior summaries feed durable future plans/goals at review/planning consumers. This update force does not establish improved capacity or automatic admission."
          records: [memory.md#mem-bap-journal-guidance, memory.md#mem-obj-task-findings, runtime.md#rt-bap-task-guidance, memory.md#mem-rte-journal-curation, epistemic.md#epi-rte-journal-review]
          note: "Separates context at the later work consumer from experience feeding durable behavior-shaping plans at the update consumer."
        - scope: "Retained journal goals/plans and task specifications/criteria at planning and product-work consumers"
          assessment: known
          findings:
            - value: instruction
              basis: claimed
              records: [memory.md#mem-obj-journal-plan, memory.md#mem-obj-task-specification, runtime.md#rt-bap-task-guidance]
              note: "Plans express commitments and specifications are design contracts interpreted by the agent, not executable permission gates."
            - value: validation
              basis: claimed
              records: [memory.md#mem-obj-task-specification, runtime.md#rt-rte-task-guide]
              note: "Retained acceptance criteria are checked before considering implementation done under prompt policy."
          records: [memory.md#mem-obj-journal-plan, memory.md#mem-obj-task-specification, runtime.md#rt-rte-task-guide]
          note: "The criteria's completion role is separate from the specification's directive force; neither is a runtime-enforced release gate."
        - scope: "Retained task status, field presence and links at guide selection and duplicate screening"
          assessment: known
          findings:
            - value: routing
              basis: claimed
              records: [runtime.md#rt-rte-task-guide, epistemic.md#epi-obj-task]
              note: "Status, missing diagnosis/specification and links determine the next guide or stop branch through agent interpretation."
            - value: validation
              basis: claimed
              records: [memory.md#mem-rte-task-curation]
              note: "Retained cancelled/existing tasks inform duplicate rejection and admission decisions in capture/refinement."
          records: [runtime.md#rt-rte-task-guide, epistemic.md#epi-obj-task, memory.md#mem-rte-task-curation]
          note: "Prompt screening has no demonstrated exhaustive duplicate oracle or mechanically enforced semantic veto."
        - scope: "Mutable schema/config at structural admission and view/navigation projection consumers"
          assessment: known
          findings:
            - value: validation
              basis: wired
              records: [runtime.md#rt-rte-graph-update, memory.md#mem-obj-config-views]
              note: "Retained schema supplies structural criteria for fresh changes."
            - value: enforcement
              basis: wired
              records: [runtime.md#rt-rte-graph-update, memory.md#mem-obj-config-views]
              note: "Schema/changeset failures refuse graph-managed mutations; this is not factual truth checking."
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-config-views, memory.md#mem-rte-document-projection]
              note: "Navigation query/path and view slots choose content and output destinations."
          records: [runtime.md#rt-rte-graph-update, memory.md#mem-obj-config-views, memory.md#mem-rte-document-projection]
          note: "Fresh preparation and projection are covered; prepared replay is not assigned fresh schema validation."
        - scope: "Snapshot metadata and retained history at synchronization, redo and repair consumers"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-snapshot-metadata, memory.md#mem-rte-document-projection, runtime.md#rt-rte-journal-repair]
              note: "Paths/hash state select synchronization treatment and history divergence selects replacement suffixes."
            - value: validation
              basis: wired
              records: [epistemic.md#epi-rte-undo-redo, runtime.md#rt-clm-transaction-boundary]
              note: "Retained predecessor/version state determines admissibility of replay/redo."
            - value: enforcement
              basis: wired
              records: [epistemic.md#epi-rte-undo-redo, runtime.md#rt-clm-transaction-boundary]
              note: "Mismatched predecessor/version blocks application; restoration is not factual endorsement."
          records: [memory.md#mem-obj-snapshot-metadata, memory.md#mem-rte-document-projection, runtime.md#rt-rte-journal-repair, epistemic.md#epi-rte-undo-redo, runtime.md#rt-clm-transaction-boundary]
          note: "Assigns force only to consumed metadata/history, not to unused author labels or absent rationale."
        - scope: "Injected journal payload and incompletely assessed app/browser or remaining guide effects"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-journal-curation, memory.md#mem-rte-selected-read, memory.md#mem-rte-task-curation]
          note: "Records do not inventory every selected part and consumer effect; no ranking authority is inferred merely from search, scores or ordered results."
      records: [memory.md#mem-bap-journal-guidance, runtime.md#rt-bap-task-guidance, memory.md#mem-obj-config-views, memory.md#mem-rte-document-projection, epistemic.md#epi-rte-undo-redo, memory.md#mem-rte-journal-curation, memory.md#mem-rte-task-curation, memory.md#mem-rte-selected-read]
      note: "Knowledge, instruction, learning, routing, validation and enforcement are locally supported, with claimed semantic and wired structural force kept separate. Unresolved consumers prevent a complete-value assertion."
    write_agency:
      assessment: partial
      units:
        - scope: "Explicitly supplied day-log content and user-approved journal summary/planning, task capture/refinement/design and import mapping/application"
          assessment: known
          findings:
            - value: manual
              basis: claimed
              records: [memory.md#mem-rte-journal-curation, memory.md#mem-rte-task-curation, epistemic.md#epi-rte-import-mapping]
              note: "These named prompt paths require the person to supply the content or approve the retained proposal; starting a workflow alone is not the warrant."
          records: [memory.md#mem-rte-journal-curation, memory.md#mem-rte-task-curation, epistemic.md#epi-rte-import-mapping]
          note: "Approval is prompt policy, not a universal graph write invariant."
        - scope: "Day-update compact conversation capture, day-start post-answer capture and investigation findings without separate content approval"
          assessment: known
          findings:
            - value: automatic
              basis: claimed
              records: [memory.md#mem-rte-journal-curation, memory.md#mem-rte-task-curation, epistemic.md#epi-rte-task-findings]
              note: "Agent admission selects/derives retained content without an explicit per-content human decision; conversation participation is not approval of the generated capture or diagnosis."
          records: [memory.md#mem-rte-journal-curation, memory.md#mem-rte-task-curation, epistemic.md#epi-rte-task-findings]
          note: "These are instructed agent writes, not observed automatic operation."
        - scope: "Structural journal initialization, document/metadata generation and software-selected history reconciliation/staging"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-rte-journal-curation, memory.md#mem-rte-document-projection, memory.md#mem-rte-history-maintenance, runtime.md#rt-rte-journal-repair]
              note: "Code determines structural entries, projected content and selected recovery suffixes; an invocation or --yes authorizes an operation, not review of each retained content item."
          records: [memory.md#mem-rte-journal-curation, memory.md#mem-rte-document-projection, memory.md#mem-rte-history-maintenance, runtime.md#rt-rte-journal-repair]
          note: "The initializer's executable structural writes are separated from semantic journal prompt policy."
        - scope: "Generic CLI/MCP/HTTP/library input, disk authoring, initial live content and opaque injected-data admission"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-graph-update, runtime.md#rt-rte-document-sync, memory.md#mem-obj-journal-plan, memory.md#mem-rte-journal-curation]
          note: "Parsers and software I/O do not resolve whether a human decided the admitted content. Caller identity, disk authorship and live initialization are not established."
      records: [runtime.md#rt-rte-graph-update, runtime.md#rt-rte-document-sync, memory.md#mem-rte-journal-curation, memory.md#mem-rte-task-curation, memory.md#mem-rte-document-projection, memory.md#mem-rte-history-maintenance, epistemic.md#epi-rte-import-mapping]
      note: "Manual and automatic mechanisms coexist; generic caller writes and original/injected content remain unresolved rather than inheriting either classification."
    curation_operations:
      assessment: partial
      units:
        - scope: "Journal log-to-summary/period aggregation and user-agreed retained plan/learning edits"
          assessment: partial
          findings:
            - value: consolidate
              basis: claimed
              records: [memory.md#mem-obj-journal-summary, memory.md#mem-rte-journal-curation]
              note: "Day and period procedures distill retained activity/child summaries while keeping raw logs separately addressable."
            - value: dedup
              basis: claimed
              records: [memory.md#mem-rte-journal-curation]
              note: "Period-summary requests final deduplicated lines merged from child and period captures."
            - value: evolve
              basis: claimed
              records: [memory.md#mem-rte-journal-curation, epistemic.md#epi-rte-journal-review]
              note: "Confirmed corrections and period updates revise existing retained summary, learning and planning fields."
            - value: invalidate
              basis: claimed
              records: [memory.md#mem-obj-journal-plan, memory.md#mem-rte-journal-curation]
              note: "Explicit drop decisions end carry-forward reliance while prior plan history remains."
          records: [memory.md#mem-obj-journal-summary, memory.md#mem-obj-journal-plan, memory.md#mem-rte-journal-curation, epistemic.md#epi-rte-journal-review]
          note: "Prompt transformations are supported as claimed, not reliable execution. Opaque inputs and indeterminate semantic generation prevent resolving synthesis; learning-line labels alone do not establish a new claim."
        - scope: "Task refinement merge/cancellation and collaborative retained-field revision"
          assessment: partial
          findings:
            - value: dedup
              basis: claimed
              records: [memory.md#mem-rte-task-curation]
              note: "Refinement merges unique overlapping content into an existing task and cancels the duplicate draft."
            - value: invalidate
              basis: claimed
              records: [memory.md#mem-rte-task-curation]
              note: "Cancelled records remain searchable while being withdrawn from implementation and informing rejection of recreation."
            - value: evolve
              basis: claimed
              records: [memory.md#mem-rte-task-curation, memory.md#mem-obj-task-specification]
              note: "Refinement and design replace or complete retained task fields under user agreement."
          records: [memory.md#mem-rte-task-curation, memory.md#mem-obj-task-specification, epistemic.md#epi-rte-task-findings]
          note: "No concrete diagnosis establishes non-entailment; remaining guide/app policies are incompletely recorded. Does not upgrade candidate explanations to synthesis."
        - scope: "Deterministic history squash and rollback/replay maintenance"
          assessment: partial
          findings:
            - value: consolidate
              basis: wired
              records: [memory.md#mem-rte-history-maintenance]
              note: "Squash reduces a transaction suffix to a merged transaction, reducing history granularity."
            - value: evolve
              basis: wired
              records: [memory.md#mem-rte-history-maintenance, runtime.md#rt-rte-journal-repair]
              note: "Recovery replaces current retained graph/history state with selected restored state."
          records: [memory.md#mem-rte-history-maintenance, runtime.md#rt-rte-journal-repair]
          note: "Exact squash aggregation, all provenance preservation and restoration algorithms remain uninspected; these operations do not establish factual criticism."
        - scope: "Projection cleanup, index/access maintenance and opaque injection alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-document-projection, memory.md#mem-rte-selected-read, memory.md#mem-rte-journal-curation]
          note: "Rendering/orphan deletion and query limits do not by themselves establish decay, semantic consolidation or invalidation with retained claim history; opaque alternatives cannot be classified."
      records: [memory.md#mem-rte-journal-curation, memory.md#mem-rte-task-curation, memory.md#mem-rte-history-maintenance, memory.md#mem-rte-document-projection, epistemic.md#epi-rte-journal-review, epistemic.md#epi-rte-task-findings]
      note: "Retains consolidation, deduplication, evolution and bounded withdrawal at their actual evidence layers. No supported promote, decay or synthesize finding is inferred from route names or uncertain model output."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Requested graph reads/searches and named journal/task later-use commands"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [memory.md#mem-rte-selected-read]
              note: "CLI/MCP/HTTP/library handlers fulfill a caller's request for selected retained records/config."
            - value: pull
              basis: claimed
              records: [memory.md#mem-rte-journal-curation, runtime.md#rt-rte-task-guide]
              note: "Journal invocation requests preloaded fields and follow-up reads; task work requests rereads. Delivery fulfilling these requests is not a second push."
          records: [memory.md#mem-rte-selected-read, memory.md#mem-rte-journal-curation, runtime.md#rt-rte-task-guide]
          note: "Requested skill-time context and explicit rereads establish intended later consumers, not always-on injection."
        - scope: "Commit/subscription delivery and automatic document projection for later consumers"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-extension-load, runtime.md#rt-rte-graph-update]
              note: "Subscribed commit events automatically supply transaction JSON to configured hooks without a hook read request; arbitrary subsequent extension memory is not inferred."
            - value: push
              basis: wired
              records: [memory.md#mem-rte-document-projection]
              note: "Originating commit/rollback triggers config-selected retained graph material to disk/editor channels for later reading or sync; an explicit render invocation is a separate requested leg."
            - value: pull
              basis: wired
              records: [memory.md#mem-rte-document-projection, runtime.md#rt-rte-document-sync, memory.md#mem-rte-history-maintenance]
              note: "Explicit render/sync and recovery invocations request retained material; later readers or redo calls obtain files/history on demand."
          records: [runtime.md#rt-rte-extension-load, runtime.md#rt-rte-graph-update, memory.md#mem-rte-document-projection, runtime.md#rt-rte-document-sync, memory.md#mem-rte-history-maintenance]
          note: "These pushes are to extension/filesystem/editor consumers, not an established automatic model-memory injector."
        - scope: "Extra journal data-sync delivery and incompletely recorded app/browser consumers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-journal-curation, memory.md#mem-rte-selected-read]
          note: "Payload producer, request boundary and selector wiring are not established for the extra injection or every consumer alternative."
      records: [memory.md#mem-rte-selected-read, memory.md#mem-rte-journal-curation, runtime.md#rt-rte-task-guide, runtime.md#rt-rte-extension-load, memory.md#mem-rte-document-projection, memory.md#mem-rte-history-maintenance]
      note: "Both pull and non-model push routes exist; unresolved injection prevents calling the whole memory boundary pull-only or completely inventoried."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Subscribed transaction push to configured hooks"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-extension-load, runtime.md#rt-rte-graph-update]
              note: "Trigger is subscribed commit activity; enabled hook configuration/event availability selects the transaction JSON delivered. No target-identity or semantic matching selector is established."
          records: [runtime.md#rt-rte-extension-load, runtime.md#rt-rte-graph-update]
          note: "Covers the recorded hook supply operation, not the unknown extension's subsequent selection or retention."
        - scope: "Automatic graph-to-document projection selection"
          assessment: partial
          findings:
            - value: coarse
              basis: wired
              records: [memory.md#mem-rte-document-projection, memory.md#mem-obj-config-views]
              note: "Commit/rollback triggers navigation queries and view-slot projection over graph entities; namespace/rendered-set and save-mode checks bound supplied files."
          records: [memory.md#mem-rte-document-projection, memory.md#mem-obj-config-views, memory.md#mem-obj-snapshot-metadata]
          note: "Recorded config/filter selection supports coarse delivery. Full query/slot algorithms are not recorded; paths and entity UIDs in metadata alone do not establish identifier-matched targeted push."
        - scope: "Requested journal/task/graph read operations"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-rte-selected-read, memory.md#mem-rte-journal-curation, runtime.md#rt-rte-task-guide]
          note: "These named operations fulfill requests, so their keys/filters are pull selectors, not push-signal findings."
        - scope: "Opaque extra journal injection and other unassessed delivery alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-journal-curation, memory.md#mem-rte-selected-read]
          note: "No recorded trigger/input-to-selected-payload chain classifies an additional signal. Unknown direction is not pull-only inapplicability."
      records: [runtime.md#rt-rte-extension-load, memory.md#mem-rte-document-projection, memory.md#mem-rte-selected-read, memory.md#mem-rte-journal-curation, runtime.md#rt-rte-task-guide]
      note: "Coarse push selection is supported locally; opaque injection and bounded projection inspection prevent complete signal coverage. Requested identifiers establish no identifier-based push."
    trace_learning:
      assessment: partial
      units:
        - scope: "Automatic agent conversation capture in day-update/day-start followed by later journal review/planning"
          assessment: known
          findings:
            - value: "yes"
              basis: claimed
              records: [memory.md#mem-obj-journal-log, memory.md#mem-rte-journal-curation, memory.md#mem-bap-journal-guidance]
              note: "Conversation feeds agent-selected compact retained capture without per-content approval; later summary/briefing/planning invocations receive that durable contextual artifact. No improvement is required or observed."
          records: [memory.md#mem-obj-journal-log, memory.md#mem-rte-journal-curation, memory.md#mem-bap-journal-guidance]
          note: "Only the named automatic capture mechanisms are classified; human-approved day/period summaries do not inherit their write agency."
        - scope: "Automatic investigation findings written after reproduction/tracing and consumed on task reread"
          assessment: known
          findings:
            - value: "yes"
              basis: claimed
              records: [epistemic.md#epi-rte-task-findings, memory.md#mem-rte-task-curation, memory.md#mem-obj-task-findings, runtime.md#rt-rte-task-guide]
              note: "Requested reproduction/execution feedback feeds an agent-written durable diagnosis without a separate confirmation step; subsequent guide selection and implementation consume it."
          records: [epistemic.md#epi-rte-task-findings, memory.md#mem-rte-task-curation, memory.md#mem-obj-task-findings, runtime.md#rt-rte-task-guide]
          note: "Doctrine establishes the chain as claimed, not execution, causal correctness or improved future capacity."
        - scope: "User-approved summaries, plans, task design and direct user-supplied content"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-rte-journal-curation, memory.md#mem-rte-task-curation, epistemic.md#epi-rte-import-mapping]
          note: "These explicitly manual admission mechanisms do not meet automatic trace-fed write conditions, even when trace inputs inform human decisions. This is not a system-wide no."
        - scope: "Structural initialization, projection and recovery plumbing as described"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-rte-document-projection, memory.md#mem-rte-history-maintenance, runtime.md#rt-rte-journal-repair, memory.md#mem-rte-journal-curation]
          note: "Recorded automatic projection/restore/initialization does not derive a new behavior-shaping artifact from experience; raw recovery traces and fixed structural copies alone do not qualify."
        - scope: "Generic caller/disk admissions, opaque injected input and unassessed remaining transformation alternatives"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-graph-update, runtime.md#rt-rte-document-sync, memory.md#mem-rte-journal-curation, memory.md#mem-rte-task-curation]
          note: "Content control, trace-fed production or later-consumer chains are unresolved for these alternatives; no bounded absence record licenses a global no."
      records: [memory.md#mem-rte-journal-curation, memory.md#mem-rte-task-curation, epistemic.md#epi-rte-task-findings, runtime.md#rt-rte-task-guide, runtime.md#rt-rte-graph-update, memory.md#mem-rte-document-projection, memory.md#mem-rte-history-maintenance]
      note: "Yes is supported at the claimed layer for automatic conversational capture and investigation retention. Manual/structural routes and unresolved alternatives remain local; no observed or causal learning benefit is asserted."
    trace_source:
      assessment: partial
      units:
        - scope: "Qualifying automatic day-update/day-start conversation capture"
          assessment: partial
          findings:
            - value: session-logs
              basis: claimed
              records: [memory.md#mem-obj-journal-log, memory.md#mem-rte-journal-curation]
              note: "Original conversational turns from the journal work session feed the compact capture; a journal wrapper does not change their origin."
          records: [memory.md#mem-obj-journal-log, memory.md#mem-rte-journal-curation]
          note: "Conversation origin is established; extra calendar/health/activity injection has opaque producer/content and is not fully traced into this automatic write."
        - scope: "Qualifying automatic task investigation findings"
          assessment: partial
          findings:
            - value: tool-traces
              basis: claimed
              records: [epistemic.md#epi-rte-task-findings, memory.md#mem-obj-task-findings, memory.md#mem-rte-task-curation]
              note: "The guide requests running the reproduction and confirming the symptom before retaining diagnosis; that execution feedback is a tool-trace input, alongside code/history and task text."
          records: [epistemic.md#epi-rte-task-findings, memory.md#mem-obj-task-findings, memory.md#mem-rte-task-curation]
          note: "No observed investigation or complete original-input inventory establishes all trace sources; code inspection and imported task text alone are not tool traces or trajectories."
        - scope: "Manual admission and fixed structural projection/recovery mechanisms"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-rte-journal-curation, memory.md#mem-rte-task-curation, memory.md#mem-rte-document-projection, memory.md#mem-rte-history-maintenance]
          note: "These specifically bounded mechanisms lack a qualifying automatic trace-learning write; source categories are not assigned to them merely because they use logs."
        - scope: "Unresolved generic writes, opaque injection and remaining transformation alternatives"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-graph-update, runtime.md#rt-rte-document-sync, memory.md#mem-rte-journal-curation, memory.md#mem-rte-task-curation]
          note: "Neither qualifying write status nor a complete original trace-input chain is established; event-streams and trajectories cannot be inferred from timestamps, health labels or multi-step workflow names."
      records: [memory.md#mem-obj-journal-log, memory.md#mem-rte-journal-curation, epistemic.md#epi-rte-task-findings, memory.md#mem-rte-task-curation, runtime.md#rt-rte-graph-update, runtime.md#rt-rte-document-sync]
      note: "Session-logs and tool-traces are claimed sources of the positive routes; opaque/mixed inputs prevent a complete source union. The printed Git-import proposal has no qualifying durable-write route."
---

# Binder memory profile

## Comparison rationale

### Boundary and evidence layers

The comparison concerns accumulated graph content and its retained projections,
configuration and recovery state. It does not classify the whole runtime's
capabilities as memory. SQLite is the inspected persistence substrate;
“knowledge graph” names the logical container. Disk snapshots and recovery
files are additional retained objects. Ephemeral process caches and printed
import proposals do not become independent memory stores merely because they
have representations. See [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph),
[MEM-OBJ-snapshot-metadata](memory.md#mem-obj-snapshot-metadata) and
[RT-RTE-git-import](runtime.md#rt-rte-git-import).

Implementation supports wired storage, structural admission, projection and
recovery. Shipped prompts support claimed semantic curation and agent use.
Neither layer establishes observed execution, dependable factual distillation
or causal improvement. A wired database write affordance does not upgrade the
journal/task semantic procedures to wired automation. See
[MEM-RTE-journal-curation](memory.md#mem-rte-journal-curation),
[MEM-RTE-task-curation](memory.md#mem-rte-task-curation) and
[RT-CLM-transaction-boundary](runtime.md#rt-clm-transaction-boundary).

### Authority and admission are independent

Retained descriptions supply knowledge; retained plans and specifications
supply directions. Acceptance criteria supply a prompt-level validation
standard, whereas retained schema and predecessor state participate in
executable validation and vetoes. Task status/field presence routes guide
selection. Experience consumed to revise a durable plan has learning authority
at that update consumer, independently of manual admission and without proving
improved capacity. See [MEM-BAP-journal-guidance](memory.md#mem-bap-journal-guidance),
[MEM-OBJ-task-specification](memory.md#mem-obj-task-specification),
[RT-RTE-task-guide](runtime.md#rt-rte-task-guide),
[EPI-RTE-journal-review](epistemic.md#epi-rte-journal-review) and
[EPI-RTE-undo-redo](epistemic.md#epi-rte-undo-redo).

User-approved summary/design writes are manual even when models produce their
wording. Conversely, an agent-written compact conversation capture or
investigation finding without a content approval step is automatic at the
claimed layer. Generic CLI/MCP/HTTP callers remain unresolved: physical I/O,
author labels and a permissive API do not identify the admission decision.
See [MEM-RTE-journal-curation](memory.md#mem-rte-journal-curation),
[MEM-RTE-task-curation](memory.md#mem-rte-task-curation) and
[RT-RTE-graph-update](runtime.md#rt-rte-graph-update).

### Curation, trace learning and later consumption

Distilling retained activity into summaries is consolidation even when raw
logs survive. Requested duplicate merges, retained-field revision and explicit
cancellation/drop support separate operations, not a blanket synthesis
classification. No recorded concrete generated proposition establishes the
non-entailment needed to classify synthesis. The history squash implementation
supports consolidation at a different layer from prompt-mediated journal
summaries; it does not establish preservation of every provenance field.
See [MEM-OBJ-journal-summary](memory.md#mem-obj-journal-summary),
[MEM-RTE-task-curation](memory.md#mem-rte-task-curation),
[MEM-RTE-history-maintenance](memory.md#mem-rte-history-maintenance) and
[EPI-RTE-journal-review](epistemic.md#epi-rte-journal-review).

The positive trace-learning units are narrower than all journal/task writes.
Automatic conversational captures become durable context for later review or
planning. Investigation retains execution-informed diagnosis for subsequent
task rereads. These qualify at the claimed layer without requiring new
knowledge, observed improvement or weight updates. The manual day/period
summary paths are not silently relabeled automatic. The Git importer remains
a proposal producer, not an automatic durable learning route. See
[MEM-OBJ-journal-log](memory.md#mem-obj-journal-log),
[MEM-RTE-journal-curation](memory.md#mem-rte-journal-curation),
[EPI-RTE-task-findings](epistemic.md#epi-rte-task-findings) and
[RT-RTE-git-import](runtime.md#rt-rte-git-import).

Requested skill context is pull. Subscribed hook delivery and automatic
config-directed projection supply non-model push paths. Their coarse event,
query and availability filtering does not establish targeted identity matching
or semantic ranking. An identifier on a requested record, output path or
metadata row is insufficient. Opaque extra journal injection remains unresolved
rather than making the system pull-only. See
[MEM-RTE-selected-read](memory.md#mem-rte-selected-read),
[RT-RTE-extension-load](runtime.md#rt-rte-extension-load),
[MEM-RTE-document-projection](memory.md#mem-rte-document-projection) and
[MEM-RTE-journal-curation](memory.md#mem-rte-journal-curation).

### Canonical records and coverage limits

Reconciliation supersedes the epistemic journal-summary object with
[MEM-OBJ-journal-summary](memory.md#mem-obj-journal-summary). All summary
classifications use that canonical object; the supersession changes no value
or evidence layer. The broader task grouping
[EPI-OBJ-task](epistemic.md#epi-obj-task) remains valid for status and links
alongside the finer findings/specification parts. History-maintenance and
repair, projection and ingress, and journal-curation and journal-review remain
distinct overlapping routes, not duplicate witnesses to be promoted in strength.

The records leave original live-content admission/provenance, extra
calendar/health/activity payloads and parts of app/browser or remaining guide
behavior unresolved. The workflow member extends guide inspection but does
not supply a complete new retained-object or trace-input inventory. These gaps
prevent complete-value assessments; they do not erase supported routes or
justify a system-wide negative. See
[MEM-RTE-journal-curation](memory.md#mem-rte-journal-curation),
[MEM-RTE-task-curation](memory.md#mem-rte-task-curation),
[MEM-RTE-selected-read](memory.md#mem-rte-selected-read) and
[RT-RTE-task-guide](runtime.md#rt-rte-task-guide).

Source-read log: none. This classification used only the supplied accepted
members and reconciliation; no target-source ambiguity required a direct read.
