---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "ReasoningBank memory comparison: retained web/coding advice, traces, feedback and query-vector access structures, with alternative-route limits."
run-id: AAS-2026-10-14-reasoning-bank-f0bedcab086c-01
source-identity: https://github.com/google-research/reasoning-bank
reviewed-boundary: ed80611788292ea739f1effd31f16c53823b8a0d
memory-comparison:
  version: 2
  scope: >-
    Retained WebArena and SWE-Bench advice banks and row metadata, query-vector
    caches, saved task trajectories and feedback used by later invocations,
    and web delivery text; ordinary admission/retrieval, successful AWM/Synapse
    alternatives, scaling and standalone induction. Initial nonempty bank/cache
    provenance and admission remain unresolved. Scaling output compatibility and
    standalone launch/later-consumer wiring remain included uncertainties.
    Ancillary retained-memory routes in other runners/adapters remain uninspected,
    not evidenced absent. Excludes static shipped prompts, provider/model weights
    not updated by these memory routes, ordinary episode-local accumulation and
    view truncation without a retained summary, and optional response memoization
    with no established shipped activation. No observed operation or benefit is asserted.
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Ordinary bank content and ledger, query cache, delivery text, saved trajectories and web feedback"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice, memory.md#mem-obj-lineage-ledger, memory.md#mem-obj-query-cache, memory.md#mem-obj-delivery-text, memory.md#mem-obj-trajectory, memory.md#mem-obj-feedback]
              note: "JSONL, text, JSON and compressed pickle are local file encodings, not distinct storage substrates."
          records: [memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice, memory.md#mem-obj-lineage-ledger, memory.md#mem-obj-query-cache, memory.md#mem-obj-delivery-text, memory.md#mem-obj-trajectory, memory.md#mem-obj-feedback]
          note: "The records inventory the operative retained objects; initial content uncertainty does not obscure their inspected file-backed storage."
        - scope: "Loaded cache tensors and retained feedback's host-memory consumption view"
          assessment: known
          findings:
            - value: in-memory
              basis: wired
              records: [memory.md#mem-obj-query-cache, memory.md#mem-obj-feedback]
              note: "Loaded vectors and feedback have host-RAM representations; this does not add provider weights to memory scope."
          records: [memory.md#mem-obj-query-cache, memory.md#mem-obj-feedback]
          note: "RAM is an access/consumption part of the file-backed memory chain."
        - scope: "Scaling and standalone intended output banks"
          assessment: known
          findings:
            - value: files
              basis: afforded
              records: [runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction]
              note: "Append bodies target JSONL files; complete executable invocation is not established."
          records: [runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction]
          note: "Storage destination is classified at affordance strength, independently of reachability and output-shape defects."
        - scope: "Ancillary memory paths in other runners/adapters"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
          note: "The accepted runtime bounds inspection to traced drivers; alternative implementations prevent a complete substrate inventory."
      records: [memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice, memory.md#mem-obj-lineage-ledger, memory.md#mem-obj-query-cache, memory.md#mem-obj-delivery-text, memory.md#mem-obj-trajectory, memory.md#mem-obj-feedback, runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction, runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
      note: "Files and RAM are supported locally; ancillary coverage prevents a system-complete inventory. Dense vectors stored in JSONL do not establish a vector database."
    representational_form:
      assessment: partial
      units:
        - scope: "Ordinary advice, Synapse demonstrations, delivery text and textual trace/feedback parts at model or human consumers"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice, memory.md#mem-obj-delivery-text, memory.md#mem-obj-trajectory, memory.md#mem-obj-feedback, runtime.md#rt-bap-system-memory]
              note: "Advice and displayed action examples take effect through interpretation; action syntax in advice is not dispatched as executable code."
          records: [memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice, memory.md#mem-obj-delivery-text, memory.md#mem-obj-trajectory, memory.md#mem-obj-feedback, runtime.md#rt-bap-system-memory]
          note: "These text consumption paths are distinct from the symbolic wrappers and numerical selector inputs."
        - scope: "Bank/cache identifiers, outcome labels, trace wrappers and recorded action strings at fixed-rule consumers"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-lineage-ledger, memory.md#mem-obj-query-cache, memory.md#mem-obj-trajectory, memory.md#mem-obj-feedback, epistemic.md#epi-obj-web-trajectory]
              note: "Identity joins, status predicates and structured trace extraction operate on localized fields under fixed rules."
          records: [memory.md#mem-obj-lineage-ledger, memory.md#mem-obj-query-cache, memory.md#mem-obj-trajectory, memory.md#mem-obj-feedback, epistemic.md#epi-obj-web-trajectory]
          note: "A trace action can be a symbolic recorded field and a displayed example on a separate interpretation path."
        - scope: "Dense cached query vectors consumed by dot-product ranking"
          assessment: known
          findings:
            - value: parametric
              basis: wired
              records: [memory.md#mem-obj-query-cache]
              note: "Dense distributed numerical representations influence similarity scores; they are not readable summaries or updated task-model weights."
          records: [memory.md#mem-obj-query-cache]
          note: "Cached IDs and query text remain separate symbolic and natural-language parts."
        - scope: "Standalone generated text and metadata"
          assessment: known
          findings:
            - value: natural-language
              basis: afforded
              records: [memory.md#mem-rte-standalone-induction]
              note: "The append body affords generated advice and extracted think/action text."
            - value: symbolic
              basis: afforded
              records: [memory.md#mem-rte-standalone-induction]
              note: "The intended row includes task identity, status and template metadata."
          records: [memory.md#mem-rte-standalone-induction]
          note: "Form is known for the intended row, not proof of completed launch or later interpretation."
        - scope: "Scaling retained payload and its ordinary text consumer compatibility"
          assessment: partial
          findings:
            - value: natural-language
              basis: claimed
              records: [runtime.md#rt-rte-web-scaling]
              note: "Parallel guidance requests combined-trajectory advice, not an established compatible output instance."
          records: [runtime.md#rt-rte-web-scaling, memory.md#mem-obj-lineage-ledger]
          note: "Class invocation and the annotated un-unpacked client tuple prevent classifying the entire operative payload as ordinary prose; requested text is not the whole return object."
        - scope: "Ancillary runner/adapter retained parts"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
          note: "Uninspected alternatives prevent closing the representational inventory."
      records: [memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice, memory.md#mem-obj-delivery-text, memory.md#mem-obj-trajectory, memory.md#mem-obj-feedback, memory.md#mem-obj-lineage-ledger, memory.md#mem-obj-query-cache, epistemic.md#epi-obj-web-trajectory, runtime.md#rt-bap-system-memory, memory.md#mem-rte-standalone-induction, runtime.md#rt-rte-web-scaling, runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
      note: "All three forms have inspected witnesses; the scaling payload and ancillary routes remain unresolved rather than inheriting the ordinary text classification."
    lineage:
      assessment: partial
      units:
        - scope: "Ordinary web/coding advice and successful AWM/Synapse trace-derived content"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [runtime.md#rt-rte-web-admission, runtime.md#rt-rte-swe-admission, memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice]
              note: "Saved task activity feeds generation, workflow extraction or formatted demonstration copying under the inspected branches."
          records: [runtime.md#rt-rte-web-admission, runtime.md#rt-rte-swe-admission, memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice]
          note: "This classifies subsequent derivation, not the provenance of preexisting external rows."
        - scope: "Task queries and copied environment/task text retained in traces, ledger and cache text"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-obj-trajectory, memory.md#mem-obj-lineage-ledger, memory.md#mem-obj-query-cache, runtime.md#rt-rte-swe-task]
              note: "Task/problem and environmental inputs enter retained records from the benchmark/environment boundary."
          records: [memory.md#mem-obj-trajectory, memory.md#mem-obj-lineage-ledger, memory.md#mem-obj-query-cache, runtime.md#rt-rte-swe-task]
          note: "Imported text's truth and source-world authenticity are not established by copying."
        - scope: "New query vectors, generated access fields and flattened delivery text"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-query-cache, memory.md#mem-obj-lineage-ledger, memory.md#mem-obj-delivery-text]
              note: "Embedding computation, row assembly and flattening derive access/delivery objects rather than manually authoring them."
          records: [memory.md#mem-obj-query-cache, memory.md#mem-obj-lineage-ledger, memory.md#mem-obj-delivery-text]
          note: "The current computation is inspected; this does not determine the provenance of old vector rows."
        - scope: "New feedback produced from retained trajectories"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [epistemic.md#epi-rte-web-check, epistemic.md#epi-rte-swe-check, memory.md#mem-obj-feedback]
              note: "Task-activity evidence feeds model outcome judgments and explanation, separately from the advice generator."
          records: [epistemic.md#epi-rte-web-check, epistemic.md#epi-rte-swe-check, memory.md#mem-obj-feedback]
          note: "Outcome extraction is not endorsement of the subsequent advice."
        - scope: "Scaling and standalone intended advice derivation"
          assessment: known
          findings:
            - value: trace-extracted
              basis: afforded
              records: [runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction]
              note: "Both intended append bodies use saved web activity; scaling does not establish distinct-trajectory contrast."
          records: [runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction]
          note: "Afforded derivation is kept separate from the wired ordinary loops."
        - scope: "Initial nonempty banks/caches, external edits and historical vector producer identity"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice, memory.md#mem-obj-query-cache]
          note: "No recorded initial admission or model/version lineage establishes authored, imported or compiled provenance for those existing contents."
        - scope: "Ancillary retained-memory derivation routes"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
          note: "Alternative runners/adapters were not exhaustively inspected."
      records: [runtime.md#rt-rte-web-admission, runtime.md#rt-rte-swe-admission, memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice, memory.md#mem-obj-trajectory, memory.md#mem-obj-lineage-ledger, memory.md#mem-obj-query-cache, memory.md#mem-obj-delivery-text, runtime.md#rt-rte-swe-task, epistemic.md#epi-rte-web-check, epistemic.md#epi-rte-swe-check, memory.md#mem-obj-feedback, runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction, runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
      note: "Known subsequent derivations coexist with unknown initial content and historical embeddings; model authorship alone is not a manual authored-lineage warrant."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Selected ordinary advice consumed by web/coding task models through system messages"
          assessment: known
          findings:
            - value: instruction
              basis: wired
              records: [runtime.md#rt-bap-system-memory, memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice]
              note: "Retained procedural guidance supplies task-horizon directions with model relevance discretion, not an execution veto."
          records: [runtime.md#rt-bap-system-memory, memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice]
          note: "Channel and advisory force are established; compliance and benefit are not."
        - scope: "Synapse demonstrations at the task model and saved trajectory evidence at evaluators/inspectors"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [memory.md#mem-obj-web-advice, memory.md#mem-obj-trajectory, epistemic.md#epi-rte-web-check, epistemic.md#epi-rte-swe-check]
              note: "Demonstrations provide reference context, while traces provide evidence for task judgments; no truth certification follows."
          records: [memory.md#mem-obj-web-advice, memory.md#mem-obj-trajectory, epistemic.md#epi-rte-web-check, epistemic.md#epi-rte-swe-check]
          note: "This is the evidence/reference consumption path, not the downstream procedural direction path."
        - scope: "Retained trajectories and web explanation at ordinary induction consumers"
          assessment: known
          findings:
            - value: learning
              basis: wired
              records: [memory.md#mem-obj-trajectory, memory.md#mem-obj-feedback, runtime.md#rt-rte-web-admission, runtime.md#rt-rte-swe-admission]
              note: "Recorded experience and available feedback feed durable advice production for later tasks; learning authority here does not assert improved capacity."
          records: [memory.md#mem-obj-trajectory, memory.md#mem-obj-feedback, runtime.md#rt-rte-web-admission, runtime.md#rt-rte-swe-admission]
          note: "Coding strips system messages and does not forward judge rationale; the updater's actual view is narrower than the saved trace."
        - scope: "Prior cached vectors at similarity scoring"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [memory.md#mem-obj-query-cache, memory.md#mem-rte-web-retrieval, memory.md#mem-rte-coding-retrieval]
              note: "Retained dense vectors determine relative prior-query priority under dot-product scoring."
          records: [memory.md#mem-obj-query-cache, memory.md#mem-rte-web-retrieval, memory.md#mem-rte-coding-retrieval]
          note: "Stored query prose is not itself rescored after load; advice content and truth do not determine this ranking."
        - scope: "Selected cache/bank IDs at lookup and saved web outcome labels at induction prompt choice"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-query-cache, memory.md#mem-obj-lineage-ledger, memory.md#mem-rte-web-retrieval, memory.md#mem-rte-coding-retrieval, memory.md#mem-obj-feedback, epistemic.md#epi-obj-autoeval]
              note: "Identity equality selects the delivered row; rm or saved reward chooses success/failure generation guidance, not semantic advice acceptance."
          records: [memory.md#mem-obj-query-cache, memory.md#mem-obj-lineage-ledger, memory.md#mem-rte-web-retrieval, memory.md#mem-rte-coding-retrieval, memory.md#mem-obj-feedback, epistemic.md#epi-obj-autoeval]
          note: "Bank status is not a retrieval filter; unconsumed template/status metadata is not assigned authority merely because it is stored."
        - scope: "Scaling and standalone experience at intended advice updaters"
          assessment: known
          findings:
            - value: learning
              basis: afforded
              records: [runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction]
              note: "Their generation bodies afford experience-fed retained advice updates, without a complete working consumer loop."
          records: [runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction]
          note: "This local update-consumer authority does not establish downstream behavior dependence."
        - scope: "Scaling payload and standalone output at later task consumers"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction]
          note: "Scaling's return contract is incompatible/unresolved; standalone has no wired destination consumer. Intended advice cannot establish actual consumed force."
        - scope: "Ancillary memory consumers"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
          note: "Other runners/adapters prevent a complete authority inventory."
      records: [runtime.md#rt-bap-system-memory, memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice, memory.md#mem-obj-trajectory, epistemic.md#epi-rte-web-check, epistemic.md#epi-rte-swe-check, memory.md#mem-obj-feedback, runtime.md#rt-rte-web-admission, runtime.md#rt-rte-swe-admission, memory.md#mem-obj-query-cache, memory.md#mem-rte-web-retrieval, memory.md#mem-rte-coding-retrieval, memory.md#mem-obj-lineage-ledger, epistemic.md#epi-obj-autoeval, runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction, runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
      note: "Separate downstream instruction/reference, update learning, numerical ranking and symbolic routing paths. No retained semantic acceptance criterion or advice execution enforcement is established; that is not a system-wide absence claim."
    write_agency:
      assessment: partial
      units:
        - scope: "Ordinary advice admission, cache creation/append, bank metadata, feedback persistence and delivery-file regeneration"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-web-admission, runtime.md#rt-rte-swe-admission, memory.md#mem-obj-query-cache, memory.md#mem-obj-lineage-ledger, memory.md#mem-obj-feedback, memory.md#mem-obj-delivery-text]
              note: "Software/model admission has no per-content human decision; starting/configuring the pipeline is not manual admission."
          records: [runtime.md#rt-rte-web-admission, runtime.md#rt-rte-swe-admission, memory.md#mem-obj-query-cache, memory.md#mem-obj-lineage-ledger, memory.md#mem-obj-feedback, memory.md#mem-obj-delivery-text]
          note: "Generation authorship and physical filesystem I/O are kept separate from who admits content."
        - scope: "Coding trajectory saver and shipped consumption of saved web trajectory artifacts"
          assessment: partial
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-obj-trajectory, runtime.md#rt-rte-swe-task]
              note: "The coding saver captures messages/configuration and exit information without per-trace approval."
          records: [memory.md#mem-obj-trajectory, runtime.md#rt-rte-web-pipeline, runtime.md#rt-rte-swe-task]
          note: "Installed BrowserGym's full persistence implementation is outside captured code; the complete web-artifact admission mechanism cannot be classified from its later reader alone."
        - scope: "Scaling and standalone advice admission bodies"
          assessment: known
          findings:
            - value: automatic
              basis: afforded
              records: [runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction]
              note: "Both bodies admit generated outputs computationally, with no item approval, but complete invocation is not established."
          records: [runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction]
          note: "CLI path selection supplies configuration, not a decision approving the retained content."
        - scope: "Initial nonempty bank/cache contents and external edits"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice, memory.md#mem-obj-query-cache, memory.md#mem-obj-delivery-text]
          note: "The records do not identify a content-supplying human decision or a software admission path for externally prepared or changed material. Manual is not inferred."
        - scope: "Ancillary retained-memory admissions"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
          note: "Alternative entry points are not exhaustively inspected."
      records: [runtime.md#rt-rte-web-admission, runtime.md#rt-rte-swe-admission, memory.md#mem-obj-query-cache, memory.md#mem-obj-lineage-ledger, memory.md#mem-obj-feedback, memory.md#mem-obj-delivery-text, memory.md#mem-obj-trajectory, runtime.md#rt-rte-web-pipeline, runtime.md#rt-rte-swe-task, runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction, memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice, runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
      note: "Automatic subsequent admissions are supported without resolving external initialization, web-host persistence internals or ancillary writes."
    curation_operations:
      assessment: partial
      units:
        - scope: "Ordinary saved-trajectory selection and compressed extraction into advice"
          assessment: partial
          findings:
            - value: consolidate
              basis: wired
              records: [runtime.md#rt-rte-web-admission, runtime.md#rt-rte-swe-admission, memory.md#mem-obj-trajectory, memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice]
              note: "Retained task records are narrowed to think/action or non-system transcript views and extracted into reduced advice representations; raw records may remain."
          records: [runtime.md#rt-rte-web-admission, runtime.md#rt-rte-swe-admission, memory.md#mem-obj-trajectory, memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice, epistemic.md#epi-obj-web-memory, epistemic.md#epi-obj-swe-memory]
          note: "Consolidation applies to retained traces, not revision of old advice. Generated propositions are unavailable, so synthesis beyond the inputs is not determined; generalization requests do not establish a new claim."
        - scope: "Scaling and standalone intended trace reduction"
          assessment: partial
          findings:
            - value: consolidate
              basis: afforded
              records: [runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction]
              note: "The intended generation bodies compress saved activity into advice; scaling's claimed distinct-trajectory comparison is not wired."
          records: [runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction]
          note: "Launch/output defects limit the implementation basis, and no generated artifact resolves whether novel claims are synthesized."
        - scope: "Other bank/cache maintenance, Synapse copying, initial external edits and ancillary transformations"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-web-advice, memory.md#mem-obj-lineage-ledger, memory.md#mem-obj-query-cache, memory.md#mem-obj-trajectory, runtime.md#rt-rte-context-control]
          note: "Trace copying, cache append and delivery overwrite alone establish none of the controlled curation operations. Template-ID comments do not establish deduplication; cleanup does not withdraw advice. External edits and ancillary paths remain unresolved, so no complete negative is asserted."
      records: [runtime.md#rt-rte-web-admission, runtime.md#rt-rte-swe-admission, memory.md#mem-obj-trajectory, memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice, epistemic.md#epi-obj-web-memory, epistemic.md#epi-obj-swe-memory, runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction, memory.md#mem-obj-lineage-ledger, memory.md#mem-obj-query-cache, runtime.md#rt-rte-context-control]
      note: "Positive consolidation concerns retained traces. It does not upgrade prompt requests for non-overlap, reflection or generalization into deduplication, evolution or demonstrated synthesis."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Runner requests to bank/cache selectors and explicit readers of retained trajectories/feedback"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [memory.md#mem-rte-web-retrieval, memory.md#mem-rte-coding-retrieval, memory.md#mem-obj-trajectory, memory.md#mem-obj-feedback]
              note: "Runner calls request retained advice; induction/evaluation and the inspector explicitly load saved artifacts. A requested return is not an additional push."
          records: [memory.md#mem-rte-web-retrieval, memory.md#mem-rte-coding-retrieval, memory.md#mem-obj-trajectory, memory.md#mem-obj-feedback]
          note: "Pull describes requests within the chain, not whether the foreground task model asked to receive memory."
        - scope: "Automatic prior-advice selection and system-message supply during ordinary task setup"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [memory.md#mem-rte-web-retrieval, memory.md#mem-rte-coding-retrieval, runtime.md#rt-bap-system-memory]
              note: "Task setup automatically selects a prior row and supplies its advice to the task model without that model requesting retained material."
          records: [memory.md#mem-rte-web-retrieval, memory.md#mem-rte-coding-retrieval, runtime.md#rt-bap-system-memory]
          note: "The user requested task work, not a memory lookup by the task model. This local supply operation coexists with the runner's selector pull."
        - scope: "Standalone output and scaling payload reaching a later consumer"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-standalone-induction, runtime.md#rt-rte-web-scaling]
          note: "Standalone destination has no established later consumer; scaling's invocation/return-shape defects prevent establishing delivery of compatible retained content."
        - scope: "Ancillary memory read-back"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
          note: "Alternative runners/adapters prevent complete direction coverage."
      records: [memory.md#mem-rte-web-retrieval, memory.md#mem-rte-coding-retrieval, memory.md#mem-obj-trajectory, memory.md#mem-obj-feedback, runtime.md#rt-bap-system-memory, memory.md#mem-rte-standalone-induction, runtime.md#rt-rte-web-scaling, runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
      note: "Both request-side pull and automatic task-model supply push exist in the ordinary chain; unresolved alternatives prevent complete coverage."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Automatic web/coding advice supply: task intent/problem to prior cached queries"
          assessment: known
          findings:
            - value: inferred-embedding
              basis: wired
              records: [memory.md#mem-obj-query-cache, memory.md#mem-rte-web-retrieval, memory.md#mem-rte-coding-retrieval]
              note: "Trigger is task setup; selector embeds the current task under an instruction and ranks retained prior-query vectors. One prior record is selected, not a fixed token budget."
            - value: identifier
              basis: wired
              records: [memory.md#mem-rte-web-retrieval, memory.md#mem-rte-coding-retrieval, memory.md#mem-obj-lineage-ledger]
              note: "Ranked cache IDs are matched against bank task_id; the first equal row supplies every memory_items block. This equality actually selects delivered content, not just a catalog label."
          records: [memory.md#mem-obj-query-cache, memory.md#mem-rte-web-retrieval, memory.md#mem-rte-coding-retrieval, memory.md#mem-obj-lineage-ledger]
          note: "Embedding priority and identity join are distinct selector operations in the same push chain. Availability checks and n=1 do not add coarse targeting."
        - scope: "Standalone/scaling and ancillary push alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-standalone-induction, runtime.md#rt-rte-web-scaling, runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
          note: "Later delivery is unresolved for standalone/scaling and ancillary routes are uninspected. Their signals cannot be inferred from the ordinary selector or declared inapplicable."
      records: [memory.md#mem-obj-query-cache, memory.md#mem-rte-web-retrieval, memory.md#mem-rte-coding-retrieval, memory.md#mem-obj-lineage-ledger, memory.md#mem-rte-standalone-induction, runtime.md#rt-rte-web-scaling, runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
      note: "Embedding inference and an operative identifier match are wired witnesses; unresolved read-back branches prevent a complete signal inventory."
    trace_learning:
      assessment: partial
      units:
        - scope: "Ordinary web and coding automatic trajectory-to-advice writes and later task-model consumption"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [runtime.md#rt-rte-web-admission, runtime.md#rt-rte-swe-admission, memory.md#mem-obj-trajectory, memory.md#mem-rte-web-retrieval, memory.md#mem-rte-coding-retrieval, runtime.md#rt-bap-system-memory]
              note: "Automatic trace-fed generation appends durable behavior-shaping text that later tasks reload into the system message. No weight update or observed gain is needed for this architectural classification."
          records: [runtime.md#rt-rte-web-admission, runtime.md#rt-rte-swe-admission, memory.md#mem-obj-trajectory, memory.md#mem-rte-web-retrieval, memory.md#mem-rte-coding-retrieval, runtime.md#rt-bap-system-memory]
          note: "The consumer chain is wired; actual learning as improved capacity and downstream causal dependence remain unobserved."
        - scope: "Scaling/standalone writes, initial external content and ancillary automatic updates"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction, memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice, memory.md#mem-obj-query-cache, runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
          note: "Scaling lacks complete executable compatible production, standalone lacks a later consumer, and external/ancillary update chains remain unresolved. Raw persistence or query caching alone does not establish a qualifying trace-fed update."
      records: [runtime.md#rt-rte-web-admission, runtime.md#rt-rte-swe-admission, memory.md#mem-obj-trajectory, memory.md#mem-rte-web-retrieval, memory.md#mem-rte-coding-retrieval, runtime.md#rt-bap-system-memory, runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction, memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice, memory.md#mem-obj-query-cache, runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
      note: "A positive ordinary-loop witness does not resolve other write-to-consumer chains; no unsupported local or system-wide negative is inferred."
    trace_source:
      assessment: partial
      units:
        - scope: "Ordinary WebArena saved think/action trajectory and outcome-conditioned advice write"
          assessment: known
          findings:
            - value: trajectories
              basis: wired
              records: [runtime.md#rt-rte-web-admission, memory.md#mem-obj-trajectory, memory.md#mem-obj-web-advice]
              note: "Ordered thought/action experience and outcome feed retained advice. Full page observations are omitted from ordinary induction; trajectory classification does not assert a complete world-state record."
          records: [runtime.md#rt-rte-web-admission, memory.md#mem-obj-trajectory, memory.md#mem-obj-web-advice]
          note: "The input is reconstructed multi-step task experience, not merely timestamped events or an adapter-defined role."
        - scope: "Ordinary coding non-system transcript consumed by judge/generator"
          assessment: known
          findings:
            - value: session-logs
              basis: wired
              records: [runtime.md#rt-rte-swe-admission, memory.md#mem-obj-trajectory]
              note: "Saved conversational turns include task/user text and assistant responses; system messages, including selected prior advice, are stripped."
            - value: tool-traces
              basis: wired
              records: [runtime.md#rt-rte-swe-task, runtime.md#rt-rte-swe-admission, memory.md#mem-obj-trajectory]
              note: "The transcript includes command requests and formatted environment observations/execution feedback, not just model reasoning."
            - value: trajectories
              basis: wired
              records: [runtime.md#rt-rte-swe-task, runtime.md#rt-rte-swe-admission, memory.md#mem-obj-trajectory]
              note: "Linked command/observation turns and task completion judgment supply multi-step experience to the durable advice write."
          records: [runtime.md#rt-rte-swe-task, runtime.md#rt-rte-swe-admission, memory.md#mem-obj-trajectory]
          note: "Several source values characterize different qualifying contents of the same mixed transcript; message role alone does not turn tool feedback into ordinary user-authored prose."
        - scope: "Scaling and standalone candidate trace-fed writes"
          assessment: partial
          findings:
            - value: trajectories
              basis: afforded
              records: [runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction]
              note: "Intended generators consume saved web think/action experience, with scaling repeatedly loading the same directory rather than distinct trials."
          records: [runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction]
          note: "Original input type is known at the afforded generator; executable update and later-consumer qualification remain unresolved, so this is not a wired additional learning loop."
        - scope: "Initial external material and ancillary qualifying update inputs"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-web-advice, memory.md#mem-obj-coding-advice, memory.md#mem-obj-query-cache, runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
          note: "No complete qualifying update/input chain establishes origin for preexisting contents or uninspected alternatives. They cannot be made inapplicable by the known ordinary routes."
      records: [runtime.md#rt-rte-web-admission, memory.md#mem-obj-trajectory, memory.md#mem-obj-web-advice, runtime.md#rt-rte-swe-admission, runtime.md#rt-rte-swe-task, runtime.md#rt-rte-web-scaling, memory.md#mem-rte-standalone-induction, memory.md#mem-obj-coding-advice, memory.md#mem-obj-query-cache, runtime.md#rt-rte-context-control, runtime.md#rt-rte-client-selection]
      note: "Ordinary learning routes consume web trajectories and mixed coding session/tool/trajectory records. No event-stream source is established merely by serialized or ordered activity."
---

# ReasoningBank memory profile

## Comparison rationale

This profile classifies accepted records only. No source files were read and no new evidence or records were added. The records' passages supply the warrants; no finding claims observed operation or causal benefit.

**Inventory and uncertainty.** The retained-object inventory separates [MEM-OBJ-web-advice](memory.md#mem-obj-web-advice), [MEM-OBJ-coding-advice](memory.md#mem-obj-coding-advice), [MEM-OBJ-lineage-ledger](memory.md#mem-obj-lineage-ledger), [MEM-OBJ-query-cache](memory.md#mem-obj-query-cache), [MEM-OBJ-delivery-text](memory.md#mem-obj-delivery-text), [MEM-OBJ-trajectory](memory.md#mem-obj-trajectory) and [MEM-OBJ-feedback](memory.md#mem-obj-feedback). Initial content control is not inferred from known subsequent writes. Exact vector producer/version lineage is unresolved, even though the inspected append computes new embeddings. Provider weights are separate computations, not accumulated memory updated by these routes. Ordinary episode histories and truncation without a durable summary are described by [RT-RTE-context-control](runtime.md#rt-rte-context-control), but do not add a compaction learning route. Ancillary alternatives remain uncertainty units rather than disappearing from coverage.

**Read-back is operation-relative.** The memory member calls [MEM-RTE-web-retrieval](memory.md#mem-rte-web-retrieval) and [MEM-RTE-coding-retrieval](memory.md#mem-rte-coding-retrieval) host-triggered requested setup rather than unsolicited background push. That source-native characterization is preserved. Under this profile's definition, the runner pulls from its selector while automatic setup pushes selected advice into a task model that did not request retained material. The initiating task request is not itself a memory request by that consumer. The same chain therefore supports both directions without counting a requested selector return as an extra push. Similarity ranks cached queries; a subsequent task-ID equality really selects the delivered row. Both selector operations matter. The bank's status and template labels do not establish quality filtering or deduplication.

**Curation and learning are separate.** The reports distinguish extracting from traces from consolidating or revising old advice. The profile's broader consolidation definition includes reducing retained traces, so ordinary [RT-RTE-web-admission](runtime.md#rt-rte-web-admission) and [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission) support that operation. The absence of generated propositions prevents deciding whether any additional claim is synthesized; instructions to generalize do not settle that question. Automatic trace-fed durable advice plus later delivery establishes architectural trace learning, independently of improved capacity, actual decision dependence or a parameter update. Retained experience has learning authority at the updater; advice has instruction authority downstream, dense vectors have ranking force, and lookup/outcome fields route specific operations. These are separate consumers, not interchangeable labels.

**Alternative routes retain their own evidence strength.** [RT-RTE-web-scaling](runtime.md#rt-rte-web-scaling) affords intended retention but has repeated-directory inputs, client invocation and output-shape defects. Its requested prose cannot classify an entire incompatible tuple payload. [MEM-RTE-standalone-induction](memory.md#mem-rte-standalone-induction) has an append body but unresolved imports/launch context and no established later destination consumer. Neither inherits the ordinary loops' wired trace-learning finding. Intended trajectory inputs can be classified at affordance strength while the complete learning chain remains unresolved.

**Canonical identities.** Reconciliation supersedes EPI-RTE-query-selection with [MEM-RTE-web-retrieval](memory.md#mem-rte-web-retrieval), and EPI-RTE-legacy-induction with [MEM-RTE-standalone-induction](memory.md#mem-rte-standalone-induction). This profile uses those canonical routes; their findings remain bounded to wired ordinary selection and afforded standalone induction respectively. The epistemic web/coding memory containers remain distinct from their content and ledger parts, so their semantic uncertainty can be cited without treating them as duplicate routes. No supersession upgrades a local basis or removes uncertainty.
