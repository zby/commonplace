---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'OpenRSI memory profile: retained search experience, selected training examples, numerical
  updates and generated Gym context at the frozen release.'
run-id: AAS-2026-10-14-openrsi-c72dec9967a3-01
source-identity: https://github.com/FrontisAI/OpenRSI
reviewed-boundary: 71ae803a035d5e3b78c19fa49ed9f67d0550cbaa
memory-comparison:
  version: 2
  scope: 'Included: Evo retained journal/cards/board/summary caches and targeted or legacy consumers;
    RL/SFT program databases, derived metadata, selected alignment examples and trained state; Gym use-generated
    inventory, descriptions, retry feedback, executable task artifacts and persisted reports. Included
    unresolved alternatives: other vendored/database copies, other RL algorithms, NatureBench context,
    metadata/tool-admission branches, sandbox operational stores, initial corpora/checkpoints and upstream
    RL training. Excluded from memory classification: unchanged shipped prompts/skills, ordinary transient
    coordination state, raw external datasets without a later memory consumer, and inference-provider
    weights not shown to change through use. Training initialization remains included as unresolved provenance,
    not silently excluded.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Evo journal, experience cards and rich summaries
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-journal
          - memory.md#mem-obj-experience-card
          - memory.md#mem-obj-rich-summary
          note: Journal JSONL, card/board JSON and separate node-ID summary cache persist on the filesystem.
        - value: in-memory
          basis: wired
          records: *id001
          note: Python nodes, attached dictionaries and journal relations retain the same parts during
            search.
        records: *id001
        note: These are separate persistence forms; they are not one lossless checkpoint.
      - scope: RL and SFT retained program databases
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records: &id002
          - memory.md#mem-obj-rl-program
          - memory.md#mem-obj-sft-program
          note: Distinct SQL program stores retain code, feedback and control metadata.
        records: *id002
        note: RL snapshots copy the SQLite file; encoding and snapshot transport do not create a graph
          or vector substrate.
      - scope: SFT alignment conversations and manifests; generated Gym task context and metric
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id003
          - memory.md#mem-obj-alignment-dataset
          - runtime.md#rt-rte-gym-build
          - runtime.md#rt-obj-metric
          note: Training datasets/manifests and Gym inventory, description, preparation records and metric
            are retained files.
        records: *id003
        note: These are use-produced artifacts, not the shipped static prompts.
      - scope: SFT updated actor/rollout state and checkpoints
        assessment: known
        findings:
        - value: model-weights
          basis: wired
          records: &id004
          - runtime.md#rt-cmp-training-models
          - runtime.md#rt-rte-sft-training
          note: Actor training changes parameters and updates rollout weights; checkpoints retain the
            result.
        - value: in-memory
          basis: wired
          records: *id004
          note: Training state is allocated in GPU/host memory.
        - value: files
          basis: wired
          records: *id004
          note: Configured checkpoint saving retains numerical state in files.
        records: *id004
        note: Substrate wiring is known although checkpoint instances and historical lineage are unavailable.
      - scope: Upstream RL numerical parameter retention
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-rl-training
        - runtime.md#rt-cmp-training-models
        note: Reward-hook and external-trainer wiring are known, but upstream optimizer and exact retained
          checkpoint substrate are not inspected.
      - scope: Other vendored memory/database copies, alternative RL search classes, NatureBench-specific
          context, metadata/tool-admission branches and sandbox operational stores
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-targeted-memory
        - runtime.md#rt-rte-rl-training
        - runtime.md#rt-rte-gym-build
        note: The accepted memory inventory names these included but untraced alternatives. Their relevant
          objects, consumers and operations are not fully inspected; this prevents a complete classification
          for this axis.
      records:
      - memory.md#mem-obj-journal
      - memory.md#mem-obj-experience-card
      - memory.md#mem-obj-rich-summary
      - memory.md#mem-obj-rl-program
      - memory.md#mem-obj-sft-program
      - memory.md#mem-obj-alignment-dataset
      - runtime.md#rt-rte-gym-build
      - runtime.md#rt-obj-metric
      - runtime.md#rt-cmp-training-models
      - runtime.md#rt-rte-sft-training
      - runtime.md#rt-rte-rl-training
      - memory.md#mem-rte-targeted-memory
      note: Inventory includes use-derived search stores, training artifacts, Gym artifacts and numerical
        training state, not all runtime storage. Included alternative implementations remain unresolved;
        positives are local implementation findings, not an exhaustive release-wide union.
    representational_form:
      assessment: partial
      units:
      - scope: 'Search history/cards, SQL rows and alignment conversations: model-interpreted prose'
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id005
          - memory.md#mem-obj-journal
          - memory.md#mem-obj-experience-card
          - memory.md#mem-obj-rich-summary
          - memory.md#mem-obj-rl-program
          - memory.md#mem-obj-sft-program
          - memory.md#mem-obj-alignment-dataset
          note: Plans, analysis, feedback, summaries and conversation text are interpreted by models or
            humans.
        records: *id005
        note: Text parts are separate from the code and fixed-rule fields in their containers.
      - scope: Executable programs, links/IDs, metrics, SQL control fields and dataset token/loss masks
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id006
          - memory.md#mem-obj-journal
          - memory.md#mem-obj-experience-card
          - memory.md#mem-obj-rl-program
          - memory.md#mem-obj-sft-program
          - memory.md#mem-obj-alignment-dataset
          - runtime.md#rt-rte-sft-training
          note: Python and structured fields have localized units consumed by execution, fixed selection
            or training-mask rules.
        records: *id006
        note: A numeric score or JSON wrapper is not distributed-parametric merely because it is numerical.
      - scope: Gym retained inventory/description versus executable metric/preparation
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id007
          - runtime.md#rt-rte-gym-build
          - runtime.md#rt-obj-metric
          note: Inventory, description and retry feedback supply interpreted context.
        - value: symbolic
          basis: wired
          records: *id007
          note: Retained Python metric/preparation code is compiled, executed or imported.
        records: *id007
        note: Distinct consumption paths coexist inside the generated package.
      - scope: Updated SFT actor/rollout weights
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: &id008
          - runtime.md#rt-cmp-training-models
          - runtime.md#rt-rte-sft-training
          note: Training changes distributed numerical parameter state.
        records: *id008
        note: The form is established without inspecting individual learned propositions.
      - scope: RL opaque evaluator payload parts beyond inspected row/display fields
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-rl-program
        - runtime.md#rt-rte-rl-training
        note: Mixed code, feedback and summary fields are known above; the complete consumed payload is
          not classified from its brief display summary.
      - scope: Other vendored memory/database copies, alternative RL search classes, NatureBench-specific
          context, metadata/tool-admission branches and sandbox operational stores
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-targeted-memory
        - runtime.md#rt-rte-rl-training
        - runtime.md#rt-rte-gym-build
        note: The accepted memory inventory names these included but untraced alternatives. Their relevant
          objects, consumers and operations are not fully inspected; this prevents a complete classification
          for this axis.
      records:
      - memory.md#mem-obj-journal
      - memory.md#mem-obj-experience-card
      - memory.md#mem-obj-rich-summary
      - memory.md#mem-obj-rl-program
      - memory.md#mem-obj-sft-program
      - memory.md#mem-obj-alignment-dataset
      - runtime.md#rt-rte-sft-training
      - runtime.md#rt-rte-gym-build
      - runtime.md#rt-obj-metric
      - runtime.md#rt-cmp-training-models
      - runtime.md#rt-rte-rl-training
      - memory.md#mem-rte-targeted-memory
      note: Mixed artifacts are split by operative encoding and consumer; opaque payload coverage is retained.
        Included alternative implementations remain unresolved; positives are local implementation findings,
        not an exhaustive release-wide union.
    lineage:
      assessment: partial
      units:
      - scope: Generated program plans/code and model-authored comparative prose
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id009
          - memory.md#mem-obj-journal
          - memory.md#mem-obj-rich-summary
          - memory.md#mem-rte-summary-cache
          - memory.md#mem-obj-rl-program
          - memory.md#mem-obj-sft-program
          note: Proposal and summary models author retained code and text.
        records: *id009
        note: Authorship does not imply semantic correctness or human admission.
      - scope: Derived cards, boards and selected/reconstructed SFT conversations
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id010
          - memory.md#mem-obj-experience-card
          - memory.md#mem-obj-alignment-dataset
          note: Cards/boards derive from evaluated attempts; training conversations reconstruct retained
            generation experience.
        - value: other-compiled
          basis: wired
          records: *id010
          note: Deterministic card aggregation and conversation reconstruction compile selected fields
            into retained products.
        records: *id010
        note: Trace origin and deterministic compilation are separate supported derivation properties,
          not proof of original corpus provenance.
      - scope: Gym raw task information and descriptions
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id011
          - runtime.md#rt-rte-gym-build
          - runtime.md#rt-obj-metric
          note: External task information enters the build.
        - value: authored
          basis: wired
          records: *id011
          note: Models author descriptions and executable package parts from selected input.
        records: *id011
        note: Import warrant remains unknown; imported task data are not automatically runtime event streams.
      - scope: SFT trained parameters after actor update
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id012
          - runtime.md#rt-rte-sft-training
          - runtime.md#rt-cmp-training-models
          note: Numerical training compiles selected conversation examples into changed parameters.
        records: *id012
        note: This known subsequent update does not resolve initialization.
      - scope: Initial SQL contents, source Parquet and starting model checkpoints
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-rl-program
        - memory.md#mem-obj-alignment-dataset
        - runtime.md#rt-cmp-training-models
        note: Initial content provenance and historical checkpoint lineage are unavailable; no origin
          is inferred from configured paths.
      - scope: Other vendored memory/database copies, alternative RL search classes, NatureBench-specific
          context, metadata/tool-admission branches and sandbox operational stores
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-targeted-memory
        - runtime.md#rt-rte-rl-training
        - runtime.md#rt-rte-gym-build
        note: The accepted memory inventory names these included but untraced alternatives. Their relevant
          objects, consumers and operations are not fully inspected; this prevents a complete classification
          for this axis.
      records:
      - memory.md#mem-obj-journal
      - memory.md#mem-obj-rich-summary
      - memory.md#mem-rte-summary-cache
      - memory.md#mem-obj-rl-program
      - memory.md#mem-obj-sft-program
      - memory.md#mem-obj-experience-card
      - memory.md#mem-obj-alignment-dataset
      - runtime.md#rt-rte-gym-build
      - runtime.md#rt-obj-metric
      - runtime.md#rt-rte-sft-training
      - runtime.md#rt-cmp-training-models
      - memory.md#mem-rte-targeted-memory
      - runtime.md#rt-rte-rl-training
      note: Known generation/extraction/update paths coexist with unknown initialization and external-corpus
        provenance. Included alternative implementations remain unresolved; positives are local implementation
        findings, not an exhaustive release-wide union.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Selected program/summary prose at proposal models
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id013
          - memory.md#mem-rte-targeted-memory
          - memory.md#mem-rte-summary-cache
          - runtime.md#rt-rte-rl-training
          - memory.md#mem-rte-sft-search
          - runtime.md#rt-rte-gym-build
          note: Selected experience supplies context/advice for later candidate proposals, without guaranteed
            compliance.
        records: *id013
        note: Use-derived prose is advisory evidence, not standing instruction merely because prompts
          tell the model to use it.
      - scope: Retained metrics, utilities and program fields at parent/final selectors
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id014
          - memory.md#mem-obj-journal
          - memory.md#mem-obj-experience-card
          - memory.md#mem-obj-rl-program
          - memory.md#mem-rte-sft-search
          - runtime.md#rt-rte-evolution-search
          - workflow.md#wf-rte-final-delivery
          note: Scores and utilities determine relative candidate priority.
        - value: routing
          basis: wired
          records: *id014
          note: Retained population and selected parent/mode state determine the next operator input or
            continuation.
        records: *id014
        note: Terminal fallback and active-solution admission have different eligibility predicates.
      - scope: Retained trace examples at summary and numerical update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id015
          - memory.md#mem-rte-summary-cache
          - memory.md#mem-obj-alignment-dataset
          - runtime.md#rt-rte-sft-training
          note: Stored code/feedback feeds durable summaries; selected conversations feed actor updates.
        records: *id015
        note: Learning authority is at the update consumer, separately from downstream advisory use; improved
          capacity is not observed.
      - scope: Retained generated metric at validation/scoring consumer
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id016
          - runtime.md#rt-obj-metric
          - epistemic.md#epi-rte-package-validation
          note: Metric criteria check submission conformance and score candidates.
        - value: enforcement
          basis: wired
          records: *id016
          note: Submission validation can reject a candidate rather than merely advise it.
        records: *id016
        note: The task metric is executable criterion material, not independently verified task truth.
      - scope: Trained parameters at subsequent Evo deployment
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-cmp-training-models
        - runtime.md#rt-rte-sft-training
        - runtime.md#rt-rte-rl-training
        note: Rollout weight refresh is wired, but historical checkpoint-to-Evo deployment and the downstream
          force of a particular trained artifact are unresolved.
      - scope: Other vendored memory/database copies, alternative RL search classes, NatureBench-specific
          context, metadata/tool-admission branches and sandbox operational stores
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-targeted-memory
        - runtime.md#rt-rte-rl-training
        - runtime.md#rt-rte-gym-build
        note: The accepted memory inventory names these included but untraced alternatives. Their relevant
          objects, consumers and operations are not fully inspected; this prevents a complete classification
          for this axis.
      records:
      - memory.md#mem-rte-targeted-memory
      - memory.md#mem-rte-summary-cache
      - runtime.md#rt-rte-rl-training
      - memory.md#mem-rte-sft-search
      - runtime.md#rt-rte-gym-build
      - memory.md#mem-obj-journal
      - memory.md#mem-obj-experience-card
      - memory.md#mem-obj-rl-program
      - runtime.md#rt-rte-evolution-search
      - workflow.md#wf-rte-final-delivery
      - memory.md#mem-obj-alignment-dataset
      - runtime.md#rt-rte-sft-training
      - runtime.md#rt-obj-metric
      - epistemic.md#epi-rte-package-validation
      - runtime.md#rt-cmp-training-models
      note: Authority belongs to each retained part at its actual consumer; no force follows simply from
        storage. Included alternative implementations remain unresolved; positives are local implementation
        findings, not an exhaustive release-wide union.
    write_agency:
      assessment: partial
      units:
      - scope: Evo journal/card admission and summary generation/cache normalization
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id017
          - memory.md#mem-obj-journal
          - memory.md#mem-obj-experience-card
          - memory.md#mem-rte-summary-cache
          note: Software retains evaluated nodes/cards and admits nonempty model summary fields without
            per-content human approval.
        records: *id017
        note: Operator launch/configuration does not make individual admissions manual.
      - scope: RL/SFT program insertions, metadata updates, pruning and selected dataset admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id018
          - memory.md#mem-obj-rl-program
          - memory.md#mem-rte-sft-search
          - runtime.md#rt-rte-rl-training
          - runtime.md#rt-rte-sft-training
          - memory.md#mem-obj-alignment-dataset
          note: Database, scheduler and data-pipeline rules admit and transform individual records.
        records: *id018
        note: Human threshold selection is distinct from approving each retained item.
      - scope: Gym description/preparation/metric admission and SFT weight update
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id019
          - runtime.md#rt-rte-gym-build
          - runtime.md#rt-obj-metric
          - runtime.md#rt-rte-sft-training
          note: Models/code write generated artifacts; trainer performs numerical updates without individual
            content approval.
        records: *id019
        note: Gym tool-save admission internals remain in the unresolved alternative inventory.
      - scope: Initial database/dataset/checkpoint admission and external checkpoint replacement
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-rl-program
        - memory.md#mem-obj-alignment-dataset
        - runtime.md#rt-cmp-training-models
        note: Generic operator-configured paths establish neither an explicit human content decision nor
          a known automatic initial admission mechanism.
      - scope: Other vendored memory/database copies, alternative RL search classes, NatureBench-specific
          context, metadata/tool-admission branches and sandbox operational stores
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-targeted-memory
        - runtime.md#rt-rte-rl-training
        - runtime.md#rt-rte-gym-build
        note: The accepted memory inventory names these included but untraced alternatives. Their relevant
          objects, consumers and operations are not fully inspected; this prevents a complete classification
          for this axis.
      records:
      - memory.md#mem-obj-journal
      - memory.md#mem-obj-experience-card
      - memory.md#mem-rte-summary-cache
      - memory.md#mem-obj-rl-program
      - memory.md#mem-rte-sft-search
      - runtime.md#rt-rte-rl-training
      - runtime.md#rt-rte-sft-training
      - memory.md#mem-obj-alignment-dataset
      - runtime.md#rt-rte-gym-build
      - runtime.md#rt-obj-metric
      - runtime.md#rt-cmp-training-models
      - memory.md#mem-rte-targeted-memory
      note: Automatic subsequent mechanisms are retained alongside unresolved initialization; no manual
        finding is inferred from workflow launch. Included alternative implementations remain unresolved;
        positives are local implementation findings, not an exhaustive release-wide union.
    curation_operations:
      assessment: partial
      units:
      - scope: Evo cards/boards and method-overview summaries
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id020
          - memory.md#mem-obj-experience-card
          - memory.md#mem-obj-rich-summary
          - memory.md#mem-rte-summary-cache
          note: Evaluated attempts are reduced into cards, aggregate boards and concise reusable method
            descriptions.
        records: *id020
        note: Raw evidence can remain available; consolidation need not erase the input. This does not
          certify preservation of every claim.
      - scope: Comparative-summary novel claims versus compression
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-rich-summary
        - memory.md#mem-rte-summary-cache
        note: Unseen comparative prose can reshape or add claims; no concrete accepted record settles
          synthesis. Known overview consolidation does not classify all comparative semantics.
      - scope: RL retained metadata merge
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id021
          - runtime.md#rt-rte-rl-training
          - memory.md#mem-obj-rl-program
          note: Post-insertion card/summary metadata revises an existing retained program entry.
        records: *id021
        note: This is an implemented metadata update, not a claim that existing explanations are semantically
          corrected.
      - scope: SQL top-k pruning and active-island eviction
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id022
          - memory.md#mem-obj-rl-program
          - memory.md#mem-rte-sft-search
          - runtime.md#rt-rte-evolution-search
          note: Configured caps forget SQL rows or remove weaker candidates from the active population.
        records: *id022
        note: SQL deletion and island eligibility loss have different horizons; journal history may survive
          eviction.
      - scope: SFT dataset reward deduplication
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records: &id023
          - runtime.md#rt-rte-sft-training
          note: Selection removes duplicate reward examples before training dataset output.
        records: *id023
        note: This is an implemented filter, not proof of semantic near-duplicate detection.
      - scope: Initial memory maintenance and external checkpoint replacement
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-rl-program
        - runtime.md#rt-cmp-training-models
        note: Records do not resolve initial content curation or external replacement policy.
      - scope: Other vendored memory/database copies, alternative RL search classes, NatureBench-specific
          context, metadata/tool-admission branches and sandbox operational stores
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-targeted-memory
        - runtime.md#rt-rte-rl-training
        - runtime.md#rt-rte-gym-build
        note: The accepted memory inventory names these included but untraced alternatives. Their relevant
          objects, consumers and operations are not fully inspected; this prevents a complete classification
          for this axis.
      records:
      - memory.md#mem-obj-experience-card
      - memory.md#mem-obj-rich-summary
      - memory.md#mem-rte-summary-cache
      - runtime.md#rt-rte-rl-training
      - memory.md#mem-obj-rl-program
      - memory.md#mem-rte-sft-search
      - runtime.md#rt-rte-evolution-search
      - runtime.md#rt-rte-sft-training
      - runtime.md#rt-cmp-training-models
      - memory.md#mem-rte-targeted-memory
      - runtime.md#rt-rte-gym-build
      note: Operations are classified from transformations, not route names; no synthesis is inferred
        from fluent explanation or unverified novelty. Included alternative implementations remain unresolved;
        positives are local implementation findings, not an exhaustive release-wide union.
    read_back_direction:
      assessment: partial
      units:
      - scope: Evo targeted and legacy operator context; RL/SFT selected-parent context; Gym retry tail
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id024
          - memory.md#mem-rte-targeted-memory
          - runtime.md#rt-rte-rl-training
          - memory.md#mem-rte-sft-search
          - runtime.md#rt-rte-gym-build
          note: Code supplies accumulated memory to later model invocations without a foreground-model
            retrieval request.
        records: *id024
        note: Automatic context assembly differs from execution of the generated proposal.
      - scope: Checkpoint/cache reload and trainer dataset loading
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id025
          - memory.md#mem-obj-journal
          - memory.md#mem-rte-summary-cache
          - memory.md#mem-obj-alignment-dataset
          - runtime.md#rt-rte-sft-training
          note: Continuation requests stored checkpoint/cache parts, and training requests the configured
            dataset.
        records: *id025
        note: A requested cache/file return is pull; the later automatic prompt injection is separately
          push.
      - scope: Persisted Gym evaluation reports and preparation JSON across later invocations
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-obj-task-evaluation
        - epistemic.md#epi-rte-quality-disposition
        - runtime.md#rt-rte-gym-build
        note: Persistence/current-command status consumption is established, but independent later report
          consumption and automatic prepares.json reload are not; neither adds a proved read-back route.
      - scope: Other vendored memory/database copies, alternative RL search classes, NatureBench-specific
          context, metadata/tool-admission branches and sandbox operational stores
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-targeted-memory
        - runtime.md#rt-rte-rl-training
        - runtime.md#rt-rte-gym-build
        note: The accepted memory inventory names these included but untraced alternatives. Their relevant
          objects, consumers and operations are not fully inspected; this prevents a complete classification
          for this axis.
      records:
      - memory.md#mem-rte-targeted-memory
      - runtime.md#rt-rte-rl-training
      - memory.md#mem-rte-sft-search
      - runtime.md#rt-rte-gym-build
      - memory.md#mem-obj-journal
      - memory.md#mem-rte-summary-cache
      - memory.md#mem-obj-alignment-dataset
      - runtime.md#rt-rte-sft-training
      - epistemic.md#epi-obj-task-evaluation
      - epistemic.md#epi-rte-quality-disposition
      note: Known pull and push operations occur within chains; storage/snapshot APIs alone do not establish
        additional consumer routes. Included alternative implementations remain unresolved; positives
        are local implementation findings, not an exhaustive release-wide union.
    read_back_signal:
      assessment: partial
      units:
      - scope: Evo targeted lineage and Debug selection
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id026
          - memory.md#mem-rte-targeted-memory
          - memory.md#mem-obj-experience-card
          note: Before an operator call, node/parent identity intersection selects ancestors and shared-parent
            siblings for delivery.
        - value: inferred-lexical
          basis: wired
          records: *id026
          note: On Debug, matching detected error signatures prioritizes related retained failure examples.
        - value: coarse
          basis: wired
          records: *id026
          note: Call/operator configuration and recent-node/count caps supply fallback nodes and aggregate
            board material.
        records: *id026
        note: Trigger is proposal preparation; selector inputs are relationships, signatures, recency
          and configured counts; selected parts are node/card summaries. Character clipping is a separate
          budget operation.
      - scope: Evo legacy simple/ancestral/sibling context
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id027
          - memory.md#mem-rte-targeted-memory
          note: Ancestral traversal and child-of-supplied-node selection use actual links to choose delivered
            history.
        - value: coarse
          basis: wired
          records: *id027
          note: Simple memory uses good/buggy filters and character-limited suffixes rather than a semantic
            query.
        records: *id027
        note: These alternatives can supplement or replace targeted context; no embedding retrieval is
          inferred.
      - scope: RL AIRA and SFT Greedy proposal context
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id028
          - runtime.md#rt-rte-rl-training
          - memory.md#mem-rte-sft-search
          - memory.md#mem-obj-rl-program
          note: Task identity and parent/child/ancestor links restrict delivered retained programs.
        - value: coarse
          basis: wired
          records: *id028
          note: Best/recent fitness, success/debug state and recency choose task-local examples.
        records: *id028
        note: Task-local identity, success/fitness and recency selection are supported in these inspected
          branches; RL and SFT selectors are not identical.
      - scope: RL AIRA Debug error-matched experience
        assessment: known
        findings:
        - value: inferred-lexical
          basis: wired
          records: &id029
          - runtime.md#rt-rte-rl-training
          note: Before Debug, detected error-signature matches prioritize retained failed programs for
            prompt delivery.
        records: *id029
        note: The lexical finding applies to the RL AIRA branch only, not the SFT selector.
      - scope: Gym preparation retry context
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id030
          - runtime.md#rt-rte-gym-build
          note: Each retry automatically supplies the retained last-two-message code/feedback tail.
        records: *id030
        note: Tail selection is not identity-targeted retrieval; full graph-history deletion is unresolved.
      - scope: Other vendored memory/database copies, alternative RL search classes, NatureBench-specific
          context, metadata/tool-admission branches and sandbox operational stores
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-targeted-memory
        - runtime.md#rt-rte-rl-training
        - runtime.md#rt-rte-gym-build
        note: The accepted memory inventory names these included but untraced alternatives. Their relevant
          objects, consumers and operations are not fully inspected; this prevents a complete classification
          for this axis.
      records:
      - memory.md#mem-rte-targeted-memory
      - memory.md#mem-obj-experience-card
      - runtime.md#rt-rte-rl-training
      - memory.md#mem-rte-sft-search
      - memory.md#mem-obj-rl-program
      - runtime.md#rt-rte-gym-build
      note: Push signals classify selectors, not filenames or requested returns. The RL/SFT grouped unit
        retains a local scope qualification for the lexical finding. Included alternative implementations
        remain unresolved; positives are local implementation findings, not an exhaustive release-wide
        union.
    trace_learning:
      assessment: partial
      units:
      - scope: Evo cards and rich summaries delivered to later proposals
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id031
          - memory.md#mem-obj-experience-card
          - memory.md#mem-rte-summary-cache
          - memory.md#mem-rte-targeted-memory
          note: Automatic evaluated-attempt-to-card/summary writes produce retained context for later
            model calls.
        records: *id031
        note: A durable continuation/context product qualifies without measured improvement or truth acceptance.
      - scope: RL derived card/summary metadata and SFT selected examples/actor updates
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id032
          - runtime.md#rt-rte-rl-training
          - memory.md#mem-obj-rl-program
          - memory.md#mem-obj-alignment-dataset
          - runtime.md#rt-rte-sft-training
          note: RL automatically derives retained experience used in later generation; SFT converts scored
            traces into examples consumed by numerical updates.
        records: *id032
        note: RL summary/context wiring is separate from the unavailable upstream optimizer implementation.
      - scope: Gym derived inventory/description reused by Describe/Prepare
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id033
          - runtime.md#rt-rte-gym-build
          note: Tool-selected saved inventory and generated description are retained derived material
            consumed by later model calls.
        records: *id033
        note: Tool-save validation internals and semantic reliability remain unresolved; source-level
          later delivery is supported.
      - scope: RL upstream optimizer and external corpus/checkpoint history
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-rl-training
        - runtime.md#rt-cmp-training-models
        - memory.md#mem-obj-alignment-dataset
        note: Reward hooks do not establish the external optimizer internals or historical trace-to-serving
          chain. No local no finding or system-wide absence is warranted.
      - scope: Other vendored memory/database copies, alternative RL search classes, NatureBench-specific
          context, metadata/tool-admission branches and sandbox operational stores
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-targeted-memory
        - runtime.md#rt-rte-rl-training
        - runtime.md#rt-rte-gym-build
        note: The accepted memory inventory names these included but untraced alternatives. Their relevant
          objects, consumers and operations are not fully inspected; this prevents a complete classification
          for this axis.
      records:
      - memory.md#mem-obj-experience-card
      - memory.md#mem-rte-summary-cache
      - memory.md#mem-rte-targeted-memory
      - runtime.md#rt-rte-rl-training
      - memory.md#mem-obj-rl-program
      - memory.md#mem-obj-alignment-dataset
      - runtime.md#rt-rte-sft-training
      - runtime.md#rt-rte-gym-build
      - runtime.md#rt-cmp-training-models
      note: Qualifying automatic derivation plus retained later context or numerical consumption establishes
        yes locally, not exercised learning or benefit. Included alternative implementations remain unresolved;
        positives are local implementation findings, not an exhaustive release-wide union.
    trace_source:
      assessment: partial
      units:
      - scope: Evo card/summary derivation from generated programs and execution feedback
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id034
          - memory.md#mem-obj-journal
          - memory.md#mem-obj-experience-card
          - memory.md#mem-obj-rich-summary
          - memory.md#mem-rte-summary-cache
          note: Recorded execution results/logs supply the derived experience.
        - value: trajectories
          basis: wired
          records: *id034
          note: Linked evaluated parent/current program states, changes and outcomes supply multi-step
            comparative experience.
        records: *id034
        note: Inputs are evaluated program-search records; event-stream serialization is not inferred
          from the journal name.
      - scope: RL card/summary metadata and SFT training-example extraction
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id035
          - runtime.md#rt-rte-rl-training
          - memory.md#mem-obj-rl-program
          - memory.md#mem-obj-alignment-dataset
          - runtime.md#rt-rte-sft-training
          note: Program evaluation feedback informs metadata and example admission.
        - value: trajectories
          basis: wired
          records: *id035
          note: Parent-linked generation/evaluation records connect states, program changes and outcomes.
        records: *id035
        note: These origins coexist; they do not establish complete external dataset provenance.
      - scope: Recorded SFT request/response conversations reconstructed for training
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id036
          - memory.md#mem-obj-alignment-dataset
          - memory.md#mem-obj-sft-program
          note: Retained system/user prompts and assistant generation/reasoning/code form recorded model-work
            conversations reconstructed into examples.
        records: *id036
        note: This classification concerns retained conversational work records, not static source prompts
          by themselves.
      - scope: Gym saved tool-derived inventory and downstream description
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id037
          - runtime.md#rt-rte-gym-build
          note: Perception tool messages and saved inspection results feed retained inventory and generated
            description.
        records: *id037
        note: External task files/web content are mixed nontrace inputs, not event streams by relabeling.
      - scope: External source Parquet, initial database contents and upstream RL training inputs
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-alignment-dataset
        - memory.md#mem-obj-rl-program
        - runtime.md#rt-rte-rl-training
        - runtime.md#rt-cmp-training-models
        note: Original mixed-input provenance is incomplete; no complete source union or absence of other
          trace types follows.
      - scope: Other vendored memory/database copies, alternative RL search classes, NatureBench-specific
          context, metadata/tool-admission branches and sandbox operational stores
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-targeted-memory
        - runtime.md#rt-rte-rl-training
        - runtime.md#rt-rte-gym-build
        note: The accepted memory inventory names these included but untraced alternatives. Their relevant
          objects, consumers and operations are not fully inspected; this prevents a complete classification
          for this axis.
      records:
      - memory.md#mem-obj-journal
      - memory.md#mem-obj-experience-card
      - memory.md#mem-obj-rich-summary
      - memory.md#mem-rte-summary-cache
      - runtime.md#rt-rte-rl-training
      - memory.md#mem-obj-rl-program
      - memory.md#mem-obj-alignment-dataset
      - runtime.md#rt-rte-sft-training
      - memory.md#mem-obj-sft-program
      - runtime.md#rt-rte-gym-build
      - runtime.md#rt-cmp-training-models
      - memory.md#mem-rte-targeted-memory
      note: Trace origin follows qualifying input content; static imports and unknown histories remain
        separate from supported trace-fed inputs. Included alternative implementations remain unresolved;
        positives are local implementation findings, not an exhaustive release-wide union.
