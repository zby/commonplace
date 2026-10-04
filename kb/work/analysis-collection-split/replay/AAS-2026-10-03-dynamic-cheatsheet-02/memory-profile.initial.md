---
type: work/analysis-collection-split/drafts/agent-memory-profile.md
description: "Memory profile of Dynamic Cheatsheet's retained cheatsheets, task examples and retrieval vectors"
run-id: AAS-2026-10-03-dynamic-cheatsheet-02
source-identity: https://github.com/suzgunmirac/dynamic-cheatsheet
reviewed-boundary: 5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9
memory-comparison:
  scope: "Cumulative cheatsheet text; persisted task and response examples; supplied retrieval vectors that select examples; initialization, JSONL persistence and continuation; later model consumers. Excludes static prompts, task targets and scores that do not feed memory routes, provider internals, and unretained request context."
  axes:
    storage_substrate:
      assessment: known
      values: [files, in-memory]
      evidence:
        files:
          basis: wired
          records: [MEM-OBJ-1, MEM-OBJ-2, MEM-OBJ-3]
          note: "The runner persists cheatsheet and interaction rows in JSONL, while supplied retrieval vectors are checked-in CSV files."
        in-memory:
          basis: wired
          records: [MEM-OBJ-1, MEM-OBJ-2, MEM-OBJ-3]
          note: "The runner and retrieval code hold the text, reconstructed history and loaded vectors in process memory."
      records: [MEM-OBJ-1, MEM-OBJ-2, MEM-OBJ-3, RT-OBJ-1, RT-OBJ-2]
      note: "All included retained parts have a declared substrate. Provider-controlled parameters and transient request context are outside this memory boundary; no database or separate memory service is declared."
    representational_form:
      assessment: known
      values: [natural-language, parametric]
      evidence:
        natural-language:
          basis: wired
          records: [MEM-OBJ-1, MEM-OBJ-2, MEM-RTE-1, MEM-RTE-2, MEM-RTE-4]
          note: "Cheatsheets and task/output examples are text interpreted by later model calls; synthesis also produces a text view. JSON row fields organize these contents."
        parametric:
          basis: afforded
          records: [MEM-OBJ-3, MEM-RTE-3]
          note: "Dense vectors select examples through cosine similarity. Their embedding model and generation process are unknown."
      records: [MEM-OBJ-1, MEM-OBJ-2, MEM-OBJ-3, MEM-RTE-1, MEM-RTE-2, MEM-RTE-3, MEM-RTE-4]
      note: "The scoped operative contents are text and dense vectors. JSON field structure is their serialization and access organization; no separately operative symbolic content is identified. Provider model weights are outside the memory boundary."
    lineage:
      assessment: partial
      values: [imported, trace-extracted]
      evidence:
        imported:
          basis: afforded
          records: [MEM-OBJ-1, MEM-OBJ-3]
          note: "The runner can initialize from a supplied cheatsheet file, and retrieval consumes supplied checked-in vectors. The origin and authorship of both are unknown."
        trace-extracted:
          basis: wired
          records: [MEM-RTE-1, MEM-RTE-4, MEM-OBJ-1]
          note: "Curation routes derive persistent text from current questions, generator outputs and prior context. This supports trace-derived lineage for those outputs, not every initialized value."
      records: [MEM-OBJ-1, MEM-OBJ-2, MEM-OBJ-3, MEM-RTE-1, MEM-RTE-2, MEM-RTE-3, MEM-RTE-4]
      note: "Known paths include supplied/imported vectors and optional initial cheatsheet text, plus text derived from task interactions. Unknown initial cheatsheet and vector provenance prevent complete lineage coverage. No record establishes authored or other-compiled lineage for the supplied materials."
    behavioral_authority:
      assessment: known
      values: [knowledge, ranking, routing, learning]
      evidence:
        knowledge:
          basis: wired
          records: [MEM-OBJ-1, MEM-OBJ-2, MEM-RTE-1, MEM-RTE-2, MEM-RTE-4]
          note: "Later generators receive cheatsheet text or prior task/response examples as reference and context; actual model use is unobserved."
        ranking:
          basis: wired
          records: [MEM-OBJ-3, MEM-RTE-3]
          note: "Cosine similarity over retained vectors determines the relative priority of prior examples."
        routing:
          basis: wired
          records: [MEM-OBJ-3, MEM-RTE-3]
          note: "Top-k vector selection chooses which retained examples enter the current generator input."
        learning:
          basis: wired
          records: [MEM-RTE-1, MEM-RTE-4, RT-RTE-1, RT-RTE-2]
          note: "Interaction-fed curation writes persistent text later supplied to model calls. This establishes a behavior-shaping route, not observed improvement or model compliance."
      records: [MEM-OBJ-1, MEM-OBJ-2, MEM-OBJ-3, MEM-RTE-1, MEM-RTE-2, MEM-RTE-3, MEM-RTE-4, RT-RTE-1, RT-RTE-2]
      note: "The records establish knowledge delivery, vector-based priority and input selection, and trace-fed durable text updates. No retained control vetoes an operation or validates admission; task scoring does not feed memory routes."
    write_agency:
      assessment: known
      values: [automatic, manual]
      evidence:
        automatic:
          basis: wired
          records: [MEM-RTE-1, MEM-RTE-2, MEM-RTE-4, MEM-OBJ-2]
          note: "The runner records rows and adopts parsed curation output automatically; append-all and synthesis routes construct context without human approval."
        manual:
          basis: afforded
          records: [MEM-OBJ-1, RT-RTE-1]
          note: "An operator can choose an initialization file whose cheatsheet text is loaded into state. The records do not establish who authored that file."
      records: [MEM-OBJ-1, MEM-OBJ-2, MEM-RTE-1, MEM-RTE-2, MEM-RTE-4, RT-RTE-1]
      note: "Both automated writes and operator-selected file initialization are within scope. No manual approval gate for ongoing curation is wired."
    curation_operations:
      assessment: known
      values: [consolidate, dedup, evolve, synthesize]
      evidence:
        consolidate:
          basis: wired
          records: [MEM-RTE-1, RT-RTE-1]
          note: "The cumulative curator receives new interaction material and prior cheatsheet to produce a reduced standing text; output correctness is unverified."
        dedup:
          basis: wired
          records: [MEM-RTE-1, RT-RTE-1, RT-CLM-1]
          note: "The cumulative curator prompt directs removal of redundancy during replacement. This is wired guidance, not evidence that a particular duplicate was removed."
        evolve:
          basis: wired
          records: [MEM-RTE-1, RT-RTE-1]
          note: "The updater proposes refined replacements based on new task material and previous cheatsheet text. No observed revision is supplied."
        synthesize:
          basis: wired
          records: [MEM-RTE-4, RT-RTE-2]
          note: "The retrieval-synthesis curator is called to produce a text view from selected examples, next input and prior returned context. Its output is not observed."
      records: [MEM-RTE-1, MEM-RTE-2, MEM-RTE-3, MEM-RTE-4, RT-RTE-1, RT-RTE-2, RT-CLM-1]
      note: "The supplied routes support consolidation, instructed de-duplication, revision and synthesis. Similarity ranking alone is selection, not curation. Replacement can omit content, but no explicit invalidation operation exists; no decay or promotion route is recorded."
    read_back_direction:
      assessment: known
      values: [pull, push]
      evidence:
        pull:
          basis: wired
          records: [MEM-RTE-1, MEM-RTE-2, MEM-RTE-3, MEM-RTE-4, RT-RTE-1]
          note: "Continuation selected through a CLI file argument reloads retained rows and the latest cheatsheet for the requested run."
        push:
          basis: wired
          records: [MEM-RTE-1, MEM-RTE-2, MEM-RTE-3, MEM-RTE-4, RT-RTE-1, RT-RTE-2]
          note: "Normal item processing supplies cheatsheet text, appended history, top-k examples or synthesized context to later model calls without a per-item consumer request."
      records: [MEM-RTE-1, MEM-RTE-2, MEM-RTE-3, MEM-RTE-4, RT-RTE-1, RT-RTE-2]
      note: "The boundary includes both explicit continuation reads and automatic later prompt supply. Their selectors and consumers differ by approach."
    read_back_signal:
      assessment: known
      values: [coarse, inferred-embedding]
      evidence:
        coarse:
          basis: wired
          records: [MEM-RTE-1, MEM-RTE-2, MEM-RTE-4]
          note: "Cumulative text is supplied whole and full-history mode appends all prior pairs; no retained-content budget or identity match selects individual entries on these routes."
        inferred-embedding:
          basis: wired
          records: [MEM-OBJ-3, MEM-RTE-3]
          note: "The current question's supplied vector is compared with prior vectors, and cosine top-k selects corresponding retained examples."
      records: [MEM-RTE-1, MEM-RTE-2, MEM-RTE-3, MEM-RTE-4]
      note: "Push includes whole-text and append-all availability as well as similarity-based selection. No identifier match or inferred judgment/lexical selector is recorded; continuation pull does not add a push signal."
    trace_learning:
      assessment: known
      values: ["yes"]
      evidence:
        "yes":
          basis: wired
          records: [MEM-RTE-1, MEM-RTE-4, RT-RTE-1, RT-RTE-2]
          note: "Interaction traces feed automatic curation routes that persist text for later model consumers. The classification is about the wired durable update route, not demonstrated improvement."
      records: [MEM-RTE-1, MEM-RTE-2, MEM-RTE-4, RT-RTE-1, RT-RTE-2]
      note: "Cumulative and synthesis curation supply qualifying trace-fed durable text. Raw row retention alone is not the warrant. No route is recorded as automatically learning from event streams or trajectories."
    trace_source:
      assessment: known
      values: [session-logs, tool-traces]
      evidence:
        session-logs:
          basis: wired
          records: [MEM-RTE-1, MEM-RTE-4]
          note: "Questions and generator outputs from benchmark interactions feed the automatic text updates."
        tool-traces:
          basis: wired
          records: [MEM-RTE-1, RT-RTE-3, RT-RTE-4]
          note: "When model-requested execution is enabled, returned execution output can enter the generator output that curation later receives; this is a wired conditional path, with no execution observed."
      records: [MEM-RTE-1, MEM-RTE-4, RT-RTE-1, RT-RTE-2, RT-RTE-3, RT-RTE-4]
      note: "The qualifying writes consume session interaction content and can consume returned code-execution feedback embedded in generator outputs. The records do not show event-stream or trajectory input to these writes."
