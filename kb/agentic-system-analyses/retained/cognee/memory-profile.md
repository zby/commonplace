---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Cognee memory comparison: graph knowledge, session guidance, trace-fed ranking and skill
  revision, with partial alternative-route coverage.'
run-id: AAS-2026-10-14-cognee-d8839fe03c5b-01
source-identity: https://github.com/topoteretes/cognee
reviewed-boundary: f154b32a9e544dac73e7ddf2010327cf9988edcd
memory-comparison:
  version: 2
  scope: Accumulated raw corpus and relational/provenance records; graph content/structure, vector access
    representations, session QA/traces/feedback/guidance and cache alternatives; session learning documents,
    ranking/preferences/truth state, global summaries, skills/metadata/runs/proposals; their admission,
    maintenance, withdrawal and later answer/update routes. Includes recorded unresolved typed, cache,
    extraction/index, concurrent, custom and alternate recall/interface paths. Excludes static shipped
    instructions, current-turn/ContextVar frames, external model weights/provider internals and arbitrary
    enclosing-host behavior. The source artifact is complete but its memory-use loop is only partially
    traced.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Retained raw ingestion files
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-rte-memory-withdrawal
          note: Memory-only forget preserves raw files for rebuilding; loaders and file lifecycle are
            not fully traced.
        records: *id001
        note: Memory-only forget preserves raw files for rebuilding; loaders and file lifecycle are not
          fully traced.
      - scope: Retained relational data records and conditional provenance ledger
        assessment: known
        findings:
        - value: rdbms
          basis: wired
          records: &id002
          - memory.md#mem-obj-graph-structure
          - memory.md#mem-rte-memory-withdrawal
          note: Relational data records survive memory-only forget; provenance ledger is a conditional
            alternative to graph-folded provenance.
        records: *id002
        note: Relational data records survive memory-only forget; provenance ledger is a conditional alternative
          to graph-folded provenance.
      - scope: Graph content text
        assessment: known
        findings:
        - value: graph
          basis: wired
          records: &id003
          - memory.md#mem-obj-graph-content
          note: DataPoint text is written to configured graph storage.
        records: *id003
        note: DataPoint text is written to configured graph storage.
      - scope: Graph IDs, edges and graph-folded provenance
        assessment: known
        findings:
        - value: graph
          basis: wired
          records: &id004
          - memory.md#mem-obj-graph-structure
          note: Symbolic graph structure is retained; ledger-backed provenance is classified separately.
        records: *id004
        note: Symbolic graph structure is retained; ledger-backed provenance is classified separately.
      - scope: Session-learning graph representations
        assessment: known
        findings:
        - value: graph
          basis: wired
          records: &id005
          - memory.md#mem-obj-session-learning
          note: Published learning documents are cognified into retained graph content.
        records: *id005
        note: Published learning documents are cognified into retained graph content.
      - scope: Global feedback weights
        assessment: known
        findings:
        - value: graph
          basis: wired
          records: &id006
          - memory.md#mem-obj-feedback-weight
          note: Numerical feedback weights are graph attributes; cache bookkeeping is a separate part.
        records: *id006
        note: Numerical feedback weights are graph attributes; cache bookkeeping is a separate part.
      - scope: Personal preference edges and preference text
        assessment: known
        findings:
        - value: graph
          basis: wired
          records: &id007
          - memory.md#mem-obj-preference-state
          - memory.md#mem-obj-preference-text
          note: Both preference tracks retain state on the user/dataset graph.
        records: *id007
        note: Both preference tracks retain state on the user/dataset graph.
      - scope: Truth-alignment per-chunk state
        assessment: known
        findings:
        - value: graph
          basis: wired
          records: &id008
          - memory.md#mem-obj-truth-state
          note: Per-chunk coordinates and epochs are graph properties, not provider weights.
        records: *id008
        note: Per-chunk coordinates and epochs are graph properties, not provider weights.
      - scope: Global summary text and hierarchy
        assessment: known
        findings:
        - value: graph
          basis: wired
          records: &id009
          - memory.md#mem-obj-global-context-summary
          note: Summary DataPoints and summarized_in edges are graph state.
        records: *id009
        note: Summary DataPoints and summarized_in edges are graph state.
      - scope: Skill procedures and metadata
        assessment: known
        findings:
        - value: graph
          basis: wired
          records: &id010
          - memory.md#mem-obj-skill-procedure
          - memory.md#mem-obj-skill-metadata
          note: Deployed procedures and scope/discovery fields are graph Skill parts.
        records: *id010
        note: Deployed procedures and scope/discovery fields are graph Skill parts.
      - scope: SkillRun summaries
        assessment: known
        findings:
        - value: graph
          basis: wired
          records: &id011
          - memory.md#mem-obj-skill-run
          note: Run summaries are graph DataPoints.
        records: *id011
        note: Run summaries are graph DataPoints.
      - scope: Skill improvement proposals
        assessment: known
        findings:
        - value: graph
          basis: wired
          records: &id012
          - runtime.md#rt-obj-skill-proposal
          note: Old/proposed procedures, rationale and status are retained as graph DataPoints.
        records: *id012
        note: Old/proposed procedures, rationale and status are retained as graph DataPoints.
      - scope: Retrieval vectors, payload projections and indexed text copies
        assessment: known
        findings:
        - value: vector
          basis: wired
          records: &id013
          - memory.md#mem-obj-vector-index
          - memory.md#mem-obj-graph-content
          - memory.md#mem-obj-global-context-summary
          - memory.md#mem-obj-skill-metadata
          note: Vector collections retain embeddings and projected payloads; encoding and provenance are
            separate axes.
        records: *id013
        note: Vector collections retain embeddings and projected payloads; encoding and provenance are
          separate axes.
      - scope: Truth centroid slots
        assessment: known
        findings:
        - value: vector
          basis: wired
          records: *id008
          note: Learning-derived centroids are retained by the vector engine.
        records: *id008
        note: Learning-derived centroids are retained by the vector engine.
      - scope: 'Session QA, traces, feedback, active guidance and update bookkeeping: cache alternatives'
        assessment: partial
        findings:
        - value: files
          basis: afforded
          records: &id014
          - memory.md#mem-obj-session-qa
          note: FS cache is offered by the factory; selected deletion bodies were inspected, not the whole
            storage contract.
        - value: rdbms
          basis: afforded
          records: *id014
          note: SQL cache is a factory alternative; adapter bodies were not audited.
        - value: kv
          basis: afforded
          records: *id014
          note: Redis cache is a factory alternative; adapter bodies were not audited.
        records:
        - memory.md#mem-obj-session-qa
        - memory.md#mem-obj-session-agent-trace
        - memory.md#mem-obj-session-feedback
        - memory.md#mem-obj-session-context
        - memory.md#mem-obj-feedback-weight
        - memory.md#mem-obj-preference-state
        note: The cache factory offers FS, SQL and Redis alternatives. These are afforded substrates,
          not audited backend semantics; Tapes storage is unresolved.
      - scope: Tapes cache backing retained session parts
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-qa
        - memory.md#mem-rte-memory-withdrawal
        note: An append-only Tapes alternative is recorded, but its backing substrate is not established
          by accepted records.
      - scope: Alternate raw loaders, code/tool lane objects, custom pipelines and storage adapters
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-permanent-memory
        - runtime.md#rt-rte-recall-dispatch
        note: Accepted route limits leave these included retained parts untraced; no complete substrate
          inventory follows.
      records:
      - memory.md#mem-rte-memory-withdrawal
      - memory.md#mem-obj-graph-structure
      - memory.md#mem-obj-graph-content
      - memory.md#mem-obj-session-learning
      - memory.md#mem-obj-feedback-weight
      - memory.md#mem-obj-preference-state
      - memory.md#mem-obj-preference-text
      - memory.md#mem-obj-truth-state
      - memory.md#mem-obj-global-context-summary
      - memory.md#mem-obj-skill-procedure
      - memory.md#mem-obj-skill-metadata
      - memory.md#mem-obj-skill-run
      - runtime.md#rt-obj-skill-proposal
      - memory.md#mem-obj-vector-index
      - memory.md#mem-obj-session-qa
      - memory.md#mem-obj-session-agent-trace
      - memory.md#mem-obj-session-feedback
      - memory.md#mem-obj-session-context
      - runtime.md#rt-rte-permanent-memory
      - runtime.md#rt-rte-recall-dispatch
      note: Graph, vector, raw-file and relational witnesses coexist with partially inspected cache alternatives
        and untraced retained parts. No external provider weight store is included merely because inference
        uses it.
    representational_form:
      assessment: partial
      units:
      - scope: Graph content at answer and summarization consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: *id003
          note: Readable chunk/entity/summary text supplies interpreted content.
        records: *id003
        note: Readable chunk/entity/summary text supplies interpreted content.
      - scope: Session question/answer fields and feedback prose
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id015
          - memory.md#mem-obj-session-qa
          - memory.md#mem-obj-session-feedback
          note: Conversation and follow-up text are interpreted by completion and maintenance models.
        records: *id015
        note: Conversation and follow-up text are interpreted by completion and maintenance models.
      - scope: Sanitized trace display/feedback text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id016
          - memory.md#mem-obj-session-agent-trace
          note: Rendered trace material supplies interpreted context; this does not classify every original
            host object.
        records: *id016
        note: Rendered trace material supplies interpreted context; this does not classify every original
          host object.
      - scope: Active guidance, preference lines and session learning statements/reasons
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id017
          - memory.md#mem-obj-session-context
          - memory.md#mem-obj-preference-text
          - memory.md#mem-obj-session-learning
          note: These text parts are interpreted guidance or knowledge at later consumers.
        records: *id017
        note: These text parts are interpreted guidance or knowledge at later consumers.
      - scope: Global hierarchy summary text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: *id009
          note: Root and bucket prose is interpreted answer context.
        records: *id009
        note: Root and bucket prose is interpreted answer context.
      - scope: Skill procedure and discovery description
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id018
          - memory.md#mem-obj-skill-procedure
          - memory.md#mem-obj-skill-metadata
          note: Procedure and description influence model interpretation; scope fields are separate.
        records: *id018
        note: Procedure and description influence model interpretation; scope fields are separate.
      - scope: SkillRun task/result text and skill proposal procedure/rationale
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id019
          - memory.md#mem-obj-skill-run
          - runtime.md#rt-obj-skill-proposal
          note: Run summaries and proposed/recovery procedure prose are natural-language parts.
        records: *id019
        note: Run summaries and proposed/recovery procedure prose are natural-language parts.
      - scope: Graph identifiers, relationships and provenance
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: *id004
          note: Localized IDs and edges have fixed traversal, scope and deletion consumers.
        records: *id004
        note: Localized IDs and edges have fixed traversal, scope and deletion consumers.
      - scope: Session references, timestamps, counters, profiles and watermarks
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id020
          - memory.md#mem-obj-session-qa
          - memory.md#mem-obj-session-agent-trace
          - memory.md#mem-obj-session-feedback
          - memory.md#mem-obj-session-context
          note: Fixed code interprets localized selection/admission and dependency fields.
        records: *id020
        note: Fixed code interprets localized selection/admission and dependency fields.
      - scope: Feedback and personal preference scalar parameters
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id021
          - memory.md#mem-obj-feedback-weight
          - memory.md#mem-obj-preference-state
          note: Localized scalar ranking parameters are symbolic, not distributed-parametric geometry.
        records: *id021
        note: Localized scalar ranking parameters are symbolic, not distributed-parametric geometry.
      - scope: Truth validity epochs and learning IDs
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: *id008
          note: Epochs and IDs are fixed-rule validity metadata, separate from dense coordinates.
        records: *id008
        note: Epochs and IDs are fixed-rule validity metadata, separate from dense coordinates.
      - scope: Global summary levels, dataset IDs and hierarchy links
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: *id009
          note: Fixed rules identify roots, datasets and parent/child relations.
        records: *id009
        note: Fixed rules identify roots, datasets and parent/child relations.
      - scope: Skill scope, active flags, declared tools and run/proposal identity/status fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id022
          - memory.md#mem-obj-skill-metadata
          - memory.md#mem-obj-skill-run
          - runtime.md#rt-obj-skill-proposal
          note: Code uses localized fields for filtering, evidence selection and application.
        records: *id022
        note: Code uses localized fields for filtering, evidence selection and application.
      - scope: Dense retrieval vectors
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: &id023
          - memory.md#mem-obj-vector-index
          note: Dense representations distribute numerical state across coordinates; they are not embedding-provider
            parameters.
        records: *id023
        note: Dense representations distribute numerical state across coordinates; they are not embedding-provider
          parameters.
      - scope: Truth centroids and chunk alignment geometry
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: *id008
          note: Embedding-derived geometry is distributed numerical material; epochs are classified separately.
        records: *id008
        note: Embedding-derived geometry is distributed numerical material; epochs are classified separately.
      - scope: Original arbitrary typed/host trace payloads and untraced code/tool/alternate retrieval
          parts
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-agent-trace
        - memory.md#mem-rte-typed-admission
        - runtime.md#rt-rte-recall-dispatch
        note: Display sanitization does not establish complete encoding of mixed originating material;
          alternate operative parts are untraced.
      records:
      - memory.md#mem-obj-graph-content
      - memory.md#mem-obj-session-qa
      - memory.md#mem-obj-session-feedback
      - memory.md#mem-obj-session-agent-trace
      - memory.md#mem-obj-session-context
      - memory.md#mem-obj-preference-text
      - memory.md#mem-obj-session-learning
      - memory.md#mem-obj-global-context-summary
      - memory.md#mem-obj-skill-procedure
      - memory.md#mem-obj-skill-metadata
      - memory.md#mem-obj-skill-run
      - runtime.md#rt-obj-skill-proposal
      - memory.md#mem-obj-graph-structure
      - memory.md#mem-obj-feedback-weight
      - memory.md#mem-obj-preference-state
      - memory.md#mem-obj-truth-state
      - memory.md#mem-obj-vector-index
      - memory.md#mem-rte-typed-admission
      - runtime.md#rt-rte-recall-dispatch
      note: Text, localized symbolic state and dense numerical representations are all supported. Raw-host
        and alternate-lane coverage prevents a complete form inventory; static prompt files and inference
        weights are excluded.
    lineage:
      assessment: partial
      units:
      - scope: Raw corpus acquisition and ingested SKILL.md procedure bodies
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id024
          - runtime.md#rt-rte-permanent-memory
          - memory.md#mem-obj-skill-procedure
          note: Content is acquired from caller/source files. Original author identity and human admission
            are unresolved.
        records: *id024
        note: Content is acquired from caller/source files. Original author identity and human admission
          are unresolved.
      - scope: Graph chunk/extraction/summary products
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id025
          - runtime.md#rt-rte-permanent-memory
          - memory.md#mem-obj-graph-content
          note: The standard assembly transforms acquired input into retained graph products; exact source
            fidelity is unestablished.
        records: *id025
        note: The standard assembly transforms acquired input into retained graph products; exact source
          fidelity is unestablished.
      - scope: Symbolic graph/provenance structure
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: *id004
          note: Storage code constructs IDs, relations and conditional provenance from processing context.
        records: *id004
        note: Storage code constructs IDs, relations and conditional provenance from processing context.
      - scope: Retrieval index derivation from retained fields
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records: *id023
          note: Embedding/index processing derives numerical access material. Immutable per-entry embedding
            provenance is missing.
        records: *id023
        note: Embedding/index processing derives numerical access material. Immutable per-entry embedding
          provenance is missing.
      - scope: Generated conversation records and captured decorated outcomes
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id026
          - memory.md#mem-obj-session-qa
          - memory.md#mem-obj-session-agent-trace
          - runtime.md#rt-rte-decorated-agent
          note: Shipped answer/host routes record activity for later consumers; typed alternatives have
            separate unresolved origin.
        records: *id026
        note: Shipped answer/host routes record activity for later consumers; typed alternatives have
          separate unresolved origin.
      - scope: Session feedback interpretation and active guidance
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id027
          - memory.md#mem-obj-session-feedback
          - memory.md#mem-obj-session-context
          - memory.md#mem-rte-session-guidance
          - memory.md#mem-rte-trace-promotion
          note: Turn/trace records feed model interpretation or deterministic error restatement into retained
            guidance.
        records: *id027
        note: Turn/trace records feed model interpretation or deterministic error restatement into retained
          guidance.
      - scope: Distilled session-learning documents
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id028
          - memory.md#mem-obj-session-learning
          - memory.md#mem-rte-session-distillation
          note: QA timelines and derived context feed curator/writer publication; preserved reasons do
            not authenticate source truth.
        records: *id028
        note: QA timelines and derived context feed curator/writer publication; preserved reasons do not
          authenticate source truth.
      - scope: Feedback weights, preference edges and preference text
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id029
          - memory.md#mem-obj-feedback-weight
          - memory.md#mem-obj-preference-state
          - memory.md#mem-obj-preference-text
          - memory.md#mem-rte-ranking-maintenance
          note: Recorded turn feedback, used IDs and context lines drive retained numerical/text updates.
        records: *id029
        note: Recorded turn feedback, used IDs and context lines drive retained numerical/text updates.
      - scope: Truth geometry from retained learning text
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records: &id030
          - memory.md#mem-obj-truth-state
          - memory.md#mem-rte-truth-maintenance
          note: Embedding and projection derive numerical state from accepted lesson text; immutable embedding
            basis is unresolved.
        records: *id030
        note: Embedding and projection derive numerical state from accepted lesson text; immutable embedding
          basis is unresolved.
      - scope: Global summaries from retained child summaries
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records: &id031
          - memory.md#mem-obj-global-context-summary
          - memory.md#mem-rte-summary-readback
          note: Model compression builds hierarchy text from child text; initial leaf derivation and all
            rebuild alternatives are untraced.
        records: *id031
        note: Model compression builds hierarchy text from child text; initial leaf derivation and all
          rebuild alternatives are untraced.
      - scope: Shipped SkillRun recorder output
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: *id011
          note: Opened-skill tool activity and result summaries produce retained run evidence.
        records: *id011
        note: Opened-skill tool activity and result summaries produce retained run evidence.
      - scope: Automatically drafted skill proposals
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id032
          - runtime.md#rt-obj-skill-proposal
          - runtime.md#rt-rte-skill-revision
          note: Selected failing/low-score run summaries and current procedure feed retained replacement
            proposals.
        records: *id032
        note: Selected failing/low-score run summaries and current procedure feed retained replacement
          proposals.
      - scope: Applied replacement procedure derivation
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id033
          - memory.md#mem-obj-skill-procedure
          - runtime.md#rt-rte-skill-revision
          note: A selected proposal overwrites procedure text; apply control is unresolved but the derivation
            path is implemented.
        records: *id033
        note: A selected proposal overwrites procedure text; apply control is unresolved but the derivation
          path is implemented.
      - scope: Initial corpus/skill authorship, typed records and graph-written skill/tool metadata
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-permanent-memory
        - memory.md#mem-obj-skill-procedure
        - memory.md#mem-obj-skill-metadata
        - memory.md#mem-rte-typed-admission
        - memory.md#mem-obj-session-agent-trace
        - memory.md#mem-obj-skill-run
        note: Generic caller and publisher labels do not resolve authored versus imported versus trace
          origin for every admitted part.
      - scope: Alternate extractors, code indexing and provider/index provenance
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-permanent-memory
        - runtime.md#rt-rte-recall-dispatch
        - memory.md#mem-obj-vector-index
        note: Known compilation paths do not resolve the uninspected alternatives or immutable embedding
          provenance.
      records:
      - runtime.md#rt-rte-permanent-memory
      - memory.md#mem-obj-skill-procedure
      - memory.md#mem-obj-graph-content
      - memory.md#mem-obj-graph-structure
      - memory.md#mem-obj-vector-index
      - memory.md#mem-obj-session-qa
      - memory.md#mem-obj-session-agent-trace
      - runtime.md#rt-rte-decorated-agent
      - memory.md#mem-obj-session-feedback
      - memory.md#mem-obj-session-context
      - memory.md#mem-rte-session-guidance
      - memory.md#mem-rte-trace-promotion
      - memory.md#mem-obj-session-learning
      - memory.md#mem-rte-session-distillation
      - memory.md#mem-obj-feedback-weight
      - memory.md#mem-obj-preference-state
      - memory.md#mem-obj-preference-text
      - memory.md#mem-rte-ranking-maintenance
      - memory.md#mem-obj-truth-state
      - memory.md#mem-rte-truth-maintenance
      - memory.md#mem-obj-global-context-summary
      - memory.md#mem-rte-summary-readback
      - memory.md#mem-obj-skill-run
      - runtime.md#rt-obj-skill-proposal
      - runtime.md#rt-rte-skill-revision
      - memory.md#mem-obj-skill-metadata
      - memory.md#mem-rte-typed-admission
      - runtime.md#rt-rte-recall-dispatch
      note: Imported acquisition, compiled access material and trace-derived updates are distinct paths.
        No authored finding is inferred from caller identity, and known embedding derivation does not
        close provenance gaps.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Graph content, QA history, trace display and summaries at answer/context consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id034
          - memory.md#mem-obj-graph-content
          - memory.md#mem-obj-session-qa
          - memory.md#mem-obj-session-agent-trace
          - memory.md#mem-obj-global-context-summary
          - runtime.md#rt-rte-decorated-agent
          - memory.md#mem-rte-summary-readback
          note: Readable retained content supplies reference/context to answering models or callers, not
            enforced factual truth.
        records: *id034
        note: Readable retained content supplies reference/context to answering models or callers, not
          enforced factual truth.
      - scope: Active guidance and durable preference text at completion consumers
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id035
          - memory.md#mem-obj-session-context
          - memory.md#mem-obj-preference-text
          - memory.md#mem-rte-session-guidance
          note: Retained preference and working guidance supply standing directions in the guidance block;
            delivery is not obedience.
        records: *id035
        note: Retained preference and working guidance supply standing directions in the guidance block;
          delivery is not obedience.
      - scope: Loaded skill procedure at subsequent AgentStep consumer
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id036
          - memory.md#mem-obj-skill-procedure
          - runtime.md#rt-bap-skill-guidance
          - workflow.md#wf-rte-skill-loading
          note: Requested retained procedure arrives as a capped tool result and is interpreted as operational
            guidance.
        records: *id036
        note: Requested retained procedure arrives as a capped tool result and is interpreted as operational
          guidance.
      - scope: Run summaries, QA/trace evidence and feedback at durable update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id037
          - memory.md#mem-obj-skill-run
          - runtime.md#rt-rte-skill-revision
          - memory.md#mem-rte-trace-promotion
          - memory.md#mem-rte-session-guidance
          - memory.md#mem-rte-session-distillation
          - memory.md#mem-rte-ranking-maintenance
          note: Retained experience feeds procedure proposals, guidance/lesson creation and persistent
            ranking updates; no capacity improvement is implied.
        records: *id037
        note: Retained experience feeds procedure proposals, guidance/lesson creation and persistent ranking
          updates; no capacity improvement is implied.
      - scope: Indexed retained content and numerical access representations at similarity selection
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id038
          - memory.md#mem-obj-vector-index
          - memory.md#mem-obj-skill-metadata
          - memory.md#mem-obj-global-context-summary
          note: Retained text/index features influence relative retrieval priority even without a learned
            ranking policy.
        records: *id038
        note: Retained text/index features influence relative retrieval priority even without a learned
          ranking policy.
      - scope: Retained guidance content/counters and feedback/preference/truth state at rankers
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id039
          - memory.md#mem-obj-session-context
          - memory.md#mem-rte-session-guidance
          - memory.md#mem-obj-feedback-weight
          - memory.md#mem-obj-preference-state
          - memory.md#mem-obj-truth-state
          - memory.md#mem-bap-ranking-state
          note: Query overlap, helpfulness and scalar/geometry adjustments change relative selection when
            enabled.
        records: *id039
        note: Query overlap, helpfulness and scalar/geometry adjustments change relative selection when
          enabled.
      - scope: Persist/extraction/distillation/preference watermarks and dependency identities
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id040
          - memory.md#mem-obj-session-qa
          - memory.md#mem-rte-trace-promotion
          - memory.md#mem-rte-session-distillation
          - memory.md#mem-obj-preference-text
          - epistemic.md#epi-rte-distillation-recovery
          note: Retained progress markers select input windows or retry work; graph/dependency IDs select
            traversal and cleanup targets.
        records: *id040
        note: Retained progress markers select input windows or retry work; graph/dependency IDs select
          traversal and cleanup targets.
      - scope: Skill active/scope/tool declarations at availability/dispatch consumers
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records: &id041
          - memory.md#mem-obj-skill-metadata
          - runtime.md#rt-rte-agentic-tools
          note: Retained scope/active/tool fields exclude candidates and narrow permissible dispatch;
            they do not sandbox handler effects.
        records: *id041
        note: Retained scope/active/tool fields exclude candidates and narrow permissible dispatch; they
          do not sandbox handler effects.
      - scope: Skill scope and truth epoch metadata at admissibility guards
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id042
          - memory.md#mem-obj-skill-metadata
          - memory.md#mem-obj-truth-state
          - memory.md#mem-rte-truth-maintenance
          note: Retained scope and epoch state determine whether a candidate skill or alignment may be
            used; equality does not prove a correct basis.
        records: *id042
        note: Retained scope and epoch state determine whether a candidate skill or alignment may be used;
          equality does not prove a correct basis.
      - scope: Truth epoch state at conditional ranker veto
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records: &id043
          - memory.md#mem-obj-truth-state
          - memory.md#mem-rte-truth-maintenance
          note: Mismatched retained epochs prevent coordinate weighting on the inspected consumer path.
        records: *id043
        note: Mismatched retained epochs prevent coordinate weighting on the inspected consumer path.
      - scope: Retained conflict warning/supersession metadata at later readers
        assessment: uninspected
        findings: []
        records:
        - epistemic.md#epi-rte-contradiction-annotation
        - epistemic.md#epi-rte-temporal-supersession
        note: Metadata writes are inspected, but later conflict/supersession consumers and their actual
          force are not. Do not infer enforced withdrawal from a superseded flag.
      - scope: Proposal rationale review and alternate recall/host effects
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-skill-proposal
        - runtime.md#rt-rte-recall-dispatch
        - runtime.md#rt-rte-decorated-agent
        note: Review is afforded; rationale use, every lane consumer and unrelated host-provider effects
          are unresolved.
      records:
      - memory.md#mem-obj-graph-content
      - memory.md#mem-obj-session-qa
      - memory.md#mem-obj-session-agent-trace
      - memory.md#mem-obj-global-context-summary
      - runtime.md#rt-rte-decorated-agent
      - memory.md#mem-rte-summary-readback
      - memory.md#mem-obj-session-context
      - memory.md#mem-obj-preference-text
      - memory.md#mem-rte-session-guidance
      - memory.md#mem-obj-skill-procedure
      - runtime.md#rt-bap-skill-guidance
      - workflow.md#wf-rte-skill-loading
      - memory.md#mem-obj-skill-run
      - runtime.md#rt-rte-skill-revision
      - memory.md#mem-rte-trace-promotion
      - memory.md#mem-rte-session-distillation
      - memory.md#mem-rte-ranking-maintenance
      - memory.md#mem-obj-vector-index
      - memory.md#mem-obj-skill-metadata
      - memory.md#mem-obj-feedback-weight
      - memory.md#mem-obj-preference-state
      - memory.md#mem-obj-truth-state
      - memory.md#mem-bap-ranking-state
      - epistemic.md#epi-rte-distillation-recovery
      - runtime.md#rt-rte-agentic-tools
      - memory.md#mem-rte-truth-maintenance
      - epistemic.md#epi-rte-contradiction-annotation
      - epistemic.md#epi-rte-temporal-supersession
      - runtime.md#rt-obj-skill-proposal
      - runtime.md#rt-rte-recall-dispatch
      note: Knowledge, instruction, learning, ranking, routing, validation and enforcement have local
        consumer warrants. Unconsumed metadata is not granted authority; opaque or untraced consumers
        prevent complete coverage.
    write_agency:
      assessment: partial
      units:
      - scope: Cognify extraction/storage admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id044
          - runtime.md#rt-rte-permanent-memory
          note: After workflow start, software/model output enters storage without per-item human approval.
        records: *id044
        note: After workflow start, software/model output enters storage without per-item human approval.
      - scope: Session-turn candidate/feedback/counter admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id045
          - memory.md#mem-rte-session-guidance
          note: Model proposals and deterministic shape/confidence/dedup gates decide writes.
        records: *id045
        note: Model proposals and deterministic shape/confidence/dedup gates decide writes.
      - scope: Decorated outcome and shipped SkillRun capture
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id046
          - runtime.md#rt-rte-decorated-agent
          - memory.md#mem-obj-skill-run
          note: Software records enabled host/tool outcomes; invoking a host function is not content approval.
        records: *id046
        note: Software records enabled host/tool outcomes; invoking a host function is not content approval.
      - scope: Trace promotion and lesson publication
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id047
          - memory.md#mem-rte-trace-promotion
          - memory.md#mem-rte-session-distillation
          note: Software/model windows and writer judgment admit derived memory without per-window/per-lesson
            human review.
        records: *id047
        note: Software/model windows and writer judgment admit derived memory without per-window/per-lesson
          human review.
      - scope: Feedback/preference/truth/summary maintenance writes
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id048
          - memory.md#mem-rte-ranking-maintenance
          - memory.md#mem-rte-truth-maintenance
          - memory.md#mem-rte-summary-readback
          note: Arithmetic, gates, embedding projection and model summarization admit subsequent state.
        records: *id048
        note: Arithmetic, gates, embedding projection and model summarization admit subsequent state.
      - scope: Typed/schema-controlled storage and skill-ingester stamping
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id049
          - memory.md#mem-rte-typed-admission
          - memory.md#mem-obj-skill-procedure
          - memory.md#mem-obj-skill-metadata
          note: Software supplies schema/access checks and stamps fields; this finding concerns computational
            admission, not proof of human content selection.
        records: *id049
        note: Software supplies schema/access checks and stamps fields; this finding concerns computational
          admission, not proof of human content selection.
      - scope: Skill replacement proposal construction
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id050
          - runtime.md#rt-obj-skill-proposal
          - runtime.md#rt-rte-skill-revision
          note: Opt-in starts drafting, but a model constructs and software stores the proposal.
        records: *id050
        note: Opt-in starts drafting, but a model constructs and software stores the proposal.
      - scope: Initial raw/skill supply, explicit feedback/editing and caller-selected proposal apply
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-permanent-memory
        - memory.md#mem-rte-typed-admission
        - memory.md#mem-obj-skill-procedure
        - runtime.md#rt-rte-skill-revision
        note: Caller can supply, edit, withhold or request apply, but human versus computational principal
          is unresolved; neither manual nor automatic caller choice is established.
      - scope: Alternative direct graph/custom pipeline/interface write controls
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-permanent-memory
        - runtime.md#rt-rte-recall-dispatch
        - memory.md#mem-rte-typed-admission
        note: Uninspected write alternatives prevent complete admission-control classification.
      records:
      - runtime.md#rt-rte-permanent-memory
      - memory.md#mem-rte-session-guidance
      - runtime.md#rt-rte-decorated-agent
      - memory.md#mem-obj-skill-run
      - memory.md#mem-rte-trace-promotion
      - memory.md#mem-rte-session-distillation
      - memory.md#mem-rte-ranking-maintenance
      - memory.md#mem-rte-truth-maintenance
      - memory.md#mem-rte-summary-readback
      - memory.md#mem-rte-typed-admission
      - memory.md#mem-obj-skill-procedure
      - memory.md#mem-obj-skill-metadata
      - runtime.md#rt-obj-skill-proposal
      - runtime.md#rt-rte-skill-revision
      - runtime.md#rt-rte-recall-dispatch
      note: Automatic internal admission is supported independently of unresolved initial/caller decisions.
        No manual finding is licensed solely by an explicit API call, workflow start or apply request.
    curation_operations:
      assessment: partial
      units:
      - scope: Normalized guidance-content duplicate admission
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records: &id051
          - memory.md#mem-obj-session-context
          - memory.md#mem-rte-session-guidance
          note: Existing profile/section/content matches reuse entries and receive source links rather
            than duplicate content.
        records: *id051
        note: Existing profile/section/content matches reuse entries and receive source links rather than
          duplicate content.
      - scope: Storage extraction/index deduplication
        assessment: partial
        findings:
        - value: dedup
          basis: afforded
          records: &id052
          - memory.md#mem-obj-graph-content
          - runtime.md#rt-rte-permanent-memory
          note: The recorded storage entry describes deduplicating graph content before indexing; detailed
            index and every extractor alternative remain untraced.
        records: *id052
        note: The recorded storage entry describes deduplicating graph content before indexing; detailed
          index and every extractor alternative remain untraced.
      - scope: Trace-to-standing-guidance extraction
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id053
          - memory.md#mem-rte-trace-promotion
          - memory.md#mem-obj-session-context
          note: Bounded trace batches produce at most five standing lessons; deterministic live errors
            are restatements, not new causal diagnoses.
        records: *id053
        note: Bounded trace batches produce at most five standing lessons; deterministic live errors are
          restatements, not new causal diagnoses.
      - scope: Global summary hierarchy compression
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id054
          - memory.md#mem-obj-global-context-summary
          - memory.md#mem-rte-summary-readback
          note: Child summary text is compressed into bucket/root representations, not a demonstrated
            new proposition.
        records: *id054
        note: Child summary text is compressed into bucket/root representations, not a demonstrated new
          proposition.
      - scope: Caller-applied skill procedure replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id055
          - runtime.md#rt-rte-skill-revision
          - memory.md#mem-obj-skill-procedure
          note: Apply overwrites an existing procedure/search text and marks proposal applied; absence
            of performance testing does not negate revision wiring.
        records: *id055
        note: Apply overwrites an existing procedure/search text and marks proposal applied; absence of
          performance testing does not negate revision wiring.
      - scope: Session-to-graph publication
        assessment: known
        findings:
        - value: promote
          basis: wired
          records: &id056
          - memory.md#mem-rte-trace-promotion
          - memory.md#mem-obj-session-learning
          - memory.md#mem-rte-session-distillation
          note: Cached conversation/trace/context-derived material is admitted to persistent graph retrieval
            tiers; this is not factual endorsement by storage.
        records: *id056
        note: Cached conversation/trace/context-derived material is admitted to persistent graph retrieval
          tiers; this is not factual endorsement by storage.
      - scope: Temporal supersession tags retaining historical assertions
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records: &id057
          - epistemic.md#epi-obj-temporal-edge
          - epistemic.md#epi-rte-temporal-supersession
          note: Older functional-relation edges receive superseded metadata while history remains. Current-by-recency
            tagging is not empirical truth; downstream compliance is unresolved.
        records: *id057
        note: Older functional-relation edges receive superseded metadata while history remains. Current-by-recency
          tagging is not empirical truth; downstream compliance is unresolved.
      - scope: Personal preference decay/prune and whole-line text caps
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id058
          - memory.md#mem-obj-preference-state
          - memory.md#mem-obj-preference-text
          - memory.md#mem-rte-ranking-maintenance
          note: Read-time decay downweights preference edges; pruning and capped preference text forget
            selected old material.
        records: *id058
        note: Read-time decay downweights preference edges; pruning and capped preference text forget
          selected old material.
      - scope: Configured cache expiry
        assessment: known
        findings:
        - value: decay
          basis: afforded
          records: &id059
          - memory.md#mem-obj-session-qa
          - memory.md#mem-obj-session-context
          note: Factory/session TTL offers forgetting, but adapter-equivalent expiry is not audited.
        records: *id059
        note: Factory/session TTL offers forgetting, but adapter-equivalent expiry is not audited.
      - scope: Curator/writer lesson semantics and other model extraction paths
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-session-distillation
        - epistemic.md#epi-rte-lesson-curation
        - epistemic.md#epi-rte-lesson-check
        - runtime.md#rt-rte-permanent-memory
        note: Without input/output pairs, accepted records leave semantic preservation/generalization
          unresolved. Model production alone does not establish synthesize.
      - scope: Withdrawal of numerical/text derivatives, summary rebuilds and custom maintenance
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-memory-withdrawal
        - memory.md#mem-rte-summary-readback
        - memory.md#mem-rte-ranking-maintenance
        note: Deletion and rebuild are not automatically invalidate or evolve; retained-history withdrawal/reversal
          on all derivatives remains untraced.
      records:
      - memory.md#mem-obj-session-context
      - memory.md#mem-rte-session-guidance
      - memory.md#mem-obj-graph-content
      - runtime.md#rt-rte-permanent-memory
      - memory.md#mem-rte-trace-promotion
      - memory.md#mem-obj-global-context-summary
      - memory.md#mem-rte-summary-readback
      - runtime.md#rt-rte-skill-revision
      - memory.md#mem-obj-skill-procedure
      - memory.md#mem-obj-session-learning
      - memory.md#mem-rte-session-distillation
      - epistemic.md#epi-obj-temporal-edge
      - epistemic.md#epi-rte-temporal-supersession
      - memory.md#mem-obj-preference-state
      - memory.md#mem-obj-preference-text
      - memory.md#mem-rte-ranking-maintenance
      - memory.md#mem-obj-session-qa
      - epistemic.md#epi-rte-lesson-curation
      - epistemic.md#epi-rte-lesson-check
      - memory.md#mem-rte-memory-withdrawal
      note: Consolidation, deduplication, revision, promotion, decay and historical supersession have
        distinct warrants. Requested novelty or generated prose is not enough for synthesize; opaque maintenance
        is retained.
    read_back_direction:
      assessment: partial
      units:
      - scope: Consumer-requested recall/search return and model-requested load_skill body
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id060
          - runtime.md#rt-rte-recall-dispatch
          - workflow.md#wf-rte-skill-loading
          note: Caller asks for recall and foreground model asks for procedure by name; fulfilling either
            request is pull, not an extra push.
        records: *id060
        note: Caller asks for recall and foreground model asks for procedure by name; fulfilling either
          request is pull, not an extra push.
      - scope: Configured decorator selection into wrapped gateway call
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id061
          - runtime.md#rt-rte-decorated-agent
          - runtime.md#rt-bap-memory-injection
          note: At host invocation code selects cached feedback and graph context without that model requesting
            those retained parts.
        records: *id061
        note: At host invocation code selects cached feedback and graph context without that model requesting
          those retained parts.
      - scope: Session history/guidance/preferences into answer model
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id062
          - memory.md#mem-rte-session-guidance
          - memory.md#mem-obj-session-qa
          - memory.md#mem-obj-preference-text
          note: Answer preparation automatically selects retained context for the completion consumer
            within a request chain.
        records: *id062
        note: Answer preparation automatically selects retained context for the completion consumer within
          a request chain.
      - scope: Root/relevant summaries into graph completion
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id063
          - memory.md#mem-rte-summary-readback
          note: Opt-in enables automatic prelude selection for the answering model; the external answer
            request remains pull.
        records: *id063
        note: Opt-in enables automatic prelude selection for the answering model; the external answer
          request remains pull.
      - scope: Skill catalog and graph/history guidance into agentic model
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id064
          - memory.md#mem-obj-skill-metadata
          - runtime.md#rt-rte-agentic-tools
          note: Prepared model context automatically supplies selected metadata and retained context;
            later body requests are separate pull operations.
        records: *id064
        note: Prepared model context automatically supplies selected metadata and retained context; later
          body requests are separate pull operations.
      - scope: Retained traces/QA/guidance/runs into subsequent maintenance consumers
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id065
          - memory.md#mem-rte-trace-promotion
          - memory.md#mem-rte-session-distillation
          - runtime.md#rt-rte-skill-revision
          - memory.md#mem-rte-ranking-maintenance
          note: Maintenance code chooses pending windows, gated entries or selected failure runs and supplies
            them to update consumers.
        records: *id065
        note: Maintenance code chooses pending windows, gated entries or selected failure runs and supplies
          them to update consumers.
      - scope: Other recall lanes, concurrent session preparation and external/remote consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-recall-dispatch
        - memory.md#mem-rte-session-guidance
        - runtime.md#rt-rte-permanent-memory
        note: One known requested path does not resolve every automatic supply alternative or actual host
          consumption.
      records:
      - runtime.md#rt-rte-recall-dispatch
      - workflow.md#wf-rte-skill-loading
      - runtime.md#rt-rte-decorated-agent
      - runtime.md#rt-bap-memory-injection
      - memory.md#mem-rte-session-guidance
      - memory.md#mem-obj-session-qa
      - memory.md#mem-obj-preference-text
      - memory.md#mem-rte-summary-readback
      - memory.md#mem-obj-skill-metadata
      - runtime.md#rt-rte-agentic-tools
      - memory.md#mem-rte-trace-promotion
      - memory.md#mem-rte-session-distillation
      - runtime.md#rt-rte-skill-revision
      - memory.md#mem-rte-ranking-maintenance
      - runtime.md#rt-rte-permanent-memory
      note: Pull request/return and push automatic context/evidence selection coexist within chains. Neither
        storage APIs alone nor code delivery of an already requested part creates another push.
    read_back_signal:
      assessment: partial
      units:
      - scope: 'Decorator invocation: recent trace feedback and query-selected graph text'
        assessment: partial
        findings:
        - value: coarse
          basis: wired
          records: &id066
          - runtime.md#rt-rte-decorated-agent
          note: Availability, last_n and truncation select recent feedback and bound mixed delivery.
        records: *id066
        note: Host invocation triggers selection; enabled sources/last_n and a 4,000-character cap select
          recent feedback, while query/top_k selects graph memory. Only structured-output gateway receives
          it. The accepted route and its memory annotation do not establish the graph selector's operation;
          GRAPH_SUMMARY_COMPLETION and an available vector index do not establish embedding-based selection
          on this path. Coarse filtering is known, but the graph-selection signal remains not determinable.
      - scope: 'Session answer preparation: history and active guidance'
        assessment: partial
        findings:
        - value: coarse
          basis: wired
          records: *id045
          note: Profile, section, recency, availability and whole-entry budgets filter selected history/guidance.
        - value: inferred-lexical
          basis: wired
          records: *id045
          note: Query-content overlap contributes to active-guidance ranking.
        - value: inferred-judgment
          basis: wired
          records:
          - memory.md#mem-rte-session-guidance
          - memory.md#mem-obj-session-context
          note: Model-produced confidence and helpful/harmful feedback counters influence which guidance
            is supplied.
        records:
        - memory.md#mem-rte-session-guidance
        - memory.md#mem-obj-session-context
        - memory.md#mem-obj-session-qa
        note: New answer preparation selects recent/history hits and guidance by profile/section, confidence,
          helpfulness, priority, recency and budgets. Session-vector implementation is unresolved.
      - scope: Global-summary prelude selection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: *id063
          note: Root detection selects dataset-wide root content.
        - value: inferred-embedding
          basis: wired
          records: *id063
          note: Query vector similarity selects non-root bucket text.
        records: *id063
        note: Single-query opt-in triggers root plus top_k relevant non-root summaries; the answering
          model receives selected text, not all child bodies.
      - scope: Skill discovery catalog supplied before procedure requests
        assessment: known
        findings:
        - value: inferred-embedding
          basis: wired
          records:
          - memory.md#mem-obj-skill-metadata
          - memory.md#mem-obj-vector-index
          note: Search over Skill_search_text selects metadata payload hits.
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-skill-metadata
          note: Active/scope/availability/top_k filtering bounds the pushed catalog.
        records:
        - memory.md#mem-obj-skill-metadata
        - memory.md#mem-obj-vector-index
        - runtime.md#rt-rte-agentic-tools
        note: Retrieval preparation supplies catalog metadata; vector hits are filtered by active/dataset
          scope and trimmed. Requested load_skill name matching is pull, not an identifier-push witness.
      - scope: Maintenance evidence selection from retained activity
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-trace-promotion
          - runtime.md#rt-rte-skill-revision
          note: Watermarks, last-window caps, status/score thresholds and recency select update evidence.
        - value: inferred-judgment
          basis: wired
          records:
          - memory.md#mem-rte-session-distillation
          note: Model-derived confidence/helpfulness gates select context available to the curator.
        records:
        - memory.md#mem-rte-trace-promotion
        - memory.md#mem-rte-session-distillation
        - runtime.md#rt-rte-skill-revision
        note: Improve or revision invocation triggers software selection of pending trace/QA windows,
          gated context or failing SkillRuns for update consumers.
      - scope: Distillation writer member-entry delivery
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id067
          - memory.md#mem-rte-session-distillation
          - epistemic.md#epi-rte-lesson-check
          note: For each curator proposal, code resolves member_entry_ids in entries_by_id and supplies
            those retained member contents to the writer; missing IDs are omitted. This is actual identity
            selection, not merely a catalog identifier.
        records: *id067
        note: For each curator proposal, code resolves member_entry_ids in entries_by_id and supplies
          those retained member contents to the writer; missing IDs are omitted. This is actual identity
          selection, not merely a catalog identifier.
      - scope: Session vector-hit selector internals and alternative recall push paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-session-guidance
        - runtime.md#rt-rte-recall-dispatch
        note: Recorded vector hits do not establish the complete selector internals. Code/temporal/lexical/custom
          lanes and concurrent preparation remain untraced.
      records:
      - runtime.md#rt-rte-decorated-agent
      - memory.md#mem-rte-session-guidance
      - memory.md#mem-obj-session-context
      - memory.md#mem-obj-session-qa
      - memory.md#mem-rte-summary-readback
      - memory.md#mem-obj-skill-metadata
      - memory.md#mem-obj-vector-index
      - runtime.md#rt-rte-agentic-tools
      - memory.md#mem-rte-trace-promotion
      - memory.md#mem-rte-session-distillation
      - runtime.md#rt-rte-skill-revision
      - epistemic.md#epi-rte-lesson-check
      - runtime.md#rt-rte-recall-dispatch
      note: Push witnesses retain trigger, selector inputs and delivered parts. Body-name lookup on a
        pull request is not counted as identifier push; the distinct writer member-resolution operation
        is. The decorator's graph-selector signal and alternative-route coverage remain unresolved;
        neither an available index nor a query-relevant result establishes route-specific embedding selection.
        These limits prevent inapplicability or a complete signal inventory.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatic turn-feedback to active guidance and durable preferences
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id068
          - memory.md#mem-rte-session-guidance
          - memory.md#mem-rte-ranking-maintenance
          - memory.md#mem-obj-session-context
          - memory.md#mem-obj-preference-text
          note: Recorded conversational turns feed automatic guidance/preference writes with later answer
            consumers; cache retention can span invocations despite TTL.
        records: *id068
        note: Recorded conversational turns feed automatic guidance/preference writes with later answer
          consumers; cache retention can span invocations despite TTL.
      - scope: Automatic decorated trace extraction/promotion to later memory
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id069
          - memory.md#mem-rte-trace-promotion
          - runtime.md#rt-rte-decorated-agent
          - memory.md#mem-obj-session-context
          note: Trace output/error records feed automatic standing-guidance and graph writes, then explicit
            profile/distillation/graph consumers. Do not infer agent-profile injection into every agentic
            loop.
        records: *id069
        note: Trace output/error records feed automatic standing-guidance and graph writes, then explicit
          profile/distillation/graph consumers. Do not infer agent-profile injection into every agentic
          loop.
      - scope: Automatic session lesson publication
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id070
          - memory.md#mem-rte-session-distillation
          - memory.md#mem-obj-session-learning
          note: Recorded QA and derived context feed automatic curator/writer publication into later graph
            recall and truth-build consumers.
        records: *id070
        note: Recorded QA and derived context feed automatic curator/writer publication into later graph
          recall and truth-build consumers.
      - scope: Automatic feedback/preference ranking updates
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id071
          - memory.md#mem-rte-ranking-maintenance
          - memory.md#mem-obj-feedback-weight
          - memory.md#mem-obj-preference-state
          note: Recorded feedback and used IDs change retained code-ranking parameters for later retrieval,
            not provider weights.
        records: *id071
        note: Recorded feedback and used IDs change retained code-ranking parameters for later retrieval,
          not provider weights.
      - scope: Learning-derived truth geometry updates
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id072
          - memory.md#mem-rte-truth-maintenance
          - memory.md#mem-obj-truth-state
          note: Session-derived learning text feeds automatic numerical retained updates consumed by conditional
            hybrid ranking; this is trace-fed shaping, not measured improvement.
        records: *id072
        note: Session-derived learning text feeds automatic numerical retained updates consumed by conditional
          hybrid ranking; this is trace-fed shaping, not measured improvement.
      - scope: Failure-fed stored skill proposal and its installation chain
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-skill-revision
        - runtime.md#rt-obj-skill-proposal
        note: Automatic drafting retains failure evidence and a candidate procedure, but proposal retention
          alone does not establish a durable behavior-shaping update. Later skill delivery requires caller-selected
          apply whose control is unresolved.
      - scope: 'Qualifying installed skill revision: caller-selected apply control'
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-skill-revision
        - memory.md#mem-obj-skill-procedure
        note: Proposal drafting is automatic, but human/software control of installation is unknown; no
          automatic replacement claim follows from generic caller identity.
      - scope: Typed trace/QA/SkillRun origins and alternate maintenance routes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-typed-admission
        - memory.md#mem-obj-session-agent-trace
        - memory.md#mem-obj-skill-run
        - memory.md#mem-rte-summary-readback
        - runtime.md#rt-rte-permanent-memory
        note: Typed data may be static, mixed or authentic activity; global-summary input origin and alternate
          writes are not completely established. No system-wide no or absence claim is warranted.
      records:
      - memory.md#mem-rte-session-guidance
      - memory.md#mem-rte-ranking-maintenance
      - memory.md#mem-obj-session-context
      - memory.md#mem-obj-preference-text
      - memory.md#mem-rte-trace-promotion
      - runtime.md#rt-rte-decorated-agent
      - memory.md#mem-rte-session-distillation
      - memory.md#mem-obj-session-learning
      - memory.md#mem-obj-feedback-weight
      - memory.md#mem-obj-preference-state
      - memory.md#mem-rte-truth-maintenance
      - memory.md#mem-obj-truth-state
      - runtime.md#rt-rte-skill-revision
      - runtime.md#rt-obj-skill-proposal
      - memory.md#mem-obj-skill-procedure
      - memory.md#mem-rte-typed-admission
      - memory.md#mem-obj-session-agent-trace
      - memory.md#mem-obj-skill-run
      - memory.md#mem-rte-summary-readback
      - runtime.md#rt-rte-permanent-memory
      note: Several automatic trace-fed writes with later behavior-shaping consumers support yes. Raw
        recording alone is not learning; caller-selected installation and opaque input alternatives stay
        unresolved. This axis does not claim improved capacity.
    trace_source:
      assessment: partial
      units:
      - scope: Turn guidance, preference/feedback updates and session lesson publication
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id073
          - memory.md#mem-rte-session-guidance
          - memory.md#mem-rte-ranking-maintenance
          - memory.md#mem-rte-session-distillation
          - memory.md#mem-obj-session-qa
          - memory.md#mem-obj-session-feedback
          note: Original recorded question/answer/follow-up turns feed the qualifying writes; derived
            context retains this session-origin path.
        records: *id073
        note: Original recorded question/answer/follow-up turns feed the qualifying writes; derived context
          retains this session-origin path.
      - scope: Decorated-agent error/output extraction and promotion
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id074
          - memory.md#mem-rte-trace-promotion
          - memory.md#mem-obj-session-agent-trace
          - runtime.md#rt-rte-decorated-agent
          note: Recorded host requests/parameters, return/error and execution feedback supply the qualifying
            agent-trace write. Arbitrary typed origins are separate unresolved alternatives.
        records: *id074
        note: Recorded host requests/parameters, return/error and execution feedback supply the qualifying
          agent-trace write. Arbitrary typed origins are separate unresolved alternatives.
      - scope: Skill revision evidence from shipped run recorder
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-skill-run
        - runtime.md#rt-rte-skill-revision
        note: Drafting consumes execution error/result summaries, not the full retained tool_trace. The
          origin is recorded, but unresolved apply control prevents establishing the qualifying automatic
          installation chain; no positive trace-source classification is assigned to this unresolved route.
      - scope: Session-derived truth geometry
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id075
          - memory.md#mem-rte-truth-maintenance
          - memory.md#mem-obj-session-learning
          - memory.md#mem-rte-session-distillation
          note: The recorded origin is QA/session context through accepted learning text, not event-stream
            merely because the lesson has a session heading.
        records: *id075
        note: The recorded origin is QA/session context through accepted learning text, not event-stream
          merely because the lesson has a session heading.
      - scope: Mixed batch trace origins and typed QA/Trace/Feedback/SkillRun entries
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-typed-admission
        - memory.md#mem-obj-session-agent-trace
        - memory.md#mem-obj-skill-run
        - memory.md#mem-rte-trace-promotion
        note: Generic typed labels and sanitized display strings do not authenticate original session/tool/event/trajectory
          content; mixed or opaque parts cannot be assigned a complete source set.
      - scope: Skill proposal current-procedure input and global-summary/custom-route origins
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-skill-revision
        - memory.md#mem-obj-skill-procedure
        - memory.md#mem-rte-summary-readback
        - runtime.md#rt-rte-permanent-memory
        note: Revision mixes current procedure with failure evidence. Initial procedure and alternate
          summary/maintenance origin are unresolved; static imported instructions do not establish trace
          sources.
      records:
      - memory.md#mem-rte-session-guidance
      - memory.md#mem-rte-ranking-maintenance
      - memory.md#mem-rte-session-distillation
      - memory.md#mem-obj-session-qa
      - memory.md#mem-obj-session-feedback
      - memory.md#mem-rte-trace-promotion
      - memory.md#mem-obj-session-agent-trace
      - runtime.md#rt-rte-decorated-agent
      - memory.md#mem-obj-skill-run
      - runtime.md#rt-rte-skill-revision
      - memory.md#mem-rte-truth-maintenance
      - memory.md#mem-obj-session-learning
      - memory.md#mem-rte-typed-admission
      - memory.md#mem-obj-skill-procedure
      - memory.md#mem-rte-summary-readback
      - runtime.md#rt-rte-permanent-memory
      note: Session logs and consumed execution feedback support local sources on qualifying writes. Timestamps/serialization
        do not establish event-streams, and linked state-action-outcome trajectories are not established.
        Opaque mixed routes prevent complete trace-source coverage.
