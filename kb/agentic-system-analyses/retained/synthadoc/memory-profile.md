---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Synthadoc memory comparison: retained wiki products, access/control state, trace compilation
  and unresolved host/peer alternatives at the frozen revision.'
run-id: AAS-2026-10-15-synthadoc-a3cae9152fff-01
source-identity: https://github.com/axoviq-ai/synthadoc
reviewed-boundary: b80d9388a3013e8051baf2854c7250942c46e91a
memory-comparison:
  version: 2
  scope: 'Accumulated wiki/candidate bodies and frontmatter; extracted sidecars; stored chat turns and
    overflow summaries; lifecycle/fix snapshots; computation/answer and faithfulness caches; generated
    overview, purpose, index, routing and agent guidance; page-vector and BM25 access structures; exports
    and backup/restore copies; cross-wiki retained page/control consumption; their admission, maintenance
    and later-consumer routes. Included uncertainties: initial content/registry control, embedding population/refresh,
    unestablished summary/overview delivery, other workflow/client feedback, peer backing stores, hook-produced
    state and opaque coding-agent checkpoints at the integration boundary. Excluded: fixed shipped package
    instructions/protocols, model weights and provider internals, arbitrary external host implementations,
    current-run-only tool messages, transient request strings and raw source files except as inputs to
    retained derivations. No deployed operation or causal benefit is asserted.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Wiki and candidate Markdown bodies/frontmatter; extracted text/pagemaps; faithfulness JSON;
          overview; generated purpose/index/routing/instructions; exported bundles and backup archives
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-page-content
          - memory.md#mem-obj-page-metadata
          - memory.md#mem-obj-source-sidecars
          - memory.md#mem-obj-faithfulness-cache
          - memory.md#mem-obj-overview
          - memory.md#mem-rte-scaffold-guidance
          - runtime.md#rt-rte-candidate-admission
          - runtime.md#rt-rte-context-export
          - memory.md#mem-rte-backup-restore
          note: These retained parts are serialized in filesystem files. A backup archive is a file container,
            not evidence that every contained database has the same logical substrate.
        records: *id001
        note: The records identify the file-backed surfaces and separate live pages, staged pages, sidecars
          and snapshots. Raw originals are source inputs, not an additional inferred memory substrate.
      - scope: Stored chat turns/summary, lifecycle snapshots/events, fix history in AuditDB, response/query
          caches and page-vector rows
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-chat-messages
          - memory.md#mem-obj-lifecycle-history
          - memory.md#mem-obj-response-cache
          - memory.md#mem-obj-search-vectors
          note: SQLite rows retain these parts. Vector blobs remain SQLite-backed; the vector access structure
            is classified separately.
        records:
        - memory.md#mem-obj-chat-messages
        - memory.md#mem-obj-lifecycle-history
        - memory.md#mem-obj-response-cache
        - memory.md#mem-obj-search-vectors
        note: The accepted object records identify each durable store; page fix pointers also reside in
          file frontmatter.
      - scope: Persisted page embeddings used to rerank BM25 candidates
        assessment: known
        findings:
        - value: vector
          basis: wired
          records:
          - memory.md#mem-obj-search-vectors
          - runtime.md#rt-cmp-text-embedding
          note: Dense stored embeddings support vector similarity over the lexical candidate pool, not
            independent full-corpus vector retrieval.
        records:
        - memory.md#mem-obj-search-vectors
        - runtime.md#rt-cmp-text-embedding
        note: Vector is the operative access substrate alongside its SQLite persistence, not a claim that
          page vectors are trained model weights.
      - scope: Reloadable process-cached BM25 corpus/token lists as access structures
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-search-vectors
          - runtime.md#rt-rte-wiki-query
          - runtime.md#rt-cmp-text-embedding
          note: In-process corpus/token lists serve later retrieval until explicit invalidation; cached
            numerical model instances are excluded along with model weights.
        records:
        - memory.md#mem-obj-search-vectors
        - runtime.md#rt-rte-wiki-query
        - runtime.md#rt-cmp-text-embedding
        note: Includes access structures built over retained pages; excludes current tool-loop messages
          and transient request strings.
      - scope: Cross-wiki peer physical stores and registry backing
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-cross-wiki
        note: The coordinator reads peer pages and registry purpose summaries, but peer deployments and
          registry initialization are not audited. HTTP delivery does not establish service-object or
          any specific underlying peer storage.
      - scope: Included opaque coding-agent checkpoints and hook-produced retained state
        assessment: uninspected
        findings: []
        records: &id004
        - runtime.md#rt-rte-provider-delegation
        - runtime.md#rt-rte-extension-loading
        note: The accepted records leave native checkpoints and hook-produced state uninspected. Their
          storage substrates cannot be classified from subprocess invocation or executable capability
          alone. External implementations are excluded; the unresolved retained-state alternative at the
          integration boundary is not silently excluded.
      records:
      - memory.md#mem-obj-page-content
      - memory.md#mem-obj-page-metadata
      - memory.md#mem-obj-source-sidecars
      - memory.md#mem-obj-faithfulness-cache
      - memory.md#mem-obj-overview
      - memory.md#mem-rte-scaffold-guidance
      - runtime.md#rt-rte-candidate-admission
      - runtime.md#rt-rte-context-export
      - memory.md#mem-rte-backup-restore
      - memory.md#mem-obj-chat-messages
      - memory.md#mem-obj-lifecycle-history
      - memory.md#mem-obj-response-cache
      - memory.md#mem-obj-search-vectors
      - runtime.md#rt-cmp-text-embedding
      - runtime.md#rt-rte-wiki-query
      - memory.md#mem-rte-cross-wiki
      - runtime.md#rt-rte-provider-delegation
      - runtime.md#rt-rte-extension-loading
      note: File, SQLite, vector and in-memory witnesses classify inspected retained parts and access
        structures. Peer storage and opaque integration state prevent a complete substrate inventory.
        Configured model weights and shipped static prompts are outside this accumulated-memory scope.
    representational_form:
      assessment: partial
      units:
      - scope: Page/sidecar prose; interpreted notes and warning criticism; chat turns/summary; snapshot
          bodies; cached text; audit reasons; overview; purpose/instructions and exported page text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id002
          - memory.md#mem-obj-page-content
          - memory.md#mem-obj-page-metadata
          - memory.md#mem-obj-source-sidecars
          - memory.md#mem-obj-chat-messages
          - memory.md#mem-obj-lifecycle-history
          - memory.md#mem-obj-response-cache
          - memory.md#mem-obj-faithfulness-cache
          - memory.md#mem-obj-overview
          - memory.md#mem-rte-scaffold-guidance
          - runtime.md#rt-rte-context-export
          note: These parts receive meaning through model or human interpretation. The same containers
            also have separately classified fixed-rule metadata.
        records: *id002
        note: Readable text is not an opaque provider checkpoint. Summary and overview form is known even
          though delivery to an answering model is not established.
      - scope: Frontmatter control/provenance fields, citation locators, pagemaps, chat role/order/session
          IDs, snapshot/fix IDs, cache keys/action fields, verdict/freshness fields and routing/index
          access rules
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id003
          - memory.md#mem-obj-page-metadata
          - memory.md#mem-obj-source-sidecars
          - memory.md#mem-obj-chat-messages
          - memory.md#mem-obj-lifecycle-history
          - memory.md#mem-obj-response-cache
          - memory.md#mem-obj-faithfulness-cache
          - epistemic.md#epi-obj-citation-markers
          - epistemic.md#epi-obj-lint-warnings
          - memory.md#mem-rte-scaffold-guidance
          note: Localized fields are parsed by fixed selection, dispatch, lookup or recovery rules; warning
            cardinality is distinct from criticism prose.
        records: *id003
        note: Splits the operative symbolic parts from natural-language bodies/reasons, including mixed
          JSON and YAML containers.
      - scope: Dense stored page vectors at the rerank consumer
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-search-vectors
          - runtime.md#rt-cmp-text-embedding
          note: Dense numerical representations distribute page features across vector entries. This is
            not a model-weight update.
        records:
        - memory.md#mem-obj-search-vectors
        - runtime.md#rt-cmp-text-embedding
        note: Vector data form is established independently of unknown initial population and refresh
          completeness.
      - scope: Backup database bytes and optional included files not semantically inventoried
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-backup-restore
        note: The manifest and known text/database parts are described, but opaque archived bytes and
          optional sources cannot all be assigned a representational form from the manifest alone.
      - scope: Uninspected peer payload alternatives beyond the inspected page-text return
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-cross-wiki
        note: Returned page text is readable; this does not classify every retained peer part or registry
          provenance.
      - scope: Included opaque coding-agent checkpoints and hook-produced retained state
        assessment: uninspected
        findings: []
        records: *id004
        note: The accepted records leave native checkpoints and hook-produced state uninspected. Their
          operative forms and consumption paths cannot be classified from subprocess invocation or executable
          capability alone. External implementations are excluded; the unresolved retained-state alternative
          at the integration boundary is not silently excluded.
      records:
      - memory.md#mem-obj-page-content
      - memory.md#mem-obj-page-metadata
      - memory.md#mem-obj-source-sidecars
      - memory.md#mem-obj-chat-messages
      - memory.md#mem-obj-lifecycle-history
      - memory.md#mem-obj-response-cache
      - memory.md#mem-obj-faithfulness-cache
      - memory.md#mem-obj-overview
      - memory.md#mem-rte-scaffold-guidance
      - runtime.md#rt-rte-context-export
      - epistemic.md#epi-obj-citation-markers
      - epistemic.md#epi-obj-lint-warnings
      - memory.md#mem-obj-search-vectors
      - runtime.md#rt-cmp-text-embedding
      - memory.md#mem-rte-backup-restore
      - memory.md#mem-rte-cross-wiki
      - runtime.md#rt-rte-provider-delegation
      - runtime.md#rt-rte-extension-loading
      note: Natural-language, symbolic and distributed-parametric parts are kept separate. Readable summaries
        and backup manifests do not classify opaque consumed or archived payloads. Uninspected integration
        and peer alternatives prevent complete coverage.
    lineage:
      assessment: partial
      units:
      - scope: Extracted source text/sidecars, caller-supplied direct edits and exported/restored content
          on their acquisition paths
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-source-sidecars
          - runtime.md#rt-rte-client-write
          - memory.md#mem-rte-backup-restore
          - runtime.md#rt-rte-context-export
          note: External extraction output and caller content enter the wiki; exports/archives can be
            reloaded without becoming newly authored facts.
        records:
        - memory.md#mem-obj-source-sidecars
        - runtime.md#rt-rte-client-write
        - memory.md#mem-rte-backup-restore
        - runtime.md#rt-rte-context-export
        note: Classifies acquisition paths, not source truth or exact original authorship. An extraction
          skill may already have transformed the input.
      - scope: SessionSkill filtered user/assistant transcript to durable wiki pages
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-rte-session-ingest
          - runtime.md#rt-rte-source-ingest
          note: Imported conversational turns feed automatic compilation and later eligible page consumption;
            tool/thinking blocks are excluded.
        records:
        - memory.md#mem-rte-session-ingest
        - runtime.md#rt-rte-source-ingest
        note: The trace extraction path is established; it does not authenticate the original transcript
          or verify its claims.
      - scope: Generated pages and annotations, cached computation text, page vectors, overflow summaries,
          overview and scaffold-generated guidance on inspected derivation paths
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - runtime.md#rt-rte-source-ingest
          - epistemic.md#epi-rte-citation-annotation
          - memory.md#mem-obj-response-cache
          - memory.md#mem-obj-search-vectors
          - memory.md#mem-rte-session-context
          - memory.md#mem-obj-overview
          - memory.md#mem-rte-scaffold-guidance
          note: Software/model transformations derive retained representations from sources, prior text,
            domain/slugs or prior turns. This value does not assert semantic preservation or novelty.
        records:
        - runtime.md#rt-rte-source-ingest
        - epistemic.md#epi-rte-citation-annotation
        - memory.md#mem-obj-response-cache
        - memory.md#mem-obj-search-vectors
        - memory.md#mem-rte-session-context
        - memory.md#mem-obj-overview
        - memory.md#mem-rte-scaffold-guidance
        note: The separate trace-extracted session path remains visible rather than treating all compilation
          as one provenance. Numerical embedding derivation does not resolve training provenance.
      - scope: Initial deployed page/purpose/routing/registry content and embedding population; detailed
          extraction-skill provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-page-content
        - memory.md#mem-rte-scaffold-guidance
        - memory.md#mem-rte-cross-wiki
        - memory.md#mem-obj-search-vectors
        - memory.md#mem-obj-source-sidecars
        note: Accepted records leave initial authorship/admission and some derivation paths unresolved.
          Possible manual changes and preserved user zones do not establish a complete authored lineage
          or the origin of every embedding.
      - scope: Included opaque coding-agent checkpoints and hook-produced retained state
        assessment: uninspected
        findings: []
        records: *id004
        note: The accepted records leave native checkpoints and hook-produced state uninspected. Their
          content provenance cannot be classified from subprocess invocation or executable capability
          alone. External implementations are excluded; the unresolved retained-state alternative at the
          integration boundary is not silently excluded.
      records:
      - memory.md#mem-obj-source-sidecars
      - runtime.md#rt-rte-client-write
      - memory.md#mem-rte-backup-restore
      - runtime.md#rt-rte-context-export
      - memory.md#mem-rte-session-ingest
      - runtime.md#rt-rte-source-ingest
      - epistemic.md#epi-rte-citation-annotation
      - memory.md#mem-obj-response-cache
      - memory.md#mem-obj-search-vectors
      - memory.md#mem-rte-session-context
      - memory.md#mem-obj-overview
      - memory.md#mem-rte-scaffold-guidance
      - memory.md#mem-obj-page-content
      - memory.md#mem-rte-cross-wiki
      - runtime.md#rt-rte-provider-delegation
      - runtime.md#rt-rte-extension-loading
      note: Imported, trace-extracted and other-compiled paths coexist. Known subsequent compilation does
        not establish initial authored provenance, embedding-model provenance, or provenance of opaque
        alternatives. No authored finding is inferred solely from an editable file or a generic caller.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Page/sidecar bodies, raw recent session turns, cached answers and restored bodies at answering,
          maintenance, source-review and requested export consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-page-content
          - memory.md#mem-obj-source-sidecars
          - memory.md#mem-rte-session-context
          - memory.md#mem-obj-response-cache
          - runtime.md#rt-rte-context-export
          - memory.md#mem-rte-health-history
          note: Reloaded prose supplies reference/context or an answer; cached answers can directly replace
            new synthesis. Advice is not a guarantee of semantic reliance or truth.
        records:
        - memory.md#mem-obj-page-content
        - memory.md#mem-obj-source-sidecars
        - memory.md#mem-rte-session-context
        - memory.md#mem-obj-response-cache
        - runtime.md#rt-rte-context-export
        - memory.md#mem-rte-health-history
        note: The named consumers are wired. External direct readers receive text, but their subsequent
          model use is only afforded.
      - scope: Generated purpose at later ingest and generated instruction files at external host loading
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-rte-scaffold-guidance
          note: Retained purpose supplies standing scope guidance to later ingest decisions.
        - value: instruction
          basis: afforded
          records:
          - memory.md#mem-rte-scaffold-guidance
          note: Generated agent files can supply standing directions if the external host loads them;
            host loading is not established.
        records:
        - memory.md#mem-rte-scaffold-guidance
        note: The wired purpose path and afforded external instruction path keep their different warrants;
          actual host delivery/compliance is not claimed.
      - scope: Page text/titles/tags/aliases and stored vectors at lexical scoring and optional vector
          reranking
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-page-metadata
          - memory.md#mem-obj-search-vectors
          - runtime.md#rt-rte-wiki-query
          note: Retained text/features determine relative retrieval priority even though scoring code
            is fixed.
        records:
        - memory.md#mem-obj-page-metadata
        - memory.md#mem-obj-search-vectors
        - runtime.md#rt-rte-wiki-query
        note: Both lexical inputs and dense ranking features are included, without implying learned scoring
          policy.
      - scope: Lifecycle eligibility and retained warning count at ordinary search and auto-resolution
          gates
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records:
          - epistemic.md#epi-obj-lifecycle-state
          - epistemic.md#epi-obj-lint-warnings
          - epistemic.md#epi-rte-warning-gate
          - runtime.md#rt-rte-wiki-query
          note: Stored status excludes noneligible pages from ordinary search; persisted warning count
            can veto auto-resolution.
        - value: validation
          basis: wired
          records:
          - epistemic.md#epi-obj-lint-warnings
          - epistemic.md#epi-rte-warning-gate
          note: Persisted warning count is compared with a configured threshold to determine whether automatic
            resolution is admissible.
        records:
        - epistemic.md#epi-obj-lifecycle-state
        - epistemic.md#epi-obj-lint-warnings
        - epistemic.md#epi-rte-warning-gate
        - runtime.md#rt-rte-wiki-query
        note: The veto is consumer-specific. It does not cover direct reads/default OKF export or certify
          factual acceptance.
      - scope: Routing/index/registry state, provenance/dedup fields, cached action fields, summary coverage
          counters, faithfulness freshness keys, scan-cycle timestamps and recovery snapshot/fix pointers
          at later software decisions
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-rte-scaffold-guidance
          - memory.md#mem-rte-cross-wiki
          - memory.md#mem-obj-page-metadata
          - memory.md#mem-obj-response-cache
          - memory.md#mem-rte-session-context
          - epistemic.md#epi-rte-faithfulness-audit
          - memory.md#mem-rte-sensitive-mask
          - memory.md#mem-rte-health-history
          note: Retained controls choose scope, whether work repeats, dispatched action, audit/scan input
            windows or the historical body to restore.
        records:
        - memory.md#mem-rte-scaffold-guidance
        - memory.md#mem-rte-cross-wiki
        - memory.md#mem-obj-page-metadata
        - memory.md#mem-obj-response-cache
        - memory.md#mem-rte-session-context
        - epistemic.md#epi-rte-faithfulness-audit
        - memory.md#mem-rte-sensitive-mask
        - memory.md#mem-rte-health-history
        note: Names actual selector effects. Semantic summary text and faithfulness reasons do not become
          answering instructions merely because adjacent counters/keys are consumed.
      - scope: Retained imported session text at the compilation/update consumer
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-rte-session-ingest
          - runtime.md#rt-rte-source-ingest
          note: Recorded experience feeds automatic production of durable knowledge pages that can shape
            later answers. Learning authority here describes the update consumer, not measured capacity
            improvement.
        records:
        - memory.md#mem-rte-session-ingest
        - runtime.md#rt-rte-source-ingest
        note: This path is distinct from the derived page knowledge authority and does not entail weight
          training or revised general methods.
      - scope: Cached faithfulness reasons/verdicts at reviewing clients and CLI result consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - epistemic.md#epi-rte-faithfulness-audit
          - memory.md#mem-obj-faithfulness-cache
          note: Retained audit reasons/verdicts supply scoped evidence/advice to review displays.
        - value: enforcement
          basis: wired
          records:
          - epistemic.md#epi-rte-faithfulness-audit
          note: The cached drift/hallucination predicate determines the audit CLI nonzero result; no automatic
            page rewrite or demotion follows.
        records:
        - epistemic.md#epi-rte-faithfulness-audit
        - memory.md#mem-obj-faithfulness-cache
        note: CLI status has a bounded software effect. Unknown downstream shell policy is not a new enforced
          page-admission gate.
      - scope: Overview, semantic overflow summary and opaque backup payloads at possible downstream semantic
          consumers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-overview
        - memory.md#mem-rte-session-context
        - memory.md#mem-rte-backup-restore
        note: Creation/storage is established, but a later model consumer of overview or overflow-summary
          text is not. Backup manifest inspection does not resolve every restored payload consumer. No
          authority is assigned to unconsumed metadata or text.
      - scope: Included opaque coding-agent checkpoints and hook-produced retained state
        assessment: uninspected
        findings: []
        records: *id004
        note: The accepted records leave native checkpoints and hook-produced state uninspected. Their
          retained parts, actual consumers and effects cannot be classified from subprocess invocation
          or executable capability alone. External implementations are excluded; the unresolved retained-state
          alternative at the integration boundary is not silently excluded.
      records:
      - memory.md#mem-obj-page-content
      - memory.md#mem-obj-source-sidecars
      - memory.md#mem-rte-session-context
      - memory.md#mem-obj-response-cache
      - runtime.md#rt-rte-context-export
      - memory.md#mem-rte-health-history
      - memory.md#mem-rte-scaffold-guidance
      - memory.md#mem-obj-page-metadata
      - memory.md#mem-obj-search-vectors
      - runtime.md#rt-rte-wiki-query
      - epistemic.md#epi-obj-lifecycle-state
      - epistemic.md#epi-obj-lint-warnings
      - epistemic.md#epi-rte-warning-gate
      - memory.md#mem-rte-cross-wiki
      - epistemic.md#epi-rte-faithfulness-audit
      - memory.md#mem-rte-sensitive-mask
      - memory.md#mem-rte-session-ingest
      - runtime.md#rt-rte-source-ingest
      - memory.md#mem-obj-faithfulness-cache
      - memory.md#mem-obj-overview
      - memory.md#mem-rte-backup-restore
      - runtime.md#rt-rte-provider-delegation
      - runtime.md#rt-rte-extension-loading
      note: Knowledge, instruction, ranking, routing, enforcement, validation and trace-update learning
        have distinct local consumers. Known generation or permission cannot upgrade opaque alternatives.
        Coverage remains partial because semantic summary/overview delivery and external state consumers
        are unresolved.
    write_agency:
      assessment: partial
      units:
      - scope: Ingest/annotation, overflow-summary/cache admission, overview/scaffold regeneration, lint/automatic
          lifecycle/warning changes, verdict caching and enabled server masking
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-source-ingest
          - epistemic.md#epi-rte-citation-annotation
          - memory.md#mem-rte-session-context
          - memory.md#mem-obj-response-cache
          - memory.md#mem-obj-overview
          - memory.md#mem-rte-scaffold-guidance
          - runtime.md#rt-rte-lint-repair
          - epistemic.md#epi-rte-lifecycle-admission
          - epistemic.md#epi-rte-warning-gate
          - epistemic.md#epi-rte-faithfulness-audit
          - memory.md#mem-rte-sensitive-mask
          note: Software/model admits the generated or transformed content without a per-result human
            decision. Starting a job and selecting configuration do not make that admission manual.
        records:
        - runtime.md#rt-rte-source-ingest
        - epistemic.md#epi-rte-citation-annotation
        - memory.md#mem-rte-session-context
        - memory.md#mem-obj-response-cache
        - memory.md#mem-obj-overview
        - memory.md#mem-rte-scaffold-guidance
        - runtime.md#rt-rte-lint-repair
        - epistemic.md#epi-rte-lifecycle-admission
        - epistemic.md#epi-rte-warning-gate
        - epistemic.md#epi-rte-faithfulness-audit
        - memory.md#mem-rte-sensitive-mask
        note: Includes known subsequent transformations regardless of unresolved initialization. Default/force/staging
          alternatives are not merged into a human-review guarantee.
      - scope: CLI sensitive masking on the confirmed --apply path
        assessment: known
        findings:
        - value: manual
          basis: wired
          records:
          - memory.md#mem-rte-sensitive-mask
          note: CLI apply normally asks the operator to approve the masking write; this is an explicit
            approval mechanism, distinct from workflow start and automatic server scans.
        records:
        - memory.md#mem-rte-sensitive-mask
        note: Only the confirmed CLI branch is classified manual. The --yes bypass does not establish
          a fresh per-content human decision.
      - scope: Candidate promotion/discard, direct MCP replacement, workflow client-gated fixes/rollback
          and HTTP snapshot replacement
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-candidate-admission
        - runtime.md#rt-rte-client-write
        - workflow.md#wf-rte-content-health
        - memory.md#mem-rte-health-history
        - epistemic.md#epi-rte-snapshot-rollback
        note: These callers supply content, movement decisions or approval booleans, but accepted records
          explicitly leave human identity/control unresolved. A client confirmation is not automatically
          a human decision; software I/O is not automatic admission independent of the caller either.
      - scope: Initial content and purpose/routing/registry admission, embedding refresh/population and
          backup restore caller control
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-scaffold-guidance
        - memory.md#mem-rte-cross-wiki
        - memory.md#mem-obj-search-vectors
        - memory.md#mem-rte-backup-restore
        note: Subsequent scaffold software adoption is known; exact deployed initialization and restore/refresh
          control are not. Engine capability alone cannot classify operator approval.
      - scope: Included opaque coding-agent checkpoints and hook-produced retained state
        assessment: uninspected
        findings: []
        records: *id004
        note: The accepted records leave native checkpoints and hook-produced state uninspected. Their
          write/admission control cannot be classified from subprocess invocation or executable capability
          alone. External implementations are excluded; the unresolved retained-state alternative at the
          integration boundary is not silently excluded.
      records:
      - runtime.md#rt-rte-source-ingest
      - epistemic.md#epi-rte-citation-annotation
      - memory.md#mem-rte-session-context
      - memory.md#mem-obj-response-cache
      - memory.md#mem-obj-overview
      - memory.md#mem-rte-scaffold-guidance
      - runtime.md#rt-rte-lint-repair
      - epistemic.md#epi-rte-lifecycle-admission
      - epistemic.md#epi-rte-warning-gate
      - epistemic.md#epi-rte-faithfulness-audit
      - memory.md#mem-rte-sensitive-mask
      - runtime.md#rt-rte-candidate-admission
      - runtime.md#rt-rte-client-write
      - workflow.md#wf-rte-content-health
      - memory.md#mem-rte-health-history
      - epistemic.md#epi-rte-snapshot-rollback
      - memory.md#mem-rte-cross-wiki
      - memory.md#mem-obj-search-vectors
      - memory.md#mem-rte-backup-restore
      - runtime.md#rt-rte-provider-delegation
      - runtime.md#rt-rte-extension-loading
      note: Automatic content admission and an explicit operator-confirmed CLI branch are supported. Generic
        API callers and session confirmation do not establish manual agency. Unknown initial, client-mediated
        and opaque write mechanisms keep this axis partial.
    curation_operations:
      assessment: partial
      units:
      - scope: Overflow summarization of retained old session turns
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-session-context
          - memory.md#mem-obj-chat-messages
          note: The summary model compresses retained messages into a reduced representation of facts/decisions;
            retaining raw messages does not negate consolidation.
        records:
        - memory.md#mem-rte-session-context
        - memory.md#mem-obj-chat-messages
        note: Transformation/admission is wired even though summary-to-answer delivery is not established.
          The requested preservation does not certify fidelity.
      - scope: Existing-page update/merge, automatic lint rewrite/link cleanup, sensitive masking, content-health
          replacement and body rollback
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-rte-source-ingest
          - runtime.md#rt-rte-lint-repair
          - epistemic.md#epi-rte-link-cleanup
          - memory.md#mem-rte-sensitive-mask
          - workflow.md#wf-rte-content-health
          - memory.md#mem-rte-health-history
          - epistemic.md#epi-rte-snapshot-rollback
          note: These implemented routes revise existing retained entries, including restoring a previous
            body or redacting matched text; none requires that revision be an improvement.
        records:
        - runtime.md#rt-rte-source-ingest
        - runtime.md#rt-rte-lint-repair
        - epistemic.md#epi-rte-link-cleanup
        - memory.md#mem-rte-sensitive-mask
        - workflow.md#wf-rte-content-health
        - memory.md#mem-rte-health-history
        - epistemic.md#epi-rte-snapshot-rollback
        note: Requested structural-only repair is not upgraded into proven semantic preservation. Actual
          replacement is independently wired.
      - scope: Warning demotion and source-unavailability lifecycle withdrawal
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records:
          - epistemic.md#epi-rte-warning-gate
          - epistemic.md#epi-rte-lifecycle-admission
          note: Contradicted/archive state with retained history withdraws ordinary-search reliance rather
            than deleting every copy.
        records:
        - epistemic.md#epi-rte-warning-gate
        - epistemic.md#epi-rte-lifecycle-admission
        note: Invalidation is bounded to consumers that honor state; direct reads and export can still
          expose withdrawn content.
      - scope: Draft activation and staged-candidate movement into the live library
        assessment: known
        findings:
        - value: promote
          basis: wired
          records:
          - epistemic.md#epi-rte-lifecycle-admission
          - runtime.md#rt-rte-candidate-admission
          note: Draft activation raises retrieval eligibility; candidate promotion raises storage/admission
            tier. Moving a draft live need not make it query-eligible.
        records:
        - epistemic.md#epi-rte-lifecycle-admission
        - runtime.md#rt-rte-candidate-admission
        note: Tier/eligibility change is implemented, not evidence-consuming factual acceptance.
      - scope: Semantic operation of general compilation/annotation, overview/scaffold generation and
          uninspected maintenance alternatives
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-source-ingest
        - epistemic.md#epi-rte-citation-annotation
        - memory.md#mem-obj-overview
        - memory.md#mem-rte-scaffold-guidance
        - workflow.md#wf-rte-content-health
        note: The records do not establish a new claim absent from inputs, or exhaustive semantic preservation
          for general outputs. No synthesize value follows from an agent named synthesis; dedup checks,
          acquisition and index rebuilds alone do not establish curation dedup. Other workflow transformations
          remain uninspected.
      - scope: Included opaque coding-agent checkpoints and hook-produced retained state
        assessment: uninspected
        findings: []
        records: *id004
        note: The accepted records leave native checkpoints and hook-produced state uninspected. Their
          implemented curation transformations cannot be classified from subprocess invocation or executable
          capability alone. External implementations are excluded; the unresolved retained-state alternative
          at the integration boundary is not silently excluded.
      records:
      - memory.md#mem-rte-session-context
      - memory.md#mem-obj-chat-messages
      - runtime.md#rt-rte-source-ingest
      - runtime.md#rt-rte-lint-repair
      - epistemic.md#epi-rte-link-cleanup
      - memory.md#mem-rte-sensitive-mask
      - workflow.md#wf-rte-content-health
      - memory.md#mem-rte-health-history
      - epistemic.md#epi-rte-snapshot-rollback
      - epistemic.md#epi-rte-warning-gate
      - epistemic.md#epi-rte-lifecycle-admission
      - runtime.md#rt-rte-candidate-admission
      - epistemic.md#epi-rte-citation-annotation
      - memory.md#mem-obj-overview
      - memory.md#mem-rte-scaffold-guidance
      - runtime.md#rt-rte-provider-delegation
      - runtime.md#rt-rte-extension-loading
      note: Consolidation, entry evolution, bounded invalidation and promotion have inspected mechanisms.
        General semantic compilation, all workflow alternatives and opaque state remain unresolved; no
        unsupported dedup, decay or synthesis finding is inferred from command names or storage cleanup
        alone.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested local/cross-wiki query, context pack, direct read, export/bundle answering and
          cached requested-answer return
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-wiki-query
          - runtime.md#rt-rte-context-export
          - memory.md#mem-rte-cross-wiki
          - memory.md#mem-obj-response-cache
          note: Consumers request retained knowledge/answers; automatic ranking and delivery within those
            requests do not create a second unsolicited push.
        records:
        - runtime.md#rt-rte-wiki-query
        - runtime.md#rt-rte-context-export
        - memory.md#mem-rte-cross-wiki
        - memory.md#mem-obj-response-cache
        note: Pull includes internal selectors serving the request. Actual external host use beyond returned
          material remains unobserved.
      - scope: Requested repair page reads, audit displays and historical snapshot/fix-record recovery
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - workflow.md#wf-rte-content-health
          - memory.md#mem-rte-health-history
          - epistemic.md#epi-rte-snapshot-rollback
          - epistemic.md#epi-rte-faithfulness-audit
          note: Maintenance/review/recovery requests cause explicit reads of pages, verdicts or historical
            bodies.
        records:
        - workflow.md#wf-rte-content-health
        - memory.md#mem-rte-health-history
        - epistemic.md#epi-rte-snapshot-rollback
        - epistemic.md#epi-rte-faithfulness-audit
        note: A requested slug/index on rollback is not itself targeted push.
      - scope: Automatic recent-session history supply to a later streaming query
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-session-context
          - memory.md#mem-obj-chat-messages
          note: On a session query the server automatically reloads and supplies recent stored turns as
            answering context; the caller need not separately request those memory turns.
        records:
        - memory.md#mem-rte-session-context
        - memory.md#mem-obj-chat-messages
        note: Separates history enrichment from the requested wiki answer. The overflow summary text is
          not included in this push.
      - scope: Standing purpose/routing and retained control state read automatically by later ingest,
          retrieval, auditing, scanning and overflow decisions
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-scaffold-guidance
          - memory.md#mem-obj-page-metadata
          - memory.md#mem-obj-response-cache
          - epistemic.md#epi-rte-faithfulness-audit
          - memory.md#mem-rte-sensitive-mask
          - memory.md#mem-rte-session-context
          note: Invocations automatically load standing scope and controls to select inputs/work or reuse
            a prior decision without a request for those retained controls themselves.
        records:
        - memory.md#mem-rte-scaffold-guidance
        - memory.md#mem-obj-page-metadata
        - memory.md#mem-obj-response-cache
        - epistemic.md#epi-rte-faithfulness-audit
        - memory.md#mem-rte-sensitive-mask
        - memory.md#mem-rte-session-context
        note: Control consumption is distinct from independent foreground prose delivery. Background writes
          alone are not push.
      - scope: Overview/overflow-summary semantic read-back, backup-restored payload reload and external
          generated-instruction loading
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-overview
        - memory.md#mem-rte-session-context
        - memory.md#mem-rte-backup-restore
        - memory.md#mem-rte-scaffold-guidance
        note: Summary/overview production does not establish semantic read-back; restoration makes bytes
          available but actual reload is unobserved; the host loading route is only afforded and does
          not fix direction.
      - scope: Included opaque coding-agent checkpoints and hook-produced retained state
        assessment: uninspected
        findings: []
        records: *id004
        note: The accepted records leave native checkpoints and hook-produced state uninspected. Their
          later read-back chains cannot be classified from subprocess invocation or executable capability
          alone. External implementations are excluded; the unresolved retained-state alternative at the
          integration boundary is not silently excluded.
      records:
      - runtime.md#rt-rte-wiki-query
      - runtime.md#rt-rte-context-export
      - memory.md#mem-rte-cross-wiki
      - memory.md#mem-obj-response-cache
      - workflow.md#wf-rte-content-health
      - memory.md#mem-rte-health-history
      - epistemic.md#epi-rte-snapshot-rollback
      - epistemic.md#epi-rte-faithfulness-audit
      - memory.md#mem-rte-session-context
      - memory.md#mem-obj-chat-messages
      - memory.md#mem-rte-scaffold-guidance
      - memory.md#mem-obj-page-metadata
      - memory.md#mem-rte-sensitive-mask
      - memory.md#mem-obj-overview
      - memory.md#mem-rte-backup-restore
      - runtime.md#rt-rte-provider-delegation
      - runtime.md#rt-rte-extension-loading
      note: Both requested pull and automatic context/control supply are supported at separate operations.
        Internal ranking in a requested query is not re-counted as push. Unknown host, summary/overview
        and recovery consumption prevent complete direction coverage.
    read_back_signal:
      assessment: partial
      units:
      - scope: Automatic session-history push on /query/stream
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-session-context
          - memory.md#mem-obj-chat-messages
          note: 'Trigger: session streaming query. Selector input: supplied session ID. Selected part:
            stored messages belonging to that identity, delivered as recent raw history.'
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-session-context
          note: Within the identified session, configured turn-pair count and recency select a raw tail;
            QueryAgent character budget can trim it further. This is coarse window/budget filtering, not
            lexical relevance.
        records:
        - memory.md#mem-rte-session-context
        - memory.md#mem-obj-chat-messages
        note: Actual row identity selection and subsequent coarse tail selection are separate operations.
          Stored summary text is not selected for synthesis.
      - scope: Automatic standing purpose/routing and global controls supply
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-scaffold-guidance
          - memory.md#mem-rte-session-context
          - memory.md#mem-rte-sensitive-mask
          note: 'Trigger: later ingest/streaming retrieval or maintenance cycle. Selector inputs: availability
            of standing purpose/routing, session overflow controls or last-cycle state. Selected parts:
            the standing file/control values, not question-ranked fragments.'
        records:
        - memory.md#mem-rte-scaffold-guidance
        - memory.md#mem-rte-session-context
        - memory.md#mem-rte-sensitive-mask
        note: Downstream routing keyword tests can select work/scope without establishing that retained
          routing-file fragments were themselves selected by lexical matching for delivery.
      - scope: Automatic cached decision reuse, per-page provenance/control and stale-audit state
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-obj-response-cache
          - memory.md#mem-obj-page-metadata
          - epistemic.md#epi-rte-faithfulness-audit
          note: 'Trigger: subsequent compilation or audit. Cache key/source hash/page slug identity selects
            the retained decision or per-page control entry that software consumes. Faithfulness page-key
            comparison then controls re-audit selection.'
        records:
        - memory.md#mem-obj-response-cache
        - memory.md#mem-obj-page-metadata
        - epistemic.md#epi-rte-faithfulness-audit
        note: The selected retained control record has an identity consumer; this differs from merely
          naming a requested file. Does not classify requested cached-answer delivery as unsolicited push.
      - scope: Other included host/opaque, overview/summary and restored-payload selection
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-overview
        - memory.md#mem-rte-session-context
        - memory.md#mem-rte-backup-restore
        - memory.md#mem-rte-scaffold-guidance
        - runtime.md#rt-rte-provider-delegation
        - runtime.md#rt-rte-extension-loading
        note: Direction/selection is unresolved for these alternatives. A known pull route cannot make
          their push signal inapplicable; a display summary cannot identify an opaque selector.
      records:
      - memory.md#mem-rte-session-context
      - memory.md#mem-obj-chat-messages
      - memory.md#mem-rte-scaffold-guidance
      - memory.md#mem-rte-sensitive-mask
      - memory.md#mem-obj-response-cache
      - memory.md#mem-obj-page-metadata
      - epistemic.md#epi-rte-faithfulness-audit
      - memory.md#mem-obj-overview
      - memory.md#mem-rte-backup-restore
      - runtime.md#rt-rte-provider-delegation
      - runtime.md#rt-rte-extension-loading
      note: Identifier and coarse signals describe supported automatic supply operations. Lexical and
        embedding relevance in requested knowledge retrieval do not automatically become push signals.
        Incomplete direction coverage prevents a pull-only/inapplicable assessment.
    trace_learning:
      assessment: partial
      units:
      - scope: Imported JSONL conversational trace to admitted durable wiki page to later eligible query
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-session-ingest
          - runtime.md#rt-rte-source-ingest
          - runtime.md#rt-rte-wiki-query
          note: Filtered recorded user/assistant turns feed automatic model/software page admission, and
            retained derived pages have a later answering consumer. This satisfies the write-route definition
            without observed improvement.
        records:
        - memory.md#mem-rte-session-ingest
        - runtime.md#rt-rte-source-ingest
        - runtime.md#rt-rte-wiki-query
        note: Manual workflow initiation is not per-page approval. The positive is architectural wiring,
          not proof that a transcript was ingested or improved future answers.
      - scope: Overflow summary production and raw-tail reload
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-session-context
        - memory.md#mem-obj-chat-messages
        note: Summary writing is automatic and trace-fed, but semantic summary delivery to a later answering
          consumer is not established. Raw-tail reload alone is not a learned transformation. Summary/count
          control reads do not establish use of the summary content as behavior-shaping guidance.
      - scope: Fix/recovery history, faithfulness evaluation cache, scan metadata, ordinary cached computations
          and benchmark score retention
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-health-history
        - epistemic.md#epi-rte-faithfulness-audit
        - memory.md#mem-rte-sensitive-mask
        - memory.md#mem-obj-response-cache
        - epistemic.md#epi-rte-answer-evaluation
        note: These records establish retention and some later control/review consumers, but do not completely
          establish an automatic trace-fed transformation into a durable behavior-shaping artifact on
          each route. Snapshotting bodies, storing raw evaluation outcomes or replaying cached text is
          not by itself qualifying trace learning. No local no is inferred without a bounded absence warrant.
      - scope: Other workflow/client feedback and initialized guidance alternatives
        assessment: not-determinable
        findings: []
        records:
        - workflow.md#wf-rte-content-health
        - memory.md#mem-rte-scaffold-guidance
        - runtime.md#rt-rte-workflow-loop
        note: The representative workflow changes products without revising shipped guidance; that is
          not a complete absence search for every trace-fed route. Initial guidance provenance and other
          feedback paths remain unresolved.
      - scope: Included opaque coding-agent checkpoints and hook-produced retained state
        assessment: uninspected
        findings: []
        records: *id004
        note: The accepted records leave native checkpoints and hook-produced state uninspected. Their
          automatic trace-fed writes and later consumers cannot be classified from subprocess invocation
          or executable capability alone. External implementations are excluded; the unresolved retained-state
          alternative at the integration boundary is not silently excluded.
      records:
      - memory.md#mem-rte-session-ingest
      - runtime.md#rt-rte-source-ingest
      - runtime.md#rt-rte-wiki-query
      - memory.md#mem-rte-session-context
      - memory.md#mem-obj-chat-messages
      - memory.md#mem-rte-health-history
      - epistemic.md#epi-rte-faithfulness-audit
      - memory.md#mem-rte-sensitive-mask
      - memory.md#mem-obj-response-cache
      - epistemic.md#epi-rte-answer-evaluation
      - workflow.md#wf-rte-content-health
      - memory.md#mem-rte-scaffold-guidance
      - runtime.md#rt-rte-workflow-loop
      - runtime.md#rt-rte-provider-delegation
      - runtime.md#rt-rte-extension-loading
      note: A wired yes is established for imported conversational trace compilation. Other retained traces,
        summaries and control histories do not supply bounded system-wide negatives. Unresolved routes
        remain included, so this axis is partial rather than known or absent.
    trace_source:
      assessment: partial
      units:
      - scope: Qualifying SessionSkill transcript-compilation write
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-rte-session-ingest
          note: Original inputs are recorded conversational user/assistant turns. SessionSkill format
            labels do not authenticate origin; tool_use, tool_result, thinking and image blocks are explicitly
            excluded.
        records:
        - memory.md#mem-rte-session-ingest
        note: Within the inspected qualifying extraction path, session-logs is supported. No tool-traces,
          event-streams or trajectories value follows from JSONL serialization or an assistant describing
          a tool.
      - scope: Overflow-summary route whose downstream semantic learning consumer is unresolved
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-session-context
        note: Its original content is known conversational turns, but the full qualifying trace-learning
          chain is unresolved. It is not added as a second positive learning-source route merely because
          a summary was stored.
      - scope: Recovery, evaluation/scan-control, benchmark, cached-computation and other workflow feedback
          alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-health-history
        - epistemic.md#epi-rte-faithfulness-audit
        - memory.md#mem-rte-sensitive-mask
        - epistemic.md#epi-rte-answer-evaluation
        - memory.md#mem-obj-response-cache
        - workflow.md#wf-rte-content-health
        note: Qualification and original trace-fed input are not fully established for each candidate.
          Audit/event labels alone do not establish event-streams; a page and sidecar judged by a model
          are not automatically tool-traces or a multi-step trajectory.
      - scope: Included opaque coding-agent checkpoints and hook-produced retained state
        assessment: uninspected
        findings: []
        records: *id004
        note: The accepted records leave native checkpoints and hook-produced state uninspected. Their
          qualifying trace-source contents and origin cannot be classified from subprocess invocation
          or executable capability alone. External implementations are excluded; the unresolved retained-state
          alternative at the integration boundary is not silently excluded.
      records:
      - memory.md#mem-rte-session-ingest
      - memory.md#mem-rte-session-context
      - memory.md#mem-rte-health-history
      - epistemic.md#epi-rte-faithfulness-audit
      - memory.md#mem-rte-sensitive-mask
      - epistemic.md#epi-rte-answer-evaluation
      - memory.md#mem-obj-response-cache
      - workflow.md#wf-rte-content-health
      - runtime.md#rt-rte-provider-delegation
      - runtime.md#rt-rte-extension-loading
      note: Session-logs is the supported source for the qualifying imported-transcript route. Other route
        qualification/origin remains unresolved. A local positive does not make all alternative sources
        absent, and unresolved learning routes prevent inapplicable coverage.
