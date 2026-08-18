# Gate-fold episode record (third episode)

Captured 2026-08-18 by the session that performed the fold, with human inputs quoted verbatim from the live conversation. Nothing here is reconstructed.

This is the episode the workshop was waiting for: the retained epistemology entering operative review machinery. Two semantic review gates were authored, installed with explicit `rests-on` lineage to the theory notes, and validated by live review runs.

## Exact human inputs

The fold directive, with a discuss-first constraint:

> OK - now lets work on folding the epistemology into the writing machinery - discuss it first.

The commission, deciding scale (the agent had recommended starting with one gate) and the validation design:

> add the two gates - then run the validation with Opus sub-agent for the validation run all semantic gates not just the two new - so that it is more similar to the most common way of running it

The discriminative experiment:

> can we run the gates on the previous version of the note?

Acceptance and the calibration follow-up:

> OK - record it and revise the gate

## Agent contributions

- **Coverage map.** Surveyed the existing semantic gate suite and mapped it onto the theory: `semantic/explanatory-reach` already implements the structural threshold; `grounding-alignment` audits cited-support routes; no gate implemented the epistemic threshold. The two-threshold distinction from the warrant note thereby became the division of labor between the old gate and the new one.
- **Gap identification.** Named the two uncovered failure modes: central-claim scope exceeding presented support with no transfer relation, and epistemic-status collapse (including support spreading to neighbouring claims), the latter operationalizing the previously unenforced mixed-epistemic-status note.
- **Gate design.** Authored `semantic/unwarranted-scope` and `semantic/epistemic-status-blur`: failure modes, tests, the pass conditions (stated transfer relation or conjecture marking carries surplus scope; informal status markers suffice), neighbour boundaries, and examples.
- **Sequencing argument.** Recommended gates before COLLECTION.md or skill changes — measurable through the review pipeline, and clean of the separate skill-revision claim.
- **Execution.** Pipeline run and off-pipeline historical run, both with Opus workers; finalization; the post-run boundary clarification prompted by worker feedback.

## Human contributions

- The fold directive itself and its timing.
- The scale decision: both gates at once, against the agent's one-gate-first recommendation.
- The validation design: run the full semantic bundle, not just the new gates, "so that it is more similar to the most common way of running it".
- The discriminative experiment: testing the gates against the previous version of the calibration note was the human's idea, and it produced the episode's strongest result.

## Installation evidence

- Gates committed as `4e935c24`; boundary clarification committed with this record.
- Both gates carry `rests-on` footer edges to *Natural-language theories carry warrant claim by claim and scope by scope*; `epistemic-status-blur` also rests on *Mixed epistemic status must be preserved below the document level*, `unwarranted-scope` also on the derivation-and-inheritance note. The theory-to-machinery lineage is explicit in the artifacts.

## Validation results

- **Pipeline run** (review job 7183, all 10 applicable semantic gates, worker model `claude-opus-5[1m]`, partition `claude-opus-5`): all PASS on the current calibration note (`agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md`), with discriminating INFO findings from both new gates (the "whenever" universal quantifier as the furthest-reaching transfer; a mechanism-bridge sentence marked a section away from its status marker).
- **Historical A/B** (off-pipeline, same model, note at `dc67ccca`, 2026-07-29): `epistemic-status-blur` returned **WARN** on exactly the flat "shared mechanism" sentence that commit `36adf3cf` (2026-08-03) later fixed by adding the quarantined working-hypothesis section. The gate independently detected a defect the note's real revision history fixed, and registers the fix as the INFO-grade residue on the current version. `unwarranted-scope` passed both versions: the old version already carried its transfer relations and interaction-surface boundary, so the historical defect was status blur, not scope overreach.

## Evidential status

This episode establishes **installation**: the retained epistemology now operates as review machinery, with explicit lineage. The A/B result is retrodictive validation — the gate discriminates a real past defect from its fix — not yet the prospective improvement the compounding pathway's third step requires. That step needs a later writing episode whose outcome is better because these gates ran.

One attribution correction recorded for accuracy: the fix commit `36adf3cf` predates the theory episode, so the current calibration note's clean pass is not evidence that the theory improved that note; it is evidence that the gates recognize the difference between the defect and the fix.
