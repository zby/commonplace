---
description: "Explains why adopting a pinned model can codify a prompt without formalizing English, and separates reference conformance, permitted variation, opacity, and requirement adequacy."
type: types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, artifact-analysis]
---

# Symbolic form holds consumers to a semantic reference

An artifact is symbolic under a consumption path when its content is localized in identifiable units and its consequences under that path are fixed by the reference of a language that has a formal semantics or is close to one. A language is close to a formal semantics when its users hold its consumers to a reference, a standard or an implementation, from which a formal semantics could be derived. [Representational form](./definitions/representational-form.md) classifies how content is encoded and consumed; [codification](./definitions/codification.md) is the move of a rule or operation from natural-language form into symbolic form. Whether the artifact and its reference let its behavior be read is a different property, marked by the modifier *opaque*, which does not change membership.

The difference between prompts and code is this: a prompt under a frozen model adopted as the reference for an operation is code under this account. It is opaque code that keeps what membership gives and loses what reading gives. A prompt read by whatever model runs is not code under this account. This is an architectural account of artifacts and of a move a system makes, not a theory of language. The classification does not depend on an explanation of how repair, redefinition and change through use maintain linguistic conventions.

## Four separate questions

1. **How content is represented.** Whether an identifiable unit carries the content, and whether its consequences are fixed by a reference or reinterpreted on each consumption.
2. **What governs correctness.** Which reference the language's users hold consumers to.
3. **Whether the reference can be read.** Whether the rule that assigns a consequence can be pointed at, read, and revised separately, and at what cost.
4. **How unresolved choices are handled.** What happens when the rules do not settle a case.

## The hypothesis

This account's hypothesis is that the practical difference is not formalizability versus non-formalizability. It is whether the operation has been committed to a delimited interpretation regime, or still relies on ordinary linguistic judgment to settle what its instructions require.

The hypothesis concerns the move, codification. What the move produces is an artifact in symbolic form, defined next. Whether the result is opaque is a separate question. The gloss of "close to a formal semantics" fixes the hypothesis's three terms: *committed* is the holding of consumers to a reference, *delimited* is what derivability tests for, and *ordinary linguistic judgment* is what derivability excludes.

## Symbolic form

Content is symbolic under a consumption path when it sits in localized units whose consequences under that path are fixed by the reference of a language that has a formal semantics or is close to one. A language is close to a formal semantics when its users hold its consumers to a reference, a standard or an implementation, from which a formal semantics could be derived. The reference may leave permitted variation, external inputs, excluded guarantees and declared clarification steps.

Two conditions are needed.

### The language's users hold consumers to a reference

A consumer held to the reference that departs from it is wrong. For C the reference is the standard; for Python it is the language reference together with CPython, so a CPython deviation from the language reference is a bug and a third-party interpreter that departs from both is wrong. Holding consumers to a reference is a convention of the language's users, so a project inherits it with the language; it does not have to adopt CPython for its scripts to count.

A system creates such a language only when it adopts a consumer as the reference: adopting a frozen prompt–model package for one operation makes the system the sole user of the language of prompts as that package reads them, and it holds the only consumer to the package. [Which reference governs decides what counts as a violation, not whether behavior can be formally described](./implementations-do-not-establish-shared-semantics.md).

The reference is external in its governing role; it need not be written in a different language from the artifact. An operation is interpreted relative to its governing rules, and the language's ability to describe or execute those rules does not remove the need to specify their interpretation.

### A formal semantics could be derived from the reference

[An implementation together with a machine model determines a formal account of execution](./implementations-do-not-establish-shared-semantics.md). A standard whose structure is exactly specified in the sense of Tarski's [1944 paper](../sources/tarski-semantic-conception-of-truth.ingest.md)—which expressions count, which terms are undefined, the rules of definition, which expressions are sentences, and under what conditions a sentence is asserted—supplies the material for one. Extending "asserted" to "an action permitted" is this account's adaptation, not Tarski's.

