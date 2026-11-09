---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "KHMS memory comparison: retained trace-derived proposals, reviewed cards, access state and later context routes at the frozen revision."
run-id: "AAS-2026-11-08-khms-memory-c5267e800c56-01"
source-identity: "https://github.com/ksx-cz/khms-memory"
reviewed-boundary: "f739eb976dab199fd4cd64e352192cc0b112c047"
memory-comparison:
  version: 2
  scope: "Retained transcripts/digests, generated MARK findings and candidate proposals, reviewed and archived K-card bodies/metadata, review/coverage and retrieval state, views/navigation, optional dense index, tombstones/corrections, portable/history copies, and their write/maintenance/later-consumer routes. Includes private extension and external-history/provider alternatives where records leave their contents or control unresolved. Excludes shipped static templates/code, fixed inference weights and ordinary unretained current-run context; no enclosing host compaction mechanism is attributed to KHMS."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Retained transcripts/digests, generated lines/proposals, K bodies/metadata, ledgers, views, numerical index/manifest, tombstones, archives and session logs"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace-material"
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-obj-card-content"
                - "memory.md#mem-obj-card-metadata"
                - "memory.md#mem-obj-mark-ledger"
                - "memory.md#mem-obj-views"
                - "memory.md#mem-obj-embedding-index"
                - "memory.md#mem-obj-tombstones"
                - "memory.md#mem-obj-hook-state"
              note: "Markdown, JSON/JSONL and NPZ are retained files; graph relations and numerical encoding do not establish a graph database or changed weights."
          records:
            - "memory.md#mem-obj-trace-material"
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-obj-card-content"
            - "memory.md#mem-obj-card-metadata"
            - "memory.md#mem-obj-mark-ledger"
            - "memory.md#mem-obj-views"
            - "memory.md#mem-obj-embedding-index"
            - "memory.md#mem-obj-tombstones"
            - "memory.md#mem-obj-hook-state"
          note: "The recorded local inventory is file-backed; offline exports remain file copies."
        -
          scope: "Private rendered prompt-extension files"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-operational-change"
              note: "Renderer reads retained extension files when present; actual deployment content is unavailable."
          records:
            - "runtime.md#rt-rte-operational-change"
          note: "File interface is known independently of unknown content."
        -
          scope: "External storage-service history and provider-side retained state, if any"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-card-admission"
            - "runtime.md#rt-cmp-agent-model"
          note: "DAV/version retention and provider internals are unavailable; no additional substrate or provider memory can be classified."
      records:
        - "memory.md#mem-obj-trace-material"
        - "memory.md#mem-obj-inbox"
        - "memory.md#mem-obj-card-content"
        - "memory.md#mem-obj-card-metadata"
        - "memory.md#mem-obj-mark-ledger"
        - "memory.md#mem-obj-views"
        - "memory.md#mem-obj-embedding-index"
        - "memory.md#mem-obj-tombstones"
        - "memory.md#mem-obj-hook-state"
        - "runtime.md#rt-rte-operational-change"
        - "runtime.md#rt-rte-card-admission"
        - "runtime.md#rt-cmp-agent-model"
      note: "Local file storage is established; external-history/provider alternatives are not resolved. Static shipped code and inference weights are not accumulated KHMS memory."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Semantic trace text, findings/proposals, card bodies, correction reasons and view guidance"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace-material"
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-obj-card-content"
                - "memory.md#mem-obj-tombstones"
                - "memory.md#mem-obj-views"
              note: "Models/readers interpret prose, claims and normative guidance."
          records:
            - "memory.md#mem-obj-trace-material"
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-obj-card-content"
            - "memory.md#mem-obj-tombstones"
            - "memory.md#mem-obj-views"
          note: "This unit excludes symbolic envelopes and dense vectors."
        -
          scope: "IDs, status/graph fields, MARK/review coverage, query/TTL state and index manifests"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-card-metadata"
                - "memory.md#mem-obj-mark-ledger"
                - "memory.md#mem-obj-hook-state"
                - "memory.md#mem-obj-embedding-index"
              note: "Fixed code applies enum, identity, edge, hash and timestamp rules."
          records:
            - "memory.md#mem-obj-card-metadata"
            - "memory.md#mem-obj-mark-ledger"
            - "memory.md#mem-obj-hook-state"
            - "memory.md#mem-obj-embedding-index"
          note: "Computed belief is symbolic access metadata, not a learned parameter."
        -
          scope: "Optional retained dense card vectors at cosine/fusion ranking"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-embedding-index"
              note: "Distributed numerical representations feed dense ranking; displayed text is fetched from cards, not decoded from a readable vector summary."
          records:
            - "memory.md#mem-obj-embedding-index"
          note: "Qwen/BGE inference derives vectors without updating encoder weights."
        -
          scope: "Private extension content and inaccessible history/provider payloads"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-operational-change"
            - "runtime.md#rt-rte-card-admission"
            - "runtime.md#rt-cmp-agent-model"
          note: "Extension rendering is known, but exact private content and other opaque payloads are not recorded sufficiently to exhaust their forms."
      records:
        - "memory.md#mem-obj-trace-material"
        - "memory.md#mem-obj-inbox"
        - "memory.md#mem-obj-card-content"
        - "memory.md#mem-obj-tombstones"
        - "memory.md#mem-obj-views"
        - "memory.md#mem-obj-card-metadata"
        - "memory.md#mem-obj-mark-ledger"
        - "memory.md#mem-obj-hook-state"
        - "memory.md#mem-obj-embedding-index"
        - "runtime.md#rt-rte-operational-change"
        - "runtime.md#rt-rte-card-admission"
        - "runtime.md#rt-cmp-agent-model"
      note: "Split prose, fixed-rule metadata and numerical ranking inputs; opaque deployed alternatives prevent complete enumeration."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "External transcripts, repository-change packets and reported findings entering KHMS"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace-material"
                - "epistemic.md#epi-obj-mark"
                - "runtime.md#rt-rte-nightly-proposals"
              note: "Externally produced session/Git records are acquired; acquisition does not endorse their assertions."
          records:
            - "memory.md#mem-obj-trace-material"
            - "epistemic.md#epi-obj-mark"
            - "runtime.md#rt-rte-nightly-proposals"
          note: "Original creation/control of every deployed input is not inferred."
        -
          scope: "Generator findings and per-MARK candidates from retained work records"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-inbox"
                - "runtime.md#rt-rte-nightly-proposals"
                - "runtime.md#rt-rte-mark-evaluation"
              note: "Models derive retained findings and proposals from activity records; earlier candidates feed later evaluation."
          records:
            - "memory.md#mem-obj-inbox"
            - "runtime.md#rt-rte-nightly-proposals"
            - "runtime.md#rt-rte-mark-evaluation"
          note: "Semantic preservation, entailment and novelty remain indeterminate."
        -
          scope: "Views, coverage state, delivery state and numerical index derived by code"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-views"
                - "memory.md#mem-obj-mark-ledger"
                - "memory.md#mem-obj-hook-state"
                - "memory.md#mem-obj-embedding-index"
              note: "Deterministic projections, selection bookkeeping and inferred card vectors have inspectable derivation paths."
          records:
            - "memory.md#mem-obj-views"
            - "memory.md#mem-obj-mark-ledger"
            - "memory.md#mem-obj-hook-state"
            - "memory.md#mem-obj-embedding-index"
          note: "Embedding model identity is not immutable weight provenance."
        -
          scope: "Approved card content and explicit corrections"
          assessment: "partial"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-card-content"
                - "runtime.md#rt-rte-card-admission"
                - "memory.md#mem-obj-inbox"
              note: "Reviewed proposals can become K-card content through the importer."
            -
              value: "authored"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-card-content"
                - "memory.md#mem-obj-tombstones"
              note: "Reviewers may edit content and explicit callers supply correction wording; this is not evidence every author is human."
            -
              value: "imported"
              basis: "claimed"
              records:
                - "epistemic.md#epi-obj-mark"
                - "memory.md#mem-obj-card-content"
              note: "Instructions allow reported external findings with locating quotations."
          records:
            - "memory.md#mem-obj-card-content"
            - "memory.md#mem-obj-tombstones"
            - "memory.md#mem-obj-inbox"
            - "runtime.md#rt-rte-card-admission"
            - "epistemic.md#epi-obj-mark"
          note: "Initial deployed card authorship and actual derivation mix are unavailable; archived and exported copies inherit that unresolved history."
        -
          scope: "Private instruction extensions and original encoder-artifact provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-operational-change"
            - "runtime.md#rt-cmp-qwen"
            - "runtime.md#rt-cmp-bge"
          note: "Known rendering/loading does not resolve authorship or exact pretrained artifact provenance."
      records:
        - "memory.md#mem-obj-trace-material"
        - "epistemic.md#epi-obj-mark"
        - "runtime.md#rt-rte-nightly-proposals"
        - "memory.md#mem-obj-inbox"
        - "runtime.md#rt-rte-mark-evaluation"
        - "memory.md#mem-obj-views"
        - "memory.md#mem-obj-mark-ledger"
        - "memory.md#mem-obj-hook-state"
        - "memory.md#mem-obj-embedding-index"
        - "memory.md#mem-obj-card-content"
        - "memory.md#mem-obj-tombstones"
        - "runtime.md#rt-rte-card-admission"
        - "runtime.md#rt-rte-operational-change"
        - "runtime.md#rt-cmp-qwen"
        - "runtime.md#rt-cmp-bge"
      note: "Known derivations do not settle initial corpus or private instruction lineage."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Cards and pending findings at foreground/review consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-recall-return"
                - "memory.md#mem-rte-pending-evidence"
                - "memory.md#mem-obj-card-content"
              note: "Selected descriptive prose supplies context/evidence, not truth guarantees."
            -
              value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-rte-precheck-return"
                - "memory.md#mem-obj-card-content"
                - "runtime.md#rt-bap-context-delivery"
              note: "Retained policies/methods supply normative guidance; delivery does not establish compliance."
          records:
            - "runtime.md#rt-rte-recall-return"
            - "memory.md#mem-rte-pending-evidence"
            - "memory.md#mem-obj-card-content"
            - "memory.md#mem-rte-precheck-return"
            - "runtime.md#rt-bap-context-delivery"
          note: "Split descriptive and normative effects; precheck is not an action veto."
        -
          scope: "Prior findings/candidates and traces at subsequent proposal-model consumers"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-inbox"
                - "runtime.md#rt-rte-mark-evaluation"
              note: "Retained work records and earlier candidates feed automatic durable proposal updates, which are reused later."
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace-material"
                - "runtime.md#rt-rte-mark-evaluation"
              note: "Selected source excerpts and existing claims also provide evidence for the next judgment."
          records:
            - "memory.md#mem-obj-inbox"
            - "runtime.md#rt-rte-mark-evaluation"
            - "memory.md#mem-obj-trace-material"
          note: "Learning authority here is at the update consumer; downstream context authority is separate."
        -
          scope: "Card prose, tags, dense vectors and derived view ordering at selectors"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-embedding-index"
                - "memory.md#mem-obj-card-metadata"
                - "runtime.md#rt-rte-recall-return"
              note: "Lexical and numerical retained features affect relative priority; belief/condense ordering is a distinct view consumer."
          records:
            - "memory.md#mem-obj-embedding-index"
            - "memory.md#mem-obj-card-metadata"
            - "runtime.md#rt-rte-recall-return"
          note: "No learned ranking policy or semantic relevance success is inferred."
        -
          scope: "Card relations, queue/review state, delivery state and retraction criteria at fixed-code consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-mark-ledger"
                - "memory.md#mem-obj-hook-state"
                - "memory.md#mem-obj-card-metadata"
              note: "Coverage selects next work; relations redirect dead hits; session state changes selection."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-card-metadata"
                - "memory.md#mem-obj-hook-state"
                - "memory.md#mem-obj-tombstones"
                - "epistemic.md#epi-rte-hook-gates"
              note: "Status/TTL controls suppress delivery; retractions can reject reassertions; dispatch seen-state affects conditional denial."
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-tombstones"
              note: "Retained retractions are consumed by lint as candidate-admission criteria."
          records:
            - "memory.md#mem-obj-mark-ledger"
            - "memory.md#mem-obj-hook-state"
            - "memory.md#mem-obj-card-metadata"
            - "memory.md#mem-obj-tombstones"
            - "epistemic.md#epi-rte-hook-gates"
          note: "Conditional guards are not universal filesystem enforcement; unused metadata has no assigned force."
        -
          scope: "Generated navigation and historical error records at documented later readers"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-index-bootstrap"
              note: "Prescribed host loading supplies generated search duties, not bootstrap-card preload."
            -
              value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-retired-lookup"
                - "memory.md#mem-rte-export-copy"
              note: "Historical lookup and portable copied cards have documented reader roles without observed deployment."
          records:
            - "memory.md#mem-rte-index-bootstrap"
            - "memory.md#mem-rte-retired-lookup"
            - "memory.md#mem-rte-export-copy"
          note: "These afforded consumers do not inherit wired live-host consumption."
        -
          scope: "Private extension effects and deployed opaque provider/history consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-operational-change"
            - "runtime.md#rt-cmp-agent-model"
          note: "Rendered private text reaches model calls but its exact force and other opaque consumers cannot be fully classified."
      records:
        - "runtime.md#rt-rte-recall-return"
        - "memory.md#mem-rte-pending-evidence"
        - "memory.md#mem-obj-card-content"
        - "memory.md#mem-rte-precheck-return"
        - "runtime.md#rt-bap-context-delivery"
        - "memory.md#mem-obj-inbox"
        - "runtime.md#rt-rte-mark-evaluation"
        - "memory.md#mem-obj-trace-material"
        - "memory.md#mem-obj-embedding-index"
        - "memory.md#mem-obj-card-metadata"
        - "memory.md#mem-obj-mark-ledger"
        - "memory.md#mem-obj-hook-state"
        - "memory.md#mem-obj-tombstones"
        - "epistemic.md#epi-rte-hook-gates"
        - "memory.md#mem-rte-index-bootstrap"
        - "memory.md#mem-rte-retired-lookup"
        - "memory.md#mem-rte-export-copy"
        - "runtime.md#rt-rte-operational-change"
        - "runtime.md#rt-cmp-agent-model"
      note: "Authority follows actual consumers, not storage labels; known paths coexist with unavailable deployed alternatives."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Generated-line checking, proposal evaluation, derived indexes/views/ledgers and hook-state writes"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-inbox"
                - "runtime.md#rt-rte-mark-evaluation"
                - "memory.md#mem-obj-views"
                - "memory.md#mem-obj-mark-ledger"
                - "memory.md#mem-obj-hook-state"
                - "memory.md#mem-obj-embedding-index"
              note: "Software/model admission occurs without a per-content human decision; launching a job does not make its outputs manual."
          records:
            - "memory.md#mem-obj-inbox"
            - "runtime.md#rt-rte-mark-evaluation"
            - "memory.md#mem-obj-views"
            - "memory.md#mem-obj-mark-ledger"
            - "memory.md#mem-obj-hook-state"
            - "memory.md#mem-obj-embedding-index"
          note: "Authorship and physical file writing are not the admission decision."
        -
          scope: "Foreground capture, initial cards, reviewer import/verdicts, explicit archive/erratum changes and private extensions"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-trace-material"
            - "memory.md#mem-obj-card-content"
            - "memory.md#mem-obj-tombstones"
            - "runtime.md#rt-rte-card-admission"
            - "runtime.md#rt-rte-maintenance-admission"
            - "runtime.md#rt-rte-operational-change"
          note: "Instructions permit human or strong-model review; CLI roles and explicit arguments do not authenticate a per-content human decision. Neither manual nor automatic can cover all these admission alternatives."
      records:
        - "memory.md#mem-obj-inbox"
        - "runtime.md#rt-rte-mark-evaluation"
        - "memory.md#mem-obj-views"
        - "memory.md#mem-obj-mark-ledger"
        - "memory.md#mem-obj-hook-state"
        - "memory.md#mem-obj-embedding-index"
        - "memory.md#mem-obj-trace-material"
        - "memory.md#mem-obj-card-content"
        - "memory.md#mem-obj-tombstones"
        - "runtime.md#rt-rte-card-admission"
        - "runtime.md#rt-rte-maintenance-admission"
        - "runtime.md#rt-rte-operational-change"
      note: "Known automatic derived writes do not resolve generic caller control. Static release admission is excluded from memory scope."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Transcript preprocessing and reusable trace-to-candidate reduction"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace-material"
                - "memory.md#mem-obj-inbox"
                - "runtime.md#rt-rte-mark-evaluation"
              note: "Code selects/clips recorded experience; model pipeline reduces records into reusable retained findings/candidates. Extraction need not be semantically perfect."
          records:
            - "memory.md#mem-obj-trace-material"
            - "memory.md#mem-obj-inbox"
            - "runtime.md#rt-rte-mark-evaluation"
          note: "Consolidation does not imply acceptance, semantic fidelity or synthesis."
        -
          scope: "Proposal replacement, card correction and current-reliance withdrawal"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-obj-tombstones"
              note: "Candidate blocks can be replaced and errata revise specific card wording while retaining retractions."
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-supersession-link"
                - "epistemic.md#epi-rte-triage-verdict"
                - "memory.md#mem-obj-tombstones"
              note: "Supersession/refutation and retractions withdraw ordinary reliance while retaining history."
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-obj-tombstones"
                - "memory.md#mem-obj-card-metadata"
              note: "Archiving removes cards from normal search without reopening historical MARK coverage; bounded forgetting, not a learned temporal decay law."
          records:
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-obj-tombstones"
            - "epistemic.md#epi-rte-supersession-link"
            - "epistemic.md#epi-rte-triage-verdict"
            - "memory.md#mem-obj-card-metadata"
          note: "Index rebuilds, primary-key collision checks and delivery cooldown alone are not curation findings."
        -
          scope: "Weekly cross-domain principles and other semantic maintenance proposals"
          assessment: "partial"
          findings:
            -
              value: "synthesize"
              basis: "claimed"
              records:
                - "epistemic.md#epi-clm-synthesis-review"
              note: "Prompt requests new cross-domain principles from observations; actual new-claim outputs are not supplied."
          records:
            - "epistemic.md#epi-clm-synthesis-review"
            - "runtime.md#rt-rte-maintenance-admission"
            - "memory.md#mem-obj-inbox"
          note: "Wired proposal machinery does not establish that requested novel claims, semantic deduplication or every maintenance transformation occurred. Short/private prompts and concrete outputs remain unresolved."
      records:
        - "memory.md#mem-obj-trace-material"
        - "memory.md#mem-obj-inbox"
        - "runtime.md#rt-rte-mark-evaluation"
        - "memory.md#mem-obj-tombstones"
        - "epistemic.md#epi-rte-supersession-link"
        - "epistemic.md#epi-rte-triage-verdict"
        - "memory.md#mem-obj-card-metadata"
        - "epistemic.md#epi-clm-synthesis-review"
        - "runtime.md#rt-rte-maintenance-admission"
      note: "Only implemented transformations receive wired basis; synthesis remains a separate claimed finding. No promote or semantic dedup is inferred merely from approval or duplicate IDs."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Foreground CLI recall, tagged precheck and requested file/topic access"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-recall-return"
                - "memory.md#mem-rte-pending-evidence"
                - "memory.md#mem-rte-precheck-return"
              note: "A consumer request returns retained cards or OPEN evidence; delivering that result is not a second push."
          records:
            - "runtime.md#rt-rte-recall-return"
            - "memory.md#mem-rte-pending-evidence"
            - "memory.md#mem-rte-precheck-return"
          note: "History returns loaded dead cards, not an automatic archive search."
        -
          scope: "Hook event selection and background packet assembly"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-recall-return"
                - "runtime.md#rt-rte-mark-evaluation"
                - "memory.md#mem-obj-hook-state"
              note: "Event hooks select retained material without a card request; code supplies selected evidence/prior candidates to fresh evaluation calls."
          records:
            - "runtime.md#rt-rte-recall-return"
            - "runtime.md#rt-rte-mark-evaluation"
            - "memory.md#mem-obj-hook-state"
          note: "SessionStart supplies operational reminders, not ranked card bodies; Agent/Task dispatch needs additional host wiring."
        -
          scope: "Generated index loading and portable/historical readers"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-index-bootstrap"
              note: "Host is prescribed to load generated navigation into context."
            -
              value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-retired-lookup"
                - "memory.md#mem-rte-export-copy"
              note: "Documented consumers can request tombstone records or search offline copies."
          records:
            - "memory.md#mem-rte-index-bootstrap"
            - "memory.md#mem-rte-retired-lookup"
            - "memory.md#mem-rte-export-copy"
          note: "Afforded roles are not observations of real use."
        -
          scope: "Opaque host propagation, private guidance and external historical retrieval alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-operational-change"
            - "runtime.md#rt-rte-card-admission"
            - "memory.md#mem-rte-index-bootstrap"
          note: "Recorded interfaces do not inventory all deployed selection/delivery operations."
      records:
        - "runtime.md#rt-rte-recall-return"
        - "memory.md#mem-rte-pending-evidence"
        - "memory.md#mem-rte-precheck-return"
        - "runtime.md#rt-rte-mark-evaluation"
        - "memory.md#mem-obj-hook-state"
        - "memory.md#mem-rte-index-bootstrap"
        - "memory.md#mem-rte-retired-lookup"
        - "memory.md#mem-rte-export-copy"
        - "runtime.md#rt-rte-operational-change"
        - "runtime.md#rt-rte-card-admission"
      note: "Both directions exist; lack of host/deployment detail prevents complete coverage of alternatives."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Matched prompt/tool events selecting ordinary card snippets"
          assessment: "known"
          findings:
            -
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-recall-return"
                - "memory.md#mem-obj-card-metadata"
              note: "Trigger is prompt/tool event; extracted event text scores retained card text/tags."
            -
              value: "inferred-embedding"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-recall-return"
                - "memory.md#mem-obj-embedding-index"
              note: "Optional dense rescue uses event query embeddings and retained card vectors; CLI fusion is a distinct requested path."
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-card-metadata"
                - "runtime.md#rt-rte-recall-return"
              note: "Matched selected-card relation IDs identify loaded live successors and bounded correction pointers actually delivered."
          records:
            - "runtime.md#rt-rte-recall-return"
            - "memory.md#mem-obj-card-metadata"
            - "memory.md#mem-obj-embedding-index"
          note: "Optional branches retain their own basis; correction construction may drop pointers."
        -
          scope: "Automatic risky-command precheck"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-precheck-return"
              note: "Recognized dangerous commands supply tags; exact tag intersection selects policy/gotcha cards for hook delivery."
          records:
            - "memory.md#mem-rte-precheck-return"
          note: "The same tagged operation on explicit request is pull, not another push witness."
        -
          scope: "Next per-MARK packet and session reminders"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mark-evaluation"
                - "memory.md#mem-obj-mark-ledger"
              note: "Queued MARK IDs and named card IDs select retained inputs for later evaluator calls."
            -
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mark-evaluation"
              note: "MARK text ranks related cards and earlier candidates before packet trimming."
            -
              value: "inferred-embedding"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mark-evaluation"
                - "memory.md#mem-obj-embedding-index"
              note: "Optional hybrid neighbors supply retained cards in prepared packets."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-hook-state"
                - "memory.md#mem-obj-mark-ledger"
                - "runtime.md#rt-rte-mark-evaluation"
              note: "SessionStart selects pending/ledger/recent-error availability; packet budget and queue state impose coarse inclusion filters."
          records:
            - "runtime.md#rt-rte-mark-evaluation"
            - "memory.md#mem-obj-mark-ledger"
            - "memory.md#mem-obj-embedding-index"
            - "memory.md#mem-obj-hook-state"
          note: "Selector inputs and retained parts differ; no relevance judgment by the receiving model is counted as a push selector."
        -
          scope: "Generated navigation prescribed for host context"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-index-bootstrap"
              note: "Rebuild selects latest paths/counts for prescribed loading, not per-card identity matching."
          records:
            - "memory.md#mem-rte-index-bootstrap"
          note: "Index carries no card IDs or bodies."
        -
          scope: "Private extension/host selection and unrecorded historical/provider alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-operational-change"
            - "memory.md#mem-rte-index-bootstrap"
            - "runtime.md#rt-rte-card-admission"
          note: "Unknown selection details prevent exhaustive signal classification; a known pull route cannot make these inapplicable."
      records:
        - "runtime.md#rt-rte-recall-return"
        - "memory.md#mem-obj-card-metadata"
        - "memory.md#mem-obj-embedding-index"
        - "memory.md#mem-rte-precheck-return"
        - "runtime.md#rt-rte-mark-evaluation"
        - "memory.md#mem-obj-mark-ledger"
        - "memory.md#mem-obj-hook-state"
        - "memory.md#mem-rte-index-bootstrap"
        - "runtime.md#rt-rte-operational-change"
        - "runtime.md#rt-rte-card-admission"
      note: "Known targeted and coarse pushes coexist; actual host installation/activation remains unobserved."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Retained generated findings and per-MARK candidate updates reused by later evaluation/review"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-obj-trace-material"
                - "runtime.md#rt-rte-nightly-proposals"
                - "runtime.md#rt-rte-mark-evaluation"
              note: "Automatic trace-fed writes produce durable reusable candidate content; earlier proposals already shape later model judgments before reviewed K admission."
          records:
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-obj-trace-material"
            - "runtime.md#rt-rte-nightly-proposals"
            - "runtime.md#rt-rte-mark-evaluation"
          note: "Qualifies without weight training, new knowledge, observed improvement or authenticated human review."
        -
          scope: "Weekly own-mistake-to-guidance proposal path"
          assessment: "partial"
          findings:
            -
              value: "yes"
              basis: "claimed"
              records:
                - "epistemic.md#epi-clm-synthesis-review"
                - "runtime.md#rt-rte-maintenance-admission"
              note: "Instructions request failure-driven countermeasures and recurring-mistake revision, persisted as proposals for subsequent review/use."
          records:
            - "epistemic.md#epi-clm-synthesis-review"
            - "runtime.md#rt-rte-maintenance-admission"
          note: "Staged implementation exists, but no concrete output or exact deployed guidance establishes the full semantic transformation beyond this requested branch."
        -
          scope: "Initial/alternate card writes, private extension replacement and opaque provider-side updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-card-content"
            - "runtime.md#rt-rte-operational-change"
            - "runtime.md#rt-cmp-agent-model"
          note: "Origin/control and qualifying trace input are not fully recorded. No bounded absence record supports a local no."
      records:
        - "memory.md#mem-obj-inbox"
        - "memory.md#mem-obj-trace-material"
        - "runtime.md#rt-rte-nightly-proposals"
        - "runtime.md#rt-rte-mark-evaluation"
        - "epistemic.md#epi-clm-synthesis-review"
        - "runtime.md#rt-rte-maintenance-admission"
        - "memory.md#mem-obj-card-content"
        - "runtime.md#rt-rte-operational-change"
        - "runtime.md#rt-cmp-agent-model"
      note: "Wired yes establishes a supported system existence finding; unresolved alternatives prevent complete coverage. No system-wide no or improved-capacity conclusion follows."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Nightly generation and per-MARK updates from recorded work"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace-material"
                - "memory.md#mem-obj-inbox"
                - "runtime.md#rt-rte-nightly-proposals"
              note: "Original inputs include user/assistant conversational turns; journal wrapping does not turn them into environmental events."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace-material"
                - "runtime.md#rt-rte-nightly-proposals"
              note: "Preprocessing includes tool names and short error-result snippets; ordinary successful tool outputs are not copied wholesale."
          records:
            - "memory.md#mem-obj-trace-material"
            - "memory.md#mem-obj-inbox"
            - "runtime.md#rt-rte-nightly-proposals"
          note: "These are the original trace inputs, not labels assigned by an adapter."
        -
          scope: "Git-change/journal event mixtures, weekly own-mistake sources and private/opaque update alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-trace-material"
            - "epistemic.md#epi-clm-synthesis-review"
            - "runtime.md#rt-rte-operational-change"
            - "runtime.md#rt-cmp-agent-model"
          note: "Journal records can summarize decisions/outcomes and Git changes, but their exact origin and sequence are unavailable; no added event-streams or trajectories finding follows from serialization or timestamps. Private writes may not be trace-fed at all."
      records:
        - "memory.md#mem-obj-trace-material"
        - "memory.md#mem-obj-inbox"
        - "runtime.md#rt-rte-nightly-proposals"
        - "epistemic.md#epi-clm-synthesis-review"
        - "runtime.md#rt-rte-operational-change"
        - "runtime.md#rt-cmp-agent-model"
      note: "Known conversational/tool inputs do not settle every mixed origin. Trace sources remain relevant because qualifying writes exist."
