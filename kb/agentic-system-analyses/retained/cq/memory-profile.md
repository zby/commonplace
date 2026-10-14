---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'CQ memory comparison: retained advice and access structures, optional embeddings, Cursor
  failure context and discovery caches; opaque alternatives remain local uncertainties.'
run-id: AAS-2026-10-14-cq-8fb3dc41c334-01
source-identity: https://github.com/mozilla-ai/cq
reviewed-boundary: 5765494a3840e5f5a7223c42101f41e85cb9d898
memory-comparison:
  version: 2
  scope: Retained knowledge-unit insight, metadata, flags and arbitrary extensions; domain/FTS access
    structures and optional SQLite vectors; built-in and injected-store admission, maintenance and query/review
    consumers; Cursor failure-context records and discovery NodeInfo caches accumulated through use. Includes
    unresolved initialization, application-specific extension consumption and custom-store alternatives.
    Excludes static shipped/installed prompts and manifests, credentials, external host/model/provider
    weights and context management, transient query embeddings, and reflection intermediates not shown
    to be durably retained.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Knowledge-unit insight, symbolic metadata, flags, extensions and domain/FTS access structures
          in inspected SQLite stores and remote SQL repository
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-insight
          - memory.md#mem-obj-selection-metadata
          - runtime.md#rt-rte-knowledge-query
          note: Local persistence/reload and the remote SQLite path retain units and their access structures.
        records:
        - memory.md#mem-obj-insight
        - memory.md#mem-obj-selection-metadata
        - memory.md#mem-obj-flags
        - memory.md#mem-obj-extensions
        - runtime.md#rt-rte-knowledge-query
        note: SQLite unit JSON, index rows and server SQL data are operative retained storage.
      - scope: SDK PostgreSQL knowledge records and domain-query alternative
        assessment: partial
        findings:
        - value: rdbms
          basis: wired
          records:
          - memory.md#mem-obj-insight
          - runtime.md#rt-rte-knowledge-query
          note: The SDK PostgreSQL path operates on retained database records.
        records:
        - memory.md#mem-obj-insight
        - runtime.md#rt-rte-knowledge-query
        note: PostgreSQL storage is identified, but the accepted records do not exhaustively trace its
          durability and mutation paths.
      - scope: Python in-memory store knowledge-unit alternative
        assessment: partial
        findings:
        - value: in-memory
          basis: wired
          records:
          - runtime.md#rt-rte-knowledge-query
          note: Python in-memory query selects units from dictionary values.
        records:
        - runtime.md#rt-rte-knowledge-query
        note: Dictionary-value selection is inspected; all mutations and persistence parity are not exhaustively
          covered.
      - scope: Injected custom Store implementations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-store-replacement
        - runtime.md#rt-rte-knowledge-query
        note: Interface injection is included; implementation substrate is not supplied or inspected.
      - scope: Optional retained knowledge-unit embeddings
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-knowledge-vectors
          note: Float32 embedding blobs are retained in knowledge_units_vec.
        records:
        - memory.md#mem-obj-knowledge-vectors
        note: The retained numerical output is SQLite storage, not the external provider weights.
      - scope: Cursor per-conversation failure record
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-obj-failure-record
          note: JSON is written to a conversation-keyed failure file.
        records:
        - runtime.md#rt-obj-failure-record
        - runtime.md#rt-rte-failure-reminder
        note: The bounded event state survives to a later stop hook.
      - scope: Discovery NodeInfo disk and resolver memo caches
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-node-info
          note: Optional address-keyed JSON files persist NodeInfo across resolver invocations.
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-node-info
          note: Successful NodeInfo is retained in the resolver memo until resolver disposal.
        records:
        - memory.md#mem-obj-node-info
        - memory.md#mem-rte-discovery-resolution
        note: Both cache levels are described; ephemeral memo lifetime differs from disk TTL.
      records:
      - memory.md#mem-obj-insight
      - memory.md#mem-obj-selection-metadata
      - memory.md#mem-obj-flags
      - memory.md#mem-obj-extensions
      - runtime.md#rt-rte-knowledge-query
      - memory.md#mem-rte-store-replacement
      - memory.md#mem-obj-knowledge-vectors
      - runtime.md#rt-obj-failure-record
      - runtime.md#rt-rte-failure-reminder
      - memory.md#mem-obj-node-info
      - memory.md#mem-rte-discovery-resolution
      note: Inventory includes unit payloads and access structures, optional vectors, auxiliary failure
        state and discovery caches. Custom-store substrate and full alternative-store persistence are
        unresolved; a wired SQLite witness does not cover them.
    representational_form:
      assessment: partial
      units:
      - scope: Knowledge insight at querying host and browser reviewer
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-insight
          - runtime.md#rt-rte-remote-review
          note: Host/reviewer consumers receive readable advice.
        records:
        - memory.md#mem-obj-insight
        - runtime.md#rt-rte-remote-review
        note: Summary/detail/action are interpreted as prose, not executed as code.
      - scope: Domains, context, confidence, identifiers, review state, domain/FTS access keys at fixed
          selectors
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-selection-metadata
          - runtime.md#rt-rte-knowledge-query
          note: Fixed selector/ranking predicates consume localized metadata.
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-insight
          - memory.md#mem-obj-selection-metadata
          - runtime.md#rt-rte-knowledge-query
          note: Retained insight text duplicated into FTS supplies lexical candidate gathering.
        records:
        - memory.md#mem-obj-selection-metadata
        - runtime.md#rt-rte-knowledge-query
        - runtime.md#rt-rte-remote-review
        note: Symbolic rules consume fields and index memberships; FTS source text remains separately
          classified as prose.
      - scope: Flags reason, timestamp and duplicate target at fixed feedback/storage consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-flags
          - runtime.md#rt-rte-knowledge-feedback
          note: Enum/time/reference fields use fixed construction and storage rules.
        records:
        - memory.md#mem-obj-flags
        - runtime.md#rt-rte-knowledge-feedback
        note: These fields are distinguished from optional explanatory detail; failed server/Python duplicate
          construction creates no retained part.
      - scope: Optional Go-local flag criticism delivered to a querying host
        assessment: partial
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-flags
          note: Optional detail is prose and can survive local serialized query delivery; arithmetic does
            not interpret its argument.
        records:
        - memory.md#mem-obj-flags
        - epistemic.md#epi-obj-evidence
        note: The container supports readable criticism and local delivery, but reconciliation retains
          the missing independent part declaration. Complete part-addressed coverage is not established.
      - scope: Arbitrary extension payload and application-specific consumption
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-extensions
        note: Namespaced JSON keys and transport are known; actual payload meaning and semantic consumer
          are not established.
      - scope: Knowledge-unit embeddings at numerical distance selector
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-knowledge-vectors
          note: Dense distributed numerical representation supplies similarity selection.
        records:
        - memory.md#mem-obj-knowledge-vectors
        - runtime.md#rt-rte-knowledge-query
        note: Numerical material is consumed for distance, not as readable reasons.
      - scope: Failure record structured fields and rendered error/input text
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-obj-failure-record
          - runtime.md#rt-rte-failure-reminder
          note: Fixed fields/key rules drive retention and rendering.
        - value: natural-language
          basis: wired
          records:
          - runtime.md#rt-obj-failure-record
          - runtime.md#rt-rte-failure-reminder
          note: Rendered bounded event strings supply host context.
        records:
        - runtime.md#rt-obj-failure-record
        - runtime.md#rt-rte-failure-reminder
        note: Split the fixed JSON/key mechanics from host interpretation of rendered strings.
      - scope: NodeInfo at discovery resolver and HTTP client
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-node-info
          - memory.md#mem-rte-discovery-resolution
          note: Compiled rules decode NodeInfo and use api_base_url.
        records:
        - memory.md#mem-obj-node-info
        - memory.md#mem-rte-discovery-resolution
        note: Fixed endpoint/version fields determine transport behavior.
      - scope: Injected-store additional operative parts
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-store-replacement
        - runtime.md#rt-rte-knowledge-query
        note: Only the Store contract is established; implementation-specific additional representations
          are not inspected.
      records:
      - memory.md#mem-obj-insight
      - runtime.md#rt-rte-remote-review
      - memory.md#mem-obj-selection-metadata
      - runtime.md#rt-rte-knowledge-query
      - memory.md#mem-obj-flags
      - runtime.md#rt-rte-knowledge-feedback
      - epistemic.md#epi-obj-evidence
      - memory.md#mem-obj-extensions
      - memory.md#mem-obj-knowledge-vectors
      - runtime.md#rt-obj-failure-record
      - runtime.md#rt-rte-failure-reminder
      - memory.md#mem-obj-node-info
      - memory.md#mem-rte-discovery-resolution
      - memory.md#mem-rte-store-replacement
      note: Known prose, symbolic and dense numerical paths coexist. Arbitrary extension semantics and
        the undeclared criticism part prevent a complete part-addressed inventory; injected-store payload
        alternatives remain uninspected.
    lineage:
      assessment: partial
      units:
      - scope: Ordinary caller-authored knowledge insight
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-insight
          - runtime.md#rt-rte-knowledge-proposal
          note: Caller supplies lesson prose to ordinary proposal.
        records:
        - memory.md#mem-obj-insight
        - runtime.md#rt-rte-knowledge-proposal
        note: Classification describes the supplied-text admission path, not the truth or provenance of
          every existing unit.
      - scope: Session-derived knowledge under the shipped reflection procedure
        assessment: known
        findings:
        - value: trace-extracted
          basis: afforded
          records:
          - runtime.md#rt-rte-session-reflection
          - memory.md#mem-obj-insight
          note: Requested session reasoning selects and rewrites events into candidate fields.
        records:
        - runtime.md#rt-rte-session-reflection
        - memory.md#mem-obj-insight
        note: Foreground-agent extraction is requested and can reach separate proposal persistence; no
          server extractor or executed session is established.
      - scope: Imported seed content, transferred local insight and legacy database content
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-insight
          - runtime.md#rt-rte-local-drain
          - memory.md#mem-rte-maintenance-migration
          note: Seed/caller content, local re-proposal and legacy migration bring existing material into
            a retained destination.
        records:
        - memory.md#mem-obj-insight
        - runtime.md#rt-rte-local-drain
        - memory.md#mem-rte-maintenance-migration
        note: Imported describes movement of existing content; it does not imply preservation of feedback
          history or source warrant.
      - scope: Generated metadata, indexes and supported feedback fields
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-selection-metadata
          - memory.md#mem-obj-flags
          note: Caller supplies tags/context and Go-local explanatory flag text.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-selection-metadata
          - runtime.md#rt-rte-knowledge-feedback
          note: Code creates IDs/default evidence, indexable domains and feedback arithmetic outputs.
        records:
        - memory.md#mem-obj-selection-metadata
        - memory.md#mem-obj-flags
        - runtime.md#rt-rte-knowledge-feedback
        note: Known code-derived fields coexist with caller-authored tags and optional criticism.
      - scope: Review status, reviewer and timestamp
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - runtime.md#rt-rte-remote-review
          - memory.md#mem-obj-selection-metadata
          note: Review request is compiled into retained status/reviewer/time.
        records:
        - runtime.md#rt-rte-remote-review
        - memory.md#mem-obj-selection-metadata
        note: The decision is external; software materializes status metadata.
      - scope: Subsequently generated knowledge vectors
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-knowledge-vectors
          note: Insight text is embedded and serialized through the provider-backed path.
        records:
        - memory.md#mem-obj-knowledge-vectors
        note: This unit is limited to the inspected insert/update derivation, not the initial population
          or provider provenance.
      - scope: Pre-existing vectors, stores and arbitrary extensions
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-knowledge-vectors
        - memory.md#mem-obj-extensions
        - memory.md#mem-rte-store-replacement
        note: Initial vector provenance, initialized store contents and actual extension authorship are
          not established; subsequent paths cannot resolve them.
      - scope: Cursor latest clipped failure record
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-obj-failure-record
          - runtime.md#rt-rte-failure-reminder
          note: A failure callback becomes formatted/clipped retained event content.
        records:
        - runtime.md#rt-obj-failure-record
        - runtime.md#rt-rte-failure-reminder
        note: The original host trace authenticity remains outside CQ; the local derivation is known.
      - scope: New discovery cache entries
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-node-info
          - memory.md#mem-rte-discovery-resolution
          note: Successful discovered endpoint metadata enters the cache.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-node-info
          - memory.md#mem-rte-discovery-resolution
          note: Documented 404 defaults are compiled into cached NodeInfo.
        records:
        - memory.md#mem-obj-node-info
        - memory.md#mem-rte-discovery-resolution
        note: This unit excludes unauthenticated initialization of old disk files.
      - scope: Pre-existing discovery disk-cache entries
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-node-info
        note: Source inspection does not authenticate the origin of existing cache files.
      records:
      - memory.md#mem-obj-insight
      - runtime.md#rt-rte-knowledge-proposal
      - runtime.md#rt-rte-session-reflection
      - runtime.md#rt-rte-local-drain
      - memory.md#mem-rte-maintenance-migration
      - memory.md#mem-obj-selection-metadata
      - memory.md#mem-obj-flags
      - runtime.md#rt-rte-knowledge-feedback
      - runtime.md#rt-rte-remote-review
      - memory.md#mem-obj-knowledge-vectors
      - memory.md#mem-obj-extensions
      - memory.md#mem-rte-store-replacement
      - runtime.md#rt-obj-failure-record
      - runtime.md#rt-rte-failure-reminder
      - memory.md#mem-obj-node-info
      - memory.md#mem-rte-discovery-resolution
      note: Known derivation paths do not authenticate initial stores, cache files, vector provenance
        or extension authorship. Interactive reflection is an affordance, not observed extraction.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Knowledge insight at querying host and browser reviewer
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-insight
          - runtime.md#rt-bap-knowledge-guidance
          note: Returned detail/action supplies reference and advice to the host.
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-insight
          - runtime.md#rt-rte-remote-review
          note: Browser reviewer reads the retained content before choosing a decision.
        records:
        - memory.md#mem-obj-insight
        - runtime.md#rt-rte-remote-review
        - runtime.md#rt-bap-knowledge-guidance
        note: Imperative action text is advice for the task, not standing host instructions or executable
          enforcement.
      - scope: Insight text, domains/context/confidence and retained vectors at query rankers
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-insight
          - memory.md#mem-obj-selection-metadata
          - memory.md#mem-obj-knowledge-vectors
          - runtime.md#rt-rte-knowledge-query
          note: Retained text, tags, confidence and numerical vectors affect priority of selected units.
        records:
        - memory.md#mem-obj-insight
        - memory.md#mem-obj-selection-metadata
        - memory.md#mem-obj-knowledge-vectors
        - runtime.md#rt-rte-knowledge-query
        note: Text and metadata drive lexical/relevance scoring; vectors drive distance preselection and
          final scoring. Benefit and truth are not implied.
      - scope: Remote review status at query gate and pending-status admission check
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-selection-metadata
          - runtime.md#rt-clm-approved-query
          note: Approved status permits ordinary remote delivery; nonapproved status excludes it.
        - value: validation
          basis: wired
          records:
          - runtime.md#rt-rte-remote-review
          note: Existing pending status is checked before a new review decision.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-rte-remote-review
          note: An already-reviewed status produces rejection of the review request.
        records:
        - memory.md#mem-obj-selection-metadata
        - runtime.md#rt-rte-remote-review
        - runtime.md#rt-clm-approved-query
        note: Query eligibility and eligibility for another review decision are separate consumers.
      - scope: Retained tier and identifiers at feedback/drain operation selectors
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-selection-metadata
          - runtime.md#rt-rte-knowledge-feedback
          - runtime.md#rt-rte-local-drain
          note: Tier/ID select local versus remote feedback and LOCAL units for drain.
        records:
        - memory.md#mem-obj-selection-metadata
        - runtime.md#rt-rte-knowledge-feedback
        - runtime.md#rt-rte-local-drain
        note: Only actually consumed metadata is assigned authority; timestamps and superseded_by receive
          none merely from storage.
      - scope: Optional Go-local explanatory criticism at host reader
        assessment: partial
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-flags
          note: Returned detail can supply criticism as context; score arithmetic does not judge its argument.
        records:
        - memory.md#mem-obj-flags
        - epistemic.md#epi-obj-evidence
        note: Prose can reach the host, but no independent criticism-part declaration resolves a complete
          part-addressed authority inventory.
      - scope: Arbitrary extensions at application-specific consumers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-extensions
        note: JSON transport is established, but no semantic consumer/effect licenses an authority value.
      - scope: Cursor failure strings at later host stop
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - runtime.md#rt-rte-failure-reminder
          note: The previous failure/tool/input text can inform later host reasoning.
        records:
        - runtime.md#rt-obj-failure-record
        - runtime.md#rt-rte-failure-reminder
        note: Automatic delivery supplies event context; actual corrective action remains unobserved.
      - scope: NodeInfo at HTTP destination construction
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-node-info
          - memory.md#mem-rte-discovery-resolution
          note: Retained api_base_url determines the operation destination.
        records:
        - memory.md#mem-obj-node-info
        - memory.md#mem-rte-discovery-resolution
        note: Endpoint reuse is transport behavior, not host instruction.
      - scope: Recorded session experience at requested reflection-to-candidate consumer
        assessment: known
        findings:
        - value: learning
          basis: afforded
          records:
          - runtime.md#rt-rte-session-reflection
          note: The foreground agent is asked to use session experience to produce candidate advice for
            later proposal and use.
        records:
        - runtime.md#rt-rte-session-reflection
        note: This is an afforded experience-to-durable-advice update path; downstream lesson knowledge
          is separately classified.
      - scope: Injected Store-specific consumers/effects
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-store-replacement
        - runtime.md#rt-rte-knowledge-query
        note: Custom-store internals are not supplied; fixed built-in witnesses cannot cover their additional
          effects.
      records:
      - memory.md#mem-obj-insight
      - runtime.md#rt-rte-remote-review
      - runtime.md#rt-bap-knowledge-guidance
      - memory.md#mem-obj-selection-metadata
      - memory.md#mem-obj-knowledge-vectors
      - runtime.md#rt-rte-knowledge-query
      - runtime.md#rt-clm-approved-query
      - runtime.md#rt-rte-knowledge-feedback
      - runtime.md#rt-rte-local-drain
      - memory.md#mem-obj-flags
      - epistemic.md#epi-obj-evidence
      - memory.md#mem-obj-extensions
      - runtime.md#rt-obj-failure-record
      - runtime.md#rt-rte-failure-reminder
      - memory.md#mem-obj-node-info
      - memory.md#mem-rte-discovery-resolution
      - runtime.md#rt-rte-session-reflection
      - memory.md#mem-rte-store-replacement
      note: Authority is classified at actual consumers, not from field names or model compliance. Opaque
        extensions/custom stores and missing criticism part declarations prevent complete coverage.
    write_agency:
      assessment: partial
      units:
      - scope: Interactive candidate approval/editing before proposal
        assessment: known
        findings:
        - value: manual
          basis: afforded
          records:
          - runtime.md#rt-rte-knowledge-proposal
          - runtime.md#rt-rte-session-reflection
          note: User approve/edit/skip selects the retained candidate content.
        records:
        - runtime.md#rt-rte-knowledge-proposal
        - runtime.md#rt-rte-session-reflection
        - runtime.md#rt-clm-proposal-approval
        note: Human decisions supply or approve specific content under the shipped procedure; invocation
          alone is not that decision.
      - scope: Headless agent proposal admission
        assessment: known
        findings:
        - value: automatic
          basis: afforded
          records:
          - runtime.md#rt-rte-knowledge-proposal
          - runtime.md#rt-clm-proposal-approval
          note: Headless model safety judgment can admit a clean/caveated proposal without user approval.
        records:
        - runtime.md#rt-rte-knowledge-proposal
        - runtime.md#rt-clm-proposal-approval
        note: No human per-content decision is required in the headless path; model admission remains
          instructed, not exercised.
      - scope: Generic direct proposal and Store content replacement caller
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-knowledge-proposal
        - memory.md#mem-rte-store-replacement
        note: Generic caller authorship or identity does not establish human versus computational per-content
          choice.
      - scope: Generated IDs/default evidence, supported feedback, drain, embeddings, indexes and format
          migration
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-selection-metadata
          - runtime.md#rt-rte-knowledge-feedback
          - runtime.md#rt-rte-local-drain
          - memory.md#mem-obj-knowledge-vectors
          - memory.md#mem-rte-maintenance-migration
          note: Compiled rules admit metadata, score/vector/index updates, transferred units and normalized
            legacy fields without individual human approval.
        records:
        - memory.md#mem-obj-selection-metadata
        - runtime.md#rt-rte-knowledge-feedback
        - runtime.md#rt-rte-local-drain
        - memory.md#mem-obj-knowledge-vectors
        - memory.md#mem-rte-maintenance-migration
        note: Software determines these retained changes after requests; starting an operation does not
          make its transformations manual.
      - scope: Browser review decision and automated seed review alternative
        assessment: known
        findings:
        - value: manual
          basis: afforded
          records:
          - runtime.md#rt-rte-remote-review
          note: Human browser reviewer chooses approve/reject for the presented unit.
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-remote-review
          note: Seed script approves and adjusts units through APIs.
        records:
        - runtime.md#rt-rte-remote-review
        note: Browser is a per-unit human affordance; seed approval is a separately wired programmatic
          mechanism.
      - scope: Generic JWT-bearing review API caller
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-remote-review
        note: Authentication does not establish human presence or decision agency.
      - scope: Cursor failure write and cache admission/cleanup
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-failure-reminder
          - memory.md#mem-rte-discovery-resolution
          note: Hook and resolver rules admit retained state without per-content human approval.
        records:
        - runtime.md#rt-rte-failure-reminder
        - memory.md#mem-rte-discovery-resolution
        note: Software selects and retains event snippets and decoded endpoint metadata.
      - scope: Pre-existing stores, vectors, caches and arbitrary extensions
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-store-replacement
        - memory.md#mem-obj-knowledge-vectors
        - memory.md#mem-obj-node-info
        - memory.md#mem-obj-extensions
        note: Initialization and actual extension admission principals are not established by later transformations.
      records:
      - runtime.md#rt-rte-knowledge-proposal
      - runtime.md#rt-rte-session-reflection
      - runtime.md#rt-clm-proposal-approval
      - memory.md#mem-rte-store-replacement
      - memory.md#mem-obj-selection-metadata
      - runtime.md#rt-rte-knowledge-feedback
      - runtime.md#rt-rte-local-drain
      - memory.md#mem-obj-knowledge-vectors
      - memory.md#mem-rte-maintenance-migration
      - runtime.md#rt-rte-remote-review
      - runtime.md#rt-rte-failure-reminder
      - memory.md#mem-rte-discovery-resolution
      - memory.md#mem-obj-node-info
      - memory.md#mem-obj-extensions
      note: Interactive per-content human choice is an affordance, not a universal software prerequisite.
        Known automatic maintenance is kept separate from unresolved generic caller control and initialized
        state.
    curation_operations:
      assessment: partial
      units:
      - scope: Local Store replacement of an existing unit
        assessment: known
        findings:
        - value: evolve
          basis: afforded
          records:
          - memory.md#mem-rte-store-replacement
          note: Update can revise an existing retained entry.
        records:
        - memory.md#mem-rte-store-replacement
        note: API capability replaces current content without edit history; no deployed content-editing
          workflow is inferred.
      - scope: Successful confirmation and supported flag score changes
        assessment: known
        findings:
        - value: promote
          basis: wired
          records:
          - runtime.md#rt-rte-knowledge-feedback
          - epistemic.md#epi-obj-evidence
          note: Confirmation raises confidence and hence selection salience.
        - value: decay
          basis: wired
          records:
          - runtime.md#rt-rte-knowledge-feedback
          - epistemic.md#epi-obj-evidence
          note: Successful flags lower confidence, without revoking review status.
        records:
        - runtime.md#rt-rte-knowledge-feedback
        - epistemic.md#epi-obj-evidence
        note: Stale/incorrect and Go-local duplicate paths are included; server/Python duplicate construction
          failures produce no retained update.
      - scope: Remote review rejection
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records:
          - runtime.md#rt-rte-remote-review
          note: Reject retains history/content but excludes ordinary remote retrieval.
        records:
        - runtime.md#rt-rte-remote-review
        note: Rejected content remains available to review readers while ordinary query reliance is withheld.
      - scope: Drain local-copy deletion and local Store physical withdrawal
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - runtime.md#rt-rte-local-drain
          - epistemic.md#epi-rte-store-deletion
          note: Successful local deletion forgets the retained local copy.
        records:
        - runtime.md#rt-rte-local-drain
        - epistemic.md#epi-rte-store-deletion
        note: Physical removal is distinct from review invalidation, which retains the payload.
      - scope: Cursor retained failure replacement and expiry
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-obj-failure-record
          - runtime.md#rt-rte-failure-reminder
          note: A later failure replaces the previous per-conversation record.
        - value: decay
          basis: wired
          records:
          - runtime.md#rt-rte-failure-reminder
          note: Stop clears the record and session-start sweeps expired files.
        records:
        - runtime.md#rt-obj-failure-record
        - runtime.md#rt-rte-failure-reminder
        note: Replacement changes existing retained state and cleanup forgets it. Clipping newly arriving
          event content is not classified as consolidation over retained memory.
      - scope: Discovery cache expiry and invalid-entry removal
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-obj-node-info
          - memory.md#mem-rte-discovery-resolution
          note: Expired or invalid disk entries are forgotten.
        records:
        - memory.md#mem-obj-node-info
        - memory.md#mem-rte-discovery-resolution
        note: Disk TTL is bounded; memo hits do not apply that TTL.
      - scope: Requested reflection lesson selection/deduplication and sanitization
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-session-reflection
        - runtime.md#rt-rte-knowledge-proposal
        note: Instructions request curation, but no actual retained-input transformation instance or CQ-owned
          implementation establishes its operation; novel synthesis cannot be inferred.
      - scope: Opaque extension/custom-store curation and pre-existing vector compatibility
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-extensions
        - memory.md#mem-rte-store-replacement
        - memory.md#mem-obj-knowledge-vectors
        note: Their implemented semantic transformations and regeneration policy are not inspected.
      records:
      - memory.md#mem-rte-store-replacement
      - runtime.md#rt-rte-knowledge-feedback
      - epistemic.md#epi-obj-evidence
      - runtime.md#rt-rte-remote-review
      - runtime.md#rt-rte-local-drain
      - epistemic.md#epi-rte-store-deletion
      - runtime.md#rt-obj-failure-record
      - runtime.md#rt-rte-failure-reminder
      - memory.md#mem-obj-node-info
      - memory.md#mem-rte-discovery-resolution
      - runtime.md#rt-rte-session-reflection
      - runtime.md#rt-rte-knowledge-proposal
      - memory.md#mem-obj-extensions
      - memory.md#mem-obj-knowledge-vectors
      note: Supported transformations include local replacement, visibility withdrawal, score salience
        changes and auxiliary cleanup. Requested reflection deduplication/sanitization is not treated
        as an implemented curation operation; opaque branches remain unresolved.
    read_back_direction:
      assessment: partial
      units:
      - scope: Knowledge query and requested review queue/get/list
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-knowledge-query
          - runtime.md#rt-rte-remote-review
          note: Callers request retained units; code returns matching knowledge or review content.
        records:
        - runtime.md#rt-rte-knowledge-query
        - runtime.md#rt-rte-remote-review
        note: Selection/ranking inside a requested return is not an additional push.
      - scope: Named-unit feedback reload and requested status views
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-knowledge-feedback
          - runtime.md#rt-rte-knowledge-query
          - memory.md#mem-obj-selection-metadata
          note: Requested feedback/status operations reload units or evidence for the caller.
        records:
        - runtime.md#rt-rte-knowledge-feedback
        - runtime.md#rt-rte-knowledge-query
        - memory.md#mem-obj-selection-metadata
        note: Retained unit/evidence reads serve the invoking operation; they do not automatically inject
          lessons into the host.
      - scope: Cursor stop reminder
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-failure-reminder
          note: Automatic conversation selector supplies the latest retained failure on hook stdout.
        records:
        - runtime.md#rt-rte-failure-reminder
        note: Stop is a lifecycle trigger, not a request for retained failure material.
      - scope: Discovery cache selection within a requested remote operation
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-node-info
          - memory.md#mem-rte-discovery-resolution
          note: Resolver memo/disk selectors deliver cached metadata to the HTTP client on an operation
            trigger.
        records:
        - memory.md#mem-obj-node-info
        - memory.md#mem-rte-discovery-resolution
        note: The outer remote operation is requested. Its resolver automatically supplies retained endpoint
          metadata rather than fulfilling a foreground request to read NodeInfo.
      - scope: Extension application consumers and additional injected-store read-back
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-extensions
        - memory.md#mem-rte-store-replacement
        - runtime.md#rt-rte-knowledge-query
        note: Transport capability does not establish application-specific interpretation or additional
          later consumers.
      records:
      - runtime.md#rt-rte-knowledge-query
      - runtime.md#rt-rte-remote-review
      - runtime.md#rt-rte-knowledge-feedback
      - memory.md#mem-obj-selection-metadata
      - runtime.md#rt-rte-failure-reminder
      - memory.md#mem-obj-node-info
      - memory.md#mem-rte-discovery-resolution
      - memory.md#mem-obj-extensions
      - memory.md#mem-rte-store-replacement
      note: Explicit advice/review requests are pull. Cursor stop delivery and resolver-selected cache
        metadata are push operations within different chains. Additional custom-store/application consumer
        routes remain unresolved.
    read_back_signal:
      assessment: partial
      units:
      - scope: Cursor stop selects retained failure by conversation identity
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-obj-failure-record
          - runtime.md#rt-rte-failure-reminder
          note: Conversation identity selects the file whose retained payload is printed.
        records:
        - runtime.md#rt-obj-failure-record
        - runtime.md#rt-rte-failure-reminder
        note: Trigger is stop; input is sanitized conversation key; delivered part is the latest bounded
          failure/error/input record.
      - scope: Remote-operation resolver selects cached NodeInfo by configured address
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-obj-node-info
          - memory.md#mem-rte-discovery-resolution
          note: Address-key equality selects the memo or address-keyed disk entry delivered to the HTTP
            client.
        records:
        - memory.md#mem-obj-node-info
        - memory.md#mem-rte-discovery-resolution
        note: Trigger is remote operation; input is normalized node address; selected retained part is
          matching NodeInfo. Memo precedence/disk TTL affect availability.
      - scope: Explicit knowledge/review/feedback/status pull operations
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-knowledge-query
        - runtime.md#rt-rte-remote-review
        - runtime.md#rt-rte-knowledge-feedback
        note: These operations fulfill requests for retained material; their lexical/embedding ranking
          is not a push signal.
      - scope: Opaque extension and injected-store additional delivery selectors
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-extensions
        - memory.md#mem-rte-store-replacement
        - runtime.md#rt-rte-knowledge-query
        note: No additional consumer selector is inspected; known pull routes cannot make these alternatives
          inapplicable.
      records:
      - runtime.md#rt-obj-failure-record
      - runtime.md#rt-rte-failure-reminder
      - memory.md#mem-obj-node-info
      - memory.md#mem-rte-discovery-resolution
      - runtime.md#rt-rte-knowledge-query
      - runtime.md#rt-rte-remote-review
      - runtime.md#rt-rte-knowledge-feedback
      - memory.md#mem-obj-extensions
      - memory.md#mem-rte-store-replacement
      note: Both established push selectors use an actual identity match. Availability, latest-record
        retention and expiry remain separate filters, not extra semantic or embedding signals. Unresolved
        consumer alternatives prevent complete coverage.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatic Cursor failure-event write to later stop context
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-obj-failure-record
          - runtime.md#rt-rte-failure-reminder
          note: Automatic trace-fed production creates retained context used by a later invocation.
        records:
        - runtime.md#rt-obj-failure-record
        - runtime.md#rt-rte-failure-reminder
        note: Formatted/clipped event material is retained and supplies later host context. Event-to-record-to-stop
          wiring is sufficient; a generalized lesson or observed improvement is not required.
      - scope: Interactive reflection session-to-proposal chain
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-session-reflection
        - runtime.md#rt-rte-knowledge-proposal
        note: Session extraction and later persistence are afforded, but the specified interactive path
          requires human content approval and actual host reasoning is unobserved. It establishes no qualifying
          automatic write or bounded system-wide no.
      - scope: Headless candidate generation and asserted-experience feedback
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-knowledge-proposal
        - runtime.md#rt-rte-knowledge-feedback
        - runtime.md#rt-rte-session-reflection
        note: Headless admission and automatic score changes are supported, but no accepted record identifies
          an original trace input actually consumed by these updates. Caller assertions are not themselves
          a recorded session/tool trace.
      - scope: Embedding, transport-cache and imported/initialized custom-store alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-knowledge-vectors
        - memory.md#mem-obj-node-info
        - memory.md#mem-rte-store-replacement
        - memory.md#mem-obj-extensions
        note: Known vector input is insight text and known cache input is endpoint discovery metadata;
          these facts do not establish qualifying trace-fed learning. Opaque initial/custom inputs prevent
          a complete negative.
      records:
      - runtime.md#rt-obj-failure-record
      - runtime.md#rt-rte-failure-reminder
      - runtime.md#rt-rte-session-reflection
      - runtime.md#rt-rte-knowledge-proposal
      - runtime.md#rt-rte-knowledge-feedback
      - memory.md#mem-obj-knowledge-vectors
      - memory.md#mem-obj-node-info
      - memory.md#mem-rte-store-replacement
      - memory.md#mem-obj-extensions
      note: A clipped retained failure context qualifies under the profile definition without diagnosis
        or benefit. Interactive reflection lacks automatic per-content admission; headless/opaque experience
        routes and custom alternatives do not establish a complete trace-fed-write inventory.
    trace_source:
      assessment: partial
      units:
      - scope: Cursor qualifying failure-context write
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records:
          - runtime.md#rt-obj-failure-record
          - runtime.md#rt-rte-failure-reminder
          note: Tool input/error feedback is the actual content used in retained failure context.
        - value: event-streams
          basis: wired
          records:
          - runtime.md#rt-obj-failure-record
          - runtime.md#rt-rte-failure-reminder
          note: The failure hook callback supplies the discrete runtime event consumed by the automatic
            write.
        records:
        - runtime.md#rt-obj-failure-record
        - runtime.md#rt-rte-failure-reminder
        note: Original input records a tool failure, including tool name, formatted request/input and
          error; callback origin also identifies a discrete runtime event.
      - scope: Interactive reflection and headless/asserted-experience update alternatives
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-session-reflection
        - runtime.md#rt-rte-knowledge-proposal
        - runtime.md#rt-rte-knowledge-feedback
        note: Session conversational and tool content is described for requested reflection, but qualifying
          automatic trace-fed admission is not established for that path; feedback input origin remains
          opaque.
      - scope: Initialized/custom/extension input alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-store-replacement
        - memory.md#mem-obj-extensions
        - memory.md#mem-obj-knowledge-vectors
        note: No original trace content for an additional qualifying automatic write is inspected. This
          axis cannot be made inapplicable from known nontrace inputs alone.
      records:
      - runtime.md#rt-obj-failure-record
      - runtime.md#rt-rte-failure-reminder
      - runtime.md#rt-rte-session-reflection
      - runtime.md#rt-rte-knowledge-proposal
      - runtime.md#rt-rte-knowledge-feedback
      - memory.md#mem-rte-store-replacement
      - memory.md#mem-obj-extensions
      - memory.md#mem-obj-knowledge-vectors
      note: The qualifying automatic failure-context write consumes a tool-failure callback. Requested
        reflection separately identifies session and tool content, but its automatic qualification is
        unresolved; do not aggregate those as positive trace sources.
