# Transformation closure workshop

## Purpose

Build an MVP of the unified version-anchored operations machinery, then use it to investigate the operation-semantics slice of the derived-artifacts problem. The goal is to determine whether that slice contains useful constraints rather than merely tautologies. The MVP combines a calibrated one-cycle closing review of the full pass, counterfactual carry judgments with rationale, an observation log, and a variance control arm. It uses shipped machinery wherever possible. Running it on real passes supplies the observations needed to locate constraints.

The investigation starts from several candidate semantic invariants: operations bind exact states; evidence kinds remain distinct; transformations stale prior assessments; and process history cannot be acknowledged onto new bytes. Stated abstractly, these claims verge on tautology: “judgments about old bytes don't bind new bytes.” Any useful content is therefore likely to lie in the exceptions and protocol rather than in the invariants themselves:

- under what conditions evidence may be **carried** across an edit (acknowledged) rather than recomputed, and who may carry it;
- what independence carrying requires so that a transformer does not certify its own transformation;
- why systems default to unanchored booleans (`reviewed: true`) anyway — whether that failure mode has a mechanism worth a note or is just sloppiness;
- which operations should **not** acquire freshness state at all, because a currency signal is itself certification-shaped.

If worked cases show the invariants are purely definitional, the honest close is *no* extracted notes — the proposal keeps them as inline rationale and this workshop records why.

## Working stance

Brainstorm on the solution side and harden on the constraint side. Keep design decisions open until doing so makes the system cumbersome in daily use; architectural tidiness alone is not a reason to close them. The MVP decides only what its construction forces, using the lightest reversible representation available, such as existing review machinery and plain log files.

Solution sketches — trust dials, footprint declarations, audit sampling, typed transformations — accumulate and compete here without becoming commitments. The essential deliverable is the constraint list: which constraints apply to *any* solution, and which are merely assumptions or tautologies. A concrete observation provides provenance but does not locate a constraint by itself. To do so, it must discriminate the constraint from plausible explanations based on judge variance or representation choice. Conversely, non-occurrence discharges a candidate only when the probe could have exhibited the failure. Once a decision hardens against located constraints, it follows the proposal → ADR path.

## Boundary with lineage-mechanisms

[lineage-mechanisms](../lineage-mechanisms/README.md) owns the general derived-artifact lineage vocabulary and the available storage weights: in-artifact, event surface, and operational store. This workshop owns the kinds of claims that operations make — verdict, routed evidence, attestation, successor state, and process fact — and the closure that a transforming workflow owes its assessments. Route storage-escalation questions there; route claim-semantics and closure-protocol questions here. Neither workshop should restate the other's conclusions.

## Candidate worked cases

These cases are starting points from the review that opened the workshop. The live investigation determines their order and may replace them. They are constraint-locating probes, not adoption trials: a probe may incidentally improve an instruction, but its purpose is to produce evidence.

