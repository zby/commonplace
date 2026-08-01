---
description: "Use to determine whether premise is an operationally distinguishable relation before reassessing historical grounds rows"
type: kb/types/instruction.md
---

# Calibrate the premise relation before reclassification

**Status:** design draft. Do not dispatch scored cases until the maintainer approves the operational contract, fixture truth table, and decision gates. This experiment changes no corpus link, collection contract, catalogue entry, ADR, or prior ledger.

## Why this experiment comes next

The [premise-cohort replication](./premise-cohort-replication/results.md) correctly returned `REOPENS` under its frozen gate, so the existing ledger cannot authorize the `grounds` migration. It did not decide whether premise is a usable relation because it had no known-positive premise controls and its mapper chose once among outcomes on three different axes:

1. semantic relation (`premise`, explanation, operation, evidence, and so on);
2. representation (`mechanically discoverable edge`, connective prose, or no connection);
3. epistemic state (`insufficient observation`).

A premise relationship can be real but too weak or local to register as a footer edge. An observation can also be insufficient without implying any particular relation. The next run must separate those judgments.

This is an instrument-calibration experiment, not a second vote over the historical cohort. Its primary question is:

> Can fresh Luna contexts recover known premise relationships and reject close non-premise relationships under an explicit operational contract, and does the observer-to-mapper pipeline preserve that distinction as well as direct classification?

## Candidate operational contract

The source artifact A is **semantically premised on** target artifact B exactly when all of these conditions hold:

1. A makes a theoretical assertion whose truth or declared applicability is under review.
2. B supplies a proposition, not merely an artifact, process, observation, definition, or available resource.
3. A's argument imports that proposition as an assumption or condition.
4. Rejecting or materially qualifying B is itself a reason to reopen whether A holds or applies.

The relation does not require deductive entailment. It does require more than topical relevance, historical influence, evidential support, or a useful explanation.

Use one semantic axis throughout the run:

| neutral class | semantic relation |
|---|---|
| S1 | premise |
| S2 | explanation |
| S3 | design dependence |
| S4 | operation |
| S5 | prerequisite |
| S6 | target supplies evidence for source |
| S7 | source supplies evidence for target |
| S8 | development or specialization |
| S9 | exemplification |
| S10 | definition |
| S11 | contrast or incompatibility |
| S12 | another substantive relation, named by the participant |
| S13 | no substantive relation |

These classes all answer the same semantic question. Registration and insufficient information do not appear in this table.

### Nearest boundaries

| competing relation | decisive difference from premise |
|---|---|
| explanation | B answers why or how A holds; rejecting B reopens the account, not necessarily A's truth |
| design dependence | A is a design, rule, description, procedure, or system-definition artifact; rejecting B prompts reconsideration or redesign rather than reassessing a theoretical assertion |
| operation | B participates in producing A's effect or behavior |
| prerequisite | B must be true, available, or completed before A works, without being imported into A's theoretical argument |
| evidence | B corroborates, qualifies, or bounds A without being required for A to hold |
| definition | B fixes the meaning of a term A uses rather than supplying a premise of A's argument |
| development or exemplification | one artifact develops, specializes, or instantiates the other rather than supplying a required proposition |
| connective association | the local journey is useful but the claimed dependence is absent or too weak to assert |

### Independent registration judgment

Semantic classification does not decide whether to create a formal link. Record registration on a separate axis:

- **R1 — mechanically registered:** the distinction changes a recurring follow/skip decision or a revision route enough to warrant a queryable footer edge;
- **R2 — connective prose only:** the local relationship helps this argument but does not earn a reusable mechanical edge;
- **R3 — no useful connection:** neither a substantive traversal nor a maintenance route is present.

For R1, the participant must state both consumers:

- what a reader of A gains by following B rather than skipping it; and
- what at A should be reconsidered if B is rejected or materially changes.

Record **insufficient information** as a status flag before either axis. It is not a semantic or registration class.

## Competing explanations

