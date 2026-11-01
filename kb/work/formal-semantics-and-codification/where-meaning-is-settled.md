# Where natural-language meaning is settled

Tentative theory, 2026-11-01, revised after [Astra's review](./review-2026-11-01-astra.md). This file is a side result of the [workshop](./README.md): it concerns how English differs from the language a frozen model defines, and it supports one claim of the account, that the frozen-model path of formalization formalizes a different language rather than English, as the second reason beside who is held to what. Nothing in the [account of symbolic form](./codification-as-commitment.md) or the [proposed definitions](./candidate-definitions.md) depends on it. Its claims are weaker than the first draft's, and several are suspended. The [Tarski thread](./tarski-thread.md) and the [evidence ledger](./sources.md) are separate files.

## The claim

Natural language has prior constraints but no designated reference. The constraints are conventions a community holds. They make some readings wrong, whether or not the author is available. No artifact or consumer is authoritative over the conventions: they are a population fact, which [meaning as coordination](../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) states as a hypothesis. When a dispute about a reading arises between parties, it is resolved locally, by repair, and what repair settles is what the parties will take the utterance to mean here, not what it conventionally means.

Three things the first draft ran together must be kept apart: what an expression conventionally means, what its author intended, and what the parties agree to do next. Repair connects them. It does not make them identical. "Meaning is settled by its author on request" was too simple.

## Four features

**Repair.** "I don't understand, explain what you mean" is a channel built into the language, not a failure of it. Conversation analysis treats repair as a structural feature of talk, and two ingested sources in the [evidence ledger](./sources.md) support that. They also limit it: most clarification requests in dialogue concern what was heard or what move was made, and only a minority ask what an expression means. Repair is frequent and structured; it is not shown to be the usual way meaning gets settled. A compiler cannot ask the programmer what they meant, and Turing's clerk follows the rules with no authority to deviate. The [commitment account](./codification-as-commitment.md) states the narrower consequence: codification removes the channel for asking what the artifact means through a step the rules did not declare, while declared clarification steps about inputs remain.

**Dynamism.** "Semantics is not set in stone" is not the contrast, because programming languages also change. What differs is the mechanism. A designated reference changes only by revision under its authority, and consumers between revisions are held to the old one. Natural language changes through use, with no authority, because local repairs and new uses can shift what a community takes a word to mean.

**Redefinition.** Some programming languages let a program redefine parts of the language: Lisp macros, operator overloading, Forth words, Smalltalk's metaclasses. The redefinition is always inside a fixed reference. It is interpreted by the reference as it stood at that moment, there is a definite current definition in force, and the specification that says what a definition does sits outside the language. Natural language goes deeper in three ways. A redefinition need not be declared: "literally" and "awful" changed through use. A redefinition is a proposal, not an act in force: it takes hold through uptake, and competing meanings coexist across speakers at once. The semantic vocabulary is inside the language: "means", "define" and "true" drift like any other word, so there is no fixed kernel in which definitions are stated. Tarski called this semantic closure; the [Tarski thread](./tarski-thread.md) says what that does and does not give.

**Fuzziness.** Vague predicates are settled case by case, and the boundary of the boundary is itself vague. A membership function would be a designated reference, so formalizing vagueness as degrees converts it into the other form. Whether that is why fuzzy semantics did not take hold in linguistics is a historical claim the workshop has not grounded; it is suspended (see the [evidence ledger](./sources.md)).

## Underspecification

The library treats [underspecification](../../theory/agentic-systems-interpret-underspecified-instructions.md), the fact that two readings of an instruction can both be reasonable, as the basic feature agents must cope with. The first draft derived it from repair. That was too strong: missing context and unanticipated cases arise with no expectation of repair. Underspecification has several sources. An author cannot settle what they did not foresee. Drift and redefinition reopen choices the author did settle. Vague predicates leave every boundary open. And because repair is usually available, authors can leave open what repair will settle. Repair explains why underspecification is cheap in ordinary use, not why it exists. The gap becomes consequential when no repair is available, and the commitment account says what follows for an author handing an artifact to a consumer that cannot ask.

The programming-language contrast is that a designated reference declares its gaps in advance, while natural language's gaps are discovered on consumption. This is a claim about what the reference names, not about what a consumer can decide before running a program.

## A conjecture about an LLM as a reference for English

A frozen model designated as a reference for English would be a snapshot of one idiolect with its channel to the community closed. The first draft inferred that English therefore cannot have a reference. Astra's objection stands: variation and change do not establish this, and a model might represent variation, context and change. The conjecture is kept as a conjecture and is not added to the [probe question](./perfect-english-reference-question.md), which already carries the weaker, open form: whether a sufficiently competent model could be designated as a reference for a scoped variety of English.

## Open questions

1. Do the repair sources themselves keep conventional meaning, author intent and local agreement apart, or does the conversation-analysis literature merge them?
2. Does any claim in this file need to be true for the proposed definitions? If one does, it belongs in the commitment account, not here.
