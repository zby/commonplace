# Review family and form recommendations

## Decision requested

Approve the family/form recommendations below before finalizing their result contracts and acceptance tests. This is the first checkpoint in the [plan](./plan.md), not an implementation authorization. No paid calls, workers or shipped changes were made for this investigation.

**Recommendation:** unify the atomic review procedures through a common execution contract, without arranging them into larger units. Each atom has explicit file inputs, standalone execution, its own result form, provenance, freshness and independent testing. Begin implementation with existing gates, conformance and critique, then apply the same contract to the remaining admitted atoms. This is implementation sequencing, not a recommended review sequence. Keep the higher-order check experimental under its evaluation workshop. Extend `commonplace-review`; no inspected consumer requires a new command name.

Existing bundles and the full pass are compatibility constraints and sources of evidence only. This workshop does not choose which atoms run together, their order, worker grouping or how their judgments are combined.

| Family | Recommended form | First slice? |
|---|---|---|
| Catalog gates | Individual criterion-level verdicts and applicability | Yes, preserve |
| Type/collection conformance | Existing contract-specific verdicts and exclusions | Yes, preserve |
| Critique | Report with attack outcome and supporting argument; completion is not a favorable verdict | Yes |
| Compression checks | Four independently runnable checks, each with its own result | Later |
| Compression synthesis | Assess separately for admission as a report-producing atom with explicit target and findings inputs; no bundle execution implied | Open |
| Composition friction | Separate report: concretization result plus ranked inferential joints | Later |
| Premise decomposition | Separate report: premises, counterexamples and local/global routing | Later |
| Connect | Separate discovery report under its existing type, not a verdict | Later |
| Higher-order check | Experimental proposal result with kind, force and grounds; preserve its current gate encoding during evaluation | Not catalog admission yet |

“Later” means part of the recommended review pool, not ready for automatic registration. Admission requires adapting output destinations, defining inputs and deterministic validation, and choosing freshness or explicit `unassessed`. It does not require proving every judgment calibrated before execution infrastructure can support it.

## Why these forms

### Keep the three adversarial reports and higher-order check separate

The full instructions assign different searches and products:

- [Critique](../../instructions/critique-note.md) builds the strongest opposing case and checks whether the note answers it. It allows an inspectable **no surviving attack**, including a low-confidence variant. Its question is not whether every premise survived a separate hunt.
- [Friction](../../instructions/composition-friction-gate.md) asks whether the claim's properties can coexist, then tests and ranks inferential joints. Its skeptical default is `UNSUPPORTED`; the concretization result is not an overall acceptance decision.
- [Premise decomposition](../../instructions/premise-decomposition-gate.md) assumes valid inference for the purpose of testing the premises themselves. It hunts counterexamples at the stated modality and records `HOLDS`, `DOUBTFUL` or `DEFEATED`, with failure scope and counterexample shape. It expressly forbids an overall verdict.
- The [current higher-order draft](../higher-order-check-evaluation/wordings/theory-claim.md) asks whether to split, merge, rehome, reject or change the claim. Its parent-loss and collection-placement tests require neighboring content. A correct argument can still belong elsewhere; an attacked premise need not warrant a note-level change.

The retained case below shows shared concerns, not identical products. Critique emphasizes near-constant types as poor routing discriminators; premise decomposition also records the false routing dichotomy and which failures are local or global; friction exposes the unsupported transitions. The higher-order draft was not part of that run. This is evidence of overlap alongside distinct information, not a measurement of complementary detection rates.

**Consumer constraint:** [the full-pass instruction](../../instructions/run-full-improvement-pass-on-note.md) carries friction and premise findings verbatim as routed attention. It does not convert them into passage actions. Critique informs warrant and the strongest-objection decision. Replacing all three with one general critique would remove information these consumers explicitly use.

**Alternative rejected for now:** merge the adversarial methods, or replace them with the higher-order check. Similar subject matter is insufficient evidence of substitutability. A merger would need matched retained targets showing that the replacement preserves the distinctions its consumers need, including non-adverse outcomes. None was established here. Do not interpret separation as a requirement to run every method on every note.

