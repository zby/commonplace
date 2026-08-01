# Premise-cohort replication results

**Protocol decision: REOPENS.** The 49-row legacy premise sample has **44 adverse rows** (89.8%): 29 stable majorities other than C1 and 15 UNSTABLE rows. This is above the frozen run's 10-row boundary, so phase B must not be approved from the current premise ledger. The two-sided 95% Wilson interval for the adverse share is 78.2%–95.6%.

**Interpretive conclusion:** the historical `grounds-baseline:P` ledger is not sufficient evidence for a mechanically registered premise cohort. The run does **not** establish that 44 individual rows are semantically non-premise, that `premised-on` is an unusable relation, or which successor each row should receive. It therefore blocks the proposed migration but does not reverse or replace the premise theory.

The experiment omitted semantic positive controls for C1 and forced semantic relations, representation choices, and observation insufficiency into one single-choice taxonomy. It can reject approval under its own pre-registered reproducibility gate; it cannot distinguish a mixed historical cohort from systematic premise undercalling or information loss between observer and mapper. The [post-run audit](./post-run-audit.md) records these and the execution-level limitations.

## Primary gate details

- Only after all mapper records were frozen did the orchestrator reveal that neutral class C1 is the proposed `premised-on` semantic class.
- Sample: 49 of 155 surviving `grounds-baseline:P` rows, selected by the frozen digest rule.
- C1 unanimous: 0; C1 stable 2/3 majority: 5.
- Stable alternative majorities: C2×11, C4×9, C13×4, C10×3, C3×1, C5×1.
- UNSTABLE: 15; patterns: `C1/C11/C2`×1; `C13/C3/C4`×1; `C13/C5/C8`×2; `C13/C2/C5`×1; `C1/C2/C4`×1; `C13/C2/C4`×2; `C1/C2/C3`×1; `C12/C3/C9`×1; `C1/C11/C13`×1; `C10/C2/C4`×1; `C2/C3/C8`×1; `C2/C3/C4`×1; `C10/C11/C13`×1.
- Adverse definition: stable majority other than C1 or UNSTABLE; observed 44/49 = 89.8%.
- Fixed decision: **reopens** (10 or more adverse rows).

The fixed decision rule is broader than the reversal condition in the original grounds review. That review proposed reversal if roughly 20% of P rows instead triggered design/rule reconsideration; this protocol counted every non-C1 class and every unstable row as adverse. Only C4 directly represents design dependence, and nine primary rows had a stable C4 majority. `REOPENS` is therefore the correct result under this run's frozen gate, but it is not a literal satisfaction of the earlier, narrower reversal condition.

The full row-level ledger, including every mapper vote, observer edge judgment, confidence, cohort, prior disposition, and source/target tuple, is [case-ledger.tsv](./case-ledger.tsv). Raw observer and mapper event streams remain under `raw-observer/` and `raw-mapper/`; frozen stage records are under `observations/` and `mappings/`.

## Secondary cohorts

### Boundary corrections (8 rows)

| source → target | mapper votes | result |
|---|---|---|
| `notes/linking-theory.md → notes/agents-navigate-by-deciding-what-to-read-next.md` | C8 / C2 / C3 | UNSTABLE |
| `notes/linking-theory.md → notes/title-as-claim-enables-traversal-as-reasoning.md` | C2 / C3 / C2 | stable-majority → C2 |
| `notes/linking-theory.md → notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md` | C2 / C2 / C2 | unanimous → C2 |
| `notes/linking-theory.md → notes/title-as-claim-makes-overlap-between-notes-visible.md` | C2 / C2 / C2 | unanimous → C2 |
| `notes/pointer-design-tradeoffs-in-progressive-disclosure.md → notes/agents-navigate-by-deciding-what-to-read-next.md` | C4 / C2 / C13 | UNSTABLE |
| `notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md → notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md` | C3 / C3 / C5 | stable-majority → C3 |
| `notes/short-composable-notes-maximize-combinatorial-discovery.md → notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md` | C13 / C13 / C13 | unanimous → C13 |
| `notes/title-as-claim-enables-traversal-as-reasoning.md → notes/agents-navigate-by-deciding-what-to-read-next.md` | C3 / C2 / C2 | stable-majority → C2 |

### Prior drift cohort (5 rows)

| basis | source → target | mapper votes | result |
|---|---|---|---|
| `grounds-drift:G009` | `notes/constraining-and-extraction-both-trade-generality-for-reliability.md → notes/exact-implementation-does-not-validate-a-requirement.md` | C11 / C13 / C13 | stable-majority → C13 |
| `grounds-drift:G001` | `notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md → notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md` | C4 / C2 / C13 | UNSTABLE |
| `grounds-drift:G002` | `notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md → notes/self-improvement-is-relative-to-a-declared-objective.md` | C1 / C13 / C13 | stable-majority → C13 |
| `grounds-drift:G014` | `notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md → notes/warranted-autonomy-is-bounded-by-oracle-domain.md` | C13 / C1 / C1 | stable-majority → C1 |
| `grounds-drift:G016` | `notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md → notes/exact-implementation-does-not-validate-a-requirement.md` | C1 / C4 / C2 | UNSTABLE |

