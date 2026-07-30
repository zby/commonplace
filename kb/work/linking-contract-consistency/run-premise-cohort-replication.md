---
description: "Use when independently replicating the legacy grounds premise classifications before approving the deferred grounds migration"
type: kb/types/instruction.md
---

# Replicate the premise-cohort classification

Run this instruction before approving phase B of the premise/mechanism migration. It tests whether fresh Luna contexts recover the premise semantics assigned to the surviving original `grounds` premise cohort. A human invokes it in a new orchestrating session; observer and mapper participants receive only their stage-specific packets and must not read this instruction.

Follow the general controls in [Design experiments in Commonplace](./link-vocabulary-experiment-design.md). This packet fixes the experiment-specific choices that another session cannot safely infer after seeing results.

## Claim boundary

Primary question:

> When the current label, production policy, candidate identifiers, and prior outcome are withheld, do independent Luna runs still describe the sampled legacy relationships as theoretical assertions depending for truth or applicability on target propositions?

The experimental unit is one directed source-to-target relationship. Three Luna runs over the same relationship estimate run stability for Luna in the declared context. The 49 sampled relationships support an inference only to the finite surviving legacy premise cohort from which they were selected; they do not establish generalization across models, collections, or future links.

This run can establish boundary reproducibility. It cannot establish:

- that `premised-on` is the best spelling;
- that a formal identifier outperforms a context phrase;
- that readers use the edge well;
- that authors can assign it reliably during normal writing;
- that the current disposition is true merely because it agrees with prior policy.

The comparison with the prior disposition happens only after all raw observations and mappings are frozen.

## Model and operativity

Use Luna for every scored observer and mapper context. Record the requested and actual model identity for every pass. If the runtime cannot verify that scored participants used Luna, stop before dispatch rather than substituting another model while calling the result a Luna replication.

The orchestrator may read production artifacts to construct fixtures. Scored participants must use fresh contexts with no inherited conversation and no access by design to production contracts, the shared catalogue, prior workshop results, the live disposition manifest, git history, or another participant's output.

Prefer prompt-contained packets or a fixture root outside the Commonplace checkout. If filesystem isolation is not technically enforced, state that limitation, audit observed reads, and describe the run as instruction-isolated and trace-audited. Root `AGENTS.md`, system/developer instructions, tool descriptions, and skill summaries remain ambient unless a separately launched, matched CLI fixture actually changes that context. Snapshot the ambient context and exact launch method in the run protocol.

## Freeze the run before scored dispatch

Create `kb/work/linking-contract-consistency/premise-cohort-replication/` and write these run artifacts before dispatch:

- `protocol.md` — repository revision, ambient-context inventory, isolation mode, requested model, batch plan, prompts, scoring rules, and any deviations from this instruction;
- `manifest.tsv` — the frozen sample and controls, including neutral ID, source, target, current tuple digest, cohort, and orchestrator-only prior disposition;
- `prompts/observer.md` and `prompts/mapper.md` — exact participant prompts;
- `fixture-build.md` or a retained script — the exact sanitization procedure and content-digest method.

Record the commit and SHA-256 digests of this instruction, the general experiment-design instruction, the live disposition manifest, root `AGENTS.md`, every source and target artifact, the prompts, and every sanitized packet. If some ambient instruction cannot be retained or hashed, record what the runtime exposed and mark the remainder uncontrolled.

Exploration may use pilot cases, but freeze the scored sample, prompts, transformations, batching, exclusions, and decision rules before any scored output is produced. Preserve every earlier protocol version if exploration changes the design.

## Rebaseline the finite cohort

Prerequisite: the current workshop must contain `premise-mechanism-live-disposition-manifest.tsv`. Use it as the decision-provenance index, then verify every candidate tuple against the live corpus. At the planning baseline it contains:

- 155 surviving rows with `disposition = premised-on` and `decision_basis = grounds-baseline:P`;
- 8 rows moved into `premised-on` by `grounds-boundary` adjudication;
- 5 rows assigned `premised-on` by a `grounds-drift:*` k=3 run.

Do not assume those counts remain current. Match tuples by source plus resolved target, not by line number or dash glyph. Report additions, deletions, target changes, duplicates, and unsupported footer syntax. Exclude disappeared tuples as attrition. Stop if the decision provenance cannot be reconciled exactly; do not repair it inside the experiment.

New `grounds` rows are outside this replication because they were not members of the original classification. Route them to a separate drift run.

## Select the cases deterministically

Construct four cohorts after rebaseline.

### Primary cohort: 49 legacy premise rows

The primary pool is every surviving tuple whose manifest row has:

```text
current_label = grounds
disposition = premised-on
decision_basis = grounds-baseline:P
```

For each tuple compute:

