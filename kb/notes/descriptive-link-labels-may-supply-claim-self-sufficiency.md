---
description: "Conjecture: Commonplace's descriptive link labels carry a note's load-bearing premises inline, so a claim-reconstruction review gate finds little the convention does not already prevent — a hypothesis to test on pre-connect drafts."
type: kb/types/note.md
traits: [title-as-claim]
tags: []
---

# Descriptive link labels may supply the self-sufficiency a reconstruction gate would check

**Status: conjecture.** The evidence is one prototype gate and five notes. Treat this as a hypothesis to test, not a finding.

A consuming agent reads a note with only the note's body and the *text of its outbound link labels* — never the content of the linked targets, the source the note was drawn from, or the conversation that produced it. For that reader to reconstruct the note's claim, every load-bearing premise has to travel on the page. In Commonplace, links carry [descriptive labels](../reference/link-vocabulary.md) that state the relation and gloss the target — "grounds: the filter only fires if the adversarial pass has teeth," "extends: develops contextual competence into minimum properties." The conjecture is that these labels do more than navigation: they carry the citing note's load-bearing premises inline, so a note is claim-self-sufficient by construction of the link grammar, not by any separate check.

If that is right, it predicts something testable about review design. A gate that asks "can a cold reader reconstruct the claim and the premises it rests on" should find almost nothing on a corpus that follows the convention, because the convention already prevents the failure the gate looks for.

A prototyped self-sufficiency gate behaved exactly that way. Run as a cold reader over five notes — a polished recent note, a notation-heavy model note, and three early rough notes — it returned PASS five times. It reconstructed each central claim correctly and located the thin spots (a mechanism named but not explained), but rated them non-blocking because a descriptive label or an inline gloss already carried the premise. It never fired.

The design consequence, if the conjecture holds: claim-level self-sufficiency is a property produced by the link-grammar text contract, so the leverage is in enforcing the label convention — and the term-level accessibility gates that already exist — not in adding a holistic reconstruction gate. A gate that always passes is cost without signal.

The claim is narrow. It is about *premises* and whole-claim reconstruction, not vocabulary or inference validity: an undefined single term belongs to the `undefined-terms`, `notation-opacity`, and `unidentified-references` gates, and whether an on-page inference actually holds belongs to the `composition-friction-gate`. This conjecture only concerns whether the reader has the premises an argument consumes.

## How this could be wrong

- The evidence is five already-promoted notes. Each had already passed through glossing and connection, so labels and inline context were in place. The failure the gate looks for should occur *before* those labels are added — in a fresh draft or a workshop artifact prior to a connect pass. The gate was never tested there. That, not the mature corpus, is the discriminating test: if the gate fires on pre-label drafts but not on labeled notes, the convention is what supplies self-sufficiency (supporting this conjecture); if it never fires anywhere, something else explains the self-sufficiency; if it fires even on well-labeled notes, the convention is not doing the work.
- A single reviewer model at one threshold produced every verdict. A stricter reviewer might reclassify the non-blocking thin spots as failures, in which case the gate has signal after all.
- The conjecture assumes labels are premise-bearing rather than decorative. A label that only names a relation without glossing the referent carries navigation but not the premise, and a note leaning on such labels would not be self-sufficient. So this is really a claim about *good* labels, and it depends on how consistently the corpus writes them.

## Open questions

- Does the gate fire on pre-connect drafts? This is the discriminating test above and the cheapest next experiment.
- Is the useful check about label *quality* — whether each load-bearing link glosses its premise — rather than about claim reconstruction? A label-quality gate would target the convention directly instead of measuring its downstream effect.

---

Relevant Notes:

- [linking-theory](./linking-theory.md) — grounds: what makes a link label carry meaning rather than merely point
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: a descriptive label frontloads the linked note's load-bearing premise into the citing note's context, sparing the reader a lookup
