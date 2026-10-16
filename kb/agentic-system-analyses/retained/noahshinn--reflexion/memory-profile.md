---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: Reflexion memory comparison for task-local retained experience, checkpoints and later consumers
  across four shipped experiment families.
run-id: AAS-2026-10-14-reflexion-19159b69b712-01
source-identity: https://github.com/noahshinn/reflexion
reviewed-boundary: 218cf0ef1df84b05ce379dd4a8e47f17766733a0
memory-comparison:
  version: 2
  scope: 'Included: ALFWorld/WebShop retained task plans, experience logs and configuration controls;
    HotPotQA diagnoses, prior-attempt excerpts, logs and whole-agent checkpoints; programming retained
    candidates, feedback, hints, UCS parent state and JSONL products, resume and offline execution consumers;
    unresolved search/grading internals and possible provider-side accumulated state. Excluded: shipped
    static prompts/examples, ordinary current-attempt windows and fixed pretrained weights as such; live
    external source contents and unrelated repository housekeeping.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: ALFWorld and WebShop plan lists, configuration flags and trial/world logs
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id001
          - memory.md#mem-obj-alfworld-memory
          - memory.md#mem-obj-alfworld-logs
          - runtime.md#rt-rte-alfworld-trial
          - memory.md#mem-obj-webshop-memory
          - memory.md#mem-obj-webshop-logs
          - runtime.md#rt-rte-webshop-trial
          note: Lists and configuration fields are retained in the driver process.
        - value: files
          basis: wired
          records: *id001
          note: Per-trial JSON configurations and text logs retain task state across trials and explicit
            resume.
        records: *id001
        note: The cited records cover this named part and its consumer.
      - scope: HotPotQA diagnosis and prior-attempt text in agent state; serialization and independently
          constructed logs
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id002
          - memory.md#mem-obj-hotpotqa-reflections
          - memory.md#mem-obj-last-attempt
          - runtime.md#rt-rte-hotpotqa-attempt
          - memory.md#mem-obj-hotpotqa-checkpoints
          note: Agent lists and strings retain prior material across calls.
        - value: files
          basis: wired
          records: *id002
          note: The writer saves agent joblib files and trial logs; binary encoding does not alter the
            file substrate.
        records: *id002
        note: The cited records cover this named part and its consumer.
      - scope: Programming candidates, hints, feedback, UCS nodes and result rows
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id003
          - memory.md#mem-obj-reflections
          - memory.md#mem-obj-test-feedback
          - runtime.md#rt-obj-cur-func-impl
          - runtime.md#rt-rte-program-attempt
          - memory.md#mem-obj-state
          - runtime.md#rt-rte-program-variants
          - memory.md#mem-obj-program-results
          - memory.md#mem-rte-result-validation
          note: Task-local strings/lists and visible UCS State objects retain candidate experience.
        - value: files
          basis: wired
          records: *id003
          note: JSONL retains result rows and their archived candidate/hint/feedback parts.
        records: *id003
        note: The cited records cover this named part and its consumer.
      - scope: Additional retention inside unavailable UCS search
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-state
        - runtime.md#rt-rte-program-variants
        note: Parent State objects are inspected; search-node retention, eviction and additional substrate
          are not. This prevents complete UCS storage classification.
      - scope: Possible provider-side state accumulated through use, separate from shipped pretrained
          model weights
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-cmp-gpt4
        - runtime.md#rt-cmp-gpt35
        - runtime.md#rt-cmp-text-davinci
        - runtime.md#rt-cmp-star-chat
        - runtime.md#rt-cmp-code-llama
        note: Generation adapters do not expose whether providers retain additional use-dependent state
          or its substrate. Pretrained weights alone do not establish accumulated memory.
      records:
      - memory.md#mem-obj-alfworld-memory
      - memory.md#mem-obj-alfworld-logs
      - runtime.md#rt-rte-alfworld-trial
      - memory.md#mem-obj-webshop-memory
      - memory.md#mem-obj-webshop-logs
      - runtime.md#rt-rte-webshop-trial
      - memory.md#mem-obj-hotpotqa-reflections
      - memory.md#mem-obj-last-attempt
      - runtime.md#rt-rte-hotpotqa-attempt
      - memory.md#mem-obj-hotpotqa-checkpoints
      - memory.md#mem-obj-reflections
      - memory.md#mem-obj-test-feedback
      - runtime.md#rt-obj-cur-func-impl
      - runtime.md#rt-rte-program-attempt
      - memory.md#mem-obj-state
      - runtime.md#rt-rte-program-variants
      - memory.md#mem-obj-program-results
      - memory.md#mem-rte-result-validation
      - runtime.md#rt-cmp-gpt4
      - runtime.md#rt-cmp-gpt35
      - runtime.md#rt-cmp-text-davinci
      - runtime.md#rt-cmp-star-chat
      - runtime.md#rt-cmp-code-llama
      note: Files and in-memory objects cover the inspected parent memory inventory. Missing UCS internals
        and opaque provider-side accumulated state prevent a complete inventory; repository packaging
        and pretrained weights are not counted as memory substrates.
    representational_form:
      assessment: partial
      units:
      - scope: Plans, diagnoses, feedback, prior-attempt excerpts and scenario text at model consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id004
          - memory.md#mem-obj-alfworld-memory
          - memory.md#mem-obj-alfworld-logs
          - runtime.md#rt-rte-alfworld-trial
          - memory.md#mem-obj-webshop-memory
          - memory.md#mem-obj-webshop-logs
          - runtime.md#rt-rte-webshop-trial
          - memory.md#mem-obj-hotpotqa-reflections
          - memory.md#mem-obj-last-attempt
          - runtime.md#rt-rte-hotpotqa-attempt
          - memory.md#mem-obj-reflections
          - memory.md#mem-obj-test-feedback
          - runtime.md#rt-obj-cur-func-impl
          - runtime.md#rt-rte-program-attempt
          note: Models interpret retained plans, explanations, feedback and trace excerpts as advice or
            evidence; code rendered to a generator also has this interpretive path.
        records: *id004
        note: The cited records cover this named part and its consumer.
      - scope: Configuration status/index fields, log delimiters, programming row metadata and UCS outcome
          tuples at fixed-rule consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id005
          - memory.md#mem-obj-alfworld-memory
          - memory.md#mem-obj-alfworld-logs
          - runtime.md#rt-rte-alfworld-trial
          - memory.md#mem-obj-webshop-memory
          - memory.md#mem-obj-webshop-logs
          - runtime.md#rt-rte-webshop-trial
          - memory.md#mem-obj-state
          - runtime.md#rt-rte-program-variants
          - memory.md#mem-obj-program-results
          - memory.md#mem-rte-result-validation
          note: Host rules parse delimiters, test bits, success flags and positional completion bookkeeping
            independently of language interpretation.
        records: *id005
        note: The cited records cover this named part and its consumer.
      - scope: Saved candidate source and reference tests at offline execution
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id006
          - memory.md#mem-obj-program-results
          - memory.md#mem-rte-result-validation
          - runtime.md#rt-obj-cur-func-impl
          note: The validator reconstructs executable code/tests from solved result rows; its consumer
            is an interpreter or Rust executor, not a language-model display.
        records: *id006
        note: The cited records cover this named part and its consumer.
      - scope: HotPotQA readable logs and joblib envelope
        assessment: partial
        findings:
        - value: natural-language
          basis: wired
          records: &id007
          - memory.md#mem-obj-hotpotqa-checkpoints
          note: Trial logs render question/attempt text and correct answers.
        - value: symbolic
          basis: wired
          records: *id007
          note: The joblib writer serializes whole agent objects.
        records: *id007
        note: The envelope and separately rendered logs are inspected; full payload and library-object
          internals are not decoded. A readable summary cannot classify every serialized part.
      - scope: Additional UCS search state representation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-state
        - runtime.md#rt-rte-program-variants
        note: The parent node fields are known; unavailable search internals prevent classifying any additional
          retained representation.
      - scope: Possible provider-side state accumulated through use, separate from shipped pretrained
          model weights
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-cmp-gpt4
        - runtime.md#rt-cmp-gpt35
        - runtime.md#rt-cmp-text-davinci
        - runtime.md#rt-cmp-star-chat
        - runtime.md#rt-cmp-code-llama
        note: No operative use-dependent provider payload is inspectable; the parametric form of pretrained
          models cannot classify unknown accumulated state.
      records:
      - memory.md#mem-obj-alfworld-memory
      - memory.md#mem-obj-alfworld-logs
      - runtime.md#rt-rte-alfworld-trial
      - memory.md#mem-obj-webshop-memory
      - memory.md#mem-obj-webshop-logs
      - runtime.md#rt-rte-webshop-trial
      - memory.md#mem-obj-hotpotqa-reflections
      - memory.md#mem-obj-last-attempt
      - runtime.md#rt-rte-hotpotqa-attempt
      - memory.md#mem-obj-reflections
      - memory.md#mem-obj-test-feedback
      - runtime.md#rt-obj-cur-func-impl
      - runtime.md#rt-rte-program-attempt
      - memory.md#mem-obj-state
      - runtime.md#rt-rte-program-variants
      - memory.md#mem-obj-program-results
      - memory.md#mem-rte-result-validation
      - memory.md#mem-obj-hotpotqa-checkpoints
      - runtime.md#rt-cmp-gpt4
      - runtime.md#rt-cmp-gpt35
      - runtime.md#rt-cmp-text-davinci
      - runtime.md#rt-cmp-star-chat
      - runtime.md#rt-cmp-code-llama
      note: Natural-language and symbolic paths are separately supported. Checkpoint payload composition,
        UCS internals and provider memory remain unresolved; binary serialization is not evidence of parametric
        memory.
    lineage:
      assessment: partial
      units:
      - scope: ALFWorld/WebShop newly generated plans, HotPotQA diagnoses/excerpts and feedback-fed programming
          hints
        assessment: partial
        findings:
        - value: trace-extracted
          basis: wired
          records: &id008
          - memory.md#mem-obj-alfworld-memory
          - memory.md#mem-obj-alfworld-logs
          - runtime.md#rt-rte-alfworld-trial
          - memory.md#mem-obj-webshop-memory
          - memory.md#mem-obj-webshop-logs
          - runtime.md#rt-rte-webshop-trial
          - memory.md#mem-obj-hotpotqa-reflections
          - memory.md#mem-obj-last-attempt
          - runtime.md#rt-rte-hotpotqa-attempt
          - memory.md#mem-obj-reflections
          - memory.md#mem-obj-test-feedback
          - runtime.md#rt-obj-cur-func-impl
          - runtime.md#rt-rte-program-attempt
          note: Recorded failed attempts or execution feedback feed automatic retained guidance and prior-attempt
            excerpts.
        records: *id008
        note: Trace derivation is wired, but static examples/context also enter producers and their initial
          provenance is unresolved; output instances were not inspected.
      - scope: Immediate-reflexion candidate-fed hints without executed test feedback
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id009
          - runtime.md#rt-rte-program-variants
          - memory.md#mem-obj-reflections
          note: The model composes an explanation from the current candidate with Test cases omitted;
            no executed-test trace provenance is supplied for this branch.
        records: *id009
        note: The cited records cover this named part and its consumer.
      - scope: Configuration resume import and persisted result-file reads
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records: &id010
          - memory.md#mem-obj-alfworld-memory
          - memory.md#mem-obj-alfworld-logs
          - runtime.md#rt-rte-alfworld-trial
          - memory.md#mem-obj-webshop-memory
          - memory.md#mem-obj-webshop-logs
          - runtime.md#rt-rte-webshop-trial
          - memory.md#mem-obj-program-results
          - memory.md#mem-rte-result-validation
          note: Explicit configuration loads and standalone saved-result reads acquire retained content
            from selected files.
        records: *id010
        note: The import path is wired, but caller-selected initial content and historical file authorship/authenticity
          are unresolved. Import does not authenticate earlier derivation.
      - scope: Programming result row packaging and HotPotQA agent serialization
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records: &id011
          - memory.md#mem-obj-program-results
          - memory.md#mem-rte-result-validation
          - memory.md#mem-obj-hotpotqa-checkpoints
          note: Host code packages task state into JSONL or whole-object serialized checkpoints without
            establishing semantic acceptance.
        records: *id011
        note: Packaging paths are known; initial dataset provenance, exact historical payload composition
          and serialized internals remain unresolved.
      - scope: Additional UCS search-derived retained state
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-state
        - runtime.md#rt-rte-program-variants
        note: Visible nodes contain generated code/feedback/hints; missing search implementation prevents
          complete node derivation and selected-node persistence classification.
      - scope: Possible provider-side state accumulated through use, separate from shipped pretrained
          model weights
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-cmp-gpt4
        - runtime.md#rt-cmp-gpt35
        - runtime.md#rt-cmp-text-davinci
        - runtime.md#rt-cmp-star-chat
        - runtime.md#rt-cmp-code-llama
        note: Initial and use-dependent derivation of possible provider-retained state is not exposed
          by generation clients.
      records:
      - memory.md#mem-obj-alfworld-memory
      - memory.md#mem-obj-alfworld-logs
      - runtime.md#rt-rte-alfworld-trial
      - memory.md#mem-obj-webshop-memory
      - memory.md#mem-obj-webshop-logs
      - runtime.md#rt-rte-webshop-trial
      - memory.md#mem-obj-hotpotqa-reflections
      - memory.md#mem-obj-last-attempt
      - runtime.md#rt-rte-hotpotqa-attempt
      - memory.md#mem-obj-reflections
      - memory.md#mem-obj-test-feedback
      - runtime.md#rt-obj-cur-func-impl
      - runtime.md#rt-rte-program-attempt
      - runtime.md#rt-rte-program-variants
      - memory.md#mem-obj-program-results
      - memory.md#mem-rte-result-validation
      - memory.md#mem-obj-hotpotqa-checkpoints
      - memory.md#mem-obj-state
      - runtime.md#rt-cmp-gpt4
      - runtime.md#rt-cmp-gpt35
      - runtime.md#rt-cmp-text-davinci
      - runtime.md#rt-cmp-star-chat
      - runtime.md#rt-cmp-code-llama
      note: Known trace extraction, model authorship, file import and host packaging coexist. They do
        not resolve initial dataset/example provenance, resumed historical content, opaque checkpoint
        internals or provider/search alternatives.
    behavioral_authority:
      assessment: partial
      units:
      - scope: ALFWorld action/reflection models, WebShop reflection model and HotPotQA/programming successor
          generators consuming advice
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id012
          - memory.md#mem-obj-alfworld-memory
          - memory.md#mem-obj-alfworld-logs
          - runtime.md#rt-rte-alfworld-trial
          - memory.md#mem-obj-webshop-memory
          - memory.md#mem-obj-webshop-logs
          - runtime.md#rt-rte-webshop-trial
          - memory.md#mem-obj-hotpotqa-reflections
          - memory.md#mem-obj-last-attempt
          - runtime.md#rt-rte-hotpotqa-attempt
          - memory.md#mem-obj-reflections
          - memory.md#mem-obj-test-feedback
          - runtime.md#rt-obj-cur-func-impl
          - runtime.md#rt-rte-program-attempt
          note: Retained plans/hints and prior traces supply interpreted advice, context or evidence.
            They are not standing host directions or executable permission policies.
        records: *id012
        note: The cited records cover this named part and its consumer.
      - scope: Failure logs, prior scratchpads, candidate feedback and past plans at automatic guidance
          producers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id013
          - memory.md#mem-obj-alfworld-memory
          - memory.md#mem-obj-alfworld-logs
          - runtime.md#rt-rte-alfworld-trial
          - memory.md#mem-obj-webshop-memory
          - memory.md#mem-obj-webshop-logs
          - runtime.md#rt-rte-webshop-trial
          - memory.md#mem-obj-hotpotqa-reflections
          - memory.md#mem-obj-last-attempt
          - runtime.md#rt-rte-hotpotqa-attempt
          - memory.md#mem-obj-reflections
          - memory.md#mem-obj-test-feedback
          - runtime.md#rt-obj-cur-func-impl
          - runtime.md#rt-rte-program-attempt
          note: Retained experience feeds a durable behavior-shaping plan, diagnosis or excerpt delivered
            to a later model call. This authority does not establish improved capacity.
        records: *id013
        note: The cited records cover this named part and its consumer.
      - scope: Configuration success/skip flags and positional result-file completion accounting
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id014
          - memory.md#mem-obj-alfworld-memory
          - memory.md#mem-obj-alfworld-logs
          - runtime.md#rt-rte-alfworld-trial
          - memory.md#mem-obj-webshop-memory
          - memory.md#mem-obj-webshop-logs
          - runtime.md#rt-rte-webshop-trial
          - memory.md#mem-obj-program-results
          - memory.md#mem-rte-result-validation
          note: Flags and result-row count select later task attempts or input windows.
        - value: enforcement
          basis: wired
          records: *id014
          note: Success/skip predicates and positional completed-prefix rules actually suppress covered
            future attempts or plan admissions.
        records: *id014
        note: The cited records cover this named part and its consumer.
      - scope: UCS retained outcome tuple/code at visible cost and successor callbacks
        assessment: partial
        findings:
        - value: ranking
          basis: wired
          records: &id015
          - memory.md#mem-obj-state
          - runtime.md#rt-rte-program-variants
          note: Failure counts assign relative candidate costs for the search interface.
        - value: knowledge
          basis: wired
          records: *id015
          note: State-specific code, feedback and hint supply the visible successor-generation context.
        records: *id015
        note: Parent callback effects are wired in the Python-scoped account; missing search scheduling
          prevents complete consumer and horizon classification.
      - scope: Persisted solution and tests at standalone Python/Rust validators
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id016
          - memory.md#mem-obj-program-results
          - memory.md#mem-rte-result-validation
          - runtime.md#rt-obj-cur-func-impl
          note: Saved source supplies executable instructions to the interpreter or Rust execution facility.
        - value: validation
          basis: wired
          records: *id016
          note: Saved reference tests supply criteria for the candidate recheck.
        - value: routing
          basis: wired
          records: *id016
          note: Retained is_solved selects which rows the validator executes.
        records: *id016
        note: The cited records cover this named part and its consumer.
      - scope: HotPotQA serialized library-object parts beyond identified text/state
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-hotpotqa-checkpoints
        note: No saved-agent reload consumer was inspected and full payload composition is unresolved;
          serialization alone supplies no additional downstream authority.
      - scope: Intended offline LeetCode persisted-implementation consumer
        assessment: partial
        findings:
        - value: instruction
          basis: afforded
          records: &id017
          - memory.md#mem-rte-leet-evaluation
          note: Parent scaffold affords executable submission of stored source to a remote grader; argument
            and record-shape defects block wired delivery.
        records: *id017
        note: The scaffold describes a consumer but does not wire an end-to-end submission; grader semantics
          remain unavailable.
      - scope: Possible provider-side state accumulated through use, separate from shipped pretrained
          model weights
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-cmp-gpt4
        - runtime.md#rt-cmp-gpt35
        - runtime.md#rt-cmp-text-davinci
        - runtime.md#rt-cmp-star-chat
        - runtime.md#rt-cmp-code-llama
        note: Possible provider memory consumers and effects are not exposed; known model generation cannot
          assign authority to an unknown retained part.
      records:
      - memory.md#mem-obj-alfworld-memory
      - memory.md#mem-obj-alfworld-logs
      - runtime.md#rt-rte-alfworld-trial
      - memory.md#mem-obj-webshop-memory
      - memory.md#mem-obj-webshop-logs
      - runtime.md#rt-rte-webshop-trial
      - memory.md#mem-obj-hotpotqa-reflections
      - memory.md#mem-obj-last-attempt
      - runtime.md#rt-rte-hotpotqa-attempt
      - memory.md#mem-obj-reflections
      - memory.md#mem-obj-test-feedback
      - runtime.md#rt-obj-cur-func-impl
      - runtime.md#rt-rte-program-attempt
      - memory.md#mem-obj-program-results
      - memory.md#mem-rte-result-validation
      - memory.md#mem-obj-state
      - runtime.md#rt-rte-program-variants
      - memory.md#mem-obj-hotpotqa-checkpoints
      - memory.md#mem-rte-leet-evaluation
      - runtime.md#rt-cmp-gpt4
      - runtime.md#rt-cmp-gpt35
      - runtime.md#rt-cmp-text-davinci
      - runtime.md#rt-cmp-star-chat
      - runtime.md#rt-cmp-code-llama
      note: 'Authority is consumer-relative: advice, update input, fixed host controls, ranking inputs
        and executable products have distinct force. No semantic compliance or accepted explanation is
        inferred. Unavailable search/grading consumers and opaque payloads prevent complete coverage.'
    write_agency:
      assessment: partial
      units:
      - scope: Failure-triggered plan/diagnosis admission and HotPotQA prior-trace replacement
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id018
          - memory.md#mem-obj-alfworld-memory
          - memory.md#mem-obj-alfworld-logs
          - runtime.md#rt-rte-alfworld-trial
          - memory.md#mem-obj-webshop-memory
          - memory.md#mem-obj-webshop-logs
          - runtime.md#rt-rte-webshop-trial
          - memory.md#mem-obj-hotpotqa-reflections
          - memory.md#mem-obj-last-attempt
          - runtime.md#rt-rte-hotpotqa-attempt
          note: Host flags and strategy rules append/replace model outputs or trace excerpts without per-content
            human approval.
        records: *id018
        note: The cited records cover this named part and its consumer.
      - scope: Programming candidate replacement, feedback/hint append, UCS parent-node construction and
          result/checkpoint saving
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id019
          - memory.md#mem-obj-reflections
          - memory.md#mem-obj-test-feedback
          - runtime.md#rt-obj-cur-func-impl
          - runtime.md#rt-rte-program-attempt
          - memory.md#mem-obj-state
          - runtime.md#rt-rte-program-variants
          - memory.md#mem-obj-program-results
          - memory.md#mem-rte-result-validation
          - memory.md#mem-obj-hotpotqa-checkpoints
          note: Software/model admission writes current candidates, retained feedback, explanations and
            packages; operator launch does not make these decisions manual.
        records: *id019
        note: The cited records cover this named part and its consumer.
      - scope: Initial dataset and caller-selected resumed configuration content admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-alfworld-memory
        - memory.md#mem-obj-alfworld-logs
        - runtime.md#rt-rte-alfworld-trial
        - memory.md#mem-obj-webshop-memory
        - memory.md#mem-obj-webshop-logs
        - runtime.md#rt-rte-webshop-trial
        - memory.md#mem-obj-hotpotqa-checkpoints
        note: Generic caller file selection does not establish explicit human approval/editing of retained
          content; initial authorship and admission control remain unresolved. No manual finding is licensed.
      - scope: Additional UCS search retention/admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-state
        - runtime.md#rt-rte-program-variants
        note: The parent creates State values automatically, but missing search implementation prevents
          classifying additional node admission mechanisms.
      - scope: Possible provider-side state accumulated through use, separate from shipped pretrained
          model weights
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-cmp-gpt4
        - runtime.md#rt-cmp-gpt35
        - runtime.md#rt-cmp-text-davinci
        - runtime.md#rt-cmp-star-chat
        - runtime.md#rt-cmp-code-llama
        note: Provider-side use-dependent write and admission control are not visible in generation adapters.
      records:
      - memory.md#mem-obj-alfworld-memory
      - memory.md#mem-obj-alfworld-logs
      - runtime.md#rt-rte-alfworld-trial
      - memory.md#mem-obj-webshop-memory
      - memory.md#mem-obj-webshop-logs
      - runtime.md#rt-rte-webshop-trial
      - memory.md#mem-obj-hotpotqa-reflections
      - memory.md#mem-obj-last-attempt
      - runtime.md#rt-rte-hotpotqa-attempt
      - memory.md#mem-obj-reflections
      - memory.md#mem-obj-test-feedback
      - runtime.md#rt-obj-cur-func-impl
      - runtime.md#rt-rte-program-attempt
      - memory.md#mem-obj-state
      - runtime.md#rt-rte-program-variants
      - memory.md#mem-obj-program-results
      - memory.md#mem-rte-result-validation
      - memory.md#mem-obj-hotpotqa-checkpoints
      - runtime.md#rt-cmp-gpt4
      - runtime.md#rt-cmp-gpt35
      - runtime.md#rt-cmp-text-davinci
      - runtime.md#rt-cmp-star-chat
      - runtime.md#rt-cmp-code-llama
      note: Subsequent host/model admission is automatic. Initial content, resumed-payload control, unavailable
        search admission and provider writes remain unresolved; human-edit renderer labels and workflow
        launch are not manual-content witnesses.
    curation_operations:
      assessment: partial
      units:
      - scope: HotPotQA formatted retained last-attempt excerpt
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id020
          - memory.md#mem-obj-last-attempt
          - runtime.md#rt-rte-hotpotqa-attempt
          note: Selection and deletion compress the retained attempt into an excerpt of its existing content,
            not a semantic model summary.
        - value: decay
          basis: wired
          records: *id020
          note: Observation text is forgotten from the delivered retained excerpt even where the original
            trace remains in an agent list.
        records: *id020
        note: The cited records cover this named part and its consumer.
      - scope: HotPotQA latest-only combined diagnosis and programming current candidate replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id021
          - memory.md#mem-obj-hotpotqa-reflections
          - memory.md#mem-obj-last-attempt
          - runtime.md#rt-rte-hotpotqa-attempt
          - memory.md#mem-obj-reflections
          - memory.md#mem-obj-test-feedback
          - runtime.md#rt-obj-cur-func-impl
          - runtime.md#rt-rte-program-attempt
          note: Combined mode replaces the retained diagnosis list with the latest diagnosis; successor
            generation replaces the current candidate while archives can remain.
        records: *id021
        note: The cited records cover this named part and its consumer.
      - scope: Semantic transformation of generated plans/diagnoses across all producers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-alfworld-memory
        - memory.md#mem-obj-alfworld-logs
        - runtime.md#rt-rte-alfworld-trial
        - memory.md#mem-obj-webshop-memory
        - memory.md#mem-obj-webshop-logs
        - runtime.md#rt-rte-webshop-trial
        - memory.md#mem-obj-hotpotqa-reflections
        - memory.md#mem-obj-last-attempt
        - runtime.md#rt-rte-hotpotqa-attempt
        - memory.md#mem-obj-reflections
        - memory.md#mem-obj-test-feedback
        - runtime.md#rt-obj-cur-func-impl
        - runtime.md#rt-rte-program-attempt
        note: Requested explanation or new plan does not establish whether actual text consolidates existing
          claims or synthesizes a new claim. No output instances were inspected; those operation values
          cannot be completed.
      - scope: UCS search merge/eviction and opaque checkpoint maintenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-state
        - runtime.md#rt-rte-program-variants
        - memory.md#mem-obj-hotpotqa-checkpoints
        note: Outcome-bit identity is passed to unavailable search; it does not prove deduplication or
          eviction. Whole-object saving does not prove any curation operation.
      - scope: Possible provider-side state accumulated through use, separate from shipped pretrained
          model weights
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-cmp-gpt4
        - runtime.md#rt-cmp-gpt35
        - runtime.md#rt-cmp-text-davinci
        - runtime.md#rt-cmp-star-chat
        - runtime.md#rt-cmp-code-llama
        note: No provider-side memory transformation is exposed by generation-only clients.
      records:
      - memory.md#mem-obj-last-attempt
      - runtime.md#rt-rte-hotpotqa-attempt
      - memory.md#mem-obj-hotpotqa-reflections
      - memory.md#mem-obj-reflections
      - memory.md#mem-obj-test-feedback
      - runtime.md#rt-obj-cur-func-impl
      - runtime.md#rt-rte-program-attempt
      - memory.md#mem-obj-alfworld-memory
      - memory.md#mem-obj-alfworld-logs
      - runtime.md#rt-rte-alfworld-trial
      - memory.md#mem-obj-webshop-memory
      - memory.md#mem-obj-webshop-logs
      - runtime.md#rt-rte-webshop-trial
      - memory.md#mem-obj-state
      - runtime.md#rt-rte-program-variants
      - memory.md#mem-obj-hotpotqa-checkpoints
      - runtime.md#rt-cmp-gpt4
      - runtime.md#rt-cmp-gpt35
      - runtime.md#rt-cmp-text-davinci
      - runtime.md#rt-cmp-star-chat
      - runtime.md#rt-cmp-code-llama
      note: Supported curation is local excerpt compression/forgetting and replacement. Last-three delivery
        is a read selector, not withdrawal of the full plan list; success-based skipping, file cleanup
        and index identity alone do not establish invalidate, dedup or promote. Unknown generation semantics
        and opaque alternatives prevent a complete operation inventory.
    read_back_direction:
      assessment: partial
      units:
      - scope: Driver/agent retry prompt assembly and updater scenario delivery
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id022
          - memory.md#mem-obj-alfworld-memory
          - memory.md#mem-obj-alfworld-logs
          - runtime.md#rt-rte-alfworld-trial
          - memory.md#mem-obj-webshop-memory
          - memory.md#mem-obj-webshop-logs
          - runtime.md#rt-rte-webshop-trial
          - memory.md#mem-obj-hotpotqa-reflections
          - memory.md#mem-obj-last-attempt
          - runtime.md#rt-rte-hotpotqa-attempt
          - memory.md#mem-obj-reflections
          - memory.md#mem-obj-test-feedback
          - runtime.md#rt-obj-cur-func-impl
          - runtime.md#rt-rte-program-attempt
          note: Host retry/update triggers select indexed lists, agent-owned prior material, failed scenarios
            or latest code/feedback/hint without a consumer retrieval request.
        records: *id022
        note: The cited records cover this named part and its consumer.
      - scope: ALFWorld/WebShop explicit resume and operator-selected standalone programming result read
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id023
          - memory.md#mem-obj-alfworld-memory
          - memory.md#mem-obj-alfworld-logs
          - runtime.md#rt-rte-alfworld-trial
          - memory.md#mem-obj-webshop-memory
          - memory.md#mem-obj-webshop-logs
          - runtime.md#rt-rte-webshop-trial
          - memory.md#mem-obj-program-results
          - memory.md#mem-rte-result-validation
          note: An explicit caller request loads the selected configuration or result file; returning
            that requested file is not another push.
        records: *id023
        note: The cited records cover this named part and its consumer.
      - scope: Standalone validator solved-row selection after requested file acquisition
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id024
          - memory.md#mem-obj-program-results
          - memory.md#mem-rte-result-validation
          note: After file acquisition, software independently selects retained solved solutions/tests
            for the execution consumer.
        records: *id024
        note: The cited records cover this named part and its consumer.
      - scope: UCS visible state expansion delivery
        assessment: partial
        findings:
        - value: push
          basis: wired
          records: &id025
          - memory.md#mem-obj-state
          - runtime.md#rt-rte-program-variants
          note: Visible callbacks automatically supply state-specific candidate/hint/feedback to expansion.
        records: *id025
        note: Parent callbacks are wired; external scheduler invocation and further selection routes remain
          uninspected.
      - scope: Intended LeetCode audit file acquisition and candidate delivery
        assessment: partial
        findings:
        - value: pull
          basis: afforded
          records: &id026
          - memory.md#mem-rte-leet-evaluation
          note: The scaffold affords reading the explicitly selected input file.
        - value: push
          basis: afforded
          records: *id026
          note: The scaffold affords iteration over stored implementations for submission without grader
            retrieval requests.
        records: *id026
        note: Entry-point defects block executable delivery; the scaffold does not establish wired remote
          read-back.
      - scope: HotPotQA saved-agent reload
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-hotpotqa-checkpoints
        note: The writer was inspected but no saved-agent reload caller was established. Retention alone
          cannot establish either direction or a bounded absence.
      - scope: Possible provider-side state accumulated through use, separate from shipped pretrained
          model weights
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-cmp-gpt4
        - runtime.md#rt-cmp-gpt35
        - runtime.md#rt-cmp-text-davinci
        - runtime.md#rt-cmp-star-chat
        - runtime.md#rt-cmp-code-llama
        note: No later-consumer route for possible provider-accumulated memory is exposed.
      records:
      - memory.md#mem-obj-alfworld-memory
      - memory.md#mem-obj-alfworld-logs
      - runtime.md#rt-rte-alfworld-trial
      - memory.md#mem-obj-webshop-memory
      - memory.md#mem-obj-webshop-logs
      - runtime.md#rt-rte-webshop-trial
      - memory.md#mem-obj-hotpotqa-reflections
      - memory.md#mem-obj-last-attempt
      - runtime.md#rt-rte-hotpotqa-attempt
      - memory.md#mem-obj-reflections
      - memory.md#mem-obj-test-feedback
      - runtime.md#rt-obj-cur-func-impl
      - runtime.md#rt-rte-program-attempt
      - memory.md#mem-obj-program-results
      - memory.md#mem-rte-result-validation
      - memory.md#mem-obj-state
      - runtime.md#rt-rte-program-variants
      - memory.md#mem-rte-leet-evaluation
      - memory.md#mem-obj-hotpotqa-checkpoints
      - runtime.md#rt-cmp-gpt4
      - runtime.md#rt-cmp-gpt35
      - runtime.md#rt-cmp-text-davinci
      - runtime.md#rt-cmp-star-chat
      - runtime.md#rt-cmp-code-llama
      note: Requested configuration/file acquisition and automatic later selection are separate operations.
        Both pull and push are supported; checkpoint reload, external search, defective remote audit and
        provider routes retain local uncertainty.
    read_back_signal:
      assessment: partial
      units:
      - scope: ALFWorld/WebShop per-task plan and scenario push
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id027
          - memory.md#mem-obj-alfworld-memory
          - memory.md#mem-obj-alfworld-logs
          - runtime.md#rt-rte-alfworld-trial
          - memory.md#mem-obj-webshop-memory
          - memory.md#mem-obj-webshop-logs
          - runtime.md#rt-rte-webshop-trial
          note: Trial/update trigger matches the indexed configuration to its own plan list and corresponding
            log scenario.
        - value: coarse
          basis: wired
          records: *id027
          note: Recency limits that matched list to the last three plans; failure/success/skip gates determine
            availability, not semantic relevance.
        records: *id027
        note: The cited records cover this named part and its consumer.
      - scope: HotPotQA agent-owned retained strategy material
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id028
          - memory.md#mem-obj-hotpotqa-reflections
          - memory.md#mem-obj-last-attempt
          - runtime.md#rt-rte-hotpotqa-attempt
          note: Retry trigger selects current-agent material by strategy and whole-list/latest availability;
            the trace copy is reduced by line type/size and token budget. Neither operation demonstrates
            identity matching across a store or semantic relevance judgment.
        records: *id028
        note: The cited records cover this named part and its consumer.
      - scope: Ordinary/immediate programming retry and standalone solved-row execution
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id029
          - memory.md#mem-obj-reflections
          - memory.md#mem-obj-test-feedback
          - runtime.md#rt-obj-cur-func-impl
          - runtime.md#rt-rte-program-attempt
          - memory.md#mem-obj-program-results
          - memory.md#mem-rte-result-validation
          - runtime.md#rt-rte-program-variants
          note: Internal failure or variant iteration supplies current/latest task values; later validation
            supplies rows gated by is_solved. These are availability and outcome predicates, not semantic
            retrieval.
        records: *id029
        note: The cited records cover this named part and its consumer.
      - scope: UCS state-specific expansion and unavailable search selection
        assessment: partial
        findings:
        - value: coarse
          basis: wired
          records: &id030
          - memory.md#mem-obj-state
          - runtime.md#rt-rte-program-variants
          note: A callback supplies its current node fields; parent failing-test cost and outcome-bit
            identity do not demonstrate an identity match selecting delivered memory.
        records: *id030
        note: Missing search code prevents classifying its actual candidate selector. No identifier-based
          or inferred selector is inferred from the node ID API.
      - scope: Intended LeetCode implementation iteration
        assessment: partial
        findings:
        - value: coarse
          basis: afforded
          records: &id031
          - memory.md#mem-rte-leet-evaluation
          note: Afforded iteration supplies every stored implementation without a relevance predicate;
            delivery is blocked at entry.
        records: *id031
        note: Parent iteration is visible but executable delivery and remote internals remain unresolved.
      - scope: HotPotQA checkpoint read-back selection
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-hotpotqa-checkpoints
        note: No reload route is established, so no push selector can be classified and pull-only inapplicability
          is not justified.
      - scope: Possible provider-side state accumulated through use, separate from shipped pretrained
          model weights
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-cmp-gpt4
        - runtime.md#rt-cmp-gpt35
        - runtime.md#rt-cmp-text-davinci
        - runtime.md#rt-cmp-star-chat
        - runtime.md#rt-cmp-code-llama
        note: No provider-side push trigger, selector input or selected retained part is inspectable.
      records:
      - memory.md#mem-obj-alfworld-memory
      - memory.md#mem-obj-alfworld-logs
      - runtime.md#rt-rte-alfworld-trial
      - memory.md#mem-obj-webshop-memory
      - memory.md#mem-obj-webshop-logs
      - runtime.md#rt-rte-webshop-trial
      - memory.md#mem-obj-hotpotqa-reflections
      - memory.md#mem-obj-last-attempt
      - runtime.md#rt-rte-hotpotqa-attempt
      - memory.md#mem-obj-reflections
      - memory.md#mem-obj-test-feedback
      - runtime.md#rt-obj-cur-func-impl
      - runtime.md#rt-rte-program-attempt
      - memory.md#mem-obj-program-results
      - memory.md#mem-rte-result-validation
      - runtime.md#rt-rte-program-variants
      - memory.md#mem-obj-state
      - memory.md#mem-rte-leet-evaluation
      - memory.md#mem-obj-hotpotqa-checkpoints
      - runtime.md#rt-cmp-gpt4
      - runtime.md#rt-cmp-gpt35
      - runtime.md#rt-cmp-text-davinci
      - runtime.md#rt-cmp-star-chat
      - runtime.md#rt-cmp-code-llama
      note: Identifier matching is supported for indexed environment/session configurations, while recency,
        strategy, outcome and budget rules are coarse. No embedding, lexical or model-judgment relevance
        selector is established; unresolved routes prevent complete coverage or blanket inapplicability.
    trace_learning:
      assessment: partial
      units:
      - scope: ALFWorld failure-log-to-plan-to-later-action/update chain
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id032
          - memory.md#mem-obj-alfworld-memory
          - memory.md#mem-obj-alfworld-logs
          - runtime.md#rt-rte-alfworld-trial
          note: Automatic plan append persists in task JSON and reaches the next action and reflection
            consumers.
        records: *id032
        note: The cited records cover this named part and its consumer.
      - scope: WebShop failure-log-to-plan-to-later-reflection chain
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id033
          - memory.md#mem-obj-webshop-memory
          - memory.md#mem-obj-webshop-logs
          - runtime.md#rt-rte-webshop-trial
          note: Automatic persisted plans reach subsequent reflection production even though the action
            prompt omits them.
        records: *id033
        note: The cited records cover this named part and its consumer.
      - scope: HotPotQA scratchpad-to-diagnosis or retained last-attempt excerpt-to-next-call chain
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id034
          - memory.md#mem-obj-hotpotqa-reflections
          - memory.md#mem-obj-last-attempt
          - runtime.md#rt-rte-hotpotqa-attempt
          note: Automatic retained diagnosis or lossy prior-trace excerpt reaches the next reasoning/action
            call; new knowledge and proven improvement are not required.
        records: *id034
        note: The cited records cover this named part and its consumer.
      - scope: Ordinary Python feedback-fed hints and immediate-refinement feedback-fed candidate replacement
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id035
          - memory.md#mem-obj-reflections
          - memory.md#mem-obj-test-feedback
          - runtime.md#rt-obj-cur-func-impl
          - runtime.md#rt-rte-program-attempt
          - runtime.md#rt-rte-program-variants
          note: Recorded execution feedback automatically produces retained successor-shaping hints or
            candidate code consumed on later calls; result files archive the material.
        records: *id035
        note: The cited records cover this named part and its consumer.
      - scope: Immediate-reflexion with omitted execution feedback
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-program-variants
        - memory.md#mem-obj-reflections
        note: The recorded derivation is candidate-fed, not executed-test-trace-fed. Records do not provide
          a bounded qualifying-trace absence warrant, so no local no or tool-trace positive is assigned.
      - scope: UCS visible feedback-fed successor production
        assessment: partial
        findings:
        - value: 'yes'
          basis: wired
          records: &id036
          - memory.md#mem-obj-state
          - runtime.md#rt-rte-program-variants
          note: Parent expansion uses candidate execution feedback to author retained state-specific hints
            and successor candidates.
        records: *id036
        note: Visible Python callback chain is wired; missing search scheduling, horizon and additional
          write routes prevent complete assessment.
      - scope: Whole-object checkpoint extras and standalone audit artifacts
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-hotpotqa-checkpoints
        - memory.md#mem-rte-leet-evaluation
        - memory.md#mem-obj-program-results
        - memory.md#mem-rte-result-validation
        note: Saving alone does not establish an additional behavior-shaping trace-fed write/later consumer.
          No audit result writeback is implemented in the named validator, but this does not warrant a
          whole-boundary no.
      - scope: Possible provider-side state accumulated through use, separate from shipped pretrained
          model weights
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-cmp-gpt4
        - runtime.md#rt-cmp-gpt35
        - runtime.md#rt-cmp-text-davinci
        - runtime.md#rt-cmp-star-chat
        - runtime.md#rt-cmp-code-llama
        note: Possible provider trace-fed adaptation or retained continuation state is inaccessible; generation-only
          client behavior is not a negative warrant.
      records:
      - memory.md#mem-obj-alfworld-memory
      - memory.md#mem-obj-alfworld-logs
      - runtime.md#rt-rte-alfworld-trial
      - memory.md#mem-obj-webshop-memory
      - memory.md#mem-obj-webshop-logs
      - runtime.md#rt-rte-webshop-trial
      - memory.md#mem-obj-hotpotqa-reflections
      - memory.md#mem-obj-last-attempt
      - runtime.md#rt-rte-hotpotqa-attempt
      - memory.md#mem-obj-reflections
      - memory.md#mem-obj-test-feedback
      - runtime.md#rt-obj-cur-func-impl
      - runtime.md#rt-rte-program-attempt
      - runtime.md#rt-rte-program-variants
      - memory.md#mem-obj-state
      - memory.md#mem-obj-hotpotqa-checkpoints
      - memory.md#mem-rte-leet-evaluation
      - memory.md#mem-obj-program-results
      - memory.md#mem-rte-result-validation
      - runtime.md#rt-cmp-gpt4
      - runtime.md#rt-cmp-gpt35
      - runtime.md#rt-cmp-text-davinci
      - runtime.md#rt-cmp-star-chat
      - runtime.md#rt-cmp-code-llama
      note: Qualifying automatic retained-guidance chains support yes without claiming improved capacity
        or exercised learning. WebShop has a later reflection consumer, not action-plan delivery. Candidate-only,
        checkpoint, search and provider alternatives remain unresolved, so no system-wide no is authored.
    trace_source:
      assessment: partial
      units:
      - scope: ALFWorld and WebShop qualifying failure-log plan writes
        assessment: partial
        findings:
        - value: trajectories
          basis: wired
          records: &id037
          - memory.md#mem-obj-alfworld-memory
          - memory.md#mem-obj-alfworld-logs
          - runtime.md#rt-rte-alfworld-trial
          - memory.md#mem-obj-webshop-memory
          - memory.md#mem-obj-webshop-logs
          - runtime.md#rt-rte-webshop-trial
          note: Per-task logs link actions, environmental observations and outcomes across multi-step
            attempts.
        - value: tool-traces
          basis: wired
          records: *id037
          note: Recorded environment actions/results and HTTP-client observations supply execution feedback
            to the update.
        records: *id037
        note: Normal trace-fed paths are supported; WebShop assertion-only failure records may lack a
          full trajectory, and historical input instances were not inspected. Static examples are auxiliary
          inputs, not trace sources.
      - scope: HotPotQA qualifying diagnosis and prior-attempt excerpt writes
        assessment: partial
        findings:
        - value: trajectories
          basis: wired
          records: &id038
          - memory.md#mem-obj-hotpotqa-reflections
          - memory.md#mem-obj-last-attempt
          - runtime.md#rt-rte-hotpotqa-attempt
          note: Scratchpads link thoughts/actions/observations and the attempt outcome used by later calls.
        - value: tool-traces
          basis: wired
          records: *id038
          note: ReAct scratchpads include Search/Lookup request/result experience consumed by reflection
            or excerpt retention.
        records: *id038
        note: The tool-trace finding applies to ReAct, not no-context CoT. Supporting paragraphs/static
          examples alone are imported auxiliary content. Historical scratchpad contents and alternate
          instances remain uninspected.
      - scope: Programming ordinary/immediate-refinement and visible UCS feedback-fed writes
        assessment: partial
        findings:
        - value: tool-traces
          basis: wired
          records: &id039
          - memory.md#mem-obj-reflections
          - memory.md#mem-obj-test-feedback
          - runtime.md#rt-obj-cur-func-impl
          - runtime.md#rt-rte-program-attempt
          - memory.md#mem-obj-state
          - runtime.md#rt-rte-program-variants
          note: Executor feedback records assertion outcomes, errors or outputs used to write later hints/candidates.
        records: *id039
        note: This finding covers executed-feedback branches and visible Python UCS callbacks, not immediate-reflexion
          with omitted feedback, blocked Rust generation or unavailable search-produced inputs.
      - scope: Additional qualifying writes inside missing search, checkpoint extras or initial imported
          payloads
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-state
        - runtime.md#rt-rte-program-variants
        - memory.md#mem-obj-hotpotqa-checkpoints
        - memory.md#mem-obj-alfworld-memory
        - memory.md#mem-obj-alfworld-logs
        - runtime.md#rt-rte-alfworld-trial
        - memory.md#mem-obj-webshop-memory
        - memory.md#mem-obj-webshop-logs
        - runtime.md#rt-rte-webshop-trial
        note: Unknown additional write routes and historical payload provenance prevent classifying their
          original trace inputs; imported files and serialization labels are not themselves trace origins.
      - scope: Possible provider-side state accumulated through use, separate from shipped pretrained
          model weights
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-cmp-gpt4
        - runtime.md#rt-cmp-gpt35
        - runtime.md#rt-cmp-text-davinci
        - runtime.md#rt-cmp-star-chat
        - runtime.md#rt-cmp-code-llama
        note: The original inputs to any provider-side qualifying trace-fed write are not exposed.
      records:
      - memory.md#mem-obj-alfworld-memory
      - memory.md#mem-obj-alfworld-logs
      - runtime.md#rt-rte-alfworld-trial
      - memory.md#mem-obj-webshop-memory
      - memory.md#mem-obj-webshop-logs
      - runtime.md#rt-rte-webshop-trial
      - memory.md#mem-obj-hotpotqa-reflections
      - memory.md#mem-obj-last-attempt
      - runtime.md#rt-rte-hotpotqa-attempt
      - memory.md#mem-obj-reflections
      - memory.md#mem-obj-test-feedback
      - runtime.md#rt-obj-cur-func-impl
      - runtime.md#rt-rte-program-attempt
      - memory.md#mem-obj-state
      - runtime.md#rt-rte-program-variants
      - memory.md#mem-obj-hotpotqa-checkpoints
      - runtime.md#rt-cmp-gpt4
      - runtime.md#rt-cmp-gpt35
      - runtime.md#rt-cmp-text-davinci
      - runtime.md#rt-cmp-star-chat
      - runtime.md#rt-cmp-code-llama
      note: Execution feedback and multi-step experience establish tool-traces and trajectories on the
        named producers. Agent scratchpad role labels do not alone establish recorded conversational session-logs;
        timestamped event-stream inputs are not established. Opaque and historical input alternatives
        prevent a complete source inventory.
