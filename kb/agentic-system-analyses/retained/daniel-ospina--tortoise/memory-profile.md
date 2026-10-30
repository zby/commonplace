---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Tortoise memory comparison: retained session traces, derived graph content, numerical controls and callback delivery, with unresolved shipped alternatives."
run-id: "AAS-2026-10-30-tortoise-0c919b4ca77d-01"
source-identity: "https://github.com/daniel-ospina/tortoise"
reviewed-boundary: "54922a800f96858935b58ef250da569a4896df44"
memory-comparison:
  version: 2
  scope: "Retained session turns, derived Points/relations/embeddings, caller-authored checkpoints/diaries, confidence/review/lifecycle state, event journals/record projections and local capture backlog; their admission, maintenance and later retrieval/context consumers. Included unresolved alternatives are M2 and full production commit, imports/packs, UI/service writers, recovery/replay readers and other harnesses. Excludes static shipped instructions, transient extraction payloads and current-run intermediates as independent memory, enclosing host internals and provider/database internals."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - 
          scope: "Retained graph content, relationships, lifecycle and belief fields"
          assessment: "known"
          findings:
            - 
              value: "graph"
              basis: "wired"
              records:
                - "memory.md#mem-obj-derived-points"
                - "memory.md#mem-obj-authored-points"
                - "memory.md#mem-obj-belief-state"
                - "epistemic.md#epi-obj-review-verdict"
              note: "Projection holds text, relations and maintenance/review state."
          records:
            - "memory.md#mem-obj-derived-points"
            - "memory.md#mem-obj-authored-points"
            - "memory.md#mem-obj-belief-state"
            - "epistemic.md#epi-obj-review-verdict"
          note: "Known projection substrate; database internals and cross-store parity are not established."
        - 
          scope: "Configured event journal and record projection"
          assessment: "known"
          findings:
            - 
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-event-emission"
              note: "Optional JSONL journal."
            - 
              value: "rdbms"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-event-emission"
              note: "Optional Postgres record sink, including record-capable turn persistence."
          records:
            - "runtime.md#rt-obj-event-emission"
            - "memory.md#mem-obj-session-turns"
          note: "These configured surfaces have independent failure outcomes, not atomic durability."
        - 
          scope: "Local capture backlog"
          assessment: "known"
          findings:
            - 
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-capture-spool"
              note: "Turn log and retry/filing metadata are local files."
          records:
            - "memory.md#mem-obj-capture-spool"
          note: "Storage is resolved even though complete producer and POST wiring are not."
        - 
          scope: "Included alternative capture, import, pack, UI, recovery and other harness memory paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-production-commit"
            - "runtime.md#rt-rte-direct-point"
            - "memory.md#mem-obj-capture-spool"
          note: "Complete remote commit consumption, generic direct-input control and full spool producers/readers are unresolved. The reports also retain imports, packs and other shipped writers/readers as an inspection frontier; no whole-system inventory is established."
      records:
        - "memory.md#mem-obj-derived-points"
        - "memory.md#mem-obj-authored-points"
        - "memory.md#mem-obj-belief-state"
        - "epistemic.md#epi-obj-review-verdict"
        - "runtime.md#rt-obj-event-emission"
        - "memory.md#mem-obj-session-turns"
        - "memory.md#mem-obj-capture-spool"
        - "runtime.md#rt-rte-production-commit"
        - "runtime.md#rt-rte-direct-point"
      note: "Inspected retained substrates are classified; unresolved shipped alternatives prevent exhaustive storage coverage. Model weights and transient payload/process state are not accumulated memory substrates."
    representational_form:
      assessment: "partial"
      units:
        - 
          scope: "Retained turn, Point, diary and checkpoint prose delivered as context"
          assessment: "known"
          findings:
            - 
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-turns"
                - "memory.md#mem-obj-derived-points"
                - "memory.md#mem-obj-authored-points"
                - "runtime.md#rt-bap-framework-block"
              note: "Content is interpreted by later models; labels and optional review reasons are prose too."
          records:
            - "memory.md#mem-obj-session-turns"
            - "memory.md#mem-obj-derived-points"
            - "memory.md#mem-obj-authored-points"
            - "runtime.md#rt-bap-framework-block"
            - "epistemic.md#epi-obj-review-verdict"
          note: "Text consumption is distinct from the fields controlling access."
        - 
          scope: "Retained IDs, relations, lifecycle, confidence parameters, freshness and filing controls"
          assessment: "known"
          findings:
            - 
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-belief-state"
                - "epistemic.md#epi-obj-belief-state"
                - "memory.md#mem-obj-capture-spool"
                - "epistemic.md#epi-obj-review-verdict"
              note: "Fixed code consumes localized graph fields, numbers, decision markers and retry state."
          records:
            - "memory.md#mem-obj-belief-state"
            - "epistemic.md#epi-obj-belief-state"
            - "memory.md#mem-obj-capture-spool"
            - "epistemic.md#epi-obj-review-verdict"
          note: "Numerical EP state is symbolic, not model weights."
        - 
          scope: "Retained dense embeddings of session turns and derived content"
          assessment: "known"
          findings:
            - 
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-turns"
                - "memory.md#mem-obj-derived-points"
                - "runtime.md#rt-cmp-embedding-model"
              note: "Dense encoded vectors are distinct from their source prose and from encoder weights."
          records:
            - "memory.md#mem-obj-session-turns"
            - "memory.md#mem-obj-derived-points"
            - "runtime.md#rt-cmp-embedding-model"
          note: "The represented encoding is classified; full training/initial provenance is not."
        - 
          scope: "Included alternative capture, import, pack, UI, recovery and other harness memory paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-production-commit"
            - "runtime.md#rt-rte-direct-point"
            - "memory.md#mem-obj-capture-spool"
          note: "Complete remote commit consumption, generic direct-input control and full spool producers/readers are unresolved. The reports also retain imports, packs and other shipped writers/readers as an inspection frontier; no whole-system inventory is established."
      records:
        - "memory.md#mem-obj-session-turns"
        - "memory.md#mem-obj-derived-points"
        - "memory.md#mem-obj-authored-points"
        - "runtime.md#rt-bap-framework-block"
        - "epistemic.md#epi-obj-review-verdict"
        - "memory.md#mem-obj-belief-state"
        - "epistemic.md#epi-obj-belief-state"
        - "memory.md#mem-obj-capture-spool"
        - "runtime.md#rt-cmp-embedding-model"
        - "runtime.md#rt-rte-production-commit"
        - "runtime.md#rt-rte-direct-point"
      note: "Mixed text, symbolic controls and dense embeddings remain separate. Remote provider internals are outside the frozen evidence, not assumed retained conversation memory."
    lineage:
      assessment: "partial"
      units:
        - 
          scope: "Stored scrubbed/windowed caller turns"
          assessment: "known"
          findings:
            - 
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-turns"
              note: "Conversation enters as caller-supplied text; windowing/redaction do not make its assertions system-authored."
          records:
            - "memory.md#mem-obj-session-turns"
          note: "Initial source truth and human control remain unknown."
        - 
          scope: "v2 extracted durable graph content"
          assessment: "known"
          findings:
            - 
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-derived-points"
                - "runtime.md#rt-rte-session-capture"
              note: "Conversation traces feed model/code formation of stored Points and relationships."
          records:
            - "memory.md#mem-obj-derived-points"
            - "runtime.md#rt-rte-session-capture"
          note: "This classifies derivation, not semantic faithfulness or factual warrant."
        - 
          scope: "Caller-composed checkpoint and diary content"
          assessment: "known"
          findings:
            - 
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-authored-points"
                - "memory.md#mem-rte-checkpoint-diary"
              note: "Caller supplies composed entries; authored lineage does not mean human approval."
          records:
            - "memory.md#mem-obj-authored-points"
            - "memory.md#mem-rte-checkpoint-diary"
          note: "Generic caller identity is unresolved, independently of content composition."
        - 
          scope: "Computed embeddings and maintained confidence/freshness values"
          assessment: "partial"
          findings:
            - 
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-turns"
                - "runtime.md#rt-cmp-embedding-model"
                - "memory.md#mem-rte-dream-writeback"
              note: "Encoding and fixed numerical maintenance derive retained representations from existing inputs."
          records:
            - "memory.md#mem-obj-session-turns"
            - "runtime.md#rt-cmp-embedding-model"
            - "memory.md#mem-rte-dream-writeback"
          note: "Known transformations only; initial graph evidence and warm-start message provenance remain unresolved."
        - 
          scope: "Included alternative capture, import, pack, UI, recovery and other harness memory paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-production-commit"
            - "runtime.md#rt-rte-direct-point"
            - "memory.md#mem-obj-capture-spool"
          note: "Complete remote commit consumption, generic direct-input control and full spool producers/readers are unresolved. The reports also retain imports, packs and other shipped writers/readers as an inspection frontier; no whole-system inventory is established."
      records:
        - "memory.md#mem-obj-session-turns"
        - "memory.md#mem-obj-derived-points"
        - "runtime.md#rt-rte-session-capture"
        - "memory.md#mem-obj-authored-points"
        - "memory.md#mem-rte-checkpoint-diary"
        - "runtime.md#rt-cmp-embedding-model"
        - "memory.md#mem-rte-dream-writeback"
        - "runtime.md#rt-rte-production-commit"
        - "runtime.md#rt-rte-direct-point"
        - "memory.md#mem-obj-capture-spool"
      note: "Known derivation paths coexist with unknown initial evidence/embedding provenance and unresolved alternative inputs."
    behavioral_authority:
      assessment: "partial"
      units:
        - 
          scope: "Selected retained prose at host framework and session-start model consumers"
          assessment: "known"
          findings:
            - 
              value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-framework-block"
                - "memory.md#mem-bap-start-digest"
              note: "Excerpts supply advisory prior context, not enforced behavior or guaranteed truth."
          records:
            - "runtime.md#rt-bap-framework-block"
            - "memory.md#mem-bap-start-digest"
          note: "Shipped static guidance and generated wrapper wording are not separately classified as accumulated standing instructions."
        - 
          scope: "Retained conversation and graph priors at the v2 extraction/update consumer"
          assessment: "known"
          findings:
            - 
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-derived-points"
                - "runtime.md#rt-rte-session-capture"
              note: "Experience feeds automatic formation of durable behavior-shaping graph content."
            - 
              value: "learning"
              basis: "wired"
              records:
                - "workflow.md#wf-rte-gap-review"
              note: "Retained graph priors enter gap review that can revise the eventual durable memory candidate."
          records:
            - "memory.md#mem-obj-derived-points"
            - "runtime.md#rt-rte-session-capture"
            - "workflow.md#wf-rte-gap-review"
          note: "Learning authority at the updater is separate from downstream knowledge authority; benefit is not demonstrated."
        - 
          scope: "Retained confidence and lifecycle at canonical selection"
          assessment: "known"
          findings:
            - 
              value: "ranking"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "epistemic.md#epi-rte-belief-evaluate"
              note: "Confidence affects relative priority."
            - 
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "memory.md#mem-rte-point-retraction"
              note: "Terminal states and confidence gates exclude candidates from canonical delivery."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "epistemic.md#epi-rte-belief-evaluate"
            - "memory.md#mem-rte-point-retraction"
          note: "This force does not extend to all readers: the local digest lacks the same terminal filter."
        - 
          scope: "Retained freshness, filing and review decision metadata at maintenance/recovery consumers"
          assessment: "known"
          findings:
            - 
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-rte-dream-writeback"
                - "memory.md#mem-obj-capture-spool"
                - "epistemic.md#epi-rte-review-disposition"
              note: "Dirty/stale roots select maintenance; filing markers select retry; verdicts select or skip review."
          records:
            - "memory.md#mem-rte-dream-writeback"
            - "memory.md#mem-obj-capture-spool"
            - "epistemic.md#epi-rte-review-disposition"
          note: "These controls select work rather than supply model knowledge."
        - 
          scope: "Retained posterior, review approval and target state at correction admission/integration"
          assessment: "known"
          findings:
            - 
              value: "validation"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-review-disposition"
                - "epistemic.md#epi-rte-review-integration"
              note: "Stored posterior and eligible target/approval state supply admission and wiring criteria."
            - 
              value: "enforcement"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-review-disposition"
                - "epistemic.md#epi-rte-review-integration"
              note: "Code can refuse conflicting decisions or ineligible wiring and applies lifecycle changes."
          records:
            - "epistemic.md#epi-rte-review-disposition"
            - "epistemic.md#epi-rte-review-integration"
          note: "Optional threshold acceptance has graph-relative scope, not truth certification."
        - 
          scope: "Included alternative capture, import, pack, UI, recovery and other harness memory paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-production-commit"
            - "runtime.md#rt-rte-direct-point"
            - "memory.md#mem-obj-capture-spool"
          note: "Complete remote commit consumption, generic direct-input control and full spool producers/readers are unresolved. The reports also retain imports, packs and other shipped writers/readers as an inspection frontier; no whole-system inventory is established."
      records:
        - "runtime.md#rt-bap-framework-block"
        - "memory.md#mem-bap-start-digest"
        - "memory.md#mem-obj-derived-points"
        - "runtime.md#rt-rte-session-capture"
        - "workflow.md#wf-rte-gap-review"
        - "runtime.md#rt-rte-context-delivery"
        - "epistemic.md#epi-rte-belief-evaluate"
        - "memory.md#mem-rte-point-retraction"
        - "memory.md#mem-rte-dream-writeback"
        - "memory.md#mem-obj-capture-spool"
        - "epistemic.md#epi-rte-review-disposition"
        - "epistemic.md#epi-rte-review-integration"
        - "runtime.md#rt-rte-production-commit"
        - "runtime.md#rt-rte-direct-point"
      note: "Authority is assigned at actual consumers, not inferred from storage or delivery channel. Other readers and admission paths remain unresolved."
    write_agency:
      assessment: "partial"
      units:
        - 
          scope: "SDK/hosted capture storage and v2 extraction admission"
          assessment: "known"
          findings:
            - 
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-capture"
                - "runtime.md#rt-rte-hosted-capture"
                - "memory.md#mem-obj-derived-points"
              note: "Model/code admit content after request gates without per-content human approval."
          records:
            - "runtime.md#rt-rte-session-capture"
            - "runtime.md#rt-rte-hosted-capture"
            - "memory.md#mem-obj-derived-points"
          note: "Caller initiation and hosted policy settings do not make each admitted proposition manual."
        - 
          scope: "Dream numerical write-back and automatic correction threshold branch"
          assessment: "known"
          findings:
            - 
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-dream-writeback"
                - "epistemic.md#epi-rte-review-disposition"
              note: "Software selects updates and, when enabled, correction acceptance."
          records:
            - "memory.md#mem-rte-dream-writeback"
            - "epistemic.md#epi-rte-review-disposition"
          note: "Default-off auto acceptance is wired conditional capacity, not observed operation."
        - 
          scope: "Direct Point/checkpoint/diary admission, explicit review verdicts and retraction"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-direct-point"
            - "memory.md#mem-rte-checkpoint-diary"
            - "epistemic.md#epi-rte-review-disposition"
            - "memory.md#mem-rte-point-retraction"
          note: "Generic callers do not establish human per-content decisions or fully automatic upstream supply. Physical SDK writes alone do not settle admission control."
        - 
          scope: "Included alternative capture, import, pack, UI, recovery and other harness memory paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-production-commit"
            - "runtime.md#rt-rte-direct-point"
            - "memory.md#mem-obj-capture-spool"
          note: "Complete remote commit consumption, generic direct-input control and full spool producers/readers are unresolved. The reports also retain imports, packs and other shipped writers/readers as an inspection frontier; no whole-system inventory is established."
      records:
        - "runtime.md#rt-rte-session-capture"
        - "runtime.md#rt-rte-hosted-capture"
        - "memory.md#mem-obj-derived-points"
        - "memory.md#mem-rte-dream-writeback"
        - "epistemic.md#epi-rte-review-disposition"
        - "runtime.md#rt-rte-direct-point"
        - "memory.md#mem-rte-checkpoint-diary"
        - "memory.md#mem-rte-point-retraction"
        - "runtime.md#rt-rte-production-commit"
        - "memory.md#mem-obj-capture-spool"
      note: "Automatic admission is supported locally; no manual finding is inferred from caller identity, consent or tool availability."
    curation_operations:
      assessment: "partial"
      units:
        - 
          scope: "Checkpoint duplicate admission filter"
          assessment: "known"
          findings:
            - 
              value: "dedup"
              basis: "wired"
              records:
                - "memory.md#mem-rte-checkpoint-diary"
              note: "Hash/in-batch and optional semantic checks reject redundant entries while preserving the survivor."
          records:
            - "memory.md#mem-rte-checkpoint-diary"
          note: "No semantic rewrite is inferred from duplicate rejection."
        - 
          scope: "Retraction and post-keep correction lifecycle changes"
          assessment: "known"
          findings:
            - 
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-point-retraction"
              note: "Tombstone withdraws canonical reliance while retaining history."
            - 
              value: "promote"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-review-disposition"
                - "epistemic.md#epi-rte-review-integration"
              note: "Keep invokes promotion to live graph use."
            - 
              value: "invalidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-review-integration"
              note: "Temporal replacement can retire prior content through supersession."
          records:
            - "memory.md#mem-rte-point-retraction"
            - "epistemic.md#epi-rte-review-disposition"
            - "epistemic.md#epi-rte-review-integration"
          note: "Promotion and supersession can partially fail; no atomic all-reader withdrawal follows."
        - 
          scope: "Same-session stored turn replacement"
          assessment: "known"
          findings:
            - 
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-turns"
                - "runtime.md#rt-rte-session-capture"
              note: "Re-capture updates stored trace content and removes surplus turns in a shorter window."
          records:
            - "memory.md#mem-obj-session-turns"
            - "runtime.md#rt-rte-session-capture"
          note: "This revises the trace, not necessarily previously extracted claims."
        - 
          scope: "v2 extraction of standing content from retained session messages"
          assessment: "partial"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-derived-points"
                - "runtime.md#rt-rte-session-capture"
              note: "Stored conversational traces feed story/mapping/review and retained graph content, reducing session material to standing claims."
          records:
            - "memory.md#mem-obj-derived-points"
            - "runtime.md#rt-rte-session-capture"
            - "epistemic.md#epi-obj-extracted-points"
          note: "Consolidation is supported without a proof of semantic faithfulness. The indeterminate truth-apt relation leaves novel-claim production and any additional synthesis unresolved; extraction errors do not negate consolidation."
        -
          scope: "Numerical confidence maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-dream-writeback"
          note: "Numerical recomputation alone does not establish a controlled curation operation such as decay, semantic evolution or promotion."
        - 
          scope: "Included alternative capture, import, pack, UI, recovery and other harness memory paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-production-commit"
            - "runtime.md#rt-rte-direct-point"
            - "memory.md#mem-obj-capture-spool"
          note: "Complete remote commit consumption, generic direct-input control and full spool producers/readers are unresolved. The reports also retain imports, packs and other shipped writers/readers as an inspection frontier; no whole-system inventory is established."
      records:
        - "memory.md#mem-rte-checkpoint-diary"
        - "memory.md#mem-rte-point-retraction"
        - "epistemic.md#epi-rte-review-disposition"
        - "epistemic.md#epi-rte-review-integration"
        - "memory.md#mem-obj-session-turns"
        - "runtime.md#rt-rte-session-capture"
        - "memory.md#mem-obj-derived-points"
        - "memory.md#mem-rte-dream-writeback"
        - "epistemic.md#epi-obj-extracted-points"
        - "runtime.md#rt-rte-production-commit"
        - "runtime.md#rt-rte-direct-point"
        - "memory.md#mem-obj-capture-spool"
      note: "Only evidenced transformations receive values. Requested MERGE, confidence recomputation, indexing and route names do not establish additional operations."
    read_back_direction:
      assessment: "partial"
      units:
        - 
          scope: "Automatic framework/prompt-hook pointers and session-start digest"
          assessment: "known"
          findings:
            - 
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "memory.md#mem-rte-hook-volunteer"
                - "memory.md#mem-rte-start-digest"
              note: "Callbacks supply retained material without a foreground model request for that memory."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "memory.md#mem-rte-hook-volunteer"
            - "memory.md#mem-rte-start-digest"
          note: "The callback's service request is not a second independent push operation."
        - 
          scope: "Requested service retrieval and source-session expansion"
          assessment: "known"
          findings:
            - 
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "memory.md#mem-rte-source-expansion"
              note: "Service answers the callback request; evaluation retrieval expands seeded sessions on its caller's request."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "memory.md#mem-rte-source-expansion"
          note: "Evaluation pool expansion is wired, not proven final reader delivery."
        - 
          scope: "Caller-requested diary reads"
          assessment: "known"
          findings:
            - 
              value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-checkpoint-diary"
              note: "An exposed diary_read fulfills a caller's requested access."
          records:
            - "memory.md#mem-rte-checkpoint-diary"
          note: "API capability affords retrieval; unspecified caller does not establish automatic model delivery."
        - 
          scope: "Included alternative capture, import, pack, UI, recovery and other harness memory paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-production-commit"
            - "runtime.md#rt-rte-direct-point"
            - "memory.md#mem-obj-capture-spool"
          note: "Complete remote commit consumption, generic direct-input control and full spool producers/readers are unresolved. The reports also retain imports, packs and other shipped writers/readers as an inspection frontier; no whole-system inventory is established."
      records:
        - "runtime.md#rt-rte-context-delivery"
        - "memory.md#mem-rte-hook-volunteer"
        - "memory.md#mem-rte-start-digest"
        - "memory.md#mem-rte-source-expansion"
        - "memory.md#mem-rte-checkpoint-diary"
        - "runtime.md#rt-rte-production-commit"
        - "runtime.md#rt-rte-direct-point"
        - "memory.md#mem-obj-capture-spool"
      note: "Push and pull describe different operations within or across chains. Remaining commit/recovery/harness readers are unresolved."
    read_back_signal:
      assessment: "partial"
      units:
        - 
          scope: "SessionStart recency digest push"
          assessment: "known"
          findings:
            - 
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-start-digest"
              note: "Trigger is session start; timestamp/limit/noise filtering selects recent diary, Point and confidence excerpts without task-specific matching."
          records:
            - "memory.md#mem-rte-start-digest"
          note: "Agent/session labels and source-routing configuration are not evidence of targeted identity selection."
        - 
          scope: "Framework and UserPromptSubmit canonical pointer push"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "memory.md#mem-rte-hook-volunteer"
          note: "Trigger and bounded window/prior-context inputs are known, but accepted records do not resolve the search/ranking implementation into lexical, embedding or judgment selectors. Confidence/budget/suppression gates do not identify that matching method."
        - 
          scope: "Included alternative capture, import, pack, UI, recovery and other harness memory paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-production-commit"
            - "runtime.md#rt-rte-direct-point"
            - "memory.md#mem-obj-capture-spool"
          note: "Complete remote commit consumption, generic direct-input control and full spool producers/readers are unresolved. The reports also retain imports, packs and other shipped writers/readers as an inspection frontier; no whole-system inventory is established."
      records:
        - "memory.md#mem-rte-start-digest"
        - "runtime.md#rt-rte-context-delivery"
        - "memory.md#mem-rte-hook-volunteer"
        - "runtime.md#rt-rte-production-commit"
        - "runtime.md#rt-rte-direct-point"
        - "memory.md#mem-obj-capture-spool"
      note: "One coarse push is classified; targeted matching remains unresolved. IDs printed in pointers and graph-seeded requested expansion do not by themselves establish identifier-based push."
    trace_learning:
      assessment: "partial"
      units:
        - 
          scope: "Automatic v2 conversation-to-graph update and later framework consumption"
          assessment: "known"
          findings:
            - 
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-derived-points"
                - "runtime.md#rt-rte-session-capture"
                - "runtime.md#rt-rte-context-delivery"
              note: "Recorded conversational turns feed durable derived content later selectable into host context; no weight update or improved performance is required."
          records:
            - "memory.md#mem-obj-derived-points"
            - "runtime.md#rt-rte-session-capture"
            - "runtime.md#rt-rte-context-delivery"
          note: "Wired qualifying trace-fed update; actual use and benefit unobserved."
        - 
          scope: "Caller-supplied checkpoints/direct content, alternative extractor/commit and numerical maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-checkpoint-diary"
            - "runtime.md#rt-rte-direct-point"
            - "runtime.md#rt-rte-production-commit"
            - "memory.md#mem-rte-dream-writeback"
          note: "Upstream content generation, full alternate extraction and initial evidence origins are unresolved. Dream alone is not established as learning from agent outcomes. No bounded absence record warrants a local no."
        - 
          scope: "Included alternative capture, import, pack, UI, recovery and other harness memory paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-production-commit"
            - "runtime.md#rt-rte-direct-point"
            - "memory.md#mem-obj-capture-spool"
          note: "Complete remote commit consumption, generic direct-input control and full spool producers/readers are unresolved. The reports also retain imports, packs and other shipped writers/readers as an inspection frontier; no whole-system inventory is established."
      records:
        - "memory.md#mem-obj-derived-points"
        - "runtime.md#rt-rte-session-capture"
        - "runtime.md#rt-rte-context-delivery"
        - "memory.md#mem-rte-checkpoint-diary"
        - "runtime.md#rt-rte-direct-point"
        - "runtime.md#rt-rte-production-commit"
        - "memory.md#mem-rte-dream-writeback"
        - "memory.md#mem-obj-capture-spool"
      note: "A supported yes coexists with unresolved learning routes. No system-wide negative or complete learning inventory is asserted."
    trace_source:
      assessment: "partial"
      units:
        - 
          scope: "Original conversational input to qualifying v2 extraction"
          assessment: "known"
          findings:
            - 
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-turns"
                - "memory.md#mem-obj-derived-points"
                - "runtime.md#rt-rte-session-capture"
              note: "Caller role/content conversational turns are bounded/redacted before derived-memory formation."
          records:
            - "memory.md#mem-obj-session-turns"
            - "memory.md#mem-obj-derived-points"
            - "runtime.md#rt-rte-session-capture"
          note: "No tool-trace, environmental event-stream or state/action/outcome trajectory source is separately established in these accepted records."
        - 
          scope: "Other possible trace-fed writes and mixed provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-production-commit"
            - "memory.md#mem-rte-checkpoint-diary"
            - "memory.md#mem-rte-dream-writeback"
          note: "Alternative commit/extraction inputs, caller-derived content and initial graph evidence provenance are not resolved. Their source cannot be made inapplicable by the known conversation route."
        - 
          scope: "Included alternative capture, import, pack, UI, recovery and other harness memory paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-production-commit"
            - "runtime.md#rt-rte-direct-point"
            - "memory.md#mem-obj-capture-spool"
          note: "Complete remote commit consumption, generic direct-input control and full spool producers/readers are unresolved. The reports also retain imports, packs and other shipped writers/readers as an inspection frontier; no whole-system inventory is established."
      records:
        - "memory.md#mem-obj-session-turns"
        - "memory.md#mem-obj-derived-points"
        - "runtime.md#rt-rte-session-capture"
        - "runtime.md#rt-rte-production-commit"
        - "memory.md#mem-rte-checkpoint-diary"
        - "memory.md#mem-rte-dream-writeback"
        - "runtime.md#rt-rte-direct-point"
        - "memory.md#mem-obj-capture-spool"
      note: "Original source content, not graph Event serialization, establishes session-logs. Included opaque alternatives prevent exhaustive source classification."
