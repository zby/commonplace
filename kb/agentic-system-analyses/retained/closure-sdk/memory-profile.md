---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Memory comparison of Closure-SDK current Rust Closure EA numerical fields, helper caches and checkpoint alternatives."
run-id: "AAS-2026-10-13-closure-sdk-294e6865ca51-01"
source-identity: "https://github.com/faltz009/Closure-SDK"
reviewed-boundary: "9735f48a6ddd00b6f429a91443489531b3a115ef"
memory-comparison:
  version: 2
  scope: "Included: use-accumulated Closure EA genomes (DNA, Epigenetic, Response), buffer, access/correction statistics, closure histories/events, pending feedback, caller-side Vocabulary/MusicEncoder caches, CurriculumTrace replay input, BrainState, genome-only and vocabulary checkpoint routes and their recorded later consumers. Included unresolved alternatives: accumulated helper-state parts, arbitrary caller mutation/replacement provenance and untraced example-consumer variants. Excluded: static compiled control code as memory, unconsumed returned reports/promotion packets, sibling integrity SDK/database, archived Python runtime, separate homeostasis demo, browser implementation and external compiler/filesystem responsibilities."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Live genomes, buffer, statistics, histories, pending prediction and replay input"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-three-cell"
                - "memory.md#mem-obj-buffer"
                - "memory.md#mem-obj-genome-statistics"
                - "memory.md#mem-obj-closure-histories"
                - "runtime.md#rt-obj-pending-prediction"
                - "memory.md#mem-obj-curriculum-trace"
              note: "Owned Rust fields retain carriers, aggregates and replay data between calls."
          records:
            - "runtime.md#rt-cmp-three-cell"
            - "memory.md#mem-obj-buffer"
            - "memory.md#mem-obj-dna"
            - "memory.md#mem-obj-epigenetic"
            - "memory.md#mem-obj-response"
            - "memory.md#mem-obj-genome-statistics"
            - "memory.md#mem-obj-closure-histories"
            - "runtime.md#rt-obj-pending-prediction"
            - "memory.md#mem-obj-curriculum-trace"
          note: "These named objects have inspected Rust field/vector storage; file encodings are classified separately."
        - scope: "Vocabulary and MusicEncoder live maps"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vocabulary"
                - "memory.md#mem-obj-music-encoder"
              note: "String/carrier and role/base associations reside in process-local maps."
          records:
            - "memory.md#mem-obj-vocabulary"
            - "memory.md#mem-obj-music-encoder"
          note: "The caches are local HashMaps, not an established external KV service."
        - scope: "BrainState and Vocabulary JSON checkpoints"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-brain-state"
                - "runtime.md#rt-rte-state-restoration"
                - "memory.md#mem-obj-vocabulary"
                - "epistemic.md#epi-rte-vocabulary-codec"
              note: "Explicit files retain selected operational state and forward token mappings."
          records:
            - "memory.md#mem-obj-brain-state"
            - "runtime.md#rt-rte-state-restoration"
            - "memory.md#mem-obj-vocabulary"
            - "epistemic.md#epi-rte-vocabulary-codec"
          note: "Named serializers write local files; JSON is encoding, not a separate substrate."
        - scope: "Genome-only checkpoint"
          assessment: "known"
          findings:
            - value: "files"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-genome-reconstruction"
              note: "Genome save/load retains the selected genome in a JSON file."
          records:
            - "memory.md#mem-rte-genome-reconstruction"
          note: "The distinct genome-only reuse route is afforded, not shipped cross-process use."
        - scope: "Included helper-state and additional example-consumer alternatives within ThreeCell"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-three-cell"
            - "runtime.md#rt-rte-carrier-ingest"
            - "runtime.md#rt-rte-readonly-consumption"
          note: "The accepted account leaves detailed body-state, localization and other helper internals and example variants unaudited. Their accumulated-state parts and subsequent consumers are not independently enumerated; the known field routes do not classify those alternatives."
      records:
        - "runtime.md#rt-cmp-three-cell"
        - "memory.md#mem-obj-buffer"
        - "memory.md#mem-obj-dna"
        - "memory.md#mem-obj-epigenetic"
        - "memory.md#mem-obj-response"
        - "memory.md#mem-obj-genome-statistics"
        - "memory.md#mem-obj-closure-histories"
        - "runtime.md#rt-obj-pending-prediction"
        - "memory.md#mem-obj-curriculum-trace"
        - "memory.md#mem-obj-vocabulary"
        - "memory.md#mem-obj-music-encoder"
        - "memory.md#mem-obj-brain-state"
        - "runtime.md#rt-rte-state-restoration"
        - "epistemic.md#epi-rte-vocabulary-codec"
        - "memory.md#mem-rte-genome-reconstruction"
        - "runtime.md#rt-rte-carrier-ingest"
        - "runtime.md#rt-rte-readonly-consumption"
      note: "Coverage includes live numerical and symbolic objects plus all three recorded checkpoint alternatives and caller-side caches. Unenumerated helper-state alternatives prevent complete substrate coverage."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Dense carriers, addresses, values, eligibility and numerical aggregates at geometric consumers"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-three-cell"
                - "memory.md#mem-obj-dna"
                - "memory.md#mem-obj-epigenetic"
                - "memory.md#mem-obj-response"
                - "memory.md#mem-obj-genome-statistics"
                - "runtime.md#rt-obj-pending-prediction"
              note: "Distributed quaternion geometry and evolving numerical aggregates shape field reads and updates; this is not a claim of neural-model weights."
          records:
            - "runtime.md#rt-cmp-three-cell"
            - "memory.md#mem-obj-buffer"
            - "memory.md#mem-obj-dna"
            - "memory.md#mem-obj-epigenetic"
            - "memory.md#mem-obj-response"
            - "memory.md#mem-obj-genome-statistics"
            - "memory.md#mem-obj-closure-histories"
            - "runtime.md#rt-obj-pending-prediction"
          note: "Numerical parts are separated from tags and fixed-rule metadata."
        - scope: "Layer tags, indices, edge counts, ages, intervals and checkpoint organization"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-buffer"
                - "memory.md#mem-obj-genome-statistics"
                - "memory.md#mem-obj-closure-histories"
                - "runtime.md#rt-obj-pending-prediction"
                - "memory.md#mem-obj-brain-state"
              note: "Localized indices, counts and tags determine expiry, transitions, admission and reconstruction."
          records:
            - "memory.md#mem-obj-buffer"
            - "memory.md#mem-obj-genome-statistics"
            - "memory.md#mem-obj-closure-histories"
            - "runtime.md#rt-obj-pending-prediction"
            - "memory.md#mem-obj-brain-state"
          note: "Fixed-rule metadata remains symbolic even when serialized beside dense carriers."
        - scope: "Vocabulary and role-cache numerical embeddings"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vocabulary"
                - "memory.md#mem-obj-music-encoder"
                - "epistemic.md#epi-rte-vocabulary-codec"
              note: "Hash-derived S2 bases and carriers feed numerical encoding and distance selection."
          records:
            - "memory.md#mem-obj-vocabulary"
            - "memory.md#mem-obj-music-encoder"
            - "epistemic.md#epi-rte-vocabulary-codec"
          note: "Dense bases/carriers are operative numerical mappings, not merely their display labels."
        - scope: "Vocabulary keys/display labels, role keys and curriculum labels/window indices"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vocabulary"
                - "memory.md#mem-obj-music-encoder"
                - "memory.md#mem-obj-curriculum-trace"
                - "epistemic.md#epi-rte-vocabulary-codec"
              note: "Exact lookup, normalization, reverse-key decode and replay indexing consume localized symbols."
          records:
            - "memory.md#mem-obj-vocabulary"
            - "memory.md#mem-obj-music-encoder"
            - "memory.md#mem-obj-curriculum-trace"
            - "epistemic.md#epi-rte-vocabulary-codec"
          note: "The established paths use strings as fixed-rule keys or display outputs. No retained prose instruction or human/model semantic consumer is established."
        - scope: "Curriculum retained carrier sequence"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-curriculum-trace"
              note: "Replayed quaternion inputs enter the numerical field."
          records:
            - "memory.md#mem-obj-curriculum-trace"
          note: "The sequence contains dense carriers distinct from labels and window indices."
        - scope: "Included helper-state and additional example-consumer alternatives within ThreeCell"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-three-cell"
            - "runtime.md#rt-rte-carrier-ingest"
            - "runtime.md#rt-rte-readonly-consumption"
          note: "The accepted account leaves detailed body-state, localization and other helper internals and example variants unaudited. Their accumulated-state parts and subsequent consumers are not independently enumerated; the known field routes do not classify those alternatives."
      records:
        - "runtime.md#rt-cmp-three-cell"
        - "memory.md#mem-obj-buffer"
        - "memory.md#mem-obj-dna"
        - "memory.md#mem-obj-epigenetic"
        - "memory.md#mem-obj-response"
        - "memory.md#mem-obj-genome-statistics"
        - "memory.md#mem-obj-closure-histories"
        - "runtime.md#rt-obj-pending-prediction"
        - "memory.md#mem-obj-brain-state"
        - "memory.md#mem-obj-vocabulary"
        - "memory.md#mem-obj-music-encoder"
        - "epistemic.md#epi-rte-vocabulary-codec"
        - "memory.md#mem-obj-curriculum-trace"
        - "runtime.md#rt-rte-carrier-ingest"
        - "runtime.md#rt-rte-readonly-consumption"
      note: "Mixed numerical and symbolic objects are split by operative part. Display text does not establish natural-language behavioral consumption. Uninspected helper and consumer alternatives prevent a complete form inventory."
    lineage:
      assessment: "partial"
      units:
        - scope: "Source-defined initial DNA and orbit seeds"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-dna"
                - "runtime.md#rt-rte-direct-maintenance"
              note: "Source-defined structural seeds provide initial authored material."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-dna"
                - "runtime.md#rt-rte-direct-maintenance"
              note: "Enumerating generator powers derives additional seed geometry by fixed computation."
          records:
            - "memory.md#mem-obj-dna"
            - "runtime.md#rt-rte-direct-maintenance"
          note: "This unit covers literal/structural seeding, not arbitrary caller replacements."
        - scope: "Caller-supplied carriers, targets and checkpoint installations"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-buffer"
                - "memory.md#mem-obj-response"
                - "memory.md#mem-obj-brain-state"
                - "memory.md#mem-rte-genome-reconstruction"
                - "runtime.md#rt-rte-state-restoration"
              note: "Caller carriers/targets and serialized fields enter memory from outside the receiving object."
          records:
            - "memory.md#mem-obj-buffer"
            - "memory.md#mem-obj-response"
            - "memory.md#mem-obj-brain-state"
            - "memory.md#mem-rte-genome-reconstruction"
            - "runtime.md#rt-rte-state-restoration"
          note: "Entry into the subsystem is recorded; upstream authorship, carrier encoding provenance and checkpoint trust are not. Imported material is not thereby trace-extracted."
        - scope: "Query/correction statistics and trace-conditioned learned geometry"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-genome-statistics"
                - "runtime.md#rt-rte-prediction-feedback"
                - "memory.md#mem-rte-memory-consolidation"
              note: "Queries, commits and target evaluations accumulate coupling/coalition/salience traces used to derive changed fields."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-epigenetic"
                - "memory.md#mem-rte-hierarchy-retention"
                - "memory.md#mem-rte-memory-consolidation"
              note: "Closure composition, interpolation, merging and promotion compute derived numerical objects."
          records:
            - "memory.md#mem-obj-genome-statistics"
            - "memory.md#mem-obj-epigenetic"
            - "runtime.md#rt-rte-prediction-feedback"
            - "memory.md#mem-rte-memory-consolidation"
            - "memory.md#mem-rte-hierarchy-retention"
          note: "This unit covers recorded runtime derivation paths, not the unknown initial meanings of input geometry."
        - scope: "Vocabulary and role-cache input labels and compiled embeddings"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vocabulary"
                - "memory.md#mem-obj-music-encoder"
                - "epistemic.md#epi-rte-vocabulary-codec"
              note: "Caller token/role strings and explicit registered geometry enter the maps."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vocabulary"
                - "memory.md#mem-obj-music-encoder"
                - "epistemic.md#epi-rte-vocabulary-codec"
              note: "Deterministic hashing and phase construction derive numerical encoding from labels."
          records:
            - "memory.md#mem-obj-vocabulary"
            - "memory.md#mem-obj-music-encoder"
            - "epistemic.md#epi-rte-vocabulary-codec"
          note: "Hashing/caching and registration are known, but arbitrary supplied label/geometry origins are not."
        - scope: "Curriculum replay sequence"
          assessment: "partial"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-curriculum-trace"
              note: "Caller-authored windows organize the retained sequence."
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-curriculum-trace"
              note: "The runtime receives the caller sequence for replay."
          records:
            - "memory.md#mem-obj-curriculum-trace"
          note: "The replay object is caller-authored; whether a caller assembled synthetic inputs or recorded experience is unresolved."
        - scope: "Included helper-state and additional example-consumer alternatives within ThreeCell"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-three-cell"
            - "runtime.md#rt-rte-carrier-ingest"
            - "runtime.md#rt-rte-readonly-consumption"
          note: "The accepted account leaves detailed body-state, localization and other helper internals and example variants unaudited. Their accumulated-state parts and subsequent consumers are not independently enumerated; the known field routes do not classify those alternatives."
      records:
        - "memory.md#mem-obj-dna"
        - "runtime.md#rt-rte-direct-maintenance"
        - "memory.md#mem-obj-buffer"
        - "memory.md#mem-obj-response"
        - "memory.md#mem-obj-brain-state"
        - "memory.md#mem-rte-genome-reconstruction"
        - "runtime.md#rt-rte-state-restoration"
        - "memory.md#mem-obj-genome-statistics"
        - "memory.md#mem-obj-epigenetic"
        - "runtime.md#rt-rte-prediction-feedback"
        - "memory.md#mem-rte-memory-consolidation"
        - "memory.md#mem-rte-hierarchy-retention"
        - "memory.md#mem-obj-vocabulary"
        - "memory.md#mem-obj-music-encoder"
        - "epistemic.md#epi-rte-vocabulary-codec"
        - "memory.md#mem-obj-curriculum-trace"
        - "runtime.md#rt-cmp-three-cell"
        - "runtime.md#rt-rte-carrier-ingest"
        - "runtime.md#rt-rte-readonly-consumption"
      note: "Known derivation paths do not settle upstream provenance or every helper-state alternative; local authored, imported, compiled and trace-extracted findings coexist."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Carrier content at later field and recall consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-buffer"
                - "memory.md#mem-obj-response"
                - "runtime.md#rt-rte-readonly-consumption"
                - "runtime.md#rt-bap-field-consumption"
              note: "Later field reads and associative recall consume retained values as context or answer content."
          records:
            - "memory.md#mem-obj-buffer"
            - "memory.md#mem-obj-dna"
            - "memory.md#mem-obj-epigenetic"
            - "memory.md#mem-obj-response"
            - "runtime.md#rt-rte-readonly-consumption"
            - "runtime.md#rt-bap-field-consumption"
          note: "Returned values supply numerical context/prediction content, not standing natural-language directions."
        - scope: "Retained addresses and counts at relative-selection consumers"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-response"
                - "runtime.md#rt-rte-readonly-consumption"
                - "memory.md#mem-obj-vocabulary"
                - "epistemic.md#epi-rte-vocabulary-codec"
              note: "Retained address/base geometry influences closest-match priority."
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-genome-statistics"
                - "runtime.md#rt-rte-readonly-consumption"
              note: "Retained edge counts determine the highest-count successor."
          records:
            - "memory.md#mem-obj-dna"
            - "memory.md#mem-obj-response"
            - "memory.md#mem-obj-genome-statistics"
            - "runtime.md#rt-rte-readonly-consumption"
            - "epistemic.md#epi-rte-vocabulary-codec"
            - "memory.md#mem-obj-vocabulary"
          note: "Scoring fixed retained addresses is ranking even without learned ranking policy."
        - scope: "Retained indices, edges and hierarchy state at operation-selection consumers"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-genome-statistics"
                - "runtime.md#rt-obj-pending-prediction"
                - "memory.md#mem-rte-hierarchy-retention"
              note: "Sequential edges, pending eligibility/source indices and hierarchy levels select destinations or update scope."
          records:
            - "memory.md#mem-obj-genome-statistics"
            - "memory.md#mem-obj-closure-histories"
            - "runtime.md#rt-obj-pending-prediction"
            - "memory.md#mem-rte-hierarchy-retention"
          note: "State selects subsequent inputs, transition destinations and update targets."
        - scope: "Layer and access statistics at correction/maintenance admission"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-dna"
                - "memory.md#mem-obj-genome-statistics"
                - "memory.md#mem-rte-memory-consolidation"
              note: "Layer, coupling, recurrence and coalition data determine correction, merge, survival and promotion eligibility."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-dna"
                - "memory.md#mem-obj-genome-statistics"
                - "memory.md#mem-rte-memory-consolidation"
                - "epistemic.md#epi-rte-category-disposition"
              note: "DNA-layer checks refuse correction/merge/prune and maintenance gates exclude inadmissible entries."
          records:
            - "memory.md#mem-obj-dna"
            - "memory.md#mem-obj-genome-statistics"
            - "memory.md#mem-rte-memory-consolidation"
            - "epistemic.md#epi-rte-category-disposition"
          note: "The force belongs to consumed layer/statistical controls, not every numerical result."
        - scope: "Retained observation/feedback state and statistics at automatic updates"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-buffer"
                - "memory.md#mem-obj-closure-histories"
                - "runtime.md#rt-obj-pending-prediction"
                - "memory.md#mem-obj-genome-statistics"
                - "runtime.md#rt-rte-prediction-feedback"
                - "memory.md#mem-rte-memory-consolidation"
              note: "Retained observations, staged experience and aggregates feed durable numerical-field changes."
          records:
            - "memory.md#mem-obj-buffer"
            - "memory.md#mem-obj-closure-histories"
            - "runtime.md#rt-obj-pending-prediction"
            - "memory.md#mem-obj-genome-statistics"
            - "runtime.md#rt-rte-prediction-feedback"
            - "memory.md#mem-rte-memory-consolidation"
          note: "Update-consumer authority is separate from the output field's knowledge/ranking force."
        - scope: "Vocabulary and role keys at lookup/encoding consumers"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vocabulary"
                - "memory.md#mem-obj-music-encoder"
                - "epistemic.md#epi-rte-vocabulary-codec"
              note: "Exact token/bit/role matches select the mapping used to return geometry or a display token."
          records:
            - "memory.md#mem-obj-vocabulary"
            - "memory.md#mem-obj-music-encoder"
            - "epistemic.md#epi-rte-vocabulary-codec"
          note: "Keys choose retained associations; decoded display labels have no established semantic downstream consumer."
        - scope: "Installed checkpoints and explicit higher-level reads"
          assessment: "partial"
          findings:
            - value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-genome-reconstruction"
                - "memory.md#mem-rte-hierarchy-retention"
              note: "Resumed-training and explicit level-read consumers can receive retained numerical content."
          records:
            - "memory.md#mem-obj-brain-state"
            - "memory.md#mem-rte-genome-reconstruction"
            - "memory.md#mem-rte-hierarchy-retention"
            - "memory.md#mem-rte-memory-consolidation"
          note: "Installed field parts retain the forces above, but automatic promoted-category delivery to primary prediction and vocabulary display interpretation are not established."
        - scope: "Included helper-state and additional example-consumer alternatives within ThreeCell"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-three-cell"
            - "runtime.md#rt-rte-carrier-ingest"
            - "runtime.md#rt-rte-readonly-consumption"
          note: "The accepted account leaves detailed body-state, localization and other helper internals and example variants unaudited. Their accumulated-state parts and subsequent consumers are not independently enumerated; the known field routes do not classify those alternatives."
      records:
        - "memory.md#mem-obj-buffer"
        - "memory.md#mem-obj-dna"
        - "memory.md#mem-obj-epigenetic"
        - "memory.md#mem-obj-response"
        - "runtime.md#rt-rte-readonly-consumption"
        - "runtime.md#rt-bap-field-consumption"
        - "memory.md#mem-obj-genome-statistics"
        - "epistemic.md#epi-rte-vocabulary-codec"
        - "memory.md#mem-obj-vocabulary"
        - "memory.md#mem-obj-closure-histories"
        - "runtime.md#rt-obj-pending-prediction"
        - "memory.md#mem-rte-hierarchy-retention"
        - "memory.md#mem-rte-memory-consolidation"
        - "epistemic.md#epi-rte-category-disposition"
        - "runtime.md#rt-rte-prediction-feedback"
        - "memory.md#mem-obj-music-encoder"
        - "memory.md#mem-obj-brain-state"
        - "memory.md#mem-rte-genome-reconstruction"
        - "runtime.md#rt-cmp-three-cell"
        - "runtime.md#rt-rte-carrier-ingest"
      note: "Recorded consumer effects support knowledge, ranking, routing, validation, enforcement and learning locally. No blanket instruction authority follows from executable influence; unestablished consumers prevent a complete authority union."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Buffer admission, structural/hierarchy writes, feedback and maintenance software admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-carrier-ingest"
                - "runtime.md#rt-rte-prediction-feedback"
                - "memory.md#mem-rte-hierarchy-retention"
                - "memory.md#mem-rte-memory-consolidation"
                - "epistemic.md#epi-rte-response-write"
              note: "Compiled checks admit carriers, numerical corrections, merges and promotions without a per-content human decision."
          records:
            - "runtime.md#rt-rte-carrier-ingest"
            - "runtime.md#rt-rte-prediction-feedback"
            - "memory.md#mem-rte-hierarchy-retention"
            - "memory.md#mem-rte-memory-consolidation"
            - "epistemic.md#epi-rte-response-write"
          note: "Calling a workflow or forcing maintenance does not make its per-content admission manual."
        - scope: "Fixed seeding, direct learn_response and cache admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-direct-maintenance"
                - "memory.md#mem-obj-response"
                - "memory.md#mem-obj-vocabulary"
                - "memory.md#mem-obj-music-encoder"
                - "epistemic.md#epi-rte-vocabulary-codec"
              note: "Software admits specified seeds, context/target associations and hashed/registered mappings."
          records:
            - "runtime.md#rt-rte-direct-maintenance"
            - "memory.md#mem-obj-response"
            - "memory.md#mem-obj-vocabulary"
            - "memory.md#mem-obj-music-encoder"
            - "epistemic.md#epi-rte-vocabulary-codec"
          note: "These software mechanisms append, interpolate or cache content without a human approval gate."
        - scope: "BrainState software installation"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-state-restoration"
                - "memory.md#mem-obj-brain-state"
              note: "Constructor installs accepted representation without per-entry human approval."
          records:
            - "runtime.md#rt-rte-state-restoration"
            - "memory.md#mem-obj-brain-state"
          note: "Parsing/construction installs fields; upstream replacement choice is a separate unit."
        - scope: "Genome-only software installation"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-genome-reconstruction"
              note: "Loader/constructor installs supplied genome content outside ordinary stream admission."
          records:
            - "memory.md#mem-rte-genome-reconstruction"
          note: "The intended resumed-training route remains afforded."
        - scope: "Arbitrary public mutation and caller choice/edit/replacement of checkpoints or initial content"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-direct-maintenance"
            - "runtime.md#rt-rte-state-restoration"
            - "memory.md#mem-rte-genome-reconstruction"
            - "memory.md#mem-obj-response"
          note: "Generic caller identity establishes neither an explicit human per-content decision nor an independently evidenced automatic upstream replacement mechanism. No manual finding can be derived from save/load selection alone."
        - scope: "Included helper-state and additional example-consumer alternatives within ThreeCell"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-three-cell"
            - "runtime.md#rt-rte-carrier-ingest"
            - "runtime.md#rt-rte-readonly-consumption"
          note: "The accepted account leaves detailed body-state, localization and other helper internals and example variants unaudited. Their accumulated-state parts and subsequent consumers are not independently enumerated; the known field routes do not classify those alternatives."
      records:
        - "runtime.md#rt-rte-carrier-ingest"
        - "runtime.md#rt-rte-prediction-feedback"
        - "memory.md#mem-rte-hierarchy-retention"
        - "memory.md#mem-rte-memory-consolidation"
        - "epistemic.md#epi-rte-response-write"
        - "runtime.md#rt-rte-direct-maintenance"
        - "memory.md#mem-obj-response"
        - "memory.md#mem-obj-vocabulary"
        - "memory.md#mem-obj-music-encoder"
        - "epistemic.md#epi-rte-vocabulary-codec"
        - "runtime.md#rt-rte-state-restoration"
        - "memory.md#mem-obj-brain-state"
        - "memory.md#mem-rte-genome-reconstruction"
        - "runtime.md#rt-cmp-three-cell"
        - "runtime.md#rt-rte-readonly-consumption"
      note: "Automatic admission is known on named implementation routes. Caller-controlled mutation and replacement lack control-principal evidence, and helper alternatives remain uninspected."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Same-layer consolidation pass over retained entries"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-consolidation"
              note: "Merging combines retained address/value and selected support material into fewer entries."
            - value: "dedup"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-consolidation"
              note: "Closest eligible near-address pairs are merged and losers removed; Response also requires value proximity."
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-consolidation"
              note: "Surviving entries receive changed values, addresses, width and metadata."
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-consolidation"
                - "epistemic.md#epi-rte-category-disposition"
              note: "BKT/coalition pruning forgets selected mutable entries rather than retaining a withdrawal history."
            - value: "promote"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-consolidation"
                - "epistemic.md#epi-rte-category-disposition"
              note: "Eligible Response values are raised to level-1 memory when not already covered."
          records:
            - "memory.md#mem-rte-memory-consolidation"
            - "epistemic.md#epi-rte-category-disposition"
          note: "This unit classifies inspected numerical transformations, not semantic warrant or effectiveness."
        - scope: "Existing Epigenetic and Response correction paths"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-epigenetic"
                - "memory.md#mem-obj-response"
                - "epistemic.md#epi-rte-response-write"
              note: "SLERP and target-directed credit revise previously retained entries."
          records:
            - "memory.md#mem-obj-epigenetic"
            - "memory.md#mem-obj-response"
            - "epistemic.md#epi-rte-response-write"
          note: "Nearest-entry correction changes existing numerical values; creation is a separate acquisition path."
        - scope: "Buffer expiry and retained history-window reduction"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-obj-buffer"
                - "memory.md#mem-obj-closure-histories"
              note: "Expiry forgets untagged observations and closed history windows are removed."
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-closure-histories"
                - "memory.md#mem-rte-hierarchy-retention"
              note: "Retained history carriers are composed into closure products while unresolved prefixes remain."
          records:
            - "memory.md#mem-obj-buffer"
            - "memory.md#mem-obj-closure-histories"
            - "runtime.md#rt-rte-carrier-ingest"
            - "memory.md#mem-rte-hierarchy-retention"
          note: "Reduction and forgetting are distinct coexisting effects; discarded windows are not historical invalidation records."
        - scope: "Vocabulary forward-map replacement"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vocabulary"
                - "epistemic.md#epi-rte-vocabulary-codec"
              note: "Explicit registration replaces an existing token-to-carrier association."
          records:
            - "memory.md#mem-obj-vocabulary"
            - "epistemic.md#epi-rte-vocabulary-codec"
          note: "Register changes the forward association but leaves stale reverse aliases until reload."
        - scope: "Meaning relation of numerical derived carriers and untraced maintenance alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-epigenetic"
            - "memory.md#mem-rte-memory-consolidation"
            - "memory.md#mem-rte-hierarchy-retention"
          note: "Numerical composition/merging does not establish a new claim absent from the inputs. These records cannot establish synthesize, and missing carrier interpretation cannot establish its bounded absence."
        - scope: "Included helper-state and additional example-consumer alternatives within ThreeCell"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-three-cell"
            - "runtime.md#rt-rte-carrier-ingest"
            - "runtime.md#rt-rte-readonly-consumption"
          note: "The accepted account leaves detailed body-state, localization and other helper internals and example variants unaudited. Their accumulated-state parts and subsequent consumers are not independently enumerated; the known field routes do not classify those alternatives."
      records:
        - "memory.md#mem-rte-memory-consolidation"
        - "epistemic.md#epi-rte-category-disposition"
        - "memory.md#mem-obj-epigenetic"
        - "memory.md#mem-obj-response"
        - "epistemic.md#epi-rte-response-write"
        - "memory.md#mem-obj-buffer"
        - "memory.md#mem-obj-closure-histories"
        - "runtime.md#rt-rte-carrier-ingest"
        - "memory.md#mem-rte-hierarchy-retention"
        - "memory.md#mem-obj-vocabulary"
        - "epistemic.md#epi-rte-vocabulary-codec"
        - "runtime.md#rt-cmp-three-cell"
        - "runtime.md#rt-rte-readonly-consumption"
      note: "The recorded curation union contains consolidation, deduplication, evolution, decay and promotion. Pruning without retained history is not invalidate; carrier semantics and unaudited alternatives prevent a complete transformation classification."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Requested ingest, feedback, evaluate, generate, solve and orbit computations over retained state"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-carrier-ingest"
                - "runtime.md#rt-rte-prediction-feedback"
                - "runtime.md#rt-rte-readonly-consumption"
                - "epistemic.md#epi-rte-slot-solver"
                - "workflow.md#wf-rte-regime-comparison"
              note: "Caller query/sequence/seed/target invokes a computation that selects and consumes accumulated numerical memory."
          records:
            - "runtime.md#rt-rte-carrier-ingest"
            - "runtime.md#rt-rte-prediction-feedback"
            - "runtime.md#rt-rte-readonly-consumption"
            - "epistemic.md#epi-rte-slot-solver"
            - "workflow.md#wf-rte-regime-comparison"
          note: "Internal selection and return fulfill caller computation requests; delivery is not another push."
        - scope: "Explicit higher-level and genome-only resumed-training consumers"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-hierarchy-retention"
                - "memory.md#mem-rte-genome-reconstruction"
              note: "Caller-selected level/address or resumed object supplies the requested retained field."
          records:
            - "memory.md#mem-rte-hierarchy-retention"
            - "memory.md#mem-rte-genome-reconstruction"
          note: "These consumer roles/capabilities are afforded; automatic promoted-category delivery into primary inference is not established."
        - scope: "Vocabulary and role-cache later lookup/encoding calls"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vocabulary"
                - "memory.md#mem-obj-music-encoder"
                - "epistemic.md#epi-rte-vocabulary-codec"
              note: "Caller token/role/carrier requests select retained associations."
          records:
            - "memory.md#mem-obj-vocabulary"
            - "memory.md#mem-obj-music-encoder"
            - "epistemic.md#epi-rte-vocabulary-codec"
          note: "Lookup, decode and encoding are requested helper computations."
        - scope: "Explicit full-state reconstruction"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-state-restoration"
                - "memory.md#mem-obj-brain-state"
              note: "Requested file/state load installs retained fields for subsequent computation."
          records:
            - "runtime.md#rt-rte-state-restoration"
            - "memory.md#mem-obj-brain-state"
          note: "A caller requests a chosen checkpoint; its payload is not automatically injected."
        - scope: "Included helper-state and additional example-consumer alternatives within ThreeCell"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-three-cell"
            - "runtime.md#rt-rte-carrier-ingest"
            - "runtime.md#rt-rte-readonly-consumption"
          note: "The accepted account leaves detailed body-state, localization and other helper internals and example variants unaudited. Their accumulated-state parts and subsequent consumers are not independently enumerated; the known field routes do not classify those alternatives."
      records:
        - "runtime.md#rt-rte-carrier-ingest"
        - "runtime.md#rt-rte-prediction-feedback"
        - "runtime.md#rt-rte-readonly-consumption"
        - "epistemic.md#epi-rte-slot-solver"
        - "workflow.md#wf-rte-regime-comparison"
        - "memory.md#mem-rte-hierarchy-retention"
        - "memory.md#mem-rte-genome-reconstruction"
        - "memory.md#mem-obj-vocabulary"
        - "memory.md#mem-obj-music-encoder"
        - "epistemic.md#epi-rte-vocabulary-codec"
        - "runtime.md#rt-rte-state-restoration"
        - "memory.md#mem-obj-brain-state"
        - "runtime.md#rt-cmp-three-cell"
      note: "All classified delivery chains are requested computations, not unsolicited model-context injection. Incomplete helper/consumer coverage prevents a whole-boundary pull-only assertion or a system-wide exclusion of push."
    read_back_signal:
      assessment: "uninspected"
      units:
        - scope: "Known requested numerical-field, checkpoint and cache delivery chains"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-carrier-ingest"
            - "runtime.md#rt-rte-prediction-feedback"
            - "runtime.md#rt-rte-readonly-consumption"
            - "epistemic.md#epi-rte-slot-solver"
            - "memory.md#mem-rte-hierarchy-retention"
            - "memory.md#mem-rte-genome-reconstruction"
            - "runtime.md#rt-rte-state-restoration"
            - "memory.md#mem-obj-vocabulary"
            - "memory.md#mem-obj-music-encoder"
            - "epistemic.md#epi-rte-vocabulary-codec"
          note: "The recorded chains fulfill requests and therefore have no push selector to classify. Geometric distance in a pull read and an identifier on a requested checkpoint do not establish a push signal."
        - scope: "Included helper-state and additional example-consumer alternatives within ThreeCell"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-three-cell"
            - "runtime.md#rt-rte-carrier-ingest"
            - "runtime.md#rt-rte-readonly-consumption"
          note: "The accepted account leaves detailed body-state, localization and other helper internals and example variants unaudited. Their accumulated-state parts and subsequent consumers are not independently enumerated; the known field routes do not classify those alternatives."
      records:
        - "runtime.md#rt-rte-carrier-ingest"
        - "runtime.md#rt-rte-prediction-feedback"
        - "runtime.md#rt-rte-readonly-consumption"
        - "epistemic.md#epi-rte-slot-solver"
        - "memory.md#mem-rte-hierarchy-retention"
        - "memory.md#mem-rte-genome-reconstruction"
        - "runtime.md#rt-rte-state-restoration"
        - "memory.md#mem-obj-vocabulary"
        - "memory.md#mem-obj-music-encoder"
        - "epistemic.md#epi-rte-vocabulary-codec"
        - "runtime.md#rt-cmp-three-cell"
      note: "No positive push-signal finding is supported. Pull-chain units are locally inapplicable, but uninspected included consumer alternatives prevent whole-boundary inapplicability."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Perception/closure history to learned carriers and later numerical field consumers"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-buffer"
                - "memory.md#mem-obj-closure-histories"
                - "memory.md#mem-obj-epigenetic"
                - "runtime.md#rt-rte-carrier-ingest"
              note: "Recorded carrier observations and closure experience automatically produce retained Epigenetic state consumed by later primary reads."
            - value: "yes"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-hierarchy-retention"
              note: "Automatic higher-level closure writes create behavior-shaping carriers with explicit later level-read consumers."
          records:
            - "memory.md#mem-obj-buffer"
            - "memory.md#mem-obj-closure-histories"
            - "memory.md#mem-obj-epigenetic"
            - "runtime.md#rt-rte-carrier-ingest"
            - "memory.md#mem-rte-hierarchy-retention"
            - "memory.md#mem-obj-curriculum-trace"
          note: "Automatic trace-fed retained numerical artifacts qualify within the same object; file saving is not required. Higher-level later reading remains an affordance."
        - scope: "Committed prediction/target experience to Response state and later reads"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-pending-prediction"
                - "runtime.md#rt-rte-prediction-feedback"
                - "epistemic.md#epi-rte-response-write"
                - "memory.md#mem-obj-response"
                - "memory.md#mem-obj-genome-statistics"
              note: "Staged context/prediction and evaluation feedback automatically change retained values/statistics/edges used by later reads and generation."
          records:
            - "runtime.md#rt-obj-pending-prediction"
            - "runtime.md#rt-rte-prediction-feedback"
            - "epistemic.md#epi-rte-response-write"
            - "memory.md#mem-obj-response"
            - "memory.md#mem-obj-genome-statistics"
          note: "Trace learning here means wired durable update, not improved capacity or authenticated targets."
        - scope: "Query/correction aggregates to consolidation and later field consumers"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-genome-statistics"
                - "memory.md#mem-rte-memory-consolidation"
              note: "Accumulated query, coalition and feedback traces feed automatic retained merge/prune/promotion changes with later consumers."
          records:
            - "memory.md#mem-obj-genome-statistics"
            - "memory.md#mem-rte-memory-consolidation"
          note: "Reasons are only partially retained and higher-level primary-inference benefit is unestablished, without negating the primary-state chain."
        - scope: "Initial seed, arbitrary replacement, caller-input provenance and cache alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-dna"
            - "runtime.md#rt-rte-direct-maintenance"
            - "runtime.md#rt-rte-state-restoration"
            - "memory.md#mem-rte-genome-reconstruction"
            - "memory.md#mem-obj-vocabulary"
            - "memory.md#mem-obj-music-encoder"
            - "memory.md#mem-obj-curriculum-trace"
          note: "Fixed seeding and unchanged checkpoint copying alone do not qualify. Generic caller inputs and arbitrary mutations lack recorded trace provenance/control; the records provide no bounded trace-learning absence warrant for every alternative."
        - scope: "Included helper-state and additional example-consumer alternatives within ThreeCell"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-three-cell"
            - "runtime.md#rt-rte-carrier-ingest"
            - "runtime.md#rt-rte-readonly-consumption"
          note: "The accepted account leaves detailed body-state, localization and other helper internals and example variants unaudited. Their accumulated-state parts and subsequent consumers are not independently enumerated; the known field routes do not classify those alternatives."
      records:
        - "memory.md#mem-obj-buffer"
        - "memory.md#mem-obj-closure-histories"
        - "memory.md#mem-obj-epigenetic"
        - "runtime.md#rt-rte-carrier-ingest"
        - "memory.md#mem-rte-hierarchy-retention"
        - "memory.md#mem-obj-curriculum-trace"
        - "runtime.md#rt-obj-pending-prediction"
        - "runtime.md#rt-rte-prediction-feedback"
        - "epistemic.md#epi-rte-response-write"
        - "memory.md#mem-obj-response"
        - "memory.md#mem-obj-genome-statistics"
        - "memory.md#mem-rte-memory-consolidation"
        - "memory.md#mem-obj-dna"
        - "runtime.md#rt-rte-direct-maintenance"
        - "runtime.md#rt-rte-state-restoration"
        - "memory.md#mem-rte-genome-reconstruction"
        - "memory.md#mem-obj-vocabulary"
        - "memory.md#mem-obj-music-encoder"
        - "runtime.md#rt-cmp-three-cell"
        - "runtime.md#rt-rte-readonly-consumption"
      note: "Qualifying automatic numerical update chains support yes locally. No local or system-wide no is asserted without bounded absence records; unknown caller/helper alternatives prevent complete coverage."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Ingestion, closure and query-statistic event inputs to automatic field writes"
          assessment: "partial"
          findings:
            - value: "event-streams"
              basis: "wired"
              records:
                - "memory.md#mem-obj-buffer"
                - "memory.md#mem-obj-closure-histories"
                - "memory.md#mem-obj-genome-statistics"
                - "runtime.md#rt-rte-carrier-ingest"
                - "memory.md#mem-rte-memory-consolidation"
              note: "Discrete ticked carrier observations, query/closure activity and their accumulated statistics feed qualifying memory writes."
          records:
            - "memory.md#mem-obj-buffer"
            - "memory.md#mem-obj-closure-histories"
            - "memory.md#mem-obj-genome-statistics"
            - "runtime.md#rt-rte-carrier-ingest"
            - "memory.md#mem-rte-hierarchy-retention"
            - "memory.md#mem-rte-memory-consolidation"
            - "memory.md#mem-obj-curriculum-trace"
          note: "Explicit runtime observations/query/closure events are classified; the original content behind arbitrary caller carriers and curriculum sequences is not determined."
        - scope: "Prediction commitment and target evaluation events"
          assessment: "partial"
          findings:
            - value: "event-streams"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-pending-prediction"
                - "runtime.md#rt-rte-prediction-feedback"
                - "epistemic.md#epi-rte-response-write"
                - "memory.md#mem-obj-genome-statistics"
              note: "Discrete prediction and target-feedback events produce correction/coalition/salience statistics and retained Response changes."
          records:
            - "runtime.md#rt-obj-pending-prediction"
            - "runtime.md#rt-rte-prediction-feedback"
            - "epistemic.md#epi-rte-response-write"
            - "memory.md#mem-obj-genome-statistics"
          note: "The recorded commit/evaluation origin is clear; arbitrary targets and predicted carriers have unresolved upstream content. No session-log or tool-trace origin follows from their serialization."
        - scope: "Opaque upstream input to caller replacement, replay and encoding mechanisms"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-direct-maintenance"
            - "runtime.md#rt-rte-state-restoration"
            - "memory.md#mem-rte-genome-reconstruction"
            - "memory.md#mem-obj-curriculum-trace"
            - "memory.md#mem-obj-vocabulary"
            - "memory.md#mem-obj-music-encoder"
          note: "These records do not identify original activity/experience sources for arbitrary supplied content. Ordered carriers alone do not establish a states/actions/outcomes trajectory, nor do token strings establish session logs."
        - scope: "Included helper-state and additional example-consumer alternatives within ThreeCell"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-three-cell"
            - "runtime.md#rt-rte-carrier-ingest"
            - "runtime.md#rt-rte-readonly-consumption"
          note: "The accepted account leaves detailed body-state, localization and other helper internals and example variants unaudited. Their accumulated-state parts and subsequent consumers are not independently enumerated; the known field routes do not classify those alternatives."
      records:
        - "memory.md#mem-obj-buffer"
        - "memory.md#mem-obj-closure-histories"
        - "memory.md#mem-obj-genome-statistics"
        - "runtime.md#rt-rte-carrier-ingest"
        - "memory.md#mem-rte-hierarchy-retention"
        - "memory.md#mem-rte-memory-consolidation"
        - "memory.md#mem-obj-curriculum-trace"
        - "runtime.md#rt-obj-pending-prediction"
        - "runtime.md#rt-rte-prediction-feedback"
        - "epistemic.md#epi-rte-response-write"
        - "runtime.md#rt-rte-direct-maintenance"
        - "runtime.md#rt-rte-state-restoration"
        - "memory.md#mem-rte-genome-reconstruction"
        - "memory.md#mem-obj-vocabulary"
        - "memory.md#mem-obj-music-encoder"
        - "runtime.md#rt-cmp-three-cell"
        - "runtime.md#rt-rte-readonly-consumption"
      note: "Event-stream origins are supported for named automatic runtime-event routes. Unknown upstream carrier content and untraced helper alternatives prevent an exhaustive trace-source union; session-logs, tool-traces and trajectories are not inferred."
