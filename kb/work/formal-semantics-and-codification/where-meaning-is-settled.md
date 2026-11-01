# Natural language and programming languages differ in where meaning is settled

Workshop draft, 2026-11-01. This file is step 2 of the [workshop](./README.md): it states the difference that the [reductions](./implementation-and-shared-semantics.md) cleared the ground for and that the [proposed definitions](./candidate-definitions.md) apply.

## The claim

The difference between a programming language and a natural language is not that one has a formal semantics and the other lacks one. Any implemented consumer together with a machine model has a formal account of its behavior, and that holds for a frozen language model as much as for a compiler. The difference is where meaning is settled. A programming language has a prior, designated reference that settles what an artifact permits before any consumer reads it. A natural language is settled by its speakers, on demand, locally, in the same language.

## The criterion

The criterion is constitutive, not formal:

> An artifact is **symbolic** when a designated reference settles what it permits. The artifact's language means what that reference says it means, so a consumer that departs from the reference is wrong. An artifact is **natural-language** when no prior reference constitutes its meaning. Its meaning is settled by its author or by speakers on request, in the same language, so two consumers can read it differently without either being wrong, and a consumer that cannot ask must leave the readings open.

The designated reference is an implementation, a specification, or a specification plus implementation parameters. For CPython and a script, the implementation constitutes the language. For a schema and a validator, the validator constitutes what the fields permit. For a route table and a resolver, the resolver constitutes the table's format. In each case the question "what does this artifact permit" has an adjudicator.

English has no prior adjudicator. Its adjudicator is the speaker, reachable only by asking, and the answer is more English. A model reading a prompt does not constitute what the prompt means. A second model reading it differently is not thereby wrong. This is the same point the current definitions make with "consumers held to one reference" and with the misuse case about repeatability. This account states it directly and drops the formal-semantics decoration around it.

Three consequences:

1. **Tests change role.** Independent implementations and conformance tests corroborate that a consumer conforms to the reference. They say nothing about formalizability, and never did. Agreement remains insufficient: consumers can share a bug and a suite can miss it.
2. **The clerk test stays.** A rule is a candidate for codification when a consumer forbidden insight could follow it ([Church–Turing](../../sources/church-turing-thesis-sep.ingest.md)). The test concerns the rules the artifact states, not the consumer's machinery, so the observation that a model's computation is also mechanical does not touch it.
3. **The proxy-versus-requirement split stays.** A designated reference fixes what the artifact permits. Whether that is the right operation for the task remains open ([fixed artifacts split into exact specs and proxy theories](../../theory/exact-implementation-does-not-validate-a-requirement.md)).

## Four faces of settlement by speakers

Natural language has an adjudicator: the speaker. What it lacks is a *prior* reference. The settlement happens on demand, locally, and in the same language. Four features of natural language that each look like an objection to the criterion are faces of this one fact.

**Repair.** "I don't understand, explain what you mean" is a channel built into the language, not a failure of it. A compiler cannot ask the programmer what they meant. Turing's clerk follows the rules with no authority to deviate, and asking would be a deviation. If a designated reference leaves a case unsettled, the consumer cannot repair it at consumption time; it is a gap until the reference's authority revises it. A speaker settles on request, and the settlement binds only that exchange.

**Dynamism.** "Semantics is not set in stone" is not the contrast, because programming languages also change. What differs is the mechanism. A designated reference changes only by revision under its authority, and consumers between revisions are held to the old one. Natural language changes through use, with no authority, because every local repair can shift what a community takes a word to mean. Dynamism is what settlement by speakers looks like over time.

**Redefinition.** Some programming languages let a program redefine parts of the language: Lisp macros, operator overloading, Forth words, Smalltalk's metaclasses. The redefinition is always inside a fixed reference. It is interpreted by the reference as it stood at that moment, there is a definite current definition in force, and the specification that says what a definition does sits outside the language. Natural language goes deeper in three ways. A redefinition need not be declared: "literally" and "awful" changed through use. A redefinition is a proposal, not an act in force: it takes hold through uptake, competing meanings coexist across speakers at once, and the language's state is a population fact, not a single state ([meaning as coordination](../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) states this as a hypothesis). The semantic vocabulary is inside the language: "means", "define" and "true" drift like any other word, so there is no fixed kernel in which definitions are stated. Tarski called this semantic closure.

**Fuzziness.** Fuzzy logic and its application to hedges tried to capture vagueness with degrees of membership. It took hold in control engineering and not in linguistics. The criterion explains why. A membership function is a designated reference; it makes "tall" symbolic. Speakers reject that because the function is arbitrary at every point and because vagueness reappears one level up: the boundary of the fuzzy boundary is itself vague. Fuzzy logic worked where an engineer could stipulate the function and be the reference. It failed where speakers settle the word case by case through context and repair. Formalizing vagueness as degrees converts it into the other form; it does not describe it.

## Underspecification is a consequence, not a primitive

The library treats [underspecification](../../theory/agentic-systems-interpret-underspecified-instructions.md), the fact that two readings of an instruction can both be reasonable, as the basic feature of natural language that agents must cope with. Under this account it is derived. Three of the faces above produce it:

- **Repair lets authors leave choices open.** Because the author can be asked, an utterance never has to settle everything in advance. Authors specify to the level that the expected repair channel makes sufficient. Specification in natural language is always relative to a repair channel.
- **Dynamism and redefinition open choices the author did settle.** Even a text that was fully specific for its author at writing time is read later, by consumers whose meanings have drifted. The readings available at consumption time need not be the readings the author had.
- **Fuzziness leaves every boundary open by design.** A predicate that speakers settle case by case is unsettled at its boundary in every instruction that uses it.

