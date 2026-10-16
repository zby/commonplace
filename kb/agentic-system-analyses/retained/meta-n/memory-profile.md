---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Meta-n memory comparison: retained evaluated traces, intervention chains, search continuation and task-local summaries, with opaque SDK/cache alternatives."
run-id: "AAS-2026-10-14-meta-n-18c23b6f8bb4-01"
source-identity: "https://github.com/MinnesotaNLP/Meta-n"
reviewed-boundary: "b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8"
memory-comparison:
  version: 2
  scope: "Included: accumulated evaluated traces; retained preprocessing, Python/bash helpers and rationale; frozen winner maps; checkpoint/admission/access metadata; within-task continuation summaries; later proposal, solving, resume, test and diagnostic consumers. Included but unresolved: SDK conversation state, copied transcript payloads, adapter/evaluator caches and remaining diagnostic transformations, including optional analytical embeddings. Excluded: shipped static prompts/instructions, task datasets as static inputs, ordinary unsummarized invocation state, provider weights without an established in-scope update, and upstream SDK/provider implementations outside the frozen source."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Evaluated traces and persisted trace/source copies"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace"
              note: "Live Candidate.traces holds mutable trace objects."
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace"
              note: "Candidate trace JSON and source sidecars retain evaluated material."
          records:
            - "memory.md#mem-obj-trace"
          note: "Both live and disk substrates are identified for this object."
        -
          scope: "Retained preprocessing, Python/bash helpers, rationale and frozen maps"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-pre-process"
                - "memory.md#mem-obj-python-library"
                - "memory.md#mem-obj-bash-library"
                - "runtime.md#rt-obj-rationale"
                - "runtime.md#rt-obj-task-solution-map"
              note: "Live injection objects and merged mappings hold source and reasons."
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-rte-archive-resume"
                - "memory.md#mem-obj-python-library"
                - "memory.md#mem-obj-bash-library"
              note: "Injection JSON and source sidecars survive candidate trials and resume."
          records:
            - "runtime.md#rt-obj-pre-process"
            - "memory.md#mem-obj-python-library"
            - "memory.md#mem-obj-bash-library"
            - "runtime.md#rt-obj-rationale"
            - "runtime.md#rt-obj-task-solution-map"
            - "memory.md#mem-rte-archive-resume"
          note: "Source objects and their disk copies are covered; file encoding is not a database substrate."
        -
          scope: "Search checkpoint and reconstructed selection state"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint"
              note: "checkpoint.json persists control, RNG and admission metadata."
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-rte-archive-resume"
              note: "Resume reconstructs archive indexes and control state."
          records:
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-rte-archive-resume"
          note: "Checkpoint and candidate files are complementary retained objects."
        -
          scope: "Within-task derived prior-work summary"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-prior-summary"
              note: "Replacement message list retains summary across subsequent model invocations."
          records:
            - "memory.md#mem-obj-prior-summary"
            - "memory.md#mem-rte-context-compaction"
          note: "Task-local retention is established; no disk continuation of this summary is established."
        -
          scope: "Included SDK conversation state, copied log payloads, adapter/evaluator caches and remaining diagnostic transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-external-spine"
            - "memory.md#mem-rte-postrun-analysis"
          note: "These included alternatives lack inspected storage substrate facts. Readable archive traces and diagnostic pointers do not classify their opaque payloads or internal mechanisms."
      records:
        - "memory.md#mem-obj-trace"
        - "runtime.md#rt-obj-pre-process"
        - "memory.md#mem-obj-python-library"
        - "memory.md#mem-obj-bash-library"
        - "runtime.md#rt-obj-rationale"
        - "runtime.md#rt-obj-task-solution-map"
        - "memory.md#mem-rte-archive-resume"
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-obj-prior-summary"
        - "memory.md#mem-rte-context-compaction"
        - "runtime.md#rt-rte-external-spine"
        - "memory.md#mem-rte-postrun-analysis"
      note: "Files and in-memory objects are supported for the named archive and summary inventory. SDK/cache/diagnostic storage remains uninspected; no repo or vector substrate is inferred from repository ownership or an embedding mention."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Trace scripts, numeric/Boolean outcomes and access instrumentation"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace"
              note: "Scripts and outcome fields have fixed execution/comparison consumers."
          records:
            - "memory.md#mem-obj-trace"
          note: "This unit excludes model-interpreted reasoning and feedback."
        -
          scope: "Trace reasoning, output/error and evaluator-feedback displays"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace"
              note: "Selected textual displays enter later Ω interpretation."
          records:
            - "memory.md#mem-obj-trace"
            - "memory.md#mem-rte-omega-context"
          note: "Textual read-back is distinct from numeric ranking and script execution."
        -
          scope: "Preprocessing/helper/frozen source and checkpoint/index controls"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-pre-process"
                - "memory.md#mem-obj-python-library"
                - "memory.md#mem-obj-bash-library"
                - "runtime.md#rt-obj-task-solution-map"
                - "memory.md#mem-obj-checkpoint"
              note: "Python/bash, task-ID maps and JSON control fields have localized rules at executable/control consumers."
          records:
            - "runtime.md#rt-obj-pre-process"
            - "memory.md#mem-obj-python-library"
            - "memory.md#mem-obj-bash-library"
            - "runtime.md#rt-obj-task-solution-map"
            - "memory.md#mem-obj-checkpoint"
          note: "Fixed-rule execution and dispatch are separate from advertising text."
        -
          scope: "Recomputed preprocessing emissions and helper advertising derived from retained source"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-prompt-guidance"
                - "epistemic.md#epi-obj-additional-context"
              note: "Native or SDK model interprets additional context and helper signature/docstring guidance."
          records:
            - "runtime.md#rt-bap-prompt-guidance"
            - "epistemic.md#epi-obj-additional-context"
          note: "Consumption form is prose even though the retained producer is symbolic source."
        -
          scope: "Retained rationale and prior-work summary"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-rationale"
                - "memory.md#mem-obj-prior-summary"
              note: "Ω interprets selected rationale; later foreground turns interpret the summary."
          records:
            - "runtime.md#rt-obj-rationale"
            - "memory.md#mem-obj-prior-summary"
            - "memory.md#mem-rte-omega-context"
            - "memory.md#mem-rte-context-compaction"
          note: "Reasons and conversation compression are different objects with the same interpretation form."
        -
          scope: "Included SDK conversation state, copied log payloads, adapter/evaluator caches and remaining diagnostic transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-external-spine"
            - "memory.md#mem-rte-postrun-analysis"
          note: "These included alternatives lack inspected representational form facts. Readable archive traces and diagnostic pointers do not classify their opaque payloads or internal mechanisms."
      records:
        - "memory.md#mem-obj-trace"
        - "memory.md#mem-rte-omega-context"
        - "runtime.md#rt-obj-pre-process"
        - "memory.md#mem-obj-python-library"
        - "memory.md#mem-obj-bash-library"
        - "runtime.md#rt-obj-task-solution-map"
        - "memory.md#mem-obj-checkpoint"
        - "runtime.md#rt-bap-prompt-guidance"
        - "epistemic.md#epi-obj-additional-context"
        - "runtime.md#rt-obj-rationale"
        - "memory.md#mem-obj-prior-summary"
        - "memory.md#mem-rte-context-compaction"
        - "runtime.md#rt-rte-external-spine"
        - "memory.md#mem-rte-postrun-analysis"
      note: "Symbolic and natural-language routes are wired. Optional analytical embeddings and opaque SDK/cache payloads are not classified as parametric merely from their names; static provider weights are outside this accumulated-memory scope."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Evaluated traces and automatically generated intervention source/rationale"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace"
                - "runtime.md#rt-rte-chain-admission"
                - "memory.md#mem-rte-omega-context"
              note: "Task execution/scorer results are retained and feed subsequent model-generated interventions."
            -
              value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chain-admission"
                - "runtime.md#rt-obj-rationale"
              note: "Ω authors proposed source and rationale rather than only copying a raw transcript."
          records:
            - "memory.md#mem-obj-trace"
            - "runtime.md#rt-rte-chain-admission"
            - "memory.md#mem-rte-omega-context"
            - "runtime.md#rt-obj-rationale"
          note: "Trace derivation and model authorship coexist; generated claim fidelity and novelty remain unobserved."
        -
          scope: "Operator-selected seed helper content at import"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-rte-seed-import"
              note: "A supplied JSON file enters chain initialization."
          records:
            - "memory.md#mem-rte-seed-import"
          note: "Import is known, but upstream authorship and trace provenance are unresolved."
        -
          scope: "Frozen task-source map and search checkpoint"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-frozen-routing"
                - "memory.md#mem-obj-checkpoint"
              note: "Software assembles indexed winners and snapshots search metadata without a new Ω proposal."
          records:
            - "runtime.md#rt-rte-frozen-routing"
            - "memory.md#mem-obj-checkpoint"
          note: "These derivation paths are software compilation, not human-authored directions."
        -
          scope: "Prior-work summary derived from removed conversation"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-context-compaction"
              note: "Role-labelled removed turns feed automatic summary production."
          records:
            - "memory.md#mem-rte-context-compaction"
            - "memory.md#mem-obj-prior-summary"
          note: "Repeated compaction can include an earlier derived summary; this does not establish faithful compression."
        -
          scope: "Included SDK conversation state, copied log payloads, adapter/evaluator caches and remaining diagnostic transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-external-spine"
            - "memory.md#mem-rte-postrun-analysis"
          note: "These included alternatives lack inspected lineage facts. Readable archive traces and diagnostic pointers do not classify their opaque payloads or internal mechanisms."
      records:
        - "memory.md#mem-obj-trace"
        - "runtime.md#rt-rte-chain-admission"
        - "memory.md#mem-rte-omega-context"
        - "runtime.md#rt-obj-rationale"
        - "memory.md#mem-rte-seed-import"
        - "runtime.md#rt-rte-frozen-routing"
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-rte-context-compaction"
        - "memory.md#mem-obj-prior-summary"
        - "runtime.md#rt-rte-external-spine"
        - "memory.md#mem-rte-postrun-analysis"
      note: "Known derivation paths retain authored, imported, trace-extracted and other-compiled findings. Seed upstream provenance and opaque alternatives prevent complete lineage coverage."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Evaluated trace text and prior injections at Ω update consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chain-admission"
                - "memory.md#mem-rte-omega-context"
              note: "Retained evaluated experience and prior interventions feed production of durable behavior-shaping source/rationale."
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-omega-context"
                - "runtime.md#rt-obj-rationale"
              note: "Selected trace displays and retained reasons supply context and advice to Ω."
          records:
            - "runtime.md#rt-rte-chain-admission"
            - "memory.md#mem-rte-omega-context"
            - "runtime.md#rt-obj-rationale"
          note: "Learning force is local to the intervention update; no improved capacity or checked explanatory warrant is inferred."
        -
          scope: "Stored scores/success and check metadata at archive selection"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace"
                - "runtime.md#rt-rte-chain-admission"
                - "memory.md#mem-obj-python-library"
              note: "Scores/success and helper adoption metadata alter relative parent/best-index priority."
          records:
            - "memory.md#mem-obj-trace"
            - "runtime.md#rt-rte-chain-admission"
            - "memory.md#mem-obj-python-library"
          note: "Whole-candidate ranking and per-task-best bars are distinct consumers; bars do not remove history."
        -
          scope: "Retained best-index bars at resume and archive admission"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-rte-archive-resume"
              note: "Persisted barred task IDs determine admissibility to the per-task-best index."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-rte-archive-resume"
              note: "Union of checkpoint and candidate bars vetoes barred index promotion."
          records:
            - "memory.md#mem-rte-archive-resume"
            - "memory.md#mem-obj-checkpoint"
            - "runtime.md#rt-rte-helper-verification"
          note: "The veto concerns promotion, not all execution or truth endorsement; helper stamps remain conditional on trusted JSON."
        -
          scope: "Retained checkpoint/control state at resumed scheduler"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint"
              note: "Iteration, RNG and reconstructed archive state select continuation and subsequent work."
          records:
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-rte-archive-resume"
          note: "Deterministic scheduling authority is not a content truth criterion."
        -
          scope: "Frozen task-ID/source map at native solver dispatch"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-task-solution-map"
              note: "Matching task identity selects retained winning source and bypasses prompting/retries."
          records:
            - "runtime.md#rt-obj-task-solution-map"
            - "runtime.md#rt-rte-frozen-routing"
          note: "Native dispatch is wired; external parity and fresh score reproduction are not established."
        -
          scope: "Retained preprocessing rules and helper descriptions at solver/SDK guidance consumer"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-prompt-guidance"
              note: "Reused chain rules emit guidance and advertise helpers to native/SDK models."
          records:
            - "runtime.md#rt-obj-pre-process"
            - "runtime.md#rt-bap-prompt-guidance"
          note: "Standing chain guidance is model-interpreted; delivery does not establish compliance."
        -
          scope: "Prior-work summary at subsequent foreground model"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-context-compaction"
              note: "Summary supplies previous actions/outcomes as context for later task turns."
          records:
            - "memory.md#mem-rte-context-compaction"
            - "memory.md#mem-obj-prior-summary"
          note: "Unchecked context authority is not validation or a guaranteed factual account."
        -
          scope: "Executable helpers and trace scripts at execution consumer"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-bap-executable-injection"
            - "memory.md#mem-rte-test-readback"
          note: "Execution determines effects, but source availability or execution alone does not identify a controlled authority value for every arbitrary generated program. Permit/refuse, ranking or routing semantics of unsupplied helper bodies are unresolved."
        -
          scope: "Retained summaries/source at inspected diagnostic loaders"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-postrun-analysis"
              note: "Saved score/source material supplies evidence for post-run analysis."
          records:
            - "memory.md#mem-rte-postrun-analysis"
            - "epistemic.md#epi-rte-arm-report"
          note: "Advisory diagnostic consumption does not establish feedback into search."
        -
          scope: "Included SDK conversation state, copied log payloads, adapter/evaluator caches and remaining diagnostic transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-external-spine"
            - "memory.md#mem-rte-postrun-analysis"
          note: "These included alternatives lack inspected behavioral authority facts. Readable archive traces and diagnostic pointers do not classify their opaque payloads or internal mechanisms."
      records:
        - "runtime.md#rt-rte-chain-admission"
        - "memory.md#mem-rte-omega-context"
        - "runtime.md#rt-obj-rationale"
        - "memory.md#mem-obj-trace"
        - "memory.md#mem-obj-python-library"
        - "memory.md#mem-rte-archive-resume"
        - "memory.md#mem-obj-checkpoint"
        - "runtime.md#rt-rte-helper-verification"
        - "runtime.md#rt-obj-task-solution-map"
        - "runtime.md#rt-rte-frozen-routing"
        - "runtime.md#rt-obj-pre-process"
        - "runtime.md#rt-bap-prompt-guidance"
        - "memory.md#mem-rte-context-compaction"
        - "memory.md#mem-obj-prior-summary"
        - "runtime.md#rt-bap-executable-injection"
        - "memory.md#mem-rte-test-readback"
        - "memory.md#mem-rte-postrun-analysis"
        - "epistemic.md#epi-rte-arm-report"
        - "runtime.md#rt-rte-external-spine"
      note: "Known consumers establish learning, knowledge, ranking, validation, enforcement, routing and instruction locally. Arbitrary executable contents and uninspected diagnostic/SDK consumers prevent complete authority classification."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Trace capture, checkpoint/index writes and candidate admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace"
                - "memory.md#mem-obj-checkpoint"
                - "runtime.md#rt-rte-chain-admission"
                - "memory.md#mem-rte-archive-resume"
              note: "Software captures outcomes and decides admission/reconstruction without a per-content operator decision."
          records:
            - "memory.md#mem-obj-trace"
            - "memory.md#mem-obj-checkpoint"
            - "runtime.md#rt-rte-chain-admission"
            - "memory.md#mem-rte-archive-resume"
          note: "Starting or resuming search does not make these writes manual."
        -
          scope: "Ω generation and within/downstream repair admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chain-admission"
                - "runtime.md#rt-rte-within-refine"
                - "runtime.md#rt-rte-downstream-repair"
              note: "Model proposes content; software evaluates, filters or gates retention of new chains."
          records:
            - "runtime.md#rt-rte-chain-admission"
            - "runtime.md#rt-rte-within-refine"
            - "runtime.md#rt-rte-downstream-repair"
          note: "A non-improving downstream variant can still be archived; no per-change human approval is required."
        -
          scope: "Summary replacement and frozen winner assembly"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-context-compaction"
                - "runtime.md#rt-rte-frozen-routing"
              note: "Code triggers summary admission and deterministic winner-map assembly."
          records:
            - "memory.md#mem-rte-context-compaction"
            - "runtime.md#rt-rte-frozen-routing"
          note: "A provider return suffices for summary replacement; neither route requires per-artifact human approval."
        -
          scope: "CLI seed helper admission"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "memory.md#mem-rte-seed-import"
              note: "Explicit operator selection of a seed JSON file supplies retained helper content to initialization."
          records:
            - "memory.md#mem-rte-seed-import"
          note: "This classifies the content-supply decision, not authorship or function-by-function review; static software checks are additional constraints."
        -
          scope: "Included SDK conversation state, copied log payloads, adapter/evaluator caches and remaining diagnostic transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-external-spine"
            - "memory.md#mem-rte-postrun-analysis"
          note: "These included alternatives lack inspected write/admission control facts. Readable archive traces and diagnostic pointers do not classify their opaque payloads or internal mechanisms."
      records:
        - "memory.md#mem-obj-trace"
        - "memory.md#mem-obj-checkpoint"
        - "runtime.md#rt-rte-chain-admission"
        - "memory.md#mem-rte-archive-resume"
        - "runtime.md#rt-rte-within-refine"
        - "runtime.md#rt-rte-downstream-repair"
        - "memory.md#mem-rte-context-compaction"
        - "runtime.md#rt-rte-frozen-routing"
        - "memory.md#mem-rte-seed-import"
        - "runtime.md#rt-rte-external-spine"
        - "memory.md#mem-rte-postrun-analysis"
      note: "Automatic generation, repair, compaction and state capture coexist with manual seed supply. Opaque SDK/cache/diagnostic admissions remain unresolved."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Conversation-to-summary replacement"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-context-compaction"
              note: "Selected retained turns are compressed into a reduced prior-work account."
          records:
            - "memory.md#mem-rte-context-compaction"
            - "memory.md#mem-obj-prior-summary"
          note: "The implemented summary route is consolidation; lack of a fidelity check does not establish synthesis."
        -
          scope: "Helper overrides and repaired chain variants"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-python-library"
                - "memory.md#mem-obj-bash-library"
                - "runtime.md#rt-rte-within-refine"
                - "runtime.md#rt-rte-downstream-repair"
              note: "Same-name helper overrides and injection replacement revise a live entry in a new candidate."
          records:
            - "memory.md#mem-obj-python-library"
            - "memory.md#mem-obj-bash-library"
            - "runtime.md#rt-rte-within-refine"
            - "runtime.md#rt-rte-downstream-repair"
          note: "Old candidates remain intact; revision is local to the new merged organization."
        -
          scope: "Override-aware helper verification status"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-python-library"
              note: "Unverified same-name overrides clear prior live verification while old history persists."
          records:
            - "memory.md#mem-obj-python-library"
            - "runtime.md#rt-rte-helper-verification"
          note: "Only current reliance on the verification status is withdrawn, not the complete archived candidate."
        -
          scope: "Archive per-task-best promotion"
          assessment: "known"
          findings:
            -
              value: "promote"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace"
              note: "Success/score comparison replaces the indexed winner, raising its selection salience."
          records:
            - "memory.md#mem-obj-trace"
            - "runtime.md#rt-rte-chain-admission"
          note: "Promotion changes the access index, not historical retention or explanatory endorsement."
        -
          scope: "Winner-map assembly and inherited non-focus traces"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-frozen-routing"
              note: "Retained winners are selected and combined into a reduced dispatch map."
          records:
            - "runtime.md#rt-rte-frozen-routing"
            - "runtime.md#rt-obj-task-solution-map"
          note: "No new proposition or fresh evaluated score follows from deterministic assembly."
        -
          scope: "Ω-generated explanations and strategies"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-chain-admission"
            - "runtime.md#rt-rte-within-refine"
            - "runtime.md#rt-rte-downstream-repair"
          note: "Actual input/output content is unsupplied. Generation requests alone cannot distinguish consolidation from creation of a claim absent from its inputs; no synthesize finding follows."
        -
          scope: "Included SDK conversation state, copied log payloads, adapter/evaluator caches and remaining diagnostic transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-external-spine"
            - "memory.md#mem-rte-postrun-analysis"
          note: "These included alternatives lack inspected curation transformation facts. Readable archive traces and diagnostic pointers do not classify their opaque payloads or internal mechanisms."
      records:
        - "memory.md#mem-rte-context-compaction"
        - "memory.md#mem-obj-prior-summary"
        - "memory.md#mem-obj-python-library"
        - "memory.md#mem-obj-bash-library"
        - "runtime.md#rt-rte-within-refine"
        - "runtime.md#rt-rte-downstream-repair"
        - "runtime.md#rt-rte-helper-verification"
        - "memory.md#mem-obj-trace"
        - "runtime.md#rt-rte-chain-admission"
        - "runtime.md#rt-rte-frozen-routing"
        - "runtime.md#rt-obj-task-solution-map"
        - "runtime.md#rt-rte-external-spine"
        - "memory.md#mem-rte-postrun-analysis"
      note: "Consolidate, evolve, invalidate and promote have implemented witnesses. Budget eviction changes visibility, not durable decay; primary acquisition and reconstruction are not curation. Unresolved generated semantics and opaque alternatives prevent complete enumeration."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested Ω archive view, resume, test and diagnostic reads"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-omega-context"
                - "memory.md#mem-rte-archive-resume"
                - "memory.md#mem-rte-test-readback"
                - "memory.md#mem-rte-postrun-analysis"
              note: "Consumers request retained candidate material, continuation files or analysis inputs; code fulfills those requests."
          records:
            - "memory.md#mem-rte-omega-context"
            - "memory.md#mem-rte-archive-resume"
            - "memory.md#mem-rte-test-readback"
            - "memory.md#mem-rte-postrun-analysis"
          note: "Ω sampling is selected requested delivery, not an additional unsolicited push merely because software formats the return."
        -
          scope: "Reused chain guidance supplied to native/agentic/external solves"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-prompt-guidance"
              note: "Chain construction supplies retained preprocessing-derived guidance and helper advertising without a foreground model memory request."
          records:
            - "runtime.md#rt-obj-pre-process"
            - "runtime.md#rt-bap-prompt-guidance"
            - "runtime.md#rt-rte-external-spine"
          note: "Automatic context supply is distinct from a consumer asking for an archive view."
        -
          scope: "Summary supply on later foreground turns"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-context-compaction"
              note: "After automatic compaction the host places the retained summary in subsequent model messages."
          records:
            - "memory.md#mem-rte-context-compaction"
            - "memory.md#mem-obj-prior-summary"
          note: "Foreground does not request that summary; compaction code selects and supplies it."
        -
          scope: "Frozen matching source supplied for native task execution"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-frozen-routing"
              note: "Automatic task-ID dispatch supplies retained source in place of a new model solve."
          records:
            - "runtime.md#rt-rte-frozen-routing"
            - "runtime.md#rt-obj-task-solution-map"
          note: "The native shortcut is a targeted supply operation; explicit terminal test reads remain pull."
        -
          scope: "Included SDK conversation state, copied log payloads, adapter/evaluator caches and remaining diagnostic transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-external-spine"
            - "memory.md#mem-rte-postrun-analysis"
          note: "These included alternatives lack inspected read-back direction facts. Readable archive traces and diagnostic pointers do not classify their opaque payloads or internal mechanisms."
      records:
        - "memory.md#mem-rte-omega-context"
        - "memory.md#mem-rte-archive-resume"
        - "memory.md#mem-rte-test-readback"
        - "memory.md#mem-rte-postrun-analysis"
        - "runtime.md#rt-obj-pre-process"
        - "runtime.md#rt-bap-prompt-guidance"
        - "runtime.md#rt-rte-external-spine"
        - "memory.md#mem-rte-context-compaction"
        - "memory.md#mem-obj-prior-summary"
        - "runtime.md#rt-rte-frozen-routing"
        - "runtime.md#rt-obj-task-solution-map"
      note: "Both requested archive/file delivery and automatic chain/summary/frozen-source supply are supported. Uninspected SDK conversation and diagnostic alternatives prevent a complete direction inventory."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Automatic chain guidance push"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-prompt-guidance"
              note: "Trigger is a solve with a constructed candidate chain; selector input is chain availability/order and budget, selecting its preprocessing and helper guidance."
          records:
            - "runtime.md#rt-obj-pre-process"
            - "runtime.md#rt-bap-prompt-guidance"
            - "runtime.md#rt-rte-external-spine"
          note: "No recorded semantic query/embedding selector determines which retained guidance is supplied. Upstream candidate choice is not itself an identifier-match push."
        -
          scope: "Automatic summary push"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-context-compaction"
              note: "Context estimate triggers middle-message summarization; later turns receive the available summary with first message and verbatim tail."
          records:
            - "memory.md#mem-rte-context-compaction"
            - "memory.md#mem-obj-prior-summary"
          note: "Age/position and budget govern source selection; the summary model authors compression rather than performing an evidenced relevance selector."
        -
          scope: "Native frozen-source push"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-task-solution-map"
              note: "Trigger is native solve; current task_id matches map keys and selects the exact retained script delivered for execution."
          records:
            - "runtime.md#rt-obj-task-solution-map"
            - "runtime.md#rt-rte-frozen-routing"
          note: "This is an actual identity match selecting source, not merely an identifier on a requested file."
        -
          scope: "Requested Ω/resume/test/diagnostic material"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-omega-context"
            - "memory.md#mem-rte-archive-resume"
            - "memory.md#mem-rte-test-readback"
            - "memory.md#mem-rte-postrun-analysis"
          note: "These named operations are pull; the signal axis characterizes push selectors, not request identifiers."
        -
          scope: "Included SDK conversation state, copied log payloads, adapter/evaluator caches and remaining diagnostic transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-external-spine"
            - "memory.md#mem-rte-postrun-analysis"
          note: "These included alternatives lack inspected push-selection signal facts. Readable archive traces and diagnostic pointers do not classify their opaque payloads or internal mechanisms."
      records:
        - "runtime.md#rt-obj-pre-process"
        - "runtime.md#rt-bap-prompt-guidance"
        - "runtime.md#rt-rte-external-spine"
        - "memory.md#mem-rte-context-compaction"
        - "memory.md#mem-obj-prior-summary"
        - "runtime.md#rt-obj-task-solution-map"
        - "runtime.md#rt-rte-frozen-routing"
        - "memory.md#mem-rte-omega-context"
        - "memory.md#mem-rte-archive-resume"
        - "memory.md#mem-rte-test-readback"
        - "memory.md#mem-rte-postrun-analysis"
      note: "Coarse chain/summary supply and identifier-matched frozen dispatch are wired. Pull-only local units are inapplicable, but unresolved alternatives prevent an axis-wide inapplicable assessment."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Trace-fed Ω source/rationale generation and repairs"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chain-admission"
                - "runtime.md#rt-rte-within-refine"
                - "runtime.md#rt-rte-downstream-repair"
              note: "Automatic evaluated-trace-fed writes persist interventions with later Ω and solver consumers."
          records:
            - "runtime.md#rt-rte-chain-admission"
            - "runtime.md#rt-rte-within-refine"
            - "runtime.md#rt-rte-downstream-repair"
            - "memory.md#mem-rte-omega-context"
            - "memory.md#mem-rte-archive-resume"
          note: "This is wired artifact learning, not demonstrated benefit or model-weight training."
        -
          scope: "Automatic within-task continuation summary"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-context-compaction"
              note: "Recorded activity feeds automatic summary retention and a subsequent model invocation receives it as context."
          records:
            - "memory.md#mem-rte-context-compaction"
            - "memory.md#mem-obj-prior-summary"
          note: "Task-local retention qualifies; disk persistence and new knowledge are not required."
        -
          scope: "Automatic frozen winner-map assembly"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-frozen-routing"
              note: "Stored evaluated task experience feeds automatic retained source-map production with later native dispatch."
          records:
            - "runtime.md#rt-rte-frozen-routing"
            - "runtime.md#rt-obj-task-solution-map"
            - "memory.md#mem-obj-trace"
          note: "Deterministic compilation can shape durable behavior without a model proposal or fresh evaluation."
        -
          scope: "Seed helper upstream trace-fed production"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-seed-import"
          note: "Import itself is a manual supply decision; the record explicitly leaves prior experimentation and trace provenance unresolved. It cannot establish an upstream automatic trace-fed write or a local no finding."
        -
          scope: "Included SDK conversation state, copied log payloads, adapter/evaluator caches and remaining diagnostic transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-external-spine"
            - "memory.md#mem-rte-postrun-analysis"
          note: "These included alternatives lack inspected automatic trace-fed write and later-consumer chain facts. Readable archive traces and diagnostic pointers do not classify their opaque payloads or internal mechanisms."
      records:
        - "runtime.md#rt-rte-chain-admission"
        - "runtime.md#rt-rte-within-refine"
        - "runtime.md#rt-rte-downstream-repair"
        - "memory.md#mem-rte-omega-context"
        - "memory.md#mem-rte-archive-resume"
        - "memory.md#mem-rte-context-compaction"
        - "memory.md#mem-obj-prior-summary"
        - "runtime.md#rt-rte-frozen-routing"
        - "runtime.md#rt-obj-task-solution-map"
        - "memory.md#mem-obj-trace"
        - "memory.md#mem-rte-seed-import"
        - "runtime.md#rt-rte-external-spine"
        - "memory.md#mem-rte-postrun-analysis"
      note: "Positive trace-learning witnesses remain local. Manual import does not erase its unresolved upstream provenance; raw log retention, absent training calls and missing execution evidence do not establish a system-wide no."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Ω and repair consumption of task execution/scorer feedback"
          assessment: "known"
          findings:
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace"
                - "runtime.md#rt-rte-chain-admission"
                - "runtime.md#rt-rte-within-refine"
                - "runtime.md#rt-rte-downstream-repair"
              note: "Original evaluated execution requests/results and failures feed automatic retained intervention writes."
          records:
            - "memory.md#mem-obj-trace"
            - "runtime.md#rt-rte-chain-admission"
            - "runtime.md#rt-rte-within-refine"
            - "runtime.md#rt-rte-downstream-repair"
            - "memory.md#mem-rte-omega-context"
          note: "Trace displays can include reasoning and instrumentation but do not establish complete original session logs or linked state/action/outcome trajectories."
        -
          scope: "Compaction of solving conversation"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-context-compaction"
              note: "Recorded role-labelled model/action/observation turns enter the summarizer."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-agentic-loop"
              note: "Conversation includes executed code and execution feedback from the action/observation loop."
          records:
            - "memory.md#mem-rte-context-compaction"
            - "runtime.md#rt-rte-agentic-loop"
            - "memory.md#mem-obj-prior-summary"
          note: "Conversation and embedded execution feedback have distinct origins. A user-role wrapper does not turn them into event-streams."
        -
          scope: "Frozen winner-map compilation"
          assessment: "known"
          findings:
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-frozen-routing"
              note: "Evaluated task scripts and their outcome-index selection supply the retained winner map."
          records:
            - "runtime.md#rt-rte-frozen-routing"
            - "memory.md#mem-obj-trace"
            - "runtime.md#rt-obj-task-solution-map"
          note: "Indexed execution experience is the input; no linked multi-step trajectory format is established."
        -
          scope: "Seed upstream source and opaque external/diagnostic learning inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-seed-import"
            - "runtime.md#rt-rte-external-spine"
            - "memory.md#mem-rte-postrun-analysis"
          note: "Seed provenance, full SDK transcript payloads and remaining analytical update inputs are unresolved. Known tool-feedback views cannot establish all original source classes."
      records:
        - "memory.md#mem-obj-trace"
        - "runtime.md#rt-rte-chain-admission"
        - "runtime.md#rt-rte-within-refine"
        - "runtime.md#rt-rte-downstream-repair"
        - "memory.md#mem-rte-omega-context"
        - "memory.md#mem-rte-context-compaction"
        - "runtime.md#rt-rte-agentic-loop"
        - "memory.md#mem-obj-prior-summary"
        - "runtime.md#rt-rte-frozen-routing"
        - "runtime.md#rt-obj-task-solution-map"
        - "memory.md#mem-rte-seed-import"
        - "runtime.md#rt-rte-external-spine"
        - "memory.md#mem-rte-postrun-analysis"
      note: "Tool-traces and session-logs have qualifying write consumers. No event-streams or trajectories finding is inferred from telemetry timestamps, conversation serialization or the word trace; opaque and upstream inputs prevent complete source coverage."
