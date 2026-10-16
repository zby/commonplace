---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'SAGE memory comparison: retained functions, access indexes, trace corpora, learned parameters
  and optional completion replay.'
run-id: AAS-2026-10-15-sage-d0de15ae5730-01
source-identity: https://github.com/amazon-science/SAGE
reviewed-boundary: 3c9244e82244abb1adc5467ee601a03ba0f433a0
memory-comparison:
  version: 2
  scope: 'Included: paired rollout functions; continuing evaluation and expert libraries; predefined function/query/vector
    alternatives; access metadata and tensors; raw expert calls and derived supervised corpus; use-updated
    RL/SFT weights and recovery state; optional completion cache. Included unresolved alternatives: provider-side
    retention and uninspected launcher/backend memory behavior. Excluded: static shipped prompts, API
    docs/demonstrations as independent memory, ordinary task-local history without a derived later-consumed
    artifact, upstream environment storage and external training/provider implementation details. Imported
    static content inside qualifying retained corpora remains mixed lineage, not an independently qualifying
    trace.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Paired function dictionaries
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id001
          - runtime.md#rt-obj-skill-libraries
          - runtime.md#rt-rte-skill-install
          note: Per-pair dictionaries survive into the second subtask, then reset.
        records: *id001
        note: The internal route retains code in process memory, not a disk skill library.
      - scope: Evaluation and expert source records and query associations
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id002
          - runtime.md#rt-obj-skill-library-functions
          - memory.md#mem-obj-rollout-functions
          - memory.md#mem-obj-query-list
          note: Continuing agent/scenario lists retain source and task-query metadata.
        - value: files
          basis: wired
          records: *id002
          note: Evaluation JSONL, separately loaded predefined JSONL, expert snapshots and optional predefined
            query metadata are files.
        records: *id002
        note: Query-list output serialization and automatic restart from output are not established; these
          gaps do not change the known physical storage paths.
      - scope: Skill/query access tensors
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id003
          - memory.md#mem-obj-skill-embeddings
          - memory.md#mem-obj-query-embeddings
          note: CPU tensors are the operative access representations.
        - value: files
          basis: wired
          records: *id003
          note: Tensor files are saved and may be loaded from predefined inputs.
        records: *id003
        note: Dense encoding does not establish a vector database; the retained substrate is tensors and
          files.
      - scope: Raw expert logs and derived corpus
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id004
          - memory.md#mem-obj-expert-dataset
          - runtime.md#rt-rte-sft-admission
          note: LM-call JSONL and the normalized dataset JSON retain the trace corpus.
        records: *id004
        note: Dataset persistence is separate from trained weights.
      - scope: RL and SFT parameter retention
        assessment: known
        findings:
        - value: model-weights
          basis: wired
          records: &id005
          - runtime.md#rt-cmp-actor-rollout
          - runtime.md#rt-cmp-sft-model
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-rte-sft-admission
          note: Updates retain behavior-shaping numerical parameters.
        - value: in-memory
          basis: wired
          records: *id005
          note: Training/inference workers hold operative parameters.
        - value: files
          basis: wired
          records: *id005
          note: Actor checkpoints and configured SFT output retain parameters on disk.
        records: *id005
        note: Backend checkpoint correctness and exact artifacts are not established.
      - scope: Optional completion cache
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id006
          - memory.md#mem-obj-llm-calls
          - memory.md#mem-rte-response-cache
          note: Joblib manages external cache files for retained response envelopes.
        records: *id006
        note: The wrapper establishes file-backed caching, not a separately evidenced KV service.
      - scope: Included provider-side retention and alternate launcher/backend-specific memory behavior
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-language-model
        - runtime.md#rt-rte-paired-rollout
        - runtime.md#rt-rte-policy-update
        note: Provider state is opaque; alternate launcher/backend retention is not exhaustively inspected.
          Records do not establish an additional memory inventory or its classification. These alternatives
          cannot be excluded by the inspected paths.
      records:
      - runtime.md#rt-obj-skill-libraries
      - runtime.md#rt-rte-skill-install
      - runtime.md#rt-obj-skill-library-functions
      - memory.md#mem-obj-rollout-functions
      - memory.md#mem-obj-query-list
      - memory.md#mem-obj-skill-embeddings
      - memory.md#mem-obj-query-embeddings
      - memory.md#mem-obj-expert-dataset
      - runtime.md#rt-rte-sft-admission
      - runtime.md#rt-cmp-actor-rollout
      - runtime.md#rt-cmp-sft-model
      - runtime.md#rt-rte-policy-update
      - memory.md#mem-obj-llm-calls
      - memory.md#mem-rte-response-cache
      - runtime.md#rt-cmp-language-model
      - runtime.md#rt-rte-paired-rollout
      note: Inventory covers code, access metadata/tensors, traces, corpus, learned parameters and optional
        response envelopes. Coverage is partial because the included provider/backend alternatives remain
        unresolved; wired findings are capacities, not observed use.
    representational_form:
      assessment: partial
      units:
      - scope: Retained Python and identity/schema parts at fixed-rule consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id007
          - runtime.md#rt-obj-skill-libraries
          - runtime.md#rt-obj-skill-library-functions
          - memory.md#mem-obj-rollout-functions
          - memory.md#mem-obj-query-list
          note: AST extraction, JSON task/name fields and interpreter execution use localized fixed-rule
            structures.
        records: *id007
        note: Executable source and access keys are distinct from their interpreted display.
      - scope: Function documentation/source at the task model
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id008
          - runtime.md#rt-rte-skill-install
          - runtime.md#rt-rte-evaluation-loop
          - memory.md#mem-obj-rollout-functions
          note: The model interprets rendered function descriptions and source as reference/guidance.
        records: *id008
        note: This is the model-consumption path, not a claim that interpreter execution is natural-language
          interpretation.
      - scope: Access vectors
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: &id009
          - memory.md#mem-obj-skill-embeddings
          - memory.md#mem-obj-query-embeddings
          note: Dense distributed representations determine embedding similarity.
        records: *id009
        note: Numerical vectors are not Python payloads.
      - scope: Task-query text at lexical/model consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id010
          - memory.md#mem-obj-query-list
          note: Retained task instructions supply query semantics and lexical ranking input.
        - value: symbolic
          basis: wired
          records: *id010
          note: Whitespace bigram sets and task-ID associations are consumed by fixed selection rules.
        records: *id010
        note: Separate interpretation and lexical/index consumption paths share the same retained query
          object.
      - scope: Trace corpus and completion envelopes
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id011
          - memory.md#mem-obj-expert-dataset
          - memory.md#mem-obj-llm-calls
          - memory.md#mem-rte-response-cache
          note: Retained user/assistant prose and observations reach model interpretation or supervision.
        - value: symbolic
          basis: wired
          records: *id011
          note: JSON envelopes and structured fields are mechanically selected; recorded Python remains
            localized source.
        records: *id011
        note: Prose and structural/source parts remain distinct; tokenization does not make the whole
          corpus parametric.
      - scope: Updated actor and supervised weights
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: &id012
          - runtime.md#rt-cmp-actor-rollout
          - runtime.md#rt-cmp-sft-model
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-rte-sft-admission
          note: Numerical parameters determine later generation distributions.
        records: *id012
        note: Exact learned content and model artifacts are unavailable.
      - scope: Included provider-side retention and alternate launcher/backend-specific memory behavior
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-language-model
        - runtime.md#rt-rte-paired-rollout
        - runtime.md#rt-rte-policy-update
        note: Provider state is opaque; alternate launcher/backend retention is not exhaustively inspected.
          Records do not establish an additional memory inventory or its classification. These alternatives
          cannot be excluded by the inspected paths.
      records:
      - runtime.md#rt-obj-skill-libraries
      - runtime.md#rt-obj-skill-library-functions
      - memory.md#mem-obj-rollout-functions
      - memory.md#mem-obj-query-list
      - runtime.md#rt-rte-skill-install
      - runtime.md#rt-rte-evaluation-loop
      - memory.md#mem-obj-skill-embeddings
      - memory.md#mem-obj-query-embeddings
      - memory.md#mem-obj-expert-dataset
      - memory.md#mem-obj-llm-calls
      - memory.md#mem-rte-response-cache
      - runtime.md#rt-cmp-actor-rollout
      - runtime.md#rt-cmp-sft-model
      - runtime.md#rt-rte-policy-update
      - runtime.md#rt-rte-sft-admission
      - runtime.md#rt-cmp-language-model
      - runtime.md#rt-rte-paired-rollout
      note: Mixed forms are split by operative part or consumption path, not by file extension. Coverage
        is partial because the included provider/backend alternatives remain unresolved; wired findings
        are capacities, not observed use.
    lineage:
      assessment: partial
      units:
      - scope: Generated function retention
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id013
          - runtime.md#rt-obj-skill-libraries
          - runtime.md#rt-obj-skill-library-functions
          - memory.md#mem-obj-rollout-functions
          - runtime.md#rt-rte-skill-install
          - runtime.md#rt-rte-expert-admission
          note: AST extraction selects function/import source from generated action histories.
        records: *id013
        note: This describes generated/extracted entries, not externally supplied initial functions.
      - scope: New task-query associations
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id014
          - memory.md#mem-obj-query-list
          note: Original task instructions enter retained query rows from task inputs.
        records: *id014
        note: Instruction text is not a model-authored summary.
      - scope: New access vectors
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id015
          - memory.md#mem-obj-skill-embeddings
          - memory.md#mem-obj-query-embeddings
          note: Encoders compile retained source or task-instruction text into vectors.
        records: *id015
        note: Encoding provenance is known for newly produced rows, not predefined tensors.
      - scope: Selected expert corpus
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id016
          - memory.md#mem-obj-expert-dataset
          - runtime.md#rt-rte-sft-admission
          note: The live extractor selects last-call messages plus response and normalizes them.
        - value: imported
          basis: wired
          records: *id016
          note: Selected traces can contain imported demonstrations and task inputs.
        records: *id016
        note: Mixed original inputs remain visible; extraction does not imply every token was generated
          experience.
      - scope: Learned parameter changes
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id017
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-rte-sft-admission
          note: Optimization compiles rewards/advantages or supervised targets into updated numerical
            state.
        records: *id017
        note: This classifies subsequent updates, not starting-weight provenance.
      - scope: Cached response admission
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id018
          - memory.md#mem-obj-llm-calls
          - memory.md#mem-rte-response-cache
          note: The cache retains a returned provider envelope rather than authoring its content.
        records: *id018
        note: Provider result is the known immediate origin; hidden generation provenance is unresolved.
      - scope: Predefined functions/query metadata/tensors and initial model weights
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-skill-library-functions
        - memory.md#mem-obj-skill-embeddings
        - memory.md#mem-obj-query-list
        - memory.md#mem-obj-query-embeddings
        - runtime.md#rt-cmp-actor-rollout
        - runtime.md#rt-cmp-sft-model
        note: External preparation, initial authorship and embedding alignment/provenance are not frozen.
          Imported loading does not settle their original derivation.
      - scope: Included provider-side retention and alternate launcher/backend-specific memory behavior
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-language-model
        - runtime.md#rt-rte-paired-rollout
        - runtime.md#rt-rte-policy-update
        note: Provider state is opaque; alternate launcher/backend retention is not exhaustively inspected.
          Records do not establish an additional memory inventory or its classification. These alternatives
          cannot be excluded by the inspected paths.
      records:
      - runtime.md#rt-obj-skill-libraries
      - runtime.md#rt-obj-skill-library-functions
      - memory.md#mem-obj-rollout-functions
      - runtime.md#rt-rte-skill-install
      - runtime.md#rt-rte-expert-admission
      - memory.md#mem-obj-query-list
      - memory.md#mem-obj-skill-embeddings
      - memory.md#mem-obj-query-embeddings
      - memory.md#mem-obj-expert-dataset
      - runtime.md#rt-rte-sft-admission
      - runtime.md#rt-rte-policy-update
      - memory.md#mem-obj-llm-calls
      - memory.md#mem-rte-response-cache
      - runtime.md#rt-cmp-actor-rollout
      - runtime.md#rt-cmp-sft-model
      - runtime.md#rt-cmp-language-model
      - runtime.md#rt-rte-paired-rollout
      note: Known subsequent derivations coexist with unresolved initial provenance. Coverage is partial
        because the included provider/backend alternatives remain unresolved; wired findings are capacities,
        not observed use.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retained source at interpreter and task model
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id019
          - runtime.md#rt-rte-skill-install
          - runtime.md#rt-rte-evaluation-loop
          - memory.md#mem-obj-rollout-functions
          - runtime.md#rt-bap-function-execution
          - runtime.md#rt-bap-function-guidance
          note: Retained executable definitions supply reusable operations to the interpreter; rendered
            source supplies interpreted usage guidance.
        - value: knowledge
          basis: wired
          records: *id019
          note: Function descriptions/source supply reference context to the later task-solving model.
        records: *id019
        note: Execution and advisory model context are separate effects; neither establishes mandatory
          invocation or correctness.
      - scope: Source and query content at retrieval scoring
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id020
          - memory.md#mem-obj-skill-embeddings
          - memory.md#mem-obj-query-embeddings
          - memory.md#mem-obj-query-list
          - runtime.md#rt-rte-evaluation-loop
          note: Function embeddings, query embeddings and retained query text influence relative retrieval
            priority.
        records: *id020
        note: Fixed scoring of retained content is ranking authority, even without trained ranking policy.
      - scope: Task/name/index associations at selectors
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id021
          - runtime.md#rt-obj-skill-library-functions
          - memory.md#mem-obj-query-list
          - runtime.md#rt-rte-evaluation-loop
          note: Task-ID associations and name deduplication determine which retained source reaches the
            next world/prompt.
        records: *id021
        note: Identifier selection is not a semantic correctness check.
      - scope: Raw trajectories and selected corpus at updates
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id022
          - runtime.md#rt-rte-skill-install
          - runtime.md#rt-rte-expert-admission
          - memory.md#mem-obj-expert-dataset
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-rte-sft-admission
          note: Recorded experience and feedback feed durable skill extraction or parameter updates.
        records: *id022
        note: The update consumer has learning authority independently of the output source's downstream
          guidance.
      - scope: Checkpoint tracker and saved training state at resume
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id023
          - runtime.md#rt-rte-policy-update
          note: Latest-iteration tracking/configured checkpoint selection restores numerical/dataloader
            state for continued training.
        records: *id023
        note: Resume selects state; it does not validate model quality.
      - scope: Cached envelope at the agent
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id024
          - memory.md#mem-obj-llm-calls
          - memory.md#mem-rte-response-cache
          note: Replayed assistant content supplies the next response to interpretation/code extraction.
        - value: instruction
          basis: wired
          records: *id024
          note: Cached executable response text can supply instructions to the AppWorld execution consumer.
        records: *id024
        note: This optional replay route is disabled in normal evaluation; cache hits and downstream effects
          are not observed.
      - scope: Included provider-side retention and alternate launcher/backend-specific memory behavior
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-language-model
        - runtime.md#rt-rte-paired-rollout
        - runtime.md#rt-rte-policy-update
        note: Provider state is opaque; alternate launcher/backend retention is not exhaustively inspected.
          Records do not establish an additional memory inventory or its classification. These alternatives
          cannot be excluded by the inspected paths.
      records:
      - runtime.md#rt-rte-skill-install
      - runtime.md#rt-rte-evaluation-loop
      - memory.md#mem-obj-rollout-functions
      - runtime.md#rt-bap-function-execution
      - runtime.md#rt-bap-function-guidance
      - memory.md#mem-obj-skill-embeddings
      - memory.md#mem-obj-query-embeddings
      - memory.md#mem-obj-query-list
      - runtime.md#rt-obj-skill-library-functions
      - runtime.md#rt-rte-expert-admission
      - memory.md#mem-obj-expert-dataset
      - runtime.md#rt-rte-policy-update
      - runtime.md#rt-rte-sft-admission
      - memory.md#mem-obj-llm-calls
      - memory.md#mem-rte-response-cache
      - runtime.md#rt-cmp-language-model
      - runtime.md#rt-rte-paired-rollout
      note: Authority is tied to concrete consumers. Transient failure-marker gates and static prompts
        do not become retained validation/enforcement memory merely because they gate writes. Coverage
        is partial because the included provider/backend alternatives remain unresolved; wired findings
        are capacities, not observed use.
    write_agency:
      assessment: partial
      units:
      - scope: Generated functions, derived indexes, query appends, expert corpus and cache admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id025
          - runtime.md#rt-rte-skill-install
          - runtime.md#rt-rte-evaluation-loop
          - memory.md#mem-obj-rollout-functions
          - memory.md#mem-obj-skill-embeddings
          - memory.md#mem-obj-query-list
          - memory.md#mem-obj-query-embeddings
          - memory.md#mem-obj-expert-dataset
          - memory.md#mem-rte-response-cache
          note: Software extraction, encoder appends, expert gates, normalization and memoization admit
            content without per-content human decisions.
        records: *id025
        note: Launching/configuring these routes does not make their admissions manual.
      - scope: RL and configured SFT updates
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id026
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-rte-sft-admission
          note: Optimizer-driven numerical updates have no per-update human content veto.
        records: *id026
        note: Separate launch prerequisites do not change update agency.
      - scope: Predefined-library preparation and initial weights
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-skill-library-functions
        - memory.md#mem-obj-skill-embeddings
        - memory.md#mem-obj-query-list
        - memory.md#mem-obj-query-embeddings
        - runtime.md#rt-cmp-actor-rollout
        - runtime.md#rt-cmp-sft-model
        note: The content supplier/editor/approver and exact initial artifacts are unknown; loading alone
          establishes no manual admission.
      - scope: Included provider-side retention and alternate launcher/backend-specific memory behavior
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-language-model
        - runtime.md#rt-rte-paired-rollout
        - runtime.md#rt-rte-policy-update
        note: Provider state is opaque; alternate launcher/backend retention is not exhaustively inspected.
          Records do not establish an additional memory inventory or its classification. These alternatives
          cannot be excluded by the inspected paths.
      records:
      - runtime.md#rt-rte-skill-install
      - runtime.md#rt-rte-evaluation-loop
      - memory.md#mem-obj-rollout-functions
      - memory.md#mem-obj-skill-embeddings
      - memory.md#mem-obj-query-list
      - memory.md#mem-obj-query-embeddings
      - memory.md#mem-obj-expert-dataset
      - memory.md#mem-rte-response-cache
      - runtime.md#rt-rte-policy-update
      - runtime.md#rt-rte-sft-admission
      - runtime.md#rt-cmp-sft-model
      - runtime.md#rt-obj-skill-library-functions
      - runtime.md#rt-cmp-actor-rollout
      - runtime.md#rt-cmp-language-model
      - runtime.md#rt-rte-paired-rollout
      note: Write control is classified at each admission mechanism, not from the candidate author or
        physical file I/O. Operator selection of an existing model path is a read choice, not a separately
        established content write/admission mechanism. Coverage is partial because the included provider/backend alternatives remain
        unresolved; wired findings are capacities, not observed use.
    curation_operations:
      assessment: partial
      units:
      - scope: Function extraction/merge over retained action and function histories
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id028
          - runtime.md#rt-obj-skill-libraries
          - runtime.md#rt-obj-skill-library-functions
          - memory.md#mem-obj-rollout-functions
          - runtime.md#rt-rte-skill-install
          - runtime.md#rt-rte-evaluation-loop
          - runtime.md#rt-rte-expert-admission
          - epistemic.md#epi-rte-function-extraction
          note: Selected function/import fragments reduce retained action histories to reusable source.
        - value: evolve
          basis: wired
          records: *id028
          note: Same-name definitions replace existing dictionary/extraction entries.
        records: *id028
        note: Consolidation describes selection of existing source, not guaranteed semantic preservation.
          Same-name replacement supports local revision, not near-duplicate content removal. Delivery
          filtering is not retained-memory curation; append-only evaluation lists are not globally revised
          or withdrawn.
      - scope: Checkpoint retention
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id029
          - runtime.md#rt-rte-policy-update
          note: Configured retention counts/remove-previous behavior remove older checkpoint material.
        records: *id029
        note: This is bounded forgetting of recovery artifacts, not semantic quality decay.
      - scope: Selected supervised corpus
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id030
          - memory.md#mem-obj-expert-dataset
          - runtime.md#rt-rte-sft-admission
          note: The extractor selects a reduced message corpus and normalizes its retained content for
            supervision.
        records: *id030
        note: Truncation/normalization can lose meaning; that defect alone does not establish synthesis.
      - scope: Predefined preparation, cache eviction and numerical-update semantics
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-skill-library-functions
        - memory.md#mem-obj-skill-embeddings
        - memory.md#mem-obj-query-embeddings
        - memory.md#mem-obj-llm-calls
        - memory.md#mem-rte-response-cache
        - runtime.md#rt-rte-policy-update
        - runtime.md#rt-rte-sft-admission
        note: Records do not resolve external preparation/eviction or map numerical optimization to an
          enumerated curation operation. Index construction and primary-key checks alone do not establish
          another operation.
      - scope: Included provider-side retention and alternate launcher/backend-specific memory behavior
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-language-model
        - runtime.md#rt-rte-paired-rollout
        - runtime.md#rt-rte-policy-update
        note: Provider state is opaque; alternate launcher/backend retention is not exhaustively inspected.
          Records do not establish an additional memory inventory or its classification. These alternatives
          cannot be excluded by the inspected paths.
      records:
      - runtime.md#rt-obj-skill-libraries
      - runtime.md#rt-obj-skill-library-functions
      - memory.md#mem-obj-rollout-functions
      - runtime.md#rt-rte-skill-install
      - runtime.md#rt-rte-evaluation-loop
      - runtime.md#rt-rte-expert-admission
      - epistemic.md#epi-rte-function-extraction
      - runtime.md#rt-rte-policy-update
      - memory.md#mem-obj-expert-dataset
      - runtime.md#rt-rte-sft-admission
      - memory.md#mem-obj-skill-embeddings
      - memory.md#mem-obj-query-embeddings
      - memory.md#mem-obj-llm-calls
      - memory.md#mem-rte-response-cache
      - runtime.md#rt-cmp-language-model
      - runtime.md#rt-rte-paired-rollout
      note: Only recorded transformations establish operations; no synthesized new claim, quality promotion
        or coherent library-wide invalidation is established by route labels. Coverage is partial because
        the included provider/backend alternatives remain unresolved; wired findings are capacities, not
        observed use.
    read_back_direction:
      assessment: partial
      units:
      - scope: Task initialization library delivery
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id031
          - runtime.md#rt-rte-skill-install
          - runtime.md#rt-rte-evaluation-loop
          - memory.md#mem-obj-rollout-functions
          note: Initialization automatically selects and supplies paired, evaluation or expert retained
            definitions without a model library request.
        records: *id031
        note: Selection precedes interpreter execution and conditional prompt rendering.
      - scope: Later training generation and automatic resume selection
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id032
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-cmp-actor-rollout
          note: Later inference automatically uses updated weights; auto resume selects available saved
            state.
        records: *id032
        note: No task-model request selects particular learned parameter contents.
      - scope: Explicitly selected SFT/checkpoint load
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id033
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-rte-sft-admission
          note: An operator-configured model/resume path requests retained numerical state for later use.
        records: *id033
        note: The subsequent automatic inference consumption is distinct from the requested load.
      - scope: Predefined constructor loading
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id034
          - runtime.md#rt-rte-evaluation-loop
          - runtime.md#rt-obj-skill-library-functions
          - memory.md#mem-obj-skill-embeddings
          - memory.md#mem-obj-query-list
          - memory.md#mem-obj-query-embeddings
          note: Initialization automatically loads separately located predefined content when present.
        records: *id034
        note: Loading output JSONL on restart is not wired; only the separately located predefined branch
          is classified.
      - scope: Completion cache return
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id035
          - memory.md#mem-rte-response-cache
          note: A later matching completion request can be fulfilled from retained response data.
        records: *id035
        note: Requested return is not an additional push merely because the adapter delivers it.
      - scope: Supervised corpus load
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id036
          - memory.md#mem-obj-expert-dataset
          - runtime.md#rt-rte-sft-admission
          note: The separately launched/configured SFT workflow requests the retained dataset.
        records: *id036
        note: Selection and masking inside training do not turn requested dataset consumption into unsolicited
          delivery.
      - scope: Included provider-side retention and alternate launcher/backend-specific memory behavior
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-language-model
        - runtime.md#rt-rte-paired-rollout
        - runtime.md#rt-rte-policy-update
        note: Provider state is opaque; alternate launcher/backend retention is not exhaustively inspected.
          Records do not establish an additional memory inventory or its classification. These alternatives
          cannot be excluded by the inspected paths.
      records:
      - runtime.md#rt-rte-skill-install
      - runtime.md#rt-rte-evaluation-loop
      - memory.md#mem-obj-rollout-functions
      - runtime.md#rt-rte-policy-update
      - runtime.md#rt-cmp-actor-rollout
      - runtime.md#rt-rte-sft-admission
      - runtime.md#rt-obj-skill-library-functions
      - memory.md#mem-obj-skill-embeddings
      - memory.md#mem-obj-query-list
      - memory.md#mem-obj-query-embeddings
      - memory.md#mem-rte-response-cache
      - memory.md#mem-obj-expert-dataset
      - runtime.md#rt-cmp-language-model
      - runtime.md#rt-rte-paired-rollout
      note: Requests and automatic supply are separated within chains; output persistence alone is not
        an extra read-back route. Coverage is partial because the included provider/backend alternatives
        remain unresolved; wired findings are capacities, not observed use.
    read_back_signal:
      assessment: partial
      units:
      - scope: Paired and expert whole-library push
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id037
          - runtime.md#rt-rte-skill-install
          - memory.md#mem-obj-rollout-functions
          note: Second-task/scenario initialization supplies all available functions in the matching local
            library; no relevance selector targets individual entries.
        records: *id037
        note: 'Trigger: next subtask/task initialization. Input: matching pair/scenario library availability.
          Selected part: all retained source.'
      - scope: Default evaluation source push
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id038
          - runtime.md#rt-rte-evaluation-loop
          - runtime.md#rt-obj-skill-library-functions
          note: Scenario-derived _1/_2 identifier matching against recorded task IDs selects source, followed
            by first-name deduplication.
        records: *id038
        note: 'Trigger: task initialization. Input: scenario identifiers and retained task/name metadata.
          Selected part: matching function records. Matching is substring-based, not equality.'
      - scope: Embedding source push
        assessment: known
        findings:
        - value: inferred-embedding
          basis: wired
          records: &id039
          - memory.md#mem-obj-skill-embeddings
          - memory.md#mem-obj-query-embeddings
          - memory.md#mem-obj-query-list
          - runtime.md#rt-rte-evaluation-loop
          note: Current instruction similarity to retained skill/query vectors selects source through
            ranks and query-to-task associations.
        records: *id039
        note: 'Trigger: task initialization with the alternate retrieval mode. Inputs: current instruction
          and retained vectors. Selected part: ranked function source; skill and query modes use different
          limits.'
      - scope: N-gram source push
        assessment: known
        findings:
        - value: inferred-lexical
          basis: wired
          records: &id040
          - memory.md#mem-obj-query-list
          - runtime.md#rt-rte-evaluation-loop
          note: Bigram Jaccard scores rank retained task queries; top threshold-qualified rows select
            associated function source.
        records: *id040
        note: 'Trigger: n-gram initialization. Input: current instruction and retained queries. Selected
          part: matching task-ID functions with name deduplication.'
      - scope: Automatic weight and checkpoint supply
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id041
          - runtime.md#rt-cmp-actor-rollout
          - runtime.md#rt-rte-policy-update
          note: Later generation uses the active updated parameters; automatic resume uses latest available
            checkpoint rather than task-relevance retrieval.
        records: *id041
        note: 'Trigger: subsequent generation/resume. Input: active state or latest-iteration availability.
          Selected part: whole parameter/checkpoint state.'
      - scope: Predefined whole-file supply
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id042
          - runtime.md#rt-obj-skill-library-functions
          - memory.md#mem-obj-skill-embeddings
          - memory.md#mem-obj-query-list
          - memory.md#mem-obj-query-embeddings
          - runtime.md#rt-rte-evaluation-loop
          note: File existence and configured mode trigger loading the supplied library/index as a whole.
        records: *id042
        note: A filename does not itself establish identifier-targeted selection of individual delivered
          parts.
      - scope: Pull-only cache and supervised dataset operations
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-response-cache
        - memory.md#mem-obj-expert-dataset
        - runtime.md#rt-rte-sft-admission
        note: Push selection signal is inapplicable to these bounded requested returns/loads; no separate
          push is inferred.
      - scope: Included provider-side retention and alternate launcher/backend-specific memory behavior
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-language-model
        - runtime.md#rt-rte-paired-rollout
        - runtime.md#rt-rte-policy-update
        note: Provider state is opaque; alternate launcher/backend retention is not exhaustively inspected.
          Records do not establish an additional memory inventory or its classification. These alternatives
          cannot be excluded by the inspected paths.
      records:
      - runtime.md#rt-rte-skill-install
      - memory.md#mem-obj-rollout-functions
      - runtime.md#rt-rte-evaluation-loop
      - runtime.md#rt-obj-skill-library-functions
      - memory.md#mem-obj-skill-embeddings
      - memory.md#mem-obj-query-embeddings
      - memory.md#mem-obj-query-list
      - runtime.md#rt-cmp-actor-rollout
      - runtime.md#rt-rte-policy-update
      - memory.md#mem-rte-response-cache
      - memory.md#mem-obj-expert-dataset
      - runtime.md#rt-rte-sft-admission
      - runtime.md#rt-cmp-language-model
      - runtime.md#rt-rte-paired-rollout
      note: Signals classify actual push selectors, not catalog identifiers, payload format or requested
        response delivery. Coverage is partial because the included provider/backend alternatives remain
        unresolved; wired findings are capacities, not observed use.
    trace_learning:
      assessment: partial
      units:
      - scope: Paired extracted functions to second-task consumers
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id043
          - runtime.md#rt-obj-skill-libraries
          - runtime.md#rt-rte-skill-install
          note: Automatic extraction from action/execution history retains reusable source supplied to
            a later task interpreter/model.
        records: *id043
        note: Conditional internal route qualifies despite per-rollout lifetime; useful reuse is unobserved.
      - scope: Continuing evaluation and expert function accumulation
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id044
          - runtime.md#rt-obj-skill-library-functions
          - memory.md#mem-obj-rollout-functions
          - runtime.md#rt-rte-evaluation-loop
          - runtime.md#rt-rte-expert-admission
          note: Automatic extraction from retained code histories produces functions for subsequent task
            consumers.
        records: *id044
        note: Current-task failure and imperfect extraction do not erase the wired trace-to-durable-artifact
          chain.
      - scope: RL outcome-fed parameters
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id045
          - runtime.md#rt-rte-policy-update
          - runtime.md#rt-rte-paired-rollout
          - runtime.md#rt-cmp-actor-rollout
          note: Trajectories, task outcomes and reuse counts feed optimizer updates consumed by later
            generation/checkpoint use.
        records: *id045
        note: The shipped two-node launcher cannot reach this route without correcting dataset-reader
          selection.
      - scope: Expert traces to SFT parameters
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id046
          - memory.md#mem-obj-expert-dataset
          - runtime.md#rt-rte-sft-admission
          - runtime.md#rt-cmp-sft-model
          note: Recorded calls become selected supervised examples and configured weights for separately
            selected later inference.
        records: *id046
        note: Configured training and operator-linked later use are not evidence that the pipeline ran
          or improved behavior.
      - scope: Predefined content, opaque initial weights and optional response replay
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-skill-library-functions
        - memory.md#mem-obj-skill-embeddings
        - memory.md#mem-obj-query-list
        - memory.md#mem-obj-query-embeddings
        - runtime.md#rt-cmp-actor-rollout
        - runtime.md#rt-cmp-sft-model
        - memory.md#mem-obj-llm-calls
        - memory.md#mem-rte-response-cache
        note: Predefined derivation is unknown. Memoizing/replaying a completion is established, but records
          do not establish whether that response is trace-derived behavior-shaping material; no system-wide
          no follows.
      - scope: Included provider-side retention and alternate launcher/backend-specific memory behavior
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-language-model
        - runtime.md#rt-rte-paired-rollout
        - runtime.md#rt-rte-policy-update
        note: Provider state is opaque; alternate launcher/backend retention is not exhaustively inspected.
          Records do not establish an additional memory inventory or its classification. These alternatives
          cannot be excluded by the inspected paths.
      records:
      - runtime.md#rt-obj-skill-libraries
      - runtime.md#rt-rte-skill-install
      - runtime.md#rt-obj-skill-library-functions
      - memory.md#mem-obj-rollout-functions
      - runtime.md#rt-rte-evaluation-loop
      - runtime.md#rt-rte-expert-admission
      - runtime.md#rt-rte-policy-update
      - runtime.md#rt-rte-paired-rollout
      - runtime.md#rt-cmp-actor-rollout
      - memory.md#mem-obj-expert-dataset
      - runtime.md#rt-rte-sft-admission
      - runtime.md#rt-cmp-sft-model
      - memory.md#mem-obj-skill-embeddings
      - memory.md#mem-obj-query-list
      - memory.md#mem-obj-query-embeddings
      - memory.md#mem-obj-llm-calls
      - memory.md#mem-rte-response-cache
      - runtime.md#rt-cmp-language-model
      note: The axis uses the automatic trace-fed write definition, not demonstrated capacity improvement.
        Raw logs alone do not qualify. Coverage is partial because the included provider/backend alternatives
        remain unresolved; wired findings are capacities, not observed use.
    trace_source:
      assessment: partial
      units:
      - scope: Paired extraction and RL update experience
        assessment: known
        findings:
        - value: trajectories
          basis: wired
          records: &id047
          - runtime.md#rt-rte-skill-install
          - runtime.md#rt-rte-paired-rollout
          - runtime.md#rt-rte-policy-update
          note: Linked task actions, observations and outcomes supply multi-step training experience.
        - value: tool-traces
          basis: wired
          records: *id047
          note: Generated Python execution and returned AppWorld feedback feed extraction/outcome-driven
            updates.
        records: *id047
        note: Original action/execution experience, not the serialized container name, establishes these
          sources.
      - scope: Evaluation and expert extracted source
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id048
          - runtime.md#rt-obj-skill-library-functions
          - memory.md#mem-obj-rollout-functions
          - runtime.md#rt-rte-evaluation-loop
          - runtime.md#rt-rte-expert-admission
          - workflow.md#wf-rte-failed-code-filter
          note: Retained assistant code histories supply source for automatic extraction.
        - value: tool-traces
          basis: wired
          records: *id048
          note: Execution feedback determines ordinary pruning/admission and expert verification of retained
            candidates.
        records: *id048
        note: These sources characterize the qualifying function-write routes; expert gates and normal
          delayed pruning remain distinct.
      - scope: Expert corpus to supervised weights
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id049
          - memory.md#mem-obj-expert-dataset
          - runtime.md#rt-rte-sft-admission
          note: Recorded conversational messages plus the last assistant response supply supervision.
        - value: tool-traces
          basis: wired
          records: *id049
          note: Recorded execution observations within those messages supply feedback content.
        - value: trajectories
          basis: wired
          records: *id049
          note: Selected task histories contain linked action/observation sequences admitted through scenario
            outcomes.
        records: *id049
        note: Imported task/demonstration text is mixed into this source; wrapping it in LM-call JSON
          does not add event-stream provenance.
      - scope: Initial/predefined material and optional cache replay
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-skill-library-functions
        - memory.md#mem-obj-skill-embeddings
        - memory.md#mem-obj-query-list
        - memory.md#mem-obj-query-embeddings
        - runtime.md#rt-cmp-actor-rollout
        - runtime.md#rt-cmp-sft-model
        - memory.md#mem-obj-llm-calls
        - memory.md#mem-rte-response-cache
        note: No qualifying original trace source is established for these unresolved routes; known trace-learning
          positives elsewhere cannot make this uncertainty inapplicable.
      - scope: Included provider-side retention and alternate launcher/backend-specific memory behavior
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-language-model
        - runtime.md#rt-rte-paired-rollout
        - runtime.md#rt-rte-policy-update
        note: Provider state is opaque; alternate launcher/backend retention is not exhaustively inspected.
          Records do not establish an additional memory inventory or its classification. These alternatives
          cannot be excluded by the inspected paths.
      records:
      - runtime.md#rt-rte-skill-install
      - runtime.md#rt-rte-paired-rollout
      - runtime.md#rt-rte-policy-update
      - runtime.md#rt-obj-skill-library-functions
      - memory.md#mem-obj-rollout-functions
      - runtime.md#rt-rte-evaluation-loop
      - runtime.md#rt-rte-expert-admission
      - workflow.md#wf-rte-failed-code-filter
      - memory.md#mem-obj-expert-dataset
      - runtime.md#rt-rte-sft-admission
      - memory.md#mem-obj-skill-embeddings
      - memory.md#mem-obj-query-list
      - memory.md#mem-obj-query-embeddings
      - runtime.md#rt-cmp-actor-rollout
      - runtime.md#rt-cmp-sft-model
      - memory.md#mem-obj-llm-calls
      - memory.md#mem-rte-response-cache
      - runtime.md#rt-cmp-language-model
      note: Each supported source names original qualifying content. No event-stream classification is
        inferred from a logging envelope. Coverage is partial because the included provider/backend alternatives
        remain unresolved; wired findings are capacities, not observed use.
