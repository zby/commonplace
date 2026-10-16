---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "SoL-Pi memory comparison: retained observation/log archives, diagnostic receipts, compaction state and summaries, Skill handoffs and Visual crop reuse."
run-id: "AAS-2026-10-14-sol-pi-42f04fbbc6bb-01"
source-identity: "https://github.com/NVlabs/SoL-Pi"
reviewed-boundary: "41fa7e0e230bedc5e639aed2e7b9cc5698726db1"
memory-comparison:
  version: 2
  scope: "Included: accumulated ObservationPack text archives, replay metadata and ledger; reducer raw-log archives, retained receipts and journals; OCC retained plan/progress/control estimates and native replacement summary/recent tail; Skill host transcripts, persisted exported prompts, child event/session records and result handbacks; Visual retained crop PNGs and receipts, including same-input reuse. Includes unresolved original host-summary/image admission and opaque native persistence/selection where material. Excluded: static shipped prompts/policies, ordinary untransformed tool returns, general configuration, arbitrary workspace edits without a demonstrated memory consumer, and external model weights not established as changing through use."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Observation text archives, reducer raw-log files, Skill prompt/events/session/result files, and Visual PNG/receipt cache"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observation"
                - "memory.md#mem-obj-archive-object"
                - "memory.md#mem-obj-context-export"
                - "memory.md#mem-obj-run-result"
                - "memory.md#mem-obj-magnify-artifact"
                - "runtime.md#rt-rte-skill-handoff"
              note: "The records identify concrete local file paths, including session JSONL in the Skill launcher. Temporary/no-session archive roots still contain files."
          records:
            - "memory.md#mem-obj-observation"
            - "memory.md#mem-obj-archive-object"
            - "memory.md#mem-obj-context-export"
            - "memory.md#mem-obj-run-result"
            - "memory.md#mem-obj-magnify-artifact"
            - "runtime.md#rt-rte-skill-handoff"
          note: "The records identify concrete local file paths, including session JSONL in the Skill launcher. Temporary/no-session archive roots still contain files."
        - scope: "Observation replay-count access map and OCC pending selection state"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observation"
                - "runtime.md#rt-obj-online-state"
                - "runtime.md#rt-rte-observation-replay"
                - "runtime.md#rt-rte-online-compaction"
              note: "Root/id replay counts and pending selection/continuation objects reside in process memory; retained session estimates are separately classified."
          records:
            - "memory.md#mem-obj-observation"
            - "runtime.md#rt-obj-online-state"
            - "runtime.md#rt-rte-observation-replay"
            - "runtime.md#rt-rte-online-compaction"
          note: "Root/id replay counts and pending selection/continuation objects reside in process memory; retained session estimates are separately classified."
        - scope: "Core Pi custom entries, persisted receipt history, and native summary/recent-tail backing store"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-online-state"
            - "memory.md#mem-obj-reducer-journal"
            - "memory.md#mem-obj-validated-receipt"
            - "runtime.md#rt-rte-online-compaction"
          note: "The records establish session retention and later consumption, but not a complete physical substrate inventory outside the shipped Skill file route. No database or service substrate is inferred from the host API."
      records:
        - "memory.md#mem-obj-observation"
        - "memory.md#mem-obj-archive-object"
        - "memory.md#mem-obj-context-export"
        - "memory.md#mem-obj-run-result"
        - "memory.md#mem-obj-magnify-artifact"
        - "runtime.md#rt-rte-skill-handoff"
        - "runtime.md#rt-obj-online-state"
        - "runtime.md#rt-rte-observation-replay"
        - "runtime.md#rt-rte-online-compaction"
        - "memory.md#mem-obj-reducer-journal"
        - "memory.md#mem-obj-validated-receipt"
      note: "Local archives, exported prompts, run records and crop caches are files; replay counters are in memory. Pi custom entries and native replacement context have an external persistence contract not fully specified by these records."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Observation/log text, receipt quotations, progress strings, exported transcript and selected final answer"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observation"
                - "memory.md#mem-obj-archive-object"
                - "memory.md#mem-obj-validated-receipt"
                - "memory.md#mem-obj-progress-summary"
                - "memory.md#mem-obj-context-export"
                - "memory.md#mem-obj-run-result"
              note: "These parts carry language interpreted as task reference, assertions or evidence, distinct from metadata."
          records:
            - "memory.md#mem-obj-observation"
            - "memory.md#mem-obj-archive-object"
            - "memory.md#mem-obj-validated-receipt"
            - "memory.md#mem-obj-progress-summary"
            - "memory.md#mem-obj-context-export"
            - "memory.md#mem-obj-run-result"
          note: "These parts carry language interpreted as task reference, assertions or evidence, distinct from metadata."
        - scope: "Observation identities/counts; receipt status/provenance and labels; journal accounting; OCC plan/status/estimates; Skill status/cost/provenance; crop receipt"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observation"
                - "memory.md#mem-obj-validated-receipt"
                - "epistemic.md#epi-obj-receipt-labels"
                - "memory.md#mem-obj-reducer-journal"
                - "runtime.md#rt-obj-online-state"
                - "memory.md#mem-obj-progress-summary"
                - "memory.md#mem-obj-run-result"
                - "memory.md#mem-obj-magnify-artifact"
              note: "These parts are localized ids, enums, hashes, booleans, numeric estimates or structured associations used by fixed parsing, selection or accounting rules."
          records:
            - "memory.md#mem-obj-observation"
            - "memory.md#mem-obj-validated-receipt"
            - "epistemic.md#epi-obj-receipt-labels"
            - "memory.md#mem-obj-reducer-journal"
            - "runtime.md#rt-obj-online-state"
            - "memory.md#mem-obj-progress-summary"
            - "memory.md#mem-obj-run-result"
            - "memory.md#mem-obj-magnify-artifact"
          note: "These parts are localized ids, enums, hashes, booleans, numeric estimates or structured associations used by fixed parsing, selection or accounting rules."
        - scope: "Native compaction summary delivered to the later foreground invocation"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-online-compaction"
              note: "The recorded host contract supplies a natural-language summary; this classifies its described form, not the correctness or implementation of its generation."
          records:
            - "runtime.md#rt-rte-online-compaction"
          note: "The recorded host contract supplies a natural-language summary; this classifies its described form, not the correctness or implementation of its generation."
        - scope: "Visual crop pixel payload at foreground-model consumption"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-magnify-artifact"
            - "runtime.md#rt-rte-visual-inspection"
          note: "The inspected artifact is sampled PNG raster data, not learned weights. Its decoder/provenance metadata is symbolic, but the records do not establish a controlled representational-form value for the image semantics consumed by the model."
      records:
        - "memory.md#mem-obj-observation"
        - "memory.md#mem-obj-archive-object"
        - "memory.md#mem-obj-validated-receipt"
        - "memory.md#mem-obj-progress-summary"
        - "memory.md#mem-obj-context-export"
        - "memory.md#mem-obj-run-result"
        - "epistemic.md#epi-obj-receipt-labels"
        - "memory.md#mem-obj-reducer-journal"
        - "runtime.md#rt-obj-online-state"
        - "memory.md#mem-obj-magnify-artifact"
        - "runtime.md#rt-rte-online-compaction"
        - "runtime.md#rt-rte-visual-inspection"
      note: "Text and fixed-rule metadata are separately classified. The native summary is described as natural language, but retained image pixels do not have an established mapping to the controlled forms at the model consumption path."
    lineage:
      assessment: "partial"
      units:
        - scope: "Observation and reducer raw text acquisition"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observation"
                - "memory.md#mem-obj-archive-object"
                - "runtime.md#rt-rte-observation-replay"
                - "runtime.md#rt-rte-reducer-receipt"
              note: "Archive acquisition copies originating tool material rather than creating its assertions."
          records:
            - "memory.md#mem-obj-observation"
            - "memory.md#mem-obj-archive-object"
            - "runtime.md#rt-rte-observation-replay"
            - "runtime.md#rt-rte-reducer-receipt"
          note: "Text is imported from tool results or a safely loaded full-output file; the originating tool may itself contain external or authored material whose provenance is unresolved."
        - scope: "Reducer selected quotes and diagnostic labels"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-validated-receipt"
                - "epistemic.md#epi-obj-receipt-labels"
                - "runtime.md#rt-rte-reducer-receipt"
              note: "A separate model extracts quotations and supplies judgments from one tool-result trace; code admits the resulting receipt."
          records:
            - "memory.md#mem-obj-validated-receipt"
            - "epistemic.md#epi-obj-receipt-labels"
            - "runtime.md#rt-rte-reducer-receipt"
          note: "A separate model extracts quotations and supplies judgments from one tool-result trace; code admits the resulting receipt."
        - scope: "OCC model-supplied plan and progress statements"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-online-state"
                - "memory.md#mem-obj-progress-summary"
                - "runtime.md#rt-rte-online-compaction"
              note: "The foreground model authors update_plan content; persistence does not independently verify its assertions."
          records:
            - "runtime.md#rt-obj-online-state"
            - "memory.md#mem-obj-progress-summary"
            - "runtime.md#rt-rte-online-compaction"
          note: "The foreground model authors update_plan content; persistence does not independently verify its assertions."
        - scope: "OCC measured request/growth/debt estimates and reducer decision journal"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-online-state"
                - "memory.md#mem-obj-reducer-journal"
                - "runtime.md#rt-rte-online-compaction"
                - "runtime.md#rt-rte-reducer-receipt"
              note: "Runtime activity is transformed into retained estimates and admission/accounting entries."
          records:
            - "runtime.md#rt-obj-online-state"
            - "memory.md#mem-obj-reducer-journal"
            - "runtime.md#rt-rte-online-compaction"
            - "runtime.md#rt-rte-reducer-receipt"
          note: "Runtime activity is transformed into retained estimates and admission/accounting entries."
        - scope: "Skill selected transcript prefix and aggregated run result"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-export"
                - "memory.md#mem-obj-run-result"
                - "runtime.md#rt-rte-skill-handoff"
              note: "The exporter and summarizer select/trim recorded conversation, tool results, session entries and final assistant text. Their derived objects are trace-extracted, not evidence that every original claim was generated locally."
          records:
            - "memory.md#mem-obj-context-export"
            - "memory.md#mem-obj-run-result"
            - "runtime.md#rt-rte-skill-handoff"
          note: "The exporter and summarizer select/trim recorded conversation, tool results, session entries and final assistant text. Their derived objects are trace-extracted, not evidence that every original claim was generated locally."
        - scope: "Native summary/recent tail and imported host compaction summaries"
          assessment: "partial"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-online-compaction"
              note: "The wired compaction contract transforms accumulated history into later replacement context; internal transformation details remain opaque."
          records:
            - "runtime.md#rt-rte-online-compaction"
            - "memory.md#mem-obj-context-export"
          note: "The summary derives from history, and the tail preserves selected history, but native generation and imported-summary provenance are not inspected."
        - scope: "Visual crop outputs and their initial image inputs"
          assessment: "partial"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-magnify-artifact"
              note: "Crop pixels and receipt are computed from source image bytes, coordinates and helper identity rather than learned parameters."
          records:
            - "memory.md#mem-obj-magnify-artifact"
            - "runtime.md#rt-rte-visual-inspection"
          note: "The helper deterministically crops/resamples supplied images. The records do not establish whether each source image was acquired, rendered during work or otherwise initialized."
      records:
        - "memory.md#mem-obj-observation"
        - "memory.md#mem-obj-archive-object"
        - "runtime.md#rt-rte-observation-replay"
        - "runtime.md#rt-rte-reducer-receipt"
        - "memory.md#mem-obj-validated-receipt"
        - "epistemic.md#epi-obj-receipt-labels"
        - "runtime.md#rt-obj-online-state"
        - "memory.md#mem-obj-progress-summary"
        - "runtime.md#rt-rte-online-compaction"
        - "memory.md#mem-obj-reducer-journal"
        - "memory.md#mem-obj-context-export"
        - "memory.md#mem-obj-run-result"
        - "runtime.md#rt-rte-skill-handoff"
        - "memory.md#mem-obj-magnify-artifact"
        - "runtime.md#rt-rte-visual-inspection"
      note: "Known production paths are retained without treating a tool name, imported host summary or image source as complete initial provenance."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Observation excerpts/pages, reducer quotations/labels, Skill prefix/final report and crop pixels at later foreground consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observation"
                - "memory.md#mem-obj-validated-receipt"
                - "epistemic.md#epi-obj-receipt-labels"
                - "memory.md#mem-obj-context-export"
                - "memory.md#mem-obj-run-result"
                - "memory.md#mem-obj-magnify-artifact"
                - "runtime.md#rt-rte-observation-replay"
                - "runtime.md#rt-rte-reducer-receipt"
                - "runtime.md#rt-rte-skill-handoff"
                - "runtime.md#rt-rte-visual-inspection"
              note: "Delivered retained content supplies advisory evidence/reference context. It neither certifies task correctness nor becomes an enforced system policy."
          records:
            - "memory.md#mem-obj-observation"
            - "memory.md#mem-obj-validated-receipt"
            - "epistemic.md#epi-obj-receipt-labels"
            - "memory.md#mem-obj-context-export"
            - "memory.md#mem-obj-run-result"
            - "memory.md#mem-obj-magnify-artifact"
            - "runtime.md#rt-rte-observation-replay"
            - "runtime.md#rt-rte-reducer-receipt"
            - "runtime.md#rt-rte-skill-handoff"
            - "runtime.md#rt-rte-visual-inspection"
          note: "Delivered retained content supplies advisory evidence/reference context. It neither certifies task correctness nor becomes an enforced system policy."
        - scope: "Native summary at later foreground invocation"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-online-compaction"
              note: "Replacement summary supplies task context after compaction; fidelity and compliance remain unobserved."
          records:
            - "runtime.md#rt-rte-online-compaction"
          note: "Replacement summary supplies task context after compaction; fidelity and compliance remain unobserved."
        - scope: "Retained raw log at reducer; history at native summarizer; host transcript at exporter; child events/session entries at result summarizer"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-archive-object"
                - "memory.md#mem-obj-validated-receipt"
                - "memory.md#mem-obj-context-export"
                - "memory.md#mem-obj-run-result"
                - "runtime.md#rt-rte-reducer-receipt"
                - "runtime.md#rt-rte-online-compaction"
                - "runtime.md#rt-rte-skill-handoff"
              note: "Retained experience feeds automatic construction of durable behavior-shaping receipts, summaries, prefixes and handbacks. This learning authority belongs to each update consumer, not automatically to all raw-log storage."
          records:
            - "memory.md#mem-obj-archive-object"
            - "memory.md#mem-obj-validated-receipt"
            - "memory.md#mem-obj-context-export"
            - "memory.md#mem-obj-run-result"
            - "runtime.md#rt-rte-reducer-receipt"
            - "runtime.md#rt-rte-online-compaction"
            - "runtime.md#rt-rte-skill-handoff"
          note: "Retained experience feeds automatic construction of durable behavior-shaping receipts, summaries, prefixes and handbacks. This learning authority belongs to each update consumer, not automatically to all raw-log storage."
        - scope: "Trace-derived OCC estimates and plan state at later turn-end selection; replay counts at context projection"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-online-state"
                - "memory.md#mem-obj-observation"
                - "runtime.md#rt-rte-online-compaction"
                - "runtime.md#rt-rte-observation-replay"
              note: "Retained state selects whether/when to compact or which replay representation to supply. It changes operation/input-window choice, not a verified task outcome."
          records:
            - "runtime.md#rt-obj-online-state"
            - "memory.md#mem-obj-observation"
            - "runtime.md#rt-rte-online-compaction"
            - "runtime.md#rt-rte-observation-replay"
          note: "Retained state selects whether/when to compact or which replay representation to supply. It changes operation/input-window choice, not a verified task outcome."
        - scope: "Active-branch session-entry metadata at restore and run-status metadata at notification/status selection"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-online-state"
                - "memory.md#mem-obj-run-result"
                - "runtime.md#rt-rte-online-compaction"
                - "runtime.md#rt-rte-skill-handoff"
              note: "Custom-entry type/validity/recency selects restored state; run identity/status selects the stored result and notification timing."
          records:
            - "runtime.md#rt-obj-online-state"
            - "memory.md#mem-obj-run-result"
            - "runtime.md#rt-rte-online-compaction"
            - "runtime.md#rt-rte-skill-handoff"
          note: "Custom-entry type/validity/recency selects restored state; run identity/status selects the stored result and notification timing."
        - scope: "Existing observation/archive content and existing Visual receipt/output hashes at integrity admission"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observation"
                - "memory.md#mem-obj-archive-object"
                - "memory.md#mem-obj-magnify-artifact"
                - "runtime.md#rt-rte-observation-replay"
                - "runtime.md#rt-rte-reducer-receipt"
              note: "Existing retained bytes supply conformance references for reuse; mismatches reject reuse or throw rather than silently overwriting. The same checks provide a veto as well as a criterion."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observation"
                - "memory.md#mem-obj-archive-object"
                - "memory.md#mem-obj-magnify-artifact"
                - "runtime.md#rt-rte-observation-replay"
                - "runtime.md#rt-rte-reducer-receipt"
              note: "Existing retained bytes supply conformance references for reuse; mismatches reject reuse or throw rather than silently overwriting. The same checks provide a veto as well as a criterion."
          records:
            - "memory.md#mem-obj-observation"
            - "memory.md#mem-obj-archive-object"
            - "memory.md#mem-obj-magnify-artifact"
            - "runtime.md#rt-rte-observation-replay"
            - "runtime.md#rt-rte-reducer-receipt"
          note: "Existing retained bytes supply conformance references for reuse; mismatches reject reuse or throw rather than silently overwriting. The same checks provide a veto as well as a criterion."
        - scope: "Reducer decision journal at Skill accounting consumer"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-reducer-journal"
                - "memory.md#mem-obj-run-result"
                - "runtime.md#rt-rte-skill-handoff"
              note: "Session entries supply evidence for reported usage, counts and costs; no learned reducer policy or task-correctness authority follows."
          records:
            - "memory.md#mem-obj-reducer-journal"
            - "memory.md#mem-obj-run-result"
            - "runtime.md#rt-rte-skill-handoff"
          note: "Session entries supply evidence for reported usage, counts and costs; no learned reducer policy or task-correctness authority follows."
        - scope: "PendingProgress as independently delivered checkpoint; ObservationPack ledger; opaque native summary-selection metadata"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-progress-summary"
            - "memory.md#mem-obj-observation"
            - "runtime.md#rt-rte-online-compaction"
          note: "Parsing progress is not a dedicated task-content prompt consumer. No later policy consumer of the pack ledger is established. Native internal selection is not inspected; additional authority cannot be inferred."
      records:
        - "memory.md#mem-obj-observation"
        - "memory.md#mem-obj-validated-receipt"
        - "epistemic.md#epi-obj-receipt-labels"
        - "memory.md#mem-obj-context-export"
        - "memory.md#mem-obj-run-result"
        - "memory.md#mem-obj-magnify-artifact"
        - "runtime.md#rt-rte-observation-replay"
        - "runtime.md#rt-rte-reducer-receipt"
        - "runtime.md#rt-rte-skill-handoff"
        - "runtime.md#rt-rte-visual-inspection"
        - "runtime.md#rt-rte-online-compaction"
        - "memory.md#mem-obj-archive-object"
        - "runtime.md#rt-obj-online-state"
        - "memory.md#mem-obj-reducer-journal"
        - "memory.md#mem-obj-progress-summary"
      note: "Knowledge, learning, routing, validation and enforcement are supported on named consumption paths. Opaque native selection and unconsumed progress/ledger parts prevent a complete authority inventory; static shipped policies are excluded."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Observation/archive admission, reducer receipt/journal admission, OCC plan/estimate updates, Skill export/result creation, Visual crop/cache admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observation"
                - "memory.md#mem-obj-archive-object"
                - "memory.md#mem-obj-validated-receipt"
                - "memory.md#mem-obj-reducer-journal"
                - "runtime.md#rt-obj-online-state"
                - "memory.md#mem-obj-progress-summary"
                - "memory.md#mem-obj-context-export"
                - "memory.md#mem-obj-run-result"
                - "memory.md#mem-obj-magnify-artifact"
                - "runtime.md#rt-rte-observation-replay"
                - "runtime.md#rt-rte-reducer-receipt"
                - "runtime.md#rt-rte-online-compaction"
                - "runtime.md#rt-rte-skill-handoff"
                - "runtime.md#rt-rte-visual-inspection"
              note: "Code and models select, validate and admit content without an explicit human decision approving each retained item."
          records:
            - "memory.md#mem-obj-observation"
            - "memory.md#mem-obj-archive-object"
            - "memory.md#mem-obj-validated-receipt"
            - "memory.md#mem-obj-reducer-journal"
            - "runtime.md#rt-obj-online-state"
            - "memory.md#mem-obj-progress-summary"
            - "memory.md#mem-obj-context-export"
            - "memory.md#mem-obj-run-result"
            - "memory.md#mem-obj-magnify-artifact"
            - "runtime.md#rt-rte-observation-replay"
            - "runtime.md#rt-rte-reducer-receipt"
            - "runtime.md#rt-rte-online-compaction"
            - "runtime.md#rt-rte-skill-handoff"
            - "runtime.md#rt-rte-visual-inspection"
          note: "Code and models select, validate and admit content without an explicit human decision approving each retained item."
        - scope: "Requested native compaction commit through Pi callback and continuation contract"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-online-compaction"
              note: "The extension automatically requests summarization and consumes commit/refusal; a manual/native trigger is an alternate initiation path, not evidence of per-summary human approval."
          records:
            - "runtime.md#rt-rte-online-compaction"
          note: "The extension automatically requests summarization and consumes commit/refusal; a manual/native trigger is an alternate initiation path, not evidence of per-summary human approval."
        - scope: "Initial host transcript/summary and source-image content admission before the inspected transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-context-export"
            - "memory.md#mem-obj-magnify-artifact"
            - "runtime.md#rt-rte-skill-handoff"
            - "runtime.md#rt-rte-visual-inspection"
          note: "Generic caller identity and selected file paths do not identify a human content decision or software-only admission for every original input. No manual value is asserted from an operator starting the workflow."
      records:
        - "memory.md#mem-obj-observation"
        - "memory.md#mem-obj-archive-object"
        - "memory.md#mem-obj-validated-receipt"
        - "memory.md#mem-obj-reducer-journal"
        - "runtime.md#rt-obj-online-state"
        - "memory.md#mem-obj-progress-summary"
        - "memory.md#mem-obj-context-export"
        - "memory.md#mem-obj-run-result"
        - "memory.md#mem-obj-magnify-artifact"
        - "runtime.md#rt-rte-observation-replay"
        - "runtime.md#rt-rte-reducer-receipt"
        - "runtime.md#rt-rte-online-compaction"
        - "runtime.md#rt-rte-skill-handoff"
        - "runtime.md#rt-rte-visual-inspection"
      note: "Inspected ongoing admissions are software/model controlled. Workflow initiation and manual compaction initiation are not per-content approval; original host checkpoint/transcript/image admission remains unresolved."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Reducer exact-quote selection and ObservationPack reduced replay display"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-validated-receipt"
                - "memory.md#mem-obj-observation"
                - "runtime.md#rt-rte-reducer-receipt"
                - "runtime.md#rt-rte-observation-replay"
              note: "Existing retained log/message content is selected into a smaller evidence representation. Packing preserves raw history and does not establish deletion or decay."
          records:
            - "memory.md#mem-obj-validated-receipt"
            - "memory.md#mem-obj-observation"
            - "runtime.md#rt-rte-reducer-receipt"
            - "runtime.md#rt-rte-observation-replay"
          note: "Existing retained log/message content is selected into a smaller evidence representation. Packing preserves raw history and does not establish deletion or decay."
        - scope: "Skill transcript clipping/recent-block selection and result final-text/count aggregation"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-export"
                - "memory.md#mem-obj-run-result"
                - "runtime.md#rt-rte-skill-handoff"
              note: "Recorded content is selected, compressed or combined for later consumers; raw traces may remain."
          records:
            - "memory.md#mem-obj-context-export"
            - "memory.md#mem-obj-run-result"
            - "runtime.md#rt-rte-skill-handoff"
          note: "Recorded content is selected, compressed or combined for later consumers; raw traces may remain."
        - scope: "OCC plan/control estimate revision across provider observations and plan updates"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-online-state"
                - "runtime.md#rt-rte-online-compaction"
              note: "Existing control entries are revised into newer retained state consumed by later context decisions."
          records:
            - "runtime.md#rt-obj-online-state"
            - "runtime.md#rt-rte-online-compaction"
          note: "Existing control entries are revised into newer retained state consumed by later context decisions."
        - scope: "OCC correction/handoff/compaction resets of plan, estimates and pending progress"
          assessment: "known"
          findings:
            - value: "invalidate"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-online-state"
                - "memory.md#mem-obj-progress-summary"
                - "runtime.md#rt-rte-online-compaction"
              note: "Resets withdraw current reliance on the affected fields while earlier custom session entries remain historical. This is not rollback of workspace effects."
          records:
            - "runtime.md#rt-obj-online-state"
            - "memory.md#mem-obj-progress-summary"
            - "runtime.md#rt-rte-online-compaction"
          note: "Resets withdraw current reliance on the affected fields while earlier custom session entries remain historical. This is not rollback of workspace effects."
        - scope: "Native summary transformation"
          assessment: "partial"
          findings:
            - value: "consolidate"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-online-compaction"
              note: "Native summarization is the afforded host transformation; the preservation instruction alone does not verify a faithful implementation."
          records:
            - "runtime.md#rt-rte-online-compaction"
          note: "The host compaction contract requests a reduced replacement of old history, but generator semantics and possible additional operations are not inspected."
        - scope: "Visual cache and raw archive reuse; diagnostic kind/uncertainty semantics"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-magnify-artifact"
            - "memory.md#mem-obj-archive-object"
            - "epistemic.md#epi-obj-receipt-labels"
          note: "Integrity validation, acquisition and collision checks establish no curation operation by themselves. Label semantics are indeterminate; no synthesis, deduplication or other operation is inferred from naming or possible model error."
      records:
        - "memory.md#mem-obj-validated-receipt"
        - "memory.md#mem-obj-observation"
        - "runtime.md#rt-rte-reducer-receipt"
        - "runtime.md#rt-rte-observation-replay"
        - "memory.md#mem-obj-context-export"
        - "memory.md#mem-obj-run-result"
        - "runtime.md#rt-rte-skill-handoff"
        - "runtime.md#rt-obj-online-state"
        - "runtime.md#rt-rte-online-compaction"
        - "memory.md#mem-obj-progress-summary"
        - "memory.md#mem-obj-magnify-artifact"
        - "memory.md#mem-obj-archive-object"
        - "epistemic.md#epi-obj-receipt-labels"
      note: "Inspected trace reductions and control-state revisions coexist with opaque native summarization and cache/input branches whose additional transformations are unresolved. Identity checks alone do not establish deduplication."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Provider-context observation projection and native summary/tail delivery to continuation"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observation"
                - "runtime.md#rt-rte-observation-replay"
                - "runtime.md#rt-rte-online-compaction"
              note: "Code supplies selected retained context without the later foreground invocation requesting each item. The hidden continuation message is a trigger, not a task-specific checkpoint."
          records:
            - "memory.md#mem-obj-observation"
            - "runtime.md#rt-rte-observation-replay"
            - "runtime.md#rt-rte-online-compaction"
          note: "Code supplies selected retained context without the later foreground invocation requesting each item. The hidden continuation message is a trigger, not a task-specific checkpoint."
        - scope: "Observation id/offset recall, Skill CLI status/result/wait/list, and Visual same-input cache read"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-observation-replay"
                - "memory.md#mem-obj-run-result"
                - "runtime.md#rt-rte-skill-handoff"
                - "memory.md#mem-obj-magnify-artifact"
                - "runtime.md#rt-rte-visual-inspection"
              note: "The consumer explicitly requests retained pages, a run result or a crop; fulfillment is pull even when code reads bytes and delivers them."
          records:
            - "runtime.md#rt-rte-observation-replay"
            - "memory.md#mem-obj-run-result"
            - "runtime.md#rt-rte-skill-handoff"
            - "memory.md#mem-obj-magnify-artifact"
            - "runtime.md#rt-rte-visual-inspection"
          note: "The consumer explicitly requests retained pages, a run result or a crop; fulfillment is pull even when code reads bytes and delivers them."
        - scope: "Reducer archive ranged shell read"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-archive-object"
                - "memory.md#mem-obj-validated-receipt"
                - "runtime.md#rt-rte-reducer-receipt"
              note: "Receipt guidance offers an explicit foreground consumer and range-read route; no observed shell reread or separate wired recall executor is established."
          records:
            - "memory.md#mem-obj-archive-object"
            - "memory.md#mem-obj-validated-receipt"
            - "runtime.md#rt-rte-reducer-receipt"
          note: "Receipt guidance offers an explicit foreground consumer and range-read route; no observed shell reread or separate wired recall executor is established."
        - scope: "OCC branch restore and automatic diagnostic-receipt replay"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-online-state"
                - "memory.md#mem-obj-validated-receipt"
                - "runtime.md#rt-rte-online-compaction"
                - "runtime.md#rt-rte-reducer-receipt"
              note: "Restore supplies the latest valid state to extension code; retained substituted receipts enter later foreground context without a specific archive request."
          records:
            - "runtime.md#rt-obj-online-state"
            - "memory.md#mem-obj-validated-receipt"
            - "runtime.md#rt-rte-online-compaction"
            - "runtime.md#rt-rte-reducer-receipt"
          note: "Restore supplies the latest valid state to extension code; retained substituted receipts enter later foreground context without a specific archive request."
        - scope: "Skill transcript request and later automatic child-prefix/parent-notification supply"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-export"
                - "memory.md#mem-obj-run-result"
                - "runtime.md#rt-rte-skill-handoff"
              note: "A caller requests transcript export or CLI result; the selected prefix is supplied to the child and a correlated completion report is supplied to the parent without those model invocations requesting individual historical parts."
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-export"
                - "memory.md#mem-obj-run-result"
                - "runtime.md#rt-rte-skill-handoff"
              note: "A caller requests transcript export or CLI result; the selected prefix is supplied to the child and a correlated completion report is supplied to the parent without those model invocations requesting individual historical parts."
          records:
            - "memory.md#mem-obj-context-export"
            - "memory.md#mem-obj-run-result"
            - "runtime.md#rt-rte-skill-handoff"
          note: "A caller requests transcript export or CLI result; the selected prefix is supplied to the child and a correlated completion report is supplied to the parent without those model invocations requesting individual historical parts."
        - scope: "Independent pendingProgress/pack-ledger consumption and opaque native context-selection alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-progress-summary"
            - "memory.md#mem-obj-observation"
            - "runtime.md#rt-rte-online-compaction"
          note: "No dedicated prompt route for pendingProgress or later pack-ledger policy consumer is established; native internal assembly is external. This does not erase the supported summary delivery."
      records:
        - "memory.md#mem-obj-observation"
        - "runtime.md#rt-rte-observation-replay"
        - "runtime.md#rt-rte-online-compaction"
        - "memory.md#mem-obj-run-result"
        - "runtime.md#rt-rte-skill-handoff"
        - "memory.md#mem-obj-magnify-artifact"
        - "runtime.md#rt-rte-visual-inspection"
        - "memory.md#mem-obj-archive-object"
        - "memory.md#mem-obj-validated-receipt"
        - "runtime.md#rt-rte-reducer-receipt"
        - "runtime.md#rt-obj-online-state"
        - "memory.md#mem-obj-context-export"
        - "memory.md#mem-obj-progress-summary"
      note: "Both automatic supply and requested readback exist. External native cut/assembly and unestablished progress/ledger consumers remain included limitations rather than being silently treated as pull-only."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Observation projection at provider-context construction"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observation"
                - "runtime.md#rt-rte-observation-replay"
              note: "Trigger: context event. Inputs: success/pure-text/size/receipt exclusion and replay count. Selected part: full retained message or literal head/tail placeholder. Root/id keys counts but no targeted relevance match selects evidence."
          records:
            - "memory.md#mem-obj-observation"
            - "runtime.md#rt-rte-observation-replay"
          note: "Trigger: context event. Inputs: success/pure-text/size/receipt exclusion and replay count. Selected part: full retained message or literal head/tail placeholder. Root/id keys counts but no targeted relevance match selects evidence."
        - scope: "Reducer evidence selection for substituted receipt later replay"
          assessment: "known"
          findings:
            - value: "inferred-judgment"
              basis: "wired"
              records:
                - "memory.md#mem-obj-validated-receipt"
                - "epistemic.md#epi-obj-receipt-labels"
                - "runtime.md#rt-rte-reducer-receipt"
              note: "Trigger: eligible diagnostic result. Selector: reducer judgment over the selected log and metadata. Selected part: bounded quotations and kind/uncertainty fields delivered in the admitted receipt."
          records:
            - "memory.md#mem-obj-validated-receipt"
            - "epistemic.md#epi-obj-receipt-labels"
            - "runtime.md#rt-rte-reducer-receipt"
          note: "Trigger: eligible diagnostic result. Selector: reducer judgment over the selected log and metadata. Selected part: bounded quotations and kind/uncertainty fields delivered in the admitted receipt."
        - scope: "Reducer candidate gate before receipt selection"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-archive-object"
                - "runtime.md#rt-rte-reducer-receipt"
              note: "Trigger: tool_result. Command regex, tool class, error metadata, byte limits and secret precaution filter select the candidate retained body; this is coarse eligibility, not lexical relevance search over an archive."
          records:
            - "memory.md#mem-obj-archive-object"
            - "runtime.md#rt-rte-reducer-receipt"
          note: "Trigger: tool_result. Command regex, tool class, error metadata, byte limits and secret precaution filter select the candidate retained body; this is coarse eligibility, not lexical relevance search over an archive."
        - scope: "OCC active-branch restore"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-online-state"
                - "runtime.md#rt-rte-online-compaction"
              note: "Trigger: session start/tree restore. Actual customType identity match selects online-state entries; parser validity and newest-active-branch order choose the retained state supplied to code."
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-online-state"
                - "runtime.md#rt-rte-online-compaction"
              note: "Trigger: session start/tree restore. Actual customType identity match selects online-state entries; parser validity and newest-active-branch order choose the retained state supplied to code."
          records:
            - "runtime.md#rt-obj-online-state"
            - "runtime.md#rt-rte-online-compaction"
          note: "Trigger: session start/tree restore. Actual customType identity match selects online-state entries; parser validity and newest-active-branch order choose the retained state supplied to code."
        - scope: "Skill child-prefix supply"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-export"
                - "runtime.md#rt-rte-skill-handoff"
              note: "Trigger: requested export during handoff. Host compaction point, roles, current-handoff cutoff, recency and character budget select retained transcript blocks. No semantic ranker is established."
          records:
            - "memory.md#mem-obj-context-export"
            - "runtime.md#rt-rte-skill-handoff"
          note: "Trigger: requested export during handoff. Host compaction point, roles, current-handoff cutoff, recency and character budget select retained transcript blocks. No semantic ranker is established."
        - scope: "Skill asynchronous parent notification"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-run-result"
                - "runtime.md#rt-rte-skill-handoff"
              note: "Trigger: correlated submit/notify hook. The recorded run id selects the matching retained result, terminal status permits reporting, and length limits trim final text. Identity targeting and coarse status/budget filtering remain distinct findings."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-run-result"
                - "runtime.md#rt-rte-skill-handoff"
              note: "Trigger: correlated submit/notify hook. The recorded run id selects the matching retained result, terminal status permits reporting, and length limits trim final text. Identity targeting and coarse status/budget filtering remain distinct findings."
          records:
            - "memory.md#mem-obj-run-result"
            - "runtime.md#rt-rte-skill-handoff"
          note: "Trigger: correlated submit/notify hook. The recorded run id selects the matching retained result, terminal status permits reporting, and length limits trim final text. Identity targeting and coarse status/budget filtering remain distinct findings."
        - scope: "Native summary/tail delivery"
          assessment: "partial"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-online-compaction"
              note: "Old history versus recent tail is selected under native context-cut/window constraints; exact summarizer selection is not established."
          records:
            - "runtime.md#rt-rte-online-compaction"
          note: "Chronological native cut and recent-tail selection are described, but host internal selector inputs and summary content decisions are uninspected."
        - scope: "Requested archive pages, CLI result and crop-cache returns"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-observation-replay"
            - "runtime.md#rt-rte-reducer-receipt"
            - "runtime.md#rt-rte-skill-handoff"
            - "memory.md#mem-obj-magnify-artifact"
            - "runtime.md#rt-rte-visual-inspection"
          note: "These are pull operations. Their requested ids/paths/hash keys do not establish an additional identifier-based push signal."
        - scope: "Independent pendingProgress or pack-ledger push"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-progress-summary"
            - "memory.md#mem-obj-observation"
          note: "No implemented later supply channel is established for these retained parts, so no selector value can be assigned."
      records:
        - "memory.md#mem-obj-observation"
        - "runtime.md#rt-rte-observation-replay"
        - "memory.md#mem-obj-validated-receipt"
        - "epistemic.md#epi-obj-receipt-labels"
        - "runtime.md#rt-rte-reducer-receipt"
        - "memory.md#mem-obj-archive-object"
        - "runtime.md#rt-obj-online-state"
        - "runtime.md#rt-rte-online-compaction"
        - "memory.md#mem-obj-context-export"
        - "runtime.md#rt-rte-skill-handoff"
        - "memory.md#mem-obj-run-result"
        - "memory.md#mem-obj-magnify-artifact"
        - "runtime.md#rt-rte-visual-inspection"
        - "memory.md#mem-obj-progress-summary"
      note: "Push selectors are classified separately from identifiers used only on requested reads. Known coarse and judgment-based selection do not resolve the host summarizer or an unestablished checkpoint channel."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Diagnostic tool log to admitted retained receipt to later foreground context"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-archive-object"
                - "memory.md#mem-obj-validated-receipt"
                - "runtime.md#rt-rte-reducer-receipt"
              note: "Automatic model/code selection turns a tool trace into retained behavior-shaping evidence; the later consumer chain is wired, not observed."
          records:
            - "memory.md#mem-obj-archive-object"
            - "memory.md#mem-obj-validated-receipt"
            - "runtime.md#rt-rte-reducer-receipt"
          note: "Automatic model/code selection turns a tool trace into retained behavior-shaping evidence; the later consumer chain is wired, not observed."
        - scope: "Request/context/boundary traces to retained OCC estimates to later compaction decisions"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-online-state"
                - "runtime.md#rt-rte-online-compaction"
              note: "The memory annotation establishes automatic trace-fed control-state adaptation and an actual later code decision consumer."
          records:
            - "runtime.md#rt-obj-online-state"
            - "runtime.md#rt-rte-online-compaction"
          note: "The memory annotation establishes automatic trace-fed control-state adaptation and an actual later code decision consumer."
        - scope: "Accumulated history to native summary to later foreground invocation"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-online-compaction"
              note: "Automatic summary production, host retention/commit and continuation form a qualifying wired chain even though summary-generation internals and fidelity are uninspected."
          records:
            - "runtime.md#rt-rte-online-compaction"
          note: "Automatic summary production, host retention/commit and continuation form a qualifying wired chain even though summary-generation internals and fidelity are uninspected."
        - scope: "Host transcript to persisted prefix to child; child events/session entries to persisted result to parent"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-export"
                - "memory.md#mem-obj-run-result"
                - "runtime.md#rt-rte-skill-handoff"
              note: "Automatic filtering and aggregation produce retained reference/handback artifacts consumed on later invocations. Starting delegation is not per-content human approval."
          records:
            - "memory.md#mem-obj-context-export"
            - "memory.md#mem-obj-run-result"
            - "runtime.md#rt-rte-skill-handoff"
          note: "Automatic filtering and aggregation produce retained reference/handback artifacts consumed on later invocations. Starting delegation is not per-content human approval."
        - scope: "Raw observation archive/replay ledger, pendingProgress as independent checkpoint, and crop cache"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-observation"
            - "memory.md#mem-obj-progress-summary"
            - "memory.md#mem-obj-magnify-artifact"
            - "runtime.md#rt-rte-observation-replay"
            - "runtime.md#rt-rte-visual-inspection"
          note: "Raw trace retention alone does not qualify; the pack placeholder is a context projection rather than an established durable generated artifact, and progress lacks a dedicated prompt readback. Crop input activity origin is not established. These records do not warrant a bounded system-wide no or an extra yes for every part."
      records:
        - "memory.md#mem-obj-archive-object"
        - "memory.md#mem-obj-validated-receipt"
        - "runtime.md#rt-rte-reducer-receipt"
        - "runtime.md#rt-obj-online-state"
        - "runtime.md#rt-rte-online-compaction"
        - "memory.md#mem-obj-context-export"
        - "memory.md#mem-obj-run-result"
        - "runtime.md#rt-rte-skill-handoff"
        - "memory.md#mem-obj-observation"
        - "memory.md#mem-obj-progress-summary"
        - "memory.md#mem-obj-magnify-artifact"
        - "runtime.md#rt-rte-observation-replay"
        - "runtime.md#rt-rte-visual-inspection"
      note: "Qualifying automatic writes produce retained context artifacts or control estimates for later consumers. This is the profile definition of trace learning, not demonstrated capacity improvement. Raw storage and image origins remain separately unresolved."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Reducer receipt update"
          assessment: "known"
          findings:
            - value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-archive-object"
                - "memory.md#mem-obj-validated-receipt"
                - "runtime.md#rt-rte-reducer-receipt"
              note: "Original input is recorded tool diagnostic output, including a fused-command suffix or validated full-output file."
          records:
            - "memory.md#mem-obj-archive-object"
            - "memory.md#mem-obj-validated-receipt"
            - "runtime.md#rt-rte-reducer-receipt"
          note: "Original input is recorded tool diagnostic output, including a fused-command suffix or validated full-output file."
        - scope: "OCC estimate adaptation"
          assessment: "known"
          findings:
            - value: "event-streams"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-online-state"
                - "runtime.md#rt-rte-online-compaction"
              note: "Original inputs include provider request/context observations, boundary/compaction callbacks and successful tool activity. Discrete runtime callbacks supply event-stream content; recorded tool results supply execution feedback."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-online-state"
                - "runtime.md#rt-rte-online-compaction"
              note: "Original inputs include provider request/context observations, boundary/compaction callbacks and successful tool activity. Discrete runtime callbacks supply event-stream content; recorded tool results supply execution feedback."
          records:
            - "runtime.md#rt-obj-online-state"
            - "runtime.md#rt-rte-online-compaction"
          note: "Original inputs include provider request/context observations, boundary/compaction callbacks and successful tool activity. Discrete runtime callbacks supply event-stream content; recorded tool results supply execution feedback."
        - scope: "Native continuation-summary update"
          assessment: "partial"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-online-compaction"
              note: "The host summarizes accumulated agent-session history for a later invocation."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-online-compaction"
              note: "Tool/progress messages occur in the accumulated history selected for compaction; exact coverage remains host-owned."
          records:
            - "runtime.md#rt-rte-online-compaction"
            - "runtime.md#rt-obj-online-state"
          note: "The described source is accumulated conversational/tool history. Exact selected inputs and any additional host-provided material are not inspected."
        - scope: "Skill transcript-prefix update"
          assessment: "partial"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-export"
                - "runtime.md#rt-rte-skill-handoff"
              note: "The exporter consumes recorded conversational turns from the host work session."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-export"
                - "runtime.md#rt-rte-skill-handoff"
              note: "Tool calls and results are rendered and clipped into the persisted child prefix."
          records:
            - "memory.md#mem-obj-context-export"
            - "runtime.md#rt-rte-skill-handoff"
          note: "Selected host user/assistant turns and tool request/results are established; imported host compaction summaries have uninspected derivation and may hide additional provenance."
        - scope: "Skill run-result aggregation"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-run-result"
                - "memory.md#mem-obj-reducer-journal"
                - "runtime.md#rt-rte-skill-handoff"
              note: "Original inputs include recorded assistant session turns, tool execution/mechanism feedback and process/provider event records; JSONL serialization alone supplies none of these values."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-run-result"
                - "memory.md#mem-obj-reducer-journal"
                - "runtime.md#rt-rte-skill-handoff"
              note: "Original inputs include recorded assistant session turns, tool execution/mechanism feedback and process/provider event records; JSONL serialization alone supplies none of these values."
            - value: "event-streams"
              basis: "wired"
              records:
                - "memory.md#mem-obj-run-result"
                - "memory.md#mem-obj-reducer-journal"
                - "runtime.md#rt-rte-skill-handoff"
              note: "Original inputs include recorded assistant session turns, tool execution/mechanism feedback and process/provider event records; JSONL serialization alone supplies none of these values."
          records:
            - "memory.md#mem-obj-run-result"
            - "memory.md#mem-obj-reducer-journal"
            - "runtime.md#rt-rte-skill-handoff"
          note: "Original inputs include recorded assistant session turns, tool execution/mechanism feedback and process/provider event records; JSONL serialization alone supplies none of these values."
        - scope: "Observation/progress/crop branches without an established independent qualifying trace-fed update"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-observation"
            - "memory.md#mem-obj-progress-summary"
            - "memory.md#mem-obj-magnify-artifact"
          note: "Without a qualifying automatic trace-fed durable update on these particular branches, and without a bounded absence record, trace_source cannot be declared inapplicable or assigned from filenames."
      records:
        - "memory.md#mem-obj-archive-object"
        - "memory.md#mem-obj-validated-receipt"
        - "runtime.md#rt-rte-reducer-receipt"
        - "runtime.md#rt-obj-online-state"
        - "runtime.md#rt-rte-online-compaction"
        - "memory.md#mem-obj-context-export"
        - "runtime.md#rt-rte-skill-handoff"
        - "memory.md#mem-obj-run-result"
        - "memory.md#mem-obj-reducer-journal"
        - "memory.md#mem-obj-observation"
        - "memory.md#mem-obj-progress-summary"
        - "memory.md#mem-obj-magnify-artifact"
      note: "Each positive names original content consumed by a qualifying update. Native selected history and initial imported summaries retain their mixed/opaque origins. Event serialization does not turn conversational/tool content into event-stream sources."
