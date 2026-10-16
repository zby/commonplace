---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: OS-Copilot memory comparison across retained tool payloads and access state, course lessons,
  benchmark resume records, and unresolved service/provider retention.
run-id: AAS-2026-10-16-os-copilot-7cef03148c53-01
source-identity: https://github.com/OS-Copilot/OS-Copilot
reviewed-boundary: f720af8807e49a92dda64572d2c6bc6c0ac7ee7e
memory-comparison:
  version: 2
  scope: Retained tool code, descriptions, vector/name access state, live reloaded manager copies, course
    lessons and their later curriculum/task routes, and GAIA result rows consumed for accounting/resume.
    Includes unresolved initial/direct-caller provenance and possible external-provider/page-service retained
    alternatives. Excludes shipped static prompts and inference weights as established accumulated memory,
    ordinary graph/repair state and example histories, raw display-only UI logs/screenshots, and arbitrary
    host effects without a recorded later consumer; no exclusion resolves opaque provider or page-cache
    alternatives.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Retained tool code and description payloads, including live manager copies
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-tool-code
          - memory.md#mem-obj-tool-description
          note: Local JSON, Python and text mirrors retain the payloads.
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-tool-code
          - memory.md#mem-obj-tool-description
          note: The manager retains dictionary copies used by later model-context getters.
        records:
        - memory.md#mem-obj-tool-code
        - memory.md#mem-obj-tool-description
        note: JSON and mirrored source/text files persist content; getters consume the reloaded dictionary.
      - scope: Tool description access index
        assessment: known
        findings:
        - value: vector
          basis: wired
          records:
          - memory.md#mem-obj-tool-vectordb
          note: Descriptions are embedded and indexed with name metadata in persistent Chroma.
        records:
        - memory.md#mem-obj-tool-vectordb
        note: The persistent Chroma collection is a vector substrate; dependency-internal SQL or file
          layout is not separately inferred.
      - scope: Course lessons and their live curriculum copy
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-course
          note: Merged course JSON retains lessons across initialization.
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-course
          note: The course dictionary supplies later curriculum rounds.
        records:
        - memory.md#mem-obj-course
        note: Course JSON reload and in-process dictionary updates are both explicit.
      - scope: GAIA retained comparison rows used for accounting/resume
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - epistemic.md#epi-rte-gaia-comparison
          note: The result file preserves answer/reference pairs and the resume index.
        records:
        - epistemic.md#epi-rte-gaia-comparison
        note: The script appends JSONL and reloads rows on later launches.
      - scope: Possible external-provider retained state and page-service cross-request state
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-chat-model
        - runtime.md#rt-cmp-tool-embeddings
        - epistemic.md#epi-cmp-web-models
        - epistemic.md#epi-rte-page-content
        note: Provider retention/update internals and Chroma page collection lifecycle were not inspected.
          Inference alone does not classify accumulated provider memory; request-local page processing
          does not establish a later-memory route.
      records:
      - memory.md#mem-obj-tool-code
      - memory.md#mem-obj-tool-description
      - memory.md#mem-obj-tool-vectordb
      - memory.md#mem-obj-course
      - epistemic.md#epi-rte-gaia-comparison
      - runtime.md#rt-cmp-chat-model
      - runtime.md#rt-cmp-tool-embeddings
      - epistemic.md#epi-cmp-web-models
      - epistemic.md#epi-rte-page-content
      note: Known payload, index, curriculum and benchmark stores coexist with unresolved service/provider
        retention. No repository or model-weight update substrate is inferred from source hosting or inference.
    representational_form:
      assessment: partial
      units:
      - scope: Retained Python source at generation-context consumption
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-tool-code
          note: Retained executable source supplies reusable code examples, not learned weights.
        records:
        - memory.md#mem-obj-tool-code
        - runtime.md#rt-bap-tool-context
        note: Python source has localized symbolic structure even when serialized for model interpretation;
          embedded prose is classified separately.
      - scope: Tool docstring/description prose and course lesson values at model consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-tool-description
          - memory.md#mem-obj-course
          - runtime.md#rt-bap-tool-context
          - runtime.md#rt-bap-course-tasks
          note: These parts receive force through model interpretation.
        records:
        - memory.md#mem-obj-tool-description
        - memory.md#mem-obj-course
        - runtime.md#rt-bap-tool-context
        - runtime.md#rt-bap-course-tasks
        note: Descriptions guide planning; lessons guide curriculum design and supply tasks.
      - scope: Tool index dense embeddings
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-tool-vectordb
          note: Distributed numerical description vectors support similarity ranking.
        records:
        - memory.md#mem-obj-tool-vectordb
        note: Dense numerical representations are separate from symbolic identity metadata.
      - scope: Tool name joins, course dictionary keys and GAIA resume/comparison fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-tool-vectordb
          - memory.md#mem-obj-course
          - epistemic.md#epi-rte-gaia-comparison
          note: Localized keys, fields and equality/resume rules have fixed code consumers.
        records:
        - memory.md#mem-obj-tool-vectordb
        - memory.md#mem-obj-course
        - epistemic.md#epi-rte-gaia-comparison
        note: Fixed rules dereference names, select dictionary entries, compare strings and skip indices.
      - scope: GAIA answer/reference strings as retained benchmark operands
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - epistemic.md#epi-rte-gaia-comparison
          note: The equality consumer treats answer text as exact-match operands.
        records:
        - epistemic.md#epi-rte-gaia-comparison
        note: No semantic interpretation or natural-language answer instance is supplied; the established
          consumer compares strings.
      - scope: Possible external-provider retained state and page-service cross-request state
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-chat-model
        - runtime.md#rt-cmp-tool-embeddings
        - epistemic.md#epi-cmp-web-models
        - epistemic.md#epi-rte-page-content
        note: Provider retention/update internals and Chroma page collection lifecycle were not inspected.
          Inference alone does not classify accumulated provider memory; request-local page processing
          does not establish a later-memory route.
      records:
      - memory.md#mem-obj-tool-code
      - runtime.md#rt-bap-tool-context
      - memory.md#mem-obj-tool-description
      - memory.md#mem-obj-course
      - runtime.md#rt-bap-course-tasks
      - memory.md#mem-obj-tool-vectordb
      - epistemic.md#epi-rte-gaia-comparison
      - runtime.md#rt-cmp-chat-model
      - runtime.md#rt-cmp-tool-embeddings
      - epistemic.md#epi-cmp-web-models
      - epistemic.md#epi-rte-page-content
      note: The inventory splits prose, source, numerical access state and fixed-rule metadata rather
        than classifying every serialized prompt as natural language. Unknown provider/page memory cannot
        inherit these forms.
    lineage:
      assessment: partial
      units:
      - scope: Automatically generated tool code
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-tool-code
          - runtime.md#rt-rte-tool-admission
          note: Model-generated candidate code is retained after the completion/score gate.
        records:
        - memory.md#mem-obj-tool-code
        - runtime.md#rt-rte-tool-admission
        note: The model authors the candidate; feedback controls admission, not a demonstrated extraction
          of code from a session log.
      - scope: Tool descriptions on the inspected docstring-extraction paths
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-tool-description
          - runtime.md#rt-rte-tool-admission
          - runtime.md#rt-rte-manual-maintenance
          note: Deterministic extraction compiles a description from code prose.
        records:
        - memory.md#mem-obj-tool-description
        - runtime.md#rt-rte-tool-admission
        - runtime.md#rt-rte-manual-maintenance
        note: Regex selects an existing fragment; independent direct-manager descriptions remain a separate
          unresolved path.
      - scope: Description-vector derivation from admitted prose
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-tool-vectordb
          note: Embedding inference derives the retained numerical access representation from descriptions.
        records:
        - memory.md#mem-obj-tool-vectordb
        - runtime.md#rt-cmp-tool-embeddings
        note: The embedding input and call are known, but exact model/weight provenance is unpinned and
          provider-internal provenance is uninspected.
      - scope: Caller-selected tool files imported through maintenance helper
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - runtime.md#rt-rte-manual-maintenance
          - memory.md#mem-obj-tool-code
          note: The helper reads caller-selected source content into retained tool state.
        records:
        - runtime.md#rt-rte-manual-maintenance
        - memory.md#mem-obj-tool-code
        note: File acquisition is established; original authorship and any human editing are not intrinsic
          to the generic caller.
      - scope: New model-designed course lessons
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-course
          - runtime.md#rt-rte-course-learning
          note: Course design produces new lesson text from configured inputs and prior course context.
        records:
        - memory.md#mem-obj-course
        - runtime.md#rt-rte-course-learning
        note: Model authorship is established without establishing successful learning or semantic novelty.
      - scope: Initial/direct-manager tool content and preexisting course content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-tool-code
        - memory.md#mem-obj-tool-description
        - memory.md#mem-obj-course
        - runtime.md#rt-rte-manual-maintenance
        note: The loader and generic API leave original authorship, imported origins and edits unresolved;
          known subsequent transformations do not resolve initialization.
      - scope: GAIA result-row construction
        assessment: partial
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - epistemic.md#epi-rte-gaia-comparison
          note: The batch driver records task-result/reference comparisons and run indices for later accounting/resume.
        records:
        - epistemic.md#epi-rte-gaia-comparison
        note: Rows record run/result and reference fields; dataset origin and answer postprocessing internals
          remain uninspected.
      - scope: Possible external-provider retained state and page-service cross-request state
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-chat-model
        - runtime.md#rt-cmp-tool-embeddings
        - epistemic.md#epi-cmp-web-models
        - epistemic.md#epi-rte-page-content
        note: Provider retention/update internals and Chroma page collection lifecycle were not inspected.
          Inference alone does not classify accumulated provider memory; request-local page processing
          does not establish a later-memory route.
      records:
      - memory.md#mem-obj-tool-code
      - runtime.md#rt-rte-tool-admission
      - memory.md#mem-obj-tool-description
      - runtime.md#rt-rte-manual-maintenance
      - memory.md#mem-obj-tool-vectordb
      - runtime.md#rt-cmp-tool-embeddings
      - memory.md#mem-obj-course
      - runtime.md#rt-rte-course-learning
      - epistemic.md#epi-rte-gaia-comparison
      - runtime.md#rt-cmp-chat-model
      - epistemic.md#epi-cmp-web-models
      - epistemic.md#epi-rte-page-content
      note: Authoring, import, deterministic derivation and run-result extraction retain their distinct
        paths. No trace-extracted lineage is inferred merely because a score gates model-authored code.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Tool code and readable descriptions at later planner/generator consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-tool-code
          - memory.md#mem-obj-tool-description
          - runtime.md#rt-bap-tool-context
          note: Descriptions and code supply reference context and examples for new plans/programs.
        records:
        - memory.md#mem-obj-tool-code
        - memory.md#mem-obj-tool-description
        - runtime.md#rt-bap-tool-context
        note: Delivery is contextual, not an enforced instruction or automatic stored-code invocation.
      - scope: Descriptions and dense vectors at tool similarity selector
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-tool-description
          - memory.md#mem-obj-tool-vectordb
          note: Description-derived vectors determine top-k tool relevance.
        records:
        - memory.md#mem-obj-tool-description
        - memory.md#mem-obj-tool-vectordb
        - runtime.md#rt-bap-tool-context
        note: Text and its embedding affect relative retrieval priority under fixed similarity code.
      - scope: Tool name metadata at retained-payload dereference
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-tool-vectordb
          - runtime.md#rt-bap-tool-context
          note: Returned names route selection to the corresponding retained code/description.
        records:
        - memory.md#mem-obj-tool-vectordb
        - runtime.md#rt-bap-tool-context
        note: Selected identity metadata chooses which JSON payload enters the context channel.
      - scope: Prior lesson values at the next course-design call
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-course
          - runtime.md#rt-bap-course-tasks
          note: Previous lesson content informs requested progression and nonduplication.
        records:
        - memory.md#mem-obj-course
        - runtime.md#rt-rte-course-learning
        - runtime.md#rt-bap-course-tasks
        note: The prior-course text is advisory design context, not verified completion evidence.
      - scope: Retained/generated lesson values at agent task dispatch
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-obj-course
          - runtime.md#rt-bap-course-tasks
          note: Lesson strings specify the tasks the agent is to execute.
        records:
        - memory.md#mem-obj-course
        - runtime.md#rt-rte-course-learning
        - runtime.md#rt-bap-course-tasks
        note: Lessons become operative requests to the task agent rather than background reference alone.
      - scope: GAIA saved answer/reference pairs at equality accounting
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - epistemic.md#epi-rte-gaia-comparison
          note: Reloaded answer/reference pairs determine exact-match credit.
        records:
        - epistemic.md#epi-rte-gaia-comparison
        note: The reference is a bounded validation criterion for exact string agreement, not tool admission
          or semantic truth.
      - scope: GAIA saved final index at resume selection
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - epistemic.md#epi-rte-gaia-comparison
          note: The retained index determines which benchmark tasks remain to run.
        - value: enforcement
          basis: wired
          records:
          - epistemic.md#epi-rte-gaia-comparison
          note: Indices at or below the resume boundary are skipped by fixed code.
        records:
        - epistemic.md#epi-rte-gaia-comparison
        note: The checkpoint selects the subsequent input window; the code comparison enforces the skip.
      - scope: Possible external-provider retained state and page-service cross-request state
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-chat-model
        - runtime.md#rt-cmp-tool-embeddings
        - epistemic.md#epi-cmp-web-models
        - epistemic.md#epi-rte-page-content
        note: Provider retention/update internals and Chroma page collection lifecycle were not inspected.
          Inference alone does not classify accumulated provider memory; request-local page processing
          does not establish a later-memory route.
      records:
      - memory.md#mem-obj-tool-code
      - memory.md#mem-obj-tool-description
      - runtime.md#rt-bap-tool-context
      - memory.md#mem-obj-tool-vectordb
      - memory.md#mem-obj-course
      - runtime.md#rt-rte-course-learning
      - runtime.md#rt-bap-course-tasks
      - epistemic.md#epi-rte-gaia-comparison
      - runtime.md#rt-cmp-chat-model
      - runtime.md#rt-cmp-tool-embeddings
      - epistemic.md#epi-cmp-web-models
      - epistemic.md#epi-rte-page-content
      note: Authority is attached to actual retained parts and consumers. Transient judge scores enforce
        automatic admission but are not retained controls. No learning authority is inferred for unretained
        feedback or from trace-learning membership alone.
    write_agency:
      assessment: partial
      units:
      - scope: Automatic candidate tool admission, extracted descriptions and index writes
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-tool-admission
          - memory.md#mem-obj-tool-description
          - memory.md#mem-obj-tool-vectordb
          note: Model judgment and software threshold/name predicates admit tools and derived access material
            without per-content human decisions.
        records:
        - runtime.md#rt-rte-tool-admission
        - memory.md#mem-obj-tool-description
        - memory.md#mem-obj-tool-vectordb
        note: Starting the task is not approval of each retained candidate.
      - scope: Course design, dictionary update and JSON merge
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-course-learning
          - memory.md#mem-obj-course
          note: The driver updates/saves model-designed course content.
        records:
        - runtime.md#rt-rte-course-learning
        - memory.md#mem-obj-course
        note: Parsed model output is software-admitted, with no lesson-success approval gate.
      - scope: Documented human tool-maintenance use
        assessment: known
        findings:
        - value: manual
          basis: afforded
          records:
          - runtime.md#rt-rte-manual-maintenance
          note: The documented operator can explicitly supply or edit the retained file content.
        records:
        - runtime.md#rt-rte-manual-maintenance
        note: This finding covers only a human following the tutorial and supplying/editing the selected
          file, not every API caller.
      - scope: Generic manager writes and initial tool/course files
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-manual-maintenance
        - memory.md#mem-obj-tool-code
        - memory.md#mem-obj-tool-description
        - memory.md#mem-obj-course
        note: Caller identity and loader behavior do not determine per-content human control. Do not label
          every maintenance API write manual.
      - scope: GAIA result persistence
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - epistemic.md#epi-rte-gaia-comparison
          note: Software records benchmark comparisons and indices for later accounting/resume.
        records:
        - epistemic.md#epi-rte-gaia-comparison
        note: The driver appends result rows without per-row operator approval.
      - scope: Possible external-provider retained state and page-service cross-request state
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-chat-model
        - runtime.md#rt-cmp-tool-embeddings
        - epistemic.md#epi-cmp-web-models
        - epistemic.md#epi-rte-page-content
        note: Provider retention/update internals and Chroma page collection lifecycle were not inspected.
          Inference alone does not classify accumulated provider memory; request-local page processing
          does not establish a later-memory route.
      records:
      - runtime.md#rt-rte-tool-admission
      - memory.md#mem-obj-tool-description
      - memory.md#mem-obj-tool-vectordb
      - runtime.md#rt-rte-course-learning
      - memory.md#mem-obj-course
      - runtime.md#rt-rte-manual-maintenance
      - memory.md#mem-obj-tool-code
      - epistemic.md#epi-rte-gaia-comparison
      - runtime.md#rt-cmp-chat-model
      - runtime.md#rt-cmp-tool-embeddings
      - epistemic.md#epi-cmp-web-models
      - epistemic.md#epi-rte-page-content
      note: Known software admission and an afforded human content-supply mechanism coexist with unresolved
        generic and initialization control.
    curation_operations:
      assessment: partial
      units:
      - scope: Docstring-fragment extraction on retained-tool admission/maintenance
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-obj-tool-description
          - runtime.md#rt-rte-tool-admission
          - runtime.md#rt-rte-manual-maintenance
          note: The first matching docstring fragment becomes a reduced description of existing content.
        records:
        - memory.md#mem-obj-tool-description
        - runtime.md#rt-rte-tool-admission
        - runtime.md#rt-rte-manual-maintenance
        note: The operation selects/compresses existing prose into the retained description; direct supplied
          descriptions need not undergo it.
      - scope: Existing-name tool replacement and overlapping course-key replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-rte-manual-maintenance
          - memory.md#mem-obj-course
          note: Manager overwrite and dictionary merge revise existing retained entries.
        records:
        - runtime.md#rt-rte-manual-maintenance
        - memory.md#mem-obj-course
        note: Known replacement operations do not imply that model-generated lessons reliably avoid duplicates.
      - scope: Explicit tool deletion
        assessment: partial
        findings:
        - value: decay
          basis: wired
          records:
          - runtime.md#rt-rte-manual-maintenance
          note: Explicit deletion removes selected tool payloads and index entries from persistent eligible
            memory.
        records:
        - runtime.md#rt-rte-manual-maintenance
        - memory.md#mem-obj-tool-code
        - memory.md#mem-obj-tool-vectordb
        note: Disk/index removal forgets selected content, but stale live dictionaries and later reserialization
          prevent a complete withdrawal claim. No retained historical invalidation ledger is established.
      - scope: Course-model design and direct supplied tool/description content
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-course-learning
        - memory.md#mem-obj-course
        - runtime.md#rt-rte-manual-maintenance
        - memory.md#mem-obj-tool-description
        note: Requested progression/nonduplication and generic supplied content do not establish implemented
          deduplication or a claim absent from the inputs. Consolidation versus synthesis cannot be decided
          for arbitrary generated content.
      - scope: GAIA append/reload and resume accounting
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-gaia-comparison
        note: Result acquisition and counting alone establish none of the controlled memory-curation transformations.
      - scope: Possible external-provider retained state and page-service cross-request state
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-chat-model
        - runtime.md#rt-cmp-tool-embeddings
        - epistemic.md#epi-cmp-web-models
        - epistemic.md#epi-rte-page-content
        note: Provider retention/update internals and Chroma page collection lifecycle were not inspected.
          Inference alone does not classify accumulated provider memory; request-local page processing
          does not establish a later-memory route.
      records:
      - memory.md#mem-obj-tool-description
      - runtime.md#rt-rte-tool-admission
      - runtime.md#rt-rte-manual-maintenance
      - memory.md#mem-obj-course
      - memory.md#mem-obj-tool-code
      - memory.md#mem-obj-tool-vectordb
      - runtime.md#rt-rte-course-learning
      - epistemic.md#epi-rte-gaia-comparison
      - runtime.md#rt-cmp-chat-model
      - runtime.md#rt-cmp-tool-embeddings
      - epistemic.md#epi-cmp-web-models
      - epistemic.md#epi-rte-page-content
      note: Positive operations retain local warrants; embedding/index rebuild and name-collision checks
        do not establish deduplication. Last-fifty prompt selection leaves older disk entries intact and
        is not itself durable decay.
    read_back_direction:
      assessment: partial
      units:
      - scope: Tool retrieval request, similarity selection and payload return
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-bap-tool-context
          - memory.md#mem-obj-tool-code
          - memory.md#mem-obj-tool-vectordb
          note: Requested relevant descriptions/code are selected and returned to planning/generation.
        records:
        - runtime.md#rt-bap-tool-context
        - runtime.md#rt-rte-tool-admission
        - memory.md#mem-obj-tool-code
        - memory.md#mem-obj-tool-vectordb
        note: Task/replan/subtask transitions issue retrieval requests. Similarity fulfills those requests;
          returned names are internal joins, not a second unsolicited push.
      - scope: Course filename initialization load
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-obj-course
          - runtime.md#rt-rte-course-learning
          note: Initialization requests prior course material by filename.
        records:
        - memory.md#mem-obj-course
        - runtime.md#rt-rte-course-learning
        note: Software/package selects the requested local course file.
      - scope: Prior-course insertion into subsequent course-design prompts
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-course
          - runtime.md#rt-rte-course-learning
          - runtime.md#rt-bap-course-tasks
          note: The driver selects retained prior lesson text and injects it into the next design call.
        records:
        - memory.md#mem-obj-course
        - runtime.md#rt-rte-course-learning
        - runtime.md#rt-bap-course-tasks
        note: At curriculum design, the driver automatically supplies up to the last fifty dictionary
          entries without a model request for those entries.
      - scope: GAIA result-file reload for counters and resume
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - epistemic.md#epi-rte-gaia-comparison
          note: The script explicitly reloads prior rows for accounting and last-index recovery.
        records:
        - epistemic.md#epi-rte-gaia-comparison
        note: The benchmark caller requests previous result rows through get_numbers; subsequent skip
          logic is a control effect, not additional content delivery.
      - scope: Possible external-provider retained state and page-service cross-request state
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-chat-model
        - runtime.md#rt-cmp-tool-embeddings
        - epistemic.md#epi-cmp-web-models
        - epistemic.md#epi-rte-page-content
        note: Provider retention/update internals and Chroma page collection lifecycle were not inspected.
          Inference alone does not classify accumulated provider memory; request-local page processing
          does not establish a later-memory route.
      records:
      - runtime.md#rt-bap-tool-context
      - runtime.md#rt-rte-tool-admission
      - memory.md#mem-obj-tool-code
      - memory.md#mem-obj-tool-vectordb
      - memory.md#mem-obj-course
      - runtime.md#rt-rte-course-learning
      - runtime.md#rt-bap-course-tasks
      - epistemic.md#epi-rte-gaia-comparison
      - runtime.md#rt-cmp-chat-model
      - runtime.md#rt-cmp-tool-embeddings
      - epistemic.md#epi-cmp-web-models
      - epistemic.md#epi-rte-page-content
      note: Both pull and push are supported, at distinct operations. Page HTTP response delivery alone
        does not establish a later-memory route; provider alternatives remain uninspected.
    read_back_signal:
      assessment: partial
      units:
      - scope: Course prior-context push selector
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-course
          - runtime.md#rt-rte-course-learning
          note: Count/order filtering supplies prior lessons without targeted query matching.
        records:
        - memory.md#mem-obj-course
        - runtime.md#rt-rte-course-learning
        - runtime.md#rt-bap-course-tasks
        note: 'Trigger: next course-design call. Input: insertion-ordered course dictionary and length.
          Selected retained part: the last fifty lesson entries, or all entries if shorter. There is no
          semantic match or token cap.'
      - scope: Requested tool retrieval, course initialization and GAIA reload
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-bap-tool-context
        - memory.md#mem-obj-course
        - epistemic.md#epi-rte-gaia-comparison
        note: These operations are pull. Embedding matching and exact filenames/IDs on requested returns
          do not establish push signals.
      - scope: Possible external-provider retained state and page-service cross-request state
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-chat-model
        - runtime.md#rt-cmp-tool-embeddings
        - epistemic.md#epi-cmp-web-models
        - epistemic.md#epi-rte-page-content
        note: Provider retention/update internals and Chroma page collection lifecycle were not inspected.
          Inference alone does not classify accumulated provider memory; request-local page processing
          does not establish a later-memory route.
      records:
      - memory.md#mem-obj-course
      - runtime.md#rt-rte-course-learning
      - runtime.md#rt-bap-course-tasks
      - runtime.md#rt-bap-tool-context
      - epistemic.md#epi-rte-gaia-comparison
      - runtime.md#rt-cmp-chat-model
      - runtime.md#rt-cmp-tool-embeddings
      - epistemic.md#epi-cmp-web-models
      - epistemic.md#epi-rte-page-content
      note: The known push has a coarse selector. The unresolved service/provider alternatives prevent
        treating all other included memory as assessed pull-only.
    trace_learning:
      assessment: partial
      units:
      - scope: Feedback-gated reusable tool artifacts and later generation context
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-tool-admission
          - memory.md#mem-obj-tool-code
          - runtime.md#rt-bap-tool-context
          note: Tool execution feedback controls an automatic durable behavior-shaping artifact write
            with later planner/generator consumption.
        records:
        - runtime.md#rt-rte-tool-admission
        - memory.md#mem-obj-tool-code
        - memory.md#mem-obj-tool-description
        - runtime.md#rt-bap-tool-context
        note: Automatic execution-feedback-responsive admission yields durable code/descriptions and a
          wired later consumer. Original-code/repaired-score divergence limits quality and candidate identity,
          not existence of the route.
      - scope: Course generation from prior lesson text, configuration and optional demo-derived content
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-course-learning
        - memory.md#mem-obj-course
        note: The saved material is proposed curriculum, not a compacted outcome trace. The optional agent-derived
          demo payload and initial/prior content provenance are not characterized enough to establish
          every trace-fed alternative or a complete local negative.
      - scope: Generic maintenance and initial tool content
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-manual-maintenance
        - memory.md#mem-obj-tool-code
        - memory.md#mem-obj-tool-description
        note: Generic callers leave both admission control and original trace-fed derivation unresolved;
          the afforded human path does not settle other callers.
      - scope: GAIA result rows used only for accounting/resume
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-gaia-comparison
        note: The accepted record establishes raw-result accounting and resume, not a qualifying learned
          artifact. It declares no bounded absence record, so a controlled local no cannot be established.
      - scope: Possible external-provider retained state and page-service cross-request state
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-chat-model
        - runtime.md#rt-cmp-tool-embeddings
        - epistemic.md#epi-cmp-web-models
        - epistemic.md#epi-rte-page-content
        note: Provider retention/update internals and Chroma page collection lifecycle were not inspected.
          Inference alone does not classify accumulated provider memory; request-local page processing
          does not establish a later-memory route.
      records:
      - runtime.md#rt-rte-tool-admission
      - memory.md#mem-obj-tool-code
      - memory.md#mem-obj-tool-description
      - runtime.md#rt-bap-tool-context
      - runtime.md#rt-rte-course-learning
      - memory.md#mem-obj-course
      - runtime.md#rt-rte-manual-maintenance
      - epistemic.md#epi-rte-gaia-comparison
      - runtime.md#rt-cmp-chat-model
      - runtime.md#rt-cmp-tool-embeddings
      - epistemic.md#epi-cmp-web-models
      - epistemic.md#epi-rte-page-content
      note: A wired yes is not observed learning, improved capacity or causal self-improvement. GAIA accounting
        does not establish a qualifying positive, but lacks a canonical bounded absence warrant for no;
        unresolved alternatives remain explicit.
    trace_source:
      assessment: partial
      units:
      - scope: Automatic feedback-gated tool admission
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records:
          - runtime.md#rt-rte-tool-admission
          - memory.md#mem-obj-tool-code
          note: Recorded execution feedback influences score/completion and therefore durable tool admission
            for later model context.
        records:
        - runtime.md#rt-rte-tool-admission
        - memory.md#mem-obj-tool-code
        - runtime.md#rt-bap-tool-context
        note: The qualifying trace-fed control input is execution output/error and evaluated feedback.
          No linked multi-step trajectory or recorded conversational-session source is established by
          the candidate code alone.
      - scope: Potential trace-fed course or generic manager alternatives
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-course-learning
        - memory.md#mem-obj-course
        - runtime.md#rt-rte-manual-maintenance
        - memory.md#mem-obj-tool-code
        note: Original trace origin and qualifying automatic control are unresolved. An extracted static
          demo document does not become a session log or event stream merely because an agent handled
          it.
      - scope: GAIA accounting/resume-only route
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-gaia-comparison
        note: The record establishes no qualifying trace-learning update but supplies no bounded absence
          record to resolve that assessment. Raw result origin alone cannot establish a qualifying learning-source
          value or complete inapplicability.
      - scope: Possible external-provider retained state and page-service cross-request state
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-chat-model
        - runtime.md#rt-cmp-tool-embeddings
        - epistemic.md#epi-cmp-web-models
        - epistemic.md#epi-rte-page-content
        note: Provider retention/update internals and Chroma page collection lifecycle were not inspected.
          Inference alone does not classify accumulated provider memory; request-local page processing
          does not establish a later-memory route.
      records:
      - runtime.md#rt-rte-tool-admission
      - memory.md#mem-obj-tool-code
      - runtime.md#rt-bap-tool-context
      - runtime.md#rt-rte-course-learning
      - memory.md#mem-obj-course
      - runtime.md#rt-rte-manual-maintenance
      - epistemic.md#epi-rte-gaia-comparison
      - runtime.md#rt-cmp-chat-model
      - runtime.md#rt-cmp-tool-embeddings
      - epistemic.md#epi-cmp-web-models
      - epistemic.md#epi-rte-page-content
      note: Tool traces are positively classified only for the qualifying tool-admission route. Missing
        provenance and provider lifecycle prevent complete trace-source coverage.
