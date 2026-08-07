---
description: "Use when deciding the source-as-subject successor, scope, and neighboring-label boundary for the canonical note-to-note grounds cohort"
type: kb/types/instruction.md
---

# Evaluate the grounds link label

## Outcome

Produce `kb/work/linking-contract-consistency/grounds-label-direction-review.md`: a read-only semantic evaluation with a complete disposition ledger for every active canonical `grounds` edge and a recommendation that is ready for maintainer adjudication.

Decide among four outcomes:

1. adopt one source-as-subject successor for the coherent premise relation;
2. merge that relation into `rests-on` because the reader action is not meaningfully distinct;
3. split or reclassify the cohort across more specific relations;
4. retire the formal relation in favor of connective prose.

Do not edit corpus edges, collection contracts, the shared catalogue, ADRs, or durable instructions. This task decides semantics; it does not perform or plan the migration.

## Governing context

Read:

- [ADR 058](../../reference/adr/058-directional-identifiers-use-source-as-subject.md) for the `source <label> target` invariant;
- [ADR 060](../../reference/adr/060-rationale-becomes-rests-on-and-off-pattern-grounds-reclassified.md) for the implemented `rests-on` boundary and the deferred canonical cohort;
- the [directional-label grammar](./directional-label-grammar.md), [rationale direction review](./rationale-label-direction-review.md), [boundary adjudication](./rationale-grounds-boundary-adjudication.md), and [rationale migration retrospective](./rationale-label-migration-retrospective.md);
- the current [link vocabulary](../../reference/link-vocabulary.md), `kb/notes/COLLECTION.md`, and any other active contract or guidance that defines or teaches `grounds`;
- the [reusable migration procedure](../../instructions/migrate-directional-link-label.md) only to understand what evidence a later migration will require.

Treat current prose and authorization as hypotheses, not conclusions. The retained distinction is that a theoretical assertion uses `grounds` to send a reader to a premise whose truth or applicability they may need to verify, while a design, rule, description, or procedure uses `rests-on` to send a reader to theory whose rejection would trigger design reconsideration. Test whether the live corpus sustains that distinction.

## Build and classify the live corpus

Rebaseline immediately. The last migration preserved 276 active note-to-note `grounds` tuples, but that count is not an execution lock. Define the positive mutable surface and mutually exclusive exclusion buckets; resolve every target before classification; cover ordinary and bold footer forms; fail visibly on syntax the inventory cannot parse.

Classify every active canonical tuple by the assertion it actually makes. Use a compact disposition vocabulary that at least distinguishes:

- premise dependency;
- `rests-on` dependency;
- evidence;
- mechanism or explanation;
- extension or specialization;
- definition, lineage, comparison, or navigation;
- removal;
- unresolved ambiguity.

Add a category only when the corpus demands it. Authorization failures and historical/excluded occurrences are bookkeeping facts, not semantic dispositions. Inspect local link context first and open the full source and target when the assertion remains unclear.

For each tuple ask:

- What question would make a reader follow this edge?
- Does changing or rejecting the target call for reassessing the source's truth, reconsidering its design, updating its evidence, or merely revising a citation?
- Does the target function as a premise, an observation, a mechanism, or a neighboring claim?
- Would `rests-on` preserve the same decision before following, or erase a useful distinction?
- Would direct prose or an existing relation communicate more precisely than a dedicated premise label?

Review incoming and reciprocal patterns only to decide whether an independently useful inverse relation exists. Do not infer a reciprocal-authoring obligation from semantic inversion.

## Compare successor assertions

Evaluate the strongest names supported by the corpus, including `premised-on` and `is-grounded-in`, but do not select by elegance or familiarity. Each candidate must complete `source <label> target`, have one stable assertion template, and avoid implying deductive entailment, evidential support, or target-side uptake unless the edges warrant it. Consider `follows-from`, `depends-on`, or another candidate only if its ordinary reading matches the reviewed assertions.

Compare at least:

- one dedicated premise successor;
- merging the coherent cohort into `rests-on`;
- reclassifying recurring subcohorts into existing relations;
- retiring the label.

Prefer the smallest vocabulary that preserves a repeated reader decision. State the neighboring-label boundary precisely enough that a later classifier can distinguish the recommended relation from `rests-on`, `evidenced-by`, `extends`, and the still-unresolved `mechanism` label.

## Required review

The review must include:

- live and excluded counts, with source→destination reconciliation;
- one disposition for every active tuple, with file and target identity sufficient for a later exact migration;
- counts and representative cases for every semantic class;
- the strongest evidence for and against each candidate outcome;
- the recommended identifier, assertion template, reader need, direction kind, and inverse decision—or an explicit recommendation to merge or retire;
- authorization and later-migration consequences without making those changes;
- ambiguous cases with minimal quotations and file/line pointers;
- surprises that could improve the next evaluation or migration;
- confidence and concrete evidence that would reverse the recommendation.

The ledger may be a table in the review or a separate workshop TSV linked from it. Keep generated artifacts and temporary scripts out of the repository unless they carry information the maintainer needs to adjudicate the result.

Validate the changed workshop artifacts, inspect the diff, and report changed paths plus any unrelated pre-existing test or validation failures. Record the actual executing model from runtime evidence; if Luna cannot be dispatched or verified, report that limitation instead of claiming Luna provenance.

