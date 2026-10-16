---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: Spacebot memory comparison across claims, temporal and continuation summaries, procedures,
  wiki and retained control state at the frozen source boundary.
run-id: AAS-2026-10-14-spacebot-6a954b400f95-01
source-identity: https://github.com/spacedriveapp/spacebot
reviewed-boundary: 5c2ee47b397e09c956dc15000ea576ecd28e92bb
memory-comparison:
  version: 2
  scope: Use-accumulated or revised agent claims, human anchors, association/selectors and dense indexes;
    working events and temporal summaries; live/durable conversation and worker continuation records;
    chronicle checkpoints; mutable skills/support files and custom identity snapshots; wiki pages/versions;
    retained task/goal/project/wake state and attachment alternatives where inventoried. Includes known
    routes and locally unresolved initial contents, org refresh, attachment payloads and restored-worker/auxiliary-state
    paths. Excludes shipped static presets/prompts/built-in procedures as such, transient current-run
    accounting, debug captures without established later consumers, provider/model-weight internals, remote
    MCP and external OpenCode internal retention. Spacebot-owned OpenCode snapshots remain included.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Agent claim text, selectors and human-anchor mapping
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-memory
          - memory.md#mem-obj-memory-metadata
          - memory.md#mem-obj-human-anchor
          note: Per-agent memories and mappings persist in SQLite.
        records:
        - memory.md#mem-obj-memory
        - memory.md#mem-obj-memory-metadata
        - memory.md#mem-obj-human-anchor
        note: Text and selector parts have the same evidenced persistence substrate.
      - scope: Typed weighted memory associations
        assessment: known
        findings:
        - value: graph
          basis: wired
          records:
          - memory.md#mem-obj-memory-metadata
          note: Association rows implement traversable typed weighted edges.
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-memory-metadata
          note: The graph rows are persisted in SQLite.
        records:
        - memory.md#mem-obj-memory-metadata
        note: Graph organization and SQL persistence coexist.
      - scope: Working events, temporal narratives, durable conversation and chronicle checkpoints
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-working-events
          - memory.md#mem-obj-temporal-summaries
          - memory.md#mem-obj-conversation-log
          - memory.md#mem-obj-chronicle-checkpoint
          note: These retained objects have explicit per-agent SQLite stores.
        records:
        - memory.md#mem-obj-working-events
        - memory.md#mem-obj-temporal-summaries
        - memory.md#mem-obj-conversation-log
        - memory.md#mem-obj-chronicle-checkpoint
        note: Storage is known for these objects, not all runtime state.
      - scope: Wiki current pages and version history
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-wiki-page
          note: Instance-wide SQLite holds pages and versions.
        records:
        - memory.md#mem-obj-wiki-page
        note: Separate instance-level retained object.
      - scope: Memory and chronicle retrieval tables
        assessment: known
        findings:
        - value: vector
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-index
          note: LanceDB persists dense embedding retrieval representations.
        records:
        - memory.md#mem-obj-retrieval-index
        note: Underlying Lance implementation and startup repair coverage are not independently audited;
          vector storage is explicit.
      - scope: Mutable skill procedures, support files and custom identity bodies
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-obj-skill-set
          - runtime.md#rt-rte-skill-change
          - memory.md#mem-obj-identity
          note: Procedures and identity text persist as filesystem files.
        records:
        - runtime.md#rt-obj-skill-set
        - runtime.md#rt-rte-skill-change
        - memory.md#mem-obj-identity
        note: Embedded static seeds are not use-derived memory.
      - scope: Live history summaries, loaded skill/identity snapshots and participant cache
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - runtime.md#rt-obj-channel-history
          - runtime.md#rt-obj-skill-set
          - memory.md#mem-obj-identity
          - memory.md#mem-obj-human-anchor
          note: These retained copies can affect later invocations in the same process.
        records:
        - runtime.md#rt-obj-channel-history
        - runtime.md#rt-obj-skill-set
        - memory.md#mem-obj-identity
        - memory.md#mem-obj-human-anchor
        note: Does not assert that rolling summaries survive restart.
      - scope: Worker/OpenCode retained snapshots, full task/goal/project/wake stores and attachment payloads
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-memory-recall
        - runtime.md#rt-rte-autonomy-epoch
        - runtime.md#rt-rte-opencode-work
        - memory.md#mem-obj-human-anchor
        note: Records establish retention or included routes, but do not classify every operative payload/store.
          Exact substrate inventory remains unresolved. External OpenCode internals are excluded.
      records:
      - memory.md#mem-obj-memory
      - memory.md#mem-obj-memory-metadata
      - memory.md#mem-obj-human-anchor
      - memory.md#mem-obj-working-events
      - memory.md#mem-obj-temporal-summaries
      - memory.md#mem-obj-conversation-log
      - memory.md#mem-obj-chronicle-checkpoint
      - memory.md#mem-obj-wiki-page
      - memory.md#mem-obj-retrieval-index
      - runtime.md#rt-obj-skill-set
      - runtime.md#rt-rte-skill-change
      - memory.md#mem-obj-identity
      - runtime.md#rt-obj-channel-history
      - memory.md#mem-rte-memory-recall
      - runtime.md#rt-rte-autonomy-epoch
      - runtime.md#rt-rte-opencode-work
      note: Known SQL, graph, vector, file and live-memory objects coexist. Attachment payloads and full
        auxiliary-state stores prevent a complete substrate inventory.
    representational_form:
      assessment: partial
      units:
      - scope: Claims, human descriptions, event/temporal text, conversation/checkpoint text and wiki
          content at model readers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-memory
          - memory.md#mem-obj-memory-metadata
          - memory.md#mem-obj-human-anchor
          - memory.md#mem-obj-working-events
          - memory.md#mem-obj-temporal-summaries
          - memory.md#mem-obj-conversation-log
          - memory.md#mem-obj-chronicle-checkpoint
          - memory.md#mem-obj-wiki-page
          - memory.md#mem-bap-memory-context
          note: Readers interpret text as claims, narratives or contextual evidence.
        records:
        - memory.md#mem-obj-memory
        - memory.md#mem-obj-memory-metadata
        - memory.md#mem-obj-human-anchor
        - memory.md#mem-obj-working-events
        - memory.md#mem-obj-temporal-summaries
        - memory.md#mem-obj-conversation-log
        - memory.md#mem-obj-chronicle-checkpoint
        - memory.md#mem-obj-wiki-page
        - memory.md#mem-bap-memory-context
        note: Readable content is classified separately from selector fields and numerical retrieval state.
      - scope: Skill procedures and custom identity at later model consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - runtime.md#rt-obj-skill-set
          - runtime.md#rt-rte-skill-change
          - memory.md#mem-obj-identity
          - runtime.md#rt-bap-skill-instruction
          note: Procedure and identity bodies supply model-interpreted directions.
        records:
        - runtime.md#rt-obj-skill-set
        - runtime.md#rt-rte-skill-change
        - memory.md#mem-obj-identity
        - runtime.md#rt-bap-skill-instruction
        note: Does not infer compliance from delivery.
      - scope: Memory associations/selectors, event ranges, checkpoint coverage, wiki versions and skill
          admission metadata
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-memory-metadata
          - memory.md#mem-obj-working-events
          - memory.md#mem-obj-chronicle-checkpoint
          - memory.md#mem-obj-wiki-page
          - runtime.md#rt-obj-skill-set
          note: Localized fields receive fixed query, navigation and admission treatment.
        records:
        - memory.md#mem-obj-memory-metadata
        - memory.md#mem-obj-working-events
        - memory.md#mem-obj-chronicle-checkpoint
        - memory.md#mem-obj-wiki-page
        - runtime.md#rt-obj-skill-set
        note: Text parts are not classified symbolic merely because serialized.
      - scope: Retained dense memory/checkpoint embeddings
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-index
          - memory.md#mem-cmp-embedding-model
          note: Dense retrieval representations are distributed-parametric, unlike symbolic IDs and text.
        records:
        - memory.md#mem-obj-retrieval-index
        - memory.md#mem-cmp-embedding-model
        note: Encoder weights themselves are initialization infrastructure; no parameter-learning route
          is inferred.
      - scope: Worker transcripts and lifecycle/task control at inspected consumers
        assessment: partial
        findings:
        - value: natural-language
          basis: wired
          records:
          - runtime.md#rt-rte-delegated-work
          - workflow.md#wf-rte-completion-admission
          note: Terminal result text and transcript text can reach later models.
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-rte-autonomy-epoch
          - workflow.md#wf-rte-completion-admission
          note: Task/wake and terminal version/kind/owner fields receive code interpretation.
        records:
        - runtime.md#rt-rte-delegated-work
        - runtime.md#rt-rte-autonomy-epoch
        - workflow.md#wf-rte-completion-admission
        note: The result body and lifecycle metadata are distinct consumption parts; full restored and
          attachment forms are unresolved.
      - scope: Attachment/binary recall payloads
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-memory-recall
        note: Text history cannot establish the form of uninspected saved attachments.
      records:
      - memory.md#mem-obj-memory
      - memory.md#mem-obj-memory-metadata
      - memory.md#mem-obj-human-anchor
      - memory.md#mem-obj-working-events
      - memory.md#mem-obj-temporal-summaries
      - memory.md#mem-obj-conversation-log
      - memory.md#mem-obj-chronicle-checkpoint
      - memory.md#mem-obj-wiki-page
      - memory.md#mem-bap-memory-context
      - runtime.md#rt-obj-skill-set
      - runtime.md#rt-rte-skill-change
      - memory.md#mem-obj-identity
      - runtime.md#rt-bap-skill-instruction
      - memory.md#mem-obj-retrieval-index
      - memory.md#mem-cmp-embedding-model
      - runtime.md#rt-rte-delegated-work
      - runtime.md#rt-rte-autonomy-epoch
      - workflow.md#wf-rte-completion-admission
      - memory.md#mem-rte-memory-recall
      note: Text, symbolic fields and dense representations are separately supported; display text does
        not resolve uninspected payloads.
    lineage:
      assessment: partial
      units:
      - scope: Conversation-derived memories, working narratives, chronicle summaries and reflected procedures
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-rte-memory-admission
          - memory.md#mem-rte-temporal-synthesis
          - memory.md#mem-rte-chronicle-retention
          - runtime.md#rt-rte-skill-change
          note: Automatic writers derive retained content from conversation, operational events or worker
            experience.
        records:
        - memory.md#mem-rte-memory-admission
        - memory.md#mem-rte-temporal-synthesis
        - memory.md#mem-rte-chronicle-retention
        - runtime.md#rt-rte-skill-change
        note: This classifies derivation paths, not initial deployed content or output truth.
      - scope: File-derived claims and externally installed skill content
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-rte-file-ingestion
          - runtime.md#rt-rte-capability-admission
          note: External files and downloaded procedures enter retained memory.
        records:
        - memory.md#mem-rte-file-ingestion
        - runtime.md#rt-rte-capability-admission
        note: Source authorship and semantic trust remain unknown; import itself is wired.
      - scope: Direct model-authored claims, wiki edits and procedure bodies
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-rte-memory-admission
          - memory.md#mem-rte-wiki-editing
          - runtime.md#rt-rte-skill-change
          note: Granted writers supply claim, page and procedure text.
        records:
        - memory.md#mem-rte-memory-admission
        - memory.md#mem-rte-wiki-editing
        - runtime.md#rt-rte-skill-change
        note: Authorship does not imply manual admission or novel claims.
      - scope: Recorded raw events/messages, generated selectors, embeddings and deterministic memory
          merges
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-working-events
          - memory.md#mem-obj-conversation-log
          - memory.md#mem-obj-retrieval-index
          - memory.md#mem-rte-memory-curation
          note: Runtime records, encoder outputs and fixed-rule metadata/merges are computational products
            rather than imported standing procedures.
        records:
        - memory.md#mem-obj-working-events
        - memory.md#mem-obj-conversation-log
        - memory.md#mem-obj-retrieval-index
        - memory.md#mem-rte-memory-curation
        note: Derived indexing is known; downloaded encoder provenance is not resolved.
      - scope: Initial content, human-org seed authorship/propagation, custom identity and encoder provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory
        - memory.md#mem-obj-human-anchor
        - memory.md#mem-obj-identity
        - memory.md#mem-cmp-embedding-model
        note: Known subsequent writers do not establish these initial or dependency-mediated derivation
          paths.
      - scope: Full attachment and auxiliary task/wake provenance
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-memory-recall
        - runtime.md#rt-rte-autonomy-epoch
        - runtime.md#rt-rte-opencode-work
        - memory.md#mem-obj-human-anchor
        note: Included paths are not completely traced; no complete lineage union follows.
      records:
      - memory.md#mem-rte-memory-admission
      - memory.md#mem-rte-temporal-synthesis
      - memory.md#mem-rte-chronicle-retention
      - runtime.md#rt-rte-skill-change
      - memory.md#mem-rte-file-ingestion
      - runtime.md#rt-rte-capability-admission
      - memory.md#mem-rte-wiki-editing
      - memory.md#mem-obj-working-events
      - memory.md#mem-obj-conversation-log
      - memory.md#mem-obj-retrieval-index
      - memory.md#mem-rte-memory-curation
      - memory.md#mem-obj-memory
      - memory.md#mem-obj-human-anchor
      - memory.md#mem-obj-identity
      - memory.md#mem-cmp-embedding-model
      - memory.md#mem-rte-memory-recall
      - runtime.md#rt-rte-autonomy-epoch
      - runtime.md#rt-rte-opencode-work
      note: Known authored, imported, trace-extracted and compiled paths remain positive; initial contents
        and opaque alternatives prevent complete lineage coverage.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Claims, temporal narratives, checkpoints, wiki and restored result text at later work models
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-bap-memory-context
          - memory.md#mem-rte-chronicle-retention
          - runtime.md#rt-rte-delegated-work
          note: Delivered content supplies evidence and context, not enforced truth.
        records:
        - memory.md#mem-bap-memory-context
        - memory.md#mem-rte-chronicle-retention
        - runtime.md#rt-rte-delegated-work
        note: A system-prompt channel does not by itself turn claim text into standing instruction.
      - scope: Retained procedures and custom identity at later model consumers
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - runtime.md#rt-bap-skill-instruction
          - memory.md#mem-obj-identity
          note: Bodies supply standing directions to later processes.
        records:
        - runtime.md#rt-bap-skill-instruction
        - memory.md#mem-obj-identity
        note: Required delivery is distinct from compliance.
      - scope: Retained session/worker/event inputs at extraction, summarization and reflection writers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-rte-memory-admission
          - memory.md#mem-rte-temporal-synthesis
          - memory.md#mem-rte-chronicle-retention
          - runtime.md#rt-rte-skill-change
          note: Retained experience feeds durable claims, narratives, checkpoints or instruction updates
            for later consumers.
        records:
        - memory.md#mem-rte-memory-admission
        - memory.md#mem-rte-temporal-synthesis
        - memory.md#mem-rte-chronicle-retention
        - runtime.md#rt-rte-skill-change
        note: Update-consumer authority is separate from downstream knowledge/instruction; no improved
          capacity is asserted.
      - scope: Claim text, embeddings, associations and importance at retrieval/render rankers
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-rte-memory-recall
          - memory.md#mem-bap-memory-selectors
          - memory.md#mem-obj-retrieval-index
          note: Retained text/features/scores affect relative candidate order under fixed algorithms.
        records:
        - memory.md#mem-rte-memory-recall
        - memory.md#mem-bap-memory-selectors
        - memory.md#mem-obj-retrieval-index
        note: Ranking inputs need not be a learned ranking policy.
      - scope: Forgotten flags and archive metadata at ordinary discovery
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-rte-memory-curation
          - memory.md#mem-rte-wiki-editing
          - runtime.md#rt-rte-skill-change
          note: Retained withdrawal state excludes ordinary recalled/discoverable content.
        records:
        - memory.md#mem-rte-memory-curation
        - memory.md#mem-rte-wiki-editing
        - runtime.md#rt-rte-skill-change
        note: Wiki explicit slug reads and previously delivered copies remain outside that exclusion.
      - scope: Skill pin/origin/read state and durable worker/task metadata at admission checks
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - runtime.md#rt-rte-skill-change
          - runtime.md#rt-rte-delegated-work
          - workflow.md#wf-rte-completion-admission
          note: Stored pin/task/terminal criteria determine admissibility of edits, execution or completion.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-rte-skill-change
          - runtime.md#rt-rte-delegated-work
          - workflow.md#wf-rte-completion-admission
          note: The corresponding handlers refuse disallowed edits/spawns or mismatching completion events.
        records:
        - runtime.md#rt-rte-skill-change
        - runtime.md#rt-rte-delegated-work
        - workflow.md#wf-rte-completion-admission
        note: These local vetoes do not establish global filesystem protection or work-product correctness.
      - scope: Chronicle boundaries, task plans and durable wake/run state at continuation/control consumers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-rte-chronicle-retention
          - runtime.md#rt-rte-delegated-work
          - runtime.md#rt-rte-autonomy-epoch
          note: Retained boundaries select hydration windows; task plans and wake/run state select execution
            inputs and continuation.
        records:
        - memory.md#mem-rte-chronicle-retention
        - runtime.md#rt-rte-delegated-work
        - runtime.md#rt-rte-autonomy-epoch
        note: Routing is supported at these consumers without resolving every auxiliary state machine.
      - scope: Uninspected attachment, profile-card and auxiliary-state consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-identity
        - memory.md#mem-rte-memory-recall
        - runtime.md#rt-rte-autonomy-epoch
        - runtime.md#rt-rte-opencode-work
        - memory.md#mem-obj-human-anchor
        note: Generated profile-card production has no established behavioral consumer; full attachment
          and auxiliary paths cannot be assigned authority from display summaries.
      records:
      - memory.md#mem-bap-memory-context
      - memory.md#mem-rte-chronicle-retention
      - runtime.md#rt-rte-delegated-work
      - runtime.md#rt-bap-skill-instruction
      - memory.md#mem-obj-identity
      - memory.md#mem-rte-memory-admission
      - memory.md#mem-rte-temporal-synthesis
      - runtime.md#rt-rte-skill-change
      - memory.md#mem-rte-memory-recall
      - memory.md#mem-bap-memory-selectors
      - memory.md#mem-obj-retrieval-index
      - memory.md#mem-rte-memory-curation
      - memory.md#mem-rte-wiki-editing
      - workflow.md#wf-rte-completion-admission
      - runtime.md#rt-rte-autonomy-epoch
      - runtime.md#rt-rte-opencode-work
      - memory.md#mem-obj-human-anchor
      note: All seven forces have local wired witnesses; remaining consumers prevent a complete authority
        assessment. Shipped static criteria and transient completion bookkeeping are not counted as accumulated
        memory.
    write_agency:
      assessment: partial
      units:
      - scope: Model memory saves/import extraction, merges, wiki edits and reflected skill mutations
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-memory-admission
          - memory.md#mem-rte-file-ingestion
          - memory.md#mem-rte-memory-curation
          - memory.md#mem-rte-wiki-editing
          - runtime.md#rt-rte-skill-change
          note: Model/software admission does not require a human decision approving the exact retained
            content.
        records:
        - memory.md#mem-rte-memory-admission
        - memory.md#mem-rte-file-ingestion
        - memory.md#mem-rte-memory-curation
        - memory.md#mem-rte-wiki-editing
        - runtime.md#rt-rte-skill-change
        note: Conversation initiation, file upload and User origin do not convert subsequent model-selected
          admission to manual.
      - scope: Runtime log/event/selector/index writes, temporal/chronicle production and periodic maintenance
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-working-events
          - memory.md#mem-obj-conversation-log
          - memory.md#mem-obj-retrieval-index
          - memory.md#mem-rte-temporal-synthesis
          - memory.md#mem-rte-chronicle-retention
          - memory.md#mem-rte-memory-curation
          note: Code or summarizer admits retained changes without per-content operator approval.
        records:
        - memory.md#mem-obj-working-events
        - memory.md#mem-obj-conversation-log
        - memory.md#mem-obj-retrieval-index
        - memory.md#mem-rte-temporal-synthesis
        - memory.md#mem-rte-chronicle-retention
        - memory.md#mem-rte-memory-curation
        note: Physical I/O is not the warrant; the decision mechanism is software/model control.
      - scope: Administrative/API/CLI edits, external skill installation requests and generic file/shell
          changes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-wiki-editing
        - runtime.md#rt-rte-capability-admission
        - runtime.md#rt-rte-skill-change
        note: Generic caller identity and available operator surfaces do not establish a human exact-content
          decision for each mechanism. Automatic reflection remains separately known.
      - scope: Initial custom contents, org seed replacement and untraced attachment/auxiliary admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory
        - memory.md#mem-obj-human-anchor
        - memory.md#mem-obj-identity
        - memory.md#mem-rte-memory-recall
        - runtime.md#rt-rte-autonomy-epoch
        - runtime.md#rt-rte-opencode-work
        note: Initial control and complete alternative write paths are unresolved; no manual classification
          or bounded automatic-only claim is licensed.
      records:
      - memory.md#mem-rte-memory-admission
      - memory.md#mem-rte-file-ingestion
      - memory.md#mem-rte-memory-curation
      - memory.md#mem-rte-wiki-editing
      - runtime.md#rt-rte-skill-change
      - memory.md#mem-obj-working-events
      - memory.md#mem-obj-conversation-log
      - memory.md#mem-obj-retrieval-index
      - memory.md#mem-rte-temporal-synthesis
      - memory.md#mem-rte-chronicle-retention
      - runtime.md#rt-rte-capability-admission
      - memory.md#mem-obj-memory
      - memory.md#mem-obj-human-anchor
      - memory.md#mem-obj-identity
      - memory.md#mem-rte-memory-recall
      - runtime.md#rt-rte-autonomy-epoch
      - runtime.md#rt-rte-opencode-work
      note: Automatic admission is wired on named routes. No manual value is inferred from administrative
        naming; unresolved initial and caller control prevents a complete agency inventory.
    curation_operations:
      assessment: partial
      units:
      - scope: Conversation-to-standing-memory extraction
        assessment: partial
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-memory-admission
          - epistemic.md#epi-rte-memory-extraction
          note: Selected conversational information is distilled into reduced standing claims.
        records:
        - memory.md#mem-rte-memory-admission
        - epistemic.md#epi-rte-memory-extraction
        note: Consolidation names the implemented selection/distillation route, not proof of faithful
          output; actual semantic novelty remains unresolved.
      - scope: Temporal narratives, chronicle summaries/rollups and live rolling summaries
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-temporal-synthesis
          - memory.md#mem-rte-chronicle-retention
          - runtime.md#rt-rte-context-control
          note: Summarization combines/compresses retained events, spans or prior summaries.
        records:
        - memory.md#mem-rte-temporal-synthesis
        - memory.md#mem-rte-chronicle-retention
        - runtime.md#rt-rte-context-control
        note: Fallback notices and emergency drops do not acquire semantic summary content from this positive
          route.
      - scope: Explicit batch and deterministic near-duplicate memory merges
        assessment: partial
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-memory-curation
          - epistemic.md#epi-rte-batch-consolidation
          note: Survivor combines retained memory inputs.
        - value: dedup
          basis: wired
          records:
          - memory.md#mem-rte-memory-curation
          - epistemic.md#epi-rte-memory-maintenance
          note: Near-duplicate candidates are merged and absorbed entries leave ordinary retrieval.
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-memory-curation
          - epistemic.md#epi-rte-batch-consolidation
          note: Survivor text is replaced.
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-rte-memory-curation
          note: Absorbed rows can remain as forgotten provenance targets.
        - value: promote
          basis: wired
          records:
          - epistemic.md#epi-rte-batch-consolidation
          note: Survivor importance becomes the maximum of the merged entries, allowing a salience increase.
        records:
        - memory.md#mem-rte-memory-curation
        - epistemic.md#epi-rte-batch-consolidation
        - epistemic.md#epi-rte-memory-maintenance
        note: Implemented transformations are known; semantic preservation, correction and model-generated
          novelty are unresolved, not synthesis findings.
      - scope: Age/access decay, pruning and explicit memory forgetting
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-memory-curation
          note: Age/access changes importance and pruning forgets low-importance old entries.
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-rte-memory-curation
          - epistemic.md#epi-rte-memory-withdrawal
          note: Soft forgetting withdraws ordinary reliance while retaining the row.
        records:
        - memory.md#mem-rte-memory-curation
        - epistemic.md#epi-rte-memory-withdrawal
        note: Hard pruning is not classified as history-preserving invalidation.
      - scope: Wiki edits/restores/archive and procedure patch/edit/archive
        assessment: partial
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-wiki-editing
          - runtime.md#rt-rte-skill-change
          note: Existing page/procedure content can be revised or replaced.
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-rte-wiki-editing
          - runtime.md#rt-rte-skill-change
          note: Archive changes discovery while history/archive content remains.
        records:
        - memory.md#mem-rte-wiki-editing
        - runtime.md#rt-rte-skill-change
        note: No particular novel claim or semantic deduplication in model-authored edits is established.
      - scope: Attachment, org refresh and full task/goal/project maintenance alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-memory-recall
        - runtime.md#rt-rte-autonomy-epoch
        - runtime.md#rt-rte-opencode-work
        - memory.md#mem-obj-human-anchor
        note: Uninspected transformations prevent an exhaustive operation inventory; index rebuild alone
          would establish none.
      records:
      - memory.md#mem-rte-memory-admission
      - epistemic.md#epi-rte-memory-extraction
      - memory.md#mem-rte-temporal-synthesis
      - memory.md#mem-rte-chronicle-retention
      - runtime.md#rt-rte-context-control
      - memory.md#mem-rte-memory-curation
      - epistemic.md#epi-rte-batch-consolidation
      - epistemic.md#epi-rte-memory-maintenance
      - epistemic.md#epi-rte-memory-withdrawal
      - memory.md#mem-rte-wiki-editing
      - runtime.md#rt-rte-skill-change
      - memory.md#mem-rte-memory-recall
      - runtime.md#rt-rte-autonomy-epoch
      - runtime.md#rt-rte-opencode-work
      - memory.md#mem-obj-human-anchor
      note: Consolidate, dedup, evolve, invalidate, decay and promote have bounded implemented witnesses.
        No record establishes a newly synthesized claim; opaque model output and uninspected alternatives
        remain unresolved rather than absent.
    read_back_direction:
      assessment: partial
      units:
      - scope: Explicit memory/channel/chronicle/wiki reads and optional skill body requests
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-memory-recall
          - memory.md#mem-rte-chronicle-retention
          - memory.md#mem-rte-wiki-editing
          - runtime.md#rt-bap-skill-instruction
          note: Consumers request retained content; fulfillment is pull even when code selects and formats
            the return.
        records:
        - memory.md#mem-rte-memory-recall
        - memory.md#mem-rte-chronicle-retention
        - memory.md#mem-rte-wiki-editing
        - runtime.md#rt-bap-skill-instruction
        note: Hybrid vector/lexical selection in requested recall is not a separate unsolicited push.
      - scope: Automatic store/temporal/participant context and chronicle view/hydration
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-context-supply
          - memory.md#mem-rte-chronicle-retention
          - runtime.md#rt-rte-channel-turn
          note: Prompt build or restart selects accumulated content without a foreground recall request.
        records:
        - memory.md#mem-rte-context-supply
        - memory.md#mem-rte-chronicle-retention
        - runtime.md#rt-rte-channel-turn
        note: Budgets may omit content or collapse it to a first line/title.
      - scope: Loaded skill index and task-required skill bodies
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-obj-skill-set
          - runtime.md#rt-clm-required-skills
          - runtime.md#rt-bap-skill-instruction
          note: Preamble construction supplies discoverable procedures or exact task-required bodies without
            a body-read request.
        records:
        - runtime.md#rt-obj-skill-set
        - runtime.md#rt-clm-required-skills
        - runtime.md#rt-bap-skill-instruction
        note: Required selection may originate in an upstream task decision; automatic body supply is
          distinct from optional pull.
      - scope: Live rolling summary and worker durable completion/resumption at later inference
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-context-control
          - runtime.md#rt-rte-delegated-work
          - workflow.md#wf-rte-completion-admission
          note: History construction or completion retrigger automatically supplies retained summary/result
            to later inference.
        records:
        - runtime.md#rt-rte-context-control
        - runtime.md#rt-rte-delegated-work
        - workflow.md#wf-rte-completion-admission
        note: Continuation context is memory across invocations without requiring cross-restart persistence.
      - scope: Mutable identity snapshots in later system prompts
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-identity
          note: Loaded custom instruction bodies are rendered into later prompts.
        records:
        - memory.md#mem-obj-identity
        note: Only custom/revised retained text is in memory scope; static preset loading alone is excluded.
      - scope: Attachment, auxiliary-state and all restored-worker alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-memory-recall
        - runtime.md#rt-rte-autonomy-epoch
        - runtime.md#rt-rte-opencode-work
        - memory.md#mem-obj-human-anchor
        note: Known push and pull routes cannot determine all included delivery alternatives.
      records:
      - memory.md#mem-rte-memory-recall
      - memory.md#mem-rte-chronicle-retention
      - memory.md#mem-rte-wiki-editing
      - runtime.md#rt-bap-skill-instruction
      - memory.md#mem-rte-context-supply
      - runtime.md#rt-rte-channel-turn
      - runtime.md#rt-obj-skill-set
      - runtime.md#rt-clm-required-skills
      - runtime.md#rt-rte-context-control
      - runtime.md#rt-rte-delegated-work
      - workflow.md#wf-rte-completion-admission
      - memory.md#mem-obj-identity
      - runtime.md#rt-rte-autonomy-epoch
      - runtime.md#rt-rte-opencode-work
      - memory.md#mem-obj-human-anchor
      note: Both directions are wired; missing alternative-route coverage prevents known rather than cancelling
        either positive.
    read_back_signal:
      assessment: partial
      units:
      - scope: Automatic global store and temporal/activity blocks
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-context-supply
          note: 'Trigger: prompt build. Fixed type sections, importance/time windows and budgets select
            claim first lines, event tails and narratives.'
        records:
        - memory.md#mem-rte-context-supply
        note: No query embedding or lexical relevance selector is established on this push branch.
      - scope: Participant-scoped anchor supply
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-obj-human-anchor
          - memory.md#mem-rte-context-supply
          note: 'Trigger: participant context build. Present platform-scoped human keys match anchor mappings
            and select delivered anchor first lines.'
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-context-supply
          note: The participant budget separately limits delivery after key-based selection.
        records:
        - memory.md#mem-obj-human-anchor
        - memory.md#mem-rte-context-supply
        note: Actual key matching, not the presence of an ID label, establishes targeted selection; cache
          refresh is unresolved.
      - scope: Chronicle view, durable channel hydration and rolling history continuation
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-chronicle-retention
          - runtime.md#rt-rte-context-control
          note: 'Trigger: later prompt/hydration. Latest boundaries, recent/older caps, sequence/time
            and budget choose summaries or message spans.'
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-rte-channel-turn
          - memory.md#mem-rte-chronicle-retention
          note: Conversation identity scopes the durable history/checkpoint rows selected for the continuing
            channel.
        records:
        - memory.md#mem-rte-chronicle-retention
        - runtime.md#rt-rte-context-control
        - runtime.md#rt-rte-channel-turn
        note: Requested sequence/cursor expansion is pull and does not supply an additional push signal.
      - scope: Skill index and required procedure body supply
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-obj-skill-set
          - runtime.md#rt-bap-skill-instruction
          note: 'Trigger: preamble build. Discoverable loaded skills supply an availability index.'
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-clm-required-skills
          - runtime.md#rt-bap-skill-instruction
          note: 'Trigger: task-worker preparation. Required skill names resolve matching loaded skills
            and select full bodies for injection.'
        records:
        - runtime.md#rt-obj-skill-set
        - runtime.md#rt-clm-required-skills
        - runtime.md#rt-bap-skill-instruction
        note: Suggested labels are not themselves full-body delivery; optional named reads remain pull.
      - scope: Worker completion/result retrigger
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - workflow.md#wf-rte-completion-admission
          note: 'Trigger: completion event. Worker identity and durable version/kind/owner agreement select
            the retained terminal result for queuing.'
        records:
        - workflow.md#wf-rte-completion-admission
        note: The consumer receives result text, not every private tool message.
      - scope: Custom identity prompt rendering
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-identity
          note: 'Trigger: prompt construction. Loaded nonblank identity/role/soul bodies render verbatim
            as standing context.'
        records:
        - memory.md#mem-obj-identity
        note: No relevance query is evidenced on this path.
      - scope: Uninspected attachment, auxiliary-state and restored-worker push alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-memory-recall
        - runtime.md#rt-rte-autonomy-epoch
        - runtime.md#rt-rte-opencode-work
        - memory.md#mem-obj-human-anchor
        note: Unresolved delivery directions also leave their push selector signals unresolved; pull witnesses
          cannot make this unit inapplicable.
      records:
      - memory.md#mem-rte-context-supply
      - memory.md#mem-obj-human-anchor
      - memory.md#mem-rte-chronicle-retention
      - runtime.md#rt-rte-context-control
      - runtime.md#rt-rte-channel-turn
      - runtime.md#rt-obj-skill-set
      - runtime.md#rt-clm-required-skills
      - runtime.md#rt-bap-skill-instruction
      - workflow.md#wf-rte-completion-admission
      - memory.md#mem-obj-identity
      - memory.md#mem-rte-memory-recall
      - runtime.md#rt-rte-autonomy-epoch
      - runtime.md#rt-rte-opencode-work
      note: Coarse and identifier push have local witnesses. Embedding/lexical selectors in requested
        recall are pull, not automatic push signals; unresolved alternatives prevent an exhaustive signal
        assessment.
    trace_learning:
      assessment: partial
      units:
      - scope: Conversation extraction to standing memories
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-memory-admission
          - memory.md#mem-bap-memory-context
          note: Automatic conversation-fed writes persist claims later supplied by recall/render.
        records:
        - memory.md#mem-rte-memory-admission
        - memory.md#mem-bap-memory-context
        note: No new claim, weight update or improved task performance is required for this route classification.
      - scope: Working-event intraday and daily summaries
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-temporal-synthesis
          note: Automatic event-fed narratives persist in SQLite and enter later channel context or daily
            synthesis.
        records:
        - memory.md#mem-rte-temporal-synthesis
        note: Raw event retention alone is not the qualifying write; the derived narratives and consumers
          are.
      - scope: Chronicle summaries/rollups and rolling continuation summaries
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-chronicle-retention
          - runtime.md#rt-rte-context-control
          note: Automatic trace-fed compression creates retained context for later model invocations.
        records:
        - memory.md#mem-rte-chronicle-retention
        - runtime.md#rt-rte-context-control
        note: Durable chronicles and session-live rolling summaries differ in persistence horizon; fallback
          notices do not demonstrate semantic summary production.
      - scope: Procedure reflection
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-skill-change
          - runtime.md#rt-bap-skill-instruction
          note: Conversation/worker experience feeds automatic retained procedure changes, with later
            instruction delivery wired.
        records:
        - runtime.md#rt-rte-skill-change
        - runtime.md#rt-bap-skill-instruction
        note: Prompted abstention and local structural rails are not an observed beneficial-learning result.
      - scope: Generic wiki/identity/API/file writes, attachment and auxiliary-state alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-wiki-editing
        - memory.md#mem-obj-identity
        - memory.md#mem-rte-memory-recall
        - runtime.md#rt-rte-autonomy-epoch
        - runtime.md#rt-rte-opencode-work
        - memory.md#mem-obj-human-anchor
        note: Inputs and admission are not completely traced. No bounded absence record supports a local
          no or a system-wide negative.
      records:
      - memory.md#mem-rte-memory-admission
      - memory.md#mem-bap-memory-context
      - memory.md#mem-rte-temporal-synthesis
      - memory.md#mem-rte-chronicle-retention
      - runtime.md#rt-rte-context-control
      - runtime.md#rt-rte-skill-change
      - runtime.md#rt-bap-skill-instruction
      - memory.md#mem-rte-wiki-editing
      - memory.md#mem-obj-identity
      - memory.md#mem-rte-memory-recall
      - runtime.md#rt-rte-autonomy-epoch
      - runtime.md#rt-rte-opencode-work
      - memory.md#mem-obj-human-anchor
      note: Several qualifying automatic trace-fed routes are wired. Unresolved writes remain included;
        this yes union is not an efficacy, exercised-learning or self-improvement finding.
    trace_source:
      assessment: partial
      units:
      - scope: Conversation-derived standing memories
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-rte-memory-admission
          - memory.md#mem-obj-conversation-log
          note: Recorded conversational turns, including user messages, feed extraction.
        records:
        - memory.md#mem-rte-memory-admission
        - memory.md#mem-obj-conversation-log
        note: The copied current history may also contain summaries/tool traffic; complete original provenance
          of every included turn is unresolved.
      - scope: Temporal narratives from working events
        assessment: partial
        findings:
        - value: event-streams
          basis: wired
          records:
          - memory.md#mem-obj-working-events
          - memory.md#mem-rte-temporal-synthesis
          note: Discrete runtime/model-selected activity records feed intraday and daily synthesis.
        records:
        - memory.md#mem-obj-working-events
        - memory.md#mem-rte-temporal-synthesis
        note: Event summaries are mixed-origin and not complete raw tool payloads; conversational information
          wrapped as events does not itself add event-stream origin. Original content of every model-selected
          event is unresolved.
      - scope: Chronicle/rolling continuation summaries
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-obj-chronicle-checkpoint
          - memory.md#mem-rte-chronicle-retention
          - runtime.md#rt-rte-context-control
          note: Selected recorded conversational spans feed summaries and rollups.
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-obj-chronicle-checkpoint
          - memory.md#mem-rte-chronicle-retention
          - runtime.md#rt-rte-context-control
          note: Available live tool traffic can enter summarization before trimming; conversation-log
            expansion alone does not recover it.
        records:
        - memory.md#mem-obj-chronicle-checkpoint
        - memory.md#mem-rte-chronicle-retention
        - runtime.md#rt-rte-context-control
        note: Known inputs support both sources; fallback markers are a separate non-summary result and
          older summary ancestry can be lossy.
      - scope: Procedure reflection from channel and worker records
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records:
          - runtime.md#rt-rte-skill-change
          note: Conversation and user procedural corrections feed the reflection writer.
        - value: tool-traces
          basis: wired
          records:
          - runtime.md#rt-rte-skill-change
          - runtime.md#rt-rte-delegated-work
          note: Worker transcript/action/outcome inspection provides execution feedback to procedure updates.
        records:
        - runtime.md#rt-rte-skill-change
        - runtime.md#rt-rte-delegated-work
        note: Mixed worker transcript completeness and full restored variants remain unresolved; a multi-step
          worker task alone does not establish trajectory-based experience encoding.
      - scope: Unresolved generic/import/attachment/auxiliary trace-fed writes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-file-ingestion
        - memory.md#mem-rte-wiki-editing
        - memory.md#mem-rte-memory-recall
        - runtime.md#rt-rte-autonomy-epoch
        - runtime.md#rt-rte-opencode-work
        - memory.md#mem-obj-human-anchor
        note: Unknown file contents cannot be assumed to be traces; unresolved qualifying writes cannot
          be made source-inapplicable from known routes.
      records:
      - memory.md#mem-rte-memory-admission
      - memory.md#mem-obj-conversation-log
      - memory.md#mem-obj-working-events
      - memory.md#mem-rte-temporal-synthesis
      - memory.md#mem-obj-chronicle-checkpoint
      - memory.md#mem-rte-chronicle-retention
      - runtime.md#rt-rte-context-control
      - runtime.md#rt-rte-skill-change
      - runtime.md#rt-rte-delegated-work
      - memory.md#mem-rte-file-ingestion
      - memory.md#mem-rte-wiki-editing
      - memory.md#mem-rte-memory-recall
      - runtime.md#rt-rte-autonomy-epoch
      - runtime.md#rt-rte-opencode-work
      - memory.md#mem-obj-human-anchor
      note: Session logs, tool traces and runtime event streams have local wired witnesses. Mixed inputs
        and unresolved qualifying writes prevent a complete source inventory; trajectories are not inferred
        from multi-step execution.
