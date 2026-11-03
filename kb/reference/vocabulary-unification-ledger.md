---
description: "Tracks different KB terms that may name one underlying concept, with the proposed unification, distinctions still to test, and the current decision for writers."
type: types/note.md
---

# Vocabulary unification ledger

This ledger records candidates for conceptual unification so that vocabulary
reviews and definition revisions can revisit them without reconstructing the
original question. The [collision ledger](./vocabulary-collision-ledger.md)
tracks one term carrying different senses. This ledger tracks different terms
that may describe the same underlying property or mechanism, including cases
where different goals led to different names.

An entry records a candidate and the current writing decision; it does not
establish equivalence or supersede the linked definitions. Shared examples or
similar wording are insufficient: the proposed common account must explain
what each concept contributes and identify any conditions under which they
come apart. Unification may yield one preferred term, or retain two terms for
distinct uses of a common account.

## Maintenance

Add an entry when a comparison supplies a specific common account worth
testing. Record the terms and their homes, the proposed unification, remaining
distinctions, the decision for new text, and what would resolve the candidate.
Keep these records compact; extended investigation belongs in a workshop and
the resulting theoretical claim belongs in theory.

Pending entries remain here. When a candidate is adopted, put the common
account and any retained distinctions in the relevant definitions or theory
notes, update affected consumers, and remove the entry. When rejected, retain
the useful distinction in the relevant notes and remove the entry. The commit
records the resolution; the ledger does not accumulate decision history.

## Addressability and near-decomposability

**Status:** candidate. **Recorded:** 2026-11-03, operator discussion of prompt
semantics following the opacity coherence audit.

**Terms and homes.** [Addressable theory](../theory/definitions/addressable-theory.md)
exposes assumptions, scope conditions and parts for individual inspection and
revision. [Near-decomposability](../theory/opacity-is-the-lack-of-a-known-near-decomposition-for-the-question.md)
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
[matching and bounded-impact account](../theory/localized-retention-pays-where-change-is-sparse-in-a-matching.md)
is a comparison target: determine whether it supplies the missing conditions
or establishes a substantive separation.
