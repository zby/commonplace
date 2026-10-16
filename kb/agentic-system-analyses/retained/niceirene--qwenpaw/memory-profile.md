---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'QwenPaw memory comparison: native checkpoints, Scroll history and summaries, ReMe notes
  and access representations, ADBPG, mutable workspace guidance and unresolved alternate consumers.'
run-id: AAS-2026-10-15-qwenpaw-e41495d47fc0-01
source-identity: https://github.com/niceirene/qwenpaw
reviewed-boundary: 16b2e712d198166c9359e77055b13bf2668bf5ae
memory-comparison:
  version: 2
  scope: 'Retained objects accumulated or changed through use: native session live/summary/control parts;
    Scroll SQLite history, continuation summary and eviction index; ReMe daily/session/digest notes, catalogs,
    cached embeddings and notifications; ADBPG retained service memory and local fallback; edited workspace
    prompt files; archive/replay artifacts; harness thread continuation; fork saved-context and retained
    project/registry paths. Opaque provider payloads, native dependency compaction, initial content and
    auxiliary governance/plugin/checkpoint/backup memory remain unresolved included alternatives. Auxiliary
    mail-thread/browser stores are included in the reports coverage limit, not inspected inventory witnesses.
    Excludes shipped unchanged instruction templates, inference/reranker model weights not shown to accumulate
    through use, ordinary current-run tool results without retention, and turn-local visual projection/recovery.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Daily/session notes and dream/paper digest files
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-daily-note
          - memory.md#mem-obj-digest
          note: Configured workspace Markdown/vault and local catalogs are file storage, not a graph substrate
            merely because they contain links.
        records: *id001
        note: Configured workspace Markdown/vault and local catalogs are file storage, not a graph substrate
          merely because they contain links.
      - scope: 'Session JSON: live state, native summary, Scroll summary/index and pending extraction
          state'
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id002
          - runtime.md#rt-obj-session-state
          - memory.md#mem-rte-scroll-retention
          - memory.md#mem-obj-continuation-summary
          - memory.md#mem-obj-eviction-index
          note: Session-directory files persist these separately produced parts.
        records: *id002
        note: Session-directory files persist these separately produced parts.
      - scope: Scroll history rows
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records: &id003
          - memory.md#mem-obj-history
          note: HistoryStore uses workspace history.db.
        records: *id003
        note: HistoryStore uses workspace history.db.
      - scope: Native JSONL archives, debug replay files and saved large tool text
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id004
          - memory.md#mem-rte-archive-replay
          note: JSONL and UUID text artifacts are retained files.
        records: *id004
        note: JSONL and UUID text artifacts are retained files.
      - scope: Mutable workspace prompt bodies
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id005
          - runtime.md#rt-obj-prompt-files
          - runtime.md#rt-rte-workspace-instruction
          note: Only edited/accumulated workspace bodies are included; packaged defaults alone are excluded.
        records: *id005
        note: Only edited/accumulated workspace bodies are included; packaged defaults alone are excluded.
      - scope: Optional ReMe cached embeddings
        assessment: partial
        findings:
        - value: vector
          basis: wired
          records:
          - memory.md#mem-cmp-embedding-model
          note: embedding_store caches numerical access representations; disabled/uncredentialed configurations
            may use keywords instead.
        records:
        - memory.md#mem-cmp-embedding-model
        note: Cached vectors are established, but complete cache backing and provider-side retained state
          are not exposed.
      - scope: ADBPG retained memory service
        assessment: partial
        findings:
        - value: service-object
          basis: wired
          records:
          - memory.md#mem-obj-adbpg-memory
          note: REST add/search addresses retained service memory.
        records:
        - memory.md#mem-obj-adbpg-memory
        - memory.md#mem-rte-adbpg-retention
        note: The external retained service object is known; database, embedding and other internal substrates
          cannot be inferred from its name.
      - scope: ReMe inbox notifications
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-inbox-event
        note: Application inbox retention is identified, but its storage implementation is uninspected.
      - scope: Alternative harness retained threads and session bridge
        assessment: partial
        findings:
        - value: service-object
          basis: wired
          records:
          - runtime.md#rt-rte-harness-turn
          note: Codex retained thread identity is resumed through the external runtime.
        records:
        - runtime.md#rt-rte-harness-turn
        note: Thread resume and persisted mappings are wired; complete provider storage is opaque.
      - scope: Fork project product retained for integration
        assessment: known
        findings:
        - value: repo
          basis: wired
          records: &id006
          - runtime.md#rt-rte-fork-worker
          - workflow.md#wf-rte-fork-finalization
          note: Git commits/branches and worktrees persist as project products; registry backing is a
            separate unresolved part.
        records: *id006
        note: Git commits/branches and worktrees persist as project products; registry backing is a separate
          unresolved part.
      - scope: Fork registry backing, governance reuse, plugin-owned memory and checkpoint/backup payload
          storage
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-tool-governance
        - runtime.md#rt-rte-plugin-install
        - epistemic.md#epi-rte-checkpoint-restore
        - workflow.md#wf-rte-fork-finalization
        note: Records expose administrative retention or restoration but not a complete storage inventory.
      records:
      - memory.md#mem-obj-daily-note
      - memory.md#mem-obj-digest
      - runtime.md#rt-obj-session-state
      - memory.md#mem-rte-scroll-retention
      - memory.md#mem-obj-continuation-summary
      - memory.md#mem-obj-eviction-index
      - memory.md#mem-obj-history
      - memory.md#mem-rte-archive-replay
      - runtime.md#rt-obj-prompt-files
      - runtime.md#rt-rte-workspace-instruction
      - memory.md#mem-cmp-embedding-model
      - memory.md#mem-obj-adbpg-memory
      - memory.md#mem-rte-adbpg-retention
      - memory.md#mem-obj-inbox-event
      - runtime.md#rt-rte-harness-turn
      - runtime.md#rt-rte-fork-worker
      - workflow.md#wf-rte-fork-finalization
      - runtime.md#rt-rte-tool-governance
      - runtime.md#rt-rte-plugin-install
      - epistemic.md#epi-rte-checkpoint-restore
      note: Local file, SQLite, vector-cache and external-service witnesses do not enumerate all included
        auxiliary stores or provider-owned payloads.
    representational_form:
      assessment: partial
      units:
      - scope: Daily/session and digest prose
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: *id001
          note: Natural-language facts, topic content and readings reach search/model interpretation.
        records: *id001
        note: Natural-language facts, topic content and readings reach search/model interpretation.
      - scope: Note/digest paths, catalogs and interest metadata
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: *id001
          note: Paths, catalogs and YAML metadata use localized symbolic structure; this does not classify
            every interest consumer.
        records: *id001
        note: Paths, catalogs and YAML metadata use localized symbolic structure; this does not classify
          every interest consumer.
      - scope: Saved live messages, native summary, Scroll summary items and archive/tool text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id007
          - runtime.md#rt-obj-session-state
          - memory.md#mem-obj-continuation-summary
          - memory.md#mem-rte-archive-replay
          note: Text-bearing parts are interpreted as context, not executable rules because their container
            is JSON.
        records: *id007
        note: Text-bearing parts are interpreted as context, not executable rules because their container
          is JSON.
      - scope: Checkpoint metadata, history rows/IDs, index spans and recovery bookkeeping
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id008
          - runtime.md#rt-obj-session-state
          - memory.md#mem-obj-history
          - memory.md#mem-obj-eviction-index
          note: Serialization, version/status, sequence and tool-call identities have fixed consumer rules.
        records: *id008
        note: Serialization, version/status, sequence and tool-call identities have fixed consumer rules.
      - scope: History bodies and eviction headlines/previews
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id009
          - memory.md#mem-obj-history
          - memory.md#mem-obj-eviction-index
          note: Raw text and readable recovery descriptions remain distinct from their symbolic addressing.
        records: *id009
        note: Raw text and readable recovery descriptions remain distinct from their symbolic addressing.
      - scope: Selected mutable workspace prompt bodies
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id010
          - runtime.md#rt-obj-prompt-files
          note: Edited prose is interpreted as standing guidance.
        records: *id010
        note: Edited prose is interpreted as standing guidance.
      - scope: Optional cached dense embedding vectors
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: &id011
          - memory.md#mem-cmp-embedding-model
          note: Dense numerical access representations are parametric; this is not a claim that provider
            weights change through use.
        records: *id011
        note: Dense numerical access representations are parametric; this is not a claim that provider
          weights change through use.
      - scope: ADBPG delivered content/memory text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id012
          - memory.md#mem-obj-adbpg-memory
          - memory.md#mem-rte-memory-retrieval
          note: Returned textual part is known; this readable projection does not classify the full stored
            server payload.
        records: *id012
        note: Returned textual part is known; this readable projection does not classify the full stored
          server payload.
      - scope: ADBPG internal retained payload
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-adbpg-memory
        note: Server representation and embedding encoding are opaque.
      - scope: Inbox body
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id013
          - memory.md#mem-obj-inbox-event
          note: Bounded response.answer text is a display summary, not the full maintenance artifact.
        records: *id013
        note: Bounded response.answer text is a display summary, not the full maintenance artifact.
      - scope: Inbox status/job/path fields and fork registry status/head
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id014
          - memory.md#mem-obj-inbox-event
          - workflow.md#wf-rte-fork-finalization
          note: Fixed metadata consumers use these localized values.
        records: *id014
        note: Fixed metadata consumers use these localized values.
      - scope: Harness context, arbitrary fork product content and auxiliary retained payload forms
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-harness-turn
        - runtime.md#rt-rte-fork-worker
        - runtime.md#rt-rte-tool-governance
        - runtime.md#rt-rte-plugin-install
        - epistemic.md#epi-rte-checkpoint-restore
        note: Outer adapters and administrative checks do not expose all retained content or its later
          encoding.
      records:
      - memory.md#mem-obj-daily-note
      - memory.md#mem-obj-digest
      - runtime.md#rt-obj-session-state
      - memory.md#mem-obj-continuation-summary
      - memory.md#mem-rte-archive-replay
      - memory.md#mem-obj-history
      - memory.md#mem-obj-eviction-index
      - runtime.md#rt-obj-prompt-files
      - memory.md#mem-cmp-embedding-model
      - memory.md#mem-obj-adbpg-memory
      - memory.md#mem-rte-memory-retrieval
      - memory.md#mem-obj-inbox-event
      - workflow.md#wf-rte-fork-finalization
      - runtime.md#rt-rte-harness-turn
      - runtime.md#rt-rte-fork-worker
      - runtime.md#rt-rte-tool-governance
      - runtime.md#rt-rte-plugin-install
      - epistemic.md#epi-rte-checkpoint-restore
      note: Text, symbolic control material and cached dense vectors are split by operative part; opaque
        service and harness payloads prevent complete form coverage.
    lineage:
      assessment: partial
      units:
      - scope: ReMe conversation-derived daily/session notes
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id015
          - memory.md#mem-obj-daily-note
          - memory.md#mem-rte-trace-extraction
          note: Selected conversation batches feed extraction; initial workspace content remains separate.
        records: *id015
        note: Selected conversation batches feed extraction; initial workspace content remains separate.
      - scope: Scroll generated continuation summary
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id016
          - memory.md#mem-obj-continuation-summary
          - memory.md#mem-rte-scroll-retention
          note: Prior valid summary plus bounded archived turns and folded results feed a new durable
            summary.
        records: *id016
        note: Prior valid summary plus bounded archived turns and folded results feed a new durable summary.
      - scope: Scroll history written from live messages
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id017
          - memory.md#mem-obj-history
          note: Recorded session messages and tool results are trace-derived retained material, not thereby
            learned artifacts.
        records: *id017
        note: Recorded session messages and tool results are trace-derived retained material, not thereby
          learned artifacts.
      - scope: Session-JSON migration into Scroll history
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id018
          - memory.md#mem-obj-history
          note: Existing session serialization is imported through migration.
        records: *id018
        note: Existing session serialization is imported through migration.
      - scope: Eviction index, sequence maps and checkpoint bookkeeping
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id019
          - memory.md#mem-obj-eviction-index
          note: Code compiles recovery structure from retained message identities/spans.
        records: *id019
        note: Code compiles recovery structure from retained message identities/spans.
      - scope: Dream digest derivation
        assessment: partial
        findings:
        - value: other-compiled
          basis: claimed
          records:
          - memory.md#mem-rte-dream-maintenance
          note: Configured job extracts/merges units from retained notes, rather than directly replaying
            all sessions.
        records:
        - memory.md#mem-obj-digest
        - memory.md#mem-rte-dream-maintenance
        note: Derivation from daily/prior digest content is declared, but exact transformation and initial
          inputs are opaque.
      - scope: Daily Paper source and generated readings
        assessment: partial
        findings:
        - value: imported
          basis: claimed
          records:
          - epistemic.md#epi-obj-paper-brief
          note: External paper material supplies the resource input.
        - value: other-compiled
          basis: claimed
          records:
          - memory.md#mem-rte-paper-maintenance
          note: Configured analysis/digest stages derive readings and a brief from papers.
        records:
        - memory.md#mem-rte-paper-maintenance
        - epistemic.md#epi-obj-paper-brief
        note: External acquisition and generated readings are declared; actual artifacts and complete
          derivation are unavailable.
      - scope: Caller-supplied memory and workspace instruction replacements
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id020
          - memory.md#mem-rte-memory-edit
          - runtime.md#rt-rte-workspace-instruction
          note: Caller text enters the retained store; its original authorship and review are not established.
        records: *id020
        note: Caller text enters the retained store; its original authorship and review are not established.
      - scope: Explicitly composed user/model note edits
        assessment: known
        findings:
        - value: authored
          basis: afforded
          records: &id021
          - memory.md#mem-obj-daily-note
          note: User/model editing is afforded, not an observed authorship history for initialized files.
        records: *id021
        note: User/model editing is afforded, not an observed authorship history for initialized files.
      - scope: Inbox job-result projection
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id022
          - memory.md#mem-obj-inbox-event
          note: Code derives bounded notification text/metadata from job responses.
        records: *id022
        note: Code derives bounded notification text/metadata from job responses.
      - scope: Initial workspace contents, cached embedding provenance and ADBPG stored derivation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-daily-note
        - memory.md#mem-cmp-embedding-model
        - memory.md#mem-obj-adbpg-memory
        note: A known later extraction or cache route does not settle original content or remote embedding
          provenance.
      - scope: Native summary generation, harness-owned retained context and fork product provenance
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-session-state
        - runtime.md#rt-rte-harness-turn
        - runtime.md#rt-rte-fork-worker
        note: Dependency compaction and worker content paths are not fully inspected.
      records:
      - memory.md#mem-obj-daily-note
      - memory.md#mem-rte-trace-extraction
      - memory.md#mem-obj-continuation-summary
      - memory.md#mem-rte-scroll-retention
      - memory.md#mem-obj-history
      - memory.md#mem-obj-eviction-index
      - memory.md#mem-obj-digest
      - memory.md#mem-rte-dream-maintenance
      - memory.md#mem-rte-paper-maintenance
      - epistemic.md#epi-obj-paper-brief
      - memory.md#mem-rte-memory-edit
      - runtime.md#rt-rte-workspace-instruction
      - memory.md#mem-obj-inbox-event
      - memory.md#mem-cmp-embedding-model
      - memory.md#mem-obj-adbpg-memory
      - runtime.md#rt-obj-session-state
      - runtime.md#rt-rte-harness-turn
      - runtime.md#rt-rte-fork-worker
      note: Known derivation paths coexist with unknown initialization, caller provenance, embedding provenance
        and external-runtime state.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retained notes and raw context at later answering/proactive models
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id023
          - memory.md#mem-bap-retained-context
          - memory.md#mem-rte-memory-retrieval
          - memory.md#mem-rte-history-recall
          - memory.md#mem-rte-proactive-context
          note: Retrieved text, restored context and cleaned saved-session text supply evidence/background
            to later inference.
        records: *id023
        note: Retrieved text, restored context and cleaned saved-session text supply evidence/background
          to later inference.
      - scope: Edited workspace prose at native system-prompt composition
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id024
          - runtime.md#rt-bap-workspace-prompt
          note: Selected retained bodies supply standing directions; delivery does not prove compliance.
        records: *id024
        note: Selected retained bodies supply standing directions; delivery does not prove compliance.
      - scope: Session/tool traces at ReMe extraction and Scroll summary update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id025
          - memory.md#mem-rte-trace-extraction
          - memory.md#mem-rte-scroll-retention
          note: Retained experience feeds durable behavior-shaping notes or continuation summaries; this
            update force is distinct from downstream knowledge delivery.
        records: *id025
        note: Retained experience feeds durable behavior-shaping notes or continuation summaries; this
          update force is distinct from downstream knowledge delivery.
      - scope: Retained note snippets at lexical search and optional reranker
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id026
          - memory.md#mem-rte-memory-retrieval
          - epistemic.md#epi-rte-rerank-check
          note: Note text influences relative retrieval priority even when scoring code is fixed.
        records: *id026
        note: Note text influences relative retrieval priority even when scoring code is fixed.
      - scope: Scroll source ranges and recovery IDs at reconciliation/recall
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id027
          - memory.md#mem-obj-eviction-index
          - memory.md#mem-rte-scroll-retention
          - memory.md#mem-rte-history-recall
          note: Retained IDs/ranges select recovery scope and source-existence checks; missing provenance
            endpoints can withdraw summary reliance.
        - value: validation
          basis: wired
          records: *id027
          note: Retained IDs/ranges select recovery scope and source-existence checks; missing provenance
            endpoints can withdraw summary reliance.
        - value: enforcement
          basis: wired
          records: *id027
          note: Retained IDs/ranges select recovery scope and source-existence checks; missing provenance
            endpoints can withdraw summary reliance.
        records: *id027
        note: Retained IDs/ranges select recovery scope and source-existence checks; missing provenance
          endpoints can withdraw summary reliance.
      - scope: Pending-turn markers/snapshots at extraction batch selection
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id028
          - memory.md#mem-rte-trace-extraction
          - runtime.md#rt-obj-session-state
          note: Retained batching state selects the next extraction inputs, not their factual endorsement.
        records: *id028
        note: Retained batching state selects the next extraction inputs, not their factual endorsement.
      - scope: Fork registry status/head/scope at repeated finalization
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id029
          - workflow.md#wf-rte-fork-finalization
          note: Registry values select reuse/transition and enforce scope/active-state eligibility.
        - value: validation
          basis: wired
          records: *id029
          note: Registry values select reuse/transition and enforce scope/active-state eligibility.
        - value: enforcement
          basis: wired
          records: *id029
          note: Registry values select reuse/transition and enforce scope/active-state eligibility.
        records: *id029
        note: Registry values select reuse/transition and enforce scope/active-state eligibility.
      - scope: Inbox notification body at operator display
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id030
          - memory.md#mem-obj-inbox-event
          note: Display supplies information to the operator; no automatic model adoption is established.
        records: *id030
        note: Display supplies information to the operator; no automatic model adoption is established.
      - scope: Digest interests/catalog downstream effects, opaque ADBPG/harness payload consumers and
          auxiliary policy reuse
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-digest
        - memory.md#mem-obj-adbpg-memory
        - runtime.md#rt-rte-harness-turn
        - runtime.md#rt-rte-tool-governance
        note: Known retrieval does not resolve every stored part or consumer; configured interests are
          not proven proactive instructions.
      records:
      - memory.md#mem-bap-retained-context
      - memory.md#mem-rte-memory-retrieval
      - memory.md#mem-rte-history-recall
      - memory.md#mem-rte-proactive-context
      - runtime.md#rt-bap-workspace-prompt
      - memory.md#mem-rte-trace-extraction
      - memory.md#mem-rte-scroll-retention
      - epistemic.md#epi-rte-rerank-check
      - memory.md#mem-obj-eviction-index
      - runtime.md#rt-obj-session-state
      - workflow.md#wf-rte-fork-finalization
      - memory.md#mem-obj-inbox-event
      - memory.md#mem-obj-digest
      - memory.md#mem-obj-adbpg-memory
      - runtime.md#rt-rte-harness-turn
      - runtime.md#rt-rte-tool-governance
      note: Authority follows retained part and actual consumer. Supported update, retrieval, guidance
        and administrative paths do not establish all interests, remote-payload or auxiliary consumers.
    write_agency:
      assessment: partial
      units:
      - scope: ReMe extraction, dream and Daily Paper computational admissions
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id031
          - memory.md#mem-rte-trace-extraction
          - memory.md#mem-rte-dream-maintenance
          - memory.md#mem-rte-paper-maintenance
          note: Software/model selects generated content without per-content human veto; initiating a
            job or /memorize is not reviewing its output.
        records: *id031
        note: Software/model selects generated content without per-content human veto; initiating a job
          or /memorize is not reviewing its output.
      - scope: Scroll archival, index generation, summary replacement and quality gate
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id032
          - memory.md#mem-rte-scroll-retention
          - memory.md#mem-obj-continuation-summary
          - memory.md#mem-obj-eviction-index
          - memory.md#mem-obj-history
          note: Code/model admission includes deterministic summary rejection; no per-summary human approval
            is shown.
        records: *id032
        note: Code/model admission includes deterministic summary rejection; no per-summary human approval
          is shown.
      - scope: ADBPG user-message forwarding
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id033
          - memory.md#mem-rte-adbpg-retention
          note: Software chooses unseen user messages and schedules add; human authorship is not review
            of remote derived facts.
        records: *id033
        note: Software chooses unseen user messages and schedules add; human authorship is not review
          of remote derived facts.
      - scope: Normal native session snapshot admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id034
          - runtime.md#rt-rte-native-turn
          - runtime.md#rt-obj-session-state
          note: Post-response hooks serialize agent/mode state without a per-snapshot content decision.
        records: *id034
        note: Post-response hooks serialize agent/mode state without a per-snapshot content decision.
      - scope: Tool-text archive and inbox projection admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id035
          - memory.md#mem-rte-archive-replay
          - memory.md#mem-obj-inbox-event
          note: Threshold pruning and notification gates are computational admission mechanisms.
        records: *id035
        note: Threshold pruning and notification gates are computational admission mechanisms.
      - scope: Fork dirty-worktree fallback commit and registry transition
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id036
          - workflow.md#wf-rte-fork-finalization
          note: Finalizer stages/commits worker changes and records administrative state without a human
            content gate.
        records: *id036
        note: Finalizer stages/commits worker changes and records administrative state without a human
          content gate.
      - scope: Managed memory/workspace PUT, explicit debug replay and checkpoint replacement
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-memory-edit
        - runtime.md#rt-rte-workspace-instruction
        - memory.md#mem-rte-archive-replay
        - epistemic.md#epi-rte-checkpoint-restore
        note: Generic caller selection/replacement is inspected, but explicit human approval versus software
          admission is unresolved for these mechanisms.
      - scope: Initial retained contents, provider-owned thread admission and auxiliary writes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-daily-note
        - runtime.md#rt-rte-harness-turn
        - runtime.md#rt-rte-tool-governance
        - runtime.md#rt-rte-plugin-install
        - epistemic.md#epi-rte-checkpoint-restore
        note: Known subsequent automatic writes do not resolve all initialization or provider/auxiliary
          admissions.
      records:
      - memory.md#mem-rte-trace-extraction
      - memory.md#mem-rte-dream-maintenance
      - memory.md#mem-rte-paper-maintenance
      - memory.md#mem-rte-scroll-retention
      - memory.md#mem-obj-continuation-summary
      - memory.md#mem-obj-eviction-index
      - memory.md#mem-obj-history
      - memory.md#mem-rte-adbpg-retention
      - runtime.md#rt-rte-native-turn
      - runtime.md#rt-obj-session-state
      - memory.md#mem-rte-archive-replay
      - memory.md#mem-obj-inbox-event
      - workflow.md#wf-rte-fork-finalization
      - memory.md#mem-rte-memory-edit
      - runtime.md#rt-rte-workspace-instruction
      - epistemic.md#epi-rte-checkpoint-restore
      - memory.md#mem-obj-daily-note
      - runtime.md#rt-rte-harness-turn
      - runtime.md#rt-rte-tool-governance
      - runtime.md#rt-rte-plugin-install
      note: Automatic admission is supported on multiple routes. Generic API/command callers and initialization
        do not establish explicit human content decisions, so no blanket manual classification follows.
    curation_operations:
      assessment: partial
      units:
      - scope: Scroll bounded continuation generation and tool-output folding
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id037
          - memory.md#mem-rte-scroll-retention
          note: Compressing archived turns/results into task state reduces existing content. Summary defects
            would not by themselves establish synthesis.
        records: *id037
        note: Compressing archived turns/results into task state reduces existing content. Summary defects
          would not by themselves establish synthesis.
      - scope: Scroll summary replacement and stale-provenance withdrawal
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id038
          - memory.md#mem-rte-scroll-retention
          note: A new candidate replaces existing task state; missing source endpoints remove reliance
            on an older summary.
        - value: invalidate
          basis: wired
          records: *id038
          note: A new candidate replaces existing task state; missing source endpoints remove reliance
            on an older summary.
        records: *id038
        note: A new candidate replaces existing task state; missing source endpoints remove reliance on
          an older summary.
      - scope: History cutoff purge and old tool-artifact cleanup
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id039
          - memory.md#mem-obj-history
          - memory.md#mem-rte-archive-replay
          note: Retention cutoff/deletion forgets archived material. This does not establish complete
            erasure across stores.
        records: *id039
        note: Retention cutoff/deletion forgets archived material. This does not establish complete erasure
          across stores.
      - scope: ReMe conversation-fact extraction
        assessment: partial
        findings:
        - value: consolidate
          basis: claimed
          records:
          - memory.md#mem-obj-daily-note
          - memory.md#mem-rte-trace-extraction
          note: Recording selected conversation facts into a daily note reduces retained session content;
            adapter wiring alone does not inspect the transformation.
        records:
        - memory.md#mem-rte-trace-extraction
        - memory.md#mem-obj-daily-note
        note: The declared daily-fact transformation is consolidation, but external step implementation
          and additional semantic operations are unresolved.
      - scope: ReMe dream note maintenance
        assessment: partial
        findings:
        - value: consolidate
          basis: claimed
          records:
          - memory.md#mem-rte-dream-maintenance
          note: Declared extraction of merged units from daily/prior digest notes combines retained material.
        records:
        - memory.md#mem-rte-dream-maintenance
        note: Configured merging supports claimed consolidation; precise revise/delete/dedup/synthesis
          semantics remain external.
      - scope: Daily Paper semantic transformation and ADBPG remote extraction
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-paper-maintenance
        - memory.md#mem-rte-adbpg-retention
        note: Analysis/digest labels and opaque fact extraction do not settle controlled semantic operations.
      - scope: Managed replacement of existing memory Markdown
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id040
          - memory.md#mem-rte-memory-edit
          note: The inspected writer can revise an existing retained entry by replacement; no semantic
            quality or versioned undo follows.
        records: *id040
        note: The inspected writer can revise an existing retained entry by replacement; no semantic quality
          or versioned undo follows.
      - scope: Native dependency compaction, embedding-cache lifecycle and auxiliary maintenance
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-context-recovery
        - memory.md#mem-cmp-embedding-model
        - runtime.md#rt-rte-tool-governance
        - runtime.md#rt-rte-plugin-install
        - epistemic.md#epi-rte-checkpoint-restore
        note: Native summarization internals and auxiliary maintenance are unresolved. Cache rebuild/invalidation
          alone is not semantic memory invalidation.
      records:
      - memory.md#mem-rte-scroll-retention
      - memory.md#mem-obj-history
      - memory.md#mem-rte-archive-replay
      - memory.md#mem-rte-trace-extraction
      - memory.md#mem-obj-daily-note
      - memory.md#mem-rte-dream-maintenance
      - memory.md#mem-rte-paper-maintenance
      - memory.md#mem-rte-adbpg-retention
      - memory.md#mem-rte-memory-edit
      - runtime.md#rt-rte-context-recovery
      - memory.md#mem-cmp-embedding-model
      - runtime.md#rt-rte-tool-governance
      - runtime.md#rt-rte-plugin-install
      - epistemic.md#epi-rte-checkpoint-restore
      note: Scroll supplies implemented compression, replacement, withdrawal and retention removal. ReMe
        maintenance descriptions remain claimed operations; opaque branches cannot be upgraded by Scroll
        witnesses.
    read_back_direction:
      assessment: partial
      units:
      - scope: Foreground memory search and file expansion
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id041
          - memory.md#mem-rte-memory-retrieval
          note: Foreground query requests retained snippets; guidance affords subsequent file expansion.
            The return itself is not an additional push.
        records: *id041
        note: Foreground query requests retained snippets; guidance affords subsequent file expansion.
          The return itself is not an additional push.
      - scope: Structured history recall and explicit debug replay
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id042
          - memory.md#mem-rte-history-recall
          - memory.md#mem-rte-archive-replay
          note: Model/caller requests rows or a selected saved checkpoint for later context.
        records: *id042
        note: Model/caller requests rows or a selected saved checkpoint for later context.
      - scope: Automatic new-user-turn memory search
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id043
          - memory.md#mem-rte-memory-retrieval
          note: Middleware selects and injects retained snippets without a foreground tool request.
        records: *id043
        note: Middleware selects and injects retained snippets without a foreground tool request.
      - scope: Native session restore and Scroll background state
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id044
          - runtime.md#rt-rte-native-turn
          - memory.md#mem-rte-scroll-retention
          note: Code restores selected retained state and renders summary/index into later calls.
        records: *id044
        note: Code restores selected retained state and renders summary/index into later calls.
      - scope: Configured mutable workspace prompt contribution
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id045
          - runtime.md#rt-rte-workspace-instruction
          - runtime.md#rt-bap-workspace-prompt
          note: Builder supplies selected edited bodies at future construction without the answering model
            requesting them.
        records: *id045
        note: Builder supplies selected edited bodies at future construction without the answering model
          requesting them.
      - scope: Idle proactive saved-session context
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id046
          - memory.md#mem-rte-proactive-context
          note: Idle/cooldown/busy checks trigger automatic supply of cleaned retained session text to
            a separate agent.
        records: *id046
        note: Idle/cooldown/busy checks trigger automatic supply of cleaned retained session text to a
          separate agent.
      - scope: Forked saved-parent context delivery
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id047
          - runtime.md#rt-rte-fork-worker
          note: Code gives child a saved-session snapshot, not the latest evolving parent window.
        records: *id047
        note: Code gives child a saved-session snapshot, not the latest evolving parent window.
      - scope: Alternative harness resume
        assessment: partial
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-harness-turn
          note: Outer adapter initiates resume using the persisted thread mapping.
        records:
        - runtime.md#rt-rte-harness-turn
        note: QwenPaw selects saved thread identity for backend continuation; provider internal selectors/returns
          remain opaque.
      - scope: Interests/catalog, inbox subsequent model adoption and auxiliary retained-store consumers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-digest
        - memory.md#mem-obj-inbox-event
        - runtime.md#rt-rte-tool-governance
        - runtime.md#rt-rte-plugin-install
        - epistemic.md#epi-rte-checkpoint-restore
        note: Display does not establish automatic model adoption; complete auxiliary consumer routes
          are not inspected.
      records:
      - memory.md#mem-rte-memory-retrieval
      - memory.md#mem-rte-history-recall
      - memory.md#mem-rte-archive-replay
      - runtime.md#rt-rte-native-turn
      - memory.md#mem-rte-scroll-retention
      - runtime.md#rt-rte-workspace-instruction
      - runtime.md#rt-bap-workspace-prompt
      - memory.md#mem-rte-proactive-context
      - runtime.md#rt-rte-fork-worker
      - runtime.md#rt-rte-harness-turn
      - memory.md#mem-obj-digest
      - memory.md#mem-obj-inbox-event
      - runtime.md#rt-rte-tool-governance
      - runtime.md#rt-rte-plugin-install
      - epistemic.md#epi-rte-checkpoint-restore
      note: Explicit requested return and unsolicited context selection coexist. Outer harness resume
        is known without complete provider-owned read-back coverage.
    read_back_signal:
      assessment: partial
      units:
      - scope: Native session restore on later request
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id048
          - runtime.md#rt-obj-session-state
          - runtime.md#rt-rte-native-turn
          note: 'Trigger: native build. Selector: session/user/channel-derived checkpoint identity. Selected
            part: matching saved state.'
        records: *id048
        note: 'Trigger: native build. Selector: session/user/channel-derived checkpoint identity. Selected
          part: matching saved state.'
      - scope: Scroll background summary/index/tail availability
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id049
          - memory.md#mem-rte-scroll-retention
          note: 'Trigger: later model call. Selector: current retained checkpoint, validity and render
            budgets. Selected part: surviving summary/index/raw tail; no query-specific identity match
            is established for this rendering.'
        records: *id049
        note: 'Trigger: later model call. Selector: current retained checkpoint, validity and render budgets.
          Selected part: surviving summary/index/raw tail; no query-specific identity match is established
          for this rendering.'
      - scope: Configured mutable prompt-file contribution
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id050
          - runtime.md#rt-obj-prompt-files
          - runtime.md#rt-rte-workspace-instruction
          note: 'Trigger: agent build. Configured filenames actually match the selected retained bodies;
            empty/missing filtering is a separate availability condition.'
        records: *id050
        note: 'Trigger: agent build. Configured filenames actually match the selected retained bodies;
          empty/missing filtering is a separate availability condition.'
      - scope: New-user-turn automatic ReMe retrieval
        assessment: partial
        findings:
        - value: inferred-lexical
          basis: wired
          records:
          - memory.md#mem-rte-memory-retrieval
          - memory.md#mem-cmp-embedding-model
          note: Keyword query/index route is configured and remains available without embeddings.
        - value: inferred-embedding
          basis: wired
          records:
          - memory.md#mem-cmp-embedding-model
          - memory.md#mem-rte-memory-retrieval
          note: Configured embedding component and cached vectors support optional vector-based candidate
            access; no relevance benefit is claimed.
        - value: inferred-judgment
          basis: wired
          records:
          - memory.md#mem-cmp-reranker-model
          - epistemic.md#epi-rte-rerank-check
          - memory.md#mem-rte-memory-retrieval
          note: Optional reranker judges truncated retained snippets against the automatic query before
            capped delivery.
        records:
        - memory.md#mem-rte-memory-retrieval
        - memory.md#mem-cmp-embedding-model
        - memory.md#mem-cmp-reranker-model
        note: 'Trigger: new external user turn. Latest user text queries daily/digest corpus; keyword
          and optional embedding retrieval are configured, while complete dependency selection is opaque.'
      - scope: Automatic ADBPG local Markdown fallback
        assessment: known
        findings:
        - value: inferred-lexical
          basis: wired
          records: &id051
          - memory.md#mem-rte-memory-retrieval
          note: 'Trigger: automatic memory search. Selector: user query keywords scored against MEMORY.md/direct
            memory paragraphs. Selected part: capped snippets.'
        records: *id051
        note: 'Trigger: automatic memory search. Selector: user query keywords scored against MEMORY.md/direct
          memory paragraphs. Selected part: capped snippets.'
      - scope: ADBPG remote search selector
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-adbpg-memory
        - memory.md#mem-rte-memory-retrieval
        note: Query and score filtering are visible, but remote lexical/embedding/judgment candidate selection
          is not exposed.
      - scope: Idle proactive context selection
        assessment: partial
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-proactive-context
          note: Idle/availability, recency and volume filtering select saved-session context, not demonstrated
            semantic targeting.
        records:
        - memory.md#mem-rte-proactive-context
        note: 'Trigger: idle monitor. Recent-session filtering and 100-message/50,000-character budgets
          supply cleaned text; exact recency predicate is uninspected.'
      - scope: Fork saved-parent snapshot selection
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id052
          - runtime.md#rt-rte-fork-worker
          note: 'Trigger: fork dispatch. Parent session identity selects the saved session file copied
            to child; missing/unreadable file may yield empty state.'
        records: *id052
        note: 'Trigger: fork dispatch. Parent session identity selects the saved session file copied to
          child; missing/unreadable file may yield empty state.'
      - scope: Harness saved-thread mapping
        assessment: partial
        findings:
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-rte-harness-turn
          note: Persisted session-to-thread mapping selects a retained thread to resume.
        records:
        - runtime.md#rt-rte-harness-turn
        note: 'Trigger: later backend turn. Outer mapping matches session to thread, but SDK-internal
          context selection is opaque.'
      - scope: Digest metadata and auxiliary push alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-digest
        - runtime.md#rt-rte-tool-governance
        - runtime.md#rt-rte-plugin-install
        - epistemic.md#epi-rte-checkpoint-restore
        note: Missing consumer/selector facts prevent inapplicability or a complete signal union.
      records:
      - runtime.md#rt-obj-session-state
      - runtime.md#rt-rte-native-turn
      - memory.md#mem-rte-scroll-retention
      - runtime.md#rt-obj-prompt-files
      - runtime.md#rt-rte-workspace-instruction
      - memory.md#mem-rte-memory-retrieval
      - memory.md#mem-cmp-embedding-model
      - memory.md#mem-cmp-reranker-model
      - memory.md#mem-obj-adbpg-memory
      - memory.md#mem-rte-proactive-context
      - runtime.md#rt-rte-fork-worker
      - runtime.md#rt-rte-harness-turn
      - memory.md#mem-obj-digest
      - runtime.md#rt-rte-tool-governance
      - runtime.md#rt-rte-plugin-install
      - epistemic.md#epi-rte-checkpoint-restore
      note: Signals apply only to automatic selection operations. Explicit search/recall returns stay
        pull; opaque ReMe/provider selectors and incomplete proactive predicates prevent complete signal
        coverage.
    trace_learning:
      assessment: partial
      units:
      - scope: Conversation batches to ReMe notes to later search/model context
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id053
          - memory.md#mem-rte-trace-extraction
          - memory.md#mem-rte-memory-retrieval
          note: Automatic trace-fed generated notes enter a wired durable behavior-shaping route; backend
            outputs and benefit are unobserved.
        records: *id053
        note: Automatic trace-fed generated notes enter a wired durable behavior-shaping route; backend
          outputs and benefit are unobserved.
      - scope: Archived turns/results to Scroll continuation summary to later context
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id054
          - memory.md#mem-rte-scroll-retention
          - memory.md#mem-obj-continuation-summary
          note: Automatic model summary is checkpointed and later rendered; reshaping qualifies without
            new claims or measured improvement.
        records: *id054
        note: Automatic model summary is checkpointed and later rendered; reshaping qualifies without
          new claims or measured improvement.
      - scope: ADBPG remote trace transformation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-adbpg-retention
        - memory.md#mem-obj-adbpg-memory
        note: Automatic user-message forwarding and later text consumption are wired, but remote retained
          artifact/transformation semantics are opaque; no local negative follows.
      - scope: Dream derived-note maintenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-dream-maintenance
        - memory.md#mem-obj-digest
        note: Retained-note input and future search are declared, but exact trace lineage and backend
          update semantics remain unresolved.
      - scope: Native compressed summary including debug replay alternative
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-context-recovery
        - memory.md#mem-rte-archive-replay
        - runtime.md#rt-obj-session-state
        note: Summary persistence/replay is identified, but dependency-owned generation and full trace-fed
          admission chain are not inspected.
      - scope: Daily Paper resource-fed route
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-paper-maintenance
        note: Original inputs are external paper resources, not established activity traces from agent
          work; resource analysis alone is not trace learning.
      - scope: Raw history capture and unchanged replay alone
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-obj-history
        - memory.md#mem-rte-history-recall
        - memory.md#mem-rte-archive-replay
        note: These units record/recover raw evidence; their separate derived-summary route is classified
          above. Raw logging alone is not a qualifying derived update.
      - scope: Harness-owned updates, fork products, initialization and auxiliary adaptation
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-harness-turn
        - runtime.md#rt-rte-fork-worker
        - runtime.md#rt-rte-tool-governance
        - runtime.md#rt-rte-plugin-install
        - epistemic.md#epi-rte-checkpoint-restore
        note: Records do not expose every automatic trace-fed artifact or later adaptation consumer.
      records:
      - memory.md#mem-rte-trace-extraction
      - memory.md#mem-rte-memory-retrieval
      - memory.md#mem-rte-scroll-retention
      - memory.md#mem-obj-continuation-summary
      - memory.md#mem-rte-adbpg-retention
      - memory.md#mem-obj-adbpg-memory
      - memory.md#mem-rte-dream-maintenance
      - memory.md#mem-obj-digest
      - runtime.md#rt-rte-context-recovery
      - memory.md#mem-rte-archive-replay
      - runtime.md#rt-obj-session-state
      - memory.md#mem-rte-paper-maintenance
      - memory.md#mem-obj-history
      - memory.md#mem-rte-history-recall
      - runtime.md#rt-rte-harness-turn
      - runtime.md#rt-rte-fork-worker
      - runtime.md#rt-rte-tool-governance
      - runtime.md#rt-rte-plugin-install
      - epistemic.md#epi-rte-checkpoint-restore
      note: Automatic session-derived note and continuation-summary writes have later consumers. This
        is architectural trace learning, not demonstrated improvement; native/remote/auxiliary alternatives
        remain unresolved.
    trace_source:
      assessment: partial
      units:
      - scope: ReMe auto-memory conversation batches
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id055
          - memory.md#mem-rte-trace-extraction
          note: Original inputs include user/assistant conversational turns and tool content; tagged synthetic
            recall is removed. Manual initiation does not change source origin.
        - value: tool-traces
          basis: wired
          records: *id055
          note: Original inputs include user/assistant conversational turns and tool content; tagged synthetic
            recall is removed. Manual initiation does not change source origin.
        records: *id055
        note: Original inputs include user/assistant conversational turns and tool content; tagged synthetic
          recall is removed. Manual initiation does not change source origin.
      - scope: Scroll continuation-summary archived turns and folded results
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id056
          - memory.md#mem-obj-continuation-summary
          - memory.md#mem-rte-scroll-retention
          note: Bounded archived conversational turns and recoverable tool results feed durable task-state
            generation.
        - value: tool-traces
          basis: wired
          records: *id056
          note: Bounded archived conversational turns and recoverable tool results feed durable task-state
            generation.
        records: *id056
        note: Bounded archived conversational turns and recoverable tool results feed durable task-state
          generation.
      - scope: ADBPG outbound user-turn input
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-rte-adbpg-retention
          note: User-role conversational messages are recorded session content, not event-streams merely
            because sent through REST.
        records:
        - memory.md#mem-rte-adbpg-retention
        - memory.md#mem-obj-adbpg-memory
        note: Original forwarded content is known, but the qualifying remote update and any other server
          inputs remain opaque.
      - scope: Dream original-input inheritance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-dream-maintenance
        - memory.md#mem-obj-digest
        note: Daily/prior digest notes are inputs; missing complete origin and transformation facts prevent
          a complete qualifying trace-source classification.
      - scope: Native summary, harness-owned and auxiliary trace-fed writes
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-context-recovery
        - runtime.md#rt-rte-harness-turn
        - runtime.md#rt-rte-tool-governance
        - runtime.md#rt-rte-plugin-install
        - epistemic.md#epi-rte-checkpoint-restore
        note: No complete original-input inventory for these unresolved updates.
      - scope: Daily Paper and raw recovery-only units
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-paper-maintenance
        - memory.md#mem-obj-history
        - memory.md#mem-rte-archive-replay
        note: Paper resources are not established activity traces; raw storage/replay alone is not qualifying
          trace learning. Separate generated continuation routes remain included above.
      records:
      - memory.md#mem-rte-trace-extraction
      - memory.md#mem-obj-continuation-summary
      - memory.md#mem-rte-scroll-retention
      - memory.md#mem-rte-adbpg-retention
      - memory.md#mem-obj-adbpg-memory
      - memory.md#mem-rte-dream-maintenance
      - memory.md#mem-obj-digest
      - runtime.md#rt-rte-context-recovery
      - runtime.md#rt-rte-harness-turn
      - runtime.md#rt-rte-tool-governance
      - runtime.md#rt-rte-plugin-install
      - epistemic.md#epi-rte-checkpoint-restore
      - memory.md#mem-rte-paper-maintenance
      - memory.md#mem-obj-history
      - memory.md#mem-rte-archive-replay
      note: Original session and tool content is supported for the qualifying ReMe and Scroll writes.
        Opaque remote/native/auxiliary updates prevent a complete source inventory; ordinary wrappers
        do not add event-stream sources.
