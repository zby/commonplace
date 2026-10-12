---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "AgeMem memory comparison at the frozen arXiv v1 boundary: abstract LTM, retained conversational context and trajectory-trained policy parameters."
run-id: "AAS-2026-10-12-2601-01885v1-32274e5bddc1-01"
source-identity: "https://arxiv.org/html/2601.01885v1"
reviewed-boundary: "arxiv-2601.01885v1-html-2026-10-12"
memory-comparison:
  version: 2
  scope: "Included: accumulated LTM content, retained dense encodings and access metadata; active conversational material after accumulation, Summary or Filter and its later consumers; collected training experience, reward-derived supervision and changed policy weights; documented explicit and driver-owned admission/read-back alternatives, including unresolved state serialization and checkpoint/provider persistence. Excluded: static shipped tool/summarizer/evaluator prompts and schemas, ordinary unchanged current-call state, imported benchmark reference material as a separate memory store, publication-only metrics, external framework internals and other systems. The horizon established for textual memory is later invocations and stages of an episode; training parameters reach subsequent training decisions and reported evaluation, not an inspected deployment."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "LTM content, embedding tuples and access metadata"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-content"
            - "memory.md#mem-obj-embedding"
            - "runtime.md#rt-cmp-text-encoder"
            - "memory.md#mem-obj-access-metadata"
          note: "An abstract external store is specified. Dense encodings do not establish a vector storage substrate; backend and reload implementation are uninspected."
        -
          scope: "Active conversational context, surviving messages and replacement summaries"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-summary"
            - "runtime.md#rt-rte-context-summary"
            - "epistemic.md#epi-obj-context-content"
            - "runtime.md#rt-rte-context-filter"
          note: "A message list and replacement prose are retained between invocations. Their abstract notation does not establish an in-memory backend or durable transcript storage."
        -
          scope: "Training experience buffer and numerical supervision"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-experience"
            - "runtime.md#rt-rte-policy-update"
          note: "An abstract buffer is reinitialized in training. Serialized logs, replay retention and the physical substrate are unspecified."
        -
          scope: "Policy parameters changed by GRPO and used in later invocations"
          assessment: "known"
          findings:
            -
              value: "model-weights"
              basis: "claimed"
              records:
                - "runtime.md#rt-cmp-agent-policy"
                - "runtime.md#rt-bap-trained-policy"
                - "memory.md#mem-obj-experience"
                - "runtime.md#rt-rte-policy-update"
              note: "Gradient optimization retains changed model parameters that govern subsequent rollout and reported evaluation decisions."
          records:
            - "runtime.md#rt-cmp-agent-policy"
            - "runtime.md#rt-bap-trained-policy"
            - "memory.md#mem-obj-experience"
            - "runtime.md#rt-rte-policy-update"
          note: "The operative retained result is updated weights; checkpoint files and serving infrastructure are not separately identified."
      records:
        - "memory.md#mem-obj-content"
        - "memory.md#mem-obj-embedding"
        - "runtime.md#rt-cmp-text-encoder"
        - "memory.md#mem-obj-access-metadata"
        - "memory.md#mem-obj-summary"
        - "runtime.md#rt-rte-context-summary"
        - "epistemic.md#epi-obj-context-content"
        - "runtime.md#rt-rte-context-filter"
        - "memory.md#mem-obj-experience"
        - "runtime.md#rt-rte-policy-update"
        - "runtime.md#rt-cmp-agent-policy"
        - "runtime.md#rt-bap-trained-policy"
      note: "The inventory includes LTM text, embeddings and metadata, active context and summaries, training experience and updated policy parameters. Only the parameter substrate has a controlled value; abstract stores and buffers do not identify files, RAM, databases or a vector backend. Deployment checkpoint and provider-state persistence remain unresolved."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "LTM content interpreted by the task policy"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-content"
                - "memory.md#mem-bap-retained-context"
              note: "Retrieved stored prose supplies interpreted context to the policy."
          records:
            - "memory.md#mem-obj-content"
            - "memory.md#mem-bap-retained-context"
          note: "The content string is separate from its embedding and addressing fields."
        -
          scope: "Stored dense content embeddings consumed by cosine selection"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-embedding"
                - "runtime.md#rt-cmp-text-encoder"
              note: "Dense numerical encodings distribute text representation across coordinates used by the selector."
          records:
            - "memory.md#mem-obj-embedding"
            - "runtime.md#rt-cmp-text-encoder"
          note: "The retained encoder output is numerical distributed representation, not the encoder weights or readable prose."
        -
          scope: "Access metadata and retrieved identifiers"
          assessment: "partial"
          findings:
            -
              value: "symbolic"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-access-metadata"
                - "memory.md#mem-rte-requested-retrieval"
              note: "IDs target entries and metadata filters narrow retrieval through localized fields."
          records:
            - "memory.md#mem-obj-access-metadata"
            - "memory.md#mem-rte-requested-retrieval"
          note: "Addressing/filter fields are specified, but free-form source descriptions and returned layouts are not fixed. Their full natural-language payload cannot be enumerated."
        -
          scope: "Surviving conversational text and generated replacement summary"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "claimed"
              records:
                - "epistemic.md#epi-obj-context-content"
                - "runtime.md#rt-rte-context-filter"
                - "memory.md#mem-obj-summary"
                - "runtime.md#rt-rte-context-summary"
                - "memory.md#mem-bap-retained-context"
              note: "Later policy invocations interpret surviving messages and generated summary prose."
          records:
            - "epistemic.md#epi-obj-context-content"
            - "runtime.md#rt-rte-context-filter"
            - "memory.md#mem-obj-summary"
            - "runtime.md#rt-rte-context-summary"
            - "memory.md#mem-bap-retained-context"
          note: "This unit names the prose part, excluding call envelopes and IDs classified with symbolic material."
        -
          scope: "Experience tuples: conversation/action text versus tuple/scoring fields"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-experience"
                - "runtime.md#rt-rte-policy-update"
              note: "States and generated responses contain conversational and action text."
            -
              value: "symbolic"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-experience"
                - "runtime.md#rt-rte-policy-update"
              note: "State/action/reward/log-probability tuples and scalar supervision have localized bookkeeping and optimizer rules."
          records:
            - "memory.md#mem-obj-experience"
            - "runtime.md#rt-rte-policy-update"
          note: "The record explicitly distinguishes text from tuple structure, scores and old log probabilities; these are not learned weights."
        -
          scope: "Updated policy parameters at later policy invocation"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "claimed"
              records:
                - "runtime.md#rt-cmp-agent-policy"
                - "runtime.md#rt-bap-trained-policy"
              note: "Learned parameters influence the future action distribution."
          records:
            - "runtime.md#rt-cmp-agent-policy"
            - "runtime.md#rt-bap-trained-policy"
          note: "The component records establish distributed weights without exposing localized propositions."
      records:
        - "memory.md#mem-obj-content"
        - "memory.md#mem-bap-retained-context"
        - "memory.md#mem-obj-embedding"
        - "runtime.md#rt-cmp-text-encoder"
        - "memory.md#mem-obj-access-metadata"
        - "memory.md#mem-rte-requested-retrieval"
        - "epistemic.md#epi-obj-context-content"
        - "runtime.md#rt-rte-context-filter"
        - "memory.md#mem-obj-summary"
        - "runtime.md#rt-rte-context-summary"
        - "memory.md#mem-obj-experience"
        - "runtime.md#rt-rte-policy-update"
        - "runtime.md#rt-cmp-agent-policy"
        - "runtime.md#rt-bap-trained-policy"
      note: "Text, dense embeddings, symbolic access fields, mixed experience and updated weights are separately classified. Metadata free-form payload and exact model-visible rendering remain unresolved; provider opacity does not negate the documented parametric role."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Policy-generated Add and Update content"
          assessment: "partial"
          findings:
            -
              value: "authored"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-content"
                - "memory.md#mem-rte-store-maintenance"
              note: "The model supplies the content string admitted by Add or Update."
            -
              value: "trace-extracted"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-content"
                - "memory.md#mem-rte-store-maintenance"
              note: "The documented conversational branch selects and rewrites interaction information, including user preferences, into stored content; this does not classify every supporting-fact input as a trace."
          records:
            - "memory.md#mem-obj-content"
            - "memory.md#mem-rte-store-maintenance"
          note: "The policy selects and rewrites presented information. The record does not establish whether every string is copied, compressed or newly derived, so no universal trace-extracted or synthesized lineage is asserted."
        -
          scope: "Retained content embeddings"
          assessment: "partial"
          findings:
            -
              value: "other-compiled"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-embedding"
                - "runtime.md#rt-cmp-text-encoder"
              note: "The encoder transforms retained text into its dense numerical access representation."
          records:
            - "memory.md#mem-obj-embedding"
            - "runtime.md#rt-cmp-text-encoder"
          note: "The content-to-embedding path is explicit; encoder training provenance and exact version remain unknown."
        -
          scope: "Access metadata creation and replacement"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-access-metadata"
          note: "Optional caller/model fields coexist with described timestamps and source information. Which fields the executor generates or verifies is unspecified; no complete derivation classification is established."
        -
          scope: "Driver-supplied context and surviving messages"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-task-rollout"
                - "epistemic.md#epi-obj-context-content"
                - "runtime.md#rt-rte-context-filter"
              note: "Driver-selected supporting information is acquired as input, not produced by AgeMem."
            -
              value: "authored"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-task-rollout"
                - "epistemic.md#epi-obj-context-content"
                - "runtime.md#rt-rte-context-filter"
              note: "The driver appends generated policy responses to context; surviving response text has model authorship, unlike imported supporting information."
          records:
            - "epistemic.md#epi-obj-context-content"
            - "runtime.md#rt-rte-context-filter"
            - "runtime.md#rt-rte-task-rollout"
          note: "Supporting context and distractors enter the episode, while generated responses and earlier summaries also appear. The origin of each surviving part is unresolved."
        -
          scope: "Generated replacement conversation summary"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-summary"
                - "runtime.md#rt-rte-context-summary"
              note: "Summary derives later-consumed memory from prior conversational activity."
          records:
            - "memory.md#mem-obj-summary"
            - "runtime.md#rt-rte-context-summary"
          note: "The named derivation is selected conversation messages through the summarizer to retained prose; fidelity is not established."
        -
          scope: "Training experience and GRPO-updated policy parameters"
          assessment: "partial"
          findings:
            -
              value: "trace-extracted"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-experience"
                - "runtime.md#rt-rte-policy-update"
                - "runtime.md#rt-cmp-agent-policy"
                - "runtime.md#rt-bap-trained-policy"
              note: "Collected stage experience is transformed into reward-derived parameter changes used by later invocations."
          records:
            - "memory.md#mem-obj-experience"
            - "runtime.md#rt-rte-policy-update"
            - "runtime.md#rt-cmp-agent-policy"
            - "runtime.md#rt-bap-trained-policy"
          note: "Experience collection and trace-fed parameter updates are specified. This does not resolve imported backbone training provenance, checkpoint lineage or synthetic-distractor provenance."
      records:
        - "memory.md#mem-obj-content"
        - "memory.md#mem-rte-store-maintenance"
        - "memory.md#mem-obj-embedding"
        - "runtime.md#rt-cmp-text-encoder"
        - "memory.md#mem-obj-access-metadata"
        - "epistemic.md#epi-obj-context-content"
        - "runtime.md#rt-rte-context-filter"
        - "runtime.md#rt-rte-task-rollout"
        - "memory.md#mem-obj-summary"
        - "runtime.md#rt-rte-context-summary"
        - "memory.md#mem-obj-experience"
        - "runtime.md#rt-rte-policy-update"
        - "runtime.md#rt-cmp-agent-policy"
        - "runtime.md#rt-bap-trained-policy"
      note: "Documented derivation paths include model authorship, conversational extraction, encoder compilation and imported driver context. Exact copy/derivation for store strings, metadata generation, original data provenance and initial model provenance remain unresolved."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Retrieved LTM prose and retained conversational prose at the task policy"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "claimed"
              records:
                - "memory.md#mem-bap-retained-context"
                - "memory.md#mem-obj-content"
                - "memory.md#mem-obj-summary"
                - "runtime.md#rt-rte-context-summary"
              note: "Selected stored text, summaries and surviving messages supply facts and interpretive context for subsequent reasoning."
          records:
            - "memory.md#mem-obj-content"
            - "memory.md#mem-obj-summary"
            - "runtime.md#rt-rte-context-summary"
            - "epistemic.md#epi-obj-context-content"
            - "runtime.md#rt-rte-context-filter"
            - "memory.md#mem-bap-retained-context"
          note: "This is contextual interpretation, not evidenced instruction-priority elevation, enforced compliance or content acceptance."
        -
          scope: "LTM embeddings at cosine retrieval selector"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-embedding"
                - "runtime.md#rt-cmp-text-encoder"
                - "runtime.md#rt-rte-stage-retrieval"
                - "memory.md#mem-rte-requested-retrieval"
              note: "Cosine similarity of retained embeddings and query encodings determines top-k entry selection."
          records:
            - "memory.md#mem-obj-embedding"
            - "runtime.md#rt-cmp-text-encoder"
            - "runtime.md#rt-rte-stage-retrieval"
            - "memory.md#mem-rte-requested-retrieval"
          note: "The retained feature representation influences relative retrieval priority; similarity establishes no truth warrant."
        -
          scope: "Retained message text at Filter similarity selector"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "claimed"
              records:
                - "epistemic.md#epi-obj-context-content"
                - "runtime.md#rt-rte-context-filter"
              note: "Dense encodings of retained messages influence their similarity score relative to the removal criterion."
          records:
            - "epistemic.md#epi-obj-context-content"
            - "runtime.md#rt-rte-context-filter"
          note: "The retained text is scored for removal eligibility; criterion polarity and encoder opacity limit reliability, not the stated score influence."
        -
          scope: "Access metadata at search restriction and retrieved ID at Update/Delete targeting"
          assessment: "partial"
          findings:
            -
              value: "routing"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-access-metadata"
                - "memory.md#mem-rte-store-maintenance"
                - "memory.md#mem-rte-requested-retrieval"
              note: "Retained identifiers select mutation targets and metadata fields restrict the search scope."
          records:
            - "memory.md#mem-obj-access-metadata"
            - "memory.md#mem-rte-requested-retrieval"
            - "memory.md#mem-rte-store-maintenance"
          note: "Filtering and target addressing are specified. Authentication, criterion enforcement and actual returned field layout are uninspected; source labels establish no trust elevation."
        -
          scope: "Experience and reward-derived supervision at optimizer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-experience"
                - "runtime.md#rt-rte-policy-update"
              note: "Recorded states/actions/outcomes and terminal advantages feed policy parameter optimization."
          records:
            - "memory.md#mem-obj-experience"
            - "runtime.md#rt-rte-policy-update"
          note: "The update consumer differs from the downstream policy consumer; scalar feedback is not a memory-entry admission gate."
        -
          scope: "Updated policy weights at subsequent action selection"
          assessment: "partial"
          findings:
            -
              value: "routing"
              basis: "claimed"
              records:
                - "runtime.md#rt-cmp-agent-policy"
                - "runtime.md#rt-bap-trained-policy"
                - "memory.md#mem-obj-experience"
                - "runtime.md#rt-rte-policy-update"
              note: "Updated parameters influence selection of subsequent memory operations and generated actions."
          records:
            - "runtime.md#rt-cmp-agent-policy"
            - "runtime.md#rt-bap-trained-policy"
            - "memory.md#mem-obj-experience"
            - "runtime.md#rt-rte-policy-update"
          note: "The specified output distribution selects operations and language; opaque internal content and exact checkpoint loading prevent a complete enumeration of downstream forces."
      records:
        - "memory.md#mem-obj-content"
        - "memory.md#mem-obj-summary"
        - "runtime.md#rt-rte-context-summary"
        - "epistemic.md#epi-obj-context-content"
        - "runtime.md#rt-rte-context-filter"
        - "memory.md#mem-bap-retained-context"
        - "memory.md#mem-obj-embedding"
        - "runtime.md#rt-cmp-text-encoder"
        - "runtime.md#rt-rte-stage-retrieval"
        - "memory.md#mem-rte-requested-retrieval"
        - "memory.md#mem-obj-access-metadata"
        - "memory.md#mem-rte-store-maintenance"
        - "memory.md#mem-obj-experience"
        - "runtime.md#rt-rte-policy-update"
        - "runtime.md#rt-cmp-agent-policy"
        - "runtime.md#rt-bap-trained-policy"
      note: "The documented consumers establish knowledge, ranking, routing and learning paths. Exact rendering, opaque policy processing and deployment admission controls prevent complete authority enumeration. Static tool prompts and schemas are excluded rather than counted as acquired instruction or validation memory."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Policy Add/Update/Delete request admitted to the abstract store"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-store-maintenance"
              note: "Model-generated content and target requests drive store mutation; its confirmation boolean is not human approval."
          records:
            - "memory.md#mem-rte-store-maintenance"
          note: "For this documented mechanism the model proposes and the described tool installs the change, without a per-content operator decision."
        -
          scope: "Summary replacement and Filter omission, including task-derived criterion alternative"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-summary"
                - "runtime.md#rt-rte-context-summary"
                - "epistemic.md#epi-obj-context-content"
                - "runtime.md#rt-rte-context-filter"
              note: "The summarizer output replaces selected messages and the threshold tool omits messages without per-content human approval."
          records:
            - "memory.md#mem-obj-summary"
            - "runtime.md#rt-rte-context-summary"
            - "epistemic.md#epi-obj-context-content"
            - "runtime.md#rt-rte-context-filter"
          note: "Both criterion alternatives and the summary installation mechanism are computational. Missing criterion derivation or preservation checks do not turn the stated admission manual."
        -
          scope: "Experience collection and GRPO parameter-update admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-experience"
                - "runtime.md#rt-rte-policy-update"
                - "runtime.md#rt-rte-task-rollout"
              note: "Rollout bookkeeping and optimization admit retained traces and changed parameters computationally."
          records:
            - "memory.md#mem-obj-experience"
            - "runtime.md#rt-rte-policy-update"
            - "runtime.md#rt-rte-task-rollout"
          note: "Researchers define the objective and launch training; the driver collects experience and gradient ascent applies each update."
        -
          scope: "Initial context/metadata supply and backbone or deployment checkpoint admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-access-metadata"
            - "runtime.md#rt-rte-task-rollout"
            - "runtime.md#rt-cmp-agent-policy"
            - "runtime.md#rt-bap-trained-policy"
          note: "The records name input selection and a backbone but do not identify all content-control principals or a separate serving replacement decision. Read selection cannot establish manual or automatic checkpoint admission."
      records:
        - "memory.md#mem-rte-store-maintenance"
        - "memory.md#mem-obj-summary"
        - "runtime.md#rt-rte-context-summary"
        - "epistemic.md#epi-obj-context-content"
        - "runtime.md#rt-rte-context-filter"
        - "memory.md#mem-obj-experience"
        - "runtime.md#rt-rte-policy-update"
        - "runtime.md#rt-rte-task-rollout"
        - "memory.md#mem-obj-access-metadata"
        - "runtime.md#rt-cmp-agent-policy"
        - "runtime.md#rt-bap-trained-policy"
      note: "The documented store mutations, context transformations, trajectory collection and gradient updates use computational admission. Researcher setup and preference input do not make these admissions manual. Initial backbone admission, checkpoint replacement and complete context/metadata initialization control remain unknown."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Conversation summary replacement"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-summary"
                - "runtime.md#rt-rte-context-summary"
              note: "Selected conversation history is reduced to a summary for subsequent policy consumption."
          records:
            - "memory.md#mem-obj-summary"
            - "runtime.md#rt-rte-context-summary"
          note: "The described operation compresses existing conversation into replacement prose. Actual semantic fidelity is unresolved; a defect would not alone make it synthesis."
        -
          scope: "Update of an existing store entry"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-store-maintenance"
                - "memory.md#mem-obj-content"
                - "memory.md#mem-obj-embedding"
                - "runtime.md#rt-cmp-text-encoder"
              note: "Update revises existing text, regenerates its embedding and changes modification metadata."
          records:
            - "memory.md#mem-rte-store-maintenance"
            - "memory.md#mem-obj-content"
            - "memory.md#mem-obj-embedding"
            - "runtime.md#rt-cmp-text-encoder"
          note: "This classifies replacement of the retained entry, not the unknown semantic relationship of every emitted replacement claim."
        -
          scope: "Delete, Filter and stage context reset"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-store-maintenance"
                - "epistemic.md#epi-obj-context-content"
                - "runtime.md#rt-rte-context-filter"
                - "runtime.md#rt-rte-task-rollout"
              note: "Delete removes entries, Filter omits messages and reset clears context at the stage transition."
          records:
            - "memory.md#mem-rte-store-maintenance"
            - "epistemic.md#epi-obj-context-content"
            - "runtime.md#rt-rte-context-filter"
            - "runtime.md#rt-rte-task-rollout"
          note: "These operations forget current retained material. Tombstones, version history and propagated retraction are not specified, so invalidate is not asserted."
        -
          scope: "Other semantic transformations of generated store content and retained checkpoint history"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-content"
            - "epistemic.md#epi-rte-language-content"
            - "memory.md#mem-obj-experience"
            - "runtime.md#rt-rte-policy-update"
          note: "The input/output semantic relation of arbitrary policy content is indeterminate, and checkpoint retention is unspecified. These records cannot establish dedup, synthesize, promote or another retained-history operation."
      records:
        - "memory.md#mem-obj-summary"
        - "runtime.md#rt-rte-context-summary"
        - "memory.md#mem-rte-store-maintenance"
        - "memory.md#mem-obj-content"
        - "memory.md#mem-obj-embedding"
        - "runtime.md#rt-cmp-text-encoder"
        - "epistemic.md#epi-obj-context-content"
        - "runtime.md#rt-rte-context-filter"
        - "runtime.md#rt-rte-task-rollout"
        - "epistemic.md#epi-rte-language-content"
        - "memory.md#mem-obj-experience"
        - "runtime.md#rt-rte-policy-update"
      note: "Summary compression, entry replacement and removal are specified transformations over retained material, all at claimed basis. Semantic effects of arbitrary generated store strings and checkpoint history are unresolved. Neither occurrence rewards nor narrated cleanup establish implemented deduplication, synthesis or history-preserving invalidation."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Policy-requested Retrieve_memory selection and return"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-requested-retrieval"
              note: "A model-selected query/count/filter request obtains retained entries for the next policy invocation."
          records:
            - "memory.md#mem-rte-requested-retrieval"
          note: "The selector fulfills the policy request. Its return is not a second push merely because code inserts results into context."
        -
          scope: "Stage 1 pre-action retrieval"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-stage-retrieval"
              note: "The driver supplies selected existing memories against the sampled message to the next action decision."
          records:
            - "runtime.md#rt-rte-stage-retrieval"
          note: "Algorithm 3 retrieves before policy choice, independently of an explicit request for retained material."
        -
          scope: "Replacement summary and surviving context supplied to subsequent policy invocation"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-summary"
                - "runtime.md#rt-rte-context-summary"
                - "epistemic.md#epi-obj-context-content"
                - "runtime.md#rt-rte-context-filter"
                - "runtime.md#rt-rte-task-rollout"
              note: "Subsequent policy calls and Stage 3 receive retained context without a separate memory-read request."
          records:
            - "memory.md#mem-obj-summary"
            - "runtime.md#rt-rte-context-summary"
            - "epistemic.md#epi-obj-context-content"
            - "runtime.md#rt-rte-context-filter"
            - "memory.md#mem-bap-retained-context"
            - "runtime.md#rt-rte-task-rollout"
          note: "Requesting a transformation does not itself request later read-back; the driver later carries retained transformed context forward."
        -
          scope: "Buffered experience to optimizer and changed parameters to subsequent training decisions"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-experience"
                - "runtime.md#rt-rte-policy-update"
                - "runtime.md#rt-cmp-agent-policy"
                - "runtime.md#rt-bap-trained-policy"
              note: "The driver supplies retained experience to optimization and the changed policy governs later invocations."
          records:
            - "memory.md#mem-obj-experience"
            - "runtime.md#rt-rte-policy-update"
            - "runtime.md#rt-cmp-agent-policy"
            - "runtime.md#rt-bap-trained-policy"
          note: "The training driver schedules consumption of the collected trajectory group and current policy parameters; no target-policy retrieval request controls these paths."
        -
          scope: "Additional model-visible store serialization and deployment checkpoint read-back"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-task-rollout"
            - "runtime.md#rt-cmp-agent-policy"
            - "runtime.md#rt-bap-trained-policy"
            - "memory.md#mem-obj-experience"
            - "runtime.md#rt-rte-policy-update"
          note: "Abstract state tuples do not settle full-store input serialization, and no deployment loader is inspected. Known delivery paths do not resolve these alternatives."
      records:
        - "memory.md#mem-rte-requested-retrieval"
        - "runtime.md#rt-rte-stage-retrieval"
        - "memory.md#mem-obj-summary"
        - "runtime.md#rt-rte-context-summary"
        - "epistemic.md#epi-obj-context-content"
        - "runtime.md#rt-rte-context-filter"
        - "memory.md#mem-bap-retained-context"
        - "runtime.md#rt-rte-task-rollout"
        - "memory.md#mem-obj-experience"
        - "runtime.md#rt-rte-policy-update"
        - "runtime.md#rt-cmp-agent-policy"
        - "runtime.md#rt-bap-trained-policy"
      note: "Both model-requested retrieval and independently triggered Stage 1 delivery exist in the specified design. Later context and training consumers are included separately. Exact full-store state serialization and deployment checkpoint routes remain unresolved rather than being excluded as pull-only."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Explicit policy-requested retrieval return"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-requested-retrieval"
          note: "This completely named operation fulfills a read request; signal characterizes push selection rather than this pull response."
        -
          scope: "Stage 1 driver retrieval selecting stored entries"
          assessment: "known"
          findings:
            -
              value: "inferred-embedding"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-stage-retrieval"
                - "memory.md#mem-obj-embedding"
                - "runtime.md#rt-cmp-text-encoder"
              note: "Automatic selection ranks existing memory by cosine similarity to the sampled message."
          records:
            - "runtime.md#rt-rte-stage-retrieval"
            - "memory.md#mem-obj-embedding"
            - "runtime.md#rt-cmp-text-encoder"
          note: "Trigger: sampled Stage 1 message before the policy action. Input: message encoding and existing memory embeddings. Selected part: cosine top-k entries; k limits count, not tokens."
        -
          scope: "Filter-selected surviving messages delivered on later policy call"
          assessment: "known"
          findings:
            -
              value: "inferred-embedding"
              basis: "claimed"
              records:
                - "epistemic.md#epi-obj-context-content"
                - "runtime.md#rt-rte-context-filter"
              note: "Cosine criterion/message similarity determines which retained messages remain available for delivery."
          records:
            - "epistemic.md#epi-obj-context-content"
            - "runtime.md#rt-rte-context-filter"
          note: "Trigger: context-maintenance action followed by the next invocation. Input: retained messages and supplied or task-derived criterion. Selected part: messages surviving the similarity threshold. The automatic criterion derivation remains unspecified."
        -
          scope: "Summary span and ordinary retained-context carryover to subsequent policy calls"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-summary"
                - "runtime.md#rt-rte-context-summary"
                - "runtime.md#rt-rte-task-rollout"
              note: "Whole-context and positional span carryover supply retained material without targeted retained-item matching."
          records:
            - "memory.md#mem-obj-summary"
            - "runtime.md#rt-rte-context-summary"
            - "runtime.md#rt-rte-task-rollout"
            - "memory.md#mem-bap-retained-context"
          note: "Trigger: later invocation or Stage 3 transition. Input: current retained context and policy-selected all/N span for compaction. Selected part: replacement prose and remaining messages, without an evidenced identity match or targeted query."
        -
          scope: "Training-group experience and current updated weights supplied by the driver"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-experience"
                - "runtime.md#rt-rte-policy-update"
                - "runtime.md#rt-cmp-agent-policy"
                - "runtime.md#rt-bap-trained-policy"
              note: "Training consumes the generated group and current parameters without a documented per-item targeted read selector."
          records:
            - "memory.md#mem-obj-experience"
            - "runtime.md#rt-rte-policy-update"
            - "runtime.md#rt-cmp-agent-policy"
            - "runtime.md#rt-bap-trained-policy"
          note: "Trigger: group optimization and subsequent training invocation. Input: current episode group and current updated policy. Selected part: collected experience and changed parameters, not retrieved prose entries."
        -
          scope: "Whole-store state visibility and deployed checkpoint selection"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-task-rollout"
            - "runtime.md#rt-cmp-agent-policy"
            - "runtime.md#rt-bap-trained-policy"
          note: "No serialization or serving loader establishes a selector, trigger-input contract or selected payload for these included alternatives."
      records:
        - "memory.md#mem-rte-requested-retrieval"
        - "runtime.md#rt-rte-stage-retrieval"
        - "memory.md#mem-obj-embedding"
        - "runtime.md#rt-cmp-text-encoder"
        - "epistemic.md#epi-obj-context-content"
        - "runtime.md#rt-rte-context-filter"
        - "memory.md#mem-obj-summary"
        - "runtime.md#rt-rte-context-summary"
        - "runtime.md#rt-rte-task-rollout"
        - "memory.md#mem-bap-retained-context"
        - "memory.md#mem-obj-experience"
        - "runtime.md#rt-rte-policy-update"
        - "runtime.md#rt-cmp-agent-policy"
        - "runtime.md#rt-bap-trained-policy"
      note: "Signals classify automatic delivery operations, not query syntax on the pull route. Stage retrieval and Filter use embedding-based selection; context-span carryover and grouped training supply are coarse. Unknown state serialization and serving selection prevent complete coverage."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Automatic conversational extraction to LTM followed by later retrieval"
          assessment: "partial"
          findings:
            -
              value: "yes"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-content"
                - "memory.md#mem-rte-store-maintenance"
                - "memory.md#mem-rte-requested-retrieval"
              note: "A documented conversation-to-store-to-later-policy chain automatically produces retained behavior-shaping context from interaction."
          records:
            - "memory.md#mem-obj-content"
            - "memory.md#mem-rte-store-maintenance"
            - "memory.md#mem-rte-requested-retrieval"
          note: "The model writes information from presented conversation and illustrative user preferences, retaining it for later policy context. Static supporting-fact inputs and arbitrary generated strings need not all be trace-fed; their provenance and exact derivation remain unresolved."
        -
          scope: "Automatic conversation summary to later policy context"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-summary"
                - "runtime.md#rt-rte-context-summary"
                - "memory.md#mem-bap-retained-context"
              note: "Trace-fed summary installation creates a continuation artifact for a later consumer; semantic novelty and measured improvement are not required."
          records:
            - "memory.md#mem-obj-summary"
            - "runtime.md#rt-rte-context-summary"
            - "memory.md#mem-bap-retained-context"
          note: "Selected prior conversational activity produces retained replacement prose that affects the input available at the next invocation; within-episode retention suffices for this route."
        -
          scope: "Automatic trajectory/reward processing into policy weights"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-experience"
                - "runtime.md#rt-rte-policy-update"
                - "runtime.md#rt-cmp-agent-policy"
                - "runtime.md#rt-bap-trained-policy"
              note: "GRPO automatically converts scored trajectories into retained learned parameters for later policy consumption."
          records:
            - "memory.md#mem-obj-experience"
            - "runtime.md#rt-rte-policy-update"
            - "runtime.md#rt-cmp-agent-policy"
            - "runtime.md#rt-bap-trained-policy"
          note: "Collected multi-step experience produces parameter updates that govern later training decisions; actual execution, causal benefit and production loading remain unestablished."
        -
          scope: "Initial backbone provenance and alternative serving/checkpoint updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-agent-policy"
            - "runtime.md#rt-bap-trained-policy"
            - "memory.md#mem-obj-experience"
            - "runtime.md#rt-rte-policy-update"
          note: "The supplied model identity and update route do not establish the initial training inputs or separate deployment replacement mechanism. Provider opacity warrants neither yes nor no for these alternatives."
      records:
        - "memory.md#mem-obj-content"
        - "memory.md#mem-rte-store-maintenance"
        - "memory.md#mem-rte-requested-retrieval"
        - "memory.md#mem-obj-summary"
        - "runtime.md#rt-rte-context-summary"
        - "memory.md#mem-bap-retained-context"
        - "memory.md#mem-obj-experience"
        - "runtime.md#rt-rte-policy-update"
        - "runtime.md#rt-cmp-agent-policy"
        - "runtime.md#rt-bap-trained-policy"
      note: "Positive qualifying writes are conversational store extraction, continuation summarization and trajectory-fed parameter optimization, all design claims. Original context provenance and checkpoint/provider alternatives remain incompletely assessed; no system-wide no is warranted."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Conversation-fed LTM content admission"
          assessment: "partial"
          findings:
            -
              value: "session-logs"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-content"
                - "memory.md#mem-rte-store-maintenance"
                - "memory.md#mem-rte-requested-retrieval"
              note: "Conversational information and user preferences presented during the episode feed automatic storage for later retrieval."
          records:
            - "memory.md#mem-obj-content"
            - "memory.md#mem-rte-store-maintenance"
            - "memory.md#mem-rte-requested-retrieval"
          note: "Illustrative preferences and conversation-derived content establish recorded interaction as one source. Supporting context and synthetic inputs have unresolved original provenance; not all imported knowledge is a session log."
        -
          scope: "Conversation summary production"
          assessment: "partial"
          findings:
            -
              value: "session-logs"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-summary"
                - "runtime.md#rt-rte-context-summary"
              note: "Selected conversational turns supply the summarizer."
            -
              value: "tool-traces"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-summary"
                - "runtime.md#rt-rte-context-summary"
              note: "The annotated input chain includes tool-related conversation; the round schema includes tool messages. This does not assert that every selected span contains a tool result."
          records:
            - "memory.md#mem-obj-summary"
            - "runtime.md#rt-rte-context-summary"
            - "memory.md#mem-bap-retained-context"
            - "runtime.md#rt-rte-task-rollout"
            - "epistemic.md#epi-obj-context-content"
          note: "The memory annotation supports session-log and tool-trace inputs, but the selected context also includes driver-supplied supporting information, synthetic distractors, retrieved content and earlier summaries. The records do not resolve every included input's original provenance. Conversational wrapping does not classify those origins; complete source enumeration for this summary write remains prevented."
        -
          scope: "GRPO training update from recorded stage experience"
          assessment: "partial"
          findings:
            -
              value: "trajectories"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-experience"
                - "runtime.md#rt-rte-policy-update"
              note: "Stage trajectories and terminal outcomes are normalized as rollout-group experience before gradient updates."
            -
              value: "session-logs"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-experience"
                - "runtime.md#rt-rte-policy-update"
              note: "Recorded conversational state and policy responses are included in collected experience."
            -
              value: "tool-traces"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-experience"
                - "runtime.md#rt-rte-policy-update"
              note: "Generated memory calls are recorded as policy actions in the stage experience consumed by optimization; complete executor-result logging is unresolved."
          records:
            - "memory.md#mem-obj-experience"
            - "runtime.md#rt-rte-policy-update"
          note: "Linked states, actions and outcomes establish multi-step experience. States and actions contain conversation and generated calls, but raw tool-result inclusion and upstream data/synthetic provenance are not fully specified."
        -
          scope: "Initial backbone and uninspected checkpoint/provider update provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-agent-policy"
            - "runtime.md#rt-bap-trained-policy"
            - "memory.md#mem-obj-experience"
            - "runtime.md#rt-rte-policy-update"
          note: "No original trace inputs are established for these alternative parameter origins. Known GRPO trajectories do not classify an opaque initial model training route."
      records:
        - "memory.md#mem-obj-content"
        - "memory.md#mem-rte-store-maintenance"
        - "memory.md#mem-rte-requested-retrieval"
        - "memory.md#mem-obj-summary"
        - "runtime.md#rt-rte-context-summary"
        - "memory.md#mem-bap-retained-context"
        - "memory.md#mem-obj-experience"
        - "runtime.md#rt-rte-policy-update"
        - "runtime.md#rt-cmp-agent-policy"
        - "runtime.md#rt-bap-trained-policy"
        - "runtime.md#rt-rte-task-rollout"
        - "epistemic.md#epi-obj-context-content"
      note: "Each qualifying write retains its original source-content distinction. Conversation and tool-related interaction feed the summary, whose included driver-data, synthetic-input and prior-memory origins remain unresolved locally; linked stage experience feeds GRPO. Mixed driver data, synthetic inputs and uninspected model/checkpoint provenance prevent a complete system inventory. No event-stream origin is established by stage bookkeeping alone."
