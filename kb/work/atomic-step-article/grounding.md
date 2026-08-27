# Grounding inventory

Collected 2026-08-27. Three kinds of material: what the KB already holds, what this session measured or reinterpreted, and literature the KB does not hold yet. None of it fixes the article's outline.

## What the KB already holds

**Atomic notes (covered, but justified differently).**

- [Short composable notes maximize combinatorial discovery](../../notes/short-composable-notes-maximize-combinatorial-discovery.md) — rests-on: "one claim, one note", justified by bounded-context co-loading, not by reviewability. The article's contrast: same shape of rule, different justification, and the two come apart on multi-source evidence notes.
- [Title as claim enables traversal as reasoning](../../notes/title-as-claim-enables-traversal-as-reasoning.md) — see-also: following links between claim-titled notes reads as a chain of reasoning. If each note is one checkable step, the chain is the argument and each link is a step boundary.
- `cp-skill-write-multistage` (SKILL.md, "one atomic central contribution … one proposition another artifact can cite as a premise") and ADR 070 (splitting preferred when it yields atomic, independently useful notes) — the operational form the atomic-note rule already takes.

**The reviewer's budget as a design constraint (present, but placed on the review, not the artifact).**

- [ADR 079](../../reference/adr/079-grounding-reviews-budget-sixteen-distinct-linked-artifacts.md) — contrasts: the budget is sixteen distinct linked artifacts, chosen at the corpus p90; reaching it is disclosure, not failure. The article proposes the opposite placement of the same constraint.
- [A five-link cap missed four grounding findings in twelve reviews](../../notes/evidence/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md) — evidenced-by, reinterpreted below: the strongest evidence the KB holds against a cap of five, and it reads differently once the cap is on the artifact.
- [Exceeding a review budget splits the task](../../reference/proposals/exceeding-a-review-budget-splits-the-task.md) — contrasts: splits the *review* into covering passes, explicitly refusing to "punish an artifact for being well-cited". Atomic steps split the *artifact* instead. The article has to say why that is not punishment.
- [review-attention-price](../review-attention-price/README.md) — see-also: the peer workshop this idea reverses; its Mechanism B (code packs the evidence) becomes "the author packs the evidence" under atomic steps.

**Verbatim quotes as mechanical evidence (covered, strongly — the escape hatch is already shipped).**

- [ADR 046](../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md) — rests-on: `verbatim`-marked quotations in any note are resolved by substring test against the linked file; mismatch fails. Implemented in `src/commonplace/lib/quote_verification.py` and `validate_verbatim_quotes` (`lib/validation.py`).
- [ADR 073](../../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md) and [ADR 078](../../reference/adr/078-writers-invoke-grounding-and-evidence-stays-in-the-ingest.md) — rests-on: the ingest's `## Quotes` section is the evidential surface, validated against the snapshot; analysis elsewhere in the ingest is not support. ADR 073 also rejects a paraphrase ledger because it "creates two semantic hops".
- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — mechanism: the general rule ADR 046 instantiates; a verbatim quote has a mechanical derivation rule (substring match), a paraphrase does not.
- [A citation cannot assert more fidelity than its capture preserved](../../notes/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md) — mechanism: the verbatim/paraphrase/second-hand layering; explains why the escape hatch works only for the verbatim layer.
- [Quotes-route rollout grounded more uses without earning claim IDs](../../notes/evidence/quotes-route-rollout-grounded-more-uses-without-earning-claim-ids.md) — evidenced-by: 30% grounded uses under a paraphrased ledger, 75% under verbatim quotes or pinned snapshots.
- Definitions the article will lean on: [codification](../../notes/definitions/codification.md), [constraining](../../notes/definitions/constraining.md), representational form (CLAUDE.md vocabulary). The escape hatch is a crossing on the representational-form axis: the support moves from natural-language (judged) to symbolic-checkable (matched).

**Oracle notes (adjacent; the check as an oracle with a domain).**

