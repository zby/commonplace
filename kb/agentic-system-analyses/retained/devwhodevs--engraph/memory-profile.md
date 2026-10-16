---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Engraph memory profile: retained vault content, derived retrieval/identity state and move-fed placement at the frozen revision."
run-id: "AAS-2026-10-14-engraph-0cd4f00695b0-01"
source-identity: "https://github.com/devwhodevs/engraph"
reviewed-boundary: "f9a95bc96accc792c02ee384d9e6bf768a88c8c8"
memory-comparison:
  version: 2
  scope: "Retained vault Markdown; SQLite file/chunk/FTS/vector/graph/tag/access structures, identity facts, folder centroids, correction/CLI telemetry, query cache, unresolved links and migration history; use-admitted identity configuration, detected vault profile and saved migration previews; their admission, maintenance and later client/internal consumers. Includes unresolved incoming-content control/provenance, telemetry consumers, graph-output details and withdrawal derivatives. Excludes shipped static prompts/skills, model weight caches and opaque model internals, transient search/context/health outputs as retained objects, HTTP permission configuration, product source/releases and external conversational-agent state."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        - scope: "Source vault Markdown bodies and frontmatter"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vault-notes"
              note: "Markdown files, not their graph encoding, are the source substrate."
          records:
            - "memory.md#mem-obj-vault-notes"
          note: "Source files remain separately retained and reread from disk."
        - scope: "SQLite file/chunk/FTS/vector/edge/tag structures, identity facts, centroids, query cache, correction and migration logs, unresolved links and CLI telemetry"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-file-record"
                - "memory.md#mem-obj-chunk-record"
                - "memory.md#mem-obj-folder-centroids"
                - "memory.md#mem-obj-placement-corrections"
                - "memory.md#mem-obj-identity-fact"
                - "runtime.md#rt-obj-llm-cache"
                - "runtime.md#rt-rte-index-refresh"
                - "runtime.md#rt-rte-para-migration"
                - "memory.md#mem-obj-health-report"
                - "memory.md#mem-obj-cli-event"
              note: "All named structures persist in Store/engraph.db. Vector and graph access structures do not establish separate storage services."
          records:
            - "memory.md#mem-obj-file-record"
            - "memory.md#mem-obj-chunk-record"
            - "memory.md#mem-obj-folder-centroids"
            - "memory.md#mem-obj-placement-corrections"
            - "memory.md#mem-obj-identity-fact"
            - "runtime.md#rt-obj-llm-cache"
            - "runtime.md#rt-rte-index-refresh"
            - "runtime.md#rt-rte-para-migration"
            - "memory.md#mem-obj-health-report"
            - "memory.md#mem-obj-cli-event"
          note: "The records identify the persisted SQLite structures, including logs whose operative consumers remain unresolved."
        - scope: "Use-admitted config identity, detected vault profile and saved migration previews"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-setup-apply"
                - "memory.md#mem-obj-vault-profile"
                - "runtime.md#rt-rte-para-migration"
              note: "Setup saves configuration/profile; migration saves later-applied previews."
          records:
            - "runtime.md#rt-rte-setup-apply"
            - "memory.md#mem-obj-vault-profile"
            - "runtime.md#rt-rte-para-migration"
          note: "TOML configuration/profile and JSON/Markdown previews are filesystem artifacts."
      records:
        - "memory.md#mem-obj-vault-notes"
        - "memory.md#mem-obj-file-record"
        - "memory.md#mem-obj-chunk-record"
        - "memory.md#mem-obj-folder-centroids"
        - "memory.md#mem-obj-placement-corrections"
        - "memory.md#mem-obj-identity-fact"
        - "runtime.md#rt-obj-llm-cache"
        - "runtime.md#rt-rte-index-refresh"
        - "runtime.md#rt-rte-para-migration"
        - "memory.md#mem-obj-health-report"
        - "memory.md#mem-obj-cli-event"
        - "runtime.md#rt-rte-setup-apply"
        - "memory.md#mem-obj-vault-profile"
      note: "The memory inventory separates source files, use-admitted configuration and previews from SQLite derivatives. Loaded static model weights, shipped prompts, product source/releases and transient outputs are excluded; numerical encoding alone is not a model-weights substrate."
    representational_form:
      assessment: "known"
      units:
        - scope: "Vault prose, heading/snippet text, identity value text and formatted configured identity"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vault-notes"
                - "memory.md#mem-obj-chunk-record"
                - "memory.md#mem-obj-identity-fact"
                - "runtime.md#rt-rte-setup-apply"
                - "memory.md#mem-rte-identity-context"
              note: "Note bodies, snippets and identity values supply readable content to later clients."
          records:
            - "memory.md#mem-obj-vault-notes"
            - "memory.md#mem-obj-chunk-record"
            - "memory.md#mem-obj-identity-fact"
            - "runtime.md#rt-rte-setup-apply"
            - "memory.md#mem-rte-identity-context"
          note: "These text parts are delivered for human/model interpretation, distinct from fixed-rule fields."
        - scope: "Frontmatter, file/chunk IDs and counts, graph/tag/access metadata, identity keys, profile roles, correction/CLI/migration records and cache intent/date fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vault-notes"
                - "memory.md#mem-obj-file-record"
                - "memory.md#mem-obj-chunk-record"
                - "runtime.md#rt-rte-index-refresh"
                - "memory.md#mem-obj-identity-fact"
                - "memory.md#mem-obj-vault-profile"
                - "memory.md#mem-obj-placement-corrections"
                - "memory.md#mem-obj-cli-event"
                - "runtime.md#rt-rte-para-migration"
                - "runtime.md#rt-obj-llm-cache"
              note: "Structured values are interpreted by code, not treated as numerical distributed weights."
          records:
            - "memory.md#mem-obj-vault-notes"
            - "memory.md#mem-obj-file-record"
            - "memory.md#mem-obj-chunk-record"
            - "runtime.md#rt-rte-index-refresh"
            - "memory.md#mem-obj-identity-fact"
            - "memory.md#mem-obj-vault-profile"
            - "memory.md#mem-obj-placement-corrections"
            - "memory.md#mem-obj-cli-event"
            - "runtime.md#rt-rte-para-migration"
            - "runtime.md#rt-obj-llm-cache"
          note: "Localized fields have fixed resolver, filter, placement or recovery consumers; no opaque consumed checkpoint is established."
        - scope: "Dense chunk vectors and folder centroids at similarity and placement consumers"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunk-record"
                - "memory.md#mem-obj-folder-centroids"
                - "memory.md#mem-rte-placement-feedback"
              note: "Dense embeddings and centroid BLOBs spread selector state across numerical dimensions."
          records:
            - "memory.md#mem-obj-chunk-record"
            - "memory.md#mem-obj-folder-centroids"
            - "memory.md#mem-rte-placement-feedback"
          note: "The records distinguish dense representations from their text displays and from model weights."
        - scope: "Query-cache expansion text at embedding/FTS consumers and migration preview display text"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-llm-cache"
                - "runtime.md#rt-rte-query-search"
                - "runtime.md#rt-rte-para-migration"
              note: "Expansion strings feed text interpretation and Markdown previews afford human inspection."
          records:
            - "runtime.md#rt-obj-llm-cache"
            - "runtime.md#rt-rte-query-search"
            - "runtime.md#rt-rte-para-migration"
          note: "The cache is mixed: strings are interpreted as query text while its intent/date fields are symbolic."
      records:
        - "memory.md#mem-obj-vault-notes"
        - "memory.md#mem-obj-chunk-record"
        - "memory.md#mem-obj-identity-fact"
        - "runtime.md#rt-rte-setup-apply"
        - "memory.md#mem-rte-identity-context"
        - "memory.md#mem-obj-file-record"
        - "runtime.md#rt-rte-index-refresh"
        - "memory.md#mem-obj-vault-profile"
        - "memory.md#mem-obj-placement-corrections"
        - "memory.md#mem-obj-cli-event"
        - "runtime.md#rt-rte-para-migration"
        - "runtime.md#rt-obj-llm-cache"
        - "memory.md#mem-obj-folder-centroids"
        - "memory.md#mem-rte-placement-feedback"
        - "runtime.md#rt-rte-query-search"
      note: "The named retained inventory has text, fixed-rule metadata and dense numerical parts. Complete form classification does not claim complete provenance, deployed consumers or audited detector correctness."
    lineage:
      assessment: "partial"
      units:
        - scope: "Incoming vault bodies and caller identity fields at Engraph acquisition"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vault-notes"
                - "runtime.md#rt-rte-note-admission"
                - "runtime.md#rt-rte-setup-apply"
              note: "External files/caller text enter the retained vault/configuration through shipped admission routes."
          records:
            - "memory.md#mem-obj-vault-notes"
            - "runtime.md#rt-rte-note-admission"
            - "runtime.md#rt-rte-setup-apply"
          note: "Engraph acquires supplied content; the original author, source derivation and human decision behind arbitrary supplied material remain unresolved."
        - scope: "Index snippets, file/edge/tag metadata and detected profile"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunk-record"
                - "memory.md#mem-obj-file-record"
                - "runtime.md#rt-rte-index-refresh"
                - "memory.md#mem-obj-vault-profile"
                - "runtime.md#rt-rte-setup-apply"
              note: "Chunking, metadata parsing, indexing and profile detection create retained derived representations."
          records:
            - "memory.md#mem-obj-chunk-record"
            - "memory.md#mem-obj-file-record"
            - "runtime.md#rt-rte-index-refresh"
            - "memory.md#mem-obj-vault-profile"
            - "runtime.md#rt-rte-setup-apply"
          note: "These derivation paths are software transformations of supplied vault state; full profile-detector accuracy is not a lineage guarantee."
        - scope: "Embedding and ordinary index/create/delete centroid derivation"
          assessment: "partial"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunk-record"
                - "memory.md#mem-obj-folder-centroids"
                - "runtime.md#rt-rte-index-refresh"
                - "runtime.md#rt-rte-note-admission"
              note: "Software embedding and averaging produce retained numerical state."
          records:
            - "memory.md#mem-obj-chunk-record"
            - "memory.md#mem-obj-folder-centroids"
            - "runtime.md#rt-rte-index-refresh"
            - "runtime.md#rt-rte-note-admission"
          note: "The encoder and aggregation paths are known, but exact weight provenance and coherent centroid aggregation across writers are not. This prevents resolving every numerical origin."
        - scope: "Move-fed centroid adjustment and raw correction rows"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-placement-feedback"
                - "memory.md#mem-obj-folder-centroids"
                - "memory.md#mem-obj-placement-corrections"
              note: "Detected filesystem moves produce correction records and durable placement-selector updates."
          records:
            - "memory.md#mem-rte-placement-feedback"
            - "memory.md#mem-obj-folder-centroids"
            - "memory.md#mem-obj-placement-corrections"
          note: "Only recognized move/provenance/suggestion combinations qualify; this is not provenance for every centroid row."
        - scope: "Tier-1 identity extraction, query-orchestration cache and migration preview/history"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-rte-identity-context"
                - "memory.md#mem-obj-identity-fact"
                - "runtime.md#rt-obj-llm-cache"
                - "runtime.md#rt-rte-query-search"
                - "runtime.md#rt-rte-para-migration"
              note: "Code/model transformation and serialization produce the derived objects; no original session provenance is established for arbitrary note text."
          records:
            - "memory.md#mem-rte-identity-context"
            - "memory.md#mem-obj-identity-fact"
            - "runtime.md#rt-obj-llm-cache"
            - "runtime.md#rt-rte-query-search"
            - "runtime.md#rt-rte-para-migration"
          note: "Separate derivations remain separate: identity extracts admitted index text, cache retains generated query policy, and migration saves proposed/applied destinations."
        - scope: "CLI telemetry original producers and inputs"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-cli-event"
          note: "Storage schema is inspected but producer call sites are not fully traced; telemetry origin cannot be completely classified."
      records:
        - "memory.md#mem-obj-vault-notes"
        - "runtime.md#rt-rte-note-admission"
        - "runtime.md#rt-rte-setup-apply"
        - "memory.md#mem-obj-chunk-record"
        - "memory.md#mem-obj-file-record"
        - "runtime.md#rt-rte-index-refresh"
        - "memory.md#mem-obj-vault-profile"
        - "memory.md#mem-obj-folder-centroids"
        - "memory.md#mem-rte-placement-feedback"
        - "memory.md#mem-obj-placement-corrections"
        - "memory.md#mem-rte-identity-context"
        - "memory.md#mem-obj-identity-fact"
        - "runtime.md#rt-obj-llm-cache"
        - "runtime.md#rt-rte-query-search"
        - "runtime.md#rt-rte-para-migration"
        - "memory.md#mem-obj-cli-event"
      note: "Known acquisition, compilation and move-trace extraction coexist with unresolved original content, weight provenance and telemetry producer wiring. No authored finding is inferred from adapter labels or the possibility of human editing."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Note bodies/snippets, identity values and L0 identity at read/context/identity clients"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vault-notes"
                - "memory.md#mem-obj-chunk-record"
                - "memory.md#mem-obj-identity-fact"
                - "memory.md#mem-rte-identity-context"
                - "memory.md#mem-rte-vault-readback"
                - "runtime.md#rt-rte-setup-apply"
                - "runtime.md#rt-rte-topic-context"
                - "runtime.md#rt-rte-query-search"
              note: "Later requested tool returns supply content to clients without a semantic acceptance guarantee."
          records:
            - "memory.md#mem-obj-vault-notes"
            - "memory.md#mem-obj-chunk-record"
            - "memory.md#mem-obj-identity-fact"
            - "memory.md#mem-rte-identity-context"
            - "memory.md#mem-rte-vault-readback"
            - "runtime.md#rt-rte-setup-apply"
            - "runtime.md#rt-rte-topic-context"
            - "runtime.md#rt-rte-query-search"
          note: "These parts supply reference/context. External obedience or reinterpretation as standing instructions is unobserved and outside the service boundary."
        - scope: "Chunk text/vectors, graph/date metadata and query cache at retrieval selectors"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunk-record"
                - "memory.md#mem-obj-file-record"
                - "runtime.md#rt-rte-index-refresh"
                - "runtime.md#rt-rte-query-search"
                - "runtime.md#rt-rte-topic-context"
              note: "Text, vectors, graph edges and dates influence relative retrieval priority."
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-llm-cache"
                - "runtime.md#rt-rte-query-search"
              note: "Cached intent, expansions and dates select retrieval lanes and inputs on later same-query searches."
          records:
            - "memory.md#mem-obj-chunk-record"
            - "memory.md#mem-obj-file-record"
            - "runtime.md#rt-rte-index-refresh"
            - "runtime.md#rt-obj-llm-cache"
            - "runtime.md#rt-rte-query-search"
            - "runtime.md#rt-rte-topic-context"
          note: "Retained candidate content and relationships influence relevance/order even with fixed ranking code."
        - scope: "Folder centroids at semantic placement and old chunk vectors at feedback update"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunk-record"
                - "memory.md#mem-rte-placement-feedback"
              note: "Retained vectors combined with detected move feedback feed durable behavior-shaping centroid updates."
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-folder-centroids"
                - "memory.md#mem-rte-placement-feedback"
                - "runtime.md#rt-rte-note-admission"
              note: "Saved centroids determine relative similarity of candidate folders."
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-folder-centroids"
                - "memory.md#mem-rte-placement-feedback"
                - "runtime.md#rt-rte-note-admission"
              note: "The admitted best semantic destination selects the later write folder."
          records:
            - "memory.md#mem-obj-folder-centroids"
            - "memory.md#mem-obj-chunk-record"
            - "memory.md#mem-rte-placement-feedback"
            - "runtime.md#rt-rte-note-admission"
          note: "The update consumer and downstream placement consumer have different effects; explicit folders and type rules can bypass semantic placement."
        - scope: "Profile roles, file metadata, tag registry and migration destinations/history at machine consumers"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vault-profile"
                - "memory.md#mem-obj-file-record"
                - "runtime.md#rt-rte-index-refresh"
                - "runtime.md#rt-rte-note-admission"
                - "memory.md#mem-rte-vault-readback"
                - "memory.md#mem-rte-identity-context"
                - "runtime.md#rt-rte-para-migration"
              note: "Retained structural state chooses destinations, scopes, resolved files and operation inputs."
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-file-record"
                - "runtime.md#rt-rte-note-admission"
              note: "Stored file mtime is compared against current disk mtime before append admission."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-file-record"
                - "runtime.md#rt-rte-note-admission"
              note: "An mtime mismatch can veto append, not merely advise its caller."
          records:
            - "memory.md#mem-obj-vault-profile"
            - "memory.md#mem-obj-file-record"
            - "runtime.md#rt-rte-index-refresh"
            - "runtime.md#rt-rte-note-admission"
            - "memory.md#mem-rte-vault-readback"
            - "memory.md#mem-rte-identity-context"
            - "runtime.md#rt-rte-para-migration"
          note: "Profile roles select folders; identifiers resolve reads; registered tags influence admitted names; saved migration paths select forward/reverse moves."
        - scope: "Stored snippets/edges/metadata and unresolved-link rows at health diagnostic consumer"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-health-report"
                - "runtime.md#rt-rte-index-refresh"
                - "epistemic.md#epi-rte-health-report"
              note: "Retained indexed structure supplies evidence for client-requested diagnostics."
          records:
            - "memory.md#mem-obj-health-report"
            - "runtime.md#rt-rte-index-refresh"
            - "epistemic.md#epi-rte-health-report"
          note: "These are evidence inputs for an advisory structural report, not retained admission criteria. Fixed diagnostic code is excluded static machinery."
        - scope: "Placement correction rows, CLI telemetry and migration preview display at unresolved or optional consumers"
          assessment: "partial"
          findings:
            - value: "knowledge"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-para-migration"
              note: "The saved human-readable preview affords operator inspection before apply."
          records:
            - "memory.md#mem-obj-placement-corrections"
            - "memory.md#mem-obj-cli-event"
            - "runtime.md#rt-rte-para-migration"
          note: "Placement consumes centroids rather than correction rows; CLI producers/consumers are incompletely traced. Preview Markdown is available for review without established review operation."
      records:
        - "memory.md#mem-obj-vault-notes"
        - "memory.md#mem-obj-chunk-record"
        - "memory.md#mem-obj-identity-fact"
        - "memory.md#mem-rte-identity-context"
        - "memory.md#mem-rte-vault-readback"
        - "runtime.md#rt-rte-setup-apply"
        - "runtime.md#rt-rte-topic-context"
        - "runtime.md#rt-rte-query-search"
        - "memory.md#mem-obj-file-record"
        - "runtime.md#rt-rte-index-refresh"
        - "runtime.md#rt-obj-llm-cache"
        - "memory.md#mem-obj-folder-centroids"
        - "memory.md#mem-rte-placement-feedback"
        - "runtime.md#rt-rte-note-admission"
        - "memory.md#mem-obj-vault-profile"
        - "runtime.md#rt-rte-para-migration"
        - "memory.md#mem-obj-health-report"
        - "epistemic.md#epi-rte-health-report"
        - "memory.md#mem-obj-placement-corrections"
        - "memory.md#mem-obj-cli-event"
      note: "The known consumers establish knowledge, ranking, routing, learning and bounded append validation/enforcement. Untraced log consumers prevent a complete authority inventory. Read-only/HTTP grants and shipped instructions are runtime controls, not use-derived memory authority."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Index admission, chunk/edge/tag/vector transformations, detected profile, identity extraction and cache admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-index-refresh"
                - "memory.md#mem-obj-chunk-record"
                - "memory.md#mem-obj-vault-profile"
                - "runtime.md#rt-rte-setup-apply"
                - "memory.md#mem-rte-identity-context"
                - "runtime.md#rt-obj-llm-cache"
                - "runtime.md#rt-rte-query-search"
              note: "Code chooses and persists transformed derived values."
          records:
            - "runtime.md#rt-rte-index-refresh"
            - "memory.md#mem-obj-chunk-record"
            - "memory.md#mem-obj-vault-profile"
            - "runtime.md#rt-rte-setup-apply"
            - "memory.md#mem-rte-identity-context"
            - "runtime.md#rt-obj-llm-cache"
            - "runtime.md#rt-rte-query-search"
          note: "Software/model admission occurs without a separate per-derived-content human decision; starting index/setup/search does not make it manual."
        - scope: "Writer tag/link/placement transformations and filesystem-feedback updates"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-note-admission"
                - "memory.md#mem-rte-placement-feedback"
                - "memory.md#mem-obj-folder-centroids"
                - "memory.md#mem-obj-placement-corrections"
              note: "Software admits naming/link/placement transformations and centroid/log changes."
          records:
            - "runtime.md#rt-rte-note-admission"
            - "memory.md#mem-rte-placement-feedback"
            - "memory.md#mem-obj-folder-centroids"
            - "memory.md#mem-obj-placement-corrections"
          note: "Caller proposal is separate from automatic transformation. Feedback code accepts qualifying moves without authenticated per-correction approval."
        - scope: "Original note text, edit/replacement/withdrawal requests, supplied identity and migration apply/undo decision"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-vault-notes"
            - "runtime.md#rt-rte-note-admission"
            - "memory.md#mem-rte-note-withdrawal"
            - "runtime.md#rt-rte-setup-apply"
            - "runtime.md#rt-rte-para-migration"
          note: "Generic CLI/MCP/HTTP or external editor identity does not determine whether an explicit human supplied or approved each retained content change; no manual value is established."
        - scope: "CLI-event admission call sites"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-cli-event"
          note: "Append/prune APIs alone do not identify the active write/admission mechanism."
      records:
        - "runtime.md#rt-rte-index-refresh"
        - "memory.md#mem-obj-chunk-record"
        - "memory.md#mem-obj-vault-profile"
        - "runtime.md#rt-rte-setup-apply"
        - "memory.md#mem-rte-identity-context"
        - "runtime.md#rt-obj-llm-cache"
        - "runtime.md#rt-rte-query-search"
        - "runtime.md#rt-rte-note-admission"
        - "memory.md#mem-rte-placement-feedback"
        - "memory.md#mem-obj-folder-centroids"
        - "memory.md#mem-obj-placement-corrections"
        - "memory.md#mem-obj-vault-notes"
        - "memory.md#mem-rte-note-withdrawal"
        - "runtime.md#rt-rte-para-migration"
        - "memory.md#mem-obj-cli-event"
      note: "Automatic transformation/admission is positive; caller-origin control and telemetry admission remain unresolved. Authorship and physical I/O are not substituted for agency."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Tier-1 identity extraction over retained snippets and indexed metadata"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-identity-context"
                - "memory.md#mem-obj-identity-fact"
              note: "Selected retained note snippets/metadata become a reduced identity view."
            - value: "synthesize"
              basis: "wired"
              records:
                - "memory.md#mem-rte-identity-context"
                - "memory.md#mem-obj-identity-fact"
              note: "The preserved OOO association and active/key category promotion can create claims not present as such in the inputs."
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-identity-context"
                - "memory.md#mem-obj-identity-fact"
              note: "Clearing/repopulating tier-1 rows replaces the retained identity view; no content-truth critique is implied."
          records:
            - "memory.md#mem-rte-identity-context"
            - "memory.md#mem-obj-identity-fact"
          note: "Copying/compressing focus/blocking and category extraction are distinguished. Reconciliation preserves the epistemic OOO association counterexample on this canonical route."
        - scope: "Existing note edits/appends/rewrites and move-fed numerical/frontmatter revisions"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-note-admission"
                - "memory.md#mem-rte-placement-feedback"
                - "memory.md#mem-obj-folder-centroids"
              note: "Existing text/frontmatter and durable centroid representations are revised."
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-placement-feedback"
                - "memory.md#mem-obj-folder-centroids"
              note: "Feedback subtracts the moved note contribution from the suggested centroid, downweighting that placement representation; this is not time-based decay."
          records:
            - "runtime.md#rt-rte-note-admission"
            - "memory.md#mem-rte-placement-feedback"
            - "memory.md#mem-obj-folder-centroids"
          note: "These modify retained entries/state. New-note acquisition and index rebuild alone are not classified as curation."
        - scope: "Archive and hard-deletion/database-clear branches"
          assessment: "known"
          findings:
            - value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-note-withdrawal"
              note: "Archive withdraws indexed reliance while keeping an archive body/history."
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-note-withdrawal"
              note: "Hard delete forgets the selected source/index entries; clear forgets database state, not vault Markdown."
          records:
            - "memory.md#mem-rte-note-withdrawal"
          note: "Archive preserves a disk body while removing ordinary indexed reliance; hard delete/clear remove specified retained state. Soft-delete auxiliary effects remain unresolved."
        - scope: "CLI telemetry age-pruning capability"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-cli-event"
              note: "Age-based deletion affords forgetting old CLI-event rows."
          records:
            - "memory.md#mem-obj-cli-event"
          note: "A retained-log pruning method exists, but no active invocation is established."
        - scope: "Uninspected metadata-edit details, soft-delete derivative cleanup and telemetry maintenance activation"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-note-admission"
            - "memory.md#mem-rte-note-withdrawal"
            - "memory.md#mem-obj-cli-event"
          note: "These included alternatives prevent exhaustive enumeration of implemented transformations and complete derivative-withdrawal claims."
      records:
        - "memory.md#mem-rte-identity-context"
        - "memory.md#mem-obj-identity-fact"
        - "runtime.md#rt-rte-note-admission"
        - "memory.md#mem-rte-placement-feedback"
        - "memory.md#mem-obj-folder-centroids"
        - "memory.md#mem-rte-note-withdrawal"
        - "memory.md#mem-obj-cli-event"
      note: "Retained-content consolidation/synthesis, revision, bounded invalidation and forgetting/downweighting have distinct warrants. Search-result dedup is transient selection, not retained-memory dedup; no promote value follows from identity labels alone."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Requested search/topic/read/section/list/person/project/map/identity returns"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-query-search"
                - "runtime.md#rt-rte-topic-context"
                - "memory.md#mem-rte-vault-readback"
                - "memory.md#mem-rte-identity-context"
              note: "Later clients request selected retained content and receive snippets, disk bodies, metadata or identity text."
          records:
            - "runtime.md#rt-rte-query-search"
            - "runtime.md#rt-rte-topic-context"
            - "memory.md#mem-rte-vault-readback"
            - "memory.md#mem-rte-identity-context"
          note: "Consumer requests retained material; internal delivery is not counted again as push."
        - scope: "Automatic cache, profile, tag-registry and centroid supply to later operations"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-llm-cache"
                - "runtime.md#rt-rte-query-search"
                - "memory.md#mem-obj-vault-profile"
                - "runtime.md#rt-rte-index-refresh"
                - "runtime.md#rt-rte-note-admission"
                - "memory.md#mem-obj-folder-centroids"
                - "memory.md#mem-rte-placement-feedback"
              note: "Same-query search automatically loads cache; loaded profile/tag/centroid state shapes subsequent writing and selection."
          records:
            - "runtime.md#rt-obj-llm-cache"
            - "runtime.md#rt-rte-query-search"
            - "memory.md#mem-obj-vault-profile"
            - "runtime.md#rt-rte-index-refresh"
            - "runtime.md#rt-rte-note-admission"
            - "memory.md#mem-obj-folder-centroids"
            - "memory.md#mem-rte-placement-feedback"
          note: "Consumers request an operation, not these specific retained selector objects; code automatically chooses/supplies retained policy/access state."
        - scope: "Automatic selection of indexed inputs for identity extraction and move-fed adaptation"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-identity-context"
                - "memory.md#mem-obj-identity-fact"
                - "memory.md#mem-obj-chunk-record"
                - "memory.md#mem-rte-placement-feedback"
              note: "Fixed extraction rules select saved snippets/metadata; detected move selects retained vectors for centroid adaptation."
          records:
            - "memory.md#mem-rte-identity-context"
            - "memory.md#mem-obj-identity-fact"
            - "memory.md#mem-obj-chunk-record"
            - "memory.md#mem-rte-placement-feedback"
          note: "Refresh/move triggers cause code to supply selected retained inputs to update consumers without a request for those individual parts."
        - scope: "Migration preview apply/history undo and requested health diagnostics"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-para-migration"
                - "memory.md#mem-obj-health-report"
                - "epistemic.md#epi-rte-health-report"
              note: "Requested later operations reload preview/history or query retained diagnostic inputs."
          records:
            - "runtime.md#rt-rte-para-migration"
            - "memory.md#mem-obj-health-report"
            - "epistemic.md#epi-rte-health-report"
          note: "Apply/undo explicitly requests retained proposed/history state; health requests diagnostic evidence over the retained index."
        - scope: "Correction-log later consumers, CLI telemetry and independently uninspected graph-output alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-placement-corrections"
            - "memory.md#mem-obj-cli-event"
            - "memory.md#mem-rte-vault-readback"
          note: "Storage APIs are not a consumer route. The memory coverage table retains incomplete producer/consumer and standalone graph-output inspection."
      records:
        - "runtime.md#rt-rte-query-search"
        - "runtime.md#rt-rte-topic-context"
        - "memory.md#mem-rte-vault-readback"
        - "memory.md#mem-rte-identity-context"
        - "runtime.md#rt-obj-llm-cache"
        - "memory.md#mem-obj-vault-profile"
        - "runtime.md#rt-rte-index-refresh"
        - "runtime.md#rt-rte-note-admission"
        - "memory.md#mem-obj-folder-centroids"
        - "memory.md#mem-rte-placement-feedback"
        - "memory.md#mem-obj-identity-fact"
        - "memory.md#mem-obj-chunk-record"
        - "runtime.md#rt-rte-para-migration"
        - "memory.md#mem-obj-health-report"
        - "epistemic.md#epi-rte-health-report"
        - "memory.md#mem-obj-placement-corrections"
        - "memory.md#mem-obj-cli-event"
      note: "Requested content return and internal automatic supply of retained selector/update state are different operations. Watcher persistence alone is not context push. Untraced included consumers prevent a completely assessed pull-only or complete direction inventory."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Same-query cache push on search with an orchestrator present"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-llm-cache"
                - "runtime.md#rt-rte-query-search"
              note: "Actual query-hash identity lookup selects the retained result consumed instead of regeneration."
          records:
            - "runtime.md#rt-obj-llm-cache"
            - "runtime.md#rt-rte-query-search"
          note: "Trigger: later query search. Selector input: original query SHA256. Selected part: cached orchestration JSON. No model/age match is imposed."
        - scope: "Automatic semantic folder selection during later note writes"
          assessment: "known"
          findings:
            - value: "inferred-embedding"
              basis: "wired"
              records:
                - "memory.md#mem-obj-folder-centroids"
                - "memory.md#mem-rte-placement-feedback"
                - "runtime.md#rt-rte-note-admission"
              note: "Cosine similarity selects the retained numerical folder representation influencing placement."
          records:
            - "memory.md#mem-obj-folder-centroids"
            - "memory.md#mem-rte-placement-feedback"
            - "runtime.md#rt-rte-note-admission"
          note: "Trigger: write without explicit folder or successful type rule. Input: new-content embedding versus saved folder vectors. Selected part: best above-threshold centroid/folder."
        - scope: "Registered tag resolution during writer transformations"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-index-refresh"
                - "runtime.md#rt-rte-note-admission"
              note: "Exact registry identity matches can select admitted canonical names."
            - value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-index-refresh"
                - "runtime.md#rt-rte-note-admission"
              note: "Fuzzy/prefix rules select retained naming state from lexical input."
          records:
            - "runtime.md#rt-rte-index-refresh"
            - "runtime.md#rt-rte-note-admission"
          note: "Trigger: proposed tags. Input: supplied tag spelling. Selected part: persisted registry names through exact/fuzzy/prefix matching."
        - scope: "Loaded profile supply to placement/context/identity and fixed identity-input extraction"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vault-profile"
                - "runtime.md#rt-rte-setup-apply"
                - "memory.md#mem-rte-identity-context"
                - "memory.md#mem-obj-file-record"
              note: "Available profile and fixed folder/tag/date/count gates supply scoped retained inputs."
            - value: "inferred-lexical"
              basis: "wired"
              records:
                - "memory.md#mem-rte-identity-context"
                - "memory.md#mem-obj-chunk-record"
              note: "Priority/blocking/OOO text predicates select retained snippets for extraction."
          records:
            - "memory.md#mem-obj-vault-profile"
            - "runtime.md#rt-rte-setup-apply"
            - "memory.md#mem-rte-identity-context"
            - "memory.md#mem-obj-file-record"
            - "memory.md#mem-obj-chunk-record"
          note: "Profile load supplies available configured roles. Extraction selects project/date/path/edge-ranked and keyword-matching retained parts. These mechanisms are not model judgment."
        - scope: "Move-triggered vector supply to centroid update"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-placement-feedback"
                - "memory.md#mem-obj-chunk-record"
                - "memory.md#mem-obj-file-record"
              note: "Matched moved-file identity selects retained vectors, not merely an identifier displayed to a client."
          records:
            - "memory.md#mem-rte-placement-feedback"
            - "memory.md#mem-obj-chunk-record"
            - "memory.md#mem-obj-file-record"
          note: "Trigger: detected move. Input: matched file/content identity plus provenance and suggested-folder conditions. Selected part: that indexed note's chunk vectors."
        - scope: "Untraced CLI/correction consumers and remaining graph selection detail"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-cli-event"
            - "memory.md#mem-obj-placement-corrections"
            - "memory.md#mem-rte-vault-readback"
          note: "Their direction/selection wiring is not established, so selector signals cannot be completed or declared inapplicable."
      records:
        - "runtime.md#rt-obj-llm-cache"
        - "runtime.md#rt-rte-query-search"
        - "memory.md#mem-obj-folder-centroids"
        - "memory.md#mem-rte-placement-feedback"
        - "runtime.md#rt-rte-note-admission"
        - "runtime.md#rt-rte-index-refresh"
        - "memory.md#mem-obj-vault-profile"
        - "runtime.md#rt-rte-setup-apply"
        - "memory.md#mem-rte-identity-context"
        - "memory.md#mem-obj-file-record"
        - "memory.md#mem-obj-chunk-record"
        - "memory.md#mem-obj-cli-event"
        - "memory.md#mem-obj-placement-corrections"
        - "memory.md#mem-rte-vault-readback"
      note: "Signals characterize the named automatic supplies only. IDs on requested reads are not identifier push, and requested search delivery is not another embedding push. Opaque/untraced alternatives remain unresolved; no inferred-judgment finding is established for retained-part push selection."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Qualifying move-fed placement adaptation"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-placement-feedback"
                - "memory.md#mem-obj-folder-centroids"
                - "memory.md#mem-obj-chunk-record"
              note: "Move traces plus retained note vectors automatically update durable centroids used on later writes."
          records:
            - "memory.md#mem-rte-placement-feedback"
            - "memory.md#mem-obj-folder-centroids"
            - "memory.md#mem-obj-chunk-record"
            - "memory.md#mem-obj-placement-corrections"
          note: "Detected activity feeds an automatic persistent selector update subsequently consumed by semantic placement; no parameter training, authenticated human correction or benefit is required for this route classification."
        - scope: "Identity derived from arbitrary vault notes and query-policy cache origin"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-identity-context"
            - "memory.md#mem-obj-vault-notes"
            - "runtime.md#rt-obj-llm-cache"
            - "runtime.md#rt-rte-query-search"
          note: "Derived content has later consumers, but accepted records do not establish that original inputs are recorded sessions/tool experience rather than arbitrary content/current requests. This prevents deciding additional qualifying trace-fed routes."
        - scope: "CLI telemetry producer and later behavior-shaping consumer"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-cli-event"
          note: "Raw-log storage/pruning does not establish or rule out a qualifying automatic update. Full producer/consumer call sites remain uninspected."
        - scope: "Other initial content, profile and ordinary centroid derivations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-vault-notes"
            - "memory.md#mem-obj-vault-profile"
            - "memory.md#mem-obj-folder-centroids"
            - "runtime.md#rt-rte-index-refresh"
            - "runtime.md#rt-rte-setup-apply"
          note: "The inspected derivations are identified, but arbitrary source experience and original write control are unresolved; there is no bounded absence record warranting a local no."
      records:
        - "memory.md#mem-rte-placement-feedback"
        - "memory.md#mem-obj-folder-centroids"
        - "memory.md#mem-obj-chunk-record"
        - "memory.md#mem-obj-placement-corrections"
        - "memory.md#mem-rte-identity-context"
        - "memory.md#mem-obj-vault-notes"
        - "runtime.md#rt-obj-llm-cache"
        - "runtime.md#rt-rte-query-search"
        - "memory.md#mem-obj-cli-event"
        - "memory.md#mem-obj-vault-profile"
        - "runtime.md#rt-rte-index-refresh"
        - "runtime.md#rt-rte-setup-apply"
      note: "A wired yes is supported for move-fed centroids. Other included origins/consumers remain unresolved, so neither a system-wide no nor complete enumeration of qualifying routes is warranted."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Original activity input to qualifying placement feedback"
          assessment: "known"
          findings:
            - value: "event-streams"
              basis: "wired"
              records:
                - "memory.md#mem-rte-placement-feedback"
                - "memory.md#mem-obj-placement-corrections"
                - "memory.md#mem-obj-folder-centroids"
              note: "Detected filesystem movement is the discrete environmental event feeding the qualifying update."
          records:
            - "memory.md#mem-rte-placement-feedback"
            - "memory.md#mem-obj-placement-corrections"
            - "memory.md#mem-obj-folder-centroids"
          note: "A filesystem move event plus saved suggestion/provenance metadata and existing vectors drives adaptation. Metadata is not authenticated human feedback or a conversational log."
        - scope: "Original source content behind vectors mixed into feedback"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-chunk-record"
            - "memory.md#mem-obj-vault-notes"
            - "memory.md#mem-rte-placement-feedback"
          note: "The event source is known, but records do not establish whether arbitrary vault content also originates in session logs, tool traces or multi-step trajectories. Existing vectors do not reveal that origin."
        - scope: "Possible additional identity/cache/content trace-fed derivations and CLI telemetry consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-identity-context"
            - "runtime.md#rt-obj-llm-cache"
            - "runtime.md#rt-rte-query-search"
            - "memory.md#mem-obj-vault-notes"
            - "memory.md#mem-obj-cli-event"
            - "memory.md#mem-obj-vault-profile"
            - "memory.md#mem-obj-folder-centroids"
          note: "Qualifying trace-fed status and original input wiring are unresolved outside the move route. Trace-source cannot be made inapplicable by a known positive or by unspecified input."
      records:
        - "memory.md#mem-rte-placement-feedback"
        - "memory.md#mem-obj-placement-corrections"
        - "memory.md#mem-obj-folder-centroids"
        - "memory.md#mem-obj-chunk-record"
        - "memory.md#mem-obj-vault-notes"
        - "memory.md#mem-rte-identity-context"
        - "runtime.md#rt-obj-llm-cache"
        - "runtime.md#rt-rte-query-search"
        - "memory.md#mem-obj-cli-event"
        - "memory.md#mem-obj-vault-profile"
      note: "Event-stream input is local to move feedback. Mixed source provenance and possible additional trace-fed consumers remain unresolved; no session-logs, tool-traces or trajectories value is inferred from adapter labels or raw-log schemas."
