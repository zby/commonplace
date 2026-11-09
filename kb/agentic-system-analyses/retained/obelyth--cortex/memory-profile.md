---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Cortex memory comparison: Git notes, working state, usage-derived context selection, answer replay and host-maintenance doctrine."
run-id: "AAS-2026-11-07-cortex-6101286707a0-01"
source-identity: "https://github.com/obelyth/cortex"
reviewed-boundary: "65d449a3275eee51efd6ce0c275572806ee9d553"
memory-comparison:
  version: 2
  scope: "Retained private Git notes/descriptions, optional Postgres mirror and working state, serving access history and derived scores/pins/edges, KV answer/proposal state, local curation outputs, host-maintenance results and later-consumed administrative receipts. Included unresolved alternatives: initial seed/private content admission/provenance, maintenance-log origin, detailed operational event/receipt retention and consumption. Excluded: static shipped contracts/skills, current response-only diagnostics, unretained evaluation output, provider internals and external-host conversation/checkpoint state."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Durable notes, descriptions and proposal publication receipts"
          assessment: "known"
          findings:
            -
              value: "repo"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "runtime.md#rt-rte-proposal-admission"
              note: "GitHub blobs and commits retain content and atomic proposal receipts."
          records:
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-rte-proposal-admission"
          note: "Repository retention is distinct from transient rendering."
        -
          scope: "Note mirror, working bodies/state, access events, score/pin and edge rows"
          assessment: "known"
          findings:
            -
              value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-mirror"
                - "memory.md#mem-obj-bubble-body"
                - "memory.md#mem-obj-bubble-state"
                - "memory.md#mem-obj-note-access"
                - "memory.md#mem-obj-note-scores"
                - "memory.md#mem-obj-note-edges"
              note: "Optional Postgres stores retained content and symbolic access structures; score views read retained rows."
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-mirror"
              note: "Process corpus caches retain complete prior snapshots for later calls."
          records:
            - "memory.md#mem-obj-mirror"
            - "memory.md#mem-obj-bubble-body"
            - "memory.md#mem-obj-bubble-state"
            - "memory.md#mem-obj-note-access"
            - "memory.md#mem-obj-note-scores"
            - "memory.md#mem-obj-note-edges"
          note: "A graph-shaped table is still relational storage; no separate graph database is established."
        -
          scope: "Answer replay and pending proposal queue"
          assessment: "known"
          findings:
            -
              value: "kv"
              basis: "wired"
              records:
                - "memory.md#mem-obj-cached-answer"
                - "runtime.md#rt-rte-proposal-admission"
              note: "KV retains rendered replies and review payloads."
          records:
            - "memory.md#mem-obj-cached-answer"
            - "runtime.md#rt-rte-proposal-admission"
          note: "Git receipts remain separately classified as repo."
        -
          scope: "Local import/backfill/split outputs before publication"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-rte-local-curation"
              note: "Local note files are written before separate Git publication on backfill/split routes."
          records:
            - "memory.md#mem-rte-local-curation"
          note: "Imported GitHub content is covered by repository storage."
        -
          scope: "Initial private corpus and administrative receipt/event storage details"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-rte-production-jobs"
            - "runtime.md#rt-rte-capability-configuration"
          note: "Initial content and full operational payload retention are not recorded sufficiently for exhaustive storage classification."
      records:
        - "memory.md#mem-obj-notes"
        - "runtime.md#rt-rte-proposal-admission"
        - "memory.md#mem-obj-mirror"
        - "memory.md#mem-obj-bubble-body"
        - "memory.md#mem-obj-bubble-state"
        - "memory.md#mem-obj-note-access"
        - "memory.md#mem-obj-note-scores"
        - "memory.md#mem-obj-note-edges"
        - "memory.md#mem-obj-cached-answer"
        - "memory.md#mem-rte-local-curation"
        - "runtime.md#rt-rte-production-jobs"
        - "runtime.md#rt-rte-capability-configuration"
      note: "Inspected retained stores are classified; operational-log and administrative details prevent complete enumeration. Provider internals and external host histories are outside the memory boundary."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Note and description prose, working bodies, cached replies and proposal text at interpretive consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-router"
                - "memory.md#mem-obj-bubble-body"
                - "memory.md#mem-obj-cached-answer"
                - "runtime.md#rt-rte-proposal-admission"
              note: "Reader, external host and reviewer interpret prose; projected descriptions do not resolve full private-note content."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-router"
            - "memory.md#mem-obj-bubble-body"
            - "memory.md#mem-obj-cached-answer"
            - "runtime.md#rt-rte-proposal-admission"
          note: "This classification covers the established textual parts, not unknown note semantics."
        -
          scope: "Paths, correction markers, working state, access rows, scores, edges, cache keys and receipts at fixed-rule consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-bubble-state"
                - "memory.md#mem-obj-note-access"
                - "memory.md#mem-obj-note-scores"
                - "memory.md#mem-obj-note-edges"
                - "memory.md#mem-obj-cached-answer"
                - "runtime.md#rt-rte-proposal-admission"
              note: "Localized fields and explicit arithmetic determine selection, state and replay; numerical scores are not distributed parameters."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-bubble-state"
            - "memory.md#mem-obj-note-access"
            - "memory.md#mem-obj-note-scores"
            - "memory.md#mem-obj-note-edges"
            - "memory.md#mem-obj-cached-answer"
            - "runtime.md#rt-rte-proposal-admission"
          note: "Natural-language edge evidence and pin reasons retain their separate display consumption."
        -
          scope: "Uninspected initial content and detailed administrative event payloads"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-rte-production-jobs"
          note: "Reports do not establish every operative part of these payloads."
      records:
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-router"
        - "memory.md#mem-obj-bubble-body"
        - "memory.md#mem-obj-cached-answer"
        - "runtime.md#rt-rte-proposal-admission"
        - "memory.md#mem-obj-bubble-state"
        - "memory.md#mem-obj-note-access"
        - "memory.md#mem-obj-note-scores"
        - "memory.md#mem-obj-note-edges"
        - "runtime.md#rt-rte-production-jobs"
      note: "Mixed parts are split by consumption. Provider model weights are not accumulated Cortex memory, so no parametric memory finding follows from reader inference."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Caller-authored note and working-body submissions"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-bubble-body"
                - "runtime.md#rt-rte-trusted-write"
              note: "Direct write/capture and deliberate bubble updates accept caller-supplied content; this does not identify a human author."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-bubble-body"
            - "runtime.md#rt-rte-trusted-write"
          note: "Submission lineage is known independently of upstream authorship."
        -
          scope: "Local note import and supplied description metadata"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-rte-local-curation"
                - "epistemic.md#epi-rte-description-backfill"
              note: "File bodies and caller JSON metadata enter retained notes without semantic certification."
          records:
            - "memory.md#mem-rte-local-curation"
            - "epistemic.md#epi-rte-description-backfill"
          note: "External input origin remains unknown."
        -
          scope: "Mirror, parsed router metadata, structural graph and rendered answer cache"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-mirror"
                - "memory.md#mem-obj-router"
                - "memory.md#mem-obj-note-edges"
                - "memory.md#mem-obj-cached-answer"
              note: "Copy/reconciliation, parsing, structural derivation and answer rendering create retained or later-consumed representations."
          records:
            - "memory.md#mem-obj-mirror"
            - "memory.md#mem-obj-router"
            - "memory.md#mem-obj-note-edges"
            - "memory.md#mem-obj-cached-answer"
          note: "Model answer generation does not establish trace extraction."
        -
          scope: "Usage-derived scoring and coaccess"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-usage-selection"
                - "memory.md#mem-obj-note-access"
                - "memory.md#mem-obj-note-scores"
                - "memory.md#mem-obj-note-edges"
              note: "Retained serving events feed later score/graph selection inputs."
          records:
            - "memory.md#mem-rte-usage-selection"
            - "memory.md#mem-obj-note-access"
            - "memory.md#mem-obj-note-scores"
            - "memory.md#mem-obj-note-edges"
          note: "Structural edges have a different nontrace lineage."
        -
          scope: "Groundskeeper-derived pages and digest"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-groundskeeper-maintenance"
              note: "Procedure requests selecting durable facts from daily activity logs and retaining results."
          records:
            - "runtime.md#rt-rte-groundskeeper-maintenance"
          note: "This is requested host processing, not observed execution."
        -
          scope: "Initial seed/private content and original maintenance-log provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-rte-groundskeeper-maintenance"
          note: "Initial authorship and whether log bodies originated in conversations, tools or other sources are unresolved."
      records:
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-bubble-body"
        - "runtime.md#rt-rte-trusted-write"
        - "memory.md#mem-rte-local-curation"
        - "epistemic.md#epi-rte-description-backfill"
        - "memory.md#mem-obj-mirror"
        - "memory.md#mem-obj-router"
        - "memory.md#mem-obj-note-edges"
        - "memory.md#mem-obj-cached-answer"
        - "memory.md#mem-rte-usage-selection"
        - "memory.md#mem-obj-note-access"
        - "memory.md#mem-obj-note-scores"
        - "runtime.md#rt-rte-groundskeeper-maintenance"
      note: "Known derivation paths do not resolve private initial content or maintenance trace provenance."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Note bodies, descriptions, bubble text, cached answers and proposal prose at later interpretive consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-router"
                - "memory.md#mem-obj-bubble-body"
                - "memory.md#mem-obj-cached-answer"
                - "runtime.md#rt-rte-proposal-admission"
              note: "Retained text supplies reference/context or review evidence, not guaranteed obedience."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-router"
            - "memory.md#mem-obj-bubble-body"
            - "memory.md#mem-obj-cached-answer"
            - "runtime.md#rt-rte-proposal-admission"
          note: "Standing instruction force at external hosts is not established."
        -
          scope: "Retained note text/metadata, temperatures, pins and edges at selectors"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-reader-answer"
                - "memory.md#mem-obj-router"
                - "memory.md#mem-obj-note-scores"
                - "memory.md#mem-obj-note-edges"
                - "memory.md#mem-rte-usage-selection"
              note: "Lexical text selection, bands, pins and graph weights influence relative priority."
          records:
            - "runtime.md#rt-rte-reader-answer"
            - "memory.md#mem-obj-router"
            - "memory.md#mem-obj-note-scores"
            - "memory.md#mem-obj-note-edges"
            - "memory.md#mem-rte-usage-selection"
          note: "Ranking does not require learned weights."
        -
          scope: "Retained working-state, path/scope/cache identities and replay/admission receipts"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-bubble-state"
                - "memory.md#mem-obj-cached-answer"
                - "runtime.md#rt-rte-proposal-admission"
                - "runtime.md#rt-rte-guest-mediation"
              note: "Project/status, matching cache identity, scope and operation receipts select delivery or recovery routes."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-bubble-state"
                - "runtime.md#rt-rte-proposal-admission"
                - "runtime.md#rt-rte-guest-mediation"
              note: "Closed working items leave open delivery; scope excludes notes and terminal receipts prevent replayed mutation."
            -
              value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-proposal-admission"
                - "runtime.md#rt-rte-production-jobs"
              note: "Expected payload/fingerprint and prior receipts constrain admissible retry or competing actions."
          records:
            - "memory.md#mem-obj-bubble-state"
            - "memory.md#mem-obj-cached-answer"
            - "runtime.md#rt-rte-proposal-admission"
            - "runtime.md#rt-rte-guest-mediation"
            - "runtime.md#rt-rte-production-jobs"
          note: "These are fixed-rule controls, not semantic truth checks."
        -
          scope: "Access history at automatic score/graph update consumers"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-usage-selection"
              note: "Recorded experience feeds durable behavior-shaping ranking inputs, separately from their downstream ranking authority."
          records:
            - "memory.md#mem-rte-usage-selection"
          note: "No improvement claim follows."
        -
          scope: "Daily logs at host maintenance update consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-groundskeeper-maintenance"
              note: "Requested automatic filing transforms retained activity into later-used pages and digest."
          records:
            - "runtime.md#rt-rte-groundskeeper-maintenance"
          note: "Host scheduling and execution remain unobserved."
        -
          scope: "Private note standing directions and detailed administrative payload consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-rte-capability-configuration"
          note: "External-host force and all administrative event consumption are not established."
      records:
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-router"
        - "memory.md#mem-obj-bubble-body"
        - "memory.md#mem-obj-cached-answer"
        - "runtime.md#rt-rte-proposal-admission"
        - "runtime.md#rt-rte-reader-answer"
        - "memory.md#mem-obj-note-scores"
        - "memory.md#mem-obj-note-edges"
        - "memory.md#mem-rte-usage-selection"
        - "memory.md#mem-obj-bubble-state"
        - "runtime.md#rt-rte-guest-mediation"
        - "runtime.md#rt-rte-production-jobs"
        - "runtime.md#rt-rte-groundskeeper-maintenance"
        - "runtime.md#rt-rte-capability-configuration"
      note: "Known consumers support knowledge, ranking, routing, enforcement, validation and learning. Shipped answer and maintenance instructions are static, excluded from accumulated-memory instruction classification; private-host instruction authority remains unresolved."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Usage event admission and score/graph derivation; mirror healing and answer caching"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-usage-selection"
                - "memory.md#mem-obj-mirror"
                - "memory.md#mem-obj-cached-answer"
                - "epistemic.md#epi-rte-answer-cache"
              note: "Software admits/transforms retained material without per-content operator approval."
          records:
            - "memory.md#mem-rte-usage-selection"
            - "memory.md#mem-obj-mirror"
            - "memory.md#mem-obj-cached-answer"
            - "epistemic.md#epi-rte-answer-cache"
          note: "A user initiating Ask does not approve every stored event or derived edge."
        -
          scope: "Console attention status changes and explicit operator pin overrides"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-trusted-write"
                - "memory.md#mem-obj-note-scores"
              note: "Human console action selects verification/reverify/settled changes; operator chooses pin override."
          records:
            - "runtime.md#rt-rte-trusted-write"
            - "memory.md#mem-obj-note-scores"
          note: "This does not make all direct notes or automatic scores manual."
        -
          scope: "Groundskeeper filing and corrections"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-groundskeeper-maintenance"
              note: "Host model selects content under the requested procedure without per-item approval."
          records:
            - "runtime.md#rt-rte-groundskeeper-maintenance"
          note: "Human proposal acceptance is a separate template policy."
        -
          scope: "Proposal decisions under the groundskeeper human-review policy"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-groundskeeper-maintenance"
                - "runtime.md#rt-rte-proposal-admission"
              note: "Template reserves accept/reject to a human, unlike generic trusted acceptance."
          records:
            - "runtime.md#rt-rte-groundskeeper-maintenance"
            - "runtime.md#rt-rte-proposal-admission"
          note: "Policy is not universal server enforcement."
        -
          scope: "Generic trusted note/bubble/proposal admission, initial corpus and local batch scripts"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-trusted-write"
            - "runtime.md#rt-rte-proposal-admission"
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-bubble-body"
            - "memory.md#mem-rte-local-curation"
          note: "Credentialed caller identity and batch apply/commit flags do not establish per-content human control; initial admission is unresolved."
      records:
        - "memory.md#mem-rte-usage-selection"
        - "memory.md#mem-obj-mirror"
        - "memory.md#mem-obj-cached-answer"
        - "epistemic.md#epi-rte-answer-cache"
        - "runtime.md#rt-rte-trusted-write"
        - "memory.md#mem-obj-note-scores"
        - "runtime.md#rt-rte-groundskeeper-maintenance"
        - "runtime.md#rt-rte-proposal-admission"
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-bubble-body"
        - "memory.md#mem-rte-local-curation"
      note: "Known software and explicit human mechanisms coexist with unresolved caller-controlled admission; authorship and physical storage do not settle agency."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Existing note and bubble replacement/update paths"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-trusted-write"
                - "memory.md#mem-obj-bubble-body"
              note: "Edit/replace and body update revise retained entries without a semantic quality prerequisite."
          records:
            - "runtime.md#rt-rte-trusted-write"
            - "memory.md#mem-obj-bubble-body"
          note: "Revision capability is established, not improved correctness."
        -
          scope: "Working-item lifecycle and bounded access influence"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-bubble-state"
              note: "Filed/dropped/aged items remain historical but leave open context."
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-obj-note-scores"
                - "memory.md#mem-obj-bubble-state"
                - "memory.md#mem-obj-cached-answer"
              note: "Time-decayed access/write influence, working-item aging and cache TTL reduce retained availability or priority."
            -
              value: "promote"
              basis: "wired"
              records:
                - "memory.md#mem-obj-note-scores"
              note: "An explicit hotter pin raises selection salience without rewriting the note."
          records:
            - "memory.md#mem-obj-bubble-state"
            - "memory.md#mem-obj-note-scores"
            - "memory.md#mem-obj-cached-answer"
          note: "Retirement nomination alone does not withdraw a note."
        -
          scope: "Groundskeeper log filing, drift corrections and supersession"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-groundskeeper-maintenance"
              note: "Procedure selects standing facts from retained logs into reduced durable page representations while keeping logs."
            -
              value: "evolve"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-groundskeeper-maintenance"
              note: "Drift procedure requests corrections to existing pages."
            -
              value: "invalidate"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-groundskeeper-maintenance"
              note: "SUPERSEDED/was conventions request withdrawal of current reliance while preserving history."
          records:
            - "runtime.md#rt-rte-groundskeeper-maintenance"
          note: "Requested transformations are not wired host execution."
        -
          scope: "Private content transformations and downstream retirement actions"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-rte-local-curation"
            - "memory.md#mem-rte-retirement-nomination"
          note: "Unknown original content and later human retirement action prevent exhaustive semantic-operation classification; relocation, rebuilds and collision checks do not establish dedup or synthesis."
      records:
        - "runtime.md#rt-rte-trusted-write"
        - "memory.md#mem-obj-bubble-body"
        - "memory.md#mem-obj-bubble-state"
        - "memory.md#mem-obj-note-scores"
        - "memory.md#mem-obj-cached-answer"
        - "runtime.md#rt-rte-groundskeeper-maintenance"
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-rte-local-curation"
        - "memory.md#mem-rte-retirement-nomination"
      note: "Implemented curation and maintenance doctrine retain distinct bases. No new-claim synthesis or semantic dedup finding is inferred from generation or reorganization labels."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Explicit read/corpus/context/handoff, working-state list, cached Ask and proposal review requests"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "memory.md#mem-obj-bubble-body"
                - "memory.md#mem-obj-cached-answer"
                - "runtime.md#rt-rte-proposal-admission"
              note: "Requested retained material is returned to its requesting consumer; delivery is not an extra push."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "memory.md#mem-obj-bubble-body"
            - "memory.md#mem-obj-cached-answer"
            - "runtime.md#rt-rte-proposal-admission"
          note: "Covers return operations, not independent selection inside the chain."
        -
          scope: "Automatic bundle/reader selection from retained notes and access structures"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "runtime.md#rt-rte-reader-answer"
                - "memory.md#mem-rte-usage-selection"
                - "memory.md#mem-obj-router"
              note: "Code chooses which retained parts enter a reader call or boot/project bundle without an item-specific request from that downstream consumer."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "runtime.md#rt-rte-reader-answer"
            - "memory.md#mem-rte-usage-selection"
            - "memory.md#mem-obj-router"
          note: "Upstream request triggers the operation; internal supply and requested return are separate."
        -
          scope: "Groundskeeper log and page acquisition"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-groundskeeper-maintenance"
              note: "Procedure directs host to request yesterday/today logs and destination pages."
          records:
            - "runtime.md#rt-rte-groundskeeper-maintenance"
          note: "No unsolicited Cortex scheduler initiation is established."
        -
          scope: "Detailed administrative history and initialization alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-rte-production-jobs"
            - "runtime.md#rt-rte-capability-configuration"
          note: "Record coverage does not settle all administrative read-back chains."
      records:
        - "runtime.md#rt-rte-context-delivery"
        - "memory.md#mem-obj-bubble-body"
        - "memory.md#mem-obj-cached-answer"
        - "runtime.md#rt-rte-proposal-admission"
        - "runtime.md#rt-rte-reader-answer"
        - "memory.md#mem-rte-usage-selection"
        - "memory.md#mem-obj-router"
        - "runtime.md#rt-rte-groundskeeper-maintenance"
        - "memory.md#mem-obj-notes"
        - "runtime.md#rt-rte-production-jobs"
        - "runtime.md#rt-rte-capability-configuration"
      note: "Both requested return and automatic downstream selection exist; no server-initiated conversation is inferred."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Boot availability/recency/temperature/budget selection"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-router"
                - "runtime.md#rt-rte-context-delivery"
                - "memory.md#mem-obj-bubble-state"
                - "memory.md#mem-obj-note-scores"
              note: "Boot trigger selects profile head, month discovery rows, recent logs and usable open working state by fixed availability, age, bands and budgets."
          records:
            - "memory.md#mem-obj-router"
            - "runtime.md#rt-rte-context-delivery"
            - "memory.md#mem-obj-bubble-state"
            - "memory.md#mem-obj-note-scores"
          note: "Trigger is boot; inputs are inventory/age/state/bands, selected parts are note descriptions, profile/log text and working snippets."
        -
          scope: "Project context and handoff targeting"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "memory.md#mem-obj-bubble-state"
                - "memory.md#mem-obj-note-edges"
              note: "Project/path matches select project page, matching working items and graph endpoint neighbors for supplied context."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "memory.md#mem-obj-bubble-state"
            - "memory.md#mem-obj-note-edges"
          note: "Trigger is scoped boot/handoff; actual project and endpoint matching selects delivered parts, beyond naming a requested file."
        -
          scope: "Question-driven reader and query selection"
          assessment: "known"
          findings:
            -
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-reader-answer"
                - "runtime.md#rt-rte-context-delivery"
                - "memory.md#mem-obj-notes"
              note: "Question tokens select retained note text through lexical narrowing before reader inference."
          records:
            - "runtime.md#rt-rte-reader-answer"
            - "runtime.md#rt-rte-context-delivery"
            - "memory.md#mem-obj-notes"
          note: "Trigger is Ask/query; question is selector input; selected note bodies enter the reader or bundle."
        -
          scope: "Groundskeeper host-requested log/page acquisition and subsequent filing"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-groundskeeper-maintenance"
          note: "Within this procedure the host requests logs and pages, then chooses facts for retained writes. The recorded reads are pull; fact selection is write-side curation. Neither establishes an automatic push supplying retained parts without the consuming host's request, so this unit has no push-selection signal."
        -
          scope: "Unresolved administrative and initial-content selection alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-rte-production-jobs"
          note: "Detailed administrative retained-payload selection is not fully recorded."
      records:
        - "memory.md#mem-obj-router"
        - "runtime.md#rt-rte-context-delivery"
        - "memory.md#mem-obj-bubble-state"
        - "memory.md#mem-obj-note-scores"
        - "memory.md#mem-obj-note-edges"
        - "runtime.md#rt-rte-reader-answer"
        - "memory.md#mem-obj-notes"
        - "runtime.md#rt-rte-groundskeeper-maintenance"
        - "runtime.md#rt-rte-production-jobs"
      note: "Wired boot, project and question-driven push selectors support coarse, identifier and inferred-lexical signals. Groundskeeper acquisition is pull and its fact selection is write-side curation, so neither contributes a push signal. Administrative selection remains unresolved; no embedding or judgment-based push selector is established."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Automatic access-event to scores/coaccess to later router/handoff"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-usage-selection"
                - "memory.md#mem-obj-note-access"
                - "memory.md#mem-obj-note-scores"
                - "memory.md#mem-obj-note-edges"
              note: "Recorded serving activity automatically shapes retained selection state consumed in later requests."
          records:
            - "memory.md#mem-rte-usage-selection"
            - "memory.md#mem-obj-note-access"
            - "memory.md#mem-obj-note-scores"
            - "memory.md#mem-obj-note-edges"
          note: "Meets trace-fed durable behavior-shaping write definition without improved-capacity evidence."
        -
          scope: "Groundskeeper log-to-page/digest-to-later-context"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-groundskeeper-maintenance"
              note: "Host procedure requests automatic derivation from activity logs, persistent page/digest writes and subsequent consumption."
          records:
            - "runtime.md#rt-rte-groundskeeper-maintenance"
          note: "A configured and exercised host loop is not established."
        -
          scope: "Initial/private content, caller-controlled captures and detailed administrative traces"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-rte-trusted-write"
            - "runtime.md#rt-rte-production-jobs"
            - "runtime.md#rt-rte-capability-configuration"
          note: "Original input and any qualifying derivation/later-consumer chain are unresolved; storing raw records alone is insufficient."
      records:
        - "memory.md#mem-rte-usage-selection"
        - "memory.md#mem-obj-note-access"
        - "memory.md#mem-obj-note-scores"
        - "memory.md#mem-obj-note-edges"
        - "runtime.md#rt-rte-groundskeeper-maintenance"
        - "memory.md#mem-obj-notes"
        - "runtime.md#rt-rte-trusted-write"
        - "runtime.md#rt-rte-production-jobs"
        - "runtime.md#rt-rte-capability-configuration"
      note: "Supported yes findings coexist with unresolved routes. No bounded absence record permits local or system-wide no; provider training and external-host compaction are excluded."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Serving telemetry feeding automatic score/coaccess updates"
          assessment: "known"
          findings:
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-note-access"
                - "memory.md#mem-rte-usage-selection"
              note: "Original rows record served tool requests/path delivery, not semantic use or conversation turns."
            -
              value: "event-streams"
              basis: "wired"
              records:
                - "memory.md#mem-obj-note-access"
                - "memory.md#mem-rte-usage-selection"
              note: "Timestamped runtime access observations are discrete serving events consumed by time-window/decay derivation."
          records:
            - "memory.md#mem-obj-note-access"
            - "memory.md#mem-rte-usage-selection"
          note: "Two values describe recorded tool activity and its runtime-event origin, not a wrapper-created origin."
        -
          scope: "Groundskeeper daily activity logs feeding requested derived pages"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-groundskeeper-maintenance"
            - "memory.md#mem-obj-notes"
          note: "Recorded daily prose may originate with human/model/tool/mixed activity. A dated Markdown log is not sufficient to choose session-logs, tool-traces, event-streams or trajectories."
        -
          scope: "Initial/caller-supplied and administrative possible trace-fed alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-rte-trusted-write"
            - "runtime.md#rt-rte-production-jobs"
          note: "Full original payload provenance and qualifying updates are not established."
      records:
        - "memory.md#mem-obj-note-access"
        - "memory.md#mem-rte-usage-selection"
        - "runtime.md#rt-rte-groundskeeper-maintenance"
        - "memory.md#mem-obj-notes"
        - "runtime.md#rt-rte-trusted-write"
        - "runtime.md#rt-rte-production-jobs"
      note: "Usage trace origin is supported, while maintenance and private-input origins remain unresolved. Adapter names and daily-log dates do not establish session or trajectory content."
