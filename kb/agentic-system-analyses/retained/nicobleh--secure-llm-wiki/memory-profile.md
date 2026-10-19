---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: Secure LLM-Wiki memory comparison across retained claims, control metadata, vectors, policy
  and history, with unresolved external alternatives.
run-id: AAS-2026-10-19-secure-llm-wiki-df02f419bddb-01
source-identity: https://github.com/nicobleh/secure-llm-wiki
reviewed-boundary: dfbc60e37487b61e9a5cbce1271a13576a776d51
memory-comparison:
  version: 2
  scope: 'Application-accumulated claim text in pages/quarantine, eligibility/provenance and gate diagnostics,
    persisted embeddings/access keys, editable policy after initialization, and data-root Git history;
    admission, maintenance and later ingestion/query/operator consumption routes. Direct API callers and
    initial payload provenance remain unresolved alternatives, as does opaque external provider retention
    if present. Excludes shipped static prompt/code policy, transient source/completion/query output,
    and external weights as such: none is shown to be application-accumulated memory.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Claim text, eligibility/provenance, gate diagnostics and retained editable policy
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-claim-text
          - memory.md#mem-obj-claim-metadata
          - memory.md#mem-obj-gate-records
          - memory.md#mem-obj-trust-rules
          note: Markdown with YAML frontmatter and policy YAML are the operative working-file stores.
        records:
        - memory.md#mem-obj-claim-text
        - memory.md#mem-obj-claim-metadata
        - memory.md#mem-obj-gate-records
        - memory.md#mem-obj-trust-rules
        note: These application-owned objects have inspected file persistence; YAML/JSON encodings are
          not additional substrates.
      - scope: Saved embedding coordinates and UUID access structure
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-claim-embeddings
          note: Vectors persist as per-claim JSON files.
        - value: vector
          basis: wired
          records:
          - memory.md#mem-obj-claim-embeddings
          note: Dense retained vectors supply cosine comparison at future admission.
        records:
        - memory.md#mem-obj-claim-embeddings
        note: The vector store is not a query retrieval index and is separate from model weights.
      - scope: Data-root historical snapshots and commit messages
        assessment: known
        findings:
        - value: repo
          basis: wired
          records:
          - memory.md#mem-obj-wiki-history
          note: A separate Git repository retains snapshots and operation messages when history survives.
        records:
        - memory.md#mem-obj-wiki-history
        note: Default reset destroys this repository; ordinary file reload does not read history.
      - scope: External provider-side retention, if any, beyond application-owned objects
        assessment: not-determinable
        findings: []
        records: &id001
        - runtime.md#rt-cmp-extraction-model
        - runtime.md#rt-cmp-review-model
        - runtime.md#rt-cmp-embed-model
        note: Adapters do not expose provider retention or update internals. No substrate, admission,
          transformation or consumer classification follows from model names; this alternative remains
          unresolved, not absent. External provider weights are not claimed to be application-accumulated
          memory.
      records:
      - memory.md#mem-obj-claim-text
      - memory.md#mem-obj-claim-metadata
      - memory.md#mem-obj-gate-records
      - memory.md#mem-obj-trust-rules
      - memory.md#mem-obj-claim-embeddings
      - memory.md#mem-obj-wiki-history
      - runtime.md#rt-cmp-extraction-model
      - runtime.md#rt-cmp-review-model
      - runtime.md#rt-cmp-embed-model
      note: Inventory covers working claims, diagnostics, policy, vectors and history. Provider-side retained
        state remains opaque; no deployed instance is supplied.
    representational_form:
      assessment: partial
      units:
      - scope: Claim bodies consumed by reviewer/query and diagnostic prose inspected by humans
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-claim-text
          - memory.md#mem-obj-gate-records
          note: Claim text and failed-review prose are interpreted linguistically; body-only detail is
            not the reload source.
        records:
        - memory.md#mem-obj-claim-text
        - memory.md#mem-obj-gate-records
        note: Natural-language diagnostics are distinct from gate-name progress fields.
      - scope: Eligibility/provenance fields, gate names, vector keys, policy predicates and historical
          snapshots
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-claim-metadata
          - memory.md#mem-obj-gate-records
          - memory.md#mem-obj-claim-embeddings
          - memory.md#mem-obj-trust-rules
          - memory.md#mem-obj-wiki-history
          note: Localized fields, identifiers, enums, thresholds and snapshots have fixed serialization
            or code consumers.
        records:
        - memory.md#mem-obj-claim-metadata
        - memory.md#mem-obj-gate-records
        - memory.md#mem-obj-claim-embeddings
        - memory.md#mem-obj-trust-rules
        - memory.md#mem-obj-wiki-history
        note: Unconsumed metadata is not thereby behavioral policy. History also contains natural-language
          messages.
      - scope: Historical commit messages at operator inspection
        assessment: known
        findings:
        - value: natural-language
          basis: afforded
          records:
          - memory.md#mem-obj-wiki-history
          note: Operators can interpret URI/trust/reason messages during forensic inspection.
        records:
        - memory.md#mem-obj-wiki-history
        note: No shipped model consumes the history.
      - scope: Embedding coordinates at cosine comparison
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-claim-embeddings
          note: Dense distributed numerical representations are consumed numerically, not as readable
            summaries or symbolic JSON keys.
        records:
        - memory.md#mem-obj-claim-embeddings
        note: This classification does not imply parameter training.
      - scope: External provider-side retention, if any, beyond application-owned objects
        assessment: not-determinable
        findings: []
        records: *id001
        note: Adapters do not expose provider retention or update internals. No substrate, admission,
          transformation or consumer classification follows from model names; this alternative remains
          unresolved, not absent. External provider weights are not claimed to be application-accumulated
          memory.
      records:
      - memory.md#mem-obj-claim-text
      - memory.md#mem-obj-gate-records
      - memory.md#mem-obj-claim-metadata
      - memory.md#mem-obj-claim-embeddings
      - memory.md#mem-obj-trust-rules
      - memory.md#mem-obj-wiki-history
      - runtime.md#rt-cmp-extraction-model
      - runtime.md#rt-cmp-review-model
      - runtime.md#rt-cmp-embed-model
      note: Mixed text, symbolic fields and dense coordinates are split by operative consumption; provider-side
        retained forms remain unresolved.
    lineage:
      assessment: partial
      units:
      - scope: CLI-extracted claim text and software-generated metadata/diagnostics
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-claim-text
          - memory.md#mem-obj-claim-metadata
          - memory.md#mem-obj-gate-records
          - runtime.md#rt-rte-ingest-admission
          note: Extraction and gate processing compile acquired source material and execution results
            into retained parts.
        records:
        - memory.md#mem-obj-claim-text
        - memory.md#mem-obj-claim-metadata
        - memory.md#mem-obj-gate-records
        - runtime.md#rt-rte-ingest-admission
        note: Source documents themselves are not retained snapshots. Imported source input is distinct
          from the derived claim object.
      - scope: Current CLI claim-to-vector derivation
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-claim-embeddings
          note: The embedding provider transforms current extracted claim text before software saves the
            resulting vector.
        records:
        - memory.md#mem-obj-claim-embeddings
        note: This resolves the inspected producer path, not the provenance of arbitrary pre-existing
          JSON.
      - scope: Initial or externally replaced claims and vectors at direct store APIs
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-claim-text
        - memory.md#mem-obj-claim-metadata
        - memory.md#mem-obj-claim-embeddings
        note: Caller-supplied payloads have no authenticated initial provenance or model/version marker;
          their derivation cannot be classified from the save capability.
      - scope: Documented operator-authored policy edits
        assessment: known
        findings:
        - value: authored
          basis: afforded
          records:
          - memory.md#mem-obj-trust-rules
          note: Operators may edit domain rules and thresholds in retained YAML.
        records:
        - memory.md#mem-obj-trust-rules
        note: The documented edit mechanism does not authenticate every deployed policy file.
      - scope: Software/template initialization of retained policy
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-trust-rules
          note: Initialization writes a software-authored configuration template from shipped defaults.
        records:
        - memory.md#mem-obj-trust-rules
        note: Static built-in rules are excluded except as inputs to retained policy initialization.
      - scope: Git snapshots/messages and retained gate outcome traces
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-wiki-history
          - memory.md#mem-obj-gate-records
          note: Host writes preserve operation outcomes, passed-gate progress and selected failed-review
            reasons.
        records:
        - memory.md#mem-obj-wiki-history
        - memory.md#mem-obj-gate-records
        note: Trace-extracted lineage alone does not establish trace learning.
      - scope: External provider-side retention, if any, beyond application-owned objects
        assessment: not-determinable
        findings: []
        records: *id001
        note: Adapters do not expose provider retention or update internals. No substrate, admission,
          transformation or consumer classification follows from model names; this alternative remains
          unresolved, not absent. External provider weights are not claimed to be application-accumulated
          memory.
      records:
      - memory.md#mem-obj-claim-text
      - memory.md#mem-obj-claim-metadata
      - memory.md#mem-obj-gate-records
      - runtime.md#rt-rte-ingest-admission
      - memory.md#mem-obj-claim-embeddings
      - memory.md#mem-obj-trust-rules
      - memory.md#mem-obj-wiki-history
      - runtime.md#rt-cmp-extraction-model
      - runtime.md#rt-cmp-review-model
      - runtime.md#rt-cmp-embed-model
      note: Known derivation paths coexist with unknown initial/direct-write provenance and opaque provider
        state. No session-log origin is inferred from document ingestion.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Selected claim text and rendered metadata at answering model
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-claim-text
          - memory.md#mem-obj-claim-metadata
          - memory.md#mem-obj-gate-records
          - runtime.md#rt-bap-query-evidence
          note: The query model receives evidence text, provenance/trust labels and gate names for answering,
            not standing directions.
        records:
        - memory.md#mem-obj-claim-text
        - memory.md#mem-obj-claim-metadata
        - memory.md#mem-obj-gate-records
        - runtime.md#rt-bap-query-evidence
        note: System-message placement does not turn evidence into instruction; actual obedience and benefit
          are unobserved.
      - scope: Active trusted retained text at later batch security review
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-claim-text
          - runtime.md#rt-rte-ingest-admission
          note: Existing claim statements supply reference context for manipulation review.
        records:
        - memory.md#mem-obj-claim-text
        - runtime.md#rt-rte-ingest-admission
        note: A model receives reference text, not prior full review rationale or a factual oracle.
      - scope: Trust/status and source fields at context and admission predicates
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-claim-metadata
          - runtime.md#rt-rte-ingest-admission
          - runtime.md#rt-rte-context-query
          note: Stored labels exclude ineligible content and existing trusted state can veto untrusted
            admission.
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-claim-metadata
          - runtime.md#rt-rte-ingest-admission
          note: Retained trusted existence and section/source relations supply candidate-admissibility
            criteria.
        records:
        - memory.md#mem-obj-claim-metadata
        - runtime.md#rt-rte-ingest-admission
        - runtime.md#rt-rte-context-query
        note: Only consumed fields have these forces; successor pointers and other unused metadata gain
          no authority by serialization.
      - scope: Retained vectors at Gate 5 comparison
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-claim-embeddings
          note: Coordinates determine relative cosine scores and the highest matching vector.
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-claim-embeddings
          note: The selected similarity score is checked against duplicate/escalation thresholds.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-claim-embeddings
          note: Threshold results cause quarantine or escalation rather than ordinary commit.
        records:
        - memory.md#mem-obj-claim-embeddings
        note: Ranking is numerical comparison, not semantic query retrieval or proof of contradiction.
      - scope: Retained rule/threshold policy at future ingestion
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-trust-rules
          note: Domain matches select the trust tier assigned to incoming source claims.
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-trust-rules
          note: Retained similarity thresholds determine admissibility criteria.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-trust-rules
          - runtime.md#rt-rte-ingest-admission
          note: Policy-derived trust and thresholds can veto ordinary admission.
        records:
        - memory.md#mem-obj-trust-rules
        - runtime.md#rt-rte-ingest-admission
        note: Effects operate through fixed code, not model-readable standing instructions; edits do not
          re-tier existing claims.
      - scope: Full diagnostics/history at operator inspection and recovery
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-obj-gate-records
          - memory.md#mem-obj-wiki-history
          note: Files and surviving Git history can supply forensic evidence to an operator.
        records:
        - memory.md#mem-obj-gate-records
        - memory.md#mem-obj-wiki-history
        note: Ordinary query/review omits full reasons and history. No automatic policy-update consumer
          is established.
      - scope: External provider-side retention, if any, beyond application-owned objects
        assessment: not-determinable
        findings: []
        records: *id001
        note: Adapters do not expose provider retention or update internals. No substrate, admission,
          transformation or consumer classification follows from model names; this alternative remains
          unresolved, not absent. External provider weights are not claimed to be application-accumulated
          memory.
      records:
      - memory.md#mem-obj-claim-text
      - memory.md#mem-obj-claim-metadata
      - memory.md#mem-obj-gate-records
      - runtime.md#rt-bap-query-evidence
      - runtime.md#rt-rte-ingest-admission
      - runtime.md#rt-rte-context-query
      - memory.md#mem-obj-claim-embeddings
      - memory.md#mem-obj-trust-rules
      - memory.md#mem-obj-wiki-history
      - runtime.md#rt-cmp-extraction-model
      - runtime.md#rt-cmp-review-model
      - runtime.md#rt-cmp-embed-model
      note: Consumer-specific forces coexist. No automatic learning authority is inferred from trace retention;
        provider-side consumers remain unresolved.
    write_agency:
      assessment: partial
      units:
      - scope: Ordinary gated claim/metadata/diagnostic and post-commit vector admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-claim-text
          - memory.md#mem-obj-claim-metadata
          - memory.md#mem-obj-gate-records
          - memory.md#mem-obj-claim-embeddings
          - runtime.md#rt-rte-ingest-admission
          note: Software admits or quarantines model proposals and saves vectors without per-content operator
            approval.
        records:
        - memory.md#mem-obj-claim-text
        - memory.md#mem-obj-claim-metadata
        - memory.md#mem-obj-gate-records
        - memory.md#mem-obj-claim-embeddings
        - runtime.md#rt-rte-ingest-admission
        note: Starting ingestion or assigning source trust is not approval of each retained proposition.
      - scope: Template policy initialization and normal history commits
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-trust-rules
          - memory.md#mem-obj-wiki-history
          note: Software initializes templates and records commits without separate human approval of
            each result.
        records:
        - memory.md#mem-obj-trust-rules
        - memory.md#mem-obj-wiki-history
        note: Physical I/O and template authorship are not substituted for admission control.
      - scope: Documented manual content/policy editing and confirmed clear/reset
        assessment: known
        findings:
        - value: manual
          basis: afforded
          records:
          - memory.md#mem-obj-claim-text
          - memory.md#mem-obj-trust-rules
          note: Explicit operator file edits supply or replace retained content.
        - value: manual
          basis: wired
          records:
          - runtime.md#rt-rte-operator-maintenance
          - memory.md#mem-obj-wiki-history
          note: CLI confirmation authorizes the selected destructive maintenance operation.
        records:
        - memory.md#mem-obj-claim-text
        - memory.md#mem-obj-trust-rules
        - runtime.md#rt-rte-operator-maintenance
        - memory.md#mem-obj-wiki-history
        note: Direct file-edit capability is distinguished from the wired CLI confirmation.
      - scope: Generic direct storage, embedding-save and add-rule callers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-claim-text
        - memory.md#mem-obj-claim-metadata
        - memory.md#mem-obj-gate-records
        - memory.md#mem-obj-claim-embeddings
        - memory.md#mem-obj-trust-rules
        note: Caller invocation can admit or replace payloads without gates, but caller identity does
          not resolve human content approval.
      - scope: External provider-side retention, if any, beyond application-owned objects
        assessment: not-determinable
        findings: []
        records: *id001
        note: Adapters do not expose provider retention or update internals. No substrate, admission,
          transformation or consumer classification follows from model names; this alternative remains
          unresolved, not absent. External provider weights are not claimed to be application-accumulated
          memory.
      records:
      - memory.md#mem-obj-claim-text
      - memory.md#mem-obj-claim-metadata
      - memory.md#mem-obj-gate-records
      - memory.md#mem-obj-claim-embeddings
      - runtime.md#rt-rte-ingest-admission
      - memory.md#mem-obj-trust-rules
      - memory.md#mem-obj-wiki-history
      - runtime.md#rt-rte-operator-maintenance
      - runtime.md#rt-cmp-extraction-model
      - runtime.md#rt-cmp-review-model
      - runtime.md#rt-cmp-embed-model
      note: Automatic CLI admission and explicit operator mechanisms are supported separately. Generic
        API callers and provider admission remain unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Same-ID page replacement and operator revision of retained policy/content
        assessment: known
        findings:
        - value: evolve
          basis: afforded
          records:
          - memory.md#mem-obj-claim-text
          - memory.md#mem-obj-trust-rules
          note: Direct replacement or manual frontmatter/policy editing can revise an existing retained
            entry.
        records:
        - memory.md#mem-obj-claim-text
        - memory.md#mem-obj-trust-rules
        note: This is an editing affordance, not an automatic semantic supersession writer.
      - scope: History-preserving deletion of working claims
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-obj-wiki-history
          - runtime.md#rt-rte-operator-maintenance
          note: Deletion can remove a claim from future working-file loads while preserving prior Git
            snapshots.
        records:
        - memory.md#mem-obj-wiki-history
        - runtime.md#rt-rte-operator-maintenance
        note: Open query snapshots are not retracted; no automatic criticism or falsification is implied.
      - scope: Destructive reset and removal of retained state
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-obj-wiki-history
          - runtime.md#rt-rte-operator-maintenance
          note: Default reset deletes the data root and history, forgetting accumulated content while
            preserving policy rules.
        records:
        - memory.md#mem-obj-wiki-history
        - runtime.md#rt-rte-operator-maintenance
        note: Explicit forgetting is supported, not time-based downweighting.
      - scope: Acquisition/extraction, duplicate quarantine and arbitrary caller transformations
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-claim-text
        - memory.md#mem-obj-claim-embeddings
        - runtime.md#rt-rte-ingest-admission
        note: The records show compilation of transient source text and rejection of new duplicates, not
          consolidation or merging/removal of existing near-duplicate memory. Arbitrary supplied replacement
          semantics are not known; synthesis and promotion cannot be established.
      - scope: External provider-side retention, if any, beyond application-owned objects
        assessment: not-determinable
        findings: []
        records: *id001
        note: Adapters do not expose provider retention or update internals. No substrate, admission,
          transformation or consumer classification follows from model names; this alternative remains
          unresolved, not absent. External provider weights are not claimed to be application-accumulated
          memory.
      records:
      - memory.md#mem-obj-claim-text
      - memory.md#mem-obj-trust-rules
      - memory.md#mem-obj-wiki-history
      - runtime.md#rt-rte-operator-maintenance
      - memory.md#mem-obj-claim-embeddings
      - runtime.md#rt-rte-ingest-admission
      - runtime.md#rt-cmp-extraction-model
      - runtime.md#rt-cmp-review-model
      - runtime.md#rt-cmp-embed-model
      note: Only transformations over retained state are classified. Compilation rhetoric, index persistence
        and duplicate rejection alone establish neither consolidation nor deduplication; unresolved transformations
        prevent a complete operation inventory.
    read_back_direction:
      assessment: partial
      units:
      - scope: CLI future-ingestion, context/query, list and configuration reload chains
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-ingest-admission
          - runtime.md#rt-rte-context-query
          - memory.md#mem-obj-trust-rules
          - memory.md#mem-obj-gate-records
          note: Operator-invoked operations request retained material; filtering and delivery fulfill
            those requests.
        records:
        - runtime.md#rt-rte-ingest-admission
        - runtime.md#rt-rte-context-query
        - memory.md#mem-obj-trust-rules
        - memory.md#mem-obj-gate-records
        note: Selection before a question does not add an unsolicited push to the requested query-startup
          load.
      - scope: Full-file and Git-history inspection/reversal
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-obj-gate-records
          - memory.md#mem-obj-wiki-history
          note: An operator can request diagnostic files or historical snapshots for inspection and recovery.
        records:
        - memory.md#mem-obj-gate-records
        - memory.md#mem-obj-wiki-history
        note: The shipped query model does not receive Git history.
      - scope: External consumers of alternate renderers and direct storage APIs
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-context-query
        - memory.md#mem-obj-claim-text
        note: Builders afford rendering caller-supplied claims but identify no external persistence-to-consumer
          chain. Its request/delivery behavior is not established.
      - scope: External provider-side retention, if any, beyond application-owned objects
        assessment: not-determinable
        findings: []
        records: *id001
        note: Adapters do not expose provider retention or update internals. No substrate, admission,
          transformation or consumer classification follows from model names; this alternative remains
          unresolved, not absent. External provider weights are not claimed to be application-accumulated
          memory.
      records:
      - runtime.md#rt-rte-ingest-admission
      - runtime.md#rt-rte-context-query
      - memory.md#mem-obj-trust-rules
      - memory.md#mem-obj-gate-records
      - memory.md#mem-obj-wiki-history
      - memory.md#mem-obj-claim-text
      - runtime.md#rt-cmp-extraction-model
      - runtime.md#rt-cmp-review-model
      - runtime.md#rt-cmp-embed-model
      note: All identified application consumer chains are requested pull. Unknown external/API consumers
        and provider retention prevent declaring the entire included boundary pull-only.
    read_back_signal:
      assessment: not-determinable
      units:
      - scope: Completely inspected requested CLI and operator-inspection chains
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-ingest-admission
        - runtime.md#rt-rte-context-query
        - memory.md#mem-obj-trust-rules
        - memory.md#mem-obj-gate-records
        - memory.md#mem-obj-wiki-history
        note: These chains are pull-only; trust/status predicates, UUID paths and cosine admission checks
          are not unsolicited push selectors.
      - scope: Unspecified alternate API consumers and provider-side read-back
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-context-query
        - runtime.md#rt-cmp-extraction-model
        - runtime.md#rt-cmp-review-model
        - runtime.md#rt-cmp-embed-model
        note: No accepted record identifies a push trigger, selector input and selected retained part
          for these unresolved alternatives; pull-only inapplicability cannot be extended to them.
      records:
      - runtime.md#rt-rte-ingest-admission
      - runtime.md#rt-rte-context-query
      - memory.md#mem-obj-trust-rules
      - memory.md#mem-obj-gate-records
      - memory.md#mem-obj-wiki-history
      - runtime.md#rt-cmp-extraction-model
      - runtime.md#rt-cmp-review-model
      - runtime.md#rt-cmp-embed-model
      note: No controlled push-selection value is established. Inapplicability is local to inspected pull
        chains, not a system-wide absence of push.
    trace_learning:
      assessment: partial
      units:
      - scope: Local shipped query-answer and feedback-to-store update path
        assessment: known
        findings:
        - value: 'no'
          basis: wired
          records:
          - memory.md#mem-abs-query-feedback
          - runtime.md#rt-rte-context-query
          note: The bounded searched query implementation streams answers without capturing reactions
            or saving an answer/feedback update.
        records:
        - memory.md#mem-abs-query-feedback
        - runtime.md#rt-rte-context-query
        note: This negative is limited to the searched query-feedback route; it does not negate source
          compilation or provider adaptation.
      - scope: Document-compilation inputs, direct replacements and diagnostic/history reuse
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-claim-text
        - memory.md#mem-obj-gate-records
        - memory.md#mem-obj-wiki-history
        - runtime.md#rt-rte-ingest-admission
        note: Compilation retains source-derived context, but accepted records do not classify original
          documents as activity traces. Stored outcome diagnostics/history have no automatic derived-policy
          consumer. Arbitrary direct input origin and downstream use remain unresolved, preventing a complete
          trace-fed-write inventory.
      - scope: External provider-side retention, if any, beyond application-owned objects
        assessment: not-determinable
        findings: []
        records: *id001
        note: Adapters do not expose provider retention or update internals. No substrate, admission,
          transformation or consumer classification follows from model names; this alternative remains
          unresolved, not absent. External provider weights are not claimed to be application-accumulated
          memory.
      records:
      - memory.md#mem-abs-query-feedback
      - runtime.md#rt-rte-context-query
      - memory.md#mem-obj-claim-text
      - memory.md#mem-obj-gate-records
      - memory.md#mem-obj-wiki-history
      - runtime.md#rt-rte-ingest-admission
      - runtime.md#rt-cmp-extraction-model
      - runtime.md#rt-cmp-review-model
      - runtime.md#rt-cmp-embed-model
      note: A warranted local negative counts as classified coverage, but unresolved alternatives suppress
        a derived system-wide no. No qualifying trace-fed positive is established in accepted records.
    trace_source:
      assessment: not-determinable
      units:
      - scope: Searched local query-feedback update path
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-abs-query-feedback
        - runtime.md#rt-rte-context-query
        note: No qualifying trace-learning write exists on this completely inspected local route, so it
          has no trace source.
      - scope: Potential trace origin of ingested documents, direct supplied material and opaque provider
          updates
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-claim-text
        - memory.md#mem-obj-gate-records
        - memory.md#mem-obj-wiki-history
        - runtime.md#rt-rte-ingest-admission
        - runtime.md#rt-cmp-extraction-model
        - runtime.md#rt-cmp-review-model
        - runtime.md#rt-cmp-embed-model
        note: Neither retained diagnostics alone nor generic document acquisition establishes an original
          qualifying trace-fed write. No session-log, tool-trace, event-stream or trajectory value can
          be assigned without that input/consumer chain.
      records:
      - memory.md#mem-abs-query-feedback
      - runtime.md#rt-rte-context-query
      - memory.md#mem-obj-claim-text
      - memory.md#mem-obj-gate-records
      - memory.md#mem-obj-wiki-history
      - runtime.md#rt-rte-ingest-admission
      - runtime.md#rt-cmp-extraction-model
      - runtime.md#rt-cmp-review-model
      - runtime.md#rt-cmp-embed-model
      note: The local negative does not make unresolved source-compilation/provider alternatives inapplicable.
        No controlled trace-source finding is supported.
