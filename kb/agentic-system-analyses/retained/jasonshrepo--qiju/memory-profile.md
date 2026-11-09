---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Qiju memory comparison: intentional session history, file-tier retrieval and optional user-authorized retrospective guidance."
run-id: "AAS-2026-11-08-qiju-1a12c31c13d1-01"
source-identity: "https://github.com/jasonshrepo/qiju"
reviewed-boundary: "a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89"
memory-comparison:
  version: 2
  scope: "Use-written session records and their narrative, action, descriptor, addressing, substitution and opaque extra fields; file-tier access, import, maintenance, scrub and purge; retained audit/recovery copies; and optional use-revised installed guidance. Static bundled instructions, transient staging as a history tier, external host conversation management, platform memories and provider parameters are excluded. Staging is considered only as an admission input; static skills only establish the supplied procedures. Initial legacy/caller provenance and later modified-skill loading remain unresolved."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        -
          scope: "Retained record fields, arbitrary extra fields and project-address marker"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-body-md"
                - "memory.md#mem-obj-address-metadata"
                - "memory.md#mem-obj-redaction-metadata"
              note: "JSONL and monthly Parquet are local files; JSON and Parquet are encodings, not distinct storage substrates."
          records:
            - "memory.md#mem-obj-body-md"
            - "memory.md#mem-obj-next-steps"
            - "memory.md#mem-obj-search-descriptors"
            - "memory.md#mem-obj-address-metadata"
            - "memory.md#mem-obj-redaction-metadata"
          note: "All admitted fields share the file tiers, including opaque caller extras. The marker is a local configuration file."
        -
          scope: "Redaction audit and source/skill recovery copies"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-redaction-log"
                - "runtime.md#rt-rte-store-migration"
                - "runtime.md#rt-rte-skill-install"
              note: "Audit JSONL, preserved migration sources and timestamped skill backups remain filesystem objects."
          records:
            - "memory.md#mem-obj-redaction-log"
            - "runtime.md#rt-rte-store-migration"
            - "runtime.md#rt-rte-skill-install"
          note: "No supplied normal later consumer for audit or backups; retention is known independently of read-back."
        -
          scope: "Optional use-revised installed guidance"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "afforded"
              records:
                - "runtime.md#rt-obj-qiju-skills"
                - "runtime.md#rt-rte-skill-review"
              note: "User-requested retrospective edits target installed skill files."
          records:
            - "runtime.md#rt-obj-qiju-skills"
            - "runtime.md#rt-rte-skill-review"
          note: "Includes only the potential use-revised artifact, not unchanged bundled instructions."
      records:
        - "memory.md#mem-obj-body-md"
        - "memory.md#mem-obj-next-steps"
        - "memory.md#mem-obj-search-descriptors"
        - "memory.md#mem-obj-address-metadata"
        - "memory.md#mem-obj-redaction-metadata"
        - "memory.md#mem-obj-redaction-log"
        - "runtime.md#rt-rte-store-migration"
        - "runtime.md#rt-rte-skill-install"
        - "runtime.md#rt-obj-qiju-skills"
        - "runtime.md#rt-rte-skill-review"
      note: "The recorded memory objects use files. External provider/platform memory is outside this inventory, not an opaque Qiju storage branch. Staging is transient input, not another history tier."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Narrative, plans and descriptors interpreted by an answering or reviewing host"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-body-md"
                - "memory.md#mem-obj-next-steps"
                - "memory.md#mem-obj-search-descriptors"
                - "memory.md#mem-bap-record-history"
              note: "Retrieved Markdown, action strings and authored titles supply interpreted history or advice."
          records:
            - "memory.md#mem-obj-body-md"
            - "memory.md#mem-obj-next-steps"
            - "memory.md#mem-obj-search-descriptors"
            - "memory.md#mem-bap-record-history"
          note: "Code snippets and anchors embedded in narrative do not make the whole narrative an executable symbolic theory."
        -
          scope: "Record addressing, tags and other fixed-rule metadata consumption"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-address-metadata"
                - "memory.md#mem-obj-search-descriptors"
                - "memory.md#mem-obj-redaction-metadata"
                - "runtime.md#rt-rte-record-retrieval"
              note: "IDs, dates, tags and field structures meet fixed matching, ordering and serialization rules."
          records:
            - "memory.md#mem-obj-address-metadata"
            - "memory.md#mem-obj-search-descriptors"
            - "memory.md#mem-obj-redaction-metadata"
            - "runtime.md#rt-rte-record-retrieval"
          note: "Includes symbolic use of descriptors, separate from their natural-language display."
        -
          scope: "Audit events and caller reason"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-redaction-log"
              note: "Event dictionaries carry counts, paths and timestamps."
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-redaction-log"
              note: "Caller-supplied reason/replacement strings are retained as text."
          records:
            - "memory.md#mem-obj-redaction-log"
          note: "No automatic later interpretation of the audit reason is established."
        -
          scope: "Optional applied retrospective guidance"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-review"
                - "runtime.md#rt-obj-qiju-skills"
              note: "Copy-ready method wording can be applied to installed skills and interpreted later by a host."
          records:
            - "runtime.md#rt-rte-skill-review"
            - "runtime.md#rt-obj-qiju-skills"
          note: "Actual applied wording and loading are unobserved."
        -
          scope: "Arbitrary extra payloads and initial legacy contents"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-address-metadata"
            - "runtime.md#rt-rte-store-migration"
          note: "Admission preserves unknown keys and imports legacy content; no retained instances establish their content encoding or interpretation."
      records:
        - "memory.md#mem-obj-body-md"
        - "memory.md#mem-obj-next-steps"
        - "memory.md#mem-obj-search-descriptors"
        - "memory.md#mem-bap-record-history"
        - "memory.md#mem-obj-address-metadata"
        - "memory.md#mem-obj-redaction-metadata"
        - "runtime.md#rt-rte-record-retrieval"
        - "memory.md#mem-obj-redaction-log"
        - "runtime.md#rt-rte-skill-review"
        - "runtime.md#rt-obj-qiju-skills"
        - "runtime.md#rt-rte-store-migration"
      note: "Known text and symbolic parts coexist with unclassified extra/imported payloads; no distributed-parametric memory value follows from the external host model."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Shipped host-composed checkpoint history and plans"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-body-md"
                - "runtime.md#rt-rte-record-capture"
              note: "The log procedure asks a host to select process history, decisions and agreed plans from its current work session."
            -
              value: "authored"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-body-md"
                - "memory.md#mem-obj-next-steps"
                - "memory.md#mem-obj-search-descriptors"
                - "runtime.md#rt-rte-record-capture"
              note: "The host composes intentional narrative, titles and plans rather than Qiju automatically copying a transcript."
          records:
            - "memory.md#mem-obj-body-md"
            - "memory.md#mem-obj-next-steps"
            - "memory.md#mem-obj-search-descriptors"
            - "runtime.md#rt-rte-record-capture"
          note: "These are requested derivation paths, not observed production; authorship does not authenticate the session account."
        -
          scope: "Capture-generated addressing and redaction metadata; scrub audit"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-address-metadata"
                - "memory.md#mem-obj-redaction-metadata"
                - "memory.md#mem-obj-redaction-log"
                - "runtime.md#rt-rte-record-capture"
              note: "Code supplies defaults/IDs, repairs timestamps and constructs substitution/audit metadata."
          records:
            - "memory.md#mem-obj-address-metadata"
            - "memory.md#mem-obj-redaction-metadata"
            - "memory.md#mem-obj-redaction-log"
            - "runtime.md#rt-rte-record-capture"
          note: "This classifies generated parts only, not the initial provenance of caller-provided fields."
        -
          scope: "Legacy records entering the Qiju store"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-store-migration"
              note: "Legacy file content is copied/merged and rebranded into the Qiju store."
          records:
            - "runtime.md#rt-rte-store-migration"
            - "memory.md#mem-obj-address-metadata"
          note: "Import is known; original authorship, trace derivation and caller extras remain unresolved."
        -
          scope: "Direct caller input and preexisting metadata"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-body-md"
            - "memory.md#mem-obj-address-metadata"
            - "memory.md#mem-obj-redaction-metadata"
          note: "Labels manual/agent and model strings do not establish original provenance; preexisting redaction dictionaries can be supplied."
        -
          scope: "Retrospective method revision"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-review"
                - "runtime.md#rt-obj-qiju-skills"
              note: "Review asks for lessons and proposed wording from retained session narratives, with application only on request."
          records:
            - "runtime.md#rt-rte-skill-review"
            - "runtime.md#rt-obj-qiju-skills"
          note: "The afforded trace-derived edit is distinct from package-body replacement, which is excluded as static shipped text."
      records:
        - "memory.md#mem-obj-body-md"
        - "memory.md#mem-obj-next-steps"
        - "memory.md#mem-obj-search-descriptors"
        - "runtime.md#rt-rte-record-capture"
        - "memory.md#mem-obj-address-metadata"
        - "memory.md#mem-obj-redaction-metadata"
        - "memory.md#mem-obj-redaction-log"
        - "runtime.md#rt-rte-store-migration"
        - "runtime.md#rt-rte-skill-review"
        - "runtime.md#rt-obj-qiju-skills"
      note: "Derivation and import positives do not resolve initial legacy/caller provenance. No source labels are treated as provenance authentication."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Retrieved process history and displayed metadata at answering host"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-bap-record-history"
                - "memory.md#mem-obj-body-md"
                - "memory.md#mem-obj-search-descriptors"
                - "runtime.md#rt-rte-record-retrieval"
              note: "CLI output supplies history/reference context; source-of-truth treatment is requested, not factual verification."
          records:
            - "memory.md#mem-bap-record-history"
            - "memory.md#mem-obj-body-md"
            - "memory.md#mem-obj-search-descriptors"
            - "runtime.md#rt-rte-record-retrieval"
          note: "Delivery is wired; host reliance and compliance are unobserved."
        -
          scope: "Retained action text at host planning consumer"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-next-steps"
                - "epistemic.md#epi-rte-action-rollup"
              note: "Agreed next-step imperatives can guide resumed work; the unchecked checklist does not establish completion status."
          records:
            - "memory.md#mem-obj-next-steps"
            - "epistemic.md#epi-rte-action-rollup"
          note: "Instructional force is afforded by the plans, not an executable task scheduler."
        -
          scope: "Retained timestamps, project and identity at fixed retrieval/maintenance consumers"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-address-metadata"
                - "runtime.md#rt-rte-record-retrieval"
              note: "Timestamp and chosen sorting determine relative order before limit."
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-address-metadata"
                - "runtime.md#rt-rte-record-retrieval"
                - "runtime.md#rt-rte-store-maintenance"
              note: "Project/session metadata and dates select scope and retained input sets."
          records:
            - "memory.md#mem-obj-address-metadata"
            - "runtime.md#rt-rte-record-retrieval"
            - "runtime.md#rt-rte-store-maintenance"
          note: "Literal keyword filtering alone is not semantic ranking; these findings name actual ordering and scope effects."
        -
          scope: "Retained ID inventory at admission and archive checks"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-record-capture"
                - "runtime.md#rt-rte-store-maintenance"
              note: "Existing IDs and expected archive ID sets determine copy admissibility or archive agreement."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-record-capture"
                - "runtime.md#rt-rte-store-maintenance"
              note: "Existing-tier IDs skip append, archived IDs return early, and failed archive validation prevents replacement."
          records:
            - "runtime.md#rt-rte-record-capture"
            - "runtime.md#rt-rte-store-maintenance"
          note: "These fixed controls have operational force, not historical-truth authority."
        -
          scope: "History at retrospective update consumer and potential revised guidance at later host"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-review"
                - "memory.md#mem-obj-body-md"
              note: "Retained experience can feed proposed durable method changes even though application is user-authorized."
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-review"
                - "runtime.md#rt-obj-qiju-skills"
              note: "An applied method revision can supply standing directions on later skill loading."
          records:
            - "runtime.md#rt-rte-skill-review"
            - "memory.md#mem-obj-body-md"
            - "runtime.md#rt-obj-qiju-skills"
          note: "Update authority and output authority are separate; neither implies automatic trace learning or improved capacity."
        -
          scope: "Unconsumed redaction audit/metadata and backups"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-obj-redaction-log"
            - "memory.md#mem-obj-redaction-metadata"
            - "runtime.md#rt-rte-store-migration"
            - "runtime.md#rt-rte-skill-install"
          note: "Normal retrieval has no audit-reason consumer or decision gate over redaction metadata; no automatic recovery-copy consumer is supplied. Mere retention gives no force."
        -
          scope: "Opaque extra fields and imported content at later consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-address-metadata"
            - "runtime.md#rt-rte-store-migration"
            - "runtime.md#rt-rte-record-retrieval"
          note: "Full JSON can expose extras, but their meaning, use and any additional authority are unspecified."
      records:
        - "memory.md#mem-bap-record-history"
        - "memory.md#mem-obj-body-md"
        - "memory.md#mem-obj-search-descriptors"
        - "runtime.md#rt-rte-record-retrieval"
        - "memory.md#mem-obj-next-steps"
        - "epistemic.md#epi-rte-action-rollup"
        - "memory.md#mem-obj-address-metadata"
        - "runtime.md#rt-rte-store-maintenance"
        - "runtime.md#rt-rte-record-capture"
        - "runtime.md#rt-rte-skill-review"
        - "runtime.md#rt-obj-qiju-skills"
        - "memory.md#mem-obj-redaction-log"
        - "memory.md#mem-obj-redaction-metadata"
        - "runtime.md#rt-rte-store-migration"
        - "runtime.md#rt-rte-skill-install"
      note: "The actual consumer controls classification. Known routing, ordering, controls and informational paths do not classify every possible extra/imported payload."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Shipped model-authored checkpoint admission and automatic capture transformations"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-record-capture"
                - "epistemic.md#epi-rte-shape-admission"
              note: "Code admits normalized/redacted content without per-record human approval; a checkpoint request is only a trigger."
          records:
            - "runtime.md#rt-rte-record-capture"
            - "epistemic.md#epi-rte-shape-admission"
          note: "This covers admission, not proof that a host complied with composition instructions."
        -
          scope: "Maintenance, scrub, migration and purge admissions"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-store-maintenance"
                - "runtime.md#rt-rte-privacy-repair"
                - "runtime.md#rt-rte-store-migration"
                - "epistemic.md#epi-rte-store-withdrawal"
              note: "Once invoked, fixed code selects moves, matches, rewrites and deletion without per-occurrence approval."
          records:
            - "runtime.md#rt-rte-store-maintenance"
            - "runtime.md#rt-rte-privacy-repair"
            - "runtime.md#rt-rte-store-migration"
            - "epistemic.md#epi-rte-store-withdrawal"
          note: "Caller selection of a mode or literal does not make every subsequent admission manual."
        -
          scope: "Optional application of retrospective skill revisions"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-review"
                - "runtime.md#rt-obj-qiju-skills"
              note: "The policy requires an explicit user request before applying proposed targeted edits."
          records:
            - "runtime.md#rt-rte-skill-review"
            - "runtime.md#rt-obj-qiju-skills"
          note: "This is host policy, not a software veto or observed edit."
        -
          scope: "Initial direct-caller content and legacy-source admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-body-md"
            - "memory.md#mem-obj-address-metadata"
            - "runtime.md#rt-rte-store-migration"
          note: "Generic caller identity does not establish whether a human supplied, edited or approved retained content before the known software transformations."
      records:
        - "runtime.md#rt-rte-record-capture"
        - "epistemic.md#epi-rte-shape-admission"
        - "runtime.md#rt-rte-store-maintenance"
        - "runtime.md#rt-rte-privacy-repair"
        - "runtime.md#rt-rte-store-migration"
        - "epistemic.md#epi-rte-store-withdrawal"
        - "runtime.md#rt-rte-skill-review"
        - "runtime.md#rt-obj-qiju-skills"
        - "memory.md#mem-obj-body-md"
        - "memory.md#mem-obj-address-metadata"
      note: "Known software admission remains separate from unresolved initial human control and from the retrospective's explicit application decision."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Requested session-to-checkpoint composition"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-body-md"
                - "runtime.md#rt-rte-record-capture"
              note: "The host is asked to retain selected process history and reasons rather than duplicate the entire session or artifact contents."
          records:
            - "memory.md#mem-obj-body-md"
            - "runtime.md#rt-rte-record-capture"
          note: "Classifies requested selection/compression, not an observed faithful summary or synthesis of new claims."
        -
          scope: "Actions presentation over retained plans"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "wired"
              records:
                - "memory.md#mem-obj-next-steps"
                - "epistemic.md#epi-rte-action-rollup"
              note: "Whitespace/casefold keys remove duplicate action strings in the returned rollup."
          records:
            - "memory.md#mem-obj-next-steps"
            - "epistemic.md#epi-rte-action-rollup"
          note: "Dedup is a read-side view transformation, not a persistent rewrite or semantic completion reconciliation."
        -
          scope: "Literal scrub and fixed migration rewrites of retained records"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-privacy-repair"
                - "runtime.md#rt-rte-store-migration"
              note: "Scrub replaces retained strings; migration changes addressing and rebrands string content."
            -
              value: "dedup"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-store-migration"
              note: "Identity repair/import merges records by ID."
          records:
            - "runtime.md#rt-rte-privacy-repair"
            - "runtime.md#rt-rte-store-migration"
          note: "Rebranding and redaction may alter meaning; neither establishes synthesis of a new warranted claim. Capture collision checks alone are excluded."
        -
          scope: "Explicit durable-store deletion"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-store-withdrawal"
              note: "Purge forgets long/archive content by deleting directories."
          records:
            - "epistemic.md#epi-rte-store-withdrawal"
          note: "Administrative deletion is bounded to those copies, not universal forgetting. Short rotation/archive movement alone do not establish decay."
        -
          scope: "Potential retrospective rewrite of installed guidance"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-review"
                - "runtime.md#rt-obj-qiju-skills"
              note: "User-requested targeted edits can revise existing standing guidance."
          records:
            - "runtime.md#rt-rte-skill-review"
            - "runtime.md#rt-obj-qiju-skills"
          note: "Recommendation generation alone is not retained curation; application is an afforded step."
        -
          scope: "Unspecified direct/imported meanings and actual review outputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-address-metadata"
            - "runtime.md#rt-rte-store-migration"
            - "runtime.md#rt-rte-skill-review"
          note: "No instances establish whether other semantic operations, including synthesis, occur. Detailed normalization helpers and actual diagnosed claims are unresolved."
      records:
        - "memory.md#mem-obj-body-md"
        - "runtime.md#rt-rte-record-capture"
        - "memory.md#mem-obj-next-steps"
        - "epistemic.md#epi-rte-action-rollup"
        - "runtime.md#rt-rte-privacy-repair"
        - "runtime.md#rt-rte-store-migration"
        - "epistemic.md#epi-rte-store-withdrawal"
        - "runtime.md#rt-rte-skill-review"
        - "runtime.md#rt-obj-qiju-skills"
        - "memory.md#mem-obj-address-metadata"
      note: "Implemented local transformations coexist with semantic uncertainty. Tier movement/Parquet encoding is not consolidation; no promote or invalidate follows merely from storage movement."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Normal record search, exact-ID hydration and retrospective evidence requests"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-record-retrieval"
                - "memory.md#mem-bap-record-history"
              note: "The host requests retained records; fixed filtering and stdout fulfillment are parts of the requested route."
          records:
            - "runtime.md#rt-rte-record-retrieval"
            - "memory.md#mem-bap-record-history"
            - "runtime.md#rt-rte-skill-review"
          note: "No additional push is created by automatically applying query predicates or by returning CLI output."
        -
          scope: "Audit, staging and backup retention"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-obj-redaction-log"
            - "memory.md#mem-obj-staging-record"
            - "runtime.md#rt-rte-store-migration"
            - "runtime.md#rt-rte-skill-install"
          note: "No particular later history consumer is supplied; a hypothetical file reader is not a read-back route."
        -
          scope: "Optional use-revised skill discovery/loading"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-skill-review"
            - "runtime.md#rt-obj-qiju-skills"
          note: "Applied edits could later be loaded, but no supplied consumer request or host injection mechanics resolves direction for the modified artifact."
      records:
        - "runtime.md#rt-rte-record-retrieval"
        - "memory.md#mem-bap-record-history"
        - "runtime.md#rt-rte-skill-review"
        - "memory.md#mem-obj-redaction-log"
        - "memory.md#mem-obj-staging-record"
        - "runtime.md#rt-rte-store-migration"
        - "runtime.md#rt-rte-skill-install"
        - "runtime.md#rt-obj-qiju-skills"
      note: "Known record pull is supported, but optional revised-skill loading remains unresolved; the inventory therefore cannot establish pull-only read-back."
    read_back_signal:
      assessment: "not-determinable"
      units:
        -
          scope: "Requested record retrieval"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-record-retrieval"
          note: "Pull fulfillment has no push selector to classify; an exact requested ID is not identifier-based push."
        -
          scope: "Optional use-revised skill loading"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-skill-review"
            - "runtime.md#rt-obj-qiju-skills"
          note: "No trigger, selector input and selected modified payload are supplied for a later host injection. Static skill-discovery metadata cannot classify this route."
        -
          scope: "Audit and recovery copies"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-obj-redaction-log"
            - "runtime.md#rt-rte-store-migration"
            - "runtime.md#rt-rte-skill-install"
          note: "No supplied later consumption route, hence no classified push selection."
      records:
        - "runtime.md#rt-rte-record-retrieval"
        - "runtime.md#rt-rte-skill-review"
        - "runtime.md#rt-obj-qiju-skills"
        - "memory.md#mem-obj-redaction-log"
        - "runtime.md#rt-rte-store-migration"
        - "runtime.md#rt-rte-skill-install"
      note: "No supported push signal is established. The unresolved revised-guidance route prevents declaring the entire memory boundary pull-only or this axis wholly inapplicable."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Host-composed session checkpoint to retained process history to later answering host"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-record-capture"
                - "memory.md#mem-obj-body-md"
                - "memory.md#mem-bap-record-history"
              note: "The requested host computation selects session experience into a durable account, software admits it without per-content human approval, and later retrieval supplies context."
          records:
            - "runtime.md#rt-rte-record-capture"
            - "memory.md#mem-obj-body-md"
            - "memory.md#mem-bap-record-history"
          note: "This satisfies the trace-fed behavior-shaping artifact route at affordance strength, not observed execution, faithful capture or benefit."
        -
          scope: "Generic caller and legacy input alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-address-metadata"
            - "memory.md#mem-obj-body-md"
            - "runtime.md#rt-rte-store-migration"
          note: "Input may be arbitrary or mixed; labels do not establish trace origin or automatic original derivation."
        -
          scope: "Retrospective recommendation and user-authorized method edits"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-skill-review"
            - "runtime.md#rt-obj-qiju-skills"
          note: "Proposals have no wired retention; application requires an explicit user decision. This manual admission is not a qualifying automatic trace-fed guidance write."
        -
          scope: "Audit retention and placement-only maintenance"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-obj-redaction-log"
            - "runtime.md#rt-rte-store-maintenance"
          note: "Audit has no supplied later behavior-shaping consumer; copy movement alone creates no derived behavioral artifact."
      records:
        - "runtime.md#rt-rte-record-capture"
        - "memory.md#mem-obj-body-md"
        - "memory.md#mem-bap-record-history"
        - "memory.md#mem-obj-address-metadata"
        - "runtime.md#rt-rte-store-migration"
        - "runtime.md#rt-rte-skill-review"
        - "runtime.md#rt-obj-qiju-skills"
        - "memory.md#mem-obj-redaction-log"
        - "runtime.md#rt-rte-store-maintenance"
      note: "A supported afforded yes coexists with unresolved alternative inputs. No local no is asserted: the set declares no bounded-absence record establishing an entire negative learning unit."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Conversational work-session input to requested checkpoint composition"
          assessment: "partial"
          findings:
            -
              value: "session-logs"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-record-capture"
                - "memory.md#mem-obj-body-md"
              note: "The instructed host records what was done, decided and agreed in its current work session; this supports conversational session material on the requested route."
          records:
            - "runtime.md#rt-rte-record-capture"
            - "memory.md#mem-obj-body-md"
            - "memory.md#mem-obj-address-metadata"
          note: "The host-selected input can be mixed. No raw transcript or original tool/event payload is supplied, preventing complete source enumeration."
        -
          scope: "Generic caller and imported original material"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-address-metadata"
            - "runtime.md#rt-rte-store-migration"
            - "memory.md#mem-obj-body-md"
          note: "Manual/agent labels and legacy wrapping cannot distinguish conversational records, tool results, events or other content."
        -
          scope: "Manual retrospective guidance application and audit/placement-only operations"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-skill-review"
            - "memory.md#mem-obj-redaction-log"
            - "runtime.md#rt-rte-store-maintenance"
          note: "These are not qualifying automatic trace-fed writes in this profile, irrespective of the review's experience-based evidence."
      records:
        - "runtime.md#rt-rte-record-capture"
        - "memory.md#mem-obj-body-md"
        - "memory.md#mem-obj-address-metadata"
        - "runtime.md#rt-rte-store-migration"
        - "runtime.md#rt-rte-skill-review"
        - "memory.md#mem-obj-redaction-log"
        - "runtime.md#rt-rte-store-maintenance"
      note: "Session material is supported at the requested-route layer only. No tool-traces, event-streams or trajectories are inferred from process-history labels, timestamps or ordinary tool use."
