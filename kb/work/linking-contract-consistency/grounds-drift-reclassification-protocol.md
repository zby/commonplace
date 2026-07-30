# Grounds drift reclassification protocol

**Date:** 2026-07-29

**Status:** pre-registered read-only classification protocol for 21 live `grounds` tuples added after the 283-row direction-review baseline.

## Purpose

Supply exact semantic dispositions for current `grounds` additions before producing a migration plan. The earlier direction review and boundary adjudication cover surviving members of their 283-row baseline; they cannot silently classify new tuples.

This run does not edit a corpus edge, collection contract, catalogue entry, ADR, or prior result. It produces evidence for maintainer adjudication.

## Rebaseline

A syntax-aware scan of active mutable artifacts found 292 live `grounds` tuples. Compared with the 283-row direction-review ledger:

- 271 baseline tuples survive;
- 12 baseline tuples disappeared: 5 P, 3 X, 2 M, and 2 E;
- 21 tuples are new and require classification.

The [drift manifest](./grounds-drift-reclassification-manifest.tsv) freezes those 21 additions. All are notes→notes. It is ordered by SHA-256 over `source + NUL + target` and assigned round-robin to two batches of 11 and 10 rows. Approximate source-plus-target loads are 26,646 and 23,626 words.

Every tuple resolved exactly once at dispatch. Recheck the full tuple after classification; report attrition or movement rather than substituting another row.

## Isolation and record

Each batch receives three independent classifier contexts. A classifier reads this protocol and the full source and target artifact for each assigned row. It must not read the prior grounds or mechanism review ledgers, their votes or results, another classifier's output, or the tuple's historical predecessor. The visible current `grounds` spelling supplies no semantic presumption.

For every row record:

1. one exact choice;
2. confidence (`high`, `medium`, or `low`);
3. reader need;
4. revision consequence;
5. closest-rival boundary test;
6. authorization impact;
7. a concise justification grounded in both artifacts.

## Exact choices

Every identifier completes **source `<choice>` target**:

- `premised-on` — the theoretical source assertion depends for truth or applicability on the target premise.
- `explained-by` — target supplies the account or principle explaining why or how the source occurs or holds.
- `operates-through` — target is a process, component, control path, artifact, or operational rule actually used to produce the source effect.
- `prerequisite-hold` — target must be available, true, or completed before the source works, but exact naming awaits the `enables` / `precondition` family review.
- `extends` — source develops, specializes, or carries the target argument further.
- `exemplifies` — source is a worked instance of the target's more general claim.
- `defined-in` — target under `kb/notes/definitions/` defines a source term.
- `evidenced-by` — target observation or case corroborates, qualifies, or bounds the source assertion.
- `is-evidence-for` — source observation or case bears materially on the target assertion.
- `contrasts` — source and target are neighboring shapes whose difference matters.
- `contradicts` — source and target make incompatible claims requiring resolution.
- `connective-prose` — the relationship helps locally but does not earn a stable formal footer edge.
- `remove` — the edge fails the articulation test or supplies only weak adjacency.
- `other:<identifier>` — another exact source-as-subject relation is materially better; name and define it.

Do not return `grounds` or `mechanism`. By maintainer decision, do not return `see-also` for notes→notes: when no stronger relation survives, choose `remove` or `connective-prose`.

## Boundary sequence

1. Test literal operational use against explanation.
2. Test explanation against premise dependence.
3. Test theoretical premise against operational prerequisite.
4. Test development, instance-to-general, definition, evidence, contrast, and contradiction.
5. If no exact formal reader and revision decision survives, choose prose or removal.

Classify semantic truth before current authorization. Record `authorized`, `candidate-new`, `candidate-delta`, `deferred-family`, `not-applicable`, or `unknown` using the same meanings as the [mechanism boundary protocol](./mechanism-boundary-adjudication-protocol.md).

## Aggregation and gate

Retain all 63 records verbatim. A 3/3 exact choice is unanimous, 2/3 is contested, and three different choices are UNSTABLE. Do not collapse prose, removal, or free-form identifiers.

No row enters a migration plan merely from aggregation. The result exposes all majority and minority rationales, then the maintainer explicitly accepts or changes the exact dispositions. Completion requires 63 parseable votes, a post-run tuple check, and authorization consequences.
