---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Hyalo memory comparison: mutable Markdown, derived access products, retained configuration
  and optional review artifacts at the frozen revision.'
run-id: AAS-2026-10-14-hyalo-ffe11d6a6d56-01
source-identity: https://github.com/ractive/hyalo
reviewed-boundary: 697f215fe8a90a5c760fceb686f2a321c9db7221
memory-comparison:
  version: 2
  scope: Retained vault body/frontmatter changed or accumulated through use; derived snapshot entries/graph/BM25
    and generated navigation; mutable configuration controlling later commands; optionally caller-retained
    Jev evidence/policy/results and prescribed trace-informed repairs. Include untraced mutation, OKF/log/changelog
    and maintenance alternatives as unresolved units. Exclude static shipped/installed instructions and
    code, current-request state unless captured for reuse, external host conversation/Claude memory persistence
    and provider model weights/state. External signals may feed included repairs without becoming Hyalo-owned
    stores.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Durable vault body, frontmatter and generated navigation regions
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-body
          - memory.md#mem-obj-frontmatter
          - memory.md#mem-obj-managed-region
          - memory.md#mem-rte-navigation-generation
          note: Markdown files retain the corpus and generated regions.
        records: *id001
        note: File persistence is established for these parts; caller-owned vault is not a repository
          substrate merely because tidy can consult Git.
      - scope: Extracted index/graph and BM25 postings, including loaded process copies
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id002
          - memory.md#mem-obj-index-entry
          - memory.md#mem-obj-bm25
          - memory.md#mem-rte-snapshot-lifecycle
          note: The binary snapshot retains extracted entries and lexical postings.
        - value: in-memory
          basis: wired
          records: *id002
          note: Loaded entries, graph and postings are operative process state.
        records: *id002
        note: Encoding is symbolic; binary serialization does not imply a database or vector substrate.
      - scope: Mutable type/schema/view configuration
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id003
          - runtime.md#rt-rte-config-install
          note: Configuration publication persists .hyalo.toml for later command loading.
        records: *id003
        note: Traced type/view configuration is file-backed; installed static assets are excluded.
      - scope: Optionally captured Jev manifest parts and classification results
        assessment: partial
        findings:
        - value: files
          basis: afforded
          records:
          - runtime.md#rt-obj-manifest
          - runtime.md#rt-rte-jev-suggestions
          - epistemic.md#epi-obj-classification-results
          note: Caller-captured JSON files can preserve evidence, policy and decisions for review.
        records:
        - runtime.md#rt-obj-manifest
        - runtime.md#rt-obj-document-content
        - epistemic.md#epi-obj-category-rubrics
        - epistemic.md#epi-obj-classification-results
        - runtime.md#rt-rte-jev-suggestions
        note: Optional file capture is established, but actual retention and later reuse are unknown.
          Request-local process objects alone are not accumulated memory.
      - scope: Included OKF/log/changelog and remaining maintenance outputs
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-body
        - memory.md#mem-obj-managed-region
        - runtime.md#rt-rte-config-install
        - runtime.md#rt-rte-tidy-review
        note: Their Markdown surface is included, but detailed retained output inventory and specialized
          consumers are uninspected.
      records:
      - memory.md#mem-obj-body
      - memory.md#mem-obj-frontmatter
      - memory.md#mem-obj-managed-region
      - memory.md#mem-rte-navigation-generation
      - memory.md#mem-obj-index-entry
      - memory.md#mem-obj-bm25
      - memory.md#mem-rte-snapshot-lifecycle
      - runtime.md#rt-rte-config-install
      - runtime.md#rt-obj-manifest
      - runtime.md#rt-obj-document-content
      - epistemic.md#epi-obj-category-rubrics
      - epistemic.md#epi-obj-classification-results
      - runtime.md#rt-rte-jev-suggestions
      - runtime.md#rt-rte-tidy-review
      note: Files and operative in-memory access products are positive witnesses. Optional helper artifact
        retention and untraced output inventory prevent complete coverage; external provider weights/state
        and host transcripts are excluded, not classified as Hyalo memory.
    representational_form:
      assessment: partial
      units:
      - scope: Vault prose delivered through read and Jev evidence copy
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id004
          - memory.md#mem-obj-body
          - runtime.md#rt-rte-query-read
          - runtime.md#rt-obj-document-content
          note: Humans/models interpret retained body assertions returned by read or copied into Jev input.
        records: *id004
        note: This classifies the prose path, not every possible user corpus payload.
      - scope: Frontmatter filter path and extracted graph/index/BM25 consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id005
          - memory.md#mem-obj-frontmatter
          - memory.md#mem-obj-index-entry
          - memory.md#mem-obj-bm25
          - memory.md#mem-bap-metadata-selection
          note: Parsed properties, task/link/outline fields and localized postings have fixed code consumers.
        records: *id005
        note: BM25 statistics are localized symbolic retrieval state, not distributed-parametric memory.
      - scope: Generated navigation display and managed-region splice paths
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id006
          - memory.md#mem-obj-managed-region
          - memory.md#mem-rte-navigation-generation
          note: Displayed headings and tables provide readable navigation.
        - value: symbolic
          basis: wired
          records: *id006
          note: Markers control owned byte regions and links identify source notes.
        records: *id006
        note: Display and splice consumers remain separate findings on the same retained region.
      - scope: Mutable configuration at deterministic CLI consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id007
          - runtime.md#rt-rte-config-install
          note: Constraints, defaults and view filters govern fixed command behavior.
        records: *id007
        note: No parametric update is established by configuration publication.
      - scope: 'Optional saved Jev artifacts: control/results versus interpreted evidence/rubrics'
        assessment: partial
        findings:
        - value: symbolic
          basis: afforded
          records:
          - runtime.md#rt-obj-manifest
          - epistemic.md#epi-obj-classification-results
          - runtime.md#rt-rte-jev-suggestions
          note: Captured hashes, labels, mappings and decisions preserve fixed-consumer controls.
        - value: natural-language
          basis: afforded
          records:
          - runtime.md#rt-obj-document-content
          - epistemic.md#epi-obj-category-rubrics
          - runtime.md#rt-rte-jev-suggestions
          note: Captured body text and category descriptions retain interpreted evidence and guidance.
        records:
        - runtime.md#rt-obj-manifest
        - runtime.md#rt-obj-document-content
        - epistemic.md#epi-obj-category-rubrics
        - epistemic.md#epi-obj-classification-results
        - runtime.md#rt-rte-jev-suggestions
        note: Forms are established for named parts; whether these optional artifacts become accumulated
          memory remains unresolved.
      - scope: Other corpus payloads and untraced log/profile output parts
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-body
        - memory.md#mem-obj-managed-region
        - runtime.md#rt-rte-config-install
        note: Actual corpus can contain logs, guidance or code; detailed remaining output parts and consumption
          paths are not inventoried.
      records:
      - memory.md#mem-obj-body
      - runtime.md#rt-rte-query-read
      - runtime.md#rt-obj-document-content
      - memory.md#mem-obj-frontmatter
      - memory.md#mem-obj-index-entry
      - memory.md#mem-obj-bm25
      - memory.md#mem-bap-metadata-selection
      - memory.md#mem-obj-managed-region
      - memory.md#mem-rte-navigation-generation
      - runtime.md#rt-rte-config-install
      - runtime.md#rt-obj-manifest
      - epistemic.md#epi-obj-category-rubrics
      - epistemic.md#epi-obj-classification-results
      - runtime.md#rt-rte-jev-suggestions
      note: 'Mixed objects are split by consumer. No parametric finding follows from the external models:
        their weights are not retained use-derived Hyalo memory. Uninspected payloads prevent a complete
        form inventory.'
    lineage:
      assessment: partial
      units:
      - scope: Initial vault prose/frontmatter provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-body
        - memory.md#mem-obj-frontmatter
        note: Initial human/agent authorship and import paths are not authenticated; subsequent metadata
          transformations do not resolve initialization.
      - scope: Extracted entries/graph and lexical postings
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id008
          - memory.md#mem-obj-index-entry
          - memory.md#mem-obj-bm25
          - memory.md#mem-rte-snapshot-lifecycle
          note: Scanning, property extraction and tokenization mechanically derive access products from
            corpus state.
        records: *id008
        note: These inputs are documents, not established interaction traces.
      - scope: Traced MADR navigation region derivation
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id009
          - memory.md#mem-obj-managed-region
          - memory.md#mem-rte-navigation-generation
          note: Collected ADR entries are rendered and spliced into a generated navigation region.
        records: *id009
        note: Links and display summaries derive from source ADRs; their original authorship remains separate.
      - scope: Mutable configuration and rule-derived metadata updates
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - runtime.md#rt-rte-config-install
          - epistemic.md#epi-rte-metadata-repair
          note: Defaults, path conventions and repair rules generate subsequent note values.
        records:
        - runtime.md#rt-rte-config-install
        - epistemic.md#epi-rte-metadata-repair
        - memory.md#mem-obj-frontmatter
        note: Rule-generated downstream values are established; initial configuration author and caller-assignment
          provenance remain unresolved.
      - scope: Optional Jev evidence copy and result production
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-body
          - runtime.md#rt-obj-document-content
          - runtime.md#rt-rte-jev-suggestions
          note: Selected corpus body/section text is copied into the manifest; this is not authenticated
            original corpus provenance.
        records:
        - runtime.md#rt-obj-manifest
        - runtime.md#rt-obj-document-content
        - epistemic.md#epi-obj-category-rubrics
        - epistemic.md#epi-obj-classification-results
        - runtime.md#rt-rte-jev-suggestions
        note: The copied evidence path is known. Initial policy provenance, saved-result retention and
          semantic result derivation remain unresolved; model output alone does not establish trace-extracted
          lineage.
      - scope: Trace-informed tidy repairs
        assessment: partial
        findings:
        - value: trace-extracted
          basis: claimed
          records:
          - runtime.md#rt-rte-tidy-review
          note: The instructed agent uses Git/task/recent-activity evidence to derive retained maintenance
            changes.
        records:
        - runtime.md#rt-rte-tidy-review
        - memory.md#mem-obj-frontmatter
        - memory.md#mem-obj-body
        note: The claim concerns the prescribed repair path, not snapshot construction or static shipped
          guidance. Actual repair instances and retained reasons are unobserved.
      - scope: OKF-specific navigation/logs, changelog and remaining mutation derivations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-managed-region
        - memory.md#mem-obj-body
        - runtime.md#rt-rte-config-install
        - runtime.md#rt-rte-tidy-review
        note: Separate generator selectors and log/release derivation paths are uninspected; MADR does
          not resolve them.
      records:
      - memory.md#mem-obj-body
      - memory.md#mem-obj-frontmatter
      - memory.md#mem-obj-index-entry
      - memory.md#mem-obj-bm25
      - memory.md#mem-rte-snapshot-lifecycle
      - memory.md#mem-obj-managed-region
      - memory.md#mem-rte-navigation-generation
      - runtime.md#rt-rte-config-install
      - epistemic.md#epi-rte-metadata-repair
      - runtime.md#rt-obj-manifest
      - runtime.md#rt-obj-document-content
      - epistemic.md#epi-obj-category-rubrics
      - epistemic.md#epi-obj-classification-results
      - runtime.md#rt-rte-jev-suggestions
      - runtime.md#rt-rte-tidy-review
      note: Known derivative paths coexist with unknown initialization. Tidy supports a claimed trace-derived
        branch; it is not promoted to wired operation or generalized to arbitrary corpus contents.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retained prose at explicit read and Jev evidence consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id010
          - memory.md#mem-obj-body
          - runtime.md#rt-rte-query-read
          - runtime.md#rt-obj-document-content
          - runtime.md#rt-rte-jev-suggestions
          note: Read supplies context/reference to the foreground agent; Jev consumes selected body text
            as classification evidence.
        records: *id010
        note: Delivery establishes a context route, not reliable compliance or source truth.
      - scope: Metadata and structural access fields at filters and link traversal
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id011
          - memory.md#mem-obj-frontmatter
          - memory.md#mem-obj-index-entry
          - memory.md#mem-bap-metadata-selection
          - runtime.md#rt-rte-query-read
          - epistemic.md#epi-rte-link-admission
          note: Properties, paths and graph/link identities select scope, operations or reachable inputs.
        records: *id011
        note: This is code-level selection, not standing model instruction.
      - scope: Lexical postings/text-derived retrieval features at ranked find
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id012
          - memory.md#mem-obj-bm25
          - runtime.md#rt-rte-query-read
          note: Retained tokens and statistics influence relative query-result order.
        records: *id012
        note: Fixed BM25 scoring still gives retained features ranking authority.
      - scope: Mutable schema and view configuration
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id013
          - runtime.md#rt-rte-config-install
          - runtime.md#rt-rte-property-write
          - epistemic.md#epi-rte-metadata-repair
          note: Configured constraints provide criteria for candidate properties.
        - value: enforcement
          basis: wired
          records: *id013
          note: Active assigned-property checks can refuse covered writes.
        - value: routing
          basis: wired
          records: *id013
          note: Views, type bindings and defaults select command scope and rule application.
        records: *id013
        note: Forces are consumer-local. Optional set validation is not a whole-document or all-writer
          guarantee.
      - scope: Generated navigation at later Markdown readers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id014
          - memory.md#mem-obj-managed-region
          - memory.md#mem-rte-navigation-generation
          note: Persisted navigation displays reference information linking readers to source notes.
        - value: routing
          basis: wired
          records: *id014
          note: Navigation links provide source-note destinations for subsequent reads.
        records: *id014
        note: No autonomous special TOC consumer or rationale acceptance is inferred.
      - scope: Optional retained Jev controls, rubrics and decisions
        assessment: partial
        findings:
        - value: instruction
          basis: afforded
          records:
          - epistemic.md#epi-obj-category-rubrics
          - runtime.md#rt-obj-manifest
          - runtime.md#rt-rte-jev-suggestions
          note: Saved category descriptions can supply standing local classification criteria on later
            reuse.
        - value: validation
          basis: afforded
          records:
          - runtime.md#rt-obj-manifest
          - runtime.md#rt-rte-jev-suggestions
          note: Saved policy labels and fingerprints provide helper consistency criteria.
        - value: enforcement
          basis: afforded
          records:
          - runtime.md#rt-obj-manifest
          - runtime.md#rt-rte-jev-suggestions
          note: Envelope validation can veto inconsistent supplied inputs.
        - value: routing
          basis: afforded
          records:
          - runtime.md#rt-obj-manifest
          - runtime.md#rt-rte-jev-suggestions
          note: Saved selections and type-folder mappings determine eligible evidence and filing suggestions.
        - value: knowledge
          basis: afforded
          records:
          - epistemic.md#epi-obj-classification-results
          - runtime.md#rt-rte-jev-suggestions
          note: Saved decisions can provide advisory repair evidence for review.
        records:
        - runtime.md#rt-obj-manifest
        - epistemic.md#epi-obj-category-rubrics
        - epistemic.md#epi-obj-classification-results
        - runtime.md#rt-rte-jev-suggestions
        note: Consumer mechanics are wired, but accumulation through optional capture/reuse is only afforded.
          Request-local guidance alone is excluded; no actual reuse is observed.
      - scope: Git/task/activity evidence at instructed tidy update consumer
        assessment: partial
        findings:
        - value: learning
          basis: claimed
          records:
          - runtime.md#rt-rte-tidy-review
          note: Retained activity evidence is prescribed input to agent-produced durable maintenance changes
            for later reads.
        records:
        - runtime.md#rt-rte-tidy-review
        - memory.md#mem-obj-frontmatter
        - memory.md#mem-obj-body
        note: This is learning authority at the trace-fed update consumer; output metadata has separate
          routing/knowledge paths. It establishes neither improved capacity nor automatic method revision.
      - scope: Untraced retained payloads and specialized consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-body
        - memory.md#mem-obj-managed-region
        - runtime.md#rt-rte-config-install
        - runtime.md#rt-rte-tidy-review
        note: Actual corpus guidance, log/release consumers and remaining rule consumers are not completely
          inspected.
      records:
      - memory.md#mem-obj-body
      - runtime.md#rt-rte-query-read
      - runtime.md#rt-obj-document-content
      - runtime.md#rt-rte-jev-suggestions
      - memory.md#mem-obj-frontmatter
      - memory.md#mem-obj-index-entry
      - memory.md#mem-bap-metadata-selection
      - epistemic.md#epi-rte-link-admission
      - memory.md#mem-obj-bm25
      - runtime.md#rt-rte-config-install
      - runtime.md#rt-rte-property-write
      - epistemic.md#epi-rte-metadata-repair
      - memory.md#mem-obj-managed-region
      - memory.md#mem-rte-navigation-generation
      - runtime.md#rt-obj-manifest
      - epistemic.md#epi-obj-category-rubrics
      - epistemic.md#epi-obj-classification-results
      - runtime.md#rt-rte-tidy-review
      note: Knowledge, routing, ranking, validation and enforcement have local code witnesses; optional
        saved rubrics add afforded instruction and tidy adds claimed learning authority. Static installed
        instructions are excluded from the accumulated-memory boundary. Missing payload/consumer coverage
        prevents a complete union.
    write_agency:
      assessment: partial
      units:
      - scope: Snapshot extraction, patch and persistent publication
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id015
          - memory.md#mem-rte-snapshot-lifecycle
          - memory.md#mem-obj-index-entry
          - memory.md#mem-obj-bm25
          note: Code admits extracted entries/postings without per-entry human approval.
        records: *id015
        note: A caller requesting a rebuild does not manually admit each product.
      - scope: MADR managed-region generation and lint rule-generated metadata repair
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id016
          - memory.md#mem-rte-navigation-generation
          - epistemic.md#epi-rte-metadata-repair
          note: Software generates and admits navigation rows or repaired values in apply mode without
            per-content human decisions.
        records: *id016
        note: Apply choice is workflow control, distinct from content admission.
      - scope: Routine instructed tidy repair admission
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records: &id017
          - runtime.md#rt-rte-tidy-review
          note: The foreground agent selects routine changes within an authorized request; the user does
            not approve each change.
        records: *id017
        note: This is claimed model admission under workflow instructions, not an enforced human review
          gate.
      - scope: Caller-assigned metadata, removal, configuration and initial body edits
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-property-write
        - memory.md#mem-rte-metadata-withdrawal
        - runtime.md#rt-rte-config-install
        - memory.md#mem-obj-body
        - memory.md#mem-obj-frontmatter
        note: Generic caller identity does not distinguish a human supplying/approving the content from
          an agent invoking the same command. No manual finding follows from CLI access alone.
      - scope: Optional Jev artifact capture and initial policy admission
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-manifest
        - epistemic.md#epi-obj-category-rubrics
        - epistemic.md#epi-obj-classification-results
        - runtime.md#rt-rte-jev-suggestions
        note: Caller capture is explicit, but caller identity and per-content approval are unresolved;
          provider proposals do not themselves persist corpus updates.
      - scope: Remaining mutation/log/release and OKF generator admission mechanisms
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-body
        - memory.md#mem-obj-managed-region
        - runtime.md#rt-rte-config-install
        - runtime.md#rt-rte-tidy-review
        note: Detailed handlers are not fully inspected; known software admission elsewhere does not settle
          these mechanisms.
      records:
      - memory.md#mem-rte-snapshot-lifecycle
      - memory.md#mem-obj-index-entry
      - memory.md#mem-obj-bm25
      - memory.md#mem-rte-navigation-generation
      - epistemic.md#epi-rte-metadata-repair
      - runtime.md#rt-rte-tidy-review
      - runtime.md#rt-rte-property-write
      - memory.md#mem-rte-metadata-withdrawal
      - runtime.md#rt-rte-config-install
      - memory.md#mem-obj-body
      - memory.md#mem-obj-frontmatter
      - runtime.md#rt-obj-manifest
      - epistemic.md#epi-obj-category-rubrics
      - epistemic.md#epi-obj-classification-results
      - runtime.md#rt-rte-jev-suggestions
      - memory.md#mem-obj-managed-region
      note: Automatic derivation/admission is supported locally. Initial authorization and physical publication
        do not establish manual content admission. Caller-assigned and untraced mechanisms retain uncertainty.
    curation_operations:
      assessment: partial
      units:
      - scope: Rule-generated revisions to existing frontmatter
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id018
          - epistemic.md#epi-rte-metadata-repair
          - memory.md#mem-obj-frontmatter
          note: Lint metadata repair revises existing properties, including nearest-enum and date normalization.
        records: *id018
        note: This is implemented entry revision, independent of factual correctness or acceptance.
      - scope: Regeneration of an existing MADR managed region
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id019
          - memory.md#mem-rte-navigation-generation
          - memory.md#mem-obj-managed-region
          note: Generation replaces an owned retained navigation region while preserving outside prose.
        records: *id019
        note: The mapped operation is existing-region revision; plain acquisition and index construction
          are not curation findings.
      - scope: Instructed tidy metadata/link/tag repairs
        assessment: partial
        findings:
        - value: evolve
          basis: claimed
          records:
          - runtime.md#rt-rte-tidy-review
          note: Agent-directed maintenance revises existing retained metadata and links.
        records:
        - runtime.md#rt-rte-tidy-review
        - memory.md#mem-obj-frontmatter
        - memory.md#mem-obj-body
        note: Specific repair requests establish a claimed revision branch. No demonstrated consolidation,
          synthesis, promotion or learning benefit follows from the tidy label.
      - scope: Index maintenance, metadata withdrawal and other repair/log/generator branches
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-snapshot-lifecycle
        - memory.md#mem-rte-metadata-withdrawal
        - epistemic.md#epi-rte-link-admission
        - memory.md#mem-obj-managed-region
        - runtime.md#rt-rte-config-install
        note: Index rebuilds and removal alone do not establish a controlled curation operation. Full
          lint/link, OKF and log/release transformations remain unresolved; no complete operation union
          or bounded absence is supported.
      records:
      - epistemic.md#epi-rte-metadata-repair
      - memory.md#mem-obj-frontmatter
      - memory.md#mem-rte-navigation-generation
      - memory.md#mem-obj-managed-region
      - runtime.md#rt-rte-tidy-review
      - memory.md#mem-obj-body
      - memory.md#mem-rte-snapshot-lifecycle
      - memory.md#mem-rte-metadata-withdrawal
      - epistemic.md#epi-rte-link-admission
      - runtime.md#rt-rte-config-install
      note: Evolve is supported for named revision mechanisms. Extraction of access fields is not automatically
        consolidation; no new claim, deduplication, forgetting or tier promotion is established solely
        by a command name. Untraced alternatives prevent known coverage.
    read_back_direction:
      assessment: partial
      units:
      - scope: Explicit CLI/Pi corpus and index query/read
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id020
          - runtime.md#rt-rte-query-read
          - memory.md#mem-obj-body
          - memory.md#mem-obj-frontmatter
          - memory.md#mem-obj-index-entry
          - memory.md#mem-obj-bm25
          - memory.md#mem-rte-snapshot-lifecycle
          note: Consumer-issued file/filter/query/section requests select retained corpus/access state
            and return requested material.
        records: *id020
        note: Code delivering the requested output is not a second push operation.
      - scope: Pi session-start aggregate supply
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id021
          - runtime.md#rt-rte-summary-injection
          - memory.md#mem-obj-frontmatter
          - memory.md#mem-obj-index-entry
          note: An opt-in session-start code rule selects retained vault state and independently supplies
            hidden orientation context.
        records: *id021
        note: The injected aggregate is fresh output from retained inputs, not an extension-owned checkpoint.
          Host transcript retention is excluded.
      - scope: Traced generated navigation ordinary note read
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id022
          - memory.md#mem-rte-navigation-generation
          - memory.md#mem-obj-managed-region
          - runtime.md#rt-rte-query-read
          note: Persisted generated Markdown is available through later explicit note reads.
        records: *id022
        note: No independently scheduled navigation delivery is established.
      - scope: Mutable configuration and optional saved Jev artifact consumption
        assessment: partial
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-config-install
          note: Command setup automatically loads retained configuration to determine later rules and
            scope.
        - value: pull
          basis: afforded
          records:
          - runtime.md#rt-obj-manifest
          - epistemic.md#epi-obj-classification-results
          - runtime.md#rt-rte-jev-suggestions
          note: Caller-captured manifests/results can be explicitly supplied for later validation or review.
        records:
        - runtime.md#rt-rte-config-install
        - runtime.md#rt-obj-manifest
        - epistemic.md#epi-obj-classification-results
        - runtime.md#rt-rte-jev-suggestions
        note: Configuration load is wired; actual saved-helper reuse and all retained artifact consumers
          remain unresolved.
      - scope: Remaining log/release, specialized generator and installed-host consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-body
        - memory.md#mem-obj-managed-region
        - runtime.md#rt-rte-config-install
        - runtime.md#rt-rte-tidy-review
        note: Specialized later-consumer routes are uninspected. Static installed assets are excluded,
          but replacement/withdrawal and dynamic retained control coverage is incomplete.
      records:
      - runtime.md#rt-rte-query-read
      - memory.md#mem-obj-body
      - memory.md#mem-obj-frontmatter
      - memory.md#mem-obj-index-entry
      - memory.md#mem-obj-bm25
      - memory.md#mem-rte-snapshot-lifecycle
      - runtime.md#rt-rte-summary-injection
      - memory.md#mem-rte-navigation-generation
      - memory.md#mem-obj-managed-region
      - runtime.md#rt-rte-config-install
      - runtime.md#rt-obj-manifest
      - epistemic.md#epi-obj-classification-results
      - runtime.md#rt-rte-jev-suggestions
      - runtime.md#rt-rte-tidy-review
      note: Both requested retrieval and independent Pi/context/configuration supply exist. A known pull
        route cannot resolve optional or uninspected read-back alternatives.
    read_back_signal:
      assessment: partial
      units:
      - scope: Pi session-summary push selection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id023
          - runtime.md#rt-rte-summary-injection
          note: Session-start plus sessionSummary/vaultDir and once flag select a vault-level aggregate;
            recency/budget filters are not semantic targeting.
        records: *id023
        note: Trigger is session start; selector inputs are configured availability, vault metadata/tasks/structure
          and recent-file modification times; selected parts are aggregate fields and recent identities.
      - scope: Automatic configuration load for a later command
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id024
          - runtime.md#rt-rte-config-install
          note: Configured project availability supplies retained schema/view controls at invocation setup.
        records: *id024
        note: The recorded mechanism loads configuration broadly; no recorded identity match targeting
          separate delivered memory parts supports identifier classification.
      - scope: Explicit query/read and navigation pull operations
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-query-read
        - memory.md#mem-rte-navigation-generation
        - memory.md#mem-obj-managed-region
        note: Signal classifies push selection, not requested file identifiers or BM25 query ranking.
      - scope: Optional helper artifact and remaining push alternatives
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-manifest
        - runtime.md#rt-rte-jev-suggestions
        - runtime.md#rt-rte-config-install
        - memory.md#mem-obj-body
        - memory.md#mem-obj-managed-region
        note: Named saved artifacts have requested reuse, but retention and untraced automatic consumers
          are unresolved. A file identifier alone cannot establish targeted push.
      records:
      - runtime.md#rt-rte-summary-injection
      - runtime.md#rt-rte-config-install
      - runtime.md#rt-rte-query-read
      - memory.md#mem-rte-navigation-generation
      - memory.md#mem-obj-managed-region
      - runtime.md#rt-obj-manifest
      - runtime.md#rt-rte-jev-suggestions
      - memory.md#mem-obj-body
      note: Coarse push is supported for session orientation and broad configuration loading. No inferred
        lexical signal is added for BM25 pull. Unknown alternatives prevent complete push-signal coverage
        or system-wide inapplicability.
    trace_learning:
      assessment: partial
      units:
      - scope: Prescribed trace-informed tidy repair to later corpus consumers
        assessment: partial
        findings:
        - value: 'yes'
          basis: claimed
          records:
          - runtime.md#rt-rte-tidy-review
          - memory.md#mem-obj-frontmatter
          - memory.md#mem-obj-body
          - runtime.md#rt-rte-query-read
          note: Git/task/recent-activity evidence feeds model admission of durable metadata/link repairs
            that later queries/reads consume as context or selection state.
        records:
        - runtime.md#rt-rte-tidy-review
        - memory.md#mem-obj-frontmatter
        - memory.md#mem-obj-body
        - runtime.md#rt-rte-query-read
        note: Starting repair is authorization, not per-content human admission. This supports the prescribed
          automatic trace-fed branch, not exercised learning, improved capacity or learned static skills;
          concrete outputs and retained rationale remain unobserved.
      - scope: Corpus-derived snapshot and MADR generation
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-snapshot-lifecycle
        - memory.md#mem-rte-navigation-generation
        - memory.md#mem-obj-index-entry
        - memory.md#mem-obj-bm25
        - memory.md#mem-obj-managed-region
        note: Named transforms derive access/navigation state from documents, not established activity
          traces. They do not constitute qualifying trace-fed updates in this scoped path.
      - scope: Pi summary injection and Jev helper computation alone
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-summary-injection
        - runtime.md#rt-rte-jev-suggestions
        - runtime.md#rt-obj-manifest
        - epistemic.md#epi-obj-classification-results
        note: Summary output is not retained by Hyalo; Jev computation does not automatically persist
          a durable corpus update. Neither alone is a qualifying trace-fed write.
      - scope: Initial corpus, caller writes and untraced maintenance/log/release branches
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-body
        - memory.md#mem-obj-frontmatter
        - runtime.md#rt-rte-property-write
        - runtime.md#rt-rte-config-install
        - runtime.md#rt-rte-tidy-review
        note: Actual corpus traces, proposal inputs and complete admission/later-consumer chains are unresolved.
          The inspected positive branch does not settle other writes; no bounded system-wide no is warranted.
      records:
      - runtime.md#rt-rte-tidy-review
      - memory.md#mem-obj-frontmatter
      - memory.md#mem-obj-body
      - runtime.md#rt-rte-query-read
      - memory.md#mem-rte-snapshot-lifecycle
      - memory.md#mem-rte-navigation-generation
      - memory.md#mem-obj-index-entry
      - memory.md#mem-obj-bm25
      - memory.md#mem-obj-managed-region
      - runtime.md#rt-rte-summary-injection
      - runtime.md#rt-rte-jev-suggestions
      - runtime.md#rt-obj-manifest
      - epistemic.md#epi-obj-classification-results
      - runtime.md#rt-rte-property-write
      - runtime.md#rt-rte-config-install
      note: A claimed yes is local to the instructed automatic trace-informed repair chain. No local no
        is invented without bounded absence records. Other writes remain unresolved, so neither wired
        system learning nor a complete negative is supported.
    trace_source:
      assessment: partial
      units:
      - scope: Git/recent-activity evidence in qualifying instructed tidy repair
        assessment: partial
        findings:
        - value: event-streams
          basis: claimed
          records:
          - runtime.md#rt-rte-tidy-review
          note: Git commit/merge and recent project-activity records are discrete recorded activity used
            to determine durable maintenance changes.
        records:
        - runtime.md#rt-rte-tidy-review
        - memory.md#mem-obj-frontmatter
        - memory.md#mem-obj-body
        note: This names original activity evidence, not the serialization of CLI results. Optional Claude
          memory origin and other diagnosis inputs are unresolved; task counts alone do not establish
          tool-traces, trajectories or session-logs.
      - scope: Snapshot and navigation document derivation
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-snapshot-lifecycle
        - memory.md#mem-rte-navigation-generation
        note: These named non-trace-fed products have no qualifying trace-learning source.
      - scope: Nonretained Pi summary and nonwriting Jev helper
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-summary-injection
        - runtime.md#rt-rte-jev-suggestions
        note: No qualifying automatic retained trace-fed update is established on these computations alone.
      - scope: Optional Claude-memory inputs, initial corpus and untraced log/release update sources
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-tidy-review
        - memory.md#mem-obj-body
        - memory.md#mem-obj-frontmatter
        - runtime.md#rt-rte-config-install
        note: Original source contents and qualifying automatic-write chains are unknown or uninspected.
          Imported memory or log labels cannot establish session-logs, tool-traces or trajectories.
      records:
      - runtime.md#rt-rte-tidy-review
      - memory.md#mem-obj-frontmatter
      - memory.md#mem-obj-body
      - memory.md#mem-rte-snapshot-lifecycle
      - memory.md#mem-rte-navigation-generation
      - runtime.md#rt-rte-summary-injection
      - runtime.md#rt-rte-jev-suggestions
      - runtime.md#rt-rte-config-install
      note: Event-streams is claimed for recorded Git/project activity in the tidy branch; mixed/opaque
        diagnosis evidence and untraced writes prevent complete trace-source coverage. Inapplicable local
        units do not make the whole axis inapplicable.