---

# CQ memory profile

## Comparison rationale

This profile classifies the supplied accepted records, not live operation. Wiring establishes capacity; neither host adherence nor benefit is observed. Static installed guidance is excluded because it is shipped configuration rather than memory accumulated through use. External embedding-provider parameters are excluded; the retained numerical outputs remain included. [MEM-OBJ-knowledge-vectors](memory.md#mem-obj-knowledge-vectors) and [RT-RTE-host-installation](runtime.md#rt-rte-host-installation) delimit those surfaces.

The insight supersession resolves EPI-OBJ-insight to [MEM-OBJ-insight](memory.md#mem-obj-insight). All classifications use that canonical identity. The combined [EPI-OBJ-evidence](epistemic.md#epi-obj-evidence), [MEM-OBJ-selection-metadata](memory.md#mem-obj-selection-metadata) and [MEM-OBJ-flags](memory.md#mem-obj-flags) remain overlapping containers, not synonyms. Optional prose criticism is supported locally, but its missing independent declaration prevents a complete part-addressed inventory. The profile preserves that limitation in form and authority rather than either inventing a record or dropping the prose finding. Store replacement and [EPI-RTE-store-deletion](epistemic.md#epi-rte-store-deletion) likewise remain different scopes, with an afforded edit capability and wired physical deletion.

Advice is knowledge at the host, while the same text can be ranking input at the FTS/relevance consumer. Imperative wording does not make task advice standing instruction. Review status enforces query eligibility and validates a further review request; approval is not a tier promotion or evidence of truth. Confirmation raises salience and supported flags downweight it. Server/Python duplicate requests that fail construction establish no retained objection, deduplication or changed score. [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query), [RT-RTE-remote-review](runtime.md#rt-rte-remote-review), [RT-RTE-knowledge-feedback](runtime.md#rt-rte-knowledge-feedback).

Requested retrieval is pull even when code ranks or delivers its results. The Cursor stop hook supplies an identity-selected failure without a request for that memory. Resolver cache selection is another automatic supply operation, internal to an explicitly requested remote call: address identity selects retained NodeInfo for the HTTP client. This does not make the returned knowledge query another push. [RT-RTE-failure-reminder](runtime.md#rt-rte-failure-reminder), [MEM-RTE-discovery-resolution](memory.md#mem-rte-discovery-resolution).

The Cursor chain qualifies as trace learning in the comparison contract: a tool-failure event automatically produces bounded retained context for a later invocation. It need not generate a diagnosis or prove improvement. Its source content is tool feedback and its origin is a runtime callback event. The requested interactive session-to-lesson path has a distinct human content decision, and headless proposal/feedback records do not expose an actual trace-fed input chain. They therefore cannot be upgraded by the Cursor witness. Reflection's requested session/tool sources are not counted as positive sources of a qualifying automatic update. [RT-OBJ-failure-record](runtime.md#rt-obj-failure-record), [RT-RTE-failure-reminder](runtime.md#rt-rte-failure-reminder), [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection), [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal).

No accepted bounded-absence record licenses a system-wide trace-learning negative or an exhaustive absence of additional curation. Index rebuilding, vector regeneration and identity collisions alone are not curation operations. Transfer imports existing prose and forgets the local copy, but does not consolidate feedback history or preserve global identity. Initial store/cache/vector provenance, arbitrary extension meaning, full alternative-store mutation parity and custom-store internals prevent stronger inventory assessments. [RT-RTE-local-drain](runtime.md#rt-rte-local-drain), [MEM-RTE-maintenance-migration](memory.md#mem-rte-maintenance-migration), [MEM-OBJ-extensions](memory.md#mem-obj-extensions), [MEM-OBJ-knowledge-vectors](memory.md#mem-obj-knowledge-vectors).

Source-read log: none. Classification used only the supplied members and contracts; no source ambiguity required a direct frozen-source read.