---

# Synthadoc memory profile

## Comparison rationale

This profile classifies accepted records, not a fresh source inspection. All positive findings are implementation wiring or the explicitly afforded external instruction-loading path. No source was read, no new record or quotation was added, and no observed-run or causal basis is inferred. Every axis remains partial because the accepted inventory includes unresolved parts; a strong local witness does not settle those alternatives.

### Objects, paths and uncertainty

The page body is natural-language knowledge; parsed frontmatter is not uniformly knowledge. Lifecycle fields enforce retrieval eligibility, warnings can veto automatic resolution, and routing/cache/recovery fields select later operations. Text/aliases and vectors also supply ranking inputs. SQLite persistence and vector access both apply to stored embeddings, independently of their distributed-parametric form. These distinctions follow [MEM-OBJ-page-metadata](memory.md#mem-obj-page-metadata), [MEM-OBJ-search-vectors](memory.md#mem-obj-search-vectors), [EPI-RTE-warning-gate](epistemic.md#epi-rte-warning-gate) and [MEM-BAP-retained-content](memory.md#mem-bap-retained-content). Ordinary model weights and fixed workflow instructions are not accumulated memory in this profile.

Known automatic compilation and scaffold regeneration do not resolve initial authorship or admission. API content suppliers, candidate callers and workflow confirmation clients are not authenticated humans in these records. The separately documented operator-confirmed CLI masking branch supports manual admission; automatic background masking supports automatic admission. A confirmation wrapper does not license a system-wide human-review finding. See [MEM-RTE-scaffold-guidance](memory.md#mem-rte-scaffold-guidance), [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission), [RT-RTE-client-write](runtime.md#rt-rte-client-write), [WF-RTE-content-health](workflow.md#wf-rte-content-health) and [MEM-RTE-sensitive-mask](memory.md#mem-rte-sensitive-mask).

### Curation and read-back

Overflow summarization consolidates retained turns even though the raw log remains. That transformation is not proof of summary-fed answering: the inspected handler supplies the recent raw tail, while the stored summary/count govern overflow control and notices. Overview has another known producer without an established semantic answering consumer. No negative trace-learning finding is inferred from either delivery gap. See [MEM-RTE-session-context](memory.md#mem-rte-session-context) and [MEM-OBJ-overview](memory.md#mem-obj-overview).

General compilation is not automatically synthesis in the controlled sense of creating a claim absent from its inputs. The accepted epistemic account leaves its semantic relation indeterminate. Existing-entry revisions, warning/lifecycle withdrawal, tier promotion and explicit session compression have narrower supported curation mappings. Structural rescanning after a content-health write does not veto the write or prove factual preservation. See [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [EPI-RTE-citation-annotation](epistemic.md#epi-rte-citation-annotation), [EPI-RTE-lifecycle-admission](epistemic.md#epi-rte-lifecycle-admission) and [WF-RTE-content-health](workflow.md#wf-rte-content-health).

Requested wiki/context/export/cached-answer retrieval is pull. Ranking inside that chain is not another unsolicited delivery. Automatic session-history enrichment and standing scope/control supply are separate push operations. The session ID actually selects retained turns before coarse recency/budget filtering; a requested rollback slug alone does not establish identifier push. Likewise BM25/vector relevance does not establish an inferred push signal merely because a query uses an automatic ranker. See [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-context-export](runtime.md#rt-rte-context-export), [MEM-RTE-session-context](memory.md#mem-rte-session-context) and [MEM-RTE-health-history](memory.md#mem-rte-health-history).

### Trace qualification and unions

The imported-transcript chain supports trace learning in the profile's write-route sense: recorded session turns feed automatic durable page production, and later queries can consume those pages. The input experience has learning authority at the update consumer; the resulting page has knowledge authority downstream. Neither classification establishes improved capacity, self-improvement, weight training or verified source claims. The recorded extraction excludes tool/thinking blocks, so session-logs does not imply tool-traces or trajectories. See [MEM-RTE-session-ingest](memory.md#mem-rte-session-ingest), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query).

Recovery snapshots, raw evaluation outcomes and scan counters have concrete consumers but are not silently upgraded into additional qualifying trace-learning transformations. Those units retain unresolved qualification/source rather than an unsupported no. Derived system unions therefore retain the wired yes and session-logs witness without claiming complete coverage or treating opaque alternatives as absent. Backup manifests and readable summaries do not resolve native provider checkpoints or arbitrary hook-written payloads. See [MEM-RTE-health-history](memory.md#mem-rte-health-history), [EPI-RTE-faithfulness-audit](epistemic.md#epi-rte-faithfulness-audit), [MEM-RTE-sensitive-mask](memory.md#mem-rte-sensitive-mask), [MEM-RTE-backup-restore](memory.md#mem-rte-backup-restore), [RT-RTE-provider-delegation](runtime.md#rt-rte-provider-delegation) and [RT-RTE-extension-loading](runtime.md#rt-rte-extension-loading).

### Canonical citations

Supersessions are resolved to the page-content and faithfulness-cache objects declared in memory; citation-audit routes resolve to the epistemic declaration; cross-wiki and sensitive-mask routes resolve to memory. These affect the object/form/storage/authority and audit/routing/maintenance citations, not their evidence strength. Their complementary findings survive reconciliation. The body/metadata, sidecar/extraction containers, generic/specialized workflow routes and the two rollback mechanisms remain distinct. No supersession supplies a missing trace-learning chain or upgrades an unobserved route. The corresponding canonical references are [MEM-OBJ-page-content](memory.md#mem-obj-page-content), [MEM-OBJ-faithfulness-cache](memory.md#mem-obj-faithfulness-cache), [EPI-RTE-faithfulness-audit](epistemic.md#epi-rte-faithfulness-audit), [MEM-RTE-cross-wiki](memory.md#mem-rte-cross-wiki) and [MEM-RTE-sensitive-mask](memory.md#mem-rte-sensitive-mask).
