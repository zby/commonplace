# Symbolic form is a language close to a formal semantics, and codification is the move into it

An artifact is symbolic under a consumption path when its consequences under that path are fixed by the reference of a language that has a formal semantics or is close to one. A language is close to a formal semantics when its users hold its consumers to a reference, a standard or an implementation, from which a formal semantics could be derived. Codification is the move of a rule or operation from natural-language form into symbolic form. Whether the artifact and its reference let its behavior be read is a different property, marked by the modifier *opaque*, which does not change membership.

The difference between prompts and code is this: a prompt that works on a frozen, adopted model is code under this account. It is opaque code that keeps what membership gives and loses what reading gives. A prompt read by whatever model runs is not code under this account. This is an architectural account of artifacts and of a move a system makes, not a theory of language. The [side theory](./where-meaning-is-settled.md) proposes how repair, redefinition and change through use maintain linguistic conventions. The classification below does not depend on that explanation.

## Workshop context

Workshop draft, 2026-11-01, revised the same day after the operator's decisions on wording and order. This file is step 2 of the [workshop](./README.md): it gives the account that the proposed [representational form](./representational-form-definition.md) and [codification](./codification-definition.md) definitions apply. Its deliverable is the difference between prompts and code.

The operator's assessment, 2026-11-01, is recorded here: it is awkward that legibility coincides with symbolic form only under further conditions, and the definitions are cleaner for separating the two than they were when one phrase carried both.

Form comes first because the library already orders it so: [representational form](../../theory/definitions/representational-form.md) says that moves between forms are named operations and that codification moves content from natural-language into symbolic form. What the library lacks is a definition of symbolic form that does not lean on the retired phrase, and the current form definition sends the reader to codification for the test. The account below puts the test in the form.

## Four questions the current definitions run together

1. **How content is represented.** Whether an identifiable unit carries the content, and whether its consequences are fixed by a reference or reinterpreted on each consumption.
2. **What governs correctness.** Which reference the language's users hold consumers to.
3. **Whether the reference can be read.** Whether the rule that assigns a consequence can be pointed at, read, and revised separately, and at what cost.
4. **How unresolved choices are handled.** What happens when the rules do not settle a case.

The current [codification](../../theory/definitions/codification.md) definition answers all four with one phrase. The sections below take them in turn.

### Review context

