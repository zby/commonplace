---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Playground memory comparison: accumulated tenant files, bounded job replay, opaque native
  piles, maintenance and unwired summary-cover doctrine.'
run-id: AAS-2026-10-14-playground-88ee8a292f9b-01
source-identity: https://github.com/triblespace/playground
reviewed-boundary: de28ac8fdda30c7a5c2ee099de089e65a685195f
memory-comparison:
  version: 2
  scope: Includes use-accumulated workspace files and subsequently modified profiles; retained job output/access
    state; self/shared pile content and opaque native-worker alternatives; standalone timestamp, wiki
    and telemetry retained material; and separately labelled summary/cover doctrine. Excludes initial
    static profiles and shipped prompts as retained memory, signer keys, credentials, worker mappings,
    bundle caches and transport-session machinery, as well as external model weights and excluded archive-import
    execution. Declared context mechanisms are compared only at their local claimed/afforded basis, never
    as current provider wiring.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Accumulated workspace files, subsequently modified profiles, self/shared piles and standalone
          script input/output piles
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-workspace-files
          - memory.md#mem-obj-session-profile
          - memory.md#mem-obj-self-pile
          - memory.md#mem-obj-shared-pile
          - epistemic.md#epi-obj-timestamp-tribles
          - epistemic.md#epi-obj-wiki-fragments
          - epistemic.md#epi-obj-telemetry-spans
          note: Workspace disks, profile files and persistent native pile files hold these parts.
        records:
        - memory.md#mem-obj-workspace-files
        - memory.md#mem-obj-session-profile
        - memory.md#mem-obj-self-pile
        - memory.md#mem-obj-shared-pile
        - epistemic.md#epi-obj-timestamp-tribles
        - epistemic.md#epi-obj-wiki-fragments
        - epistemic.md#epi-obj-telemetry-spans
        note: The records identify filesystem storage, including opaque pile bytes. Native encoding is
          not another established substrate.
      - scope: Retained job output and accumulated polling/terminal-observation metadata
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-output-log
          - memory.md#mem-obj-job-snapshot
          - runtime.md#rt-rte-retained-jobs
          note: The manager retains chunks and handle state in process RAM and loses them at restart.
        records:
        - memory.md#mem-obj-output-log
        - memory.md#mem-obj-job-snapshot
        - runtime.md#rt-rte-retained-jobs
        note: Retention is bounded to the same daemon; delivered JSON is not a separate durable substrate.
      - scope: Documented summary/cognition/archive branch storage
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-clm-memory-cover
        note: Branch and blob descriptions do not establish a controlled storage substrate for the unwired
          context system.
      - scope: Additional retained state inside the native worker
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-worker-forward
        - memory.md#mem-obj-self-pile
        note: The fixed mounted pile is covered separately. The external implementation prevents enumeration
          of other operative storage.
      records:
      - memory.md#mem-obj-workspace-files
      - memory.md#mem-obj-session-profile
      - memory.md#mem-obj-self-pile
      - memory.md#mem-obj-shared-pile
      - epistemic.md#epi-obj-timestamp-tribles
      - epistemic.md#epi-obj-wiki-fragments
      - epistemic.md#epi-obj-telemetry-spans
      - memory.md#mem-obj-output-log
      - memory.md#mem-obj-job-snapshot
      - runtime.md#rt-rte-retained-jobs
      - memory.md#mem-clm-memory-cover
      - runtime.md#rt-rte-worker-forward
      note: Files and RAM are established for the inspected retained inventory. Additional native-worker
        retained state is opaque; file custody does not enumerate that state.
    representational_form:
      assessment: partial
      units:
      - scope: Workspace prose through file-read interpretation and workspace scripts/modified profiles
          through execution
        assessment: partial
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-workspace-files
          - runtime.md#rt-rte-file-exchange
          note: Prose supplied by file read receives meaning through client interpretation.
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-workspace-files
          - memory.md#mem-obj-session-profile
          - runtime.md#rt-rte-sandbox-exec
          note: Shell scripts and changed profile instructions receive effects through shell rules.
        records:
        - memory.md#mem-obj-workspace-files
        - memory.md#mem-obj-session-profile
        - runtime.md#rt-rte-file-exchange
        - runtime.md#rt-rte-sandbox-exec
        note: Prose and code paths are supported; actual images, binary blobs and arbitrary file contents
          lack an interpreted instance.
      - scope: Job stream/sequence/cursor/state metadata and terminal results
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-output-log
          - memory.md#mem-obj-job-snapshot
          - runtime.md#rt-rte-retained-jobs
          note: Sequence numbers, stream labels, state and terminal outcome determine fixed-rule access/display.
        records:
        - memory.md#mem-obj-output-log
        - memory.md#mem-obj-job-snapshot
        - runtime.md#rt-rte-retained-jobs
        note: Localized metadata is consumed by fixed paging and state rules, separately from arbitrary
          output bytes.
      - scope: Raw job-output payload and decoded client display
        assessment: partial
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-output-log
          - epistemic.md#epi-rte-result-render
          note: Surviving textual output is delivered as an advisory execution report; lossy decoding
            does not establish its truth.
        records:
        - memory.md#mem-obj-output-log
        - epistemic.md#epi-rte-result-render
        note: Readable prose is a supported consumption path, but arbitrary or malformed bytes have no
          established complete form classification.
      - scope: Timestamp tribles and telemetry ID/name/duration facts at their script consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - epistemic.md#epi-obj-timestamp-tribles
          - epistemic.md#epi-obj-telemetry-spans
          - epistemic.md#epi-rte-timestamp-reshape
          - epistemic.md#epi-rte-telemetry-report
          note: Attribute mapping, integer conversion, fixed queries and arithmetic consume localized
            records.
        records:
        - epistemic.md#epi-obj-timestamp-tribles
        - epistemic.md#epi-obj-telemetry-spans
        - epistemic.md#epi-rte-timestamp-reshape
        - epistemic.md#epi-rte-telemetry-report
        note: Names are grouping keys and durations are arithmetic inputs, not distributed parameters.
      - scope: Wiki fragment prose and link identifiers at wrapper/resolver consumers
        assessment: partial
        findings:
        - value: natural-language
          basis: wired
          records:
          - epistemic.md#epi-obj-wiki-fragments
          note: Fragment prose carries assertions for interpretation.
        - value: symbolic
          basis: wired
          records:
          - epistemic.md#epi-obj-wiki-fragments
          - epistemic.md#epi-rte-link-rewrite
          note: Wiki/files identifiers and prefix patterns receive fixed wrapper selection and edit handling.
        records:
        - epistemic.md#epi-obj-wiki-fragments
        - epistemic.md#epi-rte-link-rewrite
        note: Text and localized links are identified; external resolver interpretation and arbitrary
          fragment instances remain unresolved.
      - scope: Documented summary text and temporal/child access structures
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records:
          - memory.md#mem-clm-memory-cover
          note: Summary blobs supply long-term model context.
        - value: symbolic
          basis: claimed
          records:
          - memory.md#mem-clm-memory-cover
          note: Temporal ranges and child edges structure cover selection and provenance queries.
        records:
        - memory.md#mem-clm-memory-cover
        note: Complete only for the parts the cover claim describes, not actual mounted piles.
      - scope: Self/shared pile payloads and native-worker semantic consumption
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-self-pile
        - memory.md#mem-obj-shared-pile
        - runtime.md#rt-rte-worker-forward
        note: Native bytes and downstream consumers are opaque; neither policy labels nor the summary
          doctrine classify actual pile payloads.
      records:
      - memory.md#mem-obj-workspace-files
      - memory.md#mem-obj-session-profile
      - runtime.md#rt-rte-file-exchange
      - runtime.md#rt-rte-sandbox-exec
      - memory.md#mem-obj-output-log
      - memory.md#mem-obj-job-snapshot
      - runtime.md#rt-rte-retained-jobs
      - epistemic.md#epi-rte-result-render
      - epistemic.md#epi-obj-timestamp-tribles
      - epistemic.md#epi-obj-telemetry-spans
      - epistemic.md#epi-rte-timestamp-reshape
      - epistemic.md#epi-rte-telemetry-report
      - epistemic.md#epi-obj-wiki-fragments
      - epistemic.md#epi-rte-link-rewrite
      - memory.md#mem-clm-memory-cover
      - memory.md#mem-obj-self-pile
      - memory.md#mem-obj-shared-pile
      - runtime.md#rt-rte-worker-forward
      note: Known textual and fixed-rule parts coexist with arbitrary bytes and opaque native content.
        Readable displays do not resolve their payloads.
    lineage:
      assessment: partial
      units:
      - scope: Workspace content and subsequent profile mutations
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-workspace-files
        - memory.md#mem-obj-session-profile
        - runtime.md#rt-rte-file-exchange
        - runtime.md#rt-rte-sandbox-exec
        note: Generic caller identity and encoding do not establish authorship or imported origin; static
          profile generation is excluded.
      - scope: Retained output capture and page/display derivation
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-output-log
          - epistemic.md#epi-rte-result-render
          note: Output bytes are normalized into stored chunks and compiled into bounded formatted reports,
            without semantic summary extraction.
        records:
        - memory.md#mem-obj-output-log
        - epistemic.md#epi-rte-result-render
        note: The capture and normalization chain is known, but the source material printed by arbitrary
          commands is not; raw capture alone is not trace extraction.
      - scope: Jail self-pile bootstrap acquisition and recipient-authored registration path
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-self-pile
          - memory.md#mem-rte-native-onboarding
          note: Jail initialization copies a bootstrap seed and invokes corpus import into retained native
            storage.
        - value: authored
          basis: wired
          records:
          - memory.md#mem-rte-native-onboarding
          note: Recipient-signed native registration supplies tenant-derived identity/label additions
            through the fixed onboarding path.
        records:
        - memory.md#mem-obj-self-pile
        - memory.md#mem-rte-native-onboarding
        - memory.md#mem-obj-shared-pile
        note: Copy/import and tenant registration are supported locally; initial shared content and native
          corpus derivation remain unresolved.
      - scope: Lima initial self-pile contents and other native-worker content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-self-pile
        - runtime.md#rt-rte-worker-forward
        note: Operator-resolved storage and worker forwarding do not disclose initial or subsequent content
          derivation.
      - scope: Timestamp migration additions
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - epistemic.md#epi-rte-timestamp-reshape
          - epistemic.md#epi-rte-timestamp-retain
          note: Fixed maps and conversion compile existing timestamp facts into alternate encoded additions.
        records:
        - epistemic.md#epi-obj-timestamp-tribles
        - epistemic.md#epi-rte-timestamp-reshape
        - epistemic.md#epi-rte-timestamp-retain
        note: This unit covers only the inspected old-to-new encoding path; source timestamp truth/provenance
          is not classified by it.
      - scope: Wiki edits and original telemetry/wiki records
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - epistemic.md#epi-obj-wiki-fragments
          - epistemic.md#epi-rte-link-rewrite
          note: Exported fragments pass through an external expansion tool and changed output becomes
            an edit request; semantic lineage remains bounded.
        records:
        - epistemic.md#epi-obj-wiki-fragments
        - epistemic.md#epi-rte-link-rewrite
        - epistemic.md#epi-obj-telemetry-spans
        - epistemic.md#epi-rte-telemetry-report
        note: Wiki changed-text production is known at the wrapper; original content and external resolution/trace
          producer provenance remain unresolved.
      - scope: Documented explicit memory text and episode-summary derivation
        assessment: partial
        findings:
        - value: authored
          basis: claimed
          records:
          - memory.md#mem-clm-memory-cover
          note: Explicit memory creation stores supplied summary text and range.
        - value: trace-extracted
          basis: claimed
          records:
          - memory.md#mem-clm-memory-cover
          note: Requested episode consolidation derives summaries from past conversational/work events.
        records:
        - memory.md#mem-clm-memory-cover
        note: Explicit supplied text and extraction from recorded episodes are declared; actual human/model
          authorship and initial content are unresolved.
      records:
      - memory.md#mem-obj-workspace-files
      - memory.md#mem-obj-session-profile
      - runtime.md#rt-rte-file-exchange
      - runtime.md#rt-rte-sandbox-exec
      - memory.md#mem-obj-output-log
      - epistemic.md#epi-rte-result-render
      - memory.md#mem-obj-self-pile
      - memory.md#mem-rte-native-onboarding
      - memory.md#mem-obj-shared-pile
      - runtime.md#rt-rte-worker-forward
      - epistemic.md#epi-obj-timestamp-tribles
      - epistemic.md#epi-rte-timestamp-reshape
      - epistemic.md#epi-rte-timestamp-retain
      - epistemic.md#epi-obj-wiki-fragments
      - epistemic.md#epi-rte-link-rewrite
      - epistemic.md#epi-obj-telemetry-spans
      - epistemic.md#epi-rte-telemetry-report
      - memory.md#mem-clm-memory-cover
      note: Known acquisition and transformation paths do not settle original workspace, native, telemetry
        or wiki provenance.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Accumulated workspace prose at MCP clients
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-workspace-files
          - runtime.md#rt-rte-file-exchange
          note: Requested file content supplies evidence/reference material to the client.
        records:
        - memory.md#mem-obj-workspace-files
        - runtime.md#rt-rte-file-exchange
        note: This classifies the delivered reference/context channel, not truth or actual client reliance.
      - scope: Stored scripts and use-modified profile instructions at fresh shells
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-obj-workspace-files
          - memory.md#mem-obj-session-profile
          - runtime.md#rt-rte-sandbox-exec
          note: The shell consumes scripts and profile code as executable directions shaping command environment
            and effects.
        records:
        - memory.md#mem-obj-workspace-files
        - memory.md#mem-obj-session-profile
        - runtime.md#rt-rte-sandbox-exec
        note: Only executable persisted content and defaults are included; initial shipped/provisioned
          directions are excluded.
      - scope: Retained job output at the client and sequence metadata at polling code
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-output-log
          - epistemic.md#epi-rte-result-render
          note: Surviving output and terminal reports provide execution evidence to the caller.
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-output-log
          - runtime.md#rt-rte-retained-jobs
          note: Retained sequence/tail state selects the surviving output window for the requested cursor.
        records:
        - memory.md#mem-obj-output-log
        - runtime.md#rt-rte-retained-jobs
        - epistemic.md#epi-rte-result-render
        note: Client delivery is advisory; fixed selectors act on metadata rather than semantic truth.
      - scope: Retained handle terminal/final-page-observation state at subsequent job admission
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - runtime.md#rt-rte-retained-jobs
          - memory.md#mem-obj-job-snapshot
          note: Live/unobserved versus observed-terminal handle state determines whether capacity can
            admit a new job.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-rte-retained-jobs
          - memory.md#mem-obj-job-snapshot
          note: The same retained state can refuse new submissions when occupied handles cannot yield
            capacity.
        records:
        - runtime.md#rt-rte-retained-jobs
        - memory.md#mem-obj-job-snapshot
        note: These criteria govern capacity recycling and refusal, not acceptance of an answer.
      - scope: Retained timestamp facts at migration and wiki fragments at rewrite
        assessment: partial
        findings:
        - value: routing
          basis: wired
          records:
          - epistemic.md#epi-obj-timestamp-tribles
          - epistemic.md#epi-rte-timestamp-reshape
          - epistemic.md#epi-obj-wiki-fragments
          - epistemic.md#epi-rte-link-rewrite
          note: Old attribute IDs and short-link patterns select facts/fragments for particular maintenance
            operations.
        records:
        - epistemic.md#epi-obj-timestamp-tribles
        - epistemic.md#epi-rte-timestamp-reshape
        - epistemic.md#epi-obj-wiki-fragments
        - epistemic.md#epi-rte-link-rewrite
        - memory.md#mem-rte-storage-maintenance
        note: Wrapper selection is known; actual later semantic readers of changed native content are
          external.
      - scope: Retained telemetry measurements at diagnostic arithmetic and operator display
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - epistemic.md#epi-obj-telemetry-spans
          - epistemic.md#epi-rte-telemetry-report
          note: Retained durations and name totals determine relative order of displayed spans/groups.
        - value: knowledge
          basis: wired
          records:
          - epistemic.md#epi-obj-telemetry-spans
          - epistemic.md#epi-rte-telemetry-report
          note: Selected retained measurements and conditional aggregates inform the console reader.
        records:
        - epistemic.md#epi-obj-telemetry-spans
        - epistemic.md#epi-rte-telemetry-report
        note: Fixed arithmetic and ordering are inspected; causal measurement truth and adaptation are
          not.
      - scope: Documented summaries at external context assembly/model and episode inputs at requested
          consolidation
        assessment: partial
        findings:
        - value: knowledge
          basis: claimed
          records:
          - memory.md#mem-clm-memory-cover
          note: Selected summaries supply long-term contextual recollection to the model.
        - value: learning
          basis: claimed
          records:
          - memory.md#mem-clm-memory-cover
          note: The requested consolidation consumer uses retained episode experience to produce durable
            later-context summaries; this is a declared update path, not demonstrated improvement.
        records:
        - memory.md#mem-clm-memory-cover
        note: Declared context supply is supported, while actual update control/consumer wiring and alternative
          legacy mechanisms remain unresolved.
      - scope: Self/shared pile content at external faculty/native-worker consumers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-self-pile
        - memory.md#mem-obj-shared-pile
        - runtime.md#rt-rte-worker-forward
        note: Custody, signer identity and policy labels do not establish downstream knowledge, enforcement
          or other semantic force.
      records:
      - memory.md#mem-obj-workspace-files
      - runtime.md#rt-rte-file-exchange
      - memory.md#mem-obj-session-profile
      - runtime.md#rt-rte-sandbox-exec
      - memory.md#mem-obj-output-log
      - runtime.md#rt-rte-retained-jobs
      - epistemic.md#epi-rte-result-render
      - memory.md#mem-obj-job-snapshot
      - epistemic.md#epi-obj-timestamp-tribles
      - epistemic.md#epi-rte-timestamp-reshape
      - epistemic.md#epi-obj-wiki-fragments
      - epistemic.md#epi-rte-link-rewrite
      - memory.md#mem-rte-storage-maintenance
      - epistemic.md#epi-obj-telemetry-spans
      - epistemic.md#epi-rte-telemetry-report
      - memory.md#mem-clm-memory-cover
      - memory.md#mem-obj-self-pile
      - memory.md#mem-obj-shared-pile
      - runtime.md#rt-rte-worker-forward
      note: Authority is attached to particular consumers; native semantic effects and arbitrary payload
        interpretation remain unresolved. No learning benefit or compliance is inferred.
    write_agency:
      assessment: partial
      units:
      - scope: MCP file replacement and arbitrary shell/profile mutation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-workspace-files
        - memory.md#mem-obj-session-profile
        - runtime.md#rt-rte-file-exchange
        - runtime.md#rt-rte-sandbox-exec
        note: No per-content human gate is imposed, but generic callers can be humans or programs; absence
          of a gate does not identify their admission decisions.
      - scope: Job output capture and retention-state updates
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-output-log
          - runtime.md#rt-rte-retained-jobs
          - memory.md#mem-obj-job-snapshot
          note: Execution sinks and manager code admit bytes/state without a per-chunk operator decision.
        records:
        - memory.md#mem-obj-output-log
        - runtime.md#rt-rte-retained-jobs
        - memory.md#mem-obj-job-snapshot
        note: Capture/state updates are software-driven once work is launched; workflow launch is not
          content approval.
      - scope: Fixed jail onboarding import/tenant registration wrapper
        assessment: partial
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-native-onboarding
          note: Provisioning invokes fixed import/registration and software checks process success, without
            per-addition human approval.
        records:
        - memory.md#mem-rte-native-onboarding
        - memory.md#mem-obj-self-pile
        - memory.md#mem-obj-shared-pile
        note: Software initiates fixed additions; per-fact native acceptance and initial corpus/shared
          seed control remain external.
      - scope: Timestamp migration and changed-text wiki edit wrappers
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-storage-maintenance
          - epistemic.md#epi-rte-timestamp-retain
          - epistemic.md#epi-rte-link-rewrite
          note: Fixed mapping/nonempty/dry-run and changed-text predicates decide individual write requests.
        records:
        - memory.md#mem-rte-storage-maintenance
        - epistemic.md#epi-rte-timestamp-reshape
        - epistemic.md#epi-rte-timestamp-retain
        - epistemic.md#epi-rte-link-rewrite
        note: Operator invocation/dry-run choice does not manually approve every retained change; external
          semantic acceptance is a separate unresolved mechanism.
      - scope: Requested model episode consolidation
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records:
          - memory.md#mem-clm-memory-cover
          note: Prompts request the model to consolidate episodes and retain memories; no per-summary
            human approval is specified.
        records:
        - memory.md#mem-clm-memory-cover
        note: This unit covers the model-directed request only, not every explicit memory-create caller.
      - scope: Initial piles, explicit memory-create callers, telemetry producers and external native
          admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-self-pile
        - memory.md#mem-obj-shared-pile
        - memory.md#mem-clm-memory-cover
        - epistemic.md#epi-obj-telemetry-spans
        - runtime.md#rt-rte-worker-forward
        note: Manual-curation terminology and an operator-supplied file do not establish an explicit human
          decision for every retained item. Native and trace-producer admission are opaque.
      records:
      - memory.md#mem-obj-workspace-files
      - memory.md#mem-obj-session-profile
      - runtime.md#rt-rte-file-exchange
      - runtime.md#rt-rte-sandbox-exec
      - memory.md#mem-obj-output-log
      - runtime.md#rt-rte-retained-jobs
      - memory.md#mem-obj-job-snapshot
      - memory.md#mem-rte-native-onboarding
      - memory.md#mem-obj-self-pile
      - memory.md#mem-obj-shared-pile
      - memory.md#mem-rte-storage-maintenance
      - epistemic.md#epi-rte-timestamp-reshape
      - epistemic.md#epi-rte-timestamp-retain
      - epistemic.md#epi-rte-link-rewrite
      - memory.md#mem-clm-memory-cover
      - epistemic.md#epi-obj-telemetry-spans
      - runtime.md#rt-rte-worker-forward
      note: Software admission is established for output capture, onboarding wrappers and maintenance.
        Caller-driven content decisions and external native admission remain unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Replacement of retained workspace content
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-workspace-files
          - runtime.md#rt-rte-file-exchange
          note: A subsequent successful write revises the stored file at the same path, with possible
            partial writes on failure.
        records:
        - memory.md#mem-obj-workspace-files
        - runtime.md#rt-rte-file-exchange
        note: The inspected file tool replaces existing retained bytes; arbitrary command transformations
          remain outside this resolved mechanism.
      - scope: Retained job-output eviction/expiry
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-obj-output-log
          - runtime.md#rt-rte-retained-jobs
          note: Oldest chunks are discarded at byte/count limits; terminal TTL and capacity recycling
            forget retained outcomes.
        records:
        - memory.md#mem-obj-output-log
        - runtime.md#rt-rte-retained-jobs
        note: Bounds and TTL forget retained material without semantic consolidation.
      - scope: Timestamp encoding maintenance
        assessment: inapplicable
        findings: []
        records:
        - epistemic.md#epi-rte-timestamp-reshape
        - epistemic.md#epi-rte-timestamp-retain
        - memory.md#mem-rte-storage-maintenance
        note: Additive encoding conversion and skipping already-present facts establish none of the controlled
          curation transformations by themselves; primary-key collision checks are not dedup.
      - scope: Wiki changed-text edit wrapper
        assessment: partial
        findings:
        - value: evolve
          basis: wired
          records:
          - epistemic.md#epi-rte-link-rewrite
          - memory.md#mem-rte-storage-maintenance
          note: Changed resolver output is submitted as an edit of the existing fragment.
        records:
        - epistemic.md#epi-rte-link-rewrite
        - memory.md#mem-rte-storage-maintenance
        note: An existing fragment is revised; whether external expansion additionally changes claims
          or merges entries is unresolved.
      - scope: Documented episode consolidation and context-cover trimming
        assessment: partial
        findings:
        - value: consolidate
          basis: claimed
          records:
          - memory.md#mem-clm-memory-cover
          note: Prompt-directed summaries compress coherent retained episodes for later context.
        - value: decay
          basis: claimed
          records:
          - memory.md#mem-clm-memory-cover
          note: The declared cover omits oldest roots when over budget; this is downweighting in delivery,
            not proven storage deletion.
        records:
        - memory.md#mem-clm-memory-cover
        note: Summary compression and dropping old roots are declared; legacy lens alternatives and actual
          transformation semantics remain unresolved.
      - scope: Arbitrary shell mutations, native pile/worker maintenance and telemetry retention
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-workspace-files
        - memory.md#mem-obj-self-pile
        - memory.md#mem-obj-shared-pile
        - runtime.md#rt-rte-worker-forward
        - epistemic.md#epi-obj-telemetry-spans
        note: These included alternative mechanisms lack recorded transformations sufficient for controlled
          values.
      records:
      - memory.md#mem-obj-workspace-files
      - runtime.md#rt-rte-file-exchange
      - memory.md#mem-obj-output-log
      - runtime.md#rt-rte-retained-jobs
      - epistemic.md#epi-rte-timestamp-reshape
      - epistemic.md#epi-rte-timestamp-retain
      - memory.md#mem-rte-storage-maintenance
      - epistemic.md#epi-rte-link-rewrite
      - memory.md#mem-clm-memory-cover
      - memory.md#mem-obj-self-pile
      - memory.md#mem-obj-shared-pile
      - runtime.md#rt-rte-worker-forward
      - epistemic.md#epi-obj-telemetry-spans
      note: Replacement, trimming and wrapper edits are inspected; consolidation/cover trimming are declared.
        Opaque native transformations and resolver effects prevent a complete operation inventory.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested workspace read/exec and retained job polling
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-file-exchange
          - runtime.md#rt-rte-sandbox-exec
          - runtime.md#rt-rte-retained-jobs
          note: Caller-selected paths, shell work and job IDs/cursors request accumulated material.
        records:
        - memory.md#mem-obj-workspace-files
        - runtime.md#rt-rte-file-exchange
        - runtime.md#rt-rte-sandbox-exec
        - memory.md#mem-obj-output-log
        - runtime.md#rt-rte-retained-jobs
        note: Delivery fulfills a consumer request; literal paths/job IDs do not turn it into independent
          push.
      - scope: Use-modified session profile on fresh login-shell invocation
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-session-profile
          - runtime.md#rt-rte-sandbox-exec
          note: A fresh login shell automatically applies persisted profile defaults without a request
            for that retained content.
        records:
        - memory.md#mem-obj-session-profile
        - runtime.md#rt-rte-sandbox-exec
        note: Only the subsequently changed profile is use-accumulated memory; clean file tools bypass
          it.
      - scope: Standalone native maintenance/telemetry input reads
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-storage-maintenance
          - epistemic.md#epi-rte-timestamp-reshape
          - epistemic.md#epi-rte-link-rewrite
          - epistemic.md#epi-rte-telemetry-report
          note: Scripts enumerate requested native branches/fragments or telemetry records for their selected
            administrative operation.
        records:
        - memory.md#mem-rte-storage-maintenance
        - epistemic.md#epi-rte-timestamp-reshape
        - epistemic.md#epi-rte-link-rewrite
        - epistemic.md#epi-obj-telemetry-spans
        - epistemic.md#epi-rte-telemetry-report
        note: Operator script invocation requests retained material; internal filtering within that request
          is not a second push.
      - scope: Documented automatic cover and explicit temporal recall/provenance
        assessment: known
        findings:
        - value: push
          basis: claimed
          records:
          - memory.md#mem-clm-memory-cover
          note: Each model invocation automatically receives budget-selected summary cover.
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-clm-memory-cover
          note: Explicit temporal recall/provenance requests retained episode/source material.
        records:
        - memory.md#mem-clm-memory-cover
        note: Directions are classified for the described mechanisms only, not attributed as implemented
          provider behavior.
      - scope: Native faculty/worker semantic read-back
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-self-pile
        - memory.md#mem-obj-shared-pile
        - runtime.md#rt-rte-worker-forward
        note: Mounted state and forwarded calls do not reveal whether requested or unsolicited native
          content reaches later semantic consumers.
      records:
      - memory.md#mem-obj-workspace-files
      - runtime.md#rt-rte-file-exchange
      - runtime.md#rt-rte-sandbox-exec
      - memory.md#mem-obj-output-log
      - runtime.md#rt-rte-retained-jobs
      - memory.md#mem-obj-session-profile
      - memory.md#mem-rte-storage-maintenance
      - epistemic.md#epi-rte-timestamp-reshape
      - epistemic.md#epi-rte-link-rewrite
      - epistemic.md#epi-obj-telemetry-spans
      - epistemic.md#epi-rte-telemetry-report
      - memory.md#mem-clm-memory-cover
      - memory.md#mem-obj-self-pile
      - memory.md#mem-obj-shared-pile
      - runtime.md#rt-rte-worker-forward
      note: Requested files, shell access, replay and diagnostic reads are pull; documented cover and
        modified-profile application are push. Native semantic alternatives remain unresolved.
    read_back_signal:
      assessment: partial
      units:
      - scope: Automatic application of a use-modified profile
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-session-profile
          - runtime.md#rt-rte-sandbox-exec
          note: Login mode automatically supplies the available persisted profile; clean mode excludes
            it.
        records:
        - memory.md#mem-obj-session-profile
        - runtime.md#rt-rte-sandbox-exec
        note: Trigger is a login-shell start; selector is login-mode/profile availability; selected part
          is the entire persisted profile. No content identity matching is recorded.
      - scope: Documented cover push
        assessment: known
        findings:
        - value: coarse
          basis: claimed
          records:
          - memory.md#mem-clm-memory-cover
          note: Chronological ordering, oldest-root removal, affordable child splitting and gap stopping
            select cover by temporal/budget rules, not task judgment or embedding.
        records:
        - memory.md#mem-clm-memory-cover
        note: Trigger is model invocation; inputs are temporal root/child structure and remaining context
          budget; selected parts are retained summary chunks.
      - scope: Explicit file/job/script/temporal recall requests
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-file-exchange
        - runtime.md#rt-rte-retained-jobs
        - memory.md#mem-rte-storage-maintenance
        - epistemic.md#epi-rte-telemetry-report
        - memory.md#mem-clm-memory-cover
        note: These units fulfill explicit requests. Path, job ID, sequence cursor and branch/tag IDs
          are pull selectors, not identifier-based push.
      - scope: Native worker/faculty unsolicited delivery alternatives
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-worker-forward
        - memory.md#mem-obj-self-pile
        - memory.md#mem-obj-shared-pile
        note: No native selector input or delivered part is inspectable; known provider pull cannot resolve
          this included alternative.
      records:
      - memory.md#mem-obj-session-profile
      - runtime.md#rt-rte-sandbox-exec
      - memory.md#mem-clm-memory-cover
      - runtime.md#rt-rte-file-exchange
      - runtime.md#rt-rte-retained-jobs
      - memory.md#mem-rte-storage-maintenance
      - epistemic.md#epi-rte-telemetry-report
      - runtime.md#rt-rte-worker-forward
      - memory.md#mem-obj-self-pile
      - memory.md#mem-obj-shared-pile
      note: Coarse profile availability and declared temporal/budget cover selection are positive push
        signals. Pull selectors are inapplicable locally, not evidence that opaque native alternatives
        are pull-only.
    trace_learning:
      assessment: partial
      units:
      - scope: Requested episode-to-memory-to-later-cover route
        assessment: partial
        findings:
        - value: 'yes'
          basis: claimed
          records:
          - memory.md#mem-clm-memory-cover
          note: Recorded episodes feed requested model consolidation into durable summaries supplied as
            later context. This is claimed, not a wired provider learning route.
        records:
        - memory.md#mem-clm-memory-cover
        note: Prompts request a model update and documents retain/deliver summaries, but actual producer/admission/wiring
          and legacy alternatives remain unresolved.
      - scope: Provider job-output capture/replay
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-output-log
        - runtime.md#rt-rte-retained-jobs
        - epistemic.md#epi-rte-result-render
        note: Records describe raw retention/rendering, not a durable derived summary or parameter update.
          They supply no canonical bounded-absence record for a controlled no; later caller updates are
          external.
      - scope: Telemetry diagnostic aggregate production
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-obj-telemetry-spans
        - epistemic.md#epi-rte-telemetry-report
        note: The inspected report ends at stdout without a retained adaptation. No qualifying yes or
          canonical bounded-absence record for no is supplied; downstream operator updates are external.
      - scope: Timestamp/link maintenance wrappers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-storage-maintenance
        - epistemic.md#epi-rte-timestamp-reshape
        - epistemic.md#epi-rte-timestamp-retain
        - epistemic.md#epi-rte-link-rewrite
        note: Encoding/reference transformations do not establish a qualifying trace-fed update. A canonical
          bounded-absence record for no and external update-consumer coverage are not supplied.
      - scope: Arbitrary workspace programs, initial native corpus, telemetry producer and native-worker
          transformations
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-workspace-files
        - memory.md#mem-rte-native-onboarding
        - memory.md#mem-obj-self-pile
        - runtime.md#rt-rte-worker-forward
        - epistemic.md#epi-obj-telemetry-spans
        note: Uninspected producers/admission and later consumers prevent a complete positive or negative
          trace-learning classification.
      records:
      - memory.md#mem-clm-memory-cover
      - memory.md#mem-obj-output-log
      - runtime.md#rt-rte-retained-jobs
      - epistemic.md#epi-rte-result-render
      - epistemic.md#epi-obj-telemetry-spans
      - epistemic.md#epi-rte-telemetry-report
      - memory.md#mem-rte-storage-maintenance
      - epistemic.md#epi-rte-timestamp-reshape
      - epistemic.md#epi-rte-timestamp-retain
      - epistemic.md#epi-rte-link-rewrite
      - memory.md#mem-obj-workspace-files
      - memory.md#mem-rte-native-onboarding
      - memory.md#mem-obj-self-pile
      - runtime.md#rt-rte-worker-forward
      note: Requested model consolidation supplies a claimed positive. Raw replay, diagnostics and maintenance
        have no recorded qualifying update, but lack canonical bounded-absence records for local no values.
        External automatic transforms and actual summary admission remain unresolved; no observed benefit
        is asserted.
    trace_source:
      assessment: partial
      units:
      - scope: Documented episode consolidation original inputs
        assessment: partial
        findings:
        - value: session-logs
          basis: claimed
          records:
          - memory.md#mem-clm-memory-cover
          - epistemic.md#epi-clm-memory-provenance
          note: Past interactions and archive messages supply conversational episode input to requested
            memory consolidation.
        - value: tool-traces
          basis: claimed
          records:
          - memory.md#mem-clm-memory-cover
          - epistemic.md#epi-clm-memory-provenance
          note: Cognition command/execution results supply recorded tool activity to the described episode-summary
            route.
        records:
        - memory.md#mem-clm-memory-cover
        - epistemic.md#epi-clm-memory-provenance
        note: Conversational archive messages and cognition execution results are described; actual consumed
          mix and opaque legacy alternatives are not established.
      - scope: Raw job replay, telemetry stdout aggregation and encoding/link maintenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-output-log
        - runtime.md#rt-rte-retained-jobs
        - epistemic.md#epi-rte-telemetry-report
        - memory.md#mem-rte-storage-maintenance
        note: No qualifying trace-learning write is established here, but the records do not provide the
          complete bounded absence needed to make trace source inapplicable.
      - scope: Opaque workspace/native-worker trace-fed writes and native initial provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-workspace-files
        - memory.md#mem-rte-native-onboarding
        - memory.md#mem-obj-self-pile
        - runtime.md#rt-rte-worker-forward
        - epistemic.md#epi-obj-telemetry-spans
        note: Whether a qualifying write exists and its original input content are unresolved; imported
          seed material or telemetry labels cannot settle trace origin.
      records:
      - memory.md#mem-clm-memory-cover
      - epistemic.md#epi-clm-memory-provenance
      - memory.md#mem-obj-output-log
      - runtime.md#rt-rte-retained-jobs
      - epistemic.md#epi-rte-telemetry-report
      - memory.md#mem-rte-storage-maintenance
      - memory.md#mem-obj-workspace-files
      - memory.md#mem-rte-native-onboarding
      - memory.md#mem-obj-self-pile
      - runtime.md#rt-rte-worker-forward
      - epistemic.md#epi-obj-telemetry-spans
      note: Session and tool origins are supported only for the claimed episode-consolidation route. No
        adapter/branch name creates an event-stream or trajectory finding; unresolved native writes retain
        uncertainty.
