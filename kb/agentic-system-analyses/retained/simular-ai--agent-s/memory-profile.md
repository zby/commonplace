---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Agent S memory comparison across historical experience/caches, ACI retained returns and offline rollout selection, with opaque initialization and provider state retained."
run-id: "AAS-2026-10-16-agent-s-db6fee212353-01"
source-identity: "https://github.com/simular-ai/Agent-S"
reviewed-boundary: "15776a8dc659658b1963816ea006f7af1978e595"
memory-comparison:
  version: 2
  scope: "Included: S1/S2 persistent task/subtask summaries, query/search caches and embedding access metadata; ACI notes across generations; S3 retained coding summaries/action history; offline rollout evidence, derived captions and saved comparison/resume state; unresolved initial archive/local content and provider-side retained-state alternatives. Excluded: static shipped procedural instructions, ordinary turn/reflection accumulation, eviction without a retained replacement, external work products, and provider weights as use-updated memory absent a recorded update route."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Historical narrative, episodic, query and search content; embedding access cache"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-narrative-memory"
                - "memory.md#mem-obj-episodic-memory"
                - "memory.md#mem-obj-formulate-query"
                - "memory.md#mem-obj-rag-knowledge"
                - "memory.md#mem-obj-embeddings"
              note: "The records identify local JSON content and embeddings.pkl, not a database or remote vector index."
          records:
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
            - "memory.md#mem-obj-formulate-query"
            - "memory.md#mem-obj-rag-knowledge"
            - "memory.md#mem-obj-embeddings"
          note: "All five named operative stores are local filesystem JSON or pickle; dense encoding is not a vector-service substrate."
        -
          scope: "ACI notes and cached code-agent result"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-code-result"
              note: "The notes list and last_code_agent_result live in ACI process memory."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-code-result"
          note: "These retained objects have instance-lifetime RAM storage, including one-shot coding return delivery."
        -
          scope: "Offline raw rollout evidence, captions and persisted comparative result"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traj"
                - "memory.md#mem-obj-fact-captions"
                - "memory.md#mem-obj-judge-results"
              note: "JSONL, PNG, text score and judgment JSON are retained in rollout/result directories."
          records:
            - "memory.md#mem-obj-traj"
            - "memory.md#mem-obj-fact-captions"
            - "memory.md#mem-obj-judge-results"
          note: "Files survive producer invocations and have named later consumers."
        -
          scope: "Uncaptured initial bundle payload beyond the named loaded content and vector stores"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-kb-bootstrap"
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
            - "memory.md#mem-obj-embeddings"
          note: "The downloader and named local destinations are known; archive bytes and any additional operative payload inventory are not. Extraction alone cannot classify every retained part."
        -
          scope: "Included provider-side retained state behind generation, grounding and embedding endpoints"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-lmm-agent"
            - "runtime.md#rt-cmp-grounding-model"
            - "runtime.md#rt-cmp-embedding-engine"
          note: "The accepted component records establish external calls, not the existence, contents or mechanisms of use-accumulated server state. No storage_substrate value for that state follows from client configuration or model weights."
      records:
        - "memory.md#mem-obj-narrative-memory"
        - "memory.md#mem-obj-episodic-memory"
        - "memory.md#mem-obj-formulate-query"
        - "memory.md#mem-obj-rag-knowledge"
        - "memory.md#mem-obj-embeddings"
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-code-result"
        - "memory.md#mem-obj-traj"
        - "memory.md#mem-obj-fact-captions"
        - "memory.md#mem-obj-judge-results"
        - "runtime.md#rt-rte-kb-bootstrap"
        - "runtime.md#rt-cmp-lmm-agent"
        - "runtime.md#rt-cmp-grounding-model"
        - "runtime.md#rt-cmp-embedding-engine"
      note: "Named local content, access metadata and offline evidence have classified substrates. Static source policy and external model weights are not accumulated-memory substrates. Provider-side retained state remains unresolved; the positive local witnesses do not close that alternative."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Historical summary and query/search value prose at manager, fusion and worker consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-narrative-memory"
                - "memory.md#mem-obj-episodic-memory"
                - "memory.md#mem-obj-formulate-query"
                - "memory.md#mem-obj-rag-knowledge"
                - "memory.md#mem-rte-experience-retrieval"
                - "memory.md#mem-rte-query-cache"
              note: "Values supply task descriptions, recipes, queries or retrieved prose to interpreting models."
          records:
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
            - "memory.md#mem-obj-formulate-query"
            - "memory.md#mem-obj-rag-knowledge"
            - "memory.md#mem-rte-experience-retrieval"
            - "memory.md#mem-rte-query-cache"
          note: "Text is interpreted by models; episodic rendered actions are advice here, not direct replay."
        -
          scope: "Historical JSON keys and embedding-cache key lookup"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-narrative-memory"
                - "memory.md#mem-obj-episodic-memory"
                - "memory.md#mem-obj-formulate-query"
                - "memory.md#mem-obj-rag-knowledge"
                - "memory.md#mem-obj-embeddings"
                - "memory.md#mem-rte-experience-retrieval"
                - "memory.md#mem-rte-query-cache"
              note: "String identities determine cache hits, missing-key admission and candidate lookup."
          records:
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
            - "memory.md#mem-obj-formulate-query"
            - "memory.md#mem-obj-rag-knowledge"
            - "memory.md#mem-obj-embeddings"
            - "memory.md#mem-rte-experience-retrieval"
            - "memory.md#mem-rte-query-cache"
          note: "Exact keys and lookup rules are distinct from the content values."
        -
          scope: "Dense embedding cache at cosine-similarity consumer"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-embeddings"
                - "memory.md#mem-rte-experience-retrieval"
              note: "Distributed numerical vectors rank keys by cosine similarity; they are not installed weight updates."
          records:
            - "memory.md#mem-obj-embeddings"
            - "memory.md#mem-rte-experience-retrieval"
          note: "Dense numerical representation is distinguished from its file storage and symbolic dictionary keys."
        -
          scope: "Notes prose and code summary/thoughts at model consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-code-result"
                - "memory.md#mem-rte-notes-delivery"
              note: "Notes and coding summaries become advisory user-message text."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-code-result"
            - "memory.md#mem-rte-notes-delivery"
          note: "The outer worker interprets note and summary text. Stored thoughts are not separately rendered to it."
        -
          scope: "Code-result dictionary, step fields and recorded action syntax"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-code-result"
                - "runtime.md#rt-rte-code-delegation"
              note: "Structured budget/completion fields and step/action records have fixed parsing and rendering rules."
          records:
            - "memory.md#mem-obj-code-result"
            - "runtime.md#rt-rte-code-delegation"
          note: "Localized fields govern return handling; recorded code remains evidence rather than automatically replayed outer-worker actions."
        -
          scope: "Offline plans, reflections, caption answers/thoughts and judgment prose"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traj"
                - "memory.md#mem-obj-fact-captions"
                - "memory.md#mem-obj-judge-results"
              note: "Model interpretations and rationale are retained as prose; only specified portions reach later models."
          records:
            - "memory.md#mem-obj-traj"
            - "memory.md#mem-obj-fact-captions"
            - "memory.md#mem-obj-judge-results"
          note: "Readable content is distinct from score/index and task-key consumers."
        -
          scope: "Offline trajectory metadata, action strings, raster observations and choice/access fields"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traj"
                - "memory.md#mem-obj-judge-results"
              note: "JSON fields, scores, raster image encoding and selected-directory identifiers are mechanically decoded before visual/model interpretation."
          records:
            - "memory.md#mem-obj-traj"
            - "memory.md#mem-obj-judge-results"
          note: "Raster bytes encode localized pixel observations, not learned distributed parameters; task IDs, score fields and directories have fixed consumers."
        -
          scope: "Initial bundle content and vector payload provenance-dependent alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-kb-bootstrap"
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
            - "memory.md#mem-obj-embeddings"
          note: "Named loaded store encodings are described, but unseen archive payloads cannot be classified from the readable summary of the downloader."
        -
          scope: "Included provider-side retained state behind generation, grounding and embedding endpoints"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-lmm-agent"
            - "runtime.md#rt-cmp-grounding-model"
            - "runtime.md#rt-cmp-embedding-engine"
          note: "The accepted component records establish external calls, not the existence, contents or mechanisms of use-accumulated server state. No representational_form value for that state follows from client configuration or model weights."
      records:
        - "memory.md#mem-obj-narrative-memory"
        - "memory.md#mem-obj-episodic-memory"
        - "memory.md#mem-obj-formulate-query"
        - "memory.md#mem-obj-rag-knowledge"
        - "memory.md#mem-rte-experience-retrieval"
        - "memory.md#mem-rte-query-cache"
        - "memory.md#mem-obj-embeddings"
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-code-result"
        - "memory.md#mem-rte-notes-delivery"
        - "runtime.md#rt-rte-code-delegation"
        - "memory.md#mem-obj-traj"
        - "memory.md#mem-obj-fact-captions"
        - "memory.md#mem-obj-judge-results"
        - "runtime.md#rt-rte-kb-bootstrap"
        - "runtime.md#rt-cmp-lmm-agent"
        - "runtime.md#rt-cmp-grounding-model"
        - "runtime.md#rt-cmp-embedding-engine"
      note: "Operative prose, symbolic access/control parts and dense numerical vectors are split by consumer; file formats alone do not make prose symbolic. Provider-side retained state remains unresolved; the positive local witnesses do not close that alternative."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Subsequent S1/S2 CLI task/subtask summaries"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-historical-experience"
                - "memory.md#mem-rte-s1-experience"
                - "memory.md#mem-obj-narrative-memory"
                - "memory.md#mem-obj-episodic-memory"
              note: "Models derive reusable summaries from accumulated task, plan and reflection text."
          records:
            - "runtime.md#rt-rte-historical-experience"
            - "memory.md#mem-rte-s1-experience"
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
          note: "Known later extraction does not resolve the origin of pre-existing values."
        -
          scope: "Alternative S2 KnowledgeBase summary generation"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-knowledge-save"
              note: "Supplied trajectory strings can feed missing-key summaries through the exposed save/finalize methods."
          records:
            - "memory.md#mem-rte-knowledge-save"
          note: "This is a separate callable capability, not a second deployed CLI lifecycle."
        -
          scope: "Bootstrap admission of externally supplied initial stores"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-kb-bootstrap"
              note: "Caller-selected release archives are admitted by HTTP/ZIP handling."
          records:
            - "runtime.md#rt-rte-kb-bootstrap"
          note: "Import into this installation is known even though authorship and prior derivation remain unknown."
        -
          scope: "Original authorship/derivation of existing local or release-provided summaries and vectors"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
            - "memory.md#mem-obj-embeddings"
            - "runtime.md#rt-rte-kb-bootstrap"
          note: "Initial material could predate this use; no per-entry or per-vector provenance determines authored versus trace-derived or other origins."
        -
          scope: "Query-cache miss composition and LLM search response branch"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-formulate-query"
                - "memory.md#mem-obj-rag-knowledge"
                - "memory.md#mem-rte-query-cache"
              note: "A model formulates a query or composes a search response on cache miss."
          records:
            - "memory.md#mem-obj-formulate-query"
            - "memory.md#mem-obj-rag-knowledge"
            - "memory.md#mem-rte-query-cache"
          note: "These model compositions are distinct from the separately opaque external search derivation."
        -
          scope: "External Perplexica search-response admission"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-rag-knowledge"
                - "memory.md#mem-rte-query-cache"
              note: "Returned external search text is cached locally."
          records:
            - "memory.md#mem-obj-rag-knowledge"
            - "memory.md#mem-rte-query-cache"
          note: "Import is established at the cache boundary, not source trust or internal derivation."
        -
          scope: "Internal derivation and source mixture of external search response"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-rag-knowledge"
            - "memory.md#mem-rte-query-cache"
          note: "The accepted record leaves external source selection/provenance opaque; import does not establish its original lineage."
        -
          scope: "Subsequent embedding-cache miss generation"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-embeddings"
              note: "External encoders transform text keys into cached dense vectors."
          records:
            - "memory.md#mem-obj-embeddings"
          note: "Encoder output is a compiled access representation rather than evidence of training."
        -
          scope: "Model-supplied ACI note strings"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-rte-notes-delivery"
              note: "Foreground model choices supply the strings admitted to the notes list."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-rte-notes-delivery"
          note: "The model supplies text through an action, but no actual note establishes whether it copies a trace or invents a statement."
        -
          scope: "Coding return summary and recorded action/thought history"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-code-result"
                - "runtime.md#rt-rte-code-delegation"
              note: "Action/thought records feed the summary and later worker display."
          records:
            - "memory.md#mem-obj-code-result"
            - "runtime.md#rt-rte-code-delegation"
          note: "Reduced model work history, not complete controller-output provenance, feeds this return."
        -
          scope: "Offline raw rollout record"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traj"
              note: "Runtime activity is serialized into trajectory and screenshot evidence."
          records:
            - "memory.md#mem-obj-traj"
          note: "The driver records actions, plans, observations and external feedback rather than curating a lesson."
        -
          scope: "Offline captions and retained comparative judgment"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact-captions"
                - "memory.md#mem-obj-judge-results"
                - "runtime.md#rt-rte-rollout-selection"
              note: "Narration consumes screenshot/action traces; comparison consumes derived captions and endpoint evidence."
          records:
            - "memory.md#mem-obj-fact-captions"
            - "memory.md#mem-obj-judge-results"
            - "runtime.md#rt-rte-rollout-selection"
          note: "Both derive from recorded rollout evidence, with different transformations and consumers."
        -
          scope: "Included provider-side retained state behind generation, grounding and embedding endpoints"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-lmm-agent"
            - "runtime.md#rt-cmp-grounding-model"
            - "runtime.md#rt-cmp-embedding-engine"
          note: "The accepted component records establish external calls, not the existence, contents or mechanisms of use-accumulated server state. No lineage value for that state follows from client configuration or model weights."
      records:
        - "runtime.md#rt-rte-historical-experience"
        - "memory.md#mem-rte-s1-experience"
        - "memory.md#mem-obj-narrative-memory"
        - "memory.md#mem-obj-episodic-memory"
        - "memory.md#mem-rte-knowledge-save"
        - "runtime.md#rt-rte-kb-bootstrap"
        - "memory.md#mem-obj-embeddings"
        - "memory.md#mem-obj-formulate-query"
        - "memory.md#mem-obj-rag-knowledge"
        - "memory.md#mem-rte-query-cache"
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-rte-notes-delivery"
        - "memory.md#mem-obj-code-result"
        - "runtime.md#rt-rte-code-delegation"
        - "memory.md#mem-obj-traj"
        - "memory.md#mem-obj-fact-captions"
        - "memory.md#mem-obj-judge-results"
        - "runtime.md#rt-rte-rollout-selection"
        - "runtime.md#rt-cmp-lmm-agent"
        - "runtime.md#rt-cmp-grounding-model"
        - "runtime.md#rt-cmp-embedding-engine"
      note: "Known imports, model composition, compilation and trace extraction coexist. Initial provenance and opaque response derivation remain local unknowns rather than being inferred from subsequent writes. Provider-side retained state remains unresolved; the positive local witnesses do not close that alternative."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Narrative and episodic summaries at historical manager/worker consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-narrative-memory"
                - "memory.md#mem-obj-episodic-memory"
                - "memory.md#mem-rte-experience-retrieval"
              note: "Retrieved plans, recipes and failure explanations supply advice for a later task."
          records:
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
            - "memory.md#mem-rte-experience-retrieval"
          note: "Optional reference advice in a system prompt is knowledge, not a standing instruction solely because of its channel."
        -
          scope: "Retained raw textual historical trajectories at summary-update consumers"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-historical-experience"
                - "memory.md#mem-rte-s1-experience"
                - "memory.md#mem-obj-narrative-memory"
                - "memory.md#mem-obj-episodic-memory"
              note: "Summary models consume accumulated task activity to produce persisted future guidance."
          records:
            - "runtime.md#rt-rte-historical-experience"
            - "memory.md#mem-rte-s1-experience"
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
          note: "Experience feeds durable behavior-shaping summaries; this force is separate from downstream advice."
        -
          scope: "Embedding vectors and associated entry keys at similarity selection"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-embeddings"
                - "memory.md#mem-rte-experience-retrieval"
              note: "Cosine similarity over cached key vectors orders candidate summaries."
          records:
            - "memory.md#mem-obj-embeddings"
            - "memory.md#mem-rte-experience-retrieval"
          note: "Fixed scoring code still gives retained access material ranking influence."
        -
          scope: "Query values at subsequent search/task-identity consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-formulate-query"
                - "memory.md#mem-rte-query-cache"
              note: "Cached query text steers the next search input and task/subtask search identity."
          records:
            - "memory.md#mem-obj-formulate-query"
            - "memory.md#mem-rte-query-cache"
          note: "A reused query chooses search input and retained task identity rather than granting factual truth."
        -
          scope: "Cached search content at fusion and planning consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-rag-knowledge"
                - "memory.md#mem-rte-query-cache"
              note: "Search/model response prose supplies context for fused planning advice."
          records:
            - "memory.md#mem-obj-rag-knowledge"
            - "memory.md#mem-rte-query-cache"
          note: "Model fusion is advisory and may omit content."
        -
          scope: "Notes and reduced code return at outer-worker consumer"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-code-result"
                - "memory.md#mem-rte-notes-delivery"
                - "runtime.md#rt-bap-code-return"
              note: "The worker receives notes, summary and formatted actions as evidence/context."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-code-result"
            - "memory.md#mem-rte-notes-delivery"
            - "runtime.md#rt-bap-code-return"
          note: "Delivery can shape decisions but no enforced compliance or accepted truth follows."
        -
          scope: "Recorded coding action/thought history at summary producer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-code-result"
                - "runtime.md#rt-rte-code-delegation"
              note: "Reduced coding experience feeds an automatically retained continuation summary."
          records:
            - "memory.md#mem-obj-code-result"
            - "runtime.md#rt-rte-code-delegation"
          note: "The update consumer differs from the outer worker and omits direct controller outputs."
        -
          scope: "Raw offline rollout evidence at caption production"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traj"
                - "memory.md#mem-obj-fact-captions"
                - "runtime.md#rt-rte-rollout-selection"
              note: "Screenshots and recorded actions produce persisted caption answers for a later judge."
          records:
            - "memory.md#mem-obj-traj"
            - "memory.md#mem-obj-fact-captions"
            - "runtime.md#rt-rte-rollout-selection"
          note: "Trace evidence feeds retained material shaping later comparison, not GUI-worker weights."
        -
          scope: "Caption answers and available endpoint images at comparative judge"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact-captions"
                - "memory.md#mem-obj-traj"
                - "runtime.md#rt-rte-rollout-selection"
              note: "The judge receives descriptions and endpoint images as comparison evidence."
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact-captions"
                - "memory.md#mem-obj-traj"
                - "runtime.md#rt-rte-rollout-selection"
              note: "Their content informs relative task-fit priority among completed rollouts."
          records:
            - "memory.md#mem-obj-fact-captions"
            - "memory.md#mem-obj-traj"
            - "runtime.md#rt-rte-rollout-selection"
          note: "Evidence and relative-priority influence coexist at this consumer."
        -
          scope: "Saved task keys and selected directory at resume/scoring consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-judge-results"
              note: "Selected directories choose which retained rollout score is read."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-judge-results"
              note: "Task-key presence prevents rejudging an already recorded task."
          records:
            - "memory.md#mem-obj-judge-results"
          note: "Only these mechanical fields, not stored rationale, establish these effects."
        -
          scope: "Unseen initial payload authority beyond named consumer paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-kb-bootstrap"
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
            - "memory.md#mem-obj-embeddings"
          note: "The known downstream consumers classify named loaded parts, not every unseen release entry or alternative payload."
        -
          scope: "Included provider-side retained state behind generation, grounding and embedding endpoints"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-lmm-agent"
            - "runtime.md#rt-cmp-grounding-model"
            - "runtime.md#rt-cmp-embedding-engine"
          note: "The accepted component records establish external calls, not the existence, contents or mechanisms of use-accumulated server state. No behavioral_authority value for that state follows from client configuration or model weights."
      records:
        - "memory.md#mem-obj-narrative-memory"
        - "memory.md#mem-obj-episodic-memory"
        - "memory.md#mem-rte-experience-retrieval"
        - "runtime.md#rt-rte-historical-experience"
        - "memory.md#mem-rte-s1-experience"
        - "memory.md#mem-obj-embeddings"
        - "memory.md#mem-obj-formulate-query"
        - "memory.md#mem-rte-query-cache"
        - "memory.md#mem-obj-rag-knowledge"
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-code-result"
        - "memory.md#mem-rte-notes-delivery"
        - "runtime.md#rt-bap-code-return"
        - "runtime.md#rt-rte-code-delegation"
        - "memory.md#mem-obj-traj"
        - "memory.md#mem-obj-fact-captions"
        - "runtime.md#rt-rte-rollout-selection"
        - "memory.md#mem-obj-judge-results"
        - "runtime.md#rt-rte-kb-bootstrap"
        - "runtime.md#rt-cmp-lmm-agent"
        - "runtime.md#rt-cmp-grounding-model"
        - "runtime.md#rt-cmp-embedding-engine"
      note: "Authority is classified at actual update, advice, ranking and mechanical consumers. Static procedural policy, format checks and external work-product effects are not attributed to accumulated memory. Provider-side retained state remains unresolved; the positive local witnesses do not close that alternative."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "S1/S2 CLI summary admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-historical-experience"
                - "memory.md#mem-rte-s1-experience"
              note: "Software invokes a summarizer and admits a new-key result without individual human approval."
          records:
            - "runtime.md#rt-rte-historical-experience"
            - "memory.md#mem-rte-s1-experience"
          note: "Human task entry is not a per-summary decision."
        -
          scope: "Exposed S2 save/finalize admission mechanism"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-knowledge-save"
              note: "If invoked and enabled, software admits the generated summary on a missing key."
          records:
            - "memory.md#mem-rte-knowledge-save"
          note: "Generic caller identity does not establish human content approval; the implemented model/key admission itself is automatic."
        -
          scope: "Query/search and embedding cache miss admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-query-cache"
                - "memory.md#mem-obj-embeddings"
              note: "Miss rules admit generated response or encoder output without per-item approval."
          records:
            - "memory.md#mem-rte-query-cache"
            - "memory.md#mem-obj-embeddings"
          note: "Writing to disk is distinguished from the model/software content admission."
        -
          scope: "Notes append and coding-result retention"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-notes-delivery"
                - "memory.md#mem-obj-code-result"
                - "runtime.md#rt-rte-code-delegation"
              note: "Model/software appends notes and caches a reduced return for later delivery."
          records:
            - "memory.md#mem-rte-notes-delivery"
            - "memory.md#mem-obj-code-result"
            - "runtime.md#rt-rte-code-delegation"
          note: "Coding capability opt-in is not approval of each retained string or summary."
        -
          scope: "Driver evidence, narrator captions and comparative choice persistence"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traj"
                - "memory.md#mem-obj-fact-captions"
                - "memory.md#mem-obj-judge-results"
                - "runtime.md#rt-rte-rollout-selection"
              note: "Driver serialization, successful caption handling and parsed judge return govern admission."
          records:
            - "memory.md#mem-obj-traj"
            - "memory.md#mem-obj-fact-captions"
            - "memory.md#mem-obj-judge-results"
            - "runtime.md#rt-rte-rollout-selection"
          note: "Workflow launch does not make each recorded/derived item manual."
        -
          scope: "Release archive installation"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-kb-bootstrap"
              note: "HTTP success and ZIP extraction admit archive contents by software rules."
          records:
            - "runtime.md#rt-rte-kb-bootstrap"
          note: "Asset selection does not establish per-entry review."
        -
          scope: "Initial content creation and prior local-file/release review"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-kb-bootstrap"
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
            - "memory.md#mem-obj-embeddings"
          note: "No explicit human supplying/editing/approval decision for retained entries is recorded. This prevents a manual finding without weakening later automatic transformations."
        -
          scope: "Included provider-side retained state behind generation, grounding and embedding endpoints"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-lmm-agent"
            - "runtime.md#rt-cmp-grounding-model"
            - "runtime.md#rt-cmp-embedding-engine"
          note: "The accepted component records establish external calls, not the existence, contents or mechanisms of use-accumulated server state. No write_agency value for that state follows from client configuration or model weights."
      records:
        - "runtime.md#rt-rte-historical-experience"
        - "memory.md#mem-rte-s1-experience"
        - "memory.md#mem-rte-knowledge-save"
        - "memory.md#mem-rte-query-cache"
        - "memory.md#mem-obj-embeddings"
        - "memory.md#mem-rte-notes-delivery"
        - "memory.md#mem-obj-code-result"
        - "runtime.md#rt-rte-code-delegation"
        - "memory.md#mem-obj-traj"
        - "memory.md#mem-obj-fact-captions"
        - "memory.md#mem-obj-judge-results"
        - "runtime.md#rt-rte-rollout-selection"
        - "runtime.md#rt-rte-kb-bootstrap"
        - "memory.md#mem-obj-narrative-memory"
        - "memory.md#mem-obj-episodic-memory"
        - "runtime.md#rt-cmp-lmm-agent"
        - "runtime.md#rt-cmp-grounding-model"
        - "runtime.md#rt-cmp-embedding-engine"
      note: "All established local admission mechanisms are automatic, with afforded alternative APIs kept separate from wired callers. Initial human control remains unresolved. Provider-side retained state remains unresolved; the positive local witnesses do not close that alternative."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Historical task/subtask trajectory summarization into persistent guidance"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-historical-experience"
                - "memory.md#mem-rte-s1-experience"
                - "memory.md#mem-obj-narrative-memory"
                - "memory.md#mem-obj-episodic-memory"
              note: "Summary generation selects/compresses existing task activity into reusable reduced guidance."
          records:
            - "runtime.md#rt-rte-historical-experience"
            - "memory.md#mem-rte-s1-experience"
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
          note: "The implemented transformation reduces accumulated activity to plans/recipes; correctness requests are not proof of faithful output."
        -
          scope: "Alternative S2 trajectory-summary save methods"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-knowledge-save"
              note: "Exposed summarizers reduce supplied task/subtask trajectories."
          records:
            - "memory.md#mem-rte-knowledge-save"
          note: "The transformation capability is inspectable; shipped lifecycle deployment is not established."
        -
          scope: "Coding history reduction into retained continuation summary"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-code-result"
                - "runtime.md#rt-rte-code-delegation"
              note: "A separate model reduces action/thought history into a short summary for a later worker invocation."
          records:
            - "memory.md#mem-obj-code-result"
            - "runtime.md#rt-rte-code-delegation"
          note: "This is lossy summarization, not preservation of omitted controller results."
        -
          scope: "Offline screenshot/action caption derivation"
          assessment: "partial"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traj"
                - "memory.md#mem-obj-fact-captions"
                - "runtime.md#rt-rte-rollout-selection"
              note: "The implemented narration pipeline selects visible before/after changes into retained descriptions."
          records:
            - "memory.md#mem-obj-traj"
            - "memory.md#mem-obj-fact-captions"
            - "runtime.md#rt-rte-rollout-selection"
          note: "Captioning reduces retained evidence, but actual output semantics and possible added claims are not resolved."
        -
          scope: "Other semantic operations over caches, vectors, notes and saved judgments"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-query-cache"
            - "memory.md#mem-obj-embeddings"
            - "memory.md#mem-rte-notes-delivery"
            - "memory.md#mem-obj-judge-results"
          note: "Append, cache filling, key preservation, filename skips and resume guards do not establish controlled curation operations. The records supply no bounded absence warrant for every possible transformation."
        -
          scope: "Initial archive preparation and opaque source curation"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-kb-bootstrap"
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
            - "memory.md#mem-obj-embeddings"
            - "memory.md#mem-obj-rag-knowledge"
          note: "Pre-installation transformations and external search processing are not captured; neither synthesis nor deduplication can be inferred from labels."
        -
          scope: "Included provider-side retained state behind generation, grounding and embedding endpoints"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-lmm-agent"
            - "runtime.md#rt-cmp-grounding-model"
            - "runtime.md#rt-cmp-embedding-engine"
          note: "The accepted component records establish external calls, not the existence, contents or mechanisms of use-accumulated server state. No curation_operations value for that state follows from client configuration or model weights."
      records:
        - "runtime.md#rt-rte-historical-experience"
        - "memory.md#mem-rte-s1-experience"
        - "memory.md#mem-obj-narrative-memory"
        - "memory.md#mem-obj-episodic-memory"
        - "memory.md#mem-rte-knowledge-save"
        - "memory.md#mem-obj-code-result"
        - "runtime.md#rt-rte-code-delegation"
        - "memory.md#mem-obj-traj"
        - "memory.md#mem-obj-fact-captions"
        - "runtime.md#rt-rte-rollout-selection"
        - "memory.md#mem-rte-query-cache"
        - "memory.md#mem-obj-embeddings"
        - "memory.md#mem-rte-notes-delivery"
        - "memory.md#mem-obj-judge-results"
        - "runtime.md#rt-rte-kb-bootstrap"
        - "memory.md#mem-obj-rag-knowledge"
        - "runtime.md#rt-cmp-lmm-agent"
        - "runtime.md#rt-cmp-grounding-model"
        - "runtime.md#rt-cmp-embedding-engine"
      note: "Consolidation witnesses retain their own evidence layers. Requested correct-step extraction does not establish deduplication; unseen semantic novelty does not establish synthesis. Ordinary context eviction is outside retained-memory curation. Provider-side retained state remains unresolved; the positive local witnesses do not close that alternative."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Historical experience requests and their fulfilled returns"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-experience-retrieval"
                - "runtime.md#rt-rte-historical-experience"
                - "memory.md#mem-rte-s1-experience"
              note: "KnowledgeBase returns the selected summary in response to the consumer retrieval request."
          records:
            - "memory.md#mem-rte-experience-retrieval"
            - "runtime.md#rt-rte-historical-experience"
            - "memory.md#mem-rte-s1-experience"
          note: "The first planning/subtask invocation requests retrieval; fulfillment is not counted again as unsolicited delivery."
        -
          scope: "Exact-task query/search cache reuse and vector access"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-query-cache"
                - "memory.md#mem-obj-embeddings"
                - "memory.md#mem-rte-experience-retrieval"
              note: "Lookup and similarity calls return retained parts to their invoking consumers."
          records:
            - "memory.md#mem-rte-query-cache"
            - "memory.md#mem-obj-embeddings"
            - "memory.md#mem-rte-experience-retrieval"
          note: "These reads fulfill requests for retained query/result/access material."
        -
          scope: "Automatic full notes delivery on worker invocation"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-notes-delivery"
              note: "Every worker call receives all ACI notes without a new request for those retained notes."
          records:
            - "memory.md#mem-rte-notes-delivery"
          note: "Independent renderer supply is distinct from the earlier save action."
        -
          scope: "Pending coding return delivery to next worker invocation"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-code-result"
                - "runtime.md#rt-rte-code-delegation"
                - "runtime.md#rt-bap-code-return"
              note: "Worker message construction automatically inserts the pending summary/action history then clears the cached field."
          records:
            - "memory.md#mem-obj-code-result"
            - "runtime.md#rt-rte-code-delegation"
            - "runtime.md#rt-bap-code-return"
          note: "The earlier delegation request is not a retrieval request for the subsequently retained cache."
        -
          scope: "Offline caption/evidence loads and saved-choice resume/scoring reads"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traj"
                - "memory.md#mem-obj-fact-captions"
                - "memory.md#mem-obj-judge-results"
                - "runtime.md#rt-rte-rollout-selection"
              note: "Loader and scoring calls read requested rollout evidence, captions and selected-directory records."
          records:
            - "memory.md#mem-obj-traj"
            - "memory.md#mem-obj-fact-captions"
            - "memory.md#mem-obj-judge-results"
            - "runtime.md#rt-rte-rollout-selection"
          note: "Explicit producer/judge/scoring invocations request recorded material; file delivery is not another push."
        -
          scope: "Initial unseen bundle read alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-kb-bootstrap"
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
            - "memory.md#mem-obj-embeddings"
          note: "Named historical loaders are classified above; unseen archive material does not establish the full alternative consumer inventory."
        -
          scope: "Included provider-side retained state behind generation, grounding and embedding endpoints"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-lmm-agent"
            - "runtime.md#rt-cmp-grounding-model"
            - "runtime.md#rt-cmp-embedding-engine"
          note: "The accepted component records establish external calls, not the existence, contents or mechanisms of use-accumulated server state. No read_back_direction value for that state follows from client configuration or model weights."
      records:
        - "memory.md#mem-rte-experience-retrieval"
        - "runtime.md#rt-rte-historical-experience"
        - "memory.md#mem-rte-s1-experience"
        - "memory.md#mem-rte-query-cache"
        - "memory.md#mem-obj-embeddings"
        - "memory.md#mem-rte-notes-delivery"
        - "memory.md#mem-obj-code-result"
        - "runtime.md#rt-rte-code-delegation"
        - "runtime.md#rt-bap-code-return"
        - "memory.md#mem-obj-traj"
        - "memory.md#mem-obj-fact-captions"
        - "memory.md#mem-obj-judge-results"
        - "runtime.md#rt-rte-rollout-selection"
        - "runtime.md#rt-rte-kb-bootstrap"
        - "memory.md#mem-obj-narrative-memory"
        - "memory.md#mem-obj-episodic-memory"
        - "runtime.md#rt-cmp-lmm-agent"
        - "runtime.md#rt-cmp-grounding-model"
        - "runtime.md#rt-cmp-embedding-engine"
      note: "Requested retrieval and independent automatic context supply coexist; a request-driven return is not relabelled push simply because code selects the returned entry. Provider-side retained state remains unresolved; the positive local witnesses do not close that alternative."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Notes push: every worker invocation, full-list availability selector"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-notes-delivery"
                - "memory.md#mem-obj-notes"
              note: "All available notes are supplied without relevance targeting, identity matching or a size cap."
          records:
            - "memory.md#mem-rte-notes-delivery"
            - "memory.md#mem-obj-notes"
          note: "Trigger is worker message construction; selector input is the current notes list; the selected retained part is the whole list."
        -
          scope: "Coding-result push: next worker invocation, pending-return availability selector"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-code-result"
                - "runtime.md#rt-rte-code-delegation"
              note: "Presence of a pending result controls delivery; task identity is displayed but does not match/select a targeted stored part."
          records:
            - "memory.md#mem-obj-code-result"
            - "runtime.md#rt-rte-code-delegation"
          note: "Trigger is the next worker call; selector input is nonempty cached return; selected parts are summary, completion fields and formatted actions, not all thoughts/outputs."
        -
          scope: "Request-driven historical similarity, exact cache/vector access and offline file loads"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-experience-retrieval"
            - "memory.md#mem-rte-query-cache"
            - "memory.md#mem-obj-embeddings"
            - "memory.md#mem-obj-traj"
            - "memory.md#mem-obj-fact-captions"
            - "memory.md#mem-obj-judge-results"
            - "runtime.md#rt-rte-rollout-selection"
          note: "These are pull operations. Their embeddings, exact keys and filenames are not push-selection signals."
        -
          scope: "Unseen initial-content delivery alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-kb-bootstrap"
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
            - "memory.md#mem-obj-embeddings"
          note: "The named pull routes do not resolve any additional consumer selection hidden in the absent bundle payload."
        -
          scope: "Included provider-side retained state behind generation, grounding and embedding endpoints"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-lmm-agent"
            - "runtime.md#rt-cmp-grounding-model"
            - "runtime.md#rt-cmp-embedding-engine"
          note: "The accepted component records establish external calls, not the existence, contents or mechanisms of use-accumulated server state. No read_back_signal value for that state follows from client configuration or model weights."
      records:
        - "memory.md#mem-rte-notes-delivery"
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-code-result"
        - "runtime.md#rt-rte-code-delegation"
        - "memory.md#mem-rte-experience-retrieval"
        - "memory.md#mem-rte-query-cache"
        - "memory.md#mem-obj-embeddings"
        - "memory.md#mem-obj-traj"
        - "memory.md#mem-obj-fact-captions"
        - "memory.md#mem-obj-judge-results"
        - "runtime.md#rt-rte-rollout-selection"
        - "runtime.md#rt-rte-kb-bootstrap"
        - "memory.md#mem-obj-narrative-memory"
        - "memory.md#mem-obj-episodic-memory"
        - "runtime.md#rt-cmp-lmm-agent"
        - "runtime.md#rt-cmp-grounding-model"
        - "runtime.md#rt-cmp-embedding-engine"
      note: "Coarse availability is the only supported local push signal. Embedding ranking belongs to requested experience retrieval, so it does not establish inferred-embedding on this axis. Provider-side retained state remains unresolved; the positive local witnesses do not close that alternative."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "S1/S2 CLI trajectory-to-summary-to-later-guidance chain"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-historical-experience"
                - "memory.md#mem-rte-s1-experience"
                - "memory.md#mem-obj-narrative-memory"
                - "memory.md#mem-obj-episodic-memory"
                - "memory.md#mem-rte-experience-retrieval"
              note: "Recorded task work feeds persisted summaries eligible for later manager/worker use."
          records:
            - "runtime.md#rt-rte-historical-experience"
            - "memory.md#mem-rte-s1-experience"
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
            - "memory.md#mem-rte-experience-retrieval"
          note: "Automatic trace-fed durable guidance qualifies architecturally; improved capacity is not established."
        -
          scope: "Alternative S2 summary lifecycle and shared-store later-consumer capability"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-knowledge-save"
                - "memory.md#mem-rte-experience-retrieval"
                - "memory.md#mem-obj-narrative-memory"
                - "memory.md#mem-obj-episodic-memory"
              note: "If invoked, trace-derived summaries enter stores with separately wired later consumers."
          records:
            - "memory.md#mem-rte-knowledge-save"
            - "memory.md#mem-rte-experience-retrieval"
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
          note: "The alternate write is afforded, not a demonstrated shipped lifecycle caller."
        -
          scope: "Coding history-to-summary-to-next-worker chain"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-code-result"
                - "runtime.md#rt-rte-code-delegation"
                - "runtime.md#rt-bap-code-return"
              note: "Automatic summary production from recorded coding work yields retained behavior-shaping continuation context."
          records:
            - "memory.md#mem-obj-code-result"
            - "runtime.md#rt-rte-code-delegation"
            - "runtime.md#rt-bap-code-return"
          note: "Within-task retention qualifies; neither cross-session storage nor complete controller feedback is required."
        -
          scope: "Offline rollout-to-caption-to-comparison chain"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traj"
                - "memory.md#mem-obj-fact-captions"
                - "memory.md#mem-obj-judge-results"
                - "runtime.md#rt-rte-rollout-selection"
              note: "Recorded screenshot/action experience automatically yields retained captions that shape later rollout selection."
          records:
            - "memory.md#mem-obj-traj"
            - "memory.md#mem-obj-fact-captions"
            - "memory.md#mem-obj-judge-results"
            - "runtime.md#rt-rte-rollout-selection"
          note: "Later comparison/scoring is the consumer, not a live GUI policy update."
        -
          scope: "Arbitrary model note admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-rte-notes-delivery"
          note: "The append and later consumer are wired, but actual note input origins are not established for this generic string-admission mechanism; no universal trace-fed classification follows."
        -
          scope: "Query/search caches and key-embedding transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-formulate-query"
            - "memory.md#mem-obj-rag-knowledge"
            - "memory.md#mem-rte-query-cache"
            - "memory.md#mem-obj-embeddings"
          note: "These mechanisms persist responses and access metadata, but the records do not establish every original input as a qualifying activity trace or bound absence of trace-fed alternatives."
        -
          scope: "Initial bundle and prior local content production"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-kb-bootstrap"
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
            - "memory.md#mem-obj-embeddings"
          note: "Original production routes and trace mixtures are unavailable; import alone establishes neither trace learning nor a bounded no."
        -
          scope: "Included provider-side retained state behind generation, grounding and embedding endpoints"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-lmm-agent"
            - "runtime.md#rt-cmp-grounding-model"
            - "runtime.md#rt-cmp-embedding-engine"
          note: "The accepted component records establish external calls, not the existence, contents or mechanisms of use-accumulated server state. No trace_learning value for that state follows from client configuration or model weights."
      records:
        - "runtime.md#rt-rte-historical-experience"
        - "memory.md#mem-rte-s1-experience"
        - "memory.md#mem-obj-narrative-memory"
        - "memory.md#mem-obj-episodic-memory"
        - "memory.md#mem-rte-experience-retrieval"
        - "memory.md#mem-rte-knowledge-save"
        - "memory.md#mem-obj-code-result"
        - "runtime.md#rt-rte-code-delegation"
        - "runtime.md#rt-bap-code-return"
        - "memory.md#mem-obj-traj"
        - "memory.md#mem-obj-fact-captions"
        - "memory.md#mem-obj-judge-results"
        - "runtime.md#rt-rte-rollout-selection"
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-rte-notes-delivery"
        - "memory.md#mem-obj-formulate-query"
        - "memory.md#mem-obj-rag-knowledge"
        - "memory.md#mem-rte-query-cache"
        - "memory.md#mem-obj-embeddings"
        - "runtime.md#rt-rte-kb-bootstrap"
        - "runtime.md#rt-cmp-lmm-agent"
        - "runtime.md#rt-cmp-grounding-model"
        - "runtime.md#rt-cmp-embedding-engine"
      note: "Positive automatic trace-fed retained artifacts are supported without a claim of observed improvement. Unresolved writes prevent a system-wide negative or complete inventory assertion. Provider-side retained state remains unresolved; the positive local witnesses do not close that alternative."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Historical CLI summary production from recorded task/plan/reflection text"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-historical-experience"
                - "memory.md#mem-rte-s1-experience"
                - "memory.md#mem-obj-narrative-memory"
                - "memory.md#mem-obj-episodic-memory"
              note: "Task-session plans and reflections accumulated by CLI feed narrative/episodic summaries."
          records:
            - "runtime.md#rt-rte-historical-experience"
            - "memory.md#mem-rte-s1-experience"
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
          note: "The recorded model work text is the established source; partial CLI accumulation is not a full observation/action/outcome transcript."
        -
          scope: "Alternative S2 save API caller-supplied trajectory content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-knowledge-save"
          note: "The callable summary mechanism qualifies, but the absent lifecycle caller leaves original source content/mix unresolved; a trajectory variable name alone does not establish trajectories."
        -
          scope: "Coding continuation summary from action/thought execution history"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-code-result"
                - "runtime.md#rt-rte-code-delegation"
              note: "Recorded coding-model thoughts and task-session work feed the reduced summary."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-code-result"
                - "runtime.md#rt-rte-code-delegation"
              note: "Recorded Python/Bash action requests feed execution_history and its summary; this does not assert that controller results are included."
          records:
            - "memory.md#mem-obj-code-result"
            - "runtime.md#rt-rte-code-delegation"
          note: "Direct controller feedback is omitted from the summary input; recorded requests and model work remain."
        -
          scope: "Offline captions from linked screenshot/action rollout evidence"
          assessment: "known"
          findings:
            -
              value: "trajectories"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traj"
                - "memory.md#mem-obj-fact-captions"
                - "runtime.md#rt-rte-rollout-selection"
              note: "Adjacent before/after screenshots with corresponding executed action form linked state/action experience."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traj"
                - "memory.md#mem-obj-fact-captions"
                - "runtime.md#rt-rte-rollout-selection"
              note: "Recorded exec_code action traces are consumed alongside screenshot pairs."
          records:
            - "memory.md#mem-obj-traj"
            - "memory.md#mem-obj-fact-captions"
            - "runtime.md#rt-rte-rollout-selection"
          note: "Original input is multi-step desktop experience, not the later JSONL adapter label."
        -
          scope: "Initial memory production, notes and cache/search/embedding alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-kb-bootstrap"
            - "memory.md#mem-obj-narrative-memory"
            - "memory.md#mem-obj-episodic-memory"
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-rte-notes-delivery"
            - "memory.md#mem-obj-formulate-query"
            - "memory.md#mem-obj-rag-knowledge"
            - "memory.md#mem-rte-query-cache"
            - "memory.md#mem-obj-embeddings"
          note: "Original trace content is unknown or qualifying trace learning unresolved. Imported static text and timestamp fields do not establish event-stream input."
        -
          scope: "Included provider-side retained state behind generation, grounding and embedding endpoints"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-lmm-agent"
            - "runtime.md#rt-cmp-grounding-model"
            - "runtime.md#rt-cmp-embedding-engine"
          note: "The accepted component records establish external calls, not the existence, contents or mechanisms of use-accumulated server state. No trace_source value for that state follows from client configuration or model weights."
      records:
        - "runtime.md#rt-rte-historical-experience"
        - "memory.md#mem-rte-s1-experience"
        - "memory.md#mem-obj-narrative-memory"
        - "memory.md#mem-obj-episodic-memory"
        - "memory.md#mem-rte-knowledge-save"
        - "memory.md#mem-obj-code-result"
        - "runtime.md#rt-rte-code-delegation"
        - "memory.md#mem-obj-traj"
        - "memory.md#mem-obj-fact-captions"
        - "runtime.md#rt-rte-rollout-selection"
        - "runtime.md#rt-rte-kb-bootstrap"
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-rte-notes-delivery"
        - "memory.md#mem-obj-formulate-query"
        - "memory.md#mem-obj-rag-knowledge"
        - "memory.md#mem-rte-query-cache"
        - "memory.md#mem-obj-embeddings"
        - "runtime.md#rt-cmp-lmm-agent"
        - "runtime.md#rt-cmp-grounding-model"
        - "runtime.md#rt-cmp-embedding-engine"
      note: "Each positive source is tied to a qualifying local update. Missing original sources are not made inapplicable by known routes, and serialization or timestamps do not establish event-streams. Provider-side retained state remains unresolved; the positive local witnesses do not close that alternative."
