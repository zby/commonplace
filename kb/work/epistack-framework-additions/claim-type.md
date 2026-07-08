# A `claim` type distinct from `structured-claim`

Layer: structure.

[`structured-claim`](../../notes/types/structured-claim.md) is *an argument for a position* (Evidence / Reasoning / Caveats). Casework needs a claim as a *node in a disagreement graph*: the proposition, who asserts it, its support, its rebuttals, and a status (`contested` / `settled` / `open`), with the proposition deliberately decoupled from any verdict.

Keep support and rebuttal on *edges* ([dialectical link vocabulary](./dialectical-link-vocabulary.md)), attributed to a party ([party/position attribution](./party-position-attribution.md)) — do not put a stance scalar on the claim itself (see the rejection of `polarity` / `status` fields in [rejected-candidates](./rejected-candidates.md)).

## Contradiction flagged 2026-07-08 (unresolved)

The status enum above (`contested` / `settled` / `open`) contradicts [rejected-candidates](./rejected-candidates.md), which rejects `status: disputed` as a stance-carrying field. Resolution sketch from the framework-side review, via the mark discipline (`kb/types/tag-readme.md`): `contested` and `open` are **recomputable from edge structure** (contested = has ≥1 rebuttal edge), so they can be legitimate validator-enforced marks. `settled` is not recomputable — the workshop's own `settlement-illusion` review gate exists because settlement is a judgment call — so `settled` must either be dropped or live in the assessment layer as an attributed judgment, never on the neutral claim node. Decide when the type is prototyped.

Related: the framework-side [assertion force separate from lifecycle status](../../reference/proposals/assertion-force-separate-from-lifecycle-status.md) proposal — the base `status` field's "commitment level" semantics are first-person and ambiguous for attributed claims ("current" = "I still endorse" vs "attribution still accurate"); the casebook's contract must say which it means.
