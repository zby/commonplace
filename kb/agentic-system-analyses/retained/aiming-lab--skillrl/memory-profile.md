---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "SkillRL memory comparison: changed skill banks, derived experiences and access indexes, SFT artifacts and fitted actor state."
run-id: "AAS-2026-10-14-skillrl-0dba0e1c895e-01"
source-identity: "https://github.com/aiming-lab/SkillRL"
reviewed-boundary: "4d984d455b9b02f0bad283cbe9ab3d66a7e5b89d"
memory-comparison:
  version: 2
  scope: "Included: banks accumulated or changed by offline and online use, derived experience records, their access metadata and dense indexes, retained SFT transformation products, fitted actor parameters/checkpoints and their write, maintenance and later-consumer operations. Initial content provenance and direct API admission alternatives remain unresolved. Excluded: unchanged shipped instructions as read-back, ordinary episode history/current rollout transport as standalone memory, fixed remote producer/encoder parameters and opaque provider internals not shown to accumulate target memory, unrelated runtime storage and external SFT fitting. Raw trajectories remain included as inputs to qualifying updates."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Changed skill bodies, access metadata and derived experience records"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-skill-content"
                - "memory.md#mem-obj-skill-metadata"
                - "memory.md#mem-obj-experience-records"
                - "memory.md#mem-rte-trace-abstraction"
              note: "JSON banks and derived memories persist to disk."
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-skill-content"
                - "memory.md#mem-obj-skill-metadata"
                - "memory.md#mem-obj-experience-records"
                - "memory.md#mem-rte-experience-selection"
              note: "Loaded dictionaries and collections support later selections."
          records:
            - "memory.md#mem-obj-skill-content"
            - "memory.md#mem-obj-skill-metadata"
            - "memory.md#mem-obj-experience-records"
            - "memory.md#mem-rte-trace-abstraction"
            - "memory.md#mem-rte-experience-selection"
          note: "The recorded bank and experience objects identify both persistence and live storage."
        - scope: "Derived skills-only and experience access indexes"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-embedding-model"
                - "memory.md#mem-obj-retrieval-index"
              note: "NumPy vectors and positional maps live in process."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-retrieval-index"
              note: "The experience index caches embedding arrays in a pickle file."
            - value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-retrieval-index"
                - "runtime.md#rt-cmp-embedding-model"
                - "memory.md#mem-rte-experience-selection"
              note: "Dense vectors and FAISS goal indexes support similarity selection."
          records:
            - "memory.md#mem-obj-retrieval-index"
            - "runtime.md#rt-cmp-embedding-model"
            - "memory.md#mem-rte-experience-selection"
          note: "Vector is the operative access substrate, not a classification of JSON instruction encoding."
        - scope: "Updated actor parameters and local recovery checkpoints"
          assessment: "partial"
          findings:
            - value: "model-weights"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-actor-rollout"
                - "runtime.md#rt-rte-policy-update"
              note: "Optimization changes the retained actor parameters."
            - value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-actor-rollout"
                - "runtime.md#rt-rte-policy-update"
              note: "Live tensor state feeds subsequent rollout generation."
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-update"
              note: "Periodic checkpoints support local resume."
          records:
            - "runtime.md#rt-cmp-actor-rollout"
            - "runtime.md#rt-rte-policy-update"
          note: "The inspected FSDP policy path records live state and checkpoint persistence; alternate serialization details are not fully audited."
        - scope: "Retained SFT intermediate traces, reasoning conversations and final pairs"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-sft-production"
                - "memory.md#mem-rte-trace-abstraction"
              note: "Pipeline stages write JSON artifacts subsequently read by aggregation and distillation."
          records:
            - "runtime.md#rt-rte-sft-production"
            - "memory.md#mem-rte-trace-abstraction"
          note: "Recorded artifact persistence is known; external SFT fitting is outside this scope."
      records:
        - "memory.md#mem-obj-skill-content"
        - "memory.md#mem-obj-skill-metadata"
        - "memory.md#mem-obj-experience-records"
        - "memory.md#mem-rte-trace-abstraction"
        - "memory.md#mem-rte-experience-selection"
        - "memory.md#mem-obj-retrieval-index"
        - "runtime.md#rt-cmp-embedding-model"
        - "runtime.md#rt-cmp-actor-rollout"
        - "runtime.md#rt-rte-policy-update"
        - "runtime.md#rt-rte-sft-production"
      note: "Includes bank, derived experiences, access caches, SFT products and changed actor state. Alternate worker/checkpoint implementations remain incompletely assessed; no whole-runtime storage census is asserted."
    representational_form:
      assessment: "known"
      units:
        - scope: "Skill bodies and experience display/aggregation text"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-skill-content"
                - "memory.md#mem-obj-experience-records"
                - "memory.md#mem-rte-experience-selection"
              note: "Models interpret principles, descriptions, patterns and mistake text."
          records:
            - "memory.md#mem-obj-skill-content"
            - "memory.md#mem-obj-experience-records"
            - "memory.md#mem-rte-experience-selection"
          note: "Text consumed as guidance remains distinct from structural access fields."
        - scope: "Bank access fields, structured experience fields and retained SFT record structure"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-skill-metadata"
                - "memory.md#mem-obj-experience-records"
                - "runtime.md#rt-rte-sft-production"
              note: "IDs, category keys, outcome fields and conversation/step structures have fixed code consumers."
          records:
            - "memory.md#mem-obj-skill-metadata"
            - "memory.md#mem-obj-experience-records"
            - "runtime.md#rt-rte-sft-production"
          note: "Only structured parts are classified symbolic, not the natural-language bodies they contain."
        - scope: "Retained SFT reasoning and training conversation bodies"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-sft-production"
              note: "Generated reasoning is inserted into persisted conversations and training pairs."
          records:
            - "runtime.md#rt-rte-sft-production"
          note: "External fitting effects are not inferred from pair production."
        - scope: "Dense access vectors and their position maps"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-retrieval-index"
                - "runtime.md#rt-cmp-embedding-model"
              note: "Dense numerical representations influence similarity selection."
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-retrieval-index"
              note: "Index-to-record positions connect search results to retained records."
          records:
            - "memory.md#mem-obj-retrieval-index"
            - "runtime.md#rt-cmp-embedding-model"
          note: "Encoder parameters are separate fixed components; derived vectors are included memory."
        - scope: "Changed actor parameters"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-actor-rollout"
                - "runtime.md#rt-rte-policy-update"
              note: "Distributed numerical weights shape subsequent generation."
          records:
            - "runtime.md#rt-cmp-actor-rollout"
            - "runtime.md#rt-rte-policy-update"
          note: "Known form on the inspected update path; proposition-level contents cannot be individuated."
      records:
        - "memory.md#mem-obj-skill-content"
        - "memory.md#mem-obj-experience-records"
        - "memory.md#mem-rte-experience-selection"
        - "memory.md#mem-obj-skill-metadata"
        - "runtime.md#rt-rte-sft-production"
        - "memory.md#mem-obj-retrieval-index"
        - "runtime.md#rt-cmp-embedding-model"
        - "runtime.md#rt-cmp-actor-rollout"
        - "runtime.md#rt-rte-policy-update"
      note: "These recorded operative parts cover the included representation inventory; uncertainty about provenance or actual model compliance does not obscure their forms."
    lineage:
      assessment: "partial"
      units:
        - scope: "Online failure-fed skills and SFT trace-derived memories/banks"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-validation-admission"
                - "runtime.md#rt-rte-training-admission"
                - "memory.md#mem-rte-trace-abstraction"
              note: "Failure excerpts or supplied multi-step experience feed generated behavioral guidance."
          records:
            - "runtime.md#rt-rte-validation-admission"
            - "runtime.md#rt-rte-training-admission"
            - "memory.md#mem-rte-trace-abstraction"
          note: "Both admission branches and inspected ALFWorld abstraction stages identify derivation paths, not authenticated original executions."
        - scope: "Imported offline memory inputs and pipeline rollout files"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-offline-production"
                - "runtime.md#rt-rte-sft-production"
                - "memory.md#mem-obj-experience-records"
              note: "Supplied experience files enter the generators and offline pipeline."
          records:
            - "runtime.md#rt-rte-offline-production"
            - "runtime.md#rt-rte-sft-production"
            - "memory.md#mem-obj-experience-records"
          note: "Import is known; original producer and authenticity of every supplied record remain unresolved."
        - scope: "Goal/skill embeddings and access indexes"
          assessment: "partial"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-retrieval-index"
                - "runtime.md#rt-cmp-embedding-model"
              note: "Encoders derive numerical access representations from goal or bank text."
          records:
            - "memory.md#mem-obj-retrieval-index"
            - "runtime.md#rt-cmp-embedding-model"
          note: "Derived vector provenance is known; exact encoder weight provenance and immutable versions are not."
        - scope: "Reward-fitted actor successor parameters"
          assessment: "partial"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-update"
                - "runtime.md#rt-obj-trajectory-batch"
              note: "Collected action/outcome experience feeds optimizer changes."
          records:
            - "runtime.md#rt-rte-policy-update"
            - "runtime.md#rt-obj-trajectory-batch"
            - "runtime.md#rt-cmp-actor-rollout"
          note: "The fitted successor path is trace-fed; initial configured model provenance remains unresolved."
        - scope: "Initial shipped bank and experience contents"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-skill-content"
            - "memory.md#mem-obj-experience-records"
          note: "Shipped instances are available without authenticated producer history; their ultimate authored versus extracted origin cannot be assigned."
        - scope: "SFT reasoning inserted around recorded actions"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-sft-production"
              note: "Recorded successful step sequences feed generated reasoning retained in training conversations."
          records:
            - "runtime.md#rt-rte-sft-production"
          note: "Generation is wired, but generated explanations are not validated accounts of actual reasoning."
      records:
        - "runtime.md#rt-rte-validation-admission"
        - "runtime.md#rt-rte-training-admission"
        - "memory.md#mem-rte-trace-abstraction"
        - "runtime.md#rt-rte-offline-production"
        - "runtime.md#rt-rte-sft-production"
        - "memory.md#mem-obj-experience-records"
        - "memory.md#mem-obj-retrieval-index"
        - "runtime.md#rt-cmp-embedding-model"
        - "runtime.md#rt-rte-policy-update"
        - "runtime.md#rt-obj-trajectory-batch"
        - "runtime.md#rt-cmp-actor-rollout"
        - "memory.md#mem-obj-skill-content"
      note: "Known transformations do not resolve initial bank, experience, encoder or actor provenance. No authored lineage is inferred merely from committed files."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Skill bodies delivered to action policy"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-skill-content"
                - "runtime.md#rt-bap-skill-conditioning"
                - "runtime.md#rt-rte-environment-rollout"
              note: "Rendered rules direct later action choice through model interpretation."
          records:
            - "memory.md#mem-obj-skill-content"
            - "runtime.md#rt-bap-skill-conditioning"
            - "runtime.md#rt-rte-environment-rollout"
          note: "Standing behavioral guidance, not simulator enforcement; applicability may be omitted."
        - scope: "Experience display fields delivered to policy"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-experience-records"
                - "memory.md#mem-rte-experience-selection"
              note: "Selected goals, action examples and mistakes provide contextual advice."
          records:
            - "memory.md#mem-obj-experience-records"
            - "memory.md#mem-rte-experience-selection"
          note: "Only display fields reaching the later policy are classified here."
        - scope: "Bank text and goal vectors at similarity selectors"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-embedding-model"
                - "memory.md#mem-obj-retrieval-index"
                - "memory.md#mem-rte-experience-selection"
                - "memory.md#mem-obj-skill-content"
              note: "Retained text is encoded and scored; goal vectors prioritize selected records."
          records:
            - "runtime.md#rt-cmp-embedding-model"
            - "memory.md#mem-obj-retrieval-index"
            - "memory.md#mem-rte-experience-selection"
            - "memory.md#mem-obj-skill-content"
          note: "A fixed selector can give retained content ranking authority without a learned ranking policy."
        - scope: "Skill access metadata at category/order selection"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-skill-metadata"
                - "runtime.md#rt-rte-environment-rollout"
              note: "Category keys select eligible task-specific input groups."
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-skill-metadata"
                - "runtime.md#rt-rte-environment-rollout"
              note: "Order and dynamic-prefix priority determine selected general rules."
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-skill-metadata"
                - "memory.md#mem-rte-bank-maintenance"
              note: "Existing IDs supply an admission exclusion criterion."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-skill-metadata"
                - "memory.md#mem-rte-bank-maintenance"
              note: "Already-present IDs veto additions on the recorded path."
          records:
            - "memory.md#mem-obj-skill-metadata"
            - "runtime.md#rt-rte-environment-rollout"
            - "memory.md#mem-rte-bank-maintenance"
          note: "Fixed initial ID checks are not within-call semantic deduplication or a universal uniqueness guarantee."
        - scope: "Derived experiences, cleaned traces and bank text at automatic SFT transformations"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-abstraction"
                - "runtime.md#rt-rte-sft-production"
                - "memory.md#mem-obj-experience-records"
              note: "Retained experience feeds durable rules, and bank text feeds reasoning-enriched training artifacts."
          records:
            - "memory.md#mem-rte-trace-abstraction"
            - "runtime.md#rt-rte-sft-production"
            - "memory.md#mem-obj-experience-records"
          note: "Update consumers differ from downstream instruction consumers; external parameter fitting is not classified as wired."
        - scope: "Rollout examples and rewards at actor fitting"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-trajectory-batch"
                - "runtime.md#rt-rte-policy-update"
              note: "Experience and feedback feed parameter updates."
          records:
            - "runtime.md#rt-obj-trajectory-batch"
            - "runtime.md#rt-rte-policy-update"
          note: "The update input has learning authority; benefit is unobserved."
        - scope: "Changed actor weights at rollout inference"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-actor-rollout"
            - "runtime.md#rt-rte-policy-update"
            - "runtime.md#rt-bap-policy-parameters"
          note: "Weights determine generation, but that downstream parametric force is not one of the controlled authority values; learning applies to the experience at its update consumer, not automatically to the output weights."
        - scope: "Existing skill titles at failure proposal model"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-validation-admission"
                - "runtime.md#rt-rte-training-admission"
                - "memory.md#mem-obj-skill-content"
              note: "Titles provide topic-avoidance hints, not full existing principles for criticism."
          records:
            - "runtime.md#rt-rte-validation-admission"
            - "runtime.md#rt-rte-training-admission"
            - "memory.md#mem-obj-skill-content"
          note: "A requested avoidance instruction does not establish actual deduplication."
        - scope: "Caller-directed removal of retained skill IDs"
          assessment: "known"
          findings:
            - value: "enforcement"
              basis: "afforded"
              records:
                - "epistemic.md#epi-rte-skill-withdrawal"
                - "memory.md#mem-rte-bank-maintenance"
              note: "When invoked, membership filtering excludes removed entries from future bank retrieval."
          records:
            - "epistemic.md#epi-rte-skill-withdrawal"
            - "memory.md#mem-rte-bank-maintenance"
          note: "Capability is not wired automatic withdrawal; cached episodes and saved copies may retain the content."
      records:
        - "memory.md#mem-obj-skill-content"
        - "runtime.md#rt-bap-skill-conditioning"
        - "runtime.md#rt-rte-environment-rollout"
        - "memory.md#mem-obj-experience-records"
        - "memory.md#mem-rte-experience-selection"
        - "runtime.md#rt-cmp-embedding-model"
        - "memory.md#mem-obj-retrieval-index"
        - "memory.md#mem-obj-skill-metadata"
        - "memory.md#mem-rte-bank-maintenance"
        - "memory.md#mem-rte-trace-abstraction"
        - "runtime.md#rt-rte-sft-production"
        - "runtime.md#rt-obj-trajectory-batch"
        - "runtime.md#rt-rte-policy-update"
        - "runtime.md#rt-cmp-actor-rollout"
        - "runtime.md#rt-bap-policy-parameters"
        - "runtime.md#rt-rte-validation-admission"
        - "runtime.md#rt-rte-training-admission"
        - "epistemic.md#epi-rte-skill-withdrawal"
      note: "All positive authorities are consumer-specific. Downstream actor-weight force has no supported controlled mapping; incomplete alternative SFT repairs cannot establish further memory authorities."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Validation and training skill admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-validation-admission"
                - "runtime.md#rt-rte-training-admission"
              note: "Software admits model proposals without per-content human approval."
          records:
            - "runtime.md#rt-rte-validation-admission"
            - "runtime.md#rt-rte-training-admission"
          note: "Launching/configuring the run does not make later admission manual."
        - scope: "Original offline generation and inspected SFT writes"
          assessment: "partial"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-offline-production"
                - "runtime.md#rt-rte-sft-production"
                - "memory.md#mem-rte-trace-abstraction"
                - "epistemic.md#epi-rte-trajectory-cleanup"
              note: "Models propose and code constructs, filters and persists outputs."
          records:
            - "runtime.md#rt-rte-offline-production"
            - "runtime.md#rt-rte-sft-production"
            - "memory.md#mem-rte-trace-abstraction"
            - "epistemic.md#epi-rte-trajectory-cleanup"
          note: "Known admission control on inspected routes; environment-specific repair and generation stages remain incompletely inspected."
        - scope: "Actor optimizer and periodic checkpoint production"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-update"
              note: "Software computes updates and saves numerical state."
          records:
            - "runtime.md#rt-rte-policy-update"
          note: "Operator-selected initial model and restart configuration are separate from each optimizer admission."
        - scope: "Derived vector cache production"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-retrieval-index"
                - "runtime.md#rt-cmp-embedding-model"
              note: "Encoder and cache code derive stored access state."
          records:
            - "memory.md#mem-obj-retrieval-index"
            - "runtime.md#rt-cmp-embedding-model"
          note: "No per-vector operator approval is recorded."
        - scope: "Direct bank addition/removal and heuristic experience save callers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-bank-maintenance"
            - "memory.md#mem-rte-experience-save"
          note: "Exposed methods do not identify whether their caller makes a human content decision or computational admission; physical I/O alone cannot resolve agency."
        - scope: "Initial bank, experience and actor-content admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-skill-content"
            - "memory.md#mem-obj-experience-records"
            - "runtime.md#rt-cmp-actor-rollout"
          note: "Configured paths identify reads, not the human/computational decision that supplied or replaced retained content."
      records:
        - "runtime.md#rt-rte-validation-admission"
        - "runtime.md#rt-rte-training-admission"
        - "runtime.md#rt-rte-offline-production"
        - "runtime.md#rt-rte-sft-production"
        - "memory.md#mem-rte-trace-abstraction"
        - "epistemic.md#epi-rte-trajectory-cleanup"
        - "runtime.md#rt-rte-policy-update"
        - "memory.md#mem-obj-retrieval-index"
        - "runtime.md#rt-cmp-embedding-model"
        - "memory.md#mem-rte-bank-maintenance"
        - "memory.md#mem-rte-experience-save"
        - "memory.md#mem-obj-skill-content"
        - "memory.md#mem-obj-experience-records"
        - "runtime.md#rt-cmp-actor-rollout"
      note: "Automatic inspected transformations coexist with unresolved generic caller and initial-content control; no manual finding is invented from file loading."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "ALFWorld SFT trajectory cleanup"
          assessment: "known"
          findings:
            - value: "dedup"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-trajectory-cleanup"
                - "memory.md#mem-rte-trace-abstraction"
              note: "Equal adjacent action windows are removed before downstream memory generation."
          records:
            - "epistemic.md#epi-rte-trajectory-cleanup"
            - "memory.md#mem-rte-trace-abstraction"
          note: "The implemented action-only comparison is known; equal observations and faithful cleanup are not guaranteed."
        - scope: "Inspected SFT experience abstraction and rule aggregation"
          assessment: "partial"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-abstraction"
              note: "Recorded experiences are reduced to patterns/mistakes and aggregated into compact behavioral rules."
          records:
            - "memory.md#mem-rte-trace-abstraction"
          note: "The implemented reduction is supported; generated instances may add claims, so synthesis is not established from a prompt or missing entailment proof."
        - scope: "Failure-fed and original offline rule proposal transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-validation-admission"
            - "runtime.md#rt-rte-training-admission"
            - "runtime.md#rt-rte-offline-production"
          note: "New-rule requests and bounded inputs do not establish whether actual generated content compresses existing claims or synthesizes new ones."
        - scope: "Direct skill withdrawal"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "afforded"
              records:
                - "epistemic.md#epi-rte-skill-withdrawal"
                - "memory.md#mem-rte-bank-maintenance"
              note: "The deletion method forgets matching entries from live general/task lists."
          records:
            - "epistemic.md#epi-rte-skill-withdrawal"
            - "memory.md#mem-rte-bank-maintenance"
          note: "Removal is not invalidate: retained history is not established. No automatic caller or immediate cached-episode revocation is wired."
        - scope: "Heuristic experience saving"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-experience-save"
          note: "The recorded heuristic descriptions may abstract or diagnose; their semantic relation does not establish a controlled curation operation over retained memory."
        - scope: "Uninspected environment-specific SFT repair stages"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-sft-production"
          note: "Earlier WebShop repair phases and other environment generation semantics remain incompletely inspected, preventing an exhaustive curation inventory."
      records:
        - "epistemic.md#epi-rte-trajectory-cleanup"
        - "memory.md#mem-rte-trace-abstraction"
        - "runtime.md#rt-rte-validation-admission"
        - "runtime.md#rt-rte-training-admission"
        - "runtime.md#rt-rte-offline-production"
        - "epistemic.md#epi-rte-skill-withdrawal"
        - "memory.md#mem-rte-bank-maintenance"
        - "memory.md#mem-rte-experience-save"
        - "runtime.md#rt-rte-sft-production"
      note: "Deduplication, inspected consolidation and afforded forgetting remain positive findings; requested novelty, ID collision checks and cache rebuilds establish no additional operation."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Manager retrieval requests and requested structured returns"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-environment-rollout"
                - "memory.md#mem-rte-experience-selection"
              note: "Managers request retained material at reset; retrieval fulfills those requests."
          records:
            - "runtime.md#rt-rte-environment-rollout"
            - "memory.md#mem-rte-experience-selection"
          note: "This internal request operation is distinct from unsolicited delivery to the foreground policy."
        - scope: "Host-selected bank and experience supply to policy"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-environment-rollout"
                - "memory.md#mem-rte-experience-selection"
              note: "Automatic reset selection caches retained parts; later positive-history observations supply them without a policy memory request."
          records:
            - "runtime.md#rt-rte-environment-rollout"
            - "memory.md#mem-rte-experience-selection"
          note: "Delivery is gated and may omit fields or rules; no foreground arbitrary-memory pull tool is established."
        - scope: "SFT aggregation and distillation file consumers"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-abstraction"
                - "runtime.md#rt-rte-sft-production"
              note: "Batch stages load retained intermediate experience and configured bank files."
          records:
            - "memory.md#mem-rte-trace-abstraction"
            - "runtime.md#rt-rte-sft-production"
          note: "Requested file loads are pull, not identifier-targeted push merely because paths are named."
        - scope: "Actor parameters for subsequent generation and local resume"
          assessment: "partial"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-update"
                - "runtime.md#rt-bap-policy-parameters"
              note: "Generation uses synchronized fitted parameters; resume explicitly loads local checkpoint state."
          records:
            - "runtime.md#rt-rte-policy-update"
            - "runtime.md#rt-bap-policy-parameters"
          note: "Inspected numerical read routes are established; alternate workers and exact synchronization remain incompletely audited."
        - scope: "Heuristic save future reload capability"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-experience-save"
              note: "A subsequently constructed retrieval instance can load the written experience file."
          records:
            - "memory.md#mem-rte-experience-save"
          note: "No live saver-to-selector loop or same-instance index update is established."
      records:
        - "runtime.md#rt-rte-environment-rollout"
        - "memory.md#mem-rte-experience-selection"
        - "memory.md#mem-rte-trace-abstraction"
        - "runtime.md#rt-rte-sft-production"
        - "runtime.md#rt-rte-policy-update"
        - "runtime.md#rt-bap-policy-parameters"
        - "memory.md#mem-rte-experience-save"
      note: "Both requested reads and automatic context supply exist at distinct operations. Alternate worker and environment-specific consumption details prevent a complete route census."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Skills-only template-mode push at manager reset"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-environment-rollout"
                - "memory.md#mem-obj-skill-metadata"
              note: "General rules are selected by availability, stored order, dynamic-prefix priority and counts."
            - value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-environment-rollout"
                - "memory.md#mem-obj-skill-metadata"
              note: "Task text keyword/category detection selects category instruction groups."
          records:
            - "runtime.md#rt-rte-environment-rollout"
            - "memory.md#mem-obj-skill-metadata"
            - "memory.md#mem-clm-search-category"
          note: "Trigger is reset; task text and bank categories select cached bodies for later observations. Search query-type categories are not delivered by the online shared schema."
        - scope: "Skills-only embedding-mode push"
          assessment: "known"
          findings:
            - value: "inferred-embedding"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-environment-rollout"
                - "runtime.md#rt-cmp-embedding-model"
              note: "Task embeddings rank retained general and task-skill representations for later prompt delivery."
          records:
            - "runtime.md#rt-rte-environment-rollout"
            - "runtime.md#rt-cmp-embedding-model"
          note: "Dynamic instructions can be omitted; ranking is not evidence of lesson relevance or compliance."
        - scope: "Alternate experience/skill push"
          assessment: "known"
          findings:
            - value: "inferred-embedding"
              basis: "wired"
              records:
                - "memory.md#mem-rte-experience-selection"
                - "memory.md#mem-obj-retrieval-index"
              note: "Task-goal similarity selects successful/failure examples."
            - value: "inferred-lexical"
              basis: "wired"
              records:
                - "memory.md#mem-rte-experience-selection"
              note: "Detected task category selects category rules in the skill-bearing branch."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-experience-selection"
              note: "First-rule slices, mistake counts, thresholds and approximate budgets limit supplied material."
          records:
            - "memory.md#mem-rte-experience-selection"
            - "memory.md#mem-obj-retrieval-index"
          note: "Reset triggers selection; task description and retained goal vectors/category lists select displayed rules, examples and mistakes."
        - scope: "Other environment-specific context delivery and filtering"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-environment-rollout"
            - "memory.md#mem-rte-experience-selection"
          note: "The accepted rollout and alternate-selector records leave other manager context handling and full WebShop length filtering incompletely inspected; the signals governing any additional selected retained parts cannot be exhaustively classified."
        - scope: "Requested SFT file and actor/checkpoint read operations"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-sft-production"
            - "memory.md#mem-rte-trace-abstraction"
            - "runtime.md#rt-rte-policy-update"
          note: "These are requested reads, not push selectors, so no push signal applies to these particular operations."
      records:
        - "runtime.md#rt-rte-environment-rollout"
        - "memory.md#mem-obj-skill-metadata"
        - "memory.md#mem-clm-search-category"
        - "runtime.md#rt-cmp-embedding-model"
        - "memory.md#mem-rte-experience-selection"
        - "memory.md#mem-obj-retrieval-index"
        - "runtime.md#rt-rte-sft-production"
        - "memory.md#mem-rte-trace-abstraction"
        - "runtime.md#rt-rte-policy-update"
      note: "Known push selectors retain lexical, embedding and coarse signals. Other environment context handling is incompletely recorded; no identity-match finding follows merely from dyn_ prefixes or file paths."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Validation and training failure-to-skill writes"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-validation-admission"
                - "runtime.md#rt-rte-training-admission"
                - "memory.md#mem-obj-skill-content"
                - "runtime.md#rt-rte-environment-rollout"
              note: "Automatic failure-fed admission creates saved guidance eligible for later training prompts."
          records:
            - "runtime.md#rt-rte-validation-admission"
            - "runtime.md#rt-rte-training-admission"
            - "memory.md#mem-obj-skill-content"
            - "runtime.md#rt-rte-environment-rollout"
          note: "Qualifies without observed benefit or a complete reconstructed episode transcript."
        - scope: "Offline experience-to-bank and inspected SFT abstraction/distillation"
          assessment: "partial"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-offline-production"
                - "memory.md#mem-rte-trace-abstraction"
                - "runtime.md#rt-rte-sft-production"
              note: "Supplied experience feeds automatically retained behavioral rules and reasoning artifacts with later pipeline consumers."
          records:
            - "runtime.md#rt-rte-offline-production"
            - "memory.md#mem-rte-trace-abstraction"
            - "runtime.md#rt-rte-sft-production"
          note: "External final fitting is not wired here; bank and intermediate consumers are recorded. Other environment transformation semantics remain incompletely inspected."
        - scope: "Reward-driven actor parameter writes"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-trajectory-batch"
                - "runtime.md#rt-rte-policy-update"
                - "runtime.md#rt-bap-policy-parameters"
              note: "Collected experience updates durable parameters used by subsequent generation."
          records:
            - "runtime.md#rt-obj-trajectory-batch"
            - "runtime.md#rt-rte-policy-update"
            - "runtime.md#rt-bap-policy-parameters"
          note: "Capacity wiring does not establish actual gains or exact deployed initial weights."
        - scope: "Heuristic experience save API"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-experience-save"
            - "memory.md#mem-rte-experience-selection"
          note: "Generic caller control and the missing saver/index-refresh connection prevent an automatic trace-fed write-to-later-consumer classification for this capability."
        - scope: "Initial content and direct mutation alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-skill-content"
            - "memory.md#mem-obj-experience-records"
            - "runtime.md#rt-cmp-actor-rollout"
            - "memory.md#mem-rte-bank-maintenance"
          note: "No recorded provenance/control establishes whether these alternative admissions are automatic trace-fed learning or nonqualifying supplied content."
      records:
        - "runtime.md#rt-rte-validation-admission"
        - "runtime.md#rt-rte-training-admission"
        - "memory.md#mem-obj-skill-content"
        - "runtime.md#rt-rte-environment-rollout"
        - "runtime.md#rt-rte-offline-production"
        - "memory.md#mem-rte-trace-abstraction"
        - "runtime.md#rt-rte-sft-production"
        - "runtime.md#rt-obj-trajectory-batch"
        - "runtime.md#rt-rte-policy-update"
        - "runtime.md#rt-bap-policy-parameters"
        - "memory.md#mem-rte-experience-save"
        - "memory.md#mem-rte-experience-selection"
        - "memory.md#mem-obj-experience-records"
        - "runtime.md#rt-cmp-actor-rollout"
        - "memory.md#mem-rte-bank-maintenance"
      note: "Positive trace-fed routes do not justify system-wide no, nor resolve unknown initial and caller-driven admissions. Ordinary episode suffix buffers are excluded, not classified as negative trace learning."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Online failure-fed skill admissions"
          assessment: "known"
          findings:
            - value: "trajectories"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-validation-admission"
                - "runtime.md#rt-rte-training-admission"
                - "runtime.md#rt-obj-trajectory-batch"
              note: "Reconstructed linked observation/action/outcome excerpts are selected from training or validation experience."
          records:
            - "runtime.md#rt-rte-validation-admission"
            - "runtime.md#rt-rte-training-admission"
            - "runtime.md#rt-obj-trajectory-batch"
          note: "These are bounded, potentially incomplete trajectory projections, not authenticated full transcripts or conversational session logs."
        - scope: "Reward-driven policy fitting"
          assessment: "known"
          findings:
            - value: "trajectories"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-trajectory-batch"
                - "runtime.md#rt-rte-policy-update"
              note: "Collected linked multi-step environment actions and outcome feedback supply the update."
          records:
            - "runtime.md#rt-obj-trajectory-batch"
            - "runtime.md#rt-rte-policy-update"
          note: "A step-row training representation does not change the original multi-step experience source."
        - scope: "Original offline banks and SFT trajectory-derived memory/reasoning"
          assessment: "partial"
          findings:
            - value: "trajectories"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-offline-production"
                - "memory.md#mem-rte-trace-abstraction"
                - "runtime.md#rt-rte-sft-production"
                - "memory.md#mem-obj-experience-records"
              note: "Supplied recorded environment step sequences and their derived patterns feed automatic behavioral-artifact writes."
          records:
            - "runtime.md#rt-rte-offline-production"
            - "memory.md#mem-rte-trace-abstraction"
            - "runtime.md#rt-rte-sft-production"
            - "memory.md#mem-obj-experience-records"
          note: "Content supports trajectory origin; exact external producers and all environment-specific inputs are not authenticated or inspected."
        - scope: "Initial and generic caller-controlled admission alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-skill-content"
            - "memory.md#mem-obj-experience-records"
            - "runtime.md#rt-cmp-actor-rollout"
            - "memory.md#mem-rte-bank-maintenance"
            - "memory.md#mem-rte-experience-save"
          note: "Whether a qualifying automatic trace-fed write exists is unresolved; its original inputs therefore cannot be exhaustively classified."
      records:
        - "runtime.md#rt-rte-validation-admission"
        - "runtime.md#rt-rte-training-admission"
        - "runtime.md#rt-obj-trajectory-batch"
        - "runtime.md#rt-rte-policy-update"
        - "runtime.md#rt-rte-offline-production"
        - "memory.md#mem-rte-trace-abstraction"
        - "runtime.md#rt-rte-sft-production"
        - "memory.md#mem-obj-experience-records"
        - "memory.md#mem-obj-skill-content"
        - "runtime.md#rt-cmp-actor-rollout"
        - "memory.md#mem-rte-bank-maintenance"
        - "memory.md#mem-rte-experience-save"
      note: "Trajectory content is supported on known routes; no session-log, tool-trace or event-stream label is added merely from conversation formatting, tool use during episodes or serialization."
