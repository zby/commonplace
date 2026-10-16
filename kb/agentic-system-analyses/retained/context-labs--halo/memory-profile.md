---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Halo memory comparison: retained trace evidence, desktop diagnostic history/report reuse and optional checkpoint continuations at the frozen partial-loop boundary."
run-id: "AAS-2026-10-14-halo-c4ed89d7f99f-01"
source-identity: "https://github.com/context-labs/halo"
reviewed-boundary: "b7f8509745d67b499b4e80efe20ea37c03426a74"
memory-comparison:
  version: 2
  scope: "Included: retained execution telemetry and JSONL exports; derived trace indexes/freshness metadata; desktop user/assistant turns, result files, raw analysis events and Markdown reports; saved AppWorld evaluation artifacts; optional terminal compaction summaries and host continuation alternatives; unresolved initial caller continuations and opaque provider-side use-acquired/caching state. Excluded: ordinary disposable current-run context/tool results except checkpoint production and local backing parts of that affordance; static shipped engine/skill prompts; inference weights and installed engine code as machinery; arbitrary external harness edits/deployment and coding-tool internals."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Captured telemetry tables and exported/caller JSONL files"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traces-jsonl"
                - "memory.md#mem-rte-telemetry-admission"
              note: "Desktop spans persist in SQLite."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traces-jsonl"
                - "memory.md#mem-rte-telemetry-admission"
              note: "Caller inputs and desktop exports persist as JSONL files."
          records:
            - "memory.md#mem-obj-traces-jsonl"
            - "memory.md#mem-rte-telemetry-admission"
          note: "The inspected retained telemetry and export parts have separately identified substrates; upstream provider storage is not covered by this unit."
        - scope: "Trace index rows and freshness sidecars, including their loaded access structures"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace-index"
              note: "Index and metadata sidecars persist on disk."
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace-index"
              note: "TraceStore loads the derived access structures into process memory."
          records:
            - "memory.md#mem-obj-trace-index"
          note: "The record identifies both disk sidecars and loaded TraceStore memory."
        - scope: "Desktop conversation turns and per-turn result artifacts"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-halo-run-turns"
              note: "Role/content/order/status rows persist in SQLite."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-halo-run-turns"
              note: "Per-turn result JSON persists in run output files."
          records:
            - "memory.md#mem-obj-halo-run-turns"
          note: "SQLite text rows and result JSON are the recorded durable conversation surfaces."
        - scope: "Desktop analysis event payloads"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-halo-run-events"
              note: "Raw event payloads and sequence/turn/agent metadata persist as event rows."
          records:
            - "memory.md#mem-obj-halo-run-events"
          note: "Live publication is not counted as another storage substrate."
        - scope: "Materialized report and artifact locator metadata"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-report"
                - "workflow.md#wf-rte-report-materialization"
              note: "Markdown content persists in the run directory."
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-report"
                - "workflow.md#wf-rte-report-materialization"
              note: "Artifact metadata retains the report locator and size."
          records:
            - "memory.md#mem-obj-report"
            - "workflow.md#wf-rte-report-materialization"
          note: "The file content and SQLite path/size metadata remain distinct retained parts."
        - scope: "Saved AppWorld evaluation artifacts"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-report"
              note: "Task and dataset evaluation reports/version files persist in experiment output directories."
          records:
            - "memory.md#mem-obj-evaluation-report"
          note: "The immediate TestTracker is not classified as durable memory independently of saved reports."
        - scope: "Optional compaction summaries and host-persisted checkpoint continuation"
          assessment: "partial"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-agent-context"
                - "runtime.md#rt-rte-checkpoint-emission"
              note: "Compaction summaries and backing originals reside in per-agent memory before checkpoint emission."
          records:
            - "memory.md#mem-obj-agent-context"
            - "runtime.md#rt-rte-checkpoint-emission"
          note: "Summary storage is known locally, but the checkpoint host chooses persistence; no desktop checkpoint store is wired."
        - scope: "Included opaque provider-side retained or caching state, if any; not the inference weights as shipped machinery"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-root-agent"
            - "runtime.md#rt-cmp-subagent"
            - "runtime.md#rt-cmp-synthesis-model"
            - "runtime.md#rt-cmp-compaction-model"
          note: "The accepted model-component records leave provider internals uninspected. Local inference and cache-oriented configuration do not classify provider-side use-acquired memory for this axis: storage substrate."
      records:
        - "memory.md#mem-obj-traces-jsonl"
        - "memory.md#mem-rte-telemetry-admission"
        - "memory.md#mem-obj-trace-index"
        - "memory.md#mem-obj-halo-run-turns"
        - "memory.md#mem-obj-halo-run-events"
        - "memory.md#mem-obj-report"
        - "workflow.md#wf-rte-report-materialization"
        - "memory.md#mem-obj-evaluation-report"
        - "memory.md#mem-obj-agent-context"
        - "runtime.md#rt-rte-checkpoint-emission"
        - "runtime.md#rt-cmp-root-agent"
        - "runtime.md#rt-cmp-subagent"
        - "runtime.md#rt-cmp-synthesis-model"
        - "runtime.md#rt-cmp-compaction-model"
      note: "The accepted memory inventory establishes local substrates; external checkpoint persistence and opaque provider state prevent a complete substrate inventory. Ordinary disposable tool results, static prompts and installed engine code are excluded."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Telemetry envelopes, trace index rows and freshness metadata"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traces-jsonl"
                - "memory.md#mem-obj-trace-index"
              note: "Local identifiers, timestamps, status fields and access metadata have fixed programmatic consumers."
          records:
            - "memory.md#mem-obj-traces-jsonl"
            - "memory.md#mem-obj-trace-index"
          note: "Fixed-rule span metadata, offsets, rollups and stat/schema fields are separate from interpreted payload text."
        - scope: "Prompt/output prose carried in retained telemetry and returned evidence"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traces-jsonl"
                - "memory.md#mem-rte-trace-read"
              note: "The diagnostic model interprets retained prompt/output text as evidence."
          records:
            - "memory.md#mem-obj-traces-jsonl"
            - "memory.md#mem-rte-trace-read"
          note: "This covers interpreted text fields, not every arbitrary attribute or upstream encoding."
        - scope: "Other arbitrary telemetry attributes and code-string consumption"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-traces-jsonl"
            - "memory.md#mem-rte-trace-read"
          note: "Records identify interpreter-dependent payloads without classifying every arbitrary attribute or executable string at its eventual consumer."
        - scope: "Retained conversation text at follow-up and report consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-halo-run-turns"
                - "memory.md#mem-bap-followup-history"
                - "memory.md#mem-obj-report"
              note: "Later analysis models and report readers interpret user questions and selected answers."
          records:
            - "memory.md#mem-obj-halo-run-turns"
            - "memory.md#mem-bap-followup-history"
            - "memory.md#mem-obj-report"
          note: "Questions and diagnoses are distinguished from role/order/status fields."
        - scope: "Conversation, event and report access/control metadata"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-halo-run-turns"
                - "memory.md#mem-obj-halo-run-events"
                - "memory.md#mem-obj-report"
                - "workflow.md#wf-rte-report-materialization"
              note: "Fixed selection and rendering rules consume these localized fields."
          records:
            - "memory.md#mem-obj-halo-run-turns"
            - "memory.md#mem-obj-halo-run-events"
            - "memory.md#mem-obj-report"
            - "workflow.md#wf-rte-report-materialization"
          note: "Roles, turn indices, event identities, statuses and report locators have code-controlled consumers."
        - scope: "Readable event message bodies at the activity UI"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-halo-run-events"
              note: "Human readers interpret displayed messages and diagnostic text."
          records:
            - "memory.md#mem-obj-halo-run-events"
          note: "The presenter exposes raw payload alongside text; text display does not classify the entire payload."
        - scope: "Other raw event payload parts at display or hypothetical replay"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-halo-run-events"
          note: "The record distinguishes arbitrary executable tool arguments/results from readable summaries; no universal payload form or durable agent replay consumer is established."
        - scope: "Compaction summary prose at afforded checkpoint replay"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-agent-context"
                - "runtime.md#rt-rte-checkpoint-emission"
              note: "A later host-supplied continuation carries summary prose for model interpretation."
          records:
            - "memory.md#mem-obj-agent-context"
            - "runtime.md#rt-rte-checkpoint-emission"
          note: "Plain-text summaries are known; disposal of backing originals prevents treating item IDs as full stored content."
        - scope: "Evaluation scores/test outcomes"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-report"
                - "epistemic.md#epi-rte-task-evaluation"
              note: "Scores and pass/fail outcomes are fixed-rule results."
          records:
            - "memory.md#mem-obj-evaluation-report"
            - "epistemic.md#epi-rte-task-evaluation"
          note: "This classifies saved criterion-relative results, not uninspected task oracle implementations."
        - scope: "Readable evaluation report prose"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-evaluation-report"
              note: "Saved readable report content affords later experimenter interpretation."
          records:
            - "memory.md#mem-obj-evaluation-report"
          note: "The report text is distinct from symbolic scores."
        - scope: "Included opaque provider-side retained or caching state, if any; not the inference weights as shipped machinery"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-root-agent"
            - "runtime.md#rt-cmp-subagent"
            - "runtime.md#rt-cmp-synthesis-model"
            - "runtime.md#rt-cmp-compaction-model"
          note: "The accepted model-component records leave provider internals uninspected. Local inference and cache-oriented configuration do not classify provider-side use-acquired memory for this axis: representational form."
      records:
        - "memory.md#mem-obj-traces-jsonl"
        - "memory.md#mem-obj-trace-index"
        - "memory.md#mem-rte-trace-read"
        - "memory.md#mem-obj-halo-run-turns"
        - "memory.md#mem-bap-followup-history"
        - "memory.md#mem-obj-report"
        - "memory.md#mem-obj-halo-run-events"
        - "workflow.md#wf-rte-report-materialization"
        - "memory.md#mem-obj-agent-context"
        - "runtime.md#rt-rte-checkpoint-emission"
        - "memory.md#mem-obj-evaluation-report"
        - "epistemic.md#epi-rte-task-evaluation"
        - "runtime.md#rt-cmp-root-agent"
        - "runtime.md#rt-cmp-subagent"
        - "runtime.md#rt-cmp-synthesis-model"
        - "runtime.md#rt-cmp-compaction-model"
      note: "Mixed objects are split by operative part and consumer. No parametric memory finding follows from remotely served inference weights; arbitrary payloads and provider memory remain unresolved."
    lineage:
      assessment: "partial"
      units:
        - scope: "Imported caller traces and normalized desktop telemetry/export"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traces-jsonl"
                - "memory.md#mem-rte-telemetry-admission"
              note: "User/service telemetry enters through files or shipped adapters and is exported from retained spans."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traces-jsonl"
                - "memory.md#mem-rte-telemetry-admission"
              note: "Common decoding, normalization and filtered export deterministically derive local envelopes."
          records:
            - "memory.md#mem-obj-traces-jsonl"
            - "memory.md#mem-rte-telemetry-admission"
          note: "Import and normalization are known; arbitrary-file initial provenance and adapter mapping fidelity are unresolved."
        - scope: "Trace sidecar rows and freshness metadata"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace-index"
              note: "Deterministic parsing/grouping derives cache rows and access metadata."
          records:
            - "memory.md#mem-obj-trace-index"
          note: "The known derivation does not authenticate the original trace source."
        - scope: "Explicit desktop user question content"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-halo-run-turns"
                - "runtime.md#rt-rte-desktop-analysis"
              note: "The user supplies questions retained as user turns."
          records:
            - "memory.md#mem-obj-halo-run-turns"
            - "runtime.md#rt-rte-desktop-analysis"
          note: "The shipped user-question route is separately identified; it does not resolve generic library caller authorship."
        - scope: "Automatically retained diagnostic answers and analysis events"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-halo-run-turns"
                - "memory.md#mem-obj-halo-run-events"
                - "runtime.md#rt-rte-desktop-analysis"
                - "memory.md#mem-rte-trace-read"
              note: "Diagnostic answers are generated from trace investigation and retained for follow-ups."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-halo-run-turns"
                - "memory.md#mem-obj-halo-run-events"
                - "runtime.md#rt-rte-desktop-analysis"
                - "memory.md#mem-rte-trace-read"
              note: "The bridge stream and software-selected answer/event envelopes are mechanically persisted."
          records:
            - "memory.md#mem-obj-halo-run-turns"
            - "memory.md#mem-obj-halo-run-events"
            - "runtime.md#rt-rte-desktop-analysis"
            - "memory.md#mem-rte-trace-read"
          note: "Model text and bridge-stream events have distinct derivations within the named route."
        - scope: "Materialized conversation report"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-report"
                - "workflow.md#wf-rte-report-materialization"
              note: "The renderer derives Markdown from retained run/turn state."
          records:
            - "memory.md#mem-obj-report"
            - "workflow.md#wf-rte-report-materialization"
          note: "Report preparation is a deterministic projection, not another model diagnosis."
        - scope: "Saved evaluation outcomes"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-report"
                - "epistemic.md#epi-rte-task-evaluation"
              note: "Programmatic task evaluation produces saved scores and reports."
          records:
            - "memory.md#mem-obj-evaluation-report"
            - "epistemic.md#epi-rte-task-evaluation"
          note: "The evaluator derives criterion-relative outcomes from task outputs/reference data; task-specific modules remain uninspected."
        - scope: "Optional compaction summaries"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-agent-context"
                - "runtime.md#rt-rte-checkpoint-emission"
              note: "The compaction model derives plain-text summaries from selected recorded conversation/tool items."
          records:
            - "memory.md#mem-obj-agent-context"
            - "runtime.md#rt-rte-checkpoint-emission"
          note: "The generation mechanism is wired even though later host persistence/replay is only afforded."
        - scope: "Externally supplied leading system message and continuation content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-agent-context"
          note: "The input continuation surface passes caller content through, but generic caller identity leaves its authorship, prior derivation and initial provenance unresolved."
        - scope: "Included opaque provider-side retained or caching state, if any; not the inference weights as shipped machinery"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-root-agent"
            - "runtime.md#rt-cmp-subagent"
            - "runtime.md#rt-cmp-synthesis-model"
            - "runtime.md#rt-cmp-compaction-model"
          note: "The accepted model-component records leave provider internals uninspected. Local inference and cache-oriented configuration do not classify provider-side use-acquired memory for this axis: lineage."
      records:
        - "memory.md#mem-obj-traces-jsonl"
        - "memory.md#mem-rte-telemetry-admission"
        - "memory.md#mem-obj-trace-index"
        - "memory.md#mem-obj-halo-run-turns"
        - "runtime.md#rt-rte-desktop-analysis"
        - "memory.md#mem-obj-halo-run-events"
        - "memory.md#mem-rte-trace-read"
        - "memory.md#mem-obj-report"
        - "workflow.md#wf-rte-report-materialization"
        - "memory.md#mem-obj-evaluation-report"
        - "epistemic.md#epi-rte-task-evaluation"
        - "memory.md#mem-obj-agent-context"
        - "runtime.md#rt-rte-checkpoint-emission"
        - "runtime.md#rt-cmp-root-agent"
        - "runtime.md#rt-cmp-subagent"
        - "runtime.md#rt-cmp-synthesis-model"
        - "runtime.md#rt-cmp-compaction-model"
      note: "Known local derivations coexist with unresolved input provenance. Report rendering is other-compiled even when its source turns contain trace-extracted diagnoses."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Retained telemetry and trace views at diagnostic model consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traces-jsonl"
                - "memory.md#mem-rte-trace-read"
                - "runtime.md#rt-rte-desktop-analysis"
                - "memory.md#mem-obj-halo-run-turns"
              note: "Trace views supply evidence to root/child analysis models."
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traces-jsonl"
                - "memory.md#mem-rte-trace-read"
                - "runtime.md#rt-rte-desktop-analysis"
                - "memory.md#mem-obj-halo-run-turns"
              note: "Retained execution evidence feeds model generation of durable diagnostic answers that later follow-ups consume."
          records:
            - "memory.md#mem-obj-traces-jsonl"
            - "memory.md#mem-rte-trace-read"
            - "runtime.md#rt-rte-desktop-analysis"
            - "memory.md#mem-obj-halo-run-turns"
          note: "The same evidence has a diagnostic consumer and a downstream durable-answer production route; no truth acceptance follows."
        - scope: "Trace access rows and freshness metadata at TraceStore/startup consumers"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace-index"
                - "epistemic.md#epi-rte-index-reuse"
              note: "Offsets and rollups select evidence locations and filtering scope."
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace-index"
                - "epistemic.md#epi-rte-index-reuse"
              note: "Retained schema/size/mtime criteria determine sidecar eligibility."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace-index"
                - "epistemic.md#epi-rte-index-reuse"
              note: "The eligibility predicate admits reuse or forces the alternative rebuild path."
          records:
            - "memory.md#mem-obj-trace-index"
            - "epistemic.md#epi-rte-index-reuse"
          note: "Access routing and cache admission are distinct effects; this unit does not imply model-interpreted instructions."
        - scope: "Retained conversation text at follow-up and report production"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-halo-run-turns"
                - "memory.md#mem-bap-followup-history"
                - "memory.md#mem-obj-report"
                - "workflow.md#wf-rte-report-materialization"
              note: "Prior selected answers supply conversational evidence to the later root model."
          records:
            - "memory.md#mem-obj-halo-run-turns"
            - "memory.md#mem-bap-followup-history"
            - "memory.md#mem-obj-report"
            - "workflow.md#wf-rte-report-materialization"
          note: "Retained questions and diagnoses supply conversational context. Replayed historical requests do not establish standing directions, so these records support knowledge but not instruction."
        - scope: "Turn ordering/status and report locator metadata at selectors"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-halo-run-turns"
                - "memory.md#mem-obj-report"
                - "workflow.md#wf-rte-report-materialization"
                - "runtime.md#rt-rte-desktop-analysis"
              note: "Turn index/content and report status/locator fields select history, report exchanges and the handoff file."
          records:
            - "memory.md#mem-obj-halo-run-turns"
            - "memory.md#mem-obj-report"
            - "workflow.md#wf-rte-report-materialization"
            - "runtime.md#rt-rte-desktop-analysis"
          note: "These are programmatic selection effects rather than semantic endorsement."
        - scope: "Retained activity payload at human display"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-halo-run-events"
              note: "Activity display supplies retained messages/tool activity as human-readable evidence."
          records:
            - "memory.md#mem-obj-halo-run-events"
          note: "The raw event store is not wired into follow-up model replay."
        - scope: "Conversation report at the receiving coding actor"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-report"
                - "runtime.md#rt-rte-report-handoff"
              note: "The path-bearing handoff affords later reading of retained diagnostic findings."
          records:
            - "memory.md#mem-obj-report"
            - "runtime.md#rt-rte-report-handoff"
          note: "The report supplies findings; the static launch prompt is not classified as acquired memory."
        - scope: "Optional summary/tail checkpoint at a later host continuation consumer"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-agent-context"
                - "runtime.md#rt-rte-checkpoint-emission"
              note: "Replayed summaries and original tail provide context for later reasoning."
          records:
            - "memory.md#mem-obj-agent-context"
            - "runtime.md#rt-rte-checkpoint-emission"
          note: "A caller can persist and re-supply messages; ordinary desktop does not do so."
        - scope: "Saved evaluation outcomes at an experimenter"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-evaluation-report"
                - "epistemic.md#epi-rte-task-evaluation"
                - "runtime.md#rt-rte-report-handoff"
              note: "Saved results afford criterion-relative evidence for later comparison."
          records:
            - "memory.md#mem-obj-evaluation-report"
            - "epistemic.md#epi-rte-task-evaluation"
            - "runtime.md#rt-rte-report-handoff"
          note: "The inspected evaluator reports outcomes; external shipping remains separately prescribed."
        - scope: "Caller-supplied retained system guidance and provider-state consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-agent-context"
            - "runtime.md#rt-cmp-root-agent"
            - "runtime.md#rt-cmp-subagent"
            - "runtime.md#rt-cmp-synthesis-model"
            - "runtime.md#rt-cmp-compaction-model"
          note: "A leading system message can bypass engine guidance, but acquired-content identity and authority are unspecified; opaque provider-state effects also remain uninspected."
      records:
        - "memory.md#mem-obj-traces-jsonl"
        - "memory.md#mem-rte-trace-read"
        - "runtime.md#rt-rte-desktop-analysis"
        - "memory.md#mem-obj-halo-run-turns"
        - "memory.md#mem-obj-trace-index"
        - "epistemic.md#epi-rte-index-reuse"
        - "memory.md#mem-bap-followup-history"
        - "memory.md#mem-obj-report"
        - "workflow.md#wf-rte-report-materialization"
        - "memory.md#mem-obj-halo-run-events"
        - "runtime.md#rt-rte-report-handoff"
        - "memory.md#mem-obj-agent-context"
        - "runtime.md#rt-rte-checkpoint-emission"
        - "memory.md#mem-obj-evaluation-report"
        - "epistemic.md#epi-rte-task-evaluation"
        - "runtime.md#rt-cmp-root-agent"
        - "runtime.md#rt-cmp-subagent"
        - "runtime.md#rt-cmp-synthesis-model"
        - "runtime.md#rt-cmp-compaction-model"
      note: "Knowledge, routing, validation, enforcement and learning are local consumer classifications, not system-wide compliance or benefit. Historical user requests do not establish acquired-memory instruction authority; caller-supplied retained system guidance remains unresolved. No retained ranking input with relative-priority effect is established by these accepted records."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Explicit human supply of desktop question content"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "wired"
              records:
                - "memory.md#mem-obj-halo-run-turns"
                - "runtime.md#rt-rte-desktop-analysis"
              note: "The shipped user makes the per-content decision supplying the question."
          records:
            - "memory.md#mem-obj-halo-run-turns"
            - "runtime.md#rt-rte-desktop-analysis"
          note: "The user supplies the retained question itself, unlike merely starting automatic diagnosis."
        - scope: "Telemetry normalization/upsert, export and trace-index derivation"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-telemetry-admission"
                - "memory.md#mem-obj-traces-jsonl"
                - "memory.md#mem-obj-trace-index"
              note: "Code admits decoded spans, exports selected rows and builds sidecars without per-item human review."
          records:
            - "memory.md#mem-rte-telemetry-admission"
            - "memory.md#mem-obj-traces-jsonl"
            - "memory.md#mem-obj-trace-index"
          note: "Software admission is separate from unknown upstream authorship."
        - scope: "Desktop answer/event admission and legacy-turn reconstruction"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-halo-run-turns"
                - "memory.md#mem-obj-halo-run-events"
                - "runtime.md#rt-rte-desktop-analysis"
              note: "Bridge/queue software selects and retains answers/events and reconstructs legacy turns."
          records:
            - "memory.md#mem-obj-halo-run-turns"
            - "memory.md#mem-obj-halo-run-events"
            - "runtime.md#rt-rte-desktop-analysis"
          note: "Human run initiation does not approve each generated answer or event."
        - scope: "Report preparation and freshness replacement"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-report"
                - "workflow.md#wf-rte-report-materialization"
              note: "Code selects exchanges and admits/replaces the Markdown projection without per-finding approval."
          records:
            - "memory.md#mem-obj-report"
            - "workflow.md#wf-rte-report-materialization"
          note: "Automatic terminal preparation and explicit UI requests use the same software content rule."
        - scope: "Evaluation result persistence"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation-report"
                - "epistemic.md#epi-rte-task-evaluation"
              note: "The evaluator writes test outcomes/report files by programmatic rule."
          records:
            - "memory.md#mem-obj-evaluation-report"
            - "epistemic.md#epi-rte-task-evaluation"
          note: "save_report is a software persistence choice, not per-result human approval."
        - scope: "Optional compaction summary admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-agent-context"
                - "runtime.md#rt-rte-checkpoint-emission"
              note: "Code and model admit summaries when unit summarization succeeds."
          records:
            - "memory.md#mem-obj-agent-context"
            - "runtime.md#rt-rte-checkpoint-emission"
          note: "Successful complete units replace rendered items without semantic or human review."
        - scope: "Initial caller-file content and externally supplied system/continuation replacement"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-traces-jsonl"
            - "memory.md#mem-obj-agent-context"
          note: "Generic caller identity and arbitrary source files do not establish a human per-content decision or software admission mechanism."
        - scope: "Included opaque provider-side retained or caching state, if any; not the inference weights as shipped machinery"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-root-agent"
            - "runtime.md#rt-cmp-subagent"
            - "runtime.md#rt-cmp-synthesis-model"
            - "runtime.md#rt-cmp-compaction-model"
          note: "The accepted model-component records leave provider internals uninspected. Local inference and cache-oriented configuration do not classify provider-side use-acquired memory for this axis: write agency."
      records:
        - "memory.md#mem-obj-halo-run-turns"
        - "runtime.md#rt-rte-desktop-analysis"
        - "memory.md#mem-rte-telemetry-admission"
        - "memory.md#mem-obj-traces-jsonl"
        - "memory.md#mem-obj-trace-index"
        - "memory.md#mem-obj-halo-run-events"
        - "memory.md#mem-obj-report"
        - "workflow.md#wf-rte-report-materialization"
        - "memory.md#mem-obj-evaluation-report"
        - "epistemic.md#epi-rte-task-evaluation"
        - "memory.md#mem-obj-agent-context"
        - "runtime.md#rt-rte-checkpoint-emission"
        - "runtime.md#rt-cmp-root-agent"
        - "runtime.md#rt-cmp-subagent"
        - "runtime.md#rt-cmp-synthesis-model"
        - "runtime.md#rt-cmp-compaction-model"
      note: "The named local admission mechanisms are classified independently of physical writes and authorship. Unknown initial input control and provider admission prevent completeness."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Optional old-item compaction"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-checkpoint-emission"
                - "memory.md#mem-obj-agent-context"
              note: "Selected conversation/tool items are compressed into shorter summary representations while originals remain local."
          records:
            - "runtime.md#rt-rte-checkpoint-emission"
            - "memory.md#mem-obj-agent-context"
          note: "Summarizer input and successful-unit replacement implement reduction; preservation defects do not make it synthesis."
        - scope: "Report exchange selection and projection"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-report"
                - "workflow.md#wf-rte-report-materialization"
              note: "Status/content selection combines a reduced conversation representation into report Markdown."
          records:
            - "memory.md#mem-obj-report"
            - "workflow.md#wf-rte-report-materialization"
          note: "The deterministic projection retains selected existing claims, not novel model claims."
        - scope: "Subsequent keyed telemetry and answer/report replacement"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-telemetry-admission"
                - "memory.md#mem-obj-halo-run-turns"
                - "memory.md#mem-obj-report"
                - "memory.md#mem-rte-retention-cleanup"
              note: "Same-key span upserts, terminal answer overwrite and stale-report rewrite revise existing retained entries/projections."
          records:
            - "memory.md#mem-rte-telemetry-admission"
            - "memory.md#mem-obj-halo-run-turns"
            - "memory.md#mem-obj-report"
            - "memory.md#mem-rte-retention-cleanup"
          note: "Only evidenced later replacement is covered; acquisition and initial writes are not themselves curation."
        - scope: "Run/telemetry and experiment-output deletion"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-retention-cleanup"
              note: "Cleanup removes retained rows and attempts/removes associated output files, ending ordinary lookup for those parts."
          records:
            - "memory.md#mem-rte-retention-cleanup"
          note: "Deletion forgets selected material; separate stores and best-effort files limit propagation."
        - scope: "Trace-index rebuilding and initial diagnostic generation"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-trace-index"
            - "memory.md#mem-rte-trace-read"
            - "runtime.md#rt-rte-desktop-analysis"
            - "memory.md#mem-obj-halo-run-turns"
          note: "Index rebuilding alone establishes no controlled curation operation. An unseen diagnostic answer can reshape or add claims, but records do not establish its implemented semantic relation well enough to assert synthesis."
        - scope: "Included opaque provider-side retained or caching state, if any; not the inference weights as shipped machinery"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-root-agent"
            - "runtime.md#rt-cmp-subagent"
            - "runtime.md#rt-cmp-synthesis-model"
            - "runtime.md#rt-cmp-compaction-model"
          note: "The accepted model-component records leave provider internals uninspected. Local inference and cache-oriented configuration do not classify provider-side use-acquired memory for this axis: curation operations."
      records:
        - "runtime.md#rt-rte-checkpoint-emission"
        - "memory.md#mem-obj-agent-context"
        - "memory.md#mem-obj-report"
        - "workflow.md#wf-rte-report-materialization"
        - "memory.md#mem-rte-telemetry-admission"
        - "memory.md#mem-obj-halo-run-turns"
        - "memory.md#mem-rte-retention-cleanup"
        - "memory.md#mem-obj-trace-index"
        - "memory.md#mem-rte-trace-read"
        - "runtime.md#rt-rte-desktop-analysis"
        - "runtime.md#rt-cmp-root-agent"
        - "runtime.md#rt-cmp-subagent"
        - "runtime.md#rt-cmp-synthesis-model"
        - "runtime.md#rt-cmp-compaction-model"
      note: "Consolidation, revision and forgetting have inspected local mechanisms. No semantic invalidation-with-history, deduplication, promotion or novel-claim synthesis is inferred from route names or successful calls; unresolved branches remain included."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Requested trace evidence retrieval and desktop export"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-read"
                - "memory.md#mem-obj-traces-jsonl"
                - "runtime.md#rt-rte-desktop-analysis"
              note: "Explicit IDs/filters/regex or a selected trace target request retained evidence."
          records:
            - "memory.md#mem-rte-trace-read"
            - "memory.md#mem-obj-traces-jsonl"
            - "runtime.md#rt-rte-desktop-analysis"
          note: "Model/user requests select retained telemetry; code delivery fulfills those requests."
        - scope: "Follow-up history selection and supply to the next root invocation"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-halo-run-turns"
                - "memory.md#mem-bap-followup-history"
                - "runtime.md#rt-rte-desktop-analysis"
              note: "Code automatically supplies qualifying earlier turns to the later root model."
          records:
            - "memory.md#mem-obj-halo-run-turns"
            - "memory.md#mem-bap-followup-history"
            - "runtime.md#rt-rte-desktop-analysis"
          note: "The new question triggers automatic selection of prior content, rather than an explicit request for those retained turns."
        - scope: "Report materialization: automatic terminal route and explicit preparation route"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-report"
                - "workflow.md#wf-rte-report-materialization"
              note: "Terminal answer handling automatically selects retained conversation for the report consumer."
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-report"
                - "workflow.md#wf-rte-report-materialization"
              note: "Explicit report preparation requests the retained conversation projection."
          records:
            - "memory.md#mem-obj-report"
            - "workflow.md#wf-rte-report-materialization"
          note: "The two triggers share a renderer but retain different request/selection operations."
        - scope: "Report reading by user-selected external coding actor"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-report-handoff"
                - "memory.md#mem-obj-report"
              note: "The path-bearing request asks the actor to read the selected stored report."
          records:
            - "runtime.md#rt-rte-report-handoff"
            - "memory.md#mem-obj-report"
          note: "User-confirmed path access is afforded, not inspected receiving-tool operation."
        - scope: "Stored activity UI and saved evaluation inspection"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-halo-run-events"
                - "memory.md#mem-obj-evaluation-report"
                - "epistemic.md#epi-rte-task-evaluation"
              note: "Display and experimenter inspection request retained activity or saved evaluation results."
          records:
            - "memory.md#mem-obj-halo-run-events"
            - "memory.md#mem-obj-evaluation-report"
            - "epistemic.md#epi-rte-task-evaluation"
          note: "Human consumers have retained display/report access; autonomous agent replay is not inferred."
        - scope: "Optional checkpoint host persistence and continuation resupply"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-agent-context"
            - "runtime.md#rt-rte-checkpoint-emission"
          note: "A later continuation consumer is afforded, but the host request versus automatic selection/delivery mechanism is unspecified."
        - scope: "Included opaque provider-side retained or caching state, if any; not the inference weights as shipped machinery"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-root-agent"
            - "runtime.md#rt-cmp-subagent"
            - "runtime.md#rt-cmp-synthesis-model"
            - "runtime.md#rt-cmp-compaction-model"
          note: "The accepted model-component records leave provider internals uninspected. Local inference and cache-oriented configuration do not classify provider-side use-acquired memory for this axis: read-back direction."
      records:
        - "memory.md#mem-rte-trace-read"
        - "memory.md#mem-obj-traces-jsonl"
        - "runtime.md#rt-rte-desktop-analysis"
        - "memory.md#mem-obj-halo-run-turns"
        - "memory.md#mem-bap-followup-history"
        - "memory.md#mem-obj-report"
        - "workflow.md#wf-rte-report-materialization"
        - "runtime.md#rt-rte-report-handoff"
        - "memory.md#mem-obj-halo-run-events"
        - "memory.md#mem-obj-evaluation-report"
        - "epistemic.md#epi-rte-task-evaluation"
        - "memory.md#mem-obj-agent-context"
        - "runtime.md#rt-rte-checkpoint-emission"
        - "runtime.md#rt-cmp-root-agent"
        - "runtime.md#rt-cmp-subagent"
        - "runtime.md#rt-cmp-synthesis-model"
        - "runtime.md#rt-cmp-compaction-model"
      note: "Pull and push coexist within the shipped local chains. Follow-up history is push selection despite a requested new analysis; external checkpoint/provider alternatives prevent a complete direction inventory."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Automatic follow-up history supply"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-halo-run-turns"
                - "memory.md#mem-bap-followup-history"
                - "runtime.md#rt-rte-desktop-analysis"
              note: "The selected run identity bounds which retained conversation is delivered."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-halo-run-turns"
                - "memory.md#mem-bap-followup-history"
                - "runtime.md#rt-rte-desktop-analysis"
              note: "Within that run, index/role/nonempty-content rules supply all qualifying earlier turns rather than semantic relevance selection."
          records:
            - "memory.md#mem-obj-halo-run-turns"
            - "memory.md#mem-bap-followup-history"
            - "runtime.md#rt-rte-desktop-analysis"
          note: "Trigger: new follow-up. Selector inputs: selected run, upToTurnIndex and role/content. Selected parts: earlier user and nonempty assistant turns."
        - scope: "Automatic terminal report projection"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-report"
                - "workflow.md#wf-rte-report-materialization"
              note: "Run identity selects the retained conversation used to build its report."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-report"
                - "workflow.md#wf-rte-report-materialization"
              note: "Role/status/content filters select qualifying exchanges without semantic targeting."
          records:
            - "memory.md#mem-obj-report"
            - "workflow.md#wf-rte-report-materialization"
          note: "Trigger: terminal answer handling. Selector inputs: run ID, role/status/content. Selected parts: user turns and completed/incomplete nonempty assistant turns."
        - scope: "Requested trace/export, explicit report and human evaluation/activity reads"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-trace-read"
            - "memory.md#mem-obj-traces-jsonl"
            - "workflow.md#wf-rte-report-materialization"
            - "runtime.md#rt-rte-report-handoff"
            - "memory.md#mem-obj-halo-run-events"
            - "memory.md#mem-obj-evaluation-report"
          note: "These requested operations are pull; their IDs/filters are not automatically classified as push signals."
        - scope: "Optional host checkpoint replay selection"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-agent-context"
            - "runtime.md#rt-rte-checkpoint-emission"
          note: "No host selector is recorded. Item IDs printed in checkpoint messages do not establish identity-matched push selection."
        - scope: "Included opaque provider-side retained or caching state, if any; not the inference weights as shipped machinery"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-root-agent"
            - "runtime.md#rt-cmp-subagent"
            - "runtime.md#rt-cmp-synthesis-model"
            - "runtime.md#rt-cmp-compaction-model"
          note: "The accepted model-component records leave provider internals uninspected. Local inference and cache-oriented configuration do not classify provider-side use-acquired memory for this axis: read-back signal."
      records:
        - "memory.md#mem-obj-halo-run-turns"
        - "memory.md#mem-bap-followup-history"
        - "runtime.md#rt-rte-desktop-analysis"
        - "memory.md#mem-obj-report"
        - "workflow.md#wf-rte-report-materialization"
        - "memory.md#mem-rte-trace-read"
        - "memory.md#mem-obj-traces-jsonl"
        - "runtime.md#rt-rte-report-handoff"
        - "memory.md#mem-obj-halo-run-events"
        - "memory.md#mem-obj-evaluation-report"
        - "memory.md#mem-obj-agent-context"
        - "runtime.md#rt-rte-checkpoint-emission"
        - "runtime.md#rt-cmp-root-agent"
        - "runtime.md#rt-cmp-subagent"
        - "runtime.md#rt-cmp-synthesis-model"
        - "runtime.md#rt-cmp-compaction-model"
      note: "Identifier matches and coarse inclusion filters are distinct supported findings on local pushes. Pull selectors do not establish push signals; host/provider uncertainty prevents system-wide inapplicability or completeness."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Trace investigation to automatically retained diagnostic answer to later desktop follow-up"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traces-jsonl"
                - "memory.md#mem-rte-trace-read"
                - "runtime.md#rt-rte-desktop-analysis"
                - "memory.md#mem-obj-halo-run-turns"
                - "memory.md#mem-bap-followup-history"
              note: "Execution traces feed automatic production of retained diagnostic text used as later model context; improved capacity is not asserted."
          records:
            - "memory.md#mem-obj-traces-jsonl"
            - "memory.md#mem-rte-trace-read"
            - "runtime.md#rt-rte-desktop-analysis"
            - "memory.md#mem-obj-halo-run-turns"
            - "memory.md#mem-bap-followup-history"
          note: "Raw trace storage alone is not the warrant: automatic model diagnosis, durable answer admission and wired later model delivery complete the scoped chain."
        - scope: "Conversation/tool-item compaction to host-persisted and re-supplied checkpoint"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-agent-context"
                - "runtime.md#rt-rte-checkpoint-emission"
              note: "Recorded conversation/tool items feed automatic summary production, with a host continuation surface affording durable retention and later context delivery."
          records:
            - "memory.md#mem-obj-agent-context"
            - "runtime.md#rt-rte-checkpoint-emission"
          note: "The write is wired, but durable host persistence and later replay are only afforded, so this chain is not upgraded to wired."
        - scope: "Initial externally supplied continuation and evaluation-to-durable-behavior alternative"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-agent-context"
            - "memory.md#mem-obj-evaluation-report"
            - "epistemic.md#epi-rte-task-evaluation"
            - "runtime.md#rt-rte-report-handoff"
          note: "Initial continuation provenance is unknown. Saved evaluation evidence and prescribed external shipping do not establish an inspected automatic durable behavior-shaping update; task-specific and receiving-tool mechanisms remain unresolved."
        - scope: "Included opaque provider-side retained or caching state, if any; not the inference weights as shipped machinery"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-root-agent"
            - "runtime.md#rt-cmp-subagent"
            - "runtime.md#rt-cmp-synthesis-model"
            - "runtime.md#rt-cmp-compaction-model"
          note: "The accepted model-component records leave provider internals uninspected. Local inference and cache-oriented configuration do not classify provider-side use-acquired memory for this axis: trace learning."
      records:
        - "memory.md#mem-obj-traces-jsonl"
        - "memory.md#mem-rte-trace-read"
        - "runtime.md#rt-rte-desktop-analysis"
        - "memory.md#mem-obj-halo-run-turns"
        - "memory.md#mem-bap-followup-history"
        - "memory.md#mem-obj-agent-context"
        - "runtime.md#rt-rte-checkpoint-emission"
        - "memory.md#mem-obj-evaluation-report"
        - "epistemic.md#epi-rte-task-evaluation"
        - "runtime.md#rt-rte-report-handoff"
        - "runtime.md#rt-cmp-root-agent"
        - "runtime.md#rt-cmp-subagent"
        - "runtime.md#rt-cmp-synthesis-model"
        - "runtime.md#rt-cmp-compaction-model"
      note: "Positive local trace-fed retained-context routes coexist with unresolved alternatives. No bounded absence record supports a local or system-wide no. The axis does not assert parameter training, observed improvement, autonomy or closed self-improvement."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Execution evidence feeding durable desktop diagnoses"
          assessment: "partial"
          findings:
            - value: "event-streams"
              basis: "wired"
              records:
                - "memory.md#mem-obj-traces-jsonl"
                - "memory.md#mem-rte-trace-read"
                - "runtime.md#rt-rte-desktop-analysis"
                - "memory.md#mem-obj-halo-run-turns"
                - "memory.md#mem-bap-followup-history"
              note: "Captured spans record discrete harness execution events with times/status/attributes; diagnostic generation consumes their evidence before durable answer admission."
          records:
            - "memory.md#mem-obj-traces-jsonl"
            - "memory.md#mem-rte-telemetry-admission"
            - "memory.md#mem-rte-trace-read"
            - "runtime.md#rt-rte-desktop-analysis"
            - "memory.md#mem-obj-halo-run-turns"
            - "memory.md#mem-bap-followup-history"
          note: "Retained spans supply execution-event evidence. Prompt/output payloads may also carry session or tool activity, but adapter fidelity and arbitrary input provenance prevent a complete original-content classification."
        - scope: "Recorded conversation turns used by optional checkpoint compaction"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-agent-context"
                - "runtime.md#rt-rte-checkpoint-emission"
              note: "User and assistant conversation items are recorded session turns consumed by the automatic summarizer."
          records:
            - "memory.md#mem-obj-agent-context"
            - "runtime.md#rt-rte-checkpoint-emission"
          note: "Compaction reads selected non-system conversation items; host persistence/later consumption remains afforded."
        - scope: "Recorded grouped tool turns used by optional checkpoint compaction"
          assessment: "known"
          findings:
            - value: "tool-traces"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-agent-context"
                - "runtime.md#rt-rte-checkpoint-emission"
              note: "Selected recorded tool calls and results feed automatic continuation summaries."
          records:
            - "memory.md#mem-obj-agent-context"
            - "runtime.md#rt-rte-checkpoint-emission"
          note: "Tool names/argument shapes/result facts are explicit summarizer inputs; accompanying assistant text can be omitted."
        - scope: "Unknown initial continuation and external evaluation-driven update source"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-agent-context"
            - "memory.md#mem-obj-evaluation-report"
            - "epistemic.md#epi-rte-task-evaluation"
            - "runtime.md#rt-rte-report-handoff"
          note: "The accepted records do not establish original inputs to a qualifying automatic update on these alternatives; imported guidance and saved scores alone do not identify a trace source."
        - scope: "Included opaque provider-side retained or caching state, if any; not the inference weights as shipped machinery"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-root-agent"
            - "runtime.md#rt-cmp-subagent"
            - "runtime.md#rt-cmp-synthesis-model"
            - "runtime.md#rt-cmp-compaction-model"
          note: "The accepted model-component records leave provider internals uninspected. Local inference and cache-oriented configuration do not classify provider-side use-acquired memory for this axis: trace source."
      records:
        - "memory.md#mem-obj-traces-jsonl"
        - "memory.md#mem-rte-telemetry-admission"
        - "memory.md#mem-rte-trace-read"
        - "runtime.md#rt-rte-desktop-analysis"
        - "memory.md#mem-obj-halo-run-turns"
        - "memory.md#mem-bap-followup-history"
        - "memory.md#mem-obj-agent-context"
        - "runtime.md#rt-rte-checkpoint-emission"
        - "memory.md#mem-obj-evaluation-report"
        - "epistemic.md#epi-rte-task-evaluation"
        - "runtime.md#rt-rte-report-handoff"
        - "runtime.md#rt-cmp-root-agent"
        - "runtime.md#rt-cmp-subagent"
        - "runtime.md#rt-cmp-synthesis-model"
        - "runtime.md#rt-cmp-compaction-model"
      note: "Source classifications follow original content, not adapter labels. Session/tool sources are supported on the checkpoint branch; execution-event sources are supported on the durable diagnosis branch. No linked state/action/outcome trajectory input is established, and opaque alternatives prevent complete enumeration."
