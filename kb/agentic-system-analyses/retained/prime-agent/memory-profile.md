---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: Prime Agent's retained harness, session summaries, namespace checkpoints and changed resources,
  with unresolved control and provider alternatives.
run-id: AAS-2026-10-14-prime-agent-8ec59ae12476-01
source-identity: https://github.com/PrimeIntellect-ai/prime-agent
reviewed-boundary: 33da15a2c15c4e903c372f69ae8e1156d77d53da
memory-comparison:
  version: 2
  scope: 'Included: all five use-authored or use-refined local/global harness kinds and their access metadata;
    accumulated session messages, compaction/branch summaries and refinement audit/event projections;
    serialized/revived namespace and distinct manifest/notice; use-authored or changed skill/resource
    files; retained child results; incompletely traced goals/quota/scheduling, fork and observe/message/recovery
    alternatives; unresolved provider-side accumulated/adapted state, if any. Excluded: unchanged shipped
    instructions and library machine templates, ordinary live factory run registry/ports as such, fixed
    inference weights as such, release deployment payloads, and export/telemetry/workspace artifacts without
    an established later memory consumer. External provider implementation is not frozen; its unresolved
    alternative is retained as uncertainty, not a positive storage or learning claim.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Local/global harness text, skill contracts, subagent templates and stored factory specifications
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-harness-entry
          - memory.md#mem-obj-skill-contract
          - memory.md#mem-obj-subagent-entry
          - runtime.md#rt-obj-factory-machine
          note: Harness JSON persists the operative content and access fields.
        records:
        - memory.md#mem-obj-harness-entry
        - memory.md#mem-obj-skill-contract
        - memory.md#mem-obj-subagent-entry
        - runtime.md#rt-obj-factory-machine
        note: All five harness kinds share the retained JSON file store; the live factory registry is
          a different object.
      - scope: Session messages, summaries, branch-summary entries, refinement audits/history and delivered
          custom rows
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-obj-session-context
          - memory.md#mem-obj-compaction-summary
          - memory.md#mem-rte-branch-navigation
          - memory.md#mem-obj-refinement-result
          - memory.md#mem-obj-kernel-manifest
          - memory.md#mem-rte-digest-delivery
          note: Session JSONL, global history JSONL and harness events retain these objects.
        - value: in-memory
          basis: wired
          records:
          - runtime.md#rt-obj-session-context
          - memory.md#mem-obj-compaction-summary
          - memory.md#mem-rte-branch-navigation
          - memory.md#mem-obj-kernel-manifest
          - memory.md#mem-rte-digest-delivery
          note: Rebuilt messages and custom rows enter live model context.
        records:
        - runtime.md#rt-obj-session-context
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-rte-branch-navigation
        - memory.md#mem-obj-refinement-result
        - memory.md#mem-obj-kernel-manifest
        - memory.md#mem-rte-digest-delivery
        note: Persistent sessions have file-backed histories and live reconstructed context; no-session
          managers retain only live memory.
      - scope: Namespace payload and manifest, with later revived namespace
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-kernel-state
          - memory.md#mem-obj-kernel-manifest
          note: Dill payload and JSON manifest occupy session artifact files.
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-kernel-state
          - memory.md#mem-rte-kernel-revival
          note: Restore assigns prepared values to the session process namespace.
        records:
        - memory.md#mem-obj-kernel-state
        - memory.md#mem-obj-kernel-manifest
        - memory.md#mem-rte-kernel-revival
        note: Payload files are distinct from reporting metadata and their restored process values.
      - scope: Changed skill bodies and executable packages
        assessment: known
        findings:
        - value: files
          basis: afforded
          records:
          - runtime.md#rt-rte-skill-install
          note: Authored resource files are discovered at later startup/reload.
        records:
        - runtime.md#rt-rte-skill-install
        note: The filesystem admission route is afforded; whole-route implementation characterization
          remains disputed, so it is not upgraded.
      - scope: Included persisted goals, quota parks, autonomous/scheduled wake-up controls, fork transfer
          and child observe/message/recovery alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-daemon-session
        - runtime.md#rt-obj-session-context
        - runtime.md#rt-rte-child-spawn
        - memory.md#mem-rte-branch-navigation
        note: The memory inventory identifies these included alternatives but does not fully trace their
          retained parts, admission or replay. Their storage classification remains uninspected; the known
          routes do not enumerate the whole boundary.
      - scope: Opaque provider-side accumulated state, if any; fixed inference weights are not use-derived
          memory
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-provider-model
        note: Provider caching, adaptation and parameter provenance are uninspected. No storage value
          is inferred from ordinary remote inference or a mutable endpoint. External implementation is
          outside frozen evidence, preventing resolution of this included alternative.
      records:
      - memory.md#mem-obj-harness-entry
      - memory.md#mem-obj-skill-contract
      - memory.md#mem-obj-subagent-entry
      - runtime.md#rt-obj-factory-machine
      - runtime.md#rt-obj-session-context
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-rte-branch-navigation
      - memory.md#mem-obj-refinement-result
      - memory.md#mem-obj-kernel-manifest
      - memory.md#mem-rte-digest-delivery
      - memory.md#mem-obj-kernel-state
      - memory.md#mem-rte-kernel-revival
      - runtime.md#rt-rte-skill-install
      - runtime.md#rt-rte-daemon-session
      - runtime.md#rt-rte-child-spawn
      - runtime.md#rt-cmp-provider-model
      note: File and live-memory substrates are supported for inspected parts. Unresolved retained controls,
        fork/recovery alternatives and opaque provider state prevent complete storage coverage; JSON and
        dill are encodings, not additional substrates.
    representational_form:
      assessment: partial
      units:
      - scope: Harness prompt/memory prose, skill explanations and subagent task templates at model consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-harness-entry
          - memory.md#mem-obj-skill-contract
          - memory.md#mem-obj-subagent-entry
          - memory.md#mem-bap-subagent-template
          note: Facts, policies, explanations and child task text are interpreted by models.
        records:
        - memory.md#mem-obj-harness-entry
        - memory.md#mem-obj-skill-contract
        - memory.md#mem-obj-subagent-entry
        - memory.md#mem-bap-subagent-template
        note: Text content has model-interpreted consequences, separate from its fixed-rule selectors.
      - scope: Harness access fields, skill callable/argument contracts, subagent selectors and stored
          machine control graph
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-harness-entry
          - memory.md#mem-obj-skill-contract
          - memory.md#mem-obj-subagent-entry
          - runtime.md#rt-obj-factory-machine
          - runtime.md#rt-bap-machine-guards
          note: Helpers address entries and factory code validates/resolves machine control and spawn
            settings.
        records:
        - memory.md#mem-obj-harness-entry
        - memory.md#mem-obj-skill-contract
        - memory.md#mem-obj-subagent-entry
        - runtime.md#rt-obj-factory-machine
        - runtime.md#rt-bap-machine-guards
        note: IDs, reference records, spawn selectors and guards have localized fixed-rule consumers.
      - scope: Session conversational text, summaries, branch summaries and audit reasons
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - runtime.md#rt-obj-session-context
          - memory.md#mem-obj-compaction-summary
          - memory.md#mem-rte-branch-navigation
          - memory.md#mem-obj-refinement-result
          note: Later models interpret retained messages, continuation summaries and history projections.
        records:
        - runtime.md#rt-obj-session-context
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-rte-branch-navigation
        - memory.md#mem-obj-refinement-result
        note: Prose supplies later context; its containing event structure is assessed separately.
      - scope: Session boundaries, event/edit records, audit snapshots and namespace manifest metadata
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-obj-session-context
          - memory.md#mem-obj-compaction-summary
          - memory.md#mem-obj-refinement-result
          - memory.md#mem-obj-kernel-manifest
          note: Entry boundaries and before/after records drive reconstruction/rollback; names and size
            fields describe checkpoints.
        records:
        - runtime.md#rt-obj-session-context
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-obj-refinement-result
        - memory.md#mem-obj-kernel-manifest
        note: Fixed-rule reconstruction, rollback and bookkeeping consume these structured fields.
      - scope: Model-facing namespace persistence notice
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-kernel-manifest
          note: Foreground model interprets the persistence notice.
        records:
        - memory.md#mem-obj-kernel-manifest
        note: The notice describes names and losses without transmitting variable values.
      - scope: Serialized namespace framing and executable objects at unpickler/runtime
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-kernel-state
          - memory.md#mem-rte-kernel-revival
          note: Framed named records and serialized executable objects are restored by fixed runtime rules.
        records:
        - memory.md#mem-obj-kernel-state
        - memory.md#mem-rte-kernel-revival
        note: Known serialization/execution structure does not resolve arbitrary caller values.
      - scope: Arbitrary values inside the consumed namespace payload
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-kernel-state
        note: Arrays, text and opaque objects are possible but no session payload was supplied. A readable
          manifest cannot classify their form.
      - scope: Changed skill instruction body and Python program
        assessment: known
        findings:
        - value: natural-language
          basis: afforded
          records:
          - runtime.md#rt-rte-skill-install
          note: Changed SKILL.md body supplies later model directions.
        - value: symbolic
          basis: afforded
          records:
          - runtime.md#rt-rte-skill-install
          note: Changed Python programs provide executable local capabilities.
        records:
        - runtime.md#rt-rte-skill-install
        note: The body and program have separate interpretation paths; neither implies model-weight adaptation.
      - scope: Included persisted goals, quota parks, autonomous/scheduled wake-up controls, fork transfer
          and child observe/message/recovery alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-daemon-session
        - runtime.md#rt-obj-session-context
        - runtime.md#rt-rte-child-spawn
        - memory.md#mem-rte-branch-navigation
        note: The memory inventory identifies these included alternatives but does not fully trace their
          retained parts, admission or replay. Their form classification remains uninspected; the known
          routes do not enumerate the whole boundary.
      - scope: Opaque provider-side accumulated state, if any; fixed inference weights are not use-derived
          memory
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-provider-model
        note: Provider caching, adaptation and parameter provenance are uninspected. No form value is
          inferred from ordinary remote inference or a mutable endpoint. External implementation is outside
          frozen evidence, preventing resolution of this included alternative.
      records:
      - memory.md#mem-obj-harness-entry
      - memory.md#mem-obj-skill-contract
      - memory.md#mem-obj-subagent-entry
      - memory.md#mem-bap-subagent-template
      - runtime.md#rt-obj-factory-machine
      - runtime.md#rt-bap-machine-guards
      - runtime.md#rt-obj-session-context
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-rte-branch-navigation
      - memory.md#mem-obj-refinement-result
      - memory.md#mem-obj-kernel-manifest
      - memory.md#mem-obj-kernel-state
      - memory.md#mem-rte-kernel-revival
      - runtime.md#rt-rte-skill-install
      - runtime.md#rt-rte-daemon-session
      - runtime.md#rt-rte-child-spawn
      - runtime.md#rt-cmp-provider-model
      note: Natural-language and symbolic paths coexist. Namespace contents, retained-control alternatives
        and opaque provider adaptation remain unresolved; no parametric memory value follows merely from
        inference.
    lineage:
      assessment: partial
      units:
      - scope: Directly authored harness content and stored factory specification path
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-harness-entry
          - memory.md#mem-obj-skill-contract
          - memory.md#mem-obj-subagent-entry
          - runtime.md#rt-obj-factory-machine
          - runtime.md#rt-rte-python-effects
          note: Caller/model supplies content to direct entry admission.
        records:
        - memory.md#mem-obj-harness-entry
        - memory.md#mem-obj-skill-contract
        - memory.md#mem-obj-subagent-entry
        - runtime.md#rt-obj-factory-machine
        - runtime.md#rt-rte-python-effects
        note: This classifies the supported direct-authoring derivation, not actual pre-existing store
          provenance.
      - scope: Refiner-produced durable entries
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-rte-harness-refine
          - memory.md#mem-obj-harness-entry
          - memory.md#mem-obj-skill-contract
          - memory.md#mem-obj-subagent-entry
          - runtime.md#rt-obj-factory-machine
          note: Trajectory-fed model proposals become retained entries for later digest, inspection or
            factory use.
        records:
        - runtime.md#rt-rte-harness-refine
        - memory.md#mem-obj-harness-entry
        - memory.md#mem-obj-skill-contract
        - memory.md#mem-obj-subagent-entry
        - runtime.md#rt-obj-factory-machine
        note: The refiner uses mixed session experience; not every existing entry was produced by this
          route.
      - scope: Continuation and abandoned-path summaries
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-compaction-summary
          - runtime.md#rt-rte-context-compact
          - memory.md#mem-rte-branch-navigation
          note: Model compression of session prefixes or abandoned branch messages produces retained continuation
            context.
        records:
        - memory.md#mem-obj-compaction-summary
        - runtime.md#rt-rte-context-compact
        - memory.md#mem-rte-branch-navigation
        note: Generated summaries derive from retained messages, sometimes including earlier derived summaries.
      - scope: Refinement result projections and namespace manifest/notice
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-refinement-result
          - memory.md#mem-obj-kernel-manifest
          note: Code constructs edit/status projections, expected-outcome events and checkpoint/name reports.
        records:
        - memory.md#mem-obj-refinement-result
        - memory.md#mem-obj-kernel-manifest
        note: Structured update records and name metadata are program-derived rather than an independently
          authenticated outcome.
      - scope: Serialized namespace framing and revived executable structure
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-kernel-state
          - memory.md#mem-rte-kernel-revival
          note: Runtime serializes eligible live names into a retained checkpoint and rebinds restored
            objects.
        records:
        - memory.md#mem-obj-kernel-state
        - memory.md#mem-rte-kernel-revival
        note: Snapshot construction is known; creation/import provenance of enclosed values is not.
      - scope: Raw session material and enclosed namespace values, including their external inputs
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-session-context
        - memory.md#mem-obj-kernel-state
        note: Messages mix caller, model and tool assertions; namespace values arise from cells, imports
          and external inputs. These records do not enumerate original retained content or establish each
          part's provenance.
      - scope: Initial populated harness-store content
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-harness-entry
        - memory.md#mem-obj-skill-contract
        - memory.md#mem-obj-subagent-entry
        note: New empty stores are possible, but actual initial content and its creator/import path are
          uninspected.
      - scope: Human/model-authored changed skill files
        assessment: known
        findings:
        - value: authored
          basis: afforded
          records:
          - runtime.md#rt-rte-skill-install
          note: The supplied authoring route permits human/model creation and editing of resource files.
        records:
        - runtime.md#rt-rte-skill-install
        note: Static bundled files and library machine templates are excluded as non-accumulated working
          context.
      - scope: Included persisted goals, quota parks, autonomous/scheduled wake-up controls, fork transfer
          and child observe/message/recovery alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-daemon-session
        - runtime.md#rt-obj-session-context
        - runtime.md#rt-rte-child-spawn
        - memory.md#mem-rte-branch-navigation
        note: The memory inventory identifies these included alternatives but does not fully trace their
          retained parts, admission or replay. Their lineage classification remains uninspected; the known
          routes do not enumerate the whole boundary.
      - scope: Opaque provider-side accumulated state, if any; fixed inference weights are not use-derived
          memory
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-provider-model
        note: Provider caching, adaptation and parameter provenance are uninspected. No lineage value
          is inferred from ordinary remote inference or a mutable endpoint. External implementation is
          outside frozen evidence, preventing resolution of this included alternative.
      records:
      - memory.md#mem-obj-harness-entry
      - memory.md#mem-obj-skill-contract
      - memory.md#mem-obj-subagent-entry
      - runtime.md#rt-obj-factory-machine
      - runtime.md#rt-rte-python-effects
      - runtime.md#rt-rte-harness-refine
      - memory.md#mem-obj-compaction-summary
      - runtime.md#rt-rte-context-compact
      - memory.md#mem-rte-branch-navigation
      - memory.md#mem-obj-refinement-result
      - memory.md#mem-obj-kernel-manifest
      - memory.md#mem-obj-kernel-state
      - memory.md#mem-rte-kernel-revival
      - runtime.md#rt-obj-session-context
      - runtime.md#rt-rte-skill-install
      - runtime.md#rt-rte-daemon-session
      - runtime.md#rt-rte-child-spawn
      - runtime.md#rt-cmp-provider-model
      note: Authored, trace-extracted and other-compiled derivations are supported locally. Known later
        transformations do not settle initial store, raw input or enclosed-value provenance; imported
        lineage is not inferred from an import-capable API alone.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Memory-kind facts/preferences/decisions at foreground model
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-harness-entry
          - runtime.md#rt-bap-harness-digest
          - memory.md#mem-rte-digest-delivery
          note: Selected factual content supplies reference/context through the user-role digest.
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-obj-harness-entry
          - memory.md#mem-rte-harness-inspection
          note: Requested full entries can supply foreground reference when exposed by the cell.
        records:
        - memory.md#mem-obj-harness-entry
        - runtime.md#rt-bap-harness-digest
        - memory.md#mem-rte-digest-delivery
        - memory.md#mem-rte-harness-inspection
        note: Digest gives advisory context; requested full detail is a separately afforded consumer path.
      - scope: Prompt policies and skill explanations at foreground model
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-obj-harness-entry
          - memory.md#mem-obj-skill-contract
          - runtime.md#rt-bap-harness-digest
          - memory.md#mem-rte-digest-delivery
          note: Retained policy and call guidance supply directions through digest text.
        - value: instruction
          basis: afforded
          records:
          - memory.md#mem-obj-harness-entry
          - memory.md#mem-obj-skill-contract
          - memory.md#mem-rte-harness-inspection
          note: Full requested policy/contract can guide later model use.
        records:
        - memory.md#mem-obj-harness-entry
        - memory.md#mem-obj-skill-contract
        - runtime.md#rt-bap-harness-digest
        - memory.md#mem-rte-digest-delivery
        - memory.md#mem-rte-harness-inspection
        note: Standing supplemental directions are model-interpreted, not immutable base-prompt enforcement.
      - scope: Stored subagent task content and metadata at factory/child consumers
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-obj-subagent-entry
          - memory.md#mem-bap-subagent-template
          note: Resolved task template directs the later child model.
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-subagent-entry
          note: Retained model/thinking selectors choose the child inference configuration.
        records:
        - memory.md#mem-obj-subagent-entry
        - memory.md#mem-bap-subagent-template
        note: Full prompt reaches the child; model/thinking selectors are consumed separately by host
          code.
      - scope: Stored machine task templates and symbolic control at factory consumers
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - runtime.md#rt-obj-factory-machine
          - runtime.md#rt-rte-factory-run
          note: Stored task templates supply child instructions.
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-obj-factory-machine
          - runtime.md#rt-rte-factory-run
          - runtime.md#rt-bap-machine-guards
          note: States, bindings and guards choose subsequent tasks/inputs.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-obj-factory-machine
          - runtime.md#rt-bap-machine-guards
          note: Declared guards and bounds permit/refuse state progression.
        - value: validation
          basis: wired
          records:
          - runtime.md#rt-obj-factory-machine
          - runtime.md#rt-rte-factory-run
          - runtime.md#rt-bap-machine-guards
          note: Retained spec requirements and guard comparisons constrain admissible progression.
        records:
        - runtime.md#rt-obj-factory-machine
        - runtime.md#rt-rte-factory-run
        - runtime.md#rt-bap-machine-guards
        note: Task directions and executable transition constraints are distinct effects of retained specification
          parts.
      - scope: Entry text/access fields at digest and requested-search rankers
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-rte-digest-delivery
          note: Title/content/path/ID and other fields influence task-query-relative delivery priority.
        - value: ranking
          basis: afforded
          records:
          - memory.md#mem-rte-harness-inspection
          note: Stored fields affect requested search scores and recency tie-breaks.
        records:
        - memory.md#mem-rte-digest-delivery
        - memory.md#mem-rte-harness-inspection
        note: Fixed lexical scoring still gives retained content ranking force.
      - scope: Session messages and retained refinement history at update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - runtime.md#rt-rte-harness-refine
          - memory.md#mem-obj-refinement-result
          note: Retained trajectory and projected history feed durable harness editing.
        - value: learning
          basis: wired
          records:
          - runtime.md#rt-rte-context-compact
          - memory.md#mem-obj-compaction-summary
          - memory.md#mem-rte-branch-navigation
          note: Retained activity feeds durable context summaries for later model invocations.
        records:
        - runtime.md#rt-rte-harness-refine
        - memory.md#mem-obj-refinement-result
        - runtime.md#rt-rte-context-compact
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-rte-branch-navigation
        note: Trace-fed guidance updates and continuation summaries consume retained experience. Expected
          outcome is not a measured benefit.
      - scope: Conversation, summary, audit projection and namespace notice at later foreground model
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - runtime.md#rt-obj-session-context
          - memory.md#mem-obj-compaction-summary
          - memory.md#mem-rte-branch-navigation
          - memory.md#mem-obj-refinement-result
          - memory.md#mem-obj-kernel-manifest
          note: Later model receives retained conversational context, summary, update projections or namespace
            names.
        records:
        - runtime.md#rt-obj-session-context
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-rte-branch-navigation
        - memory.md#mem-obj-refinement-result
        - memory.md#mem-obj-kernel-manifest
        note: These supply context/reports, not authenticated truth; bounded projections omit much retained
          detail.
      - scope: Compaction boundary, digest fingerprint and retained audit snapshots at host consumers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-compaction-summary
          - memory.md#mem-rte-digest-delivery
          - memory.md#mem-obj-refinement-result
          note: Boundary IDs choose reconstructed window; fingerprint gates digest refresh; applied before/after
            snapshots select rollback restoration.
        records:
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-rte-digest-delivery
        - memory.md#mem-obj-refinement-result
        note: Access/control metadata is separated from advisory content.
      - scope: Changed skill body/program at model/kernel admission
        assessment: known
        findings:
        - value: instruction
          basis: afforded
          records:
          - runtime.md#rt-rte-skill-install
          note: Later skill body supplies model directions.
        records:
        - runtime.md#rt-rte-skill-install
        note: Whole installation route retains afforded evidence in light of the cross-report disagreement;
          arbitrary program effects are not blanket enforcement authority.
      - scope: Opaque checkpoint values and executable payload effects
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-kernel-state
        - memory.md#mem-rte-kernel-revival
        note: Restored values can alter later Python execution, but actual content and consumers are absent.
          Generic execution dependence does not determine a controlled authority for every enclosed value.
      - scope: Included persisted goals, quota parks, autonomous/scheduled wake-up controls, fork transfer
          and child observe/message/recovery alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-daemon-session
        - runtime.md#rt-obj-session-context
        - runtime.md#rt-rte-child-spawn
        - memory.md#mem-rte-branch-navigation
        note: The memory inventory identifies these included alternatives but does not fully trace their
          retained parts, admission or replay. Their authority classification remains uninspected; the
          known routes do not enumerate the whole boundary.
      - scope: Opaque provider-side accumulated state, if any; fixed inference weights are not use-derived
          memory
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-provider-model
        note: Provider caching, adaptation and parameter provenance are uninspected. No authority value
          is inferred from ordinary remote inference or a mutable endpoint. External implementation is
          outside frozen evidence, preventing resolution of this included alternative.
      records:
      - memory.md#mem-obj-harness-entry
      - runtime.md#rt-bap-harness-digest
      - memory.md#mem-rte-digest-delivery
      - memory.md#mem-rte-harness-inspection
      - memory.md#mem-obj-skill-contract
      - memory.md#mem-obj-subagent-entry
      - memory.md#mem-bap-subagent-template
      - runtime.md#rt-obj-factory-machine
      - runtime.md#rt-rte-factory-run
      - runtime.md#rt-bap-machine-guards
      - runtime.md#rt-rte-harness-refine
      - memory.md#mem-obj-refinement-result
      - runtime.md#rt-rte-context-compact
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-rte-branch-navigation
      - runtime.md#rt-obj-session-context
      - memory.md#mem-obj-kernel-manifest
      - runtime.md#rt-rte-skill-install
      - memory.md#mem-obj-kernel-state
      - memory.md#mem-rte-kernel-revival
      - runtime.md#rt-rte-daemon-session
      - runtime.md#rt-rte-child-spawn
      - runtime.md#rt-cmp-provider-model
      note: Knowledge, instruction, learning, ranking, routing, validation and enforcement are attached
        to actual consumers. They do not establish compliance, factual acceptance or benefit. Unresolved
        payload and control consumers prevent complete authority coverage.
    write_agency:
      assessment: partial
      units:
      - scope: Refinement proposal admission, including operator-triggered and automatic review routes
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-harness-refine
          note: Model proposes content; parser/validator/locked apply software admits each permissible
            edit without obligatory per-edit human approval.
        records:
        - runtime.md#rt-rte-harness-refine
        note: Operator scope/focus and factory opt-in do not supply per-edit content approval.
      - scope: Foreground-model direct harness edits through Python
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-python-effects
          note: Model-generated cells supply content and software helpers admit it.
        records:
        - runtime.md#rt-rte-python-effects
        - memory.md#mem-obj-harness-entry
        - memory.md#mem-obj-skill-contract
        - memory.md#mem-obj-subagent-entry
        note: The explicitly model-generated path is known; generic helper callers are separated below.
      - scope: Other direct helper callers, initial populated-store admission and unrestricted raw file
          replacement
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-python-effects
        - memory.md#mem-obj-harness-entry
        note: Caller-authored content is accepted, but generic caller identity does not establish whether
          an explicit human content decision occurred. Initial store control and raw replacement approval
          are also unresolved.
      - scope: Session accumulation, summary commitment and namespace capture
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-obj-session-context
          - runtime.md#rt-rte-context-compact
          - memory.md#mem-obj-compaction-summary
          - memory.md#mem-rte-branch-navigation
          - memory.md#mem-rte-kernel-revival
          - memory.md#mem-obj-refinement-result
          note: Host appends records, commits model summaries and serializes eligible values without per-content
            operator approval.
        records:
        - runtime.md#rt-obj-session-context
        - runtime.md#rt-rte-context-compact
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-rte-branch-navigation
        - memory.md#mem-rte-kernel-revival
        - memory.md#mem-obj-refinement-result
        note: Calling compaction/navigation does not make the resulting model summary manually admitted;
          checkpoint serialization likewise uses software checks.
      - scope: Human-authored and model-authored changed skill/resource files
        assessment: known
        findings:
        - value: manual
          basis: afforded
          records:
          - runtime.md#rt-rte-skill-install
          note: Explicit human supply/edit of retained skill content is an afforded admission route.
        - value: automatic
          basis: afforded
          records:
          - runtime.md#rt-rte-skill-install
          note: Model-authored resource content can reach later discovery without obligatory per-content
            human approval.
        records:
        - runtime.md#rt-rte-skill-install
        note: The supplied route explicitly permits humans to choose/edit content and models to author
          it; discovery is not a mandatory human approval stage.
      - scope: Included persisted goals, quota parks, autonomous/scheduled wake-up controls, fork transfer
          and child observe/message/recovery alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-daemon-session
        - runtime.md#rt-obj-session-context
        - runtime.md#rt-rte-child-spawn
        - memory.md#mem-rte-branch-navigation
        note: The memory inventory identifies these included alternatives but does not fully trace their
          retained parts, admission or replay. Their admission control classification remains uninspected;
          the known routes do not enumerate the whole boundary.
      - scope: Opaque provider-side accumulated state, if any; fixed inference weights are not use-derived
          memory
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-provider-model
        note: Provider caching, adaptation and parameter provenance are uninspected. No admission control
          value is inferred from ordinary remote inference or a mutable endpoint. External implementation
          is outside frozen evidence, preventing resolution of this included alternative.
      records:
      - runtime.md#rt-rte-harness-refine
      - runtime.md#rt-rte-python-effects
      - memory.md#mem-obj-harness-entry
      - memory.md#mem-obj-skill-contract
      - memory.md#mem-obj-subagent-entry
      - runtime.md#rt-obj-session-context
      - runtime.md#rt-rte-context-compact
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-rte-branch-navigation
      - memory.md#mem-rte-kernel-revival
      - memory.md#mem-obj-refinement-result
      - runtime.md#rt-rte-skill-install
      - runtime.md#rt-rte-daemon-session
      - runtime.md#rt-rte-child-spawn
      - runtime.md#rt-cmp-provider-model
      note: Automatic admission is wired for refinement, model cells, summaries and checkpoints; manual
        resource authoring is afforded. Generic caller identity, raw store replacements, initialization
        and untraced controls retain uncertainty.
    curation_operations:
      assessment: partial
      units:
      - scope: Session prefix and abandoned-path summary generation
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - runtime.md#rt-rte-context-compact
          - memory.md#mem-obj-compaction-summary
          - memory.md#mem-rte-branch-navigation
          note: Selected retained messages/previous summaries become smaller durable continuation summaries.
        records:
        - runtime.md#rt-rte-context-compact
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-rte-branch-navigation
        note: Implemented compression combines retained claims into reduced continuation context. Semantic
          fidelity remains unobserved and does not turn compression into evidenced synthesis.
      - scope: Digest and refinement-history projection
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-digest-delivery
          - memory.md#mem-obj-refinement-result
          note: Rendered hints and history projections select/compress existing retained content.
        records:
        - memory.md#mem-rte-digest-delivery
        - memory.md#mem-obj-refinement-result
        note: Selected/clipped entry text and bounded history form reduced representations; index ranking
          alone is not the operation.
      - scope: Harness entry update and audited rollback/delete
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-rte-harness-refine
          - runtime.md#rt-rte-python-effects
          note: Supported update paths replace/revise entry content and version.
        - value: invalidate
          basis: wired
          records:
          - runtime.md#rt-rte-harness-refine
          - memory.md#mem-obj-refinement-result
          note: Delete/rollback withdraws reliance on applied content at future loads while retaining
            before/after audit history.
        records:
        - runtime.md#rt-rte-harness-refine
        - runtime.md#rt-rte-python-effects
        - memory.md#mem-obj-refinement-result
        note: Update revises an existing retained entry; audited withdrawal keeps the edit history, not
          necessarily the withdrawn live entry.
      - scope: Oversized live namespace pruning and checkpoint-budget forgetting
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-obj-kernel-state
          - memory.md#mem-rte-kernel-revival
          - runtime.md#rt-rte-context-compact
          note: Explicit per-variable pruning forgets oversized live retained values; serialization exclusions
            limit retained checkpoint content.
        records:
        - memory.md#mem-obj-kernel-state
        - memory.md#mem-rte-kernel-revival
        - runtime.md#rt-rte-context-compact
        note: Actual pruning deletes names after successful artifact replacement; ordinary skips only
          limit what survives restart.
      - scope: Meaning-changing refinement alternatives
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-harness-refine
        note: The records establish generic model edits and evidence-directed instructions, not whether
          a particular new claim synthesizes beyond inputs or whether near-duplicates are merged. Route
          names and requested benefits do not establish synthesis, dedup or promotion.
      - scope: Changed resource maintenance and initial-store curation
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-skill-install
        - memory.md#mem-obj-harness-entry
        note: Authoring/reload is established, but implemented curate-over-retained-content operations
          and initial maintenance are not resolved.
      - scope: Arbitrary enclosed checkpoint values
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-kernel-state
        note: Serialization is not itself consolidation or synthesis; payload-specific transformations
          are uninspected.
      - scope: Included persisted goals, quota parks, autonomous/scheduled wake-up controls, fork transfer
          and child observe/message/recovery alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-daemon-session
        - runtime.md#rt-obj-session-context
        - runtime.md#rt-rte-child-spawn
        - memory.md#mem-rte-branch-navigation
        note: The memory inventory identifies these included alternatives but does not fully trace their
          retained parts, admission or replay. Their curation classification remains uninspected; the
          known routes do not enumerate the whole boundary.
      - scope: Opaque provider-side accumulated state, if any; fixed inference weights are not use-derived
          memory
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-provider-model
        note: Provider caching, adaptation and parameter provenance are uninspected. No curation value
          is inferred from ordinary remote inference or a mutable endpoint. External implementation is
          outside frozen evidence, preventing resolution of this included alternative.
      records:
      - runtime.md#rt-rte-context-compact
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-rte-branch-navigation
      - memory.md#mem-rte-digest-delivery
      - memory.md#mem-obj-refinement-result
      - runtime.md#rt-rte-harness-refine
      - runtime.md#rt-rte-python-effects
      - memory.md#mem-obj-kernel-state
      - memory.md#mem-rte-kernel-revival
      - runtime.md#rt-rte-skill-install
      - memory.md#mem-obj-harness-entry
      - runtime.md#rt-rte-daemon-session
      - runtime.md#rt-obj-session-context
      - runtime.md#rt-rte-child-spawn
      - runtime.md#rt-cmp-provider-model
      note: Consolidate, evolve, invalidate and decay have local implemented witnesses. No unsupported
        dedup, synthesize or promote value is inferred from refinement doctrine, version increments, primary-key
        checks or lexical ranking. Uninspected alternatives prevent a complete operation inventory.
    read_back_direction:
      assessment: partial
      units:
      - scope: Harness digest to foreground context
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-digest-delivery
          - runtime.md#rt-bap-harness-digest
          note: Boundary/fingerprint-driven rendering supplies a selected digest user turn.
        records:
        - memory.md#mem-rte-digest-delivery
        - runtime.md#rt-bap-harness-digest
        note: Code selects retained hints without a foreground request for those entries.
      - scope: Foreground requested harness get/list/search/overview/snapshot
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-rte-harness-inspection
          note: Caller requests operation/query and receives retained objects or rendering.
        records:
        - memory.md#mem-rte-harness-inspection
        note: Requested returns are pull, not another push because helper code chooses matches.
      - scope: Factory stored specification request and automatic subagent-template resolution
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-obj-factory-machine
          - runtime.md#rt-rte-factory-run
          note: Caller selects a stored factory ID for another run.
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-subagent-entry
          - memory.md#mem-bap-subagent-template
          - runtime.md#rt-rte-factory-run
          note: Factory resolves full stored subagent entries by ID/title and supplies template content
            to children without a child request for that entry.
        records:
        - runtime.md#rt-obj-factory-machine
        - runtime.md#rt-rte-factory-run
        - memory.md#mem-obj-subagent-entry
        - memory.md#mem-bap-subagent-template
        note: The requested machine return/launch is distinct from code selecting full referenced retained
          child templates.
      - scope: Refiner automatic state/history inputs
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-harness-refine
          - memory.md#mem-obj-refinement-result
          note: Automatic current-state and recent-history projections accompany the refiner request.
        records:
        - runtime.md#rt-rte-harness-refine
        - memory.md#mem-obj-refinement-result
        note: Starting refine requests a transformation, not each retained history row. Host supplies
          bounded state/history to planner.
      - scope: Session restore/navigation request and automatic reconstructed summary/tail context
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-obj-session-context
          - runtime.md#rt-rte-daemon-session
          - memory.md#mem-rte-branch-navigation
          note: Caller opening/selecting a session or branch requests retained path context.
        - value: push
          basis: wired
          records:
          - runtime.md#rt-obj-session-context
          - runtime.md#rt-rte-context-compact
          - memory.md#mem-obj-compaction-summary
          - memory.md#mem-rte-branch-navigation
          note: Host rebuild supplies summary-first context and preserved tail to later inference.
        records:
        - runtime.md#rt-obj-session-context
        - runtime.md#rt-rte-daemon-session
        - runtime.md#rt-rte-context-compact
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-rte-branch-navigation
        note: Caller session/branch selection is a request; host context reconstruction selects and supplies
          retained content within that chain.
      - scope: Kernel revival and independent namespace notice
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-kernel-state
          - memory.md#mem-obj-kernel-manifest
          - memory.md#mem-rte-kernel-revival
          note: Host-selected checkpoint restores eligible values before bootstrap and supplies model-facing
            names/loss notice.
        records:
        - memory.md#mem-obj-kernel-state
        - memory.md#mem-obj-kernel-manifest
        - memory.md#mem-rte-kernel-revival
        note: Kernel boot restoration and notice delivery do not require a later cell to request each
          retained value/name.
      - scope: Changed skill inventory and requested full instruction body
        assessment: known
        findings:
        - value: push
          basis: afforded
          records:
          - runtime.md#rt-rte-skill-install
          note: Startup/reload makes available resource inventory part of later session context.
        - value: pull
          basis: afforded
          records:
          - runtime.md#rt-rte-skill-install
          note: Named skill invocation or requested file inspection supplies body detail.
        records:
        - runtime.md#rt-rte-skill-install
        note: Inventory is coarse automatic supply; full body invocation/inspection is requested. Whole-route
          classification stays afforded.
      - scope: Retained completed child results
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-child-spawn
          - workflow.md#wf-rte-builder-report
          note: Parent explicitly re-collects completed child results until deletion.
        records:
        - runtime.md#rt-rte-child-spawn
        - workflow.md#wf-rte-builder-report
        note: Explicit collect is distinct from live factory bindings and status previews.
      - scope: Included persisted goals, quota parks, autonomous/scheduled wake-up controls, fork transfer
          and child observe/message/recovery alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-daemon-session
        - runtime.md#rt-obj-session-context
        - runtime.md#rt-rte-child-spawn
        - memory.md#mem-rte-branch-navigation
        note: The memory inventory identifies these included alternatives but does not fully trace their
          retained parts, admission or replay. Their read-back direction classification remains uninspected;
          the known routes do not enumerate the whole boundary.
      - scope: Opaque provider-side accumulated state, if any; fixed inference weights are not use-derived
          memory
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-provider-model
        note: Provider caching, adaptation and parameter provenance are uninspected. No read-back direction
          value is inferred from ordinary remote inference or a mutable endpoint. External implementation
          is outside frozen evidence, preventing resolution of this included alternative.
      records:
      - memory.md#mem-rte-digest-delivery
      - runtime.md#rt-bap-harness-digest
      - memory.md#mem-rte-harness-inspection
      - runtime.md#rt-obj-factory-machine
      - runtime.md#rt-rte-factory-run
      - memory.md#mem-obj-subagent-entry
      - memory.md#mem-bap-subagent-template
      - runtime.md#rt-rte-harness-refine
      - memory.md#mem-obj-refinement-result
      - runtime.md#rt-obj-session-context
      - runtime.md#rt-rte-daemon-session
      - runtime.md#rt-rte-context-compact
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-rte-branch-navigation
      - memory.md#mem-obj-kernel-state
      - memory.md#mem-obj-kernel-manifest
      - memory.md#mem-rte-kernel-revival
      - runtime.md#rt-rte-skill-install
      - runtime.md#rt-rte-child-spawn
      - workflow.md#wf-rte-builder-report
      - runtime.md#rt-cmp-provider-model
      note: Both pull and push occur at distinct operations, sometimes within one request chain. Live
        factory port bindings alone are not accumulated read-back; retained child result collection is.
        Untraced alternatives prevent a complete direction assessment.
    read_back_signal:
      assessment: partial
      units:
      - scope: Boundary-triggered harness digest entry selection
        assessment: known
        findings:
        - value: inferred-lexical
          basis: wired
          records:
          - memory.md#mem-rte-digest-delivery
          note: Weighted query-term/field overlap selects retained compact entries.
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-digest-delivery
          note: State/flag freshness, per-kind top-three and character/event limits gate which retained
            hints/events are supplied.
        records:
        - memory.md#mem-rte-digest-delivery
        note: Trigger is cold start/resume/compaction or stale/missing digest; goal and recent text terms
          rank retained entries, while availability and clipping bound delivery.
      - scope: Factory automatic stored subagent-template push
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-obj-subagent-entry
          - memory.md#mem-bap-subagent-template
          - runtime.md#rt-rte-factory-run
          note: Actual subagent ID lookup, then title fallback, selects the retained full template copied
            into child tasks.
        records:
        - memory.md#mem-obj-subagent-entry
        - memory.md#mem-bap-subagent-template
        - runtime.md#rt-rte-factory-run
        note: Triggered while resolving the requested machine; its retained reference names select delivered
          full prompt templates.
      - scope: Refiner automatic history/state projection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-harness-refine
          - memory.md#mem-obj-refinement-result
          note: Last-twenty history and per-kind/count/character-limited state overview select inputs
            without semantic matching.
        records:
        - runtime.md#rt-rte-harness-refine
        - memory.md#mem-obj-refinement-result
        note: Trigger is planner request; latest history and bounded overview select retained result summaries
          and current entries.
      - scope: Automatic compaction/branch context reconstruction
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-obj-session-context
          - runtime.md#rt-rte-context-compact
          - memory.md#mem-obj-compaction-summary
          - memory.md#mem-rte-branch-navigation
          note: Window/path position and budget select retained summary, tail and abandoned-path material
            for later context.
        records:
        - runtime.md#rt-obj-session-context
        - runtime.md#rt-rte-context-compact
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-rte-branch-navigation
        note: Trigger is commit/rebuild for the selected path; cut, tail and abandoned-path budget select
          retained summary/context. A stored boundary ID alone does not prove identifier-based push.
      - scope: Checkpoint restore and namespace notice
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-kernel-state
          - memory.md#mem-obj-kernel-manifest
          - memory.md#mem-rte-kernel-revival
          note: Availability, name eligibility and budget filtering supply restored values and name/loss
            reporting; no semantic matcher is established.
        records:
        - memory.md#mem-obj-kernel-state
        - memory.md#mem-obj-kernel-manifest
        - memory.md#mem-rte-kernel-revival
        note: Trigger is artifact-backed boot or post-compaction probe; snapshot target, eligible names
          and size/serialization limits bound retained payload/notice.
      - scope: Changed skill inventory push
        assessment: known
        findings:
        - value: coarse
          basis: afforded
          records:
          - runtime.md#rt-rte-skill-install
          note: Configured resource availability controls inventory supply.
        records:
        - runtime.md#rt-rte-skill-install
        note: Trigger is startup/reload; discovered availability provides names/descriptions/imports.
          A catalog name alone is not identity-matched body delivery.
      - scope: Requested harness detail/search, stored factory lookup, session selection and child collection
          operations
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-harness-inspection
        - runtime.md#rt-rte-factory-run
        - runtime.md#rt-obj-session-context
        - runtime.md#rt-rte-child-spawn
        note: Only the requested-return operations are covered here; independent pushes in those chains
          are separate units.
      - scope: Included persisted goals, quota parks, autonomous/scheduled wake-up controls, fork transfer
          and child observe/message/recovery alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-daemon-session
        - runtime.md#rt-obj-session-context
        - runtime.md#rt-rte-child-spawn
        - memory.md#mem-rte-branch-navigation
        note: The memory inventory identifies these included alternatives but does not fully trace their
          retained parts, admission or replay. Their push selection classification remains uninspected;
          the known routes do not enumerate the whole boundary.
      - scope: Opaque provider-side accumulated state, if any; fixed inference weights are not use-derived
          memory
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-provider-model
        note: Provider caching, adaptation and parameter provenance are uninspected. No push selection
          value is inferred from ordinary remote inference or a mutable endpoint. External implementation
          is outside frozen evidence, preventing resolution of this included alternative.
      records:
      - memory.md#mem-rte-digest-delivery
      - memory.md#mem-obj-subagent-entry
      - memory.md#mem-bap-subagent-template
      - runtime.md#rt-rte-factory-run
      - runtime.md#rt-rte-harness-refine
      - memory.md#mem-obj-refinement-result
      - runtime.md#rt-obj-session-context
      - runtime.md#rt-rte-context-compact
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-rte-branch-navigation
      - memory.md#mem-obj-kernel-state
      - memory.md#mem-obj-kernel-manifest
      - memory.md#mem-rte-kernel-revival
      - runtime.md#rt-rte-skill-install
      - memory.md#mem-rte-harness-inspection
      - runtime.md#rt-rte-child-spawn
      - runtime.md#rt-rte-daemon-session
      - runtime.md#rt-cmp-provider-model
      note: Lexical, coarse and identifier-based pushes are supported on separate selectors. Requested
        search is pull despite lexical ranking. Unresolved push alternatives prevent axis inapplicability
        or complete signal coverage.
    trace_learning:
      assessment: partial
      units:
      - scope: Trajectory-fed refinement to durable harness entry to later foreground/child consumer
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-harness-refine
          - memory.md#mem-rte-digest-delivery
          - memory.md#mem-bap-subagent-template
          note: Recorded session experience feeds automatic durable editing and a later digest/inspection/factory
            consumer.
        records:
        - runtime.md#rt-rte-harness-refine
        - memory.md#mem-obj-harness-entry
        - memory.md#mem-obj-skill-contract
        - memory.md#mem-obj-subagent-entry
        - runtime.md#rt-obj-factory-machine
        - memory.md#mem-rte-digest-delivery
        - memory.md#mem-rte-harness-inspection
        - memory.md#mem-bap-subagent-template
        note: Automatic software admission produces retained behavior-shaping content; no novelty, truth
          acceptance or measured capacity gain is required for this route classification.
      - scope: Compaction summary to later model invocation
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-context-compact
          - memory.md#mem-obj-compaction-summary
          - runtime.md#rt-obj-session-context
          note: Session prefix/previous summary feeds model summary; host retains it and later rebuilt
            context consumes it.
        records:
        - runtime.md#rt-rte-context-compact
        - memory.md#mem-obj-compaction-summary
        - runtime.md#rt-obj-session-context
        note: Compression qualifies because it automatically transforms traces into retained continuation
          guidance; old raw history can also remain.
      - scope: Optional abandoned-branch summary to later selected context
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-branch-navigation
          note: Recorded abandoned-path activity feeds an automatically admitted durable summary consumed
            on rebuilt later context.
        records:
        - memory.md#mem-rte-branch-navigation
        note: Caller choosing summarize is not per-summary content approval; host persists the generated
          summary for later model context.
      - scope: Direct caller edits, changed resources and initialization
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-python-effects
        - runtime.md#rt-rte-skill-install
        - memory.md#mem-obj-harness-entry
        note: These routes can write retained behavior-shaping content, but their original trace inputs
          are not established for every caller. Model authorship alone does not establish trace learning.
      - scope: Namespace capture and arbitrary revived values
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-kernel-state
        - memory.md#mem-rte-kernel-revival
        note: Known capture preserves current values rather than deriving lessons from recorded activity.
          Enclosed values and their producers are uninspected, so no system-wide or payload-wide negative
          is asserted.
      - scope: Included persisted goals, quota parks, autonomous/scheduled wake-up controls, fork transfer
          and child observe/message/recovery alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-daemon-session
        - runtime.md#rt-obj-session-context
        - runtime.md#rt-rte-child-spawn
        - memory.md#mem-rte-branch-navigation
        note: The memory inventory identifies these included alternatives but does not fully trace their
          retained parts, admission or replay. Their qualifying trace-fed writes classification remains
          uninspected; the known routes do not enumerate the whole boundary.
      - scope: Opaque provider-side accumulated state, if any; fixed inference weights are not use-derived
          memory
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-provider-model
        note: Provider caching, adaptation and parameter provenance are uninspected. No qualifying trace-fed
          writes value is inferred from ordinary remote inference or a mutable endpoint. External implementation
          is outside frozen evidence, preventing resolution of this included alternative.
      records:
      - runtime.md#rt-rte-harness-refine
      - memory.md#mem-obj-harness-entry
      - memory.md#mem-obj-skill-contract
      - memory.md#mem-obj-subagent-entry
      - runtime.md#rt-obj-factory-machine
      - memory.md#mem-rte-digest-delivery
      - memory.md#mem-rte-harness-inspection
      - memory.md#mem-bap-subagent-template
      - runtime.md#rt-rte-context-compact
      - memory.md#mem-obj-compaction-summary
      - runtime.md#rt-obj-session-context
      - memory.md#mem-rte-branch-navigation
      - runtime.md#rt-rte-python-effects
      - runtime.md#rt-rte-skill-install
      - memory.md#mem-obj-kernel-state
      - memory.md#mem-rte-kernel-revival
      - runtime.md#rt-rte-daemon-session
      - runtime.md#rt-rte-child-spawn
      - runtime.md#rt-cmp-provider-model
      note: Three wired automatic trace-fed durable summary/edit routes support local yes findings. No
        local no is invented without bounded absence records. Other write inputs and later consumers remain
        unresolved; this is not demonstrated improvement.
    trace_source:
      assessment: partial
      units:
      - scope: Original conversational and tool activity supplied to harness refinement
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - runtime.md#rt-rte-harness-refine
          - runtime.md#rt-obj-session-context
          note: Recorded conversational turns, tasks and corrections feed the automatic harness edit.
        - value: tool-traces
          basis: wired
          records:
          - runtime.md#rt-rte-harness-refine
          - runtime.md#rt-obj-session-context
          note: Recorded tool results and tool activity in the supplied session experience feed refinement.
        records:
        - runtime.md#rt-rte-harness-refine
        - runtime.md#rt-obj-session-context
        note: Recorded human/model messages and tool requests/results are explicitly included; previous
          derived/custom context and external-origin warrant are separately unresolved.
      - scope: Original session prefix/split-turn material supplied to compaction
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - runtime.md#rt-rte-context-compact
          - memory.md#mem-obj-compaction-summary
          - runtime.md#rt-obj-session-context
          note: Recorded conversation supplies the continuation summary input.
        - value: tool-traces
          basis: wired
          records:
          - runtime.md#rt-rte-context-compact
          - memory.md#mem-obj-compaction-summary
          - runtime.md#rt-obj-session-context
          note: Included recorded tool calls/results and file-operation experience supply summary input.
        records:
        - runtime.md#rt-rte-context-compact
        - memory.md#mem-obj-compaction-summary
        - runtime.md#rt-obj-session-context
        note: Message content, not the compaction event envelope, determines origin.
      - scope: Original abandoned-path messages supplied to optional branch summary
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-rte-branch-navigation
          - runtime.md#rt-obj-session-context
          note: Recorded abandoned-path conversation feeds retained branch summary.
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-rte-branch-navigation
          - runtime.md#rt-obj-session-context
          note: Recorded tool/file-operation activity in the selected path supplies summary input.
        records:
        - memory.md#mem-rte-branch-navigation
        - runtime.md#rt-obj-session-context
        note: Newest-first abandoned-path messages and accumulated file-operation tracking are recorded
          activity.
      - scope: Mixed derived/custom context within qualifying refinement and summary inputs
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-harness-refine
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-rte-branch-navigation
        note: Previous summaries, derived/custom rows and externally supplied content can occur. The records
          do not fully enumerate their original inputs or establish event-stream or linked states/actions/outcomes
          lineage. Calling a transcript a trajectory does not alone establish trajectories.
      - scope: Potential qualifying direct/resource/initial-content and enclosed namespace updates
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-python-effects
        - runtime.md#rt-rte-skill-install
        - memory.md#mem-obj-harness-entry
        - memory.md#mem-obj-kernel-state
        note: Trace-fed production is unresolved on these paths, so their trace source cannot be declared
          inapplicable based on the known summaries.
      - scope: Included persisted goals, quota parks, autonomous/scheduled wake-up controls, fork transfer
          and child observe/message/recovery alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-daemon-session
        - runtime.md#rt-obj-session-context
        - runtime.md#rt-rte-child-spawn
        - memory.md#mem-rte-branch-navigation
        note: The memory inventory identifies these included alternatives but does not fully trace their
          retained parts, admission or replay. Their trace origin classification remains uninspected;
          the known routes do not enumerate the whole boundary.
      - scope: Opaque provider-side accumulated state, if any; fixed inference weights are not use-derived
          memory
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-provider-model
        note: Provider caching, adaptation and parameter provenance are uninspected. No trace origin value
          is inferred from ordinary remote inference or a mutable endpoint. External implementation is
          outside frozen evidence, preventing resolution of this included alternative.
      records:
      - runtime.md#rt-rte-harness-refine
      - runtime.md#rt-obj-session-context
      - runtime.md#rt-rte-context-compact
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-rte-branch-navigation
      - runtime.md#rt-rte-python-effects
      - runtime.md#rt-rte-skill-install
      - memory.md#mem-obj-harness-entry
      - memory.md#mem-obj-kernel-state
      - runtime.md#rt-rte-daemon-session
      - runtime.md#rt-rte-child-spawn
      - runtime.md#rt-cmp-provider-model
      note: Session-logs and tool-traces have positive original-content warrants on qualifying routes.
        Mixed/custom inputs and unresolved writes prevent complete source coverage; no event-streams or
        trajectories value is inferred from route labels or event serialization.