**Higher-order ownership:** its evaluation workshop still owns wording and calibration. Keep proposal kind, force and grounds visible; preserve PASS/no proposal, WARN/weak and FAIL/strong as its existing experimental encoding, not as a mandatory encoding for every report. The [evaluation record](../higher-order-check-evaluation/README.md) reports missed historical cases and reserves held-out cases for the next wording. No new calibration claim or catalog promotion follows from unifying execution.

### Expose the four compression checks as standalone atoms

Reading all four tests and [the synthesis instruction](../../instructions/compression-bundle/high-impact-simplification-synthesis.md) supports distinct responsibilities:

| Component | Question | Product |
|---|---|---|
| Core claim obscured | Is the artifact's supported claim prominent and findable? | Local PASS/INFO/WARN and locations |
| Branch bloat | Does a side claim serve the main argument or belong elsewhere? | Local PASS/INFO/WARN and candidate removal/demotion/rehome |
| Detail overhang | Does useful detail earn its amount, including argumentative force? | Local PASS/INFO/WARN and compression candidates |
| Marginal-value redundancy | What reader work would disappear if a chunk were deleted or folded? | Local PASS/INFO/WARN and deletion/folding candidates |
| Synthesis | Which zero to three substantial changes follow from the artifact and findings? | Opportunities with prerequisites and must-preserve meanings; no independent verdict |

Recommend a standalone instruction, invocation and result for each of the four checks. An operator must be able to run and test any one without running the others or a synthesis. Merely naming four sections in a combined report does not meet that requirement.

Their edit-strategy bias deliberately questions true, defensible material. Preserve their local PASS/INFO/WARN judgments rather than silently translating them into ordinary gate decisions. Sharing the runner does not automatically add them to `--all-gates`.

The synthesis instruction is a separate admission question. If admitted as an atom, it must take the target and an explicitly supplied, self-contained finding set and return opportunities with unresolved authorial choices intact. It must not launch the checks, discover their outputs in shared state or silently require a surrounding bundle. Whether a larger procedure invokes it after any checks is outside this workshop.

**Alternative rejected:** expose only the combined compression operation. That would leave its individual checks unavailable for standalone use and testing, contrary to the workshop goal.

**Compatibility and limits:** the [existing bundle](../../instructions/run-compression-bundle-on-note.md) and full-pass consumer must keep working, but this investigation makes no recommendation about their worker grouping or composition. The retained one-worker report illustrates the checks' products; it does not establish how independently executed checks will behave. Exact per-check result contracts remain conditional on operator approval.

### Connect belongs, but not first

[Connect](../../instructions/cp-skill-connect/SKILL.md) already produces a non-mutating, target-specific [typed report](../../types/connect-report.md). Its product is candidates, rejected candidates and a discovery trace, not authored links or a judgment that the note is acceptable. Empty sections are valid and explicitly say `None`.

It therefore fits the shared review execution boundary without pretending to be a gate. Its input scope is broader: authorized destination collections, their contracts and navigation surfaces, and searched/linked content. The full pass uses its candidates to inform the existing-KB comparison, explicitly not as an exhaustive ownership proof.

**Defer implementation:** the retained report says it could not execute its required validator because the worker had no shell tool. Current `full_pass._methods` checks only that method output is nonempty. Moving connect unchanged into a registry would not establish deterministic report conformance. Run-owned destinations also affect its file-relative links. Both need explicit handling, without giving the worker shared-state access.

**Alternative:** exclude discovery entirely. That would leave a report-only operation used by the same consumer outside the common evidence mechanism for no execution-boundary reason. Include it later, with its corpus dependence stated and freshness initially unassessed unless a defensible policy is adopted. A target-only hash must not imply that its discovery context is unchanged.

## Overlap dispositions after reading full tests

These recommendations concern the named candidates, not a fresh audit of all 40 gates.