1. **Full-pass closure.** The semantic-bundle acceptance written at step 5 of [run-full-improvement-pass-on-note.md](../../instructions/run-full-improvement-pass-on-note.md) becomes stale after the edits in steps 8–9. The review database already detects this. What the instruction lacks is a closure step that re-runs the review — or, eventually, acknowledges its result — against the final text. The MVP adds the minimum result-kind and retention machinery needed to test this step honestly, then runs a calibrated one-cycle closing review with a variance control arm. See [mvp-plan.md](./mvp-plan.md) for the build list and [unified-diff-and-ack.md](./unified-diff-and-ack.md) for the design rationale.
2. **Human review anchoring.** This case asks whether human attestation can be represented as another factored `(note, contract)` pair, following the ADR 038/041 pattern but with a human actor or partition. It also asks what, exactly, such an attestation certifies. The cheapest semantically adequate representation should decide the design; see [factored dependency pairs](../../reference/proposals/factored-dependency-pairs-for-review-freshness.md). Part 5 of [mvp-plan.md](./mvp-plan.md) deliberately selects a representation only after the closure experiment and outside MVP completion; construction follows selection. The surviving constraints call for one **force-free** attestation under a human partition: “the user recorded that they reviewed these bytes,” not the already endorsement-shaped “accepts.” The attestation is anchored and queryable but licenses nothing, and it requires explicit byte confirmation (`--reviewed-hash`) rather than an after-the-fact echo. This is a separate architectural probe, not a reuse of the acceptance store, which requires completed review-pair evidence. The wider space of attestation kinds and forces — skimmed, approved, claims-verified, each licensing different actions — remains deliberately undesigned. Any attempt in practice to stretch the single kind locates a requirement.
3. **Routed reports: anchor and watch.** The original framing presumed a do-not-anchor rule: giving critique or friction reports freshness state might re-create certification semantics through the back door. The broader design in [unified-diff-and-ack.md](./unified-diff-and-ack.md) turns that presumption into an experiment with a sharp licensing distinction. A calibrated closed-ended assay acceptance may license skipping a re-run; a fresh open-ended assay record licenses only reusing the report as current evidence. The MVP tests the anchored path through critique alone. Compression, friction, and connect are rerun directly, and the friction gate's “For the human” routing is never silenced. The case asks whether downstream consumers nevertheless read a current-critique signal as “critiqued and handled.” If they do, the do-not-anchor rule becomes located rather than assumed.
4. **Trajectory-aware closure audit (post-MVP probe).** The [agent-as-a-judge framing](https://x.com/aparnadhinak/status/2075688574960488558) suggests that evaluating only the final output can miss failures within an agent trajectory. After the MVP produces real histories, compare a fresh judge given the closure trajectory with a control shown only the final note and closing results. Calibrate the comparison through human spot checks and repeated runs. This is a protocol meta-evaluation, not another **note assay**: it asks whether retained process evidence materially improves detection of closure errors, without assuming that the external analogy already establishes the result for Commonplace.

## Working files

- [carry-heuristics.md](./carry-heuristics.md) — candidate constraints for safe carry and the trust-but-check sketch the MVP will test
- [unified-diff-and-ack.md](./unified-diff-and-ack.md) — the broader design: closed-ended and open-ended questions share freshness machinery but carry different licenses
- [mvp-plan.md](./mvp-plan.md) — the critique-only anchored vertical slice, five-method closing experiment, manual controls, and post-observation decision gates

The closed-ended/open-ended taxonomy classifies independently anchored questions, not necessarily entire instruction files. Hybrid procedures need separately factored records before either license can apply. The current exact-byte surface also covers only self-contained questions. When an assay follows evidence into linked artifacts, those dependencies must also be anchored before the unified freshness claim can extend to them.

## What closes this workshop

- The MVP exists and has been used on real passes: closing review in the full-pass procedure, counterfactual carry judgments with rationale, observation log with variance control.
- Each candidate constraint (in [carry-heuristics.md](./carry-heuristics.md) and later files) is either located by an observation that discriminates it from the main confounds, or discharged by a probe capable of exhibiting its failure.
- The solution space is mapped against the located constraints, with sketches recorded as options, not choices.
- The tautology question is answered: extracted notes that meet the quality bar (they change how someone builds a KB), or an explicit conclusion that the invariants are definitional and stay inline in the proposal.
- The located constraints and surviving sketches are distilled into the appropriate durable artifacts; decisions then proceed on the proposal → ADR path where machinery is warranted.

---

Relevant material:

- [Run a full improvement pass on one note](../../instructions/run-full-improvement-pass-on-note.md) — tests: the one real composite workflow; first closure trial target
- [Factored dependency pairs for review freshness](../../reference/proposals/factored-dependency-pairs-for-review-freshness.md) — draws-on: the keep-it-small default a human-attestation pair would extend
- [History has one chance to become checkable](../../notes/history-has-one-chance-to-become-checkable.md) — grounds: the state-judgment vs. process-fact split the claim-kinds taxonomy rests on
- [Criteria edits invalidate verdicts; process edits invalidate artifacts](../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) — grounds: existing invalidation semantics any extracted note must not merely restate
- [Reasoning production is not reasoning evaluation](../../notes/reasoning-production-is-not-reasoning-evaluation.md) — draws-on: why a trajectory judge must inspect the actual route rather than reconstruct a plausible result
- [An outcome check licenses replay; a rule needs the process verified](../../notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md) — draws-on: the process-vs-outcome distinction tested by the trajectory-aware control
- [Agent Harness for Large Language Model Agents ingest](../../sources/agent-harness-large-language-model-agents-survey.ingest.md) — evidence: durable local support for trajectory rather than string-output evaluation
- [lineage-mechanisms](../lineage-mechanisms/README.md) — see-also: peer workshop owning storage weights and the general lineage vocabulary
