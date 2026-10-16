---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: Synto memory comparison profile covering retained source knowledge, identity constraints,
  feedback, recovery/cache state, reports and exported packs, with optional RAG uncertainty.
run-id: AAS-2026-10-15-synto-eabcdcce3da2-01
source-identity: https://github.com/kytmanov/synto
reviewed-boundary: 91ac6a3681df0552b6c9baef159439c7ebd780c9
memory-comparison:
  version: 2
  scope: 'Retained source documents/segments and raw notes; derived analyses, summaries, articles/drafts,
    saved Q&A/synthesis; identities, denials, relations, routing indexes and rebuild seeds; rejection
    guidance; checkpoints and response cache; metric/audit and comparison reports; exported content and
    vault-derived pack guidance; optional injected RAG write payload and unresolved store/consumer. Static
    shipped prompts, current-call-only answers/context and external provider weights or mutation are excluded:
    no use-updated provider memory is established within Synto. External hosts are excluded implementations,
    but shipped pack consumer affordances remain included.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: 'Vault and pack files: originals, raw Markdown, articles/drafts, summaries, saved answers,
          indexes, identity seed, guidance and comparison reports'
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-source-documents
          - memory.md#mem-obj-raw-notes
          - memory.md#mem-obj-source-summaries
          - memory.md#mem-obj-synthesis
          - memory.md#mem-obj-index
          - runtime.md#rt-rte-pipeline-run
          - runtime.md#rt-rte-pack-export
          - runtime.md#rt-rte-compare-eval
          note: Filesystem retention; Git auto-commit is optional history, not the substrate of every
            live object.
        records:
        - memory.md#mem-obj-source-documents
        - memory.md#mem-obj-raw-notes
        - memory.md#mem-obj-source-summaries
        - memory.md#mem-obj-synthesis
        - memory.md#mem-obj-index
        - runtime.md#rt-rte-pipeline-run
        - runtime.md#rt-rte-pack-export
        - runtime.md#rt-rte-compare-eval
        note: These retained filesystem objects have inspected write and later-reader paths.
      - scope: SQLite analysis, source segments, identities/denials, relations, checkpoints, response
          cache, rejection and metrics state
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-source-documents
          - memory.md#mem-obj-raw-notes
          - memory.md#mem-obj-concept-entities
          - memory.md#mem-obj-relations
          - memory.md#mem-obj-ingest-chunks
          - memory.md#mem-obj-llm-cache
          - memory.md#mem-obj-rejections
          - memory.md#mem-obj-metric-events
          note: Retained rows in state.db, not a generic opaque service.
        records:
        - memory.md#mem-obj-source-documents
        - memory.md#mem-obj-raw-notes
        - memory.md#mem-obj-concept-entities
        - memory.md#mem-obj-relations
        - memory.md#mem-obj-ingest-chunks
        - memory.md#mem-obj-llm-cache
        - memory.md#mem-obj-rejections
        - memory.md#mem-obj-metric-events
        note: The accepted inventory names the database objects separately from exported representations.
      - scope: Retained relation edges and occurrence associations
        assessment: known
        findings:
        - value: graph
          basis: wired
          records:
          - memory.md#mem-obj-relations
          note: Relations and source associations are retained graph access structures used by optional
            graph expansion.
        records:
        - memory.md#mem-obj-relations
        note: Graph-organized memory coexists with its SQLite persistence.
      - scope: Injected RAG store persistence
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-rag-embeddings
        note: add_document arguments do not disclose the store substrate or durability; dense encoding
          alone does not establish a vector storage backend.
      records:
      - memory.md#mem-obj-source-documents
      - memory.md#mem-obj-raw-notes
      - memory.md#mem-obj-source-summaries
      - memory.md#mem-obj-synthesis
      - memory.md#mem-obj-index
      - runtime.md#rt-rte-pipeline-run
      - runtime.md#rt-rte-pack-export
      - runtime.md#rt-rte-compare-eval
      - memory.md#mem-obj-concept-entities
      - memory.md#mem-obj-relations
      - memory.md#mem-obj-ingest-chunks
      - memory.md#mem-obj-llm-cache
      - memory.md#mem-obj-rejections
      - memory.md#mem-obj-metric-events
      - memory.md#mem-obj-rag-embeddings
      note: Files, SQLite and graph organization are supported. The included injected-store alternative
        prevents complete substrate coverage; external inference weights are not asserted to be use-updated
        Synto memory.
    representational_form:
      assessment: partial
      units:
      - scope: Source and derived prose consumed by people/models; feedback, cache text and routing catalogues
          on their textual paths
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-source-documents
          - memory.md#mem-obj-raw-notes
          - memory.md#mem-obj-source-summaries
          - memory.md#mem-obj-rejections
          - memory.md#mem-obj-llm-cache
          - memory.md#mem-obj-index
          - memory.md#mem-obj-synthesis
          - runtime.md#rt-rte-pipeline-run
          - runtime.md#rt-bap-pack-guidance
          note: Source text, summaries, article/answer prose, revision feedback and generated guidance
            are interpreted as language.
        records:
        - memory.md#mem-obj-source-documents
        - memory.md#mem-obj-raw-notes
        - memory.md#mem-obj-source-summaries
        - memory.md#mem-obj-rejections
        - memory.md#mem-obj-llm-cache
        - memory.md#mem-obj-index
        - memory.md#mem-obj-synthesis
        - runtime.md#rt-rte-pipeline-run
        - runtime.md#rt-bap-pack-guidance
        note: Natural-language consumption is distinct from fixed-rule access fields.
      - scope: Identity keys/denials, statuses/hashes, graph predicates, checkpoint fields, source references
          and audit counters at fixed-rule consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-concept-entities
          - memory.md#mem-obj-relations
          - memory.md#mem-obj-ingest-chunks
          - memory.md#mem-obj-raw-notes
          - memory.md#mem-obj-index
          - memory.md#mem-obj-synthesis
          - memory.md#mem-obj-metric-events
          note: Localized identifiers and typed metadata determine normalization, resume, access and overwrite
            decisions.
        records:
        - memory.md#mem-obj-concept-entities
        - memory.md#mem-obj-relations
        - memory.md#mem-obj-ingest-chunks
        - memory.md#mem-obj-raw-notes
        - memory.md#mem-obj-index
        - memory.md#mem-obj-synthesis
        - memory.md#mem-obj-metric-events
        note: JSON/Markdown containers can mix prose and symbolic fields; this unit covers only fixed-rule
          parts.
      - scope: Dense embeddings passed to injected store, separate source chunks and metadata
        assessment: partial
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-rag-embeddings
          note: Dense distributed numerical vectors, not symbolic numbers merely because serialized as
            arrays.
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-rag-embeddings
          note: Source chunks accompany vectors.
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-rag-embeddings
          note: Source/type identifiers accompany chunks and vectors.
        records:
        - memory.md#mem-obj-rag-embeddings
        note: The numerical write arguments are inspected; the provider version and full stored payload
          remain unresolved.
      - scope: Opaque additional retained payload inside injected RAG implementation
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-rag-embeddings
        note: Stored encoding beyond inspected write arguments and actual later consumption are uninspected.
      records:
      - memory.md#mem-obj-source-documents
      - memory.md#mem-obj-raw-notes
      - memory.md#mem-obj-source-summaries
      - memory.md#mem-obj-rejections
      - memory.md#mem-obj-llm-cache
      - memory.md#mem-obj-index
      - memory.md#mem-obj-synthesis
      - runtime.md#rt-rte-pipeline-run
      - runtime.md#rt-bap-pack-guidance
      - memory.md#mem-obj-concept-entities
      - memory.md#mem-obj-relations
      - memory.md#mem-obj-ingest-chunks
      - memory.md#mem-obj-metric-events
      - memory.md#mem-obj-rag-embeddings
      note: Mixed forms are split by consumption. Known dense write arguments do not classify every operative
        part inside the injected store.
    lineage:
      assessment: partial
      units:
      - scope: Imported original documents, segments and externally supplied source text
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-source-documents
          - memory.md#mem-obj-raw-notes
          note: External source material is copied/extracted or supplied as raw input; source truth and
            extraction fidelity are separate.
        records:
        - memory.md#mem-obj-source-documents
        - memory.md#mem-obj-raw-notes
        note: Acquisition lineage is known; original authorship of every external note is not established.
      - scope: Human supplied rejection reasons, explicit identity decisions and edited drafts
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-rejections
          - memory.md#mem-obj-concept-entities
          - workflow.md#wf-rte-interactive-review
          note: Humans supply criticism, alias/identity decisions or edited retained text.
        records:
        - memory.md#mem-obj-rejections
        - memory.md#mem-obj-concept-entities
        - workflow.md#wf-rte-interactive-review
        note: Direct content decisions have authored lineage, independently of physical software writes.
      - scope: Source-derived analysis, concepts, relations, summaries, articles, saved answers, indexes
          and generated pack guidance
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-raw-notes
          - memory.md#mem-obj-source-summaries
          - memory.md#mem-obj-concept-entities
          - memory.md#mem-obj-relations
          - memory.md#mem-obj-index
          - memory.md#mem-obj-synthesis
          - runtime.md#rt-rte-pipeline-run
          - runtime.md#rt-rte-pack-export
          - runtime.md#rt-bap-pack-guidance
          note: Model/code transformations of source knowledge and vault state; a command named synthesis
            alone proves no novel claim.
        records:
        - memory.md#mem-obj-raw-notes
        - memory.md#mem-obj-source-summaries
        - memory.md#mem-obj-concept-entities
        - memory.md#mem-obj-relations
        - memory.md#mem-obj-index
        - memory.md#mem-obj-synthesis
        - runtime.md#rt-rte-pipeline-run
        - runtime.md#rt-rte-pack-export
        - runtime.md#rt-bap-pack-guidance
        note: These are derived retained representations, not automatically evidence of experience learning.
      - scope: Analysis checkpoints and response-cache outputs retained from prior calls; metrics/audit
          and comparison artifacts
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-ingest-chunks
          - memory.md#mem-rte-checkpoint-resume
          - memory.md#mem-obj-llm-cache
          - memory.md#mem-rte-response-reuse
          - memory.md#mem-obj-metric-events
          - runtime.md#rt-rte-compare-eval
          note: Prior call outputs and activity are captured for resume, reuse or inspection.
        records:
        - memory.md#mem-obj-ingest-chunks
        - memory.md#mem-rte-checkpoint-resume
        - memory.md#mem-obj-llm-cache
        - memory.md#mem-rte-response-reuse
        - memory.md#mem-obj-metric-events
        - runtime.md#rt-rte-compare-eval
        note: Retained call results and activity/report artifacts derive from execution records, without
          implying trace learning for every object.
      - scope: Feedback-conditioned rewritten articles
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-bap-rejection-guidance
          - memory.md#mem-obj-rejections
          - runtime.md#rt-rte-pipeline-run
          - runtime.md#rt-rte-draft-publication
          note: Retained criticism of a generated draft feeds later durable revision.
        records:
        - runtime.md#rt-bap-rejection-guidance
        - memory.md#mem-obj-rejections
        - runtime.md#rt-rte-pipeline-run
        - runtime.md#rt-rte-draft-publication
        note: The article combines source compilation and retained review experience.
      - scope: Injected dense vectors and unknown store initialization
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-rag-embeddings
          - runtime.md#rt-cmp-embed
          note: Vectors are computed from supplied preprocessed source chunks.
        records:
        - memory.md#mem-obj-rag-embeddings
        - runtime.md#rt-cmp-embed
        note: The visible text-to-vector derivation is known, but endpoint provenance and initial/store-side
          material are not.
      records:
      - memory.md#mem-obj-source-documents
      - memory.md#mem-obj-raw-notes
      - memory.md#mem-obj-rejections
      - memory.md#mem-obj-concept-entities
      - workflow.md#wf-rte-interactive-review
      - memory.md#mem-obj-source-summaries
      - memory.md#mem-obj-relations
      - memory.md#mem-obj-index
      - memory.md#mem-obj-synthesis
      - runtime.md#rt-rte-pipeline-run
      - runtime.md#rt-rte-pack-export
      - runtime.md#rt-bap-pack-guidance
      - memory.md#mem-obj-ingest-chunks
      - memory.md#mem-rte-checkpoint-resume
      - memory.md#mem-obj-llm-cache
      - memory.md#mem-rte-response-reuse
      - memory.md#mem-obj-metric-events
      - runtime.md#rt-rte-compare-eval
      - runtime.md#rt-bap-rejection-guidance
      - runtime.md#rt-rte-draft-publication
      - memory.md#mem-obj-rag-embeddings
      - runtime.md#rt-cmp-embed
      note: Positive derivation paths coexist with unresolved initialization, external authorship and
        embedding provenance; no complete provenance union is warranted.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Raw prose, summaries, published/saved article slices and source passages at writing, answering
          or external reading consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-raw-notes
          - memory.md#mem-obj-source-summaries
          - memory.md#mem-obj-synthesis
          - runtime.md#rt-rte-pipeline-run
          - runtime.md#rt-rte-query-answer
          - memory.md#mem-rte-source-passages
          - runtime.md#rt-rte-pack-export
          note: Retained content supplies source material or answering context.
        records:
        - memory.md#mem-obj-raw-notes
        - memory.md#mem-obj-source-summaries
        - memory.md#mem-obj-synthesis
        - runtime.md#rt-rte-pipeline-run
        - runtime.md#rt-rte-query-answer
        - memory.md#mem-rte-source-passages
        - runtime.md#rt-rte-pack-export
        note: These objects supply context/evidence, not a factual acceptance guarantee.
      - scope: Rejection feedback at heavy writer
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - runtime.md#rt-bap-rejection-guidance
          - memory.md#mem-obj-rejections
          note: Previous rejection reasons are supplied as directions to address issues.
        - value: learning
          basis: wired
          records:
          - runtime.md#rt-bap-rejection-guidance
          - memory.md#mem-obj-rejections
          - runtime.md#rt-rte-pipeline-run
          - runtime.md#rt-rte-draft-publication
          note: Retained review experience conditions an automatic rewrite of a durable article later
            available as knowledge; improvement is unobserved.
        records:
        - runtime.md#rt-bap-rejection-guidance
        - memory.md#mem-obj-rejections
        note: The same experience has separate update and downstream effects.
      - scope: Generated pack guidance at an external agent host
        assessment: known
        findings:
        - value: instruction
          basis: afforded
          records:
          - runtime.md#rt-bap-pack-guidance
          - runtime.md#rt-rte-pack-export
          note: Standing directions request source checking and read-only behavior.
        - value: routing
          basis: afforded
          records:
          - runtime.md#rt-bap-pack-guidance
          - runtime.md#rt-rte-pack-export
          note: Vault-derived catalogue and instructions direct later agents to indexes, articles and
            sources.
        records:
        - runtime.md#rt-bap-pack-guidance
        - runtime.md#rt-rte-pack-export
        note: Rendering and disk delivery are wired, but later host loading and interpretation are only
          afforded.
      - scope: Retained aliases/denials and identity seed at normalization, query expansion and restore
          code
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-concept-entities
          - memory.md#mem-rte-identity-rebuild
          note: Canonical identities, aliases and source allocation select normalization and query routes.
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-concept-entities
          - memory.md#mem-rte-identity-rebuild
          note: Retained denials constrain admissible alias candidates.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-concept-entities
          - memory.md#mem-rte-identity-rebuild
          note: Denials veto reattachment; restoration preserves their negative effect.
        records:
        - memory.md#mem-obj-concept-entities
        - memory.md#mem-rte-identity-rebuild
        note: Fixed-rule identity decisions have distinct force from article prose.
      - scope: Retained status/hash/confidence/block state at scheduler and admission/overwrite consumers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-raw-notes
          - memory.md#mem-obj-rejections
          note: Hashes/status and blocked concepts select skip, retry or compilation eligibility.
        - value: validation
          basis: wired
          records:
          - runtime.md#rt-rte-draft-publication
          - memory.md#mem-rte-synthesis-save
          - epistemic.md#epi-rte-synthesis-guard
          - epistemic.md#epi-rte-confidence-score
          note: Retained confidence and content hashes are checked against enabled admission/update criteria.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-rejections
          - runtime.md#rt-rte-draft-publication
          - memory.md#mem-rte-synthesis-save
          - epistemic.md#epi-rte-synthesis-guard
          note: Blocks, thresholds and edit guards can prevent compilation, publication or overwrite.
        records:
        - memory.md#mem-obj-raw-notes
        - memory.md#mem-obj-rejections
        - runtime.md#rt-rte-draft-publication
        - memory.md#mem-rte-synthesis-save
        - epistemic.md#epi-rte-synthesis-guard
        - epistemic.md#epi-rte-confidence-score
        note: These values control eligibility rather than certify truth.
      - scope: Retained catalogues/text/aliases and graph occurrence/confidence fields at retrieval selectors
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-index
          - memory.md#mem-obj-concept-entities
          - memory.md#mem-obj-relations
          - runtime.md#rt-rte-query-answer
          - memory.md#mem-rte-source-passages
          - runtime.md#rt-rte-mcp-answer
          note: Model relevance uses retained catalogue content; lexical search and passage/neighbor ordering
            use retained text, aliases, associations and confidence.
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-index
          - memory.md#mem-obj-concept-entities
          - memory.md#mem-obj-relations
          - runtime.md#rt-rte-query-answer
          note: Catalogue titles, aliases and graph neighbors select delivered pages.
        records:
        - memory.md#mem-obj-index
        - memory.md#mem-obj-concept-entities
        - memory.md#mem-obj-relations
        - runtime.md#rt-rte-query-answer
        - memory.md#mem-rte-source-passages
        - runtime.md#rt-rte-mcp-answer
        note: Ranking inputs need not be learned ranking policies.
      - scope: Checkpoint and cache identity/payload at resume and response consumers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-rte-checkpoint-resume
          - memory.md#mem-rte-response-reuse
          note: Exact checkpoint/key matches select reused results and bypass corresponding inference.
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-rte-checkpoint-resume
          - memory.md#mem-rte-response-reuse
          - memory.md#mem-obj-ingest-chunks
          - memory.md#mem-obj-llm-cache
          note: Stored analysis or response content supplies the result used by downstream derivation/parser
            code.
        records:
        - memory.md#mem-rte-checkpoint-resume
        - memory.md#mem-rte-response-reuse
        - memory.md#mem-obj-ingest-chunks
        - memory.md#mem-obj-llm-cache
        note: Payloads supply prior results, while keys and compatibility fields determine reuse.
      - scope: Metrics/audit and comparison reports at examining operator
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-metric-events
          - runtime.md#rt-rte-compare-eval
          note: Diagnostic activity and evaluation reports inform operator examination.
        records:
        - memory.md#mem-obj-metric-events
        - runtime.md#rt-rte-compare-eval
        note: The recorded later consumer is human inspection, not an automatic winner installer.
      - scope: Injected RAG payload at unknown later consumer
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-rag-embeddings
        note: No consumer is established; storage/add_document alone cannot assign authority.
      records:
      - memory.md#mem-obj-raw-notes
      - memory.md#mem-obj-source-summaries
      - memory.md#mem-obj-synthesis
      - runtime.md#rt-rte-pipeline-run
      - runtime.md#rt-rte-query-answer
      - memory.md#mem-rte-source-passages
      - runtime.md#rt-rte-pack-export
      - runtime.md#rt-bap-rejection-guidance
      - memory.md#mem-obj-rejections
      - runtime.md#rt-bap-pack-guidance
      - memory.md#mem-obj-concept-entities
      - memory.md#mem-rte-identity-rebuild
      - runtime.md#rt-rte-draft-publication
      - memory.md#mem-rte-synthesis-save
      - epistemic.md#epi-rte-synthesis-guard
      - epistemic.md#epi-rte-confidence-score
      - memory.md#mem-obj-index
      - memory.md#mem-obj-relations
      - runtime.md#rt-rte-mcp-answer
      - memory.md#mem-rte-checkpoint-resume
      - memory.md#mem-rte-response-reuse
      - memory.md#mem-obj-ingest-chunks
      - memory.md#mem-obj-llm-cache
      - memory.md#mem-obj-metric-events
      - runtime.md#rt-rte-compare-eval
      - memory.md#mem-obj-rag-embeddings
      note: Distinct retained parts support knowledge, instruction, learning, ranking, routing, validation
        and enforcement. Host-dependent guidance stays afforded; injected-store effects remain unresolved.
    write_agency:
      assessment: partial
      units:
      - scope: Explicit import selection/replacement, draft editing/approval/rejection reasons and identity
          curation
        assessment: known
        findings:
        - value: manual
          basis: wired
          records:
          - memory.md#mem-obj-source-documents
          - memory.md#mem-obj-rejections
          - memory.md#mem-obj-concept-entities
          - runtime.md#rt-rte-draft-publication
          - runtime.md#rt-rte-concept-curation
          - workflow.md#wf-rte-interactive-review
          note: Human supplies source files, feedback/edits, approval or semantic identity decisions.
        records:
        - memory.md#mem-obj-source-documents
        - memory.md#mem-obj-rejections
        - memory.md#mem-obj-concept-entities
        - runtime.md#rt-rte-draft-publication
        - runtime.md#rt-rte-concept-curation
        - workflow.md#wf-rte-interactive-review
        note: These paths require a content-directed operator decision, not merely workflow launch.
      - scope: Analysis, candidate filtering, summaries, drafts, automatic publication, answer saves,
          checkpoints/cache, seed restoration, export and metric retention
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-raw-notes
          - memory.md#mem-obj-source-summaries
          - memory.md#mem-obj-relations
          - runtime.md#rt-rte-pipeline-run
          - runtime.md#rt-rte-draft-publication
          - memory.md#mem-rte-synthesis-save
          - memory.md#mem-rte-checkpoint-resume
          - memory.md#mem-rte-response-reuse
          - memory.md#mem-rte-identity-rebuild
          - runtime.md#rt-rte-pack-export
          - memory.md#mem-obj-metric-events
          note: Software/model admits generated or reconstructed retained content without per-item human
            approval.
        records:
        - memory.md#mem-obj-raw-notes
        - memory.md#mem-obj-source-summaries
        - memory.md#mem-obj-relations
        - runtime.md#rt-rte-pipeline-run
        - runtime.md#rt-rte-draft-publication
        - memory.md#mem-rte-synthesis-save
        - memory.md#mem-rte-checkpoint-resume
        - memory.md#mem-rte-response-reuse
        - memory.md#mem-rte-identity-rebuild
        - runtime.md#rt-rte-pack-export
        - memory.md#mem-obj-metric-events
        note: Starting a run, save flag, clean or export does not approve each subsequently generated
          item.
      - scope: Source import extraction and segment admission after file selection
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-source-documents
          note: Software extracts and persists segments without per-segment approval.
        records:
        - memory.md#mem-obj-source-documents
        note: Separate from the manual decision supplying the original document.
      - scope: Visible optional embedding submission and unknown injected-store admission/initialization
        assessment: partial
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-rag-embeddings
          note: Ingestion automatically chunks, embeds and calls add_document.
        records:
        - memory.md#mem-obj-rag-embeddings
        note: The API write is software driven; internal acceptance/replacement and initial state are
          uninspected.
      - scope: Initial control of externally supplied raw notes and preexisting seed material
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-raw-notes
        - memory.md#mem-obj-concept-entities
        - memory.md#mem-rte-identity-rebuild
        note: External material may be supplied or restored; records do not establish each original admission
          principal.
      records:
      - memory.md#mem-obj-source-documents
      - memory.md#mem-obj-rejections
      - memory.md#mem-obj-concept-entities
      - runtime.md#rt-rte-draft-publication
      - runtime.md#rt-rte-concept-curation
      - workflow.md#wf-rte-interactive-review
      - memory.md#mem-obj-raw-notes
      - memory.md#mem-obj-source-summaries
      - memory.md#mem-obj-relations
      - runtime.md#rt-rte-pipeline-run
      - memory.md#mem-rte-synthesis-save
      - memory.md#mem-rte-checkpoint-resume
      - memory.md#mem-rte-response-reuse
      - memory.md#mem-rte-identity-rebuild
      - runtime.md#rt-rte-pack-export
      - memory.md#mem-obj-metric-events
      - memory.md#mem-obj-rag-embeddings
      note: Manual content decisions and automatic subsequent admission coexist. Unknown initial control
        and injected-store policy prevent complete write coverage.
    curation_operations:
      assessment: partial
      units:
      - scope: Source-derived summaries and concept articles
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-obj-raw-notes
          - memory.md#mem-obj-source-summaries
          - runtime.md#rt-rte-pipeline-run
          note: Analysis summarizes source text and compilation combines selected retained sources into
            reduced article representations.
        records:
        - memory.md#mem-obj-raw-notes
        - memory.md#mem-obj-source-summaries
        - runtime.md#rt-rte-pipeline-run
        note: Source selection and compression are implemented; generated claim fidelity and novelty are
          not observed.
      - scope: Reingestion and recompilation of existing entries; feedback-conditioned revision
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-raw-notes
          - memory.md#mem-obj-source-summaries
          - runtime.md#rt-rte-pipeline-run
          - runtime.md#rt-bap-rejection-guidance
          - memory.md#mem-rte-synthesis-save
          note: Reingestion/recompilation and synthesis update can replace existing retained content.
        records:
        - memory.md#mem-obj-raw-notes
        - memory.md#mem-obj-source-summaries
        - runtime.md#rt-rte-pipeline-run
        - runtime.md#rt-bap-rejection-guidance
        - memory.md#mem-rte-synthesis-save
        note: Known update paths do not establish correct revisions.
      - scope: Explicit merge and alias identity curation
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records:
          - memory.md#mem-obj-concept-entities
          - runtime.md#rt-rte-concept-curation
          note: Merging supplied concept identities removes duplicate live identities and redirects aliases/source
            allocation.
        records:
        - memory.md#mem-obj-concept-entities
        - runtime.md#rt-rte-concept-curation
        note: Known transformations apply to selected identities, not every inverse or semantic equivalence.
      - scope: Publication and retained retirement of generated content
        assessment: known
        findings:
        - value: promote
          basis: wired
          records:
          - runtime.md#rt-rte-draft-publication
          note: Publication raises a retained draft to the published consumption tier.
        - value: invalidate
          basis: wired
          records:
          - runtime.md#rt-rte-concept-curation
          note: Retirement retains old article bodies outside ordinary draft/publication paths while withdrawing
            current use.
        records:
        - runtime.md#rt-rte-draft-publication
        - runtime.md#rt-rte-concept-curation
        note: Tier changes and withdrawal with history are separate operations.
      - scope: Metrics retention/size trimming and checkpoint invalidation
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-obj-metric-events
          note: Configured horizons and size caps remove detailed events/rollups.
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-checkpoint-resume
          note: Stale/corrupt or consumed checkpoints are discarded rather than retained indefinitely.
        records:
        - memory.md#mem-obj-metric-events
        - memory.md#mem-rte-checkpoint-resume
        note: These apply to trace/recovery memory, not a time-decay policy over article knowledge.
      - scope: Novel claim creation, item helpers, relation aggregation and uninspected maintenance inverses
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-rag-embeddings
        - memory.md#mem-obj-relations
        - memory.md#mem-obj-concept-entities
        - epistemic.md#epi-obj-query-answer
        - runtime.md#rt-rte-pipeline-run
        note: A name such as synthesis is insufficient for synthesize; no input/output instance establishes
          novelty. Item admission, aggregation and all inverses are incompletely inspected, and injected-store
          transformations are opaque.
      records:
      - memory.md#mem-obj-raw-notes
      - memory.md#mem-obj-source-summaries
      - runtime.md#rt-rte-pipeline-run
      - runtime.md#rt-bap-rejection-guidance
      - memory.md#mem-rte-synthesis-save
      - memory.md#mem-obj-concept-entities
      - runtime.md#rt-rte-concept-curation
      - runtime.md#rt-rte-draft-publication
      - memory.md#mem-obj-metric-events
      - memory.md#mem-rte-checkpoint-resume
      - memory.md#mem-obj-rag-embeddings
      - memory.md#mem-obj-relations
      - epistemic.md#epi-obj-query-answer
      note: Consolidation, revision, identity deduplication, publication promotion, retirement and trace
        forgetting have local warrants. Index rebuilding or duplicate-key checks alone add no curation
        value; synthesis novelty and opaque alternatives remain unresolved.
    read_back_direction:
      assessment: partial
      units:
      - scope: Question-driven vault/MCP answer context, explicit article/source reads and operator report
          inspection
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-query-answer
          - runtime.md#rt-rte-mcp-answer
          - memory.md#mem-rte-source-passages
          - memory.md#mem-obj-metric-events
          - runtime.md#rt-rte-compare-eval
          note: Request-led retrieval returns selected page slices, source passages or diagnostic artifacts.
        records:
        - runtime.md#rt-rte-query-answer
        - runtime.md#rt-rte-mcp-answer
        - memory.md#mem-rte-source-passages
        - memory.md#mem-obj-metric-events
        - runtime.md#rt-rte-compare-eval
        note: A consumer requests retained material or an answer using it; automatic delivery within that
          request is not a second unsolicited push.
      - scope: 'Compiler/ingestion automatic auxiliary context: concept hints and recent rejection feedback'
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-pipeline-run
          - runtime.md#rt-bap-rejection-guidance
          - memory.md#mem-obj-rejections
          note: Code selects bounded concept hints and up to three feedback strings into model prompts.
        records:
        - runtime.md#rt-rte-pipeline-run
        - runtime.md#rt-bap-rejection-guidance
        - memory.md#mem-obj-rejections
        note: A run/compile trigger causes selectors to supply prior hints/feedback without a separate
          request for those retained parts.
      - scope: Automatic checkpoint and exact response reuse on later ingestion/inference attempts
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-checkpoint-resume
          - memory.md#mem-rte-response-reuse
          note: Matching saved analyses/cache strings are supplied automatically before fresh calls.
        records:
        - memory.md#mem-rte-checkpoint-resume
        - memory.md#mem-rte-response-reuse
        note: The caller requests work or inference; automatic selectors substitute compatible retained
          prior results.
      - scope: Identity seed restore on later ingest
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-identity-rebuild
          note: Available compatible seed state is automatically restored into subsequent normalization
            state.
        records:
        - memory.md#mem-rte-identity-rebuild
        note: Code selects preserved identities and constraints into reconstruction without a per-row
          read request.
      - scope: Exported pack consumption under generated guidance
        assessment: partial
        findings:
        - value: pull
          basis: afforded
          records:
          - runtime.md#rt-rte-pack-export
          - runtime.md#rt-bap-pack-guidance
          note: PackReader or external readers can reopen exported retained content.
        records:
        - runtime.md#rt-rte-pack-export
        - runtime.md#rt-bap-pack-guidance
        note: Files permit later requested inspection; host startup injection is not established.
      - scope: Injected RAG later consumer
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-rag-embeddings
        note: Only the write is established; neither requested recall nor automatic supply is classified.
      records:
      - runtime.md#rt-rte-query-answer
      - runtime.md#rt-rte-mcp-answer
      - memory.md#mem-rte-source-passages
      - memory.md#mem-obj-metric-events
      - runtime.md#rt-rte-compare-eval
      - runtime.md#rt-rte-pipeline-run
      - runtime.md#rt-bap-rejection-guidance
      - memory.md#mem-obj-rejections
      - memory.md#mem-rte-checkpoint-resume
      - memory.md#mem-rte-response-reuse
      - memory.md#mem-rte-identity-rebuild
      - runtime.md#rt-rte-pack-export
      - runtime.md#rt-bap-pack-guidance
      - memory.md#mem-obj-rag-embeddings
      note: Request-led query/source consumption and automatic auxiliary/recovery selection coexist. Pack
        host behavior and optional store recall remain unresolved.
    read_back_signal:
      assessment: partial
      units:
      - scope: 'Compilation/ingestion trigger: concept hints selected from retained concepts using current
          body/title matches and caps'
        assessment: known
        findings:
        - value: inferred-lexical
          basis: wired
          records:
          - runtime.md#rt-rte-pipeline-run
          note: Current body/title lexical matches favor retained concept hints.
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-pipeline-run
          note: Availability and capped hint/title lists bound delivered auxiliary context.
        records:
        - runtime.md#rt-rte-pipeline-run
        note: Targeted lexical matching is separate from the coarse list budget.
      - scope: 'Recompile trigger: latest feedback strings for the current concept'
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-obj-rejections
          - runtime.md#rt-bap-rejection-guidance
          - runtime.md#rt-rte-draft-publication
          note: Concept identity matches feedback delivered to the writer.
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-rejections
          - runtime.md#rt-rte-draft-publication
          note: Recent-three selection and deduplication bound feedback strings; rejected bodies are not
            injected.
        records:
        - memory.md#mem-obj-rejections
        - runtime.md#rt-bap-rejection-guidance
        - runtime.md#rt-rte-draft-publication
        note: The concept key selects the retained rejection records; recency and the three-record bound
          are separate.
      - scope: 'Ingest restart trigger: compatible saved analysis units'
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-checkpoint-resume
          - memory.md#mem-obj-ingest-chunks
          note: Source path, checkpoint hash, chunk shape and schema select retained AnalysisResult units.
        records:
        - memory.md#mem-rte-checkpoint-resume
        - memory.md#mem-obj-ingest-chunks
        note: A compound identity match actually selects reused payloads.
      - scope: 'Inference request trigger: exact-key response substitution'
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-response-reuse
          - memory.md#mem-obj-llm-cache
          note: Digest of namespace, model and sorted messages selects the returned retained response.
        records:
        - memory.md#mem-rte-response-reuse
        - memory.md#mem-obj-llm-cache
        note: No similarity lookup is implemented in this cache.
      - scope: 'Later ingest trigger: preserved identity seed restoration'
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-identity-rebuild
          - memory.md#mem-obj-index
          note: Available valid seed content supplies the restoration inventory.
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-identity-rebuild
          - memory.md#mem-obj-index
          note: Identity/source bindings and existing DB identities determine which retained identities
            are reconstructed.
        records:
        - memory.md#mem-rte-identity-rebuild
        - memory.md#mem-obj-index
        note: Selection reads available seed entries and restores identities while respecting existing
          entities.
      - scope: Opaque injected-store selection and external pack host injection
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-rag-embeddings
        - runtime.md#rt-bap-pack-guidance
        note: No selector/input/delivered-part chain establishes a push signal on these alternatives.
      records:
      - runtime.md#rt-rte-pipeline-run
      - memory.md#mem-obj-rejections
      - runtime.md#rt-bap-rejection-guidance
      - runtime.md#rt-rte-draft-publication
      - memory.md#mem-rte-checkpoint-resume
      - memory.md#mem-obj-ingest-chunks
      - memory.md#mem-rte-response-reuse
      - memory.md#mem-obj-llm-cache
      - memory.md#mem-rte-identity-rebuild
      - memory.md#mem-obj-index
      - memory.md#mem-obj-rag-embeddings
      - runtime.md#rt-bap-pack-guidance
      note: Push signals classify actual auxiliary/resume/cache selectors, not IDs on requested source
        files. Query model relevance and BM25 belong to request-led pull routes, not inferred push signals.
    trace_learning:
      assessment: partial
      units:
      - scope: Retained human draft criticism to automatic revised article to later answer/export consumers
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-rejections
          - runtime.md#rt-bap-rejection-guidance
          - runtime.md#rt-rte-pipeline-run
          - runtime.md#rt-rte-draft-publication
          - runtime.md#rt-rte-query-answer
          note: Recorded review experience conditions durable article revision later usable as context;
            no demonstrated improvement or model-weight update is required.
        records:
        - memory.md#mem-obj-rejections
        - runtime.md#rt-bap-rejection-guidance
        - runtime.md#rt-rte-pipeline-run
        - runtime.md#rt-rte-draft-publication
        - runtime.md#rt-rte-query-answer
        note: The per-content feedback write is manual, but subsequent feedback-fed article generation/retention
          is automatic and behavior-shaping across invocations.
      - scope: Checkpoint analysis and response reuse
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-checkpoint-resume
        - memory.md#mem-rte-response-reuse
        - memory.md#mem-obj-ingest-chunks
        - memory.md#mem-obj-llm-cache
        note: These are automatic trace-fed retention routes with later consumers. Records describe replay/merge,
          but do not fully resolve whether each retained result and subsequent derived artifact qualifies
          as a behavior-shaping update rather than unchanged result reuse.
      - scope: Metrics/audit and comparison reporting
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-metric-events
        - runtime.md#rt-rte-compare-eval
        note: Known traces reach operator reports; no automatic production-update consumer is established.
          Records do not declare a bounded absence across every downstream human-mediated use.
      - scope: Source-derived knowledge and optional RAG inputs
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-source-documents
        - memory.md#mem-obj-raw-notes
        - memory.md#mem-obj-rag-embeddings
        note: External raw-note contents/origins and injected-store later consumers are unresolved. Source
          import alone is not evidence of trace learning, nor of its absence.
      records:
      - memory.md#mem-obj-rejections
      - runtime.md#rt-bap-rejection-guidance
      - runtime.md#rt-rte-pipeline-run
      - runtime.md#rt-rte-draft-publication
      - runtime.md#rt-rte-query-answer
      - memory.md#mem-rte-checkpoint-resume
      - memory.md#mem-rte-response-reuse
      - memory.md#mem-obj-ingest-chunks
      - memory.md#mem-obj-llm-cache
      - memory.md#mem-obj-metric-events
      - runtime.md#rt-rte-compare-eval
      - memory.md#mem-obj-source-documents
      - memory.md#mem-obj-raw-notes
      - memory.md#mem-obj-rag-embeddings
      note: A wired review-feedback revision chain supports yes locally. Checkpoint/cache qualification,
        external source origins and optional-store behavior prevent a complete trace-learning inventory;
        no system-wide no is inferred.
    trace_source:
      assessment: not-determinable
      units:
      - scope: Human draft-review experience recorded as rejection feedback, feeding automatic later article
          revision
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-rejections
        - runtime.md#rt-bap-rejection-guidance
        - workflow.md#wf-rte-interactive-review
        note: This is review activity feedback, not a retained conversational session transcript or a
          demonstrated trajectory. Controlled origin cannot be resolved more finely from these records.
      - scope: Checkpoint/cache results and unresolved external or optional-store trace-fed routes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-checkpoint-resume
        - memory.md#mem-rte-response-reuse
        - memory.md#mem-obj-raw-notes
        - memory.md#mem-obj-rag-embeddings
        note: Prior model outputs are retained, but the records do not establish qualifying original session-log/tool-trace/event-stream/trajectory
          content for every possible update; unknown source-note origins stay local.
      records:
      - memory.md#mem-obj-rejections
      - runtime.md#rt-bap-rejection-guidance
      - workflow.md#wf-rte-interactive-review
      - memory.md#mem-rte-checkpoint-resume
      - memory.md#mem-rte-response-reuse
      - memory.md#mem-obj-raw-notes
      - memory.md#mem-obj-rag-embeddings
      note: A qualifying review-fed write does not itself identify one of the four controlled source classes.
        Human criticism is not automatically a session log or timestamped event stream. No source value
        is asserted without a record establishing original content and origin.