The five prior drift rows were previously classified `premised-on`; only one now has a stable C1 majority, two are UNSTABLE, and two have stable C13 majorities. This is a cross-runtime disagreement diagnostic, not a change to the primary denominator.

### Negative controls (16 rows)

| prior disposition | rows | majority classes | C1 majorities |
|---|---:|---|---:|
| `explained-by` | 4 | UNSTABLE×2, C4×1, C2×1 | 0 |
| `operates-through` | 4 | C3×2, C4×1, UNSTABLE×1 | 0 |
| `extends` | 4 | UNSTABLE×2, C3×2 | 0 |
| `evidenced-by` | 4 | C6×2, UNSTABLE×2 | 0 |

No negative control received a C1 majority (0/16), so the pipeline-discrimination veto is not triggered. All control-level disagreements remain in the ledger.

## Observer-versus-mapper diagnostics

Observers returned 234 valid records: mechanically-discoverable×155, connective-prose-only×79 edge-disposition judgments and high×199, medium×34, low×1 confidence judgments. Mappers returned 234 valid class mappings with distribution `C2×59, C4×41, C13×40, C3×28, C1×20, C10×15, C5×9, C8×6, C6×6, C11×5, C12×2, C9×2, C7×1`.

Observers were not asked to choose a taxonomy, so this comparison is diagnostic rather than a second class score. At case level, observer edge majority versus mapper majority/instability was:

| mapper result | observer edge result | cases |
|---|---|---:|
| C1-majority | connective-majority | 1 |
| C1-majority | mechanical-majority | 5 |
| mapper-unstable | connective-majority | 12 |
| mapper-unstable | mechanical-majority | 14 |
| non-C1-majority | connective-majority | 9 |
| non-C1-majority | mechanical-majority | 37 |

The observer stage had no `no-useful-connection` records; 79/234 were `connective-prose-only` and 155/234 mechanically discoverable. These are exposed as residual semantic/format diagnostics, not converted into C1 scores.

## Robustness and non-conclusions

The migration block is not an artifact of the two mapper retries. Thirty-eight of 49 primary rows received no C1 vote, and ten were unanimously mapped to non-C1 outcomes. Replacing the two scored retry batches with every valid first-attempt record, using retry output only for the missing or malformed record, produces 45/49 adverse primary rows and still 0/16 C1-majority negative controls.

The exact alternatives are much less stable than the absence of C1. Fifteen primary rows and 26 of all 78 rows were UNSTABLE; the three mapper passes also used C13 at markedly different rates. Consequently:

- the result is strong enough to stop a migration premised on the old ledger;
- it is not a row-level replacement manifest;
- stable C13 (`connective prose only`) is a representation decision, not evidence that no premise relationship exists;
- C15 (`insufficient observation`) is an epistemic state, not a semantic relation;
- no conclusion about premise sensitivity follows because the run had no known-positive C1 cohort.

## Blindness, provenance, and leakage audit

Scored participants were label-blind, outcome-blind, production-contract-file-blind, catalogue-file-blind, and prior-ledger-file-blind by packet construction. They received fresh contexts and stage-specific fixture files. The exact ambient instruction set was not captured: processes were launched with their working directory at the external fixture root, which contained no `AGENTS.md`, and no trace read the Commonplace root. The protocol's stronger claim that repository-root governance remained ambient is therefore unsupported; system/developer instructions and installed skill descriptions remained possible ambient context. Filesystem isolation was **not enforced**: the fixture root was outside the checkout and the read-only sandbox prevented writes, while reads were prompt-restricted and trace-audited. Observer traces found 443 command events, all against `packets/`; mapper traces found 12 command events, all against `observations/`. No unexpected production-file read was observed.

The artifact bodies themselves retain substantive prose that sometimes names ordinary relation vocabulary (for example, `grounds` or `extends`) or discusses link semantics. Those words were not footer annotations and were retained under the frozen transformation rule; this is a residual lexical exposure, so the result is not a claim of vocabulary-free perception. No participant saw the orchestrator manifest, cohort names, tuple paths, or prior classification by design.

Requested model was `luna`; the CLI endpoint rejects that bare alias for this account. Every scored pass instead used and reported the verified configured model ID `gpt-5.6-luna`. Provenance, return codes, durations, and stdout/stderr digests are in `pass-provenance.jsonl`; the two malformed mapper attempts and identical-prompt retries are recorded in [amendments.md](./amendments.md) and `parse-failures.json`.

## Scope and next action

The result is a reproducibility boundary failure for the sampled legacy premise cohort: the current `grounds-baseline:P` assignment does not survive independent Luna observation-and-mapping under this packet/context. Maintainers should not approve phase B from the current ledger. They should neither delete the premise relation nor reclassify rows from this output.

The next evidence step is the [premise-relation discriminability experiment](../premise-relation-discriminability-experiment.md). It first tests known premise positives and close counterexamples, scores semantic relation separately from footer registration, and compares direct classification with the observer-to-mapper pipeline. Only a calibrated instrument should return to untouched historical rows. This run does not authorize migration, edit corpus edges, alter collection contracts, or change the shared catalogue.
