# Formal semantics and codification

## Goal

Posed by the operator on 2026-10-31 while revising the definition of [codification](../../theory/definitions/codification.md). The goal is a better capture of the difference between natural language and programming languages, and from it revised definitions of [representational form](../../theory/definitions/representational-form.md) and codification. The immediate trigger was the wish to replace Commonplace's special phrase "unique operational semantics" with ordinary vocabulary; the workshop found that the phrase concealed a wrong account of the difference, so the account comes first and the wording follows from it.

The motivating correction is the operator's construction: a compiler's complete implementation together with a sufficiently specified machine can supply a formal account of its behavior. Two incompatible compilers can each supply such an account while passing the same tests. Therefore agreement on tests must not be presented as establishing the bare existence of a formal account.

## How the parts serve the goal

The argument runs in four steps. Each file states at its head which step it serves.

1. **Clear the ground.** [An implementation supplies a formal model, not proof of shared semantics](./implementation-and-shared-semantics.md) shows that formalizability cannot be the difference: any implemented consumer plus a machine model has a formal account of its behavior, for a frozen language model as for a compiler. Tests corroborate conformance to a reference, not formalizability. The current library definitions rest on the opposite assumption.
2. **State the difference.** [Natural language and programming languages differ in where meaning is settled](./where-meaning-is-settled.md) gives the replacement account. A programming language has a prior, designated reference that settles what an artifact permits. A natural language is settled by its speakers, on demand, locally, in the same language. Repair, dynamism, redefinition and fuzziness are four faces of that one fact, and underspecification, which the library treats as primitive, is derived from them. The file carries the boundary-case table, the consequences for Commonplace, the sources to ingest and the open questions about the account.
3. **Apply it to the definitions.** [Candidate definitions of codification and representational form](./candidate-definitions.md) gives proposed wording for codification, representational form, constraining and the collision ledger, the migration list for the retired phrase, and the open questions about wording. Its footnote retains the rejected formal-semantics candidates of 2026-10-31 with the reasons.
4. **Probe it.** [Could an LLM with perfect command of English define its semantics?](./perfect-english-reference-question.md) is a self-contained question to copy to other agents. It tests the account at its hardest case: whether a sufficiently competent model could be designated as a reference for English. The account predicts it cannot, for a reason about the kind of the language rather than about competence; the question does not yet put that prediction to the agents.

## Status

2026-11-01. Steps 1 and 2 are drafted and consistent. Step 3 has wording for every affected passage but has not been reviewed against the open questions. Step 4 has been sent to no agent yet, and does not yet carry the step 2 prediction.

## Boundary

Current write scope is this directory and its entry in the active workshop index. Do not change the library definitions or migrate terminology under this commission. Preserve the operator's distinction between existence of a formal model and corroboration by executors. Do not treat disagreements over which specification is authoritative as an answer to the formalizability question.

The [institution-theory workshop](../institution-theory-import/README.md) investigates broader semantic imports. The [ideal-interpreter workshop](../ideal-interpreter/README.md) owns the experimental LLM interpreter definition. This argument neither adopts that device nor depends on it; step 2 sends it one conjecture.

## Closure

Close when the account in step 2 survives review, including the probe in step 4, and the operator decides whether to promote the wording in step 3. A successful result states the difference without making every machine-consumed artifact symbolic, identifies what conformance tests corroborate, and supplies wording for the affected definitions. An explicit unresolved boundary or rejection is preferable to a forced replacement.

Promotion requires a separately authorized library revision, including checks of codification, constraining, representational form, and the vocabulary collision ledger. On closure, extract the step 2 account to `kb/theory/`, the wording to the library definitions, the sources to `kb/sources/` as they are ingested, and remove this workshop and its index entry.
