---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "ContextPilot memory comparison: per-trajectory stores and edited views, access metadata, and reward-fed actor state at the frozen revision."
run-id: "AAS-2026-10-19-contextpilot-0826e2df5b2f-01"
source-identity: "https://github.com/Tencent/ContextPilot"
reviewed-boundary: "782cbb6611fb610c4cf6fafda6022b7e89cae191"
memory-comparison:
  version: 2
  scope: "Included: inference and training keyed memories/notes, signatures/edges/optional vectors, retained history-derived replacement views and visibility controls, branch copies, training snapshots/credit and updated actor parameters/checkpoints; persisted inference traces remain included with unresolved later semantic reuse. Initial library content and actor/provider provenance remain explicit uncertainties. Excluded: acquisition-only document indexes, plain accumulation of untransformed turns as a standalone learning mechanism, shipped static prompts/tool schemas, unchanged judge/compressor/embedding-provider parameters, external service internals and benchmark payloads. Actor export/production adoption is an unresolved downstream alternative, not an established consumer."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        -
          scope: "Inference rich/simple stores and training rich/simple stores, including branch copies"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-simple-notes"
                - "memory.md#mem-obj-memories"
                - "memory.md#mem-obj-training-notes"
              note: "Python dictionaries retain entries for later policy invocations within a sample or trajectory."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-simple-notes"
            - "memory.md#mem-obj-memories"
            - "memory.md#mem-obj-training-notes"
            - "memory.md#mem-rte-inference-stores"
            - "memory.md#mem-rte-training-stores"
          note: "The four recorded stores are process-local dictionaries; cloning copies them rather than creating a persistent shared database."
        -
          scope: "Memory signatures, relation edges and optional dense embedding caches"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-indexes"
              note: "Edges and vectors are held in process; neither graph structure nor dense encoding proves a graph or vector database."
          records:
            - "memory.md#mem-obj-memory-indexes"
          note: "All three access structures are explicitly in-process caches, including the numerical vectors."
        -
          scope: "Retained replacement views and masks"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-context-masks"
                - "runtime.md#rt-rte-context-edit"
                - "memory.md#mem-rte-training-context"
              note: "Process-local sets/maps and strings hold the operative edited view."
          records:
            - "runtime.md#rt-obj-context-masks"
            - "runtime.md#rt-rte-context-edit"
            - "memory.md#mem-rte-training-context"
          note: "Masks and replacement text remain in agent state and enter subsequent payload builds."
        -
          scope: "Training token/mask snapshots and reward-bearing trajectory rows"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory-snapshots"
                - "runtime.md#rt-rte-training-rollout"
                - "runtime.md#rt-rte-actor-update"
              note: "Snapshot arrays and metadata are retained and passed to worker and actor-update consumers."
          records:
            - "memory.md#mem-obj-trajectory-snapshots"
            - "runtime.md#rt-rte-training-rollout"
            - "runtime.md#rt-rte-actor-update"
          note: "Worker-returned Python structures supply training consumers; optional logging is not presumed to be a reloaded textual memory store."
        -
          scope: "Actor state changed by training and checkpoint resume"
          assessment: "known"
          findings:
            -
              value: "model-weights"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-actor-model"
                - "runtime.md#rt-rte-actor-update"
                - "runtime.md#rt-bap-reward-actor"
              note: "The learned retained artifact is numerical actor parameter state."
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-actor-model"
                - "runtime.md#rt-rte-actor-update"
                - "runtime.md#rt-bap-reward-actor"
              note: "Checkpoint files retain model-related state for trainer reload."
          records:
            - "runtime.md#rt-cmp-actor-model"
            - "runtime.md#rt-rte-actor-update"
            - "runtime.md#rt-bap-reward-actor"
          note: "Inspected update calls and checkpoint save/load establish mutable parameter state and saved files, not exact weights or deployment."
        -
          scope: "Serialized inference history, view maps and payload snapshots"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-full-history"
                - "runtime.md#rt-obj-context-masks"
              note: "Trajectory JSON retains history and edit state; this is not a verified complete keyed-store backup."
          records:
            - "runtime.md#rt-obj-full-history"
            - "runtime.md#rt-obj-context-masks"
          note: "Logging persists trace/view copies. The reports establish no semantic reload across QA samples."
      records:
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-simple-notes"
        - "memory.md#mem-obj-memories"
        - "memory.md#mem-obj-training-notes"
        - "memory.md#mem-rte-inference-stores"
        - "memory.md#mem-rte-training-stores"
        - "memory.md#mem-obj-memory-indexes"
        - "runtime.md#rt-obj-context-masks"
        - "runtime.md#rt-rte-context-edit"
        - "memory.md#mem-rte-training-context"
        - "memory.md#mem-obj-trajectory-snapshots"
        - "runtime.md#rt-rte-training-rollout"
        - "runtime.md#rt-rte-actor-update"
        - "runtime.md#rt-cmp-actor-model"
        - "runtime.md#rt-bap-reward-actor"
        - "runtime.md#rt-obj-full-history"
      note: "Recorded operative stores, access metadata, edited views, training arrays, actor state and trace files have classified substrates. Static provider weights and acquisition-only document indexes are outside this memory inventory; exact provider deployment is not inferred."
    representational_form:
      assessment: "known"
      units:
        -
          scope: "Saved summaries, full bodies, entities and episodes interpreted by policy models"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-simple-notes"
                - "memory.md#mem-obj-memories"
                - "memory.md#mem-obj-training-notes"
                - "memory.md#mem-rte-inference-stores"
                - "memory.md#mem-rte-training-stores"
              note: "Inventories and read results supply text interpreted as context by the policy."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-simple-notes"
            - "memory.md#mem-obj-memories"
            - "memory.md#mem-obj-training-notes"
            - "memory.md#mem-rte-inference-stores"
            - "memory.md#mem-rte-training-stores"
          note: "Readable entry content is separate from its keys and normalization envelopes."
        -
          scope: "Store keys, source lists, timestamps, relation envelopes and access signatures/edges"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-simple-notes"
                - "memory.md#mem-obj-memories"
                - "memory.md#mem-obj-training-notes"
                - "memory.md#mem-obj-memory-indexes"
              note: "Keys select values; symbolic features and edge scores control access and ranking."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-simple-notes"
            - "memory.md#mem-obj-memories"
            - "memory.md#mem-obj-training-notes"
            - "memory.md#mem-obj-memory-indexes"
          note: "Fixed Python access, normalization and scoring rules consume these localized fields; source lists are not verified provenance."
        -
          scope: "Optional retained dense memory embeddings"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-indexes"
              note: "Normalized dense numerical representations participate in the optional similarity channel."
          records:
            - "memory.md#mem-obj-memory-indexes"
          note: "The dense vectors are selector inputs, not readable neighbor displays or a verified model of source truth."
        -
          scope: "Context replacement bodies supplied to later model calls"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-context-masks"
                - "runtime.md#rt-rte-context-edit"
                - "memory.md#mem-rte-training-context"
              note: "Later payloads substitute retained text for original messages."
          records:
            - "runtime.md#rt-obj-context-masks"
            - "runtime.md#rt-rte-context-edit"
            - "memory.md#mem-rte-training-context"
          note: "Summary, substring and compression strings are interpreted as language even when mechanically produced."
        -
          scope: "View-control masks and message identifiers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-context-masks"
                - "runtime.md#rt-rte-context-edit"
                - "memory.md#mem-rte-training-context"
              note: "Set membership, identity and precedence select the model-visible view."
          records:
            - "runtime.md#rt-obj-context-masks"
            - "runtime.md#rt-rte-context-edit"
            - "memory.md#mem-rte-training-context"
          note: "These parts determine substitution and visibility through fixed rules rather than language interpretation."
        -
          scope: "Training trajectory token IDs, masks, log-probabilities, node IDs and credit values"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory-snapshots"
                - "runtime.md#rt-rte-training-rollout"
                - "runtime.md#rt-rte-actor-update"
              note: "Token IDs, response masks, numerical credit and ancestry fields govern row selection and optimization."
          records:
            - "memory.md#mem-obj-trajectory-snapshots"
            - "runtime.md#rt-rte-training-rollout"
            - "runtime.md#rt-rte-actor-update"
          note: "Localized arrays and scalars have fixed consumer rules; decoded prompt/action text is a separate language consumption path."
        -
          scope: "Decoded training prompt/action content and retained inference trace text"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory-snapshots"
                - "runtime.md#rt-obj-full-history"
              note: "Prompts, tool observations and actions carry language content."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory-snapshots"
                - "runtime.md#rt-obj-full-history"
              note: "Message envelopes and serialized token/metadata fields preserve fixed-rule structure."
          records:
            - "memory.md#mem-obj-trajectory-snapshots"
            - "runtime.md#rt-obj-full-history"
          note: "Text remains language at policy/decoded-content consumption; surrounding role and ID fields have symbolic consumers."
        -
          scope: "Updated actor parameters restored from checkpoints"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-actor-model"
                - "runtime.md#rt-rte-actor-update"
                - "runtime.md#rt-bap-reward-actor"
              note: "Training updates distributed numerical policy parameters, not a textual instruction registry."
          records:
            - "runtime.md#rt-cmp-actor-model"
            - "runtime.md#rt-rte-actor-update"
            - "runtime.md#rt-bap-reward-actor"
          note: "Particular propositions inside the weights and exact versions are not determinable, but their representational form is recorded."
      records:
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-simple-notes"
        - "memory.md#mem-obj-memories"
        - "memory.md#mem-obj-training-notes"
        - "memory.md#mem-rte-inference-stores"
        - "memory.md#mem-rte-training-stores"
        - "memory.md#mem-obj-memory-indexes"
        - "runtime.md#rt-obj-context-masks"
        - "runtime.md#rt-rte-context-edit"
        - "memory.md#mem-rte-training-context"
        - "memory.md#mem-obj-trajectory-snapshots"
        - "runtime.md#rt-rte-training-rollout"
        - "runtime.md#rt-rte-actor-update"
        - "runtime.md#rt-obj-full-history"
        - "runtime.md#rt-cmp-actor-model"
        - "runtime.md#rt-bap-reward-actor"
      note: "Language, localized symbolic structures and dense distributed representations are split by operative part and consumer. Provider opacity limits provenance and operation, not the recorded form of these parts."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Keyed memory/note text at model-argument admission"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-simple-notes"
                - "memory.md#mem-obj-memories"
                - "memory.md#mem-obj-training-notes"
                - "memory.md#mem-rte-inference-stores"
                - "memory.md#mem-rte-training-stores"
              note: "The policy supplies summary/content and structured fields in write arguments."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-simple-notes"
            - "memory.md#mem-obj-memories"
            - "memory.md#mem-obj-training-notes"
            - "memory.md#mem-rte-inference-stores"
            - "memory.md#mem-rte-training-stores"
          note: "Model authorship is established; normal proximity to document reads does not prove each entry was extracted from those documents."
        -
          scope: "Explicit summary, span and compression replacements derived from retained messages"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-context-masks"
                - "runtime.md#rt-rte-context-edit"
                - "memory.md#mem-rte-training-context"
              note: "Selected assistant/tool history supplies retained summary or reduced replacement content."
          records:
            - "runtime.md#rt-obj-context-masks"
            - "runtime.md#rt-rte-context-edit"
            - "memory.md#mem-rte-training-context"
          note: "Recorded handlers transform selected trace text into later-consumed views; fidelity is not assured."
        -
          scope: "Memory signatures, edges and vectors derived from current entries"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-indexes"
              note: "Fixed feature extraction, edge scoring and optional embedding requests compile access metadata from entries."
          records:
            - "memory.md#mem-obj-memory-indexes"
          note: "The derivation from entry features/signature text is recorded independently of the embedding provider's training provenance."
        -
          scope: "Trajectory snapshots, branch copies and actor updates from rollout experience"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory-snapshots"
                - "runtime.md#rt-rte-training-rollout"
                - "runtime.md#rt-rte-actor-update"
                - "memory.md#mem-rte-training-context"
              note: "Rollout histories/actions are captured as snapshots and feed reward-responsive parameter updates."
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-actor-update"
              note: "Descendant reward averaging, query normalization and optimization compile experience into actor state."
          records:
            - "memory.md#mem-obj-trajectory-snapshots"
            - "runtime.md#rt-rte-training-rollout"
            - "runtime.md#rt-rte-actor-update"
            - "memory.md#mem-rte-training-context"
          note: "Snapshot and branch lineage includes sampled actions and code-authored forced actions; conditioning-only cleanup is not a trainable action."
        -
          scope: "Document-derived evidence retained inside history"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-document-evidence"
                - "runtime.md#rt-obj-full-history"
              note: "Selected external document text enters the trace; its retention does not authenticate it."
          records:
            - "epistemic.md#epi-obj-document-evidence"
            - "runtime.md#rt-obj-full-history"
          note: "Imported document passages are distinct from generated summaries and carry unresolved source warrant."
        -
          scope: "Initial actor checkpoint provenance, embedding-provider provenance and arbitrary caller-supplied initial store content"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-actor-model"
            - "runtime.md#rt-cmp-embedding-provider"
            - "memory.md#mem-obj-memory-indexes"
            - "memory.md#mem-rte-training-stores"
          note: "Paths/endpoints do not identify training provenance, and generic library initialization does not identify content origin. The known subsequent derivations do not resolve these origins."
      records:
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-simple-notes"
        - "memory.md#mem-obj-memories"
        - "memory.md#mem-obj-training-notes"
        - "memory.md#mem-rte-inference-stores"
        - "memory.md#mem-rte-training-stores"
        - "runtime.md#rt-obj-context-masks"
        - "runtime.md#rt-rte-context-edit"
        - "memory.md#mem-rte-training-context"
        - "memory.md#mem-obj-memory-indexes"
        - "memory.md#mem-obj-trajectory-snapshots"
        - "runtime.md#rt-rte-training-rollout"
        - "runtime.md#rt-rte-actor-update"
        - "epistemic.md#epi-obj-document-evidence"
        - "runtime.md#rt-obj-full-history"
        - "runtime.md#rt-cmp-actor-model"
        - "runtime.md#rt-cmp-embedding-provider"
      note: "Known authored, imported and derived paths coexist with unresolved initialization and provider provenance; the accepted records cannot establish a complete lineage inventory."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Saved entry bodies, inventories and retained replacement language at later policy invocations"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-inference-stores"
                - "memory.md#mem-rte-training-stores"
                - "runtime.md#rt-obj-context-masks"
                - "runtime.md#rt-rte-context-edit"
                - "memory.md#mem-rte-training-context"
                - "runtime.md#rt-bap-context-policy"
              note: "The policy receives retained summaries, selected full entries and edited evidence views as context."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-simple-notes"
            - "memory.md#mem-obj-memories"
            - "memory.md#mem-obj-training-notes"
            - "memory.md#mem-rte-inference-stores"
            - "memory.md#mem-rte-training-stores"
            - "runtime.md#rt-obj-context-masks"
            - "runtime.md#rt-rte-context-edit"
            - "memory.md#mem-rte-training-context"
            - "runtime.md#rt-bap-context-policy"
          note: "The consumed text supplies evidence/context/advice, not special instruction priority or executable authorization."
        -
          scope: "Retained entry text/features, relation scores and optional embeddings at neighbor selection"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-indexes"
                - "memory.md#mem-rte-inference-stores"
                - "memory.md#mem-rte-training-stores"
              note: "Entry features and optional vector similarities determine relative neighbor scores."
          records:
            - "memory.md#mem-obj-memory-indexes"
            - "memory.md#mem-rte-inference-stores"
            - "memory.md#mem-rte-training-stores"
          note: "Fixed scoring consumes retained features and positive edges to prioritize bounded neighbor displays, not to certify their truth."
        -
          scope: "Context mask membership and substitution maps at the payload renderer"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-context-masks"
                - "runtime.md#rt-rte-context-edit"
                - "memory.md#mem-rte-training-context"
              note: "Retained masks suppress original content or replace it before the policy receives a payload."
          records:
            - "runtime.md#rt-obj-context-masks"
            - "runtime.md#rt-rte-context-edit"
            - "memory.md#mem-rte-training-context"
          note: "The renderer enforces which backing-history content is visible; this is independent of whether a model follows any textual advice."
        -
          scope: "Snapshot ancestry IDs, branchability flags, response masks and descendant credit at worker/trainer consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory-snapshots"
                - "runtime.md#rt-rte-training-rollout"
                - "runtime.md#rt-rte-actor-update"
              note: "Node/prefix ancestry selects descendant outcomes and branchability controls continuation paths."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory-snapshots"
                - "runtime.md#rt-rte-training-rollout"
                - "runtime.md#rt-rte-actor-update"
              note: "Missing-terminal snapshot rejection and response masks exclude rows or tokens from training."
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory-snapshots"
                - "runtime.md#rt-rte-training-rollout"
                - "runtime.md#rt-rte-actor-update"
                - "runtime.md#rt-bap-reward-actor"
              note: "Scored and masked experience feeds durable actor parameter updates."
          records:
            - "memory.md#mem-obj-trajectory-snapshots"
            - "runtime.md#rt-rte-training-rollout"
            - "runtime.md#rt-rte-actor-update"
            - "memory.md#mem-rte-training-context"
          note: "Each finding names a separate consumer/effect of the retained training structures."
        -
          scope: "Updated actor parameters at checkpoint load and resumed training"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-actor-model"
            - "runtime.md#rt-rte-actor-update"
            - "runtime.md#rt-bap-reward-actor"
          note: "Checkpoint loading restores the output of learning, but these records do not establish a controlled authority value at that consumer. In particular, restoration does not establish consumption of the parameters as retained examples, experience or feedback feeding another update. Production inference adoption and exercised behavioral dependence remain untraced."
        -
          scope: "Exact downstream effects of provider-resolved actor state outside the traced training/resume path"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-actor-model"
            - "runtime.md#rt-rte-actor-update"
          note: "Unpinned endpoints and untraced rollout synchronization/export prevent classifying an additional production-consumer authority path."
      records:
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-simple-notes"
        - "memory.md#mem-obj-memories"
        - "memory.md#mem-obj-training-notes"
        - "memory.md#mem-rte-inference-stores"
        - "memory.md#mem-rte-training-stores"
        - "runtime.md#rt-obj-context-masks"
        - "runtime.md#rt-rte-context-edit"
        - "memory.md#mem-rte-training-context"
        - "runtime.md#rt-bap-context-policy"
        - "memory.md#mem-obj-memory-indexes"
        - "memory.md#mem-obj-trajectory-snapshots"
        - "runtime.md#rt-rte-training-rollout"
        - "runtime.md#rt-rte-actor-update"
        - "runtime.md#rt-cmp-actor-model"
        - "runtime.md#rt-bap-reward-actor"
      note: "Context, ranking, view enforcement and training-credit effects are supported at named consumers. The downstream authority of restored actor parameters is not determinable from restoration alone, and production-consumer effects remain uninspected. Supplied references and fixed format rules are outside accumulated memory and establish no validation finding here."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Shipped inference and training keyed-store admission and revision"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-inference-stores"
                - "memory.md#mem-rte-training-stores"
              note: "Model/software add, append, overwrite and delete without a per-content human approval decision."
          records:
            - "memory.md#mem-rte-inference-stores"
            - "memory.md#mem-rte-training-stores"
          note: "Humans select workflow configuration, not each retained entry; policy arguments and Python checks admit the content."
        -
          scope: "Access-metadata reconstruction, view edits, compression fallback and proactive cleanup"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-indexes"
                - "runtime.md#rt-obj-context-masks"
                - "runtime.md#rt-rte-context-edit"
                - "memory.md#mem-rte-training-context"
              note: "Software rebuilds indexes, stores masks/replacements and admits compressor fallback or cleanup actions."
          records:
            - "memory.md#mem-obj-memory-indexes"
            - "runtime.md#rt-obj-context-masks"
            - "runtime.md#rt-rte-context-edit"
            - "memory.md#mem-rte-training-context"
          note: "Model-directed edits and independent code rules are both software admission, including synthetic recovery."
        -
          scope: "Snapshot capture, branch inheritance, reward-credit rows, actor updates and checkpoint writes"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory-snapshots"
                - "runtime.md#rt-rte-training-rollout"
                - "runtime.md#rt-rte-actor-update"
                - "runtime.md#rt-cmp-actor-model"
                - "runtime.md#rt-bap-reward-actor"
              note: "Worker/trainer machinery admits generated trajectories and numerical updates without a per-update human veto."
          records:
            - "memory.md#mem-obj-trajectory-snapshots"
            - "runtime.md#rt-rte-training-rollout"
            - "runtime.md#rt-rte-actor-update"
            - "runtime.md#rt-cmp-actor-model"
            - "runtime.md#rt-bap-reward-actor"
          note: "Launching the training curriculum is not manual admission of each snapshot or parameter update."
        -
          scope: "Optional merge handler admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-memory-merge"
              note: "The model/caller proposes keys and software admits the resulting merge."
          records:
            - "epistemic.md#epi-rte-memory-merge"
          note: "The configurable handler writes merged content without per-content human approval; default schema does not expose it."
        -
          scope: "Initial actor-checkpoint content and direct arbitrary library-dictionary initialization"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-actor-model"
            - "memory.md#mem-rte-training-stores"
          note: "Supplying a model path or a generic caller does not establish the explicit human content decision required for manual, nor a traced automatic admission mechanism for those initial contents."
      records:
        - "memory.md#mem-rte-inference-stores"
        - "memory.md#mem-rte-training-stores"
        - "memory.md#mem-obj-memory-indexes"
        - "runtime.md#rt-obj-context-masks"
        - "runtime.md#rt-rte-context-edit"
        - "memory.md#mem-rte-training-context"
        - "memory.md#mem-obj-trajectory-snapshots"
        - "runtime.md#rt-rte-training-rollout"
        - "runtime.md#rt-rte-actor-update"
        - "runtime.md#rt-cmp-actor-model"
        - "runtime.md#rt-bap-reward-actor"
        - "epistemic.md#epi-rte-memory-merge"
      note: "Subsequent model/code admissions are automatic. Initial content control is unresolved and cannot be labeled manual merely because an operator launches the workflow."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Summary, span and compression replacement of retained history in inference and training"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-context-masks"
                - "runtime.md#rt-rte-context-edit"
                - "memory.md#mem-rte-training-context"
              note: "Selected retained messages become reduced summaries, spans or compressed replacement strings."
          records:
            - "runtime.md#rt-obj-context-masks"
            - "runtime.md#rt-rte-context-edit"
            - "memory.md#mem-rte-training-context"
          note: "The implemented reduced-view transformation is consolidation; qualifier loss is a fidelity risk, not evidence of synthesis."
        -
          scope: "Append/overwrite revision of current keyed entries"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-inference-stores"
                - "memory.md#mem-rte-training-stores"
              note: "Append/overwrite changes a current keyed memory or note."
          records:
            - "memory.md#mem-rte-inference-stores"
            - "memory.md#mem-rte-training-stores"
          note: "Update checks and exact empty-content/summary behavior differ between training and inference; both revise existing retained entries."
        -
          scope: "Store deletion and context suppression"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-inference-stores"
                - "memory.md#mem-rte-training-stores"
                - "runtime.md#rt-obj-context-masks"
                - "runtime.md#rt-rte-context-edit"
                - "memory.md#mem-rte-training-context"
              note: "Deletion and eviction forget content from subsequent current-store or visible-context use."
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-context-masks"
                - "runtime.md#rt-rte-context-edit"
                - "memory.md#mem-rte-training-context"
              note: "A retained visibility mask withdraws reliance on the original message in later payloads while preserving backing history."
          records:
            - "memory.md#mem-rte-inference-stores"
            - "memory.md#mem-rte-training-stores"
            - "runtime.md#rt-obj-context-masks"
            - "runtime.md#rt-rte-context-edit"
            - "memory.md#mem-rte-training-context"
          note: "Store deletion removes current content; view masking withdraws access while backing history remains. Neither establishes semantic rejection of a false claim."
        -
          scope: "Optional merge of retained rich entries"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-memory-merge"
                - "memory.md#mem-obj-notes"
              note: "Body concatenation combines retained claims into one entry and discards rich fields; no semantic reconciliation is established."
          records:
            - "epistemic.md#epi-rte-memory-merge"
            - "memory.md#mem-obj-notes"
          note: "A configurable implemented handler combines bodies and removes inputs, but its absence from the default schema prevents asserting ordinary activation."
        -
          scope: "Semantic transformation of unrestricted new model-authored store content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-simple-notes"
            - "memory.md#mem-obj-memories"
            - "memory.md#mem-obj-training-notes"
            - "memory.md#mem-rte-inference-stores"
            - "memory.md#mem-rte-training-stores"
            - "epistemic.md#epi-obj-memory-content"
          note: "Arguments may be extraction, inference or error; no instantiated outputs establish additional synthesis, deduplication or promotion. Prompt requests alone do not establish those implemented transformations."
        -
          scope: "Lower-level actor optimization as additional curation of parameter state"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-actor-update"
          note: "An update call is established, but lower-level optimizer internals were not traced and cannot supply an additional controlled curation value."
      records:
        - "runtime.md#rt-obj-context-masks"
        - "runtime.md#rt-rte-context-edit"
        - "memory.md#mem-rte-training-context"
        - "memory.md#mem-rte-inference-stores"
        - "memory.md#mem-rte-training-stores"
        - "epistemic.md#epi-rte-memory-merge"
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-simple-notes"
        - "memory.md#mem-obj-memories"
        - "memory.md#mem-obj-training-notes"
        - "epistemic.md#epi-obj-memory-content"
        - "runtime.md#rt-rte-actor-update"
      note: "Implemented consolidation, entry revision and withdrawal/forgetting are classified. Unrestricted generated contents and lower-level parameter transformations do not support a complete operation list; rebuilding access metadata alone adds no curation value."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Automatic inventory supply and policy-requested keyed full-entry reads"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-inference-stores"
                - "memory.md#mem-rte-training-stores"
              note: "Payload rebuilding appends every current entry key/summary without a memory-read request."
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-inference-stores"
                - "memory.md#mem-rte-training-stores"
              note: "readNote/loadMemory return the full primary entry requested by the policy."
          records:
            - "memory.md#mem-rte-inference-stores"
            - "memory.md#mem-rte-training-stores"
          note: "These are separate operations: unsolicited summaries versus fulfillment of a consumer's exact-key request."
        -
          scope: "Related-memory display expansion within a requested rich-memory read"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-inference-stores"
                - "memory.md#mem-rte-training-stores"
                - "memory.md#mem-obj-memory-indexes"
              note: "Positive-scored neighbors are supplied automatically beyond the requested primary entry."
          records:
            - "memory.md#mem-rte-inference-stores"
            - "memory.md#mem-rte-training-stores"
            - "memory.md#mem-obj-memory-indexes"
          note: "The requested primary body remains pull; bounded neighbor displays are automatically added by a selector."
        -
          scope: "Inference mandatory recovery or key correction"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-inference-stores"
                - "runtime.md#rt-clm-fsm-controls"
              note: "Code-selected recovery material enters subsequent policy context without that exact policy request."
          records:
            - "memory.md#mem-rte-inference-stores"
            - "runtime.md#rt-clm-fsm-controls"
          note: "The controller can select a newest/sole entry or mechanically perform a mandatory read; model-requested identity is not universal."
        -
          scope: "Retained context replacements and training branch inheritance"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-context-masks"
                - "runtime.md#rt-rte-context-edit"
                - "memory.md#mem-rte-training-context"
                - "runtime.md#rt-rte-training-rollout"
              note: "Renderer and branch cloning carry forward retained summaries, masks and copied stores into later invocations."
          records:
            - "runtime.md#rt-obj-context-masks"
            - "runtime.md#rt-rte-context-edit"
            - "memory.md#mem-rte-training-context"
            - "runtime.md#rt-rte-training-rollout"
          note: "Later payload construction supplies the retained view, and descendants inherit copied memory/edit state without an independent retrieval request."
        -
          scope: "Worker-selected training snapshots and numerical checkpoint resume"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-actor-update"
                - "memory.md#mem-obj-trajectory-snapshots"
              note: "Selected snapshot rows and derived credit are automatically delivered to the update machinery."
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-actor-update"
              note: "The trainer loads saved actor state through its configured resume request."
          records:
            - "runtime.md#rt-rte-actor-update"
            - "memory.md#mem-obj-trajectory-snapshots"
          note: "Worker selection automatically supplies scored rows; trainer-requested checkpoint loading restores model state. Production deployment is not included as a proven read-back."
        -
          scope: "Possible additional consumers of inference trace files and production actor export"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-obj-full-history"
            - "runtime.md#rt-rte-document-qa"
            - "runtime.md#rt-rte-actor-update"
          note: "The records establish artifact persistence but not a semantic trace-reload route or complete model export/adoption route; no extra direction can be classified for these alternatives."
      records:
        - "memory.md#mem-rte-inference-stores"
        - "memory.md#mem-rte-training-stores"
        - "memory.md#mem-obj-memory-indexes"
        - "runtime.md#rt-clm-fsm-controls"
        - "runtime.md#rt-obj-context-masks"
        - "runtime.md#rt-rte-context-edit"
        - "memory.md#mem-rte-training-context"
        - "runtime.md#rt-rte-training-rollout"
        - "runtime.md#rt-rte-actor-update"
        - "memory.md#mem-obj-trajectory-snapshots"
        - "runtime.md#rt-obj-full-history"
        - "runtime.md#rt-rte-document-qa"
      note: "Both push and pull have wired witnesses. Persisted trace files and untraced production adoption remain unresolved alternatives rather than evidence of absent read-back."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "All-entry inventory push and whole-state inheritance"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-inference-stores"
                - "memory.md#mem-rte-training-stores"
                - "runtime.md#rt-rte-training-rollout"
              note: "Availability/current membership supplies the inventory and branch copy; keys displayed in an inventory do not alone establish identifier-targeted push."
          records:
            - "memory.md#mem-rte-inference-stores"
            - "memory.md#mem-rte-training-stores"
            - "runtime.md#rt-rte-training-rollout"
          note: "Trigger: payload/branch construction. Selector input: current store membership or cloned state. Selected part: all available summaries or copied memory state, not a question-ranked subset."
        -
          scope: "Automatic related-entry push"
          assessment: "known"
          findings:
            -
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-indexes"
                - "memory.md#mem-rte-inference-stores"
                - "memory.md#mem-rte-training-stores"
              note: "Fixed overlap of retained entry features/text contributes to neighbor prioritization."
            -
              value: "inferred-embedding"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-indexes"
                - "memory.md#mem-rte-inference-stores"
                - "memory.md#mem-rte-training-stores"
              note: "Optional cached dense similarities contribute to neighbor selection; vector-channel failure leaves fixed scoring active."
          records:
            - "memory.md#mem-rte-inference-stores"
            - "memory.md#mem-rte-training-stores"
            - "memory.md#mem-obj-memory-indexes"
          note: "Trigger: rich-memory read. Selector input: selected entry's retained features and optional vectors. Selected part: bounded positive-score neighbor summaries/episodes and score displays, not full neighbor bodies."
        -
          scope: "Message-identity substitution of retained context views"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-context-masks"
                - "runtime.md#rt-rte-context-edit"
                - "memory.md#mem-rte-training-context"
              note: "Actual message-ID lookup selects which retained replacement is delivered instead of the original message."
          records:
            - "runtime.md#rt-obj-context-masks"
            - "runtime.md#rt-rte-context-edit"
            - "memory.md#mem-rte-training-context"
          note: "Trigger: later payload rendering. Selector input: message IDs and retained edit maps. Selected part: the matching summary/span/compressed replacement or suppression view."
        -
          scope: "Automatic recovery reads and token-pressure view selection"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-inference-stores"
                - "runtime.md#rt-rte-context-edit"
                - "memory.md#mem-rte-training-context"
              note: "Code uses store availability/recency and age/size/budget rules, not an established relevance judgment."
          records:
            - "memory.md#mem-rte-inference-stores"
            - "runtime.md#rt-rte-context-edit"
            - "memory.md#mem-rte-training-context"
          note: "Trigger: mandatory-review API failure/key correction or context pressure. Selector input: availability/recency, age, size and simulated rendered length. Selected part: newest/sole saved entry or reducing retained view."
        -
          scope: "Snapshot ancestor-credit selection for update supply"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-actor-update"
                - "memory.md#mem-obj-trajectory-snapshots"
              note: "Actual ancestry ID matches associate retained snapshots with descendant terminal results."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-actor-update"
              note: "Configured output budgets and missing-terminal filtering further limit automatically supplied rows."
          records:
            - "runtime.md#rt-rte-actor-update"
            - "memory.md#mem-obj-trajectory-snapshots"
          note: "Trigger: training-row preparation. Selector input: node/prefix identities and available descendant terminals. Selected part: snapshot rows and associated descendant reward credit."
        -
          scope: "Additional snapshot downsampling priorities and possible file/export delivery selectors"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-training-rollout"
            - "runtime.md#rt-rte-actor-update"
            - "runtime.md#rt-obj-full-history"
          note: "The runtime explicitly leaves exact scheduler ranking and export/deployment untraced; trace-file persistence supplies no inspected selector. No extra signal is inferred from identifiers or filenames."
      records:
        - "memory.md#mem-rte-inference-stores"
        - "memory.md#mem-rte-training-stores"
        - "runtime.md#rt-rte-training-rollout"
        - "memory.md#mem-obj-memory-indexes"
        - "runtime.md#rt-obj-context-masks"
        - "runtime.md#rt-rte-context-edit"
        - "memory.md#mem-rte-training-context"
        - "runtime.md#rt-rte-actor-update"
        - "memory.md#mem-obj-trajectory-snapshots"
        - "runtime.md#rt-obj-full-history"
      note: "Signals are attached to actual push operations and selected parts. Exact downstream scheduling and possible file/export consumers remain unresolved; pull-only primary reads do not create identifier push findings."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Automatic inference and training history-to-replacement writes with later policy consumption"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-context-masks"
                - "runtime.md#rt-rte-context-edit"
                - "memory.md#mem-rte-training-context"
              note: "History-fed summaries, spans and compression results persist as behavior-shaping context for later policy calls."
          records:
            - "runtime.md#rt-obj-context-masks"
            - "runtime.md#rt-rte-context-edit"
            - "memory.md#mem-rte-training-context"
          note: "A within-trajectory summary qualifies because it is automatically admitted, retained and supplied at a later invocation. No measured improvement or new proposition is required."
        -
          scope: "Recorded rollout snapshots through reward assignment to actor state and checkpoint resume"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory-snapshots"
                - "runtime.md#rt-rte-training-rollout"
                - "runtime.md#rt-rte-actor-update"
                - "memory.md#mem-rte-training-context"
                - "runtime.md#rt-bap-reward-actor"
              note: "Scored rollout experience feeds actor updates and saved/reloaded parameters; operation and benefit remain unobserved."
          records:
            - "memory.md#mem-obj-trajectory-snapshots"
            - "runtime.md#rt-rte-training-rollout"
            - "runtime.md#rt-rte-actor-update"
            - "memory.md#mem-rte-training-context"
            - "runtime.md#rt-bap-reward-actor"
          note: "This is a wired trace-fed durable parameter-update path. Trainable synthetic actions and conditioning-only cleanup remain distinct; only the former supplies the synthetic action to actor training."
        -
          scope: "Unrestricted keyed text writes, arbitrary initial state and possible inference-log reuse"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-inference-stores"
            - "memory.md#mem-rte-training-stores"
            - "runtime.md#rt-obj-full-history"
            - "runtime.md#rt-rte-document-qa"
          note: "Entry authorship/admission does not prove trace derivation for every write, and persisted JSON has no established semantic reload consumer. The records contain no bounded absence warrant for a local no."
      records:
        - "runtime.md#rt-obj-context-masks"
        - "runtime.md#rt-rte-context-edit"
        - "memory.md#mem-rte-training-context"
        - "memory.md#mem-obj-trajectory-snapshots"
        - "runtime.md#rt-rte-training-rollout"
        - "runtime.md#rt-rte-actor-update"
        - "runtime.md#rt-bap-reward-actor"
        - "memory.md#mem-rte-inference-stores"
        - "memory.md#mem-rte-training-stores"
        - "runtime.md#rt-obj-full-history"
        - "runtime.md#rt-rte-document-qa"
      note: "Supported yes findings coexist with unresolved write/reuse alternatives. The inventory is partial; no local or system-wide no is asserted without an evidenced-absence record."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "History-derived retained replacement content in inference and training"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-context-masks"
                - "runtime.md#rt-rte-context-edit"
                - "memory.md#mem-rte-training-context"
                - "runtime.md#rt-obj-full-history"
              note: "Recorded assistant/session turns can feed retained summaries and reduced views."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-context-masks"
                - "runtime.md#rt-rte-context-edit"
                - "memory.md#mem-rte-training-context"
              note: "Recorded tool observations can feed retained summaries, spans and compressor output."
          records:
            - "runtime.md#rt-obj-context-masks"
            - "runtime.md#rt-rte-context-edit"
            - "memory.md#mem-rte-training-context"
            - "runtime.md#rt-obj-full-history"
          note: "The handlers can target assistant/session language and tool-result text; source values follow the original selected content rather than the message envelope."
        -
          scope: "Reward-fed actor update from sampled and qualifying synthetic rollout snapshots"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory-snapshots"
                - "runtime.md#rt-rte-training-rollout"
                - "runtime.md#rt-rte-actor-update"
              note: "Recorded prompt and policy-turn content participates in retained training experience."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory-snapshots"
                - "runtime.md#rt-rte-training-rollout"
                - "runtime.md#rt-rte-actor-update"
                - "memory.md#mem-rte-training-context"
              note: "Recorded tool requests/results and qualifying forced cleanup actions enter the training trace."
            -
              value: "trajectories"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory-snapshots"
                - "runtime.md#rt-rte-training-rollout"
                - "runtime.md#rt-rte-actor-update"
              note: "Snapshot ancestry and descendant terminal outcomes supply linked multi-step experience for parameter updates."
          records:
            - "memory.md#mem-obj-trajectory-snapshots"
            - "runtime.md#rt-rte-training-rollout"
            - "runtime.md#rt-rte-actor-update"
            - "memory.md#mem-rte-training-context"
          note: "Original inputs include conversational prompt/action content, tool feedback and linked multi-step rollouts with descendant outcomes. Code-authored actions do not become a new event-stream source merely because a hook emits them."
        -
          scope: "Unrestricted store admission and additional opaque initial/provider provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-inference-stores"
            - "memory.md#mem-rte-training-stores"
            - "runtime.md#rt-cmp-actor-model"
            - "runtime.md#rt-obj-full-history"
          note: "A qualifying trace-fed route is not established for every arbitrary stored argument or possible log consumer; neither original input type nor applicability can be settled for those alternatives."
      records:
        - "runtime.md#rt-obj-context-masks"
        - "runtime.md#rt-rte-context-edit"
        - "memory.md#mem-rte-training-context"
        - "runtime.md#rt-obj-full-history"
        - "memory.md#mem-obj-trajectory-snapshots"
        - "runtime.md#rt-rte-training-rollout"
        - "runtime.md#rt-rte-actor-update"
        - "memory.md#mem-rte-inference-stores"
        - "memory.md#mem-rte-training-stores"
        - "runtime.md#rt-cmp-actor-model"
      note: "Session logs, tool traces and linked trajectories support the known qualifying routes. Remaining origins and consumers are unresolved, not inapplicable merely because another route is understood."
