---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: Quicky Wiki memory comparison across retained graph parts, source/configuration files, answer
  reuse, views and opaque provider alternatives.
run-id: AAS-2026-10-15-quicky-wiki-628f7d7cc628-01
source-identity: https://github.com/anzal1/quicky-wiki
reviewed-boundary: cfeecbffce5b6d0f16533b258a1e88edd86f731e
memory-comparison:
  version: 2
  scope: Use-derived or edited retained source documents, SQLite claims/control/provenance/relations/events/FTS,
    page summaries, project configuration, optional saved answers and rendered/exported views; their admission,
    maintenance and later consumers, plus unresolved provider-retained use-derived state and embedding
    initialization. Excludes static shipped prompts/defaults, static model weights, transient extraction/diff/consensus/review
    arrays except as transformation inputs or outputs, package release artifacts and external host planning.
    Remaining export payload details and opaque alternatives stay included as unresolved.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Claims, controls, summaries, source register, events, relations and FTS indexes
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - runtime.md#rt-obj-knowledge-store
          note: KnowledgeStore persists rows, relations and indexes in graph.sqlite.
        records:
        - runtime.md#rt-obj-knowledge-store
        - memory.md#mem-obj-claims
        - memory.md#mem-obj-claim-controls
        - memory.md#mem-obj-page-summaries
        - memory.md#mem-obj-source-register
        - memory.md#mem-obj-epistemic-events
        - memory.md#mem-obj-graph-relations
        note: All six retained graph parts and their access structures are accounted for.
      - scope: Source files, saved answer sources, rendered views and edited project configuration
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - epistemic.md#epi-obj-source-content
          - runtime.md#rt-rte-answer-save
          - memory.md#mem-obj-rendered-views
          - runtime.md#rt-rte-runtime-setup
          note: Compiler, loaders and dashboard read retained filesystem bytes.
        records:
        - epistemic.md#epi-obj-source-content
        - runtime.md#rt-rte-answer-save
        - memory.md#mem-obj-rendered-views
        - runtime.md#rt-rte-runtime-setup
        note: These operative retained objects are filesystem files; deployment contents are not supplied.
      - scope: Opaque provider-retained state, if any, accumulated through use
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-llm-adapter
        note: The substrate of any provider-retained use-derived state cannot be classified. Provider
          internals were not inspected; inference calls do not resolve provider retention or updates.
          Static model weights are not themselves classified as accumulated memory.
      records:
      - runtime.md#rt-obj-knowledge-store
      - memory.md#mem-obj-claims
      - memory.md#mem-obj-claim-controls
      - memory.md#mem-obj-page-summaries
      - memory.md#mem-obj-source-register
      - memory.md#mem-obj-epistemic-events
      - memory.md#mem-obj-graph-relations
      - epistemic.md#epi-obj-source-content
      - runtime.md#rt-rte-answer-save
      - memory.md#mem-obj-rendered-views
      - runtime.md#rt-rte-runtime-setup
      - runtime.md#rt-cmp-llm-adapter
      note: The recorded inventory covers SQLite parts, retained files and configuration, but provider-retained
        alternatives remain opaque. Graph relations and FTS are SQLite structures, not additional physical
        substrates.
    representational_form:
      assessment: partial
      units:
      - scope: Claim statements and page summaries at model, search and human readers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-claims
          - memory.md#mem-obj-page-summaries
          note: Models and people interpret retained assertions and summaries.
        records:
        - memory.md#mem-obj-claims
        - memory.md#mem-obj-page-summaries
        note: Natural-language claims and descriptions are separate from row identifiers and scores.
      - scope: Claim controls, source metadata, graph edges and FTS access structures at fixed-rule consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-claim-controls
          - memory.md#mem-obj-source-register
          - memory.md#mem-obj-graph-relations
          - runtime.md#rt-obj-knowledge-store
          note: Code uses these retained parts for matching, filtering, score rules and graph traversal;
            numerical scores are not distributed parameters.
        records:
        - memory.md#mem-obj-claim-controls
        - memory.md#mem-obj-source-register
        - memory.md#mem-obj-graph-relations
        - runtime.md#rt-obj-knowledge-store
        note: Scalar numbers, IDs, paths, hashes, JSON filters and relations have localized fixed-rule
          use.
      - scope: Epistemic event notes at inspection readers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-epistemic-events
          note: Human inspection can read mutation notes.
        records:
        - memory.md#mem-obj-epistemic-events
        note: Notes are textual reasons or generic descriptions; ordinary answer models do not receive
          them.
      - scope: Epistemic event identifiers, type, date and score transitions
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-epistemic-events
          note: Fixed fields encode event identity and confidence transitions.
        records:
        - memory.md#mem-obj-epistemic-events
        note: Timeline and dashboard consume structured mutation fields.
      - scope: Inspected source, saved-answer and rendered-file text parts; entity-specific configuration
          guidance
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - epistemic.md#epi-obj-source-content
          - runtime.md#rt-rte-answer-save
          - memory.md#mem-obj-rendered-views
          - runtime.md#rt-rte-runtime-setup
          note: Source bodies, answer prose, view statements and entity instructions receive semantic
            interpretation.
        records:
        - epistemic.md#epi-obj-source-content
        - runtime.md#rt-rte-answer-save
        - memory.md#mem-obj-rendered-views
        - runtime.md#rt-rte-runtime-setup
        note: These are text paths, not restored hidden model state.
      - scope: Inspected file frontmatter, links, scores and configuration routing fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - epistemic.md#epi-obj-source-content
          - runtime.md#rt-rte-answer-save
          - memory.md#mem-obj-rendered-views
          - runtime.md#rt-rte-runtime-setup
          note: Parsers/loaders use field identities and fixed configuration rules.
        records:
        - epistemic.md#epi-obj-source-content
        - runtime.md#rt-rte-answer-save
        - memory.md#mem-obj-rendered-views
        - runtime.md#rt-rte-runtime-setup
        note: Mixed files retain symbolic parts separately from prose.
      - scope: Remaining alternative export templates
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-rendered-views
        note: Selectors and write paths are recorded, but detailed templates were not fully inspected;
          complete payload-form classification is prevented.
      - scope: Opaque provider-retained state, if any, accumulated through use
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-llm-adapter
        note: No form is assigned from a readable endpoint description. Provider internals were not inspected;
          inference calls do not resolve provider retention or updates. Static model weights are not themselves
          classified as accumulated memory.
      records:
      - memory.md#mem-obj-claims
      - memory.md#mem-obj-page-summaries
      - memory.md#mem-obj-claim-controls
      - memory.md#mem-obj-source-register
      - memory.md#mem-obj-graph-relations
      - runtime.md#rt-obj-knowledge-store
      - memory.md#mem-obj-epistemic-events
      - epistemic.md#epi-obj-source-content
      - runtime.md#rt-rte-answer-save
      - memory.md#mem-obj-rendered-views
      - runtime.md#rt-rte-runtime-setup
      - runtime.md#rt-cmp-llm-adapter
      note: Inspected retained objects have distinct text and fixed-rule symbolic parts; opaque provider
        payloads and remaining export templates prevent complete form coverage.
    lineage:
      assessment: partial
      units:
      - scope: Externally supplied source bodies and direct statement/metadata replacements
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - epistemic.md#epi-obj-source-content
          - memory.md#mem-obj-claims
          - memory.md#mem-obj-source-register
          - runtime.md#rt-rte-client-access
          note: File reads and caller replacements acquire content from outside the compiler.
        records:
        - epistemic.md#epi-obj-source-content
        - memory.md#mem-obj-claims
        - memory.md#mem-obj-source-register
        - runtime.md#rt-rte-client-access
        note: Import describes entry into this system, not authenticated original authorship.
      - scope: Explicit operator-authored configuration overrides
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - runtime.md#rt-rte-runtime-setup
          note: Explicit setup options and operator edits supply retained configuration choices.
        records:
        - runtime.md#rt-rte-runtime-setup
        note: The recorded human options constitute authored retained input; arbitrary external config
          writers are separate.
      - scope: Document-derived claims, summaries, computed controls, metadata, page links and rendered
          views
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - runtime.md#rt-rte-source-ingest
          - memory.md#mem-obj-page-summaries
          - memory.md#mem-obj-claim-controls
          - memory.md#mem-obj-source-register
          - memory.md#mem-obj-graph-relations
          - memory.md#mem-obj-rendered-views
          note: Model/code transformations derive retained objects from supplied documents and graph state.
        records:
        - runtime.md#rt-rte-source-ingest
        - memory.md#mem-obj-page-summaries
        - memory.md#mem-obj-claim-controls
        - memory.md#mem-obj-source-register
        - memory.md#mem-obj-graph-relations
        - memory.md#mem-obj-rendered-views
        note: Compilation provenance is established independently of semantic fidelity.
      - scope: Automatically recorded mutation events and answer-derived sources/re-extracted claims
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-epistemic-events
          - runtime.md#rt-rte-answer-save
          - runtime.md#rt-rte-source-ingest
          note: Events derive from graph mutations; saved question/answer content can be re-extracted
            into later graph content.
        records:
        - memory.md#mem-obj-epistemic-events
        - runtime.md#rt-rte-answer-save
        - runtime.md#rt-rte-source-ingest
        note: Reduced mutation history and answer-derived material have distinct activity origins; this
          lineage alone does not establish automatic trace learning.
      - scope: Initial embedding-created database content, externally inserted claim edges/events and
          generic external config writers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-claims
        - memory.md#mem-obj-graph-relations
        - memory.md#mem-obj-epistemic-events
        - runtime.md#rt-rte-runtime-setup
        note: Caller APIs do not establish original derivation or authorship for arbitrary initialized
          content.
      - scope: Opaque provider-retained state, if any, accumulated through use
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-llm-adapter
        note: The original and update provenance of any provider-retained state is unknown. Provider internals
          were not inspected; inference calls do not resolve provider retention or updates. Static model
          weights are not themselves classified as accumulated memory.
      records:
      - epistemic.md#epi-obj-source-content
      - memory.md#mem-obj-claims
      - memory.md#mem-obj-source-register
      - runtime.md#rt-rte-client-access
      - runtime.md#rt-rte-runtime-setup
      - runtime.md#rt-rte-source-ingest
      - memory.md#mem-obj-page-summaries
      - memory.md#mem-obj-claim-controls
      - memory.md#mem-obj-graph-relations
      - memory.md#mem-obj-rendered-views
      - memory.md#mem-obj-epistemic-events
      - runtime.md#rt-rte-answer-save
      - runtime.md#rt-cmp-llm-adapter
      note: Known derivation routes coexist with unauthenticated original authorship, embedding initialization
        and opaque provider provenance.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Statements, scores, summaries and saved/raw documents at informational model/human consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-claims
          - memory.md#mem-obj-claim-controls
          - memory.md#mem-obj-page-summaries
          - epistemic.md#epi-obj-source-content
          - runtime.md#rt-rte-answer-save
          - runtime.md#rt-bap-retained-context
          note: Comparison, answering, summaries, reviews and page readers receive reference/context content.
        records:
        - memory.md#mem-obj-claims
        - memory.md#mem-obj-claim-controls
        - memory.md#mem-obj-page-summaries
        - epistemic.md#epi-obj-source-content
        - runtime.md#rt-rte-answer-save
        - runtime.md#rt-bap-retained-context
        note: Delivered evidence and context are not verified truth or enforced obedience.
      - scope: Statements and summaries in lexical retrieval; confidence/age in ordered review selection
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-claims
          - memory.md#mem-obj-page-summaries
          - memory.md#mem-obj-claim-controls
          - runtime.md#rt-rte-question-answer
          - runtime.md#rt-rte-health-review
          note: Text determines lexical retrieval priority; confidence and staleness determine ordered
            review candidates.
        records:
        - memory.md#mem-obj-claims
        - memory.md#mem-obj-page-summaries
        - memory.md#mem-obj-claim-controls
        - runtime.md#rt-rte-question-answer
        - runtime.md#rt-rte-health-review
        note: Fixed scoring and ordering give retained content ranking force without learned ranking policy.
      - scope: Source hashes, kind/metadata, IDs and graph edges at compiler/selector consumers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-source-register
          - memory.md#mem-obj-graph-relations
          - memory.md#mem-obj-claim-controls
          - runtime.md#rt-rte-source-ingest
          - runtime.md#rt-rte-client-access
          note: Retained metadata selects operations, input scopes and graph destinations.
        records:
        - memory.md#mem-obj-source-register
        - memory.md#mem-obj-graph-relations
        - memory.md#mem-obj-claim-controls
        - runtime.md#rt-rte-source-ingest
        - runtime.md#rt-rte-client-access
        note: Routing includes skip/extract, entity scope, page grouping and conditional cascade destinations.
      - scope: Retained confidence at default slide/export eligibility checks
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-claim-controls
          - epistemic.md#epi-rte-slide-output
          note: Retained score is a numeric admissibility criterion for default slide inclusion, not a
            factual test.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-claim-controls
          - epistemic.md#epi-rte-slide-output
          note: Code excludes below-threshold claims on the default selector, but not the topic override.
        records:
        - memory.md#mem-obj-claim-controls
        - epistemic.md#epi-rte-slide-output
        note: 'Default slide eligibility is bounded: explicit topic selection bypasses the confidence
          floor.'
      - scope: Edited configuration entity prompts and symbolic runtime choices
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - runtime.md#rt-rte-runtime-setup
          - runtime.md#rt-bap-retained-context
          note: Entity-specific retained text is appended to extraction system instructions.
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-rte-runtime-setup
          note: Provider/model, path and kind choices select subsequent runtime behavior.
        records:
        - runtime.md#rt-rte-runtime-setup
        - runtime.md#rt-bap-retained-context
        note: Standing entity guidance is distinct from graph evidence.
      - scope: Saved question/answer material at subsequent automatic extraction
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - runtime.md#rt-rte-answer-save
          - runtime.md#rt-rte-source-ingest
          note: Recorded answer experience feeds automatic production of durable graph context for later
            questions; benefit is unobserved.
        records:
        - runtime.md#rt-rte-answer-save
        - runtime.md#rt-rte-source-ingest
        note: Update-consumer force is distinct from the resulting claims knowledge force.
      - scope: Event history and rendered Markdown at shipped display consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-epistemic-events
          - memory.md#mem-obj-rendered-views
          note: Timeline/dashboard readers receive informational history and view content.
        records:
        - memory.md#mem-obj-epistemic-events
        - memory.md#mem-obj-rendered-views
        note: Stored reasons are inspectable, not ordinary answer inputs; dashboard reads files for display.
      - scope: Exported content at external presentation/application readers
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-obj-rendered-views
          - epistemic.md#epi-rte-slide-output
          note: Export files afford later human/application reference; actual adoption is unobserved.
        records:
        - memory.md#mem-obj-rendered-views
        - epistemic.md#epi-rte-slide-output
        note: Only the documented/export-afforded informational consumer role is established.
      - scope: Opaque provider-retained state, if any, accumulated through use
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-llm-adapter
        note: No actual consumer/effect path for opaque provider-retained material can be classified.
          Provider internals were not inspected; inference calls do not resolve provider retention or
          updates. Static model weights are not themselves classified as accumulated memory.
      records:
      - memory.md#mem-obj-claims
      - memory.md#mem-obj-claim-controls
      - memory.md#mem-obj-page-summaries
      - epistemic.md#epi-obj-source-content
      - runtime.md#rt-rte-answer-save
      - runtime.md#rt-bap-retained-context
      - runtime.md#rt-rte-question-answer
      - runtime.md#rt-rte-health-review
      - memory.md#mem-obj-source-register
      - memory.md#mem-obj-graph-relations
      - runtime.md#rt-rte-source-ingest
      - runtime.md#rt-rte-client-access
      - epistemic.md#epi-rte-slide-output
      - runtime.md#rt-rte-runtime-setup
      - memory.md#mem-obj-epistemic-events
      - memory.md#mem-obj-rendered-views
      - runtime.md#rt-cmp-llm-adapter
      note: Authority follows actual retained parts and consumers, not the fact that host code enforces
        a write. Provider paths and external adoption remain unresolved.
    write_agency:
      assessment: partial
      units:
      - scope: Compiler claim/summary/control/page-link admission, event recording, decay and generated-view
          writes
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-source-ingest
          - memory.md#mem-obj-epistemic-events
          - memory.md#mem-obj-claim-controls
          - memory.md#mem-obj-rendered-views
          - runtime.md#rt-rte-health-review
          note: Software and models decide and admit each derived item or numeric update.
        records:
        - runtime.md#rt-rte-source-ingest
        - memory.md#mem-obj-epistemic-events
        - memory.md#mem-obj-claim-controls
        - memory.md#mem-obj-rendered-views
        - runtime.md#rt-rte-health-review
        note: No per-content human decision intervenes on these recorded transformations.
      - scope: Explicit human setup overrides and opt-in answer-file save
        assessment: known
        findings:
        - value: manual
          basis: wired
          records:
          - runtime.md#rt-rte-runtime-setup
          - runtime.md#rt-rte-answer-save
          note: Operator choices supply configuration content or explicitly authorize retaining the returned
            answer.
        records:
        - runtime.md#rt-rte-runtime-setup
        - runtime.md#rt-rte-answer-save
        note: Save is a human decision to retain that answer, not per-claim factual approval or approval
          of subsequent extraction.
      - scope: Dashboard/MCP/library content edits, external files and embedding initialization
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-client-access
        - memory.md#mem-obj-claims
        - memory.md#mem-obj-source-register
        - memory.md#mem-obj-graph-relations
        note: Handlers accept caller content, but generic HTTP/API access does not identify an explicit
          human content decision or an autonomous producer; no blanket manual or automatic classification
          is warranted.
      - scope: Opaque provider-retained state, if any, accumulated through use
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-llm-adapter
        note: Provider admission/update control is uninspected. Provider internals were not inspected;
          inference calls do not resolve provider retention or updates. Static model weights are not themselves
          classified as accumulated memory.
      records:
      - runtime.md#rt-rte-source-ingest
      - memory.md#mem-obj-epistemic-events
      - memory.md#mem-obj-claim-controls
      - memory.md#mem-obj-rendered-views
      - runtime.md#rt-rte-health-review
      - runtime.md#rt-rte-runtime-setup
      - runtime.md#rt-rte-answer-save
      - runtime.md#rt-rte-client-access
      - memory.md#mem-obj-claims
      - memory.md#mem-obj-source-register
      - memory.md#mem-obj-graph-relations
      - runtime.md#rt-cmp-llm-adapter
      note: Compiler admission is automatic despite user initiation; explicit operator choices are manual.
        Generic caller identities and provider updates remain unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Existing claim confidence revisions and direct statement replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-claims
          - memory.md#mem-obj-claim-controls
          - runtime.md#rt-rte-source-ingest
          note: Reinforcement/challenge and direct edits revise existing entries and scores.
        records:
        - memory.md#mem-obj-claims
        - memory.md#mem-obj-claim-controls
        - runtime.md#rt-rte-source-ingest
        note: Revision of a current retained entry is evolve; a challenge is not a history-preserving
          withdrawal.
      - scope: Elapsed-time downweighting of retained claim confidence
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-obj-claim-controls
          - runtime.md#rt-rte-health-review
          note: Fixed exponential/clamped updates lower durable confidence over time.
        records:
        - memory.md#mem-obj-claim-controls
        - runtime.md#rt-rte-health-review
        note: Time decay is separate from knowledge acceptance and from deletion.
      - scope: Model reduction of retained page claims into summary text
        assessment: partial
        findings:
        - value: consolidate
          basis: claimed
          records:
          - memory.md#mem-obj-page-summaries
          note: The prompt asks for a single short sentence representing the retained page claims; minimum
            length is the admission check.
        records:
        - memory.md#mem-obj-page-summaries
        note: Reduction is explicitly requested and the persistence path is wired; concrete output semantics
          are not verified, preventing stronger implementation-level semantic guarantees.
      - scope: Semantic equivalence handling during comparison
        assessment: partial
        findings:
        - value: dedup
          basis: claimed
          records:
          - runtime.md#rt-rte-source-ingest
          - memory.md#mem-obj-claims
          note: The comparison request classifies matching new evidence as reinforcement rather than another
            new claim.
        records:
        - runtime.md#rt-rte-source-ingest
        - memory.md#mem-obj-claims
        note: Comparison can avoid an additional retained duplicate by reinforcing an existing claim.
          Semantic matching is model judgment; completeness and equivalence accuracy are not established.
      - scope: Other model-generated summary/slide claims and remaining export transformations
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-page-summaries
        - memory.md#mem-obj-rendered-views
        - epistemic.md#epi-rte-slide-output
        note: No source/output pairs establish novel claims versus faithful reshaping; synthesize cannot
          be inferred from model generation alone. Remaining templates are incompletely inspected.
      - scope: Opaque provider-retained state, if any, accumulated through use
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-llm-adapter
        note: Provider-side curation of retained state, if any, is uninspected. Provider internals were
          not inspected; inference calls do not resolve provider retention or updates. Static model weights
          are not themselves classified as accumulated memory.
      records:
      - memory.md#mem-obj-claims
      - memory.md#mem-obj-claim-controls
      - runtime.md#rt-rte-source-ingest
      - runtime.md#rt-rte-health-review
      - memory.md#mem-obj-page-summaries
      - memory.md#mem-obj-rendered-views
      - epistemic.md#epi-rte-slide-output
      - runtime.md#rt-cmp-llm-adapter
      note: Retained score/statement revisions and decay are implemented. Summary compression is requested,
        not verified; candidate-prefix filtering and FTS rebuilds are not curation of retained claims.
    read_back_direction:
      assessment: partial
      units:
      - scope: Question/consensus, explicit page/search/entity/history/file-display requests and maintenance
          requests
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-question-answer
          - runtime.md#rt-rte-consensus-answer
          - runtime.md#rt-rte-client-access
          - runtime.md#rt-rte-health-review
          - memory.md#mem-obj-rendered-views
          - memory.md#mem-obj-epistemic-events
          note: Shipped callers fulfill consumer requests against retained graph or file content.
        records:
        - runtime.md#rt-rte-question-answer
        - runtime.md#rt-rte-consensus-answer
        - runtime.md#rt-rte-client-access
        - runtime.md#rt-rte-health-review
        - memory.md#mem-obj-rendered-views
        - memory.md#mem-obj-epistemic-events
        note: Requests for retained material lead to code selection and delivery; lexical selection within
          a requested answer does not create another push.
      - scope: Automatic comparison, page assignment/summary and configuration guidance selection during
          ingestion
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-source-ingest
          - memory.md#mem-obj-page-summaries
          - runtime.md#rt-rte-runtime-setup
          note: Host automatically supplies retained statement lists, titles, page claims or selected
            entity guidance to fresh compiler calls.
        records:
        - runtime.md#rt-rte-source-ingest
        - memory.md#mem-obj-page-summaries
        - runtime.md#rt-rte-runtime-setup
        note: The source-ingest request is not a separate request by the receiving model for existing
          graph/configuration material.
      - scope: Filesystem-event watcher supplying retained file content to extraction
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-source-ingest
          - epistemic.md#epi-obj-source-content
          note: Watcher change events select a file for automatic compiler reading.
        records:
        - runtime.md#rt-rte-source-ingest
        - epistemic.md#epi-obj-source-content
        note: This is push to the admission pipeline, not injection into an ongoing answering conversation.
      - scope: Export files at external human/application readers
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-obj-rendered-views
          - epistemic.md#epi-rte-slide-output
          note: Exported artifacts are available for later reader-initiated access.
        records:
        - memory.md#mem-obj-rendered-views
        - epistemic.md#epi-rte-slide-output
        note: Affordance is not deployed wiring.
      - scope: Opaque provider-retained state, if any, accumulated through use
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-llm-adapter
        note: Provider-retained state delivery direction cannot be determined from inference calls. Provider
          internals were not inspected; inference calls do not resolve provider retention or updates.
          Static model weights are not themselves classified as accumulated memory.
      records:
      - runtime.md#rt-rte-question-answer
      - runtime.md#rt-rte-consensus-answer
      - runtime.md#rt-rte-client-access
      - runtime.md#rt-rte-health-review
      - memory.md#mem-obj-rendered-views
      - memory.md#mem-obj-epistemic-events
      - runtime.md#rt-rte-source-ingest
      - memory.md#mem-obj-page-summaries
      - runtime.md#rt-rte-runtime-setup
      - epistemic.md#epi-obj-source-content
      - epistemic.md#epi-rte-slide-output
      - runtime.md#rt-cmp-llm-adapter
      note: Requested query/client delivery is pull; automatic compilation-context selection and watched-file
        admission are push operations. These are distinct operations, not duplicate labels on one return.
    read_back_signal:
      assessment: partial
      units:
      - scope: Automatic all-existing-statement and all-page-title supply to compiler models
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-source-ingest
          note: Host supplies all existing statements to comparison and all page titles to assignment
            without targeted semantic filtering.
        records:
        - runtime.md#rt-rte-source-ingest
        note: Trigger is a new/changed source compilation; availability in the existing store is the selector
          input.
      - scope: Automatic per-page summary context and entity-specific extraction guidance
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-obj-page-summaries
          - runtime.md#rt-rte-source-ingest
          - runtime.md#rt-rte-runtime-setup
          note: Exact page/kind lookup selects retained parts; merely carrying an ID would not establish
            this value.
        records:
        - memory.md#mem-obj-page-summaries
        - runtime.md#rt-rte-source-ingest
        - runtime.md#rt-rte-runtime-setup
        note: Trigger is summary refresh or extraction. Page ID and resolved entity kind perform actual
          matches selecting delivered page claims or entityPrompts text.
      - scope: Watched changed-file content delivered to compiler
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-rte-source-ingest
          - epistemic.md#epi-obj-source-content
          note: Watcher path selection determines the retained source file whose bytes reach extraction.
        records:
        - runtime.md#rt-rte-source-ingest
        - epistemic.md#epi-obj-source-content
        note: Trigger is debounced filesystem change; event path identifies the actual file read. Startup
          unregistered-path and hash skip predicates additionally constrain processing.
      - scope: Opaque provider-retained state, if any, accumulated through use
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-llm-adapter
        note: Neither a push selector nor its input and selected opaque payload is recorded. Provider
          internals were not inspected; inference calls do not resolve provider retention or updates.
          Static model weights are not themselves classified as accumulated memory.
      records:
      - runtime.md#rt-rte-source-ingest
      - memory.md#mem-obj-page-summaries
      - runtime.md#rt-rte-runtime-setup
      - epistemic.md#epi-obj-source-content
      - runtime.md#rt-cmp-llm-adapter
      note: Signals classify push selectors only. Ordinary question lexical search is a pull selector,
        not inferred-lexical push. Opaque alternatives prevent declaring the entire signal inventory complete.
    trace_learning:
      assessment: partial
      units:
      - scope: Saved question/answer document automatically re-extracted into graph for later questions
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-answer-save
          - runtime.md#rt-rte-source-ingest
          note: Question/answer activity supplies a retained source; automatic extraction/resolution produces
            durable context consumed by subsequent questions.
        records:
        - runtime.md#rt-rte-answer-save
        - runtime.md#rt-rte-source-ingest
        note: Manual save does not make the later model/software claim-admission mechanism manual. Explicit
          ingest or active watch is required; activation is unobserved.
      - scope: Reduced graph-mutation events and return-only critique/consensus outputs
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-epistemic-events
        - runtime.md#rt-rte-health-review
        - runtime.md#rt-rte-consensus-answer
        note: Events alone are raw reduced traces, not an established learned derivative; review/consensus
          callers do not persist revisions. No qualifying automatic trace-fed transformation is established
          for these parts, but no bounded absence record supports a local no.
      - scope: Arbitrary imported documents, initial embedding state and external caller updates
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-obj-source-content
        - memory.md#mem-obj-claims
        - runtime.md#rt-rte-client-access
        note: Unknown original content/control prevents enumerating further trace-fed learning routes;
          generic documents are not assumed to be session logs.
      - scope: Opaque provider-retained state, if any, accumulated through use
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-llm-adapter
        note: Provider-side trace-fed durable updates are not inspected. Provider internals were not inspected;
          inference calls do not resolve provider retention or updates. Static model weights are not themselves
          classified as accumulated memory.
      records:
      - runtime.md#rt-rte-answer-save
      - runtime.md#rt-rte-source-ingest
      - memory.md#mem-obj-epistemic-events
      - runtime.md#rt-rte-health-review
      - runtime.md#rt-rte-consensus-answer
      - epistemic.md#epi-obj-source-content
      - memory.md#mem-obj-claims
      - runtime.md#rt-rte-client-access
      - runtime.md#rt-cmp-llm-adapter
      note: A qualifying answer-trace route is wired after optional human retention, but opaque provider
        updates and unknown arbitrary source origins preclude a system-complete classification. Trace
        learning here means an automatic trace-fed durable update, not demonstrated improvement.
    trace_source:
      assessment: partial
      units:
      - scope: Original question and generated answer in optional saved source, then automatic graph extraction
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - runtime.md#rt-rte-answer-save
          - runtime.md#rt-rte-source-ingest
          note: Saved conversational question/answer content feeds automatic retained claim production
            and later answers.
        records:
        - runtime.md#rt-rte-answer-save
        - runtime.md#rt-rte-source-ingest
        note: The original content is recorded question/answer activity, not the Markdown wrapper or file
          event used to deliver it.
      - scope: Origins of any additional externally supplied trace-fed updates
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-obj-source-content
        - runtime.md#rt-rte-client-access
        - memory.md#mem-obj-epistemic-events
        note: No recorded original corpus or qualifying update chain resolves additional trace sources;
          events retained for display alone establish none.
      - scope: Opaque provider-retained state, if any, accumulated through use
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-llm-adapter
        note: The inputs to any qualifying provider-side write are unknown. Provider internals were not
          inspected; inference calls do not resolve provider retention or updates. Static model weights
          are not themselves classified as accumulated memory.
      records:
      - runtime.md#rt-rte-answer-save
      - runtime.md#rt-rte-source-ingest
      - epistemic.md#epi-obj-source-content
      - runtime.md#rt-rte-client-access
      - memory.md#mem-obj-epistemic-events
      - runtime.md#rt-cmp-llm-adapter
      note: The known qualifying route records question/answer turns. Mutation-event storage does not
        automatically add event-streams, and no tool trace or trajectory source is established for that
        write.
