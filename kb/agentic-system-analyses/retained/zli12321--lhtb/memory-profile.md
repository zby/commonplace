---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "LHTB memory comparison: derived continuation context, retained evaluation evidence and analysis, scheduling, artifact access and opaque alternatives."
run-id: "AAS-2026-10-15-lhtb-a0548ba4edbf-01"
source-identity: "https://github.com/zli12321/lhtb"
reviewed-boundary: "7ca0cacea9bf6a0694eaad7306bed794eaaaabce"
memory-comparison:
  version: 2
  scope: "Use-accumulated or revised Terminus-2 handoff/overflow context, provider conversation chains, retained workspace products, trajectories, outcomes/configuration, checkpoint snapshots, optional saved task-quality assessments, trial/job analysis caches, recovery/sweep selectors, viewer/export/upload routes and afforded adopted runtime replacements. Includes unresolved SDK/alternate-agent retention and remote downstream consumers. Excludes static shipped task/skill/MCP/prompt/rubric definitions as memory objects, fixed model weights not updated by inspected routes, task-local RAG/memory internals as general harness capabilities, independent Harbor training applications and external deployment internals beyond their exposed retention boundary. Initial provenance/control and remaining task-product details stay unresolved rather than being inferred from an inspected example."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Terminus-2 derived handoff text in local Chat and associated retained logs"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
                - "memory.md#mem-obj-handoff-context"
              note: "The replacement frame is retained in the process Chat for the next solver call."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-handoff-context"
                - "memory.md#mem-obj-trajectory"
              note: "Associated generated exchanges are retained in host trajectory/log files; references do not guarantee successful saves."
          records:
            - "runtime.md#rt-rte-context-handoff"
            - "memory.md#mem-obj-handoff-context"
            - "memory.md#mem-obj-trajectory"
          note: "Covers local handoff state and its logged representation, not the remote chain."
        - scope: "Host trajectory, checkpoint, saved result/configuration and trial/job analysis files"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-obj-process-reward"
                - "runtime.md#rt-obj-trial-result"
                - "memory.md#mem-obj-analysis"
                - "memory.md#mem-rte-trial-analysis"
              note: "JSON, JSONL and Markdown artifacts reside on host disk; JSON encoding does not imply a database substrate."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-obj-process-reward"
            - "runtime.md#rt-obj-trial-result"
            - "memory.md#mem-obj-analysis"
            - "memory.md#mem-rte-trial-analysis"
          note: "File-backed objects are separately identified by the accepted inventory."
        - scope: "Task workspace retained between commands/phases and optional saved task-quality output"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-terminal-actions"
                - "runtime.md#rt-rte-verifier-continuation"
                - "epistemic.md#epi-rte-task-check"
              note: "Workspace files persist in the environment; task-quality checking can save a JSON result."
          records:
            - "runtime.md#rt-rte-terminal-actions"
            - "runtime.md#rt-rte-verifier-continuation"
            - "epistemic.md#epi-rte-task-check"
          note: "No task-local database or memory-store substrate is inferred from the workspace container."
        - scope: "Terminus Responses conversation chain behind previous_response_id"
          assessment: "partial"
          findings:
            - value: "service-object"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-terminus-model"
              note: "The adapter delegates accumulated conversation state to the external Responses chain."
          records:
            - "runtime.md#rt-cmp-terminus-model"
          note: "Service-object describes the exposed retention boundary; underlying representation, storage and lifetime remain opaque."
        - scope: "Analysis SDK context, alternate-agent retention and remote upload platform internals"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-cmp-analysis-model"
            - "runtime.md#rt-rte-agent-dispatch"
            - "memory.md#mem-rte-artifact-access"
          note: "SDK/CLI state and remote persistence implementation are not inspected; no concrete backend database or vector substrate is licensed."
        - scope: "Version-specific replacement runtime module when maintained and adopted"
          assessment: "known"
          findings:
            - value: "files"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-runtime-patching"
                - "runtime.md#rt-bap-runtime-module"
              note: "The afforded maintenance recipe replaces an installed package file for future imports."
          records:
            - "runtime.md#rt-rte-runtime-patching"
            - "runtime.md#rt-bap-runtime-module"
          note: "This is a separate adoption path, not static shipped source counted as accumulated memory."
      records:
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-obj-handoff-context"
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-obj-process-reward"
        - "runtime.md#rt-obj-trial-result"
        - "memory.md#mem-obj-analysis"
        - "memory.md#mem-rte-trial-analysis"
        - "runtime.md#rt-rte-terminal-actions"
        - "runtime.md#rt-rte-verifier-continuation"
        - "epistemic.md#epi-rte-task-check"
        - "runtime.md#rt-cmp-terminus-model"
        - "memory.md#mem-cmp-analysis-model"
        - "runtime.md#rt-rte-agent-dispatch"
        - "memory.md#mem-rte-artifact-access"
        - "runtime.md#rt-rte-runtime-patching"
        - "runtime.md#rt-bap-runtime-module"
      note: "Files and process retention are resolved locally; the service boundary is known without its internals. SDK, alternate agents and remote platform internals prevent complete coverage."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Handoff payload as interpreted by the next task-solving model"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-handoff-context"
                - "runtime.md#rt-rte-context-handoff"
              note: "Summary, questions and answers supply interpreted prose rather than learned parameters."
          records:
            - "memory.md#mem-obj-handoff-context"
            - "runtime.md#rt-rte-context-handoff"
          note: "The local replacement payload is distinct from provider-side encoding."
        - scope: "Trajectory observations, model content and optional reasoning at inspection/analysis consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trial-analysis"
              note: "Narrative turns and observations are read interpretively."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trial-analysis"
          note: "Readable trajectory prose is not a description of opaque provider state."
        - scope: "Trajectory commands, metrics, session references and continuation filenames at fixed-code consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-artifact-access"
              note: "Export traversal and formatting follow localized JSON fields and filenames."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-artifact-access"
          note: "Separates fixed-code structural use from narrative interpretation."
        - scope: "Saved results/configuration and checkpoint fields at scheduling and metadata consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-trial-result"
                - "memory.md#mem-obj-process-reward"
                - "runtime.md#rt-rte-job-recovery"
                - "memory.md#mem-rte-sweep-selection"
              note: "Identity, reward, timing and configuration fields are parsed under fixed rules."
          records:
            - "runtime.md#rt-obj-trial-result"
            - "memory.md#mem-obj-process-reward"
            - "runtime.md#rt-rte-job-recovery"
            - "memory.md#mem-rte-sweep-selection"
          note: "Numerical scores used by fixed code are symbolic, not distributed-parametric."
        - scope: "Trial/job analysis summaries and explanations at aggregate/display consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-analysis"
                - "memory.md#mem-bap-analysis-guidance"
                - "epistemic.md#epi-rte-job-aggregation"
              note: "Summaries and check explanations reach a later model or operator as prose."
          records:
            - "memory.md#mem-obj-analysis"
            - "memory.md#mem-bap-analysis-guidance"
            - "epistemic.md#epi-rte-job-aggregation"
          note: "Retained reasons can be interpreted without establishing their correctness."
        - scope: "Structured analysis fields and optional task-quality result at parser/display consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-analysis"
                - "epistemic.md#epi-rte-analysis-cache"
                - "epistemic.md#epi-obj-analysis"
                - "epistemic.md#epi-rte-task-check"
              note: "Schema-shaped check outcomes and cache data are parsed and rendered by code."
          records:
            - "memory.md#mem-obj-analysis"
            - "epistemic.md#epi-rte-analysis-cache"
            - "epistemic.md#epi-obj-analysis"
            - "epistemic.md#epi-rte-task-check"
          note: "Form classification does not require a demonstrated later consumer of optional task-check output."
        - scope: "Inspected reconstruction product executed by its verifier"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-reconstruct"
                - "workflow.md#wf-rte-migration-grading"
              note: "Executable source and submitted project metadata enter fixed runtime/grader consumers."
          records:
            - "epistemic.md#epi-obj-reconstruct"
            - "workflow.md#wf-rte-migration-grading"
          note: "This resolves inspected product paths, not all possible workspace content."
        - scope: "Adopted version-specific replacement runtime code at future import"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-runtime-patching"
                - "runtime.md#rt-bap-runtime-module"
              note: "Executable Python controls future trial behavior after the afforded replacement."
          records:
            - "runtime.md#rt-rte-runtime-patching"
            - "runtime.md#rt-bap-runtime-module"
          note: "The future import consumer is distinct from natural-language patch guidance."
        - scope: "Opaque Responses/SDK payloads, alternate agents, remaining task-product forms and remote platform transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-terminus-model"
            - "memory.md#mem-cmp-analysis-model"
            - "runtime.md#rt-rte-agent-dispatch"
            - "runtime.md#rt-rte-terminal-actions"
            - "memory.md#mem-rte-artifact-access"
          note: "No internal form can be inferred from display summaries or transport identifiers; other workspace contents and export normalization are not exhaustively characterized."
      records:
        - "memory.md#mem-obj-handoff-context"
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-rte-trial-analysis"
        - "memory.md#mem-rte-artifact-access"
        - "runtime.md#rt-obj-trial-result"
        - "memory.md#mem-obj-process-reward"
        - "runtime.md#rt-rte-job-recovery"
        - "memory.md#mem-rte-sweep-selection"
        - "memory.md#mem-obj-analysis"
        - "memory.md#mem-bap-analysis-guidance"
        - "epistemic.md#epi-rte-job-aggregation"
        - "epistemic.md#epi-rte-analysis-cache"
        - "epistemic.md#epi-obj-analysis"
        - "epistemic.md#epi-rte-task-check"
        - "epistemic.md#epi-obj-reconstruct"
        - "workflow.md#wf-rte-migration-grading"
        - "runtime.md#rt-rte-runtime-patching"
        - "runtime.md#rt-bap-runtime-module"
        - "runtime.md#rt-cmp-terminus-model"
        - "memory.md#mem-cmp-analysis-model"
        - "runtime.md#rt-rte-agent-dispatch"
        - "runtime.md#rt-rte-terminal-actions"
      note: "Mixed local objects are split by part and consumer. Parametric model components are not themselves use-accumulated memory here; unknown provider encoding is not classified as parametric."
    lineage:
      assessment: "partial"
      units:
        - scope: "Generated handoff and shortened model-summary fallback derived from task interactions"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
                - "memory.md#mem-obj-handoff-context"
              note: "History, model turns and terminal observations feed automatic generated continuation context."
          records:
            - "runtime.md#rt-rte-context-handoff"
            - "memory.md#mem-obj-handoff-context"
          note: "Derivation from traces is established; semantic fidelity and every retained reason are not."
        - scope: "Raw/structured trajectories, saved outcomes and checkpoint snapshots"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-obj-process-reward"
                - "runtime.md#rt-obj-trial-result"
                - "memory.md#mem-rte-checkpoint-retention"
              note: "Recorded agent activity and verification outcomes supply these retained records and copies."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-obj-process-reward"
            - "runtime.md#rt-obj-trial-result"
            - "memory.md#mem-rte-checkpoint-retention"
          note: "Recording and copying need not qualify as trace learning to have trace-derived lineage."
        - scope: "Trial assessments and job narratives derived from recorded work and prior assessments"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trial-analysis"
                - "memory.md#mem-obj-analysis"
                - "epistemic.md#epi-rte-job-aggregation"
              note: "Trial evidence feeds model interpretation; summaries/checks then feed narrative aggregation."
          records:
            - "memory.md#mem-rte-trial-analysis"
            - "memory.md#mem-obj-analysis"
            - "epistemic.md#epi-rte-job-aggregation"
          note: "Source asks for file reads; wired derivation does not prove complete evidence consumption."
        - scope: "Task/workspace content imported through declared verifier artifact transfer"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "workflow.md#wf-rte-migration-grading"
                - "runtime.md#rt-rte-verifier-execution"
              note: "The verifier imports selected project artifacts from the solver environment, not the entire environment."
          records:
            - "workflow.md#wf-rte-migration-grading"
            - "runtime.md#rt-rte-verifier-execution"
          note: "This is a transfer path, not a claim about how each original file was created."
        - scope: "Model-command revision of retained task workspace"
          assessment: "partial"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-terminal-actions"
              note: "Model-selected terminal commands can author and revise workspace content."
          records:
            - "runtime.md#rt-rte-terminal-actions"
            - "runtime.md#rt-rte-verifier-continuation"
          note: "The actual initial content and derivation of arbitrary workload files are not resolved by the editing capability."
        - scope: "Optional task-quality assessment from static task inputs"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-task-check"
                - "epistemic.md#epi-obj-analysis"
              note: "A computational rubric assessment derives from task files rather than a qualifying trace source."
          records:
            - "epistemic.md#epi-rte-task-check"
            - "epistemic.md#epi-obj-analysis"
          note: "Model-produced judgment is separate from trace-derived trial analysis."
        - scope: "Installed replacement module supplied by the version-specific recipe"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-runtime-patching"
              note: "The afforded recipe copies the provided replacement module into an installation."
          records:
            - "runtime.md#rt-rte-runtime-patching"
          note: "Manual porting/edit history and actual adoption are not established by this copy route."
        - scope: "Initial/adopted content provenance beyond inspected paths, remote/SDK chains, alternate-agent memory and remote transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-terminus-model"
            - "memory.md#mem-cmp-analysis-model"
            - "runtime.md#rt-rte-agent-dispatch"
            - "memory.md#mem-rte-artifact-access"
            - "runtime.md#rt-rte-runtime-patching"
          note: "The reports do not resolve initial authorship, provider compaction or every export/maintenance derivation; known local paths do not settle them."
      records:
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-obj-handoff-context"
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-obj-process-reward"
        - "runtime.md#rt-obj-trial-result"
        - "memory.md#mem-rte-checkpoint-retention"
        - "memory.md#mem-rte-trial-analysis"
        - "memory.md#mem-obj-analysis"
        - "epistemic.md#epi-rte-job-aggregation"
        - "workflow.md#wf-rte-migration-grading"
        - "runtime.md#rt-rte-verifier-execution"
        - "runtime.md#rt-rte-terminal-actions"
        - "runtime.md#rt-rte-verifier-continuation"
        - "epistemic.md#epi-rte-task-check"
        - "epistemic.md#epi-obj-analysis"
        - "runtime.md#rt-rte-runtime-patching"
        - "runtime.md#rt-cmp-terminus-model"
        - "memory.md#mem-cmp-analysis-model"
        - "runtime.md#rt-rte-agent-dispatch"
        - "memory.md#mem-rte-artifact-access"
      note: "Trace-derived handoffs and analysis coexist with authored work products and imported submissions. Unknown initialization and opaque transformations prevent a complete lineage inventory."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Interaction history at automatic handoff update consumer"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
                - "memory.md#mem-obj-handoff-context"
              note: "Retained experience feeds a durable replacement context consumed by a later foreground invocation."
          records:
            - "runtime.md#rt-rte-context-handoff"
            - "memory.md#mem-obj-handoff-context"
          note: "Learning authority at the update consumer does not assert improved capacity."
        - scope: "Handoff findings and continuation directions at later solver"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-handoff-context"
                - "runtime.md#rt-rte-context-handoff"
              note: "Historical findings/status supply context for subsequent solving."
            - value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
                - "runtime.md#rt-bap-task-guidance"
              note: "The handoff asks the later solver to continue prior work through its replacement prompt."
          records:
            - "memory.md#mem-obj-handoff-context"
            - "runtime.md#rt-rte-context-handoff"
            - "runtime.md#rt-bap-task-guidance"
          note: "Guidance is interpretive, not a symbolic compliance guarantee."
        - scope: "Saved configurations/outcomes at job recovery scheduler"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-job-recovery"
                - "runtime.md#rt-obj-trial-result"
              note: "Completed trial matches select which work remains."
            - value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-job-recovery"
              note: "Saved configuration is the equality reference for admissible job recovery."
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-job-recovery"
              note: "A changed job configuration is refused and unmatched trials cause errors."
          records:
            - "runtime.md#rt-rte-job-recovery"
            - "runtime.md#rt-obj-trial-result"
          note: "These forces belong to retained scheduler references, not a model answer oracle."
        - scope: "Saved result reward at sweep successor selection"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-rte-sweep-selection"
              note: "The inspected >0 predicate removes qualifying successful tasks from subsequent sweeps."
          records:
            - "memory.md#mem-rte-sweep-selection"
          note: "Code-level route is wired; singular reward-key compatibility and actual filtering remain unresolved."
        - scope: "Trial evidence at the automatic analysis update consumer"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trial-analysis"
                - "memory.md#mem-obj-analysis"
                - "epistemic.md#epi-rte-job-aggregation"
              note: "Recorded work feeds automatic durable analysis whose explanations shape subsequent aggregation."
          records:
            - "memory.md#mem-rte-trial-analysis"
            - "memory.md#mem-obj-analysis"
            - "epistemic.md#epi-rte-job-aggregation"
          note: "This update-consumer force does not establish improved capacity."
        - scope: "Retained analysis summaries/check explanations at the aggregate model and operator consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-bap-analysis-guidance"
                - "memory.md#mem-obj-analysis"
              note: "Persisted explanations provide interpretive evidence/context to the aggregation model and operators."
          records:
            - "memory.md#mem-rte-trial-analysis"
            - "memory.md#mem-obj-analysis"
            - "epistemic.md#epi-rte-job-aggregation"
            - "memory.md#mem-bap-analysis-guidance"
          note: "No scored reward withdrawal, solver adoption or epistemic certification follows."
        - scope: "Analysis cache state at later analyzer"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-analysis-cache"
                - "memory.md#mem-rte-trial-analysis"
              note: "Existing parseable analysis with overwrite false selects cached return and can skip reanalysis."
          records:
            - "epistemic.md#epi-rte-analysis-cache"
            - "memory.md#mem-rte-trial-analysis"
          note: "The static schema is not counted as retained learned validation policy."
        - scope: "Trajectory narrative at the file-inspecting model/operator"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trial-analysis"
                - "memory.md#mem-rte-artifact-access"
              note: "Read trajectory content supplies evidence for interpretation."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trial-analysis"
            - "memory.md#mem-rte-artifact-access"
          note: "This interpretive evidence path is distinct from structural export traversal."
        - scope: "Retained trajectory continuation references at the exporter"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-artifact-access"
              note: "Retained continued_trajectory_ref selects the next continuation file during traversal."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trial-analysis"
            - "memory.md#mem-rte-artifact-access"
          note: "No training authority is inferred from export formatting."
        - scope: "Inspected task product at later verifier execution"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-obj-reconstruct"
            - "workflow.md#wf-rte-migration-grading"
          note: "The records establish execution of retained workload source and checking its outputs, but do not establish that this retained part supplies a permission veto, selection rule, criterion or other controlled authority at that consumer. Executable form alone does not establish enforcement."
        - scope: "Adopted replacement module at future Harbor control consumer"
          assessment: "known"
          findings:
            - value: "enforcement"
              basis: "afforded"
              records:
                - "runtime.md#rt-bap-runtime-module"
                - "runtime.md#rt-rte-runtime-patching"
              note: "Executable replacement controls grading hardening and continuation policy."
            - value: "routing"
              basis: "afforded"
              records:
                - "runtime.md#rt-bap-runtime-module"
                - "runtime.md#rt-rte-runtime-patching"
              note: "Replacement phase logic directs future scheduling and feedback branches."
          records:
            - "runtime.md#rt-bap-runtime-module"
            - "runtime.md#rt-rte-runtime-patching"
          note: "This authority is afforded after installation, not observed deployment."
        - scope: "Hidden checkpoint file reload, optional saved task-quality output, opaque provider/SDK and alternate-agent consumers, remote platform consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-checkpoint-retention"
            - "epistemic.md#epi-rte-task-check"
            - "runtime.md#rt-cmp-terminus-model"
            - "memory.md#mem-cmp-analysis-model"
            - "runtime.md#rt-rte-agent-dispatch"
            - "memory.md#mem-rte-artifact-access"
          note: "Checkpoint live-return control is not file read-back. These later retained-payload consumers are unresolved, preventing authority classifications for them."
      records:
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-obj-handoff-context"
        - "runtime.md#rt-bap-task-guidance"
        - "runtime.md#rt-rte-job-recovery"
        - "runtime.md#rt-obj-trial-result"
        - "memory.md#mem-rte-sweep-selection"
        - "memory.md#mem-rte-trial-analysis"
        - "memory.md#mem-obj-analysis"
        - "epistemic.md#epi-rte-job-aggregation"
        - "memory.md#mem-bap-analysis-guidance"
        - "epistemic.md#epi-rte-analysis-cache"
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-rte-artifact-access"
        - "epistemic.md#epi-obj-reconstruct"
        - "workflow.md#wf-rte-migration-grading"
        - "runtime.md#rt-bap-runtime-module"
        - "runtime.md#rt-rte-runtime-patching"
        - "memory.md#mem-rte-checkpoint-retention"
        - "epistemic.md#epi-rte-task-check"
        - "runtime.md#rt-cmp-terminus-model"
        - "memory.md#mem-cmp-analysis-model"
        - "runtime.md#rt-rte-agent-dispatch"
      note: "The inventory separates update-consumer learning from downstream knowledge/instruction and scheduler control. Opaque and unestablished consumers remain included; no ranking finding follows merely from numerical rewards."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Handoff and fallback generated-content admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
                - "memory.md#mem-obj-handoff-context"
              note: "Code installs model-produced handoff/fallback context without per-content human approval."
          records:
            - "runtime.md#rt-rte-context-handoff"
            - "memory.md#mem-obj-handoff-context"
          note: "Launching a task is not manual admission of later handoff text."
        - scope: "Workspace edits and host trajectory/result/checkpoint recording"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-terminal-actions"
                - "memory.md#mem-obj-trajectory"
                - "runtime.md#rt-obj-trial-result"
                - "memory.md#mem-rte-checkpoint-retention"
              note: "Parsed commands mutate the workspace; software records activity and outcomes without a per-content operator gate."
          records:
            - "runtime.md#rt-rte-terminal-actions"
            - "memory.md#mem-obj-trajectory"
            - "runtime.md#rt-obj-trial-result"
            - "memory.md#mem-rte-checkpoint-retention"
          note: "Model authorship and physical file writes are not separate human admission decisions."
        - scope: "Trial/job analysis and optional task-check result admission or overwrite"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trial-analysis"
                - "epistemic.md#epi-rte-analysis-cache"
                - "epistemic.md#epi-rte-job-aggregation"
                - "epistemic.md#epi-rte-task-check"
              note: "Schema-valid model results are saved by software; overwrite requests do not supply per-generated-content approval."
          records:
            - "memory.md#mem-rte-trial-analysis"
            - "epistemic.md#epi-rte-analysis-cache"
            - "epistemic.md#epi-rte-job-aggregation"
            - "epistemic.md#epi-rte-task-check"
          note: "Structural validation does not make the admission manual."
        - scope: "Configured trial-end streaming upload admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-artifact-access"
              note: "A configured END hook can upload completed trial material without a later per-trial user decision."
          records:
            - "memory.md#mem-rte-artifact-access"
          note: "The hook establishes this admission mechanism independently of generic explicit uploader callers."
        - scope: "Initial content, explicit export/upload caller control and installed runtime replacement admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-artifact-access"
            - "runtime.md#rt-rte-runtime-patching"
            - "runtime.md#rt-rte-agent-dispatch"
            - "runtime.md#rt-obj-task-instruction"
          note: "Generic caller or maintenance-actor identity does not establish an explicit human content decision. No manual finding is licensed."
        - scope: "Provider/SDK and alternate-agent internal writes"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-terminus-model"
            - "memory.md#mem-cmp-analysis-model"
            - "runtime.md#rt-rte-agent-dispatch"
          note: "Internal admission and mutation policies remain uninspected."
      records:
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-obj-handoff-context"
        - "runtime.md#rt-rte-terminal-actions"
        - "memory.md#mem-obj-trajectory"
        - "runtime.md#rt-obj-trial-result"
        - "memory.md#mem-rte-checkpoint-retention"
        - "memory.md#mem-rte-trial-analysis"
        - "epistemic.md#epi-rte-analysis-cache"
        - "epistemic.md#epi-rte-job-aggregation"
        - "epistemic.md#epi-rte-task-check"
        - "memory.md#mem-rte-artifact-access"
        - "runtime.md#rt-rte-runtime-patching"
        - "runtime.md#rt-rte-agent-dispatch"
        - "runtime.md#rt-obj-task-instruction"
        - "runtime.md#rt-cmp-terminus-model"
        - "memory.md#mem-cmp-analysis-model"
      note: "Known automatic admission survives unresolved initialization and maintenance control. The reports do not support conflating caller initiation with manual curation."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Successful three-call summary/questions/answers handoff and short model-summary fallback"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
                - "memory.md#mem-obj-handoff-context"
              note: "The implemented model-mediated compression selects historical actions, findings and status into reduced continuation context."
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
                - "memory.md#mem-obj-handoff-context"
              note: "Successful full handoff revises the active retained context by installing a replacement frame."
          records:
            - "runtime.md#rt-rte-context-handoff"
            - "memory.md#mem-obj-handoff-context"
          note: "No semantic fidelity guarantee follows; short fallback is not assumed to perform the same complete replacement."
        - scope: "Reactive trimming of retained Chat before retry/handoff"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
              note: "Most recent turn pairs are removed from active retained context under overflow recovery."
          records:
            - "runtime.md#rt-rte-context-handoff"
          note: "Local forgetting does not prove deletion of trajectories or provider copies; plain terminal-output filtering alone is not counted as retained-memory curation."
        - scope: "Automatic revisions of retained task workspace"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-terminal-actions"
                - "runtime.md#rt-rte-verifier-continuation"
              note: "Later model commands can revise prior retained workspace state during repair."
          records:
            - "runtime.md#rt-rte-terminal-actions"
            - "runtime.md#rt-rte-verifier-continuation"
          note: "A task-product capability is not autonomous improvement of the harness."
        - scope: "Tool-less job aggregation over retained trial summaries/check explanations"
          assessment: "partial"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-job-aggregation"
                - "memory.md#mem-rte-trial-analysis"
                - "memory.md#mem-obj-analysis"
              note: "The implemented aggregate route combines retained per-trial interpretation into a job narrative."
          records:
            - "epistemic.md#epi-rte-job-aggregation"
            - "memory.md#mem-rte-trial-analysis"
            - "memory.md#mem-obj-analysis"
          note: "Additional assertions or exact semantic preservation are not established; synthesize is not inferred from model generation alone."
        - scope: "Trial interpretation and task-quality model judgments as semantic transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-trial-analysis"
            - "epistemic.md#epi-rte-task-check"
            - "epistemic.md#epi-rte-trial-analysis"
          note: "Records leave the content relation indeterminate; no particular new claim or entailment establishes synthesis rather than interpretation."
        - scope: "Opaque provider/SDK compaction, alternate-agent maintenance, remote normalization and maintenance-actor edits"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-terminus-model"
            - "memory.md#mem-cmp-analysis-model"
            - "runtime.md#rt-rte-agent-dispatch"
            - "memory.md#mem-rte-artifact-access"
            - "runtime.md#rt-rte-runtime-patching"
          note: "Unknown transformations prevent a complete operations inventory. Upload trial-ID skipping is not near-duplicate memory merging."
      records:
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-obj-handoff-context"
        - "runtime.md#rt-rte-terminal-actions"
        - "runtime.md#rt-rte-verifier-continuation"
        - "epistemic.md#epi-rte-job-aggregation"
        - "memory.md#mem-rte-trial-analysis"
        - "memory.md#mem-obj-analysis"
        - "epistemic.md#epi-rte-task-check"
        - "epistemic.md#epi-rte-trial-analysis"
        - "runtime.md#rt-cmp-terminus-model"
        - "memory.md#mem-cmp-analysis-model"
        - "runtime.md#rt-rte-agent-dispatch"
        - "memory.md#mem-rte-artifact-access"
        - "runtime.md#rt-rte-runtime-patching"
      note: "Implemented reduction and revision are positive local operations. Acquisition, index/format conversion, cache reuse and primary-key upload checks alone establish none; unresolved semantic and opaque branches prevent exhaustive classification."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Automatic retained context selection and supply on the handoff/recovery path"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
                - "memory.md#mem-obj-handoff-context"
              note: "Threshold/overflow code supplies reduced historical context to the later foreground call without that consumer requesting retrieval."
          records:
            - "runtime.md#rt-rte-context-handoff"
            - "memory.md#mem-obj-handoff-context"
          note: "Full replacement and prompts submitted through unwound Chat remain distinct forms of recovery."
        - scope: "Model-selected later file reads of workspace or analysis evidence"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-terminal-actions"
                - "memory.md#mem-rte-trial-analysis"
                - "memory.md#mem-obj-trajectory"
              note: "The consumer selects file reads; fulfilling them is requested delivery, not another push."
          records:
            - "runtime.md#rt-rte-terminal-actions"
            - "memory.md#mem-rte-trial-analysis"
            - "memory.md#mem-obj-trajectory"
          note: "The route is wired; actual analysis file choices and complete evidence reading are unobserved."
        - scope: "Job recovery, outcome-driven sweep selection and cache-to-aggregate construction"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-job-recovery"
                - "memory.md#mem-rte-sweep-selection"
                - "memory.md#mem-rte-trial-analysis"
                - "epistemic.md#epi-rte-job-aggregation"
              note: "Host code automatically uses retained configurations/outcomes or selected summary/check fields to determine or supply later work."
          records:
            - "runtime.md#rt-rte-job-recovery"
            - "memory.md#mem-rte-sweep-selection"
            - "memory.md#mem-rte-trial-analysis"
            - "epistemic.md#epi-rte-job-aggregation"
          note: "An upstream request to run/resume/analyze does not itself request every automatically selected retained part."
        - scope: "Explicit viewer/export/upload access versus configured streaming upload"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-artifact-access"
              note: "Explicit artifact access serves the caller-selected trial/step/export request."
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-artifact-access"
              note: "Configured trial-end hook independently sends retained trial material to upload."
          records:
            - "memory.md#mem-rte-artifact-access"
          note: "Requested export traversal is a suboperation of fulfilling that request, not independently counted as unsolicited delivery."
        - scope: "Version-specific installation followed by a later runtime import"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-runtime-patching"
                - "runtime.md#rt-bap-runtime-module"
              note: "Future Harbor import requests the installed module selected by the installation."
          records:
            - "runtime.md#rt-rte-runtime-patching"
            - "runtime.md#rt-bap-runtime-module"
          note: "The maintenance replacement decision is not reclassified as a read."
        - scope: "Hidden checkpoint file reload, optional task-check output reader, provider/SDK and alternate-agent later consumption, remote platform consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-checkpoint-retention"
            - "epistemic.md#epi-rte-task-check"
            - "runtime.md#rt-cmp-terminus-model"
            - "memory.md#mem-cmp-analysis-model"
            - "runtime.md#rt-rte-agent-dispatch"
            - "memory.md#mem-rte-artifact-access"
          note: "Retention or access paths alone do not establish an additional later read-back operation for these branches."
      records:
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-obj-handoff-context"
        - "runtime.md#rt-rte-terminal-actions"
        - "memory.md#mem-rte-trial-analysis"
        - "memory.md#mem-obj-trajectory"
        - "runtime.md#rt-rte-job-recovery"
        - "memory.md#mem-rte-sweep-selection"
        - "epistemic.md#epi-rte-job-aggregation"
        - "memory.md#mem-rte-artifact-access"
        - "runtime.md#rt-rte-runtime-patching"
        - "runtime.md#rt-bap-runtime-module"
        - "memory.md#mem-rte-checkpoint-retention"
        - "epistemic.md#epi-rte-task-check"
        - "runtime.md#rt-cmp-terminus-model"
        - "memory.md#mem-cmp-analysis-model"
        - "runtime.md#rt-rte-agent-dispatch"
      note: "Pull and push coexist at distinct request/selection operations. Opaque alternatives and retained objects with no established later reader prevent complete direction coverage."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Handoff/recovery automatic selection of retained history and generated continuation payload"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
              note: "Token threshold or overflow triggers positional/size selection of history and screen tail."
            - value: "inferred-judgment"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
                - "memory.md#mem-obj-handoff-context"
              note: "At that trigger the summarizing model selects historical actions/findings for the delivered handoff."
          records:
            - "runtime.md#rt-rte-context-handoff"
            - "memory.md#mem-obj-handoff-context"
          note: "Trigger, code selection and model content choice are distinct; no identifier or embedding targeting is established."
        - scope: "Automatic completed-result recovery selection"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-job-recovery"
                - "runtime.md#rt-obj-trial-result"
              note: "At restart, exact saved/planned configuration matching identifies completed trials and therefore remaining work."
          records:
            - "runtime.md#rt-rte-job-recovery"
            - "runtime.md#rt-obj-trial-result"
          note: "This is an actual retained-result identity comparison, not an identifier on a requested file alone."
        - scope: "Automatic sweep successor selection from saved outcomes"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-sweep-selection"
              note: "At each later sweep, qualifying reward and task identity select tasks to exclude from the next job."
          records:
            - "memory.md#mem-rte-sweep-selection"
          note: "The >0 reward condition accompanies identity selection; singular reward-field compatibility remains unresolved."
        - scope: "Automatic cache/field supply to aggregation"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trial-analysis"
                - "epistemic.md#epi-rte-analysis-cache"
                - "epistemic.md#epi-rte-job-aggregation"
              note: "On selected job analysis, cache availability/overwrite and successful trial analyses govern supply; code selects summary/check fields, not semantic relevance."
          records:
            - "memory.md#mem-rte-trial-analysis"
            - "epistemic.md#epi-rte-analysis-cache"
            - "epistemic.md#epi-rte-job-aggregation"
          note: "Trial names in aggregation input are not evidence of identity-targeted semantic retrieval."
        - scope: "Configured END-hook upload of a completed trial"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-artifact-access"
              note: "Trial completion triggers supply of the current trial package; availability and already-uploaded-ID suppression qualify admission."
          records:
            - "memory.md#mem-rte-artifact-access"
          note: "No identity match selects particular delivered content; duplicate-upload veto is not an identifier-based retrieval witness."
        - scope: "Explicit file/viewer/export requests and later replacement-module import"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-terminal-actions"
            - "memory.md#mem-rte-trial-analysis"
            - "memory.md#mem-rte-artifact-access"
            - "runtime.md#rt-rte-runtime-patching"
            - "runtime.md#rt-bap-runtime-module"
          note: "These named operations are pull; their paths and continuation references do not independently establish a push signal."
        - scope: "Provider/SDK and alternate-agent selection, remote downstream supply and unestablished checkpoint/task-check readers"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-terminus-model"
            - "memory.md#mem-cmp-analysis-model"
            - "runtime.md#rt-rte-agent-dispatch"
            - "memory.md#mem-rte-artifact-access"
            - "memory.md#mem-rte-checkpoint-retention"
            - "epistemic.md#epi-rte-task-check"
          note: "Unknown direction/selector facts cannot be converted to inapplicability from the known pull routes."
      records:
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-obj-handoff-context"
        - "runtime.md#rt-rte-job-recovery"
        - "runtime.md#rt-obj-trial-result"
        - "memory.md#mem-rte-sweep-selection"
        - "memory.md#mem-rte-trial-analysis"
        - "epistemic.md#epi-rte-analysis-cache"
        - "epistemic.md#epi-rte-job-aggregation"
        - "memory.md#mem-rte-artifact-access"
        - "runtime.md#rt-rte-terminal-actions"
        - "runtime.md#rt-rte-runtime-patching"
        - "runtime.md#rt-bap-runtime-module"
        - "runtime.md#rt-cmp-terminus-model"
        - "memory.md#mem-cmp-analysis-model"
        - "runtime.md#rt-rte-agent-dispatch"
        - "memory.md#mem-rte-checkpoint-retention"
        - "epistemic.md#epi-rte-task-check"
      note: "Positive selectors are attached only to actual push operations, with triggers and selected parts. Unknown alternatives prevent complete signal coverage."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Automatic handoff and generated short-summary continuation write to later foreground model"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
                - "memory.md#mem-obj-handoff-context"
              note: "Interaction traces produce retained behavior-shaping context automatically consumed by a later solver invocation."
          records:
            - "runtime.md#rt-rte-context-handoff"
            - "memory.md#mem-obj-handoff-context"
          note: "The profile definition includes this within-run durable handoff without requiring new knowledge, weight change or improved performance."
        - scope: "Automatic persisted trial analysis and aggregate narrative chain"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trial-analysis"
                - "memory.md#mem-obj-analysis"
                - "epistemic.md#epi-rte-job-aggregation"
                - "memory.md#mem-bap-analysis-guidance"
              note: "Trace-fed explanations persist and reach the subsequent aggregation model; cached analysis can also reach later analysis commands."
          records:
            - "memory.md#mem-rte-trial-analysis"
            - "memory.md#mem-obj-analysis"
            - "epistemic.md#epi-rte-job-aggregation"
            - "memory.md#mem-bap-analysis-guidance"
          note: "This is an interpretation route, not demonstrated improvement of the task solver or a training pipeline."
        - scope: "Optional task-quality assessment from static inputs"
          assessment: "inapplicable"
          findings: []
          records:
            - "epistemic.md#epi-rte-task-check"
          note: "This named route consumes task files/rubric rather than recorded activity; no qualifying trace-fed update is established by its static-input scope."
        - scope: "Raw trajectory/outcome/checkpoint retention and exports as further learning routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-trajectory"
            - "runtime.md#rt-obj-trial-result"
            - "memory.md#mem-obj-process-reward"
            - "memory.md#mem-rte-checkpoint-retention"
            - "memory.md#mem-rte-artifact-access"
            - "runtime.md#rt-rte-job-recovery"
            - "memory.md#mem-rte-sweep-selection"
          note: "Raw recording, replay/scheduling and packaging alone do not identify another durable behavior-shaping update. No bounded absence record licenses a local no."
        - scope: "Arbitrary workspace products, adopted maintenance changes, provider/SDK, alternate agents and remote downstream updates"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-terminal-actions"
            - "runtime.md#rt-rte-runtime-patching"
            - "runtime.md#rt-cmp-terminus-model"
            - "memory.md#mem-cmp-analysis-model"
            - "runtime.md#rt-rte-agent-dispatch"
            - "memory.md#mem-rte-artifact-access"
          note: "Generic edits/imports and opaque internal retention do not resolve whether these branches implement qualifying trace-fed updates."
      records:
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-obj-handoff-context"
        - "memory.md#mem-rte-trial-analysis"
        - "memory.md#mem-obj-analysis"
        - "epistemic.md#epi-rte-job-aggregation"
        - "memory.md#mem-bap-analysis-guidance"
        - "epistemic.md#epi-rte-task-check"
        - "memory.md#mem-obj-trajectory"
        - "runtime.md#rt-obj-trial-result"
        - "memory.md#mem-obj-process-reward"
        - "memory.md#mem-rte-checkpoint-retention"
        - "memory.md#mem-rte-artifact-access"
        - "runtime.md#rt-rte-job-recovery"
        - "memory.md#mem-rte-sweep-selection"
        - "runtime.md#rt-rte-terminal-actions"
        - "runtime.md#rt-rte-runtime-patching"
        - "runtime.md#rt-cmp-terminus-model"
        - "memory.md#mem-cmp-analysis-model"
        - "runtime.md#rt-rte-agent-dispatch"
      note: "Two positive automatic trace-fed derivation chains survive unresolved routes. There is no system-wide or local no finding without a bounded absence warrant; the union retains yes without asserting measured learning."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Original inputs to automatic handoff and short-summary continuation write"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
                - "memory.md#mem-obj-handoff-context"
              note: "Recorded user/model conversational turns feed the handoff."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
                - "memory.md#mem-obj-handoff-context"
              note: "Terminal commands, returned observations and current screen supply execution experience to the same write."
          records:
            - "runtime.md#rt-rte-context-handoff"
            - "memory.md#mem-obj-handoff-context"
          note: "Time/token triggers are not event-stream source content. These transcripts are not classified as linked state/action/outcome trajectories merely by a filename."
        - scope: "Original activity evidence feeding trial-analysis to later aggregate chain"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trial-analysis"
              note: "Trajectory model/user turn content and summaries derived from it feed persisted interpretation."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trial-analysis"
              note: "Action history, verifier stdout and exception/execution feedback feed that interpretation."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trial-analysis"
            - "memory.md#mem-obj-analysis"
            - "epistemic.md#epi-rte-job-aggregation"
          note: "Wired evidence access is established, not proof that every actual model call reads every file; aggregation inherits this trace origin through trial assessments."
        - scope: "Static-input task-quality route"
          assessment: "inapplicable"
          findings: []
          records:
            - "epistemic.md#epi-rte-task-check"
          note: "Static task/rubric material is not a trace source for this route."
        - scope: "Further qualifying updates from raw artifact retention, workspace/maintenance, provider/SDK/alternate-agent and remote platform routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-checkpoint-retention"
            - "runtime.md#rt-rte-terminal-actions"
            - "runtime.md#rt-rte-runtime-patching"
            - "runtime.md#rt-cmp-terminus-model"
            - "memory.md#mem-cmp-analysis-model"
            - "runtime.md#rt-rte-agent-dispatch"
            - "memory.md#mem-rte-artifact-access"
          note: "These branches lack a resolved qualifying write or its original inputs. No complete negative trace-learning assessment licenses globally inapplicable trace sources."
      records:
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-obj-handoff-context"
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-rte-trial-analysis"
        - "memory.md#mem-obj-analysis"
        - "epistemic.md#epi-rte-job-aggregation"
        - "epistemic.md#epi-rte-task-check"
        - "memory.md#mem-rte-checkpoint-retention"
        - "runtime.md#rt-rte-terminal-actions"
        - "runtime.md#rt-rte-runtime-patching"
        - "runtime.md#rt-cmp-terminus-model"
        - "memory.md#mem-cmp-analysis-model"
        - "runtime.md#rt-rte-agent-dispatch"
        - "memory.md#mem-rte-artifact-access"
      note: "Session logs and tool traces are supported on both qualifying local chains. Opaque or unestablished updates retain unknown source coverage; no event-streams or trajectories value is inferred from runtime timing or ATIF naming."