| Candidate overlap | Recommendation and reason |
|---|---|
| `prose/proportion-mismatch` / `compression/detail-overhang` | Keep both for now. Proportion compares development of the core against secondary material; detail-overhang tests whether particular useful detail can be shortened without losing its work. They can flag the same passage, but a balanced note can still contain overlong detail, and a thin core may need development rather than compression. |
| `complexity/could-be-a-paragraph` / higher-order parent-loss | Keep both. The catalog test asks whether collapsing section structure loses non-obvious content. Parent-loss asks what remains beyond an existing parent's contribution and can reject elaboration that the catalog test counts as necessary support. One concerns structure; the other concerns separate ownership/existence. Do not retire the catalog gate merely when a higher-order atom becomes available. |
| `prose/redundant-restatement` / `compression/marginal-value-redundancy` | Keep their boundaries. The former checks section-boundary repetition; the latter tests chunks at their presented granularity, including true material not repeated anywhere. A future shared subtest is possible, but replacement would change the targeted review coverage. |
| `sentence/clause-packing` / `sentence/parsing-ambiguity` | Keep both. Dependency load and plausible alternative parsing are distinct even when they occur in one sentence. |
| Sentence checks / `compression/core-claim-obscured` | Keep both. Locally easy sentences do not establish that a document foregrounds its central claim. |
| `complexity/claim-to-section-ratio` / compression checks | Keep both. The former tests whether section structure is justified by distinct claims and necessary support units; the latter can act inside a justified section or an unsectioned note. |

This revises two hypotheses in the [older overlap map](../decision-lifecycle-evidence/review-operation-overlaps.md): detail-overhang is not established as redundant, and the catalog paragraph test is not simply a temporary substitute for parent-loss. No shipped criteria were changed. Full-pass reconciliation already permits collapsing findings when both finding and action are identical; semantic deduplication need not remove the underlying questions.

## Evidence and limits

### Inspection baseline

Checkout HEAD: `8374de1dd28da9388b6a3f175fe1f7af377f322c`. The plan was locally modified when inspected; its SHA-256 was `fa157b869bdf82c4a578b02e35ce335981493a0cd42c120daee974cbf07c90fd`. Inspected instruction, runtime, report-type and adjacent evaluation/decision-workshop files had no tracked diffs when checked. The concurrently modified improvement-procedure proposal was not used to establish current runtime behavior.

Read the complete compression tests, adversarial instructions, connect skill/type, higher-order `theory-claim` draft, named overlap tests and full-pass consumer instruction. Runtime inspection covered `src/commonplace/lib/review_workflows/full_pass.py::_methods`, `results.py::Result` and the report/verdict paths in `criteria.py`/`outcomes.py`. Existing test inspection included report marker rejection in `test_outcomes.py` and full-pass freshness bypass, publication and continuation cases in `test_full_pass.py`. No tests were executed; this is a design checkpoint, not verified implementation coverage.

Current shared results have a Python record containing note/criterion hashes, outcome, profile/model, run and launch. Report completion accepts `REPORT`, not PASS/WARN/FAIL. This does not validate all of critique's required sections. Other full-pass methods currently receive only a nonempty-output check. The shared typed-result gap remains real.

### Retained sample

Recounted Markdown files recursively: 13 standalone critique, 89 friction, 67 premise-decomposition, 808 connect, zero standalone compression-bundle, and 136 shared review results. The full-pass tree held 123 Markdown files, including inputs and outputs, and one `artifact/start.md`; those are not 123 trials.

Sample selection: use the single retained full-pass case because it has all five report methods over identical captured target bytes. The standalone stores had no three-way intersection after stripping `.critique.md`, `.friction.md` and `.premises.md` from filenames. Filename matching alone would not establish target-version equality anyway. No favorable-only or warning-only filtering was applied to the selected run.

Run root, relative to the repository:

`kb/reports/state/review/runs/full-pass/kb/theory/types-give-agents-structural-hints-before-opening-documents/3fe0a68b3910/`

Each locator below is under `calls/launches/` in that root:

