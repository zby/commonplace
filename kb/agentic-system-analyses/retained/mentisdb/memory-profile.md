---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'MentisDB memory comparison: retained thoughts, uploaded instruction versions, derived retrieval state and unresolved maintenance/diagnostic consumers.'
run-id: AAS-2026-10-14-mentisdb-a8b5903ae3e2-01
source-identity: https://github.com/cloudllm-ai/mentisdb
reviewed-boundary: 4c9b95041da68c5a26dece9f8776ff54b05b910c
memory-comparison:
  version: 2
  scope: Retained thought content/envelopes (including Python and evaluator conversation writes), uploaded skill bodies/version/lifecycle state, managed embedding vectors and symbolic retrieval access structures, caller-retained Markdown views and evaluator/interaction diagnostics, with their admission, curation and later-consumer routes. Includes unresolved custom adapters, backend detail, caller-controlled semantic updates and diagnostic/log consumers. Excludes static compiled core/project instructions, product binaries, inference-provider weights, transient extraction/source-window/bundle responses as retained objects, and current append-event delivery as historical read-back. External host/provider internals remain outside the frozen boundary; unknown callback retention is retained as a limitation, not attributed to MentisDB.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Canonical thought content and symbolic envelope; built-in binary and JSONL chain persistence
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-thought-content
          - runtime.md#rt-obj-thought
          - runtime.md#rt-rte-memory-roundtrip
          note: Built-in adapters retain chain records in backing files.
        - value: in-memory
          basis: wired
          records: *id001
          note: Opening loads retained records into the thought collection for later selection.
        records: *id001
        note: Built-in persisted and loaded parts are identified; custom adapters are assessed separately.
      - scope: Uploaded skill bodies, version patches and lifecycle registry
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id002
          - memory.md#mem-obj-skill-body
          - runtime.md#rt-obj-skill-registry
          - runtime.md#rt-rte-skill-admission
          note: Bincode registry persists full bodies and patches through temporary-file write and rename.
        records: *id002
        note: This is accumulated uploaded state, not the compiled core skill.
      - scope: Managed vectors, retrieval indexes and semantic-neighbor overlay
        assessment: partial
        findings:
        - value: vector
          basis: wired
          records:
          - memory.md#mem-obj-embedding-vector
          - memory.md#mem-rte-derived-update
          note: Dense retained embeddings are operative vector retrieval state.
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-embedding-vector
          - memory.md#mem-obj-retrieval-state
          - memory.md#mem-rte-derived-update
          note: Managed sidecars/WAL and persisted implicit-edge/registry metadata supply file-backed derived state.
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-state
          - memory.md#mem-rte-derived-update
          note: Lookup, lexical and graph indexes are rebuilt in memory from retained records.
        - value: graph
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-state
          - memory.md#mem-rte-derived-update
          note: Explicit adjacency and implicit-neighbor overlays are operative graph access structures.
        records:
        - memory.md#mem-obj-embedding-vector
        - memory.md#mem-obj-retrieval-state
        - memory.md#mem-rte-derived-update
        note: Full HNSW/WAL persistence and metadata freshness are incompletely inspected; file and vector witnesses do not resolve every backend.
      - scope: Caller-saved MEMORY Markdown view
        assessment: known
        findings:
        - value: files
          basis: afforded
          records: &id003
          - memory.md#mem-rte-markdown-exchange
          note: A caller can save the exported view as a file; no saved instance was supplied.
        records: *id003
        note: Export itself is transient; file retention is only afforded.
      - scope: Evaluator diagnostic outputs
        assessment: partial
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-rte-retrieval-evaluation
          note: Drivers can persist optional JSON/JSONL diagnostic outputs.
        records:
        - memory.md#mem-rte-retrieval-evaluation
        note: Complete output lifecycle and subsequent readers are not established.
      - scope: Custom canonical storage adapters and optional service interaction-log persistence
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-memory-roundtrip
        - memory.md#mem-obj-retrieval-state
        note: Custom storage semantics and complete log rotation/reload consumers are not inspected; substrate coverage cannot be closed.
      records:
      - memory.md#mem-obj-thought-content
      - runtime.md#rt-obj-thought
      - runtime.md#rt-rte-memory-roundtrip
      - memory.md#mem-obj-skill-body
      - runtime.md#rt-obj-skill-registry
      - runtime.md#rt-rte-skill-admission
      - memory.md#mem-obj-embedding-vector
      - memory.md#mem-obj-retrieval-state
      - memory.md#mem-rte-derived-update
      - memory.md#mem-rte-markdown-exchange
      - memory.md#mem-rte-retrieval-evaluation
      note: Thoughts, uploaded skills and derived access state have positive substrate witnesses. Custom storage, backend detail and diagnostic/log lifecycle keep the included inventory partial. External model weights are inference dependencies, not memory accumulated by these routes.
    representational_form:
      assessment: partial
      units:
      - scope: Thought prose at human/model context consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id004
          - memory.md#mem-obj-thought-content
          - runtime.md#rt-bap-retained-context
          note: Statements and raw messages supply interpreted content at later context consumers.
        records: *id004
        note: Arbitrary caller text is split from its fixed-rule envelope; actual live content was not supplied.
      - scope: Thought envelope, skill version/lifecycle metadata and retrieval lookup/graph structures at code consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id005
          - runtime.md#rt-obj-thought
          - runtime.md#rt-obj-skill-registry
          - memory.md#mem-obj-retrieval-state
          note: Localized identifiers, relations, hashes, patches and indexes have fixed-rule consumers.
        records: *id005
        note: Symbolic machinery is not a factual interpretation of the prose.
      - scope: Uploaded skill instruction body at interpreting reader
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id006
          - memory.md#mem-obj-skill-body
          - runtime.md#rt-rte-skill-admission
          note: Reconstructed instruction sections are interpreted by the downstream reader.
        records: *id006
        note: Document metadata remains in the separate symbolic registry unit.
      - scope: Dense embedding outputs at vector ranking and neighbor derivation
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: &id007
          - memory.md#mem-obj-embedding-vector
          - memory.md#mem-rte-derived-update
          note: Dense numerical representations distribute information across vector coordinates.
        records: *id007
        note: Parametric here denotes embedding outputs, not a claim that retained memory changes model weights.
      - scope: 'Saved Markdown view: prose and parser-facing section/metadata format'
        assessment: known
        findings:
        - value: natural-language
          basis: afforded
          records: &id008
          - memory.md#mem-rte-markdown-exchange
          note: Exported thought prose is interpreted by readers.
        - value: symbolic
          basis: afforded
          records: *id008
          note: Section and bullet metadata has a fixed import parser.
        records: *id008
        note: The saved-view route is afforded; generated response and import machinery are wired.
      - scope: Retained evaluator diagnostics
        assessment: partial
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-rte-retrieval-evaluation
          note: Optional outputs retain scores, categories and miss/return diagnostics under a structured format.
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-rte-retrieval-evaluation
          note: Miss and returned-text diagnostics can retain conversation text.
        records:
        - memory.md#mem-rte-retrieval-evaluation
        note: No complete output inventory or later consumer was supplied.
      - scope: Arbitrary caller payload alternatives, custom storage contents and complete interaction-log consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-thought-content
        - runtime.md#rt-rte-memory-roundtrip
        - memory.md#mem-obj-retrieval-state
        note: Accepted records permit arbitrary text and leave custom/log consumption uninspected; they cannot classify every operative payload.
      records:
      - memory.md#mem-obj-thought-content
      - runtime.md#rt-bap-retained-context
      - runtime.md#rt-obj-thought
      - runtime.md#rt-obj-skill-registry
      - memory.md#mem-obj-retrieval-state
      - memory.md#mem-obj-skill-body
      - runtime.md#rt-rte-skill-admission
      - memory.md#mem-obj-embedding-vector
      - memory.md#mem-rte-derived-update
      - memory.md#mem-rte-markdown-exchange
      - memory.md#mem-rte-retrieval-evaluation
      - runtime.md#rt-rte-memory-roundtrip
      note: The inspected prose, symbolic control and dense numerical parts are separated. Unknown payload and diagnostic/log consumption prevents a complete form inventory; opaque provider weights do not replace these parts.
    lineage:
      assessment: partial
      units:
      - scope: Explicitly authored thoughts, revisions and handoff/checkpoint content
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id009
          - memory.md#mem-obj-thought-content
          - memory.md#mem-rte-correction-update
          - workflow.md#wf-rte-session-continuation
          note: Callers supply statements, revisions and accepting continuation text without a required extraction step.
        records: *id009
        note: Authored does not imply human admission or established truth.
      - scope: Markdown import, copied/merged thoughts and archive restoration
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id010
          - memory.md#mem-rte-markdown-exchange
          - memory.md#mem-rte-agent-copy
          - runtime.md#rt-rte-state-maintenance
          note: External Markdown and existing source/archived state enter destination memory through explicit import/copy/restore paths.
        records: *id010
        note: Fresh IDs and omitted graph metadata can degrade imported lineage.
      - scope: Python and benchmark retained raw conversational messages
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id011
          - memory.md#mem-obj-thought-content
          - runtime.md#rt-rte-memory-roundtrip
          - memory.md#mem-rte-retrieval-evaluation
          note: Recorded conversational turns are admitted directly, not distilled merely because their type is Summary or FactLearned.
        records: *id011
        note: Raw trace retention is acquisition, not trace extraction.
      - scope: Vectors, indexes, inferred neighbors and skill patch reconstruction
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id012
          - memory.md#mem-obj-embedding-vector
          - memory.md#mem-obj-retrieval-state
          - memory.md#mem-rte-derived-update
          - memory.md#mem-obj-skill-body
          note: Code/provider derivation builds dense vectors and access structures; version patches reconstruct uploaded bodies.
        records: *id012
        note: This known derivation does not resolve original content provenance or dependency-controlled model provenance.
      - scope: Caller-produced distilled lesson or summary/checkpoint follow-on
        assessment: known
        findings:
        - value: trace-extracted
          basis: afforded
          records: &id013
          - memory.md#mem-rte-summary-selection
          note: The documented follow-on distills retained work into an authored lesson/checkpoint for later requests.
        records: *id013
        note: Only the source selector is wired; semantic distillation is afforded, not a shipped automatic summarizer.
      - scope: Initial uploaded skill provenance, separately appended extraction candidates and mixed embedding inputs
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-skill-body
        - memory.md#mem-obj-thought-content
        - memory.md#mem-obj-embedding-vector
        - runtime.md#rt-rte-memory-roundtrip
        note: No concrete uploaded version or extraction input/output was supplied; arbitrary caller content and metadata have unresolved origins. Known compilation does not settle those upstream paths.
      records:
      - memory.md#mem-obj-thought-content
      - memory.md#mem-rte-correction-update
      - workflow.md#wf-rte-session-continuation
      - memory.md#mem-rte-markdown-exchange
      - memory.md#mem-rte-agent-copy
      - runtime.md#rt-rte-state-maintenance
      - runtime.md#rt-rte-memory-roundtrip
      - memory.md#mem-rte-retrieval-evaluation
      - memory.md#mem-obj-embedding-vector
      - memory.md#mem-obj-retrieval-state
      - memory.md#mem-rte-derived-update
      - memory.md#mem-obj-skill-body
      - memory.md#mem-rte-summary-selection
      note: Retain authored, imported, compiled and afforded trace-extraction paths separately. Missing live-content and embedding-input provenance prevents a complete lineage union.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Returned thought content and handoffs at human/model context readers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id014
          - memory.md#mem-obj-thought-content
          - runtime.md#rt-bap-retained-context
          - workflow.md#wf-rte-session-continuation
          note: Returned statements, state and raw messages supply reference/context.
        - value: instruction
          basis: wired
          records: *id014
          note: Handoff next actions and retained rules can supply directions at their interpreting reader.
        records: *id014
        note: Wired delivery supports available forces at the interpreter, not observed obedience or task improvement.
      - scope: Uploaded skill bodies at downstream interpreters
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id015
          - memory.md#mem-obj-skill-body
          - runtime.md#rt-rte-skill-admission
          - runtime.md#rt-bap-retained-context
          note: Reconstructed skill bodies supply standing directions through requested skill read.
        records: *id015
        note: Returned revoked content is not itself an enforced execution prohibition.
      - scope: Thought text/metadata and numerical vectors at ranking code
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id016
          - runtime.md#rt-rte-memory-roundtrip
          - memory.md#mem-obj-thought-content
          - memory.md#mem-obj-embedding-vector
          - memory.md#mem-obj-retrieval-state
          - memory.md#mem-rte-derived-update
          - memory.md#mem-rte-bundle-read
          note: Lexical text, metadata and vector representations affect relative retrieval priority.
        records: *id016
        note: Ranking is a force of retained inputs under fixed code, not a learned policy claim.
      - scope: Retained invalidation-ID set at default retrieval predicate
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records: &id017
          - memory.md#mem-rte-correction-update
          - memory.md#mem-obj-retrieval-state
          note: Persisted invalidating relations rebuild the set that vetoes delivery of targeted records on covered default readers.
        records: *id017
        note: Audit, direct lookup and unfiltered renderers bound the veto.
      - scope: Retained thought sequence/reference identities and canonical hashes at append/open checks
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id018
          - runtime.md#rt-obj-thought
          - runtime.md#rt-rte-memory-roundtrip
          - workflow.md#wf-rte-session-continuation
          note: Existing reference range and retained canonical representation determine structural admissibility of a new ref or reopened chain.
        - value: enforcement
          basis: wired
          records: *id018
          note: Invalid refs or failed reopened integrity can block append/open on covered shared-core routes.
        records: *id018
        note: Structural force does not license content truth, authorship or crash-proof storage.
      - scope: Retained Summarizes targets at source-window selection
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id019
          - memory.md#mem-rte-summary-selection
          note: Stored coverage selects which source windows become later summarization work candidates.
        records: *id019
        note: Target membership routes proposed work; it does not evaluate summary adequacy.
      - scope: Automatically compiled embeddings from retained conversation content at the update consumer
        assessment: partial
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-obj-thought-content
          - runtime.md#rt-rte-memory-roundtrip
          - memory.md#mem-obj-embedding-vector
          - memory.md#mem-rte-derived-update
          note: Retained raw conversation is an available embedding input; automatic durable vector/neighbor derivation changes later retrieval behavior-shaping state.
        records:
        - memory.md#mem-obj-thought-content
        - runtime.md#rt-rte-memory-roundtrip
        - memory.md#mem-obj-embedding-vector
        - memory.md#mem-rte-derived-update
        note: This learning force is the numerical update path, not semantic lesson generation, parameter training or demonstrated capacity improvement. Actual inputs may instead be nontrace caller text.
      - scope: Unspecified live skill/status interpretation and later consumers of diagnostic/log files
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-skill-body
        - epistemic.md#epi-rte-skill-withdrawal
        - memory.md#mem-rte-retrieval-evaluation
        - memory.md#mem-obj-retrieval-state
        note: No complete subsequent diagnostic/log reader or live host status-handling path is established; these parts cannot acquire additional forces by inference.
      records:
      - memory.md#mem-obj-thought-content
      - runtime.md#rt-bap-retained-context
      - workflow.md#wf-rte-session-continuation
      - memory.md#mem-obj-skill-body
      - runtime.md#rt-rte-skill-admission
      - runtime.md#rt-rte-memory-roundtrip
      - memory.md#mem-obj-embedding-vector
      - memory.md#mem-obj-retrieval-state
      - memory.md#mem-rte-derived-update
      - memory.md#mem-rte-bundle-read
      - memory.md#mem-rte-correction-update
      - runtime.md#rt-obj-thought
      - memory.md#mem-rte-summary-selection
      - epistemic.md#epi-rte-skill-withdrawal
      - memory.md#mem-rte-retrieval-evaluation
      note: Knowledge/instruction delivery, ranking, routing and structural vetoes have local consumers. The trace-fed numerical update has a distinct learning consumer. Downstream compliance and unresolved diagnostics are not upgraded by those witnesses.
    write_agency:
      assessment: partial
      units:
      - scope: Python message admission and benchmark per-turn ingestion
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id020
          - runtime.md#rt-rte-memory-roundtrip
          - memory.md#mem-rte-retrieval-evaluation
          note: Software admits each nonempty message/dataset turn without a per-content human approval event.
        records: *id020
        note: Starting the driver or configuring an adapter does not make each admission manual.
      - scope: Managed vector/index/neighbor updates and optional similarity supersession
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id021
          - memory.md#mem-rte-derived-update
          - memory.md#mem-rte-correction-update
          note: Code/provider computes and admits each derivative or supersession under configuration, without approving each output with a human.
        records: *id021
        note: Configuration/maintenance initiation is distinct from per-output admission.
      - scope: CLI/service/direct caller thought, correction, checkpoint and handoff admissions
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-memory-roundtrip
        - memory.md#mem-rte-correction-update
        - memory.md#mem-rte-summary-selection
        - workflow.md#wf-rte-session-continuation
        note: Generic caller attribution does not determine whether a human supplied, approved or replaced each retained item.
      - scope: Skill upload/revision/lifecycle, Markdown import, agent-copy, merge/restore and deletion
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-skill-admission
        - epistemic.md#epi-rte-skill-withdrawal
        - memory.md#mem-rte-markdown-exchange
        - memory.md#mem-rte-agent-copy
        - runtime.md#rt-rte-state-maintenance
        - memory.md#mem-rte-chain-withdrawal
        note: Explicit request, dashboard access, signature or structural parsing is not proof of a per-content human decision. Automation versus human content approval is unresolved on these caller-controlled paths.
      records:
      - runtime.md#rt-rte-memory-roundtrip
      - memory.md#mem-rte-retrieval-evaluation
      - memory.md#mem-rte-derived-update
      - memory.md#mem-rte-correction-update
      - memory.md#mem-rte-summary-selection
      - workflow.md#wf-rte-session-continuation
      - runtime.md#rt-rte-skill-admission
      - epistemic.md#epi-rte-skill-withdrawal
      - memory.md#mem-rte-markdown-exchange
      - memory.md#mem-rte-agent-copy
      - runtime.md#rt-rte-state-maintenance
      - memory.md#mem-rte-chain-withdrawal
      note: Automatic message/derivative mechanisms are known. No manual finding is inferred from a CLI/UI or an agent ID; caller-controlled alternatives keep agency partial.
    curation_operations:
      assessment: partial
      units:
      - scope: Relation-bearing correction and configured near-duplicate supersession
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records: &id022
          - memory.md#mem-rte-correction-update
          note: Targeted old claims are excluded from current default reliance while canonical history survives.
        - value: dedup
          basis: wired
          records: *id022
          note: Configured token-set near-duplicate matching replaces default reliance on the chosen earlier entry.
        records: *id022
        note: Wired semantic-equivalence checking is not claimed; dedup force follows lexical similarity and supersession.
      - scope: Uploaded skill revision and lifecycle retirement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id023
          - runtime.md#rt-rte-skill-admission
          - memory.md#mem-obj-skill-body
          - epistemic.md#epi-rte-skill-withdrawal
          note: Uploading another instruction version revises the current entry while preserving earlier versions.
        - value: invalidate
          basis: wired
          records: *id023
          note: Deprecation/revocation retires current reliance by retained lifecycle status, conditional on the reader honoring it.
        records: *id023
        note: Skill invalidation is advisory downstream, unlike the thought retrieval veto.
      - scope: Whole-chain withdrawal and skill deletion
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id024
          - memory.md#mem-rte-chain-withdrawal
          - runtime.md#rt-rte-skill-admission
          note: Explicit deletion forgets retained source state or skill history; it is not automatic time-based downweighting.
        records: *id024
        note: Physical forgetting is wired, but complete erasure of copies/residual backends is not established.
      - scope: Caller-authored summary/checkpoint of retained sources
        assessment: known
        findings:
        - value: consolidate
          basis: afforded
          records: &id025
          - memory.md#mem-rte-summary-selection
          note: The documented caller can reduce retained work into summary/checkpoint content and append it for later consumption.
        records: *id025
        note: Afforded consolidation is separate from the wired read-only window selector.
      - scope: Semantic transformations of live corrections/skills/extraction outputs and diagnostic-driven maintenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-thought-content
        - memory.md#mem-obj-skill-body
        - memory.md#mem-rte-summary-selection
        - memory.md#mem-rte-retrieval-evaluation
        - runtime.md#rt-rte-memory-roundtrip
        note: No concrete transformation or diagnostic-to-update episode resolves additional consolidation, synthesis, promotion or other curation. Index rebuilds and packaging alone establish none of them.
      records:
      - memory.md#mem-rte-correction-update
      - runtime.md#rt-rte-skill-admission
      - memory.md#mem-obj-skill-body
      - epistemic.md#epi-rte-skill-withdrawal
      - memory.md#mem-rte-chain-withdrawal
      - memory.md#mem-rte-summary-selection
      - memory.md#mem-obj-thought-content
      - memory.md#mem-rte-retrieval-evaluation
      - runtime.md#rt-rte-memory-roundtrip
      note: Invalidate, lexical deduplication, version evolution, explicit forgetting and afforded consolidation have separate warrants. Unknown actual content changes prevent enumeration of all curation; extraction return alone is not retained curation.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested thought recent/ranked/flat/federated/addressed/history access, bundles and Markdown export
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id026
          - runtime.md#rt-rte-memory-roundtrip
          - memory.md#mem-rte-bundle-read
          - memory.md#mem-rte-markdown-exchange
          note: A host/human/library request selects retained source material for return; ancestor expansion and response formatting fulfill that request.
        records: *id026
        note: Incomplete exact/history filtering prevents a uniform visibility claim, not classification of these request-driven routes.
      - scope: Requested uploaded skill/version read and derived search-state use
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id027
          - runtime.md#rt-rte-skill-admission
          - memory.md#mem-obj-skill-body
          - memory.md#mem-rte-derived-update
          note: Explicit skill/version requests reconstruct retained bodies; query execution consumes retained vector/index state in fulfillment of search.
        records: *id027
        note: An identifier in a request is addressing, not identifier-based push.
      - scope: Later consumption of optional interaction logs, diagnostic outputs and any callback-owned historical memory
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-retrieval-state
        - memory.md#mem-rte-retrieval-evaluation
        - memory.md#mem-rte-webhook-delivery
        note: Complete later file-reading consumers and external callback retention are uninspected. The wired webhook only pushes the current append event, not selected accumulated history.
      records:
      - runtime.md#rt-rte-memory-roundtrip
      - memory.md#mem-rte-bundle-read
      - memory.md#mem-rte-markdown-exchange
      - runtime.md#rt-rte-skill-admission
      - memory.md#mem-obj-skill-body
      - memory.md#mem-rte-derived-update
      - memory.md#mem-obj-retrieval-state
      - memory.md#mem-rte-retrieval-evaluation
      - memory.md#mem-rte-webhook-delivery
      note: Established accumulated-memory return is pull. Current-event webhook dispatch is excluded as a read-back finding, but its unknown external later consumer and diagnostic/log alternatives prevent a complete pull-only inventory.
    read_back_signal:
      assessment: uninspected
      units:
      - scope: Inspected requested thought/skill returns and request-driven derived retrieval
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-memory-roundtrip
        - runtime.md#rt-rte-skill-admission
        - memory.md#mem-rte-bundle-read
        - memory.md#mem-rte-markdown-exchange
        - memory.md#mem-rte-derived-update
        note: These completely characterized direction units are pull operations; ranking/query selectors are not push signals.
      - scope: Potential later diagnostic/log or callback-owned historical-memory supply
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-retrieval-state
        - memory.md#mem-rte-retrieval-evaluation
        - memory.md#mem-rte-webhook-delivery
        note: There is no established push of accumulated memory in these records and no complete later consumer inspection. Current-event chain/type matching is not a historical read-back selector.
      records:
      - runtime.md#rt-rte-memory-roundtrip
      - runtime.md#rt-rte-skill-admission
      - memory.md#mem-rte-bundle-read
      - memory.md#mem-rte-markdown-exchange
      - memory.md#mem-rte-derived-update
      - memory.md#mem-obj-retrieval-state
      - memory.md#mem-rte-retrieval-evaluation
      - memory.md#mem-rte-webhook-delivery
      note: No controlled push-selection value is established. Unresolved later-consumer alternatives prevent system-wide inapplicability; observed current-event webhook selection cannot classify a retained historical payload.
    trace_learning:
      assessment: partial
      units:
      - scope: Managed embeddings and semantic-neighbor update from retained raw conversation, then later search
        assessment: partial
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-thought-content
          - runtime.md#rt-rte-memory-roundtrip
          - memory.md#mem-obj-embedding-vector
          - memory.md#mem-rte-derived-update
          note: Automatic compilation can consume the retained Python/evaluator conversational traces and persist numerical/symbolic retrieval state that later search uses.
        records:
        - memory.md#mem-obj-thought-content
        - runtime.md#rt-rte-memory-roundtrip
        - memory.md#mem-obj-embedding-vector
        - memory.md#mem-rte-derived-update
        note: The qualifying witness is durable behavior-shaping retrieval machinery, not raw-log storage alone. Other nontrace input text and metadata are included, and their origins are unresolved. No semantic lesson, weight update or improved task capacity is implied.
      - scope: Caller-authored lesson/summary/checkpoint and uploaded instruction revision
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-summary-selection
        - runtime.md#rt-rte-skill-admission
        - workflow.md#wf-rte-session-continuation
        note: Durable behavior-shaping content and later return are afforded/wired, but per-content human versus automatic admission and qualifying original trace inputs are unresolved.
      - scope: Diagnostic/log-driven later updates and callback consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-retrieval-evaluation
        - memory.md#mem-obj-retrieval-state
        - memory.md#mem-rte-webhook-delivery
        note: Inspected diagnostics have no traced automatic successor-policy consumer; no bounded absence record closes every included route, and complete later consumers are uninspected.
      records:
      - memory.md#mem-obj-thought-content
      - runtime.md#rt-rte-memory-roundtrip
      - memory.md#mem-obj-embedding-vector
      - memory.md#mem-rte-derived-update
      - memory.md#mem-rte-summary-selection
      - runtime.md#rt-rte-skill-admission
      - workflow.md#wf-rte-session-continuation
      - memory.md#mem-rte-retrieval-evaluation
      - memory.md#mem-obj-retrieval-state
      - memory.md#mem-rte-webhook-delivery
      note: A wired trace-fed numerical derivative witness coexists with unresolved semantic and diagnostic update routes. No local or system-wide no is asserted without bounded absence evidence.
    trace_source:
      assessment: partial
      units:
      - scope: Qualifying numerical retrieval-state derivative from recorded conversational messages
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-obj-thought-content
          - runtime.md#rt-rte-memory-roundtrip
          - memory.md#mem-rte-retrieval-evaluation
          - memory.md#mem-obj-embedding-vector
          - memory.md#mem-rte-derived-update
          note: Original recorded user/assistant conversational turns can feed automatic retained embedding/neighbor derivation for later search.
        records:
        - memory.md#mem-obj-thought-content
        - runtime.md#rt-rte-memory-roundtrip
        - memory.md#mem-rte-retrieval-evaluation
        - memory.md#mem-obj-embedding-vector
        - memory.md#mem-rte-derived-update
        note: Session origin follows message content, not Summary/FactLearned type. Generic thought text, tag/concept/agent metadata and imported text also feed this derivative; their trace origins are not resolved.
      - scope: Possible automatic summary/checkpoint, instruction revision and diagnostic/log/callback update originals
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-summary-selection
        - runtime.md#rt-rte-skill-admission
        - memory.md#mem-rte-retrieval-evaluation
        - memory.md#mem-obj-retrieval-state
        - memory.md#mem-rte-webhook-delivery
        note: No qualifying automatic semantic-update chain or complete original-input inventory resolves further source values. An append callback event alone does not establish event-stream-fed learning.
      records:
      - memory.md#mem-obj-thought-content
      - runtime.md#rt-rte-memory-roundtrip
      - memory.md#mem-rte-retrieval-evaluation
      - memory.md#mem-obj-embedding-vector
      - memory.md#mem-rte-derived-update
      - memory.md#mem-rte-summary-selection
      - runtime.md#rt-rte-skill-admission
      - memory.md#mem-obj-retrieval-state
      - memory.md#mem-rte-webhook-delivery
      note: Recorded conversational turns establish session-logs on the qualifying derivative branch. Mixed/opaque upstream inputs and unresolved alternative qualifying writes prevent a complete source inventory; tool-traces, event-streams and trajectories are not inferred from envelopes.
