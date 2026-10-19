---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "JAZ memory comparison: retained console histories, replay traces, workflow artifacts, rollout samples and persisted console state at the frozen release."
run-id: "AAS-2026-10-19-jaz-9d991c410bb9-01"
source-identity: "https://github.com/jaz-lang/JAZ"
reviewed-boundary: "0803d4971be785e95b80054b02259664d70fa3da"
memory-comparison:
  version: 2
  scope: "Retained objects accumulated or changed through use: console main/helper and readline histories; ATIF and diagnostic projections; replay access/control state; generated workflow packages; token sidecars and rollout samples; persisted settings and credentials; exposed replacement serving-policy state and unresolved provider/remote trace alternatives. Includes their write, maintenance and later-consumer routes. Excludes static shipped prompts, ordinary current-invocation REPL/messages except when bridged into retained objects, unshipped development/evaluation systems, and external trainer/server/collector internals as implementation evidence. Exclusion does not resolve their included interface payloads or provenance."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Console main/history records and helper exchanges"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-history"
                - "memory.md#mem-obj-helper-history"
              note: "Live process records; no restored cross-session live-object checkpoint is established."
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-obj-helper-history"
          note: "Both retained across fresh invocations in one console namespace."
        -
          scope: "Readline, ATIF disk output, diagnostic directories, workflow packages, settings and credentials"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-readline-history"
                - "memory.md#mem-obj-atif-trajectory"
                - "memory.md#mem-obj-trajectory-directory"
                - "runtime.md#rt-rte-workflow-emission"
                - "runtime.md#rt-bap-settings-load"
                - "memory.md#mem-obj-credentials"
              note: "Text, JSON and Python files are storage objects, not a database or vector index."
          records:
            - "memory.md#mem-obj-readline-history"
            - "memory.md#mem-obj-atif-trajectory"
            - "memory.md#mem-obj-trajectory-directory"
            - "runtime.md#rt-rte-workflow-emission"
            - "runtime.md#rt-bap-settings-load"
            - "memory.md#mem-obj-credentials"
          note: "These recorded local retained objects have explicit disk/file paths."
        -
          scope: "Recorder buffers, token sidecars and rollout/sample objects"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-atif-trajectory"
                - "memory.md#mem-obj-token-stamp"
                - "memory.md#mem-obj-rollout"
              note: "Sidecars and frozen samples remain Python objects; JSON-compatible export is not a disk writer."
          records:
            - "memory.md#mem-obj-atif-trajectory"
            - "memory.md#mem-obj-token-stamp"
            - "memory.md#mem-obj-rollout"
          note: "Process-side capture and projection are distinct from optional persistence."
        -
          scope: "Serving weights behind the exposed SGLang update endpoint"
          assessment: "known"
          findings:
            -
              value: "model-weights"
              basis: "wired"
              records:
                - "memory.md#mem-rte-weight-update"
                - "runtime.md#rt-cmp-llm"
              note: "The retained serving policy resides in model parameters; the service physical backing and actual accepted replacement remain outside inspected evidence."
          records:
            - "memory.md#mem-rte-weight-update"
            - "runtime.md#rt-cmp-llm"
          note: "Provider-hosted retained parameters are distinguished from symbolic model-selection settings."
        -
          scope: "Other provider-retained state and remote trace alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-llm"
            - "memory.md#mem-obj-atif-trajectory"
          note: "Default provider internals remain uninspected; local trajectory storage cannot classify remote retention. The accepted record inventory does not determine remote trace payload or substrate."
      records:
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-obj-helper-history"
        - "memory.md#mem-obj-readline-history"
        - "memory.md#mem-obj-atif-trajectory"
        - "memory.md#mem-obj-trajectory-directory"
        - "runtime.md#rt-rte-workflow-emission"
        - "runtime.md#rt-bap-settings-load"
        - "memory.md#mem-obj-credentials"
        - "memory.md#mem-obj-token-stamp"
        - "memory.md#mem-obj-rollout"
        - "memory.md#mem-rte-weight-update"
        - "runtime.md#rt-cmp-llm"
      note: "Known local file/process storage coexists with unresolved provider and remote retained alternatives; this is not a complete storage union."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Main-history transcript description and prompt text; helper rendered transcripts"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-history"
                - "memory.md#mem-obj-helper-history"
              note: "Prior prompts, answers and readable transcripts supply model-interpreted context."
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-obj-helper-history"
          note: "Only the interpreted text path is classified here, not opaque live payloads."
        -
          scope: "Console turn structure, helper tags/applied flags and stored snippets"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-history"
                - "memory.md#mem-obj-helper-history"
              note: "Ordered fields and Python snippets have localized, fixed-rule consumers."
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-obj-helper-history"
          note: "Fixed record fields and executable snippets are separated from text interpretation."
        -
          scope: "Opaque live Python input/result parts in main history"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-conversation-history"
          note: "A capped repr does not determine the form of arbitrary inspectable live payloads."
        -
          scope: "Readline source lines, ATIF tree/edit coordinates, directory provenance and workflow executable code"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-readline-history"
                - "memory.md#mem-obj-atif-trajectory"
                - "memory.md#mem-obj-trajectory-directory"
                - "runtime.md#rt-rte-workflow-emission"
              note: "Line editing/source execution, structured trace fields and generated Python use fixed-rule representations."
          records:
            - "memory.md#mem-obj-readline-history"
            - "memory.md#mem-obj-atif-trajectory"
            - "memory.md#mem-obj-trajectory-directory"
            - "runtime.md#rt-rte-workflow-emission"
          note: "Symbolic routes do not resolve all text carried by their containers."
        -
          scope: "ATIF message text and diagnostic Markdown displays"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-atif-trajectory"
                - "memory.md#mem-obj-trajectory-directory"
              note: "Recorded messages and readable diagnostic text are consumed through interpretation."
          records:
            - "memory.md#mem-obj-atif-trajectory"
            - "memory.md#mem-obj-trajectory-directory"
          note: "Text displays are not restored live objects."
        -
          scope: "Token IDs, masks, logprobs, frozen rollout structures and sample projections"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-token-stamp"
                - "memory.md#mem-obj-rollout"
              note: "Exact IDs and per-token fields use explicit localized rules."
          records:
            - "memory.md#mem-obj-token-stamp"
            - "memory.md#mem-obj-rollout"
          note: "Numerical log probabilities are recorded scores, not distributed learned parameters."
        -
          scope: "Persisted settings and credential lookup fields"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-settings-load"
                - "memory.md#mem-obj-credentials"
              note: "Configuration keys and provider/field mappings feed deterministic consumers."
          records:
            - "runtime.md#rt-bap-settings-load"
            - "memory.md#mem-obj-credentials"
          note: "Secrets are opaque values in a fixed access mechanism, not natural-language knowledge."
        -
          scope: "Retained serving policy reached through weight replacement"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-rte-weight-update"
                - "runtime.md#rt-cmp-llm"
              note: "The later serving component consumes model parameters; provenance and service acceptance remain unresolved."
          records:
            - "memory.md#mem-rte-weight-update"
            - "runtime.md#rt-cmp-llm"
          note: "The parameter form is established without asserting its physical storage or observed replacement."
        -
          scope: "Other provider state and remote diagnostic payloads"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-llm"
            - "memory.md#mem-obj-atif-trajectory"
          note: "The recorded local projections do not reveal all operative remote payload forms."
      records:
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-obj-helper-history"
        - "memory.md#mem-obj-readline-history"
        - "memory.md#mem-obj-atif-trajectory"
        - "memory.md#mem-obj-trajectory-directory"
        - "runtime.md#rt-rte-workflow-emission"
        - "memory.md#mem-obj-token-stamp"
        - "memory.md#mem-obj-rollout"
        - "runtime.md#rt-bap-settings-load"
        - "memory.md#mem-obj-credentials"
        - "memory.md#mem-rte-weight-update"
        - "runtime.md#rt-cmp-llm"
      note: "Mixed text and symbolic parts are split by consumer; arbitrary live and remote payloads prevent complete coverage."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Console turn and helper exchange records derived from interaction"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-history"
                - "memory.md#mem-obj-helper-history"
              note: "Runtime records preserve work-session activity, including failure and rejected proposals."
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-obj-helper-history"
          note: "The record structure is software-produced from prompts, outcomes, proposals and permission state."
        -
          scope: "Original arbitrary payloads retained by reference in main conversation history"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-conversation-history"
          note: "Recording a value establishes the capture path, not its original authorship or derivation."
        -
          scope: "Typed input lines and operator-supplied settings/credentials"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-readline-history"
                - "runtime.md#rt-bap-settings-load"
                - "memory.md#mem-obj-credentials"
                - "runtime.md#rt-rte-settings-admission"
              note: "User supplies lines, directly edits configuration or supplies credentials; helper-produced alternatives are separate."
          records:
            - "memory.md#mem-obj-readline-history"
            - "runtime.md#rt-bap-settings-load"
            - "memory.md#mem-obj-credentials"
            - "runtime.md#rt-rte-settings-admission"
          note: "Explicit user content and human-admitted helper changes have distinct origins."
        -
          scope: "Human-confirmed helper snippet used to change persisted settings"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-admission"
                - "runtime.md#rt-bap-settings-load"
              note: "Model-produced settings proposals are compiled from supplied context, not necessarily extracted solely from traces."
          records:
            - "runtime.md#rt-rte-settings-admission"
            - "runtime.md#rt-bap-settings-load"
          note: "The model proposes code from request/configuration/transcript inputs; confirmation admits it."
        -
          scope: "ATIF, directory recorder, token sidecars, frozen rollouts and event-derived workflow code"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-atif-trajectory"
                - "memory.md#mem-obj-trajectory-directory"
                - "memory.md#mem-obj-token-stamp"
                - "memory.md#mem-obj-rollout"
                - "runtime.md#rt-rte-workflow-emission"
              note: "Capture, event projection and code materialization derive retained parts from runtime traces."
          records:
            - "memory.md#mem-obj-atif-trajectory"
            - "memory.md#mem-obj-trajectory-directory"
            - "memory.md#mem-obj-token-stamp"
            - "memory.md#mem-obj-rollout"
            - "runtime.md#rt-rte-workflow-emission"
          note: "These derivations use recorded invocation/query/execution activity."
        -
          scope: "Offline ATIF-to-directory projection"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory-directory"
              note: "Diagnostic files can be compiled from an already retained ATIF document."
          records:
            - "memory.md#mem-obj-trajectory-directory"
          note: "The converter changes representation rather than establishing a new source event."
        -
          scope: "Weights supplied to update-from-disk/tensor/distributed wrappers"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-rte-weight-update"
              note: "External caller supplies replacement policy content to the serving-engine transport."
          records:
            - "memory.md#mem-rte-weight-update"
          note: "Only acquisition of externally chosen candidates is established, not training provenance."
        -
          scope: "Initial serving-policy derivation, proposed weight training history and other remote retained parts"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-weight-update"
            - "runtime.md#rt-cmp-llm"
          note: "Neither export coexistence nor an update method establishes the candidate training inputs or initial model lineage."
      records:
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-obj-helper-history"
        - "memory.md#mem-obj-readline-history"
        - "runtime.md#rt-bap-settings-load"
        - "memory.md#mem-obj-credentials"
        - "runtime.md#rt-rte-settings-admission"
        - "memory.md#mem-obj-atif-trajectory"
        - "memory.md#mem-obj-trajectory-directory"
        - "memory.md#mem-obj-token-stamp"
        - "memory.md#mem-obj-rollout"
        - "runtime.md#rt-rte-workflow-emission"
        - "memory.md#mem-rte-weight-update"
        - "runtime.md#rt-cmp-llm"
      note: "Capture paths are known locally; original opaque values and policy-training provenance remain unresolved. Imported parameters do not imply trace learning."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Main/history text and live prior objects at later main-agent consumer"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-history"
                - "runtime.md#rt-rte-console-turn"
              note: "Previous prompts/results and accessible objects supply context, not validated facts or higher-priority instructions."
          records:
            - "memory.md#mem-obj-conversation-history"
            - "runtime.md#rt-rte-console-turn"
          note: "Retained data can inform later code selection; delivery does not prove reliance."
        -
          scope: "Helper proposal/confirmation and main transcripts at later helper model"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-helper-history"
                - "runtime.md#rt-rte-settings-admission"
              note: "Rendered prior exchanges inform later help/settings requests; applied does not certify success."
          records:
            - "memory.md#mem-obj-helper-history"
            - "runtime.md#rt-rte-settings-admission"
          note: "Proposals, rejections and permission state are delivered as context."
        -
          scope: "Saved response source at replay protocol/executor"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-trajectory-replay"
                - "memory.md#mem-obj-atif-trajectory"
              note: "Retained Python response supplies the actions the parser/executor will execute, rather than examples for model training."
          records:
            - "runtime.md#rt-rte-trajectory-replay"
            - "memory.md#mem-obj-atif-trajectory"
          note: "Responses substitute for a model completion; code admission remains downstream."
        -
          scope: "Recorded expectations at replay comparison and serving latch"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-replay-comparison"
                - "runtime.md#rt-rte-trajectory-replay"
              note: "Saved edit/content/observation expectations are criteria for divergence checks."
            -
              value: "routing"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-replay-comparison"
                - "runtime.md#rt-rte-trajectory-replay"
              note: "Queue position and divergence state select saved-response service versus live completion."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-replay-comparison"
                - "runtime.md#rt-rte-trajectory-replay"
              note: "A diverged node is refused further saved-response delivery; this is not rollback of earlier effects."
          records:
            - "epistemic.md#epi-rte-replay-comparison"
            - "runtime.md#rt-rte-trajectory-replay"
          note: "Check domain is representation agreement, not answer truth."
        -
          scope: "Generated workflow code at intended later Python executor"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-workflow-emission"
              note: "Executable retained code determines later actions if the generated program is run."
          records:
            - "runtime.md#rt-rte-workflow-emission"
          note: "Emission is wired; later execution is a distinct documented affordance."
        -
          scope: "Frozen samples at documented external trainer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-rollout-export"
                - "memory.md#mem-obj-rollout"
              note: "Recorded examples can feed an external parameter update; actual ingestion and benefits are not observed."
          records:
            - "memory.md#mem-rte-rollout-export"
            - "memory.md#mem-obj-rollout"
          note: "The training role is documented; no shipped trainer-to-serving closure is established."
        -
          scope: "Stored backend/model choice at later console startup"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-settings-load"
                - "runtime.md#rt-rte-settings-admission"
              note: "Reloaded backend/model determines which component handles later invocations."
          records:
            - "runtime.md#rt-bap-settings-load"
            - "runtime.md#rt-rte-settings-admission"
          note: "Only the recorded provider-selection consumer is classified, not all hypothetical configuration leaves."
        -
          scope: "Stored credential at backend access consumer"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-credentials"
              note: "Retained secret authorizes provider access, not knowledge or learned policy."
          records:
            - "memory.md#mem-obj-credentials"
          note: "Lookup is wired; all backend precedence is not established."
        -
          scope: "Readline retained lines at interactive recall/editor"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-readline-history"
              note: "Past command text is available as reference for recall/edit and possible resubmission."
          records:
            - "memory.md#mem-obj-readline-history"
          note: "Human recall is not automatic agent guidance."
        -
          scope: "Arbitrary live payload consumers, complete remote policy effects and remote trace readers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-rte-weight-update"
            - "runtime.md#rt-cmp-llm"
          note: "Their actual content/effect or later consumption is not determined; known transcript and local consumers do not close these alternatives."
      records:
        - "memory.md#mem-obj-conversation-history"
        - "runtime.md#rt-rte-console-turn"
        - "memory.md#mem-obj-helper-history"
        - "runtime.md#rt-rte-settings-admission"
        - "runtime.md#rt-rte-trajectory-replay"
        - "memory.md#mem-obj-atif-trajectory"
        - "epistemic.md#epi-rte-replay-comparison"
        - "runtime.md#rt-rte-workflow-emission"
        - "memory.md#mem-rte-rollout-export"
        - "memory.md#mem-obj-rollout"
        - "runtime.md#rt-bap-settings-load"
        - "memory.md#mem-obj-credentials"
        - "memory.md#mem-obj-readline-history"
        - "memory.md#mem-rte-weight-update"
        - "runtime.md#rt-cmp-llm"
      note: "Authority follows actual recorded consumers, with afforded training/workflow consumers kept below wired status. No ranking finding follows from nonempty-history selection."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Console/history append, line retention, recorders and workflow emission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-history"
                - "memory.md#mem-obj-helper-history"
                - "memory.md#mem-obj-readline-history"
                - "memory.md#mem-obj-atif-trajectory"
                - "memory.md#mem-obj-trajectory-directory"
                - "memory.md#mem-obj-token-stamp"
                - "memory.md#mem-obj-rollout"
                - "runtime.md#rt-rte-workflow-emission"
              note: "Software admits turn outcomes, proposals/permission records, trace projections and generated artifacts without per-record approval."
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-obj-helper-history"
            - "memory.md#mem-obj-readline-history"
            - "memory.md#mem-obj-atif-trajectory"
            - "memory.md#mem-obj-trajectory-directory"
            - "memory.md#mem-obj-token-stamp"
            - "memory.md#mem-obj-rollout"
            - "runtime.md#rt-rte-workflow-emission"
          note: "Activating a recorder or typing a request does not approve each subsequent retained record."
        -
          scope: "Direct settings edits, confirmed helper settings changes and user-supplied credentials"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-settings-load"
                - "runtime.md#rt-rte-settings-admission"
                - "memory.md#mem-obj-credentials"
              note: "User edits/supplies content or explicitly confirms the helper snippet before host execution."
          records:
            - "runtime.md#rt-bap-settings-load"
            - "runtime.md#rt-rte-settings-admission"
            - "memory.md#mem-obj-credentials"
          note: "Content-specific operator decision is evidenced for these mechanisms."
        -
          scope: "External replacement-weight admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-weight-update"
          note: "Caller identity does not determine human approval; server acceptance is external. Neither manual nor automatic admission control is established."
        -
          scope: "Opaque input initialization and other provider/remote retained writes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-conversation-history"
            - "runtime.md#rt-cmp-llm"
          note: "Known software capture does not resolve original payload admission or provider-internal writes."
      records:
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-obj-helper-history"
        - "memory.md#mem-obj-readline-history"
        - "memory.md#mem-obj-atif-trajectory"
        - "memory.md#mem-obj-trajectory-directory"
        - "memory.md#mem-obj-token-stamp"
        - "memory.md#mem-obj-rollout"
        - "runtime.md#rt-rte-workflow-emission"
        - "runtime.md#rt-bap-settings-load"
        - "runtime.md#rt-rte-settings-admission"
        - "memory.md#mem-obj-credentials"
        - "memory.md#mem-rte-weight-update"
        - "runtime.md#rt-cmp-llm"
      note: "Automatic recording and manual settings/access-content admission coexist; parameter replacement and opaque initialization control remain unresolved."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Readline entry cap over retained command history"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-obj-readline-history"
              note: "The persisted line history is capped at 1000 entries; this does not establish semantic relevance selection."
          records:
            - "memory.md#mem-obj-readline-history"
          note: "The configured retained history limit is an implemented forgetting operation."
        -
          scope: "Persisted settings/credential replacement"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-settings-load"
                - "memory.md#mem-obj-credentials"
                - "runtime.md#rt-rte-settings-admission"
              note: "Settings overwrite/edit and credential rotation replace retained content, without demonstrating improvement."
          records:
            - "runtime.md#rt-bap-settings-load"
            - "memory.md#mem-obj-credentials"
            - "runtime.md#rt-rte-settings-admission"
          note: "Content-specific edits revise existing retained entries."
        -
          scope: "Saved-response reliance after replay divergence"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-replay-comparison"
                - "runtime.md#rt-rte-trajectory-replay"
              note: "Divergence stops reliance on remaining saved responses for that node, without deleting its trace."
          records:
            - "epistemic.md#epi-rte-replay-comparison"
            - "runtime.md#rt-rte-trajectory-replay"
          note: "The source trace remains while future serving is withdrawn."
        -
          scope: "Workflow materialization, rollout projections and diagnostic rendering as semantic curation"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-workflow-emission"
            - "memory.md#mem-rte-rollout-export"
            - "memory.md#mem-obj-atif-trajectory"
            - "memory.md#mem-obj-trajectory-directory"
          note: "Transformation and structural eligibility checks are recorded, but do not determine consolidation of claims, deduplication or synthesis. Routine projection alone is not a controlled curation operation."
        -
          scope: "Opaque payload, remote traces and serving-policy maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-conversation-history"
            - "runtime.md#rt-cmp-llm"
            - "memory.md#mem-rte-weight-update"
          note: "No complete recorded account determines transformations of these included parts."
      records:
        - "memory.md#mem-obj-readline-history"
        - "runtime.md#rt-bap-settings-load"
        - "memory.md#mem-obj-credentials"
        - "runtime.md#rt-rte-settings-admission"
        - "epistemic.md#epi-rte-replay-comparison"
        - "runtime.md#rt-rte-trajectory-replay"
        - "runtime.md#rt-rte-workflow-emission"
        - "memory.md#mem-rte-rollout-export"
        - "memory.md#mem-obj-atif-trajectory"
        - "memory.md#mem-obj-trajectory-directory"
        - "memory.md#mem-obj-conversation-history"
        - "runtime.md#rt-cmp-llm"
        - "memory.md#mem-rte-weight-update"
      note: "Local decay, revision and withdrawal have separate warrants. Observation truncation of current-run context is excluded; acquisition and index/projection machinery do not imply consolidation or synthesis."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Later main-agent and helper invocation history supply"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-history"
                - "memory.md#mem-obj-helper-history"
                - "runtime.md#rt-rte-console-turn"
              note: "Nonempty history and constructed transcript text enter new invocation inputs without a request to retrieve particular prior turns."
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-obj-helper-history"
            - "runtime.md#rt-rte-console-turn"
          note: "Supply occurs automatically when history exists; later payload inspection is separate."
        -
          scope: "Later model-written access to specific live history values"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-history"
                - "runtime.md#rt-rte-console-turn"
              note: "Code can request/index/print retained live values when supplied history is reachable."
          records:
            - "memory.md#mem-obj-conversation-history"
            - "runtime.md#rt-rte-console-turn"
          note: "Requested inspection is not another automatic transcript push."
        -
          scope: "Interactive readline recall"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-readline-history"
              note: "Interactive user requests prior retained input lines for editing/resubmission."
          records:
            - "memory.md#mem-obj-readline-history"
          note: "Recall is a consumer request rather than automatic prompt injection."
        -
          scope: "Host-requested ATIF loading and automatic response serving"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-trajectory-replay"
                - "memory.md#mem-obj-atif-trajectory"
              note: "Host explicitly chooses and loads an ATIF trace."
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-trajectory-replay"
                - "memory.md#mem-obj-atif-trajectory"
              note: "At later query Send, node/cursor/availability and divergence select a saved response without a content-retrieval request by the executing agent."
          records:
            - "runtime.md#rt-rte-trajectory-replay"
            - "memory.md#mem-obj-atif-trajectory"
          note: "The explicit source choice and automatic serving operation are distinct."
        -
          scope: "Console settings reload and credential access"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-settings-load"
                - "memory.md#mem-obj-credentials"
              note: "Console startup automatically applies stored backend/model choices."
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-settings-load"
                - "memory.md#mem-obj-credentials"
              note: "Credential getter fulfills the backend request for a provider/field value."
          records:
            - "runtime.md#rt-bap-settings-load"
            - "memory.md#mem-obj-credentials"
          note: "Startup configuration delivery is separate from requested provider/field lookup."
        -
          scope: "Generated program and diagnostic-file consumers"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-workflow-emission"
                - "memory.md#mem-obj-trajectory-directory"
              note: "Consumer chooses a generated program to execute or diagnostic files to inspect."
          records:
            - "runtime.md#rt-rte-workflow-emission"
            - "memory.md#mem-obj-trajectory-directory"
          note: "Intended later execution and human inspection are afforded, not observed."
        -
          scope: "External training driver requesting rollout export"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-rollout-export"
              note: "External driver explicitly obtains sample projections for training."
          records:
            - "memory.md#mem-rte-rollout-export"
          note: "Export APIs document a requesting training role, not automatic installation."
        -
          scope: "Other provider/remote retained state and later service-policy consumption"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-llm"
            - "memory.md#mem-rte-weight-update"
          note: "No complete recorded request/selection/delivery chain classifies every remote alternative."
      records:
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-obj-helper-history"
        - "runtime.md#rt-rte-console-turn"
        - "memory.md#mem-obj-readline-history"
        - "runtime.md#rt-rte-trajectory-replay"
        - "memory.md#mem-obj-atif-trajectory"
        - "runtime.md#rt-bap-settings-load"
        - "memory.md#mem-obj-credentials"
        - "runtime.md#rt-rte-workflow-emission"
        - "memory.md#mem-obj-trajectory-directory"
        - "memory.md#mem-rte-rollout-export"
        - "runtime.md#rt-cmp-llm"
        - "memory.md#mem-rte-weight-update"
      note: "Both request-driven access and independent automatic supply are supported. Unresolved remote consumers prevent a complete pull-only or push-only conclusion."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Later console/history push"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-history"
                - "memory.md#mem-obj-helper-history"
                - "runtime.md#rt-rte-console-turn"
              note: "Nonemptiness selects whole histories; caps are display budgets, not relevance or identifier matching."
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-obj-helper-history"
            - "runtime.md#rt-rte-console-turn"
          note: "Trigger: next prompt/helper invocation. Input: history availability. Selected part: all prior turns/transcripts, with per-value display caps."
        -
          scope: "Replay response push"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-trajectory-replay"
                - "memory.md#mem-obj-atif-trajectory"
                - "epistemic.md#epi-rte-replay-comparison"
              note: "Sequential availability and divergence gating select the next queued response; the chosen filename alone is not identifier-targeted push."
          records:
            - "runtime.md#rt-rte-trajectory-replay"
            - "memory.md#mem-obj-atif-trajectory"
            - "epistemic.md#epi-rte-replay-comparison"
          note: "Trigger: LLMQuerySend. Inputs: chosen invocation-tree position, response cursor, availability and optional divergence. Selected part: next saved response."
        -
          scope: "Settings startup push"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-settings-load"
              note: "Startup applies available configuration, without task-specific semantic or identity retrieval."
          records:
            - "runtime.md#rt-bap-settings-load"
          note: "Trigger: console startup. Input: presence/validity of stored settings. Selected part: persisted console configuration."
        -
          scope: "Provider/remote push alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-llm"
            - "memory.md#mem-rte-weight-update"
          note: "Missing selectors and payload delivery prevent determining whether targeted or other coarse push exists."
      records:
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-obj-helper-history"
        - "runtime.md#rt-rte-console-turn"
        - "runtime.md#rt-rte-trajectory-replay"
        - "memory.md#mem-obj-atif-trajectory"
        - "epistemic.md#epi-rte-replay-comparison"
        - "runtime.md#rt-bap-settings-load"
        - "runtime.md#rt-cmp-llm"
        - "memory.md#mem-rte-weight-update"
      note: "Signals classify push operations only. Requested credential lookup, history indexing and file/export access do not acquire push signals from their identifiers."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Automatic runtime-event to workflow-package production and intended later execution"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-workflow-emission"
              note: "Trace-fed materialization produces an executable artifact for later Python consumption. The later-consumer route is afforded, not observed."
          records:
            - "runtime.md#rt-rte-workflow-emission"
          note: "The emitter writes durable behavior-shaping Python, even on abnormal exit; no automatic installation or benefit is asserted."
        -
          scope: "Token trace to training samples and documented external trainer"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-rollout-export"
                - "memory.md#mem-obj-token-stamp"
                - "memory.md#mem-obj-rollout"
              note: "Retained trace-derived samples afford a parameter-update consumer; this classification does not join export to the independent SGLang update transport."
          records:
            - "memory.md#mem-rte-rollout-export"
            - "memory.md#mem-obj-token-stamp"
            - "memory.md#mem-obj-rollout"
          note: "Software admission and projection are wired; actual trainer/update closure is not."
        -
          scope: "Raw console, line, text trajectory and diagnostic histories as qualifying durable updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-obj-helper-history"
            - "memory.md#mem-obj-readline-history"
            - "memory.md#mem-obj-atif-trajectory"
            - "memory.md#mem-obj-trajectory-directory"
            - "runtime.md#rt-rte-trajectory-replay"
          note: "Raw logging/context delivery and saved-response serving alone do not establish a qualifying transformed durable artifact; no bounded absence record licenses a local no."
        -
          scope: "Settings proposals influenced by transcripts"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-settings-admission"
            - "runtime.md#rt-bap-settings-load"
            - "memory.md#mem-obj-helper-history"
          note: "Human confirmation is required on the evidenced helper write path; no bounded automatic trace-fed update inventory or absence record establishes a controlled trace-learning value here."
        -
          scope: "Replacement-policy provenance and other provider/remote update routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-weight-update"
            - "runtime.md#rt-cmp-llm"
          note: "Candidate trace inputs, training control and remote durable update consumers remain unresolved."
      records:
        - "runtime.md#rt-rte-workflow-emission"
        - "memory.md#mem-rte-rollout-export"
        - "memory.md#mem-obj-token-stamp"
        - "memory.md#mem-obj-rollout"
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-obj-helper-history"
        - "memory.md#mem-obj-readline-history"
        - "memory.md#mem-obj-atif-trajectory"
        - "memory.md#mem-obj-trajectory-directory"
        - "runtime.md#rt-rte-trajectory-replay"
        - "runtime.md#rt-rte-settings-admission"
        - "runtime.md#rt-bap-settings-load"
        - "memory.md#mem-rte-weight-update"
        - "runtime.md#rt-cmp-llm"
      note: "Afforded positive routes support a partial yes union, not wired training, observed learning or benefit. No evidenced-absence records support a local or system-wide no."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Workflow materialization input"
          assessment: "known"
          findings:
            -
              value: "tool-traces"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-workflow-emission"
              note: "REPL execution requests/results and code-bearing invocation/query/REPL activity feed durable workflow generation."
            -
              value: "session-logs"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-workflow-emission"
              note: "Model-generated code from recorded query/execution turns is retained in the generated program; wrapping these turns in hook callbacks does not add event-stream provenance."
          records:
            - "runtime.md#rt-rte-workflow-emission"
          note: "Classify actual original hook content, not merely event-callback serialization."
        -
          scope: "Rollout training-sample input: conversational content"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-rollout-export"
                - "memory.md#mem-obj-token-stamp"
                - "memory.md#mem-obj-rollout"
              note: "Recorded conversational conditioning and sampled agent responses supply training examples."
          records:
            - "memory.md#mem-rte-rollout-export"
            - "memory.md#mem-obj-token-stamp"
            - "memory.md#mem-obj-rollout"
          note: "The sidecar retains tokenized sent messages and model responses; external trainer is afforded."
        -
          scope: "Other original conditioning content within rollout tokens"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-token-stamp"
            - "memory.md#mem-obj-rollout"
            - "memory.md#mem-rte-rollout-export"
          note: "Sample IDs and masks alone do not enumerate whether tool feedback, environmental event content or linked state/action/outcome experience occurs in all original inputs. Do not infer event-streams from hook delivery."
        -
          scope: "Raw histories, helper settings and remote policy-update alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-obj-helper-history"
            - "runtime.md#rt-rte-settings-admission"
            - "memory.md#mem-rte-weight-update"
            - "runtime.md#rt-cmp-llm"
          note: "Qualification or original trace provenance is unresolved; these units are not made inapplicable by known local exports."
      records:
        - "runtime.md#rt-rte-workflow-emission"
        - "memory.md#mem-rte-rollout-export"
        - "memory.md#mem-obj-token-stamp"
        - "memory.md#mem-obj-rollout"
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-obj-helper-history"
        - "runtime.md#rt-rte-settings-admission"
        - "memory.md#mem-rte-weight-update"
        - "runtime.md#rt-cmp-llm"
      note: "Supported original source content is retained, with mixed/opaque inputs unresolved. No complete trace-source union or event-stream/trajectory classification follows from the word trajectory."
