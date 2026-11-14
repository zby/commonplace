# Plan: unify the review operations

Written 2026-11-14 for an agent in a later session. The [workshop framing](./README.md) holds the goal, the operator's premises, the shipped constraints and what closes the workshop. This file states the intent, the result wanted and the limits. The method is yours.

## Intent

The operator wants to build one improvement procedure from atoms that are each sound alone, and has chosen the review operations as the first atoms to put in order. The purpose of this work is to let the operator decide, per review operation, how it comes to meet the atom contract or why it stays outside the pool.

A decision is useful to the operator only with its evidence and its unknowns. A tidy scheme that the records do not support is worse than an open question stated precisely.

## Result wanted

`decisions.md` in this directory: one entry per question in the framing, each with a recommendation, the alternatives considered, the evidence, and what remains unknown. Supporting material goes in further files here as you see fit.

The first seven framing questions reduce to three decisions, in this order of dependence:

1. **Form:** per family (compression bundle, the three adversarial reports, connect), whether it becomes a gate, gets a typed report form, or stays outside the pool. This includes whether the bundle is four atoms and a composing step, whether the adversarial reports stay three, and the open duplications.
2. **Result:** what a stored result must carry.
3. **Test:** what must exist before a procedure relies on an operation of each form.

Report to the operator when the form decision is ready. The other two depend on the answer, and you may prepare them but not presume it.

## Limits

- Read anything in the checkout, including `kb/reports/state/`. Write only inside this directory.
- No edits to shipped criteria, types, instructions, code or proposals. No paid review, sweep or worker. No commit unless the operator asks.
- Other sessions edit this checkout. Leave their changes alone.
- Return to the operator at once if a decision cannot be reached without a paid run, if every option you find would break an operation's current user, or if the evidence contradicts one of the operator's premises. Record it; do not act on it.

## Principles to work by

From the [stochastic-operation-testing workshop](../stochastic-operation-testing/README.md). A review operation is model-dependent and its output varies between runs, so these govern what the evidence here can show.

- **Ordinary records first.** The state tree holds hundreds of retained outputs. A trial is warranted only by a question they cannot answer and whose answer changes a decision.
- **Ordinary records carry qualified provenance.** They came from a changing checkout and are not controlled observations.
- **Comparable means the whole configuration matches,** not only the input text.
- **Judge tendencies, not single outputs.** Say so where you rest on one case.
- **Keep apart** finding a case that exposes a failure, estimating how often it fails, and comparing a change with the incumbent. A case chosen because it failed gives no rate.
- **Keep denominators,** including cases that showed nothing. Absence in a small sample leaves the question open.
- **Your own reading is an evaluator too.** Record how you matched or classified, so the operator can check it.
- **Consumers before schema.** The form of a result follows from what its readers used.
- **A recommended trial states its terms:** failure criterion, fixture, evaluator, trial count, budget, stopping rule and the decision it serves.

## What you cannot find out yourself

**The first pilot.** The [gate verdict stability pilot](../stochastic-operation-testing/pilot-gate-verdict-stability-results.md) ran four sweeps of one note on unchanged text on 2026-11-14, on the `sonnet` profile, which was then the default. The operator made `opus` the default the same day, so these figures describe the profile being left; an Opus rerun is not yet done. It covers one note, chosen because it looked unstable, so treat these as constraints on design and not as rates.

- 33 of 44 pairs kept one outcome across four trials; 11 changed, 5 of them warning only once.
- Whether a gate warned varied more than what it flagged when it warned.
- Severity labels inside results vary between runs of one gate (`warn`, `WARN`, `low`, `minor`, `medium`), so a warning-level finding cannot be identified mechanically today.
- An earlier sweep with byte-identical inputs was still not comparable: the profile and model differed, and the prompt wrapper for the conformance pairs had changed in code. The wrapper is outside the hashed inputs.
- One full sweep of one note is 44 launches: about 5.2 USD on `sonnet`, and 11.08 USD in the one `opus` sweep on record (2026-11-12).

**Where the evidence is,** as of 2026-11-14:

| Operation | Instruction | Retained outputs |
|---|---|---|
| Catalog gates, conformance lenses | `kb/instructions/review-gates/` | `kb/reports/state/review/results/`, `runs/` |
| Compression bundle | [compression-bundle/](../../instructions/compression-bundle/README.md) | Inside full-pass run directories |
| Critique | [critique-note](../../instructions/critique-note.md) | 13 files in `kb/reports/state/critique/` |
| Composition friction | [composition-friction-gate](../../instructions/composition-friction-gate.md) | 89 files in `kb/reports/state/friction/` |
| Premise decomposition | [premise-decomposition-gate](../../instructions/premise-decomposition-gate.md) | 67 files in `kb/reports/state/premise-decomposition/` |
| Connect | [cp-skill-connect](../../instructions/cp-skill-connect/SKILL.md) | 808 files in `kb/reports/state/connect/` |
| Higher-order check | `kb/work/higher-order-check-evaluation/wordings/` | That workshop's results files |

The full pass is the main consumer of the non-gate methods: its code is `src/commonplace/lib/review_workflows/full_pass.py`, its runs are under `kb/reports/state/review/runs/full-pass/`, and its packets under `kb/reports/state/review/packets/`.

**Known traps.**

- The [overlap map](../decision-lifecycle-evidence/review-operation-overlaps.md) was read from failure modes only. Two of its proposed merges did not survive a full reading of the tests.
- The compression bundle was kept out of the catalog on purpose. Its stated reason may or may not still hold.
- The higher-order check's wording and calibration belong to [its own workshop](../higher-order-check-evaluation/README.md). Take what its result needs from there.
- Freshness and provenance are different consumers of a result's identity. A field can record how a result was produced without making it stale.

## Left to you

How you inventory the operations, which records you sample and how many, how you compare reports, the layout of your files, and the order of work within each decision. Choose from the evidence as you find it, and state the samples behind any count.

## Report

Outcome first: the decisions you recommend, those you could not reach and why, the samples behind them, and anything in this plan or the framing that proved wrong. Validate each file you write with `commonplace-validate`, one file per call.