```text
SHA256("premise-primary-v1" + NUL + source + NUL + resolved_target)
```

Sort ascending by this digest and take the first 49 rows. If fewer than 49 survive, use the complete surviving pool and replace the count-based decision bands below with the corresponding proportions, recorded before dispatch.

### High-risk cohort: every boundary correction

Include every surviving `premised-on` row whose decision basis is `grounds-boundary`. These rows entered the premise class only after a coarse X/D classification, so report each separately. They do not enter the primary denominator.

### Prior-replication cohort: every premise drift row

Include every surviving `premised-on` row whose decision basis begins `grounds-drift:`. These rows already received k=3 classification under the prior runtime. They are a cross-run diagnostic and do not enter the primary denominator.

### Negative controls: 16 non-premise rows

From current `grounds` rows in the live manifest, select four rows from each disposition:

- `explained-by`;
- `operates-through`;
- `extends`;
- `evidenced-by`.

Within each disposition rank rows by:

```text
SHA256("premise-control-v1" + NUL + source + NUL + resolved_target)
```

and take the first four. These controls detect a pipeline that maps most articulated relationships to the premise class. They are diagnostics against prior adjudications, not independent semantic ground truth.

Assign every case a neutral ID from a salted digest. IDs, paths, batch names, and packet order must not reveal cohort or prior disposition. Keep the mapping in the orchestrator-only manifest.

## Build label-blind case packets

Each case packet contains:

- the substantive source artifact as `Artifact A`;
- the substantive target artifact as `Artifact B`;
- the under-review context phrase, if the footer supplied one;
- a neutral statement that the possible A-to-B relationship is under review.

Keep titles because they carry substantive claims. Remove or neutralize:

- the current footer identifier on the tested edge;
- all other labelled footer lines from both artifacts;
- source and target paths, line numbers, tuple IDs, cohort names, and prior classifications;
- links that could lead a participant into the production repository;
- frontmatter or annotations that disclose an experimental result rather than artifact meaning.

Do not erase ordinary argumentative prose merely because it uses words such as “because,” “assumes,” “explains,” or “requires.” That prose is evidence about the relationship, not an experimental annotation. Record every transformation and retain pre- and post-transformation digests.

Use synthetic cases or corpus cases outside every scored cohort and outside the legacy pool eligible for a later full-cohort expansion to test parsing, sanitization, prompt clarity, and output parsing. Never repair a scored case after seeing its outcome. If a material fixture defect appears after dispatch, stop, preserve the failed run, version the protocol, and restart the affected scored surface.

## Stage 1 — observe without a vocabulary

For every case, obtain three observations from three fresh Luna contexts. A context may process a frozen batch of cases, but every case must appear in three independently launched passes, participants must not see one another's answers, and case order must be independently randomized per pass from recorded seeds.

Observers see only their sanitized case packets and this prompt substance:

> Read Artifact A and Artifact B. Do not assign a relationship label or choose from a taxonomy. For the possible directed relationship from A to B, report:
>
> 1. the particular assertion in A that makes B potentially relevant;
> 2. why a reader of A would follow B, if at all;
> 3. what the author of A should reconsider (a) if B's central claim were rejected and (b) if B's contents, implementation, or availability materially changed, where applicable;
> 4. whether this deserves a mechanically discoverable edge, belongs only in connective prose, or supplies no useful connection;
> 5. one short sentence with A as grammatical subject describing what A asserts about B;
> 6. confidence (`high`, `medium`, or `low`) and a concise justification grounded in both artifacts.

Observers must not see candidate definitions, identifiers, production contracts, the sample frame, prior decisions, or the decision threshold. Freeze all observation records before beginning Stage 2.

## Stage 2 — map frozen observations to neutral classes

Use fresh Luna mapper contexts. Each mapper sees only one pass's frozen Stage-1 observations, in a newly randomized order, plus the neutral class definitions below. It does not see the source or target artifacts, production identifiers, current authorization, cohort membership, or another mapper's output.

Map each observation to exactly one class:

