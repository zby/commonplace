# Bounded test: resource or program when the executor can interpret

**Status:** designed 2026-10-31, not run. This file is the protocol record for the run; a research-evidence commit cites it. Results go to `kb/reports/retained/` with the exact launch record, as the [calibration pilot](../../reports/retained/analysis-calibration-pi-luna-low-20261010/README.md) did.
**Owner of launch, judging and integration:** the operator or a coordinating session. Workers are single-use.

## Question

When the executor can interpret, does operationalized knowledge act as a resource consulted at breakdowns rather than a program followed step by step? Two predictions from the [exploration](./exploration.md) make this testable.

- **P2 (method detail can harm).** Under late-arriving evidence, a step-fixed script does worse than the same method supplied as purpose and bounds, with the same executor and the same evidence available.
- **Suchman (section 6.6).** In the resource arm, the executor consults the method at breakdowns and supplies the rest from judgment. The method does not drive the sequence of decisions.

Both are conjectures. The test is designed so that each can fail.

## Fixed task T

**Objective.** Build the strongest case that a KB note's central commitment is wrong, and report whether it survives. This is the assay that [critique-note](../../instructions/critique-note.md) already defines, used here as the task, not as the method.
**Admitted cases.** Eight `kb/theory/` notes selected by the coordinator. Four carry one inserted defect each. Four are unmodified supported controls.
**Success criterion.** A faulty case counts as detected when the report names the inserted defect as its strongest surviving objection or as a surviving objection. A control counts as accepted when the report finds no surviving objection or only objections the note already answers. A control blocked on an objection the note does not answer is recorded as disputed, not scored.
**Authority.** Report only. No edits to the KB. One call per case, no retries.

## Fixed method K

The Popperian criticism method the KB already holds: seek the test the claim could fail, check that an experiment's contrast matches the attribution it names, and separate origin from corroboration. Its retained sources are the [epistemic stance](../../reference/epistemic-stance.md), [an experiment identifies only the contrast it actually runs](../../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md), and the origin-is-not-corroboration rule in [`kb/theory/COLLECTION.md`](../../theory/COLLECTION.md). K is fixed by commit hash at launch.

## Fixed executor E and setting S

One model at one effort level, pinned by identifier in the launch record. Fresh context per case. Read access to the repository at the pinned commit. The same tools in every arm. Filesystem restrictions are instruction-only, as in the pilot; the record says so.

## Three arms

The arms differ only in what accompanies T. Everything else is identical bytes.

| Arm | What the worker receives beyond T | What it tests |
|---|---|---|
| A0 bare | T and the logging rule | The outcome level without K. Not an effect of K. |
| A1 resource | T, the logging rule, and K as purpose and bounds: what a refutation attempt is, what the contrast check asks, when to stop. No ordering, no mandated steps. Framed "use as needed". | K supplied in a form the executor interprets |
| A2 script | T, the logging rule, and K rendered as a numbered procedure with a fixed order, a fixed source order, a mandated stop point, and the sentence "do not deviate from these steps" | K supplied in a form the executor follows |

A2 is derived from A1 by adding ordering, defaults and stopping conditions and nothing else. That is the `operationalized-from` transformation of ADR 054, so the A1–A2 contrast measures that operation. The treatment grain is the bundle "ordering plus mandate plus stop point"; the plan does not attribute any difference to one of them.

The A0–A1 contrast is "K present" as a bundle with its delivery slot and added length. It is reported as such.

## Case construction: late-arriving evidence

The four defects come in two kinds, two of each.

- **In-path defects.** Visible from the note's own text under the script's prescribed reading: a contrast named finer than the experiment ran, or a corroboration claim whose source is the claim's origin.
- **Off-path defects.** Visible only through a lead the script does not prescribe and stops before: the note's claim is contradicted by the Limitations section of an ingest it cites, or by a note two links away. The script's fixed source order ends at the note's own footer.

P2 predicts A1 and A2 detect in-path defects alike, and A2 detects off-path defects less often than A1. The controls are matched to the faulty cases on length and link count, as the pilot matched its pairs.

The answer key, the defect insertions and the pairing are written and committed before launch. The coordinator writes them; no independent review of the key is planned, and the record will say so.

## Logging rule, identical in every arm

The worker appends a decision log to its report. Each consequential decision gets one line: which source to open, when to stop, what counts as the strongest objection. Each line carries one label.

- `method`, with a verbatim quotation from the supplied method text that the decision followed. A1 and A2 only.
- `judgment`, when no supplied text settled it.
- `tool`, when a deterministic tool settled it.

A `method` label without a quotation, or with a quotation that does not bear on the decision, is rescored as `judgment` by the judge. Self-report is weak evidence; the tool trace is the primary record of which sources were opened and in what order.

## Measures

| Measure | Source | Bears on |
|---|---|---|
| Detection per faulty case, acceptance per control | Blind judge against the answer key | P2 |
| Decisive lead followed or not, per off-path case | Tool trace | P2 mechanism |
| Count of `method`, `judgment`, `tool` after rescoring | Decision log plus judge | Suchman |
| Order of decisions against the order K states | Decision log and trace, A1 only | Suchman |
| Deviation from the script | Trace, A2 only | Suchman, from the other side |
| Tokens and elapsed time | Launch tool, where supplied | Cost |

The judge is a fresh worker that receives the report, the answer key and the scoring rules, and nothing about the arm. Judging is report-only.

## What would refute each prediction

- **P2 is refuted** if A2 detects off-path defects as often as A1 across the four cases, or if A1 loses detection on in-path defects that A2 keeps. Either result says the script did not exclude the late lead, or the resource form cost precision.
- **The Suchman reading is refuted** if A1's decisions are mostly `method` after rescoring and follow K's stated order without a mandate. That would mean the resource acted as a program anyway, and the distinction has no behavioural content for this executor.
- **Both can survive and still mean little.** Eight cases and three arms cannot support a rate. The result is a discriminating observation, retained for the next test, not a measured effect.

## Budget and stop conditions

Twenty-four worker runs plus eight judge runs. Stop and report if a worker edits the KB, if more than two runs fail to complete, or if the answer key is found wrong during judging; a wrong key voids the affected pair, not the run.

## Decisions left open until launch

- Which model and effort, and whether a second, weaker executor is run as a replication. A replication tests executor-relativity, which section 0 claims and this plan does not.
- Which eight notes. The coordinator chooses after writing the defect kinds, so that off-path defects are genuinely off the script's path.
- Whether the judge sees the decision log. Seeing it helps rescoring and risks bias toward the arm's framing; the launch record states the choice.

## Closure

The run closes this workshop's open predictions P2 and the Suchman question with one retained observation each, or refutes them. P1, P3, P4 and P5 are not touched. The workshop's [closure rule](./README.md#closure-rule) still applies: a surviving prediction is retained in the exploration as corroborated once, not promoted.
