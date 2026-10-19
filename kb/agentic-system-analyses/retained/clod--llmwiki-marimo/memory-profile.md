---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Memory profile of llmwiki-marimo: local wiki files, lexical retrieval, control state, conversation-derived
  pages and recovery artifacts.'
run-id: AAS-2026-10-18-llmwiki-marimo-58054ccd9ae7-01
source-identity: https://github.com/Clod/llmwiki-marimo
reviewed-boundary: 0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7
memory-comparison:
  version: 2
  scope: Accumulated source/extracted text; wiki prose, collection/index metadata and retained warnings;
    dataset files; generated aliases and mutable workspace controls including configured prompt text;
    stored page diagnostics; caller-held history reused by later invocations; optional trace artifacts;
    Git/index recovery and frozen developer reference copies. Includes their known writes, transformations
    and later consumers plus locally unresolved initialization, maintenance and evaluator alternatives.
    Excludes shipped static prompts, unretained current-call results, external provider state/weights
    and independently unfrozen dependency implementations.
  axes:
    storage_substrate:
      assessment: known
      units:
      - scope: Source files/cache and extracted source rows/chunks
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-source-text
          note: Workspace sources and extraction cache are file-backed.
        - value: sqlite
          basis: wired
          records: *id001
          note: Source documents, pages and chunks persist in index.db.
        records: *id001
        note: Original files and indexed extraction are separate retained parts.
      - scope: Wiki pages, datasets and configuration controls
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id002
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-datasets
          - memory.md#mem-obj-aliases-generated
          note: Wiki prose, dataset rows and configuration/alias files persist on disk.
        records: *id002
        note: Markdown/TOML parts are retained files; transient dataset parsing does not add a database
          store.
      - scope: Search/reference state and stored verification
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records: &id003
          - memory.md#mem-obj-document-chunks
          - memory.md#mem-obj-page-verifications
          note: FTS/reference tables and verification tables persist in SQLite.
        records: *id003
        note: The indexed content, access metadata and diagnostic scores are SQLite state.
      - scope: Caller-held conversation and reduced later-turn messages
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id004
          - epistemic.md#epi-obj-chat-answer
          - runtime.md#rt-rte-preretrieval-chat
          - runtime.md#rt-rte-streaming-chat
          note: Caller-held text and its reduced model-facing view survive between invocations in application
            memory.
        records: *id004
        note: Later turns reuse application-held messages; cross-session persistence is not established.
      - scope: Trace inspection artifacts, history, snapshots and golden fixtures
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id005
          - memory.md#mem-obj-spans
          - memory.md#mem-obj-index-snapshots
          - epistemic.md#epi-rte-corpus-freeze
          note: JSONL/payloads and frozen source/wiki files persist on disk.
        - value: repo
          basis: wired
          records: *id005
          note: Git history retains page/config versions and commit identities.
        - value: sqlite
          basis: wired
          records: *id005
          note: Commit-associated index snapshots and golden database copies retain SQLite state.
        records: *id005
        note: The recorded persistence mechanisms are classified, not universal availability or lossless
          restoration.
      records:
      - memory.md#mem-obj-source-text
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-datasets
      - memory.md#mem-obj-aliases-generated
      - memory.md#mem-obj-document-chunks
      - memory.md#mem-obj-page-verifications
      - epistemic.md#epi-obj-chat-answer
      - runtime.md#rt-rte-preretrieval-chat
      - runtime.md#rt-rte-streaming-chat
      - memory.md#mem-obj-spans
      - memory.md#mem-obj-index-snapshots
      - epistemic.md#epi-rte-corpus-freeze
      note: The recorded inventory covers file-backed knowledge and controls, SQLite indexes/diagnostics,
        caller-held history, inspection artifacts and recovery/developer copies. External provider internals
        are excluded, not classified as accumulated memory.
    representational_form:
      assessment: known
      units:
      - scope: Source/wiki/dataset text, conversation text, verification excerpts, warnings and trace
          text payloads
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id006
          - memory.md#mem-obj-source-text
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-datasets
          - epistemic.md#epi-obj-chat-answer
          - memory.md#mem-obj-page-verifications
          - epistemic.md#epi-obj-lint-issues
          - memory.md#mem-obj-spans
          note: Prose, labels, messages, source excerpts and diagnostic descriptions supply interpreted
            meaning.
        records: *id006
        note: These parts reach models or humans as interpreted text.
      - scope: Metadata, structured dataset values, indexes, retained controls, diagnostics and recovery
          identities
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id007
          - memory.md#mem-obj-document-chunks
          - memory.md#mem-obj-datasets
          - memory.md#mem-obj-aliases-generated
          - memory.md#mem-obj-page-verifications
          - memory.md#mem-obj-spans
          - memory.md#mem-obj-index-snapshots
          - epistemic.md#epi-rte-corpus-freeze
          note: IDs, FTS terms, references, rows, aliases, thresholds, scores, hashes and snapshot identities
            have fixed program consumers.
        records: *id007
        note: Numerical cells/scores have localized identities and fixed comparisons; Markdown syntax
          and fields coexist with prose.
      records:
      - memory.md#mem-obj-source-text
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-datasets
      - epistemic.md#epi-obj-chat-answer
      - memory.md#mem-obj-page-verifications
      - epistemic.md#epi-obj-lint-issues
      - memory.md#mem-obj-spans
      - memory.md#mem-obj-document-chunks
      - memory.md#mem-obj-aliases-generated
      - memory.md#mem-obj-index-snapshots
      - epistemic.md#epi-rte-corpus-freeze
      note: Forms follow operative parts and consumers. Local numeric rows and probabilities are symbolic
        values, not parametric memory. Excluded inference weights are not added merely because models
        consume memory.
    lineage:
      assessment: partial
      units:
      - scope: Original source acquisition and extracted-text indexing
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id008
          - memory.md#mem-obj-source-text
          - runtime.md#rt-rte-document-ingest
          note: Operator-supplied documents enter the workspace as external content.
        - value: other-compiled
          basis: wired
          records: *id008
          note: Extraction/chunking builds queryable source representations.
        records: *id008
        note: External assertions enter through ingestion; extraction does not certify their truth.
      - scope: Generated/merged wiki, indexes, aliases, verification and retained maintenance notes
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id009
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-document-chunks
          - memory.md#mem-obj-aliases-generated
          - memory.md#mem-obj-page-verifications
          - runtime.md#rt-rte-document-ingest
          - memory.md#mem-rte-page-verification
          - epistemic.md#epi-obj-lint-issues
          note: Software/model transformations produce pages, indexes, alias mappings, scores and diagnostic
            notes.
        records: *id009
        note: The known subsequent transformations do not resolve initial content provenance or the semantic
          relation of every model output.
      - scope: Direct web content approval/editing and manual control edits
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id010
          - runtime.md#rt-rte-chat-save
          - runtime.md#rt-rte-wiki-maintenance
          - runtime.md#rt-rte-configure-grants
          note: Human-submitted page bodies and explicit settings/vocabulary edits provide retained content.
        records: *id010
        note: Explicit content edits and approvals are separate from job initiation.
      - scope: Conversation-derived wiki pages on software-admitted save paths
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id011
          - runtime.md#rt-rte-chat-save
          - memory.md#mem-obj-wiki-pages
          note: Chat-save extracts retained prose from recorded user/assistant turns.
        records: *id011
        note: Selected exchanges or the last response become a structured retained page; raw transcripts
          are not guaranteed to survive.
      - scope: Versioned recovery and frozen reference copies
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id012
          - memory.md#mem-obj-index-snapshots
          - epistemic.md#epi-rte-corpus-freeze
          note: Snapshot and fixture production copy/index previously accumulated state.
        records: *id012
        note: Copying/versioning preserves a known derivation path without proving original page authorship.
      - scope: Initial dataset authorship/replacement and pre-existing workspace content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-datasets
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-aliases-generated
        note: External provenance and admission history are not supplied; do not infer a human author
          or a trace origin from file format.
      - scope: Raw optional trace payload origins and evaluator-packet content beyond recorded paths
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-spans
        - epistemic.md#epi-rte-eval-packet
        note: Mixed captured inputs and uninspected packet internals do not establish complete lineage
          classifications.
      records:
      - memory.md#mem-obj-source-text
      - runtime.md#rt-rte-document-ingest
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-document-chunks
      - memory.md#mem-obj-aliases-generated
      - memory.md#mem-obj-page-verifications
      - memory.md#mem-rte-page-verification
      - epistemic.md#epi-obj-lint-issues
      - runtime.md#rt-rte-chat-save
      - runtime.md#rt-rte-wiki-maintenance
      - runtime.md#rt-rte-configure-grants
      - memory.md#mem-obj-index-snapshots
      - epistemic.md#epi-rte-corpus-freeze
      - memory.md#mem-obj-datasets
      - memory.md#mem-obj-spans
      - epistemic.md#epi-rte-eval-packet
      note: Known import, authoring, compilation and conversation extraction coexist with unresolved initial
        dataset/content provenance and unspecified semantic derivations.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Source/wiki/dataset prose and retained conversation at later model/human consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id013
          - memory.md#mem-obj-source-text
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-datasets
          - epistemic.md#epi-obj-chat-answer
          - runtime.md#rt-rte-preretrieval-chat
          - runtime.md#rt-rte-strict-chat
          - memory.md#mem-obj-spans
          note: Retained content supplies evidence, context or inspection material to later readers and
            models.
        records: *id013
        note: Inspection rendering is reference use; QA context is not an executable instruction.
      - scope: Existing page at update models and saved conversation at structuring models
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id014
          - runtime.md#rt-rte-document-ingest
          - runtime.md#rt-rte-chat-save
          - memory.md#mem-obj-wiki-pages
          note: Retained page/conversation content feeds durable behavior-shaping page revisions; this
            is update authority, not demonstrated capacity improvement.
        records: *id014
        note: Prior content shapes a durable page update, separately from its downstream evidence role.
      - scope: FTS content and dataset values at retrieval/projection ranking consumers
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id015
          - memory.md#mem-obj-document-chunks
          - runtime.md#rt-rte-preretrieval-chat
          - epistemic.md#epi-rte-finance-derive
          - memory.md#mem-obj-datasets
          note: Retained text determines FTS rank; retained rates/attributes affect gain ordering.
        records: *id015
        note: Fixed algorithms can rank using retained operands without learned ranking weights.
      - scope: Retained configured prompt at agent construction
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id016
          - memory.md#mem-obj-aliases-generated
          - runtime.md#rt-rte-configure-grants
          note: Configured prompt text supplies standing model directions.
        records: *id016
        note: Only the user-configured retained prompt part is included; shipped static templates are
          excluded.
      - scope: Aliases, fingerprints, blacklist/settings and dataset attributes at scope/grant selectors
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id017
          - memory.md#mem-obj-aliases-generated
          - runtime.md#rt-rte-configure-grants
          - epistemic.md#epi-rte-finance-select
          note: Aliases and fingerprint/config state select scope, regeneration and available operations.
        - value: enforcement
          basis: wired
          records: *id017
          note: Blacklist and dataset eligibility predicates can refuse generation or exclude inputs.
        - value: validation
          basis: wired
          records: *id017
          note: False-synonym/collision controls and retained typed attributes constrain accepted mappings
            or eligible calculation inputs.
        records: *id017
        note: Each effect is bounded to its inspected consumer.
      - scope: Verification scores/hashes and retained threshold at diagnostic consumers
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id018
          - memory.md#mem-obj-page-verifications
          - memory.md#mem-rte-page-verification
          - epistemic.md#epi-rte-verify-use
          note: Hashes and thresholds determine current diagnostic conformity and supported labels.
        - value: knowledge
          basis: wired
          records: *id018
          note: Sentence/excerpt summaries and labels inform human inspection.
        records: *id018
        note: These classify diagnostic reuse/support, not page truth or universal chat admissibility.
      - scope: Warning/TODO text and recovery state at maintenance/restore consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id019
          - epistemic.md#epi-obj-lint-issues
          - epistemic.md#epi-rte-gap-note
          - memory.md#mem-obj-index-snapshots
          - runtime.md#rt-rte-wiki-maintenance
          note: Retained warnings preserve criticism for later readers.
        - value: routing
          basis: wired
          records: *id019
          note: Gap markers and chosen revision/snapshot state select maintenance or restore actions.
        records: *id019
        note: Readable warnings remain advisory while markers and identities drive code decisions.
      - scope: Frozen golden fixtures at regression/evaluation consumers
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id020
          - epistemic.md#epi-rte-corpus-freeze
          note: Frozen source/wiki/database state supplies reference criteria to later development checks.
        records: *id020
        note: The reference baseline checks conformity, not universal factual truth.
      - scope: Remaining repair/evaluator consumption paths
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-wiki-maintenance
        - epistemic.md#epi-rte-eval-packet
        - runtime.md#rt-rte-model-evaluation
        note: Every repair, packet/rubric consumer and evaluation feedback path was not audited; no complete
          authority union follows.
      records:
      - memory.md#mem-obj-source-text
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-datasets
      - epistemic.md#epi-obj-chat-answer
      - runtime.md#rt-rte-preretrieval-chat
      - runtime.md#rt-rte-strict-chat
      - memory.md#mem-obj-spans
      - runtime.md#rt-rte-document-ingest
      - runtime.md#rt-rte-chat-save
      - memory.md#mem-obj-document-chunks
      - epistemic.md#epi-rte-finance-derive
      - memory.md#mem-obj-aliases-generated
      - runtime.md#rt-rte-configure-grants
      - epistemic.md#epi-rte-finance-select
      - memory.md#mem-obj-page-verifications
      - memory.md#mem-rte-page-verification
      - epistemic.md#epi-rte-verify-use
      - epistemic.md#epi-obj-lint-issues
      - epistemic.md#epi-rte-gap-note
      - memory.md#mem-obj-index-snapshots
      - runtime.md#rt-rte-wiki-maintenance
      - epistemic.md#epi-rte-corpus-freeze
      - epistemic.md#epi-rte-eval-packet
      - runtime.md#rt-rte-model-evaluation
      note: Authority is consumer-relative. The supported forces below do not establish beneficial activation;
        uninspected maintenance/evaluator consumers prevent a complete inventory.
    write_agency:
      assessment: partial
      units:
      - scope: Ingestion, aliases, diagnostics, repair mutations and trace recording
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id021
          - runtime.md#rt-rte-document-ingest
          - memory.md#mem-obj-aliases-generated
          - memory.md#mem-rte-page-verification
          - runtime.md#rt-rte-wiki-maintenance
          - memory.md#mem-obj-spans
          note: Pipeline/model outputs, validated aliases, stored scores, notes and enabled trace records
            are admitted by software.
        records: *id021
        note: A user may start the job; code admits the resulting retained content without per-content
          approval.
      - scope: Web submitted content, manual page/control edits and requested historical replacement
        assessment: known
        findings:
        - value: manual
          basis: wired
          records: &id022
          - runtime.md#rt-rte-chat-save
          - runtime.md#rt-rte-wiki-maintenance
          - runtime.md#rt-rte-configure-grants
          - memory.md#mem-obj-index-snapshots
          note: Web submit approves/edits Markdown; direct edits and chosen restore revision explicitly
            select retained content.
        records: *id022
        note: The explicit human decision supplies or replaces the retained content at these mechanisms.
      - scope: Marimo/convenience generated page admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id023
          - runtime.md#rt-rte-chat-save
          note: Drafting proceeds directly to write without an intervening content approval.
        records: *id023
        note: Starting save does not make the subsequently generated draft human-approved.
      - scope: Golden fixture replacement
        assessment: known
        findings:
        - value: manual
          basis: wired
          records: &id024
          - epistemic.md#epi-rte-corpus-freeze
          note: Freeze is a deliberate operator-selected baseline replacement, not automatic model admission.
        records: *id024
        note: The operator explicitly chooses the staging snapshot for replacement; code performs the
          copy.
      - scope: Initial/external dataset replacement and pre-existing workspace initialization
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-datasets
        - memory.md#mem-obj-wiki-pages
        note: Generic workspace/file origin does not establish who decided the retained content.
      - scope: Remaining unaudited repair/evaluation artifact admissions
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-wiki-maintenance
        - epistemic.md#epi-rte-eval-packet
        note: Known automatic transformations do not resolve all uninspected mutation paths.
      records:
      - runtime.md#rt-rte-document-ingest
      - memory.md#mem-obj-aliases-generated
      - memory.md#mem-rte-page-verification
      - runtime.md#rt-rte-wiki-maintenance
      - memory.md#mem-obj-spans
      - runtime.md#rt-rte-chat-save
      - runtime.md#rt-rte-configure-grants
      - memory.md#mem-obj-index-snapshots
      - epistemic.md#epi-rte-corpus-freeze
      - memory.md#mem-obj-datasets
      - memory.md#mem-obj-wiki-pages
      - epistemic.md#epi-rte-eval-packet
      note: Human content control and software admission both exist. Initial dataset/workspace admission
        and unaudited mutation paths remain unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Summary extraction and accumulation of concept/overview pages
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id025
          - runtime.md#rt-rte-document-ingest
          - memory.md#mem-obj-wiki-pages
          note: Summaries and merged existing content reduce/combine retained source claims.
        - value: evolve
          basis: wired
          records: *id025
          note: Existing concepts and overview are revised as new material arrives.
        records: *id025
        note: Summary/reuse mechanisms reduce and revise accumulated content; exact semantic preservation
          remains unproved.
      - scope: Conversation view and chat-to-page structuring
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id026
          - runtime.md#rt-rte-preretrieval-chat
          - runtime.md#rt-rte-chat-save
          - epistemic.md#epi-obj-chat-answer
          note: Table compaction and conversation structuring reduce retained text into a later-consumed
            representation.
        - value: decay
          basis: wired
          records: *id026
          note: Refused exchanges and old turns are removed from later model-visible history.
        - value: evolve
          basis: wired
          records: *id026
          note: Same-slug chat structuring updates existing page content.
        records: *id026
        note: Reduced history reaches later invocations; software save retains structured conversation-derived
          pages.
      - scope: Verification freshness and source-dependent withdrawal
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records: &id027
          - memory.md#mem-rte-page-verification
          - memory.md#mem-rte-source-withdrawal
          - memory.md#mem-obj-page-verifications
          note: Hash changes/page writes invalidate stored diagnostics; source withdrawal marks surviving
            dependent pages stale.
        records: *id027
        note: 'Invalidation is local: stale page prose can remain searchable, and old diagnostics lose
          current reliance.'
      - scope: Retained reminders and manual/automatic page revision
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id028
          - epistemic.md#epi-rte-gap-note
          - runtime.md#rt-rte-wiki-maintenance
          note: Maintenance and direct editing revise retained page/reminder content.
        records: *id028
        note: Replacing a TODO with a related link changes an existing retained entry, without proving
          semantic gap resolution.
      - scope: Semantic novelty of model page/alias/diagnostic outputs
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-document-ingest
        - runtime.md#rt-rte-chat-save
        - epistemic.md#epi-obj-lint-issues
        - memory.md#mem-obj-aliases-generated
        note: No input/output content evidence settles newly synthesized claims; generation is not by
          itself synthesis.
      - scope: Other repair transformations and recovery/evaluator internals
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-wiki-maintenance
        - memory.md#mem-obj-index-snapshots
        - epistemic.md#epi-rte-eval-packet
        note: Index rebuilding alone establishes no curation operation; remaining algorithm coverage is
          incomplete.
      records:
      - runtime.md#rt-rte-document-ingest
      - memory.md#mem-obj-wiki-pages
      - runtime.md#rt-rte-preretrieval-chat
      - runtime.md#rt-rte-chat-save
      - epistemic.md#epi-obj-chat-answer
      - memory.md#mem-rte-page-verification
      - memory.md#mem-rte-source-withdrawal
      - memory.md#mem-obj-page-verifications
      - epistemic.md#epi-rte-gap-note
      - runtime.md#rt-rte-wiki-maintenance
      - epistemic.md#epi-obj-lint-issues
      - memory.md#mem-obj-aliases-generated
      - memory.md#mem-obj-index-snapshots
      - epistemic.md#epi-rte-eval-packet
      note: Recorded reduction, revision, withdrawal and forgetting are supported locally. Semantic indeterminacy
        and unaudited repair algorithms prevent complete classification; no synthesis is inferred solely
        from generated prose.
    read_back_direction:
      assessment: partial
      units:
      - scope: Model-requested page/search/data tools and operator inspection/restore
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id029
          - runtime.md#rt-rte-strict-chat
          - runtime.md#rt-rte-streaming-chat
          - memory.md#mem-obj-datasets
          - memory.md#mem-obj-spans
          - memory.md#mem-obj-index-snapshots
          - runtime.md#rt-rte-wiki-maintenance
          note: Explicit tool reads, trace rendering and selected historical restoration fulfill consumer
            requests.
        records: *id029
        note: Requested material returns are pull; mere code delivery is not another push.
      - scope: Pre-retrieval evidence and shaped history delivery to answer/condenser models
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id030
          - runtime.md#rt-rte-preretrieval-chat
          - epistemic.md#epi-obj-chat-answer
          - memory.md#mem-obj-datasets
          note: Question/roster/open-page/collection selectors and history shaping supply context automatically.
        records: *id030
        note: Code selects retained material before the answer invocation, rather than waiting for its
          retrieval request.
      - scope: Same-slug existing-page input and retained configuration at later invocations
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id031
          - runtime.md#rt-rte-document-ingest
          - runtime.md#rt-rte-chat-save
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-aliases-generated
          - runtime.md#rt-rte-configure-grants
          note: Existing page and accumulated controls are automatically supplied to update/generation
            or scope consumers.
        records: *id031
        note: Code selects earlier retained content for generation or config consumers.
      - scope: Stored diagnostic and frozen fixture reads
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id032
          - memory.md#mem-rte-page-verification
          - memory.md#mem-obj-page-verifications
          - epistemic.md#epi-rte-corpus-freeze
          note: Requested page diagnostics and developer fixture reads obtain retained state.
        records: *id032
        note: Page/lint callers load diagnostic state; development callers load a chosen reference baseline.
      - scope: Other repair, evaluation packet and feedback read paths
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-wiki-maintenance
        - epistemic.md#epi-rte-eval-packet
        - runtime.md#rt-rte-model-evaluation
        note: Detailed consumers are not completely inspected; no pull-only boundary or complete union
          is asserted.
      records:
      - runtime.md#rt-rte-strict-chat
      - runtime.md#rt-rte-streaming-chat
      - memory.md#mem-obj-datasets
      - memory.md#mem-obj-spans
      - memory.md#mem-obj-index-snapshots
      - runtime.md#rt-rte-wiki-maintenance
      - runtime.md#rt-rte-preretrieval-chat
      - epistemic.md#epi-obj-chat-answer
      - runtime.md#rt-rte-document-ingest
      - runtime.md#rt-rte-chat-save
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-aliases-generated
      - runtime.md#rt-rte-configure-grants
      - memory.md#mem-rte-page-verification
      - memory.md#mem-obj-page-verifications
      - epistemic.md#epi-rte-corpus-freeze
      - epistemic.md#epi-rte-eval-packet
      - runtime.md#rt-rte-model-evaluation
      note: Requested reads and automatic context selection both exist within chains. The request for
        an answer is not a request for each selected retained part; code selection is a distinct push
        operation. Remaining maintenance/evaluator internals prevent complete direction coverage.
    read_back_signal:
      assessment: partial
      units:
      - scope: Pre-retrieval wiki/source/dataset selection
        assessment: known
        findings:
        - value: inferred-lexical
          basis: wired
          records: &id033
          - runtime.md#rt-rte-preretrieval-chat
          - memory.md#mem-obj-document-chunks
          - memory.md#mem-obj-datasets
          - memory.md#mem-obj-aliases-generated
          note: FTS terms and lexical roster/key matching select retained evidence.
        - value: identifier
          basis: wired
          records: *id033
          note: Open-page identity selects that page body and named dataset keys select corresponding
            rows.
        - value: coarse
          basis: wired
          records: *id033
          note: Collection intent supplies whole overview/index bodies and count limits bound returned
            chunks.
        records: *id033
        note: 'Trigger: requested QA turn. Inputs: question or accepted rewrite, aliases/roster, open-page
          identity and collection intent. Selected parts: chunks, page bodies, dataset rows or key names.'
      - scope: Later-turn history and configured-context delivery
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id034
          - runtime.md#rt-rte-preretrieval-chat
          - epistemic.md#epi-obj-chat-answer
          - runtime.md#rt-rte-configure-grants
          - memory.md#mem-obj-aliases-generated
          note: Availability, exclusion rules and a fixed recent-message budget select history/configured
            context.
        records: *id034
        note: 'Trigger: later model/agent invocation. Inputs: available history, refusal/table predicates,
          tail count and loaded workspace settings. Parts: filtered recent text and configured guidance.'
      - scope: Existing-page selection for ingestion and chat structuring
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id035
          - runtime.md#rt-rte-document-ingest
          - runtime.md#rt-rte-chat-save
          - memory.md#mem-obj-wiki-pages
          note: Slug identity selects the prior page delivered to an update model.
        records: *id035
        note: 'Trigger: concept update or same-title draft. Input: generated/selected slug. Part: matching
          existing page body.'
      - scope: Condenser-mediated pre-retrieval choice
        assessment: known
        findings:
        - value: inferred-judgment
          basis: wired
          records: &id036
          - runtime.md#rt-rte-preretrieval-chat
          note: A model interprets retained conversational context into a rewrite that influences downstream
            evidence selection; lexical gates still determine delivery.
        records: *id036
        note: 'Trigger: uncovered follow-up with history. Input: history and question. Part: retained
          evidence selected after a model rewrite is rechecked.'
      - scope: Remaining maintenance/evaluator automatic selection
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-wiki-maintenance
        - epistemic.md#epi-rte-eval-packet
        note: Incomplete selector inspection prevents a complete signal inventory; pull file identifiers
          alone do not supply a push signal.
      records:
      - runtime.md#rt-rte-preretrieval-chat
      - memory.md#mem-obj-document-chunks
      - memory.md#mem-obj-datasets
      - memory.md#mem-obj-aliases-generated
      - epistemic.md#epi-obj-chat-answer
      - runtime.md#rt-rte-configure-grants
      - runtime.md#rt-rte-document-ingest
      - runtime.md#rt-rte-chat-save
      - memory.md#mem-obj-wiki-pages
      - runtime.md#rt-rte-wiki-maintenance
      - epistemic.md#epi-rte-eval-packet
      note: Signals describe push selectors, not identifiers merely carried by requested files. Coarse
        and targeted selection remain distinct; unresolved paths are not made inapplicable by known pulls.
    trace_learning:
      assessment: partial
      units:
      - scope: Marimo/convenience conversation-to-wiki admission
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id037
          - runtime.md#rt-rte-chat-save
          - memory.md#mem-obj-wiki-pages
          note: Software admission produces retained behavior-shaping prose from conversation traces,
            without requiring observed benefit.
        records: *id037
        note: Recorded conversational turns feed automatic structuring/write and the resulting durable
          page enters later retrieval or merge.
      - scope: Human-reviewed web admission and direct human edits
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-chat-save
        - runtime.md#rt-rte-wiki-maintenance
        note: Human content approval is established here, not an automatic trace-fed admission; no evidenced-absence
          record closes all alternatives.
      - scope: History reduction and condenser rewrite
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-preretrieval-chat
        - epistemic.md#epi-obj-chat-answer
        note: Later-invocation context reuse is established, but no durable conversation-summary checkpoint
          is recorded; this does not support a qualifying positive or bounded negative.
      - scope: Source ingestion, datasets, aliases and diagnostics/repair
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-source-text
        - memory.md#mem-obj-datasets
        - memory.md#mem-obj-aliases-generated
        - memory.md#mem-rte-page-verification
        - epistemic.md#epi-obj-lint-issues
        - runtime.md#rt-rte-document-ingest
        note: Ordinary source content is not automatically a trace. Its complete origin and all repair/update
          alternatives are not established as trace-fed or bounded absent.
      - scope: Raw spans, evaluator outputs, snapshots and frozen fixtures
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-spans
        - epistemic.md#epi-rte-eval-packet
        - runtime.md#rt-rte-model-evaluation
        - memory.md#mem-obj-index-snapshots
        - epistemic.md#epi-rte-corpus-freeze
        note: Raw retention/recovery/reference use alone is not a qualifying automatic durable behavior
          update. Uninspected feedback and evaluator internals prevent an absence conclusion.
      records:
      - runtime.md#rt-rte-chat-save
      - memory.md#mem-obj-wiki-pages
      - runtime.md#rt-rte-wiki-maintenance
      - runtime.md#rt-rte-preretrieval-chat
      - epistemic.md#epi-obj-chat-answer
      - memory.md#mem-obj-source-text
      - memory.md#mem-obj-datasets
      - memory.md#mem-obj-aliases-generated
      - memory.md#mem-rte-page-verification
      - epistemic.md#epi-obj-lint-issues
      - runtime.md#rt-rte-document-ingest
      - memory.md#mem-obj-spans
      - epistemic.md#epi-rte-eval-packet
      - runtime.md#rt-rte-model-evaluation
      - memory.md#mem-obj-index-snapshots
      - epistemic.md#epi-rte-corpus-freeze
      note: Software-admitted chat-to-page writes establish a qualifying trace-fed durable artifact and
        later consumer. Other included routes do not have bounded absence records; no local or system-wide
        no is asserted.
    trace_source:
      assessment: partial
      units:
      - scope: Automatic conversation-to-wiki write
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id038
          - runtime.md#rt-rte-chat-save
          - memory.md#mem-obj-wiki-pages
          note: Recorded user/assistant conversational turns feed the software-admitted durable page.
        records: *id038
        note: Original inputs are selected question/answer exchanges or the last assistant response; tool
          transcripts are not the saved conversation representation.
      - scope: Other possible trace-fed writes across included source, repair, history and evaluation
          paths
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-source-text
        - memory.md#mem-obj-datasets
        - memory.md#mem-obj-aliases-generated
        - runtime.md#rt-rte-preretrieval-chat
        - epistemic.md#epi-obj-lint-issues
        - memory.md#mem-obj-spans
        - epistemic.md#epi-rte-eval-packet
        - epistemic.md#epi-rte-corpus-freeze
        note: A qualifying write and its complete original trace content are not established for these
          alternatives. No bounded complete absence permits inapplicability.
      records:
      - runtime.md#rt-rte-chat-save
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-source-text
      - memory.md#mem-obj-datasets
      - memory.md#mem-obj-aliases-generated
      - runtime.md#rt-rte-preretrieval-chat
      - epistemic.md#epi-obj-lint-issues
      - memory.md#mem-obj-spans
      - epistemic.md#epi-rte-eval-packet
      - epistemic.md#epi-rte-corpus-freeze
      note: Session logs establish the source of the known qualifying chat-save route. Other potential
        qualifying routes remain unresolved; neither tool traces nor event streams follow from trace-file
        names or serialization.