---

# Tortoise memory profile

## Comparison rationale

This comparison classifies the accepted records, not the repository afresh. All positive findings are implementation-level wiring except the explicitly afforded diary read. There is no observed-operation or causal-benefit upgrade. Each axis remains partial because the included writer, maintenance and consumer inventory is incomplete, not because implementation evidence is intrinsically too weak to classify a route.

### Objects, derivation and control

Graph content, local backlog and optional journal/record projections are distinct retained surfaces. Record-capable session writes and graph-only source expansion do not establish restoration or retrieval parity. The relevant warrants are [MEM-OBJ-session-turns](memory.md#mem-obj-session-turns), [RT-OBJ-event-emission](runtime.md#rt-obj-event-emission) and [MEM-RTE-source-expansion](memory.md#mem-rte-source-expansion). Transient payload dictionaries and process-local numerical work are not additional accumulated-memory substrates.

Dense embeddings and fixed-rule numerical belief fields have different forms. The former encode distributed numerical representations; the latter have localized fields consumed by fixed code. Neither is a change to extraction-model weights. Known encoding/maintenance paths do not settle all initial provenance: [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model), [MEM-OBJ-belief-state](memory.md#mem-obj-belief-state) and [EPI-OBJ-belief-state](epistemic.md#epi-obj-belief-state).

Authored checkpoint/diary lineage does not establish manual admission. A generic caller may be human or computational. Conversely, starting capture does not make the ensuing software/model admission manual. These distinctions follow [MEM-RTE-checkpoint-diary](memory.md#mem-rte-checkpoint-diary), [RT-RTE-direct-point](runtime.md#rt-rte-direct-point) and [RT-RTE-session-capture](runtime.md#rt-rte-session-capture).

### Authority, transformation and trace learning

Conversation experience feeds a durable graph update, and retained graph priors enter gap review before that update. Those are learning-authority paths at the update consumer; selected output has knowledge authority at the later host model. They do not imply improved capacity or reliable factual acceptance: [MEM-OBJ-derived-points](memory.md#mem-obj-derived-points), [WF-RTE-gap-review](workflow.md#wf-rte-gap-review) and [RT-BAP-framework-block](runtime.md#rt-bap-framework-block).

The qualifying v2 route supports trace-learning yes and conversational session-log origin. Raw spool retention alone does not establish another qualifying learning route. Neither graph Event envelopes nor a model call establish additional original trace types: [MEM-OBJ-capture-spool](memory.md#mem-obj-capture-spool), [MEM-OBJ-session-turns](memory.md#mem-obj-session-turns) and [MEM-OBJ-derived-points](memory.md#mem-obj-derived-points). No accepted evidenced-absence record warrants a local trace-learning no; opaque alternatives remain unresolved rather than negative.

Checkpoint duplicate rejection, re-capture revision, tombstone withdrawal and correction promotion have identifiable implemented effects. Extracting standing graph content from retained session messages also supports wired consolidation: bounded/redacted turns pass through narrative, mapping and review into durable claims. This operation does not require proof of semantic faithfulness. The epistemic account's indeterminate truth-apt relation leaves novel claims and factual warrant unresolved, not consolidation unsupported. Possible extraction errors do not establish synthesis. The extraction unit remains partial for unresolved additional transformations, and opaque alternative extractors remain unresolved. Numerical maintenance is assessed separately: dream recomputation is not automatically decay or semantic revision. See [MEM-OBJ-derived-points](memory.md#mem-obj-derived-points), [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [WF-RTE-gap-review](workflow.md#wf-rte-gap-review), [EPI-OBJ-extracted-points](epistemic.md#epi-obj-extracted-points), and the other transformation records: [MEM-RTE-checkpoint-diary](memory.md#mem-rte-checkpoint-diary), [MEM-OBJ-session-turns](memory.md#mem-obj-session-turns), [MEM-RTE-point-retraction](memory.md#mem-rte-point-retraction), [EPI-RTE-review-integration](epistemic.md#epi-rte-review-integration) and [MEM-RTE-dream-writeback](memory.md#mem-rte-dream-writeback).

### Delivery and coverage

Automatic callback supply is push at the host boundary, while the memory service fulfills a request inside that chain. Source-session expansion is requested evaluation retrieval, not independent push or established live reflex delivery. The session-start digest's recency selection supports coarse push; the canonical pipeline's unresolved search internals prevent choosing lexical, embedding or judgment matching merely from its API name. Printed pointer IDs do not establish identifier matching: [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [MEM-RTE-hook-volunteer](memory.md#mem-rte-hook-volunteer), [MEM-RTE-start-digest](memory.md#mem-rte-start-digest) and [MEM-RTE-source-expansion](memory.md#mem-rte-source-expansion).

Lifecycle enforcement is consumer-specific. Canonical terminal exclusion does not cover the recent-session digest, whose inspected query lacks that predicate. No union of these findings means universal withdrawal. Likewise unknown complete remote commit consumption, spool producers and caller control prevent extrapolating one wired path across all admissions: [MEM-RTE-point-retraction](memory.md#mem-rte-point-retraction), [MEM-RTE-start-digest](memory.md#mem-rte-start-digest), [RT-RTE-production-commit](runtime.md#rt-rte-production-commit) and [MEM-OBJ-capture-spool](memory.md#mem-obj-capture-spool).

The supplied reconciliation supersedes the duplicate epistemic hook route with [MEM-RTE-hook-volunteer](memory.md#mem-rte-hook-volunteer), and the duplicate epistemic withdrawal route with [MEM-RTE-point-retraction](memory.md#mem-rte-point-retraction). This profile uses those canonical destinations. Their supplemental advisory-channel and message-invalidation findings do not create extra routes or stronger universal guarantees. Payload versus admitted content, overlapping belief fields and maintenance versus retention functions remain distinct; no other supersession changes a value.

Source-read log: none. No source ambiguity required inspection beyond the supplied accepted members.
