---
description: "Candidate common account of addressable theory and near-decomposability, with counterexamples and tests for deciding whether to retain both concepts."
type: types/note.md
---

# Addressability and near-decomposability

**Status:** candidate. **Recorded:** 2026-11-03, operator discussion of prompt
semantics following the opacity coherence audit.

**Terms and homes.** [Addressable theory](../../theory/definitions/addressable-theory.md)
exposes assumptions, scope conditions and parts for individual inspection and
revision. [Near-decomposability](../../theory/near-decomposability-may-make-local-inspection-affordable.md)
is proposed as a mechanism for local inspection: interactions within blocks
can be considered while interactions across blocks are summarized or neglected
within a question's tolerance.

**Proposed unification.** Both may express one organization into meaningful
parts with manageable interactions, used for different goals. Addressability
uses it for targeted criticism and revision; near-decomposability uses it for
understanding behavior. At a coarse semantic level, a prompt clause can expose
a commitment such as target language without exposing the model computation
that realizes it. Its usefulness for both goals depends on how well that
description captures the relevant interactions.

**Distinctions still to test.** The current minimum for addressability is
weaker than this common account: separately identifiable and editable
commitments can remain strongly coupled. Conversely, a system may have a
near-decomposition that an agent cannot access or does not know. Determine
whether these are different grades or access conditions of one property, or
differences that require separate concepts. Compare the same semantic level,
consumer, question and tolerance; editable text and isolated parameter blocks
are not interchangeable tests.

The [JSON/exception case](../../theory/clear-instructions-can-compose-into-an-unsettled-contract.md)
is a constructed test: the clauses are separately editable, but their combined
obligations are unsettled until scope and exception handling are specified.
It shows that separate editability does not establish a usable semantic
decomposition. It does not show that no decomposition is possible, or that
behavior under an adopted package has strong cross-part interactions; those
are further questions.

**Decision for new text.** Keep the current terms and definitions. Do not
infer independent effects from separate editability, or absence of semantic
addressability from absence of separately located parameter blocks. Treat the
common account as a candidate, not an adopted synonym relation.

**Resolution test.** Explain both useful local revision and useful local
inspection through the proposed common organization. Check the account
against a prompt's coarse semantic clauses, explicit but coupled equations,
and a decomposition unavailable to the inspecting agent. State what would
change in the current definition of addressability if the common account were
adopted, and which distinctions writers would still need. The existing
[matching and bounded-impact account](../../theory/localized-retention-pays-where-change-is-sparse-in-a-matching.md)
is a comparison target: determine whether it supplies the missing conditions
or establishes a substantive separation.
