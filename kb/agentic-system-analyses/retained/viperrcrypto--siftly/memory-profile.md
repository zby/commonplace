---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Siftly memory profile: SQLite bookmark knowledge, derived access structures, request caches,
  exports and opaque external retention at the frozen revision.'
run-id: AAS-2026-10-18-siftly-b81c94cf0f77-01
source-identity: https://github.com/ViperrCrypto/Siftly
reviewed-boundary: b25daa45b858f4be096b5c368671c34db4407d8e
memory-comparison:
  version: 2
  scope: Retained imported bookmarks/rawJson, extracted entities, image and semantic metadata, category
    guidance and memberships, processing markers, FTS5, hydrated search cache, updated configuration and
    derived exports; their write, maintenance and later-consumer routes. External CLI context/checkpoint
    and provider-retention alternatives remain included but uninspected at Siftly adapters. Excludes static
    instructions as independent memory, ordinary current-run queues/progress, executor weights without
    established use-dependent updates, remote service internals beyond the adapter boundary and hypothetical
    external helper callers.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: SQLite imported content, entities, image/semantic metadata, category guidance, memberships,
          processing markers and FTS5
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records: &id001
          - memory.md#mem-obj-raw-json
          - memory.md#mem-obj-entities
          - memory.md#mem-obj-image-tags
          - memory.md#mem-obj-semantic-tags
          - memory.md#mem-obj-category
          - memory.md#mem-obj-bookmark-category
          - memory.md#mem-obj-bookmark-fts
          - runtime.md#rt-rte-settings-change
          note: Prisma rows and the FTS5 table persist these local parts, including updated configuration
            rows.
        records: *id001
        note: Each named local retained part is stored in SQLite. FTS is a virtual table, not a vector
          or graph store.
      - scope: AI search hydrated-response cache
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id002
          - memory.md#mem-obj-search-cache
          note: Five-minute response reuse uses a module-local Map.
        records: *id002
        note: This Map persists across requests within one process, not restarts.
      - scope: Obsidian Markdown notes and indexes
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id003
          - memory.md#mem-obj-export-copy
          - runtime.md#rt-rte-cli-export
          note: Notes and category/author indexes are written to the selected vault.
        records: *id003
        note: The exporter writes independent filesystem artifacts; caller persistence of download responses
          is not assumed.
      - scope: Downloaded CSV/JSON/ZIP response copies after HTTP delivery
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-export-copy
        note: Response formats are inspected, but whether and where a caller retains downloaded files
          is not supplied.
      - scope: Included external Claude/Codex retained context, checkpoints and provider-owned state at
          the adapter boundary
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-model-dispatch
        note: No external CLI checkpoint or provider retention substrate was inspected; endpoint execution
          alone does not establish a service-object memory store.
      records:
      - memory.md#mem-obj-raw-json
      - memory.md#mem-obj-entities
      - memory.md#mem-obj-image-tags
      - memory.md#mem-obj-semantic-tags
      - memory.md#mem-obj-category
      - memory.md#mem-obj-bookmark-category
      - memory.md#mem-obj-bookmark-fts
      - runtime.md#rt-rte-settings-change
      - memory.md#mem-obj-search-cache
      - memory.md#mem-obj-export-copy
      - runtime.md#rt-rte-cli-export
      - runtime.md#rt-rte-model-dispatch
      note: The collection, access index, process cache and filesystem export have established substrates.
        Included external retained state is opaque; remote model weights are executors, not an established
        use-accumulated memory store.
    representational_form:
      assessment: partial
      units:
      - scope: Imported tweet text and readable author content at model and human consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id004
          - memory.md#mem-obj-raw-json
          note: Tweet text supplies model/human context.
        records: *id004
        note: Readable content is interpreted as language; rawJson packaging is not a fourth form.
      - scope: Imported identities, dates and rawJson fields at parsers, joins and selectors
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id005
          - memory.md#mem-obj-raw-json
          - memory.md#mem-obj-entities
          note: IDs, dates and field tests have localized fixed semantics.
        records: *id005
        note: This classification covers the fixed-rule extraction/selection path, not every uninterpreted
          nested payload value.
      - scope: Successful image descriptions/OCR, semantic strings and category descriptions at prompts,
          CLI and human readers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id006
          - memory.md#mem-obj-image-tags
          - memory.md#mem-obj-semantic-tags
          - memory.md#mem-obj-category
          - memory.md#mem-obj-export-copy
          note: Models and readers interpret descriptions, tags and classification guidance.
        records: *id006
        note: Language values remain natural language despite JSON serialization.
      - scope: Memberships/confidence, category identities, failure/empty markers, enrichedAt, configuration
          and FTS tokens at fixed consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id007
          - memory.md#mem-obj-bookmark-category
          - memory.md#mem-obj-image-tags
          - memory.md#mem-obj-semantic-tags
          - memory.md#mem-obj-category
          - memory.md#mem-obj-bookmark-fts
          - runtime.md#rt-rte-settings-change
          note: Code compares markers and IDs, orders scores and matches lexical tokens.
        records: *id007
        note: This is a separate path from the semantic interpretation of the same text. Numeric confidence
          is a localized score, not distributed parameters.
      - scope: Cached response content and exports at their respective consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id008
          - memory.md#mem-obj-search-cache
          - memory.md#mem-obj-export-copy
          note: Cached explanations and exported tweet text are read as language.
        - value: symbolic
          basis: wired
          records: *id008
          note: Cache keys, returned IDs and structured export metadata are handled by fixed code.
        records: *id008
        note: Readable text/reasons and fixed IDs/metadata remain distinct consumption paths in the delivered
          copies.
      - scope: Included external Claude/Codex retained context, checkpoints and provider-owned state at
          the adapter boundary
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-model-dispatch
        note: No payload of retained external context or checkpoint is available for form classification;
          executing a parametric model does not establish parametric accumulated memory.
      records:
      - memory.md#mem-obj-raw-json
      - memory.md#mem-obj-entities
      - memory.md#mem-obj-image-tags
      - memory.md#mem-obj-semantic-tags
      - memory.md#mem-obj-category
      - memory.md#mem-obj-export-copy
      - memory.md#mem-obj-bookmark-category
      - memory.md#mem-obj-bookmark-fts
      - runtime.md#rt-rte-settings-change
      - memory.md#mem-obj-search-cache
      - runtime.md#rt-rte-model-dispatch
      note: Text interpretation and fixed-rule symbolic consumption are established on local parts. Opaque
        external context is not classified by its adapter or display summary.
    lineage:
      assessment: partial
      units:
      - scope: Imported bookmark text, rawJson and source fields
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id009
          - memory.md#mem-obj-raw-json
          - runtime.md#rt-rte-import-content
          note: File and X-facing ingress acquire external content rather than Siftly execution history.
        records: *id009
        note: This covers acquisition of external post content, not verification of its original author
          or truth.
      - scope: Backfilled entities and retained vision/semantic outputs
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id010
          - memory.md#mem-obj-entities
          - memory.md#mem-obj-image-tags
          - memory.md#mem-obj-semantic-tags
          note: Deterministic extraction and model annotation compile derived retained metadata; they
            do not extract agent-session traces.
        records: *id010
        note: Fixed extraction and model transformations derive metadata from imported content/media;
          URL-cache copying preserves an already derived output.
      - scope: Default category content and admitted sample-derived suggestions
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id011
          - memory.md#mem-obj-category
          - runtime.md#rt-rte-category-admission
          note: Shipped category descriptions originate as authored defaults before seeding.
        - value: other-compiled
          basis: wired
          records: *id011
          note: Suggested guidance is generated from sampled bookmarks and their metadata.
        records: *id011
        note: Defaults have an authored source; suggestion descriptions have a separately established
          model derivation from retained samples.
      - scope: Additional caller-authored category descriptions and initial deployed settings
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-category
        - runtime.md#rt-rte-category-admission
        - runtime.md#rt-rte-settings-change
        note: The accepted category inventory includes an incompletely assessed direct writer. Caller
          identity and initial deployed values do not establish human authorship or the original derivation
          path.
      - scope: Category memberships, processing markers, lexical index, response cache and export projections
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id012
          - memory.md#mem-obj-bookmark-category
          - memory.md#mem-obj-image-tags
          - memory.md#mem-obj-semantic-tags
          - memory.md#mem-obj-bookmark-fts
          - memory.md#mem-obj-search-cache
          - memory.md#mem-obj-export-copy
          note: Application/model processing produces the retained links, markers, index, cached response
            and formatted exports.
        records: *id012
        note: These are generated assignments, state results and derived copies; ordinary assignment is
          not trace extraction.
      - scope: Uninterpreted nested payload parts and alternate-ingress normalization
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-raw-json
        - runtime.md#rt-rte-import-content
        note: External acquisition is known, but complete nested payload provenance and uniform normalization
          are not established by the accepted records.
      - scope: Included external Claude/Codex retained context, checkpoints and provider-owned state at
          the adapter boundary
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-model-dispatch
        note: External retained context may have additional initial or trace-derived provenance; none
          is inspected.
      records:
      - memory.md#mem-obj-raw-json
      - runtime.md#rt-rte-import-content
      - memory.md#mem-obj-entities
      - memory.md#mem-obj-image-tags
      - memory.md#mem-obj-semantic-tags
      - memory.md#mem-obj-category
      - runtime.md#rt-rte-category-admission
      - runtime.md#rt-rte-settings-change
      - memory.md#mem-obj-bookmark-category
      - memory.md#mem-obj-bookmark-fts
      - memory.md#mem-obj-search-cache
      - memory.md#mem-obj-export-copy
      - runtime.md#rt-rte-model-dispatch
      note: Known local derivation paths coexist with unresolved initial category/configuration provenance,
        incompletely interpreted alternate ingress and opaque host retention.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retained source text, derived metadata and response explanations delivered to models or
          query callers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id013
          - memory.md#mem-obj-raw-json
          - memory.md#mem-obj-entities
          - memory.md#mem-obj-image-tags
          - memory.md#mem-obj-semantic-tags
          - memory.md#mem-obj-search-cache
          - runtime.md#rt-bap-enrichment-search
          note: Text, descriptions and tags supply evidence/context to enrichment, classification, reranking
            and readers.
        records: *id013
        note: Evidence-like context is a consumption role, not verified truth or general tool authority.
      - scope: Category descriptions delivered to subsequent categorization models
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id014
          - memory.md#mem-obj-category
          - runtime.md#rt-bap-category-guidance
          note: Persisted category meanings guide later category judgments.
        records: *id014
        note: Standing organizational guidance is distinct from the bookmark content it classifies.
      - scope: Retained text/metadata, FTS tokens and membership confidence at search and graph ordering
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id015
          - memory.md#mem-obj-bookmark-fts
          - memory.md#mem-obj-bookmark-category
          - runtime.md#rt-bap-enrichment-search
          - memory.md#mem-rte-browse-memory
          note: Lexical matches, retained metadata and membership confidence affect relative selection
            or order.
        records: *id015
        note: Fixed-code scoring and model relevance interpretation both consume retained inputs; ranking
          does not imply learned ranking policy.
      - scope: Category slugs at assignment parser and retained candidate IDs at result hydration
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id016
          - memory.md#mem-obj-category
          - runtime.md#rt-bap-category-guidance
          - runtime.md#rt-rte-search-content
          note: Known category identities and selected candidate identities determine admissible outputs.
        - value: enforcement
          basis: wired
          records: *id016
          note: Unknown slugs and noncandidate result IDs are excluded by executable checks.
        records: *id016
        note: These retained identities are consumed as allowed-domain criteria and enforced admission
          restrictions.
      - scope: enrichedAt, non-null/empty markers and retained configuration at future work selection
          and dispatch
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id017
          - memory.md#mem-obj-bookmark-category
          - memory.md#mem-obj-image-tags
          - memory.md#mem-obj-semantic-tags
          - runtime.md#rt-rte-enrich-categorize
          - runtime.md#rt-rte-settings-change
          note: Processing markers select future work, while retained settings select provider/model and
            export destination.
        records: *id017
        note: Markers can suppress retry without establishing annotation quality. Configuration chooses
          executor/location rather than teaching a model.
      - scope: Exported content at an external vault or agent consumer
        assessment: partial
        findings:
        - value: knowledge
          basis: afforded
          records: &id018
          - memory.md#mem-obj-export-copy
          - runtime.md#rt-rte-cli-export
          note: Formatted bookmark notes are afforded as externally readable reference material.
        records: *id018
        note: The delivered artifact affords reference use, but the external consumer and any stronger
          authority are not observed or fully inspected.
      - scope: Included external Claude/Codex retained context, checkpoints and provider-owned state at
          the adapter boundary
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-model-dispatch
        note: No retained host payload, update consumer or downstream force was inspected; learning authority
          cannot be inferred from model execution.
      records:
      - memory.md#mem-obj-raw-json
      - memory.md#mem-obj-entities
      - memory.md#mem-obj-image-tags
      - memory.md#mem-obj-semantic-tags
      - memory.md#mem-obj-search-cache
      - runtime.md#rt-bap-enrichment-search
      - memory.md#mem-obj-category
      - runtime.md#rt-bap-category-guidance
      - memory.md#mem-obj-bookmark-fts
      - memory.md#mem-obj-bookmark-category
      - memory.md#mem-rte-browse-memory
      - runtime.md#rt-rte-search-content
      - runtime.md#rt-rte-enrich-categorize
      - runtime.md#rt-rte-settings-change
      - memory.md#mem-obj-export-copy
      - runtime.md#rt-rte-cli-export
      - runtime.md#rt-rte-model-dispatch
      note: Local consumed parts establish context, standing classification guidance, retrieval priority,
        routing and admissibility constraints. External retained-state effects and downstream vault/agent
        behavior remain unresolved.
    write_agency:
      assessment: partial
      units:
      - scope: Pipeline extraction, vision/semantic/category writes, default seeding, FTS/cache writes
          and export formatting
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id019
          - memory.md#mem-obj-entities
          - memory.md#mem-obj-image-tags
          - memory.md#mem-obj-semantic-tags
          - memory.md#mem-obj-bookmark-category
          - memory.md#mem-obj-category
          - memory.md#mem-obj-bookmark-fts
          - memory.md#mem-obj-search-cache
          - memory.md#mem-obj-export-copy
          - runtime.md#rt-rte-enrich-categorize
          note: Software/model decisions admit derived content, markers, defaults and copies without a
            separate operator decision for each content item.
        records: *id019
        note: An operator starting processing/export is not per-content approval of generated additions
          or formatted copies.
      - scope: Browser file selection and category suggestion/manual-assignment UI
        assessment: known
        findings:
        - value: manual
          basis: afforded
          records: &id020
          - runtime.md#rt-rte-import-content
          - runtime.md#rt-rte-category-admission
          note: A user can supply an import file, approve selected suggestions or replace category assignments.
        records: *id020
        note: The UI affords an explicit human content-supply or selection decision; this is not evidence
          of exercised human review.
      - scope: Direct generic import/category/suggestion/assignment/settings callers and initial settings
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-import-content
        - runtime.md#rt-rte-category-admission
        - memory.md#mem-obj-category
        - memory.md#mem-obj-bookmark-category
        - runtime.md#rt-rte-settings-change
        note: An HTTP caller may be human or software. isAiGenerated=false and confidence=1.0 do not establish
          an explicit human decision; the additional direct category writer remains incompletely assessed.
      - scope: Included external Claude/Codex retained context, checkpoints and provider-owned state at
          the adapter boundary
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-model-dispatch
        note: No admission mechanism for external retained context/checkpoints was inspected.
      records:
      - memory.md#mem-obj-entities
      - memory.md#mem-obj-image-tags
      - memory.md#mem-obj-semantic-tags
      - memory.md#mem-obj-bookmark-category
      - memory.md#mem-obj-category
      - memory.md#mem-obj-bookmark-fts
      - memory.md#mem-obj-search-cache
      - memory.md#mem-obj-export-copy
      - runtime.md#rt-rte-enrich-categorize
      - runtime.md#rt-rte-import-content
      - runtime.md#rt-rte-category-admission
      - runtime.md#rt-rte-settings-change
      - runtime.md#rt-rte-model-dispatch
      note: Automatic admission is wired for transformations and copies. Explicit human content decisions
        are afforded in file supply and category selection/editing, but generic HTTP principals and initial
        deployment content remain unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Reduced projections of retained metadata into stored export copies
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id021
          - memory.md#mem-obj-export-copy
          - runtime.md#rt-rte-cli-export
          note: Software selects retained bookmark text and metadata into reduced notes and indexes, without
            establishing a novel claim.
        records: *id021
        note: The retained copy reduces/reformats existing claims; omission of full analysis and rawJson
          is explicit.
      - scope: Revisions of retained category guidance and assignments
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id022
          - memory.md#mem-obj-bookmark-category
          - memory.md#mem-obj-category
          - runtime.md#rt-rte-category-admission
          note: Existing memberships and category descriptions can be replaced or revised through the
            inspected writers.
        records: *id022
        note: Model upserts, manual delete/create replacement and default-description overwrites change
          existing retained organization. No history-preserving invalidation is implied.
      - scope: Short-lived hydrated response cache
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id023
          - memory.md#mem-obj-search-cache
          note: Five-minute expiry and first-key eviction remove retained cached responses.
        records: *id023
        note: TTL/size eviction forgets cached responses but does not withdraw source rows or exports.
      - scope: Vision/semantic annotation and suggested guidance transformations beyond established revisions
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-image-tags
        - memory.md#mem-obj-semantic-tags
        - memory.md#mem-obj-category
        - epistemic.md#epi-rte-semantic-tags
        - epistemic.md#epi-rte-image-analysis
        note: Actual generated semantic edges are not available to distinguish compression, entailed extraction
          and new non-entailed claims. Category generation as a route name does not establish synthesis.
      - scope: Additional direct category authoring/maintenance mechanism
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-category
        - runtime.md#rt-rte-category-admission
        note: Its retained target is known, but the accepted inventory leaves this writer incompletely
          assessed; no full operation enumeration is warranted.
      - scope: Included external Claude/Codex retained context, checkpoints and provider-owned state at
          the adapter boundary
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-model-dispatch
        note: No external checkpoint maintenance, consolidation or forgetting operation was inspected.
      records:
      - memory.md#mem-obj-export-copy
      - runtime.md#rt-rte-cli-export
      - memory.md#mem-obj-bookmark-category
      - memory.md#mem-obj-category
      - runtime.md#rt-rte-category-admission
      - memory.md#mem-obj-search-cache
      - memory.md#mem-obj-image-tags
      - memory.md#mem-obj-semantic-tags
      - epistemic.md#epi-rte-semantic-tags
      - epistemic.md#epi-rte-image-analysis
      - runtime.md#rt-rte-model-dispatch
      note: Supported operations are restricted to implemented changes over already retained material.
        Acquisition, duplicate-ID skipping, index rebuilding and requested topic invention alone add no
        curation value. Semantic model transformations and additional writers remain incompletely characterized.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested search/cache hit, browse/graph, CLI detail/list and export return
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id024
          - runtime.md#rt-rte-search-content
          - memory.md#mem-obj-search-cache
          - memory.md#mem-rte-browse-memory
          - runtime.md#rt-rte-cli-export
          note: A consumer query/filter/ID or export request causes retained material to be returned.
        records: *id024
        note: Automatic scoring inside a requested retrieval does not make the requested return another
          push.
      - scope: Application-selected retained tags/entities/category guidance delivered into enrichment
          and categorization calls
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id025
          - runtime.md#rt-rte-enrich-categorize
          - memory.md#mem-obj-entities
          - memory.md#mem-obj-image-tags
          - memory.md#mem-obj-semantic-tags
          - memory.md#mem-obj-category
          - runtime.md#rt-bap-category-guidance
          note: The application automatically supplies selected metadata and available category guidance
            to later model invocations.
        records: *id025
        note: The pipeline trigger starts work; application code then selects retained context for models
          without those models requesting its retrieval. This is not an unsolicited external-agent injection.
      - scope: External reading of exported response files or vault artifacts
        assessment: partial
        findings:
        - value: pull
          basis: afforded
          records: &id026
          - memory.md#mem-obj-export-copy
          - runtime.md#rt-rte-cli-export
          note: Saved Markdown and structured copies afford later on-demand reading.
        records: *id026
        note: Export affords later reader access, but no deployed vault or agent read trace establishes
          the full external delivery chain.
      - scope: Included external Claude/Codex retained context, checkpoints and provider-owned state at
          the adapter boundary
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-model-dispatch
        note: Host context/checkpoint delivery is not inspected; local requested routes cannot resolve
          it.
      records:
      - runtime.md#rt-rte-search-content
      - memory.md#mem-obj-search-cache
      - memory.md#mem-rte-browse-memory
      - runtime.md#rt-rte-cli-export
      - runtime.md#rt-rte-enrich-categorize
      - memory.md#mem-obj-entities
      - memory.md#mem-obj-image-tags
      - memory.md#mem-obj-semantic-tags
      - memory.md#mem-obj-category
      - runtime.md#rt-bap-category-guidance
      - memory.md#mem-obj-export-copy
      - runtime.md#rt-rte-model-dispatch
      note: Request-directed query delivery and automatic context supply inside processing are separate
        operations. Opaque host retention prevents declaring a complete local-plus-host direction inventory.
    read_back_signal:
      assessment: partial
      units:
      - scope: Pipeline automatic loading of retained per-bookmark media/tags/entities into worker and
          category batches
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id027
          - runtime.md#rt-rte-enrich-categorize
          - memory.md#mem-obj-entities
          - memory.md#mem-obj-image-tags
          - memory.md#mem-obj-semantic-tags
          note: Bookmark identity and relational matches select which retained metadata is supplied to
            each later model call.
        records: *id027
        note: 'Trigger: pipeline worker or queued category flush. Selector inputs: chosen database bookmark
          IDs and linked media rows. Selected parts: retained text/entities/imageTags/semanticTags for
          those matching rows. Field truncation limits delivery after the identity selection.'
      - scope: Pipeline available-category context and incremental eligibility
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id028
          - runtime.md#rt-rte-enrich-categorize
          - memory.md#mem-obj-category
          - memory.md#mem-obj-bookmark-category
          - memory.md#mem-obj-image-tags
          - runtime.md#rt-bap-category-guidance
          note: Available-set and processing-state predicates gate context availability rather than infer
            a semantic match.
        records: *id028
        note: 'Trigger: pipeline start/work selection. Inputs: available categories, explicit/force versus
          missing enrichedAt, null/non-null tag markers. Parts: category descriptions/slugs supplied as
          the available set and eligible bookmark content. These broad predicates are distinct from matching
          chosen bookmark identities.'
      - scope: Requested AI search/cache, browser, CLI and export returns
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-search-content
        - memory.md#mem-obj-search-cache
        - memory.md#mem-rte-browse-memory
        - runtime.md#rt-rte-cli-export
        note: These inspected delivery operations fulfill consumer requests. Lexical and model relevance
          selectors inside that pull chain are not classified as push signals.
      - scope: Included external Claude/Codex retained context, checkpoints and provider-owned state at
          the adapter boundary
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-model-dispatch
        note: No trigger, selector input or delivered retained host part is known; cannot assign lexical,
          embedding or judgment push signals from external execution alone.
      records:
      - runtime.md#rt-rte-enrich-categorize
      - memory.md#mem-obj-entities
      - memory.md#mem-obj-image-tags
      - memory.md#mem-obj-semantic-tags
      - memory.md#mem-obj-category
      - memory.md#mem-obj-bookmark-category
      - runtime.md#rt-bap-category-guidance
      - runtime.md#rt-rte-search-content
      - memory.md#mem-obj-search-cache
      - memory.md#mem-rte-browse-memory
      - runtime.md#rt-rte-cli-export
      - runtime.md#rt-rte-model-dispatch
      note: Classify only the pipeline push selector, not a requested query return. Known pull-only local
        consumers are inapplicable units; opaque host alternatives remain included.
    trace_learning:
      assessment: not-determinable
      units:
      - scope: Local imported-content transformations, category guidance, markers, caches and export routes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-raw-json
        - memory.md#mem-obj-image-tags
        - memory.md#mem-obj-semantic-tags
        - memory.md#mem-obj-bookmark-category
        - memory.md#mem-obj-category
        - memory.md#mem-obj-search-cache
        - runtime.md#rt-rte-enrich-categorize
        - epistemic.md#epi-rte-semantic-tags
        note: The records distinguish imported source content from Siftly execution traces and report
          only a bounded feedback search, explicitly not an absence record. Marker/assignment persistence
          and topic generation do not by themselves establish qualifying experience learning. No yes or
          no is warranted.
      - scope: Included external Claude/Codex retained context, checkpoints and provider-owned state at
          the adapter boundary
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-model-dispatch
        note: External conversations, checkpoints and parameter-update internals are uninspected; no automatic
          trace-fed write/later-consumer chain can be classified.
      records:
      - memory.md#mem-obj-raw-json
      - memory.md#mem-obj-image-tags
      - memory.md#mem-obj-semantic-tags
      - memory.md#mem-obj-bookmark-category
      - memory.md#mem-obj-category
      - memory.md#mem-obj-search-cache
      - runtime.md#rt-rte-enrich-categorize
      - epistemic.md#epi-rte-semantic-tags
      - runtime.md#rt-rte-model-dispatch
      note: No accepted bounded evidenced-absence record licenses a local or system-wide no. Operational
        markers have explicit future selectors but do not establish a qualifying trace-fed durable behavior-shaping
        artifact; imported posts and generated annotations do not alone establish trace learning. Opaque
        hosts remain unresolved.
    trace_source:
      assessment: not-determinable
      units:
      - scope: Original inputs to potentially qualifying local behavior-shaping writes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-raw-json
        - memory.md#mem-obj-image-tags
        - memory.md#mem-obj-semantic-tags
        - memory.md#mem-obj-bookmark-category
        - memory.md#mem-obj-category
        - runtime.md#rt-rte-enrich-categorize
        note: Imported tweets/media and operational markers are described, but no accepted record establishes
          their role as original trace inputs to a qualifying automatic learning write. Mere timestamps
          or generated metadata do not establish a controlled trace source.
      - scope: Included external Claude/Codex retained context, checkpoints and provider-owned state at
          the adapter boundary
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-model-dispatch
        note: The original inputs to any external context/checkpoint or parametric update are unknown;
          no adapter name establishes trace origin.
      records:
      - memory.md#mem-obj-raw-json
      - memory.md#mem-obj-image-tags
      - memory.md#mem-obj-semantic-tags
      - memory.md#mem-obj-bookmark-category
      - memory.md#mem-obj-category
      - runtime.md#rt-rte-enrich-categorize
      - runtime.md#rt-rte-model-dispatch
      note: No qualifying local trace-learning write is established, and the learning inventory is not
        a bounded completely assessed absence. Therefore source is unresolved, not inapplicable; imported
        X JSON is not relabeled as session logs or event streams.
