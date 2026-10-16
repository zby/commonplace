---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Echel memory profile: legacy work-context delivery and canonical records, query, review and recovery."
run-id: AAS-2026-10-15-echel-08d27848b99a-01
source-identity: https://github.com/alirezabbasi/echel
reviewed-boundary: aee36de4d2d1c404fb36e9ad68cc0a920784ee61
memory-comparison:
  version: 2
  scope: >-
    Echel-retained legacy project, knowledge, work, findings, run commands/summaries
    and verification evidence; canonical record families and access metadata;
    disposable index; transaction journals, staged records and migration backups;
    their admission, maintenance and later-consumer routes. Canonical specialized
    task, release, artifact-payload and learning-adoption routes remain unresolved.
    External referenced artifact bytes, Hermes/provider memory and model weights,
    static shipped skills, contributor source history and synthetic benchmark
    datasets/reports are excluded from this project-memory comparison. Transient
    compiled context is considered only as a consumption/derivation path from
    retained files and as text copied into retained run commands.
  axes:
    storage_substrate:
      assessment: known
      units:
        - scope: "Legacy retained project, knowledge, work, findings, runs and evidence"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [runtime.md#rt-rte-file-workflow, memory.md#mem-obj-run, memory.md#mem-obj-evidence, runtime.md#rt-rte-compile-run]
              note: "Local JSON retains these objects; transient compiler text is not a separate retained in-memory store."
          records: [runtime.md#rt-rte-file-workflow, memory.md#mem-obj-run, memory.md#mem-obj-evidence, runtime.md#rt-rte-compile-run]
          note: "The producer/read routes establish the legacy file inventory."
        - scope: "Canonical record envelopes and artifact access metadata, not external payload bytes"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-canonical-records]
              note: "All named canonical families have JSON paths; relationship records do not establish a graph storage engine."
          records: [memory.md#mem-obj-canonical-records]
          note: "Generic storage covers even families whose specialized consumers are unresolved."
        - scope: "Disposable canonical search/relationship projection"
          assessment: known
          findings:
            - value: sqlite
              basis: wired
              records: [memory.md#mem-obj-disposable-index]
              note: "SQLite/FTS5 stores the replaceable projection; no vector substrate is inferred from lexical indexing."
          records: [memory.md#mem-obj-disposable-index]
          note: "The retained database and its canonical source are distinguished."
        - scope: "Transaction and migration journals, staging and backups"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-recovery-state]
              note: "Recovery reads retained journals and exact staged/backup bytes."
          records: [memory.md#mem-obj-recovery-state]
          note: "Operational recovery objects are included, not generalized to all runtime storage."
      records: [runtime.md#rt-rte-file-workflow, memory.md#mem-obj-canonical-records, memory.md#mem-obj-disposable-index, memory.md#mem-obj-run, memory.md#mem-obj-evidence, memory.md#mem-obj-recovery-state]
      note: "Records cover the scoped retained inventory. External payload and provider substrates are excluded, not classified from metadata."
    representational_form:
      assessment: known
      units:
        - scope: "Legacy statements, objectives, acceptance, findings and retained prompt/stdout text at readable consumers"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [epistemic.md#epi-obj-knowledge-record, epistemic.md#epi-obj-work-item, memory.md#mem-obj-run, runtime.md#rt-bap-context-prompt]
              note: "Text supplies model context or readable retained content, independently of its JSON encoding."
          records: [epistemic.md#epi-obj-knowledge-record, epistemic.md#epi-obj-work-item, memory.md#mem-obj-run, runtime.md#rt-bap-context-prompt]
          note: "No numerical parameters are retained by these paths."
        - scope: "Canonical statements, decisions, observations, implications and reasons exposed through query"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-canonical-records, memory.md#mem-rte-canonical-query]
              note: "Readable fields are distinct from symbolic gate inputs; external artifact payload form is outside scope."
          records: [memory.md#mem-obj-canonical-records, memory.md#mem-rte-canonical-query]
          note: "Full-record retrieval preserves readable fields without establishing dedicated model consumers."
        - scope: "Legacy/canonical identity, relationships, status, policy, commands, digests, index rows and recovery controls at fixed-rule consumers"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [runtime.md#rt-rte-file-workflow, memory.md#mem-obj-canonical-records, memory.md#mem-obj-disposable-index, memory.md#mem-obj-recovery-state, memory.md#mem-obj-evidence]
              note: "Fixed predicates, argv execution, fingerprints and recovery protocols consume localized fields."
          records: [runtime.md#rt-rte-file-workflow, memory.md#mem-obj-canonical-records, memory.md#mem-obj-disposable-index, memory.md#mem-obj-recovery-state, memory.md#mem-obj-evidence]
          note: "JSON is not itself the form classification; consumption establishes symbolic form."
      records: [runtime.md#rt-bap-context-prompt, memory.md#mem-obj-canonical-records, memory.md#mem-obj-disposable-index, memory.md#mem-obj-recovery-state, memory.md#mem-obj-run, memory.md#mem-obj-evidence, epistemic.md#epi-obj-knowledge-record, epistemic.md#epi-obj-work-item]
      note: "The scoped retained fields are text and fixed-rule structures. Unknown specialized use does not obscure their recorded representation; excluded payloads are not inferred from display fields."
    lineage:
      assessment: partial
      units:
        - scope: "Caller-authored legacy knowledge/work and canonical content"
          assessment: partial
          findings:
            - value: authored
              basis: wired
              records: [runtime.md#rt-rte-file-workflow, memory.md#mem-obj-canonical-records, memory.md#mem-rte-finding-maintenance, epistemic.md#epi-rte-relationship-write]
              note: "Caller statements, work definitions, criticism and link reasons enter authored-content routes. Authored does not mean authenticated human."
          records: [runtime.md#rt-rte-file-workflow, memory.md#mem-obj-canonical-records]
          note: "Initial payload provenance and whether callers copied or generated content remain caller-dependent; authored is not an exhaustive origin claim."
        - scope: "Portable canonical bundle installation"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [epistemic.md#epi-rte-portable-import]
              note: "The route transfers external records with their supplied metadata, without authenticating original origin."
          records: [epistemic.md#epi-rte-portable-import]
          note: "Known transfer lineage does not resolve the authored/imported history before the bundle."
        - scope: "Executed legacy stdout tails and verification outcomes/checksums"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [memory.md#mem-obj-run, memory.md#mem-obj-evidence]
              note: "Execution return supplies a bounded output tail or generated outcome/hash; this lineage does not imply learned guidance."
          records: [memory.md#mem-obj-run, memory.md#mem-obj-evidence]
          note: "Preview runs are excluded from this execution-trace unit and covered as compiled artifacts below."
        - scope: "Index projection, retained preview commands, recovery copies and service-generated revisions"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-disposable-index, memory.md#mem-obj-recovery-state, runtime.md#rt-rte-compile-run, memory.md#mem-rte-staleness-propagation, memory.md#mem-rte-storage-maintenance]
              note: "Deterministic projection, formatting, copying and revisions derive these retained parts without a trace-learning inference."
          records: [memory.md#mem-obj-disposable-index, memory.md#mem-obj-recovery-state, runtime.md#rt-rte-compile-run, memory.md#mem-rte-storage-maintenance]
          note: "This derivation classification leaves source content provenance with the original-content unit."
      records: [memory.md#mem-obj-canonical-records, runtime.md#rt-rte-file-workflow, epistemic.md#epi-rte-portable-import, memory.md#mem-obj-run, memory.md#mem-obj-evidence, memory.md#mem-obj-disposable-index, memory.md#mem-obj-recovery-state, memory.md#mem-rte-storage-maintenance]
      note: "Supported acquisition and derivation paths coexist with unresolved caller-supplied initial provenance."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Legacy objective/acceptance/verification directions delivered to Hermes"
          assessment: known
          findings:
            - value: instruction
              basis: wired
              records: [epistemic.md#epi-obj-work-item, runtime.md#rt-bap-context-prompt]
              note: "Retained work directions supply task guidance through the rendered prompt; this is not enforcement or demonstrated compliance."
          records: [epistemic.md#epi-obj-work-item, runtime.md#rt-bap-context-prompt]
          note: "Static implementation skills are not counted as retained project instructions."
        - scope: "Legacy knowledge/findings in prompt and canonical content/reasons returned to query caller"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [runtime.md#rt-bap-context-prompt, memory.md#mem-rte-canonical-query]
              note: "Statements and reasons supply context/reference, not automatically verified truth."
          records: [runtime.md#rt-bap-context-prompt, memory.md#mem-rte-canonical-query]
          note: "Delivery establishes the contextual path, not beneficial reliance."
        - scope: "Canonical searchable strings in FTS/BM25 ordering"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [memory.md#mem-obj-disposable-index, memory.md#mem-rte-canonical-query]
              note: "Retained searchable text influences relative result priority under fixed lexical code."
          records: [memory.md#mem-obj-disposable-index, memory.md#mem-rte-canonical-query]
          note: "No learned ranking policy is required or inferred."
        - scope: "Retained relationship, kind, stage, profile and recovery-state selectors"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [runtime.md#rt-rte-compile-run, memory.md#mem-rte-clarification-read, memory.md#mem-rte-policy-revision, memory.md#mem-obj-recovery-state]
              note: "Work relationships select input scope; active kinds select questions; project policy selects requirements; journals select recovery progression."
          records: [runtime.md#rt-rte-compile-run, memory.md#mem-rte-clarification-read, memory.md#mem-rte-policy-revision, memory.md#mem-obj-recovery-state]
          note: "These fixed-rule effects do not depend on semantic understanding of retained rationale."
        - scope: "Canonical eligibility and index/record freshness controls; legacy stage gate"
          assessment: known
          findings:
            - value: validation
              basis: wired
              records: [memory.md#mem-rte-policy-revision, memory.md#mem-rte-canonical-query, runtime.md#rt-rte-file-workflow, memory.md#mem-rte-storage-maintenance]
              note: "Retained accepted kinds/findings/profile, fingerprints and expected state supply conformance criteria for transitions, reads or installation."
            - value: enforcement
              basis: wired
              records: [memory.md#mem-rte-policy-revision, memory.md#mem-rte-canonical-query, runtime.md#rt-rte-file-workflow, memory.md#mem-rte-storage-maintenance]
              note: "Those predicates can refuse a transition, query or conflicting restoration. Legacy force bypass and direct writes bound the veto, not erase it."
          records: [memory.md#mem-rte-policy-revision, memory.md#mem-rte-canonical-query, runtime.md#rt-rte-file-workflow, memory.md#mem-rte-storage-maintenance]
          note: "Retained controls have local enforcing force, not a system-wide product-truth security guarantee."
        - scope: "Specialized canonical task, release, artifact and learning adoption; legacy run/evidence later behavior-shaping uses"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-canonical-records, memory.md#mem-obj-run, memory.md#mem-obj-evidence]
          note: "Generic storage/query does not establish specialized adoption or an update consumer; learning authority cannot be asserted from names or evidence IDs."
      records: [runtime.md#rt-bap-context-prompt, runtime.md#rt-rte-compile-run, runtime.md#rt-rte-file-workflow, memory.md#mem-rte-clarification-read, memory.md#mem-rte-policy-revision, memory.md#mem-rte-canonical-query, memory.md#mem-obj-recovery-state, memory.md#mem-obj-canonical-records, memory.md#mem-obj-run, memory.md#mem-obj-evidence]
      note: "Known consumer effects are retained separately from unresolved specialized consumers. No learning authority or universal approval enforcement follows."
    write_agency:
      assessment: partial
      units:
        - scope: "Automatic run/evidence retention, index rebuild admission and structural portable import"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-obj-run, memory.md#mem-obj-evidence, memory.md#mem-rte-canonical-query, epistemic.md#epi-rte-portable-import]
              note: "Software admits returned summaries, generated evidence, projected rows and structurally valid imports without per-content operator review; initiating the workflow does not make these manual."
          records: [memory.md#mem-obj-run, memory.md#mem-obj-evidence, memory.md#mem-rte-canonical-query, epistemic.md#epi-rte-portable-import]
          note: "Classification concerns admission, not whether a human started the command."
        - scope: "Canonical protected decisions, finding dispositions, staleness and profile/maturity transitions under the human-decision protocol"
          assessment: known
          findings:
            - value: manual
              basis: wired
              records: [runtime.md#rt-rte-knowledge-decide, memory.md#mem-rte-finding-maintenance, memory.md#mem-rte-staleness-propagation, memory.md#mem-rte-policy-revision]
              note: "These service protocols require an explicit human-labelled decision with capability and rationale for that retained transition. Wiring is conditional on honest principal provisioning, not proof of an actual human decision."
          records: [runtime.md#rt-rte-knowledge-decide, memory.md#mem-rte-finding-maintenance, memory.md#mem-rte-staleness-propagation, memory.md#mem-rte-policy-revision]
          note: "Manual protocol coverage is local; fabricated identity and direct writes are not authenticated or forced through it."
        - scope: "Initial/caller-authored records, direct store writes, finding/link creation and migration resolutions"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-idea-init, runtime.md#rt-rte-file-workflow, memory.md#mem-obj-canonical-records, memory.md#mem-rte-finding-maintenance, epistemic.md#epi-rte-relationship-write, epistemic.md#epi-rte-schema-migration]
          note: "Caller identity and content-level human control are unresolved. Physical software writes and explicit apply alone cannot decide manual versus automatic admission."
      records: [memory.md#mem-obj-run, memory.md#mem-obj-evidence, memory.md#mem-rte-canonical-query, epistemic.md#epi-rte-portable-import, runtime.md#rt-rte-knowledge-decide, memory.md#mem-rte-finding-maintenance, memory.md#mem-rte-staleness-propagation, memory.md#mem-rte-policy-revision, memory.md#mem-obj-canonical-records, epistemic.md#epi-rte-schema-migration]
      note: "Automatic admissions and explicit human-decision protocols coexist; generic caller and bypass paths prevent complete agency coverage."
    curation_operations:
      assessment: partial
      units:
        - scope: "Legacy retained knowledge/work/findings reduced into text and copied into retained run command"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [runtime.md#rt-obj-compiled-context, runtime.md#rt-rte-compile-run, memory.md#mem-obj-run]
              note: "Selection and narrower rendering reduce existing retained content to a task representation; source records remain. No novel claim or semantic verification is inferred."
          records: [runtime.md#rt-obj-compiled-context, runtime.md#rt-rte-compile-run, memory.md#mem-obj-run]
          note: "This is the inspected rendering path, not opaque Hermes compaction."
        - scope: "Canonical status/policy revisions and migration field edits"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [runtime.md#rt-rte-knowledge-decide, memory.md#mem-rte-finding-maintenance, memory.md#mem-rte-policy-revision, epistemic.md#epi-rte-schema-migration]
              note: "Existing retained entries receive revised status, policy or caller-specified fields; schema migration alone would not establish semantic revision, but explicit field editing does."
          records: [runtime.md#rt-rte-knowledge-decide, memory.md#mem-rte-finding-maintenance, memory.md#mem-rte-policy-revision, epistemic.md#epi-rte-schema-migration]
          note: "Migration can preserve or change meaning; no synthesis classification follows from its unrestricted edit surface."
        - scope: "Canonical stale/rejected eligibility and inactive finding impact"
          assessment: known
          findings:
            - value: invalidate
              basis: wired
              records: [memory.md#mem-rte-staleness-propagation, runtime.md#rt-rte-knowledge-decide, memory.md#mem-rte-finding-maintenance]
              note: "Retained status changes withdraw particular consumers' reliance/impact while keeping content and rationale."
          records: [memory.md#mem-rte-staleness-propagation, runtime.md#rt-rte-knowledge-decide, memory.md#mem-rte-finding-maintenance]
          note: "No deletion, time decay or revocation of already delivered prompts is inferred."
        - scope: "Caller-dependent canonical learning/content transformations and unrestricted migration semantics"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-canonical-records, epistemic.md#epi-rte-schema-migration]
          note: "No recorded instance establishes whether caller content adds claims, merges duplicates or changes salience. Projection, acquisition and storage cleanup alone add no controlled curation value."
      records: [runtime.md#rt-obj-compiled-context, runtime.md#rt-rte-compile-run, memory.md#mem-obj-run, runtime.md#rt-rte-knowledge-decide, memory.md#mem-rte-finding-maintenance, memory.md#mem-rte-policy-revision, memory.md#mem-rte-staleness-propagation, epistemic.md#epi-rte-schema-migration, memory.md#mem-obj-canonical-records]
      note: "Inspected reductions and revisions support positives, but unresolved semantic transforms prevent exhaustive operation coverage. Accepted status is not automatically a promote operation."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Explicit work context/run request and canonical query/clarification/lifecycle/recovery requests"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-compile-run, memory.md#mem-rte-canonical-query, memory.md#mem-rte-clarification-read, memory.md#mem-rte-policy-revision, memory.md#mem-obj-recovery-state]
              note: "Requested work material or retained state is selected and consumed for the requested operation; automatic rendering/return does not add an unsolicited push."
          records: [runtime.md#rt-rte-compile-run, memory.md#mem-rte-canonical-query, memory.md#mem-rte-clarification-read, memory.md#mem-rte-policy-revision, memory.md#mem-obj-recovery-state]
          note: "Relationship selection remains part of requested context delivery, not a second independent push route."
        - scope: "Specialized canonical task/release/learning/artifact consumers and run/evidence later consumption"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-canonical-records, memory.md#mem-obj-run, memory.md#mem-obj-evidence]
          note: "Storage affordances do not establish these consumer routes or their direction; no push absence claim covers them."
      records: [runtime.md#rt-rte-compile-run, memory.md#mem-rte-canonical-query, memory.md#mem-rte-clarification-read, memory.md#mem-rte-policy-revision, memory.md#mem-obj-recovery-state, memory.md#mem-obj-canonical-records, memory.md#mem-obj-run, memory.md#mem-obj-evidence]
      note: "Pull is implemented on assessed routes; unresolved included consumers prevent a complete pull-only conclusion."
    read_back_signal:
      assessment: not-determinable
      units:
        - scope: "Inspected explicit-request routes"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-compile-run, memory.md#mem-rte-canonical-query, memory.md#mem-rte-clarification-read, memory.md#mem-rte-policy-revision, memory.md#mem-obj-recovery-state]
          note: "These are pull operations. Their identifier membership and lexical ranking are not push signals."
        - scope: "Unestablished specialized canonical and retained trace consumer alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-canonical-records, memory.md#mem-obj-run, memory.md#mem-obj-evidence]
          note: "No recorded push trigger, selector input and delivered retained part establish a controlled signal; unresolved directions prevent axis-wide inapplicability."
      records: [runtime.md#rt-rte-compile-run, memory.md#mem-rte-canonical-query, memory.md#mem-rte-clarification-read, memory.md#mem-rte-policy-revision, memory.md#mem-obj-recovery-state, memory.md#mem-obj-canonical-records, memory.md#mem-obj-run, memory.md#mem-obj-evidence]
      note: "No positive push signal is established. This is not evidence that every included alternative lacks push."
    trace_learning:
      assessment: not-determinable
      units:
        - scope: "Legacy execution-output and verification-result automatic writes"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-run, memory.md#mem-obj-evidence]
          note: "Trace-fed retention is wired, but durable behavior-shaping derivation and later consumer are unestablished; neither yes nor a bounded absence warrant for no is supplied."
        - scope: "Canonical learning, evidence-linked content and other caller-produced updates"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-canonical-records, epistemic.md#epi-obj-learning, memory.md#mem-rte-storage-maintenance]
          note: "Learning labels, evidence IDs and imported metadata do not establish automatic trace-fed production or later adoption. Caller-dependent provenance prevents a complete negative."
      records: [memory.md#mem-obj-run, memory.md#mem-obj-evidence, memory.md#mem-obj-canonical-records, epistemic.md#epi-obj-learning, memory.md#mem-rte-storage-maintenance]
      note: "No qualifying automatic trace-to-durable-behavior-shaping-output-to-later-consumer chain is established; lack of such a record is not a system-wide no. External parameter learning is outside this memory scope."
    trace_source:
      assessment: not-determinable
      units:
        - scope: "Potential legacy run/evidence learning route"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-run, memory.md#mem-obj-evidence]
          note: "Subprocess returns identify trace retention, but no qualifying learning route exists in the accepted account to which a trace-source value can attach. No session or tool sequence is reconstructed from the tail/hash."
        - scope: "Potential canonical learning/adoption and caller/imported-content routes"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-canonical-records, epistemic.md#epi-obj-learning, epistemic.md#epi-rte-portable-import]
          note: "Original source content and qualifying automatic update remain unresolved; names and evidence references do not identify session logs, tool traces, events or trajectories."
      records: [memory.md#mem-obj-run, memory.md#mem-obj-evidence, memory.md#mem-obj-canonical-records, epistemic.md#epi-obj-learning, epistemic.md#epi-rte-portable-import]
      note: "Unresolved trace learning prevents inapplicability. Trace-extracted lineage alone does not license a learning-route source classification."
---

# Echel memory profile

## Comparison rationale

The two storage families remain separate. Canonical review does not protect the
legacy prompt route, and current initialization does not establish a continuous
fresh-init-to-agent journey. The comparison retains files and SQLite, rather
than treating JSON as a form or relationship edges as a graph substrate. The
canonical artifact record is included as access metadata; its externally
referenced payload is not classified from that metadata. See
[MEM-OBJ-canonical-records](memory.md#mem-obj-canonical-records),
[MEM-OBJ-disposable-index](memory.md#mem-obj-disposable-index) and
[RT-RTE-compile-run](runtime.md#rt-rte-compile-run).

Retained work supplies instructions; knowledge and findings supply context.
Canonical strings influence lexical ranking, while status, profile and recovery
fields have symbolic routing or gate effects. These are consumer-specific
forces, not an implication that every stored statement is accepted or obeyed.
Unknown specialized consumers remain included uncertainty. See
[RT-BAP-context-prompt](runtime.md#rt-bap-context-prompt),
[MEM-RTE-canonical-query](memory.md#mem-rte-canonical-query),
[MEM-RTE-policy-revision](memory.md#mem-rte-policy-revision) and
[MEM-OBJ-recovery-state](memory.md#mem-obj-recovery-state).

Human-labelled review is classified only as a local manual decision protocol.
It does not authenticate a person or classify generic caller writes as manual.
Conversely, automatic retention and import admission do not become manual merely
because a caller requested execution or transfer. Direct store writes and
caller-dependent initial content keep agency partial. See
[RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide),
[MEM-OBJ-run](memory.md#mem-obj-run) and
[EPI-RTE-portable-import](epistemic.md#epi-rte-portable-import).

Text compilation reduces existing retained material, and the run command retains
that representation. This supports consolidation without claiming semantic
synthesis. Canonical revisions support evolution; stale/rejected eligibility
and resolved finding impact support local invalidation without deleting history.
Index rebuilding is a projection, not independently consolidation or promotion.
Unrestricted migration permits edits but does not prove a new claim. See
[RT-OBJ-compiled-context](runtime.md#rt-obj-compiled-context),
[MEM-OBJ-run](memory.md#mem-obj-run),
[MEM-RTE-staleness-propagation](memory.md#mem-rte-staleness-propagation) and
[EPI-RTE-schema-migration](epistemic.md#epi-rte-schema-migration).

Requested context selection is pull even though code chooses related IDs.
Likewise lexical search on request does not establish inferred-lexical push.
Unestablished specialized consumers prevent an axis-wide pull-only conclusion
and therefore prevent read-back signal from being wholly inapplicable. Raw
stdout/evidence retention establishes trace-extracted lineage, not qualifying
trace learning. No positive trace-source finding follows without that qualifying
route; nor do the records supply an exhaustive absence warrant. See
[RT-RTE-compile-run](runtime.md#rt-rte-compile-run),
[MEM-RTE-canonical-query](memory.md#mem-rte-canonical-query),
[MEM-OBJ-canonical-records](memory.md#mem-obj-canonical-records),
[MEM-OBJ-run](memory.md#mem-obj-run) and
[MEM-OBJ-evidence](memory.md#mem-obj-evidence).

Reconciliation resolves duplicate epistemic Run, Evidence, clarification, query,
finding-review and stale-propagation referents to the corresponding memory
records. All citations here use those canonical destinations. Canonical family
containers and their epistemic parts, and grouped maintenance/policy routes and
their distinct operations, remain nonsuperseded; their scopes are not collapsed.
No value is upgraded by supersession. There is no supplied observed execution
or causal comparison supporting stronger bases than the recorded wiring.

Source-read log: none. This profile uses only the supplied accepted members and
reconciliation; it adds no source evidence or records.
