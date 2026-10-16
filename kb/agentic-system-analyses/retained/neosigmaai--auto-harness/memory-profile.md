---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "auto-harness memory profile: retained experiment evidence, candidate revisions and evaluation controls."
run-id: AAS-2026-10-15-auto-harness-92303e444cb2-01
source-identity: https://github.com/neosigmaai/auto-harness
reviewed-boundary: "52360dbbeb8cea8886d90778e634a145c51da735"
memory-comparison:
  version: 2
  scope: "Retained Terminal/BIRD diagnostic copies and their source-job lifecycle; requested learning entries; through-use candidate Python/instruction revisions and their later adoption; last CLI results, score history, suite membership/threshold/diagnostics and baseline-derived task splits. Includes unresolved caller-controlled content admission and requested note reuse. Excludes unchanged shipped program/templates, ordinary Terminal/tau/BIRD task/session accumulation and diagnostic previews as supposed model checkpoints, external coding-host memory, provider state and external framework internals."
  axes:
    storage_substrate:
      assessment: known
      units:
        - scope: "Diagnostic copies/source jobs, learning log, CLI results, score history, suite parts and task splits"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-traces, memory.md#mem-obj-learnings, memory.md#mem-obj-train-results, memory.md#mem-obj-results, memory.md#mem-obj-suite, memory.md#mem-obj-task-split, memory.md#mem-rte-trace-retention]
              note: "Local JSON, Markdown and TSV persistence is implemented; log initialization does not demonstrate substantive entries."
          records: [memory.md#mem-obj-traces, memory.md#mem-obj-learnings, memory.md#mem-obj-train-results, memory.md#mem-obj-results, memory.md#mem-obj-suite, memory.md#mem-obj-task-split]
          note: "These records enumerate the local retained noncandidate surfaces; suite parts share their container's file substrate."
        - scope: "Through-use candidate code and instruction revisions"
          assessment: known
          findings:
            - value: files
              basis: afforded
              records: [runtime.md#rt-obj-agent-code, runtime.md#rt-obj-agent-instructions, runtime.md#rt-rte-candidate-revision]
              note: "The external coding agent can replace the candidate file; no learned revision was supplied."
            - value: repo
              basis: claimed
              records: [runtime.md#rt-rte-candidate-revision, runtime.md#rt-rte-iteration-record]
              note: "The program prescribes committing admitted revisions; the recorder's commit lookup does not prove compliance."
          records: [runtime.md#rt-obj-agent-code, runtime.md#rt-obj-agent-instructions, runtime.md#rt-rte-candidate-revision]
          note: "File and prescribed Git retention classify this revision surface, not the coding model's own storage."
      records: [memory.md#mem-obj-traces, memory.md#mem-obj-learnings, memory.md#mem-obj-train-results, memory.md#mem-obj-results, memory.md#mem-obj-suite, memory.md#mem-obj-task-split, runtime.md#rt-rte-candidate-revision]
      note: "Complete substrate inventory within the local retained boundary; excluded ordinary sessions and external models do not add in-memory or model-weight memory values."
    representational_form:
      assessment: known
      units:
        - scope: "Trace dialogue and diagnostic text interpreted by the outer coding agent"
          assessment: known
          findings:
            - value: natural-language
              basis: afforded
              records: [memory.md#mem-obj-traces, memory.md#mem-rte-trace-retention]
              note: "The program directs diagnostic interpretation of retained dialogue/tool text; an exercised read is not shown."
          records: [memory.md#mem-obj-traces]
          note: "Text consumption is separate from the trace's structured fields; truncated text remains text."
        - scope: "Trace structures/results and retained CLI, history, suite and split fields"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-traces, memory.md#mem-obj-train-results, memory.md#mem-obj-results, memory.md#mem-obj-suite-tasks, memory.md#mem-obj-suite-threshold, memory.md#mem-obj-suite-last-results, memory.md#mem-obj-task-split]
              note: "Task IDs, rewards, thresholds and serialization fields have localized fixed-code interpretation; numeric thresholds are not parametric weights."
          records: [memory.md#mem-obj-traces, memory.md#mem-obj-train-results, memory.md#mem-obj-results, memory.md#mem-obj-suite, memory.md#mem-obj-task-split]
          note: "No authority is inferred for unconsumed diagnostic metadata from its symbolic form."
        - scope: "Requested learning entries"
          assessment: known
          findings:
            - value: natural-language
              basis: claimed
              records: [memory.md#mem-obj-learnings]
              note: "Requested accounts of changes, outcomes and patterns are prose; actual entries are unavailable."
          records: [memory.md#mem-obj-learnings]
          note: "Classification of the specified content, not evidence that the empty initialized file contains learnings."
        - scope: "Revised candidate Python at import and embedded directions at task-model delivery"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [runtime.md#rt-obj-agent-code, runtime.md#rt-bap-candidate-runtime]
              note: "The import channel executes Python, including future revisions."
            - value: natural-language
              basis: wired
              records: [runtime.md#rt-obj-agent-instructions, runtime.md#rt-bap-candidate-runtime]
              note: "Embedded instruction constants reach model interpretation through system messages or ADK agents."
          records: [runtime.md#rt-obj-agent-code, runtime.md#rt-obj-agent-instructions, runtime.md#rt-bap-candidate-runtime]
          note: "Two explicit consumption paths within the retained revision surface; wiring does not prove an updated instance existed."
      records: [memory.md#mem-obj-traces, memory.md#mem-obj-learnings, memory.md#mem-obj-suite, memory.md#mem-obj-train-results, memory.md#mem-obj-results, memory.md#mem-obj-task-split, runtime.md#rt-bap-candidate-runtime]
      note: "All scoped parts have a recorded text or symbolic form. Provider parameters are not a through-use memory surface of this local plane."
    lineage:
      assessment: partial
      units:
        - scope: "Copied Terminal/BIRD diagnostic evidence"
          assessment: partial
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-obj-traces, memory.md#mem-rte-trace-retention]
              note: "Adapters copy or extract task-framework outputs into local diagnostic files."
          records: [memory.md#mem-obj-traces, memory.md#mem-rte-trace-retention]
          note: "Local acquisition is known; full BIRD payload construction and external trace fidelity are unresolved, preventing complete derivation provenance."
        - scope: "CLI outcomes, suite diagnostic results, promoted IDs and baseline-derived split membership"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [memory.md#mem-obj-train-results, memory.md#mem-obj-suite-last-results, memory.md#mem-obj-suite-tasks, memory.md#mem-obj-task-split]
              note: "Execution feedback is serialized or transformed into retained outcomes and selection IDs. This names derivation, not authenticated benchmark truth."
          records: [memory.md#mem-obj-train-results, memory.md#mem-obj-suite-last-results, memory.md#mem-obj-suite-tasks, memory.md#mem-obj-task-split]
          note: "Covers the locally recorded derivation from returned feedback; split metadata does not authenticate train provenance."
        - scope: "Coding-agent learning entries and candidate revisions"
          assessment: known
          findings:
            - value: authored
              basis: claimed
              records: [memory.md#mem-obj-learnings, runtime.md#rt-rte-candidate-revision]
              note: "The program assigns diagnosis, note writing and code editing to the external coding agent; it does not establish mere extraction or actual authored instances."
          records: [memory.md#mem-obj-learnings, runtime.md#rt-rte-candidate-revision]
          note: "Complete classification of the prescribed authorship path, without inferring a semantic transformation for absent content."
        - scope: "Caller-supplied history numbers and configuration-derived suite threshold"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-results, memory.md#mem-obj-suite-threshold, runtime.md#rt-rte-iteration-record]
          note: "Local serialization and configuration copying do not establish the origin of the supplied content. Human authorship, software derivation and imported values cannot be resolved."
      records: [memory.md#mem-obj-traces, memory.md#mem-obj-train-results, memory.md#mem-obj-suite-last-results, memory.md#mem-obj-suite-tasks, memory.md#mem-obj-task-split, memory.md#mem-obj-learnings, runtime.md#rt-rte-candidate-revision, memory.md#mem-obj-results, memory.md#mem-obj-suite-threshold]
      note: "Known local acquisition/derivation and prescribed authorship coexist with opaque upstream payload and caller/configuration provenance."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Retained diagnostic traces at outer diagnosis and subsequent revision"
          assessment: known
          findings:
            - value: knowledge
              basis: afforded
              records: [memory.md#mem-obj-traces, memory.md#mem-rte-trace-retention]
              note: "Foreground diagnosis can use copied traces as evidence, not as standing commands."
            - value: learning
              basis: afforded
              records: [runtime.md#rt-rte-candidate-revision, memory.md#mem-obj-traces]
              note: "The prescribed diagnosis route can use retained experience to revise durable candidate behavior; no benefit or exercised update is established."
          records: [memory.md#mem-obj-traces, runtime.md#rt-rte-candidate-revision]
          note: "Separate evidence and update consumers/effects within the same prescribed route."
        - scope: "Suite IDs, split membership and prior CLI failures at future task selection"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-suite-tasks, memory.md#mem-obj-task-split, memory.md#mem-obj-train-results, runtime.md#rt-bap-history-gate]
              note: "These retained parts select task sets, reruns or failing non-suite promotion inputs."
          records: [memory.md#mem-obj-suite-tasks, memory.md#mem-obj-task-split, memory.md#mem-obj-train-results]
          note: "Selection is fixed code, not semantic ranking."
        - scope: "Suite threshold, suite membership denominator and history maximum at gate decision"
          assessment: known
          findings:
            - value: validation
              basis: wired
              records: [memory.md#mem-obj-suite-threshold, memory.md#mem-obj-suite-tasks, memory.md#mem-obj-results, runtime.md#rt-rte-gate-admission]
              note: "Retained parameters and prior scores determine the comparison criteria for candidate eligibility."
            - value: enforcement
              basis: wired
              records: [runtime.md#rt-rte-gate-admission, runtime.md#rt-bap-history-gate]
              note: "Within an invoked gate these comparisons can veto successful return; they cannot intercept every commit or enforce external rollback."
          records: [memory.md#mem-obj-suite-threshold, memory.md#mem-obj-suite-tasks, memory.md#mem-obj-results, runtime.md#rt-rte-gate-admission]
          note: "Validation and enforced gate-return consequences coexist but do not authenticate inputs."
        - scope: "Outcome feedback at suite promotion and baseline split construction"
          assessment: known
          findings:
            - value: learning
              basis: wired
              records: [memory.md#mem-obj-train-results, memory.md#mem-obj-suite-tasks, memory.md#mem-obj-task-split, runtime.md#rt-rte-gate-admission, runtime.md#rt-rte-prepare-baseline]
              note: "Retained/reported execution feedback feeds durable future selection controls. The resulting IDs have routing authority downstream, not an accepted explanation."
          records: [memory.md#mem-obj-train-results, memory.md#mem-obj-suite-tasks, memory.md#mem-obj-task-split]
          note: "Update-consumer authority is distinct from the downstream task-selector authority."
        - scope: "Revised instruction constants at later task-model calls"
          assessment: known
          findings:
            - value: instruction
              basis: wired
              records: [runtime.md#rt-obj-agent-instructions, runtime.md#rt-bap-candidate-runtime]
              note: "Directions in the adopted candidate are supplied to task models; delivery does not establish compliance."
          records: [runtime.md#rt-obj-agent-instructions, runtime.md#rt-bap-candidate-runtime]
          note: "This classifies the instruction part, not all executable Python as instruction or enforcement."
        - scope: "Arbitrary revised Python's particular downstream effects and learning-log later use"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-agent-code, runtime.md#rt-rte-candidate-revision, memory.md#mem-obj-learnings]
          note: "Imports are wired but absent revisions do not identify particular retained controls or their force. The learning log has no established loader or actual reader, preventing a definite authority classification at reuse."
        - scope: "Historical suite diagnostics and accounting metadata beyond consumed score fields"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-suite-last-results, memory.md#mem-obj-results]
          note: "Merge/serialization and commit/timestamp bookkeeping establish no further consequential consumer; no additional force is assigned."
      records: [memory.md#mem-obj-traces, memory.md#mem-obj-learnings, memory.md#mem-obj-train-results, memory.md#mem-obj-suite-tasks, memory.md#mem-obj-suite-threshold, memory.md#mem-obj-suite-last-results, memory.md#mem-obj-results, memory.md#mem-obj-task-split, runtime.md#rt-bap-candidate-runtime, runtime.md#rt-rte-candidate-revision]
      note: "Preserves implemented gate/selection and instruction channels without upgrading arbitrary executable revisions, unconsumed diagnostics or requested note reuse."
    write_agency:
      assessment: partial
      units:
        - scope: "Adapter result/trace writes, baseline history/splits, suite initialization, diagnostic overwrite and post-check membership promotion"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-rte-trace-retention, memory.md#mem-obj-train-results, memory.md#mem-obj-task-split, memory.md#mem-obj-suite-tasks, memory.md#mem-obj-suite-threshold, memory.md#mem-obj-suite-last-results, runtime.md#rt-rte-prepare-baseline]
              note: "Software admits these outputs without per-content human approval. Configuration provenance is a separate unresolved input mechanism."
          records: [memory.md#mem-rte-trace-retention, memory.md#mem-obj-train-results, memory.md#mem-obj-task-split, memory.md#mem-obj-suite, runtime.md#rt-rte-prepare-baseline]
          note: "Starting preparation or evaluation does not make subsequent deterministic admission manual."
        - scope: "Requested coding-agent learning entries and candidate changes"
          assessment: known
          findings:
            - value: automatic
              basis: claimed
              records: [memory.md#mem-obj-learnings, runtime.md#rt-rte-candidate-revision]
              note: "The program assigns content decisions to computation without an explicit per-entry human approval stage; external permission behavior is not established."
          records: [memory.md#mem-obj-learnings, runtime.md#rt-rte-candidate-revision]
          note: "Classification of the requested admission mechanism, not demonstrated autonomous editing."
        - scope: "Score-number submission to recorder and configuration/previous-content admission"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-results, memory.md#mem-obj-suite-threshold, runtime.md#rt-rte-iteration-record, runtime.md#rt-rte-prepare-baseline]
          note: "Recorder serialization is software, but the substantive supplying/approval decision is caller-controlled and unresolved. Existing workspace contents are preserved. No explicit human decision establishes manual admission, and generic caller identity does not establish automatic admission of those contents."
      records: [memory.md#mem-rte-trace-retention, memory.md#mem-obj-train-results, memory.md#mem-obj-task-split, memory.md#mem-obj-suite, memory.md#mem-obj-learnings, memory.md#mem-obj-results, memory.md#mem-obj-suite-threshold, runtime.md#rt-rte-candidate-revision, runtime.md#rt-rte-iteration-record]
      note: "Automatic local transformations and prescribed model admission do not resolve the separate caller/configuration and preserved-content mechanisms."
    curation_operations:
      assessment: partial
      units:
        - scope: "Regression membership transformation"
          assessment: known
          findings:
            - value: promote
              basis: wired
              records: [memory.md#mem-obj-suite-tasks, runtime.md#rt-rte-gate-admission]
              note: "A newly passing former failure is raised into the persistent regression suite, changing its future evaluation salience."
            - value: evolve
              basis: wired
              records: [memory.md#mem-obj-suite-tasks, runtime.md#rt-rte-gate-admission]
              note: "The existing suite membership is revised by union with newly passing task IDs. Set uniqueness alone is not treated as semantic deduplication."
          records: [memory.md#mem-obj-suite-tasks, runtime.md#rt-rte-gate-admission]
          note: "Implemented transformation, not merely the promotion route name, establishes these operations."
        - scope: "Retained diagnostic lifecycle"
          assessment: known
          findings:
            - value: decay
              basis: wired
              records: [memory.md#mem-rte-trace-retention, runtime.md#rt-rte-terminal-task]
              note: "Old Terminal raw job directories are deleted after selection of the current job; selected diagnostic copies persist separately."
            - value: evolve
              basis: wired
              records: [memory.md#mem-obj-suite-last-results, memory.md#mem-rte-trace-retention]
              note: "Existing latest diagnostic files and suite diagnostic mappings are replaced/merged; these are content revisions, not epistemic withdrawal or transactional rollback."
          records: [memory.md#mem-rte-trace-retention, memory.md#mem-obj-suite-last-results]
          note: "First-seen preservation and stale latest entries qualify the reach of revision/deletion."
        - scope: "Requested revision of existing candidate"
          assessment: known
          findings:
            - value: evolve
              basis: claimed
              records: [runtime.md#rt-rte-candidate-revision]
              note: "The program explicitly requests focused changes to the existing implementation and instructions."
          records: [runtime.md#rt-rte-candidate-revision]
          note: "Requested evolution is not implemented model-responsive optimization or an observed edit."
        - scope: "Semantic transformations in learning entries and external diagnostic payload construction"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-learnings, memory.md#mem-obj-traces, runtime.md#rt-rte-candidate-revision]
          note: "Requested hypotheses and patterns do not establish whether actual content consolidates existing claims or synthesizes new ones. External payload formation is opaque; copying, field extraction and primary-key checks alone establish neither operation."
      records: [memory.md#mem-obj-suite-tasks, memory.md#mem-obj-suite-last-results, memory.md#mem-rte-trace-retention, memory.md#mem-obj-learnings, memory.md#mem-obj-traces, runtime.md#rt-rte-candidate-revision]
      note: "Known local promotion, revision and deletion coexist with unresolved semantic note/payload transformations. No consolidation or synthesis is inferred from the word learning."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Gate loaders, split lookup and executable candidate adoption"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-bap-history-gate, memory.md#mem-obj-task-split, runtime.md#rt-bap-candidate-runtime]
              note: "Gate/runner/import consumers explicitly request retained JSON/TSV, task membership and candidate implementation. Explicit task IDs can bypass split lookup."
          records: [runtime.md#rt-bap-history-gate, memory.md#mem-obj-task-split, runtime.md#rt-bap-candidate-runtime]
          note: "Decoding and returning requested data are not an additional unsolicited push."
        - scope: "Foreground failure-trace diagnosis"
          assessment: known
          findings:
            - value: pull
              basis: afforded
              records: [memory.md#mem-rte-trace-retention, runtime.md#rt-rte-candidate-revision]
              note: "The foreground coding agent is directed to choose and inspect failing train evidence, not automatically injected historical traces."
          records: [memory.md#mem-rte-trace-retention, runtime.md#rt-rte-candidate-revision]
          note: "No exercised read or local loader is supplied."
        - scope: "Revised instruction constants supplied to task models"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-obj-agent-instructions, runtime.md#rt-bap-candidate-runtime, runtime.md#rt-rte-terminal-task, runtime.md#rt-rte-tau-task, runtime.md#rt-rte-bird-session]
              note: "After candidate adoption, task initialization/context construction supplies its directions without a task-model request for retained guidance. Only through-use revised constants count here, not unchanged stock instructions."
          records: [runtime.md#rt-obj-agent-instructions, runtime.md#rt-bap-candidate-runtime]
          note: "Automatic instruction delivery is separate from the upstream requested Python import; cached runners qualify replacement timing."
        - scope: "Learning-log reuse and historical diagnostic consumption beyond serialization"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-learnings, memory.md#mem-obj-suite-last-results]
          note: "The log's memory label supplies no reader/selector; suite diagnostic loading supplies no consequential historical-diagnostic reader. Direction cannot be assigned to these unresolved later-consumer paths."
      records: [runtime.md#rt-bap-history-gate, memory.md#mem-obj-task-split, memory.md#mem-rte-trace-retention, runtime.md#rt-bap-candidate-runtime, memory.md#mem-obj-learnings, memory.md#mem-obj-suite-last-results]
      note: "Known pull and automatic instruction push coexist with unresolved note/diagnostic read-back."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Automatic delivery of revised candidate instruction constants"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [runtime.md#rt-obj-agent-instructions, runtime.md#rt-bap-candidate-runtime, runtime.md#rt-rte-terminal-task, runtime.md#rt-rte-tau-task, runtime.md#rt-rte-bird-session]
              note: "Trigger: task/context or selected ADK-agent construction. Selector input: adopted candidate and configured integration/mode. Selected retained part: that candidate's instruction constant, supplied as standing guidance without content-targeted retrieval."
          records: [runtime.md#rt-obj-agent-instructions, runtime.md#rt-bap-candidate-runtime]
          note: "Mode/configuration availability is coarse selection; task IDs are not a match selecting historical prose."
        - scope: "Gate/split/import requests and foreground trace inspection"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-bap-history-gate, memory.md#mem-obj-task-split, memory.md#mem-rte-trace-retention, runtime.md#rt-bap-candidate-runtime]
          note: "These operations fulfill explicit consumer requests and are pull; filenames and task IDs on them do not establish identifier-based push."
        - scope: "Unresolved learning-log and historical-diagnostic delivery"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-learnings, memory.md#mem-obj-suite-last-results]
          note: "No established selection/delivery mechanism decides whether these are additional pushes or which signal would select their contents."
      records: [runtime.md#rt-obj-agent-instructions, runtime.md#rt-bap-candidate-runtime, runtime.md#rt-bap-history-gate, memory.md#mem-obj-task-split, memory.md#mem-rte-trace-retention, memory.md#mem-obj-learnings, memory.md#mem-obj-suite-last-results]
      note: "A coarse instruction-supply witness does not resolve unknown note reuse or convert task-identified pull into targeted push."
    trace_learning:
      assessment: partial
      units:
        - scope: "Outcome-fed regression-suite promotion and baseline split generation"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-obj-suite-tasks, memory.md#mem-obj-task-split, runtime.md#rt-rte-gate-admission, runtime.md#rt-rte-prepare-baseline]
              note: "Automatic reward-fed writes retain task membership, and later gates/runners consume those IDs to shape behavior. Neither explanations nor improved measured capacity are prerequisites for this axis."
          records: [memory.md#mem-obj-suite-tasks, memory.md#mem-obj-task-split, runtime.md#rt-rte-gate-admission]
          note: "The raw feedback-to-durable-selection-to-later-consumer chain is recorded; actual operation is unobserved."
        - scope: "Trace-responsive candidate revision and later imports/model instruction delivery"
          assessment: known
          findings:
            - value: "yes"
              basis: afforded
              records: [runtime.md#rt-rte-candidate-revision, runtime.md#rt-bap-candidate-runtime, memory.md#mem-obj-traces]
              note: "The outer program affords computational diagnosis of retained task evidence, durable code/instruction changes and later adoption. The optimizer is external and unobserved; this does not upgrade it to wired learning."
          records: [runtime.md#rt-rte-candidate-revision, runtime.md#rt-bap-candidate-runtime]
          note: "Standing trace-fed revision capacity is independent of the report's uninspected future-capacity learning and causal-benefit conclusions."
        - scope: "Learning-log entries and their proposed later consumer"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-learnings, runtime.md#rt-rte-candidate-revision]
          note: "Automatic note writing is requested, but an established later consumption route is missing. Raw trace retention and a memory label do not close this chain."
        - scope: "Caller-supplied score content and external payload transformations"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-results, runtime.md#rt-rte-iteration-record, memory.md#mem-obj-traces]
          note: "Caller control and opaque upstream processing prevent a complete classification of additional trace-fed durable updates. No bounded global negative follows."
      records: [memory.md#mem-obj-suite-tasks, memory.md#mem-obj-task-split, runtime.md#rt-rte-candidate-revision, runtime.md#rt-bap-candidate-runtime, memory.md#mem-obj-learnings, memory.md#mem-obj-results, memory.md#mem-obj-traces]
      note: "Known wired selection updates and an afforded candidate-update route coexist with unresolved log reuse and caller/upstream alternatives. No system-wide no is asserted."
    trace_source:
      assessment: partial
      units:
        - scope: "Suite promotion and reward-stratified split construction"
          assessment: known
          findings:
            - value: tool-traces
              basis: wired
              records: [memory.md#mem-obj-suite-tasks, memory.md#mem-obj-task-split, memory.md#mem-obj-train-results, runtime.md#rt-rte-gate-admission, runtime.md#rt-rte-prepare-baseline]
              note: "Original consumed content is recorded benchmark execution feedback: task rewards and rerun outcomes. Serialized reward mappings are not conversational logs or multi-step trajectories."
          records: [memory.md#mem-obj-suite-tasks, memory.md#mem-obj-task-split, runtime.md#rt-rte-gate-admission]
          note: "Classifies the outcome content actually used by local membership updates, not all data inside the external benchmark."
        - scope: "Trace-guided candidate revision"
          assessment: partial
          findings:
            - value: session-logs
              basis: afforded
              records: [memory.md#mem-obj-traces, runtime.md#rt-rte-candidate-revision]
              note: "Retained agent dialogue/messages can feed outer coding-agent diagnosis and durable revisions."
            - value: tool-traces
              basis: afforded
              records: [memory.md#mem-obj-traces, runtime.md#rt-rte-candidate-revision]
              note: "Tool requests/results and task execution feedback can feed the same revision route."
          records: [memory.md#mem-obj-traces, runtime.md#rt-rte-candidate-revision]
          note: "BIRD payload composition and actual diagnostic choices are unresolved. A field named tool_trajectory does not establish a linked state-action-outcome learning input; an ADK event wrapper alone does not establish event-stream origin."
        - scope: "Potential qualifying learning-log/caller-content update alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-learnings, memory.md#mem-obj-results, runtime.md#rt-rte-iteration-record]
          note: "The log's later consumer and the origin/control of submitted numbers are unresolved, so their qualifying original trace inputs cannot be completely classified."
      records: [memory.md#mem-obj-suite-tasks, memory.md#mem-obj-task-split, memory.md#mem-obj-train-results, memory.md#mem-obj-traces, runtime.md#rt-rte-candidate-revision, memory.md#mem-obj-learnings, memory.md#mem-obj-results]
      note: "Each positive source value belongs to a qualifying route; opaque alternatives remain unresolved rather than being declared inapplicable."
---

# auto-harness memory profile

## Comparison rationale

The memory boundary is the retained experiment loop, not every state holder in the runtime. Local diagnostic files, evaluation controls and candidate revisions have different consumers. Ordinary task messages and BIRD in-memory sessions are working state, not demonstrated durable derived memory. BIRD diagnostic previews do not establish a model-window checkpoint; external model parameters and coding-host compaction therefore add no substrate, form or trace-learning value here. These distinctions follow [MEM-OBJ-traces](memory.md#mem-obj-traces), [RT-RTE-bird-session](runtime.md#rt-rte-bird-session), [RT-RTE-tau-task](runtime.md#rt-rte-tau-task) and [RT-CMP-coding-model](runtime.md#rt-cmp-coding-model).

The accepted suite inventory separates [MEM-OBJ-suite-tasks](memory.md#mem-obj-suite-tasks), [MEM-OBJ-suite-threshold](memory.md#mem-obj-suite-threshold) and [MEM-OBJ-suite-last-results](memory.md#mem-obj-suite-last-results). Promotion changes future selection only after successful checks; diagnostics can persist before rejection; the threshold is carried forward rather than learned. This prevents assigning one authority or admission history to the whole suite. The score recorder similarly admits caller numbers without authenticating a gate result, leaving a separate content-control uncertainty despite implemented physical append; see [RT-RTE-iteration-record](runtime.md#rt-rte-iteration-record).

Suite and split membership are automatic trace-fed durable behavior-shaping results. Their source is execution feedback, classified as tool traces, rather than natural-language generalizations. Their downstream authority is routing; feedback has learning authority at the update consumer. This is a memory-route classification, not a claim of improved future capacity or exercised self-improvement. Those conclusions remain independently limited in [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision). No event-stream or trajectory source is inferred merely from JSON event labels or a field name; [MEM-OBJ-traces](memory.md#mem-obj-traces) leaves external payload fidelity unresolved.

Candidate adoption contains two operations. Imports request Python and are pull. Subsequent context construction supplies the adopted candidate's instruction constants without a model request and is coarse push. The memory claim applies only when those constants have changed through use. It does not count unchanged shipped instructions as memory. The import/delivery channel is wired, while experience-responsive revision remains afforded/requested and actual replacement timing is qualified by caching; see [RT-BAP-candidate-runtime](runtime.md#rt-bap-candidate-runtime), [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions) and [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision).

Reconciliation supersedes the epistemic learning-log declaration with [MEM-OBJ-learnings](memory.md#mem-obj-learnings). All profile citations use that canonical identity. The supersession resolves identity, not a missing reader or explanatory warrant. The valid suite and task-content containers remain alongside their parts; none of those parts supersedes a container. No other supersession changes a value.

Partial assessments preserve specific unknowns: external trace construction, supplied-score/configuration provenance and control, absent concrete semantic note transformations, arbitrary revised-code effects, and learning-log/historical-diagnostic later consumers. A known local path does not erase these alternatives. No observed-run or causal basis is used. No source files were read for this profile; all classifications use the supplied accepted records, so there is no additional source-read log.
