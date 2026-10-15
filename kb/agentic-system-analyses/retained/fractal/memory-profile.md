---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Fractal memory comparison: retained session projections, detailed traces, workspace guidance,
  configuration and startup cache at the frozen revision.'
run-id: AAS-2026-10-14-fractal-ee03010af4c2-01
source-identity: https://github.com/trampoline-ai/fractal
reviewed-boundary: 6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385
memory-comparison:
  version: 2
  scope: Fractal-retained summary, bounded detailed history including opaque RunTrace, usage parts, their
    checkpoint admission/recovery and later model/UI routes; changed root workspace guidance and its reload;
    operator-changed provider/default configuration and later resolution; accumulated release-notice cache
    and later fallback. Includes unresolved caller-supplied summary/history alternatives at the direct
    Python API as afforded consumption, not invented persistence. Excludes shipped static instructions,
    arbitrary application work products without an established later memory consumer, external provider
    weights/state, SBX contents, PredictRLM internal compaction/recursive frames and release artifacts.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Summary, detailed history including opaque RunTrace, and usage checkpoint parts
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-session-summary
          - memory.md#mem-obj-session-history
          - memory.md#mem-obj-turn-usage
          - memory.md#mem-rte-checkpoint-update
          note: All three parts persist in session JSON files and live in Pydantic objects. Opaque trace
            semantics do not make its visible checkpoint substrate unknown.
        - value: in-memory
          basis: wired
          records: *id001
          note: All three parts persist in session JSON files and live in Pydantic objects. Opaque trace
            semantics do not make its visible checkpoint substrate unknown.
        records: *id001
        note: All three parts persist in session JSON files and live in Pydantic objects. Opaque trace
          semantics do not make its visible checkpoint substrate unknown.
      - scope: Root AGENTS.md retained guidance
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id002
          - runtime.md#rt-bap-workspace-guidance
          note: The loader rereads a mutable workspace file; no repository-backed retention requirement
            is established.
        records: *id002
        note: The loader rereads a mutable workspace file; no repository-backed retention requirement
          is established.
      - scope: Changed provider/default settings
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id003
          - runtime.md#rt-rte-config-change
          note: TOML files retain settings for later launch resolution; live selected adapters are not
            a trained-memory store.
        records: *id003
        note: TOML files retain settings for later launch resolution; live selected adapters are not a
          trained-memory store.
      - scope: Version notice cache
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id004
          - epistemic.md#epi-obj-version-cache
          - epistemic.md#epi-rte-version-notice
          note: A config-directory JSON file retains latest, fetched_at and install_id for later startup.
        records: *id004
        note: A config-directory JSON file retains latest, fetched_at and install_id for later startup.
      - scope: Direct API supplied summary/history retention
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-direct-agent
        note: The adapter accepts supplied context but does not persist it. Caller retention and initial
          substrate are unspecified; this afforded alternative cannot be assigned the checkpoint substrate.
      records:
      - memory.md#mem-obj-session-summary
      - memory.md#mem-obj-session-history
      - memory.md#mem-obj-turn-usage
      - memory.md#mem-rte-checkpoint-update
      - runtime.md#rt-bap-workspace-guidance
      - runtime.md#rt-rte-config-change
      - epistemic.md#epi-obj-version-cache
      - epistemic.md#epi-rte-version-notice
      - runtime.md#rt-rte-direct-agent
      note: Session parts, root guidance, configuration and version cache have inspected file retention
        and live host objects. The direct API permits caller-supplied context without establishing its
        retention substrate.
    representational_form:
      assessment: partial
      units:
      - scope: Summary messages, responses and errors at model and conversation readers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id005
          - memory.md#mem-obj-session-summary
          - memory.md#mem-bap-summary-context
          note: Copied prose supplies interpreted conversational context even when stored inside structured
            JSON or delivered in a signature.
        records: *id005
        note: Copied prose supplies interpreted conversational context even when stored inside structured
          JSON or delivered in a signature.
      - scope: Summary/status/count fields and TurnUsage at deterministic host consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id006
          - memory.md#mem-obj-session-summary
          - memory.md#mem-obj-turn-usage
          note: IDs, statuses and numerical accounting are localized fields processed by fixed rendering
            and aggregation rules.
        records: *id006
        note: IDs, statuses and numerical accounting are localized fields processed by fixed rendering
          and aggregation rules.
      - scope: Detailed-history messages/errors at exact-recall consumer
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id007
          - memory.md#mem-obj-session-history
          - memory.md#mem-rte-session-context
          note: Message and error strings remain interpreted language; Python inspection of supplied detail
            is afforded rather than observed.
        records: *id007
        note: Message and error strings remain interpreted language; Python inspection of supplied detail
          is afforded rather than observed.
      - scope: Detailed-history IDs, timestamps and file/command lists at host serialization and selection
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id008
          - memory.md#mem-obj-session-history
          - memory.md#mem-rte-session-reload
          note: Fixed field, schema and recency rules make these metadata symbolic; arbitrary command
            semantics inside external trace content are not classified here.
        records: *id008
        note: Fixed field, schema and recency rules make these metadata symbolic; arbitrary command semantics
          inside external trace content are not classified here.
      - scope: Opaque RunTrace contents at delegated exact-recall consumer
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-history
        - memory.md#mem-rte-session-context
        note: The dependency defines the payload. Host typing and readable summary do not classify all
          consumed trace reasoning, code, results or numerical representations.
      - scope: Root guidance at the model-facing signature
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id009
          - runtime.md#rt-bap-workspace-guidance
          note: Root AGENTS.md is interpreted instruction prose, not an executor permission object.
        records: *id009
        note: Root AGENTS.md is interpreted instruction prose, not an executor permission object.
      - scope: Configuration and version cache at host resolvers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id010
          - runtime.md#rt-rte-config-change
          - epistemic.md#epi-obj-version-cache
          - epistemic.md#epi-rte-version-notice
          note: TOML settings and cache identifiers/timestamps have fixed host interpretation; they are
            not delivered as model instruction prose.
        records: *id010
        note: TOML settings and cache identifiers/timestamps have fixed host interpretation; they are
          not delivered as model instruction prose.
      - scope: Direct API supplied history and rendered summary initial material
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-direct-agent
        note: Rendered summary has a text delivery channel, but caller payload contents and derivation
          are unspecified; full mixed history form cannot be established.
      records:
      - memory.md#mem-obj-session-summary
      - memory.md#mem-bap-summary-context
      - memory.md#mem-obj-turn-usage
      - memory.md#mem-obj-session-history
      - memory.md#mem-rte-session-context
      - memory.md#mem-rte-session-reload
      - runtime.md#rt-bap-workspace-guidance
      - runtime.md#rt-rte-config-change
      - epistemic.md#epi-obj-version-cache
      - epistemic.md#epi-rte-version-notice
      - runtime.md#rt-rte-direct-agent
      note: Known text and host fields are split by consumption. The external RunTrace payload and generic
        direct-API context leave included forms unresolved; no model-weight form is inferred.
    lineage:
      assessment: partial
      units:
      - scope: Host-created summary counts/status, detailed operation observations and usage
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id011
          - memory.md#mem-obj-session-summary
          - memory.md#mem-obj-session-history
          - memory.md#mem-obj-turn-usage
          - memory.md#mem-rte-checkpoint-update
          - epistemic.md#epi-rte-event-projection
          note: The host extracts execution observations and trace accounting into retained fields; this
            is trace-extracted lineage, not model-authored semantic lessons.
        records: *id011
        note: The host extracts execution observations and trace accounting into retained fields; this
          is trace-extracted lineage, not model-authored semantic lessons.
      - scope: Copied caller messages and returned response strings entering checkpoint
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id012
          - memory.md#mem-obj-session-summary
          - memory.md#mem-rte-checkpoint-update
          note: These contents are imported into host state without semantic condensation. Generic caller
            identity does not establish human authorship, and external response generation is not reconstructed.
        records: *id012
        note: These contents are imported into host state without semantic condensation. Generic caller
          identity does not establish human authorship, and external response generation is not reconstructed.
      - scope: Original production of retained RunTrace contents
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-history
        note: Result/exception traces are acquired, but dependency-owned original production and complete
          internal provenance remain unspecified.
      - scope: Reloaded root guidance
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - runtime.md#rt-bap-workspace-guidance
          note: The loader imports retained root file text into a later signature; this does not establish
            how that text was first authored.
        records:
        - runtime.md#rt-bap-workspace-guidance
        note: File-to-signature import is known. Initial author and any model- or externally edited derivation
          are unresolved.
      - scope: Selected configuration settings
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id013
          - runtime.md#rt-rte-config-change
          note: The operator supplies or replaces symbolic selections through commands/setup. This is
            authored configuration, not trace-extracted adaptation.
        records: *id013
        note: The operator supplies or replaces symbolic selections through commands/setup. This is authored
          configuration, not trace-extracted adaptation.
      - scope: Website latest-release assertion retained in cache
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id014
          - epistemic.md#epi-obj-version-cache
          - epistemic.md#epi-rte-version-notice
          note: The latest identifier is imported from website JSON; host timestamping does not confer
            source warrant.
        records: *id014
        note: The latest identifier is imported from website JSON; host timestamping does not confer source
          warrant.
      - scope: Direct API supplied summary/history provenance
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-direct-agent
        note: Caller-provided context lacks established initialization and derivation; the visible adapter
          cannot classify those routes.
      records:
      - memory.md#mem-obj-session-summary
      - memory.md#mem-obj-session-history
      - memory.md#mem-obj-turn-usage
      - memory.md#mem-rte-checkpoint-update
      - epistemic.md#epi-rte-event-projection
      - runtime.md#rt-bap-workspace-guidance
      - runtime.md#rt-rte-config-change
      - epistemic.md#epi-obj-version-cache
      - epistemic.md#epi-rte-version-notice
      - runtime.md#rt-rte-direct-agent
      note: Host projections and imports have supported derivation paths. Generic caller origin, arbitrary
        workspace edits, externally produced traces and direct-API initialization prevent a complete provenance
        inventory.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Summary at later PredictRLM context consumer
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id015
          - memory.md#mem-obj-session-summary
          - memory.md#mem-bap-summary-context
          - memory.md#mem-rte-session-context
          - workflow.md#wf-rte-audit-repair
          note: Prior requests/results/status/counts supply trajectory context and advice for subsequent
            work. Placement in an instruction docstring alone does not turn historical responses into
            standing directions or prove reliance.
        records: *id015
        note: Prior requests/results/status/counts supply trajectory context and advice for subsequent
          work. Placement in an instruction docstring alone does not turn historical responses into standing
          directions or prove reliance.
      - scope: Detailed history at afforded model Python recall consumer
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records: &id016
          - memory.md#mem-obj-session-history
          - memory.md#mem-rte-session-context
          note: The supplied tail offers exact-recall reference material. Fractal wires delivery; actual
            inspection is only afforded and is not observed.
        records: *id016
        note: The supplied tail offers exact-recall reference material. Fractal wires delivery; actual
          inspection is only afforded and is not observed.
      - scope: Additional authority of opaque RunTrace internals
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-history
        - memory.md#mem-rte-session-context
        note: No accepted record identifies all interpreted trace parts or their exact dependency consumers;
          blanket instruction, learning or enforcement authority cannot be assigned.
      - scope: Usage and retained conversation at later UI/accounting readers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id017
          - memory.md#mem-obj-session-summary
          - memory.md#mem-obj-turn-usage
          - memory.md#mem-rte-session-reload
          note: Retained fields provide information for conversation display and cumulative usage, not
            an action-approval barrier.
        records: *id017
        note: Retained fields provide information for conversation display and cumulative usage, not an
          action-approval barrier.
      - scope: Retained root guidance at signature consumer
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id018
          - runtime.md#rt-bap-workspace-guidance
          note: The model is asked to follow root guidance subject to the current request; no filesystem
            enforcement follows from that instruction policy.
        records: *id018
        note: The model is asked to follow root guidance subject to the current request; no filesystem
          enforcement follows from that instruction policy.
      - scope: Retained provider/default configuration at later launch resolution
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id019
          - runtime.md#rt-rte-config-change
          note: Settings select adapters and execution defaults. Routing is not parameter learning or
            task-answer validation.
        records: *id019
        note: Settings select adapters and execution defaults. Routing is not parameter learning or task-answer
          validation.
      - scope: Cached release identifier at later notice consumer
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id020
          - epistemic.md#epi-obj-version-cache
          - epistemic.md#epi-rte-version-notice
          note: The cached assertion supports an advisory upgrade notice, not automatic installation or
            a quality verdict.
        records: *id020
        note: The cached assertion supports an advisory upgrade notice, not automatic installation or
          a quality verdict.
      - scope: Direct API supplied context at unspecified later consumer
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-direct-agent
        note: Construction affords consumption but does not establish a separately wired later caller,
          content semantics or all authority paths.
      records:
      - memory.md#mem-obj-session-summary
      - memory.md#mem-bap-summary-context
      - memory.md#mem-rte-session-context
      - workflow.md#wf-rte-audit-repair
      - memory.md#mem-obj-session-history
      - memory.md#mem-obj-turn-usage
      - memory.md#mem-rte-session-reload
      - runtime.md#rt-bap-workspace-guidance
      - runtime.md#rt-rte-config-change
      - epistemic.md#epi-obj-version-cache
      - epistemic.md#epi-rte-version-notice
      - runtime.md#rt-rte-direct-agent
      note: Authority is assigned at actual later consumers, not from container names or prompt placement.
        Opaque trace semantics and direct-API initialization leave possible additional forces unresolved.
    write_agency:
      assessment: partial
      units:
      - scope: Pending/final checkpoint admission, counts/status/usage projection
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id021
          - memory.md#mem-rte-checkpoint-update
          note: Software admits caller/model/event contents and finalizes matching turns without a per-content
            human approval; launching a task does not make these admissions manual.
        records: *id021
        note: Software admits caller/model/event contents and finalizes matching turns without a per-content
          human approval; launching a task does not make these admissions manual.
      - scope: Session load rejection and empty-state replacement
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id022
          - memory.md#mem-rte-session-reload
          note: Schema/JSON/ID checks and recovery code admit or replace state automatically; requesting
            an ID is selection, not content approval.
        records: *id022
        note: Schema/JSON/ID checks and recovery code admit or replace state automatically; requesting
          an ID is selection, not content approval.
      - scope: Provider/default settings supplied by operator command or setup
        assessment: known
        findings:
        - value: manual
          basis: wired
          records: &id023
          - runtime.md#rt-rte-config-change
          note: The operator explicitly chooses settings to save or replace. Software validity checks
            do not remove this per-setting operator decision.
        records: *id023
        note: The operator explicitly chooses settings to save or replace. Software validity checks do
          not remove this per-setting operator decision.
      - scope: Website assertion and cache metadata admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id024
          - epistemic.md#epi-obj-version-cache
          - epistemic.md#epi-rte-version-notice
          note: Network/shape/fallback code writes cache contents without operator content approval.
        records: *id024
        note: Network/shape/fallback code writes cache contents without operator content approval.
      - scope: Model editing of retained root guidance
        assessment: partial
        findings:
        - value: automatic
          basis: afforded
          records:
          - runtime.md#rt-bap-workspace-guidance
          - runtime.md#rt-rte-headless-turn
          note: Delegated task editing can change root guidance without per-edit human approval; this
            is an afforded path, not observed guidance revision.
        records:
        - runtime.md#rt-bap-workspace-guidance
        - runtime.md#rt-rte-headless-turn
        note: The mutable-workspace route affords a model edit without per-edit veto, but no dedicated
          guidance write or instance is established, and external editing control remains unknown.
      - scope: Generic caller message origination and direct-API context initialization
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-summary
        - runtime.md#rt-rte-direct-agent
        note: Caller identity does not prove a human per-content decision. Known automatic checkpoint
          admission does not resolve how caller-supplied material was initialized.
      records:
      - memory.md#mem-rte-checkpoint-update
      - memory.md#mem-rte-session-reload
      - runtime.md#rt-rte-config-change
      - epistemic.md#epi-obj-version-cache
      - epistemic.md#epi-rte-version-notice
      - runtime.md#rt-bap-workspace-guidance
      - runtime.md#rt-rte-headless-turn
      - memory.md#mem-obj-session-summary
      - runtime.md#rt-rte-direct-agent
      note: Checkpoint, recovery and cache admissions are software decisions. Configuration explicitly
        takes operator selections. Human content control is unresolved for generic input and open workspace/direct-API
        alternatives.
    curation_operations:
      assessment: partial
      units:
      - scope: Existing pending summary/history turn finalization
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id025
          - memory.md#mem-rte-checkpoint-update
          note: Matching existing turn IDs receive final status/response/accounting/trace fields, revising
            the retained entry rather than merely adding an unrelated item.
        records: *id025
        note: Matching existing turn IDs receive final status/response/accounting/trace fields, revising
          the retained entry rather than merely adding an unrelated item.
      - scope: Detailed-history tail eviction
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id026
          - memory.md#mem-obj-session-history
          - memory.md#mem-rte-session-context
          - memory.md#mem-rte-checkpoint-update
          note: Older retained detailed turns are removed beyond the 20-entry recency tail. This is decay
            by forgetting; the accumulating summary does not restore evicted traces.
        records: *id026
        note: Older retained detailed turns are removed beyond the 20-entry recency tail. This is decay
          by forgetting; the accumulating summary does not restore evicted traces.
      - scope: Previously retained provider/default settings replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id027
          - runtime.md#rt-rte-config-change
          note: Set/unset/reset or setup replacement revises existing configuration entries; it is evolution,
            not learned optimization.
        records: *id027
        note: Set/unset/reset or setup replacement revises existing configuration entries; it is evolution,
          not learned optimization.
      - scope: Cached latest-release entry replacement and fallback expiry
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id028
          - epistemic.md#epi-obj-version-cache
          - epistemic.md#epi-rte-version-notice
          note: Fresh fetch overwrites latest, while the one-day fallback rule stops relying on old cache
            contents. Replacement is evolution and fallback expiry is decay of eligibility.
        - value: decay
          basis: wired
          records: *id028
          note: Fresh fetch overwrites latest, while the one-day fallback rule stops relying on old cache
            contents. Replacement is evolution and fallback expiry is decay of eligibility.
        records: *id028
        note: Fresh fetch overwrites latest, while the one-day fallback rule stops relying on old cache
          contents. Replacement is evolution and fallback expiry is decay of eligibility.
      - scope: Summary activity-count projection of retained turn experience
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id029
          - memory.md#mem-obj-session-summary
          - memory.md#mem-rte-checkpoint-update
          - epistemic.md#epi-rte-summary-render
          note: Host field selection reduces detailed operation lists to counts in the durable summary,
            while recent detail remains retained separately. This consolidates existing activity information,
            not response meaning or novel lessons.
        records: *id029
        note: Host field selection reduces detailed operation lists to counts in the durable summary,
          while recent detail remains retained separately. This consolidates existing activity information,
          not response meaning or novel lessons.
      - scope: Root guidance transformations and opaque direct-API/trace processing
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-bap-workspace-guidance
        - runtime.md#rt-rte-direct-agent
        - memory.md#mem-obj-session-history
        note: Open task editing and dependency-defined payloads do not identify a specific implemented
          transformation over retained guidance/history. No dedup, promote or synthesis completeness claim
          follows.
      records:
      - memory.md#mem-rte-checkpoint-update
      - memory.md#mem-obj-session-history
      - memory.md#mem-rte-session-context
      - runtime.md#rt-rte-config-change
      - epistemic.md#epi-obj-version-cache
      - epistemic.md#epi-rte-version-notice
      - memory.md#mem-obj-session-summary
      - epistemic.md#epi-rte-summary-render
      - runtime.md#rt-bap-workspace-guidance
      - runtime.md#rt-rte-direct-agent
      note: The detailed-tail eviction and existing-state replacements are implemented. Opaque trace processing
        and unconstrained workspace/API transformations prevent a complete curation inventory. No semantic
        lesson synthesis is inferred.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested session-ID reload, session listing and usage access
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id030
          - memory.md#mem-rte-session-reload
          - memory.md#mem-obj-turn-usage
          - workflow.md#wf-rte-audit-repair
          note: The caller requests retained state or accounting; fulfilling that request is pull, not
            another push because code returns it.
        records: *id030
        note: The caller requests retained state or accounting; fulfilling that request is pull, not another
          push because code returns it.
      - scope: Subsequent turn summary/history handoff
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id031
          - memory.md#mem-rte-session-context
          - memory.md#mem-obj-session-summary
          - memory.md#mem-obj-session-history
          note: Submit automatically supplies all retained summary turns and the recent detailed tail
            without a separate request for these memory parts.
        records: *id031
        note: Submit automatically supplies all retained summary turns and the recent detailed tail without
          a separate request for these memory parts.
      - scope: Foreground exact-detail lookup within supplied history
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records: &id032
          - memory.md#mem-obj-session-history
          - memory.md#mem-rte-session-context
          note: The delegated model is directed to inspect retained history from Python when it wants
            details. That requested inspection is an afforded pull, separate from host push delivery.
        records: *id032
        note: The delegated model is directed to inspect retained history from Python when it wants details.
          That requested inspection is an afforded pull, separate from host push delivery.
      - scope: Root guidance reread on agent invocation
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id033
          - runtime.md#rt-bap-workspace-guidance
          note: The loader supplies retained root text on each call without a separate consumer retrieval
            request.
        records: *id033
        note: The loader supplies retained root text on each call without a separate consumer retrieval
          request.
      - scope: Configuration resolution and cached release fallback on later launches
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id034
          - runtime.md#rt-rte-config-change
          - epistemic.md#epi-rte-version-notice
          note: Host launch/startup automatically consumes retained settings and eligible cached latest
            information.
        records: *id034
        note: Host launch/startup automatically consumes retained settings and eligible cached latest
          information.
      - scope: Direct API supplied context across consumer invocations
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-direct-agent
        note: The adapter offers caller input consumption, not established persistence or a later memory
          route; whether a particular later caller requests or receives retained parts is unspecified.
      records:
      - memory.md#mem-rte-session-reload
      - memory.md#mem-obj-turn-usage
      - workflow.md#wf-rte-audit-repair
      - memory.md#mem-rte-session-context
      - memory.md#mem-obj-session-summary
      - memory.md#mem-obj-session-history
      - runtime.md#rt-bap-workspace-guidance
      - runtime.md#rt-rte-config-change
      - epistemic.md#epi-rte-version-notice
      - runtime.md#rt-rte-direct-agent
      note: Explicit session and accounting requests are pull; subsequent automatic context, guidance,
        configuration and cache supply are push. A separate later consumer for generic direct-API input
        remains unresolved.
    read_back_signal:
      assessment: partial
      units:
      - scope: Automatic summary/history push on submit
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id035
          - memory.md#mem-rte-session-context
          - memory.md#mem-obj-session-history
          - memory.md#mem-obj-session-summary
          note: 'Trigger: later submit. Input: selected session state. Parts: every summary turn plus
            the latest 20 history entries, including pending turn. Coarse session/recency selection is
            not semantic similarity or identity-matched subset delivery.'
        records: *id035
        note: 'Trigger: later submit. Input: selected session state. Parts: every summary turn plus the
          latest 20 history entries, including pending turn. Coarse session/recency selection is not semantic
          similarity or identity-matched subset delivery.'
      - scope: Root guidance push on agent call
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id036
          - runtime.md#rt-bap-workspace-guidance
          note: 'Trigger: invocation. Input: presence/readability of root AGENTS.md. Part: whole text
            or its 20,000-character prefix. A fixed filename alone is not targeted identity-matched push.'
        records: *id036
        note: 'Trigger: invocation. Input: presence/readability of root AGENTS.md. Part: whole text or
          its 20,000-character prefix. A fixed filename alone is not targeted identity-matched push.'
      - scope: Configuration and version-cache host push
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id037
          - runtime.md#rt-rte-config-change
          - epistemic.md#epi-rte-version-notice
          note: 'Triggers: launch resolution/startup fallback. Inputs: fixed configuration layers and
            cache availability/age. Parts: applicable settings or cached latest identifier. Precedence
            and TTL are coarse eligibility rules.'
        records: *id037
        note: 'Triggers: launch resolution/startup fallback. Inputs: fixed configuration layers and cache
          availability/age. Parts: applicable settings or cached latest identifier. Precedence and TTL
          are coarse eligibility rules.'
      - scope: Requested session reload/list/usage and foreground detail inspection
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-session-reload
        - memory.md#mem-obj-turn-usage
        - memory.md#mem-obj-session-history
        - memory.md#mem-rte-session-context
        note: These are pull operations; their request IDs or model lookup choices do not classify a push
          signal. Other included push operations remain separately assessed.
      - scope: Direct API caller selection for later supplied memory
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-direct-agent
        note: No independently established later consumer/selector is recorded; cannot classify its signal
          or declare this alternative pull-only.
      records:
      - memory.md#mem-rte-session-context
      - memory.md#mem-obj-session-history
      - memory.md#mem-obj-session-summary
      - runtime.md#rt-bap-workspace-guidance
      - runtime.md#rt-rte-config-change
      - epistemic.md#epi-rte-version-notice
      - memory.md#mem-rte-session-reload
      - memory.md#mem-obj-turn-usage
      - runtime.md#rt-rte-direct-agent
      note: Inspected push selectors use availability, recency, fixed root location, configuration precedence
        and TTL. Requested session IDs are not identifier-based push. Direct-API later selection is unresolved.
    trace_learning:
      assessment: partial
      units:
      - scope: Trace-fed derived checkpoint context
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id038
          - memory.md#mem-rte-checkpoint-update
          - memory.md#mem-obj-session-summary
          - memory.md#mem-rte-session-context
          - epistemic.md#epi-rte-event-projection
          note: Hook observations and trace status/accounting automatically produce durable summary context
            for a later model invocation. This qualifies even though responses are not semantically summarized
            and no general lesson algorithm exists.
        records: *id038
        note: Hook observations and trace status/accounting automatically produce durable summary context
          for a later model invocation. This qualifies even though responses are not semantically summarized
          and no general lesson algorithm exists.
      - scope: Raw detailed-history retention alone
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-obj-session-history
        - memory.md#mem-rte-checkpoint-update
        note: Saving raw messages/traces without a separate behavior-shaping derivation is not itself
          a qualifying learning write. Its role as input/context remains distinct from the derived summary
          route.
      - scope: Usage-only host accounting output
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-obj-turn-usage
        note: Standalone numeric usage display/aggregation is not a behavior-shaping model artifact or
          learned parameter update; context counts/status are assessed separately.
      - scope: Operator configuration and website-version cache writes
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-config-change
        - epistemic.md#epi-obj-version-cache
        - epistemic.md#epi-rte-version-notice
        note: These routes admit explicit selections or website assertions, not automatic trace-fed behavioral
          artifacts. This is route inapplicability, not a system-wide negative.
      - scope: Potential trace-responsive root guidance editing
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-bap-workspace-guidance
        note: Model task editing can change later guidance, but no accepted record ties its proposal to
          qualifying trace inputs. A reread path does not establish or exclude trace-fed learning.
      - scope: Direct API supplied context derivation
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-direct-agent
        note: Initialization control, trace inputs, durable transformation and later caller are unspecified;
          the known checkpoint yes does not resolve this alternative.
      records:
      - memory.md#mem-rte-checkpoint-update
      - memory.md#mem-obj-session-summary
      - memory.md#mem-rte-session-context
      - epistemic.md#epi-rte-event-projection
      - memory.md#mem-obj-session-history
      - memory.md#mem-obj-turn-usage
      - runtime.md#rt-rte-config-change
      - epistemic.md#epi-obj-version-cache
      - epistemic.md#epi-rte-version-notice
      - runtime.md#rt-bap-workspace-guidance
      - runtime.md#rt-rte-direct-agent
      note: Automatic derived status/accounting/context reaches a later model, supporting a narrow yes.
        This does not establish improved capacity. Open guidance edits and generic API alternatives cannot
        supply a system-wide no.
    trace_source:
      assessment: partial
      units:
      - scope: Conversational turns feeding retained continuation context
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id039
          - memory.md#mem-obj-session-summary
          - memory.md#mem-rte-checkpoint-update
          - memory.md#mem-rte-session-context
          note: Copied user messages and returned responses are recorded agent-session turns used in the
            durable context projection; neither a human caller nor semantic abstraction is required.
        records: *id039
        note: Copied user messages and returned responses are recorded agent-session turns used in the
          durable context projection; neither a human caller nor semantic abstraction is required.
      - scope: Hook callback observations feeding context counts and history
        assessment: known
        findings:
        - value: event-streams
          basis: wired
          records: &id040
          - memory.md#mem-rte-checkpoint-update
          - epistemic.md#epi-rte-event-projection
          - memory.md#mem-rte-session-context
          note: Original discrete runtime hook callbacks supply reported file operations and command attempts.
            These are event-stream inputs; they do not prove complete or successful tool execution.
        records: *id040
        note: Original discrete runtime hook callbacks supply reported file operations and command attempts.
          These are event-stream inputs; they do not prove complete or successful tool execution.
      - scope: Execution request/feedback material feeding derived context
        assessment: partial
        findings:
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-rte-checkpoint-update
          - epistemic.md#epi-rte-event-projection
          - memory.md#mem-rte-session-context
          note: File-operation feedback and command-attempt records feed automatically retained context
            counts. This value concerns execution records, not arbitrary strings imported as events.
        records:
        - memory.md#mem-rte-checkpoint-update
        - memory.md#mem-obj-session-history
        - epistemic.md#epi-rte-event-projection
        - memory.md#mem-rte-session-context
        note: Recorded file/command observations are tool activity, but full externally defined RunTrace
          origin/content remains unknown; no complete trajectory or trace-source inventory follows.
      - scope: Raw retention, standalone usage display, operator settings and release assertion
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-obj-session-history
        - memory.md#mem-obj-turn-usage
        - runtime.md#rt-rte-config-change
        - epistemic.md#epi-obj-version-cache
        - epistemic.md#epi-rte-version-notice
        note: These separately scoped routes do not establish a qualifying automatic behavior-shaping
          trace write; their storage lineage is not a trace-source classification.
      - scope: Potential guidance update and direct-API supplied context sources
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-bap-workspace-guidance
        - runtime.md#rt-rte-direct-agent
        note: The qualifying write chain is itself unresolved; no original trace content can be assigned
          or declared absent for these alternatives.
      records:
      - memory.md#mem-obj-session-summary
      - memory.md#mem-rte-checkpoint-update
      - memory.md#mem-rte-session-context
      - epistemic.md#epi-rte-event-projection
      - memory.md#mem-obj-session-history
      - memory.md#mem-obj-turn-usage
      - runtime.md#rt-rte-config-change
      - epistemic.md#epi-obj-version-cache
      - epistemic.md#epi-rte-version-notice
      - runtime.md#rt-bap-workspace-guidance
      - runtime.md#rt-rte-direct-agent
      note: Qualifying checkpoint context has recorded conversational and hook-event origins; externally
        produced RunTrace contents remain incompletely characterized. Nonqualifying stores do not add
        source values.