- **C1 — theoretical dependence:** A is an assertion whose truth or applicability takes the proposition in B as an assumption or condition. Rejecting B reopens whether A holds or applies. B is not merely evidence, an explanatory account, an operating path, or a prior operational requirement.
- **C2 — explanation:** B supplies the account or principle explaining why or how A occurs or holds. Rejecting B reopens A's explanation without by itself changing an implementation.
- **C3 — operation:** A's effect is literally produced through the process, component, control path, artifact, or rule in B. Changing B reopens operational fit or behavior.
- **C4 — design dependence:** A is a design, rule, description, procedure, or system-definition artifact shaped or justified by theory in B. Rejecting B prompts reconsideration or redesign rather than reassessment of A as a theoretical claim.
- **C5 — prerequisite:** B must be available, true, or completed before A works, but B is neither A's theoretical premise, explanatory account, nor operating path.
- **C6 — target evidence:** An observation or case in B corroborates, qualifies, or bounds the assertion in A.
- **C7 — source evidence:** A is an observation or case bearing materially on an assertion in B.
- **C8 — development:** A develops, specializes, or carries B's argument further.
- **C9 — exemplification:** A is a worked instance of B's more general claim.
- **C10 — definition:** B defines a term materially used by A.
- **C11 — contrast or incompatibility:** A and B are meaningfully contrasting or conflicting claims.
- **C12 — another formal relation:** another recurring formal relationship is better; name it and state its reader and revision consequences.
- **C13 — connective prose only:** the local relationship is useful but does not earn a mechanically discoverable edge.
- **C14 — no useful connection:** the proposed edge fails the articulation test or adds no useful traversal.
- **C15 — insufficient observation:** the frozen Stage-1 record does not contain enough information to distinguish the relevant classes without reopening the artifacts.

For each mapping return the neutral case ID, one class, confidence, and a concise explanation using only the frozen observation. A mapper may not reopen an artifact to fill gaps. Preserve C15 rather than leaking an underspecified case back into Stage 1.

After all mappings are frozen, the orchestrator reveals that C1 corresponds to the semantic class proposed for `premised-on`. No participant uses the identifier during scored work.

## Aggregate and apply the gate

Each case must have exactly three observer records and three corresponding mapper records. For each case:

- three identical mapped classes are unanimous;
- two identical classes are a stable majority;
- three different classes are UNSTABLE;
- an invalid or missing record is not silently dropped; apply the frozen exclusion rule or stop.

For the 49-row primary cohort, define an **adverse row** as either:

- a stable majority other than C1; or
- UNSTABLE.

Apply the [grounds review's pre-existing reversal boundary](./grounds-label-direction-review.md#confidence-and-reversal-evidence) as follows:

- **0–4 adverse rows:** the sample survives; the upper bound of its two-sided 95% Wilson interval remains below approximately 20%. Retain the cohort-level premise decision, while preserving every row-level disagreement.
- **10 or more adverse rows:** the observed adverse share is at least approximately 20%. Reopen the premise classification and do not approve phase B from the current ledger.
- **5–9 adverse rows:** inconclusive. Before interpreting the result, extend the same frozen protocol to every remaining surviving `grounds-baseline:P` row and decide from the complete cohort.

Do not move thresholds after seeing the distribution. Report unanimous and 2/3 C1 rows separately, the exact alternative-class distribution, confidence, and observer-versus-mapper failure patterns.

The secondary cohorts do not alter the primary denominator:

- adjudicate any changed boundary-correction row explicitly rather than hiding it in an aggregate;
- compare the five drift rows with their prior k=3 dispositions as a cross-runtime diagnostic;
- if four or more of the 16 negative controls receive a C1 majority, treat the pipeline as insufficiently discriminating and do not issue a “survives” conclusion, regardless of the primary count.

Agreement with the prior ledger is reproducibility evidence, not an independent semantic oracle. Maintainer adjudication remains separate from aggregation.

## Audit and report

Retain under the run directory:

- all sanitized packet digests and the transformation manifest;
- all raw observer outputs;
- all raw mapper outputs;
- parse failures, exclusions, attrition, and mid-run amendments;
- requested and actual model/runtime provenance;
- observed tool/file reads and any unexpected exposure;
- the neutral-ID mapping, revealed only in the final orchestrator result;
- `results.md` with the primary gate first, followed by secondary diagnostics.

The result must state its blindness precisely. For example:

> Scored participants were label-blind, outcome-blind, production-contract-file-blind, and catalogue-file-blind. They received fresh contexts and prompt-contained sanitized packets. Root governance and skill descriptions remained ambient and matched across passes. Filesystem isolation was [enforced / not enforced]; trace inspection found [summary].

Validate every committed Markdown output with `commonplace-validate` and run `git diff --check`. Do not edit corpus edges, collection contracts, the shared catalogue, ADRs, the implementation packet, the live disposition manifest, or prior results during this experiment.

## Completion condition

The run is complete when:

1. the live sample frame reconciles and every selected tuple is accounted for;
2. the protocol and all scored inputs were frozen before dispatch;
3. every included case has three valid observer and mapper records or a pre-registered exclusion;
4. ambient context, isolation, leakage, model provenance, and transformations are auditable;
5. the primary result is stated as survives, reopens, or inconclusive under the fixed gate;
6. secondary cohort disagreements are exposed for maintainer adjudication;
7. the report says explicitly that it tests premise-boundary reproducibility, not vocabulary utility or authorability.