The clerk explains why derivation is possible. In [Copeland's account of the Church–Turing thesis](../sources/church-turing-thesis-sep.ingest.md), Turing's machines idealize human numerical computation, and an effective method consists of exact instructions carried out without insight. The account here uses that mechanical-procedure intuition: a human following a formal procedure is the clerk. The clerk is the explanation, not the definition.

The condition asks that each step of applying the reference be mechanically checkable. It does not ask that every consequence of the reference be decidable, which is stronger and often false.

Designating a judge does not supply a rule, so a reference that settles by unformalized judgment about what was intended, a contract's arbitrator or a workflow's human judge of "sufficient evidence", governs without making the artifact symbolic. The exclusion is the unformalized judgment, not the human. A protocol that takes a human decision as an input is the required external selection treated below: it formalizes the step without formalizing the judgment. The hypothesis's ordinary linguistic judgment is judgment by whoever reads, under conventions that no held-to reference fixes.

### Three grades and consumption paths

The account distinguishes three grades by the reference users accept. In the first, users accept a written formal semantics: Standard ML, WebAssembly. In the second, they rely on a standard or implementation from which a formal semantics could be derived: the C standard, Python's language reference and CPython, a legacy codebase's interpreter, or a schema's validator. This describes the governing reference, not the absence of research formalizations. In the third, formalizations of consumers exist but none governs the language's users: English. The symbolic membership criterion groups the first two grades together.

Form is relative to the consumption path. Under a path with no held-to reference, the same artifact is reinterpreted on each consumption and is natural-language under that path. Mixed artifacts are split by operative part or consumption path, as the form definition allows.

## A formalization of a consumer is not the semantics of the language

A frozen language model is as formalizable as a compiler under the supplied machine assumptions. The formalization describes the consumer. It is the semantics of a language only when that language's users hold consumers to it. C's users hold every compiler to the standard, so a formalization derived from the standard is a formalization of C. A formalization derived from GCC describes GCC. Which of GCC's behaviors are C's is settled against the standard, and telling the bugs apart already requires it.

English's users hold no reader to the frozen model, so a reader that departs from it is not thereby wrong. A descriptive formalization of English answers to linguistic practice; formalizing the model does not make that model authoritative over the practice.

Change by use does not block a formal account of English in principle. A fixed update rule fed with new evidence is a fixed formal specification that tracks a changing practice, and a model with context can handle repair and redefinition within a conversation. Formalizing a model does not by itself make its behavior authoritative for English. Adopting the model for an operation establishes that authority within the adopting system, not for English's users generally.

A designated language reference changes through revision under its authority, and consumers between revisions are held to the reference in force. The asymmetry is in which side answers to which. A community that came to hold its readers to a model would have made a scoped language that is symbolic under the criterion; it would not have made the model the semantics of English.

A system that adopts the package for an operation creates a language of one user, prompts as this package reads them, and the package's formalization is that language's semantics. So the prompt is symbolic under that path, and the semantics of English is untouched. The two claims are about different languages.

Adopting the package does not, by that act alone, establish it as an adequate semantics of English: a descriptive account of English answers to the practice, and the adoption answers to the system. Tarski's remark that formalized languages of interest are fragments of natural languages provided with complete vocabularies and precise syntactical rules, or languages adequately translatable into natural languages ([Truth and Proof](../sources/tarski-truth-and-proof.ingest.md)), provides an analogy for the scoped language adoption creates. The application to adoption is this account's, not Tarski's. It is not a proof that English could not be described, and this account makes no such claim.

Merely requiring a procedure for formalizing a consumer fails as the criterion: every sufficiently specified implemented consumer has one. What picks out the language's governing semantics among consumer formalizations is who is held to which.

## Codification is the move into symbolic form

A system codifies a rule or operation stated in natural language when it moves the artifact that carries it into symbolic form under the consumption path the system uses. The consumer changes from one who reinterprets the text on each use to one bound by the reference, so what the artifact permits no longer depends on who reads it. The adequacy of the symbolic artifact to the original requirement remains a separate question.

The move is made in one of two ways. The ordinary way rewrites the artifact in a language close to a formal semantics: prose becomes code, a schema, a route table. The other way leaves the text alone and changes the consumption path: the system adopts a consumer, a pinned prompt–model package with its decoding procedure, as the reference for the operation. The text of the prompt does not change; its form under that path does, because the system has created a one-user language whose reference it holds the consumer to. This is a test case for the definition rather than an exception to it. The same prompt read by whatever model a session happens to run stays natural-language, because nothing fixes its consequences.

The weights have two consumption paths, and localization is relative to the path as form is. Under the runtime's path each kernel and parameter is an addressed unit whose consequences the pinned runtime fixes, so the weights are symbolic there, and opaque by scale. Under the path on which the whole model is run as the interpreter, nothing in them is addressed as a separate instruction-level commitment, so they are distributed-parametric there, and adoption does not change that. The [form definition](./definitions/representational-form.md) states the rule in its derivation.

Repeatability is not adoption: repeatability alone does not make the prompt symbolic; adoption does. Pinning a model version and adopting its behavior as the reference codifies the instructions it reads. It is an opaque codification, which loses the advantages that reading gives, not its membership. The adoption must include the decoding procedure, or model the output distribution as permitted variation.

## What the reference leaves open

Four cases must be distinguished:

- **Permitted variation.** The rules settle the allowed alternatives. "Return either A or B" completely specifies the permitted behavior; different permitted outputs are not disagreement about what is permitted, as [the distinction between agreement and conformance](./implementations-do-not-establish-shared-semantics.md) explains.
- **Required external selection.** An input or an implementation parameter supplies the choice, and the reference says so.
- **An excluded guarantee.** The reference states in advance that it requires nothing for a case. This declared absence of any requirement completely specifies that no behavior is guaranteed. It is not a failure of the reference.
- **A defect in the reference.** The rules fail to settle what they were supposed to settle: an accidental ambiguity in a standard, or a case nobody foresaw. This is an undeclared absence, discovered on use, and it is the only one of the four that is a failure of the reference.

The [C11 committee draft N1570, §§3.4.1–3.4.4](../sources/wg14-n1570-behavior-definitions.ingest.md), supplies examples of the first three cases. Its unspecified behavior permits alternatives without further requirements on which is chosen in an instance. Implementation-defined behavior adds the requirement that each implementation document how the choice is made. Undefined behavior carries no requirements from that standard. The fourth case, a defect in the reference, is this account's distinction, not a fourth behavior category defined in those sections; §3.4.2 defines locale-specific behavior.

Whether a particular program reaches an open case can be undecidable, so these are claims about what the reference says, not about what a consumer can decide before running.

## Opaque symbolic form

Adoption fixes which behavior counts as conforming. It does not make that behavior easy to understand, predict, revise or justify against the requirement. Symbolic content is **opaque** under a consumption path, relative to a behavior or change of interest, when the artifact together with its reference does not let an inspector establish that behavior, or the effect of that change, at acceptable cost. Opacity is an inspection property, not a fourth form.

A large codebase can be opaque through scale. A one-line prompt under an adopted model package can be opaque because the reference's numerical operations do not expose the instruction-level rule the inspector needs. Deliberate obfuscation can also obstruct inspection. The [opacity note](./opacity-depends-on-the-inspection-question-and-budget.md) develops these mechanisms, their evidence, and the gap between the path on which a reference is readable and the path on which a question is asked.

Three questions stay apart:

1. Whether execution conformed to the reference.
2. What behavior the reference specifies, including variation and failure outputs.
3. Whether that behavior satisfies the requirement.

Opacity removes an affordable inspection route for the question at hand; evaluation then relies more on execution, other analysis such as abstraction or certificates, or explicitly retained uncertainty. None is a guaranteed substitute for understanding. For an adopted package, repair can mean editing the prompt or swapping the reference rather than locating and revising an instruction-level rule within it.

The adoption declares what the package specifies: the decoding procedure, the output distribution as permitted variation, and any error, refusal or clarification output the package produces. Execution either conforms to it or does not. A frozen package settles every input, so what is found on use is whether the specified behavior satisfies the requirement. An adopted package that always returns a wrong summary for one input executes exactly and fails the summarization requirement. That is an inadequacy, not a newly discovered gap in the reference.

What membership gives remains: what counts as nonconformance is fixed, and the operation is testable against a reference. It is repeatable where the decoding procedure is deterministic and varies within the declared distribution where it is not. Readability determines the cost of finding out what the reference specifies and whether that behavior satisfies the requirement; membership alone supplies no affordable route to those answers.

Write the modifier where readability is at issue. Unmodified "symbolic" says that what counts as wrong against the reference is fixed; it says nothing about whether the reference can be read.

## Unresolved choices are handled differently on each side

The claim here is an execution-contract claim. Execution follows declared transitions, and changes to the governing rules happen through a separately authorized process. A consumer of a symbolic artifact handles an unresolved choice only through a step the rules declare: an error, a declared default, an Ambiguous result, or a question to the user about the *input*. An interactive parser that offers two parses is asking which reading of the input sentence was intended. It is not asking its author what the grammar means. What codification removes is the channel for asking what the artifact itself means through a step the rules did not declare. Interactions the rules provide for remain, and they are declared in advance.

A consumer of natural language can ask the author what the artifact means, and in ordinary use does. When it cannot, because the author is unavailable or the run is noninteractive, it must either leave the readings open or choose, and the choice is its own. This is one application of the advice to [fix what the executor cannot determine](./fix-what-the-executor-cant-determine-not-what-it-will.md): a consequential choice that neither inherited rules nor authorized execution evidence can settle must be fixed before handoff. It is also one reason [progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md): the move removes the channel for asking what the rule means, so the rule must already be right. The availability of an undeclared channel is a symptom of the natural-language side, not a standalone test of form.

## Boundary cases

| Artifact | Held-to reference | Semantics derivable | Reference form | Form under that path | Note |
|---|---|---|---|---|---|
| Python script | the language reference and CPython at a version | yes | symbolic | symbolic | inherited with the language |
| policy clause read by whoever handles the case | none that fixes permitted behavior | no | — | natural-language | localized, but reasonable readings can differ |
| schema enum | the validator | yes | symbolic | symbolic | only for the fields the validator reads |
| tensor operand under the runtime's path | the pinned runtime | yes | symbolic | symbolic | an addressed numerical unit; no instruction-level rule is thereby exposed |
| route table | the resolver | yes | symbolic | symbolic | the operative part the resolver reads |
| regular expression | the engine | yes | symbolic | symbolic | the engine's dialect is part of the reference |
| test suite | the runner and the code under test | yes | symbolic | symbolic | what it checks is a proxy for the requirement |
| large legacy codebase | its interpreter or compiler | yes | symbolic | symbolic, opaque | opacity from the artifact's scale |
| YAML frontmatter on a skill | the loader, for declared fields | yes, for those fields | symbolic | mixed | the instructions stay natural-language |
| prose instruction read by whatever model runs | none | — | — | natural-language | nothing fixes its consequences |
| the same instruction under a pinned, adopted model | the pinned package | yes | symbolic under the runtime's path, distributed-parametric under the interpreter's | symbolic, opaque, under that path | opacity from the reference's form; revised through the prompt |
| ambiguous passage in a language standard | the standard | no, at that passage | symbolic | defect in a symbolic reference | governs without settling |
| declared case with no behavioral guarantee | the reference declaring the exclusion | yes | symbolic | symbolic | an excluded guarantee, declared in advance; not a defect |
| compiled program behind an API, from the caller | the API contract | yes | symbolic | symbolic, for the request | the program's internals are not under the caller's path |
| neural model behind the same API, from the caller | the API contract | yes | symbolic | symbolic, for the request | identical to the compiled program under this path; the two differ under the paths inside |
| contract clause with a designated arbitrator | the arbitrator | no | — | natural-language | held to unformalized judgment |
| workflow step judged by a human | the human | no | — | natural-language | held to unformalized judgment |
| workflow step that waits for a human approval input | the workflow engine | yes; the decision is an input | symbolic | symbolic | the human decision is a required external selection, not the rule |
| LLM-based validator adopted as the reference for a check | the frozen package | yes | symbolic under the runtime's path, distributed-parametric under the interpreter's | symbolic, opaque, under that path | the check is committed; the requirement it proxies stays open |
| interactive parser that asks which parse | the grammar | yes; the question concerns the input | symbolic | symbolic | the clarification step is declared |
| prompt whose output is parsed by a schema | the schema, for the output | yes, for the output | symbolic, for the schema | mixed | prompt natural-language unless its model is adopted, output contract symbolic |
| frozen prompt–model package adopted for one operation | the package, decoding included | yes | symbolic under the runtime's path, distributed-parametric under the interpreter's | prompt symbolic, opaque, under that path; weights distributed-parametric under the interpreter's path | codifies the operation; defines nothing about English |

## Scope

The account classifies an artifact under a named consumption path. It does not establish a reference's adequacy to a requirement, a model's fidelity to scoped English, or physical execution's fidelity to a supplied machine model. Declared variation is compatible with symbolic membership; different permitted results need not be semantic disagreement. Natural-language interpretation can still violate an unambiguous instruction, as [underspecification differs from execution indeterminism](./agentic-systems-interpret-underspecified-instructions.md).

The three grades explain the membership boundary; they are not three additional representational forms. Localization is checked before assigned consequences. Where instruction-level content is distributed across numerical state with no separately addressed units, adoption does not make those weights localized under the interpreter's path.

Semantic closure and universality are not premises of this classification. Whether they distinguish English from formalized languages remains outside the account. Tarski's [1944 discussion](../sources/tarski-semantic-conception-of-truth.ingest.md) says the consistency question has no exact meaning for everyday language and offers only a guess about an exactly specified language resembling it. His truth-predicate restrictions do not establish a prohibition on executing instructions. This account makes no impossibility claim about a formal description of English.

---

Relevant Notes:

- [Representational form](./definitions/representational-form.md) — defined-in: the membership criterion, path-relative localization, and opaque modifier
- [Codification](./definitions/codification.md) — defined-in: the move into symbolic form by rewriting or adoption
- [Implementations do not establish shared semantics](./implementations-do-not-establish-shared-semantics.md) — grounds: formalizing a consumer supplies a model of execution, not authority or conformance to a language
- [Opacity depends on the inspection question and budget](./opacity-depends-on-the-inspection-question-and-budget.md) — extends: separates membership from affordable inspection and develops the three opacity mechanisms
- [Agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — grounds: multiple reasonable readings differ from execution variation or instruction violation
- [An author should fix what the executor can't determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md) — grounds: choices unavailable to authorized execution must be settled before handoff
- [Progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md) — extends: observation precedes committing a reading to a reference
