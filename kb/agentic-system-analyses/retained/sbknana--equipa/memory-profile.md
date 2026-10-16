---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'EQUIPA memory comparison: retained experience, recovery, project and initiative context,
  access metadata and accumulated instruction changes, with unresolved alternatives.'
run-id: AAS-2026-10-15-equipa-32016e8dd9ae-01
source-identity: https://github.com/sbknana/equipa
reviewed-boundary: fa8f41a6948584ee53e804edbb08b7449d05cd14
memory-comparison:
  version: 2
  scope: 'Included: accumulated episode/lesson prose and access metadata, embeddings and graph edges,
    hard/soft checkpoints, reconstructed sessions and cross-invocation summaries, project records, initiative
    appends, inter-agent messages, optional output offload, and through-use prompt/configuration variants
    and their maintenance metadata. Included unresolved alternatives: initial-content admission/provenance,
    provider-owned compaction/state, arbitrary hooks/plugins, complete optimizers/scorers/rollback, training
    metadata consumers, housekeeping/setup/migration/sync and alternate callers. Excluded: unchanged shipped
    instructions, ordinary current-call conversation/REPL accumulation, general runtime storage/permissions,
    external model weights merely used for inference, and product Git/source changes except the particular
    retained initiative/prompt artifacts. No live deployment or execution evidence is asserted.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: SQLite episode prose, lessons, project records, messages, session state, Q/effectiveness
          metadata, vectors and graph-edge rows
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-agent-episodes
          - memory.md#mem-obj-lessons-learned
          - memory.md#mem-obj-q-value
          - memory.md#mem-obj-embedding
          - memory.md#mem-obj-lesson-graph-edges
          - memory.md#mem-obj-agent-sessions
          - memory.md#mem-obj-project-context
          - memory.md#mem-obj-agent-messages
          - epistemic.md#epi-obj-effectiveness-score
          note: Each recorded operative part resides in SQLite; vector encoding and graph-shaped access
            metadata do not establish separate vector or graph storage engines.
        records:
        - memory.md#mem-obj-agent-episodes
        - memory.md#mem-obj-lessons-learned
        - memory.md#mem-obj-q-value
        - memory.md#mem-obj-embedding
        - memory.md#mem-obj-lesson-graph-edges
        - memory.md#mem-obj-agent-sessions
        - memory.md#mem-obj-project-context
        - memory.md#mem-obj-agent-messages
        - epistemic.md#epi-obj-effectiveness-score
        note: These named table parts have recorded storage; provider weights are not included as learned
          memory merely because inference uses them.
      - scope: Hard/soft checkpoint files and optional output-offload files
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-checkpoints
          - memory.md#mem-obj-soft-checkpoints
          - memory.md#mem-obj-persisted-output
          note: Output text and state JSON persist in filesystem files; the offload helper does not establish
            later reload.
        records:
        - memory.md#mem-obj-checkpoints
        - memory.md#mem-obj-soft-checkpoints
        - memory.md#mem-obj-persisted-output
        note: Storage classification does not assert that optional offload is enabled.
      - scope: Initiative memory and accumulated prompt/configuration variants and backups
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-initiative-plan
          - runtime.md#rt-obj-role-prompts
          - runtime.md#rt-rte-forgesmith-changes
          - runtime.md#rt-rte-gepa-prompts
          - runtime.md#rt-rte-autoresearch-prompts
          note: Initiative Markdown and changed/versioned role text or configuration persist as files.
        - value: repo
          basis: wired
          records:
          - memory.md#mem-obj-initiative-plan
          - memory.md#mem-rte-initiative-memory
          note: Initiative updates are also committed to the task branch when the dispatch helper succeeds;
            this is a repository-backed memory artifact, not a classification of every product file.
        records:
        - memory.md#mem-obj-initiative-plan
        - memory.md#mem-rte-initiative-memory
        - runtime.md#rt-obj-role-prompts
        - runtime.md#rt-rte-forgesmith-changes
        - runtime.md#rt-rte-gepa-prompts
        - runtime.md#rt-rte-autoresearch-prompts
        note: SQLite evolution/version metadata is covered with its own metadata unit below; static shipped
          instructions are excluded.
      - scope: GEPA version and change metadata
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - runtime.md#rt-obj-role-prompts
          - runtime.md#rt-rte-gepa-prompts
          note: The versioned prompt path retains SQLite change/version records in addition to file bytes.
        records:
        - runtime.md#rt-obj-role-prompts
        - runtime.md#rt-rte-gepa-prompts
        note: Metadata storage is separate from the natural-language instruction payload.
      - scope: Exposure tracker and retained cross-invocation summary strings
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-q-value
          - epistemic.md#epi-obj-prior-summary
          - memory.md#mem-rte-context-recovery
          note: Process-local task-to-episode tracking and Python history strings survive to later consumers
            within the process.
        records:
        - memory.md#mem-obj-q-value
        - epistemic.md#epi-obj-prior-summary
        - memory.md#mem-rte-context-recovery
        note: Process memory qualifies for these accumulated/reshaped objects; ordinary current-call Ollama/RLM
          conversation accumulation is excluded.
      - scope: Training-marker metadata
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - epistemic.md#epi-obj-training-marker
          note: Imported marker JSON remains in a processed filesystem directory when the move succeeds.
        - value: sqlite
          basis: wired
          records:
          - epistemic.md#epi-obj-training-marker
          note: Importer commits a model_registry row; the row does not establish changed model weights.
        records:
        - epistemic.md#epi-obj-training-marker
        note: Storage is inspected even though downstream consumers are not.
      - scope: Remaining included maintenance, plugin, training and provider-owned memory alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lifecycle-hooks
        - epistemic.md#epi-obj-training-marker
        - epistemic.md#epi-rte-rubric-scores
        - runtime.md#rt-rte-forgesmith-changes
        - memory.md#mem-rte-context-recovery
        note: Arbitrary hook/plugin writes, complete optimizer/scoring/evaluation and training consumers,
          and opaque host compaction remain included but incompletely inspected. Setup/migration/sync
          and housekeeping routes lack complete recorded admission/consumer coverage. These alternatives
          cannot inherit the classifications of the inspected routes.
      records:
      - memory.md#mem-obj-agent-episodes
      - memory.md#mem-obj-lessons-learned
      - memory.md#mem-obj-q-value
      - memory.md#mem-obj-embedding
      - memory.md#mem-obj-lesson-graph-edges
      - memory.md#mem-obj-agent-sessions
      - memory.md#mem-obj-project-context
      - memory.md#mem-obj-agent-messages
      - epistemic.md#epi-obj-effectiveness-score
      - memory.md#mem-obj-checkpoints
      - memory.md#mem-obj-soft-checkpoints
      - memory.md#mem-obj-persisted-output
      - memory.md#mem-obj-initiative-plan
      - memory.md#mem-rte-initiative-memory
      - runtime.md#rt-obj-role-prompts
      - runtime.md#rt-rte-forgesmith-changes
      - runtime.md#rt-rte-gepa-prompts
      - runtime.md#rt-rte-autoresearch-prompts
      - epistemic.md#epi-obj-prior-summary
      - memory.md#mem-rte-context-recovery
      - epistemic.md#epi-obj-training-marker
      - runtime.md#rt-rte-lifecycle-hooks
      - epistemic.md#epi-rte-rubric-scores
      note: The named retained-object inventory establishes filesystem, repository, SQLite and process-memory
        witnesses. Opaque provider memory and remaining shipped maintenance alternatives prevent complete
        substrate coverage; no graph/vector/model-weight substrate follows from an encoding or model name.
    representational_form:
      assessment: partial
      units:
      - scope: Episode and lesson prose, project history, initiative summaries/decisions, checkpoint output
          and rendered recovery/history at inference
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-agent-episodes
          - memory.md#mem-obj-lessons-learned
          - memory.md#mem-obj-project-context
          - memory.md#mem-obj-initiative-plan
          - memory.md#mem-obj-checkpoints
          - memory.md#mem-obj-soft-checkpoints
          - memory.md#mem-obj-agent-sessions
          - epistemic.md#epi-obj-prior-summary
          - memory.md#mem-rte-context-recovery
          note: The later model interprets prose, including selected historical descriptions and advice.
        records:
        - memory.md#mem-obj-agent-episodes
        - memory.md#mem-obj-lessons-learned
        - memory.md#mem-obj-project-context
        - memory.md#mem-obj-initiative-plan
        - memory.md#mem-obj-checkpoints
        - memory.md#mem-obj-soft-checkpoints
        - memory.md#mem-obj-agent-sessions
        - epistemic.md#epi-obj-prior-summary
        - memory.md#mem-rte-context-recovery
        note: This unit covers text parts only, not identifiers, counters, paths or tool-status envelopes.
      - scope: Accumulated role-instruction bodies at the prompt consumer
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - runtime.md#rt-obj-role-prompts
          - runtime.md#rt-rte-gepa-prompts
          - runtime.md#rt-rte-autoresearch-prompts
          - runtime.md#rt-rte-forgesmith-changes
          note: Changed role text supplies model-interpreted instructions.
        records:
        - runtime.md#rt-obj-role-prompts
        - runtime.md#rt-rte-gepa-prompts
        - runtime.md#rt-rte-autoresearch-prompts
        - runtime.md#rt-rte-forgesmith-changes
        note: Symbolic settings and selector metadata are classified separately.
      - scope: Access, recovery and configuration metadata at fixed-rule consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-q-value
          - memory.md#mem-obj-lesson-graph-edges
          - memory.md#mem-obj-agent-sessions
          - memory.md#mem-obj-soft-checkpoints
          - epistemic.md#epi-obj-effectiveness-score
          - memory.md#mem-rte-experience-retrieval
          - runtime.md#rt-rte-gepa-prompts
          - runtime.md#rt-rte-forgesmith-changes
          - runtime.md#rt-rte-role-extension
          note: IDs, status/time flags, paths, scores, graph edges, settings and version labels have localized
            units interpreted by fixed rules.
        records:
        - memory.md#mem-obj-q-value
        - memory.md#mem-obj-lesson-graph-edges
        - memory.md#mem-obj-agent-sessions
        - memory.md#mem-obj-soft-checkpoints
        - epistemic.md#epi-obj-effectiveness-score
        - memory.md#mem-rte-experience-retrieval
        - runtime.md#rt-rte-gepa-prompts
        - runtime.md#rt-rte-forgesmith-changes
        - runtime.md#rt-rte-role-extension
        note: Numerical Q-values and effectiveness are symbolic scalars, not distributed parameters.
      - scope: Stored dense embeddings at cosine-similarity consumer
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-embedding
          - memory.md#mem-rte-experience-retrieval
          note: Distributed numerical vectors are the operative dense representation. JSON serialization
            does not make the similarity-consumed representation a symbolic reasoning artifact.
        records:
        - memory.md#mem-obj-embedding
        - memory.md#mem-rte-experience-retrieval
        note: Model/vector version compatibility remains unresolved, not the recorded vector form.
      - scope: Agent messages and optional offloaded output payloads
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-agent-messages
          - memory.md#mem-obj-persisted-output
          note: Prose messages and textual output/preview parts are interpreted as text.
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-agent-messages
          - memory.md#mem-obj-persisted-output
          note: Routing/read-state fields and returned file paths are symbolic metadata distinct from
            payload text.
        records:
        - memory.md#mem-obj-agent-messages
        - memory.md#mem-obj-persisted-output
        note: Known mixed text/envelope distinction; optional output has no established later reload route.
      - scope: Training marker and retained score descriptions
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - epistemic.md#epi-obj-training-marker
          - epistemic.md#epi-obj-rubric-scores
          note: Marker fields and scoring result numbers are structured metadata.
        - value: natural-language
          basis: wired
          records:
          - epistemic.md#epi-obj-training-marker
          - epistemic.md#epi-obj-rubric-scores
          note: Marker provenance/notes and matched-pattern descriptions retain text parts.
        records:
        - epistemic.md#epi-obj-training-marker
        - epistemic.md#epi-rte-rubric-scores
        - epistemic.md#epi-obj-rubric-scores
        note: This classifies the inspected metadata, not an opaque trained model.
      - scope: Remaining included maintenance, plugin, training and provider-owned memory alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lifecycle-hooks
        - epistemic.md#epi-obj-training-marker
        - epistemic.md#epi-rte-rubric-scores
        - runtime.md#rt-rte-forgesmith-changes
        - memory.md#mem-rte-context-recovery
        note: Arbitrary hook/plugin writes, complete optimizer/scoring/evaluation and training consumers,
          and opaque host compaction remain included but incompletely inspected. Setup/migration/sync
          and housekeeping routes lack complete recorded admission/consumer coverage. These alternatives
          cannot inherit the classifications of the inspected routes.
      records:
      - memory.md#mem-obj-agent-episodes
      - memory.md#mem-obj-lessons-learned
      - memory.md#mem-obj-project-context
      - memory.md#mem-obj-initiative-plan
      - memory.md#mem-obj-checkpoints
      - memory.md#mem-obj-soft-checkpoints
      - memory.md#mem-obj-agent-sessions
      - epistemic.md#epi-obj-prior-summary
      - memory.md#mem-rte-context-recovery
      - runtime.md#rt-obj-role-prompts
      - runtime.md#rt-rte-gepa-prompts
      - runtime.md#rt-rte-autoresearch-prompts
      - runtime.md#rt-rte-forgesmith-changes
      - memory.md#mem-obj-q-value
      - memory.md#mem-obj-lesson-graph-edges
      - epistemic.md#epi-obj-effectiveness-score
      - memory.md#mem-rte-experience-retrieval
      - runtime.md#rt-rte-role-extension
      - memory.md#mem-obj-embedding
      - memory.md#mem-obj-agent-messages
      - memory.md#mem-obj-persisted-output
      - epistemic.md#epi-obj-training-marker
      - epistemic.md#epi-rte-rubric-scores
      - epistemic.md#epi-obj-rubric-scores
      - runtime.md#rt-rte-lifecycle-hooks
      note: Text, fixed-rule symbolic metadata and dense vectors are separately supported. Uninspected
        plugin/provider and maintenance payloads prevent a complete form inventory; opaque model inference
        is not automatically accumulated parametric memory.
    lineage:
      assessment: partial
      units:
      - scope: Derived episode/reflection, failure lessons, SIMBA rules, outcome priorities and continuation
          summaries
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-rte-episode-feedback
          - memory.md#mem-rte-lesson-maintenance
          - memory.md#mem-rte-context-recovery
          - epistemic.md#epi-rte-simba-rules
          - epistemic.md#epi-rte-episode-values
          note: Task output, outcomes, episode contrasts and recorded tool/state context feed extraction,
            reflection, deterministic summary or priority updates.
        records:
        - memory.md#mem-rte-episode-feedback
        - memory.md#mem-rte-lesson-maintenance
        - memory.md#mem-rte-context-recovery
        - epistemic.md#epi-rte-simba-rules
        - epistemic.md#epi-rte-episode-values
        note: Derivation is recorded even where factual faithfulness, rule novelty and benefit are not.
      - scope: Initiative task-outcome appends
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-rte-initiative-memory
          note: Parsed sibling outputs become capped summaries and decisions/rationales for later tasks.
        records:
        - memory.md#mem-rte-initiative-memory
        note: This does not resolve provenance of the initial plan.
      - scope: Accumulated prompt/configuration changes from run evidence
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-rte-forgesmith-changes
          - runtime.md#rt-rte-gepa-prompts
          - runtime.md#rt-rte-autoresearch-prompts
          note: Recorded maintenance/optimization paths use run or failure feedback to produce retained
            instruction/configuration changes.
        records:
        - runtime.md#rt-rte-forgesmith-changes
        - runtime.md#rt-rte-gepa-prompts
        - runtime.md#rt-rte-autoresearch-prompts
        note: Optimizer numerical internals remain a separate unresolved included branch.
      - scope: Embedding and graph derivation
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-embedding
          - memory.md#mem-obj-lesson-graph-edges
          note: Embedding inference compiles text into dense vectors; graph construction derives edges
            from similarity or co-access IDs.
        records:
        - memory.md#mem-obj-embedding
        - memory.md#mem-obj-lesson-graph-edges
        note: Recorded derivation does not pin historical embedding model versions or prove coherent lesson/episode
          node identity.
      - scope: Interactive project-context supplying/editing
        assessment: partial
        findings:
        - value: authored
          basis: afforded
          records:
          - memory.md#mem-rte-project-context
          note: Interactive human/agent entries are an afforded authoring route, not proof every existing
            row was human-approved.
        records:
        - memory.md#mem-rte-project-context
        - memory.md#mem-obj-project-context
        note: Initial table content and alternate direct/external writers have unresolved provenance.
      - scope: Declared operator initiative-plan editing
        assessment: partial
        findings:
        - value: authored
          basis: afforded
          records:
          - memory.md#mem-obj-initiative-plan
          - memory.md#mem-rte-initiative-memory
          note: The declared plan-edit surface affords deliberate authored content.
        records:
        - memory.md#mem-obj-initiative-plan
        - memory.md#mem-rte-initiative-memory
        note: Initial-plan provenance and actual editing governance remain unresolved.
      - scope: Raw agent output checkpoints and agent messages
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-checkpoints
          - memory.md#mem-obj-agent-messages
          note: Retained raw output/message prose originates in agent work rather than an independently
            warranted source.
        records:
        - memory.md#mem-obj-checkpoints
        - memory.md#mem-obj-agent-messages
        note: Checkpoint persistence is not itself a claim that every raw byte was extracted into a new
          rule.
      - scope: Imported training marker
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - epistemic.md#epi-obj-training-marker
          note: External marker metadata is acquired into model_registry, not generated or independently
            verified training evidence.
        records:
        - epistemic.md#epi-obj-training-marker
        note: Original training lineage and downstream weights are unresolved.
      - scope: Initial role/configuration content, trusted overlays and state-file hints
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-role-prompts
        - runtime.md#rt-rte-role-extension
        - memory.md#mem-rte-context-recovery
        note: The records identify sources and loaders but do not settle initial authorship/admission
          or all state-file provenance. Changed prompt paths above do not resolve these initial alternatives.
      - scope: Remaining included maintenance, plugin, training and provider-owned memory alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lifecycle-hooks
        - epistemic.md#epi-obj-training-marker
        - epistemic.md#epi-rte-rubric-scores
        - runtime.md#rt-rte-forgesmith-changes
        - memory.md#mem-rte-context-recovery
        note: Arbitrary hook/plugin writes, complete optimizer/scoring/evaluation and training consumers,
          and opaque host compaction remain included but incompletely inspected. Setup/migration/sync
          and housekeeping routes lack complete recorded admission/consumer coverage. These alternatives
          cannot inherit the classifications of the inspected routes.
      records:
      - memory.md#mem-rte-episode-feedback
      - memory.md#mem-rte-lesson-maintenance
      - memory.md#mem-rte-context-recovery
      - epistemic.md#epi-rte-simba-rules
      - epistemic.md#epi-rte-episode-values
      - memory.md#mem-rte-initiative-memory
      - runtime.md#rt-rte-forgesmith-changes
      - runtime.md#rt-rte-gepa-prompts
      - runtime.md#rt-rte-autoresearch-prompts
      - memory.md#mem-obj-embedding
      - memory.md#mem-obj-lesson-graph-edges
      - memory.md#mem-rte-project-context
      - memory.md#mem-obj-project-context
      - memory.md#mem-obj-initiative-plan
      - memory.md#mem-obj-checkpoints
      - memory.md#mem-obj-agent-messages
      - epistemic.md#epi-obj-training-marker
      - runtime.md#rt-obj-role-prompts
      - runtime.md#rt-rte-role-extension
      - runtime.md#rt-rte-lifecycle-hooks
      - epistemic.md#epi-rte-rubric-scores
      note: Known extraction/compilation and afforded authoring coexist with imported registry metadata.
        Initial content, historical embedding provenance and optimizer/provider alternatives remain unresolved;
        no initial provenance is inferred from a later transformation.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Historical experience, recovery, project, initiative and message text at later task inference
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-bap-experience-context
          - memory.md#mem-rte-experience-retrieval
          - memory.md#mem-rte-context-recovery
          - memory.md#mem-rte-project-context
          - memory.md#mem-rte-initiative-memory
          - memory.md#mem-obj-agent-messages
          note: Selected retained prose supplies historical evidence/context/advice under untrusted wrappers;
            delivery is not compliance.
        records:
        - memory.md#mem-bap-experience-context
        - memory.md#mem-rte-experience-retrieval
        - memory.md#mem-rte-context-recovery
        - memory.md#mem-rte-project-context
        - memory.md#mem-rte-initiative-memory
        - memory.md#mem-obj-agent-messages
        note: Raw reasons reach this consumer only to the extent extraction and truncation preserve them.
      - scope: Changed standing role text at later inference
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - runtime.md#rt-bap-role-instructions
          - runtime.md#rt-rte-forgesmith-changes
          - runtime.md#rt-rte-gepa-prompts
          - runtime.md#rt-rte-autoresearch-prompts
          note: Installed prompt revisions supply standing directions through ordinary role assembly.
        records:
        - runtime.md#rt-bap-role-instructions
        - runtime.md#rt-rte-forgesmith-changes
        - runtime.md#rt-rte-gepa-prompts
        - runtime.md#rt-rte-autoresearch-prompts
        note: This is distinct from advisory historical-memory text and from unchanged shipped prompts.
      - scope: Episodes, task traces and retained failures at update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-rte-episode-feedback
          - memory.md#mem-rte-lesson-maintenance
          - memory.md#mem-rte-context-recovery
          - epistemic.md#epi-rte-simba-rules
          - runtime.md#rt-rte-forgesmith-changes
          - runtime.md#rt-rte-gepa-prompts
          - runtime.md#rt-rte-autoresearch-prompts
          note: Experience and feedback feed durable rules, continuation state or behavior-shaping prompt/configuration
            updates.
        records:
        - memory.md#mem-rte-episode-feedback
        - memory.md#mem-rte-lesson-maintenance
        - memory.md#mem-rte-context-recovery
        - epistemic.md#epi-rte-simba-rules
        - runtime.md#rt-rte-forgesmith-changes
        - runtime.md#rt-rte-gepa-prompts
        - runtime.md#rt-rte-autoresearch-prompts
        note: Authority at the update consumer does not establish truth or improved future capacity.
      - scope: Episode/lesson prose and access metadata at retrieval ranking consumers
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-rte-experience-retrieval
          - memory.md#mem-obj-q-value
          - memory.md#mem-obj-embedding
          - memory.md#mem-obj-lesson-graph-edges
          - memory.md#mem-obj-lessons-learned
          note: Retained keywords/text, recency/counts, Q-values, vectors and graph edges influence relative
            priority.
        records:
        - memory.md#mem-rte-experience-retrieval
        - memory.md#mem-obj-q-value
        - memory.md#mem-obj-embedding
        - memory.md#mem-obj-lesson-graph-edges
        - memory.md#mem-obj-lessons-learned
        note: Fixed scoring code still gives retained text ranking force; graph identity/fallback caveats
          limit quality, not the existence of the ranking path.
      - scope: Active/Q/expiry/read-state fields at selection and withdrawal consumers
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-rte-lesson-maintenance
          - memory.md#mem-rte-experience-retrieval
          - memory.md#mem-rte-context-recovery
          - memory.md#mem-obj-agent-messages
          note: Active and Q predicates exclude rows, session expiry blocks restore, and read-state suppresses
            future unread-message delivery.
        - value: routing
          basis: wired
          records:
          - memory.md#mem-rte-experience-retrieval
          - memory.md#mem-rte-project-context
          - memory.md#mem-rte-initiative-memory
          - memory.md#mem-rte-context-recovery
          - memory.md#mem-obj-agent-messages
          - runtime.md#rt-rte-gepa-prompts
          - runtime.md#rt-rte-forgesmith-changes
          note: Retained role/project/initiative/task IDs, dates/status and version/configuration state
            choose scope, source, input window or execution settings.
        records:
        - memory.md#mem-rte-lesson-maintenance
        - memory.md#mem-rte-experience-retrieval
        - memory.md#mem-rte-context-recovery
        - memory.md#mem-obj-agent-messages
        - memory.md#mem-rte-project-context
        - memory.md#mem-rte-initiative-memory
        - runtime.md#rt-rte-gepa-prompts
        - runtime.md#rt-rte-forgesmith-changes
        note: 'Withdrawal is consumer-specific: inactive lessons remain available to explicit MCP queries.'
      - scope: Existing rules and retained performance metadata at candidate/maintenance admission
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-rte-lesson-maintenance
          - epistemic.md#epi-rte-simba-rules
          - runtime.md#rt-rte-gepa-prompts
          - runtime.md#rt-rte-autoresearch-prompts
          note: Existing rule text supplies duplicate criteria; retained performance statistics participate
            in retention/rollback criteria.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-rte-lesson-maintenance
          - epistemic.md#epi-rte-simba-rules
          - runtime.md#rt-rte-gepa-prompts
          - runtime.md#rt-rte-autoresearch-prompts
          note: Candidate duplicate rejection, active-flag pruning and baseline/revert branches have executable
            veto force at their own consumers.
        records:
        - memory.md#mem-rte-lesson-maintenance
        - epistemic.md#epi-rte-simba-rules
        - runtime.md#rt-rte-gepa-prompts
        - runtime.md#rt-rte-autoresearch-prompts
        note: These criteria concern structural/operational admission rather than factual warrant.
      - scope: Explicit MCP returned records at requesting client
        assessment: partial
        findings:
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-rte-memory-queries
          note: Requesters are afforded retained informational content; downstream model incorporation
            is not established.
        records:
        - memory.md#mem-rte-memory-queries
        - epistemic.md#epi-rte-mcp-retrieval
        note: Use the capability-level warrant; the retained handler-status conflict does not license
          a stronger downstream-consumption assertion.
      - scope: Offloaded output, training marker, rubric details and audit-written LITM weights at later
          consumers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-persisted-output
        - epistemic.md#epi-obj-training-marker
        - epistemic.md#epi-rte-rubric-scores
        - epistemic.md#epi-rte-context-reorder
        note: No complete later-consumer/effect path is established for these retained outputs; do not
          infer authority from availability or a numeric name.
      - scope: Remaining included maintenance, plugin, training and provider-owned memory alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lifecycle-hooks
        - epistemic.md#epi-obj-training-marker
        - epistemic.md#epi-rte-rubric-scores
        - runtime.md#rt-rte-forgesmith-changes
        - memory.md#mem-rte-context-recovery
        note: Arbitrary hook/plugin writes, complete optimizer/scoring/evaluation and training consumers,
          and opaque host compaction remain included but incompletely inspected. Setup/migration/sync
          and housekeeping routes lack complete recorded admission/consumer coverage. These alternatives
          cannot inherit the classifications of the inspected routes.
      records:
      - memory.md#mem-bap-experience-context
      - memory.md#mem-rte-experience-retrieval
      - memory.md#mem-rte-context-recovery
      - memory.md#mem-rte-project-context
      - memory.md#mem-rte-initiative-memory
      - memory.md#mem-obj-agent-messages
      - runtime.md#rt-bap-role-instructions
      - runtime.md#rt-rte-forgesmith-changes
      - runtime.md#rt-rte-gepa-prompts
      - runtime.md#rt-rte-autoresearch-prompts
      - memory.md#mem-rte-episode-feedback
      - memory.md#mem-rte-lesson-maintenance
      - epistemic.md#epi-rte-simba-rules
      - memory.md#mem-obj-q-value
      - memory.md#mem-obj-embedding
      - memory.md#mem-obj-lesson-graph-edges
      - memory.md#mem-obj-lessons-learned
      - memory.md#mem-rte-memory-queries
      - epistemic.md#epi-rte-mcp-retrieval
      - memory.md#mem-obj-persisted-output
      - epistemic.md#epi-obj-training-marker
      - epistemic.md#epi-rte-rubric-scores
      - epistemic.md#epi-rte-context-reorder
      - runtime.md#rt-rte-lifecycle-hooks
      note: The inventory distinguishes model-interpreted context/instructions from learning, ranking,
        routing and executable validation/veto consumers. Missing downstream consumers and remaining plugin/optimizer
        routes keep system coverage partial.
    write_agency:
      assessment: partial
      units:
      - scope: Episode admission/reflection replacement and Q updates
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-episode-feedback
          - epistemic.md#epi-rte-episode-values
          note: Parser/sanitizer, fallback-model success/length checks and fixed outcome updates admit
            content without per-item human approval.
        records:
        - memory.md#mem-rte-episode-feedback
        - epistemic.md#epi-rte-episode-values
        note: Starting a task is not approval of its subsequent reflection or Q changes.
      - scope: Template/SIMBA lesson admission, score updates and pruning
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-lesson-maintenance
          - epistemic.md#epi-rte-simba-rules
          note: Software gates store rules and numerical effectiveness or change active state; no per-rule
            human decision is required.
        records:
        - memory.md#mem-rte-lesson-maintenance
        - epistemic.md#epi-rte-simba-rules
        note: Model authorship and physical database I/O are not the admission classification.
      - scope: Hard/soft checkpoint, session capture, deterministic summary and agent-message writes
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-context-recovery
          - memory.md#mem-obj-agent-messages
          - runtime.md#rt-rte-dev-test
          note: Code captures output/state, compacts it and posts failure messages without per-snapshot
            approval.
        records:
        - memory.md#mem-rte-context-recovery
        - memory.md#mem-obj-agent-messages
        - runtime.md#rt-rte-dev-test
        note: Unknown authorship of an input state file does not erase known automatic capture.
      - scope: Initiative outcome appends
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-initiative-memory
          note: Parser/sanitizer and field/count caps admit sibling-task output into a persisted plan.
        records:
        - memory.md#mem-rte-initiative-memory
        note: Initial plan and separate editing control are not settled by this append mechanism.
      - scope: GEPA/autoresearch prompt admission and ForgeSmith automatic configuration or enabled auto-patch
          paths
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-gepa-prompts
          - runtime.md#rt-rte-autoresearch-prompts
          - runtime.md#rt-rte-forgesmith-changes
          note: Software gates select/store/deploy/retain candidate changes on these specific paths.
        records:
        - runtime.md#rt-rte-gepa-prompts
        - runtime.md#rt-rte-autoresearch-prompts
        - runtime.md#rt-rte-forgesmith-changes
        note: ForgeSmith manual-default patch proposals are not silently counted as installed automatic
          patches.
      - scope: Interactive human supply/edit of project context and declared plan editing
        assessment: known
        findings:
        - value: manual
          basis: afforded
          records:
          - memory.md#mem-rte-project-context
          - memory.md#mem-rte-initiative-memory
          note: An explicit human supplying/editing this retained content is an afforded route; it is
            not universal control over all table/file writes.
        records:
        - memory.md#mem-rte-project-context
        - memory.md#mem-rte-initiative-memory
        note: Skill requests and declared editing surface establish a capability, not an observed approved
          entry.
      - scope: Initial project records, state-file content, trusted role overlays and manual-gated patch
          installation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-project-context
        - memory.md#mem-rte-context-recovery
        - runtime.md#rt-rte-role-extension
        - runtime.md#rt-rte-forgesmith-changes
        note: Generic writers/trusted commits and recorded proposals do not establish who made a content-specific
          decision or how a later manual installation occurs.
      - scope: Optional output-file persistence
        assessment: known
        findings:
        - value: automatic
          basis: afforded
          records:
          - memory.md#mem-obj-persisted-output
          note: Helper code admits supplied content under write-once filename policy; no per-content human
            decision is shown.
        records:
        - memory.md#mem-obj-persisted-output
        note: The persistence capability is inspected but enabling callers and reload remain unestablished.
      - scope: Imported training-marker row admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - epistemic.md#epi-obj-training-marker
          note: Required-field/range checks admit and commit a registry row before attempting to move
            the marker.
        records:
        - epistemic.md#epi-obj-training-marker
        note: External training and marker production control remain unresolved.
      - scope: Remaining included maintenance, plugin, training and provider-owned memory alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lifecycle-hooks
        - epistemic.md#epi-obj-training-marker
        - epistemic.md#epi-rte-rubric-scores
        - runtime.md#rt-rte-forgesmith-changes
        - memory.md#mem-rte-context-recovery
        note: Arbitrary hook/plugin writes, complete optimizer/scoring/evaluation and training consumers,
          and opaque host compaction remain included but incompletely inspected. Setup/migration/sync
          and housekeeping routes lack complete recorded admission/consumer coverage. These alternatives
          cannot inherit the classifications of the inspected routes.
      records:
      - memory.md#mem-rte-episode-feedback
      - epistemic.md#epi-rte-episode-values
      - memory.md#mem-rte-lesson-maintenance
      - epistemic.md#epi-rte-simba-rules
      - memory.md#mem-rte-context-recovery
      - memory.md#mem-obj-agent-messages
      - runtime.md#rt-rte-dev-test
      - memory.md#mem-rte-initiative-memory
      - runtime.md#rt-rte-gepa-prompts
      - runtime.md#rt-rte-autoresearch-prompts
      - runtime.md#rt-rte-forgesmith-changes
      - memory.md#mem-rte-project-context
      - memory.md#mem-obj-project-context
      - runtime.md#rt-rte-role-extension
      - memory.md#mem-obj-persisted-output
      - epistemic.md#epi-obj-training-marker
      - runtime.md#rt-rte-lifecycle-hooks
      - epistemic.md#epi-rte-rubric-scores
      note: Known automatic admissions coexist with afforded content-specific human editing. Initial-content
        and alternate admission control stays unresolved; neither generic caller identity nor workflow
        launch establishes manual approval.
    curation_operations:
      assessment: partial
      units:
      - scope: Deterministic continuation/session compaction
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-context-recovery
          note: Selected structured sections, output prefixes and bounded tool metadata reduce retained
            history to continuation context.
        - value: dedup
          basis: wired
          records:
          - memory.md#mem-rte-context-recovery
          note: Recorded code/log compression and deduplication remove repeated retained material.
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-context-recovery
          note: Expiry purge deletes old session rows; truncation/history filtering forgets selected material
            at later consumers.
        records:
        - memory.md#mem-rte-context-recovery
        note: Consolidation retains existing claims within extraction/truncation limits; a faithfulness
          defect would not by itself establish synthesis.
      - scope: Lesson and episode maintenance
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records:
          - memory.md#mem-rte-lesson-maintenance
          - memory.md#mem-rte-experience-retrieval
          note: Rule word-overlap rejection and retrieved lesson deduplication suppress near duplicates.
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-episode-feedback
          - memory.md#mem-rte-lesson-maintenance
          note: Null episode reflection replacement, existing signature counts and Q/effectiveness updates
            revise retained entries.
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-rte-lesson-maintenance
          note: SIMBA active=0 withdraws generic automatic reliance while retaining row history.
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-episode-feedback
          - memory.md#mem-rte-lesson-maintenance
          note: Negative Q increments lower salience/eligibility and pruning suppresses future automatic
            delivery.
        - value: promote
          basis: wired
          records:
          - memory.md#mem-rte-episode-feedback
          - memory.md#mem-rte-lesson-maintenance
          note: Positive Q rewards and recurring-signature frequency increments raise later selection
            salience.
        records:
        - memory.md#mem-rte-episode-feedback
        - memory.md#mem-rte-lesson-maintenance
        - memory.md#mem-rte-experience-retrieval
        note: These are implemented transformations at named consumers. Whole-task rewards and confounded
          rates do not establish usefulness or causal rule improvement.
      - scope: Prompt/configuration maintenance and rollback
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-rte-forgesmith-changes
          - runtime.md#rt-rte-gepa-prompts
          - runtime.md#rt-rte-autoresearch-prompts
          note: Retained configuration/prompt instructions are appended, replaced or versioned for later
            loading.
        - value: invalidate
          basis: wired
          records:
          - runtime.md#rt-rte-gepa-prompts
          note: Rollback marks an evolved prompt reverted and selects baseline while version files remain.
        records:
        - runtime.md#rt-rte-forgesmith-changes
        - runtime.md#rt-rte-gepa-prompts
        - runtime.md#rt-rte-autoresearch-prompts
        note: Autoresearch rewrite/rollback and ForgeSmith append/configuration routes retain their distinct
          gates.
      - scope: SIMBA semantic transformation beyond its duplicate/score gates
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-simba-rules
        - memory.md#mem-rte-lesson-maintenance
        note: Records establish generation requests and structural admission, but actual rules are unavailable
          and semantic relation is indeterminate. Neither synthesize nor consolidation of every generated
          rule can be asserted merely from the command name.
      - scope: Initiative parsed summary/decision append semantic transformation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-initiative-memory
        note: The recorded route admits bounded parsed output. It does not establish whether each agent-authored
          summary adds a claim or only reduces prior retained claims.
      - scope: Remaining included maintenance, plugin, training and provider-owned memory alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lifecycle-hooks
        - epistemic.md#epi-obj-training-marker
        - epistemic.md#epi-rte-rubric-scores
        - runtime.md#rt-rte-forgesmith-changes
        - memory.md#mem-rte-context-recovery
        note: Arbitrary hook/plugin writes, complete optimizer/scoring/evaluation and training consumers,
          and opaque host compaction remain included but incompletely inspected. Setup/migration/sync
          and housekeeping routes lack complete recorded admission/consumer coverage. These alternatives
          cannot inherit the classifications of the inspected routes.
      records:
      - memory.md#mem-rte-context-recovery
      - memory.md#mem-rte-episode-feedback
      - memory.md#mem-rte-lesson-maintenance
      - memory.md#mem-rte-experience-retrieval
      - runtime.md#rt-rte-forgesmith-changes
      - runtime.md#rt-rte-gepa-prompts
      - runtime.md#rt-rte-autoresearch-prompts
      - epistemic.md#epi-rte-simba-rules
      - memory.md#mem-rte-initiative-memory
      - runtime.md#rt-rte-lifecycle-hooks
      - epistemic.md#epi-obj-training-marker
      - epistemic.md#epi-rte-rubric-scores
      note: Recorded consolidation, deduplication, evolution, consumer-specific invalidation and salience
        changes survive semantic uncertainty on model-generated rules. Index construction/acquisition
        alone contributes no curation value; remaining cleanup/optimizer paths are unresolved.
    read_back_direction:
      assessment: partial
      units:
      - scope: Automatic experience, project, initiative, message and recovery delivery
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-experience-retrieval
          - memory.md#mem-rte-project-context
          - memory.md#mem-rte-initiative-memory
          - memory.md#mem-rte-context-recovery
          - memory.md#mem-obj-agent-messages
          note: Orchestrator invocation construction selects retained context without a foreground consumer
            request for those particular memories.
        records:
        - memory.md#mem-rte-experience-retrieval
        - memory.md#mem-rte-project-context
        - memory.md#mem-rte-initiative-memory
        - memory.md#mem-rte-context-recovery
        - memory.md#mem-obj-agent-messages
        note: Each route is conditional on flags, available state and history/budget gates; these conditions
          do not remove the implemented push path.
      - scope: Accumulated role/version and configuration reuse
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-gepa-prompts
          - runtime.md#rt-rte-forgesmith-changes
          - runtime.md#rt-rte-autoresearch-prompts
          - runtime.md#rt-obj-role-prompts
          note: Subsequent assembly/configuration loading automatically supplies installed variants/settings
            to the next task consumer.
        records:
        - runtime.md#rt-rte-gepa-prompts
        - runtime.md#rt-rte-forgesmith-changes
        - runtime.md#rt-rte-autoresearch-prompts
        - runtime.md#rt-obj-role-prompts
        note: Static shipped prompt bytes are excluded; retained edits and version selection are included.
      - scope: Explicit MCP memory queries
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-rte-memory-queries
          note: A client requests a tool/filter and receives the selected retained records.
        records:
        - memory.md#mem-rte-memory-queries
        - epistemic.md#epi-rte-mcp-retrieval
        note: Requested return is pull, not a second push. The handler-status disagreement is retained
          rather than selecting the stronger status.
      - scope: Output-offload files, training registry, rubric/audit artifacts at later consumers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-persisted-output
        - epistemic.md#epi-obj-training-marker
        - epistemic.md#epi-rte-rubric-scores
        - epistemic.md#epi-rte-context-reorder
        note: File pointers and persisted metadata alone do not establish a reload or later-consumer route.
      - scope: Remaining included maintenance, plugin, training and provider-owned memory alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lifecycle-hooks
        - epistemic.md#epi-obj-training-marker
        - epistemic.md#epi-rte-rubric-scores
        - runtime.md#rt-rte-forgesmith-changes
        - memory.md#mem-rte-context-recovery
        note: Arbitrary hook/plugin writes, complete optimizer/scoring/evaluation and training consumers,
          and opaque host compaction remain included but incompletely inspected. Setup/migration/sync
          and housekeeping routes lack complete recorded admission/consumer coverage. These alternatives
          cannot inherit the classifications of the inspected routes.
      records:
      - memory.md#mem-rte-experience-retrieval
      - memory.md#mem-rte-project-context
      - memory.md#mem-rte-initiative-memory
      - memory.md#mem-rte-context-recovery
      - memory.md#mem-obj-agent-messages
      - runtime.md#rt-rte-gepa-prompts
      - runtime.md#rt-rte-forgesmith-changes
      - runtime.md#rt-rte-autoresearch-prompts
      - runtime.md#rt-obj-role-prompts
      - memory.md#mem-rte-memory-queries
      - epistemic.md#epi-rte-mcp-retrieval
      - memory.md#mem-obj-persisted-output
      - epistemic.md#epi-obj-training-marker
      - epistemic.md#epi-rte-rubric-scores
      - epistemic.md#epi-rte-context-reorder
      - runtime.md#rt-rte-lifecycle-hooks
      note: Wired automatic supply and afforded request-driven retrieval are supported separately. Unknown
        reload/consumer/provider alternatives prevent complete direction coverage; the pull witness does
        not make push selection inapplicable.
    read_back_signal:
      assessment: partial
      units:
      - scope: 'Task prompt experience selection: role/project/error matching and availability/budget
          gates'
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-experience-retrieval
          note: 'Trigger: prompt assembly. Exact role/project/error identity predicates select retained
            lesson/episode candidates.'
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-experience-retrieval
          - memory.md#mem-clm-context-budget
          note: 'Trigger: prompt assembly. Active/nonempty/Q eligibility, recency/frequency limits, feature
            flags and prompt budget restrict eligible/delivered retained text.'
        - value: inferred-lexical
          basis: wired
          records:
          - memory.md#mem-rte-experience-retrieval
          note: 'Trigger: episode assembly. Task keywords and retained episode/rule text supply overlap
            relevance boosts.'
        records:
        - memory.md#mem-rte-experience-retrieval
        - memory.md#mem-clm-context-budget
        note: These are separate selectors in one chain, not three descriptions of an identifier on a
          catalog entry.
      - scope: Optional dense and graph episode selectors
        assessment: partial
        findings:
        - value: inferred-embedding
          basis: wired
          records:
          - memory.md#mem-rte-experience-retrieval
          - memory.md#mem-obj-embedding
          - memory.md#mem-obj-lesson-graph-edges
          note: 'Trigger: feature-enabled retrieval. Task/text embeddings and retained vectors supply
            similarity and similarity-derived graph ranking for eligible episodes.'
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-experience-retrieval
          - memory.md#mem-obj-lesson-graph-edges
          note: 'Trigger: feature-enabled graph rerank. Retained co-access adjacency and fixed graph scores
            influence priority independently of a semantic match.'
        records:
        - memory.md#mem-rte-experience-retrieval
        - memory.md#mem-obj-embedding
        - memory.md#mem-obj-lesson-graph-edges
        note: Ordinary telemetry does not forward optional embedding config; alternative vectors/callers
          remain possible. Mixed integer identity spaces and graph-error fallback prevent a complete coherent-semantic-network
          claim.
      - scope: Project history push
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-project-context
          note: 'Trigger: task construction. Project ID matches note/question/decision records delivered
            to that task.'
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-project-context
          note: 'Trigger: task construction. Latest note, unresolved state and five most recent decisions
            select historical context without topical inference.'
        records:
        - memory.md#mem-rte-project-context
        note: Resolved questions and older decisions can leave automatic visibility without deletion.
      - scope: Initiative plan push
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-initiative-memory
          note: 'Trigger: task prompt construction. Task initiative_id selects the retained initiative
            plan from the project path.'
        records:
        - memory.md#mem-rte-initiative-memory
        note: Actual identity matching, not merely a filename returned on explicit request, selects the
          delivered plan.
      - scope: Recovery and inter-agent message push
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-context-recovery
          - memory.md#mem-obj-agent-messages
          - runtime.md#rt-rte-dev-test
          note: 'Trigger: restore/next developer phase. Task/role identities select checkpoints, session
            rows and destination-addressed messages.'
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-context-recovery
          - memory.md#mem-obj-agent-messages
          note: 'Trigger: restore/history formatting. Expiry/latest ordering, bounded unread counts, truncation
            and anti-compaction gating restrict retained material delivered.'
        records:
        - memory.md#mem-rte-context-recovery
        - memory.md#mem-obj-agent-messages
        - runtime.md#rt-rte-dev-test
        note: Session and hard checkpoint can both enter history; delivery is not guaranteed merely because
          storage was loaded.
      - scope: Changed prompt/version supply
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-rte-gepa-prompts
          - runtime.md#rt-obj-role-prompts
          note: 'Trigger: role assembly. Requested role matches its active version/baseline artifacts.'
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-gepa-prompts
          - runtime.md#rt-rte-forgesmith-changes
          - runtime.md#rt-rte-autoresearch-prompts
          note: 'Trigger: later invocation/configuration load. File availability, configured enablement,
            randomized A/B split and rollback statistics choose installed material.'
        records:
        - runtime.md#rt-rte-gepa-prompts
        - runtime.md#rt-rte-forgesmith-changes
        - runtime.md#rt-rte-autoresearch-prompts
        - runtime.md#rt-obj-role-prompts
        note: Performance thresholds/random assignment are coarse selectors, not inferred model judgment
          of current task semantics.
      - scope: Request-driven MCP response selection
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-memory-queries
        note: 'This unit is pull: the caller requests records, so a push-selection signal is inapplicable
          here. It does not make the whole axis inapplicable.'
      - scope: Unknown output reload, metadata consumers and other automatic selectors
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-persisted-output
        - epistemic.md#epi-obj-training-marker
        - epistemic.md#epi-rte-rubric-scores
        - runtime.md#rt-rte-lifecycle-hooks
        - memory.md#mem-rte-context-recovery
        note: No actual selector/delivery fact classifies these included alternatives; opaque host compaction
          and plugin selection remain uninspected.
      records:
      - memory.md#mem-rte-experience-retrieval
      - memory.md#mem-clm-context-budget
      - memory.md#mem-obj-embedding
      - memory.md#mem-obj-lesson-graph-edges
      - memory.md#mem-rte-project-context
      - memory.md#mem-rte-initiative-memory
      - memory.md#mem-rte-context-recovery
      - memory.md#mem-obj-agent-messages
      - runtime.md#rt-rte-dev-test
      - runtime.md#rt-rte-gepa-prompts
      - runtime.md#rt-rte-forgesmith-changes
      - runtime.md#rt-rte-autoresearch-prompts
      - runtime.md#rt-obj-role-prompts
      - memory.md#mem-rte-memory-queries
      - memory.md#mem-obj-persisted-output
      - epistemic.md#epi-obj-training-marker
      - epistemic.md#epi-rte-rubric-scores
      - runtime.md#rt-rte-lifecycle-hooks
      note: Identifier matching, coarse availability/ordering/budget filters, lexical inference and optional
        embedding ranking are positive witnesses. No inferred-judgment value is inferred from the mere
        presence of a model; missing alternative selectors keep the axis partial.
    trace_learning:
      assessment: partial
      units:
      - scope: Post-task episode/reflection and outcome-priority writes with later retrieval
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-episode-feedback
          - epistemic.md#epi-rte-episode-values
          - memory.md#mem-rte-experience-retrieval
          note: Automatic output-derived prose and outcome-derived Q updates persist in SQLite and shape
            later selected task context.
        records:
        - memory.md#mem-rte-episode-feedback
        - epistemic.md#epi-rte-episode-values
        - memory.md#mem-rte-experience-retrieval
        note: Qualifying write/consumer wiring, not observed use or improved capacity.
      - scope: Failure-template and SIMBA lesson/eligibility writes
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-lesson-maintenance
          - epistemic.md#epi-rte-simba-rules
          - memory.md#mem-rte-experience-retrieval
          note: Repeated run failures or episode contrasts feed automatic retained rules and score/pruning
            state consumed by later generic active retrieval.
        records:
        - memory.md#mem-rte-lesson-maintenance
        - epistemic.md#epi-rte-simba-rules
        - memory.md#mem-rte-experience-retrieval
        note: Unknown semantic novelty and causal usefulness do not negate the qualifying trace-fed write.
      - scope: Retained continuation snapshots/session reconstruction and summaries
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-context-recovery
          - memory.md#mem-obj-checkpoints
          - memory.md#mem-obj-soft-checkpoints
          - memory.md#mem-obj-agent-sessions
          note: Automatic session output/tool-state capture and deterministic continuation summaries are
            retained and can reach a later invocation as context.
        records:
        - memory.md#mem-rte-context-recovery
        - memory.md#mem-obj-checkpoints
        - memory.md#mem-obj-soft-checkpoints
        - memory.md#mem-obj-agent-sessions
        note: A generated continuation summary qualifies even within a run. Flags, expiry and history
          gating limit activation, not the existence of the wired route.
      - scope: Sibling-task initiative outcome memory
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-initiative-memory
          note: Automatic task-output parse/sanitized append produces durable sibling-task context with
            a later plan-loading consumer.
        records:
        - memory.md#mem-rte-initiative-memory
        note: Initial operator plan content is a separate unresolved admission branch.
      - scope: Trace-fed prompt/configuration evolution
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-forgesmith-changes
          - runtime.md#rt-rte-gepa-prompts
          - runtime.md#rt-rte-autoresearch-prompts
          note: Run/failure feedback automatically produces admitted standing prompt/configuration changes
            for later execution on the enabled branches.
        records:
        - runtime.md#rt-rte-forgesmith-changes
        - runtime.md#rt-rte-gepa-prompts
        - runtime.md#rt-rte-autoresearch-prompts
        note: Manual-default ForgeSmith patch proposals alone are not an automatic installed update; config
          and separately enabled automatic paths supply the positive.
      - scope: Interactive project entries, raw-message-only retention, embedding initialization and offload/metadata
          routes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-project-context
        - memory.md#mem-obj-agent-messages
        - memory.md#mem-obj-embedding
        - memory.md#mem-obj-persisted-output
        - epistemic.md#epi-obj-training-marker
        - epistemic.md#epi-rte-rubric-scores
        note: Records do not completely establish automatic trace derivation into a durable behavior-shaping
          result on every one of these alternatives. Raw retention alone and imported training claims
          do not prove a qualifying write; insufficient bounded absence evidence prevents a local no.
      - scope: Remaining included maintenance, plugin, training and provider-owned memory alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lifecycle-hooks
        - epistemic.md#epi-obj-training-marker
        - epistemic.md#epi-rte-rubric-scores
        - runtime.md#rt-rte-forgesmith-changes
        - memory.md#mem-rte-context-recovery
        note: Arbitrary hook/plugin writes, complete optimizer/scoring/evaluation and training consumers,
          and opaque host compaction remain included but incompletely inspected. Setup/migration/sync
          and housekeeping routes lack complete recorded admission/consumer coverage. These alternatives
          cannot inherit the classifications of the inspected routes.
      records:
      - memory.md#mem-rte-episode-feedback
      - epistemic.md#epi-rte-episode-values
      - memory.md#mem-rte-experience-retrieval
      - memory.md#mem-rte-lesson-maintenance
      - epistemic.md#epi-rte-simba-rules
      - memory.md#mem-rte-context-recovery
      - memory.md#mem-obj-checkpoints
      - memory.md#mem-obj-soft-checkpoints
      - memory.md#mem-obj-agent-sessions
      - memory.md#mem-rte-initiative-memory
      - runtime.md#rt-rte-forgesmith-changes
      - runtime.md#rt-rte-gepa-prompts
      - runtime.md#rt-rte-autoresearch-prompts
      - memory.md#mem-rte-project-context
      - memory.md#mem-obj-agent-messages
      - memory.md#mem-obj-embedding
      - memory.md#mem-obj-persisted-output
      - epistemic.md#epi-obj-training-marker
      - epistemic.md#epi-rte-rubric-scores
      - runtime.md#rt-rte-lifecycle-hooks
      note: Several automatic trace-fed durable-artifact paths support yes at wired level. No observed
        learning benefit or weight training follows. Unresolved writes prevent a system-wide no or a complete
        all-routes assessment.
    trace_source:
      assessment: partial
      units:
      - scope: Episode/reflection and rule extraction inputs
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-rte-episode-feedback
          - memory.md#mem-rte-lesson-maintenance
          - epistemic.md#epi-rte-simba-rules
          note: Original inputs include recorded task-agent output/reflection and role success/failure
            episode narratives from agent work sessions.
        records:
        - memory.md#mem-rte-episode-feedback
        - memory.md#mem-rte-lesson-maintenance
        - epistemic.md#epi-rte-simba-rules
        note: Host outcomes supply feedback as well; full underlying session/tool provenance is not reconstructed
          from shortened stored prose.
      - scope: Continuation/session recovery input content
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-rte-context-recovery
          - memory.md#mem-obj-checkpoints
          - memory.md#mem-obj-agent-sessions
          note: Recorded agent output and state hints feed summaries and session reconstruction.
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-rte-context-recovery
          - memory.md#mem-obj-agent-sessions
          note: Session capture consumes up to twenty recent tool calls; formatter retains tool name/turn/ok
            rather than complete payloads.
        - value: event-streams
          basis: wired
          records:
          - memory.md#mem-obj-soft-checkpoints
          - memory.md#mem-rte-context-recovery
          note: Soft checkpoints sample streaming turn/compaction counts and signals from runtime activity;
            these runtime events are distinct from the conversational output prefix.
        records:
        - memory.md#mem-rte-context-recovery
        - memory.md#mem-obj-checkpoints
        - memory.md#mem-obj-soft-checkpoints
        - memory.md#mem-obj-agent-sessions
        note: Original state-file content/authorship and opaque host compaction are unresolved; do not
          treat every JSON state field as a known trace origin.
      - scope: Initiative task-outcome append inputs
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-rte-initiative-memory
          note: Agent-authored ORCHESTRATOR_OUTPUT summaries and decisions from sibling-task sessions
            feed the automatic retained append.
        records:
        - memory.md#mem-rte-initiative-memory
        note: The initial plan is not relabeled as an event stream merely because append metadata includes
          task/status fields.
      - scope: Prompt/configuration evolution input content
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records:
          - runtime.md#rt-rte-forgesmith-changes
          - runtime.md#rt-rte-autoresearch-prompts
          - runtime.md#rt-rte-gepa-prompts
          note: Run patterns and recent task failure/output text feed mutation or maintenance proposals
            retained for later task behavior.
        records:
        - runtime.md#rt-rte-forgesmith-changes
        - runtime.md#rt-rte-autoresearch-prompts
        - runtime.md#rt-rte-gepa-prompts
        note: Detailed optimizer inputs, scoring/OPRO internals and complete provenance are not recorded
          well enough to enumerate every original source.
      - scope: Other qualifying or potentially qualifying writes and opaque origins
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-project-context
        - memory.md#mem-obj-embedding
        - epistemic.md#epi-obj-training-marker
        - epistemic.md#epi-rte-rubric-scores
        - runtime.md#rt-rte-lifecycle-hooks
        - memory.md#mem-rte-context-recovery
        note: Interactive summaries, historical embeddings, training utilities, plugins and provider compaction
          lack a completely classified qualifying write/source chain. Neither imported static guidance
          nor a training marker establishes a trace source.
      records:
      - memory.md#mem-rte-episode-feedback
      - memory.md#mem-rte-lesson-maintenance
      - epistemic.md#epi-rte-simba-rules
      - memory.md#mem-rte-context-recovery
      - memory.md#mem-obj-checkpoints
      - memory.md#mem-obj-soft-checkpoints
      - memory.md#mem-obj-agent-sessions
      - memory.md#mem-rte-initiative-memory
      - runtime.md#rt-rte-forgesmith-changes
      - runtime.md#rt-rte-autoresearch-prompts
      - runtime.md#rt-rte-gepa-prompts
      - memory.md#mem-rte-project-context
      - memory.md#mem-obj-embedding
      - epistemic.md#epi-obj-training-marker
      - epistemic.md#epi-rte-rubric-scores
      - runtime.md#rt-rte-lifecycle-hooks
      note: Session-output and recorded-tool inputs are supported, with runtime streaming signals on the
        soft-checkpoint branch. Linked multi-step trajectories are not established by a success/failure
        label. Mixed/opaque inputs prevent a complete source enumeration; source is not inapplicable in
        a boundary with qualifying trace learning.