---

# Synto memory profile

## Comparison rationale

This classification uses accepted records and their memory annotations. No target source was reread and no new evidence was added. Reconciliation supplies no supersession: containers and narrower parts remain canonical. The findings describe implementation or afforded later host consumption, not observed operation or causal benefit.

### Objects, provenance and control

SQLite and files are distinct persistence substrates; retained relations also provide graph organization. Dense embedding arguments establish numerical form, not an inspected vector backend. The injected store remains in the inventory on every affected axis rather than disappearing behind a known file/SQLite witness. See [MEM-OBJ-rag-embeddings](memory.md#mem-obj-rag-embeddings) and [MEM-OBJ-relations](memory.md#mem-obj-relations). Provider inference weights are outside this use-accumulated memory boundary, not an asserted negative about provider learning.

Imported notes, model/code-derived knowledge, authored human criticism and captured call/activity outputs have different derivation paths. Admission is independent: a human can supply an import or reject a draft while software admits extracted segments or a feedback-conditioned rewrite. Save flags similarly enable automatic content admission. Initial external/seed provenance and injected-store control remain unresolved. See [MEM-OBJ-source-documents](memory.md#mem-obj-source-documents), [MEM-OBJ-rejections](memory.md#mem-obj-rejections) and [MEM-RTE-synthesis-save](memory.md#mem-rte-synthesis-save).

### Consumer effects and retrieval

Feedback has instructional authority at the writer and learning authority at the durable-revision update consumer; the resulting article supplies knowledge at later answering. These are separate effects, neither demonstrating better capacity. Identity denials can both validate a candidate and enforce its rejection. Retained catalogue text, aliases and relation confidence are ranking/routing inputs even when scoring code is fixed. Generated pack guidance has only afforded instruction/routing force at the excluded host; file generation alone does not prove host loading. See [RT-BAP-rejection-guidance](runtime.md#rt-bap-rejection-guidance), [MEM-OBJ-concept-entities](memory.md#mem-obj-concept-entities), [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) and [RT-BAP-pack-guidance](runtime.md#rt-bap-pack-guidance).

A question requests retained page context, and source tools explicitly request passages: those chains are pull. Automatically supplied concept hints, rejection feedback and compatible prior results are separate push operations. Exact cache/checkpoint identity matching selects delivered payloads; merely returning a requested segment ID does not establish identifier-based push. No opaque RAG selector is inferred from the visible write. See [MEM-RTE-source-passages](memory.md#mem-rte-source-passages), [MEM-RTE-checkpoint-resume](memory.md#mem-rte-checkpoint-resume) and [MEM-RTE-response-reuse](memory.md#mem-rte-response-reuse).

### Transformations and uncertainty

Consolidation describes retained-source compression, not guaranteed faithful generation. The source-native synthesis command does not establish the controlled curation value synthesize without recorded novel-claim evidence. Merge supplies a local identity-deduplication witness; publication raises a draft tier; retirement withdraws live use while retaining bodies. No universal retraction or full-state rollback follows. See [RT-RTE-concept-curation](runtime.md#rt-rte-concept-curation), [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication) and [EPI-OBJ-query-answer](epistemic.md#epi-obj-query-answer).

Ordinary Q&A remains filesystem/export-accessible and title-resolvable, but refreshing the index does not enumerate that tree. Synthesis has explicit later catalogue admission subject to the newest-25 limit. This accepted qualification changes neither record identity nor the positive later-consumer routes. See [EPI-RTE-answer-retention](epistemic.md#epi-rte-answer-retention), [MEM-OBJ-synthesis](memory.md#mem-obj-synthesis) and [MEM-OBJ-index](memory.md#mem-obj-index).

The review-feedback chain supports trace learning as an automatic experience-fed durable revision, not exercised self-improvement. Its source is human criticism of a generated draft; the records do not establish that criticism as a conversational session log, recorded tool request/result, timestamped runtime event stream or linked state/action/outcome trajectory. Trace source therefore remains not-determinable instead of manufacturing an event-stream label. Cache/checkpoint reuse and metrics reports also retain their unresolved qualification and consumer limits; raw activity retention alone does not warrant a learning union. See [WF-RTE-interactive-review](workflow.md#wf-rte-interactive-review), [RT-BAP-rejection-guidance](runtime.md#rt-bap-rejection-guidance), [MEM-RTE-response-reuse](memory.md#mem-rte-response-reuse) and [MEM-OBJ-metric-events](memory.md#mem-obj-metric-events).
