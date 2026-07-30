# Full mechanism reclassification adjudication packet

**Status:** maintainer decision complete for the semantic split, spellings, and 87 unanimous EX/OP dispositions; exact-boundary evidence is authorized for the remaining 42 rows, but no vocabulary, contract, ADR, authorization, migration, or corpus change is authorized.

## Maintainer decision

On 2026-07-29, after a plain-language restatement of the two relations and unanimous cohorts, the maintainer approved continuing with the recommended course. This accepts:

- the explanatory/operational semantic split;
- `explained-by` and `operates-through` as the source-as-subject spellings;
- the 56 unanimous EX rows and 31 unanimous OP rows as exact semantic dispositions;
- the next read-only evidence work for the remaining 42 rows.

The approval has the scope stated in [What approval authorizes next](#what-approval-authorizes-next). It does not itself adopt catalogue entries, alter collection contracts, authorize pairings, approve an ADR, or permit migration.

## Decision result

The [full reclassification](./mechanism-full-reclassification-results.md) replaces the old mechanism disposition ledger and passes its pre-registered usability rule: 127/129 rows (98.4%) have a stable majority, including 101 unanimous rows. It finds two large reproducible cohorts whose reader and revision consequences differ:

- 65 EX rows, including 56 unanimous rows across 58 source artifacts;
- 40 OP rows, including 31 unanimous rows across 33 source artifacts.

The evidence supports retaining the explanatory/operational distinction. It does not preserve the old row assignments: among 111 surviving rows previously classified EX or OP, only 62 (55.9%) retain the same result and 30 (27.0%) reverse directly between EX and OP.

Accepted maintainer decision: **retain the semantic split, use `explained-by` and `operates-through` as its source-as-subject spellings, and accept the 87 unanimous EX/OP rows as migration candidates.** Prepare a separate exact-boundary packet for the other 42 rows before any contract or corpus change.

## Proposed registered semantics

### `explained-by`

> **source `explained-by` target** means the target supplies an account or principle that explains why or how the source claim occurs or holds.

The reader follows the target for the source's explanatory account. Rejecting or materially revising the target reopens the source's causal or explanatory argument, even when no implementation changes.

The label must not be used merely because the target describes an operation. If the target is the process, component, control path, artifact, or rule actually used to produce the effect, the edge is operational instead.

### `operates-through`

> **source `operates-through` target** means the source effect is produced through the target process, component, control path, artifact, or operational rule.

The reader follows the target to inspect how the source works in operation. Changing the target reopens interface, behavioral, or operational-fit review, even when the general explanation remains accepted.

The label must not be used merely because the target explains why an operation works. Literal use in producing the source effect is the boundary.

These spellings preserve the source as grammatical subject, state distinct traversal decisions, and make the counterfactual maintenance consequence legible. The classifiers tested the semantics without seeing the spellings, so accepting the names remains a maintainer judgment rather than a measured result.

## Cohort decision

The 87 unanimous EX/OP rows are the reproducible core:

| candidate | unanimous rows | proposed disposition |
|---|---:|---|
| `explained-by` | 56 | accept as exact migration candidates |
| `operates-through` | 31 | accept as exact migration candidates |

Acceptance here fixes semantic dispositions, not line numbers. Any later migration must rebaseline each exact tuple and report attrition or additions before editing.

The remaining 42 rows must not inherit either successor automatically:

| result | rows | required treatment |
|---|---:|---|
| contested EX | 9 | explicit row adjudication |
| contested OP | 9 | explicit row adjudication |
| EN | 4 | hold for the `enables` / `precondition` boundary review |
| OTHER | 18 | map to an exact existing relation, connective prose, or removal |
| UNSTABLE | 2 | no candidate; adjudicate from the source and target |
| **total** | **42** | exact boundary packet before migration |

Of these, 26 rows are non-unanimous stable majorities and two are three-way splits. Their complete rationales appear in the result's [contested and unstable diagnostics](./mechanism-full-reclassification-results.md#contested-and-unstable-diagnostics). The protocol requires explicit maintainer adjudication for every 2/3 row; another classifier vote cannot silently convert those rows into automatic candidates.

## Authorization consequences

Accepting the recommended decision does not yet authorize any new collection pairing. The current surface includes one reference→notes row, `F115`, and that row is UNSTABLE. Do not broaden a contract around it; settle or remove the exact edge first.

The active and deferred cohorts otherwise require a fresh pairing audit after their exact successors are known. Existing authorization for another identifier must not be inferred to authorize either new identifier.

The proposed relations have no demonstrated inverse-reader need in this workshop. Do not register inverse labels as part of this decision.

## What approval authorizes next

Approval of the recommendation authorizes evidence and planning work only:

1. treat the 56 unanimous EX and 31 unanimous OP rows as accepted semantic dispositions;
2. prepare one exact-boundary adjudication packet for the remaining 42 rows, preserving all vote rationales;
3. audit the resulting exact source→target collection pairings;
4. return with proposed catalogue entries, contract deltas, ADR scope, and a rebaselined migration plan.

It does not authorize editing link labels, adopting catalogue entries, changing collection contracts, widening reference→notes pairings, writing an ADR as accepted, or migrating the corpus.

The ADR 009 scoping contradiction remains logically independent. It may be amended separately or folded into a later mechanism ADR, but approval here does not choose between those paths.

## Alternatives

### Revise only the spellings

Accept the explanatory/operational semantics and unanimous cohorts but withhold the names. State replacement names or authorize a focused identifier evaluation. This delays catalogue and migration planning but does not require rerunning the classification.

### Reject the split

Reject both proposed relations and evaluate a new broad successor or retirement into existing relations and connective prose. This overrides strong full-surface evidence: 65 stable EX and 40 stable OP rows with distinct reader and maintenance consequences. The reason for the override should be recorded in the eventual ADR.

### Reopen the semantic evidence

Require cross-model-family replication or another protocol before deciding. State the additional acceptance rule in advance. The present run used fresh isolated contexts but one reported model family; this option buys independence evidence at the cost of another full classification.

## Recorded maintainer response

The maintainer's “ok — go on” followed the requested explanation of the split, spellings, and unanimous cohorts. It is recorded here as approval of the recommended split, spellings, 87 unanimous dispositions, and next evidence work, within the non-mutation boundary above.
