---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: Sparks memory comparison of accumulated vault files, generated collections and manifest-mediated
  later consumption.
run-id: AAS-2026-10-15-sparks-563865f8b26f-01
source-identity: https://github.com/YogiRK/sparks
reviewed-boundary: 49abddc848ea55f78518bfbbbe04c3d37a5f2705
memory-comparison:
  version: 2
  scope: Accumulated inbox/raw/archive files; wiki bodies and Revision text; operation log; live Tasks;
    index descriptions/catalog; all seven regenerated collections; SQLite file/frontmatter/link projections
    and ingest history; optional Git history; their write, maintenance and later-consumer routes. Excludes
    shipped static contract/instruction copies, product builds, external harness conversation/checkpoints
    and provider/model state. Unknown initial content and generic caller/direct-edit admission remain
    included limitations, not excluded alternatives.
  axes:
    storage_substrate:
      assessment: known
      units:
      - scope: Raw capture/archive, wiki bodies and revisions, log, Tasks, index descriptions/catalog
          and seven regenerated collections
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-raw
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-log
          - memory.md#mem-obj-tasks
          - memory.md#mem-obj-index
          - memory.md#mem-obj-collections
          - memory.md#mem-rte-collection-regeneration
          note: Retained payloads are ordinary Markdown files; deterministic writes and later file reads
            establish the substrate, not successful semantic authorship.
        records:
        - memory.md#mem-obj-raw
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-log
        - memory.md#mem-obj-tasks
        - memory.md#mem-obj-index
        - memory.md#mem-obj-collections
        - memory.md#mem-rte-collection-regeneration
        note: The retained file inventory distinguishes live Tasks from the seven generated collections
          and prose from manifest projections.
      - scope: Manifest file/frontmatter/link projections and ingest lifecycle rows
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-manifest-projections
          - runtime.md#rt-obj-ingests
          - runtime.md#rt-rte-ingest-cycle
          - runtime.md#rt-rte-maintenance-write
          note: The vault SQLite database persists lookup state and ingest history for later deterministic
            consumers.
        records:
        - memory.md#mem-obj-manifest-projections
        - runtime.md#rt-obj-ingests
        - runtime.md#rt-rte-ingest-cycle
        - runtime.md#rt-rte-maintenance-write
        note: Includes both symbolic access projections and the separately declared session-state rows.
      - scope: Optional Git history of accumulated vault files
        assessment: known
        findings:
        - value: repo
          basis: wired
          records:
          - runtime.md#rt-rte-ingest-cycle
          - runtime.md#rt-rte-maintenance-write
          note: Finalize optionally commits the dirty vault tree through system Git; retained file versions
            are repository-backed when that branch is used.
        records:
        - runtime.md#rt-rte-ingest-cycle
        - runtime.md#rt-rte-maintenance-write
        note: Git is optional and not a semantic acceptance store; filesystem and SQLite storage remain
          operative without a commit.
      records:
      - memory.md#mem-obj-raw
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-log
      - memory.md#mem-obj-tasks
      - memory.md#mem-obj-index
      - memory.md#mem-obj-collections
      - memory.md#mem-rte-collection-regeneration
      - memory.md#mem-obj-manifest-projections
      - runtime.md#rt-obj-ingests
      - runtime.md#rt-rte-ingest-cycle
      - runtime.md#rt-rte-maintenance-write
      note: The accepted object inventory covers retained files, SQLite access/session state and optional
        Git history. Static shipped instructions, build products and excluded provider/harness state are
        not accumulated vault memory.
    representational_form:
      assessment: known
      units:
      - scope: Raw prose, wiki bodies/Revision reasons, operation log text, task text, index descriptions
          and generated collection text at human/agent readers
        assessment: known
        findings:
        - value: natural-language
          basis: afforded
          records:
          - memory.md#mem-obj-raw
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-log
          - memory.md#mem-obj-tasks
          - memory.md#mem-obj-index
          - memory.md#mem-obj-collections
          - runtime.md#rt-rte-vault-consume
          note: Prose supplies meaning through human or external-agent interpretation; later answering-agent
            body reads are prescribed, not observed.
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-raw
          - memory.md#mem-obj-log
          - memory.md#mem-obj-tasks
          - memory.md#mem-obj-collections
          - runtime.md#rt-rte-vault-consume
          note: Viewer body reads and Brief delivery of selected log/task text are implemented delivery
            paths for retained natural-language content.
        records:
        - memory.md#mem-obj-raw
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-log
        - memory.md#mem-obj-tasks
        - memory.md#mem-obj-index
        - memory.md#mem-obj-collections
        - runtime.md#rt-rte-vault-consume
        note: Natural-language force is distinct from structural parsing. Delivery does not prove a model
          used or obeyed the text.
      - scope: Raw capture dates/hints/paths, wiki frontmatter and link catalogs, task headings/checkboxes
          and log dates at fixed parsers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-raw
          - memory.md#mem-obj-manifest-projections
          - memory.md#mem-obj-tasks
          - memory.md#mem-obj-log
          - memory.md#mem-obj-index
          - memory.md#mem-obj-collections
          - runtime.md#rt-rte-maintenance-write
          - runtime.md#rt-rte-vault-consume
          note: Localized dates, identifiers, markers and fields have fixed Go/SQL interpretation, separate
            from the prose they organize.
        records:
        - memory.md#mem-obj-raw
        - memory.md#mem-obj-manifest-projections
        - memory.md#mem-obj-tasks
        - memory.md#mem-obj-log
        - memory.md#mem-obj-index
        - memory.md#mem-obj-collections
        - runtime.md#rt-rte-maintenance-write
        - runtime.md#rt-rte-vault-consume
        note: Includes mixed file parts rather than treating all Markdown as natural language.
      - scope: Manifest projections and ingest lifecycle state at SQL/Go consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-manifest-projections
          - runtime.md#rt-obj-ingests
          - memory.md#mem-rte-affected-selection
          - runtime.md#rt-rte-ingest-cycle
          note: Hashes, timestamps, statuses, title/alias/tag fields and resolved edges control fixed
            lookup and lifecycle rules.
        records:
        - memory.md#mem-obj-manifest-projections
        - runtime.md#rt-obj-ingests
        - memory.md#mem-rte-affected-selection
        - runtime.md#rt-rte-ingest-cycle
        note: Provider parameters are excluded external dependencies, not an opaque retained vault payload
          to classify.
      records:
      - memory.md#mem-obj-raw
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-log
      - memory.md#mem-obj-tasks
      - memory.md#mem-obj-index
      - memory.md#mem-obj-collections
      - runtime.md#rt-rte-vault-consume
      - memory.md#mem-obj-manifest-projections
      - runtime.md#rt-rte-maintenance-write
      - runtime.md#rt-obj-ingests
      - memory.md#mem-rte-affected-selection
      - runtime.md#rt-rte-ingest-cycle
      note: All included retained operative parts have prose or fixed-rule structural consumption paths.
        External model computation is not the accumulated-memory boundary.
    lineage:
      assessment: partial
      units:
      - scope: Human-supplied inbox and raw sources before archive
        assessment: partial
        findings:
        - value: authored
          basis: claimed
          records:
          - memory.md#mem-obj-raw
          note: The contract assigns inbox capture to the human; this supports authored capture as doctrine,
            not an authenticated instance.
        - value: imported
          basis: claimed
          records:
          - memory.md#mem-obj-raw
          - runtime.md#rt-rte-ingest-cycle
          note: Human-added source files and captured source material enter the vault from outside; their
            original authorship and trust are not authenticated.
        records:
        - memory.md#mem-obj-raw
        - runtime.md#rt-rte-ingest-cycle
        note: Capture and source import are included, but actual initial payload provenance is unavailable;
          cannot exhaustively classify every raw item.
      - scope: Deterministic raw archive and manifest/session access-state derivation
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-raw
          - memory.md#mem-obj-manifest-projections
          - runtime.md#rt-obj-ingests
          - runtime.md#rt-rte-ingest-cycle
          - runtime.md#rt-rte-maintenance-write
          note: Archive copies/date-groups retained captures; scan compiles file/frontmatter/link state
            and lifecycle code records session state.
        records:
        - memory.md#mem-obj-raw
        - memory.md#mem-obj-manifest-projections
        - runtime.md#rt-obj-ingests
        - runtime.md#rt-rte-ingest-cycle
        - runtime.md#rt-rte-maintenance-write
        note: Compilation does not establish model-trace extraction or source warrant.
      - scope: External-agent wiki bodies, revisions, operation summaries and initial index entries
        assessment: partial
        findings:
        - value: authored
          basis: claimed
          records:
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-log
          - memory.md#mem-obj-index
          - epistemic.md#epi-rte-semantic-revision
          note: The semantic agent is instructed to directly write derived prose, log summaries and index
            entries.
        records:
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-log
        - memory.md#mem-obj-index
        - epistemic.md#epi-rte-semantic-revision
        note: Actual writing episodes and semantic derivations are unavailable. Log summaries are requested
          authored records, not established trace-extracted lessons; initial content provenance cannot
          be completed.
      - scope: Seven collection outputs and regenerated index links/descriptions
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-collections
          - memory.md#mem-obj-index
          - memory.md#mem-rte-collection-regeneration
          - runtime.md#rt-rte-maintenance-write
          note: Fixed extractors compile selected raw/archive/manifest parts; Index rebuilds links while
            retaining matched old description text.
        records:
        - memory.md#mem-obj-collections
        - memory.md#mem-obj-index
        - memory.md#mem-rte-collection-regeneration
        - runtime.md#rt-rte-maintenance-write
        note: The transformation path is known, but preserved descriptions and initial source payload
          provenance are unresolved. A compiled output does not settle its upstream origin.
      - scope: Live Tasks caller-provided text and later marker edits
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-tasks
          - runtime.md#rt-rte-maintenance-write
          note: TasksAdd deterministically appends supplied text and TaskDone changes selected open markers.
        - value: authored
          basis: claimed
          records:
          - memory.md#mem-obj-tasks
          - epistemic.md#epi-rte-semantic-revision
          note: The agent protocol requests task writing from captures and project assignments.
        records:
        - memory.md#mem-obj-tasks
        - runtime.md#rt-rte-maintenance-write
        - epistemic.md#epi-rte-semantic-revision
        note: Generic caller identity and unavailable direct edits do not resolve the initial task-text
          origin; subsequent fixed transformations remain supported.
      records:
      - memory.md#mem-obj-raw
      - runtime.md#rt-rte-ingest-cycle
      - memory.md#mem-obj-manifest-projections
      - runtime.md#rt-obj-ingests
      - runtime.md#rt-rte-maintenance-write
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-log
      - memory.md#mem-obj-index
      - epistemic.md#epi-rte-semantic-revision
      - memory.md#mem-obj-collections
      - memory.md#mem-rte-collection-regeneration
      - memory.md#mem-obj-tasks
      note: Known subsequent compilation and requested authorship coexist with missing initial-content
        and actual agent derivation provenance. No accepted record establishes trace-extracted lineage
        for these payloads.
    behavioral_authority:
      assessment: known
      units:
      - scope: Retained raw/wiki/Revision/log/task/collection prose and index descriptions at readers
          or answering/briefing agents
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-obj-raw
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-index
          - memory.md#mem-obj-collections
          - runtime.md#rt-rte-vault-consume
          - epistemic.md#epi-rte-semantic-revision
          note: File readers and the prescribed answering agent receive reference/context, including Revision
            reasons only through full-body reading.
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-log
          - memory.md#mem-obj-tasks
          - runtime.md#rt-rte-vault-consume
          note: Brief forwards selected retained operation-log blocks and task text; viewer renders requested
            bodies for reference.
        records:
        - memory.md#mem-obj-raw
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-log
        - memory.md#mem-obj-tasks
        - memory.md#mem-obj-index
        - memory.md#mem-obj-collections
        - runtime.md#rt-rte-vault-consume
        - epistemic.md#epi-rte-semantic-revision
        note: These routes supply context/advice, not standing harness instructions; actual compliance
          or answer dependence is unobserved.
      - scope: Manifest fields/edges and ingest history at Query, index, Projects, affected and viewer
          navigation selectors
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-manifest-projections
          - runtime.md#rt-obj-ingests
          - memory.md#mem-rte-affected-selection
          - runtime.md#rt-rte-vault-consume
          - runtime.md#rt-rte-maintenance-write
          note: Retained fields/edges select page catalogs, groups, navigation and affected-maintenance
            suggestions; completed-ingest time selects the changed-path window.
        records:
        - memory.md#mem-obj-manifest-projections
        - runtime.md#rt-obj-ingests
        - memory.md#mem-rte-affected-selection
        - runtime.md#rt-rte-vault-consume
        - runtime.md#rt-rte-maintenance-write
        note: Metadata has fixed selection force even when no source body is loaded. Advisory affected
          names do not automatically execute regeneration.
      - scope: Retained open/done task markers at TaskDone and Brief
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-tasks
          - runtime.md#rt-rte-maintenance-write
          - runtime.md#rt-rte-vault-consume
          note: Checkbox state selects open candidates and future task previews.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-tasks
          - runtime.md#rt-rte-maintenance-write
          - runtime.md#rt-rte-vault-consume
          note: Completed markers exclude tasks from later open-candidate sets and Brief previews.
        records:
        - memory.md#mem-obj-tasks
        - runtime.md#rt-rte-maintenance-write
        - runtime.md#rt-rte-vault-consume
        note: The exclusion concerns delivery/selection, not enforcement of task execution or real-world
          success.
      - scope: Retained task text at fuzzy target matching
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-tasks
          - runtime.md#rt-rte-maintenance-write
          note: Task text influences relative fuzzy-match scores; a sole or sufficiently separated winner
            can be selected.
        records:
        - memory.md#mem-obj-tasks
        - runtime.md#rt-rte-maintenance-write
        note: Fixed scoring establishes ranking input authority without retained learned ranking policy.
      - scope: Retained ingest active state at prepare/finalize admission
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - runtime.md#rt-obj-ingests
          - runtime.md#rt-rte-ingest-cycle
          note: Active-row state is a criterion for admitting prepare/finalize transitions.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-obj-ingests
          - runtime.md#rt-rte-ingest-cycle
          note: Existing active state blocks a new sequential prepare; missing active state rejects finalize.
        records:
        - runtime.md#rt-obj-ingests
        - runtime.md#rt-rte-ingest-cycle
        note: This is a best-effort lifecycle interlock, not a semantic-content veto or race-free filesystem
          lock.
      records:
      - memory.md#mem-obj-raw
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-log
      - memory.md#mem-obj-tasks
      - memory.md#mem-obj-index
      - memory.md#mem-obj-collections
      - runtime.md#rt-rte-vault-consume
      - epistemic.md#epi-rte-semantic-revision
      - memory.md#mem-obj-manifest-projections
      - runtime.md#rt-obj-ingests
      - memory.md#mem-rte-affected-selection
      - runtime.md#rt-rte-maintenance-write
      - runtime.md#rt-rte-ingest-cycle
      note: The inventory resolves actual reader, selector, scoring and lifecycle consumers. Static contract
        instruction authority is excluded; unconsumed metadata gets no authority. Missing observed activation
        does not erase wired/afforded force.
    write_agency:
      assessment: partial
      units:
      - scope: Human capture and direct human source provision
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records:
          - memory.md#mem-obj-raw
          - runtime.md#rt-rte-ingest-cycle
          note: The protocol explicitly assigns captured input/source provision to the human; that decision
            supplies the retained content.
        records:
        - memory.md#mem-obj-raw
        - runtime.md#rt-rte-ingest-cycle
        note: Manual admission is doctrinal here; no actual operator-content instance was supplied.
      - scope: Protocol-directed external-agent wiki/index/log/task writing
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records:
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-log
          - memory.md#mem-obj-index
          - memory.md#mem-obj-tasks
          - epistemic.md#epi-rte-semantic-revision
          - runtime.md#rt-rte-ingest-cycle
          note: The external model/agent proposes and directly writes without a required per-content human
            approval; initiating ingest is not approval of its pages.
        records:
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-log
        - memory.md#mem-obj-index
        - memory.md#mem-obj-tasks
        - epistemic.md#epi-rte-semantic-revision
        - runtime.md#rt-rte-ingest-cycle
        note: Classification concerns the prescribed admission mechanism, not observed model obedience
          or the unknown author of an initial file.
      - scope: Archive/clear, scan/session transitions, collection regeneration and index preservation/rebuild
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-raw
          - memory.md#mem-obj-manifest-projections
          - runtime.md#rt-obj-ingests
          - runtime.md#rt-rte-ingest-cycle
          - memory.md#mem-rte-collection-regeneration
          - memory.md#mem-obj-index
          - runtime.md#rt-rte-maintenance-write
          note: Software selects and admits exact transformed content under fixed rules; dry-run or initiating
            the command does not make generated-content admission manual.
        records:
        - memory.md#mem-obj-raw
        - memory.md#mem-obj-manifest-projections
        - runtime.md#rt-obj-ingests
        - runtime.md#rt-rte-ingest-cycle
        - memory.md#mem-rte-collection-regeneration
        - memory.md#mem-obj-index
        - runtime.md#rt-rte-maintenance-write
        note: Known deterministic admission covers subsequent writes; it does not identify upstream content
          authors.
      - scope: TaskAdd/TaskDone deterministic append and selected-marker admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-tasks
          - runtime.md#rt-rte-maintenance-write
          note: Program rules admit nonempty task fields and choose a completion target without a second
            human approval of the selected line.
        records:
        - memory.md#mem-obj-tasks
        - runtime.md#rt-rte-maintenance-write
        note: Automatic target/write admission is separate from who supplied the task text or matching
          request.
      - scope: Initial vault content, arbitrary direct edits and generic caller-supplied task text
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-raw
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-tasks
        - memory.md#mem-obj-index
        - memory.md#mem-obj-log
        - runtime.md#rt-rte-ingest-cycle
        - runtime.md#rt-rte-maintenance-write
        note: No authenticated initial-content decision or generic caller principal establishes human
          versus model admission for these alternatives. This prevents complete write-control coverage,
          not classification of inspected subsequent transformations.
      records:
      - memory.md#mem-obj-raw
      - runtime.md#rt-rte-ingest-cycle
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-log
      - memory.md#mem-obj-index
      - memory.md#mem-obj-tasks
      - epistemic.md#epi-rte-semantic-revision
      - memory.md#mem-obj-manifest-projections
      - runtime.md#rt-obj-ingests
      - memory.md#mem-rte-collection-regeneration
      - runtime.md#rt-rte-maintenance-write
      note: Explicit human capture and model/software admission are supported separately; initial/direct/generic-caller
        control remains unresolved, so the axis is partial.
    curation_operations:
      assessment: partial
      units:
      - scope: Protocol-directed wiki alias deduplication, preferred updates and contradiction sections
        assessment: partial
        findings:
        - value: dedup
          basis: claimed
          records:
          - memory.md#mem-obj-wiki-pages
          - epistemic.md#epi-rte-semantic-revision
          note: The contract requests alias-aware duplicate suppression before creating pages.
        - value: evolve
          basis: claimed
          records:
          - memory.md#mem-obj-wiki-pages
          - epistemic.md#epi-rte-semantic-revision
          note: The contract prefers revising existing pages and appending sourced contradictions.
        records:
        - memory.md#mem-obj-wiki-pages
        - epistemic.md#epi-rte-semantic-revision
        note: Requested operations are positive claimed findings, not implemented semantic checks. Actual
          page contents are unavailable; summary/synthesis labels do not establish which further transformations
          occurred.
      - scope: Quotes/Ideas field selection, Books context reduction and index catalog/description reduction
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - epistemic.md#epi-rte-quotes-extract
          - epistemic.md#epi-rte-ideas-extract
          - epistemic.md#epi-rte-books-extract
          - memory.md#mem-obj-index
          - runtime.md#rt-rte-maintenance-write
          note: These routes select retained fields, omit source bodies, truncate quote context or reduce
            the old catalog to current links and matching descriptions.
        records:
        - epistemic.md#epi-rte-quotes-extract
        - epistemic.md#epi-rte-ideas-extract
        - epistemic.md#epi-rte-books-extract
        - memory.md#mem-obj-index
        - runtime.md#rt-rte-maintenance-write
        note: Reduced representations of existing material establish consolidation even while source files
          remain retained; not every index rebuild alone establishes curation.
      - scope: Reading List archive-to-queue extraction
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records:
          - epistemic.md#epi-rte-reading-extract
          - memory.md#mem-obj-collections
          note: Exact case-sensitive repeated captured text is removed from the output queue.
        - value: consolidate
          basis: wired
          records:
          - epistemic.md#epi-rte-reading-extract
          - memory.md#mem-obj-collections
          note: The queue selects to-read lines from archived capture and retains a reduced directive/path
            representation.
        records:
        - epistemic.md#epi-rte-reading-extract
        - memory.md#mem-obj-collections
        note: The operation is exact-text deduplication, not an inferred semantic-near-duplicate check
          or completed-reading lifecycle.
      - scope: Books probable-title branch and Projects maturity-to-shipping branch
        assessment: known
        findings:
        - value: synthesize
          basis: wired
          records:
          - epistemic.md#epi-rte-books-extract
          - epistemic.md#epi-rte-projects-extract
          note: 'The accepted non-entailment examples establish claims absent from input warrant: guessed
            book identity and shipping status from maturity.'
        records:
        - epistemic.md#epi-rte-books-extract
        - epistemic.md#epi-rte-projects-extract
        note: Separate Books literal book-hint copying is not synthesis; deterministic execution alone
          does not make these inferred claims entailed.
      - scope: TaskDone revision of a retained task marker
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-tasks
          - runtime.md#rt-rte-maintenance-write
          note: The existing selected task entry changes from open to checked and survives in the file.
        records:
        - memory.md#mem-obj-tasks
        - runtime.md#rt-rte-maintenance-write
        note: A recorded-state revision, not evidence that the work succeeded.
      - scope: Missing-file tombstones at later manifest page catalogs
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-obj-manifest-projections
          - runtime.md#rt-rte-maintenance-write
          note: Deletion markers preserve file history while excluding missing parents from ListPages
            and derived catalogs.
        records:
        - memory.md#mem-obj-manifest-projections
        - runtime.md#rt-rte-maintenance-write
        note: Withdrawal is limited to those catalogs; stale outgoing graph edges can survive and derived
          wiki claims are not automatically retracted.
      - scope: Bookmarks residual-text and Media first-URL association branches
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-bookmarks-extract
        - epistemic.md#epi-rte-media-extract
        note: Accepted records establish extraction but leave semantic preservation/association indeterminate
          for actual inputs. Cannot classify further curation from an extractor name or assume every opaque
          association is synthesis.
      records:
      - memory.md#mem-obj-wiki-pages
      - epistemic.md#epi-rte-semantic-revision
      - epistemic.md#epi-rte-quotes-extract
      - epistemic.md#epi-rte-ideas-extract
      - epistemic.md#epi-rte-books-extract
      - memory.md#mem-obj-index
      - runtime.md#rt-rte-maintenance-write
      - epistemic.md#epi-rte-reading-extract
      - memory.md#mem-obj-collections
      - epistemic.md#epi-rte-projects-extract
      - memory.md#mem-obj-tasks
      - memory.md#mem-obj-manifest-projections
      - epistemic.md#epi-rte-bookmarks-extract
      - epistemic.md#epi-rte-media-extract
      note: Implemented reductions, duplicate removal, revisions, bounded withdrawal and two novel-claim
        branches are retained alongside unresolved semantic transformations. No decay or promotion is
        inferred from generated stable metadata or status labels.
    read_back_direction:
      assessment: known
      units:
      - scope: Query/Brief/Viewer request, selection and delivery; prescribed external page reads
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-vault-consume
          - memory.md#mem-obj-manifest-projections
          - memory.md#mem-obj-log
          - memory.md#mem-obj-tasks
          note: Explicit CLI/MCP or URL requests obtain selected metadata, log/task text or rendered bodies.
        - value: pull
          basis: afforded
          records:
          - runtime.md#rt-rte-vault-consume
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-raw
          - memory.md#mem-obj-index
          - memory.md#mem-obj-collections
          - epistemic.md#epi-rte-semantic-revision
          note: The external answering agent is instructed to read matching page bodies; direct file readers
            can request retained prose/catalogs.
        records:
        - runtime.md#rt-rte-vault-consume
        - memory.md#mem-obj-manifest-projections
        - memory.md#mem-obj-log
        - memory.md#mem-obj-tasks
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-raw
        - memory.md#mem-obj-index
        - memory.md#mem-obj-collections
        - epistemic.md#epi-rte-semantic-revision
        note: Automatic selection within fulfillment is not unsolicited push; actual agent body-read/context
          inclusion is not observed.
      - scope: Requested collection/index/task/scan maintenance and affected advice consume earlier retained
          state
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-collection-regeneration
          - memory.md#mem-obj-index
          - memory.md#mem-obj-tasks
          - memory.md#mem-obj-manifest-projections
          - runtime.md#rt-obj-ingests
          - memory.md#mem-rte-affected-selection
          - runtime.md#rt-rte-maintenance-write
          note: Explicit operations request extraction/rebuild, task selection or changed-state advice;
            code reads prior content/state to fulfill them.
        records:
        - memory.md#mem-rte-collection-regeneration
        - memory.md#mem-obj-index
        - memory.md#mem-obj-tasks
        - memory.md#mem-obj-manifest-projections
        - runtime.md#rt-obj-ingests
        - memory.md#mem-rte-affected-selection
        - runtime.md#rt-rte-maintenance-write
        note: Includes machine later-consumers, not only model readers. Affected advice is not retained,
          but its scan/session inputs are read back.
      records:
      - runtime.md#rt-rte-vault-consume
      - memory.md#mem-obj-manifest-projections
      - memory.md#mem-obj-log
      - memory.md#mem-obj-tasks
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-raw
      - memory.md#mem-obj-index
      - memory.md#mem-obj-collections
      - epistemic.md#epi-rte-semantic-revision
      - memory.md#mem-rte-collection-regeneration
      - runtime.md#rt-obj-ingests
      - memory.md#mem-rte-affected-selection
      - runtime.md#rt-rte-maintenance-write
      note: The accepted dispatch/consumer inventory describes caller-requested chains throughout the
        accumulated-vault boundary. Static harness contract loading and external context scheduling are
        excluded; no included unsolicited payload branch is left unresolved.
    read_back_signal:
      assessment: inapplicable
      units:
      - scope: All included caller-requested vault content and metadata read-back chains
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-vault-consume
        - memory.md#mem-rte-collection-regeneration
        - memory.md#mem-obj-index
        - memory.md#mem-obj-tasks
        - memory.md#mem-obj-manifest-projections
        - runtime.md#rt-obj-ingests
        - memory.md#mem-rte-affected-selection
        - runtime.md#rt-rte-maintenance-write
        - runtime.md#rt-rte-ingest-cycle
        note: All covered read-back is pull. Query identity matches, brief date/budget rules and requested
          URLs are selectors within fulfillment, not push signals.
      records:
      - runtime.md#rt-rte-vault-consume
      - memory.md#mem-rte-collection-regeneration
      - memory.md#mem-obj-index
      - memory.md#mem-obj-tasks
      - memory.md#mem-obj-manifest-projections
      - runtime.md#rt-obj-ingests
      - memory.md#mem-rte-affected-selection
      - runtime.md#rt-rte-maintenance-write
      - runtime.md#rt-rte-ingest-cycle
      note: No push operation is established within the completely inventoried requested vault-consumer
        boundary; signal classification applies to push only. This does not classify excluded harness
        scheduling.
    trace_learning:
      assessment: not-determinable
      units:
      - scope: Archive, scan/lifecycle state, collections, index and task writes with later consumers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-raw
        - memory.md#mem-obj-manifest-projections
        - runtime.md#rt-obj-ingests
        - memory.md#mem-rte-collection-regeneration
        - memory.md#mem-obj-index
        - memory.md#mem-obj-tasks
        - runtime.md#rt-rte-maintenance-write
        - runtime.md#rt-rte-ingest-cycle
        note: Inspected writes retain captures, access state, projections or task status; accepted records
          establish no qualifying original trace-to-durable-behavior-shaping update. No bounded absence
          record warrants a controlled no finding for the whole family.
      - scope: Agent-authored operation log and semantic wiki revision; Brief log consumption
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-log
        - memory.md#mem-obj-wiki-pages
        - epistemic.md#epi-rte-semantic-revision
        - runtime.md#rt-rte-vault-consume
        note: Log summaries are requested authored history, not recorded automatic trace extraction. Brief
          delivers history but saves no derived checkpoint/policy. Unavailable actual agent traces/content
          prevent establishing a qualifying automatic write; no supported yes or bounded no is asserted.
      records:
      - memory.md#mem-obj-raw
      - memory.md#mem-obj-manifest-projections
      - runtime.md#rt-obj-ingests
      - memory.md#mem-rte-collection-regeneration
      - memory.md#mem-obj-index
      - memory.md#mem-obj-tasks
      - runtime.md#rt-rte-maintenance-write
      - runtime.md#rt-rte-ingest-cycle
      - memory.md#mem-obj-log
      - memory.md#mem-obj-wiki-pages
      - epistemic.md#epi-rte-semantic-revision
      - runtime.md#rt-rte-vault-consume
      note: The accepted records support retention/curation and historical read-back, but neither a qualifying
        trace-fed write nor an evidenced-absence record supplying a controlled negative. This is not a
        system-wide no and does not assess excluded provider/harness learning.
    trace_source:
      assessment: not-determinable
      units:
      - scope: Potential trace-fed wiki/log routes and inspected deterministic vault writes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-raw
        - memory.md#mem-obj-log
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-manifest-projections
        - runtime.md#rt-obj-ingests
        - memory.md#mem-rte-collection-regeneration
        - memory.md#mem-obj-index
        - memory.md#mem-obj-tasks
        - epistemic.md#epi-rte-semantic-revision
        - runtime.md#rt-rte-vault-consume
        - runtime.md#rt-rte-ingest-cycle
        note: No qualifying trace-learning write has been established and complete bounded absence is
          not recorded. Captured source files, dated archive separators and ingest rows cannot alone establish
          session-logs, tool-traces, event-streams or trajectories as original qualifying inputs.
      records:
      - memory.md#mem-obj-raw
      - memory.md#mem-obj-log
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-manifest-projections
      - runtime.md#rt-obj-ingests
      - memory.md#mem-rte-collection-regeneration
      - memory.md#mem-obj-index
      - memory.md#mem-obj-tasks
      - epistemic.md#epi-rte-semantic-revision
      - runtime.md#rt-rte-vault-consume
      - runtime.md#rt-rte-ingest-cycle
      note: Without an established qualifying update or a completely warranted negative, trace-source
        is unresolved rather than inapplicable. Operational dates and journal formatting do not change
        the original content into an event stream.