---

# Reflexion memory profile

## Comparison rationale

This profile classifies accepted implementation records, not executed behavior. Every wired finding is conditional on reaching the inspected path and on its external calls returning. No observed or causal basis is supported by the supplied members. All axes remain partial because their inventories include unresolved parts, not because source wiring is weak evidence of the parts it actually exposes.

The central boundary is task-local accumulated experience. [MEM-OBJ-alfworld-memory](memory.md#mem-obj-alfworld-memory), [MEM-OBJ-hotpotqa-reflections](memory.md#mem-obj-hotpotqa-reflections) and [MEM-OBJ-reflections](memory.md#mem-obj-reflections) give advice to later model calls. Advice is knowledge authority here, not standing instruction authority. Raw experience has learning authority at the automatic update producer; its derived output has a separate downstream advisory role. Executable persisted programs instead have instruction authority at the actual code consumer in [MEM-RTE-result-validation](memory.md#mem-rte-result-validation). Success flags and result counts have host-control authority, not the language interpretation granted to plan text.

[MEM-OBJ-webshop-memory](memory.md#mem-obj-webshop-memory) qualifies for trace learning through the later reflection consumer, despite the absence of plan delivery to the action model in [RT-RTE-webshop-trial](runtime.md#rt-rte-webshop-trial). This positive does not claim an action-guidance improvement pathway. HotPotQA's retained lossy prior-attempt excerpt also qualifies when automatically written and supplied to a later call; neither novelty nor a model-generated semantic summary is required. Its compression and local forgetting do not imply consolidation of every accumulated diagnosis into a checked theory.

Requested configuration and file acquisition is pull. Automatic indexed-plan, latest-value and solved-row selection is push at its own later operation. Environment-index correspondence is an actual identity selector; a UCS outcome-bit ID merely passed to missing search code is not evidence that identity matching selected the material ultimately delivered. Latest/last-three, strategy, budget and outcome predicates remain coarse signals. Read-back is not inferred from physical serialization alone: [MEM-OBJ-hotpotqa-checkpoints](memory.md#mem-obj-hotpotqa-checkpoints) establishes a writer, not a saved-agent reload caller.

The supersession of the epistemic program-diagnosis object resolves to [MEM-OBJ-reflections](memory.md#mem-obj-reflections). The two standalone audit supersessions resolve to [MEM-RTE-result-validation](memory.md#mem-rte-result-validation) and [MEM-RTE-leet-evaluation](memory.md#mem-rte-leet-evaluation). Their duplicate evidence does not create additional consumers or increase evidence strength. The LeetCode scaffold remains afforded: its contradictory argument handling and unavailable grader prevent a wired standalone submission finding. Valid epistemic containers for task state, and their narrower memory parts, remain distinct rather than being merged.

The Python scope of [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt) and [RT-RTE-program-variants](runtime.md#rt-rte-program-variants) is preserved. The Rust generation caller's required-argument omission blocks complete generation-to-successor progression; independently callable Rust validators still consume saved source. Missing UCS scheduling and the evaluated-node versus archived-candidate mismatch prevent attributing a solved archived row to the selected node.

Unresolved initial dataset/example provenance, resumed-content control, serialized library-object internals, historical trace instances and possible provider-accumulated state remain local limitations. Fixed pretrained model weights are not automatically included as use-dependent memory. Their known parametric form cannot fill the unknown provider-memory unit. No explicit manual content-admission witness or bounded whole-memory negative is available, so neither is invented. Requested new plans and diagnoses do not establish synthesize without recorded output semantics.

Source-read log: none. This mapping used only the supplied accepted members, reconciliation and contracts; it neither added evidence nor reopened report verification.
