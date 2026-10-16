---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: Virtual Context memory profile covering retained conversation derivatives, access state,
  archives, cards and engagement history at the frozen repository boundary.
run-id: AAS-2026-10-14-virtual-context-bbd06cc3ac95-01
source-identity: https://github.com/virtual-context/virtual-context
reviewed-boundary: 74ccc570c40bb551820fcd330c42e0dfc0588f05
memory-comparison:
  version: 2
  scope: Canonical live/imported conversation content and provenance; segment summaries/full text, facts,
    structured envelopes, tag rollups, search vectors and actor cards; fact ledgers, checkpoint/working-set
    state, curation memo, proxy archives and retained engagement history; their admitted write, maintenance
    and later-consumer routes, including unresolved provider/backend, MCP, administrative repair and evaluator
    alternatives. Excludes static shipped core instructions, unmodified model weights, current-call-only
    checks/drafts and diagnostic artifacts without a traced later memory consumer.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Canonical text/provenance, fact content/links and verdict/refusal ledgers in the inspected
          relational storage family
        assessment: known
        findings:
        - value: rdbms
          basis: wired
          records: &id001
          - memory.md#mem-obj-source-content
          - memory.md#mem-obj-source-metadata
          - memory.md#mem-obj-fact
          - memory.md#mem-obj-fact-ledgers
          note: Canonical relational rows, fact rows/links and relational decision tables retain these
            parts.
        records: *id001
        note: Relational rows and ledger tables establish this substrate locally; configured backend equivalence
          is not established.
      - scope: Stored segment views, tag rollups, structured envelopes and actor cards through the configured
          store
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-stored-segment
        - memory.md#mem-obj-tag-summary
        - epistemic.md#epi-obj-structured-summary
        - memory.md#mem-obj-actor-card
        note: Persistence is wired, but the records do not resolve a single controlled physical substrate
          for every configured store alternative.
      - scope: Retained fact, chunk and tag-summary search representations
        assessment: known
        findings:
        - value: vector
          basis: wired
          records: &id002
          - memory.md#mem-obj-search-vectors
          note: Stored dense fact/chunk/tag-summary representations are operative vector-search memory.
        records: *id002
        note: The embedding storage/search backend holds dense retrieval state; backend and stale-index
          alternatives remain unresolved.
      - scope: Proxy tool/chain rows and local media restore files in the inspected path
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records: &id003
          - memory.md#mem-obj-payload-archives
          - memory.md#mem-rte-payload-restore
          note: Tool/chain snapshots are retained through the inspected SQLite store path.
        - value: files
          basis: wired
          records: *id003
          note: Media restoration reads retained local media files.
        records: *id003
        note: The inspected SQLite archive path and local media files are classified; this does not classify
          opaque media encoding.
      - scope: In-process checkpoint state and optional Redis cache
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id004
          - runtime.md#rt-obj-engine-state
          note: Engine counters, tag entries and working-set state live in process.
        - value: kv
          basis: wired
          records: *id004
          note: Optional Redis retains the checkpoint/history cache.
        records: *id004
        note: These two named alternatives are wired; durable store/provider-owned saving is a separate
          unresolved unit.
      - scope: Durable checkpoint store, provider-owned checkpoint/curation memo and engagement history
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-engine-state
        - memory.md#mem-obj-curation-memo
        - runtime.md#rt-rte-engagement-stage
        note: Store/provider implementations and engagement history substrate are not fully classified;
          a known Redis witness cannot classify them.
      - scope: Other MCP resources, migrations/backfills, evaluator caches and dated repair replacement
          surfaces
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-mcp-tools
        - memory.md#mem-rte-evaluator-reuse
        - runtime.md#rt-rte-record-edits
        note: Included alternatives remain incompletely inspected in the accepted accounts; their retained-object
          substrates cannot be enumerated.
      records:
      - memory.md#mem-obj-source-content
      - memory.md#mem-obj-source-metadata
      - memory.md#mem-obj-fact
      - memory.md#mem-obj-fact-ledgers
      - memory.md#mem-obj-stored-segment
      - memory.md#mem-obj-tag-summary
      - epistemic.md#epi-obj-structured-summary
      - memory.md#mem-obj-actor-card
      - memory.md#mem-obj-search-vectors
      - memory.md#mem-obj-payload-archives
      - memory.md#mem-rte-payload-restore
      - runtime.md#rt-obj-engine-state
      - memory.md#mem-obj-curation-memo
      - runtime.md#rt-rte-engagement-stage
      - runtime.md#rt-rte-mcp-tools
      - memory.md#mem-rte-evaluator-reuse
      - runtime.md#rt-rte-record-edits
      note: Inventory covers canonical and derived content, access representations, archives, checkpoints,
        memo and engagement state. Configured store/provider alternatives and other maintenance/evaluator
        surfaces prevent complete storage coverage. Static core files, model service weights and diagnostic-only
        artifacts are excluded from accumulated memory.
    representational_form:
      assessment: partial
      units:
      - scope: Canonical conversation text, segment synopsis/full text, tag summary/description, fact
          statement/why and card body
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id005
          - memory.md#mem-obj-source-content
          - memory.md#mem-obj-stored-segment
          - memory.md#mem-obj-tag-summary
          - memory.md#mem-obj-fact
          - memory.md#mem-obj-actor-card
          note: Source and derived prose provide model/human-readable conversation evidence and preferences.
        records: *id005
        note: These operative text parts are consumed through natural-language interpretation, separately
          from their fixed-rule fields.
      - scope: Structured exact-copy claim text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id006
          - epistemic.md#epi-obj-structured-summary
          - epistemic.md#epi-rte-structured-materialization
          note: Deterministic copying preserves a natural-language utterance rather than changing its
            form.
        records: *id006
        note: Exact claim text is distinct from inferred status/modality and source-digest metadata.
      - scope: Source provenance, fact lifecycle, card entry/source fields, structured envelope metadata,
          ledger keys, checkpoint and curation indices
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id007
          - memory.md#mem-obj-source-metadata
          - memory.md#mem-obj-fact
          - memory.md#mem-obj-actor-card
          - epistemic.md#epi-obj-structured-summary
          - memory.md#mem-obj-fact-ledgers
          - runtime.md#rt-obj-engine-state
          - memory.md#mem-obj-curation-memo
          note: Identity, lifecycle, version, watermark, depth and kept-index fields control software
            selection/admission.
        records: *id007
        note: Localized fields have fixed consumer rules; mixed prose and dense vectors have separate
          units.
      - scope: Retained fact/chunk/tag-summary dense vectors
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: &id008
          - memory.md#mem-obj-search-vectors
          note: Dense search representations distribute numerical retrieval information across vector
            coordinates.
        records: *id008
        note: The numerical outputs are distinct from encoder weights and from readable source statements.
      - scope: Tool/chain archive text and envelope/reference fields
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id009
          - memory.md#mem-obj-payload-archives
          - memory.md#mem-rte-payload-restore
          note: Archived tool and assistant text is interpreted when restored.
        - value: symbolic
          basis: wired
          records: *id009
          note: Chain JSON structure and archive references are read by restoration code.
        records: *id009
        note: Inspected text/envelope paths are classified; opaque media is not inferred from a stub or
          metadata.
      - scope: Archived media payload encoding
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-payload-archives
        note: The record explicitly distinguishes opaque image content from its readable metadata; no
          controlled form is established.
      - scope: Retained engagement question text and day/repetition ledger fields
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id010
          - runtime.md#rt-rte-engagement-stage
          - workflow.md#wf-rte-draft-selection
          note: Previously staged question text informs later question-similarity decisions.
        - value: symbolic
          basis: wired
          records: *id010
          note: Day claims and repetition fields have code-governed eligibility effects.
        records: *id010
        note: The question and fingerprint/claim roles are supported; arbitrary supplied history internals
          are not classified here.
      - scope: Additional resource, repair, backfill and evaluator retained parts
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-mcp-tools
        - runtime.md#rt-rte-record-edits
        - memory.md#mem-rte-evaluator-reuse
        note: Uninspected alternative bodies prevent a complete form inventory.
      records:
      - memory.md#mem-obj-source-content
      - memory.md#mem-obj-stored-segment
      - memory.md#mem-obj-tag-summary
      - memory.md#mem-obj-fact
      - memory.md#mem-obj-actor-card
      - epistemic.md#epi-obj-structured-summary
      - epistemic.md#epi-rte-structured-materialization
      - memory.md#mem-obj-source-metadata
      - memory.md#mem-obj-fact-ledgers
      - runtime.md#rt-obj-engine-state
      - memory.md#mem-obj-curation-memo
      - memory.md#mem-obj-search-vectors
      - memory.md#mem-obj-payload-archives
      - memory.md#mem-rte-payload-restore
      - runtime.md#rt-rte-engagement-stage
      - workflow.md#wf-rte-draft-selection
      - runtime.md#rt-rte-mcp-tools
      - runtime.md#rt-rte-record-edits
      - memory.md#mem-rte-evaluator-reuse
      note: Text, fixed-rule fields and dense retrieval representations coexist. Opaque media and additional
        retained parts prevent complete coverage; display summaries do not classify the opaque consumed
        payload.
    lineage:
      assessment: partial
      units:
      - scope: Canonical conversational content acquisition paths
        assessment: partial
        findings:
        - value: authored
          basis: wired
          records: &id011
          - memory.md#mem-obj-source-content
          - runtime.md#rt-rte-headless-chat
          - runtime.md#rt-rte-import-history
          note: Human messages and foreground assistant output supply directly authored canonical text.
        - value: imported
          basis: wired
          records: *id011
          note: Adapters normalize selected exported histories into canonical content.
        records: *id011
        note: Positive authorship/import routes are established; original transport, import byte fidelity
          and provenance authenticity remain unresolved.
      - scope: Segment synopsis, extracted facts, tag rollups and actor-card bodies derived from conversation
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id012
          - runtime.md#rt-rte-memory-maintenance
          - memory.md#mem-obj-stored-segment
          - memory.md#mem-obj-fact
          - memory.md#mem-obj-tag-summary
          - memory.md#mem-rte-card-refresh
          note: Recorded conversations feed summarization, fact extraction, rollup and actor-evidence
            card derivation.
        records: *id012
        note: Recorded source-to-derivative routes establish lineage, not semantic fidelity; prior rollups
          can survive recovery without regeneration.
      - scope: Exact-copy structured claim envelope and numerical search outputs
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records: &id013
          - epistemic.md#epi-rte-structured-materialization
          - memory.md#mem-obj-search-vectors
          note: Code materializes digest-bound claims/metadata and an encoder computes retained vectors
            from facts or summary text.
        records: *id013
        note: Exact-copy envelope construction and embedding computation are distinct from model prose
          generation; encoder version/provenance is unresolved.
      - scope: Code-derived source mappings, checkpoints and curation memo
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records: &id014
          - memory.md#mem-obj-source-metadata
          - runtime.md#rt-obj-engine-state
          - memory.md#mem-obj-curation-memo
          note: Code builds physical mappings, state snapshots and question/candidate-hash selection memos.
        records: *id014
        note: Software derivation is known; initial host provenance and opaque provider initialization
          are not resolved.
      - scope: Retained fact decision/verdict ledgers
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id015
          - memory.md#mem-obj-fact-ledgers
          - memory.md#mem-rte-fact-admission
          note: Policy comparison/refusal and version keys compile admission outcomes.
        - value: authored
          basis: wired
          records: *id015
          note: Explicit caller verdict/reason supplies review content retained in the ledger.
        records: *id015
        note: Software decisions and explicit caller verdicts have distinct origins; caller authentication/control
          remains unresolved.
      - scope: Proxy tool/chain capture
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id016
          - memory.md#mem-obj-payload-archives
          - memory.md#mem-rte-payload-restore
          note: Proxy captures tool output and message-chain snapshots from request activity.
        records: *id016
        note: Raw request traces are archived rather than rewritten as learned policy; media conversion
          remains separate.
      - scope: Media conversion and engagement/evaluator/repair initial content origins
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-payload-archives
        - runtime.md#rt-rte-engagement-stage
        - memory.md#mem-rte-evaluator-reuse
        - runtime.md#rt-rte-record-edits
        note: Original media encoding, arbitrary engagement inputs, dataset origins and unavailable repair
          inputs prevent complete lineage classification.
      records:
      - memory.md#mem-obj-source-content
      - runtime.md#rt-rte-headless-chat
      - runtime.md#rt-rte-import-history
      - runtime.md#rt-rte-memory-maintenance
      - memory.md#mem-obj-stored-segment
      - memory.md#mem-obj-fact
      - memory.md#mem-obj-tag-summary
      - memory.md#mem-rte-card-refresh
      - epistemic.md#epi-rte-structured-materialization
      - memory.md#mem-obj-search-vectors
      - memory.md#mem-obj-source-metadata
      - runtime.md#rt-obj-engine-state
      - memory.md#mem-obj-curation-memo
      - memory.md#mem-obj-fact-ledgers
      - memory.md#mem-rte-fact-admission
      - memory.md#mem-obj-payload-archives
      - memory.md#mem-rte-payload-restore
      - runtime.md#rt-rte-engagement-stage
      - memory.md#mem-rte-evaluator-reuse
      - runtime.md#rt-rte-record-edits
      note: Known acquisition and derivation paths do not resolve original authenticity, encoder provenance
        or every retained alternative. Imported static core instructions are excluded unless a use-fed
        retained update is established.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Canonical transcripts, summary/full text and facts at answer-model consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id017
          - memory.md#mem-obj-source-content
          - memory.md#mem-obj-stored-segment
          - memory.md#mem-obj-fact
          - runtime.md#rt-bap-assembled-context
          - epistemic.md#epi-rte-summary-rendering
          note: Later answer invocations interpret delivered canonical/source and derived content as context/evidence.
        records: *id017
        note: Selected content supplies evidence/context, not a truth certificate or guaranteed model
          compliance.
      - scope: Retained conversation experience at summary/fact/card update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id018
          - runtime.md#rt-rte-memory-maintenance
          - memory.md#mem-rte-card-refresh
          note: Compactor/extractor/card refresh consumes retained experience to produce durable behavior-shaping
            memory.
        records: *id018
        note: The update path differs from downstream evidence and instructions; wired learning authority
          establishes neither weight training nor measured improvement.
      - scope: Actor-card communication preferences and person context at optional answer consumer
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id019
          - epistemic.md#epi-rte-card-integration
          - epistemic.md#epi-bap-card-influence
          note: Retained communication preferences are presented as response directions.
        - value: knowledge
          basis: wired
          records: *id019
          note: Retained person-context bodies supply background for relevance and tone.
        records: *id019
        note: The wrapper requests following response preferences and supplies relevance context; ships
          disabled and compliance is unobserved.
      - scope: Source IDs/epochs, lifecycle state and refusal/verdict ledger fields at admission/disclosure
          consumers
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id020
          - memory.md#mem-obj-source-metadata
          - memory.md#mem-rte-fact-admission
          - memory.md#mem-bap-fact-refusals
          - epistemic.md#epi-rte-fact-proof
          - epistemic.md#epi-rte-fact-withholding
          - memory.md#mem-rte-card-refresh
          note: Source versions, identity/scope and rejected-statement keys test candidate admissibility.
        - value: enforcement
          basis: wired
          records: *id020
          note: Retained verdict/trust/refusal state blocks extraction, comparison or delivery when checks
            fail.
        records: *id020
        note: Criterion and veto are separate effects; structural proof does not entail statement truth.
      - scope: Checkpoint watermarks, tag/working-set state and matching curation memo at later selectors
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id021
          - runtime.md#rt-bap-engine-watermarks
          - runtime.md#rt-obj-engine-state
          - memory.md#mem-obj-curation-memo
          note: Watermarks/depth/tag fields and kept indices select later input windows, operations and
            retained subsets.
        records: *id021
        note: Retained control fields select windows, eligible inputs and fact subsets rather than directing
          a model in prose.
      - scope: Stored dense vectors at fact ranker and tag-summary text at embedding/scoring
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id022
          - memory.md#mem-obj-search-vectors
          - memory.md#mem-obj-tag-summary
          note: Fact vectors influence top-N retrieval; retained tag-summary text supplies embedding/scoring
            input.
        records: *id022
        note: Ranking is a software selection effect, not a semantic warrant; not all retriever strategies
          are inspected.
      - scope: Engagement day claims and prior-question history at repetition/posting admission
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id023
          - runtime.md#rt-rte-engagement-stage
          - workflow.md#wf-rte-draft-selection
          note: Day/repetition history supplies eligibility criteria for candidate/draft/send admission.
        - value: enforcement
          basis: wired
          records: *id023
          note: Existing claims and repeated-question/thread history can prevent subsequent outward action.
        records: *id023
        note: Earlier retained activity can veto later selection and day availability even after ambiguous
          sending.
      - scope: Restored tool/chain text at provider continuation
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id024
          - memory.md#mem-rte-payload-restore
          - memory.md#mem-obj-payload-archives
          note: Restored raw tool/assistant content supplies continuation context/evidence.
        records: *id024
        note: Sanitized selected raw context reaches later continuation, not unrestricted store content.
      - scope: Opaque media effect, full hint/structured-envelope consumer routes and other MCP/repair/evaluator
          consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-payload-archives
        - memory.md#mem-obj-tag-summary
        - epistemic.md#epi-rte-structured-materialization
        - runtime.md#rt-rte-mcp-tools
        - memory.md#mem-rte-evaluator-reuse
        note: Metadata or a readable display does not resolve opaque consumption; untraced consumers prevent
          an exhaustive authority union.
      records:
      - memory.md#mem-obj-source-content
      - memory.md#mem-obj-stored-segment
      - memory.md#mem-obj-fact
      - runtime.md#rt-bap-assembled-context
      - epistemic.md#epi-rte-summary-rendering
      - runtime.md#rt-rte-memory-maintenance
      - memory.md#mem-rte-card-refresh
      - epistemic.md#epi-rte-card-integration
      - epistemic.md#epi-bap-card-influence
      - memory.md#mem-obj-source-metadata
      - memory.md#mem-rte-fact-admission
      - memory.md#mem-bap-fact-refusals
      - epistemic.md#epi-rte-fact-proof
      - epistemic.md#epi-rte-fact-withholding
      - runtime.md#rt-bap-engine-watermarks
      - runtime.md#rt-obj-engine-state
      - memory.md#mem-obj-curation-memo
      - memory.md#mem-obj-search-vectors
      - memory.md#mem-obj-tag-summary
      - runtime.md#rt-rte-engagement-stage
      - workflow.md#wf-rte-draft-selection
      - memory.md#mem-rte-payload-restore
      - memory.md#mem-obj-payload-archives
      - epistemic.md#epi-rte-structured-materialization
      - runtime.md#rt-rte-mcp-tools
      - memory.md#mem-rte-evaluator-reuse
      note: Knowledge, instruction, learning, ranking, routing, validation and enforcement each have a
        local retained part and actual consumer. Unconsumed metadata and static policies are not assigned
        authority; unresolved consumers prevent complete coverage.
    write_agency:
      assessment: partial
      units:
      - scope: Completed-turn tagging, summary/fact/vector writes and optional actor-card admission/replacement
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id025
          - runtime.md#rt-rte-memory-maintenance
          - memory.md#mem-rte-card-refresh
          - epistemic.md#epi-rte-card-check
          note: Models propose derivatives and software parses, judges, gates and persists them.
        records: *id025
        note: Code/model admission has no per-derived-content human approval; enabling or manually starting
          compaction does not change this.
      - scope: Normalized import admission, checkpoints/curation memo and proxy archive captures
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id026
          - runtime.md#rt-rte-import-history
          - runtime.md#rt-obj-engine-state
          - memory.md#mem-obj-curation-memo
          - memory.md#mem-obj-payload-archives
          note: Ingestion, state/memo serialization and request capture do not require per-record human
            decisions.
        records: *id026
        note: Software performs content/state admission after caller input; provider-owned persistence
          internals remain separate.
      - scope: Software fact comparisons/refusal decisions and engagement ledger claims
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id027
          - memory.md#mem-rte-fact-admission
          - runtime.md#rt-rte-engagement-stage
          - workflow.md#wf-rte-draft-selection
          note: Policy/store revalidation admits decision ledgers and poster code admits the day/question
            claim.
        records: *id027
        note: Posting intent is not approval of every retained draft; code owns claims and comparison
          disposition.
      - scope: Explicit human-admin canonical edit and fact review path
        assessment: known
        findings:
        - value: manual
          basis: wired
          records: &id028
          - runtime.md#rt-rte-record-edits
          - memory.md#mem-rte-fact-admission
          note: A human admin explicitly supplies or approves replacement text, removal or fact verdict.
        records: *id028
        note: The records distinguish a human admin supplying exact edit/verdict from an arbitrary API
          actor. This finding is confined to that explicit human path.
      - scope: Generic API edits/verdicts and initial host-supplied source/provenance admission control
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-record-edits
        - memory.md#mem-rte-fact-admission
        - memory.md#mem-obj-source-metadata
        note: An actor label or generic caller does not establish human decision versus software admission.
      - scope: Provider-owned saving, additional administrative backfills/repair and evaluator alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-engine-state
        - runtime.md#rt-rte-record-edits
        - memory.md#mem-rte-evaluator-reuse
        note: The records leave provider save mechanisms and alternative replacement bodies incompletely
          inspected.
      records:
      - runtime.md#rt-rte-memory-maintenance
      - memory.md#mem-rte-card-refresh
      - epistemic.md#epi-rte-card-check
      - runtime.md#rt-rte-import-history
      - runtime.md#rt-obj-engine-state
      - memory.md#mem-obj-curation-memo
      - memory.md#mem-obj-payload-archives
      - memory.md#mem-rte-fact-admission
      - runtime.md#rt-rte-engagement-stage
      - workflow.md#wf-rte-draft-selection
      - runtime.md#rt-rte-record-edits
      - memory.md#mem-obj-source-metadata
      - memory.md#mem-rte-evaluator-reuse
      note: Known automatic transformations and the explicit human-admin path coexist. Generic caller
        identity, initial provenance control and other replacement/save mechanisms prevent complete admission-control
        classification.
    curation_operations:
      assessment: partial
      units:
      - scope: Canonical history to segment summaries/facts, tag rollups and actor cards
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id029
          - runtime.md#rt-rte-memory-maintenance
          - memory.md#mem-obj-stored-segment
          - memory.md#mem-obj-fact
          - memory.md#mem-obj-tag-summary
          - memory.md#mem-rte-card-refresh
          note: Summarization, raw-message fact extraction, rollups and bounded person-context derivation
            compress or select retained experience.
        records: *id029
        note: Reduction/extraction of existing claims is consolidation; indeterminate fidelity is not
          evidence of a newly synthesized claim.
      - scope: Canonical edits, derivative rebuild and card replacement/carryover reconsideration
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id030
          - runtime.md#rt-rte-record-edits
          - memory.md#mem-rte-card-refresh
          - epistemic.md#epi-rte-card-integration
          note: Edits/rebuilds and accepted card replacement revise existing retained entries.
        records: *id030
        note: Existing content is revised/replaced under explicit edit or subsequent refresh; transformation
          does not demonstrate benefit.
      - scope: Fact retraction/rejection and source-bound supersession
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records: &id031
          - memory.md#mem-rte-fact-admission
          - epistemic.md#epi-rte-fact-withholding
          - runtime.md#rt-rte-record-edits
          note: Retraction/rejection and supersession withdraw current reliance on older or rejected facts
            while retaining history.
        records: *id031
        note: Withholding changes current reliance while ledgers/supersession history retain disposition;
          unfinished rebuilds can leave facts withheld.
      - scope: Retained paging working-set cold-page collapse/eviction
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id032
          - runtime.md#rt-rte-paging-loop
          - runtime.md#rt-obj-engine-state
          note: Least-recently accessed pages lose full depth or leave the working set; checkpointed depth
            state can carry that reduction forward.
        records: *id032
        note: This is forgetting from the retained working-set tier, not deletion of canonical or archived
          source content.
      - scope: Full tag-rollup transformation, comparison deduplication internals and additional repair/admin/evaluator
          transformations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-tag-summary
        - memory.md#mem-rte-fact-admission
        - runtime.md#rt-rte-record-edits
        - memory.md#mem-rte-evaluator-reuse
        note: Route labels, requested faithfulness and index rebuilds alone do not classify deduplication,
          synthesis or promotion; incomplete bodies prevent a complete operation set.
      records:
      - runtime.md#rt-rte-memory-maintenance
      - memory.md#mem-obj-stored-segment
      - memory.md#mem-obj-fact
      - memory.md#mem-obj-tag-summary
      - memory.md#mem-rte-card-refresh
      - runtime.md#rt-rte-record-edits
      - epistemic.md#epi-rte-card-integration
      - memory.md#mem-rte-fact-admission
      - epistemic.md#epi-rte-fact-withholding
      - runtime.md#rt-rte-paging-loop
      - runtime.md#rt-obj-engine-state
      - memory.md#mem-rte-evaluator-reuse
      note: Implemented consolidation, revision, withdrawal and working-set decay are retained locally.
        No synthesized new claim is inferred from lossy extraction, and no deduplication finding is inferred
        solely from a route label; unresolved transformations remain included.
    read_back_direction:
      assessment: partial
      units:
      - scope: Automatic inbound selection into headless/proxy model context and requester-card delivery
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id033
          - memory.md#mem-rte-inbound-context
          - runtime.md#rt-rte-headless-chat
          - runtime.md#rt-rte-proxy-request
          - memory.md#mem-rte-card-refresh
          note: Code selects and supplies earlier retained memory/preferences into the next foreground
            model invocation.
        records: *id033
        note: Inbound user work triggers selection, but the answer model need not request each retained
          part. Requested API return is not a second automatic supply operation.
      - scope: Model/host paging, recall and proxy archive restoration requests
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id034
          - runtime.md#rt-rte-paging-loop
          - runtime.md#rt-rte-mcp-tools
          - memory.md#mem-rte-payload-restore
          note: Model or host requests recall, expansion or restoration and receives the selected retained
            material.
        records: *id034
        note: These are explicit requests for retained content; downstream formatting/return does not
          independently add another push.
      - scope: Checkpoint restoration and fact-refusal/curation decision read-back by software consumers
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id035
          - runtime.md#rt-obj-engine-state
          - memory.md#mem-rte-fact-admission
          - memory.md#mem-obj-curation-memo
          note: Restoration and update code request saved snapshots, matching memo entries and prior refusals/verdict
            keys.
        records: *id035
        note: Code explicitly loads retained state/decisions for restoration or admission. Their effects
          are distinct from foreground automatic context supply.
      - scope: Engagement history lookup at later repetition/day consumers
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id036
          - runtime.md#rt-rte-engagement-stage
          - workflow.md#wf-rte-draft-selection
          note: Runner/poster queries retained repetition/day state to decide eligibility.
        records: *id036
        note: History is requested internally during candidate/draft admission and posting; caller-owned
          scheduling is not an unsolicited memory notification.
      - scope: Other MCP resources/searches, complete hint/envelope routes, provider alternatives and
          repair/evaluator reuse
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-mcp-tools
        - memory.md#mem-obj-tag-summary
        - epistemic.md#epi-rte-structured-materialization
        - runtime.md#rt-obj-engine-state
        - memory.md#mem-rte-evaluator-reuse
        note: Known push/pull witnesses do not establish all direction units for incompletely traced alternative
          consumers.
      records:
      - memory.md#mem-rte-inbound-context
      - runtime.md#rt-rte-headless-chat
      - runtime.md#rt-rte-proxy-request
      - memory.md#mem-rte-card-refresh
      - runtime.md#rt-rte-paging-loop
      - runtime.md#rt-rte-mcp-tools
      - memory.md#mem-rte-payload-restore
      - runtime.md#rt-obj-engine-state
      - memory.md#mem-rte-fact-admission
      - memory.md#mem-obj-curation-memo
      - runtime.md#rt-rte-engagement-stage
      - workflow.md#wf-rte-draft-selection
      - memory.md#mem-obj-tag-summary
      - epistemic.md#epi-rte-structured-materialization
      - memory.md#mem-rte-evaluator-reuse
      note: Automatic supply to a later answer invocation and requested recall/restore/state reads coexist.
        Inventory retains unresolved consumer chains; host method calls and requested result delivery
        are not indiscriminately counted as pushes.
    read_back_signal:
      assessment: partial
      units:
      - scope: 'Inbound summary/fact selection: query/context embedding and model selection'
        assessment: partial
        findings:
        - value: inferred-embedding
          basis: wired
          records: &id037
          - memory.md#mem-rte-inbound-context
          - memory.md#mem-obj-search-vectors
          note: Query or recent-context vectors rank stored fact vectors, selecting fact text for bounded
            assembly.
        - value: inferred-judgment
          basis: wired
          records: *id037
          note: Query tagging and optional fact-curator decisions infer relevant retained content from
            current work.
        records: *id037
        note: Trigger is inbound work; selector inputs are current query/recent context and eligible candidate
          facts. Exact retriever and curator alternatives remain incompletely inspected.
      - scope: Inbound tag matching and availability/protection/budget selection
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id038
          - memory.md#mem-rte-inbound-context
          - runtime.md#rt-bap-engine-watermarks
          note: Matching retained history/topic tags against current tags selects specific retained parts.
        - value: coarse
          basis: wired
          records: *id038
          note: Protected window, utilization, availability and rendered-token budget select eligible
            retained context without targeted semantic inference.
        records: *id038
        note: Inbound work triggers tag/state filtering and measured-budget admission. Tag identity matches
          select history/topic parts; coarse gates separately bound inclusion.
      - scope: Optional requester-card push
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id039
          - memory.md#mem-rte-card-refresh
          - epistemic.md#epi-rte-card-integration
          note: Tenant/actor/request-audience identity selects the retained requester card delivered to
            the answer model.
        - value: coarse
          basis: wired
          records: *id039
          note: Feature flag, validity and whole-entry confidence/token limits govern card availability
            and bounded delivery.
        records: *id039
        note: Assembly trigger uses tenant/requester actor and audience to read that actor card; validity/confidence/token
          cap further select whole entries.
      - scope: Explicit paging/restore/recall selection operations only
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-paging-loop
        - memory.md#mem-rte-payload-restore
        - runtime.md#rt-rte-mcp-tools
        note: These units fulfill requests, so their supplied ref or requested topic is not an identifier-based
          push signal.
      - scope: Untraced automatic selection alternatives and full hint/evaluator/MCP consumer chains
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-tag-summary
        - memory.md#mem-rte-evaluator-reuse
        - runtime.md#rt-rte-mcp-tools
        note: Their selectors and selected retained parts are not completely established; known pull branches
          cannot make the entire signal axis inapplicable.
      records:
      - memory.md#mem-rte-inbound-context
      - memory.md#mem-obj-search-vectors
      - runtime.md#rt-bap-engine-watermarks
      - memory.md#mem-rte-card-refresh
      - epistemic.md#epi-rte-card-integration
      - runtime.md#rt-rte-paging-loop
      - memory.md#mem-rte-payload-restore
      - runtime.md#rt-rte-mcp-tools
      - memory.md#mem-obj-tag-summary
      - memory.md#mem-rte-evaluator-reuse
      note: Signal findings describe automatic selection into model context only, with trigger/input/selected
        part retained locally. Inapplicable requested operations do not remove uncertainty about other
        automatic consumers.
    trace_learning:
      assessment: partial
      units:
      - scope: Completed-conversation compaction summaries/facts/tag derivatives to later answer context
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id040
          - runtime.md#rt-rte-memory-maintenance
          - memory.md#mem-obj-stored-segment
          - memory.md#mem-obj-fact
          - memory.md#mem-obj-tag-summary
          - memory.md#mem-rte-inbound-context
          note: Recorded conversations automatically produce retained behavior-shaping derivatives consumed
            by later assembly/paging.
        records: *id040
        note: Automatic durable continuation memory qualifies even when lossy or source-text fallback;
          no new claim, parameter update or measured improvement is required.
      - scope: Optional actor evidence to admitted card entries to requester context
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id041
          - memory.md#mem-rte-card-refresh
          - epistemic.md#epi-rte-card-check
          - epistemic.md#epi-rte-card-integration
          note: Actor turns/facts feed automatic card admission/replacement and later preference/context
            delivery.
        records: *id041
        note: Actor-authored traces feed automatic durable card refresh and optional later guidance; the
          disabled default limits activation, not wiring.
      - scope: Posting activity to retained question/day history to later engagement admission
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id042
          - runtime.md#rt-rte-engagement-stage
          - workflow.md#wf-rte-draft-selection
          note: Runner/poster automatically retains staged-question and claim experience that shapes later
            candidate/draft/send behavior.
        records: *id042
        note: A claim may persist even after ambiguous send; later history constrains selection without
          demonstrating improvement.
      - scope: Raw tool/chain/media capture and provider checkpoint alternatives as qualifying learned
          artifacts
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-payload-archives
        - memory.md#mem-rte-payload-restore
        - runtime.md#rt-obj-engine-state
        note: Raw archive/reload alone is not a qualifying derived update; records do not bound all alternative
          transformations or opaque saving. No local or system-wide no is warranted.
      - scope: Full rollup/curator alternatives, additional evaluators/admin repair and general diagnostics
          feedback
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-tag-summary
        - memory.md#mem-obj-curation-memo
        - memory.md#mem-rte-evaluator-reuse
        - runtime.md#rt-rte-record-edits
        note: Missing transformation and feedback-consumer facts prevent exhaustive qualifying-route coverage;
          diagnostic retention alone does not establish learning.
      records:
      - runtime.md#rt-rte-memory-maintenance
      - memory.md#mem-obj-stored-segment
      - memory.md#mem-obj-fact
      - memory.md#mem-obj-tag-summary
      - memory.md#mem-rte-inbound-context
      - memory.md#mem-rte-card-refresh
      - epistemic.md#epi-rte-card-check
      - epistemic.md#epi-rte-card-integration
      - runtime.md#rt-rte-engagement-stage
      - workflow.md#wf-rte-draft-selection
      - memory.md#mem-obj-payload-archives
      - memory.md#mem-rte-payload-restore
      - runtime.md#rt-obj-engine-state
      - memory.md#mem-obj-curation-memo
      - memory.md#mem-rte-evaluator-reuse
      - runtime.md#rt-rte-record-edits
      note: Positive wired trace-fed durable memory and engagement routes coexist with unresolved alternatives.
        This is the comparison axis meaning, not measured improved capacity or exercised self-improvement;
        no unsupported system-wide no is asserted.
    trace_source:
      assessment: partial
      units:
      - scope: Conversation summary/fact/tag maintenance and actor-card derivation inputs
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records: &id043
          - memory.md#mem-obj-source-content
          - runtime.md#rt-rte-memory-maintenance
          - memory.md#mem-rte-card-refresh
          note: Human/assistant session turns feed automatic summary/fact maintenance and actor-card derivation.
        records: *id043
        note: Original input is recorded conversational turns, including user messages. Import/adaptation
          does not change that origin; tool-specific content coverage is not fully resolved.
      - scope: Engagement claim and question history update from staging attempts
        assessment: known
        findings:
        - value: event-streams
          basis: wired
          records: &id044
          - runtime.md#rt-rte-engagement-stage
          - workflow.md#wf-rte-draft-selection
          note: Posting attempts, day claims and staged receipts supply runtime events retained for subsequent
            eligibility decisions.
        records: *id044
        note: The qualifying update records discrete staging/send/claim activity; original candidate-source
          content behind caller-supplied retrieval/drafting is a separate uncertainty.
      - scope: Engagement candidate/draft input origins behind supplied callables
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-engagement-stage
        - workflow.md#wf-rte-draft-selection
        note: The runner accepts caller-supplied candidates and model functions; these do not fully establish
          original trace content feeding every admitted question.
      - scope: Tool/media and provider-state alternatives, other evaluator/repair feedback and opaque
          original trace inputs
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-payload-archives
        - runtime.md#rt-obj-engine-state
        - memory.md#mem-rte-evaluator-reuse
        - runtime.md#rt-rte-record-edits
        note: First qualifying-write coverage is unresolved on these alternatives; archive names do not
          establish tool-trace learning or linked trajectory consumption.
      records:
      - memory.md#mem-obj-source-content
      - runtime.md#rt-rte-memory-maintenance
      - memory.md#mem-rte-card-refresh
      - runtime.md#rt-rte-engagement-stage
      - workflow.md#wf-rte-draft-selection
      - memory.md#mem-obj-payload-archives
      - runtime.md#rt-obj-engine-state
      - memory.md#mem-rte-evaluator-reuse
      - runtime.md#rt-rte-record-edits
      note: Session conversational origin and engagement runtime-event origin have local qualifying-write
        warrants. Other original inputs remain unresolved, so no inapplicable whole-axis claim or exhaustive
        source union is warranted.