---

# ContextPilot memory profile

## Comparison rationale

This profile classifies the handed accepted records, not target execution.
All positive findings are wired implementation witnesses. No supplied record
establishes observed use or causal benefit. Local uncertainties concern missing
provenance, incomplete downstream tracing and unconstrained content generation;
they do not cancel the inspected write and consumption paths.

### Objects, consumers and boundaries

The four keyed stores are different operative objects, not alternate names for
raw history. Their summaries reach later model calls automatically, while full
primary bodies are requested by key. Rich-memory reads also select bounded
neighbor displays. Dense vectors are retained access metadata and do not make
the dictionaries a vector database. Their producing provider's unpinned weights
do not erase the known derived-vector path, but they leave initial provenance
unresolved. See [MEM-OBJ-memory-indexes](memory.md#mem-obj-memory-indexes),
[MEM-RTE-inference-stores](memory.md#mem-rte-inference-stores) and
[MEM-RTE-training-stores](memory.md#mem-rte-training-stores).

Retained replacement text supplies knowledge/context at the policy consumer.
Its symbolic mask separately enforces visibility at the renderer. Standing
shipped guidance is excluded from accumulated memory; the records do not grant
saved facts special instruction priority. Fixed neighbor scoring gives retained
text/features ranking authority without requiring a learned ranking policy.
See [RT-OBJ-context-masks](runtime.md#rt-obj-context-masks),
[RT-BAP-context-policy](runtime.md#rt-bap-context-policy) and
[MEM-OBJ-memory-indexes](memory.md#mem-obj-memory-indexes).

Training snapshots supply scored/masked experience to the actor-update consumer,
which establishes learning authority there. Ancestry and masks also route credit
and exclude rows/tokens. Actor state is the retained output of that learning
path. Restoring it for continuing training does not independently establish
learning authority at the loader: the records do not show that the restored
parameters are consumed as examples, experience or feedback for another update.
Its downstream authority therefore remains not determinable rather than a
second learning finding. See
[MEM-OBJ-trajectory-snapshots](memory.md#mem-obj-trajectory-snapshots),
[RT-CMP-actor-model](runtime.md#rt-cmp-actor-model),
[RT-RTE-actor-update](runtime.md#rt-rte-actor-update) and
[RT-BAP-reward-actor](runtime.md#rt-bap-reward-actor).

Terminal scoring compares answers against supplied references and fixed format
rules. Those criteria are not established as accumulated or changed through use;
consequential scoring does not make them memory. They remain outside this
profile's memory boundary and supply no validation-authority finding. This does
not erase the learning authority of the scored experience at the update
consumer. See [EPI-OBJ-answer-evaluation](epistemic.md#epi-obj-answer-evaluation),
[EPI-RTE-terminal-evaluation](epistemic.md#epi-rte-terminal-evaluation) and
[RT-RTE-actor-update](runtime.md#rt-rte-actor-update).

### Transformations and selection

Consolidation describes the implemented reduced-history view, not a guarantee
of semantic fidelity. Retaining a substring after dropping a qualifier does not
establish synthesis. Optional merge combines existing bodies and loses rich
fields; its configurable handler is wired, but ordinary default exposure and
observed use are not established. Unrestricted new store arguments have no
complete semantic classification. See
[RT-RTE-context-edit](runtime.md#rt-rte-context-edit),
[MEM-RTE-training-context](memory.md#mem-rte-training-context),
[EPI-OBJ-memory-content](epistemic.md#epi-obj-memory-content) and
[EPI-RTE-memory-merge](epistemic.md#epi-rte-memory-merge).

Push signals name actual selection operations. All-summary availability is
coarse; matching a retained replacement to its message ID is identifier-based.
Requested primary reads are pull even though their key is an identifier.
Neighbor expansion is an additional automatic push with fixed-feature and
optional embedding signals. Recovery reads use availability/recency, not an
established relevance judgment. Training ancestry matches select descendant
credit; exact additional scheduler ranking remains uninspected. See
[MEM-RTE-inference-stores](memory.md#mem-rte-inference-stores),
[MEM-RTE-training-stores](memory.md#mem-rte-training-stores),
[RT-RTE-context-edit](runtime.md#rt-rte-context-edit),
[RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout) and
[RT-RTE-actor-update](runtime.md#rt-rte-actor-update).

### Learning coverage and unresolved alternatives

Automatic trace-fed replacement writes qualify when their result reaches a
later invocation, even within the same QA trajectory. The actor-update route
also qualifies, independently of whether improved capacity was measured.
Synthetic recovery has two branches: a trainable forced-action suffix or
conditioning only. Both alter later context; the latter does not supply a
trainable synthetic action. Session content, tool feedback and multi-step
rollouts retain their different origins. No event-stream value is inferred
merely from code-authored cleanup. See
[MEM-RTE-training-context](memory.md#mem-rte-training-context),
[MEM-OBJ-trajectory-snapshots](memory.md#mem-obj-trajectory-snapshots) and
[RT-RTE-actor-update](runtime.md#rt-rte-actor-update).

No evidenced-absence records were supplied. This profile therefore asserts no
local trace-learning negative and no absence of additional controlled values.
Known learning routes support the derived system union's "yes"; incomplete
coverage prevents a complete-value conclusion. A persisted inference trace
without a later semantic consumer is unresolved, not a negative learning
witness. Initial content control is similarly unresolved rather than manual.
See [RT-OBJ-full-history](runtime.md#rt-obj-full-history),
[RT-RTE-document-qa](runtime.md#rt-rte-document-qa),
[MEM-RTE-training-stores](memory.md#mem-rte-training-stores) and
[RT-RTE-actor-update](runtime.md#rt-rte-actor-update).

Reconciliation supplies no supersessions. Its container/part dispositions leave
the combined inference-content account and the four specific store objects
valid; training token snapshots remain distinct from inference history
snapshots. No value depends on replacing a declared record. The profile cites
only the permitted runtime, memory and epistemic declaring members.

### Source-read log

No target-source files were read for this classification. Only the supplied
invocation, job/type/contracts and handed report members were read; no named
record ambiguity required a permitted source reread.
