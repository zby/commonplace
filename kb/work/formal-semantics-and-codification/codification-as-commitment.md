# Codification commits an operation to rules a clerk could follow

Workshop draft, 2026-11-01. A system codifies an operation when it commits the operation to a designated reference that settles the relevant choices by rules a clerk could execute. Whether those rules can be read and revised separately is a different, graded property. This file is step 2 of the [workshop](./README.md): it gives the account that the [proposed definitions](./candidate-definitions.md) apply. It is an architectural account of a commitment made in a system, not a theory of language. The [tentative theory of natural language](./where-meaning-is-settled.md) is a side result, and nothing here depends on it.

## Four questions the current definitions run together

1. **What governs correctness.** Which reference the system holds the consumer to.
2. **How content is represented.** Whether an identifiable unit carries the content, and whether its consequences are fixed by such a reference or reinterpreted on each consumption.
3. **How addressable the reference is.** Whether the rule that assigns a consequence can be pointed at, read, and revised separately, and at what cost.
4. **How unresolved choices are handled.** What happens when the rules do not settle a case.

The current [codification](../../theory/definitions/codification.md) definition answers all four with one phrase. [Astra's first review](./review-2026-11-01-astra.md) separated the first, second and fourth; the [second review](./review-2026-11-01-astra-second.md) showed that without the third the frozen prompt–model package is classified both ways. The sections below take them in turn.

## The hypothesis

Astra, in a [follow-up comment](./review-2026-11-01-astra.md#follow-up-comment-prompted-by-the-tarski-thread) prompted by the Tarski thread:

> The practical difference is not formalizability versus non-formalizability. It is whether the operation has been committed to a delimited interpretation regime, or still relies on ordinary linguistic judgment to settle what its instructions require.

The workshop adopts this as the hypothesis under test. It concerns the operation; representational form and addressability are separate questions, treated below. The commitment restates it in full, and its two conjuncts fix the hypothesis's three terms: *committed* is the first conjunct, *delimited* is what the second tests for, and *ordinary linguistic judgment* is what the second excludes.

## The commitment

> For a specified operation, a system can commit to rules that determine permitted behavior instead of asking a consumer to recover the intended operation afresh from natural language. The commitment names a reference, and the reference settles the relevant choices by rules a consumer forbidden insight could follow. It may include permitted variation, external inputs and declared clarification steps. Its adequacy to the original requirement remains a separate question.

Two conjuncts, and both are needed.

**A designated reference governs.** The system has adopted an implementation, a specification, or a specification plus execution parameters as what the artifact's language means. A consumer held to it that departs from it is wrong. Designation is an act of the system: the same instruction can be committed to a regime in one system and left to ordinary judgment in another, and running an implementation does not by itself adopt it. CPython is Python's reference only where a project has adopted its behavior as such; otherwise a CPython deviation from the language reference is a bug. A validator fixes what a schema means only where the system has adopted it as the reference rather than as one implementation of a schema language. [Which reference is designated decides what counts as a violation, not whether behavior can be formally described](./implementation-and-shared-semantics.md). The reference is external in its governing role; it need not be written in a different language from the artifact. An operation is interpreted relative to its governing rules, and the language's ability to describe or execute those rules does not remove the need to specify their interpretation.

**The reference settles by rules a clerk could execute.** Turing derived the formal machine by asking what a human computer can do when following exact instructions without insight ([Church–Turing](../../sources/church-turing-thesis-sep.ingest.md)). This conjunct tests for the hypothesis's delimited regime, and it asks one thing: that each step of applying the reference to the artifact be mechanically checkable. It does not ask that the reference's structure be merely precisely defined, which is weaker, nor that every consequence of the reference be decidable, which is stronger and often false. Tarski's exactly specified structure, in the sense the [1944 paper](../../sources/tarski-semantic-conception-of-truth.ingest.md) gives it, is the precondition: the regime fixes which expressions count, which terms are undefined, and under what conditions a sentence is asserted. Extending "asserted" to "an action permitted" is this workshop's adaptation, not Tarski's. The hypothesis's ordinary linguistic judgment is judgment by whoever reads, under conventions that no designated reference fixes. A reference that settles choices by judgment about what was intended governs without codifying. A contract's arbitrator and a workflow's human judge of "sufficient evidence" are designated readers who still exercise that judgment, so they fail this conjunct: no clerk can simulate the arbitrator. A frozen prompt–model package passes it: a clerk could simulate inference, and the package's behavior is what the designation makes count.

## What the reference leaves open

Three cases that the first draft ran together as "declared gaps":

- **Permitted variation.** The rules settle the allowed alternatives. "Return either A or B" completely specifies the permitted behavior; different permitted outputs are not disagreement about what is permitted, as [step 1](./implementation-and-shared-semantics.md) already separates. C's unspecified behavior, where the standard enumerates the options, is this case.
- **Required external selection.** An input or an implementation parameter supplies the choice, and the reference says so. C's implementation-defined behavior is this case; the implementation's documentation becomes part of the designated reference.
- **A defect in the reference.** The rules fail to settle what they were supposed to settle: an accidental ambiguity in a standard, or a case nobody foresaw. C's undefined behavior is a declared absence of any requirement, which the reference states in advance; an ambiguous passage is an undeclared absence, discovered on use. Both are gaps, and only the first is declared.

Whether a particular program reaches an open case can be undecidable, so these are claims about what the reference says, not about what a consumer can decide before running.

## Representation is a separate question

Form is a property of an artifact under a consumption path. Commitment is a property of a system. Under the consumption path the commitment governs, the artifact's consequences are fixed by the reference, and the artifact is symbolic under that path. Under a path with no designated reference, the same artifact is reinterpreted on each consumption and is natural-language under that path. Mixed artifacts are split by operative part or consumption path, as [representational form](../../theory/definitions/representational-form.md) already allows.

The frozen prompt–model package is the test case, and it decides the definition rather than being an exception to it. Adopting the package as the reference for one operation codifies that operation: both conjuncts hold. The prompt is then symbolic under that path. The same prompt read by whatever model a session happens to run is natural-language, because nothing fixes its consequences. The weights are distributed-parametric under any path. The library's misuse case against counting a fixed prompt and model as symbolic is right about its reason and wrong about its scope: repeatability is not designation, so repeatability alone does not make the prompt symbolic; designation does. A consequence the library should state: pinning a model version and adopting its behavior as the reference codifies the instructions it reads. It is a codification with almost no addressability, which is why it is a poor one, not why it is not one. The designation must include the decoding procedure, or model the output distribution as permitted variation.

## Addressability is separate and graded

A reference is addressable to the degree that the rule assigning a consequence can be pointed at, read, and revised without touching the rest. A schema is addressable. A grammar is addressable. A large legacy codebase is codified and only partly addressable. A frozen model is codified and, in practice, not addressable: tools exist in principle to locate what fixes a given consequence, and the cost is prohibitive. The library already holds that [opacity is a scale threshold](../../theory/opacity-is-a-scale-threshold.md), an inspection property that appears at sufficient scale in symbolic systems too, so addressability cannot be a conjunct of codification without declassifying large codebases.

Addressability sets two things that form alone does not. It sets the inspection method: a symbolic artifact is checked against its reference, statically where the reference's rules can be read, and by running cases where they cannot. And it sets where revision happens: with a schema, the rule is fixed; with a frozen package, the only addressable part is the prompt, so repair means editing the input or swapping the reference. This is the practical cost of codifying through a model.

## Unresolved choices are handled differently on each side

The claim here is an execution-contract claim. Execution follows declared transitions, and changes to the governing rules happen through a separately authorized process. A codified consumer handles an unresolved choice only through a step the rules declare: an error, a declared default, an Ambiguous result, or a question to the user about the *input*. An interactive parser that offers two parses is asking which reading of the input sentence was intended. It is not asking its author what the grammar means. What codification removes is the channel for asking what the artifact itself means through a step the rules did not declare. Interactions the rules provide for remain, and they are declared in advance.

A consumer of natural language can ask the author what the artifact means, and in ordinary use does. When it cannot, because the author is unavailable or the run is noninteractive, it must either leave the readings open or choose, and the choice is its own. This is the mechanism behind the library's advice to [fix what the executor cannot determine](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md): whatever no declared step will handle must be settled before the artifact is handed over. It is also one reason [progressive constraining commits only after patterns stabilize](../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md): the commitment removes the channel for asking what the rule means, so the rule must already be right. The availability of an undeclared channel is a symptom of the natural-language side, not a standalone test of form.

## Boundary cases

| Artifact | Designated reference | Clerk-executable | Addressable in practice | Form under that path | Note |
|---|---|---|---|---|---|
| Python script in a project that has adopted CPython as its reference | CPython at a version | yes | high | symbolic | adoption, not mere use, designates |
| schema enum | the validator | yes | high | symbolic | only for the fields the validator reads |
| route table | the resolver | yes | high | symbolic | the operative part the resolver reads |
| regular expression | the engine | yes | high | symbolic | the engine's dialect is part of the reference |
| test suite | the runner and the code under test | yes | high | symbolic | what it checks is a proxy for the requirement |
| large legacy codebase | its interpreter or compiler | yes | low | symbolic | codified and opaque at scale |
| YAML frontmatter on a skill | the loader, for declared fields | yes, for those fields | high | mixed | the instructions stay natural-language |
| prose instruction read by whatever model runs | none | — | — | natural-language | nothing fixes its consequences |
| the same instruction under a pinned, adopted model | the pinned package | yes | none in practice | symbolic under that path | codified by designation; revised through the prompt |
| ambiguous passage in a language standard | the standard | no, at that passage | high | defect in a symbolic reference | governs without settling |
| contract clause with a designated arbitrator | the arbitrator | no | — | natural-language | designation without codification |
| workflow step judged by a human | the human | no | — | natural-language | same |
| LLM-based validator adopted as the reference for a check | the frozen package | yes | none in practice | symbolic under that path | the check is committed; the requirement it proxies stays open |
| interactive parser that asks which parse | the grammar | yes; the question concerns the input | high | symbolic | the clarification step is declared |
| prompt whose output is parsed by a schema | the schema, for the output | yes, for the output | high for the schema | mixed | prompt natural-language unless its model is adopted, output contract symbolic |
| frozen prompt–model package adopted for one operation | the package, decoding included | yes | none in practice | operation codified; prompt symbolic under that path; weights distributed-parametric | the case that decides the definition |

## Open questions

1. Does the library want the consequence that pinning and adopting a model codifies the instructions it reads? If so, the representational-form misuse case and the inspection rule change as the [candidate definitions](./candidate-definitions.md) propose.
2. Addressability is stated as graded. Does any library rule need a threshold on it, or is "statically where the rules can be read, by running cases where they cannot" enough?
3. Does the boundary table survive a reviewer adding cases?
4. The parser-versus-agent distinction rests on the input-versus-artifact wording. Does that wording need to be explicit in the library, or does the execution-contract framing carry it?