---

# Virtual Context memory profile

## Comparison rationale

This classification uses accepted records only. No source file was read, no
record was declared, and no report verification was reopened. Every positive
finding is wired implementation, not observed activation or causal benefit.
Every axis is partial because the retained inventory includes unresolved
alternatives; a known local unit is not a complete system-value claim.

### Parts and canonical identity

The reconciliation supersedes EPI-OBJ-fact with
[MEM-OBJ-fact](memory.md#mem-obj-fact). All fact-object citations use that
canonical record. This affects form, substrate, lineage, authority and the
conversation-derived trace chain without upgrading fact truth or coverage.
Synopsis, structured envelope and tag rollup remain different operative
parts. Card entry/check/integration records likewise remain parts of a wider
cache, not competing identities.

Relational storage, dense vector storage and archive files classify retained
objects rather than encoder weights or serialization. The checkpoint's known
in-process/Redis alternatives do not classify its opaque provider-owned
persistence or the curation provider. Media metadata does not establish the
opaque image payload's form or lineage. See
[RT-OBJ-engine-state](runtime.md#rt-obj-engine-state),
[MEM-OBJ-payload-archives](memory.md#mem-obj-payload-archives) and
[MEM-OBJ-search-vectors](memory.md#mem-obj-search-vectors).

### Independent effects and transformations

Conversation experience has learning authority at its automatic derivative
update; delivered statements have knowledge authority at a later answer
consumer. The card wrapper separately supplies standing response directions.
Neither route proves compliance, semantic truth or improved capacity. The
card's disabled default does not remove its wired path. See
[RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance),
[EPI-RTE-card-integration](epistemic.md#epi-rte-card-integration) and
[EPI-BAP-card-influence](epistemic.md#epi-bap-card-influence).

Fact/refusal state can both test admissibility and enforce a veto. Those
consumers are not a general truth oracle. Source-responsive revision and
withholding support evolve and invalidate. Extraction of standing facts from
retained messages supports consolidate; a dropped negation does not establish
synthesize. Cold paging reduces the retained working-set tier, not the source
archive. Requested deduplication or route naming does not substitute for an
inspected retained-memory transformation. See
[MEM-RTE-fact-admission](memory.md#mem-rte-fact-admission),
[EPI-RTE-fact-withholding](epistemic.md#epi-rte-fact-withholding) and
[RT-RTE-paging-loop](runtime.md#rt-rte-paging-loop), including its memory
annotation.

The explicit human-admin edit/verdict path supports manual admission, while a
generic API actor remains indeterminate. Starting import, compaction or posting
does not make downstream software admission manual. Provider persistence and
other repair/replacement mechanisms stay unresolved. See
[RT-RTE-record-edits](runtime.md#rt-rte-record-edits),
[MEM-RTE-fact-admission](memory.md#mem-rte-fact-admission) and
[RT-RTE-import-history](runtime.md#rt-rte-import-history).

### Selection and trace chains

Inbound work triggers automatic push to the answer model. Explicit paging,
recall and restoration are pull. Requested API delivery is not counted as an
additional push solely because software returns text. Tag/actor identity
matching, inferred vector/model selection and coarse window/budget gates have
distinct local selectors; no lexical finding is invented for incompletely
inspected retrieval strategies. See
[MEM-RTE-inbound-context](memory.md#mem-rte-inbound-context),
[MEM-RTE-payload-restore](memory.md#mem-rte-payload-restore) and
[RT-BAP-engine-watermarks](runtime.md#rt-bap-engine-watermarks).

Automatic durable summaries, facts and cards qualify as trace learning because
later invocations consume them as context or guidance. Session turns retain
session-log origin even when imported. Dense-vector computation establishes
compiled numerical lineage, not encoder training. Raw tool/media archiving
alone does not establish a qualifying learned artifact; lacking bounded absence
records, it also cannot establish a local no covering all its alternatives.
See [MEM-OBJ-source-content](memory.md#mem-obj-source-content),
[MEM-RTE-card-refresh](memory.md#mem-rte-card-refresh) and
[MEM-OBJ-search-vectors](memory.md#mem-obj-search-vectors).

Engagement's automatically retained question/day history shapes future
candidate, draft and posting eligibility. Its staging/claim activity supplies
event-stream input locally. Arbitrary candidate and model-callable origins
remain unresolved. The personal-versus-timed fidelity distinction changes draft
admission but does not eliminate the independent retained-history consumer.
A dry-run return alone has no runner ledger write. See
[RT-RTE-engagement-stage](runtime.md#rt-rte-engagement-stage) and
[WF-RTE-draft-selection](workflow.md#wf-rte-draft-selection).

Full MCP resource/search routes, repair/backfill bodies, evaluator feedback,
initial provenance, opaque providers and complete card serving predicates
remain limited by the accepted accounts. Known witnesses do not turn those
included parts into absence, inapplicability or complete enumeration. Evaluator
cache reuse and answer scoring establish neither benchmark benefit nor a
live behavior-update consumer for general diagnostic scores. See
[MEM-RTE-evaluator-reuse](memory.md#mem-rte-evaluator-reuse),
[EPI-RTE-answer-scoring](epistemic.md#epi-rte-answer-scoring) and
[RT-RTE-mcp-tools](runtime.md#rt-rte-mcp-tools).
