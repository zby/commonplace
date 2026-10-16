---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'CrewAI memory comparison: unified memory, knowledge, feedback instructions, continuation
  summaries and execution recovery at the frozen revision.'
run-id: AAS-2026-10-15-crewai-62e53db969a7-01
source-identity: https://github.com/crewAIInc/crewAI
reviewed-boundary: 3da2d4e9932b5f2fa9aa73ea9245e0f8b5c154f8
memory-comparison:
  version: 2
  scope: Retained unified-memory text, metadata and embeddings; acquired knowledge chunks and opaque backend
    access state; training feedback/suggestions; Flow feedback lessons; overflow summaries; task replay
    logs, Flow snapshots/pending feedback and runtime checkpoints, including replaceable providers and
    unresolved file/tool-cache/retrieval-adapter consumers inventoried by the accepted account. Includes
    writes, maintenance and later-consumer routes. Excludes static shipped skills/instructions, ordinary
    untransformed turn/task-context accumulation, generic runtime permissions, model weights not written
    by these routes, remote hosted internals and unrelated application storage. Restored use-derived state
    and compacted summaries remain included despite those exclusions.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: 'Built-in unified-memory content, metadata and embedding fields: LanceDB and Qdrant Edge'
        assessment: known
        findings:
        - value: vector
          basis: wired
          records:
          - memory.md#mem-obj-memory-content
          - memory.md#mem-obj-memory-vector
          note: LanceDB vector fields and Qdrant vector shards retain the records and dense access representations.
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-memory-content
          note: LanceDB filesystem database and Qdrant worker-local/central shard paths are the inspected
            backing storage; this is not a claim of independent plaintext copies.
        records:
        - memory.md#mem-obj-memory-content
        - memory.md#mem-obj-memory-metadata
        - memory.md#mem-obj-memory-vector
        note: Built-in backing objects are identified; merge/deletion and cross-process durability guarantees
          are not implied.
      - scope: Supplied unified-memory backend and process-wide factory replacement
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-content
        note: Backend replacement is explicit; the operative storage behind an arbitrary supplied implementation
          is not inspected.
      - scope: Trained-agent suggestions and raw training files
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-obj-trained-agents
          - runtime.md#rt-rte-crew-training
          note: Pickle files retain suggestions and per-iteration feedback data.
        records:
        - runtime.md#rt-obj-trained-agents
        - runtime.md#rt-rte-crew-training
        note: The training file substrate is separate from provider weights.
      - scope: Overflow summary in executor messages
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - runtime.md#rt-rte-context-summary
          note: Mutable message list retains the replacement summary for the next invocation.
        records:
        - runtime.md#rt-rte-context-summary
        note: Within-run retention is included even without a file write.
      - scope: Default Flow snapshots, pending-feedback rows and task replay outputs
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-flow-state
          - memory.md#mem-rte-output-replay
          note: SQLite retains Flow JSON snapshots/pending feedback and kickoff task outputs.
        records:
        - memory.md#mem-obj-flow-state
        - memory.md#mem-rte-output-replay
        note: Encoding as JSON does not replace the SQLite substrate.
      - scope: Built-in runtime checkpoint providers
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-runtime-state
          - memory.md#mem-rte-checkpoint-restore
          note: Default JsonProvider retains checkpoint files.
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-runtime-state
          - memory.md#mem-rte-checkpoint-restore
          note: A shipped SQLite checkpoint provider is identified; its detailed pruning semantics remain
            uninspected.
        records:
        - memory.md#mem-obj-runtime-state
        - memory.md#mem-rte-checkpoint-restore
        note: Provider substrate identity is recorded despite incomplete implementation coverage of maintenance.
      - scope: Knowledge RAG client and custom knowledge/checkpoint/Flow persistence
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-knowledge-chunks
        - memory.md#mem-obj-flow-state
        - memory.md#mem-rte-checkpoint-restore
        note: Client collections and replaceable providers are recorded, but their underlying retained
          substrate is unresolved. A client call is not enough to infer service-object or vector persistence.
      - scope: Additional file-input, tool-cache and retrieval-adapter retained parts and their later
          consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-tool-dispatch
        - memory.md#mem-rte-memory-recall
        note: The accepted account inventories but does not trace these memory-detail alternatives. Their
          storage substrate cannot be inferred from the general tool/cache route or from unified-memory
          witnesses.
      records:
      - memory.md#mem-obj-memory-content
      - memory.md#mem-obj-memory-metadata
      - memory.md#mem-obj-memory-vector
      - runtime.md#rt-obj-trained-agents
      - runtime.md#rt-rte-crew-training
      - runtime.md#rt-rte-context-summary
      - memory.md#mem-obj-flow-state
      - memory.md#mem-rte-output-replay
      - memory.md#mem-obj-runtime-state
      - memory.md#mem-rte-checkpoint-restore
      - memory.md#mem-obj-knowledge-chunks
      - runtime.md#rt-rte-tool-dispatch
      - memory.md#mem-rte-memory-recall
      note: Built-in retained objects have positive substrate findings. Replaceable providers, knowledge
        persistence and additional adapter/cache surfaces prevent complete coverage; external model weights
        are not use-written memory in this boundary.
    representational_form:
      assessment: partial
      units:
      - scope: Unified-memory statements, fallback blobs, consolidated content and distilled lessons at
          model consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-memory-content
          - epistemic.md#epi-obj-feedback-lessons
          - memory.md#mem-rte-memory-recall
          note: Statements and lesson strings are interpreted as context by encoding, review and foreground
            models.
        records:
        - memory.md#mem-obj-memory-content
        - epistemic.md#epi-obj-feedback-lessons
        - memory.md#mem-rte-memory-recall
        note: This text unit excludes numerical access fields and fixed-rule metadata.
      - scope: Unified-memory metadata at filter/ranker and formatting consumers
        assessment: partial
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-memory-metadata
          - memory.md#mem-rte-memory-recall
          note: IDs, scope, categories, importance, times and privacy fields have fixed filter/ranking
            rules.
        records:
        - memory.md#mem-obj-memory-metadata
        - memory.md#mem-rte-memory-recall
        note: Arbitrary free metadata can also be displayed; its caller-defined values are not completely
          characterized, so the symbolic witness does not classify all metadata payloads.
      - scope: MemoryRecord embedding at vector-search consumer
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-memory-vector
          note: Dense numerical state distributes the access representation across coordinates; it is
            not the encoder weights.
        records:
        - memory.md#mem-obj-memory-vector
        note: The record explicitly identifies a distributed numerical representation and its search consumer.
      - scope: Knowledge text chunks at task model
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-knowledge-chunks
          - memory.md#mem-rte-knowledge-context
          note: Stored textual snippets enter task context.
        records:
        - memory.md#mem-obj-knowledge-chunks
        - memory.md#mem-rte-knowledge-context
        note: Text only; backend embeddings and conversion payloads remain separate.
      - scope: Knowledge backend embeddings and non-string/custom parser payloads
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-knowledge-chunks
        - memory.md#mem-rte-knowledge-context
        note: Backend-generated embedding existence does not establish the complete consumed representation
          or custom-parser alternatives.
      - scope: Training suggestions versus role/evaluation fields
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - runtime.md#rt-obj-trained-agents
          - runtime.md#rt-rte-crew-training
          note: Suggestions are interpreted as imperative prompt instructions.
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-obj-trained-agents
          - runtime.md#rt-rte-crew-training
          note: Role keys and evaluation fields have structured storage and role-selection consumers.
        records:
        - runtime.md#rt-obj-trained-agents
        - runtime.md#rt-rte-crew-training
        note: Distinct parts and consumption paths are named; scores are not assumed to be delivered as
          instructions.
      - scope: Overflow summary text versus message frame
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - runtime.md#rt-rte-context-summary
          note: Merged model summary is read by the next model call.
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-rte-context-summary
          note: System/non-system message roles and attached-file framing control the replacement operation.
        records:
        - runtime.md#rt-rte-context-summary
        note: This covers the inspected replacement frame, not provider-specific hidden payloads.
      - scope: Recovery-state structure and recorded model-visible text
        assessment: partial
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-flow-state
          - memory.md#mem-obj-runtime-state
          - memory.md#mem-rte-output-replay
          - memory.md#mem-rte-checkpoint-restore
          note: JSON fields, task identities and checkpoint entities feed fixed restoration rules.
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-runtime-state
          - memory.md#mem-rte-output-replay
          note: Restored entity messages and raw task outputs can reach later models through resumption/context
            aggregation.
        records:
        - memory.md#mem-obj-flow-state
        - memory.md#mem-obj-runtime-state
        - memory.md#mem-rte-output-replay
        - memory.md#mem-rte-checkpoint-restore
        note: Arbitrary Flow application fields, hidden provider payloads and complete serialization fidelity
          remain unresolved; readable JSON does not classify opaque payloads.
      - scope: Additional file-input, tool-cache and retrieval-adapter retained parts and their later
          consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-tool-dispatch
        - memory.md#mem-rte-memory-recall
        note: The accepted account inventories but does not trace these memory-detail alternatives. Their
          representational form cannot be inferred from the general tool/cache route or from unified-memory
          witnesses.
      records:
      - memory.md#mem-obj-memory-content
      - epistemic.md#epi-obj-feedback-lessons
      - memory.md#mem-rte-memory-recall
      - memory.md#mem-obj-memory-metadata
      - memory.md#mem-obj-memory-vector
      - memory.md#mem-obj-knowledge-chunks
      - memory.md#mem-rte-knowledge-context
      - runtime.md#rt-obj-trained-agents
      - runtime.md#rt-rte-crew-training
      - runtime.md#rt-rte-context-summary
      - memory.md#mem-obj-flow-state
      - memory.md#mem-obj-runtime-state
      - memory.md#mem-rte-output-replay
      - memory.md#mem-rte-checkpoint-restore
      - runtime.md#rt-rte-tool-dispatch
      note: Text, fixed-rule structures and dense numerical access state are separated by consumer. Arbitrary
        metadata, application payloads and provider alternatives keep the inventory partial.
    lineage:
      assessment: partial
      units:
      - scope: Task/standalone extraction, Flow lessons, trained suggestions and overflow summaries
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-rte-memory-encoding
          - memory.md#mem-rte-feedback-lessons
          - runtime.md#rt-rte-crew-training
          - runtime.md#rt-rte-context-summary
          note: Task results, feedback/revisions and message histories feed automatic derived retained
            text; fallback retains raw task content rather than guaranteeing extraction.
        records:
        - memory.md#mem-rte-memory-encoding
        - memory.md#mem-rte-feedback-lessons
        - runtime.md#rt-rte-crew-training
        - runtime.md#rt-rte-context-summary
        note: Classification names these derivation paths only, not truth, human authorship or complete
          original-input provenance.
      - scope: Knowledge strings and configured external source content
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-knowledge-chunks
          - memory.md#mem-rte-knowledge-context
          note: Configured strings/files/external conversions enter as acquired source material, not framework-produced
            findings.
        records:
        - memory.md#mem-obj-knowledge-chunks
        - memory.md#mem-rte-knowledge-context
        note: String slicing is traced; source-specific conversions and provenance preservation for other
          sources remain uninspected.
      - scope: Generated access structures and raw execution-state serialization
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-memory-vector
          - memory.md#mem-obj-memory-metadata
          - memory.md#mem-obj-flow-state
          - memory.md#mem-obj-runtime-state
          - memory.md#mem-rte-output-replay
          note: Embeddings compile text into dense access state; generated IDs/times and recovery serialization
            mechanically construct structured retained state.
        records:
        - memory.md#mem-obj-memory-vector
        - memory.md#mem-obj-memory-metadata
        - memory.md#mem-obj-flow-state
        - memory.md#mem-obj-runtime-state
        - memory.md#mem-rte-output-replay
        note: This covers generated/serialized parts, not arbitrary initial content, supplied metadata
          or opaque entity provenance.
      - scope: Explicit API/tool content, caller metadata and initial/custom-provider state
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-content
        - memory.md#mem-obj-memory-metadata
        - memory.md#mem-rte-memory-maintenance
        - memory.md#mem-obj-runtime-state
        note: Generic caller identity and serialization do not establish authored versus imported provenance
          or the origin of opaque initial payloads. Subsequent transformations do not settle initialization.
      - scope: Additional file-input, tool-cache and retrieval-adapter retained parts and their later
          consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-tool-dispatch
        - memory.md#mem-rte-memory-recall
        note: The accepted account inventories but does not trace these memory-detail alternatives. Their
          lineage cannot be inferred from the general tool/cache route or from unified-memory witnesses.
      records:
      - memory.md#mem-rte-memory-encoding
      - memory.md#mem-rte-feedback-lessons
      - runtime.md#rt-rte-crew-training
      - runtime.md#rt-rte-context-summary
      - memory.md#mem-obj-knowledge-chunks
      - memory.md#mem-rte-knowledge-context
      - memory.md#mem-obj-memory-vector
      - memory.md#mem-obj-memory-metadata
      - memory.md#mem-obj-flow-state
      - memory.md#mem-obj-runtime-state
      - memory.md#mem-rte-output-replay
      - memory.md#mem-obj-memory-content
      - memory.md#mem-rte-memory-maintenance
      - runtime.md#rt-rte-tool-dispatch
      - memory.md#mem-rte-memory-recall
      note: Recorded extraction, import and compilation paths are positive. Initial content control/provenance,
        arbitrary caller payloads and external conversion branches remain unresolved; no authored finding
        is inferred from a public write API.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Recalled memory/knowledge text at task and tool-model consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-bap-memory-context
          - memory.md#mem-rte-knowledge-context
          note: Selected text supplies context/reference to later agent models, without verified truth
            or enforced compliance.
        records:
        - memory.md#mem-bap-memory-context
        - memory.md#mem-rte-knowledge-context
        note: Delivery establishes context authority, not observed semantic influence.
      - scope: Stored text/vectors and metadata at retrieval ranker and selectors
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-memory-vector
          - memory.md#mem-obj-memory-metadata
          - memory.md#mem-rte-memory-recall
          - epistemic.md#epi-rte-memory-selection
          note: Retained embeddings, importance and timestamps influence relative retrieval priority.
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-memory-metadata
          - memory.md#mem-rte-memory-recall
          note: Scopes/categories/time fields select search regions and eligible records.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-memory-metadata
          - memory.md#mem-rte-memory-recall
          note: The private/source predicate excludes nonmatching private records unless overridden; this
            is a local delivery veto, not authenticated isolation.
        records:
        - memory.md#mem-obj-memory-vector
        - memory.md#mem-obj-memory-metadata
        - memory.md#mem-rte-memory-recall
        - epistemic.md#epi-rte-memory-selection
        note: Ranking and selection consumers differ from downstream text interpretation. Consolidation
          can lose source/private fields.
      - scope: Retained old memory content at encoding review/update consumer
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-obj-memory-content
          - memory.md#mem-rte-memory-encoding
          - epistemic.md#epi-rte-consolidation-check
          - epistemic.md#epi-rte-plan-application
          note: Old retained text feeds model consolidation and durable replacement/retention decisions
            affecting later recall.
        records:
        - memory.md#mem-obj-memory-content
        - memory.md#mem-rte-memory-encoding
        - epistemic.md#epi-rte-consolidation-check
        - epistemic.md#epi-rte-plan-application
        note: Learning authority is local to the durable artifact update, not a claim of improved capacity
          or factual acceptance.
      - scope: Recorded training outputs/feedback at evaluator and trained suggestions at later task model
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - runtime.md#rt-rte-crew-training
          note: Retained per-iteration initial/revised outputs and feedback feed persisted behavioral
            suggestions.
        - value: instruction
          basis: wired
          records:
          - runtime.md#rt-rte-crew-training
          - runtime.md#rt-bap-training-instructions
          note: Role-selected suggestions enter later prompts as directions to follow.
        records:
        - runtime.md#rt-rte-crew-training
        - runtime.md#rt-bap-training-instructions
        note: The raw update input and derived instruction output have distinct consumers and forces.
      - scope: Flow feedback and retained lesson content at distillation/pre-review
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-rte-feedback-lessons
          note: Output and feedback feed durable lesson artifacts for later review.
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-rte-feedback-lessons
          - memory.md#mem-bap-feedback-review
          note: Later reviewer receives matched strings as advice for revising current output.
        records:
        - memory.md#mem-rte-feedback-lessons
        - memory.md#mem-bap-feedback-review
        note: The reviewer may receive public non-lessons too. No exclusive lesson lineage or mandatory
          compliance is inferred.
      - scope: History at summary producer and retained summary at next model invocation
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - runtime.md#rt-rte-context-summary
          note: Accumulated history feeds automatic retained continuation-summary production.
        - value: knowledge
          basis: wired
          records:
          - runtime.md#rt-rte-context-summary
          note: The next invocation consumes summary text as continuation context.
        records:
        - runtime.md#rt-rte-context-summary
        note: These are separate update and downstream paths, not provider-weight learning.
      - scope: Replay identities, restored task outputs and runtime/Flow reconstruction fields
        assessment: partial
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-rte-output-replay
          note: Stored task identity is checked against the requested replay task for structural admissibility.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-rte-output-replay
          note: Identity mismatch/ambiguity can refuse replay.
        - value: routing
          basis: wired
          records:
          - memory.md#mem-rte-output-replay
          - memory.md#mem-rte-checkpoint-restore
          - runtime.md#rt-rte-flow-execution
          note: Retained task indices/state select continuation inputs and reconstructed execution state.
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-rte-output-replay
          - memory.md#mem-obj-runtime-state
          note: Prior raw outputs/messages can supply later model context after reconstruction.
        records:
        - memory.md#mem-rte-output-replay
        - memory.md#mem-rte-checkpoint-restore
        - memory.md#mem-obj-runtime-state
        - runtime.md#rt-rte-flow-execution
        note: Arbitrary application fields and opaque checkpoint payloads lack uniform downstream authority.
          Schema code itself is not counted as retained memory.
      - scope: Additional file-input, tool-cache and retrieval-adapter retained parts and their later
          consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-tool-dispatch
        - memory.md#mem-rte-memory-recall
        note: The accepted account inventories but does not trace these memory-detail alternatives. Their
          behavioral authority cannot be inferred from the general tool/cache route or from unified-memory
          witnesses.
      records:
      - memory.md#mem-bap-memory-context
      - memory.md#mem-rte-knowledge-context
      - memory.md#mem-obj-memory-vector
      - memory.md#mem-obj-memory-metadata
      - memory.md#mem-rte-memory-recall
      - epistemic.md#epi-rte-memory-selection
      - memory.md#mem-obj-memory-content
      - memory.md#mem-rte-memory-encoding
      - epistemic.md#epi-rte-consolidation-check
      - epistemic.md#epi-rte-plan-application
      - runtime.md#rt-rte-crew-training
      - runtime.md#rt-bap-training-instructions
      - memory.md#mem-rte-feedback-lessons
      - memory.md#mem-bap-feedback-review
      - runtime.md#rt-rte-context-summary
      - memory.md#mem-rte-output-replay
      - memory.md#mem-rte-checkpoint-restore
      - memory.md#mem-obj-runtime-state
      - runtime.md#rt-rte-flow-execution
      - runtime.md#rt-rte-tool-dispatch
      note: Authority is classified at each actual update, ranking, filter, reconstruction and model consumer.
        Unknown application/provider payloads prevent a system-complete union; configured static skills
        and generic guardrails are excluded from memory authority.
    write_agency:
      assessment: partial
      units:
      - scope: Runtime extraction/encoding, consolidation and generated access fields
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-memory-encoding
          - epistemic.md#epi-rte-plan-application
          - memory.md#mem-obj-memory-vector
          - memory.md#mem-obj-memory-metadata
          note: Software/model decisions admit extracted statements, organizational fields, embeddings
            and consolidation effects without per-content human approval.
        records:
        - memory.md#mem-rte-memory-encoding
        - epistemic.md#epi-rte-plan-application
        - memory.md#mem-obj-memory-vector
        - memory.md#mem-obj-memory-metadata
        note: Starting an execution does not make downstream admission manual.
      - scope: Feedback lesson distillation, training evaluator suggestions and overflow summary replacement
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-feedback-lessons
          - runtime.md#rt-rte-crew-training
          - runtime.md#rt-rte-context-summary
          note: Software admits lessons, evaluator suggestions and replacement summaries; human feedback
            supplies input rather than approval of every derived item.
        records:
        - memory.md#mem-rte-feedback-lessons
        - runtime.md#rt-rte-crew-training
        - runtime.md#rt-rte-context-summary
        note: The inspected admissions are automatic even when human feedback triggers them.
      - scope: Runtime checkpoints, Flow snapshots and replay-log production
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-checkpoint-restore
          - memory.md#mem-obj-flow-state
          - memory.md#mem-rte-output-replay
          note: Event/runtime persistence serializes execution state without a per-field approval decision.
        records:
        - memory.md#mem-rte-checkpoint-restore
        - memory.md#mem-obj-flow-state
        - memory.md#mem-rte-output-replay
        note: A caller choosing a checkpoint/replay target is a read choice, not evidence of manual replacement
          admission.
      - scope: Explicit remember/tool writes, update/forget/reset, configured knowledge sources and initial
          state
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-memory-encoding
        - memory.md#mem-rte-memory-maintenance
        - memory.md#mem-rte-knowledge-context
        - memory.md#mem-obj-flow-state
        - memory.md#mem-obj-runtime-state
        note: Caller supplies or decides content but its human/software identity and per-content approval
          are unresolved. Do not infer manual from API invocation or automatic from physical software
          I/O.
      - scope: Custom-provider admissions, pending-feedback continuation and TUI editing alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-feedback-lessons
        - memory.md#mem-rte-checkpoint-restore
        - memory.md#mem-rte-memory-maintenance
        note: These admission branches are only inventoried or incompletely traced; no per-content control
          classification is available.
      - scope: Additional file-input, tool-cache and retrieval-adapter retained parts and their later
          consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-tool-dispatch
        - memory.md#mem-rte-memory-recall
        note: The accepted account inventories but does not trace these memory-detail alternatives. Their
          write agency cannot be inferred from the general tool/cache route or from unified-memory witnesses.
      records:
      - memory.md#mem-rte-memory-encoding
      - epistemic.md#epi-rte-plan-application
      - memory.md#mem-obj-memory-vector
      - memory.md#mem-obj-memory-metadata
      - memory.md#mem-rte-feedback-lessons
      - runtime.md#rt-rte-crew-training
      - runtime.md#rt-rte-context-summary
      - memory.md#mem-rte-checkpoint-restore
      - memory.md#mem-obj-flow-state
      - memory.md#mem-rte-output-replay
      - memory.md#mem-rte-memory-maintenance
      - memory.md#mem-rte-knowledge-context
      - memory.md#mem-obj-runtime-state
      - runtime.md#rt-rte-tool-dispatch
      - memory.md#mem-rte-memory-recall
      note: Automatic derived and recovery-state admissions are wired. No explicit-human per-content decision
        is established for the generic caller routes, so manual is not asserted; those included mechanisms
        remain unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Unified-memory batch and similar-record encoding transformations
        assessment: partial
        findings:
        - value: dedup
          basis: wired
          records:
          - memory.md#mem-rte-memory-encoding
          note: Embedding near-duplicate rejection drops redundant batch entries.
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-memory-encoding
          - epistemic.md#epi-rte-consolidation-check
          note: New text and retained similar text are compared/compressed into keep/update/insert decisions
            over existing claims.
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-memory-encoding
          - epistemic.md#epi-rte-plan-application
          note: Applied update actions revise existing record content.
        records:
        - memory.md#mem-rte-memory-encoding
        - epistemic.md#epi-rte-consolidation-check
        - epistemic.md#epi-rte-plan-application
        note: Inspected transformations support these operations. Unread analysis fallback branches and
          arbitrary model output semantics prevent a complete operation inventory; a request for novel
          insight is not synthesis evidence.
      - scope: Explicit record update
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-memory-maintenance
          note: Caller update revises retained entry fields/content and re-embeds changed text.
        records:
        - memory.md#mem-rte-memory-maintenance
        note: Physical deletion/reset is withdrawal without retained history, not by itself invalidate
          as defined here.
      - scope: Retained training feedback and working history reduction
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - runtime.md#rt-rte-crew-training
          - runtime.md#rt-rte-context-summary
          note: Evaluator consolidates retained iteration feedback into suggestions; overflow compacts
            retained history into a reduced summary.
        records:
        - runtime.md#rt-rte-crew-training
        - runtime.md#rt-rte-context-summary
        note: This classifies the implemented reduction route, not guaranteed semantic faithfulness.
      - scope: Retrieval recency weighting
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - epistemic.md#epi-rte-memory-selection
          note: Age-dependent decay downweights retained records in composite relevance ranking.
        records:
        - epistemic.md#epi-rte-memory-selection
        note: Decay need not delete records. This is ranking downweighting, not a universal time-to-live.
      - scope: Flow lesson semantic generalization relative to inputs
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-feedback-lessons
        - epistemic.md#epi-obj-feedback-lessons
        note: Distillation requests generalizable lessons, but no instances determine whether the transformation
          only consolidates retained claims or creates a claim absent from inputs.
      - scope: Qdrant merge/delete, custom backends, knowledge source maintenance and SQLite checkpoint
          pruning
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-content
        - memory.md#mem-obj-knowledge-chunks
        - memory.md#mem-rte-memory-maintenance
        - memory.md#mem-rte-checkpoint-restore
        note: Operation inventories and incomplete backend reads do not establish all implemented curation
          transformations. Indexing, primary-key checks and raw serialization alone add no curation value.
      - scope: Additional file-input, tool-cache and retrieval-adapter retained parts and their later
          consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-tool-dispatch
        - memory.md#mem-rte-memory-recall
        note: The accepted account inventories but does not trace these memory-detail alternatives. Their
          curation operations cannot be inferred from the general tool/cache route or from unified-memory
          witnesses.
      records:
      - memory.md#mem-rte-memory-encoding
      - epistemic.md#epi-rte-consolidation-check
      - epistemic.md#epi-rte-plan-application
      - memory.md#mem-rte-memory-maintenance
      - runtime.md#rt-rte-crew-training
      - runtime.md#rt-rte-context-summary
      - epistemic.md#epi-rte-memory-selection
      - memory.md#mem-rte-feedback-lessons
      - epistemic.md#epi-obj-feedback-lessons
      - memory.md#mem-obj-memory-content
      - memory.md#mem-obj-knowledge-chunks
      - memory.md#mem-rte-checkpoint-restore
      - runtime.md#rt-rte-tool-dispatch
      - memory.md#mem-rte-memory-recall
      note: Deduplication, consolidation, revision and age downweighting have local wired witnesses. No
        synthesize, invalidate or promote finding is inferred from route names, deletion or initial importance
        assignment; unresolved transformations prevent a complete list.
    read_back_direction:
      assessment: partial
      units:
      - scope: Unified-memory runtime caller, Search memory and feedback pre-review requests
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-memory-recall
          - memory.md#mem-rte-feedback-lessons
          note: Runtime/tool/reviewer asks recall for retained content, and the recall service fulfills
            that request.
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-memory-recall
          - memory.md#mem-rte-feedback-lessons
          note: Without a foreground model request, task/standalone preparation automatically selects
            and appends memories; feedback pre-review automatically supplies matches to its reviewing
            model.
        records:
        - memory.md#mem-rte-memory-recall
        - memory.md#mem-rte-feedback-lessons
        note: 'Separate operations in each chain: requested recall return is pull, automatic context selection
          for the later model is push. Public API capability alone adds no unnamed consumer.'
      - scope: Knowledge query and task-prompt delivery
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-knowledge-context
          note: Task preparation requests search results from configured knowledge collections.
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-knowledge-context
          note: Runtime supplies selected snippets to the task model without its own retrieval request.
        records:
        - memory.md#mem-rte-knowledge-context
        note: Generated query and prompt injection are distinguished from the storage query response.
      - scope: Trained suggestions and overflow summary delivery
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-crew-training
          - runtime.md#rt-rte-context-summary
          note: Prompt preparation automatically supplies role-selected suggestions; overflow handler
            places the summary in the next invocation frame.
        records:
        - runtime.md#rt-rte-crew-training
        - runtime.md#rt-rte-context-summary
        note: Neither later model explicitly requests this retained content.
      - scope: Explicit checkpoint/replay and Flow UUID restore operations
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-checkpoint-restore
          - memory.md#mem-rte-output-replay
          - runtime.md#rt-rte-flow-execution
          note: Caller/runtime requests a checkpoint, replay target or UUID state and receives reconstruction.
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-output-replay
          - runtime.md#rt-rte-crew-kickoff
          note: During resumed tasks the scheduler supplies selected prior stored outputs to the model
            via task-context aggregation.
        records:
        - memory.md#mem-rte-checkpoint-restore
        - memory.md#mem-rte-output-replay
        - runtime.md#rt-rte-flow-execution
        - runtime.md#rt-rte-crew-kickoff
        note: Pull names requested restoration, not an extra push merely because bytes are returned. Replay
          downstream context selection is a separate operation.
      - scope: Custom storage/callers, provider-specific compaction and pending-feedback application consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-checkpoint-restore
        - memory.md#mem-obj-flow-state
        - runtime.md#rt-rte-context-summary
        - memory.md#mem-rte-knowledge-context
        note: The inspected returns do not establish all later consumers or whether opaque content is
          requested or automatically supplied.
      - scope: Additional file-input, tool-cache and retrieval-adapter retained parts and their later
          consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-tool-dispatch
        - memory.md#mem-rte-memory-recall
        note: The accepted account inventories but does not trace these memory-detail alternatives. Their
          read-back direction cannot be inferred from the general tool/cache route or from unified-memory
          witnesses.
      records:
      - memory.md#mem-rte-memory-recall
      - memory.md#mem-rte-feedback-lessons
      - memory.md#mem-rte-knowledge-context
      - runtime.md#rt-rte-crew-training
      - runtime.md#rt-rte-context-summary
      - memory.md#mem-rte-checkpoint-restore
      - memory.md#mem-rte-output-replay
      - runtime.md#rt-rte-flow-execution
      - runtime.md#rt-rte-crew-kickoff
      - memory.md#mem-obj-flow-state
      - runtime.md#rt-rte-tool-dispatch
      note: Both request fulfillment and automatic supply exist, with operation boundaries stated. Opaque
        downstream consumers and additional cache/adapter paths prevent complete direction coverage.
    read_back_signal:
      assessment: partial
      units:
      - scope: Automatic task/standalone memory and Flow pre-review push
        assessment: known
        findings:
        - value: inferred-embedding
          basis: wired
          records:
          - memory.md#mem-rte-memory-recall
          - memory.md#mem-rte-feedback-lessons
          note: 'Trigger: task/input preparation or eligible pre-review; query text is embedded and selects
            retained records.'
        - value: inferred-judgment
          basis: wired
          records:
          - memory.md#mem-rte-memory-recall
          - memory.md#mem-rte-feedback-lessons
          note: On deep long-query branches the memory LLM analyzes query/scopes/time and exploration
            before selecting delivered records.
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-memory-recall
          - memory.md#mem-obj-memory-metadata
          note: Scope/category/time/privacy eligibility and result/exploration budgets broadly filter
            candidates alongside targeted semantic selection.
        records:
        - memory.md#mem-rte-memory-recall
        - memory.md#mem-rte-feedback-lessons
        - memory.md#mem-obj-memory-metadata
        note: Short-query/shallow paths do not inherit the deep judgment basis. Source/private is a visibility
          predicate, not authenticated lesson identity.
      - scope: Knowledge snippets automatically appended at task preparation
        assessment: partial
        findings:
        - value: inferred-judgment
          basis: wired
          records:
          - memory.md#mem-rte-knowledge-context
          note: Agent generates the search query used to select retained snippets for task prompt injection.
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-knowledge-context
          note: Collection, result limit and score threshold constrain delivered knowledge snippets.
        records:
        - memory.md#mem-rte-knowledge-context
        note: Opaque RAG/custom selector internals and uninspected parsers prevent deciding every signal;
          no embedding or lexical mechanism is inferred solely from the RAG label.
      - scope: Role-keyed trained suggestions automatically appended to task prompt
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-rte-crew-training
          - runtime.md#rt-obj-trained-agents
          note: 'Trigger: task preparation; agent.role matches the stored role key and selects that role''s
            retained suggestions.'
        records:
        - runtime.md#rt-rte-crew-training
        - runtime.md#rt-obj-trained-agents
        note: This is an actual retained-part identity match, not merely an identifier on a requested
          file.
      - scope: Overflow summary supplied to next model invocation
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-context-summary
          note: 'Trigger: overflow; code retains the summary replacement frame wholesale, preserving system/file
            material rather than searching it for a topical match.'
        records:
        - runtime.md#rt-rte-context-summary
        note: The producer uses a model, but model production is not automatically inferred-judgment selection
          among already-retained summaries.
      - scope: Stored replay outputs supplied as later task context
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-output-replay
          - runtime.md#rt-rte-crew-kickoff
          note: Explicit task.context selects named TaskOutputs among reconstructed prior results.
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-output-replay
          - runtime.md#rt-rte-crew-kickoff
          note: Unspecified context supplies accumulated preceding outputs; false context supplies none.
        records:
        - memory.md#mem-rte-output-replay
        - runtime.md#rt-rte-crew-kickoff
        note: This covers downstream scheduler push. Requested checkpoint filenames and UUID reloads alone
          establish no identifier-based push.
      - scope: Opaque restored payload delivery, custom knowledge/provider selectors and pending-feedback
          continuation
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-runtime-state
        - memory.md#mem-obj-flow-state
        - memory.md#mem-rte-checkpoint-restore
        - memory.md#mem-rte-knowledge-context
        note: Requested recovery reads do not reveal all downstream push selectors; mixed direction coverage
          forbids treating these alternatives as pull-only inapplicable.
      - scope: Additional file-input, tool-cache and retrieval-adapter retained parts and their later
          consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-tool-dispatch
        - memory.md#mem-rte-memory-recall
        note: The accepted account inventories but does not trace these memory-detail alternatives. Their
          push selection signals cannot be inferred from the general tool/cache route or from unified-memory
          witnesses.
      records:
      - memory.md#mem-rte-memory-recall
      - memory.md#mem-rte-feedback-lessons
      - memory.md#mem-obj-memory-metadata
      - memory.md#mem-rte-knowledge-context
      - runtime.md#rt-rte-crew-training
      - runtime.md#rt-obj-trained-agents
      - runtime.md#rt-rte-context-summary
      - memory.md#mem-rte-output-replay
      - runtime.md#rt-rte-crew-kickoff
      - memory.md#mem-obj-runtime-state
      - memory.md#mem-obj-flow-state
      - memory.md#mem-rte-checkpoint-restore
      - runtime.md#rt-rte-tool-dispatch
      note: Positive signals belong to named automatic supplies. No inferred-lexical witness is recorded.
        Pull recovery identity matching is not counted as push, and opaque alternatives are retained rather
        than made inapplicable.
    trace_learning:
      assessment: partial
      units:
      - scope: Task/standalone trace extraction and full-input fallback through encoding to later recall
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-memory-encoding
          - memory.md#mem-rte-memory-recall
          note: Automatic task/input-output capture writes statements or raw fallback as retained behavior-shaping
            context, later supplied to agent models.
        records:
        - memory.md#mem-rte-memory-encoding
        - memory.md#mem-rte-memory-recall
        note: The route is wired even when extraction fails into a full-content memory; improvement and
          observed activation are not required or claimed.
      - scope: Crew training feedback to durable suggestions and later role-selected instructions
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-crew-training
          - runtime.md#rt-bap-training-instructions
          note: Initial outputs, feedback and revised outputs automatically yield persisted suggestions
            consumed as later prompt directions.
        records:
        - runtime.md#rt-rte-crew-training
        - runtime.md#rt-bap-training-instructions
        note: Human feedback does not make derived admission manual.
      - scope: Flow feedback distillation to retained lessons and later pre-review
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-feedback-lessons
          - memory.md#mem-bap-feedback-review
          note: Automatic lessons from output/feedback are saved and later consumed by review models.
        records:
        - memory.md#mem-rte-feedback-lessons
        - memory.md#mem-bap-feedback-review
        note: This is the traced learn-enabled branch, not complete pending-feedback continuation coverage.
      - scope: Overflow history to retained continuation summary
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-context-summary
          note: Accumulated session history automatically produces a retained replacement summary delivered
            to the next invocation.
        records:
        - runtime.md#rt-rte-context-summary
        note: Within-run retention meets the continuation-summary rule; provider-weight updates are not
          asserted.
      - scope: Explicit API/tool writes, recovery-state application transformations and custom-provider
          routes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-memory-encoding
        - memory.md#mem-rte-memory-maintenance
        - memory.md#mem-obj-flow-state
        - memory.md#mem-obj-runtime-state
        - memory.md#mem-rte-checkpoint-restore
        note: Generic caller provenance and arbitrary application consumers do not establish whether these
          mechanisms produce qualifying trace-fed artifacts. Raw logs/checkpoint copies alone are insufficient.
      - scope: Pending-feedback async continuation and provider-specific summaries
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-feedback-lessons
        - runtime.md#rt-rte-context-summary
        note: Inspected positive branches do not settle alternate write and later-consumer chains.
      - scope: Additional file-input, tool-cache and retrieval-adapter retained parts and their later
          consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-tool-dispatch
        - memory.md#mem-rte-memory-recall
        note: The accepted account inventories but does not trace these memory-detail alternatives. Their
          trace learning cannot be inferred from the general tool/cache route or from unified-memory witnesses.
      records:
      - memory.md#mem-rte-memory-encoding
      - memory.md#mem-rte-memory-recall
      - runtime.md#rt-rte-crew-training
      - runtime.md#rt-bap-training-instructions
      - memory.md#mem-rte-feedback-lessons
      - memory.md#mem-bap-feedback-review
      - runtime.md#rt-rte-context-summary
      - memory.md#mem-rte-memory-maintenance
      - memory.md#mem-obj-flow-state
      - memory.md#mem-obj-runtime-state
      - memory.md#mem-rte-checkpoint-restore
      - runtime.md#rt-rte-tool-dispatch
      note: Four automatic trace-to-retained-artifact-to-later-consumer chains support yes. No bounded
        absence record establishes a local no, and uninspected writes prevent a system-complete trace-learning
        inventory.
    trace_source:
      assessment: partial
      units:
      - scope: Overflow summary input history
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - runtime.md#rt-rte-context-summary
          note: The summary consumes recorded conversational history from the agent work session.
        - value: tool-traces
          basis: wired
          records:
          - runtime.md#rt-rte-context-summary
          - runtime.md#rt-rte-tool-dispatch
          note: When tools were used, observations accumulated in that history are included in the non-system
            material submitted for summarization.
        records:
        - runtime.md#rt-rte-context-summary
        - runtime.md#rt-rte-tool-dispatch
        note: Conditional tool content is wired by the executor loop; it is not an observed tool-containing
          summary instance.
      - scope: Training initial-output, human-feedback and revised-output sequence
        assessment: known
        findings:
        - value: trajectories
          basis: wired
          records:
          - runtime.md#rt-rte-crew-training
          note: Linked initial task result, feedback and revised result across iterations supply multi-step
            experience to the suggestion evaluator.
        records:
        - runtime.md#rt-rte-crew-training
        note: This names linked input/action/outcome content, not an event-stream inferred from serialization
          or a training label.
      - scope: Task/standalone extraction input blobs and explicit mixed content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-memory-encoding
        - memory.md#mem-rte-memory-recall
        note: Task/role/expected-result/output and caller messages are identified, but the recorded input
          inventories do not completely establish which original content belongs to session-logs, tool-traces,
          event-streams or multi-step trajectories. Task result text alone does not prove included tool
          traces.
      - scope: Flow method output and raw human-feedback lesson input
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-feedback-lessons
        - epistemic.md#epi-obj-feedback-lessons
        note: Method/output/feedback origin is recorded, but arbitrary method bodies and feedback channels
          leave the controlled trace-source classification unresolved; a method name alone does not establish
          event-streams or trajectories.
      - scope: Other possible qualifying writes and opaque alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-flow-state
        - memory.md#mem-obj-runtime-state
        - memory.md#mem-rte-checkpoint-restore
        - memory.md#mem-rte-memory-encoding
        - runtime.md#rt-rte-context-summary
        note: Unresolved write/consumer qualification and opaque payload origins prevent a complete source
          inventory; known positive learning routes cannot make these units inapplicable.
      - scope: Additional file-input, tool-cache and retrieval-adapter retained parts and their later
          consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-tool-dispatch
        - memory.md#mem-rte-memory-recall
        note: The accepted account inventories but does not trace these memory-detail alternatives. Their
          qualifying trace source cannot be inferred from the general tool/cache route or from unified-memory
          witnesses.
      records:
      - runtime.md#rt-rte-context-summary
      - runtime.md#rt-rte-tool-dispatch
      - runtime.md#rt-rte-crew-training
      - memory.md#mem-rte-memory-encoding
      - memory.md#mem-rte-memory-recall
      - memory.md#mem-rte-feedback-lessons
      - epistemic.md#epi-obj-feedback-lessons
      - memory.md#mem-obj-flow-state
      - memory.md#mem-obj-runtime-state
      - memory.md#mem-rte-checkpoint-restore
      note: Sources are assigned from original content, not adapter roles. Session history/tool observations
        and linked training experience have positive witnesses; mixed task blobs, Flow feedback origins
        and uninspected qualifying alternatives keep this axis partial.
