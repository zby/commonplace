---
description: "Editing quality criteria invalidates verdicts; editing production processes calls for artifact regeneration — verdict freshness includes the artifact and criteria but excludes its production process"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [kb-maintenance]
---

# Criteria edits invalidate verdicts; process edits invalidate artifacts

An artifact's quality contract has two halves that propagate change differently. Editing the **criteria** — what a good artifact looks like — invalidates **verdicts**: the artifact stands, and the correct response is re-judgment against the new criteria. Editing the **process** — how artifacts get produced — invalidates **artifacts**: existing verdicts stand, because the artifacts still meet the unchanged criteria, and the correct response, when the improvement matters retroactively, is regeneration or revision, not review.

Getting this wrong in the process direction is not merely wasteful but misleading. Re-review re-passes the unchanged criteria while the actual deficiency — content produced by a worse method — is invisible to those criteria by construction. A green verdict then certifies exactly the thing that did not improve.

## The formal frame

[Build Systems à la Carte](../sources/build-systems-a-la-carte.ingest.md) supplies a bounded analogy, not the criteria/process distinction itself. In the paper's framework, a rebuilder decides whether a key needs rebuilding. Shake is classified as a verifying-traces system: it persists the prior dependency graph with file-content hashes and rebuilds a target when a recorded dependency changes. The paper separately calls Excel *self-tracking* because a changed formula causes recomputation; many software build systems instead require a manually initiated full rebuild after a task changes.

Applied to review, an accepted verdict is a cached judgment keyed on the evaluated artifact and its criteria-bearing inputs. Cache-key design then predicts two local failure modes. Including process text makes a process wording edit spuriously stale the verdict. Omitting a criteria-bearing document leaves the verdict falsely fresh after its contract changes. The review key must therefore include the artifact and all criteria-bearing inputs while excluding its production process. Concretely, a review acceptance pins note and gate hashes; the gate supplies the criterion, while the process that wrote the note is deliberately absent. This exact key boundary and the conclusion that process edits call for artifact regeneration are Commonplace's transfer from the build-system model; the paper does not state them.

## An institutional witness

The replication crisis fits the process side exactly. Peer-review verdicts checked papers against unchanged criteria while the deficiency lived in production processes — p-hacking, flexible analysis. No amount of re-refereeing could see it, and the working fixes are process-side (pre-registration, registered reports), not verdict-side.

Unlike cached verdicts, which can always be recomputed by re-review, records of process cannot be recreated after the fact — see the linked companion.

---

Relevant Notes:

- [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md) — grounds: the state/history asymmetry this corollary rides on — why process deficiencies are invisible to review-time criteria
- [Link graph plus timestamps enables make-like staleness detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — extends: the make-like staleness model, refined by distinguishing which kind of edit invalidates which kind of product
- [Build Systems à la Carte](../sources/build-systems-a-la-carte.ingest.md) — evidenced-by: separates rebuild decisions from scheduling, classifies Shake by dependency-and-hash verifying traces, and distinguishes input tracking from self-tracking task changes; the verdict mapping is local