---

# OS-Copilot memory profile

## Comparison rationale

This revision-2 mapping uses accepted implementation records, not observed
runs. All positive implementation findings are wired unless their local basis
says afforded. The afforded manual path concerns a human supplying or editing
a selected tool file; it does not upgrade generic manager calls to manual
admission. Provider inference does not establish provider learning or retained
memory. Its possible retained alternatives remain uninspected on every axis.
The page service has request-time transformations but unresolved collection
lifecycle and no established later-memory consumer; it remains an unresolved
alternative rather than a classified persistent summary store.

### Canonical identities and coverage

The reconciliation supersedes the epistemic description object with
[MEM-OBJ-tool-description](memory.md#mem-obj-tool-description), the epistemic
course-text object with [MEM-OBJ-course](memory.md#mem-obj-course), and the
memory page-context route with
[EPI-RTE-page-content](epistemic.md#epi-rte-page-content). The mapping uses
those canonical records. The web-model container remains valid; its parts do
not imply separate retained stores. Generated/current candidate code is
broader than [MEM-OBJ-tool-code](memory.md#mem-obj-tool-code); only its retained
part is classified here. These supersessions change citation identity, not
evidence strength or certainty.

The known inventory spans payloads, access structures, write mechanisms and
later consumers. It retains separately unresolved initialization, direct
manager writes, service lifecycle and provider retention. Consequently no
axis claims a complete system-wide value inventory. The ordinary graph,
transient critique and example histories have no established accumulated
memory route in [RT-OBJ-tool-graph](runtime.md#rt-obj-tool-graph) and
[RT-RTE-example-loops](runtime.md#rt-rte-example-loops). Static prompts are
shipped methods rather than learned content in
[RT-OBJ-friday-prompts](runtime.md#rt-obj-friday-prompts).

GAIA rows belong to the inventory because
[EPI-RTE-gaia-comparison](epistemic.md#epi-rte-gaia-comparison) establishes a
later accounting/resume consumer. Their narrow exact-match validation and
resume-control forces do not establish agent knowledge or a trace-learning
artifact. The record supplies no canonical bounded absence warrant for a
controlled trace-learning no. This separates retained control/accounting state
from display-only logs without asserting complete absence. No dataset quality
or postprocessor semantics are inferred.

### Local mappings and unions

Tool descriptions have both knowledge authority at planning and ranking
authority through their embeddings. Name metadata routes selected payloads.
Retained source remains symbolic code used as examples, not automatically
executed retrieved functions. See
[MEM-OBJ-tool-vectordb](memory.md#mem-obj-tool-vectordb) and
[RT-BAP-tool-context](runtime.md#rt-bap-tool-context). Neither a retained
instruction consumer nor learning authority follows merely from the tool
admission route's trace-learning membership: raw execution feedback is not
itself retained as an update-consumer input by this store.

The tool chain pulls requested relevant content, even though runtime
transitions initiate requests automatically. Its semantic selector is not a
push-signal finding. In contrast, curriculum design receives an automatically
selected prior-course window. That push uses dictionary order/count, not an
identifier match, recency timestamps or embeddings. Filename-based course
initialization is a separate pull operation. Prior-course context supplies
knowledge to curriculum design, while lesson dispatch supplies instructions
to the agent. See [MEM-OBJ-course](memory.md#mem-obj-course) and
[RT-BAP-course-tasks](runtime.md#rt-bap-course-tasks).

Docstring selection is consolidation; overwrite/key replacement is evolution.
Deletion supports bounded forgetting, not historical invalidation or complete
revocation: live dictionary copies can survive and later be reserialized.
Index rebuilding and existing-name checks are not deduplication. Requested
nonduplication/progression does not prove those curation operations happened.
See [MEM-OBJ-tool-description](memory.md#mem-obj-tool-description),
[RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance) and
[MEM-OBJ-course](memory.md#mem-obj-course).

The automatic tool route qualifies as trace learning because execution
feedback controls durable admission and later generation receives retained
artifacts. The admitted payload need not contain the raw trace. It is still
model-authored code, with a separately compiled description and vector, not
necessarily trace-extracted code. The repair-score/original-code defect limits
faithfulness and reuse warrant without removing the wired route. Tool traces
are the established qualifying source; no session-log, event-stream or linked
trajectory source is inferred. See
[RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) and
[MEM-OBJ-tool-code](memory.md#mem-obj-tool-code). A derived union retains this
positive yes without manufacturing a local accounting-only no from a route
that declares no bounded absence. The positive does not mean observed
improvement, and missing optional/demo and direct-caller provenance prevents
a complete negative elsewhere.

### Source-read log

No source files were read for this classification. The supplied pinned
members, types, reconciliation and records contract were sufficient. No new
records, evidence passages or source observations are introduced.
