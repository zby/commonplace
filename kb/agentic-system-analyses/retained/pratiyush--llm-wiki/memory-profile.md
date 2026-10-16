---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'llm-wiki memory profile: retained session/wiki files, access state, deferred tasks, method
  revisions and reader products'
run-id: AAS-2026-10-16-llm-wiki-6786c5985cdc-01
source-identity: https://github.com/Pratiyush/llm-wiki
reviewed-boundary: b1088890ee0743810a92577aecad946c6b3eb2d2
memory-comparison:
  version: 2
  scope: Retained raw session renderings; derived source/entity/concept/overview and saved-answer wiki
    content; navigation, graph, quality, mtime and deferred-task metadata; candidate archives/reasons;
    queue and special-memory alternatives; approved method/steering/skill revisions; reader/search/export
    products and their write, maintenance and later-consumer routes. Includes unresolved initialization,
    special-cache wiring and unread repair/vault/editor variants. Excludes static shipped instructions
    as accumulated memory, transient unsaved lint reports, native private stores, external provider weights
    and host windows.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Retained raw sessions and derived wiki page bodies/frontmatter
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - epistemic.md#epi-obj-raw-sessions
          - runtime.md#rt-rte-session-conversion
          - memory.md#mem-obj-wiki
          - runtime.md#rt-rte-backend-synthesis
          note: Conversion and synthesis persist local Markdown; this is filesystem storage, not a repository
            database.
        records:
        - epistemic.md#epi-obj-raw-sessions
        - runtime.md#rt-rte-session-conversion
        - memory.md#mem-obj-wiki
        - runtime.md#rt-rte-backend-synthesis
        note: Covers the recorded raw and wiki products, not provider parameters.
      - scope: Navigation/folder context, quality fields, candidate archives/reasons and JSON work state
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-navigation
          - memory.md#mem-obj-quality-metadata
          - memory.md#mem-obj-candidate-archive
          - memory.md#mem-obj-ingest-queue
          - runtime.md#rt-rte-session-conversion
          - runtime.md#rt-obj-pending-prompts
          note: Markdown, adjacent reason text and JSON files retain content or access/coordination metadata.
        records:
        - memory.md#mem-obj-navigation
        - memory.md#mem-obj-quality-metadata
        - memory.md#mem-obj-candidate-archive
        - memory.md#mem-obj-ingest-queue
        - runtime.md#rt-rte-session-conversion
        - runtime.md#rt-obj-pending-prompts
        note: Includes initialized scaffolds and the stored queue even though their proposed automatic
          use is unresolved.
      - scope: Retained graph JSON and reader/search/export products
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-rte-graph-query
          - runtime.md#rt-rte-reader-build
          - epistemic.md#epi-obj-reader-overview
          note: The graph is serialized JSON reloaded from disk; reader products include HTML and copied/generated
            artifacts.
        records:
        - memory.md#mem-rte-graph-query
        - runtime.md#rt-rte-reader-build
        - epistemic.md#epi-obj-reader-overview
        note: Graph encoding does not establish a graph storage service; transient NetworkX structures
          are not a separate accumulated store.
      - scope: Retained method/steering/skill revisions
        assessment: known
        findings:
        - value: files
          basis: afforded
          records:
          - memory.md#mem-rte-self-learn
          note: Approved changes persist in documentation, steering, skills and changelog for later host/framework
            reads.
        records:
        - memory.md#mem-rte-self-learn
        note: The instruction-mediated route is afforded, not an observed deployment.
      - scope: Included vault/editor retained variants and repair-produced representations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-wiki
        - memory.md#mem-obj-navigation
        note: The supplied memory coverage leaves overlay/write-helper and repair variants uninspected;
          their entire retained-object inventory cannot be classified.
      records:
      - epistemic.md#epi-obj-raw-sessions
      - runtime.md#rt-rte-session-conversion
      - memory.md#mem-obj-wiki
      - runtime.md#rt-rte-backend-synthesis
      - memory.md#mem-obj-navigation
      - memory.md#mem-obj-quality-metadata
      - memory.md#mem-obj-candidate-archive
      - memory.md#mem-obj-ingest-queue
      - runtime.md#rt-obj-pending-prompts
      - memory.md#mem-rte-graph-query
      - runtime.md#rt-rte-reader-build
      - epistemic.md#epi-obj-reader-overview
      - memory.md#mem-rte-self-learn
      note: Known retained objects use files. Uninspected included variants prevent claiming complete
        substrate coverage. External provider weights and live host windows are excluded, not additional
        accumulated memory stores.
    representational_form:
      assessment: partial
      units:
      - scope: Raw transcript prose and wiki/archived page prose at model or human readers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - epistemic.md#epi-obj-raw-sessions
          - memory.md#mem-obj-wiki
          - memory.md#mem-obj-candidate-archive
          - runtime.md#rt-rte-backend-synthesis
          - runtime.md#rt-rte-mcp-access
          note: Retained summaries, quotations, contradictions and rendered utterances reach interpretation
            through read-back.
        records:
        - epistemic.md#epi-obj-raw-sessions
        - memory.md#mem-obj-wiki
        - memory.md#mem-obj-candidate-archive
        - runtime.md#rt-rte-backend-synthesis
        - runtime.md#rt-rte-mcp-access
        note: Covers prose paths; code/tool excerpts and exact structural fields are split below.
      - scope: File identities, mtime state, frontmatter, links, UUIDs, queue paths and graph nodes/edges
          at fixed-code consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-rte-session-conversion
          - runtime.md#rt-obj-pending-prompts
          - runtime.md#rt-rte-agent-completion
          - memory.md#mem-obj-quality-metadata
          - memory.md#mem-obj-ingest-queue
          - memory.md#mem-rte-graph-query
          - runtime.md#rt-rte-mcp-access
          note: Exact equality, matching, filtering and traversal rules consume localized fields and labels.
        records:
        - runtime.md#rt-rte-session-conversion
        - runtime.md#rt-obj-pending-prompts
        - runtime.md#rt-rte-agent-completion
        - memory.md#mem-obj-quality-metadata
        - memory.md#mem-obj-ingest-queue
        - memory.md#mem-rte-graph-query
        - runtime.md#rt-rte-mcp-access
        note: Numeric confidence is symbolic metadata, not distributed model parameters.
      - scope: Pending rendered task/source prose and navigation descriptions at the foreground host
        assessment: known
        findings:
        - value: natural-language
          basis: afforded
          records:
          - runtime.md#rt-obj-pending-prompts
          - runtime.md#rt-rte-host-ingest
          - memory.md#mem-obj-navigation
          note: Later host procedures interpret the rendered prompt and folder descriptions; the 240-character
            display summary is not the whole payload.
        records:
        - runtime.md#rt-obj-pending-prompts
        - runtime.md#rt-rte-host-ingest
        - memory.md#mem-obj-navigation
        note: UUID/header consumers remain a separate symbolic unit; host compliance is unobserved.
      - scope: Method revisions and approved reflection output at later host readers
        assessment: known
        findings:
        - value: natural-language
          basis: afforded
          records:
          - memory.md#mem-rte-self-learn
          - memory.md#mem-rte-wiki-maintenance
          note: Textual lessons, revised guidance and saved reflections are interpreted rather than executed
            as numerical weights.
        records:
        - memory.md#mem-rte-self-learn
        - memory.md#mem-rte-wiki-maintenance
        note: Maintenance implementation status is disputed; this finding concerns the memory report's
          afforded textual route only.
      - scope: Reader overview and generated publication structure
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - epistemic.md#epi-obj-reader-overview
          - runtime.md#rt-rte-reader-build
          note: Optional model prose is retained in HTML for readers.
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-rte-reader-build
          - memory.md#mem-rte-graph-query
          note: Generated navigation/search/export structures are consumed by fixed rendering, lookup
            or graph rules.
        records:
        - epistemic.md#epi-obj-reader-overview
        - runtime.md#rt-rte-reader-build
        - memory.md#mem-rte-graph-query
        note: The optional reader prose does not enter curated wiki Markdown.
      - scope: Code/tool excerpt consumption beyond prose previews; customized special caches and unread
          publication/editor variants
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-obj-raw-sessions
        - memory.md#mem-obj-wiki
        - memory.md#mem-obj-navigation
        - runtime.md#rt-rte-reader-build
        note: Records identify mixed raw code/tool material and special-file labels but do not resolve
          every operative consumption form or every unread variant. No parametric memory finding follows.
      records:
      - epistemic.md#epi-obj-raw-sessions
      - memory.md#mem-obj-wiki
      - memory.md#mem-obj-candidate-archive
      - runtime.md#rt-rte-backend-synthesis
      - runtime.md#rt-rte-mcp-access
      - runtime.md#rt-rte-session-conversion
      - runtime.md#rt-obj-pending-prompts
      - runtime.md#rt-rte-agent-completion
      - memory.md#mem-obj-quality-metadata
      - memory.md#mem-obj-ingest-queue
      - memory.md#mem-rte-graph-query
      - runtime.md#rt-rte-host-ingest
      - memory.md#mem-obj-navigation
      - memory.md#mem-rte-self-learn
      - memory.md#mem-rte-wiki-maintenance
      - epistemic.md#epi-obj-reader-overview
      - runtime.md#rt-rte-reader-build
      note: Natural-language and symbolic paths coexist and are classified separately. Unresolved mixed/externalized
        variants prevent complete form coverage; model components are not retained memory merely because
        synthesis calls them.
    lineage:
      assessment: partial
      units:
      - scope: Acquired raw Markdown from external session stores and source inputs
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - runtime.md#rt-rte-session-conversion
          - epistemic.md#epi-obj-raw-sessions
          note: Adapter-discovered material enters rendered/redacted/truncated raw files; import does
            not certify source truth.
        records:
        - runtime.md#rt-rte-session-conversion
        - epistemic.md#epi-obj-raw-sessions
        note: Native-session fidelity and specific adapter loss remain unknown without changing the established
          acquisition path.
      - scope: Backend-derived source pages and deferred rendered source tasks
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-rte-backend-synthesis
          - runtime.md#rt-obj-pending-prompts
          - runtime.md#rt-rte-agent-completion
          - memory.md#mem-obj-wiki
          note: Recorded session material feeds selected prefixes, generated or staged source-page content,
            and later consumers.
        records:
        - runtime.md#rt-rte-backend-synthesis
        - runtime.md#rt-obj-pending-prompts
        - runtime.md#rt-rte-agent-completion
        - memory.md#mem-obj-wiki
        note: Covers the established session-derived branch, not all initial wiki content or every non-session
          source.
      - scope: Host-ingested pages and session lessons retained as method guidance
        assessment: known
        findings:
        - value: trace-extracted
          basis: afforded
          records:
          - runtime.md#rt-rte-host-ingest
          - memory.md#mem-obj-wiki
          - memory.md#mem-rte-self-learn
          note: Shipped host procedures derive summaries or lessons from session material and retain the
            result.
        records:
        - runtime.md#rt-rte-host-ingest
        - memory.md#mem-obj-wiki
        - memory.md#mem-rte-self-learn
        note: Human approval of method edits is independent of their trace-derived lineage.
      - scope: Derived graph/access metadata and reader products
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-rte-graph-query
          - runtime.md#rt-rte-session-conversion
          - runtime.md#rt-rte-backend-synthesis
          - runtime.md#rt-rte-reader-build
          - epistemic.md#epi-obj-reader-overview
          note: File predicates, graph extraction, page wrapping and publication compile retained inputs
            into access state or reader representations.
        records:
        - memory.md#mem-rte-graph-query
        - runtime.md#rt-rte-session-conversion
        - runtime.md#rt-rte-backend-synthesis
        - runtime.md#rt-rte-reader-build
        - epistemic.md#epi-obj-reader-overview
        note: The optional overview is metadata-derived, not an ordinary curated wiki synthesis.
      - scope: Initial wiki/candidate/custom folder content, exact quality-field initialization and special
          caches
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-wiki
        - runtime.md#rt-rte-candidate-admission
        - memory.md#mem-obj-navigation
        - memory.md#mem-obj-quality-metadata
        note: The records establish subsequent uses/transitions but not all initial authorship or derivation
          paths. Static init scaffolds are not accumulated experience.
      - scope: Non-session-source branches, external graph construction and unread repairs/vault overlays
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-wiki
        - memory.md#mem-rte-graph-query
        note: Mixed imported sources and opaque/uninspected transformation details prevent a complete
          lineage inventory.
      records:
      - runtime.md#rt-rte-session-conversion
      - epistemic.md#epi-obj-raw-sessions
      - runtime.md#rt-rte-backend-synthesis
      - runtime.md#rt-obj-pending-prompts
      - runtime.md#rt-rte-agent-completion
      - memory.md#mem-obj-wiki
      - runtime.md#rt-rte-host-ingest
      - memory.md#mem-rte-self-learn
      - memory.md#mem-rte-graph-query
      - runtime.md#rt-rte-reader-build
      - epistemic.md#epi-obj-reader-overview
      - runtime.md#rt-rte-candidate-admission
      - memory.md#mem-obj-navigation
      - memory.md#mem-obj-quality-metadata
      note: Imported, trace-extracted and other-compiled paths are supported locally. Unknown initialization
        and alternative transformations remain included; a known later transform cannot establish original
        authorship.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retained raw and wiki prose at synthesis and answer consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - epistemic.md#epi-obj-raw-sessions
          - runtime.md#rt-rte-backend-synthesis
          - memory.md#mem-obj-wiki
          - runtime.md#rt-rte-mcp-access
          note: Raw content supplies synthesis context and wiki text supplies requested MCP answer context.
        - value: learning
          basis: wired
          records:
          - runtime.md#rt-rte-backend-synthesis
          - epistemic.md#epi-obj-raw-sessions
          - memory.md#mem-obj-wiki
          note: Retained session experience feeds automatic durable source-page production with later
            host/MCP consumers; this is update-consumer authority, not proof of improved capacity.
        records:
        - epistemic.md#epi-obj-raw-sessions
        - runtime.md#rt-rte-backend-synthesis
        - memory.md#mem-obj-wiki
        - runtime.md#rt-rte-mcp-access
        note: Knowledge at delivery and learning at the trace-fed update consumer are separate paths.
      - scope: Wiki text, graph labels/connectivity and quality fields at retrieval selectors
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - runtime.md#rt-rte-mcp-access
          - memory.md#mem-rte-graph-query
          - epistemic.md#epi-rte-metadata-selection
          note: Retained text and graph features affect relative retrieval priority; quality views also
            sort stored confidence labels.
        - value: routing
          basis: wired
          records:
          - memory.md#mem-rte-graph-query
          - epistemic.md#epi-rte-metadata-selection
          note: Graph adjacency and retained metadata select traversal scope and filtered result sets.
        records:
        - runtime.md#rt-rte-mcp-access
        - memory.md#mem-rte-graph-query
        - epistemic.md#epi-rte-metadata-selection
        note: Relevance/metadata selection does not establish epistemic acceptance or a stale-read veto.
      - scope: Mtime state, pending identities and queue paths at coordination consumers
        assessment: partial
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-rte-session-conversion
          - runtime.md#rt-rte-backend-synthesis
          - runtime.md#rt-rte-agent-completion
          note: Retained mtimes select future processing and page identity associates deferred completion.
        - value: validation
          basis: wired
          records:
          - runtime.md#rt-obj-pending-prompts
          - runtime.md#rt-rte-agent-completion
          note: Retained UUID/sentinel supplies the criterion for admitting a completion.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-obj-pending-prompts
          - runtime.md#rt-rte-agent-completion
          note: Missing or mismatched retained sentinel blocks body replacement before writing.
        records:
        - runtime.md#rt-rte-session-conversion
        - runtime.md#rt-rte-backend-synthesis
        - runtime.md#rt-obj-pending-prompts
        - runtime.md#rt-rte-agent-completion
        - memory.md#mem-obj-ingest-queue
        note: Queue retention is implemented but its actual later consumer is unresolved; no queue routing
          force is inferred from its docstring.
      - scope: Navigation descriptions and pending task guidance at the foreground host
        assessment: known
        findings:
        - value: routing
          basis: afforded
          records:
          - memory.md#mem-obj-navigation
          - runtime.md#rt-rte-host-ingest
          note: Folder description meaning guides which folders/pages the querying host reads.
        - value: instruction
          basis: afforded
          records:
          - runtime.md#rt-obj-pending-prompts
          - runtime.md#rt-rte-agent-completion
          - runtime.md#rt-rte-host-ingest
          note: Rendered durable pending prompts supply task directions on later foreground pickup.
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-obj-navigation
          - runtime.md#rt-rte-host-ingest
          - runtime.md#rt-obj-pending-prompts
          note: Overview/context and the retained raw excerpt supply interpretive context alongside directions.
        records:
        - memory.md#mem-obj-navigation
        - runtime.md#rt-rte-host-ingest
        - runtime.md#rt-obj-pending-prompts
        - runtime.md#rt-rte-agent-completion
        note: No automatic injection or binding host policy follows from these file-mediated procedures.
      - scope: Trace-derived method revisions at update and later host consumers
        assessment: known
        findings:
        - value: learning
          basis: afforded
          records:
          - memory.md#mem-rte-self-learn
          note: Session lessons feed a human-approved durable method-guidance revision.
        - value: instruction
          basis: afforded
          records:
          - memory.md#mem-rte-self-learn
          note: Revised steering/skills can supply standing host directions when loaded.
        records:
        - memory.md#mem-rte-self-learn
        note: Human-gated learning authority is not automatic trace learning. Deployment-specific later
          loading is uninspected.
      - scope: Retained reader prose at site readers and archived wiki prose at ordinary queries
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - epistemic.md#epi-obj-reader-overview
          - runtime.md#rt-rte-reader-build
          - memory.md#mem-obj-candidate-archive
          - memory.md#mem-clm-archive-visibility
          note: Reader prose supplies reference/context to readers; generic Markdown scans may return
            archived candidate claims without their reasons.
        records:
        - epistemic.md#epi-obj-reader-overview
        - runtime.md#rt-rte-reader-build
        - memory.md#mem-obj-candidate-archive
        - memory.md#mem-clm-archive-visibility
        note: Archival therefore is not general enforcement at read consumers; no dedicated later reason-file
          consumer is established.
      - scope: Quality update consumers, hot/Auto Dream/special-memory routes and unread maintenance variants
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-quality-metadata
        - memory.md#mem-obj-navigation
        note: Production quality-field writers and special-file selectors/loading are unresolved; downstream
          forces for those routes cannot be enumerated.
      records:
      - epistemic.md#epi-obj-raw-sessions
      - runtime.md#rt-rte-backend-synthesis
      - memory.md#mem-obj-wiki
      - runtime.md#rt-rte-mcp-access
      - memory.md#mem-rte-graph-query
      - epistemic.md#epi-rte-metadata-selection
      - runtime.md#rt-rte-session-conversion
      - runtime.md#rt-obj-pending-prompts
      - runtime.md#rt-rte-agent-completion
      - memory.md#mem-obj-ingest-queue
      - memory.md#mem-obj-navigation
      - runtime.md#rt-rte-host-ingest
      - memory.md#mem-rte-self-learn
      - epistemic.md#epi-obj-reader-overview
      - runtime.md#rt-rte-reader-build
      - memory.md#mem-obj-candidate-archive
      - memory.md#mem-clm-archive-visibility
      - memory.md#mem-obj-quality-metadata
      note: Knowledge, learning, ranking, routing, instruction, validation and enforcement have separate
        local witnesses. Unconsumed metadata/reasons do not gain authority merely by retention; unresolved
        consumers prevent complete coverage.
    write_agency:
      assessment: partial
      units:
      - scope: Converter admission of selected raw files and mtime state
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-session-conversion
          note: Code admits selected renderings without a per-content human decision; invocation and force
            selection are not approval of every retained record.
        records:
        - runtime.md#rt-rte-session-conversion
        note: Scope is converter admission, not authorship of native session material.
      - scope: Backend page/state/index writes and deferred prompt/completion admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-backend-synthesis
          - runtime.md#rt-obj-pending-prompts
          - runtime.md#rt-rte-agent-completion
          note: Software accepts backend text or caller body after association checks; no per-content
            human approval is required.
        records:
        - runtime.md#rt-rte-backend-synthesis
        - runtime.md#rt-obj-pending-prompts
        - runtime.md#rt-rte-agent-completion
        note: Foreground initiation does not make the code/model admission manual.
      - scope: Routine foreground semantic ingest and requested page-update admission
        assessment: partial
        findings:
        - value: automatic
          basis: afforded
          records:
          - runtime.md#rt-rte-host-ingest
          - memory.md#mem-rte-wiki-maintenance
          note: Model-mediated routine page edits need no separate approval for each admitted claim in
            the memory report's afforded account.
        - value: automatic
          basis: claimed
          records:
          - epistemic.md#epi-rte-page-update
          note: The epistemic page-update record describes the same direct model edit at claimed strength.
        records:
        - runtime.md#rt-rte-host-ingest
        - memory.md#mem-rte-wiki-maintenance
        - epistemic.md#epi-rte-page-update
        note: 'Keep both maintenance evidence bases: reconciliation leaves afforded versus claimed unresolved.
          No single stronger implementation assessment is selected.'
      - scope: Saving substantial query answers, saving/editing after reflection, and self-learn method
          revisions
        assessment: known
        findings:
        - value: manual
          basis: afforded
          records:
          - runtime.md#rt-rte-host-ingest
          - memory.md#mem-rte-wiki-maintenance
          - memory.md#mem-rte-self-learn
          note: Each route explicitly requires a human choice approving the retained answer, reflection/change
            or proposed method diff.
        - value: manual
          basis: claimed
          records:
          - epistemic.md#epi-rte-wiki-reflection
          note: The epistemic reflection record preserves the approval requirement at claimed strength.
        records:
        - runtime.md#rt-rte-host-ingest
        - memory.md#mem-rte-wiki-maintenance
        - memory.md#mem-rte-self-learn
        - epistemic.md#epi-rte-wiki-reflection
        note: Starting the workflow alone is not this approval; the explicit later content decision establishes
          manual admission.
      - scope: Graph export and regenerated reader/publication admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-graph-query
          - runtime.md#rt-rte-reader-build
          - epistemic.md#epi-obj-reader-overview
          note: Code emits graph/reader files and admits optional nonempty model stdout without per-content
            approval.
        records:
        - memory.md#mem-rte-graph-query
        - runtime.md#rt-rte-reader-build
        - epistemic.md#epi-obj-reader-overview
        note: Opting into the command is not approval of each resulting content item.
      - scope: Candidate creation and caller-selected promotion/merge/discard
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-candidate-admission
        - memory.md#mem-obj-candidate-archive
        note: Transition code is wired, but generic CLI caller identity does not establish a human decision
          or autonomous admission. Candidate initialization is separately unresolved.
      - scope: Customized navigation, quality-field updates, queue callers, special caches and unread
          repair/vault variants
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-navigation
        - memory.md#mem-obj-quality-metadata
        - memory.md#mem-obj-ingest-queue
        note: Who supplies or approves each retained update is unresolved or uninspected; known automatic
          page writes cannot decide these admissions.
      records:
      - runtime.md#rt-rte-session-conversion
      - runtime.md#rt-rte-backend-synthesis
      - runtime.md#rt-obj-pending-prompts
      - runtime.md#rt-rte-agent-completion
      - runtime.md#rt-rte-host-ingest
      - memory.md#mem-rte-wiki-maintenance
      - epistemic.md#epi-rte-page-update
      - memory.md#mem-rte-self-learn
      - epistemic.md#epi-rte-wiki-reflection
      - memory.md#mem-rte-graph-query
      - runtime.md#rt-rte-reader-build
      - epistemic.md#epi-obj-reader-overview
      - runtime.md#rt-rte-candidate-admission
      - memory.md#mem-obj-candidate-archive
      - memory.md#mem-obj-navigation
      - memory.md#mem-obj-quality-metadata
      - memory.md#mem-obj-ingest-queue
      note: Automatic and manual admissions coexist. Candidate caller identity and initialization remain
        unresolved; maintenance status disagreement is retained as distinct warranted findings, not silently
        upgraded.
    curation_operations:
      assessment: partial
      units:
      - scope: Backend trace-prefix extraction and source-page regeneration
        assessment: partial
        findings:
        - value: consolidate
          basis: wired
          records:
          - runtime.md#rt-rte-backend-synthesis
          - memory.md#mem-obj-wiki
          note: The deterministic/source-prefix branch reduces retained session content into source-page
            material; raw retention does not disqualify consolidation.
        - value: consolidate
          basis: afforded
          records:
          - runtime.md#rt-rte-host-ingest
          - memory.md#mem-obj-wiki
          note: Foreground ingest requests per-source summaries and integration of retained claims.
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-rte-backend-synthesis
          note: Force regeneration can replace an existing source-page body while preserving available
            tags.
        records:
        - runtime.md#rt-rte-backend-synthesis
        - runtime.md#rt-rte-host-ingest
        - memory.md#mem-obj-wiki
        note: The available record account does not establish whether every opaque model body preserves,
          derives or adds claims. No synthesize value is inferred from the command name.
      - scope: Optional candidate promotion, merge and archive transitions
        assessment: known
        findings:
        - value: promote
          basis: wired
          records:
          - runtime.md#rt-rte-candidate-admission
          note: Promotion changes candidate status to reviewed and moves content into the target wiki
            tier.
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-rte-candidate-admission
          - memory.md#mem-obj-candidate-archive
          note: Merge appends retained candidate content to an existing target.
        - value: invalidate
          basis: wired
          records:
          - runtime.md#rt-rte-candidate-admission
          - memory.md#mem-obj-candidate-archive
          - memory.md#mem-clm-archive-visibility
          note: Discard/archive withdraws trusted-area placement while retaining candidate history, bounded
            to that admission/location mechanism.
        records:
        - runtime.md#rt-rte-candidate-admission
        - memory.md#mem-obj-candidate-archive
        - memory.md#mem-clm-archive-visibility
        note: 'Invalidation is not a universal read veto: archived Markdown remains eligible for recursive
          retrieval; promotion may overwrite the target.'
      - scope: Requested corrective wiki edits and approved method revisions
        assessment: partial
        findings:
        - value: evolve
          basis: afforded
          records:
          - memory.md#mem-rte-wiki-maintenance
          - memory.md#mem-rte-self-learn
          note: Targeted page edits and approved documentation/steering/skill changes revise existing
            retained text.
        - value: evolve
          basis: claimed
          records:
          - epistemic.md#epi-rte-page-update
          note: The epistemic corrective-update record supports requested revision only at claimed strength.
        records:
        - memory.md#mem-rte-wiki-maintenance
        - memory.md#mem-rte-self-learn
        - epistemic.md#epi-rte-page-update
        note: The maintenance implementation-status conflict remains. Criticism success or novel claims
          are not established.
      - scope: Confidence decay/auto-stale suggestions and special hot/Auto Dream caches
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-quality-metadata
        - memory.md#mem-obj-navigation
        note: Pure helper arithmetic does not establish durable decay/invalidation. Scaffold claims do
          not establish implemented consolidation or promotion.
      - scope: External graph transformations and uninspected repairs/vault/editor variants
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-graph-query
        - memory.md#mem-obj-wiki
        note: Graph index compilation alone is not curation, and unread alternate transformations cannot
          establish or exclude additional operations.
      records:
      - runtime.md#rt-rte-backend-synthesis
      - runtime.md#rt-rte-host-ingest
      - memory.md#mem-obj-wiki
      - runtime.md#rt-rte-candidate-admission
      - memory.md#mem-obj-candidate-archive
      - memory.md#mem-clm-archive-visibility
      - memory.md#mem-rte-wiki-maintenance
      - memory.md#mem-rte-self-learn
      - epistemic.md#epi-rte-page-update
      - memory.md#mem-obj-quality-metadata
      - memory.md#mem-obj-navigation
      - memory.md#mem-rte-graph-query
      note: Consolidate, evolve, promote and bounded invalidate retain local warrants. Index rebuilds,
        acquisition and queue set normalization do not by themselves establish semantic curation; opaque
        outputs prevent a complete operation set.
    read_back_direction:
      assessment: partial
      units:
      - scope: Host question/page requests, MCP query/read/search/quality/export and CLI graph query
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-mcp-access
          - memory.md#mem-rte-quality-inspection
          - memory.md#mem-rte-graph-query
          note: Consumers request retained pages, snippets, metadata, exports or graph summaries; code
            selects and delivers the requested material.
        - value: pull
          basis: afforded
          records:
          - runtime.md#rt-rte-host-ingest
          - memory.md#mem-obj-navigation
          note: The foreground host requests index/overview, folder descriptions and selected pages under
            query doctrine.
        records:
        - runtime.md#rt-rte-mcp-access
        - memory.md#mem-rte-quality-inspection
        - memory.md#mem-rte-graph-query
        - runtime.md#rt-rte-host-ingest
        - memory.md#mem-obj-navigation
        note: Automatic ranking within a requested return is not a separate push operation.
      - scope: Synthesis/ingest and deferred-task pickup on explicit invocation
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-backend-synthesis
          - runtime.md#rt-rte-agent-completion
          - runtime.md#rt-obj-pending-prompts
          note: Invoked synthesis reloads retained raw material and state; the completion workflow uses
            persisted pending tasks.
        - value: pull
          basis: afforded
          records:
          - runtime.md#rt-rte-host-ingest
          - runtime.md#rt-rte-agent-completion
          - runtime.md#rt-obj-pending-prompts
          - memory.md#mem-rte-self-learn
          note: The later slash/self-learn procedure requests retained task/transcript/framework context.
        records:
        - runtime.md#rt-rte-backend-synthesis
        - runtime.md#rt-rte-agent-completion
        - runtime.md#rt-obj-pending-prompts
        - runtime.md#rt-rte-host-ingest
        - memory.md#mem-rte-self-learn
        note: The backend does not launch a worker or schedule unsolicited delivery; UUID association
          is not evidence of push.
      - scope: Reader/export consumption after requested publication
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-reader-build
          - epistemic.md#epi-obj-reader-overview
          note: Build consumes retained raw/metadata and later readers/export requests load generated
            artifacts.
        records:
        - runtime.md#rt-rte-reader-build
        - epistemic.md#epi-obj-reader-overview
        note: No deployment or actual later reading is observed.
      - scope: SessionStart/queue, hot-refresh and special-memory injection
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-ingest-queue
        - memory.md#mem-obj-navigation
        note: Missing hook and unresolved automatic selectors/loading prevent establishing the direction
          of proposed delivery. Ordinary readability is not proof of push.
      records:
      - runtime.md#rt-rte-mcp-access
      - memory.md#mem-rte-quality-inspection
      - memory.md#mem-rte-graph-query
      - runtime.md#rt-rte-host-ingest
      - memory.md#mem-obj-navigation
      - runtime.md#rt-rte-backend-synthesis
      - runtime.md#rt-rte-agent-completion
      - runtime.md#rt-obj-pending-prompts
      - memory.md#mem-rte-self-learn
      - runtime.md#rt-rte-reader-build
      - epistemic.md#epi-obj-reader-overview
      - memory.md#mem-obj-ingest-queue
      note: Requested read-back is established on several independent routes. Unresolved automatic surfaces
        prevent a completely assessed pull-only boundary; no supported push finding is invented.
    read_back_signal:
      assessment: not-determinable
      units:
      - scope: Completely assessed requested query/read/graph/quality and deferred pickup operations
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-mcp-access
        - memory.md#mem-rte-graph-query
        - memory.md#mem-rte-quality-inspection
        - runtime.md#rt-rte-host-ingest
        - runtime.md#rt-obj-pending-prompts
        - runtime.md#rt-rte-agent-completion
        note: These individual operations fulfill consumer requests, so their lexical, identity or judgment
          selectors are not push signals.
      - scope: Proposed SessionStart/queue and hot/special-file delivery
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-ingest-queue
        - memory.md#mem-obj-navigation
        note: No automatic push selector, actual selected retained parts or channel is established. Special
          filenames and queue paths alone cannot support identifier; scaffold availability cannot support
          coarse.
      records:
      - runtime.md#rt-rte-mcp-access
      - memory.md#mem-rte-graph-query
      - memory.md#mem-rte-quality-inspection
      - runtime.md#rt-rte-host-ingest
      - runtime.md#rt-obj-pending-prompts
      - runtime.md#rt-rte-agent-completion
      - memory.md#mem-obj-ingest-queue
      - memory.md#mem-obj-navigation
      note: No push-signal controlled value is established. Pull-only assessed units are locally inapplicable,
        but unresolved proposed push alternatives prevent making the axis inapplicable or absent.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatic session-to-source-page backend pipeline and deferred rendered-task chain
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-backend-synthesis
          - runtime.md#rt-obj-pending-prompts
          - runtime.md#rt-rte-agent-completion
          - memory.md#mem-obj-wiki
          note: Retained session traces automatically feed durable source-page/task context which later
            foreground/MCP invocations can consume; no improvement measurement is required.
        records:
        - runtime.md#rt-rte-backend-synthesis
        - runtime.md#rt-obj-pending-prompts
        - runtime.md#rt-rte-agent-completion
        - memory.md#mem-obj-wiki
        note: This is an architectural trace-fed write classification, not proof of model truth, completed
          agent work or exercised learning benefit.
      - scope: Routine foreground session ingestion
        assessment: known
        findings:
        - value: 'yes'
          basis: afforded
          records:
          - runtime.md#rt-rte-host-ingest
          - memory.md#mem-obj-wiki
          note: Model-mediated ingest automatically admits trace-derived durable pages for later knowledge
            use without per-content human approval.
        records:
        - runtime.md#rt-rte-host-ingest
        - memory.md#mem-obj-wiki
        note: The host instruction route is afforded, not observed.
      - scope: Optional metadata-fed reader overview
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-reader-build
          - epistemic.md#epi-obj-reader-overview
          note: Session-derived grouped metadata feeds automatically admitted prose persisted in reader
            HTML for later readers.
        records:
        - runtime.md#rt-rte-reader-build
        - epistemic.md#epi-obj-reader-overview
        note: Separate reader memory route; no claim that this output enters ordinary wiki query context
          or improves an agent.
      - scope: Human-approved self-learn method revision and permission-gated saved answers/reflection
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-self-learn
        - runtime.md#rt-rte-host-ingest
        - memory.md#mem-rte-wiki-maintenance
        - epistemic.md#epi-rte-wiki-reflection
        note: These explicitly human-approved admission mechanisms are outside the automatic-write
          condition of trace learning. This is not an evidenced absence of other automatic writes;
          the accepted set supplies no bounded absence record for a local no. Self-learn can still
          carry learning authority at its human-gated update consumer.
      - scope: Mixed non-session wiki sources, candidate initialization, quality writers and hot/Auto
          Dream/queue alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-wiki
        - runtime.md#rt-rte-candidate-admission
        - memory.md#mem-obj-quality-metadata
        - memory.md#mem-obj-navigation
        - memory.md#mem-obj-ingest-queue
        note: Original source/control and later consumer facts are unresolved. Raw-log retention or a
          cache label alone cannot decide whether an automatic durable behavior-shaping write exists.
      records:
      - runtime.md#rt-rte-backend-synthesis
      - runtime.md#rt-obj-pending-prompts
      - runtime.md#rt-rte-agent-completion
      - memory.md#mem-obj-wiki
      - runtime.md#rt-rte-host-ingest
      - runtime.md#rt-rte-reader-build
      - epistemic.md#epi-obj-reader-overview
      - memory.md#mem-rte-self-learn
      - memory.md#mem-rte-wiki-maintenance
      - epistemic.md#epi-rte-wiki-reflection
      - runtime.md#rt-rte-candidate-admission
      - memory.md#mem-obj-quality-metadata
      - memory.md#mem-obj-navigation
      - memory.md#mem-obj-ingest-queue
      note: Qualifying automatic trace-fed writes support yes locally. Explicitly human-gated admission
        mechanisms are locally inapplicable, not bounded absence findings. Unknown alternative admissions
        and consumers prevent complete trace-learning coverage.
    trace_source:
      assessment: partial
      units:
      - scope: Session-fed source-page generation, rendered pending tasks and routine host ingest
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - epistemic.md#epi-obj-raw-sessions
          - runtime.md#rt-rte-backend-synthesis
          - runtime.md#rt-obj-pending-prompts
          - runtime.md#rt-rte-agent-completion
          - memory.md#mem-obj-wiki
          note: The original inputs are recorded coding-session turns, not event streams merely because
            conversion stores dates or adapter records.
        - value: tool-traces
          basis: wired
          records:
          - epistemic.md#epi-obj-raw-sessions
          - runtime.md#rt-rte-session-conversion
          - memory.md#mem-obj-wiki
          - runtime.md#rt-rte-backend-synthesis
          note: Raw session material can include recorded tool output/previews consumed in the source-page
            trace-fed chain.
        - value: session-logs
          basis: afforded
          records:
          - runtime.md#rt-rte-host-ingest
          - memory.md#mem-obj-wiki
          note: Foreground ingest requests the converted session material.
        - value: tool-traces
          basis: afforded
          records:
          - runtime.md#rt-rte-host-ingest
          - memory.md#mem-obj-wiki
          note: The afforded host path can ingest the tool-preview portions of those retained session
            sources.
        records:
        - epistemic.md#epi-obj-raw-sessions
        - runtime.md#rt-rte-session-conversion
        - runtime.md#rt-rte-backend-synthesis
        - runtime.md#rt-obj-pending-prompts
        - runtime.md#rt-rte-agent-completion
        - memory.md#mem-obj-wiki
        - runtime.md#rt-rte-host-ingest
        note: Values describe supported input content; no guarantee every page contains both kinds, or
          that truncation preserves every tool result.
      - scope: Optional reader-overview trace-fed write
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - runtime.md#rt-rte-reader-build
          - epistemic.md#epi-obj-reader-overview
          note: Grouped project/session metadata and session slugs originate in recorded coding sessions;
            model input is metadata rather than full transcript/tool bodies.
        records:
        - runtime.md#rt-rte-reader-build
        - epistemic.md#epi-obj-reader-overview
        note: No tool-traces or event-streams value is inferred for this metadata-only branch.
      - scope: Human-approved self-learn, answer saving and reflection writes
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-self-learn
        - runtime.md#rt-rte-host-ingest
        - memory.md#mem-rte-wiki-maintenance
        - epistemic.md#epi-rte-wiki-reflection
        note: These scoped admissions do not qualify as automatic trace learning; transcript use by self-learn
          is not a trace_source finding for a nonqualifying write.
      - scope: Imported non-session sources and unresolved hot/cache/quality/candidate/queue learning
          alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-wiki
        - memory.md#mem-obj-navigation
        - memory.md#mem-obj-quality-metadata
        - runtime.md#rt-rte-candidate-admission
        - memory.md#mem-obj-ingest-queue
        note: Their original input content and qualifying automatic write/consumer chains are not fully
          established. Session adapter names do not resolve mixed provenance; no trajectories or event-streams
          value follows.
      records:
      - epistemic.md#epi-obj-raw-sessions
      - runtime.md#rt-rte-session-conversion
      - runtime.md#rt-rte-backend-synthesis
      - runtime.md#rt-obj-pending-prompts
      - runtime.md#rt-rte-agent-completion
      - memory.md#mem-obj-wiki
      - runtime.md#rt-rte-host-ingest
      - runtime.md#rt-rte-reader-build
      - epistemic.md#epi-obj-reader-overview
      - memory.md#mem-rte-self-learn
      - memory.md#mem-rte-wiki-maintenance
      - epistemic.md#epi-rte-wiki-reflection
      - memory.md#mem-obj-navigation
      - memory.md#mem-obj-quality-metadata
      - runtime.md#rt-rte-candidate-admission
      - memory.md#mem-obj-ingest-queue
      note: Session logs and recorded tool material support local source values. Nonqualifying manual
        routes are locally inapplicable; unresolved source/admission alternatives prevent system-wide
        complete source classification.