---

# Secure LLM-Wiki memory profile

## Comparison rationale

This profile classifies accepted implementation records, not a deployed wiki instance. Wiring establishes delivery and code effects; no finding asserts observed model compliance, factual accuracy, attack resistance or benefit. The retained inventory is separated into text, control metadata, numerical vectors, diagnostics, editable policy and history because their consumers differ ([MEM-OBJ-claim-text](memory.md#mem-obj-claim-text), [MEM-OBJ-claim-metadata](memory.md#mem-obj-claim-metadata), [MEM-OBJ-claim-embeddings](memory.md#mem-obj-claim-embeddings), [MEM-OBJ-gate-records](memory.md#mem-obj-gate-records), [MEM-OBJ-trust-rules](memory.md#mem-obj-trust-rules), [MEM-OBJ-wiki-history](memory.md#mem-obj-wiki-history)).

Reconciliation supersedes the epistemic claim-text and embedding objects with the memory objects cited here. It does not supersede the broader epistemic metadata container by its finer memory parts. No value relies on a superseded citation. Indeterminate extraction fidelity is not evidence of synthesis: the extraction route establishes source-derived compilation but no concrete novel claim or transformation over retained source sessions ([RT-RTE-extraction-parsing](runtime.md#rt-rte-extraction-parsing)).

Vector coordinates count as distributed-parametric form and a vector substrate even though their serialization is a JSON file. Their actual authority is at admission: maximum cosine selection ranks matches, thresholds supply validation criteria, and the gate enforces rejection/escalation. This is not question-conditioned retrieval. Query text instead supplies knowledge; its location in a system string does not establish instruction authority ([MEM-OBJ-claim-embeddings](memory.md#mem-obj-claim-embeddings), [RT-BAP-query-evidence](runtime.md#rt-bap-query-evidence)).

Operator initiation is not manual admission of each extracted claim. Manual edits and confirmed destructive maintenance are separate mechanisms; generic storage caller identity cannot determine whether a human approved content. The same distinction prevents arbitrary caller replacements from resolving lineage or automatic trace learning ([MEM-OBJ-claim-text](memory.md#mem-obj-claim-text), [RT-RTE-operator-maintenance](runtime.md#rt-rte-operator-maintenance)).

The explicit query-feedback absence warrants only a local trace-learning negative. Source-derived context is retained, but records do not establish whether original ingested documents contain qualifying activity traces; retained review outcomes and Git messages are not automatically transformed into new guidance. Opaque provider updates remain unresolved. Therefore the partial learning inventory has no system-wide negative, and its source axis is not globally inapplicable ([MEM-ABS-query-feedback](memory.md#mem-abs-query-feedback), [MEM-OBJ-gate-records](memory.md#mem-obj-gate-records), [MEM-OBJ-wiki-history](memory.md#mem-obj-wiki-history), [RT-CMP-review-model](runtime.md#rt-cmp-review-model)).

Requested startup loading remains pull even when code filters before the first question. UUID filenames and vector comparisons do not establish identifier- or embedding-selected push. Unknown external renderer consumers cannot inherit the inspected CLI chains' pull-only inapplicability ([RT-RTE-context-query](runtime.md#rt-rte-context-query), [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)).

Source-read log: no source files were read for this profile. All classifications use the supplied accepted records and reconciliation; no new evidence or record is introduced.