---

# SoL-Pi memory profile

## Comparison rationale

The profile classifies retained memory, not every storage or permission surface of the runtime. Exact archives, context replacements, code-consumed control estimates, delegated transcript/result artifacts and reused crops have distinct consumers. General configuration and static Visual/reducer instructions are not accumulated memory. Opaque external model weights are not assumed to change through use merely because a provider is called. The boundary of those components remains described by [RT-CMP-frontier-model](runtime.md#rt-cmp-frontier-model) and [RT-CMP-reducer-model](runtime.md#rt-cmp-reducer-model).

Reconciliation supersedes the epistemic observation, exported-context and crop object declarations with [MEM-OBJ-observation](memory.md#mem-obj-observation), [MEM-OBJ-context-export](memory.md#mem-obj-context-export) and [MEM-OBJ-magnify-artifact](memory.md#mem-obj-magnify-artifact). Profile citations use those canonical objects. Their retained qualifications remain in force: assembled text is not authenticated truth, export can degrade provenance, and crop identity does not establish scene correctness. The receipt container and its quotation/label parts remain distinct, as do [MEM-OBJ-progress-summary](memory.md#mem-obj-progress-summary), [RT-OBJ-online-state](runtime.md#rt-obj-online-state) and the native replacement context in [RT-RTE-online-compaction](runtime.md#rt-rte-online-compaction). No supersession creates a stronger evidence basis.

Trace learning here means an automatic trace-fed durable update with a later consumer. It does not require a new proposition, learned parameters or demonstrated improvement. Receipt selection, exported prefixes, result aggregation, native continuation summaries and trace-derived OCC estimates meet that route definition. Input learning authority and downstream knowledge/routing authority remain separate findings. Raw observation storage alone does not establish another qualifying update, nor does a transient display projection prove a durable generated artifact. No local or system-wide trace-learning negative is manufactured from missing evidence ([RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt), [RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff), [RT-OBJ-online-state](runtime.md#rt-obj-online-state), [MEM-OBJ-observation](memory.md#mem-obj-observation)).

The native-summary chain has wired request, commit/continuation and later-consumption interfaces. Its opaque implementation prevents complete curation, selection, persistence and provenance coverage; it does not erase the supported chain. Consolidation at the native generator is kept at afforded basis. Preservation instructions do not establish faithful summarization, and receipt label uncertainty does not justify asserting synthesis ([RT-RTE-online-compaction](runtime.md#rt-rte-online-compaction), [EPI-OBJ-receipt-labels](epistemic.md#epi-obj-receipt-labels)).

Requests and unsolicited supply are operations within a chain, not competing labels for an entire feature. Observation recall and a requested crop/result return are pull; automatic context projection and correlated completion notification are push. A requested id is not an identifier-based push witness. OCC custom-type matching and Skill run-id correlation do actually select retained parts on automatic supply routes. Coarse eligibility and budget filtering remain separate from those matches and from the reducer's model judgment ([RT-RTE-observation-replay](runtime.md#rt-rte-observation-replay), [RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff), [RT-RTE-online-compaction](runtime.md#rt-rte-online-compaction), [MEM-OBJ-magnify-artifact](memory.md#mem-obj-magnify-artifact)).

All axes retain their included unresolved branches. File paths do not settle every host persistence substrate; sampled image data is not classified as model weights; generic callers do not prove human content admission. No additional source read was performed: the profile uses the supplied accepted records, annotations and reconciliation only. Evidence is implementation or afforded contract, not an observed run, measured benefit or causal experiment.
