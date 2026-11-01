# Formal semantics and codification

## Commission

Posed by the operator on 2026-10-31 while revising the definition of [codification](../../theory/definitions/codification.md). The operator wants a note that works through the reductions behind replacing Commonplace's special phrase “unique operational semantics” with ordinary formal-semantics vocabulary. Write in the workshop first; the replacement definition is not yet adopted.

The motivating correction is the operator's construction: a compiler's complete implementation together with a sufficiently specified machine can supply a formal account of its behavior. Two incompatible compilers can each supply such an account while passing the same tests. Therefore, agreement on tests must not be presented as establishing the bare existence of a formal account.

## Working artifacts

- [An implementation supplies a formal model, not proof of shared semantics](./implementation-and-shared-semantics.md) retains the initial reductions, their assumptions, and the remaining boundary question.
- [Candidate definitions for codification and symbolic form](./candidate-definitions.md) holds the current candidate: a constitutive criterion under which an artifact is symbolic when a designated reference settles what it permits, with proposed wording for the affected library passages and a boundary-case table. The earlier formal-semantics candidates are retained in its footnote with the reasons for their rejection.
- [Could an LLM with perfect command of English define its semantics?](./perfect-english-reference-question.md) is a self-contained question to copy to other agents. It asks for a definition of perfect command, a semantic interface, counterexamples, and a bounded assessment design.

The operator requires an objective criterion, not our belief that semantics exists. Implementation-to-semantics construction applies to compilers and LLMs alike, so formalizability cannot be the discriminator. The current candidate (2026-11-01) therefore drops formal semantics as the ground: an artifact is symbolic when a designated reference constitutes what it permits, and natural-language when no consumer does. Tests corroborate conformance to the reference only. The clerk test and the proxy-versus-requirement split are kept. The earlier hypothesis that an adequately competent interpreter could be a reference for English is relegated to a research question owned by the ideal-interpreter workshop and the standalone question file.

These are conceptual drafts from the discussion, not a literature review or adopted vocabulary changes. The candidate-definitions file holds the latest proposed wording; the earlier reductions remain its supporting argument.

## Boundary

Current write scope is this directory and its entry in the active workshop index. Do not change the library definitions or migrate terminology under this commission. Preserve the operator's distinction between existence of a formal model and corroboration by executors. Do not treat disagreements over which specification is authoritative as an answer to the formalizability question.

The [institution-theory workshop](../institution-theory-import/README.md) investigates broader semantic imports. The [ideal-interpreter workshop](../ideal-interpreter/README.md) owns the experimental LLM interpreter definition. This argument neither adopts that device nor depends on it.

## Closure

Close when the reductions survive review and the operator decides whether they support retiring the special term. A successful result identifies what conformance tests corroborate, states the remaining symbolic/natural-language distinction without making every machine-consumed artifact symbolic, and supplies wording suitable for the affected definitions. An explicit unresolved boundary or rejection is preferable to a forced replacement.

Promotion requires a separately authorized library revision, including checks of codification, constraining, representational form, and the vocabulary collision ledger. Extract the durable result and remove this workshop and its index entry when it closes.
