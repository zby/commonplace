# Genre-drift cohort: the hypothesis is refuted, and a better claim replaces it

Scored 2026-08-21 from the 23 run readouts in [adr-066-test-runs.md](./adr-066-test-runs.md). The question, as the workshop README posed it: *do keep-reframes systematically move claims from causal/ontological to diagnostic/procedural framing?* When it was written, two or three reframes had run and all of them drifted.

## The tally

Of 23 runs, 16 changed a title. Six were plain keeps at the existing path (runs 4, 10, 12, 16, 19, 23), and run 11 was a merge whose source was deleted rather than renamed. No run was excluded for missing titles, though three old titles survive only as truncated filename slugs (runs 7, 15, 22); their genre is unambiguous from the surviving text.

Coding each title move as DRIFT (toward diagnostic/procedural), NO DRIFT (genre unchanged), or COUNTER (toward causal/ontological):

- **DRIFT: 5** — runs 1, 2, 3, 9, 18
- **NO DRIFT: 5** — runs 6, 7, 14, 15, 17
- **COUNTER: 3** — runs 8, 13, 20
- **Lateral, into CONDITIONAL, which the three-label scheme does not cover: 3** — runs 5, 21, 22. Forced into the scheme they read COUNTER, giving 5/5/6.

Drift is a minority under either coding: 5 of 16, against 11 that hold genre or move the other way.

## Why this refutes the hypothesis rather than leaving it open

"Systematically" is the load-bearing word, and three clean reversals defeat it. Run 20 turned an ontological identity ("storing LLM outputs *is* constraining") into a scoped causal claim; run 8 turned a causal claim ("can turn tools into hidden schedulers") into an ontological one ("remains scheduling behind a tool interface"); run 13 turned a normative imperative ("reinforce facts at point of use") into a refuter-bearing predictive comparison. A machinery-wide attractor toward diagnostic/procedural framing would not produce those, nor the five genre-preserving repairs alongside them.

Two things make the drift column weaker still.

**The coding is sensitive at the margin.** Runs 9 and 18 land on "does not certify" and "do not establish" — negative universal epistemic claims. Read as denials inside the causal/ontological family rather than as diagnostics, DRIFT falls to 3 of 16, and all three (runs 1, 2, 3) sit in wave 1, the exact window the hypothesis was generalized from.

**The original count had no denominator.** The README recorded "two keep-reframes", run 2's readout called itself "third instance for the cohort thread", and `third-episode-criterion-note-reframed.md` independently calls itself "third case" for the same thread — the pre-wave count was both uncontrolled and internally inconsistent, because only drift-positive cases were being counted. Runs 5 through 23 supply the missing denominator and it is large.

What survives is narrower: all three uncontested drift cases are notes about KB and authoring method, where "analysis should separate" is a natural landing. The runtime, storage, and prompt notes did not drift. A weak domain-specific tendency is compatible with this corpus; a machinery-wide one is not.

## The claim that fits the data

**Reframes systematically trade universality for conditions and negations. Genre movement is a byproduct of where the surviving warrant sits, not an attractor.** Fifteen of the sixteen title changes narrow scope, add a condition, or weaken strength while keeping the claim's kind:

- *Conditions hoisted into the title:* run 5 ("when required evidence fits"), run 21 ("when they suppress fallback search"), run 22 ("until write invariants stabilize"), run 3 (scoped to the consumption path).
- *Actor or quantity narrowed:* run 8 (cross-task transition policy only), run 14 (harmful retained inflow, not gross throughput), run 17 (model-resolved indirection only), run 7 (distinct rather than independent).
- *Strength weakened to a limiting or negative form:* runs 1, 6, 9, 15, 18, 20.

Run 13 is the single exception, and it moves to a *stronger*, more testable claim by adding a comparator and a refuter.

Six of the sixteen landings are negative or limiting universals. That is the cohort's largest single cluster, and it is exactly the shape a counterexample-driven repair produces: a defeated universal survives as a claim about what its evidence does not license.

The series verdict already names the mechanism, arrived at independently — "large-radius foundational notes state universals whose defeats are counterexamples, and counterexamples route scope and category repairs." `instance`-shaped defeats cannot license a mode conversion, so they route scope and category repair; genre follows the warrant. Runs 19 through 23 produced no `prevalence` and no `priced-exception` shapes at all, which is why those runs cluster so tightly on conditionalization.

## What this does to the episode record's story

[episode-record.md](./episode-record.md) proposed the causal story behind the original hypothesis: "question-framings survive better than causal framings because a diagnostic question cannot be false", and "the installation's goals made diagnosis the attractor". The cohort falsifies the second half — diagnosis is not the attractor. The first half survives in weakened form, with a different subject: what survives review is the negative or conditional framing rather than the question framing, and it survives for a related but distinct reason. It states less, so there is less for a counterexample to reach.

That weakened claim is not free of the original worry. A repair that buys survival by stating less is the failure mode [narrowing bought to survive review is paid for in content](../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) already names, and the refuter and citer guards exist to price it. The cohort says the guards are being applied to the right thing — condition-and-negation trades, not genre — and that no run in the series bought survival with vacuity, since run 3 was blocked from re-hedging and run 13 moved upward.

## Status

**Closed.** The question is answered: refuted as posed, replaced by the conditionalization claim above, which is itself a restatement of the series verdict rather than a new finding needing its own evidence. No promotion is proposed — the transferable content is already carried by the narrowing note and the series verdict.
