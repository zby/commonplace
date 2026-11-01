# Codification commits an operation to rules a clerk could follow

Workshop draft, 2026-11-01. A system codifies an operation when it commits the operation to a designated reference that settles the relevant choices by rules a clerk could follow. This file is step 2 of the [workshop](./README.md): it gives the account that the [proposed definitions](./candidate-definitions.md) apply. It is an architectural account of a commitment made in a system, not a theory of language. The [tentative theory of natural language](./where-meaning-is-settled.md) is a side result, and nothing here depends on it.

## Three questions the current definitions run together

1. **What governs correctness.** Which reference the system holds the consumer to.
2. **How content is represented.** Whether an identifiable unit carries the content, and whether its consequences are assigned or reinterpreted on each consumption.
3. **How unresolved choices are handled.** What happens when the rules do not settle a case.

The current [codification](../../theory/definitions/codification.md) definition answers all three with one phrase. [Astra's review](./review-2026-11-01-astra.md) showed that each needs its own test. The sections below take them in turn.

## The hypothesis

Astra, in a [follow-up comment](./review-2026-11-01-astra.md#follow-up-comment-prompted-by-the-tarski-thread) prompted by the Tarski thread:

> The practical difference is not formalizability versus non-formalizability. It is whether the operation has been committed to a delimited interpretation regime, or still relies on ordinary linguistic judgment to settle what its instructions require.

The workshop adopts this as the hypothesis under test. It concerns the operation; representational form is a separate question, treated below. The commitment restates it in full, and its two conjuncts fix the hypothesis's three terms: *committed* is the first conjunct, *delimited* is what the second tests for, and *ordinary linguistic judgment* is what the second excludes.

## The commitment

> For a specified operation, a system can commit to rules that determine permitted behavior instead of asking a consumer to recover the intended operation afresh from natural language. The commitment names a reference, and the reference settles the relevant choices by rules a consumer forbidden insight could follow. It may include permitted variation, external inputs and declared clarification steps. Its adequacy to the original requirement remains a separate question.

Two conjuncts, and both are needed.

**A designated reference governs.** The system has adopted an implementation, a specification, or a specification plus execution parameters as what the artifact's language means. A consumer held to it that departs from it is wrong. Designation is an act of the system: the same instruction can be committed to a regime in one system and left to ordinary judgment in another. CPython is Python's reference only where a project has adopted its behavior as such; otherwise a CPython deviation from the language reference is a bug. A validator fixes what a schema means only where the system has adopted it as the reference rather than as one implementation of a schema language. [Which reference is designated decides what counts as a violation, not whether behavior can be formally described](./implementation-and-shared-semantics.md). The reference is stated outside the artifact's language, in a specification, a machine, or both. Whether natural language can have a reference stated outside itself is the [Tarski thread](./tarski-thread.md), and this account does not depend on its answer.

**The reference settles by rules a clerk could follow.** Turing derived the formal machine by asking what a human computer can do when following exact instructions without insight ([Church–Turing](../../sources/church-turing-thesis-sep.ingest.md)). This conjunct tests for the hypothesis's delimited regime: Tarski's exactly specified structure, in the sense the [1944 paper](../../sources/tarski-semantic-conception-of-truth.ingest.md) gives it. The regime fixes which expressions count, which terms are undefined, and under what conditions a sentence is asserted or an action permitted, so what the instructions require is settled within the regime and not by appeal outside it. The hypothesis's ordinary linguistic judgment is judgment by whoever reads, under conventions that no designated reference fixes. A reference that settles choices by judgment about what was intended governs without codifying. A contract's arbitrator and a workflow's human judge of "sufficient evidence" are designated readers who still exercise that judgment, so they fail this conjunct. A frozen prompt–model package is committed to a delimited regime by stipulation: the regime is the package's behavior, not the conventions of English. An ambiguous passage in a language standard is a gap in a reference that otherwise passes this conjunct: the passage governs, but it does not settle.

Where the reference leaves a choice open, that is a declared gap. C's undefined, unspecified and implementation-defined behaviors are named in advance. Whether a particular program reaches such a gap can be undecidable, so the claim concerns what the reference declares, not what a consumer can decide before running.

## Representation is a separate question

Form is a property of an artifact under a consumption path. Commitment is a property of a system. They usually coincide: a script consumed by its designated interpreter is symbolic because its consequences are assigned by the commitment. They can come apart, and when they do the artifact is split by operative part or consumption path, as [representational form](../../theory/definitions/representational-form.md) already allows for mixed artifacts.

The frozen prompt–model package is the clear case of the two coming apart. Adopting the package as the reference for one operation commits that operation. It does not change the form of the parts: the prompt stays natural-language and the weights stay distributed-parametric. What the commitment adds is that, for this operation, the package's behavior is what counts, so a different model reading the same prompt performs a different operation.

The assigned-consequences axis of representational form should therefore read: consequences are assigned when the artifact is consumed under a commitment of the kind above, and reinterpreted on each consumption otherwise.

## Unresolved choices are handled differently on each side

A codified consumer handles an unresolved choice only through a step the rules declare: an error, a declared default, an Ambiguous result, or a question to the user about the *input*. An interactive parser that offers two parses is asking which reading of the input sentence was intended. It is not asking its author what the grammar means. What codification removes is the channel for asking what the artifact itself means through a step the rules did not declare. Interactions the rules provide for remain, and they are declared in advance.

A consumer of natural language can ask the author what the artifact means, and in ordinary use does. When it cannot, because the author is unavailable or the run is noninteractive, it must either leave the readings open or choose, and the choice is its own. This is the mechanism behind the library's advice to [fix what the executor cannot determine](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md): whatever no declared step will handle must be settled before the artifact is handed over. It is also one reason [progressive constraining commits only after patterns stabilize](../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md): the commitment removes the channel for asking what the rule means, so the rule must already be right.

Diagnostic: if a consumer can legitimately ask the author what the artifact means, through a channel the rules did not declare, the artifact is natural-language under that consumption path.

## Boundary cases

| Artifact | Designated reference | Settles without judgment | Form under that path | Note |
|---|---|---|---|---|
| Python script in a project that runs CPython | CPython at a version | yes | symbolic | the project adopted the implementation |
| schema enum | the validator | yes | symbolic | only for the fields the validator reads |
| route table | the resolver | yes | symbolic | the operative part the resolver reads |
| regular expression | the engine | yes | symbolic | the engine's dialect is part of the reference |
| test suite | the runner and the code under test | yes | symbolic | what it checks is a proxy for the requirement |
| YAML frontmatter on a skill | the loader, for declared fields | yes, for those fields | mixed | the instructions stay natural-language |
| prose instruction run by a model | none | — | natural-language | no reference designated; the model reads the instruction |
| ambiguous passage in a language standard | the standard | no, at that passage | gap in a symbolic reference | governs without settling |
| contract clause with a designated arbitrator | the arbitrator | no | natural-language | designation without codification |
| workflow step judged by a human | the human | no | natural-language | same |
| interactive parser that asks which parse | the grammar | yes; the question concerns the input | symbolic | the clarification step is declared |
| prompt whose output is parsed by a schema | the schema, for the output | yes, for the output | mixed | prompt natural-language, output contract symbolic |
| frozen prompt–model package adopted for one operation | the package | running it needs none; what it does was shaped by judgment (open question 2) | operation committed; prompt natural-language, weights distributed-parametric | commitment and form treated separately |

## Open questions

1. Does "designated reference" need a definition of its own in the library, or do the two conjunct paragraphs above suffice?
2. The second conjunct is the clerk test. Does it classify an LLM-based validator correctly, where a system has adopted a model's judgment as the reference for a check? The account says the operation is committed while the check stays natural-language in form. Confirm this is the answer the KB wants.
3. Does the boundary table survive a reviewer adding cases?
4. Is "declared clarification step" enough to separate the parser case from an agent that asks what an instruction means, or does the input-versus-artifact wording need to be explicit in the library?