---

# Cognee memory profile

## Comparison rationale

All ten axes are partial. Positive witnesses classify particular retained parts and consumers, not every shipped memory path. Cache factory alternatives are afforded rather than treated as audited storage contracts. Typed caller origins, all recall lanes, custom extraction/indexing, concurrent answer preparation, direct writes and derivative withdrawal remain unresolved in the accepted records. No absence record licenses a system-wide negative. The partial scope does not exclude an opaque alternative just because an inspected branch is classifiable.

Dense retrieval vectors and truth geometry are parametric representations, while feedback scalars, counters and epochs are symbolic localized state. Neither is evidence that embedding-provider or language-model weights change. Their graph/vector stores are substrates, not forms. See [MEM-OBJ-vector-index](memory.md#mem-obj-vector-index), [MEM-OBJ-truth-state](memory.md#mem-obj-truth-state) and [MEM-OBJ-feedback-weight](memory.md#mem-obj-feedback-weight).

Authority belongs to actual consumers. Retained session/run evidence has learning authority at guidance/procedure/ranking updates, while the resulting text has knowledge or instruction authority and numerical state has ranking authority downstream. Scope/tool and epoch guards establish local enforced selection, not truth guarantees or handler isolation. Conflict and supersession metadata have unresolved later consumers. See [MEM-RTE-ranking-maintenance](memory.md#mem-rte-ranking-maintenance), [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision), [MEM-OBJ-skill-metadata](memory.md#mem-obj-skill-metadata), [MEM-RTE-truth-maintenance](memory.md#mem-rte-truth-maintenance) and [EPI-RTE-temporal-supersession](epistemic.md#epi-rte-temporal-supersession).

Software admission is automatic on the inspected internal routes; explicit workflow start is not human approval of each retained fact. Initial supply, editing and caller-selected skill installation remain not determinable for human versus software control. Trace-fed proposal drafting is wired, but installation is a separate unresolved mechanism. Its unresolved qualifying-write assessment must not become an unconditional automatic deployed-skill update. Other session-guidance and ranking routes independently establish qualifying trace-fed updates; none establishes improved capacity. See [MEM-RTE-typed-admission](memory.md#mem-rte-typed-admission), [MEM-RTE-session-guidance](memory.md#mem-rte-session-guidance), [MEM-RTE-trace-promotion](memory.md#mem-rte-trace-promotion) and [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision).

Consolidation describes compression or extraction of retained content; synthesis would require a new claim absent from the inputs. Curator/writer semantic indeterminacy is therefore retained rather than classified as synthesis. Exact normalized-content merging supports dedup independently of the writer's novelty request. Temporal supersession retains history and marks current reliance withdrawn by recency policy, without establishing downstream compliance. See [MEM-RTE-summary-readback](memory.md#mem-rte-summary-readback), [MEM-OBJ-session-context](memory.md#mem-obj-session-context), [EPI-RTE-lesson-check](epistemic.md#epi-rte-lesson-check) and [EPI-RTE-temporal-supersession](epistemic.md#epi-rte-temporal-supersession).

Recall and load_skill are pull operations. Inside answer/update preparation, automatic selection supplies retained material to a different consumer and supports push. The writer's resolution of member_entry_ids is an identity-selected push; the model's requested skill-name lookup is not. Skills remain truncated at both handler and loop boundaries. See [RT-RTE-recall-dispatch](runtime.md#rt-rte-recall-dispatch), [WF-RTE-skill-loading](workflow.md#wf-rte-skill-loading), [MEM-RTE-session-guidance](memory.md#mem-rte-session-guidance) and [EPI-RTE-lesson-check](epistemic.md#epi-rte-lesson-check).

The decorator's push signal is only partially classified. Recent-feedback availability, last_n and delivery truncation support coarse filtering. Query/top_k and GRAPH_SUMMARY_COMPLETION establish graph-memory selection but not its route-specific embedding operation. The unsupported inferred-embedding finding is withdrawn; the unit remains partial rather than known. Embedding findings for the separately recorded global-summary and skill-catalog selectors are unchanged. See [RT-RTE-decorated-agent](runtime.md#rt-rte-decorated-agent), including its memory annotation, [MEM-RTE-summary-readback](memory.md#mem-rte-summary-readback) and [MEM-OBJ-vector-index](memory.md#mem-obj-vector-index).

The reconciliation supersedes EPI-OBJ-learning-document with [MEM-OBJ-session-learning](memory.md#mem-obj-session-learning) and EPI-OBJ-truth-coordinates with [MEM-OBJ-truth-state](memory.md#mem-obj-truth-state). This profile uses those canonical objects for storage, form, lineage and later consumer findings. The separate epistemic route functions remain valid; no other record is superseded. Progressive-load inspection qualifies delivery completeness without replacing the runtime authority-path identity.

No source files were read for this classification. All warrants are the supplied accepted records and their annotations, resolved through the supplied reconciliation. Evidence is implementation or doctrine/design, not observed operation or causal benefit. Missing execution evidence does not erase implemented capacity; it prevents claims of activated guidance, successful persistence, improved accuracy and beneficial learning.
