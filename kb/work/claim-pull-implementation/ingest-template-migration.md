# Ingest-template structural migration

## Purpose

Add the required home for claim grounding to every tracked ingest without
inventing claims from old prose. Semantic population belongs to the
[cleanup plan](./cleanup-plan.md).

## Candidate template delta

Add one required top-level section:

```markdown
## Claims

No claims have been grounded in this ingest yet.
```

Place it after `## Code Grounding` when that conditional section exists, and
otherwise after `## Summary`. `## Connections Found` follows it.

The final entry shape, empty-state wording, and position must be fixed in the ADR
before migration. V1 adds no claim identifiers, anchors, or reverse-use section.

## Migration boundary

As of 2026-08-24 there are 284 tracked `kb/sources/*.ingest.md` files. The
migration may add only the heading and selected empty-state sentence. It must not
infer claims from `Summary`, split `Extractable Value`, convert connections into
claims, or change frontmatter, checksums, links, or existing analysis.

An ingest already carrying an experimental claim section stops the mechanical
run for adjudication.

## Atomic rollout

1. Freeze the tracked ingest path list and count.
2. Validate every ingest before mutation and separate pre-existing failures.
3. Test insertion on an ordinary ingest and every conditional template shape,
   including one with `## Code Grounding`.
4. Update the type spec, schema, template, drafting instruction, and corpus in
   one coherent change so no intermediate revision invalidates all ingests.
5. Make same-checksum re-ingestion preserve the complete `Claims` section before
   any populated cache is deployed. A changed checksum with non-empty `Claims`
   blocks pending explicit regrounding or invalidation.
6. Insert the exact section without reflowing surrounding prose.
7. Require every frozen path to contain `## Claims` exactly once and preserve its
   pre-migration `snapshot_sha256`.
8. Run `commonplace-validate kb/sources` and relevant type-contract, schema,
   and instruction tests.
9. Review the diff for changes outside the allowed insertion and commit the
   contract plus migration atomically.

## Failure and recovery

Stop on duplicate claim headings, unrecognized section order, an experimental
claim representation, checksum change, path-set drift, or mutation beyond the
permitted insertion. After an ambiguous partial failure, inspect state with a
separate read-only check before any rerun.

## Completion

- Every frozen ingest contains one `## Claims` heading.
- Empty states make no source claim.
- Existing frontmatter, checksums, links, and prose are unchanged.
- Collection validation and relevant tests pass.
- Semantic cleanup begins only when a source is actually read.
