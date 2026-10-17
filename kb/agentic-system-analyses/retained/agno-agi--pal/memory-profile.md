---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Pal memory comparison: retained context files, routing and learning stores, structured facts and framework conversational continuity."
run-id: AAS-2026-10-17-pal-e313a0902289-01
source-identity: https://github.com/agno-agi/pal
reviewed-boundary: 6516b8ede0c085e48f39f3bd04cb85b475a855dc
memory-comparison:
  version: 2
  scope: "Retained raw/wiki/user files and access metadata, optional context Git replication, PostgreSQL user facts, routing and learning text/vector stores, personal memory and session history; includes model, direct API, loader, synchronization, evaluator-cleanup and opaque registered-service alternatives. Excludes unchanged shipped instructions/templates, current replies and transient evaluation maps, external source services unless saved, and provider model weights not shown to accumulate Pal experience."
  axes:
    storage_substrate:
      assessment: known
      units:
        - scope: "Raw sources, wiki articles/index/state/lint, manifest and edited or generated user files"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-raw, memory.md#mem-obj-wiki-articles, memory.md#mem-obj-wiki-index, memory.md#mem-obj-wiki-state, memory.md#mem-obj-lint-report, memory.md#mem-obj-user-files, runtime.md#rt-obj-manifest]
              note: "Retained content and access metadata reside in context-directory files; lint production is instructed but its retention substrate is explicit."
          records: [memory.md#mem-obj-raw, memory.md#mem-obj-wiki-articles, memory.md#mem-obj-wiki-index, memory.md#mem-obj-wiki-state, memory.md#mem-obj-lint-report, memory.md#mem-obj-user-files, runtime.md#rt-obj-manifest]
          note: "Covers substantive file content and its separate navigation/status objects, not merely the article body."
        - scope: "Optional Git copies and history of retained context files"
          assessment: known
          findings:
            - value: repo
              basis: wired
              records: [runtime.md#rt-rte-git-sync]
              note: "Git commits/push/pull transport and version context files when configured; successful remote persistence is unobserved."
          records: [runtime.md#rt-rte-git-sync]
          note: "Git supplements filesystem storage; it does not replicate database memories."
        - scope: "Routing and operational-learning contents and dense retrieval indexes"
          assessment: known
          findings:
            - value: rdbms
              basis: wired
              records: [memory.md#mem-obj-pal-knowledge, memory.md#mem-obj-pal-learnings]
              note: "Both contents stores are configured in PostgreSQL."
            - value: vector
              basis: wired
              records: [memory.md#mem-obj-pal-knowledge, memory.md#mem-obj-pal-learnings, runtime.md#rt-cmp-openai-embedder]
              note: "Separate hybrid PgVector indexes retain dense representations; vectors are data, not updated model weights."
          records: [memory.md#mem-obj-pal-knowledge, memory.md#mem-obj-pal-learnings, runtime.md#rt-cmp-openai-embedder]
          note: "Opaque entry serialization does not obscure these configured storage substrates. Registered services expose these same handles, not an evidenced additional store."
        - scope: "Structured user facts, framework personal memory and persisted sessions"
          assessment: known
          findings:
            - value: rdbms
              basis: wired
              records: [memory.md#mem-obj-pal-tables, memory.md#mem-obj-user-memory, memory.md#mem-obj-session-history]
              note: "User tables and shared agent/session database handles use PostgreSQL."
          records: [memory.md#mem-obj-pal-tables, memory.md#mem-obj-user-memory, memory.md#mem-obj-session-history]
          note: "Payload schemas and exact table contents remain unknown; substrate classification does not require guessing them."
      records: [memory.md#mem-obj-raw, memory.md#mem-obj-wiki-articles, memory.md#mem-obj-wiki-index, memory.md#mem-obj-wiki-state, memory.md#mem-obj-lint-report, memory.md#mem-obj-user-files, runtime.md#rt-obj-manifest, runtime.md#rt-rte-git-sync, memory.md#mem-obj-pal-knowledge, memory.md#mem-obj-pal-learnings, memory.md#mem-obj-pal-tables, memory.md#mem-obj-user-memory, memory.md#mem-obj-session-history, memory.md#mem-clm-service-boundary]
      note: "The accepted inventory locates all included retained objects, including opaque framework state and the two registered service handles. Known is configuration-level substrate coverage, not observed persistence or complete payload knowledge."
    representational_form:
      assessment: partial
      units:
        - scope: "Raw/wiki bodies, lint findings, index descriptions, edited guidance and saved products at model readers"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-raw, memory.md#mem-obj-wiki-articles, memory.md#mem-obj-wiki-index, memory.md#mem-obj-lint-report, memory.md#mem-obj-user-files]
              note: "Model interpretation gives prose, descriptive metadata and article links their content/navigation effects; path syntax alone does not make that interpretation symbolic."
          records: [memory.md#mem-obj-raw, memory.md#mem-obj-wiki-articles, memory.md#mem-obj-wiki-index, memory.md#mem-obj-lint-report, memory.md#mem-obj-user-files]
          note: "Classifies the recorded model-consumption path, not every possible encoding inside files."
        - scope: "Manifest filename/boolean updates and wiki state count/timestamp setters"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [runtime.md#rt-obj-manifest, memory.md#mem-obj-wiki-state]
              note: "Fixed Python rules match filenames, set flags and update named fields."
          records: [runtime.md#rt-obj-manifest, memory.md#mem-obj-wiki-state]
          note: "Separate from model interpretation of displayed JSON and descriptive manifest fields."
        - scope: "Routing descriptions and intended operational-learning text"
          assessment: partial
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-pal-knowledge, memory.md#mem-rte-knowledge-update]
              note: "Routing strings reach model search consumers and guide subsequent source choices."
            - value: natural-language
              basis: claimed
              records: [memory.md#mem-obj-pal-learnings, memory.md#mem-rte-learning-reuse]
              note: "Retrieval/Pattern/Correction entries are requested as model-interpreted guidance."
          records: [memory.md#mem-obj-pal-knowledge, memory.md#mem-obj-pal-learnings, memory.md#mem-rte-learning-reuse]
          note: "Learning serialization and actual consumed entries are uninspected; intended text is not a complete classification of the opaque payload."
        - scope: "Dense routing and learning retrieval representations"
          assessment: known
          findings:
            - value: parametric
              basis: wired
              records: [runtime.md#rt-cmp-openai-embedder, memory.md#mem-obj-pal-knowledge, memory.md#mem-obj-pal-learnings]
              note: "Dense vectors are distributed numerical representations; this value does not assert training of the embedder."
          records: [runtime.md#rt-cmp-openai-embedder, memory.md#mem-obj-pal-knowledge, memory.md#mem-obj-pal-learnings]
          note: "Separated from the text that the vector index represents."
        - scope: "Structured user table fields and delivered free-text facts"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-pal-tables]
              note: "Schemas, IDs and tag arrays participate in SQL operations."
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-pal-tables]
              note: "Delivered free-text notes and facts are interpreted by Navigator."
          records: [memory.md#mem-obj-pal-tables]
          note: "Both operative parts are described; no populated table instance is asserted."
        - scope: "Personal-memory payload and persisted session payload, including possible tool records/checkpoints"
          assessment: partial
          findings:
            - value: natural-language
              basis: claimed
              records: [memory.md#mem-obj-user-memory, memory.md#mem-obj-session-history, memory.md#mem-rte-conversation-reuse]
              note: "Preferences and conversational history are intended model inputs."
          records: [memory.md#mem-obj-user-memory, memory.md#mem-obj-session-history, memory.md#mem-rte-conversation-reuse]
          note: "Opaque serialization, exact delivered parts and tool-result inclusion prevent complete form coverage. No display summary substitutes for those payloads."
      records: [memory.md#mem-obj-raw, memory.md#mem-obj-wiki-articles, memory.md#mem-obj-wiki-index, memory.md#mem-obj-lint-report, memory.md#mem-obj-user-files, runtime.md#rt-obj-manifest, memory.md#mem-obj-wiki-state, memory.md#mem-obj-pal-knowledge, memory.md#mem-obj-pal-learnings, runtime.md#rt-cmp-openai-embedder, memory.md#mem-obj-pal-tables, memory.md#mem-rte-conversation-reuse]
      note: "Text, fixed-field operations and dense representations are supported locally; dependency-owned memory/learning/session payloads remain unresolved."
    lineage:
      assessment: partial
      units:
        - scope: "Raw content acquisition and Researcher-curated raw alternatives"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-obj-raw, runtime.md#rt-rte-raw-ingest]
              note: "Caller text and URL extraction enter retained raw files; imported does not authenticate source truth."
            - value: other-compiled
              basis: wired
              records: [runtime.md#rt-rte-raw-ingest]
              note: "Fixed code constructs source/frontmatter and pending-extraction stubs."
            - value: other-compiled
              basis: claimed
              records: [memory.md#mem-obj-raw]
              note: "Researcher is instructed to summarize multi-page sources before saving them."
          records: [memory.md#mem-obj-raw, runtime.md#rt-rte-raw-ingest]
          note: "Includes full content, curated summaries and stubs; raw is not synonymous with verbatim source."
        - scope: "Wiki summaries/concepts/index, lint reports and workflow metadata"
          assessment: known
          findings:
            - value: other-compiled
              basis: claimed
              records: [epistemic.md#epi-rte-compiler-transform, memory.md#mem-obj-wiki-index, memory.md#mem-obj-lint-report]
              note: "Models are instructed to derive articles, navigation and criticism from retained material. Semantic novelty of actual outputs is unresolved, not required for this derivation category."
            - value: other-compiled
              basis: wired
              records: [runtime.md#rt-obj-manifest, memory.md#mem-obj-wiki-state]
              note: "Code derives or updates workflow fields from admitted calls."
          records: [epistemic.md#epi-rte-compiler-transform, memory.md#mem-obj-wiki-index, memory.md#mem-obj-lint-report, runtime.md#rt-obj-manifest, memory.md#mem-obj-wiki-state]
          note: "Source links are requested provenance, not demonstrated semantic preservation."
        - scope: "Loader routing entries, specialist descriptions and dense indexes"
          assessment: partial
          findings:
            - value: other-compiled
              basis: wired
              records: [runtime.md#rt-rte-context-refresh, runtime.md#rt-cmp-openai-embedder]
              note: "File metadata is code-derived and vectors are derived by the configured remote embedder."
            - value: authored
              basis: wired
              records: [memory.md#mem-rte-knowledge-update]
              note: "Specialists propose title/content descriptions admitted by insertion. Authored does not imply human control."
          records: [runtime.md#rt-rte-context-refresh, runtime.md#rt-cmp-openai-embedder, memory.md#mem-rte-knowledge-update, memory.md#mem-clm-service-boundary]
          note: "Initial store contents, additional service writes and exact embedding provenance remain unknown. A known refresh does not classify all prior entries."
        - scope: "Operational learnings and personal memory derived from interactions"
          assessment: partial
          findings:
            - value: trace-extracted
              basis: wired
              records: [memory.md#mem-rte-learning-reuse, memory.md#mem-rte-conversation-reuse]
              note: "Configured interaction-to-learning and agentic-memory paths retain derived material for later use; exact extraction belongs to Agno."
          records: [memory.md#mem-obj-pal-learnings, memory.md#mem-obj-user-memory, memory.md#mem-rte-learning-reuse, memory.md#mem-rte-conversation-reuse, memory.md#mem-clm-service-boundary]
          note: "Known subsequent trace-fed paths do not settle initialization, all input mixtures or alternative service admissions."
        - scope: "Persisted conversational history"
          assessment: partial
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-obj-session-history, memory.md#mem-rte-conversation-reuse]
              note: "Configured persistence carries prior conversational material into later invocation context. Retaining a trace is not the same as extracting a derived learning."
          records: [memory.md#mem-obj-session-history, memory.md#mem-rte-conversation-reuse]
          note: "Exact turn/tool filtering and any derived checkpoint lineage remain uninspected; verbatim full-transcript retention is not established."
        - scope: "Edited/generated user files, SQL captures and incoming Git replacements"
          assessment: partial
          findings:
            - value: authored
              basis: wired
              records: [memory.md#mem-obj-user-files, memory.md#mem-obj-pal-tables, runtime.md#rt-rte-navigator-work]
              note: "User edits and model-proposed files/facts can persist; initial shipped copies alone are excluded."
            - value: imported
              basis: wired
              records: [runtime.md#rt-rte-git-sync]
              note: "Git can admit remote retained-file replacements independently of the leader."
            - value: other-compiled
              basis: claimed
              records: [memory.md#mem-obj-user-files, epistemic.md#epi-obj-answer]
              note: "Summaries, reviews, exports and optionally filed substantive answers are generated from selected material."
          records: [memory.md#mem-obj-user-files, memory.md#mem-obj-pal-tables, runtime.md#rt-rte-git-sync, epistemic.md#epi-obj-answer]
          note: "Actual source mixtures, initial retained contents and remote authorship are unknown; not every saved product is shown to derive from traces."
      records: [memory.md#mem-obj-raw, runtime.md#rt-rte-raw-ingest, epistemic.md#epi-rte-compiler-transform, memory.md#mem-obj-wiki-index, memory.md#mem-obj-lint-report, runtime.md#rt-obj-manifest, memory.md#mem-obj-wiki-state, runtime.md#rt-rte-context-refresh, memory.md#mem-rte-knowledge-update, runtime.md#rt-cmp-openai-embedder, memory.md#mem-rte-learning-reuse, memory.md#mem-rte-conversation-reuse, memory.md#mem-obj-user-files, memory.md#mem-obj-pal-tables, runtime.md#rt-rte-git-sync, memory.md#mem-clm-service-boundary]
      note: "Supported authored, imported, compiled and trace-extracted paths coexist. Initialization, remote provenance and opaque framework/service alternatives prevent a complete derivation inventory."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Selected raw/wiki/SQL/saved content at answering or maintenance models"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [memory.md#mem-obj-raw, memory.md#mem-obj-wiki-articles, memory.md#mem-obj-pal-tables, memory.md#mem-obj-user-files, runtime.md#rt-rte-navigator-work]
              note: "Tool-delivered content supplies evidence/context for answers and later article work; it does not certify truth."
          records: [memory.md#mem-obj-raw, memory.md#mem-obj-wiki-articles, memory.md#mem-obj-pal-tables, memory.md#mem-obj-user-files, runtime.md#rt-rte-navigator-work]
          note: "Actual content supplies knowledge rather than a hard control; compliance and answer benefit are unobserved."
        - scope: "Wiki index, manifest eligibility, routing descriptions and dense features at retrieval/compile selectors"
          assessment: partial
          findings:
            - value: routing
              basis: claimed
              records: [memory.md#mem-obj-wiki-index, runtime.md#rt-obj-manifest, memory.md#mem-rte-knowledge-update, runtime.md#rt-rte-wiki-maintenance]
              note: "Index descriptions, Discovery entries and compiled-false flags are requested inputs to source/window selection by models."
            - value: ranking
              basis: wired
              records: [memory.md#mem-obj-pal-knowledge, memory.md#mem-obj-pal-learnings, runtime.md#rt-cmp-openai-embedder]
              note: "Retained text/dense representations participate in configured hybrid retrieval, influencing relative retrieval priority without a learned ranking policy claim."
          records: [memory.md#mem-obj-wiki-index, runtime.md#rt-obj-manifest, memory.md#mem-rte-knowledge-update, memory.md#mem-obj-pal-knowledge, memory.md#mem-obj-pal-learnings, runtime.md#rt-cmp-openai-embedder]
          note: "Exact dependency ranking, service consumers and automatic selectors are uninspected. Bookkeeping timestamps alone are not classified as enforcement or validation."
        - scope: "Retained operational guidance, personal preferences and edited voice/template files at later generation"
          assessment: partial
          findings:
            - value: instruction
              basis: wired
              records: [memory.md#mem-bap-retained-guidance, memory.md#mem-rte-learning-reuse]
              note: "Configured learning-context supply delivers intended standing guidance to leader/Researcher. This is directive force, not guaranteed obedience."
            - value: instruction
              basis: claimed
              records: [memory.md#mem-bap-retained-guidance, memory.md#mem-obj-user-files, memory.md#mem-obj-user-memory]
              note: "Navigator is instructed to apply corrections, preferences, voice and template guidance; exact personal-memory delivery is opaque."
            - value: ranking
              basis: claimed
              records: [memory.md#mem-bap-retained-guidance, memory.md#mem-rte-learning-reuse]
              note: "Correction type and recency are requested priority inputs when learnings conflict, not enforced semantic precedence."
          records: [memory.md#mem-bap-retained-guidance, memory.md#mem-rte-learning-reuse, memory.md#mem-obj-user-files, memory.md#mem-obj-user-memory]
          note: "Payload contents, precedence enforcement and all dependency-owned effects remain unresolved."
        - scope: "Recorded interactions/corrections at learning and personal-memory update consumers"
          assessment: partial
          findings:
            - value: learning
              basis: wired
              records: [memory.md#mem-rte-learning-reuse, memory.md#mem-rte-conversation-reuse, epistemic.md#epi-rte-learning-adapt]
              note: "Retained experience feeds configured durable behavior-shaping updates; this authority belongs to update inputs, separately from the output's later instruction force."
            - value: knowledge
              basis: wired
              records: [memory.md#mem-rte-conversation-reuse]
              note: "History and session recall additionally supply past conversational context directly to generation."
          records: [memory.md#mem-rte-learning-reuse, memory.md#mem-rte-conversation-reuse, epistemic.md#epi-rte-learning-adapt]
          note: "Exact trace contents, extraction and delivered payloads are not inspected; no improvement or additional veto authority follows."
        - scope: "Retained lint criticism at intended later repair readers"
          assessment: partial
          findings:
            - value: knowledge
              basis: afforded
              records: [memory.md#mem-obj-lint-report, epistemic.md#epi-rte-lint-retain]
              note: "The named Compiler fixer may use retained advisory findings, but no mandatory report-to-repair handoff is wired."
          records: [memory.md#mem-obj-lint-report, epistemic.md#epi-rte-lint-retain]
          note: "No enforced article withdrawal or validation criterion is established by storing a diagnosis. Actual repair consumption remains unresolved."
      records: [runtime.md#rt-rte-navigator-work, runtime.md#rt-obj-manifest, memory.md#mem-obj-wiki-index, memory.md#mem-rte-knowledge-update, memory.md#mem-obj-pal-knowledge, memory.md#mem-obj-pal-learnings, memory.md#mem-bap-retained-guidance, memory.md#mem-rte-learning-reuse, memory.md#mem-rte-conversation-reuse, memory.md#mem-obj-lint-report, memory.md#mem-clm-service-boundary]
      note: "Consumer-specific knowledge, instruction, ranking, routing and learning effects are supported at distinct layers. Opaque payload/service effects remain included; no system-wide enforcement/validation negative is asserted."
    write_agency:
      assessment: partial
      units:
        - scope: "Researcher ingest, Compiler/Linter files and metadata, Navigator files/SQL and specialist routing writes"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-raw-ingest, runtime.md#rt-rte-wiki-maintenance, runtime.md#rt-rte-navigator-work, memory.md#mem-rte-knowledge-update]
              note: "Model/tool admission proceeds without a general per-content human decision; starting the task or supplying a correction is not approval of its stored formulation."
          records: [runtime.md#rt-rte-raw-ingest, runtime.md#rt-rte-wiki-maintenance, runtime.md#rt-rte-navigator-work, memory.md#mem-rte-knowledge-update]
          note: "Classifies these model-proposed admission mechanisms, not every direct caller of the same underlying API."
        - scope: "Loader metadata admission and evaluator raw/wiki cleanup"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-context-refresh, runtime.md#rt-rte-evaluation-driver]
              note: "Software admits batch metadata or deletion without per-entry/per-file human selection."
          records: [runtime.md#rt-rte-context-refresh, runtime.md#rt-rte-evaluation-driver]
          note: "A caller's recreate or suite-launch decision is not approval of each retained item."
        - scope: "Configured learning writes, personal-memory updates and session persistence"
          assessment: partial
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-rte-learning-reuse, memory.md#mem-rte-conversation-reuse]
              note: "Model/framework admission and persistence are configured without a visible per-memory human gate."
          records: [memory.md#mem-rte-learning-reuse, memory.md#mem-rte-conversation-reuse, memory.md#mem-clm-service-boundary]
          note: "Exact dependency rejection/replacement control and registered-service alternatives remain unknown."
        - scope: "Explicit human edits to retained user guidance/content"
          assessment: known
          findings:
            - value: manual
              basis: afforded
              records: [memory.md#mem-obj-user-files]
              note: "A user can explicitly supply/edit retained guidance. This is the human-edit mechanism, not an inference that subsequent model overwrites are human-approved."
          records: [memory.md#mem-obj-user-files]
          note: "Static shipped guidance is excluded; no actual human editing episode is observed."
        - scope: "Generic direct-ingest submissions, initial retained contents, remote Git authorship and service API admission"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-raw-ingest, runtime.md#rt-rte-git-sync, memory.md#mem-clm-service-boundary, memory.md#mem-obj-pal-learnings, memory.md#mem-obj-user-memory]
          note: "Caller/remote identity and dependency operation contracts do not establish who decided the exact content. Fixed physical writes or a Git pull cannot settle its upstream admission agency."
      records: [runtime.md#rt-rte-raw-ingest, runtime.md#rt-rte-wiki-maintenance, runtime.md#rt-rte-navigator-work, memory.md#mem-rte-knowledge-update, runtime.md#rt-rte-context-refresh, runtime.md#rt-rte-evaluation-driver, memory.md#mem-rte-learning-reuse, memory.md#mem-rte-conversation-reuse, memory.md#mem-obj-user-files, runtime.md#rt-rte-git-sync, memory.md#mem-clm-service-boundary]
      note: "Automatic mechanisms and an afforded explicit human-edit path coexist with unresolved generic caller, initialization, remote and service admission."
    curation_operations:
      assessment: partial
      units:
        - scope: "Compiler reduction of raw sources into summaries"
          assessment: known
          findings:
            - value: consolidate
              basis: claimed
              records: [epistemic.md#epi-obj-summaries, epistemic.md#epi-rte-compiler-transform]
              note: "Requested 200–500-word summaries select and compress source claims. The request is not evidence that a particular output faithfully performed it."
          records: [epistemic.md#epi-obj-summaries, epistemic.md#epi-rte-compiler-transform]
          note: "Mapping describes the specified transformation only, not observed semantic preservation."
        - scope: "Compiler enrichment of existing concepts and navigation"
          assessment: partial
          findings:
            - value: evolve
              basis: claimed
              records: [epistemic.md#epi-obj-concepts, memory.md#mem-obj-wiki-articles, memory.md#mem-obj-wiki-index]
              note: "Instructions request revision of existing concept articles with new information and replacement navigation."
          records: [epistemic.md#epi-obj-concepts, epistemic.md#epi-rte-compiler-transform, memory.md#mem-obj-wiki-index]
          note: "No paired output establishes a new claim absent from inputs; cross-source synthesis wording alone does not establish synthesize."
        - scope: "Operational-learning hygiene over retained entries"
          assessment: partial
          findings:
            - value: evolve
              basis: claimed
              records: [memory.md#mem-rte-learning-reuse]
              note: "Search-before-save and update-rather-than-duplicate request changes to existing learnings."
          records: [memory.md#mem-rte-learning-reuse, memory.md#mem-obj-pal-learnings]
          note: "Exact replacement, consolidation, duplicate removal, expiry and rejection mechanisms are external; preventing duplicates by instruction is not demonstrated dedup."
        - scope: "Loader index refresh/recreate, Git replacement, evaluator deletion, lint reports and other file/SQL maintenance"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-context-refresh, runtime.md#rt-rte-git-sync, runtime.md#rt-rte-evaluation-driver, memory.md#mem-obj-lint-report, runtime.md#rt-rte-navigator-work]
          note: "Rebuild/acquisition/deletion and advisory lint do not by themselves establish a controlled retained-memory transformation. No retained-history withdrawal, age-based downweighting or implemented duplicate merge is established here. This is not an absence claim."
        - scope: "Personal-memory/session transformations and alternative knowledge-service maintenance"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-rte-conversation-reuse, memory.md#mem-clm-service-boundary]
          note: "Dependency-owned extraction, checkpoints, replacement and service operations are not inspected; no complete operation inventory is available."
      records: [epistemic.md#epi-obj-summaries, epistemic.md#epi-obj-concepts, epistemic.md#epi-rte-compiler-transform, memory.md#mem-obj-wiki-index, memory.md#mem-rte-learning-reuse, runtime.md#rt-rte-context-refresh, runtime.md#rt-rte-git-sync, runtime.md#rt-rte-evaluation-driver, memory.md#mem-obj-lint-report, memory.md#mem-rte-conversation-reuse, memory.md#mem-clm-service-boundary]
      note: "Consolidation and evolution have instruction-level warrants. No actual new proposition or duplicate removal is supplied; opaque maintenance alternatives prevent complete classification."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Requested wiki/raw/user-file/SQL retrieval and routing or learning search"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-navigator-work, memory.md#mem-rte-knowledge-update, memory.md#mem-rte-learning-reuse]
              note: "Foreground models request retained material through read/query/search tools. Index-guided follow-up reads remain requested returns, not an extra push."
          records: [runtime.md#rt-rte-navigator-work, memory.md#mem-rte-knowledge-update, memory.md#mem-rte-learning-reuse]
          note: "Includes maintenance article/raw reads; file identifiers implement requested fetches rather than autonomous delivery."
        - scope: "Configured learning addition, recent history supply and explicit history/session search"
          assessment: partial
          findings:
            - value: push
              basis: wired
              records: [memory.md#mem-rte-learning-reuse, memory.md#mem-rte-conversation-reuse]
              note: "Leader/Researcher learning-context flags and leader/Navigator recent-history flags request automatic supply at later invocations."
            - value: pull
              basis: wired
              records: [memory.md#mem-rte-conversation-reuse]
              note: "Foreground history/session search is a separate requested recall route."
          records: [memory.md#mem-rte-learning-reuse, memory.md#mem-rte-conversation-reuse]
          note: "Personal-memory delivery, exact automatic selection and possible checkpoint alternatives remain dependency-internal."
        - scope: "Lint report later repair use and registered knowledge-service consumers"
          assessment: partial
          findings:
            - value: pull
              basis: afforded
              records: [memory.md#mem-obj-lint-report, epistemic.md#epi-rte-lint-retain]
              note: "Named later readers can retrieve the report, but no compulsory repair consumer is wired."
          records: [memory.md#mem-obj-lint-report, epistemic.md#epi-rte-lint-retain, memory.md#mem-clm-service-boundary]
          note: "Registered service handles alone do not establish another read-back route; their concrete consumers and operations remain unresolved."
      records: [runtime.md#rt-rte-navigator-work, memory.md#mem-rte-knowledge-update, memory.md#mem-rte-learning-reuse, memory.md#mem-rte-conversation-reuse, memory.md#mem-obj-lint-report, memory.md#mem-clm-service-boundary]
      note: "Both foreground pull and configured automatic push exist. Dependency-owned memory and service alternatives prevent complete route coverage, not the positive direction findings."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Recent-history push to leader and Navigator"
          assessment: partial
          findings:
            - value: coarse
              basis: wired
              records: [memory.md#mem-rte-conversation-reuse, memory.md#mem-obj-session-history]
              note: "Invocation context building requests recent history bounded by five leader runs or ten Navigator runs. The run-count window is coarse selection of prior conversational material."
          records: [memory.md#mem-rte-conversation-reuse, memory.md#mem-obj-session-history]
          note: "Exact turn/tool filtering and scope keys are external. Run/session IDs do not establish a separately inspected identifier-matched push."
        - scope: "Automatic learning-context supply and personal-memory inclusion"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-learning-reuse, memory.md#mem-rte-conversation-reuse, memory.md#mem-obj-user-memory]
          note: "Trigger is a later configured invocation; selected parts are intended learnings/preferences. Selector inputs, matching rule and budget are unknown. Hybrid store configuration alone cannot establish the signal of automatic delivery."
        - scope: "Requested file/SQL/knowledge/learning/history reads"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-navigator-work, memory.md#mem-rte-knowledge-update, memory.md#mem-rte-learning-reuse, memory.md#mem-rte-conversation-reuse]
          note: "These named operations fulfill consumer requests; push selection signal does not apply to their requested returns. This local inapplicability does not cover automatic alternatives."
        - scope: "Unresolved registered-service read-back alternatives"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-clm-service-boundary]
          note: "No concrete service consumer or push selector is established by registration; cannot classify its signal or declare it inapplicable."
      records: [memory.md#mem-rte-conversation-reuse, memory.md#mem-obj-session-history, memory.md#mem-rte-learning-reuse, memory.md#mem-obj-user-memory, runtime.md#rt-rte-navigator-work, memory.md#mem-rte-knowledge-update, memory.md#mem-clm-service-boundary]
      note: "The history window supports a coarse component. Opaque automatic learning/personal-memory selection and service alternatives prevent complete signal classification; requested identifier reads do not add identifier push."
    trace_learning:
      assessment: partial
      units:
        - scope: "Interaction-fed operational learning writes and later guidance consumers"
          assessment: partial
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-rte-learning-reuse, memory.md#mem-obj-pal-learnings, epistemic.md#epi-rte-learning-adapt]
              note: "Configured model/framework writes derive durable Retrieval/Pattern/Correction guidance from interactions, with later learning search and automatic context-supply consumers. No improvement measurement is required for this route classification."
          records: [memory.md#mem-rte-learning-reuse, memory.md#mem-obj-pal-learnings, epistemic.md#epi-rte-learning-adapt]
          note: "Exact extraction, stored entries and all alternative input/write paths are opaque; the positive is architectural, not observed uptake or benefit."
        - scope: "Agentic personal-memory updates and later preference guidance"
          assessment: partial
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-rte-conversation-reuse, memory.md#mem-obj-user-memory, memory.md#mem-bap-retained-guidance]
              note: "Configured memory updates derive retained preferences from conversational work for later leader/Navigator guidance."
          records: [memory.md#mem-rte-conversation-reuse, memory.md#mem-obj-user-memory, memory.md#mem-bap-retained-guidance]
          note: "Precise payload, extraction and delivery remain external. This does not classify raw history persistence itself as learning."
        - scope: "Generated/saved user products, ordinary source compilation and opaque session checkpoints"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-user-files, epistemic.md#epi-obj-answer, epistemic.md#epi-rte-compiler-transform, memory.md#mem-rte-conversation-reuse]
          note: "Saved summaries/reviews can survive, but records do not resolve every product's original input and later behavior-shaping route. Document compilation need not be trace-fed; raw history alone is insufficient. External continuation-summary/checkpoint production is uninspected, not absent."
        - scope: "Additional admissions and consumers through registered knowledge services"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-clm-service-boundary]
          note: "Service operations and callers are dependency-owned; registration does not prove or exclude a qualifying trace-fed write."
      records: [memory.md#mem-rte-learning-reuse, memory.md#mem-obj-pal-learnings, epistemic.md#epi-rte-learning-adapt, memory.md#mem-rte-conversation-reuse, memory.md#mem-obj-user-memory, memory.md#mem-obj-user-files, epistemic.md#epi-rte-compiler-transform, memory.md#mem-clm-service-boundary]
      note: "Qualifying configured guidance-update chains support yes. No bounded-absence record supports no for other routes; unknown products, checkpoints and service writes remain included. Trace learning is not measured learning capacity or exercised self-improvement."
    trace_source:
      assessment: partial
      units:
        - scope: "Original inputs to interaction/correction-fed operational learnings"
          assessment: partial
          findings:
            - value: session-logs
              basis: wired
              records: [memory.md#mem-rte-learning-reuse, epistemic.md#epi-rte-learning-adapt]
              note: "The configured path consumes interaction/history and explicit conversational corrections to create reusable operational guidance."
          records: [memory.md#mem-rte-learning-reuse, epistemic.md#epi-rte-learning-adapt, memory.md#mem-obj-session-history]
          note: "Exact input-to-entry traces and tool-result inclusion are unavailable. A strategy about tool use does not itself prove recorded tool requests/results were consumed; tool-traces, event-streams and trajectories are not established."
        - scope: "Original inputs to derived personal preferences"
          assessment: partial
          findings:
            - value: session-logs
              basis: wired
              records: [memory.md#mem-rte-conversation-reuse, memory.md#mem-obj-user-memory]
              note: "Conversational invocation and preference-update configuration establish the session-input route, not the exact stored preference formulation."
          records: [memory.md#mem-rte-conversation-reuse, memory.md#mem-obj-user-memory]
          note: "Dependency extraction and mixed inputs remain opaque; no complete trace-source union is warranted."
        - scope: "Other saved products, possible checkpoint transformations and service writes"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-user-files, epistemic.md#epi-obj-answer, memory.md#mem-rte-conversation-reuse, memory.md#mem-clm-service-boundary]
          note: "Qualifying trace-learning status and original inputs are unresolved on these branches. External calendar/email availability and filenames do not establish event-stream learning; static imported guidance is not a trace source."
      records: [memory.md#mem-rte-learning-reuse, epistemic.md#epi-rte-learning-adapt, memory.md#mem-rte-conversation-reuse, memory.md#mem-obj-user-memory, memory.md#mem-obj-session-history, memory.md#mem-obj-user-files, memory.md#mem-clm-service-boundary]
      note: "Session-origin guidance updates are positively supported, while exact mixed trace provenance is not. Because qualifying routes exist and others remain unresolved, this axis is neither absent nor inapplicable."
---

# Pal memory profile

## Comparison rationale

This profile classifies accepted records only. It adds no source quotations, records or execution evidence. No source files were read for this job, so there is no additional source-read log. Configuration and implementation support wiring; prompts support requested transformations. Neither establishes actual admission, delivered payloads, changed decisions or benefit.

### Inventory and evidence layers

The memory boundary includes content and its access structures. Raw files, articles, edited guidance and saved products are not interchangeable with manifest flags, index descriptions or routing vectors. PostgreSQL storage is known even where framework payload form is opaque. Git is optional retained-file replication, not a copy of learning/session databases. These distinctions follow [MEM-OBJ-raw](memory.md#mem-obj-raw), [MEM-OBJ-wiki-articles](memory.md#mem-obj-wiki-articles), [RT-OBJ-manifest](runtime.md#rt-obj-manifest), [MEM-OBJ-pal-knowledge](memory.md#mem-obj-pal-knowledge), [MEM-OBJ-user-memory](memory.md#mem-obj-user-memory) and [RT-RTE-git-sync](runtime.md#rt-rte-git-sync). The workflow's push-failure qualification changes confidence in remote delivery, not the existence of the repository substrate or local file retention.

The storage inventory can therefore be known while most other axes remain partial. In particular, the registered knowledge-service handles are included, but registration supplies neither a concrete additional consumer nor a fully specified admission contract. Framework learning/session payloads and possible checkpoints stay unresolved rather than being replaced by their intended readable descriptions. See [MEM-CLM-service-boundary](memory.md#mem-clm-service-boundary), [MEM-RTE-learning-reuse](memory.md#mem-rte-learning-reuse) and [MEM-RTE-conversation-reuse](memory.md#mem-rte-conversation-reuse).

### Canonicalization

Reconciliation supersedes epistemic raw, lint-report, routing, learning and SQL object duplicates with their memory declarations, and the epistemic routing-write duplicate with [MEM-RTE-knowledge-update](memory.md#mem-rte-knowledge-update). The profile uses those canonical destinations. This affects citation identity, not evidence strength or a value union. Wiki summaries and concepts remain valid separate parts of [MEM-OBJ-wiki-articles](memory.md#mem-obj-wiki-articles); their unsuperseded [EPI-OBJ-summaries](epistemic.md#epi-obj-summaries) and [EPI-OBJ-concepts](epistemic.md#epi-obj-concepts) support local transformation distinctions. [EPI-RTE-learning-adapt](epistemic.md#epi-rte-learning-adapt) remains broader than operational-learning reuse because it also includes personal memory; it is not treated as a replacement for either memory route.

### Non-obvious mappings

Dense retrieval representations establish parametric form and vector storage, not model-weight learning. Routing text and vectors have ranking force at search, while selected descriptions have routing force at the model's next retrieval choice. Manifest flags likewise guide compile selection but are not a truth-validation criterion. Retained correction labels and recency have requested ranking force; preference/voice and strategy text have intended instruction force. Experience at the update consumer has learning authority independently of that downstream instruction force. See [RT-CMP-openai-embedder](runtime.md#rt-cmp-openai-embedder), [MEM-OBJ-pal-knowledge](memory.md#mem-obj-pal-knowledge), [RT-OBJ-manifest](runtime.md#rt-obj-manifest), [MEM-BAP-retained-guidance](memory.md#mem-bap-retained-guidance) and [EPI-RTE-learning-adapt](epistemic.md#epi-rte-learning-adapt).

Compiler summaries support claimed consolidation, and concept/learning revision instructions support claimed evolution. The semantic relation of an actual generated article remains indeterminate. Neither a request to synthesize nor missing evidence of entailment establishes creation of a new claim. Search-before-save is not an implemented duplicate merge; vector recreation is not by itself controlled semantic invalidation with history preserved. Lint advice is not enforced withdrawal. These limits follow [EPI-RTE-compiler-transform](epistemic.md#epi-rte-compiler-transform), [MEM-RTE-learning-reuse](memory.md#mem-rte-learning-reuse), [RT-RTE-context-refresh](runtime.md#rt-rte-context-refresh) and [MEM-OBJ-lint-report](memory.md#mem-obj-lint-report).

Read-back distinguishes requests from automatic supply. A model-requested file fetch remains pull even when index descriptions helped choose its path. Automatic history and learning additions are push. Recent-history run limits support a coarse window component, but neither file paths nor past-session IDs establish an inspected identifier-matched push. The automatic learning selector is unresolved despite the configured hybrid store. See [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work), [MEM-RTE-knowledge-update](memory.md#mem-rte-knowledge-update), [MEM-RTE-learning-reuse](memory.md#mem-rte-learning-reuse) and [MEM-RTE-conversation-reuse](memory.md#mem-rte-conversation-reuse).

Trace-learning positives belong to automatic interaction-to-durable-guidance chains, not raw transcript retention, source compilation in general or provider weights. The session-origin path is supported; exact tool-trace inclusion and other source mixtures remain unknown. No local or global no is invented without a bounded absence record. Unresolved service writes and checkpoints also prevent trace-source inapplicability. See [MEM-RTE-learning-reuse](memory.md#mem-rte-learning-reuse), [MEM-RTE-conversation-reuse](memory.md#mem-rte-conversation-reuse), [MEM-OBJ-session-history](memory.md#mem-obj-session-history) and [MEM-CLM-service-boundary](memory.md#mem-clm-service-boundary).

Automatic model/tool admission is distinct from human authorship. Explicit user editing affords manual admission; generic API submission and remote Git authorship do not identify a human decision. Running a loader or evaluator does not make each metadata insertion or file removal manual. These distinctions preserve known mechanisms without assigning unknown initial or alternative content control. See [MEM-OBJ-user-files](memory.md#mem-obj-user-files), [RT-RTE-raw-ingest](runtime.md#rt-rte-raw-ingest), [RT-RTE-git-sync](runtime.md#rt-rte-git-sync), [RT-RTE-context-refresh](runtime.md#rt-rte-context-refresh) and [RT-RTE-evaluation-driver](runtime.md#rt-rte-evaluation-driver).