---

# Meta-n memory profile

## Comparison rationale

The profile classifies accepted records, not new source evidence. All positive findings are wired implementation witnesses; no finding claims observed operation, faithful compaction, actual helper adoption, causal benefit or improved capacity. Partial coverage is not weak wiring: every axis preserves the known routes and the included unresolved alternatives.

The revision's reconciliation supersedes the epistemic Python/bash objects and prior-summary object with their memory counterparts, and the epistemic summary replacement route with memory's compaction route. This profile cites the canonical memory declarations. The valid runtime helper container and emitted-context part remain distinct. Supersession does not resolve the epistemic uncertainty about summary fidelity or the semantics of unsupplied generated claims.

The learning force of retained experience at Ω is separate from instruction/knowledge force at a later solver. Similarly, stored scores rank candidates, checkpoint state routes continuation, and persisted bars validate and veto best-index admission. Executable availability alone does not establish a permit/refuse criterion or every generated program's authority. Verification stamps retain their conditional runner/JSON warrant, rather than being upgraded into authenticated execution evidence.

Requested archive views are pull. Automatic supplies to subsequent solving invocations are push: chain guidance and continuation summaries use coarse availability/position/budget selection, while native frozen dispatch actually matches a task identifier to retained source. A requested file's identifier alone supplies no identifier-push finding. The Ω trace-sampling predicate therefore is not listed as another push merely because code returns a formatted view.

The summary's retention horizon is later invocations within one task, whereas intervention chains and maps survive trials and disk resume. Both support automatic trace-fed writes into behavior-shaping artifacts. Manual seed supply classifies the operator's explicit content-import decision, not human authorship, per-function approval, or a negative about its unknown upstream learning history. Tool execution feedback and recorded solving turns supply the supported trace origins; telemetry pointers do not reveal an opaque transcript's source or form.

Consolidation follows compression/selection of retained content, not the route name. Same-name overrides and repairs evolve a new candidate's organization; cleared verification status invalidates current reliance while history remains. Indexed winner replacement promotes selection salience. No actual generated claim establishes synthesis, and budget eviction from a request is not durable decay. The unresolved diagnostic, SDK and cache routes remain included instead of being dropped to obtain complete coverage.

Source-read log: none. No target source was read for this classification; all warrants come from supplied accepted records and their annotations, with duplicate identities resolved through the supplied reconciliation.