---

# Spacebot memory profile

## Comparison rationale

This is a classification of accepted records, not a new source inspection. All positive findings above are wired capacities. No supplied record establishes observed operation or causal benefit. A partial axis preserves those capacities while keeping unresolved included parts visible. Whole-system functional scope does not turn selected source inspection into complete memory coverage.

Canonical references follow reconciliation: the memory-declared encoder, claim content, selectors and wiki page replace the duplicate epistemic component/object declarations. Their paths are [MEM-CMP-embedding-model](memory.md#mem-cmp-embedding-model), [MEM-OBJ-memory](memory.md#mem-obj-memory), [MEM-OBJ-memory-metadata](memory.md#mem-obj-memory-metadata) and [MEM-OBJ-wiki-page](memory.md#mem-obj-wiki-page). No supersession changes a value or upgrades a basis. Chronicle retention remains a part of context control, and completion admission remains a part of delegated work; neither container is discarded.

Dense embeddings have parametric form and vector substrate. SQL association rows have symbolic form, graph organization and SQLite persistence. Neither new vectors nor changed claim text establish model-parameter training. Exact encoder provenance remains unresolved in [MEM-CMP-embedding-model](memory.md#mem-cmp-embedding-model). External provider internals are outside this profile, not classified as absent memory.

Trace-fed summaries qualify even when they compress existing claims rather than add knowledge. The operative chain is retained experience, automatic derived write, then a later consumer. This holds for conversation extraction, temporal narratives, chronicles and procedure reflection; session-live rolling summaries have a shorter horizon than durable checkpoints. These findings do not inherit the stronger meaning of successful learning or self-improvement. See [MEM-RTE-temporal-synthesis](memory.md#mem-rte-temporal-synthesis), [MEM-RTE-chronicle-retention](memory.md#mem-rte-chronicle-retention) and [RT-RTE-skill-change](runtime.md#rt-rte-skill-change). Fallback notices and unsummarized emergency cuts are not silently treated as successful summaries.

Learning authority belongs to experience at an update consumer; knowledge or instruction belongs to the resulting artifact at its later work consumer. Ranking belongs to retained text, vectors and metadata used by selectors. Forgotten flags and local pin/task/terminal checks have enforcing force only at their named consumers. They establish neither truth acceptance nor global protection. See [MEM-BAP-memory-selectors](memory.md#mem-bap-memory-selectors), [RT-BAP-skill-instruction](runtime.md#rt-bap-skill-instruction) and [WF-RTE-completion-admission](workflow.md#wf-rte-completion-admission).

Consolidation and deduplication describe implemented selection/compression/merge mechanisms, not universal semantic fidelity. Substring loss, first-line omission or a model extraction error does not establish synthesis. The maximum-importance assignment in [EPI-RTE-batch-consolidation](epistemic.md#epi-rte-batch-consolidation) supports salience promotion of the survivor; it does not establish epistemic endorsement. Novel claims in particular model outputs remain unresolved, as [EPI-RTE-memory-extraction](epistemic.md#epi-rte-memory-extraction) explains.

Requested recall uses lexical/vector/graph algorithms, but its fulfillment remains pull. Automatic participant matching and required-skill name resolution establish identifier push because they select delivered retained parts. Availability, chronological windows and budgets separately establish coarse push. A stored label alone establishes neither direction nor signal. See [MEM-RTE-memory-recall](memory.md#mem-rte-memory-recall), [MEM-RTE-context-supply](memory.md#mem-rte-context-supply) and [RT-CLM-required-skills](runtime.md#rt-clm-required-skills).

Initial authored content and generic administrative identity do not settle write agency. No manual value or negative trace-learning finding is manufactured from those gaps. Full attachment payloads, org seeding/refresh, auxiliary state revisions and restored-worker alternatives remain unresolved. Known displays and local routes do not license complete-value statistics for those surfaces.

Additional source reads: none. Classification used only the supplied accepted members and their records; no quotes or new records were added.