---

# OpenRSI memory profile

## Comparison rationale

All positive findings classify accepted implementation records, not observed operation. The inventory is deliberately partial on every axis: the accepted memory report retains included alternate copies and consumers that have not been traced. A known witness does not resolve them. External numerical state has known SFT update wiring but unresolved initial provenance and historical deployment. The upstream RL optimizer remains distinct from the vendored SFT trainer. See [RT-CMP-training-models](runtime.md#rt-cmp-training-models), [RT-RTE-sft-training](runtime.md#rt-rte-sft-training) and [RT-RTE-rl-training](runtime.md#rt-rte-rl-training).

Reconciliation supersedes the epistemic rich-summary object with [MEM-OBJ-rich-summary](memory.md#mem-obj-rich-summary), and its summary-generation route with [MEM-RTE-summary-cache](memory.md#mem-rte-summary-cache). Those are the canonical citations used here. This changes identity resolution, not the strength or semantic warrant of any finding. The targeted display route remains separate.

Memory advice is knowledge at the proposal consumer; its source experience can separately have learning authority at a durable-summary or numerical-update consumer. Neither entails measured capacity gains. Generated metric code instead acts as executable validation criteria; its rejection path supplies enforcement. The profile does not upgrade advisory experience into standing instruction or warranted explanatory knowledge. See [RT-BAP-operator-guidance](runtime.md#rt-bap-operator-guidance), [MEM-RTE-summary-cache](memory.md#mem-rte-summary-cache) and [EPI-RTE-package-validation](epistemic.md#epi-rte-package-validation).

Summary method overviews and boards reduce existing experience; the comparative explanation field can contain unknown semantic additions. Consolidation is locally supported, while synthesis of new claims remains unresolved. SQL pruning forgets rows; island eviction only removes active eligibility and can leave journal evidence. Metadata merging revises retained entries. These effects have different scopes, rather than a global forgetting or truth-maintenance guarantee. See [MEM-OBJ-experience-card](memory.md#mem-obj-experience-card), [MEM-OBJ-rl-program](memory.md#mem-obj-rl-program) and [MEM-RTE-sft-search](memory.md#mem-rte-sft-search).

Requested checkpoint/cache/dataset reads and automatic later prompt selection are different operations, so both pull and push are supported. Identity-targeted push requires actual relationship matching, not merely a node-ID cache filename. Error-signature matching is lexical selection; numeric rank and recency are coarse selection, not inferred model judgment. Evo shared-parent siblings and RL children-of-current-parent are not interchangeable. See [MEM-RTE-targeted-memory](memory.md#mem-rte-targeted-memory) and [RT-RTE-rl-training](runtime.md#rt-rte-rl-training).

The trace-source findings concern recorded model-work conversations, tool execution feedback and linked program-change/outcome sequences. Imported task files do not become event streams merely by entering a journal or pipeline. No local negative trace-learning finding is invented: records establish positive routes and unresolved alternatives, not a bounded all-route absence. See [MEM-OBJ-alignment-dataset](memory.md#mem-obj-alignment-dataset), [MEM-OBJ-journal](memory.md#mem-obj-journal) and [RT-RTE-gym-build](runtime.md#rt-rte-gym-build).

No frozen-source files were read for this mapping. Only the supplied members and governing contracts were read; no new records, quotations or evidence were added.