---

# SkillRL memory profile

## Comparison rationale

The profile separates retained instruction bodies, symbolic targeting fields,
dense access representations and fitted actor state. The same JSON file can
support different forms and authorities at different consumers. Its storage is
not a repository substrate merely because the initial artifact is shipped in
Git. The included inventory follows [MEM-OBJ-skill-content](memory.md#mem-obj-skill-content),
[MEM-OBJ-skill-metadata](memory.md#mem-obj-skill-metadata),
[MEM-OBJ-experience-records](memory.md#mem-obj-experience-records),
[MEM-OBJ-retrieval-index](memory.md#mem-obj-retrieval-index),
[RT-RTE-sft-production](runtime.md#rt-rte-sft-production) and
[RT-RTE-policy-update](runtime.md#rt-rte-policy-update).

Reconciliation supersedes EPI-OBJ-skill-principles with
[MEM-OBJ-skill-content](memory.md#mem-obj-skill-content). All profile findings
use that canonical object. Containers and their inspected parts remain distinct:
[MEM-RTE-trace-abstraction](memory.md#mem-rte-trace-abstraction) and
[EPI-RTE-trajectory-cleanup](epistemic.md#epi-rte-trajectory-cleanup) do not
replace the complete SFT route. Likewise the afforded withdrawal method is not
a wired maintenance workflow. Its forgetting effect supports local decay, not
history-preserving invalidation.

Requested manager retrieval is pull at the requesting operation; automatic
observation supply is push at the later policy consumer. File loading by SFT
stages remains pull. This union does not invent a foreground policy memory
tool. The push signals distinguish lexical category selection, coarse slices
and embedding ranking; a dynamic prefix is not an exact identity match. See
[RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout) and
[MEM-RTE-experience-selection](memory.md#mem-rte-experience-selection).

Automatic trace-fed writes qualify without evidence of improved capacity.
Failure fragments can produce durable instructions and reward-bearing
experience can change actor parameters. The learning authority of retained
experience at an update consumer is separate from the output's later force.
The controlled authority vocabulary does not describe the actor weights'
downstream generative force, so that unit remains not-determinable rather than
being labeled instruction or learning by analogy. See
[RT-BAP-policy-parameters](runtime.md#rt-bap-policy-parameters).

Known forms and local mechanisms do not authenticate shipped instances or
resolve generic API caller decisions. Missing source-control facts prevent
manual admission and complete lineage findings. Missing generated instances
prevent synthesis from being inferred from requests for new rules. The
implemented reduction in the inspected SFT abstraction supports consolidation,
without asserting that every generated proposition is semantically preserved.
[MEM-RTE-experience-save](memory.md#mem-rte-experience-save) cannot be connected
to a wired live learning loop without the missing caller and index refresh.
Environment-specific repair semantics and alternate numerical workers remain
locally unresolved. These uncertainties remain in units rather than being
removed from the inventory.

All positive bases are source-level wiring or exposed affordance. No finding
claims observed operation or causal benefit. No source files were read for this
classification; it uses only the supplied accepted members and reconciliation.
