---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "ExpeL memory comparison covering retained trials, retry reflections, maintained rules, access state and checkpoint reuse."
run-id: AAS-2026-10-14-expel-efd908f05069-01
source-identity: https://github.com/LeapLabTHU/ExpeL
reviewed-boundary: e41ec9a24823e7b560c561ab191441b56d9bcefc
memory-comparison:
  version: 2
  scope: "Use-derived trial histories, retry reflections and their archives, rule text and fold caches, rule counters, persisted trial/critique logs and resume state, rebuilt retrieval documents/vectors and their access metadata, and auxiliary critique dictionaries with unresolved later consumers. Includes training, extraction, retry, evaluation, checkpoint replacement and reporting routes. Excludes shipped static examples and method prompts as memory objects, ordinary unretained task frames, external model weights and provider-internal retention; includes the access structures derived from retained experience, not the embedding model itself."
  axes:
    storage_substrate:
      assessment: known
      units:
        - scope: "Trial histories, reflection copies, rules/caches, counters, logs and resume state"
          assessment: known
          findings:
            - value: in-memory
              basis: wired
              records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-reflections, memory.md#mem-obj-rule-items, memory.md#mem-obj-rule-counts, memory.md#mem-obj-analysis-logs]
              note: "Agent containers hold text, trajectories, counters and selected state."
            - value: files
              basis: wired
              records: [memory.md#mem-obj-analysis-logs, runtime.md#rt-rte-checkpoint-restore]
              note: "Text logs and pickle snapshots retain these parts across processes; encoding does not imply a database substrate."
          records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-reflections, memory.md#mem-obj-rule-items, memory.md#mem-obj-rule-counts, memory.md#mem-obj-analysis-logs, runtime.md#rt-rte-checkpoint-restore]
          note: "Records cover the operative retained containers and their persistence; no checkpoint instance or successful write was observed."
        - scope: "Rebuilt retrieval documents, mappings and FAISS access store"
          assessment: known
          findings:
            - value: in-memory
              basis: wired
              records: [memory.md#mem-obj-retrieval-docs]
              note: "Documents and task metadata are rebuilt in RAM."
            - value: vector
              basis: wired
              records: [memory.md#mem-obj-retrieval-docs, runtime.md#rt-cmp-embedder]
              note: "FAISS supplies the vector access substrate; no persistent FAISS export is established."
          records: [memory.md#mem-obj-retrieval-docs, runtime.md#rt-cmp-embedder]
          note: "Numerical encoding and vector substrate are separate classifications."
        - scope: "Auxiliary critique dictionaries and optional dictionary snapshots"
          assessment: known
          findings:
            - value: in-memory
              basis: afforded
              records: [memory.md#mem-obj-critiques, memory.md#mem-rte-auxiliary-critique]
              note: "Helper invocation affords dictionary population, conditional on custom compatible templates."
            - value: files
              basis: afforded
              records: [memory.md#mem-obj-critiques, runtime.md#rt-rte-checkpoint-restore]
              note: "Populated dictionaries are eligible for snapshots; this is not observed persistence."
          records: [memory.md#mem-obj-critiques, memory.md#mem-rte-auxiliary-critique, runtime.md#rt-rte-checkpoint-restore]
          note: "Known substrate classification does not imply a functioning shipped auxiliary generation loop."
      records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-reflections, memory.md#mem-obj-rule-items, memory.md#mem-obj-rule-counts, memory.md#mem-obj-retrieval-docs, memory.md#mem-obj-analysis-logs, memory.md#mem-obj-critiques, runtime.md#rt-rte-checkpoint-restore]
      note: "The recorded object inventory covers scoped memory storage, including conditional auxiliary objects; external weights are not accumulated memory here."
    representational_form:
      assessment: known
      units:
        - scope: "Trial, reflection, rule, retrieval-document and log text"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-reflections, memory.md#mem-obj-rule-items, memory.md#mem-obj-retrieval-docs, memory.md#mem-obj-analysis-logs]
              note: "Models or reporting readers interpret retained task, action, observation and guidance text."
          records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-reflections, memory.md#mem-obj-rule-items, memory.md#mem-obj-retrieval-docs, memory.md#mem-obj-analysis-logs]
          note: "No generated payload is needed to establish the wired text channels; its substantive correctness remains unknown."
        - scope: "Task/fold keys, trajectory partitions, counters, retrieval metadata and resume containers"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-rule-counts, memory.md#mem-obj-retrieval-docs, memory.md#mem-obj-analysis-logs, memory.md#mem-obj-rule-items]
              note: "Localized keys, integers and containers have fixed software meanings independently of their contained prose."
          records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-rule-counts, memory.md#mem-obj-retrieval-docs, memory.md#mem-obj-analysis-logs, memory.md#mem-obj-rule-items]
          note: "The symbolic part is not an alternative description of the text's model-interpreted force."
        - scope: "Dependency-created dense representations used by retrieval"
          assessment: known
          findings:
            - value: parametric
              basis: wired
              records: [memory.md#mem-obj-retrieval-docs, runtime.md#rt-cmp-embedder]
              note: "Dense numerical access representations are distributed-parametric, not readable demonstrations or symbolic counters."
          records: [memory.md#mem-obj-retrieval-docs, runtime.md#rt-cmp-embedder]
          note: "Form is classified without claiming immutable embedding provenance or parameter updates."
        - scope: "Auxiliary critique text and task/group keys"
          assessment: known
          findings:
            - value: natural-language
              basis: afforded
              records: [memory.md#mem-obj-critiques, memory.md#mem-rte-auxiliary-critique]
              note: "Conditional helper outputs are text lists."
            - value: symbolic
              basis: afforded
              records: [memory.md#mem-obj-critiques, memory.md#mem-rte-auxiliary-critique]
              note: "Task/group keys organize those lists through fixed code."
          records: [memory.md#mem-obj-critiques, memory.md#mem-rte-auxiliary-critique]
          note: "Both forms are known for this conditional object, not evidence of successful default dispatch."
      records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-reflections, memory.md#mem-obj-rule-items, memory.md#mem-obj-rule-counts, memory.md#mem-obj-retrieval-docs, memory.md#mem-obj-analysis-logs, memory.md#mem-obj-critiques, runtime.md#rt-cmp-embedder]
      note: "The recorded inventory resolves form for text, fixed access state and numerical access state separately."
    lineage:
      assessment: partial
      units:
        - scope: "Retained trials/logs, generated retry reflections and maintained rule text"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-analysis-logs, memory.md#mem-obj-reflections, memory.md#mem-obj-rule-items, runtime.md#rt-rte-training-loop, runtime.md#rt-rte-rule-admission]
              note: "Recorded interaction produces retained trajectories/logs and feeds reflection/rule extraction; this lineage does not by itself establish trace learning for raw logs."
          records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-analysis-logs, memory.md#mem-obj-reflections, memory.md#mem-obj-rule-items, runtime.md#rt-rte-rule-admission]
          note: "Known derivation paths incorporate actor and environment material, not independent endorsement of each sentence."
        - scope: "Counter, resume and retrieval-access derivation"
          assessment: partial
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-rule-counts, memory.md#mem-obj-retrieval-docs, runtime.md#rt-rte-checkpoint-restore]
              note: "Fixed code maintains counters/resume state and builds access documents and mappings from histories."
            - value: imported
              basis: wired
              records: [memory.md#mem-obj-retrieval-docs]
              note: "The rebuilt access pool also imports shipped demonstrations; their static source text is excluded as memory, but its incorporation into this mixed access structure is retained."
          records: [memory.md#mem-obj-rule-counts, memory.md#mem-obj-retrieval-docs, runtime.md#rt-cmp-embedder, runtime.md#rt-rte-checkpoint-restore]
          note: "Embedding generation is wired, but dependency-managed embedding provenance and exact weight identity remain unresolved; fixed-code access construction cannot settle that provenance."
        - scope: "Checkpoint replacement content"
          assessment: partial
          findings:
            - value: imported
              basis: wired
              records: [runtime.md#rt-rte-checkpoint-restore, memory.md#mem-obj-rule-items]
              note: "Drivers import saved fields, including cached rules, without rederiving them."
          records: [runtime.md#rt-rte-checkpoint-restore, memory.md#mem-obj-rule-items]
          note: "Actual file provenance and whether replacement content was edited or generated are unknown; imported admission does not resolve upstream authorship."
        - scope: "Auxiliary critique derivation"
          assessment: known
          findings:
            - value: trace-extracted
              basis: afforded
              records: [memory.md#mem-obj-critiques, memory.md#mem-rte-auxiliary-critique]
              note: "Compatible custom invocation can derive critiques from trial pairs or success/failure groups."
          records: [memory.md#mem-obj-critiques, memory.md#mem-rte-auxiliary-critique, epistemic.md#epi-rte-critique-cleanup]
          note: "Cleanup modifies proposed text; no output instance or shipped later consumer is established."
      records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-reflections, memory.md#mem-obj-rule-items, memory.md#mem-obj-rule-counts, memory.md#mem-obj-analysis-logs, memory.md#mem-obj-retrieval-docs, memory.md#mem-obj-critiques, runtime.md#rt-cmp-embedder, runtime.md#rt-rte-checkpoint-restore]
      note: "Positive derivation and import paths coexist with unresolved embedding and replacement-content provenance; no authored lineage is inferred from generic caller supply."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Retained trials and current rule text consumed by the extraction critic"
          assessment: known
          findings:
            - value: learning
              basis: wired
              records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-rule-items, runtime.md#rt-rte-rule-admission]
              note: "Experience and existing guidance feed updates to durable behavior-shaping rules, not model weights."
          records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-rule-items, runtime.md#rt-rte-rule-admission]
          note: "Authority at the update consumer is separate from the output's acting authority and from demonstrated improved capacity."
        - scope: "Retained reflection and rules supplied to retry/evaluation acting"
          assessment: known
          findings:
            - value: instruction
              basis: wired
              records: [memory.md#mem-obj-reflections, runtime.md#rt-rte-training-loop, runtime.md#rt-bap-rules-acting]
              note: "Formatted retry plans and retained benchmark rules supply directions in later acting prompts; compliance is not enforced."
            - value: knowledge
              basis: wired
              records: [runtime.md#rt-bap-rules-acting, memory.md#mem-obj-rule-items]
              note: "Benchmark templates also deliver rule text as interpretive references/advice; this does not license its truth."
          records: [memory.md#mem-obj-reflections, memory.md#mem-obj-rule-items, runtime.md#rt-rte-training-loop, runtime.md#rt-bap-rules-acting]
          note: "Instruction and advisory consumption coexist across the recorded templates; FEVER's MANDATORY text remains model-interpreted, not an action veto."
        - scope: "Retained demonstrations at retrieval selection and subsequent acting"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [memory.md#mem-obj-retrieval-docs, runtime.md#rt-rte-evaluation-context]
              note: "Retained document content and its embeddings influence similarity priority; trajectory length influences which task-associated example is delivered."
            - value: knowledge
              basis: wired
              records: [runtime.md#rt-bap-fewshots-acting, memory.md#mem-obj-trial-history]
              note: "Selected experience reaches the actor as demonstrations/context, not enforced action commands."
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-retrieval-docs]
              note: "Selected document task metadata locates the task-associated history whose shortest trajectory is delivered."
          records: [memory.md#mem-obj-retrieval-docs, runtime.md#rt-rte-evaluation-context, runtime.md#rt-bap-fewshots-acting, memory.md#mem-obj-trial-history]
          note: "Selected key and displayed trajectory can differ; ranking does not establish relevance or truth."
        - scope: "Rule counters at the updater"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [memory.md#mem-obj-rule-counts, epistemic.md#epi-rte-counter-disposition]
              note: "Descending counter order determines rule priority/order."
            - value: validation
              basis: wired
              records: [memory.md#mem-obj-rule-counts, epistemic.md#epi-rte-counter-disposition]
              note: "Positive count is a retained criterion for current pool eligibility, not semantic correctness."
            - value: enforcement
              basis: wired
              records: [memory.md#mem-obj-rule-counts, epistemic.md#epi-rte-counter-disposition]
              note: "The updater actually excludes nonpositive entries from the pool."
          records: [memory.md#mem-obj-rule-counts, epistemic.md#epi-rte-counter-disposition]
          note: "The same criterion supplies validation and an enforced membership veto; numeric counters are not delivered to the actor."
        - scope: "Resume state and persisted logs at restoration/extraction/reporting consumers"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [runtime.md#rt-rte-checkpoint-restore, memory.md#mem-obj-analysis-logs, runtime.md#rt-rte-rule-admission]
              note: "Saved indices and groups select continuation positions and extraction inputs."
            - value: knowledge
              basis: wired
              records: [memory.md#mem-rte-log-inspection, epistemic.md#epi-rte-log-summary]
              note: "Persisted trial text supplies informational reports to an operator, not an automatic insight rejection gate."
          records: [runtime.md#rt-rte-checkpoint-restore, memory.md#mem-obj-analysis-logs, memory.md#mem-rte-log-inspection, epistemic.md#epi-rte-log-summary]
          note: "A report's textual predicates do not independently authenticate benchmark success."
        - scope: "Auxiliary critique payloads and archived reflections without established direct consumers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-critiques, memory.md#mem-rte-auxiliary-critique, memory.md#mem-obj-reflections]
          note: "No shipped later decision reader is established for auxiliary dictionaries or past_reflections; storage and display alone cannot assign force, and unsupported reflection retrieval is not silently counted."
      records: [runtime.md#rt-rte-training-loop, runtime.md#rt-rte-rule-admission, runtime.md#rt-rte-evaluation-context, runtime.md#rt-rte-checkpoint-restore, runtime.md#rt-bap-rules-acting, runtime.md#rt-bap-fewshots-acting, memory.md#mem-obj-rule-counts, memory.md#mem-rte-log-inspection, memory.md#mem-rte-auxiliary-critique, memory.md#mem-obj-reflections]
      note: "Inspected consumers establish multiple local forces; unresolved archive/auxiliary consumers prevent complete authority coverage. Static parser policy is excluded as a memory object."
    write_agency:
      assessment: partial
      units:
        - scope: "Ordinary non-testing trial admission, reflection retention, rule updates, cache copies and snapshots"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-reflections, memory.md#mem-obj-rule-items, runtime.md#rt-rte-rule-admission, runtime.md#rt-rte-checkpoint-restore]
              note: "Software/model admission lacks per-content human approval; startup and overwrite consent do not change this classification."
          records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-reflections, memory.md#mem-obj-rule-items, runtime.md#rt-rte-rule-admission, runtime.md#rt-rte-checkpoint-restore]
          note: "Computational outcome classification and syntax/counter gates govern ordinary writes."
        - scope: "Retrieval-access reconstruction"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-obj-retrieval-docs, runtime.md#rt-rte-evaluation-context]
              note: "Code rebuilds documents, vectors and mappings during prompt refresh."
          records: [memory.md#mem-obj-retrieval-docs, runtime.md#rt-rte-evaluation-context]
          note: "No per-document approval is recorded."
        - scope: "Checkpoint restoration"
          assessment: partial
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-checkpoint-restore]
              note: "Software sets permitted attributes from the selected saved dictionary without per-item review."
          records: [runtime.md#rt-rte-checkpoint-restore, memory.md#mem-obj-rule-items]
          note: "Upstream supplying/editing/approving replacement content is unresolved: a generic caller-selected file does not establish manual admission."
        - scope: "Testing response supply and auxiliary caller content control"
          assessment: partial
          findings:
            - value: automatic
              basis: afforded
              records: [memory.md#mem-rte-auxiliary-critique]
              note: "With compatible templates, helper code admits normalized nonempty critique lines."
          records: [memory.md#mem-rte-auxiliary-critique, memory.md#mem-obj-reflections, runtime.md#rt-rte-training-loop]
          note: "Testing input changes content supply to the caller; exact principal and explicit human decision on retained content are not established for every alternate, so manual is not asserted."
      records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-reflections, memory.md#mem-obj-rule-items, memory.md#mem-obj-retrieval-docs, memory.md#mem-rte-auxiliary-critique, runtime.md#rt-rte-checkpoint-restore, runtime.md#rt-rte-rule-admission]
      note: "Automatic admission is supported locally; replacement provenance and alternate caller control prevent a complete agency inventory."
    curation_operations:
      assessment: partial
      units:
        - scope: "Existing rule text and retention counters under operation-based maintenance"
          assessment: partial
          findings:
            - value: evolve
              basis: wired
              records: [memory.md#mem-obj-rule-items, epistemic.md#epi-rte-counter-disposition]
              note: "EDIT replaces an existing rule's text."
            - value: decay
              basis: wired
              records: [memory.md#mem-obj-rule-counts, epistemic.md#epi-rte-counter-disposition]
              note: "REMOVE downweights the retained rule by decrementing its count."
            - value: invalidate
              basis: wired
              records: [memory.md#mem-obj-rule-counts, memory.md#mem-obj-rule-items, epistemic.md#epi-rte-counter-disposition]
              note: "Nonpositive counts withdraw current pool reliance while old snapshots/cache copies can retain history."
            - value: promote
              basis: wired
              records: [memory.md#mem-obj-rule-counts, epistemic.md#epi-rte-counter-disposition]
              note: "AGREE/EDIT increase counts and surviving rules sort by count, raising retention priority/salience rather than certifying correctness."
            - value: synthesize
              basis: claimed
              records: [epistemic.md#epi-clm-general-insights, epistemic.md#epi-rte-insight-proposal]
              note: "Prompts request general claims about avoiding similar future failures, beyond finite trial inputs; no generated new claim is established."
          records: [memory.md#mem-obj-rule-items, memory.md#mem-obj-rule-counts, epistemic.md#epi-rte-counter-disposition, epistemic.md#epi-rte-insight-proposal, epistemic.md#epi-clm-general-insights]
          note: "Implemented text replacement and counter changes are known; actual semantic transformation of generated rules is indeterminate, preventing a wired synthesis or exhaustive semantic-operation classification."
        - scope: "Trial-to-reflection transformation and auxiliary critique normalization"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-reflections, memory.md#mem-rte-auxiliary-critique, epistemic.md#epi-rte-critique-cleanup]
          note: "Generated reflection meaning is uninspected; stripping parentheses from auxiliary text may reshape or broaden a claim. Neither mechanism alone establishes consolidation or synthesis of actual retained claims."
      records: [memory.md#mem-obj-rule-items, memory.md#mem-obj-rule-counts, memory.md#mem-obj-reflections, memory.md#mem-rte-auxiliary-critique, epistemic.md#epi-rte-counter-disposition, epistemic.md#epi-rte-insight-proposal, epistemic.md#epi-rte-critique-cleanup, epistemic.md#epi-clm-general-insights]
      note: "Counter maintenance and rule revision support positives; semantic outputs remain unresolved. Index rebuild, raw trace acquisition, duplicate-proposal filtering and transient scratchpad trimming are not inferred to be additional retained-memory curation."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Requested checkpoint/log loading by drivers or reporting callers"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-checkpoint-restore, memory.md#mem-rte-log-inspection]
              note: "Drivers/callers request saved state or a selected log and loaders return that material; the return is not another push."
          records: [runtime.md#rt-rte-checkpoint-restore, memory.md#mem-rte-log-inspection]
          note: "Explicit loading requests precede separate downstream automatic context selection."
        - scope: "Retry reflections, extraction evidence/existing rules, evaluation rules and demonstrations"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-training-loop, runtime.md#rt-rte-rule-admission, runtime.md#rt-rte-evaluation-context, runtime.md#rt-bap-rules-acting, runtime.md#rt-bap-fewshots-acting]
              note: "Code assembles retained material into later model inputs without an actor/critic-issued request for that material."
          records: [runtime.md#rt-rte-training-loop, runtime.md#rt-rte-rule-admission, runtime.md#rt-rte-evaluation-context, runtime.md#rt-bap-rules-acting, runtime.md#rt-bap-fewshots-acting]
          note: "Starting extraction/evaluation supplies workflow inputs, not a model memory query; selection and model delivery are separate from requested file returns."
        - scope: "Auxiliary critique and direct reflection-archive consumption alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-auxiliary-critique, memory.md#mem-obj-reflections, runtime.md#rt-rte-evaluation-context]
          note: "No shipped auxiliary decision reader or direct past_reflections reader is established; reflection_similarity lacks final dispatch, so its potential direction is not classified."
      records: [runtime.md#rt-rte-checkpoint-restore, memory.md#mem-rte-log-inspection, runtime.md#rt-rte-training-loop, runtime.md#rt-rte-rule-admission, runtime.md#rt-rte-evaluation-context, memory.md#mem-rte-auxiliary-critique, memory.md#mem-obj-reflections]
      note: "Both requested loading and automatic model supply are supported; unresolved included alternatives prevent complete read-back coverage."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Retry reflection and full current-rule supply"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-training-loop, memory.md#mem-obj-reflections, runtime.md#rt-bap-rules-acting, memory.md#mem-obj-rule-items]
              note: "Retry/model-prompt construction supplies available formatted reflections; evaluation supplies the whole formatted rule pool unless no_rules. There is no query targeting within those texts."
          records: [runtime.md#rt-rte-training-loop, memory.md#mem-obj-reflections, runtime.md#rt-bap-rules-acting, memory.md#mem-obj-rule-items]
          note: "Failure/retry and evaluation prompt construction are triggers; available reflection/current-rule state is the selector input."
        - scope: "Extraction task lookup and evaluation fold-cache rule selection"
          assessment: known
          findings:
            - value: identifier
              basis: wired
              records: [runtime.md#rt-rte-rule-admission, memory.md#mem-obj-rule-items]
              note: "Compare extraction resolves training IDs through idx2task to select retained trial pairs; load_cache_fold matches a cache key to select the rule list delivered downstream."
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-rule-admission]
              note: "Success grouping uses eligible enumeration positions and first available success, then supplies groups and existing rules; eligibility is not embedding or judgment selection."
          records: [runtime.md#rt-rte-rule-admission, memory.md#mem-obj-rule-items]
          note: "Triggers are create_rules or fold rule load. Identifier matching is an actual retained-part lookup, not merely an identifier on a requested file; success-group task-identity holdout remains conditional."
        - scope: "Automatic evaluation demonstration refresh"
          assessment: known
          findings:
            - value: inferred-embedding
              basis: wired
              records: [runtime.md#rt-rte-evaluation-context, memory.md#mem-obj-retrieval-docs]
              note: "Prompt refresh uses task/latest thought/action/step text to similarity-select buffered documents; optional task reranking also uses similarity."
            - value: identifier
              basis: wired
              records: [memory.md#mem-obj-retrieval-docs, runtime.md#rt-bap-fewshots-acting]
              note: "Matched document task metadata selects the task-associated history from which the delivered shortest trajectory is chosen."
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-evaluation-context, memory.md#mem-obj-retrieval-docs]
              note: "Environment, trajectory eligibility/length, token/count budgets, current-task and duplicate-task exclusions further filter delivery; random reranking acts on the already retrieved subset."
          records: [runtime.md#rt-rte-evaluation-context, memory.md#mem-obj-retrieval-docs, runtime.md#rt-bap-fewshots-acting]
          note: "Selected retained parts are successful-history demonstrations via document keys, mixed with shipped examples; unsupported reflection_similarity is excluded from supported selectors, not from the uncertainty inventory."
        - scope: "Auxiliary critique and direct reflection-archive read-back"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-auxiliary-critique, memory.md#mem-obj-reflections, runtime.md#rt-rte-evaluation-context]
          note: "An actual later push and selector are unestablished, preventing classification rather than implying pull-only inapplicability."
      records: [runtime.md#rt-rte-training-loop, runtime.md#rt-rte-rule-admission, runtime.md#rt-rte-evaluation-context, memory.md#mem-obj-rule-items, memory.md#mem-obj-retrieval-docs, memory.md#mem-obj-reflections, memory.md#mem-rte-auxiliary-critique]
      note: "Signals characterize automatic selection within push chains; requested file/log names are not counted as identifier push signals. Unresolved consumers keep this axis partial."
    trace_learning:
      assessment: partial
      units:
        - scope: "Ordinary failed-trial reflection write followed by retry acting"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-obj-reflections, runtime.md#rt-rte-training-loop]
              note: "Failed experience automatically produces retained guidance consumed by a later retry invocation, including within one task."
          records: [memory.md#mem-obj-reflections, runtime.md#rt-rte-training-loop]
          note: "The retained list/trajectory/checkpoint chain qualifies without parameter updates or observed improvement."
        - scope: "Ordinary trial-conditioned rule maintenance followed by critique/evaluation"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-rule-items, runtime.md#rt-rte-rule-admission, runtime.md#rt-bap-rules-acting]
              note: "Automatic trace-fed updates produce durable rules used in later critique and acting prompts."
          records: [memory.md#mem-obj-trial-history, memory.md#mem-obj-rule-items, runtime.md#rt-rte-rule-admission, runtime.md#rt-bap-rules-acting]
          note: "Wired behavior-shaping artifact production is not successful capacity improvement or epistemic acceptance."
        - scope: "Auxiliary critiques, replacement checkpoint provenance and testing content alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-auxiliary-critique, runtime.md#rt-rte-checkpoint-restore, memory.md#mem-obj-reflections]
          note: "Auxiliary durable later behavior-shaping use is unestablished; external replacement generation and testing supply control are unknown. Raw retention or restoration alone does not settle a qualifying automatic trace-fed write."
      records: [memory.md#mem-obj-reflections, memory.md#mem-obj-trial-history, memory.md#mem-obj-rule-items, runtime.md#rt-rte-training-loop, runtime.md#rt-rte-rule-admission, runtime.md#rt-bap-rules-acting, memory.md#mem-rte-auxiliary-critique, runtime.md#rt-rte-checkpoint-restore]
      note: "Two positive wired routes coexist with unresolved alternatives. No bounded absence record supports a local or system-wide no; raw trajectory retrieval alone is not counted as a derived learning write."
    trace_source:
      assessment: partial
      units:
        - scope: "Failed-trial input to retained retry reflection"
          assessment: known
          findings:
            - value: trajectories
              basis: wired
              records: [runtime.md#rt-rte-training-loop, memory.md#mem-obj-reflections]
              note: "Linked task thoughts/actions/observations and failure experience feed retry guidance."
            - value: tool-traces
              basis: wired
              records: [runtime.md#rt-rte-training-loop, memory.md#mem-obj-trial-history]
              note: "Recorded benchmark action requests and returned observations/outcome feedback are consumed within the failed trial."
          records: [runtime.md#rt-rte-training-loop, memory.md#mem-obj-reflections, memory.md#mem-obj-trial-history]
          note: "Source is multi-step benchmark experience, not generic conversational session logs or discrete hook events; static method instructions are not trace sources."
        - scope: "Successful/failed pairs and success groups feeding durable rule maintenance"
          assessment: known
          findings:
            - value: trajectories
              basis: wired
              records: [memory.md#mem-obj-trial-history, runtime.md#rt-rte-rule-admission]
              note: "Extraction consumes linked trial experience with outcome classifications."
            - value: tool-traces
              basis: wired
              records: [memory.md#mem-obj-trial-history, runtime.md#rt-rte-rule-admission]
              note: "Selected trial text contains action/observation execution records used by the critic; this is not an additional event-stream source merely because it is logged."
          records: [memory.md#mem-obj-trial-history, runtime.md#rt-rte-rule-admission]
          note: "Task text and existing rules also enter prompts, but neither adds a separate trace-source class. Effective heldout exclusion is conditional in success grouping."
        - scope: "Unresolved auxiliary later-use and replacement/testing learning alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-auxiliary-critique, runtime.md#rt-rte-checkpoint-restore, memory.md#mem-obj-reflections]
          note: "Trial-fed auxiliary generation is afforded, but its qualifying later behavior-shaping consumer is missing; replacement provenance and testing write control remain unknown. These routes cannot be marked inapplicable based on the two known positives."
      records: [runtime.md#rt-rte-training-loop, runtime.md#rt-rte-rule-admission, memory.md#mem-obj-trial-history, memory.md#mem-obj-reflections, memory.md#mem-rte-auxiliary-critique, runtime.md#rt-rte-checkpoint-restore]
      note: "Both known qualifying writes consume trajectories including execution feedback. Missing qualifying-chain/provenance facts in included alternatives prevent complete source coverage."
---

# ExpeL memory profile

## Comparison rationale

This profile classifies the accepted records, not a target execution. All positive bases remain local: the shipped reflection and rule routes are wired, while auxiliary helper invocation is only afforded. No supplied execution or comparison upgrades these findings to observed operation or causal benefit ([RT-RTE-training-loop](runtime.md#rt-rte-training-loop), [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), [MEM-RTE-auxiliary-critique](memory.md#mem-rte-auxiliary-critique)).

Storage and form have complete classification within the recorded object inventory. Other axes retain the specific unresolved facts: auxiliary/archive consumers, caller content control, checkpoint provenance, embedding provenance and generated semantic transformations. An unresolved consumer does not make an otherwise described object's substrate or form unknowable. External model weights are components, not the accumulated memory boundary; their opacity is not used to invent model-weight memory or to erase the recorded dense retrieval-access part ([MEM-OBJ-retrieval-docs](memory.md#mem-obj-retrieval-docs), [RT-CMP-embedder](runtime.md#rt-cmp-embedder)).

The reconciliation supersedes the epistemic rule-text, counter and auxiliary-dictionary object declarations with [MEM-OBJ-rule-items](memory.md#mem-obj-rule-items), [MEM-OBJ-rule-counts](memory.md#mem-obj-rule-counts) and [MEM-OBJ-critiques](memory.md#mem-obj-critiques). Those canonical objects are cited here. Epistemic proposal, checking, disposition and cleanup parts remain distinct accepted routes, so their local semantic limits and counter effects remain usable. The reconciliation's remaining discrepancy concerns how epistemic describes the current runtime's fold qualification, not the selection mechanism. This profile relies on the conditional mechanism now explicit in [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), not the characterization of an unconditional peer claim.

Learning authority belongs to retained trials/current rules at the rule-update consumer; instruction and advice belong to derived guidance at later acting consumers. Counter eligibility supplies validation and an enforced membership decision independently of model-interpreted rule content. Positive trace learning names the automatic retained-guidance chains, not successful improvement, accepted knowledge or fine-tuning ([EPI-RTE-counter-disposition](epistemic.md#epi-rte-counter-disposition), [RT-BAP-rules-acting](runtime.md#rt-bap-rules-acting), [MEM-OBJ-reflections](memory.md#mem-obj-reflections)).

Curation distinguishes fixed-code revision, priority changes and withdrawal from requested semantic generalization. A prompt asking for generally applicable future insights supplies only a claimed synthesis finding. Actual generated rule semantics remain indeterminate; the profile does not upgrade that request to wired production of novel claims, or classify every model extraction as consolidation. Substring duplicate-proposal filtering is not evidence of merging/removing duplicate retained entries ([EPI-RTE-insight-proposal](epistemic.md#epi-rte-insight-proposal), [EPI-CLM-general-insights](epistemic.md#epi-clm-general-insights), [EPI-RTE-syntax-check](epistemic.md#epi-rte-syntax-check)).

Read-back separates requested saved-state/log loading from subsequent automatic model context supply. Embedding matching, task-identity lookup and coarse eligibility operate at different steps; the matched document can point to a different shortest trajectory from the one that supplied its key. Fold extraction and retrieval have different pools, so the profile makes no complete held-out isolation claim ([RT-RTE-checkpoint-restore](runtime.md#rt-rte-checkpoint-restore), [MEM-RTE-log-inspection](memory.md#mem-rte-log-inspection), [MEM-OBJ-retrieval-docs](memory.md#mem-obj-retrieval-docs), [RT-RTE-evaluation-context](runtime.md#rt-rte-evaluation-context)).

Source-read log: none. Classification used only the supplied accepted members and their records; no source ambiguity required an additional frozen-source read.
