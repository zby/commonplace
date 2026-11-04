---
description: "Two accounts of prompting share a behavior-prediction problem but assign failures differently: English governs requirements, or an adopted model package defines the prompt language."
type: types/note.md
brief: prompting-changes-failure-diagnosis-with-the-semantic-reference.brief.md
traits: [title-as-claim, has-comparison]
tags: [learning-theory, computational-model, constraining, llm-reliability]
---

# Prompting changes failure diagnosis with the semantic reference

Prompting can be understood as programming in a model-defined language, using English as an accessible approximation, or as asking a fallible interpreter to execute English instructions. The activity can be identical under both accounts. What changes is the reference that determines whether execution is wrong. Both accounts face the same problem of predicting the package's behavior; changing the reference changes the diagnosis without making that prediction cheaper.

This distinction matters when writing and maintaining KB instructions. An unwanted response may reveal an unsettled requirement, a departure from a settled instruction, or a poor prediction of what a particular prompt will do. Those findings can coexist, and their repairs target different things.

## Programming in a model-defined prompt language

Consider a language whose expressions use English surface forms and whose semantics is supplied by a specified LLM package. Fix the model, inference and decoding rules, runtime assumptions, and how context and other inputs enter execution. A [formal account of the implemented computation](./implementations-do-not-establish-shared-semantics.md) can then describe its behavior. Sampling, if present, is part of that account; precise semantics does not require one identical output on every run.

Under this stipulated reference, writing a prompt is programming in the language the package defines. A system that adopts the package as the governing reference for an operation makes its prompts [symbolic under that consumption path](./definitions/representational-form.md): localized content whose consequences are fixed by the reference. Describing this possible language does not establish that every prompting system has adopted it. Nor does adoption make the package authoritative over English generally.

The package's semantics may be precise while too complex to inspect for a particular question. [Opacity](./opacity-depends-on-the-inspection-question-and-budget.md) means that establishing the behavior or the effect of a change exceeds an acceptable inspection cost. A short prompt can have that problem even when every word is familiar. Conversely, some properties of a prompt can be easy to understand, and conventional code can be opaque for a difficult system-wide question.

## English makes a coarse behavioral account available

“Translate into French” identifies a task and a place to change the target language. “Preserve personal names” identifies another responsibility. These are useful semantic parts, not merely separately editable strings. They suggest what a prompt edit will change without exposing the model computation that realizes its effects.

[English can approximate a model-defined prompt language](./english-can-approximate-a-model-defined-prompt-language.md) develops this relationship. The English reading is a candidate coarse account of selected behavioral effects. Its fidelity must be assessed for the package, inputs and edits where it will be used. Model-specific conventions and empirical probes can improve that account.

If the account captures the interactions relevant to a question, it supports local reasoning. Where it fails, the inspector needs a refinement or additional evidence. Useful understanding need not locate a separate block of parameters for each clause. [Near-decomposability](./near-decomposability-may-make-local-inspection-affordable.md), where interactions across parts can be summarized within the question's tolerance, is a proposed explanation of when such local inspection stays affordable. The prompting account does not require that conjecture to succeed.

## Executing English through a fallible interpreter

A caller can instead treat the English instructions as the governing specification and ask the LLM to carry them out. Execution can then violate the instruction even when it follows the model package exactly. It can also select an unwanted outcome that the instruction permits.

The governing reference includes the surrounding rules as well as the instruction. [Clear instructions can compose into an unsettled contract](./clear-instructions-can-compose-into-an-unsettled-contract.md): “Return JSON only” and “On failure, raise an exception” leave a choice unless the contract or runtime settles whether exceptions use a separate channel or a JSON error record. Scope, precedence and exception handling belong in the interpretation. The issue applies to human readers as well as models.

A deployed workflow needs to say who settles the applicable English reading. It may use the caller's clarification, a designated reviewer applying stated conventions, or an agreed contract with examples and precedence rules. These arrangements let a workflow adjudicate requirements. Naming a judge does not supply mechanically fixed semantics or make every verdict unambiguous.

Where the applicable contract and adjudication process leave a consequential reading unsettled, the diagnosis should retain that uncertainty. The disputed outcome cannot yet count as a demonstrated interpreter failure.

English consequently serves two roles. It states what the system should do, and it supplies an approximate account of what the model-defined program will do. A successful prediction can describe behavior the caller should reject. A clear requirement can be a poor prediction of what the model will produce.