---

# AgeMem memory profile

## Comparison rationale

This profile classifies the accepted documentary records. Every positive has
`claimed` basis: pseudocode, formulas, prompts and attributed experiments do
not establish executable wiring, inspectable operation or causal support.
Coverage assessment is separate. A named mechanism can be completely classified
at design level while its execution remains uninspected.

The three identity supersessions concern the content object, store-maintenance
route and explicit retrieval route. Their canonical citations here are
[MEM-OBJ-content](memory.md#mem-obj-content),
[MEM-RTE-store-maintenance](memory.md#mem-rte-store-maintenance) and
[MEM-RTE-requested-retrieval](memory.md#mem-rte-requested-retrieval).
They change citation identity, not evidence strength or acceptance. The active
context container remains distinct from its summary part; the embedding remains
distinct from the encoder; experience remains distinct from updated weights.
No unresolved inter-report conflict or value-changing supersession was supplied.

An external store and an active message list do not identify a storage backend.
The only positive substrate classification is model weights, at the update's
retained result rather than its unspecified checkpoint files. Dense embeddings
establish parametric form, not vector storage. These distinctions keep unknown
physical persistence beside the relevant objects
([MEM-OBJ-embedding](memory.md#mem-obj-embedding),
[MEM-OBJ-summary](memory.md#mem-obj-summary),
[MEM-OBJ-experience](memory.md#mem-obj-experience),
[RT-CMP-agent-policy](runtime.md#rt-cmp-agent-policy)).

The knowledge path is retained prose to later policy context. The learning path
is experience to optimizer, and the downstream parameter path selects later
actions. Ranking belongs to the retained embeddings or message text consumed by
similarity selectors; routing belongs to search/target metadata and the policy's
operation selection. Static prompt instructions and schema validation requests
are outside accumulated memory. None of these paths establishes epistemic
endorsement or human approval
([MEM-BAP-retained-context](memory.md#mem-bap-retained-context),
[MEM-OBJ-access-metadata](memory.md#mem-obj-access-metadata),
[RT-RTE-policy-update](runtime.md#rt-rte-policy-update)).

Summary's declared compression supports consolidation even though output
fidelity is not demonstrated. Arbitrary generated Add/Update strings have no
established semantic relationship to their inputs; their indeterminacy is not
permission to assert synthesis or deduplication. Delete, Filter and reset forget
material, but no history-retaining withdrawal route establishes invalidation.
The classification therefore preserves positive transformations without turning
maintenance rewards into evidence of correct repair
([RT-RTE-context-summary](runtime.md#rt-rte-context-summary),
[RT-RTE-context-filter](runtime.md#rt-rte-context-filter),
[EPI-RTE-language-content](epistemic.md#epi-rte-language-content),
[MEM-RTE-store-maintenance](memory.md#mem-rte-store-maintenance)).

The explicit retrieval return is pull. Stage 1 pre-action retrieval is push,
with sampled message, cosine selector and selected stored entries named together.
Context carryover and training consumption are separate push operations; they
are not additional pushes inside a requested retrieval return. Identifier-based
mutation targeting does not establish identifier-based delivery. Unknown
whole-store serialization and deployment loading remain unresolved units, so a
known pull route cannot make the signal axis inapplicable
([MEM-RTE-requested-retrieval](memory.md#mem-rte-requested-retrieval),
[RT-RTE-stage-retrieval](runtime.md#rt-rte-stage-retrieval),
[RT-RTE-task-rollout](runtime.md#rt-rte-task-rollout)).

Trace learning here means an automatic trace-fed write with a retained
behavior-shaping result and later consumer, not demonstrated capacity gain or
exercised self-improvement. Summary meets this criterion within an episode;
conversation-fed storage and GRPO supply other positive paths. The summary
write's trace-source coverage is partial: session-log and tool-trace positives
do not resolve the original provenance of supporting information, synthetic
distractors, retrieved content or earlier summaries included in selected context
([RT-RTE-task-rollout](runtime.md#rt-rte-task-rollout),
[EPI-OBJ-context-content](epistemic.md#epi-obj-context-content)). Tool requests
recorded as actions support tool-trace origin, while linked states/actions/outcomes
support trajectory origin. The records do not establish complete raw tool-result
logging, static-input provenance or initial backbone training provenance. No
bounded absence record licenses a system-wide negative
([MEM-OBJ-experience](memory.md#mem-obj-experience),
[RT-RTE-context-summary](runtime.md#rt-rte-context-summary),
[RT-RTE-policy-update](runtime.md#rt-rte-policy-update),
[MEM-OBJ-content](memory.md#mem-obj-content)).

Source-read log: none. This classification uses only the supplied accepted
records and their annotations; no ambiguity required opening the frozen capture.