| Method | Launch / output | Observed report, not independently verified truth |
|---|---|---|
| Compression | `fe24068adc134f5dbfd30c58abc4ba17/outputs/report.md` | Core INFO, branch PASS, detail PASS, marginal-value WARN; one synthesis opportunity preserving the author's thesis choice |
| Critique | `ee3a330d62144a4db422efd273ab1b2a/outputs/review.md` | Attack partially lands: type adds little discrimination where nearly constant; scope and trait distinctions remain |
| Friction | `e6e43e4de102468db3d813f76a1f4ef6/outputs/report.md` | SURVIVES; one UNSUPPORTED and four THIN joints |
| Premises | `4643c7119c0d4685a00559c92fd14df2/outputs/report.md` | Eight premises: three HOLDS, four DOUBTFUL (one described as close to defeated), one DEFEATED; local/global routing retained |
| Connect | `b9a285d7e2ce4808a6089e6dca021efe/outputs/report.md` | Candidate links and maintenance observations; empty off-authorization, raw-text and synthesis sections; validation explicitly not run |
| Proportion gate | `b1cbd1adcc964c3a9cd5db25254b4b2d/outputs/review-proportion-mismatch.md` | PASS with an INFO observation about emphasis |

All five report launches' `inputs/note.md` have SHA-256 `3fe0a68b3910f29f1cfa9d267064142fabbddb9a9348e514bd179871862e098b`. The run's `sweep.json` requests Claude Code, Opus, medium effort, with Bash disallowed. Target bytes and requested profile match; operation instructions deliberately differ. Effective model versions, tool readiness and surrounding KB reads were not compared. The evidence does not establish independent information gain, success rates, or superiority of one method. The two compression PASS entries and three held premises remain in the denominator; they were not dropped as uninteresting.

A case-insensitive literal search for `no surviving attack` in the 13 standalone critique files and 136 current shared results found no matching file. This is not proof that the outcome never occurred: these are incomplete, replaceable stores and older reports may use other wording. The honest-empty outcome is established by the current instruction, not demonstrated by this sample. No all-empty connect report was sampled either.

### Two operator retirement cases, not a rate

Fable, the session responsible for the first improvement run and overlap map, supplied follow-up evidence through the operator on 2026-11-15. The two cases must remain distinct:

1. **Structural hints:** the retained full-pass target above was deleted in `bbc5ef0a47d364b18a17a67ce53df03303091370`. The commit records that the pass handed it back as `revise`, while the operator chose deletion: routing was carried by title and description, and the added conditions were owned by the verifiability and enforcement notes. Critique, friction and premise decomposition had all run; none of those three reports proposed removal. Their forms have no dedicated note-removal disposition. That does not prevent a critique from discussing redundancy, but it does mean these reports do not replace an existence judgment.
2. **Two context boundaries:** the [first improvement run](../decision-lifecycle-evidence/first-run.md) target was retired in `278b35ae57bea4eec92e3dc4b52ead9a198a2099`. The commit records the operator's judgment that the general claim was arithmetic and the remaining content described Commonplace. The run record reports that no gate or higher-order wording proposed retirement. No adversarial report had been run on this target, so this case cannot establish what those methods would have found.

These are two selected cases, not a frequency estimate. They support keeping argument criticism distinct from the question of whether a note warrants separate existence. The higher-order check is the candidate dedicated owner of that latter atomic judgment; its wording and evaluation remain with its workshop. Neither case establishes that the current wording solves it. Existing full-pass disposition remains a consumer behavior, not another atom designed here.

## Consumer requirements supplied by Fable

These are reported costs and workarounds from actual use, received through the operator on 2026-11-15, not an adopted schema. They constrain the next contract design. Fable also accepted the two overlap-map corrections; no change to that other workshop was made here.