## The same prediction problem, a different diagnosis

Suppose the applicable contract requires successful responses to contain JSON only. The caller and reviewer agree that no exception applies to the successful case under inspection. The package nevertheless produces a Markdown wrapper.

| Account | Diagnosis, assuming execution followed the specified package |
|---|---|
| Model-defined prompt language | The program permits behavior that fails the requirement. The English-based prediction was inadequate if it predicted JSON-only output. |
| English instruction execution | The interpreter violated the settled applicable instruction. |

For a fixed package, prompt, inputs, question and evidence, changing the account changes no behavior and supplies no new predictive information. Under the first account, the difficulty is inspecting an opaque language's behavior. Under the second, it includes predicting where the interpreter will depart from the intended instruction. These are two descriptions of the same behavior-prediction burden.

The adjudication of an English requirement can add work, so this does not assert equality of every evaluation cost.

An implementation can also fail to conform to the adopted package, for example by running a different version from the one specified. The model-defined account relocates the conformance reference; it does not make implementation failures impossible. A model upgrade changes that reference when adopted, while in the English account it changes the implementation assessed against the instruction. Neither account licenses assuming unchanged behavior.

## What the distinction changes in practice

The next action should follow the question that remains unresolved:

- **Settle the requirement.** Clarify scope, precedence, examples or an adjudication route when materially different obligations remain possible. Repeated model agreement does not decide what the caller should require.
- **Test the behavioral account.** Compare predicted effects with outputs across relevant inputs and edits. [Execution variation](./execution-indeterminism-is-a-property-of-the-sampling-process.md) determines when repetition or distributional checks are needed. Deterministic execution still needs coverage of different cases.
- **Check conformance against the named reference.** A test against the package's behavior and a review against the English instruction answer different questions. [Interpreter failure](./out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) is a diagnosis against a sufficiently settled instruction, not a synonym for every unwanted output.
- **Expose or enforce the needed operation.** A readable procedure or a validator can make a particular rule easier to inspect or enforce. The gain depends on the implemented rule and its activation, and does not establish that it captures the requirement adequately. [LLM–code boundaries](./llm-code-boundaries-are-natural-checkpoints.md) provide explicit values at which to check arguments and results.

[Constraining](./definitions/constraining.md) commits choices that narrow or rank permitted readings or behaviors. [Codification](./definitions/codification.md) moves a rule into symbolic form, either by rewriting it in a governed language or by adopting a consumer as its reference. Adoption can codify an operation without exposing a readable rule or reducing inference cost.

Extracting a repeated operation into code is a different intervention with potentially different inspection and execution costs. The [code-extraction trade-off](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) should be assessed against the required scope and available checks.

Version the prompt, its execution binding and the requirement used to assess it. Otherwise a changed outcome can hide a change in the program, reference or judging standard.

Neither account treats generated code as necessarily a valid interpretation of its source instruction, or removes the need to test adequacy after an operation is made deterministic.

## Scope

This is a distinction between governing references, not a claim about which account most users hold, a universal ranking of prompts and conventional code by inspection cost, or a literal internal interpret-then-execute pipeline. It needs no impossibility claim about formalizing English. Actual programming-language references can also have defects and unsettled cases.

The examples are conceptual cases. The reliability of an English-based abstraction, the usefulness of a particular near-decomposition, and the prevalence of failures caused by missing composition rules require empirical assessment. The proposed unification of addressability and near-decomposability remains open; this argument needs only meaningful parts and evidence about their interactions.

---

Relevant Notes:

- [Symbolic form holds consumers to a semantic reference](./symbolic-form-holds-consumers-to-a-semantic-reference.md) — grounds: adoption fixes the governing semantics separately from adequacy and inspection cost
- [English can approximate a model-defined prompt language](./english-can-approximate-a-model-defined-prompt-language.md) — mechanism: a coarse behavioral account supports local reasoning where its predictions hold
- [Clear instructions can compose into an unsettled contract](./clear-instructions-can-compose-into-an-unsettled-contract.md) — grounds: the English account must assess the whole applicable instruction set
- [Traditional software can bracket executor conformance; LLM systems cannot assume it](./traditional-software-can-bracket-executor-conformance-llm-systems.md) — extends: develops the conformance question under ordinary instruction interpretation
- [Opacity depends on the inspection question and budget](./opacity-depends-on-the-inspection-question-and-budget.md) — defined-in: the inspection obstacle shared by the two accounts for a fixed prediction question
