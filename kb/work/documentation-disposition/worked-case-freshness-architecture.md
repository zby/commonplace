# Worked case: `freshness-architecture.md`

Executed 2026-08-24. The seventh and final artifact in the original scope.

## Result

**Minimized around cache-coherence semantics.** The page now explains target
and input identity, registered status versus review discovery, the distinct
evidence effects of capture, acknowledgement, and retirement, and the complete
queue-to-finalize concurrency guard. Physical storage, data-model, package,
command, flag, exit-code, JSON, and deferred-design inventories route to live
owners or adopted decisions.

The edit reduced the page from 6,915 bytes and 113 lines to 5,813 bytes and 107
lines. It also added one cross-component invariant that the old page omitted,
so the reduction understates the removed exact-fact obligation.

## Consumption events and dispositions

| Unit | Consumer question | Required reliability | Recovery result | Source grain | Document grain | Maintenance form | Disposition | Retrieval path |
|---|---|---|---|---|---|---|---|---|
| Physical store paths and migration warning | Where is the database and how is an old store handled? | exact | direct recovery | `commonplace.store`, migration source, command help | path table plus procedure | executable source | omit | store source; help; ADR 052 for history |
| Data-model table | What tables and views exist? | exact | direct recovery; prose incomplete | packaged SQL and `EXPECTED_TABLES` | six-row table | executable schema | omit | `store-schema.sql`; `commonplace.store` |
| Target and input identity | What is one freshness unit, and what does v1 version? | architectural | distributed across keys, versioning, baselines, review adapter | several small modules | one paragraph | authored synthesis | keep and clarify | target/input section |
| Package layout | Which module owns a symbol? | orientation | direct task-vocabulary recovery; inventory incomplete | module docstrings and symbols | 11-line tree | live source | omit | `commonplace-source`; source search |
| Generic substrate versus review adapter | Why can status not discover an unreviewed pair? | architectural | cross-component | generic selector plus review target selector | two scattered paragraphs | authored ownership boundary | keep and consolidate | registered-status section |
| Transition table | What inputs and evidence does capture, ack, or retirement use? | architectural | cross-component | finalization, transition, baseline, and pruning code | table plus prose | authored synthesis | keep and sharpen | transition section |
| Acknowledgement revision, hash, and evidence rules | What prevents acknowledging a different observation? | architectural | distributed | CLI parser, transition, baseline refresh | one extracted invariant | authored boundary plus live exact fields | keep and compress | transition section; live source |
| Queue CAS | Can queued work overwrite a changed baseline? | architectural | old account incomplete | pair creation, generation ledger, finalization, integrity checks | one sentence | authored concurrency invariant | replace with complete rule | queue-to-finalize section |
| Status flags, labels, and exit codes | How do I invoke and parse status now? | exact | direct recovery; list incomplete | `--help`, status serializer and exit mapper | two paragraphs | help and executable serializer | omit | command help; live status source |
| Command surface | Which freshness commands exist? | complete discovery | duplicate | checked command catalogue | three bullets | checked catalogue | omit | `commands.md` |
| Registration limit and deferred target names | Why is there no generic creation command? | architectural decision; proposal specifics elsewhere | mixed | ADR 065 plus live admissible kinds | one command absence plus named proposal internals | retain withdrawal rule; omit proposal inventory | split | registration-scope section; ADR 065 |

## Recovery and drift experiment

Source searches beginning with `store`, `baseline`, `status`, `ack`, `retire`,
and `expected revision` selected the owning modules without the old package
map. Exact schema questions selected the packaged SQL resource and
`commonplace.store.EXPECTED_TABLES`; CLI questions selected side-effect-free
help and the three small command modules.

Four mismatches showed the cost of mixing those facts into architecture prose:

- The physical-store section named `PRAGMA user_version = 1`; the live store
  version is 3.
- The data-model table listed six tables and omitted
  `freshness_target_generations`.
- The package tree omitted `freshness/revisions.py`, the module that allocates
  monotonically increasing revisions across retirement and recreation.
- The status option list omitted the shipped `--missing` filter.

Each omission was locally plausible and harmless for orientation, but none was
safe for an exact consumer. Removing the inventories makes source the first and
only exact read.

## Unique invariant recovered

The old concurrency paragraph covered only a queued pair whose baseline
already existed: record `expected_baseline_revision`, then compare it at
finalization. That cannot represent a pair queued while no baseline exists.

The implementation closes the absent-state race with a persistent generation
ledger. Pair creation records either the current baseline revision or the next
generation revision, never both. The generation value remains advanced after
a baseline is retired. Finalization therefore rejects both ordinary
baseline movement and the absent/create/retire ABA sequence that would
otherwise look absent again.

This relation spans review pair creation, freshness revision allocation,
retirement, finalization, store integrity, and transition tests. It was added
to the architecture page because no one source unit states the complete
queue-to-finalize rule. Exact fields and error strings remain in source.

## Why the document survives

The retained questions are relational. A reader needs to know why a baseline
makes evidence applicable but does not endorse it; why global status cannot
report `missing-baseline`; why capture trusts queued snapshots while ack reads
live files; why one transition preserves evidence and another replaces it; and
why retirement cannot reset concurrency history. Reconstructing any one answer
requires several packages or a decision plus implementation.

The page now closes those questions without acting as a second store schema,
module index, command reference, or serialization contract. Its maintenance
triggers name semantic changes; exact implementation churn no longer creates a
documentation obligation.

## Next

The original artifact sweep is complete. The workshop can now synthesize the
seven dispositions into a durable rule, identify any newly exposed candidates
such as `instruction-generation.md`, and close rather than expand the sweep
without a fresh scope decision.
