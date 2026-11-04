---
description: "Maps typing, testing, code extraction and versioning to the questions they answer; distinguishes requirement adequacy, conformance, predictive fidelity and execution variation."
type: types/note.md
brief: underspecification-and-indeterminism-complicate-programming-for.brief.md
traits: [title-as-claim, has-comparison]
tags: [learning-theory, computational-model, constraining, llm-reliability]
---

# Programming practices for prompts need evidence matched to the question

Typing, testing, code extraction and version control help maintain prompts and KB instructions when each practice addresses a specific question. A type check can establish that required fields are present without establishing that their contents are correct. Repeated runs can estimate failure frequency without settling which outputs should count as failures. The useful transfer from programming is the check and the evidence it supplies, together with the limits of that evidence.

[The two accounts of prompting](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) distinguish executing an English instruction from programming in a language defined by an adopted model package. The same prompt can be assessed under either account. A precise model-defined semantics can remain [opaque](./opacity-depends-on-the-inspection-question-and-budget.md): establishing a behavior or the effect of an edit can exceed the inspection budget. English then supplies a candidate prediction of behavior, as well as a possible requirement against which behavior is judged.

## Testing starts with the question

Four questions call for different evidence. They can arise together; they are not exclusive failure classes.

| Question | Useful check | What it leaves unresolved |
|---|---|---|
| Does the requirement capture what is wanted? | Review examples, exclusions, scope and interactions with other instructions against the caller's intent. | Whether execution follows that requirement. |
| Does execution conform? | Compare behavior with the named reference: the applicable English instruction or the adopted package. | Whether conforming behavior meets the task's needs. |
| Does the behavioral description predict execution? | Compare predicted effects with observations across relevant inputs and edits. | Whether accurately predicted behavior is acceptable. |
| Do repeated executions vary in a way that matters? | Record execution conditions and compare outputs using the acceptance criterion. | Whether that criterion captures the requirement, or what caused a failure. |

For example, suppose the caller and reviewer agree that every successful response must be JSON, with no Markdown wrapper. A wrapper violates that English requirement. Under a model-defined language, the same wrapper can conform to the package while defeating the programmer's prediction and failing the requirement. Repeating the request can help estimate how often the wrapper appears. It does not determine whether wrappers should be accepted.

When the applicable instruction leaves a consequential choice unsettled, clarify it or retain the uncertainty in the verdict. [Clear instructions can compose into an unsettled contract](./clear-instructions-can-compose-into-an-unsettled-contract.md), so reviewing each clause separately may miss a scope or precedence issue. [Legal drafting](./legal-drafting-solves-the-same-problem-as-context-engineering.md) offers comparison cases for that English requirement work; it is not the explanation of every prompt-testing difficulty.

### Repetition and assertions answer different questions

[Output variation depends on decoding and execution conditions](./execution-indeterminism-is-a-property-of-the-sampling-process.md). Sampling can vary outputs; changing context, tool state or numerical serving conditions can also change them. A fixed prompt alone does not fix the complete computation.

Variation does not prevent assertions. Each response can be checked for valid JSON even when its contents differ. Repeated trials support estimates of failure frequency under the tested conditions; the number of trials depends on the estimate and uncertainty required, not a universal multiplier. Exact-output comparison is useful when exact reproduction is the property being checked.

A deterministic setup still needs coverage of different inputs and interactions. A finite sequence of identical answers does not prove determinism, and a consistently wrong answer is still wrong. [Debugging](./llm-debugging-starts-with-retry-versus-rewrite-triage.md) therefore compares intent, instruction and output before treating retry frequency as a diagnosis.

### Generators and their artifacts are separate testing targets

A prompt or template can be tested for the quality of the artifacts it produces. A retained artifact can also be checked on its own merits. [Selecting one output](./selecting-an-llm-output-fixes-a-result-not-its-interpretation.md) fixes the artifact to inspect without settling how later readers interpret it. This distinction applies to deterministic generators too.

The [text-testing pyramid](./automated-tests-for-text.md) offers artifact checks at different levels: deterministic structure checks, rubric-based content judgments, and compatibility with the surrounding corpus. A generated note passing those checks does not establish that its generator reliably produces acceptable notes. A good generator likewise does not certify every retained output.

## Other practices and their limits

### Typing

[Document types](./document-types-should-be-verifiable.md) identify expected structure and operations. [Procedure signatures](./instructions-are-typed-callables.md) can state which document types an operation accepts and produces. Their benefit depends on checking those expectations. Supplying an Evidence section makes evidence available for review; it does not establish that the evidence supports the claim.

### Code extraction

Replacing a repeated prompt operation with a readable function can expose its rule for inspection and testing. Under English instruction execution, this replacement may be described as projecting a specification into a particular implementation. Generation does not establish that the implementation is a valid projection. The implementation must be checked against the applicable requirement, including cases the observed runs did not cover.

[Progressive constraining](./progressive-constraining-commits-only-after-patterns-stabilize.md) uses recurring behavior to identify candidates for extraction. Recurrence alone establishes neither adequacy nor equivalence. Compare the candidate with the required behavior and assess its inspection and execution costs. The gain depends on the extracted rule and its scope, not on code being inherently correct.

[Constraining](./definitions/constraining.md) commits choices that narrow or rank permitted readings or behaviors. [Codification](./definitions/codification.md) moves an operation into symbolic form through a governed language or adoption of a consumer as its reference. Adopting a model package can codify an operation without exposing a readable rule. Code extraction is therefore one intervention, not the definition of every codification.

Instructions, skills, hooks and scripts do not form an automatic progression in enforcement. [Activation and response must be assessed separately](./methodology-enforcement-is-constraining.md).

### Version control

Where they affect the comparison, version the prompt, assembled inputs, model and runtime binding, and the requirements or rubrics used to assess results. Version retained [knowledge artifacts](./definitions/knowledge-artifact.md) separately from their generator. Regeneration may reproduce an artifact when the full computation is fixed. When regeneration produces a different artifact, the recorded versions help identify what changed. A fixed version does not establish an unambiguous instruction or an adequate result.

### Design for testability

[Readable scripts and validators](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) can expose individual rules for review. [LLM–code boundaries](./llm-code-boundaries-are-natural-checkpoints.md) expose arguments and results that can be captured, checked and replayed under specified conditions. These mechanisms reduce particular inspection costs. They do not guarantee that the checks encode the right requirement or run at every relevant boundary.

## Scope

This account does not rank all prompts as harder to test than all conventional programs. Inspection cost depends on the question, available descriptions, tools and evidence. Conventional programs also need requirement assessment, implementation checks and adequate test coverage.

Underspecification and execution variation remain distinct concerns when present. Neither is necessary to every prompt operation, and neither exhausts its testing obligations. Precise semantics and deterministic execution can coexist with an opaque program and an inadequate requirement.

The examples are conceptual checks, not empirical claims that these practices improve every workflow. The choice and cost of a check depend on the property it must establish and the consequences of missing a defect.

---

Relevant Notes:

- [Prompting changes failure diagnosis with the semantic reference](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — grounds: the reference determines what counts as a conformance failure
- [English can approximate a model-defined prompt language](./english-can-approximate-a-model-defined-prompt-language.md) — grounds: predictive fidelity is separate from requirement adequacy
- [Automated tests for text](./automated-tests-for-text.md) — extends: checks applied to retained artifacts
- [LLM debugging separates specification gaps, instruction violations, and run-to-run variation](./llm-debugging-starts-with-retry-versus-rewrite-triage.md) — extends: selects repairs using distinct comparisons
- [Methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — grounds: packaging a procedure does not by itself establish enforcement
