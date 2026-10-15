---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Hindsight memory comparison at the frozen partial-loop boundary: facts, derived observations/pages,
  controls, curation and later delivery.'
run-id: AAS-2026-10-14-hindsight-34c2ca821edf-01
source-identity: https://github.com/vectorize-io/hindsight
reviewed-boundary: 610c135b6f2d0d8b972da94146ae635943f36271
memory-comparison:
  version: 2
  scope: Accumulated documents/chunks, extracted facts, observations, standing mental-model/page content,
    embeddings, provenance/access fields, refresh controls/grounding/history, directives, archive and
    bank overrides; shipped transcript admission, curation, recall/reflect, automatic maintenance, hook
    delivery, filesystem mirror and retained evaluation reporting. Alternative stores, attachments, other
    integrations/imports and embedded paths remain included but unresolved. Excludes static shipped instructions,
    current-request reflection working history, external host orchestration and provider-internal model
    weights/updates.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Default memory-store document/chunk text, fact and observation text, access/provenance
          fields and source metadata
        assessment: known
        findings:
        - value: rdbms
          basis: wired
          records: &id001
          - memory.md#mem-obj-document-text
          - memory.md#mem-obj-fact-text
          - memory.md#mem-obj-fact-embedding
          - memory.md#mem-obj-memory-lineage
          - memory.md#mem-obj-source-metadata
          - memory.md#mem-obj-observation-text
          note: Default relational storage holds these retained parts.
        records: *id001
        note: The default SQL path is classified separately from the configured store alternative.
      - scope: Fact retrieval vectors on the default database path
        assessment: known
        findings:
        - value: rdbms
          basis: wired
          records: &id002
          - memory.md#mem-obj-fact-embedding
          note: The default store persists the fact vector in the database.
        - value: vector
          basis: wired
          records: *id002
          note: The retained embedding is consumed by numerical similarity search.
        records: *id002
        note: Numerical encoding and vector access structure are distinct from the embedding model weights.
      - scope: SQL standing-page prose, tree, edit baseline, refresh controls/grounding/history, directives,
          archive and bank overrides
        assessment: known
        findings:
        - value: rdbms
          basis: wired
          records: &id003
          - memory.md#mem-obj-mental-model
          - memory.md#mem-obj-refresh-specification
          - memory.md#mem-obj-page-embedding
          - memory.md#mem-obj-knowledge-pages
          - memory.md#mem-obj-structured-content
          - memory.md#mem-obj-refresh-response
          - memory.md#mem-obj-directive-content
          - memory.md#mem-obj-curation-archive
          - runtime.md#rt-obj-bank-config
          note: These operative parts persist in SQL rows/JSON rather than current-request messages.
        records: *id003
        note: SQL page content survives even when an alternate store owns its search index.
      - scope: Page-search vector on the SQL-backed search path
        assessment: known
        findings:
        - value: rdbms
          basis: wired
          records: &id004
          - memory.md#mem-obj-page-embedding
          note: The default page search representation is stored as a database vector.
        - value: vector
          basis: wired
          records: *id004
          note: Semantic page search consumes this retained vector representation.
        records: *id004
        note: The alternate page-index owner remains a separate unresolved unit.
      - scope: CLI knowledge mirror and evaluation report files
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id005
          - memory.md#mem-rte-filesystem-mirror
          - memory.md#mem-rte-page-evaluation
          note: Synchronization writes Markdown/state and evaluation reporting optionally writes JSON.
        records: *id005
        note: File persistence is wired; later model reading of the mirror and full report consumers remain
          uninspected.
      - scope: Configured memory store, configured page index and attachment payloads
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-retain-work
        - memory.md#mem-obj-document-text
        - memory.md#mem-obj-fact-embedding
        - memory.md#mem-obj-page-embedding
        note: An extension may own rows or search outside PostgreSQL. Actual retained substrate and attachment
          storage are not established; an extension interface alone does not establish service-object
          or graph storage.
      - scope: Additional integration-local and embedded retained state
        assessment: uninspected
        findings: []
        records: &id028
        - memory.md#mem-rte-filesystem-mirror
        - memory.md#mem-rte-page-evaluation
        - runtime.md#rt-rte-claude-hooks
        - runtime.md#rt-rte-retain-work
        note: Additional shipped integrations, imports, attachments, embedded callers and alternate-store
          consumption remain incompletely inspected in the accepted records; complete system enumeration
          is prevented.
      records:
      - memory.md#mem-obj-document-text
      - memory.md#mem-obj-fact-text
      - memory.md#mem-obj-fact-embedding
      - memory.md#mem-obj-memory-lineage
      - memory.md#mem-obj-source-metadata
      - memory.md#mem-obj-observation-text
      - memory.md#mem-obj-mental-model
      - memory.md#mem-obj-refresh-specification
      - memory.md#mem-obj-page-embedding
      - memory.md#mem-obj-knowledge-pages
      - memory.md#mem-obj-structured-content
      - memory.md#mem-obj-refresh-response
      - memory.md#mem-obj-directive-content
      - memory.md#mem-obj-curation-archive
      - runtime.md#rt-obj-bank-config
      - memory.md#mem-rte-filesystem-mirror
      - memory.md#mem-rte-page-evaluation
      - runtime.md#rt-rte-retain-work
      - runtime.md#rt-rte-claude-hooks
      note: Known SQL, vector and file witnesses do not enumerate alternative stores or every shipped
        retained part. Provider inference weights and current-request lists are not added to the accumulated-memory
        inventory merely because they are used by the runtime.
    representational_form:
      assessment: partial
      units:
      - scope: Source document/chunk text, fact/observation prose, standing pages, directive prose and
          archive text/reasons
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id006
          - memory.md#mem-obj-document-text
          - memory.md#mem-obj-fact-text
          - memory.md#mem-obj-observation-text
          - memory.md#mem-obj-mental-model
          - memory.md#mem-obj-directive-content
          - memory.md#mem-obj-curation-archive
          note: Retained prose supplies source material, evidence, standing answers or instructions.
        records: *id006
        note: These text parts are interpreted by models or callers; their access fields are separate.
      - scope: Fact and page retrieval embeddings
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: &id007
          - memory.md#mem-obj-fact-embedding
          - memory.md#mem-obj-page-embedding
          note: Numerical search consumes dense distributed representations rather than localized symbols.
        records: *id007
        note: Dense inference outputs are not model parameters, but have distributed numerical encoding.
      - scope: Memory IDs/scopes/provenance, tree references and refresh scheduling/watermarks
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id008
          - memory.md#mem-obj-memory-lineage
          - memory.md#mem-obj-knowledge-pages
          - memory.md#mem-obj-refresh-specification
          note: Fixed code interprets IDs, scope, tree structure and maintenance windows.
        records: *id008
        note: The query text is split from fixed-rule controls.
      - scope: Refresh source query
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id009
          - memory.md#mem-obj-refresh-specification
          note: The source query requests model synthesis through interpreted text.
        records: *id009
        note: The same retained specification also contains separately classified symbolic fields.
      - scope: Structured document edit addresses and rendered bodies
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id010
          - memory.md#mem-obj-structured-content
          note: Localized blocks and edit operations have fixed addressing rules.
        - value: natural-language
          basis: wired
          records: *id010
          note: Block bodies and rendered Markdown are interpreted prose.
        records: *id010
        note: Both structure and body are recorded; a content reader need not receive edit addresses.
      - scope: Source metadata at its fixed-field and model-visible paths
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id011
          - memory.md#mem-obj-source-metadata
          note: Stored key/value fields have localized serialization.
        - value: natural-language
          basis: wired
          records: *id011
          note: A model interprets preserved source descriptions in tool results.
        records: *id011
        note: A serialized source stamp is not authenticated by its representation.
      - scope: Refresh grounding/outcomes/history and bank overrides
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id012
          - memory.md#mem-obj-refresh-response
          - runtime.md#rt-obj-bank-config
          note: IDs, outcomes and settings are read by fixed rules.
        - value: natural-language
          basis: wired
          records: *id012
          note: Supporting text and prompt-bearing values receive interpretive consumption.
        records: *id012
        note: Structured controls and outcomes differ from supporting prose, warnings and prompt-bearing
          settings.
      - scope: Filesystem mirror and evaluation JSON
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id013
          - memory.md#mem-rte-filesystem-mirror
          - memory.md#mem-rte-page-evaluation
          note: Markdown pages and verdict reasons contain interpreted text.
        - value: symbolic
          basis: wired
          records: *id013
          note: Local synchronization state and JSON verdict/identity fields have fixed structure.
        records: *id013
        note: The output projection is inspected, not every later consumer.
      - scope: Attachment payloads, alternate store internals and remaining integration state
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-filesystem-mirror
        - memory.md#mem-rte-page-evaluation
        - runtime.md#rt-rte-claude-hooks
        - runtime.md#rt-rte-retain-work
        - memory.md#mem-obj-document-text
        note: Additional shipped integrations, imports, attachments, embedded callers and alternate-store
          consumption remain incompletely inspected in the accepted records; complete system enumeration
          is prevented.
      records:
      - memory.md#mem-obj-document-text
      - memory.md#mem-obj-fact-text
      - memory.md#mem-obj-observation-text
      - memory.md#mem-obj-mental-model
      - memory.md#mem-obj-directive-content
      - memory.md#mem-obj-curation-archive
      - memory.md#mem-obj-fact-embedding
      - memory.md#mem-obj-page-embedding
      - memory.md#mem-obj-memory-lineage
      - memory.md#mem-obj-knowledge-pages
      - memory.md#mem-obj-refresh-specification
      - memory.md#mem-obj-structured-content
      - memory.md#mem-obj-source-metadata
      - memory.md#mem-obj-refresh-response
      - runtime.md#rt-obj-bank-config
      - memory.md#mem-rte-filesystem-mirror
      - memory.md#mem-rte-page-evaluation
      - runtime.md#rt-rte-claude-hooks
      - runtime.md#rt-rte-retain-work
      note: Mixed prose, fixed-rule fields and dense representations are split by operative part and path.
        Display text does not resolve opaque attachments or provider/store payloads.
    lineage:
      assessment: partial
      units:
      - scope: Submitted document/chunk content and caller source metadata
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id014
          - memory.md#mem-obj-document-text
          - memory.md#mem-obj-source-metadata
          note: Caller-supplied source content and stamps enter retained memory.
        records: *id014
        note: Origin truth, original authorship and screening fidelity remain unresolved.
      - scope: Claude Code transcript-derived fact content
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id015
          - runtime.md#rt-rte-claude-hooks
          - runtime.md#rt-rte-retain-work
          - memory.md#mem-obj-fact-text
          note: Automatic transcript selection feeds durable extracted facts for later prompts.
        records: *id015
        note: This is the concrete trace extraction branch, not every generic retain input.
      - scope: Derived observation text and refreshed standing-page content
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id016
          - memory.md#mem-obj-observation-text
          - memory.md#mem-rte-observation-consolidation
          - memory.md#mem-rte-page-maintenance
          note: Model proposals combine retained facts/observations or revise existing standing pages.
        records: *id016
        note: This lineage describes model transformation, not a claim of novel or warranted knowledge.
      - scope: Caller-supplied initial page and directive content
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id017
          - memory.md#mem-rte-page-maintenance
          - memory.md#mem-rte-directive-admission
          note: Creation can persist caller-authored Markdown or directive prose without a preceding synthesis.
        records: *id017
        note: Authored means supplied content rather than generated refresh output; it does not imply
          human admission.
      - scope: Fact/page embeddings, structured baseline and refreshed controls/grounding
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records: &id018
          - memory.md#mem-obj-fact-embedding
          - memory.md#mem-obj-page-embedding
          - memory.md#mem-obj-structured-content
          - memory.md#mem-obj-refresh-specification
          - memory.md#mem-obj-refresh-response
          note: Inference, canonicalization and maintenance compute durable representations or bookkeeping
            from inputs.
        records: *id018
        note: Known derivation does not freeze producing model provenance; complete embedding augmentation
          alternatives remain unresolved.
      - scope: Archive, filesystem mirror and evaluation report
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id019
          - memory.md#mem-obj-curation-archive
          - memory.md#mem-rte-filesystem-mirror
          - memory.md#mem-rte-page-evaluation
          note: Archive snapshots, API-derived Markdown and recorded verdicts are produced by software
            transformations.
        records: *id019
        note: Moving/copying content and serializing results is derivation, not new assertion synthesis.
      - scope: Generic retain input origin, initial controls/configuration and additional imports/integrations
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-retain-work
        - runtime.md#rt-rte-config-update
        - memory.md#mem-obj-memory-lineage
        - memory.md#mem-obj-refresh-specification
        note: Caller identity alone does not resolve original content provenance; verbatim modes, imports
          and additional integrations remain incompletely traced.
      records:
      - memory.md#mem-obj-document-text
      - memory.md#mem-obj-source-metadata
      - runtime.md#rt-rte-claude-hooks
      - runtime.md#rt-rte-retain-work
      - memory.md#mem-obj-fact-text
      - memory.md#mem-obj-observation-text
      - memory.md#mem-rte-observation-consolidation
      - memory.md#mem-rte-page-maintenance
      - memory.md#mem-rte-directive-admission
      - memory.md#mem-obj-fact-embedding
      - memory.md#mem-obj-page-embedding
      - memory.md#mem-obj-structured-content
      - memory.md#mem-obj-refresh-specification
      - memory.md#mem-obj-refresh-response
      - memory.md#mem-obj-curation-archive
      - memory.md#mem-rte-filesystem-mirror
      - memory.md#mem-rte-page-evaluation
      - runtime.md#rt-rte-config-update
      - memory.md#mem-obj-memory-lineage
      note: Known imported, authored, trace-extracted and compiled routes coexist. Generic ingress and
        initialization cannot inherit the concrete hook lineage; numerical model-output lineage does not
        establish immutable producer weights.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retrieved facts, observations, pages and source metadata at answer models
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id020
          - memory.md#mem-bap-reflect-content
          - runtime.md#rt-bap-hook-context
          - memory.md#mem-rte-recall-selection
          - memory.md#mem-rte-page-delivery
          note: Selected retained prose supplies evidence/context for answers and subsequent host work.
        records: *id020
        note: Internal reflection and external host-context channels remain distinct consumers; delivered
          evidence is not guaranteed reliance.
      - scope: Directive text at reflection prompt consumer
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id021
          - memory.md#mem-bap-directive-prompt
          - memory.md#mem-rte-directive-admission
          note: Active selected directive prose supplies standing imperative directions.
        records: *id021
        note: A prompt predicting rejection does not establish a response-level semantic veto.
      - scope: Fact text, fact/page embeddings and query/candidate representations at retrieval ranking
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id022
          - memory.md#mem-obj-fact-embedding
          - memory.md#mem-obj-page-embedding
          - memory.md#mem-cmp-cross-encoder
          - memory.md#mem-rte-recall-selection
          note: Retained representations and candidate text influence similarity, reranking and relative
            delivery priority.
        records: *id022
        note: Ranking modes vary; a cross-encoder is not universal to recall.
      - scope: Transcript-derived facts and retained evidence/baseline at automatic memory-update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id023
          - runtime.md#rt-rte-claude-hooks
          - memory.md#mem-rte-observation-consolidation
          - memory.md#mem-rte-page-maintenance
          note: Retained experience/evidence feeds consolidation or standing-page revision for later model
            context.
        records: *id023
        note: Learning authority here names input to durable artifact updates, not measured improved capacity.
      - scope: Stored source IDs, grounding and recalled-target membership at update/withdrawal gates
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id024
          - memory.md#mem-rte-observation-consolidation
          - memory.md#mem-obj-refresh-response
          - memory.md#mem-rte-page-maintenance
          - epistemic.md#epi-rte-source-withdrawal
          note: Live/resolvable source and target membership determines candidate admissibility or required
            retraction handling.
        - value: enforcement
          basis: wired
          records: *id024
          note: Code can veto actions, remove stale observations or preserve a prior page at these gates.
        records: *id024
        note: This authority belongs to the consumed lineage fields, not to truth of the associated prose.
      - scope: Refresh query/trigger/watermark, access scopes and bank configuration at operation selectors
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id025
          - memory.md#mem-obj-refresh-specification
          - memory.md#mem-obj-memory-lineage
          - runtime.md#rt-bap-config-consumer
          note: Retained controls select subsequent operation settings, input windows and scoped material.
        records: *id025
        note: Symbolic controls select operation scope/windows; query text shapes the maintenance input
          request.
      - scope: Archive reasons, full audit history, mirror/report later consumers and remaining shipped
          paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-curation-archive
        - memory.md#mem-obj-refresh-response
        - memory.md#mem-rte-filesystem-mirror
        - memory.md#mem-rte-page-evaluation
        note: Restoration and audit/report capability are recorded, but complete consequential downstream
          effects and additional integration consumers are uninspected. Unconsumed fields are not assigned
          authority.
      records:
      - memory.md#mem-bap-reflect-content
      - runtime.md#rt-bap-hook-context
      - memory.md#mem-rte-recall-selection
      - memory.md#mem-rte-page-delivery
      - memory.md#mem-bap-directive-prompt
      - memory.md#mem-rte-directive-admission
      - memory.md#mem-obj-fact-embedding
      - memory.md#mem-obj-page-embedding
      - memory.md#mem-cmp-cross-encoder
      - runtime.md#rt-rte-claude-hooks
      - memory.md#mem-rte-observation-consolidation
      - memory.md#mem-rte-page-maintenance
      - memory.md#mem-obj-refresh-response
      - epistemic.md#epi-rte-source-withdrawal
      - memory.md#mem-obj-refresh-specification
      - memory.md#mem-obj-memory-lineage
      - runtime.md#rt-bap-config-consumer
      - memory.md#mem-obj-curation-archive
      - memory.md#mem-rte-filesystem-mirror
      - memory.md#mem-rte-page-evaluation
      note: Authority follows the actual retained part and consumer. Evidence, standing directions, ranking
        inputs, update inputs and fixed-rule vetoes do not collapse into one force. Unknown downstream
        paths prevent a complete inventory.
    write_agency:
      assessment: partial
      units:
      - scope: Transcript-to-fact admission, observation proposals and automatic page refresh
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id026
          - runtime.md#rt-rte-claude-hooks
          - runtime.md#rt-rte-retain-work
          - memory.md#mem-rte-observation-consolidation
          - memory.md#mem-rte-page-maintenance
          note: Software/model selection and code gates admit durable content without per-content human
            decision.
        records: *id026
        note: Starting the host or maintenance workflow is not human approval of each admitted fact/edit.
      - scope: Derived indexes, archive/restore representation rebuilding, mirror and report writes
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id027
          - memory.md#mem-obj-fact-embedding
          - memory.md#mem-obj-page-embedding
          - memory.md#mem-rte-memory-curation
          - memory.md#mem-rte-filesystem-mirror
          - memory.md#mem-rte-page-evaluation
          note: Software computes and admits derived representations, mirrored bytes and evaluation records.
        records: *id027
        note: The derived-output admission is separate from unresolved control of the initiating caller
          edit.
      - scope: Generic retain ingress, caller page/directive creation, explicit curation and bank override
          replacement
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-retain-work
        - memory.md#mem-rte-page-maintenance
        - memory.md#mem-rte-directive-admission
        - memory.md#mem-rte-memory-curation
        - runtime.md#rt-rte-config-update
        note: The accepted records leave caller identity and per-item human control unresolved. Explicit
          API mutation alone establishes neither manual nor automatic admission for this initiating mechanism.
      - scope: Initial content, alternate stores and additional shipped integration admissions
        assessment: uninspected
        findings: []
        records: *id028
        note: Additional shipped integrations, imports, attachments, embedded callers and alternate-store
          consumption remain incompletely inspected in the accepted records; complete system enumeration
          is prevented.
      records:
      - runtime.md#rt-rte-claude-hooks
      - runtime.md#rt-rte-retain-work
      - memory.md#mem-rte-observation-consolidation
      - memory.md#mem-rte-page-maintenance
      - memory.md#mem-obj-fact-embedding
      - memory.md#mem-obj-page-embedding
      - memory.md#mem-rte-memory-curation
      - memory.md#mem-rte-filesystem-mirror
      - memory.md#mem-rte-page-evaluation
      - memory.md#mem-rte-directive-admission
      - runtime.md#rt-rte-config-update
      note: Automatic transformation/admission is supported locally. Manual is not asserted without an
        explicit human content decision; unresolved initialization and API callers remain in the inventory.
    curation_operations:
      assessment: partial
      units:
      - scope: Transcript extraction into durable facts
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id029
          - runtime.md#rt-rte-claude-hooks
          - runtime.md#rt-rte-retain-work
          - memory.md#mem-obj-fact-text
          note: Selected transcript content is compressed into later-retrievable fact text.
        records: *id029
        note: Extracting standing facts from recorded conversation reduces its representation even if
          source text remains.
      - scope: Observation consolidation and revision
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id030
          - memory.md#mem-rte-observation-consolidation
          - memory.md#mem-obj-observation-text
          note: Fact and observation content is combined into reduced observation prose.
        - value: evolve
          basis: wired
          records: *id030
          note: Prepared updates replace existing observation text and retrieval representations.
        records: *id030
        note: Combining existing claims and revising existing observations are distinct supported transformations.
      - scope: Standing-page full regeneration and delta editing
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id031
          - memory.md#mem-rte-page-maintenance
          - epistemic.md#epi-rte-page-refresh
          note: Refresh builds a standing representation over scoped retained facts/observations.
        - value: evolve
          basis: wired
          records: *id031
          note: Full replacement or localized edits revise the standing page.
        records: *id031
        note: Combining source material and revising a durable baseline is established; novel claims are
          not established by the word synthesis.
      - scope: Raw-memory correction and archive-based withdrawal
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id032
          - memory.md#mem-rte-memory-curation
          - memory.md#mem-obj-curation-archive
          note: Explicit content edits replace a live raw fact and rebuild its representations.
        - value: invalidate
          basis: wired
          records: *id032
          note: Archive movement withdraws live reliance while preserving restoration state and reason.
        records: *id032
        note: The archived history distinguishes invalidation from permanent deletion.
      - scope: Optional semantic dedup verdict handling and semantic novelty of generated claims
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-observation-consolidation
        - epistemic.md#epi-rte-page-refresh
        note: Dedup is located but not fully traced; prompts and route names alone do not establish a
          dedup transformation or a claim absent from inputs. The accepted semantic-relation uncertainty
          prevents a positive synthesize classification.
      - scope: Remaining curation, decay/promotion and alternative-store mechanisms
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-filesystem-mirror
        - memory.md#mem-rte-page-evaluation
        - runtime.md#rt-rte-claude-hooks
        - runtime.md#rt-rte-retain-work
        - memory.md#mem-rte-memory-curation
        note: Additional shipped integrations, imports, attachments, embedded callers and alternate-store
          consumption remain incompletely inspected in the accepted records; complete system enumeration
          is prevented. No bounded absence record establishes absence of decay, promote or other operations.
      records:
      - runtime.md#rt-rte-claude-hooks
      - runtime.md#rt-rte-retain-work
      - memory.md#mem-obj-fact-text
      - memory.md#mem-rte-observation-consolidation
      - memory.md#mem-obj-observation-text
      - memory.md#mem-rte-page-maintenance
      - epistemic.md#epi-rte-page-refresh
      - memory.md#mem-rte-memory-curation
      - memory.md#mem-obj-curation-archive
      - memory.md#mem-rte-filesystem-mirror
      - memory.md#mem-rte-page-evaluation
      note: Consolidate, evolve and archive-preserving invalidate have implemented witnesses. Reindexing
        alone adds no curation value. Prompted synthesis/dedup and uninspected branches are not upgraded
        to implemented semantic transformations.
    read_back_direction:
      assessment: partial
      units:
      - scope: Caller/model-requested recall, page search and explicit page-ID reads
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id033
          - memory.md#mem-rte-recall-selection
          - memory.md#mem-rte-page-delivery
          - runtime.md#rt-rte-reflect-request
          note: A consumer asks for retained material through query or explicit IDs and receives selected
            content.
        records: *id033
        note: Fulfilling the requested retrieval is pull, not a second push merely because code serializes
          its result.
      - scope: Claude Code per-prompt context injection
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id034
          - runtime.md#rt-rte-claude-hooks
          - runtime.md#rt-bap-hook-context
          note: Hook code automatically selects/formats memories and emits additionalContext on UserPromptSubmit.
        records: *id034
        note: The host event triggers the hook; the answering consumer has not requested particular retained
          items.
      - scope: Active directives and automatic maintenance inputs
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id035
          - memory.md#mem-rte-directive-admission
          - memory.md#mem-bap-directive-prompt
          - memory.md#mem-rte-page-maintenance
          - memory.md#mem-obj-refresh-specification
          note: Code supplies selected stored directives, maintenance baseline/query and grounding to
            their later consumers.
        records: *id035
        note: An upstream reflect request or configured trigger does not make implicit direction/baseline
          loading a requested content return.
      - scope: CLI server-to-disk snapshot synchronization
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id036
          - memory.md#mem-rte-filesystem-mirror
          note: Configured synchronization requests a knowledge snapshot and materializes it locally.
        records: *id036
        note: This classifies snapshot acquisition/delivery, not an invented later agent file-read route.
      - scope: Mirror later agent reading, report consumer details and additional shipped read-back
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-filesystem-mirror
        - memory.md#mem-rte-page-evaluation
        - runtime.md#rt-rte-claude-hooks
        note: Additional shipped integrations, imports, attachments, embedded callers and alternate-store
          consumption remain incompletely inspected in the accepted records; complete system enumeration
          is prevented. Mirroring capability and documented dashboards do not establish wired model consumption.
      records:
      - memory.md#mem-rte-recall-selection
      - memory.md#mem-rte-page-delivery
      - runtime.md#rt-rte-reflect-request
      - runtime.md#rt-rte-claude-hooks
      - runtime.md#rt-bap-hook-context
      - memory.md#mem-rte-directive-admission
      - memory.md#mem-bap-directive-prompt
      - memory.md#mem-rte-page-maintenance
      - memory.md#mem-obj-refresh-specification
      - memory.md#mem-rte-filesystem-mirror
      - memory.md#mem-rte-page-evaluation
      note: Both requested retrieval and independent automatic supply exist. Request, selection and delivery
        steps are distinguished within chains. Current-request synthesis history is not counted as a separate
        accumulated-memory read-back route.
    read_back_signal:
      assessment: partial
      units:
      - scope: Prompt-triggered hook selection of fact/observation context
        assessment: partial
        findings:
        - value: inferred-embedding
          basis: wired
          records: &id037
          - runtime.md#rt-rte-claude-hooks
          - memory.md#mem-rte-recall-selection
          - memory.md#mem-obj-fact-embedding
          - memory.md#mem-cmp-cross-encoder
          note: The inspected numerical retrieval representation supplies semantic relevance for automatic
            context selection.
        - value: inferred-judgment
          basis: wired
          records: *id037
          note: Configured cross-encoder query/candidate scoring can influence the ranking from which
            hook context is selected.
        records: *id037
        note: Trigger is UserPromptSubmit; selector input is prompt/context-derived query plus bank/filter
          settings; selected parts are retained fact/observation text. Complete retrieval arms and configured
          ranking mode are unresolved.
      - scope: Directive loading during reflect
        assessment: partial
        findings:
        - value: coarse
          basis: wired
          records: &id038
          - memory.md#mem-rte-directive-admission
          - memory.md#mem-bap-directive-prompt
          - runtime.md#rt-rte-reflect-request
          note: Active/scoped availability selects the directive set for automatic prompt delivery.
        records: *id038
        note: Trigger is a reflect invocation; active availability and optional all-active loading select
          directive prose. Exact tag-selector implementation is not recorded sufficiently to classify
          targeted identity matching here.
      - scope: Automatic page maintenance baseline and grounding supply
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id039
          - memory.md#mem-rte-page-maintenance
          - memory.md#mem-obj-refresh-specification
          - memory.md#mem-obj-refresh-response
          note: The maintenance target identity selects the retained page baseline for its update consumer.
        records: *id039
        note: A scheduled/explicit refresh selects its retained page baseline by model identity and uses
          stored source IDs to detect retracted grounding; supplied parts are baseline, query and maintenance
          evidence.
      - scope: Other hook retrieval arms, tag targeting and additional push routes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-recall-selection
        - memory.md#mem-rte-directive-admission
        - runtime.md#rt-rte-claude-hooks
        note: Complete selector implementations and alternative integrations are uninspected. Lexical
          selection is not inferred from an unspecified retrieval arm; identifier on a requested page
          alone is not a push witness.
      records:
      - runtime.md#rt-rte-claude-hooks
      - memory.md#mem-rte-recall-selection
      - memory.md#mem-obj-fact-embedding
      - memory.md#mem-cmp-cross-encoder
      - memory.md#mem-rte-directive-admission
      - memory.md#mem-bap-directive-prompt
      - runtime.md#rt-rte-reflect-request
      - memory.md#mem-rte-page-maintenance
      - memory.md#mem-obj-refresh-specification
      - memory.md#mem-obj-refresh-response
      note: Signals describe automatic supply operations only. Query/ID selectors on explicitly requested
        pull results are not added as push signals. Known pull paths cannot make unresolved push alternatives
        inapplicable.
    trace_learning:
      assessment: partial
      units:
      - scope: Claude Code transcript retention into facts and optional derived observations/pages, then
          later host context
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id040
          - runtime.md#rt-rte-claude-hooks
          - runtime.md#rt-rte-retain-work
          - memory.md#mem-obj-fact-text
          - runtime.md#rt-bap-hook-context
          note: Automatic trace-fed writes produce retained facts and derivatives available to subsequent
            model context.
        records: *id040
        note: The durable behavior-shaping artifact is extracted memory, not merely a raw log. Delivery
          is wired; actual host reliance and improvement remain unobserved.
      - scope: Generic retention/refresh inputs and other integrations, imports and attachment routes
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-retain-work
        - memory.md#mem-rte-page-maintenance
        - memory.md#mem-obj-document-text
        note: Generic inputs can mix static documents and activity records. Complete origin, automatic
          admission and later-consumer chains are not established for every included route.
      records:
      - runtime.md#rt-rte-claude-hooks
      - runtime.md#rt-rte-retain-work
      - memory.md#mem-obj-fact-text
      - runtime.md#rt-bap-hook-context
      - memory.md#mem-rte-page-maintenance
      - memory.md#mem-obj-document-text
      note: A concrete qualifying trace-fed write supports yes without proving improved capacity or parameter
        training. No bounded absence record warrants local or system-wide no; unresolved routes remain
        included.
    trace_source:
      assessment: partial
      units:
      - scope: Conversational source of the qualifying Claude Code trace-fed write
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id041
          - runtime.md#rt-rte-claude-hooks
          - runtime.md#rt-rte-retain-work
          note: Selected user/assistant turns from recorded work sessions feed fact extraction.
        records: *id041
        note: Classification follows original conversational content rather than hook event scheduling.
      - scope: Optional tool-call material in the same qualifying hook write
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id042
          - runtime.md#rt-rte-claude-hooks
          note: Recorded tool-call material can be included by the retention selector and consumed by
            extraction.
        records: *id042
        note: This is a configurable content branch, not a claim that every retention includes tools or
          execution outcomes.
      - scope: Other original inputs to generic retention and derived page-update routes
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-retain-work
        - memory.md#mem-rte-page-maintenance
        - memory.md#mem-obj-document-text
        note: Other integrations and mixed inputs remain unresolved. Stop/UserPromptSubmit scheduling
          is not itself an event-stream input to extraction; no trajectory learning source is established
          merely by a multi-step workflow.
      records:
      - runtime.md#rt-rte-claude-hooks
      - runtime.md#rt-rte-retain-work
      - memory.md#mem-rte-page-maintenance
      - memory.md#mem-obj-document-text
      note: Session logs and optional tool traces classify the concrete qualifying route. Other qualifying
        routes and mixed origins are not completely assessed, so trace_source is partial rather than inapplicable
        or complete.