---

# LHTB memory profile

## Comparison rationale

The two positive trace-fed chains are context handoff to later foreground
solving and persisted trial interpretation to later aggregation. Their
classification follows automatic derivation, retention and later consumption,
not proof of better performance. The update consumer gives prior experience
learning authority; the resulting text supplies downstream knowledge and,
for the continuation handoff, instructions. These are separate effects:
[RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff),
[MEM-OBJ-handoff-context](memory.md#mem-obj-handoff-context),
[MEM-RTE-trial-analysis](memory.md#mem-rte-trial-analysis) and
[MEM-BAP-analysis-guidance](memory.md#mem-bap-analysis-guidance).

Successful three-call handoff installs replacement history. Short and ultimate
fallback prompts instead pass through unwound Chat; the profile does not
pretend that every recovery installs the same frame. Summary generation and
aggregation support consolidation without establishing faithful preservation.
The indeterminate epistemic content relation does not negate implemented
compression, nor license synthesis of a new claim:
[RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff) and
[EPI-RTE-job-aggregation](epistemic.md#epi-rte-job-aggregation).

Requested file access remains pull, while independent host selection and
supply are push. Recovery's saved/planned configuration identity match and
sweep task identity have actual selection consequences. A requested pathname,
a trial name printed in an aggregate, or an upload duplicate-ID veto alone
does not establish identifier-based push. The sweep implementation is retained
at its wired layer despite unresolved singular reward-key compatibility:
[RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery),
[MEM-RTE-sweep-selection](memory.md#mem-rte-sweep-selection),
[MEM-RTE-trial-analysis](memory.md#mem-rte-trial-analysis) and
[MEM-RTE-artifact-access](memory.md#mem-rte-artifact-access).

The Responses chain is a service-object at the exposed API boundary, not a
known internal substrate or form. Readable trajectories do not classify it.
Analysis SDK context and alternate-agent memory remain separate opaque units:
[RT-CMP-terminus-model](runtime.md#rt-cmp-terminus-model),
[MEM-CMP-analysis-model](memory.md#mem-cmp-analysis-model) and
[RT-RTE-agent-dispatch](runtime.md#rt-rte-agent-dispatch).

Reconciliation supersedes the duplicate epistemic analysis-model component
with [MEM-CMP-analysis-model](memory.md#mem-cmp-analysis-model). That component
supports the retained SDK uncertainty, not a positive model-weights memory
finding. No other supersession affects these values. The broad memory analysis
route and its narrower epistemic assessment/cache/aggregate records remain
compatible; retained trial/job files are not equated with the broader object
that also includes task-quality checking:
[MEM-OBJ-analysis](memory.md#mem-obj-analysis),
[EPI-OBJ-analysis](epistemic.md#epi-obj-analysis),
[EPI-RTE-analysis-cache](epistemic.md#epi-rte-analysis-cache) and
[EPI-RTE-task-check](epistemic.md#epi-rte-task-check).

All axes are partial because their included inventories have unresolved
alternatives, not because wired evidence requires observed execution. Raw
checkpoint retention has no established later JSONL reader; live reward
control is not a reload of that file. Optional task-check output has no
established later consumer. Neither unknown licenses an absent route or a
trace-learning negative. Maintenance adoption is separately afforded and its
actor is not assumed human:
[MEM-RTE-checkpoint-retention](memory.md#mem-rte-checkpoint-retention),
[EPI-RTE-task-check](epistemic.md#epi-rte-task-check) and
[RT-RTE-runtime-patching](runtime.md#rt-rte-runtime-patching).

Source-read log: none. Classification used only the supplied accepted records
and reconciliation; no source inspection, execution, new evidence or record
declaration was performed.