---

# Engraph memory profile

## Comparison rationale

This profile classifies accepted records, not new source facts. It includes retained source content, derived access/selector state, write feedback and unresolved alternatives. Model weights and shipped instructions are excluded because these records do not show their accumulation or change through Engraph use. Current-call bundles and health reports are not retained objects; their retained inputs and later consumption routes remain included. The inventory and limits are supported by [MEM-OBJ-vault-notes](memory.md#mem-obj-vault-notes), [MEM-OBJ-chunk-record](memory.md#mem-obj-chunk-record), [MEM-OBJ-vault-profile](memory.md#mem-obj-vault-profile), [MEM-OBJ-health-report](memory.md#mem-obj-health-report), and [MEM-OBJ-cli-event](memory.md#mem-obj-cli-event).

SQLite is the substrate for the graph, FTS and vector structures. Their encodings and access algorithms do not imply separate graph/vector storage services. Dense chunk embeddings and centroids are parametric representations, distinct from the excluded loaded model parameters. Their provenance is only partially resolved, even though their storage and form are known ([MEM-OBJ-chunk-record](memory.md#mem-obj-chunk-record), [MEM-OBJ-folder-centroids](memory.md#mem-obj-folder-centroids)).

Reconciliation identifies the epistemic identity-fact, identity-extraction and placement-correction declarations with the canonical memory objects/routes cited here; the health-output duplicate likewise resolves to the memory object. Those amendments change citation destinations, not values or evidence strength. They preserve the identity extraction counterexample, source loss and activity/importance promotion. Thus extraction includes both consolidation of existing text and synthesis of non-entailed category associations. Faithfulness loss in copied focus/blocking bullets alone would not establish synthesis. The canonical route remains [MEM-RTE-identity-context](memory.md#mem-rte-identity-context), and the numerical feedback route remains [MEM-RTE-placement-feedback](memory.md#mem-rte-placement-feedback). No other supersession changes these classifications.

Move feedback establishes automatic trace-fed durable behavior shaping: an environmental move plus retained vectors changes centroids consumed by later writes. Old vectors have learning authority at the update; updated centroids rank and route future placement. The raw correction log is not the inspected placement input. Event-stream origin is supported for the move, not for every original note that contributed vectors. The inconsistent centroid writer keys/counts prevent a uniform full-vault mean or complete reset inference, not existence of the update pathway ([MEM-RTE-placement-feedback](memory.md#mem-rte-placement-feedback), [MEM-OBJ-folder-centroids](memory.md#mem-obj-folder-centroids), [MEM-OBJ-placement-corrections](memory.md#mem-obj-placement-corrections)).

Requested note/identity/search/context returns are pull. Their automatic internal supply of cache, profile, naming and placement state is a separate operation, not a second push for every returned search hit. Cache query-hash equality actually selects retained JSON; a requested note identifier alone does not establish identifier push. Automatic extraction supplies selected retained snippets to an update consumer rather than unsolicited identity text to an agent ([RT-OBJ-llm-cache](runtime.md#rt-obj-llm-cache), [RT-RTE-query-search](runtime.md#rt-rte-query-search), [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh), [MEM-RTE-vault-readback](memory.md#mem-rte-vault-readback), [MEM-RTE-identity-context](memory.md#mem-rte-identity-context)).

Agency remains partial because caller identity does not establish human per-content decisions. Starting a workflow does not turn tag/link/placement or identity extraction into manual admission. No manual finding follows from the CLI label or the opportunity to review a migration preview ([RT-RTE-note-admission](runtime.md#rt-rte-note-admission), [RT-RTE-setup-apply](runtime.md#rt-rte-setup-apply), [RT-RTE-para-migration](runtime.md#rt-rte-para-migration)).

Curation distinguishes retained changes from transient formatting or indexing. Archive can invalidate ordinary indexed reliance while preserving a body; hard deletion forgets selected material, but soft deletion and auxiliary cleanup do not support complete erasure. Feedback subtraction downweights one numerical representation, not time-based forgetting. CLI-event age pruning is an afforded method with untraced activation, not a wired maintenance loop ([MEM-RTE-note-withdrawal](memory.md#mem-rte-note-withdrawal), [MEM-RTE-placement-feedback](memory.md#mem-rte-placement-feedback), [MEM-OBJ-cli-event](memory.md#mem-obj-cli-event)).

Unknown telemetry consumers, arbitrary source provenance/control, uninspected graph-output details and unresolved lifecycle derivatives prevent stronger coverage assessments. No bounded absence records establish local trace-learning no or a pull-only boundary. Unknown source origins do not justify invented session/tool/trajectory values. Every positive remains at its own wired or afforded basis; no observed operation, causal benefit, client obedience or improved placement is asserted.

Source-read log: none. Classification used only the supplied members, types, collection and records contract; no source ambiguity required a frozen-checkout read.