---

# EQUIPA memory profile

## Comparison rationale

This profile classifies the supplied accepted records, not source files or an incumbent profile. Every axis is partial because the recorded inventory retains material alternatives with missing admission, provenance, transformation or later-consumer facts. A wired finding is implementation-level capacity. It does not establish enabled features, exercised model reliance, semantic faithfulness or benefit.

The reconciliation supersedes the epistemic episode, lesson and Q-value object declarations with [MEM-OBJ-agent-episodes](memory.md#mem-obj-agent-episodes), [MEM-OBJ-lessons-learned](memory.md#mem-obj-lessons-learned) and [MEM-OBJ-q-value](memory.md#mem-obj-q-value). This profile uses those canonical objects; the independently scoped epistemic routes and effectiveness-score part remain valid. No route/container supersession is inferred from overlap.

The retained MCP disagreement concerns implementation status, not query syntax. [MEM-RTE-memory-queries](memory.md#mem-rte-memory-queries) warrants an afforded pull route; [EPI-RTE-mcp-retrieval](epistemic.md#epi-rte-mcp-retrieval) calls its inspected handler wired but does not establish subsequent client incorporation. The profile retains the capability-level pull witness and leaves downstream authority incomplete rather than upgrading it from that handler alone.

SQLite holds text, symbolic scores, dense vectors and graph-edge rows. Those forms do not imply four storage engines. Dense vector similarity supports parametric representation and inferred-embedding selection, not model-weight learning. The configured embedding model and historical vector compatibility remain unresolved in [MEM-OBJ-embedding](memory.md#mem-obj-embedding). Numeric Q/effectiveness and graph IDs remain symbolic at their fixed-rule consumers.

Historical text has knowledge authority at task inference; changed role text has instruction authority. Retained experience has learning authority at the maintenance/derivation consumer, while access fields have ranking, routing or enforced eligibility effects at host code. Existing-rule duplicate criteria and version-performance criteria have validation force at their own admission consumers. These forces are local: [MEM-RTE-lesson-maintenance](memory.md#mem-rte-lesson-maintenance) can withdraw generic injection without revoking the MCP read surface. The source-label and graph-ID qualifications in [MEM-RTE-experience-retrieval](memory.md#mem-rte-experience-retrieval) prevent idealized coherence or usefulness claims, not the recorded positive selectors.

Consolidation is established by deterministic continuation extraction and bounded reconstruction in [MEM-RTE-context-recovery](memory.md#mem-rte-context-recovery). SIMBA's requested synthesis and admitted rule format do not establish semantic novelty. [EPI-RTE-simba-rules](epistemic.md#epi-rte-simba-rules) keeps the content relation indeterminate without actual rule instances. No synthesize value is invented to match its name. Positive Q/frequency changes raise salience; negative changes lower it. Pruning and GEPA reversion retain history while withdrawing reliance. These curation findings do not establish causal improvement.

Automatic write agency is assessed at each admission, not at workflow launch or physical I/O. Known automatic reflection replacement, session reconstruction and initiative appends coexist with unresolved original state-file/plan/table control. Interactive human supplying/editing is only afforded manual admission. ForgeSmith's default manual patch gate does not govern GEPA or autoresearch and does not by itself establish that a proposal was manually installed.

Push signals name actual selectors: task/role/project/initiative matches, coarse state/expiry/budget limits, lexical overlaps and optional dense similarity. An explicit MCP query remains pull, including its requested response. The memory records do not establish an inferred-judgment selector merely because a model generated the stored text. Nor does the existence of an output path establish a later reload.

Automatic trace-fed continuation artifacts qualify alongside cross-task rules and prompt changes. Their later consumers are conditional but wired; full conversation restoration is not. [MEM-RTE-context-recovery](memory.md#mem-rte-context-recovery) retains the history gate, lexical checkpoint ordering and possible simultaneous session/checkpoint inclusion. Recorded session tool metadata supports tool-traces; streaming turn/compaction signals support event-streams only on that sampled runtime-state part. An agent narrative or JSON wrapper is not relabeled as an event stream. Neither training-registry metadata nor inference service use establishes weight training, and no bounded complete absence permits a system-wide trace-learning no.

Source-read log: none. No target source was read to supplement the accepted record set. Missing source facts remain limitations rather than new evidence or record declarations.
