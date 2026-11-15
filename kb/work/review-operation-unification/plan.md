# Plan: design the unified review subset

Handoff dated 2026-11-14. Read the [framing](./README.md) for scope and premises and the [execution design](./execution-design.md) for selected requirements. The purpose is to turn those requirements into a bounded implementation recommendation, supported by actual operations and consumers.

## Deliverable and checkpoints

Write `decisions.md` here. For each decision below, state the recommendation, alternatives, evidence locators, sample selection, unknowns and affected consumers. Supporting files are optional. A precise unresolved question is preferable to an unsupported tidy scheme.

1. **Family membership and form.** Decide which operations enter the pool and what instruction/result contracts they need. Check whether compression is four atoms plus synthesis, whether critique/friction/premise decomposition remain distinct from each other and from the higher-order check (all four question a note's central commitment), whether connect belongs, and whether apparent duplicates operate at different scales. Inspect full tests and actual consumers, not just failure-mode descriptions. Uniform execution is not a reason to merge semantic tasks.
2. **Shared record and execution requirements.** Choose ownership and fields for captured targets, self-contained operational inputs, provenance, completed results and trial history. Resolve uncommitted instruction/code identities and effective harness configuration. Specify each operation's freshness policy or explicit absence of one. State how a stored result records the number of trials behind it; the stability premise does not make one run sufficient. Reconcile target capture with the evidence contract of the improvement-run types under `kb/reports/types/`, which already store note texts and cite review launch outputs by hash, so that there is one provenance design and not two. Assess the [command sketch](./operation-command-sketch.md) against existing callers; do not design a second runtime. A new command name needs a consumer that extending `commonplace-review` cannot serve.
3. **First slice and acceptance.** Choose a bounded implementation slice and tests; prefer the easier case first (critique already runs through the review command, while connect depends on the whole corpus and has the hardest freshness) unless the evidence favors another. The tests are those demonstrating the execution contract without claiming calibrated judgment. Include uncommitted-target reconstruction, missing-input handling, independent trials, interrupted/retried work, latest-result replacement and existing-consumer compatibility. Separately state the evidence each result form needs before a procedure relies on its judgments.

**Checkpoint:** return the family/form recommendations and stop for the operator's disposition before finalizing dependent result contracts and tests. Shared provenance requirements can be investigated in parallel with that analysis; retain dependent alternatives as conditional. Workjig execution, the review-only scope and the run-local input boundary are already selected, not questions to reopen by default.

## Authority and stop conditions

- Read the checkout, including ignored operational evidence. Write only in this workshop directory.
- No shipped criteria, types, code, instructions or proposal edits; no paid runs or workers; no commit unless requested.
- Leave other sessions' changes alone. Record inspected versions where concurrent changes could affect conclusions.
- Return immediately if a necessary question requires a paid run, every viable option breaks an existing consumer, or evidence contradicts an operator premise. Record the blocker rather than silently changing the commission.

## Evidence to start from

| Evidence | Use and limit |
|---|---|
| [Review operation overlaps](../decision-lifecycle-evidence/review-operation-overlaps.md) | Candidate duplications. Two proposed merges did not survive full test reading; do not treat the map as an adopted merger plan. |
| [Compression bundle](../../instructions/compression-bundle/README.md) | Explains its deliberate exclusion from `--all-gates`; decide whether the reason still applies. |
| [Higher-order check evaluation](../higher-order-check-evaluation/README.md) | Result requirements such as proposal kind and force; its workshop owns wording and calibration. |
| [Verdict stability pilot results](../stochastic-operation-testing/pilot-gate-verdict-stability-results.md) | Four Sonnet sweeps on one selected note: 33/44 pairs unchanged, 11 changed; variable severity vocabulary and prompt-wrapper/model mismatches. Not population rates or an Opus calibration. The note was retired later that day (commit `278b35ae5`); its text is recoverable from the commit the pilot names. |
| [First improvement run](../decision-lifecycle-evidence/first-run.md) | One case for the family decision: the run's target note was retired because its claim, stated generally, was trivial and the rest was local. No gate and no higher-order wording proposed that; no adversarial report had been run on it, so the case does not show whether one would have. |
| [Provenance reconstruction results](../stochastic-operation-testing/provenance-reconstruction-results.md) | Two Opus calls on one gate, exact input reconstruction and differing advertised MCP tools. Not a repeated full-sweep stability study. |

Operational evidence locations, inventoried on 2026-11-14; recount before making sampling claims:

| Operation | Locations |
|---|---|
| Gates and conformance | `kb/reports/state/review/results/` and `review/runs/` |
| Critique | Shared review results/runs through the `critique` lens; also 13 standalone files under `kb/reports/state/critique/` |
| Compression | Full-pass run directories |
| Composition friction | 89 files under `kb/reports/state/friction/`; full-pass runs |
| Premise decomposition | 67 files under `kb/reports/state/premise-decomposition/`; full-pass runs |
| Connect | 808 files under `kb/reports/state/connect/`; full-pass runs |

Inspect `src/commonplace/lib/review_workflows/criteria.py`, `results.py` and `full_pass.py` for current behavior. Full-pass runs and packets are under `kb/reports/state/review/runs/full-pass/` and `kb/reports/state/review/packets/`. The typed-result gap in the framing must be checked against current code, not assumed solved because the criteria are typed.

## Evidence discipline

Use existing records first. State which configuration dimensions match, deliberately differ or remain unknown. Distinguish a failure-exposing case from a frequency estimate and from a repair comparison. Keep denominators, including empty findings, and describe your matching/classification method so the operator can inspect your evaluation. Single-case support stays single-case support.

A proposed new trial must name its failure criterion, fixture, evaluator, trial count, budget, stopping rule and decision consequence. Do not launch it under this plan. No broad literature survey or fixed sample size is required; choose further investigation only where it can change a decision.

## Return

Lead with recommendations and blockers, then evidence and limits. Validate each written file with `commonplace-validate`, one file per call. After operator dispositions, a separate implementation commission can act on the first slice; this plan does not authorize implementation by reaching its final step.