---

# llm-wiki memory profile

## Comparison rationale

This profile classifies retained objects and their actual consumers, not every
file or model used by the runtime. The supplied records establish filesystem
persistence and later-consumer routes, but leave several initial admissions,
special-cache routes and included variants unresolved. The positive findings
therefore do not claim exhaustive system coverage. No observed or causal basis
is assigned: the accepted members supply implementation and doctrine only.

### Objects, encoding and authority

Retained graph JSON is a file substrate with symbolic content, not evidence of a
graph database. Likewise a floating confidence field is symbolic metadata, not
parametric memory. Prose, exact fields and pending UUIDs have different consumers.
The rendered pending task gives the foreground agent directions/context; the
sentinel gives completion code an enforced association criterion. See
[MEM-RTE-graph-query](memory.md#mem-rte-graph-query),
[MEM-OBJ-quality-metadata](memory.md#mem-obj-quality-metadata),
[RT-OBJ-pending-prompts](runtime.md#rt-obj-pending-prompts) and
[RT-RTE-agent-completion](runtime.md#rt-rte-agent-completion).

Learning authority is local to the update consumer of retained experience.
Knowledge authority is local to the later reader of the resulting page. Human
approval of a self-learn diff changes write agency, not the transcript's role at
the revision consumer. The trace-learning axis instead requires automatic
admission. The manual self-learn unit can consequently carry learning authority
without a trace-learning yes. See
[MEM-RTE-self-learn](memory.md#mem-rte-self-learn),
[RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis) and
[MEM-OBJ-wiki](memory.md#mem-obj-wiki).

### Transformations and delivery

Summarization/excerpt reduction supports consolidation; it does not establish
novel claim synthesis. Opaque model outputs retain their semantic uncertainty.
Force replacement and candidate merge support evolution; promotion raises the
candidate tier. Archiving is bounded invalidation of trusted-area placement,
not corpus-wide suppression: recursive retrieval can still return archived
claims without their rejection reasons. See
[RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis),
[RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission),
[MEM-OBJ-candidate-archive](memory.md#mem-obj-candidate-archive) and
[MEM-CLM-archive-visibility](memory.md#mem-clm-archive-visibility).

MCP lexical matching, exact page paths, graph seed matches and foreground
relevance judgment occur inside requested read-back. They establish no push
signal. Pending prompts are picked up by an explicitly invoked procedure, not a
launched worker. The unresolved SessionStart/queue and hot-memory routes prevent
an exhaustive pull-only conclusion, so read-back signal is not-determinable
rather than globally inapplicable. See
[RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access),
[MEM-RTE-graph-query](memory.md#mem-rte-graph-query),
[RT-RTE-agent-completion](runtime.md#rt-rte-agent-completion),
[MEM-OBJ-ingest-queue](memory.md#mem-obj-ingest-queue) and
[MEM-OBJ-navigation](memory.md#mem-obj-navigation).

The optional reader overview is separately retained HTML derived from session
metadata. It is included as a trace-fed retained context route, without claiming
that it enters curated wiki Markdown or that a reader actually used it. Source
classification follows session origin, not the timestamped serialization or the
name of the synthesis operation. See
[EPI-OBJ-reader-overview](epistemic.md#epi-obj-reader-overview) and
[RT-RTE-reader-build](runtime.md#rt-rte-reader-build).

### Canonical identities and unresolved evidence layers

The supplied reconciliation supersedes EPI-OBJ-wiki-pages with
[MEM-OBJ-wiki](memory.md#mem-obj-wiki), and EPI-OBJ-quality-metadata with
[MEM-OBJ-quality-metadata](memory.md#mem-obj-quality-metadata). All classification
citations use those canonical identities. The supersessions change no values;
they retain unknown semantic fidelity and the distinction between transient
helper returns and persisted quality fields. The separate reader-overview object
and grouped quality/maintenance routes are not superseded.

The supplied reconciliation leaves maintenance implementation status disputed:
[MEM-RTE-wiki-maintenance](memory.md#mem-rte-wiki-maintenance) says afforded;
[EPI-RTE-page-update](epistemic.md#epi-rte-page-update) and
[EPI-RTE-wiki-reflection](epistemic.md#epi-rte-wiki-reflection) say claimed.
Relevant findings retain both bases instead of upgrading the claimed procedure.
Both accounts agree on direct update admission and approval-gated reflection,
and neither establishes execution. This limits a unified implementation verdict
without preventing the bounded classification above.

Initial candidate/custom navigation content, persisted confidence writers,
queue consumers and special-cache selectors remain unresolved. The coverage
limits carried by [MEM-OBJ-navigation](memory.md#mem-obj-navigation),
[MEM-OBJ-quality-metadata](memory.md#mem-obj-quality-metadata),
[MEM-OBJ-ingest-queue](memory.md#mem-obj-ingest-queue) and
[RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) prevent
stronger coverage assessments. Unread repair/vault/editor variants remain
included uncertainties rather than evidenced absences. No source files were
read for this mapping; only the supplied members and governing contracts were
used. No records, quotations or source evidence were added.
