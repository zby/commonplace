# Simplifications beyond mechanical offloading

- **Recorded:** 2026-09-29, at the operator's request after a discussion of two commits and similar possible simplifications.
- **Revised:** 2026-09-29, after an agent review of the candidates against the code, the operator's selection, and the implementation of that selection.
- **Status:** five of the six recorded candidates are implemented by [ADR 097](../../reference/adr/097-agentic-analysis-drops-decisions-that-change-no-result.md). This document now holds what remains open: one deferred question, one deferred follow-on, and three larger cuts.

## Direction

Remove decisions whose alternatives have no useful effect on the analysis, especially when later steps must reconcile those decisions. Moving a mechanism into code can make it cheaper and more reliable; changing the contract can make the mechanism unnecessary.

Working statement of the required result: produce a source-grounded account of one frozen target, inspect it through the runtime, memory, and epistemic perspectives, resolve their interactions, independently check the result, and publish an attributable, bounded conclusion.

Most removable flexibility appeared in identity, handoffs, representation, and publication. Much of the necessary flexibility is in evidence and interpretation.

## Disposition of the recorded candidates

The decision numbers are those of the operator's selection on 2026-09-29. The workshop log cites them.

| Recorded candidate | Decision | Disposition |
|---|---|---|
| 1. Write the public synthesis once | 3 | Implemented by ADR 097: code renders the public review from the verified overview |
| 2. Remove the separate scoping job | 1 | Implemented by ADR 097, as one cut with candidate 3 |
| 3. Make memory an ordinary workflow job | 1, 2 | Implemented by ADR 097, including the removal of `worker-model` |
| 4. Use one correction policy across the set | 7 | Deferred; see below |
| 5. Give workflow decisions one explicit representation | 6 | Implemented by ADR 097, narrowed to the form of the Blockers section |
| 6. Normalize source identity once | 5 | Implemented by ADR 097, narrowed to one normalization and one author; removing `review-path` is deferred |

Decisions 1, 2 and 3 were the operator's. Decisions 5 and 6 were agent defaults to which the operator raised no objection. Decision 4 set the timing: everything adopted lands before the second real run.

The findings that supported each change are in ADR 097's Context and Considered alternatives.

## Deferred: correction routing

The recorded candidate 4 proposed one correction policy in which missing evidence returns to the responsible author, with three possible destinations. Only the memory specialist can receive a return today. The runtime and epistemic members are written once. That policy would add two routes.

The option under test is the opposite: no returns. All three members are written once, and the reconciliation's amendments and limitations are the only correction. This would remove the `## Returned to the specialist` branch, the separate memory counter, the `memory-report-<n>` rounds, the rule for the last round, and the correction half of the memory job instruction.

What it surrenders: a specialist cannot redo its analysis inside the run. A finding the reconciliation cannot correct by amendment becomes a limitation, as it already does for the runtime and epistemic members.

Evidence so far is thin. The batch 01 correction turns were structural, and validator retries now cover that case. The content error found in the first real run was in a reconciliation amendment, not in the memory report.

Agent recommendation, not yet an operator decision: keep the return route for the second real run, and remove it if that run makes no substantive return.

## Deferred: removing `review-path`

Two repositories with the same name under different owners get the same run slug and the same review path. Opening refuses the second because the source identities differ, and `review-path` is the only way to proceed. Removing the parameter needs the owner in the slug, and a decision on whether several boundaries within one repository need separate public reviews. Filenames alone cannot settle that requirement.

## More aggressive cuts to defer

| Candidate | Simplification | Capability surrendered |
|---|---|---|
| Static analysis only | Remove dynamic probes and their execution preflight from the ordinary workflow | Direct observations of execution; claims must remain bounded accordingly |
| Failure receipt only | Retain a short receipt for blocked/out-of-scope targets instead of assembling an overview-only set | Uniform artifact shape across successful and unsuccessful runs |
| One source bundle per run | Prepare heterogeneous evidence before opening analysis | Convenient evidence acquisition during boundary work |

These narrow the product's capabilities. Defer them until the surrendered capabilities are shown to be unnecessary. The first would also supersede the workshop's proposed probe runner rather than add another implementation item.

## Preserve

Preserve independent verification, frozen evidence, the distinction between uncertainty and absence, both analytical lenses, and publication consistency checks. Their complexity protects meaningful properties.

Before selecting any further cut, state which decision, handoff, representation, or failure mode disappears, and which useful result becomes impossible. A change to a shipped contract needs a design proposal under the workshop's existing requirement. A bundled method rerun cannot isolate the effect of an individual change.

Related reasoning: [Constraining and extraction can trade generality for reliability, speed, or cost](../../notes/constraining-and-extraction-both-trade-generality-for-reliability.md) and [Progressive constraining commits only after patterns stabilize](../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md).