---

# Hyalo memory profile

## Comparison rationale

The comparison separates source notes, derivative access products and later
consumer paths. Binary snapshots remain files; their loaded operative copies
are in-memory state. Symbolic BM25 postings are not vectors or learned weights.
Their ranking force is independent of the knowledge force of prose delivered
by an explicit read. See [MEM-OBJ-bm25](memory.md#mem-obj-bm25),
[MEM-OBJ-index-entry](memory.md#mem-obj-index-entry) and
[RT-RTE-query-read](runtime.md#rt-rte-query-read).

Reconciliation supersedes the epistemic vault-body and frontmatter declarations
with [MEM-OBJ-body](memory.md#mem-obj-body) and
[MEM-OBJ-frontmatter](memory.md#mem-obj-frontmatter). Those canonical objects
support storage, form, provenance limits and downstream context/selection.
The epistemic metadata-repair and link-admission routes remain distinct from
caller-assigned writes and retain their own consumer effects. No supersession
upgrades evidence strength or replaces the routes' semantic limits. See
[EPI-RTE-metadata-repair](epistemic.md#epi-rte-metadata-repair) and
[EPI-RTE-link-admission](epistemic.md#epi-rte-link-admission).

Automatic admission is local to software-generated access/navigation products,
rule-generated repairs and the prescribed agent-selected routine tidy repairs.
An operator starting a workflow does not manually approve each output. Conversely,
a generic CLI caller could be human or agent: its assignments, withdrawals and
configuration requests do not establish manual admission. See
[MEM-RTE-navigation-generation](memory.md#mem-rte-navigation-generation),
[MEM-RTE-snapshot-lifecycle](memory.md#mem-rte-snapshot-lifecycle),
[RT-RTE-property-write](runtime.md#rt-rte-property-write) and
[RT-RTE-tidy-review](runtime.md#rt-rte-tidy-review).

The tidy instructions prescribe an automatic activity-to-repair-to-later-read
chain, so its trace-derived lineage, learning authority, trace-learning yes and
activity-event source retain claimed basis. They do not establish executed
repairs, learning benefit, autonomous method revision or retained rationale.
Git activity is original recorded activity; wrapping its read in a tool response
does not turn it into tool-traces. Optional Claude memory has unresolved origin.
See [RT-RTE-tidy-review](runtime.md#rt-rte-tidy-review). This branch is not
collapsed into the corpus-derived index branch, and its positive finding cannot
resolve other included writes.

Jev is a nonwriting helper. Its process-local evidence and results are excluded
unless captured for later use; optional saved artifacts retain afforded memory
consumption and unresolved actual retention. Existing corpus text copied into
its manifest supports an imported derivation path, not original corpus trust.
Saved rubrics can supply instruction at the classifier, while saved labels and
hashes supply validation/enforcement at helper code; returned decisions remain
advice at review. None inherits the authority of static installed skills or
becomes an accepted truth merely through capture. See
[RT-OBJ-manifest](runtime.md#rt-obj-manifest),
[RT-OBJ-document-content](runtime.md#rt-obj-document-content),
[EPI-OBJ-category-rubrics](epistemic.md#epi-obj-category-rubrics),
[EPI-OBJ-classification-results](epistemic.md#epi-obj-classification-results) and
[RT-RTE-jev-suggestions](runtime.md#rt-rte-jev-suggestions).

Pi's unsolicited orientation is a push over retained vault state, not a durable
continuation summary written by Hyalo. The trigger and aggregate availability
are coarse, even though the aggregate contains file identities. Explicit file
requests and BM25 queries remain pull; their selector vocabulary does not
establish an identifier or inferred-lexical push. Configuration loads supply
retained rule state broadly to subsequent commands. See
[RT-RTE-summary-injection](runtime.md#rt-rte-summary-injection) and
[RT-RTE-config-install](runtime.md#rt-rte-config-install).

Every axis retains partial coverage. Initial corpus provenance and caller
identity, optional saved artifacts, specialized log/release consumers and
untraced maintenance alternatives prevent complete classifications. No observed
or causal basis is asserted, and no bounded absence is manufactured from
uninspected paths. Wired mechanics do not establish compliance, repair truth or
benefit. The missing mechanisms remain inventory limits, not omitted alternatives.

Source reads: none. This profile uses only supplied accepted records and their
annotations; no new source evidence, records or verification judgments were added.
