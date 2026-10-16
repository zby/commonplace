---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "AgentFly memory comparison of local case banks, outcome records, training artifacts and tool-retained files at the frozen commit."
run-id: "AAS-2026-10-12-agentfly-bbfc9fb2d5c7-01"
source-identity: "https://github.com/Agent-on-the-Fly/AgentFly"
reviewed-boundary: "42fbbcac63dd58ed6856c0761357345a58e4f032"
memory-comparison:
  version: 2
  scope: "Local memory accumulated or changed through shipped use: both driver case banks and their access views; result traces and restart keys; retrieved-case training pairs; trained retriever checkpoints and later numerical ranking; workspace payloads/logs and document/media retained side files with their write and reuse surfaces. Include opaque local payloads and unresolved initial/admission/consumer alternatives. Exclude static prompts, ordinary current-query history (including accidental exception carryover without a durable artifact), temporary return-only extraction, external provider retention/training and dependency caches, pretrained assets as use-accumulated memory, and bare helpers as established consumer routes."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        - scope: "Two case banks, result JSONL and training-pair JSONL on disk"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-query-record", "memory.md#mem-obj-training-data"]
              note: "Driver appends persist across queries and process starts."
          records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-query-record", "memory.md#mem-obj-training-data"]
          note: "The distinct local JSONL artifacts cover both driver alternatives and their recovery/training outputs."
        - scope: "Loaded case pools/metadata and converted training samples"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-training-data"]
              note: "Readers construct process-memory pools and dataset samples."
          records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-training-data"]
          note: "These are operative derived views, not an additional durable bank."
        - scope: "Persisted retriever checkpoint and later loaded weights"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records: ["memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-retriever-training"]
              note: "best.pt/last.pt persist numerical state in local files."
            - value: "model-weights"
              basis: "wired"
              records: ["memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-retriever-training"]
              note: "The accumulated state is backbone/head parameters consumed by later inference."
            - value: "in-memory"
              basis: "wired"
              records: ["memory.md#mem-obj-checkpoint"]
              note: "Initialization loads parameters into the classifier in process memory."
          records: ["memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-retriever-training"]
          note: "The numerical artifact is separate from the retriever component; missing checkpoint contents do not prevent substrate classification."
        - scope: "Workspace payloads, execution/process logs and document/video side files"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records: ["memory.md#mem-obj-workspace-files", "memory.md#mem-obj-tool-files"]
              note: "Workspace writes, logs, converted documents, downloaded media and extracted audio use local files."
          records: ["memory.md#mem-obj-workspace-files", "memory.md#mem-obj-tool-files"]
          note: "Opaque binary payloads remain included as files; readable summaries do not replace them."
      records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-query-record", "memory.md#mem-obj-training-data", "memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-retriever-training", "memory.md#mem-obj-workspace-files", "memory.md#mem-obj-tool-files"]
      note: "The local retained-object inventory is the two case banks, rich results, training pairs, checkpoints, workspace files/logs and document/media side files. All have file storage; loaded case and training views and initialized weights additionally reside in process memory. Binary encoding and unavailable exact weights do not obscure these substrates. External provider retention and dependency caches are excluded, not classified as local memory."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Case and pair question/plan descriptions; result conversation, answer and rationale text"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-training-data", "memory.md#mem-obj-query-record"]
              note: "Questions, plan descriptions, task summaries and rationale are textual content."
          records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-training-data", "memory.md#mem-obj-query-record"]
          note: "Natural-language descriptions receive consequences through interpretation or tokenization; JSON framing is a separate part."
        - scope: "Case rewards/labels and envelopes, pair truth labels, result IDs/tool arguments and restart keys"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-training-data", "memory.md#mem-obj-query-record"]
              note: "JSON structure, labels, Boolean targets, query keys and tool arguments drive parsing, grouping, training and scheduling."
          records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-training-data", "memory.md#mem-obj-query-record"]
          note: "Fixed code interprets these localized fields independently of descriptive text."
        - scope: "Retriever checkpoint parameters at classifier consumption"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records: ["memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-retriever-training"]
              note: "Gradient-updated backbone/head state is distributed numerical parameter material."
          records: ["memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-retriever-training"]
          note: "The form of the numerical output is known even though its exact trained contents are unavailable."
        - scope: "Workspace text/scripts and log fields at read/execution consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records: ["memory.md#mem-obj-workspace-files", "memory.md#mem-rte-workspace-read"]
              note: "Stored notes can be returned as executor context."
            - value: "symbolic"
              basis: "wired"
              records: ["memory.md#mem-obj-workspace-files", "runtime.md#rt-rte-terminal-execution"]
              note: "Scripts/configuration are consumed by execution; operation/timestamp metadata use fixed fields."
          records: ["memory.md#mem-obj-workspace-files", "memory.md#mem-rte-workspace-read", "runtime.md#rt-rte-terminal-execution"]
          note: "Split interpreted text from executable code and fixed metadata."
        - scope: "Converted document text and JSON framing"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records: ["memory.md#mem-obj-tool-files"]
              note: "Converted Markdown/text contains descriptive material."
            - value: "symbolic"
              basis: "wired"
              records: ["memory.md#mem-obj-tool-files"]
              note: "JSON conversion framing is localized structured data."
          records: ["memory.md#mem-obj-tool-files"]
          note: "Only the inspected output parts are resolved; their source binaries are separate."
        - scope: "Workspace binary outputs, source documents, PPTX image side files, downloaded video and audio payloads"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-workspace-files", "memory.md#mem-obj-tool-files"]
          note: "The records explicitly leave binary payloads opaque. No controlled form is established by a filename or metadata display."
      records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-training-data", "memory.md#mem-obj-query-record", "memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-retriever-training", "memory.md#mem-obj-workspace-files", "memory.md#mem-rte-workspace-read", "runtime.md#rt-rte-terminal-execution", "memory.md#mem-obj-tool-files"]
      note: "Text, symbolic control data and retriever parameters are resolved separately. Workspace and document/media binary payloads remain opaque; their displays cannot establish payload form."
    lineage:
      assessment: "partial"
      units:
        - scope: "Driver-created latest-plan cases, result traces and outcome-labelled retrieved-case pairs"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-query-record", "memory.md#mem-obj-training-data", "runtime.md#rt-rte-case-admission"]
              note: "Completed benchmark activity is serialized or reduced to retained cases and pairs."
          records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-query-record", "memory.md#mem-obj-training-data", "runtime.md#rt-rte-case-admission"]
          note: "The current query/plan/outcome derivation is inspected; initial corpus genealogy is a separate unit."
        - scope: "Checkpoint produced by the standalone trainer"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records: ["memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-retriever-training", "memory.md#mem-obj-training-data"]
              note: "Tokenized pair text and targets compile into numerical parameters through optimization."
          records: ["memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-retriever-training", "memory.md#mem-obj-training-data"]
          note: "This classifies the gradient-produced output, not the initial pretrained backbone or an unspecified deployed checkpoint."
        - scope: "External document/media acquisition parts"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records: ["memory.md#mem-obj-tool-files"]
              note: "Document/media content is acquired rather than originating as benchmark experience."
          records: ["memory.md#mem-obj-tool-files"]
          note: "The source content enters from documents/media and external services; transformations remain distinct."
        - scope: "Caller-supplied workspace text and command-derived files"
          assessment: "partial"
          findings:
            - value: "authored"
              basis: "wired"
              records: ["memory.md#mem-obj-workspace-files", "runtime.md#rt-rte-terminal-execution"]
              note: "The write tool stores caller-proposed content directly."
          records: ["memory.md#mem-obj-workspace-files", "runtime.md#rt-rte-terminal-execution"]
          note: "Text supplied for a file is authored content, without an inference of human authorship. Commands can create other files whose derivation is unspecified."
        - scope: "Initial case/result/pair content, pretrained assets and exact loaded checkpoint provenance"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-query-record", "memory.md#mem-obj-training-data", "memory.md#mem-obj-checkpoint", "runtime.md#rt-cmp-case-retriever"]
          note: "Committed samples have no authenticated generation route; pretrained asset versions and deployed checkpoint contents are unresolved. Subsequent extraction/compilation does not resolve them."
        - scope: "Converted document outputs and opaque workspace/media payload derivations"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records: ["memory.md#mem-obj-tool-files"]
              note: "Converted outputs carry content from external documents/media; no full provenance or fidelity guarantee is established."
          records: ["memory.md#mem-obj-tool-files", "memory.md#mem-obj-workspace-files"]
          note: "External source contribution is known for document/media outputs, but exact service transformations and binary genealogy remain unresolved."
      records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-query-record", "memory.md#mem-obj-training-data", "runtime.md#rt-rte-case-admission", "memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-retriever-training", "memory.md#mem-obj-tool-files", "memory.md#mem-obj-workspace-files", "runtime.md#rt-rte-terminal-execution", "runtime.md#rt-cmp-case-retriever"]
      note: "Known subsequent driver extraction and gradient compilation coexist with unauthenticated initial corpora, unresolved asset provenance and mixed tool-file derivations. No known subsequent path authenticates initial content."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Case descriptions and labels at later planner/executor example consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-rte-embedding-examples", "memory.md#mem-rte-classifier-examples"]
              note: "Cases provide contextual examples/advice, not a system instruction or enforced correctness guarantee."
          records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-rte-embedding-examples", "memory.md#mem-rte-classifier-examples", "runtime.md#rt-bap-case-guidance"]
          note: "User-role examples request imitation/avoidance; standing interpretation rules are static prompts outside this memory boundary."
        - scope: "Retained question/case-plan text at embedding/classifier scorers and checkpoint parameters at classifier"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-rte-embedding-examples", "memory.md#mem-rte-classifier-examples", "memory.md#mem-obj-checkpoint"]
              note: "Retained question embeddings, case/plan text and learned parameters affect relative case priority."
          records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-rte-embedding-examples", "memory.md#mem-rte-classifier-examples", "memory.md#mem-obj-checkpoint", "runtime.md#rt-bap-case-guidance"]
          note: "Ranking includes both fixed scoring of retained text and numerical policy state; observed usefulness is not asserted."
        - scope: "Training pair text and truth labels at gradient-update consumer"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records: ["memory.md#mem-obj-training-data", "runtime.md#rt-rte-retriever-training"]
              note: "Retained pairs feed the parameter update; this does not establish improved future capacity."
          records: ["memory.md#mem-obj-training-data", "runtime.md#rt-rte-retriever-training"]
          note: "Update authority is separate from downstream example guidance and numerical ranking."
        - scope: "Persisted result question/query keys at restart suppression"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records: ["memory.md#mem-obj-query-record", "runtime.md#rt-rte-case-admission"]
              note: "Previously recorded questions select which benchmark work is skipped."
            - value: "enforcement"
              basis: "wired"
              records: ["memory.md#mem-obj-query-record", "runtime.md#rt-rte-case-admission"]
              note: "A matching recorded question excludes that query from restarted processing even if later memory writes failed."
          records: ["memory.md#mem-obj-query-record", "runtime.md#rt-rte-case-admission"]
          note: "Only keys are read for restart; retained rationale receives no demonstrated reassessment force."
        - scope: "Stored workspace text delivered to executor by requested read"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records: ["memory.md#mem-obj-workspace-files", "memory.md#mem-rte-workspace-read"]
              note: "Prior file text becomes tool-result context for later executor invocations."
          records: ["memory.md#mem-obj-workspace-files", "memory.md#mem-rte-workspace-read"]
          note: "Returned text supplies context, with truncation; a script execution is a different consumer."
        - scope: "Executable workspace scripts/configuration and opaque tool-file consumers"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-workspace-files", "runtime.md#rt-rte-terminal-execution", "memory.md#mem-obj-tool-files"]
          note: "Execution is wired but a generic executable payload does not establish one of the seven controlled memory forces without its content/effect. Binary displays and potential later media reuse cannot classify unseen payload authority."
        - scope: "Rich result rationale/tool traces and execution/process log content beyond restart keys"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-query-record", "memory.md#mem-obj-workspace-files"]
          note: "No implemented later rationale/log consumer is established. Their mere retention supplies no controlled force."
      records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-rte-embedding-examples", "memory.md#mem-rte-classifier-examples", "runtime.md#rt-bap-case-guidance", "memory.md#mem-obj-checkpoint", "memory.md#mem-obj-training-data", "runtime.md#rt-rte-retriever-training", "memory.md#mem-obj-query-record", "runtime.md#rt-rte-case-admission", "memory.md#mem-obj-workspace-files", "memory.md#mem-rte-workspace-read", "runtime.md#rt-rte-terminal-execution", "memory.md#mem-obj-tool-files"]
      note: "Authority is consumer-relative: examples advise models, retained text/weights rank cases, pairs train parameters and result keys govern restart. Unread rationale/logs and opaque tool payload paths do not inherit these forces."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Completed-query result/case/pair admission and checkpoint optimization/save"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-query-record", "memory.md#mem-obj-training-data", "memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-case-admission", "runtime.md#rt-rte-retriever-training"]
              note: "No per-content human approval is present on these admission paths."
          records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-query-record", "memory.md#mem-obj-training-data", "memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-case-admission", "runtime.md#rt-rte-retriever-training"]
          note: "Models propose plans/judgments, software appends labels and saves updates, and humans configure runs rather than approve items."
        - scope: "Executor-selected workspace writes/commands and document/video tool writes"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records: ["memory.md#mem-obj-workspace-files", "memory.md#mem-obj-tool-files", "runtime.md#rt-rte-terminal-execution", "runtime.md#rt-rte-query-execution"]
              note: "Software/model tool operations persist content without default per-content human approval."
          records: ["memory.md#mem-obj-workspace-files", "memory.md#mem-obj-tool-files", "runtime.md#rt-rte-terminal-execution", "runtime.md#rt-rte-query-execution"]
          note: "This unit is the inspected model-dispatch path, not every possible external caller of the APIs."
        - scope: "Initial corpora/checkpoint supply, external file edits and generic caller-controlled workspace content"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-training-data", "memory.md#mem-obj-checkpoint", "memory.md#mem-obj-workspace-files"]
          note: "Possible file editing and operator path choice do not identify a content-supplying/approving human decision. Generic callers do not resolve admission control."
      records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-query-record", "memory.md#mem-obj-training-data", "memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-case-admission", "runtime.md#rt-rte-retriever-training", "memory.md#mem-obj-workspace-files", "memory.md#mem-obj-tool-files", "runtime.md#rt-rte-terminal-execution", "runtime.md#rt-rte-query-execution"]
      note: "Driver admissions and numerical saves are automatic despite operator-started workflows. Caller identity and unauthenticated initial content prevent complete enumeration of control; no explicit per-content human decision warrants manual."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Completed-query material reduced to latest-plan labelled cases and retrieved-case/outcome pairs"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-query-record", "memory.md#mem-obj-training-data", "runtime.md#rt-rte-case-admission"]
              note: "Existing run content is selected into reduced retained representations without an established novel claim."
          records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-query-record", "memory.md#mem-obj-training-data", "runtime.md#rt-rte-case-admission"]
          note: "Reduction keeps question/latest plan/outcome and omits fuller trace/reasons; raw results can remain available."
        - scope: "Successive retriever checkpoint state and explicit workspace-file replacement"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records: ["memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-retriever-training", "memory.md#mem-obj-workspace-files", "runtime.md#rt-rte-terminal-execution"]
              note: "Optimization revises checkpoint parameters and the workspace write surface overwrites existing file content."
          records: ["memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-retriever-training", "memory.md#mem-obj-workspace-files", "runtime.md#rt-rte-terminal-execution"]
          note: "Numerical revision and file overwrite replace existing retained content; this is not history-preserving invalidation."
        - scope: "Other workspace-command outputs, document/media conversions and external bank edits"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-workspace-files", "memory.md#mem-obj-tool-files", "memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory"]
          note: "Their general write/conversion capability does not establish a particular controlled transformation over retained claims. No bounded absence record supplies a complete negative."
      records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-query-record", "memory.md#mem-obj-training-data", "runtime.md#rt-rte-case-admission", "memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-retriever-training", "memory.md#mem-obj-workspace-files", "runtime.md#rt-rte-terminal-execution", "memory.md#mem-obj-tool-files"]
      note: "Driver reduction and inspected replacement paths establish transformations, but arbitrary tool commands, opaque converters and initial edits remain unresolved. Plain append, reload, index/scoring recomputation and parser filtering are not extra semantic curation values."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Query-triggered example retrieval and fulfilled delivery to planner/executor"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records: ["memory.md#mem-rte-embedding-examples", "memory.md#mem-rte-classifier-examples"]
              note: "Current-query retrieval requests retained examples; fulfilling that request is pull."
          records: ["memory.md#mem-rte-embedding-examples", "memory.md#mem-rte-classifier-examples"]
          note: "The records explicitly describe driver retrieval requests followed by delivery, not an additional independent unsolicited example push."
        - scope: "Requested workspace reads, later file-path tool reuse, standalone retrieval CLI and separately started trainer"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records: ["memory.md#mem-rte-workspace-read", "memory.md#mem-obj-tool-files", "memory.md#mem-rte-retrieval-display", "runtime.md#rt-rte-retriever-training", "memory.md#mem-obj-training-data"]
              note: "Explicit consumer calls or operator-supplied input requests obtain persisted content."
          records: ["memory.md#mem-rte-workspace-read", "memory.md#mem-obj-tool-files", "memory.md#mem-rte-retrieval-display", "runtime.md#rt-rte-retriever-training", "memory.md#mem-obj-training-data"]
          note: "These callers request retained files/pairs/cases; immediate converted-document return is excluded from later read-back."
        - scope: "Automatic case-bank initialization/reload, configured checkpoint initialization and result-key restart scan"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-checkpoint", "memory.md#mem-obj-query-record", "runtime.md#rt-rte-case-admission", "memory.md#mem-rte-classifier-examples"]
              note: "Startup/reload supplies available retained pools/parameters/restart keys to later runtime consumers without requesting individual stored items."
          records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-checkpoint", "memory.md#mem-obj-query-record", "runtime.md#rt-rte-case-admission", "memory.md#mem-rte-classifier-examples"]
          note: "These loading/supply operations are separate from subsequent requested query selection and from choosing a checkpoint replacement."
        - scope: "Execution/process logs, opaque payload alternatives and unspecified library consumers"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-workspace-files", "memory.md#mem-obj-tool-files", "memory.md#mem-rte-retrieval-display"]
          note: "No additional later-consumer route is established for logs or the bare helper. Actual opaque payload reuse and alternative delivery are unresolved rather than absent."
      records: ["memory.md#mem-rte-embedding-examples", "memory.md#mem-rte-classifier-examples", "memory.md#mem-rte-workspace-read", "memory.md#mem-obj-tool-files", "memory.md#mem-rte-retrieval-display", "runtime.md#rt-rte-retriever-training", "memory.md#mem-obj-training-data", "memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-checkpoint", "memory.md#mem-obj-query-record", "runtime.md#rt-rte-case-admission", "memory.md#mem-obj-workspace-files"]
      note: "Query-requested example selection, explicit file/CLI reads and operator-started training are pull operations. Automatic startup/reload supplies persisted pools, checkpoint state and restart keys without a consumer request for individual records. Opaque file/log alternatives lack established later routes."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Automatic bank/restart-file scan and configured checkpoint loading"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-query-record", "memory.md#mem-obj-checkpoint", "memory.md#mem-rte-classifier-examples", "runtime.md#rt-rte-case-admission"]
              note: "Loading supplies available configured retained state; it does not relevance-match individual examples for unsolicited delivery."
          records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-query-record", "memory.md#mem-obj-checkpoint", "memory.md#mem-rte-classifier-examples", "runtime.md#rt-rte-case-admission"]
          note: "Trigger is driver initialization or completed-query reload; selector input is configured path/existence or persisted result availability; selected material is the loaded pool, numerical checkpoint or restart keys. A path alone is not targeted identity matching of delivered parts."
        - scope: "Query-requested case retrieval, explicit workspace/file/CLI reads and requested training inputs"
          assessment: "inapplicable"
          findings: []
          records: ["memory.md#mem-rte-embedding-examples", "memory.md#mem-rte-classifier-examples", "memory.md#mem-rte-workspace-read", "memory.md#mem-obj-tool-files", "memory.md#mem-rte-retrieval-display", "runtime.md#rt-rte-retriever-training"]
          note: "These units are fully classified as pull; their embeddings, judgment scores or filenames are not push-selection signals."
        - scope: "Unestablished log/opaque-payload and unspecified helper consumer alternatives"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-workspace-files", "memory.md#mem-obj-tool-files", "memory.md#mem-rte-retrieval-display"]
          note: "No recorded push selector or complete direction assessment permits a signal value or inapplicability for these alternatives."
      records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-query-record", "memory.md#mem-obj-checkpoint", "memory.md#mem-rte-classifier-examples", "runtime.md#rt-rte-case-admission", "memory.md#mem-rte-embedding-examples", "memory.md#mem-rte-workspace-read", "memory.md#mem-obj-tool-files", "memory.md#mem-rte-retrieval-display", "runtime.md#rt-rte-retriever-training", "memory.md#mem-obj-workspace-files"]
      note: "Push loading is coarse availability/configuration based. Embedding/classifier relevance belongs to pull selection, not an inferred push signal. Unestablished alternative consumers prevent axis inapplicability or complete coverage."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Automatic latest-plan/outcome case writes followed by later model examples"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "runtime.md#rt-rte-case-admission", "memory.md#mem-rte-embedding-examples", "memory.md#mem-rte-classifier-examples"]
              note: "Completed benchmark activity automatically produces durable example guidance with later model consumers."
          records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "runtime.md#rt-rte-case-admission", "memory.md#mem-rte-embedding-examples", "memory.md#mem-rte-classifier-examples"]
          note: "Reduced experience is retained and delivered to later questions; no improvement or exercised reliance is required for this architectural classification."
        - scope: "Retrieved-case/outcome pair admission, separately launched parameter update and later checkpoint ranking"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records: ["memory.md#mem-obj-training-data", "memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-retriever-training", "memory.md#mem-rte-classifier-examples"]
              note: "Recorded experience automatically feeds retained training artifacts/parameters that shape later ranking."
          records: ["memory.md#mem-obj-training-data", "memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-retriever-training", "memory.md#mem-rte-classifier-examples"]
          note: "Operator launch does not make each gradient/save manual; later inference requires initialization, not just text reload."
        - scope: "Workspace/tool payload writes, retained raw results/logs beyond known consumers and initial data/assets"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-workspace-files", "memory.md#mem-obj-tool-files", "memory.md#mem-obj-query-record", "memory.md#mem-obj-training-data", "memory.md#mem-obj-checkpoint"]
          note: "Arbitrary commands may derive durable content, but no complete trace-to-derived-to-behavior consumer chain is recorded for these alternatives. Raw log retention alone is insufficient, and no bounded absence record warrants no."
      records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "runtime.md#rt-rte-case-admission", "memory.md#mem-rte-embedding-examples", "memory.md#mem-rte-classifier-examples", "memory.md#mem-obj-training-data", "memory.md#mem-obj-checkpoint", "runtime.md#rt-rte-retriever-training", "memory.md#mem-obj-workspace-files", "memory.md#mem-obj-tool-files", "memory.md#mem-obj-query-record"]
      note: "Automatic outcome-fed case writes and numerical training produce durable behavior-shaping material with wired later consumers. Other tool-file transformations, initial provenance and raw logs do not establish a qualifying update or bounded system-wide negative."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Benchmark activity feeding case reduction and retrieved-case/current-outcome pairs, then retriever training"
          assessment: "partial"
          findings:
            - value: "trajectories"
              basis: "wired"
              records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-training-data", "memory.md#mem-obj-query-record", "runtime.md#rt-rte-case-admission", "runtime.md#rt-rte-retriever-training"]
              note: "The write consumes a query record/latest action plan and its final judged outcome; pair training combines prior case experience with current-query outcome. Full recorded tool histories and rationale are omitted from these derived artifacts."
          records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-training-data", "memory.md#mem-obj-query-record", "runtime.md#rt-rte-case-admission", "runtime.md#rt-rte-retriever-training"]
          note: "Linked query, task plan and outcome support trajectories for the inspected subsequent route. Prior case genealogy and initial training rows are unauthenticated; exact full-trace provenance cannot be inferred."
        - scope: "Initial corpus/assets and possible trace-fed workspace/tool-file alternatives"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-training-data", "memory.md#mem-obj-checkpoint", "memory.md#mem-obj-workspace-files", "memory.md#mem-obj-tool-files"]
          note: "Missing genealogy and opaque command/service inputs prevent classifying original qualifying trace inputs. Static imports alone do not establish trace sources."
      records: ["memory.md#mem-obj-dummy-memo", "memory.md#mem-obj-memory", "memory.md#mem-obj-training-data", "memory.md#mem-obj-query-record", "runtime.md#rt-rte-case-admission", "runtime.md#rt-rte-retriever-training", "memory.md#mem-obj-checkpoint", "memory.md#mem-obj-workspace-files", "memory.md#mem-obj-tool-files"]
      note: "The qualifying driver chains use linked benchmark question, proposed task plan and judged outcome as reduced multi-step experience. This is not a claim that full trajectories/tool traces enter the case bank or trainer. Initial and arbitrary-tool inputs remain unresolved."