---

# QwenPaw memory profile

## Comparison rationale

All ten axes are partial. Local witnesses establish real classifications, but the accepted records do not supply a complete inventory of provider-owned memory, initial contents or auxiliary stores. Unread available implementations and unavailable external internals are different limits. No absence record supports a system-wide negative, and no run or causal evidence upgrades a wired route to observed operation or benefit.

The profile follows the reconciliation's identity amendments. It cites canonical [MEM-RTE-trace-extraction](memory.md#mem-rte-trace-extraction), [MEM-RTE-dream-maintenance](memory.md#mem-rte-dream-maintenance), [MEM-RTE-paper-maintenance](memory.md#mem-rte-paper-maintenance), [MEM-RTE-memory-edit](memory.md#mem-rte-memory-edit) and [MEM-CMP-reranker-model](memory.md#mem-cmp-reranker-model), rather than their superseded epistemic declarations. Their epistemic qualifications survive: dispatch/completion is not factual acceptance, dream completion may follow a null response, and backend semantic operations remain opaque. Non-superseded relevance subfunctions remain separate witnesses.

The session container is not replaced by its summary/index parts. [RT-OBJ-session-state](runtime.md#rt-obj-session-state), [MEM-OBJ-continuation-summary](memory.md#mem-obj-continuation-summary) and [MEM-OBJ-eviction-index](memory.md#mem-obj-eviction-index) classify different consumed parts. The continuation summary supplies context; its source ranges and recovery map additionally route and constrain recovery. A user-role background message is not automatically a standing instruction. Actual system-prompt authority instead follows [RT-BAP-workspace-prompt](runtime.md#rt-bap-workspace-prompt).

Trace learning is positive for automatic derived notes and continuation state with later consumers, independently of semantic novelty, parameter updates or successful improvement. Retained experience has learning force at the update consumer, while produced text has knowledge force at later task consumers. [MEM-RTE-scroll-retention](memory.md#mem-rte-scroll-retention) supports implemented consolidation, replacement and provenance-based withdrawal. ReMe's described fact extraction and dream merging retain claimed curation findings, not an upgraded wired semantic transformation. Neither opaque analysis nor a potentially inaccurate summary establishes synthesis.

Retrieval direction follows operations, not delivery mechanics. [MEM-RTE-memory-retrieval](memory.md#mem-rte-memory-retrieval) supports requested pull and middleware push. Keyword/vector access and optional judgment-based reranking concern automatic query selection; the explicit search return does not become another push. [MEM-RTE-history-recall](memory.md#mem-rte-history-recall) remains pull even when parameters are IDs. Conversely session restore and configured prompt contribution use actual identity matches selecting delivered retained parts. Availability and summary-render budgets are coarse filtering, not semantic targeting. Proactive selection remains partial because its exact recent-session predicate is unresolved.

[WF-RTE-fork-finalization](workflow.md#wf-rte-fork-finalization) supports automatic Git/registry admission and administrative validation/enforcement. It does not establish product correctness or learning from the product. The workflow's saved-parent-file inheritance narrows fork context selection: it may be stale or empty. External harness resume establishes an outer identity-selection path, not complete provider memory semantics. Neither project retention nor model inference admits all runtime storage into the comparison boundary.

No additional source files were read. Classifications use only the supplied accepted records and their retained evidence. Unknown admission control for generic caller replacements is preserved rather than converted into manual agency; starting extraction or restoration is not per-content human approval. Remote returned text is classified separately from opaque stored payloads, and inbox display text never substitutes for the underlying modified memory artifact.