---

# Sparks memory profile

## Comparison rationale

This profile classifies the accepted records, not a running personal vault. Wiring establishes deterministic file/SQLite writes and selection. The external agent's semantic obligations remain claimed, and its later body-reading route is afforded. No classification is observed or causally supported: the records supply no execution trace or comparison. The scope separates accumulated content from the static [RT-OBJ-contract](runtime.md#rt-obj-contract) and the external [RT-CMP-agent](runtime.md#rt-cmp-agent); their persistence or parametric computation does not turn them into accumulated Sparks vault memory.

### Inventory and local uncertainty

The raw, wiki, log, Tasks, index, generated-collection, manifest-projection and ingest-history units retain distinct consumption paths. Markdown has natural-language bodies and symbolic dates, links, fields and markers. The [MEM-OBJ-manifest-projections](memory.md#mem-obj-manifest-projections) is executable access state rather than source-body meaning. Optional repository history follows [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle), not an assertion that every vault has Git enabled. Available helper details and absent executions limit extraction quality or activation; they do not make the inspected substrate opaque.

Known deterministic admission does not settle initial provenance or generic caller identity. In particular, [MEM-OBJ-tasks](memory.md#mem-obj-tasks) has software target admission and unresolved caller-supplied content control. The [MEM-OBJ-index](memory.md#mem-obj-index) preserves old descriptions without authenticating their initial author or reevaluating them. Those unresolved alternatives remain in lineage and write-agency units. The prescribed external-agent writer has automatic admission because no per-page human decision is required, not because a human started the ingest.

### Authority, curation and read-back

Page and log content supplies knowledge at readers; it is not standing host instruction. Manifest/session state supplies routing and lifecycle admission criteria. Retained task text influences fuzzy ranking, while checkbox state controls the candidate/preview set. These consumer-specific effects do not depend on demonstrated answer improvement. Task identity matching and row interlocks also do not license semantic truth or real-world task success: see [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write), [RT-OBJ-ingests](runtime.md#rt-obj-ingests) and [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume).

The two wired synthesis findings are local: [EPI-RTE-books-extract](epistemic.md#epi-rte-books-extract) infers probable book identity from attribution punctuation, and [EPI-RTE-projects-extract](epistemic.md#epi-rte-projects-extract) turns maturity into shipping labels. Their accepted non-entailment warrants distinguish these from literal hint import, source-field selection and context reduction. [EPI-RTE-reading-extract](epistemic.md#epi-rte-reading-extract) implements exact-text deduplication. Requested semantic summaries do not establish synthesis, and uncertain Bookmarks/Media associations remain unresolved rather than inheriting a neighboring extractor's basis. Likewise generated stable headers do not establish promotion through review.

Requested collection regeneration consumes retained sources and produces files for a later requested reader. Query supplies metadata, not Revision reasons; the prescribed full-body read is the bridge to those reasons. Brief delivers selected retained log/task text without automatically saving a new summary. The [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume) and [MEM-RTE-collection-regeneration](memory.md#mem-rte-collection-regeneration) therefore support pull, not a second push merely because fixed code selects and delivers material. Read-back signal is inapplicable for this fully named pull-only vault inventory; no claim is made about the excluded harness loader.

Trace-learning remains not-determinable rather than a controlled negative. The [MEM-OBJ-log](memory.md#mem-obj-log) is requested authored operational history; its forwarding to Brief is not a recorded automatic trace-fed durable update. Archive and access-state derivation alone do not establish that chain either. The accepted records declare no bounded absence supplying a local no. Consequently trace-source cannot be made inapplicable by an unsupported system negative, and dated captures cannot be relabeled event-stream inputs without a qualifying write.

### Reconciliation and source-read log

The supplied reconciliation supersedes the epistemic raw object with [MEM-OBJ-raw](memory.md#mem-obj-raw), the epistemic task object with [MEM-OBJ-tasks](memory.md#mem-obj-tasks), and the epistemic affected route with [MEM-RTE-affected-selection](memory.md#mem-rte-affected-selection). All values above use those canonical destinations. The combined epistemic wiki object and seven-output memory collection container remain valid alongside their parts; they are not reasons to merge consumer effects or strengthen one branch from another's evidence.

The recorded missing-frontmatter conflict prevents assuming tolerated scan files remain ordinary query candidates. No value here depends on that implication. Missing-file withdrawal is limited to catalog visibility, not complete graph withdrawal or truth-based retraction: [MEM-OBJ-manifest-projections](memory.md#mem-obj-manifest-projections) retain the stale-edge qualification. Thus neither catalog routing nor bounded invalidation promises complete freshness.

Source-read log: none. This job used only the supplied accepted members and governing contracts; it added no source passages, records or evidence and did not reopen report verification.