---

# CrewAI memory profile

## Comparison rationale

All positive findings are implementation-wired classifications, not observations of operation or benefit. Axis coverage is partial because the accepted inventory names unresolved providers, application payloads and additional adapter/cache consumers. Local known units classify only their named objects or mechanisms; they do not establish a complete system-wide value list. The inventory and limits come from [MEM-OBJ-memory-content](memory.md#mem-obj-memory-content), [MEM-OBJ-knowledge-chunks](memory.md#mem-obj-knowledge-chunks), [MEM-OBJ-flow-state](memory.md#mem-obj-flow-state), [MEM-OBJ-runtime-state](memory.md#mem-obj-runtime-state) and their route records.

Text, dense access representations and symbolic controls are separate operative parts. Dense embeddings count as parametric form without claiming weight learning. JSON is an encoding, not a substrate: Flow/replay storage is SQLite, default checkpoints are files, and knowledge client persistence remains unresolved. A provider API does not by itself establish service-object persistence. See [MEM-OBJ-memory-vector](memory.md#mem-obj-memory-vector), [MEM-RTE-output-replay](memory.md#mem-rte-output-replay) and [MEM-RTE-checkpoint-restore](memory.md#mem-rte-checkpoint-restore).

Request fulfillment and automatic model-context supply are different operations in a read-back chain. Runtime recall is pull at the recall service; task preparation is push at the later model. Model-requested Search memory remains pull. Role matching really selects retained training suggestions, whereas an explicitly requested checkpoint location alone establishes no identifier-based push. Replay has a separate downstream task-context selection after requested restoration. See [MEM-RTE-memory-recall](memory.md#mem-rte-memory-recall), [RT-RTE-crew-training](runtime.md#rt-rte-crew-training), [MEM-RTE-output-replay](memory.md#mem-rte-output-replay) and [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff).

Learning authority at an update consumer is separated from knowledge or instruction authority at the output consumer. Retained old text can shape consolidation; recorded training feedback shapes suggestions; the latter become imperative directions. Summary history shapes a replacement artifact that later supplies continuation context. These pathways satisfy the trace-learning write-route definition without demonstrating improved capacity, truthful extraction or provider-parameter updates. See [EPI-RTE-consolidation-check](epistemic.md#epi-rte-consolidation-check), [EPI-RTE-plan-application](epistemic.md#epi-rte-plan-application), [RT-RTE-crew-training](runtime.md#rt-rte-crew-training) and [RT-RTE-context-summary](runtime.md#rt-rte-context-summary).

Curation follows implemented transformations. Recency weighting supports decay; record update supports evolve; physical deletion without retained history does not establish invalidate. Extraction/consolidation labels do not prove synthesis of a new claim. The semantic relation of generalized Flow lessons remains unresolved without instances. See [EPI-RTE-memory-selection](epistemic.md#epi-rte-memory-selection), [MEM-RTE-memory-maintenance](memory.md#mem-rte-memory-maintenance), [MEM-RTE-memory-encoding](memory.md#mem-rte-memory-encoding) and [MEM-RTE-feedback-lessons](memory.md#mem-rte-feedback-lessons).

Privacy filtering supplies a bounded enforced veto on delivery, not authenticated tenancy or an invariant through update. Consolidation reconstruction can lose source/private values. Feedback pre-review may therefore consume public non-lessons as well as retained lessons; source is not an exclusive lineage selector. See [MEM-OBJ-memory-metadata](memory.md#mem-obj-memory-metadata), [MEM-CLM-retention-limits](memory.md#mem-clm-retention-limits) and [MEM-RTE-feedback-lessons](memory.md#mem-rte-feedback-lessons).

Canonical resolution follows the supplied reconciliation: the superseded epistemic memory-content declaration resolves to [MEM-OBJ-memory-content](memory.md#mem-obj-memory-content), and the superseded epistemic feedback route resolves to [MEM-RTE-feedback-lessons](memory.md#mem-rte-feedback-lessons). Neither amendment upgrades evidence or removes opaque alternatives. The epistemic consolidation, selection and mutation stages remain valid distinct parts rather than superseded duplicates. Their narrower warrants are retained locally.

No source reads were needed or performed. All classifications use the supplied accepted records and their passages; no new records, source evidence, quotations, execution results or complete-value assertion are introduced.
