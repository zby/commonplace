# Episode record: the three-way-diagnosis note as Popperian maintenance

Reconstructed 2026-08-19 from git history, the full-pass report, and `kb/log.md`. The subject is `kb/notes/llm-output-deviation-requires-three-way-diagnosis.md`, formerly `llm-output-deviation-has-three-sources-with-non-substitutable.md`.

## Timeline

| Date | Commit | Event |
|---|---|---|
| 2026-08-05 | `ffd5c7d7` | Note promoted from the tag README as a synthesis note: "LLM output deviation has three sources with non-substitutable remedies" |
| 2026-08-05 | `982a018f` | "Interpretation error" renamed to "interpreter failure", grounded in the executor-conformance bracket |
| 2026-08-08 | `39176adb` | Retained intent separated from model capability; the fixed-assembled-input scoping seed |
| 2026-08-18 | pass `20260818T132531Z-e11d99` | Full improvement pass: two premises GLOBAL-defeated, disposition keep-reframe, body rewritten around three diagnostic questions |
| 2026-08-18 | `af8feccf` | Rename executed via `commonplace-relocate-note`; citer reconciliation (two stale summaries, one overclaim) |
| 2026-08-19 | `d2f1048f` | Worked comparison settles the analytic-versus-operational residual; masking separated from repair via a perturbation test |

## Act 1 — the bold conjecture (2026-08-05)

The original note made an ontological claim with exclusive structure: deviation "has one of three causes," each "a property of a different part of the system"; "each standard remedy acts on exactly one of the three objects, so it cannot repair a failure located in another"; and "the three claims are about three different objects, which is why the taxonomy is not a list of observed symptoms but a decomposition of the pipeline." High unification: one principle (one remedy per object) organized the whole remedy space.

## Act 2 — refutation and guarded reframe (2026-08-18)

The full pass did not soften the note for style; its premise-decomposition gate defeated two load-bearing premises with concrete counterexamples:

- **Exact one-object action — DEFEATED.** Few-shot examples, schemas, and stricter formatting instructions often leave intended meaning unchanged yet sharply reduce out-of-`V` violations, so a "spec narrowing" edit also repairs interpreter behavior.
- **Best-of-N as pure sampling control — DEFEATED.** Best-of-N needs a chooser; once a selector prefers one sample, the procedure imports error correction or preference encoding.

The composition-friction gate independently found "three different objects" UNSUPPORTED by the note's own setup: interpreter failure and indeterminism are both properties of `D`. Two premises survived an active counterexample hunt — the three loci stay genuinely distinct once `I`, `V`, `D` are represented separately, and checkers cannot reject valid-but-unwanted outputs without encoding the missing intent. The disposition was keep-reframe: "the warranted claim is a three-question diagnosis with non-substitutable primary repair targets, not three mutually exclusive causes."

The reframe ran under both guards from [narrowing bought to survive review is paid for in content](../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) — their second application, and they discriminated rather than firing on everything. The refuter test passed: the new title keeps an independently identifiable subject, and a two-question-suffices result or a fourth in-pipeline relation would refute it (the KB even holds a two-source rival in `llm-debugging-starts-with-retry-versus-rewrite-triage.md`). The citer test caught two summaries still asserting the defeated "properties of different objects" premise and one "only error correction addresses this source" overclaim.

The pass also flagged, without settling, an analytic-drift residual: non-substitution had weakened from "acts on exactly one object" to "primary target" plus "does not guarantee," and if remedies are identified by their primary targets while "complete repair" means "repairs the primary defect," the supporting claim drifts toward true-by-construction.

## Act 3 — re-earning empirical content (2026-08-19)

The follow-up closed the residual with a worked comparison rather than another qualifier, and writing it produced a discovery the original never had: besides repair (the intervention reaches the defective relation) and failure to reach it, an intervention can **mask** a defect — lowering temperature concentrates `D` on an admissible point inside `I` while `V` stays wide. Masking is separable from repair by perturbation: a masked defect returns when its masking condition lapses; a repaired relation does not. That test is what makes non-substitution empirical rather than definitional. The refuter test caught the draft's own overclaim in the process — "restores acceptable behavior only if it reaches the defective relation" is refuted by the note's own temperature example.

## Analysis

**Content accounting.** By the KB's own measure — a claim's content is what it forbids — the final note plausibly forbids *more true things* than the original: two-question sufficiency, a fourth in-pipeline relation, remedy substitution as complete repair, masked defects surviving perturbation. The original forbade more overall, but some of its prohibitions were false. What was genuinely lost is **unification**, not content: the one-principle elegance of "one remedy per object." "Worse as an explanation" conflates those two losses; only the second occurred, and it is a real cost.

**Three drivers, in sequence.** (1) *The domain* supplied the refutation — the counterexamples are true in any installation; messy domains that will not support clean exclusive ontologies are where honest inquiry retreats to the operational level (medicine's diagnostic categories are the standing precedent, with the DSM as the standard example of reliable-but-explanatorily-sterile). (2) *The machinery* chose the landing place: "reframe to the strongest claim the artifact warrants" is a warrant-now standard, and question-framings survive it better than causal framings because a diagnostic question cannot be false. The guards catch emptiness, not genre drift — a claim can pass the refuter test and still have changed kind from ontology to procedure. (3) *The installation's goals* made diagnosis the attractor: the pass's warranted-contribution section derived its reader as "an agent or maintainer choosing how to diagnose and repair," which is this KB's decision-support purpose reaching into the reframe.

**The road not taken.** Physics keeps refuted-in-detail models as idealizations — first-order models with declared validity domains and estimable corrections. The disposition vocabulary (`keep | delete | merge | rehome`, reframe as a keep variant) has no such option, so "each remedy acts on one relation, to first order, with these named cross-effects" was not a survivable form; the crisp model persists only informally as "primary target." This gap is what the promoted proposal makes explicit.

**Not off-model, but close to the line.** The reframed note is still truth-apt and still on the theory side of the design-proposal/claim distinction — its distinctive choices are defended as correct, not merely workable. It is methodology-shaped theory, like measurement theory, not an instruction: it adds no ordering, defaults, or stopping conditions. But the middle of the episode shows the reframe *initially did* cost explanation, and only deliberate extra work bought it back. The safe generalization is not "methodology framings are fine" but "methodology framings are acceptable when they re-earn empirical content at the operational level — and the guards that force that are load-bearing."

## Sources

- `kb/reports/full-pass/llm-output-deviation-has-three-sources-with-non-substitutable/20260818T132531Z-e11d99/full-pass-report.md` — the pass packet: premise verdicts, friction joints, disposition rationale, open items
- `kb/log.md` — the two FIX entries recording the guard application and the worked-comparison closure
- git history of both filenames (the `commonplace-relocate-note` rename breaks `--follow` at `af8feccf`)
