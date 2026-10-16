---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "SkillNote memory comparison of retained procedures, archives, installed copies, access state and feedback at the frozen revision."
run-id: AAS-2026-10-14-skillnote-0ccfe85cda4a-01
source-identity: "https://github.com/luna-prompts/SkillNote"
reviewed-boundary: "7ea2fc7a8435af64d1c080d8765c0eabba1121ea"
memory-comparison:
  version: 2
  scope: >-
    Accumulated current skill rows, content history and staged inbound bodies,
    independently published archives, installed project/user copies, browser-local
    fallback, comments, ratings, usage/call events and watcher state; their
    admission, maintenance, selection and later-consumer routes. Includes opaque
    archive payloads, arbitrary extra frontmatter and usage metadata as unresolved
    parts. Excludes shipped static authoring/adapter policies as memory objects,
    ordinary transient hook/bundle responses, and external-host weights and
    compaction state. Static policies remain evidence of memory routes.
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Registry current rows, snapshots/staging, release metadata, comments, ratings and usage/call events"
          assessment: known
          findings:
            - value: rdbms
              basis: wired
              records: [memory.md#mem-obj-skill, memory.md#mem-obj-content-version, memory.md#mem-obj-skill-version, memory.md#mem-obj-comment, memory.md#mem-obj-usage-event, memory.md#mem-rte-trace-reporting, epistemic.md#epi-rte-rating-admission]
              note: "Postgres tables retain these objects; JSONB and text are encodings within that substrate."
          records: [memory.md#mem-obj-skill, memory.md#mem-obj-content-version, memory.md#mem-obj-skill-version, memory.md#mem-obj-comment, memory.md#mem-obj-usage-event, memory.md#mem-rte-trace-reporting, epistemic.md#epi-rte-rating-admission]
          note: "The declared stores cover the named database parts, not every analytics consumer."
        - scope: "Published archive bytes, installed skill copies/manifests and watcher cursor state"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [runtime.md#rt-rte-bundle-install, runtime.md#rt-rte-project-sync, runtime.md#rt-rte-openclaw-use, memory.md#mem-obj-watcher-state, memory.md#mem-rte-install-maintenance]
              note: "Publication writes a bundle file; adapters retain files and manifests; watcher recovery uses local JSON."
          records: [runtime.md#rt-rte-bundle-install, runtime.md#rt-rte-project-sync, runtime.md#rt-rte-openclaw-use, memory.md#mem-obj-watcher-state, memory.md#mem-rte-install-maintenance]
          note: "Unknown archive content does not obscure the inspected archive storage substrate."
        - scope: "Browser-local editor fallback and remote claude.ai copies"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-registry-write, runtime.md#rt-rte-browser-sync]
          note: "localStorage persistence and remote upload are established, but records do not resolve their implementation to a controlled substrate. Browser storage is not classified as files or kv by assumption; remote provider storage is uninspected."
      records: [memory.md#mem-obj-skill, memory.md#mem-obj-skill-version, memory.md#mem-obj-watcher-state, runtime.md#rt-rte-registry-write, runtime.md#rt-rte-browser-sync]
      note: "Database and filesystem witnesses coexist with browser/provider storage uncertainty. A Git origin does not make the accumulated registry a repo substrate."
    representational_form:
      assessment: partial
      units:
        - scope: "Descriptions, instruction bodies, titles, release notes, comment text, task summaries and stored evaluation prose on inspected text paths"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-skill, memory.md#mem-obj-content-version, memory.md#mem-obj-skill-version, memory.md#mem-obj-comment, memory.md#mem-obj-usage-event, memory.md#mem-rte-trace-reporting, runtime.md#rt-bap-host-instructions]
              note: "Humans/models interpret the text in rows and delivered copies; SQL text storage does not make its meaning symbolic."
          records: [memory.md#mem-obj-skill, memory.md#mem-obj-content-version, memory.md#mem-obj-skill-version, memory.md#mem-obj-comment, memory.md#mem-obj-usage-event, memory.md#mem-rte-trace-reporting]
          note: "Covers the text part only, not opaque archive members or arbitrary metadata."
        - scope: "IDs, collections, version/status/hash/pointer fields, manifests, watcher offsets, ratings and numeric usage/confidence fields"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-skill, memory.md#mem-obj-content-version, memory.md#mem-obj-skill-version, memory.md#mem-obj-comment, memory.md#mem-obj-usage-event, memory.md#mem-obj-watcher-state, memory.md#mem-rte-install-maintenance, epistemic.md#epi-rte-rating-admission]
              note: "Localized fields have fixed lookup, comparison, arithmetic or branch consumers; a scalar confidence is not parametric memory."
          records: [memory.md#mem-obj-skill, memory.md#mem-obj-content-version, memory.md#mem-obj-skill-version, memory.md#mem-obj-comment, memory.md#mem-obj-usage-event, memory.md#mem-obj-watcher-state, memory.md#mem-rte-install-maintenance, epistemic.md#epi-rte-rating-admission]
          note: "Form is resolved for the named fixed-rule parts, not arbitrary values carried alongside them."
        - scope: "Arbitrary archive payloads, extra_frontmatter and usage metadata"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-skill-version, memory.md#mem-obj-skill, memory.md#mem-obj-usage-event]
          note: "Payload contents and downstream interpretation are unresolved. A displayed Markdown body or archive checksum cannot classify these parts."
      records: [memory.md#mem-obj-skill, memory.md#mem-obj-skill-version, memory.md#mem-obj-usage-event, memory.md#mem-obj-watcher-state]
      note: "Natural-language and symbolic parts are independently supported; opaque parts prevent complete coverage. External host weights are outside this memory scope."
    lineage:
      assessment: partial
      units:
        - scope: "Explicit editor/approved authoring path and selected upstream or remote admission paths"
          assessment: known
          findings:
            - value: authored
              basis: afforded
              records: [runtime.md#rt-rte-registry-write]
              note: "The editor and approval-following draft path afford authored procedures; no actual corpus authorship is observed."
            - value: imported
              basis: wired
              records: [runtime.md#rt-rte-source-import, memory.md#mem-rte-inbound-resolution]
              note: "Git import and remote-body adoption bring external procedures into current rows or staged snapshots."
          records: [runtime.md#rt-rte-registry-write, runtime.md#rt-rte-source-import, memory.md#mem-rte-inbound-resolution]
          note: "These are known derivation alternatives, not a uniform lineage assigned to every skill."
        - scope: "Save snapshots, reconstructed installed copies, generated current-content archives and watcher-derived events/cursors"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-content-version, runtime.md#rt-rte-project-sync, runtime.md#rt-rte-bundle-install]
              note: "Software copies current fields into snapshots and packages/substitutes content for later reads; no trace input is required by these transformations."
            - value: trace-extracted
              basis: wired
              records: [memory.md#mem-rte-trace-reporting, memory.md#mem-obj-watcher-state]
              note: "Read-tool activity yields retained call events and scan/dedup state. This lineage does not imply trace learning."
          records: [memory.md#mem-obj-content-version, runtime.md#rt-rte-project-sync, runtime.md#rt-rte-bundle-install, memory.md#mem-rte-trace-reporting, memory.md#mem-obj-watcher-state]
          note: "Known subsequent derivations do not resolve initialization provenance."
        - scope: "Initial caller content, independent published payloads, feedback prose/evaluations and arbitrary metadata"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-skill, memory.md#mem-obj-skill-version, memory.md#mem-obj-comment, memory.md#mem-obj-usage-event, memory.md#mem-rte-trace-reporting]
          note: "Caller authorship/control and production of reports/evaluations are not established uniformly. Archive origin is independent of the current Markdown row."
      records: [runtime.md#rt-rte-registry-write, runtime.md#rt-rte-source-import, memory.md#mem-rte-inbound-resolution, memory.md#mem-obj-content-version, memory.md#mem-rte-trace-reporting, memory.md#mem-obj-skill-version]
      note: "Retains authored/imported paths and software/trace derivations without upgrading unknown initial content provenance."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Retained procedural body at the external task-performing agent"
          assessment: known
          findings:
            - value: instruction
              basis: afforded
              records: [runtime.md#rt-bap-host-instructions, runtime.md#rt-rte-mcp-delivery, runtime.md#rt-rte-project-sync]
              note: "Installed bodies and MCP results supply reusable directions under the host hierarchy; delivery is wired, but application is external and unobserved."
          records: [runtime.md#rt-bap-host-instructions, runtime.md#rt-rte-mcp-delivery, runtime.md#rt-rte-project-sync]
          note: "The consumer force is instruction, not SkillNote enforcement of task actions."
        - scope: "Retained comments and reports at reporting readers and the documented bundle consumer"
          assessment: known
          findings:
            - value: knowledge
              basis: afforded
              records: [memory.md#mem-obj-comment, memory.md#mem-rte-feedback-catalog, epistemic.md#epi-rte-rating-admission]
              note: "Comments/outcomes supply attributed reference or advice. Bundle consumers receive the latest comment prefix, not full criticism history or task summaries."
          records: [memory.md#mem-obj-comment, memory.md#mem-rte-feedback-catalog, epistemic.md#epi-rte-rating-admission]
          note: "Information availability does not verify reported outcomes or establish a deployed resolver."
        - scope: "Usage IDs/count inputs and comment ratings at bundle ordering; skill descriptions at foreground selection"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [memory.md#mem-rte-feedback-catalog, epistemic.md#epi-rte-bundle-selection]
              note: "Retained feedback determines relative candidate priority before response truncation. The algorithm itself need not be learned."
            - value: ranking
              basis: claimed
              records: [runtime.md#rt-rte-openclaw-use]
              note: "Foreground selection is instructed to compare retained descriptions with task language; this model judgment path is policy, not inspected model execution."
          records: [memory.md#mem-rte-feedback-catalog, epistemic.md#epi-rte-bundle-selection, runtime.md#rt-rte-openclaw-use]
          note: "Distinct code and host-policy consumers retain distinct evidence bases."
        - scope: "Collections, active-version/pointer/manifest fields and watcher cursor state at fixed-rule selectors"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [runtime.md#rt-rte-project-sync, runtime.md#rt-rte-mcp-delivery, memory.md#mem-rte-inbound-resolution, memory.md#mem-rte-install-maintenance, memory.md#mem-obj-watcher-state]
              note: "These fields select scope, version, adapter destination, staged body or next scan window."
            - value: enforcement
              basis: wired
              records: [runtime.md#rt-rte-bundle-install, memory.md#mem-obj-watcher-state]
              note: "Disabled release state vetoes download on covered branches; seen-slug state suppresses repeated event admission. Neither revokes cached instructions."
            - value: validation
              basis: wired
              records: [runtime.md#rt-rte-bundle-install, memory.md#mem-rte-install-maintenance, epistemic.md#epi-rte-comment-check]
              note: "Retained release checksums constrain admitted bytes, and retained linked-event skill IDs supply referential criteria for agent comments. Static schemas are not counted as accumulated memory."
          records: [runtime.md#rt-rte-project-sync, runtime.md#rt-rte-mcp-delivery, runtime.md#rt-rte-bundle-install, memory.md#mem-rte-inbound-resolution, memory.md#mem-rte-install-maintenance, memory.md#mem-obj-watcher-state, epistemic.md#epi-rte-comment-check]
          note: "Covers the named control consumers, not arbitrary frontmatter semantics or a universal access-control guarantee."
        - scope: "Opaque archive files, arbitrary frontmatter/metadata and incompletely traced analytics/evaluation consumers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-skill-version, memory.md#mem-obj-skill, memory.md#mem-obj-usage-event, memory.md#mem-rte-trace-reporting]
          note: "Missing payload/consumer facts prevent complete force classification, including a learning-authority conclusion for evaluations."
      records: [runtime.md#rt-bap-host-instructions, memory.md#mem-rte-feedback-catalog, runtime.md#rt-rte-bundle-install, memory.md#mem-obj-watcher-state, memory.md#mem-obj-skill-version, memory.md#mem-rte-trace-reporting]
      note: "Instruction, knowledge, ranking and symbolic control forces coexist. Feedback ranking alone does not establish a durable learning update."
    write_agency:
      assessment: partial
      units:
        - scope: "Human editor supply and approval-following skill-push publication"
          assessment: known
          findings:
            - value: manual
              basis: afforded
              records: [runtime.md#rt-rte-registry-write]
              note: "These alternatives explicitly allow human editing or final content approval, rather than merely starting a workflow."
          records: [runtime.md#rt-rte-registry-write]
          note: "This does not classify all POST/PATCH callers as human-controlled."
        - scope: "Snapshots, hook sync, code-governed imports/staging/adoption, adapter updates, installed-copy replacement and trace/feedback software admission"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-obj-content-version, runtime.md#rt-rte-project-sync, runtime.md#rt-rte-source-import, memory.md#mem-rte-inbound-resolution, runtime.md#rt-rte-adapter-update, memory.md#mem-rte-install-maintenance, memory.md#mem-rte-trace-reporting, epistemic.md#epi-rte-comment-retention, epistemic.md#epi-rte-rating-admission]
              note: "Software admits or replaces retained parts under structural/version/conflict rules without a required per-content human decision; launching update/import is not itself manual content approval."
          records: [memory.md#mem-obj-content-version, runtime.md#rt-rte-project-sync, runtime.md#rt-rte-source-import, memory.md#mem-rte-inbound-resolution, runtime.md#rt-rte-adapter-update, memory.md#mem-rte-install-maintenance, memory.md#mem-rte-trace-reporting, epistemic.md#epi-rte-comment-retention, epistemic.md#epi-rte-rating-admission]
          note: "Automatic admission is independent of who originally authored the body or report. Ask-policy resolution has a separate available human surface, not a universal requirement."
        - scope: "Generic initial direct writes, caller archive proposal and explicit conflict-resolution caller control"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-skill, runtime.md#rt-rte-bundle-install, memory.md#mem-rte-inbound-resolution]
          note: "Caller-supplied content or resolution choice alone does not establish a human decision. Human UI resolution is available, but no mandatory human decision is established for every such call."
      records: [runtime.md#rt-rte-registry-write, runtime.md#rt-rte-project-sync, memory.md#mem-rte-inbound-resolution, runtime.md#rt-rte-bundle-install, memory.md#mem-rte-trace-reporting]
      note: "Manual affordances and automatic admission coexist; generic caller control remains unresolved rather than silently assigned to either."
    curation_operations:
      assessment: partial
      units:
        - scope: "Current procedure edits, content restoration, inbound adoption and replacement of installed entries"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [runtime.md#rt-rte-registry-write, memory.md#mem-rte-inbound-resolution, memory.md#mem-rte-install-maintenance]
              note: "Existing retained entries are revised or replaced; update eligibility does not establish semantic improvement."
            - value: promote
              basis: wired
              records: [memory.md#mem-rte-inbound-resolution]
              note: "keep_claude_ai raises a staged, non-current body to current content for normal consumers."
          records: [runtime.md#rt-rte-registry-write, memory.md#mem-rte-inbound-resolution, memory.md#mem-rte-install-maintenance]
          note: "Transformations are classified by implemented state changes, not by the names of commands."
        - scope: "Published release disabling and age-limited influence of retained usage"
          assessment: known
          findings:
            - value: invalidate
              basis: wired
              records: [memory.md#mem-obj-skill-version, runtime.md#rt-rte-bundle-install]
              note: "Disabled release metadata withdraws reliance on download paths while retaining the release reference/history; it does not revoke current rows or caches."
            - value: decay
              basis: wired
              records: [memory.md#mem-rte-feedback-catalog, epistemic.md#epi-rte-bundle-metadata]
              note: "Usage older than 30 days ceases to contribute to candidate priority even though reports remain retained. Comment ratings have no analogous cutoff here."
          records: [memory.md#mem-obj-skill-version, runtime.md#rt-rte-bundle-install, memory.md#mem-rte-feedback-catalog, epistemic.md#epi-rte-bundle-metadata]
          note: "Withdrawal and decay are branch-specific, not global forgetting."
        - scope: "Repeated analytics rating reports with the same nonempty session/agent/slug"
          assessment: known
          findings:
            - value: dedup
              basis: wired
              records: [epistemic.md#epi-rte-rating-admission]
              note: "A matching report updates the existing assessment rather than retaining a second report; this is report deduplication, not merely a primary-key collision check."
            - value: evolve
              basis: wired
              records: [epistemic.md#epi-rte-rating-admission]
              note: "The existing report's rating, outcome, version and timestamp are revised."
          records: [epistemic.md#epi-rte-rating-admission]
          note: "This operation does not deduplicate procedures or merge the Comment and SkillRating stores."
        - scope: "Model-authored procedure generalization, opaque bundle transformations and evaluation-driven maintenance"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-registry-write, memory.md#mem-obj-skill-version, memory.md#mem-rte-trace-reporting]
          note: "No draft instance resolves compression versus a new claim; opaque archive contents and evaluation consumers prevent a complete transformation inventory. Packaging/indexing alone is not consolidation or synthesis."
      records: [runtime.md#rt-rte-registry-write, memory.md#mem-rte-inbound-resolution, memory.md#mem-obj-skill-version, memory.md#mem-rte-feedback-catalog, epistemic.md#epi-rte-rating-admission, memory.md#mem-rte-trace-reporting]
      note: "Positive maintenance operations are retained without inferring consolidation/synthesis from a route name or claiming a complete operation set."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Requested registry/history/editor reads, MCP skill calls, archive install/update, conflict resolution and context-bundle requests"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-registry-write, memory.md#mem-obj-content-version, runtime.md#rt-rte-mcp-delivery, runtime.md#rt-rte-bundle-install, memory.md#mem-rte-install-maintenance, memory.md#mem-rte-inbound-resolution, memory.md#mem-rte-feedback-catalog]
              note: "The caller requests retained content or an operation consuming it. Requested server selection and return are not additional unsolicited pushes."
          records: [runtime.md#rt-rte-registry-write, memory.md#mem-obj-content-version, runtime.md#rt-rte-mcp-delivery, runtime.md#rt-rte-bundle-install, memory.md#mem-rte-install-maintenance, memory.md#mem-rte-inbound-resolution, memory.md#mem-rte-feedback-catalog]
          note: "HTTP/code return routes are wired; downstream host use and deployed resolver wiring remain separate."
        - scope: "Hook-triggered project synchronization toward later host discovery"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-project-sync]
              note: "Startup/resume/configuration hooks automatically select configured collections and write retained instructions into discovery paths without a task consumer requesting those bodies."
          records: [runtime.md#rt-rte-project-sync]
          note: "The fetch inside this chain is requested, but the automatic selection/supply toward host discovery is push; it does not prove model-window injection."
        - scope: "Foreground OpenClaw body loading and symbolic scanner/maintenance state reads"
          assessment: known
          findings:
            - value: pull
              basis: claimed
              records: [runtime.md#rt-rte-openclaw-use]
              note: "The prompt asks the foreground agent to read selected retained bodies on demand."
            - value: pull
              basis: wired
              records: [memory.md#mem-obj-watcher-state, memory.md#mem-rte-install-maintenance]
              note: "Later scanner and maintenance invocations explicitly load retained cursor/manifest state."
          records: [runtime.md#rt-rte-openclaw-use, memory.md#mem-obj-watcher-state, memory.md#mem-rte-install-maintenance]
          note: "Request-driven state access is separated from any subsequent automatic distribution."
        - scope: "PostCompact reminder delivery, remote-host later consumption and untraced analytics readers"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-context-hooks, runtime.md#rt-rte-browser-sync, memory.md#mem-rte-trace-reporting]
          note: "Catalog fetch/output is inspected but model-visible PostCompact delivery is unresolved; remote discovery and full reporting consumers are uninspected. These alternatives prevent complete direction coverage."
      records: [runtime.md#rt-rte-project-sync, runtime.md#rt-rte-mcp-delivery, memory.md#mem-rte-feedback-catalog, runtime.md#rt-rte-context-hooks, runtime.md#rt-rte-browser-sync, memory.md#mem-rte-trace-reporting]
      note: "Pull and push are both supported on different operations, not by counting a requested response twice."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Automatic project-sync collection selection and unfiltered wildcard supply"
          assessment: known
          findings:
            - value: identifier
              basis: wired
              records: [runtime.md#rt-rte-project-sync]
              note: "Hook/configuration trigger uses configured collection identities to select matching current skill rows for installed delivery. This is actual membership filtering, not an ID merely printed in a catalog."
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-project-sync]
              note: "Wildcard selection supplies available skills without task-specific matching; empty/bodyless-response and cache guards are coarse availability controls, not semantic selectors."
          records: [runtime.md#rt-rte-project-sync]
          note: "Selection is toward host discovery; subsequent model choice is not established by the sync selector."
        - scope: "Requested MCP/archive/bundle retrieval and foreground body reads"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-mcp-delivery, runtime.md#rt-rte-bundle-install, memory.md#mem-rte-feedback-catalog, runtime.md#rt-rte-openclaw-use]
          note: "These are pull operations. Slug lookup, bundle ranking and task-description judgment here do not establish an additional push signal."
        - scope: "Unresolved reminder/remote/analytics delivery alternatives"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-context-hooks, runtime.md#rt-rte-browser-sync, memory.md#mem-rte-trace-reporting]
          note: "Missing downstream delivery/consumer facts prevent determining whether further push operations and signals exist."
      records: [runtime.md#rt-rte-project-sync, runtime.md#rt-rte-context-hooks, runtime.md#rt-rte-browser-sync, memory.md#mem-rte-trace-reporting, memory.md#mem-rte-feedback-catalog]
      note: "Known push selectors are retained; neither a known pull route nor the supplied foreground policy resolves other alternatives."
    trace_learning:
      assessment: not-determinable
      units:
        - scope: "Watcher/hook analytics, evaluation reports and caller usage/comment/rating chains"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-trace-reporting, memory.md#mem-rte-feedback-catalog, memory.md#mem-obj-usage-event, epistemic.md#epi-rte-comment-retention, epistemic.md#epi-rte-rating-admission]
          note: "Automatic trace extraction and retained reports are established. Watcher events serve analytics/recovery; bundle aggregates are recomputed rather than written as durable derived behavior-shaping artifacts. Evaluation production/consumers and broader reporting paths remain uninspected, so these records establish neither qualifying yes nor a bounded complete no."
        - scope: "Conversation-to-procedure authoring and opaque imported/published payload production"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-registry-write, memory.md#mem-obj-skill, memory.md#mem-obj-skill-version, runtime.md#rt-rte-source-import]
          note: "Repeated-convention authoring can involve session material but the supported human-approval path is not automatic trace learning. Generic callers and independent archive producers have unresolved derivation/control; no trace-fed automatic artifact update is established for them."
      records: [memory.md#mem-rte-trace-reporting, memory.md#mem-rte-feedback-catalog, runtime.md#rt-rte-registry-write, memory.md#mem-obj-skill-version, epistemic.md#epi-rte-rating-admission]
      note: "No accepted record establishes a qualifying automatic trace-fed durable artifact update with its later consumer. Uninspected alternatives and lack of bounded absence records prevent a system negative; learning benefit is independently unobserved."
    trace_source:
      assessment: not-determinable
      units:
        - scope: "Potential learning chains through watcher/evaluation and feedback reports"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-trace-reporting, memory.md#mem-rte-feedback-catalog, memory.md#mem-obj-usage-event]
          note: "Read-tool JSONL is an identified analytics input, but no qualifying learning write is established. Its trace origin cannot be promoted into a trace_source finding without that write; evaluation/report derivation also remains incomplete."
        - scope: "Potential conversation-derived or opaque payload learning chains"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-registry-write, memory.md#mem-obj-skill-version, runtime.md#rt-rte-source-import]
          note: "Conversation references and imported procedures alone do not identify the original input to an automatic learning write. Payload provenance/control remains unresolved."
      records: [memory.md#mem-rte-trace-reporting, memory.md#mem-rte-feedback-catalog, runtime.md#rt-rte-registry-write, memory.md#mem-obj-skill-version]
      note: "Not inapplicable: complete bounded absence of qualifying trace learning is not established. No session/tool/event/trajectory value is asserted solely from the presence of logs."
---

# SkillNote memory profile

## Comparison rationale

The comparison concerns accumulated procedures and their supporting state, not
all runtime storage. The database, independent release archives, installed copies
and staged snapshots have different consumers and rollback boundaries. In
particular, an archive can contain scripts and assets whose form and authority
cannot inherit the classification of displayed Markdown. See
[MEM-OBJ-skill](memory.md#mem-obj-skill),
[MEM-OBJ-content-version](memory.md#mem-obj-content-version) and
[MEM-OBJ-skill-version](memory.md#mem-obj-skill-version).

The reconciliation supersedes EPI-RTE-install-maintenance with
[MEM-RTE-install-maintenance](memory.md#mem-rte-install-maintenance). All profile
maintenance citations use that canonical record. This affects file replacement,
manifest routing, automatic admission, evolution and requested read-back; it
adds neither atomic rollback nor universal withdrawal. Other overlapping text,
feedback and endpoint records remain valid containers or functional parts, not
superseded identities.

Instruction delivery is implemented, while its force at the external model is
an afforded instruction path. The foreground OpenClaw comparison of descriptions
with a task is requested model judgment, not a wired semantic ranker. By contrast,
retained comment ratings and usage counts influence code-level relative priority
in the requested bundle. That is ranking authority, even though the response is
transient and the scoring policy is fixed. The comment prefix supplies reference
or advice to the documented consumer, not verified task truth. See
[RT-BAP-host-instructions](runtime.md#rt-bap-host-instructions),
[RT-RTE-openclaw-use](runtime.md#rt-rte-openclaw-use) and
[MEM-RTE-feedback-catalog](memory.md#mem-rte-feedback-catalog).

The automatic sync chain has both a requested registry fetch and automatic supply
toward later host discovery. Collection membership actually selects delivered
parts, supporting identifier-based push; wildcard availability is coarse.
Neither a requested MCP slug nor a task-conditioned foreground read is itself a
push signal. PostCompact output does not become confirmed model-visible delivery
merely because a catalog was fetched. See
[RT-RTE-project-sync](runtime.md#rt-rte-project-sync),
[RT-RTE-mcp-delivery](runtime.md#rt-rte-mcp-delivery) and
[RT-RTE-context-hooks](runtime.md#rt-rte-context-hooks).

Curation is local. A staged body promoted to current content gains a consumption
tier. Disabled archives retain history while losing covered download eligibility.
A 30-day usage window removes old reports' ranking influence, not their stored
rows. Deduplicating a repeated rating updates an assessment, not a procedure.
These mechanisms do not imply semantic improvement, global revocation or a
synthesized procedure. See
[MEM-RTE-inbound-resolution](memory.md#mem-rte-inbound-resolution),
[MEM-OBJ-skill-version](memory.md#mem-obj-skill-version),
[EPI-RTE-bundle-metadata](epistemic.md#epi-rte-bundle-metadata) and
[EPI-RTE-rating-admission](epistemic.md#epi-rte-rating-admission).

Trace extraction is not automatically trace learning. The watcher retains
analytics events and replay state, not revised guidance; its events are not the
usage store counted by the bundle. The latter recomputes a candidate payload
from retained reports without persisting a derived procedure or learned ranking
artifact. This supports trace-extracted lineage and feedback-dependent ranking,
not a qualifying positive learning finding. Uninspected evaluation consumers and
unknown caller/payload production also prevent a complete negative. Therefore
trace source remains unresolved rather than being inferred from the visible
JSONL input or declared inapplicable. See
[MEM-RTE-trace-reporting](memory.md#mem-rte-trace-reporting),
[MEM-RTE-feedback-catalog](memory.md#mem-rte-feedback-catalog) and
[MEM-OBJ-skill-version](memory.md#mem-obj-skill-version).

No frozen-source files were read for this profile. Classification uses only the
supplied accepted records and their annotations, with reconciliation resolving
identity. No operation or benefit is upgraded to observed or causally supported.