---

# Prime Agent memory profile

## Comparison rationale

This profile classifies the supplied accepted records, not the source checkout. No source files were read for this job. Evidence is implementation or doctrine/design; no finding claims observed operation, causal support, fidelity or benefit. The retained inventory remains partial because the memory account includes incompletely traced controls and recovery alternatives as well as unknown initial content and opaque checkpoint/provider state. See [RT-RTE-daemon-session](runtime.md#rt-rte-daemon-session), [RT-OBJ-session-context](runtime.md#rt-obj-session-context), [MEM-OBJ-harness-entry](memory.md#mem-obj-harness-entry), [MEM-OBJ-kernel-state](memory.md#mem-obj-kernel-state) and [RT-CMP-provider-model](runtime.md#rt-cmp-provider-model).

Reconciliation establishes no supersessions. The epistemic factual/policy groupings overlap the finer memory objects without adding independent objects or stronger evidence. Session summary, payload and manifest remain separate parts of valid runtime containers. This profile therefore cites each actual part and consumer rather than counting overlapping groupings as additional memory. See [EPI-OBJ-harness-memory](epistemic.md#epi-obj-harness-memory), [EPI-OBJ-harness-policy](epistemic.md#epi-obj-harness-policy), [MEM-OBJ-compaction-summary](memory.md#mem-obj-compaction-summary), [MEM-OBJ-kernel-state](memory.md#mem-obj-kernel-state) and [MEM-OBJ-kernel-manifest](memory.md#mem-obj-kernel-manifest).

The unresolved resource-admission disagreement does not justify upgrading the whole installation route. Its findings retain the runtime's afforded basis; separately recorded current-session body expansion does not prove complete authoring, discovery, installation and reload wiring. Human resource authoring supports manual admission only on the explicit human-content path. Model-generated edits and refinement remain automatic even when a human starts the task or enables factory. Generic helper callers and unknown initial stores are not silently made manual or automatic. See [RT-RTE-skill-install](runtime.md#rt-rte-skill-install), [RT-RTE-python-effects](runtime.md#rt-rte-python-effects) and [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine).

Compaction and optional abandoned-path summarization qualify as trace learning: recorded activity feeds automatic retained summaries with later model consumers. Consolidation describes the implemented reduction, not verified semantic equivalence. The epistemic assessment of summary meaning remains indeterminate; it neither removes the wired summary path nor establishes synthesis. Refiner edits likewise support evolution and trace learning without warranting novel claims, successful criticism or improved capacity. See [RT-RTE-context-compact](runtime.md#rt-rte-context-compact), [MEM-OBJ-compaction-summary](memory.md#mem-obj-compaction-summary), [MEM-RTE-branch-navigation](memory.md#mem-rte-branch-navigation) and [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine).

Session-logs and tool-traces classify original recorded content, not serialization or the route's trajectory label. Mixed derived/custom inputs remain unresolved. Namespace capture preserves values, whereas manifest/notice reports names; neither the display nor a model's ability to create values resolves the opaque payload's original content or trace-fed production. No absence record supports a blanket trace-learning no. See [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine), [MEM-OBJ-compaction-summary](memory.md#mem-obj-compaction-summary), [MEM-OBJ-kernel-state](memory.md#mem-obj-kernel-state) and [MEM-RTE-kernel-revival](memory.md#mem-rte-kernel-revival).

Read-back separates requests from unsolicited selection within a chain. Requested harness search, stored-machine lookup and child collection are pull; automatic digest, template resolution, planner history and reconstruction are push. Lexical ranking supplies both ranking authority and a lexical push signal only on the automatic digest path. An actual subagent ID/title match selects full child templates; names on catalogs, checkpoints or requested objects alone do not establish identifier push. See [MEM-RTE-digest-delivery](memory.md#mem-rte-digest-delivery), [MEM-RTE-harness-inspection](memory.md#mem-rte-harness-inspection), [MEM-OBJ-subagent-entry](memory.md#mem-obj-subagent-entry), [MEM-BAP-subagent-template](memory.md#mem-bap-subagent-template) and [RT-RTE-child-spawn](runtime.md#rt-rte-child-spawn).

The audit retains reasons and snapshots while automatic planner/digest readers receive projections. Those projections support consolidation and knowledge at their actual consumers, not complete reason read-back or validation of expected outcomes. Fingerprint freshness controls delivery, not endorsement; query drift alone does not force reselection. Delete/rollback changes future loads without recalling delivered copies. See [MEM-OBJ-refinement-result](memory.md#mem-obj-refinement-result), [MEM-RTE-digest-delivery](memory.md#mem-rte-digest-delivery) and [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest).

Machine guards supply code-level validation/enforcement and routing, separately from model-interpreted task instructions. Static built-in machine prompts and ordinary current-run verdict/port state are not counted as use-derived memory merely because they influence progression. Completed retained child results do have explicit later collection; builder status remains a preview and does not establish full report delivery. See [RT-OBJ-factory-machine](runtime.md#rt-obj-factory-machine), [RT-BAP-machine-guards](runtime.md#rt-bap-machine-guards), [EPI-RTE-port-capture](epistemic.md#epi-rte-port-capture) and [WF-RTE-builder-report](workflow.md#wf-rte-builder-report).
