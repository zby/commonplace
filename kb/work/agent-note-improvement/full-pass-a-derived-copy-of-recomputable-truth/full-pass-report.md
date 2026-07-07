# Full Improvement Pass: A derived copy of recomputable truth must be checked or absent

**Target:** `kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`
**Reports used:** compression bundle, critique-note, connect (semantic bundle skipped — this is an exploratory pass, not a promotion decision)

## Strongest retained claim

A copy of information mechanically recomputable from a ground-truth source must be either machine-checked (a validator re-derives it and fails on mismatch) or absent — hand-maintained-and-trusted is forbidden as a third state. The compression bundle confirms this is already maximally prominent (frontmatter, title, opening paragraph) — no repositioning needed.

## Body edits

| Location | Source method(s) | Finding | Action | Rationale |
|---|---|---|---|---|
| "What enforcement buys" (4 paragraphs) | compression/detail-overhang, compression/marginal-value-redundancy | Restates at length what the two "Relevant Notes" extends-bullets already say in one line each; not load-bearing for the core deontic claim | compress to one short paragraph | Deletion test passes — "What checked requires" and "Consequences" already carry the note's support route without it |
| "Where the rule applies," 2nd paragraph | compression/detail-overhang | Four sentences of parallel rhetoric restate the same point three times before a closing sentence that compresses the whole paragraph into one clause | compress, keep the closing compression as the topic sentence | Same signal as above: the paragraph's own ending shows the preceding buildup was excess |
| "What 'checked' requires — and its limits" | critique-note | Unaddressed regress objection: a validator is itself a hand-maintained artifact carrying an unenforced claim ("this derivation rule correctly re-derives the copy"), which is the same forbidden third state relocated one layer down. Bites concretely on the note's own flagship instance (tag-README `rg` sweep is a judgment-laden heuristic, not a strict mechanical derivation) | add a short 4th precondition/caveat naming why enforcement is expected to bottom out (validators are centralized, versioned, reviewed, and amortized across many copies, unlike N hand-maintained instances) rather than recurse | This is not a hedge against a possible objection — it's the strongest attack the critique produced, it is currently fully unengaged, and without it the note's "forbidden" framing overclaims relative to what enforcement actually buys. Net effect keeps this pass close to length-neutral: the space cut from "What enforcement buys" pays for this addition. |
| "Instances across four surfaces," tag-README bullet | critique-note (secondary objection) | The bullet calls the tag-README marks "enforced and shipped" without qualifying that the `rg`-sweep derivation rule is itself a hand-authored heuristic | add one clause acknowledging the derivation rule's own correctness is what the new caveat above is about | Ties the caveat back to the note's one concrete "already enforced" instance instead of leaving it abstract |

Not adopted from critique-note: the expected-value / validator-authoring-cost objection (secondary prong) and the graduated-enforcement objection (secondary objections list). Both are real but are hedges against edge cases the note's scope note already gestures at ("too costly to run always" language exists elsewhere in the KB's testing-pyramid framing); adding them here would re-open the additive-apparatus failure mode the compression bundle is biased against. Left as-is.

## Connection candidates (from connect report)

- `history-has-one-chance-to-become-checkable` — **contrasts** (add). Strongest missing return link: it develops the non-recomputable complement of this note's preconditions #1/#3.
- `an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract` — **extends** (add). Directly relevant to the new validator-correctness caveat and the note's own instance #1.
- `prose-has-no-dereference-reinforce-facts-at-point-of-use` — **extends** (add). Partially answers the note's own first Open Question about the `status:` field.
- `many-to-many-edge-state-is-where-files-yield-to-a-database` — see-also (skip). Connect itself flagged this as optional/asymmetric; skipping keeps the footer from growing past what earns its place.
- `criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts` — contrasts (skip). Connect flagged moderate confidence and a plausible redundant-transitive-path concern; not worth the added footer line on a compression-biased pass.
- Maintenance fix: the existing `llm-recompute-cost-inverts-the-store-vs-recompute-default` footer entry uses `complements`, which is not in `kb/notes/COLLECTION.md`'s authorised label set. Retarget to **grounds** ("wants to verify the premise") — the linked note supplies the economic premise (recompute is dear to a model) that this note's claim leans on.

## Proposed revision shape

Unchanged overall structure and length. "What enforcement buys" shrinks from 4 paragraphs to 1; "Where the rule applies" 2nd paragraph shortens by roughly half; "What 'checked' requires" gains one short 4th precondition; the tag-README instance bullet gains one clause; the footer gains three links and fixes one label. No section is removed, split, or rehomed — this note is a single-claim synthesis (connect's own "no split candidate" flag agrees), so the workshop's split/rehome frame doesn't apply here; the compression and critique frames do all the work.

## Open items

- Whether the new validator-correctness caveat should eventually grow into its own note (a general "who checks the checker" claim) is left as a candidate for a later pass — critique-note's regress objection is general enough to outlive this specific note, but one precondition-level caveat is enough to make *this* note defensible without opening a second thesis.
