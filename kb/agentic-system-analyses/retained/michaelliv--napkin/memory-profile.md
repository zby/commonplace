---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Memory profile of Napkin: retained vault content, access structures, agent-mediated updates
  and shipped benchmark consumers.'
run-id: AAS-2026-10-12-napkin-2b85bef38252-01
source-identity: https://github.com/Michaelliv/napkin
reviewed-boundary: 7582d6a46f5a11995956e60a59c41a5b242109f1
memory-comparison:
  version: 2
  scope: Retained Markdown/daily/folder notes and NAPKIN.md; persisted templates and retrieval/layout
    configuration; search/overview caches including opaque index payload; base definitions, canvas and
    bookmarks; benchmark source/summary notes and retained reports; packaged session distill/tend update
    routes and separately claimed external background update/incremental state. Includes unresolved initial
    provenance, external context delivery and cursor alternatives. Excludes static shipped skill/method
    text as a memory object, external provider weights, installed-package changes, process-only vault/template
    registries, transient SQL/link/graph/query projections and ordinary current-run state. Temporary benchmark
    notes are included within their later-question-consumer horizon.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Markdown notes, daily notes, folder descriptions, NAPKIN.md and persisted note templates
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-markdown-notes
          - memory.md#mem-obj-napkin
          - memory.md#mem-obj-note-templates
          note: Markdown bytes survive mutations and reach subsequent file readers.
        records:
        - memory.md#mem-obj-markdown-notes
        - memory.md#mem-obj-napkin
        - memory.md#mem-obj-note-templates
        note: All these retained objects have recorded filesystem locations.
      - scope: Disk configuration, search-cache payload/metadata and overview-cache result
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-rte-machinery-change
          - memory.md#mem-obj-search-cache
          - memory.md#mem-obj-overview-cache
          note: Configuration and both caches are persisted under the resolved configuration path.
        records:
        - runtime.md#rt-rte-machinery-change
        - memory.md#mem-obj-search-cache
        - memory.md#mem-obj-overview-cache
        note: JSON encoding, including an opaque serialized index, does not change the known filesystem
          substrate.
      - scope: Base definitions, canvas content and bookmarks
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-base
          - memory.md#mem-obj-canvas
          - memory.md#mem-obj-bookmarks
          note: YAML base definitions and JSON canvas/bookmark stores reload from disk.
        records:
        - memory.md#mem-obj-base
        - memory.md#mem-obj-canvas
        - memory.md#mem-obj-bookmarks
        note: The base query database is transient and excluded from the retained substrate inventory.
      - scope: Benchmark source notes, supplied LoCoMo summaries and retained evaluation reports
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-rte-benchmark-answer
          - memory.md#mem-rte-benchmark-variants
          - memory.md#mem-obj-session-summary
          - memory.md#mem-obj-evaluation-results
          note: Drivers retain note files before question invocations and can persist evaluation report
            files.
        records:
        - runtime.md#rt-rte-benchmark-answer
        - memory.md#mem-rte-benchmark-variants
        - memory.md#mem-obj-session-summary
        - memory.md#mem-obj-evaluation-results
        note: Temporary files qualify during their later-consumer horizon; current-process result arrays
          alone are excluded.
      - scope: External background-distillation incremental cursor or checkpoint
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-background-distill
        note: The design names new messages since the prior run, but the unavailable extension leaves
          retained state, format and persistence location uninspected. No substrate is inferred.
      records:
      - memory.md#mem-obj-markdown-notes
      - memory.md#mem-obj-napkin
      - memory.md#mem-obj-note-templates
      - runtime.md#rt-rte-machinery-change
      - memory.md#mem-obj-search-cache
      - memory.md#mem-obj-overview-cache
      - memory.md#mem-obj-base
      - memory.md#mem-obj-canvas
      - memory.md#mem-obj-bookmarks
      - runtime.md#rt-rte-benchmark-answer
      - memory.md#mem-rte-benchmark-variants
      - memory.md#mem-obj-session-summary
      - memory.md#mem-obj-evaluation-results
      - memory.md#mem-rte-background-distill
      note: The recorded local inventory is file-backed, including the opaque dependency index. External
        incremental cursor persistence is unresolved; provider weights are excluded as external runtime
        components, not accumulated vault memory.
    representational_form:
      assessment: partial
      units:
      - scope: Note/context/template prose, canvas text/labels and benchmark source/summary/answer prose
          at readers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-markdown-notes
          - memory.md#mem-obj-napkin
          - memory.md#mem-obj-note-templates
          - memory.md#mem-obj-canvas
          - memory.md#mem-obj-session-summary
          - memory.md#mem-obj-evaluation-results
          note: Human/model-readable bodies, guidance, descriptions and answer strings are retained and
            exposed by file or store reads.
        records:
        - memory.md#mem-obj-markdown-notes
        - memory.md#mem-obj-napkin
        - memory.md#mem-obj-note-templates
        - memory.md#mem-obj-canvas
        - memory.md#mem-obj-session-summary
        - memory.md#mem-obj-evaluation-results
        note: These recorded readable parts are separate from their structural fields.
      - scope: Note frontmatter/tasks/link targets, paths/mtimes, template placeholders, disk configuration,
          cache metadata, base definitions, canvas structure, bookmark references and evaluation metrics
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-markdown-notes
          - memory.md#mem-obj-note-templates
          - runtime.md#rt-rte-machinery-change
          - memory.md#mem-obj-search-cache
          - memory.md#mem-obj-overview-cache
          - memory.md#mem-obj-base
          - memory.md#mem-obj-canvas
          - memory.md#mem-obj-bookmarks
          - memory.md#mem-obj-evaluation-results
          note: Structured fields, IDs, geometry, expressions, cache keys and numeric metrics are consumed
            by program rules.
        records:
        - memory.md#mem-obj-markdown-notes
        - memory.md#mem-obj-note-templates
        - runtime.md#rt-rte-machinery-change
        - memory.md#mem-obj-search-cache
        - memory.md#mem-obj-overview-cache
        - memory.md#mem-obj-base
        - memory.md#mem-obj-canvas
        - memory.md#mem-obj-bookmarks
        - memory.md#mem-obj-evaluation-results
        note: Localized fields have fixed parser/selector consumers; no embedding provenance is inferred.
      - scope: Overview-cache copied context and folder descriptions at caller display
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-overview-cache
          note: Retained about/context strings reach later overview callers unchanged or trimmed.
        records:
        - memory.md#mem-obj-overview-cache
        note: The display projection contains prose as well as separately classified structural arrays.
      - scope: Serialized search dependency index internals
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-search-cache
        note: The serialized string and its loader are known, but internal operative representation is
          opaque. No vector or parametric value follows from serialization or lexical behavior.
      - scope: External incremental cursor/checkpoint payload
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-background-distill
        note: Unavailable extension implementation prevents classifying the retained payload, if any.
      records:
      - memory.md#mem-obj-markdown-notes
      - memory.md#mem-obj-napkin
      - memory.md#mem-obj-note-templates
      - memory.md#mem-obj-canvas
      - memory.md#mem-obj-session-summary
      - memory.md#mem-obj-evaluation-results
      - runtime.md#rt-rte-machinery-change
      - memory.md#mem-obj-search-cache
      - memory.md#mem-obj-overview-cache
      - memory.md#mem-obj-base
      - memory.md#mem-obj-bookmarks
      - memory.md#mem-rte-background-distill
      note: Readable prose and fixed-rule metadata have distinct consumers. An opaque dependency index
        and external cursor prevent complete payload classification; external model weights and transient
        query data are excluded.
    lineage:
      assessment: partial
      units:
      - scope: Packaged distill session-to-declarative-note path
        assessment: known
        findings:
        - value: trace-extracted
          basis: claimed
          records:
          - runtime.md#rt-rte-distill-session
          note: Session findings are selected, clustered and transformed into future-use notes by the
            instructed model.
        records:
        - runtime.md#rt-rte-distill-session
        - memory.md#mem-obj-markdown-notes
        note: Coverage is the specified transformation, not generic note initialization or demonstrated
          semantic preservation.
      - scope: Separate-model background session-to-note path
        assessment: known
        findings:
        - value: trace-extracted
          basis: claimed
          records:
          - memory.md#mem-rte-background-distill
          note: New conversational entries are the claimed inputs to generated vault notes.
        records:
        - memory.md#mem-rte-background-distill
        note: This is a documented derivation path; the external implementation remains unavailable.
      - scope: Benchmark dialogue/paragraph ingestion and copying supplied summaries/observations
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - runtime.md#rt-rte-benchmark-answer
          - memory.md#mem-rte-benchmark-variants
          - memory.md#mem-obj-session-summary
          note: Drivers copy external dataset text and summaries into retained Markdown.
        records:
        - runtime.md#rt-rte-benchmark-answer
        - memory.md#mem-rte-benchmark-variants
        - memory.md#mem-obj-session-summary
        note: Subsequent copying is inspected even though dataset generation is not.
      - scope: Search/overview cache projections and benchmark report fields
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-search-cache
          - memory.md#mem-obj-overview-cache
          - memory.md#mem-obj-evaluation-results
          note: Algorithms derive indices, access metadata, display projections and evaluation report
            fields from supplied content and events.
        records:
        - memory.md#mem-obj-search-cache
        - memory.md#mem-obj-overview-cache
        - memory.md#mem-obj-evaluation-results
        note: This covers recorded downstream compilation, not unseen index internals or model-answer
          reasoning.
      - scope: Template copying/instantiation into new or existing notes and scaffolded context
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-note-templates
          - memory.md#mem-rte-auxiliary-edits
          - runtime.md#rt-rte-machinery-change
          note: Stored or shipped template text is copied into retained notes/context.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-note-templates
          - memory.md#mem-rte-auxiliary-edits
          note: The insertion path substitutes symbolic variables before persisting the copied text; not
            every template consumer substitutes.
        records:
        - memory.md#mem-obj-note-templates
        - memory.md#mem-rte-auxiliary-edits
        - runtime.md#rt-rte-machinery-change
        note: Known copying is separate from the template original author.
      - scope: Canvas structure created through caller operations
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-canvas
          - memory.md#mem-rte-structured-access
          note: Caller-supplied nodes and edges are directly constructed and edited, not extracted from
            traces by this path.
        records:
        - memory.md#mem-obj-canvas
        - memory.md#mem-rte-structured-access
        note: The recorded construction path does not identify the caller as human.
      - scope: Generic existing notes, context, templates, configuration, base/canvas/bookmark files and
          source-summary upstream generation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-markdown-notes
        - memory.md#mem-obj-napkin
        - memory.md#mem-obj-note-templates
        - runtime.md#rt-rte-machinery-change
        - memory.md#mem-obj-base
        - memory.md#mem-obj-canvas
        - memory.md#mem-obj-bookmarks
        - memory.md#mem-obj-session-summary
        note: The records leave original authorship and initialization unresolved; supported subsequent
          paths do not settle them.
      - scope: Opaque index internal derivation and external incremental state
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-search-cache
        - memory.md#mem-rte-background-distill
        note: Dependency internals and extension checkpoint production were not inspected, preventing
          complete provenance classification.
      records:
      - runtime.md#rt-rte-distill-session
      - memory.md#mem-obj-markdown-notes
      - memory.md#mem-rte-background-distill
      - runtime.md#rt-rte-benchmark-answer
      - memory.md#mem-rte-benchmark-variants
      - memory.md#mem-obj-session-summary
      - memory.md#mem-obj-search-cache
      - memory.md#mem-obj-overview-cache
      - memory.md#mem-obj-evaluation-results
      - memory.md#mem-obj-note-templates
      - memory.md#mem-rte-auxiliary-edits
      - runtime.md#rt-rte-machinery-change
      - memory.md#mem-obj-canvas
      - memory.md#mem-rte-structured-access
      - memory.md#mem-obj-napkin
      - memory.md#mem-obj-base
      - memory.md#mem-obj-bookmarks
      note: Known later derivations do not resolve initial provenance. Copying supplied LoCoMo summaries
        establishes imported lineage, not their upstream extraction process.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retained note/context/summary and canvas text supplied as caller reference
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-markdown-notes
          - memory.md#mem-obj-napkin
          - memory.md#mem-obj-session-summary
          - memory.md#mem-obj-canvas
          - runtime.md#rt-rte-vault-retrieval
          - memory.md#mem-rte-structured-access
          note: Later reads return content and context to requesting callers.
        records:
        - memory.md#mem-obj-markdown-notes
        - memory.md#mem-obj-napkin
        - memory.md#mem-obj-session-summary
        - memory.md#mem-obj-canvas
        - runtime.md#rt-rte-vault-retrieval
        - memory.md#mem-rte-structured-access
        note: The effect is availability as evidence/context, not compliance or truth certification.
      - scope: Retained benchmark notes at question-agent evidence consumer
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - runtime.md#rt-rte-benchmark-answer
          - memory.md#mem-rte-benchmark-variants
          - runtime.md#rt-bap-benchmark-evidence
          note: Previously written dialogues, paragraphs and summaries supply candidate answer evidence
            through requested retrieval.
        records:
        - runtime.md#rt-rte-benchmark-answer
        - memory.md#mem-rte-benchmark-variants
        - runtime.md#rt-bap-benchmark-evidence
        note: The shipped drivers request later question-agent retrieval; exercised dependence remains
          unobserved.
      - scope: Note terms, basenames, links/mtimes and serialized index/access metadata at search ranking
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-markdown-notes
          - memory.md#mem-obj-search-cache
          - runtime.md#rt-rte-vault-retrieval
          note: Lexical content, backlinks and relative recency affect relative result scores and order.
        records:
        - memory.md#mem-obj-markdown-notes
        - memory.md#mem-obj-search-cache
        - runtime.md#rt-rte-vault-retrieval
        note: A fixed scoring algorithm still gives retained content ranking authority.
      - scope: Disk retrieval/layout settings, overview handles, base query definitions and saved access
          references at selectors or requesting callers
        assessment: partial
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-rte-machinery-change
          - memory.md#mem-obj-overview-cache
          - memory.md#mem-obj-base
          - memory.md#mem-rte-structured-access
          note: Settings select retrieval scope/budgets; overview handles guide access; retained base
            definitions select views and projections.
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-bookmarks
          - memory.md#mem-rte-structured-access
          note: Bookmark entries expose saved access information to callers without executing their targets.
        records:
        - runtime.md#rt-rte-machinery-change
        - memory.md#mem-obj-overview-cache
        - memory.md#mem-obj-base
        - memory.md#mem-obj-bookmarks
        - memory.md#mem-rte-structured-access
        note: Base filter/formula internals are only partly inspected. Bookmarks expose destinations,
          not automatically executed queries.
      - scope: Stored template section guidance and project conventions at external model guidance consumers
        assessment: partial
        findings:
        - value: instruction
          basis: afforded
          records:
          - memory.md#mem-obj-note-templates
          - memory.md#mem-obj-napkin
          note: Retained section guidance and project conventions can guide later model readers.
        - value: instruction
          basis: claimed
          records:
          - memory.md#mem-obj-note-templates
          - memory.md#mem-obj-napkin
          - memory.md#mem-rte-background-distill
          - runtime.md#rt-rte-distill-session
          note: The background design supplies templates/context to its model; the skill describes NAPKIN.md
            as always-loaded host context.
        records:
        - memory.md#mem-obj-note-templates
        - memory.md#mem-obj-napkin
        - memory.md#mem-rte-background-distill
        - runtime.md#rt-rte-distill-session
        note: Template bytes are wired into notes, but host interpretation and automatic convention delivery
          remain external.
      - scope: Session experience at packaged distill update consumer
        assessment: known
        findings:
        - value: learning
          basis: claimed
          records:
          - runtime.md#rt-rte-distill-session
          note: Session findings guide selection and revision of durable future-use notes.
        records:
        - runtime.md#rt-rte-distill-session
        note: The local authority is the claimed durable update path, separate from downstream knowledge
          authority.
      - scope: Conversation entries at separate-model background update consumer
        assessment: known
        findings:
        - value: learning
          basis: claimed
          records:
          - memory.md#mem-rte-background-distill
          note: New messages guide production of notes intended for later vault consumers.
        records:
        - memory.md#mem-rte-background-distill
        note: This is claimed authority, not verified scheduler or model operation.
      - scope: Evaluation report text and metrics at aggregation/report consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-evaluation-results
          - epistemic.md#epi-rte-score-report
          note: Stored answer/metric records supply performance information to reporting readers.
        records:
        - memory.md#mem-obj-evaluation-results
        - epistemic.md#epi-rte-score-report
        note: Scores affect reports, not knowledge admission or policy successors.
      - scope: External automatic context injection, incremental checkpoint consumer and graph renderer
          continuation
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-napkin
        - memory.md#mem-rte-background-distill
        - memory.md#mem-obj-markdown-notes
        note: External delivery/state and partially inspected rendering do not establish additional instruction,
          enforcement or routing effects. Static packaged skills and core guards are not accumulated memory
          criteria.
      records:
      - memory.md#mem-obj-markdown-notes
      - memory.md#mem-obj-napkin
      - memory.md#mem-obj-session-summary
      - memory.md#mem-obj-canvas
      - runtime.md#rt-rte-vault-retrieval
      - memory.md#mem-rte-structured-access
      - runtime.md#rt-rte-benchmark-answer
      - memory.md#mem-rte-benchmark-variants
      - runtime.md#rt-bap-benchmark-evidence
      - memory.md#mem-obj-search-cache
      - runtime.md#rt-rte-machinery-change
      - memory.md#mem-obj-overview-cache
      - memory.md#mem-obj-base
      - memory.md#mem-obj-bookmarks
      - memory.md#mem-obj-note-templates
      - memory.md#mem-rte-background-distill
      - runtime.md#rt-rte-distill-session
      - memory.md#mem-obj-evaluation-results
      - epistemic.md#epi-rte-score-report
      note: Authority is local to consumed parts and effects. Wired routing/ranking coexist with claimed
        trace-fed learning and external guidance. Unknown injection and partially inspected base/graph
        consumers prevent complete authority coverage.
    write_agency:
      assessment: partial
      units:
      - scope: Search/overview cache admission and benchmark note/result ingestion
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-search-cache
          - memory.md#mem-obj-overview-cache
          - runtime.md#rt-rte-benchmark-answer
          - memory.md#mem-rte-benchmark-variants
          - memory.md#mem-obj-evaluation-results
          note: Cache writers and benchmark loops admit derived or imported retained material.
        records:
        - memory.md#mem-obj-search-cache
        - memory.md#mem-obj-overview-cache
        - runtime.md#rt-rte-benchmark-answer
        - memory.md#mem-rte-benchmark-variants
        - memory.md#mem-obj-evaluation-results
        note: Algorithms and drivers admit these contents without a per-content operator decision.
      - scope: Packaged distill and ordinary tend semantic admission/repair
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records:
          - runtime.md#rt-rte-distill-session
          - runtime.md#rt-rte-tend-vault
          - workflow.md#wf-rte-distill-verification
          note: User initiation does not add note-by-note or repair-by-repair approval.
        records:
        - runtime.md#rt-rte-distill-session
        - runtime.md#rt-rte-tend-vault
        - workflow.md#wf-rte-distill-verification
        note: The instructed external model makes keep/skip, merge, repair and retirement decisions.
      - scope: Background model/extension note admission
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records:
          - memory.md#mem-rte-background-distill
          note: Generated notes are claimed to be parsed and written directly, with NO_DISTILL permitting
            skip.
        records:
        - memory.md#mem-rte-background-distill
        note: The stated admission controller is a separate model/extension, not the human launching pi.
      - scope: Tend proposed new-template adoption
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records:
          - runtime.md#rt-rte-tend-vault
          note: The skill reports a schema candidate and reserves template creation to the user.
        records:
        - runtime.md#rt-rte-tend-vault
        note: This human schema decision is separate from ordinary tend cleanup and unrestricted template
          APIs.
      - scope: Generic CRUD, auxiliary edits, template/scaffold/configuration, base/canvas/bookmark admissions
          and pre-existing content
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-caller-mutation
        - memory.md#mem-rte-auxiliary-edits
        - runtime.md#rt-rte-machinery-change
        - memory.md#mem-rte-structured-access
        - memory.md#mem-obj-markdown-notes
        - memory.md#mem-obj-note-templates
        - memory.md#mem-obj-base
        - memory.md#mem-obj-canvas
        - memory.md#mem-obj-bookmarks
        note: Caller identity and initial admission control are unspecified. Physical filesystem I/O does
          not establish automatic admission or human approval.
      records:
      - memory.md#mem-obj-search-cache
      - memory.md#mem-obj-overview-cache
      - runtime.md#rt-rte-benchmark-answer
      - memory.md#mem-rte-benchmark-variants
      - memory.md#mem-obj-evaluation-results
      - runtime.md#rt-rte-distill-session
      - runtime.md#rt-rte-tend-vault
      - workflow.md#wf-rte-distill-verification
      - memory.md#mem-rte-background-distill
      - runtime.md#rt-rte-caller-mutation
      - memory.md#mem-rte-auxiliary-edits
      - runtime.md#rt-rte-machinery-change
      - memory.md#mem-rte-structured-access
      - memory.md#mem-obj-markdown-notes
      - memory.md#mem-obj-note-templates
      - memory.md#mem-obj-base
      - memory.md#mem-obj-canvas
      - memory.md#mem-obj-bookmarks
      note: Automatic admission is supported locally; generic callers and initial-content admissions do
        not identify human control. Starting a workflow or benchmark is not per-content approval.
    curation_operations:
      assessment: partial
      units:
      - scope: Caller replacement/property/task edits and canvas entry edits
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-rte-caller-mutation
          - memory.md#mem-rte-auxiliary-edits
          - memory.md#mem-obj-canvas
          - memory.md#mem-rte-structured-access
          - epistemic.md#epi-rte-property-edit
          note: Overwrite and field/status/node edits change already retained entries.
        records:
        - runtime.md#rt-rte-caller-mutation
        - memory.md#mem-rte-auxiliary-edits
        - memory.md#mem-obj-canvas
        - memory.md#mem-rte-structured-access
        - epistemic.md#epi-rte-property-edit
        note: These revise existing retained entries; semantic validity or better quality is not implied.
      - scope: Ordinary trash withdrawal from search/listing
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records:
          - runtime.md#rt-rte-caller-mutation
          - memory.md#mem-obj-markdown-notes
          note: Default delete moves notes to excluded trash rather than erasing their history globally.
        records:
        - runtime.md#rt-rte-caller-mutation
        - memory.md#mem-obj-markdown-notes
        note: Reliance is withdrawn on walker-based routes while bytes remain and exact-path read still
          works.
      - scope: Permanent deletion of retained Markdown notes
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - runtime.md#rt-rte-caller-mutation
          note: The permanent-delete branch unlinks the retained note, forgetting its content rather than retaining it in trash.
        records:
        - runtime.md#rt-rte-caller-mutation
        - memory.md#mem-obj-markdown-notes
        note: Permanent unlink is an implemented forgetting operation, separate from ordinary trash withdrawal. No timed or scored forgetting policy is required; successful execution and downstream benefit remain unobserved.
      - scope: Packaged session distill transformation and existing-note integration
        assessment: known
        findings:
        - value: consolidate
          basis: claimed
          records:
          - runtime.md#rt-rte-distill-session
          note: Session material is selected and compressed into declarative notes rather than conversational
            minutes.
        - value: dedup
          basis: claimed
          records:
          - runtime.md#rt-rte-distill-session
          note: Already retained content is dropped and same-subject discoveries are merged rather than
            duplicated.
        - value: evolve
          basis: claimed
          records:
          - runtime.md#rt-rte-distill-session
          note: New information and contradictions are integrated into existing sections.
        records:
        - runtime.md#rt-rte-distill-session
        note: The consolidation classification follows selected conclusions/reasons and reduced topic-based
          output. Actual output faithfulness is not established.
      - scope: Tend duplicate merge, note revision and retirement
        assessment: known
        findings:
        - value: dedup
          basis: claimed
          records:
          - runtime.md#rt-rte-tend-vault
          note: Obvious overlap is merged and the duplicate loser retired.
        - value: evolve
          basis: claimed
          records:
          - runtime.md#rt-rte-tend-vault
          note: Retained notes, links, tags and context are corrected or integrated.
        - value: invalidate
          basis: claimed
          records:
          - runtime.md#rt-rte-tend-vault
          note: Superseded notes are retired to trash with planned backlink repair.
        records:
        - runtime.md#rt-rte-tend-vault
        note: These are specified operations, not an implemented semantic supervisor.
      - scope: Background-model note transformation
        assessment: partial
        findings:
        - value: consolidate
          basis: claimed
          records:
          - memory.md#mem-rte-background-distill
          note: A capture model selects new conversation material and produces structured future-use notes.
        records:
        - memory.md#mem-rte-background-distill
        note: The design supports selected conversation compression; unknown overwrite/withdrawal and
          cursor behavior prevent complete classification.
      - scope: Inferred generalizations, arbitrary caller payload changes and supplied LoCoMo summary
          upstream transformations
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-distill-session
        - epistemic.md#epi-obj-vault-prose
        - runtime.md#rt-rte-caller-mutation
        - memory.md#mem-obj-session-summary
        note: An inferred marker or indeterminate content relation does not establish a new non-entailed
          claim. Upstream summary production and arbitrary supplied changes do not determine synthesis
          or other semantic operations.
      - scope: Opaque serialized index and external maintenance/checkpoint internals
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-search-cache
        - memory.md#mem-rte-background-distill
        note: Index derivation alone is not consolidation, deduplication or decay; unavailable internal
          transformation rules prevent additional conclusions.
      records:
      - runtime.md#rt-rte-caller-mutation
      - memory.md#mem-rte-auxiliary-edits
      - memory.md#mem-obj-canvas
      - memory.md#mem-rte-structured-access
      - epistemic.md#epi-rte-property-edit
      - memory.md#mem-obj-markdown-notes
      - runtime.md#rt-rte-distill-session
      - runtime.md#rt-rte-tend-vault
      - memory.md#mem-rte-background-distill
      - epistemic.md#epi-obj-vault-prose
      - memory.md#mem-obj-session-summary
      - memory.md#mem-obj-search-cache
      note: Known byte-level revision, trash withdrawal and permanent-delete forgetting, and claimed semantic consolidation/duplicate integration
        remain separate. Opaque external transformations and generic caller content prevent a complete
        operation inventory; cache rebuilding alone supplies no curation value.
    read_back_direction:
      assessment: partial
      units:
      - scope: Later overview/search/full-note requests including cached inputs and context bundled with
          overview
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-vault-retrieval
          - memory.md#mem-obj-markdown-notes
          - memory.md#mem-obj-napkin
          - memory.md#mem-obj-search-cache
          - memory.md#mem-obj-overview-cache
          note: Caller requests retained material; algorithms select and return it in CLI/SDK results.
        records:
        - runtime.md#rt-rte-vault-retrieval
        - memory.md#mem-obj-markdown-notes
        - memory.md#mem-obj-napkin
        - memory.md#mem-obj-search-cache
        - memory.md#mem-obj-overview-cache
        note: A broad context return fulfilling overview is pull, not another push.
      - scope: Daily/template/field, base, canvas and bookmark reads or update-consumer requests
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-auxiliary-edits
          - memory.md#mem-obj-note-templates
          - memory.md#mem-rte-structured-access
          - memory.md#mem-obj-base
          - memory.md#mem-obj-canvas
          - memory.md#mem-obj-bookmarks
          note: Explicit operations reload stored objects or copy a requested retained template.
        records:
        - memory.md#mem-rte-auxiliary-edits
        - memory.md#mem-obj-note-templates
        - memory.md#mem-rte-structured-access
        - memory.md#mem-obj-base
        - memory.md#mem-obj-canvas
        - memory.md#mem-obj-bookmarks
        note: A template selected for create/insert is requested retained input at an update consumer.
      - scope: Benchmark question-agent requested retrieval and evaluator report aggregation
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-benchmark-answer
          - memory.md#mem-rte-benchmark-variants
          - memory.md#mem-obj-evaluation-results
          note: Question agents are instructed to request stored evidence and evaluator aggregation consumes
            retained result fields.
        records:
        - runtime.md#rt-rte-benchmark-answer
        - memory.md#mem-rte-benchmark-variants
        - memory.md#mem-obj-evaluation-results
        note: Earlier writes have later question/aggregation consumers; actual exercise remains unobserved.
      - scope: NAPKIN.md always-loaded host context
        assessment: partial
        findings:
        - value: push
          basis: claimed
          records:
          - memory.md#mem-obj-napkin
          - runtime.md#rt-rte-distill-session
          note: The always-loaded description claims broad context is supplied without a specific consumer
            retrieval request.
        records:
        - memory.md#mem-obj-napkin
        - runtime.md#rt-rte-distill-session
        note: The skill describes automatic host loading, but the host implementation, trigger and actual
          delivery are unavailable.
      - scope: External background capture context/templates, incremental cursor delivery and benchmark
          extension injection
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-background-distill
        - memory.md#mem-obj-napkin
        - runtime.md#rt-rte-benchmark-answer
        - memory.md#mem-rte-benchmark-variants
        note: Design names inputs and external extensions, but request/selection/delivery operations are
          not inspected. No additional push wiring is inferred.
      - scope: Graph human UI continuation
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-markdown-notes
        note: The recorded graph snapshot is current-run data, not a distinct retained store; unread renderer
          continuation prevents classifying later display delivery.
      records:
      - runtime.md#rt-rte-vault-retrieval
      - memory.md#mem-obj-markdown-notes
      - memory.md#mem-obj-napkin
      - memory.md#mem-obj-search-cache
      - memory.md#mem-obj-overview-cache
      - memory.md#mem-rte-auxiliary-edits
      - memory.md#mem-obj-note-templates
      - memory.md#mem-rte-structured-access
      - memory.md#mem-obj-base
      - memory.md#mem-obj-canvas
      - memory.md#mem-obj-bookmarks
      - runtime.md#rt-rte-benchmark-answer
      - memory.md#mem-rte-benchmark-variants
      - memory.md#mem-obj-evaluation-results
      - runtime.md#rt-rte-distill-session
      - memory.md#mem-rte-background-distill
      note: Requested core and shipped benchmark routes are established. The always-loaded host-context
        description supplies a claimed push path, while actual external injection/cursor delivery and
        graph rendering remain unresolved.
    read_back_signal:
      assessment: partial
      units:
      - scope: Claimed always-loaded NAPKIN.md context selection
        assessment: partial
        findings:
        - value: coarse
          basis: claimed
          records:
          - memory.md#mem-obj-napkin
          - runtime.md#rt-rte-distill-session
          note: On the claimed host-loading trigger, the fixed broad project context note is selected
            as a whole, not by task relevance or identity matching.
        records:
        - memory.md#mem-obj-napkin
        - runtime.md#rt-rte-distill-session
        note: The claim is broad availability-based loading. Exact host trigger, filtering and injection
          are not recorded.
      - scope: Requested core/template/structured/benchmark retrieval chains
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-vault-retrieval
        - memory.md#mem-rte-auxiliary-edits
        - memory.md#mem-rte-structured-access
        - runtime.md#rt-rte-benchmark-answer
        - memory.md#mem-rte-benchmark-variants
        note: These recorded chains fulfill explicit requests. Their query/path/view selectors therefore
          do not classify push signals.
      - scope: External extension/background cursor selection and graph continuation
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-background-distill
        - memory.md#mem-obj-napkin
        - runtime.md#rt-rte-benchmark-answer
        - memory.md#mem-rte-benchmark-variants
        - memory.md#mem-obj-markdown-notes
        note: Missing external direction and selection details prevent concluding whether there is a push
          signal or assigning targeted identity, lexical, embedding or judgment values.
      records:
      - memory.md#mem-obj-napkin
      - runtime.md#rt-rte-distill-session
      - runtime.md#rt-rte-vault-retrieval
      - memory.md#mem-rte-auxiliary-edits
      - memory.md#mem-rte-structured-access
      - runtime.md#rt-rte-benchmark-answer
      - memory.md#mem-rte-benchmark-variants
      - memory.md#mem-rte-background-distill
      - memory.md#mem-obj-markdown-notes
      note: Only the claimed broad always-loaded context supports a positive push signal. Requested paths,
        base IDs, bookmark references and query ranking do not establish identifier or lexical push. Unresolved
        external direction units prevent system-wide inapplicability.
    trace_learning:
      assessment: partial
      units:
      - scope: Packaged distill session-to-note-to-future-reader chain
        assessment: known
        findings:
        - value: 'yes'
          basis: claimed
          records:
          - runtime.md#rt-rte-distill-session
          - memory.md#mem-obj-markdown-notes
          note: The model selects session findings and writes lasting notes for future search/read.
        records:
        - runtime.md#rt-rte-distill-session
        - memory.md#mem-obj-markdown-notes
        note: Qualifies by the claimed automatic trace-fed durable content write and later knowledge consumer,
          not by observed improvement.
      - scope: Separate-model background conversation-to-vault chain
        assessment: known
        findings:
        - value: 'yes'
          basis: claimed
          records:
          - memory.md#mem-rte-background-distill
          note: New conversational entries feed model-produced durable notes intended for ordinary later
            retrieval.
        records:
        - memory.md#mem-rte-background-distill
        note: The documented write and intended later vault consumer establish a claimed qualifying route,
          not inspected implementation.
      - scope: Benchmark raw-dialogue ingestion, supplied summaries and evaluation outputs
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-benchmark-answer
        - memory.md#mem-rte-benchmark-variants
        - memory.md#mem-obj-session-summary
        - memory.md#mem-obj-evaluation-results
        - epistemic.md#epi-rte-score-report
        note: Retaining raw logs alone is not a qualifying transformation. Summary production is upstream
          and uninspected; reports have no inspected score-to-behavior update. No bounded absence record
          warrants a local no for all these alternatives.
      - scope: Other generic content edits and external incremental state/host behavior
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-caller-mutation
        - memory.md#mem-rte-auxiliary-edits
        - memory.md#mem-rte-structured-access
        - memory.md#mem-rte-background-distill
        note: Generic callers do not identify trace-fed admission or a durable behavior-shaping chain;
          external cursor/host implementation is unavailable.
      records:
      - runtime.md#rt-rte-distill-session
      - memory.md#mem-obj-markdown-notes
      - memory.md#mem-rte-background-distill
      - runtime.md#rt-rte-benchmark-answer
      - memory.md#mem-rte-benchmark-variants
      - memory.md#mem-obj-session-summary
      - memory.md#mem-obj-evaluation-results
      - epistemic.md#epi-rte-score-report
      - runtime.md#rt-rte-caller-mutation
      - memory.md#mem-rte-auxiliary-edits
      - memory.md#mem-rte-structured-access
      note: Two specified automatic session-to-vault routes support local yes findings at claimed strength.
        Raw log ingestion, supplied summaries and evaluator reports do not establish an additional qualifying
        update; unresolved derivation and external state prevent a system-wide no.
    trace_source:
      assessment: partial
      units:
      - scope: Packaged distill recorded working-session findings
        assessment: partial
        findings:
        - value: session-logs
          basis: claimed
          records:
          - runtime.md#rt-rte-distill-session
          note: The instructed update consumes current-session conversational material as data.
        records:
        - runtime.md#rt-rte-distill-session
        note: The session includes user/agent findings, but the record does not establish whether original
          tool-result or linked-trajectory material is consumed as such.
      - scope: Background new-user/assistant-message extraction
        assessment: known
        findings:
        - value: session-logs
          basis: claimed
          records:
          - memory.md#mem-rte-background-distill
          note: The separate capture model receives new user/assistant messages since its previous run.
        records:
        - memory.md#mem-rte-background-distill
        note: This input branch explicitly names conversational entries; timer events are triggers, not
          retained learning-source content.
      - scope: Additional opaque host/update inputs and supplied-summary upstream source
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-background-distill
        - memory.md#mem-obj-session-summary
        - runtime.md#rt-rte-distill-session
        note: Unavailable extension/dataset producer and unspecified original findings prevent complete
          tool-traces, event-streams or trajectories classification.
      - scope: Raw benchmark ingestion and evaluation report routes without established qualifying update
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-benchmark-answer
        - memory.md#mem-rte-benchmark-variants
        - memory.md#mem-obj-evaluation-results
        note: Raw dialogue origin is known, but trace_source is scoped to qualifying learning writes.
          No complete bounded trace-learning absence or additional qualifying transformation is established
          for these routes.
      records:
      - runtime.md#rt-rte-distill-session
      - memory.md#mem-rte-background-distill
      - memory.md#mem-obj-session-summary
      - runtime.md#rt-rte-benchmark-answer
      - memory.md#mem-rte-benchmark-variants
      - memory.md#mem-obj-evaluation-results
      note: Recorded conversational inputs support session-logs on each claimed qualifying route. They
        do not justify event-streams merely because a timer triggers the update. Tool/environment content
        inside findings and opaque host inputs prevent complete origin coverage.
