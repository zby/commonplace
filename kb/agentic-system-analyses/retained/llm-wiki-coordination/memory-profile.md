---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "LLM Wiki Coordination memory profile: accumulated downstream wiki discussion, coordination metadata, reviewed pages and maintenance records."
run-id: AAS-2026-10-14-llm-wiki-coordination-a12f3c7007f2-01
source-identity: https://github.com/AEVYRA/llm-wiki-coordination
reviewed-boundary: "126749634d1c8c2fd6141f59711c882c2d629699"
memory-comparison:
  version: 2
  scope: "Included: downstream thread context/OQ, metadata and orientation estimates, contribution/closure/reopen and historical entries, canon-page content and revision-specific endorsements, persona manifests, retained audit reports/global-log summaries and cemetery tombstones; their admission, maintenance and later participant/page-review/audit consumption. Excluded: unchanged shipped protocols and maintainer source, audit-instance caches/indexes/findings, external provider parameters and unshipped host context management."
  axes:
    storage_substrate:
      assessment: known
      units:
        - scope: "Thread context, meta/zhat, entries, canon pages, endorsements, manifests, reports/log summaries and tombstones"
          assessment: known
          findings:
            - value: files
              basis: claimed
              records: [memory.md#mem-obj-thread-context, memory.md#mem-obj-thread-meta, memory.md#mem-obj-thread-entries, memory.md#mem-obj-canon-pages, memory.md#mem-obj-consensus-block, memory.md#mem-obj-anchor-form, memory.md#mem-obj-audit-reports, memory.md#mem-obj-cemetery-log]
              note: "Protocols prescribe downstream Markdown/YAML/manifest/log files; no downstream instance or deployed storage is supplied."
          records: [memory.md#mem-obj-thread-context, memory.md#mem-obj-thread-meta, memory.md#mem-obj-thread-entries, memory.md#mem-obj-canon-pages, memory.md#mem-obj-consensus-block, memory.md#mem-obj-anchor-form, memory.md#mem-obj-audit-reports, memory.md#mem-obj-cemetery-log]
          note: "All recorded retained surfaces are file objects, including unspecified report and tombstone layouts; unknown schema does not imply unknown substrate."
      records: [memory.md#mem-obj-thread-context, memory.md#mem-obj-thread-meta, memory.md#mem-obj-thread-entries, memory.md#mem-obj-canon-pages, memory.md#mem-obj-consensus-block, memory.md#mem-obj-anchor-form, memory.md#mem-obj-audit-reports, memory.md#mem-obj-cemetery-log, runtime.md#rt-abs-runtime-orchestration]
      note: "Known for the complete prescribed retained-object inventory, not observed deployment. Process memory and external model weights are outside this memory boundary."
    representational_form:
      assessment: partial
      units:
        - scope: "Context/OQ and entry prose, canon prose, dispute reasons and identity manifests at interpreting agents/users"
          assessment: known
          findings:
            - value: natural-language
              basis: claimed
              records: [memory.md#mem-obj-thread-context, memory.md#mem-obj-thread-entries, memory.md#mem-obj-canon-pages, memory.md#mem-obj-consensus-block, memory.md#mem-obj-anchor-form]
              note: "Retained prose acquires meaning through participant/user interpretation, not fixed symbolic rules."
          records: [memory.md#mem-obj-thread-context, memory.md#mem-obj-thread-entries, memory.md#mem-obj-canon-pages, memory.md#mem-obj-consensus-block, memory.md#mem-obj-anchor-form]
          note: "Classifies the recorded textual parts, not unshipped signed payloads or reconstruction algorithms."
        - scope: "Thread status, references, evaluation/checkpoint vectors, page lifecycle/revision and endorsement statuses at the audit"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-thread-meta, memory.md#mem-obj-thread-entries, memory.md#mem-obj-consensus-block, epistemic.md#epi-rte-vector-check, epistemic.md#epi-rte-consensus-check]
              note: "Fixed predicates, arithmetic and string tests consume localized YAML fields; numerical vectors are not distributed parameters."
          records: [memory.md#mem-obj-thread-meta, memory.md#mem-obj-thread-entries, memory.md#mem-obj-consensus-block, epistemic.md#epi-rte-vector-check, epistemic.md#epi-rte-consensus-check]
          note: "Symbolic audit consumption does not upgrade external semantic interpretation or endorse score truth."
        - scope: "Target/orientation and endorsement/revision fields at external coordination consumers"
          assessment: known
          findings:
            - value: symbolic
              basis: claimed
              records: [memory.md#mem-obj-thread-meta, epistemic.md#epi-obj-zhat, runtime.md#rt-rte-thread-participation, runtime.md#rt-rte-canon-admission]
              note: "Prescribed sum, deficit, normalization and revision/quorum comparisons provide localized rules."
            - value: natural-language
              basis: claimed
              records: [memory.md#mem-obj-thread-meta, epistemic.md#epi-obj-zhat, memory.md#mem-obj-consensus-block]
              note: "Participants interpret orientation preferences and the meaning of endorsement judgments; symbolic serialization does not eliminate that path."
          records: [memory.md#mem-obj-thread-meta, epistemic.md#epi-obj-zhat, memory.md#mem-obj-consensus-block, runtime.md#rt-rte-thread-participation, runtime.md#rt-rte-canon-admission]
          note: "Mixed consumption paths remain separate findings."
        - scope: "Retained audit reports/log summaries and cemetery records"
          assessment: partial
          findings:
            - value: natural-language
              basis: claimed
              records: [memory.md#mem-obj-audit-reports, memory.md#mem-obj-cemetery-log]
              note: "Interpreted summaries and structural-history records are prescribed."
          records: [memory.md#mem-obj-audit-reports, memory.md#mem-obj-cemetery-log]
          note: "Report format and optional retained structured findings are unspecified; no later fixed-rule consumer is established."
      records: [memory.md#mem-obj-thread-context, memory.md#mem-obj-thread-meta, memory.md#mem-obj-thread-entries, memory.md#mem-obj-canon-pages, memory.md#mem-obj-consensus-block, memory.md#mem-obj-anchor-form, memory.md#mem-obj-audit-reports, memory.md#mem-obj-cemetery-log, epistemic.md#epi-obj-zhat]
      note: "Textual and symbolic paths are supported, while maintenance-output formats prevent complete form classification. No parametric retained object is included."
    lineage:
      assessment: partial
      units:
        - scope: "Initiating context, new contributions, initial coordination settings, page edits, endorsements, co-created manifests and external maintenance records"
          assessment: known
          findings:
            - value: authored
              basis: claimed
              records: [memory.md#mem-obj-thread-context, memory.md#mem-obj-thread-meta, memory.md#mem-obj-thread-entries, memory.md#mem-obj-canon-pages, memory.md#mem-obj-consensus-block, memory.md#mem-obj-anchor-form, memory.md#mem-obj-audit-reports, memory.md#mem-obj-cemetery-log]
              note: "Agents, users or deletion operators create the recorded content; this classifies production paths, not human approval."
          records: [memory.md#mem-obj-thread-context, memory.md#mem-obj-thread-meta, memory.md#mem-obj-thread-entries, memory.md#mem-obj-canon-pages, memory.md#mem-obj-consensus-block, memory.md#mem-obj-anchor-form, memory.md#mem-obj-audit-reports, memory.md#mem-obj-cemetery-log]
          note: "Unknown initial target rationale does not erase the specified initializer."
        - scope: "Historical dialogue acquisition"
          assessment: partial
          findings:
            - value: imported
              basis: claimed
              records: [epistemic.md#epi-rte-archival-import, memory.md#mem-obj-thread-entries]
              note: "Adopters wrap previously existing discussion without reconstructing the evaluation chain."
          records: [epistemic.md#epi-rte-archival-import, memory.md#mem-obj-thread-entries]
          note: "Original authorship, provenance and warrant of imported text remain unresolved."
        - scope: "Peer evaluations, closure summary/checkpoint and observation-derived orientation"
          assessment: partial
          findings:
            - value: trace-extracted
              basis: claimed
              records: [memory.md#mem-obj-thread-entries, epistemic.md#epi-rte-peer-judgment]
              note: "Participant activity is retained and converted to peer assessments and closing summaries/checkpoints."
            - value: trace-extracted
              basis: afforded
              records: [memory.md#mem-rte-profile-refinement]
              note: "A formula affords deriving preferred orientation from past attributed contribution evaluations; it supplies no identified writer."
          records: [memory.md#mem-obj-thread-entries, epistemic.md#epi-rte-peer-judgment, memory.md#mem-rte-profile-refinement, epistemic.md#epi-obj-zhat]
          note: "Derivation is specified, but initial profile provenance, history window and updates are unresolved; the reconciled doctrine-status disagreement remains."
        - scope: "Canon derivation and retained technical audit diagnoses"
          assessment: partial
          findings:
            - value: other-compiled
              basis: claimed
              records: [memory.md#mem-obj-canon-pages, memory.md#mem-obj-audit-reports, memory.md#mem-rte-audit-retention]
              note: "Canon is produced from discussion and reports incorporate diagnostics derived from current retained wiki state; neither is model-parameter provenance."
          records: [memory.md#mem-obj-canon-pages, memory.md#mem-obj-audit-reports, memory.md#mem-rte-audit-retention]
          note: "The exact canon transformation and source-reason mapping are unspecified; report persistence is external, not a wired compiler output write."
      records: [memory.md#mem-obj-thread-context, memory.md#mem-obj-thread-meta, memory.md#mem-obj-thread-entries, memory.md#mem-obj-canon-pages, memory.md#mem-obj-consensus-block, memory.md#mem-obj-anchor-form, memory.md#mem-obj-audit-reports, memory.md#mem-obj-cemetery-log, memory.md#mem-rte-profile-refinement, epistemic.md#epi-rte-archival-import]
      note: "Positive production/import/derivation paths coexist with unresolved original historical provenance, profile initialization and canon transformation."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Context, preceding contribution and canon prose read by later participants/reviewers"
          assessment: known
          findings:
            - value: knowledge
              basis: claimed
              records: [memory.md#mem-obj-thread-context, memory.md#mem-obj-thread-entries, memory.md#mem-obj-canon-pages, runtime.md#rt-rte-thread-participation, runtime.md#rt-rte-canon-admission]
              note: "Prose supplies task context, candidate arguments and page content for review; knowledge authority here means supplied context, not warranted truth."
          records: [memory.md#mem-obj-thread-context, memory.md#mem-obj-thread-entries, memory.md#mem-obj-canon-pages, runtime.md#rt-rte-thread-participation, runtime.md#rt-rte-canon-admission]
          note: "No concrete adopted canon page supports an additional standing-instruction classification."
        - scope: "Contribution prose and peer scores at evaluation, closing summary and next-direction consumers"
          assessment: known
          findings:
            - value: learning
              basis: claimed
              records: [memory.md#mem-obj-thread-entries, epistemic.md#epi-rte-peer-judgment, runtime.md#rt-rte-thread-participation]
              note: "Recorded contributions feed new retained evaluations and summaries that shape later work, without demonstrating improved capacity."
            - value: ranking
              basis: claimed
              records: [epistemic.md#epi-rte-peer-judgment, runtime.md#rt-rte-thread-participation]
              note: "Retained scores influence relative next-axis priority through the target deficit."
            - value: routing
              basis: claimed
              records: [memory.md#mem-obj-thread-meta, runtime.md#rt-rte-thread-participation]
              note: "Target, preferred orientation and accumulated scores select the intended next contribution direction."
          records: [memory.md#mem-obj-thread-entries, memory.md#mem-obj-thread-meta, epistemic.md#epi-rte-peer-judgment, runtime.md#rt-rte-thread-participation]
          note: "All these effects are prescribed external-agent consumers, not dispatched or observed behavior."
        - scope: "Past evaluation vectors at orientation refinement and resulting zhat at later participants"
          assessment: partial
          findings:
            - value: learning
              basis: afforded
              records: [memory.md#mem-rte-profile-refinement]
              note: "Past participation experience can feed a durable preferred-direction estimate; automatic admission remains unknown."
            - value: routing
              basis: afforded
              records: [memory.md#mem-rte-profile-refinement, epistemic.md#epi-obj-zhat]
              note: "Resulting estimate supplies preferred-direction guidance subordinate to deficit rotation."
          records: [memory.md#mem-rte-profile-refinement, epistemic.md#epi-obj-zhat]
          note: "Producer, actual replacement and delivery are unresolved, and the records disagree about doctrine status."
        - scope: "Consensus/revision metadata at page reviewers and canon approvers"
          assessment: known
          findings:
            - value: instruction
              basis: claimed
              records: [memory.md#mem-obj-consensus-block, runtime.md#rt-rte-canon-admission]
              note: "Retained revision/status directs re-review and renewal of endorsements."
            - value: validation
              basis: claimed
              records: [memory.md#mem-obj-consensus-block, runtime.md#rt-rte-canon-admission]
              note: "Endorsements, stale/disputed state and quorum determine prescribed canonical admissibility."
            - value: enforcement
              basis: claimed
              records: [runtime.md#rt-rte-canon-admission, runtime.md#rt-clm-canon-enforcement]
              note: "Stale or disputed state prohibits specified canonical transitions under the protocol only; there is no shipped admission interceptor."
          records: [memory.md#mem-obj-consensus-block, runtime.md#rt-rte-canon-admission, runtime.md#rt-clm-canon-enforcement]
          note: "Normative veto and criterion are separately classified without attributing implemented enforcement."
        - scope: "Thread migration/status metadata at deterministic audit dispatch"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-thread-meta, runtime.md#rt-rte-archival-audit]
              note: "Retained archival flag selects the early-return path, omitting metadata/entry-chain checks."
          records: [memory.md#mem-obj-thread-meta, runtime.md#rt-rte-archival-audit]
          note: "This is an implemented effect on a later checker, not a provider context selector."
        - scope: "Manifest/persona retained identity at recognition and active-agent qualification"
          assessment: partial
          findings:
            - value: knowledge
              basis: claimed
              records: [memory.md#mem-obj-anchor-form]
              note: "Manifest content supplies intended identity/continuity context for recognition."
            - value: validation
              basis: claimed
              records: [memory.md#mem-obj-anchor-form, runtime.md#rt-rte-canon-admission]
              note: "Persistent persona/note existence is a prescribed active-agent qualification for consensus."
          records: [memory.md#mem-obj-anchor-form, runtime.md#rt-rte-canon-admission]
          note: "No loader or reconstruction algorithm establishes the retained manifest's additional downstream behavioral effects."
        - scope: "Retained reports/global-log summaries and cemetery tombstones"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-audit-reports, memory.md#mem-obj-cemetery-log, memory.md#mem-rte-audit-retention, memory.md#mem-rte-page-withdrawal]
          note: "No specified later consumer establishes authority for these retained outputs; current stdout advisory force cannot be transferred to them."
      records: [memory.md#mem-obj-thread-context, memory.md#mem-obj-thread-meta, memory.md#mem-obj-thread-entries, memory.md#mem-obj-canon-pages, memory.md#mem-obj-consensus-block, memory.md#mem-obj-anchor-form, memory.md#mem-obj-audit-reports, memory.md#mem-obj-cemetery-log, memory.md#mem-rte-profile-refinement, runtime.md#rt-rte-thread-participation, runtime.md#rt-rte-canon-admission, runtime.md#rt-rte-archival-audit]
      note: "Local consumers support several forces; unspecified maintenance readers and manifest/profile delivery prevent complete authority coverage."
    write_agency:
      assessment: partial
      units:
        - scope: "Agent creation/appending of context, metadata, contributions, evaluations, closing summaries/checkpoints, page edits and individual endorsements; report/log authorship"
          assessment: known
          findings:
            - value: automatic
              basis: claimed
              records: [memory.md#mem-obj-thread-context, memory.md#mem-obj-thread-meta, memory.md#mem-obj-thread-entries, memory.md#mem-obj-canon-pages, memory.md#mem-obj-consensus-block, memory.md#mem-rte-audit-retention]
              note: "External agent admission is prescribed without a human per-content approval decision. Starting the work is not manual admission of every entry."
          records: [memory.md#mem-obj-thread-context, memory.md#mem-obj-thread-meta, memory.md#mem-obj-thread-entries, memory.md#mem-obj-canon-pages, memory.md#mem-obj-consensus-block, memory.md#mem-rte-audit-retention]
          note: "Automatic is a control classification of the prescribed agent path, not implemented scheduling or physical persistence."
        - scope: "Closure recognition, full/soft canonical promotion, manifest recognition and mutually acknowledged modification"
          assessment: known
          findings:
            - value: manual
              basis: claimed
              records: [runtime.md#rt-rte-canon-admission, memory.md#mem-obj-anchor-form]
              note: "User Recognition/explicit approval governs these admission transitions; manifest changes require mutual acknowledgment."
          records: [runtime.md#rt-rte-canon-admission, memory.md#mem-obj-anchor-form]
          note: "Human admission is separate from earlier agent authorship and endorsement writes."
        - scope: "Orientation-estimate replacement, historical import and tombstone/deletion admission"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-profile-refinement, epistemic.md#epi-rte-archival-import, memory.md#mem-rte-page-withdrawal]
          note: "The profile writer is unspecified; generic adopter/deletion operator identity does not resolve per-content human control for the other paths."
      records: [memory.md#mem-obj-thread-context, memory.md#mem-obj-thread-meta, memory.md#mem-obj-thread-entries, memory.md#mem-obj-canon-pages, memory.md#mem-obj-consensus-block, memory.md#mem-obj-anchor-form, memory.md#mem-rte-audit-retention, memory.md#mem-rte-profile-refinement, epistemic.md#epi-rte-archival-import, memory.md#mem-rte-page-withdrawal, runtime.md#rt-rte-canon-admission]
      note: "Known agent and user mechanisms coexist with unresolved profile/import/deletion control."
    curation_operations:
      assessment: partial
      units:
        - scope: "Closure summary and persisted cumulative checkpoint over retained discussion"
          assessment: known
          findings:
            - value: consolidate
              basis: claimed
              records: [memory.md#mem-obj-thread-entries, runtime.md#rt-rte-thread-participation]
              note: "Closing summary and accumulated checkpoint reduce retained discussion/evaluations without requiring deletion of inputs."
          records: [memory.md#mem-obj-thread-entries, runtime.md#rt-rte-thread-participation]
          note: "Summary/checkpoint transformation is prescribed, not implemented by a shipped writer."
        - scope: "Existing page revision and consensus lifecycle maintenance"
          assessment: known
          findings:
            - value: evolve
              basis: claimed
              records: [memory.md#mem-obj-canon-pages, memory.md#mem-obj-consensus-block, runtime.md#rt-rte-canon-admission]
              note: "Authors revise existing page content and agents renew existing revision-specific endorsements."
            - value: invalidate
              basis: claimed
              records: [memory.md#mem-obj-consensus-block, runtime.md#rt-rte-canon-admission]
              note: "Stale/disputed endorsements withdraw current reliance while retaining recorded state/history; disputed soft canon returns to working."
            - value: promote
              basis: claimed
              records: [runtime.md#rt-rte-canon-admission, memory.md#mem-obj-canon-pages]
              note: "Approved full/soft canonical transitions raise the page's retained maturity tier."
          records: [memory.md#mem-obj-canon-pages, memory.md#mem-obj-consensus-block, runtime.md#rt-rte-canon-admission]
          note: "These are doctrine transformations; the audit neither performs nor enforces them."
        - scope: "Orientation refinement from retained past evaluations"
          assessment: partial
          findings:
            - value: consolidate
              basis: afforded
              records: [memory.md#mem-rte-profile-refinement]
              note: "Sum/normalization affords a reduced representation of attributed past vectors."
            - value: evolve
              basis: afforded
              records: [memory.md#mem-rte-profile-refinement]
              note: "The working estimate can be refined rather than remaining a fixed constant."
          records: [memory.md#mem-rte-profile-refinement, epistemic.md#epi-obj-zhat]
          note: "Unknown update mechanism and observation scope prevent complete transformation coverage or a justified synthesis finding."
        - scope: "New canon derivation, maintenance summaries, manifest changes, historical wrapping and hard deletion"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-canon-pages, memory.md#mem-rte-audit-retention, memory.md#mem-obj-anchor-form, epistemic.md#epi-rte-archival-import, memory.md#mem-rte-page-withdrawal]
          note: "Canon semantic relation is unspecified; report shortening lacks a defined claims-preservation transformation. Manifest updates and hard deletion lack enough detail for these controlled operations. Acquisition/wrapping alone is not curation; hard removal with a tombstone is not evidenced decay or history-preserving invalidation of the old content."
      records: [memory.md#mem-obj-thread-entries, memory.md#mem-obj-canon-pages, memory.md#mem-obj-consensus-block, memory.md#mem-rte-profile-refinement, memory.md#mem-rte-audit-retention, memory.md#mem-obj-anchor-form, epistemic.md#epi-rte-archival-import, memory.md#mem-rte-page-withdrawal, runtime.md#rt-rte-canon-admission]
      note: "Consolidation, revision, endorsement invalidation and promotion retain their local doctrine/affordance warrants; no novelty label or requested synthesis establishes a new claim."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Participant requests for thread context, preceding prose and chain metadata; page work requests for content and consensus"
          assessment: known
          findings:
            - value: pull
              basis: claimed
              records: [runtime.md#rt-rte-thread-participation, runtime.md#rt-rte-canon-admission]
              note: "External agents read retained files as part of requested participation or page review. File identity is not an unsolicited push selector."
          records: [runtime.md#rt-rte-thread-participation, runtime.md#rt-rte-canon-admission]
          note: "Both prescribed later-consumer routes are classified without claiming wired model delivery."
        - scope: "Caller-requested wiki audit followed by automatic filesystem selection for the checker"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-audit-invocation]
              note: "Caller requests checking the selected wiki root; requested report delivery is not a second push."
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-audit-invocation]
              note: "After root selection, fixed traversal automatically supplies retained file parts to audit checks without a separate request for each file."
          records: [runtime.md#rt-rte-audit-invocation]
          note: "The automatic supply reaches deterministic checks, not a model-context injector."
        - scope: "Profile later guidance, manifest loading, report/log and cemetery later readers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-profile-refinement, memory.md#mem-obj-anchor-form, memory.md#mem-rte-audit-retention, memory.md#mem-rte-page-withdrawal]
          note: "Intended guidance/availability does not specify a delivery mechanism; these alternatives cannot be removed from direction coverage."
      records: [runtime.md#rt-rte-thread-participation, runtime.md#rt-rte-canon-admission, runtime.md#rt-rte-audit-invocation, memory.md#mem-rte-profile-refinement, memory.md#mem-obj-anchor-form, memory.md#mem-rte-audit-retention, memory.md#mem-rte-page-withdrawal]
      note: "Requested agent reads and a requested/automatic audit chain coexist with unresolved later delivery of other retained surfaces."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Audit-triggered automatic selection of wiki Markdown and fixed dialogue metadata/entry paths"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-audit-invocation]
              note: "Audit invocation triggers broad wiki glob/fixed dialogue-root selection from caller-selected root, supplying file text and metadata to deterministic checks; no relevance or context budget is used."
          records: [runtime.md#rt-rte-audit-invocation]
          note: "File-type/root coverage is coarse, not an identity-matched model-memory injection."
        - scope: "Conditional cross-protocol audit checks of canon pointers already supplied in retained metadata"
          assessment: inapplicable
          findings: []
          records: [epistemic.md#epi-rte-cross-check, runtime.md#rt-rte-audit-invocation]
          note: "L3 checks referenced-path existence and field presence; it does not select and deliver retained canon-page parts. The consumed pointer arrives within the coarse-selected metadata covered above, so this existence predicate supplies no additional push signal."
        - scope: "Thread/page requested reads"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-thread-participation, runtime.md#rt-rte-canon-admission]
          note: "These direction units are requested pull reads, so their filenames do not establish push signals."
        - scope: "Profile, manifest and maintenance-history delivery alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-profile-refinement, memory.md#mem-obj-anchor-form, memory.md#mem-rte-audit-retention, memory.md#mem-rte-page-withdrawal]
          note: "Unknown delivery prevents determining whether push exists and which selector would supply it."
      records: [runtime.md#rt-rte-audit-invocation, epistemic.md#epi-rte-cross-check, runtime.md#rt-rte-thread-participation, runtime.md#rt-rte-canon-admission, memory.md#mem-rte-profile-refinement, memory.md#mem-obj-anchor-form, memory.md#mem-rte-audit-retention, memory.md#mem-rte-page-withdrawal]
      note: "Coarse automatic audit supply is supported; referenced-path existence checks add no targeted retained-content delivery. Unresolved external delivery alternatives prevent complete signal coverage."
    trace_learning:
      assessment: partial
      units:
        - scope: "Agent evaluation and closure-summary/checkpoint writes from retained discussion to later participants"
          assessment: known
          findings:
            - value: "yes"
              basis: claimed
              records: [memory.md#mem-obj-thread-entries, epistemic.md#epi-rte-peer-judgment, runtime.md#rt-rte-thread-participation]
              note: "Agent activity records feed per-content-unapproved agent evaluations and closing summaries/checkpoints, retained for next-axis decisions and reopen/continuation. This meets the trace-fed durable-artifact definition in doctrine, not wired operation or improved capacity."
          records: [memory.md#mem-obj-thread-entries, epistemic.md#epi-rte-peer-judgment, runtime.md#rt-rte-thread-participation]
          note: "The qualifying path is derived assessments/continuation context, not mere storage of raw contribution prose."
        - scope: "Orientation refinement and initial preferred-direction content"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-profile-refinement, epistemic.md#epi-obj-zhat]
          note: "Past-evaluation input and intended later guidance are specified, but automatic admission, writer and actual durable replacement are unresolved."
        - scope: "Canon production/admission, historical import, manifest maintenance, retained reports and cemetery history"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-canon-pages, runtime.md#rt-rte-canon-admission, epistemic.md#epi-rte-archival-import, memory.md#mem-obj-anchor-form, memory.md#mem-rte-audit-retention, memory.md#mem-rte-page-withdrawal]
          note: "Human canonical/identity recognition is not automatic learning. Earlier canon generation has unspecified transformation and later substantive use; import control and maintenance later consumers are unknown. No bounded record proves a negative across these alternatives."
      records: [memory.md#mem-obj-thread-entries, epistemic.md#epi-rte-peer-judgment, runtime.md#rt-rte-thread-participation, memory.md#mem-rte-profile-refinement, epistemic.md#epi-obj-zhat, memory.md#mem-obj-canon-pages, runtime.md#rt-rte-canon-admission, epistemic.md#epi-rte-archival-import, memory.md#mem-obj-anchor-form, memory.md#mem-rte-audit-retention, memory.md#mem-rte-page-withdrawal]
      note: "A prescribed qualifying agent transformation is positive; no shipped automatic writer establishes wiring, and other admission/consumer gaps remain local uncertainty rather than a system-wide no."
    trace_source:
      assessment: partial
      units:
        - scope: "Recorded conversational contributions feeding qualifying peer-evaluation and closure-summary/checkpoint writes"
          assessment: known
          findings:
            - value: session-logs
              basis: claimed
              records: [memory.md#mem-obj-thread-entries, epistemic.md#epi-rte-peer-judgment, runtime.md#rt-rte-thread-participation]
              note: "One agent contribution per dialogue round is retained, read and assessed by subsequent participants, and summarized at closure. These recorded conversational turns from agent work meet session-logs without requiring verbatim provider transcripts."
          records: [memory.md#mem-obj-thread-entries, epistemic.md#epi-rte-peer-judgment, runtime.md#rt-rte-thread-participation]
          note: "Known for the recorded conversational contribution input to the claimed qualifying write path; this does not classify additional original inputs or unresolved routes."
        - scope: "Potential orientation, canon, import and maintenance trace-fed alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-profile-refinement, memory.md#mem-obj-canon-pages, epistemic.md#epi-rte-archival-import, memory.md#mem-rte-audit-retention, memory.md#mem-rte-page-withdrawal, memory.md#mem-obj-anchor-form]
          note: "Qualifying automatic writes/later consumers are unresolved, and contribution vectors, current wiki diagnostics or generic deletion events alone do not establish original source categories for such a write."
      records: [memory.md#mem-obj-thread-entries, epistemic.md#epi-rte-peer-judgment, runtime.md#rt-rte-thread-participation, memory.md#mem-rte-profile-refinement, memory.md#mem-obj-canon-pages, epistemic.md#epi-rte-archival-import, memory.md#mem-rte-audit-retention, memory.md#mem-rte-page-withdrawal, memory.md#mem-obj-anchor-form]
      note: "Recorded conversational contributions establish a claimed session-logs source for the qualifying dialogue transformation. Additional original inputs and potential qualifying alternatives remain unresolved, so the axis is partial, not absent or inapplicable."
---

# LLM Wiki Coordination memory profile

## Comparison rationale

The comparison covers accumulated downstream wiki material, not every stored byte in the package. [MEM-OBJ-thread-context](memory.md#mem-obj-thread-context), [MEM-OBJ-thread-meta](memory.md#mem-obj-thread-meta), [MEM-OBJ-thread-entries](memory.md#mem-obj-thread-entries), [MEM-OBJ-canon-pages](memory.md#mem-obj-canon-pages), [MEM-OBJ-consensus-block](memory.md#mem-obj-consensus-block), [MEM-OBJ-anchor-form](memory.md#mem-obj-anchor-form), [MEM-OBJ-audit-reports](memory.md#mem-obj-audit-reports) and [MEM-OBJ-cemetery-log](memory.md#mem-obj-cemetery-log) supply the retained inventory. Static shipped instructions and per-audit transient caches/results are excluded; [RT-CMP-generic-wiki-audit](runtime.md#rt-cmp-generic-wiki-audit) and its memory annotation distinguish those from durable state. External model parameters are not an included provider-memory alternative because no target route retains or updates them: [RT-CMP-agent-substrate](runtime.md#rt-cmp-agent-substrate), [RT-ABS-runtime-orchestration](runtime.md#rt-abs-runtime-orchestration).

Known file storage means that the prescribed objects have a complete substrate classification. It does not mean an adopting wiki was observed. Most other positives are doctrine or afforded design. The implemented checker establishes symbolic consumption and automatic selection, not deployed agent compliance. [RT-RTE-audit-invocation](runtime.md#rt-rte-audit-invocation) is both an overall requested audit and an automatic file-selection chain. Its requested report return remains pull; supplying glob-selected wiki material to individual checks is coarse push. [EPI-RTE-cross-check](epistemic.md#epi-rte-cross-check) consumes pointers within already selected metadata and checks target existence; it does not supply retained parts of the referenced page to a later consumer. The pointer's delivery is covered by coarse metadata selection, not an additional identifier-based push finding.

Admission differs by mechanism. Agents append entries, scores and summaries without human approval of each item. User recognition controls closing acceptance and canonical promotion separately. Thus automatic authoring and manual promotion coexist rather than giving the entire page lifecycle one agency value: [MEM-OBJ-thread-entries](memory.md#mem-obj-thread-entries), [RT-RTE-canon-admission](runtime.md#rt-rte-canon-admission). Generic adopter/deletion operator labels and an unspecified profile writer do not resolve other admission choices. Canon agreement criteria and stale/disputed vetoes retain claimed validation/enforcement force, while [RT-CLM-canon-enforcement](runtime.md#rt-clm-canon-enforcement) prevents upgrading them to an implemented gate.

Curation is classified by the recorded change. Closure reduces discussion into a summary/checkpoint; canon promotion changes tier; edits revise pages; stale/dispute handling changes current endorsement reliance. The canon filename and the description of synthesis do not establish a proposition absent from the inputs. [MEM-OBJ-canon-pages](memory.md#mem-obj-canon-pages) leaves that semantic transformation unresolved. Historical wrapping is acquisition, not consolidation: [EPI-RTE-archival-import](epistemic.md#epi-rte-archival-import).

The trace-learning positive is deliberately local and claimed. Prior agent work feeds durable peer assessments and closing continuation material, which subsequent participants consume in direction choice or reopening: [MEM-OBJ-thread-entries](memory.md#mem-obj-thread-entries), [EPI-RTE-peer-judgment](epistemic.md#epi-rte-peer-judgment), [RT-RTE-thread-participation](runtime.md#rt-rte-thread-participation). No automatic writer is shipped, so this is not wired learning. Nor does it establish the separate improved-capacity property. The recorded dialogue contributions are conversational turns from agent work and therefore support a claimed session-logs source on this same qualifying path. Their distinction from verbatim provider transcripts does not exclude that category. Additional original inputs and other potential qualifying routes retain not-determinable coverage; no tool-traces, event-streams or trajectories finding is inferred merely from numbered files or timestamps.

Supersessions affect identity but do not strengthen evidence. Citations use [MEM-OBJ-anchor-form](memory.md#mem-obj-anchor-form), [MEM-OBJ-consensus-block](memory.md#mem-obj-consensus-block) and [MEM-RTE-profile-refinement](memory.md#mem-rte-profile-refinement) as the canonical referents replacing their epistemic duplicates. The reconciliation retains a disagreement over whether orientation refinement's doctrine status is afforded or claimed. The profile keeps the memory formula's local afforded witness and the conflict beside it; it makes no system-wide strongest-status substitution. [EPI-OBJ-zhat](epistemic.md#epi-obj-zhat) remains a distinct operative part, not a superseded producer. Its unspecified initial provenance, writer, admission and delivery prevent complete lineage, agency and trace-learning classification. Missing report/tombstone readers and manifest reconstruction similarly remain included uncertainty.

Source-read log: none. This profile uses only the supplied accepted members and reconciliation; it adds no source facts, quotations or records.
