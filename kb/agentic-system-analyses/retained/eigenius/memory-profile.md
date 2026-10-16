---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Eigenius memory comparison of retained decision replay, resource graphs, derived indexes, published source and scoped proof-credit consumption."
run-id: "AAS-2026-10-15-eigenius-fe68ed89519b-01"
source-identity: "https://github.com/eigenius/eigenius"
reviewed-boundary: "836498ebd99733067d45aa6f7b09d4ff5035dd99"
memory-comparison:
  version: 2
  scope: "Included: use-accumulated document decision records, task result artifacts, layer-resident knowledge/program/proof/statistical resources, published notebook source, numerical access segments and rebuilt institution access state, with their admission, maintenance and later-consumer routes. Included unresolved alternatives: initial/bootstrap/import control, sense/proposal rationale use, full text-index derivation, local/offline mutations, reflection, autosave/merge persistence and durable task recovery. Excluded: shipped static ontologies/instructions/prompts as such, unretained current-document working context, external model weights/services and external dataset bytes beyond their retained descriptors and inspected consumer seams. The artifact remains a partial operational loop."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Layer corpus, ProposalDraw envelopes, published cells, retained programs, proof inputs, verification traces and statistical results"
          assessment: "known"
          findings:
            - value: "graph"
              basis: "wired"
              records:
                - "memory.md#mem-obj-layer-resources"
                - "memory.md#mem-obj-proposal-draw"
              note: "Resource identities, properties, references and layer visibility form the operative retained graph."
          records:
            - "memory.md#mem-obj-layer-resources"
            - "memory.md#mem-obj-proposal-draw"
            - "memory.md#mem-obj-notebook-cells"
            - "runtime.md#rt-obj-program-resource"
            - "epistemic.md#epi-obj-proof-inputs"
            - "epistemic.md#epi-obj-verification-trace"
            - "epistemic.md#epi-obj-statistical-result"
          note: "These are retained typed resource graphs on parent-linked layers, not a repository merely because the implementation is in Git."
        - scope: "Formalization task result metadata on the persistent backend"
          assessment: "known"
          findings:
            - value: "kv"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-formalization-artifact"
                - "runtime.md#rt-rte-document-formalize"
              note: "The metadata backend stores and fetches a result by its formalize:result task key; completion writes are best effort."
          records:
            - "runtime.md#rt-obj-formalization-artifact"
            - "runtime.md#rt-rte-document-formalize"
          note: "The task-UUID result key addresses a retained metadata blob. CBOR is an encoding, not a substrate."
        - scope: "Retained vector segments and optional HNSW access structure"
          assessment: "known"
          findings:
            - value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vector-segment"
                - "memory.md#mem-rte-query-resources"
              note: "Persisted dense segments support later similarity search."
            - value: "graph"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vector-segment"
              note: "Optional retained HNSW structure supplies graph-based vector access."
          records:
            - "memory.md#mem-obj-vector-segment"
            - "memory.md#mem-rte-query-resources"
          note: "The vector store and its optional graph are separately meaningful access structures; neither is provider weights."
        - scope: "Rebuilt institution index/runtime during the serving process"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-bap-institution-refresh"
              note: "The hook replaces the shared runtime with a rebuilt Arc for later operations."
          records:
            - "memory.md#mem-bap-institution-refresh"
            - "memory.md#mem-rte-index-refresh"
          note: "This is derived access state retained for subsequent dispatch, distinct from durable declarations."
        - scope: "Other backend, notebook, task and import storage alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-layer-resources"
            - "memory.md#mem-rte-state-maintenance"
            - "memory.md#mem-rte-notebook-reopen"
            - "memory.md#mem-rte-index-refresh"
          note: "Bootstrap/import admission, wider institution and reflection routes, local/offline mutations, full text-index maintenance, autosave/merge persistence and durable task recovery remain included but uninspected. The recorded inventory is not a whole-system enumeration."
      records:
        - "memory.md#mem-obj-layer-resources"
        - "memory.md#mem-obj-proposal-draw"
        - "memory.md#mem-obj-notebook-cells"
        - "runtime.md#rt-obj-program-resource"
        - "epistemic.md#epi-obj-proof-inputs"
        - "epistemic.md#epi-obj-verification-trace"
        - "epistemic.md#epi-obj-statistical-result"
        - "runtime.md#rt-obj-formalization-artifact"
        - "runtime.md#rt-rte-document-formalize"
        - "memory.md#mem-obj-vector-segment"
        - "memory.md#mem-rte-query-resources"
        - "memory.md#mem-bap-institution-refresh"
        - "memory.md#mem-rte-index-refresh"
        - "memory.md#mem-rte-state-maintenance"
        - "memory.md#mem-rte-notebook-reopen"
      note: "The accepted objects resolve graph/layer, metadata, vector and rebuilt dispatch storage; physical backend internals and the remaining retained-state inventory prevent complete coverage."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Resource graph identities, bodies, declarations, proof judgements and notebook query/configuration references"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-layer-resources"
                - "runtime.md#rt-obj-program-resource"
                - "epistemic.md#epi-obj-verification-trace"
              note: "Resource evaluation, dispatch and witness checking interpret explicit symbolic fields."
          records:
            - "memory.md#mem-obj-layer-resources"
            - "runtime.md#rt-obj-program-resource"
            - "memory.md#mem-obj-notebook-cells"
            - "epistemic.md#epi-obj-proof-inputs"
            - "epistemic.md#epi-obj-verification-trace"
            - "epistemic.md#epi-obj-statistical-result"
          note: "Localized properties and constructors have fixed programmatic consumers."
        - scope: "Draw envelopes and inspected decision fields, including selection/kind choices"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-proposal-draw"
                - "memory.md#mem-obj-selection-record"
                - "memory.md#mem-obj-kind-record"
              note: "Seam names, keys, indexes, abstentions and kind IRIs are rule-interpreted decision data."
          records:
            - "memory.md#mem-obj-proposal-draw"
            - "memory.md#mem-obj-selection-record"
            - "memory.md#mem-obj-kind-record"
          note: "A JSON string containing a record is not itself a natural-language prompt."
        - scope: "Selection glosses/rationale, kind rationale, notebook prose and retained completion strings"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-selection-record"
                - "memory.md#mem-obj-kind-record"
                - "memory.md#mem-obj-notebook-cells"
                - "epistemic.md#epi-obj-completion-template"
              note: "Retained prose, explanations and prompt strings have linguistic content."
          records:
            - "memory.md#mem-obj-selection-record"
            - "memory.md#mem-obj-kind-record"
            - "memory.md#mem-obj-notebook-cells"
            - "epistemic.md#epi-obj-completion-template"
          note: "These text parts require human/model interpretation, even when embedded in symbolic resources; rationale display does not imply operational use."
        - scope: "Dense vector values"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vector-segment"
              note: "Dense embedding values spread representation over numerical coordinates; this does not assert model-weight updates."
          records:
            - "memory.md#mem-obj-vector-segment"
          note: "Dense distributed numerical representations are distinct from symbolic subject IDs and model/dimension metadata."
        - scope: "Vector subject and model/dimension/metric metadata"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vector-segment"
              note: "The retained segment has rule-interpreted IDs and compatibility metadata."
          records:
            - "memory.md#mem-obj-vector-segment"
          note: "Explicit metadata controls shape checks, subject identity and compatibility rather than linguistic interpretation."
        - scope: "Inspected sense/proposal decision payloads beyond their known symbolic fields"
          assessment: "partial"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-rank-record"
                - "memory.md#mem-obj-proposal-record"
              note: "Stored order/ranking and returned proposals feed resolver decision implementations."
          records:
            - "memory.md#mem-obj-rank-record"
            - "memory.md#mem-obj-proposal-record"
          note: "Rank/order and Proposal fields are symbolic; full rationale/probability transformations and downstream interpretation were not independently read."
        - scope: "Pinned external data payloads and untraced imported/persisted alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "epistemic.md#epi-obj-pinned-file"
            - "memory.md#mem-obj-layer-resources"
          note: "The pinned-file descriptor is symbolic, but the bytes have content-dependent form. Import and other retained-state paths are not fully inspected; no form is inferred from a display or descriptor."
      records:
        - "memory.md#mem-obj-layer-resources"
        - "runtime.md#rt-obj-program-resource"
        - "memory.md#mem-obj-notebook-cells"
        - "epistemic.md#epi-obj-proof-inputs"
        - "epistemic.md#epi-obj-verification-trace"
        - "epistemic.md#epi-obj-statistical-result"
        - "memory.md#mem-obj-proposal-draw"
        - "memory.md#mem-obj-selection-record"
        - "memory.md#mem-obj-kind-record"
        - "epistemic.md#epi-obj-completion-template"
        - "memory.md#mem-obj-vector-segment"
        - "memory.md#mem-obj-rank-record"
        - "memory.md#mem-obj-proposal-record"
        - "epistemic.md#epi-obj-pinned-file"
      note: "Inspected operative symbolic, linguistic and numerical parts are separated by consumer. Full sense/proposal payload interpretation, external data contents and remaining alternatives are unresolved."
    lineage:
      assessment: "partial"
      units:
        - scope: "Live decision exchanges recorded into ProposalDraw resources"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-draw-retention"
                - "memory.md#mem-obj-proposal-draw"
              note: "Recorder output extracts question/answer data from the formalization decision activity for later replay."
          records:
            - "memory.md#mem-rte-draw-retention"
            - "memory.md#mem-obj-proposal-draw"
          note: "This unit is the automatic recorder path, not unknown original authorship of externally supplied recordings."
        - scope: "Externally supplied inline recordings and loaded resource inputs"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-rte-draw-retention"
                - "runtime.md#rt-rte-resource-admission"
              note: "Inline records and caller-supplied resource documents enter the retained-state routes from outside those routes."
          records:
            - "memory.md#mem-rte-draw-retention"
            - "runtime.md#rt-rte-resource-admission"
            - "epistemic.md#epi-obj-proof-inputs"
          note: "Import identifies the entry path, not the original producer or truth of supplied material."
        - scope: "Generated artifacts, query/program outputs and checker/statistical result resources"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-formalization-artifact"
                - "runtime.md#rt-rte-program-execution"
                - "memory.md#mem-rte-query-resources"
                - "epistemic.md#epi-rte-lean-check"
                - "epistemic.md#epi-rte-statistical-decision"
              note: "Parser/emitter, evaluator and domain-checker routes construct durable resource artifacts from supplied inputs."
          records:
            - "runtime.md#rt-obj-formalization-artifact"
            - "runtime.md#rt-rte-program-execution"
            - "memory.md#mem-rte-query-resources"
            - "epistemic.md#epi-rte-lean-check"
            - "epistemic.md#epi-rte-statistical-decision"
          note: "These are computed structured outputs. Their common compiled lineage does not identify them with each other or establish scientific warrant."
        - scope: "Vector/index derivation and published notebook serialization"
          assessment: "partial"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-rte-index-refresh"
                - "memory.md#mem-rte-notebook-reopen"
              note: "Resource material becomes numerical index segments; edited notebook source becomes content-addressed graph resources."
          records:
            - "memory.md#mem-obj-vector-segment"
            - "memory.md#mem-rte-index-refresh"
            - "memory.md#mem-rte-notebook-reopen"
          note: "Compilation is wired, but exact vector source-property extraction, initial notebook content origin and provider representation provenance remain unresolved."
        - scope: "Explicit caller editing of notebook source"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-notebook-reopen"
                - "memory.md#mem-obj-notebook-cells"
              note: "The publication route accepts caller-edited source, and reopening reconstructs it for editing."
          records:
            - "memory.md#mem-rte-notebook-reopen"
            - "memory.md#mem-obj-notebook-cells"
          note: "Editable source affords authored content, without asserting who authored every published cell."
        - scope: "Initial lexicon/bootstrap, imports and all untraced content origins"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-layer-resources"
            - "memory.md#mem-obj-rank-record"
            - "memory.md#mem-obj-proposal-record"
          note: "Bootstrap/import admission, wider institution and reflection routes, local/offline mutations, full text-index maintenance, autosave/merge persistence and durable task recovery remain included but uninspected. The recorded inventory is not a whole-system enumeration."
      records:
        - "memory.md#mem-rte-draw-retention"
        - "memory.md#mem-obj-proposal-draw"
        - "runtime.md#rt-rte-resource-admission"
        - "epistemic.md#epi-obj-proof-inputs"
        - "runtime.md#rt-obj-formalization-artifact"
        - "runtime.md#rt-rte-program-execution"
        - "memory.md#mem-rte-query-resources"
        - "epistemic.md#epi-rte-lean-check"
        - "epistemic.md#epi-rte-statistical-decision"
        - "memory.md#mem-obj-vector-segment"
        - "memory.md#mem-rte-index-refresh"
        - "memory.md#mem-rte-notebook-reopen"
        - "memory.md#mem-obj-notebook-cells"
        - "memory.md#mem-obj-layer-resources"
        - "memory.md#mem-obj-rank-record"
        - "memory.md#mem-obj-proposal-record"
      note: "Known derivation paths do not settle initial caller authorship or embedding-provider provenance. Independent imported and trace-extracted paths coexist with compilation."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Recorded selection, ranking, proposal and classification fields at replay consumers"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-bap-recorded-decision"
              note: "Stored choices/proposals/kinds select parser, resolver and lander outputs."
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-rank-record"
                - "memory.md#mem-bap-recorded-decision"
              note: "Retained sense order/rank information influences candidate priority."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-bap-recorded-decision"
                - "memory.md#mem-obj-selection-record"
              note: "A recorded abstention/refusal can withhold the decision output."
          records:
            - "memory.md#mem-bap-recorded-decision"
            - "memory.md#mem-rte-draw-retention"
            - "memory.md#mem-obj-rank-record"
          note: "Replay supplies operational decisions rather than optional background text. The classification concerns returned fields, not uninspected rationale interpretation."
        - scope: "Resource and vector material at retrieval and notebook inspection consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-query-resources"
                - "memory.md#mem-rte-notebook-reopen"
              note: "Requested retained facts and editable source supply context/reference to the later caller."
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-rte-query-resources"
                - "memory.md#mem-obj-vector-segment"
              note: "Retained text/vector features affect lexical, vector and hybrid result ordering."
          records:
            - "memory.md#mem-rte-query-resources"
            - "memory.md#mem-obj-vector-segment"
            - "memory.md#mem-rte-notebook-reopen"
          note: "Returned reference/source content and similarity ranking are distinct effects, neither a truth certificate."
        - scope: "Retained completion text at the CompleteText model"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-completion-template"
                - "runtime.md#rt-bap-completion-prompt"
              note: "Stored system/user strings guide later model calls through input interpolation."
          records:
            - "epistemic.md#epi-obj-completion-template"
            - "runtime.md#rt-bap-completion-prompt"
          note: "Prompt guidance has instruction force, not guaranteed compliance or a grant to register capabilities."
        - scope: "Retained program symbolic body at IO evaluation and institution declarations at dispatch"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-retained-program"
                - "memory.md#mem-bap-institution-refresh"
              note: "Executable bodies select evaluation/dispatch operations; declarations rebuild later institution dispatch context."
          records:
            - "runtime.md#rt-bap-retained-program"
            - "memory.md#mem-bap-institution-refresh"
          note: "Execution/dispatch paths choose supported operations under the active registry; symbolic execution is not evidence that all contained text is instruction."
        - scope: "Retained proof judgements and dependency state at witness-dependent type checking"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-witness-consumption"
              note: "Current chain evidence and proposition/dependency matches determine whether a witness-dependent constructor is well-typed."
            - value: "enforcement"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-witness-consumption"
              note: "Missing credit or rebound/tombstoned dependencies block witness admission."
          records:
            - "epistemic.md#epi-rte-witness-consumption"
            - "epistemic.md#epi-obj-verification-trace"
          note: "Formal proof credit and dependency checks have bounded conformance and veto effects. Declared/Observed attribution and ProgramTrace do not inherit Verified authority."
        - scope: "Live recorded decision experience at durable replay-artifact production"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-draw-retention"
                - "memory.md#mem-bap-recorded-decision"
              note: "Recorded execution exchanges feed the retained decision artifact that supplies later parser/resolver behavior. No capacity improvement is asserted."
          records:
            - "memory.md#mem-rte-draw-retention"
            - "memory.md#mem-bap-recorded-decision"
          note: "The recorder converts prior decision experience into durable behavior-shaping replay implementations, independently of downstream ranking/routing force."
        - scope: "Untraced rationale, imported policy, institution and recovery consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-proposal-record"
            - "memory.md#mem-obj-rank-record"
            - "memory.md#mem-obj-layer-resources"
            - "runtime.md#rt-rte-program-execution"
          note: "Bootstrap/import admission, wider institution and reflection routes, local/offline mutations, full text-index maintenance, autosave/merge persistence and durable task recovery remain included but uninspected. The recorded inventory is not a whole-system enumeration."
      records:
        - "memory.md#mem-bap-recorded-decision"
        - "memory.md#mem-rte-draw-retention"
        - "memory.md#mem-obj-rank-record"
        - "memory.md#mem-rte-query-resources"
        - "memory.md#mem-obj-vector-segment"
        - "memory.md#mem-rte-notebook-reopen"
        - "epistemic.md#epi-obj-completion-template"
        - "runtime.md#rt-bap-completion-prompt"
        - "runtime.md#rt-bap-retained-program"
        - "memory.md#mem-bap-institution-refresh"
        - "epistemic.md#epi-rte-witness-consumption"
        - "epistemic.md#epi-obj-verification-trace"
        - "memory.md#mem-obj-proposal-record"
        - "memory.md#mem-obj-layer-resources"
        - "runtime.md#rt-rte-program-execution"
      note: "Authority is attached to each actual consumer, not assigned uniformly to persisted content. Supported ranking, routing, instruction, knowledge, validation, enforcement and learning paths do not resolve untraced consumers."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Live draw recording, generated result retention and optional notebook land"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-draw-retention"
                - "runtime.md#rt-rte-document-formalize"
                - "runtime.md#rt-rte-resource-admission"
              note: "Recorders, result storage and optional immediate Load admit generated content under software control."
          records:
            - "memory.md#mem-rte-draw-retention"
            - "runtime.md#rt-rte-document-formalize"
            - "runtime.md#rt-rte-resource-admission"
          note: "These writes do not require an explicit human decision on each retained output."
        - scope: "Program/query output, domain-result disposition, index refresh and maintenance transformations"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-program-execution"
                - "memory.md#mem-rte-query-resources"
                - "epistemic.md#epi-rte-verdict-disposition"
                - "memory.md#mem-rte-index-refresh"
                - "memory.md#mem-rte-state-maintenance"
              note: "Software computes/adopts outputs, derivative indexes and eligible maintenance changes."
          records:
            - "runtime.md#rt-rte-program-execution"
            - "memory.md#mem-rte-query-resources"
            - "epistemic.md#epi-rte-verdict-disposition"
            - "memory.md#mem-rte-index-refresh"
            - "memory.md#mem-rte-state-maintenance"
          note: "Starting a query or maintenance job is not manual admission of each computed result; full maintenance CAS/recovery is outside this control finding."
        - scope: "Explicit browser editing/publishing of notebook source"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-notebook-reopen"
                - "memory.md#mem-obj-notebook-cells"
              note: "The editor/publication surface affords an operator decision supplying retained source, not mandatory human review of generated claims."
          records:
            - "memory.md#mem-rte-notebook-reopen"
            - "memory.md#mem-obj-notebook-cells"
          note: "A human can explicitly supply/edit/publish retained notebook content; generic SDK publication has a separate unresolved principal."
        - scope: "Generic Load, inline records and SDK publication initial content decisions"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-resource-admission"
            - "memory.md#mem-rte-draw-retention"
            - "memory.md#mem-rte-notebook-reopen"
          note: "Callers may be human or automated. Code performs I/O, but that alone cannot classify the upstream per-content decision."
        - scope: "Bootstrap/import, offline mutation, autosave and durable recovery admission"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-layer-resources"
            - "memory.md#mem-rte-notebook-reopen"
          note: "Bootstrap/import admission, wider institution and reflection routes, local/offline mutations, full text-index maintenance, autosave/merge persistence and durable task recovery remain included but uninspected. The recorded inventory is not a whole-system enumeration."
      records:
        - "memory.md#mem-rte-draw-retention"
        - "runtime.md#rt-rte-document-formalize"
        - "runtime.md#rt-rte-resource-admission"
        - "runtime.md#rt-rte-program-execution"
        - "memory.md#mem-rte-query-resources"
        - "epistemic.md#epi-rte-verdict-disposition"
        - "memory.md#mem-rte-index-refresh"
        - "memory.md#mem-rte-state-maintenance"
        - "memory.md#mem-rte-notebook-reopen"
        - "memory.md#mem-obj-notebook-cells"
        - "memory.md#mem-obj-layer-resources"
      note: "Software-controlled admission is established on concrete routes. Generic caller identity leaves human control of other writes unresolved; browser publication alone does not certify per-claim human approval."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Layer consolidation over existing definitions and tombstones"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-state-maintenance"
              note: "Combining a layer range into latest effective definitions/tombstones reduces representation of existing content."
          records:
            - "memory.md#mem-rte-state-maintenance"
          note: "The merge reduces the retained representation by first-seen modification per IRI while preserving suppression; it is not model summarization."
        - scope: "Tombstones, cascade suppression and dependency-based proof-credit withdrawal"
          assessment: "known"
          findings:
            - value: "invalidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-resource-admission"
                - "memory.md#mem-rte-state-maintenance"
                - "epistemic.md#epi-rte-witness-consumption"
              note: "Tombstones suppress resolution and dependency rebinding refuses ancestor witness credit."
          records:
            - "runtime.md#rt-rte-resource-admission"
            - "memory.md#mem-rte-state-maintenance"
            - "epistemic.md#epi-rte-witness-consumption"
          note: "Withdrawal of current reliance is distinct from physical deletion and can preserve immutable history."
        - scope: "Eligible unreachable-layer garbage collection"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-state-maintenance"
              note: "GC removes eligible unreachable retained layers, reducing accessible retained history."
          records:
            - "memory.md#mem-rte-state-maintenance"
          note: "This is storage forgetting under reachability and age conditions, not content-directed rejection; complete erasure and metadata expiry remain unproved."
        - scope: "Replacement of vector segments after changed model declarations"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-index-refresh"
          note: "This bounded operation rebuilds the access index under changed model declarations. Index rebuilding alone is excluded from curation operations; the record establishes no separate qualifying memory-entry transformation."
        - scope: "Semantic effect of general generated/query resources"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-formalization-artifact"
            - "memory.md#mem-rte-query-resources"
            - "epistemic.md#epi-rte-prompt-interpolation"
          note: "The records do not establish whether arbitrary output preserves, entails or adds claims. No synthesize finding follows from generation, fluency or an indeterminate transformation."
        - scope: "Other semantic curation, text-index lifecycle and recovery transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-layer-resources"
            - "memory.md#mem-rte-index-refresh"
            - "memory.md#mem-rte-notebook-reopen"
          note: "Bootstrap/import admission, wider institution and reflection routes, local/offline mutations, full text-index maintenance, autosave/merge persistence and durable task recovery remain included but uninspected. The recorded inventory is not a whole-system enumeration."
      records:
        - "memory.md#mem-rte-state-maintenance"
        - "runtime.md#rt-rte-resource-admission"
        - "epistemic.md#epi-rte-witness-consumption"
        - "memory.md#mem-rte-index-refresh"
        - "runtime.md#rt-obj-formalization-artifact"
        - "memory.md#mem-rte-query-resources"
        - "epistemic.md#epi-rte-prompt-interpolation"
        - "memory.md#mem-obj-layer-resources"
        - "memory.md#mem-rte-notebook-reopen"
      note: "Concrete layer consolidation, visibility withdrawal and storage forgetting support positive values. Vector reindexing alone supplies no curation value. Neither the name consolidation nor model generation establishes semantic synthesis; broader transformations remain uninspected."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Explicit query/inspect, notebook reopen, result fetch and program-by-IRI requests"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-query-resources"
                - "memory.md#mem-rte-notebook-reopen"
                - "runtime.md#rt-obj-formalization-artifact"
                - "runtime.md#rt-rte-program-execution"
              note: "Caller-directed requests return selected retained resources, source, results or executable bodies."
          records:
            - "memory.md#mem-rte-query-resources"
            - "memory.md#mem-rte-notebook-reopen"
            - "runtime.md#rt-obj-formalization-artifact"
            - "runtime.md#rt-rte-program-execution"
          note: "These consumers ask for retained material or a specifically named retained program; code fulfilling the request is not an additional push."
        - scope: "Document-branch draw loading followed by keyed decision replay"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-draw-retention"
              note: "The later formalization request selects document recordings, with inline/live/branch alternatives."
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-draw-retention"
                - "memory.md#mem-bap-recorded-decision"
              note: "The installed replay selector automatically injects a matching retained answer into a decision seam rather than requiring a request for that individual saved answer."
          records:
            - "memory.md#mem-rte-draw-retention"
            - "memory.md#mem-bap-recorded-decision"
          note: "The document request selects the branch/recording source; within it, a replay implementation automatically matches each decision question and supplies the saved answer to the parser."
        - scope: "Post-commit institution index/runtime refresh"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-index-refresh"
                - "memory.md#mem-bap-institution-refresh"
              note: "The hook rebuilds and installs dispatch state from the committed chain without a consumer request for those declarations."
          records:
            - "memory.md#mem-rte-index-refresh"
            - "memory.md#mem-bap-institution-refresh"
          note: "A commit automatically refreshes retained declaration-derived dispatch context for later operations; it is not an unsolicited chat-context route."
        - scope: "Chain-attached witness-dependent checking"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-witness-consumption"
              note: "Category, target and proposition select available chain witness credit during type checking."
          records:
            - "epistemic.md#epi-rte-witness-consumption"
          note: "A later checking request causes automatic evidence lookup; the checking consumer receives selected retained credit rather than a user-requested trace document."
        - scope: "Alternative CLI, reflection, autosave and durable task consumer directions"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-layer-resources"
            - "runtime.md#rt-rte-program-execution"
            - "memory.md#mem-rte-notebook-reopen"
          note: "Bootstrap/import admission, wider institution and reflection routes, local/offline mutations, full text-index maintenance, autosave/merge persistence and durable task recovery remain included but uninspected. The recorded inventory is not a whole-system enumeration."
      records:
        - "memory.md#mem-rte-query-resources"
        - "memory.md#mem-rte-notebook-reopen"
        - "runtime.md#rt-obj-formalization-artifact"
        - "runtime.md#rt-rte-program-execution"
        - "memory.md#mem-rte-draw-retention"
        - "memory.md#mem-bap-recorded-decision"
        - "memory.md#mem-rte-index-refresh"
        - "memory.md#mem-bap-institution-refresh"
        - "epistemic.md#epi-rte-witness-consumption"
        - "memory.md#mem-obj-layer-resources"
      note: "Requested returns coexist with automatic internal selection. Push is assigned only to the independent retained-part selectors inside the computation, not a second delivery of requested query/notebook results."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Keyed replay to parser/resolver/lander on a formalization decision"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-draw-retention"
                - "memory.md#mem-obj-selection-record"
                - "memory.md#mem-obj-kind-record"
              note: "An actual exact question-key match selects the delivered saved answer, not merely a catalog entry."
          records:
            - "memory.md#mem-rte-draw-retention"
            - "memory.md#mem-obj-selection-record"
            - "memory.md#mem-obj-kind-record"
            - "memory.md#mem-bap-recorded-decision"
          note: "Trigger: decision seam invocation. Input: question key. Selected part: matching saved choice/rank/proposal/kind. Selection/proposal use context-rich keys; kind uses sentence/gloss only."
        - scope: "Post-commit declaration-derived dispatch-context installation"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-index-refresh"
                - "memory.md#mem-bap-institution-refresh"
              note: "The refresh supplies available declaration-derived context at the commit boundary, rather than matching a consumer topic."
          records:
            - "memory.md#mem-rte-index-refresh"
            - "memory.md#mem-bap-institution-refresh"
          note: "Trigger: commit hook. Input: new committed chain. Selected retained material: available institution declarations used to rebuild the runtime; no relevance-ranked or per-task declaration selection is established."
        - scope: "Witness credit supplied during chain-attached checking"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-witness-consumption"
              note: "IRI and proposition-hash matching select actual credit; rebinding checks can refuse it."
          records:
            - "epistemic.md#epi-rte-witness-consumption"
          note: "Trigger: witness-dependent check. Inputs: category, target IRI, normalized proposition and dependencies. Selected retained part: matching local/ancestor proof judgement or trace credit."
        - scope: "Push selectors on untraced reflection, task recovery and alternative consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-layer-resources"
            - "runtime.md#rt-rte-program-execution"
            - "memory.md#mem-rte-notebook-reopen"
          note: "Bootstrap/import admission, wider institution and reflection routes, local/offline mutations, full text-index maintenance, autosave/merge persistence and durable task recovery remain included but uninspected. The recorded inventory is not a whole-system enumeration."
      records:
        - "memory.md#mem-rte-draw-retention"
        - "memory.md#mem-obj-selection-record"
        - "memory.md#mem-obj-kind-record"
        - "memory.md#mem-bap-recorded-decision"
        - "memory.md#mem-rte-index-refresh"
        - "memory.md#mem-bap-institution-refresh"
        - "epistemic.md#epi-rte-witness-consumption"
        - "memory.md#mem-obj-layer-resources"
        - "runtime.md#rt-rte-program-execution"
        - "memory.md#mem-rte-notebook-reopen"
      note: "Signals are classified on actual push selectors, not borrowed from pull-query similarity or an identifier attached to a requested notebook. Untraced delivery alternatives prevent complete coverage."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Live formalization decision exchanges to retained draws to later replay"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-draw-retention"
                - "memory.md#mem-obj-proposal-draw"
                - "memory.md#mem-bap-recorded-decision"
              note: "Experience automatically produces durable behavior-shaping decision records with a concrete later consumer; no weight update or improved capacity is required."
          records:
            - "memory.md#mem-rte-draw-retention"
            - "memory.md#mem-obj-proposal-draw"
            - "memory.md#mem-bap-recorded-decision"
          note: "The automatic recorder extracts executed decision questions/answers into persistent structured artifacts that change later parser/resolver/lander behavior. Branch reset limits horizon but does not negate the wired next-invocation route."
        - scope: "Retained program traces and durable task recovery alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-program-execution"
          note: "Trace retention is known, but a later trace-derived policy/behavior artifact and full recovery consumers are not established. This is not bounded absence of every qualifying write."
        - scope: "Vector refresh over resource material"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-index-refresh"
            - "memory.md#mem-obj-vector-segment"
          note: "Automatic durable numerical derivation is wired, but original indexed content is not established as trace experience. No trace-learning yes or no is inferred from asynchronous indexing alone."
        - scope: "Other imports, reflection, maintenance and recovery learning alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-layer-resources"
            - "memory.md#mem-rte-notebook-reopen"
          note: "Bootstrap/import admission, wider institution and reflection routes, local/offline mutations, full text-index maintenance, autosave/merge persistence and durable task recovery remain included but uninspected. The recorded inventory is not a whole-system enumeration."
      records:
        - "memory.md#mem-rte-draw-retention"
        - "memory.md#mem-obj-proposal-draw"
        - "memory.md#mem-bap-recorded-decision"
        - "runtime.md#rt-rte-program-execution"
        - "memory.md#mem-rte-index-refresh"
        - "memory.md#mem-obj-vector-segment"
        - "memory.md#mem-obj-layer-resources"
        - "memory.md#mem-rte-notebook-reopen"
      note: "Automatic recording of decision experience into durable replay artifacts supports a local yes. Raw program traces, index derivation and uninspected recovery alternatives do not establish a system-wide no or complete inventory."
    trace_source:
      assessment: "not-determinable"
      units:
        - scope: "Original inputs to automatic live decision recording"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-draw-retention"
            - "memory.md#mem-obj-selection-record"
            - "memory.md#mem-obj-proposal-record"
            - "memory.md#mem-obj-kind-record"
          note: "The records establish source prose, contextual questions and model answers. They do not establish that the original input is session-logs, tool-traces, event-streams or linked state/action/outcome trajectories. Calling an RPC a tool would not establish the origin of the retained content."
        - scope: "Original trace input to untraced program/recovery and other qualifying-write alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-program-execution"
            - "memory.md#mem-obj-layer-resources"
          note: "Bootstrap/import admission, wider institution and reflection routes, local/offline mutations, full text-index maintenance, autosave/merge persistence and durable task recovery remain included but uninspected. The recorded inventory is not a whole-system enumeration."
      records:
        - "memory.md#mem-rte-draw-retention"
        - "memory.md#mem-obj-selection-record"
        - "memory.md#mem-obj-proposal-record"
        - "memory.md#mem-obj-kind-record"
        - "runtime.md#rt-rte-program-execution"
        - "memory.md#mem-obj-layer-resources"
      note: "The qualifying draw route has recorded model decision activity, but accepted records do not resolve its original inputs into the controlled trace-origin categories. Do not relabel a model exchange as an agent session or environmental event."
