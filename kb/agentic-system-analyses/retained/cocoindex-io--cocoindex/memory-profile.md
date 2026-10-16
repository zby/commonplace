---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'CocoIndex memory comparison: internal reuse, maintained content indexes and shipped session/search
  consumers with unresolved payload and producer alternatives.'
run-id: AAS-2026-10-15-cocoindex-3514227a0537-01
source-identity: https://github.com/cocoindex-io/cocoindex
reviewed-boundary: 1639793b3602408a9cb220728fb30e306d433473
memory-comparison:
  version: 2
  scope: Retained component/function memos, persistent user-state payloads and reconciliation metadata;
    PostgreSQL document/session text, vectors, session metadata and manual extraction products; memoized
    entity decisions; alternate image/filing indexes and their shipped consumers. Includes unresolved
    opaque payloads, upstream imported checkpoint-summary derivation, untraced producer/read-back branches
    and remaining included retained-output alternatives. Excludes static shipped instructions, transient
    retry messages/check exits/current-run maps as memory in themselves, the unacquired CocoIndex-code
    product and provider/model-weight implementations outside the frozen repository; their adapter-facing
    uncertainty remains included.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Component and function memo envelopes, serialized user state and reconciliation bookkeeping
        assessment: known
        findings:
        - value: kv
          basis: wired
          records:
          - runtime.md#rt-obj-component-memoization
          - memory.md#mem-obj-function-memoization
          - memory.md#mem-obj-state-handle
          - memory.md#mem-obj-tracking-info
          note: LMDB retains the memo, user-state and tracking records.
        records:
        - runtime.md#rt-obj-component-memoization
        - memory.md#mem-obj-function-memoization
        - memory.md#mem-obj-state-handle
        - memory.md#mem-obj-tracking-info
        note: The internal per-app LMDB store is a key-value substrate, not an external content index.
      - scope: PostgreSQL document text, vectors, session rows, session metadata and manual extraction
          rows
        assessment: known
        findings:
        - value: rdbms
          basis: wired
          records:
          - memory.md#mem-obj-doc-embedding
          - memory.md#mem-obj-doc-vector
          - memory.md#mem-obj-session-embedding
          - memory.md#mem-obj-session-metadata
          - epistemic.md#epi-obj-module-info
          - epistemic.md#epi-obj-module-counts
          note: These operative row parts are retained in PostgreSQL.
        records:
        - memory.md#mem-obj-doc-embedding
        - memory.md#mem-obj-doc-vector
        - memory.md#mem-obj-session-embedding
        - memory.md#mem-obj-session-metadata
        - epistemic.md#epi-obj-module-info
        - epistemic.md#epi-obj-module-counts
        note: Dense-vector encoding does not replace the relational storage classification.
      - scope: Alternate image and filing indexes
        assessment: partial
        findings:
        - value: vector
          basis: wired
          records:
          - memory.md#mem-rte-alternate-search
          note: Qdrant is the retained vector-search substrate for the image API; this finding does not
            classify the separate image-byte files.
        - value: rdbms
          basis: wired
          records:
          - memory.md#mem-rte-alternate-search
          note: The filing query reads retained filing_chunks through SQL.
        records:
        - memory.md#mem-rte-alternate-search
        note: The record identifies Qdrant and filing_chunks consumers, but full producer/storage arrangements
          are untraced.
      - scope: Other retained outputs and opaque caller/provider alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-function-memoization
        - memory.md#mem-obj-state-handle
        - memory.md#mem-rte-alternate-search
        note: Generic serialized values do not enumerate every operative retained object; alternate producers
          and provider implementations remain untraced. No files, model-weights or service-object storage
          union is inferred from execution components.
      records:
      - runtime.md#rt-obj-component-memoization
      - memory.md#mem-obj-function-memoization
      - memory.md#mem-obj-state-handle
      - memory.md#mem-obj-tracking-info
      - memory.md#mem-obj-doc-embedding
      - memory.md#mem-obj-doc-vector
      - memory.md#mem-obj-session-embedding
      - memory.md#mem-obj-session-metadata
      - epistemic.md#epi-obj-module-info
      - epistemic.md#epi-obj-module-counts
      - memory.md#mem-rte-alternate-search
      note: Inspected internal and external stores are classified separately. Alternate producers and
        arbitrary caller payloads prevent a complete store inventory.
    representational_form:
      assessment: partial
      units:
      - scope: Document chunk text, session transcript/prompt/context text and session intent text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-doc-embedding
          - memory.md#mem-obj-session-embedding
          - memory.md#mem-obj-session-metadata
          note: Source assertions and imported conversational/context text are retained as readable language.
        records:
        - memory.md#mem-obj-doc-embedding
        - memory.md#mem-obj-session-embedding
        - memory.md#mem-obj-session-metadata
        note: These are interpreted textual parts, distinct from their keys and vectors.
      - scope: Document and session lineage fields, counters and metadata arrays
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-doc-embedding
          - memory.md#mem-obj-session-embedding
          - memory.md#mem-obj-session-metadata
          note: Identity, positional and count fields are symbolic rather than linguistic solely because
            encoded as strings.
        records:
        - memory.md#mem-obj-doc-embedding
        - memory.md#mem-obj-session-embedding
        - memory.md#mem-obj-session-metadata
        note: Identifiers, offsets, roles and computed counts have localized fixed-rule uses.
      - scope: Document and session dense embeddings at numerical selection consumers
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-doc-vector
          - memory.md#mem-obj-session-embedding
          - memory.md#mem-rte-session-search
          note: Dense representations distribute numerical information across coordinates; this is not
            a weight-training claim.
        records:
        - memory.md#mem-obj-doc-vector
        - memory.md#mem-obj-session-embedding
        - memory.md#mem-rte-session-search
        note: The records identify dense embeddings consumed by distance ordering.
      - scope: Internal envelopes, slot/key protocol and bookkeeping; concrete counter-test payload
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-obj-component-memoization
          - memory.md#mem-obj-function-memoization
          - memory.md#mem-obj-state-handle
          - memory.md#mem-rte-state-access
          - memory.md#mem-obj-tracking-info
          note: Fixed rules interpret dependencies, identities, ownership, slot keys and the counter.
        records:
        - runtime.md#rt-obj-component-memoization
        - memory.md#mem-obj-function-memoization
        - memory.md#mem-obj-state-handle
        - memory.md#mem-rte-state-access
        - memory.md#mem-obj-tracking-info
        note: This unit excludes arbitrary serialized return and state payload semantics.
      - scope: Manual ModuleInfo descriptions versus API structures and row counts
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - epistemic.md#epi-obj-module-info
          note: Titles and descriptions are textual content.
        - value: symbolic
          basis: wired
          records:
          - epistemic.md#epi-obj-module-info
          - epistemic.md#epi-obj-module-counts
          note: API names/list structure and list cardinalities are fixed-rule structured parts.
        records:
        - epistemic.md#epi-obj-module-info
        - epistemic.md#epi-obj-module-counts
        note: The record separates natural-language title/descriptions from API lists and integer counts.
      - scope: Memoized PairDecision output
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - epistemic.md#epi-obj-pair-decision
          note: The actual consumer interprets localized decision fields.
        records:
        - epistemic.md#epi-obj-pair-decision
        - epistemic.md#epi-rte-pair-proposal
        note: Match/null and canonical-side enum are symbolic decisions; retention-container identity
          remains disputed.
      - scope: Opaque return/user-state payloads and alternate-index unprojected parts
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-component-memoization
        - memory.md#mem-obj-function-memoization
        - memory.md#mem-obj-state-handle
        - memory.md#mem-rte-alternate-search
        note: Byte envelopes and inspected display projections do not determine all consumed payload forms.
      records:
      - memory.md#mem-obj-doc-embedding
      - memory.md#mem-obj-session-embedding
      - memory.md#mem-obj-session-metadata
      - memory.md#mem-obj-doc-vector
      - memory.md#mem-rte-session-search
      - runtime.md#rt-obj-component-memoization
      - memory.md#mem-obj-function-memoization
      - memory.md#mem-obj-state-handle
      - memory.md#mem-rte-state-access
      - memory.md#mem-obj-tracking-info
      - epistemic.md#epi-obj-module-info
      - epistemic.md#epi-obj-module-counts
      - epistemic.md#epi-obj-pair-decision
      - epistemic.md#epi-rte-pair-proposal
      - memory.md#mem-rte-alternate-search
      note: Readable content, fixed-rule metadata and dense numerical parts are split. Generic return
        bytes and incomplete alternate producers prevent complete coverage.
    lineage:
      assessment: partial
      units:
      - scope: Source document chunks and imported session text/metadata at acquisition
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-doc-embedding
          - memory.md#mem-obj-session-embedding
          - memory.md#mem-obj-session-metadata
          note: Text, checkpoint artifacts and metadata enter from source files.
        records:
        - memory.md#mem-obj-doc-embedding
        - memory.md#mem-obj-session-embedding
        - memory.md#mem-obj-session-metadata
        note: Imported describes acquisition; it does not endorse source assertions.
      - scope: Session transcript textual records produced by parsing/filtering
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-session-embedding
          - memory.md#mem-rte-session-search
          note: Automatic parsing selects transcript textual parts and drops invalid or short entries
            for retained retrieval.
        records:
        - memory.md#mem-obj-session-embedding
        - memory.md#mem-rte-session-search
        note: This unit is the local derivation from conversational transcripts, not upstream context.md
          generation.
      - scope: Chunk vectors and session vectors at the inspected embedding step; manual extraction and
          counts
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-doc-vector
          - memory.md#mem-obj-session-embedding
          note: Inference compiles source text into numerical retrieval representations.
        - value: other-compiled
          basis: wired
          records:
          - runtime.md#rt-rte-manual-extraction
          - epistemic.md#epi-obj-module-info
          - epistemic.md#epi-obj-module-counts
          note: Model extraction and fixed list counting produce structured retained products.
        records:
        - memory.md#mem-obj-doc-vector
        - memory.md#mem-obj-session-embedding
        - runtime.md#rt-rte-manual-extraction
        - epistemic.md#epi-obj-module-info
        - epistemic.md#epi-obj-module-counts
        note: This classifies the local transformation, not the provenance of external weights.
      - scope: Memo envelopes, stable IDs and reconciliation bookkeeping
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - runtime.md#rt-obj-component-memoization
          - memory.md#mem-obj-function-memoization
          - memory.md#mem-obj-tracking-info
          - memory.md#mem-rte-function-reuse
          note: Call results, fingerprints, ownership and staged cleanup metadata arise from execution.
        records:
        - runtime.md#rt-obj-component-memoization
        - memory.md#mem-obj-function-memoization
        - memory.md#mem-obj-tracking-info
        - memory.md#mem-rte-function-reuse
        note: Runtime computation produces reuse and reconciliation structures, rather than a human authoring
          these entries.
      - scope: Pair decisions at model proposal and memoization boundary
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - epistemic.md#epi-obj-pair-decision
          - epistemic.md#epi-rte-pair-proposal
          note: The returned structured decision derives from inference over names and configured guidance.
        records:
        - epistemic.md#epi-obj-pair-decision
        - epistemic.md#epi-rte-pair-proposal
        note: The provider proposes the retained decision; no specific memo container is chosen here.
      - scope: Initial user-state payload, upstream context summary and external embedding/model provenance;
          alternate producers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-state-handle
        - memory.md#mem-obj-session-embedding
        - memory.md#mem-obj-doc-vector
        - memory.md#mem-rte-alternate-search
        note: Caller APIs do not establish initial authorship; imported context does not expose its generator;
          model aliases and alternate projections do not resolve upstream derivation. No authored finding
          is licensed for those payloads.
      records:
      - memory.md#mem-obj-doc-embedding
      - memory.md#mem-obj-session-embedding
      - memory.md#mem-obj-session-metadata
      - memory.md#mem-rte-session-search
      - memory.md#mem-obj-doc-vector
      - runtime.md#rt-rte-manual-extraction
      - epistemic.md#epi-obj-module-info
      - epistemic.md#epi-obj-module-counts
      - runtime.md#rt-obj-component-memoization
      - memory.md#mem-obj-function-memoization
      - memory.md#mem-obj-tracking-info
      - memory.md#mem-rte-function-reuse
      - epistemic.md#epi-obj-pair-decision
      - epistemic.md#epi-rte-pair-proposal
      - memory.md#mem-obj-state-handle
      - memory.md#mem-rte-alternate-search
      note: Known import and compilation paths coexist with unresolved upstream summary creation, embedding
        provenance and arbitrary initial-state provenance.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retained document/session text and image/filing result content at search recipients; internal
          diagnostic summaries at operators
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-doc-embedding
          - runtime.md#rt-rte-query-index
          - memory.md#mem-obj-session-embedding
          - memory.md#mem-rte-session-search
          - memory.md#mem-rte-alternate-search
          - memory.md#mem-rte-inspect-state
          note: Selected text, filenames and diagnostic summaries supply information to the requested
            result recipient.
        records:
        - memory.md#mem-obj-doc-embedding
        - runtime.md#rt-rte-query-index
        - memory.md#mem-obj-session-embedding
        - memory.md#mem-rte-session-search
        - memory.md#mem-rte-alternate-search
        - memory.md#mem-rte-inspect-state
        note: Search/display supplies reference material, not standing instructions or factual endorsement.
      - scope: Retained dense document/session vectors and filing text/features at search selectors
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-doc-vector
          - memory.md#mem-obj-session-embedding
          - memory.md#mem-rte-session-search
          note: Dense retained representations determine distance ordering.
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-rte-alternate-search
          note: Retained filing text and vector features contribute lexical and semantic ranks to reciprocal-rank
            fusion.
        records:
        - memory.md#mem-obj-doc-vector
        - memory.md#mem-obj-session-embedding
        - memory.md#mem-rte-session-search
        - memory.md#mem-rte-alternate-search
        note: Scored retained material changes relative result priority even though scoring code is fixed.
      - scope: Memo dependency/identity envelopes and ownership/recovery bookkeeping at engine consumers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-obj-component-memoization
          - memory.md#mem-obj-function-memoization
          - memory.md#mem-rte-function-reuse
          - memory.md#mem-obj-tracking-info
          note: Stored identities/dependencies and ownership select reuse, execution and cleanup paths.
        - value: validation
          basis: wired
          records:
          - runtime.md#rt-obj-component-memoization
          - memory.md#mem-obj-function-memoization
          - memory.md#mem-rte-function-reuse
          note: Stored dependency information is checked for cache reuse admissibility.
        records:
        - runtime.md#rt-obj-component-memoization
        - memory.md#mem-obj-function-memoization
        - memory.md#mem-rte-function-reuse
        - memory.md#mem-obj-tracking-info
        note: Return payload semantics are excluded from this envelope unit.
      - scope: Memoized pair-decision fields at canonical-map application
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - epistemic.md#epi-obj-pair-decision
          - epistemic.md#epi-rte-pair-proposal
          - epistemic.md#epi-rte-pair-disposition
          note: Matched identifier and canonical side select canonical, alias or repoint operations.
        records:
        - epistemic.md#epi-obj-pair-decision
        - epistemic.md#epi-rte-pair-proposal
        - epistemic.md#epi-rte-pair-disposition
        note: This is the decision content consumer, not a claim about which memo schema persists it.
      - scope: Arbitrary memo/state payload effects, session-metadata and manual-content later consumers;
          alternate opaque parts
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-function-memoization
        - memory.md#mem-obj-state-handle
        - memory.md#mem-obj-session-metadata
        - runtime.md#rt-rte-manual-extraction
        - memory.md#mem-rte-alternate-search
        note: Known writes do not establish uninspected downstream consumers. No instruction, enforcement
          or learning authority is inferred merely from retention, a static prompt, or a transient check
          result.
      records:
      - memory.md#mem-obj-doc-embedding
      - runtime.md#rt-rte-query-index
      - memory.md#mem-obj-session-embedding
      - memory.md#mem-rte-session-search
      - memory.md#mem-rte-alternate-search
      - memory.md#mem-rte-inspect-state
      - memory.md#mem-obj-doc-vector
      - runtime.md#rt-obj-component-memoization
      - memory.md#mem-obj-function-memoization
      - memory.md#mem-rte-function-reuse
      - memory.md#mem-obj-tracking-info
      - epistemic.md#epi-obj-pair-decision
      - epistemic.md#epi-rte-pair-proposal
      - epistemic.md#epi-rte-pair-disposition
      - memory.md#mem-obj-state-handle
      - memory.md#mem-obj-session-metadata
      - runtime.md#rt-rte-manual-extraction
      note: Findings name actual consumers, not every force an arbitrary stored payload might acquire.
        Opaque payloads and untraced downstream consumers remain unresolved.
    write_agency:
      assessment: partial
      units:
      - scope: Index row construction/reconciliation and session parsing/embedding admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-index-update
          - memory.md#mem-rte-session-search
          note: Matcher, pipeline and connector code admit transformed retained rows.
        records:
        - runtime.md#rt-rte-index-update
        - memory.md#mem-rte-session-search
        note: No per-content operator decision gates these inspected transformations.
      - scope: Manual extraction proposal, schema-mediated row admission and memo resolution
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-manual-extraction
          - memory.md#mem-rte-function-reuse
          note: These admissions occur without explicit human approval of each result.
        records:
        - runtime.md#rt-rte-manual-extraction
        - memory.md#mem-rte-function-reuse
        note: The model proposes; code validates shape and persists successful results.
      - scope: Internal memo and bookkeeping writes
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-function-memoization
          - memory.md#mem-rte-function-reuse
          - memory.md#mem-obj-tracking-info
          note: Successful computation and submit planning cause retained memo/tracking updates.
        records:
        - memory.md#mem-obj-function-memoization
        - memory.md#mem-rte-function-reuse
        - memory.md#mem-obj-tracking-info
        note: Physical commit is not the agency test; software result resolution and reconciliation determine
          content admission.
      - scope: Concrete counter assignment in shipped test source
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-state-access
          note: Test code increments and assigns the value without a per-value human decision.
        records:
        - memory.md#mem-rte-state-access
        - memory.md#mem-obj-state-handle
        note: Only the concrete code-controlled counter mechanism is classified; no test execution is
          claimed.
      - scope: Generic state initialization/assignment and alternate-index producers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-state-handle
        - memory.md#mem-rte-state-access
        - memory.md#mem-rte-alternate-search
        note: Caller identity alone does not decide manual versus automatic admission; alternate producer
          mechanisms were not traced. Source authorship does not supply a manual admission finding.
      records:
      - runtime.md#rt-rte-index-update
      - memory.md#mem-rte-session-search
      - runtime.md#rt-rte-manual-extraction
      - memory.md#mem-rte-function-reuse
      - memory.md#mem-obj-function-memoization
      - memory.md#mem-obj-tracking-info
      - memory.md#mem-rte-state-access
      - memory.md#mem-obj-state-handle
      - memory.md#mem-rte-alternate-search
      note: Software admission is established locally; initiating an app is not per-record approval. Arbitrary
        initialization and alternate-producer control stay unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Existing document/session target entries refreshed through update/live reconciliation
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-rte-index-update
          - runtime.md#rt-rte-live-maintenance
          - memory.md#mem-rte-session-search
          note: Reprocessing and upsert maintenance replace retained entry content.
        records:
        - runtime.md#rt-rte-index-update
        - runtime.md#rt-rte-live-maintenance
        - memory.md#mem-rte-session-search
        note: This is revision of indexed entries after tracked source change, not abstract synthesis
          or a quality-improvement claim.
      - scope: Internal memo invalidation/recomputation, tombstone cleanup and explicit app drop
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-function-reuse
        - memory.md#mem-obj-tracking-info
        - runtime.md#rt-rte-drop-app
        note: Cache rejection and physical deletion are evidenced, but do not establish the controlled
          invalidate operation of withdrawing reliance while retaining history. Deletion is not assigned
          decay without a forgetting/downweighting mechanism warrant.
      - scope: Model extraction, imported checkpoint summary creation and alternate producer transformations
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-manual-extraction
        - memory.md#mem-obj-session-embedding
        - memory.md#mem-rte-alternate-search
        note: Extraction semantics and upstream context production are unresolved. Session text filtering/chunking
          and index rebuilds alone do not establish claim consolidation, synthesis or deduplication. The
          transient canonical map is not established as a curation transformation over retained memory.
      records:
      - runtime.md#rt-rte-index-update
      - runtime.md#rt-rte-live-maintenance
      - memory.md#mem-rte-session-search
      - memory.md#mem-rte-function-reuse
      - memory.md#mem-obj-tracking-info
      - runtime.md#rt-rte-drop-app
      - runtime.md#rt-rte-manual-extraction
      - memory.md#mem-obj-session-embedding
      - memory.md#mem-rte-alternate-search
      note: Only supported changes to retained entries are classified. Index creation and primary-key
        checks do not establish consolidation or deduplication; opaque transformations remain unresolved.
    read_back_direction:
      assessment: partial
      units:
      - scope: Document/session queries, image/filing requests and diagnostic CLI
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-query-index
          - memory.md#mem-rte-session-search
          - memory.md#mem-rte-alternate-search
          - memory.md#mem-rte-inspect-state
          note: Shipped query/inspection requests select and deliver retained content.
        records:
        - runtime.md#rt-rte-query-index
        - memory.md#mem-rte-session-search
        - memory.md#mem-rte-alternate-search
        - memory.md#mem-rte-inspect-state
        note: The consumer explicitly requests retained material; automatic ranking and printing fulfill
          that request rather than adding another push.
      - scope: Explicit keyed StateHandle access
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-rte-state-access
          note: A later component explicitly requests the stored slot by key.
        records:
        - memory.md#mem-rte-state-access
        note: The API affords later retrieval and the counter test supplies a concrete caller; no deployed
          route is claimed.
      - scope: Component/function automatic cached-return substitution on later computation requests
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-obj-component-memoization
          - memory.md#mem-obj-function-memoization
          - memory.md#mem-rte-function-reuse
          note: Processor/call probing selects retained returns and dependencies without an explicit consumer
            request for those memo records.
        records:
        - runtime.md#rt-obj-component-memoization
        - memory.md#mem-obj-function-memoization
        - memory.md#mem-rte-function-reuse
        note: The caller requests computation, not the retained memo; engine selection automatically supplies
          a prior result when reusable.
      - scope: Session metadata/manual row readers, generic payload consumers and other included alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-session-metadata
        - runtime.md#rt-rte-manual-extraction
        - memory.md#mem-obj-state-handle
        - memory.md#mem-rte-alternate-search
        note: Retention does not determine every later consumer request or automatic delivery path. Live
          source-event maintenance is not itself retained-context read-back.
      records:
      - runtime.md#rt-rte-query-index
      - memory.md#mem-rte-session-search
      - memory.md#mem-rte-alternate-search
      - memory.md#mem-rte-inspect-state
      - memory.md#mem-rte-state-access
      - runtime.md#rt-obj-component-memoization
      - memory.md#mem-obj-function-memoization
      - memory.md#mem-rte-function-reuse
      - memory.md#mem-obj-session-metadata
      - runtime.md#rt-rte-manual-extraction
      - memory.md#mem-obj-state-handle
      note: Requested search/state/diagnostic returns and automatic engine reuse are distinguished within
        the chain. Untraced metadata/manual readers and alternate producers prevent complete direction
        coverage.
    read_back_signal:
      assessment: partial
      units:
      - scope: Engine component and function memo push selection
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-obj-component-memoization
          - memory.md#mem-obj-function-memoization
          - memory.md#mem-rte-function-reuse
          note: Actual path/fingerprint matching selects the reused stored entry; validity checks further
            constrain reuse.
        records:
        - runtime.md#rt-obj-component-memoization
        - memory.md#mem-obj-function-memoization
        - memory.md#mem-rte-function-reuse
        note: 'Trigger: later component/function computation. Inputs: stable component path or call fingerprint
          plus validity dependencies. Selected part: corresponding retained return and dependencies.'
      - scope: Explicit semantic search, state requests and diagnostics
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-query-index
        - memory.md#mem-rte-session-search
        - memory.md#mem-rte-alternate-search
        - memory.md#mem-rte-state-access
        - memory.md#mem-rte-inspect-state
        note: These named operations fulfill requests for retained material; their relevance ranking and
          requested identifiers are not push signals.
      - scope: Uninspected later metadata/manual/generic payload consumers and alternative push possibilities
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-session-metadata
        - runtime.md#rt-rte-manual-extraction
        - memory.md#mem-obj-state-handle
        - memory.md#mem-rte-alternate-search
        note: Missing consumer/selector wiring prevents deciding whether another push exists and, if so,
          its trigger, selector input and selected retained part.
      records:
      - runtime.md#rt-obj-component-memoization
      - memory.md#mem-obj-function-memoization
      - memory.md#mem-rte-function-reuse
      - runtime.md#rt-rte-query-index
      - memory.md#mem-rte-session-search
      - memory.md#mem-rte-alternate-search
      - memory.md#mem-rte-state-access
      - memory.md#mem-rte-inspect-state
      - memory.md#mem-obj-session-metadata
      - runtime.md#rt-rte-manual-extraction
      - memory.md#mem-obj-state-handle
      note: Signals classify push selectors only; vector/lexical ranking inside requested search is not
        an inferred push signal. Incomplete alternative consumers prevent complete coverage.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatic session transcript filtering/embedding to retained text/vectors and later query
          snippets
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-session-embedding
          - memory.md#mem-rte-session-search
          note: Automatic trace-fed writes produce derived retained search context and ranking representations
            with a wired later consumer. No observed use, benefit or agent-instruction installation is
            asserted.
        records:
        - memory.md#mem-obj-session-embedding
        - memory.md#mem-rte-session-search
        note: Raw conversational text is transformed into durable retrieval content and selection representations;
          later snippets supply context/reference to the query recipient.
      - scope: Upstream imported context.md generation and generic state/memo or alternate-index trace-fed
          updates
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-embedding
        - memory.md#mem-obj-state-handle
        - memory.md#mem-obj-function-memoization
        - memory.md#mem-rte-alternate-search
        note: The context summary generator is outside the inspected record; arbitrary payloads and alternative
          producers lack a complete trace-write-artifact-consumer account. No system-wide no is supported
          by these gaps.
      - scope: Pair retry feedback and retained return
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-pair-check
        - epistemic.md#epi-obj-pair-decision
        - epistemic.md#epi-rte-pair-proposal
        note: Retry messages change current-call context but are not shown retained; the final memoized
          decision is supported, but the records do not establish an original qualifying trace input to
          that durable write.
      records:
      - memory.md#mem-obj-session-embedding
      - memory.md#mem-rte-session-search
      - memory.md#mem-obj-state-handle
      - memory.md#mem-obj-function-memoization
      - memory.md#mem-rte-alternate-search
      - epistemic.md#epi-rte-pair-check
      - epistemic.md#epi-obj-pair-decision
      - epistemic.md#epi-rte-pair-proposal
      note: The local session trace-to-derived-search-context path supplies a positive wired route under
        the profile definition, not observed capacity improvement. Upstream summaries, opaque writes and
        other included alternatives remain unresolved.
    trace_source:
      assessment: partial
      units:
      - scope: Qualifying session transcript-derived indexing and later snippet route
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-obj-session-embedding
          - memory.md#mem-rte-session-search
          note: Conversation text extracted from imported full.jsonl supplies the qualifying automatic
            derivation.
        records:
        - memory.md#mem-obj-session-embedding
        - memory.md#mem-rte-session-search
        note: The parsed input records conversational turns; roles and checkpoint packaging do not independently
          add event-stream or tool-trace origins.
      - scope: Imported context/prompt upstream origins, omitted tool payloads and opaque alternative
          write routes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-embedding
        - memory.md#mem-rte-session-search
        - memory.md#mem-obj-state-handle
        - memory.md#mem-obj-function-memoization
        - memory.md#mem-rte-alternate-search
        note: Checkpoint text filtering excludes non-text payloads, and context generation is not inspected.
          No trajectories, tool-traces or event-streams finding follows from filenames, role labels, live
          watcher callbacks or generic serialization.
      records:
      - memory.md#mem-obj-session-embedding
      - memory.md#mem-rte-session-search
      - memory.md#mem-obj-state-handle
      - memory.md#mem-obj-function-memoization
      - memory.md#mem-rte-alternate-search
      note: Classify original content for the qualifying local route, not checkpoint filenames or vector
        serialization. Unknown summary and opaque routes prevent a complete source inventory.
