---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "EchoesVault for OpenCode memory comparison: managed project text, derived discovery, persisted bookkeeping and unresolved raw/asset paths."
run-id: "AAS-2026-10-15-echoes-vault-opencode-239c6738bb9e-01"
source-identity: "https://github.com/psinetron/echoes-vault-opencode"
reviewed-boundary: "875c45aa45559529b87a7481b0c21e6dfd8c5eb0"
memory-comparison:
  version: 2
  scope: "Included: accumulated page bodies/frontmatter, daily entries, generated index, persisted session/access bookkeeping, raw/assets, and their proposal, admission, maintenance and later-consumer routes. Excluded: shipped static guides/protocol/command templates, installed executable machinery, external host weights/provider state, host compaction and arbitrary future compatible runtimes. Initial origins and independent raw/asset routes remain unresolved, not excluded."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        - scope: "Page bodies/frontmatter, generated index and daily entries"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-body"
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-daily"
              note: "These operative retained parts reside in local Markdown files."
          records:
            - "memory.md#mem-obj-page-body"
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-daily"
          note: "The records inventory all managed knowledge files, including legacy daily files."
        - scope: "Persisted session/access bookkeeping"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-local-state"
              note: "Local state is a JSON file, including legacy-state fallback paths."
          records:
            - "memory.md#mem-obj-local-state"
          note: "JSON is encoding, not a separate substrate."
        - scope: "Raw source and asset containers/payloads"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-material"
              note: "The included raw and asset surfaces are local filesystem containers and files."
          records:
            - "memory.md#mem-obj-source-material"
          note: "Unknown payload encodings and producers do not obscure their recorded filesystem substrate."
      records:
        - "memory.md#mem-obj-page-body"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-daily"
        - "memory.md#mem-obj-local-state"
        - "memory.md#mem-obj-source-material"
      note: "The memory inventory is files throughout, including unresolved raw/assets. Host weights, installed executables and static templates are outside this accumulated-memory scope; repository locality alone does not add a repo substrate."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Page bodies, authored summaries, index descriptions and daily text at host interpretation"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-body"
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-daily"
                - "runtime.md#rt-rte-context-restore"
              note: "Retained Markdown prose reaches host interpretation through restoration/search; full-page reading is separately afforded."
          records:
            - "memory.md#mem-obj-page-body"
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-daily"
            - "runtime.md#rt-rte-context-restore"
          note: "The classification concerns encoding and delivery, not successful interpretation or true project claims."
        - scope: "Page metadata keys/status, discovery identifiers and daily wrappers at fixed parsers/selectors"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-daily"
                - "runtime.md#rt-rte-context-restore"
              note: "Fixed rules consume required keys, deprecated equality, page identifiers and filename order."
          records:
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-daily"
            - "runtime.md#rt-rte-context-restore"
          note: "Separate from the prose consumed by the host; wrappers do not authenticate provenance."
        - scope: "Local session/access state at maintenance and TUI consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-local-state"
                - "memory.md#mem-rte-health-report"
              note: "Boolean/count/string fields drive fixed display and maintenance rules."
          records:
            - "memory.md#mem-obj-local-state"
            - "memory.md#mem-rte-health-report"
          note: "Rendered labels do not turn the stored bookkeeping into a retained semantic evaluation."
        - scope: "Raw source and asset payloads"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-material"
          note: "Payload encodings and actual consuming tools are unresolved. Document link syntax does not classify the referenced payload."
      records:
        - "memory.md#mem-obj-page-body"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-daily"
        - "runtime.md#rt-rte-context-restore"
        - "memory.md#mem-obj-local-state"
        - "memory.md#mem-rte-health-report"
        - "memory.md#mem-obj-source-material"
      note: "Mixed known prose and symbolic managed parts coexist with unknown raw/asset payload forms. No parametric memory finding follows from the external host model."
    lineage:
      assessment: "partial"
      units:
        - scope: "Caller-proposed page text/frontmatter and daily notes on the documented proposal path"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-body"
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-daily"
                - "runtime.md#rt-rte-page-upsert"
                - "runtime.md#rt-rte-daily-append"
                - "runtime.md#rt-rte-session-save"
              note: "Callers supply complete page text or notes rather than the engine deriving their meaning."
          records:
            - "memory.md#mem-obj-page-body"
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-daily"
            - "runtime.md#rt-rte-page-upsert"
            - "runtime.md#rt-rte-daily-append"
            - "runtime.md#rt-rte-session-save"
          note: "Authorship may be computational; this says nothing about human approval or earlier source provenance."
        - scope: "Requested session-to-summary/page derivation"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-session-distill"
                - "runtime.md#rt-rte-session-save"
              note: "The prompt requests a model distillation of session experience for later restoration."
          records:
            - "epistemic.md#epi-rte-session-distill"
            - "runtime.md#rt-rte-session-save"
          note: "This local path is prescribed only; prompt delivery and file writing do not upgrade semantic derivation to wired."
        - scope: "Generated discovery index and normalized wrappers/bookkeeping"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-daily"
                - "memory.md#mem-obj-local-state"
                - "epistemic.md#epi-rte-index-render"
              note: "Code renders page summaries, wraps submitted entries and refreshes counters/flags."
          records:
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-daily"
            - "memory.md#mem-obj-local-state"
            - "epistemic.md#epi-rte-index-render"
          note: "These fixed derivations do not establish original source warrant."
        - scope: "Legacy description copied into missing canonical summary"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-rte-summary-migration"
              note: "Migration takes a preexisting legacy-index description into page summary metadata."
          records:
            - "memory.md#mem-rte-summary-migration"
          note: "This is a known local import path; the description initial origin remains unresolved."
        - scope: "Initial/preexisting pages, daily files, legacy descriptions and raw/assets"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-page-body"
            - "memory.md#mem-obj-daily"
            - "memory.md#mem-rte-summary-migration"
            - "memory.md#mem-obj-source-material"
          note: "Initial authors/import sources and derivations are unresolved. Known subsequent copying and rendering cannot complete that history."
      records:
        - "memory.md#mem-obj-page-body"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-daily"
        - "runtime.md#rt-rte-page-upsert"
        - "runtime.md#rt-rte-daily-append"
        - "runtime.md#rt-rte-session-save"
        - "epistemic.md#epi-rte-session-distill"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-local-state"
        - "epistemic.md#epi-rte-index-render"
        - "memory.md#mem-rte-summary-migration"
        - "memory.md#mem-obj-source-material"
      note: "Known authored, compiled, imported and prescribed trace-extracted paths do not exhaust initial provenance. No embedding lineage is asserted."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Page/daily/index content at later host and status bookkeeping at operator"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-body"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-daily"
                - "memory.md#mem-obj-local-state"
                - "runtime.md#rt-rte-context-restore"
                - "memory.md#mem-rte-health-report"
              note: "Restored prose supplies project context; persisted session flags/counters supply status information to later display consumers."
          records:
            - "memory.md#mem-obj-page-body"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-daily"
            - "memory.md#mem-obj-local-state"
            - "runtime.md#rt-rte-context-restore"
            - "memory.md#mem-rte-health-report"
          note: "Delivery and display establish the local force, not compliance, factual endorsement or beneficial decisions."
        - scope: "Current retained page bytes at replacement preflight"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-page-upsert"
                - "memory.md#mem-obj-page-body"
              note: "The digest of current retained bytes supplies the comparison reference for expectedSha256."
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-page-upsert"
                - "memory.md#mem-obj-page-body"
              note: "A mismatch with that current-content reference vetoes replacement."
          records:
            - "runtime.md#rt-rte-page-upsert"
            - "memory.md#mem-obj-page-body"
          note: "This is concurrency authority, not project-truth validation or authority of a retained schema."
        - scope: "Session experience at the requested distillation consumer"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-session-distill"
                - "runtime.md#rt-rte-session-save"
              note: "Session experience is requested as input to durable summaries/pages that later hosts receive as context."
          records:
            - "epistemic.md#epi-rte-session-distill"
            - "runtime.md#rt-rte-session-save"
          note: "The update-consumer force remains prescribed; downstream output knowledge authority is independently wired."
        - scope: "Raw/asset payloads at later host-tool consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-material"
          note: "Reference syntax affords access but does not identify actual payload consumption or its authority."
      records:
        - "memory.md#mem-obj-page-body"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-daily"
        - "memory.md#mem-obj-local-state"
        - "runtime.md#rt-rte-context-restore"
        - "memory.md#mem-rte-health-report"
        - "runtime.md#rt-rte-page-upsert"
        - "epistemic.md#epi-rte-session-distill"
        - "runtime.md#rt-rte-session-save"
        - "memory.md#mem-obj-source-material"
      note: "Project knowledge, concurrency criteria/veto and prescribed experience-to-artifact learning have distinct consumers. Static guides and executable machinery are excluded; neither supplies an instruction/enforcement finding for accumulated content merely by being installed. Literal inclusion and stable file order do not establish relative-priority ranking."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Managed append/upsert/end admission, including page replacements"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-page-upsert"
                - "runtime.md#rt-rte-daily-append"
                - "runtime.md#rt-rte-session-save"
              note: "Software admits caller/model proposals without a per-content human decision; end initiation is not per-claim approval."
          records:
            - "runtime.md#rt-rte-page-upsert"
            - "runtime.md#rt-rte-daily-append"
            - "runtime.md#rt-rte-session-save"
          note: "Tool and direct CLI alternatives share software admission; a caller-provided confirmation is not evidence of human content approval."
        - scope: "Index/state regeneration and legacy summary migration"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-local-state"
                - "memory.md#mem-rte-summary-migration"
                - "epistemic.md#epi-rte-index-render"
              note: "Deterministic software chooses generated rows, refreshed bookkeeping and eligible legacy summary insertions."
          records:
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-local-state"
            - "memory.md#mem-rte-summary-migration"
            - "epistemic.md#epi-rte-index-render"
          note: "Starting maintenance does not make each generated-content admission manual."
        - scope: "Requested host session-distillation admission to proposed artifacts"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-session-distill"
                - "runtime.md#rt-rte-session-save"
              note: "The host model is asked to select session content without per-fact operator approval."
          records:
            - "epistemic.md#epi-rte-session-distill"
            - "runtime.md#rt-rte-session-save"
          note: "Classification retains the weaker evidence layer of semantic selection."
        - scope: "Initial/preexisting file admission and independent raw/asset writes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-page-body"
            - "memory.md#mem-obj-daily"
            - "memory.md#mem-obj-source-material"
          note: "Generic caller identity and available containers do not establish explicit human decisions or automatic admission on these paths."
      records:
        - "runtime.md#rt-rte-page-upsert"
        - "runtime.md#rt-rte-daily-append"
        - "runtime.md#rt-rte-session-save"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-local-state"
        - "memory.md#mem-rte-summary-migration"
        - "epistemic.md#epi-rte-index-render"
        - "epistemic.md#epi-rte-session-distill"
        - "memory.md#mem-obj-page-body"
        - "memory.md#mem-obj-daily"
        - "memory.md#mem-obj-source-material"
      note: "Known software admission is not erased by unresolved initial control. No manual positive is supported merely because users initiate lifecycle commands."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Existing-page whole replacement through upsert/end"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-page-upsert"
                - "runtime.md#rt-rte-session-save"
              note: "The writer supports validated replacement of an existing knowledge entry."
          records:
            - "runtime.md#rt-rte-page-upsert"
            - "runtime.md#rt-rte-session-save"
          note: "Revision capability is wired; a particular semantic improvement is not observed."
        - scope: "Requested reduction of retained session experience to durable summary/pages"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-session-distill"
                - "runtime.md#rt-rte-session-save"
              note: "The requested transformation compresses session work to dense outcomes rather than a transcript."
          records:
            - "epistemic.md#epi-rte-session-distill"
            - "runtime.md#rt-rte-session-save"
          note: "The model transformation is prescribed; the engine sees only submitted products. No synthesis is inferred from an unknown semantic relation."
        - scope: "Deprecation warning and replacement-link practice"
          assessment: "known"
          findings:
            - value: "invalidate"
              basis: "afforded"
              records:
                - "runtime.md#rt-obj-agent-protocol"
                - "memory.md#mem-obj-page-metadata"
                - "epistemic.md#epi-rte-index-render"
              note: "Guidance affords withdrawing current reliance while retaining the old page and directing readers to its replacement."
          records:
            - "runtime.md#rt-obj-agent-protocol"
            - "memory.md#mem-obj-page-metadata"
            - "epistemic.md#epi-rte-index-render"
          note: "The wired status prefix is advisory only; replacement links and withdrawal compliance are not validated or enforced."
        - scope: "Initial/raw/asset maintenance and unspecified caller transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-material"
            - "memory.md#mem-obj-page-body"
            - "memory.md#mem-obj-daily"
          note: "The records do not establish operations over these payloads or the semantic relation of arbitrary proposals. This prevents a complete curation inventory."
      records:
        - "runtime.md#rt-rte-page-upsert"
        - "runtime.md#rt-rte-session-save"
        - "epistemic.md#epi-rte-session-distill"
        - "runtime.md#rt-obj-agent-protocol"
        - "memory.md#mem-obj-page-metadata"
        - "epistemic.md#epi-rte-index-render"
        - "memory.md#mem-obj-source-material"
        - "memory.md#mem-obj-page-body"
        - "memory.md#mem-obj-daily"
      note: "Index regeneration, summary relocation and whitespace normalization alone do not add consolidate/dedup/synthesize. Supported replacement, prescribed consolidation and afforded invalidation retain separate bases; no blanket curation absence is asserted."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Start/search requests and their selected delivery of managed knowledge"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-restore"
                - "memory.md#mem-obj-page-body"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-daily"
              note: "User/agent requests start or search; filename selection and line matching fulfill that request, not independent push."
          records:
            - "runtime.md#rt-rte-context-restore"
            - "memory.md#mem-obj-page-body"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-daily"
          note: "Automatic selection inside a requested return is still pull; result and count caps are not token budgets."
        - scope: "Host-directed complete-page reads"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-page-body"
                - "runtime.md#rt-rte-context-restore"
              note: "Generated guidance directs the host to request relevant complete pages using its own tools."
          records:
            - "memory.md#mem-obj-page-body"
            - "runtime.md#rt-rte-context-restore"
          note: "No actual complete-page reads are supplied."
        - scope: "Persisted session state on periodic TUI display"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-local-state"
                - "memory.md#mem-rte-health-report"
              note: "Every three seconds the TUI polls retained state and presents its fields without a new request for those contents."
          records:
            - "memory.md#mem-obj-local-state"
            - "memory.md#mem-rte-health-report"
          note: "This is access/status memory delivery to the operator, not unsolicited project-knowledge injection into a model."
        - scope: "Raw/asset referenced payload delivery"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-material"
          note: "References do not establish a dedicated retained-payload read-back operation or resolve independent host-tool routes."
      records:
        - "runtime.md#rt-rte-context-restore"
        - "memory.md#mem-obj-page-body"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-daily"
        - "memory.md#mem-obj-local-state"
        - "memory.md#mem-rte-health-report"
        - "memory.md#mem-obj-source-material"
      note: "Both request-driven project reload and periodic bookkeeping display are included. Opaque independent raw/asset consumption prevents complete direction coverage."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Periodic TUI push of persisted session/access bookkeeping"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-local-state"
                - "memory.md#mem-rte-health-report"
              note: "Trigger is the three-second poll; selector is fixed workspace state availability/field selection; selected retained parts are session flags, versions, counts and writer metadata."
          records:
            - "memory.md#mem-obj-local-state"
            - "memory.md#mem-rte-health-report"
          note: "This coarse fixed-field display has no task query, embedding or identity-match targeting."
        - scope: "Requested start/search and afforded complete-page delivery"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-context-restore"
            - "memory.md#mem-obj-page-body"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-daily"
          note: "These are pull operations; recent filename selection, literal queries and requested paths are not push signals."
        - scope: "Independent raw/asset delivery alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-material"
          note: "Whether a push route exists and which payload selector it uses is unresolved; known managed pull routes cannot make this branch inapplicable."
      records:
        - "memory.md#mem-obj-local-state"
        - "memory.md#mem-rte-health-report"
        - "runtime.md#rt-rte-context-restore"
        - "memory.md#mem-obj-page-body"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-daily"
        - "memory.md#mem-obj-source-material"
      note: "The coarse positive is local to TUI bookkeeping. Lexical matching on a pull request does not establish inferred-lexical push; page identifiers on index rows do not establish identifier-targeted push."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Requested session distillation to retained final notes/pages and later host context"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-session-distill"
                - "runtime.md#rt-rte-session-save"
                - "runtime.md#rt-rte-context-restore"
              note: "Session experience is requested to feed automatic model-produced durable summaries/pages that later start/search/read routes expose as context."
          records:
            - "epistemic.md#epi-rte-session-distill"
            - "runtime.md#rt-rte-session-save"
            - "runtime.md#rt-rte-context-restore"
          note: "This meets the trace-to-artifact-to-later-consumer shape at the prescribed layer, not observed learning or measured improved capacity. Wired persistence does not upgrade the semantic producer."
        - scope: "Arbitrary append/upsert inputs, legacy content and raw/asset-derived alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-daily-append"
            - "runtime.md#rt-rte-page-upsert"
            - "memory.md#mem-obj-daily"
            - "memory.md#mem-obj-page-body"
            - "memory.md#mem-obj-source-material"
          note: "The records do not establish whether these inputs are traces or derived behavior-shaping artifacts. No bounded trace-learning negative covers them."
      records:
        - "epistemic.md#epi-rte-session-distill"
        - "runtime.md#rt-rte-session-save"
        - "runtime.md#rt-rte-context-restore"
        - "runtime.md#rt-rte-daily-append"
        - "runtime.md#rt-rte-page-upsert"
        - "memory.md#mem-obj-daily"
        - "memory.md#mem-obj-page-body"
        - "memory.md#mem-obj-source-material"
      note: "A claimed qualifying route supports a local positive. Unknown input lineage prevents complete coverage; lack of background conversation capture does not negate foreground-agent distillation."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Conversational session input to requested finalization distillation"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-session-distill"
                - "runtime.md#rt-rte-session-save"
              note: "The host is asked to distill its current work session into final outcomes and reusable pages."
          records:
            - "epistemic.md#epi-rte-session-distill"
            - "runtime.md#rt-rte-session-save"
          note: "Original conversational content, not JSON payload role labels, supplies this source mapping."
        - scope: "Other content of the host session and independent trace-fed proposals"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-session-distill"
            - "runtime.md#rt-rte-session-save"
            - "runtime.md#rt-rte-daily-append"
            - "runtime.md#rt-rte-page-upsert"
            - "memory.md#mem-obj-source-material"
          note: "Actual host context assembly and complete trace provenance are not supplied. Tool requests/results or linked state-action-outcome sequences cannot be classified merely from the word session; raw/assets may have independent origins."
      records:
        - "epistemic.md#epi-rte-session-distill"
        - "runtime.md#rt-rte-session-save"
        - "runtime.md#rt-rte-daily-append"
        - "runtime.md#rt-rte-page-upsert"
        - "memory.md#mem-obj-source-material"
      note: "The prescribed conversational route does not classify all possible mixed host inputs. No event-streams value follows from timestamps or note wrappers; absence of other sources is not established."
