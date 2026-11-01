# Formal semantics and codification

## Goal

Posed by the operator on 2026-10-31 while revising the definition of [codification](../../theory/definitions/codification.md). The goal is revised definitions of codification and [representational form](../../theory/definitions/representational-form.md) that rest on a correct account of what codification commits to. The immediate trigger was the wish to replace Commonplace's special phrase "unique operational semantics" with ordinary vocabulary; the workshop found that the phrase concealed a wrong justification, so the account comes first and the wording follows from it.

The workshop first sought a general account of the difference between natural language and programming languages. [Astra's review](./review-2026-11-01-astra.md) of 2026-11-01 showed that the definitions do not need one and should not be hostage to one. The definitions now rest on an architectural account of a commitment made in a system. The theory of natural language is kept as a side result with weaker claims.

The motivating correction is the operator's construction: a compiler's complete implementation together with a sufficiently specified machine can supply a formal account of its behavior. Two incompatible compilers can each supply such an account while passing the same tests. Therefore agreement on tests must not be presented as establishing the bare existence of a formal account.

## How the parts serve the goal

The argument runs in four steps, with two side results. Each file states at its head which part it serves.

1. **Clear the ground.** [An implementation supplies a formal model, not proof of shared semantics](./implementation-and-shared-semantics.md) shows that formalizability cannot be the difference: any implemented consumer plus a machine model has a formal account of its behavior, for a frozen language model as for a compiler. Tests corroborate conformance to a reference, not formalizability. The current library definitions rest on the opposite assumption. This is the workshop's established result, and it does not depend on anything below.
2. **State the commitment.** [Codification commits an operation to rules a clerk could follow](./codification-as-commitment.md) gives the account the definitions rest on. Its hypothesis, in Astra's words, is that the practical difference is whether an operation has been committed to a delimited interpretation regime or still relies on ordinary linguistic judgment, with "delimited" read as Tarski's exactly specified structure. It separates three questions the current definitions run together: what governs correctness, how content is represented, and how unresolved choices are handled. The criterion has two conjuncts: a designated reference governs, and it settles the relevant choices by rules a consumer forbidden insight could follow. The file carries the boundary-case table, including the cases Astra asked for, and the open questions about the account.
3. **Apply it to the definitions.** [Candidate definitions of codification and representational form](./candidate-definitions.md) gives proposed wording for codification, representational form, constraining and the collision ledger, the migration list for the retired phrase, and the open questions about wording. Its footnote retains the rejected formal-semantics candidates of 2026-10-31 with the reasons.
4. **Probe it.** [Could an LLM with perfect command of English define its semantics?](./perfect-english-reference-question.md) is a self-contained question to copy to other agents. It tests the account at its hardest case. It stays open-ended; no prediction from the side results is added to it.

The Tarski ingest, done 2026-11-01, found that the 1944 paper supplies exactly specified structure and the metalanguage hierarchy, that undefinability of a language's own truth holds for formalized arithmetic too and so does not separate the two kinds of language, while the antinomy hits only semantically closed languages, which formalized ones are not, and that the universality argument is in the 1933 monograph, which is not ingested.

Side results, not load-bearing:

- [Where natural-language meaning is settled](./where-meaning-is-settled.md) is a tentative theory of natural language: conventions nobody is authoritative over, local repair, dynamism, redefinition and fuzziness, with the first draft's stronger claims weakened or suspended. It carries the Tarski thread, the operator's suggestion that exactly specified structure and semantic closure may be the core of the distinction, and the list of sources to ingest.
- [Review by Astra](./review-2026-11-01-astra.md) is retained verbatim. Its points were accepted except one: codification narrows the clarification channel to declared steps about inputs rather than leaving it open, which step 2 states.

## Status

2026-11-01. Step 1 is established. Step 2 was rewritten after Astra's review and has not been reviewed since. Step 3 carries the two-conjunct wording for every affected passage but has not been reviewed against the open questions. Step 4 has been sent to no agent yet. Four of five sources are being ingested; Lakoff 1973 has no accessible copy, so the fuzziness claim stays suspended.

## Boundary

Current write scope is this directory and its entry in the active workshop index. Do not change the library definitions or migrate terminology under this commission. Preserve the operator's distinction between existence of a formal model and corroboration by executors. Do not treat disagreements over which specification is authoritative as an answer to the formalizability question. Keep the side results out of the definitions: a claim the definitions need belongs in step 2.

The [institution-theory workshop](../institution-theory-import/README.md) investigates broader semantic imports and flagged the library's blanket impossibility appeal for a primary-source audit, which the Tarski ingest supplies. The [ideal-interpreter workshop](../ideal-interpreter/README.md) owns the experimental LLM interpreter definition. This argument neither adopts that device nor depends on it.

## Closure

Close when the account in step 2 survives review, including the probe in step 4, and the operator decides whether to promote the wording in step 3. A successful result states the commitment without making every machine-consumed artifact symbolic, identifies what conformance tests corroborate, and supplies wording for the affected definitions. An explicit unresolved boundary or rejection is preferable to a forced replacement.

Promotion requires a separately authorized library revision, including checks of codification, constraining, representational form, and the vocabulary collision ledger. On closure, extract the step 2 account to `kb/theory/`, the wording to the library definitions, the side theory to `kb/theory/proposals/` if it earns a note or the log otherwise, the sources to `kb/sources/` as they are ingested, and remove this workshop and its index entry.
