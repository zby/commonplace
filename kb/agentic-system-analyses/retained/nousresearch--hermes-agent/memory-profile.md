---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Hermes Agent memory comparison: notes/profile, skills, retained sessions and handoffs, provider
  alternatives and unresolved context routes at the frozen commit.'
run-id: AAS-2026-10-14-hermes-agent-bfb4bdc54d37-01
source-identity: https://github.com/nousresearch/hermes-agent
reviewed-boundary: 0e427d788d253630d38a3a51cd76849e73cd6925
memory-comparison:
  version: 2
  scope: 'Retained material accumulated or changed through use: built-in notes/profile; revised skill
    packages and access/lifecycle metadata; pending proposals; session traces, derived handoffs and checkpoint
    sidecars; optional provider state/recall; successful child-output spills; saved goal feedback/control;
    and named unresolved editable context-file, todo, context-engine, micro-compaction, native-thread
    and async-completion alternatives. Static bundled instructions/skills before use-derived change, ordinary
    current-run tool-call state, arbitrary application file effects, model-provider weights, plugin implementation
    installation, Python kernels and general command-approval policy are excluded from this compared retained-context
    boundary. External provider/native internals remain included as opaque operative alternatives, not
    attributed implementation.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Built-in notes/profile, retained skill trees and pending proposals
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-memory
          - memory.md#mem-obj-user
          - memory.md#mem-obj-skill-package
          - memory.md#mem-obj-pending-write
          note: UTF-8/JSON files retain content; live stores, prompt snapshots and index caches hold process
            copies. Plugin-registry skill alternatives are separately unresolved.
        - value: in-memory
          basis: wired
          records: *id001
          note: UTF-8/JSON files retain content; live stores, prompt snapshots and index caches hold process
            copies. Plugin-registry skill alternatives are separately unresolved.
        records: *id001
        note: UTF-8/JSON files retain content; live stores, prompt snapshots and index caches hold process
          copies. Plugin-registry skill alternatives are separately unresolved.
      - scope: Session text, local summaries and Responses checkpoint sidecars
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records: &id002
          - memory.md#mem-obj-session-content
          - memory.md#mem-obj-native-checkpoint
          - memory.md#mem-rte-local-compaction
          note: Serialized session rows and working message copies retain distinct raw, derived and opaque
            parts; opacity does not obscure the local row substrate.
        - value: in-memory
          basis: wired
          records: *id002
          note: Serialized session rows and working message copies retain distinct raw, derived and opaque
            parts; opacity does not obscure the local row substrate.
        records: *id002
        note: Serialized session rows and working message copies retain distinct raw, derived and opaque
          parts; opacity does not obscure the local row substrate.
      - scope: Provider-side RetainDB queue and named external memory objects
        assessment: partial
        findings:
        - value: sqlite
          basis: wired
          records: &id003
          - memory.md#mem-obj-provider-state
          - memory.md#mem-rte-provider-cycle
          note: The queue is local SQLite; remote messages/facts/files/profile are service-owned objects.
            Their underlying databases or embeddings are not established.
        - value: service-object
          basis: wired
          records: *id003
          note: The queue is local SQLite; remote messages/facts/files/profile are service-owned objects.
            Their underlying databases or embeddings are not established.
        records: *id003
        note: The queue is local SQLite; remote messages/facts/files/profile are service-owned objects.
          Their underlying databases or embeddings are not established.
      - scope: ByteRover persistent tree/cloud internals and optional provider implementations
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-provider-state
        - memory.md#mem-rte-provider-cycle
        note: CLI ownership and a knowledge-tree display do not identify the underlying substrate.
      - scope: Successful delegated-answer spills
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id004
          - workflow.md#wf-rte-summary-return
          note: Full child output is written to cache files when spill succeeds, separately from its returned
            head/tail.
        records: *id004
        note: Full child output is written to cache files when spill succeeds, separately from its returned
          head/tail.
      - scope: Saved goal verdict/control state
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-obj-goal-verdict
        - epistemic.md#epi-rte-goal-disposition
        note: Manager saving is wired, but these records do not identify its durable substrate.
      - scope: Plugin skill payloads, editable context files, todo rehydration, external context engines,
          app-server native context and durable async completions
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-skill-package
        - memory.md#mem-rte-local-compaction
        - runtime.md#rt-rte-codex-turn
        - runtime.md#rt-rte-child-delegation
        note: Named included alternatives have no complete retained-object substrate account in the accepted
          records. Spill reload, frontend retention and rolling-summary lifecycle are also incomplete.
      records:
      - memory.md#mem-obj-memory
      - memory.md#mem-obj-user
      - memory.md#mem-obj-skill-package
      - memory.md#mem-obj-pending-write
      - memory.md#mem-obj-session-content
      - memory.md#mem-obj-native-checkpoint
      - memory.md#mem-rte-local-compaction
      - memory.md#mem-obj-provider-state
      - memory.md#mem-rte-provider-cycle
      - workflow.md#wf-rte-summary-return
      - epistemic.md#epi-obj-goal-verdict
      - epistemic.md#epi-rte-goal-disposition
      - runtime.md#rt-rte-codex-turn
      - runtime.md#rt-rte-child-delegation
      note: Files, SQLite, process copies and service objects are positive witnesses, not a full inventory
        of the partial-loop boundary. Provider and alternate context surfaces prevent complete substrate
        coverage.
    representational_form:
      assessment: partial
      units:
      - scope: Notes/profile and skill prose at model-input consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id005
          - memory.md#mem-obj-memory
          - memory.md#mem-obj-user
          - memory.md#mem-obj-skill-package
          - memory.md#mem-bap-retained-text
          note: Descriptions, preferences, procedures and references receive force through model interpretation;
            this excludes skill scripts and lookup metadata.
        records: *id005
        note: Descriptions, preferences, procedures and references receive force through model interpretation;
          this excludes skill scripts and lookup metadata.
      - scope: Skill lookup/platform/dependency metadata and scripts; pending replay kwargs; session access
          envelopes
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id006
          - memory.md#mem-obj-skill-package
          - memory.md#mem-obj-pending-write
          - memory.md#mem-obj-session-content
          note: Fixed-rule fields and executable script syntax are symbolic; script execution envelopes
            remain incompletely traced, not parametric.
        records: *id006
        note: Fixed-rule fields and executable script syntax are symbolic; script execution envelopes
          remain incompletely traced, not parametric.
      - scope: Raw conversation text, readable local handoffs and provider-returned prose
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id007
          - memory.md#mem-obj-session-content
          - memory.md#mem-rte-local-compaction
          - memory.md#mem-obj-provider-state
          - epistemic.md#epi-rte-recall-consume
          note: These readable parts are model input. They do not reveal opaque service representations
            or encrypted checkpoint contents.
        records: *id007
        note: These readable parts are model input. They do not reveal opaque service representations
          or encrypted checkpoint contents.
      - scope: Checkpoint type/position and provider queue/API envelopes
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id008
          - memory.md#mem-obj-native-checkpoint
          - memory.md#mem-obj-provider-state
          note: Replay positions/type tags and queue/API fields have fixed-rule consumers; the encrypted
            payload is a separate part.
        records: *id008
        note: Replay positions/type tags and queue/API fields have fixed-rule consumers; the encrypted
          payload is a separate part.
      - scope: Encrypted checkpoint payload and provider internal profiles/embeddings
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-native-checkpoint
        - memory.md#mem-obj-provider-state
        note: Encryption and a prose display identify neither natural-language nor parametric form of
          the operative opaque material.
      - scope: Saved goal verdict/status and reason/output parts
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id009
          - epistemic.md#epi-obj-goal-verdict
          - epistemic.md#epi-rte-goal-disposition
          note: Verdict/status drive manager rules; reason and bounded execution/response evidence are
            text, not a truth certificate.
        - value: natural-language
          basis: wired
          records: *id009
          note: Verdict/status drive manager rules; reason and bounded execution/response evidence are
            text, not a truth certificate.
        records: *id009
        note: Verdict/status drive manager rules; reason and bounded execution/response evidence are text,
          not a truth certificate.
      - scope: Spilled child answer content
        assessment: not-determinable
        findings: []
        records:
        - workflow.md#wf-rte-summary-return
        note: Arbitrary natural-language or JSON-text output may be retained; the record does not resolve
          every actual payload consumption path.
      - scope: Plugin/preprocessed skills, context engines, todo/context-file payloads and app-server
          native context
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-skill-cycle
        - memory.md#mem-rte-local-compaction
        - runtime.md#rt-rte-codex-turn
        note: Their material transformations and consumed payloads remain incompletely recorded. Configured
          inference weights are not accumulated memory and are excluded.
      records:
      - memory.md#mem-obj-memory
      - memory.md#mem-obj-user
      - memory.md#mem-obj-skill-package
      - memory.md#mem-bap-retained-text
      - memory.md#mem-obj-pending-write
      - memory.md#mem-obj-session-content
      - memory.md#mem-rte-local-compaction
      - memory.md#mem-obj-provider-state
      - epistemic.md#epi-rte-recall-consume
      - memory.md#mem-obj-native-checkpoint
      - epistemic.md#epi-obj-goal-verdict
      - epistemic.md#epi-rte-goal-disposition
      - workflow.md#wf-rte-summary-return
      - memory.md#mem-rte-skill-cycle
      - runtime.md#rt-rte-codex-turn
      note: Readable text and symbolic controls coexist. No parametric memory finding is inferred from
        provider names, encryption or the numerical inference component; unresolved payloads remain included.
    lineage:
      assessment: partial
      units:
      - scope: Model-authored notes and skill writes; review-derived lessons
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id010
          - memory.md#mem-rte-notes-cycle
          - memory.md#mem-rte-skill-cycle
          - memory.md#mem-rte-review-write
          note: Foreground models author/revise prose; automatic review extracts lessons from mixed completed-turn
            history. These are supported paths, not initial-file provenance.
        - value: trace-extracted
          basis: wired
          records: *id010
          note: Foreground models author/revise prose; automatic review extracts lessons from mixed completed-turn
            history. These are supported paths, not initial-file provenance.
        records: *id010
        note: Foreground models author/revise prose; automatic review extracts lessons from mixed completed-turn
          history. These are supported paths, not initial-file provenance.
      - scope: Model summaries of retained conversation
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id011
          - memory.md#mem-rte-local-compaction
          - epistemic.md#epi-obj-summary-content
          note: Selected recorded conversation feeds the summary; semantic fidelity and individual claim
            novelty are not established.
        records: *id011
        note: Selected recorded conversation feeds the summary; semantic fidelity and individual claim
          novelty are not established.
      - scope: Deterministic handoffs and skill index/access structures
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id012
          - memory.md#mem-rte-local-compaction
          - memory.md#mem-obj-skill-package
          note: Code assembles fallback handoffs and descriptions/signatures into access structures; this
            is not evidence of novel semantic claims.
        records: *id012
        note: Code assembles fallback handoffs and descriptions/signatures into access structures; this
          is not evidence of novel semantic claims.
      - scope: Externally sourced recall and installed/authored skill alternatives
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records: &id013
          - memory.md#mem-rte-provider-cycle
          - epistemic.md#epi-rte-recall-consume
          - memory.md#mem-obj-skill-package
          note: Provider-return prose enters model context through the adapter.
        - value: imported
          basis: afforded
          records: *id013
          note: Hub/external skill trees supply an acquisition alternative; full hub admission is not
            traced.
        records: *id013
        note: Import is a known route; original fact, embedding and initial package provenance remain
          unresolved.
      - scope: Native checkpoint derivation from earlier context
        assessment: partial
        findings:
        - value: trace-extracted
          basis: wired
          records: &id014
          - memory.md#mem-obj-native-checkpoint
          note: The checkpoint follows earlier context through a provider-derived route; exact server
            transformation and complete original input remain opaque.
        records: *id014
        note: The checkpoint follows earlier context through a provider-derived route; exact server transformation
          and complete original input remain opaque.
      - scope: Child returned head/tail projection and full-output spill
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records: &id015
          - workflow.md#wf-rte-summary-return
          note: Fixed slicing produces the returned projection and full output is copied into a cache
            artifact; this does not establish initial child-output provenance.
        records: *id015
        note: Fixed slicing produces the returned projection and full output is copied into a cache artifact;
          this does not establish initial child-output provenance.
      - scope: Goal verdict derivation
        assessment: partial
        findings:
        - value: trace-extracted
          basis: wired
          records: &id016
          - epistemic.md#epi-obj-goal-verdict
          - epistemic.md#epi-rte-goal-check
          - epistemic.md#epi-rte-goal-disposition
          note: Recorded response and gate execution feedback feed a verdict/reason subsequently saved
            for manager use; configuration/goal authorship is unresolved.
        records: *id016
        note: Recorded response and gate execution feedback feed a verdict/reason subsequently saved for
          manager use; configuration/goal authorship is unresolved.
      - scope: Initial notes/profile/skills/provider content, UI input provenance and opaque provider
          derivation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory
        - memory.md#mem-obj-skill-package
        - memory.md#mem-obj-provider-state
        - epistemic.md#epi-rte-memory-gate
        note: Existing content and generic caller identity do not establish authored versus imported origins;
          known later writes do not settle them.
      - scope: Editable context files, todo/context engines, micro summaries and async/native thread state
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-local-compaction
        - runtime.md#rt-rte-child-delegation
        - runtime.md#rt-rte-codex-turn
        note: These included derivation alternatives lack a complete accepted account.
      records:
      - memory.md#mem-rte-notes-cycle
      - memory.md#mem-rte-skill-cycle
      - memory.md#mem-rte-review-write
      - memory.md#mem-rte-local-compaction
      - epistemic.md#epi-obj-summary-content
      - memory.md#mem-obj-skill-package
      - memory.md#mem-rte-provider-cycle
      - epistemic.md#epi-rte-recall-consume
      - memory.md#mem-obj-native-checkpoint
      - workflow.md#wf-rte-summary-return
      - epistemic.md#epi-obj-goal-verdict
      - epistemic.md#epi-rte-goal-check
      - epistemic.md#epi-rte-goal-disposition
      - memory.md#mem-obj-memory
      - memory.md#mem-obj-provider-state
      - epistemic.md#epi-rte-memory-gate
      - runtime.md#rt-rte-child-delegation
      - runtime.md#rt-rte-codex-turn
      note: Known derivation routes coexist with unknown initial and provider provenance. Authored and
        trace-extracted describe distinct supported paths, not an exhaustive origin assignment.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retained note facts, recalled prose, history and readable handoffs at foreground model
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id017
          - memory.md#mem-rte-notes-cycle
          - epistemic.md#epi-rte-recall-consume
          - memory.md#mem-rte-local-compaction
          - memory.md#mem-rte-session-recall
          note: These parts supply reference/context at later inference. Delivery does not establish truth,
            compliance or benefit.
        records: *id017
        note: These parts supply reference/context at later inference. Delivery does not establish truth,
          compliance or benefit.
      - scope: Retained preferences and skill procedures at foreground model
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id018
          - memory.md#mem-obj-user
          - memory.md#mem-rte-skill-cycle
          - memory.md#mem-bap-retained-text
          note: Preferences and procedures provide standing directions through prompt blocks or skill
            tool results, not executable enforcement.
        records: *id018
        note: Preferences and procedures provide standing directions through prompt blocks or skill tool
          results, not executable enforcement.
      - scope: Retained conversations at review and summary update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id019
          - memory.md#mem-rte-review-write
          - memory.md#mem-rte-local-compaction
          note: Trace content feeds automatic durable lessons or continuation handoffs. This authority
            concerns the update consumer, separate from downstream knowledge/instruction.
        records: *id019
        note: Trace content feeds automatic durable lessons or continuation handoffs. This authority concerns
          the update consumer, separate from downstream knowledge/instruction.
      - scope: Retained session text and metadata at search ranking code
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id020
          - memory.md#mem-rte-session-recall
          note: FTS text, lineage and cron demotion influence relative retrieval priority; no learned
            ranker is implied.
        records: *id020
        note: FTS text, lineage and cron demotion influence relative retrieval priority; no learned ranker
          is implied.
      - scope: Skill lifecycle/provenance/read-mark/suppression metadata and pinned pending targets at
          admission/load code
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id021
          - memory.md#mem-rte-skill-curation
          - epistemic.md#epi-rte-skill-guard
          - memory.md#mem-rte-pending-review
          note: Protection/read marks and content pins constrain admissible mutations; archived/suppressed
            state constrains later catalog delivery. These retained controls differ from static scanner
            code.
        - value: enforcement
          basis: wired
          records: *id021
          note: Protection/read marks and content pins constrain admissible mutations; archived/suppressed
            state constrains later catalog delivery. These retained controls differ from static scanner
            code.
        records: *id021
        note: Protection/read marks and content pins constrain admissible mutations; archived/suppressed
          state constrains later catalog delivery. These retained controls differ from static scanner
          code.
      - scope: Session active/compacted flags, checkpoint positions and saved goal status at runtime consumers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id022
          - memory.md#mem-obj-session-content
          - memory.md#mem-obj-native-checkpoint
          - epistemic.md#epi-rte-goal-disposition
          note: Flags/positions select live projections or replay windows; saved goal state selects continuation,
            park or stop. Their role is operational routing, not factual endorsement.
        records: *id022
        note: Flags/positions select live projections or replay windows; saved goal state selects continuation,
          park or stop. Their role is operational routing, not factual endorsement.
      - scope: Saved goal failure/reason text at subsequent repair model
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id023
          - epistemic.md#epi-rte-goal-disposition
          note: Failure evidence is turned into a continuation/repair prompt delivered to a later model
            turn; successful repair is unobserved.
        records: *id023
        note: Failure evidence is turned into a continuation/repair prompt delivered to a later model
          turn; successful repair is unobserved.
      - scope: Spilled output at a later requesting parent
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records: &id024
          - workflow.md#wf-rte-summary-return
          note: The footer affords paging full retained output with read_file; actual reload is not established.
        records: *id024
        note: The footer affords paging full retained output with read_file; actual reload is not established.
      - scope: Opaque checkpoints/provider internals, skill script execution, UI/context-engine/todo and
          async consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-native-checkpoint
        - memory.md#mem-obj-provider-state
        - memory.md#mem-obj-skill-package
        - memory.md#mem-rte-local-compaction
        - runtime.md#rt-rte-child-delegation
        note: Readable displays do not classify opaque consumers. Script support files may execute but
          full downstream effect is not established; alternate consumers remain incomplete.
      records:
      - memory.md#mem-rte-notes-cycle
      - epistemic.md#epi-rte-recall-consume
      - memory.md#mem-rte-local-compaction
      - memory.md#mem-rte-session-recall
      - memory.md#mem-obj-user
      - memory.md#mem-rte-skill-cycle
      - memory.md#mem-bap-retained-text
      - memory.md#mem-rte-review-write
      - memory.md#mem-rte-skill-curation
      - epistemic.md#epi-rte-skill-guard
      - memory.md#mem-rte-pending-review
      - memory.md#mem-obj-session-content
      - memory.md#mem-obj-native-checkpoint
      - epistemic.md#epi-rte-goal-disposition
      - workflow.md#wf-rte-summary-return
      - memory.md#mem-obj-provider-state
      - memory.md#mem-obj-skill-package
      - runtime.md#rt-rte-child-delegation
      note: Knowledge, instruction, learning, ranking, validation, enforcement and routing have local
        consumer warrants. Static guards and shipped instructions are not reclassified as accumulated
        memory; opaque and alternate consumers prevent complete coverage.
    write_agency:
      assessment: partial
      units:
      - scope: Ungated foreground memory/skill admission and review additions
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id025
          - memory.md#mem-rte-notes-cycle
          - memory.md#mem-rte-skill-cycle
          - memory.md#mem-rte-review-write
          note: Software/model admission can commit content without an explicit human decision about each
            retained item. Starting a request or choosing configuration is not manual admission.
        records: *id025
        note: Software/model admission can commit content without an explicit human decision about each
          retained item. Starting a request or choosing configuration is not manual admission.
      - scope: Per-content pending approval and attended inline approval
        assessment: known
        findings:
        - value: manual
          basis: wired
          records: &id026
          - memory.md#mem-rte-pending-review
          - memory.md#mem-rte-notes-cycle
          note: An explicit human-facing approve/apply decision admits a selected payload; reject leaves
            it unadopted. Staging alone is automatic proposal retention.
        records: *id026
        note: An explicit human-facing approve/apply decision admits a selected payload; reject leaves
          it unadopted. Staging alone is automatic proposal retention.
      - scope: Pending proposal staging
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id027
          - memory.md#mem-rte-pending-review
          note: Software stages the replay payload and removes it after successful apply; no human decision
            is required to create the proposal.
        records: *id027
        note: Software stages the replay payload and removes it after successful apply; no human decision
          is required to create the proposal.
      - scope: Compaction commit, deterministic aging/archive and provider queue/adapter ingress
        assessment: partial
        findings:
        - value: automatic
          basis: wired
          records: &id028
          - memory.md#mem-rte-local-compaction
          - memory.md#mem-rte-skill-curation
          - memory.md#mem-rte-provider-cycle
          note: Code admits summaries, lifecycle changes and trace ingress; manual focus or enabling extraction
            is not approval of each result. Remote derived admission remains unresolved.
        records: *id028
        note: Code admits summaries, lifecycle changes and trace ingress; manual focus or enabling extraction
          is not approval of each result. Remote derived admission remains unresolved.
      - scope: Delegated full-output spill and goal-state save
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id029
          - workflow.md#wf-rte-summary-return
          - epistemic.md#epi-rte-goal-disposition
          note: Host sizing rules create spill files; manager rules save verdict/status without per-content
            approval.
        records: *id029
        note: Host sizing rules create spill files; manager rules save verdict/status without per-content
          approval.
      - scope: Existing files, learning-node UI mutation and hub/direct-file acquisition
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory
        - memory.md#mem-obj-skill-package
        - epistemic.md#epi-rte-memory-gate
        note: The records identify mutation surfaces but not every per-content principal/decision; a UI
          label or generic caller does not prove human control.
      - scope: Native checkpoint creation, remote provider derived writes, optional curator consolidation,
          micro/context-engine/todo and async completion admission
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-native-checkpoint
        - memory.md#mem-rte-provider-cycle
        - memory.md#mem-rte-skill-curation
        - memory.md#mem-rte-local-compaction
        - runtime.md#rt-rte-child-delegation
        note: Known adapter calls and local commits do not establish all alternate admission mechanisms.
      records:
      - memory.md#mem-rte-notes-cycle
      - memory.md#mem-rte-skill-cycle
      - memory.md#mem-rte-review-write
      - memory.md#mem-rte-pending-review
      - memory.md#mem-rte-local-compaction
      - memory.md#mem-rte-skill-curation
      - memory.md#mem-rte-provider-cycle
      - workflow.md#wf-rte-summary-return
      - epistemic.md#epi-rte-goal-disposition
      - memory.md#mem-obj-memory
      - memory.md#mem-obj-skill-package
      - epistemic.md#epi-rte-memory-gate
      - memory.md#mem-obj-native-checkpoint
      - runtime.md#rt-rte-child-delegation
      note: Both automatic and explicit per-content manual admission exist. Initial/control-unknown and
        remote alternatives remain separate; the tool gate is not universal and UI mutation bypasses it.
    curation_operations:
      assessment: partial
      units:
      - scope: Notes/profile and skill content revision
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id030
          - memory.md#mem-rte-notes-cycle
          - memory.md#mem-rte-skill-cycle
          note: Patch/edit replaces existing retained content. Primary acquisition/create alone is not
            curation.
        records: *id030
        note: Patch/edit replaces existing retained content. Primary acquisition/create alone is not curation.
      - scope: Review fact extraction and local readable summary/fallback reduction
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id031
          - memory.md#mem-rte-review-write
          - memory.md#mem-rte-local-compaction
          note: Standing facts/lessons and handoffs reduce selected retained trace; raw evidence may remain
            archived. No new claim is inferred merely from a summary or lesson label.
        records: *id031
        note: Standing facts/lessons and handoffs reduce selected retained trace; raw evidence may remain
          archived. No new claim is inferred merely from a summary or lesson label.
      - scope: Local tool-result pruning and exact recall bullet reduction
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records: &id032
          - memory.md#mem-rte-local-compaction
          - epistemic.md#epi-rte-recall-reshape
          note: Implemented duplicate removal reduces retained-context projections; continuation bullets
            remain distinct. This is not semantic near-duplicate inference.
        records: *id032
        note: Implemented duplicate removal reduces retained-context projections; continuation bullets
          remain distinct. This is not semantic near-duplicate inference.
      - scope: Activity-driven skill aging/archive and restore
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id033
          - memory.md#mem-rte-skill-curation
          note: Aging lowers availability, archive withdraws active reliance while preserving the package,
            and restore raises it back to active availability. These operations do not endorse procedural
            truth.
        - value: invalidate
          basis: wired
          records: *id033
          note: Aging lowers availability, archive withdraws active reliance while preserving the package,
            and restore raises it back to active availability. These operations do not endorse procedural
            truth.
        - value: promote
          basis: wired
          records: *id033
          note: Aging lowers availability, archive withdraws active reliance while preserving the package,
            and restore raises it back to active availability. These operations do not endorse procedural
            truth.
        records: *id033
        note: Aging lowers availability, archive withdraws active reliance while preserving the package,
          and restore raises it back to active availability. These operations do not endorse procedural
          truth.
      - scope: Optional curator consolidation/synthesis, provider internal transformation, native payload
          and micro/context-engine maintenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-skill-curation
        - memory.md#mem-rte-provider-cycle
        - memory.md#mem-obj-native-checkpoint
        - memory.md#mem-rte-local-compaction
        note: Requested consolidation and remote synthesis displays do not establish implemented controlled
          transformations at those opaque branches. No synthesize finding follows from fidelity defects.
      - scope: Hub/preprocessing, reset/purge/rollback, context-file/todo and spill retention maintenance
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-skill-cycle
        - memory.md#mem-rte-skill-curation
        - memory.md#mem-rte-local-compaction
        - workflow.md#wf-rte-summary-return
        note: Acquisition, index rebuild and file deletion alone establish none of the remaining operations;
          full maintenance routes are not traced.
      records:
      - memory.md#mem-rte-notes-cycle
      - memory.md#mem-rte-skill-cycle
      - memory.md#mem-rte-review-write
      - memory.md#mem-rte-local-compaction
      - epistemic.md#epi-rte-recall-reshape
      - memory.md#mem-rte-skill-curation
      - memory.md#mem-rte-provider-cycle
      - memory.md#mem-obj-native-checkpoint
      - workflow.md#wf-rte-summary-return
      note: Implemented revision, reduction, duplicate removal and reversible availability changes support
        positives. Opaque semantic transformations and incompletely inspected maintenance prevent an exhaustive
        operation set.
    read_back_direction:
      assessment: partial
      units:
      - scope: Whole notes/profile blocks and eligible skill index at prompt assembly
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id034
          - memory.md#mem-rte-notes-cycle
          - memory.md#mem-rte-skill-cycle
          note: Load/rebuild automatically supplies enabled snapshots and catalog descriptions without
            the later model requesting each entry.
        records: *id034
        note: Load/rebuild automatically supplies enabled snapshots and catalog descriptions without the
          later model requesting each entry.
      - scope: Requested skill body/support files, session search/read and explicit provider query/read
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id035
          - memory.md#mem-rte-skill-cycle
          - memory.md#mem-rte-session-recall
          - memory.md#mem-rte-provider-cycle
          note: A model/caller request is fulfilled by selection and return. Code delivery within that
            requested chain is not a second push.
        records: *id035
        note: A model/caller request is fulfilled by selection and return. Code delivery within that requested
          chain is not a second push.
      - scope: Local handoffs, latest native checkpoint run and automatic provider prefetch
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id036
          - memory.md#mem-rte-local-compaction
          - memory.md#mem-obj-native-checkpoint
          - memory.md#mem-rte-provider-cycle
          - epistemic.md#epi-rte-recall-consume
          note: Code supplies selected accumulated context to later requests without a retained-material
            request by that consumer. Opaque content does not remove the known adapter direction.
        records: *id036
        note: Code supplies selected accumulated context to later requests without a retained-material
          request by that consumer. Opaque content does not remove the known adapter direction.
      - scope: Requested caller resume
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id037
          - runtime.md#rt-rte-oneshot-turn
          - memory.md#mem-rte-session-recall
          note: The caller requests retained active history; it does not request every archived/audit
            row.
        records: *id037
        note: The caller requests retained active history; it does not request every archived/audit row.
      - scope: Full spilled answer requested by parent
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records: &id038
          - workflow.md#wf-rte-summary-return
          note: The file pointer affords a later read_file request, not automatic paging.
        records: *id038
        note: The file pointer affords a later read_file request, not automatic paging.
      - scope: Saved goal status and generated repair prompts
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id039
          - epistemic.md#epi-rte-goal-disposition
          note: Later manager boundaries consume saved verdict/status automatically; continuing code enqueues
            repair guidance for a later model invocation.
        records: *id039
        note: Later manager boundaries consume saved verdict/status automatically; continuing code enqueues
          repair guidance for a later model invocation.
      - scope: Pending payload display/apply command
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id040
          - memory.md#mem-rte-pending-review
          note: An explicit list/diff/apply request loads pending retained payloads; adoption and later
            prompt supply are separate operations.
        records: *id040
        note: An explicit list/diff/apply request loads pending retained payloads; adoption and later
          prompt supply are separate operations.
      - scope: Auto-load/slash/plugin skills, micro/context engines, editable context files/todo, native
          app-server state and async completion consumption
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-skill-cycle
        - memory.md#mem-rte-local-compaction
        - runtime.md#rt-rte-codex-turn
        - runtime.md#rt-rte-child-delegation
        note: Alternate delivery exists or is named, but its complete request/selection/delivery chain
          is not traced. No pull-only or read-back-absence conclusion follows.
      records:
      - memory.md#mem-rte-notes-cycle
      - memory.md#mem-rte-skill-cycle
      - memory.md#mem-rte-session-recall
      - memory.md#mem-rte-provider-cycle
      - memory.md#mem-rte-local-compaction
      - memory.md#mem-obj-native-checkpoint
      - epistemic.md#epi-rte-recall-consume
      - runtime.md#rt-rte-oneshot-turn
      - workflow.md#wf-rte-summary-return
      - epistemic.md#epi-rte-goal-disposition
      - memory.md#mem-rte-pending-review
      - runtime.md#rt-rte-codex-turn
      - runtime.md#rt-rte-child-delegation
      note: Both requested and unsolicited routes are supported. Known native adapter replay is distinct
        from opaque payload meaning; unresolved alternate chains remain included.
    read_back_signal:
      assessment: partial
      units:
      - scope: Notes/profile whole-block push and skill-index push
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id041
          - memory.md#mem-rte-notes-cycle
          - memory.md#mem-rte-skill-cycle
          note: Trigger is prompt load/rebuild; selector inputs are enable flags and catalog eligibility/platform/disabled/tool
            filters; selected parts are entire eligible blocks/descriptions, not query-matched entries.
        records: *id041
        note: Trigger is prompt load/rebuild; selector inputs are enable flags and catalog eligibility/platform/disabled/tool
          filters; selected parts are entire eligible blocks/descriptions, not query-matched entries.
      - scope: Local handoff/head-tail and latest checkpoint-run push
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id042
          - memory.md#mem-rte-local-compaction
          - memory.md#mem-obj-native-checkpoint
          note: Pressure/next-request triggers select by recency, grouping and budget; retained summary/tail
            or latest checkpoint plus plaintext budget slices are delivered. Positions and session IDs
            alone are not identity-targeted selection.
        records: *id042
        note: Pressure/next-request triggers select by recency, grouping and budget; retained summary/tail
          or latest checkpoint plus plaintext budget slices are delivered. Positions and session IDs alone
          are not identity-targeted selection.
      - scope: Provider automatic recall
        assessment: partial
        findings:
        - value: coarse
          basis: wired
          records: &id043
          - memory.md#mem-rte-provider-cycle
          - epistemic.md#epi-rte-recall-consume
          note: Nontrivial-turn/provider availability triggers consumption of caches or query responses.
            Coarse gates are known; RetainDB uses prior queued results and ByteRover a current-query CLI
            call. Exact remote matching signals are unresolved.
        records: *id043
        note: Nontrivial-turn/provider availability triggers consumption of caches or query responses.
          Coarse gates are known; RetainDB uses prior queued results and ByteRover a current-query CLI
          call. Exact remote matching signals are unresolved.
      - scope: Remote provider context/profile selection algorithm
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-provider-cycle
        - memory.md#mem-obj-provider-state
        - epistemic.md#epi-rte-recall-consume
        note: A query or prose synthesis name does not establish lexical, embedding or judgment selection
          of the actual retained payload. No exact targeting algorithm is recorded.
      - scope: Saved goal control and repair delivery
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id044
          - epistemic.md#epi-rte-goal-disposition
          note: Eligible goal boundaries consume status/verdict and conditionally enqueue the associated
            repair prompt; this is state/availability selection, not relevance ranking.
        records: *id044
        note: Eligible goal boundaries consume status/verdict and conditionally enqueue the associated
          repair prompt; this is state/availability selection, not relevance ranking.
      - scope: Requested skill/session/provider/pending/spill routes
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-skill-cycle
        - memory.md#mem-rte-session-recall
        - memory.md#mem-rte-pending-review
        - workflow.md#wf-rte-summary-return
        note: Push-signal classification is inapplicable to these explicitly requested returns; their
          IDs/queries do not supply an independent push selector.
      - scope: Auto-loaded/plugin skills, micro/context-engine and todo/context-file selectors, async/native-thread
          delivery
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-skill-cycle
        - memory.md#mem-rte-local-compaction
        - runtime.md#rt-rte-child-delegation
        - runtime.md#rt-rte-codex-turn
        note: Trigger/selector/selected-part triples are not fully recorded for these alternative pushes.
          Neither inferred-judgment nor identifier follows from model use or a catalog name.
      records:
      - memory.md#mem-rte-notes-cycle
      - memory.md#mem-rte-skill-cycle
      - memory.md#mem-rte-local-compaction
      - memory.md#mem-obj-native-checkpoint
      - memory.md#mem-rte-provider-cycle
      - epistemic.md#epi-rte-recall-consume
      - memory.md#mem-obj-provider-state
      - epistemic.md#epi-rte-goal-disposition
      - memory.md#mem-rte-session-recall
      - memory.md#mem-rte-pending-review
      - workflow.md#wf-rte-summary-return
      - runtime.md#rt-rte-child-delegation
      - runtime.md#rt-rte-codex-turn
      note: Coarse automatic selection is established locally. Query-based provider calls do not reveal
        their actual matching mechanism; unresolved alternatives prevent a complete signal classification.
    trace_learning:
      assessment: partial
      units:
      - scope: Completed-turn review to admitted notes/skills and later prompt/view
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id045
          - memory.md#mem-rte-review-write
          - memory.md#mem-rte-notes-cycle
          - memory.md#mem-rte-skill-cycle
          note: Automatic trace-fed lesson writes produce durable behavior-shaping content with later
            consumers; optional human-gated alternatives do not erase ungated admissions.
        records: *id045
        note: Automatic trace-fed lesson writes produce durable behavior-shaping content with later consumers;
          optional human-gated alternatives do not erase ungated admissions.
      - scope: Local generated/deterministic continuation handoffs
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id046
          - memory.md#mem-rte-local-compaction
          note: Automatic trace reduction is committed and supplied to subsequent inference. Knowledge
            novelty, lossless retention and measured improvement are not required.
        records: *id046
        note: Automatic trace reduction is committed and supplied to subsequent inference. Knowledge novelty,
          lossless retention and measured improvement are not required.
      - scope: Goal feedback to saved verdict/reason and later manager/repair input
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id047
          - epistemic.md#epi-obj-goal-verdict
          - epistemic.md#epi-rte-goal-check
          - epistemic.md#epi-rte-goal-disposition
          note: Automatic response/gate evaluation saves durable behavior-shaping state; later boundaries
            consume it and can deliver a repair prompt. This is not a claim of improved capacity.
        records: *id047
        note: Automatic response/gate evaluation saves durable behavior-shaping state; later boundaries
          consume it and can deliver a repair prompt. This is not a claim of improved capacity.
      - scope: Raw-only session archival and full-output spill
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-obj-session-content
        - memory.md#mem-rte-session-recall
        - workflow.md#wf-rte-summary-return
        note: Raw trace retention/copy alone is not a qualifying behavior-shaping update. Compaction-derived
          handoffs and review writes are assessed separately.
      - scope: Provider derived facts/profiles/tree and native encrypted checkpoint
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-provider-cycle
        - memory.md#mem-obj-provider-state
        - memory.md#mem-obj-native-checkpoint
        note: Trace ingress and later adapters are known, but opaque transformation/admission and exact
          behavior-shaping output prevent a complete qualifying-write assessment.
      - scope: Micro/context-engine updates, optional curator consolidation and other skill/context-file/todo/async
          writes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-local-compaction
        - memory.md#mem-rte-skill-curation
        - memory.md#mem-rte-skill-cycle
        - runtime.md#rt-rte-child-delegation
        note: Full raw-to-derived-to-later-consumer chains remain incompletely inspected. Foreground writes
          may also use selected traces but no complete trace-input inventory is recorded.
      records:
      - memory.md#mem-rte-review-write
      - memory.md#mem-rte-notes-cycle
      - memory.md#mem-rte-skill-cycle
      - memory.md#mem-rte-local-compaction
      - epistemic.md#epi-obj-goal-verdict
      - epistemic.md#epi-rte-goal-check
      - epistemic.md#epi-rte-goal-disposition
      - memory.md#mem-obj-session-content
      - memory.md#mem-rte-session-recall
      - workflow.md#wf-rte-summary-return
      - memory.md#mem-rte-provider-cycle
      - memory.md#mem-obj-provider-state
      - memory.md#mem-obj-native-checkpoint
      - memory.md#mem-rte-skill-curation
      - runtime.md#rt-rte-child-delegation
      note: Review, local continuation handoffs and saved goal-feedback adaptation establish architectural
        yes findings. No system-wide no, observed learning benefit or exercised self-improvement is inferred;
        opaque and alternate writes remain unresolved.
    trace_source:
      assessment: partial
      units:
      - scope: Review lesson input
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id048
          - memory.md#mem-rte-review-write
          note: The completed-turn snapshot/digest contains recorded user/model conversation and tool
            requests/results. Digest routing does not turn it into an event stream.
        - value: tool-traces
          basis: wired
          records: *id048
          note: The completed-turn snapshot/digest contains recorded user/model conversation and tool
            requests/results. Digest routing does not turn it into an event stream.
        records: *id048
        note: The completed-turn snapshot/digest contains recorded user/model conversation and tool requests/results.
          Digest routing does not turn it into an event stream.
      - scope: Local continuation handoff input
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id049
          - memory.md#mem-rte-local-compaction
          note: Mixed recorded conversation, including tool content, feeds selected/pruned summary input
            or deterministic fallback. These are not established trajectories of linked states/actions/outcomes.
        - value: tool-traces
          basis: wired
          records: *id049
          note: Mixed recorded conversation, including tool content, feeds selected/pruned summary input
            or deterministic fallback. These are not established trajectories of linked states/actions/outcomes.
        records: *id049
        note: Mixed recorded conversation, including tool content, feeds selected/pruned summary input
          or deterministic fallback. These are not established trajectories of linked states/actions/outcomes.
      - scope: Goal feedback adaptation input
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id050
          - epistemic.md#epi-rte-goal-check
          - epistemic.md#epi-rte-goal-disposition
          note: Last conversational response and shell gate execution feedback feed saved verdict/reason
            and subsequent repair/continuation; packaging as synthetic events does not add event-stream
            lineage.
        - value: tool-traces
          basis: wired
          records: *id050
          note: Last conversational response and shell gate execution feedback feed saved verdict/reason
            and subsequent repair/continuation; packaging as synthetic events does not add event-stream
            lineage.
        records: *id050
        note: Last conversational response and shell gate execution feedback feed saved verdict/reason
          and subsequent repair/continuation; packaging as synthetic events does not add event-stream
          lineage.
      - scope: Raw-only archives and full-answer spills
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-obj-session-content
        - workflow.md#wf-rte-summary-return
        note: Without a qualifying trace-fed update these raw retention paths have no trace-learning source
          classification; their derived review/summary consumers are separate units.
      - scope: Provider ingress associated with unresolved derived updates
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-provider-cycle
        - memory.md#mem-obj-provider-state
        note: Repository-side turn-pair queuing and curate requests identify possible trace inputs,
          but the accepted records do not establish a qualifying automatic write with a durable
          behavior-shaping result and later consumer. No provider trace-source value can therefore
          be assigned; opaque transformation and admission prevent that classification.
      - scope: Native checkpoint original input and remote derivation beyond recorded adapter ingress
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-native-checkpoint
        - memory.md#mem-obj-provider-state
        - memory.md#mem-rte-provider-cycle
        note: Earlier context and remote displays do not establish the complete original input of every
          qualifying write.
      - scope: Micro/context-engine, optional curator and alternate content/async writes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-local-compaction
        - memory.md#mem-rte-skill-curation
        - memory.md#mem-rte-skill-cycle
        - runtime.md#rt-rte-child-delegation
        note: Missing qualifying-write chains prevent full source assignment; no event-streams or trajectories
          value is inferred from serialization or execution labels.
      records:
      - memory.md#mem-rte-review-write
      - memory.md#mem-rte-local-compaction
      - epistemic.md#epi-rte-goal-check
      - epistemic.md#epi-rte-goal-disposition
      - memory.md#mem-obj-session-content
      - workflow.md#wf-rte-summary-return
      - memory.md#mem-rte-provider-cycle
      - memory.md#mem-obj-native-checkpoint
      - memory.md#mem-obj-provider-state
      - memory.md#mem-rte-skill-curation
      - memory.md#mem-rte-skill-cycle
      - runtime.md#rt-rte-child-delegation
      note: Known qualifying routes consume session records and execution feedback. Mixed/opaque alternatives
        remain unresolved rather than inapplicable; no complete-source union is claimed.
