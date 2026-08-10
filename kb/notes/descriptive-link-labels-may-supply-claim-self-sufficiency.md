---
description: "Conjecture, partially tested: a claim-reconstruction gate is redundant on Commonplace notes; a label-ablation test attributes the self-sufficiency to the body-premise convention, not link labels. The thin pre-connect-draft case stays untested."
type: kb/types/note.md
traits: [title-as-claim]
tags: []
---

# Descriptive link labels may supply the self-sufficiency a reconstruction gate would check

**Status: conjecture, partially tested.** Evidence: a prototype gate over five notes, plus a label-ablation test over three mature notes (see [Test: label ablation](#test-label-ablation-2026-08-10)). The test strengthens the note's no-gate recommendation but reassigns its mechanism. Treat this as a hypothesis under test, not a finding.

A consuming agent reads a note with only the note's body and the *text of its outbound link labels* — never the content of the linked targets, the source the note was drawn from, or the conversation that produced it. For that reader to reconstruct the note's claim, every load-bearing premise has to travel on the page. In Commonplace, links carry [descriptive labels](../reference/link-vocabulary.md) that state the relation and gloss the target — "grounds: the filter only fires if the adversarial pass has teeth," "extends: develops contextual competence into minimum properties." The conjecture is that these labels do more than navigation: they carry the citing note's load-bearing premises inline, so a note is claim-self-sufficient by construction of the link grammar, not by any separate check.

If that is right, it predicts something testable about review design. A gate that asks "can a cold reader reconstruct the claim and the premises it rests on" should find almost nothing on a corpus that follows the convention, because the convention already prevents the failure the gate looks for.

A prototyped self-sufficiency gate behaved exactly that way. Run as a cold reader over five notes — a polished recent note, a notation-heavy model note, and three early rough notes — it returned PASS five times. It reconstructed each central claim correctly and located the thin spots (a mechanism named but not explained), but rated them non-blocking because a descriptive label or an inline gloss already carried the premise. It never fired.

The design consequence, if the conjecture holds: claim-level self-sufficiency is a property produced by the link-grammar text contract, so the leverage is in enforcing the label convention — and the term-level accessibility gates that already exist — not in adding a holistic reconstruction gate. A gate that always passes is cost without signal. (The [label-ablation test](#test-label-ablation-2026-08-10) below keeps the no-gate half of this consequence but reassigns the mechanism away from the label convention.)

The claim is narrow. It is about *premises* and whole-claim reconstruction, not vocabulary or inference validity: an undefined single term belongs to the `undefined-terms`, `notation-opacity`, and `unidentified-references` gates, and whether an on-page inference actually holds belongs to the `composition-friction-gate`. This conjecture only concerns whether the reader has the premises an argument consumes.

## Test: label ablation (2026-08-10)

A first controlled test isolated the labels as the only variable. Three mature notes — [frontloading spares execution context](./frontloading-spares-execution-context.md), [warranted reader update is the objective of substantive writing](./warranted-reader-update-is-the-objective-of-substantive-writing.md), and [human analogies can motivate functions without determining component boundaries](./human-analogies-suggest-functions-not-component-boundaries.md) — were each read by two cold sub-agents that could not open any linked note. The FULL reader could use the descriptive link text and the Relevant Notes glosses; the STRIPPED reader had to treat every link as an opaque pointer and ignore the Relevant Notes section, simulating a draft before connection labels are added. Both had to reconstruct the central claim, enumerate its load-bearing premises, and flag any premise not present on the page.

All six verdicts were PASS, STRIPPED included. The stripped readers reported that the removed labels only "deepen or motivate" the claim and that "no load-bearing premise is available only through link text or the Relevant Notes section."

This reassigns the mechanism. Removing the labels did not remove self-sufficiency, so the descriptive-label convention is not what supplies it. The premises survived in the note body — the effect of the substantive-specificity rule (`AGENTS.md`) that requires load-bearing premises to travel in the prose. Labels corroborate and route; the body carries. The conjecture's practical recommendation is *strengthened* — a holistic reconstruction gate passed even on de-labeled notes, so it is cost without signal — but its causal attribution to the link grammar is *not* supported.

The test is partial. It varied the labels while holding each body at full maturity; it did not test a genuinely thin pre-connect draft, whose body might not yet carry the premises. So the finding is narrow: for mature notes, self-sufficiency lives in the body, not the labels. Whether a thin draft fails, and whether label-addition or body-enrichment is what rescues it, remains the open discriminating test.

## How this could be wrong

- The evidence is five already-promoted notes. Each had already passed through glossing and connection, so labels and inline context were in place. The failure the gate looks for should occur *before* those labels are added — in a fresh draft or a workshop artifact prior to a connect pass. The three-outcome logic is: if the gate fires on pre-label drafts but not on labeled notes, the convention supplies self-sufficiency (supporting this conjecture); if it never fires anywhere, something else explains it; if it fires even on well-labeled notes, the convention is not doing the work. The label-ablation test above landed in the second branch — the gate never fired, even with labels removed — which points the mechanism at the body-premise convention rather than the labels. But that test simulated the no-label condition on *mature* bodies; the thin-body half of a genuine pre-connect draft is still untested.
- A single reviewer model at one threshold produced every verdict. A stricter reviewer might reclassify the non-blocking thin spots as failures, in which case the gate has signal after all.
- The conjecture assumes labels are premise-bearing rather than decorative. A label that only names a relation without glossing the referent carries navigation but not the premise, and a note leaning on such labels would not be self-sufficient. So this is really a claim about *good* labels, and it depends on how consistently the corpus writes them.

## Open questions

- Does the gate fire on a genuinely thin pre-connect draft? The label-ablation test answered only the mature-body case (it did not fire); the thin-body case is the cheapest remaining experiment.
- Is the useful check about label *quality* — whether each load-bearing link glosses its premise — rather than about claim reconstruction? A label-quality gate would target the convention directly instead of measuring its downstream effect.

---

Relevant Notes:

- [linking-theory](./linking-theory.md) — grounds: what makes a link label carry meaning rather than merely point
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: a descriptive label frontloads the linked note's load-bearing premise into the citing note's context, sparing the reader a lookup
