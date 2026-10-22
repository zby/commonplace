---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Harness² memory comparison: retained harnesses, reflected experience, reconstructed trace evidence and recovery state, with opaque native-memory alternatives."
run-id: AAS-2026-10-22-harness2-d5a180ba559c-01
source-identity: https://github.com/google-research/harness2
reviewed-boundary: "1cfe254e8d25b15f37048c3730134686abe60335"
memory-comparison:
  version: 2
  scope: "Accumulated or changed harness trees, experience and navigation, task-local traces/history supplied to later invocations, proposer and summary/rollout recovery state, and retained benchmark score rows. Includes unresolved native compaction/delegated/provider memory alternatives reached through shipped integrations; excludes unchanged static baseline instructions, ordinary current-call state, provider weights as storage without an established operational update, and printed reports without a later retained consumer."
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Retained harness text/code, EXPERIENCE.md, INDEX.md, evidence/history files, response/workspace caches, summaries/run marks and judged.json"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [runtime.md#rt-obj-harness-text, runtime.md#rt-obj-harness-code, memory.md#mem-obj-experience, memory.md#mem-obj-library-index, memory.md#mem-obj-evidence-tree, memory.md#mem-obj-cached-response, runtime.md#rt-rte-resume-reuse, epistemic.md#epi-rte-score-cache]
              note: "Local filesystem objects persist across consumer invocations; JSON and Markdown are encodings, not additional substrates."
          records: [memory.md#mem-rte-evidence-frame, runtime.md#rt-rte-resume-reuse, epistemic.md#epi-obj-score-rows]
          note: "These accepted records cover the named framework-owned retained inventory, not every external runtime store."
        - scope: "Native compaction checkpoints, delegated return memory and provider-retained state"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-clm-compaction-boundary, memory.md#mem-rte-evidence-frame]
          note: "Configuration does not expose the operative payload or its storage; no service-object or model-weights substrate is inferred."
      records: [memory.md#mem-rte-evidence-frame, runtime.md#rt-rte-resume-reuse, epistemic.md#epi-rte-score-cache, memory.md#mem-clm-compaction-boundary]
      note: "Filesystem witnesses resolve framework retention, while external alternatives prevent complete inventory classification."
    representational_form:
      assessment: partial
      units:
        - scope: "Retained harness prose at solver interpretation and as improver evidence; reflected experience, cues, response prose and rendered trace narratives"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [runtime.md#rt-obj-harness-text, memory.md#mem-obj-experience, memory.md#mem-obj-library-index, memory.md#mem-obj-cached-response, memory.md#mem-obj-evidence-tree]
              note: "These bodies receive meaning through model interpretation; filesystem delivery alone is not observed reading."
          records: [runtime.md#rt-bap-harness-consumption, memory.md#mem-rte-evidence-frame]
          note: "Classification is of the named text paths, not all material inside the evidence-tree container."
        - scope: "Retained executable harness components at interpreter/hook consumers, navigation addresses, fingerprints, summary predicates and scoring fields"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [runtime.md#rt-obj-harness-code, memory.md#mem-obj-library-index, memory.md#mem-obj-call-fingerprint, runtime.md#rt-rte-resume-reuse, epistemic.md#epi-obj-score-rows]
              note: "Localized code, identifiers and numeric fields have fixed consumer rules; code read as evidence is a different path from execution."
          records: [runtime.md#rt-bap-harness-consumption, runtime.md#rt-rte-resume-reuse, epistemic.md#epi-rte-score-report]
          note: "Only the specified executable/metadata consumers are classified here."
        - scope: "Copied raw images/binaries and native compaction, delegated or provider payloads"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-evidence-tree, memory.md#mem-clm-compaction-boundary, memory.md#mem-rte-evidence-frame]
          note: "Opaque raw assets and external reader/checkpoint semantics cannot be classified from display summaries or configuration."
      records: [memory.md#mem-obj-evidence-tree, runtime.md#rt-obj-harness-code, memory.md#mem-clm-compaction-boundary]
      note: "Textual and symbolic paths are resolved separately; external weights are components, not evidence of a retained parametric update in this boundary."
    lineage:
      assessment: partial
      units:
        - scope: "Automatically retained edited harness content and model-written experience"
          assessment: known
          findings:
            - value: authored
              basis: wired
              records: [runtime.md#rt-rte-edit-admission, memory.md#mem-obj-experience]
              note: "Models author proposed edits and explanatory substance, although fallback can retain unchanged content instead."
            - value: trace-extracted
              basis: wired
              records: [runtime.md#rt-rte-experience-admission, memory.md#mem-obj-experience]
              note: "Reflection consumes execution contrasts and decisions to produce retained experience; semantic validity is not established."
          records: [runtime.md#rt-rte-experience-admission, epistemic.md#epi-rte-lesson-parse]
          note: "The production paths are known even though no generated lesson instance or actual execution is supplied."
        - scope: "Library index, rendered trajectories/diffs, fingerprints and normalized scoring fields"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-library-index, memory.md#mem-obj-evidence-tree, memory.md#mem-obj-call-fingerprint, epistemic.md#epi-rte-judge-result]
              note: "Code enumerates, renders, hashes or normalizes inputs; this does not imply new semantic claims or embedding provenance."
          records: [memory.md#mem-obj-library-index, memory.md#mem-obj-evidence-tree, epistemic.md#epi-obj-score-rows]
          note: "Known derivations concern the recorded projections, not the ultimate truth of their inputs."
        - scope: "Task/source and grader evidence copied from adapters, and unchanged shipped trees admitted as exemplars"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-obj-evidence-tree, epistemic.md#epi-rte-judge-result, memory.md#mem-obj-experience, runtime.md#rt-obj-harness-text]
              note: "Existing task data, external evaluation results and baseline content enter retained contexts without being newly authored by the retaining route."
          records: [epistemic.md#epi-obj-execution-evidence, memory.md#mem-obj-experience]
          note: "Import path is known; source warrant and initial factual provenance are not thereby authenticated."
        - scope: "Scripted demo edits and experience"
          assessment: known
          findings:
            - value: authored
              basis: wired
              records: [memory.md#mem-clm-demo-experience, epistemic.md#epi-rte-demo-check]
              note: "DemoProposer supplies fixed authored text and a fixed edit rather than model-inferred experience."
          records: [memory.md#mem-clm-demo-experience]
          note: "This separate mode prevents generalizing model or trace-extracted authorship to every entry."
        - scope: "Native checkpoint, delegated-return and provider-state derivation"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-clm-compaction-boundary, memory.md#mem-rte-evidence-frame]
          note: "External payload production and initial provenance are not exposed."
      records: [memory.md#mem-obj-experience, memory.md#mem-obj-evidence-tree, memory.md#mem-clm-demo-experience, memory.md#mem-clm-compaction-boundary]
      note: "Known authoring, trace derivation, import and compilation coexist; opaque alternatives prevent a complete lineage union."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Library exemplars, explanations and rendered historical evidence at later improver/composer consumers"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [memory.md#mem-obj-experience, memory.md#mem-rte-evidence-frame, runtime.md#rt-rte-experience-admission]
              note: "Supplied files provide reference and advice, not automatically installed solver instructions or accepted truths."
            - value: learning
              basis: wired
              records: [runtime.md#rt-rte-task-recursion, runtime.md#rt-rte-edit-admission, runtime.md#rt-rte-experience-admission]
              note: "Retained execution evidence and prior experience feed updates to durable harness instructions/code and further experience; improved capacity is not established."
          records: [memory.md#mem-rte-evidence-frame, runtime.md#rt-rte-experience-admission]
          note: "Both effects concern the update consumer; installation is a separate path."
        - scope: "Retained harness prose after selection/adaptation, admission and installation into a fresh solver"
          assessment: known
          findings:
            - value: instruction
              basis: wired
              records: [runtime.md#rt-obj-harness-text, runtime.md#rt-bap-harness-consumption]
              note: "Always-on and on-demand prose directs the solver, conditional on reaching this installed consumer; library membership alone does not grant this force."
          records: [runtime.md#rt-bap-harness-consumption, memory.md#mem-obj-experience]
          note: "Wiring establishes instruction delivery, not reliable compliance."
        - scope: "Retained identity/integrity metadata and saved selection/graded-status fields at cache/resume consumers"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-call-fingerprint, runtime.md#rt-rte-resume-reuse, epistemic.md#epi-rte-score-cache]
              note: "Keys and stored state select cached replies, restored entries, skipped tasks and retained score rows."
            - value: validation
              basis: wired
              records: [runtime.md#rt-rte-resume-reuse]
              note: "Stored harness fingerprint supplies a conformance criterion for accepting reuse."
            - value: enforcement
              basis: wired
              records: [runtime.md#rt-rte-resume-reuse, epistemic.md#epi-rte-score-cache]
              note: "Fingerprint mismatch vetoes reuse; score-cache predicates enforce which saved row survives."
          records: [runtime.md#rt-rte-resume-reuse, epistemic.md#epi-rte-score-cache]
          note: "These are bounded operational controls, not epistemic acceptance of saved content."
        - scope: "Retained WorkBuddy trial grade-availability/recency fields at fresh and batched trial selection"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [runtime.md#rt-rte-solver-execution, runtime.md#rt-rte-resume-reuse]
              note: "Parseable-grade availability influences relative priority before recency; higher score values do not drive this ranking."
          records: [runtime.md#rt-rte-solver-execution, runtime.md#rt-rte-resume-reuse]
          note: "Single-rollout reuse instead uses newest usable trial; neither route validates a lesson."
        - scope: "Retained benchmark score fields at later report computation"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [epistemic.md#epi-obj-score-rows, epistemic.md#epi-rte-score-report]
              note: "Imported evaluator outcomes supply reference data for conditional arithmetic summaries, not adaptation feedback."
          records: [epistemic.md#epi-rte-judge-result, epistemic.md#epi-rte-score-report]
          note: "Reports consume saved rows, but the printed report has no retained later consumer established here."
        - scope: "Generated retained executable hook/plugin/script effects beyond recorded installation, and native-memory payload effects"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-harness-code, runtime.md#rt-bap-harness-consumption, memory.md#mem-clm-compaction-boundary]
          note: "Executable capability alone cannot determine the authority of absent generated code; external checkpoint effects are opaque."
      records: [runtime.md#rt-bap-harness-consumption, memory.md#mem-rte-evidence-frame, runtime.md#rt-rte-resume-reuse, epistemic.md#epi-rte-score-cache, memory.md#mem-clm-compaction-boundary]
      note: "Known consumer-specific forces do not resolve arbitrary extensions or opaque native memory. Index browsing suggests relevance judgment but supplies no separate implemented ranking engine."
    write_agency:
      assessment: partial
      units:
        - scope: "Proposal admission, reflection/library admission, frame copying, index rebuilding, response caching, resume restoration, scheduler prefix withdrawal and score-cache merging"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-edit-admission, runtime.md#rt-rte-experience-admission, memory.md#mem-rte-evidence-frame, memory.md#mem-obj-library-index, memory.md#mem-obj-cached-response, runtime.md#rt-rte-resume-reuse, memory.md#mem-rte-library-withdrawal, epistemic.md#epi-rte-score-cache]
              note: "Software/model admission operates without a human decision approving each retained content item; starting a sweep or judge is not manual admission."
          records: [memory.md#mem-rte-evidence-frame, runtime.md#rt-rte-experience-admission, epistemic.md#epi-rte-score-cache]
          note: "The scripted demo also uses software admission, irrespective of the human origin of its fixed text."
        - scope: "External direct Library API content replacement/withdrawal and initial caller-supplied content decisions"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-library-withdrawal, memory.md#mem-obj-experience]
          note: "Generic caller identity does not establish explicit human content approval or its absence on alternative calls."
        - scope: "Native compaction/delegated/provider admission mechanisms"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-clm-compaction-boundary, memory.md#mem-rte-evidence-frame]
          note: "Configuration is not evidence of checkpoint write control."
      records: [runtime.md#rt-rte-edit-admission, runtime.md#rt-rte-experience-admission, memory.md#mem-rte-library-withdrawal, memory.md#mem-clm-compaction-boundary]
      note: "Automatic framework writes are supported; no explicit per-content human admission witness establishes manual. Alternatives remain unresolved rather than being called automatic."
    curation_operations:
      assessment: partial
      units:
        - scope: "Historical trajectory rendering with observation/argument clipping and whole-prefix caps"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [memory.md#mem-obj-evidence-tree, memory.md#mem-rte-evidence-frame]
              note: "Filtering and clipping reduce retained execution content supplied to later invocations; loss and omissions do not create warrant."
          records: [memory.md#mem-rte-evidence-frame]
          note: "This classifies the implemented reduction of history, not a claim of lossless semantic preservation."
        - scope: "Edits to accumulated current/composed harnesses and replacement of a same-task library entry"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [runtime.md#rt-rte-edit-admission, runtime.md#rt-rte-task-recursion, memory.md#mem-rte-library-withdrawal]
              note: "Existing behavioral artifacts can be revised and retained; unchanged fallback does not itself count as revision."
          records: [runtime.md#rt-rte-edit-admission, memory.md#mem-rte-library-withdrawal]
          note: "The revision mechanism is wired; no particular successful revision is observed."
        - scope: "Scheduler prefix withdrawal and explicit forget/retain deletion capability"
          assessment: known
          findings:
            - value: decay
              basis: wired
              records: [memory.md#mem-rte-library-withdrawal]
              note: "Physical removal forgets entries from future library copies; no global erasure or historical reliance-withdrawal service is inferred."
          records: [memory.md#mem-rte-library-withdrawal]
          note: "Index reconstruction alone is not another curation operation."
        - scope: "Semantic operation of reflection-generated transferable lessons"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-experience-admission, epistemic.md#epi-rte-lesson-parse, epistemic.md#epi-obj-experience]
          note: "The request for a transferable lesson does not establish whether actual content consolidates existing claims or synthesizes a new one; generated content is absent and parsing can lose qualifiers."
        - scope: "Native compaction or provider-side transformations"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-clm-compaction-boundary]
          note: "No implemented native summary transformation is supplied by configuration comments."
      records: [memory.md#mem-rte-evidence-frame, runtime.md#rt-rte-edit-admission, memory.md#mem-rte-library-withdrawal, epistemic.md#epi-rte-lesson-parse, memory.md#mem-clm-compaction-boundary]
      note: "Implemented reduction, revision and forgetting coexist with unresolved lesson semantics and external maintenance. No dedup, promote or synthesize value is inferred from route names."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Automatic library/history supply to later proposal, composition and reflection sessions"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [memory.md#mem-rte-evidence-frame, runtime.md#rt-rte-experience-admission]
              note: "Stage entry triggers code-selected history and domain/mode/prefix library copying without an item request from the receiving session."
          records: [memory.md#mem-rte-evidence-frame]
          note: "Reachability on disk is supplied; actual model-window reading is a later operation."
        - scope: "Model-requested library file opening and caller-requested response, summary, rollout and score-cache retrieval"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [memory.md#mem-obj-library-index, memory.md#mem-rte-evidence-frame, memory.md#mem-obj-cached-response, runtime.md#rt-rte-resume-reuse, epistemic.md#epi-rte-score-report]
              note: "Browsed entries and keyed/reloaded records fulfill consumer requests. Code delivery of requested content is not an additional push."
          records: [memory.md#mem-obj-cached-response, runtime.md#rt-rte-resume-reuse, epistemic.md#epi-rte-score-report]
          note: "File browsing follows the initial coarse supply; exact cache identity does not itself establish targeted push."
        - scope: "Native compaction, skill/delegated retained-return and provider-memory delivery"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-clm-compaction-boundary, memory.md#mem-rte-evidence-frame]
          note: "External payload, trigger and later delivery rules are not available for classification."
      records: [memory.md#mem-rte-evidence-frame, runtime.md#rt-rte-resume-reuse, memory.md#mem-clm-compaction-boundary]
      note: "Both push and pull exist in distinct operations; unresolved external delivery prevents complete direction coverage."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Automatic library/history copying at framework stage entry"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [memory.md#mem-rte-evidence-frame, memory.md#mem-obj-library-index, runtime.md#rt-rte-experience-admission]
              note: "Trigger is stage construction; inputs are domain/mode/preceding-task membership and caller-supplied pool/history; all eligible parts are copied, without cue similarity or top-k targeting."
          records: [memory.md#mem-rte-evidence-frame]
          note: "Entry IDs bound eligible inventory but do not constitute a targeted identity-match push selector."
        - scope: "Requested index browsing/file opens, fingerprint cache return and report reload"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-obj-library-index, memory.md#mem-obj-call-fingerprint, memory.md#mem-obj-cached-response, epistemic.md#epi-rte-score-report]
          note: "These operations are pull; model relevance judgment in requested browsing and exact-key lookup do not classify push signal."
        - scope: "Native compaction/delegated/provider push selection alternatives"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-clm-compaction-boundary, memory.md#mem-rte-evidence-frame]
          note: "Missing selector input and selected retained payload prevent signal classification or pull-only inapplicability."
      records: [memory.md#mem-rte-evidence-frame, memory.md#mem-obj-call-fingerprint, memory.md#mem-clm-compaction-boundary]
      note: "Coarse push has a wired witness; no identifier, lexical, embedding or judgment-based push is established by these records."
    trace_learning:
      assessment: partial
      units:
        - scope: "Execution/history-fed harness revision across fresh stage invocations and ordinary reflection into later-task library experience"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [runtime.md#rt-rte-task-recursion, runtime.md#rt-rte-edit-admission, runtime.md#rt-rte-experience-admission, memory.md#mem-rte-evidence-frame]
              note: "Recorded executions and decisions automatically feed admitted durable behavioral artifacts and experience available to later invocations; no weight update or demonstrated improvement is required."
          records: [runtime.md#rt-rte-experience-admission, memory.md#mem-obj-experience, runtime.md#rt-bap-harness-consumption]
          note: "The trace-to-write-to-later-consumer chain is wired, conditional on successful admission; actual use, valid criticism and benefit remain unobserved."
        - scope: "Scripted demo experience as an alternative producer"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-clm-demo-experience, epistemic.md#epi-rte-demo-check]
          note: "Fixed replacement/text and script-inequality attribution do not establish the ordinary trace-learning chain. No bounded absence record supports a local no."
        - scope: "Native compaction, delegated and provider-retained update routes"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-clm-compaction-boundary, memory.md#mem-rte-evidence-frame]
          note: "Checkpoint production, retention and later consumer are opaque; configuration cannot establish yes or no."
      records: [runtime.md#rt-rte-experience-admission, runtime.md#rt-rte-edit-admission, memory.md#mem-clm-demo-experience, memory.md#mem-clm-compaction-boundary]
      note: "A supported yes survives unresolved alternatives in the existence union; complete learning-inventory coverage and any system-wide no are unwarranted."
    trace_source:
      assessment: partial
      units:
        - scope: "Recorded conversational and tool content rendered into ordinary revision/reflection inputs"
          assessment: known
          findings:
            - value: session-logs
              basis: wired
              records: [memory.md#mem-obj-evidence-tree, memory.md#mem-rte-evidence-frame, runtime.md#rt-rte-experience-admission]
              note: "Solver messages and retained proposer decisions from work sessions feed subsequent behavioral writes."
            - value: tool-traces
              basis: wired
              records: [memory.md#mem-obj-evidence-tree, memory.md#mem-rte-evidence-frame, runtime.md#rt-rte-experience-admission]
              note: "Rendered tool requests, observations and execution feedback feed revision/reflection, subject to clipping and withholding."
            - value: trajectories
              basis: wired
              records: [runtime.md#rt-rte-task-recursion, memory.md#mem-rte-evidence-frame, runtime.md#rt-rte-experience-admission]
              note: "Linked rollout actions/results and associated outcomes supply multi-step experience for proposed revisions and lessons."
          records: [memory.md#mem-obj-evidence-tree, runtime.md#rt-rte-experience-admission]
          note: "These findings concern the recorded trace components, not every mixed input in the update context."
        - scope: "Additional task/source files, generated artifact bodies and opaque binary assets mixed into qualifying updates"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-evidence-tree, epistemic.md#epi-obj-execution-evidence]
          note: "Mixed imported/static and opaque material lacks a complete original-content classification. JSONL event serialization alone does not establish event-streams."
        - scope: "Scripted demo and native compaction/delegated/provider alternative inputs"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-clm-demo-experience, memory.md#mem-clm-compaction-boundary, memory.md#mem-rte-evidence-frame]
          note: "No qualifying demo trace-fed write is established, and external update inputs are opaque; unresolved routes are not made inapplicable by the ordinary route's known inputs."
      records: [memory.md#mem-obj-evidence-tree, runtime.md#rt-rte-experience-admission, memory.md#mem-clm-compaction-boundary]
      note: "Session/tool and multi-step trace content is supported locally; mixed original inputs and external alternatives prevent complete source coverage."
---

# Harness² memory profile

## Comparison rationale

The operative memory is not everything the runtime stores. The comparison covers accumulated behavioral artifacts, execution/history evidence received by later invocations, access metadata and recovery records. Unchanged baseline instructions are excluded until admitted as retained exemplars. External model components do not by themselves establish model-weights memory storage or parametric learning. The opaque native-memory branches remain included uncertainties rather than being erased by the inspected filesystem path. See [MEM-RTE-evidence-frame](memory.md#mem-rte-evidence-frame), [MEM-CLM-compaction-boundary](memory.md#mem-clm-compaction-boundary) and [RT-RTE-resume-reuse](runtime.md#rt-rte-resume-reuse).

No supersessions affect these values: reconciliation retains the declarations as distinct referents. EXPERIENCE.md, the reflected payload and INDEX.md overlap without being interchangeable. The evidence-tree container likewise does not substitute for every opaque raw asset or consumed projection. The profile therefore cites both object and route warrants where their scopes differ. See [MEM-OBJ-experience](memory.md#mem-obj-experience), [EPI-OBJ-experience](epistemic.md#epi-obj-experience), [MEM-OBJ-library-index](memory.md#mem-obj-library-index) and [MEM-OBJ-evidence-tree](memory.md#mem-obj-evidence-tree).

The library reaches improvers as evidence, not automatically as installed solver instructions. At the update consumer, retained execution evidence can have learning authority; at the reference consumer it supplies knowledge; only a subsequently admitted and installed harness grants instruction or executable force to solvers. These paths establish wired trace learning without establishing improved capacity, exercised self-improvement, actual rationale use or lesson truth. The fixed demo is kept separate from ordinary model-authored reflection. See [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission), [RT-BAP-harness-consumption](runtime.md#rt-bap-harness-consumption) and [MEM-CLM-demo-experience](memory.md#mem-clm-demo-experience).

Curation values follow implemented transformations. Clipping reduces historical evidence, edits revise existing harnesses, and prefix deletion forgets entries. Lesson generation requests transferable explanations, but no generated instance establishes whether those explanations merely compress prior claims or add one. The parser can also discard qualifiers. No synthesis finding is derived from that request or defect. See [MEM-RTE-evidence-frame](memory.md#mem-rte-evidence-frame), [MEM-RTE-library-withdrawal](memory.md#mem-rte-library-withdrawal) and [EPI-RTE-lesson-parse](epistemic.md#epi-rte-lesson-parse).

Automatic coarse supply and subsequent requested browsing are separate read-back operations. Exact fingerprints identify requested cache returns, not an unsolicited targeted push. Trial grade-availability ranking is independently supported, but it is neither higher-score preference nor an expected-answer oracle for lesson acceptance. Retained scoring records supply report data, not a wired adaptation update. See [MEM-OBJ-call-fingerprint](memory.md#mem-obj-call-fingerprint), [MEM-RTE-evidence-frame](memory.md#mem-rte-evidence-frame), [RT-RTE-solver-execution](runtime.md#rt-rte-solver-execution) and [EPI-RTE-score-report](epistemic.md#epi-rte-score-report).

Every axis is partial because supported framework findings coexist with included opaque alternatives. Missing external payloads, write control, original inputs and delivery policies prevent complete classification. No bounded absence record licenses a trace-learning no. All positive bases are wired implementation, not observed operation or causal support.

Source-read log: none. This classification uses only the supplied accepted members and reconciliation; no frozen-source ambiguity required an additional read.
