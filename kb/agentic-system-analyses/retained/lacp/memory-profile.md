---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: LACP memory comparison across native persistence, host recovery/SMS, research and hybrid
  retrieval, learning events and retained control/source revisions, with unresolved offline and external
  alternatives.
run-id: AAS-2026-10-14-lacp-91efd16f7a35-01
source-identity: https://github.com/0xNyk/lacp
reviewed-boundary: e31f134b689afd6a71d94b0420682d1f528d6fa1
memory-comparison:
  version: 2
  scope: 'Accumulated or revised memory: native keyed JSON and saved conversations; Stop-derived handoffs,
    SMS episodes/self-model/narrative/epochs; research staging/inbox/registry/graph; daily captures and
    adopted durable text; hybrid chunk/sparse/dense index; captured learning events and retained promotion
    controls; workflow transition state; improvement source/history; their access, admission, maintenance
    and later-consumer routes. Includes unresolved session/article/repository/code synchronization, research
    consolidation, gap/link/review generation, MCP-memory rendering, quarantine/threshold maintenance,
    ingestion delegates, revised installed capabilities and external-host checkpoint alternatives. Excludes
    unchanged shipped instructions/scaffolds, ordinary transient current-turn state, unrelated runtime
    storage, and provider inference weights not established as accumulated or changed memory. External
    memory internals remain unresolved rather than assigned the local adapter properties.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Native keyed entry files
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-memory-entries
          note: Per-key JSON files are the operative store; a key namespace does not establish a separate
            KV service.
        records: *id001
        note: Per-key JSON files are the operative store; a key namespace does not establish a separate
          KV service.
      - scope: Native conversation across save and resume
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id002
          - runtime.md#rt-obj-messages
          - runtime.md#rt-rte-native-turn
          note: Messages reside in RAM during operation and in saved JSONL for later resume.
        - value: files
          basis: wired
          records: *id002
          note: Messages reside in RAM during operation and in saved JSONL for later resume.
        records: *id002
        note: Messages reside in RAM during operation and in saved JSONL for later resume.
      - scope: Handoff JSON
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id003
          - memory.md#mem-obj-handoff-artifact
          note: Latest per-cwd handoff and hook-contract JSON persist on disk.
        records: *id003
        note: Latest per-cwd handoff and hook-contract JSON persist on disk.
      - scope: SMS episodes
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id004
          - memory.md#mem-obj-episodes
          note: Append-only episode JSONL is retained under SMS_ROOT.
        records: *id004
        note: Append-only episode JSONL is retained under SMS_ROOT.
      - scope: SMS self-model
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id005
          - memory.md#mem-obj-self-model
          note: The operative pattern/preference object is self-model.json.
        records: *id005
        note: The operative pattern/preference object is self-model.json.
      - scope: SMS narrative
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id006
          - memory.md#mem-obj-agent-narrative
          note: Narrative has a known JSON-file substrate despite unresolved admission.
        records: *id006
        note: Narrative has a known JSON-file substrate despite unresolved admission.
      - scope: SMS epochs
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id007
          - memory.md#mem-obj-epochs
          note: Epochs are appended to a distinct JSONL file, not the narrative file.
        records: *id007
        note: Epochs are appended to a distinct JSONL file, not the narrative file.
      - scope: Research staging, inbox, registry and graph notes
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id008
          - memory.md#mem-obj-research-memory
          note: Staging JSONL, inbox Markdown and registry JSON are files; materialized linked graph Markdown
            supplies a graph access structure, not a graph database claim.
        - value: graph
          basis: wired
          records: *id008
          note: Staging JSONL, inbox Markdown and registry JSON are files; materialized linked graph Markdown
            supplies a graph access structure, not a graph database claim.
        records: *id008
        note: Staging JSONL, inbox Markdown and registry JSON are files; materialized linked graph Markdown
          supplies a graph access structure, not a graph database claim.
      - scope: Daily captures, suggestion reports and adopted durable bullets
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id009
          - memory.md#mem-rte-daily-promotion
          - epistemic.md#epi-rte-memory-promotions
          note: Daily and durable Markdown and suggestion reports are retained files.
        records: *id009
        note: Daily and durable Markdown and suggestion reports are retained files.
      - scope: Hybrid retained chunk index
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id010
          - memory.md#mem-obj-hybrid-index
          note: JSON retains chunks, sparse weights and optional dense vectors; vector denotes the vector
            retrieval structure, not a separately established vector database.
        - value: vector
          basis: wired
          records: *id010
          note: JSON retains chunks, sparse weights and optional dense vectors; vector denotes the vector
            retrieval structure, not a separately established vector database.
        records: *id010
        note: JSON retains chunks, sparse weights and optional dense vectors; vector denotes the vector
          retrieval structure, not a separately established vector database.
      - scope: Cross-CLI captured events and promotion state
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id011
          - memory.md#mem-obj-learning-events
          - runtime.md#rt-rte-learning-promotion
          note: Canonical event JSONL, promotion-state JSON and receipts persist on the filesystem.
        records: *id011
        note: Canonical event JSONL, promotion-state JSON and receipts persist on the filesystem.
      - scope: Workflow progression state
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id012
          - runtime.md#rt-rte-workflow-advance
          note: Persisted state.json and transition history govern later advance/status invocations.
        records: *id012
        note: Persisted state.json and transition history govern later advance/status invocations.
      - scope: Improvement source, logs and result history
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id013
          - runtime.md#rt-rte-idle-experiment
          - runtime.md#rt-bap-autoresearch-code
          note: Changed source and Git commits are retained in the repository; logs and TSV results persist
            as files. Static shipped program content alone is not accumulated memory.
        - value: repo
          basis: wired
          records: *id013
          note: Changed source and Git commits are retained in the repository; logs and TSV results persist
            as files. Static shipped program content alone is not accumulated memory.
        records: *id013
        note: Changed source and Git commits are retained in the repository; logs and TSV results persist
          as files. Static shipped program content alone is not accumulated memory.
      - scope: Included alternative offline and external memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-trace-research
        - memory.md#mem-rte-memory-maintenance
        - memory.md#mem-rte-vault-access
        - runtime.md#rt-rte-extension-load
        note: Session-history mirroring, article/repository/code synchronization, research consolidation,
          gap/link and review-queue generation, generated MCP memory, quarantine hygiene, threshold recalibration,
          ingestion delegates and deployed external MCP/QMD memory remain incompletely inspected. Their
          retained outputs, transformations, admission and later consumers cannot be completely classified
          from the accepted records. These are included alternatives, not excluded stores or evidenced
          absences.
      - scope: External-host retained conversation or compaction state
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-host-launch
        note: Host persistence and checkpoint internals are outside the inspected adapter; returned text
          saved in native messages does not classify the host store.
      records:
      - memory.md#mem-obj-memory-entries
      - runtime.md#rt-obj-messages
      - runtime.md#rt-rte-native-turn
      - memory.md#mem-obj-handoff-artifact
      - memory.md#mem-obj-episodes
      - memory.md#mem-obj-self-model
      - memory.md#mem-obj-agent-narrative
      - memory.md#mem-obj-epochs
      - memory.md#mem-obj-research-memory
      - memory.md#mem-rte-daily-promotion
      - epistemic.md#epi-rte-memory-promotions
      - memory.md#mem-obj-hybrid-index
      - memory.md#mem-obj-learning-events
      - runtime.md#rt-rte-learning-promotion
      - runtime.md#rt-rte-workflow-advance
      - runtime.md#rt-rte-idle-experiment
      - runtime.md#rt-bap-autoresearch-code
      - memory.md#mem-rte-trace-research
      - memory.md#mem-rte-memory-maintenance
      - memory.md#mem-rte-vault-access
      - runtime.md#rt-rte-extension-load
      - runtime.md#rt-rte-host-launch
      note: Known file-backed, graph, vector-access, in-memory and repository parts coexist with uninspected
        offline/external alternatives; this is not a complete substrate union.
    representational_form:
      assessment: partial
      units:
      - scope: Native keyed content at model/tool-result interpretation
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id014
          - memory.md#mem-obj-memory-entries
          note: Content text is interpreted as natural-language context; key/tags/time are separately
            assessed.
        records: *id014
        note: Content text is interpreted as natural-language context; key/tags/time are separately assessed.
      - scope: Native keyed metadata at lookup/search
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id015
          - memory.md#mem-obj-memory-entries
          - memory.md#mem-rte-keyed-memory
          note: Keys and JSON envelopes are localized symbolic fields; search also inspects serialized
            metadata.
        records: *id015
        note: Keys and JSON envelopes are localized symbolic fields; search also inspects serialized metadata.
      - scope: Saved/resumed message text at provider
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id016
          - runtime.md#rt-obj-messages
          - runtime.md#rt-rte-native-turn
          note: Conversation text supplies interpreted model context.
        records: *id016
        note: Conversation text supplies interpreted model context.
      - scope: Message roles, tool IDs and JSONL envelope
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id017
          - runtime.md#rt-obj-messages
          note: Code routes role/type/identifier fields with fixed rules.
        records: *id017
        note: Code routes role/type/identifier fields with fixed rules.
      - scope: Handoff summary and diff text at host
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id018
          - memory.md#mem-obj-handoff-artifact
          note: Startup supplies selected textual recovery context, not the whole JSON payload.
        records: *id018
        note: Startup supplies selected textual recovery context, not the whole JSON payload.
      - scope: Handoff path, branch, timestamp and checkpoint fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id019
          - memory.md#mem-obj-handoff-artifact
          - memory.md#mem-rte-session-memory
          note: Fixed code uses identity, age and status fields in recovery selection.
        records: *id019
        note: Fixed code uses identity, age and status fields in recovery selection.
      - scope: SMS episode summaries at host and epoch readers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id020
          - memory.md#mem-obj-episodes
          note: Summaries and copied decision text are natural-language material.
        records: *id020
        note: Summaries and copied decision text are natural-language material.
      - scope: SMS episode selection metadata
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id021
          - memory.md#mem-obj-episodes
          note: Time, project, files and significance have localized symbolic representation.
        records: *id021
        note: Time, project, files and significance have localized symbolic representation.
      - scope: SMS preference, failure and other self-model text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id022
          - memory.md#mem-obj-self-model
          note: Pattern lists are interpreted text, including retained fields not delivered at startup.
        records: *id022
        note: Pattern lists are interpreted text, including retained fields not delivered at startup.
      - scope: SMS self-model counter/confidence gate
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id023
          - memory.md#mem-obj-self-model
          - memory.md#mem-rte-session-memory
          note: Fixed thresholding consumes numeric confidence and update count as symbolic fields, not
            distributed parameters.
        records: *id023
        note: Fixed thresholding consumes numeric confidence and update count as symbolic fields, not
          distributed parameters.
      - scope: SMS narrative text and arc
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id024
          - memory.md#mem-obj-agent-narrative
          note: Current arc/themes/strengths are known text; unknown authorship does not make their form
            opaque.
        records: *id024
        note: Current arc/themes/strengths are known text; unknown authorship does not make their form
          opaque.
      - scope: SMS narrative identity and timestamp
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id025
          - memory.md#mem-obj-agent-narrative
          note: Dataclass/JSON identity and timestamp fields are symbolic.
        records: *id025
        note: Dataclass/JSON identity and timestamp fields are symbolic.
      - scope: Epoch copied decisions and labels
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id026
          - memory.md#mem-obj-epochs
          note: Copied decisions and textual labels are natural-language fields, distinct from generated
            empty themes.
        records: *id026
        note: Copied decisions and textual labels are natural-language fields, distinct from generated
          empty themes.
      - scope: Epoch grouping/count/time metadata
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id027
          - memory.md#mem-obj-epochs
          note: IDs, episode counts and timestamps are symbolic.
        records: *id027
        note: IDs, episode counts and timestamps are symbolic.
      - scope: Research and daily retained text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id028
          - memory.md#mem-obj-research-memory
          - memory.md#mem-rte-daily-promotion
          note: Extracted signals, Markdown notes and adopted bullets retain natural-language text.
        records: *id028
        note: Extracted signals, Markdown notes and adopted bullets retain natural-language text.
      - scope: Research access/admission/provenance metadata
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id029
          - memory.md#mem-obj-research-memory
          note: IDs, links, counts and confidence/access fields are symbolic.
        records: *id029
        note: IDs, links, counts and confidence/access fields are symbolic.
      - scope: Research optional embedding part
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: &id030
          - memory.md#mem-obj-research-memory
          - memory.md#mem-cmp-embedding-service
          note: Stored dense representations are distributed-parametric; this does not establish training
            or exact embedding provenance.
        records: *id030
        note: Stored dense representations are distributed-parametric; this does not establish training
          or exact embedding provenance.
      - scope: Hybrid full chunk payload
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id031
          - memory.md#mem-obj-hybrid-index
          note: Classification follows retained full text, not only the 260-character displayed preview.
        records: *id031
        note: Classification follows retained full text, not only the 260-character displayed preview.
      - scope: Hybrid sparse weights, paths and headings as selectors
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id032
          - memory.md#mem-obj-hybrid-index
          - memory.md#mem-rte-hybrid-retrieval
          note: Sparse term coordinates, paths and fixed scoring fields are symbolic; interpreted heading
            text remains part of the text payload.
        records: *id032
        note: Sparse term coordinates, paths and fixed scoring fields are symbolic; interpreted heading
          text remains part of the text payload.
      - scope: Hybrid optional dense-vector ranking part
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: &id033
          - memory.md#mem-obj-hybrid-index
          - memory.md#mem-rte-hybrid-retrieval
          note: Dense vectors spread numerical representation and influence similarity ranking.
        records: *id033
        note: Dense vectors spread numerical representation and influence similarity ranking.
      - scope: Cross-CLI event summary and outcome-note text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id034
          - memory.md#mem-obj-learning-events
          note: Textual summaries and notes are distinct from the selected summary-only hint display.
        records: *id034
        note: Textual summaries and notes are distinct from the selected summary-only hint display.
      - scope: Cross-CLI event labels, provenance and promotion controls
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id035
          - memory.md#mem-obj-learning-events
          - runtime.md#rt-rte-learning-promotion
          note: Hash/schema/score/mode fields are localized symbolic data.
        records: *id035
        note: Hash/schema/score/mode fields are localized symbolic data.
      - scope: Workflow retained status/token/history
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id036
          - runtime.md#rt-rte-workflow-advance
          note: Fixed transition checks consume symbolic JSON; optional note text remains interpreted
            prose.
        records: *id036
        note: Fixed transition checks consume symbolic JSON; optional note text remains interpreted prose.
      - scope: Workflow optional retained notes
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id037
          - runtime.md#rt-rte-workflow-advance
          note: Caller-supplied notes can be retained natural-language text; model delivery is not established.
        records: *id037
        note: Caller-supplied notes can be retained natural-language text; model delivery is not established.
      - scope: Retained changed executable source
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id038
          - runtime.md#rt-rte-idle-experiment
          - runtime.md#rt-bap-autoresearch-code
          note: Later Python imports execute symbolic source; source storage is not model-weight learning.
        records: *id038
        note: Later Python imports execute symbolic source; source storage is not model-weight learning.
      - scope: Included alternative offline and external memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-trace-research
        - memory.md#mem-rte-memory-maintenance
        - memory.md#mem-rte-vault-access
        - runtime.md#rt-rte-extension-load
        note: Session-history mirroring, article/repository/code synchronization, research consolidation,
          gap/link and review-queue generation, generated MCP memory, quarantine hygiene, threshold recalibration,
          ingestion delegates and deployed external MCP/QMD memory remain incompletely inspected. Their
          retained outputs, transformations, admission and later consumers cannot be completely classified
          from the accepted records. These are included alternatives, not excluded stores or evidenced
          absences.
      - scope: External-host checkpoint payload
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-host-launch
        note: Neither opaque host summaries nor full retained host state can be assigned a form from the
          adapter return.
      records:
      - memory.md#mem-obj-memory-entries
      - memory.md#mem-rte-keyed-memory
      - runtime.md#rt-obj-messages
      - runtime.md#rt-rte-native-turn
      - memory.md#mem-obj-handoff-artifact
      - memory.md#mem-rte-session-memory
      - memory.md#mem-obj-episodes
      - memory.md#mem-obj-self-model
      - memory.md#mem-obj-agent-narrative
      - memory.md#mem-obj-epochs
      - memory.md#mem-obj-research-memory
      - memory.md#mem-rte-daily-promotion
      - memory.md#mem-cmp-embedding-service
      - memory.md#mem-obj-hybrid-index
      - memory.md#mem-rte-hybrid-retrieval
      - memory.md#mem-obj-learning-events
      - runtime.md#rt-rte-learning-promotion
      - runtime.md#rt-rte-workflow-advance
      - runtime.md#rt-rte-idle-experiment
      - runtime.md#rt-bap-autoresearch-code
      - memory.md#mem-rte-trace-research
      - memory.md#mem-rte-memory-maintenance
      - memory.md#mem-rte-vault-access
      - runtime.md#rt-rte-extension-load
      - runtime.md#rt-rte-host-launch
      note: Mixed text, symbolic control data and dense numerical representations are split by part and
        consumer; external and offline alternatives remain unresolved.
    lineage:
      assessment: partial
      units:
      - scope: Model-proposed native keyed content
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id039
          - memory.md#mem-obj-memory-entries
          - memory.md#mem-rte-keyed-memory
          note: The foreground model supplies authored content for the inspected write path; arbitrary
            initial/caller text is not thereby trace-derived.
        records: *id039
        note: The foreground model supplies authored content for the inspected write path; arbitrary initial/caller
          text is not thereby trace-derived.
      - scope: Initial or arbitrary caller content of keyed entries
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-entries
        - memory.md#mem-rte-keyed-memory
        note: The store permits supplied opaque text without source/rationale fields; original provenance
          of arbitrary entries is not determined.
      - scope: Native persisted conversational text
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id040
          - runtime.md#rt-obj-messages
          - runtime.md#rt-rte-native-turn
          note: User/assistant contributions are authored; tool output enters conversation from execution
            results. This finding classifies the authored contributions, not every tool payload.
        records: *id040
        note: User/assistant contributions are authored; tool output enters conversation from execution
          results. This finding classifies the authored contributions, not every tool payload.
      - scope: Native imported tool-result provenance
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-messages
        - runtime.md#rt-rte-native-turn
        - runtime.md#rt-rte-host-launch
        note: The record establishes result delivery and truncation but not the original derivation of
          every possible tool or delegated output.
      - scope: Stop-derived handoffs and episodes
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id041
          - memory.md#mem-obj-handoff-artifact
          - memory.md#mem-obj-episodes
          - memory.md#mem-rte-session-memory
          note: Assistant/transcript/checkpoint signals are extracted into lossy recovery artifacts.
        records: *id041
        note: Assistant/transcript/checkpoint signals are extracted into lossy recovery artifacts.
      - scope: Automatic SMS self-model update
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id042
          - memory.md#mem-obj-self-model
          - epistemic.md#epi-rte-self-model-update
          note: Heuristics derive durable pattern/preference content from recorded summary and outcome
            signals.
        records: *id042
        note: Heuristics derive durable pattern/preference content from recorded summary and outcome signals.
      - scope: Initial narrative and separately supplied SMS content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-agent-narrative
        - memory.md#mem-obj-self-model
        note: Narrative replacement is exposed but initial author/admission and provenance are unresolved;
          automatic self-model updates do not resolve initial bias/preference content.
      - scope: Epoch grouping and decision copy
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id043
          - memory.md#mem-obj-epochs
          - memory.md#mem-rte-epoch-synthesis
          note: Deterministic copying/grouping compiles retained episodes into another representation;
            original decision lineage remains only as good as episode inputs.
        records: *id043
        note: Deterministic copying/grouping compiles retained episodes into another representation; original
          decision lineage remains only as good as episode inputs.
      - scope: Assistant/history-derived research path
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id044
          - memory.md#mem-obj-research-memory
          - memory.md#mem-rte-trace-research
          note: Selected conversational signals become staging/inbox/registry/graph text, with truncation
            and title fallback.
        records: *id044
        note: Selected conversational signals become staging/inbox/registry/graph text, with truncation
          and title fallback.
      - scope: Non-trace inbox input to research
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id045
          - memory.md#mem-obj-research-memory
          - memory.md#mem-rte-trace-research
          note: The alternative inbox path imports externally supplied research material; this does not
            establish its initial author or warrant.
        records: *id045
        note: The alternative inbox path imports externally supplied research material; this does not
          establish its initial author or warrant.
      - scope: Research optional embedding and mixed initial inbox provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-research-memory
        - memory.md#mem-rte-trace-research
        - memory.md#mem-cmp-embedding-service
        note: Embedding helpers and prediction-error details are incompletely inspected; model metadata
          does not freeze weights or settle initial inbox derivation.
      - scope: History-to-daily-to-durable promotion
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id046
          - memory.md#mem-rte-daily-promotion
          - epistemic.md#epi-rte-memory-promotions
          note: Historical prompt highlights and tool/command summaries are extracted, filtered and optionally
            appended; no novel lesson follows from the route name.
        records: *id046
        note: Historical prompt highlights and tool/command summaries are extracted, filtered and optionally
          appended; no novel lesson follows from the route name.
      - scope: Hybrid Markdown-to-chunk/sparse index
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id047
          - memory.md#mem-obj-hybrid-index
          - memory.md#mem-rte-hybrid-retrieval
          note: Retained corpus text is compiled into copied chunks and access features. Rebuilding does
            not establish the corpus original provenance.
        records: *id047
        note: Retained corpus text is compiled into copied chunks and access features. Rebuilding does
          not establish the corpus original provenance.
      - scope: Hybrid dense embedding provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-hybrid-index
        - memory.md#mem-cmp-embedding-service
        note: Inference route and model metadata are known, but exact numerical model provenance is unpinned;
          sparse compilation does not settle this part.
      - scope: Cross-CLI capture source authorship
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-learning-events
        - memory.md#mem-rte-learning-hints
        note: Generic caller supplies task/outcome data; hashed canonicalization does not identify human,
          agent or original trace derivation.
      - scope: Workflow and promotion derived state
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id048
          - runtime.md#rt-rte-workflow-advance
          - runtime.md#rt-rte-learning-promotion
          note: Software compiles admitted caller values and gate outcomes into persistent transition/receipt
            data.
        records: *id048
        note: Software compiles admitted caller values and gate outcomes into persistent transition/receipt
          data.
      - scope: Delegated improvement edits
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id049
          - runtime.md#rt-rte-idle-experiment
          - runtime.md#rt-bap-autoresearch-code
          note: The improvement host authors source changes, which can remain in source/commits for later
            imports; logs alone do not establish trace-fed guidance revision.
        records: *id049
        note: The improvement host authors source changes, which can remain in source/commits for later
          imports; logs alone do not establish trace-fed guidance revision.
      - scope: Included alternative offline and external memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-trace-research
        - memory.md#mem-rte-memory-maintenance
        - memory.md#mem-rte-vault-access
        - runtime.md#rt-rte-extension-load
        note: Session-history mirroring, article/repository/code synchronization, research consolidation,
          gap/link and review-queue generation, generated MCP memory, quarantine hygiene, threshold recalibration,
          ingestion delegates and deployed external MCP/QMD memory remain incompletely inspected. Their
          retained outputs, transformations, admission and later consumers cannot be completely classified
          from the accepted records. These are included alternatives, not excluded stores or evidenced
          absences.
      records:
      - memory.md#mem-obj-memory-entries
      - memory.md#mem-rte-keyed-memory
      - runtime.md#rt-obj-messages
      - runtime.md#rt-rte-native-turn
      - runtime.md#rt-rte-host-launch
      - memory.md#mem-obj-handoff-artifact
      - memory.md#mem-obj-episodes
      - memory.md#mem-rte-session-memory
      - memory.md#mem-obj-self-model
      - epistemic.md#epi-rte-self-model-update
      - memory.md#mem-obj-agent-narrative
      - memory.md#mem-obj-epochs
      - memory.md#mem-rte-epoch-synthesis
      - memory.md#mem-obj-research-memory
      - memory.md#mem-rte-trace-research
      - memory.md#mem-cmp-embedding-service
      - memory.md#mem-rte-daily-promotion
      - epistemic.md#epi-rte-memory-promotions
      - memory.md#mem-obj-hybrid-index
      - memory.md#mem-rte-hybrid-retrieval
      - memory.md#mem-obj-learning-events
      - memory.md#mem-rte-learning-hints
      - runtime.md#rt-rte-workflow-advance
      - runtime.md#rt-rte-learning-promotion
      - runtime.md#rt-rte-idle-experiment
      - runtime.md#rt-bap-autoresearch-code
      - memory.md#mem-rte-memory-maintenance
      - memory.md#mem-rte-vault-access
      - runtime.md#rt-rte-extension-load
      note: Known derivation paths do not settle initial text or embedding provenance. Trace extraction,
        imported research, authored contributions and compiled access/control structures are separate
        positives.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Keyed content returned to foreground model
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id050
          - memory.md#mem-obj-memory-entries
          - memory.md#mem-rte-keyed-memory
          note: Actual tool-result delivery supplies retained reference/context; action changes remain
            unobserved.
        records: *id050
        note: Actual tool-result delivery supplies retained reference/context; action changes remain unobserved.
      - scope: Saved messages restored as later provider conversation
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id051
          - runtime.md#rt-obj-messages
          - runtime.md#rt-rte-native-turn
          note: Resumed content provides conversational knowledge/context, not an independent acceptance
            criterion.
        records: *id051
        note: Resumed content provides conversational knowledge/context, not an independent acceptance
          criterion.
      - scope: Handoff and SMS episode/arc text at later host
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id052
          - memory.md#mem-obj-handoff-artifact
          - memory.md#mem-obj-episodes
          - memory.md#mem-obj-agent-narrative
          - memory.md#mem-rte-session-memory
          note: Selected recovery summaries, episodes and current arc supply interpreted context through
            systemMessage.
        records: *id052
        note: Selected recovery summaries, episodes and current arc supply interpreted context through
          systemMessage.
      - scope: Selected SMS preferences and caution at host
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id053
          - memory.md#mem-obj-self-model
          - memory.md#mem-rte-session-memory
          - epistemic.md#epi-rte-self-model-update
          note: Preferred approaches, biases and failures supply standing behavioral directions; retained
            success labels are not all delivered.
        records: *id053
        note: Preferred approaches, biases and failures supply standing behavioral directions; retained
          success labels are not all delivered.
      - scope: Episode and session signals at self-model/recovery update
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id054
          - memory.md#mem-obj-episodes
          - memory.md#mem-rte-session-memory
          - epistemic.md#epi-rte-self-model-update
          note: Retained experience feeds durable pattern/preference and recovery-artifact updates; learning
            authority at update is distinct from instruction/context at host.
        records: *id054
        note: Retained experience feeds durable pattern/preference and recovery-artifact updates; learning
          authority at update is distinct from instruction/context at host.
      - scope: Retained self-model confidence and episode significance at startup selector
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id055
          - memory.md#mem-obj-self-model
          - memory.md#mem-obj-episodes
          - memory.md#mem-rte-session-memory
          note: Confidence gates field delivery and significance/recency prioritize episode eligibility;
            these retained fields affect selection priority rather than prove truth.
        records: *id055
        note: Confidence gates field delivery and significance/recency prioritize episode eligibility;
          these retained fields affect selection priority rather than prove truth.
      - scope: Retained handoff cwd/time and SMS confidence at delivery routing
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id056
          - memory.md#mem-obj-handoff-artifact
          - memory.md#mem-rte-session-memory
          note: Cwd identity and age select the recovery artifact; confidence selects whether a self-model
            context part is eligible.
        records: *id056
        note: Cwd identity and age select the recovery artifact; confidence selects whether a self-model
          context part is eligible.
      - scope: Epochs at CLI display
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id057
          - memory.md#mem-obj-epochs
          - memory.md#mem-rte-epoch-synthesis
          note: Later CLI exposes copied episode decisions as reference for caller interpretation; no
            startup narrative consumer is established.
        records: *id057
        note: Later CLI exposes copied episode decisions as reference for caller interpretation; no startup
          narrative consumer is established.
      - scope: Research text, counts and access features at admission/publication
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id058
          - memory.md#mem-obj-research-memory
          - memory.md#mem-rte-trace-research
          note: Counts, confidence and retained text affect selection/priority of registry candidates
            and graph publication.
        records: *id058
        note: Counts, confidence and retained text affect selection/priority of registry candidates and
          graph publication.
      - scope: Research blocked IDs at ingestion
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id059
          - memory.md#mem-rte-trace-research
          note: 'A retained blocked-ID criterion rejects matching candidate admission: it both validates
            admissibility and enforces a veto, not factual truth.'
        - value: enforcement
          basis: wired
          records: *id059
          note: 'A retained blocked-ID criterion rejects matching candidate admission: it both validates
            admissibility and enforces a veto, not factual truth.'
        records: *id059
        note: 'A retained blocked-ID criterion rejects matching candidate admission: it both validates
          admissibility and enforces a veto, not factual truth.'
      - scope: History/daily text at durable extraction and promotion
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id060
          - memory.md#mem-rte-trace-research
          - memory.md#mem-rte-daily-promotion
          - epistemic.md#epi-rte-memory-promotions
          note: Retained historical inputs feed durable guidance/reference updates even without observed
            improvement.
        records: *id060
        note: Retained historical inputs feed durable guidance/reference updates even without observed
          improvement.
      - scope: Hybrid retained text and sparse features at ranking
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id061
          - memory.md#mem-obj-hybrid-index
          - memory.md#mem-rte-hybrid-retrieval
          - epistemic.md#epi-rte-retrieval-ranking
          note: Chunk text and access features affect relative retrieval score under fixed code; no retained
            learned ranking policy is required.
        records: *id061
        note: Chunk text and access features affect relative retrieval score under fixed code; no retained
          learned ranking policy is required.
      - scope: Hybrid retained dense vectors at numerical ranking
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id062
          - memory.md#mem-obj-hybrid-index
          - memory.md#mem-rte-hybrid-retrieval
          note: The separate dense part influences similarity priority when enabled; fallback does not
            erase its supported optional path.
        records: *id062
        note: The separate dense part influences similarity priority when enabled; fallback does not erase
          its supported optional path.
      - scope: Selected hybrid chunks at CLI and evaluator
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id063
          - memory.md#mem-obj-hybrid-index
          - memory.md#mem-rte-hybrid-retrieval
          note: Returned retained text supplies reference/context; benchmark/probe interpretation is wired,
            foreground task-model integration only afforded.
        records: *id063
        note: Returned retained text supplies reference/context; benchmark/probe interpretation is wired,
          foreground task-model integration only afforded.
      - scope: Retained probe results and registry features at forgetting
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id064
          - memory.md#mem-rte-memory-maintenance
          - epistemic.md#epi-rte-consolidation-policy
          note: Probe gap/importance and registry strength/edges protect or prioritize archival candidates.
            They constrain maintenance rather than establish source truth.
        - value: validation
          basis: wired
          records: *id064
          note: Probe gap/importance and registry strength/edges protect or prioritize archival candidates.
            They constrain maintenance rather than establish source truth.
        records: *id064
        note: Probe gap/importance and registry strength/edges protect or prioritize archival candidates.
          They constrain maintenance rather than establish source truth.
      - scope: Cross-CLI retained event fields at advisory ranking
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id065
          - memory.md#mem-obj-learning-events
          - memory.md#mem-rte-learning-hints
          note: Summary tokens, trust, status/score and recency affect relative priority and eligibility
            of hints.
        records: *id065
        note: Summary tokens, trust, status/score and recency affect relative priority and eligibility
          of hints.
      - scope: Selected event summaries at advisory caller
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id066
          - memory.md#mem-obj-learning-events
          - memory.md#mem-rte-learning-hints
          note: Printed retained summaries offer advice/reference; query is explicitly non-routing and
            does not read enforce-state as activation.
        records: *id066
        note: Printed retained summaries offer advice/reference; query is explicitly non-routing and does
          not read enforce-state as activation.
      - scope: Retained event labels at metric gate
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id067
          - memory.md#mem-obj-learning-events
          - epistemic.md#epi-rte-learning-metrics
          - runtime.md#rt-rte-learning-promotion
          note: Reloaded event labels yield metric predicates used by promotion admission. This is validation
            for mode transition, not acceptance of each assertion.
        records: *id067
        note: Reloaded event labels yield metric predicates used by promotion admission. This is validation
          for mode transition, not acceptance of each assertion.
      - scope: Promotion state at re-promotion and rollback
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id068
          - runtime.md#rt-rte-learning-promotion
          note: Saved mode/active-promotion state selects later status, re-promotion refusal or rollback
            progression; downstream host enforcement remains unresolved.
        - value: enforcement
          basis: wired
          records: *id068
          note: Saved mode/active-promotion state selects later status, re-promotion refusal or rollback
            progression; downstream host enforcement remains unresolved.
        records: *id068
        note: Saved mode/active-promotion state selects later status, re-promotion refusal or rollback
          progression; downstream host enforcement remains unresolved.
      - scope: Workflow retained stage/token at next advance
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id069
          - runtime.md#rt-rte-workflow-advance
          note: Stored stage/owner/token controls which transition is admissible and can refuse advancement;
            history notes do not verify completed work.
        - value: validation
          basis: wired
          records: *id069
          note: Stored stage/owner/token controls which transition is admissible and can refuse advancement;
            history notes do not verify completed work.
        - value: enforcement
          basis: wired
          records: *id069
          note: Stored stage/owner/token controls which transition is admissible and can refuse advancement;
            history notes do not verify completed work.
        records: *id069
        note: Stored stage/owner/token controls which transition is admissible and can refuse advancement;
          history notes do not verify completed work.
      - scope: Improvement TSV count at experiment scheduler
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id070
          - runtime.md#rt-rte-idle-experiment
          note: Retained history count selects whether further experiments are eligible, not content-directed
            criticism.
        records: *id070
        note: Retained history count selects whether further experiments are eligible, not content-directed
          criticism.
      - scope: Changed source at later imports
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-idle-experiment
        - runtime.md#rt-bap-autoresearch-code
        note: Executable authority is established, but the exact changed functions/effects are not individuated;
          execution is not itself one controlled authority value. Static program instructions are excluded
          unless revised through use.
      - scope: All retained SMS fields and initial narrative at other consumers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-self-model
        - memory.md#mem-obj-agent-narrative
        note: Full CLI displays and startup arc/preference subsets differ. Unconsumed success/effective-context
          metadata does not acquire startup authority by association.
      - scope: Included alternative offline and external memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-trace-research
        - memory.md#mem-rte-memory-maintenance
        - memory.md#mem-rte-vault-access
        - runtime.md#rt-rte-extension-load
        note: Session-history mirroring, article/repository/code synchronization, research consolidation,
          gap/link and review-queue generation, generated MCP memory, quarantine hygiene, threshold recalibration,
          ingestion delegates and deployed external MCP/QMD memory remain incompletely inspected. Their
          retained outputs, transformations, admission and later consumers cannot be completely classified
          from the accepted records. These are included alternatives, not excluded stores or evidenced
          absences.
      records:
      - memory.md#mem-obj-memory-entries
      - memory.md#mem-rte-keyed-memory
      - runtime.md#rt-obj-messages
      - runtime.md#rt-rte-native-turn
      - memory.md#mem-obj-handoff-artifact
      - memory.md#mem-obj-episodes
      - memory.md#mem-obj-agent-narrative
      - memory.md#mem-rte-session-memory
      - memory.md#mem-obj-self-model
      - epistemic.md#epi-rte-self-model-update
      - memory.md#mem-obj-epochs
      - memory.md#mem-rte-epoch-synthesis
      - memory.md#mem-obj-research-memory
      - memory.md#mem-rte-trace-research
      - memory.md#mem-rte-daily-promotion
      - epistemic.md#epi-rte-memory-promotions
      - memory.md#mem-obj-hybrid-index
      - memory.md#mem-rte-hybrid-retrieval
      - epistemic.md#epi-rte-retrieval-ranking
      - memory.md#mem-rte-memory-maintenance
      - epistemic.md#epi-rte-consolidation-policy
      - memory.md#mem-obj-learning-events
      - memory.md#mem-rte-learning-hints
      - epistemic.md#epi-rte-learning-metrics
      - runtime.md#rt-rte-learning-promotion
      - runtime.md#rt-rte-workflow-advance
      - runtime.md#rt-rte-idle-experiment
      - runtime.md#rt-bap-autoresearch-code
      - memory.md#mem-rte-vault-access
      - runtime.md#rt-rte-extension-load
      note: Authority belongs to the named consumed part and effect. Retained text can rank before supplying
        knowledge; trace inputs can supply learning at an update consumer without proving improvement
        or downstream enforcement.
    write_agency:
      assessment: partial
      units:
      - scope: Foreground model keyed-memory admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id071
          - memory.md#mem-rte-keyed-memory
          note: Model-selected content is written after nonempty checks without per-content human approval.
        records: *id071
        note: Model-selected content is written after nonempty checks without per-content human approval.
      - scope: Native conversation save
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id072
          - runtime.md#rt-obj-messages
          - runtime.md#rt-rte-native-turn
          note: Software saves the accumulated message list on its save paths; writing user turns is not
            a separate explicit human approval of the saved whole.
        records: *id072
        note: Software saves the accumulated message list on its save paths; writing user turns is not
          a separate explicit human approval of the saved whole.
      - scope: Stop handoff, episode and self-model admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id073
          - memory.md#mem-rte-session-memory
          - epistemic.md#epi-rte-self-model-update
          note: Stop capture/heuristics select retained content before later quality judgment, without
            a per-content human gate.
        records: *id073
        note: Stop capture/heuristics select retained content before later quality judgment, without a
          per-content human gate.
      - scope: Narrative replacement admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-agent-narrative
        note: Library physical replacement does not identify the decision maker; no inspected constructing/admitting
          caller establishes manual or automatic admission.
      - scope: Initial self-model fields and direct replacement
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-self-model
        - memory.md#mem-rte-epoch-synthesis
        note: Heuristic subsequent updates are automatic, but initial preference/bias content and separately
          supplied replacements have unresolved control.
      - scope: Epoch derivation and append
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id074
          - memory.md#mem-obj-epochs
          - memory.md#mem-rte-epoch-synthesis
          note: Caller starts synthesis; software selects episodes and copied decisions, not a human deciding
            each retained epoch content.
        records: *id074
        note: Caller starts synthesis; software selects episodes and copied decisions, not a human deciding
          each retained epoch content.
      - scope: Trace staging and research synchronization
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id075
          - memory.md#mem-obj-research-memory
          - memory.md#mem-rte-trace-research
          note: Heuristics, graph admission and apply-enabled publication select content; starting apply
            is not per-candidate human approval.
        records: *id075
        note: Heuristics, graph admission and apply-enabled publication select content; starting apply
          is not per-candidate human approval.
      - scope: Daily capture and optional durable-bullet apply
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id076
          - memory.md#mem-rte-daily-promotion
          - epistemic.md#epi-rte-memory-promotions
          note: Software chooses and appends eligible bullets when enabled; pipeline suggestions without
            apply are a separate non-adopting invocation.
        records: *id076
        note: Software chooses and appends eligible bullets when enabled; pipeline suggestions without
          apply are a separate non-adopting invocation.
      - scope: Hybrid index admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id077
          - memory.md#mem-obj-hybrid-index
          - memory.md#mem-rte-hybrid-retrieval
          note: Builder admits current eligible filesystem corpus and derived features without per-document
            operator approval.
        records: *id077
        note: Builder admits current eligible filesystem corpus and derived features without per-document
          operator approval.
      - scope: Rename, prune, cap and archive selection
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id078
          - memory.md#mem-rte-memory-maintenance
          - epistemic.md#epi-rte-consolidation-policy
          - epistemic.md#epi-rte-title-renaming
          note: Software selects changes/discards after enablement; driver/parser mismatch limits actual
            archive-driver activation, not helper selection agency.
        records: *id078
        note: Software selects changes/discards after enablement; driver/parser mismatch limits actual
          archive-driver activation, not helper selection agency.
      - scope: Direct resolution status/reason admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-memory-maintenance
        note: Caller supplies the actual status/reason; the records require no authenticated human and
          do not establish whether a human or agent decides the supplied content.
      - scope: Cross-CLI caller capture and supplied promotion evidence
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-learning-events
        - memory.md#mem-rte-learning-hints
        - runtime.md#rt-rte-learning-promotion
        note: Generic caller provides task/outcome/evidence/names. Code checks form/gates, but manual-labelled
          inputs are not proof of a human decision.
      - scope: Workflow supplied decisions and note content
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-workflow-advance
        note: Actor strings and approve/reject values do not identify human versus computational admission
          of the recorded decision.
      - scope: Idle delegated source edits and numeric keep/discard
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id079
          - runtime.md#rt-rte-idle-experiment
          note: User enables experiments but model/host proposes edits and code decides score disposition
            without per-edit human approval.
        records: *id079
        note: User enables experiments but model/host proposes edits and code decides score disposition
          without per-edit human approval.
      - scope: Installed revised skill/config admission
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-extension-load
        note: Configuration and skill files can be reloaded, but their revision writer and factory admission
          are unresolved.
      - scope: Included alternative offline and external memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-trace-research
        - memory.md#mem-rte-memory-maintenance
        - memory.md#mem-rte-vault-access
        - runtime.md#rt-rte-extension-load
        note: Session-history mirroring, article/repository/code synchronization, research consolidation,
          gap/link and review-queue generation, generated MCP memory, quarantine hygiene, threshold recalibration,
          ingestion delegates and deployed external MCP/QMD memory remain incompletely inspected. Their
          retained outputs, transformations, admission and later consumers cannot be completely classified
          from the accepted records. These are included alternatives, not excluded stores or evidenced
          absences.
      records:
      - memory.md#mem-rte-keyed-memory
      - runtime.md#rt-obj-messages
      - runtime.md#rt-rte-native-turn
      - memory.md#mem-rte-session-memory
      - epistemic.md#epi-rte-self-model-update
      - memory.md#mem-obj-agent-narrative
      - memory.md#mem-obj-self-model
      - memory.md#mem-rte-epoch-synthesis
      - memory.md#mem-obj-epochs
      - memory.md#mem-obj-research-memory
      - memory.md#mem-rte-trace-research
      - memory.md#mem-rte-daily-promotion
      - epistemic.md#epi-rte-memory-promotions
      - memory.md#mem-obj-hybrid-index
      - memory.md#mem-rte-hybrid-retrieval
      - memory.md#mem-rte-memory-maintenance
      - epistemic.md#epi-rte-consolidation-policy
      - epistemic.md#epi-rte-title-renaming
      - memory.md#mem-obj-learning-events
      - memory.md#mem-rte-learning-hints
      - runtime.md#rt-rte-learning-promotion
      - runtime.md#rt-rte-workflow-advance
      - runtime.md#rt-rte-idle-experiment
      - runtime.md#rt-rte-extension-load
      - memory.md#mem-rte-vault-access
      note: Automatic admission is supported on specific routes. No manual value is inferred from apply
        flags, caller identity, role names or manual-gate labels; unresolved initial/replacement and caller-controlled
        mechanisms remain included.
    curation_operations:
      assessment: partial
      units:
      - scope: Keyed-content replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id080
          - memory.md#mem-rte-keyed-memory
          note: Overwriting an existing key revises the retained entry; initial creation alone is not
            curation.
        records: *id080
        note: Overwriting an existing key revises the retained entry; initial creation alone is not curation.
      - scope: Stop recovery summaries
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id081
          - memory.md#mem-obj-handoff-artifact
          - memory.md#mem-rte-session-memory
          note: Selected assistant/transcript material is compressed into durable handoff/episode context;
            lossy extraction remains consolidation.
        records: *id081
        note: Selected assistant/transcript material is compressed into durable handoff/episode context;
          lossy extraction remains consolidation.
      - scope: Self-model heuristic conjecture
        assessment: known
        findings:
        - value: synthesize
          basis: wired
          records: &id082
          - memory.md#mem-obj-self-model
          - epistemic.md#epi-rte-self-model-update
          note: Preference and tests-pass assertions can be absent from/non-entailed by the inputs; this
            specific mechanism adds claims, not just faithful compression.
        records: *id082
        note: Preference and tests-pass assertions can be absent from/non-entailed by the inputs; this
          specific mechanism adds claims, not just faithful compression.
      - scope: Self-model update and capped pattern lists
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id083
          - memory.md#mem-obj-self-model
          - epistemic.md#epi-rte-self-model-update
          note: Existing self-model is revised and bounded arrays forget older entries.
        - value: decay
          basis: wired
          records: *id083
          note: Existing self-model is revised and bounded arrays forget older entries.
        records: *id083
        note: Existing self-model is revised and bounded arrays forget older entries.
      - scope: SMS episode read significance decay
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id084
          - memory.md#mem-obj-episodes
          - memory.md#mem-rte-session-memory
          note: Age-adjusted significance downweights eligibility at read time without rewriting stored
            original scores.
        records: *id084
        note: Age-adjusted significance downweights eligibility at read time without rewriting stored
          original scores.
      - scope: Epoch grouping and copied-decision reduction
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id085
          - memory.md#mem-obj-epochs
          - memory.md#mem-rte-epoch-synthesis
          note: Selection/grouping and first-ten decision copy reduce existing claims, not new semantic
            synthesis despite the command name.
        records: *id085
        note: Selection/grouping and first-ten decision copy reduce existing claims, not new semantic
          synthesis despite the command name.
      - scope: Narrative replacement transformation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-agent-narrative
        note: A whole-file writer exists but no admitting caller/input relation establishes which curation
          operation it performs.
      - scope: Trace signal extraction and title-fallback reduction
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id086
          - memory.md#mem-obj-research-memory
          - memory.md#mem-rte-trace-research
          note: Retained assistant/history content is selected and compressed, sometimes to an 80-character
            H1. Negation/context loss would not itself establish synthesis.
        records: *id086
        note: Retained assistant/history content is selected and compressed, sometimes to an 80-character
          H1. Negation/context loss would not itself establish synthesis.
      - scope: Daily extraction and normalized duplicate suppression
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id087
          - memory.md#mem-rte-daily-promotion
          - epistemic.md#epi-rte-memory-promotions
          note: Highlights/lesson candidates reduce retained histories; normalized repeated lines are
            removed from candidate/admission output. This is not merely a primary-key collision check.
        - value: dedup
          basis: wired
          records: *id087
          note: Highlights/lesson candidates reduce retained histories; normalized repeated lines are
            removed from candidate/admission output. This is not merely a primary-key collision check.
        records: *id087
        note: Highlights/lesson candidates reduce retained histories; normalized repeated lines are removed
          from candidate/admission output. This is not merely a primary-key collision check.
      - scope: Daily candidate to durable memory tier
        assessment: known
        findings:
        - value: promote
          basis: wired
          records: &id088
          - memory.md#mem-rte-daily-promotion
          - epistemic.md#epi-rte-memory-promotions
          note: Apply raises selected daily candidates into durable memory/lessons/tasks/tools files;
            default driver suggestions alone do not perform this promotion.
        records: *id088
        note: Apply raises selected daily candidates into durable memory/lessons/tasks/tools files; default
          driver suggestions alone do not perform this promotion.
      - scope: Research publication selection
        assessment: known
        findings:
        - value: promote
          basis: wired
          records: &id089
          - memory.md#mem-obj-research-memory
          - memory.md#mem-rte-trace-research
          note: Qualifying registry content is raised to published graph visibility, including fallback
            thresholds.
        records: *id089
        note: Qualifying registry content is raised to published graph visibility, including fallback
          thresholds.
      - scope: Optional research semantic merge/prediction-error transformation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-trace-research
        note: Semantic helper bodies are uninspected. Exact hashes alone do not establish semantic dedup,
          contradiction handling or synthesis; the optional branch retains uncertainty.
      - scope: Local status resolution
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records: &id090
          - memory.md#mem-rte-memory-maintenance
          note: Resolve retains body/history while marking status/reason to withdraw local current reliance.
            This does not establish propagation to all collectors or copied indexes.
        records: *id090
        note: Resolve retains body/history while marking status/reason to withdraw local current reliance.
          This does not establish propagation to all collectors or copied indexes.
      - scope: Pruning, archival, handoff expiry and tail deletion
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id091
          - memory.md#mem-rte-memory-maintenance
          - epistemic.md#epi-rte-consolidation-policy
          - memory.md#mem-rte-session-memory
          note: Moving weak/old files, dropping capped tail text and aging handoff eligibility implement
            local forgetting/downweighting; universal revocation and successful driver archival are not
            claimed.
        records: *id091
        note: Moving weak/old files, dropping capped tail text and aging handoff eligibility implement
          local forgetting/downweighting; universal revocation and successful driver archival are not
          claimed.
      - scope: Similarity conflict marker and title renaming
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-memory-maintenance
        - epistemic.md#epi-rte-consolidation-policy
        - epistemic.md#epi-rte-title-renaming
        note: Renaming is address maintenance, not synthesis; supersedes mutation lacks established registry
          serialization. These operations do not establish durable semantic merging/evolution or withdrawal
          of a loser.
      - scope: Promotion rollback of active reliance state
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records: &id092
          - runtime.md#rt-rte-learning-promotion
          note: 'Rollback removes active promotion while preserving event/receipt history: local withdrawal,
            not erasure or retraction of every delivered hint.'
        records: *id092
        note: 'Rollback removes active promotion while preserving event/receipt history: local withdrawal,
          not erasure or retraction of every delivered hint.'
      - scope: Improvement source revision
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id093
          - runtime.md#rt-rte-idle-experiment
          - runtime.md#rt-bap-autoresearch-code
          note: The delegated experiment revises retained source organization; numeric selection does
            not establish explanatory synthesis or criticism.
        records: *id093
        note: The delegated experiment revises retained source organization; numeric selection does not
          establish explanatory synthesis or criticism.
      - scope: Included alternative offline and external memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-trace-research
        - memory.md#mem-rte-memory-maintenance
        - memory.md#mem-rte-vault-access
        - runtime.md#rt-rte-extension-load
        note: Session-history mirroring, article/repository/code synchronization, research consolidation,
          gap/link and review-queue generation, generated MCP memory, quarantine hygiene, threshold recalibration,
          ingestion delegates and deployed external MCP/QMD memory remain incompletely inspected. Their
          retained outputs, transformations, admission and later consumers cannot be completely classified
          from the accepted records. These are included alternatives, not excluded stores or evidenced
          absences.
      records:
      - memory.md#mem-rte-keyed-memory
      - memory.md#mem-obj-handoff-artifact
      - memory.md#mem-rte-session-memory
      - memory.md#mem-obj-self-model
      - epistemic.md#epi-rte-self-model-update
      - memory.md#mem-obj-episodes
      - memory.md#mem-obj-epochs
      - memory.md#mem-rte-epoch-synthesis
      - memory.md#mem-obj-agent-narrative
      - memory.md#mem-obj-research-memory
      - memory.md#mem-rte-trace-research
      - memory.md#mem-rte-daily-promotion
      - epistemic.md#epi-rte-memory-promotions
      - memory.md#mem-rte-memory-maintenance
      - epistemic.md#epi-rte-consolidation-policy
      - epistemic.md#epi-rte-title-renaming
      - runtime.md#rt-rte-learning-promotion
      - runtime.md#rt-rte-idle-experiment
      - runtime.md#rt-bap-autoresearch-code
      - memory.md#mem-rte-vault-access
      - runtime.md#rt-rte-extension-load
      note: All seven controlled operation values have local supported transformations, not a complete
        system enumeration. Semantic-helper, narrative and other offline operations remain unresolved;
        index rebuilding alone adds no curation value.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested native key/read/search/list
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id094
          - memory.md#mem-rte-keyed-memory
          note: Foreground consumer explicitly asks for retained material; returning the result is pull,
            not an additional push.
        records: *id094
        note: Foreground consumer explicitly asks for retained material; returning the result is pull,
          not an additional push.
      - scope: Explicit native conversation resume
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id095
          - runtime.md#rt-rte-native-turn
          - runtime.md#rt-obj-messages
          note: Startup resume or /resume reloads the selected saved conversation at the consumer request.
            No automatic unrelated memory injection is inferred.
        records: *id095
        note: Startup resume or /resume reloads the selected saved conversation at the consumer request.
          No automatic unrelated memory injection is inferred.
      - scope: Host-event recovery and SMS supply
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id096
          - memory.md#mem-rte-session-memory
          - memory.md#mem-obj-handoff-artifact
          - memory.md#mem-obj-episodes
          - memory.md#mem-obj-self-model
          - memory.md#mem-obj-agent-narrative
          note: Startup/clear/compact automatically selects eligible retained parts and supplies systemMessage
            without a content request from the receiving host.
        records: *id096
        note: Startup/clear/compact automatically selects eligible retained parts and supplies systemMessage
          without a content request from the receiving host.
      - scope: Explicit SMS/handoff/epoch/vault display
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id097
          - memory.md#mem-rte-session-memory
          - memory.md#mem-rte-epoch-synthesis
          - memory.md#mem-rte-vault-access
          note: CLI caller requests retained records or search results; display is pull even when software
            selects matching results.
        records: *id097
        note: CLI caller requests retained records or search results; display is pull even when software
          selects matching results.
      - scope: Requested hybrid query and evaluator loads
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id098
          - memory.md#mem-rte-hybrid-retrieval
          - epistemic.md#epi-rte-retrieval-ranking
          note: CLI/probe/benchmark requests load retained payload and return selected chunks. Incoming
            read-only consumption counts despite no persisted new query output.
        records: *id098
        note: CLI/probe/benchmark requests load retained payload and return selected chunks. Incoming
          read-only consumption counts despite no persisted new query output.
      - scope: Research sync, daily suggestions and maintenance input reload
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id099
          - memory.md#mem-rte-trace-research
          - memory.md#mem-rte-daily-promotion
          - memory.md#mem-rte-memory-maintenance
          note: Invoked processing consumers explicitly load their retained registry/daily/probe inputs;
            later foreground delivery is not automatically wired by this fact.
        records: *id099
        note: Invoked processing consumers explicitly load their retained registry/daily/probe inputs;
          later foreground delivery is not automatically wired by this fact.
      - scope: Cross-CLI query and evaluation
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id100
          - memory.md#mem-rte-learning-hints
          - epistemic.md#epi-rte-learning-metrics
          note: Requested advisory retrieval and evaluator reload consume retained events. Neither establishes
            unsolicited foreground hint injection.
        records: *id100
        note: Requested advisory retrieval and evaluator reload consume retained events. Neither establishes
          unsolicited foreground hint injection.
      - scope: Workflow and promotion reload
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id101
          - runtime.md#rt-rte-workflow-advance
          - runtime.md#rt-rte-learning-promotion
          note: Advance/status/re-promotion/rollback requests consult persisted state and controls.
        records: *id101
        note: Advance/status/re-promotion/rollback requests consult persisted state and controls.
      - scope: Improvement history and source reload
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id102
          - runtime.md#rt-rte-idle-experiment
          - runtime.md#rt-bap-autoresearch-code
          note: Experiment setup reads saved history; subsequent process import loads retained source.
            Static program loading alone is outside accumulated memory.
        records: *id102
        note: Experiment setup reads saved history; subsequent process import loads retained source. Static
          program loading alone is outside accumulated memory.
      - scope: Revised installed skill/config and external-host checkpoint delivery
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-extension-load
        - runtime.md#rt-rte-host-launch
        note: On-demand skill loading is known but whether a revised through-use artifact reaches a later
          invocation, and how opaque host checkpoints are supplied, remain unresolved.
      - scope: Included alternative offline and external memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-trace-research
        - memory.md#mem-rte-memory-maintenance
        - memory.md#mem-rte-vault-access
        - runtime.md#rt-rte-extension-load
        note: Session-history mirroring, article/repository/code synchronization, research consolidation,
          gap/link and review-queue generation, generated MCP memory, quarantine hygiene, threshold recalibration,
          ingestion delegates and deployed external MCP/QMD memory remain incompletely inspected. Their
          retained outputs, transformations, admission and later consumers cannot be completely classified
          from the accepted records. These are included alternatives, not excluded stores or evidenced
          absences.
      records:
      - memory.md#mem-rte-keyed-memory
      - runtime.md#rt-rte-native-turn
      - runtime.md#rt-obj-messages
      - memory.md#mem-rte-session-memory
      - memory.md#mem-obj-handoff-artifact
      - memory.md#mem-obj-episodes
      - memory.md#mem-obj-self-model
      - memory.md#mem-obj-agent-narrative
      - memory.md#mem-rte-epoch-synthesis
      - memory.md#mem-rte-vault-access
      - memory.md#mem-rte-hybrid-retrieval
      - epistemic.md#epi-rte-retrieval-ranking
      - memory.md#mem-rte-trace-research
      - memory.md#mem-rte-daily-promotion
      - memory.md#mem-rte-memory-maintenance
      - memory.md#mem-rte-learning-hints
      - epistemic.md#epi-rte-learning-metrics
      - runtime.md#rt-rte-workflow-advance
      - runtime.md#rt-rte-learning-promotion
      - runtime.md#rt-rte-idle-experiment
      - runtime.md#rt-bap-autoresearch-code
      - runtime.md#rt-rte-extension-load
      - runtime.md#rt-rte-host-launch
      note: Both requested reloads and unsolicited host recovery delivery exist. Query return is not push
        merely because a selector ranks results; unknown external/offline delivery alternatives prevent
        complete direction coverage.
    read_back_signal:
      assessment: partial
      units:
      - scope: 'Host handoff push: cwd identity match'
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id103
          - memory.md#mem-obj-handoff-artifact
          - memory.md#mem-rte-session-memory
          note: Trigger is host startup/clear/compact. Selector hashes current cwd and reads its matching
            latest handoff; the matched retained handoff supplies recovery text. This actual match, not
            merely a printed ID, establishes identifier selection.
        records: *id103
        note: Trigger is host startup/clear/compact. Selector hashes current cwd and reads its matching
          latest handoff; the matched retained handoff supplies recovery text. This actual match, not
          merely a printed ID, establishes identifier selection.
      - scope: 'Host handoff push: age and priority budget'
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id104
          - memory.md#mem-obj-handoff-artifact
          - memory.md#mem-rte-session-memory
          note: Same event uses under-24h availability and priority/budget inclusion for the selected
            handoff. Coarse filtering remains distinct from its cwd identity match.
        records: *id104
        note: Same event uses under-24h availability and priority/budget inclusion for the selected handoff.
          Coarse filtering remains distinct from its cwd identity match.
      - scope: SMS arc push
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id105
          - memory.md#mem-obj-agent-narrative
          - memory.md#mem-rte-session-memory
          note: Host event selects nonempty current_arc and truncates to 200 characters; selection is
            availability/length, not inferred goal relevance.
        records: *id105
        note: Host event selects nonempty current_arc and truncates to 200 characters; selection is availability/length,
          not inferred goal relevance.
      - scope: SMS self-model push
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id106
          - memory.md#mem-obj-self-model
          - memory.md#mem-rte-session-memory
          note: Host event uses confidence >0.4 and fixed field/list slices to supply preferences, biases
            and failures; no semantic or identifier-based project targeting is established.
        records: *id106
        note: Host event uses confidence >0.4 and fixed field/list slices to supply preferences, biases
          and failures; no semantic or identifier-based project targeting is established.
      - scope: SMS episode push
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id107
          - memory.md#mem-obj-episodes
          - memory.md#mem-rte-session-memory
          note: Host event supplies last three episodes from seven-day, decayed-significance>=0.6 selection,
            then priority budget. Agent/project arguments are not applied as identity filters.
        records: *id107
        note: Host event supplies last three episodes from seven-day, decayed-significance>=0.6 selection,
          then priority budget. Agent/project arguments are not applied as identity filters.
      - scope: Inspected explicit pull-only query/display/control routes
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-keyed-memory
        - runtime.md#rt-rte-native-turn
        - memory.md#mem-rte-epoch-synthesis
        - memory.md#mem-rte-vault-access
        - memory.md#mem-rte-hybrid-retrieval
        - memory.md#mem-rte-learning-hints
        - epistemic.md#epi-rte-learning-metrics
        - runtime.md#rt-rte-workflow-advance
        - runtime.md#rt-rte-learning-promotion
        note: These particular consumers request retained data; push-signal classification is inapplicable
          locally. Lexical/dense ranking on requested hybrid queries is not a push signal.
      - scope: Unresolved external-host checkpoint and revised-extension push
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-host-launch
        - runtime.md#rt-rte-extension-load
        note: Known pull routes do not establish the signal of opaque or unresolved alternatives.
      - scope: Included alternative offline and external memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-trace-research
        - memory.md#mem-rte-memory-maintenance
        - memory.md#mem-rte-vault-access
        - runtime.md#rt-rte-extension-load
        note: Session-history mirroring, article/repository/code synchronization, research consolidation,
          gap/link and review-queue generation, generated MCP memory, quarantine hygiene, threshold recalibration,
          ingestion delegates and deployed external MCP/QMD memory remain incompletely inspected. Their
          retained outputs, transformations, admission and later consumers cannot be completely classified
          from the accepted records. These are included alternatives, not excluded stores or evidenced
          absences.
      records:
      - memory.md#mem-obj-handoff-artifact
      - memory.md#mem-rte-session-memory
      - memory.md#mem-obj-agent-narrative
      - memory.md#mem-obj-self-model
      - memory.md#mem-obj-episodes
      - memory.md#mem-rte-keyed-memory
      - runtime.md#rt-rte-native-turn
      - memory.md#mem-rte-epoch-synthesis
      - memory.md#mem-rte-vault-access
      - memory.md#mem-rte-hybrid-retrieval
      - memory.md#mem-rte-learning-hints
      - epistemic.md#epi-rte-learning-metrics
      - runtime.md#rt-rte-workflow-advance
      - runtime.md#rt-rte-learning-promotion
      - runtime.md#rt-rte-host-launch
      - runtime.md#rt-rte-extension-load
      - memory.md#mem-rte-trace-research
      - memory.md#mem-rte-memory-maintenance
      note: Known automatic host supply uses identity plus coarse gates. Hybrid lexical/embedding query
        ranking is retained under authority, not misclassified as an unsolicited push signal; other push
        alternatives remain unresolved.
    trace_learning:
      assessment: partial
      units:
      - scope: Stop-derived recovery handoff to subsequent host
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id108
          - memory.md#mem-obj-handoff-artifact
          - memory.md#mem-rte-session-memory
          note: Automatic capture compresses session activity into durable recovery text subsequently
            supplied as host context. It qualifies without new knowledge or observed improvement.
        records: *id108
        note: Automatic capture compresses session activity into durable recovery text subsequently supplied
          as host context. It qualifies without new knowledge or observed improvement.
      - scope: SMS episode capture to later host context
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id109
          - memory.md#mem-obj-episodes
          - memory.md#mem-rte-session-memory
          note: Automatic trace-fed summary capture persists episodes and later host-event selection delivers
            them as context.
        records: *id109
        note: Automatic trace-fed summary capture persists episodes and later host-event selection delivers
          them as context.
      - scope: SMS self-model update to selected later guidance
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id110
          - memory.md#mem-obj-self-model
          - epistemic.md#epi-rte-self-model-update
          - memory.md#mem-rte-session-memory
          note: Recorded summary/outcome signals automatically revise durable preference/failure fields
            consumed in later host guidance. Count-based confidence is not a truth warrant.
        records: *id110
        note: Recorded summary/outcome signals automatically revise durable preference/failure fields
          consumed in later host guidance. Count-based confidence is not a truth warrant.
      - scope: Assistant/history-to-research-to-index-to-caller
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id111
          - memory.md#mem-rte-trace-research
          - memory.md#mem-obj-research-memory
          - memory.md#mem-rte-hybrid-retrieval
          note: Implemented extraction/admission yields durable graph/reference material with later query
            consumers. Hook registration/activation remains unresolved, while the implemented qualifying
            chain remains wired.
        records: *id111
        note: Implemented extraction/admission yields durable graph/reference material with later query
          consumers. Hook registration/activation remains unresolved, while the implemented qualifying
          chain remains wired.
      - scope: Daily trace extraction and optional durable promotion
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id112
          - memory.md#mem-rte-daily-promotion
          - epistemic.md#epi-rte-memory-promotions
          - memory.md#mem-rte-hybrid-retrieval
          note: Automatic extraction and enabled software append produce durable context/reference artifacts
            reachable by later suggestion/sync/index consumers; the default pipeline does not enable append.
        records: *id112
        note: Automatic extraction and enabled software append produce durable context/reference artifacts
          reachable by later suggestion/sync/index consumers; the default pipeline does not enable append.
      - scope: Epoch grouping to CLI display
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-epochs
        - memory.md#mem-rte-epoch-synthesis
        note: Automatic trace-derived grouping and persistent display are established; behavior-shaping
          guidance beyond display is not established. Do not transfer the episode host consumer to epochs.
      - scope: Narrative initial/replacement route
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-agent-narrative
        note: Startup arc consumption is known, but a trace-fed automatic admission path is not; the epoch
          writer does not establish one.
      - scope: Keyed entries and initial self-model content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-entries
        - memory.md#mem-rte-keyed-memory
        - memory.md#mem-obj-self-model
        note: Model/caller admission can be automatic, but supplied arbitrary text/initial fields lack
          a demonstrated original trace input and qualifying derivation chain.
      - scope: Raw native conversation retention
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-messages
        - runtime.md#rt-rte-native-turn
        note: Raw save/resume is not by itself a demonstrated trace-derived behavior-shaping update; these
          records do not establish an exhaustive bounded absence of all qualifying native updates.
      - scope: Cross-CLI events and promotion
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-learning-events
        - memory.md#mem-rte-learning-hints
        - epistemic.md#epi-rte-learning-metrics
        - runtime.md#rt-rte-learning-promotion
        note: Captured summaries/outcomes and later hints/evaluation are established, but generic caller
          identity leaves automatic trace-fed content admission unresolved. Mode promotion is not by itself
          a content-learning route.
      - scope: Idle source changes and count history
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-idle-experiment
        - runtime.md#rt-bap-autoresearch-code
        note: Score-selected source revision and recurrence are wired, but retained logs/scores are not
          systematically fed into guidance content; original qualifying trace input to edits is not established.
      - scope: External host checkpoint generation
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-host-launch
        note: Host compaction/summary implementation is opaque; local adapter returns do not establish
          trace-fed durable checkpoint generation.
      - scope: Included alternative offline and external memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-trace-research
        - memory.md#mem-rte-memory-maintenance
        - memory.md#mem-rte-vault-access
        - runtime.md#rt-rte-extension-load
        note: Session-history mirroring, article/repository/code synchronization, research consolidation,
          gap/link and review-queue generation, generated MCP memory, quarantine hygiene, threshold recalibration,
          ingestion delegates and deployed external MCP/QMD memory remain incompletely inspected. Their
          retained outputs, transformations, admission and later consumers cannot be completely classified
          from the accepted records. These are included alternatives, not excluded stores or evidenced
          absences.
      records:
      - memory.md#mem-obj-handoff-artifact
      - memory.md#mem-rte-session-memory
      - memory.md#mem-obj-episodes
      - memory.md#mem-obj-self-model
      - epistemic.md#epi-rte-self-model-update
      - memory.md#mem-rte-trace-research
      - memory.md#mem-obj-research-memory
      - memory.md#mem-rte-hybrid-retrieval
      - memory.md#mem-rte-daily-promotion
      - epistemic.md#epi-rte-memory-promotions
      - memory.md#mem-obj-epochs
      - memory.md#mem-rte-epoch-synthesis
      - memory.md#mem-obj-agent-narrative
      - memory.md#mem-obj-memory-entries
      - memory.md#mem-rte-keyed-memory
      - runtime.md#rt-obj-messages
      - runtime.md#rt-rte-native-turn
      - memory.md#mem-obj-learning-events
      - memory.md#mem-rte-learning-hints
      - epistemic.md#epi-rte-learning-metrics
      - runtime.md#rt-rte-learning-promotion
      - runtime.md#rt-rte-idle-experiment
      - runtime.md#rt-bap-autoresearch-code
      - runtime.md#rt-rte-host-launch
      - memory.md#mem-rte-memory-maintenance
      - memory.md#mem-rte-vault-access
      - runtime.md#rt-rte-extension-load
      note: Positive wired trace-fed routes coexist with unresolved admissions, raw-log-only routes and
        opaque alternatives. No global no, observed improvement or parameter training is inferred; no
        local no is invented without bounded absence records.
    trace_source:
      assessment: partial
      units:
      - scope: Handoff summary and transcript-derived content
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id113
          - memory.md#mem-obj-handoff-artifact
          - memory.md#mem-rte-session-memory
          note: Original assistant turns and transcript context are recorded conversational session content,
            not event-streams merely because a Stop hook triggers capture.
        records: *id113
        note: Original assistant turns and transcript context are recorded conversational session content,
          not event-streams merely because a Stop hook triggers capture.
      - scope: Handoff tool/file/test inputs
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id114
          - memory.md#mem-obj-handoff-artifact
          - memory.md#mem-rte-session-memory
          note: Transcript tool/file activity and recorded evaluation checkpoint feedback feed recovery
            metadata; this is tool execution feedback, not proof a fresh test passed.
        records: *id114
        note: Transcript tool/file activity and recorded evaluation checkpoint feedback feed recovery
          metadata; this is tool execution feedback, not proof a fresh test passed.
      - scope: SMS episode textual summary
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id115
          - memory.md#mem-obj-episodes
          - memory.md#mem-rte-session-memory
          note: The Stop producer extracts the last assistant text from an agent work session. Hook transport
            alone does not add event-stream lineage.
        records: *id115
        note: The Stop producer extracts the last assistant text from an agent work session. Hook transport
          alone does not add event-stream lineage.
      - scope: SMS self-model summary-keyword input
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id116
          - memory.md#mem-obj-self-model
          - epistemic.md#epi-rte-self-model-update
          - memory.md#mem-rte-session-memory
          note: Recorded session summary text feeds preference/pattern heuristics.
        records: *id116
        note: Recorded session summary text feeds preference/pattern heuristics.
      - scope: SMS self-model file/test-outcome input
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id117
          - memory.md#mem-obj-self-model
          - epistemic.md#epi-rte-self-model-update
          - memory.md#mem-rte-session-memory
          note: Changed-file and stored test-failure signals are execution feedback used by the update.
            They may be stale and do not entail session success.
        records: *id117
        note: Changed-file and stored test-failure signals are execution feedback used by the update.
          They may be stale and do not entail session success.
      - scope: Assistant and daily-history research extraction
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id118
          - memory.md#mem-rte-trace-research
          - memory.md#mem-obj-research-memory
          note: Assistant last-message and historical conversational signals are original session-log
            inputs, even when serialized as staging events.
        records: *id118
        note: Assistant last-message and historical conversational signals are original session-log inputs,
          even when serialized as staging events.
      - scope: Mixed research inbox and partially inspected helper input
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-research-memory
        - memory.md#mem-rte-trace-research
        note: Alternative external inbox notes and uninspected semantic helpers prevent complete qualifying
          trace-origin coverage; static imported research alone establishes no trace source.
      - scope: Daily prompt-history extraction
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id119
          - memory.md#mem-rte-daily-promotion
          - epistemic.md#epi-rte-memory-promotions
          note: Original prompt highlights, including user turns, are session-log sources; a lessons label
            does not prove an experienced lesson.
        records: *id119
        note: Original prompt highlights, including user turns, are session-log sources; a lessons label
          does not prove an experienced lesson.
      - scope: Daily Codex execution summary inputs
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id120
          - memory.md#mem-rte-daily-promotion
          note: Tool/command counts derive from recorded execution activity; exact original history parsing/redaction
            is incompletely inspected.
        records: *id120
        note: Tool/command counts derive from recorded execution activity; exact original history parsing/redaction
          is incompletely inspected.
      - scope: Narrative and epoch qualifying update source
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-agent-narrative
        - memory.md#mem-obj-epochs
        - memory.md#mem-rte-epoch-synthesis
        note: Narrative origin/admission is unresolved; epoch episode provenance is known in part but
          a qualifying behavior-shaping later consumer is unresolved. Neither can be declared globally
          inapplicable.
      - scope: Other unresolved qualifying trace-fed routes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-entries
        - memory.md#mem-rte-keyed-memory
        - memory.md#mem-obj-learning-events
        - memory.md#mem-rte-learning-hints
        - runtime.md#rt-rte-idle-experiment
        - runtime.md#rt-rte-host-launch
        - runtime.md#rt-rte-native-turn
        note: Keyed/caller event admissions, opaque external checkpoints, raw native persistence and improvement-edit
          input lack enough facts to classify every qualifying original source. Automatic persistence
          or event labels alone do not supply them.
      - scope: Included alternative offline and external memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-trace-research
        - memory.md#mem-rte-memory-maintenance
        - memory.md#mem-rte-vault-access
        - runtime.md#rt-rte-extension-load
        note: Session-history mirroring, article/repository/code synchronization, research consolidation,
          gap/link and review-queue generation, generated MCP memory, quarantine hygiene, threshold recalibration,
          ingestion delegates and deployed external MCP/QMD memory remain incompletely inspected. Their
          retained outputs, transformations, admission and later consumers cannot be completely classified
          from the accepted records. These are included alternatives, not excluded stores or evidenced
          absences.
      records:
      - memory.md#mem-obj-handoff-artifact
      - memory.md#mem-rte-session-memory
      - memory.md#mem-obj-episodes
      - memory.md#mem-obj-self-model
      - epistemic.md#epi-rte-self-model-update
      - memory.md#mem-rte-trace-research
      - memory.md#mem-obj-research-memory
      - memory.md#mem-rte-daily-promotion
      - epistemic.md#epi-rte-memory-promotions
      - memory.md#mem-obj-agent-narrative
      - memory.md#mem-obj-epochs
      - memory.md#mem-rte-epoch-synthesis
      - memory.md#mem-obj-memory-entries
      - memory.md#mem-rte-keyed-memory
      - memory.md#mem-obj-learning-events
      - memory.md#mem-rte-learning-hints
      - runtime.md#rt-rte-idle-experiment
      - runtime.md#rt-rte-host-launch
      - runtime.md#rt-rte-native-turn
      - memory.md#mem-rte-memory-maintenance
      - memory.md#mem-rte-vault-access
      - runtime.md#rt-rte-extension-load
      note: Session-log and tool-trace sources are supported at named qualifying writes. Hook event names
        do not establish event-stream sources, and no linked states/actions/outcomes warrant trajectories.
        Unresolved trace learning keeps corresponding source units unresolved, not inapplicable.
