---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'kgai memory comparison: retained decision reasons, event/graph state, conventions and access
  metadata, with opaque host/provider alternatives.'
run-id: AAS-2026-10-14-kgai-54bcae52e039-01
source-identity: https://github.com/kgaidev/kgai
reviewed-boundary: 0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b
memory-comparison:
  version: 2
  scope: 'Included: accumulated decision titles/rationales and symbolic events, Kuzu and reader projections,
    configured conventions, local approval and autosync control/diagnostic state, their admission/maintenance/later-consumer
    routes, opaque host-managed task/session context consumed by extraction, and unresolved external host/provider
    numerical-state alternatives identified by the accepted inventory. External parameter storage, provenance
    and update routes are uninspected rather than credited to kgai. Excluded: shipped static skill/capture
    prompts, transient turn markers and pending proposals, UI-compaction bookkeeping, installed executable
    replacement, and hypothetical export re-import. External host compaction is not an established kgai
    memory route.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Retained decision text and symbolic event shards
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-decision
          - memory.md#mem-obj-event
          note: Per-install log shards retain reasons and event envelopes.
        records:
        - memory.md#mem-obj-decision
        - memory.md#mem-obj-event
        note: NDJSON is an encoding of persisted files, not a separate substrate.
      - scope: Kuzu projection, including decision text fields
        assessment: known
        findings:
        - value: graph
          basis: wired
          records:
          - memory.md#mem-obj-graph
          note: Element, decision and relationship tables in graph.kuzu supply operative structural state.
        records:
        - memory.md#mem-obj-decision
        - memory.md#mem-obj-graph
        note: The persisted graph is rebuildable from the authoritative log.
      - scope: Reader replay projection
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-graph
          - runtime.md#rt-rte-editor-read
          note: Go maps retain the loaded projection across reader requests.
        records:
        - memory.md#mem-obj-graph
        - runtime.md#rt-rte-editor-read
        note: The shipped human-facing reader independently materializes accumulated events.
      - scope: Configured conventions and local approval registry
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-prompt
          - runtime.md#rt-obj-trusted
          note: Configuration files retain conventions; trusted.json retains local approvals.
        records:
        - memory.md#mem-obj-prompt
        - runtime.md#rt-obj-trusted
        note: The convention text and fingerprint registry are distinct content and control files.
      - scope: Autosync outcome and cooldown state
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-rte-team-sync
          note: last-autosync.json persists timestamps, failures and soft-failure detail.
        records:
        - runtime.md#rt-rte-team-sync
        note: Local diagnostics are not engineering reasons but affect later status and control.
      - scope: External host/provider numerical state used by capture
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-host-model
        note: The component identifies external provider/host-managed parameters, but not their storage
          implementation. No model-weights substrate is inferred merely from numerical form.
      - scope: Host-managed retained task/session context copied into the capture fork
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-fork-capture
        - runtime.md#rt-cmp-host-model
        note: The external host owns copied input and its retained representation/provenance or maintenance.
          The capture prompt and completed-turn display do not classify the opaque payload.
      records:
      - memory.md#mem-obj-decision
      - memory.md#mem-obj-event
      - memory.md#mem-obj-graph
      - runtime.md#rt-rte-editor-read
      - memory.md#mem-obj-prompt
      - runtime.md#rt-obj-trusted
      - runtime.md#rt-rte-team-sync
      - runtime.md#rt-cmp-host-model
      - runtime.md#rt-rte-fork-capture
      note: The records cover decision shards, both projections, conventions, approval and sync-control
        files. The provider-managed numerical state has no inspected physical substrate; this prevents
        a complete inventory of substrates.
    representational_form:
      assessment: partial
      units:
      - scope: Decision titles and rationales at model/human recall consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-decision
          note: Reasons acquire meaning through later model or human interpretation.
        records:
        - memory.md#mem-obj-decision
        - memory.md#mem-rte-context-recall
        - memory.md#mem-rte-search-history
        - runtime.md#rt-rte-editor-read
        note: Full history and clipped recall share a natural-language form, not equal completeness.
      - scope: Event envelope and structural projection at engine/replay consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-event
          - memory.md#mem-obj-graph
          note: IDs, mutations, authority relations and fixed replay rules localize machine-consumed units.
        records:
        - memory.md#mem-obj-event
        - memory.md#mem-obj-graph
        note: Natural-language fields are assessed separately rather than turning the entire graph into
          one form.
      - scope: Configured conventions at the foreground model
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-prompt
          - runtime.md#rt-rte-config-admission
          note: The model receives selection and naming directions in ordinary language.
        records:
        - memory.md#mem-obj-prompt
        - runtime.md#rt-rte-config-admission
        note: Framing and length limits do not change how the convention content is interpreted.
      - scope: Approval fingerprints and autosync diagnostics at deterministic loaders/control and status
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-obj-trusted
          - runtime.md#rt-rte-config-admission
          - runtime.md#rt-rte-team-sync
          note: Fingerprint matches and timestamps determine configuration eligibility and cooldown control.
        - value: natural-language
          basis: wired
          records:
          - runtime.md#rt-rte-team-sync
          note: Saved error/detail text is exposed by later status as diagnostic information.
        records:
        - runtime.md#rt-obj-trusted
        - runtime.md#rt-rte-config-admission
        - runtime.md#rt-rte-team-sync
        note: Machine state and human-readable error detail have different consumption paths.
      - scope: Host model and optional fork numerical state
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - runtime.md#rt-cmp-host-model
          note: The capture model is a distributed-parametric component.
        records:
        - runtime.md#rt-cmp-host-model
        note: This form is recorded independently of exact version, storage and parameter-update uncertainty.
      - scope: Host-managed retained task/session context copied into the capture fork
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-fork-capture
        - runtime.md#rt-cmp-host-model
        note: The external host owns copied input and its retained representation/provenance or maintenance.
          The capture prompt and completed-turn display do not classify the opaque payload.
      records:
      - memory.md#mem-obj-decision
      - memory.md#mem-rte-context-recall
      - memory.md#mem-rte-search-history
      - runtime.md#rt-rte-editor-read
      - memory.md#mem-obj-event
      - memory.md#mem-obj-graph
      - memory.md#mem-obj-prompt
      - runtime.md#rt-rte-config-admission
      - runtime.md#rt-obj-trusted
      - runtime.md#rt-rte-team-sync
      - runtime.md#rt-cmp-host-model
      - runtime.md#rt-rte-fork-capture
      note: The recorded inventory separates reasons, machine-consumed structure, convention text, access
        metadata and numerical model state. Exact host-copied fork payload remains opaque; a known model
        form does not classify that consumed alternative.
    lineage:
      assessment: partial
      units:
      - scope: Foreground model or human supplied decision text
        assessment: partial
        findings:
        - value: authored
          basis: afforded
          records:
          - memory.md#mem-obj-decision
          - runtime.md#rt-rte-foreground-capture
          note: The foreground model can formulate reasons and a human can supply or edit a decision.
        records:
        - memory.md#mem-obj-decision
        - runtime.md#rt-rte-foreground-capture
        note: The admitted text is copied from a caller proposal. Arbitrary API submissions do not resolve
          initial origin or truth.
      - scope: Optional fork derived decision content
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-rte-fork-capture
          - memory.md#mem-obj-decision
          note: A model selects decision JSON from completed task/session experience for durable admission.
        records:
        - memory.md#mem-obj-decision
        - runtime.md#rt-rte-fork-capture
        note: The recorded extraction path is distinct from the unknown exact copied input.
      - scope: Decision events acquired through synchronization
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - runtime.md#rt-rte-team-sync
          - memory.md#mem-obj-event
          - memory.md#mem-obj-decision
          note: Remote decision events and their reasons enter local retained shards.
        records:
        - runtime.md#rt-rte-team-sync
        - memory.md#mem-obj-event
        - memory.md#mem-obj-decision
        note: The local acquisition path is known; the remote authors original content provenance is not
          upgraded.
      - scope: Engine event envelope and graph/reader projections
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-event
          - memory.md#mem-obj-graph
          note: Engine/store metadata and ordered event application produce envelopes and projected state.
        records:
        - memory.md#mem-obj-event
        - memory.md#mem-obj-graph
        note: Reference resolution, computed authority and replay are deterministic derivations rather
          than fresh reasons.
      - scope: Configured convention text
        assessment: partial
        findings:
        - value: authored
          basis: afforded
          records:
          - memory.md#mem-obj-prompt
          note: Configuration provides an authoring surface for capture conventions.
        records:
        - memory.md#mem-obj-prompt
        - runtime.md#rt-rte-config-admission
        note: Configuration authors supply the text, but the records do not establish every initial author
          or pre-existing derivation.
      - scope: Approval records and autosync outcome state
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - runtime.md#rt-obj-trusted
          - runtime.md#rt-rte-config-admission
          - runtime.md#rt-rte-team-sync
          note: Fingerprint computation, timestamping and outcome recording construct retained local metadata.
        records:
        - runtime.md#rt-obj-trusted
        - runtime.md#rt-rte-config-admission
        - runtime.md#rt-rte-team-sync
        note: These are software-generated access/control artifacts, not authored engineering knowledge.
      - scope: External numerical model provenance
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-host-model
        note: No training, initialization or embedding provenance is inspected; the model call cannot
          establish any lineage value.
      - scope: Host-managed retained task/session context copied into the capture fork
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-fork-capture
        - runtime.md#rt-cmp-host-model
        note: The external host owns copied input and its retained representation/provenance or maintenance.
          The capture prompt and completed-turn display do not classify the opaque payload.
      records:
      - memory.md#mem-obj-decision
      - runtime.md#rt-rte-foreground-capture
      - runtime.md#rt-rte-fork-capture
      - runtime.md#rt-rte-team-sync
      - memory.md#mem-obj-event
      - memory.md#mem-obj-graph
      - memory.md#mem-obj-prompt
      - runtime.md#rt-rte-config-admission
      - runtime.md#rt-obj-trusted
      - runtime.md#rt-cmp-host-model
      note: Derivation paths of admitted content, envelopes and projections are supported. Generic initial
        content provenance, convention authorship and external numerical provenance remain unresolved;
        a known subsequent path does not resolve them.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Decision text at later CLI model and editor human consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-decision
          - memory.md#mem-rte-context-recall
          - memory.md#mem-rte-search-history
          - runtime.md#rt-rte-editor-read
          - runtime.md#rt-bap-decision-recall
          note: Selected reasons supply reference and context for later explanation or development.
        records:
        - memory.md#mem-obj-decision
        - memory.md#mem-rte-context-recall
        - memory.md#mem-rte-search-history
        - runtime.md#rt-rte-editor-read
        - runtime.md#rt-bap-decision-recall
        note: Informational delivery is wired; activated coding dependence and benefit remain unobserved.
      - scope: Retained lexical fields and authority/recency metadata at retrieval selection
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-rte-context-recall
          - memory.md#mem-rte-search-history
          - memory.md#mem-obj-decision
          note: Retained names and decision texts feed fixed lexical scores; authority Lamport contributes
            context priority.
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-graph
          - memory.md#mem-rte-context-recall
          - memory.md#mem-rte-search-history
          note: Head and attachment predicates select which retained reasons reach context or history.
        records:
        - memory.md#mem-obj-decision
        - memory.md#mem-obj-event
        - memory.md#mem-obj-graph
        - memory.md#mem-rte-context-recall
        - memory.md#mem-rte-search-history
        note: Retained historical text can affect rank even when it is not delivered as a head reason.
      - scope: Event mutations and projected graph at replay and structural-read consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-graph
          - memory.md#mem-rte-asof-recall
          note: Structural queries and as-of reconstruction deliver encoded domain structure.
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-event
          - memory.md#mem-obj-graph
          note: Targets and supersession select current authority heads and subsequent state.
        records:
        - memory.md#mem-obj-event
        - memory.md#mem-obj-graph
        - memory.md#mem-rte-asof-recall
        note: Graph authority governs encoded state and recall eligibility, not permission to change source
          code.
      - scope: Event identities and parent-chain state at covered integrity admission gates
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-event
          - runtime.md#rt-rte-team-sync
          note: Retained hashes, decision IDs and chain/prefix relationships supply consistency criteria.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-rte-team-sync
          note: Covered replay and object-sync gates skip or reject invalid candidates.
        records:
        - memory.md#mem-obj-event
        - runtime.md#rt-rte-team-sync
        note: The gate applies to covered engine/object-sync paths, not uniformly to the editor.
      - scope: Configured conventions at foreground model injection
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-obj-prompt
          - runtime.md#rt-rte-config-admission
          note: Effective conventions direct capture selection and naming across sessions.
        records:
        - memory.md#mem-obj-prompt
        - runtime.md#rt-rte-config-admission
        note: Standing directions are supplied, but reliable compliance is unobserved.
      - scope: Approval registry at project settings loaders
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - runtime.md#rt-obj-trusted
          - runtime.md#rt-rte-config-admission
          note: Allowed-setting fingerprints determine whether a project layer has an approval.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-obj-trusted
          - runtime.md#rt-rte-config-admission
          note: Unapproved project values remain inactive.
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-obj-trusted
          - runtime.md#rt-rte-config-admission
          note: Approved store values select the later read/write destination.
        records:
        - runtime.md#rt-obj-trusted
        - runtime.md#rt-rte-config-admission
        note: Approval state is not authenticated human consent and does not certify convention quality.
      - scope: Autosync persisted timestamp and outcome at later hook/status consumers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-rte-team-sync
          note: Cooldown state affects when the next automatic sync attempt is eligible.
        - value: knowledge
          basis: wired
          records:
          - runtime.md#rt-rte-team-sync
          note: Later status can expose persistent failure and outcome detail.
        records:
        - runtime.md#rt-rte-team-sync
        note: Control and diagnostics have distinct effects.
      - scope: External numerical state at model inference or updates
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-host-model
        note: Inference is used by capture, but accepted records do not isolate memory authority or a
          parameter-update consumer for this opaque component.
      - scope: Retained task/session experience at the automatic fork extraction consumer
        assessment: partial
        findings:
        - value: learning
          basis: wired
          records:
          - runtime.md#rt-rte-fork-capture
          - memory.md#mem-obj-decision
          - memory.md#mem-obj-event
          note: Task experience feeds the automatic extraction that writes durable decision context for
            later consumers; this is the update-side force, not proof of improved capacity.
        records:
        - runtime.md#rt-rte-fork-capture
        - memory.md#mem-obj-decision
        - memory.md#mem-obj-event
        note: The update consumer receives opaque host-forked experience and can produce durable reasons;
          exact included parts and additional forces are unresolved.
      records:
      - memory.md#mem-obj-decision
      - memory.md#mem-rte-context-recall
      - memory.md#mem-rte-search-history
      - runtime.md#rt-rte-editor-read
      - runtime.md#rt-bap-decision-recall
      - memory.md#mem-obj-event
      - memory.md#mem-obj-graph
      - memory.md#mem-rte-asof-recall
      - runtime.md#rt-rte-team-sync
      - memory.md#mem-obj-prompt
      - runtime.md#rt-rte-config-admission
      - runtime.md#rt-obj-trusted
      - runtime.md#rt-cmp-host-model
      - runtime.md#rt-rte-fork-capture
      note: Authority is classified at each actual consumer. Static capture instructions are excluded;
        their instruction to respect recalled choices does not convert every reason into an enforcement
        mechanism. External numerical authority remains unclassified within the memory boundary.
    write_agency:
      assessment: partial
      units:
      - scope: Routine foreground skill/review decision admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-foreground-capture
          note: The model selects and submits the decision without routine operator confirmation.
        records:
        - runtime.md#rt-rte-foreground-capture
        note: The engine has no per-decision human-consent check on routine capture.
      - scope: Explicit decision-command confirmation and human supply/edit
        assessment: known
        findings:
        - value: manual
          basis: afforded
          records:
          - runtime.md#rt-rte-foreground-capture
          - memory.md#mem-obj-decision
          note: The human can supply/edit retained content, and the explicit command requests proposal
            confirmation.
        records:
        - runtime.md#rt-rte-foreground-capture
        - memory.md#mem-obj-decision
        note: The explicit command offers a separate per-content operator decision; source does not demonstrate
          its use.
      - scope: Optional fork auto mode and unsupported-surface confirm fallback
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-fork-capture
          note: Software parses, dry-runs and ingests the model proposal without a per-content human decision.
        records:
        - runtime.md#rt-rte-fork-capture
        note: Headless confirm follows automatic admission rather than implying a human gate.
      - scope: Optional fork confirm mode with terminal/desktop UI
        assessment: known
        findings:
        - value: manual
          basis: wired
          records:
          - runtime.md#rt-rte-fork-capture
          note: Supported confirmation surfaces allow a human Record/Skip decision over retained content.
        records:
        - runtime.md#rt-rte-fork-capture
        note: Record admits the particular proposal; Skip does not create memory.
      - scope: Generic direct API/shell decision submissions
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-foreground-capture
        - memory.md#mem-obj-decision
        note: An arbitrary caller may be human or software; physical append and author labels do not resolve
          admission control.
      - scope: Sync import, envelope construction, projections and autosync state
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-team-sync
          - memory.md#mem-obj-event
          - memory.md#mem-obj-graph
          note: Verified imports, event metadata and replay/control-state updates are admitted without
            per-content human decisions.
        records:
        - runtime.md#rt-rte-team-sync
        - memory.md#mem-obj-event
        - memory.md#mem-obj-graph
        note: Transport approval is not per-reason approval; derived state is constructed by software.
      - scope: Convention text and local approval admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-prompt
        - runtime.md#rt-obj-trusted
        - runtime.md#rt-rte-config-admission
        note: The skill prescribes consent but kg trust authenticates no human; authoring a config file
          and approving its use are separate unresolved controls.
      - scope: External numerical state initialization or updates
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-host-model
        note: No parameter-admission mechanism or provider control is inspected.
      - scope: Host-managed retained task/session context copied into the capture fork
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-fork-capture
        - runtime.md#rt-cmp-host-model
        note: The external host owns copied input and its retained representation/provenance or maintenance.
          The capture prompt and completed-turn display do not classify the opaque payload.
      records:
      - runtime.md#rt-rte-foreground-capture
      - memory.md#mem-obj-decision
      - runtime.md#rt-rte-fork-capture
      - runtime.md#rt-rte-team-sync
      - memory.md#mem-obj-event
      - memory.md#mem-obj-graph
      - memory.md#mem-obj-prompt
      - runtime.md#rt-obj-trusted
      - runtime.md#rt-rte-config-admission
      - runtime.md#rt-cmp-host-model
      note: Automatic and human-approved decision routes coexist. Generic CLI caller identity, convention
        admission and external parameter control remain unresolved; initiating a coding task is not per-content
        approval.
    curation_operations:
      assessment: partial
      units:
      - scope: Live graph mutation and successor authority
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-event
          - memory.md#mem-obj-graph
          note: New mutations revise existing live structural entries.
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-obj-event
          - memory.md#mem-obj-graph
          - runtime.md#rt-rte-foreground-capture
          note: Supersession withdraws current head reliance and link retirement withdraws live edges
            while preserving event history.
        records:
        - memory.md#mem-obj-event
        - memory.md#mem-obj-graph
        - runtime.md#rt-rte-foreground-capture
        note: History remains retained while properties/edges and governing heads change.
      - scope: Foreground selection of a choice and concise rationale from task work
        assessment: partial
        findings:
        - value: consolidate
          basis: claimed
          records:
          - runtime.md#rt-rte-foreground-capture
          note: The model is instructed to select the acted-on structural choice and compress its reasons.
        records:
        - runtime.md#rt-rte-foreground-capture
        - memory.md#mem-obj-decision
        note: The skill requests a consolidated choice and short why; actual semantic preservation of
          model output is not recorded.
      - scope: Optional fork extraction from host task/session context
        assessment: partial
        findings:
        - value: consolidate
          basis: afforded
          records:
          - runtime.md#rt-rte-fork-capture
          - memory.md#mem-obj-decision
          note: The capture handoff offers selection and compression of task experience into durable decision
            content.
        records:
        - runtime.md#rt-rte-fork-capture
        - memory.md#mem-obj-decision
        note: Extraction into a reduced decision payload is afforded. Exact copied input and semantic
          transformation are opaque, preventing complete classification, including any synthesis.
      - scope: Sync/replay metadata maintenance, approval changes and convention editing
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-team-sync
        - memory.md#mem-obj-graph
        - memory.md#mem-obj-prompt
        - runtime.md#rt-rte-config-admission
        note: Acquisition, rebuild and shard reconciliation do not themselves establish a controlled semantic
          curation operation; detailed content transformations of arbitrary convention replacements are
          not recorded.
      - scope: External numerical-state maintenance
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-host-model
        note: No parameter transformation over retained experience is inspected.
      - scope: Host-managed retained task/session context copied into the capture fork
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-fork-capture
        - runtime.md#rt-cmp-host-model
        note: The external host owns copied input and its retained representation/provenance or maintenance.
          The capture prompt and completed-turn display do not classify the opaque payload.
      records:
      - memory.md#mem-obj-event
      - memory.md#mem-obj-graph
      - runtime.md#rt-rte-foreground-capture
      - memory.md#mem-obj-decision
      - runtime.md#rt-rte-fork-capture
      - runtime.md#rt-rte-team-sync
      - memory.md#mem-obj-prompt
      - runtime.md#rt-rte-config-admission
      - runtime.md#rt-cmp-host-model
      note: Implemented live-state revision and supersession support evolve and invalidate. Requested
        extraction supports consolidation at its own weaker basis. Exact-identity no-ops, acquisition
        and index rebuilds are not deduplication; opaque model transformations and maintenance alternatives
        prevent a complete value inventory.
    read_back_direction:
      assessment: partial
      units:
      - scope: CLI context/search/history/query/as-of and editor requests
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-context-recall
          - memory.md#mem-rte-search-history
          - memory.md#mem-rte-asof-recall
          - runtime.md#rt-rte-editor-read
          - runtime.md#rt-rte-query-read
          note: A model, user or editor requests retained content and receives the selected answer.
        records:
        - memory.md#mem-rte-context-recall
        - memory.md#mem-rte-search-history
        - memory.md#mem-rte-asof-recall
        - runtime.md#rt-rte-editor-read
        - runtime.md#rt-rte-query-read
        note: These shipped callers consume accumulated state; sync only changes its availability.
      - scope: SessionStart convention injection
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-prompt
          - runtime.md#rt-rte-config-admission
          note: SessionStart selects and delivers effective approved conventions into host context.
        records:
        - memory.md#mem-obj-prompt
        - runtime.md#rt-rte-config-admission
        note: The hook supplies retained convention text without a consumer topic request.
      - scope: Explicit raw convention reload and trust/status inspection
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-obj-prompt
          - runtime.md#rt-rte-config-admission
          - runtime.md#rt-rte-team-sync
          note: kg prompt --raw and configuration/status requests reload retained convention or control
            information.
        records:
        - memory.md#mem-obj-prompt
        - runtime.md#rt-rte-config-admission
        - runtime.md#rt-rte-team-sync
        note: These returns fulfill an explicit retained-state request; they are not additional pushes.
      - scope: Local control metadata consumed by automatic session/lifecycle operations
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-obj-trusted
          - runtime.md#rt-rte-config-admission
          - runtime.md#rt-rte-team-sync
          note: Settings loaders and autosync control retrieve their retained metadata to evaluate the
            next operation.
        records:
        - runtime.md#rt-obj-trusted
        - runtime.md#rt-rte-config-admission
        - runtime.md#rt-rte-team-sync
        note: Code loads approval and cooldown state as inputs to its own requested resolution/control
          operations.
      - scope: External host/provider retained-context or numerical-state delivery
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-host-model
        note: The records do not expose an independently classifiable accumulated-memory request/delivery
          chain inside the host/provider.
      records:
      - memory.md#mem-rte-context-recall
      - memory.md#mem-rte-search-history
      - memory.md#mem-rte-asof-recall
      - runtime.md#rt-rte-editor-read
      - runtime.md#rt-rte-query-read
      - memory.md#mem-obj-prompt
      - runtime.md#rt-rte-config-admission
      - runtime.md#rt-rte-team-sync
      - runtime.md#rt-obj-trusted
      - runtime.md#rt-cmp-host-model
      note: Demand decision/structure reads and automatic convention injection are supported. Requested
        selection and returned JSON remain pull even when code ranks the answer. Provider-managed memory
        delivery alternatives remain uninspected.
    read_back_signal:
      assessment: partial
      units:
      - scope: SessionStart effective convention push
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-prompt
          - runtime.md#rt-rte-config-admission
          note: Configuration availability, approval and precedence select effective conventions without
            relevance matching to a task.
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-obj-trusted
          - runtime.md#rt-rte-config-admission
          - memory.md#mem-obj-prompt
          note: An actual allowed-settings fingerprint match licenses the project layer whose retained
            prompt can be delivered; this is approval targeting, not semantic decision recall.
        records:
        - memory.md#mem-obj-prompt
        - runtime.md#rt-rte-config-admission
        - runtime.md#rt-obj-trusted
        note: Trigger is SessionStart; selector inputs are layer precedence, allowed settings and approval;
          selected retained part is the effective prompt text, capped by Bash string length.
      - scope: Inspected demand decision/structure/control reads
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-context-recall
        - memory.md#mem-rte-search-history
        - memory.md#mem-rte-asof-recall
        - runtime.md#rt-rte-editor-read
        - runtime.md#rt-obj-trusted
        - runtime.md#rt-rte-config-admission
        - runtime.md#rt-rte-team-sync
        note: These operations fulfill requests or code-owned reads rather than independently push selected
          memory to a consumer; lexical scoring on a pull does not establish a push signal.
      - scope: External host/provider unsolicited memory selection
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-host-model
        note: No trigger, selector input or delivered retained part is exposed for this alternative.
      records:
      - memory.md#mem-obj-prompt
      - runtime.md#rt-rte-config-admission
      - runtime.md#rt-obj-trusted
      - memory.md#mem-rte-context-recall
      - memory.md#mem-rte-search-history
      - memory.md#mem-rte-asof-recall
      - runtime.md#rt-rte-editor-read
      - runtime.md#rt-rte-team-sync
      - runtime.md#rt-cmp-host-model
      note: The assessed unsolicited convention supply is coarse, not topic-sensitive recall. Pull-only
        units are locally inapplicable; they do not make unresolved provider alternatives inapplicable.
    trace_learning:
      assessment: partial
      units:
      - scope: Optional auto/headless fork extraction to admitted decisions and later recall
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-fork-capture
          - memory.md#mem-obj-decision
          - memory.md#mem-obj-event
          - memory.md#mem-rte-context-recall
          - memory.md#mem-rte-search-history
          - runtime.md#rt-rte-editor-read
          note: Automatic trace-fed production retains behavior-shaping decision context for later tasks,
            independently of observed benefit.
        records:
        - runtime.md#rt-rte-fork-capture
        - memory.md#mem-obj-decision
        - memory.md#mem-obj-event
        - memory.md#mem-rte-context-recall
        - memory.md#mem-rte-search-history
        - runtime.md#rt-rte-editor-read
        note: Eligible task experience feeds automatic durable extraction; later CLI/editor consumption
          is wired. Exact fork context remains opaque but does not erase this write/consumer chain.
      - scope: Routine foreground capture from coding experience to later reasons
        assessment: partial
        findings:
        - value: 'yes'
          basis: afforded
          records:
          - runtime.md#rt-rte-foreground-capture
          - memory.md#mem-obj-decision
          - memory.md#mem-rte-context-recall
          - memory.md#mem-rte-search-history
          note: The skill affords model selection of acted-on task experience into retained reasons subsequently
            read by coding consumers.
        records:
        - runtime.md#rt-rte-foreground-capture
        - memory.md#mem-obj-decision
        - memory.md#mem-rte-context-recall
        - memory.md#mem-rte-search-history
        note: The automatic route is provided by model-facing capture policy; actual input/output trace
          lineage is not supplied for each submitted decision.
      - scope: Per-content human supply/confirmation routes
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-foreground-capture
        - runtime.md#rt-rte-fork-capture
        note: These locally scoped writes require an explicit human decision and therefore are not qualifying
          automatic trace-fed writes. This does not establish an absence on other modes.
      - scope: Generic submissions, convention initialization and local sync/approval control metadata
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-decision
        - runtime.md#rt-rte-foreground-capture
        - memory.md#mem-obj-prompt
        - runtime.md#rt-rte-config-admission
        - runtime.md#rt-rte-team-sync
        note: Generic source/control is unresolved. Stored diagnostics and cooldown updates are documented,
          but no recorded extraction/update-to-durable behavior-shaping artifact beyond operational bookkeeping
          warrants a trace-learning value for them.
      - scope: External provider numerical-state learning
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-host-model
        note: Parameter mutability and learning routes remain uninspected; fixed-weight or no-learning
          conclusions cannot follow from the absence of exposed update code.
      records:
      - runtime.md#rt-rte-fork-capture
      - memory.md#mem-obj-decision
      - memory.md#mem-obj-event
      - memory.md#mem-rte-context-recall
      - memory.md#mem-rte-search-history
      - runtime.md#rt-rte-editor-read
      - runtime.md#rt-rte-foreground-capture
      - memory.md#mem-obj-prompt
      - runtime.md#rt-rte-config-admission
      - runtime.md#rt-rte-team-sync
      - runtime.md#rt-cmp-host-model
      note: Automatic extraction can create durable decision context for later consumers without demonstrated
        improvement. Human-approved and arbitrary-caller alternatives, local control bookkeeping and external
        parameters do not become system-wide negatives.
    trace_source:
      assessment: not-determinable
      units:
      - scope: Optional fork automatic decision extraction input
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-fork-capture
        - runtime.md#rt-cmp-host-model
        note: The host controls copied session context. Exact conversational turns, recorded tool requests/results
          and any linked state/action/outcome sequences consumed by the write are not established; session-logs,
          tool-traces and trajectories cannot be asserted from the eligibility trigger.
      - scope: Routine foreground experience capture input
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-foreground-capture
        - memory.md#mem-obj-decision
        note: Task experience is described but no grounded trace-fed input instance identifies its original
          recorded content; do not classify the derived engineering event as an event-stream source.
      - scope: Per-content human supply/confirmation routes
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-foreground-capture
        - runtime.md#rt-rte-fork-capture
        note: Without automatic admission these locally scoped writes do not qualify for the trace-learning
          source axis.
      - scope: Generic submissions, conventions and sync/approval diagnostics
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-foreground-capture
        - memory.md#mem-obj-prompt
        - runtime.md#rt-rte-config-admission
        - runtime.md#rt-rte-team-sync
        note: A qualifying automatic trace-learning path is not established for these units, and unresolved
          control/provenance prevents a bounded absence warrant.
      - scope: External numerical-state update input
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-host-model
        note: No qualifying provider write or original trace input is inspected.
      records:
      - runtime.md#rt-rte-fork-capture
      - runtime.md#rt-cmp-host-model
      - runtime.md#rt-rte-foreground-capture
      - memory.md#mem-obj-decision
      - memory.md#mem-obj-prompt
      - runtime.md#rt-rte-config-admission
      - runtime.md#rt-rte-team-sync
      note: Records identify task/session/tool experience but leave exact original inputs to the qualifying
        model writes opaque. No controlled source value is established for those writes; an edited-turn
        trigger or an NDJSON event envelope is not itself their trace source. Provider alternatives remain
        separately uninspected.