---

# Qiju memory profile

## Comparison rationale

The comparison classifies retained memory and actual consumer paths, not the CLI's entire filesystem capability. [MEM-OBJ-body-md](memory.md#mem-obj-body-md), [MEM-OBJ-next-steps](memory.md#mem-obj-next-steps), [MEM-OBJ-search-descriptors](memory.md#mem-obj-search-descriptors), [MEM-OBJ-address-metadata](memory.md#mem-obj-address-metadata) and [MEM-OBJ-redaction-metadata](memory.md#mem-obj-redaction-metadata) separate fields that share storage but differ in meaning and fixed-rule use. Unknown extra keys share file storage without acquiring a known semantic form, lineage or authority. Initial legacy provenance remains unresolved despite a known import mechanism in [RT-RTE-store-migration](runtime.md#rt-rte-store-migration).

Reconciliation supersedes the epistemic body_md and next_steps object declarations with the memory declarations cited here. It retains the epistemic metadata aggregate alongside the differentiated memory objects. Neither identity resolution upgrades evidence strength; the action-rendering route [EPI-RTE-action-rollup](epistemic.md#epi-rte-action-rollup) remains distinct from its retained input.

Record text supplies knowledge through [MEM-BAP-record-history](memory.md#mem-bap-record-history). Retained next-step imperatives can guide work, but the checklist neither executes tasks nor verifies that they remain open. Fixed metadata supports ranking through timestamp ordering and routing through project/session/date selection. Existing retained IDs supply validation and enforcement at capture and archive checks, rather than a factual warrant for narrative claims ([RT-RTE-record-capture](runtime.md#rt-rte-record-capture), [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance)). Static schema criteria and the bundled trust instruction are not counted as use-written memory.

Checkpoint composition is trace-derived at the afforded host-procedure layer. The requested host operation selects session experience into a persistent record admitted without per-content human approval and later delivered as context. Thus trace_learning has an afforded yes, not an observed or beneficial learning claim. Qiju does not itself acquire a transcript; direct caller and legacy alternatives leave provenance and the complete trace-source inventory unresolved ([MEM-OBJ-body-md](memory.md#mem-obj-body-md), [RT-RTE-record-capture](runtime.md#rt-rte-record-capture)). Conversational session material supports the local session-logs finding; references to work or tools do not establish separate tool-traces or trajectories. No evidenced-absence record supports a local no.

The retrospective has a different admission boundary. Retained experience can have learning authority at the method-update consumer, while an applied output can have instruction authority at a later host. Explicit user authorization makes that application manual at affordance strength; it is not another automatic trace_learning yes. Recommendations alone have no supplied durable queue, and modified guidance's later loading remains unspecified. Direct package refresh is not a retrospective-result consumer and can overwrite local changes ([RT-RTE-skill-review](runtime.md#rt-rte-skill-review), [RT-OBJ-qiju-skills](runtime.md#rt-obj-qiju-skills), [RT-RTE-skill-install](runtime.md#rt-rte-skill-install)).

Requested checkpoint selection supports consolidation only at the afforded layer. Actions deduplication is a wired view over retained plans, not a persistent plan-state resolver. Scrub and migration implement retained revision; explicit purge implements bounded forgetting. Rotation and Parquet movement alone are not decay or semantic consolidation, and faithful compression cannot be presumed from archive row/ID checks ([MEM-OBJ-next-steps](memory.md#mem-obj-next-steps), [RT-RTE-privacy-repair](runtime.md#rt-rte-privacy-repair), [RT-RTE-store-migration](runtime.md#rt-rte-store-migration), [EPI-RTE-store-withdrawal](epistemic.md#epi-rte-store-withdrawal)). Actual review outputs and imported meanings do not support stronger synthesis findings.

Search/show is pull, including automatic filtering and stdout delivery in fulfillment of the host's request. Exact-ID hydration does not establish identifier-based push. The two-phase manifest is output shaping, not host compaction. Optional modified-skill discovery remains unresolved, so the whole read-back boundary cannot be classified pull-only and read_back_signal cannot be globally inapplicable ([RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval), [RT-RTE-skill-review](runtime.md#rt-rte-skill-review)).

No source files were read for this mapping: the accepted records and reconciliation supplied all warrants. Findings remain implementation wiring or afforded procedures; none is upgraded to observed operation or causal support. No records were declared, added or amended.
