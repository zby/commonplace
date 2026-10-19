---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Autogenesis memory comparison: retained execution summaries, plans, corpora, diagnostic products, evaluations and capability/workflow recovery at the frozen revision."
run-id: "AAS-2026-10-15-autogenesis-9bcfa57fd7c1-01"
source-identity: "https://github.com/DVampire/Autogenesis"
reviewed-boundary: "5b070d5cd497e951a188a01409138e8b530eaf4a"
memory-comparison:
  version: 2
  scope: "Included: use-accumulated recent/working tiers and displays, TodoTool plans, corpora/backend access metadata, conversation/chat/feedback, traces/prompt snapshots/trajectories, workflow evaluations and recovery checkpoints, capability version maps, active generated extensions/archives and use-retained skill results; their admission, maintenance and later consumers. Unresolved included alternatives: custom memory/ranking backends, initial/administrative content, feedback/export consumers, full frontend resend, canvas/library and kernel/notebook persistence. Excluded: shipped static prompts/skills by themselves, ordinary unretained current-run state, transient ranker matrices, provider weights/internal retention and external dependencies not established as accumulated memory."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Tiered recent event records"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-recent-history"
              note: "RAM deque; GeneralMemorySystem also serializes records to JSON."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-recent-history"
              note: "RAM deque; GeneralMemorySystem also serializes records to JSON."
          records:
            - "memory.md#mem-obj-recent-history"
          note: "RAM deque; GeneralMemorySystem also serializes records to JSON."
        - scope: "Derived working summaries"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-working-memory"
              note: "Bounded RAM strings with JSON/HTML projections; disk writing does not establish restart reload."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-working-memory"
              note: "Bounded RAM strings with JSON/HTML projections; disk writing does not establish restart reload."
          records:
            - "memory.md#mem-obj-working-memory"
          note: "Bounded RAM strings with JSON/HTML projections; disk writing does not establish restart reload."
        - scope: "Memory display projections"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-display"
              note: "GeneralMemorySystem JSON and built-in/constraint HTML are files, not an executable checkpoint."
          records:
            - "memory.md#mem-obj-memory-display"
          note: "GeneralMemorySystem JSON and built-in/constraint HTML are files, not an executable checkpoint."
        - scope: "Separate todo plan"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-todo-tool"
                - "memory.md#mem-rte-todo-context"
              note: "steps.json reconstructs cached Step objects; todo.md is the separately consumed file."
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-todo-tool"
                - "memory.md#mem-rte-todo-context"
              note: "steps.json reconstructs cached Step objects; todo.md is the separately consumed file."
          records:
            - "memory.md#mem-obj-todo-tool"
            - "memory.md#mem-rte-todo-context"
          note: "steps.json reconstructs cached Step objects; todo.md is the separately consumed file."
        - scope: "Corpus documents and backend manifest"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-corpus"
              note: "corpus.jsonl and manifest.json are the retained objects. BM25/TF-IDF intermediates are rebuilt; no persistent vector index is established."
          records:
            - "memory.md#mem-obj-corpus"
          note: "corpus.jsonl and manifest.json are the retained objects. BM25/TF-IDF intermediates are rebuilt; no persistent vector index is established."
        - scope: "Conversation event transcript"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-events"
              note: "Metadata JSON and event JSONL persist separately from agent memory."
          records:
            - "memory.md#mem-obj-conversation-events"
          note: "Metadata JSON and event JSONL persist separately from agent memory."
        - scope: "Chat text and feedback"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-records"
              note: "Chat, metadata and feedback are independent files."
          records:
            - "memory.md#mem-obj-chat-records"
          note: "Chat, metadata and feedback are independent files."
        - scope: "Trace events and access index"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace-events"
              note: "Session JSONL and index.json are retained disk objects."
          records:
            - "memory.md#mem-obj-trace-events"
          note: "Session JSONL and index.json are retained disk objects."
        - scope: "Rendered message snapshots"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-message-snapshots"
              note: "Numbered HTML snapshots persist rendered messages."
          records:
            - "memory.md#mem-obj-message-snapshots"
          note: "Numbered HTML snapshots persist rendered messages."
        - scope: "Trajectories and reward records"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectories"
              note: "Task-keyed objects are exported to JSONL; the inspected get/export path uses RAM."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectories"
              note: "Task-keyed objects are exported to JSONL; the inspected get/export path uses RAM."
          records:
            - "memory.md#mem-obj-trajectories"
          note: "Task-keyed objects are exported to JSONL; the inspected get/export path uses RAM."
        - scope: "Workflow evaluation ledger"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-workflow-evaluations"
              note: "Evaluation objects persist in evaluations.json and reload at initialization."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-workflow-evaluations"
              note: "Evaluation objects persist in evaluations.json and reload at initialization."
          records:
            - "memory.md#mem-obj-workflow-evaluations"
          note: "Evaluation objects persist in evaluations.json and reload at initialization."
        - scope: "Capability restore-point map"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-version-snapshot"
              note: "Checkpoint JSON stores version pointers, not component source."
          records:
            - "memory.md#mem-obj-version-snapshot"
          note: "Checkpoint JSON stores version pointers, not component source."
        - scope: "Workflow recovery checkpoint"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-workflow-checkpoint"
              note: "Run/frame/invocation JSON is reconstituted as executable recovery state."
            - value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-workflow-checkpoint"
              note: "Run/frame/invocation JSON is reconstituted as executable recovery state."
          records:
            - "runtime.md#rt-obj-workflow-checkpoint"
          note: "Run/frame/invocation JSON is reconstituted as executable recovery state."
        - scope: "Active extension identities, archives and source"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-extension-manifest"
                - "runtime.md#rt-obj-extension-source"
              note: "Active files/archives/manifest persist; loaded classes and registry entries reside in process memory."
            - value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-extension-manifest"
                - "runtime.md#rt-obj-extension-source"
              note: "Active files/archives/manifest persist; loaded classes and registry entries reside in process memory."
          records:
            - "runtime.md#rt-obj-extension-manifest"
            - "runtime.md#rt-obj-extension-source"
          note: "Active files/archives/manifest persist; loaded classes and registry entries reside in process memory."
        - scope: "Included custom memory/backend alternatives, canvas/library and kernel/notebook persistence"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-tier-context"
            - "memory.md#mem-obj-corpus"
            - "memory.md#mem-obj-run-records"
            - "memory.md#mem-rte-memory-admission"
          note: "Untraced implementations may retain other substrates. Provider parameters are outside the accumulated-memory boundary, not evidence for model-weight memory."
      records:
        - "memory.md#mem-obj-recent-history"
        - "memory.md#mem-obj-working-memory"
        - "memory.md#mem-obj-memory-display"
        - "memory.md#mem-obj-todo-tool"
        - "memory.md#mem-rte-todo-context"
        - "memory.md#mem-obj-corpus"
        - "memory.md#mem-obj-conversation-events"
        - "memory.md#mem-obj-chat-records"
        - "memory.md#mem-obj-trace-events"
        - "memory.md#mem-obj-message-snapshots"
        - "memory.md#mem-obj-trajectories"
        - "memory.md#mem-obj-workflow-evaluations"
        - "memory.md#mem-obj-version-snapshot"
        - "runtime.md#rt-obj-workflow-checkpoint"
        - "runtime.md#rt-obj-extension-manifest"
        - "runtime.md#rt-obj-extension-source"
        - "memory.md#mem-rte-tier-context"
        - "memory.md#mem-obj-run-records"
        - "memory.md#mem-rte-memory-admission"
      note: "Files and RAM are established for the named retained objects, not for every included implementation. File encoding is not a database, graph or vector substrate; transient ranker vectors do not establish retained vector storage."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Tiered recent event records text payload"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-recent-history"
              note: "Retained task, result, message, document or note text remains linguistic content."
          records:
            - "memory.md#mem-obj-recent-history"
          note: "Text content is interpreted by people or models, separately from its wrapper."
        - scope: "Tiered recent event records structured fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-recent-history"
              note: "Structured records, IDs, scores, timestamps and serialization/display fields are not distributed model parameters."
          records:
            - "memory.md#mem-obj-recent-history"
          note: "IDs, status, layout or access metadata have localized fixed interpretations."
        - scope: "Derived working summaries prose"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-working-memory"
              note: "CompactHook writes short prose for later model context."
          records:
            - "memory.md#mem-obj-working-memory"
          note: "The consumed summary strings are natural language."
        - scope: "Memory display projections text payload"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-display"
              note: "Retained task, result, message, document or note text remains linguistic content."
          records:
            - "memory.md#mem-obj-memory-display"
          note: "Text content is interpreted by people or models, separately from its wrapper."
        - scope: "Memory display projections structured fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-display"
              note: "Structured records, IDs, scores, timestamps and serialization/display fields are not distributed model parameters."
          records:
            - "memory.md#mem-obj-memory-display"
          note: "IDs, status, layout or access metadata have localized fixed interpretations."
        - scope: "Separate todo plan text payload"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-todo-tool"
                - "memory.md#mem-rte-todo-context"
              note: "Retained task, result, message, document or note text remains linguistic content."
          records:
            - "memory.md#mem-obj-todo-tool"
            - "memory.md#mem-rte-todo-context"
          note: "Text content is interpreted by people or models, separately from its wrapper."
        - scope: "Separate todo plan structured fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-todo-tool"
                - "memory.md#mem-rte-todo-context"
              note: "Structured records, IDs, scores, timestamps and serialization/display fields are not distributed model parameters."
          records:
            - "memory.md#mem-obj-todo-tool"
            - "memory.md#mem-rte-todo-context"
          note: "IDs, status, layout or access metadata have localized fixed interpretations."
        - scope: "Corpus documents and backend manifest text payload"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-corpus"
              note: "Retained task, result, message, document or note text remains linguistic content."
          records:
            - "memory.md#mem-obj-corpus"
          note: "Text content is interpreted by people or models, separately from its wrapper."
        - scope: "Corpus documents and backend manifest structured fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-corpus"
              note: "Structured records, IDs, scores, timestamps and serialization/display fields are not distributed model parameters."
          records:
            - "memory.md#mem-obj-corpus"
          note: "IDs, status, layout or access metadata have localized fixed interpretations."
        - scope: "Conversation event transcript text payload"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-events"
              note: "Retained task, result, message, document or note text remains linguistic content."
          records:
            - "memory.md#mem-obj-conversation-events"
          note: "Text content is interpreted by people or models, separately from its wrapper."
        - scope: "Conversation event transcript structured fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-events"
              note: "Structured records, IDs, scores, timestamps and serialization/display fields are not distributed model parameters."
          records:
            - "memory.md#mem-obj-conversation-events"
          note: "IDs, status, layout or access metadata have localized fixed interpretations."
        - scope: "Chat text and feedback text payload"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-records"
              note: "Retained task, result, message, document or note text remains linguistic content."
          records:
            - "memory.md#mem-obj-chat-records"
          note: "Text content is interpreted by people or models, separately from its wrapper."
        - scope: "Chat text and feedback structured fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-records"
              note: "Structured records, IDs, scores, timestamps and serialization/display fields are not distributed model parameters."
          records:
            - "memory.md#mem-obj-chat-records"
          note: "IDs, status, layout or access metadata have localized fixed interpretations."
        - scope: "Trace events and access index text payload"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace-events"
              note: "Retained task, result, message, document or note text remains linguistic content."
          records:
            - "memory.md#mem-obj-trace-events"
          note: "Text content is interpreted by people or models, separately from its wrapper."
        - scope: "Trace events and access index structured fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace-events"
              note: "Structured records, IDs, scores, timestamps and serialization/display fields are not distributed model parameters."
          records:
            - "memory.md#mem-obj-trace-events"
          note: "IDs, status, layout or access metadata have localized fixed interpretations."
        - scope: "Rendered message snapshots text payload"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-message-snapshots"
              note: "Retained task, result, message, document or note text remains linguistic content."
          records:
            - "memory.md#mem-obj-message-snapshots"
          note: "Text content is interpreted by people or models, separately from its wrapper."
        - scope: "Rendered message snapshots structured fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-message-snapshots"
              note: "Structured records, IDs, scores, timestamps and serialization/display fields are not distributed model parameters."
          records:
            - "memory.md#mem-obj-message-snapshots"
          note: "IDs, status, layout or access metadata have localized fixed interpretations."
        - scope: "Trajectories and reward records text payload"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectories"
              note: "Retained task, result, message, document or note text remains linguistic content."
          records:
            - "memory.md#mem-obj-trajectories"
          note: "Text content is interpreted by people or models, separately from its wrapper."
        - scope: "Trajectories and reward records structured fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectories"
              note: "Structured records, IDs, scores, timestamps and serialization/display fields are not distributed model parameters."
          records:
            - "memory.md#mem-obj-trajectories"
          note: "IDs, status, layout or access metadata have localized fixed interpretations."
        - scope: "Workflow evaluation ledger text payload"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-workflow-evaluations"
              note: "Retained task, result, message, document or note text remains linguistic content."
          records:
            - "memory.md#mem-obj-workflow-evaluations"
          note: "Text content is interpreted by people or models, separately from its wrapper."
        - scope: "Workflow evaluation ledger structured fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-workflow-evaluations"
              note: "Structured records, IDs, scores, timestamps and serialization/display fields are not distributed model parameters."
          records:
            - "memory.md#mem-obj-workflow-evaluations"
          note: "IDs, status, layout or access metadata have localized fixed interpretations."
        - scope: "Capability restore-point map control fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-version-snapshot"
              note: "Component/version pointers or workflow state govern fixed recovery rules."
          records:
            - "memory.md#mem-obj-version-snapshot"
          note: "Localized fields are interpreted by fixed restore/resume code."
        - scope: "Workflow recovery checkpoint control fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-workflow-checkpoint"
              note: "Component/version pointers or workflow state govern fixed recovery rules."
          records:
            - "runtime.md#rt-obj-workflow-checkpoint"
          note: "Localized fields are interpreted by fixed restore/resume code."
        - scope: "Retained extension executable bodies and active/version metadata"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-extension-manifest"
                - "runtime.md#rt-obj-extension-source"
              note: "Dynamic loading executes source and fixed manifest rules select active versions."
          records:
            - "runtime.md#rt-obj-extension-manifest"
            - "runtime.md#rt-obj-extension-source"
          note: "Python executes symbolically; manifest identities have fixed loader meaning."
        - scope: "Natural-language descriptions within retained extensions"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-extension-source"
                - "runtime.md#rt-bap-extension-execution"
              note: "Runtime distinguishes descriptive instruction text influencing model selection from executable methods."
          records:
            - "runtime.md#rt-obj-extension-source"
            - "runtime.md#rt-bap-extension-execution"
          note: "Description strings have an interpretation path distinct from executable bodies."
        - scope: "Included custom memory/backend alternatives, canvas/library and kernel/notebook persistence"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-tier-context"
            - "memory.md#mem-obj-corpus"
            - "memory.md#mem-obj-run-records"
            - "memory.md#mem-rte-memory-admission"
          note: "Custom consumed payloads and untraced persistence can contain other forms; inspected displays cannot classify those payloads."
      records:
        - "memory.md#mem-obj-recent-history"
        - "memory.md#mem-obj-working-memory"
        - "memory.md#mem-obj-memory-display"
        - "memory.md#mem-obj-todo-tool"
        - "memory.md#mem-rte-todo-context"
        - "memory.md#mem-obj-corpus"
        - "memory.md#mem-obj-conversation-events"
        - "memory.md#mem-obj-chat-records"
        - "memory.md#mem-obj-trace-events"
        - "memory.md#mem-obj-message-snapshots"
        - "memory.md#mem-obj-trajectories"
        - "memory.md#mem-obj-workflow-evaluations"
        - "memory.md#mem-obj-version-snapshot"
        - "runtime.md#rt-obj-workflow-checkpoint"
        - "runtime.md#rt-obj-extension-manifest"
        - "runtime.md#rt-obj-extension-source"
        - "runtime.md#rt-bap-extension-execution"
        - "memory.md#mem-rte-tier-context"
        - "memory.md#mem-obj-run-records"
        - "memory.md#mem-rte-memory-admission"
      note: "Natural-language payloads and symbolic control/access fields are split by consumption path. No parametric retained memory is established by transient statistical vectors or use of a remote generator."
    lineage:
      assessment: "partial"
      units:
        - scope: "Recent event projections"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-recent-history"
                - "memory.md#mem-rte-tier-context"
              note: "Task, action output/error and stop events become the retained recent projection."
          records:
            - "memory.md#mem-obj-recent-history"
            - "memory.md#mem-rte-tier-context"
          note: "Selected runtime events supply records; this is not a complete conversational transcript."
        - scope: "Working summary derivation"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-working-memory"
                - "memory.md#mem-rte-tier-context"
              note: "Compaction extracts short execution summaries from selected retained event lines and prior summary."
          records:
            - "memory.md#mem-obj-working-memory"
            - "memory.md#mem-rte-tier-context"
          note: "The known downstream path does not authenticate the original tool/service assertions."
        - scope: "Display, recovery maps, workflow checkpoints and evaluation aggregates"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-display"
                - "memory.md#mem-obj-version-snapshot"
                - "runtime.md#rt-obj-workflow-checkpoint"
                - "memory.md#mem-obj-workflow-evaluations"
                - "epistemic.md#epi-rte-workflow-evidence"
              note: "Renderers, version enumeration, workflow checkpoint serialization and metric aggregation produce derived retained representations."
          records:
            - "memory.md#mem-obj-memory-display"
            - "memory.md#mem-obj-version-snapshot"
            - "runtime.md#rt-obj-workflow-checkpoint"
            - "memory.md#mem-obj-workflow-evaluations"
            - "epistemic.md#epi-rte-workflow-evidence"
          note: "Fixed serialization, snapshot and aggregation paths compile supplied state rather than establish its truth."
        - scope: "Model-authored todo plan and generated extension source"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-todo-tool"
                - "memory.md#mem-rte-todo-context"
                - "runtime.md#rt-rte-capability-admission"
                - "memory.md#mem-rte-memory-admission"
              note: "Plans and generated source are authored content, not demonstrated extraction of a specific trace-fed update."
          records:
            - "memory.md#mem-obj-todo-tool"
            - "memory.md#mem-rte-todo-context"
            - "runtime.md#rt-rte-capability-admission"
            - "memory.md#mem-rte-memory-admission"
          note: "Model/caller authoring paths are known; untraced initial content and administrative alternatives remain separate."
        - scope: "Corpus acquisition"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-corpus"
                - "runtime.md#rt-rte-knowledge-admission"
              note: "Ingest appends supplied documents or upstream data.records."
          records:
            - "memory.md#mem-obj-corpus"
            - "runtime.md#rt-rte-knowledge-admission"
          note: "Import into the corpus is known; initial authorship and upstream truth provenance remain caller-dependent."
        - scope: "Conversation, chat, diagnostic snapshots, trajectories and caller evaluation content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-run-records"
            - "memory.md#mem-obj-chat-records"
            - "memory.md#mem-obj-trajectories"
            - "memory.md#mem-obj-workflow-evaluations"
          note: "Records distinguish event serialization, supplied messages/quality and lifecycle fields, but do not completely resolve initial authorship and all payload derivation paths."
        - scope: "Initial and administratively replaced extension/skill content"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-runtime-configuration"
            - "runtime.md#rt-obj-extension-manifest"
          note: "Configuration lookup and startup loading do not establish the retained content's initial derivation."
        - scope: "Included custom memory/backend alternatives, canvas/library and kernel/notebook persistence"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-tier-context"
            - "memory.md#mem-obj-corpus"
            - "memory.md#mem-obj-run-records"
            - "memory.md#mem-rte-memory-admission"
          note: "Custom initial contents and derivation paths were not traced."
      records:
        - "memory.md#mem-obj-recent-history"
        - "memory.md#mem-rte-tier-context"
        - "memory.md#mem-obj-working-memory"
        - "memory.md#mem-obj-memory-display"
        - "memory.md#mem-obj-version-snapshot"
        - "runtime.md#rt-obj-workflow-checkpoint"
        - "memory.md#mem-obj-workflow-evaluations"
        - "epistemic.md#epi-rte-workflow-evidence"
        - "memory.md#mem-obj-todo-tool"
        - "memory.md#mem-rte-todo-context"
        - "runtime.md#rt-rte-capability-admission"
        - "memory.md#mem-rte-memory-admission"
        - "memory.md#mem-obj-corpus"
        - "runtime.md#rt-rte-knowledge-admission"
        - "memory.md#mem-obj-run-records"
        - "memory.md#mem-obj-chat-records"
        - "memory.md#mem-obj-trajectories"
        - "runtime.md#rt-rte-runtime-configuration"
        - "runtime.md#rt-obj-extension-manifest"
      note: "Known authoring, import, trace extraction and fixed compilation are local paths. Unresolved initial content and diagnostic-payload provenance prevent a complete lineage inventory."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Recent/working context at foreground model"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-bap-memory-guidance"
                - "memory.md#mem-rte-tier-context"
              note: "Agent model receives selected results and summaries through memory_context."
          records:
            - "memory.md#mem-bap-memory-guidance"
            - "memory.md#mem-rte-tier-context"
          note: "History supplies evidence and context; delivery does not prove compliance."
        - scope: "Retained event lines and previous summary at compacting model"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-working-memory"
                - "memory.md#mem-rte-tier-context"
              note: "CompactHook consumes retained execution experience to write later-consumed working summaries."
          records:
            - "memory.md#mem-obj-working-memory"
            - "memory.md#mem-rte-tier-context"
          note: "The retained experience feeds an automatic durable context update, separately from downstream use."
        - scope: "Todo Markdown at Agent model"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-bap-todo-guidance"
                - "memory.md#mem-rte-todo-context"
              note: "Retained plans guide subsequent work."
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-bap-todo-guidance"
                - "memory.md#mem-rte-todo-context"
              note: "Status and result text supply task context alongside plan directions."
          records:
            - "memory.md#mem-bap-todo-guidance"
            - "memory.md#mem-rte-todo-context"
          note: "Task plan is interpreted guidance, not an enforced scheduler."
        - scope: "Corpus text at rankers and returned workflow data"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-corpus"
                - "epistemic.md#epi-rte-corpus-ranking"
                - "runtime.md#rt-rte-knowledge-admission"
              note: "BM25 and TF-IDF score retained texts to select/order hits."
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-corpus"
                - "epistemic.md#epi-rte-corpus-ranking"
                - "runtime.md#rt-rte-knowledge-admission"
              note: "Selected document payloads survive normalization into workflow data for downstream reference."
          records:
            - "memory.md#mem-obj-corpus"
            - "epistemic.md#epi-rte-corpus-ranking"
            - "runtime.md#rt-rte-knowledge-admission"
          note: "The consumed text influences fixed-code relative priority and supplies returned reference data; no automatic model injection follows."
        - scope: "Corpus backend manifest at retrieval dispatcher"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-corpus"
                - "runtime.md#rt-rte-knowledge-admission"
              note: "Retained backend type selects the retrieval implementation."
          records:
            - "memory.md#mem-obj-corpus"
            - "runtime.md#rt-rte-knowledge-admission"
          note: "Backend type is control metadata, not a fact endorsement."
        - scope: "Conversation and chat text at frontend replay"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-client-replay"
                - "memory.md#mem-obj-conversation-events"
                - "memory.md#mem-obj-chat-records"
              note: "Frontend loads retained messages/events as visible conversational context."
          records:
            - "memory.md#mem-rte-client-replay"
            - "memory.md#mem-obj-conversation-events"
            - "memory.md#mem-obj-chat-records"
          note: "Display supplies retained dialogue to the client, not Agent resumption."
        - scope: "Workflow evaluation records at summary/inspect consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-workflow-evaluations"
                - "epistemic.md#epi-rte-workflow-evidence"
              note: "inspect_workflow exposes aggregate evidence to the agent; fixed summary computation supplies a health signal."
          records:
            - "memory.md#mem-obj-workflow-evaluations"
            - "epistemic.md#epi-rte-workflow-evidence"
          note: "Metrics support advisory judgment; there is no mandatory quality-triggered adoption branch."
        - scope: "Workflow checkpoint state at resume"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-workflow-checkpoint"
                - "runtime.md#rt-rte-workflow-execution"
              note: "Completed records select reuse while incomplete invocations are requeued."
            - value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-workflow-checkpoint"
                - "runtime.md#rt-rte-workflow-execution"
              note: "Saved workflow identity/hash/version are checked against the executable."
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-workflow-checkpoint"
                - "runtime.md#rt-rte-workflow-execution"
              note: "A resume identity mismatch rejects resumption."
          records:
            - "runtime.md#rt-obj-workflow-checkpoint"
            - "runtime.md#rt-rte-workflow-execution"
          note: "Retained identity and completion fields have fixed resume consequences."
        - scope: "Active extension manifest and version snapshot at loaders/restorers"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-extension-manifest"
                - "memory.md#mem-rte-version-recovery"
              note: "Startup active entries and restore map versions select what is loaded or restored."
          records:
            - "runtime.md#rt-obj-extension-manifest"
            - "memory.md#mem-rte-version-recovery"
          note: "Retained identities select implementations, not semantic quality."
        - scope: "Retained skill results at later foreground model"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-skill-guidance"
                - "runtime.md#rt-rte-skill-instructions"
                - "memory.md#mem-rte-tier-context"
              note: "Retained action-result instruction bodies can guide later turns before or after compaction."
          records:
            - "runtime.md#rt-bap-skill-guidance"
            - "runtime.md#rt-rte-skill-instructions"
            - "memory.md#mem-rte-tier-context"
          note: "Only use-retained skill text is included; shipped static skill instructions alone are excluded."
        - scope: "Extension executable method bodies"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-extension-source"
            - "runtime.md#rt-bap-extension-execution"
          note: "Executable authority is established, but arbitrary method semantics do not determine a single controlled consumer effect such as validation or enforcement."
        - scope: "Feedback, trace helper outputs, prompt displays and trajectory exports"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-run-records"
            - "memory.md#mem-obj-trace-events"
            - "memory.md#mem-obj-message-snapshots"
            - "memory.md#mem-obj-trajectories"
          note: "Diagnostic/API capability is established; consequential downstream learning or model-input consumers were not traced. Unconsumed metadata receives no inferred authority."
        - scope: "Included custom memory/backend alternatives, canvas/library and kernel/notebook persistence"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-tier-context"
            - "memory.md#mem-obj-corpus"
            - "memory.md#mem-obj-run-records"
            - "memory.md#mem-rte-memory-admission"
          note: "Untraced implementations and notebook/canvas consumers can have additional authority paths."
      records:
        - "memory.md#mem-bap-memory-guidance"
        - "memory.md#mem-rte-tier-context"
        - "memory.md#mem-obj-working-memory"
        - "memory.md#mem-bap-todo-guidance"
        - "memory.md#mem-rte-todo-context"
        - "memory.md#mem-obj-corpus"
        - "epistemic.md#epi-rte-corpus-ranking"
        - "runtime.md#rt-rte-knowledge-admission"
        - "memory.md#mem-rte-client-replay"
        - "memory.md#mem-obj-conversation-events"
        - "memory.md#mem-obj-chat-records"
        - "memory.md#mem-obj-workflow-evaluations"
        - "epistemic.md#epi-rte-workflow-evidence"
        - "runtime.md#rt-obj-workflow-checkpoint"
        - "runtime.md#rt-rte-workflow-execution"
        - "runtime.md#rt-obj-extension-manifest"
        - "memory.md#mem-rte-version-recovery"
        - "runtime.md#rt-bap-skill-guidance"
        - "runtime.md#rt-rte-skill-instructions"
        - "runtime.md#rt-obj-extension-source"
        - "runtime.md#rt-bap-extension-execution"
        - "memory.md#mem-obj-run-records"
        - "memory.md#mem-obj-trace-events"
        - "memory.md#mem-obj-message-snapshots"
        - "memory.md#mem-obj-trajectories"
        - "memory.md#mem-rte-memory-admission"
      note: "Authority belongs to actual retained-part/consumer paths, not the runtime permission envelope. Summary-input learning is distinct from summary-output knowledge. Opaque source semantics and untraced diagnostic consumers remain unresolved."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Memory hook event admission, nonempty summary insertion and display writes"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tier-context"
                - "memory.md#mem-obj-memory-display"
              note: "Typed hook envelopes and nonempty compact output govern admission."
          records:
            - "memory.md#mem-rte-tier-context"
            - "memory.md#mem-obj-memory-display"
          note: "Software admits events and model prose without a per-content operator decision."
        - scope: "Model-issued TodoTool edits"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-todo-context"
              note: "The model/tool route does not consume per-item human approval."
          records:
            - "memory.md#mem-rte-todo-context"
          note: "A model can propose plan/status edits and software persists them."
        - scope: "Generated tool and memory component admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capability-admission"
                - "memory.md#mem-rte-memory-admission"
              note: "Registration hooks validate/promote/register without consuming a human answer."
          records:
            - "runtime.md#rt-rte-capability-admission"
            - "memory.md#mem-rte-memory-admission"
          note: "Generator finalization admits resolvable source through code, despite approval doctrine."
        - scope: "Observational conversation/trace/snapshot/trajectory lifecycle writes"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-events"
                - "memory.md#mem-obj-trace-events"
                - "memory.md#mem-obj-message-snapshots"
                - "memory.md#mem-obj-trajectories"
              note: "Lifecycle handlers serialize observations and available prompt/trajectory fields."
          records:
            - "memory.md#mem-obj-conversation-events"
            - "memory.md#mem-obj-trace-events"
            - "memory.md#mem-obj-message-snapshots"
            - "memory.md#mem-obj-trajectories"
          note: "Automatic observational writers are distinct from caller-submitted chat and reward edits."
        - scope: "Evaluation normalization/persistence and workflow checkpoint writing"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-workflow-evidence"
                - "runtime.md#rt-rte-workflow-execution"
              note: "Code decides admissibility against run identity/state and persists accepted records; workflow runtime checkpoints its execution."
          records:
            - "epistemic.md#epi-rte-workflow-evidence"
            - "runtime.md#rt-rte-workflow-execution"
          note: "Software records validated evaluation submissions and executable state; initial quality authorship remains a separate question."
        - scope: "Corpus ingest, chat/feedback append, administrative edits, initial content, checkpoint-label and external file replacements"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-knowledge-admission"
            - "memory.md#mem-rte-client-replay"
            - "runtime.md#rt-rte-runtime-configuration"
            - "memory.md#mem-rte-version-recovery"
            - "memory.md#mem-obj-todo-tool"
          note: "Generic caller identity does not decide human per-content control. No explicit human content decision is established, and automatic serialization alone does not settle these caller-selected admission alternatives."
        - scope: "Included custom memory/backend alternatives, canvas/library and kernel/notebook persistence"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-tier-context"
            - "memory.md#mem-obj-corpus"
            - "memory.md#mem-obj-run-records"
            - "memory.md#mem-rte-memory-admission"
          note: "Custom content admission and generated-memory state migration remain untraced."
      records:
        - "memory.md#mem-rte-tier-context"
        - "memory.md#mem-obj-memory-display"
        - "memory.md#mem-rte-todo-context"
        - "runtime.md#rt-rte-capability-admission"
        - "memory.md#mem-rte-memory-admission"
        - "memory.md#mem-obj-conversation-events"
        - "memory.md#mem-obj-trace-events"
        - "memory.md#mem-obj-message-snapshots"
        - "memory.md#mem-obj-trajectories"
        - "epistemic.md#epi-rte-workflow-evidence"
        - "runtime.md#rt-rte-workflow-execution"
        - "runtime.md#rt-rte-knowledge-admission"
        - "memory.md#mem-rte-client-replay"
        - "runtime.md#rt-rte-runtime-configuration"
        - "memory.md#mem-rte-version-recovery"
        - "memory.md#mem-obj-todo-tool"
        - "memory.md#mem-obj-corpus"
        - "memory.md#mem-obj-run-records"
      note: "Automatic mechanisms are established separately from authorship and physical I/O. No manual finding is warranted merely by a CLI, approval claim or generic caller; those alternatives remain unresolved."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Execution-history compaction"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-working-memory"
                - "memory.md#mem-rte-tier-context"
              note: "CompactHook reduces oldest-record lines into 2–4 sentence summaries. Fidelity is requested, not verified."
          records:
            - "memory.md#mem-obj-working-memory"
            - "memory.md#mem-rte-tier-context"
          note: "Old records are compressed into a shorter representation of their execution claims."
        - scope: "Bounded summary retention and recent/session eviction"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tier-context"
              note: "Working maxlen drops oldest summaries; compaction removes raw chunks and LRU eviction drops prompt-reachable session state."
          records:
            - "memory.md#mem-rte-tier-context"
          note: "These are operative forgetting routes, not a truth judgment."
        - scope: "TodoTool plan maintenance"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-todo-context"
              note: "Existing plan/status/result entries can be updated."
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-todo-context"
              note: "Clear removes completed plan items from the retained plan."
          records:
            - "memory.md#mem-rte-todo-context"
          note: "Update and completion revise retained plan entries; clear removes completed items."
        - scope: "Extension rollback/unload and version maintenance"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capability-admission"
                - "runtime.md#rt-obj-extension-manifest"
                - "memory.md#mem-rte-memory-admission"
              note: "A new implementation can replace an existing live capability."
            - value: "invalidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capability-admission"
                - "runtime.md#rt-obj-extension-manifest"
                - "memory.md#mem-rte-memory-admission"
              note: "Rollback/unload withdraws current reliance on an installed version while archives/history can remain."
          records:
            - "runtime.md#rt-rte-capability-admission"
            - "runtime.md#rt-obj-extension-manifest"
            - "memory.md#mem-rte-memory-admission"
          note: "Registration changes active versions while archives retain history. Staging-to-shared copying is admission, not automatically a promote operation."
        - scope: "Workflow evaluation current-version view"
          assessment: "known"
          findings:
            - value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-workflow-evaluations"
                - "epistemic.md#epi-rte-workflow-evidence"
              note: "Current-version filtering withdraws old-version evidence from the active summary without deleting its history."
          records:
            - "memory.md#mem-obj-workflow-evaluations"
            - "epistemic.md#epi-rte-workflow-evidence"
          note: "Old evidence remains retained but is excluded from current-version reliance until that version returns."
        - scope: "Trajectory reward backfill"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectories"
              note: "Reward mutation revises a retained trajectory product."
          records:
            - "memory.md#mem-obj-trajectories"
          note: "Backfill changes and re-persists the existing trajectory record, not model weights."
        - scope: "Conversation/chat deletion"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-client-replay"
              note: "Deleting retained dialogue forgets those files."
          records:
            - "memory.md#mem-rte-client-replay"
          note: "Deletion removes this transcript or chat directory, not every memory store."
        - scope: "Other implemented routes and opaque transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-corpus"
            - "memory.md#mem-obj-memory-display"
            - "runtime.md#rt-rte-runtime-configuration"
            - "memory.md#mem-obj-run-records"
          note: "Corpus acquisition/index reconstruction and duplicate-run rejection alone establish no additional operation. Records do not settle every display, administrative or diagnostic transformation; no synthesis, promotion or near-duplicate merging is inferred from route names."
        - scope: "Included custom memory/backend alternatives, canvas/library and kernel/notebook persistence"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-tier-context"
            - "memory.md#mem-obj-corpus"
            - "memory.md#mem-obj-run-records"
            - "memory.md#mem-rte-memory-admission"
          note: "Custom maintenance transformations are untraced."
      records:
        - "memory.md#mem-obj-working-memory"
        - "memory.md#mem-rte-tier-context"
        - "memory.md#mem-rte-todo-context"
        - "runtime.md#rt-rte-capability-admission"
        - "runtime.md#rt-obj-extension-manifest"
        - "memory.md#mem-rte-memory-admission"
        - "memory.md#mem-obj-workflow-evaluations"
        - "epistemic.md#epi-rte-workflow-evidence"
        - "memory.md#mem-obj-trajectories"
        - "memory.md#mem-rte-client-replay"
        - "memory.md#mem-obj-corpus"
        - "memory.md#mem-obj-memory-display"
        - "runtime.md#rt-rte-runtime-configuration"
        - "memory.md#mem-obj-run-records"
      note: "Consolidation, forgetting, revision and withdrawal have local implemented warrants. A summary faithfulness defect would not itself establish synthesis; primary-key/duplicate-run rejection is not dedup. Versioned install is not automatically salience promotion."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Agent memory request and automatic foreground context selection"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tier-context"
                - "memory.md#mem-bap-memory-guidance"
              note: "Agent context builder requests retained material from configured memory by context ID."
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tier-context"
                - "memory.md#mem-bap-memory-guidance"
              note: "Per-turn context assembly supplies selected history/summaries to the decision model without a model recall request."
          records:
            - "memory.md#mem-rte-tier-context"
            - "memory.md#mem-bap-memory-guidance"
          note: "Distinguish get(ctx.id) from automatic delivery of count-selected context to the model."
        - scope: "Overflow compactor input delivery"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tier-context"
                - "memory.md#mem-obj-working-memory"
              note: "Overflow selects oldest chunks plus the last working summary for CompactHook."
          records:
            - "memory.md#mem-rte-tier-context"
            - "memory.md#mem-obj-working-memory"
          note: "Automatic maintenance selects retained records and prior summary for a separate model."
        - scope: "Todo context disk request and foreground delivery"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-todo-context"
              note: "Context builder requests todo content by ctx.id."
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-todo-context"
              note: "Each turn delivers whole todo Markdown without another model show action."
          records:
            - "memory.md#mem-rte-todo-context"
          note: "The internal file request is separate from automatic model context supply."
        - scope: "Corpus retrieval and evaluation inspection"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-admission"
                - "epistemic.md#epi-rte-corpus-ranking"
                - "epistemic.md#epi-rte-workflow-evidence"
              note: "Query/base/top_k retrieval and explicit evidence inspection fulfill requests for retained material."
          records:
            - "runtime.md#rt-rte-knowledge-admission"
            - "epistemic.md#epi-rte-corpus-ranking"
            - "epistemic.md#epi-rte-workflow-evidence"
          note: "Caller requests query results or evidence; backend ranking and response transport are not a second unsolicited push."
        - scope: "Client replay metadata request and automatic latest-record selection"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-client-replay"
              note: "conversation.events and chat.session.load request retained content."
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-client-replay"
              note: "Frontend mount automatically chooses the latest matching conversation/chat for display."
          records:
            - "memory.md#mem-rte-client-replay"
          note: "Metadata/event load requests are pull; mount-time newest-record choice supplies context without an explicit choice of that record."
        - scope: "Workflow resume and capability restore requests"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-workflow-execution"
                - "memory.md#mem-rte-version-recovery"
              note: "Caller-selected checkpoint or restore label supplies recovery state."
          records:
            - "runtime.md#rt-rte-workflow-execution"
            - "memory.md#mem-rte-version-recovery"
          note: "Requested recovery selects retained checkpoint/map content; delivery fulfills the request."
        - scope: "Extension startup reloading"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-extension-manifest"
                - "runtime.md#rt-bap-extension-execution"
              note: "Active manifest entries supply registered executable implementations at startup."
          records:
            - "runtime.md#rt-obj-extension-manifest"
            - "runtime.md#rt-bap-extension-execution"
          note: "Startup automatically delivers active retained source to the dynamic loader."
        - scope: "Trace, prompt snapshot, trajectory, feedback and full frontend resend alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-run-records"
            - "memory.md#mem-rte-client-replay"
          note: "Read/export helpers are capabilities; concrete downstream invocation routes or resend-to-model behavior are not established for all these parts."
        - scope: "Included custom memory/backend alternatives, canvas/library and kernel/notebook persistence"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-tier-context"
            - "memory.md#mem-obj-corpus"
            - "memory.md#mem-obj-run-records"
            - "memory.md#mem-rte-memory-admission"
          note: "Custom read-back and notebook/canvas consumers remain untraced."
      records:
        - "memory.md#mem-rte-tier-context"
        - "memory.md#mem-bap-memory-guidance"
        - "memory.md#mem-obj-working-memory"
        - "memory.md#mem-rte-todo-context"
        - "runtime.md#rt-rte-knowledge-admission"
        - "epistemic.md#epi-rte-corpus-ranking"
        - "epistemic.md#epi-rte-workflow-evidence"
        - "memory.md#mem-rte-client-replay"
        - "runtime.md#rt-rte-workflow-execution"
        - "memory.md#mem-rte-version-recovery"
        - "runtime.md#rt-obj-extension-manifest"
        - "runtime.md#rt-bap-extension-execution"
        - "memory.md#mem-obj-run-records"
        - "memory.md#mem-obj-corpus"
        - "memory.md#mem-rte-memory-admission"
      note: "Both requested access and automatic supply occur within distinct chains. A ranked response to an explicit query is pull; returning it does not add push. Known recovery or display routes do not resolve other retained products."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Automatic tier-context delivery to foreground model"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tier-context"
              note: "Context-ID registry match selects the history actually delivered to this model turn."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tier-context"
              note: "Count-tail availability and working/recent budgets select material without query relevance scoring."
          records:
            - "memory.md#mem-rte-tier-context"
          note: "Trigger is context assembly; selector uses configured memory, ctx.id and count windows; selected parts are that context's working/recent tails and optional final result."
        - scope: "Compactor input selection"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tier-context"
                - "memory.md#mem-obj-working-memory"
              note: "Age/count selection supplies the oldest chunk and available prior summary, not a semantic match."
          records:
            - "memory.md#mem-rte-tier-context"
            - "memory.md#mem-obj-working-memory"
          note: "Trigger is recent overflow; oldest-record count and last summary select the compacting model's input."
        - scope: "Automatic todo delivery"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-todo-context"
                - "memory.md#mem-obj-todo-tool"
              note: "Actual context/file identity match selects this plan rather than another context's plan."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-todo-context"
                - "memory.md#mem-obj-todo-tool"
              note: "Whole available Markdown is supplied, with no relevance filtering or token excerpt."
          records:
            - "memory.md#mem-rte-todo-context"
            - "memory.md#mem-obj-todo-tool"
          note: "Trigger is per-turn assembly; ctx.id selects the corresponding todo.md, then whole-file content is delivered."
        - scope: "Frontend automatic latest-record replay"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-client-replay"
              note: "Session and view identity constrain which conversation or chat can be automatically selected."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-client-replay"
              note: "Newest-record choice is recency selection, not semantic relevance."
          records:
            - "memory.md#mem-rte-client-replay"
          note: "Trigger is pane mount/session selection; owner/session/view filter and newest metadata choose the transcript/chat delivered to display."
        - scope: "Extension startup selection"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-extension-manifest"
            - "runtime.md#rt-bap-extension-execution"
          note: "Startup iterates active manifest entries and loads their paths. Catalog path/name/version alone does not establish an identity-matching selector against a selection input. These records establish automatic supply but do not resolve a controlled push-signal value."
        - scope: "Requested corpus/evaluation/recovery access"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-knowledge-admission"
            - "epistemic.md#epi-rte-workflow-evidence"
            - "runtime.md#rt-rte-workflow-execution"
            - "memory.md#mem-rte-version-recovery"
          note: "These named operations fulfill explicit retained-material requests; their selectors do not classify push signals. In particular lexical corpus ranking is not an unsolicited push."
        - scope: "Unresolved diagnostic and frontend-to-model alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-run-records"
            - "memory.md#mem-rte-client-replay"
          note: "No complete delivery/selector chain is recorded for all retained diagnostic products or possible frontend resend; displayed text does not establish the opaque consumer payload."
        - scope: "Included custom memory/backend alternatives, canvas/library and kernel/notebook persistence"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-tier-context"
            - "memory.md#mem-obj-corpus"
            - "memory.md#mem-obj-run-records"
            - "memory.md#mem-rte-memory-admission"
          note: "No selector classification can be assigned to untraced custom read-back."
      records:
        - "memory.md#mem-rte-tier-context"
        - "memory.md#mem-obj-working-memory"
        - "memory.md#mem-rte-todo-context"
        - "memory.md#mem-obj-todo-tool"
        - "memory.md#mem-rte-client-replay"
        - "runtime.md#rt-obj-extension-manifest"
        - "runtime.md#rt-bap-extension-execution"
        - "runtime.md#rt-rte-knowledge-admission"
        - "epistemic.md#epi-rte-workflow-evidence"
        - "runtime.md#rt-rte-workflow-execution"
        - "memory.md#mem-rte-version-recovery"
        - "memory.md#mem-obj-run-records"
        - "memory.md#mem-obj-corpus"
        - "memory.md#mem-rte-memory-admission"
      note: "Identifier matches and coarse availability/age/count selection coexist at different selector stages. No inferred-lexical push is implied by pull corpus ranking, and no inferred-embedding selector follows from TF-IDF."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Automatic recent-history to retained working summary to later model"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-recent-history"
                - "memory.md#mem-obj-working-memory"
                - "memory.md#mem-rte-tier-context"
                - "memory.md#mem-bap-memory-guidance"
              note: "Execution traces feed automatic summary writes retained for later context/guidance; weight training and new knowledge are not required."
          records:
            - "memory.md#mem-obj-recent-history"
            - "memory.md#mem-obj-working-memory"
            - "memory.md#mem-rte-tier-context"
            - "memory.md#mem-bap-memory-guidance"
          note: "This is durable across model invocations within the live registry, not proven cross-process recall or improved capacity."
        - scope: "Retained skill/action text included in compaction"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-skill-instructions"
                - "memory.md#mem-rte-tier-context"
                - "memory.md#mem-obj-working-memory"
              note: "Action-result records, including returned instructions, feed retained continuation summaries for later turns."
          records:
            - "runtime.md#rt-rte-skill-instructions"
            - "memory.md#mem-rte-tier-context"
            - "memory.md#mem-obj-working-memory"
          note: "The same summary mechanism can consume recorded skill/tool/child outputs; this is not a second independent training implementation."
        - scope: "Todo edits, generated capabilities, evaluation tracking, corpus and diagnostic export alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-todo-context"
            - "runtime.md#rt-rte-capability-admission"
            - "memory.md#mem-rte-memory-admission"
            - "epistemic.md#epi-rte-workflow-evidence"
            - "memory.md#mem-obj-corpus"
            - "memory.md#mem-obj-run-records"
          note: "Automatic writes or behavior-shaping outputs alone do not close every trace-input/update/later-consumer chain. Diagnostic export is not an inspected trainer; generated source has no recorded concrete trace-fed update. No bounded system-wide or local no is inferred."
        - scope: "Included custom memory/backend alternatives, canvas/library and kernel/notebook persistence"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-tier-context"
            - "memory.md#mem-obj-corpus"
            - "memory.md#mem-obj-run-records"
            - "memory.md#mem-rte-memory-admission"
          note: "Custom updates, feedback consumers and canvas/notebook routes remain untraced."
      records:
        - "memory.md#mem-obj-recent-history"
        - "memory.md#mem-obj-working-memory"
        - "memory.md#mem-rte-tier-context"
        - "memory.md#mem-bap-memory-guidance"
        - "runtime.md#rt-rte-skill-instructions"
        - "memory.md#mem-rte-todo-context"
        - "runtime.md#rt-rte-capability-admission"
        - "memory.md#mem-rte-memory-admission"
        - "epistemic.md#epi-rte-workflow-evidence"
        - "memory.md#mem-obj-corpus"
        - "memory.md#mem-obj-run-records"
      note: "A wired yes is supported by the continuation-summary route. Other included routes are unresolved, not negative; learning-as-improved-capacity and beneficial self-improvement remain unestablished."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Execution-action results/errors feeding working summaries"
          assessment: "known"
          findings:
            - value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-recent-history"
                - "memory.md#mem-obj-working-memory"
                - "memory.md#mem-rte-tier-context"
              note: "Recorded tool/skill/child action outcomes and errors supply execution feedback to summary production."
            - value: "event-streams"
              basis: "wired"
              records:
                - "memory.md#mem-obj-recent-history"
                - "memory.md#mem-obj-working-memory"
                - "memory.md#mem-rte-tier-context"
              note: "Agent start/stop lifecycle records and event status/time supply discrete runtime-event content to the summary input."
          records:
            - "memory.md#mem-obj-recent-history"
            - "memory.md#mem-obj-working-memory"
            - "memory.md#mem-rte-tier-context"
          note: "The compactor consumes selected execution record lines; event envelopes do not replace original content classification."
        - scope: "Recorded task message feeding working summary"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-recent-history"
                - "memory.md#mem-obj-working-memory"
              note: "Recorded user task text is included in the recent projection consumed by compaction."
          records:
            - "memory.md#mem-obj-recent-history"
            - "memory.md#mem-obj-working-memory"
          note: "Start-task content is a recorded user message; it is not an event-stream source merely because the hook wraps it in an event."
        - scope: "Mixed upstream payloads and previous-summary provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-working-memory"
            - "memory.md#mem-obj-recent-history"
          note: "Known action and task origins do not enumerate the original source content of every service/child output or prior summary; richer linked trajectories are not shown as this compactor's input."
        - scope: "Other potentially qualifying trace-fed writes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-run-records"
            - "memory.md#mem-rte-todo-context"
            - "runtime.md#rt-rte-capability-admission"
            - "memory.md#mem-rte-memory-admission"
            - "epistemic.md#epi-rte-workflow-evidence"
          note: "Qualification itself is unresolved for these routes, so their trace source is not made inapplicable by known summary inputs. Stored trajectory data does not establish trajectories as a learning source without an update consumer."
        - scope: "Included custom memory/backend alternatives, canvas/library and kernel/notebook persistence"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-tier-context"
            - "memory.md#mem-obj-corpus"
            - "memory.md#mem-obj-run-records"
            - "memory.md#mem-rte-memory-admission"
          note: "Original inputs of untraced updates remain uninspected."
      records:
        - "memory.md#mem-obj-recent-history"
        - "memory.md#mem-obj-working-memory"
        - "memory.md#mem-rte-tier-context"
        - "memory.md#mem-obj-run-records"
        - "memory.md#mem-rte-todo-context"
        - "runtime.md#rt-rte-capability-admission"
        - "memory.md#mem-rte-memory-admission"
        - "epistemic.md#epi-rte-workflow-evidence"
        - "memory.md#mem-obj-corpus"
      note: "Tool execution feedback, discrete lifecycle events and recorded user messages support local sources for the wired summary update. Mixed/opaque upstream content and other unresolved writes prevent a complete source inventory; serialization names do not add sources."