---

# Siftly memory profile

## Comparison rationale

### Boundary and canonical identities

This is a revision-2 classification of accepted records, not a new inspection of Siftly. The substrate is the retained bookmark system, not all runtime storage. Process queues and shipped prompts are not independently accumulated memory. Updated settings are included only where later resolvers consume them; external context/checkpoint retention remains an unresolved alternative at the adapter boundary. The actual executors' parametric form does not establish use-accumulated parametric memory. See [RT-RTE-model-dispatch](runtime.md#rt-rte-model-dispatch), [RT-RTE-settings-change](runtime.md#rt-rte-settings-change) and [MEM-OBJ-raw-json](memory.md#mem-obj-raw-json).

Reconciliation supersedes the epistemic entity, image-tag, semantic-tag and category-description object identities with [MEM-OBJ-entities](memory.md#mem-obj-entities), [MEM-OBJ-image-tags](memory.md#mem-obj-image-tags), [MEM-OBJ-semantic-tags](memory.md#mem-obj-semantic-tags) and [MEM-OBJ-category](memory.md#mem-obj-category). Values above cite those canonical objects. The additional direct category writer and empty-store seeding remain qualifications of that same category object, not a new memory surface. Its incomplete admission assessment prevents complete write-agency, lineage and curation coverage. Membership-only and membership-plus-enrichedAt records are not whole-record aliases. Neither are query matches and the complete response cache. The wider memory records retain their distinct scopes.

### Consumption, selection and authority

SQLite FTS5 is a lexical access structure, not vector memory, and the mindmap is a display projection, not a graph substrate. Language tokens can have natural-language force at a model and symbolic force at a fixed selector. Classification therefore separates these consumption paths rather than treating JSON as a semantic form. See [MEM-OBJ-bookmark-fts](memory.md#mem-obj-bookmark-fts) and [MEM-RTE-browse-memory](memory.md#mem-rte-browse-memory).

Category descriptions supply standing classification instructions. Tags and source text supply context and ranking inputs. Allowed slugs supply both admissibility criteria and enforced exclusion. Processing markers route later work; they are not evidence of correctness. No blanket learning authority follows from these effects. In particular, success at categorization can set enrichedAt even after semantic enrichment failed. The accepted retry qualification changes routing coverage, not the existence of retained metadata. See [RT-BAP-category-guidance](runtime.md#rt-bap-category-guidance), [RT-BAP-enrichment-search](runtime.md#rt-bap-enrichment-search), [MEM-OBJ-bookmark-category](memory.md#mem-obj-bookmark-category) and [EPI-RTE-semantic-tags](epistemic.md#epi-rte-semantic-tags).

A requested search is pull even when automatic lexical/model selection fulfills it. A different operation automatically supplies retained metadata and category guidance into pipeline model calls. That operation is push, with bookmark identity and broad availability/state predicates kept separate. Neither classification asserts an unsolicited injection into an external agent. Category/all-record availability is coarse selection; a requested CLI ID is not a push identifier signal. See [RT-RTE-search-content](runtime.md#rt-rte-search-content), [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize) and [RT-RTE-cli-export](runtime.md#rt-rte-cli-export).

### Transformation and uncertainty

Reduced persisted exports support consolidation; assignment/default overwrites support evolution; cache TTL/eviction supports decay. Duplicate import IDs, URL reuse and full index rebuilding alone do not establish semantic deduplication. Deletion without retained history is not the controlled invalidate operation. Actual vision/enrichment outputs are absent, so semantic novelty or faithfulness cannot be inferred from a generation route name. No synthesis finding is added from that uncertainty. See [MEM-OBJ-export-copy](memory.md#mem-obj-export-copy), [MEM-OBJ-search-cache](memory.md#mem-obj-search-cache), [MEM-OBJ-category](memory.md#mem-obj-category), [EPI-RTE-image-analysis](epistemic.md#epi-rte-image-analysis) and [EPI-RTE-semantic-tags](epistemic.md#epi-rte-semantic-tags).

There is no accepted evidenced-absence declaration for trace learning. The reports' feedback-search limits do not license a local no, much less a system-wide no. Imported post content is not automatically a session/tool trace, and attempted-analysis markers are not established durable experience-derived guidance. Without a qualifying local write chain or complete negative coverage, trace source cannot become inapplicable. Opaque external retention remains uninspected for both axes. This withholds a classification rather than asserting absence or requiring demonstrated improvement for a wired yes. See [MEM-OBJ-raw-json](memory.md#mem-obj-raw-json), [MEM-OBJ-image-tags](memory.md#mem-obj-image-tags), [MEM-OBJ-bookmark-category](memory.md#mem-obj-bookmark-category) and [RT-RTE-model-dispatch](runtime.md#rt-rte-model-dispatch).

Axis assessments preserve local findings without claiming complete system unions. Automatic/manual differ by admission mechanism and evidence layer; the human UI affordance does not upgrade generic API callers. External file reading is afforded, not observed. No finding is observed or causally supported: the supplied records establish source wiring and explicit affordances, not successful use, truthful annotations or improved performance.

### Source-read log

No target-source reads were made. Only the supplied invocation, job, types, contracts and pinned members were read. No additional evidence or records were introduced.
