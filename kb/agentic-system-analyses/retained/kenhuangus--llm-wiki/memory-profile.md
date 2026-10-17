---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "LLM Wiki memory profile: retained source and wiki files, admission state, evaluation feedback and later synthesis at the frozen revision."
run-id: AAS-2026-10-17-llm-wiki-507fade8a56e-01
source-identity: https://github.com/kenhuangus/llm-wiki
reviewed-boundary: d2bd485921f6c7b6071afbb389f44ab8e4e83c69
memory-comparison:
  version: 2
  scope: >-
    Accumulated raw/normalized sources, extraction sidecars, wiki bodies and
    frontmatter, newsletters, catalogs and operation/research notes, generated
    paper drafts, monitor admission rows, evaluation fixtures/manifest and
    operational metrics/experiments; their acquisition, editing, maintenance,
    access and later-consumer routes. Includes unresolved initial curated-table
    admission, generic API caller control and metric producer provenance.
    Excludes static shipped prompts, prompt-registry constants and governance,
    current-call messages and transient queues, and external provider weights,
    hidden provider retention and coding-agent host memory. Git history is an
    externally populated historical-read alternative, not automatic save storage.
  axes:
    storage_substrate:
      assessment: known
      units:
        - scope: "Raw/normalized source text, JSON sidecars and their access fields"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-normalized, memory.md#mem-obj-extracted, memory.md#mem-rte-curated-poll]
              note: "Acquisition, normalization and extraction persist ordinary filesystem artifacts."
          records: [memory.md#mem-obj-normalized, memory.md#mem-obj-extracted, memory.md#mem-rte-curated-poll]
          note: "Markdown and JSON are encodings on the same file substrate, not graph storage."
        - scope: "Wiki bodies/frontmatter, curated table, newsletters, catalog, operation/research notes and paper outputs"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-wiki-body, memory.md#mem-obj-wiki-metadata, memory.md#mem-obj-newsletters, memory.md#mem-rte-curated-poll, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-wiki-consumption, runtime.md#rt-obj-metrics]
              note: "These producers and consumers write or reload Markdown/log/draft files; output availability in a deployment is not asserted."
          records: [memory.md#mem-obj-wiki-body, memory.md#mem-obj-wiki-metadata, memory.md#mem-obj-newsletters, memory.md#mem-rte-curated-poll, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-wiki-consumption, runtime.md#rt-obj-metrics]
          note: "Covers the retained file outputs and their metadata, not transient BM25 objects or model context copies."
        - scope: "Monitor admission state and operational metric/experiment rows"
          assessment: known
          findings:
            - value: sqlite
              basis: wired
              records: [memory.md#mem-obj-ingested-ids, runtime.md#rt-obj-metrics]
              note: "state.db and metrics.db use SQLite tables; unavailable actual DB contents do not obscure the inspected storage mechanism."
          records: [memory.md#mem-obj-ingested-ids, runtime.md#rt-obj-metrics]
          note: "Local SQL storage, distinct from human-readable experiment notes."
        - scope: "Evaluation fixture inputs, generated outputs and manifest"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-eval-set]
              note: "Builder copies Markdown and writes a JSON manifest; evaluation overwrites file sidecars."
          records: [memory.md#mem-obj-eval-set]
          note: "No independent expected-answer store is implied."
        - scope: "Requested historical versions backed by externally existing commits"
          assessment: known
          findings:
            - value: repo
              basis: afforded
              records: [runtime.md#rt-rte-api-mutation]
              note: "Git history endpoints afford retrieval of versions if an external actor made commits."
          records: [runtime.md#rt-rte-api-mutation]
          note: "API save does not create a commit; this alternative is not promoted to automatic checkpoint wiring."
      records: [memory.md#mem-obj-normalized, memory.md#mem-obj-extracted, memory.md#mem-obj-wiki-body, memory.md#mem-obj-wiki-metadata, memory.md#mem-obj-newsletters, memory.md#mem-rte-curated-poll, memory.md#mem-obj-ingested-ids, memory.md#mem-obj-eval-set, runtime.md#rt-obj-metrics, runtime.md#rt-rte-api-mutation, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-wiki-consumption]
      note: "The recorded inventory resolves substrate within the scoped client memory boundary. Provider internals and host memory are excluded, not classified from readable client payloads."
    representational_form:
      assessment: known
      units:
        - scope: "Source, claim, evidence, wiki/newsletter, research/experiment-note and draft text interpreted by people or models"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-normalized, memory.md#mem-obj-extracted, memory.md#mem-obj-wiki-body, memory.md#mem-obj-newsletters, runtime.md#rt-obj-metrics, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-wiki-consumption]
              note: "Prose supplies subject matter, summaries, hypotheses or model context through interpretation."
          records: [memory.md#mem-obj-normalized, memory.md#mem-obj-extracted, memory.md#mem-obj-wiki-body, memory.md#mem-obj-newsletters, runtime.md#rt-obj-metrics, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-wiki-consumption]
          note: "JSON containment does not make the meaning of claim text symbolic. Historical retrieval preserves the retrieved text's form."
        - scope: "IDs, paths, link-matching strings, sidecar structure, frontmatter, fixture manifest, SQLite rows and numeric/string selectors"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-normalized, memory.md#mem-obj-extracted, memory.md#mem-obj-wiki-body, memory.md#mem-obj-wiki-metadata, memory.md#mem-obj-ingested-ids, memory.md#mem-obj-eval-set, runtime.md#rt-obj-metrics, runtime.md#rt-rte-api-mutation, runtime.md#rt-rte-wiki-consumption, memory.md#mem-rte-curated-poll]
              note: "Fixed parsing, equality, thresholds, table-column extraction, token scoring and path rules consume localized fields. Wiki text is also a symbolic token/link input on those paths."
          records: [memory.md#mem-obj-normalized, memory.md#mem-obj-extracted, memory.md#mem-obj-wiki-body, memory.md#mem-obj-wiki-metadata, memory.md#mem-obj-ingested-ids, memory.md#mem-obj-eval-set, runtime.md#rt-obj-metrics, runtime.md#rt-rte-api-mutation, runtime.md#rt-rte-wiki-consumption, memory.md#mem-rte-curated-poll]
          note: "These are separate consumption paths from interpretation of the same serialized text. Confidence numbers are not distributed parameters."
      records: [memory.md#mem-obj-normalized, memory.md#mem-obj-extracted, memory.md#mem-obj-wiki-body, memory.md#mem-obj-wiki-metadata, memory.md#mem-obj-newsletters, memory.md#mem-obj-ingested-ids, memory.md#mem-obj-eval-set, memory.md#mem-rte-curated-poll, runtime.md#rt-obj-metrics, runtime.md#rt-rte-api-mutation, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-wiki-consumption]
      note: "The recorded file/SQL inventory separates interpreted prose from fixed-rule access parts. External inference components are not accumulated memory in this scope."
    lineage:
      assessment: partial
      units:
        - scope: "Acquired source documents and normalized bodies"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-obj-normalized, memory.md#mem-rte-curated-poll, runtime.md#rt-rte-batch-ingestion]
              note: "External files/feed/search material enters persistent source files; normalization does not authenticate it."
          records: [memory.md#mem-obj-normalized, memory.md#mem-rte-curated-poll, runtime.md#rt-rte-batch-ingestion]
          note: "Import is known despite unresolved source truth and per-item authorship."
        - scope: "Inspected derivation of sidecars, claim projection/merges, catalogs, metadata, newsletters, fixtures and drafts"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-extracted, epistemic.md#epi-rte-claim-projection, memory.md#mem-obj-wiki-body, memory.md#mem-obj-wiki-metadata, memory.md#mem-obj-newsletters, memory.md#mem-obj-eval-set, runtime.md#rt-rte-wiki-consumption, runtime.md#rt-rte-research-maintenance]
              note: "Software/model projections, copying, aggregation and generation derive these artifacts from retained source/page material; their scientific semantics need not be known to establish derivation."
          records: [memory.md#mem-obj-extracted, epistemic.md#epi-rte-claim-projection, memory.md#mem-obj-wiki-body, memory.md#mem-obj-wiki-metadata, memory.md#mem-obj-newsletters, memory.md#mem-obj-eval-set, runtime.md#rt-rte-wiki-consumption, runtime.md#rt-rte-research-maintenance]
          note: "This unit names the inspected derivation routes, not the complete initialization history of every shipped file."
        - scope: "Browser-supplied page replacements"
          assessment: known
          findings:
            - value: authored
              basis: wired
              records: [runtime.md#rt-rte-api-mutation]
              note: "The React editor explicitly supplies human-edited content to save, independently of the generic API-caller alternative."
          records: [runtime.md#rt-rte-api-mutation]
          note: "The editor path establishes authored replacement, not authorship of all API payloads."
        - scope: "Operational metrics and experiment/research summaries derived from execution feedback"
          assessment: partial
          findings:
            - value: trace-extracted
              basis: wired
              records: [runtime.md#rt-obj-metrics, runtime.md#rt-rte-prompt-optimization, runtime.md#rt-rte-research-maintenance]
              note: "Process/JSON outcomes, errors, counts and decisions are recorded and summarized for later optimizer use."
          records: [runtime.md#rt-obj-metrics, runtime.md#rt-rte-prompt-optimization, runtime.md#rt-rte-research-maintenance]
          note: "The memory annotation retains incomplete initial metric-row producer coverage; this witness cannot resolve every row's provenance."
        - scope: "Initial curated-table entries, shipped fixture initialization, arbitrary API replacement payloads and externally committed historical content"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-curated-poll, memory.md#mem-obj-eval-set, runtime.md#rt-rte-api-mutation]
          note: "Known subsequent reads/copies/saves do not establish initial authorship or upstream derivation of these alternatives."
      records: [memory.md#mem-obj-normalized, memory.md#mem-obj-extracted, memory.md#mem-obj-wiki-body, memory.md#mem-obj-wiki-metadata, memory.md#mem-obj-newsletters, memory.md#mem-obj-eval-set, memory.md#mem-rte-curated-poll, epistemic.md#epi-rte-claim-projection, runtime.md#rt-obj-metrics, runtime.md#rt-rte-batch-ingestion, runtime.md#rt-rte-api-mutation, runtime.md#rt-rte-prompt-optimization, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-wiki-consumption]
      note: "Imported, compiled, authored and trace-derived paths coexist; unresolved initialization and generic caller provenance prevent a complete lineage inventory."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Source/fixture text to extraction, retained old claims and wiki/newsletter/notes to later models or requested readers"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [memory.md#mem-obj-normalized, memory.md#mem-obj-eval-set, runtime.md#rt-rte-knowledge-admission, runtime.md#rt-bap-wiki-context, runtime.md#rt-rte-wiki-consumption, runtime.md#rt-obj-metrics]
              note: "Bodies and excerpts provide subject matter, evidence or reference context; knowledge authority does not certify truth."
          records: [memory.md#mem-obj-normalized, memory.md#mem-obj-eval-set, runtime.md#rt-rte-knowledge-admission, runtime.md#rt-bap-wiki-context, runtime.md#rt-rte-wiki-consumption, runtime.md#rt-obj-metrics]
          note: "Explicit evidence fields omitted by integration gain no invented downstream authority."
        - scope: "Retained wiki text as BM25 token-scoring input"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [runtime.md#rt-rte-wiki-consumption]
              note: "Current file text determines relative BM25 scores under fixed code, including frontmatter and unverified/conflict text."
          records: [runtime.md#rt-rte-wiki-consumption]
          note: "Ranking influence requires neither learned weights nor a persistent search index."
        - scope: "Admission rows and sidecar-existence checkpoints at acquisition/extraction gates"
          assessment: known
          findings:
            - value: enforcement
              basis: wired
              records: [memory.md#mem-obj-ingested-ids, runtime.md#rt-rte-batch-ingestion]
              note: "Existing IDs suppress reacquisition and existing sidecars suppress extraction."
            - value: validation
              basis: wired
              records: [memory.md#mem-obj-ingested-ids, runtime.md#rt-rte-batch-ingestion]
              note: "Retained identity/existence state supplies the criterion for whether a candidate enters processing on these routes; this is not factual validation."
          records: [memory.md#mem-obj-ingested-ids, runtime.md#rt-rte-batch-ingestion]
          note: "The same retained checkpoint is a criterion and an enforced veto at its actual consumer."
        - scope: "Frontmatter/mtime, fixture paths, curated query table and metric/experiment state at code selectors"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-wiki-metadata, memory.md#mem-obj-eval-set, memory.md#mem-rte-curated-poll, runtime.md#rt-obj-metrics, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-prompt-optimization, epistemic.md#epi-rte-newsletter-context]
              note: "Retained fields choose eligible research/validation tasks, evaluation inputs, acquisition queries, optimizer hypothesis focus and newsletter context."
          records: [memory.md#mem-obj-wiki-metadata, memory.md#mem-obj-eval-set, memory.md#mem-rte-curated-poll, runtime.md#rt-obj-metrics, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-prompt-optimization, epistemic.md#epi-rte-newsletter-context]
          note: "Confidence/status displays are not generalized content enforcement; notably conflict state does not quarantine reads."
        - scope: "Retained operational metrics consumed in automatic durable experiment-feedback updates"
          assessment: partial
          findings:
            - value: learning
              basis: wired
              records: [runtime.md#rt-obj-metrics, runtime.md#rt-rte-prompt-optimization]
              note: "Execution-derived aggregates feed retained experiment decisions/hypotheses and counts that affect later optimizer cycles, rather than merely being displayed."
          records: [runtime.md#rt-obj-metrics, runtime.md#rt-rte-prompt-optimization]
          note: "This local update-consumer force does not imply learned parameters, improved capacity or installed candidate prompts; complete metric-producer history is unresolved."
        - scope: "Authority of externally committed historical replacements and unaudited initial curated/fixture content beyond recorded consumers"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-api-mutation, memory.md#mem-rte-curated-poll, memory.md#mem-obj-eval-set]
          note: "Recorded historical reads and known selectors do not establish all uses or effects of externally initialized content. No retained standing-instruction update is inferred from a generic text save."
      records: [memory.md#mem-obj-normalized, memory.md#mem-obj-eval-set, memory.md#mem-obj-ingested-ids, memory.md#mem-obj-wiki-metadata, memory.md#mem-rte-curated-poll, runtime.md#rt-obj-metrics, runtime.md#rt-rte-api-mutation, runtime.md#rt-rte-batch-ingestion, runtime.md#rt-rte-knowledge-admission, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-prompt-optimization, runtime.md#rt-rte-wiki-consumption, runtime.md#rt-bap-wiki-context, epistemic.md#epi-rte-newsletter-context]
      note: "Positive forces attach to actual consumers; unresolved history does not erase them or justify complete authority enumeration. Static prompt instruction authority is outside accumulated memory scope."
    write_agency:
      assessment: partial
      units:
        - scope: "Acquisition/normalization, extraction/integration, monitor rows, metrics/experiment logging, fixture construction, lint/validator and synthesis/draft admissions"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-batch-ingestion, runtime.md#rt-rte-knowledge-admission, runtime.md#rt-rte-scheduled-drivers, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-prompt-optimization, runtime.md#rt-rte-wiki-consumption, memory.md#mem-obj-ingested-ids, memory.md#mem-obj-eval-set, memory.md#mem-rte-curated-poll, epistemic.md#epi-rte-newsletter-admission]
              note: "Software/model decisions admit each result without per-content human approval. Starting a CLI cycle is not manual admission of its outputs."
          records: [runtime.md#rt-rte-batch-ingestion, runtime.md#rt-rte-knowledge-admission, runtime.md#rt-rte-scheduled-drivers, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-prompt-optimization, runtime.md#rt-rte-wiki-consumption, memory.md#mem-obj-ingested-ids, memory.md#mem-obj-eval-set, memory.md#mem-rte-curated-poll, epistemic.md#epi-rte-newsletter-admission]
          note: "Known subsequent admissions, distinct from unresolved initialization of their inputs."
        - scope: "React editor save of human-supplied article content"
          assessment: known
          findings:
            - value: manual
              basis: wired
              records: [runtime.md#rt-rte-api-mutation]
              note: "Human edits and submits the replacement content; backend physical I/O does not erase that explicit decision."
          records: [runtime.md#rt-rte-api-mutation]
          note: "This separately evidenced browser path does not establish the identity of every API client."
        - scope: "Generic API saves/uploads, initial curated-table and shipped fixture admission, external historical commits and RSS reset caller"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-api-mutation, memory.md#mem-rte-curated-poll, memory.md#mem-obj-eval-set, memory.md#mem-rte-rss-reset]
          note: "Caller invocation and editable content do not by themselves distinguish human per-content control from software admission. External commit and initial-entry decisions are not reconstructed."
      records: [runtime.md#rt-rte-batch-ingestion, runtime.md#rt-rte-knowledge-admission, runtime.md#rt-rte-scheduled-drivers, runtime.md#rt-rte-api-mutation, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-prompt-optimization, runtime.md#rt-rte-wiki-consumption, memory.md#mem-obj-ingested-ids, memory.md#mem-obj-eval-set, memory.md#mem-rte-curated-poll, memory.md#mem-rte-rss-reset, epistemic.md#epi-rte-newsletter-admission]
      note: "Automatic processing and manual browser edits coexist; untyped callers and initial admission prevent complete coverage."
    curation_operations:
      assessment: partial
      units:
        - scope: "Deterministic retained-claim/context reduction and evaluation aggregation"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [epistemic.md#epi-rte-claim-projection, epistemic.md#epi-rte-newsletter-context, runtime.md#rt-rte-prompt-optimization, runtime.md#rt-obj-metrics]
              note: "Claim projection selects existing claims into a reduced body, newsletter context selects bounded retained snippets, and metric aggregates reduce retained execution records. No new proposition is required for these reductions."
          records: [epistemic.md#epi-rte-claim-projection, epistemic.md#epi-rte-newsletter-context, runtime.md#rt-rte-prompt-optimization, runtime.md#rt-obj-metrics]
          note: "These inspected fixed transformations do not certify semantic preservation in subsequent model generations."
        - scope: "Existing page/body/frontmatter replacement and augmentation"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [memory.md#mem-obj-wiki-body, memory.md#mem-obj-wiki-metadata, runtime.md#rt-rte-api-mutation, runtime.md#rt-rte-research-maintenance]
              note: "Integration, edits, conflict annotations and validator updates revise retained entries."
          records: [memory.md#mem-obj-wiki-body, memory.md#mem-obj-wiki-metadata, runtime.md#rt-rte-api-mutation, runtime.md#rt-rte-research-maintenance]
          note: "Revision is wired even where semantic fidelity and operator purpose are unresolved."
        - scope: "Confidence reinforcement and newsletter verification-tier assignment"
          assessment: known
          findings:
            - value: promote
              basis: wired
              records: [epistemic.md#epi-rte-confidence-update, epistemic.md#epi-rte-newsletter-admission]
              note: "Rules raise confidence on existing pages and assign derived newsletters verified/high-confidence standing in the retained wiki."
          records: [epistemic.md#epi-rte-confidence-update, epistemic.md#epi-rte-newsletter-admission]
          note: "This is tier/salience promotion, not independently warranted corroboration or truth acceptance."
        - scope: "Semantic operations within model extraction/merges and newsletter/paper generation"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-knowledge-admission, runtime.md#rt-rte-wiki-consumption, epistemic.md#epi-rte-newsletter-admission]
          note: "Requested merging, summarization or novelty does not distinguish consolidation from synthesis in actual unavailable model outputs. Nonempty output admission supplies no semantic test."
        - scope: "Dependency withdrawal, arbitrary edit semantics and admission-state deletion"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-rss-reset, runtime.md#rt-rte-api-mutation, runtime.md#rt-rte-research-maintenance]
          note: "RSS reset deletes admission history, not dependent knowledge. Conflict flags do not withdraw read reliance; direct replacement alone does not prove decay, deduplication or cascading invalidation."
      records: [epistemic.md#epi-rte-claim-projection, epistemic.md#epi-rte-newsletter-context, epistemic.md#epi-rte-confidence-update, epistemic.md#epi-rte-newsletter-admission, memory.md#mem-obj-wiki-body, memory.md#mem-obj-wiki-metadata, memory.md#mem-rte-rss-reset, runtime.md#rt-obj-metrics, runtime.md#rt-rte-api-mutation, runtime.md#rt-rte-knowledge-admission, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-prompt-optimization, runtime.md#rt-rte-wiki-consumption]
      note: "Implemented reductions, revisions and promotions survive unresolved semantic branches. Acquisition deduplication and catalog rebuild names do not add memory deduplication or synthesis findings."
    read_back_direction:
      assessment: known
      units:
        - scope: "Requested CLI/API query, article, backlink, log and historical retrieval"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-api-mutation, runtime.md#rt-rte-wiki-consumption]
              note: "Explicit queries/paths request retained material; ranking and returning the requested results are not a second unsolicited delivery."
          records: [runtime.md#rt-rte-api-mutation, runtime.md#rt-rte-wiki-consumption]
          note: "Current-file retrieval is wired; historical payload availability depends on external commits."
        - scope: "Historical-content delivery if externally created Git commits exist"
          assessment: known
          findings:
            - value: pull
              basis: afforded
              records: [runtime.md#rt-rte-api-mutation]
              note: "The history route affords requested access, without a wired checkpoint-producing save route."
          records: [runtime.md#rt-rte-api-mutation]
          note: "Kept separate from live-file reads to preserve its conditional warrant."
        - scope: "Write-triggered old-body reuse, paper/newsletter context, evaluation inputs, admission/maintenance/optimizer selectors and curated polling"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-knowledge-admission, runtime.md#rt-rte-wiki-consumption, runtime.md#rt-rte-batch-ingestion, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-prompt-optimization, memory.md#mem-obj-eval-set, memory.md#mem-obj-ingested-ids, memory.md#mem-rte-curated-poll]
              note: "After an ingestion, maintenance, generation or monitor trigger, code supplies retained material/state to downstream consumers that did not independently request those retained parts."
          records: [runtime.md#rt-rte-knowledge-admission, runtime.md#rt-rte-wiki-consumption, runtime.md#rt-rte-batch-ingestion, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-prompt-optimization, memory.md#mem-obj-eval-set, memory.md#mem-obj-ingested-ids, memory.md#mem-rte-curated-poll]
          note: "An upstream CLI/operator choice supplies trigger or targeting inputs, not a separate request by the receiving model."
      records: [runtime.md#rt-rte-api-mutation, runtime.md#rt-rte-wiki-consumption, runtime.md#rt-rte-knowledge-admission, runtime.md#rt-rte-batch-ingestion, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-prompt-optimization, memory.md#mem-obj-eval-set, memory.md#mem-obj-ingested-ids, memory.md#mem-rte-curated-poll]
      note: "The scoped inventory contains both requested returns and independent downstream supply. Unresolved write provenance does not obscure direction on these recorded consumer routes."
    read_back_signal:
      assessment: known
      units:
        - scope: "Integration target and identity-based monitor/sidecar/manifest selection after driver triggers"
          assessment: known
          findings:
            - value: identifier
              basis: wired
              records: [runtime.md#rt-rte-knowledge-admission, runtime.md#rt-rte-batch-ingestion, memory.md#mem-obj-ingested-ids, memory.md#mem-obj-eval-set]
              note: "Integration destination equality selects the saved old body for model delivery; item IDs select admission rows, sidecar paths select checkpoints, and manifest paths select fixture bodies after evaluation launch."
          records: [runtime.md#rt-rte-knowledge-admission, runtime.md#rt-rte-batch-ingestion, memory.md#mem-obj-ingested-ids, memory.md#mem-obj-eval-set]
          note: "These identities select consumed retained parts. An identifier merely displayed in an article request is not counted."
        - scope: "Newsletter, deep lint, curated polling, retrospective/research scans and optimizer time-window supply"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [epistemic.md#epi-rte-newsletter-context, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-prompt-optimization, memory.md#mem-rte-curated-poll]
              note: "Generation/maintenance/poll triggers use recentness, category, confidence/count thresholds, table membership, group membership or time windows to supply pages, fields, table entries and metric rows."
          records: [epistemic.md#epi-rte-newsletter-context, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-prompt-optimization, memory.md#mem-rte-curated-poll]
          note: "Count/prefix budgets and broad eligibility remain coarse rather than semantic targeting."
        - scope: "Paper topic-to-page matching after paper-generation trigger"
          assessment: known
          findings:
            - value: inferred-lexical
              basis: wired
              records: [runtime.md#rt-rte-wiki-consumption]
              note: "Topic-string containment in retained page text selects matches for delivery to the analysis model."
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-wiki-consumption]
              note: "Traversal order, first-five matching pages and 2,000-character prefixes limit the lexically selected context."
          records: [runtime.md#rt-rte-wiki-consumption]
          note: "Optional model topic choice is upstream; the retained-page selector itself is lexical, not an embedding or model relevance judgment."
      records: [runtime.md#rt-rte-knowledge-admission, runtime.md#rt-rte-batch-ingestion, memory.md#mem-obj-ingested-ids, memory.md#mem-obj-eval-set, epistemic.md#epi-rte-newsletter-context, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-prompt-optimization, memory.md#mem-rte-curated-poll, runtime.md#rt-rte-wiki-consumption]
      note: "Every recorded push family has an identified selector. Requested BM25 search remains pull, so its lexical scoring does not independently add a push finding."
    trace_learning:
      assessment: partial
      units:
        - scope: "Optimizer execution-feedback to retained experiment/hypothesis/decision state and later proposal selection"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [runtime.md#rt-obj-metrics, runtime.md#rt-rte-prompt-optimization]
              note: "Automatic feedback processing writes durable experiment state; retained failures, experiments/counts and aggregates shape subsequent optimizer cycles. This is a behavior-shaping feedback artifact, not just an unused log."
          records: [runtime.md#rt-obj-metrics, runtime.md#rt-rte-prompt-optimization]
          note: "The qualifying result is retained optimizer state, not the proposed prompt: candidate wording is neither installed nor saved as active guidance. No improvement is asserted."
        - scope: "Complete metric-row producer coverage and other retained operational/research logs"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-metrics, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-prompt-optimization, runtime.md#rt-rte-wiki-consumption]
          note: "All original producers and qualifying durable-update/later-consumer chains are not established. Raw logging or possible topic-matched log reuse is not enough to classify every branch as learning."
        - scope: "Ordinary external-source knowledge processing, direct article edits and page-to-page synthesis/metadata maintenance"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-obj-normalized, memory.md#mem-obj-extracted, memory.md#mem-obj-wiki-body, memory.md#mem-obj-newsletters, epistemic.md#epi-rte-confidence-update, runtime.md#rt-rte-api-mutation]
          note: "These recorded inputs are source documents, page claims or caller text, not identified activity traces feeding a trace-learning write. This does not establish a system-wide no or classify unknown input histories."
      records: [runtime.md#rt-obj-metrics, runtime.md#rt-rte-prompt-optimization, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-wiki-consumption, memory.md#mem-obj-normalized, memory.md#mem-obj-extracted, memory.md#mem-obj-wiki-body, memory.md#mem-obj-newsletters, epistemic.md#epi-rte-confidence-update, runtime.md#rt-rte-api-mutation]
      note: "A positive local automatic trace-fed feedback route coexists with unresolved producer coverage. Neither missing prompt installation nor missing benefit erases that route; neither makes all logs qualifying."
    trace_source:
      assessment: partial
      units:
        - scope: "Inspected optimizer fixture-execution feedback feeding retained experiment updates"
          assessment: known
          findings:
            - value: tool-traces
              basis: wired
              records: [runtime.md#rt-rte-prompt-optimization, runtime.md#rt-obj-metrics, memory.md#mem-obj-eval-set]
              note: "Subprocess extraction success/failure, JSON-load outcomes and returned confidence/count aggregates are execution feedback consumed by the experiment update."
          records: [runtime.md#rt-rte-prompt-optimization, runtime.md#rt-obj-metrics, memory.md#mem-obj-eval-set]
          note: "Original feedback is tool execution, not conversational session turns. Fixture source documents are static task inputs, not automatically trace sources themselves."
        - scope: "Other extraction/integration/research metric producers and any mixed original feedback inputs"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-metrics, runtime.md#rt-rte-research-maintenance, runtime.md#rt-rte-prompt-optimization]
          note: "Incomplete producer/provenance coverage prevents enumerating original trace content for all qualifying alternatives. Timestamps alone do not establish event-streams; no linked state-action-outcome experience is inferred."
        - scope: "Non-trace source/page processing and caller edits, outside a qualifying trace-fed route"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-obj-normalized, memory.md#mem-obj-wiki-body, memory.md#mem-obj-newsletters, runtime.md#rt-rte-api-mutation, epistemic.md#epi-rte-confidence-update]
          note: "Source-document lineage and page metadata are not a trace origin without a qualifying trace-fed write. This local exclusion does not make the partial axis inapplicable."
      records: [runtime.md#rt-rte-prompt-optimization, runtime.md#rt-obj-metrics, memory.md#mem-obj-eval-set, runtime.md#rt-rte-research-maintenance, memory.md#mem-obj-normalized, memory.md#mem-obj-wiki-body, memory.md#mem-obj-newsletters, runtime.md#rt-rte-api-mutation, epistemic.md#epi-rte-confidence-update]
      note: "Tool feedback is positively classified on the inspected experiment branch; unresolved initial metric producers prevent a complete trace-source union."
---

# LLM Wiki memory profile

## Comparison rationale

The comparison covers accumulated client-side artifacts and their consumers, not every store used by the runtime. The retained file/SQLite inventory is supported by [MEM-OBJ-normalized](memory.md#mem-obj-normalized), [MEM-OBJ-extracted](memory.md#mem-obj-extracted), [MEM-OBJ-wiki-body](memory.md#mem-obj-wiki-body), [MEM-OBJ-wiki-metadata](memory.md#mem-obj-wiki-metadata), [MEM-OBJ-newsletters](memory.md#mem-obj-newsletters), [MEM-OBJ-ingested-ids](memory.md#mem-obj-ingested-ids), [MEM-OBJ-eval-set](memory.md#mem-obj-eval-set) and [RT-OBJ-metrics](runtime.md#rt-obj-metrics). The model services are external dependencies, not evidence of accumulated parameter memory. Static prompt instructions and the process-local registry are excluded. Historical access is retained as a conditional alternative: [RT-RTE-api-mutation](runtime.md#rt-rte-api-mutation) does not turn article saves into Git checkpoints.

Reconciliation supersedes EPI-OBJ-eval-set with [MEM-OBJ-eval-set](memory.md#mem-obj-eval-set); all fixture findings cite the latter. No other supersession changes a value. The normalized body and full normalized document, extracted claim/evidence parts and full sidecar, and broad wiki-body/frontmatter accounts remain valid overlapping parts and containers. They are not independent stores or independent corroborating evidence.

Natural-language and symbolic findings describe consumption, not extensions. The same wiki text supplies interpreted model context through [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context), BM25 ranking input through [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption), and literal backlink matching through [RT-RTE-api-mutation](runtime.md#rt-rte-api-mutation). Confidence, status and source count route fixed-rule maintenance, but do not establish factual warrant or quarantine. Monitor ID rows and sidecar existence do enforce bounded admission decisions. Their access checks do not establish memory-content deduplication.

The browser editor establishes manual content replacement independently of the generic API-client branch. Software admission remains automatic for extraction, integration and maintenance even after an operator launches a cycle. Initial curated-table entries, fixture history, external commits and generic caller identity remain unresolved under [MEM-RTE-curated-poll](memory.md#mem-rte-curated-poll), [MEM-OBJ-eval-set](memory.md#mem-obj-eval-set) and [RT-RTE-api-mutation](runtime.md#rt-rte-api-mutation).

Curation positives are restricted to implemented reductions, revisions and promotions. [EPI-RTE-claim-projection](epistemic.md#epi-rte-claim-projection) and [EPI-RTE-newsletter-context](epistemic.md#epi-rte-newsletter-context) reduce retained inputs without adding claims at those edges. Subsequent model semantics remain unresolved; a request for novelty does not establish synthesis. [EPI-RTE-confidence-update](epistemic.md#epi-rte-confidence-update) raises a reliance label without new corroboration, while [EPI-RTE-newsletter-admission](epistemic.md#epi-rte-newsletter-admission) promotes derived output to verified/high-confidence standing after a length gate. Conflict annotations do not establish withdrawal, and [MEM-RTE-rss-reset](memory.md#mem-rte-rss-reset) resets admission history rather than dependent knowledge.

Read-back separates explicit material requests from automatic downstream supply. Search returns remain pull even though BM25 selects results. A merge receives an automatically selected old destination body; newsletter, paper, maintenance and optimizer consumers receive code-selected retained inputs. Topic matching is lexical, recentness/category/budget selection is coarse, and destination equality is identifier selection. Upstream operator or model topic choice does not replace the actual retained-page selector in [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption).

The trace-learning positive is deliberately local. [RT-OBJ-metrics](runtime.md#rt-obj-metrics) and [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization) establish automatic execution-feedback processing, retained experiment/hypothesis/decision state and later cycle dependence. Those artifacts shape optimizer behavior even though the proposed prompt is not installed. They support learning authority at that update consumer and a wired trace-learning route, not parameter training, improved future capacity, successful self-improvement or a candidate-to-production-method loop. Incomplete metric producer provenance prevents complete coverage. Recorded fixture subprocess/JSON feedback supports tool-traces on its own branch; no session-logs, event-streams or trajectories value is inferred from timestamps or static source documents. Ordinary page feedback is not silently reclassified as runtime experience.

No new records, source quotations or source evidence were added. No frozen-source files were read for this classification; the supplied accepted records and their annotations supply the warrants. All positive implementation findings remain wiring or affordance, not observed operation or causal benefit. The profile's local coverage assessments do not upgrade those evidence bases.