---

# llmwiki-marimo memory profile

## Comparison rationale

This profile classifies accepted records, not fresh source inspection. All positive findings are implementation-level wiring. No observed execution, activation benefit or causal improvement is claimed. Known coverage of storage and form concerns the recorded retained-part inventory, not every internal algorithm or deployment artifact. Other axes retain missing provenance and unaudited alternatives rather than extending one inspected witness to all routes.

### Admission, authority and trace learning

The normal web save has a human content decision; marimo and convenience saves admit subsequently structured prose automatically. These are separate write mechanisms in [RT-RTE-chat-save](runtime.md#rt-rte-chat-save). Starting the latter save is not approval of its generated content. A conversation-derived durable page supports trace learning at this wired route, even though factual acceptance and improved future capacity remain unestablished. Its original input is conversational turns, not the answer agent's full tool transcript. The downstream page supplies knowledge to QA; at the structuring/update consumer the retained input shapes a durable artifact. These effects have separate authority findings.

[MEM-OBJ-aliases-generated](memory.md#mem-obj-aliases-generated) separates optional configured instructions from symbolic scope controls. Retained operands can supply ranking or validation authority without a learned ranking policy or epistemic truth acceptance. [MEM-OBJ-page-verifications](memory.md#mem-obj-page-verifications) supplies probabilities, hashes and short excerpts to later diagnostic consumers; it does not establish ordinary chat injection or a universal admission veto. Source withdrawal marks some pages stale but leaves them searchable, as [MEM-RTE-source-withdrawal](memory.md#mem-rte-source-withdrawal) records.

### Selection and transformation

The requested QA chain contains automatic pre-selection before the answer model and, alternatively, model-requested tools. These establish push and pull respectively, not two directions for every individual delivery. [RT-RTE-preretrieval-chat](runtime.md#rt-rte-preretrieval-chat) supplies the selectors, open-page/collection alternatives, dataset augmentation and history budgets. A model rewrite contributes inferred judgment without upgrading the later lexical selector into embedding search. Full-page tool requests are pull; their path identifiers do not independently establish identifier-based push.

Consolidation describes the implemented reduction/combination mechanisms, not a guarantee of faithful preservation. Existing-page revision establishes evolution. Neither fluent generated prose nor the absence of a proof of entailment establishes synthesis. [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest) and [RT-RTE-chat-save](runtime.md#rt-rte-chat-save) retain that semantic uncertainty. Index rebuilding is not by itself consolidation, and idempotent warning markers are not by themselves deduplication of retained claims. History forgetting concerns the later model-visible view, not deletion of full caller-held UI text.

### Coverage and canonical identity

The reconciliation supersedes EPI-OBJ-dataset-rows with [MEM-OBJ-datasets](memory.md#mem-obj-datasets). Dataset findings therefore use the latter canonical destination, including where finance consumers are cited. Other overlapping objects and maintenance parts remain valid containers or distinct consumers, not supersessions. No other supersession changes a value here.

Initial dataset authorship, complete model-output derivation, every repair/evaluator path and cross-session conversation persistence are not supplied as settled facts. The unresolved units preserve those limits. No analyst declares an evidenced-absence record, so unestablished feedback or durable-summary routes do not become trace-learning negatives. The supported local yes yields an existence finding, not complete trace-learning/source coverage. Likewise there is no complete-value claim for partial authority, curation or selection inventories.

### Source-read log

No source files were read or searched. The supplied accepted members and reconciliation were the only evidence inputs; no new records, quotations or evidence were added.
