# Transformation closure workshop

## Purpose

The unified version-anchored operations MVP is built and has run on five real full-improvement passes. This workshop now interprets what those runs establish about the operation-semantics slice of the derived-artifacts problem: which results change how Commonplace should operate, which candidate constraints remain unidentified, and which planned machinery did not earn a build decision. The MVP combines a calibrated one-cycle closing review of the full pass, counterfactual carry judgments with rationale, an observation log, and a variance control arm.

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

1. **Full-pass closure — implemented and supported locally.** The semantic and critique evidence written before steps 8–9 becomes stale after the edits. Across five passes, semantic verdicts flipped on 14/23 edited-note reruns and critique materially changed on 5/5; the one-cycle closing review therefore stays in [run-full-improvement-pass-on-note.md](../../instructions/run-full-improvement-pass-on-note.md). It closes the protocol by routing residuals, not by claiming convergence.
2. **Human review anchoring — still independent and unrun.** The closure experiment did not select an attestation representation or provide evidence for building one. The candidate remains one force-free, byte-confirmed, non-licensing fact — “the user recorded that they reviewed these bytes” — but even that is a design constraint awaiting its own probe, not an MVP result. See [factored dependency pairs](../../reference/proposals/factored-dependency-pairs-for-review-freshness.md).
3. **Routed reports — anchoring worked; the categorical license claim did not.** Critique's version anchor was useful because every post-edit rerun materially changed. But all five same-byte critique controls were materially stable, so open-ended question shape alone does not establish that a cached report has no skip value. The MVP conservatively gives critique evidence-currency semantics; whether calibrated open-ended reports can ever license skipping remains empirical. The downstream “current means handled” misuse case was not instrumented and remains untested.
4. **Trajectory-aware closure audit — suggested, not controlled.** The [agent-as-a-judge framing](https://x.com/aparnadhinak/status/2075688574960488558) suggests that evaluating only the final output can miss failures within an agent trajectory. Retained pass histories now make a trajectory-versus-final-output comparison possible, but the earlier trace audit had no blinded output-only control. This remains protocol meta-evaluation, not another **note assay**.

## Working files

- [carry-heuristics.md](./carry-heuristics.md) — candidate constraints the MVP did not locate, plus the now-deferred trust-but-check sketch
- [unified-diff-and-ack.md](./unified-diff-and-ack.md) — the broader design: closed-ended and open-ended questions share freshness machinery but carry different licenses
- [mvp-plan.md](./mvp-plan.md) — the critique-only anchored vertical slice, five-method closing experiment, manual controls, and post-observation decision gates
- [mvp-results.md](./mvp-results.md) — five-pass evidence, constraint status, and the documented no-for-now decision on carry instrumentation

The closed-ended/open-ended taxonomy classifies independently anchored questions, not necessarily entire instruction files. Hybrid procedures need separately factored records before either license can apply. The current exact-byte surface also covers only self-contained questions. When an assay follows evidence into linked artifacts, those dependencies must also be anchored before the unified freshness claim can extend to them.

## Current status

- **MVP and observation phase complete:** result-kind review support, anchored critique, closing cycle, retained reports, five observation logs, and same-byte controls exist; the full test suite passes.
- **Carry instrumentation declined for now:** every counterfactual decision was `would_rerun`, so the experiment produced no plausible carry case, and rerun cost was not measured. Part 4's gate did not open.
- **Candidate carry heuristics remain unidentified:** the passes did not isolate edit direction from size, compositional drift, or the step-9 copyedit footprint. More passes of the same substantive workflow would add volume without testing those claims.
- **Workshop remains open only for an explicit next probe or an honest close:** trajectory-aware evaluation and human attestation are independent candidates. If neither is chosen, the remaining broad heuristics should stay documented as untested and the implemented findings should be distilled before closing.

## What closes this workshop

- The MVP exists and has been used on real passes: closing review in the full-pass procedure, counterfactual carry judgments with rationale, observation log with variance control. **Complete.**
- Each candidate constraint (in [carry-heuristics.md](./carry-heuristics.md) and later files) is either located by an observation that discriminates it from the main confounds, or explicitly retained as unidentified because the probe could not decide it. **Classified in `mvp-results.md`; none of the broad carry heuristics was located.**
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