---

# Hermes Agent memory profile

## Comparison rationale

This is a revision-2 classification of the accepted records, not a new source account. Every axis is partial because the included unresolved alternatives differ by dimension. Local known units establish their scoped mechanisms, not complete system inventories. All positive mechanisms are wired unless a finding explicitly says afforded; none is observed or causally supported. The frozen analysis remains partial-loop inspection.

The reconciliation establishes no supersessions. The session envelope, its readable retained content, local summary and opaque checkpoint remain distinct parts. Notes/profile share a mechanism but not a file or budget. Skill content does not replace the package/control inventory. Review scheduling, candidate generation and guarded downstream retention are connected stages, not duplicate routes. These distinctions preserve the warrants of [MEM-OBJ-session-content](memory.md#mem-obj-session-content), [MEM-OBJ-native-checkpoint](memory.md#mem-obj-native-checkpoint), [MEM-OBJ-skill-package](memory.md#mem-obj-skill-package) and [MEM-RTE-review-write](memory.md#mem-rte-review-write).

The initial authorship of a store is independent of its later admission. Automatic model/software writes and explicit human pending approvals therefore coexist with unresolved initial files and learning-node UI control. The latter bypasses the optional tool gate; it cannot be silently assigned manual agency or excluded to make coverage complete. See [EPI-RTE-memory-gate](epistemic.md#epi-rte-memory-gate) and [MEM-RTE-pending-review](memory.md#mem-rte-pending-review).

Learning authority belongs to traces at update consumers; downstream notes, procedures and summaries separately provide knowledge or instruction. Local continuation summaries count as trace learning even when they merely compress existing claims. Saved goal feedback also changes later manager/repair behavior; its source is response history and execution feedback, not an event stream just because a gateway wraps a repair as an event. None of these classifications establishes semantic novelty, improved capacity or exercised self-improvement. See [MEM-RTE-local-compaction](memory.md#mem-rte-local-compaction), [MEM-RTE-review-write](memory.md#mem-rte-review-write) and [EPI-RTE-goal-disposition](epistemic.md#epi-rte-goal-disposition).

Skill archive/restore maps to decay, invalidation and promotion because it changes availability while retaining the package. Exact bullet reduction and tool-result deduplication supply dedup; extraction and summary reduction supply consolidation. Model prompts requesting class-level rules or optional curator consolidation do not by themselves establish synthesis. See [MEM-RTE-skill-curation](memory.md#mem-rte-skill-curation), [EPI-RTE-recall-reshape](epistemic.md#epi-rte-recall-reshape) and [MEM-RTE-local-compaction](memory.md#mem-rte-local-compaction).

A requested body or archive read remains pull, including its code-owned result delivery. Whole prompt blocks, summary selection and unsolicited provider prefetch are push. RetainDB cache consumption follows prior queued queries; ByteRover queries at prefetch time. Neither adapter exposes a sufficiently specific remote selector to assert inferred lexical, embedding or judgment selection. Identifier-bearing catalog entries and requested file paths are not identity-matched push evidence. See [MEM-RTE-skill-cycle](memory.md#mem-rte-skill-cycle), [MEM-RTE-session-recall](memory.md#mem-rte-session-recall) and [EPI-RTE-recall-consume](epistemic.md#epi-rte-recall-consume).

Successful spill creation establishes file retention; the later parent read is afforded, not established as wired replay. The child summary's earlier schema verdict does not classify omitted or altered content. Raw retention alone is not trace learning. See [WF-RTE-summary-return](workflow.md#wf-rte-summary-return) and [WF-RTE-output-contract](workflow.md#wf-rte-output-contract).

Provider ingress does not establish a trace-learning source. Queued turn pairs and explicit curate requests can carry traces, but the accepted records leave the derived transformation, admission and durable behavior-shaping result unresolved. The provider trace-source unit therefore has no positive findings and remains not-determinable, consistent with its trace-learning unit. This does not withdraw the supported sources of review, local handoffs or goal feedback. See [MEM-RTE-provider-cycle](memory.md#mem-rte-provider-cycle) and [MEM-OBJ-provider-state](memory.md#mem-obj-provider-state).

No frozen target source files were read for this profile. All warrants come from the supplied accepted record passages. Opaque provider/checkpoint contents, frontend lifecycle equivalence, UI authorization/refresh, micro-summary commits, optional maintenance and alternate context/async consumers remain limits rather than inferred absences.
