---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "ACE memory comparison: retained playbook advice, counters, selected snapshots and audit artifacts, with unresolved initialization and provider retention."
run-id: "AAS-2026-10-18-ace-007571102a54-01"
source-identity: "https://github.com/ace-agent/ace"
reviewed-boundary: "82709de050e1db6e6ef2f07bcb0393560b94992a"
memory-comparison:
  version: 2
  scope: "Main-repository ACE and ACEBatch retained playbook advice and IDs/counters; current, intermediate, final, window and selected-best text snapshots; call/usage audit artifacts; their admission, maintenance, reload and later-consumer routes; unresolved initial/replacement provenance and provider-side retention alternatives. Excludes unavailable AppWorld implementation, shipped static role prompts, model weights not updated by ACE, and transient reflection/proposal/embedding frames as independent retained stores; those intermediates remain relevant to the retained-output routes."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Current playbook advice and symbolic metadata, including the selected best snapshot"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-playbook-content"
                - "memory.md#mem-obj-bullet-metadata"
                - "memory.md#mem-obj-best-playbook"
              note: "Operative text and counters are retained as Python strings across model invocations."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-playbook-content"
                - "memory.md#mem-obj-bullet-metadata"
                - "memory.md#mem-obj-best-playbook"
                - "runtime.md#rt-rte-playbook-reload"
              note: "Intermediate, epoch, window, final and best text files retain playbooks for explicit later reload."
          records:
            - "memory.md#mem-obj-playbook-content"
            - "memory.md#mem-obj-bullet-metadata"
            - "memory.md#mem-obj-best-playbook"
            - "runtime.md#rt-rte-playbook-reload"
          note: "Covers the recorded runtime and file forms of both current and selected text; the encoding does not imply a database."
        - scope: "Retained call JSON and usage JSONL audit artifacts"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-call-logs"
              note: "Logger writes filesystem artifacts, separate from derived advice."
          records:
            - "memory.md#mem-obj-call-logs"
          note: "File retention is known even though no historical automatic reader is established."
        - scope: "Included but unresolved provider-side retention behind the generator, reflector and curator APIs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-generator"
            - "runtime.md#rt-cmp-reflector"
            - "runtime.md#rt-cmp-curator"
          note: "The accepted component and memory records do not expose provider retention, admission or later consumption. No storage substrate value is established for that alternative; configured model weights are not themselves ACE memory accumulated through use."
      records:
        - "memory.md#mem-obj-playbook-content"
        - "memory.md#mem-obj-bullet-metadata"
        - "memory.md#mem-obj-best-playbook"
        - "runtime.md#rt-rte-playbook-reload"
        - "memory.md#mem-obj-call-logs"
        - "runtime.md#rt-cmp-generator"
        - "runtime.md#rt-cmp-reflector"
        - "runtime.md#rt-cmp-curator"
      note: "Main-repository playbook and audit-log storage is classified. Provider-side retention remains unresolved; temporary analyzer arrays and proposal frames are not additional retained stores."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Playbook advice at generator and curator/reducer consumers, including best-snapshot advice"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-playbook-content"
                - "memory.md#mem-obj-best-playbook"
                - "runtime.md#rt-bap-playbook-guidance"
              note: "Advice, formulas and snippets are interpreted as prompt content, not executed as a symbolic program."
          records:
            - "memory.md#mem-obj-playbook-content"
            - "memory.md#mem-obj-best-playbook"
            - "runtime.md#rt-bap-playbook-guidance"
          note: "Known encoding/consumption path; this does not establish obedience or truth."
        - scope: "Retained bullet identifiers and helpful/harmful counters at fixed-rule consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-bullet-metadata"
                - "memory.md#mem-rte-counter-update"
              note: "ID matching and integer increments have localized fixed rules; the same fields persist in snapshots."
          records:
            - "memory.md#mem-obj-bullet-metadata"
            - "memory.md#mem-rte-counter-update"
            - "memory.md#mem-obj-best-playbook"
          note: "Split from advice despite sharing the same physical strings."
        - scope: "Call-log prompt/response and shortened textual display parts"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-call-logs"
              note: "Prompts, responses and textual displays retain language content."
          records:
            - "memory.md#mem-obj-call-logs"
          note: "Classifies stored textual parts, not an automatic historical consumer."
        - scope: "Call-log IDs, correctness, timing and usage fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-call-logs"
              note: "Structured JSON/JSONL fields encode operational metadata."
          records:
            - "memory.md#mem-obj-call-logs"
          note: "Separate fields from the textual log body."
        - scope: "Included but unresolved provider-side retention behind the generator, reflector and curator APIs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-generator"
            - "runtime.md#rt-cmp-reflector"
            - "runtime.md#rt-cmp-curator"
          note: "The accepted component and memory records do not expose provider retention, admission or later consumption. No representational form value is established for that alternative; configured model weights are not themselves ACE memory accumulated through use."
      records:
        - "memory.md#mem-obj-playbook-content"
        - "memory.md#mem-obj-best-playbook"
        - "runtime.md#rt-bap-playbook-guidance"
        - "memory.md#mem-obj-bullet-metadata"
        - "memory.md#mem-rte-counter-update"
        - "memory.md#mem-obj-call-logs"
        - "runtime.md#rt-cmp-generator"
        - "runtime.md#rt-cmp-reflector"
        - "runtime.md#rt-cmp-curator"
      note: "Known retained language and symbolic parts coexist. Temporary dense analyzer representations and externally loaded model weights are not persistent memory artifacts in the inspected loop; opaque remote retention cannot be classified from their presence."
    lineage:
      assessment: "partial"
      units:
        - scope: "Installed sequential and batch advice derived from task response and reflection"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-sample-adaptation"
                - "runtime.md#rt-rte-batch-adaptation"
                - "memory.md#mem-obj-playbook-content"
              note: "Generator experience and task feedback feed reflection, proposals and admitted advice for later tasks."
          records:
            - "runtime.md#rt-rte-sample-adaptation"
            - "runtime.md#rt-rte-batch-adaptation"
            - "memory.md#mem-obj-playbook-content"
          note: "Known derivation route does not determine actual lesson semantics or initial-text authorship."
        - scope: "Stored counter increments derived from reflector tags"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-counter-update"
                - "memory.md#mem-obj-bullet-metadata"
              note: "Model judgments over current response/feedback produce retained utility metadata."
          records:
            - "memory.md#mem-rte-counter-update"
            - "memory.md#mem-obj-bullet-metadata"
          note: "Counts record processed tag judgments, not causal utility measurements."
        - scope: "Explicit file-to-playbook acquisition"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-playbook-reload"
                - "memory.md#mem-obj-playbook-content"
              note: "An existing caller-selected text file is acquired whole, without provenance checks."
          records:
            - "runtime.md#rt-rte-playbook-reload"
            - "memory.md#mem-obj-playbook-content"
          note: "Import is established separately from the unknown origin of the file content."
        - scope: "Initial supplied advice and loaded metadata before the known import or update route"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-playbook-content"
            - "memory.md#mem-obj-bullet-metadata"
            - "runtime.md#rt-rte-playbook-reload"
          note: "No initial instance or authorship history is supplied. Authored versus externally derived provenance cannot be determined merely from the loader."
        - scope: "Analyzer replacement/dedup and selected-best snapshot derivation"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bulletpoint-merge"
                - "memory.md#mem-obj-best-playbook"
                - "runtime.md#rt-rte-evaluate-select"
              note: "Maintenance reconstructs retained text from prior bullets; validation selects a whole existing snapshot rather than deriving it from a new trace."
          records:
            - "runtime.md#rt-rte-bulletpoint-merge"
            - "memory.md#mem-obj-best-playbook"
            - "runtime.md#rt-rte-evaluate-select"
          note: "This classifies the recorded downstream derivation, not the unknown original origin of each retained claim."
        - scope: "Call and usage audit artifacts"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-call-logs"
              note: "Recorded model prompts/responses and usage are operational traces, not imported static guidance."
          records:
            - "memory.md#mem-obj-call-logs"
          note: "Their trace origin does not imply a later learning consumer."
        - scope: "Included but unresolved provider-side retention behind the generator, reflector and curator APIs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-generator"
            - "runtime.md#rt-cmp-reflector"
            - "runtime.md#rt-cmp-curator"
          note: "The accepted component and memory records do not expose provider retention, admission or later consumption. No lineage value is established for that alternative; configured model weights are not themselves ACE memory accumulated through use."
      records:
        - "runtime.md#rt-rte-sample-adaptation"
        - "runtime.md#rt-rte-batch-adaptation"
        - "memory.md#mem-obj-playbook-content"
        - "memory.md#mem-rte-counter-update"
        - "memory.md#mem-obj-bullet-metadata"
        - "runtime.md#rt-rte-playbook-reload"
        - "runtime.md#rt-rte-bulletpoint-merge"
        - "memory.md#mem-obj-best-playbook"
        - "runtime.md#rt-rte-evaluate-select"
        - "memory.md#mem-obj-call-logs"
        - "runtime.md#rt-cmp-generator"
        - "runtime.md#rt-cmp-reflector"
        - "runtime.md#rt-cmp-curator"
      note: "Known import, trace extraction and subsequent compilation/selection routes do not settle initial authorship or remote provenance. No authored finding follows from generic caller identity."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Retained playbook advice at subsequent generator invocations"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-playbook-content"
                - "runtime.md#rt-bap-playbook-guidance"
              note: "Strategies supply standing task-solving guidance through the full-playbook prompt slot."
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-playbook-content"
                - "runtime.md#rt-bap-playbook-guidance"
              note: "Formulas and insights also supply reference/advice for answering; interpretation is advisory."
          records:
            - "memory.md#mem-obj-playbook-content"
            - "runtime.md#rt-bap-playbook-guidance"
          note: "Both recorded uses are prompt-mediated; enforced delivery is not enforced obedience."
        - scope: "Current retained playbook at curator/reducer update consumers"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-playbook-content"
                - "runtime.md#rt-rte-sample-adaptation"
                - "runtime.md#rt-rte-batch-adaptation"
              note: "Existing accumulated advice participates in proposing and selecting further durable behavior-shaping advice."
          records:
            - "memory.md#mem-obj-playbook-content"
            - "runtime.md#rt-rte-sample-adaptation"
            - "runtime.md#rt-rte-batch-adaptation"
          note: "Update-consumer force is separate from generator instruction/knowledge. No improved capacity is inferred."
        - scope: "Retained bullet content at optional analyzer similarity grouping"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-playbook-content"
                - "memory.md#mem-obj-analyzer-embeddings"
                - "runtime.md#rt-rte-bulletpoint-merge"
              note: "Encoded retained content determines relative similarity and the groups selected for maintenance."
          records:
            - "memory.md#mem-obj-playbook-content"
            - "memory.md#mem-obj-analyzer-embeddings"
            - "runtime.md#rt-rte-bulletpoint-merge"
          note: "Fixed similarity code consumes features derived from retained content; embeddings are transient, not a vector store."
        - scope: "Retained bullet identifiers at reflector-line selection and counter update"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-bullet-metadata"
                - "runtime.md#rt-rte-sample-adaptation"
                - "memory.md#mem-rte-counter-update"
              note: "Identity matching selects the retained lines sent to reflection and fields to increment."
          records:
            - "memory.md#mem-obj-bullet-metadata"
            - "runtime.md#rt-rte-sample-adaptation"
            - "memory.md#mem-rte-counter-update"
          note: "IDs route content and updates; they are not access permissions."
        - scope: "Retained counters at generator and curator prompt/statistics consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-bullet-metadata"
                - "memory.md#mem-rte-counter-update"
              note: "Displayed model utility judgments and statistics supply advisory context to later model decisions."
          records:
            - "memory.md#mem-obj-bullet-metadata"
            - "memory.md#mem-rte-counter-update"
          note: "No deterministic harmful-count veto or causal-utility interpretation is warranted."
        - scope: "Retained call logs as potential historical decision inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-call-logs"
          note: "No specified historical automatic reader is established. Storage alone establishes none of the controlled forces; bounded absence is not declared."
        - scope: "Included but unresolved provider-side retention behind the generator, reflector and curator APIs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-generator"
            - "runtime.md#rt-cmp-reflector"
            - "runtime.md#rt-cmp-curator"
          note: "The accepted component and memory records do not expose provider retention, admission or later consumption. No behavioral authority value is established for that alternative; configured model weights are not themselves ACE memory accumulated through use."
      records:
        - "memory.md#mem-obj-playbook-content"
        - "runtime.md#rt-bap-playbook-guidance"
        - "runtime.md#rt-rte-sample-adaptation"
        - "runtime.md#rt-rte-batch-adaptation"
        - "memory.md#mem-obj-analyzer-embeddings"
        - "runtime.md#rt-rte-bulletpoint-merge"
        - "memory.md#mem-obj-bullet-metadata"
        - "memory.md#mem-rte-counter-update"
        - "memory.md#mem-obj-call-logs"
        - "runtime.md#rt-cmp-generator"
        - "runtime.md#rt-cmp-reflector"
        - "runtime.md#rt-cmp-curator"
      note: "Recorded consumers support local instruction, knowledge, learning, ranking and routing. Audit-history consumption and remote retained-state consumers remain unresolved; host parser gates and shipped static schemas are outside the retained-memory boundary."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Curator additions, batch reduction/application and reflector counter admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-sample-adaptation"
                - "runtime.md#rt-rte-batch-adaptation"
                - "memory.md#mem-rte-counter-update"
              note: "Software/model decisions admit advice and tags without content-specific human approval."
          records:
            - "runtime.md#rt-rte-sample-adaptation"
            - "runtime.md#rt-rte-batch-adaptation"
            - "memory.md#mem-rte-counter-update"
          note: "Starting the run is not per-content approval."
        - scope: "Analyzer maintenance and strict-improvement best-snapshot admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bulletpoint-merge"
                - "runtime.md#rt-rte-evaluate-select"
                - "memory.md#mem-obj-best-playbook"
              note: "Code/model maintenance and validation comparison replace retained artifacts without a human content veto."
          records:
            - "runtime.md#rt-rte-bulletpoint-merge"
            - "runtime.md#rt-rte-evaluate-select"
            - "memory.md#mem-obj-best-playbook"
          note: "Optional activation does not alter admission agency when these routes run."
        - scope: "Call and usage log admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-call-logs"
                - "runtime.md#rt-rte-sample-adaptation"
              note: "Operational logging writes call and usage artifacts as part of the computational loop."
          records:
            - "memory.md#mem-obj-call-logs"
            - "runtime.md#rt-rte-sample-adaptation"
          note: "This is automatic trace recording, not independently a learning write."
        - scope: "Initial supplied text, file selection/editing and replacement admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-playbook-reload"
            - "memory.md#mem-obj-playbook-content"
          note: "A human may supply or replace content, but the records leave the actual human-versus-program decision unresolved. Physical file reads do not establish manual agency."
        - scope: "Included but unresolved provider-side retention behind the generator, reflector and curator APIs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-generator"
            - "runtime.md#rt-cmp-reflector"
            - "runtime.md#rt-cmp-curator"
          note: "The accepted component and memory records do not expose provider retention, admission or later consumption. No write agency value is established for that alternative; configured model weights are not themselves ACE memory accumulated through use."
      records:
        - "runtime.md#rt-rte-sample-adaptation"
        - "runtime.md#rt-rte-batch-adaptation"
        - "memory.md#mem-rte-counter-update"
        - "runtime.md#rt-rte-bulletpoint-merge"
        - "runtime.md#rt-rte-evaluate-select"
        - "memory.md#mem-obj-best-playbook"
        - "memory.md#mem-obj-call-logs"
        - "runtime.md#rt-rte-playbook-reload"
        - "memory.md#mem-obj-playbook-content"
        - "runtime.md#rt-cmp-generator"
        - "runtime.md#rt-cmp-reflector"
        - "runtime.md#rt-cmp-curator"
      note: "Automatic downstream admission is established independently of unresolved initialization/replacement control. No manual value is inferred from an operator-capable interface."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Optional similarity-group removal and replacement over retained bullets"
          assessment: "known"
          findings:
            - value: "dedup"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bulletpoint-merge"
              note: "The exposed merge=False route and first-bullet fallback remove near-similar group members."
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bulletpoint-merge"
              note: "Enabled merging replaces the first retained line with regex-admitted model content while reconstructing the remaining store."
            - value: "consolidate"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-bulletpoint-merge"
              note: "Merge guidance asks for a comprehensive concise combination; semantic preservation is not checked."
          records:
            - "runtime.md#rt-rte-bulletpoint-merge"
          note: "Removal and replacement are implemented. Concise preservation is requested, not established by a generated instance; failures can still remove other group members."
        - scope: "Validation-selected best snapshot relative to current text"
          assessment: "known"
          findings:
            - value: "promote"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-evaluate-select"
                - "memory.md#mem-obj-best-playbook"
              note: "Strict validation improvement raises a whole snapshot to selected-best status for final offline testing."
          records:
            - "runtime.md#rt-rte-evaluate-select"
            - "memory.md#mem-obj-best-playbook"
          note: "Promotion concerns the selected consumer tier, not each bullet or current-state rollback."
        - scope: "Meaning-changing operations in curator and reducer generated additions"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-sample-adaptation"
            - "runtime.md#rt-rte-batch-adaptation"
            - "epistemic.md#epi-rte-curator-admission"
          note: "The routes request new reusable advice and can drop proposals, but no concrete output settles consolidation versus synthesis of claims. ADD and reducer names alone do not establish those transformations."
        - scope: "Initial-content editing or replacement transformation"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-playbook-reload"
            - "memory.md#mem-obj-playbook-content"
          note: "Whole-text replacement is exposed, but no content instance establishes its semantic curation operation."
        - scope: "Included but unresolved provider-side retention behind the generator, reflector and curator APIs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-generator"
            - "runtime.md#rt-cmp-reflector"
            - "runtime.md#rt-cmp-curator"
          note: "The accepted component and memory records do not expose provider retention, admission or later consumption. No curation operations value is established for that alternative; configured model weights are not themselves ACE memory accumulated through use."
      records:
        - "runtime.md#rt-rte-bulletpoint-merge"
        - "runtime.md#rt-rte-evaluate-select"
        - "memory.md#mem-obj-best-playbook"
        - "runtime.md#rt-rte-sample-adaptation"
        - "runtime.md#rt-rte-batch-adaptation"
        - "epistemic.md#epi-rte-curator-admission"
        - "runtime.md#rt-rte-playbook-reload"
        - "memory.md#mem-obj-playbook-content"
        - "runtime.md#rt-cmp-generator"
        - "runtime.md#rt-cmp-reflector"
        - "runtime.md#rt-cmp-curator"
      note: "Implemented deduplication, revision and selected-best promotion coexist with only claimed consolidating merge behavior. Generated semantic novelty, initialization transformations and remote maintenance remain unresolved; no decay or truth-directed invalidation is inferred."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Automatic in-loop delivery to generator, reflector, curator/reducer and analyzer"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-sample-adaptation"
                - "runtime.md#rt-rte-batch-adaptation"
                - "runtime.md#rt-bap-playbook-guidance"
                - "runtime.md#rt-rte-bulletpoint-merge"
                - "memory.md#mem-obj-bullet-metadata"
              note: "Scheduling supplies retained playbook text or selected lines without the receiving model requesting those parts."
          records:
            - "runtime.md#rt-rte-sample-adaptation"
            - "runtime.md#rt-rte-batch-adaptation"
            - "runtime.md#rt-bap-playbook-guidance"
            - "runtime.md#rt-rte-bulletpoint-merge"
            - "memory.md#mem-obj-bullet-metadata"
          note: "Covers whole-playbook delivery, reported-ID filtering and maintenance groups, not just serialization."
        - scope: "Explicit cross-run file request and returned full text"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-playbook-reload"
              note: "Caller names an existing file and the loader fulfills that request with its whole contents."
          records:
            - "runtime.md#rt-rte-playbook-reload"
          note: "Subsequent automatic prompt formatting is the separate push operation above; the requested return is not another push."
        - scope: "Historical call-log read-back"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-call-logs"
          note: "No wired historical automatic consumer is established. Retention and possible external inspection do not classify a read-back route."
        - scope: "Included but unresolved provider-side retention behind the generator, reflector and curator APIs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-generator"
            - "runtime.md#rt-cmp-reflector"
            - "runtime.md#rt-cmp-curator"
          note: "The accepted component and memory records do not expose provider retention, admission or later consumption. No read-back direction value is established for that alternative; configured model weights are not themselves ACE memory accumulated through use."
      records:
        - "runtime.md#rt-rte-sample-adaptation"
        - "runtime.md#rt-rte-batch-adaptation"
        - "runtime.md#rt-bap-playbook-guidance"
        - "runtime.md#rt-rte-bulletpoint-merge"
        - "memory.md#mem-obj-bullet-metadata"
        - "runtime.md#rt-rte-playbook-reload"
        - "memory.md#mem-obj-call-logs"
        - "runtime.md#rt-cmp-generator"
        - "runtime.md#rt-cmp-reflector"
        - "runtime.md#rt-cmp-curator"
      note: "Known pull acquisition and push delivery coexist in the reload-to-prompt chain. Historical-log and remote routes remain unresolved rather than being treated as absent."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Scheduled whole-playbook prompt delivery, including supplied and best snapshots"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-playbook-content"
                - "runtime.md#rt-bap-playbook-guidance"
                - "runtime.md#rt-rte-evaluate-select"
              note: "A generation or update invocation triggers delivery of the entire current/selected playbook; no task-specific fixed selector narrows its content."
          records:
            - "memory.md#mem-obj-playbook-content"
            - "runtime.md#rt-bap-playbook-guidance"
            - "runtime.md#rt-rte-evaluate-select"
          note: "Trigger is invocation scheduling; selector input is current or selected text; selected retained part is the whole playbook. Budget guidance is not targeted retrieval."
        - scope: "Reported-ID push into reflector input"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-sample-adaptation"
                - "memory.md#mem-obj-bullet-metadata"
              note: "After generation, reported bullet IDs are matched to parsed retained lines and those lines are delivered to reflection."
          records:
            - "runtime.md#rt-rte-sample-adaptation"
            - "memory.md#mem-obj-bullet-metadata"
          note: "Trigger is reflection; input is generator-reported IDs; selected parts are matching advice and counters, possibly multiple lines with duplicate IDs. Reporting is not proof of actual use."
        - scope: "Optional analyzer push of selected retained bullet groups into merge prompt"
          assessment: "known"
          findings:
            - value: "inferred-embedding"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bulletpoint-merge"
                - "memory.md#mem-obj-analyzer-embeddings"
              note: "Enabled maintenance encodes current bullet content and selects groups by normalized dot-product threshold."
          records:
            - "runtime.md#rt-rte-bulletpoint-merge"
            - "memory.md#mem-obj-analyzer-embeddings"
          note: "Trigger is post-curation analysis; input is retained content embeddings; delivered parts are grouped text/IDs/counts, not the vectors. This is maintenance selection, not generator retrieval."
        - scope: "Caller-requested whole-file return"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-playbook-reload"
          note: "Push signal is inapplicable to fulfillment of an explicit file request; later prompt push is classified separately."
        - scope: "Any historical call-log push selector"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-call-logs"
          note: "No historical automatic reader or selector is established; display summaries cannot supply a missing consumption route."
        - scope: "Included but unresolved provider-side retention behind the generator, reflector and curator APIs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-generator"
            - "runtime.md#rt-cmp-reflector"
            - "runtime.md#rt-cmp-curator"
          note: "The accepted component and memory records do not expose provider retention, admission or later consumption. No read-back signal value is established for that alternative; configured model weights are not themselves ACE memory accumulated through use."
      records:
        - "memory.md#mem-obj-playbook-content"
        - "runtime.md#rt-bap-playbook-guidance"
        - "runtime.md#rt-rte-evaluate-select"
        - "runtime.md#rt-rte-sample-adaptation"
        - "memory.md#mem-obj-bullet-metadata"
        - "runtime.md#rt-rte-bulletpoint-merge"
        - "memory.md#mem-obj-analyzer-embeddings"
        - "runtime.md#rt-rte-playbook-reload"
        - "memory.md#mem-obj-call-logs"
        - "runtime.md#rt-cmp-generator"
        - "runtime.md#rt-cmp-reflector"
        - "runtime.md#rt-cmp-curator"
      note: "Known coarse, identity and embedding-based push operations keep their distinct selected parts and triggers. A pull filename is not an identifier-push finding. Unresolved alternatives prevent complete coverage."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Sequential and batched response/feedback through reflection and curation to retained advice"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-sample-adaptation"
                - "runtime.md#rt-rte-batch-adaptation"
                - "memory.md#mem-obj-playbook-content"
                - "runtime.md#rt-bap-playbook-guidance"
              note: "Automatic trace-fed additions become retained guidance delivered to post-curator and later-sample/window generators."
          records:
            - "runtime.md#rt-rte-sample-adaptation"
            - "runtime.md#rt-rte-batch-adaptation"
            - "memory.md#mem-obj-playbook-content"
            - "runtime.md#rt-bap-playbook-guidance"
          note: "Known write-and-later-consumer wiring; the trace-learning definition does not require observed gain or a novel proposition."
        - scope: "Response-conditioned reflector tags to durable utility counters"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-counter-update"
                - "memory.md#mem-obj-bullet-metadata"
              note: "Automatic tag admission changes retained metadata delivered to later generator/curator inputs and persisted with advice."
          records:
            - "memory.md#mem-rte-counter-update"
            - "memory.md#mem-obj-bullet-metadata"
          note: "Counts are durable behavior-shaping advisory inputs, not measured causal utility. No successful learning claim follows."
        - scope: "Initial imported/replacement content as a possible external trace-derived artifact"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-playbook-content"
            - "runtime.md#rt-rte-playbook-reload"
          note: "Initial content and its producing mechanism are unknown, so a qualifying external trace-fed write cannot be affirmed or excluded."
        - scope: "Historical audit-log learning alternative"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-call-logs"
          note: "Logs retain traces, but no historical automatic update consumer is established; no evidenced-absence record warrants a local no."
        - scope: "Included but unresolved provider-side retention behind the generator, reflector and curator APIs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-generator"
            - "runtime.md#rt-cmp-reflector"
            - "runtime.md#rt-cmp-curator"
          note: "The accepted component and memory records do not expose provider retention, admission or later consumption. No trace learning value is established for that alternative; configured model weights are not themselves ACE memory accumulated through use."
      records:
        - "runtime.md#rt-rte-sample-adaptation"
        - "runtime.md#rt-rte-batch-adaptation"
        - "memory.md#mem-obj-playbook-content"
        - "runtime.md#rt-bap-playbook-guidance"
        - "memory.md#mem-rte-counter-update"
        - "memory.md#mem-obj-bullet-metadata"
        - "runtime.md#rt-rte-playbook-reload"
        - "memory.md#mem-obj-call-logs"
        - "runtime.md#rt-cmp-generator"
        - "runtime.md#rt-cmp-reflector"
        - "runtime.md#rt-cmp-curator"
      note: "Wired yes routes coexist with unresolved initial, audit-history and remote alternatives. Coverage is partial; there is no local or system-wide no finding, and no claim of observed improvement."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Generator reasoning, predictions and target-derived outcome feedback consumed through reflection by advice and counter updates"
          assessment: "known"
          findings:
            - value: "trajectories"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-sample-adaptation"
                - "runtime.md#rt-rte-batch-adaptation"
                - "memory.md#mem-rte-counter-update"
                - "memory.md#mem-obj-reflection-content"
              note: "The qualifying updates consume linked task-solving reasoning/answer activity and its outcome feedback, not merely a static question."
          records:
            - "runtime.md#rt-rte-sample-adaptation"
            - "runtime.md#rt-rte-batch-adaptation"
            - "memory.md#mem-rte-counter-update"
            - "memory.md#mem-obj-reflection-content"
          note: "Classifies original multi-step experience behind retained advice and counters. The reducer receives transformed last-reflection/proposal views, not all earlier traces."
        - scope: "External task/oracle material mixed into the qualifying update"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-reflection-content"
            - "runtime.md#rt-rte-sample-adaptation"
            - "runtime.md#rt-rte-batch-adaptation"
          note: "Question/context/targets also feed the route, but their original provenance is not supplied. These external references alone establish none of the trace-source values; completeness of the mixed input origin remains unresolved."
        - scope: "Possible external trace origin of imported/replaced initial content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-playbook-content"
            - "runtime.md#rt-rte-playbook-reload"
          note: "No initial instance or producer history establishes original traces or absence of them."
        - scope: "Possible historical-log qualifying write"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-call-logs"
          note: "The stored logs have operational content, but no historical learning consumer is established. A trace-source value requires a qualifying write, not just a log filename."
        - scope: "Included but unresolved provider-side retention behind the generator, reflector and curator APIs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-generator"
            - "runtime.md#rt-cmp-reflector"
            - "runtime.md#rt-cmp-curator"
          note: "The accepted component and memory records do not expose provider retention, admission or later consumption. No trace source value is established for that alternative; configured model weights are not themselves ACE memory accumulated through use."
      records:
        - "runtime.md#rt-rte-sample-adaptation"
        - "runtime.md#rt-rte-batch-adaptation"
        - "memory.md#mem-rte-counter-update"
        - "memory.md#mem-obj-reflection-content"
        - "memory.md#mem-obj-playbook-content"
        - "runtime.md#rt-rte-playbook-reload"
        - "memory.md#mem-obj-call-logs"
        - "runtime.md#rt-cmp-generator"
        - "runtime.md#rt-cmp-reflector"
        - "runtime.md#rt-cmp-curator"
      note: "Linked reasoning/action/outcome experience supports trajectories for the known automatic updates. Mixed external input provenance and other possible qualifying writes remain unresolved; single-message API transport does not independently establish session-logs or tool-traces, nor does wrapping feedback make it an event stream."