| Consumer need | Evidence and cost | Contract requirement to carry forward |
|---|---|---|
| Repeat one wording without changing its identity | [Third calibration round](../higher-order-check-evaluation/third-results.md), “Keeping the two runs apart”: the second trial changed `gate_id` to `higher-order/direct-tests-repeat` to avoid replacing the first result. The changed id was visible to the worker. | Separate execution identity from criterion identity. Retain each execution after current-result replacement. A repeat must not require changing worker-visible wording or using a second criterion id. |
| Execute a draft criterion | The same round's setup used `COMMONPLACE_LIBRARY_ROOT` pointing to a scratch library. Fable reports this as the workaround for uncommitted wordings. This investigation has not established that it is the only possible current route. | Support an explicit supplied draft without catalog promotion; retain its exact bytes, hash and origin separately from the KB commit and execution id. Do not require a scratch library solely to give a draft an identity. |
| Read individual findings mechanically | Fable reports manually transcribing 50 results and being unable to extract INFO findings mechanically. The [first-run record](../decision-lifecycle-evidence/first-run.md) also records omitted INFO findings. | Expose each finding and its level, separately from the result's overall outcome, for forms that have levels. Preserve no-finding results. Do not force report forms without severity levels to invent them. Exact representation and validation remain open. |
| Cite a retained launch output | [Improvement-run findings](../../reports/types/improvement-run-findings.md) cites run, launch and output hash, not the replaceable current result. Fable reports that all 220 stored results checked on 2026-11-14 had bodies identical to their launch outputs; that historical count was not independently reproduced here and is not the current inventory above. | Keep the actual launch-output path and exact-byte SHA-256 citable, including the existing `calls/launches/<launch>/outputs/review.md` path where used. Structured findings must not silently rewrite the retained raw output or make existing citations unusable. Other workflows may have different output filenames. |
| Reuse captured target text | [Improvement-run](../../reports/types/improvement-run.md) currently stores start and edited texts by SHA-256. Fable asks whether retained review inputs can replace duplicate copies. | Recommend that the review execution own the exact target capture it supplied. An improvement run may cite that capture when the hash matches and retention is guaranteed; it owns edit-produced texts not yet captured by a review. Do not remove existing copies until the retention and reader contracts support this. |

**Ownership is not worker access.** A durable reference can avoid a duplicate evidence copy; it cannot authorize a worker to traverse another run. The launcher must still supply self-contained run-local operational inputs. Such execution copies are deliberate, even when the authoritative retained evidence has one owner. The next contract must define retention for referenced captures before a consumer drops its own copy.

Fable's observation/retry clarification in the plan was included in commit `de994f027`; it is no longer an outstanding uncommitted edit in this workshop. The promised pointer from the overlap map remains for Fable to add in that workshop.

## Conditional next work, not finalized contracts

If the operator accepts these forms:

1. Specify the first slice around gates/conformance and critique, reusing the existing command and Workjig route. Do not make connect or the higher-order check a prerequisite.
2. Reconcile target capture and launch citations with [improvement-run](../../reports/types/improvement-run.md) and [improvement-run-findings](../../reports/types/improvement-run-findings.md). These already retain full texts by hash and cite launch outputs by hash rather than the replaceable shared result. Preserve that identity chain; a copied input carries its original identity but must contain everything the worker needs. A citation is not permission to traverse another run.
3. Keep whole-text capture hashes distinct from the gate store's watched-parts freshness hash. One preserves supplied bytes; the other deliberately ignores some changes. Finalize uncommitted instruction/code identity and effective configuration alongside the run record, not through a second provenance scheme.
4. Record one observation per execution, with retries/resume inside it. Keep independent trial records separate and link them where needed; build no aggregation or voting.
5. Finalize schema ownership, validation, freshness and compatibility tests only after this disposition. Quality evaluation remains separate: verdict forms need labelled judgments and repeatability evidence; adversarial reports need assessed attacks and misses, including honest empty findings; compression needs assessed recommendations and preservation of necessary content; connect needs assessed candidate validity and bounded recall evidence. None follows merely from valid output files.

The command sketch remains provisional. No inspected consumer establishes a need for `commonplace-operation`; retaining `commonplace-review` avoids migrating its full-pass, revise and publication consumers solely for naming. The next design step must still inspect the complete caller surface before fixing a compatibility plan.

**Stopped at the family/form checkpoint.** Approve, reject or amend the table and overlap dispositions before dependent result/test recommendations are finalized. No new experiment is needed to choose this conservative separation; evaluation of a proposed semantic merger would be a separate commission.