---

# Dynamic Cheatsheet memory profile

## Comparison rationale

The compared boundary is the runner-managed cheatsheet, persisted task and response rows, and supplied vectors used to select earlier examples. The vectors are a separate operative access structure inside the history container. Static prompts, task targets and post-answer scores do not become memory values because the supplied records show no path from them into memory admission or later selection. Reconciliation leaves the containers and their parts intact and confirms EPI-RTE-1 does not add a memory classification.

Lineage is partial. The records establish supplied/imported vectors and an optional supplied initial cheatsheet, but not their origins; they also establish automatic text derivation from task interactions. This supports imported and trace-extracted paths without extending either to all included material. Structured JSON fields organize stored text, while dense vectors are parametric and text is natural-language. No separate operative symbolic memory content is established.

The profile includes knowledge, ranking and routing because retained text supplies context and vector similarity orders and selects examples. It includes learning and trace-learning `yes` because interaction-fed curation is wired to persist new text for later model calls; it does not claim observed learning benefit. Manual write agency refers only to choosing and loading an initialization file. Curation includes the wired cumulative replacement and retrieval-synthesis routes, with prompt-directed de-duplication retained at implementation strength. Similarity selection is not itself curation.

Read-back includes pull through explicit continuation and push through automatic later prompt supply. Push signals include coarse whole-content or append-all supply and inferred-embedding selection. Tool-trace source is conditional: execution feedback can flow into generator output and then into persistent curation, but the records contain no observed execution. The reconciliation's unresolved evaluator-helper coverage affects epistemic completeness, not a memory route, so it leaves these classifications unchanged. Provider outputs, actual activation, content correctness and benefit remain unobserved.