The calibration distinguishes four explanations for the replication result:

- **Cohort mixture:** the premise contract is recoverable on controls, while the historical P ledger mixed several relations or registration strengths.
- **Unusable contract:** even explicit premise positives cannot be separated reliably from near misses, so `premised-on` should be revised, collapsed, or abandoned before any corpus work.
- **Pipeline loss:** direct classifiers recover the distinction, but mappers cannot recover it from frozen observer records; the prior replication measured information compression rather than premise semantics.
- **Registration failure:** premise is semantically recoverable, but formal-edge worthiness is not; the relation may exist without earning a registered identifier under the two-consumer test.

## Freeze a 36-case calibration set

Create 36 short, self-contained artifact pairs whose gold truth table is approved before scored dispatch:

- 12 premise positives covering explicit assumptions, applicability conditions, and imported theoretical commitments;
- 18 close semantic negatives: three each for explanation, design dependence, operation, prerequisite, evidence, and definition;
- 6 association controls covering development/exemplification, connective prose, and no useful connection.

Assign six premise positives to R1 and six to R2. Among the 24 non-premise cases, assign six to R1, six to R2, and 12 to R3. The complete set is therefore balanced at 12 cases per registration class, and neither axis can serve as a shortcut for the other.

Construct at least 12 minimal-pair families. Within a family, keep topic, endpoint shape, length, and vocabulary as similar as possible while changing the decisive relationship. Do not use the disputed `grounds-baseline:P` rows as positive controls. Synthetic cases are allowed because this phase tests whether the supplied contract can be applied; they are normative fixtures, not evidence that the relation occurs naturally in the corpus.

For every case retain:

- neutral case ID;
- Artifact A and Artifact B;
- gold semantic class and registration class;
- the exact sentence or inference that makes the gold answer true;
- the rejection/change counterfactual;
- the nearest tempting wrong answer and why it fails;
- whether the case is synthetic or corpus-derived;
- content and packet digests.

The maintainer approves the truth table, not merely the case text. Cases that reasonable maintainers cannot assign before model execution are boundary research, not controls; move them to an unscored diagnostic appendix.

## Run two matched arms

Use the same 36 cases, model identity, sanitized packets, class definitions, output schema, and three recorded randomization seeds in both arms. Each case receives three independent judgments per arm. Launch every pass in a fresh context with no prior outputs.

### Arm D — direct classification

The classifier sees Artifact A, Artifact B, the neutral semantic definitions, and the separate registration definitions. It returns:

1. `sufficient: true|false`;
2. one semantic class when sufficient;
3. the decisive rejection/change counterfactual;
4. one registration class when sufficient;
5. the reader follow/skip consequence;
6. the revision consequence;
7. confidence and a short rationale grounded in both artifacts.

This arm tests whether the operational contract itself is recoverable when no observation bottleneck intervenes.

### Arm O→M — observation followed by mapping

The observer sees only Artifact A and Artifact B, not the taxonomy or gold answer. It records:

1. A's relevant assertion and whether it is theoretical, descriptive, or prescriptive;
2. the proposition, process, observation, definition, or resource B contributes;
3. whether and how A imports B;
4. what rejecting B changes about A's truth, applicability, explanation, design, or operation;
5. the reader's follow/skip decision;
6. the revision consequence;
7. whether a formal edge, connective prose, or no connection appears warranted;
8. confidence and evidence from both artifacts.

Freeze all observations. A fresh mapper then sees only one randomized observation batch and the same semantic and registration definitions used in Arm D. It records sufficiency, semantic class, and registration class separately. Do not let the mapper reopen artifacts.

This arm tests whether the staged apparatus used by the replication preserves enough information to apply the contract.

## Neutralization and leakage controls

Use neutral semantic IDs and keep the mapping to relation names outside participant context. The definitions necessarily expose the distinctions being calibrated; this is intentional conformance testing, not discovery. Withhold:

