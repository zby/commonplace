# Divergence in reflective self-improvement

## Goal

Determine when non-convergent improvement processing becomes a failure mode in reflective self-improving systems, which mechanisms are specific to reflection, and what kind of episode closure lets improvement remain open-ended across the system's lifetime without consuming the work it exists to improve.

The motivating distinction is:

> A system may remain indefinitely improvable; an improvement episode must still yield control.

This workshop starts from the hypothesis that convergence is often the wrong completion criterion. Open-ended objectives admit further candidates indefinitely, revisions can reveal or create new concerns, and a reflective system can revise the search, evaluation, retention, or stopping machinery that would otherwise provide a fixed point. The failure is not the continued existence of possible improvements. It is failure to govern that non-convergence relative to the system's declared objective, assessment horizon, and opportunity cost.

## Why a separate workshop

The existing KB contains several local treatments but no single cross-system account:

- [Automated note refinement as a search over a fixed source bundle](../../reference/proposals/automated-note-refinement-as-search-over-source-bundle.md) treats split, drift, and kill as legitimate search outcomes and makes budget plus incumbent survival load-bearing stopping rules.
- [Full improvement pass closure](../../reference/full-improvement-pass-closure.md) reassesses the final artifact once, preserves residual findings, and stops without claiming convergence.
- [Machinery persists by warrant, not position, in a reflective loop](../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) argues that reflection removes the stable external meta-method: governance and reversibility stand in for a free fixed point.
- [Gödel machines are a proof-governed case of reflective self-modification](../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) makes the allocation problem formal: a rewrite is adopted only when switching is provably preferable to continuing the search.
- [Traversal improvements should be deferred via logging](../../notes/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md) separates noticing improvement opportunities from interrupting object-level work to pursue them.
- [Improvements can accumulate without compounding](../../notes/improvements-can-accumulate-without-compounding.md) identifies how fixed human attention can limit the scale or duration of compounding, but does not ask whether a computational improvement episode itself returns.

The adjacent [self-improvement-cluster operationalization workshop](../self-improvement-cluster-operationalization/README.md) concerns how the existing theory gains force in Commonplace changes. This workshop owns the narrower unresolved theory problem: how improvement processing diverges and how an episode closes.

## Evaluation boundary

Do not infer a universal convergence requirement from the motivating cases.

- Distinguish a system's open-ended lifetime from a bounded improvement episode.
- Distinguish continuing candidate production from revision drift, oscillation, criterion drift, and failure to yield control.
- Treat failure as objective- and horizon-relative. A long improvement episode can be rational when its expected value exceeds returning to operation.
- Compare reflective and non-reflective improvement. Generic optimization can fail to terminate; reflection's proposed increment is that the loop can move its own target, evaluator, search policy, update surface, or stopping rule.
- Separate direct-update pathways from proposal-selection pathways. Both may diverge, but their observable traces and controls need not match.
- Do not treat a final artifact or successful task as evidence that the improvement process was healthy. Inspect the trajectory, resource allocation, stop decision, and displaced object-level work.
- Treat the Yegge account as one retrospective practitioner report, not causal proof or prevalence evidence.

“Divergence” is working vocabulary. The workshop should replace it if the cases resolve into mechanisms that do not share enough structure to support one term.

## Initial questions

1. What is the episode whose closure is being judged, and what event returns control to ordinary operation?
2. Which non-convergence cases are productive search, and which impose enough opportunity cost to count as failure against the declared objective?
3. Does reflection add a distinctive failure mechanism, or merely enlarge the ordinary search space?
4. Can an active episode revise its own evaluator, scope, budget, or stop rule without making its completion evidence circular?
5. Must some episode boundary remain fixed during a run even if it is revisable between runs?
6. What observable signature separates useful continued improvement, diminishing returns, oscillation, scope expansion, and runaway meta-work?
7. Which controls transfer across systems: fixed budgets, incumbent survival, marginal-value tests, phase boundaries, deferred queues, rollback, or an adoption decision outside the active revision?
8. Can a retained improvement to defect-finding make termination harder by discovering further defects faster than the system resolves them?

## Working artifacts

- [Problem map](./problem-map.md) — provisional distinctions, mechanism sketch, cases, controls, predictions, and promotion candidates.

Add case material and rival explanations to the problem map until one thread becomes large enough to need its own file. External snapshots belong in `kb/sources/`; this workshop should link them rather than copy them here.

## What closes this workshop

The workshop closes when:

1. the umbrella “divergence” has been decomposed into a small set of discriminable mechanisms or rejected as unhelpful;
2. at least three cases spanning more than one improvement architecture have been mapped with their evidence limits;
3. the reflection-specific increment has been stated and tested against a non-reflective counterexample;
4. episode closure has been separated from artifact convergence and from permanent cessation of improvement;
5. at least one design claim about budgets, yield rules, frozen-within-episode machinery, or governance has been promoted, rejected, or explicitly deferred for lack of evidence; and
6. any durable result has been extracted into `kb/notes/`, with descriptive or procedural consequences routed to `kb/reference/` or `kb/instructions/` as appropriate.
