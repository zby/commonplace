---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'SwarmWorld memory comparison: live private, public, empirical, program and request memory
  plus recorded reconstruction, with unresolved offline consumers.'
run-id: AAS-2026-10-15-swarmworld-e39fbc17e3fb-01
source-identity: https://github.com/lamm-mit/SwarmWorld
reviewed-boundary: 6af7ae9fa36d98b07b0492cf139658e8af1f6eab
memory-comparison:
  version: 2
  scope: Use-generated private evidence and research state, retrieval metadata, empirical cells, public
    archive, spatial insights, message/request ledger, research mission history, program registry/skills
    and installed retained instructions; recorded traces, replay/playback and included but uninspected
    offline analysis/dossier transformations. Excludes shipped static prompts/catalogs, pre-execution
    queues, ordinary physical world arrays and external provider state/weights.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Live agent-memory
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id001
          - memory.md#mem-obj-agent-memory
          note: Retained content or access metadata resides in process-local collections.
        records: *id001
        note: The record identifies the operative collections; serialization is classified separately.
      - scope: Live research-state
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id002
          - memory.md#mem-obj-research-state
          note: Retained content or access metadata resides in process-local collections.
        records: *id002
        note: The record identifies the operative collections; serialization is classified separately.
      - scope: Live retrieval-stats
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id003
          - memory.md#mem-obj-retrieval-stats
          note: Retained content or access metadata resides in process-local collections.
        records: *id003
        note: The record identifies the operative collections; serialization is classified separately.
      - scope: Live empirical-knowledge
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id004
          - memory.md#mem-obj-empirical-knowledge
          note: Retained content or access metadata resides in process-local collections.
        records: *id004
        note: The record identifies the operative collections; serialization is classified separately.
      - scope: Live cultural-archive
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id005
          - memory.md#mem-obj-cultural-archive
          note: Retained content or access metadata resides in process-local collections.
        records: *id005
        note: The record identifies the operative collections; serialization is classified separately.
      - scope: Live deposited-insights
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id006
          - memory.md#mem-obj-deposited-insights
          note: Retained content or access metadata resides in process-local collections.
        records: *id006
        note: The record identifies the operative collections; serialization is classified separately.
      - scope: Live message-records
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id007
          - memory.md#mem-obj-message-records
          note: Retained content or access metadata resides in process-local collections.
        records: *id007
        note: The record identifies the operative collections; serialization is classified separately.
      - scope: Live research-mission
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id008
          - memory.md#mem-obj-research-mission
          note: Retained content or access metadata resides in process-local collections.
        records: *id008
        note: The record identifies the operative collections; serialization is classified separately.
      - scope: Live program-library
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id009
          - memory.md#mem-obj-program-library
          note: Retained content or access metadata resides in process-local collections.
        records: *id009
        note: The record identifies the operative collections; serialization is classified separately.
      - scope: Live program-skills
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id010
          - memory.md#mem-obj-program-skills
          note: Retained content or access metadata resides in process-local collections.
        records: *id010
        note: The record identifies the operative collections; serialization is classified separately.
      - scope: Recorded events, model decisions, prompt templates and snapshots
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id011
          - memory.md#mem-obj-event-trace
          note: Recorder persists JSONL or gzip streams to the filesystem.
        records: *id011
        note: Files are the retained substrate, not the JSON encoding.
      - scope: Included offline analysis/dossier transformations and downstream consumers of recorded
          research state
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-event-trace
        - epistemic.md#epi-rte-proposal-evaluation
        note: Available offline transformation and consumer internals were not inspected. Their additional
          classifications cannot be enumerated from accepted records.
      records:
      - memory.md#mem-obj-agent-memory
      - memory.md#mem-obj-research-state
      - memory.md#mem-obj-retrieval-stats
      - memory.md#mem-obj-empirical-knowledge
      - memory.md#mem-obj-cultural-archive
      - memory.md#mem-obj-deposited-insights
      - memory.md#mem-obj-message-records
      - memory.md#mem-obj-research-mission
      - memory.md#mem-obj-program-library
      - memory.md#mem-obj-program-skills
      - memory.md#mem-obj-event-trace
      - epistemic.md#epi-rte-proposal-evaluation
      note: Live memory and its file-backed recorded representation are separately inventoried. External
        provider state, static packages and ordinary physical arrays are excluded. Offline alternatives
        remain included and unresolved; positives do not establish a complete system union.
    representational_form:
      assessment: partial
      units:
      - scope: agent-memory prose at model/context or human interpretation
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id012
          - memory.md#mem-obj-agent-memory
          note: Text is interpreted as evidence, advice, goals or hypotheses, rather than executed as
            fixed-rule symbols.
        records: *id012
        note: This unit covers prose only.
      - scope: agent-memory structured IDs, locations, timestamps and provenance
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id013
          - memory.md#mem-obj-agent-memory
          note: Fixed-rule selectors and resolvers consume localized fields.
        records: *id013
        note: Metadata is distinct from the interpreted payload.
      - scope: research-state prose at model/context or human interpretation
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id014
          - memory.md#mem-obj-research-state
          note: Text is interpreted as evidence, advice, goals or hypotheses, rather than executed as
            fixed-rule symbols.
        records: *id014
        note: This unit covers prose only.
      - scope: research-state structured IDs, locations, timestamps and provenance
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id015
          - memory.md#mem-obj-research-state
          note: Fixed-rule selectors and resolvers consume localized fields.
        records: *id015
        note: Metadata is distinct from the interpreted payload.
      - scope: cultural-archive prose at model/context or human interpretation
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id016
          - memory.md#mem-obj-cultural-archive
          note: Text is interpreted as evidence, advice, goals or hypotheses, rather than executed as
            fixed-rule symbols.
        records: *id016
        note: This unit covers prose only.
      - scope: cultural-archive structured IDs, locations, timestamps and provenance
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id017
          - memory.md#mem-obj-cultural-archive
          note: Fixed-rule selectors and resolvers consume localized fields.
        records: *id017
        note: Metadata is distinct from the interpreted payload.
      - scope: deposited-insights prose at model/context or human interpretation
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id018
          - memory.md#mem-obj-deposited-insights
          note: Text is interpreted as evidence, advice, goals or hypotheses, rather than executed as
            fixed-rule symbols.
        records: *id018
        note: This unit covers prose only.
      - scope: deposited-insights structured IDs, locations, timestamps and provenance
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id019
          - memory.md#mem-obj-deposited-insights
          note: Fixed-rule selectors and resolvers consume localized fields.
        records: *id019
        note: Metadata is distinct from the interpreted payload.
      - scope: message-records prose at model/context or human interpretation
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id020
          - memory.md#mem-obj-message-records
          note: Text is interpreted as evidence, advice, goals or hypotheses, rather than executed as
            fixed-rule symbols.
        records: *id020
        note: This unit covers prose only.
      - scope: message-records structured IDs, locations, timestamps and provenance
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id021
          - memory.md#mem-obj-message-records
          note: Fixed-rule selectors and resolvers consume localized fields.
        records: *id021
        note: Metadata is distinct from the interpreted payload.
      - scope: retrieval-stats structured evidence, instructions or access fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id022
          - memory.md#mem-obj-retrieval-stats
          note: Counts, measurements, recipes, DSL instructions or membership have localized fixed-rule
            representation.
        records: *id022
        note: Covers structured parts, not descriptive names or prose claims.
      - scope: empirical-knowledge structured evidence, instructions or access fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id023
          - memory.md#mem-obj-empirical-knowledge
          note: Counts, measurements, recipes, DSL instructions or membership have localized fixed-rule
            representation.
        records: *id023
        note: Covers structured parts, not descriptive names or prose claims.
      - scope: research-mission structured evidence, instructions or access fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id024
          - memory.md#mem-obj-research-mission
          note: Counts, measurements, recipes, DSL instructions or membership have localized fixed-rule
            representation.
        records: *id024
        note: Covers structured parts, not descriptive names or prose claims.
      - scope: program-library structured evidence, instructions or access fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id025
          - memory.md#mem-obj-program-library
          note: Counts, measurements, recipes, DSL instructions or membership have localized fixed-rule
            representation.
        records: *id025
        note: Covers structured parts, not descriptive names or prose claims.
      - scope: program-skills structured evidence, instructions or access fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id026
          - memory.md#mem-obj-program-skills
          note: Counts, measurements, recipes, DSL instructions or membership have localized fixed-rule
            representation.
        records: *id026
        note: Covers structured parts, not descriptive names or prose claims.
      - scope: Research mission task claims at model consumer
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id027
          - memory.md#mem-obj-research-mission
          note: Public task claims are interpreted prose.
        records: *id027
        note: Separate from numeric evaluator fields.
      - scope: Recorded trace text payloads
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id028
          - memory.md#mem-obj-event-trace
          note: Raw request/response text is retained for later record consumers.
        records: *id028
        note: No parametric encoding is established.
      - scope: Recorded trace envelopes, templates and replay fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id029
          - memory.md#mem-obj-event-trace
          - runtime.md#rt-rte-recorded-replay
          note: Reader expands template markers and replay interprets committed-state fields.
        records: *id029
        note: A readable summary does not replace authoritative fields.
      - scope: Included offline analysis/dossier transformations and downstream consumers of recorded
          research state
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-event-trace
        - epistemic.md#epi-rte-proposal-evaluation
        note: Available offline transformation and consumer internals were not inspected. Their additional
          classifications cannot be enumerated from accepted records.
      records:
      - memory.md#mem-obj-agent-memory
      - memory.md#mem-obj-research-state
      - memory.md#mem-obj-cultural-archive
      - memory.md#mem-obj-deposited-insights
      - memory.md#mem-obj-message-records
      - memory.md#mem-obj-retrieval-stats
      - memory.md#mem-obj-empirical-knowledge
      - memory.md#mem-obj-research-mission
      - memory.md#mem-obj-program-library
      - memory.md#mem-obj-program-skills
      - memory.md#mem-obj-event-trace
      - runtime.md#rt-rte-recorded-replay
      - epistemic.md#epi-rte-proposal-evaluation
      note: Mixed natural-language and symbolic parts remain separate; excluded provider weights do not
        make simulator memory parametric. Offline alternatives remain included and unresolved; positives
        do not establish a complete system union.
    lineage:
      assessment: partial
      units:
      - scope: Controller-authored research state, messages, insights and task claims
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id030
          - memory.md#mem-obj-research-state
          - memory.md#mem-rte-social-retention
          - memory.md#mem-obj-research-mission
          note: Model, human or scripted controller supplies retained prose or structured proposals.
        records: *id030
        note: Authorship does not imply human admission or truth.
      - scope: Program instructions proposed through installation
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id031
          - runtime.md#rt-rte-program-install
          - memory.md#mem-obj-program-library
          note: Controller proposes bounded DSL instructions retained in registry/history.
        records: *id031
        note: No trace derivation of arbitrary instruction content is implied.
      - scope: Sensor evidence, measured outcomes, summaries, feedback counters and measured skill indices
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id032
          - memory.md#mem-rte-evidence-retention
          - memory.md#mem-rte-retrieval-feedback
          - memory.md#mem-obj-program-skills
          note: Software derives retained evidence and access metadata from sensing, measurement, selection,
            citation and action outcomes.
        records: *id032
        note: Covers recorded derivation paths, not unsupported model-internal provenance.
      - scope: Teaching copies and replay restoration
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id033
          - memory.md#mem-rte-social-retention
          - runtime.md#rt-rte-recorded-replay
          note: Existing retained content is admitted into another notebook or reconstructed simulation
            without re-authoring its meaning.
        records: *id033
        note: Import is relative to the destination store; original authorship remains distinct.
      - scope: Recorded reversible template factoring and registry canonicalization
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id034
          - memory.md#mem-obj-event-trace
          - memory.md#mem-obj-program-library
          note: Software factors retained strings or constructs canonical registry/history representations
            without trace-based semantic extraction.
        records: *id034
        note: Compilation here names mechanical derivation, not new scientific knowledge.
      - scope: Included offline analysis/dossier transformations and downstream consumers of recorded
          research state
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-event-trace
        - epistemic.md#epi-rte-proposal-evaluation
        note: Available offline transformation and consumer internals were not inspected. Their additional
          classifications cannot be enumerated from accepted records.
      records:
      - memory.md#mem-obj-research-state
      - memory.md#mem-rte-social-retention
      - memory.md#mem-obj-research-mission
      - runtime.md#rt-rte-program-install
      - memory.md#mem-obj-program-library
      - memory.md#mem-rte-evidence-retention
      - memory.md#mem-rte-retrieval-feedback
      - memory.md#mem-obj-program-skills
      - runtime.md#rt-rte-recorded-replay
      - memory.md#mem-obj-event-trace
      - epistemic.md#epi-rte-proposal-evaluation
      note: Different derivation paths for copied, authored and mechanically derived memory are retained.
        Offline alternatives remain included and unresolved; positives do not establish a complete system
        union.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retained evidence and research prose at later model/viewer context
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id035
          - memory.md#mem-rte-context-selection
          - runtime.md#rt-bap-model-guidance
          - memory.md#mem-obj-event-trace
          note: Selected text, measurements and histories supply evidence or context to later model or
            observer consumption.
        records: *id035
        note: Delivery is not demonstrated reliance; research-state goals are not automatically standing
          host instructions.
      - scope: Private/archive text, salience and feedback counters at retrieval; skill evidence at ordering
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id036
          - memory.md#mem-rte-context-selection
          - memory.md#mem-rte-retrieval-feedback
          - memory.md#mem-obj-program-skills
          note: Retained features and numeric feedback alter relative selection priority.
        records: *id036
        note: Ranking authority does not require a learned ranking model.
      - scope: Retained resource evidence, publication provenance and program membership at action validators
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id037
          - memory.md#mem-bap-evidence-admission
          note: Retained evidence determines recipe/provenance and known-parent admissibility.
        - value: enforcement
          basis: wired
          records: *id037
          note: The same fixed-rule checks can veto the proposed action.
        records: *id037
        note: Criteria and enforcing veto coexist at this consumer.
      - scope: Request ledger and committed trace fields at routing consumers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id038
          - memory.md#mem-obj-message-records
          - memory.md#mem-rte-social-retention
          - runtime.md#rt-rte-recorded-replay
          note: Recipient/reply edges select receipt destinations and pending work; commitment markers
            select replay writes.
        records: *id038
        note: Routing is separate from interpreting request prose.
      - scope: Retained selections, citations, outcomes and measurements at automatic update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id039
          - memory.md#mem-rte-retrieval-feedback
          - memory.md#mem-rte-evidence-retention
          - memory.md#mem-obj-program-skills
          note: Experience feeds durable feedback, evidence summaries and skill indices subsequently used
            in context or admission.
        records: *id039
        note: This update-consumer force is separate from the downstream knowledge and ranking forces;
          benefit is unobserved.
      - scope: Installed retained artifact instructions at repeated VM execution
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records: &id040
          - runtime.md#rt-obj-artifact-program
          - runtime.md#rt-bap-program-execution
          note: Fixed DSL instructions determine bounded actuator outputs through the VM and artifact
            dynamics.
        records: *id040
        note: This covers the executable memory part, not arbitrary prose or host permissions.
      - scope: Included offline analysis/dossier transformations and downstream consumers of recorded
          research state
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-event-trace
        - epistemic.md#epi-rte-proposal-evaluation
        note: Available offline transformation and consumer internals were not inspected. Their additional
          classifications cannot be enumerated from accepted records.
      records:
      - memory.md#mem-rte-context-selection
      - runtime.md#rt-bap-model-guidance
      - memory.md#mem-obj-event-trace
      - memory.md#mem-rte-retrieval-feedback
      - memory.md#mem-obj-program-skills
      - memory.md#mem-bap-evidence-admission
      - memory.md#mem-obj-message-records
      - memory.md#mem-rte-social-retention
      - runtime.md#rt-rte-recorded-replay
      - memory.md#mem-rte-evidence-retention
      - runtime.md#rt-obj-artifact-program
      - runtime.md#rt-bap-program-execution
      - epistemic.md#epi-rte-proposal-evaluation
      note: Actual consumers, not labels such as verified or publication, determine authority. Offline
        alternatives remain included and unresolved; positives do not establish a complete system union.
    write_agency:
      assessment: partial
      units:
      - scope: Sensing, measurement, retrieval feedback, recording, reconstruction and inheritance admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id041
          - memory.md#mem-rte-evidence-retention
          - memory.md#mem-rte-retrieval-feedback
          - memory.md#mem-rte-cultural-inheritance
          - memory.md#mem-obj-event-trace
          - runtime.md#rt-rte-recorded-replay
          note: Software admits retained results without per-content human approval.
        records: *id041
        note: Starting the episode or replay is not a content approval decision.
      - scope: Model-generated research-state admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id042
          - runtime.md#rt-rte-model-planning
          - memory.md#mem-obj-research-state
          note: Local schema and evidence-availability filtering admit model output without a human content
            decision.
        records: *id042
        note: Optional outage rollback is a separate software control.
      - scope: Model/script social content and program proposals
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id043
          - memory.md#mem-rte-social-retention
          - runtime.md#rt-rte-program-install
          - runtime.md#rt-rte-direct-control
          note: Software/controller proposals pass simulator checks without routine human approval.
        records: *id043
        note: Different controller routes are not homogenized as manual.
      - scope: Human-play content-bearing action proposals
        assessment: known
        findings:
        - value: manual
          basis: wired
          records: &id044
          - runtime.md#rt-rte-direct-control
          - memory.md#mem-rte-social-retention
          - runtime.md#rt-rte-program-install
          note: A human explicitly supplies a possessed/manual action, including its content when communicating
            or installing a program.
        records: *id044
        note: Only the human content decision is manual; resulting sensing, receipts and metadata updates
          remain automatic.
      - scope: Included offline analysis/dossier transformations and downstream consumers of recorded
          research state
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-event-trace
        - epistemic.md#epi-rte-proposal-evaluation
        note: Available offline transformation and consumer internals were not inspected. Their additional
          classifications cannot be enumerated from accepted records.
      records:
      - memory.md#mem-rte-evidence-retention
      - memory.md#mem-rte-retrieval-feedback
      - memory.md#mem-rte-cultural-inheritance
      - memory.md#mem-obj-event-trace
      - runtime.md#rt-rte-recorded-replay
      - runtime.md#rt-rte-model-planning
      - memory.md#mem-obj-research-state
      - memory.md#mem-rte-social-retention
      - runtime.md#rt-rte-program-install
      - runtime.md#rt-rte-direct-control
      - epistemic.md#epi-rte-proposal-evaluation
      note: Human control is local to explicit content-bearing decisions, not inherited by all writes
        in an interactive episode. Offline alternatives remain included and unresolved; positives do not
        establish a complete system union.
    curation_operations:
      assessment: partial
      units:
      - scope: Empirical and observation summary production over retained evidence
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id045
          - memory.md#mem-rte-context-selection
          - memory.md#mem-rte-evidence-retention
          note: Views select and compress retained cells, measurements and action history into bounded
            summaries.
        records: *id045
        note: Claims of semantic fidelity remain bounded; arbitrary clipping can discard a condition.
      - scope: Latest cells, feedback counters, skill indices and installed program replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id046
          - memory.md#mem-obj-empirical-knowledge
          - memory.md#mem-rte-retrieval-feedback
          - memory.md#mem-obj-program-skills
          - runtime.md#rt-rte-program-install
          note: Updates revise retained evidence/access entries or installed behavior while histories
            can remain.
        records: *id046
        note: A new research-state append alone is not classified as in-place evolution.
      - scope: Bounded deques, skill evidence tails and generation reset
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id047
          - memory.md#mem-obj-agent-memory
          - memory.md#mem-obj-program-skills
          - memory.md#mem-rte-cultural-inheritance
          note: Retention caps and reset forget private content or evidence tails.
        records: *id047
        note: Prompt omission alone does not delete retained memory.
      - scope: Reversible recorded prompt factoring
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records: &id048
          - memory.md#mem-obj-event-trace
          note: Repeated prompt text is stored as templates and replaced by markers expanded by the reader.
        records: *id048
        note: Reversible string factoring is not semantic synthesis; primary-key collision checks alone
          are not the warrant.
      - scope: Fulfilled request withdrawal from pending view
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records: &id049
          - memory.md#mem-obj-message-records
          - memory.md#mem-rte-social-retention
          note: Fulfillment stops current pending-request reliance for that recipient while ledger history
            remains.
        records: *id049
        note: This is operational withdrawal, not a truth-based retraction of a publication.
      - scope: Meaning-changing model research-state authorship
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-research-state
        - runtime.md#rt-rte-model-planning
        note: No actual output proposition establishes whether the update combines existing claims or
          synthesizes a new claim. Requested revision does not establish a controlled semantic curation
          value.
      - scope: Included offline analysis/dossier transformations and downstream consumers of recorded
          research state
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-event-trace
        - epistemic.md#epi-rte-proposal-evaluation
        note: Available offline transformation and consumer internals were not inspected. Their additional
          classifications cannot be enumerated from accepted records.
      records:
      - memory.md#mem-rte-context-selection
      - memory.md#mem-rte-evidence-retention
      - memory.md#mem-obj-empirical-knowledge
      - memory.md#mem-rte-retrieval-feedback
      - memory.md#mem-obj-program-skills
      - runtime.md#rt-rte-program-install
      - memory.md#mem-obj-agent-memory
      - memory.md#mem-rte-cultural-inheritance
      - memory.md#mem-obj-event-trace
      - memory.md#mem-obj-message-records
      - memory.md#mem-rte-social-retention
      - memory.md#mem-obj-research-state
      - runtime.md#rt-rte-model-planning
      - epistemic.md#epi-rte-proposal-evaluation
      note: Implemented transformations are classified independently of names such as verified and of
        indeterminate model output semantics. Offline alternatives remain included and unresolved; positives
        do not establish a complete system union.
    read_back_direction:
      assessment: partial
      units:
      - scope: Scheduled macroturn context selection and delivery
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id050
          - memory.md#mem-rte-context-selection
          note: Software automatically supplies selected retained material without a model-issued memory
            request.
        records: *id050
        note: This includes latest research state, private/public retrieval and empirical, spatial, skill
          and request views.
      - scope: Controller-requested teaching/resolution and recorded reconstruction
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id051
          - memory.md#mem-rte-social-retention
          - memory.md#mem-obj-program-library
          - runtime.md#rt-rte-recorded-replay
          note: Explicit source IDs or a requested trace select existing retained content for transfer,
            program resolution or replay.
        records: *id051
        note: Requested return is not counted again as push merely because code delivers it.
      - scope: Automatic request-result receipt and replacement inheritance
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id052
          - memory.md#mem-rte-social-retention
          - memory.md#mem-rte-cultural-inheritance
          note: Successful reply-linked actions and respawn triggers select retained result records or
            skills for a later recipient.
        records: *id052
        note: Receipt routing differs from the controller request to teach a named record.
      - scope: Included offline analysis/dossier transformations and downstream consumers of recorded
          research state
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-event-trace
        - epistemic.md#epi-rte-proposal-evaluation
        note: Available offline transformation and consumer internals were not inspected. Their additional
          classifications cannot be enumerated from accepted records.
      records:
      - memory.md#mem-rte-context-selection
      - memory.md#mem-rte-social-retention
      - memory.md#mem-obj-program-library
      - runtime.md#rt-rte-recorded-replay
      - memory.md#mem-rte-cultural-inheritance
      - memory.md#mem-obj-event-trace
      - epistemic.md#epi-rte-proposal-evaluation
      note: Request, automatic selection and later delivery are distinguished within each chain. Offline
        alternatives remain included and unresolved; positives do not establish a complete system union.
    read_back_signal:
      assessment: partial
      units:
      - scope: Macroturn private retrieval and compact archive selection
        assessment: known
        findings:
        - value: inferred-lexical
          basis: wired
          records: &id053
          - memory.md#mem-rte-context-selection
          note: Trigger is a scheduled macroturn; query uses prior state, pending requests and local observations
            for private evidence, or prior-state focus for compact archive text.
        records: *id053
        note: Scored retained text is the selected part; optional feedback modifies ranking.
      - scope: Latest state, ordinary archive, nearby insights, empirical summaries and context budget
          selection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id054
          - memory.md#mem-rte-context-selection
          - memory.md#mem-obj-deposited-insights
          - memory.md#mem-obj-empirical-knowledge
          note: Macroturn selectors use latest/recent availability, spatial proximity and budgets to supply
            bounded retained views.
        records: *id054
        note: These predicates are not an identity match merely because records have IDs.
      - scope: Program focus and recipient-specific pending requests
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id055
          - memory.md#mem-obj-program-skills
          - memory.md#mem-obj-message-records
          note: Macroturn selection matches prior-state focus program IDs and ledger recipient IDs to
            select delivered skills and pending content.
        records: *id055
        note: Program ranking also uses verified status and recency, a separate coarse selection input.
      - scope: Replacement skill selection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id056
          - memory.md#mem-rte-cultural-inheritance
          note: Respawn selects verified entries by measurement count, recency and cap for inherited knowledge.
        records: *id056
        note: Selection is not a content-understanding or embedding inference.
      - scope: Reply-result receipt routing
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id057
          - memory.md#mem-rte-social-retention
          - memory.md#mem-obj-message-records
          note: Successful action trigger uses a reply edge to select a retained request and its original
            sender, copying resolved result records.
        records: *id057
        note: This is an actual match controlling unsolicited delivery, not merely an identifier on a
          requested file.
      - scope: Included offline analysis/dossier transformations and downstream consumers of recorded
          research state
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-event-trace
        - epistemic.md#epi-rte-proposal-evaluation
        note: Available offline transformation and consumer internals were not inspected. Their additional
          classifications cannot be enumerated from accepted records.
      records:
      - memory.md#mem-rte-context-selection
      - memory.md#mem-obj-deposited-insights
      - memory.md#mem-obj-empirical-knowledge
      - memory.md#mem-obj-program-skills
      - memory.md#mem-obj-message-records
      - memory.md#mem-rte-cultural-inheritance
      - memory.md#mem-rte-social-retention
      - memory.md#mem-obj-event-trace
      - epistemic.md#epi-rte-proposal-evaluation
      note: Signals classify automatic push selection only; source-ID resolution on requested pull routes
        is not added as another identifier push. Offline alternatives remain included and unresolved;
        positives do not establish a complete system union.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatic model research-state continuation write
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id058
          - runtime.md#rt-rte-model-planning
          - memory.md#mem-obj-research-state
          - memory.md#mem-rte-context-selection
          note: Prior retained experience and observations feed admitted state retained in notebook; a
            later macroturn receives the latest state as context.
        records: *id058
        note: A generated continuation artifact qualifies without observed improvement or verified explanatory
          novelty.
      - scope: Citation/action feedback to durable selector metadata
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id059
          - memory.md#mem-rte-retrieval-feedback
          note: Automatic trace-fed counters persist and alter future adaptive evidence ranking.
        records: *id059
        note: This is a behavior-shaping access artifact, not a weight update.
      - scope: Empirical/experiment summaries and measured program indices
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id060
          - memory.md#mem-rte-evidence-retention
          - memory.md#mem-obj-research-mission
          - memory.md#mem-obj-program-skills
          - memory.md#mem-rte-cultural-inheritance
          note: Recorded sensing, tests and measurements yield retained summaries/indices consumed in
            later context, admission or inheritance.
        records: *id060
        note: Raw log retention alone is not an additional qualifying route.
      - scope: Included offline analysis/dossier transformations and downstream consumers of recorded
          research state
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-event-trace
        - epistemic.md#epi-rte-proposal-evaluation
        note: Available offline transformation and consumer internals were not inspected. Their additional
          classifications cannot be enumerated from accepted records.
      records:
      - runtime.md#rt-rte-model-planning
      - memory.md#mem-obj-research-state
      - memory.md#mem-rte-context-selection
      - memory.md#mem-rte-retrieval-feedback
      - memory.md#mem-rte-evidence-retention
      - memory.md#mem-obj-research-mission
      - memory.md#mem-obj-program-skills
      - memory.md#mem-rte-cultural-inheritance
      - memory.md#mem-obj-event-trace
      - epistemic.md#epi-rte-proposal-evaluation
      note: The axis tests automatic trace-fed durable artifacts and later consumers, independently of
        demonstrated learning benefit. No bounded system-wide negative is inferred from excluded provider
        weights. Offline alternatives remain included and unresolved; positives do not establish a complete
        system union.
    trace_source:
      assessment: partial
      units:
      - scope: Selection/citation/action-outcome feedback source
        assessment: known
        findings:
        - value: event-streams
          basis: wired
          records: &id061
          - memory.md#mem-rte-retrieval-feedback
          note: Discrete selection, citation and simulator action-outcome events feed retained ranking
            counters.
        records: *id061
        note: No tool API or conversational session-log origin is asserted merely from action serialization.
      - scope: Sensor observations, inspection and measured skill evidence source
        assessment: known
        findings:
        - value: event-streams
          basis: wired
          records: &id062
          - memory.md#mem-rte-evidence-retention
          - memory.md#mem-obj-program-skills
          note: Discrete environmental observations and measurement events feed summaries and knowledge
            indices.
        records: *id062
        note: Source follows simulator activity, not imported static scenario instructions.
      - scope: Experience-reuse recipe and measured outcome pairing
        assessment: known
        findings:
        - value: trajectories
          basis: wired
          records: &id063
          - memory.md#mem-obj-research-mission
          - epistemic.md#epi-rte-batch-measurement
          note: Retained recipe, fabrication/sample identity and measured test outcome link action/input
            to later result for future context.
        records: *id063
        note: This classification is local to the enabled experience-reuse path, not every stored isolated
          event.
      - scope: Research-state continuation source mixture
        assessment: partial
        findings:
        - value: event-streams
          basis: wired
          records: &id064
          - memory.md#mem-obj-research-state
          - memory.md#mem-rte-context-selection
          - runtime.md#rt-rte-model-planning
          note: Context supplies environmental observations and retained action/test evidence to the automatic
            continuation write.
        records: *id064
        note: The complete original provenance of model-authored prior prose and communicated records
          is not established; no exhaustive source union or session-log source is inferred from a fresh
          message pair.
      - scope: Included offline analysis/dossier transformations and downstream consumers of recorded
          research state
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-event-trace
        - epistemic.md#epi-rte-proposal-evaluation
        note: Available offline transformation and consumer internals were not inspected. Their additional
          classifications cannot be enumerated from accepted records.
      records:
      - memory.md#mem-rte-retrieval-feedback
      - memory.md#mem-rte-evidence-retention
      - memory.md#mem-obj-program-skills
      - memory.md#mem-obj-research-mission
      - epistemic.md#epi-rte-batch-measurement
      - memory.md#mem-obj-research-state
      - memory.md#mem-rte-context-selection
      - runtime.md#rt-rte-model-planning
      - memory.md#mem-obj-event-trace
      - epistemic.md#epi-rte-proposal-evaluation
      note: Trace origins are local to qualifying writes. Mixed original provenance and uninspected offline
        transformations prevent a complete source inventory. Offline alternatives remain included and
        unresolved; positives do not establish a complete system union.