---

# LACP memory profile

## Comparison rationale

This comparison classifies implementation-supported memory routes, not observed use or benefit. All ten axes remain partial because the accepted inventory includes uninspected offline responsibilities, unknown initial admissions and external-host alternatives. A known file or consumer does not settle a different part's derivation, admission or authority. The units preserve that separation rather than presenting a complete system value set.

### Operative parts and coverage

Native entries and saved conversations are distinct stores. JSON envelopes do not turn interpreted content into symbolic knowledge, and keyed filenames do not imply a KV service. Research Markdown has graph links; the hybrid index has copied chunks and vector access structures. Neither establishes a dedicated graph/vector database. Dense representations are parametric form, not evidence of weight training. Full indexed text, not its short display preview, determines the content classification ([MEM-OBJ-memory-entries](memory.md#mem-obj-memory-entries), [RT-OBJ-messages](runtime.md#rt-obj-messages), [MEM-OBJ-research-memory](memory.md#mem-obj-research-memory), [MEM-OBJ-hybrid-index](memory.md#mem-obj-hybrid-index)).

The narrative and epochs retain separate units. Narrative has a known file, form and startup arc reader but unresolved initial admission. Epochs have automatic selection/copying and a later CLI display; this does not establish narrative generation or startup epoch consumption. Their valid shared container needs no supersession ([MEM-OBJ-agent-narrative](memory.md#mem-obj-agent-narrative), [MEM-OBJ-epochs](memory.md#mem-obj-epochs), [MEM-RTE-epoch-synthesis](memory.md#mem-rte-epoch-synthesis)).

Reconciliation makes one identity amendment: the epistemic self-model object is superseded by [MEM-OBJ-self-model](memory.md#mem-obj-self-model). This profile cites that canonical object. The distinct [EPI-RTE-self-model-update](epistemic.md#epi-rte-self-model-update) remains its update-route witness; the amendment upgrades no status or authority. Other overlaps are connected stages/parts, not duplicate whole routes. In particular, query ranking and learning evaluation consume retained input even without persisting new output ([MEM-RTE-hybrid-retrieval](memory.md#mem-rte-hybrid-retrieval), [EPI-RTE-retrieval-ranking](epistemic.md#epi-rte-retrieval-ranking), [EPI-RTE-learning-metrics](epistemic.md#epi-rte-learning-metrics)).

### Admission and transformation

Automatic admission is software/model selection without a per-content human decision. Enabling an apply workflow is not approving each bullet, pattern or rename. Conversely, generic callers, role strings and manual-labelled gates do not establish human decisions. Unknown narrative initialization and separately supplied checkpoint/content replacement cannot inherit automatic agency from an unrelated derived update ([MEM-RTE-keyed-memory](memory.md#mem-rte-keyed-memory), [MEM-RTE-daily-promotion](memory.md#mem-rte-daily-promotion), [MEM-RTE-memory-maintenance](memory.md#mem-rte-memory-maintenance), [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion), [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance)).

Curation follows the transformation. Handoff/extraction/epoch copying consolidates existing content. SMS preference and tests-pass labels can introduce non-entailed assertions, supporting synthesis only on that specific update. Normalized duplicate-line filtering is distinct from mere hash collision checking. Optional semantic helpers remain uninspected. Resolution and rollback withdraw local reliance, not every copied index or hint; file moves and truncation forget locally. Similarity-based supersedes changes lack established registry persistence, so they do not support durable semantic deduplication or universal invalidation. Title renaming and index rebuild alone establish no curation value ([MEM-RTE-trace-research](memory.md#mem-rte-trace-research), [EPI-RTE-memory-promotions](epistemic.md#epi-rte-memory-promotions), [EPI-RTE-self-model-update](epistemic.md#epi-rte-self-model-update), [EPI-RTE-consolidation-policy](epistemic.md#epi-rte-consolidation-policy), [MEM-RTE-memory-maintenance](memory.md#mem-rte-memory-maintenance)).

### Consumers and trace-fed updates

Authority is assessed where retained parts are consumed. Text can supply knowledge/context or standing preference instructions. The same retained text/features can separately affect ranking. Blocked research IDs validate admission and enforce exclusion. Workflow tokens constrain later transitions, not software correctness. Promotion state controls re-promotion/rollback, not an established host enforcement route. Changed source can execute later, but executable force alone does not specify which controlled effect any arbitrary edit has ([MEM-BAP-memory-text](memory.md#mem-bap-memory-text), [MEM-RTE-trace-research](memory.md#mem-rte-trace-research), [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance), [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion), [RT-BAP-autoresearch-code](runtime.md#rt-bap-autoresearch-code)).

Host recovery is push. The cwd hash actually selects the delivered handoff, establishing identifier selection; recency, significance, fixed field slices and priority budget establish separate coarse selection. SMS agent/project arguments do not establish identity filtering. Explicit native reads, CLI search, hybrid ranking, metric evaluation and status reloads are pull. Dense/lexical scoring of a requested query does not establish a push signal, nor does delivery of the requested result create a second push ([MEM-RTE-session-memory](memory.md#mem-rte-session-memory), [MEM-RTE-keyed-memory](memory.md#mem-rte-keyed-memory), [MEM-RTE-hybrid-retrieval](memory.md#mem-rte-hybrid-retrieval), [MEM-RTE-learning-hints](memory.md#mem-rte-learning-hints)).

Automatic trace-derived handoffs, episodes and selected self-model guidance qualify as trace learning through durable artifacts and later context delivery; improved task capacity need not be shown. Their original inputs include conversational turns and recorded execution feedback. A Stop callback is a trigger, not evidence that the extracted assistant text originated as an event stream. Daily/history-to-research chains retain session-log and tool-trace positives while preserving mixed external inbox inputs and incompletely inspected history parsing. Raw transcript persistence, generic event capture and an opaque narrative writer do not by themselves establish qualifying trace-fed updates. Epoch display is not silently assigned the episode's host guidance consumer ([MEM-RTE-session-memory](memory.md#mem-rte-session-memory), [EPI-RTE-self-model-update](epistemic.md#epi-rte-self-model-update), [MEM-RTE-daily-promotion](memory.md#mem-rte-daily-promotion), [MEM-RTE-trace-research](memory.md#mem-rte-trace-research), [MEM-RTE-epoch-synthesis](memory.md#mem-rte-epoch-synthesis)).

The unresolved inventory is retained on every axis rather than erased to obtain known coverage. It includes partially inspected offline mirrors, ingestion/synthesis/review and maintenance branches, external MCP/QMD paths, unknown narrative/initial-content control and opaque host checkpoint internals. Missing facts prevent complete unions and complete-value statistics, not the local positives. No new bounded absence is inferred from selective inspection ([MEM-RTE-memory-maintenance](memory.md#mem-rte-memory-maintenance), [MEM-RTE-vault-access](memory.md#mem-rte-vault-access), [RT-RTE-extension-load](runtime.md#rt-rte-extension-load), [RT-RTE-host-launch](runtime.md#rt-rte-host-launch)).

### Source-read log

No source files were read for this profile. Classification uses only the supplied accepted records, their supplied annotations and reconciliation. No named record ambiguity required an additional frozen-source read. No new evidence, record declaration or execution result is added.
