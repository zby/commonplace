---
description: "Editing an artifact's quality criteria invalidates verdicts (re-judge); editing its production process invalidates artifacts (regenerate) — a verdict is a cache keyed exactly on criteria"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [kb-maintenance]
status: seedling
---

# Criteria edits invalidate verdicts; process edits invalidate artifacts

An artifact's quality contract has two halves that propagate change differently. Editing the **criteria** — what a good artifact looks like — invalidates **verdicts**: the artifact stands, and the correct response is re-judgment against the new criteria. Editing the **process** — how artifacts get produced — invalidates **artifacts**: existing verdicts stand, because the artifacts still meet the unchanged criteria, and the correct response, when the improvement matters retroactively, is regeneration or revision, not review.

Getting this wrong in the process direction is not merely wasteful but misleading. Re-review re-passes the unchanged criteria while the actual deficiency — content produced by a worse method — is invisible to those criteria by construction. A green verdict then certifies exactly the thing that did not improve.

## The formal frame

An accepted verdict is a cached judgment keyed on its inputs. In build-systems terms it is a *verifying trace* (Build Systems à la Carte, Mokhov/Mitchell/Peyton Jones 2018): store hashes of the inputs, compare later to decide freshness. Cache-key design then predicts the two failure modes on either side of the correct boundary. A key too coarse — process text hashed alongside criteria — makes every process wording tweak spuriously stale a whole cohort of verdicts. A key too fine — a criteria-bearing document left out of the hash — leaves verdicts falsely fresh when the real contract changes. The key must contain exactly the criteria: nothing more, nothing less. (Concretely, a review acceptance pins note and gate hashes; the gate is the criteria, and the process that wrote the note is deliberately absent from the key.)

## An institutional witness

The replication crisis fits the process side exactly. Peer-review verdicts checked papers against unchanged criteria while the deficiency lived in production processes — p-hacking, flexible analysis. No amount of re-refereeing could see it, and the working fixes are process-side (pre-registration, registered reports), not verdict-side.

Unlike cached verdicts, which can always be recomputed by re-review, records of process cannot be recreated after the fact — see the linked companion.

---

Relevant Notes:

- [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md) — grounds: the state/history asymmetry this corollary rides on — why process deficiencies are invisible to review-time criteria
- [Link graph plus timestamps enables make-like staleness detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — extends: the make-like staleness model, refined by distinguishing which kind of edit invalidates which kind of product
- [Build Systems à la Carte](../sources/build-systems-a-la-carte.ingest.md) — evidence: verifying traces and rebuilder design as the formal home of verdict invalidation