- [Warranted autonomy is bounded by oracle domain](../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) — see-also: evaluation autonomy extends only to what the oracle can assess with the required confidence. A step is atomic relative to an oracle; "fits one pass" is a domain bound.
- [Error correction works above chance oracles with decorrelated checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — see-also: the reviewer's discriminative power is what the step size protects; the paired assay measured that power falling at the cap, not capacity running out.

**Layered / transitive grounding (weak — the KB does not hold it).** Nothing asserts "a linked note passed its own gate, so the citing note need not re-ground it". Nearest: `kb/notes/COLLECTION.md` treats `kb/notes/evidence/` as a real layer whose notes state their own bounded inference; [Descriptive link labels may supply claim self-sufficiency](../../notes/descriptive-link-labels-may-supply-claim-self-sufficiency.md) is a partially tested conjecture that a reader never needs to open the target. ADR 073's two-hops argument is a negative result for the *paraphrase* case and must be distinguished from it.

## Measured this session

Distinct link targets per file, counted mechanically (`]( … .md)` targets, deduplicated; ingest = a target under `sources/` ending `.ingest.md`):

| population | files | 0 ingest links | >3 | >5 | max ingest links | max distinct `.md` targets |
|---|---|---|---|---|---|---|
| `kb/notes/` | 344 | 256 | 18 | 8 | 9 | 35 |
| `kb/articles/` | 7 | 2 | 1 | 0 | 4 | 29 |

The eight notes over five sources: `theory-mediated-learning-may-improve-sample-efficiency-under-shifts` (9), `knowledge-storage-does-not-imply-contextual-activation` (8), `an-omitted-loop-function-and-a-frozen-one-need-different-repairs` (7), `evidence/real-self-improving-systems-occupy-combinations-no-rung-captures` (7), `a-proposal-selection-loop-requires-search-evaluation-and-retention` (6), `evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces` (6), `instantiation-alone-cannot-model-agent-learning-across-sessions` (6), `formal-systems-assess-explanatory-reach-through-causal-and-proof` (6).

What this fixes: a cap of five on *sources* costs eight notes; a cap of five on *distinct artifacts* (ADR 079's unit, p50 = 7) would violate over half the corpus. The idea is affordable only in the source-counting form, which is why the note-link exemption is load-bearing.

## Reinterpretations made this session (working claims, not yet defended)

1. **The four-miss evidence flips sides.** The misses appeared after reading 6, 11, 14 and 16 artifacts because those notes were larger than the step and the reviewer stopped at the cap. That shows reviewers stop at a cap — which an author-side limit relies on — not that five is too small for a five-source note. Under an artifact-side cap the note splits or quotes; the gate does not grow.
2. **Capacity was never the protected resource.** The uncapped arm read 22 artifacts and 322 KB with no observed loss. What a small step buys that a price never does: the verdict itself becomes checkable by a human in one sitting.
3. **Author packs, code does not.** Mechanism B in review-attention-price has code assemble the evidence pack so nothing is trusted to a tally. Under atomic steps the author assembles it — the quoted passages are the pack, and the pack is the note. The pull-mode reviewer with a small cap is then fine because the cap never binds on a conforming note.
4. **What the validator would check** (for the peer workshop, not the article): distinct ingest targets without an accompanying verified verbatim quote ≤ N. The verifier already pairs a quote with the nearest link in its paragraph. One tightening needed: `verify_content` matches against the whole linked file (`quote_verification.py:268`), so a quote aimed at an ingest can match its analytical prose; for ingest targets it should match the `## Quotes` section only.
5. **Bytes are still unbounded.** A `(snapshot required)` route can be 753 KB. The full-source exception in review-attention-price's design survives unchanged.

## Open questions the article must face

- **Why note links are exempt.** The candidate argument: a paraphrase ledger *stands in for* a source, so trusting it is a second semantic hop over the same evidence; a linked note is a *premise with its own certificate* — it passed its own gates, its title is the claim, and the citing note's obligation is to represent it (concept-attribution, misleading-link-text), not to re-ground it. Whether that distinction holds is the claim the KB does not yet contain; it decides whether the article's rule is "five sources" or "five things to open".
- **Whether "atomic step" is a property of the note or of the (note, check) pair.** A note with nine sources and nine verbatim quotes is one step for the grounding gate and possibly not for a gate that judges the inference across them. The oracle notes suggest the answer is "relative to the check".
- **Where the number comes from.** Not from a degradation point (that was Track B's question). Candidates: what a human can check in one sitting; the smallest N at which no observed miss occurred; a chosen step size stated as a convention. The article should say which kind of number it is, not what it is.

## Literature candidates (not in the KB; ingest before attributing)

Presence checked by `rg` over `kb/sources/*.ingest.md` on 2026-08-27 morning; Descartes and Lamport were ingested and grounded later that day (see the README's state entry), the Paulsen item already had an ingest, the rest still do not.

- **Descartes, *Rules for the Direction of the Mind* (Rules VII, XI) and *Discourse on Method* (the second and fourth precepts)** — divide each difficulty into as many parts as needed; run through long chains of inference in a continuous movement because memory cannot hold them. The classical statement that a chain is checked step by step and that step size is bounded by what the checker can hold. Not ingested.
- **Lamport, "How to Write a Proof" (1993) and "How to Write a 21st Century Proof" (2012)** — hierarchical structured proofs; errors are found because each leaf step is small enough to check, and the method's own test was that structuring exposed errors in published proofs. Closest engineering precedent for "size the step to the check". Not ingested.
- **De Millo, Lipton, Perlis, "Social Processes and Proofs of Theorems and Programs" (1979)** — proofs are believed through social checking, which long formal verifications defeat. Useful as the contrast the verbatim hatch answers: a mechanical check that a human can also read. Not ingested.
- **Proof assistants and the de Bruijn criterion** — a small trusted kernel checks every step; the human's work is decomposition. The verbatim-quote validator is a very small kernel for one kind of step. Only a Darwin Gödel Machine ingest mentions a proof checker; no dedicated source.
- **Code-review change-size evidence** — Cohen/SmartBear (2006, defect detection falls beyond ~200–400 LOC), Rigby & Bird 2013 ("Convergent contemporary software peer review practices"), Sadowski et al. 2018 ("Modern Code Review: A Case Study at Google", small changes as norm). The engineering practice that already sizes the artifact to the reviewer. Not ingested.
- **Lightman et al., "Let's Verify Step by Step" (2023)** — process supervision (per-step verification) beats outcome supervision; the LLM-side form of the same claim. Six ingests mention process reward models in passing; no ingest of this paper.
- **Luhmann / Zettelkasten atomicity** — the origin of the atomic-note rule the article contrasts with. `kb/sources/luhmann-archive-schlagwortregister.ingest.md` exists but covers keyword registers, not note size; an Ahrens or Luhmann "Kommunikation mit Zettelkästen" ingest would be needed for the atomic-note attribution.
- **Paulsen, maximum effective context window** — [ingested](../../sources/paulsen-maximum-effective-context-window-mecw.ingest.md): effective windows far below advertised, task-dependent, hallucination rising beyond them. The degradation-side support for bounding what one check reads; check its Quotes before citing.
