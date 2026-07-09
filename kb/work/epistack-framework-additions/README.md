# Workshop: epistack-framework-additions

Brainstorm of framework additions to Commonplace that would make **epistemic casework** — tasks like the FLF Epistemic Case Study Competition's lab-leak / black-hole / egg cases — easier, plus a recommended personal-epistemology stance for the person running such casework.

This is the *design-thinking* companion to [`epistack-competition`](../epistack-competition/README.md), which is only the framework-side pointer to the sibling `epistack-casebooks` repo and the `backlog-to-commonplace.md` protocol. This workshop holds the menu of candidate additions; the sibling repo is where any of them get built and proven.

Each candidate now lives in its own document, linked below. **No framework code is written from this workshop.** The discipline is build-local-first in the casebook repo, upstream what survives — this is a design menu, not an implementation plan. What closes the workshop: each candidate has either become a queued experiment in `epistack-casebooks` and logged to its backlog, or been rejected with a reason; anything that survives a worked case gets promoted as a proposal/type/note, then this workshop is deleted.

**Source caveat.** The competition pages (`flf.org`, EA Forum, GreaterWrong, Oliver Sourbut's "A Full Epistemic Stack") were unfetchable from the authoring environment (403 via network policy). The framing is assembled from search snippets, the sibling-repo summary in `epistack-competition`, and a pasted [ChatGPT second opinion](./chatgpt-second-opinion.md); verify against the primary sources before relying on specifics.

## Framework-side results (2026-07-08 review session)

A framework-side review of this menu produced library artifacts that change the ground under the Foundation section — read these before the next brainstorming round:

- [A universal knowledge framework demotes content taxonomies to defaults and keeps answerability](../../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) — the theory: register-style taxonomies are guarded defaults, not universals; what stays universal is the declared collection contract plus answerability. **Consequence for this workshop: the "fourth register" needs no taxonomy amendment — the casebook just writes its `COLLECTION.md` contract** (see the updated [fourth-register](./fourth-register.md)).
- [ADR 042: register becomes a default profile under open-ended text contracts](../../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) — the decision instantiating that claim for registers, adopted on the strength of this casework's first worked case.
- A predicted follow-up gap, now also a proposal: the note type's `status` field fuses lifecycle with first-person endorsement — see [assertion force separate from lifecycle status](../../reference/proposals/assertion-force-separate-from-lifecycle-status.md) and the contradiction flag added to [claim-type](./claim-type.md).
- The review also flagged: the [second opinion](./chatgpt-second-opinion.md) file is truncated (see its header note), and the "contradictions get silently averaged" mechanism several candidates lean on is untested — added as a third experiment in [suggested-first-experiments](./suggested-first-experiments.md).

## Foundation

- [The core tension to design around](./core-tension.md) — why casework needs a stance-neutral evidence map, against Commonplace's first-person-committed grain
- [The biggest single addition: a fourth register](./fourth-register.md) — a dialectical/evidential register; the methodological move everything else hangs off. **Updated 2026-07-08: demoted from taxonomy addition to collection contract — see the file.**

## Ingestion / provenance layer

- [Source-span citations, not file-level links](./source-span-citations.md)
- [A richer `source` type](./richer-source-type.md)
- [Traversable provenance chains](./traversable-provenance-chains.md)

## Structure layer

- [A `claim` type distinct from `structured-claim`](./claim-type.md)
- [A dialectical/evidential link vocabulary](./dialectical-link-vocabulary.md)
- [Party/position attribution](./party-position-attribution.md)
- [A first-class gap register](./gap-register.md)

## Assessment layer

- [Confidence must be attributed, never a mark](./attributed-confidence-not-marks.md)
- [Epistemic review gates](./epistemic-review-gates.md)
- [Adjudication as a separate, labeled, downstream layer](./adjudication-as-separate-layer.md)

## Additional candidates (imported from the second opinion)

- [Independence clustering of evidence](./independence-clustering.md)
- [A `crux` type, distinct from the gap register](./crux-type.md)
- [Model / calculation artifacts](./model-calculation-artifacts.md)
- [Multi-method assessment comparison](./multi-method-assessment-comparison.md)
- [Derived dashboards and a source-impact command](./dashboards-and-source-impact.md)
- [The belief-ledger practice](./belief-ledger.md)

## Cross-cutting

- [Recommended personal-epistemology stance](./personal-epistemology-stance.md)
- [Suggested first experiments](./suggested-first-experiments.md)
- [Rejected candidates (with reasons)](./rejected-candidates.md)
- [Open questions](./open-questions.md)

## Source material

- [ChatGPT second opinion](./chatgpt-second-opinion.md) — the pasted independent analysis these candidates were screened against
