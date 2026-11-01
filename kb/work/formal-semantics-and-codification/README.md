# Formal semantics and codification

## Goal

Posed by the operator on 2026-10-31 while revising the definition of [codification](../../theory/definitions/codification.md). The goal is revised definitions of codification and [representational form](../../theory/definitions/representational-form.md) that rest on a correct account of what codification commits to. The trigger was the wish to replace the special phrase "unique operational semantics"; the phrase turned out to conceal a wrong justification, so the account comes first and the wording follows from it.

After [Astra's second review](./review-2026-11-01-astra-second.md), the operator resolved its blocking question: adopting a frozen prompt–model package as the reference is codification, and whether the reference can be read is a separate property that sets inspection and revision cost rather than membership. The hypothesis under test, in Astra's words: the practical difference is not formalizability versus non-formalizability, but whether an operation has been committed to a delimited interpretation regime or still relies on ordinary linguistic judgment to settle what its instructions require.

The operator then set the wording, 2026-11-01: the criterion is a formal semantics or something close to one, and the work is in what "close" means. The gloss is that the language's users hold its consumers to a reference, a standard or an implementation, from which a formal semantics could be derived. The gloss has to admit that adopting a frozen package is codification while denying that this defines the semantics of English, and it does so because the two claims are about different languages: the package's formalization is the semantics of the one-user language of prompts as it reads them. The complexity of the frozen package, which drives cost and unreliability in practice, is marked by the modifier *opaque* on symbolic form, with three sources, the artifact's scale, the reference's form and deliberate obfuscation, the last suggested by the operator from the cryptography of program obfuscation; symbolic does not mean readable, as the library's opacity note already says. The modifier is written only where readability is at issue; the operator judged the separation cleaner than the old single phrase, with the awkwardness that legibility coincides with symbolic form only under further conditions.

The deliverable is the difference between prompts and code. Under these definitions a prompt that works on a frozen, adopted model is code, opaque code that lacks the advantages of ordinary code, and a prompt read by whatever model runs is not. How English differs from the language a frozen model defines, in the side theory and in the open half of the Tarski thread, supports the deliverable at one point: it shows that the frozen-model path of formalization formalizes a different language, not English, because English has repair, redefinition from inside and change by use as features of the language, which any formalization drops, while C has none of them, so formalizing C drops nothing. That is the second reason, beside who is held to what, why adopting the package codifies the operation without defining the semantics of English. The order is form first: symbolic form is defined by the language, and codification is the move into it, which is the order the library's form definition already uses.

## How the parts serve the goal

Four steps carry the argument. Each file says at its head which part it serves.

1. **Clear the ground.** [An implementation supplies a formal model, not proof of shared semantics](./implementation-and-shared-semantics.md): formalizability cannot be the difference, and tests corroborate conformance, not formalizability. Established; nothing below is needed for it.
2. **State the commitment.** [Symbolic form is a language close to a formal semantics, and codification is the move into it](./codification-as-commitment.md): the hypothesis, symbolic form with the gloss of "close" and its two conditions, why a formalization of a consumer is not the semantics of the language, codification as the move made by rewriting or by adoption, the three cases of what a reference leaves open, the opaque modifier with its two sources, the handling of unresolved choices as an execution contract, the boundary table, open questions.
3. **Apply it to the definitions.** [Candidate definitions](./candidate-definitions.md): proposed wording for representational form, codification, constraining and the ledger's `operational` row, with the migration list.
4. **Probe it.** [Could an LLM with perfect command of English define its semantics?](./perfect-english-reference-question.md): a self-contained question for other agents, kept open-ended.

Supporting files:

- [The Tarski thread](./tarski-thread.md). Its settled part, exactly specified structure, gives step 2 the sense of "delimited". Its open part, semantic closure and universality, concerns how English differs from any formalized language, which supports the claim that the frozen-model path does not formalize English; it rests on the 1969 article and an encyclopedia entry standing in for the 1933 monograph. It also holds the audit of the library's impossibility appeal.
- [Evidence ledger](./sources.md). Each commissioned source, the claim it was to support, what it supports, and its limits.
- [Where natural-language meaning is settled](./where-meaning-is-settled.md). A tentative theory of how English differs from any frozen language, side result; it supports the claim that the frozen-model path does not formalize English, and the definitions do not depend on it.
- [Follow-up library changes](./follow-up-library-changes.md). Ledger rows, the impossibility paragraph, links from theory notes. Not authorized here.
- [First review by Astra](./review-2026-11-01-astra.md), verbatim. Accepted except one point: codification narrows the clarification channel to declared steps about inputs rather than leaving it open.
- [Second review by Astra](./review-2026-11-01-astra-second.md), verbatim. All points accepted; the blocking question was resolved by the operator in favor of adoption as codification, with opacity a separate modifier.

## Status

2026-11-01. Step 1 established. Step 2 rewritten around the operator's "close to a formal semantics" wording with symbolic form defined first, not reviewed since. Step 3 carries that wording, order and the opaque modifier, not reviewed against the open questions. Step 4 sent to no agent. Five sources ingested, Tarski's 1969 article and an encyclopedia entry on the liar standing in for the 1933 monograph; Clark and Brennan deferred, since it supports only the side theory; Lakoff not ingested.

## Boundary

Write scope is this directory and its entry in the active workshop index. Do not change the library definitions or migrate terminology under this commission. Keep the side theory out of the definitions: a claim the definitions need belongs in step 2. The [ideal-interpreter workshop](../ideal-interpreter/README.md) owns the LLM interpreter device; the [institution-theory workshop](../institution-theory-import/README.md) asked for the Tarski audit.

## Closure

Close when step 2 survives review, including the probe, and the operator decides whether to promote step 3. On closure, extract step 2 to `kb/theory/`, the wording to the library definitions, the follow-ups to their targets, the side theory to `kb/theory/proposals/` if it earns a note or the log otherwise, and remove this workshop and its index entry. An explicit unresolved boundary or rejection is preferable to a forced replacement.