---

# CocoIndex memory profile

## Comparison rationale

All findings classify the supplied records, not fresh source evidence. No source files were read for this mapping. No supersession changes a value: reconciliation retains the component memo, function memo, user-state and tracking objects as distinct referents.

**Storage and encoding.** LMDB maps to `kv`; PostgreSQL maps to `rdbms`, including when it stores vectors. Dense embedding parts are `parametric`, separately from natural-language text and symbolic lineage. The alternate Qdrant consumer supports a vector-store finding without establishing the whole image producer. Opaque serialized returns are not classified from their diagnostic summaries. See [MEM-OBJ-function-memoization](memory.md#mem-obj-function-memoization), [MEM-OBJ-doc-vector](memory.md#mem-obj-doc-vector) and [MEM-RTE-alternate-search](memory.md#mem-rte-alternate-search).

**Local derivations and control.** Imported content and its local compilation are separate lineage paths. Initial state control and external embedding/summary provenance remain unresolved. Operator initiation does not turn software admission into manual approval. Known existing-entry replacement supports evolve; physical deletion, index construction and canonical-map names alone do not establish the other curation operations. See [MEM-RTE-state-access](memory.md#mem-rte-state-access), [RT-RTE-live-maintenance](runtime.md#rt-rte-live-maintenance) and [EPI-RTE-pair-disposition](epistemic.md#epi-rte-pair-disposition).

**Consumers determine force and direction.** Dense vectors and filing features rank candidates; selected textual results supply knowledge rather than standing instructions. Internal envelopes route work and supply cache-validity criteria. Explicit retrieval is pull even though code performs selection. Automatic substitution of retained results for a computation request is push: identity matching actually selects the delivered memo, rather than merely naming an entry in a display. Uninspected consumers prevent treating all remaining directions or signals as absent or inapplicable. See [RT-RTE-query-index](runtime.md#rt-rte-query-index), [MEM-RTE-function-reuse](memory.md#mem-rte-function-reuse) and [MEM-RTE-inspect-state](memory.md#mem-rte-inspect-state).

**Trace-fed context is not demonstrated improvement.** The session parser automatically derives retained textual records and dense retrieval representations from conversational traces, and a later invocation selects and displays those derived snippets. That chain supports wired trace learning under this profile's artifact-and-consumer definition, without inferring an answering agent, improved capacity, factual endorsement or newly generated context summaries. Its source is session logs, not event streams merely because checkpoints have identities. Uninspected upstream context generation and opaque alternatives remain local unknowns. See [MEM-OBJ-session-embedding](memory.md#mem-obj-session-embedding) and [MEM-RTE-session-search](memory.md#mem-rte-session-search).

**Reconciliation limit.** The unresolved attribution of pair-decision retention to a component memo versus a decorated function entry prevents choosing that decision's specific internal container. The profile preserves the independently recorded symbolic decision, inference derivation and canonical-selection consumer without resolving the conflict or borrowing a stronger status. Generic LMDB memo-storage findings concern the separately established memo objects, not a repaired pair-decision dependency. See [EPI-RTE-pair-proposal](epistemic.md#epi-rte-pair-proposal), [RT-OBJ-component-memoization](runtime.md#rt-obj-component-memoization) and [MEM-OBJ-function-memoization](memory.md#mem-obj-function-memoization).

All ten axes remain partial. Positives establish local existence, not complete enumeration across opaque caller content, alternate producers and uninspected downstream consumers. There is no observed-run or causal evidence in these classifications. The transient contributor results and current-call corrective messages do not become retained instruction or learning-authority findings merely because they can influence an immediate next step. See [EPI-RTE-hook-result](epistemic.md#epi-rte-hook-result) and [EPI-RTE-pair-check](epistemic.md#epi-rte-pair-check).