---

# ACE memory profile

## Comparison rationale

The profile classifies retained outputs and their later consumers, not the whole runtime. [MEM-OBJ-playbook-content](memory.md#mem-obj-playbook-content), [MEM-OBJ-bullet-metadata](memory.md#mem-obj-bullet-metadata), [MEM-OBJ-best-playbook](memory.md#mem-obj-best-playbook) and [MEM-OBJ-call-logs](memory.md#mem-obj-call-logs) supply the local retained inventory. Model components expose no comparable inventory of provider retention. That included uncertainty remains a separate unit on every axis; it is not evidence for a provider memory store. Unavailable AppWorld implementation is outside this main-repository classification, so this is not a whole-system AppWorld profile.

Automatic trace learning is wired through response/feedback → last reflection → admitted advice → later generator, and through response-conditioned tags → retained counters → later prompt consumers. [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation), [RT-RTE-batch-adaptation](runtime.md#rt-rte-batch-adaptation) and [MEM-RTE-counter-update](memory.md#mem-rte-counter-update) support these routes without establishing benefit. The original linked reasoning, prediction and correctness feedback supports trajectories; neither role names nor raw JSON logging establish additional source values. External task/oracle provenance remains unresolved beside that positive. Log retention alone does not establish an additional learning route.

The whole-playbook generator route is coarse push. Its model-internal relevance interpretation does not establish another recorded selector. The reflector route is identifier push because it actually matches reported IDs to retained lines. Analyzer maintenance separately selects retained groups with embeddings. Cross-run file return is pull; automatic delivery of the returned text to a later role is push. These are distinct operations within one chain, not competing system labels ([RT-BAP-playbook-guidance](runtime.md#rt-bap-playbook-guidance), [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation), [RT-RTE-bulletpoint-merge](runtime.md#rt-rte-bulletpoint-merge), [RT-RTE-playbook-reload](runtime.md#rt-rte-playbook-reload)).

Analyzer deduplication and replacement support dedup and evolve, including destructive fallback. Consolidation is only claimed for its requested concise combination: the records do not establish meaning preservation. Likewise new-insight instructions do not prove synthesis of a claim absent from the inputs. Selection of a best snapshot promotes a complete retained artifact for final testing; it does not promote every bullet or roll back current training state ([RT-RTE-bulletpoint-merge](runtime.md#rt-rte-bulletpoint-merge), [EPI-RTE-curator-admission](epistemic.md#epi-rte-curator-admission), [RT-RTE-evaluate-select](runtime.md#rt-rte-evaluate-select)).

Reconciliation supersedes EPI-OBJ-reflection with [MEM-OBJ-reflection-content](memory.md#mem-obj-reflection-content), EPI-OBJ-playbook with [MEM-OBJ-playbook-content](memory.md#mem-obj-playbook-content), and EPI-RTE-counter-update with [MEM-RTE-counter-update](memory.md#mem-rte-counter-update). These identity resolutions affect the trace, lineage, authority and admission citations; they do not upgrade evidence strength. The combined epistemic tags object remains distinct from persisted metadata, so this profile uses the latter for retained-field classification. Last-tag-per-ID admission is not a tally of all batch judgments.

Every axis retains unresolved included units. Supported unions therefore include only local positive findings at their stated bases, never complete-value conclusions. There is no warranted local trace-learning no: the set declares no bounded absence record for these alternatives. Missing initial authorship prevents manual/authored classification; missing actual generated lessons prevents stronger semantic curation conclusions; missing remote retention and consumers prevents a complete inventory. No observed operation or causal improvement is asserted.

Source-read log: none. This classification used only the supplied accepted members, reconciliation, types and record contract; it added no source evidence or records.