---

# AgentFly memory profile

## Comparison rationale

This comparison classifies local retained objects and their actual consumers, not all runtime storage. The accepted records establish both case banks, result/recovery records, training pairs, numerical checkpoint outputs and tool-local files. External provider retention is outside the memory boundary; opaque local binaries remain inside it. The missing checkpoint prevents inspecting exact content and deployment, not identifying the numerical form or the inspected update/load mechanisms ([MEM-OBJ-checkpoint](memory.md#mem-obj-checkpoint)). No source files were read for this profile; all warrants come from supplied accepted records.

The reconciliation supersedes the epistemic training-entry declaration with [MEM-OBJ-training-data](memory.md#mem-obj-training-data), which supplies this profile's pair-artifact citations. The combined [EPI-OBJ-case-entry](epistemic.md#epi-obj-case-entry) remains a valid container; the two driver-specific bank records supply separate selector and schema findings. No supersession strengthens evidence or removes provenance uncertainty.

Cases give contextual advice through user-role examples. Static system prompts explain how to interpret those examples but are not accumulated instruction memory. The retained labels partition examples; retained text and numerical parameters determine ranking. Training pairs have learning authority at the optimizer, whereas trained parameters have ranking authority downstream. Result keys route and enforce restart skipping; rationale retention does not establish a rationale reader ([RT-BAP-case-guidance](runtime.md#rt-bap-case-guidance), [MEM-OBJ-query-record](memory.md#mem-obj-query-record), [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training)). No validation authority is inferred from a current-run judge or trainer metric that is not itself retained and later consumed.

Requested query retrieval is pull, including its fulfilled model delivery. Startup/reload is a distinct automatic supply operation: available configured banks, checkpoint parameters and restart keys are loaded without selecting individual relevant items. Its coarse signal must not be conflated with the embeddings/classifier scores used on the later pull request. Requested filenames and configured checkpoint paths alone do not establish identifier-targeted push. Unspecified helpers and unread logs supply no additional resolved routes ([MEM-RTE-embedding-examples](memory.md#mem-rte-embedding-examples), [MEM-RTE-classifier-examples](memory.md#mem-rte-classifier-examples), [MEM-RTE-retrieval-display](memory.md#mem-rte-retrieval-display)).

The cases reduce completed run material to latest-plan/outcome examples; that is consolidation even though rich results remain. Checkpoint optimization and workspace replacement revise retained state. Append, reload, parsing filters and transient prompt formatting do not by themselves add deduplication, synthesis, decay or promotion. Formatting can omit evidence fields without introducing a new claim ([EPI-RTE-case-format](epistemic.md#epi-rte-case-format)). Unknown command/converter transformations stay unresolved rather than receiving unsupported negatives.

Both case guidance and outcome-fed numerical training meet the profile's trace-learning test at wired strength. Starting training manually is not a per-update content decision. Linked benchmark question, task plan and outcome provide reduced trajectory experience; full tool histories and judge reasons are retained only in results and do not thereby become update inputs. Prior case genealogy remains unresolved, so trace-source coverage is partial. Neither these writes nor later loading establishes observed reliance, causal case utility, successful learning or scheduled live deployment ([RT-RTE-case-admission](runtime.md#rt-rte-case-admission), [MEM-OBJ-training-data](memory.md#mem-obj-training-data), [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training)).

All positive findings retain implementation-level wiring, not observed or causal evidence. Unknown initial control, opaque binaries, arbitrary tool derivations and missing consumer facts remain local units; a resolved witness does not eliminate them from the inventory.
