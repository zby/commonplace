# Workshop: artifact freshness and referential checks

## Question

What general mechanism should register artifact-to-artifact dependencies, retain accepted dependency baselines, expose repository-wide freshness status, select targets affected by changed inputs, and distinguish freshness from deterministic cross-artifact validity?

No artifact class is intrinsically a source or a derivative. A source snapshot, ingest, note, criterion, type specification, instruction, report, or generated index may be an input in one target and a freshness target in another. Artifact types may define different refresh policies, but the mechanism must not special-case sources or ingests.

Working design:

- [Implementation plan](./implementation-plan.md)
- [Database design](./database-design.md) — exact old-to-new schema map, review-first migration, transitions, and integrity
- [Future work: collection freshness](./future-work-collection-freshness.md) — deferred `collection-text` and casebook targets

## Implemented foundation

[ADR 051](../../reference/adr/051-full-pass-packets-own-guarded-captures-and-resolutions.md) shipped the first non-review artifact-version case:

- full-pass packets retain immutable `.txt` start-state captures under separate logical artifact identities;
- `commonplace.lib.hashing` supplies the shared UTF-8-text SHA-256 contract already used by review freshness and full-pass captures;
- the typed full-pass report records every guarded logical path, packet-relative capture, and accepted hash;
- `commonplace-guard-full-pass-report` verifies captures, compares all live inputs, emits `matching`, `changed`, `missing`, or `corrupt-capture`, includes diffs for changed text, and refuses unless all inputs match;
- deterministic validation rechecks capture integrity and report-resolution consistency; and
- the resolution and full-pass instructions require the guard immediately before packet-driven transitions.

The implementation is intentionally split at the demonstrated boundary. Content hashing is shared. Report parsing, packet-capture persistence, capture verification, comparison/diff results, and guarding remain in `commonplace.lib.full_pass`, with a full-pass-specific command and type contract. There is no general capture store, artifact-version service, or freshness target API.

That is the desired starting point, not unfinished foundation work. Full-pass owns one persistence policy and one response to net drift: a disposition becomes `superseded` instead of executing against changed text. General freshness is independently justified by repository-wide dependency maintenance. Its implementation may extract full-pass comparison or diff code where the shapes coincide, but shared semantics do not require shared storage or a universal `GuardedInput` type.

Pinned assessment input is not part of the shipped foundation. Full-pass methods still read live logical paths under a cooperative no-edit rule; the final optimistic guard covers later application and asynchronous resolution, not in-flight reads or the residual check-to-mutation race. Evidence that this rule is restrictive or unreliable must appear before this workshop adds pinned-input seams or stronger concurrency machinery.

## Remaining problem after the foundation

Review freshness proves accepted baselines for one purpose-built target kind: a `(note, criterion, model partition)` pair retains the note and criterion snapshots against which its evidence was accepted. ADR 051 adds a report-owned capture, selector-like comparison, diff, and guarded response. Together they establish the vocabulary and two storage weights, but still do not provide an artifact-neutral dependency baseline or reverse selector.

General freshness still lacks:

- an artifact-neutral target identity and dependency-registration contract;
- accepted baselines over the dependencies of non-review targets;
- a repository-wide status and selector from changed dependencies to affected target keys and reasons;
- acknowledgement that advances selected dependency versions while preserving the target output;
- refresh acceptance that records a new target version and complete dependency baseline;
- a target-kind-specific workflow for mapping neutral changes to reassess, regenerate, or acknowledge; and
- a storage-weight decision for dependency state that has no natural owner artifact.

Ordinary links may nominate dependency candidates, but Commonplace defines links as reader aids rather than obligations. A link alone cannot create an accepted baseline or prove that its target is stale.

Epistack eventually needs to detect a source collection gaining, losing, or changing a member even when no target has registered an edge to the new member. The planned workaround — a **collection source snapshot** via `collection-text` and `collection-maintenance` targets — is [deferred](./future-work-collection-freshness.md). The current implementation phase ships review-first migration and `file-text` infrastructure only.

## Why referential checks remain in the workshop

Freshness and referential validation resolve relationships in different ways:

- **Freshness selection** compares registered accepted dependency versions with their current versions. It says the accepted basis changed, not that a claim is false.
- **Referential validation** follows a type- or check-owned relationship to test current state. It can prove a cross-artifact assertion invalid without any prior accepted baseline.

Existing content-addressed verbatim-quote verification is already a robust referential check. It remains evidence that domain-owned referential checks can work; this workshop does not redesign its positional parsing.

## Evaluation boundary

The remaining mechanism must account for these witnesses:

