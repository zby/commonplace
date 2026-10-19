---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Memory profile of JAZ: session objects, recorded execution reuse, workflow derivatives and unresolved external training at the frozen distribution boundary."
run-id: "AAS-2026-10-15-jaz-a94bea79c61a-01"
source-identity: "https://github.com/jaz-lang/JAZ"
reviewed-boundary: "0803d4971be785e95b80054b02259664d70fa3da"
memory-comparison:
  version: 2
  scope: "Retained console main/helper histories and opaque live result parts; ATIF state/files and replay selectors; generated workflow programs; token rollouts/sample exports; diagnostic trace derivatives; changed persisted console configuration; external weight/trainer alternatives only to the extent identified by accepted records. Excludes ordinary current-invocation messages/REPL state, static shipped prompts, credentials and readline command recall, arbitrary application stores and unspecified custom hooks. Remote telemetry is not established as later-consumer memory; its external retention remains unclassified."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Console main and helper session containers"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-history"
                - "memory.md#mem-obj-helper-history"
              note: "Session-owned lists retain live objects and exchange strings."
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-obj-helper-history"
            - "memory.md#mem-rte-session-history"
          note: "These containers are session-local; no serialized object reload is established."
        - scope: "ATIF recorder state and optional JSON file"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-atif-trace"
                - "memory.md#mem-rte-trace-recording"
              note: "Recorder state precedes document serialization."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-atif-trace"
                - "memory.md#mem-rte-trace-recording"
              note: "Configured teardown writes a JSON artifact consumed by replay."
          records:
            - "memory.md#mem-obj-atif-trace"
            - "memory.md#mem-rte-trace-recording"
            - "runtime.md#rt-rte-trajectory-replay"
          note: "Both retained forms are documented; neither is a namespace checkpoint."
        - scope: "Generated workflows and diagnostic displays"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-workflow-emission"
                - "memory.md#mem-rte-trace-display"
              note: "Workflow emission and diagnostic converters write source/log/Markdown files."
          records:
            - "runtime.md#rt-rte-workflow-emission"
            - "memory.md#mem-rte-trace-display"
          note: "These local outputs are distinct from remote telemetry."
        - scope: "Rollout token records and sample objects"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-rollout"
                - "memory.md#mem-rte-rollout-export"
              note: "Frozen rollouts and exported samples are caller-held Python values."
          records:
            - "memory.md#mem-obj-rollout"
            - "memory.md#mem-rte-rollout-export"
          note: "Durable external sample persistence belongs to the unresolved trainer boundary."
        - scope: "Changed console model/backend defaults"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-user-settings"
                - "epistemic.md#epi-rte-model-ping"
              note: "Successful switch attempts settings JSON persistence for later console startup."
          records:
            - "memory.md#mem-obj-user-settings"
            - "epistemic.md#epi-rte-model-ping"
          note: "Failed persistence can leave only a live switch; file storage is not guaranteed for each action."
        - scope: "Opaque live results retained by ConversationHistory"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-conversation-history"
          note: "The container substrate is known, but arbitrary host payload internals and external backing are not classified."
        - scope: "External parameter state, trainer retention and provider caches"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-model-backend"
            - "memory.md#mem-rte-weight-transport"
            - "memory.md#mem-rte-rollout-export"
          note: "JAZ exposes transport and samples, not frozen server storage or trainer persistence; model-weights, service-object or other substrates cannot be inferred."
      records:
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-obj-helper-history"
        - "memory.md#mem-rte-session-history"
        - "memory.md#mem-obj-atif-trace"
        - "memory.md#mem-rte-trace-recording"
        - "runtime.md#rt-rte-trajectory-replay"
        - "runtime.md#rt-rte-workflow-emission"
        - "memory.md#mem-rte-trace-display"
        - "memory.md#mem-obj-rollout"
        - "memory.md#mem-rte-rollout-export"
        - "memory.md#mem-obj-user-settings"
        - "epistemic.md#epi-rte-model-ping"
        - "runtime.md#rt-cmp-model-backend"
        - "memory.md#mem-rte-weight-transport"
      note: "Inventory covers session histories, traces, derivatives, samples and changed defaults; opaque object backing and external retention prevent complete substrate coverage."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Main prompts and displayed history; helper transcript strings at model interpretation"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-history"
                - "memory.md#mem-obj-helper-history"
                - "memory.md#mem-rte-session-history"
              note: "Prompt, answer and rendered transcript content is interpreted by later agents, including snippets quoted as history."
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-obj-helper-history"
            - "memory.md#mem-rte-session-history"
          note: "A code string quoted as prior context is not automatically executed."
        - scope: "History bindings, result access structure, helper tags and admission flags"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-history"
                - "memory.md#mem-obj-helper-history"
              note: "Fixed Python access and formatting rules consume bindings, tags and flags."
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-obj-helper-history"
          note: "This classifies structure, not arbitrary result internals."
        - scope: "ATIF instructions/observations at interpretive display consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-atif-trace"
                - "memory.md#mem-rte-trace-display"
              note: "Retained conversation prose reaches diagnostic interpretation."
          records:
            - "memory.md#mem-obj-atif-trace"
            - "memory.md#mem-rte-trace-display"
          note: "The displayed namespace repr is not the original object payload."
        - scope: "ATIF response source and access metadata at replay"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-atif-trace"
                - "runtime.md#rt-rte-trajectory-replay"
              note: "Response code enters Python parsing/execution; tree, cursor and comparison metadata have fixed-rule consumers."
          records:
            - "memory.md#mem-obj-atif-trace"
            - "runtime.md#rt-rte-trajectory-replay"
          note: "Code execution and metadata selection differ from prose interpretation."
        - scope: "Generated workflow source at standalone executor"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-workflow-emission"
              note: "Functions and entry blocks afford native Python execution."
          records:
            - "runtime.md#rt-rte-workflow-emission"
          note: "Emission is wired; later standalone execution is afforded, not observed."
        - scope: "Rollout IDs, masks, spans and localized logprob measurements"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-rollout"
                - "memory.md#mem-rte-rollout-export"
              note: "Fixed projection rules consume token and numerical record fields, not distributed learned weights."
          records:
            - "memory.md#mem-obj-rollout"
            - "memory.md#mem-rte-rollout-export"
          note: "Numerical measurements alone do not establish parametric memory."
        - scope: "Persisted console configuration at startup loader"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-user-settings"
              note: "Parsed settings select and construct configured components."
          records:
            - "memory.md#mem-obj-user-settings"
          note: "Configuration strings have fixed configuration consumers."
        - scope: "External model weight representation"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "afforded"
              records:
                - "runtime.md#rt-cmp-model-backend"
                - "memory.md#mem-rte-weight-transport"
              note: "Records identify external distributed-parametric weights; update transport does not expose their content."
          records:
            - "runtime.md#rt-cmp-model-backend"
            - "memory.md#mem-rte-weight-transport"
          note: "Form is identified independently of unknown storage, version and update policy."
        - scope: "Arbitrary live result payloads and externally persisted trainer state"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-rte-rollout-export"
          note: "Lossy repr displays do not classify consumed opaque host internals; external trainer artifacts are unspecified."
      records:
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-obj-helper-history"
        - "memory.md#mem-rte-session-history"
        - "memory.md#mem-obj-atif-trace"
        - "memory.md#mem-rte-trace-display"
        - "runtime.md#rt-rte-trajectory-replay"
        - "runtime.md#rt-rte-workflow-emission"
        - "memory.md#mem-obj-rollout"
        - "memory.md#mem-rte-rollout-export"
        - "memory.md#mem-obj-user-settings"
        - "runtime.md#rt-cmp-model-backend"
        - "memory.md#mem-rte-weight-transport"
      note: "Known text, fixed-rule structures and external parametric form coexist; opaque result content and trainer artifacts remain unresolved."
    lineage:
      assessment: "partial"
      units:
        - scope: "Original user prompts retained in main and helper histories"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-history"
                - "memory.md#mem-obj-helper-history"
                - "memory.md#mem-rte-session-history"
              note: "Console histories preserve user-authored requests without a summarizing model."
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-obj-helper-history"
            - "memory.md#mem-rte-session-history"
          note: "This lineage finding concerns request text, not the mixed result payloads."
        - scope: "Recorded session results, helper responses and ATIF conversation/event records"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-history"
                - "memory.md#mem-rte-trace-recording"
                - "memory.md#mem-obj-atif-trace"
              note: "Software captures conversation and execution records, including failures."
          records:
            - "memory.md#mem-rte-session-history"
            - "memory.md#mem-rte-trace-recording"
            - "memory.md#mem-obj-atif-trace"
          note: "Recorded origin does not authenticate the source assertions or arbitrary payload provenance."
        - scope: "Workflow derivative and diagnostic conversions"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-workflow-emission"
                - "memory.md#mem-rte-trace-display"
              note: "Programs and displays derive from recorded execution-associated content."
          records:
            - "runtime.md#rt-rte-workflow-emission"
            - "memory.md#mem-rte-trace-display"
          note: "Program materialization preserves trace ancestry without certifying equivalence."
        - scope: "Rollout token records and derived sample projections"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-rollout"
                - "memory.md#mem-rte-rollout-export"
              note: "Backend query traces feed retained token records and sample projections."
          records:
            - "memory.md#mem-obj-rollout"
            - "memory.md#mem-rte-rollout-export"
          note: "Backend model labels and stamps are trusted premises, not authenticated weight provenance."
        - scope: "Console-persisted model/backend selection"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-user-settings"
                - "epistemic.md#epi-rte-model-ping"
              note: "Software projects the selected component into persisted configuration fields."
          records:
            - "memory.md#mem-obj-user-settings"
            - "epistemic.md#epi-rte-model-ping"
          note: "This path is known independently of the initial settings-file provenance."
        - scope: "Initial settings content, arbitrary result internals and loaded weights"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-user-settings"
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-rte-weight-transport"
            - "runtime.md#rt-cmp-model-backend"
          note: "Existing-file authorship is not verified; opaque payload derivations and external weight provenance are not supplied. Manual file authorship is an available path, not verified origin for all existing content."
      records:
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-obj-helper-history"
        - "memory.md#mem-rte-session-history"
        - "memory.md#mem-rte-trace-recording"
        - "memory.md#mem-obj-atif-trace"
        - "runtime.md#rt-rte-workflow-emission"
        - "memory.md#mem-rte-trace-display"
        - "memory.md#mem-obj-rollout"
        - "memory.md#mem-rte-rollout-export"
        - "memory.md#mem-obj-user-settings"
        - "epistemic.md#epi-rte-model-ping"
        - "memory.md#mem-rte-weight-transport"
        - "runtime.md#rt-cmp-model-backend"
      note: "Trace-derived and explicitly authored parts retain separate lineage; known subsequent projections do not resolve initialization or external model provenance."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Rendered main/helper history at later model consumer"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-history"
                - "memory.md#mem-obj-helper-history"
              note: "Prior requests, results and admission status supply context or evidence to the next model invocation."
          records:
            - "memory.md#mem-rte-session-history"
            - "memory.md#mem-obj-helper-history"
          note: "Delivery is wired; reliable model reliance and success are unobserved. Remembered snippets acquire no host execution authority from history alone."
        - scope: "Saved response code at normal replay parse/REPL consumer"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-trajectory-replay"
                - "memory.md#mem-obj-atif-trace"
              note: "Retained Python source directs execution by supplying the actions for the replayed turn."
          records:
            - "runtime.md#rt-rte-trajectory-replay"
            - "memory.md#mem-obj-atif-trace"
          note: "Standing procedural content is executable rather than advisory; this is not an independently validated answer or an enforced permission rule."
        - scope: "Saved invoke structure, cursors and comparison signatures at replay selector"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-trajectory-replay"
                - "memory.md#mem-obj-atif-trace"
              note: "Retained tree/cursor state selects saved response or live continuation."
            - value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-trajectory-replay"
              note: "When enabled, expected observation/edit signatures determine replay compatibility."
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-trajectory-replay"
              note: "Detected incompatibility or exhaustion prevents further saved-response supply on the selected node."
          records:
            - "runtime.md#rt-rte-trajectory-replay"
            - "memory.md#mem-obj-atif-trace"
          note: "Optional comparison is structural, not semantic; shared-stack routing assumes sequential nesting."
        - scope: "Generated workflow source at standalone Python consumer"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-workflow-emission"
              note: "Retained function bodies and entry blocks direct later standalone execution."
          records:
            - "runtime.md#rt-rte-workflow-emission"
          note: "No automatic installation as next Agent policy is established."
        - scope: "Execution experience at workflow materializer"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-workflow-emission"
              note: "Recorded model code and execution feedback feed automatic production of a durable behavior-shaping program."
          records:
            - "runtime.md#rt-rte-workflow-emission"
          note: "Learning authority at the artifact producer is distinct from downstream procedural instruction; improvement is not established."
        - scope: "Rollout samples at documented external trainer"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-rollout-export"
                - "memory.md#mem-obj-rollout"
              note: "Examples and sampled spans are afforded as training inputs."
          records:
            - "memory.md#mem-rte-rollout-export"
            - "memory.md#mem-obj-rollout"
          note: "No shipped trainer, optimizer, parameter artifact or actual training consumption is supplied."
        - scope: "Persisted model/backend and configuration groups at console startup"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-user-settings"
                - "epistemic.md#epi-rte-model-ping"
              note: "Retained configuration selects components and request settings."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-user-settings"
              note: "Persisted permission settings can constrain or loosen later console execution policy."
          records:
            - "memory.md#mem-obj-user-settings"
            - "epistemic.md#epi-rte-model-ping"
          note: "Loader warns rather than rejecting sandbox loosening; changed settings affect console, not bare library import."
        - scope: "Opaque retained result methods, external weights and trainer update consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-conversation-history"
            - "runtime.md#rt-cmp-model-backend"
            - "memory.md#mem-rte-weight-transport"
            - "memory.md#mem-rte-rollout-export"
          note: "Internal payload effects and external learned-parameter consumers are not inspected; no complete authority inventory follows from displayed text."
      records:
        - "memory.md#mem-rte-session-history"
        - "memory.md#mem-obj-helper-history"
        - "runtime.md#rt-rte-trajectory-replay"
        - "memory.md#mem-obj-atif-trace"
        - "runtime.md#rt-rte-workflow-emission"
        - "memory.md#mem-rte-rollout-export"
        - "memory.md#mem-obj-rollout"
        - "memory.md#mem-obj-user-settings"
        - "epistemic.md#epi-rte-model-ping"
        - "memory.md#mem-obj-conversation-history"
        - "runtime.md#rt-cmp-model-backend"
        - "memory.md#mem-rte-weight-transport"
      note: "Classifications follow the actual consumer. Executable retained source supplies procedural instruction; replay gates and configuration controls have separate routing/validation/enforcement effects. External consumers remain bounded affordances."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Console history append, ATIF serialization, workflow emission, rollout collection and diagnostic conversion"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-history"
                - "memory.md#mem-rte-trace-recording"
                - "runtime.md#rt-rte-workflow-emission"
                - "memory.md#mem-rte-rollout-export"
                - "memory.md#mem-rte-trace-display"
              note: "Software admits entries, trace records and generated files without per-content human approval."
          records:
            - "memory.md#mem-rte-session-history"
            - "memory.md#mem-rte-trace-recording"
            - "runtime.md#rt-rte-workflow-emission"
            - "memory.md#mem-rte-rollout-export"
            - "memory.md#mem-rte-trace-display"
          note: "Starting a console session, hook or converter does not make its subsequent content admission manual."
        - scope: "Explicit operator editing or approval of retained settings content"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "wired"
              records:
                - "memory.md#mem-obj-user-settings"
                - "runtime.md#rt-rte-settings-change"
              note: "Direct file editing or explicitly approved configuration-changing helper code supplies a content-level human decision."
          records:
            - "memory.md#mem-obj-user-settings"
            - "runtime.md#rt-rte-settings-change"
          note: "Applies to the evidenced human decision path, not every generic programmatic settings write."
        - scope: "Generic model-switch settings persistence and pre-existing configuration"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-user-settings"
            - "epistemic.md#epi-rte-model-ping"
          note: "Human/caller selection is mixed in the recorded API; a generic caller does not establish human decision or automatic admission for every settings value."
        - scope: "External weight replacement and trainer admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-weight-transport"
            - "memory.md#mem-rte-rollout-export"
          note: "External caller identity, optimizer decisions and server admission control are unresolved; transmitting bytes does not resolve write agency."
      records:
        - "memory.md#mem-rte-session-history"
        - "memory.md#mem-rte-trace-recording"
        - "runtime.md#rt-rte-workflow-emission"
        - "memory.md#mem-rte-rollout-export"
        - "memory.md#mem-rte-trace-display"
        - "memory.md#mem-obj-user-settings"
        - "runtime.md#rt-rte-settings-change"
        - "epistemic.md#epi-rte-model-ping"
        - "memory.md#mem-rte-weight-transport"
      note: "Automatic trace and session writers are known. Content-level human settings decisions are manual; generic API callers and external training remain unresolved."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Persisted model/backend replacement after an admitted switch"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-user-settings"
                - "epistemic.md#epi-rte-model-ping"
              note: "The writer revises existing model/backend defaults while preserving unrelated settings."
          records:
            - "memory.md#mem-obj-user-settings"
            - "epistemic.md#epi-rte-model-ping"
          note: "This is revision of retained configuration, not evidence-responsive improvement."
        - scope: "Session append, ATIF/raw trace capture and diagnostic projection"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-session-history"
            - "memory.md#mem-rte-trace-recording"
            - "memory.md#mem-rte-trace-display"
          note: "Records establish append and display conversion, not semantic consolidation, deduplication, synthesis or another controlled curation transformation. Display truncation is not treated as a retained semantic summary."
        - scope: "Workflow materialization and token sample projection"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-workflow-emission"
            - "memory.md#mem-rte-rollout-export"
          note: "Source-to-program emission and mask/projection construction do not establish a reduced representation of existing claims or a novel claim. No controlled semantic curation operation is determined by these records."
        - scope: "External model/trainer updates and opaque payload maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-weight-transport"
            - "memory.md#mem-rte-rollout-export"
            - "memory.md#mem-obj-conversation-history"
          note: "Transformation rules, quality selection and retained payload maintenance are uninspected."
      records:
        - "memory.md#mem-obj-user-settings"
        - "epistemic.md#epi-rte-model-ping"
        - "memory.md#mem-rte-session-history"
        - "memory.md#mem-rte-trace-recording"
        - "memory.md#mem-rte-trace-display"
        - "runtime.md#rt-rte-workflow-emission"
        - "memory.md#mem-rte-rollout-export"
        - "memory.md#mem-rte-weight-transport"
        - "memory.md#mem-obj-conversation-history"
      note: "Settings revision supports evolve; generic message edits, raw capture, representation conversion and external training cannot be upgraded to unrecorded curation semantics."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Console history delivery and subsequent explicit live-object inspection"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-history"
              note: "Every next prompt automatically receives nonempty main history; helpers automatically receive rendered transcripts."
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-history"
                - "memory.md#mem-rte-session-history"
              note: "The main agent can explicitly inspect prior live inputs/results through the bound history object."
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-obj-helper-history"
            - "memory.md#mem-rte-session-history"
          note: "Automatic delivery and requested object inspection are separate operations within the same chain."
        - scope: "ATIF file request followed by automatic query-time response selection"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-trajectory-replay"
              note: "Caller explicitly chooses a trace file for replay."
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-trajectory-replay"
              note: "At each query the installed selector supplies the selected saved response without a request for that individual retained response."
          records:
            - "runtime.md#rt-rte-trajectory-replay"
            - "memory.md#mem-obj-atif-trace"
          note: "Requested trace acquisition does not erase automatic per-query selection; concurrent invoke correspondence remains limited."
        - scope: "Generated standalone workflow"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-workflow-emission"
              note: "A later caller can explicitly run emitted entry blocks."
          records:
            - "runtime.md#rt-rte-workflow-emission"
          note: "No independent automatic Agent installation is recorded."
        - scope: "Rollout projections and requested diagnostic file conversion"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-rollout-export"
                - "memory.md#mem-rte-trace-display"
              note: "Caller chooses an export projection or requests conversion of a named retained trace/log."
          records:
            - "memory.md#mem-rte-rollout-export"
            - "memory.md#mem-rte-trace-display"
          note: "Export mechanics are wired; trainer use is only afforded."
        - scope: "Persisted console defaults"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-user-settings"
              note: "Startup automatically loads the console-scoped settings file before CLI overrides."
          records:
            - "memory.md#mem-obj-user-settings"
          note: "Starting the console is not a request for each persisted configuration value."
        - scope: "External trainer, updated serving weights and opaque result consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-weight-transport"
            - "runtime.md#rt-cmp-model-backend"
            - "memory.md#mem-rte-rollout-export"
            - "memory.md#mem-obj-conversation-history"
          note: "Later external parameter consumption and payload-specific access cannot be completely enumerated."
      records:
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-obj-helper-history"
        - "memory.md#mem-rte-session-history"
        - "runtime.md#rt-rte-trajectory-replay"
        - "memory.md#mem-obj-atif-trace"
        - "runtime.md#rt-rte-workflow-emission"
        - "memory.md#mem-rte-rollout-export"
        - "memory.md#mem-rte-trace-display"
        - "memory.md#mem-obj-user-settings"
        - "memory.md#mem-rte-weight-transport"
        - "runtime.md#rt-cmp-model-backend"
      note: "Both requested access and automatic per-invocation delivery exist; external consumer routes prevent a complete direction inventory."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Automatic main/helper history injection"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-history"
                - "memory.md#mem-obj-helper-history"
              note: "Trigger is the next prompt/helper request; selector uses nonempty/available history and delivers all turns with per-entry display caps."
          records:
            - "memory.md#mem-rte-session-history"
            - "memory.md#mem-obj-helper-history"
          note: "No relevance match is recorded; caps are presentation limits, not semantic targeting."
        - scope: "Automatic ATIF response supply"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-trajectory-replay"
            - "memory.md#mem-obj-atif-trace"
          note: "Query Send uses the shared stack's top frame and response-cursor progression after next-child mapping. These records establish sequential selection, not an identity-match predicate or another controlled signal. Structural metadata and addressable positions do not establish identifier-based push; the recorded selector does not determine a controlled signal. Replay push remains wired, with invoke correspondence limited to sequential nesting."
        - scope: "Automatic console defaults load"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-user-settings"
              note: "Trigger is console startup; availability and loader policy determine whole-file baseline delivery."
          records:
            - "memory.md#mem-obj-user-settings"
          note: "Model names inside the configuration are not themselves identifier-based selection of retained memory parts."
        - scope: "Pull-only workflow, sample export and diagnostic conversion operations"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-workflow-emission"
            - "memory.md#mem-rte-rollout-export"
            - "memory.md#mem-rte-trace-display"
          note: "No push selector occurs within these requested operations; they cannot establish a system-wide inapplicable axis."
        - scope: "External weights/trainer and opaque payload selection"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-weight-transport"
            - "memory.md#mem-rte-rollout-export"
            - "memory.md#mem-obj-conversation-history"
            - "runtime.md#rt-cmp-model-backend"
          note: "Direction and selectors beyond JAZ transport/export are unresolved; no embedding, lexical or judgment selector can be inferred."
      records:
        - "memory.md#mem-rte-session-history"
        - "memory.md#mem-obj-helper-history"
        - "runtime.md#rt-rte-trajectory-replay"
        - "memory.md#mem-obj-atif-trace"
        - "memory.md#mem-obj-user-settings"
        - "runtime.md#rt-rte-workflow-emission"
        - "memory.md#mem-rte-rollout-export"
        - "memory.md#mem-rte-trace-display"
        - "memory.md#mem-rte-weight-transport"
        - "memory.md#mem-obj-conversation-history"
        - "runtime.md#rt-cmp-model-backend"
      note: "Coarse session/default delivery is supported. Replay's sequential frame/cursor progression does not determine a controlled signal, and external selection remains unresolved. These unresolved included selectors keep coverage partial; pull-only local operations do not make the axis inapplicable."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Execution-to-workflow automatic materialization with standalone consumer"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-workflow-emission"
              note: "Recorded execution-associated code is automatically retained as durable functions/entry blocks that afford later execution."
          records:
            - "runtime.md#rt-rte-workflow-emission"
          note: "Automatic emission is wired; qualifying later use is afforded. No improved performance, equivalence or observed execution is implied."
        - scope: "Raw session histories and ATIF response reuse"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-session-history"
            - "memory.md#mem-rte-trace-recording"
            - "runtime.md#rt-rte-trajectory-replay"
          note: "Records establish raw capture and later context/action reuse, but no separately established durable behavior-shaping update from these raw logs. No bounded absence record supports a local no."
        - scope: "Rollout samples to external trainer and weight replacement"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-rollout-export"
            - "memory.md#mem-rte-weight-transport"
            - "runtime.md#rt-cmp-model-backend"
          note: "A documented training consumer and update transport exist, but durable learner output, automatic update admission and later parameter consumer are not connected by accepted records."
        - scope: "Configuration replacements and opaque result updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-user-settings"
            - "epistemic.md#epi-rte-model-ping"
            - "memory.md#mem-obj-conversation-history"
          note: "Configuration admission is not recorded as trace-fed adaptation; payload updates and initial provenance remain unresolved. This does not warrant a boundary-wide no."
      records:
        - "runtime.md#rt-rte-workflow-emission"
        - "memory.md#mem-rte-session-history"
        - "memory.md#mem-rte-trace-recording"
        - "runtime.md#rt-rte-trajectory-replay"
        - "memory.md#mem-rte-rollout-export"
        - "memory.md#mem-rte-weight-transport"
        - "runtime.md#rt-cmp-model-backend"
        - "memory.md#mem-obj-user-settings"
        - "epistemic.md#epi-rte-model-ping"
        - "memory.md#mem-obj-conversation-history"
      note: "An afforded trace-to-program route supports yes independently of unresolved raw-history and external training routes. Trace learning is not demonstrated improvement."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Workflow materialization inputs"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-workflow-emission"
              note: "Query-completion response text from agent conversation supplies code for retained program generation."
            - value: "tool-traces"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-workflow-emission"
              note: "REPL execution code/results and recoverable-error feedback shape emitted code/wrapping."
          records:
            - "runtime.md#rt-rte-workflow-emission"
          note: "Classification follows recorded conversational output and execution feedback, not hook event-envelope labels. No event-streams value is inferred merely from event callbacks."
        - scope: "Unresolved rollout-to-trainer, raw-history and external parameter update routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-rollout-export"
            - "memory.md#mem-rte-weight-transport"
            - "memory.md#mem-rte-session-history"
            - "memory.md#mem-rte-trace-recording"
            - "runtime.md#rt-rte-trajectory-replay"
          note: "Original session and query activity is visible, but which inputs feed a qualifying durable automatic update remains unestablished on these routes."
        - scope: "Opaque payload derivation and any trace-fed settings update"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-obj-user-settings"
            - "epistemic.md#epi-rte-model-ping"
          note: "The records do not identify a qualifying trace input/update chain for these unresolved parts."
      records:
        - "runtime.md#rt-rte-workflow-emission"
        - "memory.md#mem-rte-rollout-export"
        - "memory.md#mem-rte-weight-transport"
        - "memory.md#mem-rte-session-history"
        - "memory.md#mem-rte-trace-recording"
        - "runtime.md#rt-rte-trajectory-replay"
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-obj-user-settings"
        - "epistemic.md#epi-rte-model-ping"
      note: "Session and execution-trace content support the afforded workflow route; external and opaque update routes remain unresolved. No global inapplicability follows from missing trainer wiring."
