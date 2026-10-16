---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: Voiden memory comparison of retained responses, execution bindings, CLI history, refreshed
  guidance and opaque provider verification state.
run-id: AAS-2026-10-14-voiden-98188b4a2f55-01
source-identity: https://github.com/voidenhq/voiden
reviewed-boundary: d7a0d05c40acb6cc483000643c700f17aecba0ef
memory-comparison:
  version: 2
  scope: 'Agent-facing MCP subsystem memory changed or accumulated through use: recorded response blocks;
    cross-call runtime/environment bindings and standalone durable snapshots; CLI execution history; publisher
    decisions/cache and unresolved provider status persistence; refreshed installed guide bodies, summaries
    and their access index. Includes opaque provider/script/initial-content alternatives and external
    guide-loading limits. Excludes unchanged shipped instructions/source code, executable plugin bytes
    and capability-installation metadata unrelated to these memory objects, outgoing transport session/token
    plumbing, ordinary current-run-only state, external host conversation/compaction and remote stores.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Recorded response blocks in project .void documents
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-response
          - runtime.md#rt-rte-result-write
          note: Selected result fields are written as document fences.
        records:
        - memory.md#mem-obj-response
        - runtime.md#rt-rte-result-write
        note: The retained block substrate is directly established; project Git tracking is not established.
      - scope: Runtime captures and selected environment across MCP calls; standalone saved variable snapshot
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - runtime.md#rt-obj-runtime-vars
          - memory.md#mem-rte-runtime-capture
          note: Mutable maps survive later calls within the process or HTTP session.
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-process-env
          - runtime.md#rt-rte-session-driver
          note: Standalone session mode reloads and saves the user-global JSON snapshot.
        records:
        - runtime.md#rt-obj-runtime-vars
        - memory.md#mem-rte-runtime-capture
        - memory.md#mem-obj-process-env
        - runtime.md#rt-rte-session-driver
        note: The two driver-specific retained locations are covered; current-run-only bindings are excluded.
      - scope: CLI accumulated execution history
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-session-results
          - memory.md#mem-rte-history-report
          note: results.json persists the appended history for reporting.
        records:
        - memory.md#mem-obj-session-results
        - memory.md#mem-rte-history-report
        note: The history file has concrete later report consumers.
      - scope: Publisher decisions and core verification-entry cache container
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - runtime.md#rt-obj-serve-decisions
          - memory.md#mem-obj-verify-entry-cache
          - runtime.md#rt-rte-tool-publication
          note: Core retains decisions and a Map across successful replanning.
        records:
        - runtime.md#rt-obj-serve-decisions
        - memory.md#mem-obj-verify-entry-cache
        - runtime.md#rt-rte-tool-publication
        note: This resolves core containers only, not provider-internal stores.
      - scope: Provider status write-back and additional provider persistence
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-tool-status-record
        - memory.md#mem-rte-status-write
        - memory.md#mem-obj-verify-entry-cache
        note: Project-file write-back is requested, but provider serialization/storage and any additional
          retention are unavailable. An interface is not a file-storage witness.
      - scope: Use-refreshed installed guide collection and its paths/index
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-bap-agent-guidance
          - runtime.md#rt-rte-host-registration
          note: Refresh retains full enabled-extension guides and the composed base/index in skill directories.
        records:
        - runtime.md#rt-bap-agent-guidance
        - runtime.md#rt-rte-host-registration
        note: Includes the changed installed collection, not unchanged bundled source instructions.
      records:
      - memory.md#mem-obj-response
      - runtime.md#rt-rte-result-write
      - runtime.md#rt-obj-runtime-vars
      - memory.md#mem-rte-runtime-capture
      - memory.md#mem-obj-process-env
      - runtime.md#rt-rte-session-driver
      - memory.md#mem-obj-session-results
      - memory.md#mem-rte-history-report
      - runtime.md#rt-obj-serve-decisions
      - memory.md#mem-obj-verify-entry-cache
      - runtime.md#rt-rte-tool-publication
      - memory.md#mem-obj-tool-status-record
      - memory.md#mem-rte-status-write
      - runtime.md#rt-bap-agent-guidance
      - runtime.md#rt-rte-host-registration
      note: Files and process memory are established locally. The included provider write-back/storage
        branch prevents complete substrate coverage; no repository substrate is inferred from file extensions
        or a source checkout.
    representational_form:
      assessment: partial
      units:
      - scope: Response attributes and parser/callback-visible block structure
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-response
          - memory.md#mem-rte-response-reload
          note: YAML attributes become normalized document JSON under fixed parser rules.
        records:
        - memory.md#mem-obj-response
        - memory.md#mem-rte-response-reload
        note: Only the structural path is classified here.
      - scope: Response body/error strings at afforded human or agent file inspection
        assessment: partial
        findings:
        - value: natural-language
          basis: afforded
          records:
          - memory.md#mem-obj-response
          note: Payload strings can supply interpreted evidence when a file reader inspects them.
        records:
        - memory.md#mem-obj-response
        - memory.md#mem-rte-response-reload
        note: Actual body content is uncaptured and plugin payload interpretation is unavailable; strings
          may instead contain symbolic data. No parametric form follows from opaque payloads.
      - scope: Runtime bindings, persisted snapshot and selected-environment map consumed by substitution
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-obj-runtime-vars
          - memory.md#mem-obj-process-env
          - memory.md#mem-rte-runtime-capture
          note: Named keys and fixed process-variable paths supply typed values to request substitution.
        records:
        - runtime.md#rt-obj-runtime-vars
        - memory.md#mem-obj-process-env
        - memory.md#mem-rte-runtime-capture
        note: Payload values can be structured or strings; the demonstrated consumption uses symbolic
          bindings, not natural-language model interpretation.
      - scope: History structure consumed by report commands
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-session-results
          - memory.md#mem-rte-history-report
          note: The JSON history and result fields feed fixed reporting/counting operations.
        records:
        - memory.md#mem-obj-session-results
        - memory.md#mem-rte-history-report
        note: This does not classify every uncaptured payload string or unaudited export formatter.
      - scope: History payload content interpreted by report readers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-results
        - memory.md#mem-rte-history-report
        note: Retained request/response strings are established, but their actual content and interpretation
          are not. Symbolic display does not resolve all payload forms.
      - scope: Publisher decision fields and verification cache schema
        assessment: partial
        findings:
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-obj-serve-decisions
          - memory.md#mem-obj-verify-entry-cache
          note: Served/excluded/status and passed/reason/time fields have localized symbolic structure.
        records:
        - runtime.md#rt-obj-serve-decisions
        - memory.md#mem-obj-verify-entry-cache
        note: runResult is opaque and provider interpretation is unavailable; cache schema does not classify
          that payload.
      - scope: Provider warning descriptions and status note channel
        assessment: partial
        findings:
        - value: natural-language
          basis: afforded
          records:
          - runtime.md#rt-obj-serve-decisions
          - memory.md#mem-obj-tool-status-record
          note: descriptionNote and note afford readable warning/summary text.
        - value: symbolic
          basis: afforded
          records:
          - memory.md#mem-obj-tool-status-record
          note: The declared state/time protocol fields are symbolic.
        records:
        - runtime.md#rt-obj-serve-decisions
        - memory.md#mem-obj-tool-status-record
        - memory.md#mem-rte-status-write
        note: Display fields do not determine provider retention encoding or the form of consumed runResult;
          actual registration formatting is uninspected.
      - scope: Refreshed guide bodies and composed index/path metadata
        assessment: known
        findings:
        - value: natural-language
          basis: afforded
          records:
          - runtime.md#rt-bap-agent-guidance
          note: Installed prose supplies directions if interpreted by the external agent.
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-bap-agent-guidance
          - runtime.md#rt-rte-host-registration
          note: Guide paths and enabled membership organize installed files.
        records:
        - runtime.md#rt-bap-agent-guidance
        - runtime.md#rt-rte-host-registration
        note: Form is separated by consumer; external loading remains unobserved, not a fourth prompt
          form.
      records:
      - memory.md#mem-obj-response
      - memory.md#mem-rte-response-reload
      - runtime.md#rt-obj-runtime-vars
      - memory.md#mem-obj-process-env
      - memory.md#mem-rte-runtime-capture
      - memory.md#mem-obj-session-results
      - memory.md#mem-rte-history-report
      - runtime.md#rt-obj-serve-decisions
      - memory.md#mem-obj-verify-entry-cache
      - memory.md#mem-obj-tool-status-record
      - memory.md#mem-rte-status-write
      - runtime.md#rt-bap-agent-guidance
      - runtime.md#rt-rte-host-registration
      note: Symbolic consumers are wired; natural-language channels are afforded. Uncaptured response/history
        payloads and provider runResult/encoding prevent complete mixed-form classification.
    lineage:
      assessment: partial
      units:
      - scope: Recorded response derivation
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-response
          - runtime.md#rt-rte-result-write
          note: Serializer selects fields, adds write metadata and truncates long bodies from a caller-supplied
            object.
        records:
        - memory.md#mem-obj-response
        - runtime.md#rt-rte-result-write
        note: Original result authorship and execution provenance are unresolved; caller-supplied is not
          proof of imported truth or trace extraction.
      - scope: Configured request/response capture into retained variable bindings
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-rte-runtime-capture
          - memory.md#mem-obj-process-env
          note: Authored field expressions extract typed values from request/response execution material
            for later substitution.
        records:
        - memory.md#mem-rte-runtime-capture
        - memory.md#mem-obj-process-env
        note: The inspected extraction path is resolved independently of initialization and scripting.
      - scope: Initial persisted bindings, selected-environment acquisition and script mutations
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-runtime-vars
        - memory.md#mem-obj-process-env
        - memory.md#mem-rte-runtime-capture
        note: External initial edits, profile resolver provenance and plugin scripts are unresolved. A
          known capture branch cannot resolve these included alternatives.
      - scope: CLI history structure and its endpoint payloads
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-session-results
          - memory.md#mem-rte-history-report
          note: Section results and generated failure records are assembled and appended to history.
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-session-results
          - runtime.md#rt-rte-request-execution
          note: Network/tool payloads are acquired from endpoints before inclusion in results.
        records:
        - memory.md#mem-obj-session-results
        - memory.md#mem-rte-history-report
        - runtime.md#rt-rte-request-execution
        note: The documented driver path is known; previous history initialization and plugin-transformed
          payload derivation remain unresolved.
      - scope: Publisher decisions, cache entries and persistent status summaries
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-serve-decisions
        - memory.md#mem-obj-verify-entry-cache
        - memory.md#mem-obj-tool-status-record
        - memory.md#mem-rte-status-write
        note: Provider owns substantive creation and mutation; reduced state/note forwarding does not
          resolve original derivation or cache provenance.
      - scope: Refreshed installed guides and generated index summaries
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - runtime.md#rt-bap-agent-guidance
          - runtime.md#rt-rte-host-registration
          note: Composition copies bundled, cached or community extension guides into the installed collection.
        - value: other-compiled
          basis: wired
          records:
          - runtime.md#rt-bap-agent-guidance
          note: Whitespace-normalized, capped summaries and substituted version text are deterministically
            composed.
        records:
        - runtime.md#rt-bap-agent-guidance
        - runtime.md#rt-rte-host-registration
        note: Imported and composed paths are established, while actual downloaded prose and its original
          authorship/derivation are unavailable. No trace-derived criticism is inferred.
      records:
      - memory.md#mem-obj-response
      - runtime.md#rt-rte-result-write
      - memory.md#mem-rte-runtime-capture
      - memory.md#mem-obj-process-env
      - runtime.md#rt-obj-runtime-vars
      - memory.md#mem-obj-session-results
      - memory.md#mem-rte-history-report
      - runtime.md#rt-rte-request-execution
      - runtime.md#rt-obj-serve-decisions
      - memory.md#mem-obj-verify-entry-cache
      - memory.md#mem-obj-tool-status-record
      - memory.md#mem-rte-status-write
      - runtime.md#rt-bap-agent-guidance
      - runtime.md#rt-rte-host-registration
      note: Known compilation, acquisition and trace extraction are retained beside unresolved original
        provenance, scripts and provider derivation. Authored capture configuration is not the lineage
        of extracted values.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Response content supplied to later callback document context and afforded file readers
        assessment: partial
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-response
          - memory.md#mem-rte-response-reload
          note: Reloaded response blocks supply historical context in callback-visible JSON.
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-obj-response
          note: File inspection affords retained outcomes as reference/evidence.
        records:
        - memory.md#mem-obj-response
        - memory.md#mem-rte-response-reload
        note: Delivery as context is established; unavailable plugin consumers prevent stronger instruction,
          enforcement or factual acceptance claims.
      - scope: Retained runtime bindings supplied to subsequent request substitution
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-rte-runtime-capture
          - memory.md#mem-obj-process-env
          - runtime.md#rt-rte-session-driver
          note: Named retained values provide data/context for later request construction.
        records:
        - memory.md#mem-rte-runtime-capture
        - memory.md#mem-obj-process-env
        - runtime.md#rt-rte-session-driver
        note: This is programmatic input authority, not factual endorsement or improved capacity.
      - scope: Selected-environment state and unresolved script-written bindings
        assessment: partial
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-obj-runtime-vars
          note: Selected environment values select the environment scope used by later requests.
        records:
        - runtime.md#rt-obj-runtime-vars
        - memory.md#mem-rte-runtime-capture
        note: Resolved values feed later execution, but resolver internals and script meanings prevent
          enumerating all effects. Session IDs are access metadata, not a learned policy.
      - scope: History consumed by later report/status/export commands
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-session-results
          - memory.md#mem-rte-history-report
          note: Stored execution entries supply evidence and reference data for reports and counts.
        records:
        - memory.md#mem-obj-session-results
        - memory.md#mem-rte-history-report
        note: No automatic future-request or model-prompt consumer is established for this history path.
      - scope: Publisher retained served-state fields at core refresh comparison
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-obj-serve-decisions
          - runtime.md#rt-rte-tool-publication
          note: Previously retained decisions determine detected state changes and supervised restart
            or later registration input.
        records:
        - runtime.md#rt-obj-serve-decisions
        - runtime.md#rt-rte-tool-publication
        note: The core consumer is known; this does not establish the provider eligibility check.
      - scope: Provider cache, substantive registration policy and persistent status read-back
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-verify-entry-cache
        - runtime.md#rt-obj-serve-decisions
        - memory.md#mem-obj-tool-status-record
        - memory.md#mem-rte-status-write
        - runtime.md#rt-rte-tool-publication
        note: Cache contents may inform checking/selection and status may inform future consumers, but
          actual provider use is unavailable. No validation/enforcement is inferred from verified labels.
      - scope: Provider warning description at external agent tool-list consumer
        assessment: partial
        findings:
        - value: knowledge
          basis: afforded
          records:
          - runtime.md#rt-obj-serve-decisions
          note: Readable description notes are intended to advise the external model about tool status.
        records:
        - runtime.md#rt-obj-serve-decisions
        - runtime.md#rt-rte-tool-publication
        note: Formatting, admission to the description and actual host interpretation are not established.
      - scope: Refreshed guide prose at external foreground agent
        assessment: known
        findings:
        - value: instruction
          basis: afforded
          records:
          - runtime.md#rt-bap-agent-guidance
          - runtime.md#rt-rte-host-registration
          note: Installed guides request discovery, inspection, repair and loading the relevant block
            guide.
        records:
        - runtime.md#rt-bap-agent-guidance
        - runtime.md#rt-rte-host-registration
        note: Directions are advisory standing guidance, not code enforcement; obedience is unobserved.
      - scope: Guide index and paths at on-demand guide loading
        assessment: known
        findings:
        - value: routing
          basis: afforded
          records:
          - runtime.md#rt-bap-agent-guidance
          note: Index membership and paths afford choosing the appropriate full guide.
        records:
        - runtime.md#rt-bap-agent-guidance
        note: This is a documented foreground-agent loading route, not an automatic targeted push.
      records:
      - memory.md#mem-obj-response
      - memory.md#mem-rte-response-reload
      - memory.md#mem-rte-runtime-capture
      - memory.md#mem-obj-process-env
      - runtime.md#rt-rte-session-driver
      - runtime.md#rt-obj-runtime-vars
      - memory.md#mem-obj-session-results
      - memory.md#mem-rte-history-report
      - runtime.md#rt-obj-serve-decisions
      - runtime.md#rt-rte-tool-publication
      - memory.md#mem-obj-verify-entry-cache
      - memory.md#mem-obj-tool-status-record
      - memory.md#mem-rte-status-write
      - runtime.md#rt-bap-agent-guidance
      - runtime.md#rt-rte-host-registration
      note: Authority is assigned at each actual or afforded later consumer. Provider criteria and payload
        effects remain unresolved. Trace learning below does not imply learning authority for every retained
        output.
    write_agency:
      assessment: partial
      units:
      - scope: MCP caller-proposed response admission
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-result-write
        - memory.md#mem-obj-response
        note: No per-result human confirmation is required, but generic caller identity does not establish
          whether a human explicitly supplied/approved this particular retained content. Serializer I/O
          is not the agency decision.
      - scope: Runtime capture, CLI map save and history append
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-runtime-capture
          - memory.md#mem-obj-process-env
          - runtime.md#rt-rte-session-driver
          - memory.md#mem-obj-session-results
          - memory.md#mem-rte-history-report
          note: Software admits extracted values, saves the snapshot and appends computed results without
            per-content operator approval.
        records:
        - memory.md#mem-rte-runtime-capture
        - memory.md#mem-obj-process-env
        - runtime.md#rt-rte-session-driver
        - memory.md#mem-obj-session-results
        - memory.md#mem-rte-history-report
        note: Authored capture rows or starting session mode do not make the subsequent values manual.
      - scope: Environment-map replacement after profile choice
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-obj-runtime-vars
          note: Software resolves and replaces individual environment values after the caller chooses
            a profile.
        records:
        - runtime.md#rt-obj-runtime-vars
        note: Global profile choice is not approval of each retained value; initial profile-file admission
          is unresolved separately.
      - scope: Initial external variable/history edits, profile authorship and plugin script admission
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-runtime-vars
        - memory.md#mem-obj-process-env
        - memory.md#mem-obj-session-results
        - memory.md#mem-rte-runtime-capture
        note: Actual initial state and external content decisions are uncaptured; scripting receives a
          writable map but its admission policy is unavailable.
      - scope: Guide refresh selection and generated installed collection
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-bap-agent-guidance
          - runtime.md#rt-rte-host-registration
          note: Software copies enabled readable guides and regenerates summaries without per-paragraph
            approval.
        records:
        - runtime.md#rt-bap-agent-guidance
        - runtime.md#rt-rte-host-registration
        note: Operator setup/enablement is a trigger, not per-content manual admission.
      - scope: Guide source-content admission
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-bap-agent-guidance
        note: Source authors supply prose but actual human/model control of downloaded guide content is
          not established.
      - scope: CLI provider-status forwarding
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-status-write
          note: --write forwards each computed state/note without individual human approval.
        records:
        - memory.md#mem-rte-status-write
        note: Known dispatch is classified independently of successful provider retention.
      - scope: Publisher decision/cache admission and provider physical status writes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-verify-entry-cache
        - runtime.md#rt-obj-serve-decisions
        - memory.md#mem-obj-tool-status-record
        - memory.md#mem-rte-status-write
        note: Provider creates/checks/adopts these retained parts; interface and caller identity do not
          resolve admission control.
      records:
      - runtime.md#rt-rte-result-write
      - memory.md#mem-obj-response
      - memory.md#mem-rte-runtime-capture
      - memory.md#mem-obj-process-env
      - runtime.md#rt-rte-session-driver
      - memory.md#mem-obj-session-results
      - memory.md#mem-rte-history-report
      - runtime.md#rt-obj-runtime-vars
      - runtime.md#rt-bap-agent-guidance
      - runtime.md#rt-rte-host-registration
      - memory.md#mem-rte-status-write
      - memory.md#mem-obj-verify-entry-cache
      - runtime.md#rt-obj-serve-decisions
      - memory.md#mem-obj-tool-status-record
      note: Automatic software admission is established for capture, driver outputs, guide refresh and
        status forwarding. Caller response control, initialization and provider-owned admission prevent
        a complete agency inventory; no manual value is inferred from workflow initiation.
    curation_operations:
      assessment: partial
      units:
      - scope: Latest retained-response replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-rte-result-write
          - memory.md#mem-obj-response
          note: A later write replaces the existing matching response for the request UID.
        records:
        - memory.md#mem-obj-response
        - runtime.md#rt-rte-result-write
        - epistemic.md#epi-rte-response-serialization
        note: UID placement is not dedup or acceptance. Initial field selection/truncation reshapes caller
          output, but does not by itself establish consolidation over previously retained memory.
      - scope: Runtime-map retained-key replacement and explicit cleanup
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-runtime-capture
          - memory.md#mem-obj-process-env
          note: Successful extraction overwrites an existing named binding; saved snapshots carry the
            changed values.
        - value: decay
          basis: wired
          records:
          - memory.md#mem-obj-process-env
          - runtime.md#rt-rte-session-driver
          note: Explicit session clear deletes the durable variable snapshot.
        records:
        - memory.md#mem-rte-runtime-capture
        - memory.md#mem-obj-process-env
        - runtime.md#rt-rte-session-driver
        note: Failed extraction can preserve old values. Forgetting here is explicit deletion, not a learned
          decay schedule.
      - scope: History cleanup and session lifecycle expiry
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-obj-session-results
          - memory.md#mem-rte-history-report
          - runtime.md#rt-obj-runtime-vars
          note: Report/session clear discards history; HTTP idle sweeping and DELETE discard session state.
        records:
        - memory.md#mem-obj-session-results
        - memory.md#mem-rte-history-report
        - runtime.md#rt-obj-runtime-vars
        note: These are bounded forgetting operations, not withdrawal of recorded remote effects.
      - scope: Guide index summary generation and refreshed body replacement/withdrawal
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - runtime.md#rt-bap-agent-guidance
          note: Whitespace normalization and capped guide summaries reduce existing guidance for the index.
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-bap-agent-guidance
          - runtime.md#rt-rte-host-registration
          note: Refresh replaces the installed guide collection with current composed content.
        - value: decay
          basis: wired
          records:
          - runtime.md#rt-bap-agent-guidance
          - runtime.md#rt-rte-host-registration
          note: Refresh removes the prior extension-guide folder and missing guides are not retained for
            future file reads.
        records:
        - runtime.md#rt-bap-agent-guidance
        - runtime.md#rt-rte-host-registration
        note: Full guide bodies remain separately available after summarization. Deletion does not revoke
          already loaded host copies.
      - scope: Provider status-summary forwarding and its relation to prior retained status
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-tool-status-record
        - memory.md#mem-rte-status-write
        note: CLI reduces current verification output to state/note, but that alone does not establish
          curation over retained memory. Provider persistence and replacement of prior retained status
          are unavailable.
      - scope: Provider cache maintenance, invalidation, status replacement and script mutations
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-verify-entry-cache
        - memory.md#mem-obj-tool-status-record
        - memory.md#mem-rte-status-write
        - runtime.md#rt-obj-serve-decisions
        - memory.md#mem-rte-runtime-capture
        note: Provider transformation/invalidation and script semantics are unavailable; schedule and
          index-rebuild labels establish no controlled curation value.
      records:
      - memory.md#mem-obj-response
      - runtime.md#rt-rte-result-write
      - epistemic.md#epi-rte-response-serialization
      - memory.md#mem-rte-runtime-capture
      - memory.md#mem-obj-process-env
      - runtime.md#rt-rte-session-driver
      - memory.md#mem-obj-session-results
      - memory.md#mem-rte-history-report
      - runtime.md#rt-obj-runtime-vars
      - runtime.md#rt-bap-agent-guidance
      - runtime.md#rt-rte-host-registration
      - memory.md#mem-obj-tool-status-record
      - memory.md#mem-rte-status-write
      - memory.md#mem-obj-verify-entry-cache
      - runtime.md#rt-obj-serve-decisions
      note: Implemented guide-summary consolidation, replacement and forgetting coexist. Opaque provider/script
        branches prevent complete operation coverage; no synthesis, promotion or dedup is inferred from
        labels, acquisition or key matching.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested file inspection and automatic later response-block callback context
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-obj-response
          note: A human/agent can request the retained document for inspection.
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-response-reload
          note: After a later execution request, core automatically supplies retained selected-section
            blocks to builders/hooks without their asking for historical responses.
        records:
        - memory.md#mem-obj-response
        - memory.md#mem-rte-response-reload
        note: The document execution request and internal historical-context supply are different operations;
          immediate new execution output is not another memory push.
      - scope: Later runtime-value substitution and durable snapshot reload
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-runtime-capture
          - memory.md#mem-obj-process-env
          - runtime.md#rt-rte-session-driver
          note: Later templates select bindings and session mode automatically reloads the saved map into
            execution context.
        - value: pull
          basis: wired
          records:
          - memory.md#mem-obj-process-env
          note: session vars explicitly requests display of retained values.
        records:
        - memory.md#mem-rte-runtime-capture
        - memory.md#mem-obj-process-env
        - runtime.md#rt-rte-session-driver
        note: The automatic load and selector are distinct from requested variable display.
      - scope: Requested history report/status/export
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-obj-session-results
          - memory.md#mem-rte-history-report
          note: Later report/status/export commands request the accumulated history.
        records:
        - memory.md#mem-obj-session-results
        - memory.md#mem-rte-history-report
        note: Formatting and requested delivery are not independent pushes.
      - scope: Core cached decision reuse and provider planning input
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-obj-serve-decisions
          - memory.md#mem-obj-verify-entry-cache
          - runtime.md#rt-rte-tool-publication
          note: Startup/ticks automatically pass retained cache state to planning and retained decisions
            to registration.
        records:
        - runtime.md#rt-obj-serve-decisions
        - memory.md#mem-obj-verify-entry-cache
        - runtime.md#rt-rte-tool-publication
        note: This establishes supply to provider calls, not that the provider reads every cached entry.
      - scope: Provider targeted cache consumption, dynamic tool search and persistent status read-back
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-verify-entry-cache
        - runtime.md#rt-obj-serve-decisions
        - runtime.md#rt-rte-tool-publication
        - memory.md#mem-obj-tool-status-record
        - memory.md#mem-rte-status-write
        note: Actual selection/request/delivery semantics and status consumers are unavailable. The dynamic
          flag is not a resolved direction route.
      - scope: Refreshed full-guide loading by foreground agent
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records:
          - runtime.md#rt-bap-agent-guidance
          note: Guidance directs the foreground agent to open the needed full guide on demand.
        records:
        - runtime.md#rt-bap-agent-guidance
        note: This is a documented request route; actual guide loading is unobserved.
      - scope: External host automatic inclusion of installed base/guide collection
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-bap-agent-guidance
        - runtime.md#rt-rte-host-registration
        note: Installation and file persistence do not establish host context assembly, so possible automatic
          inclusion remains unresolved.
      - scope: Selected-environment carry-over and plugin script consumers
        assessment: partial
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-obj-runtime-vars
          note: Fixed handlers automatically supply selected environment values to later execution.
        records:
        - runtime.md#rt-obj-runtime-vars
        - memory.md#mem-rte-runtime-capture
        note: Script-specific later consumers remain unavailable; the known fixed carry-over does not
          resolve them.
      records:
      - memory.md#mem-obj-response
      - memory.md#mem-rte-response-reload
      - memory.md#mem-rte-runtime-capture
      - memory.md#mem-obj-process-env
      - runtime.md#rt-rte-session-driver
      - memory.md#mem-obj-session-results
      - memory.md#mem-rte-history-report
      - runtime.md#rt-obj-serve-decisions
      - memory.md#mem-obj-verify-entry-cache
      - runtime.md#rt-rte-tool-publication
      - memory.md#mem-obj-tool-status-record
      - memory.md#mem-rte-status-write
      - runtime.md#rt-bap-agent-guidance
      - runtime.md#rt-rte-host-registration
      - runtime.md#rt-obj-runtime-vars
      note: Both pull and push have supported local routes. Provider and host selection alternatives remain
        included and unresolved; a known request route cannot establish a globally pull-only boundary.
    read_back_signal:
      assessment: partial
      units:
      - scope: Automatic response-block supply to callbacks
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-response-reload
          note: Trigger is later runVoidFile; file/section rules select all retained blocks in the selected
            context, not responses by semantic relevance.
        records:
        - memory.md#mem-rte-response-reload
        note: A requested file path/placement UID is not an identity-matched targeted push selector.
      - scope: Runtime binding substitution
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-runtime-capture
          - memory.md#mem-obj-process-env
          note: Trigger is later request construction; exact process-variable paths select named retained
            values for substituted fields.
        records:
        - memory.md#mem-rte-runtime-capture
        - memory.md#mem-obj-process-env
        note: This is an actual identity match selecting delivered values, not merely a catalog identifier.
      - scope: Whole durable snapshot reload and selected-environment supply
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-process-env
          - runtime.md#rt-rte-session-driver
          - runtime.md#rt-obj-runtime-vars
          note: Session-mode startup reloads all persisted keys; subsequent fixed requests receive the
            selected resolved environment map.
        records:
        - memory.md#mem-obj-process-env
        - runtime.md#rt-rte-session-driver
        - runtime.md#rt-obj-runtime-vars
        note: Whole-map carry-over is separate from identifier targeting inside later substitution.
      - scope: Core publisher planning/registration supply
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-obj-serve-decisions
          - memory.md#mem-obj-verify-entry-cache
          - runtime.md#rt-rte-tool-publication
          note: Startup/ticks supply the cache and current decision collection wholesale to provider calls.
        records:
        - runtime.md#rt-obj-serve-decisions
        - memory.md#mem-obj-verify-entry-cache
        - runtime.md#rt-rte-tool-publication
        note: Core supply is known; provider entry matching and dynamic-mode targeting are not.
      - scope: History report requested return
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-obj-session-results
        - memory.md#mem-rte-history-report
        note: 'This assessed route is pull-only: callers request all retained entries and their report
          format; no independent automatic selector supplies history.'
      - scope: Foreground full-guide requested read
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-bap-agent-guidance
        note: The documented opening of a guide is a requested pull, so that operation has no push signal.
          This does not cover external host injection.
      - scope: Provider dynamic targeting/cache selection, status read-back, host base loading and script
          consumers
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-serve-decisions
        - memory.md#mem-obj-verify-entry-cache
        - runtime.md#rt-rte-tool-publication
        - memory.md#mem-obj-tool-status-record
        - memory.md#mem-rte-status-write
        - runtime.md#rt-bap-agent-guidance
        - runtime.md#rt-rte-host-registration
        - memory.md#mem-rte-runtime-capture
        note: Missing actual selectors, trigger inputs and selected payloads prevent additional signal
          values or inapplicability for these alternatives.
      records:
      - memory.md#mem-rte-response-reload
      - memory.md#mem-rte-runtime-capture
      - memory.md#mem-obj-process-env
      - runtime.md#rt-rte-session-driver
      - runtime.md#rt-obj-runtime-vars
      - runtime.md#rt-obj-serve-decisions
      - memory.md#mem-obj-verify-entry-cache
      - runtime.md#rt-rte-tool-publication
      - memory.md#mem-obj-session-results
      - memory.md#mem-rte-history-report
      - runtime.md#rt-bap-agent-guidance
      - memory.md#mem-obj-tool-status-record
      - memory.md#mem-rte-status-write
      - runtime.md#rt-rte-host-registration
      note: Coarse supply and exact binding identity selection are established. Inapplicability is local
        to assessed requested reads; opaque push alternatives prevent an axis-wide inapplicability or
        complete selector inventory.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatic execution capture with standalone durable binding persistence and later substitution
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-runtime-capture
          - memory.md#mem-obj-process-env
          - runtime.md#rt-rte-session-driver
          note: Request/response traces feed automatic extraction, retained JSON bindings and subsequent
            request behavior through substitution.
        records:
        - memory.md#mem-rte-runtime-capture
        - memory.md#mem-obj-process-env
        - runtime.md#rt-rte-session-driver
        note: This wired trace-fed behavior-shaping chain needs neither novel knowledge nor an observed
          capacity improvement. The durable standalone route is the positive witness.
      - scope: Recorded response admission and later plugin use
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-result-write
        - memory.md#mem-obj-response
        - memory.md#mem-rte-response-reload
        note: Caller provenance/admission control and unavailable plugin behavior prevent determining
          an automatic trace-fed durable behavior-shaping chain; serialization alone does not establish
          it.
      - scope: Raw accumulated execution history and its report consumer
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-obj-session-results
        - memory.md#mem-rte-history-report
        note: This inspected route retains raw outcomes for reporting, not an automatically produced durable
          behavior-shaping derivative. It cannot yield a qualifying learning route from history retention
          alone.
      - scope: Refreshed guide collection and index summaries
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-bap-agent-guidance
        - runtime.md#rt-rte-host-registration
        note: The inspected composition route imports/statically reshapes guides rather than consuming
          activity traces. External guide-authoring processes are not resolved by this unit.
      - scope: Initial bindings, environment acquisition, script writes and source-guide updates
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-runtime-vars
        - memory.md#mem-obj-process-env
        - memory.md#mem-rte-runtime-capture
        - runtime.md#rt-bap-agent-guidance
        note: Uncaptured initial provenance, resolver details and opaque script/source updates prevent
          qualifying or excluding further trace-fed writes.
      - scope: Provider decision/cache/status transformation and later consumption
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-serve-decisions
        - memory.md#mem-obj-verify-entry-cache
        - memory.md#mem-obj-tool-status-record
        - memory.md#mem-rte-status-write
        - runtime.md#rt-rte-tool-publication
        note: Provider verification might yield qualifying retained updates, but original inputs, actual
          write/persistence and later consumers are unavailable.
      records:
      - memory.md#mem-rte-runtime-capture
      - memory.md#mem-obj-process-env
      - runtime.md#rt-rte-session-driver
      - runtime.md#rt-rte-result-write
      - memory.md#mem-obj-response
      - memory.md#mem-rte-response-reload
      - memory.md#mem-obj-session-results
      - memory.md#mem-rte-history-report
      - runtime.md#rt-bap-agent-guidance
      - runtime.md#rt-rte-host-registration
      - runtime.md#rt-obj-runtime-vars
      - runtime.md#rt-obj-serve-decisions
      - memory.md#mem-obj-verify-entry-cache
      - memory.md#mem-obj-tool-status-record
      - memory.md#mem-rte-status-write
      - runtime.md#rt-rte-tool-publication
      note: A wired yes belongs to the durable capture/substitution route, not a system-level improvement
        claim. Raw reporting and deterministic guide packaging are locally inapplicable; unresolved write
        alternatives prevent complete trace-learning coverage. No unsupported no is asserted.
    trace_source:
      assessment: partial
      units:
      - scope: Qualifying durable runtime capture route
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-rte-runtime-capture
          - memory.md#mem-obj-process-env
          - runtime.md#rt-rte-session-driver
          note: 'Configured extraction consumes request fields and execution-response/result fields: recorded
            tool request/result material.'
        records:
        - memory.md#mem-rte-runtime-capture
        - memory.md#mem-obj-process-env
        - runtime.md#rt-rte-session-driver
        note: Original input is execution material, not a conversational session or an event-stream merely
          because the driver is called a session.
      - scope: Raw report-history retention without qualifying derivative
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-obj-session-results
        - memory.md#mem-rte-history-report
        note: No qualifying trace-learning write is established in this fully described report-only route;
          raw tool outcomes are not a positive trace_source absent such a write.
      - scope: Deterministic guide-copy/index route
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-bap-agent-guidance
        - runtime.md#rt-rte-host-registration
        note: The assessed refresh consumes guide prose, not traces, and is not a qualifying trace-learning
          write.
      - scope: Response/caller route, initial/environment/script bindings, source-guide updates and provider
          verification retention
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-result-write
        - memory.md#mem-obj-response
        - memory.md#mem-rte-response-reload
        - runtime.md#rt-obj-runtime-vars
        - memory.md#mem-rte-runtime-capture
        - memory.md#mem-obj-process-env
        - runtime.md#rt-bap-agent-guidance
        - runtime.md#rt-obj-serve-decisions
        - memory.md#mem-obj-verify-entry-cache
        - memory.md#mem-obj-tool-status-record
        - memory.md#mem-rte-status-write
        - runtime.md#rt-rte-tool-publication
        note: Qualification and/or original inputs of these included writes remain unresolved. Missing
          provenance prevents enumerating their trace sources; the known tool-trace witness does not resolve
          them.
      records:
      - memory.md#mem-rte-runtime-capture
      - memory.md#mem-obj-process-env
      - runtime.md#rt-rte-session-driver
      - memory.md#mem-obj-session-results
      - memory.md#mem-rte-history-report
      - runtime.md#rt-bap-agent-guidance
      - runtime.md#rt-rte-host-registration
      - runtime.md#rt-rte-result-write
      - memory.md#mem-obj-response
      - memory.md#mem-rte-response-reload
      - runtime.md#rt-obj-runtime-vars
      - runtime.md#rt-obj-serve-decisions
      - memory.md#mem-obj-verify-entry-cache
      - memory.md#mem-obj-tool-status-record
      - memory.md#mem-rte-status-write
      - runtime.md#rt-rte-tool-publication
      note: Tool-traces is supported only for the qualifying durable capture route. Opaque alternative
        inputs remain unresolved rather than being assigned session-logs, event-streams or trajectories
        from names or serialization.