---

# Playground memory profile

## Comparison rationale

The inventory follows retained material and its later consumers, not every piece of provider storage. Mounted pile files are a known substrate even when their internal form and semantic use are opaque. Additional external-worker state remains unresolved. Initial provisioning profiles are static directions; only their later use-driven changes enter the profile. Signer keys, credentials, fixed gateway mappings and executable bundle caches are access/capability machinery, not recollections. See [MEM-OBJ-self-pile](memory.md#mem-obj-self-pile), [MEM-OBJ-session-profile](memory.md#mem-obj-session-profile) and [RT-RTE-worker-forward](runtime.md#rt-rte-worker-forward).

Workspace payloads do not get one form or lineage from their MIME label. Prose interpretation and executable scripts are classified separately from opaque bytes. Similarly, job metadata selects output and gates later capacity, while raw output supplies an advisory execution report. Retention does not grant substantive warrant, and final-page observation does not establish receipt. See [MEM-OBJ-workspace-files](memory.md#mem-obj-workspace-files), [MEM-OBJ-output-log](memory.md#mem-obj-output-log), [MEM-OBJ-job-snapshot](memory.md#mem-obj-job-snapshot) and [EPI-RTE-result-render](epistemic.md#epi-rte-result-render).

Other-compiled lineage names the inspected conversion/formatting paths, not inferred original authorship. Timestamp collision avoidance is not deduplication; additive encoding conversion alone is not a controlled curation operation. Wiki changed-text editing supports evolution at the wrapper, without resolving whether the external resolver also changes claims. Retained telemetry durations influence ranking under fixed code, but console arithmetic creates no retained behavioral adaptation. See [EPI-RTE-timestamp-reshape](epistemic.md#epi-rte-timestamp-reshape), [EPI-RTE-timestamp-retain](epistemic.md#epi-rte-timestamp-retain), [EPI-RTE-link-rewrite](epistemic.md#epi-rte-link-rewrite) and [EPI-RTE-telemetry-report](epistemic.md#epi-rte-telemetry-report).

The summary-cover branch remains doctrine. The requested model consolidation path supports claimed automatic admission, consolidation, learning authority at the update consumer and trace learning through later-context summaries. None upgrades unspecified memory-create callers or opaque native admission. “Manually curated” does not identify a human per-content approval mechanism. Actual automatic production, loaded prompts, summary fidelity and exercised improvement remain unestablished. The current provider has no recorded built-in loader on the searched entry/module surfaces; that bounded absence does not negate the external-worker alternative. See [MEM-CLM-memory-cover](memory.md#mem-clm-memory-cover), [EPI-CLM-memory-provenance](epistemic.md#epi-clm-memory-provenance) and [MEM-ABS-context-loader](memory.md#mem-abs-context-loader).

Direction is assessed operation by operation. File/job/script requests are pull even when IDs select their returned parts. Automatically applying a subsequently changed profile is a separate coarse push. Declared cover push uses temporal hierarchy and budgets; child links alone do not establish an identity-match push selector. Unknown native delivery prevents an all-pull conclusion. See [RT-RTE-file-exchange](runtime.md#rt-rte-file-exchange), [RT-RTE-retained-jobs](runtime.md#rt-rte-retained-jobs), [MEM-OBJ-session-profile](memory.md#mem-obj-session-profile) and [MEM-CLM-memory-cover](memory.md#mem-clm-memory-cover).

Raw replay, non-retained telemetry reports and compatibility maintenance establish no qualifying trace-fed update. The accepted set supplies no canonical bounded-absence records licensing local no findings on those units, so they remain not-determinable rather than becoming system-wide negatives. The system union retains claimed episode-summary learning and unresolved native writes without implying complete coverage. Conversation and execution-result origin support session-logs and tool-traces on the claimed summary path; timestamped serialization and temporal association do not add event-streams or prove causal derivation. See [MEM-CLM-memory-cover](memory.md#mem-clm-memory-cover), [MEM-OBJ-output-log](memory.md#mem-obj-output-log), [EPI-RTE-telemetry-report](epistemic.md#epi-rte-telemetry-report) and [EPI-CLM-memory-provenance](epistemic.md#epi-clm-memory-provenance).

Reconciliation supersedes the memory telemetry-display route with the canonical [EPI-RTE-telemetry-report](epistemic.md#epi-rte-telemetry-report). Telemetry classifications cite that canonical route. The valid maintenance container remains alongside its timestamp conversion/retention and wiki parts; none is discarded. These connections change citation identity, not the local wired implementation or uninspected operation findings. No observed-run or causal basis is available for any classification.

Source-read log: none. This profile uses only the supplied accepted records and their annotations, with supersessions resolved through the supplied reconciliation; no frozen-source read or report re-verification was performed.
