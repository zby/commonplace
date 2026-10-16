---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "WeKnora memory comparison across personal notes, retrieval feedback, indexed evidence, wiki, conversation checkpoints and admitted skill state."
run-id: "AAS-2026-10-15-weknora-7adf8a01c381-01"
source-identity: "https://github.com/Tencent/WeKnora"
reviewed-boundary: "234aa948db29c10f5ed4b7939285c7b3711c5d4c"
memory-comparison:
  version: 2
  scope: "Accumulated personal notes, note vectors/renderings, topic/affinity/tombstone controls; source files, document chunks/revisions and retrieval indexes; editable wiki bodies/revisions and access/withdrawal state; raw stored conversation/AgentSteps, generated or raw-fallback checkpoints and optional Q&A indexes; admitted skill files, instructions, snapshot/pointer and diagnostic state; later-queryable evaluation metrics. Included unresolved alternatives retain connector/manual/FAQ admission, graph/multimodal/enrichment derivatives, wiki map/taxonomy/issues, attachments/workspace payloads, suspended approval snapshots, MCP caches and host installation. Excludes shipped static prompts/code and ordinary unretained turn state, external model weights, provider internals and external host scheduling. Scope covers writes, maintenance, selectors and actual later consumers, not all runtime storage or permissions."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Personal-note content and status/provenance, topic recurrence, familiarity and tombstones in GORM memory tables"
          assessment: "known"
          findings:
            - value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-item"
                - "memory.md#mem-obj-memory-topic"
                - "memory.md#mem-obj-doc-affinity"
                - "memory.md#mem-obj-memory-tombstone"
              note: "Named memory tables retain these distinct parts; no database-engine identity is inferred."
          records:
            - "memory.md#mem-obj-memory-item"
            - "memory.md#mem-obj-memory-topic"
            - "memory.md#mem-obj-doc-affinity"
            - "memory.md#mem-obj-memory-tombstone"
          note: "Table/repository evidence covers these relational objects, not every application backend."
        - scope: "Personal-note embedding rows"
          assessment: "known"
          findings:
            - value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-embedding"
              note: "Binary float32 vectors reside in memory_item_embeddings; numerical encoding is not a separate storage engine."
          records:
            - "memory.md#mem-obj-memory-embedding"
          note: "The stored vector row is classified independently of the external producing model."
        - scope: "Document and optional conversation-passage retrieval indexes"
          assessment: "known"
          findings:
            - value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunk"
                - "memory.md#mem-rte-knowledge-read"
                - "memory.md#mem-rte-chat-index"
              note: "Produced numerical indexes support subsequent scoped vector search, including Q&A passage search."
          records:
            - "memory.md#mem-obj-chunk"
            - "memory.md#mem-rte-knowledge-read"
            - "memory.md#mem-rte-chat-index"
          note: "Vector is the operative access substrate, not a claim about backend implementation equivalence."
        - scope: "Uploaded source files and seeded installed skill files"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-admission"
                - "runtime.md#rt-rte-skill-install"
              note: "Source-file retention and seeded skill files persist separately from rows and image pointers."
          records:
            - "runtime.md#rt-rte-knowledge-admission"
            - "runtime.md#rt-rte-skill-install"
          note: "Classifies the exposed file objects; remote object-store internals are not inferred."
        - scope: "Published remote skill snapshot"
          assessment: "known"
          findings:
            - value: "service-object"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-skill-install"
                - "runtime.md#rt-bap-skill-image"
              note: "A provider snapshot is admitted and selected by a durable pointer for later workspace startup."
          records:
            - "runtime.md#rt-rte-skill-install"
            - "runtime.md#rt-bap-skill-image"
          note: "The exposed retained object is established; this classification does not describe its internal filesystem or provider database."
        - scope: "Evaluation metrics task map"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-dataset-evaluation"
                - "epistemic.md#epi-obj-metric-result"
              note: "In-process evaluation state has a later result-lookup consumer, without established restart durability."
          records:
            - "runtime.md#rt-rte-dataset-evaluation"
            - "epistemic.md#epi-obj-metric-result"
          note: "Memory includes later-invocation lookup; it need not survive process restart."
        - scope: "Stored message/AgentSteps/checkpoint rows, document chunks/revisions, wiki pages/revisions and Q&A Knowledge records: exact storage backend"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-turn"
            - "runtime.md#rt-rte-context-rewrite"
            - "memory.md#mem-obj-chunk"
            - "memory.md#mem-obj-wiki-page"
            - "memory.md#mem-obj-chat-passage"
          note: "Repositories and DB persistence are recorded, but these records do not pin every operative backend to a controlled substrate; personal-table evidence is not generalized."
        - scope: "Included unresolved alternatives: URL/manual/FAQ and connector admission; summaries/profiles, generated questions, OCR/captions, image vectors, graph derivatives and auto-tags; wiki map/taxonomy/issues; attachments/workspace artifacts, suspended approval snapshots and MCP caches; host installation alternative."
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-chunk"
            - "memory.md#mem-rte-wiki-update"
            - "runtime.md#rt-rte-sandbox-execution"
            - "runtime.md#rt-rte-mcp-call"
            - "runtime.md#rt-rte-skill-install"
          note: "Exact provider/cache/graph/multimodal storage and alternate backend coverage are not established in accepted records. Graph-related names alone do not establish a graph substrate."
      records:
        - "memory.md#mem-obj-memory-item"
        - "memory.md#mem-obj-memory-topic"
        - "memory.md#mem-obj-doc-affinity"
        - "memory.md#mem-obj-memory-tombstone"
        - "memory.md#mem-obj-memory-embedding"
        - "memory.md#mem-obj-chunk"
        - "memory.md#mem-rte-knowledge-read"
        - "memory.md#mem-rte-chat-index"
        - "runtime.md#rt-rte-knowledge-admission"
        - "runtime.md#rt-rte-skill-install"
        - "runtime.md#rt-bap-skill-image"
        - "runtime.md#rt-rte-dataset-evaluation"
        - "epistemic.md#epi-obj-metric-result"
        - "runtime.md#rt-rte-agent-turn"
        - "runtime.md#rt-rte-context-rewrite"
        - "memory.md#mem-obj-wiki-page"
        - "memory.md#mem-obj-chat-passage"
        - "memory.md#mem-rte-wiki-update"
        - "runtime.md#rt-rte-sandbox-execution"
        - "runtime.md#rt-rte-mcp-call"
      note: "Known file, relational, vector, service-object and in-process parts coexist with backend-unspecified repositories and included uninspected alternatives. External model weights and shipped static prompts are excluded from retained memory."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Personal-note statements/topics, wiki Markdown/title/summary, document text/OCR/captions, Q&A passages, raw conversational text and checkpoint summaries/raw archives"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-item"
                - "memory.md#mem-obj-wiki-page"
                - "memory.md#mem-obj-chunk"
                - "memory.md#mem-obj-chat-passage"
                - "runtime.md#rt-rte-context-rewrite"
              note: "These readable bodies reach interpretation as evidence or conversation context; raw fallback remains text rather than becoming a model abstraction."
          records:
            - "memory.md#mem-obj-memory-item"
            - "memory.md#mem-obj-wiki-page"
            - "memory.md#mem-obj-chunk"
            - "memory.md#mem-obj-chat-passage"
            - "runtime.md#rt-rte-context-rewrite"
          note: "Classifies recorded readable parts, not all content of an uploaded binary or provider snapshot."
        - scope: "Memory status/keys/provenance, recurrence/hit counters, tombstone fingerprints, chunk/wiki identifiers and revisions, checkpoint boundaries, image pointer and metric numbers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-item"
                - "memory.md#mem-obj-memory-topic"
                - "memory.md#mem-obj-doc-affinity"
                - "memory.md#mem-obj-memory-tombstone"
                - "memory.md#mem-obj-chunk"
                - "memory.md#mem-obj-wiki-page"
                - "runtime.md#rt-rte-context-rewrite"
                - "runtime.md#rt-bap-skill-image"
                - "epistemic.md#epi-obj-metric-result"
              note: "Localized fields are consumed by fixed eligibility, arithmetic, replay, routing and metric rules."
          records:
            - "memory.md#mem-obj-memory-item"
            - "memory.md#mem-obj-memory-topic"
            - "memory.md#mem-obj-doc-affinity"
            - "memory.md#mem-obj-memory-tombstone"
            - "memory.md#mem-obj-chunk"
            - "memory.md#mem-obj-wiki-page"
            - "runtime.md#rt-rte-context-rewrite"
            - "runtime.md#rt-bap-skill-image"
            - "epistemic.md#epi-obj-metric-result"
          note: "Numerical counters and metrics are symbolic, unlike dense representations."
        - scope: "Dense note vectors and numerical document/passage search representations"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-embedding"
                - "memory.md#mem-obj-chunk"
                - "memory.md#mem-rte-chat-index"
              note: "Dense selection representations distribute numerical information; they are retained outputs, not model-weight updates."
          records:
            - "memory.md#mem-obj-memory-embedding"
            - "memory.md#mem-obj-chunk"
            - "memory.md#mem-rte-chat-index"
          note: "Symbolic model IDs/dimensions remain separate from the vectors."
        - scope: "Installed skill instruction files versus executable files/dependency declarations"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-skill-install"
                - "runtime.md#rt-bap-skill-image"
              note: "Skill documentation guides later model use."
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-skill-install"
                - "runtime.md#rt-bap-skill-image"
              note: "Executable files and declared environment requirements have fixed runtime consumers."
          records:
            - "runtime.md#rt-rte-skill-install"
            - "runtime.md#rt-bap-skill-image"
          note: "Only these evidenced operative parts are classified; the complete provider image remains unresolved."
        - scope: "Opaque snapshot remainder, original binary/multimodal payloads, graph derivatives, attachments, suspended-run payload and cache bodies"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-skill-install"
            - "runtime.md#rt-rte-sandbox-execution"
            - "runtime.md#rt-rte-mcp-call"
            - "memory.md#mem-obj-chunk"
          note: "Readable ledger summaries and attachment manifests cannot classify the payloads they describe. Full multimodal/graph and approval-state forms remain uninspected."
      records:
        - "memory.md#mem-obj-memory-item"
        - "memory.md#mem-obj-wiki-page"
        - "memory.md#mem-obj-chunk"
        - "memory.md#mem-obj-chat-passage"
        - "runtime.md#rt-rte-context-rewrite"
        - "memory.md#mem-obj-memory-topic"
        - "memory.md#mem-obj-doc-affinity"
        - "memory.md#mem-obj-memory-tombstone"
        - "runtime.md#rt-bap-skill-image"
        - "epistemic.md#epi-obj-metric-result"
        - "memory.md#mem-obj-memory-embedding"
        - "memory.md#mem-rte-chat-index"
        - "runtime.md#rt-rte-skill-install"
        - "runtime.md#rt-rte-sandbox-execution"
        - "runtime.md#rt-rte-mcp-call"
      note: "Mixed text, localized controls/executables and dense representations are split by operative part. Unread payloads remain included; provider weights are not treated as accumulated memory."
    lineage:
      assessment: "partial"
      units:
        - scope: "Explicit personal directives and client-supplied manager content; imported document sources and supplied skill bundles"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-rte-personal-write"
                - "runtime.md#rt-rte-knowledge-admission"
                - "runtime.md#rt-rte-skill-install"
              note: "Content enters from statements, files or caller-supplied bundles; caller identity does not establish human authorship."
          records:
            - "memory.md#mem-rte-personal-write"
            - "runtime.md#rt-rte-knowledge-admission"
            - "runtime.md#rt-rte-skill-install"
          note: "Known import paths do not resolve original authorship or all connector/manual alternatives."
        - scope: "User-message-derived notes, recurrence interests, answer-reference familiarity and conversation Q&A passages"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-personal-write"
                - "memory.md#mem-obj-memory-topic"
                - "memory.md#mem-rte-retrieval-conditioning"
                - "memory.md#mem-rte-chat-index"
              note: "Extraction, recurrence/count updates and Q&A indexing derive retained parts from prior conversational activity."
          records:
            - "memory.md#mem-rte-personal-write"
            - "memory.md#mem-obj-memory-topic"
            - "memory.md#mem-rte-retrieval-conditioning"
            - "memory.md#mem-rte-chat-index"
          note: "Assistant answers enter the Q&A path, not the user-only personal-note extractor."
        - scope: "Automatic history summary and raw-archive checkpoint projection"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-rewrite"
              note: "Selected conversation and AgentSteps become a retained summary or raw fallback consumed by later history loading."
          records:
            - "runtime.md#rt-rte-context-rewrite"
          note: "Raw archive and generated summary are separate trace-derived alternatives; neither preserves a proof of semantic fidelity."
        - scope: "Memory embeddings, block renderings, maintenance merges and source-derived document index inputs"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-embedding"
                - "memory.md#mem-obj-memory-item"
                - "memory.md#mem-rte-memory-review"
                - "memory.md#mem-obj-chunk"
              note: "Software/model transformations compile retained text into access or reduced representations."
          records:
            - "memory.md#mem-obj-memory-embedding"
            - "memory.md#mem-obj-memory-item"
            - "memory.md#mem-rte-memory-review"
            - "memory.md#mem-obj-chunk"
          note: "This finding covers the derivation path, not exact model weights or provenance of every input."
        - scope: "Wiki reducer body from existing page, cited chunks or Details fallback"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-rte-wiki-update"
                - "memory.md#mem-obj-wiki-page"
              note: "Reduction rewrites retained source/page material and persists revisions and references."
          records:
            - "memory.md#mem-rte-wiki-update"
            - "memory.md#mem-obj-wiki-page"
          note: "Derivation is established, while proposition entailment and completeness of cited support are not."
        - scope: "Installer-generated files and install-report content"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-skill-install"
              note: "Installer model proposes setup commands and a runtime report rather than merely importing an unchanged bundle."
          records:
            - "runtime.md#rt-rte-skill-install"
          note: "Generated setup material is distinguished from the supplied bundle; full provider-image provenance remains unresolved."
        - scope: "Initial provenance of external inputs and complete alternate source/model/graph/multimodal, direct wiki-writer and provider-payload derivations"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-chunk"
            - "memory.md#mem-rte-wiki-update"
            - "runtime.md#rt-rte-skill-install"
            - "runtime.md#rt-rte-sandbox-execution"
          note: "Known compilation does not establish original author or every enrichment path. These unresolved initial and alternative paths prevent a complete lineage inventory."
      records:
        - "memory.md#mem-rte-personal-write"
        - "runtime.md#rt-rte-knowledge-admission"
        - "runtime.md#rt-rte-skill-install"
        - "memory.md#mem-obj-memory-topic"
        - "memory.md#mem-rte-retrieval-conditioning"
        - "memory.md#mem-rte-chat-index"
        - "runtime.md#rt-rte-context-rewrite"
        - "memory.md#mem-obj-memory-embedding"
        - "memory.md#mem-obj-memory-item"
        - "memory.md#mem-rte-memory-review"
        - "memory.md#mem-obj-chunk"
        - "memory.md#mem-rte-wiki-update"
        - "memory.md#mem-obj-wiki-page"
        - "runtime.md#rt-rte-sandbox-execution"
      note: "Import, trace extraction, compilation and setup authorship are independently supported paths; initial provenance and opaque alternatives remain unresolved. A path label never supplies missing embedding/model provenance."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Personal statements, document/chunk and wiki bodies, Q&A search results, replayed history and checkpoint text at their later readers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-personal-recall"
                - "memory.md#mem-rte-memory-search"
                - "memory.md#mem-rte-knowledge-read"
                - "memory.md#mem-rte-wiki-read"
                - "memory.md#mem-rte-chat-index"
                - "runtime.md#rt-rte-context-rewrite"
              note: "Selected text supplies background/evidence/context to answering models or message-search readers, not authorization to act."
          records:
            - "memory.md#mem-rte-personal-recall"
            - "memory.md#mem-rte-memory-search"
            - "memory.md#mem-rte-knowledge-read"
            - "memory.md#mem-rte-wiki-read"
            - "memory.md#mem-rte-chat-index"
            - "runtime.md#rt-rte-context-rewrite"
          note: "Notes are explicitly wrapped as background data; preference content alone is not standing instruction authority."
        - scope: "Personal text/aliases and dense representations at recall/search selectors; document text/index features at retrieval"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-rte-personal-recall"
                - "memory.md#mem-rte-memory-search"
                - "memory.md#mem-obj-memory-embedding"
                - "memory.md#mem-rte-knowledge-read"
              note: "Retained content and vectors affect lexical/semantic relative selection even when scoring code is fixed."
          records:
            - "memory.md#mem-rte-personal-recall"
            - "memory.md#mem-rte-memory-search"
            - "memory.md#mem-obj-memory-embedding"
            - "memory.md#mem-rte-knowledge-read"
          note: "Ranking is the force at selection, distinct from knowledge at subsequent interpretation."
        - scope: "Familiarity counts at RAG rerank and profile/interests/titles at query rewriter"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-rte-retrieval-conditioning"
                - "memory.md#mem-obj-doc-affinity"
              note: "Persisted hit counts multiply candidate scores and change order."
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-retrieval-conditioning"
              note: "Rewriter receives retained personal background and familiar titles as advisory vocabulary."
          records:
            - "memory.md#mem-rte-retrieval-conditioning"
            - "memory.md#mem-obj-doc-affinity"
          note: "Rewriter context and executable score effects are separate consumers, neither a quality endorsement."
        - scope: "Retained user lines, prior notes/topics and answer references at automatic durable personalization updaters"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-personal-write"
                - "memory.md#mem-obj-memory-topic"
                - "memory.md#mem-rte-retrieval-conditioning"
              note: "Experience feeds durable note, interest and familiarity updates that can shape later retrieval and answering."
          records:
            - "memory.md#mem-rte-personal-write"
            - "memory.md#mem-obj-memory-topic"
            - "memory.md#mem-rte-retrieval-conditioning"
          note: "Authority is at the update consumer; wired trace-fed behavior shaping is not measured improved capacity."
        - scope: "Retained conversation/AgentSteps at automatic checkpoint writer"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-rewrite"
              note: "Recorded experience feeds durable continuation summaries or raw-archive checkpoints with later model consumers."
          records:
            - "runtime.md#rt-rte-context-rewrite"
          note: "This update-consumer force is separate from the checkpoint text knowledge effect and boundary routing effect."
        - scope: "Tombstone fingerprints/source-message windows at future write admission"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-tombstone"
                - "memory.md#mem-rte-personal-write"
              note: "Retained rejection state supplies a criterion for candidate eligibility."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-tombstone"
                - "memory.md#mem-rte-personal-write"
              note: "Matching candidates are refused; bounded windows and best-effort tombstone writes limit the veto."
          records:
            - "memory.md#mem-obj-memory-tombstone"
            - "memory.md#mem-rte-personal-write"
          note: "Tombstone topics also reach the extractor as guidance, but that does not turn deleted content into retained knowledge."
        - scope: "Retained memory status and chunk/wiki enablement at later eligibility checks"
          assessment: "known"
          findings:
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-rte-personal-recall"
                - "memory.md#mem-rte-memory-search"
                - "memory.md#mem-rte-chunk-edit"
                - "memory.md#mem-rte-wiki-read"
              note: "Inactive/replaced or disabled parts are withheld on inspected read routes."
          records:
            - "memory.md#mem-rte-personal-recall"
            - "memory.md#mem-rte-memory-search"
            - "memory.md#mem-rte-chunk-edit"
            - "memory.md#mem-rte-wiki-read"
          note: "Local selection constraints are not a universal stale-cache or backend-erasure guarantee."
        - scope: "Stored wiki table identities at machine rewrite gate"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-wiki-guard"
              note: "Existing row identities define the bounded preservation test."
            - value: "enforcement"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-wiki-guard"
              note: "Excessive identity loss refuses the write, with user/revert/shrink exemptions."
          records:
            - "epistemic.md#epi-rte-wiki-guard"
          note: "The reference is retained content; the fixed shipped guard code is not itself accumulated memory."
        - scope: "Checkpoint coverage identifiers and published image pointer at later loaders/resolvers"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-rewrite"
                - "runtime.md#rt-bap-skill-image"
              note: "Checkpoint boundaries choose replay windows; snapshot pointer chooses the later executable environment."
          records:
            - "runtime.md#rt-rte-context-rewrite"
            - "runtime.md#rt-bap-skill-image"
          note: "These are selected retained control parts, not model-interpreted text."
        - scope: "Retained skill documentation at future model skill use"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-skill-image"
                - "runtime.md#rt-rte-skill-install"
              note: "Natural-language skill files provide standing directions to later model invocations."
          records:
            - "runtime.md#rt-bap-skill-image"
            - "runtime.md#rt-rte-skill-install"
          note: "Executable capability is described in rationale without inventing a controlled authority value for every executable effect."
        - scope: "Complete skill executable effects, attachments, approval snapshots, MCP caches, graph/multimodal derivatives, wiki issue/taxonomy and alternate admission consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-chunk"
            - "memory.md#mem-rte-wiki-update"
            - "runtime.md#rt-rte-sandbox-execution"
            - "runtime.md#rt-rte-mcp-call"
            - "runtime.md#rt-rte-skill-install"
          note: "Opaque payloads and incompletely traced consumers prevent exhaustive authority classification. No blanket authority follows from retention alone."
      records:
        - "memory.md#mem-rte-personal-recall"
        - "memory.md#mem-rte-memory-search"
        - "memory.md#mem-rte-knowledge-read"
        - "memory.md#mem-rte-wiki-read"
        - "memory.md#mem-rte-chat-index"
        - "runtime.md#rt-rte-context-rewrite"
        - "memory.md#mem-obj-memory-embedding"
        - "memory.md#mem-rte-retrieval-conditioning"
        - "memory.md#mem-obj-doc-affinity"
        - "memory.md#mem-rte-personal-write"
        - "memory.md#mem-obj-memory-topic"
        - "memory.md#mem-obj-memory-tombstone"
        - "memory.md#mem-rte-chunk-edit"
        - "epistemic.md#epi-rte-wiki-guard"
        - "runtime.md#rt-bap-skill-image"
        - "runtime.md#rt-rte-skill-install"
        - "memory.md#mem-obj-chunk"
        - "memory.md#mem-rte-wiki-update"
        - "runtime.md#rt-rte-sandbox-execution"
        - "runtime.md#rt-rte-mcp-call"
      note: "Each value is attached to an actual retained part and consumer: knowledge, ranking, learning, validation, enforcement, routing and instruction coexist. Opaque consumers prevent complete coverage; delivery never establishes obedience or benefit."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Ordinary user-transcript extraction, recurrence promotion and reference-hit updates"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-personal-write"
                - "memory.md#mem-obj-memory-topic"
                - "memory.md#mem-rte-retrieval-conditioning"
              note: "Software/model admits statements and interests or increments counters; initiating chat is not per-content approval."
          records:
            - "memory.md#mem-rte-personal-write"
            - "memory.md#mem-obj-memory-topic"
            - "memory.md#mem-rte-retrieval-conditioning"
          note: "Only flagged inferences are held pending; the positive does not classify manager/confirmation caller control."
        - scope: "Timed or forced memory maintenance, vector/backfill and cached rendering"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-review"
                - "memory.md#mem-obj-memory-embedding"
                - "memory.md#mem-obj-memory-item"
              note: "Model/code chooses merged replacements, expiry/demotion, embedding and rendering without a decision approving each output."
          records:
            - "memory.md#mem-rte-memory-review"
            - "memory.md#mem-obj-memory-embedding"
            - "memory.md#mem-obj-memory-item"
          note: "Pressing ConsolidateNow does not make resulting content admission manual."
        - scope: "Document parsing/index enablement, wiki batch rewrite/structural AutoFix, Q&A indexing and eligible compaction checkpoint saves"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-admission"
                - "memory.md#mem-rte-wiki-update"
                - "epistemic.md#epi-rte-wiki-maintenance"
                - "memory.md#mem-rte-chat-index"
                - "runtime.md#rt-rte-context-rewrite"
              note: "Implemented software transformations and eligibility gates admit their outputs independently of per-content human decisions."
          records:
            - "runtime.md#rt-rte-knowledge-admission"
            - "memory.md#mem-rte-wiki-update"
            - "epistemic.md#epi-rte-wiki-maintenance"
            - "memory.md#mem-rte-chat-index"
            - "runtime.md#rt-rte-context-rewrite"
          note: "Known automatic transformations do not settle initial upload control or every direct edit path."
        - scope: "Remote installer snapshot admission and verifier-directed repair"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-skill-install"
              note: "Service verification and pointer switch decide admission of generated setup state; upload initiation is not approval of every package/file change."
          records:
            - "runtime.md#rt-rte-skill-install"
          note: "This covers inspected remote admission, not the host alternative."
        - scope: "Explicit/directive and manager create/edit/confirm/reject; chunk edit/revert; direct wiki user/agent write and supplied-source admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-personal-write"
            - "memory.md#mem-rte-chunk-edit"
            - "memory.md#mem-rte-wiki-update"
            - "epistemic.md#epi-rte-memory-review"
          note: "API/service callers can be human or computation. Origin/manual/EditSource labels and authentication alone do not establish an explicit human content decision, so neither manual nor automatic is assigned to these caller decisions."
        - scope: "Connector/manual/FAQ details, graph/multimodal enrichment, approval snapshots/cache updates and host skill installation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-chunk"
            - "memory.md#mem-rte-wiki-update"
            - "runtime.md#rt-rte-sandbox-execution"
            - "runtime.md#rt-rte-mcp-call"
            - "runtime.md#rt-rte-skill-install"
          note: "Distinct admission mechanisms remain incompletely recorded; automatic physical I/O cannot fill their control gaps."
      records:
        - "memory.md#mem-rte-personal-write"
        - "memory.md#mem-obj-memory-topic"
        - "memory.md#mem-rte-retrieval-conditioning"
        - "memory.md#mem-rte-memory-review"
        - "memory.md#mem-obj-memory-embedding"
        - "memory.md#mem-obj-memory-item"
        - "runtime.md#rt-rte-knowledge-admission"
        - "memory.md#mem-rte-wiki-update"
        - "epistemic.md#epi-rte-wiki-maintenance"
        - "memory.md#mem-rte-chat-index"
        - "runtime.md#rt-rte-context-rewrite"
        - "runtime.md#rt-rte-skill-install"
        - "memory.md#mem-rte-chunk-edit"
        - "epistemic.md#epi-rte-memory-review"
        - "memory.md#mem-obj-chunk"
        - "runtime.md#rt-rte-sandbox-execution"
        - "runtime.md#rt-rte-mcp-call"
      note: "Automatic admission is wired on multiple routes. Manual-capable interfaces are retained as control uncertainty rather than converted into a supported manual finding."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Personal-note update/conflict resolution and automatic maintenance"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-personal-write"
                - "memory.md#mem-rte-memory-review"
              note: "Updates replace existing statements through supersession."
            - value: "dedup"
              basis: "wired"
              records:
                - "memory.md#mem-rte-personal-write"
                - "memory.md#mem-rte-memory-review"
              note: "Bounded duplicate checks and model-selected redundant-memory merging suppress or replace duplicates."
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-review"
              note: "Selected similar notes are combined into a reduced retained statement."
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-review"
              note: "Expiry archives entries and stale tasks lose importance."
            - value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-review"
                - "memory.md#mem-rte-personal-write"
              note: "Superseded/archived retained rows lose normal active-read reliance while history remains."
          records:
            - "memory.md#mem-rte-personal-write"
            - "memory.md#mem-rte-memory-review"
          note: "These implemented transformations have bounded selection/fidelity, not semantic-completeness or quality guarantees."
        - scope: "Recurrence topics promoted into retained interests"
          assessment: "known"
          findings:
            - value: "promote"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-topic"
                - "memory.md#mem-rte-personal-write"
              note: "Repeated resolved topic state crosses a threshold into active interest memory with later recall/rewrite salience."
          records:
            - "memory.md#mem-obj-memory-topic"
            - "memory.md#mem-rte-personal-write"
          note: "Topic resolution fidelity is unresolved; the implemented tier transition is nevertheless supported."
        - scope: "User-only transcript extraction into standing notes"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-personal-write"
              note: "Bounded recorded user messages yield compact durable personal statements for later consumption."
          records:
            - "memory.md#mem-rte-personal-write"
          note: "Consolidation covers the extraction path, not a guarantee that every proposed claim is entailed."
        - scope: "Permitted inferred personal-note candidate class"
          assessment: "known"
          findings:
            - value: "synthesize"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-memory-extraction"
              note: "Extraction instructions explicitly permit the non-entailed event-organising guess; no actual generated instance or reliably realized novelty is recorded."
          records:
            - "epistemic.md#epi-rte-memory-extraction"
          note: "A requested non-input claim is kept at claim strength, not upgraded by the wired ordinary extraction route."
        - scope: "Model-generated conversation summary checkpoint"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-rewrite"
              note: "Selected older retained conversation is compressed into summary context and eligible durable checkpoint."
          records:
            - "runtime.md#rt-rte-context-rewrite"
          note: "Raw-archive fallback is not assigned consolidation merely because it is also a checkpoint."
        - scope: "Versioned document-body edit/revert"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-chunk-edit"
              note: "Existing retained evidence is replaced/reverted while prior bodies/revisions remain."
          records:
            - "memory.md#mem-rte-chunk-edit"
          note: "Index rebuild and generated-question staleness marking do not alone add dedup or semantic invalidation."
        - scope: "Wiki whole-page revision and retained structural cleanup"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-wiki-update"
                - "epistemic.md#epi-rte-wiki-maintenance"
              note: "Page bodies/references are revised from existing content and additions/retractions."
            - value: "invalidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-wiki-maintenance"
              note: "Short retained pages can be archived, withdrawing normal availability while retaining content."
          records:
            - "memory.md#mem-rte-wiki-update"
            - "epistemic.md#epi-rte-wiki-maintenance"
          note: "Deletion is not itself history-preserving invalidation. The archived branch supplies that finding."
        - scope: "Semantic novelty/reduction in all wiki batch/Details alternatives, raw-archive checkpoint transformation, multimodal/graph derivatives and provider-image maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-wiki-update"
            - "runtime.md#rt-rte-context-rewrite"
            - "memory.md#mem-obj-chunk"
            - "runtime.md#rt-rte-skill-install"
          note: "Recorded rewrite routes and source names do not establish every controlled operation. Wiki semantic relation remains indeterminate; index rebuild alone supplies none."
        - scope: "Topic resolver merge internals, wiki map/taxonomy/issues and alternate ingestion/cache cleanup"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-memory-topic"
            - "memory.md#mem-rte-wiki-update"
            - "memory.md#mem-obj-chunk"
            - "runtime.md#rt-rte-mcp-call"
          note: "Uninspected transformations remain included; no dedup/consolidation value is inferred from a route name."
      records:
        - "memory.md#mem-rte-personal-write"
        - "memory.md#mem-rte-memory-review"
        - "memory.md#mem-obj-memory-topic"
        - "epistemic.md#epi-rte-memory-extraction"
        - "runtime.md#rt-rte-context-rewrite"
        - "memory.md#mem-rte-chunk-edit"
        - "memory.md#mem-rte-wiki-update"
        - "epistemic.md#epi-rte-wiki-maintenance"
        - "memory.md#mem-obj-chunk"
        - "runtime.md#rt-rte-skill-install"
        - "runtime.md#rt-rte-mcp-call"
      note: "Positive implemented curation and a separately claimed synthesis class retain different warrants. Raw fallback, semantically unresolved rewrites and uninspected alternatives prevent a complete operation inventory."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "On-demand personal-memory, document, wiki and conversation-message searches/read requests"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-search"
                - "memory.md#mem-rte-knowledge-read"
                - "memory.md#mem-rte-wiki-read"
                - "memory.md#mem-rte-chat-index"
              note: "Consumer-issued query/slug/limit requests retrieve accumulated material and return it to that requesting consumer."
          records:
            - "memory.md#mem-rte-memory-search"
            - "memory.md#mem-rte-knowledge-read"
            - "memory.md#mem-rte-wiki-read"
            - "memory.md#mem-rte-chat-index"
          note: "Code selection and delivery fulfilling the request are not an additional push."
        - scope: "Evaluation-result lookup by task caller"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-dataset-evaluation"
              note: "Caller requests retained in-process task metrics after evaluation work."
          records:
            - "runtime.md#rt-rte-dataset-evaluation"
          note: "No automatic metric-driven successor is inferred."
        - scope: "Turn preparation personal recall and caller history/checkpoint loading"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-personal-recall"
                - "runtime.md#rt-rte-context-rewrite"
                - "runtime.md#rt-rte-agent-turn"
              note: "Application automatically chooses and supplies retained background/history without a foreground request for those memory parts."
          records:
            - "memory.md#mem-rte-personal-recall"
            - "runtime.md#rt-rte-context-rewrite"
            - "runtime.md#rt-rte-agent-turn"
          note: "The user turn triggers the selector; the turn is not an explicit request for each retained item."
        - scope: "Query-understanding background and per-candidate familiarity conditioning"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-retrieval-conditioning"
              note: "Pipeline automatically supplies profile/interests/titles and matched counts to rewriter or rerank code."
          records:
            - "memory.md#mem-rte-retrieval-conditioning"
          note: "Candidate score adjustment is a later code consumer, not only model-prompt read-back."
        - scope: "Later extraction/review and page rewrite consuming retained notes, tombstones/topics and current page/reference state"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-personal-write"
                - "memory.md#mem-rte-memory-review"
                - "memory.md#mem-obj-memory-tombstone"
                - "memory.md#mem-rte-wiki-update"
              note: "Maintenance selectors automatically supply prior retained parts to the updater/model and its admission checks."
          records:
            - "memory.md#mem-rte-personal-write"
            - "memory.md#mem-rte-memory-review"
            - "memory.md#mem-obj-memory-tombstone"
            - "memory.md#mem-rte-wiki-update"
          note: "These updater consumers are separate from requested foreground read tools."
        - scope: "Published skill pointer at subsequent workspace resolution"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-skill-image"
                - "runtime.md#rt-rte-skill-install"
              note: "Application resolves the admitted snapshot and supplies its environment to later sessions."
          records:
            - "runtime.md#rt-bap-skill-image"
            - "runtime.md#rt-rte-skill-install"
          note: "Specific later model selection of a skill is a different operation; full documentation selection was not traced."
        - scope: "Complete skill-document selection, external HTTP/MCP readers, attachments, approval/resume/cache payloads and graph/multimodal consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-bap-skill-image"
            - "memory.md#mem-rte-wiki-read"
            - "runtime.md#rt-rte-sandbox-execution"
            - "runtime.md#rt-rte-mcp-call"
            - "memory.md#mem-obj-chunk"
          note: "Available routes or retained metadata do not settle every requested-versus-automatic delivery. Both established directions remain positive despite this incomplete inventory."
      records:
        - "memory.md#mem-rte-memory-search"
        - "memory.md#mem-rte-knowledge-read"
        - "memory.md#mem-rte-wiki-read"
        - "memory.md#mem-rte-chat-index"
        - "runtime.md#rt-rte-dataset-evaluation"
        - "memory.md#mem-rte-personal-recall"
        - "runtime.md#rt-rte-context-rewrite"
        - "runtime.md#rt-rte-agent-turn"
        - "memory.md#mem-rte-retrieval-conditioning"
        - "memory.md#mem-rte-personal-write"
        - "memory.md#mem-rte-memory-review"
        - "memory.md#mem-obj-memory-tombstone"
        - "memory.md#mem-rte-wiki-update"
        - "runtime.md#rt-bap-skill-image"
        - "runtime.md#rt-rte-skill-install"
        - "runtime.md#rt-rte-sandbox-execution"
        - "runtime.md#rt-rte-mcp-call"
        - "memory.md#mem-obj-chunk"
      note: "Both explicit consumer retrieval and application/maintenance supply are wired. Delivery inside a requested return is counted only as pull; unresolved payload and external-consumer routes remain included."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Automatic personal recall at turn preparation: resident and situational selection"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-personal-recall"
              note: "Trigger is turn preparation; enabled scope, kind/status and availability select resident profile/preferences within rune/item budgets."
            - value: "inferred-lexical"
              basis: "wired"
              records:
                - "memory.md#mem-rte-personal-recall"
              note: "Opening query lexical relevance selects interest and fact/task statements."
            - value: "inferred-embedding"
              basis: "wired"
              records:
                - "memory.md#mem-rte-personal-recall"
                - "memory.md#mem-obj-memory-embedding"
              note: "When configured, query embeddings and stored note vectors select situational statements through fused ranking."
          records:
            - "memory.md#mem-rte-personal-recall"
            - "memory.md#mem-obj-memory-embedding"
          note: "No chat-judgment selector is inferred: recall can invoke an embedder but does not generate recalled notes."
        - scope: "Query-understanding and affinity score push"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-retrieval-conditioning"
              note: "Pipeline-stage trigger loads allowed profile/interests and threshold-qualified familiar titles under small count/text budgets."
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-retrieval-conditioning"
                - "memory.md#mem-obj-doc-affinity"
              note: "At rerank, actual candidate document-ID matches select the corresponding persisted hit counts for score multiplication."
          records:
            - "memory.md#mem-rte-retrieval-conditioning"
            - "memory.md#mem-obj-doc-affinity"
          note: "This identifier value is warranted by a match supplying retained counts, not merely by IDs attached to tool requests."
        - scope: "Automatic history/checkpoint replay to the next model call"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-rewrite"
                - "runtime.md#rt-rte-agent-turn"
              note: "Turn preparation selects newest eligible checkpoint and recent filtered turns using coverage boundaries and contiguous budget rules."
          records:
            - "runtime.md#rt-rte-context-rewrite"
            - "runtime.md#rt-rte-agent-turn"
          note: "Checkpoint IDs control exclusion/window routing; the recorded selector is recency/coverage, not an established targeted identity-match push finding."
        - scope: "Memory review candidate selection and merge-model decision"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-review"
              note: "Due/forced review selects active entries and stale/expiry candidates within review budgets."
            - value: "inferred-lexical"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-review"
              note: "Lexical overlap supplies candidate clusters of retained notes."
            - value: "inferred-embedding"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-review"
              note: "Stored vector similarity can supply retained-note candidate clusters."
            - value: "inferred-judgment"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-review"
              note: "Chat model selects redundant candidate content for a merged replacement or vetoes the merge."
          records:
            - "memory.md#mem-rte-memory-review"
          note: "Cluster admission and model-selected reduction are distinct selection operations in the maintenance chain."
        - scope: "Tombstone matching on later extraction/write admission"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-tombstone"
                - "memory.md#mem-rte-personal-write"
              note: "New candidate trigger supplies fingerprint and source-message identity; actual matches select retained rejection state for a write veto."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-tombstone"
                - "memory.md#mem-rte-personal-write"
              note: "Extraction preparation additionally supplies a bounded recent-tombstone list as guidance."
          records:
            - "memory.md#mem-obj-memory-tombstone"
            - "memory.md#mem-rte-personal-write"
          note: "The exact-fingerprint and bounded extracted-message checks differ from recent-list delivery; neither gives universal suppression."
        - scope: "Published image selection at later workspace startup"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-skill-install"
                - "runtime.md#rt-bap-skill-image"
              note: "Workspace/config resolution uses the published snapshot pointer to select the retained provider image for that later environment."
          records:
            - "runtime.md#rt-rte-skill-install"
            - "runtime.md#rt-bap-skill-image"
          note: "The selected snapshot is the delivered part, unlike a mere catalog identifier."
        - scope: "Full extraction existing-note/topic selector, wiki reducer page/source/link selector, wiki lint probes and skill-doc delivery"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-personal-write"
            - "memory.md#mem-obj-memory-topic"
            - "memory.md#mem-rte-wiki-update"
            - "epistemic.md#epi-rte-wiki-maintenance"
            - "runtime.md#rt-bap-skill-image"
          note: "Some trigger/input/output facts are recorded, but complete selector alternatives and selected payloads are not classified. This prevents complete push-signal coverage."
        - scope: "Consumer-requested note/document/wiki/message and evaluation-result returns"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-memory-search"
            - "memory.md#mem-rte-knowledge-read"
            - "memory.md#mem-rte-wiki-read"
            - "memory.md#mem-rte-chat-index"
            - "runtime.md#rt-rte-dataset-evaluation"
          note: "These completely named requested-return operations are pull; push-signal classification does not apply to them. Their presence cannot make unresolved push routes inapplicable."
        - scope: "Graph/multimodal, attachments/workspaces, approval snapshots, caches and host-install alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-chunk"
            - "memory.md#mem-rte-wiki-update"
            - "runtime.md#rt-rte-sandbox-execution"
            - "runtime.md#rt-rte-mcp-call"
            - "runtime.md#rt-rte-skill-install"
          note: "Triggers and actual delivered parts of these included alternatives remain incompletely inspected."
      records:
        - "memory.md#mem-rte-personal-recall"
        - "memory.md#mem-obj-memory-embedding"
        - "memory.md#mem-rte-retrieval-conditioning"
        - "memory.md#mem-obj-doc-affinity"
        - "runtime.md#rt-rte-context-rewrite"
        - "runtime.md#rt-rte-agent-turn"
        - "memory.md#mem-rte-memory-review"
        - "memory.md#mem-obj-memory-tombstone"
        - "memory.md#mem-rte-personal-write"
        - "runtime.md#rt-rte-skill-install"
        - "runtime.md#rt-bap-skill-image"
        - "memory.md#mem-obj-memory-topic"
        - "memory.md#mem-rte-wiki-update"
        - "epistemic.md#epi-rte-wiki-maintenance"
        - "memory.md#mem-rte-memory-search"
        - "memory.md#mem-rte-knowledge-read"
        - "memory.md#mem-rte-wiki-read"
        - "memory.md#mem-rte-chat-index"
        - "runtime.md#rt-rte-dataset-evaluation"
        - "memory.md#mem-obj-chunk"
        - "runtime.md#rt-rte-sandbox-execution"
        - "runtime.md#rt-rte-mcp-call"
      note: "Push routes establish coarse, identifier, lexical, embedding and model-judgment selection locally. Pull-only units are inapplicable locally, while unresolved push alternatives prevent whole-axis completeness or inapplicability."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Automatic user-message extraction and recurrence-interest promotion to later recall/search/rewriter"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-personal-write"
                - "memory.md#mem-obj-memory-topic"
                - "memory.md#mem-rte-personal-recall"
                - "memory.md#mem-rte-retrieval-conditioning"
              note: "Recorded user activity feeds software-admitted durable notes/interests, then subsequent answering and retrieval consumers."
          records:
            - "memory.md#mem-rte-personal-write"
            - "memory.md#mem-obj-memory-topic"
            - "memory.md#mem-rte-personal-recall"
            - "memory.md#mem-rte-retrieval-conditioning"
          note: "The trace-fed chain qualifies even without new knowledge or benefit measurements; inferred/pending outputs require later activation."
        - scope: "Completed-answer reference counts to later familiarity rerank and rewriter"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-doc-affinity"
                - "memory.md#mem-rte-retrieval-conditioning"
              note: "Prior answer references automatically update retained counters/titles that later alter retrieval order and background vocabulary."
          records:
            - "memory.md#mem-obj-doc-affinity"
            - "memory.md#mem-rte-retrieval-conditioning"
          note: "Counts encode selection experience, not satisfaction or verified relevance improvement."
        - scope: "Automatic model summary and raw-archive continuation checkpoints"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-rewrite"
                - "runtime.md#rt-rte-agent-turn"
              note: "Conversation/AgentSteps feed automatic retained checkpoints; later caller history loading supplies the result as context."
          records:
            - "runtime.md#rt-rte-context-rewrite"
            - "runtime.md#rt-rte-agent-turn"
          note: "Both generated and raw-fallback continuation forms qualify as durable behavior-shaping artifacts. Transient previews alone are not this finding."
        - scope: "Q&A passage indexing to message-search results"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-chat-index"
            - "memory.md#mem-obj-chat-passage"
          note: "Automatic trace retention and later search are wired, but accepted records stop at message-search output and do not establish a durable behavior-shaping consumer beyond that endpoint. No positive or bounded negative is assigned."
        - scope: "Verifier-directed setup repair and final skill image"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-skill-install"
            - "runtime.md#rt-bap-skill-image"
          note: "Diagnostic findings affect repair and files later affect capability, but accepted records do not establish every persisted trace-to-durable-artifact write; transcript retention alone cannot classify this route."
        - scope: "Document/connector/wiki/multimodal/graph input origins; attachments, approval snapshots and remaining maintenance writes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-chunk"
            - "memory.md#mem-rte-wiki-update"
            - "runtime.md#rt-rte-sandbox-execution"
            - "runtime.md#rt-rte-mcp-call"
            - "runtime.md#rt-rte-skill-install"
          note: "Imported content can include activity records, but exact original content and qualifying trace-fed later-consumer chains are not recorded for every included path. No system-wide no is warranted."
      records:
        - "memory.md#mem-rte-personal-write"
        - "memory.md#mem-obj-memory-topic"
        - "memory.md#mem-rte-personal-recall"
        - "memory.md#mem-rte-retrieval-conditioning"
        - "memory.md#mem-obj-doc-affinity"
        - "runtime.md#rt-rte-context-rewrite"
        - "runtime.md#rt-rte-agent-turn"
        - "memory.md#mem-rte-chat-index"
        - "memory.md#mem-obj-chat-passage"
        - "runtime.md#rt-rte-skill-install"
        - "runtime.md#rt-bap-skill-image"
        - "memory.md#mem-obj-chunk"
        - "memory.md#mem-rte-wiki-update"
        - "runtime.md#rt-rte-sandbox-execution"
        - "runtime.md#rt-rte-mcp-call"
      note: "Wired yes findings cover personalization, familiarity feedback and continuation checkpoints. Other retention and capability paths stay unresolved; absence of improvement evidence is not trace-learning absence."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Personal note extraction and recurrence-interest update inputs"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-personal-write"
                - "memory.md#mem-obj-memory-topic"
              note: "Original inputs are recorded user turns from conversational sessions; preceding user context is not tool output."
          records:
            - "memory.md#mem-rte-personal-write"
            - "memory.md#mem-obj-memory-topic"
          note: "Assistant messages advance cursors but are not the personal-note extraction transcript. No tool-traces value is inferred on this route."
        - scope: "Familiarity update original answer-reference input"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-doc-affinity"
                - "memory.md#mem-rte-retrieval-conditioning"
              note: "References attached to completed conversational answers supply document identities for retained familiarity counts."
          records:
            - "memory.md#mem-obj-doc-affinity"
            - "memory.md#mem-rte-retrieval-conditioning"
          note: "The source is answer-associated session content, not an explicit thumbs-up or a reconstructed tool-call trace."
        - scope: "Conversation summary/raw-archive checkpoint original history"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-rewrite"
                - "runtime.md#rt-rte-agent-turn"
              note: "Selected conversational turns feed the continuation artifact."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-rewrite"
                - "runtime.md#rt-rte-agent-turn"
              note: "Persisted AgentSteps/tool requests and results are part of replayed/compacted history, distinct from conversational prose."
          records:
            - "runtime.md#rt-rte-context-rewrite"
            - "runtime.md#rt-rte-agent-turn"
          note: "Both source kinds survive classification even when summarization omits detail. Linked agent activity alone is not asserted as trajectories."
        - scope: "Potential trace inputs to indexed Q&A, setup diagnostics/images and source/wiki/graph/multimodal alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-chat-index"
            - "runtime.md#rt-rte-skill-install"
            - "memory.md#mem-rte-wiki-update"
            - "memory.md#mem-obj-chunk"
          note: "Where qualifying trace learning or original mixed input remains unresolved, trace source is also unresolved; static import is not by itself a trace source."
        - scope: "Attachments/workspace, approval snapshots, caches and host-install trace input"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-sandbox-execution"
            - "runtime.md#rt-rte-mcp-call"
            - "runtime.md#rt-rte-skill-install"
          note: "Original payload content and qualifying update consumers are not established. Known qualifying routes elsewhere do not resolve these parts."
      records:
        - "memory.md#mem-rte-personal-write"
        - "memory.md#mem-obj-memory-topic"
        - "memory.md#mem-obj-doc-affinity"
        - "memory.md#mem-rte-retrieval-conditioning"
        - "runtime.md#rt-rte-context-rewrite"
        - "runtime.md#rt-rte-agent-turn"
        - "memory.md#mem-rte-chat-index"
        - "runtime.md#rt-rte-skill-install"
        - "memory.md#mem-rte-wiki-update"
        - "memory.md#mem-obj-chunk"
        - "runtime.md#rt-rte-sandbox-execution"
        - "runtime.md#rt-rte-mcp-call"
      note: "Session logs and tool traces are supported on their actual qualifying writes. No event-streams or trajectories value follows merely from runtime callbacks, timestamps or step serialization; unknown qualifying routes retain unknown source coverage."