---

# Agent S memory profile

## Comparison rationale

The profile follows the accepted records, not an inferred uniform architecture. Historical S1/S2 experience and query caches, current ACI retained context, and offline comparison have different write mechanisms and later consumers. Their local findings remain separate. All axis inventories retain unresolved initialization and provider-state alternatives; partial coverage is not weak implementation evidence.

### Content, access and authority

[MEM-OBJ-narrative-memory](memory.md#mem-obj-narrative-memory) and [MEM-OBJ-episodic-memory](memory.md#mem-obj-episodic-memory) provide optional advice. Placement in a system prompt does not turn retrieved recipes into standing instructions. [MEM-OBJ-embeddings](memory.md#mem-obj-embeddings) supplies ranking at a numerical consumer, not textual advice or a model-weight update. [MEM-RTE-query-cache](memory.md#mem-rte-query-cache) additionally routes search inputs. [MEM-OBJ-judge-results](memory.md#mem-obj-judge-results) route scoring and enforce a resume skip through task-key presence; their retained rationale is not the field those consumers use.

The raw historical work text has learning authority at summary generation, while the resulting summary has knowledge authority at later planning. The [MEM-OBJ-code-result](memory.md#mem-obj-code-result) similarly separates the history-to-summary update from advisory delivery. Missing controller-output detail limits warrant, not the existence of this update. [MEM-OBJ-traj](memory.md#mem-obj-traj) feed retained captions; [MEM-OBJ-fact-captions](memory.md#mem-obj-fact-captions) then provide evidence and ranking influence at comparison. None of those paths establishes improved capacity, correct captions or exercised beneficial self-change.

### Transformations and qualifying traces

Summary production is consolidation of retained work, including when the input trace remains. This classification does not certify semantic preservation. The epistemic account's indeterminate content relations concern whether particular propositions are preserved, entailed or conjectured; unseen output cannot establish synthesis. The [MEM-RTE-knowledge-save](memory.md#mem-rte-knowledge-save) retains afforded findings rather than borrowing the CLI's wired caller. Its caller-supplied original trace mixture remains unknown.

The coding summary qualifies as retained continuation context even within a task. Its input includes recorded model thoughts and action requests, not direct controller-result dictionaries. Offline captioning also qualifies because its automatically produced durable descriptions shape a later comparison invocation. Its source is linked screenshot/action experience and recorded execution actions. Ordinary reflection, raw logging without a transformation, and context trimming do not independently establish trace learning. Generic note strings and cached answers retain unresolved trace origins rather than inheriting the historical summary chain's positive value.

### Request and selection boundaries

[MEM-RTE-experience-retrieval](memory.md#mem-rte-experience-retrieval) explicitly fulfills a consumer request. Its cosine ranking and exact-key skipping do not establish an unsolicited embedding-selected push. Query-cache and offline loader returns are also pull. [MEM-RTE-notes-delivery](memory.md#mem-rte-notes-delivery) and the pending coding return are automatic message-construction pushes: availability selects the full applicable content. They support coarse selection, not identifier targeting merely because a task label appears in the payload.

### Canonicalization and limits

Reconciliation supersedes the epistemic caption and comparative-choice object declarations with [MEM-OBJ-fact-captions](memory.md#mem-obj-fact-captions) and [MEM-OBJ-judge-results](memory.md#mem-obj-judge-results). The profile cites those canonical records. Other overlaps are parts or cross-generation scopes, not replacement identities: the S3 code summary remains part of the larger return, and the S2 admission container is not counted as another store beside its content objects.

[RT-RTE-kb-bootstrap](runtime.md#rt-rte-kb-bootstrap) establishes software import, not original entry authorship, human review or complete archive inventory. Existing vector provenance is likewise unknown. The [RT-CMP-lmm-agent](runtime.md#rt-cmp-lmm-agent), [RT-CMP-grounding-model](runtime.md#rt-cmp-grounding-model) and [RT-CMP-embedding-engine](runtime.md#rt-cmp-embedding-engine) component records leave provider-side retention and learning opaque. External model components do not establish a model-weights substrate for use-accumulated memory. These missing facts prevent stronger axis coverage; no local positive witness upgrades those alternatives.

Source-read log: none. This classification used only the supplied accepted members and their governing contracts. No source passages, new records, observed runs or causal evidence were added.