---

# Closure-SDK memory profile

## Comparison rationale

This profile classifies accepted records, not newly inspected source. Every positive finding is implementation wiring or an explicit consumer affordance; none is observed or causally supported. Coverage is separate from that evidence strength. The accepted accounts retain unaudited helper internals and example variants, unresolved input provenance, and missing downstream consumers. These limits remain in the units rather than disappearing behind one known numerical-field witness.

### Operative parts and alternatives

Dense geometry is parametric; fixed-rule layer tags, counts, indices and lookup keys are symbolic. JSON carries both without changing their representational forms. Files are checkpoint substrate, not a repository or model-weight service. Local HashMaps remain in-memory caches. The string display surface does not establish a retained natural-language instruction consumer: see [MEM-OBJ-vocabulary](memory.md#mem-obj-vocabulary), [MEM-OBJ-music-encoder](memory.md#mem-obj-music-encoder) and [EPI-RTE-vocabulary-codec](epistemic.md#epi-rte-vocabulary-codec).

The reconciliation supersedes the epistemic Vocabulary object with [MEM-OBJ-vocabulary](memory.md#mem-obj-vocabulary). All object classifications therefore cite that canonical object; the distinct codec route remains [EPI-RTE-vocabulary-codec](epistemic.md#epi-rte-vocabulary-codec). No other supersession changes a value. BrainState, genome-only reconstruction and vocabulary files stay separate alternatives: [MEM-OBJ-brain-state](memory.md#mem-obj-brain-state), [MEM-RTE-genome-reconstruction](memory.md#mem-rte-genome-reconstruction) and [MEM-OBJ-vocabulary](memory.md#mem-obj-vocabulary). Copying a checkpoint is not another trace-learning transformation.

### Force and admission

Retained carriers provide numerical context/answers, addresses and counts influence priority, and retained tags/statistics determine eligibility or block transformations. The word enforcing in a numerical account does not turn all returned content into enforcement authority. Each finding names its actual consumer/effect. Retained staged experience and access statistics have learning authority at update consumers separately from the resulting field's knowledge/ranking authority: see [RT-BAP-field-consumption](runtime.md#rt-bap-field-consumption), [MEM-OBJ-genome-statistics](memory.md#mem-obj-genome-statistics) and [RT-RTE-prediction-feedback](runtime.md#rt-rte-prediction-feedback).

Software admission is automatic even when the caller starts the curriculum, supplies a target or forces maintenance. Arbitrary mutable access and the caller's checkpoint replacement choice remain unresolved because caller identity does not establish a human content decision: see [RT-RTE-direct-maintenance](runtime.md#rt-rte-direct-maintenance) and [RT-RTE-state-restoration](runtime.md#rt-rte-state-restoration). No manual value is inferred from file I/O.

### Transformation and later consumption

The inspected consolidation pass merges near entries, edits survivors, forgets selected weak entries and promotes eligible values. It supports consolidate, dedup, evolve, decay and promote. It does not establish historical invalidation, synthesis of new claims, semantic acceptance or improved learning. Numerical composition has an unresolved claim interpretation, not automatically a new proposition: see [MEM-RTE-memory-consolidation](memory.md#mem-rte-memory-consolidation), [MEM-RTE-hierarchy-retention](memory.md#mem-rte-hierarchy-retention) and [EPI-RTE-category-disposition](epistemic.md#epi-rte-category-disposition).

Recorded reads fulfill requested computations. Internal numerical selection is not an additional unsolicited push, and a requested checkpoint's path is not an identifier-based push signal. Read-back signal is locally inapplicable on those pull chains; incomplete included consumer coverage prevents whole-boundary inapplicability. Promoted level-1 carriers have explicit read affordances, not established automatic delivery into primary prediction: see [RT-RTE-readonly-consumption](runtime.md#rt-rte-readonly-consumption), [MEM-RTE-hierarchy-retention](memory.md#mem-rte-hierarchy-retention) and [MEM-RTE-genome-reconstruction](memory.md#mem-rte-genome-reconstruction).

Automatic perception/feedback/statistics writes qualify as trace learning because accumulated activity shapes retained numerical artifacts with later consumers. Event-stream findings name runtime observations, query/closure activity and commit/evaluation events, not an adapter label. Arbitrary upstream carriers may encode other content; their original provenance remains unresolved. An ordered replay input does not by itself establish a linked trajectory of states, actions and outcomes. No trace-learning no, session-log or tool-trace value is inferred from missing evidence: see [MEM-OBJ-curriculum-trace](memory.md#mem-obj-curriculum-trace), [MEM-OBJ-closure-histories](memory.md#mem-obj-closure-histories), [MEM-OBJ-genome-statistics](memory.md#mem-obj-genome-statistics) and [EPI-RTE-response-write](epistemic.md#epi-rte-response-write).

### Source-read log

No source reads were made. The supplied accepted members and reconciliation alone support this classification; no new record, quotation or evidence is added.
