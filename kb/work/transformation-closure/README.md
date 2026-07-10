# Transformation closure workshop

## Purpose

Build an MVP of the unified version-anchored operations machinery, and use it to work the operation-semantics slice of the derived-artifacts problem into something non-tautological. The MVP — a calibrated one-cycle closing review on the full pass, carry records with rationale, an observation log with a variance control arm — is assembled from shipped machinery wherever possible; its use in real passes supplies the evidence that locates constraints.

The investigation starts from candidate semantic invariants — operations bind exact states, evidence kinds stay distinct, transformations stale prior assessments, process history can't be acknowledged onto new bytes. Stated abstractly these verge on tautology ("judgments about old bytes don't bind new bytes"). The suspected real content sits in the exceptions and the protocol, not the invariants:

- under what conditions evidence may be **carried** across an edit (acknowledged) rather than recomputed, and who may carry it;
- what independence carrying requires, so the transformer doesn't certify its own transformation;
- why systems default to unanchored booleans (`reviewed: true`) anyway — whether that failure mode has a mechanism worth a note or is just sloppiness;
- which operations should **not** acquire freshness state at all, because a currency signal is itself certification-shaped.

If worked cases show the invariants are purely definitional, the honest close is *no* extracted notes — the proposal keeps them as inline rationale and this workshop records why.

## Working stance

Brainstorm on the solution side; harden on the constraint side; keep design decisions open for as long as keeping them open doesn't make the system too cumbersome to work with. The MVP decides only what building it forces, in the lightest reversible representation available (existing ack machinery, plain log files) — cumbersomeness in daily use, not architectural tidiness, is the trigger for closing a decision. Solution sketches (trust dials, footprint declarations, audit sampling, typed transformations) accumulate and compete here — none is a commitment. The deliverable that must be right is the constraint list: which constraints on *any* solution are real — each located by a concrete observation from MVP use — and which are assumed or tautological. Decisions that harden go the proposal → ADR path, taken only against located constraints.

## Boundary with lineage-mechanisms

[lineage-mechanisms](../lineage-mechanisms/README.md) owns the general derived-artifact lineage vocabulary and its storage weights (in-artifact, event surface, operational store). This workshop owns what kinds of claims operations make — verdict, routed evidence, attestation, successor state, process fact — and what closure a transforming workflow owes its assessments. Storage-escalation questions route there; claim-semantics and closure-protocol questions route here. Neither workshop should restate the other's conclusions.

## Candidate worked cases

Starting points from the review that opened this workshop; the live work decides order and may replace them. These are constraint-locating probes, not adoption trials — a probe may incidentally improve an instruction, but its purpose is evidence.

1. **Full-pass closure.** The semantic-bundle acceptance written at step 5 of [run-full-improvement-pass-on-note.md](../../instructions/run-full-improvement-pass-on-note.md) is staled by the step 8–9 edits, and the review DB already detects that. The missing piece is only a closure step in the instruction: re-run (or ack) against the final text. This is the MVP — a calibrated, one-cycle closing review plus evidence collection (including a variance control arm), before any machinery is designed.
2. **Human review anchoring.** Can human attestation be one more factored `(note, contract)` pair in the existing review store (the ADR 038/041 pattern, human actor/partition), and what exactly does such an acceptance certify? Cheapest representation decides; see [factored dependency pairs](../../reference/proposals/factored-dependency-pairs-for-review-freshness.md).
3. **Negative case: routed reports.** Test the claim that giving critique/friction reports freshness state re-creates certification semantics through the back door. Expected output is a documented do-not-anchor rule, not machinery.

## Working files

- [carry-heuristics.md](./carry-heuristics.md) — carry judgments live in the agent, the system trusts but checks: per (edit-kind, check-kind) safety hypotheses as planning guidance, system-owned baseline diffs, anchored carry records, sampled audits with a variance-calibrated flip-rate trust dial (starting at 100% = always-rerun), and fail-toward-rerun wherever the audit surface is missing

## What closes this workshop

- The MVP exists and has been used on real passes: closing review in the full-pass procedure, carry records with rationale, observation log with variance control.
- Each candidate constraint (in [carry-heuristics.md](./carry-heuristics.md) and later files) is either located — pinned to a concrete observation from MVP use — or discharged as assumed or tautological.
- The solution space is mapped against the located constraints, with sketches recorded as options, not choices.
- The tautology question is answered: extracted notes that meet the quality bar (they change how someone builds a KB), or an explicit conclusion that the invariants are definitional and stay inline in the proposal.
- The located constraints and surviving sketches are distilled into the appropriate durable artifacts; decisions then proceed on the proposal → ADR path where machinery is warranted.

---

Relevant material:

- [Run a full improvement pass on one note](../../instructions/run-full-improvement-pass-on-note.md) — tests: the one real composite workflow; first closure trial target
- [Factored dependency pairs for review freshness](../../reference/proposals/factored-dependency-pairs-for-review-freshness.md) — draws-on: the keep-it-small default a human-attestation pair would extend
- [History has one chance to become checkable](../../notes/history-has-one-chance-to-become-checkable.md) — grounds: the state-judgment vs. process-fact split the claim-kinds taxonomy rests on
- [Criteria edits invalidate verdicts; process edits invalidate artifacts](../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) — grounds: existing invalidation semantics any extracted note must not merely restate
- [lineage-mechanisms](../lineage-mechanisms/README.md) — see-also: peer workshop owning storage weights and the general lineage vocabulary