---

# Napkin memory profile

## Comparison rationale

The scope is accumulated vault material and its access/update routes, not every storage object in the runtime. Temporary benchmark vaults count because later question invocations consume earlier driver writes; transient SQLite query databases and reconstructed link/graph snapshots are not persistent memory substrates. External model weights are components outside this vault-memory boundary, not evidence for model-weight storage or parametric vault memory. See [MEM-OBJ-base](memory.md#mem-obj-base), [MEM-RTE-benchmark-variants](memory.md#mem-rte-benchmark-variants), [MEM-OBJ-search-cache](memory.md#mem-obj-search-cache) and [RT-CMP-pi-model](runtime.md#rt-cmp-pi-model).

No supersession affects a value. Reconciliation retains valid containers and their parts. This profile uses the memory object's finer distinctions without replacing the broader epistemic containers. In particular, the supplied LoCoMo summary's inspected copy supports imported lineage, not a Napkin extraction route or its unknown upstream learning mechanism. See [MEM-OBJ-session-summary](memory.md#mem-obj-session-summary) and [EPI-OBJ-benchmark-notes](epistemic.md#epi-obj-benchmark-notes).

Requested semantic changes remain claimed. The packaged session procedure and separate-model background design each describe automatic session-fed durable writes with later consumers, so each supports claimed trace learning. They are distinct routes, not one wired scheduler. This classification neither establishes learning benefit nor settles whether a concrete inferred claim was novel or warranted. The post-write diagnostic checks links, not admission of knowledge. Template/path mismatches further limit successful delivery of the requested distillation. See [RT-RTE-distill-session](runtime.md#rt-rte-distill-session), [MEM-RTE-background-distill](memory.md#mem-rte-background-distill), [WF-RTE-distill-verification](workflow.md#wf-rte-distill-verification) and [RT-RTE-caller-mutation](runtime.md#rt-rte-caller-mutation).

Consolidation follows the specified reduction of session material to selected topic-based conclusions; it does not depend on proving that every resulting sentence is faithful. Deduplication and evolution follow their own requested merge/rewrite mechanisms. Inference markers alone do not establish synthesis of a claim absent from the inputs. Cache derivation and index rebuilding alone are not semantic curation. Trash invalidates ordinary search/listing reliance but leaves exact-path read capacity; it is not global access enforcement. The separate permanent-delete branch forgets the retained note through unlink and therefore supplies wired decay, independently of timed or scored decay policies. This resolved branch is included in the operation inventory even though other transformations remain unresolved. See [RT-RTE-distill-session](runtime.md#rt-rte-distill-session), [RT-RTE-tend-vault](runtime.md#rt-rte-tend-vault), [EPI-OBJ-vault-prose](epistemic.md#epi-obj-vault-prose), [MEM-OBJ-search-cache](memory.md#mem-obj-search-cache) and [MEM-OBJ-markdown-notes](memory.md#mem-obj-markdown-notes).

Knowledge, ranking and routing are separate effects. Retained note terms affect fixed lexical ranking even without a learned ranking policy. Templates and conventions afford guidance, while their delivery and interpretation by a host remain uncertain. Static skill instructions, executable create guards and result-score heuristics are not automatically retained-memory validation/enforcement criteria. Evaluation reports affect aggregation, not an inspected durable policy update. See [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval), [MEM-OBJ-note-templates](memory.md#mem-obj-note-templates), [MEM-OBJ-napkin](memory.md#mem-obj-napkin) and [EPI-RTE-score-report](epistemic.md#epi-rte-score-report).

Core read-back fulfills explicit requests. Bundling NAPKIN.md with requested overview does not create a second push. Its always-loaded host description supports only claimed broad/coarse push: external scheduling, identity matching and injection remain unresolved. Requested filenames and base/view selectors cannot establish identifier-based push, and lexical search cannot establish lexical push. The opaque alternative therefore keeps direction and signal coverage partial. See [RT-RTE-vault-retrieval](runtime.md#rt-rte-vault-retrieval), [MEM-RTE-structured-access](memory.md#mem-rte-structured-access), [MEM-OBJ-napkin](memory.md#mem-obj-napkin) and [MEM-RTE-background-distill](memory.md#mem-rte-background-distill).

Raw dialogue ingestion alone is not trace learning. Supplied summaries have unknown production; stored scores have no inspected successor-policy consumer. Those limits are not bounded absence records and cannot justify a system-wide no or inapplicable trace source. Known session-message origin does not turn timer triggers into event-stream inputs, nor prove that findings include original tool traces or trajectories. See [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer), [MEM-OBJ-session-summary](memory.md#mem-obj-session-summary), [MEM-OBJ-evaluation-results](memory.md#mem-obj-evaluation-results) and [MEM-RTE-background-distill](memory.md#mem-rte-background-distill).

Source-read log: none. Classification used only the supplied accepted members and reconciliation; no frozen source file was read and no new evidence was introduced. Missing initial admission/provenance, opaque index semantics, external cursor/injection and partly inspected query/rendering consumers remain local limits rather than being erased by stronger witnesses elsewhere.
