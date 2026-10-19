---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Autogenesis memory comparison: resident history and summaries, disk plans and corpora, recovery/evaluation records, and unresolved external histories and training consumers."
run-id: AAS-2026-10-19-autogenesis-05936a4e4c3b-01
source-identity: https://github.com/DVampire/Autogenesis
reviewed-boundary: "5b070d5cd497e951a188a01409138e8b530eaf4a"
memory-comparison:
  version: 2
  scope: >-
    Use-accumulated lifecycle history, compacted summaries, session displays,
    todo plans, conversation/chat/feedback records, named knowledge corpora,
    execution snapshots and trajectories, workflow checkpoints and evaluations,
    and changed capability artifacts with their version/access metadata.
    Includes the Astra/Mem0 history alternatives and unresolved downstream
    training, process and arbitrary workspace-recall paths recorded by the
    analysts. Excludes unchanged shipped prompts/skills, ordinary transient
    invocation state with no later consumer, external gitlink internals, and
    provider model weights not established as memory changed through these routes.
    Memory machinery source/configuration is distinguished from its session contents.
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: Resident recent records, working summaries, todo cache, trajectory objects and memory configuration/history dictionaries
          assessment: known
          findings:
            - value: in-memory
              basis: wired
              records: [memory.md#mem-obj-recent-history, memory.md#mem-obj-working-memory, memory.md#mem-obj-todo-files, memory.md#mem-obj-execution-records, memory.md#mem-obj-memory-config]
              note: Python deques, dictionaries and cached objects hold these operative parts; config serialization omits live instances.
          records: [memory.md#mem-obj-recent-history, memory.md#mem-obj-working-memory, memory.md#mem-obj-todo-files, memory.md#mem-obj-execution-records, memory.md#mem-obj-memory-config]
          note: These named resident parts are classified independently of their disk projections.
        - scope: Session displays, todo files, conversation events, corpus/manifest, snapshots/trajectory files, workflow checkpoints/evaluations and capability archives
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-memory-display, memory.md#mem-obj-todo-files, memory.md#mem-obj-conversation-events, memory.md#mem-obj-knowledge-corpus, memory.md#mem-obj-execution-records, epistemic.md#epi-obj-checkpoint, epistemic.md#epi-obj-evaluation, runtime.md#rt-obj-extension-manifest]
              note: Named JSON, JSONL, Markdown, HTML and archived-source paths are file storage, not relational or vector databases merely because some fields are numerical.
          records: [memory.md#mem-obj-memory-display, memory.md#mem-obj-todo-files, memory.md#mem-obj-conversation-events, memory.md#mem-obj-knowledge-corpus, memory.md#mem-obj-execution-records, epistemic.md#epi-obj-checkpoint, epistemic.md#epi-obj-evaluation, runtime.md#rt-obj-extension-manifest]
          note: Disk retention is wired; this does not imply every persisted part is reloaded by a model consumer.
        - scope: External plugin history payload/storage and untraced workspace/process/training retention
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-plugin-history, memory.md#mem-obj-execution-records, memory.md#mem-rte-corpus-retrieval]
          note: Adapter names do not resolve external storage implementation; records leave downstream training and arbitrary upstream/downstream payload storage unresolved. Mem0's inspected adapter is a stub.
      records: [memory.md#mem-obj-recent-history, memory.md#mem-obj-memory-display, memory.md#mem-obj-plugin-history, memory.md#mem-obj-execution-records, epistemic.md#epi-obj-checkpoint, epistemic.md#epi-obj-evaluation, runtime.md#rt-obj-extension-manifest]
      note: Files and resident memory are supported, but opaque external and untraced retained parts prevent complete substrate coverage. No vector substrate is inferred from lexical ranking.
    representational_form:
      assessment: partial
      units:
        - scope: Recent-history content, working summaries, todo prose, corpus text, conversational messages and readable execution snapshots
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-recent-history, memory.md#mem-obj-working-memory, memory.md#mem-obj-todo-files, memory.md#mem-obj-knowledge-corpus, memory.md#mem-obj-conversation-events, memory.md#mem-obj-execution-records]
              note: These textual parts supply interpreted assertions, history or plans; stringified payloads do not establish semantic fidelity.
          records: [memory.md#mem-obj-recent-history, memory.md#mem-obj-working-memory, memory.md#mem-obj-todo-files, memory.md#mem-obj-knowledge-corpus, memory.md#mem-obj-conversation-events, memory.md#mem-obj-execution-records]
          note: Classification concerns the named readable text parts, not every arbitrary nested payload.
        - scope: Identity/status envelopes, plan steps, corpus backend metadata, configuration/version maps, generated executable machinery, workflow checkpoint/evaluation fields
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-memory-config, memory.md#mem-obj-memory-display, memory.md#mem-obj-todo-files, memory.md#mem-obj-knowledge-corpus, memory.md#mem-rte-memory-admission, runtime.md#rt-obj-extension-manifest, epistemic.md#epi-obj-checkpoint, epistemic.md#epi-obj-evaluation]
              note: Localized fields and executable source have fixed software consumers. Numeric scores and sparse lexical statistics are not distributed model weights.
          records: [memory.md#mem-obj-memory-config, memory.md#mem-obj-memory-display, memory.md#mem-obj-todo-files, memory.md#mem-obj-knowledge-corpus, memory.md#mem-rte-memory-admission, runtime.md#rt-obj-extension-manifest, epistemic.md#epi-obj-checkpoint, epistemic.md#epi-obj-evaluation]
          note: Structural parts are separate from prose within the same files and from resident session content.
        - scope: Changed skill instruction bodies when subsequently returned to a calling agent
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [runtime.md#rt-obj-skill-content, runtime.md#rt-rte-skill-delivery, runtime.md#rt-rte-extension-admission]
              note: Registered instruction text can be replaced and retrieved; this finding covers the instruction consumer, not unchanged shipped method text as learned memory.
          records: [runtime.md#rt-obj-skill-content, runtime.md#rt-rte-skill-delivery, runtime.md#rt-rte-extension-admission]
          note: Later instruction delivery is distinct from executable Python dispatch.
        - scope: Opaque provider payloads and untraced training/process/workspace consumers
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-plugin-history, memory.md#mem-obj-execution-records, runtime.md#rt-cmp-model-manager]
          note: Readable adapter messages and snapshots do not reveal provider internals or establish learned parameters downstream of exports.
      records: [memory.md#mem-obj-working-memory, memory.md#mem-obj-knowledge-corpus, memory.md#mem-obj-plugin-history, memory.md#mem-obj-execution-records, runtime.md#rt-rte-extension-admission, epistemic.md#epi-obj-checkpoint]
      note: Natural-language and symbolic parts are supported; unknown alternatives cannot be resolved by the readable displays. External inference weights alone do not add parametric memory here.
    lineage:
      assessment: partial
      units:
        - scope: Lifecycle projections, compacted summaries, session displays, snapshots, trajectories and automatically recorded workflow execution fields
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [memory.md#mem-obj-recent-history, memory.md#mem-obj-working-memory, memory.md#mem-obj-memory-display, memory.md#mem-obj-execution-records, epistemic.md#epi-obj-checkpoint, epistemic.md#epi-rte-workflow-evaluation]
              note: Immediate derivation is from lifecycle/execution activity, including summary condensation and run-derived evaluation metrics; this says nothing about original truth or authorship of tool-returned content.
          records: [memory.md#mem-obj-recent-history, memory.md#mem-obj-working-memory, memory.md#mem-obj-memory-display, memory.md#mem-obj-execution-records, epistemic.md#epi-obj-checkpoint, epistemic.md#epi-rte-workflow-evaluation]
          note: Known immediate derivation paths do not classify ultimate source provenance, which remains a separate unresolved unit.
        - scope: Model-authored todo plans and generated/optimized capability source or instructions
          assessment: known
          findings:
            - value: authored
              basis: wired
              records: [memory.md#mem-obj-todo-files, memory.md#mem-rte-todo-context, memory.md#mem-rte-memory-admission, runtime.md#rt-rte-extension-admission]
              note: Foreground models supply plan assertions and authoring workers propose changed source; authorship is independent of admission control.
          records: [memory.md#mem-obj-todo-files, memory.md#mem-rte-todo-context, memory.md#mem-rte-memory-admission, runtime.md#rt-rte-extension-admission]
          note: Covers the evidenced authoring routes, not every caller-supplied initial plan or restored artifact.
        - scope: Corpus document admission from caller payloads
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [epistemic.md#epi-rte-corpus-ingest, memory.md#mem-rte-corpus-retrieval]
              note: Ingestion preserves/coerces supplied documents into a retained base without establishing their upstream warrant.
          records: [epistemic.md#epi-rte-corpus-ingest, memory.md#mem-rte-corpus-retrieval]
          note: Import is the immediate path; corpus authorship is unresolved separately.
        - scope: Initial caller content, nested external tool/document provenance, chat feedback, external histories, restored/generated artifact provenance and untraced process/training derivations
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-recent-history, memory.md#mem-obj-conversation-events, memory.md#mem-obj-plugin-history, memory.md#mem-obj-knowledge-corpus, memory.md#mem-obj-execution-records, runtime.md#rt-rte-extension-admission]
          note: Generic caller identity, raw labels and archive presence do not determine these origins or show which route produced a particular instance.
      records: [memory.md#mem-rte-history-compaction, memory.md#mem-rte-todo-context, epistemic.md#epi-rte-corpus-ingest, memory.md#mem-obj-plugin-history, runtime.md#rt-rte-extension-admission]
      note: Supported derivation paths coexist with unknown initial and external provenance; no complete lineage union is asserted.
    behavioral_authority:
      assessment: partial
      units:
        - scope: History and summaries delivered as memory_context to later foreground model calls
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [memory.md#mem-rte-tiered-context, memory.md#mem-bap-memory-context]
              note: Selected history supplies context, not verified facts or enforced action.
          records: [memory.md#mem-rte-tiered-context, memory.md#mem-bap-memory-context]
          note: Delivery establishes this context force, not observed reliance or benefit.
        - scope: Retained history and prior summary consumed by the automatic compact-model update
          assessment: known
          findings:
            - value: learning
              basis: wired
              records: [memory.md#mem-rte-history-compaction, memory.md#mem-obj-working-memory]
              note: Experience feeds an automatic durable summary update whose output reaches later agent decisions; improved capacity is not established.
          records: [memory.md#mem-rte-history-compaction, memory.md#mem-obj-working-memory]
          note: This is the update consumer, distinct from the output's knowledge authority.
        - scope: Todo plan text at subsequent agent context builds and changed skill bodies returned to calling agents
          assessment: known
          findings:
            - value: instruction
              basis: wired
              records: [memory.md#mem-rte-todo-context, memory.md#mem-bap-memory-context, runtime.md#rt-rte-skill-delivery, runtime.md#rt-bap-method-instructions]
              note: Plans and methods supply directions through interpreted text; completed-step assertions are not correctness certificates.
          records: [memory.md#mem-rte-todo-context, memory.md#mem-bap-memory-context, runtime.md#rt-rte-skill-delivery, runtime.md#rt-bap-method-instructions]
          note: Instruction force does not imply compliance or human approval.
        - scope: Corpus text at lexical ranker and selected document records returned to workflow caller
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [memory.md#mem-obj-knowledge-corpus, epistemic.md#epi-rte-corpus-retrieve]
              note: Retained text determines relative BM25/TF-IDF relevance scores even though the ranking algorithm is fixed.
            - value: knowledge
              basis: wired
              records: [memory.md#mem-rte-corpus-retrieval, epistemic.md#epi-rte-corpus-retrieve]
              note: Retrieved document fields provide reference candidates in workflow result data; later model consumption requires authored payload mapping.
          records: [memory.md#mem-obj-knowledge-corpus, memory.md#mem-rte-corpus-retrieval, epistemic.md#epi-rte-corpus-retrieve]
          note: These two consumers/effects are kept as separate findings; neither score nor delivery endorses truth.
        - scope: Capability-version metadata and workflow checkpoint state at reload/resume consumers
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [runtime.md#rt-obj-extension-manifest, runtime.md#rt-rte-extension-admission, runtime.md#rt-rte-workflow-execution, epistemic.md#epi-obj-checkpoint]
              note: Version/file and checkpoint fields select restored artifacts and continuation/cache state.
            - value: validation
              basis: wired
              records: [runtime.md#rt-rte-workflow-execution, epistemic.md#epi-obj-checkpoint]
              note: Retained workflow identity/runtime version and nonempty prior hash participate in resume compatibility checks.
            - value: enforcement
              basis: wired
              records: [runtime.md#rt-rte-workflow-execution, epistemic.md#epi-obj-checkpoint]
              note: Mismatching checked identity/hash fields refuse restore; hashless migration does not verify original executable identity.
          records: [runtime.md#rt-obj-extension-manifest, runtime.md#rt-rte-extension-admission, runtime.md#rt-rte-workflow-execution, epistemic.md#epi-obj-checkpoint]
          note: Each force belongs to its named reload or guard consumer, not every archived payload or restore branch.
        - scope: Retained workflow evaluation run IDs at duplicate-evidence admission and evaluation records at health-summary caller
          assessment: known
          findings:
            - value: validation
              basis: wired
              records: [epistemic.md#epi-rte-workflow-evaluation]
              note: Existing run IDs are an admissibility criterion for another evaluation record.
            - value: enforcement
              basis: wired
              records: [epistemic.md#epi-rte-workflow-evaluation]
              note: A duplicate retained run ID causes rejection before another record is stored.
            - value: knowledge
              basis: wired
              records: [epistemic.md#epi-rte-workflow-evaluation]
              note: Current-version records supply an advisory aggregate/healthy result, not automatic rollback or verified task quality.
          records: [epistemic.md#epi-rte-workflow-evaluation]
          note: Admission veto and later advisory summary are distinct consumers of retained evaluation fields.
        - scope: External histories, feedback/training exports, arbitrary workspace/process consumers and semantic force of particular generated executable artifacts
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-plugin-history, memory.md#mem-obj-conversation-events, memory.md#mem-obj-execution-records, runtime.md#rt-bap-capability-load, memory.md#mem-rte-memory-admission]
          note: Export/display/admission alone does not establish these later behavioral consumers; memory-class registration can leave the live instance null. Executable availability alone does not identify a more specific controlled force for every generated artifact.
      records: [memory.md#mem-bap-memory-context, memory.md#mem-rte-history-compaction, epistemic.md#epi-rte-corpus-retrieve, runtime.md#rt-rte-workflow-execution, epistemic.md#epi-rte-workflow-evaluation, memory.md#mem-obj-plugin-history]
      note: Supported forces are consumer-specific. Client-visible replay and persisted display alone are not evidence of model recall; unresolved downstream uses prevent complete coverage.
    write_agency:
      assessment: partial
      units:
        - scope: Lifecycle projection, overflow-summary admission, model-selected todo mutations, normalized corpus admission, event persistence, workflow checkpoint/evaluation admission and generator finalizer registration
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-rte-tiered-context, memory.md#mem-rte-history-compaction, memory.md#mem-rte-todo-context, memory.md#mem-rte-corpus-retrieval, memory.md#mem-rte-conversation-replay, runtime.md#rt-rte-workflow-execution, epistemic.md#epi-rte-workflow-evaluation, runtime.md#rt-rte-extension-admission]
              note: Software/model gates decide these admissions without a required per-content human decision; a user starting a task does not make them manual.
          records: [memory.md#mem-rte-tiered-context, memory.md#mem-rte-history-compaction, memory.md#mem-rte-todo-context, memory.md#mem-rte-corpus-retrieval, memory.md#mem-rte-conversation-replay, runtime.md#rt-rte-workflow-execution, epistemic.md#epi-rte-workflow-evaluation, runtime.md#rt-rte-extension-admission]
          note: Classification is the evidenced software admission mechanism, not the unknown authorship of all incoming content.
        - scope: Initial caller-supplied documents/plans/chat/feedback, explicit source replacement/promotion/restore, direct configuration updates and provider-history admissions
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-conversation-events, memory.md#mem-rte-todo-context, memory.md#mem-rte-corpus-retrieval, memory.md#mem-obj-memory-config, memory.md#mem-obj-plugin-history, runtime.md#rt-rte-extension-admission, runtime.md#rt-rte-workflow-execution]
          note: Generic caller identity does not establish a human per-content decision. Explicit command availability and prompt requests for approval cannot establish manual admission or resolve all alternative controls.
      records: [memory.md#mem-rte-history-compaction, memory.md#mem-rte-memory-admission, memory.md#mem-rte-todo-context, memory.md#mem-obj-plugin-history, runtime.md#rt-rte-extension-admission]
      note: Automatic routes are supported, but manual control is not established for unresolved alternatives; no manual finding is inferred from API invocation or workflow launch.
    curation_operations:
      assessment: partial
      units:
        - scope: Overflow compaction of recent records into working summaries
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [memory.md#mem-rte-history-compaction, epistemic.md#epi-rte-history-compact, epistemic.md#epi-rte-summary-retain]
              note: Selected old history is condensed into retained replacement summary text. This operation does not require proof of semantic fidelity or novel knowledge.
          records: [memory.md#mem-rte-history-compaction, epistemic.md#epi-rte-history-compact, epistemic.md#epi-rte-summary-retain]
          note: Model summarization is wired; exact semantic relation of an unobserved input/output pair remains unresolved without adding synthesize.
        - scope: Bounded working-summary deque and resident-session LRU eviction
          assessment: known
          findings:
            - value: decay
              basis: wired
              records: [memory.md#mem-obj-working-memory, memory.md#mem-rte-tiered-context, memory.md#mem-abs-tiered-reload]
              note: Old summaries are discarded and evicted sessions lose resident recall; disk display persistence does not provide built-in rehydration.
          records: [memory.md#mem-obj-working-memory, memory.md#mem-rte-tiered-context, memory.md#mem-abs-tiered-reload]
          note: This is forgetting, not a relevance-dependent learned decay policy.
        - scope: Todo mutation and clearing of completed plan entries
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [memory.md#mem-rte-todo-context]
              note: Update/complete revise retained plan entries and rewrite their files.
            - value: decay
              basis: wired
              records: [memory.md#mem-rte-todo-context]
              note: Clear removes completed entries rather than preserving them as current plan content.
          records: [memory.md#mem-rte-todo-context]
          note: Model/caller-selected edits are not automatic evidence of trace-fed learning or independent success verification.
        - scope: Workflow evaluation current-version filtering
          assessment: known
          findings:
            - value: invalidate
              basis: wired
              records: [epistemic.md#epi-rte-workflow-evaluation]
              note: Older-version records remain retained but are excluded from the active-version health summary.
          records: [epistemic.md#epi-rte-workflow-evaluation]
          note: This withdraws current reliance by version, not factual refutation of the older evaluations.
        - scope: Generated optimizer replacement of retained capability source
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [runtime.md#rt-rte-extension-admission, memory.md#mem-rte-memory-admission]
              note: Optimizer finalization can replace registered source while archives retain previous versions; changed memory source need not supply a live instance.
          records: [runtime.md#rt-rte-extension-admission, memory.md#mem-rte-memory-admission]
          note: Artifact revision is classified independently of improvement, state migration or successful later activation.
        - scope: External history transformations, upstream corpus/process transforms and downstream training/workspace maintenance
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-plugin-history, memory.md#mem-rte-corpus-retrieval, memory.md#mem-obj-execution-records]
          note: Opaque or untraced transformations cannot establish more operations. Corpus append/ranker rebuild and duplicate-ID rejection alone do not establish deduplication.
      records: [memory.md#mem-rte-history-compaction, memory.md#mem-rte-tiered-context, memory.md#mem-rte-todo-context, epistemic.md#epi-rte-workflow-evaluation, runtime.md#rt-rte-extension-admission, memory.md#mem-obj-plugin-history]
      note: Consolidation, forgetting, revision and version-based withdrawal are supported locally. No synthesis is inferred from possible summary error, and staging promotion is not itself promotion of memory salience.
    read_back_direction:
      assessment: partial
      units:
        - scope: Agent get requests, conversation reopen requests, corpus queries, workflow/evaluation reload requests and changed-skill or archived-capability retrieval
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [memory.md#mem-rte-tiered-context, memory.md#mem-rte-conversation-replay, memory.md#mem-rte-corpus-retrieval, runtime.md#rt-rte-workflow-execution, epistemic.md#epi-rte-workflow-evaluation, runtime.md#rt-rte-skill-delivery, runtime.md#rt-rte-extension-admission]
              note: Each fulfills an actual consumer request for retained material. Automatic delivery of the requested result is not an additional push.
          records: [memory.md#mem-rte-tiered-context, memory.md#mem-rte-conversation-replay, memory.md#mem-rte-corpus-retrieval, runtime.md#rt-rte-workflow-execution, epistemic.md#epi-rte-workflow-evaluation, runtime.md#rt-rte-skill-delivery, runtime.md#rt-rte-extension-admission]
          note: Tiered get is a resident-state pull, not disk recovery; client transcript replay is a different consumer.
        - scope: Todo supply during context construction and prior-history/summary supply to overflow-triggered compaction
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [memory.md#mem-rte-todo-context, memory.md#mem-rte-history-compaction]
              note: Context-build code supplies the same-ID plan without a model plan-read request; overflow code independently selects old records and previous summary for the summarizer.
          records: [memory.md#mem-rte-todo-context, memory.md#mem-rte-history-compaction]
          note: The later foreground get that reads the resulting summary remains pull; it is not converted to push by its automatic producer.
        - scope: External plugin deployment/consumer graphs, feedback/training consumers and arbitrary workspace/process recall
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-plugin-history, memory.md#mem-obj-conversation-events, memory.md#mem-obj-execution-records, memory.md#mem-rte-corpus-retrieval]
          note: Adapter get/export capability alone does not establish a later consumer route or its direction. Mem0's stub is not a working retrieval alternative.
      records: [memory.md#mem-rte-tiered-context, memory.md#mem-rte-todo-context, memory.md#mem-rte-history-compaction, memory.md#mem-rte-corpus-retrieval, memory.md#mem-obj-plugin-history]
      note: Both requested retrieval and independent automatic supply exist; unresolved consumers prevent a complete direction inventory.
    read_back_signal:
      assessment: partial
      units:
        - scope: Todo plan push into each same-context agent prompt
          assessment: known
          findings:
            - value: identifier
              basis: wired
              records: [memory.md#mem-rte-todo-context, memory.md#mem-obj-todo-files]
              note: Trigger is context construction; ctx.id selects the sanitized plan filename whose full Markdown is delivered as todo context. This identity actually selects supplied content, not merely a catalog label.
          records: [memory.md#mem-rte-todo-context, memory.md#mem-obj-todo-files]
          note: No task-similarity selector or explicit read budget is recorded for this push.
        - scope: Overflow-triggered supply of chronological records and immediately preceding summary to compact model
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [memory.md#mem-rte-history-compaction, memory.md#mem-obj-working-memory]
              note: recent_max overflow triggers oldest compact_chunk selection plus the most recent previous summary; chronological counts select parts, not inferred topic relevance.
          records: [memory.md#mem-rte-history-compaction, memory.md#mem-obj-working-memory]
          note: Session ownership confines this operation, but the recorded delivered-part selector is the chronological chunk/last-summary rule.
        - scope: Request-only get, transcript, corpus, skill, archive and workflow/evaluation retrieval chains
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-rte-tiered-context, memory.md#mem-rte-conversation-replay, memory.md#mem-rte-corpus-retrieval, runtime.md#rt-rte-skill-delivery, runtime.md#rt-rte-extension-admission, runtime.md#rt-rte-workflow-execution, epistemic.md#epi-rte-workflow-evaluation]
          note: These named operations fulfill requests rather than push material. Lexical corpus ranking is a selector on pull, so it does not establish inferred-lexical push.
        - scope: Unresolved external history, feedback/training and workspace/process delivery alternatives
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-plugin-history, memory.md#mem-obj-conversation-events, memory.md#mem-obj-execution-records, memory.md#mem-rte-corpus-retrieval]
          note: Missing later consumers prevent determining direction and therefore push signals; known pull routes cannot make these alternatives inapplicable.
      records: [memory.md#mem-rte-todo-context, memory.md#mem-rte-history-compaction, memory.md#mem-rte-corpus-retrieval, memory.md#mem-obj-plugin-history, memory.md#mem-obj-execution-records]
      note: Identifier and coarse push are supported; neither corpus BM25 nor an identifier on a requested file adds another push signal. Unresolved alternatives remain included.
    trace_learning:
      assessment: partial
      units:
        - scope: Automatic overflow summary production, retention and later foreground/summarizer consumption
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-rte-history-compaction, memory.md#mem-rte-tiered-context, memory.md#mem-obj-working-memory, epistemic.md#epi-rte-summary-retain]
              note: Lifecycle experience automatically produces retained behavior-shaping text delivered on later model invocations. Within-process persistence and serialized summaries suffice; restart reload and outcome improvement are not prerequisites.
          records: [memory.md#mem-rte-history-compaction, memory.md#mem-rte-tiered-context, memory.md#mem-obj-working-memory, epistemic.md#epi-rte-summary-retain]
          note: Qualifying wiring is complete for this route even though fidelity, actual reliance and benefit are unobserved.
        - scope: Feedback/trajectory training successors, provider-history transformations, possible trace-fed capability revision and upstream/downstream process/workspace alternatives
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-conversation-events, memory.md#mem-obj-execution-records, memory.md#mem-obj-plugin-history, memory.md#mem-rte-corpus-retrieval, runtime.md#rt-rte-extension-admission, runtime.md#rt-cmp-model-manager]
          note: Logs, rewards, SFT/RL exports, improvement instructions and inference calls alone do not establish a trace-fed write-to-later-consumer chain for these alternatives. Their missing consumers/control or opaque implementations prevent positive or negative classification.
      records: [memory.md#mem-rte-history-compaction, epistemic.md#epi-rte-summary-retain, memory.md#mem-obj-execution-records, memory.md#mem-obj-plugin-history, runtime.md#rt-rte-extension-admission]
      note: A wired yes survives in the derived system union with partial inventory coverage. No local no is asserted because the accepted absence record concerns tiered reload, not absence of qualifying trace learning.
    trace_source:
      assessment: partial
      units:
        - scope: Original lifecycle activity and action-result content feeding overflow summaries
          assessment: partial
          findings:
            - value: event-streams
              basis: wired
              records: [memory.md#mem-obj-recent-history, memory.md#mem-rte-tiered-context, memory.md#mem-rte-history-compaction]
              note: Selected agent-start/end and runtime lifecycle callbacks record activity that is formatted into the compacted history; this is not inferred merely from a storage adapter label.
            - value: tool-traces
              basis: wired
              records: [memory.md#mem-obj-recent-history, memory.md#mem-rte-history-compaction]
              note: Recorded tool/skill requests or results, failures and action feedback are among the actual summary inputs.
          records: [memory.md#mem-obj-recent-history, memory.md#mem-rte-tiered-context, memory.md#mem-rte-history-compaction]
          note: The input mix also contains task text, child/environment outputs and explicit notes with unresolved original provenance. These findings do not classify all embedded content as runtime events or establish session-log or trajectory inputs.
        - scope: Sources of unresolved feedback/training, provider, process/workspace and capability-revision learning alternatives
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-execution-records, memory.md#mem-obj-conversation-events, memory.md#mem-obj-plugin-history, memory.md#mem-rte-corpus-retrieval, runtime.md#rt-rte-extension-admission]
          note: No qualifying downstream update is established for these alternatives. Trajectory export does not by itself license a trajectories source finding, nor does chat feedback storage license session-logs learning.
      records: [memory.md#mem-obj-recent-history, memory.md#mem-rte-history-compaction, memory.md#mem-obj-execution-records, memory.md#mem-obj-plugin-history, runtime.md#rt-rte-extension-admission]
      note: The summary route supports event-streams and tool-traces, but mixed origin and unresolved alternative updates prevent complete source coverage; this axis is not inapplicable.
---

# Autogenesis memory profile

## Comparison rationale

The profile covers retained content and its access structures, not every file or permission in the enclosing runtime. The main supported learning route is [MEM-RTE-history-compaction](memory.md#mem-rte-history-compaction): projected lifecycle records become model-written summaries, and later calls consume those summaries. Its wired trace-learning value does not claim improved capacity, faithful summarization, exercised reliance or causal benefit. The raw-history update consumer has learning authority; the summary's later foreground consumer has knowledge authority. These are separate paths rather than an implication from storage to learning.

The summaries' file representation does not repair the resident-state horizon. [MEM-ABS-tiered-reload](memory.md#mem-abs-tiered-reload) establishes a bounded reload absence, not a trace-learning negative. Todo reload, client transcript replay and workflow continuation retain their separate consumers and horizons. A display heading such as “Confirmed constraints” adds no verification force and does not classify an opaque model checkpoint: [MEM-OBJ-memory-display](memory.md#mem-obj-memory-display) is a readable persistence view distinct from get selection.

Requested get delivery is pull. The automatic same-ID todo supply is push, with an actual filename identity match selecting delivered plan text. The overflow summarizer receives a code-selected oldest chunk and prior summary without a foreground request, so that supply is coarse push. Corpus lexical ranking occurs on a requested route; it supports ranking authority but not inferred-lexical push. These distinctions follow [MEM-RTE-tiered-context](memory.md#mem-rte-tiered-context), [MEM-RTE-todo-context](memory.md#mem-rte-todo-context), [MEM-RTE-history-compaction](memory.md#mem-rte-history-compaction) and [EPI-RTE-corpus-retrieve](epistemic.md#epi-rte-corpus-retrieve).

Consolidation describes the implemented summary transformation. The epistemic overlay leaves the exact semantic relation indeterminate without an input/output pair, which does not erase the consolidation wiring or add synthesis. Nonempty-output admission is not a fidelity check. Summary eviction is forgetting; current-version evaluation filtering withdraws current reliance while retaining older records. The latter is separate from duplicate-run rejection, which supplies a validation criterion and enforcing veto rather than deduplication of stored content: [EPI-RTE-summary-retain](epistemic.md#epi-rte-summary-retain), [EPI-RTE-workflow-evaluation](epistemic.md#epi-rte-workflow-evaluation).

Changed capability artifacts and access metadata are retained separately from the session content they might manage. Supported active consumers can use restored or replaced artifacts; memory-class registration alone leaves instance null. No value above upgrades that branch to usable context delivery. Likewise, requested user approval and model-authored source do not establish manual admission: [RT-RTE-extension-admission](runtime.md#rt-rte-extension-admission), [MEM-RTE-memory-admission](memory.md#mem-rte-memory-admission). Checkpoint validation/enforcement is branch-specific: unequal nonempty hashes reject; hashless migration can reuse cached work without verifying its original executable identity, as recorded in [EPI-OBJ-checkpoint](epistemic.md#epi-obj-checkpoint).

Reconciliation supersedes the epistemic working-memory object with [MEM-OBJ-working-memory](memory.md#mem-obj-working-memory), and the epistemic corpus object with [MEM-OBJ-knowledge-corpus](memory.md#mem-obj-knowledge-corpus). Those canonical objects are used here. The narrower epistemic compaction/retention and ingestion/retrieval routes remain valid parts, not superseded duplicates. No other supersession changes a value.

All ten axes retain incomplete coverage. In particular, external Astra history storage/transformations, Mem0's nonoperational adapter, feedback consumers, downstream trajectory training, initial caller control and untraced process/workspace routes cannot be filled in from names or exports. The supported summary-route yes therefore coexists with unresolved learning alternatives; no system-wide no is derived. [MEM-OBJ-plugin-history](memory.md#mem-obj-plugin-history), [MEM-OBJ-execution-records](memory.md#mem-obj-execution-records), [MEM-OBJ-conversation-events](memory.md#mem-obj-conversation-events) and [MEM-RTE-corpus-retrieval](memory.md#mem-rte-corpus-retrieval) retain those limits.

Source-read log: none. This profile uses only the supplied accepted records and reconciliation; it adds no source quotations, analyst records or new evidence.