---

# Fractal memory profile

## Comparison rationale

The operative memory is not the whole workspace or runtime storage surface. Session summary, detailed history and usage are contained parts of the checkpoint with different consumers. Changed root guidance, selected configuration and startup cache have their own later-consumer routes. The public API's unspecified supplied context remains an unresolved alternative rather than being assigned the shipped driver's retention protocol. External provider and sandbox internals are outside this comparison, not evidenced absences.

The summary combines interpreted prose with symbolic status/count fields. Its model-facing force is historical context, not standing instruction merely because the signature contains it. Root guidance does supply standing directions. Configuration routes adapter/default choices. Numeric usage informs host display. None of these channels establishes compliance or semantic task acceptance. See [MEM-OBJ-session-summary](memory.md#mem-obj-session-summary), [MEM-BAP-summary-context](memory.md#mem-bap-summary-context), [RT-BAP-workspace-guidance](runtime.md#rt-bap-workspace-guidance), [RT-RTE-config-change](runtime.md#rt-rte-config-change) and [MEM-OBJ-turn-usage](memory.md#mem-obj-turn-usage).

The narrow trace-learning yes is automatic production of durable status/accounting/context followed by later model delivery. It does not mean parameter learning, semantic lesson synthesis, accepted truth or improved capacity. Raw trace storage and standalone usage display do not independently qualify. Conversational turns, discrete runtime hook callbacks and execution observations support the positive source findings; complete external RunTrace content and provenance remain unresolved. See [MEM-RTE-checkpoint-update](memory.md#mem-rte-checkpoint-update), [EPI-RTE-event-projection](epistemic.md#epi-rte-event-projection), [MEM-OBJ-session-history](memory.md#mem-obj-session-history) and [MEM-RTE-session-context](memory.md#mem-rte-session-context).

Curation is not assigned from the word summary. The recorded renderer copies entire responses; activity-count projection consolidates detailed turn activity into a reduced representation, even while raw detail remains available in the recent tail. This does not establish semantic abstraction of response prose or novel lesson synthesis. Existing turn finalization and configuration/cache replacement support evolution; recent-tail eviction and cache fallback expiry support decay in their respective scopes. See [MEM-OBJ-session-summary](memory.md#mem-obj-session-summary), [MEM-RTE-checkpoint-update](memory.md#mem-rte-checkpoint-update), [MEM-RTE-session-context](memory.md#mem-rte-session-context), [RT-RTE-config-change](runtime.md#rt-rte-config-change) and [EPI-RTE-version-notice](epistemic.md#epi-rte-version-notice).

Explicit resume is pull. Later submit independently pushes selected-session context. The requested session ID does not make that subsequent all-turn/recency push identifier-targeted; a fixed root filename is likewise not an identity-matched selection of delivered memory parts. Foreground exact-detail inspection is only afforded. The audit/repair recipe demonstrates the shipped continuation wiring, not exercised recall or successful repair. See [MEM-RTE-session-reload](memory.md#mem-rte-session-reload), [MEM-RTE-session-context](memory.md#mem-rte-session-context), [RT-BAP-workspace-guidance](runtime.md#rt-bap-workspace-guidance) and [WF-RTE-audit-repair](workflow.md#wf-rte-audit-repair).

Reconciliation supersedes EPI-OBJ-session-summary with [MEM-OBJ-session-summary](memory.md#mem-obj-session-summary). This profile uses the canonical memory object throughout. No other identity is superseded: checkpoint, answer fields, usage part, rendering route and context-delivery route retain their separate scopes. No value is strengthened by that identity amendment.

All positive findings are implementation wiring or explicitly marked affordances. No observed operation or causal experiment is supplied. Partial assessments retain the unresolved direct-API admission/provenance and opaque trace parts rather than projecting a strongest witness into complete system coverage. There are no system-wide absence findings or local trace-learning no findings. Source-read log: no source files were read; classification used only the supplied accepted members and reconciliation.