---

# Cortex memory profile

## Comparison rationale

The profile classifies accepted records, not a deployment. All positive findings retain implementation wiring or attributed procedure as their basis. No supplied execution establishes exercised maintenance, changed host behavior, improved answers or causal benefit. The partial assessments preserve the memory report's unresolved initial-content, operational-payload and provenance inventory rather than treating one positive route as complete coverage.

**Content versus access structures.** [MEM-OBJ-notes](memory.md#mem-obj-notes) and [MEM-OBJ-bubble-body](memory.md#mem-obj-bubble-body) supply interpreted context; [MEM-OBJ-bubble-state](memory.md#mem-obj-bubble-state), [MEM-OBJ-note-scores](memory.md#mem-obj-note-scores) and [MEM-OBJ-note-edges](memory.md#mem-obj-note-edges) supply fixed-rule selection inputs. Postgres edges establish relational storage with graph structure, not a separate graph database. Scalar score arithmetic is symbolic, not parametric. Static [RT-OBJ-answer-contract](runtime.md#rt-obj-answer-contract) and [RT-BAP-maintenance-instructions](runtime.md#rt-bap-maintenance-instructions) explain instruction force but are not accumulated memory. Unknown private-host interpretation does not establish an instruction finding.

**Admission is mechanism-specific.** Software event/graph/cache admission is automatic. Human attention changes and pins have their own manual warrant. Credentialed generic writers, proposal reviewers and batch-script callers do not establish who approved individual content. The groundskeeper's human proposal-review policy remains a claimed manual mechanism alongside claimed automatic filing; it does not narrow the trusted server grant. See [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write), [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission), [MEM-RTE-local-curation](memory.md#mem-rte-local-curation) and [RT-RTE-groundskeeper-maintenance](runtime.md#rt-rte-groundskeeper-maintenance).

**Direction follows the operation.** [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) returns requested retained content: pull. Its internal selectors also choose parts for downstream context without item-specific requests: push. [RT-RTE-reader-answer](runtime.md#rt-rte-reader-answer) supplies question-selected notes to the provider, then returns an answer to the requester. Availability/budget filters, project/endpoint identity matches and lexical targeting remain separate signals. Explicit path requests and exact answer-cache lookup are not extra identifier-based pushes. The groundskeeper requests its logs and destination pages; choosing which facts to file is write-side curation, not judgment-based push retrieval. Its bounded date/order rules likewise govern host-requested acquisition, not a separate coarse push. Read-back signal is therefore inapplicable to that local acquisition/filing unit, while the axis remains partial because wired push selectors coexist with unresolved administrative selection.

**Learning is not demonstrated improvement.** [MEM-RTE-usage-selection](memory.md#mem-rte-usage-selection) establishes a wired trace-to-retained-selector-to-later-context chain. Access history has learning authority at its update consumer; derived scores and edges have ranking authority at later selectors. [RT-RTE-groundskeeper-maintenance](runtime.md#rt-rte-groundskeeper-maintenance) supplies a separate claimed log-to-page/digest chain. Its log consolidation retains raw logs; this is not synthesis merely because a host model performs the selection. Neither chain establishes improved capacity. [MEM-CLM-evaluation-gate](memory.md#mem-clm-evaluation-gate) and [EPI-RTE-prediction-evaluation](epistemic.md#epi-rte-prediction-evaluation) do not install a winning ranker.

Serving rows record tool activity and discrete runtime observations, supporting tool-traces and event-streams for that usage route. They do not establish recorded conversational turns or linked state/action/outcome trajectories. The groundskeeper's dated activity prose has unresolved original content, so its trace source cannot be classified merely from the word log. Cached answers are retained model responses, not automatically experience-fed behavior updates: [MEM-OBJ-cached-answer](memory.md#mem-obj-cached-answer) and [EPI-RTE-answer-cache](epistemic.md#epi-rte-answer-cache) license replay, not reader training.

**Curation remains local.** Note/body revision supports evolve; retained working history leaving open context supports invalidate; bounded age/TTL and score decay support decay; hotter pin overrides support promote. The maintenance procedure separately requests consolidation and historical correction/withdrawal. [MEM-RTE-retirement-nomination](memory.md#mem-rte-retirement-nomination) only nominates: it does not support executed deletion or semantic invalidation. Import collision checks, mirror rebuilds and file relocation do not establish dedup, and generated answers alone do not establish synthesis of new claims in curated memory.

**Canonical identity.** Reconciliation supersedes EPI-OBJ-note with [MEM-OBJ-notes](memory.md#mem-obj-notes), EPI-OBJ-note-edges with [MEM-OBJ-note-edges](memory.md#mem-obj-note-edges), and EPI-RTE-retirement-nomination with [MEM-RTE-retirement-nomination](memory.md#mem-rte-retirement-nomination). Those canonical records support the corresponding content/form/storage, graph/ranking and nomination limits here. The graph-rebuild and usage-selection routes remain distinct, as do current reader replies and retained cached answers. No supersession upgrades evidence strength.

**Source-read log.** No frozen-source reads were needed or performed. Classification uses only the supplied accepted runtime, memory, epistemic and workflow records and their reconciliation; no records or evidence were added.