---

# kgai memory profile

## Comparison rationale

The inventory separates retained reasons from the symbolic machinery selecting their current authority. [MEM-OBJ-decision](memory.md#mem-obj-decision) supplies knowledge at later model/human readers; [MEM-OBJ-event](memory.md#mem-obj-event) and [MEM-OBJ-graph](memory.md#mem-obj-graph) supply structural state and routing inputs. Text can also influence ranking without being delivered. [MEM-RTE-context-recall](memory.md#mem-rte-context-recall) specifically retains this distinction for historical text versus current head reasons. The static instruction to respect or supersede reasons is not itself accumulated memory.

Reconciliation supersedes the epistemic decision-reasons declaration with [MEM-OBJ-decision](memory.md#mem-obj-decision), and the epistemic historical-replay declaration with [MEM-RTE-asof-recall](memory.md#mem-rte-asof-recall). Those are the canonical citations here. The narrower authority part [EPI-OBJ-decision-mutations](epistemic.md#epi-obj-decision-mutations) remains distinct from the encompassing event. [EPI-RTE-recall-shaping](epistemic.md#epi-rte-recall-shaping) remains a valid overlapping operation; its semantic-preservation uncertainty does not remove wired pull delivery or ranking. No supersession upgrades a basis or changes an axis value.

Read-back direction follows each operation, not the presence of a selector. Lexical context/search and editor requests are pull. SessionStart convention injection is push: configuration precedence and approval choose retained directions without a task request. The approval fingerprint is an actual matched identifier selecting an eligible project layer, not an identifier attached only to a requested file. Coarse layer availability remains a separate selection basis. Neither synchronization nor a static Stop reminder establishes automatic relevance-based decision-history delivery ([RT-RTE-config-admission](runtime.md#rt-rte-config-admission), [MEM-OBJ-prompt](memory.md#mem-obj-prompt), [RT-RTE-team-sync](runtime.md#rt-rte-team-sync)).

Curation findings concern the implemented change. Successor authority and edge retirement invalidate current reliance while preserving history; live mutations evolve existing entries. Exact content-identity admission no-ops and event-hash deduplication do not establish semantic deduplication. Rebuild is another materialization, not consolidation. Model consolidation retains the weaker policy/affordance warrant because exact inputs and meaning preservation are unresolved; no synthesis is inferred merely from a model-generated rationale ([MEM-OBJ-event](memory.md#mem-obj-event), [MEM-OBJ-graph](memory.md#mem-obj-graph), [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture)).

Trace learning here means an automatic trace-fed write with a durable behavior-shaping result and later consumer, not demonstrated improvement. The fork's parsed decision crosses into persistent event memory and later recall, whereas a pending or skipped proposal does not. Its supported human-confirmation mode is separate from auto and headless fallback. The exact source content copied by the host remains unknown. Eligibility based on successful editing cannot establish that recorded tool traces were consumed, and derived event serialization does not establish event-stream origin. Thus positive trace-learning routes coexist with a not-determinable trace-source axis ([RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture), [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture)).

The external model's recorded parametric form is not a warrant for its storage, provenance, admission or learning routes. Those unresolved alternatives prevent complete-value claims without negating known kgai file/graph routes. Generic shell control likewise cannot establish manual admission. All architectural positives remain source-grounded rather than observed or causally supported; no deployed compliance, capture success or benefit is claimed ([RT-CMP-host-model](runtime.md#rt-cmp-host-model), [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture)).

Source-read log: none. Classification used only the supplied accepted members and reconciliation; no frozen-source ambiguity was resolved by additional source reads.