---

# Voiden memory profile

## Comparison rationale

The comparison covers memory produced or changed through use, not all storage in the runtime. The inventories distinguish a response record, a binding snapshot, raw outcome history and provider-defined verification state. Their later consumers differ. Installed guidance is included only as the use-refreshed collection and its access index; unchanged shipped prose and downloaded executable capabilities are not counted as learned memory. The record-backed inventory is in [MEM-OBJ-response](memory.md#mem-obj-response), [MEM-OBJ-process-env](memory.md#mem-obj-process-env), [MEM-OBJ-session-results](memory.md#mem-obj-session-results), [MEM-OBJ-verify-entry-cache](memory.md#mem-obj-verify-entry-cache), [MEM-OBJ-tool-status-record](memory.md#mem-obj-tool-status-record) and [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance).

There are no supersessions affecting these values. Reconciliation retains valid containers alongside their separately assessed parts: runtime variables versus durable JSON, and served decisions versus cache. The CLI status writer and verification consumer overlap without replacing one another. This profile cites each retained canonical declaration rather than assigning the broader container's warrant to its opaque parts.

The strongest positive trace-learning witness is automatic request/response extraction, durable standalone snapshot persistence and later named-value substitution: [MEM-RTE-runtime-capture](memory.md#mem-rte-runtime-capture), [MEM-OBJ-process-env](memory.md#mem-obj-process-env) and [RT-RTE-session-driver](runtime.md#rt-rte-session-driver). That is wired trace-fed behavior shaping, not demonstrated improvement, reflection or a methodological theory update. Its original input is tool request/result material, not session logs merely because the CLI uses session mode. Raw history reporting has a concrete later consumer but no qualifying behavior-shaping derivative in its inspected route: [MEM-RTE-history-report](memory.md#mem-rte-history-report).

Selected retained bindings provide symbolic request inputs. Response blocks provide callback context and afford file inspection, but unavailable plugin semantics prevent attributing enforcement or instruction authority to their contents: [MEM-RTE-response-reload](memory.md#mem-rte-response-reload). The core decision-state comparison has routing force; provider registration, verification/cache use and status read-back are separate unresolved effects in [RT-RTE-tool-publication](runtime.md#rt-rte-tool-publication). A readable description note does not classify the opaque consumed runResult. No retained validation or learning authority is inferred merely from status labels or the positive trace-learning route.

Curation includes replacement of a matching retained response. Initial selection/truncation reshapes caller output but does not independently establish consolidation of prior retained memory. These distinct transformations are documented in [EPI-RTE-response-serialization](epistemic.md#epi-rte-response-serialization) and [RT-RTE-result-write](runtime.md#rt-rte-result-write). Explicit deletion/expiry counts as forgetting, not rollback of remote effects. Deterministic guide summaries consolidate existing retained guide content, not a synthesized claim. Provider status forwarding reduces current output to the upsert payload, but actual retained-memory curation and storage remain unresolved in [MEM-RTE-status-write](memory.md#mem-rte-status-write).

Requested file inspection and history reporting are pulls. Supplying selected-section historical blocks to callbacks is a distinct internal push with coarse scope, not identifier targeting merely because the user requested a named file. Binding substitution is identifier-targeted push; whole-map reload is coarse. Provider dynamic-mode search, cache entry selection and host guide injection are unresolved, so local pull-only operations cannot make the signal axis inapplicable. See [MEM-RTE-response-reload](memory.md#mem-rte-response-reload), [MEM-RTE-runtime-capture](memory.md#mem-rte-runtime-capture), [MEM-RTE-history-report](memory.md#mem-rte-history-report) and [RT-OBJ-serve-decisions](runtime.md#rt-obj-serve-decisions).

Every axis remains partial because its included inventory contains unresolved alternatives. Evidence strength remains attached to the local mechanism: implemented transformations and delivery are wired; documented file inspection, guide loading and warning interpretation are afforded. Neither means observed activation. Generic caller identity prevents classifying response content as manual or automatic; starting a workflow does not turn software-generated bindings/history into manual writes. Missing provider implementation, actual initial/project content, plugin script semantics and external host context policy prevent stronger coverage. Those gaps are retained rather than treated as bounded absences.

Source-read log: no frozen source files were read for this profile. Classification uses only supplied accepted records and their annotations; no new evidence, quotes or records were added.
