# Mechanism boundary adjudication protocol

**Date:** 2026-07-29

**Status:** pre-registered read-only classification protocol for the 42 rows outside the accepted unanimous EX/OP core.

## Purpose

Produce independent exact-successor evidence for every mechanism-surface row that the maintainer did not accept as part of the 87-row unanimous core. The result is an adjudication packet, not a migration ledger: every row remains an explicit maintainer decision.

The decision baseline is the [recorded mechanism adjudication](./mechanism-full-reclassification-adjudication-packet.md): `explained-by`, `operates-through`, and their 87 unanimous dispositions are accepted semantically, while contracts, pair authorizations, catalogue entries, ADR text, and corpus edits remain unchanged.

## Frozen surface

The [boundary manifest](./mechanism-boundary-adjudication-manifest.tsv) freezes 42 current tuples after resolving every source link against its target:

- 18 contested EX/OP rows;
- 4 prerequisite-shaped EN rows;
- 18 OTHER rows whose coarse class is not an exact successor;
- 2 three-way UNSTABLE rows.

The surface contains 24 active `mechanism` rows and 18 deferred `grounds` rows. Forty-one pair notes→notes; `F115` alone pairs reference→notes. All 42 tuples resolved exactly once at dispatch. The manifest is ordered by the full-run SHA-256 digest and assigned round-robin to four batches of 11, 11, 10, and 10 rows. Approximate source-plus-target loads are 26,257, 24,580, 21,453, and 21,033 words.

Recheck every tuple after classification. Runtime attrition or movement is reported; it is never silently replaced with a new row.

## Isolation and evidence rule

Each batch receives three independent classifier contexts. A classifier reads only this protocol, the batch's source and target artifacts, and the source collection contract when checking authorization. It must not read the prior mechanism review, full-run vote ledger, result diagnostics, origin label, prior disposition, or another classifier's output.

The existing footer label remains visible in the source artifact but supplies no semantic presumption. Classifiers decide from the source assertion, target content, reader need, and revision consequence.

For every row, each classifier records:

1. one exact choice;
2. confidence (`high`, `medium`, or `low`);
3. the reader's reason to follow the target;
4. what target rejection or change would make the source author recheck;
5. one boundary test separating the choice from its closest rival;
6. current authorization impact;
7. a concise justification grounded in both artifacts.

No classifier edits a library artifact, collection contract, catalogue, ADR, prior result, or manifest.

## Exact choices

Every choice completes **source `<choice>` target**. Choose for semantic truth before considering current authorization.

- `explained-by` — target supplies the account or principle explaining why or how the source occurs or holds. Rejecting the target reopens the source explanation without requiring an implementation change.
- `operates-through` — target is a process, component, control path, artifact, or operational rule actually used to produce the source effect. Changing it reopens operational fit even if the explanation remains accepted.
- `premised-on` — the theoretical source assertion depends for truth or applicability on the target premise. Rejecting the target reopens the source assertion, but the target is neither its explanatory account nor operating path.
- `prerequisite-hold` — the target must be available, true, or completed before the source works, but the exact source-as-subject identifier awaits the full `enables` / `precondition` family review. This is a disposition class, not a proposed registered label.
- `extends` — source develops, specializes, or carries the target's argument further.
- `exemplifies` — source is a worked instance of the target's more general claim.
- `defined-in` — target is the definition of a term used by the source; the target must be under `kb/notes/definitions/`.
- `evidenced-by` — target observation, case, or source corroborates, qualifies, or bounds the source assertion.
- `is-evidence-for` — source observation or case bears materially on the target assertion without implying target-side uptake.
- `contrasts` — source and target are neighboring shapes whose difference matters to the reader.
- `contradicts` — source and target make incompatible claims the reader must resolve.
- `rests-on` — descriptive, prescriptive, or system-definition source depends on the target theoretical claim. Use only where the source's register fits; in this surface it is relevant only to the reference→notes row.
- `see-also` — a useful adjacent companion remains after every specific relation is ruled out.
- `connective-prose` — the relationship helps the local sentence or example but does not earn a formal footer edge with a stable reader and revision decision.
- `remove` — the edge fails the articulation test or adds no useful traversal.
- `other:<identifier>` — another exact source-as-subject relation is materially better. Name and define it; do not return bare `other`.

Do not return the retired broad labels `mechanism` or `grounds`. Do not force a row into the accepted split merely because it came from that review.

## Boundary sequence

Apply these questions in order:

1. Is the target literally used in producing the source effect? If yes, test `operates-through` against explanation and prerequisite.
2. Does the target explain why or how the source holds, such that rejecting it reopens the source account while operation may stay unchanged? If yes, test `explained-by`.
3. Does the source's truth or applicability assume the target rather than derive its explanation or operation from it? If yes, test `premised-on`.
4. Must the target be available, true, or completed before the source can work, without being a theoretical premise? If yes, return `prerequisite-hold`.
5. Is the relationship development, instance-to-general, definition, evidence, contrast, contradiction, or descriptive dependence? Apply the exact catalogue boundary above.
6. If no specific formal reader need and revision consequence survive, choose `see-also`, `connective-prose`, or `remove` without preserving an edge for tuple conservation.

## Authorization record

Authorization does not change semantic choice. Record one of:

- `authorized` — the current source collection contract permits this label for the destination;
- `candidate-new` — the accepted semantic label still requires catalogue and source-contract adoption (`explained-by`, `operates-through`, or `premised-on`);
- `candidate-delta` — an existing label would require a new source→destination authorization;
- `deferred-family` — `prerequisite-hold` awaits the family review;
- `not-applicable` — prose or removal creates no label authorization;
- `unknown` — an `other:<identifier>` candidate needs later contract analysis.

## Aggregation and adjudication rule

Retain all 126 records verbatim. For each row:

- 3/3 exact agreement is a unanimous recommendation;
- 2/3 exact agreement is a contested recommendation;
- three different exact choices are UNSTABLE and have no aggregate recommendation.

Do not collapse `prerequisite-hold`, `connective-prose`, `remove`, or different `other:<identifier>` values into one class. Similar free-form identifiers may be normalized only when their stated assertion is identical, with the normalization exposed in the result.

There is no automatic migration cohort in this run. Completion means 126 parseable votes, a post-run tuple check, an authorization summary, and a per-row packet exposing majority and minority rationales. The maintainer explicitly accepts, revises, or rejects every proposed disposition before any catalogue, contract, ADR, or corpus mutation.