---

# SAGE memory profile

## Comparison rationale

The profile classifies accepted records, not new source facts. Reconciliation establishes no supersessions: containers, their numerical access parts, expert products and separately isolated route stages remain canonical. The axes preserve these scopes rather than merging every similarly named function list.

The internal training findings are wired capacities, conditional on reaching the AppWorld loader. The shipped two-node configuration instead selects an incompatible Parquet reader; it does not establish launch-to-learning operation. This qualification applies to paired reuse and RL trace learning alike ([RT-RTE-paired-rollout](runtime.md#rt-rte-paired-rollout), [RT-RTE-policy-update](runtime.md#rt-rte-policy-update)). No observed or causal basis is asserted.

Code extraction is consolidation of retained action material even though it can omit bindings or damage a multiline definition. Such faithfulness defects do not establish synthesis. Same-name replacement supports local evolution, but key collisions and first-name delivery filtering do not establish near-duplicate retained-content curation. No `dedup` finding is emitted. Appended evaluation records do not guarantee withdrawal of older entries. Function source is symbolic at the interpreter and interpreted reference/guidance at the model. Numerical access tensors are parametric representations on files/in-memory substrates, not evidence of a vector database ([EPI-RTE-function-extraction](epistemic.md#epi-rte-function-extraction), [RT-OBJ-skill-library-functions](runtime.md#rt-obj-skill-library-functions), [MEM-OBJ-skill-embeddings](memory.md#mem-obj-skill-embeddings)).

Learning authority belongs to trace-consuming update routes; downstream code advice and execution are different authority paths. Trace learning therefore includes extracted reusable code as well as parameters. It asserts no improved competence. The original conversational, execution and trajectory contents remain distinct from imported demonstrations and task text ([RT-RTE-skill-install](runtime.md#rt-rte-skill-install), [MEM-OBJ-rollout-functions](memory.md#mem-obj-rollout-functions), [MEM-OBJ-expert-dataset](memory.md#mem-obj-expert-dataset), [RT-RTE-sft-admission](runtime.md#rt-rte-sft-admission)).

Initialization supplies code without a model retrieval request. Paired/scenario whole-library availability is coarse selection; evaluation's actual task-ID match is identifier selection; alternative vector and query-text scores support embedding and lexical selection. The cache instead fulfills a requested completion, so its argument matching is not classified as push targeting ([RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop), [MEM-OBJ-query-list](memory.md#mem-obj-query-list), [MEM-RTE-response-cache](memory.md#mem-rte-response-cache)).

Every axis remains partial. Unknown predefined preparation, initial weight provenance, provider retention and unread alternate backend behavior cannot inherit a known route's classifications. No absence record supports a blanket trace-learning negative. Predefined load versus output write, missing query-list serialization, and operator selection of the SFT output prevent stronger restart or automatic pipeline conclusions, without erasing wired subsequent transformations ([RT-OBJ-skill-library-functions](runtime.md#rt-obj-skill-library-functions), [MEM-OBJ-query-embeddings](memory.md#mem-obj-query-embeddings), [RT-RTE-sft-admission](runtime.md#rt-rte-sft-admission)). Static context and the API-prediction/retry branch do not independently qualify as accumulated memory ([MEM-RTE-api-context](memory.md#mem-rte-api-context), [EPI-RTE-code-retrial](epistemic.md#epi-rte-code-retrial)).

Operator selection of an existing SFT model path is retained as a requested load, not manual write agency. The accepted records establish neither per-content human approval nor a separate replacement/admission mechanism at that selection edge ([RT-RTE-sft-admission](runtime.md#rt-rte-sft-admission), [RT-CMP-sft-model](runtime.md#rt-cmp-sft-model)).

Recovery comparisons remain incomplete: latest-iteration tracking and saved dataloader state have resume-routing support, but the storage, form and lineage inventories do not separately enumerate all non-parameter recovery parts. The affected axes remain partial; their positive parameter findings do not license complete per-part recovery statistics ([RT-RTE-policy-update](runtime.md#rt-rte-policy-update)).

Source-read log: none. This classification uses only the supplied accepted members and their annotations; no frozen-source ambiguity required a source read.