---

# Halo memory profile

## Comparison rationale

The inventory follows the accepted memory account, including alternative checkpoint and caller-continuation paths. Reconciliation establishes no supersessions: the trace store and its evidence projections, conversation and answer parts, compaction summary and context container, report artifact and materialization route, and evaluation artifact and tracker remain distinct records. Classification cites their declaring members, not reconciliation as evidence.

The central positive trace-learning route is not raw-log retention. Trace evidence feeds model diagnosis; the desktop automatically retains the selected answer; a later follow-up receives that answer as context. This supports wired trace learning without observed improvement or parameter updates. The bridge's nonempty last-assistant fallback and the history selector's disregard for assistant status limit the epistemic warrant, not the existence of the retained-context route. See [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis), [MEM-OBJ-halo-run-turns](memory.md#mem-obj-halo-run-turns) and [MEM-BAP-followup-history](memory.md#mem-bap-followup-history).

Checkpoint production is wired consolidation, but its qualifying durable learning/read-back chain is only afforded: a host must retain and re-supply emitted messages. Desktop does neither. Recent originals, failed units and summaries can coexist, and replay does not recreate the backing original-item index. Local get_context_item and ordinary retry input are working-context controls, not separate durable memory routes. See [RT-RTE-checkpoint-emission](runtime.md#rt-rte-checkpoint-emission), [MEM-OBJ-agent-context](memory.md#mem-obj-agent-context) and [MEM-RTE-context-reload](memory.md#mem-rte-context-reload).

The epistemic report leaves the semantic relation of an unseen summary indeterminate. That does not defeat the curation classification: the inspected compactor reduces retained items into summaries, while semantic faithfulness remains unchecked. Conversely, the name trace synthesis and an unseen diagnostic answer do not establish novel-claim synthesis. See [EPI-OBJ-compaction-summary](epistemic.md#epi-obj-compaction-summary) and [RT-RTE-trace-synthesis](runtime.md#rt-rte-trace-synthesis).

Read-back direction is classified by operation. A new question requests analysis, not the particular old answers: the host automatically selects and supplies history, so that operation is push. Run matching provides identifier targeting; chronological/role/content filtering provides a separate coarse signal. Explicit trace retrieval and report reading are pull. Automatic terminal report preparation and requested preparation remain separate triggers even though their renderer is shared. See [MEM-OBJ-halo-run-turns](memory.md#mem-obj-halo-run-turns) and [WF-RTE-report-materialization](workflow.md#wf-rte-report-materialization).

Retained conversation supplies knowledge at follow-up: historical user questions remain conversational context, not evidenced standing directions. Preserving their user role does not establish instruction authority. The accepted history records therefore do not support a positive acquired-memory instruction finding; the caller-supplied retained system-guidance alternative remains unresolved. See [MEM-OBJ-halo-run-turns](memory.md#mem-obj-halo-run-turns) and [MEM-BAP-followup-history](memory.md#mem-bap-followup-history).

A materialized report is a deterministic conversation projection, not independent acceptance of its findings. Its external knowledge consumer is afforded; the path-bearing directive and static skill are not newly acquired instruction memory. Saved evaluation results likewise afford evidence consumption but do not establish automatic instruction revision. See [MEM-OBJ-report](memory.md#mem-obj-report), [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff) and [MEM-OBJ-evaluation-report](memory.md#mem-obj-evaluation-report).

Partial axes preserve positives without converting uninspected provider state, arbitrary telemetry payloads, unknown initial continuation provenance, adapter fidelity or host checkpoint policy into absence. Remote inference bindings do not by themselves establish model-weights storage or parametric form for use-acquired memory. Static prompts, engine installation and arbitrary external harness changes are excluded for their functional role, not because their storage is unknown. See [MEM-OBJ-traces-jsonl](memory.md#mem-obj-traces-jsonl), [MEM-OBJ-agent-context](memory.md#mem-obj-agent-context) and [RT-CMP-root-agent](runtime.md#rt-cmp-root-agent).

Source-read log: none. This profile uses only the supplied accepted records and annotations; it adds no evidence, declarations or source facts. No observed or causally supported finding is asserted.