---

# Autogenesis memory profile

## Comparison rationale

This profile classifies the accepted records, not new source evidence. Every positive finding is wired implementation evidence, not observed operation or causal benefit. All ten axes remain partial: the reports explicitly retain untraced alternatives, initial-content questions and missing consumer paths. A complete classification of a named local part is not a complete inventory of the system.

### Retained parts and consumer boundaries

The RAM tiers, their JSON/HTML display, the separate todo files and executable checkpoints are different objects. Tier persistence does not establish disk-to-model reload, while the todo reader does reread disk. The summary route does qualify as trace learning because the automatic trace-derived result survives into a later model invocation; this does not assert improved capacity. The compacting model receives experience with learning authority, and the foreground model receives its result as knowledge. See [MEM-RTE-tier-context](memory.md#mem-rte-tier-context), [MEM-OBJ-working-memory](memory.md#mem-obj-working-memory), [MEM-BAP-memory-guidance](memory.md#mem-bap-memory-guidance) and [MEM-RTE-todo-context](memory.md#mem-rte-todo-context).

Corpus texts are retained ranking inputs even though scoring code is fixed. BM25 and TF-IDF do not establish a persistent embedding store or a parametric memory update. Query fulfillment is pull; it does not contribute an inferred-lexical push finding. Workflow normalization preserves the returned data, but automatic Agent model injection is not established. See [MEM-OBJ-corpus](memory.md#mem-obj-corpus), [EPI-RTE-corpus-ranking](epistemic.md#epi-rte-corpus-ranking) and [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission).

Automatic per-turn model-context supply is distinguished from the context builder's internal get/content requests. The actual context-ID match selects retained parts delivered to a foreground model; count tails and whole-file availability are separate coarse selectors. Mount-time replay similarly distinguishes explicit server requests from automatic latest-record choice. Startup extension loading is automatic supply of retained source, not an explicit later tool invocation. Its signal remains not-determinable: iterating active catalog entries and loading their paths does not establish an identity match against a selection input. No controlled signal is inferred from the catalog identifiers alone. See [MEM-RTE-tier-context](memory.md#mem-rte-tier-context), [MEM-RTE-todo-context](memory.md#mem-rte-todo-context), [MEM-RTE-client-replay](memory.md#mem-rte-client-replay) and [RT-OBJ-extension-manifest](runtime.md#rt-obj-extension-manifest).

Executable extension bodies have symbolic form and a live execution path, but arbitrary executable behavior is not itself one of the controlled authority values. Their active identity metadata has a supported routing effect. Workflow recovery fields additionally validate and veto mismatched resume requests. These distinct forces do not establish an approval or quality guarantee for all runtime effects. See [RT-OBJ-extension-source](runtime.md#rt-obj-extension-source), [RT-BAP-extension-execution](runtime.md#rt-bap-extension-execution), [RT-OBJ-workflow-checkpoint](runtime.md#rt-obj-workflow-checkpoint) and [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution).

### Transformations and unresolved alternatives

Compaction implements consolidation even though semantic fidelity is unverified. No concrete new claim is needed for consolidation, and a possible fidelity defect does not establish synthesis. Bounded queues/deletion implement forgetting; versioned replacement and withdrawal support evolve/invalidate. Staging promotion does not by its name establish raised memory tier or salience. Duplicate-run rejection and index reconstruction do not establish dedup. See [MEM-RTE-tier-context](memory.md#mem-rte-tier-context), [MEM-RTE-todo-context](memory.md#mem-rte-todo-context), [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) and [EPI-RTE-workflow-evidence](epistemic.md#epi-rte-workflow-evidence).

Generic caller identity does not establish manual control. Model-generated admissions and automatic lifecycle writes are positively classified; initial/admin edits, corpus callers and external file replacements retain their unresolved control facts. Feedback retention and trajectory export do not demonstrate a training consumer. Neither uninspected custom backends nor detailed canvas/notebook persistence can be classified through the inspected display or registry. See [RT-RTE-runtime-configuration](runtime.md#rt-rte-runtime-configuration), [MEM-RTE-memory-admission](memory.md#mem-rte-memory-admission), [MEM-OBJ-run-records](memory.md#mem-obj-run-records) and [MEM-OBJ-corpus](memory.md#mem-obj-corpus).

Trace-source findings classify original content: recorded user task text is conversational input; tool/action feedback is execution trace content; lifecycle start/stop observations are discrete runtime events. Their common hook envelope does not merge these origins. Prior-summary and service/child output provenance remains mixed; persisted trajectories do not imply that the compactor consumes linked state/action/outcome trajectories. See [MEM-OBJ-recent-history](memory.md#mem-obj-recent-history) and [MEM-OBJ-working-memory](memory.md#mem-obj-working-memory).

### Canonical resolution and source-read log

Reconciliation resolves the duplicate corpus object to [MEM-OBJ-corpus](memory.md#mem-obj-corpus), the duplicate history-summary route to [MEM-RTE-tier-context](memory.md#mem-rte-tier-context), the duplicate evaluation object to [MEM-OBJ-workflow-evaluations](memory.md#mem-obj-workflow-evaluations), and the evaluation-maintenance route to [EPI-RTE-workflow-evidence](epistemic.md#epi-rte-workflow-evidence). The profile cites those canonical records. These identity supersessions do not strengthen a basis or resolve summary fidelity, source warrant or caller quality. The epistemic combined history container remains valid; recent/working parts retain their different producers. Runtime task, corpus and workflow containers remain distinct from their material parts.

No frozen-source reads were performed for this classification. All warrants are supplied accepted records and their annotations; no new record, quotation or evidence is introduced.