[Astra's first review](./review-2026-11-01-astra.md) separated the first, second and fourth; the [second review](./review-2026-11-01-astra-second.md) showed that without the third the frozen prompt–model package is classified both ways.

## The hypothesis

Astra, in a [follow-up comment](./review-2026-11-01-astra.md#follow-up-comment-prompted-by-the-tarski-thread) prompted by the Tarski thread:

> The practical difference is not formalizability versus non-formalizability. It is whether the operation has been committed to a delimited interpretation regime, or still relies on ordinary linguistic judgment to settle what its instructions require.

The workshop adopts this as the hypothesis under test. It concerns the move, codification. What the move produces is an artifact in symbolic form, defined next. Whether the result is opaque is a separate question, treated below. The gloss of "close to a formal semantics" fixes the hypothesis's three terms: *committed* is the holding of consumers to a reference, *delimited* is what derivability tests for, and *ordinary linguistic judgment* is what derivability excludes.

## Symbolic form

> Content is symbolic under a consumption path when it sits in localized units whose consequences under that path are fixed by the reference of a language that has a formal semantics or is close to one. A language is close to a formal semantics when its users hold its consumers to a reference, a standard or an implementation, from which a formal semantics could be derived. The reference may leave permitted variation, external inputs, excluded guarantees and declared clarification steps.

Two conditions, and both are needed.

### The language's users hold consumers to a reference

A consumer held to the reference that departs from it is wrong. For C the reference is the standard; for Python it is the language reference together with CPython, so a CPython deviation from the language reference is a bug and a third-party interpreter that departs from both is wrong. Holding consumers to a reference is a convention of the language's users, so a project inherits it with the language; it does not have to adopt CPython for its scripts to count.

A system creates such a language only when it adopts a consumer as the reference: adopting a frozen prompt–model package for one operation makes the system the sole user of the language of prompts as that package reads them, and it holds the only consumer to the package. [Which reference governs decides what counts as a violation, not whether behavior can be formally described](./implementation-and-shared-semantics.md).

The reference is external in its governing role; it need not be written in a different language from the artifact. An operation is interpreted relative to its governing rules, and the language's ability to describe or execute those rules does not remove the need to specify their interpretation.

### A formal semantics could be derived from the reference

This is what [step 1](./implementation-and-shared-semantics.md) constructs: an implementation together with a machine model determines a formal account of execution, and a standard whose structure is exactly specified in the sense of Tarski's [1944 paper](../../sources/tarski-semantic-conception-of-truth.ingest.md), which expressions count, which terms are undefined, and under what conditions a sentence is asserted, supplies the material for one. Extending "asserted" to "an action permitted" is this workshop's adaptation, not Tarski's. Why derivation is possible is Turing's observation that a human computer following exact instructions without insight can be replaced by a machine ([Church–Turing](../../sources/church-turing-thesis-sep.ingest.md)); the clerk is the explanation, not the definition.

The condition asks one thing, that each step of applying the reference be mechanically checkable. It does not ask that every consequence of the reference be decidable, which is stronger and often false.

Designating a judge does not supply a rule, so a reference that settles by unformalized judgment about what was intended, a contract's arbitrator or a workflow's human judge of "sufficient evidence", governs without making the artifact symbolic. The exclusion is the unformalized judgment, not the human: a human following a formal procedure is the clerk, and a protocol that takes a human decision as an input is the required external selection treated below, which formalizes the step without formalizing the judgment. The hypothesis's ordinary linguistic judgment is judgment by whoever reads, under conventions that no held-to reference fixes.

### Three grades and consumption paths

Three grades follow. A language has a formal semantics when the derivation has been written and its users accept it as the language's: Standard ML, WebAssembly. It is close when the reference exists and the derivation is possible but unwritten: C, Python, a legacy codebase under its interpreter, a schema under its validator. It is neither when formalizations of its consumers exist and none is accepted as the language's: English.

Form is relative to the consumption path. Under a path with no held-to reference, the same artifact is reinterpreted on each consumption and is natural-language under that path. Mixed artifacts are split by operative part or consumption path, as the library's form definition already allows.

## A formalization of a consumer is not the semantics of the language

Step 1 shows that a frozen language model is as formalizable as a compiler. The formalization describes the consumer. It is the semantics of a language only when that language's users hold consumers to it. C's users hold every compiler to the standard, so a formalization derived from the standard is a formalization of C. A formalization derived from GCC describes GCC. Which of GCC's behaviors are C's is settled against the standard, and telling the bugs apart already requires it.

English's users hold no reader to the frozen model, so a reader that departs from it is not thereby wrong, and the model's formalization fixes nothing about English. The [side theory](./where-meaning-is-settled.md) describes the features by which the practice keeps that authority: repair, redefinition from inside and change by use. They are not what a formalization drops; they are how the practice keeps authority over every formalization. A formalization of English answers to the practice, which can overrule it from inside, and a frozen package is cut off besides, since the practice's corrections never reach it.

[Astra's answer](./probe-response-2026-11-01-astra.md) to the probe makes the limit precise: a fixed update rule fed with new evidence is a fixed formal specification that tracks a changing practice, so change by use does not block a formal account of English in principle, and a model with context handles repair and redefinition within a conversation. Formalizing a model does not by itself make its behavior authoritative for English. Adopting the model for an operation establishes that authority within the adopting system, not for English's users generally.

C's reference changes only by revision under its committee's authority, so the standard is what C's users are held to and a formalization derived from it drops nothing. The asymmetry is in which side answers to which, and that is what makes the gloss non-arbitrary. A community that came to hold its readers to a model would have made a scoped language that is symbolic under the criterion; it would not have made the model the semantics of English.

A system that adopts the package for an operation creates a language of one user, prompts as this package reads them, and the package's formalization is that language's semantics. So the prompt is symbolic under that path, and the semantics of English is untouched. The two claims are about different languages, and the workshop asserts both.

Adopting the package for an operation does not, by that act alone, establish it as an adequate semantics of English: a descriptive account of English answers to the practice, and the adoption answers to the system. Tarski's remark that formalized languages are fragments of natural languages provided with complete vocabularies and precise syntactical rules ([Truth and Proof](../../sources/tarski-truth-and-proof.ingest.md)) describes what adoption creates, a fragment under one user's rules; it is not a proof that English could not be described, and the account makes no such claim.

The earlier proposal that "close to a formal semantics" means a procedure for formalizing exists fails here: every implemented consumer has such a procedure, and what picks out the language's semantics among consumer formalizations is who is held to which.

## Codification is the move into symbolic form

> A system codifies a rule or operation stated in natural language when it moves the artifact that carries it into symbolic form under the consumption path the system uses. The consumer changes from one who reinterprets the text on each use to one bound by the reference, so what the artifact permits no longer depends on who reads it. The adequacy of the symbolic artifact to the original requirement remains a separate question.

The move is made in one of two ways. The ordinary way rewrites the artifact in a language close to a formal semantics: prose becomes code, a schema, a route table. The other way leaves the text alone and changes the consumption path: the system adopts a consumer, a pinned prompt–model package with its decoding procedure, as the reference for the operation. The text of the prompt does not change; its form under that path does, because the system has created a one-user language whose reference it holds the consumer to. This is the test case that decides the definition rather than an exception to it. The same prompt read by whatever model a session happens to run stays natural-language, because nothing fixes its consequences.

The weights have two consumption paths, and localization is relative to the path as form is. Under the runtime's path each kernel and parameter is an addressed unit whose consequences the pinned runtime fixes, so the weights are symbolic there, and opaque by scale. Under the path on which the whole model is run as the interpreter, nothing in them is addressed, so they are distributed-parametric there, and adoption does not change that. The [form definition](./representational-form-definition.md) states the rule in its derivation.

The library's misuse case against counting a fixed prompt and model as symbolic is right about its reason and wrong about its scope: repeatability is not adoption, so repeatability alone does not make the prompt symbolic; adoption does. A consequence the library should state: pinning a model version and adopting its behavior as the reference codifies the instructions it reads. It is an opaque codification, which is why it is a poor one, not why it is not one. The adoption must include the decoding procedure, or model the output distribution as permitted variation.

## What the reference leaves open

Four cases that the first draft ran together as "declared gaps":

- **Permitted variation.** The rules settle the allowed alternatives. "Return either A or B" completely specifies the permitted behavior; different permitted outputs are not disagreement about what is permitted, as [step 1](./implementation-and-shared-semantics.md) already separates. C's unspecified behavior, where the standard enumerates the options, is this case.
- **Required external selection.** An input or an implementation parameter supplies the choice, and the reference says so. C's implementation-defined behavior is this case; the implementation's documentation becomes part of the reference.
- **An excluded guarantee.** The reference states in advance that it requires nothing for a case. C's undefined behavior is this case: a declared absence of any requirement, which completely specifies that no behavior is guaranteed. It is not a failure of the reference.
- **A defect in the reference.** The rules fail to settle what they were supposed to settle: an accidental ambiguity in a standard, or a case nobody foresaw. This is an undeclared absence, discovered on use, and it is the only one of the four that is a failure of the reference.

Whether a particular program reaches an open case can be undecidable, so these are claims about what the reference says, not about what a consumer can decide before running.

## Opaque symbolic form

Adoption fixes which behavior counts as conforming. It does not make that behavior easy to understand, predict, revise or justify against the requirement. The usual advantages of symbolic form do not follow from membership, and the library already says so: [opacity is a scale threshold](../../theory/opacity-is-a-scale-threshold.md), not a class property, and any form becomes practically opaque at sufficient size. The account therefore gives symbolic form a modifier rather than a condition.

Symbolic content is **opaque** under a consumption path, relative to a behavior or change of interest, when the artifact together with its reference does not let an inspector establish that behavior, or the effect of that change, at acceptable cost. Opacity removes an affordable inspection route for the question at hand; evaluation then relies more on execution, on other analysis such as abstraction or certificates, or on explicitly retained uncertainty, and none of these is a guaranteed substitute for understanding. The definition is relative because the reference of a frozen package can be read rule by rule under the runtime's path, kernel by kernel, and that reading does not answer a question asked on the interpreter's path. Opaque is a label for an inspection property, as the library's note has it, not a fourth form; the form definition's misuse case against calling weights "opaque" as if opacity were the form still holds.

### Three sources of opacity

Three sources obstruct inspection, and the library names only the first.

- **The artifact's scale.** A trillion-line program is opaque because of its size: each line is readable against the C standard, and the whole is not. Opacity of this kind grows with size. Local edits often keep predictable local effects, and coupling erodes that as the program grows.
- **The reference's form.** The reference itself has a representational form under the path on which it is read. C's reference is symbolic: the standard, or a compiler read as an implementation of it, fixes what `+` does in a paragraph you can point at, on the same path the program is read on. The frozen package is readable rule by rule under the runtime's path, where each kernel and parameter is a unit, and it is used under the interpreter's path, where the rule that assigns a consequence to "summarize" is spread over all the weights and no unit carries it. The inspector's question lives on the second path, so reading on the first yields arithmetic. Opacity of this kind does not grow with size; it is present at the smallest unit. A one-line prompt is readable, and the effect of editing it is not read from the reference: it is predicted from experience with the package and confirmed by running cases. That is what "too complex to disentangle" means precisely, and it is why the loss is present for the frozen package at a scale where a program is still readable.
- **Deliberate obfuscation.** Cryptography formalized hiding how a program works. The strong form, the virtual black-box property, asks that whatever can be computed from the obfuscated program could be computed from input–output access alone. [Barak and co-authors](../../sources/on-the-impossibility-of-obfuscating-programs.ingest.md) prove that no obfuscator achieves it for all programs: assuming one-way functions, there are circuit families from which any equivalent circuit lets the source be reconstructed, while oracle access reveals nothing. Their explanation is that a program is a succinct description of the function on which one can perform computations, which black-box access cannot match, and the gap closes exactly for function classes learnable from queries. The counterexamples are contrived by the authors' own description, so the result rules out a general obfuscator, not obfuscation of any particular useful program.

  What exists provably is weaker: indistinguishability obfuscation hides which of the equivalent same-size programs was used, not what the function is, and [Jain, Lin and Sahai](../../sources/indistinguishability-obfuscation-well-founded-assumptions.ingest.md) construct one under four standard assumptions, with no claim about what it hides beyond that definition. Heuristic obfuscation, which the Barak paper illustrates with an obfuscated-code contest entry, is the practical evidence that function-preserving transformation defeats human readers.

  For the modifier two things follow. Opacity by construction is a definable source that owes nothing to scale, so opacity is not monotone in size. And symbolic form guarantees neither readability nor hiding: for the unobfuscatable families, reading strictly exceeds running, which is the advantage the modifier marks as lost when it is lost.

### What is lost and what stays

The modifier marks what is lost and what stays. Three questions stay apart throughout:

1. Whether execution conformed to the reference.
2. What behavior the reference specifies, including variation and failure outputs.
3. Whether that behavior satisfies the requirement.

Lost: checking by reading, since adequacy to intent is not established by comparing the rule the artifact invokes with the behavior wanted; and revision by locating the rule, since with a frozen package the only editable part is the input, so repair means editing the prompt or swapping the reference.

Not lost: declared behavior. The adoption declares what the package specifies, the decoding procedure, the output distribution as permitted variation, and any error, refusal or clarification output the package produces, and execution either conforms to it or does not.

A frozen package settles every input, so it has no unresolved choices in the sense defined under [What the reference leaves open](#what-the-reference-leaves-open); what is found on use, or by whatever other analysis is affordable, is whether the specified behavior satisfies the requirement. An adopted package that always returns a wrong summary for one input executes exactly and fails the summarization requirement. That is an inadequacy, not a newly discovered gap.

Opacity makes the third question harder, and the prediction of the second; it neither removes declared behavior nor turns inadequacy into an unspecified case. The resemblance to the natural-language side is in where the answer comes from, use rather than reading, not in what is unsettled.

What stays is what membership gives: what counts as wrong is fixed, a consumer that departs from the package is wrong, and the operation is committed and testable against a reference, repeatable where the decoding procedure is deterministic and varying within the declared distribution where it is not, which the natural-language path never gives.

### Cost and unreliability

The modifier drives cost and unreliability through one mechanism. Where the artifact and its reference can be read for the behavior in question, adequacy to intent can be checked before any run by comparing the rule the artifact invokes with the behavior wanted; reading does not prove adequacy, and it is the affordable route where it is available. Where they cannot, that route is gone, and inadequacies are found on use, by other analysis, or not at all until retained uncertainty is resolved. That is the cost.

The unreliability follows from the same fact: the package fixes what a changed prompt will do, decoding included, but the reference does not let one read it off. So every revision is an experiment. The unreliability is not in the formalization. It is in the inability to read it against the requirement.

### When to write the modifier

The modifier is written only where readability is at issue. Unmodified "symbolic" says that what counts as wrong is fixed and says nothing about whether the reference can be read; the usual case is that it can, and the text does not say so. "Opaque" is added where that usual accompaniment fails and the point depends on it: the frozen package, a codebase past the scale where reading stops working, an obfuscated program.

Two practical differences follow from the account, and they answer different questions. Whether a language is close to a formal semantics decides what counts as wrong. Whether the result is opaque decides what it costs to find out.

## Unresolved choices are handled differently on each side

The claim here is an execution-contract claim. Execution follows declared transitions, and changes to the governing rules happen through a separately authorized process. A consumer of a symbolic artifact handles an unresolved choice only through a step the rules declare: an error, a declared default, an Ambiguous result, or a question to the user about the *input*. An interactive parser that offers two parses is asking which reading of the input sentence was intended. It is not asking its author what the grammar means. What codification removes is the channel for asking what the artifact itself means through a step the rules did not declare. Interactions the rules provide for remain, and they are declared in advance.

A consumer of natural language can ask the author what the artifact means, and in ordinary use does. When it cannot, because the author is unavailable or the run is noninteractive, it must either leave the readings open or choose, and the choice is its own. This is the mechanism behind the library's advice to [fix what the executor cannot determine](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md): whatever no declared step will handle must be settled before the artifact is handed over. It is also one reason [progressive constraining commits only after patterns stabilize](../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md): the move removes the channel for asking what the rule means, so the rule must already be right. The availability of an undeclared channel is a symptom of the natural-language side, not a standalone test of form.

## Boundary cases

| Artifact | Held-to reference | Semantics derivable | Reference form | Form under that path | Note |
|---|---|---|---|---|---|
| Python script | the language reference and CPython at a version | yes | symbolic | symbolic | inherited with the language |
| schema enum | the validator | yes | symbolic | symbolic | only for the fields the validator reads |
| route table | the resolver | yes | symbolic | symbolic | the operative part the resolver reads |
| regular expression | the engine | yes | symbolic | symbolic | the engine's dialect is part of the reference |
| test suite | the runner and the code under test | yes | symbolic | symbolic | what it checks is a proxy for the requirement |
| large legacy codebase | its interpreter or compiler | yes | symbolic | symbolic, opaque | opacity from the artifact's scale |
| YAML frontmatter on a skill | the loader, for declared fields | yes, for those fields | symbolic | mixed | the instructions stay natural-language |
| prose instruction read by whatever model runs | none | — | — | natural-language | nothing fixes its consequences |
| the same instruction under a pinned, adopted model | the pinned package | yes | symbolic under the runtime's path, distributed-parametric under the interpreter's | symbolic, opaque, under that path | opacity from the reference's form; revised through the prompt |
| ambiguous passage in a language standard | the standard | no, at that passage | symbolic | defect in a symbolic reference | governs without settling |
| undefined behavior in C | the standard | yes | symbolic | symbolic | an excluded guarantee, declared in advance; not a defect |
| compiled program behind an API, from the caller | the API contract | yes | symbolic | symbolic, for the request | the program's internals are not under the caller's path |
| neural model behind the same API, from the caller | the API contract | yes | symbolic | symbolic, for the request | identical to the compiled program under this path; the two differ under the paths inside |
| contract clause with a designated arbitrator | the arbitrator | no | — | natural-language | held to unformalized judgment |
| workflow step judged by a human | the human | no | — | natural-language | held to unformalized judgment |
| workflow step that waits for a human approval input | the workflow engine | yes; the decision is an input | symbolic | symbolic | the human decision is a required external selection, not the rule |
| LLM-based validator adopted as the reference for a check | the frozen package | yes | symbolic under the runtime's path, distributed-parametric under the interpreter's | symbolic, opaque, under that path | the check is committed; the requirement it proxies stays open |
| interactive parser that asks which parse | the grammar | yes; the question concerns the input | symbolic | symbolic | the clarification step is declared |
| prompt whose output is parsed by a schema | the schema, for the output | yes, for the output | symbolic, for the schema | mixed | prompt natural-language unless its model is adopted, output contract symbolic |
| frozen prompt–model package adopted for one operation | the package, decoding included | yes | symbolic under the runtime's path, distributed-parametric under the interpreter's | prompt symbolic, opaque, under that path; weights distributed-parametric under the interpreter's path | codifies the operation; defines nothing about English |

## Decisions and remaining questions

The [question register](./decisions-and-open-questions.md) explains which choices are settled and which concern presentation. Adoption, path-relative localization and the opacity modifier are settled decisions. Testing the boundary cases is a [review check](./decisions-and-open-questions.md#review-checks-not-wording-decisions), not a standing request to decide those points again. The [follow-up list](./follow-up-library-changes.md#promotion-checklist) holds promotion tasks.