---

# Hindsight memory profile

## Comparison rationale

Every positive finding is source-wired, not an observed run or demonstrated benefit. The ten axes remain partial because accepted records retain additional shipped paths and opaque alternatives. No known database, caller or consumer resolves another route's missing facts. Unknown units are not negative findings.

### Parts, derivations and authority

Default SQL content and vector access structures coexist with unresolved configured stores. Dense embeddings receive parametric form without being classified as trained weights. Facts, observations and page prose are distinct from their access IDs, edit addresses and audit state. A readable snippet does not classify an opaque attachment or store payload. See [MEM-OBJ-fact-embedding](memory.md#mem-obj-fact-embedding), [MEM-OBJ-page-embedding](memory.md#mem-obj-page-embedding) and [MEM-OBJ-document-text](memory.md#mem-obj-document-text).

Authored page creation does not mean human admission. The caller may be software, while later model/code refresh admission is automatic. Source-conditioned transformations support compiled lineage without establishing new claims, faithful semantic preservation or truth. Consolidation and revision are supported; the semantic uncertainty prevents inferring synthesize from a route's name. Optional semantic-dedup handling remains incompletely inspected. See [MEM-RTE-page-maintenance](memory.md#mem-rte-page-maintenance), [MEM-RTE-observation-consolidation](memory.md#mem-rte-observation-consolidation) and [EPI-RTE-page-refresh](epistemic.md#epi-rte-page-refresh).

Learning authority belongs to retained experience/evidence at durable-artifact update consumers. Knowledge belongs to selected prose at the later answering consumer. Directive instruction is not semantic enforcement; the prompt's rejection wording is not a witnessed response checker. In contrast, retained source/target identities can supply fixed-rule validation and veto criteria. Bank overrides and refresh windows route operations without establishing improved capacity. See [MEM-BAP-reflect-content](memory.md#mem-bap-reflect-content), [MEM-BAP-directive-prompt](memory.md#mem-bap-directive-prompt), [MEM-OBJ-refresh-response](memory.md#mem-obj-refresh-response) and [RT-BAP-config-consumer](runtime.md#rt-bap-config-consumer).

### Chains and coverage

The hook requests recall upstream and independently pushes selected context downstream. Requested recall/page results are pull, not duplicate pushes. Automatic directive loading and maintenance baseline supply are separate operations. Push signals retain their local selector limits: an embedding/reranker witness does not classify every retrieval arm, and a requested ID alone does not establish identifier push. Mirror synchronization is inspected server-to-disk delivery; later agent reading is unresolved. See [RT-RTE-claude-hooks](runtime.md#rt-rte-claude-hooks), [MEM-RTE-recall-selection](memory.md#mem-rte-recall-selection), [MEM-RTE-page-delivery](memory.md#mem-rte-page-delivery) and [MEM-RTE-filesystem-mirror](memory.md#mem-rte-filesystem-mirror).

Transcript-to-fact-to-later-context wiring qualifies as trace learning under this profile's write-route definition. It does not require a measured benefit, learned weights or epistemic acceptance. Conversation and optional tool-call content establish distinct source findings. Hook scheduling does not add event-stream content. Current-request map/reduce history is excluded because the accepted account establishes no durable reload chain for it. See [RT-RTE-claude-hooks](runtime.md#rt-rte-claude-hooks) and [RT-RTE-context-synthesis](runtime.md#rt-rte-context-synthesis).

### Reconciliation and source-read log

Reconciliation supersedes the duplicate epistemic observation-batch and page-evaluation routes with [MEM-RTE-observation-consolidation](memory.md#mem-rte-observation-consolidation) and [MEM-RTE-page-evaluation](memory.md#mem-rte-page-evaluation). Those canonical destinations are used here; supersession does not upgrade their evidence or remove the semantic and evaluator-feedback limits. Valid containers and narrower disposition/withdrawal routes remain distinct, not silently replaced. The conditional refresh/reflection model alias does not prove identical weights or accumulated parameter learning.

No target source files were read for this classification. All warrants come from the supplied accepted records and their annotations, resolved through the supplied reconciliation. Missing alternative-store, initialization, integration-consumer and semantic-transformation facts prevent stronger assessments; they are not reopened report-verification findings.