---

# SwarmWorld memory profile

## Comparison rationale

The accepted records establish implementation wiring, not observed episodes or benefit. All positive findings therefore use `wired`. The ten axes remain partial because the reports leave offline transformation and downstream consumer internals uninspected; a whole-system frozen source boundary does not establish complete memory classification. See [MEM-OBJ-event-trace](memory.md#mem-obj-event-trace) and [EPI-RTE-proposal-evaluation](epistemic.md#epi-rte-proposal-evaluation). These unresolved alternatives are retained on every axis rather than silently excluded.

Reconciliation supersedes EPI-OBJ-empirical-knowledge with [MEM-OBJ-empirical-knowledge](memory.md#mem-obj-empirical-knowledge). The profile uses that canonical object. Other containers and intersecting routes remain distinct: private collections, research-state payload, registry instructions, executable programs and skill indices have different consumers. No other supersession changes a value.

Retained prose is knowledge at model-context consumption; its delivery is not proof of compliance. Numeric feedback is ranking input downstream and an automatic trace-fed behavior-shaping update. Resource/provenance and known-parent data supply both validation criteria and enforced vetoes. Installed instructions have executable force at the VM, separate from their descriptive use in model context. See [MEM-BAP-evidence-admission](memory.md#mem-bap-evidence-admission), [MEM-RTE-retrieval-feedback](memory.md#mem-rte-retrieval-feedback) and [RT-BAP-program-execution](runtime.md#rt-bap-program-execution).

Explicit human content-bearing actions support manual admission locally; starting an episode does not convert software sensing, model-state admission or feedback into manual writes. The ordinary software/model routes remain automatic. See [RT-RTE-direct-control](runtime.md#rt-rte-direct-control) and [MEM-RTE-social-retention](memory.md#mem-rte-social-retention).

The continuation-state route qualifies as trace learning because automatically generated state persists and reaches a later macroturn, not because a hypothesis field proves novelty or improvement. State-update semantics remain indeterminate for curation. Empirical summaries consolidate; eviction forgets; feedback revises access metadata. Reversible prompt factoring deduplicates strings without certifying semantic synthesis. Request fulfillment withdraws pending status without deleting ledger history. See [MEM-OBJ-research-state](memory.md#mem-obj-research-state), [MEM-OBJ-event-trace](memory.md#mem-obj-event-trace) and [MEM-OBJ-message-records](memory.md#mem-obj-message-records).

Scheduled context is push even though internal code calls retrieval. Requested record resolution, teaching and trace replay are pull operations. Identifier push requires actual focus/recipient/reply matching; identifiers on requested content alone do not qualify. Trimming changes delivered context, not authoritative store retention. See [MEM-RTE-context-selection](memory.md#mem-rte-context-selection) and [MEM-RTE-social-retention](memory.md#mem-rte-social-retention).

Trace sources follow original content. Simulator activity supports event streams; linked recipe/sample/test experience supports trajectories on its enabled route. A fresh provider message pair does not alone establish retained conversational session logs, nor do simulator actions alone establish tool traces. Unknown original origins of prior prose prevent a complete research-state source union. Replay restores committed research records, not all adaptive selector evolution; recorded digest agreement would not establish complete adaptive continuation. See [RT-RTE-recorded-replay](runtime.md#rt-rte-recorded-replay), [MEM-OBJ-research-mission](memory.md#mem-obj-research-mission) and [MEM-RTE-retrieval-feedback](memory.md#mem-rte-retrieval-feedback).

Source-read log: none. Classification used only supplied accepted records and their annotations; no source ambiguity required an additional frozen-source read.