---

# Quicky Wiki memory profile

## Comparison rationale

The authoritative accumulated graph is SQLite, not a vector store or model-weight update. Its text, fixed-rule controls, provenance, relations and reduced event history remain separate units. Files are independently retained surfaces: the standard answer reads the graph, whereas dashboard page display can reload rendered Markdown. Export readers are afforded, not observed. These boundaries follow [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store), [MEM-OBJ-rendered-views](memory.md#mem-obj-rendered-views) and [RT-RTE-question-answer](runtime.md#rt-rte-question-answer).

Reconciliation supersedes the epistemic statement and summary duplicates with [MEM-OBJ-claims](memory.md#mem-obj-claims) and [MEM-OBJ-page-summaries](memory.md#mem-obj-page-summaries). All classifications use those canonical objects. The confidence-state container, SQLite store container and slide-specific parts remain valid overlapping scopes, not replacement identities. No supersession changes a controlled value.

Authority is consumer-relative. Retained text participates in lexical ranking even though fixed code computes retrieval; scores rank review candidates and gate default slide inclusion. That gate is not a universal truth veto: a topic override bypasses it, and ordinary answers have no confidence floor. Hashes, metadata and relations route work. Configured entity guidance supplies instructions rather than ordinary evidence. See [MEM-OBJ-claim-controls](memory.md#mem-obj-claim-controls), [MEM-OBJ-source-register](memory.md#mem-obj-source-register), [EPI-RTE-slide-output](epistemic.md#epi-rte-slide-output) and [RT-BAP-retained-context](runtime.md#rt-bap-retained-context). Host mutation enforcement is not itself evidence that every retained part has enforcement authority.

Requested answers and client reads are pull. Compiler-side automatic provision of existing graph context is a separate push: coarse all-content selection and actual page/kind identity matches coexist. Watch supplies file content to admission, not to an answering conversation. Its path match is a selector of the delivered file, unlike a passive identifier on a requested catalog entry. The record chain is [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [MEM-OBJ-page-summaries](memory.md#mem-obj-page-summaries) and [RT-RTE-runtime-setup](runtime.md#rt-rte-runtime-setup).

The answer-save path separates manual retention from automatic re-extraction. The latter consumes recorded question/answer content and writes claims for later answers; it therefore supports wired trace learning and session-log origin without claiming weight training, improvement or observed activation. Saved output is not independent corroboration. Event rows alone do not establish such an update. See [RT-RTE-answer-save](runtime.md#rt-rte-answer-save), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [MEM-OBJ-epistemic-events](memory.md#mem-obj-epistemic-events).

Curation findings do not promote requested semantic behavior into verified transformations. Summary compression and semantic duplicate avoidance remain claimed at their model mechanisms. Numeric evolution and decay are wired. Prefix filtering removes transient candidates before admission, not retained memory; index rebuilding is access maintenance. No controlled synthesis value follows from uninspected output meaning. See [MEM-OBJ-page-summaries](memory.md#mem-obj-page-summaries), [MEM-OBJ-claim-controls](memory.md#mem-obj-claim-controls), [EPI-RTE-chunk-selection](epistemic.md#epi-rte-chunk-selection) and [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest).

All axes retain provider opacity and route-specific missing coverage instead of inferring absence. Source originals, arbitrary embedding writes, remaining export payloads and provider-side retention limit different units; one inspected graph route cannot resolve them. Missing runs separately prevent operation and benefit claims. See [RT-CMP-llm-adapter](runtime.md#rt-cmp-llm-adapter), [RT-RTE-client-access](runtime.md#rt-rte-client-access) and [MEM-OBJ-rendered-views](memory.md#mem-obj-rendered-views).

Source-read log: none. Classification used only the supplied accepted members and reconciliation; no frozen source reread was needed.