---

# KHMS memory profile

## Comparison rationale

The strongest supported memory mechanism is automatic production of durable
trace-derived proposals that later evaluation calls consume. Reviewed K-card
adoption is a separate admission path. The retained intermediate candidates
already meet the trace-learning write-route definition; observed improvement,
parameter training and semantic truth acceptance are not required.
[MEM-OBJ-inbox](memory.md#mem-obj-inbox) and
[RT-RTE-mark-evaluation](runtime.md#rt-rte-mark-evaluation) retain that chain.
The weekly request for novel principles and own-mistake countermeasures stays
at claimed semantic synthesis/learning basis:
[EPI-CLM-synthesis-review](epistemic.md#epi-clm-synthesis-review).
Wired orchestration cannot upgrade a requested novel claim to a demonstrated
transformation.

File-backed edges are not evidence of a graph database. NPZ numerical state
is file storage with distributed-parametric form at its dense-ranking
consumer; it is not a changed encoder model.
[MEM-OBJ-card-metadata](memory.md#mem-obj-card-metadata) and
[MEM-OBJ-embedding-index](memory.md#mem-obj-embedding-index) distinguish these.
The initial corpus and exact encoder artifacts remain unavailable. Known
derivation paths therefore do not establish complete lineage.

Authority depends on the consumer. Card facts provide knowledge; retained
policy text provides instruction rather than an action veto. Trace inputs
at proposal updates have learning authority; statuses, review coverage and
session-state controls route or suppress code operations. Retraction text
also supplies lint criteria, independently of its historical explanatory
role. See [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery),
[MEM-OBJ-mark-ledger](memory.md#mem-obj-mark-ledger),
[MEM-OBJ-hook-state](memory.md#mem-obj-hook-state) and
[MEM-OBJ-tombstones](memory.md#mem-obj-tombstones).
These forces do not prove model compliance or beneficial activation.

Explicit recall is pull. Event-driven card injection and code-assembled
later evaluation packets are push, with targeted and coarse selectors kept
separate. SessionStart supplies operational reminders, not a card search.
Generated MEMORY navigation has an afforded loading channel; it contains
neither card bodies nor the bootstrap-digest body claimed by older doctrine.
See [RT-RTE-recall-return](runtime.md#rt-rte-recall-return),
[MEM-OBJ-hook-state](memory.md#mem-obj-hook-state) and
[MEM-RTE-index-bootstrap](memory.md#mem-rte-index-bootstrap).
Tag matching on the automatic risky-action branch is an actual identity
selector, unlike an ID merely printed on a requested file.
[MEM-RTE-precheck-return](memory.md#mem-rte-precheck-return) supplies that
bounded witness.

No supersession affects these classifications: reconciliation establishes
no duplicate replacement. The combined epistemic card and the memory
body/metadata records remain valid at different granularities. The supplied
doctrine/implementation distinctions remain local limits rather than competing
whole-system verdicts. In particular, current-only search excludes archives,
history returns loaded dead cards, and correction pointers are bounded.
[MEM-OBJ-card-metadata](memory.md#mem-obj-card-metadata) and
[RT-RTE-recall-return](runtime.md#rt-rte-recall-return) support those limits.

Missing initial-content control, private prompt contents, provider internals,
deployed corpus and external version-retention evidence prevent complete
coverage, not the positive classifications retained here. Generic reviewer
identity does not establish manual content admission. No accepted bounded
absence record warrants a local trace-learning "no"; unknown alternatives
cannot be converted into negatives. The supported "yes" is an existence
finding, not an exhaustive-value or improved-capacity conclusion.
See [MEM-OBJ-card-content](memory.md#mem-obj-card-content),
[RT-RTE-operational-change](runtime.md#rt-rte-operational-change) and
[RT-CMP-agent-model](runtime.md#rt-cmp-agent-model).

Source-read log: no frozen-source reads were needed. Classification used only
the supplied accepted members and their retained passages; no record,
quotation or evidence was added.