---

# JAZ memory profile

## Comparison rationale

The comparison concerns retained use-derived material, not every object in the runtime. The local witnesses do not settle arbitrary live Python payloads, provider state or remote trace alternatives. All ten axes therefore retain partial inventory coverage rather than converting implementation witnesses into complete-value claims. Unresolved remote trace parts are carried as coverage limits: the accepted records do not supply a canonical remote-payload declaration from which to classify them.

The console supplies both an automatic transcript/history path and a later requested object-access path. The main-history display cannot classify the form or provenance of its opaque live values. The helper instead receives rendered transcripts, including rejected proposals and permission state; these are context, not validated knowledge. See [MEM-OBJ-conversation-history](memory.md#mem-obj-conversation-history), [MEM-OBJ-helper-history](memory.md#mem-obj-helper-history) and [RT-RTE-console-turn](runtime.md#rt-rte-console-turn).

Replay is not semantic retrieval or model training. A requested trace load is followed by automatic sequential saved-response selection. Saved source supplies executable directions; saved comparison expectations supply validation criteria; the divergence latch routes continuation and vetoes further saved service. Queue exhaustion is not forgetting the trace. See [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay), [EPI-RTE-replay-comparison](epistemic.md#epi-rte-replay-comparison) and [MEM-OBJ-atif-trajectory](memory.md#mem-obj-atif-trajectory).

Generated workflow code is a trace-fed durable behavior-shaping artifact with an afforded later Python consumer. Its positive trace-learning finding does not require new claims, autonomous installation, observed execution or improved capacity. The training sample route likewise retains an afforded update consumer, not a wired end-to-end trainer. No accepted evidenced-absence record supports a local trace-learning negative. The unresolved update inventory prevents complete classification independently of these positive witnesses. See [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission), [MEM-RTE-rollout-export](memory.md#mem-rte-rollout-export) and [MEM-RTE-weight-update](memory.md#mem-rte-weight-update).

The reconciliation supersedes the epistemic rollout object and export-route identities with the memory declarations. All classification citations use the canonical [MEM-OBJ-rollout](memory.md#mem-obj-rollout) and [MEM-RTE-rollout-export](memory.md#mem-rte-rollout-export). Their structural eligibility checks do not certify token provenance, reward, training success or accepted knowledge. Neither supersession connects export to the independent weight-update transport.

Readline retention caps support local decay; settings/credential edits support revision; replay divergence supports withdrawal of reliance while preserving the trace. These do not turn routine event projection into semantic consolidation or synthesis. Current-run observation abbreviation and advisory context warnings are outside the retained-memory curation findings. See [MEM-OBJ-readline-history](memory.md#mem-obj-readline-history), [MEM-OBJ-credentials](memory.md#mem-obj-credentials), [RT-BAP-settings-load](runtime.md#rt-bap-settings-load) and [RT-RTE-context-control](runtime.md#rt-rte-context-control).

Source-read log: no source files were read. Classification uses only the supplied accepted members and their records; no evidence or records were added. Implementation and documented affordances establish neither observed activation nor causal benefit.
