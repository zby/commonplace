---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Memory profile of IsaacCLupus_mnemosyn_spec: proposed retained knowledge and conversation/feedback
  routes versus legacy publication and opaque backends.'
run-id: AAS-2026-10-15-isaacclupus-mnemosyn-spec-1887e13dcc13-01
source-identity: https://github.com/noirblue/IsaacCLupus_mnemosyn_spec
reviewed-boundary: 0fda14eb33d2fc01a4e3969a9ab487b22c4f9d92
memory-comparison:
  version: 2
  scope: 'Included: use-accumulated raw/draft/published/committed pages; normalized legacy vault and optional
    Git history; conversations, profile facts, rejection feedback, metadata and draft governance; graph access
    views, packs and optional proof outputs; their admission, maintenance and later-consumer routes. External
    Link/LLM-WIKI retained state and history, optional embedding/reranking state, response cache and provider-retained
    state remain included unresolved alternatives at their recorded interfaces. Excluded: shipped static templates/configuration/AGENTS
    instructions, configured model weights without an established use-fed update, and volatile current-request
    proxy queues. Proposed unified OS, draft extensions/studies and wired legacy bridge remain distinct evidence
    layers.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Legacy normalized Markdown and optional version history
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-unified-vault
          - runtime.md#rt-rte-vault-publish
          note: Normalized pages are written to the unified-vault filesystem.
        - value: repo
          basis: wired
          records:
          - runtime.md#rt-rte-vault-publish
          note: Publication optionally commits the unified files to Git; this is a conditional implemented
            history route.
        records:
        - memory.md#mem-obj-unified-vault
        - runtime.md#rt-rte-vault-publish
        note: Files are wired outputs; Git history is conditional on publication configuration and command
          success, not observed.
      - scope: Proposed raw, draft, published and committed page bodies; rejection text and page metadata
        assessment: known
        findings:
        - value: files
          basis: claimed
          records:
          - memory.md#mem-obj-vault-pages
          note: Markdown bodies reside in vault directories.
        - value: sqlite
          basis: claimed
          records:
          - memory.md#mem-obj-vault-pages
          - memory.md#mem-obj-rejection-feedback
          note: Page metadata and rejection_feedback reside in proposed state.db.
        records:
        - memory.md#mem-obj-vault-pages
        - memory.md#mem-obj-rejection-feedback
        note: Filesystem page bodies and SQLite page fields are the recorded proposed storage split.
      - scope: Conversation, profile, link, job, audit, contradiction and draft governance rows
        assessment: known
        findings:
        - value: sqlite
          basis: claimed
          records:
          - memory.md#mem-obj-conversations
          - memory.md#mem-obj-user-profiles
          - memory.md#mem-obj-state-metadata
          - epistemic.md#epi-obj-governance-state
          note: Initial tables and later profile/governance additions describe retained SQLite state.
        records:
        - memory.md#mem-obj-conversations
        - memory.md#mem-obj-user-profiles
        - memory.md#mem-obj-state-metadata
        - epistemic.md#epi-obj-governance-state
        note: DDL and proposed additions specify SQLite, without establishing populated runtime state.
      - scope: Reconstructed knowledge-graph access view
        assessment: known
        findings:
        - value: graph
          basis: claimed
          records:
          - memory.md#mem-obj-knowledge-graph
          note: Published-page nodes and relations form the graph access structure.
        - value: in-memory
          basis: claimed
          records:
          - memory.md#mem-obj-knowledge-graph
          note: The graph is rebuilt in RAM from SQLite on startup.
        records:
        - memory.md#mem-obj-knowledge-graph
        note: Graph topology and RAM residence are separate supported properties of the proposed view.
      - scope: Exported articles, index, navigation, manifest and optional proof serialization
        assessment: known
        findings:
        - value: files
          basis: claimed
          records:
          - memory.md#mem-obj-agent-pack
          - memory.md#mem-rte-pack-export
          - epistemic.md#epi-rte-proof-export
          note: Pack directories retain copied articles and generated access/provenance artifacts.
        records:
        - memory.md#mem-obj-agent-pack
        - memory.md#mem-rte-pack-export
        - epistemic.md#epi-rte-proof-export
        note: Ordinary pack files and optional draft proof output remain design-level storage.
      - scope: External Link/LLM-WIKI state, optional embedding storage, response cache and provider-retained
          state
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-link-remember
        - runtime.md#rt-rte-client-query
        - memory.md#mem-obj-state-metadata
        - runtime.md#rt-rte-model-proxy
        note: Payloads, backend storage and cache/embedding implementations are unresolved; neither service-object
          nor vector nor model-weights follows from endpoint names or model aliases.
      records:
      - memory.md#mem-obj-unified-vault
      - runtime.md#rt-rte-vault-publish
      - memory.md#mem-obj-vault-pages
      - memory.md#mem-obj-rejection-feedback
      - memory.md#mem-obj-conversations
      - memory.md#mem-obj-user-profiles
      - memory.md#mem-obj-state-metadata
      - epistemic.md#epi-obj-governance-state
      - memory.md#mem-obj-knowledge-graph
      - memory.md#mem-obj-agent-pack
      - memory.md#mem-rte-pack-export
      - epistemic.md#epi-rte-proof-export
      - runtime.md#rt-rte-link-remember
      - runtime.md#rt-rte-client-query
      - runtime.md#rt-rte-model-proxy
      note: The inventory covers proposed retained content/access state and legacy publication. External backend
        state, cache and optional embedding storage prevent a complete substrate classification.
    representational_form:
      assessment: partial
      units:
      - scope: Legacy copied page bodies
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-unified-vault
          note: Copied assertions remain readable Markdown body content.
        records:
        - memory.md#mem-obj-unified-vault
        note: The normalizer preserves the natural-language body.
      - scope: Legacy normalized frontmatter at copying/indexing boundary
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-unified-vault
          - runtime.md#rt-rte-vault-publish
          note: Fixed code transforms and writes selected metadata keys.
        records:
        - memory.md#mem-obj-unified-vault
        - runtime.md#rt-rte-vault-publish
        note: Selected keys and deterministic maturity labels are symbolic; downstream backend interpretation
          is unresolved.
      - scope: Proposed raw/page/article/profile/conversation/rejection/contradiction/governance text
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records:
          - memory.md#mem-obj-vault-pages
          - memory.md#mem-obj-conversations
          - memory.md#mem-obj-user-profiles
          - memory.md#mem-obj-rejection-feedback
          - memory.md#mem-obj-state-metadata
          - epistemic.md#epi-obj-governance-state
          - epistemic.md#epi-obj-article-output
          note: Assertions, conversation messages, criticism and rationale are interpreted text.
        records:
        - memory.md#mem-obj-vault-pages
        - memory.md#mem-obj-conversations
        - memory.md#mem-obj-user-profiles
        - memory.md#mem-obj-rejection-feedback
        - memory.md#mem-obj-state-metadata
        - epistemic.md#epi-obj-governance-state
        - epistemic.md#epi-obj-article-output
        note: This unit names textual parts only, not their containers or opaque job payloads.
      - scope: Proposed IDs, stages, counters, heat, hashes, link topology, governance statuses and pack indexes
        assessment: known
        findings:
        - value: symbolic
          basis: claimed
          records:
          - memory.md#mem-obj-vault-pages
          - memory.md#mem-obj-conversations
          - memory.md#mem-obj-user-profiles
          - memory.md#mem-obj-state-metadata
          - memory.md#mem-obj-knowledge-graph
          - memory.md#mem-obj-agent-pack
          - epistemic.md#epi-obj-governance-state
          note: Localized fields and relations support fixed selection, tracking and navigation rules.
        records:
        - memory.md#mem-obj-vault-pages
        - memory.md#mem-obj-conversations
        - memory.md#mem-obj-user-profiles
        - memory.md#mem-obj-state-metadata
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-obj-agent-pack
        - epistemic.md#epi-obj-governance-state
        note: Fixed-rule metadata is distinct from relationship descriptions and article bodies.
      - scope: Proposed graph edge context and exported article/navigation text
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records:
          - memory.md#mem-obj-knowledge-graph
          - memory.md#mem-obj-agent-pack
          - memory.md#mem-bap-query-knowledge
          note: Relationship descriptions, knowledge articles and generated agent navigation are text.
        records:
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-obj-agent-pack
        - memory.md#mem-bap-query-knowledge
        note: Only readable parts are classified here; index fields are classified separately.
      - scope: Opaque job payload/results, external retained memory/history, cache, optional embeddings and
          provider state
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-state-metadata
        - runtime.md#rt-rte-link-remember
        - runtime.md#rt-rte-client-query
        - runtime.md#rt-rte-model-proxy
        note: Serialization or a readable returned summary does not resolve the operative payload. No use-updated
          numerical memory is established; shipped model components are excluded from this memory inventory.
      records:
      - memory.md#mem-obj-unified-vault
      - runtime.md#rt-rte-vault-publish
      - memory.md#mem-obj-vault-pages
      - memory.md#mem-obj-conversations
      - memory.md#mem-obj-user-profiles
      - memory.md#mem-obj-rejection-feedback
      - memory.md#mem-obj-state-metadata
      - epistemic.md#epi-obj-governance-state
      - epistemic.md#epi-obj-article-output
      - memory.md#mem-obj-knowledge-graph
      - memory.md#mem-obj-agent-pack
      - memory.md#mem-bap-query-knowledge
      - runtime.md#rt-rte-link-remember
      - runtime.md#rt-rte-client-query
      - runtime.md#rt-rte-model-proxy
      note: Known text and fixed-rule access parts coexist with opaque backend/cache/embedding content. Display
        output cannot classify full consumed payloads.
    lineage:
      assessment: partial
      units:
      - scope: 'Legacy unified pages: immediate external-vault import'
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-unified-vault
          - runtime.md#rt-rte-vault-publish
          note: Pages enter from Synto/Synthadoc wiki files.
        records:
        - memory.md#mem-obj-unified-vault
        - runtime.md#rt-rte-vault-publish
        note: This is local acquisition lineage, not a claim about original raw authorship.
      - scope: 'Legacy selected frontmatter: local deterministic transformation'
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-unified-vault
          - epistemic.md#epi-rte-maturity-mapping
          note: Confidence/status and selected fields are transformed into normalized metadata.
        records:
        - memory.md#mem-obj-unified-vault
        - epistemic.md#epi-rte-maturity-mapping
        note: Metadata normalization is a compiled derivation; body reasons are not reconstructed.
      - scope: Proposed external raw-source acquisition
        assessment: known
        findings:
        - value: imported
          basis: claimed
          records:
          - memory.md#mem-obj-vault-pages
          - epistemic.md#epi-rte-article-generation
          note: External source assertions enter retained raw material.
        records:
        - memory.md#mem-obj-vault-pages
        - epistemic.md#epi-rte-article-generation
        note: Only the acquisition path is resolved; raw sources need not be interaction traces.
      - scope: Proposed generated articles, graph view, file packs and proof serialization
        assessment: known
        findings:
        - value: other-compiled
          basis: claimed
          records:
          - epistemic.md#epi-rte-article-generation
          - memory.md#mem-obj-knowledge-graph
          - memory.md#mem-obj-agent-pack
          - epistemic.md#epi-rte-proof-export
          note: Generation, graph reconstruction and export derive representations from earlier retained inputs.
        records:
        - epistemic.md#epi-rte-article-generation
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-obj-agent-pack
        - epistemic.md#epi-rte-proof-export
        note: Model/program derivation is specified even though semantic fidelity and successful execution
          are not.
      - scope: Conversation-derived facts and memory proposals
        assessment: known
        findings:
        - value: trace-extracted
          basis: claimed
          records:
          - memory.md#mem-obj-conversations
          - memory.md#mem-obj-user-profiles
          - memory.md#mem-rte-conversation-promotion
          note: The fast model extracts facts and proposals from conversation logs.
        records:
        - memory.md#mem-obj-conversations
        - memory.md#mem-obj-user-profiles
        - memory.md#mem-rte-conversation-promotion
        note: The proposed derivation path consumes recorded turns; direct profile visibility remains unresolved.
      - scope: Retained rejection feedback and subsequent article rewrite
        assessment: partial
        findings:
        - value: trace-extracted
          basis: claimed
          records:
          - memory.md#mem-obj-rejection-feedback
          - memory.md#mem-rte-feedback-recompile
          note: Persisted rejection criticism carries audit feedback into a later writer.
        - value: other-compiled
          basis: claimed
          records:
          - memory.md#mem-rte-feedback-recompile
          note: The writer produces another article from source material and prior criticism.
        records:
        - memory.md#mem-obj-rejection-feedback
        - memory.md#mem-rte-feedback-recompile
        note: Criticism derives from audit experience and feeds rewriting; whether every raw audit reason is
          copied is unresolved.
      - scope: Initial page/proposal authorship; raw turn acquisition; profile/governance input provenance;
          opaque backend/cache/embedding origins
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-vault-pages
        - memory.md#mem-obj-conversations
        - memory.md#mem-obj-user-profiles
        - epistemic.md#epi-obj-governance-state
        - runtime.md#rt-rte-link-remember
        - runtime.md#rt-rte-client-query
        - memory.md#mem-obj-state-metadata
        note: The records do not establish all initial producers, external content origins or embedding derivations.
          Generic caller identity does not establish authored lineage.
      records:
      - memory.md#mem-obj-unified-vault
      - runtime.md#rt-rte-vault-publish
      - epistemic.md#epi-rte-maturity-mapping
      - memory.md#mem-obj-vault-pages
      - epistemic.md#epi-rte-article-generation
      - memory.md#mem-obj-knowledge-graph
      - memory.md#mem-obj-agent-pack
      - epistemic.md#epi-rte-proof-export
      - memory.md#mem-obj-conversations
      - memory.md#mem-obj-user-profiles
      - memory.md#mem-rte-conversation-promotion
      - memory.md#mem-obj-rejection-feedback
      - memory.md#mem-rte-feedback-recompile
      - epistemic.md#epi-obj-governance-state
      - runtime.md#rt-rte-link-remember
      - runtime.md#rt-rte-client-query
      - memory.md#mem-obj-state-metadata
      note: Recorded local copying and compilation paths are retained separately from unknown initial content,
        semantic derivation and embedding provenance.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Published page bodies and graph relationship context at proposed query/compilation consumers
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records:
          - memory.md#mem-obj-vault-pages
          - memory.md#mem-rte-graph-context
          - memory.md#mem-bap-query-knowledge
          - runtime.md#rt-rte-design-lifecycle
          note: Retained source/related pages and graph context inform later compilation or answering.
        records:
        - memory.md#mem-obj-vault-pages
        - memory.md#mem-rte-graph-context
        - memory.md#mem-bap-query-knowledge
        - runtime.md#rt-rte-design-lifecycle
        note: Knowledge supply is proposed; delivery does not establish model compliance.
      - scope: Exported article bodies at documented file-aware agents
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-rte-pack-export
          - memory.md#mem-bap-query-knowledge
          note: Agents may import and read retained exported knowledge.
        records:
        - memory.md#mem-obj-agent-pack
        - memory.md#mem-rte-pack-export
        - memory.md#mem-bap-query-knowledge
        note: The external consumer role is afforded, not deployed wiring.
      - scope: Persisted rejection criticism at ArticleWriter update consumer
        assessment: known
        findings:
        - value: instruction
          basis: claimed
          records:
          - memory.md#mem-rte-feedback-recompile
          - memory.md#mem-bap-feedback-guidance
          note: Previous criticism directs the next rewrite.
        - value: learning
          basis: claimed
          records:
          - memory.md#mem-obj-rejection-feedback
          - memory.md#mem-rte-feedback-recompile
          note: Retained evaluation experience feeds an update to a durable article.
        records:
        - memory.md#mem-obj-rejection-feedback
        - memory.md#mem-rte-feedback-recompile
        - memory.md#mem-bap-feedback-guidance
        note: Update force and prompt force coexist; neither establishes improved capacity.
      - scope: Recorded conversation turns at fact-extraction consumer
        assessment: known
        findings:
        - value: learning
          basis: claimed
          records:
          - memory.md#mem-obj-conversations
          - memory.md#mem-rte-conversation-promotion
          note: Logged conversational experience supplies the proposed durable-fact update.
        records:
        - memory.md#mem-obj-conversations
        - memory.md#mem-rte-conversation-promotion
        note: This force belongs to the raw experience at the update consumer, not an assumed profile prompt
          injection.
      - scope: Heat/reference state at promotion and cold-retention selector
        assessment: known
        findings:
        - value: ranking
          basis: claimed
          records:
          - memory.md#mem-rte-conversation-promotion
          note: Heat affects which retained material receives promotion priority.
        - value: routing
          basis: claimed
          records:
          - memory.md#mem-rte-conversation-promotion
          note: Hot/cold state selects promotion or archival handling.
        records:
        - memory.md#mem-rte-conversation-promotion
        - memory.md#mem-obj-conversations
        note: Heat represents relevance, not factual acceptance.
      - scope: Rejected-count and hand-edit/hash state at proposed scheduler
        assessment: known
        findings:
        - value: validation
          basis: claimed
          records:
          - memory.md#mem-rte-feedback-recompile
          note: Counter/approval and hand-edit conditions test retry eligibility.
        - value: enforcement
          basis: claimed
          records:
          - memory.md#mem-rte-feedback-recompile
          note: Repeated-rejection or protected-page conditions block scheduling.
        - value: routing
          basis: claimed
          records:
          - memory.md#mem-rte-feedback-recompile
          note: Eligible affected concepts select subsequent compilation work.
        records:
        - memory.md#mem-rte-feedback-recompile
        note: The scheduler tests retained state before queuing another compilation; deployed plumbing remains
          absent from these sketches.
      - scope: Published-stage/page-ID/link state at proposed graph/export selectors
        assessment: known
        findings:
        - value: routing
          basis: claimed
          records:
          - memory.md#mem-obj-knowledge-graph
          - memory.md#mem-rte-graph-context
          - memory.md#mem-rte-pack-export
          note: Stage, primary page identity and graph relations select export/query inputs.
        records:
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-rte-graph-context
        - memory.md#mem-rte-pack-export
        note: Fixed selection fields determine included material rather than factual truth.
      - scope: Direct profile consumption, governance verdict effects, backend ranking/retrieval, cache and
          optional embedding consumers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-user-profiles
        - epistemic.md#epi-obj-governance-state
        - epistemic.md#epi-rte-claim-governance
        - runtime.md#rt-rte-link-remember
        - runtime.md#rt-rte-client-query
        - memory.md#mem-obj-state-metadata
        note: No settled profile delivery or inspected backend force is established. Stored metadata or trust
          labels alone cannot establish instruction, validation or enforcement authority.
      records:
      - memory.md#mem-obj-vault-pages
      - memory.md#mem-rte-graph-context
      - memory.md#mem-bap-query-knowledge
      - runtime.md#rt-rte-design-lifecycle
      - memory.md#mem-obj-agent-pack
      - memory.md#mem-rte-pack-export
      - memory.md#mem-obj-rejection-feedback
      - memory.md#mem-rte-feedback-recompile
      - memory.md#mem-bap-feedback-guidance
      - memory.md#mem-obj-conversations
      - memory.md#mem-rte-conversation-promotion
      - memory.md#mem-obj-knowledge-graph
      - memory.md#mem-obj-user-profiles
      - epistemic.md#epi-obj-governance-state
      - epistemic.md#epi-rte-claim-governance
      - runtime.md#rt-rte-link-remember
      - runtime.md#rt-rte-client-query
      - memory.md#mem-obj-state-metadata
      note: Authority follows actual proposed or wired consumers, not labels. Profile delivery, opaque backends,
        cache/embeddings and unconsumed governance metadata leave coverage partial.
    write_agency:
      assessment: partial
      units:
      - scope: Legacy per-page publication/copy/overwrite admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-vault-publish
          - memory.md#mem-obj-unified-vault
          note: Recursive copy and normalization admit retained content through code.
        records:
        - runtime.md#rt-rte-vault-publish
        - memory.md#mem-obj-unified-vault
        note: The caller starts a workflow; fixed software chooses and writes each page without per-page approval.
      - scope: Proposed conversation extraction and daily maintenance admission
        assessment: partial
        findings:
        - value: automatic
          basis: claimed
          records:
          - memory.md#mem-rte-conversation-promotion
          note: The fast model and background heat/decay process produce/update retained facts and candidates.
        records:
        - memory.md#mem-rte-conversation-promotion
        - memory.md#mem-obj-user-profiles
        note: Automatic extraction/promotion is specified; separate profile-row veto/control is not.
      - scope: Proposed explicit human commitment of promoted memories
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records:
          - memory.md#mem-rte-conversation-promotion
          note: A human approves promoted candidates into committed memory.
        records:
        - memory.md#mem-rte-conversation-promotion
        note: This is the distinct final approval mechanism, not the preceding automatic extraction.
      - scope: Proposed configurable article and explicit-memory approval
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records:
          - runtime.md#rt-rte-design-lifecycle
          - memory.md#mem-rte-memory-lifecycle
          - epistemic.md#epi-rte-article-disposition
          note: Configured human approval can admit or veto specific content.
        - value: automatic
          basis: claimed
          records:
          - runtime.md#rt-rte-design-lifecycle
          - memory.md#mem-rte-memory-lifecycle
          - epistemic.md#epi-rte-article-disposition
          note: Score threshold or configured auto-approval can admit content without a per-content human decision.
        records:
        - runtime.md#rt-rte-design-lifecycle
        - memory.md#mem-rte-memory-lifecycle
        - epistemic.md#epi-rte-article-disposition
        note: Human and configured automatic alternatives remain distinct findings at the same claimed evidence
          layer.
      - scope: Proposed feedback-guided writing, graph reconstruction and pack generation
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records:
          - memory.md#mem-rte-feedback-recompile
          - memory.md#mem-obj-knowledge-graph
          - memory.md#mem-rte-pack-export
          note: Writer, graph builder and exporter derive retained outputs by software/model decisions.
        records:
        - memory.md#mem-rte-feedback-recompile
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-rte-pack-export
        note: Software/model transformations are automatic even when an operator initiates recompilation or
          export.
      - scope: Draft claim-level human verdict admission
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records:
          - epistemic.md#epi-rte-claim-governance
          note: Human endorsement/rejection controls proposed claim admission.
        records:
        - epistemic.md#epi-rte-claim-governance
        note: The future governance gate expressly assigns content verdicts to humans.
      - scope: Initial retained content, conversation logging control, external ingest/compile and Link HTTP
          versus CLI fallback; cache/embedding writes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-vault-pages
        - memory.md#mem-obj-conversations
        - runtime.md#rt-rte-foundry-tools
        - runtime.md#rt-rte-link-remember
        - memory.md#mem-obj-state-metadata
        note: Generic caller content and unknown backend admission do not establish human decisions or automatic
          admission; HTTP/fallback scope differs and neither resolves this missing fact.
      records:
      - runtime.md#rt-rte-vault-publish
      - memory.md#mem-obj-unified-vault
      - memory.md#mem-rte-conversation-promotion
      - memory.md#mem-obj-user-profiles
      - runtime.md#rt-rte-design-lifecycle
      - memory.md#mem-rte-memory-lifecycle
      - epistemic.md#epi-rte-article-disposition
      - memory.md#mem-rte-feedback-recompile
      - memory.md#mem-obj-knowledge-graph
      - memory.md#mem-rte-pack-export
      - epistemic.md#epi-rte-claim-governance
      - memory.md#mem-obj-vault-pages
      - memory.md#mem-obj-conversations
      - runtime.md#rt-rte-foundry-tools
      - runtime.md#rt-rte-link-remember
      - memory.md#mem-obj-state-metadata
      note: Known automatic publication and proposed automatic/human gates do not resolve generic caller control
        or every initialization and backend admission alternative.
    curation_operations:
      assessment: partial
      units:
      - scope: Legacy repeated publication into existing destinations
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-rte-vault-publish
          - memory.md#mem-obj-unified-vault
          note: Subsequent publication overwrites selected destination pages and metadata.
        records:
        - runtime.md#rt-rte-vault-publish
        - memory.md#mem-obj-unified-vault
        note: Rewriting existing normalized entries is distinct from merely rebuilding indexes.
      - scope: Proposed conversation-to-fact extraction
        assessment: known
        findings:
        - value: consolidate
          basis: claimed
          records:
          - memory.md#mem-rte-conversation-promotion
          - memory.md#mem-obj-conversations
          - memory.md#mem-obj-user-profiles
          note: The fast model extracts key facts from retained turns.
        records:
        - memory.md#mem-rte-conversation-promotion
        - memory.md#mem-obj-conversations
        - memory.md#mem-obj-user-profiles
        note: Extraction reduces recorded conversation content into standing facts; novel inferred claims are
          not established.
      - scope: Proposed heat decay and hot-tier promotion
        assessment: known
        findings:
        - value: decay
          basis: claimed
          records:
          - memory.md#mem-rte-conversation-promotion
          note: Daily decay lowers retention heat.
        - value: promote
          basis: claimed
          records:
          - memory.md#mem-rte-conversation-promotion
          note: Hot mid-term material moves to the memory inbox.
        records:
        - memory.md#mem-rte-conversation-promotion
        note: These are explicit proposed transformations, not evidence that quality improved.
      - scope: Proposed stale/cold archive with retained provenance
        assessment: known
        findings:
        - value: invalidate
          basis: claimed
          records:
          - memory.md#mem-rte-memory-lifecycle
          - memory.md#mem-rte-conversation-promotion
          note: Archived content remains for provenance but is excluded from active search by design.
        records:
        - memory.md#mem-rte-memory-lifecycle
        - memory.md#mem-rte-conversation-promotion
        note: Withdrawal from active use differs from physical deletion.
      - scope: Proposed rejection-guided revision
        assessment: known
        findings:
        - value: evolve
          basis: claimed
          records:
          - memory.md#mem-rte-feedback-recompile
          - memory.md#mem-obj-rejection-feedback
          note: The later writer is directed to rewrite prior content using retained criticism.
        records:
        - memory.md#mem-rte-feedback-recompile
        - memory.md#mem-obj-rejection-feedback
        note: The transformation revises an existing article candidate; the named compile route alone would
          not establish it.
      - scope: Other article compilation/normalization, external Link/LLM-WIKI maintenance, cache/embedding
          lifecycle and draft supersession propagation
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-article-generation
        - epistemic.md#epi-rte-markdown-normalization
        - runtime.md#rt-rte-link-remember
        - runtime.md#rt-rte-client-query
        - memory.md#mem-obj-state-metadata
        - epistemic.md#epi-rte-claim-governance
        note: Article semantic relation and title-link fidelity are unresolved. Index rebuilds, collision renaming,
          maintenance flags and status names do not establish further controlled curation operations.
      records:
      - runtime.md#rt-rte-vault-publish
      - memory.md#mem-obj-unified-vault
      - memory.md#mem-rte-conversation-promotion
      - memory.md#mem-obj-conversations
      - memory.md#mem-obj-user-profiles
      - memory.md#mem-rte-memory-lifecycle
      - memory.md#mem-rte-feedback-recompile
      - memory.md#mem-obj-rejection-feedback
      - epistemic.md#epi-rte-article-generation
      - epistemic.md#epi-rte-markdown-normalization
      - runtime.md#rt-rte-link-remember
      - runtime.md#rt-rte-client-query
      - memory.md#mem-obj-state-metadata
      - epistemic.md#epi-rte-claim-governance
      note: Positive transformations are tied to the recorded route and evidence layer. Opaque backend maintenance
        and cache/embedding routes prevent complete operation coverage; no unsupported deduplication or synthesis
        is inferred.
    read_back_direction:
      assessment: partial
      units:
      - scope: Legacy client search/ask fulfillment
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-client-query
          note: Search/ask fulfills an explicit client query to backend memory.
        records:
        - runtime.md#rt-rte-client-query
        note: A caller requests retained material; wrapping a requested return as MCP text does not add push.
      - scope: Proposed graph get_context request and automatic model-input assembly
        assessment: known
        findings:
        - value: pull
          basis: claimed
          records:
          - memory.md#mem-rte-graph-context
          note: get_context(page_id, depth) requests retained graph context.
        - value: push
          basis: claimed
          records:
          - memory.md#mem-rte-graph-context
          - memory.md#mem-bap-query-knowledge
          note: The QueryEngine automatically inserts primary content and selected outbound relationship summaries
            into generation input.
        records:
        - memory.md#mem-rte-graph-context
        - memory.md#mem-bap-query-knowledge
        note: 'Two different operations occur: page-seeded retrieval is requested; the assembler supplies selected
          context to the answering model.'
      - scope: Proposed retained criticism delivered to a later writer
        assessment: known
        findings:
        - value: push
          basis: claimed
          records:
          - memory.md#mem-rte-feedback-recompile
          - memory.md#mem-bap-feedback-guidance
          note: Affected-concept recompilation appends previous rejection feedback to the writer prompt.
        records:
        - memory.md#mem-rte-feedback-recompile
        - memory.md#mem-bap-feedback-guidance
        note: The writer is supplied feedback by orchestration, not shown issuing a retrieval request.
      - scope: Proposed retained source/related-page rendering into compilation
        assessment: partial
        findings:
        - value: push
          basis: claimed
          records:
          - runtime.md#rt-rte-design-lifecycle
          - runtime.md#rt-obj-compile-template
          note: Orchestration renders retained sources, related summaries and flagged conflicts into model
            input.
        records:
        - runtime.md#rt-rte-design-lifecycle
        - runtime.md#rt-obj-compile-template
        note: Automatic rendering supplies retained material, but the selector providing related pages is not
          shown.
      - scope: Documented exported-file consumer
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-rte-pack-export
          note: File-aware agents can request/read articles from the retained export.
        records:
        - memory.md#mem-rte-pack-export
        note: Directory import is an affordance; actual external reads are not inspected.
      - scope: Conversation extraction/history, direct profile delivery, backend-internal context, cache/embedding
          reuse and optional proof consumers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-conversations
        - memory.md#mem-obj-user-profiles
        - memory.md#mem-rte-conversation-promotion
        - runtime.md#rt-rte-client-query
        - memory.md#mem-obj-state-metadata
        - epistemic.md#epi-rte-proof-export
        note: Proposed later consumers or storage are named without enough invocation/selection facts to classify
          every direction. This uncertainty does not negate the independently supported push/pull routes.
      records:
      - runtime.md#rt-rte-client-query
      - memory.md#mem-rte-graph-context
      - memory.md#mem-bap-query-knowledge
      - memory.md#mem-rte-feedback-recompile
      - memory.md#mem-bap-feedback-guidance
      - runtime.md#rt-rte-design-lifecycle
      - runtime.md#rt-obj-compile-template
      - memory.md#mem-rte-pack-export
      - memory.md#mem-obj-conversations
      - memory.md#mem-obj-user-profiles
      - memory.md#mem-rte-conversation-promotion
      - memory.md#mem-obj-state-metadata
      - epistemic.md#epi-rte-proof-export
      note: Request-led backend/file routes coexist with proposed automatic context supply inside compilation/query
        chains. Opaque backend assembly and unsettled profile/cache consumers prevent complete direction coverage.
    read_back_signal:
      assessment: partial
      units:
      - scope: Proposed QueryEngine context insertion on a query with supplied primary page ID
        assessment: known
        findings:
        - value: identifier
          basis: claimed
          records:
          - memory.md#mem-rte-graph-context
          - memory.md#mem-obj-knowledge-graph
          note: Actual page/node identity and linked edge identities determine selected retained context.
        - value: coarse
          basis: claimed
          records:
          - memory.md#mem-rte-graph-context
          note: The assembler takes the first five outbound entries having an edge; this availability/count
            filter is separate from identity-based targeting.
        records:
        - memory.md#mem-rte-graph-context
        - memory.md#mem-obj-knowledge-graph
        note: 'Trigger: query generation. Selector input: supplied page_id and graph edges. Selected parts:
          matching primary page and reachable outbound entries with edge context.'
      - scope: Proposed feedback insertion during affected-concept recompilation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-feedback-recompile
        - memory.md#mem-obj-rejection-feedback
        note: 'Trigger: another compilation attempt. The record identifies affected concepts and prior feedback,
          but inconsistent lookup scope leaves the actual identity-match selector unresolved; an identifier
          finding would overstate it.'
      - scope: Proposed compiler source/related-summary truncation
        assessment: partial
        findings:
        - value: coarse
          basis: claimed
          records:
          - runtime.md#rt-obj-compile-template
          note: Source length and 200-character related-summary limits filter supplied material without demonstrated
            semantic targeting.
        records:
        - runtime.md#rt-obj-compile-template
        - runtime.md#rt-rte-design-lifecycle
        note: 'Trigger: template rendering. Selected parts: supplied retained source text/related summaries/flagged
          pairs. Length truncation is known; the upstream related-page selector is unknown.'
      - scope: Legacy requested backend results and documented requested pack reads, considered only at their
          pull operation
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-client-query
        - memory.md#mem-rte-pack-export
        note: These operations fulfill requests rather than independently selecting unsolicited context; no
          push signal applies to those specific operations.
      - scope: Unsettled profile/history delivery and external backend/cache/optional embedding automatic selection
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-user-profiles
        - memory.md#mem-obj-conversations
        - runtime.md#rt-rte-client-query
        - runtime.md#rt-rte-link-remember
        - memory.md#mem-obj-state-metadata
        note: No actual push selector is recorded for these alternatives. Optional vector re-ranking and model
          aliases alone cannot establish inferred-embedding selection; neither lexical nor judgment selection
          is inferred from a tool name.
      records:
      - memory.md#mem-rte-graph-context
      - memory.md#mem-obj-knowledge-graph
      - memory.md#mem-rte-feedback-recompile
      - memory.md#mem-obj-rejection-feedback
      - runtime.md#rt-obj-compile-template
      - runtime.md#rt-rte-design-lifecycle
      - runtime.md#rt-rte-client-query
      - memory.md#mem-rte-pack-export
      - memory.md#mem-obj-user-profiles
      - memory.md#mem-obj-conversations
      - runtime.md#rt-rte-link-remember
      - memory.md#mem-obj-state-metadata
      note: Push selectors are classified locally. A requested file ID alone is not a push signal, and opaque
        selectors remain unresolved rather than being made inapplicable by a known pull route.
    trace_learning:
      assessment: partial
      units:
      - scope: Proposed automatic extraction from logged conversation to durable facts/proposals and later
          committed knowledge
        assessment: known
        findings:
        - value: 'yes'
          basis: claimed
          records:
          - memory.md#mem-rte-conversation-promotion
          - memory.md#mem-obj-conversations
          - memory.md#mem-rte-memory-lifecycle
          note: Recorded session turns feed automatic retained fact/proposal production with intended later
            knowledge consumption.
        records:
        - memory.md#mem-rte-conversation-promotion
        - memory.md#mem-obj-conversations
        - memory.md#mem-obj-user-profiles
        - memory.md#mem-rte-memory-lifecycle
        note: Automatic derived writes and later committed-memory retrieval are specified; final human commitment
          is a separate admission step.
      - scope: Direct user-profile branch of conversation extraction
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-user-profiles
        - memory.md#mem-rte-conversation-promotion
        note: Automatic profile production is proposed but direct later visibility is undecided, preventing
          a separately complete qualifying profile-to-consumer chain.
      - scope: Proposed retained audit criticism to automatic article rewrite to later compilation/query
        assessment: known
        findings:
        - value: 'yes'
          basis: claimed
          records:
          - memory.md#mem-obj-rejection-feedback
          - memory.md#mem-rte-feedback-recompile
          - runtime.md#rt-rte-design-lifecycle
          note: Audit experience is persisted as feedback, automatically shapes a rewritten article and has
            intended later knowledge consumers.
        records:
        - memory.md#mem-obj-rejection-feedback
        - memory.md#mem-rte-feedback-recompile
        - runtime.md#rt-rte-design-lifecycle
        note: The trace-fed durable rewrite chain is design only; broken sketch plumbing prevents wired evidence,
          not the claimed route.
      - scope: Legacy imported-page publication, generic remember, original raw sources, audit/job/governance
          rows, graph/pack outputs and opaque cache/embedding/provider updates
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-vault-publish
        - runtime.md#rt-rte-link-remember
        - memory.md#mem-obj-vault-pages
        - memory.md#mem-obj-state-metadata
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-obj-agent-pack
        - epistemic.md#epi-obj-governance-state
        - runtime.md#rt-rte-model-proxy
        note: The records do not establish every original input, automatic trace-fed write and later behavior-shaping
          consumer. Ordinary copying or raw log retention alone is insufficient, and no bounded absence record
          supports no.
      records:
      - memory.md#mem-rte-conversation-promotion
      - memory.md#mem-obj-conversations
      - memory.md#mem-obj-user-profiles
      - memory.md#mem-rte-memory-lifecycle
      - memory.md#mem-obj-rejection-feedback
      - memory.md#mem-rte-feedback-recompile
      - runtime.md#rt-rte-design-lifecycle
      - runtime.md#rt-rte-vault-publish
      - runtime.md#rt-rte-link-remember
      - memory.md#mem-obj-vault-pages
      - memory.md#mem-obj-state-metadata
      - memory.md#mem-obj-knowledge-graph
      - memory.md#mem-obj-agent-pack
      - epistemic.md#epi-obj-governance-state
      - runtime.md#rt-rte-model-proxy
      note: The proposed conversation and audit-feedback update chains support local positives without observed
        improvement or parameter learning. Other writes lack bounded absence evidence, so no system-wide no
        is asserted.
    trace_source:
      assessment: partial
      units:
      - scope: Conversation-derived committed-memory chain
        assessment: known
        findings:
        - value: session-logs
          basis: claimed
          records:
          - memory.md#mem-obj-conversations
          - memory.md#mem-rte-conversation-promotion
          note: Logged role/content turns feed fast-model extraction and proposed memory production.
        records:
        - memory.md#mem-obj-conversations
        - memory.md#mem-rte-conversation-promotion
        note: Recorded conversational turns are the original input, regardless of later profile/page serialization.
      - scope: Retained audit execution feedback used for an article rewrite
        assessment: known
        findings:
        - value: tool-traces
          basis: claimed
          records:
          - memory.md#mem-obj-rejection-feedback
          - memory.md#mem-rte-feedback-recompile
          - runtime.md#rt-rte-design-lifecycle
          note: Recorded audit rejection/criticism from the checking stage feeds the later writer.
        records:
        - memory.md#mem-obj-rejection-feedback
        - memory.md#mem-rte-feedback-recompile
        - runtime.md#rt-rte-design-lifecycle
        note: The qualifying original experience is audit/check feedback, not the entire document source or
          an invented multi-step trajectory.
      - scope: Direct profile-only consumer branch
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-user-profiles
        - memory.md#mem-rte-conversation-promotion
        note: Conversation origin is recorded, but the qualifying later-consumer chain is unresolved; this
          does not make the source axis inapplicable.
      - scope: Opaque remember/backend/raw-source provenance, audit/job payloads, cache/embedding/provider
          updates and other graph/pack derivation inputs
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-link-remember
        - runtime.md#rt-rte-client-query
        - memory.md#mem-obj-vault-pages
        - memory.md#mem-obj-state-metadata
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-obj-agent-pack
        - runtime.md#rt-rte-model-proxy
        note: No complete qualifying trace-fed chain or original trace-content inventory is established. Event-streams
          and trajectories are not inferred from scheduling, timestamps, or workflow diagrams.
      records:
      - memory.md#mem-obj-conversations
      - memory.md#mem-rte-conversation-promotion
      - memory.md#mem-obj-rejection-feedback
      - memory.md#mem-rte-feedback-recompile
      - runtime.md#rt-rte-design-lifecycle
      - memory.md#mem-obj-user-profiles
      - runtime.md#rt-rte-link-remember
      - runtime.md#rt-rte-client-query
      - memory.md#mem-obj-vault-pages
      - memory.md#mem-obj-state-metadata
      - memory.md#mem-obj-knowledge-graph
      - memory.md#mem-obj-agent-pack
      - runtime.md#rt-rte-model-proxy
      note: Qualifying sources are classified at original content, not adapter labels. Unsettled profile delivery
        and opaque input/update routes prevent a complete trace-source inventory.
