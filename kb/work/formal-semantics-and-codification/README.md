# Formal semantics and codification

## Goal

Posed by the operator on 2026-10-31 while revising the definition of [codification](../../theory/definitions/codification.md). The goal is revised definitions of codification and [representational form](../../theory/definitions/representational-form.md) that rest on a correct account of what codification commits to. The trigger was the wish to replace the special phrase "unique operational semantics"; the phrase turned out to conceal a wrong justification, so the account comes first and the wording follows from it.

The hypothesis under test, in Astra's words: the practical difference is not formalizability versus non-formalizability, but whether an operation has been committed to a delimited interpretation regime or still relies on ordinary linguistic judgment to settle what its instructions require.

## How the parts serve the goal

Four steps carry the argument. Each file says at its head which part it serves.

1. **Clear the ground.** [An implementation supplies a formal model, not proof of shared semantics](./implementation-and-shared-semantics.md): formalizability cannot be the difference, and tests corroborate conformance, not formalizability. Established; nothing below is needed for it.
2. **State the commitment.** [Codification commits an operation to rules a clerk could follow](./codification-as-commitment.md): the hypothesis, the two-conjunct criterion, commitment separated from representational form and from the handling of unresolved choices, the boundary table, open questions.
3. **Apply it to the definitions.** [Candidate definitions](./candidate-definitions.md): proposed wording for codification, representational form, constraining and the ledger's `operational` row, with the migration list.
4. **Probe it.** [Could an LLM with perfect command of English define its semantics?](./perfect-english-reference-question.md): a self-contained question for other agents, kept open-ended.

Supporting files:

- [The Tarski thread](./tarski-thread.md). Its settled part, exactly specified structure, gives step 2 the sense of "delimited". Its open part, semantic closure and universality, waits on the 1933 monograph. It also holds the audit of the library's impossibility appeal.
- [Evidence ledger](./sources.md). Each commissioned source, the claim it was to support, what it supports, and its limits.
- [Where natural-language meaning is settled](./where-meaning-is-settled.md). A tentative theory of natural language, side result, not load-bearing.
- [Follow-up library changes](./follow-up-library-changes.md). Ledger rows, the impossibility paragraph, links from theory notes. Not authorized here.
- [Review by Astra](./review-2026-11-01-astra.md), verbatim. Accepted except one point: codification narrows the clarification channel to declared steps about inputs rather than leaving it open.

## Status

2026-11-01. Step 1 established. Step 2 rewritten after Astra's review, not reviewed since. Step 3 carries the two-conjunct wording, not reviewed against the open questions. Step 4 sent to no agent. Five sources ingested, Tarski's 1969 article and an encyclopedia entry on the liar standing in for the 1933 monograph; Clark and Brennan deferred, since it supports only the side theory; Lakoff not ingested.

## Boundary

Write scope is this directory and its entry in the active workshop index. Do not change the library definitions or migrate terminology under this commission. Keep the side theory out of the definitions: a claim the definitions need belongs in step 2. The [ideal-interpreter workshop](../ideal-interpreter/README.md) owns the LLM interpreter device; the [institution-theory workshop](../institution-theory-import/README.md) asked for the Tarski audit.

## Closure

Close when step 2 survives review, including the probe, and the operator decides whether to promote step 3. On closure, extract step 2 to `kb/theory/`, the wording to the library definitions, the follow-ups to their targets, the side theory to `kb/theory/proposals/` if it earns a note or the log otherwise, and remove this workshop and its index entry. An explicit unresolved boundary or rejection is preferable to a forced replacement.