---

# MentisDB memory profile

## Comparison rationale

The inventory separates content from its envelope, uploaded instructions from their registry, and embedding outputs from inference weights. [MEM-OBJ-thought-content](memory.md#mem-obj-thought-content), [MEM-OBJ-skill-body](memory.md#mem-obj-skill-body), [MEM-OBJ-embedding-vector](memory.md#mem-obj-embedding-vector) and [MEM-OBJ-retrieval-state](memory.md#mem-obj-retrieval-state) carry those distinctions. The compiled core skill and provider models are not accumulated memory merely because they guide or compute a memory operation. No observed-run or causal basis is asserted.

Reconciliation supersedes the epistemic duplicate thought-content, skill-document, summary-candidate, relation-withdrawal, summary-selection, bundle-selection and recall-evaluation records with their memory declarations. This profile cites the canonical memory IDs. These supersessions preserve the original findings; they do not upgrade consumer affordance to wired summarization. The Markdown import subroute and skill-withdrawal subroute remain distinct accepted epistemic records; only the latter is needed here.

The admitted content, actual update consumer and later consumer determine authority. Retained text influences ranking even under fixed code. Default invalidation has an enforcing selector; revoked skill content remains readable, so lifecycle retirement does not enforce host nonexecution. Structural reference/hash checks concern conformance, not factual truth. [MEM-RTE-correction-update](memory.md#mem-rte-correction-update), [EPI-RTE-skill-withdrawal](epistemic.md#epi-rte-skill-withdrawal), [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip) and [WF-RTE-session-continuation](workflow.md#wf-rte-session-continuation) bound these different effects.

Raw conversation storage is not itself trace learning or consolidation. The positive trace-learning finding belongs only to the automatic numerical derivative: recorded messages can become durable vectors and neighbor state, and later search consumes that derivative. Its update-consumer learning force and downstream ranking force are separate. This classification requires neither a new proposition nor measured improvement. It does not classify the optional extraction response as retained learning, infer model training, or call a Summary-labelled raw message a summary. [MEM-OBJ-thought-content](memory.md#mem-obj-thought-content), [MEM-OBJ-embedding-vector](memory.md#mem-obj-embedding-vector), [MEM-RTE-derived-update](memory.md#mem-rte-derived-update) and [MEM-RTE-retrieval-evaluation](memory.md#mem-rte-retrieval-evaluation) establish the input/derivative/later-consumer chain and its limits.

Caller-authored semantic summaries and skill revisions remain separate alternatives. Their documented semantic consolidation is afforded; the source-window selector neither generates nor persists it. Generic caller identity does not resolve human approval versus automatic admission, so no manual agency or automatic semantic trace-learning finding follows. Initial skill provenance and mixed derivative inputs remain unresolved even where compilation is known. [MEM-RTE-summary-selection](memory.md#mem-rte-summary-selection), [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) and [MEM-OBJ-embedding-vector](memory.md#mem-obj-embedding-vector) retain those missing facts.

Deletion is explicit forgetting, not timed decay or guaranteed secure erasure. Correction keeps history while changing default reliance; skill evolution preserves earlier versions. Optional lexical supersession provides a wired near-duplicate removal from current retrieval, without checking equivalent meaning. These are distinct curation operations, not names inferred from index rebuilding. [MEM-RTE-chain-withdrawal](memory.md#mem-rte-chain-withdrawal), [MEM-RTE-correction-update](memory.md#mem-rte-correction-update) and [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) support the mappings.

Known requests are pull. Automatic ancestor traversal and Python formatting fulfill a request, rather than adding push operations. The webhook selects a new append event, not accumulated historical memory. Unknown later diagnostic/log/callback consumption prevents a complete pull-only boundary and therefore prevents an axis-wide inapplicable push signal. Missing facts stay unresolved rather than becoming bounded negatives. [RT-RTE-memory-roundtrip](runtime.md#rt-rte-memory-roundtrip), [MEM-RTE-webhook-delivery](memory.md#mem-rte-webhook-delivery), [MEM-OBJ-retrieval-state](memory.md#mem-obj-retrieval-state) and [MEM-RTE-retrieval-evaluation](memory.md#mem-rte-retrieval-evaluation) supply those limits.

Source-read log: none. Classification used only the supplied accepted members and reconciliation; no source ambiguity required an additional frozen-source read.
