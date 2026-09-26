---
description: "Curated head for the claims-and-grounding tag — claim titles, claim modality, ground truth and supersession, source grounding and quotes, and grounding evidence from review runs"
type: types/tag-readme.md
complete: true
---

# claims-and-grounding

How KB content commits to claims and how those claims stay tied to what supports them: titles written as claims, the modes a claim can take, what counts as ground truth, grounding a claim in a source, and what happens to a claim once it is superseded. The establishing notes are [title as claim exposes commitments, enabling Popperian maintenance](../notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) for claim titles and [commitment, not derivation, creates new ground truth](../notes/commitment-not-derivation-creates-new-ground-truth.md) for ground truth. The grounding procedure is [cp-skill-ground](../instructions/cp-skill-ground/SKILL.md). Running a grounding check as an LLM gate, and when its verdict goes stale, belongs to [review-system](./review-system-README.md); this tag is about what the check asks. A child of [kb-maintenance](./kb-maintenance-README.md).

## Claims as commitments

- [Title as claim exposes commitments, enabling Popperian maintenance](../notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — a list of claim titles can be scanned with "do I still believe this?" without opening files
- [Title as claim makes overlap between notes visible](../notes/title-as-claim-makes-overlap-between-notes-visible.md) — similar assertions show at the index level, where topical titles hide them
- [Claim modality is the inference form of the refuter](../notes/claim-modality-is-the-inference-form-of-the-refuter.md) — the three claim modes follow from how a claim would be refuted, which closes the mode list for empirical claims
- [Ad hoc explanation can be rational when error is cheap and local](../notes/ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md) — a disposable guess may pick the next probe; a retained explanation needs reach checks
- [Write-time vocabulary collision controls](../reference/proposals/write-time-vocabulary-collision-controls.md) — proposal for mechanical controls that keep one term to one sense, so a claim's words keep their registered meaning

## Ground truth and supersession

- [Commitment, not derivation, creates new ground truth](../notes/commitment-not-derivation-creates-new-ground-truth.md) — derived claims leave the source as ground truth; unentailed resolutions become ground truth at commit
- [A derived copy of recomputable truth must be checked or absent](../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — a copy of recomputable information is machine-checked against its source or does not exist
- [Superseded choices need a historical witness; refuted beliefs lose subject-matter standing](../notes/superseded-choices-are-retained-superseded-beliefs-are-not.md) — what to keep after supersession depends on the claim's remaining truth role

## Grounding in sources

- [A linked note discharges its own grounding, so a citing note owes representation, not re-grounding](../notes/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md) — citing a source imposes a grounding obligation; citing a grounded note imposes only faithful representation
- [A quotes-route rollout grounded more claim uses without earning claim identifiers](../notes/evidence/quotes-route-rollout-grounded-more-uses-without-earning-claim-ids.md) — evidence for verbatim quotes over a paraphrased claims ledger: 75% versus 30% grounded uses, descriptive only
- [A five-link cap missed four grounding findings in twelve reviews](../notes/evidence/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md) — evidence that capping linked reading hides grounding findings
- [An independent pass tightened three of four Pirolli grounding verdicts](../notes/evidence/independent-pass-tightened-three-of-four-pirolli-verdicts.md) — evidence that separating source reconstruction from claim judgment changes grounding verdicts; a candidate control, not a proven cause

## Related Tags

- [kb-maintenance](./kb-maintenance-README.md) — the parent: claims and their grounding are what maintenance keeps true
- [review-system](./review-system-README.md) — sibling: the gates that run grounding checks and track verdict freshness
- [curation](./curation-README.md) — sibling: indexes and tag heads, where claim titles are scanned
- [evaluation](./evaluation-README.md) — the grounding evidence notes are also evaluation results
- [links](./links-README.md) — link semantics behind citing a note versus citing a source