---

# Eigenius memory profile

## Comparison rationale

The classifications concern retained material and its actual later consumers, not every storage or permission mechanism in the runtime. All positive implementation findings are wired; manual notebook editing/publication is an afforded operator route. No accepted record supplies observed operation or causal benefit. Partial axes retain the included uninspected alternatives rather than allowing one implemented witness to stand for a complete system inventory.

### Objects, representations and provenance

The layered resource graph, result-key metadata and vector access segments have different storage roles. Graph structure and numerical vector storage can coexist in the HNSW access path. Provider weights are excluded: the accepted records establish inference dependencies, not parameters accumulated or changed through this platform's use. Dense segments are parametric representations, not learned provider weights. Symbolic JSON decision fields remain distinct from linguistic rationale and gloss fields. A readable rendering does not replace the encoded consumed artifact. See [MEM-OBJ-vector-segment](memory.md#mem-obj-vector-segment), [MEM-OBJ-selection-record](memory.md#mem-obj-selection-record) and [RT-OBJ-formalization-artifact](runtime.md#rt-obj-formalization-artifact).

Trace-extracted lineage is assigned to automatic live-exchange recording; externally supplied recordings have imported lineage at entry. The same object kind can therefore have different derivation paths. Generated resource artifacts and index segments have other-compiled lineage without a claim of new knowledge. Initial lexicon, caller and embedding provenance remain unresolved. Published notebook serialization does not establish that every cell was human-authored. See [MEM-RTE-draw-retention](memory.md#mem-rte-draw-retention), [MEM-RTE-index-refresh](memory.md#mem-rte-index-refresh) and [MEM-RTE-notebook-reopen](memory.md#mem-rte-notebook-reopen).

### Authority and maintenance

Retained decisions route or rank parser work, retained completion strings instruct a model, and retained graph/vector material supplies knowledge or retrieval ranking inputs. Formal witness evidence instead has validation and enforcing force at a specific checker. It does not grant generic truth authority to all retained assertions. The recorded experience has learning authority at production of the durable replay artifact, separately from that artifact's routing/ranking effect at replay. See [MEM-BAP-recorded-decision](memory.md#mem-bap-recorded-decision), [RT-BAP-completion-prompt](runtime.md#rt-bap-completion-prompt) and [EPI-RTE-witness-consumption](epistemic.md#epi-rte-witness-consumption).

Layer consolidation is reduction of the effective representation of existing definitions, not semantic synthesis. Tombstones and witness-credit withdrawal invalidate current reliance; eligible unreachable-layer deletion is decay in the storage-forgetting sense. Vector segment replacement under changed model declarations is access-index rebuilding alone, not a qualifying evolve operation. Its bounded curation unit is inapplicable; no separate memory-entry revision is established by the accepted record. No dedup value is inferred merely from content addressing or primary-key identity, and no synthesize value follows from unassessed model/query output. These classifications do not certify erasure, crash consistency, scientific warrant or complete maintenance coverage. See [MEM-RTE-state-maintenance](memory.md#mem-rte-state-maintenance), [MEM-RTE-index-refresh](memory.md#mem-rte-index-refresh) and [EPI-RTE-witness-consumption](epistemic.md#epi-rte-witness-consumption).

### Read-back and trace boundary

A query, notebook reopen or artifact fetch returns requested retained material: pull. A requested formalization can also contain a subsequent automatic keyed replay selection: push at the decision consumer, not a second push of the caller's requested result. Post-commit installation of declaration-derived dispatch state is coarse push. A witness-dependent check selects actual retained evidence by target/proposition identity. Pull-query lexical/vector ranking is not imported into the push-signal axis. See [MEM-RTE-query-resources](memory.md#mem-rte-query-resources), [MEM-RTE-draw-retention](memory.md#mem-rte-draw-retention), [MEM-BAP-institution-refresh](memory.md#mem-bap-institution-refresh) and [EPI-RTE-witness-consumption](epistemic.md#epi-rte-witness-consumption).

The automatic decision-exchange recorder has a durable later replay consumer and therefore supports a local trace-learning yes without parameter training or demonstrated improvement. It does not establish any controlled original trace-source category: document prose and model decision exchanges are not automatically conversational session logs, tool traces, environmental event streams or trajectories. That missing origin fact leaves trace_source not-determinable. Other unresolved routes are not made inapplicable by the known replay route. See [MEM-RTE-draw-retention](memory.md#mem-rte-draw-retention), [MEM-OBJ-selection-record](memory.md#mem-obj-selection-record) and [RT-RTE-program-execution](runtime.md#rt-rte-program-execution).

Replay's horizon is explicitly bounded. Branch recreation plus recording only live exchanges can remove old decisions from the next default branch after an all-replay invocation. This limits persistence coverage without withdrawing the implemented subsequent-consumer path. Sense/proposal rationale use, original generic-caller control, vector input provenance and recovery remain independent gaps. See [MEM-RTE-draw-retention](memory.md#mem-rte-draw-retention), [MEM-OBJ-rank-record](memory.md#mem-obj-rank-record) and [MEM-OBJ-proposal-record](memory.md#mem-obj-proposal-record).

### Reconciliation and source-read log

The supplied reconciliation contains no supersessions and no unresolved cross-report conflicts. All citations therefore retain their declaring records. The broader query route and narrower FIBER retention route remain valid overlapping scopes; neither replaces Load or program execution. The profile does not merge domain proof inputs, generated artifacts and general corpus containers into one provenance chain. See [MEM-RTE-query-resources](memory.md#mem-rte-query-resources), [EPI-RTE-fiber-retention](epistemic.md#epi-rte-fiber-retention) and [EPI-RTE-lean-check](epistemic.md#epi-rte-lean-check).

Source reads for this classification: none. Only the supplied invocation, types, contracts and accepted members were read. No new evidence or records were introduced, and no report verification was reopened.
