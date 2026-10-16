---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "SkillLift memory classifications for retained task portfolios, scoring receipts, recovery state, category snapshots and domain fusion, with unresolved alternative routes."
run-id: AAS-2026-10-14-skilllift-0f350bf64418-01
source-identity: https://github.com/walter-mitty-pro/SkillLift
reviewed-boundary: "599358b4d4c4a27c0e004df8228ab93026600653"
memory-comparison:
  version: 2
  scope: "Use-accumulated skill bodies and auxiliary content, candidate reconstruction records, search history, receipt rules and rationale, revision diagnostics, verifier scores, trial recovery records, category and cluster checkpoints, trained cluster artifacts and fused final guides. Includes unresolved raw-trajectory consumers and other shipped baseline/entry-point alternatives; their missing records prevent complete coverage. Excludes static shipped prompts, transient request views as independent stores, external benchmark/host memory and opaque provider weights: no accepted record establishes those weights as use-accumulated SkillLift memory."
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Task skill trees, candidate recipes, search state and trial recovery records"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-skill-instructions, memory.md#mem-obj-candidate-record, memory.md#mem-obj-search-state, runtime.md#rt-rte-cell-recovery]
              note: "Retained filesystem trees, patches and JSON state are reconstructed or looked up by later coordinator invocations."
          records: [memory.md#mem-obj-skill-instructions, memory.md#mem-obj-candidate-record, memory.md#mem-obj-search-state, runtime.md#rt-rte-cell-recovery]
          note: "Filesystem retention is established for these parts; a Git dependency used to apply patches does not make the store a repository substrate."
        - scope: "Receipt rules, rationale, revision attempts and persisted verifier scores"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-receipt-rubrics, memory.md#mem-obj-receipt-metadata, memory.md#mem-obj-revision-attempts, epistemic.md#epi-obj-verifier-score]
              note: "Task-state receipts and ExperimentStore JSON/text artifacts retain these parts beyond the producing call."
          records: [memory.md#mem-obj-receipt-rubrics, memory.md#mem-obj-receipt-metadata, memory.md#mem-obj-revision-attempts, epistemic.md#epi-obj-verifier-score]
          note: "Python schema objects are working copies of these retained files, not an independently established in-memory persistence system."
        - scope: "Category snapshots/final trees, domain checkpoints/cluster artifacts/master bundle and behavior diagnostics"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-master-skill, memory.md#mem-obj-behavior-summary, runtime.md#rt-rte-domain-fusion]
              note: "Round JSON, skill Markdown, bundle/provenance files and aggregate diagnostic files are retained on the run filesystem."
          records: [memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-master-skill, memory.md#mem-obj-behavior-summary, runtime.md#rt-rte-domain-fusion]
          note: "Full snapshots differ from task replay but share its file substrate."
        - scope: "Raw trajectory payloads and remaining shipped baseline/standalone memory alternatives"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-obj-behavior-summary, runtime.md#rt-rte-task-evolution, runtime.md#rt-rte-domain-fusion]
          note: "Raw trajectory serialization/readers and wider algorithm stores are not fully established by accepted records; inspected file witnesses do not enumerate their operative parts."
      records: [memory.md#mem-obj-candidate-record, memory.md#mem-obj-search-state, memory.md#mem-obj-receipt-rubrics, memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-master-skill, memory.md#mem-obj-behavior-summary, runtime.md#rt-rte-task-evolution]
      note: "Files are wired across the assessed routes; remaining shipped memory alternatives prevent a complete substrate inventory."
    representational_form:
      assessment: partial
      units:
        - scope: "Skill instruction bodies and receipt criterion text at planner/editor/verifier and benchmark consumers"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-skill-instructions, memory.md#mem-obj-receipt-rubrics, runtime.md#rt-bap-skill-delivery, runtime.md#rt-bap-receipt-scoring]
              note: "Models interpret the retained instructions and scoring criteria; downstream compliance is unobserved."
          records: [memory.md#mem-obj-skill-instructions, memory.md#mem-obj-receipt-rubrics, runtime.md#rt-bap-skill-delivery, runtime.md#rt-bap-receipt-scoring]
          note: "This unit classifies instruction semantics, not the symbolic packaging surrounding them."
        - scope: "Task patch recipe, accepted IDs, hashes, novelty keys, checkpoints, score fields and bundle identity at code consumers"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-candidate-record, memory.md#mem-obj-search-state, memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-master-skill, epistemic.md#epi-obj-verifier-score, runtime.md#rt-rte-cell-recovery]
              note: "Localized fields, patch syntax, booleans and numbers have fixed application, arithmetic, identity and continuation rules."
          records: [memory.md#mem-obj-candidate-record, memory.md#mem-obj-search-state, memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-master-skill, epistemic.md#epi-obj-verifier-score, runtime.md#rt-rte-cell-recovery]
          note: "Numerical scores are symbolic scalars, not distributed parameters. Checkpoint text is classified separately at its model consumption path."
        - scope: "Direction hypotheses, prior plans, receipt diagnosis, repair rationale and verifier explanations at model consumers"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-candidate-record, memory.md#mem-obj-search-state, memory.md#mem-obj-receipt-metadata, memory.md#mem-obj-revision-attempts, epistemic.md#epi-obj-verifier-score]
              note: "Textual hypotheses and explanations survive in explicit planning, receipt and repair inputs."
          records: [memory.md#mem-obj-candidate-record, memory.md#mem-obj-search-state, memory.md#mem-obj-receipt-metadata, memory.md#mem-obj-revision-attempts, epistemic.md#epi-obj-verifier-score]
          note: "JSON slots are symbolic organization; the contained reasons still require language interpretation, and delivery does not prove reliance."
        - scope: "Category/cluster/fused skill and receipt bodies at resumed training, fusion and held-out consumers"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-master-skill, runtime.md#rt-rte-domain-fusion, epistemic.md#epi-rte-category-fusion]
              note: "Reloaded rule text and retained SKILL.md bodies feed subsequent model requests and benchmark instruction channels."
          records: [memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-master-skill, runtime.md#rt-rte-domain-fusion, epistemic.md#epi-rte-category-fusion]
          note: "Domain fusion loads every current cluster skill, not only ranked winners; metadata has a different form and consumer."
        - scope: "tau2 execution behavior summary counts and heuristic labels"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-behavior-summary]
              note: "Fixed reducers produce counts, termination counts and coarse pattern labels; these are diagnostic fields rather than semantic rule explanations."
          records: [memory.md#mem-obj-behavior-summary]
          note: "A readable label does not turn a fixed heuristic category into model-interpreted advice."
        - scope: "Auxiliary portfolio payloads, raw trajectories and other shipped memory alternatives"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-obj-skill-instructions, memory.md#mem-obj-behavior-summary, runtime.md#rt-rte-task-evolution]
          note: "Some selected auxiliary text reaches editors, but host script execution, all auxiliary loading branches and raw-payload consumers are uninspected. Their operative forms cannot be inferred from display text."
      records: [memory.md#mem-obj-skill-instructions, memory.md#mem-obj-candidate-record, memory.md#mem-obj-search-state, memory.md#mem-obj-receipt-rubrics, memory.md#mem-obj-master-skill, memory.md#mem-obj-behavior-summary, runtime.md#rt-rte-task-evolution]
      note: "Natural-language and symbolic parts are separated by consumption. Opaque provider model form is not asserted as retained experience memory. Unresolved payload routes prevent complete coverage."
    lineage:
      assessment: partial
      units:
        - scope: "Native task seed skill bodies"
          assessment: partial
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-obj-skill-instructions, runtime.md#rt-rte-task-evolution]
              note: "Benchmark/native seed content is acquired and snapshotted by the adapter/store route."
          records: [memory.md#mem-obj-skill-instructions, runtime.md#rt-rte-task-evolution]
          note: "Import is known; original seed authorship is unresolved and cannot be inferred as human-authored."
        - scope: "Model-produced plans, directions, initial criteria, edits, diagnoses and fused skill content"
          assessment: known
          findings:
            - value: authored
              basis: wired
              records: [memory.md#mem-obj-candidate-record, memory.md#mem-obj-search-state, memory.md#mem-obj-receipt-rubrics, memory.md#mem-obj-receipt-metadata, memory.md#mem-obj-master-skill, epistemic.md#epi-rte-category-fusion]
              note: "Planner, generator, rubricator and fusion models compose proposals from supplied inputs; authorship is not human admission."
          records: [memory.md#mem-obj-candidate-record, memory.md#mem-obj-search-state, memory.md#mem-obj-receipt-rubrics, memory.md#mem-obj-receipt-metadata, memory.md#mem-obj-master-skill, epistemic.md#epi-rte-category-fusion]
          note: "This is the established generation path, not a guarantee of novelty, semantic faithfulness or source truth."
        - scope: "Scalar search experience and rank/criterion contrast feeding durable planning and receipt updates"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [memory.md#mem-obj-search-state, runtime.md#rt-rte-task-evolution, runtime.md#rt-rte-receipt-revision]
              note: "Recorded evaluation results and rejected directions are selected into retained history and subsequent rule-update evidence."
          records: [memory.md#mem-obj-search-state, runtime.md#rt-rte-task-evolution, runtime.md#rt-rte-receipt-revision]
          note: "This derivation coexists with model authorship of the revised text; it does not imply full-transcript extraction."
        - scope: "tau2 behavior summary derived from simulation messages"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [memory.md#mem-obj-behavior-summary]
              note: "Recorded simulation messages, tool names/requestors and retry phrases feed deterministic counts and labels."
          records: [memory.md#mem-obj-behavior-summary]
          note: "Trace-derived diagnostic lineage does not establish a later behavior-shaping summary consumer."
        - scope: "Validation metadata, replay/control fields, checkpoint serialization and bundle/hash packaging"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-candidate-record, memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-master-skill, epistemic.md#epi-obj-verifier-score]
              note: "Fixed code computes validation/score/hash fields and serializes selected content into replay records, snapshots and bundles."
          records: [memory.md#mem-obj-candidate-record, memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-master-skill, epistemic.md#epi-obj-verifier-score]
          note: "This unit covers compiled packaging and arithmetic, not the independently model-authored skill/rationale text."
        - scope: "Initial category/domain input provenance, raw trajectory payloads and other shipped alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-behavior-summary, runtime.md#rt-rte-category-training, runtime.md#rt-rte-task-evolution]
          note: "Known later transformations do not resolve all original content provenance; raw serialization and wider stores lack an accepted derivation inventory."
      records: [memory.md#mem-obj-skill-instructions, memory.md#mem-obj-search-state, memory.md#mem-obj-receipt-rubrics, memory.md#mem-obj-master-skill, memory.md#mem-obj-behavior-summary, runtime.md#rt-rte-task-evolution]
      note: "Import, model authorship, trace extraction and code compilation coexist at named parts. Unknown initialization and alternative routes prevent complete lineage classification."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Retained skill bodies at later benchmark agents"
          assessment: known
          findings:
            - value: instruction
              basis: wired
              records: [memory.md#mem-obj-skill-instructions, memory.md#mem-obj-master-skill, runtime.md#rt-bap-skill-delivery, epistemic.md#epi-rte-category-fusion]
              note: "Loaded portfolios and final/master skill text supply standing task guidance, not enforced tool permissions."
          records: [memory.md#mem-obj-skill-instructions, memory.md#mem-obj-master-skill, runtime.md#rt-bap-skill-delivery, epistemic.md#epi-rte-category-fusion]
          note: "Wiring establishes instruction delivery, not actual agent compliance."
        - scope: "Retained skill bodies and plans/rationales at planning, editing and revision consumers"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [memory.md#mem-obj-skill-instructions, memory.md#mem-obj-search-state, memory.md#mem-obj-receipt-metadata, runtime.md#rt-rte-receipt-revision]
              note: "Existing text and retained reasons supply evidence/context for proposals; receipt diagnosis delivery does not prove that a model relies on it."
          records: [memory.md#mem-obj-skill-instructions, memory.md#mem-obj-search-state, memory.md#mem-obj-receipt-metadata, runtime.md#rt-rte-receipt-revision]
          note: "Knowledge means reference/context force here, not accepted factual truth."
        - scope: "Receipt criterion text and signed points at verifier and score/selection consumers"
          assessment: known
          findings:
            - value: instruction
              basis: wired
              records: [memory.md#mem-obj-receipt-rubrics, runtime.md#rt-bap-receipt-scoring]
              note: "Retained criteria direct subsequent verifier judgments and criterion-hit update guidance."
            - value: ranking
              basis: wired
              records: [memory.md#mem-obj-receipt-rubrics, epistemic.md#epi-rte-verifier-check, runtime.md#rt-bap-receipt-scoring]
              note: "Criterion text and signed points determine scores that influence refinement and relative candidate priority."
          records: [memory.md#mem-obj-receipt-rubrics, epistemic.md#epi-rte-verifier-check, runtime.md#rt-bap-receipt-scoring]
          note: "Language interpretation and fixed arithmetic are separate mechanisms; neither certifies task quality."
        - scope: "Persisted score/history/direction experience at planning and receipt-update consumers"
          assessment: known
          findings:
            - value: learning
              basis: wired
              records: [memory.md#mem-obj-search-state, runtime.md#rt-rte-receipt-revision, memory.md#mem-obj-receipt-rubrics]
              note: "Retained evaluation and proposal experience feeds automatic durable planning constraints and scoring-rule updates for subsequent rounds."
            - value: ranking
              basis: wired
              records: [epistemic.md#epi-obj-verifier-score, runtime.md#rt-rte-task-evolution, runtime.md#rt-rte-category-training]
              note: "Retained numerical results and winner markers influence successor and completed-round selection."
          records: [memory.md#mem-obj-search-state, runtime.md#rt-rte-receipt-revision, memory.md#mem-obj-receipt-rubrics, epistemic.md#epi-obj-verifier-score, runtime.md#rt-rte-category-training]
          note: "Learning authority is the update-input effect, independently of downstream instruction authority and without demonstrated capacity improvement."
        - scope: "Accepted IDs, checkpoints, trial results and attempt markers at continuation/recovery consumers"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-search-state, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-category-round, runtime.md#rt-rte-cell-recovery]
              note: "Retained IDs and completion/results state choose reconstructed parents, next rounds and reuse/recovery/retry operations."
          records: [memory.md#mem-obj-search-state, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-category-round, runtime.md#rt-rte-cell-recovery]
          note: "Checkpoint contents route continuation; merely supplying a run-root path does not constitute manual admission."
        - scope: "Retained hashes, validity, scopes, novelty exclusions and identity fields at replay/admission consumers"
          assessment: known
          findings:
            - value: validation
              basis: wired
              records: [memory.md#mem-obj-candidate-record, memory.md#mem-obj-search-state, memory.md#mem-obj-category-round, memory.md#mem-obj-master-skill, runtime.md#rt-rte-cell-recovery]
              note: "Stored scope/identity/hash fields and novelty constraints supply conformance criteria for reconstruction, reuse and later proposals."
            - value: enforcement
              basis: wired
              records: [memory.md#mem-obj-candidate-record, memory.md#mem-obj-search-state, memory.md#mem-obj-master-skill, runtime.md#rt-rte-cell-recovery]
              note: "Invalid or mismatched recipes/results/bundles are refused; prohibited novelty keys constrain later search."
          records: [memory.md#mem-obj-candidate-record, memory.md#mem-obj-search-state, memory.md#mem-obj-category-round, memory.md#mem-obj-master-skill, runtime.md#rt-rte-cell-recovery]
          note: "These are retained controls, not attribution of every static validator rule to memory. Domain checkpoint loading lacks category's configuration check."
        - scope: "Behavior summaries, full revision archives beyond repair, auxiliary host payloads and wider alternative consumers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-behavior-summary, memory.md#mem-obj-revision-attempts, memory.md#mem-obj-skill-instructions, runtime.md#rt-rte-task-evolution]
          note: "Diagnostic summary metadata is excluded from shared receipt input; archive rereading and other consumers are unresolved. Retention alone establishes no authority, and no bounded global absence is warranted."
      records: [runtime.md#rt-bap-skill-delivery, runtime.md#rt-bap-receipt-scoring, memory.md#mem-obj-search-state, memory.md#mem-obj-candidate-record, memory.md#mem-obj-master-skill, memory.md#mem-obj-behavior-summary]
      note: "Instruction, context, update, ranking, routing and veto effects have distinct actual consumers. Unresolved diagnostic and alternative routes prevent a complete authority inventory."
    write_agency:
      assessment: partial
      units:
        - scope: "Task proposal retention, patch/successor admission, search-state update and receipt validation/alignment admission"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-obj-candidate-record, memory.md#mem-obj-search-state, memory.md#mem-obj-receipt-rubrics, runtime.md#rt-rte-task-evolution, runtime.md#rt-rte-receipt-revision]
              note: "Models propose and code admits/records content without per-candidate or per-receipt human decisions."
          records: [memory.md#mem-obj-candidate-record, memory.md#mem-obj-search-state, memory.md#mem-obj-receipt-rubrics, runtime.md#rt-rte-task-evolution, runtime.md#rt-rte-receipt-revision]
          note: "Starting/configuring the run is not manual content admission; saving failed proposals is separate from promoting a successor."
        - scope: "Revision diagnostics, behavior reducers and trial/score recording"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-obj-revision-attempts, memory.md#mem-obj-behavior-summary, runtime.md#rt-rte-cell-recovery, epistemic.md#epi-obj-verifier-score]
              note: "Software records model outputs, validation diagnostics, reduced execution feedback and evaluation state."
          records: [memory.md#mem-obj-revision-attempts, memory.md#mem-obj-behavior-summary, runtime.md#rt-rte-cell-recovery, epistemic.md#epi-obj-verifier-score]
          note: "These automatic diagnostic writes do not all qualify as behavior-shaping learning."
        - scope: "Category/domain updates, snapshot admission and final fusion/materialization"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-master-skill, epistemic.md#epi-rte-category-fusion, runtime.md#rt-rte-domain-fusion]
              note: "Model/code gates select updates and publish retained content; category nondecrease and domain structural admission are not identical gates."
          records: [memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-master-skill, epistemic.md#epi-rte-category-fusion, runtime.md#rt-rte-domain-fusion]
          note: "A human domain/configuration choice is not approval of each rule or snapshot."
        - scope: "Initial supplied seed/checkpoint content and alternate/custom admission paths"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-skill-instructions, memory.md#mem-obj-cluster-checkpoint, runtime.md#rt-rte-task-evolution, runtime.md#rt-rte-category-training]
          note: "Interfaces do not establish whether an explicit operator decision supplied/approved each initial object; constructor injection and remaining shipped routes lack complete admission evidence. No manual value is inferred."
      records: [memory.md#mem-obj-candidate-record, memory.md#mem-obj-receipt-rubrics, memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-master-skill, runtime.md#rt-rte-task-evolution]
      note: "Automatic subsequent admission is wired, while initialization and alternatives remain unresolved."
    curation_operations:
      assessment: partial
      units:
        - scope: "Task skill/receipt revisions and category/domain skill updates"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [runtime.md#rt-rte-branch-refinement, runtime.md#rt-rte-receipt-revision, memory.md#mem-obj-category-round, runtime.md#rt-rte-domain-fusion]
              note: "Existing retained skill or scoring-rule entries are revised and selected for subsequent use, with different route-specific gates."
          records: [runtime.md#rt-rte-branch-refinement, runtime.md#rt-rte-receipt-revision, memory.md#mem-obj-category-round, runtime.md#rt-rte-domain-fusion, runtime.md#rt-clm-refinement-replay]
          note: "The revision route is wired; persistence of every accepted task refinement is qualified by replay of the original patch. Semantic improvement is not implied."
        - scope: "Candidate successor and category batch-winner promotion"
          assessment: known
          findings:
            - value: promote
              basis: wired
              records: [runtime.md#rt-rte-task-evolution, memory.md#mem-obj-category-round]
              note: "A retained candidate is raised to accepted parent, or a completed-round winner to batch/final input, by code selection."
          records: [runtime.md#rt-rte-task-evolution, memory.md#mem-obj-category-round]
          note: "Promotion changes reliance/tier without certifying all content. Domain fusion is not winner-only promotion."
        - scope: "Category and domain fusion over retained skill bodies"
          assessment: partial
          findings:
            - value: consolidate
              basis: claimed
              records: [epistemic.md#epi-rte-category-fusion, memory.md#mem-obj-master-skill]
              note: "Fusion requests preservation/combination of complementary retained workflows and domain rules into final guidance."
            - value: dedup
              basis: claimed
              records: [memory.md#mem-obj-master-skill]
              note: "The domain fusion prompt requests deduplication; structural output checks do not establish that duplicates were actually merged."
          records: [epistemic.md#epi-rte-category-fusion, memory.md#mem-obj-master-skill, runtime.md#rt-rte-domain-fusion]
          note: "The model-call and output-retention route is wired, but no linked output establishes semantic consolidation, deduplication or new-claim synthesis. Preserve request-level bases."
        - scope: "Behavior summary reduction, checkpoint deletion, final tree replacement and unresolved maintenance alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-behavior-summary, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-category-round, runtime.md#rt-rte-task-evolution]
          note: "Fixed diagnostic counts do not establish consolidation of claims; deleting obsolete checkpoints or replacing materialization alone establishes neither semantic decay nor history-preserving invalidation. Wider maintenance lacks accepted bounded coverage."
      records: [runtime.md#rt-rte-branch-refinement, runtime.md#rt-rte-receipt-revision, memory.md#mem-obj-category-round, memory.md#mem-obj-master-skill, memory.md#mem-obj-behavior-summary, runtime.md#rt-rte-task-evolution]
      note: "Wired revision/promotion coexist with requested fusion curation and unresolved semantic/maintenance operations. Route names and retention do not warrant synthesis, decay or invalidation."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Task replay, planning, receipt scoring/revision, editor inputs and logical-cell recovery"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-task-evolution, runtime.md#rt-rte-branch-refinement, runtime.md#rt-rte-receipt-revision, runtime.md#rt-rte-cell-recovery, memory.md#mem-obj-search-state]
              note: "The coordinator requests specific operations and retained inputs; scheduled file selection and delivery fulfill those requests rather than independently injecting memory."
          records: [runtime.md#rt-rte-task-evolution, runtime.md#rt-rte-branch-refinement, runtime.md#rt-rte-receipt-revision, runtime.md#rt-rte-cell-recovery, memory.md#mem-obj-search-state]
          note: "Task IDs, accepted IDs and model file selection do not make requested read-back push."
        - scope: "Category resume/fusion/test and domain checkpoint/fusion/held-out consumption"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-master-skill, runtime.md#rt-rte-category-training, runtime.md#rt-rte-domain-fusion, runtime.md#rt-bap-skill-delivery]
              note: "Explicit training, fusion and test operations load their specified snapshots, artifact inputs or complete final guide."
          records: [memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-master-skill, runtime.md#rt-rte-category-training, runtime.md#rt-rte-domain-fusion, runtime.md#rt-bap-skill-delivery]
          note: "Category uses winners; domain loads all current cluster skills. Neither establishes unsolicited foreground retrieval."
        - scope: "Raw trajectory/archive consumers, auxiliary host loading branches and remaining shipped alternatives"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-obj-behavior-summary, memory.md#mem-obj-revision-attempts, memory.md#mem-obj-skill-instructions, runtime.md#rt-rte-task-evolution]
          note: "No complete accepted consumer inventory resolves these alternatives; pull witnesses cannot establish a repository-wide pull-only boundary."
      records: [runtime.md#rt-rte-task-evolution, runtime.md#rt-rte-branch-refinement, runtime.md#rt-rte-receipt-revision, runtime.md#rt-rte-cell-recovery, runtime.md#rt-rte-category-training, runtime.md#rt-rte-domain-fusion, memory.md#mem-obj-behavior-summary]
      note: "Assessed operations are requested pull chains; unresolved consumers prevent known or absent push at system scope."
    read_back_signal:
      assessment: uninspected
      units:
        - scope: "Inspected requested task/category/domain read-back chains"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-task-evolution, runtime.md#rt-rte-branch-refinement, runtime.md#rt-rte-receipt-revision, runtime.md#rt-rte-cell-recovery, runtime.md#rt-rte-category-training, runtime.md#rt-rte-domain-fusion]
          note: "These operations fulfill explicit requests; push-signal classification does not apply to their IDs, budgets or optional file selector."
        - scope: "Unresolved raw trajectory, auxiliary loading and other shipped read-back alternatives"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-obj-behavior-summary, memory.md#mem-obj-skill-instructions, runtime.md#rt-rte-task-evolution]
          note: "Missing consumer/selector facts prevent determining whether a push exists and what signal selects retained parts."
      records: [runtime.md#rt-rte-task-evolution, runtime.md#rt-rte-branch-refinement, runtime.md#rt-rte-category-training, runtime.md#rt-rte-domain-fusion, memory.md#mem-obj-behavior-summary, memory.md#mem-obj-skill-instructions]
      note: "No positive push signal is established; unresolved alternatives prevent making the entire axis inapplicable. Identifiers in requested lookup are not identifier-based push."
    trace_learning:
      assessment: partial
      units:
        - scope: "Task scalar evaluation/proposal experience to retained search history/constraints and later planner"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-obj-search-state, runtime.md#rt-rte-task-evolution]
              note: "Automatic experience-fed writes retain history and rejected-direction constraints; later planning receives them and subsequent search is constrained by them."
          records: [memory.md#mem-obj-search-state, runtime.md#rt-rte-task-evolution]
          note: "A task-scoped durable behavior-shaping artifact qualifies without new knowledge, provider weight change or observed benefit."
        - scope: "Recorded oracle/verifier contrast to revised receipt and later scoring/refinement"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [runtime.md#rt-rte-receipt-revision, memory.md#mem-obj-receipt-rubrics, runtime.md#rt-bap-receipt-scoring]
              note: "Automatic rank-responsive receipt admission persists scoring guidance and supplies it to subsequent verifier/update calls."
          records: [runtime.md#rt-rte-receipt-revision, memory.md#mem-obj-receipt-rubrics, runtime.md#rt-bap-receipt-scoring]
          note: "Scalar experience is sufficient; trajectory exclusion does not negate this route."
        - scope: "Category/domain evaluation-responsive updates, snapshots and later training/final consumption"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, runtime.md#rt-rte-category-training, runtime.md#rt-rte-domain-fusion]
              note: "Recorded verifier/oracle outcomes guide automatic updates and winner selection; durable skills/receipts feed resumed training, fusion or later tests."
          records: [memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, runtime.md#rt-rte-category-training, runtime.md#rt-rte-domain-fusion]
          note: "Category and domain gates differ; no observed improvement or causal transfer is claimed. Fusion consumes retained training products, not established raw trajectories."
        - scope: "tau2 behavior-summary to policy, raw trajectory readers, diagnostic archive reuse and other shipped alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-behavior-summary, memory.md#mem-obj-revision-attempts, runtime.md#rt-rte-task-evolution]
          note: "Shared revision input excludes summary metadata, but unresolved other consumers and raw readers prevent a bounded no for the included alternative inventory. Diagnostic retention alone is insufficient."
      records: [memory.md#mem-obj-search-state, runtime.md#rt-rte-receipt-revision, memory.md#mem-obj-receipt-rubrics, memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-behavior-summary, runtime.md#rt-rte-task-evolution]
      note: "Several qualifying automatic trace-fed durable-text/control updates are wired. Remaining consumers are unresolved; no global negative or capacity-improvement conclusion follows."
    trace_source:
      assessment: partial
      units:
        - scope: "Task evaluation/proposal result records consumed by search-history and receipt-rule updates"
          assessment: known
          findings:
            - value: event-streams
              basis: wired
              records: [memory.md#mem-obj-search-state, runtime.md#rt-rte-task-evolution, runtime.md#rt-rte-receipt-revision]
              note: "Original qualifying inputs are discrete recorded candidate evaluation outcomes and rejected/admitted proposal events, projected to scalar history and rank/criterion contrast."
          records: [memory.md#mem-obj-search-state, runtime.md#rt-rte-task-evolution, runtime.md#rt-rte-receipt-revision]
          note: "These are runtime outcome events, not conversational session turns or full linked benchmark state/action trajectories. Static task and visible skill text are mixed nontrace context, not additional trace-source values."
        - scope: "Category/domain verifier and benchmark outcome records feeding retained updates"
          assessment: known
          findings:
            - value: event-streams
              basis: wired
              records: [memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, runtime.md#rt-rte-category-training, runtime.md#rt-rte-domain-fusion]
              note: "Discrete recorded evaluation results and round selection/update outcomes are the evidenced experience input to durable skills/receipt updates."
          records: [memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, runtime.md#rt-rte-category-training, runtime.md#rt-rte-domain-fusion]
          note: "Fusion later uses retained skill bodies; domain inputs include all current skills. Neither fusion adapter labels nor saved diagnostic traces establish a new original trace source."
        - scope: "Possible summary/raw-trajectory learning routes and remaining shipped alternatives"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-obj-behavior-summary, memory.md#mem-obj-revision-attempts, runtime.md#rt-rte-task-evolution]
          note: "Simulation messages/tool calls explain diagnostic lineage, but no qualifying summary-to-rule consumer is established. Raw payload/readers and alternative learning inputs remain unresolved; do not infer session-logs, tool-traces or trajectories from their storage alone."
      records: [memory.md#mem-obj-search-state, runtime.md#rt-rte-receipt-revision, memory.md#mem-obj-category-round, memory.md#mem-obj-cluster-checkpoint, memory.md#mem-obj-behavior-summary, runtime.md#rt-rte-task-evolution]
      note: "Runtime evaluation-event inputs are supported on qualifying routes. Unresolved trace consumers prevent complete source coverage; trace-derived diagnostics without a qualifying later update do not add source values."
---

# SkillLift memory profile

## Comparison rationale

The comparison covers retained improvement-plane memory, not every object in
SkillLift's runtime. File trees, patch recipes, JSON checkpoints, receipt
rules and recorded outcome history reach later rounds or test invocations.
The ephemeral evidence view is a transformation of these inputs, not an
additional memory store. Remote inference components do not establish
use-accumulated provider memory: [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client)
leaves provider mutability unresolved. This profile does not turn that runtime
component's distributed-parametric form into a memory finding.

Natural-language bodies and symbolic control fields have different consumers.
Retained skill text supplies instructions to benchmark agents; retained hashes,
accepted IDs and validity fields instead route or veto reconstruction and
reuse. Receipt text directs verifier judgments, while points and hits determine
ranking and code thresholds. Retained score/proposal experience also has
learning authority at the update consumer, independently of the generated
receipt's instruction authority at the next verifier. See
[MEM-OBJ-candidate-record](memory.md#mem-obj-candidate-record),
[MEM-OBJ-search-state](memory.md#mem-obj-search-state),
[MEM-OBJ-receipt-rubrics](memory.md#mem-obj-receipt-rubrics) and
[RT-BAP-receipt-scoring](runtime.md#rt-bap-receipt-scoring).
None of these classifications claims observed compliance, accurate diagnosis
or demonstrated improvement.

The qualifying trace-learning witnesses are automatic durable updates from
recorded evaluation/proposal events to later search, skill or scoring behavior.
Full benchmark conversations are not needed for these witnesses. Their original
recorded input is discrete runtime outcome experience, hence event-streams,
not a session-log merely because models participate. Static task text and skill
bodies remain nontrace inputs. The message/tool-derived summary in
[MEM-OBJ-behavior-summary](memory.md#mem-obj-behavior-summary) is different:
it has trace-extracted lineage but its feedback metadata is projected out of
shared receipt revision. Saved raw trajectories and uninspected readers cannot
establish either additional trace-learning sources or a global negative.

Read-back in the assessed chains is pull. Coordinator requests for planning,
replay, calibration and testing cause code to fetch the specified material.
A selector model choosing optional editor files fulfills that request; it is
not independent push. Thus IDs and budgets on these chains supply no positive
push-signal finding. Unresolved consumers leave the system-level signal axis
uninspected rather than inapplicable. See
[RT-RTE-branch-refinement](runtime.md#rt-rte-branch-refinement),
[RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution) and
[RT-RTE-domain-fusion](runtime.md#rt-rte-domain-fusion).

Wired evolution and promotion do not certify semantic curation. Domain fusion
requests deduplication and preservation of disputed rules; category fusion
requests complementary workflows. Their structural checks do not prove these
transformations occurred, so consolidation and deduplication keep claimed
bases. No linked output establishes synthesis of a new claim. Checkpoint cleanup
and materialized-tree replacement are not by themselves decay or
history-preserving invalidation. See
[MEM-OBJ-master-skill](memory.md#mem-obj-master-skill),
[EPI-RTE-category-fusion](epistemic.md#epi-rte-category-fusion) and
[MEM-OBJ-cluster-checkpoint](memory.md#mem-obj-cluster-checkpoint).

Reconciliation establishes no supersessions, so each citation retains its
canonical declaring member. Its corrected domain connection matters to lineage
and selection: [RT-RTE-domain-fusion](runtime.md#rt-rte-domain-fusion)
exports/loads every current cluster skill, not just an oracle-ranked winner.
Category fusion still uses batch winners. Its corrected evidence-packing
connection also matters: exact `SKILL.md` key protection does not cover all
prefixed instruction paths under a budget, while ordinary task Mode B uses no
evidence budget and can reject an oversized request instead. See
[EPI-RTE-evidence-packing](epistemic.md#epi-rte-evidence-packing) and the
memory annotation on
[RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision).
Neither corrected connection upgrades semantic checking.

The conditional replay defect in
[RT-CLM-refinement-replay](runtime.md#rt-clm-refinement-replay)
qualifies persistence of accepted refined task bodies, not existence of the
revision route or category/domain full snapshots. Initial content control,
auxiliary payload consumers, raw trajectory readers and other shipped
baseline/entry-point mechanisms lack complete accepted classification records.
They remain included unresolved alternatives; positive witnesses cannot make
the inventory complete. No absence records justify system-wide negative values.

Source-read log: none. The supplied accepted records, their annotations and
reconciliation resolved the classification questions without frozen-source
inspection. No records, evidence passages or source identities were added.
