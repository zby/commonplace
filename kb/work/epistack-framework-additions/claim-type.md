# A `claim` type distinct from `structured-claim`

Layer: structure.

[`structured-claim`](../../notes/types/structured-claim.md) is *an argument for a position* (Evidence / Reasoning / Caveats). Casework needs a claim as a *node in a disagreement graph*: the proposition, who asserts it, its support, its rebuttals, and a status (`contested` / `settled` / `open`), with the proposition deliberately decoupled from any verdict.

Keep support and rebuttal on *edges* ([dialectical link vocabulary](./dialectical-link-vocabulary.md)), attributed to a party ([party/position attribution](./party-position-attribution.md)) — do not put a stance scalar on the claim itself (see the rejection of `polarity` / `status` fields in [rejected-candidates](./rejected-candidates.md)).