---

# IsaacCLupus_mnemosyn_spec memory profile

## Comparison rationale

All ten axes remain partial. This is an inventory of proposed memory and the legacy adapter's retained outputs, not a claim that the unified OS runs. Claimed design, afforded external consumption and wired copying stay separate. Missing execution evidence prevents observed or causal findings, not the wired local copying classification. The unresolved backend boundary is supported by [RT-RTE-client-query](runtime.md#rt-rte-client-query), [RT-RTE-link-remember](runtime.md#rt-rte-link-remember) and [MEM-OBJ-state-metadata](memory.md#mem-obj-state-metadata).

### Canonical identities and scope

Reconciliation supersedes EPI-OBJ-unified-pages with [MEM-OBJ-unified-vault](memory.md#mem-obj-unified-vault), EPI-OBJ-user-profiles with [MEM-OBJ-user-profiles](memory.md#mem-obj-user-profiles), and EPI-RTE-profile-promotion with [MEM-RTE-conversation-promotion](memory.md#mem-rte-conversation-promotion). Those canonical objects/routes supply the corresponding storage, form, lineage, admission and trace classifications. Supersession changes citation identity, not evidence strength. The article functions, feedback subroute, graph context and exports remain distinct parts/routes rather than replacements for [RT-RTE-design-lifecycle](runtime.md#rt-rte-design-lifecycle).

The memory boundary excludes the shipped compilation template itself and current-request proxy queues. It includes the use-produced source/related-page material rendered through that template and any provider-retained alternative whose contents remain unresolved. Static template instructions do not establish memory instruction authority; use-retained criticism does, through [MEM-BAP-feedback-guidance](memory.md#mem-bap-feedback-guidance). Model aliases establish neither a vector substrate nor a use-fed parametric-memory update: see [RT-RTE-model-proxy](runtime.md#rt-rte-model-proxy) and [MEM-OBJ-state-metadata](memory.md#mem-obj-state-metadata).

### Mapping limits

Legacy publication imports page bodies and compiles selected metadata; repeated overwrites evolve existing entries. It is not semantic consolidation or deduplication merely because it normalizes metadata, renames collisions and rebuilds indexes. Optional Git history is a conditional wired repository route, not observed recovery. Its initial source authorship, Link reload payload and downstream ranking remain unresolved: [RT-RTE-vault-publish](runtime.md#rt-rte-vault-publish), [MEM-OBJ-unified-vault](memory.md#mem-obj-unified-vault), [EPI-RTE-maturity-mapping](epistemic.md#epi-rte-maturity-mapping).

Conversation extraction consolidates retained turns; daily heat decay, hot-tier promotion and archival have separate proposed effects. Profile visibility is not settled. The committed-memory branch supplies a claimed trace-learning chain without requiring automatic final approval or proving improvement. The feedback chain separately retains audit execution feedback, gives it instruction and learning force at a later rewrite, and yields proposed durable article updates. These classifications do not assert accepted new knowledge, parameter training, theory building or exercised self-improvement: [MEM-RTE-conversation-promotion](memory.md#mem-rte-conversation-promotion), [MEM-RTE-feedback-recompile](memory.md#mem-rte-feedback-recompile), [MEM-OBJ-user-profiles](memory.md#mem-obj-user-profiles).

Read-back operations are distinguished within a chain. A requested backend response is pull. The graph study's get_context request is also pull, while its automatic addition of selected context to the answering model is push. The page-ID/node match supplies identifier targeting; first-five/edge-availability filtering supplies a separate coarse constraint. No semantic ranking is inferred. Feedback insertion supports proposed push but its inconsistent lookup does not establish a complete identifier selector. Related-page truncation supports coarse filtering without resolving upstream selection: [RT-RTE-client-query](runtime.md#rt-rte-client-query), [MEM-RTE-graph-context](memory.md#mem-rte-graph-context), [MEM-RTE-feedback-recompile](memory.md#mem-rte-feedback-recompile), [RT-OBJ-compile-template](runtime.md#rt-obj-compile-template). The documented file consumer remains afforded pull, not an observed import: [MEM-RTE-pack-export](memory.md#mem-rte-pack-export).

No negative trace-learning finding is supplied: the accepted records declare no bounded absence warrant for these unresolved alternatives. Likewise, pull-only units do not make the whole read-back-signal axis inapplicable. Complete statistics cannot be derived from these partial inventories, even where a local wired witness establishes a value's existence.

### Source-read log

No source files were read for this profile. Classification uses only the supplied accepted records and their annotations, with identity resolution from the supplied reconciliation. No new evidence, quotations or records are introduced.
