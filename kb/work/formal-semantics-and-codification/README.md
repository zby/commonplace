# Formal semantics and codification

## Goal

Posed by the operator on 2026-10-31 while revising the definition of [codification](../../theory/definitions/codification.md). The goal is revised definitions of [representational form](../../theory/definitions/representational-form.md) and codification that rest on a correct account of what makes an artifact symbolic. The trigger was the wish to replace the special phrase "unique operational semantics"; the phrase turned out to conceal a wrong justification, so the account comes first and the wording follows from it. The deliverable is the difference between prompts and code.

The operator's decisions, all 2026-11-01, fix the shape of the account:

- Symbolic form is defined first, by the language: a formal semantics or something close to one, where close means the language's users hold its consumers to a reference, a standard or an implementation, from which a formal semantics could be derived. Codification is the move into that form.
- Adopting a frozen prompt–model package is codification. A prompt that works on a frozen, adopted model is code, opaque code that lacks the advantages of ordinary code. This does not define the semantics of English, for two reasons: English's users hold no reader to the package, and formalizing English by any path drops repair, redefinition from inside and change by use, which are features of English and not of C.
- The complexity that drives cost and unreliability in practice is marked by the modifier *opaque* on symbolic form, with three sources: the artifact's scale, the reference's form, and deliberate obfuscation, the last suggested by the operator from the cryptography of program obfuscation. The modifier is written only where readability is at issue. Symbolic does not mean readable, as the library's opacity note already says; the separation is cleaner than the old single phrase, with the awkwardness that legibility coincides with symbolic form only under further conditions.

The hypothesis under test, in [Astra's words](./review-2026-11-01-astra.md#follow-up-comment-prompted-by-the-tarski-thread): the practical difference is not formalizability versus non-formalizability, but whether an operation has been committed to a delimited interpretation regime or still relies on ordinary linguistic judgment to settle what its instructions require.

## How the parts serve the goal

Four steps carry the argument. Each file says at its head which part it serves.

1. **Clear the ground.** [An implementation supplies a formal model, not proof of shared semantics](./implementation-and-shared-semantics.md): formalizability of a consumer cannot be the difference, and tests corroborate conformance, not formalizability. Established; nothing below is needed for it.
2. **State the account.** [Symbolic form is a language close to a formal semantics, and codification is the move into it](./symbolic-form-and-codification.md): the hypothesis, symbolic form with the gloss of "close" and its two conditions, why a formalization of a consumer is not the semantics of the language, codification as the move made by rewriting or by adoption, what a reference leaves open, the opaque modifier with its three sources, unresolved choices as an execution contract, the boundary table, open questions.
3. **Write the definitions.** Complete proposed texts, each ending in its open questions: [representational form](./representational-form-definition.md), where the criterion now sits, and [codification](./codification-definition.md), which points to it.
4. **Probe it.** [Could an LLM with perfect command of English define its semantics?](./perfect-english-reference-question.md): a self-contained question for other agents, kept open-ended. [Astra's answer](./probe-response-2026-11-01-astra.md), verbatim, not yet assessed against steps 2 and 3.

Supporting files:

- [The Tarski thread](./tarski-thread.md). Its settled part, exactly specified structure, gives step 2 the sense of "delimited". Its open part, semantic closure and universality, concerns how English differs from any formalized language, which supports the claim that the frozen-model path does not formalize English; it rests on the 1969 article and an encyclopedia entry standing in for the 1933 monograph. It also holds the audit of the library's impossibility appeal.
- [Evidence ledger](./sources.md). Each commissioned source, the claim it was to support, what it supports, and its limits. Seven sources ingested with quotes.
- [Where natural-language meaning is settled](./where-meaning-is-settled.md). A tentative theory of how English differs from any frozen language, side result; it supports the claim that the frozen-model path does not formalize English, and the definitions do not depend on it.
- [Follow-up library changes](./follow-up-library-changes.md). The migration of the retired phrase, ledger rows, the opacity note's further sources, the impossibility paragraph, links from theory notes. Not authorized here.
- [First review by Astra](./review-2026-11-01-astra.md), verbatim. Accepted except one point: codification narrows the clarification channel to declared steps about inputs rather than leaving it open.
- [Second review by Astra](./review-2026-11-01-astra-second.md), verbatim. All points accepted; the blocking question was resolved by the operator in favor of adoption as codification, with opacity a separate modifier. Its file references name the step 2 file by its earlier name.

## History

Four candidate definitions of 2026-10-31 kept formal semantics as the ground with an "adequate reference interpreter" doing the distinguishing work; they are in commit 9f67de3f1 and were rejected because the constructibility clause is satisfied by every machine-consumed artifact and adequacy is a judgment nobody can run. A "designated reference that a clerk could execute" criterion followed, in commit 99bf794fb, and was replaced on 2026-11-01 by the present wording, which returns to formal semantics as the ground and replaces the adequacy judgment with who is held to the reference. The earlier step 3, a file of wording fragments, was replaced by the two complete definitions.

## Status

2026-11-01. Step 1 established. Step 2 rewritten around the operator's decisions, not reviewed since. Step 3 written as complete definitions, not reviewed. Step 4 sent to Astra, answer recorded, not yet assessed. Seven sources ingested with quotes: two on repair and clarification, three on Tarski and the liar, two on program obfuscation, the last two from substitute copies because the ePrint server refused the downloads. Clark and Brennan deferred, since it supports only the side theory; Lakoff not ingested.

## Boundary

Write scope is this directory and its entry in the active workshop index. Do not change the library definitions or migrate terminology under this commission. Keep the side theory out of the definitions: a claim the definitions need belongs in step 2. The [ideal-interpreter workshop](../ideal-interpreter/README.md) owns the LLM interpreter device; the [institution-theory workshop](../institution-theory-import/README.md) asked for the Tarski audit.

## Closure

Close when step 2 and the two definitions survive review, including the probe, and the operator decides whether to promote them. On closure, extract step 2 to `kb/theory/`, the two definitions to the library with their links repointed, the follow-ups to their targets, the side theory to `kb/theory/proposals/` if it earns a note or the log otherwise, and remove this workshop and its index entry. An explicit unresolved boundary or rejection is preferable to a forced replacement.