- **Artifact-neutral baseline:** a non-review target records an accepted set of versioned artifact dependencies using the shipped text-version contract.
- **Global and reverse selection:** one check reports every registered stale target, while changing any registered dependency selects every affected target regardless of the path class or colloquial role of either side.
- **Collection source snapshot (deferred):** adding, removing, or changing a member will change a canonical collection snapshot and select registered targets; see [future-work-collection-freshness.md](./future-work-collection-freshness.md).
- **Diff-backed acknowledgement:** the operator inspects the accepted-to-current change and advances selected dependency baselines without claiming that a new target output was produced.
- **Refresh acceptance:** producing or reassessing a target records its current target version and complete accepted dependency baseline.
- **Target-kind consequence:** the shared selector emits neutral input-change reasons; the workflow consuming that target kind decides whether to reassess, regenerate, or acknowledge.
- **Relationship is not freshness:** backlinks and authored links remain discovery evidence unless a target acceptance registers them as dependencies.
- **Selection is not execution:** the mechanism returns target keys, changed inputs, and reasons; review, regeneration, agent revision, or bulk-operation workflows decide what to do.

## General contract under test

A freshness target adds this state beyond the shipped review and full-pass cases:

- a stable target kind and structured key;
- the accepted target/output version, where an output artifact exists;
- registered dependency identities, roles, and accepted versions;
- accepted baseline transitions for refresh and acknowledgement.

Acknowledgement means that the existing target remains acceptable against displayed current dependency versions. It advances only those versions and preserves the target output. Refresh means that the target was produced or reassessed and records a new target version plus its complete dependency baseline. Both operations record the exact versions inspected or consumed, not whichever versions happen to be current later. A concurrent subsequent edit therefore makes the new baseline immediately stale without requiring locks or atomic filesystem transactions.

The review-first migration uses one operational SQLite store for the mutable many-to-many baseline state and global selector. Authored artifacts remain files; full-pass packet captures retain their separate artifact-owned storage because they do not participate in this baseline mesh.

## Ownership boundaries

This workshop owns the vertical behavior contract for artifact-neutral dependency baselines and their interaction with deterministic referential checks.

It consumes rather than duplicates adjacent work:

- [ADR 051](../../reference/adr/051-full-pass-packets-own-guarded-captures-and-resolutions.md) owns the shipped packet capture, full-pass comparison/guard command, and report-specific resolution. This workshop owns the additional baseline, global-status, and reverse-selection behavior plus any implementation-level extraction justified by matching code shapes.
- [lineage-mechanisms](../lineage-mechanisms/README.md) owns the general dependency/freshness vocabulary, storage-weight rules, and any common operational state design.
- [kb-graph-loader](../kb-graph-loader/README.md) owns shared reading, parsing, and artifact indexes used by deterministic referential checks.
- [bulk-operations](../bulk-operations/README.md) owns executing selected refresh work at scale.
- The review subsystem continues to own review-pair lifecycle, result protocols, and evidence; the planned migration moves only its snapshots and freshness baselines onto the general tables in the shared operational store.

Out of scope: reworking full-pass capture/guard behavior, adding pinned-input or full-concurrency machinery without a failed case, automatic rewriting, semantic truth adjudication, a universal dependency-role ontology, authority ranking, and refresh-job execution.

## Open decisions

- Which dependencies are declared in artifact contracts or manifests, and which are registered only by an acceptance operation?
- When an input is itself a stale target but its content is unchanged, does the dependency watch content only or explicitly require the input target's accepted freshness state?
- How should deterministic referential checks publish invalidity without conflating a currently false assertion with a stale accepted derivation?

## What closes it

The workshop closes when:

1. at least one artifact-neutral target records and queries an advancing accepted dependency baseline through the general mechanism;
2. a repository-wide check reports stale registered targets, and a changed dependency selects each affected target with its accepted and current versions plus a neutral reason;
3. acknowledgement and refresh demonstrate distinct baseline transitions over the exact inspected or consumed versions for review-pair targets;
4. the boundary between dependency discovery, changed dependency, deterministic invalidity, and target-kind workflow response has a written contract and executable cases for the shipped scope;
5. Commonplace implements the operational-store storage weight for review freshness;
6. durable outcomes move to the appropriate API/reference documentation, ADR, validator instruction, and owning workshops;
7. deferred collection-as-artifact freshness is promoted to a formal proposal in `kb/reference/proposals/` per implementation-plan step 9 (M4); and
8. the workshop scratch in [future-work-collection-freshness.md](./future-work-collection-freshness.md) is retired or narrowed to point at that proposal.

Then delete this workshop and remove it from the active-workshop index.