---

# EchoesVault for OpenCode memory profile

## Comparison rationale

This profile classifies accepted records only. No source files were read, no records were declared and no report finding was revised. All positive bases remain local: deterministic persistence cannot turn requested semantic distillation into an implemented transformation. The model proposal path supports claimed trace extraction, consolidation and trace learning; software admission and later delivery are separately wired. See [EPI-RTE-session-distill](epistemic.md#epi-rte-session-distill), [RT-RTE-session-save](runtime.md#rt-rte-session-save) and [RT-RTE-context-restore](runtime.md#rt-rte-context-restore).

The reconciliation supersedes the epistemic daily object with [MEM-OBJ-daily](memory.md#mem-obj-daily), and the epistemic migration route with [MEM-RTE-summary-migration](memory.md#mem-rte-summary-migration). The profile uses those canonical records. The complete-page container and its body/frontmatter parts remain distinct valid records; summary source and derived index likewise remain separate operative parts. These dispositions change citation ownership, not values or evidence strength.

Current page text has two consumers: the host receives knowledge, while replacement preflight uses its digest as a concurrency reference and enforced veto. That narrowly scoped validation/enforcement is independent of factual acceptance. The generated schema and lifecycle grant are not accumulated knowledge and are not used to inflate authority findings. See [MEM-OBJ-page-body](memory.md#mem-obj-page-body), [RT-RTE-page-upsert](runtime.md#rt-rte-page-upsert) and [EPI-ABS-semantic-check](epistemic.md#epi-abs-semantic-check).

Managed project restoration is pull even though code chooses recent filenames and matching lines inside the request. The periodic TUI is a separate push consumer of persisted bookkeeping; its fixed-field selection supplies coarse signal, not task-relevant targeting. Raw/assets have known file storage but unresolved payload forms, origin, control and consumers. Their uncertainty remains in each affected axis rather than being erased by the better-inspected managed paths. See [MEM-OBJ-local-state](memory.md#mem-obj-local-state), [MEM-RTE-health-report](memory.md#mem-rte-health-report), [RT-RTE-context-restore](runtime.md#rt-rte-context-restore) and [MEM-OBJ-source-material](memory.md#mem-obj-source-material).

No observation or causal comparison is supplied. The profile therefore makes no claim of deployed compliance, faithful compression, verified saved facts, complete trace provenance or improved future decisions. Missing initial provenance limits lineage and control, not the known file substrate. Unknown actual input/output content prevents adding synthesis or extra trace-source values; it does not erase the prescribed session-distillation route. See [EPI-RTE-session-distill](epistemic.md#epi-rte-session-distill), [MEM-OBJ-daily](memory.md#mem-obj-daily) and [MEM-OBJ-page-body](memory.md#mem-obj-page-body).