---

# WeKnora memory profile

## Comparison rationale

This profile classifies accepted implementation records, not observed operation.
All positive implementation findings remain `wired`; the explicit synthesis
request retains `claimed`. No execution or benefit is inferred from retention,
prompt delivery, successful validation or an available consumer.

### Canonical records and scope

Reconciliation supersedes the epistemic chunk, memory-item and wiki-page
objects with [MEM-OBJ-chunk](memory.md#mem-obj-chunk),
[MEM-OBJ-memory-item](memory.md#mem-obj-memory-item) and
[MEM-OBJ-wiki-page](memory.md#mem-obj-wiki-page). Their canonical IDs supply
this profile's object citations. This changes no classification warrant:
epistemic route records still describe distinct extraction, checking and
maintenance functions. Context rewrite is not personal-store review; a
checkpoint object is not its transformation route. Neither containment nor
shared conversational origin merges these objects.

Every axis is partial over the stated inventory. Accepted records establish
positive routes but retain uninspected alternatives and backend/payload gaps.
The limits on [MEM-OBJ-chunk](memory.md#mem-obj-chunk),
[MEM-RTE-wiki-update](memory.md#mem-rte-wiki-update),
[RT-RTE-sandbox-execution](runtime.md#rt-rte-sandbox-execution),
[RT-RTE-mcp-call](runtime.md#rt-rte-mcp-call) and
[RT-RTE-skill-install](runtime.md#rt-rte-skill-install) prevent extending one
inspected path to graph, multimodal, workspace, approval or host alternatives.
A provider-backed image has a known exposed service-object boundary without a
known complete payload. A diagnostic report does not classify that payload.
Repository persistence without a pinned backend is retained as uncertainty,
not silently projected to SQLite or a particular relational engine.

### Consumer-relative mappings

Personal notes supply background knowledge, not permission or automatically
binding instructions. Retained words/vectors also rank selection, and
familiarity counts change executable rerank order. Those forces coexist with
learning authority at the experience-fed updater. These are separate
consumers, not a blanket consequence of trace learning
([MEM-RTE-personal-recall](memory.md#mem-rte-personal-recall),
[MEM-RTE-retrieval-conditioning](memory.md#mem-rte-retrieval-conditioning)).
Checkpoint boundary fields route replay while checkpoint text supplies context.
Skill documentation instead supplies standing instructions; a snapshot pointer
routes later workspace resolution. Executable capability is not forced into a
new authority category absent from the controlled vocabulary
([RT-RTE-context-rewrite](runtime.md#rt-rte-context-rewrite),
[RT-BAP-skill-image](runtime.md#rt-bap-skill-image)).

Tombstones supply both a candidate criterion and an enforced veto. Existing
wiki row identities likewise supply validation and bounded enforcement at the
rewrite gate. Neither is truth certification. Status exclusion and archival
withdraw reliance locally; deletion does not imply retained history or global
erasure ([MEM-OBJ-memory-tombstone](memory.md#mem-obj-memory-tombstone),
[EPI-RTE-wiki-guard](epistemic.md#epi-rte-wiki-guard),
[EPI-RTE-wiki-maintenance](epistemic.md#epi-rte-wiki-maintenance)).

Human-capable APIs do not establish manual write agency. Explicit/manual origin
labels and authenticated callers leave the actual content decision unresolved.
This does not weaken known software admission of unflagged extraction,
consolidation or snapshots. Conversely, a user initiating those workflows does
not make each admitted output manually approved
([MEM-RTE-personal-write](memory.md#mem-rte-personal-write),
[MEM-RTE-memory-review](memory.md#mem-rte-memory-review),
[RT-RTE-skill-install](runtime.md#rt-rte-skill-install)).

### Transformations, selection and traces

Consolidation is supported for standing-note extraction, selected duplicate
merges and generated continuation summaries. Raw checkpoint fallback has its
own path: retention and later consumption qualify as trace-fed continuation,
but copying an archive does not establish consolidation. The extraction
prompt's deliberately non-entailed inference example supports a claimed
synthesis class, not a wired guarantee that outputs contain new claims. Wiki
rewriting supports evolution; indeterminate semantics do not prove synthesis
([MEM-RTE-personal-write](memory.md#mem-rte-personal-write),
[MEM-RTE-memory-review](memory.md#mem-rte-memory-review),
[EPI-RTE-memory-extraction](epistemic.md#epi-rte-memory-extraction),
[RT-RTE-context-rewrite](runtime.md#rt-rte-context-rewrite),
[MEM-RTE-wiki-update](memory.md#mem-rte-wiki-update)).

Requested search/read returns are pull. Turn-time recall, history supply and
maintenance selection are push at their respective consumers. A document-ID
match selects familiarity counts; a snapshot pointer selects the delivered
image. These actual identity matches establish identifier signals. A slug on a
requested wiki read does not. Coarse availability/budget selection remains
separate from query lexical/vector ranking and maintenance-model judgment
([MEM-RTE-memory-search](memory.md#mem-rte-memory-search),
[MEM-RTE-personal-recall](memory.md#mem-rte-personal-recall),
[MEM-RTE-retrieval-conditioning](memory.md#mem-rte-retrieval-conditioning),
[MEM-RTE-memory-review](memory.md#mem-rte-memory-review),
[RT-BAP-skill-image](runtime.md#rt-bap-skill-image)).

User-turn extraction, recurrence, familiarity feedback and durable continuation
checkpoints have qualifying automatic trace-to-later-consumer chains. Their
wired yes does not claim better future action. Q&A indexing proves later
message-search output but not the further behavior-shaping consumer needed
for a positive here. Installation repair preserves effects and selected gate
findings, not replayed prior conversation; a diagnostic transcript alone cannot
establish trace learning. These unresolved routes remain unresolved rather
than receiving local no or inapplicable source labels
([MEM-RTE-chat-index](memory.md#mem-rte-chat-index),
[RT-RTE-skill-install](runtime.md#rt-rte-skill-install)).

The source classification follows original content. Personal extraction uses
user session lines. Familiarity uses answer-associated references, not user
approval. Checkpoint history also includes AgentSteps and tool-call/result
material. Neither a timestamp nor being handled by a completion callback adds
event-stream provenance; step sequences alone do not establish trajectories
([MEM-RTE-personal-write](memory.md#mem-rte-personal-write),
[MEM-OBJ-doc-affinity](memory.md#mem-obj-doc-affinity),
[RT-RTE-context-rewrite](runtime.md#rt-rte-context-rewrite),
[RT-RTE-agent-turn](runtime.md#rt-rte-agent-turn)).

### Source-read log

No frozen-source files were read for this classification. The supplied records,
their annotations and reconciliation supplied the warrants. No additional
records, quotations or evidence were introduced.