- gold outcomes and rationales;
- case-family membership;
- historical cohort membership and replication results;
- production identifiers, contracts, catalogue text, and prior ledgers;
- another pass's output.

Snapshot the actual ambient context and launch command. If the fixture runs outside the repository, install an explicit fixture-root `AGENTS.md` or record that repository governance is absent; do not infer ambient exposure from the orchestrator's context. Retain the exact fixture builder as a script before dispatch and independently randomize mapper order rather than inheriting observer order.

## Pre-registered calibration gates

Score the premise predicate as the primary semantic outcome. Exact recovery of the other semantic classes is secondary; an explanation-versus-operation disagreement does not count as a premise false positive when both votes are non-premise.

Within each arm, aggregate three votes per row as unanimous, stable 2/3 majority, or UNSTABLE. The arm passes semantic calibration only if all conditions hold:

- at least 10 of 12 premise positives have a premise majority;
- at least 22 of 24 non-premise cases have a non-premise majority;
- no more than 4 of 36 rows are UNSTABLE on premise versus non-premise;
- no more than 2 of 36 rows have majority `insufficient`.

The arm passes registration calibration only if:

- at least 10 of 12 R1 cases have an R1 majority;
- at least 10 of 12 R2 cases have an R2 majority;
- at least 10 of 12 R3 cases have an R3 majority;
- no more than 4 of 36 rows are UNSTABLE on R1/R2/R3.

If pilot review removes or replaces a case, restore these exact balances and freeze the replacement before scored dispatch. Do not alter gates after outputs exist.

## Decision table

| direct semantic arm | staged semantic arm | conclusion |
|---|---|---|
| pass | pass | premise is operational under both apparatuses; corpus transport may be tested |
| pass | fail | observer-to-mapper compression is unfit; the prior replication cannot decide premise semantics |
| fail | pass | investigate leakage, arm mismatch, or an invalid gold set; issue no semantic conclusion |
| fail | fail | premise is not operational under this contract; revise, collapse, or retire it before corpus work |

Registration is adjudicated independently:

- semantic pass + registration pass: the candidate relation and its formalization rule are both testable;
- semantic pass + registration fail: premise may be coherent, but it has not earned a mechanically registered identifier;
- semantic fail: registration results cannot rescue the relation.

Do not choose whichever arm produces the desired historical answer. The direct/staged comparison diagnoses the apparatus; it is not a model-selection tournament.

## Only after calibration

If both semantic arms pass, freeze a separate corpus-transport protocol before reopening any historical file. Start with an untouched deterministic holdout from the 106 `grounds-baseline:P` rows not sampled in the replication. Score semantic relation and registration separately. Use historical cases already seen in the replication only as secondary diagnostics.

If the holdout indicates cohort mixture, exact migration still requires a complete row-level disposition ledger and maintainer adjudication. Neither the calibration controls nor a sampled transport result may be copied into production as replacement labels.

If direct classification passes and the staged arm fails, redesign the observer schema or use the direct instrument for the transport study. If both arms fail, return to the operational contract rather than increasing the sample size.

## Required artifacts

Before scored dispatch retain:

- `protocol.md` with commit, ambient context, actual model, launch method, seeds, gates, and stop conditions;
- a reusable fixture-builder script;
- the gold truth table, hidden from participants but frozen by digest;
- exact participant prompts and sanitized packets;
- a transformation manifest and packet digests.

After dispatch retain normalized outputs, raw failures, model provenance, amendments, an aggregation table, and a result report that leads with the decision table outcome. Raw successful CLI traces may stay outside Git if normalized outputs, exact inputs, trace audit, and cryptographic digests are retained; state that retention boundary explicitly.

## Completion condition

The calibration is complete when another reader can tell:

1. whether premise was recoverable on known positives and close negatives;
2. whether errors came from the contract or the observer-to-mapper pipeline;
3. whether semantic premise and formal registration were independently recoverable;
4. which, if any, corpus-transport experiment is now justified;
5. which claims remain normative fixture conformance rather than evidence about the natural corpus.