---

# JAZ memory profile

## Comparison rationale

This profile classifies accepted records, not observed operation. The session-object container is known while arbitrary native results remain opaque. A capped repr cannot establish the form, backing store, lineage or effects of the original payload. [MEM-OBJ-conversation-history](memory.md#mem-obj-conversation-history) and [MEM-RTE-session-history](memory.md#mem-rte-session-history) preserve that distinction. Ordinary current-loop buffers and input abbreviation are outside accumulated read-back memory; the generic message-edit seam does not establish an automatic summary producer.

Executable reuse has two different horizons. [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay) supplies raw saved response source into the normal execution pipeline. [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission) automatically produces retained standalone procedural artifacts. The latter supports an afforded trace-learning route even without automatic next-Agent installation or proof of improved capacity. Its session response text and REPL feedback support session-logs and tool-traces; hook transport alone adds no event-stream source. At downstream execution, retained code supplies procedural instruction, not a correctness oracle or a permission veto. Workflow emission gives the input experience learning authority at the artifact producer separately from the output's instruction authority at the executor.

Read-back chains retain their separate operations. Choosing an ATIF file is pull; query-time frame/cursor selection is push. The recorded replay selector progresses through saved children and response cursors using the shared stack's top frame; it does not establish an identity comparison selecting delivered parts. Neither addressable positions nor retained structural metadata support identifier-based push. No controlled signal is determined for this unit, so its assessment is not-determinable without withdrawing wired replay push. The concurrency caveat limits frame/caller correspondence, not whether an identity predicate exists; divergence detection defaults off. Automatic session history and startup defaults instead use coarse availability selection. [MEM-OBJ-atif-trace](memory.md#mem-obj-atif-trace) and [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay) warrant the replay split; [MEM-RTE-session-history](memory.md#mem-rte-session-history) warrants the separate object-inspection pull.

Changed console defaults remain included because their values are revised through use and reloaded for later operation, unlike shipped static configuration templates. Their consumer selects components and applies configured permission policies. Model/backend replacement supports evolve, but says nothing about learned improvement. Manual content edits and approved helper changes are separated from generic caller-controlled model persistence; a caller is not necessarily a human. [MEM-OBJ-user-settings](memory.md#mem-obj-user-settings), [EPI-RTE-model-ping](epistemic.md#epi-rte-model-ping) and [RT-RTE-settings-change](runtime.md#rt-rte-settings-change) bound those findings. Helper admission flags do not prove snippet execution completed; the workflow annotation on [RT-RTE-settings-change](runtime.md#rt-rte-settings-change) keeps that distinction.

Reconciliation resolves the duplicate rollout object and export route to [MEM-OBJ-rollout](memory.md#mem-obj-rollout) and [MEM-RTE-rollout-export](memory.md#mem-rte-rollout-export), and the duplicate weight update to [MEM-RTE-weight-transport](memory.md#mem-rte-weight-transport). No duplicate citations are counted as additional routes. The preserved afforded-versus-wired disagreement concerns the weight request wrapper, not proven server application. This profile chooses neither side to upgrade parameter retention, admission, provenance or later consumption: those units remain unresolved. The identified external parametric form does not establish its physical substrate. Samples afford a learning consumer but do not supply the missing trainer-to-durable-weights chain. Raw capture and structural export rejection do not supply bounded absence warrants for trace-learning no or a semantic curation finding.

All axis assessments remain partial. Positives retain their local evidence layers; unresolved result internals, initialization and external update/consumer alternatives cannot be removed to obtain complete coverage. Diagnostic derivatives support local file storage and requested conversion, not an automatic future-agent telemetry route. The bounded diagnostic inspection and unavailable external lifecycle prevent a universal inventory claim. [MEM-RTE-trace-display](memory.md#mem-rte-trace-display), [MEM-RTE-rollout-export](memory.md#mem-rte-rollout-export) and [MEM-RTE-weight-transport](memory.md#mem-rte-weight-transport) retain those limits. No axis asserts observed use, causal benefit, a global negative, or an absent alternative from missing execution evidence.

Source-read log: none. This correction used the supplied accepted members, reconciliation, refusal and previous output as its baseline; no source files or other profiles were read.
