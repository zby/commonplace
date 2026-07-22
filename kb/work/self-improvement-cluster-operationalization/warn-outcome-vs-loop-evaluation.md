# The `warn` outcome vs. the loop's evaluation criterion

Ledger item from the [workshop framing](./README.md), analyzed 2026-07-21. The analysis is complete; the deciding evidence is local-only (`kb/reports/fixes/`, the commonplace store), so **the empirical check at the bottom must run on a machine that has the review data**. Nothing here is resolved until it does.

**Parked 2026-07-22.** The check is postponed rather than blocking: phase 0's rule forbids only *silent* ambiguity, and this item is now explicitly held open with both candidate readings and the decision rule written down. Until the check runs, phase 1 treats the review-system and fix-pipeline artifacts as conditional — audited under both readings or deferred — while every other artifact's audit proceeds normally.

## The collision

The [proposal-selection loop note](../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) sets a strict criterion for evaluation: the verdict must control an operation *distinct from producing the next candidate* — select, discard, block, roll back — and it explicitly excludes the near-miss: "a conditional trigger whose only effect is to launch the next variation is not [an evaluator] either." Rejection and merely-changing-again must be different events in the mechanism. (This clause is what keeps the Homeostat outside the subtype.)

The [review system](../../reference/README-REVIEW-SYSTEM.md) produces `pass`/`warn`/`fail` verdict outcomes, but:

1. **It evaluates incumbents, not candidates.** Every reviewed note is already committed, linked, loadable — already operative. No outcome changes that: a `warn` (even a `fail`) note keeps full behavioral authority. No discard, block, or roll-back operation is wired to any outcome.
2. **`warn`'s only consumer is the fix pipeline.** `commonplace-warn-selector` → fix queue → edited note. The sole operation the verdict controls is producing the next candidate — exactly the operation the theory says does not count as rejection.
3. Finalization writes a freshness baseline for `warn` and `fail` outcomes too — acceptance-like bookkeeping regardless of verdict (defensible, since a baseline is defined as evidence-pinning rather than endorsement, but the mapping must keep that straight).

So by the loop note's own test, the review gates *as currently consumed* are not evaluation.

## Why it bites (the operational stake)

The phase-1 audit asks, per artifact: which loop function does this implement, and does its oracle warrant it? For the review system the answer flips the guidance:

- If gates are **evaluation**, automating them (model workers — which is what the system does) is the dangerous move: [evaluation must be bought with a warranted oracle](../../notes/false-positive-generation-is-filtered-before-retention.md), and a weak one degrades the KB silently.
- If gates are **search** — mechanized problem-noticing that generates correction candidates — automating them is the cheap, safe move the same note says to make first, because their false positives get filtered downstream.

Same artifact, opposite verdicts from the methodology. Until `warn` is placed, the cluster cannot guide the review system's own evolution.

## Candidate resolutions

**A. Reclassify by consumer (theory unchanged).** The review system is not the loop's evaluation function. Gates are *search* over incumbents, feeding correction candidates into the fix queue. The evaluation event is the human judging the fix diff — [FIX-SYSTEM](../../instructions/FIX-SYSTEM.md) nearly says this: "when the fix produces a diff, reviewing that diff is the judgment step." Retention is the merge; pass-baselines are retention *bookkeeping* (evidence freshness), not acceptance. Consequence to state plainly if adopted: Commonplace currently has no computational rejection for semantic criteria — `fail` is an escalation flag, not a gate.

**B. Extend the theory.** The accept/reject dichotomy is too coarse for maintenance loops that evaluate incumbents rather than candidates; `warn` names a third mechanism — **retain-with-obligation**: the artifact keeps operating while carrying a debt something downstream must discharge or escalate. A genuine amendment to the loop note's evaluation section. It must survive the Homeostat exclusion: the theory must still be able to say why launch-the-next-variation is not evaluation while retain-with-obligation is.

Current lean: **A** — no new ontology, and it matches what the machinery does. But A carries a hidden testable commitment, which is what the empirical check decides.

## The empirical check (run where the data lives)

If gates are search (reading A), their false positives should be routinely **rejected at the fix step** — a fix agent or diff reviewer declining a warn as spurious, recorded as a non-fix. If in practice every warn gets "fixed", the downstream filter is not real, the warn verdict functions as de facto acceptance of the criticism, and reading B is honest rather than generous.

Procedure, on a machine with `kb/reports/fixes/` and the commonplace store populated:

1. Enumerate fix reports: `ls kb/reports/fixes/*.fix-report.md`. Each maps warnings to fix applied, strategy, and status (`fixed` or `deferred`).
2. Count dispositions across all reports: fixed vs. deferred vs. anything recording *rejected / spurious / no change needed*. The fix-report contract only names `fixed` and `deferred` — check whether "this warning is wrong" even has a representable disposition, or gets shoehorned into `deferred`. If it is unrepresentable, that is itself a finding: the pipeline has no rejection vocabulary.
3. Read the deferred cases: are they "warning is wrong" (a real downstream filter — supports A) or "fix is hard / postponed" (no filter — supports B)?
4. Cross-check `fail` outcomes in the store: does any consumer exist (triage records, retirement, demotion), or do `fail` notes simply persist untouched? `commonplace-warn-selector --json` plus the review store's completed verdict pairs give the counts.
5. Optional corroboration: sample a few fixed cases and check whether the diff reviewer ever pushed back (fix report vs. what was actually committed).

Decision rule: a nontrivial rejected-as-spurious rate (or clear deferred-because-wrong cases) → adopt A; write the review-system-to-loop mapping note with gates classified as search, and record the no-computational-rejection consequence. Near-zero rejection → adopt B or repair the pipeline (give the fix step a real rejection disposition) and then re-run the check — note that repairing the pipeline to make A true is also an available move, and arguably the better one, since it adds the missing filter instead of weakening the theory.

---

Links:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — tests: the evaluation criterion the `warn` consumer appears to violate
- [False-positive generation is filtered; false-positive acceptance becomes operative](../../notes/false-positive-generation-is-filtered-before-retention.md) — grounds: why the search-vs-evaluation classification flips the automation guidance
- [README-REVIEW-SYSTEM](../../reference/README-REVIEW-SYSTEM.md) — depends-on: outcome and baseline semantics under analysis
- [FIX-SYSTEM](../../instructions/FIX-SYSTEM.md) — depends-on: the warn consumer, and the diff-review sentence reading A leans on
