# Workshop: artifact freshness and referential checks

## Question

What general mechanism should register artifact-to-artifact dependencies, retain accepted dependency baselines, expose repository-wide freshness status, select targets affected by changed inputs, and distinguish freshness from deterministic cross-artifact validity?

No artifact class is intrinsically a source or a derivative. A source snapshot, ingest, note, criterion, type specification, instruction, report, or generated index may be an input in one target and a freshness target in another. The mechanism must not special-case sources or ingests.

## Current phase (v1)

Ship **review-first migration** onto a general operational store:

- one `file-text` version function;
- `review-pair` targets only;
- repository-wide status, accept, ack, and retire over registered baselines; and
- capture refresh vs observation refresh separated, with queued-job CAS.

**Out of this phase:** `collection-text` versioning, `collection-maintenance` targets, and any non-review registration. Those designs are sketched in [future-work-collection-freshness.md](./future-work-collection-freshness.md) and exit through **M4 proposals** — see [implementation plan](./implementation-plan.md).

Referential-check class design (general cross-artifact prose validation, positioned parse model) remains open; verbatim-quote verification (ADR 046) is already shipped and is not redesigned here.

## Document map

| document | role |
|---|---|
| [implementer-handoff.md](./implementer-handoff.md) | compressed entry point — verdict, milestones, traps |
| [implementation-plan.md](./implementation-plan.md) | sequence, gates M1–M4, done-when |
| [database-design.md](./database-design.md) | schema authority — migration map, DDL, transactions |
| [freshness-schemas.md](./freshness-schemas.md) | canonical status/accept/ack/retire JSON (v1: `review-pair`, `file-text`) |
| [future-work-collection-freshness.md](./future-work-collection-freshness.md) | deferred sketch → M4 proposal source |

## Implemented foundation

[ADR 051](../../reference/adr/051-full-pass-packets-own-guarded-captures-and-resolutions.md) shipped the first non-review artifact-version case: packet-owned captures, shared UTF-8 SHA-256 hashing, guarded comparison, and report-resolution validation. Full-pass owns its persistence and guard command; this workshop adds the **operational-store** baseline mesh for targets whose state has no natural owner artifact.

Review freshness today retains accepted `(note, criterion, model partition)` baselines in `review-store.sqlite`. v1 generalizes that substrate without changing review execution semantics.

## What v1 adds

- artifact-neutral target identity (`target_kind` + canonical `target_key_json`);
- path-keyed `artifact_snapshots` and `freshness_inputs` replacing review-shaped baseline columns;
- reverse selection from changed `file-text` paths to affected registered targets;
- optimistic baseline revision with two refresh paths (capture vs observation);
- `commonplace-freshness-status`, accept, ack, retire; and
- source-to-destination migration to `commonplace-store.sqlite` with `review-store.sqlite` retained byte-identical as backup.

Freshness selection compares registered accepted versions with current versions — it says the accepted basis changed, not that a claim is false. Referential validation (type-owned checks, verbatim quotes) tests current state and can prove invalidity without a prior baseline; that boundary stays separate.

## Ownership boundaries

| adjacent work | relationship |
|---|---|
| [ADR 051](../../reference/adr/051-full-pass-packets-own-guarded-captures-and-resolutions.md) | consumes shipped guard/capture; may share diff helpers |
| [lineage-mechanisms](../lineage-mechanisms/README.md) | vocabulary and storage-weight theory |
| [kb-graph-loader](../kb-graph-loader/README.md) | shared indexes for deterministic referential checks |
| [bulk-operations](../bulk-operations/README.md) | executes selected refresh at scale |
| review subsystem | owns jobs, pairs, evidence, result protocols; migrates snapshots/baselines only |

Out of scope for v1: full-pass rework, pinned-input machinery, automatic rewriting, semantic truth adjudication, refresh-job execution, collection-as-artifact freshness.

## Open decisions (post-v1 or proposal-bound)

- manifest-declared vs acceptance-only dependency registration;
- whether a dependency watches content only when the input path is itself a stale target; and
- how referential checks publish invalidity without conflating false assertions with stale derivations.

## What closes the workshop

1. review baselines migrate to the general store with parity-tested selection, evidence, ack, and finalization;
2. global status and reverse selection work over registered `review-pair` targets;
3. capture refresh, observation refresh/ack, retirement, and queued-job CAS behave per [database-design.md](./database-design.md);
4. reference documentation and an ADR describe the shipped mechanism;
5. [collection-as-artifact-freshness](../../reference/proposals/collection-as-artifact-freshness.md) proposal is committed (M4); and
6. [future-work-collection-freshness.md](./future-work-collection-freshness.md) narrows to a pointer at that proposal.

Then delete this workshop and remove it from the active-workshop index. Implementing deferred designs follows proposal adoption, not this workshop.