Underspecification is therefore not a property of a text. It is the gap between what an utterance settled and what its consumer needs settled, and in ordinary use repair closes it. The gap becomes visible as "two reasonable readings and no one to adjudicate" exactly when the consumer cannot ask: an agent in a noninteractive run, or a codified consumer. That is why the library's advice is to [fix what the executor cannot determine](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md): the author must pre-settle whatever the missing repair channel would have settled.

The programming-language contrast is sharp here. A designated reference can also leave things unsettled, but it declares them: C's undefined, unspecified and implementation-defined behavior are gaps the reference names in advance. Natural language's gaps are not declared; they are discovered on consumption. A consumer of a programming language can know before reading whether a case is settled. A consumer of natural language finds out when its reading is challenged or when it has no one to ask.

## Consequences for Commonplace

1. **Codification closes the repair channel.** Once a rule is codified, its consumer cannot ask. Every ambiguity must have been settled in advance or it becomes a gap. This supplies the mechanism for two claims the library holds without one: [progressive constraining commits only after patterns stabilize](../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md), and [an author should fix what the executor cannot determine](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md).
2. **An agent reading natural language inherits the repair channel.** The ambiguity exception in the [standalone question](./perfect-english-reference-question.md) is this channel made explicit. The delegation rule in `AGENTS.md`, to return or escalate a gap, is the same mechanism as policy. A diagnostic follows: if the consumer can legitimately ask the author what the artifact *means*, the artifact is natural-language.
3. **Meaning repair stays separate from requirement repair.** A consumer can also ask whether a schema is the right schema. That question is about the requirement, is available in both forms, and is the proxy-versus-requirement split again. Only "what does this mean" marks the form.

## Boundary cases

| Artifact | Designated reference | Form | Note |
|---|---|---|---|
| Python script | CPython at a version | symbolic | the implementation constitutes the language |
| schema enum | the validator | symbolic | the validator constitutes what the field permits |
| route table | the resolver | symbolic | only the operative part the resolver reads |
| YAML frontmatter on a skill | the loader, for declared fields | mixed | declared fields symbolic, instructions natural-language |
| prose instruction run by a model | none | natural-language | the model reads English; it does not constitute it |
| exact numerical claim in prose | none | natural-language | needs symbolic form only when acceptance must be mechanical |
| frozen prompt–model package used as a reference for one operation | the package, for the operation | split | designation closes the repair channel for the operation, so the packaged operation is symbolic; the prompt text stays natural-language, because another model reading it differently is not wrong |

The last row is the boundary the reductions note left open. The criterion resolves it by splitting on consumption path, which [representational form](../../theory/definitions/representational-form.md) already allows for mixed artifacts. Whether such a package would be a *good* reference for the English in its prompt is a different question, taken up below.

## What this does to the question of an LLM as a reference for English

A frozen model designated as a reference for English would be a snapshot of one idiolect with its repair channel closed. It would fail as a reference not because its competence is too low but because English is not the kind of thing that has a state for a reference to capture. This is a conjecture about the kind of the language, not about models, and it is stronger than the adequacy objection recorded with the [rejected candidates](./candidate-definitions.md). The standalone question should put it to other agents.

The weaker form of the question remains open. Whether a sufficiently competent model could reasonably be designated as a reference for a scoped variety of English is a research question about language fidelity, not a classification criterion. It is graded, currently unassessable, and would make every classification depend on an evaluation nobody can run. The [standalone question for other agents](./perfect-english-reference-question.md) retains it, and the [ideal-interpreter workshop](../ideal-interpreter/README.md) owns the interpreter device.

**Semantic expansion** is a separate question. "Return an integer greater than 10" permits several answers without disagreement about which integers qualify. A different case arises when interpreters disagree about what is permitted and the semantics is revised to settle it, then meets a further disagreement, indefinitely. That no stage is final does not establish that no fixed account of the sequence exists. No impossibility result about natural-language semantics is assumed by this account, and none is needed: the account does not claim that English lacks a formal semantics, only that English lacks a designated reference.

## Sources to ingest

Each would support one claim, named here, and none is grounded yet:

- Schegloff, Jefferson and Sacks, "The preference for self-correction in the organization of repair in conversation" (1977): repair is a structural feature of conversation, not a failure mode.
- Ginzburg, *The Interactive Stance* (2012): clarification requests are a core phenomenon that a semantics of natural language must account for.
- Tarski, "The concept of truth in formalized languages" (1933/1956): semantic closure, the result that colloquial language contains its own semantic predicates; the assumptions under which this blocks a consistent truth definition must be stated when invoked.
- Lakoff, "Hedges: a study in meaning criteria and the logic of fuzzy concepts" (1973): the attempt to give natural-language vagueness a fuzzy-logic reference, and its failure to take hold.
- Clark, *Using Language* (1996): grounding, the joint establishment of what was meant, as part of language use.

## Open questions about the account

1. Does "designated reference" need a definition of its own, or does the gloss in the criterion paragraph suffice? The main risk is a reader taking any machine consumer to be a designated reference, which would collapse the distinction again.
2. Does the boundary table survive a reviewer adding cases? Candidates: a regular expression, a Markdown table consumed only by readers, a test suite, a prompt whose output is parsed by a schema.
3. Does the "can the consumer ask the author what it means" diagnostic hold against the boundary table, including a schema whose author is available to ask?
